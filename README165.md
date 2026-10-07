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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d8ea447-bfef-33c9-8208-14cf737081a2 | -7.276 | -46.15646 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd22f71e-7777-372b-9529-abbf5ad98560 | -7.00528 | -44.05117 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 99d2d121-4053-35ec-8457-bd1031c2f756 | -7.28143 | -46.15873 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 31cdf1c9-72a4-37ad-9767-9b916bfaa268 | -3.88704 | -44.12396 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 134db472-78ab-353c-af04-6015fd09d502 | -7.04724 | -44.31821 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 87ccbc21-dbb8-3fd0-9196-acbaa9dc3c36 | -3.20799 | -42.95869 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| be065f2c-7e35-3110-812b-e91df0129b6c | -7.37985 | -46.20698 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f3440852-9362-3f84-b4bd-7115b3571138 | -3.49218 | -39.50098 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7efc291d-d9ab-3294-a866-29103da69ddc | -7.81146 | -44.58826 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4f9c8d37-02f6-3ffb-9148-81ed3660c221 | -3.89424 | -44.11517 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a5e8263e-995f-3766-ab7a-9de09a07dc09 | -6.03173 | -43.02761 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf43cd06-1534-3f0b-86dc-f7dba8e013d6 | -4.42046 | -43.73232 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 08ebe072-ebe6-363e-8b38-7d2f93eb0625 | -3.51282 | -41.94855 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f2a2c2d3-a7ff-3e93-9970-e5e6439c0d3f | -6.68158 | -44.95266 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1070935a-529a-36e4-95c8-c7675c2a082d | -7.38451 | -46.2033 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c4b74a5c-1b18-34e5-ae51-de7c9eeb14e9 | -4.17732 | -42.0435 | 2026-10-07 16:03:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cf851e5b-d195-36cd-8e62-e7515972acf8 | -8.11055 | -50.92637 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c8967d17-dfa5-394a-970a-be977302b7c9 | -4.95004 | -42.73051 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 845a1484-f014-3f08-931f-170032529772 | -3.75025 | -51.2248 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a1b419e-0793-3dd5-80de-71b9793e0cde | -6.93462 | -38.29153 | 2026-10-07 16:03:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 48.2 |
| a5efbdb0-ab24-3802-ae87-560ccb14feca | -3.9476 | -40.73756 | 2026-10-07 16:03:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| ce879c7d-3375-34b2-8745-641420328a95 | -7.56844 | -46.70004 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f711003a-5d34-3782-b067-486b0070e0e8 | -6.22609 | -44.84221 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f7e00cf0-ca16-36e9-89f2-871a06630b71 | -3.87705 | -44.11379 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| ef9c8b04-be9d-36a5-95c3-ef0f24a3b204 | -3.86678 | -44.13065 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12c44be0-8733-3e73-a06b-3d89b9f8c71e | -6.06162 | -35.52747 | 2026-10-07 16:03:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 9894fd4d-208f-3c58-828a-ea67709b39f8 | -3.7494 | -41.70701 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 14dd74e3-189b-3f46-9f00-b971a6527857 | -8.29019 | -51.23916 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 741ad8a5-6228-3d8f-ab50-9a8df2b23ec2 | -3.32757 | -44.58282 | 2026-10-07 16:03:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a4fd69f2-c650-3647-8e23-28f85fe1c0ff | -3.76258 | -40.83481 | 2026-10-07 16:03:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 2407f0fe-177c-3048-99c1-2eabcfcf50a1 | -7.24756 | -45.26018 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c4420530-f82d-36b1-9197-ffd459cb4276 | -4.63133 | -48.86471 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| ba6bef2c-fd1a-3c9a-95e8-0dda4ba43418 | -3.58933 | -39.44641 | 2026-10-07 16:03:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9a79d938-daa1-3f7a-b159-2987c383b512 | -6.00969 | -42.27261 | 2026-10-07 16:03:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 7dc6c524-f4db-3991-a1ac-ccb792e5d5c1 | -6.04937 | -44.19099 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c7e7c6b-2f90-3509-ac2e-d8990ce70847 | -5.96048 | -46.36691 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 34bb745b-11fb-3fa5-8890-437f1c9adce1 | -3.87455 | -44.12571 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d81ca539-8e92-3ed1-93b0-3c97916eaf0e | -6.8184 | -38.53362 | 2026-10-07 16:03:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 152.5 |
| fc88be69-0588-3837-899d-c3fb2acb046d | -3.75361 | -41.7106 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 77b84bb7-de8f-32d5-a2ae-a276e5213b76 | -6.03521 | -43.0235 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 470edca8-f85d-3f7a-a2a9-93ae81552a84 | -2.94466 | -41.40984 | 2026-10-07 16:03:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 380f7a7a-1bfb-377c-8e5f-90da4566ed7b | -3.80738 | -40.45884 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6ed414b7-b9d6-3f8e-99f3-19e10515bdac | -5.7278 | -45.1644 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 858f32e8-c7a1-3bf8-9985-12c78ada6c23 | -5.96713 | -43.52609 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d62fe43-3196-3cd5-b563-b18d04b37bf4 | -2.05749 | -45.97985 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 536c6a25-afb7-3b83-a716-e46ed2ea2425 | -4.97788 | -50.57181 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5289b72e-e4a8-362a-be09-17263af1240a | -6.98443 | -43.2868 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 19b2288c-4f84-311d-a0ac-1d2d8d12bb17 | -8.18965 | -46.33963 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3603c8d1-1ceb-3f1e-a8f4-796a90b054e9 | -2.99737 | -41.42607 | 2026-10-07 16:03:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 62bc33a5-6df9-300e-b3bd-b63b6a1dd2bb | -6.67226 | -41.772 | 2026-10-07 16:03:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 69d3ec50-36df-3d3f-8707-6d2db9996e61 | -4.52318 | -44.03664 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 647c334a-1f93-376d-819b-4a79e4ca5e7a | -7.1781 | -43.71424 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 91e92810-29d1-39df-b3ee-129cb1c66f19 | -7.24119 | -43.76587 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a9907517-797e-34ad-a3bc-7b9a3d3e2028 | -4.39954 | -41.57675 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| df5095cc-dd0d-368b-b6c0-28530587d9f0 | -3.18854 | -50.5702 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d0d23a43-ffe8-3ed7-81a2-2806ea484262 | -4.47583 | -44.60578 | 2026-10-07 16:03:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b278b9f-6c0e-3817-ae27-4227a941a560 | -3.17834 | -50.54541 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0929aae0-b23b-374d-85a0-d701b77d569f | -6.62637 | -35.65993 | 2026-10-07 16:03:00 | NOAA-21 | DONA INÊS | PARAÍBA | Brasil | 2505709 | 25 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6ec9dd39-f44a-3538-9f6f-fd779b526f70 | -6.29222 | -43.65114 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| af8096bd-a6b2-3791-961c-f2bf860eaff8 | -5.04966 | -44.74868 | 2026-10-07 16:03:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| d51f228c-992a-3eb6-aa90-e5bdcabaa809 | -3.86427 | -44.14262 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9efcf70c-0567-3dd9-b823-8ac877e11f57 | -6.15518 | -51.73258 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7984c26d-19d8-3f41-9e65-346a92b890da | -3.12901 | -43.84303 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09687ec8-2ba5-3aa5-8f09-7a07c90836d4 | -3.27181 | -50.43415 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| faab896a-5a1d-3c92-82cc-385124d304e9 | -6.80681 | -43.62143 | 2026-10-07 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1139ddfc-5de7-3757-8d86-a7cdf41edfcc | -7.21471 | -44.32926 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1023cc5-cf3c-36c9-a26c-cabb0f809d90 | -6.9961 | -45.12026 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 86c7f8ad-1051-339e-8e8d-0c0c2f1834dc | -8.02951 | -47.95971 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 67fa8765-c340-3cd9-8514-a45b80ad772d | -2.05692 | -45.97658 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ce173149-cb95-3be0-bf7c-b9dfcbf70b71 | -7.11035 | -48.03798 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2ca9a5c1-c8d1-340f-b7a4-30c0d06160a9 | -5.86682 | -51.15965 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| cb3796a6-9aa7-329a-bd79-79164a5f0af4 | -4.0799 | -44.07973 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16458946-e737-360d-9d14-9d06e3fb0118 | -7.30549 | -43.97765 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8470a66f-6bb3-3bec-96e7-585dc8a17232 | -4.74587 | -43.31199 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73ea69bd-4223-316f-9291-e94915575e90 | -5.96485 | -40.93685 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| f51e6c84-6659-33c8-a798-d4128543e58e | -6.44055 | -44.80155 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93ff9417-50c8-359a-a117-4c40563e120c | -7.62544 | -45.94483 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5fb24f19-66d5-3d23-a5c7-e5e8a9615157 | -3.97168 | -42.86845 | 2026-10-07 16:03:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 350cd519-73e7-31d2-bfd9-02f93d5b728e | -6.68427 | -44.93826 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a05d4dba-aa65-31f0-8360-0ea0e5fbee02 | -3.25964 | -44.64864 | 2026-10-07 16:03:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d5159e9a-1156-379a-8914-56d91fe43f23 | -3.23099 | -40.02271 | 2026-10-07 16:03:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 0ddcacce-79ae-3f59-bc5a-9c97116c4099 | -5.9697 | -40.94441 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| e4fc1916-c52d-312d-a24e-2b57bb491f65 | -5.47429 | -41.21815 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 99627ca5-61ee-3307-8964-f54a96897e73 | -4.32226 | -41.22958 | 2026-10-07 16:03:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 62aa9785-0243-39f0-bf2f-e2abb30c5b63 | -5.72586 | -41.7137 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 85cb57c3-ec31-392b-9463-b2d7c8b4328a | -4.4922 | -43.85337 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c0362c8b-2819-3757-8cd8-d060c6f86ff5 | -3.81262 | -41.69892 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| ac6846ca-0213-3ee7-9451-b4c5362e818e | -7.47531 | -42.81815 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 3a822952-4118-3f77-85f0-4771ce7aaec4 | -8.38871 | -48.07407 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e8b37a3-81f4-38a2-8c90-029778b5577a | -2.99151 | -42.83214 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 44a280bc-9ec4-3597-ae86-b3a7d7142c2c | -6.98204 | -45.12181 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8db9392-9bd3-3817-809e-a9c5dc6312b1 | -1.48391 | -46.28761 | 2026-10-07 16:03:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 50e9b764-8596-3091-83bf-473c2408ae84 | -5.83925 | -42.42797 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7b11b50b-f457-35bf-b369-f46c4d0f0829 | -5.96738 | -40.92841 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 9930f8e6-bed7-3c35-b5c7-bef3bcc120d7 | -6.22414 | -35.38531 | 2026-10-07 16:03:00 | NOAA-21 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1aef527e-1145-31f0-95ac-62967a454df4 | -6.9838 | -43.22278 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 483b15a8-300a-363f-a0a0-c413fc84f6ad | -4.02724 | -42.84605 | 2026-10-07 16:03:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 30.6 |
| a62fcdd4-e763-3c6b-97d8-ff2b1f5fc738 | -7.21566 | -44.29955 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e3a778f-823b-3910-a0a8-9f1e5c00d78f | -6.33616 | -43.83916 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d21bb286-40eb-3c18-8efc-7b310d4eb7cc | -5.34463 | -45.68902 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README166.md)
