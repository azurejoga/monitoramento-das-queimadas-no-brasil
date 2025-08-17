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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3d1fed-4045-3f50-a621-1cccda9eb8bc | -8.99908 | -60.52267 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e930762-8b9e-3dc0-bf88-ab666093702c | -8.98927 | -60.53528 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d5087a5-7b5e-3f80-ac8a-693057585dc4 | -13.59709 | -47.76139 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e37c0b9-0116-376a-99df-cdc7997cc398 | -9.18058 | -59.69242 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 836359e2-8bbe-39f0-b35e-b6a2a4495d06 | -10.84161 | -45.35175 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a7b00fe1-4907-3a8f-937b-3bcbafe5ec77 | -13.43308 | -56.93848 | 2025-08-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5a9dfa1-4fb8-3976-9b95-2dc19b3a4c5c | -12.60883 | -46.90946 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35983b89-e044-333f-9afe-03b06da488f1 | -12.50683 | -57.77646 | 2025-08-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c0d4321-b6e9-3760-a6e0-f634511ae9f6 | -13.60736 | -46.89599 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 33e1dabb-5654-3f42-b906-19b8a31e2bc5 | -12.86598 | -46.06407 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34e5eb31-3150-3140-ae29-a968994a2e23 | -8.98551 | -60.53467 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb56c1c1-3bde-3da3-9cff-719c3a1a6846 | -11.36495 | -55.41258 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68ab1073-78f2-31bd-af14-5266a2aa784f | -9.76762 | -48.75142 | 2025-08-17 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0f23b4de-a1a8-350e-b9a4-cbb3476921a5 | -12.2063 | -47.25207 | 2025-08-17 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f24f84db-1bb2-342b-8259-dd6a4856e50a | -13.42217 | -57.03144 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6f6d92-42e6-3a20-9437-2c045c163232 | -9.51243 | -60.52113 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7623b36-64ca-3d9f-9934-adc98d076ff3 | -13.58914 | -47.78147 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8a257f3d-020e-3f5b-afca-908de56c2e25 | -9.18386 | -59.65038 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7b049dd-c6cf-38d1-b3fd-394036bb92bf | -10.8467 | -45.3625 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1636ef16-95ce-33c5-99a1-f8b20a81c73a | -13.01405 | -56.85697 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 418c81ff-7918-32e1-af5c-a4f1c63f431e | -9.51013 | -60.55812 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce0d577e-5471-3c8d-b0a6-7f3f4829ed47 | -8.99224 | -60.52051 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fd28414-a4e2-3487-9722-e0b58544877f | -8.98851 | -60.53989 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85173eab-4a31-3378-87c8-44caf60205c3 | -8.23808 | -61.46618 | 2025-08-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e17b3e96-3111-3c76-962e-6ccbdf151314 | -10.00096 | -65.28784 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd319701-8150-3dd9-abc9-b50867e35ace | -8.97952 | -60.50064 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ceb8d4b-7f14-37ab-894d-7123ffc6d7c1 | -11.35808 | -55.38879 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ecc5957-fca6-3848-aef0-a3b33a17a81e | -9.9231 | -60.48619 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff4160a-69e4-3c00-9dac-a4e1c7212d22 | -12.14199 | -47.90719 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 172a2d98-cc10-3f5c-8ac2-de85fb2cd948 | -9.13784 | -58.29705 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18ff5706-f26e-3bef-90fb-b307c154404d | -10.31303 | -54.15764 | 2025-08-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 94026978-da86-35da-996c-a0b6b75ef9f0 | -12.88929 | -46.12994 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74f10de9-f28c-314b-a1da-599c20816a86 | -8.99535 | -60.50229 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ff80ca-02df-366e-8b1d-65816ce77472 | -11.37118 | -55.41733 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e181797-e94a-3dca-b856-ccf6b261c7ab | -9.51839 | -60.53147 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df91edcf-40db-3794-8361-f244813d5466 | -9.50341 | -60.55228 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf6b66cb-6c68-3f60-a821-2a2dd16c22c0 | -13.01074 | -56.85644 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f057d9fb-9b18-3787-88f4-bbad8a3af4f8 | -9.15863 | -59.62515 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ebf5c8-bfae-3a96-9114-fa5b2feac9b7 | -9.16289 | -59.62163 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39c9f1a0-21d1-38df-99a2-e960de45de7a | -9.9261 | -60.46835 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b373d1c-1494-3a5d-a008-852b59977f5d | -8.99756 | -60.53191 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eae0cd76-dff4-35e2-96b3-8bba263449bc | -13.43609 | -56.7855 | 2025-08-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93d80137-f8a6-3129-887c-e5b379aa9915 | -9.14182 | -58.29391 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2826f7b-1c67-3bf6-b7ca-9b67b064cfc8 | -9.22034 | -59.65229 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13c3fa10-566f-3c98-94c8-b7524d0bdde1 | -8.11611 | -61.19055 | 2025-08-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9d097eb-7708-34ed-b01b-16177bf07f7c | -12.57511 | -47.05118 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2addc6f8-b3ac-3c2c-8674-fac562bbc701 | -12.4509 | -47.00322 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2661412f-f069-3296-b2e1-6f6feac5981a | -13.63507 | -46.9086 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e57bac58-496c-3097-a92e-0d6f51c7f3e6 | -11.41234 | -55.3516 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6949be98-f579-3c75-adcf-4fe1d2cec7ca | -8.87176 | -68.5065 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12678558-a988-39d6-8f34-ebfc1d7cfbee | -13.00742 | -56.85591 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9447fa9b-1073-3322-a8d4-5fb8ca36b851 | -14.19024 | -45.3171 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf98eb1c-61f5-3aaf-9998-0d1124857d01 | -10.11308 | -57.76629 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 727a2141-e746-3565-b070-bf0e0dfd6cd1 | -12.13786 | -47.92014 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c6fa2a1-0520-36e6-9e25-48a8a39db50a | -11.36148 | -55.3893 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| dd33de29-5343-3b2c-83d3-422402b80d09 | -9.22527 | -59.64462 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d6694df-f9c6-3894-9ed3-bde8a34b0ba3 | -9.50346 | -60.52888 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 377e9e12-2361-357c-ab25-f5e67215889f | -13.43327 | -45.89653 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 382a5385-c845-3218-a73d-84bfb4c4d428 | -8.87805 | -68.50779 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63a28fec-7f02-3064-9b34-d9c9d098cc14 | -9.18317 | -59.65452 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4bfbeeaa-d67a-3946-9ced-4f490879fbac | -9.55366 | -63.66174 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc0dccd4-48cb-37fa-b10b-f3e7e7572199 | -14.93841 | -47.0616 | 2025-08-17 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc309d0b-51e3-39be-b05e-91be515f979b | -13.62812 | -46.91791 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 887e7122-20ea-3142-a9ea-7dc1ac3aa290 | -8.88073 | -68.51366 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ada98d8c-0033-3b61-b231-3f074259f38b | -8.98328 | -60.5013 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da8753ac-1ca9-3127-88c6-145c6b3962da | -11.56997 | -47.26485 | 2025-08-17 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a62de31d-4e13-327a-a5a1-f7e8635f516f | -8.99155 | -60.52145 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f2c8c65-80eb-36b7-85c3-e56d9b752f36 | -8.30821 | -55.10669 | 2025-08-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6311f64-7d04-3aa5-9632-846859ed64c2 | -13.60797 | -46.89058 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8108d8e8-3a48-31bb-be08-a50db6c9ff49 | -9.62457 | -65.36974 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79a60391-caf7-3415-b041-afdc9d40395e | -7.21552 | -60.38295 | 2025-08-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb90951-3de7-34e0-9352-f83e83a22678 | -9.61323 | -65.37402 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d050cca-ea03-36d3-b324-1f7e77485a55 | -8.99741 | -60.53555 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 877a4c4d-aade-32af-966f-9ccc8e6e2979 | -8.99379 | -60.5313 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c50d1ffb-c34f-3077-aefa-8bb240b5bb39 | -13.43585 | -56.94258 | 2025-08-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5500a7a3-5fc6-3dea-81a1-a5a8d11f4f0b | -12.84926 | -46.04757 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13452579-1da8-3acb-a387-80fe7b6d71fb | -9.22101 | -59.64814 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3662c7f2-92fa-30c3-9ecd-eaf298854757 | -9.39579 | -60.54539 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f57c3cc4-ab8b-3fa3-814f-26f0e6999a2d | -9.21744 | -59.64754 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ae99236-62ed-30b2-b2ca-246ac8e83046 | -9.51465 | -60.53084 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| babb411d-dde2-3ec5-8012-7b2f611ed762 | -9.18522 | -59.64217 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58f68c6d-2370-34e6-bf60-c571ca7a0d87 | -11.36779 | -55.41681 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 354086ba-78b3-3e60-8203-b872685fcc5d | -9.19173 | -59.6473 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a47c81f-501a-3886-b6ee-2c34644506ca | -8.99455 | -60.52668 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79f52fba-6b90-3b5f-a270-605275f06d07 | -10.84127 | -45.36623 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 981b6132-0e2a-3975-8217-bdca05e17d34 | -10.84217 | -45.34678 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 93f68ba6-8426-39da-b01d-aec2e6592dd8 | -9.14463 | -58.29815 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a60f89-3dfb-3500-9b5e-1b2a66d2b3c2 | -12.55656 | -46.94654 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54cc77ac-3541-322b-987d-e0664d9835e9 | -10.84273 | -45.34185 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1bb16ea8-8da7-338e-bdee-848d95b43d41 | -12.99691 | -56.85788 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5af5df83-6b25-3d3e-b44e-3629ef1b0675 | -9.62401 | -65.3728 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 027f62bf-f912-3e1c-8c4b-cdd4e3f67c75 | -11.70088 | -51.6371 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18dd1dd9-0246-3172-80ed-73478d0d44a9 | -13.59208 | -46.97834 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9caa4967-d455-300d-b309-f3477949e3d0 | -8.98702 | -60.52545 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 853ebea7-daf8-3681-97a3-6010126e3816 | -14.58912 | -47.95113 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afc6498b-f59b-3be7-860e-2361a5e4691b | -9.21811 | -59.64341 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 368cab34-205b-31f4-9d15-ec978c92a1ce | -9.18776 | -59.69363 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89f0f8e6-9878-3c99-a5e0-071432829c3f | -8.99457 | -60.50686 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af8a538b-20b3-3fa4-9a46-1640732626d4 | -12.83921 | -46.02667 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e21fb3b-7ddc-3f1a-947e-7584f71c1764 | -9.20415 | -60.82999 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README27.md)
