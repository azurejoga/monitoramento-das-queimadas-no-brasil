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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a80bbd37-ae9d-31d3-a818-045f2a38912a | -11.5373 | -50.9576 | 2026-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c989ceb8-5802-3b60-b415-e5a87bef35ac | -3.8604 | -44.0585 | 2026-09-03 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3ca21234-b6aa-3a10-98a9-dca53c992188 | -7.9239 | -44.2327 | 2026-09-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 3aa7c593-353b-3ada-a221-9645290b3b7e | -17.0875 | -56.874 | 2026-09-03 14:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| 988bf9eb-74f9-32bc-9dd9-3b5297dcef5b | -12.1316 | -47.1084 | 2026-09-03 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c0501bd2-9e02-30da-8c8e-e04c48a78a05 | -10.3205 | -49.9567 | 2026-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e78cf9ee-ba43-32f8-ad9e-90eb123e3336 | -11.5479 | -45.4676 | 2026-09-03 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| adc44d8f-d608-3dc0-9765-368752bf665d | -12.3814 | -48.1655 | 2026-09-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 60badc9f-4d69-3785-8634-ac69d58050e1 | -14.2537 | -52.0964 | 2026-09-03 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 708fa651-3b61-38b9-9590-d48ac1be41cd | -7.5324 | -60.753 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 361c467d-bfc1-3471-9bf2-78299f350b69 | -5.4553 | -60.0626 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 91b66cfc-4893-38df-bb18-324ca8d1908e | -8.0731 | -45.9049 | 2026-09-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 95bbabbe-d3b8-397d-80ff-9e5d137e074b | -8.4677 | -54.6429 | 2026-09-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| eb37cd92-3f8b-3cb6-82dd-8d4d36f01627 | -9.6839 | -48.1386 | 2026-09-03 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0110f21d-4eb7-3723-9037-28eed5497ea2 | -8.4488 | -54.6644 | 2026-09-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 54216172-a712-3cd2-bc8f-188e6e9b0124 | -7.0242 | -59.2374 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 618198b9-4aa8-3d83-8787-afdff8e62e07 | -6.8172 | -59.9578 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 267.8 |
| 17cb7fca-0018-35ad-b144-a66888fcc9c1 | -10.2214 | -50.3089 | 2026-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 399b78ed-a6a5-332a-b251-cdacb46d707c | -10.8614 | -50.4985 | 2026-09-03 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4f083708-2533-3ea0-a1a5-703a80edc1c1 | -11.1307 | -51.5728 | 2026-09-03 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9fb4d970-5228-3641-bf88-e38229890cbd | -7.5137 | -60.7919 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5564e42c-6e41-377c-b6fb-4eb87961fe3b | -7.1187 | -42.2264 | 2026-09-03 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 65696724-3c6f-3112-b9bf-f6192d877036 | -3.6232 | -54.5931 | 2026-09-03 14:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c7b43608-cd16-34b9-886b-8c6a92ddb6fe | -7.6458 | -47.1479 | 2026-09-03 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 44f88f24-9a01-3023-bf3f-0711fb80422b | -1.8019 | -47.9586 | 2026-09-03 14:40:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 09da40e3-beca-33df-b9f0-5e56b217da68 | -6.6883 | -59.9436 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 94d12469-18c7-3b85-a164-0bf9f12f235e | -12.1462 | -44.1725 | 2026-09-03 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 5fc5f900-9ea6-37fa-95b0-8d8d31fd18e1 | -3.3685 | -59.5036 | 2026-09-03 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| e81d1f3b-0089-30f1-81dc-0f6941efff60 | -12.1504 | -47.1283 | 2026-09-03 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 5f4a58fd-944a-37df-b007-c560147a69bd | -5.4737 | -60.0621 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 998c3927-77a4-3390-a729-843673652f27 | -6.9514 | -59.0666 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1fc02886-cd43-38bf-9f89-d6a3001d97ab | -12.0557 | -47.0741 | 2026-09-03 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 8684e126-f66c-3d35-8ca9-343e0c5ac4e6 | -12.3434 | -48.1485 | 2026-09-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 24f4e8d1-0a52-3a99-a2f5-989a1f54c0f0 | -13.3813 | -51.378 | 2026-09-03 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 0cf011af-016a-32c4-9779-07ccb0adb3e2 | -17.1423 | -55.9377 | 2026-09-03 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| de6a3846-d952-319a-acd0-26e8bd7c0315 | -17.0878 | -56.8534 | 2026-09-03 14:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| d2c93564-6dfa-36a0-be07-04343e8cea86 | -10.3574 | -50.0171 | 2026-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4a3f5147-6544-381d-b0bf-720995a04c44 | -13.4191 | -51.4159 | 2026-09-03 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 75cad2a7-b797-32e7-87f3-066a01b87cc1 | -12.1312 | -47.1309 | 2026-09-03 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 80274ab1-d8cd-3921-8d0d-cb0c5d2bd76f | -8.43 | -54.6858 | 2026-09-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 48ccbb2b-94d7-3327-b312-0d288c594c8a | -5.3264 | -60.143 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 610afb36-fd67-3f35-8e66-68bc20f3f77e | -9.4813 | -60.4516 | 2026-09-03 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c104be25-4b40-3255-a221-ca9f0d3241d3 | -11.3892 | -50.6972 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b4c3db89-f3f1-3498-ab63-39c1d14b4a62 | -13.6236 | -51.8158 | 2026-09-03 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d50db841-c14d-3204-8d03-8b23d9ad02eb | -11.0434 | -49.6851 | 2026-09-03 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4900c86a-6cf0-359e-9259-7225b7400961 | -17.0875 | -56.874 | 2026-09-03 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| c7139f05-319d-32bc-8a68-51e2fa5153e6 | -7.1123 | -42.7727 | 2026-09-03 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 191e496b-a6c7-3384-bef1-ab67ca75d646 | -11.4892 | -50.344 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 5541188e-fa3a-3f46-b217-8d07964ea027 | -7.3486 | -60.6074 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bd49d6aa-ed01-35fb-9920-a47666e548f8 | -7.2255 | -42.7616 | 2026-09-03 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 08bf2662-0607-3ce8-9cda-7bc37f2f9bd1 | -5.565 | -60.1739 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e1720f83-8931-31d8-8157-078b903b441d | -11.006 | -49.6461 | 2026-09-03 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d63adce8-87a1-356b-a3f5-396bfccb9951 | -7.3487 | -60.5883 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9e8e062f-2204-3ff9-94a2-c192b55f8fce | -6.6697 | -59.9635 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| f6406ecc-bb8c-34b5-8edf-5f4bec8ce053 | -7.3117 | -60.6089 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2116cadb-17b2-34b7-a374-ab84ce95fa0b | -15.2866 | -53.8617 | 2026-09-03 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| bb8212ba-2c6b-3fdc-9c28-b2e127d2700d | -3.6232 | -54.5931 | 2026-09-03 14:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ccab873d-3279-399a-8bec-507878f6a8b4 | -14.5758 | -53.5948 | 2026-09-03 14:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 13267ae1-ce07-33e2-8f1c-2e863128f232 | -10.3961 | -49.9488 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 4c7155ad-00a6-3f69-8515-d5e2a3b31c60 | -9.9915 | -46.4184 | 2026-09-03 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a3e6cd49-da88-303d-b572-8bf39170826c | -9.01 | -44.8979 | 2026-09-03 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| e14c8e43-14c0-353c-bef8-08d2d5adf8b7 | -6.9872 | -59.2582 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9b75fa0d-fe91-3a54-b61d-a63571d0bdfc | -10.4334 | -49.9878 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 51e05f7a-0f2c-350c-ba60-05e5275677a6 | -3.1996 | -61.2177 | 2026-09-03 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 6315fa8f-fec2-3002-b8a3-61934625aa55 | -3.3872 | -59.3692 | 2026-09-03 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b9060c83-84e9-3402-a9fa-0d230ad4ea8f | -12.1265 | -44.199 | 2026-09-03 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| b998227f-12af-3c3b-8c38-d137f05c35a3 | -13.3817 | -51.3566 | 2026-09-03 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 121c546f-1fc9-3ea2-9e46-adba92432a7e | -10.8249 | -45.3382 | 2026-09-03 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c7cb9628-9533-3b50-870a-97268b68dc9d | -7.5324 | -60.753 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2d5f5771-017a-3ed6-ac7a-fba327572f0e | -13.3813 | -51.378 | 2026-09-03 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 66a439c5-cd06-34dc-8745-bd6e2c719a5f | -7.4954 | -60.7736 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 933a13ef-0a4b-3834-a808-89ab11ba125e | -10.1273 | -50.2971 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a45179d2-19ef-39d6-9756-14870b143fd4 | -7.6169 | -49.9439 | 2026-09-03 14:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 1e9c35da-5cb9-3ba7-9c27-7ded7ff457d8 | -7.5139 | -60.7537 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ac95b8f9-d6ae-39be-9ade-9fce6d310a29 | -11.0063 | -49.6245 | 2026-09-03 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 89373e3b-120d-3568-b6e4-fbead65fa100 | -7.0428 | -59.2173 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fda2c101-0c88-3428-8f16-721c1b7f614c | -10.7856 | -50.5066 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5cd4f7fa-c630-3a6e-bbb5-cc8dc22783d6 | -7.1187 | -42.2264 | 2026-09-03 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| c8f37681-75b6-3f21-ae83-765dfd702079 | -7.5325 | -60.7338 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 27907f33-48f8-39ff-806e-4842039fbc29 | -14.2982 | -52.8945 | 2026-09-03 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 796fdd8f-df9c-33b6-b98a-1d52e5996a73 | -8.1345 | -45.4923 | 2026-09-03 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| f8c3e0da-2f52-3078-b2f2-967787d26e3a | -10.4636 | -45.317 | 2026-09-03 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 85659013-4bdd-3ce5-83ba-b7f04fdf7e91 | -7.0242 | -59.2374 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5e83055c-27f5-3176-be7a-94083d0df3e5 | -3.6215 | -60.566 | 2026-09-03 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 4017a262-316d-3c06-9044-2922dc8b6d75 | -6.6698 | -59.9443 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.4 |
| c3c0e2f7-a515-3a5c-8860-2bc05a73aab3 | -11.2764 | -50.6243 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c20b4c81-55cb-365e-8ea5-a0f5a3fdafc4 | -13.4191 | -51.4159 | 2026-09-03 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8264d56b-7b90-35c1-9f4a-edf130a1aa2d | -7.0232 | -62.9708 | 2026-09-03 14:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 64a8cd75-60a3-33ea-9e36-f9d1c683f923 | -6.7463 | -59.4416 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 651c00fd-a40c-3d5e-84be-383651cef817 | -10.8807 | -50.4751 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 835add44-ab10-3bee-86f5-82a6b8132eb9 | -7.5137 | -60.7919 | 2026-09-03 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 612fa12f-14fa-35f7-a1ba-646d47b33043 | -8.7615 | -62.5679 | 2026-09-03 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ed70ae84-f421-3819-825b-21d6da5ce995 | -10.5278 | -49.9993 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c51a75b2-108f-33c3-b557-f0f57af92fa0 | -3.7533 | -59.3231 | 2026-09-03 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f87e39ce-64e9-3cfc-81dd-6bfe7f34940b | -7.3118 | -60.5897 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| fc6d2e99-f4a7-3867-9d3d-9ca097d1b7de | -10.4716 | -49.9624 | 2026-09-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 51eb9827-f14a-376f-8386-14d0b8a5e02c | -6.9513 | -59.0859 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 25132028-fba5-3893-b9c9-5a1f69f98cb0 | -11.025 | -49.644 | 2026-09-03 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 636a04e2-d14f-3a61-a240-e2ffa1dead03 | -10.8049 | -50.4832 | 2026-09-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5a902329-988c-364f-97b7-2f6c836a7d47 | -6.9657 | -59.7791 | 2026-09-03 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |


[Clique aqui para ver as próximas entradas](README63.md)
