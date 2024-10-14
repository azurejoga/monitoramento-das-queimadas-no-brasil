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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37ccee7e-7e48-32a5-b191-615f38db8bb6 | -3.93012 | -46.43484 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 562ad113-5bf5-318d-98bf-b63f2ae222a8 | -3.85558 | -46.91853 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261a67be-c2ff-3747-8500-799113fb6197 | -3.85506 | -46.92212 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95c63711-de39-3260-bada-93cff0d06595 | -3.85166 | -46.91788 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e61c34c5-12fc-3280-bfa3-2dedd9c85db5 | -3.85112 | -46.92146 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95ec272b-8548-37aa-9493-45220b2f5783 | -3.84942 | -46.92154 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 614e3d65-6ced-3204-8182-f349c071f32b | -3.84087 | -46.47923 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9fddd02-a7fe-3916-99ca-360b0b82a53b | -3.83511 | -46.47831 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cddbcaff-5d4f-3f16-bfbc-bbc76e9cb518 | -3.83452 | -46.4824 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eed732aa-8080-33ec-bbb9-c7e6ea98faa3 | -4.67395 | -46.29918 | 2024-10-14 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3ba7e23-d71a-3f91-868f-2b7903cb8428 | -4.67214 | -46.2971 | 2024-10-14 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b174fcfa-69b1-3b8a-81fe-ec0eab8058d5 | -4.67154 | -46.30137 | 2024-10-14 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18061a48-8d88-314b-ac74-89f3a9e34f85 | -4.66806 | -46.29817 | 2024-10-14 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c1091f8-3dac-3b2c-b37b-78cfb912ed1e | -4.65924 | -46.80992 | 2024-10-14 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84331e83-dcf4-3a90-a4d0-2c52e0bbac3d | -4.65868 | -46.81381 | 2024-10-14 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 860f527e-9506-3165-9db2-7fa858785f74 | -4.65355 | -46.80888 | 2024-10-14 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13975a92-6148-378a-8490-d01c496e0e96 | -4.65299 | -46.81279 | 2024-10-14 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 149880b2-8fdb-3939-90a0-6b0d8c7d7468 | -5.64963 | -47.9232 | 2024-10-14 05:08:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11cd6f6b-b046-3004-b53f-d486faee1b70 | -5.64916 | -47.92656 | 2024-10-14 05:08:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 280781bc-6c06-3db6-9153-ef5d69b11853 | -5.14358 | -47.59714 | 2024-10-14 05:08:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7e40534-27c1-3329-86e4-6896530c7769 | -5.1431 | -47.60059 | 2024-10-14 05:08:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d1832c6-92c5-311d-ab7f-3c70b37884e8 | -5.14238 | -47.59893 | 2024-10-14 05:08:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4afa5d0c-ee79-31dc-9f05-03e71ecb230d | -5.13277 | -47.35557 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 86f492af-fd1a-3c3c-a365-87904262a2f5 | -5.13227 | -47.35905 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebf70485-ccc3-31c2-a48d-7dcfb64671d9 | -7.67081 | -47.31607 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca9f3f14-4b53-3c33-adad-dbd170e95394 | -7.66974 | -47.32416 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38c13842-b646-3631-a78b-8d864f295f0c | -6.98326 | -47.32826 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a6e0185-df99-3cc3-83dd-2225763e0d4a | -6.94673 | -47.49267 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| de99c07a-c122-34fc-8bdd-e963df8c745c | -6.94621 | -47.49641 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 73d59f26-e2ca-3516-aaf0-17d2cb81b95c | -6.94112 | -47.49164 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c181b9d4-98c9-3d5d-8399-064ca6eeb81b | -6.9406 | -47.49535 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fee6bb88-cd3b-3166-86a5-03536395ef23 | -6.93601 | -47.487 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d93077c9-8e1e-360e-a921-357913d818c9 | -6.93549 | -47.49073 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9eaa95e8-358a-302a-9396-7d2b6da4d54f | -6.93141 | -47.47857 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fbe3111b-4d11-3841-a53c-296449be142d | -6.93089 | -47.48238 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c8bef38-89fe-322f-9232-c3b683d9a789 | -6.93037 | -47.48617 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d89105c2-eb08-3e54-9a96-ad4446c1b17e | -6.9263 | -47.47388 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cac6e171-affa-3d41-a123-a42befea2300 | -6.92116 | -47.46936 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 574cac67-4f54-3996-b759-6f91fc304c52 | -6.92065 | -47.47309 | 2024-10-14 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e72ae9a1-9a6a-3f8f-84ff-b1ae82c79ea0 | -6.91768 | -47.238 | 2024-10-14 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0ee71ab-e9f5-324e-8ba6-a64aa805404c | -6.91715 | -47.24192 | 2024-10-14 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b8c9844-a213-3daa-9449-0a55efdfa55b | -3.21979 | -48.92322 | 2024-10-14 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3769aa50-823e-3397-96e8-2ba4efcd6bc4 | -3.21887 | -48.91917 | 2024-10-14 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 350fa3be-e9cb-3c29-b882-164bf61a0386 | -3.2181 | -48.92448 | 2024-10-14 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3e4b45a3-93c1-31fc-9998-0f29b7f194b4 | -3.12922 | -48.61243 | 2024-10-14 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a349465-e0e6-3c1f-98c3-4dc7fd5aff16 | -2.87405 | -48.90862 | 2024-10-14 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76bdb26a-b565-31e1-b618-bb645f18203a | -2.76073 | -48.65007 | 2024-10-14 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49bc60ac-fd78-35f5-afbe-7497a4ff3b94 | -2.75064 | -48.40556 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc3e589e-8374-3522-b82f-2b7375ea7d81 | -2.7502 | -48.40842 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 612059df-f64b-364d-9e48-6323488d12d5 | -2.74976 | -48.41128 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e4123c-233f-3a50-9c58-dfb966c76d2a | -2.74566 | -48.40475 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c510e9dc-de53-3ca0-b149-9340d0640d10 | -2.74523 | -48.4076 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f32f720-6fd7-34ec-9eec-92f1084412e3 | -2.74479 | -48.41046 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cec96e57-0fd8-3299-8bc5-1399ab41c578 | -2.47577 | -48.19525 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e101c54-9dd6-32b2-a7e3-774a49d9f7a3 | -2.47524 | -48.19332 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5314e0fc-e3d2-398b-bd0f-8be11799f9d4 | -2.4748 | -48.19628 | 2024-10-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a758b5c-dd9a-38bc-a9d9-03cd507411d5 | -2.17309 | -48.36585 | 2024-10-14 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a92e84a-6579-32e8-a169-4b548f92e59c | -4.90583 | -48.63893 | 2024-10-14 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b44ac8-cb60-3f92-bfa1-8c0be8ca2511 | -4.90076 | -48.63819 | 2024-10-14 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c5651bdc-5c89-34f6-82f7-0e19a78cc320 | -4.31952 | -48.63058 | 2024-10-14 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eebfdc4f-463d-32eb-b5ab-0e473ca1e017 | -4.31909 | -48.63342 | 2024-10-14 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41b868f2-b76c-3f12-83ac-85d09b0d4d4e | -4.31867 | -48.63627 | 2024-10-14 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1247ba1-7e4c-3962-b485-546cc504ca4d | -4.27896 | -48.59161 | 2024-10-14 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1b58590-950d-335c-b3c5-4359a6400629 | -4.27254 | -48.22234 | 2024-10-14 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e38d7b7-f43c-3ce7-891e-7b459661dc69 | -4.27209 | -48.22533 | 2024-10-14 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0323373-b26f-3e4c-b8fa-dbd5f6d9a1fc | -4.12047 | -48.27694 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 337b5719-a9bd-39a5-aee2-8a78fe927f84 | -4.12002 | -48.28003 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a0a0db7-24ae-3987-8329-1db1cf103966 | -4.11955 | -48.28321 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e72825b0-a026-3bc7-83c5-da72cb83c0b5 | -4.11909 | -48.2864 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 476193b6-01eb-31dd-b14e-652044419099 | -4.11547 | -48.23914 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 408e8078-ab3d-3735-b7d9-18e0c4383518 | -4.115 | -48.24235 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f425c92-5f6a-395c-95f0-eb7b49c4f75d | -4.11491 | -48.27909 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91453dca-0306-33dc-aed3-530befc318f4 | -4.11454 | -48.24551 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 984a5119-06bc-3642-9383-6b6b4d5748c3 | -4.11446 | -48.28217 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d723ffc7-e77b-3dc4-921d-98880f1ab385 | -4.11401 | -48.28525 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d01f17e-2309-3474-9600-0e3340c07694 | -4.11356 | -48.28833 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd3dad4e-6729-3d03-af2d-35e1b258406e | -4.11311 | -48.29147 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9b54a92-7548-33b9-b615-c2d97e6f0902 | -4.11079 | -48.23516 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 42891e5f-5fcc-3a8a-9c04-a7da7ba772e2 | -4.11031 | -48.23843 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| d55f7e16-53c5-35f3-b4cc-17841016a153 | -4.10986 | -48.24158 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 11bee168-018e-316c-bd70-3a2e4a5bfe89 | -4.1094 | -48.24474 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7d209913-a9de-366b-a807-9661fb41f873 | -4.10934 | -48.28129 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3256dbd-7414-3c36-8169-82b73235ce42 | -4.10895 | -48.24783 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 013ae0b7-4218-3f25-83cf-2496fa3260b0 | -4.10891 | -48.28428 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c92282-267e-38e4-a232-c9f130245146 | -4.10847 | -48.28728 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d6d553-cbf9-3b57-94cf-0afdddb00345 | -4.0836 | -48.27802 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b0bb3bf-8d8a-33fc-bc3e-85559bb6f3f1 | -4.08316 | -48.28107 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8b715d5-2c40-36d4-a9eb-28e7070b576a | -4.08085 | -48.27902 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd36272-ac97-3b24-b371-c9de1f551194 | -4.04909 | -48.24572 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ff0c35f-3161-39ee-8e2e-b62073f4e719 | -4.04862 | -48.24891 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67fb75d0-c8ef-3f77-b4a1-5b9d845cfd96 | -3.92565 | -48.35466 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69b5c1d0-2fd5-3255-948f-ba9f093a8390 | -3.92522 | -48.35756 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 285fcb83-4ac3-375b-8e9e-ed3c39279718 | -3.92478 | -48.36048 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f0db1ad-ee29-36dd-b558-d1fd05a7a1b5 | -3.92101 | -48.35087 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 859b3779-41d5-314f-8eb1-1c933647edb7 | -3.92057 | -48.35384 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a76e11c1-3eeb-3057-bc9a-4e165d16e448 | -3.92013 | -48.35681 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 636c8463-ddc6-3d22-bb5f-a64d3e203834 | -3.91969 | -48.35976 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 221b1ed6-caea-3e6b-872c-ae57cd30630d | -3.91925 | -48.36271 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 518ef922-af1f-3d85-8c7c-cb7a90099b60 | -3.9146 | -48.35899 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31cb1e1e-43b5-3b90-b616-f9d3ba9dc09f | -3.91416 | -48.36195 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README107.md)
