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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8354f855-9919-3671-92f1-b1dd5287bac3 | -12.9268 | -62.473701 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0fbbd43-d6bb-3607-bc9a-a223f5c7c4a4 | -12.9312 | -62.490299 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4720ef2f-f16f-300b-ba3d-5823ffd28e94 | -12.9086 | -62.443001 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2814f972-989f-39dd-a560-d9b25b00b5a3 | -12.9119 | -62.495499 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5be8add6-68c7-312e-97af-d2095a081cd4 | -12.8991 | -62.725201 | 2024-10-09 02:20:25 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12088607-a1c7-3131-8248-77117d152fcb | -12.8853 | -62.7118 | 2024-10-09 02:20:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3002dd6e-b97f-3051-89fd-6230449d162c | -12.8894 | -62.727798 | 2024-10-09 02:20:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff254f6f-85c4-3b8e-a34f-e6b0e5eca7e5 | -12.8535 | -62.788601 | 2024-10-09 02:20:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6a3eaac-aaef-3e2e-bdd7-b9063e63565c | -12.8576 | -62.804401 | 2024-10-09 02:20:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a73ec9f7-ab34-3d67-807d-867666d568ef | -12.8438 | -62.791199 | 2024-10-09 02:20:27 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8e3bebb-ff3c-3ea3-a1d8-b1de9a8530ab | -12.8479 | -62.806999 | 2024-10-09 02:20:27 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b66c0d89-9adf-3abd-9741-05127ea75d28 | -12.8342 | -62.793701 | 2024-10-09 02:20:27 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bee33562-e9c4-3b6b-addb-e64d0560f34b | -12.8383 | -62.809601 | 2024-10-09 02:20:27 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc805ed7-e5ac-3ae0-ba79-cc2cc30958e7 | -12.6611 | -62.924301 | 2024-10-09 02:20:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebef31f-a16a-325a-b6d1-e2869683ffb0 | -12.6651 | -62.939899 | 2024-10-09 02:20:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03d63c2d-6e4c-36c8-82fc-f64aba834704 | -12.6691 | -62.955502 | 2024-10-09 02:20:30 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a88e292d-bd56-32fe-8e39-51d7f9d4ee9a | -12.6486 | -63.076302 | 2024-10-09 02:20:31 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bfd6b4cd-aa7b-3682-9b74-5e62e345a7fc | -12.6525 | -63.091599 | 2024-10-09 02:20:31 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4704fb9f-7f0a-3b99-9d5f-1a1052a5eaf0 | -12.6389 | -63.078899 | 2024-10-09 02:20:31 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3f80086-9027-35aa-aed2-5bf5042a0887 | -12.6428 | -63.0942 | 2024-10-09 02:20:31 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8dcabb56-e8ba-3e27-b4df-e95e0c7f471b | -12.6292 | -63.081501 | 2024-10-09 02:20:31 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 26b9edcf-e7f2-3bb9-b306-4efc48771e0b | -11.8702 | -63.266102 | 2024-10-09 02:20:44 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1df18e3-58af-380b-9b5c-dc4b6094ac45 | -11.8741 | -63.281399 | 2024-10-09 02:20:44 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12b1d671-20a9-3f24-8498-b89caeba35e5 | -11.6845 | -64.038902 | 2024-10-09 02:20:50 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b560eda2-2e1a-3726-804f-4182c743fec9 | -11.6644 | -64.000298 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 212899e1-51a1-3510-a92b-938beb41957f | -11.6679 | -64.014 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6bbea2d-b418-37e6-a046-01dc2482ca43 | -11.6547 | -64.0028 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6d8bf73-52d7-3c7e-999e-6f6c4d0293ff | -11.6582 | -64.016502 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 28d60bfe-23e1-3453-a469-6a4b951b4405 | -11.6616 | -64.030296 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b0ccaed-23c0-322b-a829-b5b6683eb33f | -11.645 | -64.005302 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f592bf40-f374-328d-a277-c45a0c224b53 | -11.6485 | -64.019096 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 038c1790-138c-378f-8354-3da69bed6955 | -11.6519 | -64.032799 | 2024-10-09 02:20:51 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82a280c1-02ab-3f8a-b6a7-e52a3ab0bbb8 | -11.675 | -64.989601 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3bdb44dd-84a2-3894-b9a1-09c58f094756 | -11.6788 | -64.963303 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac57fa73-2121-3963-9960-4995644224a7 | -11.6847 | -64.987099 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a84dbd7f-4f5e-3716-bc64-8c0df6c4bf67 | -11.6877 | -64.999001 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5b791f-9731-3197-af3b-97fd2d8bcfb4 | -11.6906 | -65.010803 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 038d111d-6e06-3573-a35b-6f09b8c0c375 | -11.6779 | -65.001503 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1afd2934-f02a-3a30-a5d1-0b2f49f8326a | -11.6809 | -65.013298 | 2024-10-09 02:20:54 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d354a65-09e0-32f0-bbd5-97caf20d95fe | -11.4942 | -65.135803 | 2024-10-09 02:20:58 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36f5a5c7-6ef3-32ab-b8f6-bdfec5602eeb | -11.4971 | -65.147499 | 2024-10-09 02:20:58 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee0ac86-a40c-3f97-8570-7f5327892b15 | -11.5036 | -65.256599 | 2024-10-09 02:20:58 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46aae9a9-a0d8-3536-a2ed-87234dff9328 | -10.3676 | -61.216999 | 2024-10-09 02:21:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 177da890-9b21-36d6-8b71-b76bc78100ef | -10.3734 | -61.239201 | 2024-10-09 02:21:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5e3f725-b875-3da3-b2cd-a26e433ae4dd | -10.358 | -61.219601 | 2024-10-09 02:21:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8640a0e1-645f-3aa9-88f5-0dea14b93df4 | -10.3638 | -61.241798 | 2024-10-09 02:21:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d92a6d26-56e3-3135-bc2d-87ead5d26019 | -10.9033 | -63.8512 | 2024-10-09 02:21:02 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1de0684-25a9-3f66-84f1-5439177f4acb | -10.8658 | -63.907101 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab231795-dac2-3c6e-97bf-f21816d2eb19 | -10.8524 | -63.895199 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 678e778f-c13d-3126-8cf3-6a4fba356034 | -10.8561 | -63.909599 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7bab334-097a-3790-8fdd-f5e5bb0be2d4 | -10.8597 | -63.924 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9127a017-8807-3b8b-8c33-ebb0f57b2db3 | -10.8391 | -63.883301 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97c4c9bd-e099-36b2-aba2-1aa3f0c96b30 | -10.8427 | -63.897701 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a6d063d2-899f-341b-95c5-eb068ff439e6 | -10.8464 | -63.912102 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e505a647-deed-3579-b639-0737623d2c7e | -10.85 | -63.926498 | 2024-10-09 02:21:03 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da4c540d-9a8b-3e94-84c5-4cb349fb09b2 | -10.833 | -63.9002 | 2024-10-09 02:21:04 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc31b9a9-0d67-3026-aad4-293f433911c9 | -10.8367 | -63.9146 | 2024-10-09 02:21:04 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc5e0b1-e0df-352f-8166-70aa42fa7ee8 | -10.884 | -64.142899 | 2024-10-09 02:21:04 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27835329-f4e1-39c2-94b2-628104c586e9 | -10.8874 | -64.1567 | 2024-10-09 02:21:04 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b79df49e-db44-3aa5-861d-d8201ff40ed6 | -10.671 | -63.627602 | 2024-10-09 02:21:05 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 124a1de5-a0ef-311b-9783-fd32ef556700 | -10.6748 | -63.6427 | 2024-10-09 02:21:05 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d19bb74-7915-3851-a981-91243426efc5 | -10.6891 | -64.148399 | 2024-10-09 02:21:07 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4619f2fa-e71e-3e8e-992c-1b3024c50a7c | -10.6233 | -63.969501 | 2024-10-09 02:21:07 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 774d9595-a52b-3174-b2eb-0920902a53a3 | -10.5724 | -64.013 | 2024-10-09 02:21:08 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20a6ff25-1f05-3990-9ef5-93287a97e639 | -10.576 | -64.027298 | 2024-10-09 02:21:08 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d902a2e5-14e9-3c13-802a-d8f7ba0162ed | -10.5626 | -64.015503 | 2024-10-09 02:21:08 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 001a3d42-190f-3b5a-bbad-b62cfba7cd23 | -10.5663 | -64.0298 | 2024-10-09 02:21:08 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20371300-3b61-31f8-8be9-bd2ac4956520 | -10.7783 | -65.166397 | 2024-10-09 02:21:10 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad9b3811-319e-38b6-8cf3-d7044e98b66c | -10.0645 | -62.507 | 2024-10-09 02:21:10 | METOP-C | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5bed8672-4f9d-39b6-b323-12fd3da2f4d0 | -10.1149 | -63.673698 | 2024-10-09 02:21:14 | METOP-C | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4934a6-848d-38ee-863d-784547c81164 | -10.3502 | -64.815903 | 2024-10-09 02:21:15 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e747c9b4-57b4-3673-9be2-4329d04c0648 | -10.3534 | -64.828598 | 2024-10-09 02:21:15 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4be0e57-73d7-376b-8e89-f107ae5df31d | -10.3565 | -64.841301 | 2024-10-09 02:21:15 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3810e211-e05c-36c2-bbff-b96e3bc6a77f | -10.3405 | -64.818298 | 2024-10-09 02:21:15 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e867256-f03e-3c84-b9e6-072a1bfda23b | -10.3437 | -64.8311 | 2024-10-09 02:21:15 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f4f2dddd-fe04-30ec-a08f-d6278b35a178 | -10.3468 | -64.843803 | 2024-10-09 02:21:15 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5a4ee4e-6620-3ea1-b9f8-bf7500d2c3c4 | -10.0751 | -64.830902 | 2024-10-09 02:21:20 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e0eae9e0-7732-3f5f-a8d6-d853c96b5755 | -10.0783 | -64.843803 | 2024-10-09 02:21:20 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5be33b-c805-3200-a0a8-6b12a6785b8f | -10.0653 | -64.833397 | 2024-10-09 02:21:20 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0723e499-0c7d-3965-9d9b-d559278aac73 | -9.9683 | -64.775398 | 2024-10-09 02:21:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 106d4681-19e0-3f75-b6ca-4f2521d9ebf2 | -9.1414 | -61.566399 | 2024-10-09 02:21:21 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 024eb1b3-8222-3d80-84c9-6d832bfd08a4 | -9.1317 | -61.569 | 2024-10-09 02:21:21 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d14b6af3-9885-33c8-af22-77603514fe3f | -9.936 | -66.746902 | 2024-10-09 02:21:29 | METOP-C | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 696dafd3-b9c0-32b2-9b0b-63af6a5f3092 | -9.931 | -66.768898 | 2024-10-09 02:21:30 | METOP-C | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 43914c25-e18d-35f3-b616-35cae14a4b33 | -9.9334 | -66.778603 | 2024-10-09 02:21:30 | METOP-C | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 128442e9-4168-3502-864f-8f28900cf4b8 | -9.0324 | -63.227798 | 2024-10-09 02:21:30 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbec2f3b-48ab-3493-b863-67c03e632c6b | -9.0227 | -63.230301 | 2024-10-09 02:21:30 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 57288843-80e5-3860-857e-b849f6e0c453 | -10.0577 | -68.4645 | 2024-10-09 02:21:34 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7a33e22b-be1f-3363-b7ef-0b30c555094a | -6.7519 | -60.0266 | 2024-10-09 02:21:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 040c802a-a5bb-3dd8-95f8-be10dc1e6a87 | -6.7599 | -60.0574 | 2024-10-09 02:21:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 161dfc6f-b350-38d7-8ede-cca6dba1a704 | -6.7424 | -60.028999 | 2024-10-09 02:21:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0bcb5a-b376-3a31-bc23-97d8b042d8d7 | -6.7503 | -60.059799 | 2024-10-09 02:21:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee552f1d-e125-31de-853c-b1684c6a7f1c | -6.7328 | -60.031502 | 2024-10-09 02:21:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50626422-2069-34ac-ab32-78a75d808dd2 | -6.7407 | -60.062302 | 2024-10-09 02:21:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5b182e8-2a98-370a-9b70-ced6e4dafdbd | -1.11 | -53.6173 | 2024-10-09 02:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 5fcb02cf-388f-3d50-921b-901e41d96ba1 | -3.8008 | -41.5989 | 2024-10-09 02:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 01325262-09a5-3cfe-bea6-f6d00b3844ca | -3.9021 | -46.4689 | 2024-10-09 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| eeae1a36-e215-3bae-bba5-3535c0eb5239 | -3.9023 | -46.4467 | 2024-10-09 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 63b2ff9c-ab24-348e-a01a-dfe001950576 | -3.9208 | -46.4459 | 2024-10-09 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cc166c25-8a35-3aff-b4b9-aebf30c7130b | -3.9393 | -46.4672 | 2024-10-09 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README53.md)
