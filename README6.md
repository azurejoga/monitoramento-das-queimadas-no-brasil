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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 003c415f-ba38-3a1e-9df2-c7d3681b067d | -4.47322 | -48.12571 | 2025-08-09 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ad623d35-c306-3c14-a9dc-2574e2bc97a1 | -6.58297 | -44.57128 | 2025-08-09 00:50:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 10839352-f000-374d-b295-616396fee785 | -7.25885 | -44.65771 | 2025-08-09 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1d2854e8-8bdb-3d74-a8e4-9e03bf5ad767 | -7.06015 | -59.20734 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 694.5 |
| da0a465c-75a7-3ca3-b8dc-de1f1266c8f6 | -8.0572 | -46.3157 | 2025-08-09 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 88c85828-294b-3f26-8000-684bbbb328f1 | -7.0689 | -59.21304 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.3 |
| fc8f8a0d-5c02-341c-a9ab-0533b2243e15 | -7.05728 | -59.18343 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 993.9 |
| e000ea39-a8b8-33c4-99d0-4ae17457cc09 | -7.07704 | -59.22972 | 2025-08-09 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 9f02154b-fc25-3f6a-aec2-2afa5db980d8 | -4.62572 | -47.41977 | 2025-08-09 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 54c46731-511f-3abc-bfbf-e3573d11dfea | -5.08958 | -48.3093 | 2025-08-09 00:50:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b31eb8ee-4292-3408-be8b-ae3948b31689 | -13.0778 | -43.83 | 2025-08-09 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 409bff45-f0bd-35a0-a212-ada730d76da3 | -8.9401 | -60.7288 | 2025-08-09 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 13de1035-24ec-35ee-8cdd-fe855f6d2a44 | -11.1074 | -50.5147 | 2025-08-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| e28366b9-1ffc-3c72-9425-af8d29db3bc8 | -5.2262 | -46.0642 | 2025-08-09 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| faca2ecf-8e68-3afd-8fff-27e736afb495 | -6.5856 | -44.564 | 2025-08-09 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3e0f0ec4-185c-328e-8ac6-ecfd95d1f531 | -17.5093 | -50.3023 | 2025-08-09 01:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 712.5 |
| 4f060f6c-6f45-3a2e-a8ab-0730ae96241c | -17.5495 | -50.2731 | 2025-08-09 01:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 61bcad35-4145-3b23-bb3f-ac791a2908f5 | -11.0887 | -50.4954 | 2025-08-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f1c1caf7-b5d9-3304-a6a4-21f5153f6b2b | -13.0584 | -43.8333 | 2025-08-09 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d53ebd0b-79b9-314e-a108-518e0e503dbc | -17.5296 | -50.2766 | 2025-08-09 01:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 589.9 |
| cc6e314b-218b-3899-a430-7dbb014c1783 | -17.549 | -50.2953 | 2025-08-09 01:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 24d92c8d-8ad4-38d2-9721-85c2d572d5ab | -11.1267 | -50.4913 | 2025-08-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3badf0c4-0842-37dc-b3bf-56d2ccc59724 | -5.2075 | -46.0653 | 2025-08-09 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cff6f11c-6e67-3e27-baf6-27de299bf8ab | -17.5098 | -50.2801 | 2025-08-09 01:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 528.4 |
| eacc226f-14c6-3a6b-8222-9fc3426bd111 | -8.9399 | -60.7481 | 2025-08-09 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| e56ba84e-4be7-3be4-8969-6b387f00bb15 | -11.1077 | -50.4934 | 2025-08-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| ab895b37-b57d-3399-b9a6-979233374f44 | -17.5291 | -50.2988 | 2025-08-09 01:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 816.9 |
| 7ef18616-c1f6-3b5e-8c01-d4653f5fe0e3 | -7.4076 | -59.9916 | 2025-08-09 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f6774ecc-1319-396f-9cd0-35475bbed3d5 | -13.058 | -43.8571 | 2025-08-09 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 84e77a20-850e-3ff8-8bf8-c1dbdca98f24 | -6.1326 | -42.9554 | 2025-08-09 01:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| afa996be-39cd-3ca8-b409-9033c689197f | -19.8328 | -47.0586 | 2025-08-09 01:00:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 9c629688-aa82-3d1a-96e3-7c694132a81e | -11.108 | -50.472 | 2025-08-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9f7bc62f-c060-3e8e-9052-6437e1cdb191 | -11.089 | -50.474 | 2025-08-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0448dccf-9f52-3912-aa69-3910637173c9 | -8.9213 | -60.7489 | 2025-08-09 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 6c8ef604-12da-32e8-ac51-d22021890c58 | -13.0386 | -43.8604 | 2025-08-09 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| fc506ae3-d334-3528-afd4-3c3a2cb20832 | -8.9215 | -60.7297 | 2025-08-09 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e4c7ae23-7f1a-3e2b-b051-94750fbd1651 | -19.8124 | -47.0634 | 2025-08-09 01:00:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 70750465-f4ff-3817-9ab7-3eecd544de8b | -13.039 | -43.8367 | 2025-08-09 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 28300ffa-7de0-3a32-801d-f455a105ff43 | -13.0778 | -43.83 | 2025-08-09 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3941112f-801c-3d70-8d2e-ad4483f7ad7a | -8.9213 | -60.7489 | 2025-08-09 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 1647bc34-f304-3ce2-ad2f-7f718e0efab6 | -11.108 | -50.472 | 2025-08-09 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 76e723ac-b9ba-3caf-9e62-f6734d49defd | -13.058 | -43.8571 | 2025-08-09 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 7caaeb83-403e-3e51-b02e-514c4749a47e | -8.9215 | -60.7297 | 2025-08-09 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e6c1b779-a424-33ec-b66b-ed092f8eb796 | -19.8124 | -47.0634 | 2025-08-09 01:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 538fb26c-ba1d-3305-93b2-364991a1ba25 | -11.1077 | -50.4934 | 2025-08-09 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 733c9d4d-6dcf-3328-a34d-663bbe89f495 | -19.8328 | -47.0586 | 2025-08-09 01:10:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4212e6f6-9600-31e9-9767-e8af8101205f | -13.039 | -43.8367 | 2025-08-09 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 5b74d212-8e9a-35b3-ba4a-060e93d5a3f0 | -9.5589 | -62.7238 | 2025-08-09 01:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8e07bfff-f731-332d-86c5-be3ad83746f0 | -5.2075 | -46.0653 | 2025-08-09 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a1c1629a-a645-35b3-9e87-b9d37c18202d | -6.1326 | -42.9554 | 2025-08-09 01:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 21336c9b-9357-3179-9e69-06b36c9953e4 | -17.5296 | -50.2766 | 2025-08-09 01:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 279.9 |
| 669ca432-6baf-3e1a-a817-1ff759078da4 | -17.5093 | -50.3023 | 2025-08-09 01:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 243.3 |
| abdb8944-9a79-3707-b4ea-826da5b40715 | -17.5098 | -50.2801 | 2025-08-09 01:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 236.2 |
| e14ca228-8aac-3755-b8b0-31a497e91322 | -17.5291 | -50.2988 | 2025-08-09 01:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 302.8 |
| 2292c822-4256-3a8b-96ef-194886017a99 | -13.0386 | -43.8604 | 2025-08-09 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 1d01bda7-980d-3afa-8c76-4c4b616cf89c | -19.813 | -47.0398 | 2025-08-09 01:10:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b14899d2-0321-3af2-8ee5-ad92eec8f905 | -13.0584 | -43.8333 | 2025-08-09 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6ad5b92e-ed09-33af-b2c2-417e17d0272c | -6.5856 | -44.564 | 2025-08-09 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 696266f6-3109-3a70-b145-098765cb9755 | -8.9399 | -60.7481 | 2025-08-09 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| fc9543c6-ac22-312b-9ebc-c5d82535f714 | -19.8328 | -47.0586 | 2025-08-09 01:20:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d712ea8d-6710-3778-8904-f0bdfaf48a59 | -13.0778 | -43.83 | 2025-08-09 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c7e9a7a4-6eaf-3f47-85f1-0ba480b21959 | -11.1077 | -50.4934 | 2025-08-09 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b9e9ba45-188c-3bff-90d1-041af3b252a1 | -13.058 | -43.8571 | 2025-08-09 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3220a234-28fd-3e2e-a690-b22b04bb908d | -17.5098 | -50.2801 | 2025-08-09 01:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1d3b2056-234a-3437-afe8-81a470338972 | -13.0584 | -43.8333 | 2025-08-09 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 1eca100a-4314-3aac-92ef-12cd19540ddf | -17.5296 | -50.2766 | 2025-08-09 01:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 54837ae2-9e0f-3bdb-9caa-d31c541722c8 | -8.9399 | -60.7481 | 2025-08-09 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| e36f80d0-ec31-346c-856a-68397b3d4715 | -8.9215 | -60.7297 | 2025-08-09 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e12537a6-0a18-382e-b1d8-22d62720d2f1 | -8.9401 | -60.7288 | 2025-08-09 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2d0e7fda-4d91-36bd-ba00-919fc8bd20e3 | -17.5291 | -50.2988 | 2025-08-09 01:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e09eb02f-4d6f-3eea-b784-e47e3d38fd4c | -6.5856 | -44.564 | 2025-08-09 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 3bc96698-ba84-3725-9030-88a628abdfb6 | -5.2075 | -46.0653 | 2025-08-09 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 72c35611-30cd-3937-9f43-e90cd986a806 | -13.5521 | -55.2633 | 2025-08-09 01:20:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d12eb3a0-a20c-3d9f-a9ae-38b1fe2edcc4 | -13.039 | -43.8367 | 2025-08-09 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a317cc54-6ab0-3be4-8d84-5a2e4e816a43 | -13.0386 | -43.8604 | 2025-08-09 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 513ef813-2d1d-356e-b942-110abc7bf3bb | -19.8124 | -47.0634 | 2025-08-09 01:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 48589c7b-0f5b-3e9c-9000-0d49f0244ea5 | -8.9213 | -60.7489 | 2025-08-09 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 6249796e-0bb7-3712-957d-2392f3b44aab | -17.5093 | -50.3023 | 2025-08-09 01:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 85dd89a6-1995-3ea6-bd23-fe03ef093190 | -17.5291 | -50.2988 | 2025-08-09 01:30:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8776bdf4-0189-3d3c-9944-08f06e71d384 | -8.9401 | -60.7288 | 2025-08-09 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d8b8c5a5-4c9e-3fbd-99e0-a405df061925 | -8.9399 | -60.7481 | 2025-08-09 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 78613f30-be7c-38a5-b57a-82ac95883acb | -13.058 | -43.8571 | 2025-08-09 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 447c911e-fdbc-31d0-9d41-015fe9fb4497 | -8.9215 | -60.7297 | 2025-08-09 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| af0f988a-147b-3b1d-baf2-87f4df2d53f6 | -13.0778 | -43.83 | 2025-08-09 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 756ce734-69c5-3e1b-a084-8df8c0cf77a5 | -5.2075 | -46.0653 | 2025-08-09 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d019a846-0e67-3dba-b7ab-466f5ee82589 | -13.5523 | -55.2428 | 2025-08-09 01:30:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 55b58519-7129-3a64-87d4-1131ee05fb51 | -19.8124 | -47.0634 | 2025-08-09 01:30:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 98b78b7b-b477-3124-8a80-e6e945b6e7ad | -13.0584 | -43.8333 | 2025-08-09 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4c783a1f-3c9e-3676-8b24-d7ecc070515b | -13.5521 | -55.2633 | 2025-08-09 01:30:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| a055a57b-c993-3ffa-998b-ab29c05435fa | -19.8328 | -47.0586 | 2025-08-09 01:30:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 69a39896-99cc-383c-a8f9-eb3261143ba2 | -17.5296 | -50.2766 | 2025-08-09 01:30:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 57e595cb-cab5-35f5-a270-1f3582012a47 | -13.0386 | -43.8604 | 2025-08-09 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 4f79324c-6d96-332b-b91c-5ff296237623 | -6.0498 | -43.7554 | 2025-08-09 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 2ed13ace-f578-3b89-9593-66b5614bdbe5 | -6.5856 | -44.564 | 2025-08-09 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| da6ddd45-3738-3081-afd2-0c9e4b93e30c | -13.039 | -43.8367 | 2025-08-09 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 8660a615-1e3c-30d6-922b-b69909edc49e | -8.9213 | -60.7489 | 2025-08-09 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 95dd7f89-e350-32b6-9870-352d03a92935 | -7.3886 | -59.9818 | 2025-08-09 01:35:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe1d61bd-2906-3465-8bea-822fc7fd23d5 | -7.4305 | -67.730003 | 2025-08-09 01:35:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 514eb3b0-1ef7-3a5c-8af1-fb2ab3a7853a | -8.585 | -62.646999 | 2025-08-09 01:35:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f4a4991a-f3cf-32fb-9746-c13278b9e7c8 | -8.9121 | -60.736801 | 2025-08-09 01:35:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
