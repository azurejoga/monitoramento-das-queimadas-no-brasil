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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec643853-3f4f-3a0a-aec9-64e735dce9d4 | -12.83941 | -44.33009 | 2026-09-22 06:03:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 65a7133a-1907-3a4e-8e7b-6e61a488371e | -12.56448 | -45.98672 | 2026-09-22 06:03:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 2cd663c3-41cb-324b-8221-523398b242cd | -12.84025 | -44.34515 | 2026-09-22 06:03:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e44f1478-22a3-374c-92f1-312020334a0c | -18.0507 | -50.9129 | 2026-09-22 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d3135b58-20dc-3368-83af-9fb76da9b98e | -18.0502 | -50.935 | 2026-09-22 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b2972411-0ac1-32dd-807f-f5109f0215ac | -18.5223 | -50.3188 | 2026-09-22 06:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 6d9a5eba-24da-30c7-9322-43f6946ce873 | -9.1832 | -65.853 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb9a1bc8-a5b9-3e0f-9b66-6df35cf98c92 | -9.36933 | -68.65762 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48ede2cc-12a5-3fae-a140-a8ac2be2fd80 | -9.55959 | -66.04331 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91a8680b-a5d9-3663-aa42-6e16b21c33d7 | -7.65473 | -67.18672 | 2026-09-22 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0f0f5bd-0303-3f6e-9e7f-b2b82ada64b9 | -8.52783 | -67.00532 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6b2bcd0-6f76-3acf-ae89-3392048cda32 | -9.80602 | -68.13196 | 2026-09-22 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7245ea0-443d-308d-bb89-ec551ac03cae | -9.55902 | -66.04802 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde1fd0f-8936-3cc8-b127-9bad63fbb3f0 | -7.22693 | -73.13969 | 2026-09-22 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89cbaf8d-cc7e-3e67-92de-b7ead4b3454a | -9.56569 | -66.04419 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0514edc-f9a1-3252-b6fb-43c596f06797 | -7.92424 | -71.34577 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51cd2a10-444a-3577-8b65-50cd9537b35f | -10.24604 | -68.74767 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fb13a59-d5e0-31bd-88f5-e3b6a7042f3f | -8.76478 | -71.10712 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd451575-9756-3c88-a88c-53eacb94c8c3 | -10.27923 | -68.87518 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44669b02-fe79-3825-bdeb-21217f4d4202 | -9.76344 | -65.05937 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4ead1e0-d62e-34b6-8154-c54fa7ddcbce | -7.90553 | -72.94803 | 2026-09-22 06:27:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d35f829-51e7-336d-9859-7079b1b2e524 | -8.73352 | -72.79321 | 2026-09-22 06:27:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec7953e7-de7f-3f0f-8f01-bb8eff90b360 | -7.92841 | -71.3464 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8fae300-2e3b-3250-b958-4724b4705d25 | -8.67653 | -70.02541 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec2168ad-1023-33e8-9cfd-127163d61470 | -8.76964 | -71.10364 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a419a4c-0e0e-3704-8e27-59302dcde393 | -9.36283 | -65.76068 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 860c9637-81e3-3077-bd7c-97810b4dfb41 | -9.56016 | -66.03864 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6accad6f-2dde-35f1-a1c7-ab98f4170f82 | -10.0989 | -69.1277 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c44a58-4baa-346c-98b0-403612e58a96 | -9.56626 | -66.03957 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f81333e-9af9-3f7a-b9a7-5fbd8082cd8f | -7.96931 | -71.33922 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796dbca6-7ae9-33c0-b054-6b87adcfec13 | -7.92896 | -71.34258 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7350a924-0333-3048-85c6-ce9d9340f732 | -7.83756 | -72.83122 | 2026-09-22 06:27:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e0d543d-3341-3e04-a72c-957bff304eb8 | -9.76932 | -65.06554 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb8d20a9-31fb-3ac0-8718-00cd4975cbf0 | -9.563 | -66.01527 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65bce190-77a7-3f3b-9d4f-23d01bb7f79c | -10.4678 | -69.19551 | 2026-09-22 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acfaa8f8-5ef2-329e-8fb3-10dc792cdeb9 | -9.12519 | -65.8665 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 10da7295-7381-3207-9fe5-5bc2a0b510ec | -10.13148 | -68.31043 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91cd6c6b-5b73-3f76-bd91-5f5be5eec1ca | -8.52732 | -67.00918 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b00c8e99-598f-3eb4-8d1b-0c7c644c4005 | -8.73806 | -72.78907 | 2026-09-22 06:27:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ea6f6af-c785-3f29-8dcc-eee40e499cd9 | -9.18874 | -65.8587 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57e6dd00-5447-3970-8ca1-be278294d092 | -8.79413 | -69.02634 | 2026-09-22 06:27:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a4a5424-ba2d-3a38-a38d-b8158ccb87f5 | -10.09859 | -69.12918 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d39f63e8-4c81-305b-8e2f-1d0121d0b645 | -9.76343 | -65.05979 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 409d7fec-a91f-3851-9fbc-7e1607abdecb | -8.73606 | -72.79057 | 2026-09-22 06:27:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8071308c-6cf2-30f9-b290-93445317cfd8 | -8.74582 | -69.45444 | 2026-09-22 06:27:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7deb6750-cdf5-3a9e-959e-98bcb69daa5b | -10.61983 | -68.80305 | 2026-09-22 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e72279f6-33ad-3dc4-89f1-504f28a162f1 | -9.55291 | -66.04728 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0d4e9d9-1781-30d6-bcab-ed173676965c | -10.10396 | -69.08987 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc233109-2e04-359f-8bad-84291f84d7c9 | -9.55327 | -66.03744 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f6a061f-1027-359d-b7bc-6311e21f955c | -10.24645 | -68.74455 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8461d273-69a6-3be8-9187-7567fffb3274 | -10.20911 | -68.74917 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d36cd366-cd22-3bbf-8f0c-00aa4e70b83b | -7.85561 | -72.27068 | 2026-09-22 06:27:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 559ef035-6bb1-350e-869a-753119647944 | -8.54939 | -67.04132 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1f3d6b5-35f0-3c32-8738-11ff26bbc8fe | -8.73736 | -72.7938 | 2026-09-22 06:27:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52dc2213-19a5-39cf-a14d-3b6e8f6f36a3 | -8.67586 | -70.03022 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 261968b2-afa2-33f4-9acf-83717c94fde8 | -10.26297 | -68.79742 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ca1653c-2f0b-382d-b168-3a59c483f294 | -9.76282 | -65.06472 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adc22ca4-4b7f-3270-93e6-7b00278016ea | -9.12503 | -65.86909 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f972d446-14ab-3d0a-9bfa-a18c4cd8d85b | -9.37445 | -68.65836 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cde62034-14b5-3023-9c6e-55611c832897 | -9.55387 | -66.03278 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b82f6870-646d-39bc-a69c-4076a771b0b9 | -10.25028 | -68.77322 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb4ccbf6-2988-312d-8135-db013275fea7 | -9.22158 | -71.86752 | 2026-09-22 06:27:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb1fa930-16f2-366e-b17a-67971204e498 | -8.00337 | -71.30904 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49dfdd70-8f95-3f91-8948-6c2676d376c9 | -10.20951 | -68.746 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd2082d5-4525-35eb-9dc8-d6bdd3bd132a | -10.25115 | -68.2942 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d5b02dc-7248-3227-acf9-a447b0fe8367 | -10.62022 | -69.35415 | 2026-09-22 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2762cdcf-2bf9-317b-be81-8581e89192fa | -9.76996 | -65.06013 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b94f12a-d537-3aad-8c74-52a5faae0ebe | -8.78248 | -68.84726 | 2026-09-22 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd1821f0-df7c-3b1d-a7de-f8f60aaa3242 | -8.26085 | -70.08611 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a5645ad-997b-3128-a029-63343e8a6a46 | -10.47244 | -69.19911 | 2026-09-22 06:27:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5223f6-c0ad-3981-b025-43402ee49e35 | -9.18995 | -65.84895 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 560af15f-8cb1-3db4-8897-5b0680b11316 | -9.12561 | -65.86428 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c3eab71-0932-386d-815d-908b9e814b66 | -9.55463 | -66.0331 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6305698-8df4-3c99-9bd0-74dfc7d92f90 | -7.96763 | -71.34044 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45f362fd-73d2-36b9-833a-c6877b596ddd | -9.55205 | -66.04696 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a84a08a-e6d3-3c3b-ad90-ca9e2c242f46 | -9.76995 | -65.06052 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40586b20-dc7a-38cd-acf8-9f1d30f5effb | -8.68114 | -70.02608 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 057cb23a-7202-3480-b41b-89e980ab222e | -10.10361 | -69.12991 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d64d943-5067-37a3-8dd8-b41fd6204797 | -10.10391 | -69.12845 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d1a9738-281f-3437-acf5-969a79a73d99 | -8.92014 | -72.81058 | 2026-09-22 06:27:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75569b61-57dc-3a47-a6be-1ddd37624900 | -9.56242 | -66.02008 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4896d13b-8fee-3d4f-b563-794bbfe0b7a4 | -8.7949 | -69.02066 | 2026-09-22 06:27:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d372631b-9687-36be-8509-1448c814ca51 | -8.76908 | -71.10773 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 729edd29-968d-3f7e-937f-8ee01382a429 | -9.5613 | -66.0293 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a9e7f538-63da-30db-94f3-62c418ab4953 | -10.25157 | -68.29089 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e40129-66e4-312a-831b-dcd07d7a4b80 | -9.56682 | -66.0349 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e9ae1a8-3e3b-3990-9e07-492411a63827 | -8.76632 | -71.10815 | 2026-09-22 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3821bbd0-fcb2-3321-87be-4e8aacc09b90 | -10.09851 | -69.1306 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04725050-b90a-3366-bc2c-75a4cf326e51 | -7.65523 | -67.18307 | 2026-09-22 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12d20bee-769a-399d-9d5a-81e17a895c1e | -8.78287 | -68.84435 | 2026-09-22 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 597d8715-46dc-30a3-8b8a-9d2f1bfbf212 | -7.8601 | -70.59351 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daf84084-a91f-304e-98e5-eb9fa31662ba | -9.76277 | -65.06512 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24eded3b-925d-3e6e-bd07-8eb3de586f9d | -9.18934 | -65.85384 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5927f239-d236-38de-9cf5-3c3760b0f076 | -10.09896 | -69.12626 | 2026-09-22 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 638f7f47-7384-3e4a-86f4-09408bf59b22 | -9.56073 | -66.03397 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95113c1b-963d-38c3-a75b-e9c4d89acee9 | -10.27413 | -68.87435 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4d1a10b-7a06-36e3-a286-be1317d2abff | -8.7875 | -68.84801 | 2026-09-22 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5bbe8d6-1445-353a-81ac-bca2152592f1 | -8.78788 | -68.8451 | 2026-09-22 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd76cab1-524b-3057-8b44-9f9b637d1587 | -9.76927 | -65.06593 | 2026-09-22 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 978951fd-bc4a-3a8f-a0ea-a3528995f1f4 | -7.93259 | -71.347 | 2026-09-22 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README120.md)
