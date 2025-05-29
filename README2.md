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
| b8babbaf-867a-3703-bc90-609deb0af99b | -10.736 | -49.30093 | 2025-05-29 00:56:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| b2e8feec-c02c-3872-9a3b-3030c05a364b | -7.62957 | -45.76053 | 2025-05-29 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| e81dfc9d-3a10-39ff-bbed-b6d7693c9605 | -7.6692 | -46.09492 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 43d07eec-d089-3f34-85a6-586b50e717ac | -8.01254 | -49.6881 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 34929319-aa86-367b-bd85-468d354708d7 | -10.65701 | -44.49213 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 0322025d-5d3b-344a-8d46-769034569d48 | -9.29837 | -50.43375 | 2025-05-29 00:56:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8369cba2-863c-3c92-b9d1-1a61255c930f | -12.30144 | -50.08999 | 2025-05-29 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 517cc80b-c058-362d-9f5a-335325d6fa46 | -7.23056 | -43.08958 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.8 |
| aa5f63ed-69a2-3e5f-8c7d-3ba657f02f7f | -7.66843 | -46.08944 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c9c4ecd6-0d10-3be1-b7cc-9cea0ea0e849 | -10.52855 | -47.5862 | 2025-05-29 00:56:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7738b614-8c92-321d-bc6a-37491fa6e474 | -9.20354 | -49.47692 | 2025-05-29 00:56:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c1a85ad2-f08e-3592-a4f4-75653b11c9ee | -9.20513 | -49.48766 | 2025-05-29 00:56:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1da1b1bf-c78a-3298-a4a0-3f6c7c6da12d | -8.78642 | -47.93693 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 02c1c61d-ee0f-336a-b5a1-c430918f6438 | -7.62623 | -45.73947 | 2025-05-29 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| cd0c6ea1-ebf8-332c-a718-3bd46f4b474d | -7.63313 | -45.95078 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 70272169-14cb-36a6-91df-046b38082214 | -8.01474 | -49.68187 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 86b7517b-58ad-3e74-b960-a3302cb47f0c | -7.6165 | -45.74617 | 2025-05-29 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 04fbf558-ad37-34c2-8010-9d5f41b406eb | -11.29291 | -46.43412 | 2025-05-29 00:56:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1d538475-881e-30b9-8471-d928cc569c9a | -10.65052 | -49.44465 | 2025-05-29 00:56:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 43e1ecd2-c0d4-3c14-b122-73bd4382f35a | -6.82806 | -44.67083 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| e2c01728-cc46-3463-88ac-f778c8b83cee | -7.98351 | -49.69239 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ab8deb29-8905-3316-9d77-7ed2ce100dde | -9.03888 | -51.13974 | 2025-05-29 00:56:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 97a8cef8-8497-383b-80ef-5821cc69525a | -7.18747 | -43.13248 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| edb867d7-d648-35b2-9a8b-ef0fb6e8960a | -12.38482 | -49.96414 | 2025-05-29 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a442c637-0963-349b-866d-f5b81cacf2ee | -10.6727 | -44.41544 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6cfb07ab-e805-3d01-86b8-6828487f2ca6 | -7.07866 | -44.90998 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 148cc0aa-61c8-3280-a718-dc651b5dc3e4 | -7.6319 | -45.93569 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1d923a99-1241-34d3-a8dd-165502fb0a8c | -6.23507 | -43.35924 | 2025-05-29 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a854c6e4-32c8-3a9a-89ee-1c4856aafd0c | -8.66768 | -48.29589 | 2025-05-29 00:56:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 40f4d407-00c3-319e-93a8-06d283bebbd9 | -7.58326 | -45.96445 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6d19e124-d76a-3d63-9a91-9e1486158dd7 | -7.46499 | -47.0621 | 2025-05-29 00:56:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 56f42f43-88f2-3043-9666-c9a2aba7b143 | -9.20193 | -49.4661 | 2025-05-29 00:56:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| efd883ef-8fc3-3a3d-a3b3-22166cfc767f | -7.08262 | -44.93531 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 758a76d1-1167-3239-96f5-e4ccf485fbfa | -12.39384 | -49.96627 | 2025-05-29 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ba2fc22-f775-3c43-88b7-68256d61be73 | -11.28527 | -46.44181 | 2025-05-29 00:56:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 625a7e8e-b5cb-39cf-a0e5-2de24e8ab888 | -10.65608 | -49.44815 | 2025-05-29 00:56:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 456e78cc-9554-3b4d-8c93-abab2075d0b7 | -5.88361 | -49.83233 | 2025-05-29 00:58:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 21f1cea5-b81c-3ff1-af8c-bfc9e419e0d1 | -6.21673 | -57.77105 | 2025-05-29 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 2a6f893c-10d1-3585-ad98-9a64626c6b13 | -2.65145 | -48.80074 | 2025-05-29 00:58:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c34447cd-10a9-341f-8b4a-4cdfa55f1bba | -10.9521 | -48.1493 | 2025-05-29 01:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 009f45d8-f065-3f7b-bbdc-39e422bb994d | -11.818 | -44.2703 | 2025-05-29 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 345bf16b-1010-31b6-b402-5e896a223bc1 | -7.2403 | -43.1134 | 2025-05-29 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| c0a6e950-a843-3a6b-8063-82f52f86dadf | -7.2405 | -43.0899 | 2025-05-29 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 6b404145-22b0-3681-9fdf-f7f22f214d41 | -11.818 | -44.2703 | 2025-05-29 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1c9a3f2b-96ca-3f70-931c-c5d04db6996e | -7.2405 | -43.0899 | 2025-05-29 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 2316cde2-a9f4-3b4b-9398-d78edfb7b95b | -7.6762 | -46.0995 | 2025-05-29 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4434c1fa-1b40-3d1b-83d1-e95e8fad967e | -7.2405 | -43.0899 | 2025-05-29 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 509733e2-c66d-3fca-bf7f-d3058d097be9 | -9.5725 | -40.3227 | 2025-05-29 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 83ba7053-7052-3e9c-9f74-9fbf3e678a52 | -11.9715 | -52.4715 | 2025-05-29 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 33b59638-86a8-3f08-a3e2-f47c13aebdf4 | -11.9718 | -52.4506 | 2025-05-29 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 67122913-ac96-32d1-ad42-149b7bef11f8 | -9.5913 | -40.3448 | 2025-05-29 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 07f97b0e-f67b-39d7-8831-fea6f6dcc3ed | -9.5721 | -40.3475 | 2025-05-29 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 2320a5dd-2cc3-37e5-84e1-b6ba53101fb6 | -7.5387 | -43.3651 | 2025-05-29 01:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| acc59b3a-42ee-3d48-951c-afbcfe5249e1 | -7.2405 | -43.0899 | 2025-05-29 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 45bef148-b156-34f5-89cc-cf13022f60e0 | -9.5917 | -40.3199 | 2025-05-29 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| c9c1d658-1ab4-373f-88c4-dffe278de454 | -11.818 | -44.2703 | 2025-05-29 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 62699a29-6118-3987-9b9b-596d318d97a9 | -9.5913 | -40.3448 | 2025-05-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 987aaae3-a055-30d0-b984-d65ea44db623 | -9.5725 | -40.3227 | 2025-05-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.3 |
| fc72bce2-2550-3a6f-a1d4-ef240a2435ae | -9.5917 | -40.3199 | 2025-05-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| d2e9e5c6-451f-31c2-816d-b5cffa6430b5 | -9.5721 | -40.3475 | 2025-05-29 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 54512e22-f828-32c7-a5e1-7c081db4820f | -7.5387 | -43.3651 | 2025-05-29 01:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 7e700cb8-b673-32a8-9cbe-68e274f29ef2 | -11.2834 | -46.4365 | 2025-05-29 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| bd6df8c9-b8c9-3b70-843b-5422464775e6 | -7.539 | -43.3417 | 2025-05-29 01:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 165.5 |
| df0ab49c-e785-3297-88f9-7225ec37d3a4 | -7.2405 | -43.0899 | 2025-05-29 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| fa33cbe4-5d5c-3f85-88f0-b15dd531c9d4 | -11.9715 | -52.4715 | 2025-05-29 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6004a7b0-b2ba-39ce-a7ad-311988a3699d | -11.9718 | -52.4506 | 2025-05-29 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a39f4dbe-d493-3269-a29f-a4bc73a4e6f6 | -11.9718 | -52.4506 | 2025-05-29 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d090cd2e-edae-3de7-aca9-5b25151256cf | -9.5913 | -40.3448 | 2025-05-29 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 249.0 |
| e7f125b3-ede1-36d6-b5ab-0c8b511c9daf | -9.5721 | -40.3475 | 2025-05-29 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 301.8 |
| c6e0a522-9f23-3861-be05-abd5f5ab21e9 | -7.5387 | -43.3651 | 2025-05-29 01:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 377d026e-76a9-30e1-a977-499b11f302ea | -9.5917 | -40.3199 | 2025-05-29 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 244.5 |
| c85640c4-2637-3c71-a469-2ce40a43c739 | -7.5576 | -43.3632 | 2025-05-29 01:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2155c50c-e357-3dc5-97dd-9faf63dcbdbb | -7.539 | -43.3417 | 2025-05-29 01:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 96e0fa0b-5fb6-3bde-868d-8d22f228c58e | -9.5725 | -40.3227 | 2025-05-29 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 269.5 |
| 5ecef86d-fc6d-3adc-aa05-8b73e2ea2b3d | -11.818 | -44.2703 | 2025-05-29 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 82b73816-137f-35ad-b78a-690241a3766f | -7.2405 | -43.0899 | 2025-05-29 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| ab665655-e3b6-37c0-bc65-2080b459997f | -7.2405 | -43.0899 | 2025-05-29 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 6a42bbcb-3f86-31cc-bad5-3443e56faa1c | -11.818 | -44.2703 | 2025-05-29 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ea55c369-49c5-35d4-97bf-d50c26b3a9d5 | -7.539 | -43.3417 | 2025-05-29 02:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c908ffe4-c7a8-306a-abca-3d848ea9aa6c | -7.5387 | -43.3651 | 2025-05-29 02:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f951e1cb-7b10-3f29-82f0-3e78c2ab2ac5 | -7.2405 | -43.0899 | 2025-05-29 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| db22b458-2f9d-3172-8b67-a932f0889342 | -7.2405 | -43.0899 | 2025-05-29 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| f95dd02f-90a2-3bfd-ae11-61ef8e6954bf | -11.818 | -44.2703 | 2025-05-29 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2b408f82-4b79-32be-92f5-6fce5af532a7 | -6.5631 | -51.1126 | 2025-05-29 03:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0f3b697d-9940-3bc6-b6ff-168efa62b9b3 | -5.21085 | -43.31898 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c64c503a-4e76-3e57-b938-69a1f64f8601 | -5.28441 | -35.48069 | 2025-05-29 03:21:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4fc52ca7-6ada-378c-af3b-60be8b0a570e | -3.2857 | -43.4669 | 2025-05-29 03:21:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bca80e2d-b425-3b4b-9195-a59bdfa94a4f | -5.21879 | -43.30648 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a705b9c8-e139-3d7e-ac78-5bbe7756e352 | -5.76724 | -38.90407 | 2025-05-29 03:21:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd0df780-bb95-38e9-a8c7-69ca17491817 | -5.20971 | -43.31813 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fb060883-b767-3e96-ad7c-9a30413843a7 | -5.7642 | -38.90511 | 2025-05-29 03:21:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a2f2cdb-5451-3658-b229-960f5437168d | -5.21199 | -43.31278 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 91739bef-dbba-37ee-9b2a-635c9f5f10ea | -5.21193 | -43.30558 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 780d0e77-0b24-3e99-bf8d-cca5ae1d47e7 | -5.21315 | -43.30646 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fe43d293-0f2f-3794-9194-182b6a3c9d69 | -5.21767 | -43.31277 | 2025-05-29 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25ea3881-09e3-391d-9cf1-5aa9bf1c1424 | -5.31989 | -38.0035 | 2025-05-29 03:21:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 051006a2-2d33-335d-a04b-b0df9223158d | -7.23383 | -43.10038 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| b443cc40-85b1-3078-85b8-355d5d719f6c | -8.07428 | -34.97702 | 2025-05-29 03:23:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 294aa4d3-3515-3f7f-b4eb-253bb9a3cac3 | -10.65154 | -44.49616 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4edeed7-434d-38a1-82d5-e5ec4bfe20be | -7.18503 | -43.10891 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |


[Clique aqui para ver as próximas entradas](README3.md)
