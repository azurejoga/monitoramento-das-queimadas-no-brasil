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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aecf2cd-bba1-3fe1-b822-3427122ca9b7 | -5.99977 | -42.82253 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07dd0d0a-58b9-3515-a3ab-bfab9bc9838a | -6.71591 | -44.33087 | 2025-08-20 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c40043e-98db-3d78-9bdc-444500519989 | -5.32122 | -44.48866 | 2025-08-20 04:55:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19bbb402-abdd-38f4-95f0-897902c98b58 | -5.48531 | -42.16425 | 2025-08-20 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed7b1600-9a78-31fa-b1f0-6442855a121e | -13.40867 | -46.35588 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cfa57af-83ab-383e-b4c2-4bf232f4719e | -6.14688 | -57.71764 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9b2e308-0477-3d4b-a4e7-c82384e51849 | -9.20776 | -59.62003 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f36d8ab-8fe2-36bd-b86e-5ed87f56ad1e | -12.52133 | -45.6027 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d75815a0-5ae4-3599-8996-55b9af7e812f | -10.44713 | -64.40623 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86ba2826-e4a2-3226-adf1-c69c135a2af7 | -14.16341 | -45.29139 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6944293-fe1d-3df9-b953-384fe2a2f7a2 | -8.87904 | -62.3931 | 2025-08-20 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa761e5c-13a4-3c0e-a008-1c15d866daf9 | -11.30553 | -44.92917 | 2025-08-20 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e63faa2f-71ce-3958-a9d0-5d00b97d0e76 | -8.69534 | -62.09576 | 2025-08-20 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3a76787-3086-3fc8-84b0-4b81f6dc3d7b | -11.31651 | -55.21561 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aeb039b-fe88-30f2-8987-e1064fc84136 | -9.23868 | -59.60469 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c4e905c-1ece-3444-9c23-8c7f3853d988 | -14.16295 | -45.28622 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7246155-81fc-3b9c-ab0b-3b4cdfd5372e | -12.9939 | -45.21035 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db4a4fc6-b698-3ac2-b072-1e69aec6d5a7 | -6.46348 | -53.37689 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd50eaec-b293-3fa5-a0a5-ca6517a12689 | -8.62892 | -67.26491 | 2025-08-20 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b08be2-7788-3eba-bc23-748d18f4409c | -13.40388 | -46.36631 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cd1ff67-74e0-3c86-97d2-9cd17c4ac63a | -12.94538 | -46.16337 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc2d6dcf-c494-377f-b631-aef11ea97c11 | -13.02732 | -46.80273 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2daf1f6-22ac-3c12-a779-b4dde056f256 | -11.47092 | -47.30272 | 2025-08-20 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fef9b7e5-89d7-3b2e-9b3b-5141f47e7382 | -9.19337 | -59.63307 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52f077c0-6c8e-320d-acc9-1ced0bf8eb2c | -8.55634 | -66.94205 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d87c7321-25e2-3c8a-84b4-887657f4df10 | -8.81803 | -47.47369 | 2025-08-20 04:57:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d0073f3-2330-3e42-bf48-ef6da26d99d1 | -11.77398 | -47.56412 | 2025-08-20 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcc78835-add3-388f-9b4f-3e5f54c48b52 | -8.30285 | -46.3508 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed7e2772-1a9e-3e26-b9c6-2aacd94f0728 | -11.12933 | -46.98582 | 2025-08-20 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a011cf2e-8097-37ea-ab1c-38c42de7e93a | -10.44185 | -64.4052 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d01e4c56-32e7-3386-b25c-088b40d82ea0 | -10.89305 | -48.49418 | 2025-08-20 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4eacf393-6d30-3c56-89f2-1ee729068d78 | -7.66296 | -45.25557 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b08d77b7-3b80-38f6-8321-b8353bb7ce41 | -5.45609 | -60.13414 | 2025-08-20 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77d73619-5acf-3654-8809-0a3eea4391c4 | -6.4607 | -53.37285 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb8a7903-9018-39c8-b567-33ce0099d307 | -9.21219 | -59.68895 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61785b02-c7d8-367c-b0dc-4c4fe67f9b08 | -8.79963 | -45.44206 | 2025-08-20 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c16cc493-5360-3ab9-ae42-21c78d5a9d18 | -10.69152 | -48.21664 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91eab442-5b0a-3773-b31c-97b1264f2776 | -11.6124 | -51.58452 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f200fb5-bd3c-3bd5-806d-05955a02c0d7 | -5.79667 | -59.21508 | 2025-08-20 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70a6ebd4-1f3a-33ec-bc3b-dc54de5427db | -9.51095 | -60.52824 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4b6ca1f-2f04-39f6-889b-2e4f6c7ab57a | -9.18461 | -59.63688 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 684aa5b6-1bb4-3399-b290-a97c9b7e3163 | -13.18931 | -46.87379 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9718c10a-2518-3fc2-ad95-292366cc9566 | -6.4618 | -53.36583 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6888e2d1-e8fb-3631-9b32-a242f791927e | -7.221 | -44.69784 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d505e15d-eaf7-37b8-937b-7a5bbbc3860b | -9.23304 | -59.61408 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62768d2d-c47f-3c12-9f0b-b590e4f5af25 | -8.6898 | -62.09987 | 2025-08-20 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e481efbf-93e2-3af5-b446-f9afdf255e27 | -9.18286 | -59.60016 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71808c81-cc07-357a-a93c-f99cbc0675c2 | -6.42294 | -53.37419 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f8b8ced-d614-3689-8410-ce9699db12d4 | -7.54943 | -63.85075 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37100de-19a4-3a83-860e-db76cfa46ecd | -7.22538 | -44.70087 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6527c975-3aaf-3f17-ba18-18822947ed20 | -12.81539 | -48.56425 | 2025-08-20 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcbddc57-ca08-305d-bf58-bbad7715711f | -7.63567 | -45.2778 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1537c3ae-c6b3-3722-9120-e863622cd693 | -11.12973 | -46.98276 | 2025-08-20 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5100f5bc-62b2-3f7b-bd1f-d2598a29e87a | -11.13013 | -46.97969 | 2025-08-20 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eea99589-05d4-38c9-bf21-8095c4fc115f | -11.67037 | -60.19111 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0080c227-1fec-3e47-b587-a5b872511573 | -6.46403 | -53.37337 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f598195a-b0be-3dba-b928-795376824d03 | -11.61548 | -51.58968 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fe44ceb-daf3-30bc-85ad-8703def4a825 | -8.56066 | -66.95415 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e54ee30-d097-30d0-99ae-98e058a2f4bf | -11.09589 | -44.81067 | 2025-08-20 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e27adf5b-0540-3f4e-a7bc-fcce29746d18 | -7.78505 | -45.16917 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71f25ae0-b293-3e8c-8ae9-5f1907ad0949 | -7.50519 | -63.83551 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a54080-68fd-3da7-bebd-dc5b519099fc | -10.46821 | -48.35354 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f578857-803e-3d60-ab8e-2ac4fd0ce91b | -9.17674 | -59.592 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b16af19-f9a3-306c-bc64-5446485d8e67 | -13.18118 | -46.89668 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 728cd88b-0dd2-3a84-807b-71518f63dc20 | -11.67441 | -60.18851 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4287f934-0444-3d16-beb4-ccbce483ff8f | -6.1366 | -57.71147 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 277c05c5-86bd-3965-a53f-ae196d676aef | -11.67208 | -60.1811 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c4081b4-21b6-3e31-b076-76b9241b2724 | -8.03264 | -47.67598 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ba44e2a-9372-341f-8d47-8ab8dd16ce19 | -8.82693 | -52.03596 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8437d94-39b7-3388-ae3f-85075621c508 | -8.69246 | -54.51701 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbca372d-f757-31e1-be0c-7c328f0e6dff | -13.02939 | -46.7854 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 584dd6b8-b779-396b-a0d1-fa331e0257f5 | -7.6352 | -45.28128 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ba8472e-e9fe-3a15-9357-8a20a01b3d31 | -5.98004 | -61.35464 | 2025-08-20 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1833805-6f4f-3244-8a0b-8b96bbf487f5 | -10.10846 | -57.76339 | 2025-08-20 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74739185-822c-38d1-ba0c-3181df9a1f47 | -13.19115 | -46.90179 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 398923e2-b1ca-3e13-8d1b-7bcd006d61be | -7.63229 | -45.26247 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57e373c4-450b-3d70-8efc-32cc1f65a447 | -13.58832 | -47.01356 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faaec603-b23e-3e9a-ab37-81c1a5a77080 | -13.40909 | -46.35247 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7b69861-00e0-31d7-847b-931f847181be | -8.01953 | -47.66909 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efeb5bf1-9de3-3db4-ae36-3ea2b8e06385 | -9.18769 | -59.6425 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ebbc0d5-cc40-3364-87cc-eb53ff267047 | -7.22435 | -44.7086 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31c82776-3b5f-31ad-8dc6-05b364e4be22 | -10.90863 | -57.50344 | 2025-08-20 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f34b6d2-9a71-3d7d-89ca-4ff4b8677c56 | -12.589 | -47.07141 | 2025-08-20 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bd6d98e-8403-342c-a115-692600b86ef8 | -11.31541 | -55.22253 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b0046c-54bd-3496-9185-23d31c969a45 | -6.46737 | -53.3739 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32a70b43-5369-3f52-9596-de4a9f0f820a | -7.55688 | -63.85575 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7fa6d70-be08-3579-88df-9ffc655cb3c3 | -9.89611 | -60.28168 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b35460f-c92c-3301-a622-367c8bb27c3d | -7.57836 | -45.41741 | 2025-08-20 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0be99cc-7b93-3e0a-b860-8909a59f4d10 | -8.56272 | -66.94331 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfe2534f-2c09-3aa7-a61d-7249b5c0d263 | -13.58766 | -47.55442 | 2025-08-20 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6cd16c7-8ed8-3a85-85ba-aadad7091517 | -8.82985 | -52.0406 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f01572fa-cf3f-3b2b-ab90-97454e030ab8 | -9.51509 | -60.52901 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b69f2d00-62bd-3ef0-9356-eac49764d262 | -13.19947 | -50.74388 | 2025-08-20 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8962157d-ee1d-3854-a943-8bab4f5295f9 | -13.56239 | -44.45972 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f31b1db7-571c-3bc9-a7db-5870a17780c2 | -6.26374 | -52.82211 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0e4fa4b-0b4b-3fb7-af37-2cba4a5b315a | -6.42404 | -53.36717 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5bb810e-37ed-3c7b-ae18-7a7da50e48b2 | -8.87631 | -62.40865 | 2025-08-20 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| da78863d-84b8-3b9e-829e-033dc2f81b76 | -13.02617 | -46.81162 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8c0120c-6bc1-363b-8015-efb29e8b50b0 | -11.1873 | -48.62285 | 2025-08-20 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9367d490-1312-383a-9ed0-4b6326e378ae | -6.14026 | -57.71209 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README44.md)
