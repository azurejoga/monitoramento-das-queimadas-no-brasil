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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c63f043a-19ac-34a7-92bf-967dd883bc47 | -15.70684 | -56.12368 | 2026-05-24 04:49:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7e50ee5-1021-3228-b59f-eaefcf2bd3a3 | -15.70809 | -56.12617 | 2026-05-24 04:49:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f81ac8f-d165-3af3-bd84-21f519b5efcd | -10.45501 | -46.25396 | 2026-05-24 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f1da90f-2c07-3135-b242-ab4df4cc67a1 | -15.0869 | -57.63023 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 448f96af-6f95-3980-a6ce-ffaac40f49e0 | -11.17435 | -55.91687 | 2026-05-24 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3ca0056-1dd9-3e75-b2af-b5dde6e60173 | -15.08616 | -57.63428 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c9dbd4d-84dc-3862-88b6-72fc75cf84e3 | -14.01592 | -53.36301 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 042ac884-a3fc-3d8c-91f6-f326f3df37a4 | -11.92727 | -43.86404 | 2026-05-24 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cec2d55b-de62-3706-a740-b5ed3d8cea69 | -12.55234 | -57.17947 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70dbbd96-fbde-3395-95d8-aeb2daa75cd6 | -11.54836 | -56.95028 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65f61951-3c62-37c2-a29e-eacf1a98512e | -12.54093 | -54.60914 | 2026-05-24 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f0112e9-64da-3e52-9261-2520912d9cab | -15.09612 | -57.62786 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f87d881-039a-3fb7-9325-74b80f1fc24f | -12.89212 | -58.17614 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6a4d4a0-3185-39b2-97c9-b2b092636bcf | -11.44485 | -54.09298 | 2026-05-24 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d47b8e66-fe47-37da-a7da-533ea0edbfe1 | -15.10037 | -57.6287 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba44ffbf-c25e-3d9e-af70-ccd2e38eeae1 | -11.06464 | -46.84068 | 2026-05-24 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6112ff6a-022a-3465-8bcf-2f893adbc3a9 | -12.55459 | -57.16704 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b603b1b-9c84-3b6d-b601-7af7975ab936 | -15.70426 | -56.12543 | 2026-05-24 04:49:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 704ad983-9607-311f-869f-814be0ecd3ee | -12.54016 | -54.61354 | 2026-05-24 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96adc408-bc96-37e7-b42e-881211e35233 | -14.70766 | -48.3371 | 2026-05-24 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab1e3bad-64de-386c-a0dd-cb90f1ee6030 | -11.27506 | -53.97043 | 2026-05-24 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1899b0da-0467-3e0d-9137-c61572a4af02 | -11.5466 | -56.95504 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca02d24d-aa2b-37fd-be2b-ce64b5555934 | -14.77331 | -52.68175 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e69aed2-194b-3859-a549-3fd2bd1bf8a9 | -10.03635 | -51.67511 | 2026-05-24 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c00ddb91-8a44-3ae7-910b-cfe56cb3b1ac | -11.27578 | -53.96615 | 2026-05-24 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30b318f0-48aa-3a1c-a14d-7efe61ec0e68 | -3.96028 | -43.12523 | 2026-05-24 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ccd827e-5813-3342-9fb8-3062221fa8b3 | -11.17373 | -55.92046 | 2026-05-24 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b467174d-6c62-37e4-84d7-9d7783609d2d | -14.01437 | -53.35094 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31d83aaf-6158-3c6d-b4a9-766fb2682c1a | -14.01999 | -53.3598 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7571ff17-a27d-3af1-a5bb-b7d87d1c1828 | -15.09114 | -57.63107 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94bd7121-c9e3-3023-8280-bcfdd4356ca8 | -12.89222 | -58.20103 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3b4e732-1a4e-3dd9-8e1c-0d9492a582ea | -12.04319 | -47.33729 | 2026-05-24 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ff8332c-8539-3f72-95c7-d52d29cb4636 | -11.05022 | -49.59974 | 2026-05-24 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a35d9182-1f28-39fd-8366-99275dc4f986 | -10.65234 | -49.7321 | 2026-05-24 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a4a301a-f45d-31ba-ad4e-68b059a56077 | -14.32442 | -49.84061 | 2026-05-24 04:49:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c80c5408-dbc1-38c4-b4a3-7d24b5f4d7e5 | -11.438 | -52.93019 | 2026-05-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8383e70-ac6a-34d3-8bff-736503844b45 | -11.18717 | -55.91541 | 2026-05-24 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e14d183-23ba-32ed-a259-4f8215931a25 | -12.87938 | -58.19359 | 2026-05-24 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b08e447-b36b-3fa2-9902-e44b2c28e420 | -11.60749 | -55.33672 | 2026-05-24 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62436c10-e539-37d6-8d75-5b1a860e9bc7 | -11.94649 | -49.30091 | 2026-05-24 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 336e6819-adab-386c-b358-d12c75f5256f | -3.95536 | -43.12863 | 2026-05-24 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86ca4730-9c8d-38a2-8472-3444c256eb7d | -16.4339 | -51.77821 | 2026-05-24 04:49:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3a7367b-d75b-3d69-b06a-8943cc4f3f6e | -12.54525 | -57.16948 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b72f22ef-127c-3960-8891-9408aedd3b07 | -14.76994 | -52.68116 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd4926d4-db1d-3f7c-8122-293aee1e72fb | -14.0183 | -53.36277 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40dafc17-2ceb-3ac1-811a-8d6b4e5a6680 | -15.1011 | -57.62465 | 2026-05-24 04:49:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d24cf1f-72dd-3a25-b975-ffc68c930120 | -11.54734 | -56.95087 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ab77167-14cf-367c-9dcc-9821147d57d5 | -14.7739 | -52.67809 | 2026-05-24 04:49:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d1f1a52-3e03-3458-b8a7-eee44558dd51 | -11.79072 | -57.3541 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4798bd60-d94f-3e7d-8394-af893f0d9696 | -11.54955 | -56.93833 | 2026-05-24 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d782ef0-3348-366d-b779-9f41dea1f842 | -18.65144 | -48.87347 | 2026-05-24 04:51:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a255a5ff-662a-39dc-bab7-534ddf9e275e | -22.57911 | -44.08322 | 2026-05-24 04:51:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d2c7a06-d33e-374d-9113-f6cae2b2620d | -16.86982 | -52.44104 | 2026-05-24 04:51:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ee70083-056a-3d79-8150-9962ba61232e | -22.58429 | -44.08281 | 2026-05-24 04:51:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1de7b303-8dc7-33e7-ae52-ea7cf3f03605 | -18.65514 | -48.87403 | 2026-05-24 04:51:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 666ead76-3b25-3cd3-aacb-1b04e0551b1a | -19.68848 | -54.35427 | 2026-05-24 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a66bec6a-cc03-394e-af89-3a81af28aebb | -22.57904 | -44.08219 | 2026-05-24 04:51:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b89e4a8-90d1-39a2-9c71-75fd4f2fd017 | -19.69188 | -54.35493 | 2026-05-24 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bde444f9-ff4c-32a9-b770-97065c98c59e | -19.97766 | -44.85629 | 2026-05-24 04:51:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711d789f-2056-35c7-9882-d83325f69ef0 | -20.91863 | -46.78827 | 2026-05-24 04:51:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cbec7dd2-d2e1-3a0f-b593-95d4cd728b22 | -20.9143 | -46.78785 | 2026-05-24 04:51:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2795ea38-a6a3-39c8-b115-227ec477a1e4 | -3.95917 | -43.12344 | 2026-05-24 05:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83eeaf1b-ae95-31c9-834e-cd19bdfcbeeb | -6.082 | -44.00684 | 2026-05-24 05:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f9486d38-d763-3a90-aa67-35a64170ee56 | -6.85117 | -48.73263 | 2026-05-24 05:06:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bae19ffd-0e3e-3652-a802-c4d3c6f03a29 | -4.42875 | -47.73014 | 2026-05-24 05:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27ff8d6a-a4b2-301c-9322-1d5f72feb87b | -6.85581 | -48.73329 | 2026-05-24 05:06:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c762ed-c2dd-3946-b18e-4cefaf1dc3b8 | -3.9584 | -43.12872 | 2026-05-24 05:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a4708943-b2d6-3eed-8942-73f842eb25c8 | -12.8912 | -58.17237 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c6718fec-ae71-3356-a8a8-e33e7d56d4b2 | -12.49655 | -57.64987 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e54149d-373c-30ff-97f2-4e4263a2f4b0 | -11.17724 | -55.91807 | 2026-05-24 05:08:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2d7aa708-4011-3607-b3e6-5c95bdc5712e | -11.29793 | -56.31783 | 2026-05-24 05:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad262bad-7dc8-31d4-8f40-641ff6f37550 | -11.54603 | -56.94149 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adf1e436-154b-369c-b419-4c507ef606ff | -11.90859 | -57.03276 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83218da6-9349-30c6-a704-956f7ac9c6a0 | -12.87854 | -58.19229 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d83f5cbd-0010-3a84-8822-869bcff9dae7 | -11.17391 | -55.91753 | 2026-05-24 05:08:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 01d3f531-f817-3b3a-a77c-292c116571f2 | -11.73129 | -54.79852 | 2026-05-24 05:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d96ab0d2-3ee2-325c-863a-0e6523cc8e07 | -11.60805 | -55.33676 | 2026-05-24 05:08:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bdb6fed-0686-34e7-9b85-248843c9ac5e | -11.5576 | -56.95418 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 398a50bb-1f37-326a-861e-39829478f1e0 | -11.94777 | -57.04276 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19d89679-9d30-363b-83ec-28857c07dcd9 | -11.40209 | -57.54588 | 2026-05-24 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96c28ebb-47a1-3d58-b321-d0910c30e070 | -12.55302 | -57.16695 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3404047b-d9a3-36d0-89e4-27cf81fd6576 | -12.54971 | -57.16641 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d1cef3-ca45-317c-adf9-3ef8645f3c81 | -12.89395 | -58.17653 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 900894af-c6e1-33b3-8180-7c0f7741bce1 | -12.89044 | -58.19808 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 017695ff-f57d-336a-b266-db0520946def | -11.95108 | -57.04329 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce705215-e71c-3678-aac0-1815fb60e883 | -11.5438 | -56.95553 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5f3fc07-e703-327f-9b5e-54c31718bded | -12.55246 | -57.17048 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02fcd205-ac76-3058-ac45-520fe49122c8 | -11.54272 | -56.94096 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe2d768b-9cdf-3f1d-b25f-64438f19a403 | -11.27749 | -53.96495 | 2026-05-24 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ac58f53-0310-3e4e-a3d8-23fd58e485f7 | -8.8642 | -46.93803 | 2026-05-24 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90b262b4-f0ca-346d-82f3-d613d4853d09 | -11.54989 | -56.93852 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78fc63e6-18ee-32d4-906d-2fb4af01d4cb | -12.88786 | -58.17181 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 29031b3c-b8c6-3f19-8ca0-9994ea959069 | -12.89061 | -58.17596 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74ee780d-7658-3818-8c70-f412ab180aa6 | -10.45181 | -46.25246 | 2026-05-24 05:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e6ae856-6ea0-3516-840d-c0310ba52974 | -11.54658 | -56.93798 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e92fc26e-4db9-36f5-9b7e-4de9bc031de3 | -12.53754 | -57.17887 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0183743-a4bd-31c9-a8e6-789a65d98057 | -12.54695 | -57.16234 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d2f280d-71c1-313e-8d09-7553d2dd5fb3 | -8.70572 | -47.91571 | 2026-05-24 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97efb5ad-c0f0-3982-9c8b-28b51afee5e5 | -11.54049 | -56.95499 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ad8de10-2dba-33e2-87b9-5d52071a8a14 | -12.89728 | -58.17709 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
