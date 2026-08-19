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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea0a1019-0b3c-37e5-bd88-79f821cda7a8 | -6.14053 | -57.86358 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27e3565c-177d-3f6f-85df-86f0a9285400 | -6.14226 | -57.87596 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d21fdba5-3177-36c8-879c-70f7c81e8dc2 | -6.10049 | -57.86557 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95bca938-3ffa-3d8f-8d3b-2c8d498e5a64 | -17.56712 | -51.88203 | 2026-08-19 05:25:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ed7c88-c1e3-3317-af89-149c1f23429b | -15.31818 | -56.45697 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1068ff31-3652-3d12-8bcc-a5b61345b7e4 | -12.00548 | -55.5251 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2993d53b-f12d-36e6-ab82-a2aeba965d15 | -10.93792 | -57.10499 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb6cc67d-295a-3603-b119-f5a246ffaf5e | -6.44879 | -52.73163 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f399c9b7-e6d3-3771-963a-469b868cbe53 | -6.34814 | -54.9045 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f138d29-6b63-34b9-ae18-fa09f5089812 | -6.14519 | -57.88047 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2beb6352-977a-3b63-b897-ce6af9cee111 | -6.45213 | -52.7434 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 127f4754-8f9f-3b93-83ac-b9b87ba43245 | -6.35772 | -54.89796 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d13e5d4a-7fd2-3ddd-8af3-780e2d140226 | -15.98777 | -54.17283 | 2026-08-19 05:25:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8aff76f-7df5-3a68-8220-174b73a6b10c | -10.93812 | -57.10746 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4607f53-5f8f-3d72-bb39-8529d2be9631 | -15.31872 | -56.45285 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ec3c212-4e3c-3660-85eb-dd2d0b5fbd58 | -14.20336 | -52.89931 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc14d2e0-ade0-360a-9242-729486f33a3c | -6.13942 | -57.84707 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fd0ac54-4ede-3c8f-bbd8-463e9d5113d2 | -6.34393 | -54.90384 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3596fa16-5a6d-3ddb-a3a0-7887d5776ab5 | -6.44723 | -52.7427 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bef396e-a782-3bdf-8d47-2ccedeac52cf | -15.89226 | -55.57052 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77e27bdd-379b-3621-9a35-fa957a28eae6 | -6.09335 | -57.91319 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 75fc27ef-4d8b-3a0e-b93e-b3ed4ffe75cf | -5.4356 | -48.41325 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4101eccb-91b8-3ea9-adac-dc54c80a5e55 | -6.10376 | -57.69798 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e163019e-a1d1-39c6-a72f-c20252daeba3 | -5.14375 | -56.27906 | 2026-08-19 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d8f600a-c3a6-311b-8d47-ebcfe05020a9 | -16.32739 | -55.39137 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a97a4ab-805f-3203-a6b2-987dcdb7d154 | -6.02428 | -57.84292 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51279512-f05d-3ebd-a396-b529553b02ef | -15.31386 | -56.4563 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de4b14bb-b965-3064-836f-3f335dfe8258 | -15.77646 | -55.57076 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dddc64d0-a21e-3a53-ab28-ccd628af563c | -16.26618 | -57.66666 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 72da674b-4053-30a1-9b0d-9e50c23e1ee3 | -15.3144 | -56.45212 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae7aa051-b187-3d1f-87ec-410d3621ab8f | -11.6908 | -54.55694 | 2026-08-19 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39536646-6950-39f5-9ca1-11baef35df82 | -13.74519 | -57.61556 | 2026-08-19 05:25:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ec9eea7-f5ec-389d-af53-8e15f1f8e45b | -6.40706 | -54.94725 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6251ab4c-af93-3276-8a8f-7481938c335d | -19.76094 | -57.93226 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 87153db3-0b85-3b87-b82e-40cd0ef6fc21 | -19.77461 | -57.95865 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 4085212c-7505-301b-ad24-f12349216902 | -19.76828 | -57.94146 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c0b81c18-ad49-36dc-be26-69eec571d739 | -19.75376 | -57.9557 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 567cf9ac-860e-3a47-82a0-1ad093cd9167 | -19.75258 | -57.93108 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5617fddb-9b81-3407-81ee-6fc5b854dffb | -19.74473 | -57.92588 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 840d17dd-802e-314a-8cee-d9117bf61ef6 | -19.05559 | -57.34156 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c80928d1-de5d-31e4-a5e7-050c01fb5b83 | -19.77346 | -57.94547 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.1 |
| c6e97768-b418-3250-a65f-e6f537119311 | -19.0798 | -57.35787 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ab104a6-0808-3d4c-b96d-7063a027b2c7 | -19.76577 | -57.96147 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 921f33e8-9830-3e00-a8c5-ce71f1488838 | -19.76361 | -57.94487 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 0d22671d-4e65-3cb6-aec9-69dc122841fe | -19.7631 | -57.94888 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 114f1387-8f76-3d8a-89fe-7989063239d5 | -19.73956 | -57.93333 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6411ec7c-21de-359a-b3a3-826315888949 | -19.77668 | -57.95409 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| d7afc1f5-de35-3e46-8402-58e82201f58a | -19.77195 | -57.94606 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 5af63835-5239-3c61-b946-367e182ca1d0 | -19.73807 | -57.94535 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7668c4a9-6b86-398a-8523-aaf3d06578f8 | -19.07499 | -57.36153 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4abc9d99-683a-3ad3-839f-4f2292f219a2 | -19.07551 | -57.35728 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5377a0cd-f540-34a0-a6c9-2316e164862b | -19.77562 | -57.95065 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 0166ae21-8129-3bd3-b3c9-2c0d1a5eadb8 | -19.74741 | -57.93852 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| faa8c141-3221-36eb-90df-daac39b1abed | -19.77145 | -57.95006 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 9b7e4ce2-40f4-3b6a-a68b-d1f90f27323b | -19.05989 | -57.34216 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 122d332a-2c2c-3082-978c-25349ef4ffd0 | -19.74791 | -57.93451 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 6762df5d-345f-3f7f-bf24-bb51c5b562c2 | -19.77511 | -57.95465 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| c97105c0-fc31-39ec-9857-f8fc81afdeda | -19.75993 | -57.94028 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.6 |
| a60ad148-c042-3169-ae98-2b1d5fa4a7a0 | -19.05781 | -57.35916 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 75d83d37-4d14-310c-b43b-05c18fd1cbef | -19.77094 | -57.95406 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 1231cf6e-08e7-3dd3-8b2f-423903c2258d | -19.76527 | -57.96546 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 850dcf26-f7d7-30cc-835c-841ef3c5ea79 | -20.4704 | -54.53942 | 2026-08-19 05:27:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 442efeeb-6e0c-37b2-932b-6e1ffb596867 | -19.7616 | -57.96088 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 26392818-3cbd-3fe5-aec6-8386b5eb03eb | -19.74542 | -57.95453 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9f281d18-ae62-3894-969a-c10e6c87176b | -19.75308 | -57.92707 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 11231337-260b-3a67-8cb6-6fcb3ada350f | -19.74522 | -57.92188 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e6382cbc-71c2-3fec-a3cb-7c1fdb8f9b07 | -19.75326 | -57.9597 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 570ae8a0-c729-32cf-863c-9211bd1003ba | -19.74006 | -57.92931 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 19980823-6bef-30a2-a9e5-83d32ef15174 | -20.47081 | -54.53876 | 2026-08-19 05:27:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59c32e2f-1cd1-3c6b-a7bd-f4715841c3c9 | -21.53165 | -52.01369 | 2026-08-19 05:27:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 85969778-1199-3fb4-b383-ff3514eb4875 | -19.06211 | -57.35975 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 18825b0e-fb4a-3ffd-8e83-7b399ea730ec | -19.77251 | -57.95349 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 414fb0fe-fafa-3c59-b1cb-d547ed7647a2 | -19.74891 | -57.92648 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 409a6db9-f8ae-3ea0-bb3b-359767754483 | -19.7494 | -57.92246 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f93b2e7b-d8c5-3dfe-b5e9-59eac76159b5 | -19.74125 | -57.95395 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 843ebf10-e043-3781-9a0e-bdaca4c2c502 | -21.52585 | -52.00784 | 2026-08-19 05:27:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| ed297ad5-5dee-3296-a34b-28ef8579eaa6 | -21.52628 | -52.00267 | 2026-08-19 05:27:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 65030496-a1fb-3864-9f43-9b6c8bfad277 | -19.07069 | -57.36094 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a3f299ec-17d7-3848-84fd-bacf33c59d64 | -19.75526 | -57.9437 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7e2fb599-3b93-3d0b-a02d-901e7e073ddc | -21.53208 | -52.00853 | 2026-08-19 05:27:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 2d83da2f-be0b-3ad7-8799-c6529a050e6f | -19.73588 | -57.92873 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e7630584-b968-30c5-82d2-37e2cdce821d | -19.75358 | -57.92304 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 12068ab7-0ec8-3367-9118-1ee7302dfa8a | -19.75159 | -57.93911 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.2 |
| bcc3fda3-c8bf-34c0-866f-d7c03b3edcb7 | -19.75676 | -57.93167 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 579608e1-225d-39dd-a274-ff291caadb6a | -19.74959 | -57.95512 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e80d7a6-9396-339b-b840-9ca3ef5c6c5a | -19.77299 | -57.94948 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.1 |
| a039b786-e87e-34cc-bca0-e30431f62477 | -19.75208 | -57.9351 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.2 |
| c66a6184-d2c1-316d-b0ea-8636099b9f7e | -19.76461 | -57.93686 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.6 |
| df12d4c7-9d44-38a8-8fac-784bbd05d29f | -19.7317 | -57.92814 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9f117474-6056-364d-9015-d748f5a86c81 | -19.77621 | -57.9581 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 5a3d2b3d-87b2-3b51-9128-73366800b312 | -19.75943 | -57.94429 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 580224aa-630e-3b0c-be63-060ff61cccbb | -19.74691 | -57.94252 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 406ed3c4-2d3f-30aa-92f6-eb869d1cf185 | -19.75893 | -57.9483 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| b1435183-d7e1-3cda-8ffb-8bd96e545c50 | -19.0664 | -57.36034 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| bf215fa6-da10-3d15-9285-d28c84c7cc5e | -19.74373 | -57.93392 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 044efad8-2fa7-366a-b60c-0e2654a46188 | -19.7339 | -57.94476 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 461df7de-9ab8-3564-ba82-e448c132dc9f | -19.73906 | -57.93734 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2b052143-ceb2-332f-a6cf-cd16a3d58158 | -19.74324 | -57.93793 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 3ceec80b-0745-37b9-ad57-e16d78ddc87f | -19.07122 | -57.35669 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1911c60d-f6c0-3e9d-88fd-3b7fb42bb0d4 | -19.74841 | -57.9305 | 2026-08-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |


[Clique aqui para ver as próximas entradas](README63.md)
