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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 709b4a95-c5fd-3fdf-aca1-77dc56f4bac3 | -3.05025 | -47.69521 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd34fa49-41c8-3121-8f9e-a9b71e9b9115 | -4.72719 | -50.37529 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ded58d-3ad3-398e-a88a-904638f15515 | -4.13438 | -46.91763 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761e5494-4ddb-3de8-8349-fd695b2f90db | -11.08478 | -43.34235 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c513ca0b-a6a0-3a73-924d-02460ea98933 | -4.60719 | -45.97255 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dcb1b74-d2f1-3ec4-8f32-ae2e945045a0 | -4.20733 | -45.85642 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1fe795db-222c-30cc-95c4-a46601eabf11 | -4.38061 | -48.58489 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19dcf48c-f7b9-3068-88d6-d5ef835848f3 | -3.60397 | -51.12058 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41c87a56-ca93-3ce8-a44d-cb4e996d1bee | -3.26652 | -49.47859 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6b557ea-af97-3a7f-b277-361201dd2050 | -5.54577 | -44.31926 | 2024-11-09 04:33:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ca99f72-23b8-3243-9ba0-831efa24b57e | -3.43694 | -51.11544 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb5b2e08-e5f1-35eb-ab7d-76296884b429 | -3.01193 | -53.43879 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b12d6ff-b97b-3062-ad7a-27646ee0ad3b | -3.67024 | -50.2239 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2fc7d0fe-517d-341f-b45b-f62e4826484f | -3.89609 | -50.08317 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91e5920f-0009-3198-9641-e764780d0149 | -3.04637 | -50.3651 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c33aeec4-ac40-3cd1-b4df-c8bf56f1d24d | -2.73207 | -51.74442 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 302220a5-7f40-3b6c-93ed-af2641fc6d76 | -4.61306 | -49.57857 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f6dfacc5-c682-396f-939c-7af9aaaa542f | -3.81768 | -46.45929 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab1bb7c6-1981-3108-840a-65bea12741f8 | -2.48082 | -54.05319 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c94f1aed-5ed9-3c50-9c0f-3184a37d57b4 | -3.92367 | -50.25018 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e753bb0c-b079-340b-b5f5-6df126dd98be | -4.61284 | -45.98083 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bcf4665-4bbd-3f64-9e44-ede4cab4a6d6 | -3.75411 | -54.64347 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2a15ebf-690a-3f3c-95f3-a2e54270326a | -4.09303 | -48.51085 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7d62d11-781e-3082-a074-64e39e07d55f | -2.95802 | -48.02473 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ec092d2-d165-3679-916b-e3268bc96fa7 | -4.23751 | -46.27522 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 324c28c5-b42b-302e-a41d-ce582a8d65ff | -4.39346 | -50.97505 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cbf82ab-d3f9-3c7e-b303-7dc9e9d02c1b | -2.86357 | -50.32096 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 27e36f2f-3ece-3519-b0b9-72cfa2e390eb | -3.17859 | -50.59816 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ef9927f-052f-3679-a412-9a4f1870ce63 | -3.97153 | -46.41085 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b91c4eb-38a2-30f9-9c26-47b7d394ba98 | -3.38272 | -52.35561 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0963a96b-9a09-3058-9c4a-36b9407d9c19 | -3.52933 | -50.86845 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5bc214fc-6450-3f2d-8149-b5403a1f06db | -3.03557 | -50.36341 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a282e06a-5060-3c32-a6fe-b0bc89ab7b1b | -2.92796 | -49.35356 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1b27124-ba9e-3f11-8cbf-dda7922061ce | -3.04143 | -50.32632 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6d697295-96b3-3909-a9f5-c58c8c647d7f | -3.64324 | -49.96066 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97799956-721e-32ec-b9a2-88220bf72467 | -3.01384 | -51.042 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 924fc4ec-d2ba-3988-a640-d350664f7818 | -3.82839 | -51.90975 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d703cf3d-1886-3b78-9454-f77921b4fe49 | -3.53381 | -50.32775 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8dff19e8-eaab-3d59-994c-64550ebe264c | -2.61894 | -51.30027 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47403526-eb05-3a43-beff-88f2dabf91d6 | -3.07505 | -50.56597 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e55506f4-7301-3239-aff1-6d8141fa1ad1 | -9.41464 | -41.18896 | 2024-11-09 04:33:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75a095d0-9f70-3030-8421-0f2883d752ad | -4.40142 | -41.90931 | 2024-11-09 04:33:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0173605-e403-3aec-86e1-7c732bef0cf0 | -2.87903 | -49.37661 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf28aa52-7507-3831-81f9-46225368a420 | -3.18495 | -46.61389 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c551372-8491-3746-ad2e-cdc36f6625c5 | -2.98653 | -51.45739 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc97f22f-44f6-377f-9ff5-c4e7f506ab1f | -3.96142 | -48.17851 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 92554d58-3f43-3fb6-962a-3fed9d3a5c54 | -3.03003 | -51.01248 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82cb1f69-a348-3357-908e-b98aa1d34018 | -2.84225 | -49.56566 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3aa5e26-f3dd-3e5a-9b2e-6d9ac3583e58 | -4.41582 | -48.77486 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63dcb272-593c-3a4d-88cb-7080457648cb | -2.80501 | -51.49417 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9afd2a18-b72f-3525-a8eb-b31a05159a13 | -2.87509 | -51.30216 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd2eca0f-3d28-3bf7-9c69-e2a0e0016328 | -4.87568 | -45.77795 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4193d5b6-3fb0-37fd-9ec2-3da2d24e691d | -3.74294 | -50.17793 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 99dee7be-3d30-31b8-84b5-ac3cb240ad15 | -11.09051 | -43.33857 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 3f623cfc-7e80-3cb6-8bc1-90ade9842188 | -3.03027 | -53.26022 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2f3bbf7-f147-3f49-be06-255f1b34ff80 | -3.27985 | -49.46132 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 358c2b27-718e-3d66-96f4-a50c62cff508 | -5.26807 | -45.87365 | 2024-11-09 04:33:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddf37c1-e902-3e22-a6af-b00373d54fc8 | -2.88642 | -49.39712 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6965547f-5137-321c-84bf-2e555031753b | -3.21635 | -50.3858 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be6223bf-66d1-368f-bc05-8e468499ca56 | -4.7826 | -49.75 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ef3ee7-5306-3e23-8224-5c06514b9363 | -8.84759 | -47.68414 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5aa7c041-ded7-36e1-8708-2314a2401843 | -3.22167 | -50.30669 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 00d55325-c9bf-3cd7-b7ff-d26c575726dc | -4.24558 | -48.5345 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9194062-e818-3cc1-aa32-4b13ae8ebb0f | -3.12163 | -53.12056 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09b8e73a-b9d8-360c-bc22-871cfb6f0e22 | -3.92471 | -48.32629 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78b0f0bc-7fac-3a41-bdef-62cdc8ec60da | -3.02073 | -48.08078 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bfe2f12-0557-3021-8bc4-bc63157f7733 | -3.09575 | -51.11295 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3156b0b3-6bef-3fc1-8150-31a220fad283 | -3.29377 | -46.41721 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7b3f0d0d-04cd-3b4b-901a-03868e29a94e | -2.85542 | -51.77932 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffb6a84e-d4f6-3500-b93c-2bc9782f0a44 | -2.64885 | -49.8961 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2d7da59-d2b8-34c4-b81a-de1f6865254f | -4.11452 | -46.91454 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cb25824-14ef-3d57-9565-37b167f68d0a | -4.13297 | -46.83939 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b70f0f63-8f2b-3b90-93ad-938dfbd286a3 | -4.75534 | -48.92648 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc4eaefb-2ffe-3707-adbf-7ed838f705b5 | -5.83893 | -39.62651 | 2024-11-09 04:33:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 769e61a0-7f2b-363f-bbcc-94ff9876b87c | -4.76459 | -49.48777 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fa516ab-8bcc-3bcd-836a-0c66cd457066 | -2.47601 | -54.05334 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d47c8ece-2b4c-3aa2-a117-3cac7ff174f4 | -2.67295 | -53.02399 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1411096-a0ef-3495-8883-13446dc770b3 | -6.18658 | -41.88332 | 2024-11-09 04:33:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12ac00e7-e929-37b8-8208-d63ca2179297 | -3.95357 | -48.14176 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adbddc02-ea5e-32c1-a044-6cb3b5c47959 | -3.96897 | -46.47151 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5c2233a-5ef2-346e-91e2-698ec3792501 | -2.93107 | -48.67045 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28e1892e-f307-317a-a162-6a507599f715 | -3.078 | -50.57079 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1612468a-260b-38ce-b738-77c651ce5c30 | -2.89165 | -49.38631 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3413a6-0ae7-3bcf-ba15-26076e0fe419 | -7.45842 | -43.57589 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 282eb87d-a6b8-32ff-b84a-1960dbc814f2 | -3.12718 | -51.10854 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93eac861-39b2-3ebd-802e-61e587bdf056 | -4.16125 | -48.24934 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8fccdf1-a2e2-38d3-a494-bcc3e90e62ae | -3.0349 | -50.32109 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44e01970-bad2-385a-9b02-eebe2ad116b7 | -6.0691 | -44.14905 | 2024-11-09 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 359e53cb-9f5c-3023-8be4-eb06257599a4 | -2.86117 | -49.26617 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10ae6c7b-a044-362e-8090-92c502c9b6e7 | -4.11469 | -48.5034 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 159b85a7-254c-3c00-9e0b-86b20a4ce0ec | -3.34077 | -50.35759 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f61275da-fcf1-37ef-8d0c-211f2c0ff800 | -3.95417 | -48.15964 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8b2d05e-13b5-3053-b33d-95b98cee2bf4 | -4.11113 | -46.89275 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cdbf02d-e4c1-3e55-b8e6-45a314c3a6a4 | -3.30459 | -50.08379 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ad7c65d-0ecd-3735-95d6-bd00aded9446 | -4.08919 | -48.85497 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57bfcfc8-1db5-35c2-875f-742a3bb03894 | -4.36408 | -48.14936 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e94a64b-bdf9-35ca-9939-f123022f4a3a | -4.60138 | -49.4969 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf7197bb-1136-376a-9a5e-446731b44959 | -3.58926 | -50.27829 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1545e725-4afe-3ec9-9cd1-93d1e8c968e7 | -2.86869 | -50.32301 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59ac8e77-d6b1-3242-8885-4e68161dd5d7 | -3.02906 | -48.09275 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README42.md)
