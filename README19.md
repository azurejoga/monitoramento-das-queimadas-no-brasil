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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6beba4ea-bc35-3ffa-9353-ab5313facab6 | -10.94542 | -55.31614 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826fccf9-cd57-363c-aaec-cb1e1292ca8f | -9.83574 | -62.888 | 2025-06-12 04:51:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97149c2f-3b03-3f25-bef8-c5c5d51dd9fb | -10.66187 | -49.36222 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 481fecea-0050-38ca-ad55-390be07deeb0 | -11.37833 | -55.10909 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d729a5-f03f-327b-8f0c-f73461bb43f7 | -9.65695 | -56.11106 | 2025-06-12 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5db13e3f-3875-3451-ba54-37957eeeee5c | -14.42257 | -47.89703 | 2025-06-12 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a76b0b3f-5f48-34a7-8bfa-8e256e889109 | -13.5209 | -56.57807 | 2025-06-12 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5221e153-24c8-34fd-b142-a5e6c730b381 | -10.86332 | -54.31557 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8294da98-aa66-3271-a82c-3efaeffaddd7 | -12.05594 | -48.07391 | 2025-06-12 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d9a8988-df4d-3c59-91e2-4b439896bc56 | -9.24735 | -57.53391 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 35c8d3c7-8196-373d-98bb-562a79b3f94c | -11.32926 | -45.45345 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8179ce90-1bbf-3a17-a156-0d81a027ff23 | -11.85532 | -62.76854 | 2025-06-12 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71c490ff-6cfc-3872-8e43-ca82546ae0a4 | -10.88485 | -54.75354 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e568f837-0dad-36db-9b05-e262be7ec4c8 | -13.0895 | -52.28854 | 2025-06-12 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6da5ef3-48ab-3f46-b0d4-dab0db068454 | -10.86566 | -54.31947 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c7ee8d4-c70b-34b2-919b-661bf3d8daf2 | -17.28728 | -42.66584 | 2025-06-12 04:51:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0def60dc-4e72-39da-977d-0d03aa72db99 | -13.88965 | -54.63928 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 314c1520-0f64-3f8d-897b-97a9b3a2ccf0 | -15.37403 | -47.88233 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50ff1872-4b6b-3780-832e-b4323da8bf9b | -12.22412 | -55.52285 | 2025-06-12 04:51:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41fe635c-9512-323b-80a8-933601fd0273 | -12.21014 | -49.63475 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 82c9d2df-279a-3e9b-aa68-1113b72aa138 | -13.89296 | -54.63984 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f65a464-ba4e-3372-93a3-f93e0149fb26 | -12.04106 | -54.68346 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3efecca-fb26-3c36-9e6b-69432543c918 | -13.28633 | -57.0698 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96a28064-783c-3288-b1a6-4bdae4c3ae7e | -10.70105 | -49.52173 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d6b89c7-d4e8-380f-8529-a8189e7081d3 | -13.89732 | -54.65512 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d88119be-5cfa-30c4-ab0d-8d9aa9d8b528 | -15.17595 | -43.06948 | 2025-06-12 04:51:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edf7dc14-a3b0-3657-8fa9-b8c7ceb192b6 | -11.91835 | -57.47836 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb76e136-db3d-30f7-9938-1fff0ab7b3a1 | -10.88092 | -54.75658 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5288937c-e961-361d-8101-832d6b91ad39 | -10.65314 | -49.42375 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f2c22e14-ac79-3402-9c54-625f5af1f73e | -10.3661 | -57.23551 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d5c7097-e169-3a61-ab4a-0ff60711e10f | -12.71008 | -58.02762 | 2025-06-12 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9cf7a591-82d1-3ab8-bcbb-9591081711df | -10.33535 | -57.48956 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2ce6fd7-f16a-3395-aefe-1ae730f88326 | -14.03572 | -55.12766 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8ccc97b-a957-3e68-9139-c62c1cc46af4 | -13.90015 | -48.7385 | 2025-06-12 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8682c845-55e5-30f9-8686-a3d309e82248 | -10.87596 | -54.7447 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6f44b39-02cc-3851-9c88-8acfe59376cf | -11.87043 | -52.2513 | 2025-06-12 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f352c2bb-6c31-34e8-a1ce-10f678555086 | -12.26011 | -57.61198 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 299cf875-62cc-344b-8f64-0cf0d00a1340 | -13.89239 | -54.64338 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1711ac3f-9a85-30ac-a3ab-9b70dde6b6cc | -12.46916 | -58.47055 | 2025-06-12 04:51:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e7662c3-d92b-3e40-a834-ea6cb7656372 | -15.37459 | -47.878 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41399319-b8b7-3e8a-8c40-62a524947e14 | -12.70553 | -58.03157 | 2025-06-12 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 31f78de8-0e6c-3b7a-b870-7af133e71d05 | -11.77897 | -47.4032 | 2025-06-12 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a2090d-c129-3774-a338-9cea2941abbf | -13.89597 | -48.73816 | 2025-06-12 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38da7a3e-af7e-3fb2-aa59-171b0aade917 | -12.20768 | -49.62463 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7979ee99-5c80-38b2-9d8f-97be64b82178 | -11.06614 | -55.04291 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba731df-462d-3bc4-a245-a2bd73f0d9d5 | -13.71744 | -58.67641 | 2025-06-12 04:51:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be30027-35ed-3f22-b25a-a7cbf5c94ab4 | -14.6555 | -48.06917 | 2025-06-12 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b70c91c1-1b5b-3dfe-a713-fd014501723e | -11.90924 | -54.42513 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19d1495d-35b8-3d7c-b42c-90273f599b3a | -11.99331 | -57.21338 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 793df506-205a-38c8-a8bb-42710db39c88 | -14.82729 | -54.65971 | 2025-06-12 04:51:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb415b8b-367c-3e8a-9cc9-888534fe25f4 | -12.23289 | -44.16133 | 2025-06-12 04:51:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fbe6134-c406-3d9a-8c78-e14dcc3c66a6 | -11.84183 | -57.85735 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88045231-6364-33d4-9d8d-2c967477b28a | -11.79188 | -54.77384 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2334050e-08af-3134-b64e-4cf39f50010b | -13.89401 | -54.65457 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2544d893-19ca-301b-a1f0-7f79fc4e178e | -11.13995 | -53.9425 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3d844ef-6982-3fde-b154-68f043b16afb | -12.82636 | -47.37687 | 2025-06-12 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eb2d35b-1d54-3198-9a0d-0128a59d34d1 | -13.71495 | -57.48008 | 2025-06-12 04:51:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f4ea9aa-1172-36eb-ae50-63e0d73edf83 | -12.76899 | -44.40391 | 2025-06-12 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 367c25a9-4a12-3d83-851e-623cfd206b44 | -13.9012 | -54.65212 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c4de4286-95bb-38bd-a958-d988df58d857 | -10.7448 | -58.0021 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 303422d0-b830-3a8c-8541-99b8da3c2ca4 | -13.52764 | -47.86082 | 2025-06-12 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00757032-df93-3105-8adb-c42e5e11730e | -11.77723 | -54.3784 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8e380f6-5a08-300f-a963-aa0c426ed20f | -12.37852 | -45.77268 | 2025-06-12 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e1a8702-79b1-399f-abb8-1f5681fa4cdc | -14.03399 | -55.1384 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab84358-692c-33fb-9a75-63adc28da82a | -15.38114 | -47.88146 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2d67272-2fd3-3b2c-a3d6-7510b5110ac6 | -13.89225 | -48.73429 | 2025-06-12 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6b83292-df1d-3b66-b92f-688eaca97baf | -12.11132 | -48.87322 | 2025-06-12 04:51:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ecd4f35-1d87-35ae-885b-80af38522244 | -10.23481 | -52.23479 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 810a0c58-17d4-3c6f-90cc-105920532a72 | -13.4927 | -53.49112 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac2e56b5-34f4-3dab-8284-052642e8f9df | -10.11415 | -58.22548 | 2025-06-12 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 816da9d0-4de9-3591-bed3-11f86a18dd72 | -12.82127 | -47.38084 | 2025-06-12 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12639219-ad0e-3378-96b1-1db56872910f | -13.89458 | -54.65102 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0435228a-1777-3136-b4d7-28b3efb787b0 | -11.33855 | -45.22038 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf07fd63-93fc-378d-b665-eb2c51d61fab | -12.51929 | -57.23215 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f10bc15f-06f0-3e28-8587-67f6e178f71b | -12.13601 | -54.66256 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57d44656-9110-300d-bb3f-dcdd60e42c44 | -17.10604 | -50.07175 | 2025-06-12 04:51:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a2aa87-a6c9-3f4a-ae69-44e1bf7d4840 | -13.28987 | -57.07045 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8407e6f9-aa5f-3e31-a11b-ad073048a126 | -9.25243 | -57.53836 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 77cab816-c48e-3747-a636-ef61f6aeec3e | -12.51497 | -57.23577 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2a4ef46-20df-3bea-b451-c267684948cd | -13.29057 | -57.06636 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5ca70c3-4692-3b89-82f9-c5148ede53d2 | -13.71648 | -57.47918 | 2025-06-12 04:51:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e4ba80-bd92-3665-b90e-6d6c83d8d664 | -11.37774 | -55.11272 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 762e82d3-ef80-3018-b72c-21ed870e99f0 | -12.83085 | -47.37745 | 2025-06-12 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b1d9f25-fd55-3657-863c-80d8860b90f5 | -11.13666 | -53.92039 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07aa67e8-2d52-3ab1-a967-01b2a322ed53 | -9.24858 | -57.53775 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 78100993-da2d-3274-8e3e-de56ae728a11 | -11.57308 | -47.43626 | 2025-06-12 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2631cf2d-0c77-393b-a22f-ec3c1f99a1dd | -12.13933 | -54.66312 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca55141e-2160-3226-81a8-0c3a9e494c10 | -11.8098 | -56.9661 | 2025-06-12 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed8a2256-5924-35d5-9493-24ff4c185c7d | -14.0324 | -55.12709 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a2f051-c0e8-3d47-9730-39d03476759a | -10.60501 | -52.82851 | 2025-06-12 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f3575a6-f33b-39e3-ac02-33c0b6523ac2 | -10.75749 | -54.78435 | 2025-06-12 04:51:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b55d6c0f-b17c-3a67-a3fa-9886860e48e2 | -10.6993 | -49.50716 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1809ad0-bb1f-3b77-b331-ca75f67464f3 | -13.29348 | -57.09237 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92d79fb8-c954-36e6-861e-8823778c9cae | -13.65695 | -53.94009 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 596b89f1-4fbb-34f1-a189-ad5500be269b | -11.37438 | -55.11216 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 048ba8f2-de8e-31bf-99e8-86956ec6a1eb | -11.7793 | -47.40126 | 2025-06-12 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4748c3e-0fee-3f88-ab4d-bd4ec2efe4fb | -11.5687 | -47.43565 | 2025-06-12 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0376a579-43fd-3a05-9129-440be41a7dbe | -18.66044 | -55.743 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f5d7664c-88f8-37fe-922e-bc335dffaacb | -21.58326 | -57.58679 | 2025-06-12 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5ee4c5b8-5264-39b5-a10b-e121fc2247ff | -19.5786 | -49.10365 | 2025-06-12 04:53:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
