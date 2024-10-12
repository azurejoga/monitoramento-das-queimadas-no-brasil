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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e84ab664-fc1b-3ee3-a58f-0f084452c0a4 | -13.26242 | -53.74923 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4006df81-a42a-3e88-a99d-453a335ecc2a | -13.26186 | -53.75304 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8ae954d-6360-3502-b131-7fdea221d8e3 | -13.2613 | -53.75685 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d642d008-11c5-3f05-927d-7e957b96c1e2 | -13.04181 | -53.65344 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13875ce0-5cf8-3f5a-ad21-c46370501644 | -13.04125 | -53.65723 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb7a67a2-994d-3aac-a451-ebf68fdaf991 | -13.03782 | -53.65671 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0cd2ef-4274-3960-95af-beee7fabed1d | -13.03726 | -53.6605 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63925344-065d-3cbe-8133-255139abaa60 | -13.03439 | -53.65618 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2fd0a2d-ef63-3b1c-ada1-0295ee106fea | -13.03439 | -53.63371 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66603a9c-697c-33bf-9ba2-b1c436b33bfc | -13.03383 | -53.65997 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1ceeded-8285-3a48-9798-d8319aef2311 | -13.03154 | -53.62934 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a94c656c-6246-393c-915f-08d9a1df4cb4 | -13.03094 | -53.65659 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99815b9b-6693-32a2-ab8b-c4eb1bfdde12 | -13.0304 | -53.65944 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1625186-fbf3-33aa-b209-7badf77e5c78 | -13.03037 | -53.66037 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c95d479-a4bd-3695-b9c3-56f16210a5fb | -13.02753 | -53.63263 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b36c9d4-6d97-3398-aef0-2254e5a68d40 | -13.02467 | -53.62826 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b20aa4e5-4e67-3ed3-9fef-c2e0530b002a | -13.0241 | -53.6321 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37af7cc9-9282-336f-84af-c548676d322d | -13.02067 | -53.63156 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62d2b42b-1769-389a-a17b-351613f97653 | -13.01723 | -53.63102 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e94f2a09-bd33-3ee6-968a-64c72aae1c5e | -13.01666 | -53.63485 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50aef7a3-85da-394c-a3a3-3f25ce9b6d25 | -13.0138 | -53.63049 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9ddcba5-e861-36be-96ec-e9b6ed6eb477 | -13.01323 | -53.63431 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| add62c80-626a-3d2a-949f-1fe7754ddc57 | -13.01095 | -53.67289 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d2e2d7e-e0a9-343b-8974-49dea10b2c24 | -13.01038 | -53.67669 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc7ee64f-c709-38dc-b567-4239244a188e | -13.00981 | -53.68048 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f11a68-6dda-3a48-b8d4-26a3867690e6 | -13.0098 | -53.63378 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e598a735-86d4-3fc7-ad33-87840d70fb2d | -13.00923 | -53.6376 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1af4641-4137-3684-ac2e-987b219e8599 | -13.00637 | -53.63324 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c77261ca-9fb8-39ea-8653-4f643270ccca | -13.00582 | -53.68375 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dadcdd9a-a01c-3c5e-b43a-10f043dfb82c | -13.0058 | -53.63707 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f7d729-f662-33df-9c76-fed6fbb1d16b | -13.00353 | -53.67564 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7dfb90c-959d-3a76-818f-0ed52acb0ea7 | -13.00351 | -53.62888 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4870adf5-1163-3968-8bb4-90cf88148f49 | -13.00296 | -53.67943 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5337f5d-5ff5-3f40-89d5-38c060699d73 | -13.00294 | -53.63271 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52ca05f8-fd42-30b0-8016-a64afa90f631 | -13.00239 | -53.68322 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60f3dfa8-8c58-3f81-9d62-d0af23e2cd5e | -13.00237 | -53.63653 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a799e1-bac9-3ab5-990e-a8bc8f74e31f | -13.00067 | -53.67131 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 529b1f91-3da0-3ed1-ad6f-3295def101f9 | -13.0001 | -53.6751 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60eec6ed-954c-3638-9435-9296e22e0598 | -13.00008 | -53.62835 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c049432b-6f60-3497-a787-873d7f49d71e | -12.99951 | -53.63218 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ee31be8-8025-3d3e-9b2d-6f0e9ede0b69 | -12.99893 | -53.63599 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 763ec787-6be2-3f2a-b99c-4c30ba531430 | -12.99836 | -53.63981 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd990b1e-6205-35e5-a505-a690a304256a | -12.99607 | -53.63164 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c123eb6-436d-3e86-b2d2-543a3ca2847d | -12.9955 | -53.63546 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f350c7c9-fea6-3271-affd-571f8fe67f50 | -12.8838 | -54.0336 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 929a2581-c2df-36ed-a11a-9c39e2b897a4 | -12.88325 | -54.03731 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ddb08e3-6136-3901-94f2-d3eba57d5e7b | -12.8827 | -54.04102 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec4d5791-3476-34f1-8ca9-e95aa7923191 | -14.45435 | -53.64116 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 416243ae-7796-3e23-b419-d44e1acab86c | -14.45378 | -53.64514 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2d5e4d7-7136-3430-8051-462a715ab6a3 | -14.80164 | -53.95274 | 2024-10-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e0b1638-de69-3e78-80ed-fad72f586cae | -9.2786 | -54.58128 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 808d7ee4-a57e-30ea-854c-c58f345f0317 | -8.90259 | -54.74506 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 986590e4-f3e8-31f9-ba4f-b5262e35ef74 | -8.89843 | -54.57747 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 700899c1-68fd-350a-8660-4fe2eca21c66 | -8.8574 | -54.68815 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c603210-0bc4-3396-8328-cdccfff6e9a4 | -8.85523 | -54.68075 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9367689-3047-3268-b478-0331cd70d67e | -8.85469 | -54.68422 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35b5b104-9033-3867-adac-b5ed8638ccbe | -8.7629 | -54.74778 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f80a6b0-adac-32cd-96af-8bc358291b01 | -8.70624 | -54.84534 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e6faafb-13b6-3137-b52f-536c8359561d | -8.70294 | -54.84483 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6101118-9bf8-3441-8893-fbfb23272ef5 | -8.7024 | -54.8483 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89ced364-4454-36be-92c3-f66e1c1f9fad | -8.70019 | -54.84085 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7f9d51a-3410-3ff0-bb4e-779e139e1d28 | -8.69964 | -54.84431 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3ebc177-a577-3d44-9cbf-e6a84bfede6c | -8.69689 | -54.84033 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8af83d8c-5b16-3481-8250-38cb6a360320 | -8.69468 | -54.83289 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb76964-57c3-32c6-835e-01550b9da13b | -8.69413 | -54.83635 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56f018f-e61e-3021-9e1e-2a0f0dc15b9a | -8.619 | -54.60017 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 547d8698-41a5-351f-8c10-a649478204c7 | -8.41944 | -54.70349 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94456ae3-c874-37a9-a29c-f8ba8ffc0b51 | -9.8286 | -54.54445 | 2024-10-12 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cedec6a0-3fd3-3a82-963c-906e133a2440 | -9.82584 | -54.54043 | 2024-10-12 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82725d61-ced3-3e4d-b503-4caface648c8 | -9.82529 | -54.54392 | 2024-10-12 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54f247ea-e673-34ec-ab65-540289dd98cf | -9.45842 | -54.5424 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b761b91-b112-3792-9238-2e45b186f0d1 | -10.68779 | -54.46583 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be3574cc-8c64-3308-8d72-5c5bf8f053f8 | -10.68447 | -54.4653 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2bfe788-de17-3178-adf2-bc78c273047b | -10.68116 | -54.46478 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f50ac8-b9be-312e-9da2-3783393a68db | -10.59079 | -55.06703 | 2024-10-12 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d249f507-6682-3f33-8385-ecc6a68716d2 | -10.59024 | -55.07052 | 2024-10-12 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 467b8bb8-9195-3328-a9d9-5c8852e20e1e | -10.32006 | -54.20505 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86de7e07-7def-3f1f-871f-9d8de10276cd | -10.31673 | -54.20453 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2c628a2-3512-3049-9a2b-5bc5d42fb6ad | -10.31619 | -54.20807 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3edff6cf-c767-30d2-89d2-d622babc5958 | -10.31286 | -54.20755 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91476533-43be-3ec5-9adb-39e47d30aada | -11.80825 | -55.13413 | 2024-10-12 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3a47084-9335-3278-998b-7cfcff0ffbc6 | -11.7291 | -54.79025 | 2024-10-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f83cda46-52fe-3aec-ba5d-4fd97926569c | -11.72634 | -54.78618 | 2024-10-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd9aa28d-829c-3bbb-82fa-7eddefc81399 | -11.72579 | -54.78971 | 2024-10-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 880b9962-e2c6-320f-b1d9-c1db7cf3fa08 | -11.72524 | -54.79324 | 2024-10-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acef1692-6f17-3a07-a391-bdc261829e04 | -11.7247 | -54.79677 | 2024-10-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbd4eb29-237f-3156-9f84-11a291b296da | -11.67365 | -54.68736 | 2024-10-12 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51b089dd-deb1-3d4b-ba94-a008409c339b | -11.67033 | -54.68683 | 2024-10-12 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 981ed118-cb25-3fe6-8e20-0de1f21fbbb8 | -11.28411 | -54.58939 | 2024-10-12 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 224b98e2-3583-3476-bca6-acfdba226ceb | -11.2808 | -54.58887 | 2024-10-12 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f803f095-f0cf-3a61-8ccc-1ba2852b7116 | -11.28025 | -54.59239 | 2024-10-12 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ac3259a-f7ed-369b-8969-b26d18ddbd28 | -11.27924 | -54.22427 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d3b6f1e-4c40-346c-a06c-1ce74ddb439c | -11.27748 | -54.58834 | 2024-10-12 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ee58e8d-e6a3-3a53-97a6-83bf23a5e10f | -11.27645 | -54.22015 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f83aaec6-2fb4-35b0-bcb4-9b810187181f | -11.2759 | -54.22374 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fd1ae11-fc80-3142-aeb0-006a3f74a626 | -11.2313 | -54.1801 | 2024-10-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d61eb98-f332-32ba-a369-dedbfbb31759 | -11.19391 | -54.75489 | 2024-10-12 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d19b436-f6aa-30d9-a002-6c5be1c9b2c9 | -12.64538 | -54.71383 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6f62fcb-82fd-3aeb-9238-8fac49ad5508 | -12.61628 | -55.21073 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16906821-b7cb-3bd2-b5ca-8cd7b85cf7d9 | -12.61573 | -55.21426 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README75.md)
