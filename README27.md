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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b94b5b43-264a-380c-b896-cb09eb38e32a | -6.63066 | -55.24271 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b57bb05-1acb-3167-9020-89bdde854ebf | -5.54612 | -46.59485 | 2026-09-03 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c61bd12d-4e47-36b6-82c0-85e12c081862 | -7.04533 | -59.21204 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea0ebc2-8d7f-3bbd-8f19-e9ed6f04d5b8 | -5.93115 | -52.19616 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb66d051-e026-3ee8-84b8-7280a3749242 | -8.79564 | -47.98562 | 2026-09-03 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11768481-c0dd-367e-be19-d0e491ba596b | -6.63911 | -59.44862 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1707a6f9-5de3-3baa-8b15-0e4e75bd770d | -6.67951 | -59.94576 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 650eb8a4-d760-3326-acce-404fd8014e10 | -7.45935 | -46.15864 | 2026-09-03 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acb7c98b-9544-39b2-91c0-20cc207b1f4a | -4.52262 | -48.75179 | 2026-09-03 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35583a78-20c8-3449-84dd-66e123dc5528 | -6.67657 | -43.40769 | 2026-09-03 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61c90e3b-b092-37d4-92e1-976e135cbe70 | -5.41704 | -44.79936 | 2026-09-03 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b167c6e-7b2b-31ce-aea9-2fc8628d0dc6 | -6.81437 | -43.52758 | 2026-09-03 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c26cba3-08dd-3e3c-842d-ffa5e90bfc46 | -1.02142 | -53.72119 | 2026-09-03 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8cad35b-7511-36ee-b95e-68bff3f24a82 | -6.62713 | -55.23208 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f978f62c-f021-3490-b793-623ace4b0acf | -4.02404 | -47.7225 | 2026-09-03 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6903052c-aa58-30e9-ad1d-b8acdee788a1 | -6.62657 | -55.2353 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7d5b50-0fd1-391a-af4d-313aa7427701 | -6.30949 | -56.03927 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5c92fcc1-c845-3286-afe6-5b8593a5cb4e | -6.77542 | -56.41473 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289d5f83-1eb6-38e2-9ae2-6cbe7c28bb2b | -6.41494 | -56.17771 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cba8103-7194-35ab-a857-881b9c390d94 | -6.65122 | -59.45158 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7290e180-54e7-387d-83dc-7a29b01af983 | -6.56538 | -43.90471 | 2026-09-03 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12964bc7-ce8a-3a85-ad94-16fbc0c96ec6 | -8.72063 | -52.36223 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53188647-4095-37fb-88bc-3c9d0b65b7c5 | -8.70327 | -52.36372 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63879bd7-dce8-3d0e-b3bd-e89882152cc8 | -7.82973 | -50.2421 | 2026-09-03 04:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fb1b2ce-31fd-3f2b-827f-3c9ed9470374 | -6.74555 | -59.44301 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 010bf0d8-6bc1-3d70-9318-b2ecd89572f9 | -6.3053 | -56.0244 | 2026-09-03 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a45a116f-3d1b-3302-be66-47ef3fd7cebf | -6.6884 | -59.9244 | 2026-09-03 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0c8eb464-5353-3cf9-a64c-b8e233569c72 | -8.0737 | -50.9656 | 2026-09-03 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 738c252f-a1e3-3921-a948-bc184afe7273 | -7.566 | -61.343 | 2026-09-03 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 8d083a12-8022-3be8-a411-a1c344a4ab5e | -6.6698 | -59.9443 | 2026-09-03 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e20b8f26-afa7-376f-bb35-cf74df64be8d | -3.2486 | -47.2438 | 2026-09-03 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 5e46377f-7918-3ff6-adf5-d10ea8ed1212 | -6.6541 | -59.4452 | 2026-09-03 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| fdf9a4eb-fbd3-3487-9db7-40c5596429d0 | -6.3237 | -56.0434 | 2026-09-03 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c9a0c06d-ae27-358e-8d0d-9ce2de4e3fd2 | -6.6358 | -59.4267 | 2026-09-03 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 1a1912fe-2fdc-3e35-b15c-fc7ec0a57fc6 | -6.6542 | -59.426 | 2026-09-03 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 1241dc1f-5bcd-31e6-9c5a-7d23cedf6737 | -8.0926 | -50.9431 | 2026-09-03 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f45aa078-734a-31f0-83a0-11bdb4182285 | -6.3052 | -56.0442 | 2026-09-03 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| a872ab3c-9db9-35c2-a5cb-cccc4177b411 | -6.6357 | -59.4459 | 2026-09-03 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 2b364474-d33c-322c-b655-29727af69abe | -8.0924 | -50.9642 | 2026-09-03 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| aa0c8c8f-51c9-33e8-949b-721c823e3546 | -6.6883 | -59.9436 | 2026-09-03 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 9521431f-7cb8-3a19-b25d-e40502039f3c | -11.29397 | -45.18257 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc529c69-89f4-37e5-b564-a0618381c43b | -12.13481 | -47.22726 | 2026-09-03 04:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ee4af0-c779-3d95-99bd-6aa44658e5a2 | -14.13022 | -42.16648 | 2026-09-03 04:40:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b2b48ed-6a5e-36c9-9cdc-803d99694e20 | -10.88737 | -45.3158 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f754a93-510b-3e51-a84f-af024abeee58 | -9.71928 | -48.06965 | 2026-09-03 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57dd058b-60db-39d6-8fce-571960b75be1 | -8.46042 | -54.65783 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 445e56ee-4161-383b-9f50-a69615d12bd2 | -8.47112 | -54.65413 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a473d1-0b9b-30a2-b580-e1626f2c2372 | -13.38749 | -51.35651 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b8447c8-e3e1-3365-af8e-cb6434bce8ab | -11.33107 | -50.52954 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| add4e49b-4227-33d9-8583-b3550405e7df | -10.87239 | -45.3213 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4165925-139c-3abb-b34e-9b3e73d527d0 | -12.09166 | -47.05349 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db036405-e53d-35ba-add5-3fa142ac6075 | -17.57571 | -44.96773 | 2026-09-03 04:40:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20fecf6c-da65-3953-b54c-91ec3e730bb5 | -11.0017 | -45.088 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce7abcef-63fe-3362-a528-ae6ba5fb6759 | -10.56722 | -47.72486 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 358f0d3d-afd7-3038-bff2-24a4fbf894f0 | -14.21037 | -42.03822 | 2026-09-03 04:40:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 917cb824-f6ef-3b04-b834-b8b4e877712a | -14.95854 | -48.11025 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74bc6000-f01b-36d8-8311-566558e68088 | -10.27996 | -50.05125 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e62971cf-3cab-3c40-a5e0-aa406c23e73a | -8.46827 | -54.65447 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c13fd582-541b-3257-a982-d530cb8c07df | -11.31791 | -45.11849 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99f7a8ab-2be4-36f4-af3e-707858f91df1 | -8.45949 | -54.66316 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 985e8613-8e1e-3257-aaf4-73e2c110cfa8 | -11.00229 | -45.0841 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc5c9d1b-563e-3200-87aa-2555fdc29dcc | -8.46827 | -54.67032 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 064b3aad-5bb0-39e1-ae9c-39bd68b6a588 | -11.33907 | -50.54813 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86e97a8f-ccf1-3488-9bb8-335af9a23a9c | -10.88509 | -45.30762 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98e170ec-c565-39da-a5d9-84ad50bf781e | -14.05279 | -48.40361 | 2026-09-03 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 281812d6-9766-351f-b5a5-de97838bbaa2 | -10.87584 | -45.32184 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d315f984-a3f0-3563-b1d3-1861981ef2cd | -11.20571 | -45.02589 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e30c2796-db5b-377e-837a-845148b656d5 | -11.30661 | -50.52099 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e765c09f-85dc-3e32-9b35-64b99e89b3a5 | -10.18566 | -50.27338 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c594d9ad-ccdb-3214-a0d0-ba70ccc172c8 | -10.23253 | -50.28841 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8f9843c-1831-36ae-aa8d-a56b64aced5c | -11.29107 | -45.17816 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baa124fa-bd73-36b7-84e2-1b46ca5306a1 | -10.99065 | -45.09027 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 743d38ac-0c91-35b3-97ff-331cd18cc780 | -8.45852 | -54.68016 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b902edf0-3189-37f0-82ef-aef1d7b0083a | -13.41551 | -42.49541 | 2026-09-03 04:40:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5bce6fe7-8b11-3f07-a525-9cf082e7c98e | -10.49177 | -48.64938 | 2026-09-03 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 858d6aa6-73ec-335b-ab2f-ed5a1b2716f6 | -9.69898 | -57.88691 | 2026-09-03 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8499b621-9f26-38ff-a445-71c673d75fb7 | -10.88163 | -45.3071 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e457238b-4341-3600-86fe-8c1290d05cfb | -9.61372 | -48.56253 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8db82fc-b858-3d1f-8142-055fe1c81996 | -11.29987 | -45.14338 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b01d6678-ca44-3b39-9db8-32e95c44f636 | -14.9658 | -48.0858 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc2ae412-7e4c-3897-ab79-712a982f7e5c | -9.76245 | -49.0852 | 2026-09-03 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b605e668-84c6-3843-bf15-63ee3e04cb2b | -10.88104 | -45.31094 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c052e498-2be2-3097-ba7b-bd53866fbd36 | -10.56333 | -47.72784 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29544bc8-8bc8-3751-8666-addfd64ed5c8 | -11.33533 | -45.12144 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 699e86fb-5339-38fe-874d-13926304f0c9 | -10.18345 | -50.26444 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 82c5e7e6-fff6-3661-8898-baf740e56b73 | -15.02416 | -46.85218 | 2026-09-03 04:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9a8bd32-3349-3985-b3ab-2c397fd7fe91 | -10.892 | -45.30867 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b35a58b1-9b08-36ce-8e40-1c7681b380ad | -11.33977 | -50.54395 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 595f2439-4054-3c47-8bc5-5a53d950550b | -11.25047 | -45.16364 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5861dcdc-de3a-3854-ac17-125daf71b62f | -8.44409 | -54.7504 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3099ac8a-646d-3cc0-9cab-bf28dbd52d96 | -12.09555 | -47.07233 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be261ebc-1cb1-3490-a171-9612378fb87e | -10.87759 | -45.31041 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4955879a-2f5e-34e1-a12e-ccabff1163aa | -10.56609 | -47.73189 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49e733e4-adfc-34ad-af3c-95f72223ea3e | -10.89082 | -45.31633 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b763914f-6d1c-339d-b2e2-0a3bd7a1fab6 | -8.46339 | -54.65369 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfdc870e-0d80-35cc-882f-dcb826d48e43 | -16.07889 | -46.07734 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08abd055-8fb5-35f3-a187-65c45d2a492b | -11.33837 | -50.55231 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17e36362-698e-3f45-9677-e8bf3253d06f | -16.48369 | -46.59991 | 2026-09-03 04:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f04173d1-732b-32af-a8b9-5df18cde87e8 | -11.31091 | -50.51745 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0964eb7-ac01-35dd-aa94-74ef41abe1ce | -12.06165 | -47.07049 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
