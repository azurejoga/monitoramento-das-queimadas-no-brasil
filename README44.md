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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 054be824-c9b9-3196-9ee9-ac3f39ff32c6 | -6.77499 | -58.66045 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab6944d6-7f6a-3d92-88a5-3e4602f3f1e2 | -6.8192 | -59.66351 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4afc6c74-ab26-3174-be73-b038579c58cc | -6.80084 | -59.41877 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 1b55508b-04ae-373f-a087-563bf0e5117d | -8.95596 | -60.58926 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053359b5-5863-3377-9b41-58cf37e79bed | -6.38123 | -54.95575 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e522613f-c21a-3940-832d-cac7e0e1af94 | -6.86318 | -59.44097 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 467c333e-6d9f-3c8e-a238-088640bb4d24 | -8.99242 | -50.73301 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e707b84-8508-3416-ad7b-f1702fe840b7 | -9.44283 | -51.60022 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37fee3ee-e36e-36cb-82bc-93b3633f06bc | -10.94063 | -49.5967 | 2026-08-22 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b871d5cd-11f8-3e44-925b-696f897a139a | -6.3708 | -62.9029 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d8940f5-ac6a-38be-b1ae-9f52ed933a4a | -6.12556 | -59.91504 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce0b9b72-d31d-3edd-bcbd-af6113fd4301 | -6.78415 | -58.63308 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50fb033c-b582-325f-b771-8c63cd49803d | -6.17611 | -55.44039 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2aba07f-b643-3978-9d5f-df1db0bbf6a1 | -9.41128 | -60.4364 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb67778f-ce61-3948-9b65-de5a792d99d8 | -7.09938 | -61.08496 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b838bd83-cfe6-3967-b32e-4dc4652316b0 | -10.6805 | -50.30003 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eddd4235-c7d0-3964-b573-695c8b782c0a | -9.44553 | -51.60054 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f32dd3c-86a2-3e31-86bf-69c7903a2ba3 | -6.1273 | -59.91311 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16e5ab34-6e54-3baf-9f67-7910e1517efc | -8.3903 | -62.68503 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 792f0c17-21c8-3a28-aa30-4b193b73774a | -11.81795 | -56.59473 | 2026-08-22 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab398963-fc48-35c9-a6fd-fc3f2e968a0b | -11.16837 | -54.03003 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a71abd-67e8-396a-b960-d19e246b7567 | -6.84564 | -59.42657 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ee2c127-6f87-329a-ab09-654d5d27b607 | -6.76058 | -58.70453 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ba3030-a4b7-3fd2-b513-56d7ec09762b | -8.6278 | -54.7261 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69663389-e725-3265-9fd2-65d54c3ee0ac | -14.00236 | -42.48255 | 2026-08-22 05:04:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 86da4a12-00c8-3b5a-bba7-d2d115771177 | -12.71803 | -48.4174 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8843f336-b260-32af-8efb-3ffd4f549a40 | -6.93164 | -59.31189 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 708abc0b-2872-3479-a9f4-37db44fe6e39 | -6.81899 | -59.66618 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f9244a7-dfa5-3bb7-9a5f-e879bf359361 | -14.00294 | -42.47721 | 2026-08-22 05:04:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ec56c226-0d21-3ddc-ab71-e6f7757f3842 | -6.81444 | -59.66534 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0bd167-4ac5-3b4e-9c12-b71929460d70 | -6.13826 | -59.8969 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc74c615-aefc-3270-9155-6ee1f11e478b | -6.91819 | -44.97191 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fa2b42e-8c0b-3628-9d21-0a904d0f3c26 | -6.80389 | -58.62015 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d72e067b-1622-3634-a33a-d5b19722dc38 | -6.93936 | -60.08543 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f394d7-81d1-3fb5-b9b5-dc8be746c473 | -5.74762 | -53.57396 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b075bf8-be30-3e88-96f5-a5a391df81dd | -9.17998 | -59.46088 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ed714f69-9e68-34dd-ae44-7c3f823e656b | -6.87943 | -56.63734 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a6be70b-e4f1-3284-a6bd-74abc12bc04b | -6.36582 | -62.89793 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e59e49a-4637-37eb-bbd5-00a22874bf47 | -6.85499 | -59.43501 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd80d041-8703-37b2-bff6-171c2ddd119f | -6.65137 | -56.33847 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 059066e6-a2cb-36f5-a9fb-b3f3da3f864a | -7.63173 | -50.03651 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0ed4a06-80ea-397d-893a-03993b0bb553 | -8.5132 | -55.32134 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9369c77-c603-31b6-af0a-676696df3190 | -8.539 | -55.32887 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01ef8d98-bc83-3a17-9603-eb353678118d | -6.00412 | -57.80506 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3070b715-a6fa-3046-bdc9-ce820af1ad35 | -6.91325 | -44.97139 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec67347d-46d4-3f6b-be6c-70e927d1d5ea | -6.86131 | -59.44305 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2963475b-796a-383f-b9b5-bc5540de1bd1 | -11.38329 | -46.35507 | 2026-08-22 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b0938b3-b840-31b4-b4b9-40b7cc375c39 | -9.58668 | -60.50962 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40efe460-6073-3c51-94c0-cd31967a2b51 | -8.6219 | -54.71426 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a48e5e33-4a05-35e8-a068-b4285b1f8324 | -9.40582 | -60.44037 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58f26f34-26ea-3de7-a69e-f1430ed75433 | -6.77925 | -58.66116 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40822d6d-cf21-32cd-b6e2-d0ed90fb74d3 | -7.47701 | -45.15283 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf8c2619-6ba1-3c14-bf3b-0c4b2c50437b | -6.00471 | -57.80151 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f877dee0-9478-3359-8880-b6b6bf13bc25 | -6.48612 | -51.6023 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b045f7c-f0b9-334a-a88f-4c2ba16413b7 | -11.20073 | -55.0672 | 2026-08-22 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a60258d-e480-345c-9798-ea4bea53e2fd | -9.04646 | -50.83001 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61fae47f-18d5-313f-8c17-4f1e8908301b | -5.91261 | -61.2985 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 701049fe-348e-3cc9-8450-063f987cecb9 | -6.7581 | -58.66696 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 19b4d751-4c69-385f-bba5-6ad61ef683d1 | -6.0053 | -57.79803 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d44b0c-f82d-3b1f-811b-a33ea8ae0ff1 | -6.66964 | -58.74687 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88a4d631-4cf2-34ac-8cde-2c9c7730acd2 | -9.40841 | -60.4261 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dbf090d-5703-33ff-884e-ac204f90fca2 | -6.57068 | -58.97777 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4461166e-d91b-3b76-8037-c2fea997b191 | -6.84793 | -59.41306 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 970c6a1c-5f4c-385b-9ca6-2a26ece115ec | -8.5299 | -55.31958 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4053500-6bc5-3c96-b26c-84882c49906f | -6.88778 | -56.72758 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11025e04-8d09-3653-a4ee-5374ae1ac9e6 | -6.89696 | -55.38179 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fdc1b57-f45b-35a3-88e0-8451e33fd3cd | -9.54014 | -63.56507 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00739e21-5237-3e90-a2ab-ba00d991908d | -8.53694 | -54.8089 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0585746d-1318-366c-8895-b7cb67ce66ee | -6.24853 | -55.41395 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 351d47dd-068e-3c7b-b2e3-8e65f5a65d88 | -8.16416 | -55.3831 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c87e738-bffb-3c19-a150-029d929ffde4 | -6.86654 | -59.43936 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8747f0ab-e570-3f44-af71-59e772534d60 | -6.1145 | -59.92332 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f1c42dd-bb54-38b9-96d3-36713ce72f97 | -6.72327 | -48.11599 | 2026-08-22 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 477d92ab-bbdc-3c03-acc5-3600fbc07d50 | -7.59724 | -60.94321 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e18f56d-35d7-35f9-a57e-099a8fcebbfb | -9.44395 | -51.61557 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0920404-0010-32fc-a9b0-3943dcea0f84 | -6.81523 | -59.66071 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dddc7404-a2a9-3921-ad05-133d3e330778 | -6.76621 | -58.69714 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ca6b38f-082a-32ed-ad6e-3479102b8d41 | -6.67393 | -58.74759 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 421e7847-3887-3564-b98d-66f6be9149c6 | -6.25141 | -55.41851 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 328dead8-6657-3caf-a1c3-4cd23552746f | -11.59661 | -46.54581 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c39ae5f-070b-30ab-b2c2-29998f8855cd | -8.08879 | -51.66908 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e1048eb-9db6-314e-b683-ac1693559250 | -9.43883 | -51.6034 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f518fbb3-f28c-3451-96a8-f13cf5363a9e | -6.24787 | -55.41793 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae8ee563-b385-3b76-981a-afed149033f5 | -11.2041 | -55.06778 | 2026-08-22 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2a33ce6-cf25-3814-a4b2-6e53da85c212 | -10.96786 | -52.02404 | 2026-08-22 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0df7405-4d5f-328e-85b5-3d1f8ac16ec0 | -8.032 | -54.01912 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05e4fbe2-85df-377e-beba-f2af73c83fee | -7.20777 | -59.4053 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6dbaa97-7f06-3e9b-9d70-5b7c7282e04b | -6.81977 | -59.66158 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2df30129-92fd-3690-932c-60278afc9bcf | -6.13659 | -59.90679 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cddae293-ca77-3ea3-86fd-818232b55358 | -13.44526 | -51.83658 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e961372-eef5-3c6f-b9a8-9a92ef00a3b7 | -6.74822 | -58.67355 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e561a54c-f3ac-3cd9-b2d1-e31fc8eca6fb | -9.21174 | -60.77406 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 386b9c22-4cac-3d95-85d7-b42b4d54d6a2 | -10.90573 | -50.23611 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a20e59b-249f-3b01-8a46-40504192fe32 | -6.81758 | -59.6727 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ad61d35d-6358-3723-96a5-96416da01e95 | -8.09334 | -50.03374 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee25c803-c632-33db-8c84-62cd5c9617c5 | -6.89672 | -55.71329 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 625016f6-1495-36d4-bb9d-9862d3d7013e | -6.22507 | -55.62164 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3ac15aa6-61ef-3042-b2ea-8534d9f81eab | -6.85612 | -59.41911 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d657c3c-88ed-331a-95ce-086a1f5148c3 | -6.59733 | -59.11399 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75d431fa-a4a7-3bff-a459-6539865f61d3 | -11.17671 | -54.80117 | 2026-08-22 05:04:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README45.md)
