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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0ac0da2-2460-3cb0-9d5e-727f827daf75 | -12.3943 | -58.0506 | 2026-01-10 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 9378b58e-5d2c-3638-924b-a75cc1d17254 | -12.3946 | -58.0307 | 2026-01-10 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 1ff57e1a-2256-3fe2-a48c-75dbe48a177e | -12.4133 | -58.049 | 2026-01-10 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 117af52f-95ab-3511-b04d-298948c6f37e | -12.4135 | -58.0292 | 2026-01-10 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a0c3ee3a-288b-3563-bef0-71d9ccc698cb | -7.4943 | -45.576 | 2026-01-10 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 31abec45-3e80-38ff-8011-8e79f032fdfe | -19.42043 | -43.48734 | 2026-01-10 00:07:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9c99baad-fa4c-38c8-b9c2-75524ee5e88e | -20.26382 | -46.42197 | 2026-01-10 00:07:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6e01d052-f9f7-3b59-9b9f-89dbbebe15d8 | -11.27935 | -44.6459 | 2026-01-10 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b48188f0-90c6-369c-ad25-9ba3971f7ee2 | -8.18578 | -43.5742 | 2026-01-10 00:09:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 89384473-9743-30e5-afa5-568d73cabaeb | -14.97202 | -43.43193 | 2026-01-10 00:09:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b2f925c7-b113-30db-b911-cc3aba5f0f76 | -15.77185 | -42.195 | 2026-01-10 00:09:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b30b4a9-cdb2-3421-a565-0b242fd02ea3 | -11.83032 | -46.60786 | 2026-01-10 00:09:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5d587219-e9cd-3491-adee-116d5d44da97 | -14.2744 | -47.84235 | 2026-01-10 00:09:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c5c99e10-86e9-327a-b639-cb144275cbba | -13.78255 | -43.24063 | 2026-01-10 00:09:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ac7e9c16-74cc-34ef-a6b2-8281ff7c480c | -10.85988 | -44.28347 | 2026-01-10 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b73cdc1-4feb-3832-8887-64fc0e1e0079 | -13.2507 | -44.11072 | 2026-01-10 00:09:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c64b23c4-6b86-3395-990b-e19b41a84dc7 | -12.79831 | -46.41698 | 2026-01-10 00:09:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d0247c0-1ab8-30cd-99b9-40a90d44fbbf | -11.83161 | -46.6177 | 2026-01-10 00:09:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6fe4ede4-ed34-3501-99e9-f1a188f8c040 | -9.04608 | -46.98555 | 2026-01-10 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6025798c-c23e-387a-a5c5-04542406393e | -10.48974 | -44.93373 | 2026-01-10 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d673e014-6bd8-3291-bee3-d986bc2d13cb | -11.13761 | -46.58456 | 2026-01-10 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 682e4a30-f905-37f2-b2e2-5b8f18aa1158 | -9.03336 | -40.58136 | 2026-01-10 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| bceff5d3-ee23-3662-a8b9-e340935c8009 | -16.469 | -43.52521 | 2026-01-10 00:09:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e84b74e0-c010-3e1f-b9f8-a928bf71ec1d | -9.03696 | -46.98682 | 2026-01-10 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bda430f6-4fd8-37d4-b6d3-31ac6d503da8 | -14.97957 | -43.4214 | 2026-01-10 00:09:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7c216f32-2441-3d62-8f8f-d17e7d382fa9 | -14.97072 | -43.42272 | 2026-01-10 00:09:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 21.8 |
| e7885e32-6872-3077-bab5-3266d3283552 | -8.69264 | -40.76429 | 2026-01-10 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.9 |
| ccecbe4a-fee3-3239-9e4f-d08ad235a488 | -13.79149 | -43.23925 | 2026-01-10 00:09:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| cd1cf3d3-f185-376f-8ab7-773587a6197b | -12.3946 | -58.0307 | 2026-01-10 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| d5071e49-c390-3fd2-856b-7afadc82bf8f | -7.4943 | -45.576 | 2026-01-10 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 6ce875c0-2459-3512-afe8-c7972f6fffe1 | -12.4133 | -58.049 | 2026-01-10 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9825ebaf-29f3-322e-baf2-c1fc9e091749 | -12.3943 | -58.0506 | 2026-01-10 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 94896dc1-e67a-3849-bfcb-0d8f70ac5d71 | -12.4135 | -58.0292 | 2026-01-10 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 61347bf8-0dd8-3b22-a789-70e83a5af02c | -1.70365 | -45.80792 | 2026-01-10 00:11:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| dcace687-2a66-3654-b759-149e9b7cf5b2 | -7.59836 | -45.89272 | 2026-01-10 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9f601db6-fc28-39a1-a4e1-1775880a742a | -1.54536 | -47.20216 | 2026-01-10 00:11:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 70d9a887-a807-345a-b4ea-dabadd2ac50f | -3.44654 | -50.13311 | 2026-01-10 00:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| da2e6647-789b-3ecc-8351-65786ac0fc0b | -2.19103 | -46.38785 | 2026-01-10 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c8e0fd5-55f2-35d9-bb26-a6ca7edc9518 | -5.4714 | -39.64398 | 2026-01-10 00:11:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 45fc5c6c-4176-32e3-97e9-97781a9a7886 | -4.27632 | -43.75891 | 2026-01-10 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 68c8c17f-a5ad-3a8c-af9f-69fd08a6608a | -2.43657 | -46.89425 | 2026-01-10 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 29059e4a-d9e6-3394-a8e4-34367e866392 | -2.90532 | -49.38102 | 2026-01-10 00:11:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c04b8119-9ea4-352f-9c79-8bec09aaafd1 | -2.8848 | -45.68103 | 2026-01-10 00:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bab21dcb-f804-32d9-b0c3-482ef88f49e0 | -7.48769 | -45.5635 | 2026-01-10 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 507e46d5-48b4-3d09-bd9d-1a1264e605bf | -7.48891 | -45.57232 | 2026-01-10 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 469d340d-e77b-3c90-8fb7-2abe7e081ed5 | -3.94339 | -43.20723 | 2026-01-10 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 204cec54-bdc5-3a26-a842-35d67868520e | -2.17088 | -47.92019 | 2026-01-10 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb3ff532-b3ec-308f-b49e-a12edb12bd2e | -2.35681 | -45.59301 | 2026-01-10 00:11:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0dbed716-a069-34c0-a6a4-2b8ee38ed976 | -5.91855 | -42.27442 | 2026-01-10 00:11:00 | TERRA_M-M | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a5c74772-79b5-3bfb-9976-e7c2060a1084 | -2.35554 | -45.58393 | 2026-01-10 00:11:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0b58bacf-8872-3d28-9c84-65f8c72ebf83 | -7.49135 | -45.58996 | 2026-01-10 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 8d847361-29de-3513-9708-b48e3a0079d8 | -2.19225 | -46.39663 | 2026-01-10 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 838b7a69-f7b6-3d30-90e8-3cec65a5d44c | -1.10786 | -46.62182 | 2026-01-10 00:11:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7771c269-6bf5-3fec-8bfc-bcc11cac129f | -5.47455 | -39.66459 | 2026-01-10 00:11:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 59.1 |
| c30860da-1c07-3920-b93a-b36eebbd3f9c | -1.70489 | -45.81693 | 2026-01-10 00:11:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| fe910caf-ddbb-32e3-b4cf-1b49db7c37da | -4.27779 | -43.76936 | 2026-01-10 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 107cf367-fbf7-35b3-9d4c-2da786481a3d | -4.57024 | -43.81497 | 2026-01-10 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff416e29-cf36-357f-9163-29990544ef83 | -2.36449 | -45.58266 | 2026-01-10 00:11:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 6dc3d56f-b97d-3d06-9be3-b132a934dd46 | -1.13867 | -47.12292 | 2026-01-10 00:11:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 95ea53bd-77e2-37bc-968a-d1770ad55e37 | -4.26087 | -48.83545 | 2026-01-10 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 41ef7c48-85dc-326b-a141-d107897187c7 | -6.26881 | -43.27459 | 2026-01-10 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e88fdbb4-14c5-36d8-a739-4d30c6b1a2c2 | -2.36576 | -45.59174 | 2026-01-10 00:11:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 031da815-3253-3053-9bd0-2a79b8888da4 | -1.10664 | -46.61305 | 2026-01-10 00:11:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a340afd4-1624-3787-b0e7-1ff9e6e6e29d | -5.89134 | -39.29738 | 2026-01-10 00:11:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 19.5 |
| aba64186-85f5-3625-adfd-b1cfedd9904c | -4.24107 | -43.78531 | 2026-01-10 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62b092c6-b7ae-3dce-865c-e7ab193db011 | -2.52454 | -45.53873 | 2026-01-10 00:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fc35fe0e-d726-3768-98a8-91b1a9bceb32 | -2.66258 | -45.60529 | 2026-01-10 00:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b476410-1ba6-37e9-a9cc-6b2202b5e493 | -7.05826 | -45.06182 | 2026-01-10 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68488bb4-c6b4-3cbc-9532-826ce9c1dcba | -3.97409 | -42.49805 | 2026-01-10 00:11:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6a5ca54d-d686-3a4b-a002-f84e81805504 | -7.49648 | -45.56225 | 2026-01-10 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 511fe575-5c31-3208-ae67-4c021625d81f | -2.52326 | -45.52963 | 2026-01-10 00:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 421cc16f-9389-37bd-9672-4e5364e9a083 | -1.54415 | -47.1934 | 2026-01-10 00:11:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d85ff54d-40f4-3ab4-bea5-ac8ca1645d7e | -1.55586 | -47.19436 | 2026-01-10 00:11:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 867a80bb-f1b1-3173-999c-8036c5a39023 | -4.57974 | -43.81359 | 2026-01-10 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ccc41e69-3ebf-3055-863b-e35b99e65343 | -2.88672 | -45.22936 | 2026-01-10 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7f42992c-7e2f-322c-a287-0f612b5157c1 | -2.78566 | -43.3489 | 2026-01-10 00:11:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e6dede5f-36ff-3ba3-9d24-777676fa128e | -1.71257 | -45.80666 | 2026-01-10 00:11:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 421da314-9a74-318a-b4a7-423e544befc8 | -6.02238 | -43.85764 | 2026-01-10 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4671d024-fece-3e42-8954-527ab1b2200c | -3.75813 | -43.49243 | 2026-01-10 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 178e2781-917a-3d57-b651-9760c6e0b68a | -3.25734 | -41.84062 | 2026-01-10 00:11:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| ed1398bb-7f6d-38d8-b1f5-7c0f0bda9bd4 | -6.25921 | -43.27596 | 2026-01-10 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e8f4006f-e579-3fe8-abf8-5773c5692069 | -7.49013 | -45.58114 | 2026-01-10 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 99fc5a27-2f5e-3189-bb8f-8a942a76a7fc | -4.26619 | -48.83941 | 2026-01-10 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c7d5a19-41a7-3940-aee2-10ecbd7bc86e | -1.32295 | -53.18027 | 2026-01-10 00:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 697bb24c-3afd-36f5-acef-0a5a0659b4f3 | -2.8962 | -49.367802 | 2026-01-10 00:19:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b397ef13-3c7e-3870-b77b-5854bef99b21 | -2.6263 | -51.939301 | 2026-01-10 00:19:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed5bbd0-28a4-356f-a494-32b89a22562b | -2.3505 | -45.5802 | 2026-01-10 00:19:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb4ff826-b31f-307b-91c8-697630a0e25b | -5.4577 | -39.609501 | 2026-01-10 00:19:00 | METOP-B | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 058fee6c-6399-32e8-bcb5-9bc1ae3b6d41 | -9.0339 | -46.9725 | 2026-01-10 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4005b8c-c944-35d8-aa03-41816a29270b | -20.931499 | -48.768501 | 2026-01-10 00:19:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87bd0b0d-3845-3793-ab1a-9dc4a16cf4c1 | -12.3914 | -57.983601 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad2ddea3-ffca-3fe4-9247-214143b0ae59 | -7.4812 | -45.5574 | 2026-01-10 00:19:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0eca837e-e6ab-3ea2-8a01-5be037869a2f | -1.3259 | -53.159901 | 2026-01-10 00:19:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b086d97b-a78d-3077-b2ed-9c00e54789d9 | -1.0986 | -46.606602 | 2026-01-10 00:19:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42275980-c145-3efa-94ce-5ae41ed6cd05 | -11.8278 | -46.603401 | 2026-01-10 00:19:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2acfe832-21f0-3470-9b8a-2fc5aee9b2b8 | -16.099001 | -56.723999 | 2026-01-10 00:19:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbcb4c3a-131f-323c-9a36-31338f4e0455 | -12.2884 | -57.3521 | 2026-01-10 00:19:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30500a19-0120-369a-8e03-efbc9586da3a | -1.096 | -46.595299 | 2026-01-10 00:19:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baedf975-75e9-37cb-b574-fd471d274722 | -20.929899 | -48.760899 | 2026-01-10 00:19:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5a944d8-f6b8-3769-8dbe-2417dcaaab28 | -12.3048 | -57.332298 | 2026-01-10 00:19:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
