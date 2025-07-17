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
| 2ced255d-8aab-3674-bfc9-95274a502b99 | -8.5287 | -47.832699 | 2025-07-17 00:21:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32698fd1-a5fe-3107-8413-874e843a8ccf | -8.0327 | -49.859501 | 2025-07-17 00:21:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6d1f64-58e2-3049-a11f-cc4badf6903d | -3.0241 | -47.848999 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988f78db-8d27-30ef-bf2c-d4332f22b4a2 | -6.8401 | -42.742802 | 2025-07-17 00:21:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7a4cc5d4-6225-36e6-b9ea-9feaba2a64bd | -11.665 | -43.763599 | 2025-07-17 00:21:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be905add-92e0-30fa-a7b5-b7ad3f12eed1 | -4.8034 | -43.216801 | 2025-07-17 00:21:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19590e77-3e38-3195-a58a-c29206a7e337 | -5.7904 | -45.105801 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcd75c7-64b1-3171-83d3-477c1ed8d503 | -12.0914 | -48.178299 | 2025-07-17 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f30b059-d208-3260-a364-c25d12c75e3a | -6.7171 | -44.329601 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cb44668-20ac-3504-94bc-bc006a3e398a | -9.2365 | -48.563499 | 2025-07-17 00:21:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0037a189-0e2a-3f2b-b2ce-d08e5b64c3bd | -2.9029 | -48.222198 | 2025-07-17 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbc7910f-099c-3978-8de5-8dcb51e3b3db | -6.9685 | -42.807598 | 2025-07-17 00:21:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d22265bc-062c-30f4-a5e2-339124baabc0 | -8.6991 | -50.0266 | 2025-07-17 00:21:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e858672-fc25-3b8e-be45-4e1700413658 | -20.180401 | -48.717999 | 2025-07-17 00:21:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fe00eb72-0ef1-35d6-8955-d10b7ee3acfc | -5.5229 | -43.881699 | 2025-07-17 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96e22059-3d25-390e-8f78-fcc087330b41 | -8.0987 | -43.151501 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1398d3b-76cc-3b3f-86cb-659a6d5986fd | -12.4118 | -50.025799 | 2025-07-17 00:21:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04d28edb-b2b7-3b29-9127-30a48fa0afe0 | -3.038 | -49.413502 | 2025-07-17 00:21:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7711cb0-123f-3399-92ec-fdabb0b03f73 | -21.0746 | -48.668201 | 2025-07-17 00:21:00 | METOP-C | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc55e49e-9532-31b2-a8fb-37379a972916 | -5.5634 | -44.285702 | 2025-07-17 00:21:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83d273df-dce8-3b57-a2ab-bdd2530d5622 | -8.5385 | -47.830601 | 2025-07-17 00:21:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f43bb641-faf9-38fa-85d9-24748f0b7a60 | -5.6599 | -43.7141 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98aff720-4861-3ec7-a427-6f925fffa2d1 | -11.0992 | -48.8479 | 2025-07-17 00:21:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6f2b49-1372-32fd-aba9-1317e6f7969c | -9.1082 | -44.294102 | 2025-07-17 00:21:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c2307ca2-b153-3679-9646-b3a476e947b3 | -3.3777 | -47.457401 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef1159fb-e9f3-3904-bc44-8a4c1db4114e | -22.6045 | -47.212002 | 2025-07-17 00:21:00 | METOP-C | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 249f0159-5b56-3482-86c4-99b6ac510e7d | -6.3021 | -46.331699 | 2025-07-17 00:21:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fe238d2-3e70-3722-81a4-287aed416bb2 | -9.4063 | -48.401901 | 2025-07-17 00:21:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffa0dec5-6684-3ec6-bef0-cf212f892618 | -9.2463 | -48.561501 | 2025-07-17 00:21:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13abf26e-d0fb-32fa-98ff-100c65909c38 | -6.9792 | -43.758202 | 2025-07-17 00:21:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc0e41fe-c1bc-3a60-9481-dae672d145e3 | -6.9783 | -42.805302 | 2025-07-17 00:21:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 77cb8111-7921-3113-86dd-00509e4fed10 | -6.3366 | -43.742802 | 2025-07-17 00:21:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da453e5a-277c-3bce-af07-fc32d4cdcbf6 | -2.4426 | -47.326 | 2025-07-17 00:21:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7170eddf-f266-346b-bb94-f7041da0c362 | -8.0972 | -43.1446 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8aeec69a-d77b-35c0-aa79-9a77bfe372e8 | -7.0866 | -49.157398 | 2025-07-17 00:21:00 | METOP-C | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d2b8ba88-c8ec-3e09-a04c-947de37e79ea | -7.1924 | -43.110298 | 2025-07-17 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cae130c8-0d5a-39d4-ab12-363ac65dce42 | -3.9908 | -43.226799 | 2025-07-17 00:21:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5e7797e-ebb2-325d-b68b-2f5fbac6b30a | -18.843901 | -45.196602 | 2025-07-17 00:21:00 | METOP-C | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f51e81b5-20f8-312c-b16c-bd42183a6244 | -12.0251 | -47.7561 | 2025-07-17 00:21:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b920525-9ebb-3432-bdd5-6deaeae9c6fa | -5.7838 | -45.076801 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5931e54c-0b6d-3fc2-a139-64685a7552eb | -5.7969 | -45.0891 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f63e91a5-119b-300f-b76a-533d44599bdf | -8.5408 | -47.841301 | 2025-07-17 00:21:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9061fe64-70aa-39fe-8b9f-38d05e3129a4 | -4.5888 | -43.315399 | 2025-07-17 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 456d057d-01e3-3fd4-9c36-d327d9b24c3d | -9.4933 | -40.383598 | 2025-07-17 00:21:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bc1348a2-85ed-33c5-a1b4-290edd27e820 | -3.0159 | -49.406502 | 2025-07-17 00:21:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9651a46-f1a7-341a-a541-bcf1ef544600 | -7.1826 | -43.112499 | 2025-07-17 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f2e1e3b4-6b5e-36af-81a6-0ccc2ddd8f99 | -20.170601 | -48.719898 | 2025-07-17 00:21:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4e017e-e66c-3366-a843-ade2843bcf86 | -4.2925 | -48.097801 | 2025-07-17 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98127af-0e55-3d62-81cb-9b5a316584af | -6.7285 | -44.334499 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb85152-4d56-37e1-9fee-ce66ca42134b | -4.6445 | -43.108501 | 2025-07-17 00:21:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2117b02e-3b76-3d23-bfd1-83a5bafafa52 | -14.0183 | -51.198002 | 2025-07-17 00:21:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cafc942-1b4c-3b0c-bab5-3ccaa6c7a980 | -8.8769 | -44.7803 | 2025-07-17 00:21:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8947e59-2d29-3bb2-9380-748f3427dbb4 | -12.4084 | -50.008598 | 2025-07-17 00:21:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9096d1e0-591c-3554-8a5d-c1c5fcb8ed5a | -5.5244 | -43.8885 | 2025-07-17 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 944db4d2-1b0d-3af0-9ce0-10fd204a29f6 | -3.0339 | -47.846901 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06f6f210-41cc-32cb-a665-e7a660561fe7 | -12.7035 | -46.7952 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4edf01d0-2e1f-326c-8a51-d3d6bd3df154 | -4.3023 | -48.095699 | 2025-07-17 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be31c079-1536-3d45-80f9-84571dd4a1d6 | -7.7175 | -44.748199 | 2025-07-17 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5e1258-858e-3385-ae75-837f0f91d164 | -5.7888 | -45.098598 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1f653a-a844-3208-9725-10c94d4f04dc | -5.7871 | -45.091301 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75fc922f-d12a-39d6-ae2f-b215ae48eb39 | -12.6915 | -46.786598 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 314b8a18-74eb-3a31-9d73-c6844d8ba91d | -11.3558 | -48.710701 | 2025-07-17 00:21:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b977dfc-9c45-34e6-b527-e555422b2ddf | -9.3125 | -44.843201 | 2025-07-17 00:21:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f82de19-5aa2-3b98-8779-45dc8fe04b1d | -4.2904 | -48.0882 | 2025-07-17 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb8391f-25cd-3afb-b71f-6d24cc2cf008 | -4.805 | -43.223598 | 2025-07-17 00:21:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14a8e295-6227-3ace-85b2-959422dc06c9 | -6.7155 | -44.322601 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1ebcea-5f27-3b63-bcba-6797a3cf9aeb | -13.0025 | -44.862701 | 2025-07-17 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10f5a134-ee89-3b73-9778-41ee6571c976 | -11.2376 | -49.475601 | 2025-07-17 00:21:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbbdf28c-4592-3294-b526-97161088baa0 | -8.531 | -47.843399 | 2025-07-17 00:21:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5be3a173-f95d-3d6b-8d09-9a3bbd5a7be5 | -11.6634 | -43.756199 | 2025-07-17 00:21:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebec9c6f-21b3-3670-8b8f-5ff7d61a13f1 | -20.1675 | -48.7015 | 2025-07-17 00:21:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcee46f-4730-37a6-80ef-7c030699a269 | -6.7041 | -44.317699 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e22c113-47b5-32b7-9d7e-b5f5922120eb | -3.3718 | -47.476799 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91084dab-1bfa-32c4-a702-202f7ee4775f | -8.7023 | -50.041599 | 2025-07-17 00:21:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed0cd92-9433-31ee-8641-cfd364a69fbf | -11.1089 | -48.845901 | 2025-07-17 00:21:00 | METOP-C | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a714d877-f851-3418-a26b-9a6c8f3cfba6 | -5.6567 | -43.700401 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1c3b564-b056-381e-8114-4f8c18d109f6 | -6.3003 | -46.323502 | 2025-07-17 00:21:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b91d3dfd-7a2f-3c8c-8823-441cd9ca9e5c | -12.0276 | -47.768002 | 2025-07-17 00:21:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fadb036c-5d74-35a7-8fa2-0733a72c6865 | -19.443001 | -48.522301 | 2025-07-17 00:21:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1d979630-5ca3-3342-bb32-5ece53bd42e8 | -11.102 | -48.8615 | 2025-07-17 00:21:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4b162af-3bd2-3e5e-b811-d9806ce0d121 | -5.5311 | -43.872601 | 2025-07-17 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32befb20-22b6-332d-9ab0-094f7fbc593b | -11.3968 | -42.286098 | 2025-07-17 00:21:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a0890d05-8950-3a7c-b655-931eab05249b | -5.5327 | -43.879501 | 2025-07-17 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27bd352d-d5be-304a-a316-8b6902553ee7 | -5.6697 | -43.711899 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79a64711-d4a2-303e-a52e-87146282a7d6 | -3.3953 | -47.489799 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b475d82-d483-34a9-a1a9-70011fa4a415 | -8.1168 | -43.140099 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 976240b7-f53a-339c-8f41-e1b92fc052b6 | -6.7253 | -44.3204 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12ce0c5f-1339-3074-9f35-215315a27223 | -12.9927 | -44.864799 | 2025-07-17 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59bc17c2-ae3a-3aff-a3f7-b8fc42397e48 | -6.3162 | -43.6534 | 2025-07-17 00:21:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 240ef9c1-950b-3bf3-ad19-83bd2ab1be22 | -14.0239 | -51.1744 | 2025-07-17 00:21:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14d9e453-cbf7-3129-9125-9f4e9263c195 | -5.5929 | -45.7822 | 2025-07-17 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5eb6de92-a39b-3602-a896-175d9e32923c | -6.6298 | -49.736599 | 2025-07-17 00:21:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9778b19f-84e4-304b-aa4f-c6c882af50b7 | -12.7057 | -46.805801 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10c5ef9e-1043-3142-b1e7-c426ae6ce064 | -12.4799 | -46.897701 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04b3b9f0-0e8f-3c6f-8b44-f783193d4ff7 | -7.3366 | -44.199001 | 2025-07-17 00:21:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 53f9a58f-a32d-369e-b281-f613b4dd76f7 | -12.4712 | -44.491299 | 2025-07-17 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f4eb45a-7610-348e-b54b-d6073c976407 | -12.4729 | -44.499298 | 2025-07-17 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5862e775-ab48-3a13-85bf-ab8e61355197 | -7.6154 | -44.293301 | 2025-07-17 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fcad6c70-b710-3655-bc4c-e467fa62d1ee | -2.4407 | -47.317699 | 2025-07-17 00:21:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7103295e-283c-326e-9824-2cbf4143fdc5 | -22.591999 | -47.197899 | 2025-07-17 00:21:00 | METOP-C | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
