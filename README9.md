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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b69dbb32-2212-3a25-8113-27da0d4688bd | -22.42597 | -46.79621 | 2025-05-20 04:36:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f31be87-3da5-3e88-afef-56c598e61298 | -19.05587 | -53.45963 | 2025-05-20 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92fc7958-05c5-3bb8-a1e3-395fb4b4cff7 | -17.80236 | -44.3448 | 2025-05-20 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 147c1161-5a7f-3267-922b-41518aefc620 | -19.16254 | -47.81814 | 2025-05-20 04:36:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea417450-dc9b-3796-bd6a-314de0599960 | -17.85258 | -50.57484 | 2025-05-20 04:36:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12e9be81-8b39-395a-a993-f51e5b9fe117 | -21.1958 | -48.48771 | 2025-05-20 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5aae254-6a2a-3125-bda0-6ed12bfe8e78 | -18.29332 | -51.86726 | 2025-05-20 04:36:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acebc95d-e182-3ba5-bb45-2678f82752ad | -17.50397 | -46.74358 | 2025-05-20 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4287f4bf-5bd7-37d9-a293-3d1d9cebd3a4 | -18.13668 | -52.35813 | 2025-05-20 04:36:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecee612e-bf1d-376d-a632-1740893fe151 | -21.22269 | -48.60631 | 2025-05-20 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8e68ff3b-49d7-3ce3-94b6-e50c7198ff06 | -20.95116 | -56.60584 | 2025-05-20 04:36:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa6bb270-1a18-3a59-87ce-ce11272d26a9 | -16.93071 | -53.01723 | 2025-05-20 04:36:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5143f28d-057c-31b4-8986-afc616e5b360 | -21.19554 | -48.4902 | 2025-05-20 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a419754b-7b28-3991-811a-e232e06c4cb6 | -19.06284 | -53.46094 | 2025-05-20 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 510835fc-af89-3e73-9326-e0d0bfe4539a | -20.95661 | -56.60678 | 2025-05-20 04:36:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c61c2c64-b7f7-3508-acd4-26e8ea9d4266 | -20.5383 | -47.30069 | 2025-05-20 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6881494b-6ad8-3ffd-834d-93b9ae91fe81 | -17.86489 | -43.76022 | 2025-05-20 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5231c30-f640-3c8d-af7d-d8ca9141b98e | -20.17751 | -55.00526 | 2025-05-20 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cb8f6f8-6740-3a46-aee9-80dc18fa536b | -20.22216 | -50.75443 | 2025-05-20 04:36:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 351c4aaa-3abd-3b6c-8f6b-b441521fee90 | -17.4177 | -51.33956 | 2025-05-20 04:36:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a22c9a3-2eaf-3813-a06f-78dec5879822 | -18.14616 | -47.8028 | 2025-05-20 04:36:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6fd4987-57b3-3baf-a904-255432f6fc4e | -17.42103 | -51.34012 | 2025-05-20 04:36:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc62361-127b-3760-b422-29ed0c8ffe6a | -17.40763 | -54.72107 | 2025-05-20 04:36:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e94bc168-50ad-36c6-82f9-ab11928a52bc | -19.45364 | -45.30571 | 2025-05-20 04:36:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1d25e84-63b7-397c-a8fd-77c3444a6615 | -16.40032 | -58.1682 | 2025-05-20 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 42b9fbac-ab02-35a7-91ed-80e49636ea72 | -17.50091 | -46.73847 | 2025-05-20 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 667abf17-c88e-3635-af79-a4faf143f822 | -20.38766 | -55.39379 | 2025-05-20 04:36:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421a923d-3fe1-3316-83f5-9716ac3cdc08 | -17.11351 | -49.1404 | 2025-05-20 04:36:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7dc5f8d-906c-3fb4-b7e4-1817b4f287c6 | -19.15898 | -47.81767 | 2025-05-20 04:36:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60d93254-99ee-3384-9273-89f406bf3f5b | -18.44737 | -50.13701 | 2025-05-20 04:36:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c1ae775-6168-3be7-83a0-4f3f7788e4f8 | -19.05657 | -53.45551 | 2025-05-20 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68745e6b-e3ef-3674-874b-af68170ab508 | -20.41872 | -43.5527 | 2025-05-20 04:36:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 741c9f56-88bd-3a65-9b30-6fb1602dbb5a | -18.50785 | -47.52183 | 2025-05-20 04:36:00 | NOAA-21 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b8246be-e5c8-3bfa-a7cc-f848a2eaeaeb | -20.47709 | -53.67584 | 2025-05-20 04:36:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55d23e70-bf5e-35bc-b3cf-a9fc0822f08b | -20.18121 | -55.00597 | 2025-05-20 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41b2d38d-c6f9-3d71-bd72-20ced2212681 | -21.22211 | -48.61048 | 2025-05-20 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| bde8e996-218c-33a8-b2a4-75c76ee41ca0 | -21.81051 | -47.24681 | 2025-05-20 04:36:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 370af898-a06b-3133-be1c-0bc8caf27d3a | -23.58347 | -46.43386 | 2025-05-20 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d8b88b7c-a540-35de-bc18-20ff0fa6d42f | -27.11963 | -50.57864 | 2025-05-20 04:38:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4586e8ca-920b-3c83-9c3a-799ae104f1a1 | -22.84001 | -51.05925 | 2025-05-20 04:38:00 | NOAA-21 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4833b77e-4527-3950-8ccb-ce91762a793c | -23.16263 | -45.77708 | 2025-05-20 04:38:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 257c02f6-853b-331e-97ca-689d46c1396f | -21.46587 | -56.29568 | 2025-05-20 04:38:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4ba0d9d-763c-3388-af92-efdd47b06736 | -23.40768 | -46.55746 | 2025-05-20 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa067ed4-e209-3072-9763-f21bca93b0e1 | -27.12021 | -50.57444 | 2025-05-20 04:38:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea73203d-2fec-3cf3-87a9-1819d47adf61 | -22.21607 | -56.19917 | 2025-05-20 04:38:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ed86603-05a8-394b-ba31-a9ca08336e85 | -27.68803 | -48.75089 | 2025-05-20 04:38:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 823042f5-dcaf-3eeb-806a-7e23efec494b | -23.60713 | -49.00764 | 2025-05-20 04:38:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21d8f4e4-1c6d-3b14-bf4b-f01ca2d17598 | -24.24229 | -50.73814 | 2025-05-20 04:38:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47c9eb0a-864e-3228-97dd-c94046b907d9 | -23.3388 | -46.77272 | 2025-05-20 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02752937-fb74-3c77-81a2-a1fd275f9268 | -25.86376 | -52.17915 | 2025-05-20 04:38:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 220f4315-45b4-318c-8b29-fdaec860a437 | -22.54042 | -48.81252 | 2025-05-20 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebffba69-0011-31ae-9853-914bfcb8cca4 | -26.71346 | -51.36183 | 2025-05-20 04:38:00 | NOAA-21 | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11899f2d-2765-312d-973f-6bfc4721806d | -23.61006 | -49.0125 | 2025-05-20 04:38:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d33332d-2280-3cd8-a7b3-3a504ef6b1ed | -23.61066 | -49.00824 | 2025-05-20 04:38:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 784668dd-a635-338e-9602-b6f609908ca7 | -28.58692 | -49.44376 | 2025-05-20 04:38:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26d767a4-731d-311c-9738-07b5ff934f0f | -23.60653 | -49.01191 | 2025-05-20 04:38:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6fe1831-1655-3ab4-af63-634ca1e75035 | -25.1862 | -50.10876 | 2025-05-20 04:38:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8389fb27-1bb3-36c6-86da-a23d73abaa45 | -6.2315 | -43.36227 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c1766cd-3b59-3eb4-ba3c-916dca8bbbf3 | -5.75871 | -43.49233 | 2025-05-20 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b719cd43-7ae4-36a9-a9df-d259819c9f1a | -6.22738 | -43.34782 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 519f8461-1396-363c-bc51-21e1a47ccdc6 | -5.02067 | -45.10253 | 2025-05-20 04:57:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f40dda3-a10d-302a-924e-129a119fe261 | -6.23276 | -43.35327 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45ab72f0-c0b4-3b5b-8679-960a78b6febe | -5.97518 | -43.7618 | 2025-05-20 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d1cb87f-ee7a-3f0d-8e93-a184c93b43c9 | -5.76519 | -43.48918 | 2025-05-20 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e6f38d1-1b1d-399d-bc62-2a2ce2c370b4 | 0.71366 | -51.36961 | 2025-05-20 04:57:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e85c8d6-ea4a-347c-b17f-c242cd9b6a1c | -5.96351 | -43.7602 | 2025-05-20 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e17faa5-9570-3ab8-9d80-1636d0fcc3f9 | -5.96994 | -43.75677 | 2025-05-20 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 185fcb9a-7ca3-3ba2-987e-ddcb6ff1bbc4 | -6.22674 | -43.35242 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d686afd3-7743-3433-b7f2-04d909ebdaf5 | -5.97578 | -43.75757 | 2025-05-20 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e321fec4-2782-34c5-81f1-e192d97e075f | -6.20465 | -43.33483 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ba77ea5-cb39-35be-a316-0849357da3dc | -6.2388 | -43.35388 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e28bfe6-b844-37bd-b69b-712bff553713 | -6.22611 | -43.35696 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54d02ac5-2a01-3c1b-a1fa-a100ff74d72f | -6.20583 | -43.32619 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9679288c-9e05-3458-8597-2196a59589ca | -6.20523 | -43.3306 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26b452dc-6e2a-372b-9b9a-7e965639b022 | -6.23088 | -43.36672 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8edc6914-5337-39f9-99e3-7df4711093c2 | -5.96935 | -43.76097 | 2025-05-20 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6bf9cfb7-f48b-3bd3-af9d-80da093c4b44 | -6.23755 | -43.36286 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca569794-2840-3fef-a894-6c8b83ad547e | -6.23341 | -43.34858 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b749a60c-2e4e-330e-bc14-5753c0a9a3a6 | -6.23212 | -43.35779 | 2025-05-20 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e9d26286-9949-3a98-97cc-c592467e5702 | -13.02942 | -45.06731 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acc992d6-93d3-3bc7-95a5-f5858ed13816 | -10.36361 | -47.9717 | 2025-05-20 04:59:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58e9eb1d-7dfc-3d11-8b4a-c8f76430d521 | -13.3175 | -45.37039 | 2025-05-20 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28930818-97de-3e72-9b71-8959da3d1c46 | -10.81803 | -56.96263 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08ac62cd-011b-315f-a1aa-dc33176b657e | -12.2939 | -52.47495 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c00c7c63-ac2a-39fe-91ba-be30287b218b | -10.36296 | -47.97651 | 2025-05-20 04:59:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33cfb163-e228-3ba4-9dd2-47c5af5bfc6a | -10.35895 | -47.97091 | 2025-05-20 04:59:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a91c557e-45f0-356f-a4a0-fc3f28276188 | -11.4188 | -44.70049 | 2025-05-20 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d44c74e-9df3-323f-8d45-7af04d02ce14 | -11.66397 | -54.94146 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765123de-b3db-37de-99cc-9d9536653b20 | -9.03523 | -47.75876 | 2025-05-20 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75d996e4-382c-32d6-b83e-052b3183cae5 | -12.83619 | -47.39709 | 2025-05-20 04:59:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ee44287-f4d9-3f45-b316-5577e025880b | -10.76562 | -54.78028 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f50c48df-c7eb-35c3-93ec-6d9d73055b40 | -11.41776 | -44.70914 | 2025-05-20 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f63b524-14d2-36d3-8a45-0d2ca494a2b8 | -9.413 | -58.3236 | 2025-05-20 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55956c14-9252-374f-a3c6-e961753360b2 | -12.01863 | -55.41869 | 2025-05-20 04:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d98af962-7f20-34c0-b5ca-767ea0947f4c | -10.34478 | -51.69238 | 2025-05-20 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cd109dd-f034-344a-8967-432ff1c518ed | -13.02255 | -45.07521 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91e3b450-b38d-30c3-a9e9-587327547917 | -12.42933 | -43.72513 | 2025-05-20 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a94753b-febb-32bb-bb54-d17f95cbd79a | -11.56717 | -54.56157 | 2025-05-20 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efe57ced-1fd6-3f3b-ba42-6d49ec204bab | -8.63238 | -51.28831 | 2025-05-20 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3398937-372a-3a2d-aa55-d17dc4702c2b | -12.34119 | -49.97592 | 2025-05-20 04:59:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
