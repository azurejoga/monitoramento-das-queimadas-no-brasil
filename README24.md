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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afb726ab-4853-3a9f-b5ae-17627d649a2c | -8.91393 | -60.74154 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6885f941-3ecc-3913-8c08-f6a28a2e3e6a | -11.49697 | -50.2874 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cb1fd9f-d7ef-3b10-b2d8-233a4a0e8b49 | -8.90385 | -60.56263 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9e5e469a-bf42-3395-a3eb-f9e79bcd8c3d | -8.92536 | -60.60609 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c819eba-0722-3b43-9874-a3071806794b | -11.49192 | -50.2867 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e736568-9f7d-3b60-800b-f058d8e99a21 | -8.91083 | -60.56375 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f90e35b4-2697-3fbb-9d01-e063f6912f77 | -8.91771 | -60.76252 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 47ee84c5-d122-3d95-91b8-2fcaebb4c26a | -8.91431 | -60.56432 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b93d31be-8fa0-3944-bc52-46b5def1b893 | -8.92477 | -60.56602 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2333311e-3164-3067-b7b1-4ed96758cd99 | -8.92378 | -60.59385 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07132d1c-c3a8-3208-9415-7508d12adc34 | -12.23854 | -59.32864 | 2025-08-06 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77ec6dc1-760e-35bc-9ce8-e33755f0327d | -8.91901 | -60.75462 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f9f30060-b75a-34d5-9785-c108fe807339 | -11.73069 | -47.5278 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04dc6297-fae1-31ba-8d8d-94609abe1f7e | -8.91908 | -60.55711 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c33cc55-3db0-3421-8d97-984450531921 | -8.91688 | -60.54876 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| dcb9693e-e6ba-3be4-89a6-0fc066caa84c | -11.03868 | -47.61637 | 2025-08-06 05:12:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 704a7d62-8795-34a1-bdd9-18fd4fa137c2 | -8.91681 | -60.5927 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d357bd12-752e-39da-8db9-48e286a0bbb2 | -9.70544 | -56.09646 | 2025-08-06 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e68f87d-084a-389c-b6fb-d4104d7cfcaf | -11.32351 | -55.21886 | 2025-08-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a9ba82-afbc-3f5c-8c3e-3dd480ba0eab | -8.90983 | -60.59156 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| d3c2853c-d09c-3f01-a5c9-a01913d3725c | -8.91496 | -60.56042 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5368523e-d6c9-3e14-88ba-6ebefbca8f00 | -11.32288 | -55.22322 | 2025-08-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d39e1d6-8fc3-3258-89e4-c4da1ef410b2 | -8.9216 | -60.73878 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8fd94dbd-6c75-3edd-be6f-8700000ab19d | -12.7346 | -46.39479 | 2025-08-06 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 145da229-cec8-3a53-8cd8-33d99a671212 | -8.53843 | -47.47848 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0887a9de-6be4-352e-9e50-a792a571794b | -8.91523 | -60.58048 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 65d8a78b-1e2f-380f-b832-1f2638a9606b | -8.52843 | -47.46745 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fa3121e-65fd-36ce-ba8f-4bc7bc733f65 | -8.30641 | -55.10896 | 2025-08-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15282ff2-b96e-3f39-a771-76f9e13365c6 | -11.91626 | -44.94058 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87908678-cb36-380e-abe7-e7e34f7d9d96 | -8.84031 | -47.61592 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd37408a-3961-3c31-941d-43eb543c49a3 | -8.53371 | -47.47251 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5363c375-1e3c-3d69-a4c0-f4ca56b8f5c1 | -8.91139 | -60.60382 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a2b67bd2-c926-3ac0-bc4d-bf55f32ac14b | -8.53426 | -47.46841 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c31b0252-57a2-3635-be05-4545c5c83448 | -8.92315 | -60.59774 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f86469d-41cf-3966-93e3-a14e0bc79120 | -9.45948 | -57.83631 | 2025-08-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4a66571-01cb-3e1a-a455-2b860e64bde4 | -13.50133 | -47.73479 | 2025-08-06 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32a0063e-f9ec-3c9f-ade3-36d00d221c7f | -11.97691 | -61.99627 | 2025-08-06 05:12:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f61c0a27-06a7-37b6-86b5-1eebcc2adf4e | -9.69763 | -48.87322 | 2025-08-06 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c5ec8937-668b-30ef-875c-370e265c3d4f | -8.91623 | -60.55265 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 620f40cb-7e2e-3eb4-947c-7d6597eeb7b6 | -8.91553 | -60.60048 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 8c7a0227-d687-38fc-91d8-8673165b47af | -11.73019 | -47.53215 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac51441c-42e6-3f08-8ae3-b2e0e59ab111 | -11.43284 | -45.14104 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 116d5d20-5be9-35a8-9eea-4e1206afd4da | -8.92384 | -60.54989 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b522fd3b-ceaf-3825-b3f1-cec4e17ed76b | -11.33168 | -47.30838 | 2025-08-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cf7a04e-1b83-3a54-819c-4fa903c87559 | -9.46002 | -57.83282 | 2025-08-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a69a2f-03e7-3f3b-beb4-93e88d0f2347 | -8.91046 | -60.58769 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e97bbe6e-65e1-397c-944f-79022c396560 | -8.91485 | -60.75798 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 43be03e8-2f9c-3d3f-ac94-e24250bb32b9 | -9.1831 | -60.82859 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e636e421-1c37-3a3d-b73f-f41c6c2b1dc9 | -9.18233 | -60.82936 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeea27d0-2a7c-3a6c-b211-0925dd9f1f22 | -12.53071 | -47.17041 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b695e485-6a05-3df0-8299-298ba5626b76 | -8.90349 | -60.58655 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3b6456cb-3069-3d27-8ce9-6a66def52805 | -8.91111 | -60.5838 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| cc2610ac-46aa-3a6b-a7cc-8b4d23378634 | -8.91972 | -60.55323 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a881e713-358e-340e-bc8f-96aae2972d6b | -8.91147 | -60.55986 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a3afe82-ca17-3dd0-9451-a44b7d152990 | -8.74996 | -55.02156 | 2025-08-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b3f5fda-ee6f-3eab-a952-c8467ea88c2e | -9.07955 | -45.05814 | 2025-08-06 05:12:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66cbe374-01e4-3341-8666-58be8a88d118 | -11.44045 | -45.136 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4a539584-93f9-33e0-b19e-b25131334437 | -12.51822 | -47.16836 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a6daa7-6afb-3409-9ffe-e62f6b4a6c14 | -8.06579 | -49.7157 | 2025-08-06 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ebe3e220-aa69-3723-884a-2b1a21e92d78 | -8.91018 | -60.56767 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 40a7ad33-2cbc-3955-bf10-f5c5a708050f | -8.9232 | -60.55379 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0513ad08-0312-3019-9d77-d0b809cb7591 | -8.92221 | -60.58163 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b15d7ad4-f9ab-3ed5-9dbe-904d5daf75f4 | -9.18244 | -60.83255 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bcf0103-57c8-36f6-846c-e15ceeb5bf57 | -11.37412 | -54.33454 | 2025-08-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0587126f-e9ca-3788-ac45-a5fd19684ea7 | -8.91902 | -60.60106 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a94f47d2-cae7-3e98-bf4a-15d5eef20333 | -8.92193 | -60.56156 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2aa32ede-fdf4-3e0f-8b84-49f004aa0fa0 | -8.91706 | -60.76648 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f9b9076-d4e6-360e-bd33-0ce058cb3504 | -8.92448 | -60.546 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62eee37e-94ef-3f38-b29f-75c6b6520db7 | -11.76049 | -47.53654 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2f8470e-b09f-3445-85eb-f6447f12f18b | -10.12215 | -51.67941 | 2025-08-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 483c058f-617d-340b-aeb8-e32ed67c4dd4 | -8.91651 | -60.5727 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58ed4aa1-cb03-37f1-bfb2-66546569c4d7 | -13.50171 | -47.73309 | 2025-08-06 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22545358-b8fd-3b4e-acb9-17490c87ab13 | -9.82635 | -63.23609 | 2025-08-06 05:12:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e895c17-3995-3519-9088-7fee7474d90a | -11.43391 | -45.14301 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fc2065a0-3540-3b3f-8e28-de8ec810e817 | -10.22144 | -59.41285 | 2025-08-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a7f403dc-0276-36cf-a988-a2022194e5a6 | -8.91679 | -60.74611 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3a467af3-50d5-3816-996e-e4ea6e82048d | -11.97331 | -61.99564 | 2025-08-06 05:12:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d5a4a02-abbd-3a0c-8654-373fdd9d72ed | -11.72885 | -47.53154 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e40c099-bfb9-3ee0-8950-90240a3d58da | -16.25126 | -39.03644 | 2025-08-06 05:12:00 | AQUA_M-M | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 09713743-6a4d-37e4-99b8-e4c44d80e873 | -13.49477 | -47.73783 | 2025-08-06 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e62c8791-3f50-3d8c-920a-b05c1d87f91b | -11.90756 | -44.95493 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac0d131c-0356-3c6d-addc-1403b5f30148 | -8.91303 | -60.57213 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0fb61952-1a12-3076-a65e-afb3a0de3bd0 | -8.90919 | -60.59546 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| d679cee8-d506-3e8c-b57c-fdfeac00c85d | -11.44157 | -45.13796 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f88302db-7d00-3774-9573-acea5c44c992 | -8.92512 | -60.54211 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10e1b1d9-025e-378c-b92a-fde2b2d5bd35 | -9.07143 | -45.05595 | 2025-08-06 05:12:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a3694a8-13b0-3892-b27d-48ad29fcf7a5 | -8.91872 | -60.58105 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b1564c80-a7e8-36c2-aa3b-abfa6e8c9105 | -8.539 | -47.4775 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4dd82982-0c80-3b13-9c39-41e5604ff991 | -8.90762 | -60.58323 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 610119a9-c6d3-31f2-90f5-3b5ef4bae86d | -8.88028 | -44.78771 | 2025-08-06 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dfffbbc-bfc1-3650-9e63-56db85d793c8 | -8.91559 | -60.55655 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1c4107a6-5c67-3e14-ae39-07b420f74edf | -9.07273 | -45.05717 | 2025-08-06 05:12:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcee5a12-d6f3-3112-8655-df3b02ebae0f | -8.91458 | -60.73759 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aabcd06e-751d-38d4-8155-e162e509072d | -11.49156 | -50.28967 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2730dae7-3fab-3738-9a4a-55fee105a8c6 | -10.23492 | -56.77012 | 2025-08-06 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b58a5a-2667-3089-8ae5-0ce00234970c | -8.91836 | -60.75857 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 03961696-4ef5-3d3f-833b-4cc8d651f246 | -8.90413 | -60.58266 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 80e281a2-9f5e-3511-8d95-a698195f9031 | -11.74079 | -47.54705 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ec5f25-e358-36f7-a1fe-20f7b814433a | -8.92036 | -60.54933 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7279af0a-f1e2-313c-9bb0-657f2f49208c | -8.9142 | -60.76193 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README25.md)
