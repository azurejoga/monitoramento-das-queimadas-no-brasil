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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a4df710-d6fc-3197-8f5a-9ad6a5c03e43 | -25.79753 | -49.37917 | 2026-02-07 04:38:00 | NPP-375D | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d303f167-31c0-3aa7-8daa-81b0c5db6ec9 | 4.97423 | -60.32051 | 2026-02-07 04:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 972114f4-5659-3e92-8581-1e3928bce91a | 4.25765 | -59.84376 | 2026-02-07 04:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b6e235-4434-34c6-98ba-fda077d030e6 | 4.26256 | -59.83911 | 2026-02-07 04:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2206c835-672e-3e13-8f87-91b2d46f167b | 1.60543 | -61.02855 | 2026-02-07 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d08d838-a537-34ab-a669-fd9b0a6e8ee8 | -11.88793 | -40.95197 | 2026-02-07 04:53:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c99aa6a0-0788-3020-9e2e-7ec7f5822e25 | 2.1855 | -61.92545 | 2026-02-07 04:53:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dae9435-0072-3cdc-aa34-a9d742ad9d48 | -12.92168 | -49.48431 | 2026-02-07 04:53:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d480549-f9bf-3091-b214-ce30dd58b391 | 2.19089 | -61.91985 | 2026-02-07 04:53:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3ef6c51-85e7-33e8-bab8-ca536772f340 | -12.91773 | -49.48372 | 2026-02-07 04:53:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ede4d446-89bb-3bbc-a542-6e369311eabd | -11.96644 | -44.51916 | 2026-02-07 04:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0fd000-02d3-3675-ba07-2f38f27b48ec | -1.66627 | -45.80107 | 2026-02-07 04:53:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed298368-cf4b-3431-8644-cdd18a8f5500 | -1.45665 | -46.08884 | 2026-02-07 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9135507-0e14-3e5e-b678-62e56d621693 | -1.45606 | -46.09263 | 2026-02-07 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bea161d-fb04-3f78-8277-d5de654832d1 | -10.93921 | -44.88593 | 2026-02-07 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49706cf5-ceb1-3dc6-b55d-4b6d275db7f1 | 2.18622 | -61.93024 | 2026-02-07 04:53:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a24b5c28-c65e-3ba5-aacf-ac997dfbd3aa | -1.66956 | -45.80106 | 2026-02-07 04:53:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 879539b6-0e64-3cf7-ae96-4ec726622f87 | -18.96994 | -52.93126 | 2026-02-07 04:55:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c9c1881-cf65-351e-80de-f26320dea45d | -15.89478 | -58.28052 | 2026-02-07 04:55:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6c3ea92-a083-3780-8239-9b78a330ed8c | -15.42599 | -41.43619 | 2026-02-07 04:55:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ad82eb03-4072-37eb-97fc-eff153b7bf3c | -18.97347 | -52.93181 | 2026-02-07 04:55:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0e3cd53-49c4-3961-ae33-3daaa0461a23 | -15.56626 | -58.84199 | 2026-02-07 04:55:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b498c9ba-09b9-336f-814e-f233df67d481 | -15.4568 | -58.99784 | 2026-02-07 04:55:00 | NOAA-20 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ae2218c-ff50-39c5-bf20-1e426431cbee | -15.89117 | -58.27985 | 2026-02-07 04:55:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0be3bd7-8a24-35cc-87f3-a49e1dba780d | -16.28983 | -40.77807 | 2026-02-07 04:55:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4de800c5-90c0-328f-b68c-efcd7c1f5fdc | -15.89193 | -58.27552 | 2026-02-07 04:55:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d24591d-54c6-33bc-927a-3e55e736b342 | -20.72323 | -55.15842 | 2026-02-07 04:57:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd8eac06-f75b-326a-8a22-c10ce73c3b48 | -27.9513 | -50.93953 | 2026-02-07 04:57:00 | NOAA-20 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 07bb4342-49b9-3e5b-8604-27f3a33fd097 | -24.13872 | -51.64619 | 2026-02-07 04:57:00 | NOAA-20 | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9182329d-3276-3222-8f08-c8522a71299e | -22.02402 | -49.50408 | 2026-02-07 04:57:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 146afe82-dcf6-38e2-afca-67c70707fb00 | -25.79485 | -49.38072 | 2026-02-07 04:57:00 | NOAA-20 | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 917f1f0e-b3f7-359d-b870-bc409129595e | -26.93721 | -52.48857 | 2026-02-07 04:57:00 | NOAA-20 | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1daa9392-98ff-3f24-8311-e3fb3ee65fc2 | -26.93496 | -52.48701 | 2026-02-07 04:57:00 | NOAA-20 | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b61d746f-b7c1-320c-b308-48e4b669f7ba | -24.03145 | -54.23507 | 2026-02-07 04:57:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 254624ad-baf1-3933-aec8-3abbc48db728 | -20.72657 | -55.15899 | 2026-02-07 04:57:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 457e7548-e84f-3623-9eb1-8af3dd56691d | -24.67522 | -51.05368 | 2026-02-07 04:57:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1e77476-7a23-3cae-bc48-b78a2dad38d0 | -22.7871 | -49.36113 | 2026-02-07 04:57:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192db1fe-a326-35a8-8bf3-51537220830a | 2.18082 | -61.92861 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d9fc0ca-c1eb-3d48-bf89-89d6128ccb82 | 4.25723 | -59.83653 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0130c900-a544-3cf0-9319-5a97d7d44217 | 3.34343 | -60.57183 | 2026-02-07 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2969e74c-c3a9-3e93-9179-331656aa50a2 | 4.26082 | -59.83589 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96300eb8-2d4f-3218-8c53-0b29682ef6df | 2.18363 | -61.9245 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79c2a41e-0f4f-3c28-8535-57fb11facab5 | 2.18026 | -61.92503 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6910c4-161e-39b7-a6a6-14dcb47ffc0f | 2.18924 | -61.91625 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c46ec531-5aa8-3608-96a4-af483fa39e79 | 3.15653 | -60.53922 | 2026-02-07 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f63bce67-eab6-370a-bf31-2fee039e79d8 | 2.19261 | -61.91571 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101cd1c2-dc0a-382d-b6dc-8457c730bf74 | 4.39801 | -60.53301 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24baaa33-3694-372f-a2a8-f611d3867566 | 4.19155 | -60.40413 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 060182fe-5537-3a73-97eb-e7a0617e480d | 2.28302 | -60.75084 | 2026-02-07 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fec292b-f051-3c9b-a44a-01839f3efb8b | 3.97891 | -59.59531 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d8ebb5a-920a-3bb0-bc5d-19aa90551b56 | 2.18307 | -61.92093 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f87b365-6883-31a8-80fc-7b257f91e8b8 | 4.24236 | -59.81255 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff616c9-c6e1-3a66-9125-816d5aa88f5c | 4.01833 | -60.04931 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e5741d5-43b2-3b90-9b4e-34abb748b8c6 | 2.18981 | -61.91985 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c25a4a-b7c2-3f35-8875-4d183929ff00 | 3.98253 | -59.59443 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34de531f-3b0e-394b-ae21-7d10ef8ede39 | 4.24595 | -59.8119 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec55cba2-e2b6-356c-8e11-ee94aa6cd0a7 | 4.25788 | -59.84064 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b136e645-e019-3f45-8857-2fff5dee6bcd | 4.01766 | -60.04512 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 620e0f4c-51a3-3458-9c3b-d9fdcc7bc9ea | 2.187 | -61.92398 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac9c069f-948c-3292-9c39-d8b778a13e7a | 4.02193 | -60.04893 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ef1307b-4a2b-3741-ae69-4f0a7ee6f55d | 2.18587 | -61.9168 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fec7211-fa37-31bf-9d69-13783191119c | 2.18419 | -61.92808 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abed9f87-60d1-313f-9938-8c917c779b73 | 3.96534 | -59.62763 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2622c398-88d5-39c2-bfda-0285a4a14fda | 2.18644 | -61.92039 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ffe4b0d-3e78-3a66-ae7c-60749504b56f | 4.96915 | -60.31992 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e99f220a-af56-34b2-88c8-e592e85c8e9e | 4.39577 | -60.54122 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e12a062-77ab-3de1-99b7-a299eb60deb1 | 2.19542 | -61.91158 | 2026-02-07 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3630dcdd-ca33-3abb-85f9-8fa8983298e9 | 3.97729 | -59.60865 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bbeeef33-6673-3f7e-b58d-00a535e12704 | 3.90948 | -60.86106 | 2026-02-07 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ff16d25-fe62-300b-a139-ae85690497d4 | 3.98614 | -59.5935 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d91c31e-8112-308c-a8fa-d6dd18934159 | 4.39639 | -60.54509 | 2026-02-07 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bbe10b3-1870-34ab-a94e-07ffc4f82c2f | 3.90603 | -60.86161 | 2026-02-07 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7dfaddad-21d4-37ba-b8fd-4d550d7d2a49 | 4.02126 | -60.04471 | 2026-02-07 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0003d1bf-9f55-33ac-ab02-2eae40ce2f79 | 3.31581 | -59.90546 | 2026-02-07 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 342abb8d-87b2-3269-a933-754f9f85dfd4 | 1.6038 | -61.02511 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdd2a751-1276-38d6-a745-07772c106ba4 | 1.60441 | -61.02903 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa200fcf-5adc-3869-954b-1e47976fd7c4 | -2.41857 | -55.47906 | 2026-02-07 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 02db67f4-9470-30ab-b88b-ff1eb07753b3 | 1.8345 | -60.85076 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c1fc5d-b67c-3250-939d-d7366ef5a738 | 1.35428 | -60.07547 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55854713-9922-3265-956f-38cfc5b7e51b | 1.35728 | -60.0705 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebc6f68a-334e-3e63-a71a-556e57426af6 | 1.3535 | -60.02174 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7ffc91-f9f8-3229-971c-a44eb9fe1b4e | 1.47844 | -60.91886 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0f47a62-8e88-378b-ad13-df91cbbf5c94 | 1.3536 | -60.07111 | 2026-02-07 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43ad710f-a6b5-3f4d-8bd8-eafedd26c58f | -15.89645 | -58.27543 | 2026-02-07 05:46:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0763fc0a-f182-3e66-be0c-a9da994b3b19 | -15.89074 | -58.27815 | 2026-02-07 05:46:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 939ca96f-3711-301e-a2ff-6f6e9a19e1be | -15.89113 | -58.27476 | 2026-02-07 05:46:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 463fd35f-fd2c-338f-832f-fa80a4b298f7 | -15.89606 | -58.27884 | 2026-02-07 05:46:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e50290d-d4aa-3467-9a2c-f57667ca8051 | -11.47695 | -46.53516 | 2026-02-07 06:03:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 128fe080-1e84-3f16-9f94-d6c41edb4098 | -11.48604 | -46.53661 | 2026-02-07 06:03:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b0e40671-ba26-3be7-9773-a7cd3ec8d60c | -18.97676 | -52.92891 | 2026-02-07 06:05:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f9410104-ea59-3945-8db2-cefb1dfbf4b1 | 3.91389 | -60.86052 | 2026-02-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7e42fe32-e8eb-3661-a197-b1cdb28fab78 | 3.98128 | -59.60975 | 2026-02-07 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a683673f-2f22-3c73-863a-6adda8d6efac | 4.39249 | -60.54624 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac5a1ddb-9141-361a-a623-cca73ff68a1c | 2.19441 | -61.91447 | 2026-02-07 06:09:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a83034a1-a68b-3d9a-822c-63b2df80505d | 4.39762 | -60.54222 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5923d43a-36df-3e0d-bbea-5790166c6c6c | 3.90937 | -60.8581 | 2026-02-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c690ea8-0898-3e25-b5db-22f92c1b5f80 | 4.3929 | -60.54596 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b45234d-6036-3e8a-a04b-9b03d9050e9d | 2.18145 | -61.92784 | 2026-02-07 06:09:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e90a6dcb-a95f-312a-936f-ec5d8ca94c40 | 4.26208 | -59.83487 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cba27e93-7db1-3493-9878-cff72eef73f4 | 1.60269 | -61.02707 | 2026-02-07 06:09:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
