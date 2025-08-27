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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be2aa00f-335e-32b5-be95-012ea4f99f3a | -9.16668 | -59.46514 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 702ff374-63e8-35c1-834f-b977a8c5399a | -9.58333 | -55.38423 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fd834ab-7f31-354e-a0fb-f4747f64db19 | -8.69098 | -47.20548 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af2bb8a0-be2c-30ca-a416-74d82fc467a2 | -6.79697 | -44.34757 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 697f1942-394d-3825-9821-f80a6cfa27aa | -11.24175 | -45.47423 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28323dc8-bb64-37b4-adfb-7dc1e86aa1a7 | -9.95284 | -46.50218 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22b9553d-3983-35cf-bdb8-d45f7370b277 | -9.23284 | -60.924 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe66db59-5e88-34d4-b498-76e3023f10fb | -6.66544 | -44.20475 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ea1256-2b34-333e-91f1-e329f59af281 | -7.70689 | -45.77553 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0135424c-0bcf-3ab9-8134-40b2554be00a | -6.71039 | -58.56867 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2fff00-0e20-3aa2-9951-024103472504 | -10.1219 | -47.43588 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21fa4dd4-9fdf-3d50-a23e-bca9ea75de98 | -9.8461 | -45.96667 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40925ebb-4b9e-3ee7-b911-aa8e75c25107 | -9.08387 | -49.57278 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35326965-be3c-37f5-a1a9-08cf87ff5511 | -6.4613 | -44.5717 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8aa4efe7-f31a-3e83-bdae-55ffd3e4c961 | -10.87135 | -45.23644 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 502e72bb-7961-36fe-b4c7-def329f2b66f | -9.08142 | -49.60917 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3908f6a8-e6f8-3323-9d5c-248bc4affd70 | -7.34803 | -59.66654 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e098bd2f-d8e7-36e5-84bd-56bc6b2d307c | -11.15466 | -44.68951 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbf219a0-b20d-39ad-aa6b-86b427d774eb | -8.88557 | -60.78005 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff29afd5-4aa3-371c-91be-686ba7150209 | -9.55777 | -55.38278 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81e83a54-7c93-3f56-9d2d-2141842fdaf7 | -7.56892 | -47.48789 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 536149d5-88b2-34dd-84c7-e4b4960ebd46 | -6.68221 | -58.54143 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88571daf-b6b1-39a3-aa5a-0119542e7788 | -3.74457 | -49.04975 | 2025-08-27 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cbb3e8c-a173-3491-8a44-3f039f47ec8f | -6.65331 | -53.18591 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f58a7eb-ddb9-34e1-904d-be2f15a7c8ae | -11.24438 | -45.47789 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 19811728-7995-3bee-8129-294a2c5bfbf7 | -6.91352 | -52.85558 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35ec2bc7-8d32-399a-aa72-8add1981c5b5 | -8.89394 | -60.77465 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb73e020-cb4d-38fe-b826-b052b1ebcdeb | -7.20826 | -44.40421 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc408e19-f0d4-36fe-98d5-5525fbbf64c5 | -8.85282 | -47.17044 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a609248-0aa5-3be1-ac52-17fcf66d4888 | -6.4579 | -44.57117 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3c96a0a-b29e-3044-b767-e04cc0b0e541 | -7.59357 | -45.21914 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 741fd636-12ae-3ab7-88c6-8f40ae6c724c | -4.31196 | -48.10299 | 2025-08-27 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| dd60c6cb-05fb-31bb-90f1-98edb5755fd5 | -6.3886 | -45.32154 | 2025-08-27 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8c355b0-a1c8-3e9d-8d7a-7beaa45d46c1 | -6.79638 | -44.35144 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e426d8f2-8aee-3000-a1a5-12302ed1e022 | -7.6625 | -42.65629 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7a4240ab-9d11-3e67-ad7a-33499b0db5ed | -10.92082 | -44.61164 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82c4ba47-9028-32ea-b4d0-44f7c62ec3ce | -4.10912 | -56.34188 | 2025-08-27 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00ea4cb-8536-3b15-a900-4ef8c6b060f0 | -7.64391 | -42.67723 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a312c08f-0860-3eb5-84c9-926e2f4ef5f4 | -7.70799 | -45.7685 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd54a979-552e-3457-9305-1e5b40bced30 | -6.8801 | -44.39795 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ba3d5d-1ace-3a9c-9c34-c7fe5b12e91e | -11.13824 | -46.33981 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e878366e-8646-3bd4-a322-7b26b22c0f5e | -9.25682 | -56.90535 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c24330a3-98c0-3169-ac7f-e79dbb8bfd5d | -10.49085 | -51.60107 | 2025-08-27 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f428022b-ae4c-3425-b85d-f7c3e2954e85 | -6.94949 | -44.10505 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e52b069-d9e4-3a98-8031-4cc3a71ccf3e | -6.25766 | -43.82716 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2109def8-9d50-3789-8490-c0eb176cf3c7 | -3.98281 | -47.88657 | 2025-08-27 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12a193dd-6fd4-3a31-a323-0939f4d31a05 | -5.53863 | -42.66208 | 2025-08-27 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 69e665b3-6794-3e88-b36b-653942973f58 | -6.89125 | -45.64787 | 2025-08-27 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2396153-41ca-375d-bb86-9e78994dd9b0 | -6.04968 | -44.17442 | 2025-08-27 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 978e33fc-da00-3c8b-91a1-889b4cd51a4a | -9.15216 | -59.56952 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a4f09acf-723f-3137-84a0-d5aba34ce805 | -10.65463 | -47.20294 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5276404-ec1c-3147-bab0-614504f96c89 | -7.14607 | -44.14542 | 2025-08-27 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 080cdfc2-a9d4-373a-be91-f9b8b80b249a | -9.17517 | -59.52151 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cce16b0a-2f36-31ba-9a1c-164c89db9466 | -5.7569 | -53.76054 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 605c5a63-acea-36a2-a6f1-00983645118e | -9.17078 | -59.54394 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f5a250a-792a-3c6a-9e18-e516e7b09b3d | -9.07969 | -49.57616 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de158dcb-3950-3cda-80b4-1affc09c4f52 | -3.80557 | -51.2607 | 2025-08-27 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d37acd0a-aebe-32df-b3f3-14553e927beb | -9.16967 | -59.54959 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4189a8a1-2ffd-311b-abfb-4e160f9d97c3 | -6.91176 | -59.36789 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 881a2f9e-ed44-31fc-ab67-88d0d4cc07b5 | -6.68428 | -58.85866 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4686776d-8a55-3a5a-abc6-b59b29b51aa3 | -6.52054 | -42.98807 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f06672d-70c2-39db-a5c5-898b57d77097 | -8.89665 | -60.76073 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58fac16c-e47b-3999-9c2a-2c49158cb38b | -9.59 | -55.37452 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93f12da8-6516-317f-9dcb-6cee57acec9b | -8.29246 | -46.32915 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd855b67-ca6b-3f17-96c3-c537b0a9cbab | -11.0368 | -45.13964 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 276dbdab-be68-3b8a-b534-d8f24beb0de1 | -7.28754 | -46.99483 | 2025-08-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06b95410-030e-312e-a565-b10027a395d8 | -8.86716 | -47.1656 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34de9c3a-db05-3032-8228-00d3678fa886 | -7.38133 | -47.04549 | 2025-08-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de4fe880-833a-3dbf-ba1d-13ac807ca9ea | -7.73896 | -51.14054 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef4def77-bc65-3d43-a9cc-96a198c85349 | -4.93117 | -48.02951 | 2025-08-27 04:25:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e96c963-836d-34a8-bc6d-c7a0aa9bf955 | -5.4771 | -42.60073 | 2025-08-27 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0a9a112d-cc6d-389d-af03-9cbb169d6599 | -5.69065 | -40.97779 | 2025-08-27 04:25:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77b062ff-3ad2-39d4-bd34-c92e775b7b53 | -9.1962 | -46.73701 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a40bfa0-4de4-3858-b0f5-f32a77b9360e | -8.46692 | -43.65881 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9107bc7f-5679-35d3-8849-e120f11eec31 | -9.16973 | -59.51463 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b64c425-61e1-307a-8359-8ff19b979ffa | -9.07704 | -49.56863 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c059ff1-188a-3f62-a9a1-f16dbaf7296f | -4.60572 | -45.6074 | 2025-08-27 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c14e1721-cfc2-3296-ab20-e3c876c01c35 | -9.57759 | -45.72976 | 2025-08-27 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae97517-2fe4-3420-9412-2f851b6e5c5a | -5.18865 | -46.11199 | 2025-08-27 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51449ae7-fa5e-3319-a207-4587c42a9169 | -4.9578 | -47.58115 | 2025-08-27 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bc6d1e2-d268-33bf-9d3f-88a7a29a0874 | -7.65802 | -42.66041 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| eae07a1d-2efa-326a-b730-5309909b5531 | -9.19508 | -46.72256 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a6077f1-3a54-37b3-8b65-d74c6586694c | -7.57998 | -47.50416 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a75624-7e24-3b9a-8a91-b1a85e9c770c | -4.84997 | -42.88971 | 2025-08-27 04:25:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdfc9206-2eb8-3b41-9da7-65c5fbfd267c | -7.20997 | -44.43926 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc04535-3cd0-3a22-bb2d-e86636d1e322 | -10.78471 | -47.066 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58c6a187-7006-3d22-abf4-a5b980b8d6ec | -10.76596 | -47.01273 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 097e924a-5a81-3a5a-8168-fb553b2bfd12 | -9.86468 | -44.69458 | 2025-08-27 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6991be1-f10f-3b44-9a41-b45ab50fc85f | -6.96802 | -44.10027 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa280238-9b16-37db-85a5-ebe6a6d7f14d | -5.59437 | -46.3392 | 2025-08-27 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 069b9dee-bad1-3ee1-a599-c8412d040e27 | -7.65872 | -42.65574 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 932384a0-f8d2-3b40-be05-af726238c05b | -7.34128 | -59.66512 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5184497a-bdf7-3122-ac2b-9e6b38a25a1c | -9.94209 | -46.37409 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40a19700-097b-39dc-925a-8978aa2baefb | -5.87877 | -46.4086 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61e8aba2-25df-398f-afaf-4a6afd0c6f44 | -9.17308 | -59.4631 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cebfeb6-2d7c-3a17-9c74-15c842e016c8 | -9.96594 | -46.3742 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95516446-59fc-32f1-8ed0-02f3c99380c3 | -8.45297 | -43.67796 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf9918a-0272-3513-b08e-f7f2cf913971 | -8.69208 | -47.19851 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15b17800-467e-306a-b7f4-ee108be92300 | -6.50151 | -42.94135 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45bdf73d-46d5-384c-b80c-26ec35d8e3a4 | -6.77979 | -44.29842 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README38.md)
