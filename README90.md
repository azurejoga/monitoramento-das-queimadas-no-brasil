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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5fe4ae8-283f-3066-b6e5-304e394b28d6 | -9.55156 | -50.18847 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ecd7688-5633-356f-b209-a53565d5418c | -9.54883 | -50.20584 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| caeec65f-3f7a-3a5d-9f84-b33b7cc51351 | -9.54881 | -50.18447 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 164e8d67-4dea-38e1-8c14-e2a8bc0b2ef6 | -9.54826 | -50.18794 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a5c58a1-d5de-3fd5-a9db-96452ecc6dfa | -9.54496 | -50.18742 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d67f1d0-600c-3318-b325-cc9f45baebed | -9.54168 | -50.20827 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e51b4ace-1b02-3373-ab88-c5c234d53f61 | -9.53893 | -50.20427 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a1245c4-55fa-335c-ac2b-8639d726f8f2 | -9.53838 | -50.20774 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27eb84df-4c07-3560-8e83-665f15c8accb | -9.53617 | -50.20026 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1996cc72-0e55-3497-90a6-8a1a9051c610 | -9.43248 | -50.05919 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 370292ee-9c7c-3014-8f5f-3f59e91633d7 | -10.15369 | -49.99648 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd1ec2fe-56cb-3b8b-b48d-434f42be6f8b | -10.15315 | -49.99996 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6026d04-6160-309a-a71e-a505e611de18 | -10.14985 | -49.99944 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 088c98f6-f64d-3c4d-bf85-c851afc61f52 | -10.1493 | -50.00292 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19fd6e82-d1a2-3ab9-8972-c4a4607498b6 | -10.14876 | -50.00641 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 02de5513-63e0-3745-b058-c56c8636a240 | -10.14654 | -49.99891 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abf444ed-db5a-349f-ad37-afcea91122b8 | -10.146 | -50.0024 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d40fc909-1145-391a-a6fc-51c12c040b7d | -10.14546 | -50.00589 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48706f58-4f2d-3404-af7a-a7a464b1d14a | -10.14491 | -50.00937 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 670bd494-da03-30cb-9f2b-a39f016a8a71 | -10.14216 | -50.00536 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67eedd22-c9ad-3b96-8353-8e32b828d7ac | -10.14161 | -50.00885 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79afb880-d39b-3c6c-ad5a-29c366e153f6 | -10.13822 | -50.00486 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5924a891-fb1a-3dc7-a26a-fcf910834543 | -10.13768 | -50.00834 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3c66679e-f612-3788-a935-3d611d1a9b51 | -10.13713 | -50.01183 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 252c3bf1-53ee-3bf5-bafb-3805156368e2 | -10.13659 | -50.01531 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6131dbc2-4ec6-34ac-9b4f-5525e0ddf8b9 | -10.13604 | -50.0188 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19079beb-aa67-3014-a9d6-651358cf42dc | -10.13492 | -50.00433 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1ec0b5b5-9ce8-3bd7-b91f-e47316854035 | -10.13438 | -50.00782 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 07a5ed66-e57f-3663-a5ec-b931505b3a90 | -10.13383 | -50.0113 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b3aea55b-ecda-36b6-8137-7a6163fd5a6b | -10.13274 | -50.01827 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a6a4a0f-af70-399d-9d4e-f5e50f567c23 | -10.13107 | -50.00729 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f730eccd-e504-35a1-b8d5-f87388659674 | -10.13053 | -50.01078 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0bcc2f10-f831-3166-a60c-50d75de8dabc | -10.12998 | -50.01426 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47132a3b-68e0-3bb0-a6c7-c4e8dd47a177 | -10.12832 | -50.00328 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcc7a09c-8642-3005-af71-545d7fc03c81 | -10.12777 | -50.00677 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a231e2c-22e9-3f4e-a8a6-0cbaa913e888 | -10.12501 | -50.00276 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d467986e-c8e6-3d39-b569-9ede4c64736a | -10.12447 | -50.00624 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed89ad99-7835-3153-ae88-baf26955b773 | -10.12171 | -50.00224 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83ece448-4597-3907-b7a4-f4ea69a7ea0a | -10.12117 | -50.00572 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ff13814-e1aa-36c0-9d4e-3d5d33915ee8 | -10.11786 | -50.0052 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 883c2ee3-61f5-3e76-96e3-267b7bcb7eca | -10.11139 | -50.08984 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f039426-7464-3ad8-bf09-31366bd66ec6 | -10.11071 | -50.00763 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a6b80c2-bed5-3314-8a21-da040d461fc3 | -10.10687 | -50.01059 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5691d6c-f395-36d0-a7d6-7a89251349b4 | -10.10302 | -50.01355 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5969a9cf-a96e-3d50-9a55-c0fe544e6e20 | -10.09972 | -50.01302 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ea000bf-38ff-3e3f-8885-d64fa4bbfda6 | -10.09587 | -50.01598 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04daa3d8-49d0-3b08-a4e8-fa38a2e5c190 | -10.08235 | -50.16727 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a08e73c5-c05b-3037-943e-34be39db0d08 | -10.07959 | -50.16327 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf6f0098-0b35-3a7e-8674-61ffff8f628d | -10.07905 | -50.16675 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d52fb16a-d86f-3a5c-adb4-3acdc66b97b2 | -11.5949 | -50.50475 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d058ca61-ffb4-3943-9f31-d03bea64ec2c | -11.59435 | -50.50825 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fab0b634-ee2c-331e-865f-c2f9da9e294c | -11.59214 | -50.50072 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 745287e8-7545-37b3-82f5-05ada3dc9db4 | -11.38593 | -50.79339 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d28f40d-39c5-3c56-bb29-0483825ffd26 | -11.10263 | -50.6683 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa988cf1-28e8-30c7-929d-7b3733155a7c | -12.17615 | -50.1556 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f48e75c-7faa-3735-896c-0759c0f3a693 | -11.83938 | -49.62572 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 51ab261a-df38-3ea0-b31f-7120033f6b7c | -11.83884 | -49.62931 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88aabb2c-0a6c-3b2d-9a11-52a9a7a5db84 | -11.83775 | -49.63645 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 267bb0dc-22b9-39cf-a8a8-5044d016e914 | -11.83496 | -49.63235 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 10728f5d-1af9-3f6e-8edf-a3398e7d01a6 | -11.83442 | -49.63593 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70eff719-3297-3d07-bc8c-1e23156b10b8 | -11.80298 | -50.14992 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1ef1bc3-7b60-3df7-b160-283309225b80 | -11.79967 | -50.14939 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29f27132-155a-3a42-96bd-ca1fa029ece7 | -11.72957 | -49.9216 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06297c8d-fab4-3034-bd5c-709ee7e23dfb | -11.72294 | -49.92054 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c381d4cf-a1bf-3f3d-9f79-a4b4f8ae5eb8 | -11.68923 | -49.91881 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4de3509e-31f4-32df-890d-7bc756d68258 | -11.68586 | -49.89654 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6629cd3e-470b-3f99-a38d-8bd928f626e2 | -11.68531 | -49.90008 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69e3ce4b-13a3-3343-9e01-1cbdb51feb98 | -11.17715 | -50.2146 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5124b2fe-ce2b-3b5a-b676-78de3eb18b33 | -11.17546 | -50.18205 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a9dd780-0f1e-36e3-933f-8e9103f304a1 | -11.16789 | -49.72722 | 2024-09-27 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95c3981c-cf86-35d0-8c6d-a488afe1baed | -11.16735 | -49.73075 | 2024-09-27 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e60f87d-a86d-3bda-8bfe-1e2121ffc2b0 | -11.16403 | -49.73022 | 2024-09-27 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 480837c0-d31c-353d-ae1b-14eb43b2258c | -11.16076 | -49.72984 | 2024-09-27 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f915ddc7-0f81-3262-8ac2-f5a453a5bebd | -11.01947 | -49.63164 | 2024-09-27 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87d26f63-73c6-34a7-ae5f-7e610d88470d | -11.01615 | -49.63111 | 2024-09-27 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c37a489-f858-34b9-ac7e-b2267739f275 | -11.01337 | -49.62705 | 2024-09-27 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16f3d32c-2a66-3018-b560-f6265a30bdfc | -10.95368 | -50.14321 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff5905a2-b1f5-3df8-b9ee-7f0d48c166cb | -10.95038 | -50.14268 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3e31ebc-8cc0-3ed7-9318-589d619a2619 | -12.22036 | -50.68181 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ede883fc-88f6-31ca-bce9-3b8d4f3062e4 | -12.2165 | -50.68478 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8de7f48b-0bb2-37ef-890e-71b474075b84 | -12.19776 | -50.84719 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17885e98-554c-3afa-8079-dcf16a849a41 | -12.19721 | -50.8507 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 286cc2c5-3435-3b61-a932-f636c2fbc81d | -12.19391 | -50.85017 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1c28d52-9f20-3e00-8b47-00b01445f12f | -12.19116 | -50.84612 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 905f9dec-25dd-327d-91a0-f5ef7604e56e | -12.18896 | -50.83857 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 453edfee-ca07-3b1c-b1c9-08be2dcd29c4 | -12.18846 | -50.81644 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 782282ba-978e-30f4-8dc7-73705834d1bd | -12.18841 | -50.84208 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b23bc4f-76e3-344a-9df3-0f8dd9e23cc1 | -12.18786 | -50.84559 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a459cf0-b50d-3f4c-979f-a3b34c915459 | -12.1868 | -50.82697 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be6bba34-a788-32cf-8edf-8f50b4f7a7dc | -12.18625 | -50.83047 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c022cfe-3eeb-3cae-80dc-9bd06540b578 | -12.1857 | -50.83398 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae91d8b-a82f-374e-b27c-c5edb8dfd93b | -12.18516 | -50.81591 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef3b517c-cada-34b8-a491-4d4c9998769f | -12.1846 | -50.841 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 342172f0-8f27-335d-a3a2-e85a5b32be26 | -12.1846 | -50.81942 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 614e77da-6e9f-3ad2-9bc3-8bcc48b39acd | -12.18405 | -50.84451 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 044fd8e4-7b1f-3505-be1a-4b96f93660bd | -12.18405 | -50.82292 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41d084e4-1559-3db6-a89f-b8e0429497c1 | -12.1835 | -50.82643 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7542d91-71cc-34bf-beba-809da4831110 | -12.18185 | -50.81537 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a988a08a-a44f-3e52-a854-9976e7eaa564 | -12.178 | -50.81834 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53a4dfe2-3bb9-3cf1-b3e8-dc27d38ed8bd | -12.17745 | -50.82185 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README91.md)
