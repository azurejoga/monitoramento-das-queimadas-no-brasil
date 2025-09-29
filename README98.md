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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6c37816-d094-3e5e-90d1-f035c8377498 | -15.0524 | -45.073 | 2025-09-29 14:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3ead006b-d418-39e9-a86b-16bc4bbeb783 | -6.0623 | -42.466 | 2025-09-29 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 2a685bd8-8787-3906-a38d-6b240b77ee34 | -7.7416 | -46.9626 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e2969d9c-5da5-3e00-872b-7d14966f2fb1 | -7.8375 | -46.7766 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 7107f1b4-14ca-303f-bb2c-670f79fd688e | -14.8902 | -51.0678 | 2025-09-29 14:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| dfb4bb0f-42d0-384d-933a-4d55db255513 | -12.887 | -44.6846 | 2025-09-29 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 07b3af9d-c30d-3fa0-bc1f-7a49c7168604 | -8.2665 | -45.4791 | 2025-09-29 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1d1d79d8-0961-3a35-85de-dcf04d43adc2 | -11.3834 | -45.0312 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2ee891f7-1c25-35ca-94fa-7b44abc2d155 | -7.7414 | -46.9848 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 43e1ed22-a96f-301b-b8f1-1837ba97dc74 | -17.4055 | -47.1199 | 2025-09-29 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 4065e57f-7221-32c1-930d-d3d0a478997e | -4.5798 | -37.8505 | 2025-09-29 14:20:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 4f1bf224-0d15-3460-a698-f0b5aeaaff32 | -7.8163 | -47.0003 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 196.9 |
| c3803263-7366-3bb8-b98d-c769f6a13e85 | -8.71 | -54.6467 | 2025-09-29 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| edd293b0-9b1f-3151-99d0-ec3932f97e0e | -13.3154 | -50.7227 | 2025-09-29 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 71922741-4815-342c-af63-b9c7e22b5851 | -9.9585 | -43.5752 | 2025-09-29 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 22b98b96-534f-332a-b929-ccf7e24cbf19 | -14.8693 | -47.2032 | 2025-09-29 14:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d23d370c-a851-3f7b-93f2-5839979e7418 | -5.1885 | -43.7495 | 2025-09-29 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d906f952-3964-3a23-8a2b-11a87b270b18 | -7.3074 | -47.2649 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5cfcc278-b5f8-3284-9d33-4759196b81d5 | -6.0811 | -42.4644 | 2025-09-29 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| b334b0b4-a8dd-3042-bed2-1d076669bfd3 | -9.4196 | -54.6767 | 2025-09-29 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d5f6058c-2da8-3cac-87ad-dab9e688466c | -4.1574 | -44.2726 | 2025-09-29 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b5b5cdc3-2424-39a0-8463-9be8b6e159e8 | -9.2631 | -45.7352 | 2025-09-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| cf4c7827-a5b3-3d48-bd53-e99ba067e484 | -14.7176 | -45.2057 | 2025-09-29 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 79fc1b2a-5a42-3b2a-af45-b36b71fb520b | -7.0293 | -45.1873 | 2025-09-29 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 0eb17c32-e08e-38c9-996d-52945d9b0c9f | -9.4901 | -48.53 | 2025-09-29 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f8b38138-58c5-378e-8184-ce0db5f787e5 | -9.9581 | -43.5987 | 2025-09-29 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| fc11fac3-dae0-3647-869a-3c35af9863fc | -9.301 | -45.7309 | 2025-09-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1835402f-fb38-3d59-aa1f-612d6487df70 | -6.8259 | -44.9091 | 2025-09-29 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 70997616-0dcb-3049-b80a-26718312ee75 | -8.2474 | -45.5037 | 2025-09-29 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 9df194e6-ba6e-333f-940c-c2f5578e42f5 | -10.6239 | -48.5386 | 2025-09-29 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d46c9ccb-94f1-361e-a240-a67292f506b6 | -5.7413 | -42.6576 | 2025-09-29 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 7c04dc5b-bc20-3800-b99e-43df69d402bb | -9.0874 | -47.6074 | 2025-09-29 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8c09cacc-8041-3359-a469-4f2671cc36b4 | -7.2813 | -42.8269 | 2025-09-29 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.9 |
| 923edb15-64e4-3376-aa9a-e37a962600c3 | -13.011 | -49.4423 | 2025-09-29 14:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b6e190e3-6ad1-3ebc-9a2c-441937c705b2 | -7.6062 | -47.3498 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 162174f8-115e-36f8-85be-84ff9cc2d1bf | -13.7889 | -47.9181 | 2025-09-29 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c4ec56d5-8491-3f0a-b781-4c4e32dcf18c | -12.9543 | -45.185 | 2025-09-29 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 7a5426f5-1625-3be5-a952-f9b4e539a92f | -5.7679 | -43.8467 | 2025-09-29 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1c9cfc79-7dd4-37ca-bd40-3c859e795953 | -7.8378 | -46.7544 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| df7fb6f4-8be0-3387-b90e-189d0c6c4e84 | -15.072 | -45.0693 | 2025-09-29 14:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 186.5 |
| e7ff0e40-4bd4-3ba1-980a-fdce8e037b95 | -15.0725 | -45.0457 | 2025-09-29 14:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7be6f48d-17c8-34a9-82b7-62d07c8a8530 | -9.764 | -47.8006 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 359172e2-b3cd-3f5a-9991-092cea26d5b6 | -9.3708 | -47.556 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9fbad83d-10ed-323d-b123-7ebdb2292c21 | -8.2662 | -45.5018 | 2025-09-29 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| aaa046f3-e8ad-318b-a5f5-55a98732b009 | -15.5518 | -41.4679 | 2025-09-29 14:20:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| 15faf9ee-4708-31c2-b3d5-e308e8efe6fc | -7.9008 | -44.5805 | 2025-09-29 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ef438100-a63c-34a0-ac2a-a3c0261b2c4e | -9.3705 | -47.5781 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 38d86986-d63f-3f3e-82eb-ccefdbc87451 | -11.383 | -45.0543 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| d29addfa-e257-31ee-a637-b1eb47b9a3c9 | -11.4604 | -44.997 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f05d5ab7-e816-35e8-95c3-a84bc578f255 | -8.5413 | -44.6284 | 2025-09-29 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 48d0914b-371a-3705-a954-06837986bb80 | -10.3896 | -49.0437 | 2025-09-29 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| b070c6ab-7ab7-3b9c-bba2-97d62b1c1a35 | -9.4744 | -45.5068 | 2025-09-29 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| da68ec3a-7888-387a-abdd-7b52906ff251 | -9.0016 | -51.6875 | 2025-09-29 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| b85c21b6-3204-39c7-b823-0111021db033 | -12.8774 | -45.1742 | 2025-09-29 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 5855efa0-a780-3254-8cc6-170dbf861902 | -9.4192 | -54.7172 | 2025-09-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| a0040ccb-7d35-35ea-be72-2f86c22d8a19 | -9.0874 | -47.6074 | 2025-09-29 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f4eaee9b-fb6c-3ed9-a77b-46b91cc791e6 | -6.5422 | -45.1601 | 2025-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 95080821-518f-347f-98eb-795fe568eb44 | -5.9004 | -43.6976 | 2025-09-29 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 79db4bcd-4bc5-3747-82d6-c27b444d8f64 | -10.7673 | -45.3687 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7047ffde-b4a4-3555-910e-d658876e9206 | -12.8865 | -44.708 | 2025-09-29 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 68aebfd2-b0f4-356a-8861-1f9991f85a4d | -8.8061 | -50.7165 | 2025-09-29 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c1effe35-f73b-3219-a71d-85464ed9e49b | -5.7679 | -43.8467 | 2025-09-29 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 81998822-7d42-3831-bf3e-43d2db5321a5 | -22.6286 | -49.03 | 2025-09-29 14:30:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 227.5 |
| c27a8b93-8bb4-39e2-999e-1c9426d6e806 | -9.4007 | -54.6984 | 2025-09-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 5c3e4f54-3645-3ab8-845d-454baab83f8a | -9.4455 | -47.6144 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b71e6043-5043-3948-8e78-699104e61d73 | -13.3989 | -48.1549 | 2025-09-29 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| ba436ba1-899c-3a44-be2a-df0d0ac1326b | -10.8055 | -45.3637 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a7d34d10-679c-381e-af7e-bbd5915cf75b | -7.5538 | -45.2989 | 2025-09-29 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5a8e43a5-9839-36a8-bebb-b2e0e7583cf7 | -10.6429 | -48.5364 | 2025-09-29 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 1b42690f-d2d5-32e5-a93a-64cfbfda8c39 | -10.8429 | -45.4044 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 272c40e8-5d49-3493-b9af-0269bc5d8bdb | -18.4667 | -43.9996 | 2025-09-29 14:30:00 | GOES-19 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 450e4f10-3761-336b-8710-ea1196384794 | -6.8256 | -44.9319 | 2025-09-29 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| ae430b1a-f6cf-3e20-9e73-1555ddb6c24b | -15.6127 | -46.2465 | 2025-09-29 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a1b020b0-5e33-334d-9b37-ee1ce5b2a350 | -8.1614 | -46.3899 | 2025-09-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| af679626-4962-31ef-bd3a-5a51b90d9c69 | -7.7414 | -46.9848 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ad5487da-f799-3dca-bd96-e92fee67866d | -10.3257 | -48.2001 | 2025-09-29 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 62390c18-468f-3851-ab6c-ed47033db711 | -6.0795 | -42.6301 | 2025-09-29 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| c605c8e5-5083-3d18-94ca-93f92ebadd0d | -6.8259 | -44.9091 | 2025-09-29 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| bebe9549-f51b-34f3-aa74-e00a9c40d4a3 | -13.3158 | -50.7011 | 2025-09-29 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c40fc224-8320-361c-b94d-1324da553727 | -8.9641 | -51.6906 | 2025-09-29 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 162a15cc-dcf4-3896-b59d-f8204d380f42 | -9.4901 | -48.53 | 2025-09-29 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 281d9af7-2a42-38d1-af6c-c9d8a4407417 | -6.4604 | -45.866 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c9e834b7-fc81-3bcb-badb-88d135bf9e65 | -4.1491 | -39.998 | 2025-09-29 14:30:00 | GOES-19 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 544b11e3-ecc7-3eb5-8a7b-118cdd4469d9 | -9.2631 | -45.7352 | 2025-09-29 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a298b092-ab9e-38da-bba6-4d5013c2915b | -12.7105 | -46.8906 | 2025-09-29 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 4e7f3a2e-1902-3399-bb38-0e9fe457f030 | -11.4409 | -45.0229 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 7b40aa1f-1828-34c9-94ac-c472abebedc6 | -9.0425 | -46.7032 | 2025-09-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a561d6b4-1335-3b64-b9d5-b19a8c267181 | -9.7864 | -46.1949 | 2025-09-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| baf7558b-ba38-3d63-9c9a-3763c4bc17c7 | -5.17 | -43.7276 | 2025-09-29 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| bac16a6f-23ba-3659-a0f8-2bfb9de644c3 | -20.7736 | -57.8446 | 2025-09-29 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 3cc89edc-d05b-3d0e-b82d-99403e47cecd | -9.3891 | -47.5982 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 963146e3-10bf-3607-951f-0a60b8c19b2b | -9.9581 | -43.5987 | 2025-09-29 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 50ed680d-a0a7-30ab-b30a-5cd7dbce8ec0 | -10.7669 | -45.3917 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e6a1873a-b876-3b1c-b4d5-882e3777b8be | -5.3645 | -42.851 | 2025-09-29 14:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| d253bb26-a7be-3556-929c-3cedc2c38a25 | -6.0609 | -42.608 | 2025-09-29 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| 8d0befe3-015c-3e81-9167-3cea2e14dd80 | -9.9585 | -43.5752 | 2025-09-29 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 72c826da-1fb9-3fd4-bfab-f53198b58d30 | -6.3154 | -43.4548 | 2025-09-29 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d9f6d0d9-1ad3-3bc0-ab07-2a3646307916 | -7.7975 | -47.0019 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b01e1fb4-460b-3b6f-9d85-b5a991bb39a8 | -7.9006 | -44.6035 | 2025-09-29 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 71e730a4-3f4f-38a4-a8a6-6e0ced4899da | -14.7176 | -45.2057 | 2025-09-29 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 499.4 |


[Clique aqui para ver as próximas entradas](README99.md)
