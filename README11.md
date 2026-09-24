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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3490acd1-f338-3356-9915-d0c2ec054a50 | -4.4694 | -54.9589 | 2026-09-24 00:38:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1b287d3-86e1-33da-a325-2f580c5e45d0 | -2.8903 | -54.088001 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d33cc4-0bdd-36f7-926f-a3440d8a825a | -4.1223 | -51.078701 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bba7979-5259-306b-879f-049d75bef666 | -2.7347 | -51.5439 | 2026-09-24 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468b1f0c-0edf-375a-9127-3ae3afa3f9d9 | -9.051 | -48.143101 | 2026-09-24 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0a3ec96-2163-3f4e-9d5a-58cbf6e5464f | -10.1108 | -46.0215 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 252801c6-b029-32bb-a051-01ecc5cf1fbf | -6.5718 | -44.891998 | 2026-09-24 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c513a937-cda1-390c-bce5-2311af74c17f | -5.2557 | -49.221699 | 2026-09-24 00:38:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85db42d8-a68f-3339-8319-ab85fec808e7 | -8.9194 | -45.960602 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1e09d18-b444-38ae-9e09-8810b183b7e8 | 1.6104 | -55.9641 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f44f4176-e38b-3d8a-9b5b-a04b02dc50cc | -9.2366 | -47.375099 | 2026-09-24 00:38:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de77ff5f-40da-377e-80f4-cc3132dd6078 | -3.5621 | -43.463402 | 2026-09-24 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8208017e-97ef-33c4-8dfc-3457457aac09 | -5.6021 | -45.945999 | 2026-09-24 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 270b9ee0-510d-36e0-a291-d0f33b6bf2be | -1.2671 | -57.007 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a41ae07-78d1-37ec-a0f7-e68e7f473a63 | -19.185801 | -47.354801 | 2026-09-24 00:38:00 | METOP-C | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 746493d6-4cf5-3cb2-9f1c-ea457fc33bb4 | -10.4584 | -44.9487 | 2026-09-24 00:38:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23698cd9-6482-3bfb-8577-e250f6ad9e27 | -15.959 | -42.948502 | 2026-09-24 00:38:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4b3a287d-fc26-3b02-ad10-978cd5e3d4e8 | -4.1091 | -51.065899 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f865a11a-2df4-31dc-afcb-f235f2c045fc | -3.1814 | -48.006199 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e5ea9b-349c-3df7-b306-eba64aa5e12d | -15.4614 | -47.897598 | 2026-09-24 00:38:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b7282648-7bfe-390f-9f4a-ea21b1fd0e7a | -7.0347 | -49.8409 | 2026-09-24 00:38:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e079ed5c-6692-38dd-8b9a-a862d07c2091 | -11.2365 | -51.384701 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c204bd6e-6d61-3d54-8bbc-89c6f4cc0f9b | -11.9544 | -50.7659 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f4b9f5b-15ef-3b8c-9080-5e51b9a5a549 | -13.4641 | -46.284901 | 2026-09-24 00:38:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 06ff5193-7a5e-3e6a-98c4-0111493b37ca | -8.5151 | -50.155499 | 2026-09-24 00:38:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66f3637-6ce3-3950-a0a7-025046140bd2 | -12.0719 | -50.740501 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5df30cb-f027-3e2e-9a8d-fa3767dfc81d | -2.3921 | -48.519699 | 2026-09-24 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db7a2b7-ea73-3568-932c-dc37190b4a7a | -4.4204 | -55.060799 | 2026-09-24 00:38:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c691cefc-0e1f-3863-a8cc-5ee792aad0ed | -5.7133 | -49.827999 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8365ef-bd2d-32f5-9a84-bb61744af9f5 | -1.6181 | -54.906399 | 2026-09-24 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5895dd-0d2b-3924-a679-897bb5d6b36a | -8.1412 | -49.541901 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66c6e438-d618-3346-9a93-4afa766abfdd | -12.4122 | -46.965302 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbd677e6-f586-387b-957e-e71b434a1cfb | -6.5792 | -44.141201 | 2026-09-24 00:38:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0f1da7d-2591-32f4-a9ab-fcb39b2e5309 | -9.1892 | -49.119801 | 2026-09-24 00:38:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 221eb20e-aacc-3866-a6a7-213746ac6d66 | -10.0864 | -46.050098 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 042c3317-542e-3d47-a548-81fcee9def21 | -12.4008 | -46.960499 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b344abc3-65f5-3f65-9e12-286f309fdde7 | -4.1125 | -51.080898 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408d4319-bee8-385c-8911-777bdd4b1434 | -6.5322 | -51.500099 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3649d033-489c-3892-92b6-4f5cbaf0bf95 | -12.1129 | -50.740799 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 808fc42b-f5e1-37b4-ba0a-90ca897a2568 | -15.5587 | -42.365101 | 2026-09-24 00:38:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 20df4dbc-d34a-35a8-921c-45c4d8e10675 | -8.9356 | -45.9412 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5e5a405-2de2-32cb-8afc-b2e8af384e90 | -5.2305 | -49.2924 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3580ba41-f7aa-33d8-93df-d29cfc59082e | -5.2262 | -49.228298 | 2026-09-24 00:38:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9445ad-4b1e-311f-8358-224d4ff8974d | -8.8714 | -49.723701 | 2026-09-24 00:38:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1586a8ff-2eb2-35fa-9892-f6aa07bba838 | -11.9465 | -50.776798 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb86214-591e-329a-a5f5-740714f7a085 | -4.7146 | -55.974998 | 2026-09-24 00:38:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b01e3174-b58d-3780-99de-243bc114a059 | -17.427999 | -42.4702 | 2026-09-24 00:38:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3689afce-1eda-3db2-8f02-d73a22cd7bd5 | -10.2839 | -47.5354 | 2026-09-24 00:38:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cb4e13c-88e4-34f9-8bf5-f6ca87c43843 | -11.2306 | -51.3568 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e62edca-a761-3ef6-b095-0bf9d7124647 | -9.258 | -47.333698 | 2026-09-24 00:38:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffc5ea0e-efc3-347e-b6e6-cdfada8c389b | -8.4563 | -51.469398 | 2026-09-24 00:38:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04442377-3793-3a62-aca7-cef4480cc4bd | -10.1412 | -45.532799 | 2026-09-24 00:38:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3892d37e-7852-310f-9ec2-513186c8c8e0 | -10.0996 | -46.062302 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20f9122f-8a17-3b4f-b9c6-8afc6fcd3288 | -13.8174 | -51.8494 | 2026-09-24 00:38:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a36e8c2f-cb52-32cd-81a7-d7d70239e3e8 | -12.1578 | -50.7589 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 219a39b3-ee69-3002-978c-1c5f1ae22252 | -8.2499 | -48.201302 | 2026-09-24 00:38:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2786970b-5493-3451-9db5-a5709120cea9 | -12.1616 | -47.3605 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b69ce85c-4f4d-3b11-90db-6666606b4f71 | -2.9258 | -48.731899 | 2026-09-24 00:38:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 552486f4-a4c4-3e86-9225-643a2559e716 | -8.9275 | -45.950901 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dbece4e5-841d-3053-852a-fcd1710c95e1 | -11.26 | -51.350498 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bfe499f-4ddc-3508-a77a-59e3520088b1 | -9.8375 | -48.476601 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d58760a-7eea-3594-ad67-f1c015cfcabc | -11.2423 | -51.363899 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8033e50-a0e1-322c-933e-f7248dc9e9d9 | 1.7779 | -56.039101 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dae741e3-4668-3ec6-999b-dcda9e09c8c9 | -3.5847 | -50.030201 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a5d6c7-0435-3f70-a498-b494f55295e5 | -8.7885 | -45.8424 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17285116-a977-3701-a96e-a3d87f3b1961 | -4.2957 | -49.1273 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6492f44f-b5c2-3a70-b214-a88c75e112f6 | -2.8782 | -54.0798 | 2026-09-24 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6161e433-9574-34cb-9642-e1ca7c5fda01 | -6.5976 | -59.922298 | 2026-09-24 00:38:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4df6f14d-fc7e-3524-84c3-5aa85716073f | -6.7825 | -48.684101 | 2026-09-24 00:38:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8abf30f3-4ed9-3c28-91d7-4feae58e8855 | -8.2576 | -54.7663 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 140fc077-206d-3f0f-96a3-1ceff83db5c9 | -4.2893 | -48.605099 | 2026-09-24 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6c2afe5-be49-3e99-ba59-8223cea42fca | -9.5766 | -45.240101 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd2a0333-6b70-33a8-a42b-91b7cf6c2761 | -5.568 | -42.720501 | 2026-09-24 00:38:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e194bab-1867-3df9-a293-398d6642d16a | -2.3822 | -48.5219 | 2026-09-24 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 845d22eb-ab5d-35f9-b1a8-9a1feecc426d | -6.4149 | -44.491798 | 2026-09-24 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d0c8fb-c276-3be2-bbbe-04ebe20e0f43 | -11.9525 | -50.757099 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21506453-178d-3670-9947-4522b064b8ea | -7.6189 | -46.803799 | 2026-09-24 00:38:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 361aab51-73b8-32a5-a08b-739b43944ab5 | -8.8192 | -50.460201 | 2026-09-24 00:38:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f445885c-9c7a-32b0-97d2-f28d3464077d | -6.4375 | -48.437599 | 2026-09-24 00:38:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9f7748-5e63-3d61-a2ab-feda2853143e | 1.6132 | -55.9524 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48a06e28-eeb6-3e73-b210-d8acfb1f0400 | -7.195 | -47.469898 | 2026-09-24 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2be8d202-fd81-36db-b988-366aecf5a9ee | -15.2479 | -43.263199 | 2026-09-24 00:38:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 89381033-ddfc-3963-9fe5-9cd7b7db8f3d | -12.0835 | -50.747101 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ab84d91-185c-3985-9c99-0e2a8f36c1cf | -8.4625 | -48.683701 | 2026-09-24 00:38:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3abc94fe-df02-349c-a06d-3e70c27e55d2 | -9.8423 | -48.4977 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 922a76c2-74e2-3bd6-abdb-a9936fb430d6 | -8.7591 | -45.849201 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 59100bf7-e7f6-3155-a17b-fc851edfd522 | -13.7795 | -54.037998 | 2026-09-24 00:38:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1f3a12a-3bdd-3ff5-a459-313c83d22a15 | -5.7928 | -49.181 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8782b1ee-978d-32be-81bf-0b75a7eedd0a | -10.0912 | -46.0261 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d146a5ec-f513-37ef-8104-7ef281b3478b | -11.9408 | -50.750401 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b315cf1-8bf7-3406-aff9-b1e578b3c353 | -11.9506 | -50.748299 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a752a7e-05b0-35b2-a25e-43ed5b7b0c13 | -3.9599 | -45.807301 | 2026-09-24 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43ce040f-e45d-372a-87fe-fdd748583656 | -1.2071 | -54.546101 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eeee5bd-8e12-3265-b085-6b49593a55e3 | -1.6376 | -54.9021 | 2026-09-24 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 655742b5-97b5-3585-8dd0-8c62453c8338 | -8.916 | -45.945801 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0122332a-d03c-32a9-b665-2b8d784830c5 | -6.0009 | -44.096298 | 2026-09-24 00:38:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e811880-4193-3cb1-ace4-a52cdbc7f313 | -5.2475 | -49.230801 | 2026-09-24 00:38:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 357aef2e-7a36-3da0-8aeb-661d98f7507e | -12.3479 | -48.191898 | 2026-09-24 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 054f8e12-ca1b-356e-b385-7eacbd0952cf | -5.7718 | -45.087799 | 2026-09-24 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9003a5be-907b-31b3-83ce-74bece472cff | -8.2948 | -49.9058 | 2026-09-24 00:38:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
