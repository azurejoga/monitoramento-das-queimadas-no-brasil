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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a8fdd84-edf3-361c-be38-fe2b88aba04f | -4.1095 | -50.99257 | 2026-08-15 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b84faf88-ed21-330f-b8e7-0efe8fdae1ce | -5.34466 | -43.17876 | 2026-08-15 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be87a5e1-f488-36eb-af2a-cd6f3782a4da | -6.1411 | -57.90119 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d6bf6f5-79b1-3944-a857-b03f5705c8e8 | -2.22546 | -51.93761 | 2026-08-15 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74483fba-d8e5-3d40-9b18-201f2c0a10a6 | -6.59871 | -56.3542 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb198f6-80f8-320d-b3ce-089783c9beb3 | -6.60072 | -59.00633 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a6a83e54-5f3a-3743-adb6-2c629a0f91c8 | -3.9725 | -49.46272 | 2026-08-15 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8caa163-7b98-3076-9b20-1a8431789427 | -6.01876 | -57.82985 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7e238a5-dba2-33dc-aed5-fd1e0841aa50 | -6.78692 | -55.83059 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af969151-05d1-3f14-bb65-f366a2a21116 | -4.10822 | -49.04844 | 2026-08-15 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4ae189f-8b74-3aeb-8dd2-a364caf0d713 | -6.61196 | -56.33671 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d8d4c80-48b3-3c27-abd1-88c7c0570d1d | -6.8622 | -56.41869 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebf27e45-900f-3736-b418-c6fc9e3a97e6 | -4.10638 | -50.4431 | 2026-08-15 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 195d22d7-3817-35b2-a8a6-8469d619e3af | -4.31188 | -59.47346 | 2026-08-15 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade50277-b3c8-3d2b-ac9c-f463b2e92145 | -6.83376 | -56.4641 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c35d0b3-3a31-33f6-a8f5-775b61f910e2 | -6.01804 | -57.83432 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf1085b3-4bc2-34c4-90a6-2133e3d0dc90 | -7.81283 | -44.11233 | 2026-08-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d09aebb-7c29-3a4d-8528-f4fe18a33c64 | -7.46146 | -55.30484 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35be8df2-19c3-3aad-8fc4-034da26bf019 | -4.10918 | -42.50695 | 2026-08-15 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c61c85db-428b-3ef2-a14d-28fb833cc429 | -7.06656 | -56.65613 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7677a2c-a2a1-3041-a13f-724f7bf677e7 | -7.72957 | -46.24778 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67524412-f5a7-3a60-aa4f-b1d27e131f6f | -6.84405 | -58.97371 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca7afc29-c0f0-3104-8090-660997153a70 | -8.55828 | -54.59935 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b167cacc-3274-333c-9d1f-0475e7e5d356 | -4.10909 | -42.50916 | 2026-08-15 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 60a8606b-3e5c-372d-bbe1-b6ce363dd596 | -6.33645 | -44.0718 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5282edb6-eb97-3c91-9b9d-8fd38bffb37b | -7.8181 | -44.11732 | 2026-08-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9924f422-4016-350f-a6bf-bae3fab62782 | -6.64229 | -56.41059 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 975b0796-7ec3-3284-89cd-904a4da94624 | -6.96331 | -59.299 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2cc4e974-4ed5-3ed3-aced-77bad57236d4 | -6.95763 | -59.28388 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 344eab9d-c035-3a92-a7ec-aa03cd438b92 | -7.4171 | -60.0049 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69cb26a7-9ce4-36b9-b446-df73bc3e2181 | -3.11509 | -47.90657 | 2026-08-15 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 514dce18-f863-34c7-965d-6c55a9d8c54a | -6.86709 | -43.8751 | 2026-08-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d15abeff-4202-3864-b46d-ab5d73c33b83 | -3.74581 | -59.3281 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adea14d4-c58d-3035-ab03-410061b29b08 | -8.94188 | -47.60167 | 2026-08-15 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304d7bef-c3fe-332e-8674-9a4ad9a589aa | -6.61964 | -58.99091 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cdf6198-4cf7-3142-9b33-75f7e14c567a | -6.63483 | -56.26035 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3cb0bad-daa3-35d9-8473-c355105caa1e | -6.5993 | -56.35046 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2718507e-b440-30a6-b63e-9d0e51f67b79 | -6.61666 | -59.05566 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 45659693-44db-381a-a8ed-a9967bdb4fec | -2.69211 | -48.21833 | 2026-08-15 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa205bf6-896b-365b-8921-98ebb05e6262 | -6.79423 | -55.82804 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 010fe19d-ce45-3886-b055-5cd014e585cc | -5.93272 | -43.64458 | 2026-08-15 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfbdaa12-3b61-3af8-ba2e-f43420bbdb6a | -9.56782 | -45.38078 | 2026-08-15 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4020d9a-9c0e-3916-95b6-57867e4af59f | -7.39021 | -60.00003 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 228707b4-ca00-350c-bced-a873ccebb036 | -6.81192 | -56.42654 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0fefeab-19f3-34be-b918-1c58ff91fc5f | -2.41488 | -48.72513 | 2026-08-15 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d04616a-4d2b-3eea-b289-4dc8a3a1b9f3 | -2.64547 | -47.97752 | 2026-08-15 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a044647-2c56-3189-92e5-a09b15839c3f | -8.36508 | -46.38384 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e9a12e4-0999-3202-b479-8bc6960fb132 | -6.62027 | -59.08239 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06c32132-1631-3b16-9344-6f644833d354 | -6.72067 | -58.93871 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ef221d1-0752-39b8-849b-983a1ffb9508 | -9.57508 | -45.36782 | 2026-08-15 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 325f3f3c-b566-358e-8fb5-6283334d12b8 | -6.60551 | -59.00193 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 53cbedbb-dfa1-3e51-abd7-da8183f97140 | -6.2047 | -57.76798 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 741d2159-860e-3fae-ba66-9c4476c2e357 | -6.61803 | -59.07158 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4f87c3d7-83c2-3174-aa23-50878f96945c | -5.66995 | -43.57452 | 2026-08-15 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 450abef9-b521-3512-aa96-28e45c430365 | -6.79082 | -55.8497 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47294ff2-6e1d-354a-8d7a-15ae99bc7480 | -6.63022 | -56.26722 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be1e47f8-3c3a-3510-8231-fa4d14dfd2c9 | -6.61272 | -59.05499 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24a9f3b9-1fc4-3c82-bd99-daf24899eed6 | -8.71817 | -49.60165 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 385b74d8-767d-3a30-8278-573714663245 | -6.3416 | -44.07673 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ebdd734-d5ab-3983-b2db-185c4286ab74 | -6.61508 | -58.9931 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bfe8803e-9689-39d3-b22f-8e98e3863575 | -3.26085 | -49.52798 | 2026-08-15 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cb60505-1187-32a6-8842-894ef4d95d89 | -6.11699 | -44.02995 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9f1287cd-6c7a-3243-8cdc-d78413527c66 | -6.995 | -45.8981 | 2026-08-15 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 905353d3-3d8f-319e-8b90-9c43fbc746ad | -6.59007 | -56.36432 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfd913f3-811b-3667-b9b0-c75d7b88b7dd | -6.62625 | -59.04679 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dde0176-6ee3-3bcd-99be-642fa2442211 | -8.51889 | -46.53144 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eac790d7-e58f-32e7-af4b-675b53a52764 | -4.64061 | -55.70645 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f71239f-3d8d-342d-b560-184c5686809e | -8.01924 | -55.13281 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a73dd3e7-abfe-3522-baf8-7644c7b1b0a0 | -6.619 | -58.99379 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29c28fc3-1e57-3e96-a2e2-e39e173074cb | -6.79029 | -55.83112 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36206103-8e60-327c-a9d6-521709456d14 | -6.14183 | -57.89678 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b99099e-a136-359d-ae96-c8f265cfc41c | -6.57449 | -55.14909 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 744662da-00bc-3707-980c-ec6fc092aebe | -6.61883 | -56.33773 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7230f358-d7ca-35cf-ae22-0e0b75ba0a6f | -5.14121 | -50.85131 | 2026-08-15 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3deba81-d923-3a2b-8bf4-810764bc4648 | -7.00419 | -41.43826 | 2026-08-15 04:57:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2d618c8-54e9-35c0-bb49-123cfdea42f3 | -7.01182 | -41.43255 | 2026-08-15 04:57:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c991fa8-35a7-3364-bc2d-ebf0b5641287 | -6.61883 | -58.99592 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dd4d8711-1ccc-3063-b870-d9c045c66853 | -6.79568 | -55.85094 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fdbb581-edea-3882-b67d-8da4cb40fd2c | -6.79476 | -55.84662 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a25924d0-7520-3a88-9809-a634c54289cc | -3.23711 | -61.16891 | 2026-08-15 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42d356b5-f880-32fe-88c7-cb66b24b2dbe | -5.49849 | -60.14654 | 2026-08-15 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 801404fd-8f5c-3423-8708-a57a7eecc3b7 | -6.7956 | -55.6883 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a20027f7-d7b3-39ca-84f9-be5bf178d391 | -3.75537 | -50.79917 | 2026-08-15 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbf17f7a-96ff-3dfa-8fb9-2a7debda7200 | -8.45527 | -45.11572 | 2026-08-15 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb1f74f2-00f6-37b6-b914-c156273319b4 | -6.14307 | -57.89802 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00b42063-f52c-3c72-8c30-74d448b068c0 | -8.71776 | -49.60519 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fe9b3ad-3923-32d2-9c9f-f4292b01ad79 | -6.93969 | -44.54289 | 2026-08-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae389048-2af0-3161-a26e-b0787b962892 | -6.96274 | -59.27765 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a302202c-0062-36f3-b5e5-8a3642fcdce8 | -3.94362 | -59.629 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1def141b-510b-3ae0-b836-fdeaaf683b9d | -3.24377 | -60.12618 | 2026-08-15 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad9be3da-1eaa-3e6a-ad30-1cbdfa016e95 | -8.02255 | -55.13333 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a08e408b-f4c8-3bd9-a850-4e0aa18a1358 | -7.28237 | -44.67633 | 2026-08-15 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 65420c6b-6cf8-3fcc-8cfb-0d1f06e0e394 | -6.02245 | -57.83048 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48e07caf-4a35-3d90-aeeb-b87b74f215da | -6.96502 | -59.28862 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 342b347f-673e-3a4c-96d8-9b4a2836fad3 | -6.79742 | -55.84011 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58066f25-6238-395b-bbf4-d8a958592afc | -1.78311 | -55.53151 | 2026-08-15 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 268fff3b-2f6d-3e14-a1f1-09d61517dfa5 | -6.88275 | -56.5106 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c68962a-c657-375d-a1a7-4c252af05af1 | -6.60333 | -56.34723 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3940027d-79fd-318c-a9e8-4b67fec0688c | -8.03193 | -55.1384 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 31808668-cd41-39cc-bc3d-a3ccaaf0a162 | -2.64961 | -47.97818 | 2026-08-15 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README25.md)
