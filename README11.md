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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53b4d999-0911-35cb-bee1-60ee8acb8ac1 | -2.94899 | -52.55001 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6135edf6-2861-33ef-b06b-7249ed405d6d | -4.93589 | -43.9605 | 2025-12-13 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c72a8ac-dccb-33c1-959f-5dd905bdd46a | -3.40906 | -52.06792 | 2025-12-13 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e226771a-9a25-370c-9513-b508413ebec6 | -4.86347 | -50.82597 | 2025-12-13 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68f20ae-acaa-355d-9035-0f7288f200ae | -5.07461 | -43.66722 | 2025-12-13 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5725b172-64fb-32fa-be8b-ac9b59a0e73e | -5.07416 | -43.67035 | 2025-12-13 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ad121fd-19c9-38de-a170-41e388ef9ed6 | -3.81943 | -47.04976 | 2025-12-13 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e96024cb-32e7-3801-8009-9d6894006cb6 | -3.22481 | -54.77502 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a044f9-00b9-372b-ac38-51735f024b50 | -3.28968 | -57.62914 | 2025-12-13 04:53:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93ca9ec-9dfd-3d37-aad2-62f874567605 | -2.23114 | -55.93117 | 2025-12-13 04:53:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48ea99b2-f4fd-37d5-9f4e-494e8aff765f | -2.94233 | -53.02481 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7874c0d1-10f8-3710-a2b4-4f309b8e7461 | -4.93546 | -43.96353 | 2025-12-13 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91af9ee9-49d6-3db9-9f86-b670bb35401e | -3.07676 | -52.84072 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f9bc0d-6909-3cef-ba63-cdf14c708a92 | -3.07343 | -52.84018 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43e4f927-acf1-3180-ba7d-2fb3caf4443f | -10.24199 | -52.22507 | 2025-12-13 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ba21444d-c54b-345a-b182-ebb823e2c9dc | -4.86403 | -50.82238 | 2025-12-13 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a1e2294-2067-3813-bd42-1914b8a94a54 | -4.4866 | -55.8032 | 2025-12-13 04:53:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbcc3a18-6205-3d0f-92ea-70d905ea6cd0 | -14.07555 | -56.16558 | 2025-12-13 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47c785db-eed8-3e99-b336-0659639c6323 | -3.15007 | -54.6046 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 198f3bb1-8da6-3a3d-8a7c-53c3cb454f12 | -3.14944 | -54.60856 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85dce509-a3ba-323b-8b60-4434b9ac9d05 | -3.19057 | -52.02975 | 2025-12-13 04:53:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 369ead0d-2727-353c-83c4-6bda585007ce | -2.88657 | -53.00898 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedc4c0f-8eb4-332d-935d-bad6a37f95c2 | -10.37536 | -45.05108 | 2025-12-13 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 044f3a1f-0822-3858-b315-86e44080c17f | -5.07849 | -43.67717 | 2025-12-13 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c73ad7ed-9d12-3e7c-9e3f-9bbc39a71a00 | -3.51559 | -52.19019 | 2025-12-13 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b4ec3f-9704-3f62-8fc4-0bcd9130253f | -3.32202 | -53.29099 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01401051-e7fc-3040-8cff-6a00066030ea | -3.31866 | -53.29046 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9af2ed74-dbf5-3854-9bdd-cf7469f72bdd | -3.15359 | -54.60514 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| efd8b4ec-69b6-3b00-b3a4-0e8c331d6951 | -29.40457 | -52.40765 | 2025-12-13 04:57:00 | NOAA-21 | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ee9c56b-272d-34af-8829-815db5cdbbec | -3.2007 | -41.8678 | 2025-12-13 05:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 51405bfa-b050-323a-8e66-966362e1ff04 | -3.2009 | -41.844 | 2025-12-13 05:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 4eb5673b-a8a2-3965-a4f0-522b3100e538 | -3.2007 | -41.8678 | 2025-12-13 05:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8b4f1a60-9ece-3737-9f4c-4cf8cfefd90c | -2.7383 | -45.0848 | 2025-12-13 05:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 6e12d902-4a88-3c58-8faa-23abe3a095be | -3.2009 | -41.844 | 2025-12-13 05:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 56540177-ff59-3c2e-bc26-f8b0674998e8 | -2.7384 | -45.0622 | 2025-12-13 05:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a148f629-f75c-3730-9b47-fab4b8e44cf1 | -3.2009 | -41.844 | 2025-12-13 05:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e1b20787-fb18-34ea-b9b6-a2f840708b4c | -2.7383 | -45.0848 | 2025-12-13 05:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7e522bff-c642-3092-80eb-d363a25fe8ba | -3.2007 | -41.8678 | 2025-12-13 05:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 96d623c9-7ab2-3789-8310-b71e2eb22ecd | -1.59488 | -55.8461 | 2025-12-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc468bd4-e4f6-38b9-8d38-1229a70f26ef | -2.10112 | -53.47606 | 2025-12-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c0877e-0759-3d49-ac37-5adc006150c0 | -2.99348 | -52.87918 | 2025-12-13 05:20:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e778c293-291a-3878-ad97-0262f6c64801 | -4.82865 | -49.54129 | 2025-12-13 05:20:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8cc172-fd01-34ec-b8e2-7ae4269e1189 | -1.66662 | -54.57889 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 198a310b-cfe6-34f6-90ee-710ae8badd4d | -2.68875 | -59.42523 | 2025-12-13 05:20:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48be0a2a-2a1a-369b-b1c7-49eb46f55686 | -3.95635 | -54.03952 | 2025-12-13 05:20:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4baef6d-0456-346d-85a3-144a37be5f48 | -1.18327 | -52.09339 | 2025-12-13 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb91c831-3da9-3109-9023-36feb52bebb7 | -2.4287 | -51.923 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dd65346-27d6-37ac-a094-2ba8ad63aebc | -2.66663 | -46.89351 | 2025-12-13 05:20:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf25db24-45da-3f7a-a168-286210873dae | -1.39179 | -55.34942 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 804b9350-6f91-3a63-8a9b-aef8018fb81d | -2.99403 | -52.87556 | 2025-12-13 05:20:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa0a9f65-0b17-366e-873a-99cf6bbebd69 | -1.90847 | -45.4732 | 2025-12-13 05:20:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6792f25f-90e9-32bc-a53d-9eaa89440304 | -2.73553 | -45.07285 | 2025-12-13 05:20:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f4a8678f-aa87-3586-a147-e053a643dee1 | -3.23805 | -47.24726 | 2025-12-13 05:20:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5be218a6-ebc3-371b-bdad-e6f8155e6337 | -4.36892 | -55.77256 | 2025-12-13 05:20:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed202cb8-eda8-36c7-9d4f-6370e3d12820 | -1.39525 | -55.87409 | 2025-12-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 610bb3c1-7dd9-3fb8-bdc8-edcfef57106e | -2.66738 | -46.88855 | 2025-12-13 05:20:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3931af04-0c5e-3832-a8d1-4096dc63f313 | -3.04906 | -53.01335 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b410738f-1dba-3bbf-870f-ff01a299b550 | -1.20018 | -51.82965 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec48a627-aff3-3fac-a121-dc4eda2b5826 | -1.47486 | -54.19992 | 2025-12-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0205e0d-47bc-3876-91b8-ffffb8aa86e7 | -1.49109 | -53.13313 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f0730b2-9ea8-3095-b2e8-d21e51d1f6de | -1.66295 | -54.57835 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d339c5f-c421-3c71-a0b9-682407127337 | 0.62425 | -59.36981 | 2025-12-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4687c4d-051a-30bc-9481-b961468b0d55 | -1.88094 | -54.68669 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3128999b-a30c-353c-a8dc-cf04aac22e95 | -2.73558 | -45.0803 | 2025-12-13 05:20:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dad29429-3bf7-3abc-8fd9-c3e1f68b827c | -4.36764 | -55.77099 | 2025-12-13 05:20:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b8b04ac-00fd-33ac-9797-0abb2c8f3489 | -1.58614 | -55.53375 | 2025-12-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c7afb64-10b7-3fcd-b551-66cc4f4a7159 | -3.80276 | -49.03326 | 2025-12-13 05:20:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33c87d08-2be5-314c-a620-ad6b82c0044b | -0.79736 | -52.35939 | 2025-12-13 05:20:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24e0281d-13f2-36f6-8e73-559aeabe828d | -2.77419 | -54.52606 | 2025-12-13 05:20:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32d690dc-3d1e-35a2-98af-1bdd2471284b | -1.20187 | -51.82813 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc6ad9cc-96ee-31b0-8b9a-b284e2199fda | -1.40083 | -55.38238 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d84c439a-fd95-3803-98b1-0a654e038a41 | -3.22508 | -54.77221 | 2025-12-13 05:20:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c5167c6-fd73-32ca-b925-28806396827c | -2.38868 | -56.0571 | 2025-12-13 05:20:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f20aa07-ef3f-3726-8280-428b5bf3f853 | -1.90514 | -54.2348 | 2025-12-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44498879-0559-3974-b341-b0991e003082 | -2.36278 | -51.94514 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bf150b1-f47f-3a96-9499-8145e5bce100 | 2.50679 | -61.02975 | 2025-12-13 05:20:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49a2c6cc-4e3f-3f07-90ec-e1de3ef32f15 | -2.48494 | -47.77691 | 2025-12-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d894b03-0563-3a7a-bb55-66d4d03820e8 | -3.44767 | -44.73752 | 2025-12-13 05:20:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc12b459-8999-3f5e-a421-01ccafbe5c4c | -1.87728 | -54.68613 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90f7d59c-b7ca-35f0-8266-85a716da950c | -3.51737 | -47.21161 | 2025-12-13 05:20:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7060dbe-865a-3429-9b65-d2f7071ed2c7 | -2.7032 | -51.88609 | 2025-12-13 05:20:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d680b986-5048-3b8d-acfe-4a2bfd6f29c2 | -1.84621 | -54.52954 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cef55ce-b78d-3ce5-8a58-c1656da89fde | -2.44608 | -52.22549 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a3b30bf-6881-3ab8-b867-12a61bddca45 | -1.59834 | -55.84662 | 2025-12-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47c35f4b-9062-3683-b65e-0c6763d3073f | -2.95182 | -52.55386 | 2025-12-13 05:20:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c04fc63c-dadd-3abe-bc98-7f0f9fa63ab2 | -2.52848 | -45.33566 | 2025-12-13 05:20:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f267cf65-ea38-3043-acfb-32f18ff03719 | -2.93938 | -53.02349 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8c63ee9-8765-3e99-9965-672c03070ae7 | -1.8469 | -54.5252 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b42f487b-6f5a-386f-b44d-024b3430149c | -2.42936 | -51.91872 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8cad2ee-d915-3d21-a88e-53338ca1d9e9 | -3.69506 | -53.75649 | 2025-12-13 05:20:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c136ad84-32ea-37f4-a7c0-d965b0204636 | -1.3878 | -60.30788 | 2025-12-13 05:20:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8347ea94-7ad7-36f8-a972-733930dfaa59 | -2.73655 | -45.0739 | 2025-12-13 05:20:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1e450a2b-7c24-346d-bb82-a21b0ed90ff3 | -2.67283 | -46.89438 | 2025-12-13 05:20:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baadeb52-1dca-3622-a046-7608bf05ddda | -1.01508 | -53.72681 | 2025-12-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3530687-c89f-3f38-933d-bdb49d32d433 | -3.81616 | -47.05122 | 2025-12-13 05:20:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d023b21-db92-34f6-b916-ef72ec5a0d1b | -1.34797 | -55.39869 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c56bd78-8e48-32d1-aacb-1a18b837eddc | -2.93882 | -53.02711 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2baaaf1-51fb-3752-b36f-7dceaa3dd85e | -2.49713 | -51.80244 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b438852d-f599-3312-b463-c4220aebf9ce | -1.9018 | -45.4721 | 2025-12-13 05:20:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82ca196b-e712-3d08-a212-2e248e94822c | 2.51059 | -61.02917 | 2025-12-13 05:20:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
