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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a114bc8b-a4d6-3234-a2ab-98d4f3d8f76e | -0.84818 | -47.56832 | 2026-01-12 04:18:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cb32385-d87e-36c6-a88f-54bfef24071d | -0.08589 | -51.27862 | 2026-01-12 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90d8324c-2f6d-3bf8-9796-9f79fd7567a9 | -1.33389 | -45.83372 | 2026-01-12 04:18:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63d0e543-a55e-3b2e-927c-03e51052bb54 | -3.94732 | -40.70193 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6c1f55ff-4e94-3f37-82ed-e17f09fbb819 | -3.91625 | -38.46418 | 2026-01-12 04:18:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c7ce7ca3-38a5-385f-b757-2f6374c578d5 | -2.92154 | -41.36214 | 2026-01-12 04:18:00 | NPP-375D | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5adf756e-858d-357c-98b9-c4cb11590c1f | -4.68634 | -41.2364 | 2026-01-12 04:18:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e605ba6d-8051-34d2-aa2e-b4fe51b06916 | -5.91797 | -38.90202 | 2026-01-12 04:18:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 98390a50-c142-3e9c-aaf4-6bb3c8085386 | -4.01079 | -38.28867 | 2026-01-12 04:18:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30f02fc7-e543-313f-a553-c7ec6e42b6fc | -4.70802 | -44.47949 | 2026-01-12 04:18:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d4a6197-4f18-3453-82b7-de0cb5839161 | -1.73413 | -45.93963 | 2026-01-12 04:18:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0b838b3-b204-3c79-97a2-85bffe9c0e8e | -3.82056 | -41.26316 | 2026-01-12 04:18:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e8a84db-c52f-3623-bb4d-b380c6f9832f | -2.72897 | -42.84056 | 2026-01-12 04:18:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d0c122-05d3-39cc-8669-79587167f4d4 | -3.94267 | -38.39502 | 2026-01-12 04:18:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 2260da16-accc-3b70-9b5d-9ddaaf267817 | -4.50777 | -43.69692 | 2026-01-12 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875f18a0-1f33-3e83-8f3d-e69925c17d09 | -3.94685 | -40.69763 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac260369-6f89-34c9-9444-3b628a5aaea9 | -5.1893 | -40.74018 | 2026-01-12 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c460010-9fee-374b-80b7-4742f5776c15 | -6.00841 | -39.52533 | 2026-01-12 04:18:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03579aa2-de1f-349e-a4de-4a08837b10ad | -4.68576 | -41.24007 | 2026-01-12 04:18:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e8f3ccf-fdbe-3a4f-b484-7cd00361e067 | -3.94972 | -40.7019 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bd23b199-f6a3-3570-a41a-95bcb4dd902f | -3.01346 | -39.99451 | 2026-01-12 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7177a49f-9a6f-3364-8e0c-17dc14a4fa10 | -5.49573 | -42.15834 | 2026-01-12 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 913b39c9-3ed0-3758-956a-d6bb1e8d013a | -3.59912 | -43.54588 | 2026-01-12 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22370819-0252-3b74-90af-09c730d24f3a | -5.49963 | -42.15533 | 2026-01-12 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a226556a-1e41-3a00-86f7-695516afc4c7 | -5.05791 | -41.6954 | 2026-01-12 04:18:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f98de233-58f9-3726-b9e7-2e8aca0b6f50 | -3.60055 | -41.86679 | 2026-01-12 04:18:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bb6c4dc-9ebe-3972-8e5a-0ab4b1acd4be | -3.9458 | -38.40038 | 2026-01-12 04:18:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 93b3ace2-e313-3169-b734-8c3d401bde12 | -4.50833 | -43.69341 | 2026-01-12 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c585d85-f64f-36a6-a52f-3f157ef51293 | -3.94387 | -40.70142 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 92a0f0c4-475a-32da-8720-a272063a01d1 | -5.19278 | -40.74072 | 2026-01-12 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e27a41aa-ad3e-3719-9521-44be5e899eb5 | -3.95029 | -40.69815 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c8264408-fde9-324b-9236-161f6b635ee7 | -5.05847 | -41.69181 | 2026-01-12 04:18:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a93927af-f982-3aa4-98e2-be4be78a9133 | -3.82394 | -41.26369 | 2026-01-12 04:18:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a7246c9-7735-3002-9e46-c4f0cdf80d23 | -5.17841 | -37.75931 | 2026-01-12 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14f7e926-f833-30a3-8ad0-8f7443c8c3b0 | -4.05109 | -38.25977 | 2026-01-12 04:18:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec08b617-d88b-3927-a1b6-d775be546ff6 | -3.92182 | -42.27014 | 2026-01-12 04:18:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3fba2231-706f-3317-ac56-b4485d060202 | -3.72206 | -43.32137 | 2026-01-12 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5f5848b-360e-30ea-a632-b7afa547ac8e | -5.49628 | -42.15482 | 2026-01-12 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f9fa4818-26ed-354f-b387-0bd2629bd9d6 | -2.73285 | -42.83762 | 2026-01-12 04:18:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92b2506d-4264-38ce-9a75-ef6109ece869 | -5.06128 | -41.69592 | 2026-01-12 04:18:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b0c18fe-19d0-36ec-86a5-830e445508d2 | -5.91412 | -38.90144 | 2026-01-12 04:18:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 562a8e89-2810-36b1-a2c0-111644817bd7 | -2.57403 | -45.8489 | 2026-01-12 04:18:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a2087fc-e55e-39f9-b5f8-853560b5216e | -2.72952 | -42.8371 | 2026-01-12 04:18:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c50b2c7-4574-3370-8b6d-d467930f7ff4 | -3.60102 | -42.8925 | 2026-01-12 04:18:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f161d3d6-7979-3941-b027-52be68b2c74a | -2.51339 | -47.56867 | 2026-01-12 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5cd381af-9383-37a6-847e-5cc87eb62408 | -6.15435 | -39.68755 | 2026-01-12 04:18:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 695891e1-46e8-36a4-a922-dfe58772abcb | -5.49908 | -42.15886 | 2026-01-12 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8ab71af1-5468-3c22-bf91-b66c4dfcd30d | -5.65336 | -41.16788 | 2026-01-12 04:18:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 83c97879-6a38-3129-9ddc-0ea483914a0d | -1.8544 | -47.48257 | 2026-01-12 04:18:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf7cd62d-b5a3-34bc-a0bd-3bf2e477b224 | -3.94193 | -38.39978 | 2026-01-12 04:18:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ab413827-ccbd-387d-b6f9-61ed8562cc2d | -2.4672 | -45.5799 | 2026-01-12 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06d235a7-1cd6-355d-b26d-2396c2ab6a48 | -3.94791 | -40.69819 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| df26c58a-6d82-35c8-8e38-f084ad518828 | -4.70461 | -44.47896 | 2026-01-12 04:18:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70a3c9a3-59a8-349e-b544-fd236a555a92 | -3.79427 | -41.6055 | 2026-01-12 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecf253ba-a561-3e03-bf0c-b62d0f24a779 | -5.42775 | -37.72856 | 2026-01-12 04:18:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2189593-7cbe-3b63-aa4a-7bda3bd02e0f | -5.49683 | -42.15129 | 2026-01-12 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a2df006a-8f0d-328b-b841-95be1a08f7cb | -2.57772 | -45.84949 | 2026-01-12 04:18:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db499c77-b91d-33f6-9d8f-df670a345716 | -4.22007 | -41.76906 | 2026-01-12 04:18:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7c97aa1b-94d3-3551-8547-016ca14af231 | -3.94627 | -40.70139 | 2026-01-12 04:18:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4b023f27-3e36-3342-ba6f-28d4cfccf9c5 | -3.91772 | -40.39145 | 2026-01-12 04:18:00 | NPP-375D | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a404aa0-b2cd-3b7a-b560-9513f1ad64eb | -3.79763 | -41.60601 | 2026-01-12 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c37a876-53ef-3a55-ab3c-88661eee563d | -4.73782 | -41.33316 | 2026-01-12 04:18:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a771cbc0-605f-3800-a209-5d3e5f1941f4 | -4.60863 | -40.55322 | 2026-01-12 04:18:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89105c66-cbfd-3df7-8799-e5fab5a15697 | -4.91331 | -37.48614 | 2026-01-12 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25c6506a-ecee-3d4d-925e-a6f410fc053f | -4.21953 | -41.77258 | 2026-01-12 04:18:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b98c48f1-578f-3fed-9d10-3179ef411b39 | -4.51897 | -42.64414 | 2026-01-12 04:18:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 800a22bf-46ca-361a-af9c-5b4a94846a8c | -5.34309 | -43.36367 | 2026-01-12 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b19bec0-8a63-3667-a898-d9e6b934c0b4 | -2.51749 | -47.56934 | 2026-01-12 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 254fe148-c5f6-3fe7-bedd-9d952ee91d70 | -5.17788 | -37.76295 | 2026-01-12 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0dcd2867-c3bd-3f71-9f29-c1214ec0f59d | -12.26924 | -44.39391 | 2026-01-12 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23221a9e-3081-3eb6-9bde-a7b497ebe709 | -11.88676 | -44.71524 | 2026-01-12 04:21:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe90c2db-53ef-36bc-810f-9a06ae1e31f7 | -5.87522 | -43.58693 | 2026-01-12 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fe65d28-89da-390d-807c-e76b48b90e6c | -10.87236 | -44.03502 | 2026-01-12 04:21:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0a270d2-efdd-3b1e-9da9-ef82d9a338d4 | -11.93051 | -44.23048 | 2026-01-12 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01a633e9-39fc-3ed5-ba1e-5f980c220753 | -12.60311 | -43.31564 | 2026-01-12 04:21:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83ebe489-c0a4-3c15-887a-17cebeccbdb0 | -9.77554 | -36.1288 | 2026-01-12 04:21:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cf3b64e6-6066-31f8-bcf5-2b53e6c4b733 | -6.95055 | -41.09678 | 2026-01-12 04:21:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e1c1b5f-4c3e-3687-8f5e-8211bec0f4c0 | -12.08754 | -43.76418 | 2026-01-12 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6163e53-ec7a-3ae5-a1ff-48b7982df7aa | -12.5985 | -46.52866 | 2026-01-12 04:21:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa1d9b00-35bd-32f1-b545-85078ae5c0dc | -10.55042 | -44.33578 | 2026-01-12 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6abe881c-6810-327e-b226-44a95ac6315e | -9.78233 | -36.13109 | 2026-01-12 04:21:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7b1fe610-21a1-3b82-b70b-23240fb82dbe | -6.94706 | -41.09629 | 2026-01-12 04:21:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 016d7f16-3866-3d71-a045-218555305c5b | -6.77026 | -38.56143 | 2026-01-12 04:21:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd77eb96-6e75-3cf8-9026-8bd31dbd3674 | -6.97822 | -40.96231 | 2026-01-12 04:21:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fea0b301-7385-33bb-bf07-5431613d54c4 | -7.99986 | -43.24337 | 2026-01-12 04:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8875bca9-2446-369a-bbe6-4d28f5c1636b | -7.80972 | -36.44373 | 2026-01-12 04:21:00 | NPP-375D | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf39ed48-28ff-3d89-a6c7-bff07e5c38d5 | -12.31324 | -46.91988 | 2026-01-12 04:21:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b2661aa-12db-35c6-a8c4-4158574ecd95 | -6.64553 | -37.3752 | 2026-01-12 04:21:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7715bc73-94bb-3ed8-92ae-9e422536ba5e | -9.78527 | -36.13079 | 2026-01-12 04:21:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c8b064e5-5b04-3b2a-84d9-ccab0d864ad8 | -10.55265 | -44.32174 | 2026-01-12 04:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3700ab4-9e55-3ab9-b4b4-ca38e27ebbb1 | -7.99598 | -43.24633 | 2026-01-12 04:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cfc2c049-dfaf-367f-bf40-061cae6b2d1d | -6.24722 | -41.24827 | 2026-01-12 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56e1d523-8a48-38b4-a9aa-650c5b9bf9ec | -6.9753 | -40.95794 | 2026-01-12 04:21:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17904d5d-d0b7-302d-840d-e9b5eaef0c58 | -5.8453 | -43.41461 | 2026-01-12 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 363c4781-b56b-34ca-8801-38a1bd85e84c | -7.99931 | -43.24686 | 2026-01-12 04:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a54ea708-abe4-3299-8aa4-6221ece7f83b | -9.78043 | -36.12961 | 2026-01-12 04:21:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3069af1c-71fe-3111-9ea1-b52c3b6d323b | -10.55653 | -44.31877 | 2026-01-12 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10e3de22-a94f-3ea6-a058-84946ea3130a | -7.99266 | -43.2458 | 2026-01-12 04:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38371867-b4da-3eba-8380-249fcd9b51b1 | -17.10142 | -46.4673 | 2026-01-12 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc103839-eac0-3ace-8b05-68295534af13 | -20.12033 | -46.85904 | 2026-01-12 04:23:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README4.md)
