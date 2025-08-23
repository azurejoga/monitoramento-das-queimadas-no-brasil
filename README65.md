# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f32e3c4-b04e-3ace-8e4a-6d80880cbf4f | -9.2028 | -59.46609 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e6226f2-31da-382b-a89e-6d35be50e119 | -15.01331 | -54.88705 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e10394e-4335-33bd-82a4-11e59a4cb9f5 | -15.02873 | -54.88858 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b62cea7a-2854-36e8-8682-d28347d7b635 | -9.47508 | -57.82412 | 2025-08-23 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b20fcf91-fc28-37fe-9104-201de645e9e7 | -13.02489 | -56.82389 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f121c47-7aae-387b-8d91-5fcd4918be4c | -7.29721 | -59.62339 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e899895-ffec-37c8-a516-cd530a2ae390 | -8.89256 | -62.43145 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb0b6899-b8ec-3890-a451-4e6d0b4855b5 | -13.03164 | -56.82943 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e2cf6bb-39e7-3f06-9b5f-bb211a2acdeb | -15.2244 | -53.85711 | 2025-08-23 05:21:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56f18d97-89a8-3ae9-9031-60e82af97e98 | -9.52701 | -60.55805 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c783d21-de13-3012-b912-2b4d120c8918 | -7.29388 | -59.64441 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1b5833f-9376-38e3-bac7-c2990a950181 | -9.71688 | -65.7161 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890fe9d0-8b01-3b48-bac1-fcfa9bb44824 | -9.24774 | -59.61299 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cfb543e-0908-32a4-a1a3-5b97faf0647f | -12.49225 | -53.81854 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dddcbdb5-b4da-3aa0-a33f-3cab36e28f88 | -9.25063 | -61.02133 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f5ae7b-853e-350a-8ac1-cc8b6d21e2da | -7.29499 | -59.6374 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85e38dff-56a4-39d2-9e3c-f59cb163936d | -14.62285 | -54.81581 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0329e701-7b36-3d6f-ba69-e63e11dc55fa | -8.88828 | -62.435 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7366c6e-f6c2-31a2-aa1d-0f230e1cb143 | -9.51316 | -60.51552 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b1783b2-3450-33b4-b935-4f42d2ea6914 | -8.44365 | -63.86096 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ba282e2-5a3a-32be-878d-1a865c2fed86 | -6.94222 | -59.64204 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5b5bdc3-3496-3d8b-945b-3ce63d21e591 | -10.64626 | -50.12466 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d76860a5-305d-35d0-ba88-b613cbb6af98 | -8.68041 | -62.87906 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2da0258f-b4bb-3484-8d6c-a0c567042c75 | -8.90336 | -62.43328 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4864e5b0-3215-360f-8e95-9a49a10afac9 | -9.20225 | -59.46958 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c433313d-c956-3d07-af61-18fbf67baba3 | -14.658 | -56.60936 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03b3661c-9c49-32ed-b5ca-765ad1e334e5 | -9.20168 | -59.45158 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee1deca8-ef16-36ea-9bc3-931e8cb14bc1 | -14.61292 | -54.85865 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baa0f699-d81b-3fea-b277-f1cd3676995b | -9.9439 | -60.16739 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6df8dc51-05ae-3968-aeec-057f47126642 | -9.95554 | -60.18011 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe9342cc-e5e3-3690-a167-dfdf199a62af | -9.21205 | -60.7837 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c51a2478-3a39-3e9d-bb68-ed7001141ecc | -9.37475 | -48.25066 | 2025-08-23 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e44bf6-5681-38e4-b940-a6f5849d82cf | -9.5076 | -60.50729 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ad77480-37ca-3107-acd8-1cf5935f5b72 | -13.02845 | -56.87843 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bb1d5a1-d0a8-37b7-b0e0-9b7540bce79b | -9.96879 | -57.97055 | 2025-08-23 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e59b5618-1003-3494-89d5-a9da6e0cfd48 | -14.76015 | -56.05164 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23a4c262-52e2-3af8-a4b1-c417071e5760 | -14.66375 | -56.58873 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b74e4e6-2fa5-3500-92b2-1b1de54b5a04 | -14.28489 | -60.38029 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b2f2bd6-2555-3f4a-87a5-baeab04b6474 | -10.6458 | -50.12831 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c7debd1a-061a-37c8-8dda-982ea449385f | -14.94099 | -48.01288 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6c3819c0-9a75-3852-8321-3585fba6fd7c | -14.61121 | -54.80528 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75abafec-1cc0-35d6-955f-633d51b6ee79 | -8.53335 | -48.85926 | 2025-08-23 05:21:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80a61cbb-8880-30a4-891a-425be85c6f2c | -9.22889 | -58.45441 | 2025-08-23 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c1a8a7-2a68-3d99-b90d-7c08a55228ec | -14.66585 | -54.91517 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2bcbb417-8924-3a75-af3f-9dac9b41432e | -11.51245 | -50.47591 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67f9bebf-45e1-334b-b754-3f41fbc1ac0a | -9.24115 | -60.47533 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a1eb27b-b3e2-350b-8bcb-3dd99a855f94 | -10.6292 | -52.34631 | 2025-08-23 05:21:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38f0841d-5e9a-39f1-be08-56f0216e2072 | -14.70017 | -54.91413 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78f020f2-d934-33bf-ab48-a47e0b18ce63 | -12.317 | -49.99902 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb1a3767-8e85-37b5-934e-8745c9d22868 | -9.95273 | -60.19772 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 0c8f0304-ce8b-3a87-9a94-85d9c658d4fd | -8.88039 | -62.43793 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5f54e8e-e18b-3be1-82d7-7c5b50b69384 | -7.43493 | -60.62549 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41aaeb3b-95e7-3ddd-82a2-c4ebca07af0f | -14.74867 | -55.99581 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e04ada2-68cf-3e6e-838d-75fe457af0e6 | -14.67454 | -56.59516 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7173698-0b2f-3e5b-ab9c-be86c2e7d608 | -9.92414 | -60.48335 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d388c38-6194-35b6-a127-948ebe68e19c | -15.71775 | -48.21014 | 2025-08-23 05:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dee5f8a-6328-319e-9f75-a9a0ce4bc201 | -9.81798 | -64.26669 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a204d6a-8330-379b-afb1-a6dd449817ce | -9.95386 | -60.19067 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| eebda302-6760-3976-9a86-910ce6c1431e | -9.51359 | -60.55587 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a11bf37-1811-3f4f-aaa8-761518db3dec | -14.94467 | -48.00709 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 900f0b11-dca1-3036-80d1-f12e6bc6ee3a | -11.51291 | -50.47236 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43c8a70f-c57a-35e8-ba0c-0fa806cabd10 | -9.47452 | -57.8278 | 2025-08-23 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a82a437d-07f0-3c9c-b6e6-111c40bc0464 | -9.84207 | -64.29186 | 2025-08-23 05:21:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceb63780-6f37-367e-80d0-dbf6ab7775cb | -9.19006 | -59.46047 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beac9682-c6d6-3b8d-a6d9-f8d8bea46cb4 | -7.56649 | -57.66927 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea2c07f5-4e11-3827-a8c8-ceab78ebaaa8 | -10.75506 | -48.24791 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d30aa84-317c-3676-8893-660570440cbf | -10.71297 | -62.7432 | 2025-08-23 05:21:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01f19fc7-f76a-3664-931c-3a0a40166558 | -6.87241 | -59.82196 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b524fcd7-0a62-391f-a925-9e3c7a62770f | -7.50985 | -63.83881 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a1b79ba-f0e2-348d-9a8a-aae54a781962 | -14.68086 | -56.60574 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d9b8437-1890-3e18-a7bd-e28a378494de | -11.61856 | -50.43046 | 2025-08-23 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dadf069-636e-3b5d-a068-b1bbe2eaa53d | -10.55213 | -62.73951 | 2025-08-23 05:21:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c623ead-efa8-3fb4-97fb-a478ce73ad9d | -10.63935 | -50.13486 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 783e6b7d-e00e-39ff-a681-223ad8f37ff8 | -9.95944 | -60.17714 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e33b4e5b-ef4d-3226-9eb8-405ad86bccb7 | -7.43833 | -60.62604 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 498c27d4-de90-3af1-8427-3d66040d0b14 | -8.88896 | -62.43085 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c532b56f-b6d3-369f-b209-1090fa85ad85 | -13.48101 | -46.90232 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 12cbb9ab-c88d-376b-9de7-59f72e84e7dd | -8.60124 | -62.6144 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aaf5542-c417-342c-bcf0-826ba3c09e79 | -15.21921 | -53.86127 | 2025-08-23 05:21:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6435c0d5-a569-3cb1-971e-0483ad6c3046 | -11.30498 | -55.14427 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d8adc2f-8691-35f5-8766-cec179d2323f | -9.1652 | -59.59617 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 885da83f-bdb0-3721-a446-232b91ca9a79 | -9.18071 | -59.62732 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99c9da21-23c0-367e-a4a0-a9f3bca071e8 | -14.67008 | -54.91573 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e7e1e045-5757-3237-8b8d-23a17f15c564 | -9.95165 | -60.18309 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 44ac1dd8-da3e-3691-909a-9a87eeca92fb | -9.1846 | -59.64582 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4415643c-89ba-36fc-b2f8-99937e23d61f | -9.51987 | -60.51662 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1a8f69-9e66-35f5-b2ce-ae5b5059c18f | -15.71715 | -48.21608 | 2025-08-23 05:21:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36159216-044f-3a86-81dc-d8d4b35728ef | -13.48278 | -46.89789 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6387c8c5-9f50-3414-bff7-4905b0af27da | -14.26068 | -58.53818 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7881a35c-b5c3-35a4-90d3-269fca6f59d9 | -8.8466 | -49.85997 | 2025-08-23 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 064c0888-1d29-397a-be36-b56e2dbfa3ba | -9.95611 | -60.1766 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98acbaff-6d88-317f-9ff7-5669e09b8a73 | -9.18017 | -59.69527 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f2544c-278a-3542-b2c1-18729e0eda92 | -8.89391 | -62.42317 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28a1d86e-4f1e-3bcc-b5c4-134e4da9d417 | -14.60859 | -54.82542 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ebf8ffd-f5fd-32f5-aa1e-dbec0937cc3a | -14.30618 | -58.5527 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ebe7f11-daba-3e1b-b026-fd6d60fd3b1f | -9.24394 | -60.47944 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 298e3746-8b2f-3312-ac69-2ca3ef51db00 | -9.23161 | -59.75369 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e81376b-05ae-3047-84a7-3ef2c787c0ab | -9.1857 | -59.61737 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9742435-d546-3696-a827-4452a5c2168b | -10.64534 | -50.13195 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4936a262-a175-33ff-880f-a8d5e95fc835 | -15.69858 | -48.09313 | 2025-08-23 05:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README66.md)
