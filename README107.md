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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d0c7dd7-7b32-38fd-b3e4-170d2dc59a55 | -10.41103 | -50.99434 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfd2c0a8-314a-3843-a2e0-7e5c79cae37b | -10.41047 | -50.99786 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 964b03df-208b-3289-8380-7a8ec6c8d154 | -10.40771 | -50.9938 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd2cf804-b370-3ebd-9f9f-a55d9aef9318 | -10.40715 | -50.99732 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d771a4f2-9376-3402-ad43-8a654e6e4916 | -10.40439 | -50.99325 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1d0a661-6a47-3796-92ad-bba0a60b4dab | -10.40383 | -50.99678 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1edc9a5d-de3f-3d6a-8818-093880731b51 | -10.40051 | -50.99623 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12436730-956b-3ace-b750-caf353110cb3 | -11.36069 | -50.81293 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d039cde-8719-39dc-943e-6c8d27140bfa | -11.24579 | -51.25692 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c99a6bec-ebf2-3276-9a33-2ee2c84f2824 | -11.24085 | -51.2452 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 528ff300-8f4d-3e55-bb37-ba5bcd1d2fac | -11.23809 | -51.24111 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 371adb96-317c-34d5-a317-e3af74a2bbf3 | -11.23477 | -51.24056 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 547b58a7-c188-3077-a8c2-3133470f9e4b | -11.23094 | -51.13808 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a19ca02-4eb3-3574-be6e-b596952889ff | -11.23038 | -51.14161 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 642ee74a-a442-3755-af62-b1594f2ccbd5 | -11.22982 | -51.14515 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13312c39-a9a2-3197-a104-c8a50b63116b | -11.22926 | -51.14868 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9cd240e-5919-328f-90fc-a9567759e561 | -11.22762 | -51.13754 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7ec817c-ab58-3469-8518-7d6cc11bdd8e | -11.22706 | -51.14107 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 080d1d68-4c4c-35a9-a231-4dea024c56c6 | -11.22696 | -51.18458 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8d53483-6699-3095-b66d-98259dc6c66f | -11.22578 | -51.21345 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d756b166-d40c-3939-96e4-eac5c8e44b0e | -11.22522 | -51.21699 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7e1db9-a04f-3fe7-ba65-56f6b5ff99a9 | -11.2219 | -51.21645 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63592dff-b505-3069-b0f9-53458a2ee4fd | -11.2197 | -51.20882 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4519733-a399-3188-bafb-af8e2d88854f | -11.21914 | -51.21236 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf53ea8-9666-33d2-a08f-fa90ba87d7a1 | -11.21581 | -51.21182 | 2024-10-05 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90e78587-9b40-353f-9aa0-a6c5b0f2dda3 | -11.07855 | -51.45581 | 2024-10-05 04:38:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 858d5937-8623-3081-b412-223ac5c80365 | -11.99269 | -51.90112 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038e5df3-9b98-30d6-abab-1dba416a33c8 | -11.98876 | -51.90416 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5627dda7-7c89-3034-a6c3-af452f5a9fc4 | -11.98482 | -51.90721 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 950f81c9-0048-3d1f-88a8-4b690cde0c19 | -11.98147 | -51.90664 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea15214a-d81d-3f57-8ece-31e02e61277e | -11.97812 | -51.90607 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbaa9d28-2018-3a1a-969f-f7721c4bddaf | -11.97476 | -51.9055 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00768e64-8859-3c76-a990-c4cf7e4dc385 | -11.97083 | -51.90856 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f3e83a6-f109-3e5e-b3c9-49993ce329f3 | -11.95858 | -51.89908 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01540b99-d1ba-3bb4-82fd-4ee18719f415 | -11.95522 | -51.89853 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3392b1ed-4133-34aa-a59e-6135624a6af0 | -11.95303 | -51.89073 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec90b18a-d3a1-3fc2-8235-2a733ea589c9 | -11.95245 | -51.89435 | 2024-10-05 04:38:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1551679e-5fb0-36b4-afff-b6dad9fb2d6c | -12.73577 | -51.97161 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bdb21d0-a1f7-3092-ac89-0dc0fd8f85af | -12.73519 | -51.97523 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4b4a92b-1d31-3587-b1b6-1aff49bc4b30 | -12.73461 | -51.97886 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4cdc8e0-6b8b-3181-8cf8-b6d60c611578 | -12.73403 | -51.98247 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4d214ca-7b59-3e46-ba3a-2766da5a6b22 | -12.7301 | -51.98552 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40cd0aea-90a8-3310-8f23-ca47599fb956 | -12.72675 | -51.98497 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fcc61fe-8b9a-35ed-aef9-363928a2b481 | -12.72617 | -51.98858 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4805d379-75ae-3e44-ad54-87bcd22b5d91 | -12.93481 | -51.46856 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c10b01d4-af75-37de-a14b-869af1c2e23e | -13.15643 | -51.20718 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d618f81f-d7fc-3a4e-b8e3-76668df9781d | -6.07479 | -52.46456 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31166c0f-ba67-3be0-a4b9-a68be1c44f05 | -9.36499 | -52.51179 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 119bb625-1e13-3304-af5c-66239de5679e | -9.34977 | -52.51719 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d9d933-c09d-36f4-ae7a-84c4e62b278c | -9.34525 | -52.54482 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c853708-7df3-3bbf-95cc-31d4c40bc289 | -9.34178 | -52.54412 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6734e02-de69-30ff-a983-bca8aa35d038 | -9.07295 | -53.24495 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fa60d0d-8ba1-38f3-a4ec-9359cf25c6ec | -9.07225 | -53.24916 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4c518f-afaf-3edd-a366-50438d7841fd | -9.06933 | -53.24434 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c164bb34-81d7-3efa-8ab1-03196ac262ff | -9.06237 | -52.96589 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65c5c000-d176-382f-b95e-d75ee3e8f7e5 | -9.0617 | -52.96995 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b28b5b3b-af95-3170-a325-e688925a9118 | -9.06036 | -52.9781 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1b5048d-0d23-3248-99fb-b564e1ae2d9a | -9.05968 | -52.98225 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 647d5359-848e-3aac-9739-b2a6bd5f5ef9 | -9.05611 | -52.98159 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 597b5685-5dca-34c5-8afe-550a00fb20b4 | -9.05253 | -52.98101 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 877f9b3f-1725-3297-8f89-969c238e30a5 | -8.97421 | -52.81782 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c17bea7b-4c2c-3f8b-afce-3e5d7dd452b4 | -8.97355 | -52.82189 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 019552f7-723d-3a3f-8a69-9493160eabf4 | -8.97047 | -52.7962 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f3b2fff-cbe8-3f2c-8d49-2efa4bf45f0d | -8.97 | -52.82126 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afaae85d-ccfc-3ed9-89e6-c43117b6ed1e | -8.96979 | -52.80036 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 820c4929-a481-3f77-b15c-afdac57e59c4 | -8.96911 | -52.80447 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e9f52e9-c968-3415-af22-3e778788b8fc | -8.96845 | -52.80848 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 068c7f5c-72df-39f8-b756-c23d7c1dc984 | -8.96692 | -52.79562 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bf4fdb1-8f8a-305f-8113-c3689f4452e8 | -8.96338 | -52.79502 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc35b88c-b534-3618-a056-dc2d3f8dcdb2 | -8.95983 | -52.79441 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6a013e-8f0f-36f9-bf3c-e786ad2708e0 | -8.95629 | -52.79379 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d0f69cc-818c-3b84-9d39-fae864718bf7 | -8.95273 | -52.79323 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76e172b2-0a7c-3d05-8797-54e5f28025bd | -8.9485 | -52.79681 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a135ec1-1842-39b2-b2e9-6befad670162 | -8.94783 | -52.80087 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e64411b1-6259-31f8-aa5f-a2ac3f3ffaa7 | -8.9441 | -52.77939 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84ac10ae-1f85-3fa8-8445-85ee46d0e4fb | -8.94342 | -52.78348 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 375f42e4-c5a4-3cc9-866f-0ca7050961b1 | -8.94293 | -52.8084 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f08b6ec-0fa4-38a8-91fa-cfac42f81020 | -8.94189 | -52.7707 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b5cc9c7-8fa7-3abe-8e1a-10ef910d12d4 | -8.94124 | -52.77466 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62bff282-3d75-3611-b8ca-64023a000037 | -8.94058 | -52.77863 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a93d33-af60-3254-93ce-9a947c27bff9 | -8.93939 | -52.80779 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99056b1-f5ed-3846-9b57-09d24f3d7c94 | -8.93901 | -52.76616 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c427513e-12db-3459-b30e-406ff9b6cf53 | -8.91894 | -52.82101 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b64216b9-cf2e-3a47-95a7-a93ea33eea87 | -8.9176 | -52.82904 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90b9e3c3-3be9-3c47-861c-a2b97e90534f | -8.88239 | -52.99563 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 286c153c-cbfc-3b50-8800-6687a350766f | -8.87297 | -53.04232 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 750477e5-58da-3029-af86-bcf21b32b0b1 | -8.87116 | -53.04053 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c61a2a29-93b1-3e06-ab3c-19ef7aed0f33 | -8.86938 | -53.04171 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ec406ef-564a-3a04-aefa-593eb052c814 | -8.69023 | -53.17691 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de696814-2057-362b-b021-f620e43b753d | -8.64466 | -53.20418 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef53dd31-a765-30dd-a336-de9c40068473 | -8.64243 | -53.17303 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d12943df-c2a5-3fda-9707-36acb257d27d | -8.63879 | -53.17247 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f37c506d-aa92-3ef9-820e-8dec87e981b7 | -8.63809 | -53.17665 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1441454d-9388-3b43-aa01-b3d789a5d3fc | -8.25824 | -51.78584 | 2024-10-05 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21bc8a23-926c-3295-89f9-9fb35ea80d14 | -8.13515 | -52.88842 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb24b9b4-5c29-36f2-b8cc-3f1247d5674f | -8.13154 | -52.88787 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e913b0d1-8780-3bd9-8011-980fa98d8872 | -7.98121 | -52.77192 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41010b3c-7690-3851-83bd-e85a7ea0b0cd | -10.92481 | -52.41219 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3c2f0ad-ed64-362b-8191-c721bce07681 | -10.92358 | -52.41975 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09cce61b-a713-326b-ad09-9937886d74cd | -10.92297 | -52.42353 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README108.md)
