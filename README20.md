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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1b0c7a4-2586-34ba-afbb-80c43e286a7c | -4.87014 | -48.52252 | 2024-12-12 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc66e793-3a1a-31b1-865e-323376df8cbd | -6.10218 | -44.04653 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e306526a-acf4-301a-9048-4240e2bc6c17 | -2.56529 | -51.88309 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e0a5cd-b9dd-32c1-a23f-f5b2b79d442f | -4.03145 | -46.88624 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ca6a5e0-10eb-37f8-93fe-fa328413a320 | -2.96751 | -53.72792 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75dd5435-ed61-396d-b2b7-f1777b7bd11c | -2.78801 | -52.86164 | 2024-12-12 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a39e956d-7732-3f86-8cc8-24a2eae07e70 | -3.82169 | -44.12191 | 2024-12-12 04:38:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0463340-b66a-3c08-a470-216e96321b7e | -3.99938 | -46.55495 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93dd14d7-0314-34a6-8429-5a956d5e62c1 | -7.43164 | -44.74385 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b198c0db-416a-3729-8ce4-cfc3fb3c6f61 | -4.13802 | -47.73194 | 2024-12-12 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b834423-b43a-3214-95f3-161dac500464 | -2.0827 | -52.27893 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4b9b04b-65cb-36b9-bede-fed5b73288ea | -2.43799 | -51.79097 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fa99816-9ce4-3ef2-ba2f-09afcc387afb | -2.56894 | -51.88368 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e13caeb-097d-3297-849c-023589b2a9f3 | -3.60008 | -53.72288 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f317eea5-6ea5-3bca-9da9-b9bbe977918e | -2.9282 | -46.69559 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9774942-92f7-3abf-959f-8fbe395c263e | -6.93243 | -43.50515 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae9b84a0-4a82-3a52-9bba-145dc43bbb89 | -4.05471 | -46.66466 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08de0c74-1ea8-3760-aa96-4f7b0483c423 | -3.20889 | -53.00695 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f61c2d7-de3d-3606-bdc3-59554c00f930 | -4.86319 | -40.75523 | 2024-12-12 04:38:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a27fbf7-c53a-3506-b0e7-b54bf37f84ee | -3.8177 | -44.12131 | 2024-12-12 04:38:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9efb7d23-9dc2-385d-baa2-8035c01efc86 | -5.70888 | -46.51411 | 2024-12-12 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b64f7786-c9e2-3c72-861b-adf948443422 | -6.97156 | -42.99715 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 40925d35-08c1-359a-945c-bf5b9b6ef4af | -4.80265 | -50.82097 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa5e17cf-a9f9-3ae9-aca0-2e5a1bfaab82 | -2.08282 | -52.27667 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29403397-d961-3192-9fdb-b88adb4cc31b | -5.92856 | -48.04583 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3950b13-e7c4-3b89-884f-6912f6fa1c9c | -5.1413 | -46.17712 | 2024-12-12 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a833c96-bf4f-30dc-9ea9-b21860e19e14 | -1.81512 | -52.69094 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ca5c89f-9a7d-38d4-aa2e-b27d8e438598 | -7.4737 | -44.74311 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecd7e00e-8abf-356a-9525-513593378295 | -4.93649 | -44.28177 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2749d20a-1b83-386c-aff9-fa7fbc522914 | -5.93138 | -48.04997 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ad406be-6971-34b0-877d-1b8aa6fcc977 | -7.88575 | -42.44462 | 2024-12-12 04:38:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5b38a496-5e61-3708-bb1c-3a60f15020ae | -4.08608 | -46.66935 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b82a3c4-0be6-348a-aad2-8a2bb2df13a0 | -4.5528 | -50.6138 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 12ede526-357e-389a-ae06-328af26958f1 | -4.08087 | -46.65685 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eeca4553-4ef5-3210-b8fe-9be5ae15b619 | -4.05339 | -46.83563 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b25830f-c3a4-30fa-8ff5-0960b52fbd79 | -4.13348 | -54.33866 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf3d6899-54b2-3118-b8d2-ea70dbf70742 | -2.27186 | -53.48422 | 2024-12-12 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a1d5302-439e-3fd4-8d23-59024639284d | -4.6471 | -49.01997 | 2024-12-12 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c156ad1-795f-3813-82ca-1d4b6c56b9e8 | -6.96403 | -42.99327 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 77c406a5-6ccc-3b83-8032-62cad93b18df | -3.98777 | -48.39579 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b814024-f8bd-355e-a58e-90e7ffe6364c | -2.91447 | -48.03257 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c960f59-4aeb-3e1b-a70b-a331711a5079 | -5.10301 | -37.6021 | 2024-12-12 04:38:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d2f62d15-a793-3155-a76c-ec0b1c433f3a | -4.4965 | -46.10777 | 2024-12-12 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cea74668-c87a-365b-b6d6-9bcaf9f5aaa6 | -7.86343 | -43.08774 | 2024-12-12 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23acfb2b-d1f2-3e36-a010-2b02242aaf85 | -4.36471 | -49.11404 | 2024-12-12 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4ee5d66-1fa3-302c-8c31-6fe30a1c3b9b | -4.02858 | -46.88197 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65c11c4f-0778-3b54-af83-1121dfabca85 | -4.06987 | -54.30259 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14d6b5cd-7c21-39c9-8bfc-6dd91747cc00 | -4.1336 | -46.70777 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca5f2d7f-2481-3289-b76e-13e5466f3f0a | -2.92672 | -48.0416 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f85540e-8871-3ad5-8cf3-f97f6e28a7d9 | -4.35622 | -49.74565 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 508bf14d-b2e6-3380-8d6d-226e72929e9f | -3.41601 | -44.4542 | 2024-12-12 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27f2fa75-09e5-3d2e-b8d6-2364d7426914 | -4.05529 | -46.66085 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a96eeba6-1584-3eb2-9cb4-3832f8142432 | -4.9405 | -44.28236 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2f73930-a76e-3a30-b553-f0d95831a298 | -3.65345 | -45.7021 | 2024-12-12 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1100370f-d6b5-342b-87ec-35dd41e1f6cd | -4.09882 | -46.67921 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b5dbc76-c1e6-3a92-a9e1-ffa898f8ae46 | -3.82949 | -41.56777 | 2024-12-12 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f563f16e-8441-3440-9813-abb513dfd4bc | -5.30364 | -43.28041 | 2024-12-12 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9d86c9e-7eae-3473-aba1-6ea69e0bb939 | -2.83538 | -53.01168 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97b46961-d1f5-35c8-b387-6337678323ed | -2.07895 | -52.27832 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d267dd7f-3ec5-3f60-8180-3ebc84eeb3a8 | -7.31849 | -49.97141 | 2024-12-12 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 383a389e-3873-3edd-94c6-f8479e4e6d6e | -5.14426 | -46.18184 | 2024-12-12 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f130dd05-67a3-3cae-bcca-5a5f6f34ccc1 | -4.00357 | -46.89428 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35ec509f-184e-3c68-a60d-db480a83f6b7 | -4.11242 | -46.79794 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48180f26-8de4-3a18-8e5f-37d03d65b35d | -6.12466 | -42.53715 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f3baf088-b604-3ad3-a828-30c5db9e7c60 | -5.30563 | -45.26991 | 2024-12-12 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6103898a-d976-3776-af18-7fc8cf058ad3 | -7.43113 | -44.74733 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec8aa85e-5b9a-3877-9a95-2259bf83a79c | -4.31771 | -49.39028 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22a9c461-655d-3669-894f-3fe3de4fb9e8 | -5.59676 | -41.38219 | 2024-12-12 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| feee4bba-3e48-318c-9d0c-1230808fbd73 | -5.28716 | -44.91394 | 2024-12-12 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b38e4a1-003d-3f61-8c2e-4df724cfd924 | -4.37367 | -48.75425 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8362abf-e7fd-31aa-b3c1-ef8d18d7e55b | -2.07836 | -52.28057 | 2024-12-12 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e45485a2-cbc1-3141-be35-0c07befc6fba | -4.19659 | -50.54722 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7c15a7a-830a-3144-940b-7b23c917976e | -4.38588 | -42.14797 | 2024-12-12 04:38:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 25718b25-9e03-3425-bada-5fdbc6681c1a | -2.71287 | -47.55315 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe2f3daf-ea58-3980-bcd0-7d9a93ccf17c | -5.87518 | -35.41707 | 2024-12-12 04:38:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 11.0 |
| a0096f5e-88b7-30c4-9d97-d8024e8fd3b7 | -3.24522 | -46.87643 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1b42c1a5-cece-3a7b-9a7a-1f01474e373e | -3.49558 | -51.17709 | 2024-12-12 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8afc5fe3-fdda-33f2-8f9f-4c51bbc9f0c9 | -2.71232 | -47.55668 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dc738d9-4c5e-3eff-98fc-42035b9220b3 | -4.04668 | -46.66448 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b00f10-21c2-33da-9e47-c48b384c580d | -4.31032 | -46.89338 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c964c0aa-6e76-3daf-becb-5f7fac96e1c7 | -3.80034 | -50.40728 | 2024-12-12 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ee990dd-297a-32ad-9aad-d1d1165c2753 | -6.12535 | -42.53241 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 97521b13-191c-3a84-a4e2-03dbda8ff8b9 | -7.47421 | -44.73955 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8ec735b-e7e0-30b1-9a85-8a30385a9c54 | -4.18199 | -42.42398 | 2024-12-12 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d469ba00-9dfd-34c1-8829-65b16e50bec5 | -2.95881 | -48.61071 | 2024-12-12 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66c919f8-9862-332a-bb77-2afd99c4f9f4 | -5.98729 | -43.48007 | 2024-12-12 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6a7d6eb-5337-311f-bbf7-889070a26a17 | -4.07965 | -46.12743 | 2024-12-12 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56914ba1-d2c5-3a9f-9169-84ce52213a57 | -4.01654 | -47.02916 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb6889b2-e881-3b65-8ba1-5c4cecb7ba27 | -3.59664 | -53.74377 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a1c6a8b-7651-3454-a2b4-8da75e2849ee | -4.07669 | -46.12293 | 2024-12-12 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55f83ecb-275a-3995-8f00-660fbf358334 | -2.81532 | -53.03971 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64c8ad33-9cff-3dc9-8126-a006b65f982f | -4.0007 | -46.89 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7045b64-fa79-3f87-bcdb-560d779b1cea | -2.52473 | -51.78624 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77fbbaff-ba90-3914-9ddc-d8eb2a6ea683 | -4.41016 | -48.73867 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4429efb-f970-3fff-becc-febdddd3cd65 | -4.22586 | -50.0781 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1007a51-85ea-3b1d-acbc-1171d16c6ed7 | -6.9176 | -43.51574 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b923a72-c943-330d-a744-1a98f3cb7875 | -5.30303 | -43.28442 | 2024-12-12 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f657774-0de6-349c-8589-76c438de481e | -4.02398 | -47.02649 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a67bf480-1555-3614-85aa-d42d00eb5e3c | -5.92633 | -48.06025 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 770c690e-5ed7-386c-afd9-cd9c4756c74d | -2.58782 | -47.48643 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
