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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0aeafaf-cf23-35f1-9c2c-a74ba4205605 | -11.10895 | -51.43606 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a3deaf9-6de2-3da9-ad0a-a32e6ea03ae8 | -10.53825 | -57.10897 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09cd6a0e-fad7-390a-af0e-6402bb4a8b67 | -10.16178 | -64.72868 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 771bbe16-62cc-3b96-80dd-303b916f15fc | -11.82238 | -50.55141 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f72a5a71-495d-386a-b39d-0c4c6c8d438f | -10.33757 | -54.31301 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 450ed44b-0129-38a7-a26c-12fff29d96a6 | -14.38784 | -60.30802 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 471b5ec9-481c-39b3-9420-bc0f32cf4a7e | -12.97231 | -54.75168 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945fd040-e825-344a-b748-2a213862f876 | -12.12083 | -44.85015 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac49b451-d41f-38ed-a34f-5ef4c77a517d | -15.12271 | -52.4985 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ee2de8b-5eed-305a-a190-33c95e5c4c1d | -10.70918 | -54.44017 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0a14fc5-00cc-36c2-9027-8b3a83cac1e6 | -11.99632 | -47.75656 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aa57a174-9771-3fc3-a000-45a18e028bd3 | -11.42667 | -45.62036 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| fda359d1-a90a-36ea-9cfb-4af1aad736b9 | -11.03891 | -51.40965 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0745ecc1-3690-3a6a-b2a7-b0361bc78871 | -11.44667 | -43.57182 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc3a37d8-c2c8-3345-84ee-21de80b10084 | -14.20878 | -46.23233 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20980be1-6cc0-3b98-93e4-ae06d408e263 | -11.10208 | -51.95407 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 153b4f8a-4095-3bc1-95ea-dd2f4021b4e4 | -9.25962 | -59.40111 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bfc38574-f8dc-3a8a-9db0-47de766b2b2e | -11.86098 | -50.58155 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bbfb995-cba2-3f6b-93ad-c36b18c6d20e | -9.90977 | -57.06059 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 660df703-0059-3b8d-b0ed-a33b8fa6fce7 | -14.43786 | -48.41721 | 2025-09-13 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2307d02b-0589-3537-aebf-73db53bbee16 | -10.77016 | -50.51558 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54dc6e99-d0d1-3d01-9c7c-daae7c83a478 | -15.21002 | -56.68351 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5ca4c2-3c21-3c36-9f9e-d400513377fc | -15.05834 | -48.00949 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d515465-8781-3b91-acab-3e6abcea5119 | -10.36751 | -50.49844 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b2656a0-9d5e-3874-a699-fe8e4d43eddb | -12.95659 | -47.98169 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9422dd3d-6659-37ae-98d9-0f4e7a38efef | -15.57654 | -54.7741 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13e1775b-ff98-30a3-bdd5-f3fb4baec65e | -10.15319 | -64.73253 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 05058e55-1cda-3582-8d97-ff711b2ce676 | -11.16286 | -50.71123 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 678e63f0-767d-33dc-8394-827f82fb1be6 | -15.05895 | -48.01104 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 058206d7-3bcd-34e6-a2b1-36013bba4b1b | -15.28995 | -53.7803 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6e5cabc-8e32-3c26-8960-55742376743d | -15.86529 | -51.8577 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92023403-7b2c-3b25-bff8-2f325d9c236e | -14.28774 | -46.07938 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9be104b3-fed9-38b0-957a-c0f78c238ba4 | -9.27425 | -59.40855 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75326840-5474-3c82-bff2-a3ab330b6d66 | -15.16444 | -52.48399 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a6fcb43-ea8a-3fb0-8636-3d2552a8a549 | -14.20132 | -46.24598 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96a6ded6-ee64-31b2-807b-804b8d2bd57d | -16.40019 | -49.06896 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c8d9f81-e4b6-39ea-b731-07a03b007a21 | -14.22789 | -46.30894 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b8631914-4fec-3549-b8aa-0cce685aed8b | -10.10128 | -59.15791 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2eaf95b-2749-390c-b39a-866e681bc279 | -12.95525 | -47.99257 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81a2809e-2d04-3309-8c72-8176af1a61d7 | -14.43517 | -48.43901 | 2025-09-13 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da53d3be-aa16-3539-80c4-47ef0edd98d0 | -9.27718 | -59.40155 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a6924c3-5790-3dc0-9966-9175708611bb | -14.28902 | -46.06812 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2970864-4564-3263-a4bd-d11d47259321 | -11.81085 | -50.54612 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb59c78a-64c3-38dd-9e78-a94d59164cd3 | -14.22871 | -46.30166 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9b6528d9-ed0d-3f04-8e5e-518a33fd3973 | -15.28938 | -53.7843 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2e5cc7a-f1a5-3515-9830-387461ac060a | -14.63495 | -52.09092 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cacbb8c-41a4-3abe-95cc-944487466272 | -14.21017 | -46.26802 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7823878e-8552-37f4-8af8-bc1316510d2c | -11.27283 | -51.12506 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a49d6d4-dd5b-31fd-97c8-b236c3512f36 | -16.55393 | -49.21736 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82450f24-126e-3f90-8958-fbc1c5f3302e | -12.80936 | -47.9558 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 741015a0-1072-3c73-8c6e-d5ba4ffbfccc | -14.20447 | -46.26883 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 110f4478-0281-317a-a87b-9b2dcfcc3092 | -11.41398 | -50.74796 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc3b6632-43f9-3536-b5fc-dbf731168f6f | -9.26187 | -59.41146 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| b616f6de-507e-3fcd-88d3-666050f5c690 | -14.2018 | -46.24387 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18b0d006-fc6c-3737-a80d-32c484bccaff | -11.25304 | -61.56786 | 2025-09-13 04:59:00 | NOAA-21 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88d0d436-e1d3-353b-ab6f-2c8fd6ff1266 | -11.23192 | -49.98865 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad01466a-f667-32d6-92dc-ef725ac59859 | -16.25076 | -50.06682 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aef46a3b-abe1-3082-bc95-f252cdf9f148 | -10.33425 | -54.31249 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ec7c1b8-225a-3a52-bb29-2ce3ed53e001 | -14.59654 | -52.52326 | 2025-09-13 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da8f7f8b-3784-35f7-b097-eb6349a31a91 | -9.27744 | -59.38919 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abb130a-6896-3f93-b29e-f16fbf2f5c8b | -14.19906 | -46.26653 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 926ca26e-88ed-3dc2-a978-ba9464c726f9 | -10.88063 | -47.2383 | 2025-09-13 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0fd208ef-d022-363f-9598-a4430d187b8f | -14.18699 | -46.27454 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f88f66f2-6677-3029-b254-3ce7bfde6ed8 | -11.06041 | -51.50858 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b820a78-f511-32a3-b5ec-eaf7157067d8 | -14.21031 | -46.26601 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee6ce1ce-76ce-3925-b383-3514631b9476 | -11.3817 | -47.30419 | 2025-09-13 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5de6d409-0d4d-36be-bd97-c9f405550f4b | -10.42531 | -50.62923 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d2cac8f-ffe9-3df6-bdd8-e42144e65b73 | -15.54981 | -54.80532 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 626172e1-bd8c-3baf-8f72-6dd7a8b034d5 | -12.85396 | -47.9453 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9721b267-c65b-3eae-94f3-997dbd039320 | -11.11144 | -51.33679 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 30133461-4450-3a01-9740-99fe32d89a68 | -11.76733 | -51.51012 | 2025-09-13 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6ba6659-bba0-36a9-92cb-f7261c763cb9 | -10.42082 | -60.80003 | 2025-09-13 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31aa9bd5-4d3e-3428-9719-1c16093b7add | -14.22059 | -46.27433 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32f92e7d-6c59-3ac0-96b6-80eff8172799 | -14.6975 | -45.15314 | 2025-09-13 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 780a8011-599d-397f-9120-20844b1737ac | -13.89357 | -48.2868 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 371a526e-5c8a-33b0-aa72-414c1600a062 | -10.33242 | -58.02325 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76ba7b35-1a8e-3c8a-aec1-fcc1c1e9b0ca | -10.7 | -48.6486 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 128dc7e5-b107-3009-ba37-c3ba4f1eb4e0 | -13.78063 | -46.29467 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38020af0-aaed-3bbb-9579-ae5b86e2d752 | -15.59625 | -54.75797 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7684aa72-213a-3ff8-a203-6f218be5adfd | -11.57508 | -50.56947 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 10e56c5a-2ea2-3cb0-9f2c-c06d3760b07b | -15.14098 | -52.47689 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 864d2fb7-399b-36e2-ac9d-20514e586f12 | -14.19746 | -46.28096 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f1282e5-6b58-3904-8773-f90260d618d4 | -15.86769 | -49.94271 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f05ef868-ee0b-34a1-a5a2-3577c42648c6 | -11.56661 | -50.57181 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 795a5f73-7e13-3fbd-be33-3605e664d403 | -12.12066 | -47.58964 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82c68946-0e04-3463-ac25-24b6187e26db | -11.36676 | -59.14544 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f748ac97-360e-3d0e-8698-298e5fd0051e | -11.93637 | -51.13548 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fa6edc2a-30e2-3b69-ac01-be9e6f201ba3 | -13.00431 | -44.11619 | 2025-09-13 04:59:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04edf839-c8fd-3a13-bb42-6a0b57a3aa53 | -10.46416 | -50.60843 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb8e3b1f-b442-397a-99eb-034424761024 | -15.23227 | -56.32595 | 2025-09-13 04:59:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df4ac897-c854-3fd5-9660-015811955914 | -14.19338 | -46.2678 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 085ceb30-cc98-3741-ac73-1d06f868677f | -11.81787 | -50.55437 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8c8d5c89-5fa3-38bd-b85a-ac55bf921b36 | -11.18529 | -51.41645 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 82eb7b97-f239-3d6c-99ec-6caa2dd4ff45 | -9.79477 | -61.51312 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ad951a-1c50-3423-9471-146de7a3c956 | -9.90916 | -57.06433 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e4dabd-6eb2-3855-9015-803fcc8a1b53 | -11.08949 | -51.43787 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 52dc9848-82c6-3998-86bf-ee6ea8f300d8 | -10.50947 | -51.54894 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a46e3d1f-920a-3f41-89a7-88e6ae2f0c6b | -12.12137 | -44.84569 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8be53f4f-ac21-3964-ae4c-f401bd85a33b | -11.73484 | -44.21312 | 2025-09-13 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ff46ab6-28fd-3386-819b-fb426ce8141f | -12.96951 | -54.74755 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README86.md)
