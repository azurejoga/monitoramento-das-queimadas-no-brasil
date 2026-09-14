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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ec4df40-0204-36c7-8e2a-72fb2dd40b6a | -7.1046 | -41.79898 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5574c6c9-1287-34f4-931d-61e175137916 | -7.96938 | -43.98677 | 2026-09-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d12b62ca-254f-3c1d-80ac-78577749d5ac | -9.38234 | -50.08299 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 889ac98e-dd6e-3143-b31f-9cd87a751972 | -4.97795 | -56.13479 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b499376-b2ba-3746-9723-2e20266af0a8 | -4.13884 | -54.01546 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4102086-13fe-3f22-ae51-7975953a7583 | -9.44186 | -50.13011 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76523fc2-dade-34f8-8435-ee1cb536c2c3 | -10.94978 | -48.3614 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71a254a6-07b8-3341-8abd-0410fe8801e4 | -5.90138 | -52.09912 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22915c70-5191-3e4d-ae6c-5f0ae8b4e067 | -9.55193 | -51.35793 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 442b161e-bbe7-3de2-82cb-3d660b43a3d1 | -9.40108 | -50.16561 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cd9f340c-f0bd-368c-8d42-fce764e4005c | -6.36379 | -57.86831 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6255adaa-7825-30e4-8256-4b1e510d4f65 | -9.41528 | -50.16402 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6d34ef05-1daf-335d-b297-c056d70652cf | -5.1324 | -55.95484 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 41b66fcd-8153-3748-81ab-78b1874fe965 | -6.50928 | -47.59964 | 2026-09-14 04:53:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e2c4fcb-0f49-37e7-913f-33ca0ca8ce63 | -12.17455 | -48.96929 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba85e0da-1033-319f-bcd2-a24eae2de331 | -11.20658 | -46.4248 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbb2e538-2dc4-3ae2-90fd-9928cbdc0b0b | -11.04931 | -49.57417 | 2026-09-14 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 398c98d8-6d2f-36de-9129-38eb569c95a8 | -10.58299 | -51.34028 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f87a6ff4-4101-3911-8d45-7c990edb9b11 | -6.57884 | -58.83974 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6a9546e-996b-33ef-b3c5-27769686e784 | -6.01742 | -59.94311 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f228d56-b727-3da6-abb8-80f4a08f99ba | -10.54521 | -51.30149 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e071f6b-61a5-3d86-a0e2-2e16cd59565a | -3.52905 | -59.06765 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86e6c012-10ed-3c50-b6ca-62d630c195bb | -7.10181 | -42.10276 | 2026-09-14 04:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 01125569-18a3-3d7d-a05f-5e7492b8d721 | -4.11876 | -60.68365 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e1694c56-4f43-34ce-9625-0a3f2afc6656 | -10.77087 | -48.97202 | 2026-09-14 04:53:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c118d62-d4ee-319e-b552-515475864138 | -3.4086 | -58.2127 | 2026-09-14 04:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9693f04e-f4c8-3388-bece-d3e15e21a8b8 | -6.32202 | -60.02221 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4965a320-3fe2-3d65-9cc8-74e3548cd067 | -10.66283 | -54.14388 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2f92fbaa-02ba-312b-8220-5c8e67796400 | -7.02006 | -44.63321 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fc4f60a-6952-3422-a390-0ee3b9e3649c | -10.68429 | -54.16295 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04444ebf-d56b-3e45-8bec-62f4b39affff | -10.10937 | -48.85162 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f765bea9-41c8-3479-b2ef-a9754d5f6e5e | -15.56509 | -48.79152 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7046f165-b234-3c93-8894-d23a1d3d016f | -10.548 | -51.32738 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcc0c236-1673-3767-9d6c-fcbfbbf40950 | -6.10737 | -55.66663 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d99ca83-ab44-390c-9e18-e505a2af62e5 | -7.09548 | -42.10877 | 2026-09-14 04:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0b75b3c2-890e-3721-8ecb-4dbe5f23a54a | -10.35991 | -46.6515 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e32ef129-cfd9-36cf-bc1b-0feeded44709 | -6.15177 | -57.69075 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d019e802-025d-3390-858c-46a48d88b4fb | -4.53781 | -54.93549 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64822b43-1b4e-31ac-a688-b914866eee84 | -7.11012 | -41.79967 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3b88d811-a1b9-3678-975d-03f8fd4072a0 | -9.42554 | -50.1201 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| e86bf5f8-7ab1-34ca-92a9-8c1c43aef70d | -8.44352 | -46.02769 | 2026-09-14 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5348b61-ffe4-33d8-a336-161ab140df28 | -6.79357 | -58.79157 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fb475d53-69c3-3dc4-81f5-f85c05d635a0 | -10.66687 | -54.14071 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 69524529-d0f3-3cd3-848a-cd3e02d3c5f2 | -6.6402 | -58.82576 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05668e76-57e1-38e8-910f-c4fbb9bf0ce5 | -6.27891 | -59.92576 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24f7f4e5-f950-37be-b17b-adc465952e2b | -7.77361 | -46.67049 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3e1720b-1667-3c30-a0a9-c52b5a6c87ca | -6.58232 | -58.84739 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca2c16c8-825b-3d51-9dbb-65e948486006 | -9.45265 | -50.12798 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4ea27af-daba-3bb1-a918-9432e6e65da4 | -6.86706 | -55.29671 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c051920-04c0-3656-945f-38c0cf947521 | -4.1275 | -60.6823 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ce11435-b125-35c5-a049-31fbaf07108b | -9.44492 | -47.87534 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4006ef85-85c7-3581-83d8-ee7d4491d119 | -9.14022 | -51.5785 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f114b974-cfc1-3be6-a3f2-529e6ab96c62 | -6.58393 | -58.86758 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a664243-ed5f-35f4-a4a2-fd9a54e3f975 | -3.39159 | -59.41351 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab6dee8-39d1-33b9-96ce-90a2ddac4f55 | -9.12864 | -51.58736 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb4de8ef-fa24-37ee-82b8-da49e0f4be32 | -9.39993 | -50.19571 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b095d1dd-77ca-3b50-93b8-9a9452bc309f | -5.08024 | -56.2499 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f868794-9bd0-3191-aeb2-a3c8e0431a6c | -9.40449 | -50.16614 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 055e1daa-0646-3dd0-92c3-4ec6771b80db | -6.10944 | -57.86198 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbc1258c-dd18-35e5-86bd-c87ffa67a74f | -5.90749 | -52.10371 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb73cb71-b69c-3c72-96f3-35c352b979e4 | -11.42623 | -45.14371 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f950a8f7-9e7f-3903-9525-0da8706b7de8 | -7.07263 | -43.55524 | 2026-09-14 04:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd4166b7-451f-3db7-9de4-8c84c5a34e83 | -9.40325 | -47.86906 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e51dba5-9378-3a31-a26d-92cc95dd032c | -5.8008 | -52.11171 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2499ff1-6b2e-3982-9758-d090f9fa05f5 | -6.34008 | -43.36715 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f60ade81-3505-3949-a4e2-ae077587363a | -6.69065 | -43.14299 | 2026-09-14 04:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8acc3a8e-20d0-38df-aab4-7d3627fd927e | -5.84764 | -52.05424 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fc135f4-864c-3aa6-8b80-5c1a928ed645 | -9.44802 | -47.8805 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59816156-b06d-3d35-a203-2afc7f8f8929 | -9.71857 | -50.85447 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b474a8a1-7761-3e2a-9ac6-259974f9eb55 | -6.59526 | -58.85881 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfddcb72-4c9c-33c8-8935-a74cf954b2d3 | -7.95906 | -43.99044 | 2026-09-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7d91ba3-b7a6-3362-8756-4bbf2135a76b | -3.72748 | -61.75792 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3e2d49a-386b-35b0-bc45-0b31c641fb57 | -9.19951 | -60.39291 | 2026-09-14 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39f7a78f-031b-37da-b310-3f4e526488f2 | -10.6765 | -54.14622 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68a3346c-34c3-3c5e-968e-620293e3073e | -10.37026 | -46.66778 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddb45d48-b3ce-3f68-8f90-e1792a031694 | -6.28699 | -55.28653 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8992c5fa-aaa6-3586-8159-6e62930bf58f | -5.08269 | -56.25263 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83e82c0d-8708-348b-a61b-a1fd8996d3c0 | -8.9155 | -45.44516 | 2026-09-14 04:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9e03ff3-475f-3084-8599-6f0f1eb8a8a4 | -9.59245 | -55.14995 | 2026-09-14 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 908b7dda-1de7-3b01-bb08-67e4685d8973 | -10.70242 | -47.52408 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6caf0838-6bfb-36bb-b045-af9cb2592501 | -7.09595 | -42.1054 | 2026-09-14 04:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1f8decdc-8bef-3779-9c88-91b144c040bb | -9.36647 | -50.16403 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fce4696c-80e2-327e-aa58-4454562381a3 | -9.36759 | -50.13388 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58805113-125a-362e-aa50-b572f0030f91 | -10.95769 | -58.95728 | 2026-09-14 04:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73edca1-91ca-3107-9cdc-1744e4f57b38 | -10.96105 | -48.36306 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab245f1d-44e9-3c00-9c94-5a0685d95a86 | -10.1009 | -48.85887 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a97091ca-b418-30c3-8c8a-816cec901d6d | -7.0568 | -45.22848 | 2026-09-14 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07b727ca-dd10-3a2a-86fb-37c1bd5aa0d8 | -9.41872 | -50.11905 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4c7e8936-d0bb-3007-95aa-4776e31185d8 | -5.83531 | -52.11002 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c5d5dbb-144a-3224-9a1d-8af7bf7ac9f4 | -5.84813 | -52.09406 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cf666a7c-57aa-389c-8d9f-928b271d8b11 | -3.72775 | -61.75138 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b8511b1-6715-3a17-824a-733511f05a84 | -3.73513 | -61.7499 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12f0e53a-171b-33e5-8fa1-4b184e879683 | -6.27268 | -59.931 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd98dbd7-b8b8-3044-a80f-5009aad448d0 | -9.55525 | -51.35846 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d788fbc4-7aa4-33f7-8bf9-0edb61d5ac8a | -6.65053 | -59.96567 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69e8d887-a9dc-39d2-ae32-9070262f95d4 | -4.53856 | -54.9308 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ef6de78-ed25-38ed-9114-88b5cd6a239b | -10.47025 | -51.32243 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0152aad3-1535-338c-8aab-91f1c8bea934 | -10.54855 | -51.30199 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09047fc5-c6f1-3a39-b201-860efe833a2c | -10.46736 | -51.25287 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62238e69-8b1f-399b-b800-f8b5eed056aa | -6.36884 | -58.30045 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README47.md)
