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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f296b61e-a7ed-3c7b-a298-8c7e06d36416 | -8.57844 | -54.78942 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d791b029-7f4f-3492-9968-87de603fce10 | -8.59011 | -54.73888 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f689f80-cd33-39d8-a955-60154774b7c3 | -6.44007 | -60.07989 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d609f815-0c04-3543-a55f-467353f08157 | -8.21152 | -55.0488 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fe9a7f6-e83e-31db-a449-e15702ecccd2 | -6.75384 | -58.66624 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c5709256-3e95-3ae4-88b4-841179280145 | -6.85712 | -59.4491 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 635d078e-e1b0-3fb3-806b-1b51283e6fa7 | -7.54999 | -61.17777 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc217c8d-bff9-3040-919d-456f49a72600 | -6.7962 | -58.63926 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b8ae10d-03a9-3d75-8f0c-840f12404c6c | -8.63059 | -54.73028 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838d3535-ed37-3bc5-87ea-fda3b9234768 | -6.01464 | -57.79228 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3743aec6-81df-3303-ba76-73460d93d961 | -6.69333 | -58.94544 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6afbb62-efc4-30ae-903c-0831441af95a | -6.11617 | -59.91346 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ac91c61-6cba-3ae0-bf3e-764e0d74df5f | -8.57785 | -54.79306 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6846d49-36a4-3680-b7e9-3505aff926ba | -6.86055 | -59.44752 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f748969-0478-363a-9462-ac1900738c30 | -9.44328 | -51.61535 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a938eae-ee3e-30ba-9aad-7dfb406a5c7d | -9.20926 | -60.76475 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e88f294b-8b4d-31d0-a3c7-b9e96d416639 | -8.15169 | -46.7213 | 2026-08-22 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 47098f29-d311-3fa0-9ab4-a399101e4342 | -8.63055 | -54.68208 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7b4dd0f-929c-33de-a20a-1b862404886b | -9.43656 | -51.61808 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31332bb4-8026-31ba-935c-7226dd1f5579 | -8.53096 | -54.84551 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a960ee03-99f7-32c6-a8d3-cc22f093419b | -6.86504 | -59.44831 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e34987ba-78d7-354d-8413-22d0bc10a747 | -6.48668 | -51.59874 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8c2cddd-2af2-37c6-8fc9-3cc5640e8758 | -9.18719 | -59.44515 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d3bfe69-f664-3ed2-8b93-24f3ec6d7367 | -6.76485 | -58.70528 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ac5d0a-15cd-3077-a45c-ae84a0f6105d | -8.59114 | -54.75402 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e336b0d4-e7da-3de1-a78e-5728baff991c | -5.78672 | -57.18812 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e6831a-f08e-3916-8524-388d87b23f08 | -8.57025 | -54.66851 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0555e7-ff48-3e2c-a20f-d5b8f10013a8 | -7.05619 | -59.83923 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 172687a0-ef2f-3fbd-adca-3b880d4dd9a4 | -13.2553 | -51.61199 | 2026-08-22 05:04:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6b00ecd9-5ce5-3532-ba26-c25e0129232c | -13.3814 | -41.34739 | 2026-08-22 05:04:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 239c0795-cc5e-3fe6-a27d-70fe1b782551 | -8.10119 | -51.65619 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6362dbdd-499a-3c6e-a255-6b27517d2190 | -9.58531 | -60.51173 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8417377e-c468-32a2-8400-cac585fb2fab | -10.79435 | -50.56277 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 457e8af5-1a62-387a-a159-c25616bab7ed | -6.76502 | -58.65187 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc7adb55-4c22-371b-a54b-749a6fd289e3 | -6.80532 | -59.41957 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f6067753-09ac-35f8-8485-7fe09d0196b8 | -6.85421 | -59.43945 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48629858-9671-31d9-b9f8-f707261b2b45 | -6.94126 | -59.30905 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 898d2db5-7a4e-3efe-be82-b6f81f7ee92e | -8.49894 | -54.87039 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd622956-4349-3ba9-a9eb-b4195e678efc | -9.21084 | -59.76946 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae6ae76d-a695-3674-a988-a55d0f3368c8 | -6.15575 | -57.74304 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b3dc8a-7928-3334-b9f6-e2b4e1d2c4d9 | -8.52775 | -54.8224 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29fe7917-fd20-3e38-bc80-9030c34f2997 | -9.00124 | -50.7462 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6d6ca5c-8601-3f9c-a698-ebcf181e5e96 | -6.81135 | -59.41135 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac8ec607-8fcd-37f6-8eb3-d0f09eeb49bc | -9.21811 | -59.77972 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e35905-8b1b-3643-9bcc-00922e67ea19 | -12.00795 | -53.42501 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93fd40f0-ba99-3fa7-8d77-e3dfc0335360 | -6.27466 | -62.5362 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e19e48f7-5645-3af6-b88a-1d4ad93ee58c | -6.82477 | -59.41376 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e17d0266-7195-3feb-b856-0b075b3e47c7 | -6.79855 | -59.43204 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c9e720c0-d91e-3b27-ae85-966c8a6267c9 | -7.35837 | -55.51832 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34badd7e-10f4-37ed-a444-d7d528aa3149 | -6.7941 | -58.65138 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 63b14d59-0724-3f58-b884-5c600ded9f8c | -6.90095 | -55.70987 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 975389b1-9938-38e8-bdd3-2c3f23a94be3 | -12.27668 | -43.16395 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ec51c700-7c94-36a6-ab27-281ec1ee3712 | -10.68719 | -50.30547 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34881b6b-1861-30c1-9292-2ccd3a02f0f4 | -6.77441 | -58.68891 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5fcae598-159a-3d23-8c0a-252a06fec427 | -6.43692 | -54.95248 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1f1859-5412-3c34-b3fd-2cb9c6d4ef60 | -12.00073 | -53.42748 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d79abc0-e8d1-3183-a31f-343f18868257 | -6.97146 | -59.05488 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0491eb92-0cf1-3a0a-9ee8-c5843c95b2bd | -6.54758 | -56.26484 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0109701-f8b6-3dcc-83fe-da6835ea2d8f | -6.22709 | -55.4857 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8134bf6e-4807-34f5-a21d-34072dd1afa4 | -6.09445 | -59.95589 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42457c15-7738-3002-97f1-54ef26323c40 | -9.048 | -60.44954 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d48991a-0193-3654-aaaa-8dee03484143 | -6.38247 | -54.94811 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7c3831a-3add-34e6-8028-8ae0d1fd263b | -12.00461 | -53.42447 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fb34ebb-6333-36ab-a1c4-40e85b9c3204 | -8.04099 | -51.79895 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62c87714-ce40-3c4e-bbd4-0fff9c84a823 | -7.07197 | -44.9935 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fe61b53-1943-3011-9be2-d8792ddc0258 | -6.96274 | -59.05334 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e6733cb1-a787-3d7b-b7b6-3cb45db0c759 | -8.53055 | -54.82662 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e55bd88-d5ed-30dc-92a3-3cdc0c0d542d | -6.85343 | -59.44387 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9bef4f0-6881-3503-bcc3-9762ad2b088a | -8.53235 | -54.81565 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c365090-3cd9-3b80-9651-da26e8ab4efc | -6.85607 | -59.4467 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 014ab4a7-9029-3850-8007-cc9691c08459 | -8.99536 | -50.73743 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e556e7e7-d629-3ca7-b048-cb69f229d765 | -6.42838 | -54.92825 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45640fc3-d2d4-3f1b-8a32-db1a169a7811 | -14.40257 | -43.79054 | 2026-08-22 05:04:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caa26039-ea17-3cde-8a23-3c2650b62ba0 | -6.7599 | -58.70858 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a01fafe7-9fdf-3677-bcde-8dcd076da5f5 | -6.82668 | -59.67435 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| dc9b5701-a339-3095-9bb7-5ca018229829 | -6.12261 | -59.9123 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c960f6b-736f-3e5e-998f-c69f4635b587 | -6.63444 | -59.07927 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9211896-22d9-3a6f-849e-f3b31f8d652e | -6.80182 | -58.63207 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bae3cfd-0c11-33db-a52f-ca0e699291b2 | -6.20673 | -53.09142 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cffcf73-aa89-3d93-b4c1-ba30ebde18df | -7.60074 | -60.82423 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67ecbc8a-cc43-3324-a65e-9d5e0f2ad4c0 | -8.55018 | -54.85608 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 865592c0-30c6-3f52-980d-d85625a2226a | -8.39574 | -62.68596 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| e30a01d1-e34d-3fed-89f3-3286b9d54d4e | -6.79896 | -59.59145 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33d16d38-9aed-32ea-bc94-790b493bbddd | -13.26179 | -51.61717 | 2026-08-22 05:04:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b14e9e0a-8634-379b-8e5f-fea21d3f0fca | -7.00047 | -59.59346 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfeaa5d0-e58b-38a1-852f-0ab4c5b7d828 | -6.87661 | -59.44339 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d303c7b-40c7-3eab-8433-9fedd4a0f93a | -8.02641 | -51.8039 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcb5cbf5-fc18-33ca-b509-bfaa70e93cc2 | -6.61016 | -58.38979 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57e91d58-fad9-3f39-9b4f-67280206fdce | -6.17145 | -53.50444 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ad522b5-a4ba-3bc6-86a4-9c0ec8c4b886 | -9.1066 | -60.92362 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a77f46e-3c23-30b9-a99a-0def32b573c1 | -11.38411 | -46.35089 | 2026-08-22 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 364704e2-2e44-3a14-9c13-0fc6c189db5d | -6.77675 | -58.68662 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a3df59b3-3caf-36a3-9696-f4a9afaea38d | -12.77556 | -48.40672 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39cb2791-a895-379e-9726-16666b28dd81 | -6.22949 | -55.48471 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6545caf-545c-3576-9536-4d3d4c6fefcb | -10.83947 | -57.51648 | 2026-08-22 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5f01fd-a42a-35a5-8ae7-3f0d4c348c02 | -9.12271 | -61.5932 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64b60b7c-acf3-32fa-bdb5-ff2f4633089c | -10.25778 | -50.29148 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10146c61-c55a-3fb2-aa3f-5556d53718d6 | -12.76444 | -48.39323 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 30d340a5-fbae-3625-a9e3-d40c4ed68387 | -9.52313 | -51.64289 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4aa08a63-630b-3a2f-81da-f6c5aad3acbd | -7.17481 | -42.74923 | 2026-08-22 05:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README40.md)
