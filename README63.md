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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7795e10-2ebb-341d-9c45-2fa8651769e2 | -5.4553 | -60.0626 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1e4cc41a-6bca-322f-b2b8-55eb740fecf9 | -10.3208 | -49.9352 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 16eea508-c69a-30f3-8c33-b7f11d277b70 | -6.6883 | -59.9436 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 04b564cd-db24-3368-9ed9-8f66c9d7585e | -12.1319 | -50.6121 | 2026-09-03 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4a17b3a1-761d-3765-a818-9621cf89e3b5 | -3.0164 | -61.4848 | 2026-09-03 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 3028fd4e-72d3-3ab0-8c2a-7e37799a963f | -8.911 | -62.372 | 2026-09-03 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ed2c6eb2-6de7-3fdd-869b-a099d7fa4c69 | -11.5287 | -45.4703 | 2026-09-03 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 06734d42-d072-3bb9-95e9-6286cbceb4e4 | -3.1997 | -61.1988 | 2026-09-03 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a53ebb57-35b5-3424-b38f-c5eeafc4c3d9 | -6.9514 | -59.0666 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 90cdca8a-ba71-3add-9129-c523535cb683 | -8.4488 | -54.6644 | 2026-09-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| abcbd8ce-ab0c-3338-9dc5-374607c5b926 | -11.0741 | -51.5576 | 2026-09-03 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 665b4810-fe47-3a4d-a510-16b99d37949e | -7.5659 | -61.362 | 2026-09-03 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d0464ba6-477b-3bc1-9ca7-919803f16d23 | -17.1423 | -55.9377 | 2026-09-03 14:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| b907f3d0-f411-3275-a040-ea953655e2a6 | -10.3772 | -49.9508 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3af7cbe1-3825-3827-a603-8d8fb05bc156 | -7.0786 | -56.5213 | 2026-09-03 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 726c9c18-97dc-3c2e-9f25-08d8206c3c0d | -7.9605 | -44.3212 | 2026-09-03 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 399bba1c-2478-3ba8-a0a6-ef595d7c39d3 | -9.6839 | -48.1386 | 2026-09-03 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 83d1cbe9-ccb3-31b7-9a0e-354227194ecd | -12.1462 | -44.1725 | 2026-09-03 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ea776256-50cf-3675-a16a-810ef2138f02 | -3.3685 | -59.5036 | 2026-09-03 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 0c3fdcaa-35a4-3b05-a4c0-63aebe538149 | -17.0878 | -56.8534 | 2026-09-03 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 2029617a-b385-3a58-ac1f-87138b463f9b | -6.9656 | -59.7984 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9b06e088-251f-3425-a993-cd068e45a49b | -7.0427 | -59.2366 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7885c754-56b5-38c0-ac50-91a9093074c2 | -9.6441 | -48.2959 | 2026-09-03 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c21ea99d-0a75-368f-9b23-3b65926e1aa7 | -1.4752 | -54.8157 | 2026-09-03 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 8c1ea9a2-65c5-30c0-affa-0d9c5c0ae154 | -7.9794 | -44.3193 | 2026-09-03 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f14000b7-1a93-305c-8e22-01bd439e6383 | -10.3394 | -49.9547 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e21a8b1b-f98a-35f8-aab0-dcc2c71bc2f0 | -9.1713 | -49.9622 | 2026-09-03 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d882391c-4e31-337b-bf27-bf8ad6da1897 | -7.0058 | -59.2382 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4c1e9f37-38d7-3019-abc2-62c8ec799528 | -8.9111 | -62.353 | 2026-09-03 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7b6f628c-dc7f-3d42-8ef2-b9ce8c595c1f | -8.4049 | -44.964 | 2026-09-03 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ff0fd3a7-c491-37f5-8375-25dd751b9ee2 | -8.0971 | -45.4734 | 2026-09-03 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2fdfbb9b-3114-3916-b36c-045f785e8061 | -5.3264 | -60.143 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| f25593b3-7258-31ab-97a9-af434da0c807 | -3.6215 | -60.585 | 2026-09-03 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ea4f7cbd-10c6-3fae-b455-6b72ad78fdd2 | -7.5476 | -61.3437 | 2026-09-03 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 99e2ec79-2c00-3389-aa9b-fe34b8b4b411 | -10.1087 | -50.2776 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 24b802ea-b7a5-37b3-bb2d-c84d41d858d3 | -10.8635 | -45.3101 | 2026-09-03 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a16e5e9b-3eb0-3eaa-af97-a5a55e385007 | -11.1935 | -46.1092 | 2026-09-03 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 040acaa7-2336-3df8-b79e-1a6167e80a3f | -3.2179 | -61.2174 | 2026-09-03 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 32677e35-1c78-3fb6-b49f-9f1b4e32cba1 | -11.537 | -50.9789 | 2026-09-03 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| c9de49e7-cfa5-39bc-b5ed-2b6faa942645 | -11.5086 | -50.3204 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 14b900c2-891b-3a84-b930-b77a32587180 | -10.8614 | -50.4985 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 61cd224b-c489-318e-89ba-2b16d5756c93 | -7.3118 | -60.5897 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 06ef9a3e-aeee-3d1a-80cc-7240fb116d7c | -17.0878 | -56.8534 | 2026-09-03 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 169.3 |
| 01cf00b7-b050-35ce-807e-f91e0a670c02 | -7.2255 | -42.7616 | 2026-09-03 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| b1915569-c3d4-38b8-946f-1b170286f577 | -10.767 | -50.4872 | 2026-09-03 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f944364b-5070-30d3-9b71-8bc6788be355 | -10.7667 | -50.5086 | 2026-09-03 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a425a502-7da4-37cd-850d-b08e3adbdf65 | -10.5604 | -50.3809 | 2026-09-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a2505986-8c15-3886-a09c-c709aa1fd40a | -10.3205 | -49.9567 | 2026-09-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 1e1a5452-133d-35ac-86c3-048f6754101b | -14.5758 | -53.5948 | 2026-09-03 15:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 70ccc1af-ce3e-3490-9cff-54034ea576b4 | -10.0105 | -46.4161 | 2026-09-03 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2369674e-cbdc-3efc-8529-385a40e92a07 | -5.565 | -60.1739 | 2026-09-03 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 750e0e5c-2bea-3f6b-86e5-6b7ba36c0aaa | -12.0741 | -47.1164 | 2026-09-03 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 41f43373-12b0-3f0f-b38f-52bfdf0134ce | -6.9514 | -59.0666 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 84203aa2-5ce8-3064-94f1-5510d98d6e91 | -10.8635 | -45.3101 | 2026-09-03 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e4860f6b-4517-36f0-8117-514b92e0fe76 | -11.0244 | -49.6872 | 2026-09-03 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9130a01e-d3e6-34d5-a3f8-5c82a571208d | -7.3486 | -60.6074 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| bc87bde2-b641-3175-8626-81f1b483e262 | -11.0063 | -49.6245 | 2026-09-03 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f24b297d-1139-31b0-81e1-9d22157c323e | -5.3264 | -60.143 | 2026-09-03 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 57c79fb7-43b9-3b86-b247-392354b52a1c | -11.2126 | -46.1066 | 2026-09-03 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| cf18cff6-30b5-387d-a2fb-cae27e2ec740 | -7.0232 | -62.9708 | 2026-09-03 15:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5d8c3c60-330e-3da4-ab37-ff9fcfa8704b | -10.8049 | -50.4832 | 2026-09-03 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7dab16a3-493a-3469-a26c-37fbd2583166 | -12.1512 | -47.0833 | 2026-09-03 15:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2ce33afd-958f-3872-a553-7c877cb03673 | -10.2401 | -50.3284 | 2026-09-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 8e11163f-a0da-3e2b-bee6-2555d638b6d5 | -10.7463 | -50.6172 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| b4629e20-2857-3041-853b-4970a0914694 | -10.7859 | -50.4852 | 2026-09-03 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f40746d8-8a1a-3348-ade6-b7947d3c8089 | -7.0786 | -56.5213 | 2026-09-03 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 1225a142-1987-3cbd-8bb0-9b1014d69779 | -7.3671 | -60.6067 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4f8175db-5362-3c5c-9651-30c0714e57eb | -7.1187 | -42.2264 | 2026-09-03 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| fa49a00b-3293-3b84-b8f8-99844667cc89 | -10.1839 | -50.2914 | 2026-09-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 54efb357-e9c5-3389-9018-9b6f39362ba1 | -10.8209 | -50.6945 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 08fd3f9e-1fa2-364d-ba42-c5eb8cc22e46 | -10.4636 | -45.317 | 2026-09-03 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 119986f4-2b14-3432-a30a-6042de7c277d | -10.8249 | -45.3382 | 2026-09-03 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 979475ac-65a2-37a9-a1da-2ef931a49101 | -10.8215 | -50.6519 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 62678235-f88d-3e8a-a830-359f794cccb9 | -10.7856 | -50.5066 | 2026-09-03 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 01747d7b-e9a6-38e2-8844-9f18de61613f | -10.7271 | -50.6405 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d51e3f41-b0d0-3f1a-b757-ccfdb29842a1 | -17.0875 | -56.874 | 2026-09-03 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| a688d548-d54d-362c-aefd-6e7eee6ea9cf | -9.6968 | -47.189 | 2026-09-03 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 110946a5-0508-3e49-8733-2170f862de94 | -11.1307 | -51.5728 | 2026-09-03 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| dd8f8bd2-06ff-3b2d-82fc-f5513b995d05 | -9.4532 | -45.6682 | 2026-09-03 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 806a5f85-66f4-3c26-967f-8cc805290f95 | -6.7451 | -59.6533 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 0944b969-59aa-34b2-a55f-2f6ae1a359ef | -10.7274 | -50.6192 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| cb7b669e-fae4-38f8-b47a-05dc6eb9e333 | -15.2281 | -53.8901 | 2026-09-03 15:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9a2d08f4-b79f-3e5d-955e-ad21e16c0803 | -10.8212 | -50.6732 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 266df4e5-9a6d-3659-8ea5-4d3d2897cb71 | -10.3394 | -49.9547 | 2026-09-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 016778bb-eb16-33b9-a415-196f61047792 | -10.7621 | -50.8495 | 2026-09-03 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e0d0f43d-dcf1-3295-907a-13ff18b0de77 | -10.4334 | -49.9878 | 2026-09-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| af67ee45-1c31-36cb-8225-630c39408b6c | -1.4752 | -54.8157 | 2026-09-03 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| f1eb98e6-2b47-335b-9877-ca4d5360536e | -9.4728 | -45.6206 | 2026-09-03 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ff7f6603-159d-35ea-93b7-bde0da23fc72 | -7.3487 | -60.5883 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 59ffea60-7b42-301c-a85e-49d7ed686a28 | -14.2537 | -52.0964 | 2026-09-03 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 15abdfd5-5fcc-3a62-9ea9-606cef99ea87 | -6.9657 | -59.7791 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f7591be0-81c9-3d23-80af-7e3bb7e81e91 | -7.3117 | -60.6089 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 259fecb3-5d11-309a-9304-ea4c04133af9 | -6.7463 | -59.4416 | 2026-09-03 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 194.4 |
| eaa06afd-329e-39df-87f2-1870f56ade49 | -5.4553 | -60.0626 | 2026-09-03 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 995494a8-18cf-35bc-ba6e-26d4bfce3e91 | -9.4813 | -60.4516 | 2026-09-03 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 2991c32b-448d-3f52-aa34-b52cbbf9ea3b | -9.4532 | -45.6682 | 2026-09-03 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 686b3dfc-5574-34b7-b256-99539419a27b | -7.3487 | -60.5883 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| bb315532-0d78-3ff3-afe2-4905b32ea11f | -7.0232 | -62.9708 | 2026-09-03 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 56c87c94-8117-3d96-90c8-7a98678ef88e | -7.9907 | -46.5177 | 2026-09-03 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 19223382-d6b6-3edb-80b3-a173ad691a92 | -17.1423 | -55.9377 | 2026-09-03 15:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |


[Clique aqui para ver as próximas entradas](README64.md)
