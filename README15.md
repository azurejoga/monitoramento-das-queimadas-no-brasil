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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c31d6ff6-4cc1-397c-9a3c-5ffb405110e2 | -10.856 | -54.03173 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e84e9ad7-01cd-32c5-9dda-cddcd60aaefd | -8.61776 | -51.5797 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96de3aeb-7ca5-31ba-9eab-ceb27fe2b925 | -10.43092 | -51.82824 | 2025-06-27 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48093668-84e6-31ab-abe5-b314ad5c6b43 | -9.23682 | -50.0328 | 2025-06-27 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4cba282-e351-31ab-a5d3-046027c56554 | -9.07448 | -49.43154 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 12f448e4-c8d5-3602-828e-3fa6d01a1fbc | -8.54495 | -55.03737 | 2025-06-27 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34b160c5-c517-337a-b218-439133ce0c9f | -9.97117 | -48.24312 | 2025-06-27 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bab4f2e5-0e29-3460-be66-679529a9996c | -11.0657 | -55.38261 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e4d9fa3-6d47-3482-a91b-8fa001b27bc8 | -14.04251 | -50.51883 | 2025-06-27 04:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67470082-f9b4-309b-a886-9c86088b725b | -10.64061 | -46.7059 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27243009-bbed-331d-a42f-3e1a8f3ac4b5 | -8.62058 | -51.5705 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b37ac0c2-b777-3a04-bab3-ee82252f8ce9 | -10.71205 | -59.13747 | 2025-06-27 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41c66e16-5361-3293-b472-8462aacb9360 | -11.81032 | -47.52538 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2330ea2d-f5b1-357c-bbf7-0ff0c7beecfe | -10.87478 | -53.76539 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd13f672-17db-3f0d-aa8f-40ab8ee4a2f9 | -10.24661 | -47.6804 | 2025-06-27 04:21:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083d4362-c092-3083-9a18-7e6e64d62015 | -10.54292 | -46.35725 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88b84900-0067-3bc6-b8d5-9d58cb2b09f8 | -10.86338 | -54.29921 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d69fc5-84d5-340b-96d4-16321242da70 | -11.06948 | -55.07056 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62bcfa3f-fb77-381f-ae84-ddb374c9c533 | -10.86283 | -54.30213 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d091e3f6-bb05-3101-a2ad-692468571b51 | -14.40904 | -47.89462 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f45008f-5eef-3d4b-a22b-22dc4f588aea | -11.60159 | -55.54468 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 042b53ff-ef77-32b0-bc56-fcdf9b03c5f3 | -14.21179 | -45.50531 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c700fb53-ce8d-3856-bccf-e4b6a9ea7117 | -10.29563 | -57.13151 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17ba00c2-5acb-3272-af50-49f8defa0023 | -14.20791 | -45.5084 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da32b6c1-8feb-300d-b90c-9fb1030966d3 | -11.60736 | -47.76453 | 2025-06-27 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5924663c-03c3-3870-957b-6bbe01d67792 | -12.00704 | -47.16486 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dde06db-f860-320b-b0ea-bf360af963cf | -9.07148 | -49.42632 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ed699cf5-c939-39d9-9109-9df16ae0cc1d | -9.11763 | -49.43182 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 444658c6-dc7a-33fc-87f5-d6ba0af18484 | -9.36905 | -47.63161 | 2025-06-27 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24e8381e-f41c-3600-96a8-b607c7d65880 | -13.5832 | -45.25791 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96d2070c-a8ad-3f75-82b3-179318d24041 | -11.57991 | -52.11434 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 3ba4e7f3-a78d-36a8-8154-382599625edc | -11.36448 | -48.71103 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 40f27090-d702-3c65-9139-da4cf30934c1 | -14.23625 | -45.50179 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6367e143-5d12-327a-ba7c-851678cf9595 | -12.01037 | -47.16541 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1c8a632-4fc8-3b47-a944-c4207cdc7751 | -11.99819 | -47.15606 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90966e62-ccce-397d-9d7a-cfc0464f8d06 | -10.30385 | -57.12591 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b36b46f7-46f0-3fdd-a71c-a78f2b715bc3 | -13.93477 | -54.49965 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5dd85aa8-a79b-38ca-8589-4e926764342a | -12.0255 | -57.08646 | 2025-06-27 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17a81cce-cdfe-36e8-b733-2ab097ba00f0 | -10.30686 | -57.13865 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| badaa49e-1cc1-33b7-83ad-b715c68f212a | -10.16932 | -51.65199 | 2025-06-27 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 337c9872-479f-3547-af4b-7052184f026b | -13.64588 | -46.81187 | 2025-06-27 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8427238-1fda-352f-9442-843e5bbe8b87 | -17.0482 | -43.7771 | 2025-06-27 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8050f360-1fe0-360d-8e2c-009a36539544 | -13.9475 | -54.485 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b3f85cb-3bc7-3cff-8e23-006a00eb5ba1 | -11.44782 | -54.46509 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6a4791d-2547-3d2f-8c5a-67d3f07d86b7 | -15.62187 | -46.46406 | 2025-06-27 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c25ec8-80a5-3aa0-812a-567b56e8f422 | -17.04429 | -45.89156 | 2025-06-27 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9703f628-7b0d-31ad-b4cb-2a4b5a86cbf4 | -10.27569 | -47.61152 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc64ec2b-8299-3220-969d-0955893a6fd6 | -11.77963 | -55.04217 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b29ab891-a04e-3818-b85d-f99cce0a98c8 | -12.42952 | -43.72541 | 2025-06-27 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 139d1f77-9f60-3ce7-a115-c02cc58c8590 | -15.16539 | -47.46685 | 2025-06-27 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f86fd766-a2a5-37c7-acad-1b07e569bb3b | -10.24721 | -47.67666 | 2025-06-27 04:21:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f9bee6f-3f4f-34f1-ad20-18ef847e8faa | -9.076 | -49.42236 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92f0ad8a-5c39-35a5-997b-ec5dca33cbe3 | -10.85386 | -54.04333 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0882f3ba-e0ab-33f6-8376-32e3d9a84530 | -12.13863 | -54.66797 | 2025-06-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5b46bbb-5a76-3d3f-86d2-e70683531121 | -15.08039 | -48.94382 | 2025-06-27 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35fae74a-3f36-3d07-9c5f-e85419eac61c | -12.04879 | -48.07529 | 2025-06-27 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b307d69-3f93-3730-9da0-ab7b2036861c | -10.83441 | -53.74866 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0f84703-2311-376f-9074-a12c5c2bfc69 | -14.31509 | -59.89313 | 2025-06-27 04:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42920f87-1723-380a-8c53-31b5be8dec3c | -11.82392 | -47.53862 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0fae7c7-544b-351b-b79a-cc7c842044b7 | -8.61412 | -51.57477 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3085c989-8eed-3058-bd41-6ee72533ebe7 | -10.83329 | -53.74627 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47e7f06b-bee2-3621-9832-e112e1bcd18a | -11.58787 | -44.64285 | 2025-06-27 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b95e95e-e0f4-3683-9f66-bc598262fa02 | -9.82533 | -48.37697 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ebbf269-bf40-35a3-a9b0-7de8712036ed | -13.94063 | -54.49502 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 26c52377-ae3d-3a47-9345-aaee1b49e2c6 | -13.04716 | -48.81938 | 2025-06-27 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d87b9cc1-6b71-3bde-b392-a7ba057db3e2 | -17.04788 | -43.77861 | 2025-06-27 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c038f80-d251-30e2-8c36-32af6ffe017c | -12.03073 | -47.77711 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c0507294-ca6f-3c3d-b94b-161873c384dd | -12.0522 | -48.07588 | 2025-06-27 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27fcc783-6842-3cf2-8c72-78f083d9741b | -13.06118 | -51.6435 | 2025-06-27 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 32789877-d057-31b9-969d-d64eb2daa005 | -11.5822 | -52.11136 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| cadadb2e-ba00-3171-8a46-ef612c8ab7f3 | -14.21458 | -45.50946 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56e15966-7045-3516-a44c-256443b92340 | -17.04765 | -45.89209 | 2025-06-27 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 696781db-1338-3385-ba1b-a2dad33f36a1 | -11.77227 | -55.02415 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b7df84-d8c1-3355-8982-d84dfb8a2b49 | -14.20457 | -45.50787 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5be7b915-2529-3dd8-af9c-f30fcbbea55a | -16.70299 | -44.97769 | 2025-06-27 04:21:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1728e746-8e94-35ef-adcd-df0143d2f5cc | -11.05559 | -55.37717 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 61e6a2d2-eed5-38d8-a7f1-4907990f15fa | -14.41315 | -47.8692 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1803cfc-d837-3911-8910-a000434afdf8 | -12.00094 | -47.16019 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b95e67-6ab7-38ae-9c97-acb30af96ca7 | -13.04368 | -48.81879 | 2025-06-27 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 377f98f8-7221-3011-b8ad-144b3d6b8343 | -12.65412 | -54.10621 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c06a792-4440-327d-8538-4fce05e258dd | -11.68216 | -46.72736 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f6b9cc-9ed9-3fa4-b06e-83404c8c5a3f | -10.8286 | -53.75311 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c179224-92da-37cb-88c4-40e1b779b2a1 | -9.073 | -49.41715 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 392c3a3a-22a8-3a98-8952-a067b6b3d899 | -11.36867 | -48.7076 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61dab1ed-aa11-378e-a8a6-c3d7ff5c422d | -11.58076 | -52.11967 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 62e5d144-e61a-3772-aa3c-a6d8880412ca | -11.57435 | -52.1057 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 24ace259-97fb-3dd8-befa-50ff774f8711 | -9.78986 | -48.5669 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 787332f9-d9ec-36da-bf07-52b78be6bfec | -9.09338 | -47.967 | 2025-06-27 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4020a634-f27c-39ce-a433-5db09fd7b9d6 | -16.25276 | -46.29432 | 2025-06-27 04:21:00 | NOAA-21 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a14baa0e-d86f-3cda-93a4-e83eceef8894 | -8.73501 | -50.26109 | 2025-06-27 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 120a4a74-d562-38fc-bd2a-48df59d168a4 | -12.11234 | -54.6692 | 2025-06-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51b90163-a6e2-3ce7-be35-bc7e4068577b | -9.75216 | -48.04416 | 2025-06-27 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20a1d117-43a6-3bf1-8f7f-6916ec0bed9e | -11.57411 | -52.12193 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 573c2683-325c-372f-84c3-83c3db298d89 | -13.04302 | -48.82275 | 2025-06-27 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 108f8d25-dd2b-3ac8-9965-41b2bfdc0d40 | -10.43163 | -51.82416 | 2025-06-27 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e83498d-733b-3fc2-a8fd-5fc9dc9447c1 | -9.35143 | -58.85491 | 2025-06-27 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a633c30-51be-3ae9-a41f-0a589f194fb7 | -11.56506 | -52.10832 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5f46367-f0a4-3f29-9449-8ada56fb0dda | -13.28749 | -44.60536 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d785cb1-70ae-3f7f-bc1b-612e9861834a | -10.86894 | -53.76991 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d7aa75c-83ad-30f0-a107-c8b4b0ddde70 | -12.12964 | -46.60953 | 2025-06-27 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
