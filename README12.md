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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a50384c6-812b-3242-9350-1fd282874b10 | -11.24107 | -43.3639 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d696787b-fd85-3c97-a166-037586b3a102 | -12.85583 | -44.35793 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d61bbc9-2370-3fe5-af22-f89995daaef2 | -10.111 | -47.54845 | 2026-06-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a36b93ab-dfdb-3c8a-8c21-370b9eda91d4 | -8.82137 | -47.06556 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6e85c17-a5e9-3920-b5cb-2681ff0eeaad | -7.602 | -46.47886 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c40367c0-b695-3614-ba2b-004f45b10e01 | -9.37884 | -41.22202 | 2026-06-24 04:34:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62213db4-3d61-33a3-869d-f96356348a31 | -14.23167 | -42.76384 | 2026-06-24 04:34:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 993038a9-cf48-3310-8fc7-ac5e569000cc | -12.81619 | -47.05506 | 2026-06-24 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c015f843-6b4d-3867-b5d8-f84dd1aa604b | -11.91751 | -44.17072 | 2026-06-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fbd5b19-f3d4-3955-8bec-1a8c0a870e22 | -12.06707 | -48.4286 | 2026-06-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6df0095a-85b1-3f9d-8aad-a38142c38105 | -9.44261 | -48.87346 | 2026-06-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17397c96-c1b0-36f1-89d5-0035b3e15a5a | -14.52583 | -49.11042 | 2026-06-24 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cddde76d-b316-352a-8a34-55b05b144d77 | -8.13795 | -47.88342 | 2026-06-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7292d33-3e7c-3a00-ba92-dee0b092779a | -14.76117 | -48.18705 | 2026-06-24 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 354991c8-bef7-3cef-b8a1-b3894526204e | -9.51455 | -48.06607 | 2026-06-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc666b8b-97bf-3086-aaa6-c79d585bf318 | -8.69015 | -47.85388 | 2026-06-24 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a86ed1b3-5835-39b5-9f19-86616eec6ee0 | -11.30746 | -54.71723 | 2026-06-24 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65862327-b39b-398f-9747-f178dfc791c2 | -14.16625 | -42.99261 | 2026-06-24 04:34:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 571cd9b7-7359-3e1d-a4b5-2153ec29541e | -12.66381 | -47.67794 | 2026-06-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fe1c78a-2dfc-3fdd-9a48-621730b74d36 | -9.74767 | -47.87792 | 2026-06-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ae25d32-6554-3889-ab84-1b523769bdcc | -12.66436 | -47.67429 | 2026-06-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2899150-32b5-34d2-aaf1-60764ae01d00 | -7.64065 | -50.21491 | 2026-06-24 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 320c12e3-13d6-3006-bc0f-efb39ed8d234 | -10.15745 | -56.62473 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b12da77d-53cc-323e-9378-16ac4c9a2ca2 | -11.47018 | -46.72783 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6d8478e1-5a4a-35fa-b7f1-b235915e081b | -9.80695 | -48.91773 | 2026-06-24 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 104eb81a-90ee-3e06-b765-3af055d04938 | -10.37611 | -47.61514 | 2026-06-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f85422f-a822-346d-b3a6-031295b4b919 | -11.75865 | -47.07527 | 2026-06-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44c7f9a7-966f-381c-9148-a836694f17da | -12.22981 | -46.60913 | 2026-06-24 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 132bed13-f0a5-33d2-a9f8-b2dc8b9fcce9 | -8.85606 | -46.95021 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99eded4b-2588-3a87-a148-ff19067e239c | -10.90258 | -54.13038 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83be4b1d-ade8-39d1-b168-29619ab38f40 | -8.85715 | -46.94313 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9738201-3ad9-3129-a50d-2c56391fefea | -9.22338 | -45.3466 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a392602-fa91-379d-9fe2-fc9a70a423b3 | -11.62603 | -48.48825 | 2026-06-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8836084e-4060-3124-875c-8a81e463092d | -12.85697 | -44.35586 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 109437f3-e25b-37e8-a4a5-9a67373920a1 | -11.91103 | -43.4033 | 2026-06-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6321e520-4dd7-3da0-afd9-841c30dba69a | -13.06422 | -53.35553 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 70fada47-1db2-3233-be89-e6efa7a230ea | -12.84906 | -44.35471 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| df9d5863-1d70-31e2-8377-67581b9f36b3 | -10.5306 | -48.15908 | 2026-06-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47688404-0d86-3707-9f28-4f52d07f2714 | -12.85301 | -44.35529 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44d01b5b-c858-3c6c-9e63-f9f30fdede8a | -12.8365 | -44.35813 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 616f0e13-1c0f-3d27-a4b9-8df763b9336f | -10.90601 | -54.13482 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 098fb20b-7cc9-3215-ab49-6307ee96a594 | -10.90257 | -54.13435 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 612d998e-cab6-3fbe-95cd-3d6471eeeb8b | -11.62219 | -48.49123 | 2026-06-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8583f4fe-cc5a-3193-b359-8413f03beede | -11.62273 | -48.48772 | 2026-06-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6525271-37d2-36e4-a721-ea5f338521f9 | -7.80436 | -46.46485 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 644c58af-a81c-3e4a-b249-2bf5959856ab | -11.42228 | -54.43946 | 2026-06-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaaa276d-933b-3edd-ac90-5c981a5b73d7 | -9.37124 | -50.53323 | 2026-06-24 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b547522a-f0e3-36ea-9bd3-1557b2c55b66 | -8.61054 | -46.00092 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88ad3788-ad9d-3713-9c8f-5290857a9388 | -14.27756 | -43.80046 | 2026-06-24 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f063a31-af8b-35d6-81e7-35537ded7fc1 | -13.06503 | -53.35081 | 2026-06-24 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ad01fc0e-a607-36a9-b3f4-0ee1877fe7e0 | -7.8049 | -46.46124 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 503c6c12-1cd4-3df2-90c6-7824dfd6f23a | -11.24571 | -43.36074 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74c18947-f073-312b-b724-d5e721d404db | -8.07798 | -46.39096 | 2026-06-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57642d4c-711e-3852-bef4-bcb5e93765ef | -12.78046 | -44.44437 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32b0bcce-c608-3383-8c8a-e089cb6141f8 | -10.90667 | -54.13109 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 087cff22-ebc8-3b23-9c98-66a0bbb6d4a9 | -11.24519 | -43.3645 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ce4c9fd5-9913-36f4-bb3a-fa92266d2474 | -10.87417 | -49.39999 | 2026-06-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4ddd831-87d6-34bc-927d-94c9c65209da | -10.12583 | -52.1103 | 2026-06-24 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce90d6db-5673-3bb3-b3d3-77896957022e | -8.13081 | -47.88578 | 2026-06-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 787034a1-0c32-34a9-9e65-2093e781867d | -10.90534 | -54.13855 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 275c6ac5-ca7f-3423-ba85-edfeea436a4a | -8.38582 | -46.48964 | 2026-06-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f0548b9-bd29-3f4d-9833-e51ad31396c8 | -8.31122 | -45.39599 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d38f8726-3f0a-3966-83aa-cf15650f4628 | -9.4404 | -48.86597 | 2026-06-24 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07b780b2-3e3a-3491-a1cd-c87a0580d504 | -13.77755 | -53.07555 | 2026-06-24 04:34:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8cc610f-d01e-3918-a9a1-006548ec954f | -10.90324 | -54.12667 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15cc2e0c-a1ae-319f-9a13-7a48eb7b5b06 | -10.57662 | -57.32012 | 2026-06-24 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fcee047-f725-3463-829d-5a88dddb8822 | -12.91714 | -49.48106 | 2026-06-24 04:34:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be50bffb-7ea0-3b08-8220-b3d04905e49b | -7.91794 | -48.28751 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c24f5aa-7871-3613-ad94-4609fa8a73a4 | -12.87059 | -44.37362 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dbe6a12-4d91-301c-a4bf-998bfe8d4243 | -11.2679 | -43.35242 | 2026-06-24 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2edc006c-f67a-3c64-b9d8-0075fa600719 | -14.04068 | -50.52896 | 2026-06-24 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90957840-5235-317e-84c2-c35b0e1c35b0 | -9.13899 | -47.98527 | 2026-06-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1606ef24-76d9-3d91-a691-9ee5c8b5d22e | -10.76823 | -54.11089 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fcf494f-0f5a-35a2-8521-e9f60b757a5a | -9.58555 | -49.1118 | 2026-06-24 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8f67e3a-109e-33a2-9570-84a0247aa5ff | -9.21685 | -45.3414 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e68ff4d-6afe-3b90-adb3-1ead5814b2f9 | -10.11433 | -47.54897 | 2026-06-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f0e3d9-b890-3cc3-81f3-414026186638 | -12.78509 | -44.43979 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e03bd6e5-abca-3519-ace0-86ee89d89a41 | -11.15632 | -48.46667 | 2026-06-24 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23ac94e2-48d3-31f6-94f3-3724eb497613 | -12.78186 | -44.43412 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 28a6a43b-a878-32fb-89b4-d9be107c9fc1 | -12.783 | -44.45514 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f29ba6d-ef76-32c3-970f-1f02124ea78f | -9.22399 | -45.34247 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 899ec9f8-2beb-391a-93a1-cf385958ea6d | -10.80107 | -48.56373 | 2026-06-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ca9fa82-f852-3297-90a9-436209703d32 | -7.92069 | -48.29148 | 2026-06-24 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c9ed358f-b5d4-3ca0-b194-bc576c7a97d1 | -9.21746 | -45.33729 | 2026-06-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9ebf4c4-a200-3a5a-8084-7b37648845e5 | -10.39194 | -56.72344 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf98281c-9f78-381a-9aec-59f5bff0f3a4 | -10.90321 | -54.13061 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf41051a-2957-3164-a0ca-f93d797475c1 | -12.84439 | -44.35931 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 36df6fcf-5bcc-3ba5-97f2-a283b353b256 | -9.1836 | -58.059 | 2026-06-24 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc0d3866-72d1-3c61-bcfc-bdf815568477 | -14.25288 | -43.22697 | 2026-06-24 04:34:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 73ea525e-cc50-3f1a-b8c1-f600c673b2ed | -11.11059 | -54.14131 | 2026-06-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48efeece-f484-307f-8977-a591e2defbc4 | -15.72845 | -41.35412 | 2026-06-24 04:34:00 | NOAA-21 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 3c3a5fa4-2153-349e-80e2-215ac373a93f | -8.82082 | -47.06912 | 2026-06-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69268eb5-f9bf-3e43-accd-f61610f7b720 | -8.60824 | -45.99278 | 2026-06-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f8777194-cc94-305d-ad88-1818708ece6d | -11.75993 | -42.05985 | 2026-06-24 04:34:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 803ed7e4-588d-3855-b4fd-9ad175acb198 | -10.12949 | -52.11092 | 2026-06-24 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59a547b-af0e-35ac-9212-28f7353aa35c | -10.38711 | -56.72217 | 2026-06-24 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d6abaa11-63e0-3820-bdf6-802da777337f | -13.85188 | -47.03927 | 2026-06-24 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e0744f7-07d6-398f-b448-a8ada11314bb | -12.72912 | -46.30516 | 2026-06-24 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45fba79b-5859-37d9-9725-33ce3641d451 | -12.77654 | -44.44379 | 2026-06-24 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bbf43be-938d-3747-898a-43c289e99dbb | -12.51604 | -48.27114 | 2026-06-24 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README13.md)
