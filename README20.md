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
| 15d307b5-061e-385d-aa08-cee90b50610f | -4.5509 | -42.95012 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 10818dd6-e916-35a5-baa0-d3b640908939 | -5.46136 | -44.9592 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0875742-e7ee-3dcc-ad59-df1db9e29a48 | -6.20231 | -42.1532 | 2026-09-17 03:53:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 31415128-b1e0-3406-9156-f40fc9dcd0a4 | -3.17615 | -48.58398 | 2026-09-17 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 642f5666-d40b-35ff-916a-9bce8a00c655 | -7.43688 | -35.24757 | 2026-09-17 03:53:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b9d3e7fb-fbdb-334a-bf64-987426fd3c87 | -6.01239 | -46.64593 | 2026-09-17 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b35783c6-025a-3d9f-9714-33454e3e34b4 | -6.94149 | -41.70265 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9baed196-5481-31f1-98f6-2df6f29839e4 | -6.51391 | -44.0582 | 2026-09-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae5657b0-7844-35ab-bbaf-6e63b4840b9a | -5.98753 | -46.63039 | 2026-09-17 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a9ea96d-6ac7-3ca9-8b80-0b1b75b26763 | -2.62394 | -49.11729 | 2026-09-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d23b001-08a0-3e52-b005-8f516c165cc4 | -6.31818 | -40.15055 | 2026-09-17 03:53:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bf6c3c7-2731-3099-bdb4-3a81b41e9948 | -4.54721 | -42.94503 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d7d9c6df-100a-323b-805a-690da997693d | -5.64094 | -44.81251 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6efef39-bb95-3815-9361-5bcb964d0732 | -6.35891 | -43.36363 | 2026-09-17 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89ca9ce0-f221-3c03-a907-5492662b479b | -5.36334 | -36.84549 | 2026-09-17 03:53:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8e059f5-ba76-3f1e-abe6-129f871d95fb | -5.7739 | -45.11335 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 513be29a-ebb4-3fcd-83fb-e58d97af2d48 | -7.36561 | -38.97836 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 382e01b1-a56d-3fae-bb3f-04eadfbe728c | -5.98135 | -46.63301 | 2026-09-17 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c2055fd-902c-334f-a273-818bf061a13a | -7.36901 | -38.9789 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 39224f49-b6c4-33f8-98d5-c92b9825af13 | -6.92894 | -41.70538 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 425b6184-cd74-3b3b-8b88-577d39239da7 | -6.76082 | -42.77657 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bee9d1a7-140b-37af-aa62-36b2a657c26c | -7.37242 | -38.97944 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8a383d31-77aa-31b6-a554-69081859ed42 | -3.40981 | -39.28105 | 2026-09-17 03:53:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 95b637f4-add3-3771-bf7a-7bc8807b8bde | -5.76488 | -45.10583 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9f972abd-7781-3d4d-aa2e-bf1c94033573 | -5.63792 | -44.80061 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 497b7b09-d980-30f3-b01f-2083f6208658 | -6.94232 | -41.69767 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8fff0f38-d162-333a-9b0e-07292533f579 | -5.77443 | -45.11035 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 8e84f9d3-ae52-323c-b59e-c653ef11fc70 | -5.76331 | -45.11474 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ff91c4a9-ed09-38e7-ab0c-01f7c10e7d1d | -6.94537 | -41.70351 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 084ed4d0-dec4-376c-9c58-345a4fae2405 | -6.16525 | -44.62561 | 2026-09-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b24837d-44b9-35ae-84de-3935a7ead1e0 | -5.46183 | -44.95638 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7525f951-8235-3c96-a39f-3fe7c1396fd9 | -4.56044 | -42.9474 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6186c4c0-9653-3921-8805-690cccb57862 | -5.58092 | -42.7283 | 2026-09-17 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4af9e51c-8075-359f-a153-f34ee9dcf95d | -5.61582 | -45.24864 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fe26212f-9abc-3901-b22e-cee233ea0856 | -3.40915 | -39.28514 | 2026-09-17 03:53:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 766c86a9-eb19-3447-b195-d2b5bb96b52c | -5.97517 | -46.63567 | 2026-09-17 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc41af58-334b-3f8c-9a8b-45b4e06caa9b | -5.636 | -44.81173 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e143847-9b73-3505-83d7-5b49e8042771 | -5.6185 | -45.24506 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c87432a-d7eb-3e69-be31-78b009aa7e58 | -6.9376 | -41.70181 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d883c8bc-028e-3816-8e38-bfaa50d4f6f6 | -6.93285 | -41.70611 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1016483f-0aa8-37b0-bc37-38fe8557f42e | -6.76571 | -42.77327 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1de6b332-db7a-30de-8194-ec999f744bad | -7.37182 | -38.98314 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5df7e2f9-e44b-3382-b498-e0cc30a91a8f | -5.73244 | -43.27963 | 2026-09-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5a5562c-8900-32b9-817f-75b01e0333f0 | -6.04377 | -44.03411 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5b0a6351-4829-30bc-b7c5-7f6a7107c3af | -6.76638 | -42.76935 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7205db2d-5ad6-3471-9d3e-e504d706b77f | -6.00051 | -44.26272 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a164268-35ac-3625-aa5d-fb14e17db691 | -6.03442 | -44.03288 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e4edba71-f1a4-3846-bfe1-8125901e8046 | -5.63696 | -44.80614 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 69cd7cd0-7284-382b-9f8f-b22bd2e6c686 | -6.51475 | -44.05341 | 2026-09-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 934d7f1b-130d-347a-a45a-921c82decc16 | -5.45685 | -44.95541 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eda1f814-420e-30bb-9027-554d00c87d7d | -6.4129 | -43.46853 | 2026-09-17 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d3d0409-85df-3123-82ff-6da55446f9b9 | -5.76541 | -45.10285 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e38c0aed-0a6c-3926-9cde-715e075fd1dc | -4.36419 | -47.78492 | 2026-09-17 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ced74393-f01f-3098-a454-c84684fc24e5 | -6.03701 | -44.03507 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 74421b5f-a023-3529-aadf-b5129f432475 | -6.03362 | -44.03766 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d0ef7aac-4b64-32f4-8613-1e39459de495 | -6.13026 | -43.74467 | 2026-09-17 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d58345f4-ac5a-3ae6-9386-eaaab567c350 | -5.77097 | -45.10061 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| b0c62251-612d-3bd2-934e-8d1aca3cdca1 | -6.16491 | -44.62005 | 2026-09-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3cd4344-96d2-32db-895c-5e783dc49ad0 | -6.76994 | -42.77393 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8ada63a-ee62-3a67-9164-e3aeb5747e29 | -5.76887 | -45.11258 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 73df927b-9a91-377f-bcf1-635cfdc2856c | -6.99506 | -40.33913 | 2026-09-17 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dff27fdb-f56f-38d6-8887-44340963854f | -6.82405 | -41.10372 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52272119-7832-3cab-a85a-c63213f4c65c | -1.7832 | -47.83382 | 2026-09-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 746c5aa9-c00d-3919-a4f4-9af8f1bb5bb3 | -4.5797 | -47.16762 | 2026-09-17 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d3c15aa-3f0e-3df9-b741-693abbd746d3 | -5.46057 | -44.96288 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb89e4a6-4c6e-33d4-ade6-6c646653df90 | -5.46606 | -44.96091 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1a3a35c-3134-31d9-8f3b-30d60789bea6 | -5.7715 | -45.09763 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0940863-2e1c-3855-9b48-6b84c5023092 | -5.64191 | -44.80692 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 58d9102e-3dc3-3560-bbe3-fc174397e18e | -6.77059 | -42.77002 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88b89eb1-46b6-3431-8060-38b1c8bfdc94 | -6.93676 | -41.70684 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fef1d8f5-0166-31d3-9900-8537148b48b9 | -5.32459 | -42.70137 | 2026-09-17 03:53:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f13a9d5-062c-3bfa-b1ce-d5d89fe53364 | -5.64286 | -44.80139 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 2c12a790-b6e7-30d3-b5ae-ad84fdbfce9d | -4.55162 | -42.9458 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7a102ab5-7b3a-39f5-a440-43da9eb5a378 | -6.16504 | -43.35778 | 2026-09-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e8ffcba-d6c8-3667-8dc9-72ff412be604 | -5.77601 | -45.10136 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 3e901c8d-ee91-3b1b-aadc-79cdbd58a31b | -7.37583 | -38.97997 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4dc9b4fd-1711-3f54-9f5c-bd7ab3a01362 | -5.49205 | -43.67741 | 2026-09-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b0b2440-b1df-3207-8914-7ed488344731 | -5.76834 | -45.11556 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ce726824-8449-36ed-9673-1602b4f46a1e | -5.9758 | -46.6321 | 2026-09-17 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4427d05-225a-3a0d-aa21-aee196731474 | -6.16945 | -43.35862 | 2026-09-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09753ec7-770b-35f1-a12f-a9423daf1b7e | -12.48736 | -50.82397 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d71e0e34-4d8f-34af-b8d1-b27622af1405 | -12.4794 | -50.86222 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 311bafef-6a64-3b0f-a05b-0af5b50034e6 | -7.12409 | -42.16145 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20702e68-5d53-355a-9805-b263a04d0726 | -7.03849 | -42.07513 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f9c79066-2b9e-3908-b4dd-9676fae76c49 | -7.44966 | -46.16514 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f18338d0-0e8f-3b3c-806c-bb50e0a05a99 | -8.5586 | -44.5118 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ae01908-f306-3dde-ab26-75c6f9f3dc07 | -8.25368 | -42.17347 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c0168062-cf1f-374a-95b8-27eaaf743d29 | -9.61484 | -45.34154 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5809053c-408d-3a86-bccb-9d7f489746fb | -12.47853 | -50.93121 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9acc7fd-6a63-3b9f-954e-95df58c86e69 | -8.5279 | -44.529 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b23d5ee-8387-323b-8144-d61cac8be3b7 | -8.94746 | -44.39512 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53fe927d-3837-3dba-a985-6065211edd6c | -8.61142 | -44.48132 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1069e2ea-2200-34dd-85b7-b2c3f09d453f | -9.11367 | -45.72955 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| c807caf2-b1c1-3cb3-8d53-1b944bece68c | -7.7249 | -42.50422 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 129b9b05-70a6-37fb-867c-043c4ed7ddad | -14.55281 | -39.63542 | 2026-09-17 03:55:00 | NOAA-20 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c3b64e57-e9f9-3a6d-9b15-04ca35095bd6 | -12.45647 | -50.81141 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| db9883f8-06c9-38f0-9e59-d99186ceaca1 | -6.67893 | -43.65196 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 497aaaa0-bab3-351c-a242-359880fbb7a2 | -11.8875 | -47.58384 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c935726c-b666-31fc-a655-eb088edc8f71 | -9.11465 | -45.72401 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 5b1da422-4c46-314b-8a54-d90fa5bb6489 | -9.7859 | -46.48197 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
