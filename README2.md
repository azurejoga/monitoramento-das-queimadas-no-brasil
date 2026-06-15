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
| 94fa1aa2-d543-3354-9248-a57bc975b3b2 | -10.77472 | -54.10749 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9356cc9-302b-33d1-9fa2-7bbd0aa18376 | -13.25996 | -43.45331 | 2026-06-15 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed99cb01-095c-3da0-aa13-efa3efcad214 | -12.44886 | -44.74991 | 2026-06-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19344e9e-4605-3161-8f43-c48d3d48a240 | -13.54463 | -47.84952 | 2026-06-15 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27f085c6-1613-3205-b8f4-1fc24d8e3a09 | -10.83089 | -53.72747 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28d2d8e8-16d3-3941-a3f4-faf8b389d700 | -12.71255 | -54.20326 | 2026-06-15 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec906c07-a422-3820-80d3-7d7b4d190368 | -10.8375 | -53.72884 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30b2d232-f4e7-3b09-872b-62388688f752 | -13.23027 | -41.97273 | 2026-06-15 04:04:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| daacc496-ae49-3132-9b9b-b588554c4dc7 | -13.81411 | -43.65588 | 2026-06-15 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea1323cd-e11d-3812-a1da-22018379afdf | -13.50766 | -47.84921 | 2026-06-15 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c077cf07-e457-3c88-b4e2-41abf298b8de | -13.54339 | -47.85048 | 2026-06-15 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af7239ad-ad7e-369a-b6fb-9787634a8789 | -13.54389 | -47.85347 | 2026-06-15 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aa655fe-6f6a-3f22-bd72-fb6c1e4187c7 | -10.80488 | -54.17432 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1e5d9bb-f373-32a3-a74e-ec40620cc168 | -14.37024 | -45.54389 | 2026-06-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbae2aaa-b2ee-3a49-b905-250175f7cca5 | -10.80391 | -54.17267 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47c01132-86be-3d1a-8b3d-c9453bd68612 | -10.83513 | -53.74055 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c339cfb7-da62-3f88-bb03-bb0a21c9126e | -10.80266 | -54.1789 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b69a4a56-9923-3a94-815b-4568d0ab46c4 | -11.06682 | -52.45596 | 2026-06-15 04:04:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b56853be-a4ae-3a8a-9ae5-0ea87db944df | -11.26587 | -53.95963 | 2026-06-15 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ea96836-3d8c-3416-a58d-b2f8ef0c3219 | -15.86866 | -41.96742 | 2026-06-15 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b409fab4-0947-3bb2-adaa-74d1ef8f4f39 | -12.73252 | -46.29057 | 2026-06-15 04:04:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 558770e8-c264-3498-9023-c3d0b96be4c6 | -11.827 | -51.6199 | 2026-06-15 04:04:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ada15334-7f97-3a96-b6ca-929950af154d | -12.71916 | -54.20452 | 2026-06-15 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f052d665-8a45-316a-9a6d-65a26d8cef30 | -21.60242 | -42.99749 | 2026-06-15 04:06:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 214df740-c711-3654-957d-99f4683c846b | -22.58281 | -44.0811 | 2026-06-15 04:06:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 44f300c8-5c55-3e9b-97f5-98500741e879 | -3.5836 | -50.26222 | 2026-06-15 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c8ac8a-7bdf-323f-bab7-2aaf4969c01c | -6.90149 | -51.16414 | 2026-06-15 04:36:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe447d9-c428-3854-ae10-81a0bf4574ca | -6.16515 | -48.49585 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af4c4899-ae62-394c-92d0-d70d59bbb589 | -6.12185 | -48.50031 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3596510-36c2-3660-b40c-bb72b385423d | -5.9371 | -43.651 | 2026-06-15 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b909116a-b4b4-35d6-8193-953db72f49ac | -8.6848 | -47.83619 | 2026-06-15 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 878fa6b5-e0f5-3fa4-8523-24663690b891 | -3.50339 | -48.03951 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 164a36e2-e07e-3e58-9897-2c016860d235 | -6.72642 | -44.3764 | 2026-06-15 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02edb300-d449-353e-b05a-27fe84fd4a37 | -8.38339 | -46.49838 | 2026-06-15 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dcaaf2e-a9a6-3c97-8ed3-06620d1aedc0 | -5.93588 | -43.65899 | 2026-06-15 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cdd4717-17ae-3516-88cc-dc1010be315d | -7.31806 | -48.88013 | 2026-06-15 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0934744-4240-3045-94fc-d9cc7224635a | -8.14029 | -47.55593 | 2026-06-15 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41dfad3d-27ad-3783-ae7c-23ea55ef2a87 | -6.11814 | -48.48817 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c90cb294-48db-3b55-bee2-13f2cffdc62c | -6.11179 | -48.48357 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f47552c-32bf-3e28-9847-fd14e51a8fdb | -6.15905 | -48.46803 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53ba57f9-aabd-33e1-9627-3333e748fc76 | -8.39101 | -47.4705 | 2026-06-15 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1be21198-0009-3f8a-891b-98b4cdeb6143 | -8.18733 | -46.75377 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72129fd4-5631-3d3e-bb19-411601ed3a06 | -6.1721 | -48.49674 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77dbcfd2-0833-35d6-97f4-abb95bee496f | -6.16252 | -48.46849 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1219d276-2f03-325f-ac36-cf9d0f329429 | -5.93883 | -43.66349 | 2026-06-15 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efbe7c2c-0e0d-3eda-a9f2-3ae173f6a68b | -7.31868 | -48.87632 | 2026-06-15 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 846e18ff-21cf-3d51-be1d-f1c49eda72c1 | -3.51505 | -48.03351 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61c38258-52af-319d-93e3-476e487418b9 | -6.15843 | -48.47179 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51dd2af-a15e-3405-80fb-f755316d583d | -6.16231 | -48.49152 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9fc928c-5ba5-3fe9-b821-029b68d49320 | -6.72584 | -44.38015 | 2026-06-15 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8286742d-17d0-39b5-a1d3-c73db1917af4 | -5.93649 | -43.65501 | 2026-06-15 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d0d82a4c-d714-3ce1-b94b-370c77d7e534 | -5.54478 | -47.57777 | 2026-06-15 04:36:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf7a0761-9368-32c2-a116-a6a2959692a2 | -6.15947 | -48.48722 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6e66d3-4839-36aa-9fc0-1796a0344657 | -7.91643 | -48.25136 | 2026-06-15 04:36:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 562d3b57-a139-3e20-a1fa-058b83e5ec57 | -5.29216 | -43.95764 | 2026-06-15 04:36:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 335be4c0-f0cf-324f-9463-bef24bfc8853 | -8.14419 | -47.55295 | 2026-06-15 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 465a3d6e-2e82-33a0-a95a-1e4ca3114e26 | -3.51158 | -48.03297 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 136bc18b-7fb3-33f9-911b-ea9c43d5a174 | -6.12025 | -48.48847 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3507f95b-2778-3293-90dc-afe7db531058 | -8.74609 | -47.49568 | 2026-06-15 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d076adbc-37f9-3fbb-8dbb-b06d7dfae54a | -6.36477 | -46.15423 | 2026-06-15 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69517bb5-223d-3b9d-981d-9ef32b1ffb7a | -6.15885 | -48.49102 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c99de61f-5224-39a7-b660-236aa35d94e8 | -7.91982 | -48.25191 | 2026-06-15 04:36:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fb6b3fe-4709-378e-b1a1-0646ba49c6ba | -7.11096 | -41.16913 | 2026-06-15 04:36:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41366f14-ff03-302a-8356-c3e7779d93bc | -7.32277 | -48.87308 | 2026-06-15 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da60eadf-9f0e-30c3-8c25-c1555da2b74c | -7.31521 | -48.87574 | 2026-06-15 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6c2622b-c9c8-3d31-a6b8-ec8ca82e8717 | -3.50749 | -48.03622 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5dcabb3-8ca4-3fb5-8988-26f0617ff64c | -6.11839 | -48.49981 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82901a35-57a1-3596-8f8d-bec46bd54e95 | -2.90564 | -49.64427 | 2026-06-15 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be1efc01-2a1b-347f-a1c6-1a3a1466f41f | -6.72237 | -44.37962 | 2026-06-15 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55a9793d-4ebb-3c1d-badb-42b493ceeba5 | -3.51097 | -48.03675 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 998cf4ae-8bfb-3a0d-a31f-efec494eb3c4 | -6.11979 | -48.49998 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4559e6-7289-30e7-a9fb-4e8a638bab88 | -6.16578 | -48.49198 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d157c044-425f-33cd-a011-7a51387226a9 | -8.19065 | -46.7543 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dca2e84d-97e7-3a2b-9ff4-c026f4b59ca8 | -8.19675 | -46.75885 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cf25245-bdee-358e-ab42-91ef7615ed7d | -7.11514 | -41.16973 | 2026-06-15 04:36:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 816f556e-3660-3363-9366-2405712615aa | -7.31901 | -46.96158 | 2026-06-15 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7dc35592-2478-3a6d-966d-dd042e8914ae | -8.11044 | -46.77024 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cac3b3db-fd76-3088-a63c-76ee2a6272a5 | -8.19343 | -46.75831 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaf82649-3b09-34d5-b776-a8544f56946c | -8.13695 | -47.5554 | 2026-06-15 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cd788e9-267d-369d-82cf-6c8d7d15676e | -3.49643 | -48.03844 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b14f3c81-618e-35a0-9d45-99cc1c53622b | -8.1026 | -46.0694 | 2026-06-15 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30f507b9-856c-34d4-9872-e64188ddee1a | -8.08043 | -47.19076 | 2026-06-15 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99311b45-7d05-3615-b50f-4280e9170bdd | -8.09925 | -46.06887 | 2026-06-15 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6fdd1a6-adcc-3f45-b1c2-bc8826df1f87 | -8.31201 | -47.11734 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0abc9183-160c-31b0-ac61-904e58a8d4d1 | -3.5081 | -48.03244 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f5630c6-6fd1-361d-83ba-14739b5f2d0d | -7.32215 | -48.87688 | 2026-06-15 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2ec502a-3a3b-3ae1-9a14-ec6991fe422d | -5.28867 | -43.9571 | 2026-06-15 04:36:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0aac13c-5b9a-32eb-a3cf-69739a34dde6 | -6.15782 | -48.47556 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd6d9c1-e15f-357d-9154-ad3310892e4c | -3.50401 | -48.03569 | 2026-06-15 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f982be-d03c-3655-b845-492949b38e01 | -6.16007 | -48.48352 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a07145-1d29-381b-b443-17fb453a1071 | -8.31256 | -47.11385 | 2026-06-15 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5af0c63c-8d6d-38b9-80c1-5f4310904bc5 | -6.17148 | -48.50057 | 2026-06-15 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd67b3ec-535d-30f7-89b0-f760f486a56b | -3.20142 | -49.04728 | 2026-06-15 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7eee552-ecb3-3c09-8079-4927641b2072 | -6.59105 | -51.69359 | 2026-06-15 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6282edc-69fc-341c-b31c-076bbc8a5489 | -8.38394 | -46.49488 | 2026-06-15 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 457f10aa-fc55-3d09-a735-755aa4fda533 | -7.789 | -48.19446 | 2026-06-15 04:36:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe9b7b1-cd5f-3cd3-b0ab-e7cd13bf9ba7 | -7.31459 | -48.87956 | 2026-06-15 04:36:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f911d94f-4462-346a-b0ed-7152a4483600 | -11.51027 | -56.12661 | 2026-06-15 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f5b0b2e-abc8-3ad7-be54-2962b0bd581a | -11.71872 | -54.49544 | 2026-06-15 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8bd99fa-41b6-3574-aab9-bef52243db9e | -13.22718 | -41.97017 | 2026-06-15 04:38:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README3.md)
