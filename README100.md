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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a5836db-acc1-3ae5-8fdc-bd08c3c30e8b | -9.43503 | -48.88376 | 2024-10-24 05:23:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 229d5fdb-c3c0-38c0-8fe5-9e439b7574db | -9.43439 | -48.88193 | 2024-10-24 05:23:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d682782a-b5f9-3743-b97c-42437c52e8ad | -9.26923 | -49.57605 | 2024-10-24 05:23:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6b5628b-6a54-3fdc-ad69-78d16d0fba6e | -9.26862 | -49.58096 | 2024-10-24 05:23:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7057ab50-cda3-353f-86ec-ac5cda768918 | -8.57887 | -49.22196 | 2024-10-24 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5283e536-2c06-3bfd-87d9-6d93c31af366 | -8.57823 | -49.22692 | 2024-10-24 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc2dcf6e-a7d9-33fb-b7cc-a105beda2292 | -8.25986 | -49.47694 | 2024-10-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577acb36-023f-3f49-a1de-18ca70adef6a | -8.15155 | -49.29867 | 2024-10-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb02ec1a-18ef-357e-8804-6240c8aa0cd9 | -8.05869 | -49.37812 | 2024-10-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5904e4f-2eb7-3039-bd8c-bf77b38b6cd2 | -8.05807 | -49.38304 | 2024-10-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f317f3-c1e2-38cd-913b-ab4abc75c07c | -8.02044 | -49.6348 | 2024-10-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6af8831c-dacb-3e22-9271-bc3647907bff | -8.01981 | -49.63955 | 2024-10-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c595151-64f4-3913-bb3a-d569dd904612 | -10.87364 | -49.53821 | 2024-10-24 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ed049a-fda7-3553-845d-821fe717fe4f | -10.873 | -49.54358 | 2024-10-24 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 399d2bf2-e305-3d1a-9da0-76178ab6131c | -10.86726 | -49.53725 | 2024-10-24 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4221aac1-61a1-3460-8764-58e7a637f5e6 | -6.22373 | -50.8758 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f1f89c6-f3fe-3171-b837-5235ee1801c9 | -6.22322 | -50.87946 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a872ca49-202a-310b-8e45-af47bae33d10 | -6.22272 | -50.88301 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfb430e8-833a-3ddc-a5ef-ed8065dc76ec | -6.2177 | -50.87866 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d8059c1-02d5-329a-a2a4-6210a7aeeb67 | -6.2082 | -50.86598 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47fc0bd4-2a17-3ae9-b393-6a2c94a1bcf3 | -6.20771 | -50.86949 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4648a43d-b1cf-3d76-b2a5-e55ceea50c79 | -6.20267 | -50.86523 | 2024-10-24 05:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcf45a02-52eb-3cab-8e25-6b2ff45d9d33 | -5.9482 | -50.87601 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b418aab6-28b3-3d36-9a50-595dbbc8477e | -5.94819 | -50.87474 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c274217-96e2-3278-88ae-4f164ecc4b67 | -5.94773 | -50.87796 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9b49c5-560c-334b-9bb2-b25bd7943219 | -5.93105 | -50.9943 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ef1ca00-2ae9-313d-b940-5a45e204f740 | -5.79466 | -50.16626 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc02477a-0d32-33a0-9ebc-af616ec020c7 | -5.79408 | -50.17036 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea945d71-6fd0-38fc-acf5-0e4679efde1a | -9.18219 | -50.54552 | 2024-10-24 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8743d65b-4ebb-3441-9f14-f156d132d9ef | -9.18163 | -50.54977 | 2024-10-24 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f29d873-724f-3d15-97db-3d08fe696c9f | -8.06222 | -50.99844 | 2024-10-24 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab132b1d-b7f4-38f8-89d1-2e7146dc08b4 | -8.06172 | -51.00213 | 2024-10-24 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d3e60e4-ebf8-36fd-8c53-83de10b8d464 | -7.99117 | -50.69199 | 2024-10-24 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0175dff-544f-365c-a00a-cc97915186f8 | -7.99064 | -50.69593 | 2024-10-24 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ece8f3f-0bdd-3308-9574-ca2544b6f878 | -7.98544 | -50.69126 | 2024-10-24 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66ae1930-b339-3414-a031-6b82279c4633 | -7.98491 | -50.6952 | 2024-10-24 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dd9e66a-0f2f-3793-b9f7-ede1214d63c5 | -9.37686 | -51.88798 | 2024-10-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5341060d-334c-3e69-8c57-8d5a5b30ead7 | -9.3715 | -51.88695 | 2024-10-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bdb0b15-2526-38a9-8d9f-0d304f320132 | -9.37101 | -51.89074 | 2024-10-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd952773-7f9f-3a6b-9ec4-b1387d43c106 | -10.09876 | -51.13211 | 2024-10-24 05:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09fdfcc4-4876-3052-9945-e87d91fd4fd2 | -10.09505 | -51.12928 | 2024-10-24 05:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6999d590-a94f-3971-9d1e-4c65def542ba | -10.09456 | -51.13328 | 2024-10-24 05:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d62a4b51-de78-3fea-be6d-1253ccc1c9c1 | -10.09304 | -51.13131 | 2024-10-24 05:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 387a5356-ebc1-3005-84a3-7a4e0842157c | -11.09779 | -51.55305 | 2024-10-24 05:23:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38c88ed0-05a6-3c71-b7e2-dfaeff5cbd65 | -11.09729 | -51.55692 | 2024-10-24 05:23:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11b51836-eafa-3e06-8d92-95df36061669 | -11.09516 | -51.55445 | 2024-10-24 05:23:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3b0fe101-2284-3e65-b471-975cb3fdf14c | -10.27018 | -52.17572 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1f3d2bd-4a4e-3e2d-a924-8de3ce5b633e | -10.26782 | -52.17525 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c01e41b1-b442-378d-ab48-8a2338a824f7 | -10.2674 | -52.17867 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13e0430d-2b66-3c8c-998b-ff89c933285a | -10.26438 | -52.17837 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef54a6cd-f54f-36db-91b0-138901ddfc81 | -10.26204 | -52.1779 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86bf237-e1c4-37f8-8159-c47245755ad2 | -10.9947 | -52.88673 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0505d683-2dee-31cf-aac2-4385385a9814 | -10.98953 | -52.88612 | 2024-10-24 05:23:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 15a47e5a-4b72-3ef0-9921-ffa402cdbb25 | -18.17178 | -56.31372 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7871a077-ec90-39b5-9066-fff7a02e25ed | -10.31891 | -55.03336 | 2024-10-24 05:23:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f457b8c-c6a8-36ed-8490-b6b11c0c0894 | -10.20272 | -53.86937 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b90acc6-78dc-3c2e-abbc-e7e653e1fc59 | -10.20203 | -53.8745 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c814f9c-0a53-34ad-aa96-a6f4c5a57355 | -10.19794 | -53.86877 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 918e7bd6-68c5-30eb-80e7-bb8f3a8e259d | -10.19726 | -53.87387 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f421e13-dc88-3ae6-9281-04af3843acd1 | -10.19658 | -53.87896 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2758584-b59d-3d4c-8d61-1f5d70844f6a | -10.1925 | -53.8732 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 758d6825-a7f2-3098-8297-00e529b0414b | -10.19182 | -53.87829 | 2024-10-24 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b56d07e-dba0-35d7-9467-95b425f8d0ba | -11.42275 | -54.30653 | 2024-10-24 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62c60f5c-0c3f-34f4-a6a8-610d8ac057be | -17.02625 | -56.0038 | 2024-10-24 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e426c1f5-1c81-31e3-b5d3-6c98629381be | -17.02112 | -56.00797 | 2024-10-24 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 64b7c998-5405-3393-826b-de34edb3f89c | -16.91904 | -56.43414 | 2024-10-24 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 252c505c-66fa-338e-92ca-178e89641a1d | -18.31967 | -56.21141 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fe58fdd3-ec89-3464-8037-bed15eb71f26 | -18.31911 | -56.21624 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bdc7d287-953e-35b9-98f8-d6835b99ad52 | -18.31888 | -56.21431 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5439ba6a-1ed4-3aa6-bd6d-cf78e11d3688 | -18.3155 | -56.20403 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8df13e95-fb08-3f7e-9f64-8e507ee45701 | -18.31228 | -56.15422 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| da23ebbd-76bc-3a32-a6f4-889cbf0c647b | -18.31196 | -56.23301 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 646ce108-7d79-3f49-9f6d-6820d62d57d4 | -18.31137 | -56.23782 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| fc53ee84-e5ea-3415-a658-069c26cc0a7e | -18.30741 | -56.2324 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 18e5aa12-cbd6-38cc-bffd-b158b841ad8c | -18.30682 | -56.23722 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d71f093c-205e-3348-a203-a699a8db6954 | -18.30286 | -56.23181 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 6cc90602-577f-3e94-88e1-8b3efa4a5aab | -18.28899 | -56.07647 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a0f27936-6dc5-3307-8f9b-d34f36586ffb | -18.26888 | -56.04879 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 8524c22e-809d-32a5-969d-3a16bf25a784 | -18.26427 | -56.04818 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 20a3f156-02bd-3082-92e5-b134f9c2e3ce | -18.26369 | -56.05313 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 70e5a070-1a5c-3f2b-9c32-e5a5cbfbbaf3 | -18.26312 | -56.05807 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 32987fd0-ed4d-3e98-9869-361448ed0fde | -18.25851 | -56.05747 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 61f1b8b3-c963-313b-828c-cb8a3c96d6f0 | -18.17236 | -56.30898 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 8e0ffe45-bb6f-33e4-b0ce-d843c73b7760 | -18.17112 | -56.3568 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2cb3c242-5f4f-32c3-9c58-c8ec8fe3a21f | -18.16726 | -56.31312 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7048af35-516d-331e-b09e-6953c218cd8c | -7.30694 | -55.30949 | 2024-10-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2bcafda-0bb0-326e-9c44-cbd8fd369702 | -7.27208 | -55.3466 | 2024-10-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4356a149-08ca-3cd4-aaf9-cdc04dad847f | -8.30648 | -55.1102 | 2024-10-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6ba1eae5-3783-3629-8726-5c5499d6d737 | -18.11487 | -57.3265 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 83d6a569-e89a-39b7-bd94-b131fc62d30c | -18.10592 | -57.32942 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 19c5eae0-027b-315f-bcd7-39e1f4707346 | -18.10542 | -57.33348 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0e4684f2-9c7b-30bb-ba73-504cb93504b5 | -18.09647 | -57.33638 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e85ec41e-051c-3f3d-83e6-7d83df5f0dc8 | -18.09597 | -57.34045 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 883ba452-876e-33e1-aa65-f8853231d544 | -18.09175 | -57.33987 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2d320c80-2e48-3219-a616-8562aca1c4ad | -18.09138 | -57.30746 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a41fe298-3836-3c51-9a23-1a3e180ffce1 | -18.09125 | -57.34393 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c449b5c7-faee-3c94-a555-61a069152e28 | -18.0883 | -57.2979 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6aef2c55-1e81-3b32-b840-434920b57b3c | -18.08821 | -57.29871 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6ac77ac8-d058-30a5-9dae-036bcd248f74 | -18.0878 | -57.30199 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3aa3d67a-c4ec-3328-bd8d-8cc81a04f110 | -18.08769 | -57.3028 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README101.md)
