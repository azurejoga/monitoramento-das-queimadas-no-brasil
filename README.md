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
| 1b08322a-7ad8-3b05-ae06-d2f30e56b30d | -10.8832 | -56.4367 | 2025-07-02 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 115f8f76-a586-334c-89dc-2f774cd46f8c | -7.7944 | -44.0377 | 2025-07-02 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 4d1c8c87-f876-31fe-8151-6a3e7420517b | -7.795 | -43.9913 | 2025-07-02 00:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 921a13ee-f9fb-305a-872a-89c45659aba2 | -3.0356 | -49.4264 | 2025-07-02 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2c60a9df-e51f-3cd8-b8d4-e82f61d50967 | -7.6051 | -45.7464 | 2025-07-02 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 182.9 |
| abb608aa-5610-3c7c-a8f2-ae8f8d78881f | -7.2217 | -43.0917 | 2025-07-02 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 235.9 |
| b4e03efc-7d00-3d84-adfc-7da38063a8b4 | -10.9018 | -56.4552 | 2025-07-02 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d2a13db1-03bf-396e-8a02-c8ee5cffa31e | -7.7758 | -44.0164 | 2025-07-02 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e8aa6de0-700c-350d-88b5-ee3056235d52 | -7.2031 | -43.0701 | 2025-07-02 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 09236d5d-8468-3a13-bc02-8212a601ffdd | -7.8133 | -44.0358 | 2025-07-02 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 922a4db2-b606-3f8d-89cd-2141869a90fb | -10.883 | -56.4567 | 2025-07-02 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 48bc00e8-edc0-3f76-9c97-3f97ccffb0bb | -7.2028 | -43.0936 | 2025-07-02 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.8 |
| 6704e888-6321-399c-9141-a00b41b2e3d8 | -7.7947 | -44.0145 | 2025-07-02 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 355.6 |
| aa2fa71a-5270-38b9-a0c1-5db0316441c7 | -6.7093 | -51.4165 | 2025-07-02 00:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 39bfa38f-3a38-3700-905b-484640b45b68 | -15.9333 | -43.5166 | 2025-07-02 00:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 813a678c-2ed5-3b05-a62a-1d272d324ddd | -7.2219 | -43.0682 | 2025-07-02 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| e0ada9bc-d8bf-3368-a118-da9766cd6f74 | -7.6239 | -45.7447 | 2025-07-02 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 82220995-6e08-3eb5-b421-1d2a41c10481 | -7.8135 | -44.0126 | 2025-07-02 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 65c0f654-4e0f-3adf-a1aa-87afcd2fb8a8 | -3.0355 | -49.4476 | 2025-07-02 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 78c24a31-907c-31e9-8ddc-bc473193685b | -7.6239 | -45.7447 | 2025-07-02 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 541faa83-141d-36d6-a4ec-a935ae975d83 | -7.2028 | -43.0936 | 2025-07-02 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 022845c6-9e74-38c6-925d-7b40ad4adfc4 | -7.6053 | -45.7238 | 2025-07-02 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 37d1d18f-0fef-39ab-8353-75b9a8986660 | -7.7947 | -44.0145 | 2025-07-02 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 342.7 |
| bf3ddee5-f5a7-3038-b48c-014c9860b153 | -7.6051 | -45.7464 | 2025-07-02 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 180.7 |
| c23549eb-54c8-323d-bbf9-38bc83e970bc | -10.8832 | -56.4367 | 2025-07-02 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9266d878-8882-3f7f-a95e-b02fb7de3d3d | -3.0356 | -49.4264 | 2025-07-02 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bb9cfcd7-db69-36b1-8886-cb247c812799 | -6.7093 | -51.4165 | 2025-07-02 00:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ffd9ba11-7845-36aa-be72-12da448a1d0d | -7.8135 | -44.0126 | 2025-07-02 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 294c06ae-3eb3-31a6-a408-e1de8ebf18ba | -7.7944 | -44.0377 | 2025-07-02 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 68c0e1bd-5407-341c-b1b3-2faf665b69d9 | -7.2219 | -43.0682 | 2025-07-02 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| a433ce56-f33f-34ae-bda1-3c3c56cb4740 | -7.2031 | -43.0701 | 2025-07-02 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| d63fcea6-84aa-31a6-ae75-07f3b9ce2927 | -10.883 | -56.4567 | 2025-07-02 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 68a8ff2c-7664-32fb-be7c-e0ff1d970312 | -7.8133 | -44.0358 | 2025-07-02 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a9c0ba86-0b65-3c91-a5df-226a48cbd2bd | -7.7758 | -44.0164 | 2025-07-02 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c6a1e311-61af-3b6f-8d25-806b7bc81292 | -7.2217 | -43.0917 | 2025-07-02 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| 61e416e0-81df-39df-8c20-0eee9c47c9d5 | -3.0355 | -49.4476 | 2025-07-02 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| aed48e90-ea4b-3c8c-8f20-85b4e8e38957 | -7.2217 | -43.0917 | 2025-07-02 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 229.7 |
| f479351f-0c2e-3c42-89e5-5ec7c906f509 | -15.9333 | -43.5166 | 2025-07-02 00:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 90374da4-1efb-38dc-9faa-1b7b8cfe8283 | -7.2219 | -43.0682 | 2025-07-02 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 659540fb-ab6b-391e-89cd-1c6b058a4e34 | -7.7947 | -44.0145 | 2025-07-02 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 272.9 |
| 5d3dc77c-8f31-30ec-80e3-9fba5f14d326 | -3.0355 | -49.4476 | 2025-07-02 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 77c9bbb1-93e5-3f7f-ad1f-c15866dfd961 | -10.9018 | -56.4552 | 2025-07-02 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3f1819ef-62e9-3534-bb20-455458d3e5a6 | -7.7944 | -44.0377 | 2025-07-02 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| c20eebf7-90a0-39a4-93c2-6b9bb88590f1 | -7.0943 | -44.3819 | 2025-07-02 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7661ff04-a7cd-38a9-991a-9746e21a73ec | -7.6239 | -45.7447 | 2025-07-02 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 6d030e63-2c78-3123-ad49-c6c60e2554b2 | -7.2214 | -43.1153 | 2025-07-02 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 8b361b5a-aedd-323d-a352-6ec48e204654 | -7.2028 | -43.0936 | 2025-07-02 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.5 |
| 7bd3c2a6-a518-3a26-883b-ebd953b307ea | -7.795 | -43.9913 | 2025-07-02 00:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3391702b-d47b-3e79-b650-bc260bb21156 | -7.8135 | -44.0126 | 2025-07-02 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 95e9c314-4bf2-3987-81ca-5215b565dda5 | -3.0356 | -49.4264 | 2025-07-02 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 7131a003-21a2-3775-87bd-cd7a3892dede | -7.8133 | -44.0358 | 2025-07-02 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 542ffa18-c245-351b-8276-63efe1824264 | -7.6051 | -45.7464 | 2025-07-02 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 47649618-4b98-3e15-975c-abd16e28d12b | -10.883 | -56.4567 | 2025-07-02 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b68d79af-b444-3abe-846a-1b3145331cce | -19.51353 | -43.59988 | 2025-07-02 00:20:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f575d86e-bef7-318d-b46d-8c979779936a | -20.24016 | -41.89333 | 2025-07-02 00:20:00 | TERRA_M-M | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 8af277bb-76f1-3175-b86d-943ba89d1aaf | -20.6675 | -48.44648 | 2025-07-02 00:20:00 | TERRA_M-M | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 1a6f9428-8d5e-3d76-9d20-e79b20806881 | -20.96293 | -43.08567 | 2025-07-02 00:20:00 | TERRA_M-M | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| d2125d28-ec0b-35d6-b405-9d6cac555055 | -19.52259 | -43.59844 | 2025-07-02 00:20:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f4ad948c-afac-3945-86a5-b0ad4d570234 | -19.44274 | -48.54873 | 2025-07-02 00:20:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 5d47cb02-695c-361e-a290-c7a3e97e5017 | -19.44421 | -48.54181 | 2025-07-02 00:20:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7cca5fdd-6848-3343-8f14-2019ee8f70a5 | -20.66541 | -48.42625 | 2025-07-02 00:20:00 | TERRA_M-M | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7163a9d7-8ff4-373e-9c15-2119c7c5608b | -20.96163 | -43.07582 | 2025-07-02 00:20:00 | TERRA_M-M | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 9351b0ca-c071-39f2-915a-fe048e47964a | -19.44626 | -48.56191 | 2025-07-02 00:20:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 40518c4d-8874-3d4e-9e10-12d5e64a266a | -19.52389 | -43.60844 | 2025-07-02 00:20:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d3bbb1bb-6373-3493-a9b3-799382953fed | -20.23885 | -41.88395 | 2025-07-02 00:20:00 | TERRA_M-M | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| aca39898-e56f-36bc-bad6-669007f4f0ef | -11.13802 | -43.33515 | 2025-07-02 00:22:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e16b6588-53cc-313f-abff-245eb673cf34 | -15.92458 | -43.51006 | 2025-07-02 00:22:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 93a27a8d-ba0c-3f12-b693-3a3f942bfa52 | -14.45091 | -48.86737 | 2025-07-02 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c4c31b97-1ae4-3053-a6f4-f3c30777f514 | -11.2418 | -49.48195 | 2025-07-02 00:22:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5fbb584c-1d61-30cc-957e-75ffad5ce46b | -12.43913 | -50.03768 | 2025-07-02 00:22:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| aad53c12-8802-36c0-99bf-38ce44627a4d | -13.36399 | -46.18969 | 2025-07-02 00:22:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9dd94947-0443-3cfe-a6fe-f31cb0d51b23 | -16.42722 | -44.52511 | 2025-07-02 00:22:00 | TERRA_M-M | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 72e4f39a-cd29-37fd-bf15-c1d72ef85c8f | -17.21729 | -44.80705 | 2025-07-02 00:22:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bcbfd446-707a-3af0-9f1f-05475be63535 | -12.32438 | -42.53783 | 2025-07-02 00:22:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bf50cea5-57c6-3156-ba54-92ad5d077e7b | -14.90111 | -45.14534 | 2025-07-02 00:22:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d76f85bf-a425-34c5-8d9a-625a9fa9725d | -15.92583 | -43.51929 | 2025-07-02 00:22:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f26a2e17-7949-3cc0-8d40-d2ebbda9bfa0 | -11.78504 | -46.43215 | 2025-07-02 00:22:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f0eb6fe-af9c-3c94-9011-1a1955e5a416 | -10.99335 | -49.3949 | 2025-07-02 00:22:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 0fd23707-70a7-325e-8d2c-39f1d0ccf4fa | -15.92708 | -43.52852 | 2025-07-02 00:22:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b64cd7b7-ee9f-397d-8d65-fe7eafa6df20 | -11.14562 | -43.32479 | 2025-07-02 00:22:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 60d0257e-2e25-3445-9a74-c67e12783f89 | -11.14689 | -43.33384 | 2025-07-02 00:22:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 265fadec-a98d-3684-84a6-5e678f0dbf15 | -16.29872 | -45.10293 | 2025-07-02 00:22:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 84c077cc-a276-3a7c-a0ce-7d6af07338b5 | -18.03583 | -46.06038 | 2025-07-02 00:22:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 31ce7936-9be5-388c-a1c2-ead09c79138e | -11.23791 | -49.50542 | 2025-07-02 00:22:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8402d63b-44af-3e06-8196-7a54fd6573e6 | -17.4883 | -46.74211 | 2025-07-02 00:22:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 0c9019bc-6815-3a94-9524-573b015eb257 | -11.83943 | -43.80425 | 2025-07-02 00:22:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 21187c7f-3c5e-319f-b26a-ea13ada988f9 | -16.42594 | -44.51526 | 2025-07-02 00:22:00 | TERRA_M-M | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1b0274ac-b9e1-3423-a483-2ba626a40db7 | -11.2438 | -49.49901 | 2025-07-02 00:22:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c6118632-d3cb-39d1-8f27-e9692a31b732 | -13.20991 | -43.12669 | 2025-07-02 00:22:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 73d854f6-5283-38e7-be85-0ab76aaf0c53 | -11.23578 | -49.48838 | 2025-07-02 00:22:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b987f4a8-4e06-3ed4-8778-c53e46f4e998 | -12.76903 | -44.40631 | 2025-07-02 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 258d7d72-51bd-3730-b671-e6fcd58813c3 | -7.80522 | -44.01213 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9908aa8b-50d4-3b2a-a1e1-f6fafa73ad34 | -5.07326 | -43.72483 | 2025-07-02 00:24:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ecdf72f1-5ab5-3452-85f6-66c78a735c83 | -7.22452 | -43.1012 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a5bac368-7261-3248-89e2-9efde1376f79 | -6.27466 | -43.68201 | 2025-07-02 00:24:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f77f1f2b-abfd-3187-b510-229b20e2650b | -5.65674 | -46.60184 | 2025-07-02 00:24:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 459ef0e5-d934-3227-b90b-df20b5a58377 | -8.86034 | -47.27884 | 2025-07-02 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 64493109-2922-395d-9d9b-8dfeb0d3ba98 | -7.7786 | -44.01597 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 24427f4e-e876-34a4-8c86-898df8454a0a | -7.80648 | -44.02109 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 52d1ba9b-7e73-34a5-94d8-8cb43119f82e | -5.87829 | -44.7947 | 2025-07-02 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README2.md)
