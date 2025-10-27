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
| 766a0509-7508-39ad-962e-b424bbe58930 | -3.33933 | -52.84002 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebc079a3-ee55-3e02-a83b-8abebe3aca65 | -4.45736 | -43.42027 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e718476c-29d8-3b6f-ac50-d15286e8f3e0 | -7.76871 | -45.39067 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66b5790c-84db-3830-80fd-8359f87d0ca6 | -4.36731 | -46.80861 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae09c7d3-b357-389f-9988-d6e79aea3aef | -3.04883 | -53.02026 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 454e1245-1aa1-3439-9a6d-e0a1e1467b6e | -5.60398 | -47.10166 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32c3954a-7dea-3dd1-aaaf-47ad90f0d30b | -4.2553 | -48.1283 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80fa3b28-0ee0-3389-b0c7-8e4ab875d567 | -9.27374 | -46.40892 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63c27f34-b8d2-3583-83ee-c3de19c0425c | -3.71268 | -47.64195 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f0fa9a3-dd5c-3c97-b52a-3991821fec93 | -5.57577 | -46.4299 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c6e73dc-63cb-3004-ab92-694eac9335c5 | -4.83572 | -45.33501 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 881b10ec-48cd-334e-9bf4-c912d3dc0f13 | -7.83133 | -46.48619 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 31318958-d57a-3f55-931b-75f85b94eabf | -2.98546 | -49.61159 | 2025-10-27 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c3b8dfd-465b-3a42-846a-df3c5af81037 | -5.24723 | -44.8671 | 2025-10-27 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 645c344e-500c-394b-aedc-987367ad2c41 | -2.69134 | -48.45889 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b3b75e1-1cf0-3d67-be58-bf8dd3ba8810 | -7.04947 | -47.21526 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ada56d8-57ec-36d8-b331-23aedcc1c834 | -8.00877 | -45.50173 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d758cf1-ef79-3dc1-b027-30497d88e490 | -6.47948 | -44.14404 | 2025-10-27 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86caad1c-8348-33ea-a904-d68db96a1e7f | -3.54386 | -42.79777 | 2025-10-27 04:32:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11353097-75d6-3b7a-aacd-f638565c72ff | -4.27339 | -46.99495 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0eb675c0-ed28-3004-8f79-66ec66d9cf2b | -3.86716 | -52.39418 | 2025-10-27 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2f01298-a8bb-3ee5-b1b2-b89fc01e98a1 | -5.65467 | -41.10575 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b79cf8c7-9f5e-3cb3-a98a-2fd56f1c8a4a | -4.95132 | -44.88018 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc793055-f846-34d2-a7ff-8f38740275df | -8.31986 | -46.17884 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fbb0a9f-24dd-3aea-95ce-0fd726a34759 | -4.45619 | -43.65719 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1732cc2f-6758-310f-9b72-edd761d4bf87 | -4.87098 | -48.64733 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e1ae53d-0586-3d4d-ab3d-3e45ab877b79 | -9.13648 | -51.30373 | 2025-10-27 04:32:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6ef90697-2f66-3240-9150-682a6998f30a | -4.94842 | -44.87572 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e9db4d3-40c7-32d0-82bb-f6ee5bb45efe | -6.87853 | -45.16713 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 70ec83ef-5ac4-3044-8405-b23005f369af | -5.71511 | -42.78621 | 2025-10-27 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5322828-f773-3727-895e-c77a0b0802d6 | -6.78341 | -41.00277 | 2025-10-27 04:32:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 95ef1cbd-82d0-3b39-b2e0-b8f6e84a9981 | -2.08274 | -48.37169 | 2025-10-27 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2716c5d0-d6af-3dd6-9dd5-94d74fc989f4 | -3.10679 | -49.44346 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4535f869-0a8e-3efb-bd08-9cf3b4a7f1b5 | -4.45144 | -49.58339 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d78927fa-52b4-3bf9-9ab9-f0a52faab32f | -4.81373 | -38.64827 | 2025-10-27 04:32:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 24371089-5ed0-309c-9fa9-c8296c4dd815 | -2.4423 | -49.0299 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 552c7921-2cf2-37d2-9140-b57dd2fd5b30 | -5.88929 | -49.37607 | 2025-10-27 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c92fd0f8-3555-3a68-9db7-8e3c66091ecb | -4.12775 | -48.80859 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d579840-5e27-33c3-9c31-6de431826f9c | -3.13739 | -50.16225 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb0c1a6-169f-3968-8bb2-544cb7eb9151 | -6.89837 | -46.14028 | 2025-10-27 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74f053bb-5f5d-3d11-ac97-63a121be5c3e | -9.56408 | -44.71138 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2dc17e96-7441-37f7-b36e-fc8f31664aa1 | -3.23576 | -50.65014 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bbd66e8-2239-3928-9c83-d7377b155ca6 | -4.25236 | -46.211 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a160a077-d697-36a3-acb1-6ce133525485 | -4.43663 | -43.43093 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93365823-f677-38f1-92c9-45e0200f108e | -3.32688 | -52.62755 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6c10ba0-7021-347f-ae41-48ebdc67cbe0 | -7.23085 | -44.97032 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92163201-b8d8-38e8-97cc-ea0adb966c28 | -9.30631 | -45.21904 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78cabcad-2b26-3c4c-a65f-96883fab90d1 | -5.71976 | -49.31972 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24cd3a76-cc0e-383e-b2e5-66a1bb5f1265 | -6.3724 | -42.62768 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ef9a2cf-d4ef-37ad-ba60-e94c9f9c1f66 | -4.25278 | -40.68741 | 2025-10-27 04:32:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4115bad3-e475-34cf-8354-4641306aac66 | -6.82138 | -41.56168 | 2025-10-27 04:32:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 94fa0c1e-a114-3b18-bba9-a9bdf0feb770 | -6.89561 | -45.14961 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc488370-88aa-3d75-9f40-bb02708b6210 | -7.78514 | -45.37704 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20dfb02b-7d15-3df1-a088-b202f32cccb4 | -7.9702 | -45.47181 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de1cd6b7-0d57-3b13-ba72-504b98d58139 | -4.47168 | -43.42709 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcc93b31-4f3a-398e-9608-ae043a646bb3 | -5.12352 | -47.73808 | 2025-10-27 04:32:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0744e931-41c8-3ab5-8dab-f69a209f8786 | -4.89383 | -48.65456 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6315359-4bd3-30f5-80a4-9b76a5d58919 | -7.43475 | -41.86603 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 731a3e3a-ec88-3d23-ac5b-cd1a0b4737f0 | -8.56286 | -47.39095 | 2025-10-27 04:32:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6142133-e0b6-3dbe-90ea-381ceea3873d | -4.45184 | -45.45609 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f6227ef-1573-3e1a-bb7c-fa1020bc324d | -9.33614 | -49.27478 | 2025-10-27 04:32:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b4fb100-8f0b-32cc-b2fd-2ea743afd339 | -6.92155 | -50.72822 | 2025-10-27 04:32:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 821afc10-429b-3f37-be89-ea1a8fcfd612 | -9.47494 | -47.78222 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 442ccd0d-3a32-3c78-8e10-06c4cacf1d38 | -6.22546 | -41.8293 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 851db624-e847-340b-b4ee-43a6760e12d2 | -8.94379 | -48.74156 | 2025-10-27 04:32:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 752a8b62-26c2-3537-a6ea-7cbaf9fc10f6 | -6.57458 | -48.7662 | 2025-10-27 04:32:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 620bb8ea-dc59-30da-81d8-af6c8893bfe6 | -5.6366 | -47.63224 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 953dab0c-4642-37a0-a008-78cd92c4c14d | -3.56981 | -44.53227 | 2025-10-27 04:32:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7ad356e0-00c2-32c2-ae95-cae43c21c5ca | -4.73503 | -41.55177 | 2025-10-27 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7881ac80-e1c0-3647-8a28-ab2667d0c1c5 | -7.09158 | -47.27165 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ae943b3-ce03-3840-8671-41816d327044 | -6.43774 | -42.03687 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6621f8a9-b990-3cab-bf44-5524a56f139e | -6.16679 | -41.57729 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a15939ab-2ded-31d6-b41c-99460a789570 | -9.56359 | -46.80865 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2091ec3b-36ba-3920-98d2-c5e021dff9f8 | -5.02911 | -44.68165 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 470fc89a-960b-3cf7-a37c-bdd96f2a8094 | -5.59666 | -41.31522 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3b2a589d-e35f-3bda-8f8e-042cfab8cfb6 | -8.22101 | -46.93965 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95624ad1-c9fc-3c32-8e16-244dff86f76c | -8.88311 | -44.83722 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07f1026b-832e-34ce-b36b-fd93d8097659 | -5.83209 | -43.44925 | 2025-10-27 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a963bb8-35e8-3ace-8ae7-186e0f3666ec | -3.14524 | -50.15928 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0a1cd0e-7b17-3727-92e6-c17d863b712b | -5.89268 | -49.37662 | 2025-10-27 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4516646-09d5-38dd-960e-1d311219671c | -3.23351 | -45.93757 | 2025-10-27 04:32:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 147752d3-f6bc-341a-aab6-7736c31884ee | -8.09387 | -44.40051 | 2025-10-27 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcd2c6c5-b5a9-3361-a056-1aaff3411a03 | -7.23147 | -44.96625 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e8f4877-7427-3942-85f8-e75f66c6d1ad | -10.02073 | -44.06856 | 2025-10-27 04:32:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59fc9577-25ea-373f-80ea-77be0d18bf31 | -6.26178 | -41.81879 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4ce861f4-1e6c-31c1-a77e-3b41d0059683 | -7.43791 | -41.8748 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9b92b63e-6c98-30dc-9d13-a8daf1ec80df | -7.85719 | -46.47529 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 824d5802-5fb4-3738-8e1e-8a7dd13b2571 | -9.18737 | -44.56989 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8b243eb-03cf-35e0-945a-befd616de098 | -8.88751 | -47.99612 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a90cb481-7361-3615-93b1-abce846c53f7 | -5.21486 | -42.60664 | 2025-10-27 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4aac7bd5-9a6b-38b9-8bf1-b5e9758257e4 | -5.61233 | -41.1166 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 019407ab-2ae7-3d18-8c36-da0f05bae1d7 | -6.1083 | -41.77178 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e5714c7-98c5-3d60-abb3-e7ae4563d5bb | -5.64896 | -41.11369 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5532cee1-d098-3065-bca1-3b4acd3a058c | -5.43557 | -40.87897 | 2025-10-27 04:32:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6bc99d68-0c80-3ca3-9c35-752d25889e87 | -5.65946 | -48.46227 | 2025-10-27 04:32:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77264031-80ed-32f3-b35a-c78be8b4258d | -6.26062 | -41.82678 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d22ee33-fb08-319c-8872-b6ca53433583 | -5.498 | -49.58354 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1384960d-1b70-3278-babc-dbc7a557b1b3 | -7.30881 | -42.48046 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 45b5e70e-0d84-33a8-956a-3c7e72f74410 | -9.27201 | -46.39717 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efc36e04-6cdb-3cdb-838a-7059b549f0a4 | -7.95829 | -45.16373 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
