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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be44eaf3-a084-3f6d-8942-1c8e421a5e57 | -12.35145 | -49.91376 | 2025-08-14 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5221bc8e-0803-35a9-b920-9e5fa8450cdc | -12.59053 | -46.976 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ac5f23d-d63d-39fb-badf-6fe4889501d5 | -15.57338 | -47.32228 | 2025-08-14 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4541b49d-91cc-3c53-aaf4-0e5bc1ec6947 | -9.60615 | -55.14594 | 2025-08-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb524c7b-c107-3c82-89d8-3c0d3aee413d | -9.22114 | -44.53327 | 2025-08-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57b1a611-3f06-3676-8d95-8c1f3d1d778b | -12.30351 | -50.0165 | 2025-08-14 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9259dfaf-22e3-3279-89cb-02007022be53 | -12.29021 | -43.68354 | 2025-08-14 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a38d2d2f-2f97-3f2e-bd0d-31b9c8fd376b | -14.32085 | -48.63691 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37f379d3-e977-382a-9792-1c75d756ec17 | -14.45635 | -48.81656 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50875319-271d-3e2f-9a69-226efc835dfa | -12.31633 | -46.06006 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f64a8fcd-9dff-3a5a-b525-843305584734 | -12.69002 | -44.95475 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7750bf8-55df-3b3c-9e44-afaeb014ccd7 | -13.89499 | -45.56275 | 2025-08-14 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0224a76d-a8f4-3a54-b50e-17b71b5ff33f | -13.07296 | -57.14196 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d4c3325c-5916-3a99-98f7-6c9daafaecf2 | -14.47746 | -46.06409 | 2025-08-14 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be723036-b567-3cb5-9249-7eafcdd7b9fb | -12.5834 | -46.95658 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f451014-97b7-3725-ba7a-53c153d30084 | -14.6131 | -51.33613 | 2025-08-14 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4febd0d-7ed0-3de0-8ae4-7d0fd3417292 | -14.36691 | -53.37322 | 2025-08-14 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04ae4ac1-0968-334c-917a-11862b127b44 | -12.58227 | -46.96368 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0b6943c-3620-3047-84ff-13ff22d166ef | -14.79507 | -42.72207 | 2025-08-14 04:21:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a08c9373-b06a-3b28-8687-582662e85ac9 | -10.00586 | -59.22383 | 2025-08-14 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c07b755-3ffb-3a4b-8f11-d4bdbb31f093 | -10.34708 | -57.59471 | 2025-08-14 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29479084-bcc2-3091-953d-e105234dac8c | -12.31302 | -46.05953 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fa1d66f-dbab-3323-9b37-3c30b15ed779 | -9.21291 | -59.65305 | 2025-08-14 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f7c8702-48c7-3302-ac37-5f65664737b1 | -13.07783 | -49.32643 | 2025-08-14 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57756666-0ee6-370c-9510-419f4cb091bb | -14.79505 | -42.72456 | 2025-08-14 04:21:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6863052-26af-3382-abb0-f2369ce70967 | -12.50215 | -46.97624 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2bf6311-8b3b-347b-82b1-3112c70083d0 | -15.58331 | -47.32396 | 2025-08-14 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 293fd8ef-5fd9-332f-939d-acae85e78388 | -7.23441 | -57.63943 | 2025-08-14 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f859691-a270-35ea-bafd-8a201189fa13 | -12.31909 | -46.0641 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e3611d5-da3f-345f-b7ef-9040bc172e49 | -7.28466 | -55.30715 | 2025-08-14 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dc5f3f3-a8eb-3e8c-b146-24f5339b616a | -12.5856 | -46.9642 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b82df08a-3d9e-3d88-a100-ce78998346fc | -12.58064 | -46.95251 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79a4d383-1d4e-34c4-9883-a4fcba1d5222 | -11.36127 | -41.3976 | 2025-08-14 04:21:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8aa22ed-0c6b-3f47-8aad-02d4b2fe0133 | -15.43274 | -47.22155 | 2025-08-14 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2260044-6072-3aae-b9e0-a7c047b75bf6 | -13.8911 | -45.56584 | 2025-08-14 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b19a8734-6d6c-379e-901a-9c9fc45a1fba | -12.57838 | -46.96671 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c811d096-6754-3d00-9078-e030bbf19bcb | -12.31357 | -46.05602 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7835b52-a774-3933-8222-d71849bf24dd | -15.42582 | -39.47906 | 2025-08-14 04:21:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 47c5bdfd-2088-34b4-9faf-0edb5395c208 | -8.79771 | -52.0397 | 2025-08-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 695ab921-7fb9-3a54-af60-eb7bb07ec007 | -10.36219 | -50.80614 | 2025-08-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d852b74-d3a5-33a7-a5e1-af99213f215a | -9.60778 | -55.14647 | 2025-08-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1359f0a4-f75e-3d49-bc53-049e3162b898 | -12.57505 | -46.9662 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52bd2430-60ec-3d37-a34b-e8c41201da2d | -11.69074 | -51.61652 | 2025-08-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d135403c-fbca-34e1-999a-0f572f694d02 | -12.32294 | -46.06112 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c59b8f94-6791-37a1-91b8-75a0db1b5ac1 | -19.78123 | -46.04458 | 2025-08-14 04:23:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6699e9a6-4c97-382d-8241-75d6ad9e62a6 | -16.31017 | -52.91626 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cf5de36-35be-326a-b2d1-a56f377f93e2 | -20.03295 | -49.4058 | 2025-08-14 04:23:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b5ccd228-f895-3513-8de5-91cf580345d0 | -18.61592 | -44.26566 | 2025-08-14 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2886465b-f6ac-38df-a069-5752819623ed | -19.08122 | -48.15336 | 2025-08-14 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f1fdea8-418e-30fe-8d3f-991ec0e83433 | -16.31845 | -52.92586 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 982fb062-31bb-3b58-8836-b95528b3c99c | -21.6343 | -49.84155 | 2025-08-14 04:23:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7f5306cd-c39b-3d0b-9daa-5a44996f0203 | -18.54336 | -46.05724 | 2025-08-14 04:23:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 27a93c7c-9d83-332e-b31b-9e7639784ce7 | -17.04856 | -51.78787 | 2025-08-14 04:23:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 271bbaac-e170-36fd-b65c-421cd39a1ed3 | -16.31014 | -52.92429 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4443b52b-1233-3de9-b369-fd2970d3f4d1 | -16.77105 | -49.31618 | 2025-08-14 04:23:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5324fbb0-4b6e-3d6e-ba48-214ced8a4512 | -20.34915 | -45.98716 | 2025-08-14 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93419423-044d-3c3f-8a75-b628ed548583 | -18.62016 | -44.26182 | 2025-08-14 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d937eed0-ea0a-30e4-937b-b79bee271b39 | -16.72684 | -49.13808 | 2025-08-14 04:23:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da689adf-79a0-3cf5-9278-6d87d157d0ee | -16.32342 | -52.92234 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3e78362-712b-35f4-9f39-77fbbbc68297 | -19.08453 | -48.15395 | 2025-08-14 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ffb8423-807d-31ac-a29d-c6eb5f4889dc | -16.34956 | -48.9312 | 2025-08-14 04:23:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d2b7c38-743e-3715-be62-5bd99cbdf65e | -18.54054 | -46.05288 | 2025-08-14 04:23:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93cf4ee2-0be2-343b-8d36-2899fd7caaf2 | -16.31356 | -52.92123 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8eac33fb-62b6-364d-88ca-2e4eb766421b | -20.46403 | -47.41279 | 2025-08-14 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c65d294-c0b3-3b32-9577-c1ecf8184440 | -16.6712 | -49.34632 | 2025-08-14 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d709a62c-e458-3fd1-b610-ad007c327e00 | -17.65758 | -46.68368 | 2025-08-14 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59f5f65e-9eed-3e4c-acc3-3dfaeb5c1e27 | -16.66778 | -49.34563 | 2025-08-14 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 355a50ae-98f4-3a2b-a62b-4a0173b49813 | -20.7357 | -46.59958 | 2025-08-14 04:23:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1854e8ea-c2cc-36c1-a325-edd1b859c61a | -17.7586 | -46.82335 | 2025-08-14 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aa83834-918f-3e13-948d-292e2b3553ff | -16.30788 | -52.92891 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c77cfc7-2c7e-3455-a0f1-25092f5d3fdb | -20.62068 | -55.48262 | 2025-08-14 04:23:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e454ecba-bf2d-3148-aea5-df3260a1d285 | -19.64436 | -46.09576 | 2025-08-14 04:23:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3bd3a833-38f1-31fa-97c9-b80da8e67523 | -18.3807 | -44.48338 | 2025-08-14 04:23:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b73f8391-7569-3a2a-a44d-c9c103e7a519 | -17.86888 | -52.19373 | 2025-08-14 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3535336b-d87e-3d05-9c08-412d8bdbcf20 | -17.86796 | -52.19895 | 2025-08-14 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 80fe8bee-01c1-3f28-82f3-2777731469e0 | -17.05151 | -51.79357 | 2025-08-14 04:23:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1aa471ea-9d45-3e19-ae97-b8ed669f1dcc | -17.63918 | -44.4986 | 2025-08-14 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71114118-ced3-3d7a-a060-2d6b672488cb | -16.41392 | -48.8837 | 2025-08-14 04:23:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 196d47be-37b5-38c2-be76-00903a9a5be9 | -20.62081 | -55.48634 | 2025-08-14 04:23:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73f1a66d-a2bc-3383-ad60-62589f281d84 | -19.03609 | -46.59032 | 2025-08-14 04:23:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e045bb0-b3b1-3a68-a981-d3940e3af487 | -20.4818 | -54.74969 | 2025-08-14 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 925ccb5c-0ae4-33ad-974c-411124ecc43b | -17.63861 | -44.50259 | 2025-08-14 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b163abbf-9476-3706-ba31-1f5a4e298626 | -16.31927 | -52.92152 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad1bea38-2601-3bf8-8983-c055140b63e0 | -21.19693 | -46.68165 | 2025-08-14 04:23:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d3af7c94-96f4-3ab8-8314-66ffb0637c1d | -21.34901 | -45.84099 | 2025-08-14 04:23:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 63d2f920-f9c8-3bc9-8345-0139abb1d78b | -19.56002 | -46.12202 | 2025-08-14 04:23:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab1617d-958f-3649-b1a0-367470d940bc | -16.38972 | -50.90736 | 2025-08-14 04:23:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bead6050-15c5-37e2-8930-4cb690dd565b | -20.85051 | -45.53457 | 2025-08-14 04:23:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a830de5-f12f-3d27-bab6-cd714fca95cc | -19.45501 | -46.12159 | 2025-08-14 04:23:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d02ead0-365f-32c1-a5f2-27782e6349ea | -18.41103 | -51.98956 | 2025-08-14 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4698b748-4cad-3da1-82e5-31d02313ab2c | -16.30863 | -52.92474 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1cacaf1-8579-3134-9f70-1f1d713fd86f | -16.306 | -52.91552 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5ef2020-d4f0-3e5a-b1b7-45c3b445b4d6 | -19.56342 | -46.1226 | 2025-08-14 04:23:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e23ce3c2-03eb-3b85-8da3-5817bd6106bd | -19.59106 | -48.45599 | 2025-08-14 04:23:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c49a8130-7e2b-30b5-aae3-96f4d5b7162d | -18.53998 | -46.05669 | 2025-08-14 04:23:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66788a1a-949c-3323-af48-8dd43fc34c2e | -21.83214 | -46.49841 | 2025-08-14 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dacf1226-4307-3b62-896d-b76f39ffeaf5 | -16.31773 | -52.92198 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 344eed55-9698-3e7f-89d6-7ad8807482ed | -17.61377 | -46.70257 | 2025-08-14 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 597acb3c-5a84-3842-8274-de56e3479238 | -18.24481 | -47.262 | 2025-08-14 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67d63887-fa5c-3dda-8605-3d3d543fd3dd | -22.60409 | -46.72425 | 2025-08-14 04:23:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README16.md)
