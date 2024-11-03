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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b401bfa-0404-30ce-96f5-34613e2c05ef | 0.07555 | -51.55249 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e86564e-44b9-3017-9976-f2ee3f615090 | 0.05559 | -51.52628 | 2024-11-03 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e7c44c6-2586-3340-adf0-5e7657816556 | -0.58855 | -51.91765 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2aecc4b-2bb9-3639-8711-fc45240db585 | -0.58475 | -51.91704 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9e435fe-12bf-343a-9530-95f639c1a1b3 | -0.56676 | -51.66506 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d2ef464-1fc5-3c88-abce-dcd84fd704ee | -0.51129 | -51.63496 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e4dd3e9-ae9f-3de2-9d80-e9af403d19f3 | -0.50877 | -51.65605 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4336746b-a7cd-3700-be15-d367a6fefbea | -0.50823 | -51.65407 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8ed6379-9a68-3687-a9fd-39c3edf6136b | -0.50784 | -51.63629 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0f01ef5-ce8f-3e28-ae8b-64d1e9e18d4f | -0.50746 | -51.65884 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4faba2ff-0f59-3d8d-ae11-ac232a6f6f89 | -0.50742 | -51.63435 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c96d7b8-fd2b-3526-981e-74ca379dbc1e | -0.50711 | -51.64108 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bceb900-4528-3a03-973e-bb51cd5443f7 | -0.50666 | -51.63913 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74f53182-9c87-3aaa-9052-106934f4dd95 | -0.50564 | -51.65065 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c6ea3b9-9862-3111-bf30-5bedae1d9cc0 | -0.50513 | -51.64868 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b17c634-5847-331f-9519-d2387fa73af9 | -0.50491 | -51.65543 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f085b5e-3f7d-3368-93a0-1c2d668131b7 | -0.50436 | -51.65345 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4796ade-cd07-3c96-8538-010be8008ecd | -0.50324 | -51.64047 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b65d3e7-6ac1-3651-baaf-a34683dc88d7 | -0.50251 | -51.64524 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2034c91-0f9f-31c9-8c3e-a8a8276afb37 | -0.50178 | -51.65002 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63a6c40d-4b38-3520-a3e1-6bff992340ff | -0.50127 | -51.64806 | 2024-11-03 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38589b02-da8a-34ef-bc10-72f6e976a747 | -0.60269 | -52.29565 | 2024-11-03 05:08:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 311191d9-3bcc-38a9-8281-f1f4df1f35bc | -0.60199 | -52.30005 | 2024-11-03 05:08:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b266387d-730c-35e2-87c9-6b811e6efbb5 | -1.91187 | -52.43866 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f257b868-4ea3-31f9-9e4c-434933d55341 | -1.8852 | -53.1992 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41d05ad0-bea9-3936-ada5-688201ad21c5 | -1.88371 | -53.20037 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee2b8df-0fea-3152-b150-d82b2e082c02 | -1.76041 | -52.63699 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe9b4594-9f0b-355b-8116-1a8fa7401f70 | -1.75889 | -52.63479 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9774d995-1e13-3dd8-91c5-8c3eb3e61b7a | -1.73668 | -52.04293 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b7ef8c2-3e9b-319b-9be3-ffa561bc716c | -1.71655 | -52.08605 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5d40048a-b933-3ec3-962f-06ac78245fe0 | -1.71581 | -52.09074 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4787ab0a-e9dd-382c-bd3f-7d58c8cd9c4b | -1.71508 | -52.09541 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d561197-4fb1-3f9a-adc9-5afe1a452f21 | -1.71272 | -52.08549 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c8f52fbf-43cb-3bc4-852b-1aa750df5bd4 | -1.71198 | -52.09018 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1df9bd8f-a87a-3c4a-b667-888906e55c92 | -1.68077 | -52.28868 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b5e2cc7-c17c-3881-9934-326e14d6f02d | -1.68005 | -52.29324 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53fde8fb-86b4-3254-80e7-0cbf06d4d709 | -1.65964 | -52.59227 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f98966fb-4f1e-3e6c-be81-fc8c8b8f444b | -1.6575 | -51.98527 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efc4d407-5448-34b2-a13c-f5e0d518704f | -1.65684 | -52.59412 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c3218f4-8c32-3346-8b13-d43c0fb7282e | -1.64841 | -52.37195 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75e78d8e-6120-3811-907e-d62906fb6460 | -1.64465 | -52.37137 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 786179f9-76e5-3f51-a155-010b8821f1aa | -1.57825 | -52.65131 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d52b97e-9c09-3df9-aa41-ba4bcf301f6b | -1.5576 | -52.30928 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5904c981-98fe-30f3-9048-9bf1b93b665b | -1.55027 | -52.47803 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b32fb1-20a6-3b02-a2e3-568c76f0df2d | -1.53508 | -52.45297 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00d09625-c97a-30cc-ac17-116fb3906e10 | -1.52675 | -52.30914 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23bb2fbc-91e0-39b5-abe4-3a68604109bf | -1.52298 | -52.30856 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 547da1ff-eb03-37b5-a272-2716d6157dc6 | -1.51921 | -52.30797 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5518a346-ee0d-3f06-b20d-ffe7e88c28cb | -1.4587 | -52.00283 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb2e88e-b10a-36ce-b9bd-23e09a2d8b78 | -1.42104 | -53.10927 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4a23f13-d015-3f5d-ba88-07b512410b8b | -1.41715 | -52.12057 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ce23334-9c2f-3912-adc3-a3b6529b9836 | -1.40574 | -52.11881 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05860330-a28f-3f8d-9121-fe7b4e521914 | -1.40542 | -52.126 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a39674ba-2791-3bd0-8a11-ebf2c0a1f2dc | -1.40503 | -52.12344 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47696e80-a112-3239-8c03-228fc23463a9 | -1.40433 | -52.12806 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b790c2be-aa3f-3264-a213-d6ebcd523c75 | -1.40309 | -52.11618 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 484183e5-20aa-3127-8354-1694bd82b401 | -1.40263 | -52.1136 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a107f95-27c8-38c5-853d-2e8b633726e3 | -1.40235 | -52.1208 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13bf81ee-0765-3d9d-be8f-b37c1cb449bb | -1.40193 | -52.11822 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0effde3-5822-3a15-94e5-f50005d4b192 | -1.40162 | -52.12542 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6253a5d5-4189-3630-80e2-4d5574f897a3 | -1.40148 | -52.10173 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e624f1ee-dd79-3d3d-98d5-c6fd2705f299 | -1.40123 | -52.12285 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6ef3c9d-71d2-3dea-9934-a3ceb360ba91 | -1.40074 | -52.10637 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd3255d1-3744-3044-98b7-0646b78da9e7 | -1.40052 | -52.12749 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e18b6a0c-15c9-31af-8fdc-bc56cb784c6b | -11.1444 | -55.17135 | 2024-11-03 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e951e1d5-3ce6-36f3-876a-8165b0abf729 | -11.14378 | -55.1756 | 2024-11-03 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b50799c0-df21-32f7-9d12-c664a0eafb3e | -11.1128 | -54.82855 | 2024-11-03 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a503f531-7f56-3b64-b176-b21679aa8245 | -3.96902 | -55.39101 | 2024-11-03 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 434fef11-d65f-3da1-8317-94bf5e6bd109 | -4.33319 | -55.42414 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 488307c2-6556-336c-b821-8de9621b5737 | -4.32531 | -55.43027 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e52a6b3f-ff74-3dc5-9790-e4404dfa7a56 | -4.2542 | -55.35298 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0103cf5-0774-36fe-be80-31bb73a49af3 | -4.25361 | -55.35339 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c531d59-e341-3080-be8b-290202ed9339 | -4.24967 | -55.35647 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5a79f34-bf03-3f83-9eeb-995d971f65f3 | -4.24345 | -55.39604 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e280b9-e8ac-326a-8c56-f300359701c8 | -4.2429 | -55.35542 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de9c9c84-d07c-37f4-9c6d-545c200da678 | -4.24233 | -55.35903 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ba206e-b222-36d5-a8ca-bea1042b42d3 | -4.12674 | -55.09307 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 490dc8ac-2d8f-3591-9c58-5b2639287979 | -4.09897 | -55.11482 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbf4ba73-846c-35c9-aaee-2a09911ab253 | -4.09163 | -55.13979 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28c23625-7e96-3087-ac91-10e9056afb45 | -4.09104 | -55.12106 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 622af515-dc4d-376a-8226-132015789443 | -4.32869 | -55.4308 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 045ca97a-3456-3958-b67e-5bcb63390a8a | -4.28504 | -54.9518 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57afff0e-3c7b-3b7f-961d-f46da16383c1 | -4.25365 | -55.35659 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b9880e4-84c3-3d73-a5a5-4cd651a9d2e0 | -4.25305 | -55.35699 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a003eacc-e0fa-3a3b-8f23-692027d7d8bc | -4.2491 | -55.36007 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5237e3a5-fa98-32fa-9879-5aaa7b82206e | -4.24628 | -55.35594 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe24216d-71ad-3d13-af16-a786a4ea54b1 | -4.24572 | -55.35954 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c51c80b-0bfe-3acd-ba07-bd269bec5343 | -4.20007 | -55.38572 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 377e5db7-ce2a-3bbc-a08f-09c07184bcaa | -4.16492 | -55.27701 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcdc4437-c9bd-3051-8ab3-05e78f0563a9 | -4.16437 | -55.28064 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dda58ea-4200-3d09-9cf5-40d6640daecf | -4.16154 | -55.27647 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e78bace-544d-378f-8c41-e18f59f697e6 | -4.16098 | -55.28009 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c65c0334-6d39-3858-8fdb-d5e9836a275b | -4.12731 | -55.08943 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc7cc8fb-7fe8-3135-a4da-95541f80d481 | -4.11018 | -54.99676 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d10c77c-ec5d-3b78-b118-c68268b24235 | -4.1035 | -55.10807 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 764d3800-40cf-3170-bd90-739b3153dd48 | -4.10066 | -55.1039 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c24c9838-984b-3856-b66e-f87865bc5903 | -4.10009 | -55.10754 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09b46bbe-033d-342a-ba24-2babe6db6347 | -4.05589 | -55.01154 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b1be55f-e040-35dc-abbc-9fae6701988f | -4.05532 | -55.01521 | 2024-11-03 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d418b177-4e05-3832-83e6-17f46a297147 | -6.05225 | -55.61848 | 2024-11-03 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README81.md)
