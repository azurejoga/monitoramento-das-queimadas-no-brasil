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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 136b76d2-223e-34ea-ae2b-a876b6910aad | -16.01373 | -50.93363 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b25e800-904b-3d60-bd38-274b25b25bd2 | -11.56235 | -47.6847 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba984d7c-2596-364f-9ef5-ac2bb0b44d3e | -14.91476 | -46.89497 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fec85c1-a1bc-3228-b777-5363d0aa7b64 | -10.05261 | -54.32757 | 2025-10-04 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60e8510b-4cfb-3e52-9772-f1714efe5a48 | -10.61257 | -48.72658 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e0bd4d0e-c2d7-3ffd-85e9-0c0e503bab8d | -11.49939 | -46.76176 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8d60d41-d5c2-30f3-972c-00d4e22c3c55 | -13.18333 | -50.93421 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| fc4ca0c7-cc2c-3012-9248-6ee9fa29bcfb | -11.92559 | -46.40585 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1859039f-2d47-3ff0-b0c1-7b1c5e6111b4 | -11.92694 | -46.39412 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9f42c2ee-f69c-3c1e-9c21-25a20473589d | -10.33288 | -50.32978 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19c6b6fe-f9aa-3d51-b82a-69f7f7e2ee1d | -13.14458 | -47.93163 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9531e78e-1ebb-30ef-af1a-6fcceb6cf5d6 | -16.16931 | -57.57887 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 41d996e0-c7a6-33cb-a25b-489d5c1cc487 | -21.60023 | -45.28941 | 2025-10-04 05:08:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 869f3798-c4d5-3b5a-b607-682352870015 | -18.18751 | -53.35192 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c33852a-d671-3019-9619-a748f0f61833 | -17.16964 | -47.04001 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb7cf704-938f-3480-bdac-decabd4d0dc2 | -17.07863 | -46.2499 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 100b98b9-e7a3-34bf-a18b-f6ec62b01e29 | -21.2 | -45.14297 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 87d2e923-4614-32b4-ac31-33f7afd1aa7e | -18.17225 | -53.34312 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15e5bc0b-f6e9-30a2-959a-d5b30b69c2cb | -18.19868 | -53.36074 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5057489e-9029-3469-96d3-2e07ec7c4c5b | -16.36388 | -51.47368 | 2025-10-04 05:08:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03f92939-a5ec-3455-ba8b-0ae1f0c7396b | -17.15203 | -47.03382 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52f4aba9-7a81-3c3e-91e7-dd6ac7b93ac8 | -17.64078 | -44.45608 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95397acd-1ab9-3d6e-bcde-b40d9c7748c1 | -20.3 | -46.73116 | 2025-10-04 05:08:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e27687f-ea08-3e0e-8b6f-147e7f72a9ee | -15.97247 | -57.24448 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14e3786b-c04d-37fc-a56f-e912d27add7e | -18.2308 | -53.36579 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d360a8a5-f9d3-30bc-945f-480ff4436a0d | -18.16292 | -53.31951 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee155258-a423-3ab9-a9cf-057e66918012 | -17.99188 | -45.00848 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b97cc158-60ab-3c7b-90ef-e0cbf4a8efc0 | -18.23428 | -53.3705 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d5b4e69-4a2f-3e4c-9bff-d33f536cd2da | -15.96693 | -57.2362 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e9c2ac3-1f47-31fe-b8c7-d22e365910d9 | -16.9447 | -52.67136 | 2025-10-04 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 654ccafa-5fcd-39b1-935e-8c3beca10fc3 | -17.15587 | -47.02966 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e18fd966-a621-30ea-ae0e-2d9c37da4fec | -18.1794 | -53.35135 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea624b0c-4b25-3912-8769-7477d6fb4a10 | -17.15675 | -47.04774 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fabc4477-cfe2-3401-b6ac-a33e43faa62a | -17.1601 | -47.04748 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5bf2c29-2315-3e80-a5a5-5f238bfff80a | -21.69055 | -50.07267 | 2025-10-04 05:08:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a350e866-d826-3479-bbfb-88d8d3572569 | -17.15499 | -47.03816 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b09db469-74a3-397d-862e-8b693c6f7732 | -16.39556 | -52.1587 | 2025-10-04 05:08:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca48b003-7fa7-33ce-b596-60900e285da9 | -17.14989 | -47.02882 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0c5586f-7097-3b7c-ba24-aa682464f2c0 | -21.68077 | -50.06473 | 2025-10-04 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1953a617-d05b-3caf-b709-c920c5530a32 | -17.30171 | -50.58826 | 2025-10-04 05:08:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3dc14d5f-9a87-3add-a0a6-ab4cf1d23705 | -18.23128 | -53.36209 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a9cf69f-52fd-365d-ba53-b3418493dde1 | -17.99007 | -45.01126 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20a2ba70-273e-32c9-9e90-5c8f94f77c0a | -18.23687 | -53.38204 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46bb35ff-ae18-38be-bd5d-e776137adec0 | -21.68044 | -50.068 | 2025-10-04 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 48ed9924-e89a-30ff-945d-33c84dcc5d5e | -18.20316 | -53.35774 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc894e71-5fd4-37bc-9f6e-4d534d8374d4 | -17.1572 | -47.04308 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f68cc1f6-0d46-3b34-8963-e30d901c4c69 | -17.52842 | -52.53134 | 2025-10-04 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f9035eb-a719-3069-adfc-2f5f00a6b6cc | -20.47363 | -44.8203 | 2025-10-04 05:08:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 57225b3a-f1ad-3f4a-9cc6-5ac6d36488bb | -16.93927 | -52.66902 | 2025-10-04 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f38ba39-99b3-30dc-9d1a-557e0dae9a64 | -17.70456 | -56.76641 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cedfb026-e70f-3258-a1cb-61b86e1a5e4f | -16.16435 | -57.58904 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ec161e08-cad1-3aec-af76-ae4a648bdeaa | -18.17532 | -53.35124 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8498dbd-8b08-3bd0-9b03-5810d158230a | -17.58209 | -44.4963 | 2025-10-04 05:08:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 658af4a7-9d45-3f77-9670-bb866b2285a3 | -21.68109 | -50.06143 | 2025-10-04 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6eed3124-29a5-3471-948c-213e66aa03b8 | -18.17632 | -53.3433 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd6d97d-b879-332a-bc74-a0c2b3945513 | -17.69898 | -47.09365 | 2025-10-04 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b3cd650-2601-3fd8-acee-69633a1bb24c | -18.23382 | -53.37405 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d277e339-77a1-3c1c-82d2-252a34733a4b | -17.71018 | -56.75176 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b8b8d506-5b75-375e-af3e-11e148b8581d | -21.68567 | -50.06855 | 2025-10-04 05:08:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b9da96e1-e469-318f-90ef-4031305f3968 | -18.18252 | -53.35899 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d703917-69a7-30d6-8b44-6a2ab516e94d | -22.28802 | -46.75589 | 2025-10-04 05:08:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8450622f-4170-3393-83f1-2996c80031cd | -15.96307 | -57.23921 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8815e086-bf3e-3cf7-8d94-6992b4bf19a0 | -21.72348 | -50.74887 | 2025-10-04 05:08:00 | NOAA-21 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 1d110563-5ddf-31b6-9be0-a2f5f7e3e414 | -17.15845 | -47.03017 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d791f1f3-7ba2-3aa6-a458-c7c71a9adf99 | -20.47853 | -44.82055 | 2025-10-04 05:08:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ca39380c-5940-3f12-9c82-dce8a59c5107 | -17.55681 | -46.75924 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e724e298-07a8-38ae-8a66-e408becfdd3e | -17.08012 | -46.23445 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0ad6fb2-656f-34c6-ae18-f2f6a9ca21f2 | -17.58349 | -44.46368 | 2025-10-04 05:08:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 646f2962-3b6c-3fb6-864f-54e9fe896411 | -20.47312 | -44.82718 | 2025-10-04 05:08:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9480a4a5-621c-3b50-90ca-87ec64110258 | -16.39038 | -52.16558 | 2025-10-04 05:08:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bf6332a6-b994-3aee-819c-9344f13cc550 | -17.15161 | -47.0382 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a0522e8-fb2e-38ae-9e2d-167cba8392ab | -18.63438 | -50.67724 | 2025-10-04 05:08:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 730c1ab2-d84b-3a77-8ad3-b65a854f9406 | -16.15828 | -57.58435 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fcb44ca0-52c7-3615-adef-14ba9e2cc655 | -18.45574 | -49.44001 | 2025-10-04 05:08:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b2982b0-9523-377f-a4d1-65594f2720d2 | -18.19892 | -53.29475 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0794e9e-b047-35f3-b1f1-4eafe517dd41 | -17.94762 | -47.02452 | 2025-10-04 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 52eb0cd7-5a85-3a3a-9b0e-8e19ef8eefdc | -20.14246 | -46.41663 | 2025-10-04 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 74907c73-560b-3fb0-96c3-6871beb86273 | -17.08592 | -46.24032 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfa53e9e-39a5-379e-979b-8a1ad6e2f147 | -18.23638 | -53.38574 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d45bd37-dadd-3cfb-8e7e-5ad77b11e63f | -15.96915 | -57.24393 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 042a9b2e-7c01-348a-929e-0c712d0575e3 | -20.47145 | -44.82001 | 2025-10-04 05:08:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dd4c7e33-cd56-34da-8b36-e3e3ff8fe5fb | -17.17005 | -47.03574 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db9a5234-dfc2-3a30-8f26-0791df2b12b3 | -16.39135 | -52.15783 | 2025-10-04 05:08:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b70b909-2c16-3692-b7cd-cf74f3251834 | -18.14458 | -51.04803 | 2025-10-04 05:08:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f74b067-7a17-3b27-9b81-f38f3f25394f | -20.14344 | -46.42052 | 2025-10-04 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9d9d87f-a9fe-35e4-89b0-c71c7d067aef | -17.70544 | -47.0897 | 2025-10-04 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bfb5b45-0419-3fe5-b52a-59fb9204f5e2 | -18.46063 | -49.44379 | 2025-10-04 05:08:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f1a7e1a-4e44-37f3-8fc1-62d379f9a8e5 | -19.57961 | -48.01989 | 2025-10-04 05:08:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d370b92d-2354-3f28-8d23-1b5c0ad6ce73 | -18.23825 | -53.37151 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d18e46cf-8559-3454-8745-e0a07c774ba8 | -16.35942 | -51.47329 | 2025-10-04 05:08:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae8fa7f1-3d2a-31c4-8be5-7e1e58847b4a | -17.70795 | -56.76695 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c8b0a579-b0ca-31a0-937e-cce5a27c9ff4 | -17.72432 | -56.77349 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| aaae9577-42dc-30e9-b5db-30662773ed16 | -17.705 | -47.09429 | 2025-10-04 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f873c5e9-5cc7-37d4-98bb-1bb15041db97 | -17.15406 | -47.04718 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34e7f39f-12b7-3ec2-a80d-1fec41405b72 | -18.27568 | -45.90334 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03da09e1-97fa-3413-82d6-d0c51d48c581 | -16.17262 | -57.57939 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 283a9fd8-80af-3390-aa15-c4dcd7eb0813 | -15.96969 | -57.24037 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9828cfb8-fb92-3c52-a133-e88597277b9f | -21.19363 | -45.15146 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c3734c17-4d42-3702-9746-4a990bfe4522 | -18.23779 | -53.37497 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1671c0d-b072-33c6-b451-413dc71a3ccb | -16.36442 | -51.46923 | 2025-10-04 05:08:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README125.md)
