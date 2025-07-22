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
| bf6ce19e-fbb2-36b6-86c9-e53f72a244f1 | -5.68485 | -43.67535 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4895d917-19ac-3739-8eb3-47f6ea257c24 | -4.38572 | -43.28193 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3e35bfb-caa9-3230-a5fb-9caeb9b011cd | -6.19463 | -44.39303 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e7a10c1-7fcb-3a0c-9967-71b66c4b335f | -6.71574 | -38.96423 | 2025-07-22 03:38:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0830fa56-d7bb-3e46-9443-4fc04a74eadc | -6.20203 | -44.38605 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59f38f31-08a4-369f-8988-cdd2facd3cea | -10.61089 | -45.23951 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfb1e07d-634f-360c-b428-57dd4590e575 | -5.51415 | -35.5794 | 2025-07-22 03:38:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 72332a75-ced8-39ce-9b12-a4426b366adc | -10.61759 | -45.23624 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 05df5eee-4480-31c7-8a84-41df6dd66456 | -5.56243 | -45.21613 | 2025-07-22 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd2de618-eb1b-3116-88ac-a1ca34b0de0a | -4.37747 | -43.29277 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8904b8fa-f4c5-3bb8-83db-f99ac022550d | -6.19818 | -44.38758 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f8e00d4-2d08-3487-b86c-36b6fca50bc4 | -8.51749 | -43.30795 | 2025-07-22 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efb15018-ab84-31e4-addf-0caeea3298fe | -9.06372 | -45.06794 | 2025-07-22 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a6890c9-edcc-3ea1-a68a-31e0fd8ca302 | -8.28907 | -44.96703 | 2025-07-22 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cdf2508-068c-3087-b5d9-72855c5d1b48 | -8.2899 | -44.96262 | 2025-07-22 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fefea9fc-0adb-307c-a694-97b5b8425ef4 | -9.06454 | -45.06356 | 2025-07-22 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a784573-4241-328e-ad7a-f5c798dbcfe6 | -5.68555 | -43.67133 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bffdce04-0bae-3276-8826-30de40452e4e | -9.6318 | -40.59225 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 43042291-c8d4-3548-bf4a-097f4e2f11dc | -6.97338 | -42.80378 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e779332d-83d1-3897-a30f-916bb4b91e37 | -9.06289 | -45.07237 | 2025-07-22 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3200237d-9540-351a-9df5-38c9277da63a | -10.61842 | -45.23196 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 564e34d2-9aa0-397f-9f70-a65e041c5f1e | -5.68747 | -43.66414 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| db41e494-6217-3935-b3f5-8e26c89ea64e | -7.1789 | -44.14451 | 2025-07-22 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ecda35e-b51a-3c41-bf8b-cd6e73972637 | -10.63165 | -45.22621 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 998f6a1a-2d31-3cee-bc22-2305381e6108 | -7.20833 | -45.33018 | 2025-07-22 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d35e8f48-bd8a-3c99-94d2-588c8fda3ff5 | -4.38502 | -43.2859 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa5f1c14-509d-32ce-80ae-04de78fd62c3 | -4.37862 | -43.28875 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 073ce54f-00c7-3db8-bfa8-dc1a7a1a670d | -4.38385 | -43.2899 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 38c7bdf7-7911-3866-a01d-feb886822788 | -10.77082 | -42.71518 | 2025-07-22 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbb65d55-981c-3b6a-ad8a-e726c97f07a9 | -8.58276 | -44.32507 | 2025-07-22 03:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abda12a0-4bfa-3756-a3b4-95d91ebd99ec | -9.49636 | -40.56896 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7e1294bf-391c-3f03-870f-70dcba5917d2 | -4.39005 | -43.29092 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 044a2e70-1db4-322b-87e9-4371dd5493ca | -5.68606 | -43.67193 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b95c01df-ddd9-372e-a0c1-7144d1a7c615 | -4.38363 | -43.29383 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d8ee1889-e2ab-3b6d-971d-aecb69c533a8 | -4.38957 | -43.29098 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b808c843-fc01-3c14-b5ed-88ff333fdcef | -7.25641 | -44.30621 | 2025-07-22 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9271ca-8a2b-3b85-b099-a3d46545b750 | -10.22697 | -48.0644 | 2025-07-22 03:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26c3e664-f35c-367b-84dc-977cc9784aa1 | -7.12172 | -43.33378 | 2025-07-22 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 87e296a9-72cb-33f8-b0d5-9d343db129bf | -8.9186 | -47.35775 | 2025-07-22 03:38:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe6540c9-bf28-3119-bb8d-797716be2b6f | -6.97869 | -42.80475 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 009d7eca-73ec-3cc2-9a5d-06b3b23e065b | -9.56876 | -44.50629 | 2025-07-22 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 753e43ce-1626-308e-80d5-740674fea4b0 | -6.84422 | -42.73916 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8635fc08-f614-373b-b516-50fbbf1a81cc | -9.63256 | -40.58796 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c00c5dd5-7f1b-3167-a490-25cff897fa35 | -9.49713 | -40.56469 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8f4264dd-cb1a-3add-8a89-41c120208280 | -9.07045 | -45.06483 | 2025-07-22 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd5141b6-26a9-39b8-b737-8922614b0d4d | -8.37829 | -47.61771 | 2025-07-22 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca633179-abac-39bf-bc79-492515cc1ee7 | -5.68533 | -43.67596 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8748b65f-808f-31e1-b540-7ca104b04ec7 | -9.5695 | -44.50236 | 2025-07-22 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 846d837a-cd53-34a6-aa0c-465066034049 | -8.10332 | -46.82795 | 2025-07-22 03:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c1507aa-3b9d-307a-a743-b5f9a15ef8c2 | -4.37792 | -43.29273 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e6b035fb-defc-31cb-a221-4a272d85456e | -8.0966 | -46.82671 | 2025-07-22 03:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92845010-1500-3600-bdfd-4221fc4af6fd | -6.20129 | -44.39022 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8226ddd-2c5e-386d-a853-88dd8e3c12f2 | -8.37644 | -47.61685 | 2025-07-22 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79ffde61-5180-3fe2-9c85-12ad0fdea3dd | -8.37778 | -47.61013 | 2025-07-22 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd478ad0-8a43-364c-b123-3810b20b0a02 | -10.62424 | -45.23319 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3bc9b21-766e-3bd8-80eb-614fd812714d | -5.66893 | -43.66465 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c006604-ffe0-3fcf-b238-ec9ede36ca9a | -6.1966 | -44.39615 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26e60da0-db8b-349a-b221-ab10e6627016 | -9.62667 | -40.59575 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 07d62a58-b307-3833-9ef6-1afa75d87567 | -9.573 | -44.51503 | 2025-07-22 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ade90230-883d-3cf8-8f62-a984d91b5c8a | -4.38319 | -43.29388 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 57a658e1-0555-32c2-b4f6-892471432381 | -10.61173 | -45.2352 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76ff7985-9bb6-37da-ba83-b68d2c847b67 | -6.8448 | -42.73591 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8f9c390-4d1a-3a13-bb62-4bd25ee35138 | -6.19739 | -44.39184 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 745a60cb-81cf-36f4-b98e-baf192446a06 | -9.62591 | -40.60004 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0431f71-d5d1-3932-b5cd-924c0157ea6c | -9.57372 | -44.51117 | 2025-07-22 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d88eec8-8e7d-3354-95ed-06bcb92ed21e | -10.62505 | -45.22902 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f741e932-e7eb-38ab-b620-297b2b189718 | -7.25131 | -44.30108 | 2025-07-22 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ff967b7-a783-3eb3-a04f-6ae256e0e4aa | -10.63086 | -45.23033 | 2025-07-22 03:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80b2d038-813c-391b-8ff5-3a3183f1f0eb | -9.49198 | -40.56818 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2c1c5ead-1d53-3030-b19c-e4b710e40dc2 | -5.68414 | -43.67941 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bc8331e-aa3b-3840-9359-5597d959b99f | -8.91735 | -47.36414 | 2025-07-22 03:38:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 082db72a-cd54-3e1e-b93f-e6f0c10e67d1 | -5.68991 | -43.68037 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edc6bbeb-ba7c-3278-b5ef-b5903f906a97 | -4.38433 | -43.28986 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c98f7e9d-6b99-327c-96c1-19ca9cab2985 | -9.06958 | -45.06947 | 2025-07-22 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b388b388-38ea-316b-ab16-c4ce59d314f9 | -8.5181 | -43.30458 | 2025-07-22 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca6c3242-3a37-3b9a-aa6a-a2a277bee287 | -4.37814 | -43.28878 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 477b0e5d-4d07-3aa9-b244-2079f8cf1bec | -4.38519 | -43.28196 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f39b30ea-0bf8-367c-9abb-26e684f4650a | -5.68115 | -43.66255 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f13755a-3f15-39d3-a9f0-c57c9377b85d | -9.63104 | -40.59654 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 1d9a9cc7-2385-346f-847c-e2e0839e86b3 | -10.23385 | -48.06617 | 2025-07-22 03:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6ea3ab5-4d96-3e0c-9e50-37ed9937d69c | -5.67399 | -43.66962 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1692cac9-19c7-3e29-8306-75f99303489b | -8.51275 | -43.30357 | 2025-07-22 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| eb9ed1c5-6f80-3906-8d28-d328b50aa7e5 | -8.51336 | -43.30021 | 2025-07-22 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 42d53cd7-fb80-3cde-a1d2-022b13569fc7 | -5.69061 | -43.67632 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae1ee5a3-56f3-34aa-8086-e127e9eea618 | -9.62818 | -40.58717 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 75e02f2b-2e66-3ff0-b78d-6f4fe5c908e3 | -5.67907 | -43.67449 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de6050eb-6cf3-3f83-a377-6a76b4bef55b | -4.38452 | -43.28593 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 84454385-1827-39eb-a1ac-cb187e427ccf | -8.91052 | -47.36284 | 2025-07-22 03:38:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c34a90b0-a807-36eb-8393-ec8ea587debb | -5.68046 | -43.66649 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c40831d-eddb-3959-a585-103487bb816d | -5.68677 | -43.66801 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cb3a9935-fa05-3e9b-ad6c-18a0e6dc2f51 | -7.20743 | -45.33513 | 2025-07-22 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdd4a0fc-0e48-3b57-a492-0817370fff24 | -4.64855 | -37.79762 | 2025-07-22 03:38:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62fd60cc-a8a9-39fe-aa8a-9f334b43684b | -9.50151 | -40.56544 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b4c41da-4ab2-300a-b737-e464dd5ab365 | -9.62743 | -40.59146 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 31f39233-61c4-3115-a469-e0c45beed7d6 | -8.58212 | -44.32143 | 2025-07-22 03:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a24ab8b9-151c-38ba-a548-3b24a5a48695 | -5.68624 | -43.66739 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6be9cc85-42a9-3c70-9959-df28e9938068 | -9.33239 | -37.98249 | 2025-07-22 03:38:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f58040f-a204-397f-adb0-00cdb96759a9 | -9.50074 | -40.56973 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b490b358-db6d-3065-976a-5c085673f2e9 | -5.67977 | -43.67048 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c95fd0f-1c6a-319d-8c2d-0014af4a8f7b | -8.51152 | -43.31032 | 2025-07-22 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |


[Clique aqui para ver as próximas entradas](README6.md)
