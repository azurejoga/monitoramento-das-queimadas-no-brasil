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
| bafa170c-79ed-319c-83ca-3023c7262641 | -10.2743 | -64.4907 | 2025-08-27 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| d0a2e19d-d7b8-3a7c-8748-5bd2da92c80a | -6.8412 | -58.9746 | 2025-08-27 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0907dbec-a98a-3253-8d2c-d491424da89f | -9.0819 | -49.5853 | 2025-08-27 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 034b1bef-5a26-3837-a3c8-010a2cfe3c22 | -9.7915 | -64.265 | 2025-08-27 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a79d8aff-f66e-3b66-bcb4-e36590600693 | -19.5767 | -47.5367 | 2025-08-27 01:10:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9a1d8b29-4243-3223-b7e2-f0121ddf995c | -8.9013 | -60.763802 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04efb6be-b816-3088-a18f-eed96d5a9341 | -8.9661 | -65.947098 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45fd4f50-bd46-374b-9707-f8b0042edf3a | -9.3983 | -60.5056 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef9939b3-6a2f-3665-a70a-197da989815d | -9.1967 | -59.523399 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35d20b58-0d23-3452-aec7-99d1983faad5 | -7.6992 | -45.770302 | 2025-08-27 01:11:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5137f97d-0575-3c81-9add-a901e376c3ca | -8.9322 | -65.9291 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0ae6951-21f0-35e2-bd20-6919087f7e20 | -9.1792 | -59.442902 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0462422-91a2-34ba-9595-4f92977966f4 | -9.5898 | -55.373798 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfe82e4-7895-313f-9ba5-02637b29e31a | -9.7997 | -64.2314 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 964e45b1-9cb3-3054-8499-066414399204 | -3.4199 | -49.0355 | 2025-08-27 01:11:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3053771-b8b2-35f9-8054-30159390ffba | -9.0812 | -49.576801 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54f133d8-034f-3919-a65e-40875abe13f5 | -7.348 | -59.655701 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cccb4519-1899-36d3-b1f1-3c4dbeefa453 | -9.0878 | -49.562 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd7267a2-aa06-3b9f-b158-501c9ee47948 | -9.2755 | -56.899601 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18645d2b-7d66-38df-853e-e8bed9472d62 | -9.6012 | -55.378502 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 959c48f8-33ef-3e12-948d-3c4bc541beab | -8.9177 | -65.907501 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c047a8bb-68ed-3176-a60b-e0b9cd13ee62 | -6.2444 | -60.005199 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26393af5-9c7a-38b7-9b3d-7056fb5a9ac8 | -9.4179 | -60.5014 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87664e34-53c9-32b8-8422-56f6b2abaddc | -4.0975 | -55.8055 | 2025-08-27 01:11:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9687a3b-7b0a-307b-85a9-47c0072f4027 | -6.5737 | -47.366798 | 2025-08-27 01:11:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2429efa-c547-3913-bccf-cf25648f4fd9 | -6.7151 | -58.565899 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d98d1389-a3a2-3d89-a883-f40b6cdd83c2 | -10.0912 | -62.881199 | 2025-08-27 01:11:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0567384-1a07-38bf-99f9-37b9ad4c043b | -9.6417 | -59.637501 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 042d1384-d192-30f0-87bd-d17e7f48658c | -9.1134 | -49.581902 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d615253-94b5-3268-8910-d44205f86e3e | -8.9111 | -60.761799 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2da4ebe-1f29-366d-b9ff-33bc3e82ee58 | -6.8132 | -58.958801 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 111dc736-bf14-3cd0-ab24-0d3e2ceac56d | -9.1575 | -59.531799 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 046be5f2-7497-331b-bb03-0f38b15be05b | -9.185 | -59.516499 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 013817b5-217e-3088-9b35-e4ee3b76bcb7 | -7.2884 | -46.980301 | 2025-08-27 01:11:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c48ca1f6-a5f4-3715-bfbf-0f0e9974261a | -9.4135 | -60.480801 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef417d74-096e-3984-8c2c-7399280c7fb6 | -9.2786 | -56.913799 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc064d4d-3391-3068-b328-bd5f6226a8c2 | -10.5229 | -57.980099 | 2025-08-27 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 549f888a-89e3-3f01-bb05-ecc577962f19 | -21.573601 | -47.482101 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8539088f-ddbe-341c-a12f-931c04850021 | -8.3396 | -62.919998 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05c1e582-582c-32ef-af36-2e6d2d7cd311 | -9.1006 | -49.571999 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9de079-8bbb-32c1-b0b9-5d32c7ee8dd1 | -9.4148 | -60.5345 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c005821-3d60-330b-bb2a-2d92884d0446 | -9.5785 | -55.369099 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17deca80-a3d9-3527-a67e-7cabbad49db8 | -9.0678 | -66.051697 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba2fbbcf-ff40-3bd9-984a-6509627b5187 | -9.5246 | -60.522099 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e539dcd-9238-35be-bfab-a13aee17749f | -8.1332 | -55.364601 | 2025-08-27 01:11:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08cac0c4-0834-3b5f-b855-0847d6fd8375 | -5.8007 | -59.2141 | 2025-08-27 01:11:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbd0b6ed-18d2-33b8-a21f-1b45c237257b | -19.569201 | -47.532398 | 2025-08-27 01:11:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f820581a-d7ec-31cf-a3c6-f8dd63b88722 | -9.1732 | -59.509602 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba04d3b-9100-37ca-8b0c-5fc074e87275 | -8.9371 | -65.903603 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be8ca2db-f18b-31e7-acc8-5cd3d6465935 | -8.9613 | -65.923302 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3c8bdbc-afc0-3893-96ef-65fa9c16af5f | -9.9232 | -54.712502 | 2025-08-27 01:11:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1448ad57-77e1-3694-8125-189770d5e445 | -6.2542 | -60.002998 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69e33ea1-c1d1-39a1-a261-82b5d471fe85 | -9.2542 | -56.8969 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f52ee55-c23a-33e1-8785-5d9b93a6e349 | -6.6274 | -53.327499 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf07850-0ccb-3a24-a5f5-e49a9a240422 | -6.8346 | -58.962399 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebd6c02c-a7cc-399e-9d7e-9cb4bb6a0f3c | -9.2698 | -59.7659 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29d02ae1-2c6f-3207-9b76-be3eca51147f | -9.2382 | -60.904701 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3762f4-8305-3198-a97a-114087fb6646 | -21.576401 | -47.493099 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ab09192e-ae25-3a60-9d55-93e7b4333c10 | -7.357 | -57.619202 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 361b3881-364d-30f3-83cd-02a5919000c3 | -9.0647 | -49.594002 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dafad930-c889-3f0d-bb91-2eba287ec589 | -4.9645 | -55.807098 | 2025-08-27 01:11:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93529bd1-a30d-3cd4-85ae-ef341c4149b4 | -9.1595 | -59.540798 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 646e850a-3d15-3eb0-b589-53d2900bed2c | -7.2838 | -47.002602 | 2025-08-27 01:11:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05c9623c-c31d-3c79-a092-bb44f34988e6 | -9.0976 | -49.559601 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1908edf1-4892-3b61-9215-a9f6b0cab209 | -9.0806 | -49.616299 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1939bc58-49e8-3490-a618-8fdbbb6d0024 | -9.5914 | -55.380699 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e69309e-13a6-3b3e-84c3-cf6f4c3f0701 | -10.4125 | -57.711498 | 2025-08-27 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06737e3d-2822-3c93-97d1-b95f5b32d517 | -7.3597 | -59.6623 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f372d307-12f7-3f6d-a93a-867a922238ee | -9.4075 | -62.477901 | 2025-08-27 01:11:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1c7225-c02c-3047-95b4-6322096116a1 | -9.5687 | -55.371399 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce145f1e-2413-357a-9124-0b0d8ce3bb0d | -7.2572 | -57.6791 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a09bbb-fcb2-30ab-a5dd-0b14639d1e99 | -9.4028 | -60.526299 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab11ad0f-9848-3244-a164-7097535c29e6 | -21.5791 | -47.504101 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a3ba16e6-8bdc-3344-a025-dcdb75c9d6a5 | -10.2776 | -64.4944 | 2025-08-27 01:11:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 240d7fd0-7949-3efa-8dc3-d1ba3f1ac2f9 | -21.34 | -46.9347 | 2025-08-27 01:11:00 | METOP-C | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1b4d96-728a-3823-acf8-a1d1b7727fc4 | -7.3587 | -57.6264 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e62f4e1b-a505-3adb-ab2d-9b4de471b512 | -6.8115 | -58.950901 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea47b1f-db4d-39b0-b6e6-0771118dff16 | -9.6495 | -59.626099 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10bff38a-3f05-3396-afb5-6b3f78dd6b88 | -6.2463 | -60.013901 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4232a741-d5b2-312d-bec3-fd333e9c7c46 | -8.8586 | -62.4347 | 2025-08-27 01:11:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 181c7abd-48e9-3783-91bc-0faa749a4329 | -9.1595 | -59.5881 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e310cfde-066f-3aef-a86c-a517d2977e42 | -7.2752 | -57.6675 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb284e2-db23-3677-8385-d4501504a540 | -7.4404 | -57.623299 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2313ea3e-dc4e-34c3-b51a-84e917c2c9d3 | -6.7667 | -59.674198 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 479b2331-3943-3e1e-8971-af8aaf3b29d3 | -9.6397 | -59.628201 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af30a298-e34d-3f4d-90b1-2af90651e51d | -10.6043 | -54.8932 | 2025-08-27 01:11:00 | METOP-C | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e18d9d41-413f-3f84-9e5b-237d68855517 | -22.558001 | -49.758202 | 2025-08-27 01:11:00 | METOP-C | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 728e7333-1729-38a3-8bd0-4c4cc2a66f78 | -9.4246 | -60.532398 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c21f9b82-4a4f-3296-aaca-9b36c44cb8c6 | -9.58 | -55.375999 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e72db6-126e-32fc-a8e9-2577fff00c15 | -9.183 | -59.5075 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d808ed3-e5f8-3d16-97ce-df132597b171 | -9.4037 | -60.482899 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aeee134f-4e8c-319f-bf5b-0ee629b27611 | -9.1732 | -59.556702 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc82cd54-76a1-3148-b03d-e5ee4280ceec | -8.9096 | -60.707298 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8968abc7-7cc1-3531-85cb-622219f57ecf | -7.7507 | -61.075199 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9db6d461-1393-3130-bf4b-d395a2c81db8 | -9.8094 | -64.229401 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15133991-e94e-3c6b-9780-2325227a7f48 | -8.5389 | -62.658199 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c5e8892-0db3-3888-a25a-37e4058d2400 | -9.1812 | -59.451801 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84273950-8509-3b4f-a9a2-e73c314d2ca1 | -10.4109 | -57.703899 | 2025-08-27 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7ce6e3-2c3e-3a80-97f7-0fb3c2b1bb9a | -7.1714 | -59.739601 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc4831ff-6347-399d-b646-d30264d5556c | -9.1853 | -60.848099 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
