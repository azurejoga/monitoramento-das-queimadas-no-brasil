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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 738a584e-a7c1-3a9c-9f14-6d9871c264a1 | -11.3963 | -52.9477 | 2025-04-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e8950658-07bc-3e7f-b7c4-bed53e267df8 | -11.4152 | -52.9458 | 2025-04-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e9a8e76d-054e-318f-a32d-b0890b01a300 | -11.3963 | -52.9477 | 2025-04-24 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f04c8989-401a-31aa-940f-f0876e16339b | -11.3963 | -52.9477 | 2025-04-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 521863d2-a406-30e3-a563-e5e04fc0795d | -11.4152 | -52.9458 | 2025-04-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 48b88838-cc8a-3770-a8d4-e1a120ce7033 | -11.3963 | -52.9477 | 2025-04-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 043ffebc-21a4-345f-9e07-1cb125dbe6d7 | -11.4152 | -52.9458 | 2025-04-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7e2940de-908a-34e8-a09b-563d02a2687a | -13.0226 | -45.09056 | 2025-04-24 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 69f02676-da37-307f-a1b8-070d0aec6af2 | -11.41295 | -52.95953 | 2025-04-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| dd254a66-4a26-3146-8f44-295f9285a8ea | -11.40267 | -52.96085 | 2025-04-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8178b86e-c3e7-365a-88b9-ed0a0cc06584 | -11.41139 | -52.94722 | 2025-04-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 810d473f-c10b-3d9b-b210-8a82266f985d | -11.3963 | -52.9477 | 2025-04-24 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 72015e2a-5e04-301e-b9fa-5d761aa2a57d | -11.4152 | -52.9458 | 2025-04-24 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 4186584c-897c-36fa-af58-d95e9d7d851c | -6.9045 | -35.0641 | 2025-04-24 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 6f799e88-279a-3382-8821-2b5b4ee346d6 | -6.8854 | -35.0666 | 2025-04-24 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 0e7ffb59-7361-36d0-9e94-204e98c2d590 | -6.9049 | -35.0366 | 2025-04-24 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| 61b2b529-25df-36e3-b369-852fb4edebe0 | -6.8858 | -35.0391 | 2025-04-24 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| 6aac5f57-4832-323c-bf2b-472776659667 | -6.9049 | -35.0366 | 2025-04-24 01:20:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| c0754e5b-8247-3a2f-aad2-d071fbc51b48 | -6.8854 | -35.0666 | 2025-04-24 01:20:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 1fafc5e6-cfb6-330b-99a6-e0b6944f4685 | -6.8858 | -35.0391 | 2025-04-24 01:20:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 100.3 |
| 9a5c4fb3-dba9-3417-b5b5-4179f4fb550d | -11.4152 | -52.9458 | 2025-04-24 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 88ffc003-409f-3770-a48d-92fb007167ac | -6.5631 | -51.1126 | 2025-04-24 02:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 194403de-1f04-3dc9-9fb4-bc76fd71d374 | -11.3963 | -52.9477 | 2025-04-24 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 433d93df-77ef-39d9-ac50-797d5011404c | -11.4152 | -52.9458 | 2025-04-24 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 7d4e79c5-bd71-3b2b-969b-6168217aa034 | -11.3963 | -52.9477 | 2025-04-24 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d1a88103-de6f-3e04-8177-265c87ae792d | -11.4152 | -52.9458 | 2025-04-24 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4c5bf739-8078-30d7-87e4-fdb08923ac40 | -11.3963 | -52.9477 | 2025-04-24 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3b5e72e0-7ce1-3d59-b1a8-3f70728261a2 | -11.3963 | -52.9477 | 2025-04-24 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1cd461f8-de04-3260-97f6-c01dfc566fa1 | -11.4152 | -52.9458 | 2025-04-24 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6d2a7e93-e776-3b5b-971d-9db1df784b1b | -11.4152 | -52.9458 | 2025-04-24 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8c8d0904-c92d-3508-9f40-7a505032cec0 | -11.3963 | -52.9477 | 2025-04-24 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b96dcc62-9ebb-35f3-b201-4730bf4de196 | -11.19983 | -37.22018 | 2025-04-24 03:06:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 71dec9ed-77c7-3d68-95db-d089399587d5 | -11.20557 | -37.22136 | 2025-04-24 03:06:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9aa0dd89-0cd0-3ea3-a937-30191b77dea6 | -11.29254 | -37.28524 | 2025-04-24 03:28:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4b1371aa-6129-3258-8b53-42c6bf28e5c4 | -9.61775 | -37.03429 | 2025-04-24 03:28:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e45f06c7-e13b-3470-bd51-7afdc7e1181b | -11.20529 | -37.22044 | 2025-04-24 03:28:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a5883bd0-ff70-3594-b66d-90235dccc7ab | -9.53186 | -40.30819 | 2025-04-24 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b069fa9-ae79-39fa-af36-308564f526f0 | -9.53092 | -40.31343 | 2025-04-24 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a7f681f-f53c-340d-a33b-a11bef16ab1c | -9.71876 | -36.69437 | 2025-04-24 03:28:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d3d9273-beee-3e8b-ba5d-abf112c91fbe | -7.37665 | -34.88535 | 2025-04-24 03:28:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e95c2f48-4384-3fb2-bc36-51f5e2b8e66f | -9.61858 | -37.02945 | 2025-04-24 03:28:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 18abfe86-04c6-3b35-ac94-10302384700e | -11.20147 | -37.21976 | 2025-04-24 03:28:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9a82884f-aa39-3849-be5e-c2e1fdd2be03 | -9.6216 | -37.035 | 2025-04-24 03:28:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2248ccb9-577e-317a-91b3-4988b8438f97 | -8.08195 | -43.11191 | 2025-04-24 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1086406c-42e2-3c24-a220-b8d92e7e3e12 | -11.3963 | -52.9477 | 2025-04-24 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6b399e1c-0ff8-3bfa-8a81-e46a35c271db | -11.4152 | -52.9458 | 2025-04-24 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 76b3f09d-7f2c-3359-aaee-9ea7b25f4292 | -16.67896 | -43.88335 | 2025-04-24 03:30:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fd1c13d-51d4-30e5-be3f-fbd0a8516e9a | -22.89857 | -43.75397 | 2025-04-24 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e65fa54d-ceed-3a71-82a2-5c1e97d96ccd | -11.4152 | -52.9458 | 2025-04-24 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 5a54b8ac-4fd7-3262-a452-758a14ef064a | -11.3963 | -52.9477 | 2025-04-24 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1422ee2a-34c7-384e-b4f8-a19ffee9d3b8 | -11.3963 | -52.9477 | 2025-04-24 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 99f277c3-2a3c-39fd-afef-6c3fe364f332 | -11.4152 | -52.9458 | 2025-04-24 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 10d0898a-3dce-375d-8edd-4cbe3c872415 | -11.3963 | -52.9477 | 2025-04-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a0712d7b-9725-330f-83f8-d5ef1b130764 | -11.3963 | -52.9477 | 2025-04-24 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 23aba96c-a295-3322-92aa-222b937534a6 | -8.87025 | -49.89165 | 2025-04-24 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f600647-ce76-360b-a0a2-e66b32cf2581 | -11.78628 | -51.3088 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78ee9c2a-b5ee-3967-9542-6d60d3ab0968 | -11.40053 | -52.94615 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 76b3f56e-2d88-32c5-8a44-7d2bc6e57fdd | -11.40887 | -52.9529 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0ad49cd4-4cc7-3bb7-a4e3-4c5e1500501e | -9.31727 | -40.50634 | 2025-04-24 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35809ec0-0adc-332e-a0ab-0af6408f8dcc | -12.29405 | -43.54417 | 2025-04-24 04:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f8b3d8c3-7029-365c-88e7-7452580373cb | -11.40975 | -52.94801 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e419f323-9e70-32e5-804e-7a9dbb259557 | -9.62019 | -37.03687 | 2025-04-24 04:19:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 374f2268-af9e-385a-a61d-ca4b317e4ca5 | -11.40338 | -52.95689 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e2a074b6-0d11-32f2-a9f4-c82708eedd2f | -8.86716 | -49.8859 | 2025-04-24 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bfdbf40-b2bb-3d9b-8de9-1146013e9dfa | -8.8663 | -49.891 | 2025-04-24 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d03e3aa-64f9-3bfb-8a42-cde9600e76c9 | -8.08764 | -43.11247 | 2025-04-24 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0904d00-8a91-3637-8f14-62ed18fa23d9 | -9.62096 | -37.03105 | 2025-04-24 04:19:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0632a7ee-d86b-3bf4-9c7f-92de247dcb60 | -11.41249 | -52.95232 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2395239f-860a-3775-a33a-08fdb055fc7a | -8.08424 | -43.11196 | 2025-04-24 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 743f4e1b-0047-3bae-a934-e63374bf30fc | -11.4014 | -52.94131 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 31c1ac04-bc0b-37bd-8d38-938afad49031 | -11.40799 | -52.95782 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99042cde-245b-33f5-9928-edf939fd4bf5 | -11.39965 | -52.95106 | 2025-04-24 04:19:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| eb1f658f-d448-3197-aff6-ac355dc6be59 | -12.29752 | -43.5447 | 2025-04-24 04:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65ead908-c41b-32a5-b7ec-d87975911d09 | -11.3963 | -52.9477 | 2025-04-24 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 87d3d3d8-51c5-36eb-baec-c452ec9f5493 | -15.07995 | -48.94289 | 2025-04-24 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88917acb-6b7d-3bae-83e3-da6cffc11299 | -17.59593 | -43.19635 | 2025-04-24 04:21:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cc2122b-79c8-387e-be08-60e670f5655e | -18.0071 | -42.89271 | 2025-04-24 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 013cef14-70f2-38a5-a6e7-fe8c611f329f | -15.76425 | -43.23095 | 2025-04-24 04:21:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| db61145d-b6ac-30d1-8c20-56b2bf1f1c13 | -14.87593 | -45.11637 | 2025-04-24 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 974f2b67-8014-3a7e-aa3c-942fe6b1607a | -16.60925 | -43.32574 | 2025-04-24 04:21:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2182c77-7505-38df-87ef-691e62735202 | -13.3412 | -43.38494 | 2025-04-24 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d836e12-6fd7-3b30-838d-2f4dd5601493 | -13.66536 | -43.78755 | 2025-04-24 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46392345-0e17-3eda-9c1e-151dcb01a8f3 | -17.00977 | -49.77935 | 2025-04-24 04:21:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 543ddf23-f460-3904-bb31-dc1d4db84dae | -16.68022 | -43.8835 | 2025-04-24 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5c16f99-36bc-3c8c-8597-aac654c1b1ca | -15.0793 | -48.94675 | 2025-04-24 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b008f6cd-0ff9-3d9b-8dcd-2a90222a4434 | -15.09089 | -52.84516 | 2025-04-24 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e242100c-8850-399a-b05d-2609312f2799 | -23.40658 | -46.55765 | 2025-04-24 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| def1b22b-8dfd-3ab1-b1cf-06a20269b56f | -27.56704 | -48.65946 | 2025-04-24 04:25:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 26557346-472a-3143-af05-79794533613a | -31.21617 | -52.06044 | 2025-04-24 04:25:00 | NOAA-21 | SÃO LOURENÇO DO SUL | RIO GRANDE DO SUL | Brasil | 4318804 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 04314f41-676f-37bd-b322-3672dc7b0461 | -28.12785 | -50.45852 | 2025-04-24 04:25:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e33f118c-9047-3c3d-89a5-896c148142ed | -27.69064 | -48.74257 | 2025-04-24 04:25:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c7385acb-4b78-3440-9d97-2a0e0c7ee862 | -27.2809 | -48.78214 | 2025-04-24 04:25:00 | NOAA-21 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b632f8c-653f-3c1b-9a4d-2f2ba625fa0c | -11.3963 | -52.9477 | 2025-04-24 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6290fa97-df47-3ae3-940c-a3ca48ed1f76 | -11.3963 | -52.9477 | 2025-04-24 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c94a76b5-1621-368c-9238-b894e0bc9371 | -8.86815 | -49.88816 | 2025-04-24 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3365751-e93b-3c40-9fb3-debad2756b9e | -8.86759 | -49.89186 | 2025-04-24 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5fc258c6-a4d0-3374-b970-ceec2e9e3b4b | -8.86474 | -49.88763 | 2025-04-24 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99f40f27-97e1-36a6-84b4-39de3bd8d7a2 | -11.40089 | -52.95473 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8179d43-22ef-3d81-b4d5-3356da64e918 | -14.87373 | -45.11629 | 2025-04-24 04:49:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a4dadbc-5509-3fc8-bc0e-5a0b9198007b | -15.08029 | -48.94551 | 2025-04-24 04:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
