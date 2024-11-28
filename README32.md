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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865c2361-e489-31ca-b431-fbb97f35f03a | -3.38244 | -50.12229 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e49d1c5b-ff20-35cf-b7db-aafb2d22f772 | -6.16518 | -42.6156 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0d5b520c-24b8-3f82-afd6-42a02e2da0f6 | -4.72232 | -43.25465 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28ff4293-6fd1-3d8d-aaf4-e7daf251da67 | -1.32988 | -51.93507 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a4c6e1fd-1259-3e53-b28b-c6e6eb9cfb71 | -2.05766 | -47.12208 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e5b7aaf-50c7-3207-b68e-c8368c2cd618 | -3.37875 | -50.1078 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50e86d50-f714-3b43-be68-7e00e0068a84 | -3.43904 | -50.00843 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff9de8b8-18f2-37e4-9be9-720e7fdfc1c4 | -2.7491 | -48.65834 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f36a4810-4e42-366e-8b55-f50b6d84f677 | -2.51871 | -47.4056 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d017664-4720-3bc4-a462-c7695c1f81a4 | -3.38318 | -50.10849 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56da088b-4a59-3826-8f1e-2b59dfdebf9e | -2.01719 | -46.39627 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50be571d-655f-3248-bf31-7e461363bde7 | -4.04963 | -48.33395 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8badb12d-9dae-38ae-a891-177cd9613425 | -5.22588 | -44.91623 | 2024-11-28 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 024f6bd3-d540-39a7-a5eb-8ceee554e256 | -2.94321 | -51.58561 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 147af9b3-8cef-35d2-beb2-23a574d665a1 | -2.61691 | -49.07314 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bec32f3d-d68b-3cdc-be1f-5d4f04b1be15 | -2.85876 | -46.86119 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e0cd29f-e2d7-3ddc-842f-760129029369 | -4.0017 | -44.281 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e667a384-1a32-3cff-bd80-a476db4e5bd0 | -3.39224 | -50.31993 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54e79ad7-6905-3b07-ad7c-50cad973d12f | -8.65934 | -39.57129 | 2024-11-28 03:59:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11c47012-8949-34c6-badb-527710a48fcc | -2.84682 | -46.84249 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba1f9d24-abfd-3c73-b6f8-31864fe5b5c9 | -2.8405 | -46.86794 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9b5da11e-d42d-3170-b975-43b08cbbcc48 | -3.69725 | -50.22374 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9589ff44-cbfb-39a6-af05-fa5b180ebe4f | -7.03388 | -35.00851 | 2024-11-28 03:59:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a928d2d7-bf70-37ac-88fb-a37333ccb851 | -2.84977 | -46.84142 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3555922c-62d7-35dd-b792-70f5a4216ae1 | -6.19346 | -44.42853 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a846e8dc-5bdb-33db-95a8-295c32bafd7d | -2.15387 | -48.71487 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9b0d7efe-c31a-37f1-81de-8e11582f09fb | -3.68386 | -50.87932 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92aa5029-f7f6-34b7-aece-aa5c9a836376 | -5.30288 | -44.43407 | 2024-11-28 03:59:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bd1897e-9081-306c-88ce-491c9c6bffeb | -1.7462 | -52.05473 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e041b58-5605-38ac-a294-2afd298a04a4 | -3.96537 | -50.19427 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7e1e9dcb-feb9-3d4f-8eb1-4f98dc16a6ad | -2.13863 | -46.48462 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 998a686c-cc68-3c2e-9ef7-3e9ff77a9a8f | -2.8459 | -46.84792 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d718e1b-1180-3baf-af9f-a74b3e099ce5 | -1.68837 | -52.50018 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d24b1207-9e4e-3a6f-b9fc-974d4ad8b19a | -3.08653 | -49.20931 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 456cfa21-50c4-3ccf-9460-a269dc237dc7 | -3.16947 | -48.43413 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c377501-5f5e-3173-afb7-24a58eb29b8f | -3.12871 | -51.04297 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9872b754-5303-3187-8569-be42d101931c | -3.93347 | -47.01847 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f15314e-27ef-3557-8fcf-02d01cd66959 | -3.67032 | -45.79129 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e3baa49-a42d-32a1-96e5-1f99273c0856 | -7.7064 | -42.98827 | 2024-11-28 03:59:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c56c223a-6f39-313f-86e0-eaa47eee4eb2 | -3.61301 | -40.81233 | 2024-11-28 03:59:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b73d1ce4-24bc-3d12-9db7-ce4a8e384b56 | -6.6526 | -42.66253 | 2024-11-28 03:59:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff71b6d9-f26e-3546-bb82-a9dd6e4f2011 | -6.99498 | -34.90885 | 2024-11-28 03:59:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3144176-b7ba-35ea-8ef7-0568aea6180a | -1.6928 | -52.49347 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85491195-4523-3fba-933e-c56bf6c90f50 | -1.57903 | -52.26082 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9792f9c3-266e-3312-84ef-db479ce9b8dd | -2.95496 | -51.28291 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d3424c6-26e1-3f86-8e95-4b97a2e198f2 | -2.83998 | -46.83985 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65923373-6ba1-3722-9e05-b4a36a8a948e | -5.19477 | -44.24902 | 2024-11-28 03:59:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b8ebeaf-6eda-302a-a358-c52a3c5bca8b | -4.77549 | -44.42962 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e827d529-c875-38d3-baaa-b79f833f1c9a | -6.12255 | -46.59245 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a171518-e55f-3844-8145-e1e2f8d5d272 | -2.48013 | -45.87221 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ceb6edb-0b0c-3281-8f79-bc762b40ec8c | -4.43971 | -46.34268 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 120ab333-1a5b-3f01-a6ea-e0a4189a341e | -2.80662 | -46.82889 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ad64c78-ef8e-3e3c-bd7a-50f1e751f809 | -2.53063 | -50.10848 | 2024-11-28 03:59:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d5c345-e34f-388a-bff4-cf222c65d48c | -2.13467 | -47.15871 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73b72497-3b06-3d45-9340-b4a4a8c80752 | -3.09121 | -50.35595 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 157bb157-5682-3c20-a16d-cad169613b90 | -7.69206 | -42.97475 | 2024-11-28 03:59:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7aad8950-3ec7-395f-8737-c40e5326f5b9 | -3.17228 | -48.58549 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1dc64196-39fc-336a-be6c-1a0bd734c92c | -6.37297 | -45.69411 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 243794f0-7f41-36c8-8ad9-881e32773869 | -3.06021 | -51.29481 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c90a5a3c-f13f-3d61-8fb7-2f8176e17b82 | -1.34808 | -51.99139 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efa0ee12-7a3f-304e-9bc1-f62836189d11 | -5.62265 | -39.69448 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d49a1e3e-4939-38a8-a525-7e75278824a8 | -4.65995 | -44.04274 | 2024-11-28 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f293f2db-79b9-3509-a6d7-9e4cffc43124 | -1.31709 | -51.92622 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ded36ba-f57b-332a-96b4-c607463598af | -5.95095 | -39.67125 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5e53f28e-c254-3a89-9d1d-ea2fb1bf8340 | -5.64253 | -46.38313 | 2024-11-28 03:59:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7ed647a-1f3c-3fed-97c0-f73c2ebbd8a1 | -3.34558 | -50.51925 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ffcaad2-43bc-3122-9b53-8c216b02c0f1 | -6.66799 | -47.8736 | 2024-11-28 03:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9417da39-a18c-37df-b5fc-a3d0d6920e1f | -2.4617 | -46.24668 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22ae989e-ab17-3478-bd0c-670dd137ef8b | -2.39324 | -47.16792 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 83577215-670c-3b9a-aa6a-b027cda231ea | -3.58977 | -50.69567 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e23fc53-44d4-3328-87c8-14a118c921b3 | -3.08534 | -41.14298 | 2024-11-28 03:59:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75488135-51ba-3798-87d1-e8e02ddb4799 | -1.58383 | -52.27549 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c548346b-a8e4-378e-aed9-f42f04660f92 | -4.53655 | -44.61687 | 2024-11-28 03:59:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 103d69a9-2686-3982-aa87-8d74e1004a89 | -6.11789 | -46.59404 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df8a35e9-5808-3d0f-8c36-7f8df557a6ff | -2.96217 | -51.00707 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dfd22f7-2b19-34f9-a82b-f052394e5078 | -3.50377 | -50.32647 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 645c6296-d4f3-3f87-ba8d-e6cd868795d9 | -2.87127 | -46.84648 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8599b2d9-bc17-3478-9c2d-86fc5f73e423 | -6.16874 | -42.61617 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 07767029-6bd7-3b0d-ac33-976fd0c9de50 | -3.22974 | -45.38823 | 2024-11-28 03:59:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f143709-7bf8-31a6-b2ba-13638fefe9de | -2.77856 | -48.5818 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1efa6dfc-6ce9-33f5-a93e-953fa4bf52c1 | -3.17973 | -48.4394 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1634293c-ecc6-39b7-83d2-0877db7e42ea | -2.8391 | -46.84534 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4759fe8d-f26d-3ae7-ad8f-27169f410c6c | -2.83607 | -51.84499 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e67022dc-1ff3-3b23-b68a-6c54b4bc1087 | -5.31192 | -43.08099 | 2024-11-28 03:59:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76bebc2a-b295-3b02-9fd6-9fee63d7252a | -6.01376 | -38.65751 | 2024-11-28 03:59:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f991227-bb2f-3dfc-a6ca-2611c5f66639 | -6.3991 | -39.55356 | 2024-11-28 03:59:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9d091f9-27d8-38a2-ac9a-43922a8b9409 | -2.84488 | -46.84061 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2446e3fc-f43f-3d47-8441-7d3170a91b2c | -6.75596 | -35.10125 | 2024-11-28 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c93cedd8-536a-3534-b6c6-de0a99d89259 | -6.7705 | -39.06085 | 2024-11-28 03:59:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63ff085b-df93-339c-9c24-825d71377681 | -5.9705 | -45.37026 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3de490cc-031d-3cbf-9498-5f7632d08a63 | -2.31528 | -48.14933 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e341d57f-311d-3080-bd07-66dae79e744f | -4.53596 | -44.62046 | 2024-11-28 03:59:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e05f81-64af-3384-a365-a3befea1da92 | -6.75997 | -35.10173 | 2024-11-28 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 12f04392-92ba-3b30-8269-7011b1554ed7 | -2.85295 | -46.86588 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95947a56-70a0-3fb6-a55f-6430fa534475 | -3.27238 | -53.30298 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22693477-d9b3-391d-9578-961727bfbf07 | -5.66006 | -47.05262 | 2024-11-28 03:59:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2130bf13-2554-3f76-9769-f240731e589e | -3.59879 | -50.3593 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f4e22a7-f80b-3e4c-a4ae-75045631dce2 | -3.38921 | -50.10945 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1db14766-4934-3cc7-a5f6-5eeb2ced9b92 | -2.7778 | -48.58511 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cce8e091-82c4-3dbf-a0ac-36fad61e6eec | -4.038 | -46.53859 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README33.md)
