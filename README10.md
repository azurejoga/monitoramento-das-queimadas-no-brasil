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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a3b4962-3bdb-3bb8-ad12-101b1c861783 | -14.06262 | -53.39839 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6e1cd81-489e-3aaa-8026-3c078689865f | -12.21001 | -57.28902 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 19f09b56-4291-3ad8-890b-55fcf09421d0 | -11.57365 | -48.13864 | 2026-06-04 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee624f91-7f85-31ed-b952-5850dc770b08 | -10.13959 | -49.15468 | 2026-06-04 04:44:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adb16c2d-4697-3f20-8a26-afb2a9a5ccff | -11.63065 | -55.17735 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56c6bb26-5ec6-369c-804a-e3b092c81b4c | -11.47697 | -57.11152 | 2026-06-04 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d52fb73a-f819-3a3c-b420-47f23416beb2 | -11.26297 | -53.97084 | 2026-06-04 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1cb5728-9d58-3f95-90f9-b39005a01ea4 | -14.08625 | -53.39354 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bba3bf07-408e-36bd-9dcd-b35c468ea8b7 | -10.39378 | -49.44884 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98278017-d13a-3992-8a2d-4c14b33a23a4 | -10.61094 | -46.71393 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3269ca9-b525-3937-acf7-c941937256e7 | -12.20649 | -57.29235 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5346c887-b34a-301b-8ef7-f70072d5b144 | -10.57196 | -57.32902 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef78ecd5-0251-3a99-8ec7-6a43d7521f26 | -10.61099 | -46.69006 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 302ba6ea-851f-3001-b1dd-d0cf9445a916 | -10.38989 | -49.45183 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50b20a14-6de5-3061-99a3-a3a036bef193 | -10.38824 | -49.4407 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0f79f3e-13da-3f8e-9d5b-f984fcca347b | -10.8233 | -56.59253 | 2026-06-04 04:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4681341-5087-3b81-b427-2d71c54b4bc4 | -12.224 | -57.27889 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b9338eb4-4bb5-37a0-9522-dab9f3cc9046 | -10.56029 | -46.62247 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9449dbe2-be19-3acf-9af0-e3647e19b482 | -9.92381 | -48.00906 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dcd67b9-8a1e-37d0-b06a-254a3d5657b7 | -14.04638 | -46.34245 | 2026-06-04 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03821361-9565-3e84-b8b0-6489c4d05865 | -11.78889 | -56.99977 | 2026-06-04 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 771053ed-dadc-36ca-b461-099f81d3eb23 | -11.55203 | -52.78373 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f39fc9df-fa1a-3037-be4f-7d310d1d56fa | -12.43644 | -58.40633 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c2cadb4-c11b-3a2b-8fd4-8e23c2efaa58 | -10.38322 | -49.45074 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0a52a30-2e14-36cc-b1f3-c4105407aa18 | -14.07673 | -53.38265 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc7183ec-efdf-3c10-bfc7-48f241949838 | -14.44798 | -48.90329 | 2026-06-04 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3ac0ad-0b7d-3354-b4e1-4ccda99b46ee | -15.438 | -46.33524 | 2026-06-04 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b27c12-5fc9-3a49-8f81-5184717fcd92 | -14.09443 | -59.38598 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb3f3436-7d1c-37fc-b995-237e36b4de52 | -12.21917 | -57.27794 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 0d1d2f37-b30d-3b82-b9e6-17769d63dbd7 | -12.17503 | -54.54153 | 2026-06-04 04:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f5113fc-e1bc-3606-b2e2-de604d038cf2 | -11.62845 | -55.1894 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48132333-7b7f-3e44-9b3e-bc195331ed4b | -12.22015 | -57.27259 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 14ada076-dfc8-3f61-a31f-27f20b40d663 | -10.35721 | -48.13605 | 2026-06-04 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f96decaa-c1d8-3f18-9cf2-683b5eef451b | -10.6139 | -46.69449 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976d9f0f-2ac6-3519-b296-221d17dba0fc | -11.16209 | -49.2522 | 2026-06-04 04:44:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd40dbbf-02b6-3e1d-b506-1480c1d5ead5 | -10.38655 | -49.45129 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c22f698c-e157-3a13-b632-be5dbd34821e | -14.76614 | -52.68198 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceb14fe8-b027-3f64-aca7-c6ed38872e54 | -11.88042 | -57.83315 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8667129-2e5b-3940-b16c-f594f4b2b75b | -11.61801 | -55.1849 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a2092e-a79e-3402-accb-c301ee6edf52 | -12.21817 | -57.28337 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3e69632a-cdf6-3b06-9867-b01df33167aa | -11.76135 | -47.07654 | 2026-06-04 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2711294b-2772-3938-b4fd-ba3ab1493f95 | -13.50966 | -54.31369 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7c957b2-a2ba-375c-8e1d-0ef20151f602 | -11.79211 | -52.51536 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26b6e1a-e28a-375c-8650-e668241fe006 | -10.53156 | -46.61862 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10b92980-9f77-34a5-aff6-5db3e612cdfb | -11.62992 | -55.18135 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5ee4519-3e9c-3ea8-bb4a-03432e39d931 | -13.50865 | -54.31508 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91b49234-ad22-31d6-b97d-cccad2200329 | -10.56803 | -57.3222 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36926a63-4005-35f1-82d8-c183f305c425 | -12.32153 | -47.90326 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a55ffd4-f57c-3c05-93dd-2422927276b2 | -10.57306 | -57.31765 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43d4f126-2043-34eb-b806-3be0284dda33 | -11.55572 | -52.78439 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e224c2e-9277-39b3-be31-a01ff6499087 | -11.88959 | -57.8298 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e53b0a6-6c57-3321-b825-4de47660bfea | -11.88489 | -57.83723 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd05cfd-2abb-3ce3-b729-cdb815b6e74c | -12.3 | -47.90748 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a196ea05-a9ff-3b7a-a211-15a62d6724af | -11.61027 | -55.33755 | 2026-06-04 04:44:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1584886-e4fe-35b1-9f95-23d7d7a9cefa | -14.16427 | -58.98415 | 2026-06-04 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b8adb93-25eb-3e59-8fdc-b5355d87399a | -11.817 | -47.50495 | 2026-06-04 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b66447f-ced1-3178-9558-ef833efeb85c | -12.17972 | -54.53873 | 2026-06-04 04:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec4f9add-e0d4-3b44-a2ef-b153ad229b14 | -10.61443 | -46.71447 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f74718c-213d-3ab4-b580-7cf063fade4a | -14.76862 | -52.67121 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 361b542f-94ff-3320-b96b-e1a0f08c2d05 | -12.22499 | -57.27351 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 41651508-8e0c-3db0-806e-6a353720bd72 | -14.7753 | -52.6711 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 475910b7-4f10-3150-8513-433173ceb3f3 | -12.7389 | -54.1995 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fc4b38c-fc96-3cb9-9e46-ce7f5073d57d | -12.21334 | -57.28237 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4e846e60-ff84-3962-8fd2-ab19c9d8ed44 | -11.47982 | -57.1109 | 2026-06-04 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2533640-40e4-38b9-8560-81a0d07d43b8 | -12.56017 | -48.34833 | 2026-06-04 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e38becd0-2bbf-32d5-8faf-bc575ded42b6 | -11.55497 | -52.78879 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8efe69ff-782c-3a1f-b885-45a08961e98f | -10.01322 | -48.21587 | 2026-06-04 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdcac7a9-bfe7-3c3e-967e-e075867255cb | -11.48242 | -52.91427 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59c3f40d-58bb-3cfa-b7b3-08fb2d78095d | -14.44742 | -48.90694 | 2026-06-04 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3011c293-27d4-3cef-802c-bfc04a4f7b53 | -11.88544 | -57.83427 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8a27db2-44e5-3eb6-8b7b-632c0b28c163 | -11.886 | -57.83129 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ea5dba4-cebc-31b2-bd04-b37fee4c05d6 | -10.55035 | -46.61702 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19f111fd-da81-33e1-b5c6-721408231168 | -11.89103 | -57.83239 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95a00898-63ad-3a01-b52d-f0a7eaf5fd53 | -11.75788 | -47.07598 | 2026-06-04 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7ca4365-6537-353a-8980-b2614ccce10f | -14.07889 | -53.39219 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95742036-d2ab-3e64-8af3-a8bd15d1a3c9 | -12.46038 | -58.47762 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d7bf7bb5-cc01-366c-86ae-d195c555f7a4 | -12.44553 | -58.41504 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfefd227-acdb-3aeb-a4db-4a21f01850fe | -10.55972 | -46.6263 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dea3f09-677c-3a75-ad16-857e913594be | -12.222 | -57.28982 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| cf29608a-9239-3336-8f04-85264f35d098 | -11.88342 | -57.83463 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abbe8332-1b2d-373b-bd6b-a51fe1920390 | -14.77215 | -52.67188 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15d524e9-7acd-32c4-9e30-d1760fb78238 | -16.1264 | -58.50513 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a90813d3-124b-39c0-abf8-30b00113fbc7 | -19.73701 | -53.54784 | 2026-06-04 04:46:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a144aa66-8eee-3d29-979d-f79340d74642 | -15.50046 | -56.031 | 2026-06-04 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c944cac8-ee9e-3083-8b92-6fcf8088b5fe | -21.55126 | -49.87178 | 2026-06-04 04:46:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 232d9829-8754-37a3-9a5b-0ef9ffc95781 | -19.73979 | -53.55256 | 2026-06-04 04:46:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 670b7d77-a54b-3b66-b7e2-77dd997c0d4c | -19.12614 | -49.76286 | 2026-06-04 04:46:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9f17a6d7-fc4f-342b-95de-9781b3861427 | -20.02182 | -48.18959 | 2026-06-04 04:46:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d5eb475-c02d-3de3-bb25-ea195286b201 | -16.1898 | -58.46648 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| df4a6fe2-4186-3694-843e-9b3f9a08e07e | -20.55521 | -46.3615 | 2026-06-04 04:46:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d635c80-745f-3cf0-a35e-52ac1dd0b9ea | -19.1701 | -55.1888 | 2026-06-04 04:46:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0876b0ac-a3b0-3518-abeb-b58d1429f0c1 | -18.46119 | -54.7086 | 2026-06-04 04:46:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8991f00a-4474-300d-8391-1ee5d8d38bc9 | -16.18763 | -58.47762 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4098c8c7-04a9-3594-a7c5-ca562c6d9045 | -17.4629 | -55.20168 | 2026-06-04 04:46:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8feaa923-50d1-3180-9824-e7af3a1a0dbe | -16.43888 | -57.26511 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6ff9a066-2511-3558-9919-91a3029fb430 | -21.55233 | -48.59384 | 2026-06-04 04:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1a5e5e4-ef5f-3ed1-a20d-a8bd8048f399 | -19.12276 | -49.7623 | 2026-06-04 04:46:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e472863b-9867-3108-8f68-b8ab51cd8c9b | -16.74438 | -49.93451 | 2026-06-04 04:46:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4390d65a-59fa-3601-b5b7-b7f8f9b70580 | -16.14433 | -58.49155 | 2026-06-04 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2b9ebb1e-8f55-3ac6-a32e-114e128a4217 | -20.02842 | -48.19502 | 2026-06-04 04:46:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
