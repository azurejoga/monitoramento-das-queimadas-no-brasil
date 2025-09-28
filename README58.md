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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d964be00-9d15-3a8a-b4f2-c9b53869fc87 | -5.90764 | -42.93113 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 38eac031-31b4-3347-8d55-263ee99e992c | -12.00674 | -47.96154 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 224ed134-23f2-32b5-83b7-1d38a8a1934b | -11.98167 | -48.01184 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd85d270-25da-369a-8a15-af36920c3a03 | -8.71963 | -47.98747 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23d290fb-6aae-3eeb-bd10-9f7025f5bb6b | -11.99053 | -47.89389 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3cf96c7c-94cf-366f-ba26-0dd3eb578bea | -8.62986 | -44.84627 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d90a80c-1f7f-3399-8f4b-9e78222b1de1 | -5.86793 | -45.75597 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6459007a-6885-3a68-8d1a-b575cc29a753 | -12.83188 | -44.68109 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c53bca13-7add-3a8f-9f40-375ea66f3450 | -7.75048 | -47.02061 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b30c0a09-b018-367a-85a7-7246127dc3f3 | -12.43768 | -45.20388 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8186bf08-c43e-336d-aa62-a1372ad346e3 | -12.92541 | -45.17454 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5594285a-d351-356f-9b09-18fe0d058a7b | -6.24632 | -42.47347 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 06df5981-2652-3576-a9bc-39294ffd6cb1 | -9.92268 | -49.81737 | 2025-09-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1362e666-d7c2-3332-abac-f4a327c992d1 | -6.5043 | -54.8712 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d1ed8a5-3d5d-30c2-b399-a2ca02772f05 | -8.26831 | -45.47085 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3d78e4c-6bb6-377d-ba30-be9c887aa499 | -10.45802 | -50.85629 | 2025-09-28 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8a100cf-e158-3a0e-9d2c-0f6e3a89b412 | -11.85533 | -48.24948 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5cf9378-f624-3115-8b20-a0e9f4cd74dd | -7.31897 | -45.98817 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b78571d3-f143-3ebe-b494-30b1736207b3 | -10.90981 | -47.46899 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23a57e1f-59b0-32fa-8644-1efaf640fee2 | -8.62588 | -44.84941 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00383932-11ce-344f-a4db-227b916a31b5 | -9.04392 | -46.72461 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4bcc90d-0822-369d-b79b-e79c28573d4c | -11.9507 | -47.90911 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2054824-a0ea-326d-8ff8-3afef85994cf | -6.4994 | -43.71674 | 2025-09-28 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee49d67c-9a96-3b6b-a212-bc3bf1d188e8 | -7.54553 | -46.10241 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06024fb8-967b-3189-a131-ea3d71f4ec1f | -7.35144 | -42.1076 | 2025-09-28 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 68657c72-dd77-3bff-97e3-99eff4c20ac8 | -5.93474 | -42.90772 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 78d4bc7d-e9da-3042-a6f3-bddfe5e9f029 | -10.29921 | -45.39747 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2a8a7dd-506d-34ba-909b-77311edeba97 | -11.36355 | -44.94763 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2991be56-ded9-32ee-8d64-4afc47f969c0 | -12.92073 | -45.18192 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2645ebc1-d7b8-3350-bee1-71648ee2aed8 | -8.49185 | -44.71914 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7377edee-813e-3416-bb2b-19034bf72998 | -6.61611 | -45.07452 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b9ff152-09a2-320c-af0c-8583bd4dcc02 | -6.61248 | -44.94263 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b097f8-c59b-32d1-94df-a4d664dc3b77 | -8.83321 | -46.20559 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ef2b333-f285-3e32-b971-fbd49f8ab905 | -10.94006 | -44.31606 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 830d40f5-1b8b-377f-a022-0f3f2d84234c | -8.85987 | -46.59938 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 710d70ad-6658-31bb-b51b-b7ade57506e3 | -7.42408 | -40.07942 | 2025-09-28 04:25:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f72b1fbf-5e34-370f-8040-cc992a5fe1e5 | -6.47966 | -44.50755 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdd27369-2666-3390-8e8e-38b667dc6ed3 | -12.89626 | -45.17817 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 395d0b4f-f52a-30c6-a005-2636184c7aa5 | -7.79842 | -46.99607 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5032f8fe-7368-347c-82c5-9c9b3796be01 | -7.10284 | -44.23607 | 2025-09-28 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cac5f5a2-367a-314d-9104-27c1a2b691aa | -10.7947 | -49.58583 | 2025-09-28 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab6c48d9-4502-39c7-b735-2fcf05a192b0 | -6.05884 | -44.75481 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c66a5285-f975-3038-a0eb-be29e7888bba | -8.38674 | -47.99636 | 2025-09-28 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8e84067-ea62-3d25-9e4d-51d9a4b29342 | -6.09096 | -49.39614 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c78abad8-ca9d-3027-a163-60340ead8094 | -10.90746 | -45.74482 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 53ec8fec-4891-387f-82a0-54b8136b6a53 | -9.41214 | -54.70082 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e64d77-2d75-3bd0-a267-3cb3ce98c0c0 | -11.37169 | -45.01284 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 192c65f3-cf91-3769-b22e-473867d2a045 | -8.16944 | -46.41077 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6d26bdcf-6291-33f8-aebe-4ea7b0a5cc53 | -12.00143 | -47.88828 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24025368-8f7f-326f-87ba-3cc07465abc8 | -9.21275 | -46.77293 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7646001b-dd96-31ed-917f-fb4a97bff0a1 | -5.35449 | -45.97585 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b52d8323-84a4-30aa-9385-1da8b682be8c | -7.18121 | -41.70653 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 470bbce0-9612-30fa-9095-30be7a89fae4 | -6.07169 | -43.76908 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41b5d4b2-d874-38dc-80a5-60cbdc31a4a8 | -10.41361 | -46.15115 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98c7c526-7707-3484-a11f-89beaff65d48 | -7.19957 | -43.84533 | 2025-09-28 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdddcc34-a880-3119-ae17-0f2d54c95fee | -8.48462 | -47.80641 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e59989e7-9602-3845-8b2d-2691c0515aec | -11.62451 | -52.85602 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1dadc1f-d963-35f3-89ba-e416f36cd4f2 | -12.00601 | -47.08466 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a9e78d-166a-3fcd-bbdb-430e1060975e | -9.97321 | -43.5754 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6e653ed-a6de-37d4-8e0d-c4a658db9b67 | -12.87861 | -46.79856 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 859052f0-edaa-31dc-b256-67a288ef1819 | -8.16999 | -46.4073 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 33a58ae4-9655-3a4f-b39c-59f7f1f66260 | -7.04473 | -44.76875 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d635dd5-376d-340d-a810-2b6762dd30e8 | -8.16989 | -46.34321 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04c2c7ae-4d2f-3a63-8c4d-426cd7e7a433 | -11.42355 | -46.64071 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75438f61-b4ee-3b95-a3f9-6a1e72919235 | -11.98224 | -48.0083 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 961cc788-33cb-3b31-84ce-5f548c50eddc | -12.95582 | -46.38571 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 883bf51a-aa3d-36ca-b96d-a194b3ec1139 | -11.61193 | -44.41363 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32f90171-efa3-339e-9fba-b8a620b4942f | -8.48903 | -47.82176 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cea185bd-d8de-301c-b907-239c07c09ad2 | -12.03435 | -46.50775 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26025c9e-5f78-31fc-b95a-8bbf5324b8c5 | -12.89978 | -45.15439 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c8a34980-06ee-376e-bbe5-1b61dda56670 | -12.82831 | -44.68055 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a6d9817-3f30-3190-9507-d9552eda73e6 | -11.95054 | -47.97427 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1d1feda-2e96-3a58-894d-dcc2d0113437 | -6.95258 | -45.39771 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a464ec-1cb4-3475-b901-8c493fb38a6c | -6.94005 | -45.67554 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31f8d2e6-6c5d-313e-ac37-c834209965c6 | -6.74572 | -44.71551 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ea9c595-ece2-36c6-8d80-83c37321e1dd | -6.50945 | -54.87204 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8321af9e-b152-300e-89e7-12348101eb53 | -9.73524 | -49.11321 | 2025-09-28 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f892da8-5dc0-30fa-bd96-5bc4e2d56d46 | -11.98558 | -47.88225 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a79ae9fe-254a-38d7-af9a-023ee52f09c0 | -9.06306 | -45.53576 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34b39d72-cdf4-3d49-8d3a-e303cee076d5 | -12.74599 | -45.9509 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e626970d-62d2-34ff-b5bf-ccfba5dc2591 | -11.51409 | -46.95166 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49ed173c-4bb8-3cf9-bf89-92c88aca776f | -11.66909 | -44.46301 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1312e9be-3db5-3a08-9420-4363d657d43f | -11.95626 | -47.89555 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bba5a87-a00b-3847-9072-33f859c763da | -7.20855 | -45.39004 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61f740f5-aa85-39a2-be34-ff758c7181a3 | -6.1119 | -41.81755 | 2025-09-28 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8c4cef31-c08b-31ca-9961-ba38d0a0f040 | -7.75987 | -45.73216 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 963bd8ed-a5b7-37fb-8d23-deae39c0c8e7 | -11.40132 | -44.90901 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d5399fa5-92b8-3602-b051-5ebf3237a763 | -6.40865 | -42.90969 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 08701cc9-f10d-3019-be67-ae967865ea13 | -12.01005 | -47.9621 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca830983-213b-3bd8-a091-d8c0f5928a46 | -9.06697 | -45.53271 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b311c9a-3a38-3b7f-a67c-4bb9f6c8c9a0 | -5.83227 | -45.59429 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b202175d-aca4-3749-89f4-406f0480fb8f | -12.91547 | -45.19324 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3849b20b-8671-3f80-b1c2-384f56b30924 | -12.88404 | -47.09164 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3766e95-dcf9-32e2-b95a-c05597aabb6c | -11.41912 | -45.02793 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b008481-96fc-33af-b356-a9cc04e95088 | -6.09091 | -49.3934 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e68b36d-bed2-3cab-b4c9-3cad04ece1dc | -11.14979 | -54.30533 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36689266-2df8-3e64-89f0-99c16cd4db8a | -6.08385 | -42.63344 | 2025-09-28 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b973321a-35cb-3890-8d85-6fda5ccf9464 | -11.4027 | -46.9699 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52b38637-491f-302e-93bf-4c79cfc0ac58 | -6.25567 | -42.46177 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4f26f85-345f-344e-bb38-6c92a26d573f | -7.60486 | -47.33813 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README59.md)
