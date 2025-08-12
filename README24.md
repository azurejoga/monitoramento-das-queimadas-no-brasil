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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cb52f5b-b441-3c5f-9071-acb22543f6a6 | -3.43782 | -49.04007 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 987b5d7c-edcc-34f3-bc41-7658e1337a18 | -5.83321 | -44.10669 | 2025-08-12 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ddb7906a-51cc-302a-965a-e2854d764319 | -6.30573 | -51.40369 | 2025-08-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad5c8a29-473b-38f1-befa-562f93cab9a4 | -8.56615 | -54.69337 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1afc79ea-9979-38f2-abf5-c15613ce13a5 | -10.00035 | -46.32131 | 2025-08-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 777c7712-7ebe-3aca-add0-b28c81d41558 | -8.5706 | -54.70831 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e210d36-ac75-3612-a1d4-90f17fe1cf3e | -7.1169 | -44.62404 | 2025-08-12 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2539e02f-8b91-3c4e-b3fd-fa0a03c5f4e9 | -7.25518 | -59.99677 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 692dd4cf-2fef-3cd2-8e7f-aa1312d087d1 | -6.97451 | -59.28375 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f95e7e28-5b84-3c8d-ae15-8f3f53dfdab5 | -8.52448 | -43.32159 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2b32c827-f76b-3030-90cc-efc3a68009e7 | -4.30242 | -48.06942 | 2025-08-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 048dbe17-efbb-3bc4-84b4-a9618885944f | -6.30993 | -51.40013 | 2025-08-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fb9008b3-9b96-3398-9936-686a6ee19193 | -8.57613 | -54.71629 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 80460546-ce42-38bd-a217-c5c1c0c28099 | -8.52508 | -43.31665 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ecdf8585-5b91-3416-b841-62a67c51c1d7 | -6.61062 | -43.88855 | 2025-08-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b656ece8-0516-334d-881d-3293118d9831 | -3.83841 | -47.74852 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d27b0acb-36d1-314c-9d98-9372e087ce63 | -7.0803 | -59.20539 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9ef4381-3dc0-3829-bdf2-f8cb96363d82 | -6.22369 | -43.32908 | 2025-08-12 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0f76cbf-bc06-3861-a994-d36a1a4c0b20 | -8.57499 | -54.70188 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d441af-152f-3860-858c-3bde36d74aec | -7.554 | -47.04864 | 2025-08-12 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72f3227c-db9b-395d-aed4-25dabe79a102 | -7.07331 | -59.19898 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5782d931-f24e-3093-9834-494dca2600cb | -3.83609 | -47.74916 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0e4d4c89-1df1-34de-89ef-d6ff57b23b97 | -10.34381 | -50.82301 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a98df1e9-c20b-3787-9779-5effd6b9c544 | -13.06589 | -56.85062 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe156256-7251-3b5b-a295-f309eeb18057 | -9.38416 | -61.52477 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cd6029c-e268-3722-b467-38ccb9e3a48b | -14.11341 | -45.38764 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86aeb292-9b48-3264-9728-1696bd69de82 | -9.38287 | -61.53485 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acc63596-dfe9-3331-a6eb-12fa443b45d9 | -11.85568 | -49.00787 | 2025-08-12 04:59:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9013bdf7-56fe-35f9-b714-ac9fae8463ab | -14.1139 | -45.38335 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c1064b9-64f7-3d22-b2df-428a2dbc70f4 | -11.85679 | -49.00989 | 2025-08-12 04:59:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5bff92b-8d7f-3b7d-8b0b-c3b29ccd7053 | -12.99728 | -44.88816 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 940e41cd-022b-303f-971c-b7d2f82c51c0 | -11.68785 | -51.59494 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 367d8768-1aec-3f6a-ae22-93ee9ca717f3 | -10.35794 | -50.83508 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cb6ce88-6c50-3597-84f5-6d2dda27c741 | -11.45878 | -47.3203 | 2025-08-12 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 128fa2ab-7812-3066-9902-77573307ae85 | -11.67966 | -51.59838 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e95caeee-e35c-3e30-a149-9b4287b3f224 | -9.88509 | -55.39256 | 2025-08-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77f7ba2d-98ed-3522-968a-6731bedf2ec4 | -10.36001 | -50.82043 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cde0f543-3895-368f-81dc-32d0f8e7f926 | -8.93629 | -60.7365 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 651c9004-c8d1-3aac-a89a-eb00401a86a4 | -12.56701 | -47.00639 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 754717d2-a4b7-3905-a1db-b25fc1f90082 | -13.90312 | -51.83218 | 2025-08-12 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e627411-cc11-325b-8504-569df06b43f2 | -13.11714 | -46.8698 | 2025-08-12 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55454875-4d44-3ee6-8e1f-cf88a3beac10 | -9.37535 | -61.52324 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7608d095-c026-36fb-bfba-73262b817a10 | -9.19543 | -59.661 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b51f792-7fe7-30b1-b292-65b03a66f207 | -12.57325 | -46.99817 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f80a7d29-08a0-3eee-81a3-1d73a4ddcf83 | -12.63858 | -45.33463 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c85145b-e70a-3b3c-8266-3f01e24cafde | -10.34245 | -50.83276 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5e3b502-92c8-3caa-be06-662970600689 | -9.03336 | -59.76401 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52087880-e77c-3c61-a811-ab5030765fc6 | -12.574 | -46.99202 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c36d334-46fe-3f3e-afad-6b81be65a5a1 | -13.04036 | -56.83905 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cd997a9-1e35-3e3b-a4f5-34de1d3c62c9 | -11.39261 | -56.20586 | 2025-08-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c32c70c-8a20-32f5-b687-dc694e867761 | -9.37975 | -61.524 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70849003-a2ed-399a-8038-ff3a73fffe60 | -14.11878 | -45.39267 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0c6ab8-98db-3958-9308-9e2a44a795f7 | -14.11814 | -45.38924 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22cb7ed7-7cda-3979-b11a-a2f01ae54439 | -12.92752 | -55.63625 | 2025-08-12 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b4d2d6-d87e-3a96-95f1-9259f04d28f9 | -10.35475 | -50.82965 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b32a80f-708c-3eb9-9f2d-556902e47ec9 | -13.87898 | -45.57888 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e147d7f1-d82c-3d79-baa5-c9e1a5cf2115 | -13.07036 | -56.84402 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0197a40-ffc3-31df-9842-57957429e65d | -13.34502 | -50.24422 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 42ac7445-2430-301c-a657-fcf8a260096d | -8.92312 | -60.7627 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5aace62-4788-3edb-a69f-600539025201 | -13.35291 | -50.24919 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5a6b7f26-6a41-367d-8570-5b7292b5f1da | -13.33614 | -50.24683 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 244bc2b9-1247-3ff7-b43b-7fa182a3f5c2 | -9.03418 | -59.75904 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da6b454e-6821-3197-b9fb-63fbe6e7f5e4 | -12.50431 | -46.34004 | 2025-08-12 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48651d15-72cd-37cd-98a8-9cbbddc47ed4 | -9.17499 | -59.66269 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac439649-eb58-3856-8c64-aaa28ac1e957 | -15.66926 | -43.49095 | 2025-08-12 04:59:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 60916467-39a7-31da-b2fa-2f63b6a5e803 | -9.26432 | -60.77593 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b2f6bfa-7e61-3956-b163-45ca573ac2c2 | -9.19152 | -59.66028 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7fd6b9d3-150c-36d1-9cf2-b81a2fba22ba | -14.02544 | -47.40656 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80f1361a-cf02-3f83-9b9c-ec9d25ec55ad | -11.71524 | -50.11901 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c07ab0-83ee-3794-8c08-8673d5c1cf5d | -12.67145 | -46.98131 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c8e6705-6ac4-3eaf-bf3f-257ad9972ad7 | -9.38624 | -61.53858 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 45a5d02a-1012-34fa-b63f-aa0da51fdedf | -12.56584 | -47.01611 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 37246045-6da1-3f56-9f90-679eee19e341 | -12.56886 | -46.99107 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e93cc982-9d68-3a86-a529-061222bd3436 | -12.77236 | -45.45311 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32a97786-1f82-3f20-b8ca-c616cd633e21 | -11.68032 | -51.59374 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9601d331-a675-3c80-93fc-96d8c3cb9c51 | -9.88454 | -55.39604 | 2025-08-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9b3c036-83e1-3e37-bf78-24b84f85bcb3 | -10.36778 | -50.82148 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 883863a2-b969-3c97-9c40-b5742a3f0b56 | -11.87966 | -55.53163 | 2025-08-12 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38e3fd88-eaed-3c10-963e-dcb6124a2e69 | -12.7781 | -45.45381 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a2dc318-35fe-34a2-a08b-935320d0c4f6 | -9.37741 | -61.53705 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb57eebc-07e9-3ed6-a43b-964dcaed492e | -11.78665 | -49.55539 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a999ab4-0d49-341d-8306-dc50c6a96c88 | -12.55856 | -46.98927 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1c9117f3-226e-3725-9830-fdd061f848b1 | -9.19847 | -59.66675 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6cfb063-99fa-31a7-bae8-ecb043fdadb5 | -9.03287 | -59.76099 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45a546da-c2fd-398b-a2be-bcede7d2bd15 | -10.62213 | -65.00814 | 2025-08-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 947553b1-2b60-36ec-a218-b13ac3f4e2a0 | -12.58027 | -47.02678 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 189e86d2-a4a9-3a98-8a56-121e69657334 | -11.68718 | -51.59957 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83ca871a-3199-340d-8981-7861c7501934 | -14.63347 | -45.85485 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6058a3df-7ae5-39f6-9448-6d9e739249cf | -11.71672 | -50.11958 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f0b6600-b6ea-3854-94d0-dcab1801d042 | -15.35862 | -48.41498 | 2025-08-12 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95a97f4e-f24f-3e08-b678-09c6d75f591b | -9.19933 | -59.66172 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c6392a7-a34f-31e3-9698-35a1ef0fd9d9 | -11.81181 | -44.93449 | 2025-08-12 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cdf6c4c-b2c1-3ec7-ba65-870b9163e8f1 | -13.34871 | -50.24864 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 111ddd51-8e88-37ee-9c96-7bf8026ea929 | -10.74642 | -58.01546 | 2025-08-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2abc7c60-2a7e-333f-ab03-039a7b86f007 | -13.63281 | -46.93283 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a65f4e10-422c-346e-bb3e-91cd326111d5 | -11.78953 | -49.55474 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bac1867-d909-3160-a4e7-d9a7bb36f8cb | -11.21539 | -46.26916 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f11fc62-a809-3b82-9004-b23b52682e82 | -9.37114 | -61.5238 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f3c36e-6147-3bc6-973f-362bcdf65ed1 | -12.56112 | -47.01168 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d41fba0d-7872-36da-8acf-6f5cf6040a3c | -9.0381 | -59.75994 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
