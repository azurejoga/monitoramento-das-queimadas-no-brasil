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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20834310-7e5c-3b65-bec9-f03cb2ac5d79 | -21.54224 | -57.52228 | 2025-12-04 12:59:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8aaf255d-affb-395e-a748-3c4b23ed67d8 | -19.79279 | -56.66877 | 2025-12-04 12:59:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| ab60cc20-c65c-3184-801d-7561e69f43fa | -21.62499 | -56.13388 | 2025-12-04 12:59:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5739c5f6-f53f-380c-88a8-58fbc2574125 | -23.66908 | -53.56066 | 2025-12-04 12:59:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| f3e84060-e6ac-3a96-8f6d-96b2f14a1f77 | -4.4079 | -43.1252 | 2025-12-04 13:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 9e74d767-6df0-3720-9152-b8b43eb4b12b | -4.3892 | -43.1263 | 2025-12-04 13:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 133b2efb-7c98-335d-8701-57a2d552fbfa | -4.389 | -43.1497 | 2025-12-04 13:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 032d2b24-9be3-3275-9c4a-955a7da01bb4 | -3.686 | -42.0108 | 2025-12-04 13:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 173.3 |
| 448392d7-8638-3f80-a5bb-f721c270e422 | -4.4077 | -43.1486 | 2025-12-04 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 98f8d9d2-8a05-3be4-a6ed-f6fa7db0ade3 | -4.3892 | -43.1263 | 2025-12-04 13:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 204.8 |
| ef7e16d3-8382-3b3d-b603-7ae1fb759673 | -3.4683 | -40.8691 | 2025-12-04 13:10:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 54f68e44-5310-3516-af8b-40eae14681c6 | -4.389 | -43.1497 | 2025-12-04 13:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 2321797c-588c-347d-8211-6695dbee828d | -19.6442 | -56.8311 | 2025-12-04 13:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 5f69cab5-3318-339e-ae3d-b8ad73192c20 | -4.4079 | -43.1252 | 2025-12-04 13:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 65c9c5f3-1aa3-3160-8d6e-32f851ae3a2c | -2.9567 | -42.0924 | 2025-12-04 13:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 236.0 |
| f36d4be2-ba0e-3af5-a228-49b293afb5a0 | -4.3876 | -43.3595 | 2025-12-04 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d393859e-b4e4-3dfc-ab0d-2e0ca986c0ba | -3.6859 | -42.0346 | 2025-12-04 13:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| f8c67190-ce08-3dc0-823e-47803f7303c7 | -4.4079 | -43.1252 | 2025-12-04 13:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 0465abb5-809b-3741-9ee1-f08c73c719d6 | -3.4462 | -41.4495 | 2025-12-04 13:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| b802545d-4794-311b-8143-dccd6f4c49de | -3.686 | -42.0108 | 2025-12-04 13:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 62bacb0b-50c3-357d-a10a-877f67632b9d | -2.9567 | -42.0924 | 2025-12-04 13:20:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 7c2df62c-285c-3f12-8cac-5b1ee0b1d307 | -4.3876 | -43.3595 | 2025-12-04 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e1725b70-d28a-3e9b-9f4c-b191a6aea5d0 | -4.3892 | -43.1263 | 2025-12-04 13:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 225.1 |
| f48d0f4d-0436-3a85-9721-1ec6e5b5e52c | -4.389 | -43.1497 | 2025-12-04 13:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| bd88f8ae-8b88-38c0-880e-c2e963746332 | -4.4079 | -43.1252 | 2025-12-04 13:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 9606745c-29d4-35b5-b978-0c340ab48179 | -4.3892 | -43.1263 | 2025-12-04 13:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 234.4 |
| 21de35c4-8551-3811-9354-16362906e6c3 | -19.9548 | -57.394 | 2025-12-04 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| e9bed94c-b598-30ab-b2f4-4301da6cce57 | -5.0238 | -41.0144 | 2025-12-04 13:30:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 5b4ce899-4c6b-35c7-bfea-9cc0d902301c | -2.9567 | -42.0924 | 2025-12-04 13:30:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1383a685-d04e-3a34-aa1e-2b4410fa83be | -4.389 | -43.1497 | 2025-12-04 13:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 3124aaaf-057b-33ec-b1c2-42dfe029c60b | -4.3876 | -43.3595 | 2025-12-04 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7675a5f2-c0e1-30cd-8f78-8f7ec9f62c1e | -8.1599 | -36.703 | 2025-12-04 13:30:00 | GOES-19 | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 92.1 |
| f42c304c-17d2-3724-97c2-80d0c82c1748 | -19.9548 | -57.394 | 2025-12-04 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 6cbbeed7-5e5e-36df-a2d0-0ab11194badd | -2.9567 | -42.0924 | 2025-12-04 13:40:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 63e008b3-092b-3070-94e1-058ed4789ad6 | -5.0238 | -41.0144 | 2025-12-04 13:40:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 9b98da53-db31-35ca-ab9d-e6631a004cb3 | -4.389 | -43.1497 | 2025-12-04 13:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8b254208-77b0-3009-9745-8f2a7be36704 | -19.9742 | -57.4331 | 2025-12-04 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 5361722d-1978-30a9-8e16-e731b46d69c2 | -4.3892 | -43.1263 | 2025-12-04 13:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 66d3fbc6-6638-32c2-8d94-22b8391e040f | -3.686 | -42.0108 | 2025-12-04 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| bac821ad-bf63-3438-97c1-ad2a3c9506c1 | -19.9742 | -57.4331 | 2025-12-04 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| c597c64e-0bda-373a-b157-6dbae076bd4e | -19.9548 | -57.394 | 2025-12-04 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 0f0b96ab-bdfa-3823-9fd4-fe54e38512c8 | -3.686 | -42.0108 | 2025-12-04 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 3acf8e35-56a0-3b75-aef1-1d907080d4ea | -5.0238 | -41.0144 | 2025-12-04 14:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 15942024-5a31-3cdf-b026-e0740e6cde3b | -1.1901 | -49.0414 | 2025-12-04 14:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 3edbe2cf-f668-3b0f-b0bd-734927c72760 | -2.9567 | -42.0924 | 2025-12-04 14:00:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a4fc9361-f3f2-37ed-931f-5bb567e55111 | -19.9742 | -57.4331 | 2025-12-04 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| d444c302-e594-3260-ba31-82741f6ca3cb | -2.9567 | -42.0924 | 2025-12-04 14:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7b08d3bf-c581-30bc-9a51-b96d010fcf95 | -2.135 | -47.8865 | 2025-12-04 14:10:00 | GOES-19 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 56dc113d-75bd-3740-8eb1-0434146550ed | -1.1901 | -49.0414 | 2025-12-04 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |


