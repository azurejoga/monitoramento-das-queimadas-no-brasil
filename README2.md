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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca5f3296-10d3-3c3c-b91d-6bf62f64625f | -3.41245 | -39.35861 | 2025-12-31 00:11:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 560ec74a-4b56-3af9-8a1c-70f9e7bf45e5 | -4.31652 | -43.78966 | 2025-12-31 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| e6e137e8-a40d-3c32-a2b9-30242bf9f838 | -1.07649 | -48.00276 | 2025-12-31 00:13:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f9c62957-a92c-3aee-afbc-7f5760472491 | -1.08418 | -47.9925 | 2025-12-31 00:13:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 98b06a91-0701-394b-8384-6ce2eee62fee | -2.09907 | -45.99499 | 2025-12-31 00:13:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dd07b650-7e24-3a81-991c-02fe2c004faa | -0.93333 | -46.89792 | 2025-12-31 00:13:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c7d617b-df80-3e2a-816c-48485853bd4f | -1.07402 | -47.98472 | 2025-12-31 00:13:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4f6ac21-92c8-3632-8d19-1acf5ae29529 | -1.62536 | -45.70869 | 2025-12-31 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ca3f1b36-bf14-3c28-ac21-d401d613cedf | -1.08542 | -48.00151 | 2025-12-31 00:13:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e10252dc-ee30-34de-8e3e-9ea0fed4e1a7 | -2.95777 | -49.28552 | 2025-12-31 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e9205775-8699-315c-b6f3-c8e116aae1d6 | -0.94816 | -46.94038 | 2025-12-31 00:13:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5c673b1-c15e-3c97-8d93-50b6cc651abe | -2.92099 | -49.37819 | 2025-12-31 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| af6c1125-b8c2-3d33-9f27-e1976ca4c5c7 | -2.34126 | -44.88967 | 2025-12-31 00:13:00 | TERRA_M-M | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9cf0074b-792a-3158-824c-ee4da5e1a534 | -2.60318 | -45.5772 | 2025-12-31 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d3f7d12-9c17-397c-995d-af35b5b8baf6 | -1.46279 | -45.73448 | 2025-12-31 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 82a14b7d-7998-3189-8f20-82df32816a2a | -0.77439 | -48.61982 | 2025-12-31 00:13:00 | TERRA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0ee1a45-72c1-3703-a5df-6cf93fc79376 | -2.09021 | -45.99624 | 2025-12-31 00:13:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2042d07-9a4a-315f-9ff0-6d61ec4a39d2 | -0.94695 | -46.93164 | 2025-12-31 00:13:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e6ae256-32da-3bb6-9b54-b8bf00b5084e | -2.65671 | -45.56964 | 2025-12-31 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 611b3a1d-e5d8-3ae6-8669-369d5d6685fa | -0.93212 | -46.88918 | 2025-12-31 00:13:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2f3d345-8dd7-3b25-a48f-8db4632ad661 | -2.90983 | -49.36872 | 2025-12-31 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0d5e3f63-eb3f-32cf-8c23-83a1c834583b | -1.79134 | -45.90243 | 2025-12-31 00:13:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b923d06-ac10-336a-a9e0-1ab3bdecf484 | -1.07525 | -47.99374 | 2025-12-31 00:13:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 2dd342bc-6fe6-317c-88b4-14d73fb96da9 | -2.90769 | -49.37541 | 2025-12-31 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 9e7ad597-6613-34bc-a721-51244b29962c | -2.9092 | -49.38625 | 2025-12-31 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 28bf804e-f29a-3a58-a688-380ee0ea96ea | -1.45385 | -45.73574 | 2025-12-31 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95ec8915-6cb7-390b-a9b8-e5ffaedccc49 | -2.91127 | -49.37954 | 2025-12-31 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 5a7a4d5b-e17e-3a43-8f90-fb8af20ed5e8 | -2.9064 | -49.3667 | 2025-12-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 51c61202-dbc1-33a4-9a84-679ea4962da8 | -17.3844 | -42.6235 | 2025-12-31 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 172.4 |
| c912d53f-3fc5-3263-9564-cf07400e4b8d | -4.3285 | -43.8032 | 2025-12-31 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| ba6bdb2c-2cea-30ca-ad4a-2b1eb5c126eb | -4.3099 | -43.7811 | 2025-12-31 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 338.7 |
| 2fff32c8-4ff6-339b-8475-408618e18b31 | -13.4254 | -43.8639 | 2025-12-31 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 952c79ae-6903-3d40-892d-d440bab89841 | -4.3101 | -43.758 | 2025-12-31 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 42828b0e-5af2-3f84-857f-4c5c0fed9ad8 | -2.9064 | -49.3879 | 2025-12-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fec97699-d079-3384-891d-953c45046503 | -4.3098 | -43.8042 | 2025-12-31 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| cd2ce171-77cc-3101-97fb-c67dfc707f4a | -4.3286 | -43.7801 | 2025-12-31 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 256.4 |
| 4276f849-8254-361b-b89a-1a6ed5c89f3e | -17.3806 | -42.616501 | 2025-12-31 00:25:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f5ee820-e83d-39c5-a153-26b80a07717c | -33.718399 | -53.350601 | 2025-12-31 00:25:00 | METOP-B | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 22d57004-9e40-3cc7-b79c-c7337f084fb8 | -13.4177 | -43.843102 | 2025-12-31 00:25:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa47589b-3b06-3ea6-aa00-e93516f8407c | -15.1295 | -52.9384 | 2025-12-31 00:25:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 118e5028-aa2f-3403-bc79-23a92f998ea4 | -2.9196 | -49.371498 | 2025-12-31 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d03171e-64c4-3941-8d9d-8929a3beae5a | -2.9099 | -49.373798 | 2025-12-31 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76723b5-24c5-31ec-a407-318dec9625eb | -3.5404 | -43.6772 | 2025-12-31 00:25:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d869a7e-0a16-33b8-89f7-1818cbb7e84d | -4.3102 | -43.772499 | 2025-12-31 00:25:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecfdb305-20da-3173-ba43-79c664d6c894 | -33.720699 | -53.366402 | 2025-12-31 00:25:00 | METOP-B | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 4c9651c0-a284-3732-a62c-782854960ab4 | -1.0796 | -47.992802 | 2025-12-31 00:25:00 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfa8163-580e-3268-b428-bb71b6793acd | -4.2533 | -46.622398 | 2025-12-31 00:25:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 090c2d0e-b311-330f-8318-1b3587d946a5 | -4.3247 | -43.7901 | 2025-12-31 00:25:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9d720c0-ffa9-3eaa-9b0b-d942c7392340 | -2.912 | -49.382702 | 2025-12-31 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485f16ac-1c05-3ada-8877-193d94e5dfcd | -4.3199 | -43.812302 | 2025-12-31 00:25:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3bbd195-3685-3712-9edf-863af885cc16 | -17.374701 | -42.6339 | 2025-12-31 00:25:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 035c149c-e8dc-338a-97ae-732d1dde9ce2 | -4.3198 | -43.770199 | 2025-12-31 00:25:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0764f01f-ec09-35c8-b7d9-f329ffcb61c4 | -5.7255 | -45.0429 | 2025-12-31 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8341ca5-9ece-3fb6-a600-2c6f587e1228 | -2.9078 | -49.364799 | 2025-12-31 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c756ea8-692c-3613-a003-2454040ccfe7 | -19.332701 | -54.0214 | 2025-12-31 00:25:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 30f96e97-18ef-37ec-a7da-7cae978784af | -5.7158 | -45.0453 | 2025-12-31 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f416f702-8c69-3488-aced-b4df63688376 | -17.3671 | -42.604698 | 2025-12-31 00:25:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 73a1eb03-6cd0-354d-a601-0c826fe30ba1 | -4.2563 | -46.635101 | 2025-12-31 00:25:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddfe8e51-f00f-3db9-a191-3f0d185e7521 | -5.7121 | -45.0298 | 2025-12-31 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24d67fe4-74ac-33bb-a73f-23535b77405b | -5.7218 | -45.027401 | 2025-12-31 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9053abfd-2c27-3306-b5f8-679a8a17a01c | -13.4213 | -43.857101 | 2025-12-31 00:25:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f21dec76-563d-3920-a041-02a42b91038d | -3.5501 | -43.6749 | 2025-12-31 00:25:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0251462b-29d8-3af6-bcac-95637cee666b | -17.370899 | -42.619301 | 2025-12-31 00:25:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e243c076-a9e1-30c3-b1cd-f1f0eecec1ff | -4.3054 | -43.7948 | 2025-12-31 00:25:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20e7600b-4081-392f-a3f0-a4bdf88c1078 | -4.3151 | -43.7924 | 2025-12-31 00:25:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf17af7b-b023-39d8-9469-c29f748628e8 | -0.0918 | -51.276699 | 2025-12-31 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d07efa85-379b-3799-8f07-d7466296b2d0 | -4.3005 | -43.774899 | 2025-12-31 00:25:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8e372d1-2bd8-3748-8385-bfc75ad3a62f | -5.0447 | -47.185398 | 2025-12-31 00:25:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f23c82a8-63fd-329d-afe7-1dac488f86ad | -17.3844 | -42.6235 | 2025-12-31 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 853a6842-23c2-3bac-85c2-18d6a24e3c5e | -4.3286 | -43.7801 | 2025-12-31 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 5e1dd894-5b09-35a8-aaaf-a907565966e7 | -4.3285 | -43.8032 | 2025-12-31 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| bb7a3a4a-bc30-3db6-b4d9-e17deaa596b9 | -4.3098 | -43.8042 | 2025-12-31 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 178.1 |
| f82afbe9-1803-3ba6-82a1-d224b0318043 | -4.3101 | -43.758 | 2025-12-31 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d74206e8-ab51-3082-b67d-29f762c29b3b | -13.4254 | -43.8639 | 2025-12-31 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 485e3705-2422-32f5-943e-c892ca7c28c8 | -4.3099 | -43.7811 | 2025-12-31 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 324.7 |
| efeed174-270e-34ac-b16b-b98835c72788 | -2.9064 | -49.3667 | 2025-12-31 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 42ab1bf3-579b-30b6-bb56-4e26c009b409 | -2.9064 | -49.3879 | 2025-12-31 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3d522755-2248-3c67-a1ac-7fb9035bd95c | -4.3098 | -43.8042 | 2025-12-31 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 9305b8f4-9ea8-37ea-bf5b-a60992085da4 | -4.3285 | -43.8032 | 2025-12-31 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| ae2797c0-fbe8-3856-a614-5f916ff48191 | -17.3643 | -42.6284 | 2025-12-31 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 431041cb-d255-37b3-bbba-089c408048c7 | -4.3286 | -43.7801 | 2025-12-31 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 243.1 |
| bfdf1c90-7628-3ec1-b9cd-8774a2d3d931 | -4.3099 | -43.7811 | 2025-12-31 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| c935e705-640c-31b5-83d5-9f7fe2bd61e7 | -17.3844 | -42.6235 | 2025-12-31 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 161.6 |
| a99b970d-0726-32e8-91b7-fd66306fdc7b | -4.3099 | -43.7811 | 2025-12-31 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 1fe120ea-5147-3470-bde6-5ccbf6960237 | -2.9249 | -49.3661 | 2025-12-31 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| faef45be-76e6-3c95-933c-13e4e1306dca | -4.3285 | -43.8032 | 2025-12-31 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2d382a1b-1b00-3c84-9ab4-d7634dfe20cb | -2.9248 | -49.3873 | 2025-12-31 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 791b601a-c7a1-329d-b338-b33ac27a2d10 | -4.3286 | -43.7801 | 2025-12-31 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 0f60c269-486e-3664-9255-f8bf75ed3a53 | -2.9064 | -49.3879 | 2025-12-31 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e402151a-b0e4-3ae3-805c-0cf81aedb3c2 | -17.3844 | -42.6235 | 2025-12-31 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 0b261c8c-eafc-329b-9d6c-eb465884f504 | -4.3098 | -43.8042 | 2025-12-31 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 83089195-a37f-3574-8a2a-fdd50d9c90b0 | -17.3844 | -42.6235 | 2025-12-31 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 138.8 |
| e716fd4d-00b7-3357-b397-a2e501b4c47a | -4.3099 | -43.7811 | 2025-12-31 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 880d250d-ff84-3303-beb5-87fd1adc367c | -4.3286 | -43.7801 | 2025-12-31 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| dc8e6a6d-3602-3a7b-926e-db78ae5a182f | -4.3285 | -43.8032 | 2025-12-31 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e8f5f0e4-0b85-352f-b6f3-f334ba2a3ab9 | -4.3098 | -43.8042 | 2025-12-31 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 40dec883-d7d8-3987-ba28-59b2b7c4daa4 | -16.8608 | -40.557899 | 2025-12-31 01:02:00 | METOP-C | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc939f36-4b9d-3931-8d70-da36afc52253 | -4.3003 | -43.761299 | 2025-12-31 01:02:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2aea060f-f1ea-3d08-9fda-49f351d9a4a3 | -17.379601 | -42.6245 | 2025-12-31 01:02:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1de87fa5-d286-32c6-a172-7d37d17696d5 | -4.3266 | -43.784599 | 2025-12-31 01:02:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
