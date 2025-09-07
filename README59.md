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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd4f6749-c787-34ba-87a4-34e84c893cdf | -19.47206 | -47.77033 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 12c9a681-a1bb-3b23-9737-9e2598cb2b73 | -13.83638 | -46.25912 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b1246d4-f34d-3079-a245-1b728496bdd2 | -19.59758 | -43.68486 | 2025-09-07 04:21:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 534893b4-6d63-39f2-a102-801b32983954 | -17.10176 | -49.88935 | 2025-09-07 04:21:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ca1d1c-c834-343d-89bc-3a40425b7b71 | -12.95188 | -54.81142 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019af320-fdce-3e8e-9054-b537742e6a0a | -14.44951 | -48.45328 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31057554-646b-3424-b483-e532b9b5bf71 | -16.34166 | -52.95149 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5139385a-f847-338e-862f-403388ea6602 | -15.36841 | -46.42611 | 2025-09-07 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09f8d63b-e859-33f2-b04d-25d7e1a5b6ce | -13.05525 | -48.07679 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bfe30f1-c5be-3f28-8d12-42839c392c5e | -13.83029 | -46.2763 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0bbf36c-4811-33f0-b255-03f39c136d37 | -17.37989 | -49.23748 | 2025-09-07 04:21:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b4e60a0-d07c-3b0d-b1ca-a978837a9c21 | -17.36378 | -42.64373 | 2025-09-07 04:21:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 41.5 |
| c5f0ebbe-b3aa-3518-8e91-448ac8f36709 | -15.53069 | -42.62674 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8991c212-8fc5-3b64-b415-64062022509c | -14.59348 | -52.16017 | 2025-09-07 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a162c39-3678-34d3-848f-2aeba8050422 | -15.53534 | -48.37915 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50588fe0-bdde-3d91-8b24-75f91c3e29c2 | -14.56192 | -48.02655 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1272361-7ea6-3e72-8adc-f30dca2cfbfa | -14.48547 | -48.76799 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 501f51ab-5097-3521-8083-d0985615acb7 | -13.83305 | -46.28038 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9af01abf-26da-31af-a801-cfd5ca18ce5f | -14.50169 | -48.77038 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d1c8752-faf4-366b-8a2f-700bf4bbac07 | -17.87875 | -44.33083 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07e3bb70-bec5-33b0-a3be-c871778405f0 | -19.34356 | -42.17247 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5f41ec37-27a3-3ecf-9f72-f2c26bf08606 | -13.04439 | -48.03623 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 781270af-d3b9-3bd3-9bfc-9b175b1594ed | -14.56005 | -43.73055 | 2025-09-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b45bdc39-5d7f-3017-b6c7-b59129ea1211 | -18.01895 | -44.90679 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c3de3a3-801e-3379-aa3e-c22927ee4bb2 | -13.82256 | -46.28227 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b4ae4c-f89d-34cc-a3a5-d401348abf55 | -19.88967 | -41.43123 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fd415058-e55d-3a7e-b396-43c663c1f484 | -13.47352 | -46.83479 | 2025-09-07 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f256d45-37e2-3d6f-9e0d-457d5efb2e5d | -15.37228 | -46.42309 | 2025-09-07 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f769467-1351-3088-bb2c-e7f218ac73da | -15.22439 | -52.35178 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fbe0c24-9946-35f3-ba91-272d937e4bc8 | -15.84139 | -52.27384 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b01dde87-eb8c-3074-8ed3-2597fcc7e661 | -15.03811 | -50.0387 | 2025-09-07 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04551da8-79e5-31ad-9508-4a48a62aa4b6 | -17.62881 | -44.79031 | 2025-09-07 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f4afd82-a44a-3cd1-a778-bd98e1449f66 | -15.22372 | -52.35544 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 20a42f11-94c7-3857-ad4f-a8b8370aeba1 | -15.29798 | -46.98176 | 2025-09-07 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28bc1756-61ba-3767-a392-7e8048d83bda | -16.90406 | -45.77166 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 495094e1-8610-3be0-81c1-62a0a56950a1 | -13.47827 | -51.82586 | 2025-09-07 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92d36f14-eed4-3c6f-94d3-987926d6ee8a | -13.82974 | -46.27984 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26adef9a-0984-306d-a767-1677719ce2a5 | -13.91871 | -48.03243 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f5ff939-9e37-3d0d-88a2-46922d1dc0e5 | -19.89255 | -41.43325 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 336a45bf-7aa0-3a24-93cc-4227b852a7b7 | -14.58417 | -48.10258 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c466d41c-d9c1-3411-b44c-f5a870c0fb11 | -16.90462 | -45.76795 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6a52f71-48cb-342f-94cc-037b97f6fbaf | -15.54087 | -42.66026 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| abc9d908-8c30-3dae-a1a2-e7e2aabd32ee | -15.13693 | -52.32765 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 169f4167-e659-32bd-8f29-69a4e2409d60 | -16.32974 | -52.9453 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8384e5e-b439-32e9-8d46-351a36ee7ee1 | -13.82666 | -43.85883 | 2025-09-07 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579fb564-3411-31ee-9477-409bd11dac18 | -18.12027 | -44.50311 | 2025-09-07 04:21:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f5909fc-550d-3dd8-a304-c3fedfbddcfd | -16.9359 | -45.75378 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6161c0c6-427c-34aa-b8bd-33dde179c0e1 | -15.23679 | -52.37745 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69c5b5d0-bad5-3af0-96a8-8efe62a2942f | -16.28871 | -45.68539 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a69607e6-b52f-3612-9afa-5b87cf22cc55 | -17.24622 | -46.70156 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f2bcce95-ea3a-3b1f-91e0-3e02326551c8 | -15.7088 | -47.51362 | 2025-09-07 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e904a9a1-7cef-39ad-8508-479522fb73d7 | -16.33047 | -52.94137 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 811cf460-2efb-3643-96ba-1e09ed879d13 | -12.77894 | -52.95329 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699f9f4f-94d2-31c5-8071-856672cd832d | -13.83858 | -46.26674 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 769b86ba-65f9-36c9-b520-71b0768b37eb | -15.14766 | -48.16032 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d37afc5-e80a-3ee0-8048-742c9463afa1 | -15.35891 | -43.67219 | 2025-09-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91eb9919-b006-342f-996e-0cb199a5ba6d | -15.82202 | -43.35488 | 2025-09-07 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27975ada-ae2e-394d-b0b7-57cbb4cdf489 | -14.85135 | -46.69192 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d998ad70-6ff0-331b-accd-80dd07b162e9 | -12.93693 | -54.77996 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 05aceb71-e476-3245-bb00-c8546c4ebcbd | -14.81903 | -48.19522 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6dd6ec3-b664-3bf0-a634-5bac39c3ecc1 | -15.72524 | -53.55794 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| addcae3d-5608-35bb-a84a-7dd7312568d2 | -18.24674 | -45.20595 | 2025-09-07 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3163f711-f1ff-3f29-8d19-d0db76b07bc7 | -18.14843 | -45.23524 | 2025-09-07 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff8103bb-4615-327a-8509-4be4b1551128 | -16.28075 | -45.68108 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b0e065bd-8ce1-3eb5-b50b-640b7bb64068 | -17.37647 | -49.23687 | 2025-09-07 04:21:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 629e0b55-0982-3dc5-84bb-89073e36b831 | -12.93959 | -48.03389 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 820bd3d9-7bd0-3400-9a09-b48d8d116954 | -13.0012 | -54.81997 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef7c0e43-bd74-3041-8e54-78da42d93254 | -15.02174 | -45.45639 | 2025-09-07 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e690cdb-af1d-354e-b070-e7a63061546e | -17.67876 | -43.5344 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ea6334b-7259-38e3-a3cb-bec2bedc00d4 | -17.68044 | -43.53661 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f4dcda4-3ac4-337e-a45b-61f45d3c7c79 | -16.30497 | -45.69183 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1c2ef4d-3f11-3c96-8b5b-7d706adf31eb | -19.40968 | -44.31401 | 2025-09-07 04:21:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fb8cf6f-5554-3b57-9b3a-6c48b8aaa617 | -17.84407 | -47.77775 | 2025-09-07 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7c5bc8da-81b8-334b-8854-1e085e15dd6d | -18.23449 | -42.6659 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 88d3a3bc-0259-3a22-9bdd-fa0a84b16c12 | -18.00775 | -43.47995 | 2025-09-07 04:21:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fd9891e-744f-3649-b23a-794948a06a8d | -14.44272 | -48.45189 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 419c6898-2224-3ff5-9749-5f74534e60b0 | -13.02775 | -48.05215 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98baafb1-659a-3e35-ad39-f17f1ac28b54 | -19.47985 | -47.76419 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da45870-1d19-3b72-bb18-8498e6b445fa | -18.36269 | -43.91571 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4179b778-0165-3259-86b6-4a1d7fa196a0 | -17.71548 | -44.48629 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41ffbf8c-a934-3999-9a55-f8c9fc509202 | -17.24336 | -46.74197 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 429dde65-831d-36ad-a9d5-75ef8d89304d | -12.19392 | -53.90596 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6c69535-5415-3b13-a50f-677bac7d5af2 | -16.33213 | -58.11936 | 2025-09-07 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f654d6d5-fcae-3883-bebc-a553f649ce87 | -13.02834 | -48.0486 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 203acb56-c670-3b00-abcc-930ca1865d2b | -20.54236 | -46.4471 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 889b4606-c458-3076-b746-20e807b01b2d | -13.90979 | -48.02315 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 160091d9-263d-3329-8d8e-98feb9c117a7 | -13.9329 | -54.02876 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 871d286b-8da0-3e2f-a7dd-868a1c2a1608 | -12.9513 | -54.81449 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4eeb57b-ad31-362f-8f66-07ac38ae4ac7 | -15.83694 | -52.29771 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b2d4758-d90f-3cb0-b2bd-7aa0142c35ff | -14.53623 | -53.15631 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6829d23f-7212-3a48-9b2f-f98aad01be5a | -20.22097 | -44.20756 | 2025-09-07 04:21:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a7311f66-b42d-3ce3-9cf2-c52689c3ffb0 | -16.69056 | -49.07825 | 2025-09-07 04:21:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2a629c9-635c-3992-95d6-4b735fb29e75 | -13.8983 | -53.99875 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 857a69f2-0e07-3304-a959-b882859cd770 | -19.89638 | -41.43796 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5dce433c-2d4f-3b47-bfa1-a64ea1f67a92 | -15.12008 | -52.34987 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e9d3bcf-2703-31c3-aa84-54be2f674b5d | -17.69319 | -44.51567 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1bd5fa1-6133-3579-b985-4b0335b0956c | -19.21741 | -46.81019 | 2025-09-07 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e7f6991-4e9e-3791-b693-1a9f525934cb | -16.32633 | -58.11789 | 2025-09-07 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4d62b04b-c461-31d5-ac9b-5e812496bb37 | -14.49825 | -48.76974 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9f3aca3-db98-39fb-8745-19339f982c8f | -18.98564 | -44.22911 | 2025-09-07 04:21:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README60.md)
