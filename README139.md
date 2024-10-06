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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a38e9c23-bd18-39bc-a201-2365e566cf29 | -20.77833 | -54.8265 | 2024-10-06 05:38:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c87e05fb-b88d-3511-af83-9cb99dd5e57b | -21.40965 | -57.24958 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 269257d7-8b9f-34c1-9ad4-8c878ef4db2c | -21.40935 | -57.25275 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ca16741-9c39-3c0f-9a1b-166cb914e733 | -21.40892 | -57.2509 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 11ed741f-f804-3062-bc1c-57e11d276e38 | -21.40442 | -57.24667 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 319b88d4-6740-37aa-bc57-54ce4c725449 | -21.40412 | -57.24988 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33aeb960-9ff3-3efd-8dcf-39fef42fba09 | -21.40403 | -57.24477 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23bdc04a-04de-3e52-bb73-2eb32af94aec | -21.4037 | -57.24801 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f75fbd-c99d-3db1-bf8c-5ef6fc538077 | -21.40338 | -57.25122 | 2024-10-06 05:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dea36ac4-45f0-3150-8ef4-8abdfc98a6cf | -18.63346 | -57.27691 | 2024-10-06 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a5e9dc3e-7c6b-3002-b528-6b1a5ab8b2aa | -17.82312 | -53.77943 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dd3d6f71-2182-3fb9-b525-35f7c40f06ca | -17.8229 | -53.77888 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 67acc34b-88e8-3ddf-a5bd-34300c3139ec | -17.8227 | -53.78413 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 75e2102d-4f30-31fb-8fa3-9a125e76c346 | -17.82243 | -53.78372 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 508ff020-1c11-32f0-bb82-f92e26ca5b9a | -17.82232 | -53.7884 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ad7535f-bdfa-3a9e-9d29-c607b576bfb3 | -17.82203 | -53.78798 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 442b24f6-5df6-3591-aea8-b7653558e108 | -17.81599 | -53.78266 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67448019-bf35-33eb-86fd-633daa11d9b3 | -17.8156 | -53.78679 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 32bd328f-4ef0-338b-a23e-076310edd52a | -17.80999 | -53.77697 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b027659f-f12c-3c87-961e-10372a2ddbc2 | -17.80955 | -53.78165 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c11645cb-006b-3f7c-96e9-e73532939aa8 | -17.80916 | -53.78577 | 2024-10-06 05:38:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7676c0b6-06fc-3b81-b9c6-51d70dff2c08 | -15.39003 | -53.74005 | 2024-10-06 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1171d07-c299-33fc-b925-856882252090 | -15.38949 | -53.74517 | 2024-10-06 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba23a2a9-1acf-3b58-b91e-a05a26b95657 | -17.01615 | -55.05967 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c32d04c1-6dd7-3e3f-9ddd-fd895d9d545e | -17.0157 | -55.06408 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 353ffa12-3ee5-3791-aae5-0147b302c4cd | -17.01525 | -55.06849 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d6fc7731-d392-32f8-a03f-027a5136d27e | -17.01066 | -55.05458 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e21126e6-c029-30bf-8df7-22704ba4a694 | -17.01021 | -55.05899 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8fe2f2f6-bf5a-3948-ac24-9cbc01f58c7a | -17.00977 | -55.06339 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22e41c4c-30dd-3846-972c-16c4d4455da1 | -17.03387 | -56.68458 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d5e3d0d1-038f-39b6-9ae0-73c32e3b4dc1 | -17.00932 | -55.0678 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e6a3a70-7fa1-3864-816d-f5d99c31607e | -17.00383 | -55.0627 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 60fa86e9-fa10-30fd-9bf6-9b6d8855ff36 | -17.00338 | -55.06711 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d3aac2cb-1dfd-33bf-a413-dfc9e6a8cc58 | -17.00335 | -55.0411 | 2024-10-06 05:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0962921d-5da1-3ea5-ab9a-222a3548794e | -16.91271 | -54.55291 | 2024-10-06 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 030264de-7006-3e3a-b978-654e539595e2 | -16.91218 | -54.55802 | 2024-10-06 05:38:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4614f109-e1e9-3fcb-bd40-ae62d1d1ad9d | -17.01744 | -56.68608 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 5cb70bff-0f47-388a-b77e-beb4078551e3 | -17.02053 | -56.68399 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ea984a76-4989-36d7-88d3-a02bb6d10a28 | -16.65472 | -55.55518 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| eb2c02f1-b83f-3f79-b78f-2bec54b13081 | -16.64858 | -55.55845 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8aee7292-6fd2-3889-afda-e179a6ac08d1 | -16.64537 | -55.53376 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 55952167-8a73-32c8-bab5-68d11625d1ad | -16.64493 | -55.53799 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 15e4419a-5fc4-3928-9a7e-e93dc8414e64 | -16.64409 | -55.546 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a2b02bd0-0676-3848-8edc-cc38ac122cb0 | -16.64367 | -55.55 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 81dfdb18-2f3c-3ef5-9ee5-4c8cef623194 | -16.64325 | -55.55398 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c988ff0b-a2f8-3b34-9151-00b154bdcfea | -16.64282 | -55.55798 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 780f18ac-3ed5-3ae9-866a-014a8436f297 | -16.64241 | -55.56195 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cfdf7e6c-ebf1-3957-b23b-7490c475f115 | -16.6401 | -55.52866 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 09a280e3-07f1-3109-92b6-cc6c3d77600d | -16.63966 | -55.53287 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7db9e1ef-7d20-305c-8048-e938ea947552 | -16.63922 | -55.53707 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e4dd4b03-c1a9-35a2-bc73-14b921ffb9a4 | -17.03238 | -56.69841 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c5da818b-4b1f-3f27-9475-49f1e047bb86 | -16.63877 | -55.54132 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f9ac88f7-9aa5-310a-9816-755c742a8052 | -16.63832 | -55.54561 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 976f93f0-ced2-321c-9a87-681185fc83d5 | -16.6379 | -55.5497 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 93594f1c-7885-3559-a3ac-967d31d37cb0 | -16.63747 | -55.55375 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd995385-dfc0-300c-851e-4dd871d06c36 | -16.63705 | -55.55769 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d3e5b62b-0707-37aa-bca2-2290d8c42eda | -16.63665 | -55.56158 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 68d298e8-138e-3e70-ad62-bc43b002150e | -16.63351 | -55.53608 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 53b124aa-d80c-3453-84a5-d42b7751e85d | -16.63288 | -55.52955 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d4347757-5d3e-3d5c-80fc-e66bef798f74 | -16.63221 | -55.54856 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e5505de3-9db0-31b4-a271-1205893d6154 | -16.63177 | -55.55273 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9f1b1b04-c10a-39a0-8b7c-a339e091dd84 | -16.63134 | -55.55687 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e20806ac-d2f5-38aa-b8a8-74a814a59390 | -16.63058 | -55.55015 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ad35068d-cdb1-34ca-aeb2-440195626514 | -16.63011 | -55.55436 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 946d8156-19bb-3de8-a0c9-e21919a4a3e5 | -16.62964 | -55.55855 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5993a407-5504-3921-81c8-24c08fa716af | -16.62864 | -55.52705 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fe787656-ffc7-353c-a01a-13a6dcc3efed | -16.62822 | -55.53112 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| caca5ba8-238b-3288-a4ef-a2315feaf1fd | -16.62716 | -55.52877 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2c0216b2-b304-31a6-afaf-76e055a300d0 | -16.58323 | -55.90535 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f9377339-1da5-3e72-b994-f217898778ec | -16.58283 | -55.90918 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5486d350-776e-3db7-92f6-b8e156ea6760 | -16.57916 | -55.90631 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| dcdbc4cb-5d2c-30bb-81fe-32e58eeabedb | -16.57873 | -55.91013 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2b96f7fc-d412-3981-9576-c59609ad3b95 | -16.57764 | -55.90468 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 057958ee-5e4f-3698-b8cd-6e4ebb1f1002 | -16.57723 | -55.90851 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9b86bde8-fb91-3952-89cf-a09512d3eb79 | -17.06675 | -56.68159 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9e1e9b99-0082-3c7f-b8b9-f52cf102752d | -17.06139 | -56.68093 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1b0ff78c-5522-35e1-a09e-c1ef61a69bcb | -17.03922 | -56.68523 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 55a24e31-18a6-3e3f-a6e8-b0f04fc25c54 | -17.03163 | -56.68182 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| be37a0da-272b-3cd1-b92e-448594328f3a | -17.03123 | -56.68527 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5d05d4a3-72e9-3e69-8903-2482a7b7ed76 | -17.02964 | -56.69907 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a5f39dfe-1482-38c2-a91f-48bdad169250 | -17.02852 | -56.68394 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 16a7d3bd-7a61-337e-8988-b726f8f8d4c7 | -17.02588 | -56.68464 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 384b64b4-6730-39fa-b92e-b03350bfeab0 | -17.0243 | -56.69843 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ceca0809-d464-3a8d-9e48-8f133736ea8a | -17.02316 | -56.68328 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 92ff6ea3-1342-397b-90e4-6ef1289327ba | -17.02279 | -56.68673 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 514bd4b7-77e4-33a9-add6-251ba99e34c3 | -17.02168 | -56.69711 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 58d3bf7b-ac79-390e-bb88-99b7c0b900a3 | -17.02014 | -56.68742 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d75f12c4-c666-379e-b364-8fc652953107 | -17.01935 | -56.69434 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3ef0a28d-b402-35a9-912a-03a3b39a3057 | -17.01895 | -56.69778 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b26cb73f-9f82-3ba5-b323-fa651fde49c9 | -17.01781 | -56.68262 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b16a9d36-6c84-32a9-b4a3-d6cc1573d00a | -17.09352 | -56.68485 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9563686a-ca48-3a36-8b0d-629731cc7ab5 | -17.08894 | -56.67729 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6ad346f8-d5c1-3b8d-8034-12f922aff557 | -17.08855 | -56.68074 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| fd09a29a-8add-3edd-b456-470e5dc44270 | -17.08817 | -56.6842 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 44e3778c-b4fd-33ce-94b3-4816efadc749 | -16.96359 | -56.61034 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dc7ff6b3-59d7-3320-bc5d-00352fc69052 | -16.9632 | -56.61382 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 296435a8-795f-395c-aa7e-f1ea292323ed | -16.95783 | -56.61316 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 160704e1-3c38-35f4-b750-fe5135952d6b | -16.95745 | -56.61664 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 580f1989-f7a1-351d-80d2-176d8ce581db | -16.95707 | -56.62011 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9e34931a-a0f0-325c-b7b0-1a23708df582 | -16.95208 | -56.61597 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README140.md)
