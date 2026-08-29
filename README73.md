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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 491b0d20-60d5-36e7-ab8e-a3b62ccb41ff | -6.7699 | -55.6644 | 2026-08-29 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 17b84cdf-9b43-3eb6-9036-df5fab256acc | -5.8895 | -57.7513 | 2026-08-29 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 83f465bd-8013-36f8-a86b-ead36ae9faa2 | -6.56823 | -56.53939 | 2026-08-29 07:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 79db4480-6b4e-3ccf-8305-d3c264fe9b3a | -5.87526 | -57.77444 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5a333452-2e14-37cd-8cb1-a5d28ce30d4e | -6.41137 | -51.66885 | 2026-08-29 07:12:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| cc520d4b-e3e2-34ca-84c8-cd529e436e7f | -6.77789 | -55.65992 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ddf9ff3a-c50d-3aaf-b472-0277392c84b6 | -5.89072 | -57.74121 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| eddaa5b7-0c25-3dd9-bea9-c0cf62273f24 | -7.57196 | -61.38023 | 2026-08-29 07:12:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 3c336bfa-f3d8-3871-a418-920dc290200c | -5.88894 | -57.75255 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f8b03eaf-0674-3958-bc53-0ac110147b7c | -6.78678 | -55.66125 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 14678cb2-1137-3473-b949-462e2129b1cf | -7.50148 | -55.27509 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06307132-8ce7-36f7-af52-00dee0abf0a9 | -5.98187 | -57.67988 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d079035b-035f-3876-b28a-7ac92652d3fd | -8.58851 | -54.75942 | 2026-08-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58910198-7b88-3f1b-a61a-1b889538290e | -2.71708 | -47.04053 | 2026-08-29 07:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f748770d-43af-3bfb-b5fa-6ab977620d53 | -6.78539 | -55.67031 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 08756a90-4cc8-3581-a8eb-95990f267f0e | -8.53016 | -55.2635 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16b2fc74-7106-32e8-83bb-8f408a1876be | -6.75873 | -55.66636 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d6763eda-e8c6-3e17-af9c-185da3834394 | -2.98876 | -48.94796 | 2026-08-29 07:12:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f66447ba-f731-3e60-a161-6f72e6c96913 | -6.16141 | -57.77885 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 91326169-94d3-366a-b5dc-f9bc7f935781 | -5.87709 | -57.76287 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 691ed949-6bf4-3cf3-a1a6-f6ff31426b1c | -6.17137 | -57.7804 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a632dd08-bbd3-3bc9-a488-3ead3909c06d | -6.77927 | -55.65094 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 50dbf2fc-8f09-353d-9a81-b115f9b23561 | -6.769 | -55.65866 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 373226ff-c737-3ffe-8410-97940c44efea | -6.76151 | -55.64831 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 54a0aebf-a0ae-30aa-be0c-006ec81e4ac3 | -6.78815 | -55.65226 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f29fc8aa-52b2-30e8-8cf1-4e4eea3ffcf8 | -6.26024 | -55.41565 | 2026-08-29 07:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df7b6781-0a1c-39fb-8f00-ec803f4ad961 | -4.54138 | -54.92197 | 2026-08-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 78e6e39a-5bbf-394f-957f-90d2ac0cee34 | -6.15961 | -57.79028 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8848f95f-06e3-37aa-b416-ea00311f81c4 | -6.4098 | -51.67975 | 2026-08-29 07:12:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 760cfc7d-7d16-3b12-b0b7-a9eae37b1f1a | -4.28478 | -48.18193 | 2026-08-29 07:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 12005ec6-969c-3a9c-9477-eae966e9659f | -2.72032 | -47.03406 | 2026-08-29 07:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4fa03f43-d4df-3b36-9587-791a411ad980 | -6.77039 | -55.64964 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2c8440cf-854e-377d-949b-e77685b2227d | -5.8989 | -57.75428 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 40de7c2c-e225-3dd9-b226-5e79b577039e | -6.94876 | -58.95313 | 2026-08-29 07:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4ef0d90a-1369-340b-a009-0b0bd52bf610 | -6.75734 | -55.67541 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c971aef6-d079-3572-b5fb-6cb041ebb528 | -8.66119 | -49.5467 | 2026-08-29 07:12:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7a18ceb8-6ce3-389f-b242-78426fcf82b6 | -7.50624 | -55.30293 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8235c0b2-9853-3606-bcb9-607b22f3cdf6 | -7.50758 | -55.29408 | 2026-08-29 07:12:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1f122181-7434-3f9a-a0cf-54bf98f245c0 | -5.99179 | -57.68141 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a890874f-2ad2-3a2a-aac6-7eb1819ceb48 | -5.88711 | -57.76425 | 2026-08-29 07:12:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| caac98da-7142-3562-b2b2-e994170749ba | -6.64285 | -53.18418 | 2026-08-29 07:12:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b7686edb-d9ba-3192-baa0-648ea55a8470 | -8.59196 | -54.79595 | 2026-08-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6bd49ded-9377-3342-8fd6-a220524d0639 | -6.5458 | -55.24093 | 2026-08-29 07:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99e76b03-4e29-35c2-94b4-98448fa63d63 | -14.19671 | -52.86169 | 2026-08-29 07:14:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ba23fe0d-9ed7-359a-8ece-f3d919325850 | -11.26573 | -54.03178 | 2026-08-29 07:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3eb15aef-d662-33ff-8c16-61472aa3e66b | -15.12036 | -53.57615 | 2026-08-29 07:14:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| c76ad24d-95b1-3002-ad3e-ce3c852d6bbb | -11.02713 | -57.2495 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8ceab9ae-e15d-3bad-aad6-548d6b320403 | -10.46975 | -64.47694 | 2026-08-29 07:14:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 9f58dcda-7106-3357-a4ae-75705055b4cd | -11.03316 | -57.21132 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| bea8dfe4-c3cf-3bf8-a15f-e2782546ae88 | -11.04223 | -57.21275 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| eaa16686-1e48-39ef-91fb-e3c8ed3e4cfd | -14.21 | -52.83923 | 2026-08-29 07:14:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ff16f5ba-7868-318d-a73b-0bf8e6a2279f | -10.48527 | -64.47973 | 2026-08-29 07:14:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| de1e0775-6a2f-3f5a-9e67-10940d0f5837 | -11.03923 | -57.2318 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b92970e1-7c93-319c-81ac-536da3fee359 | -9.96987 | -53.92791 | 2026-08-29 07:14:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 57ab84e8-02de-36c3-ab94-5fcb4730d1cb | -10.47955 | -64.51149 | 2026-08-29 07:14:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 4a7dc621-6357-3cc2-a503-7ce8952d4591 | -9.92652 | -60.43376 | 2026-08-29 07:14:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e77f6ec6-2ca6-3828-9821-ba1d566fe707 | -11.02863 | -57.23998 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e440d27c-f43f-3743-bdb4-e8d1a63346b3 | -10.46402 | -64.5085 | 2026-08-29 07:14:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 8c7afc89-ead2-31ad-86f6-40b3a3957445 | -10.81029 | -50.63395 | 2026-08-29 07:14:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c951d480-85da-3e7e-b01e-1fa63801f4a9 | -11.03166 | -57.22085 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 471048b1-22ee-366b-bbf5-ad76ebfd385f | -10.75602 | -54.04231 | 2026-08-29 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 26cd2843-3ddb-340d-8457-5164fe21ef75 | -9.9685 | -53.93726 | 2026-08-29 07:14:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d2024733-7b61-3696-87bd-be3e3d55358d | -11.71828 | -54.53753 | 2026-08-29 07:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf9e4de0-c717-38cc-91fe-f0d42c27aeba | -11.70936 | -54.5362 | 2026-08-29 07:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fe4429ae-3c5c-35c2-9697-22dd0e0bc8ad | -9.92978 | -60.42719 | 2026-08-29 07:14:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9b7c1d11-6262-36a8-98a4-a45e1cb53f5b | -9.6074 | -55.12207 | 2026-08-29 07:14:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cb00ab03-554b-3375-837e-971b3f3fac8b | -10.88544 | -50.49605 | 2026-08-29 07:14:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a8821da6-e8d3-323a-85e5-332a5ca8bc88 | -11.71963 | -54.52829 | 2026-08-29 07:14:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 550b9c45-27cd-328e-a34f-796cdb794296 | -14.19834 | -52.84983 | 2026-08-29 07:14:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b453e135-ab08-34b7-b7d5-0b779bf466b8 | -10.7482 | -54.03443 | 2026-08-29 07:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 359f72f8-6627-32ce-821f-88b00e785263 | -9.42928 | -51.69014 | 2026-08-29 07:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f39fd27-be8a-336c-9b98-157d83e0f6c1 | -14.92332 | -56.33228 | 2026-08-29 07:14:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97df531c-2d93-3b6e-a51d-aa1781589e03 | -11.04073 | -57.22227 | 2026-08-29 07:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ea73905d-7739-3724-92d2-a1db04505e8e | -20.94782 | -57.57745 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 8c2af92e-551c-3db1-9616-4be7b7d4cfab | -20.94115 | -57.55043 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8f613e18-b20a-3b1a-bba5-4a8b84bbbdf0 | -20.92955 | -57.56769 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 61d37e69-946b-3fc6-922f-aa3f82a635a1 | -20.95801 | -57.56955 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 119fdbf0-4761-3364-9e93-f0b123d93988 | -19.2254 | -57.65784 | 2026-08-29 07:16:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e145f1ea-04e6-395d-a183-e5e705d2f192 | -20.93096 | -57.55833 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 27.7 |
| fc4b5f0c-08d4-36d6-bf7a-5e4149383040 | -20.95661 | -57.57891 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d4a25451-f3fa-341f-bec8-c71bd79d9589 | -20.9598 | -57.61783 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b7f081f6-009e-36ca-a635-a2dd5e9cf20d | -20.93975 | -57.5598 | 2026-08-29 07:16:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 35d19403-7127-3eae-8850-ad08bbd3c3e3 | -6.7699 | -55.6644 | 2026-08-29 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| d8a306eb-1b66-331f-9c0e-03adec6800a9 | -6.77 | -55.6445 | 2026-08-29 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6c115aa3-f645-30e2-9e97-51edb31d5319 | -10.4794 | -64.5012 | 2026-08-29 07:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b9cbde0e-82d8-3661-be46-58ceb8d26010 | -6.6315 | -43.7533 | 2026-08-29 07:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 130ebd0e-b98f-3bd5-9443-dd92ab1b8eed | -5.8895 | -57.7513 | 2026-08-29 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 073a7c29-adee-3d3f-a32d-473454dd7339 | -5.8894 | -57.7708 | 2026-08-29 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f4bdca51-56ae-3712-914d-1185bd31d9fc | -6.8069 | -55.6626 | 2026-08-29 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f9b6ad21-356d-38fd-ad87-0dec83734f73 | -6.7885 | -55.6436 | 2026-08-29 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| c173b5c9-911d-3892-a4fc-f440ed066833 | -6.7884 | -55.6635 | 2026-08-29 07:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 255.0 |
| 597ae850-5f1c-3e9d-bc99-cecbf014643f | -6.6317 | -43.73 | 2026-08-29 07:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 546321d0-797b-3a25-838e-1631ade7e752 | -6.7699 | -55.6644 | 2026-08-29 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4cc09612-9cb4-333c-ad11-cc2d58136d80 | -6.77 | -55.6445 | 2026-08-29 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9c60b904-58e8-3030-be20-36c60e7c0243 | -6.6315 | -43.7533 | 2026-08-29 07:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| d0ca7c11-1979-3b3a-a454-60166a9e182c | -10.4795 | -64.4824 | 2026-08-29 07:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f3e9e2c4-d48e-352c-a43f-3ae77e35cf00 | -6.6317 | -43.73 | 2026-08-29 07:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| bdca2e84-c0d0-3f6d-b981-3b7936bfe5ac | -6.7885 | -55.6436 | 2026-08-29 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b946bd99-85c4-355a-b066-7f87ec35a4b8 | -5.8895 | -57.7513 | 2026-08-29 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7e09188e-e2a3-30df-9ec3-af96f969e717 | -6.8069 | -55.6626 | 2026-08-29 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |


[Clique aqui para ver as próximas entradas](README74.md)
