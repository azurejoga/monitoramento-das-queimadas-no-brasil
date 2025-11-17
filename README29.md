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
| 7afd3a36-c1dd-37d7-acac-82e4fbe79d61 | -7.70895 | -42.94538 | 2025-11-17 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1103c3f-6dfa-311e-b585-50bcdf77685e | -6.44521 | -44.21729 | 2025-11-17 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61216823-f973-3483-aba3-beb0050b5cb4 | -2.52239 | -47.82144 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef6de126-ad6c-3cdc-9f5e-ab70eeb0aec5 | -3.18241 | -50.65037 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b02a4287-c934-3ad8-bdf8-ebd3d193a6af | -3.66144 | -44.73037 | 2025-11-17 04:38:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 896d636e-19ce-37cc-b6fe-e5a0de395888 | -8.1496 | -46.72346 | 2025-11-17 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a123972e-330f-3bfa-9538-9e85c2581431 | -3.14759 | -51.32075 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a567e894-ed2f-3405-ba7a-a624e40781f8 | -5.51943 | -40.96795 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc40df78-a384-3654-b195-1caf053f8031 | -4.40384 | -45.83503 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fec4252-69b1-383e-a8af-1ba2c069f792 | -8.11593 | -43.53553 | 2025-11-17 04:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 349491f8-9142-3a1d-8006-5d5e12d7bc80 | -5.41025 | -44.06359 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e44962d-528b-3d63-b4b3-e8d595430dfc | -4.54986 | -48.47465 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efcd847f-aa54-3130-8d45-ddb812cbeadf | -3.52099 | -50.53216 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d03c9e1d-32cb-35bb-aa18-9c3f6bdcfb6d | -5.47369 | -40.96415 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0101644e-35f9-3b43-9bd3-ea59fc44bc5e | -8.05379 | -45.66086 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 130dcac4-1613-3353-b79b-842b7704f213 | -1.17805 | -49.19159 | 2025-11-17 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fc9bd85-9b40-39bf-ac6d-5e88a2bf249f | -2.86432 | -44.10296 | 2025-11-17 04:38:00 | NOAA-21 | AXIXÁ | MARANHÃO | Brasil | 2101103 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1751ab43-b671-338c-8266-4cef6a685d29 | -4.38603 | -54.83001 | 2025-11-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06aabe3e-fc39-3d8a-aae2-9b45e8a80654 | -4.6402 | -45.90223 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a18a011-875b-34ce-b005-f067125932b7 | -8.81059 | -40.40643 | 2025-11-17 04:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 83472633-4628-33fa-a698-cbb7a1c587db | -4.39541 | -49.65488 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28af8adc-c60d-36ba-9d21-691aa2e070f3 | -3.07824 | -45.19765 | 2025-11-17 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9a7c48f-02d3-3d63-8b50-6959590b1235 | -3.25092 | -50.68344 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0d281a4-9b47-310d-a496-ec8e4621d159 | -3.07758 | -45.20189 | 2025-11-17 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf2a40a0-ce67-39e3-aa53-f7bdfa242514 | -3.85333 | -51.31038 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 83feafb2-dcc0-3cb5-80d9-099451b0b94b | -4.16466 | -46.84356 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdaa89a4-a643-3bbe-afa8-6ca7ffb6d649 | -4.40679 | -45.83971 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b34a4654-de4e-3ccf-82ba-62c18a9971b5 | -6.68837 | -42.04041 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6222c8f2-ae53-3378-951e-b0d6b1e8731c | -6.54265 | -42.20844 | 2025-11-17 04:38:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b35a4fb2-7546-35a4-a5a6-be90c30d29fc | -4.2143 | -49.14053 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07d37ae0-68e4-3851-8fcc-b351579b9a5e | -5.88517 | -43.97692 | 2025-11-17 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 961b7e33-b0d6-3b44-810f-9d86537b5c61 | -3.1484 | -50.202 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fe87c7c9-3503-368b-805c-2c1592420e28 | -2.59147 | -51.83269 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf423680-2a92-36e7-9239-a7755ab8f24a | -4.06239 | -47.50055 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31692061-ec5d-3877-9b5c-f4c2c614d5c8 | -3.58438 | -50.41819 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 108e4fee-d035-370f-8d7d-949e51bbc7ac | -7.36557 | -45.83347 | 2025-11-17 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae0eca60-79eb-312c-992c-2d19c59c733c | -5.79943 | -43.99296 | 2025-11-17 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8bfb756-d27e-3091-8274-40d78af9f771 | -4.09961 | -48.02438 | 2025-11-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 90f49cea-08b4-3f4d-8f5d-dc18afcb57de | -3.15178 | -50.20252 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bc53282-6e5e-3b60-88bf-3a1f079721ea | -5.35197 | -50.42989 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db273d33-893f-3bd6-b99a-63da50f73992 | -5.58839 | -44.89592 | 2025-11-17 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ab24562-877a-3071-8479-a23a95fd3024 | -6.37535 | -42.29546 | 2025-11-17 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 431fe9da-435a-32cb-b9fe-dfea9c39ea4b | -1.97077 | -44.7998 | 2025-11-17 04:38:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88a15b01-8fbc-3452-a425-26adf09c9c2b | -3.96213 | -49.9418 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a515bb3b-5ccc-3cc9-9b20-754a7f969ef6 | -3.49953 | -50.44206 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff1bb41a-f746-3813-9ecd-84443bbc24fe | -4.76094 | -45.77618 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26eb512c-408b-3618-98d2-cfcecbcb4149 | -2.89204 | -53.2817 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 70c3d4f1-06bd-3462-b7e1-36bedee3130d | -7.22045 | -47.98288 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a238d431-52f5-3723-91a7-1e8ffce0fa7f | -6.68386 | -47.38659 | 2025-11-17 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57fd2318-a46e-3517-9df6-6d6c8ff2ed31 | -5.78483 | -48.58319 | 2025-11-17 04:38:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f43776dd-52a1-3c5e-b138-3fe26449e592 | -4.45873 | -50.17923 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dfd4609-b02c-309c-93db-3e317f0be3c6 | -4.70127 | -46.30804 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adfea2bf-8cfc-343f-8fed-cfde63be1978 | -7.09762 | -42.72559 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 81f22064-91d7-3269-b109-5dec4d7ec5ab | -3.34589 | -50.19911 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7635cfc-ec57-3d35-b165-6c6eeaf6771f | -7.18466 | -44.65132 | 2025-11-17 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1272e6d-6dbe-3b47-a28c-9dbb7e6b267b | -5.46752 | -40.97155 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 72b1661e-4cc8-3ee6-8810-375e170b37e9 | -7.36995 | -45.82957 | 2025-11-17 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98b9080e-bbaf-3f7f-99f6-87bc4ca68a5a | -3.30555 | -53.85085 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5848979d-5ff5-351a-9cde-cd3f63deab7f | -7.70831 | -42.94999 | 2025-11-17 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3c64797a-14c2-3ed4-9740-5bb49422a596 | -7.13296 | -47.13072 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 255b9d04-cde4-31a0-9384-e5dd35e71edd | -4.255 | -46.82618 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e63c2dfe-eb38-3dc5-8a5f-4fbe2b13bfdf | -7.96774 | -50.00307 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3d419b76-03ff-3bae-b282-442c95e8f295 | -3.60008 | -50.71842 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9235c263-6524-319e-9bec-b4e3c3269ed3 | -4.28572 | -48.61994 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06f231a4-114f-365a-b469-b4a94853829a | -3.23788 | -50.49966 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 734eb6ae-e55b-3a86-b9d4-1eee8ef8a2fb | -3.65062 | -50.22828 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f4ffc47-27a2-3bac-8452-8e0aa2aadd4f | -8.32244 | -45.40581 | 2025-11-17 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cc8fcdd-813d-3fea-bddb-23d371a68771 | -4.21208 | -49.13313 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce9ffcfd-fc5d-3aee-922a-9e09421cfa3e | -6.22196 | -46.98465 | 2025-11-17 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14039c6a-b0b9-3075-8eb4-e28909d538ec | -7.54033 | -47.04978 | 2025-11-17 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8812ae0d-9f89-30f8-a8d6-d714a0de84f1 | -7.21708 | -47.98236 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c30e5b1d-a9be-3403-80bb-cd6d8612e554 | -4.69404 | -46.30403 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0a528b2-970e-33ce-bd1d-2c8dfbef88d3 | -6.48542 | -47.53879 | 2025-11-17 04:38:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ade42cb-d2dc-3226-9cc2-0b6e4c509cf7 | -3.19707 | -51.00515 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 528c90dd-9bba-35d1-8e60-6016bf6359c3 | -5.19669 | -47.24792 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cebc9283-cf84-3204-a19b-c5ed8d71c7f6 | -4.16448 | -50.19126 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cc375f9-19d4-30f6-85bc-251392510c11 | -3.69679 | -49.22799 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8338a8ca-db5b-3237-9f8c-135c35307996 | -2.50583 | -47.81888 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4454eb70-13e5-31a5-b707-88c4857470bc | -3.37853 | -42.20205 | 2025-11-17 04:38:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7efa1db-184e-3431-aea1-cdf3389ecf96 | -3.83744 | -42.01556 | 2025-11-17 04:38:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5865a8bf-f1be-3568-b8fb-8340ad80c0cb | -2.69208 | -51.79064 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1d2d2a3-dadb-3b70-a1e6-a9ffb7d909b8 | -4.6329 | -45.68515 | 2025-11-17 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 713231a4-f7b8-35dc-be70-c04f6d92c70a | -2.58782 | -51.83212 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9f05274-3a74-3f15-ab9d-a84f02cf766d | -5.15522 | -46.12826 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e324b84-8a17-379f-aa1a-dc53e2e2c689 | -5.64263 | -51.32341 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09998ded-140a-3253-8576-f23205cecdb1 | -3.41013 | -50.12076 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b5655a3-7881-3ce8-af23-eb5042d8b09e | -4.72569 | -46.3842 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c3b87790-caac-3a19-8c11-83bec951e140 | -4.69717 | -46.31137 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8876fa4-9f1b-37d0-8a9c-40e981e3691c | -3.08754 | -51.04321 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e22cac2-ac7b-3357-b6a0-33a086d36f33 | -4.69306 | -46.31477 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 258a1815-43f8-3a69-b73c-a36f335c4416 | -3.13461 | -50.28886 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5beb6740-188f-32f6-bf41-99474cf65b0d | -4.69658 | -46.3153 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4885258b-0e51-3cfd-82df-16ba028d6aa3 | -6.40815 | -42.33009 | 2025-11-17 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4bf04bf8-7826-3f7c-abc8-31f2c8026818 | -3.9124 | -50.03911 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c454e86-7724-3330-a0db-0e093c559aca | -7.06002 | -41.58847 | 2025-11-17 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 176092df-6517-34b5-87f4-70a8f6b98d27 | -4.7304 | -46.37682 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7a1d033-a673-3060-9cd0-53e3960d9300 | -5.45305 | -48.0909 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3172e2e6-5ca9-3021-99b2-00453c0e96f9 | -6.69237 | -42.04614 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 09444ad3-4c56-38f4-82a4-cc5c419e4bdf | -5.11496 | -46.22983 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 378b1c2b-1689-3471-bcec-c33acb712d6f | -7.09243 | -42.72964 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README30.md)
