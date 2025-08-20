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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efaf748f-03f9-31e1-834c-242f412d83b8 | -10.25146 | -64.48368 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98223f22-c265-33eb-9f30-d7dd9ebc93ca | -8.75677 | -64.19431 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b65f04b-2430-34dd-90c0-080d190ad570 | -9.23884 | -59.60468 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93227bac-8e3f-31f4-8912-efb6189aab86 | -9.18308 | -59.63325 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9ad578f-b657-3155-88cd-098f71c4014b | -9.8966 | -60.28542 | 2025-08-20 06:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f14915b2-628b-399a-a914-547b594994e3 | -8.88422 | -62.40197 | 2025-08-20 06:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daedf989-1431-3f32-b7f1-ee4214499b54 | -9.17425 | -71.93829 | 2025-08-20 06:16:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec0339d5-1bfb-3439-a1f4-6af20f4853a9 | -8.6304 | -67.26064 | 2025-08-20 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 439b42a9-7160-35e4-a4e9-0a6313b2fbc8 | -9.18057 | -59.59715 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4739753-6302-35a9-bef2-cc79cd6701ee | -9.23795 | -59.61209 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f66e4835-572c-3a3f-b79c-b046c8a6646c | -8.56631 | -66.95186 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9055aa60-22d2-3f71-a78b-1dbaee6723ab | -8.56427 | -70.06093 | 2025-08-20 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aa078d1-b8a6-305f-8a7b-bcba6623a2ce | -9.17765 | -59.61748 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5223f27-2c3c-357b-978e-6e5ca2f7c4d8 | -9.18674 | -59.60373 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7672b2a8-360f-3620-8aa1-c8974cbef751 | -8.56367 | -66.93773 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27574335-dd1c-3fad-b447-1454f943d9a1 | -8.56569 | -66.95634 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b9af70-a696-3175-a05d-fc20fa3eae71 | -7.5542 | -63.85283 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7a47811-3720-3592-973f-abd871dba7c3 | -9.22759 | -60.33894 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 135ea090-cbac-361d-b17f-8dfbbe6e70ab | -9.19795 | -59.63778 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a2274c2-3538-3496-8c9c-b8855ad0e7e4 | -8.30908 | -70.7407 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73949bc9-92b7-3885-94e3-c79f6f8950c7 | -7.55969 | -63.85358 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7e76199-3e6a-31ed-9549-072240956219 | -8.76175 | -64.19856 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad6cec41-b2f7-315e-b9e6-487fb8d86782 | -8.6298 | -67.26495 | 2025-08-20 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a243225b-d59d-3a63-bab0-75bf031532d8 | -8.56305 | -66.94225 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b742d316-93a6-3cb1-95f6-44dafe0a5df0 | -9.21285 | -59.69818 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b47c7b9-fe0d-329e-9280-d92ee7484998 | -10.09932 | -68.45691 | 2025-08-20 06:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69cbd42e-84c4-3e9a-900d-1f50a82bb364 | -9.22743 | -60.33139 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3a24ec32-82e6-37c8-bba8-b98f65358d55 | -8.37033 | -70.14208 | 2025-08-20 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20fa7d54-80dc-3a3a-acd5-7025b3fba686 | -8.63481 | -67.26126 | 2025-08-20 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e05ae512-30b2-3d1b-857d-c0199897c87e | -7.55518 | -63.84574 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6619f0f0-778f-38ea-b5b4-2a7f2866f44a | -8.92541 | -72.8249 | 2025-08-20 06:16:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b65904c-550c-32bb-8693-bac7239ec5de | -9.21372 | -59.69086 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3b91699-b9db-3988-b276-90021607262f | -9.1704 | -59.61637 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eb7fb55-c573-3649-80ae-ec7ccada097b | -10.24602 | -64.48283 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d00da1c2-dbaa-34bd-8de7-8ceef0e77ffb | -8.55854 | -66.94158 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b71db089-fd3c-3153-bf19-87d1c26d8ab6 | -7.50675 | -63.83171 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b929bc26-f146-3b1b-b577-9a06af24f187 | -7.78889 | -66.96193 | 2025-08-20 06:16:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6f4982-43f9-3dd8-b0ec-5bca45a2d5f8 | -7.78726 | -66.9594 | 2025-08-20 06:16:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a037db22-6bfe-36b9-b345-4af261d39824 | -9.22665 | -60.33786 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3042847c-cb0b-34c7-ba48-b8f2d6d232ec | -9.23153 | -59.60397 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e82c00f-9032-39da-8bb7-eb4e29398749 | -9.18036 | -59.59554 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61732d5e-0820-3b0e-a848-2a60073d1763 | -9.18143 | -59.58984 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 804e9b97-4622-3ef1-86be-856e55826382 | -7.78953 | -66.95756 | 2025-08-20 06:16:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f137cd24-ad1e-3717-8c80-204987a072ab | -8.96226 | -60.50022 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ee3c325-b583-3c1d-bf04-4e8c5c99da12 | -8.56817 | -66.9384 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc797115-5d7d-3da3-a655-679049f190c7 | -9.18933 | -59.64233 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 541cb1e8-a402-3c7d-923c-c06d578c1042 | -10.09985 | -68.4531 | 2025-08-20 06:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4910bf2a-4b43-3281-8e22-bc587730290d | -7.79171 | -66.96004 | 2025-08-20 06:16:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd380001-b9c1-3e95-b77e-eb480418a274 | -9.1916 | -59.62901 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 040c5327-263b-3bc4-85ed-9282dc4803d3 | -10.45093 | -64.41287 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46ac7e0c-4afd-3dfe-9fdd-e36478302ae8 | -9.18763 | -59.59658 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42368acf-f604-3dd2-b386-eccab7cf4919 | -8.56492 | -70.05656 | 2025-08-20 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 694715d3-d7ee-3264-80aa-e0b79ee203fc | -8.63922 | -67.26189 | 2025-08-20 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d7ee42-3161-3248-bf31-c1417adb9a75 | -7.54969 | -63.84497 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4758a062-ce1d-37be-b6fa-f19a13b15090 | -10.25194 | -64.48005 | 2025-08-20 06:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6dc058e-af07-36c1-ad50-6870eb39b400 | -9.18784 | -59.59822 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60f24139-0978-3847-bde6-53b31bb5dbd8 | -9.23242 | -59.59651 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55a4f6d5-fb58-3825-8e9d-2bd342a94345 | -9.18126 | -59.58824 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df451dee-b2ba-3ad6-9a5b-c1fd2f29128a | -8.87689 | -62.41043 | 2025-08-20 06:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97e40f67-e47c-36c2-9175-6372ee0dfa60 | -8.9699 | -60.49493 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a2b34d3-7c43-3561-b780-7c897c5996d7 | -8.76222 | -64.19509 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f367f253-b7eb-3076-a375-0151e3758e36 | -8.56243 | -66.94673 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c609a125-1d25-3f89-9799-1a4038e09ed8 | -7.56018 | -63.85004 | 2025-08-20 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cee0457d-1c6f-3773-842c-d04488e7b226 | -9.88955 | -60.28447 | 2025-08-20 06:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75ab6a04-ca2e-3949-9d30-ca70bf7892a3 | -8.56119 | -66.95567 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65478b2c-2164-3c3a-bbfb-35d2041e90ee | -9.19753 | -59.63581 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d26541ca-49e3-3cf5-be12-b7af59ef06a3 | -8.56181 | -66.95119 | 2025-08-20 06:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e0b9b95-7aa3-3bb3-81a2-8fa4a02c4701 | -7.79232 | -66.95566 | 2025-08-20 06:16:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e89e6bfd-cc87-356f-a8bf-859f19e87420 | -8.87927 | -62.39178 | 2025-08-20 06:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40bfb272-8389-3f94-8df9-78b14ebe8a4d | -9.19072 | -59.63647 | 2025-08-20 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 013bc1ab-3e37-397c-8e00-0c8c3ba402a1 | -8.30553 | -70.74015 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 570e4426-6988-30e8-81ef-cd12af4900b1 | -8.30136 | -70.74364 | 2025-08-20 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a7ed949e-27dc-3506-81db-6b323993415f | -13.1364 | -54.9376 | 2025-08-20 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2cb576a7-34d2-3bd0-bee6-cbbe34596d69 | -13.1367 | -54.9171 | 2025-08-20 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 585efdef-dafa-3eda-896e-9c70a6942417 | -13.1558 | -54.9151 | 2025-08-20 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6f55b59c-ead3-31e1-b466-25b96fc1a2d3 | -13.1555 | -54.9357 | 2025-08-20 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 00376adf-12e0-31b5-b348-bd5e317b262a | -13.1364 | -54.9376 | 2025-08-20 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e98d540d-c2ac-3aca-8292-f1f25d795324 | -20.339 | -51.7062 | 2025-08-20 06:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 3e08d662-8dc3-356c-9ebb-a0b29f49f062 | -10.7043 | -48.2226 | 2025-08-20 06:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5186210a-d98c-3a3e-803a-780f91bd6b0a | -10.6853 | -48.2248 | 2025-08-20 06:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5e209957-138b-3a57-a2b5-06d45e36e192 | -8.034 | -47.6639 | 2025-08-20 06:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| f5421275-c6e6-3d4a-82c7-caf184a74698 | -13.1555 | -54.9357 | 2025-08-20 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 16bb46a8-67e7-381b-8935-5316f4d75927 | -13.1558 | -54.9151 | 2025-08-20 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 0dfc3583-3207-3d8d-adf0-24d04d560b4b | -13.1367 | -54.9171 | 2025-08-20 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 4c3ffa2e-a37f-30b6-8c1d-09f3f910726e | -8.56316 | -66.95061 | 2025-08-20 06:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e686c1e0-2eec-3d97-80ef-a2c6bacf3533 | -8.30424 | -70.74598 | 2025-08-20 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab76fdf-f1c4-35ec-81ad-68eb77943054 | -8.55705 | -66.9435 | 2025-08-20 06:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdd9a522-a201-3ac8-9e7c-539d5a6b5672 | -8.56405 | -70.05927 | 2025-08-20 06:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82160769-e070-3456-821b-8d40c78aef63 | -8.63617 | -67.26493 | 2025-08-20 06:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7922d7e-b6e0-3b5f-8095-e1a05f675ac0 | -8.3047 | -70.74258 | 2025-08-20 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5a7376-406d-3055-8f49-1796d2ee5485 | -8.56354 | -70.06315 | 2025-08-20 06:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66d2916e-52ce-34e5-bfce-235659adb218 | -8.56394 | -66.9444 | 2025-08-20 06:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c1132c8-2118-3df4-ac67-222beb581592 | -8.63541 | -67.27096 | 2025-08-20 06:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e79bc61-31ce-3124-b5b3-2bab9b6af882 | -8.55626 | -66.94981 | 2025-08-20 06:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c34688d7-a667-3e32-9b02-739874289e86 | -20.339 | -51.7062 | 2025-08-20 06:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 620c5075-70bf-31ad-af2c-a2ee91f16e27 | -10.8214 | -43.2665 | 2025-08-20 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 49.1 |
| c65ff14d-49a5-3cb3-92f1-e01e7622b7ed | -13.1364 | -54.9376 | 2025-08-20 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3b88707c-a413-3e40-8399-eb167a9be1e3 | -13.1555 | -54.9357 | 2025-08-20 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| cef143a0-0067-3a37-84dd-874bbfd089f9 | -13.1367 | -54.9171 | 2025-08-20 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 449f8708-5188-3a3d-9819-02489f6a4be8 | -13.1558 | -54.9151 | 2025-08-20 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |


[Clique aqui para ver as próximas entradas](README58.md)
