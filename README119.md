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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4be1f393-ac46-3766-9a42-632744c208f2 | -8.52127 | -50.03082 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c0427a4-196f-3cd0-a345-779c7be812c3 | -6.17595 | -44.60656 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8c40540-c43e-3f55-a5ff-5cdfabbfcdbb | -7.58861 | -63.35361 | 2025-10-05 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dd570d5-dee5-3d07-881a-2877d829bd9f | -6.16518 | -44.61839 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58f3be52-7ddb-3bcd-bb27-4df5564202c0 | -7.16714 | -44.99455 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a02b656-04f7-3a73-9a17-56b8bbbb871f | -11.44811 | -49.71627 | 2025-10-05 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf4c59c1-aa53-3cc5-b373-3a8e8cc144c1 | -9.3011 | -45.99446 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52432d3a-adc2-3cab-be15-3f7ac4f7a349 | -8.91077 | -46.59322 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf202908-747b-3649-96aa-5be4e27ae1fb | -10.46321 | -57.49676 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e8cd318-c45d-3cb7-b9be-60388bc3f692 | -7.81655 | -44.53581 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c03ad9b9-dd07-3868-a8e6-dc7bf11779e4 | -8.68064 | -47.21723 | 2025-10-05 05:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f888645-84aa-37bc-b6f7-84acc2ade53b | -10.74403 | -47.89866 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 811ef255-4f02-3c6c-8795-439c8a7a7b4e | -8.60978 | -54.97414 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 490d8739-a036-316f-8d99-9b7c5b603b6b | -8.54022 | -46.33652 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bdd68e7-c404-33b4-928a-901cb14edf02 | -10.0116 | -48.29482 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54f40eed-5683-35cc-9e95-65d4d1d63e4a | -6.43233 | -46.0226 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 208d9fdf-6b8d-3b3d-bef9-1bdd7d805a65 | -6.17188 | -44.6197 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a3f4d25b-dcf2-30ce-abcf-10547c3365c1 | -9.2042 | -46.92208 | 2025-10-05 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cff2223-de77-36ed-ba94-09f7e4d8634f | -9.28297 | -45.66761 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 684f40e9-ce9c-354b-b66b-e842972d7338 | -10.84706 | -47.97262 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0abcb83-cc2d-30b2-b35f-20d86e026d79 | -11.8006 | -46.85442 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0d9a55c-2bbe-3ef0-b429-e0e1e7aa069e | -5.61132 | -51.80939 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f622930-9445-349c-9cae-508ce80685ca | -9.65299 | -63.79414 | 2025-10-05 05:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b2ed0ff-7b3a-3014-9b2e-3bbafafd93c3 | -11.23276 | -47.79908 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81ecc523-2913-3844-a365-9c1e41be8a4b | -10.64823 | -46.32743 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c323510-417a-3a7f-bf23-a6d3112ed5e4 | -5.92897 | -43.32518 | 2025-10-05 05:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 390b91e2-4219-3d19-8f50-6f966d392114 | -9.90717 | -50.20062 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3826be1e-d243-32ce-8b76-6d36001a77e7 | -8.60174 | -46.27638 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 25a5485d-797f-3431-b366-506a5e969296 | -7.80099 | -44.54683 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 827c6859-6946-3e39-bcf3-fd77dd56ed59 | -7.81578 | -44.54157 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dec315e-6c95-3793-a5c8-e95f3227c599 | -10.21614 | -54.12788 | 2025-10-05 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f99af9-110f-3e08-ad21-2191135914ec | -8.60232 | -46.27177 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d83e7b37-fead-3118-a043-c56f0464d68c | -8.93418 | -48.6619 | 2025-10-05 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b072963-4523-3402-b820-8d56e5ac6559 | -10.46488 | -57.48607 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6e3d01d-f9fa-3c67-996a-d467cd6408e3 | -11.09834 | -47.74162 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2079e2d-d85d-3f51-bab9-7c23143496cd | -10.6476 | -46.3327 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| debeb74b-f83a-341f-8ad3-da4011e8fa69 | -7.78638 | -44.55081 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4653a38f-942b-325a-a729-954fc9161b7b | -10.45568 | -47.8107 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1caa68f5-3a83-3959-9b6d-95a8226f5ed4 | -5.6104 | -51.80604 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bb00b56-62b9-3d19-8569-d8f5ede3364e | -7.31543 | -45.5648 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e502c4-78c9-3154-b3c0-9a39834be46f | -5.11205 | -45.47026 | 2025-10-05 05:14:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f046950-a0fb-35dc-bedc-7d91d8c88234 | -9.32166 | -54.53393 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abb3d154-cca9-379d-81d8-d45631e3f3b6 | -10.57123 | -48.71955 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb9cd5ce-20a5-305a-bea7-8b11294819c4 | -8.93476 | -48.66478 | 2025-10-05 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e6ac99d-da92-314e-b145-eaf3613a5028 | -11.45755 | -51.51989 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a99b828-e8e2-3156-bdbb-c0f7054e3da5 | -8.90063 | -46.67852 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c8acf11-96aa-3290-9c0a-ab0064897017 | -8.59192 | -46.30396 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e2dfd444-c211-3be9-a818-35c7dcce4ed2 | -10.84065 | -47.97663 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a151a23-d91f-3bdd-8f82-96a37de188ab | -6.99837 | -44.21307 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51afc039-8ce4-3173-baaf-456bd9f5bebf | -11.77996 | -47.9445 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bba97c25-c5f6-3038-a9de-087c32706bb9 | -6.46472 | -44.58606 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f0eeddc-7f19-31ba-96c6-0ba49ed5a82d | -10.94065 | -47.08928 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20f23503-a204-38b7-8af7-40e341bba71b | -9.34214 | -54.52334 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86e5b0f5-4571-3853-a05a-ceeef8e03ccd | -8.59623 | -46.29879 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 24e23355-8d92-375a-8e66-da28e6bdfd3f | -8.58944 | -46.32401 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9b041649-4357-3b55-94cb-1558a8916dc8 | -7.80024 | -44.55249 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90889d38-e18a-38ff-b9de-73e6896afaf8 | -10.06072 | -59.35483 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77544d10-5ff5-36ef-8c7f-3ccd9e731e91 | -11.75508 | -44.7421 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0fb4d46-49c6-3e1f-80f2-524356a607d9 | -10.67985 | -49.27717 | 2025-10-05 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1ef1820-f0c1-38e4-9e38-be736844b7f8 | -9.18132 | -58.92285 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fd281fe-e388-3801-8997-6932a03fb77f | -11.1225 | -47.17515 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4d296b4-cf7d-3501-bc4c-c3b0d4426be7 | -8.57418 | -46.3208 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 9edcca00-83c9-398d-92fd-254b13ccd2b4 | -11.90271 | -44.99301 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f129dfc6-77a2-3d7d-b4d6-2722c4c58567 | -12.45593 | -44.73792 | 2025-10-05 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2553f7c4-ec50-317d-8441-2b5fcbb19aa3 | -6.14151 | -44.58986 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 718bed91-18c4-38df-8758-32977b8f94ed | -10.39274 | -45.40458 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fd6fa8-2cd8-3929-bca2-9e9e136b983c | -11.75668 | -44.74784 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 20d2e68b-9aa2-32ea-9caa-6029bfcc1faa | -9.34278 | -54.51895 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c22df44-6cbd-3bd4-ad38-9d6c580a8dff | -10.36221 | -48.28417 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 948449b3-22a6-3ee7-828c-bb9f62a27cd1 | -11.23065 | -49.92619 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84023f18-75b2-363e-bfc2-1807629fb2be | -8.62179 | -54.96753 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd7b7b06-4b7d-3b2e-9c19-33642b7461ae | -6.18188 | -44.61383 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77e5963b-1f03-3aa8-85b3-8763d7e54ce0 | -11.67544 | -47.4807 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e13130b-31fc-3eba-9af8-8838762f5c49 | -6.80965 | -63.05471 | 2025-10-05 05:14:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14034aa3-c6ac-30f5-904e-fc7aec6963c2 | -10.22696 | -54.28573 | 2025-10-05 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89a9454b-975b-3900-99e0-acefeea2dc12 | -10.35733 | -48.16744 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a0acf826-1e20-32a7-a0d6-b2815d8543a9 | -11.12032 | -49.86291 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7b50b3f-855e-3ba6-8ca6-7251570d8cd5 | -7.02843 | -50.73548 | 2025-10-05 05:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4079eb7c-0a0c-3c3f-a932-83aafc64d118 | -11.49522 | -46.78819 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d3877b5-41d6-3bda-93c0-e9a2184f1958 | -9.15133 | -59.53823 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f27f1eae-ed4a-3288-9743-e90a6d8d3dc1 | -9.63813 | -54.31563 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4885055a-6a59-32a1-8812-6dc429bcd944 | -9.85188 | -52.21937 | 2025-10-05 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d937365e-c62b-307a-9a31-9366c2d36980 | -10.35912 | -58.45516 | 2025-10-05 05:14:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca64b077-9d61-340f-a88a-90f1d45f5e90 | -10.68563 | -49.27435 | 2025-10-05 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4c59b34-2894-38e6-aee5-45367a357d81 | -7.43942 | -46.53076 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a3c1980-dabf-3823-acf6-7f0f78383cc6 | -9.65718 | -63.79487 | 2025-10-05 05:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 310a25cb-e336-31c5-b4e6-4eac89fb7680 | -8.56034 | -46.32898 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9d4f9b3-37b4-3b45-99f3-f0fcaac0bb1c | -9.8418 | -60.27248 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e90e6fcd-9b8e-3e95-99db-0dc16dfa493e | -8.59314 | -46.29414 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 311676d9-5e92-396c-b092-4171c0a7cd24 | -6.15502 | -44.59186 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d8e78a1-b25b-38b3-a79f-8138c597e6ff | -8.2424 | -46.80618 | 2025-10-05 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465af3d5-a7bb-3aab-ab66-2ea9a9c98e93 | -6.14068 | -44.59598 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ccd66fb-1b99-33ee-90b8-7acad7fe7af0 | -9.04378 | -47.0178 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 090318a8-a29b-353a-b1e7-74810b4bf89b | -8.59942 | -46.29513 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2aa90312-c536-30dd-b922-d1ae81515587 | -6.15421 | -44.59786 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 46b81281-5480-3589-bca0-2627a991bcb3 | -6.87551 | -47.23227 | 2025-10-05 05:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c58ca7a-e70f-3799-a88f-a73914f68e89 | -10.73768 | -47.90206 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f5d7d78-6a6e-3ba6-a1db-e23b725f95f7 | -9.98863 | -57.82001 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d57ba65-10e1-3458-9e9e-f7c2f443a692 | -9.33037 | -54.5261 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ea034b0-e7cd-31ca-969a-9343c4f39c7b | -9.85964 | -48.81332 | 2025-10-05 05:14:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README120.md)
