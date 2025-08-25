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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b283195-7d95-3625-a505-fd7ed69a5545 | -11.18493 | -55.03255 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9ad9013-cc86-3efc-aa7c-98cf39733af3 | -9.25903 | -59.77379 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ecfcd29-9110-347e-b17e-e6eb3656ebd6 | -10.46676 | -48.32491 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9b40b47-f43f-387a-a90f-456e55f4b3d3 | -9.06717 | -65.71559 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d72ad6a-eca0-375b-869a-a2dde33bff98 | -6.82181 | -58.9539 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ce4de1d-f62a-36d9-ac3f-17a2a9133a6b | -8.90399 | -62.46452 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f51177d7-660f-3ff4-bd14-4f887ce4d616 | -9.1745 | -59.60587 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2dfe19df-95ba-316f-9d33-8fce00c28dc9 | -7.09186 | -44.63026 | 2025-08-25 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6b84e15-4fb4-3f20-87d6-c99af2f2509b | -6.83785 | -58.95907 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| afe511bd-b575-3d55-8a33-b8b79fbbf648 | -8.12196 | -62.87753 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfacc1b6-ac70-38ce-9d1e-4642bd3c1d07 | -9.52026 | -60.51353 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b166df65-be28-3976-a435-5cc78dd63fe8 | -8.58574 | -62.63432 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38269b2-19b4-347e-a663-12ee0a0f0b5c | -10.10332 | -57.7645 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8702bf2-25e9-3c08-a076-616045a64520 | -8.87756 | -62.464 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 764ae42d-ef09-3e2b-9b45-31b5e4326f5c | -6.82557 | -58.94447 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9f57d3-f345-3685-918e-7327530110c1 | -11.60005 | -46.3486 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43cc9a5c-f4c6-3f34-9fbd-ac86eae64d70 | -10.04907 | -59.35872 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3d3f1f8-45b7-30f4-9d43-d116abad53a6 | -7.91008 | -63.05981 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49bc8a19-50d5-3719-b5af-d4c0225c1bf0 | -10.47028 | -48.32468 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb5501ae-085d-3071-b01b-753af489e400 | -9.22385 | -59.67288 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28b0b040-3351-3929-936c-695db1607855 | -7.82077 | -46.8924 | 2025-08-25 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3ce6d9f-beb5-39ca-86e6-1241b96981d0 | -11.45802 | -55.46913 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3140b355-c1b6-3a03-8ba9-8f97e9cb1bfe | -9.17108 | -60.83287 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24d08f79-c58a-3e96-aa72-e4588bb430e4 | -8.8997 | -62.46375 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab89a55c-9183-3972-be38-7c627502f61b | -9.165 | -60.82206 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c951cc24-24c4-3b4b-adc9-4c18f0d28245 | -8.90112 | -62.45559 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4ad9738-63dc-3ce2-8fb1-28ae5bfc0b36 | -10.72194 | -47.12299 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21846f9e-499e-3267-bad5-13b917711d25 | -9.15504 | -59.47911 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d097f15-3736-3224-9760-55c28ac142b4 | -4.95952 | -55.82395 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5246de55-6bca-340a-b4b7-fd7d6553763e | -9.14939 | -59.49089 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06003dd0-4b65-313d-890a-a03eadf46c6c | -7.89938 | -63.06744 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5adb0137-1183-3399-a188-a2a4442d6bc6 | -6.16533 | -43.00135 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85de40fd-aa7a-3d52-81a8-55e4543e4395 | -9.20015 | -59.4952 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eaca8df-d607-3ad2-b14f-ed7f955d3238 | -5.4533 | -60.18726 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdb60dac-fb6a-385b-9182-f77401fb8f90 | -8.21034 | -69.86175 | 2025-08-25 05:04:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dd1c815-5238-3e8c-9368-96381e69ce52 | -9.71081 | -54.98929 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f43639-c1b8-31f2-b67b-8b5b6d284a77 | -7.52658 | -63.81192 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7aa35b0b-cb4a-3d37-8cfa-d6ef71ad261e | -9.00952 | -65.38264 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 418ebb07-8432-32e5-908f-f86697a35b53 | -9.1615 | -59.48444 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3db05c1d-bd75-377d-9c7f-896f8fe834f7 | -6.63005 | -58.41488 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df6bddc8-8a7c-350e-9f9b-74443cc74e4e | -9.17397 | -60.76935 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54798d8b-ddfa-36ad-8dde-a15e0d571114 | -9.30985 | -63.43683 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff26b5db-f5a9-3332-8c72-7b69658af0db | -8.65836 | -68.67387 | 2025-08-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97567cac-ab17-3bcf-864c-b773962bc9b0 | -9.02199 | -65.70361 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37d82ef5-7f57-3a7e-b911-7d52f1169347 | -12.93426 | -46.30758 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47928058-8958-31cf-8f74-163b93511fa1 | -7.54792 | -63.85948 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1df7821c-e85d-3c94-bfa3-aafc6bb648b7 | -4.96501 | -55.81067 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f262a41a-87a8-31aa-85f0-ee82165814e4 | -12.94251 | -46.31714 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fb74d26-d158-3f7d-a647-dc95a0fec250 | -8.21585 | -69.86271 | 2025-08-25 05:04:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd5b9c2e-baff-33ef-814d-eb8964eeb14c | -7.27088 | -57.66652 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba7387a2-f675-3782-bf78-9309002693f4 | -8.63006 | -62.63787 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66e61ecb-1e14-3e3a-b8be-dc840b3254de | -7.14292 | -44.15787 | 2025-08-25 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 586a7b1a-77d5-3150-b319-ea93b38c6729 | -9.64683 | -59.63594 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d5892efc-cd95-3333-8d87-2564f9dd372b | -6.82847 | -58.94915 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5aa2e1d6-f476-3888-a2d8-300b8e0f5cc5 | -8.75808 | -49.9485 | 2025-08-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb00c85-8018-31a8-a090-d892cf81317a | -10.71415 | -47.13972 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f7de3c3-c722-32ae-a28e-734807ed23ea | -10.53655 | -57.96711 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba661cd1-b350-382d-88c7-61da509c9b6e | -8.67404 | -62.87497 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fe19ac0-5804-3a84-bd0a-ba7a92e8df06 | -8.90395 | -62.43928 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b6b5290-324e-3601-8c16-edaa16802616 | -9.15944 | -59.4968 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef30576-ab01-3f1c-925b-d4624f22509e | -10.03146 | -59.35582 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a19077ad-9983-3858-9533-8f0934c57d76 | -5.85951 | -51.75081 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c8779fb-0fcd-3a9b-812e-40356d4f8d91 | -9.19861 | -59.48225 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7902c5f6-6d7a-3d66-b12d-8a08b7c8ff8d | -6.80001 | -58.63916 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a61f61-300b-351b-a044-bb284b3da573 | -6.62719 | -58.41041 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5fc3f94-28ee-310c-96e8-f789e49a68a4 | -10.89468 | -55.78314 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3466570-b842-30c0-b45e-7969e615dd90 | -8.22728 | -61.39438 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da203162-155c-32ec-9241-af166affdd08 | -7.36369 | -57.62922 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28ca4f10-fe9d-3cd0-8252-7c801d398b2e | -6.91804 | -62.99317 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29b85fd1-30d8-32b6-a571-c8c5db52a17c | -9.0055 | -63.63527 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 966ab106-d623-3d2f-99a7-a56131148728 | -9.14844 | -59.45269 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db117766-8c16-321c-b599-3d744b8c2d37 | -10.88914 | -55.79685 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba106243-714d-3f7e-93b7-aa0ef7b478d2 | -6.28513 | -64.15695 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdb55970-182d-322b-9e65-4ec3684fbfdb | -9.64753 | -59.6318 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 32679092-9959-38a6-b270-97631a316594 | -6.92181 | -62.99872 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6cc7126d-1cff-3b4b-9ab5-6f0c0681fd6c | -9.15958 | -59.518 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dde3cf1-893b-3a75-82f8-c7d897635f2b | -5.7489 | -57.57667 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f823eca7-2fee-334e-b930-32c019747548 | -9.81568 | -64.25542 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8ac7f45-c388-33b8-9e33-1990b920a828 | -9.17741 | -59.61063 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9a14282-137c-3a5f-82da-4fbce3a55811 | -9.194 | -59.44348 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3479df53-b32c-3a1f-99e8-63b09cc74ad2 | -9.51729 | -60.50828 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8213cabe-d37b-3719-ba94-1841a44b4de7 | -9.1487 | -59.49499 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7bfaf58-d0ef-3e38-bb42-9e65ae9290d0 | -8.61202 | -62.6128 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eb101b5-8443-3080-b42d-4c606ce6f89e | -5.41983 | -60.17159 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ec59129-6acb-3e4f-9192-ad189620ed00 | -6.25295 | -60.02285 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebcc4254-415a-3089-bcf9-1bf798bcea20 | -8.54613 | -48.84935 | 2025-08-25 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8b64584-366a-386d-bbdd-cfa1ee00843b | -11.20041 | -48.46877 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7917c7f-764d-36c1-8619-ddf2bdc2c478 | -9.05464 | -65.72385 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c608f35-0615-3a07-8d58-ae0a102cebaf | -9.16261 | -62.35054 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a56e7e-9e7b-36e0-b3b1-e28f53ccac94 | -9.15701 | -62.35773 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4f4fc2e-3883-3211-bd26-b1896b536378 | -9.00637 | -63.63041 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fae030fb-8766-35a2-9c40-3ccf56f6340b | -9.20537 | -59.44124 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12b29fec-8f1a-31ff-8785-a25f4f9a087a | -9.72213 | -54.93825 | 2025-08-25 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc911e6f-e25f-3175-a0df-144aa728536c | -10.70645 | -48.31176 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ad96fe8-1e82-3dce-b472-854a29369dd3 | -9.17269 | -60.82338 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fbfbdeb-0d11-396a-b21e-50c9e2199d04 | -7.72771 | -67.06588 | 2025-08-25 05:04:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5cf8241-a5a4-3bfe-ad3a-48033d6a9292 | -11.1758 | -55.02343 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de79bf12-52c6-3da4-b6d7-a8a75a3a951b | -10.61604 | -55.04619 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4aece9e1-c9ab-3347-860c-ea44d7214414 | -9.20261 | -60.92861 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de6f8b00-1ffc-361d-b9d0-1560d08d5a9a | -8.50931 | -63.87788 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README65.md)
