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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da9f07f6-7b0f-3c0c-8f54-54821c58629a | -4.4655 | -42.9112 | 2024-10-25 19:15:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 60c2041d-2952-32ec-b218-ce179519cd0d | -4.58 | -48.0132 | 2024-10-25 19:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 300.3 |
| 2311c205-dc75-3551-beb4-84cd1174205b | -4.5613 | -48.0358 | 2024-10-25 19:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 67394764-1dc3-396a-be92-f443b9680088 | -4.5614 | -48.0141 | 2024-10-25 19:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| f14ab2ae-dd3d-37db-90e3-4b205c0f1a40 | -4.7445 | -45.6679 | 2024-10-25 19:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 54b58915-eb46-354e-99a6-84302eda899d | -4.8735 | -48.5598 | 2024-10-25 19:15:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b66c9b29-fbd9-3878-b728-6df9e61ee243 | -4.9927 | -44.8856 | 2024-10-25 19:15:33 | GOES-16 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 359bf360-a9d9-32ef-bd1e-de9f8615aff0 | -5.0769 | -43.6644 | 2024-10-25 19:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 2b62c752-be98-31ba-af74-e3468f4965c5 | -5.2424 | -41.7931 | 2024-10-25 19:15:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 92499c7f-ef70-3d8b-b9b8-a2a5277cb96a | -5.3017 | -41.4526 | 2024-10-25 19:15:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| b02b6de5-8736-3f59-8666-e9024bbf6943 | -5.2236 | -41.7945 | 2024-10-25 19:15:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 72f3d6b0-7da4-3170-b8f7-e605a5faafe5 | -5.4553 | -45.3988 | 2024-10-25 19:15:36 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 0b6f44ff-79a8-307e-9edc-7c0755aada2c | -5.5815 | -43.7448 | 2024-10-25 19:15:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 415.9 |
| 490e0724-f1d2-30bd-a829-dc9b2a341ef9 | -5.6536 | -44.0629 | 2024-10-25 19:15:37 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d113cc46-fe8b-3f92-a2d1-91a680d3419b | -5.5813 | -43.768 | 2024-10-25 19:15:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 272b6e65-4a28-3a37-bb5a-4de4faa14b01 | -5.6538 | -44.0399 | 2024-10-25 19:15:37 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| eb0ac05b-7d2a-3e5c-a198-cb2f2dde535b | -5.8961 | -44.16 | 2024-10-25 19:15:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 145fc464-f6ec-34ab-b0b0-e918718499ec | -5.7858 | -41.9179 | 2024-10-25 19:15:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| f8554372-b1ef-34b5-a240-d6aea17ebe32 | -6.2547 | -42.0213 | 2024-10-25 19:15:40 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 166.9 |
| 36ef909e-fab0-302a-8af6-57ba54855cd1 | -6.3483 | -43.9164 | 2024-10-25 19:15:41 | GOES-16 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e31db928-5154-39f9-89a3-fb73a9264407 | -6.2742 | -47.8471 | 2024-10-25 19:15:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 788c24de-d3d2-3e8a-8f62-f83f3b01b292 | -6.2744 | -47.8253 | 2024-10-25 19:15:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 257.6 |
| a3b99cbe-1939-3674-b313-9d49ddeb6db6 | -6.5054 | -47.0414 | 2024-10-25 19:15:42 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 9e95d5e7-01b5-398e-a83e-b037a39adeb0 | -6.7096 | -43.4673 | 2024-10-25 19:15:43 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4695db24-013e-37cc-8917-9d3f0e9d2438 | -6.7045 | -43.9554 | 2024-10-25 19:15:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9fb81d45-2389-3e34-af03-1b6e68d51434 | -6.9275 | -60.0303 | 2024-10-25 19:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 7fe89ffc-c041-38c4-b5ac-40c64e953103 | -6.9952 | -46.6714 | 2024-10-25 19:15:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 9b1442e6-fbe9-3d13-93ea-b6ab51f25cf6 | -7.3134 | -44.9572 | 2024-10-25 19:15:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ae26cdd2-9a82-3b5b-b91b-067ae2260c0b | -7.1673 | -46.3233 | 2024-10-25 19:15:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 05f091e7-a993-3c73-aa25-df6c01dd8784 | -7.2946 | -44.9589 | 2024-10-25 19:15:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8bfe01b6-f9a6-380d-aea8-6eb283af114e | -7.2609 | -38.3594 | 2024-10-25 19:15:46 | GOES-16 | SÃO JOSÉ DE CAIANA | PARAÍBA | Brasil | 2514305 | 25 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 1744d994-09c9-3928-9953-29dfc242a5db | -7.1861 | -46.3217 | 2024-10-25 19:15:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c3e6112a-b508-35b3-a890-d27cfefd6a0c | -7.5289 | -45.8434 | 2024-10-25 19:15:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 943f869f-538f-371d-bf22-19af7d30c76d | -7.5477 | -45.8417 | 2024-10-25 19:15:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 26c73c9f-56ed-35df-89b8-79dd5c09e09a | -7.5559 | -46.8017 | 2024-10-25 19:15:48 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 06feac03-186d-3892-855e-ff2c37e88809 | -9.0635 | -48.0051 | 2024-10-25 19:15:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 3655ddac-d4fc-38b6-be9e-bba4bf51c04a | -9.0824 | -48.0032 | 2024-10-25 19:15:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 76cfcce5-b268-3b63-a7d4-5d6aa26a6039 | -9.2024 | -43.3429 | 2024-10-25 19:15:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 15181f0d-332f-3821-8c6d-83f475d49078 | -9.4699 | -43.215 | 2024-10-25 19:15:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| a49a049e-8e08-3c25-b95f-6fbed5c42c71 | -9.6072 | -42.9371 | 2024-10-25 19:15:59 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 541.9 |
| 8419eb44-876c-301c-b1d6-9d51e8db9cf0 | -9.5073 | -47.2319 | 2024-10-25 19:15:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 3402595f-34e7-31ae-81d1-cafb9f9109a0 | -9.6816 | -40.6535 | 2024-10-25 19:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| b448f64e-63fd-3c25-8d4f-038537881f43 | -10.5753 | -44.287 | 2024-10-25 19:16:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 186.2 |
| ddf3ca47-d84e-3e87-8d9c-72f83093122a | -10.5948 | -44.261 | 2024-10-25 19:16:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7a8f5464-81c0-3edb-b2ad-9b9e1cc24952 | -10.5944 | -44.2844 | 2024-10-25 19:16:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d4323ce6-3c0b-388d-91cb-f0acdca56437 | -10.6135 | -44.2817 | 2024-10-25 19:16:05 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 469354c8-7e5d-3ff5-bd39-83af555d0e76 | -10.6139 | -44.2584 | 2024-10-25 19:16:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 156.7 |
| bdbe5bc2-5c2f-395c-882d-9d31dc1335de | -10.6249 | -55.9757 | 2024-10-25 19:16:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 9359b1a4-c431-3d94-afd7-c1822a56a8b3 | -10.8984 | -47.9355 | 2024-10-25 19:16:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| d1a6f175-5fff-3f31-a8a6-b67a8c80098a | -10.879 | -47.9599 | 2024-10-25 19:16:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 2fe51c01-dd02-3674-aa3e-3aab9730cc79 | -10.8793 | -47.9378 | 2024-10-25 19:16:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 3cae0d9a-bee5-3232-8ae2-d53bc2c49089 | -11.5357 | -43.9853 | 2024-10-25 19:16:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 93894204-eb4e-3412-8464-c36c35a4a71d | -11.6711 | -43.9178 | 2024-10-25 19:16:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6b23aa57-8984-3114-8537-35b4cfa273db | -11.9642 | -44.6676 | 2024-10-25 19:16:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dc6c0461-991d-3e94-85f7-39d1aa1248a6 | -12.1179 | -43.6354 | 2024-10-25 19:16:13 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ce3c5058-d2cd-3175-9d45-71fe462628f7 | -12.4612 | -43.7921 | 2024-10-25 19:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 4e790a89-beff-3570-ae6f-13a937829fe1 | -12.6636 | -43.3074 | 2024-10-25 19:16:16 | GOES-16 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f51679e8-8548-3f53-a3eb-57072d5ff855 | -19.6414 | -56.9778 | 2024-10-25 19:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| d5a2267b-46ca-3cae-8d59-177eb2be18dd | -19.6225 | -56.9178 | 2024-10-25 19:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.4 |
| 4e24e4d4-02a9-3c04-8264-c16a3a6eb9aa | -19.6611 | -56.996 | 2024-10-25 19:16:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 58339751-5489-3bc8-a8c8-dc3283ecdbb7 | -19.6024 | -56.9206 | 2024-10-25 19:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| d4c8b4a8-38c8-3d5d-b3dc-45be08578aa1 | -1.0733 | -53.658 | 2024-10-25 19:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3dc08b8c-7e39-34b9-ab09-8e67120de655 | -1.0368 | -53.5171 | 2024-10-25 19:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c21c7175-f28d-32bf-91ad-1ee2ec3ef14d | -1.3637 | -55.8472 | 2024-10-25 19:25:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9a13e5a8-c8b9-3e46-adc0-2cb92dd018e9 | -1.382 | -55.847 | 2024-10-25 19:25:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| a85b1d2b-6ed3-3aa4-bb23-29c1d948c5d4 | -2.1129 | -56.6823 | 2024-10-25 19:25:17 | GOES-16 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1f9fd511-2936-38b2-8516-96ca1b38032d | -2.1534 | -54.9256 | 2024-10-25 19:25:17 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| a783216e-63f6-33a3-a30d-26f71f9eff1e | -2.0232 | -55.7798 | 2024-10-25 19:25:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7cceb559-0c61-3539-a196-3ec8b4511258 | -2.3056 | -46.637 | 2024-10-25 19:25:18 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 505151fd-b488-3daa-ab85-d11b2bdebf25 | -2.4251 | -49.7186 | 2024-10-25 19:25:19 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 822960ae-0b57-3083-aeab-38a0fad04359 | -2.6658 | -49.5008 | 2024-10-25 19:25:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9061ef59-1ed9-380e-84dc-60dfafbc9388 | -2.6473 | -49.5225 | 2024-10-25 19:25:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9ab9ca2b-7f11-302f-a5b6-308d81f5d5b4 | -2.6473 | -49.5013 | 2024-10-25 19:25:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0a4de0ba-a529-3301-a06b-bc6258621e8f | -2.9578 | -50.4198 | 2024-10-25 19:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 71d39b27-2eb2-38d0-92d9-d7a31a1feb30 | -3.1281 | -54.286 | 2024-10-25 19:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0d661e9a-209d-3d1f-82d4-5b9077539169 | -3.2172 | -50.1811 | 2024-10-25 19:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 766454a7-13ab-354a-81b5-2faba8b70d82 | -3.2357 | -50.1805 | 2024-10-25 19:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 613d6b56-3966-3721-b7c4-a7f59f726172 | -3.3045 | -47.1761 | 2024-10-25 19:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| da595f89-99f4-360b-b1c2-0e0351834d68 | -3.3044 | -47.198 | 2024-10-25 19:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b693c607-ea42-3857-b90a-681da5e37f4e | -3.3561 | -44.2654 | 2024-10-25 19:25:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7eea3e05-5704-385f-af7d-e7f5ddd1f2e8 | -3.6381 | -55.5084 | 2024-10-25 19:25:26 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 24a911c1-820a-325a-889d-31313bf35148 | -3.5993 | -51.4619 | 2024-10-25 19:25:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 175.6 |
| dc51aa0c-ff97-3ced-99cb-48dcb6599bb7 | -3.8729 | -45.0834 | 2024-10-25 19:25:27 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a96899e8-6d7d-3d60-b66f-c207cafd0dad | -3.8356 | -45.1078 | 2024-10-25 19:25:27 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 516.4 |
| b044f2e3-9e5d-3e32-8d15-73b3767f0df6 | -3.8144 | -48.9729 | 2024-10-25 19:25:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 5873eb96-7fef-3bc5-80de-247be1a2bd91 | -3.9462 | -52.2538 | 2024-10-25 19:25:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2c147c57-e914-3c7f-be86-adc7b64938f7 | -3.999 | -45.7969 | 2024-10-25 19:25:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a9415ace-00e7-3912-b428-dedac1677d89 | -4.2607 | -45.6046 | 2024-10-25 19:25:29 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 280fdede-b9cd-3326-bef8-09666db34da8 | -4.4844 | -42.8866 | 2024-10-25 19:25:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2567dea6-207c-3421-82f0-57033d0dc9c8 | -4.4397 | -43.9122 | 2024-10-25 19:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c59b43aa-40c6-3d3f-be9a-3410732aaf21 | -4.4655 | -42.9112 | 2024-10-25 19:25:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 287bad66-fbb8-381b-a82e-4837446d7ce4 | -4.4657 | -42.8877 | 2024-10-25 19:25:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| dd19db62-bfd0-3614-a451-f970dad4b2f1 | -4.58 | -48.0132 | 2024-10-25 19:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| 32eb7a5b-9b3d-35f2-a70a-a35c5d2f06f1 | -4.5613 | -48.0358 | 2024-10-25 19:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6f0409b6-3395-36a0-88e0-2a9966b5c194 | -4.5614 | -48.0141 | 2024-10-25 19:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 9843804d-341e-3ad8-80fa-b6ad3673f9ab | -4.7445 | -45.6679 | 2024-10-25 19:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6393f6c0-959d-3b03-93f2-13615d7ddde3 | -4.9241 | -44.0899 | 2024-10-25 19:25:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9984e99b-c161-33f0-912b-27c085fbbd76 | -5.0689 | -56.2336 | 2024-10-25 19:25:34 | GOES-16 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ca51ded3-aaa0-3444-8bdc-3a7f5843264f | -5.1211 | -45.1722 | 2024-10-25 19:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 6a5b2cfa-7c33-3464-88b1-02e18c85bb2a | -5.2424 | -41.7931 | 2024-10-25 19:25:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 254.6 |


[Clique aqui para ver as próximas entradas](README197.md)
