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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deb67347-4b3a-38db-a347-9d276424a2f4 | -13.1236 | -46.855099 | 2025-08-13 01:01:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01672e9b-8fe9-3d3e-a9c5-cc600fe9360a | -7.1206 | -60.114101 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c025b1a-5f8c-34c7-ba2c-dd4859f23d06 | -8.1219 | -55.5509 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2f5f79e-0c84-3364-8073-f0c3b351e745 | -5.8827 | -57.730999 | 2025-08-13 01:01:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b02a14-befa-3375-96dd-120b86316764 | -8.3766 | -49.358501 | 2025-08-13 01:01:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a123e91d-bc58-3396-a664-8d5298c76b80 | -9.7124 | -49.458 | 2025-08-13 01:01:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d14eb7b8-5f08-3cb1-93d4-83dd0a3c6182 | -12.6829 | -46.9562 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da6fabe2-c945-34cb-b3f1-ec69cf539d4a | -9.0523 | -60.627102 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f392a1db-e2ae-31fe-9a2b-5fcab731acfe | -22.3738 | -45.463902 | 2025-08-13 01:01:00 | METOP-C | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a720bc2-f51d-3eea-9b32-d9c126b1f2cf | -9.204 | -59.650002 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1641c3ed-3034-3984-b038-4df3647cd3f5 | -7.4518 | -60.6134 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84f08f9a-0bf0-3dfa-b185-0a5097fbe513 | -6.8808 | -59.147099 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b842e77-8242-3e3d-a11b-68c4b7f020d8 | -9.7047 | -49.468899 | 2025-08-13 01:01:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f917e8b-409e-360e-bb86-fa9461afd1e1 | -4.2294 | -47.2048 | 2025-08-13 01:01:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2f7372-0309-316d-8db6-c1eefdf7b481 | -10.9661 | -49.557598 | 2025-08-13 01:01:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca170c6b-a9ef-3180-84dc-8403d47c92b6 | -9.0621 | -60.625099 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34c4eafb-0ccb-36ab-bc70-3d4b7ed0b8b1 | -6.9272 | -59.125301 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee6933a-95df-3b86-9eb6-e6b5b3ffab67 | -16.320999 | -52.9044 | 2025-08-13 01:01:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98d138f6-bfc6-34e4-a67f-ed86907f3ef4 | -11.9873 | -45.137699 | 2025-08-13 01:01:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7057a6-a92c-368d-9dec-11c1b4d0dcc0 | -22.383499 | -45.461102 | 2025-08-13 01:01:00 | METOP-C | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c80ae423-d4eb-369a-bda5-ccbe70a8562e | -7.2554 | -57.626202 | 2025-08-13 01:01:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb908f89-52e4-364b-b137-a2602c7252fb | -16.311199 | -52.9067 | 2025-08-13 01:01:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7ce27d1-4667-368b-8550-fbaa4bb9ad95 | -9.2082 | -59.6213 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a9e2b43-1654-37eb-85a8-aff1a6d81160 | -12.5341 | -46.982498 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18864b75-0103-39e2-b44b-8b2d0ad000ba | -8.1236 | -55.558498 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da853ecc-8687-33a8-aa7a-486972da3cf9 | -12.1464 | -48.0163 | 2025-08-13 01:01:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 959575b2-b7df-352b-add6-5d4d4a72bd74 | -7.4673 | -59.875801 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 898c1d03-5b4a-33a6-9a34-40dcf8ffffc4 | -16.322599 | -52.9118 | 2025-08-13 01:01:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dfc02066-887d-3371-838b-a6c2f267bea3 | -4.2197 | -47.2071 | 2025-08-13 01:01:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 843aafe1-031f-3c1c-953a-2ab7347dd8bc | -7.254 | -59.9753 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47c081dc-42c3-3e81-a4f6-e903eaebdf5f | -6.2861 | -53.626598 | 2025-08-13 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588d82ca-c82d-3dc7-8743-4105314bd4ea | -15.0885 | -51.339001 | 2025-08-13 01:01:00 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b8aed6d0-747c-39d4-b2cc-16cbc6a95495 | -10.2318 | -50.209999 | 2025-08-13 01:01:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6a1effc-e958-3b29-a084-64b85440025f | -18.530701 | -46.047798 | 2025-08-13 01:01:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc25ded3-9f31-3eb1-a001-323aea9f7b9c | -9.1748 | -59.656101 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92e7257c-e522-384a-aa35-4f4f952863ef | -16.9715 | -48.410702 | 2025-08-13 01:01:00 | METOP-C | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f444289-6d83-3cef-a451-98ab312532e0 | -7.1006 | -60.0214 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6e23897-3d24-324a-be85-43c09648db6f | -6.6135 | -43.869202 | 2025-08-13 01:01:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 628d9f57-a020-3ca0-aa89-d798ae130111 | -6.2845 | -53.619701 | 2025-08-13 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75fc7115-988f-3e61-b410-7bf8b00ed1e3 | -8.1138 | -55.5606 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 112ac11c-fd62-324d-a553-e06c5dce9c3e | -9.211 | -59.634701 | 2025-08-13 01:01:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c37a1f0e-1b01-380f-b36b-2ce78ec01f39 | -10.2374 | -50.233601 | 2025-08-13 01:01:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bcf55b2-1341-374e-ab8f-434efa154512 | -12.5698 | -47.042999 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adc03fc4-f444-316a-8e66-f9d55996e5db | -10.3426 | -50.813702 | 2025-08-13 01:01:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efee9f48-44f1-30ad-80d4-d7ba90d3bbce | -7.4576 | -59.8778 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6aeed57-d9f5-341e-bdc3-3fd58de60355 | -7.0742 | -59.189999 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa9b6524-93c9-3e01-acc4-28703c6be1e7 | -6.8855 | -59.1222 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6408d986-ebe0-3e53-88a7-21d7ab2cd23c | -7.4549 | -59.864799 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8730de5-0d28-3166-aa89-6ac3d1b537d5 | -20.004499 | -49.0387 | 2025-08-13 01:01:00 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1c44b5e-1451-32e7-bbda-33c3427ecf87 | -9.9481 | -48.331902 | 2025-08-13 01:01:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fba71277-1cdd-3907-9140-028e6e1ee8f1 | -12.5758 | -46.983601 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 209fc401-ced3-397a-91a6-7b3e7c0de091 | -13.1209 | -46.8442 | 2025-08-13 01:01:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7cbb3dd1-b80a-356e-9706-ed0c730f478f | -6.866 | -59.1264 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88108916-6901-3613-bd97-e2144f36c5ed | -7.2701 | -60.620998 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec38880-43b0-3a16-9537-a306743fbce0 | -6.8953 | -59.120098 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca35895-edac-36ea-8e3e-c157d4dd2f34 | -6.9297 | -59.1367 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4825925-06af-3ad4-949d-87dd442ca4ca | -5.8946 | -57.737999 | 2025-08-13 01:01:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2202f182-3ba0-314c-b783-868f3209b6e4 | -10.2337 | -50.217899 | 2025-08-13 01:01:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9753ac76-3e9a-39c9-a14b-9c5bc7319621 | -6.9174 | -59.1273 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25b64005-fd37-34b1-8dc7-e05dc9f77502 | -7.088 | -60.010399 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7e1eb2f-ba5c-39c8-8961-bc11227527c3 | -6.8783 | -59.1357 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36199926-2525-3956-95ac-d07a70cb7da8 | -16.3988 | -50.884998 | 2025-08-13 01:01:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54f013c2-6d2b-3b6d-99c0-f73deb5c0861 | -9.0663 | -45.064201 | 2025-08-13 01:01:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fb3df98-ac5c-3e64-bfe7-42cd8633d8f7 | -8.1202 | -55.543301 | 2025-08-13 01:01:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca9a19a7-2d6b-3266-b92b-e9e6c92b3166 | -10.4165 | -54.396198 | 2025-08-13 01:01:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6d75f26-4c63-31cd-8436-d0764af2a51f | -10.4181 | -54.4035 | 2025-08-13 01:01:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac4956d4-b826-3f88-b96d-a561eceb4247 | -7.2568 | -59.988499 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7185333-50ad-3049-8b6a-47d0a5f6b40a | -18.5282 | -46.037498 | 2025-08-13 01:01:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3e83ee5b-d409-3e52-8f7b-927e9f917393 | -16.312799 | -52.914101 | 2025-08-13 01:01:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69d8accc-65de-3af2-9a5a-1c43fdc84023 | -8.3863 | -49.356201 | 2025-08-13 01:01:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad67e82c-0709-34b5-b69a-a1125edf8568 | -7.1299 | -60.1182 | 2025-08-13 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 1db87f41-0882-3dc6-8009-10c8cfb78713 | -11.7699 | -48.18 | 2025-08-13 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 734cb5d7-3619-3671-ada2-d2c07c77eeb0 | -8.106 | -55.5701 | 2025-08-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a98fa11b-81be-3842-b2ec-fef250a36212 | -15.0787 | -51.364 | 2025-08-13 01:10:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 846e8662-7e96-3374-88a0-c0e4a7d5fed7 | -22.3869 | -45.4716 | 2025-08-13 01:10:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.6 |
| 245d1498-3c7f-3fe9-add2-067d4384bc9b | -8.1246 | -55.569 | 2025-08-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| a6f2c6a9-4ccb-3f38-a204-ee58c92921a2 | -6.6112 | -43.8941 | 2025-08-13 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 68628623-4479-3111-9c24-44c75d64d3c9 | -9.1894 | -59.6558 | 2025-08-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 21e49e7e-152e-3e1d-9dd9-81bc4679a773 | -11.7504 | -48.2046 | 2025-08-13 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f64e8e58-dc0a-3148-9130-8cd35a374fa1 | -7.0935 | -60.0237 | 2025-08-13 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fc7075d8-26d5-3f14-bb7e-aa4f139bd5be | -11.9938 | -45.1496 | 2025-08-13 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 48b7848f-a8bf-3ad3-ae55-6a904e839905 | -7.1298 | -60.1374 | 2025-08-13 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ff2f9145-b4df-330b-a020-79951b5a5935 | -11.7695 | -48.2021 | 2025-08-13 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1ca1a3a0-7535-3b8b-bc19-f04a9cf78598 | -7.1483 | -60.1174 | 2025-08-13 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 03397c27-57a4-3312-868c-cccbc803502d | -15.0981 | -51.3612 | 2025-08-13 01:10:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e11ef5a4-cd7d-33aa-8536-6165e2ba09ab | -11.7508 | -48.1825 | 2025-08-13 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c322403d-27f4-374e-aa4e-f654f949f5fb | -7.2562 | -60.6302 | 2025-08-13 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| d3045df5-2642-385e-a15c-3e0b79527ad6 | -9.208 | -59.6548 | 2025-08-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 51c6b396-a3a6-307c-856f-95bc31e1433d | -21.1405 | -49.1022 | 2025-08-13 01:10:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 28b1e2b4-68ee-3957-87e5-90d516088357 | -7.2746 | -60.6294 | 2025-08-13 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 490b8886-a94a-3cb1-9235-3809934b7995 | -7.1299 | -60.1182 | 2025-08-13 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 171c4387-f679-3f20-a43e-bf8ff36a2479 | -7.2562 | -60.6302 | 2025-08-13 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 88a2ea96-bc12-3dd8-8b5d-28a2d95c75a8 | -22.3877 | -45.447 | 2025-08-13 01:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| f1af4599-6ef9-358f-b05a-200657198292 | -11.7699 | -48.18 | 2025-08-13 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 73372a3c-7d42-34d9-bf92-31d27ab946d7 | -2.9108 | -48.254 | 2025-08-13 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1a32a2a1-52aa-3c68-ba76-beb740711e5b | -11.9938 | -45.1496 | 2025-08-13 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ed2891f4-3cd5-3475-b15e-317a35b0d35f | -7.1483 | -60.1174 | 2025-08-13 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 54871a3b-a801-3d3e-8612-dc9a8cd39951 | -10.9693 | -49.5639 | 2025-08-13 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f4da8a39-b7d6-31c4-9d38-62f753e92ab7 | -8.106 | -55.5701 | 2025-08-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 416d903a-a348-36f8-a3fd-7fba2ed4adfb | -9.1894 | -59.6558 | 2025-08-13 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |


[Clique aqui para ver as próximas entradas](README9.md)
