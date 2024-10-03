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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04f7c125-d5f9-3d95-bda6-1113a7221a26 | -4.09004 | -48.47255 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4588051d-60ec-3299-8f9e-ac3246e3e4ad | -4.08996 | -48.47573 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c038b03c-3b87-39d0-ae23-a87546faffd2 | -4.08931 | -48.47971 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3645b466-5418-3f36-99ba-58c25de107bc | -4.08834 | -48.27876 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ff9887d-377d-3b22-b3be-437c80d61527 | -4.58424 | -48.00961 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b41b49-fa8b-34be-a26b-b8f50b839458 | -4.57676 | -48.0123 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e9016a6c-de4a-35c7-9ecb-f018dc14799e | -4.57616 | -48.01607 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b89d8ece-9dcb-3bc5-a077-9c233b59d31d | -4.57272 | -48.01553 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 38046789-cc0a-3188-bc92-21992d0b150f | -4.57212 | -48.01931 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e253515c-70e2-3f15-b8bd-bff67966b4b4 | -4.49422 | -48.10803 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90dbdfdb-f8fb-33dc-bc54-92597e33a444 | -4.49361 | -48.11182 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 442d9e78-5ca8-394f-bf2a-8c1502faf189 | -4.48731 | -48.10694 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b5e3f97-4fed-3aa1-a81c-2d30d501f0fc | -4.48669 | -48.11074 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bd428ef-5cd4-388c-ae43-0e16313585e0 | -4.28294 | -48.0674 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7203ae3-657b-33c6-9327-d5f60c12d90c | -4.27948 | -48.06684 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee6a99aa-ab39-3d2b-a858-4177c47b5d4e | -6.16899 | -49.28542 | 2024-10-03 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bbb4e47-35c3-3b9e-8df5-a512cc3bcaa7 | -6.08056 | -49.13734 | 2024-10-03 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84d68f9-1fd5-3374-bff1-c2e85d104c5a | -5.46767 | -49.02312 | 2024-10-03 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a548841-6a50-3de7-aa50-85eed8aaa01a | -5.36314 | -48.97406 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95cf1c06-b6bc-32e1-82e0-c18e4957ebd7 | -5.2215 | -47.95628 | 2024-10-03 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84e80b94-721d-34a8-aa4e-2e0bb0ac4cbd | -5.21809 | -47.95573 | 2024-10-03 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e73eacbe-7fe1-3ac1-8c38-c7a4be133e30 | -6.97733 | -49.43071 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 197ecd73-13dc-3175-8a8e-54b10795c981 | -6.97375 | -49.43015 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdb60755-093d-3c50-ba30-d09b294862b2 | -6.97309 | -49.43424 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a3561f-c130-37fb-8a98-da17769bbe81 | -6.97017 | -49.42957 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 307d5381-5dee-3408-817b-2665352d4c42 | -6.96951 | -49.43367 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e48638d4-c97b-345f-b45d-ec767a21a467 | -6.96659 | -49.429 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb3238c3-3da0-3ae7-91a8-842961bcc435 | -6.96593 | -49.43309 | 2024-10-03 04:25:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f0b286ef-1d25-3a4c-9edc-f5ae2328ba96 | -6.73571 | -48.7011 | 2024-10-03 04:25:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e17af6d8-3dc6-3f00-ab90-61036f60c5b9 | -3.30716 | -50.44633 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf19cc3b-3f53-3ac2-9e96-63eb69a500f7 | -3.30262 | -50.44918 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d306d33e-25b3-38bd-9206-f0033fef33e7 | -3.27296 | -49.10993 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dfe53b8-7aed-3066-90c4-2baa43c9360d | -3.26928 | -49.10936 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 422fd513-695b-3780-8458-3a0702d91afb | -3.25568 | -50.13985 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05ece58c-d2a3-3aa6-b18f-95d9413b9cfe | -3.25176 | -50.13924 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98e4d041-c6a0-363c-b3e9-e941617f8f4a | -3.20922 | -50.38015 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af0957c4-4b83-31da-8228-b1311ac3e68e | -3.14158 | -49.41803 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29f030eb-74f3-3bb0-895b-2ee68ec11fd4 | -3.14015 | -49.42705 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d9023dc-fb76-3c7a-a4a7-cd97b46e49b3 | -3.13783 | -49.41745 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 373fa54f-28e7-3824-9f59-2ca0e663e1c4 | -3.13712 | -49.42194 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc5f22b6-c152-3786-aff8-705015229751 | -3.03971 | -50.45234 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac63f003-7c65-35f0-9b77-578052a42d37 | -3.03571 | -50.45171 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fd34890-500b-36ac-bbc9-e9c81bb2ee4f | -2.95723 | -49.35507 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f52abaa-b208-3ce5-b523-6a8d9f51e65f | -2.95651 | -49.35962 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62ec68c3-5f56-3ffb-aa88-593baa0e816d | -2.9558 | -49.36415 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d842f994-5287-3652-9a7d-514046b0d234 | -3.45843 | -49.14579 | 2024-10-03 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a0c4c6d-bf42-34a8-93c1-a296843f6417 | -3.4542 | -49.55096 | 2024-10-03 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86a27f75-b08b-31ca-8e30-9a2f1a345e25 | -2.33889 | -48.90007 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e793b57e-6f65-37f2-acdf-3a8e1e913984 | -3.3106 | -50.45038 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f26b4f34-9093-326e-831f-0caa49916e05 | -3.31005 | -50.45382 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4146e41b-f696-3a0e-8f5e-2c60ad5b7f4f | -3.30661 | -50.44978 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3265361-5194-3935-bc99-697049e75de0 | -3.26858 | -49.1137 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38739ad8-a543-33e8-8441-d04c0f434863 | -3.25097 | -50.1442 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 46de3c76-d675-312e-8a06-8ea22927a55e | -3.24785 | -50.13863 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ebbacfea-4311-3273-b244-ebe6a558e8e2 | -3.14087 | -49.42253 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86ee3685-2b54-32bb-84fd-06c515a7ddc1 | -3.11679 | -49.40486 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 041d101e-c6eb-302e-abdf-077ef3380c49 | -3.11606 | -49.40938 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8cb4a8a-42be-31f3-bae4-2e245d588f9e | -3.11231 | -49.40877 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83556520-9380-30a8-bdd6-0feef2f7495e | -2.96026 | -49.3602 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25d0986d-4c1d-3c67-9f28-652ed0b35d75 | -2.95955 | -49.36472 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 41a72934-c55d-3456-9496-ec938bfeb98d | -2.80213 | -50.28573 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0352eeea-98a2-30ae-97be-4b87391b33b2 | -2.80159 | -50.28916 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3fac074-abb0-3eec-83c7-307e2ffd31c4 | -2.79816 | -50.28511 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d042f7eb-8235-39da-a18d-f53801813640 | -2.79761 | -50.28854 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 970290f0-932c-31e9-bdbc-417fbc54e7f7 | -2.57072 | -49.07265 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5e30738-b62c-3a02-b355-576b226dc438 | -2.49062 | -49.05116 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa1cc6aa-d59e-3b26-912e-4c0bd9b4dcf9 | -2.48991 | -49.05553 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d85dd61c-e67c-3a50-8b64-fc4503a1127b | -3.92382 | -50.66423 | 2024-10-03 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9958688-29d1-3393-9c93-6d32ff1ff742 | -3.91981 | -50.66362 | 2024-10-03 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad2af1f-e4c5-39bf-9ce5-a00dd3c4d5a1 | -3.57196 | -50.57152 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0a789ca-8abd-3ebb-9bd2-9c7661f4c434 | -3.56909 | -50.56398 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 504e3b90-3ce3-316d-b694-d6ace99914c9 | -5.06047 | -49.80283 | 2024-10-03 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a52755f3-107e-35c3-a9a5-2d34fb752250 | -4.09458 | -49.98629 | 2024-10-03 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d277251-9bfe-309b-a1f7-6f39d704134d | -3.92918 | -49.69082 | 2024-10-03 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dababf13-d024-31d0-9e23-69a584e535df | -3.92543 | -49.6901 | 2024-10-03 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2700b450-e4c2-3f68-acf8-8ab7936ce44f | -3.65531 | -50.18352 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fe1bb5c-51f3-32f9-a083-e97051875761 | -3.56853 | -50.56741 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0fd8da-b5a3-3f93-a962-42e1f7a576d5 | -5.06794 | -49.78921 | 2024-10-03 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6384729-07a3-3052-b632-4c5bfa4c475f | -5.06637 | -49.78992 | 2024-10-03 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df827025-7c21-3eac-85ae-abcc53a7b563 | -5.06264 | -49.78928 | 2024-10-03 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b8dbf6b-4197-333e-b6d0-5e84c02da5ae | -5.06119 | -49.79831 | 2024-10-03 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e183839-c358-39be-b96f-686c1b7e44ea | -5.05746 | -49.79768 | 2024-10-03 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ca19fc9-94b3-3339-839f-5127584f268e | -4.3296 | -50.4924 | 2024-10-03 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a9067ae-3c6f-3f33-84d4-6f24274344df | -4.04086 | -50.38747 | 2024-10-03 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5926ef65-b3eb-35bb-aba6-a8b4e4696291 | -5.69159 | -49.79409 | 2024-10-03 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5acbc86-9101-3209-be9d-e0cefbde796a | -5.5232 | -50.04162 | 2024-10-03 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75466875-7c79-304d-b1a0-09627505e173 | -5.51869 | -50.04557 | 2024-10-03 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b62182-9723-3134-baad-f160c4c207d1 | -5.51491 | -50.04504 | 2024-10-03 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b2fd890-c981-37d7-8549-b4cf5ccf8492 | -5.51416 | -50.04963 | 2024-10-03 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df37f8e0-1fad-3e62-b795-740308fca4fe | -5.02058 | -50.86714 | 2024-10-03 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ad1c085-e6e0-30b7-a308-0702b8d390bd | -6.54976 | -51.04937 | 2024-10-03 04:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be132995-8aaa-3417-bff0-9fa2d799ad8a | -1.62225 | -50.53845 | 2024-10-03 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26f64ceb-9c71-38fc-aaeb-aaffd926b2b5 | -3.25625 | -50.94057 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3399ceb-69c8-34c0-8815-f66a28b43d29 | -3.25213 | -50.93993 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01160443-0679-3707-aff1-7cb9218c1fa0 | -3.22591 | -50.79649 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d0027b6-4f00-3b28-9b18-374c0628a3f7 | -3.49189 | -50.80579 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca1cba7e-bdfb-372c-8cd4-efe32701eac1 | -3.49187 | -50.80487 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f76c28-454c-36ce-83bc-18a8f512ffbe | -3.48781 | -51.18987 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e507c23d-4a35-3aba-a787-ea4c13c086bf | -3.30445 | -51.11361 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 970dac6a-cce5-3798-8dee-23207380be37 | -3.30089 | -51.10915 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README84.md)
