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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fc35e50-4ece-3a65-b44d-a2aa3835d082 | -12.7557 | -44.4959 | 2026-07-03 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 4a81239c-6a33-3c89-90bb-6e3a344a4de7 | -10.9588 | -43.0565 | 2026-07-03 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e56ad00b-63d6-33bd-a594-af17a34f7894 | -10.9397 | -43.0593 | 2026-07-03 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 363.5 |
| b1070fa6-f353-3718-8cfd-7d0fe5ea1211 | -12.7359 | -44.5225 | 2026-07-03 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b2adcd68-4769-313b-b685-42b8e156862a | -12.7746 | -44.5162 | 2026-07-03 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 78d40446-3db7-3449-b45d-5c46578ae542 | -10.9593 | -43.0326 | 2026-07-03 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| c2c69cb6-918e-3af6-befb-589a5f096a6a | -12.7553 | -44.5194 | 2026-07-03 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 435.0 |
| 74074cd9-be55-35d4-a3e0-a6e6e6ae462f | -10.9401 | -43.0355 | 2026-07-03 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 341.6 |
| af9ea1d2-6cdc-3d00-89b8-ef48d4f07134 | -12.7746 | -44.5162 | 2026-07-03 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b7570cf7-3dae-3edf-9b77-41e1d2bcd78f | -10.9588 | -43.0565 | 2026-07-03 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 938034b6-fd20-35dc-bcc1-18b4f2e30347 | -11.4345 | -46.5291 | 2026-07-03 04:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| c6c77a03-aacb-3da2-bee2-c3a22f36ed46 | -5.7945 | -45.0586 | 2026-07-03 04:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 57d9519a-7025-386a-821f-9fb984b7d491 | -10.9401 | -43.0355 | 2026-07-03 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 312.3 |
| 23ca31b6-e498-373b-b54d-eda6bf2d5b35 | -12.7359 | -44.5225 | 2026-07-03 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8697803a-c81a-3755-a12d-dd4edfd002f0 | -10.9397 | -43.0593 | 2026-07-03 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 356.1 |
| aaf5cff3-16b5-3895-9b43-3095a6e4891b | -10.9593 | -43.0326 | 2026-07-03 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 026ccb92-f668-3eb0-9036-3e40ef73f669 | -12.7548 | -44.5428 | 2026-07-03 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 313da1f7-7903-3e68-8285-140c9ef21051 | -12.7557 | -44.4959 | 2026-07-03 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6212be0d-9a2f-3ce8-8216-5c793dfb1618 | -12.7553 | -44.5194 | 2026-07-03 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 377.4 |
| 0cd36433-cf1e-3dde-a614-317c2e635b22 | -12.7359 | -44.5225 | 2026-07-03 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| aab88faa-cb45-35ff-83ca-2fc9b3ee976c | -10.9588 | -43.0565 | 2026-07-03 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| d84468e6-2320-303e-8dfe-d0a71a31c228 | -12.7553 | -44.5194 | 2026-07-03 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 350.6 |
| 65cdceef-6c9a-3845-8025-c8b7877f305d | -5.7945 | -45.0586 | 2026-07-03 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4dc9e8ff-0544-3bcf-902b-1a74c3c0c9f4 | -10.9397 | -43.0593 | 2026-07-03 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 349.4 |
| b73f30dc-2982-37ff-9208-a170ce9914c3 | -10.9593 | -43.0326 | 2026-07-03 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 87914112-52ec-36d1-94f2-6d3710f4196e | -12.7746 | -44.5162 | 2026-07-03 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| ae2b6fdb-3432-34da-b31d-044767d3ef5f | -10.9401 | -43.0355 | 2026-07-03 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.8 |
| efa33ab9-655f-3afd-9b9b-0f8f1df84b28 | -12.7548 | -44.5428 | 2026-07-03 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4d60797e-2854-3880-8aa7-570a78c68d39 | -12.7557 | -44.4959 | 2026-07-03 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 84c9096b-8d4e-3d82-a39e-26a6a29b5334 | -5.7945 | -45.0586 | 2026-07-03 05:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 4edaa0ff-2393-3799-92ac-cb5f4a2ae35c | -10.9588 | -43.0565 | 2026-07-03 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 1fa13517-346f-3863-9a6d-489633610082 | -12.7359 | -44.5225 | 2026-07-03 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 5846639d-7c45-36cb-a906-afb55ea1b0a3 | -10.9593 | -43.0326 | 2026-07-03 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 0a190538-3013-322e-a217-7c7090b41c47 | -10.9401 | -43.0355 | 2026-07-03 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 8b2f5ddf-aa22-39fc-bcab-fbb23431345e | -12.7557 | -44.4959 | 2026-07-03 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 2667be12-a81a-345b-b2e1-2c824c11c3db | -12.7548 | -44.5428 | 2026-07-03 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fd07f0a6-5526-3d71-b503-1b58e788b616 | -10.9397 | -43.0593 | 2026-07-03 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 413141fb-b4e5-37d8-a886-ddfab2a6fe2f | -12.7553 | -44.5194 | 2026-07-03 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 4baf2f3b-898f-3687-8801-23b057eb017e | -5.79694 | -45.06565 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cb3f0453-63d2-35e5-b84b-9a01607fad44 | -6.93389 | -43.72852 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0ba1fb4-96e7-316e-b638-fd50ed803fbc | -9.04252 | -47.7385 | 2026-07-03 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b18c585-f36c-330f-a164-c13119027e4f | -3.42156 | -41.71028 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d36f0768-c7f7-3819-a550-a477c55c9a59 | -7.27357 | -44.50343 | 2026-07-03 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a382a24b-000e-3ae3-9124-e8224e95bc06 | -5.80982 | -43.80214 | 2026-07-03 05:04:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8dc23583-28f8-325f-8c80-fe4377ef8a49 | -3.04655 | -47.81948 | 2026-07-03 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bae2f50e-0bc9-3c82-b339-aa53ba7691b3 | -3.978 | -47.20762 | 2026-07-03 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c78c2bd-9699-3478-af09-36fc8ef0a4dd | -6.91016 | -43.71912 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0561c2f-b613-350d-9778-e97b889ef5a7 | -8.39078 | -48.21882 | 2026-07-03 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e64d5cc-f6ab-3f96-adf7-2fc91687bd2a | -9.46572 | -47.41708 | 2026-07-03 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c95c427c-c7c2-3afc-8748-e463a6d58ff0 | -6.92244 | -43.71611 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f668836f-35a5-37e9-bde5-ddc541041816 | -9.47099 | -47.41771 | 2026-07-03 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7221030e-18b6-3828-ab65-88de3a10a4c1 | -5.52847 | -43.94603 | 2026-07-03 05:04:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f0550df-fe53-3ce5-b0b4-aaac3085554c | -5.94135 | -43.47012 | 2026-07-03 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d8e3a0fe-833d-329f-b19b-9c1281655bfc | -5.79178 | -45.06279 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e9b0c3d2-91c4-37fe-ae78-82d7c5b9f847 | -5.79477 | -45.04159 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a61e092d-d5d4-3f33-bcaa-36d712b76201 | -5.80091 | -45.03599 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acd6247d-8d4a-3b9e-b6f5-c51db03f6b70 | -7.01665 | -45.42899 | 2026-07-03 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 246f807e-ade4-31f0-9fb8-915a595a879a | -4.34651 | -47.76569 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d52afe6-404c-3801-8381-84831fe2a0b1 | -7.27423 | -44.49859 | 2026-07-03 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba399c07-e6ba-3d1c-9c94-9eb7dac54836 | -6.42791 | -55.79467 | 2026-07-03 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706ac30c-599f-3d1d-a7a1-44b1645c77d5 | -5.80178 | -45.0341 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc685f2e-053f-31e3-bdf1-b407e5f87e7d | -5.91366 | -43.62869 | 2026-07-03 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6e21ea6-3101-3fb9-a533-f45d85e4c8e3 | -7.92342 | -48.25198 | 2026-07-03 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78de97bb-bc39-3f1a-bf9a-f443d2d4ba93 | -8.73285 | -48.33168 | 2026-07-03 05:04:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7d65a789-d29f-3651-b52f-447773a71869 | -5.79359 | -45.04994 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9262f59e-c86c-391a-a89d-71a85343735c | -4.01435 | -48.06024 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d651f264-6a15-38f3-9a51-3b8becbb6a1d | -5.80648 | -45.04297 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 135bc024-04b2-34f7-bdf9-762cfafca47f | -5.79638 | -45.06989 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7cb933db-4035-374a-a13a-afd0b3798d07 | -9.20173 | -45.32163 | 2026-07-03 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6836f61-0b11-3cde-a17c-22ed8a1c3462 | -1.78683 | -55.52668 | 2026-07-03 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e5a1528-1b30-3910-a83c-96843977518c | -7.27339 | -44.50297 | 2026-07-03 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 658b013a-41df-34dc-89af-c829ee28cba0 | -7.92241 | -47.82119 | 2026-07-03 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32fcebf1-6c06-32d7-891e-9b9f447c4b44 | -9.19572 | -45.32086 | 2026-07-03 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0ce1e8-33d4-3665-8f73-6852d2948f9d | -6.9296 | -43.71159 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 22ddb2f5-a38c-36b9-a05c-0be5b2ba329c | -5.7934 | -45.04766 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 039ea487-fb55-31a9-8e0e-72cdf2f6e001 | -6.2009 | -42.51713 | 2026-07-03 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9bf2ef23-a2ee-32fd-b751-3f0fd72a03cd | -4.34592 | -47.76353 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e13f7dc-6cac-38ff-9271-7b86157e7249 | -6.92816 | -43.72233 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c0fb857-a04f-3c8c-8dea-5f4a76c99866 | -5.80062 | -45.04229 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bf0c4e3-53ad-3e7f-a3d9-d658b2562eb0 | -3.872 | -42.97347 | 2026-07-03 05:04:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e39c5498-6c62-3f32-ae0a-ad939026f5f6 | -4.88583 | -48.90261 | 2026-07-03 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b36d280b-2236-3460-82fa-034445da091d | -6.9288 | -43.72724 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 334ac6b5-d49d-3362-ad0b-df33b8868dfb | -5.8012 | -45.03822 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60a35a4b-c8b7-34a4-9ac2-3092df51e12b | -5.81207 | -45.0415 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cf5a43f3-3a39-3782-957a-e6ca1ab039ac | -3.41559 | -41.70036 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| eb6e8458-848b-31b9-817f-92424c4411fe | -4.87825 | -48.89254 | 2026-07-03 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71ca8117-bcd5-344c-bba0-cec83f645914 | -6.92371 | -43.71567 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 96b4effb-1547-36c9-a3e5-6f239d97e9fe | -4.00514 | -48.05845 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2154b9e-308c-3905-8155-c3a73920d2fb | -4.35067 | -47.7643 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c8f8173-56d1-36a9-9790-63dd21b9b2c5 | -3.42061 | -41.71667 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a40bddb7-6f3c-39a2-8b16-5d89ebc04627 | -6.91659 | -43.72009 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 09aad687-32b9-3231-a934-a4cf187c8591 | -7.01609 | -45.43307 | 2026-07-03 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bd85a5d-c238-3724-8f16-462619a8ebfb | -3.51627 | -48.0337 | 2026-07-03 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 870abf76-b0d6-3c5d-9fdd-ba333d766aca | -5.79226 | -45.05622 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5e2f9f1d-2a84-32cb-b7af-49e0e0130521 | -5.79169 | -45.06052 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0b6bf77f-5877-304b-acba-777d5507b86c | -5.91434 | -43.62358 | 2026-07-03 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df72e667-b0f4-307f-a5f3-8b2201d4e0b2 | -5.80621 | -45.04081 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7c7448ea-673b-3fc1-a567-6fb6a2b29647 | -6.90885 | -43.71958 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d3a96c9-6409-30f6-959e-9841d428487b | -5.79283 | -45.05193 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ec3fd9c0-a8d6-3ab2-88fd-222b9a651ad5 | -5.79761 | -45.06363 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README15.md)
