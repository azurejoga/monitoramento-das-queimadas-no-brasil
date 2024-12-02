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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 051d58df-2223-356b-adf0-76a5f285d3fb | -1.36715 | -51.38929 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf2fd5a7-91be-33d0-9315-b8f297f17fde | -3.53749 | -51.50031 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 969116b2-54c9-3fb8-9fba-4bfea671e94e | -2.8601 | -53.99087 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa9f372c-ee68-3af5-9945-e0d8cb1636c9 | -2.87377 | -54.01643 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ad00694-6fb8-3880-9386-7e1348a76c25 | -1.59255 | -51.25257 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f9b6fe4-9ae3-3a36-bf22-d62a2c72c5b2 | -2.704 | -52.0039 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31092e14-e6cb-330f-b669-257984a3d7e5 | -3.26703 | -53.63953 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 034602c5-b6b8-3149-aba2-9d7011f36586 | -4.26353 | -47.61521 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64c4f83c-74b6-3df5-b038-2948887c6c3b | -3.88533 | -49.9274 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4210db4b-954f-3c90-ad4f-e952fb7190f8 | -2.68729 | -48.85699 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97c5f469-2158-3622-a5f0-2d1af8272a61 | -2.58834 | -53.98442 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62afc799-63e5-3c78-8383-4a48b78a118e | -2.01164 | -51.20187 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efbc9bea-c53a-3bb3-a550-301902b0da87 | -3.97818 | -46.75566 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b123ebcc-8862-3f61-b9c0-51cbabceb911 | -3.43623 | -53.80965 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2a4b61-92a7-3b1f-a560-b47f90ad28de | -1.03371 | -53.55428 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c939159e-33d3-3ac3-8446-979efeae0a54 | -2.74402 | -54.16982 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7941af4-d220-322a-9e80-55894534e64d | -3.59395 | -53.78873 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 656eb0a0-0a53-3fda-8804-822ccad3358a | -2.47592 | -46.56436 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2d3d973-bcad-3949-b0bf-1734bf1af174 | -3.5258 | -52.15749 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3c42951-87e9-3090-a3b8-440e0946531c | -1.32806 | -51.7455 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9281155-2164-3f07-bec9-a36c65391e57 | -3.23976 | -53.63522 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccb2d365-6e3d-33d9-9cd4-4bc6c9d755be | -4.31956 | -48.09798 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99eacce4-e76d-3a4a-b515-a15fcfdc69e1 | -1.92505 | -52.09705 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92c92ce2-2f2e-3ffe-a8eb-8b235a8ca494 | -1.11918 | -53.74674 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a46b8eec-a5e5-3703-8484-c831cb94351d | -1.75687 | -50.85485 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2436c264-e962-3853-b34b-9d0f4616ee68 | 1.20616 | -56.02527 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e59c695b-f55b-385e-b0fc-e6ff92b0b059 | -2.44623 | -53.62 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9c189d6-74b1-310f-8423-e9a58e50ce86 | -3.73978 | -52.26546 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 182e9888-fb47-3287-86c1-b06682dbb42f | -0.94398 | -51.66078 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1897cedd-4c40-3851-94d9-a7ec69c564a9 | -4.01572 | -47.00175 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 260550ab-b699-3933-891f-78780153b352 | -2.73657 | -54.03821 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 194d59d1-2e78-3d90-986b-d1f51de5d200 | -1.67929 | -52.51142 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42d54c56-6896-35ec-9727-a27d6e1001f3 | -2.61235 | -51.80988 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 804e264b-45de-30fb-9cf0-d75af3606cc4 | -3.91743 | -47.09586 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b1189f2-7688-30c3-a5a2-6d44d1e38342 | -2.56361 | -53.96093 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42ef6b50-fccb-34eb-b618-6d01935954a8 | -3.47187 | -50.26735 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b51e62b-4243-3859-b04d-0e7392c3c7f8 | -3.19629 | -46.36979 | 2024-12-02 04:48:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 334bff00-631f-3c2f-a6ff-6297fb52737d | -3.88818 | -49.93167 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a4b2223-4bbe-3094-8ac5-23e20cc2a38c | -2.35922 | -53.79056 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb5483bb-b2c1-3237-8f71-b70ee6a2e4ee | -2.78779 | -51.90458 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58e20060-d29c-3075-a736-ef1e1caccaf2 | -2.92351 | -48.01806 | 2024-12-02 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b803b0c5-c252-34d8-a27f-33e798f8c996 | -1.49658 | -51.94867 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72fa6b49-6693-3ca7-8ffb-bfb98d69482f | -1.72725 | -52.6416 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 53552c6e-e034-3295-a5ef-8d323253bcf2 | -1.07389 | -53.23134 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8394a615-9acf-33b6-a114-3c79f23196ff | -3.27815 | -48.78031 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61a04d3d-6362-35bd-9abc-840ef8c2e8ae | 0.88908 | -50.95889 | 2024-12-02 04:48:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3f6a2fba-de21-3a3d-a19b-bff248ec680c | -1.60322 | -52.50025 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1212aa0-fb90-3b72-ae31-6d0a7f08f8f2 | -2.86071 | -53.98706 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| defeb15e-f5c8-363c-bdae-2f529795d051 | -3.43456 | -54.60796 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 10233f90-791f-31b6-b81f-84f2d1c06453 | -3.6629 | -50.43619 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fb4a06f-1485-3492-be7b-24f6bb36ae30 | -2.90336 | -51.5807 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 940fc407-f646-3fdb-8d56-df91688b42d5 | -3.53517 | -50.17305 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6d14cff-0cde-3fb3-a30e-32a754d889c4 | -2.34479 | -54.58232 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28985280-9844-340b-b745-ac9e5325ba78 | -1.45057 | -54.52161 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1ae0b80-b358-3760-9e0d-ce8ed34cd7db | -1.45675 | -54.96093 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bd66757d-9869-3bca-abe5-9cf53ef6366d | -3.11288 | -54.01369 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 505ce5fa-8559-3f1a-95b0-c95b449ca763 | 0.91156 | -59.45041 | 2024-12-02 04:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a0cd5f79-0dea-3576-bccb-70b72d1c7399 | -2.43881 | -53.88436 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c8aa818-bc97-3814-affe-467bca22d02c | -3.49895 | -53.83475 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80b073a2-e0df-3316-bd76-ab364fdc806c | -3.27486 | -46.45318 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| f5430d9d-27c6-3576-a00c-248d7e4296b9 | -3.65581 | -49.91633 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 437ef63b-15e8-315e-8f33-8efa572cd10a | -3.36123 | -53.53461 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 728c30ce-28f3-3c22-a33f-197781d67b33 | -2.91865 | -53.07439 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1206d84c-dbde-39d0-8a44-3d2408bc3c99 | -2.32269 | -50.64735 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86d375a2-b791-3f52-81a5-0baf838ddf14 | -3.25801 | -54.10986 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3db765a7-775a-3eb0-a856-0edbc8d877b8 | -2.60858 | -54.08238 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8eb3149-9ffb-3628-b4be-3eacb88296b7 | -2.54243 | -53.4119 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163d99b7-f7fb-35f3-9deb-f221ba3a0e7b | -4.65765 | -45.65097 | 2024-12-02 04:48:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fe6b5ac-4ed8-3bc4-863f-d50a160de267 | -1.69098 | -52.63231 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f84d0b53-061a-33cd-8a94-75749eaa1fd5 | -2.39319 | -53.88929 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33737863-9e04-3ea5-9a54-245ed7aec1ee | -3.50698 | -53.82839 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f5fb7fb-6ff9-3d82-8a37-a1043735e27a | -3.40236 | -50.2381 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621a8efa-ebfa-3c33-bbe6-710de579f22e | -3.06468 | -53.67704 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01492219-e47e-32b9-8b3b-e1f2b5d47a4f | -2.86567 | -51.25805 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cb395a1-befd-36c9-8bcc-a162ba256299 | -3.25622 | -53.64156 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe511926-fffb-37e5-9aad-fd49e58c9676 | -1.00425 | -51.73006 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b95073c6-8a75-3552-a8ef-d3b65f6ccb41 | -2.32995 | -50.66638 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78a7db17-e14a-3e0b-bef6-8ae54447743d | -3.25574 | -53.6227 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 778c7e41-b2fe-356d-a8c4-1d1415a74c4d | -3.4742 | -52.24827 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74e69e78-96a0-3750-82d0-397c1aa10a40 | -2.26803 | -53.61537 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0211c3f3-aff0-3674-80de-e1d1bc48b69d | -3.11771 | -53.98334 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6efa5c9-0d0a-3372-aa31-13118b01fb02 | -2.33219 | -50.67388 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f4c643e-de5d-3e4f-9bd6-455585449c1d | -3.50291 | -50.22385 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14055433-ca25-3148-b0e3-0df05e2f66e7 | -3.831 | -46.54647 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb5ebd39-7e44-385d-a888-d3886c36bfb5 | -1.52602 | -52.77078 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b325b45-b84d-31b5-9269-a0c5fe88dceb | -3.30933 | -50.50294 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07868be0-0ca3-339f-8592-7dcda43d1611 | -3.74766 | -54.50887 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e45fe46-718b-363f-b52c-d9fef50e0575 | -3.02582 | -51.53675 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8702f566-546c-392b-a5b3-f60bf8b39b3b | -3.84525 | -52.0285 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7462a4e-cf0d-3514-8837-a5eb03357109 | -2.40838 | -53.86045 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 047406fc-1385-3d53-8a6a-e3a806a55eab | -2.45749 | -53.68267 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30fc3394-60c3-3c0c-bd32-a8d0441bb34b | -2.37618 | -53.6624 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 977fe721-455c-3972-9419-38ab71d865ea | -3.09869 | -53.74976 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 026aed66-7836-329f-bf58-48823398f950 | -2.56059 | -53.40728 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b33cfd9f-54d3-38d7-91f4-78eeede22fe5 | -3.23541 | -50.65497 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54c72410-a672-31d1-af82-83b07969ab51 | -5.12222 | -43.21609 | 2024-12-02 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6e7d3a2-78f3-3cb2-a2ba-71f646fb1b0b | -2.26073 | -51.23751 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5015994b-6212-3900-ba10-d416a6961754 | -3.79546 | -46.69935 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d193fb93-05a8-3318-84f6-aae0091d11b8 | -2.36026 | -53.80622 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b394362e-2790-3fb4-80bc-205d82e8a81e | -2.88886 | -54.01099 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README48.md)
