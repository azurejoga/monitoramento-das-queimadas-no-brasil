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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9320e75d-ec38-33fe-a836-edb914efe6ab | -5.14583 | -55.96947 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a97645-6da3-3035-a1d4-4f55749f5fb8 | -3.14412 | -60.65197 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e24a9c-9579-3a51-8465-a351e1ef8ba3 | -6.44377 | -58.15221 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98deeb10-89f8-3ce8-91b9-56073fd88a0b | -3.76333 | -61.75368 | 2026-09-07 05:23:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 913d9e52-0c3c-3e09-9bff-032b18779bb5 | -1.86417 | -47.98342 | 2026-09-07 05:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d74ec9e0-f6bb-31e0-b1be-8d3906595f23 | -4.97936 | -50.63228 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89714395-940d-370d-ba59-8c3d0eb3bf0b | -3.61049 | -60.56592 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d1b7912-ea78-3743-aa1d-eb276635df5d | -5.14478 | -55.95272 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30ed5329-3d44-3847-a22d-faa16b6f6cb5 | -5.36485 | -56.04398 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa98790-e329-360c-afc6-4b91cd69fb73 | -5.27065 | -59.96239 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1581c8cc-3050-34e5-ba7c-5e0f58f8c909 | -5.16134 | -55.96363 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b44ca70b-bba1-3fe2-a69a-e9754ecb4fb7 | -3.77576 | -58.85125 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3868edd-4d8b-360f-8ae7-08c539622843 | -3.41378 | -61.31628 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af406484-bd9c-32b2-90d0-21569cca8e80 | -6.12254 | -57.70526 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bc25e06-f711-3fe7-a299-2cbed6c069e4 | -8.73105 | -62.43565 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d143bd2-dd28-3374-8bdf-66415eab73e8 | -5.98892 | -57.6881 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9b726d-cc0e-3431-bc56-1f7b43005a85 | -5.26315 | -60.11741 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c117f97b-a3e7-31e9-af1c-caafc76b7357 | -5.65134 | -60.23725 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 579794d9-9fdf-32ba-acbc-b064ceae12e2 | -6.1338 | -57.74374 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 954f90cb-0b14-314e-b484-a09fa4b84e2f | -5.99007 | -57.70301 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cd8f93b4-ccbf-3cea-a058-728d9ed227e9 | -6.01532 | -57.69584 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2820e0ae-8a8b-32ea-af99-f29a42e7f755 | -5.99903 | -57.68964 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b4b409-7eaa-3043-902c-16ec29d3803f | -3.38729 | -61.345 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07dc14ab-dfe0-3f7a-9d31-c83434705186 | -4.07871 | -48.95634 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8150a58a-0c39-3177-bf6d-57f5329c01d3 | -5.29895 | -55.86011 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d8d9514-072d-32f3-98a6-607a0f28e921 | -5.26372 | -60.11385 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6329436-dbe7-3186-b752-a5bf74fb1cc1 | -3.12063 | -57.68792 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91a23375-2426-3323-8924-f057cf094195 | -11.64702 | -52.86651 | 2026-09-07 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb7e17d9-26c7-3231-9381-3eff8e1c2144 | -3.0826 | -61.53434 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da9ed933-e03a-3a3c-a18e-4bc8554538ca | -5.45645 | -57.18821 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0966ebd-bd27-3229-a6cc-b38d9c091b51 | -12.75759 | -52.86187 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19264f11-2313-397c-9a6e-827d2095cf98 | -5.28758 | -60.12879 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57d1f3c7-86d3-3e05-ba15-6ea1d362cc52 | -5.29371 | -60.13342 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75311ee2-ae4c-3aa5-af0e-27fd4337c48d | -6.446 | -58.15981 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5330a684-3578-3590-84d0-8447d0955657 | -5.57589 | -60.02956 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5133ae2-6ec1-38f5-a234-0818c5d7d396 | -4.15303 | -60.70409 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 774c0f9f-0069-3897-b8a7-ee17cca006ef | -3.72033 | -59.3715 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445c8bf6-5090-350e-9151-705c0709c8b4 | -3.13558 | -60.63897 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7f458c5-f7b2-3ff6-bbde-1400a96c834a | -8.71557 | -62.44134 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b150b24c-4ad2-31b3-b27b-69120b53b12b | -6.05909 | -57.79063 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fb3e1a4-8b29-3eed-b0f6-251367881aa1 | -3.44309 | -59.25626 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d0dac3e-6777-3969-807b-f2a01b368112 | -12.75964 | -52.84576 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13cfbecb-3095-3300-b914-2597edab4d9f | -3.61272 | -60.57393 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98df8cb0-d38d-3712-8927-13735c22fdaf | -3.07766 | -61.17527 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56ba84d3-780d-3521-8234-b9a0908c82ba | -3.79 | -59.72442 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c65029-cb23-3ee0-8a40-eb3b161a1030 | -6.10563 | -57.65837 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d79c96c8-1200-3fd4-9e5b-ae5aab2e9009 | -8.75424 | -62.42717 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d81acbd-3f86-3d69-9766-fa58b13b8f3b | -5.64463 | -60.23618 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4af6c03c-674f-369c-99e7-085ef071e739 | -3.42124 | -58.32269 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fc6f5da-e156-3e82-af13-433f079a8e0e | -5.15692 | -55.96095 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0043b527-6cc6-31ef-a508-16176e6551c3 | -3.76694 | -61.75427 | 2026-09-07 05:23:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ec1f81b9-74d6-3d49-8ee9-3bbc2138cbc2 | -8.70917 | -62.43613 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76202c47-7fb9-3bf0-909b-9343021594bd | -8.76549 | -62.42502 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f24380d-0f5d-3971-ad4f-1f268ef51a2b | -8.7613 | -62.42841 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54cd421e-7617-380b-ac38-1a02aa006880 | -12.75548 | -52.83981 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdbfdf86-bf4f-3eb7-9fa4-0bfb473e1bd1 | -5.35518 | -56.01887 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a94a6ae-bacd-37a7-948c-2daf9d16bb5f | -5.14058 | -55.95622 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b237ebc-82f4-3769-8647-3e2b3caab2a7 | -8.88919 | -62.33474 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 741c7b26-ba7c-3e7b-ad04-b5f84175ab21 | -3.67345 | -48.91744 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37e4853-534f-3599-9cae-36e7fdd49954 | -3.76247 | -59.42465 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4898dab5-0b6e-3332-9669-b207e3172002 | -4.67607 | -55.62962 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 727998b9-d5ff-3082-bd78-ee5d67af673d | -6.12202 | -57.75296 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b34730a-1aed-3c7b-8eb2-09a3aa57ca94 | -3.08179 | -59.13483 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55f219f-bfa7-3912-b2fd-b6fb7e8f98f9 | -3.78864 | -55.8799 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c40dab2-b429-3ad1-aa74-7c46c45e618f | -4.66762 | -55.63671 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fdf7d18-3a32-306e-a5be-4ba6a61516bf | -5.3621 | -56.04473 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f7218c9-5172-3dd8-b751-df6fa6e5181d | -6.12932 | -57.7504 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23889c41-a2f9-37c8-882c-c1831b97720e | -4.6553 | -56.02913 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ef1e0d-5086-37a3-a8fd-d43bd6009301 | -5.46304 | -59.71262 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d16aea2-05ee-3537-8efc-47cdf2dd6012 | -8.52582 | -63.88803 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56f99fe9-6c93-39b6-8e64-513ad835a6a8 | -8.75004 | -62.43061 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bef6844-cfc1-3056-81bd-408d6f5c5fd2 | -5.26621 | -60.15458 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41c9e64c-f0bf-3bd1-b4b4-6a3630503782 | -5.35204 | -56.03908 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41860982-89c1-3939-95db-bbeca44ab0ba | -5.99455 | -57.69633 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 827241f3-1a7a-3151-b8d0-2a32c85a8582 | -5.30401 | -56.01939 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3b73a65-38c3-311a-b685-20ce78ef3057 | -8.53586 | -63.8751 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94b9b531-b452-38eb-a2e1-9983330486c1 | -4.42958 | -55.09317 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f85d605d-f777-359a-aa74-0f22d848413d | -4.09601 | -60.66426 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5318fdc-256e-3c63-926b-97bde140b0ae | -5.59755 | -60.25056 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d936b0b-4b5b-3352-9a5e-c5cefbc785e6 | -3.78108 | -59.71576 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80c41794-22fc-341e-bbb0-65abba55a9bf | -5.36525 | -56.02452 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1929250b-b52d-310a-94a5-f7657920f5db | -3.3687 | -59.50985 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a505f446-98a1-381e-8f1b-683bac6ee9f8 | -4.47412 | -55.08893 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edce1f18-d6cf-3938-b4f1-755d97141ca2 | -4.29209 | -59.96397 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f4556cb-471b-339e-93ba-cd7ae61f9830 | -4.97879 | -65.33486 | 2026-09-07 05:23:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0997cac-eec1-3591-bfe0-1379374ca056 | -8.53204 | -63.87443 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c82ecabb-6eec-3e17-a7cb-00ac61537afc | -5.26651 | -60.11795 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc95f78c-6144-3dfc-8894-d027e7544a3b | -3.78572 | -55.87542 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7944a34c-1dbc-33dd-ac0f-6118cc26f2f9 | -5.29314 | -60.13698 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d81c1616-07ed-3a78-99b5-f6f82b1320bf | -8.72551 | -62.44713 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5996ba8d-a873-3ae1-845c-d9e791c6aa7e | -5.68155 | -60.24208 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 717da28a-75eb-3733-b9c3-b0e0389e5971 | -8.76417 | -62.43301 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeaf2f90-c928-3c40-a212-1a555a664c27 | -5.13357 | -60.30182 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0bd470f-6ee4-3593-9c15-b2f26bd8b678 | -3.78569 | -58.85282 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46739e96-2569-309a-9b35-8020b47a0c04 | -3.82766 | -60.76564 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab1b2e89-8a7c-38a4-af7d-e34a61abe67b | -5.97714 | -57.68712 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a0ce877-9af3-3168-ba16-54253be42027 | -3.62662 | -54.6096 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91a53f87-f92f-322f-b0ba-52d891cc9613 | -5.83207 | -60.25164 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5bc5ed1-6761-33f0-b12a-1a004056e447 | -3.41759 | -59.2451 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4df72bb5-456a-3d4f-acf7-b287a82ea4a1 | -3.079 | -61.53378 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README34.md)
