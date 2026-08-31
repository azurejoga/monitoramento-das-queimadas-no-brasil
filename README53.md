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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bac4cb3c-4503-3334-9c45-9c10d14cec80 | -14.27231 | -52.87989 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1dfd6934-589e-3215-ab21-1cbc5836da6f | -13.5666 | -55.16087 | 2026-08-31 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9c6753a-1401-3339-9140-c2ef0bae9752 | -10.73993 | -47.96678 | 2026-08-31 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27342a55-5fd8-31b7-9021-a4234c081510 | -10.99423 | -49.68993 | 2026-08-31 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce8bef8e-d9eb-3937-bacb-032994492c06 | -14.17508 | -52.87997 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 119d1b53-688f-3270-8035-1004fb95bc21 | -10.48318 | -59.61615 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8053ed65-8e3a-38e5-9eab-368babde9149 | -13.45092 | -57.04887 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a214c19f-5f3a-3b16-8fc8-21ab606d7fc0 | -9.20388 | -51.56784 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 286a35a0-f38a-388e-8573-2c92548bd736 | -9.30673 | -56.80118 | 2026-08-31 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15195b78-a990-3324-bd2b-04b19875d998 | -9.89258 | -60.28691 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e632b768-ea86-386d-baa5-2bbb67865c13 | -14.38845 | -52.55811 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5bc0641a-499f-3db9-9295-f35cc56c6cf3 | -10.74929 | -44.87885 | 2026-08-31 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1711a9ce-cc91-3d86-bb32-0e93cfd4993c | -7.69544 | -63.32673 | 2026-08-31 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbab58c5-1b92-3e36-baad-164e2bc80a89 | -9.79395 | -60.17841 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc7941a1-6141-31ca-8f27-438be96a845a | -11.04121 | -47.12411 | 2026-08-31 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fd71efe-5706-35e6-a8cc-7a3ee8b2c883 | -9.17352 | -59.60808 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2eb1c384-c211-313c-b303-f3562a669c39 | -9.89379 | -60.27979 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8c6ea80-2ff5-3120-96b8-441e5e942127 | -8.96563 | -62.39219 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a340616-1a67-3dcb-8535-cbf58c3c7fa8 | -13.96914 | -54.40245 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d737222c-1459-36d7-9160-af0a9309f0ea | -9.19417 | -51.55769 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 87678d62-ff77-3df6-97a4-8313b9abb1f6 | -13.41981 | -51.38643 | 2026-08-31 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8016bd2-ed5e-3d82-ae07-0498be12fe8c | -9.08989 | -53.03909 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26156ec0-532f-30c8-a10e-fc57605b90e4 | -9.94088 | -60.51703 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8be1da7e-1a46-34fb-99b2-86deedf01f54 | -14.57943 | -54.08742 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bdf247b-69b3-30f6-9506-b36a0682d52d | -14.59952 | -54.11823 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92c73c5e-a8c8-3e4e-a8af-08fde8c02273 | -10.80293 | -50.65594 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0c0b35c-dec0-392d-aee2-8d7c0abc16c3 | -9.00224 | -65.43494 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a28a11d1-1e23-3c27-94ee-52c5062d1efc | -14.5789 | -54.11491 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48bbc99c-40e4-335f-9765-ca1899b0f1a6 | -11.21351 | -45.10031 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcfe02fd-e7ca-32fc-884a-8fef69aa2dc5 | -10.77505 | -54.04086 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f176ee4-f59e-3d14-b5f2-6afd5fc8e79a | -11.19987 | -43.37738 | 2026-08-31 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6a45e94c-9078-30c5-bfb3-efa8b533e4c9 | -9.8457 | -64.98302 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 418956c3-a314-3cf5-b8b0-4300165b4553 | -7.5125 | -63.65348 | 2026-08-31 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 954204f8-0c37-3b24-a0cc-f63253c23061 | -10.75053 | -54.06662 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dad670c-8cc6-3d2f-8937-6efc88cd877f | -7.441 | -61.42376 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 020b608a-9500-3040-8c3e-1cb3943d81ad | -14.437 | -52.52678 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 207ed0f9-632e-357a-bb92-7be545de4a51 | -9.79796 | -60.17912 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04feacd2-d452-3da2-812d-1e585dc70ce9 | -14.61214 | -54.10435 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb939e96-a05e-34cb-a2ce-65a4ef237451 | -11.37535 | -45.21807 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f78b2dcf-8778-3d4d-9b3f-ca86529046d4 | -7.58291 | -61.34639 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7d95bb7-c01c-3355-a2e4-63dfe3206162 | -11.69195 | -54.60145 | 2026-08-31 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a5a6d7c-7f5f-3cae-bca8-558d3bf87400 | -9.17188 | -56.98662 | 2026-08-31 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fb5d04d-2949-3cf0-a2a0-e8318fdd2888 | -11.8781 | -45.82341 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d26d424-400a-385f-aec0-655adb8246fb | -8.79816 | -62.50359 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e91ea009-e7ce-3dae-95aa-1d252bb74226 | -12.77816 | -46.46064 | 2026-08-31 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 393af7cb-1968-3364-9fba-565aaf07b790 | -12.39045 | -46.45032 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15a4e05a-554d-3884-98da-d38558f5ae70 | -9.06019 | -65.412 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9995af3b-70c3-3578-ab84-a84689a7b340 | -10.77169 | -54.04035 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 863c24af-d043-3fd5-89ad-ddfd9a1706ed | -15.66525 | -45.91675 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 142c0aeb-93c1-3815-bd8f-5c53cd87ac49 | -14.59378 | -54.10947 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f53a08be-a032-3db7-b6ed-6d0c490225c3 | -7.56237 | -61.32014 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ab50b50-90fd-344e-adc6-f27a493e2034 | -14.39714 | -53.0234 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 260a5c55-7364-345d-a29c-dc8f5fc7e287 | -11.92043 | -45.06519 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4640e69-4fcc-354c-83b2-9b26986f558c | -9.95378 | -46.31374 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3b93f54-30db-392e-b735-015076bf03b9 | -9.23064 | -59.57973 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c63b73af-fdd9-3095-97a6-f9ded23a69f2 | -8.61705 | -54.76968 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc58cb4f-7b0d-3508-a558-f792dafaaf7b | -11.79308 | -47.66766 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2eb369c1-11f0-34d7-8fe1-c1995bd39451 | -10.1528 | -45.73743 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 588e9d28-436b-30bd-b81d-da69671c3ee9 | -10.48486 | -59.60643 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 512b6420-51db-34d6-9f0a-0048e41f4e05 | -13.63951 | -51.84167 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a6c8a7b-ca12-3be9-afeb-25f91fdc0878 | -15.19546 | -46.23943 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50cfa93a-8553-3949-b471-ea86d290f9ec | -9.79455 | -60.1749 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ad7c4ab-c049-3b9d-8b70-6c15ee6e3f5f | -11.07095 | -51.47406 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ee2d879-ed20-3a97-9a5a-c6f50b1a60c4 | -9.04758 | -65.44752 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de0addda-3295-3d6a-ae67-01667f8b4072 | -10.54483 | -46.21074 | 2026-08-31 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b6753f2-18d5-3189-8a8c-8946033c74d1 | -12.9168 | -45.90236 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 868e328d-902f-3bd9-a18f-7231b0b47ab9 | -9.85742 | -64.98137 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6ad9e61-d4b5-3777-a13a-8bb126c31e95 | -11.69474 | -54.60554 | 2026-08-31 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a8287f-35dc-3e99-881c-e4d4d08e07ee | -9.8509 | -64.98377 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f45a0dd4-1cde-3eef-b0ed-44221c10b7ab | -9.36567 | -60.31103 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e163fbd-c7e8-39fd-8ca3-c96ff153724d | -14.20242 | -46.57318 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 247463d2-d623-3a8b-980f-265b06fed1aa | -13.63571 | -51.84111 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 26dbf513-5cf8-3707-8553-6bb5fa3a6c4a | -9.14848 | -61.0947 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3651fdbd-55ad-3aed-93c1-fedd07b68d47 | -10.90685 | -61.67951 | 2026-08-31 04:59:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b9bb941-057b-336b-b07d-9c0340acfee2 | -14.58061 | -54.10331 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3362cf0a-5602-3b3a-aef5-b07bdb777277 | -9.84468 | -64.98646 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29b3e522-35a6-3e9f-afac-046a6fa47eaa | -13.64022 | -51.83666 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a49dd0e-a83e-3dbb-a756-83220436606c | -7.51259 | -60.73363 | 2026-08-31 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a55a3f96-b1de-3d3f-8f69-ef4610befa16 | -11.04621 | -47.12484 | 2026-08-31 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d627e99-269d-3905-b22c-fa5ca1ade6ac | -8.96945 | -62.39812 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3785b4cf-f3f4-3624-80ae-00b355850021 | -9.40678 | -51.61193 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47e6a24f-3276-33e9-9554-8bfca71ff77f | -8.86992 | -66.78059 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6536064e-5a19-398a-b602-2308d748af5c | -11.23208 | -53.98441 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4feba36f-6ee1-3e4e-ab95-9bd56f704631 | -7.61049 | -61.37445 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3dc87de4-2872-306a-a2bc-c07dcc4345cb | -10.57834 | -57.49743 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50be17a0-e3b8-3324-8bce-ed5c0566ac54 | -15.19149 | -46.24073 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3f264df-b7e5-3443-baca-407c70c1f508 | -11.68399 | -47.60419 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d910c04-fdaa-3752-871f-58620c10b086 | -10.15912 | -45.73136 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 11319cd8-ab8f-341b-8052-d1427d1a0976 | -9.23951 | -51.52896 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7329d6c7-1690-30e7-bf96-a1ffff4a1c57 | -10.15558 | -45.72981 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39df43c6-8419-347a-b922-ed8a9b4c79f5 | -8.62125 | -54.69923 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddb75100-1318-37f2-86ca-e613ac008b9b | -10.13955 | -45.72541 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3468e25-e51e-3b07-8c71-e0bdf287056f | -9.88914 | -60.28268 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f8beaed-ff89-3328-b74f-83346cb2f2e0 | -7.48812 | -61.40126 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e52a35a-33c0-3722-b6fe-6b1302b1cf4c | -9.84988 | -64.99142 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 25b0f230-ca7c-365d-a4f6-a4b47420c9f6 | -9.17269 | -59.61311 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9118aad-b64a-3ab2-ac52-4ec361b269ac | -11.47957 | -58.50783 | 2026-08-31 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ba06ff0-0b05-3079-bfd2-66d14da58560 | -10.84515 | -48.34389 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6ea98346-d639-395a-8a91-0bad6cf0c91b | -11.21473 | -45.33028 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41c0c079-695d-3f5d-81d5-60a129272153 | -11.79377 | -47.66224 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README54.md)
