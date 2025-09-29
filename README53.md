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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1759b8c6-96cf-3ada-8fbb-0d15ebf70837 | -19.86455 | -43.8339 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d92b2607-c78d-3a59-a217-da4bcc771954 | -17.7023 | -46.70471 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd546774-4612-3739-bc6f-ebf3bca1d576 | -17.0007 | -43.50722 | 2025-09-29 04:10:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62361d32-cf27-3c39-8a95-69da46288db6 | -17.71286 | -46.72762 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff120867-a8cb-3645-8e46-cfca0eb5eab8 | -19.00051 | -40.50106 | 2025-09-29 04:10:00 | NOAA-20 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a347164c-c756-3243-a5d6-b9037f0ea295 | -21.33457 | -44.48954 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f7a7d08f-02f2-3ef4-abf8-11bddf759f6e | -19.86686 | -43.7965 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ffa66b8-bcef-354b-accc-824fbd52c346 | -15.84544 | -48.23706 | 2025-09-29 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f1e028d-e5cb-334f-8f9c-d73d07f6eee2 | -20.05039 | -41.33725 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 64bb0a90-44c6-3190-85c2-ff4ee4d7d89e | -20.04622 | -41.34072 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7ff42005-700f-3bff-84ff-943be08a7be4 | -22.03 | -46.49209 | 2025-09-29 04:10:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7c661277-5bdf-3236-a5c0-961abba85be0 | -22.07901 | -47.26958 | 2025-09-29 04:10:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2dfac19b-46f0-38cb-a06e-2f7682c1387e | -16.5026 | -46.03237 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d4695ff-d982-3f4f-a8fe-5dfdbf3b537e | -19.85574 | -43.80221 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7c313951-d3e3-396e-ad8e-03f79c429599 | -16.53563 | -45.28622 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e48ce0e-3f11-35db-bbfb-53ab02cf9a52 | -21.72737 | -44.40456 | 2025-09-29 04:10:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f117f905-b4dc-3f53-8bd5-f2fd32ede03b | -18.86213 | -41.98872 | 2025-09-29 04:10:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f90e1eec-7d3f-3f70-9a42-e6b858a1dba5 | -19.85907 | -43.80279 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 424ca8c2-10ab-37ca-9791-7e8e7f588587 | -22.09247 | -46.83843 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c5a5e3d-2e53-39ca-a66c-2f8ad6fb8c1d | -23.22387 | -49.41261 | 2025-09-29 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 53fb7fb7-8bb8-3d19-8eb1-249a1db504bc | -17.70951 | -44.31047 | 2025-09-29 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e47cf0a-a46e-3efb-bc60-08a2693c3651 | -17.55009 | -44.81617 | 2025-09-29 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97969111-d3ee-3016-8d66-9978b3c0c31c | -19.96915 | -41.73629 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7b15d8a1-f00d-3335-9181-15455cddaf24 | -20.04321 | -41.33582 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| aedf358c-40be-39d7-a07e-9bec263048ee | -17.7163 | -46.6862 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8964acb5-d611-3820-b808-cd0c062a5696 | -17.74009 | -46.69495 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f165bb9b-7dd3-355d-8219-cfe57938e9ec | -19.32861 | -43.81257 | 2025-09-29 04:10:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbe19f94-510e-345a-802f-98ed92a4d212 | -19.20054 | -43.98232 | 2025-09-29 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d201ab9d-d76a-386d-a9c8-622b1ef3bf05 | -17.90765 | -57.61687 | 2025-09-29 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3e638a45-2af0-33f6-b1bd-b3aeb1a0c840 | -16.5393 | -45.30614 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0383e39-91e5-33ea-9d50-5fa9866a5c84 | -18.98885 | -43.35183 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a791c4b5-c609-373d-a983-371fffde1ee0 | -19.82465 | -44.63696 | 2025-09-29 04:10:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ccc0a821-3299-3f86-b049-b4f21c8be627 | -22.75738 | -44.74392 | 2025-09-29 04:10:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49456697-e453-331c-91dc-0880d645b6be | -17.55068 | -44.81251 | 2025-09-29 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b5bf6a6-72d2-3e7c-ae18-e77aa2afd171 | -17.72329 | -46.68752 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a909444-bbe8-3fa0-94a0-0923c1730ed2 | -23.54372 | -47.54207 | 2025-09-29 04:10:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 436091e6-2db4-369d-8928-e36a1e52034e | -18.91314 | -41.12719 | 2025-09-29 04:10:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ed693e24-56f5-3f93-9cd3-a66c13cf1b06 | -19.7483 | -45.98611 | 2025-09-29 04:10:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4603a78c-0bd7-3686-8b44-42b1b75ab7e1 | -16.294 | -45.85178 | 2025-09-29 04:10:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 935c4567-c336-30f4-8aaa-bea4ade03b9d | -16.49848 | -46.03571 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9425517-c2fe-338d-8faf-dd2ea7dd11ab | -19.30698 | -43.82025 | 2025-09-29 04:10:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d7cb62d-5ce4-3a3c-a14f-f3c9f26c8b9b | -20.40953 | -42.34612 | 2025-09-29 04:10:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1dee8a6b-7cbb-3341-bf84-91d9fd47e72e | -19.32917 | -43.80892 | 2025-09-29 04:10:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2a23c3-5d02-3db5-8a11-f364aeccc5f6 | -22.0857 | -46.83715 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 858a3d07-e725-388e-b75c-7ec0c4d104aa | -19.92889 | -41.61596 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 011e2db9-a56c-39e7-9c62-ecbc85891cc3 | -19.94329 | -43.67654 | 2025-09-29 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 17888614-b690-315e-8c10-d3ce891f2bdf | -18.79309 | -47.43485 | 2025-09-29 04:10:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2c1319b-ef2b-3ad8-88b7-6df8aee2a485 | -23.2302 | -49.39898 | 2025-09-29 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0c68877a-7513-3c59-a27d-146710a3a42a | -20.0498 | -41.34147 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 3ab76491-70b7-38db-833f-c717dceb6640 | -19.69408 | -43.908 | 2025-09-29 04:10:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07fd810f-bcf2-3e8c-a0a9-dcb1d320df26 | -17.97606 | -44.30071 | 2025-09-29 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ed631dc-1fcd-33c3-86ce-83ff0dbe5da4 | -19.67354 | -43.73058 | 2025-09-29 04:10:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e84a3ceb-a4bf-3dfe-b91b-ce31881f0d41 | -20.04737 | -41.33245 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1721a40e-86d1-30e6-abe5-eb8c3e8bbfcb | -19.96856 | -41.74057 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| af3aae77-a749-33ab-9ef2-2594942dc956 | -19.55752 | -44.21998 | 2025-09-29 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30ad8f30-d8e4-3dfc-9479-551d1bcae7f8 | -19.18272 | -44.93477 | 2025-09-29 04:10:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95c8032c-44fe-351a-9319-efc3a2b9a480 | -17.3977 | -47.12339 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab901837-d518-323b-95ad-44bfbcee5c69 | -20.63304 | -43.95566 | 2025-09-29 04:10:00 | NOAA-20 | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9cc7332d-c252-39bf-b960-7f90581fec50 | -19.47013 | -44.34352 | 2025-09-29 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96298414-8d85-36db-8804-26db4f615a6c | -16.5295 | -46.95538 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc7284bc-0fe6-3930-9a49-42314b8a240b | -17.73379 | -46.68948 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2d5a086-bec3-3ddb-8e79-0e05345d2d93 | -16.65045 | -49.53107 | 2025-09-29 04:10:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99a209ff-6155-30ac-8458-d7b5782a1e4f | -22.0316 | -46.49091 | 2025-09-29 04:10:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9dcaa9c8-4072-3a09-9b03-8313f6e5b3b2 | -16.59706 | -45.13176 | 2025-09-29 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a180b85f-437e-389d-95be-6ae59a6edee4 | -17.90533 | -57.62694 | 2025-09-29 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 562e9bd7-32c3-3c70-b616-bc2b929f5e8d | -18.85288 | -46.83552 | 2025-09-29 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 517758c5-d3f7-383d-8575-c9bc1726a433 | -16.54268 | -45.30674 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c4f5301d-6fab-35e6-9f6d-3f211e597d3c | -19.87238 | -43.80504 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 94c134e7-7948-3035-9da7-e32147a2b4c6 | -21.33514 | -44.48583 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 74b57770-607c-38ba-a5e4-4cd3f7139e5c | -20.54534 | -45.10216 | 2025-09-29 04:10:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b5808bca-f136-3b41-86eb-9321f539c381 | -20.63439 | -46.16565 | 2025-09-29 04:10:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6f8fac4-1262-35e5-83ff-ba719ceb65da | -21.41886 | -43.89487 | 2025-09-29 04:10:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d1be275-7125-3d7c-af49-58ddbcefb13e | -18.90475 | -41.13453 | 2025-09-29 04:10:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e02916b3-116a-38c2-8cac-7523abf35846 | -17.3941 | -47.12281 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 273cc9b7-e4e4-3ad7-9211-e4c189930b75 | -19.1833 | -44.93111 | 2025-09-29 04:10:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f7799dc1-acf4-3a7c-8f97-8772b24e11f3 | -15.92729 | -49.08804 | 2025-09-29 04:10:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 983b0ece-73f1-367b-b0ef-47f8d27a5b9e | -19.06396 | -45.79074 | 2025-09-29 04:10:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53261c2d-e271-3797-a5b0-0310a3caa6cc | -20.57194 | -43.36718 | 2025-09-29 04:10:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| db91bbec-1c71-3870-ae67-eee5a8658f81 | -19.3089 | -48.9202 | 2025-09-29 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b46e4838-c101-32a9-b98e-03c97093f8d4 | -18.97661 | -48.40489 | 2025-09-29 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73d7ffd5-d424-3107-917f-8568b72a9b70 | -20.07988 | -41.36365 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 431886de-ec00-3e5e-bae1-03750c26f5f6 | -16.48813 | -46.03379 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 259482eb-54db-352b-bb3a-adfae1815555 | -16.10722 | -46.67429 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80e5fd8f-3d7e-39f6-81b2-5709ef282af7 | -17.08413 | -48.57287 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 27a50fa7-61fb-3d8a-ad46-bc468adeea24 | -19.94174 | -43.6193 | 2025-09-29 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 791f9939-1924-362b-8700-dbbe2946ffe3 | -17.07625 | -48.56957 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c984df-1ee5-3293-9241-8f60e02974bf | -17.12108 | -46.98326 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c8393c4-be1f-33f7-b410-f5ed1ec0fe41 | -16.52305 | -46.94989 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37182945-bda3-3a14-9f4d-8a92e674cdb2 | -20.20737 | -41.38344 | 2025-09-29 04:10:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffcdb8a4-fe06-3745-a33d-e3ba07cc531a | -16.20308 | -48.26693 | 2025-09-29 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 81fa4496-e0e7-3a50-9026-c0a9b8313e4f | -17.08697 | -48.57701 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 55cfbfa7-4277-37f4-8429-fb024419d2ce | -21.98647 | -43.01411 | 2025-09-29 04:10:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 662b5153-d892-3878-8d2e-88340a7325ac | -16.54329 | -45.303 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 89ceb349-b6f1-3fcc-84bf-bd04bbc523da | -16.49092 | -46.03835 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef5db0f1-21d8-33e0-9be5-61b68fde57fb | -17.08403 | -48.57097 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12dc9e4f-a5e3-373c-8e4e-9e81b3398f59 | -17.75016 | -48.77113 | 2025-09-29 04:10:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 769ca9d2-1403-3bed-a30a-48b7f2646a74 | -19.74767 | -45.98988 | 2025-09-29 04:10:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10ddd274-fa66-3404-ad32-5588b5717d02 | -19.00423 | -40.50164 | 2025-09-29 04:10:00 | NOAA-20 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d8f9b9a-50fd-339c-853f-4daca8be2adf | -17.94703 | -40.20077 | 2025-09-29 04:10:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 12f5f9d4-4385-3d4c-aa12-03efcdc9e115 | -18.97793 | -48.40213 | 2025-09-29 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README54.md)
