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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7e35bf-77ed-3b17-9870-bfd29b63edf1 | -4.11337 | -49.07061 | 2026-10-04 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fdc7c548-634e-31f8-a4b6-ee8b213cb52d | -4.13586 | -51.1873 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1ef9b6b-dd79-360c-8b02-c13662c80baf | -3.87024 | -55.81372 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 7bdd9cf0-de4e-3cb1-95a1-72dee4eab95d | -6.08145 | -53.47417 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66ff55db-4ea7-3804-b0a4-5759cb7b6b0e | -6.9016 | -43.68465 | 2026-10-04 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68a13eca-fb13-3b70-9caa-2f7c9cc59f28 | -6.57928 | -44.14415 | 2026-10-04 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6d2e26a-a9ff-3fff-bd36-1119888e6a7f | -7.10033 | -44.29321 | 2026-10-04 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6905d79a-2990-3317-ad6f-5ff49e2801b3 | -5.6139 | -47.44177 | 2026-10-04 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c65eeac6-0688-31d9-8465-b4ae7084a5ea | -4.47123 | -50.97136 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2857de4-af27-326e-9cb1-7cc2e7fd77d7 | -3.15901 | -53.0683 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85db8c66-87f2-3e6d-97ed-1da380099278 | -7.89239 | -45.32291 | 2026-10-04 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4918bffc-21cc-389d-b9fa-d06f1c3ea0ab | -1.20956 | -55.86512 | 2026-10-04 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1fdc5206-102a-3083-8f9e-a55b2a4f74c9 | -4.2626 | -46.36594 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 87b942dd-7296-3e14-ad21-f1a69bc97816 | -2.90525 | -54.13311 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f61cdb15-de81-3d61-a2ef-9884a461f341 | -2.80957 | -54.13205 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2afeb3fa-5c13-3ed1-85ec-d398402e5554 | -3.13322 | -53.75329 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8c2c3bb-9396-39e1-b63b-4ceae815ae93 | -1.08785 | -54.11245 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6200654-60b2-3c83-912e-adbf80953f83 | -6.00183 | -53.5258 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 82b85977-61bc-3a6b-88df-a8ed87bc7eb0 | -6.06496 | -53.47781 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd83dd58-8efb-338e-bcdd-2ef4adfacc3a | -2.80342 | -54.09941 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3efe0d97-a7bb-3f62-a37c-3b1c7d095f14 | -6.01889 | -53.52938 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76fe4788-ee24-3749-a44a-ef30b3187d0e | -3.17146 | -48.69521 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20e4b2d3-93a2-3661-a834-0820df9acdde | -6.07114 | -53.47264 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 900807d8-a020-35cb-856f-e6ff9e8a7a00 | -2.97556 | -54.09341 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab0032d3-87ae-368f-a8f2-d3aa99f9c3c2 | -8.3443 | -38.96743 | 2026-10-04 04:19:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32104978-7b39-3282-8a95-dbd2e13d02cf | -4.27297 | -50.26475 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38e4ce49-fc3e-3a75-896f-384a7aa0e9ca | -6.07063 | -53.47559 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db266ee-a226-3cfe-b006-e0701883207f | -1.49687 | -49.45061 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b1442f5-feba-3642-9959-567887a98946 | -3.13009 | -53.73802 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d6cc84d-b05b-35e3-b4e8-e3b64ef9ca28 | -2.21284 | -48.22918 | 2026-10-04 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3684b245-ea72-3819-b19f-14b5c784f1a0 | -6.4183 | -43.46799 | 2026-10-04 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 985fdd58-3fc1-371d-88b9-5364612174d8 | -6.00065 | -53.63327 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4c265dc-635a-35c7-8b4c-3b25bc5ead6c | -6.23523 | -53.14793 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b6f6204-d6a0-373f-8a3d-09eb95bb6849 | -4.28746 | -48.56345 | 2026-10-04 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df7d48c9-9676-361c-bf3c-c1138ddbe01c | -2.81536 | -54.09735 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5467b29-639a-30a4-98a9-06ee5e8a09b8 | -5.62947 | -50.0279 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c449810-f8ee-36e5-b216-3dc1baaf9a0e | -4.15797 | -47.54203 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffc4b80a-b59a-319a-af43-3f41d496c1a6 | -3.18197 | -50.5385 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6f43e17-7d8a-337c-b63d-72b1f4850c2f | -3.81333 | -50.85074 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54300f2-6f07-362b-94fe-8503716a6c11 | -6.30508 | -43.34025 | 2026-10-04 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9d9faed-9e3e-323f-9431-ae2f2003bedf | -3.15389 | -53.06827 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9bf252f-19de-34d7-a025-7e388e29598f | -2.68859 | -54.64498 | 2026-10-04 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bb528be9-b7c9-3869-8e6c-d4009fd7b8cf | -2.96443 | -50.3157 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6bce61e-e4ae-324a-9adb-9c7fc3ececfe | -2.95294 | -54.12536 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5536b13-0f6c-3482-83db-d1d9ea7a2c83 | -2.79841 | -54.09465 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b307fd17-9348-31db-88a3-8f1d0593a6c4 | -5.5547 | -45.25974 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec687da7-a8cc-3267-b4dd-55bc1e703b62 | -2.21455 | -48.22708 | 2026-10-04 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ba198ac-2d7b-30a6-b77f-da98601a2d2f | -5.99832 | -53.55556 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5abcfed8-512f-3a56-aa6c-1c0823129055 | -3.36016 | -43.38331 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f9cebbb-d8e7-348c-8ae8-1410d250c911 | -2.81482 | -48.66201 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d84e01e7-f321-311d-9f09-32c18205625b | -3.17317 | -48.5854 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f32dda6-fb70-3380-af89-4f46a5d9ae7e | -6.00129 | -53.52897 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ca01d06-09f9-36be-a837-0fb19b39a67b | -4.4346 | -45.63046 | 2026-10-04 04:19:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82434329-f766-3ae5-97ee-81b8a1c6d194 | -3.14106 | -53.73984 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 302e9333-4da8-318e-a990-8e8362d8e8e9 | -3.30085 | -53.83718 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a78baab-20c3-3359-98be-146f6c18db0d | -1.46362 | -49.46572 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e8753b-ce3c-3d8d-9ac6-080f6541dba4 | -3.11185 | -53.74612 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 27ca15ec-5b74-3db6-9539-2925fbd3cc76 | -3.95788 | -55.77854 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d92252e-5e32-3ea9-9249-11dc57648327 | -4.28904 | -50.27051 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 79380bb9-8d3c-3c48-b4ed-cf6d4fec6eaa | -3.19012 | -54.09658 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1eeaa090-5fa9-3c6e-a1e4-ae0e30655857 | -3.07563 | -51.27488 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45a63b65-8d24-3a59-b2d6-3e84d26e1eb4 | -1.35145 | -56.09845 | 2026-10-04 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a47ba043-cc32-3120-b00a-4a5511015e6e | -2.92871 | -48.75347 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d227c225-5b85-3d3a-a034-32e161e713d3 | -4.04228 | -48.98745 | 2026-10-04 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 945b237b-44cc-359f-a51a-b403e4e13f2a | -5.34315 | -44.82678 | 2026-10-04 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97763b9c-9593-39c6-9ab4-c90f644acb61 | -5.57208 | -49.74549 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c202cd68-75f7-3eef-aa6b-9e877dd8fded | -5.00502 | -45.14121 | 2026-10-04 04:19:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b224debd-ab26-3bb9-9fe9-37aff03a0180 | -3.18637 | -50.5392 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d1f4bbe-2c33-369a-8efe-a55f0bfb8b10 | -2.8896 | -54.12264 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 845b34df-d8a3-3b02-9efc-a31589c14460 | -5.12199 | -42.4046 | 2026-10-04 04:19:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81d7353e-e50e-3b4c-b821-912cdfef2e89 | -4.20985 | -53.46149 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c783fb0a-6682-3603-b3e8-a60e05ca290d | -3.09906 | -51.1023 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c1297af-b2f2-33e8-91fc-b863cde01b40 | -3.00437 | -53.88234 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70538d6e-c56f-35d1-82d6-9fdf7eb01bd0 | -3.11363 | -53.73535 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 67ff47b2-e1a3-3083-a0f3-7250e53dc5dc | -6.31574 | -43.33821 | 2026-10-04 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da62e82e-7b0f-36b0-89c0-6ce99e8e366b | -5.29761 | -46.59484 | 2026-10-04 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feca7418-0aa0-3dd7-96f0-d47914ca24f2 | -6.35713 | -45.6113 | 2026-10-04 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f95f8075-c548-3dd1-9f2e-b8b650266d43 | -3.17387 | -41.39665 | 2026-10-04 04:19:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2c2a074-593d-303e-aeb6-9f33830d47ca | -2.58448 | -51.8671 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 590223d1-7b4e-3d73-ac74-cede26e1f128 | -4.23328 | -49.67632 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3abd0079-6d1c-37f5-bdaa-08945f4c792e | -3.21024 | -50.74766 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b30f691-29e6-313c-8610-15e5510c20ab | -5.78471 | -49.84917 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a21b521c-dcd4-30b4-84a4-068c04bf3cef | -5.54439 | -49.7627 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8bce06f3-a12a-37ac-8658-27351ba441be | -2.97418 | -54.08865 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0276b115-2471-33f5-bf16-97c504ea22a4 | -3.4764 | -50.09112 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e21802d-7052-30ce-b047-cc03a79228dd | -2.68243 | -54.42676 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9b308b62-3922-34cb-b2ac-3df0f8a2491f | -3.12224 | -53.75148 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 615da692-b05f-3797-a91a-fb370ef3ebd4 | -3.80814 | -50.85453 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64dd2dc9-f143-38f5-8b4e-b63aef9e1095 | -2.9798 | -54.0896 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84e15d6f-b985-32ba-b2ca-bb5c34df3b9a | -6.08469 | -53.30287 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69b05659-b241-3008-969a-6b38caf29dae | -3.11125 | -53.74971 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9eb2e390-7d8b-3ce3-97bc-960ea732beeb | -4.51616 | -45.89105 | 2026-10-04 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96929d36-a7dc-3d1d-9780-a269a02d036f | -3.86486 | -55.80785 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 14b7fca5-1b41-3faf-8eff-5f3e23258629 | -1.56292 | -46.86064 | 2026-10-04 04:19:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 533aef02-562f-3a6c-910a-3c541c1b0e8a | -3.35353 | -43.38229 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c63896bf-1b9b-3e26-a1e8-97fc9a9e12e6 | -2.58384 | -51.85256 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 86305d7d-d5c2-35b3-8bf5-2b67ee7f1b5d | -2.80971 | -54.09647 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 038e1afd-4b89-3c54-8623-0090ac12edfb | -2.24932 | -51.93096 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e684952a-ec14-3cc0-8196-aba90e52ce5a | -2.81587 | -54.12911 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b05ef5bc-b8af-33c1-a3cc-9602f015937d | -4.27234 | -50.26871 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README30.md)
