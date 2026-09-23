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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5a57df8-3541-3f35-a1b4-313dcdfcf319 | -14.64402 | -45.65226 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 025af4ab-0220-3455-99a9-f57c47d9a4f5 | -8.25596 | -50.86976 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8980d11-7bcf-3779-ab77-8e1aa9efe4c5 | -11.2897 | -51.3305 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9151b78-8925-3649-a396-ecf85b01faad | -6.43351 | -55.61821 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6100477b-36e5-3b2b-a5de-9e3ec7857d61 | -8.7884 | -45.62904 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9838d4ce-2753-3df3-887d-072c1d313f69 | -12.02322 | -47.8052 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a74b429-2505-3208-b5cb-74e67512cb72 | -8.3032 | -44.75358 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46c56d27-0e8c-3af2-9c56-a8cdbaa1ae9e | -10.45675 | -44.95002 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9dbf873-06e5-3dd4-9720-def77e2319b8 | -5.89649 | -52.09353 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cde32fed-6fe0-3e5c-a38d-f6a48e5d057d | -8.19376 | -54.71724 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f93c0250-85d2-3b8f-ab3d-79ef4751fa05 | -12.77047 | -50.9048 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1fa6e29-054a-360b-a6b7-f47343d36b0f | -10.54522 | -57.44186 | 2026-09-23 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77fd4f8d-7cd4-3df1-9b5e-e677f6bd03c7 | -14.62996 | -45.6501 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6da28b2c-79b9-3b40-b9d8-2340f04ef7d8 | -12.76109 | -50.87346 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b51d715c-e6f1-3af3-a587-685481a022b1 | -10.70766 | -48.71836 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c38204d6-c6f3-3ea4-a1a9-dd435a1942e1 | -12.0493 | -50.34646 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20d95d88-7b99-3fc8-9153-4d31d8429b1b | -8.30646 | -54.77754 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 72ff543c-4fbb-3b01-a6e1-de5eccc82f13 | -6.35189 | -57.77021 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d896a593-ae23-3000-a4fb-8499b998bf18 | -10.72223 | -48.71328 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f83b291-4338-312f-8aec-95ae89258a7a | -14.59341 | -45.62469 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cdd8130-744f-360e-b2e8-e08640fe9076 | -14.60512 | -45.64307 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6c1a5bdd-babb-3b1f-a9d7-3cea5afe82fb | -13.45941 | -46.26812 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca33f673-f0cf-3b2e-b5af-92475daf6d00 | -8.08548 | -44.34167 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7db733-0bda-3d47-8516-8fb3a06281bf | -10.29547 | -49.11621 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0569e899-1ac2-3c61-a034-42aaecffe1cf | -14.63463 | -45.64246 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72029d25-159c-31e4-aeac-7911a5566718 | -8.33276 | -50.82607 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5931be3d-15c2-3acb-bf35-5e80073aad95 | -6.62064 | -59.99348 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6677aec-b0ba-3b81-b010-7c207cf0158c | -9.71154 | -37.27434 | 2026-09-23 04:27:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5018ac0-a060-3a3b-a613-06813254c539 | -6.64704 | -59.93043 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c3d62ca9-0f9f-3b4e-b33a-2fea15b2f605 | -14.64051 | -45.65171 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5862c05a-2f18-3f21-a493-e15474ff53e1 | -12.71905 | -50.88874 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1df53fd-d320-3757-a38d-85a779a9d031 | -14.59868 | -45.63794 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| b907484e-d014-3f2b-8a14-00492248cb95 | -9.54083 | -46.28901 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aba0eb76-c2dd-3dbb-aef8-4f77efef5daf | -12.86124 | -50.86067 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c11df45-da26-36e1-ba21-a30bcec47744 | -14.6329 | -45.65471 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 066b1f74-44b8-380a-85c5-7ef1f0c4d30d | -11.09453 | -48.34239 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b95313e-693d-3844-94f8-393f8b70a8ac | -6.19162 | -57.78231 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9747e7b7-28b7-35b4-b6f1-0202a6cf8ad8 | -7.46249 | -45.50283 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93f74d7c-47e6-3daa-be95-f2fa899e5323 | -6.89352 | -55.33685 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 014c409b-286a-307e-b0ed-e4f3bea81821 | -7.78574 | -50.22766 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 390db0e9-8ee2-3fc6-8a90-4607b8d4cc87 | -11.78643 | -47.44704 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 593ef876-bf3b-3fd9-988d-df93de6e83e6 | -6.67326 | -55.07176 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76455146-c0d8-3ec2-972b-5ac5a946e8cc | -8.45675 | -48.70591 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcfa1cca-3366-3bec-9998-ab597c19c1be | -10.7183 | -48.71634 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b51af7f-2fbb-3553-bb7c-80e414171cb0 | -5.45704 | -60.14736 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 11bb7da9-9adb-3dd6-b69f-58a5ab16a53c | -12.08052 | -50.35921 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a06dc222-f785-3f6f-874f-c4c51d41c1d5 | -14.61334 | -45.63602 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bf30cc44-a689-358f-97f9-ab257ca19e6f | -6.30901 | -59.94633 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 383d8ac9-5ed3-360d-b955-5ca191c5c65a | -14.6122 | -45.61911 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f728b80a-cea4-381e-be4a-c7286e4a4e33 | -11.652 | -47.80616 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c307c5c6-3fcf-3443-9276-cfcae1ece347 | -10.51054 | -44.8608 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc4a4194-e754-3ef6-8705-62e8ee512b4d | -14.63637 | -45.6302 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 673155a3-bdf3-3eaf-befb-a30ec41fe9a2 | -14.62587 | -45.65363 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4039e5e-e966-3928-a946-549c9925acc7 | -6.67929 | -55.056 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6da8719f-930e-31c5-ac1e-71a9a90cbf26 | -6.66335 | -50.88561 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72fe494a-f202-3253-aa80-b44e9ed75b2d | -8.28702 | -54.77423 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f95b509d-803a-30bb-b438-ffea2d6024c2 | -11.93892 | -38.2923 | 2026-09-23 04:27:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 9d269fb4-3131-3a9f-87a4-104409105936 | -11.70699 | -50.22131 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb7ef92-4c0f-3b7f-b9c8-1d9b71f1caf7 | -10.90334 | -51.523 | 2026-09-23 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b79a1243-648c-3f93-b813-a2c90f16e6ad | -5.8958 | -52.0976 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faf58b11-b1a2-32d9-a193-c15ee4eb7e11 | -6.62507 | -59.93323 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5dea6a0-84c1-32b8-b4b6-e887d084bab8 | -6.73674 | -55.08721 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b8adf9e-a928-3547-942a-385f0c39838c | -8.48528 | -44.75333 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59cbca77-4a96-35d3-8992-4be19e8fa141 | -9.84319 | -46.37945 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c8c83a5-d0e5-3688-8779-7333bc1214e1 | -10.26916 | -49.98063 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1708cb77-329a-30a7-9c5b-d12256ffc291 | -7.1017 | -52.75003 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 696b9109-e95b-383c-8ff0-9cc2de241912 | -7.54587 | -48.6909 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fcdd6e4-3aa7-3c02-84df-7ca1f53a183e | -9.17264 | -51.47504 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25c836ef-4ae6-39b0-8416-cd17e768d53d | -11.30295 | -51.36517 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39fb67c8-c26b-3e09-a42f-1297deac4e12 | -6.74819 | -50.67994 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16229aa6-c59e-32cf-b6b5-016d1a6ac96d | -13.29873 | -47.88938 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c981c24-b650-3e9f-a19f-34fb1b45a131 | -8.48698 | -44.74193 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f7efc75-ddd4-38d2-8243-585c493422c0 | -8.49215 | -57.61107 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 62fb1cc0-973c-3323-b51e-a132a4cc948e | -12.07235 | -50.05185 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88e4ad29-66d3-31b6-a954-5e3a1dac1b44 | -7.18717 | -47.44532 | 2026-09-23 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fd59e02-d6ee-31f3-952a-0c8c7f9426ff | -7.55855 | -48.6776 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e81984ef-3a63-3e2f-8a9b-5e9385bb4ddb | -13.22165 | -47.02264 | 2026-09-23 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9feaa7b6-f15b-3da0-bab5-79020d03bfd7 | -11.26465 | -43.41737 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e86e17a0-9e32-34d2-8843-34a236ddbb9a | -5.89294 | -52.08895 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31b26232-9e71-3d9c-9ba0-20632a2a163e | -8.49825 | -57.61407 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18ac2dd4-54cf-3eed-aa55-380c9616b2c6 | -7.42494 | -49.85984 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5636fbcd-b4c5-3839-b876-ad5a5ed10d4f | -6.7842 | -48.68597 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1902ca45-4279-3da1-a4f8-f5a9ce391228 | -8.80218 | -44.27374 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19655561-d177-37af-bf02-a844fbb42db8 | -7.43195 | -49.83923 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2bd71b89-1aa5-39e1-8756-5a66e812363b | -10.25361 | -49.98244 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8309111-55a5-35e0-9f7a-2320c70117b3 | -14.62503 | -45.65438 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6f189b3-25a4-3ad5-a37d-f9f81fe057ed | -11.78367 | -47.443 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f1227c4-cefb-39cd-ac11-2e2b9cd36cd5 | -8.35861 | -45.61836 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2764434-baa8-33e4-aae3-f8d438581c31 | -11.89363 | -45.76855 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ce82c14-932d-3d44-888e-4fda6498ad6e | -14.61741 | -45.65737 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdbb0629-bc67-3700-8704-451a962ec582 | -7.57036 | -57.67769 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf5f0bf0-87db-368a-befa-b34d561dc43f | -14.69565 | -45.59331 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d4b6dc60-f1ac-3174-8319-0ecad281d5e3 | -6.68282 | -55.06562 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c81721-1d52-356e-a32d-5bb1ed6f50c3 | -14.65042 | -45.60727 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c3268385-5946-3752-8a13-df53e1a77877 | -6.81932 | -47.8758 | 2026-09-23 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3cc1725-2b2a-33b2-a79d-11137f3566b0 | -6.67162 | -55.06957 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f8f8da2-a051-3cd4-85c7-ff8346d43c88 | -10.12735 | -46.07404 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc937371-f9ed-3858-a988-8a6b31be7c69 | -6.74124 | -55.30623 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a397b560-fe91-3fd3-8309-f807b38270d0 | -8.49798 | -57.61213 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e788c1f6-83f4-3431-ad9f-180f581bc39a | -12.34763 | -47.68517 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README67.md)
