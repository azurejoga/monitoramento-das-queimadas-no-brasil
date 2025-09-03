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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4208ab7-31bf-3533-9b5e-4f0c22260194 | -18.69248 | -52.72737 | 2025-09-03 00:48:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ad9a75ff-e4ab-3636-90a0-cffb56ccc9c6 | -17.9283 | -47.18586 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 77d3ba32-11b3-3af5-b83d-4113ef89a2ce | -22.75998 | -47.2705 | 2025-09-03 00:48:00 | TERRA_M-M | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 30.9 |
| bfe0217f-63be-3411-8bbb-7c63e3c5cbbd | -19.38259 | -49.06892 | 2025-09-03 00:48:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 90dde50a-574c-3df2-91b9-5bf29579e2da | -20.89338 | -50.10596 | 2025-09-03 00:48:00 | TERRA_M-M | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| cc5f80e7-1287-31a6-a4ba-0de277557d49 | -18.65849 | -49.09901 | 2025-09-03 00:48:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e78f967-8e65-3d76-a364-a871960ddb3b | -22.70516 | -47.03659 | 2025-09-03 00:48:00 | TERRA_M-M | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 4c1ac8e4-753c-398a-9597-9d941957b204 | -20.40562 | -45.68734 | 2025-09-03 00:48:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c4408878-e74a-34d1-b923-5033c579d639 | -18.65708 | -49.08932 | 2025-09-03 00:48:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4df6b83-d724-3f74-9b7a-f0bfba699416 | -18.92158 | -47.57858 | 2025-09-03 00:48:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1375176-6dae-34f9-ae6d-94ec89667993 | -20.75248 | -47.13562 | 2025-09-03 00:48:00 | TERRA_M-M | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 76281567-3c26-323b-be88-986f133c16d2 | -17.9383 | -47.18427 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| db280c54-c7fc-32bb-8201-c410c98a4745 | -17.94748 | -47.24369 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6b7269e8-82fd-3882-a021-e54fcce26be6 | -17.93387 | -47.22176 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bafd2a54-01b9-3d82-8a85-52fd606242c3 | -20.8886 | -50.0937 | 2025-09-03 00:50:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| b14b8278-32b7-386d-b98a-ded9bd3cfc76 | -4.1604 | -46.7881 | 2025-09-03 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 1496754d-f5b9-361c-8c50-48bbae7d980e | -12.6341 | -56.9926 | 2025-09-03 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ca7217e0-8e27-3d99-81e7-7e4eaab791cf | -9.1949 | -45.1972 | 2025-09-03 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4d7bd991-a045-3ddd-9910-931125d92f81 | -18.6875 | -52.7244 | 2025-09-03 00:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 85237352-2770-33e2-bf2c-80b060ce5cd1 | -12.4889 | -47.4837 | 2025-09-03 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 62368dc2-e53c-35c9-8017-4cc6cc7dc1b7 | -7.7226 | -48.7355 | 2025-09-03 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 73602e0e-3cdf-3f6f-9d08-e7be881e53e8 | -5.6266 | -45.0252 | 2025-09-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6df06eeb-c876-34e6-a08c-ccceb8373417 | -6.4403 | -58.1186 | 2025-09-03 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9f372aed-de1f-3832-ba29-98d771af2e21 | -7.7039 | -48.7371 | 2025-09-03 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f63458b3-024a-316f-b64e-c2d595fa0a04 | -12.8436 | -48.035 | 2025-09-03 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c217f262-df71-3661-ab8d-7064552b8111 | -11.0181 | -51.5001 | 2025-09-03 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| a0864435-dfaf-348f-bbbb-199eb0b1ead9 | -7.7224 | -48.7572 | 2025-09-03 00:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cb656a16-faf0-3c03-bb53-2abbbbb07b51 | -11.0184 | -51.479 | 2025-09-03 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| d749850c-de90-3135-854e-6cce9b353c60 | -11.1224 | -44.6521 | 2025-09-03 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c5a4e2a3-10bf-3b6a-976d-7b83fa5df72f | -7.5477 | -61.3247 | 2025-09-03 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fa8bc06d-e53e-3e22-95a4-59cdaac7b8b7 | -5.6079 | -45.0265 | 2025-09-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 66869880-f4da-395d-a5f3-66ab7cd5c9a0 | -5.6081 | -45.0038 | 2025-09-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 9fbdfc5e-e9bc-38bb-b06d-5470ef995ece | -11.0371 | -51.4981 | 2025-09-03 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b5c1b23f-c52b-3d23-a65a-a957dcf156c2 | -11.0373 | -51.477 | 2025-09-03 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0777dda4-91cd-3008-af4b-b86ebd5ad7ec | -10.4853 | -50.346 | 2025-09-03 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 40493978-7995-3799-89a9-7e8b068c4645 | -7.7036 | -48.7587 | 2025-09-03 00:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5012c072-4aec-3e24-ae2c-3788254d32c9 | -15.5656 | -48.3918 | 2025-09-03 00:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1c8b2809-2c91-381e-9184-fc179ce98a8b | -12.6339 | -57.0127 | 2025-09-03 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6a7915b6-ab80-3581-b73f-a393c5b04b55 | -9.1375 | -49.6444 | 2025-09-03 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 24cf1b86-1636-3351-a39a-301b7ae455ca | -6.4646 | -49.5364 | 2025-09-03 00:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b79841f9-b6dc-3b39-8294-4c5496e8242a | -12.6531 | -56.9909 | 2025-09-03 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| c464824e-6d45-348c-8bdf-25af6a66518a | -7.0964 | -63.0625 | 2025-09-03 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 46bc9ec8-6854-389a-8b3c-b246328dc43d | -5.6268 | -45.0025 | 2025-09-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e08fc7d9-27b6-322b-ac93-38c48921288f | -6.4648 | -49.5151 | 2025-09-03 00:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 07106f05-b90c-3879-a53c-d1f529d008d6 | -3.212 | -47.1357 | 2025-09-03 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| cedf4c60-1126-3004-9bbb-d8fc39cbdb5f | -3.2305 | -47.135 | 2025-09-03 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 67463a9b-79ef-34b0-80a4-bc0e185fdb43 | -6.4402 | -58.138 | 2025-09-03 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 7172c046-4405-3e3d-8955-e83feb35c239 | -3.2306 | -47.1131 | 2025-09-03 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9e237d9f-dd6e-3298-9ac8-ed177c1fd343 | -9.3394 | -55.2277 | 2025-09-03 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 36a90431-2277-33ba-8886-2b8905616840 | -7.5476 | -61.3437 | 2025-09-03 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| e1677d17-48ec-37c9-afbd-70b7e3a3e5b9 | -3.2121 | -47.1138 | 2025-09-03 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d13df8a9-09ae-3cb2-b968-7b53950e0cfe | -7.5291 | -61.3444 | 2025-09-03 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e40864aa-9fca-3337-bb68-6436fd85a472 | -10.25249 | -51.16544 | 2025-09-03 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d940fee3-e58b-3410-be99-7c7460d7a994 | -14.97492 | -50.216 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6dfc013f-837e-3f1a-97e6-6974b3bf1826 | -11.01672 | -51.4929 | 2025-09-03 00:50:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 266a90d5-0f93-32c5-8884-9886839f22d4 | -16.55009 | -55.07479 | 2025-09-03 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| c4db38f6-66f9-397a-9393-b6121b4fd7af | -7.72433 | -48.74695 | 2025-09-03 00:50:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2389368e-1410-397e-9328-255d620088c7 | -9.94898 | -51.62515 | 2025-09-03 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1c75c713-e8db-377c-8451-8cc45a2ece8c | -7.1126 | -44.76602 | 2025-09-03 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| decbad3e-6226-301a-a08c-4e4158ba804f | -13.66957 | -46.94588 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2f5715fc-1419-36a0-b325-67ee65883535 | -9.63996 | -47.0367 | 2025-09-03 00:50:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dba11022-c470-30b1-8d31-bb1e4eed8cf3 | -15.89598 | -48.16131 | 2025-09-03 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 00f84e3c-08b6-34f1-9c0a-6c80ebc847fb | -10.54241 | -50.42366 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| e7192ce2-9b25-3699-a5b0-5c25d5280f3d | -11.59774 | -52.14879 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2963c064-a8d9-3b18-8819-996c71ab1fb9 | -10.97401 | -50.92406 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c772df7b-dfaf-3fa8-bc0b-ddd5e7fa19d4 | -9.72883 | -49.00274 | 2025-09-03 00:50:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 21756581-9567-3a1a-899a-49e15ceaec6a | -11.11609 | -44.62608 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 62e7fc54-286d-37fa-b613-5358d3e117f1 | -11.80645 | -51.53241 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 505f6109-42f7-3490-b572-bf763ca36c80 | -7.70878 | -50.26129 | 2025-09-03 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 15b1ea84-331d-34ad-be51-4c7f45178aa4 | -8.05158 | -52.36357 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3f6cde04-e29a-350e-a149-681bf1983c2f | -15.24891 | -53.80392 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bba7e1f8-7441-310b-aeea-302683f6fac1 | -13.09517 | -57.14178 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7a708fc6-59f5-3dbc-b836-0bcb7a2ec1d0 | -11.12004 | -44.64975 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 544cc3f7-255e-3d0c-a9d3-93c204cfe82a | -14.27031 | -51.23117 | 2025-09-03 00:50:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f38f2e95-8dca-3d4d-8b03-f2a2c53a277b | -16.86118 | -49.61123 | 2025-09-03 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7fc635e6-ee52-3d36-aca6-a0fc9dc00796 | -7.70128 | -48.73726 | 2025-09-03 00:50:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 63df2758-9ba5-3707-a6bb-c4ff8ca44224 | -10.49291 | -50.34166 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9d418dd4-53e9-3a6b-b31f-d0c0b184edc5 | -11.05927 | -45.39729 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1c7f53b5-fd99-310f-916f-862b51164bd8 | -8.86004 | -52.01908 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c3df6cf-aca2-3500-bdc2-b282c477a8a3 | -8.06165 | -52.37125 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7983620d-67ea-390f-ad6c-7bd0d4f1168b | -7.72242 | -48.7341 | 2025-09-03 00:50:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ce014d92-6e1a-3e0c-8ae5-b59661e68233 | -13.70618 | -46.94758 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 70201551-8b24-332d-a124-6d5dd3da2ebc | -10.08717 | -54.11275 | 2025-09-03 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a98810d6-3b8d-30bf-952f-a0df94fec977 | -8.83224 | -52.014 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea64b0d6-c9d9-3f81-b3ba-622dd5f12410 | -14.34512 | -52.79448 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49a48586-3006-3f5d-99a6-79c06bb633e2 | -9.14731 | -49.64363 | 2025-09-03 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5e04d720-7720-31f7-93db-a8695d971f49 | -11.02648 | -51.48513 | 2025-09-03 00:50:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f0bb727-3739-3dfe-b07a-a1d914e49fb3 | -12.86154 | -48.0371 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4b86bfe4-f139-34d2-bd33-f7231bc55ff6 | -14.96387 | -50.07436 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b731f26c-f087-3b71-b365-8f64f2ddf4ad | -11.79887 | -51.54271 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5a9a2a72-b791-31ed-8bec-10acdb7e4c44 | -10.26144 | -51.16411 | 2025-09-03 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 35f6dfef-0b0b-35be-84ce-7f014019b509 | -10.55158 | -50.42228 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 26f460c1-e3ec-377c-964a-7e48c551e279 | -13.46139 | -46.93691 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 49a39220-c69a-3851-b65d-0302b820475c | -11.59403 | -52.12191 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 778.7 |
| c630ca1f-fcea-3233-98b8-4571de2bb5bf | -14.90679 | -49.61871 | 2025-09-03 00:50:00 | TERRA_M-M | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 25925a49-0a06-3ba9-aaf4-69976b537f0c | -8.3698 | -52.53475 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1bdc508a-cf36-3209-ab6a-15d9dce394ed | -17.36049 | -49.17831 | 2025-09-03 00:50:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 398a6f59-dc90-3e76-849b-8d5c5ea905a7 | -14.61562 | -48.109 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 75d1655d-1a4e-32f6-a4ed-2ca1bace1751 | -11.05006 | -52.05534 | 2025-09-03 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d505d3d-0f6d-38a7-a3eb-a06806298ff2 | -14.54425 | -51.94832 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README11.md)
