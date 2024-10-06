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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4b1484c-f122-3148-8683-8b1048bde90a | -17.03904 | -56.82901 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 835b8ebe-a705-3784-a446-719067ea325e | -17.03849 | -56.71385 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 5dcc11e5-fbda-368b-bc36-5638d0fd869e | -17.03705 | -56.72319 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 7ed1f06f-32a8-33eb-9ed3-7ad7678f1e16 | -17.03587 | -55.05431 | 2024-10-06 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b081d430-c151-3872-99dd-2cb28e45da1c | -17.03561 | -56.73252 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 9d75b99d-1f91-39e3-868f-09b17bb3d61c | -17.0345 | -55.06373 | 2024-10-06 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f67a3c85-69b4-3e81-895c-68f2af6fff38 | -17.03176 | -56.68787 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| b4f29bdf-c67d-33b1-a1eb-dbd5a3c880b9 | -17.03155 | -56.81818 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e65dac55-2252-3787-b40a-77cd508e5953 | -17.03034 | -56.69719 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| b6370494-2798-3332-ae5a-fe0dbfc2b669 | -17.02962 | -55.03409 | 2024-10-06 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d7ee4aca-a9ca-39f4-b8b1-e8860e949371 | -17.02892 | -56.70652 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 99cb19eb-3f56-3fbf-bae7-8ed7b53a51a9 | -17.02826 | -55.04352 | 2024-10-06 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| dab9d9ef-a83a-3b15-b3c1-2c25b48729e6 | -17.02749 | -56.71585 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 7c8697c2-6789-3a38-b342-911b55e16c52 | -17.02607 | -56.72519 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| f813cb24-ea65-3f3b-82b1-ddea6d430b4d | -17.02554 | -55.06236 | 2024-10-06 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a263462e-1218-3cc2-a8fa-7354bda8769f | -17.02464 | -56.73453 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b4f4112d-7174-38ca-85eb-497407691d34 | -17.02262 | -56.81672 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 485da439-05ae-3d38-a49d-b37c135bea9c | -17.02117 | -56.82609 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| eb4f69fb-bc0c-3844-8206-177bb7fc981b | -17.0193 | -55.04214 | 2024-10-06 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c3ce03b7-535b-36a0-83d9-3b88c40113b1 | -17.01572 | -56.73308 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.1 |
| e8d3ed2e-682f-337d-b423-71547be9e585 | -17.01177 | -56.81876 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 429506ef-f7e5-3b64-ba08-2e4f8f53914a | -17.01108 | -56.70361 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.8 |
| 7f5ce19e-565a-3450-8007-c1082097b31b | -17.00965 | -56.71294 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 97c7f6e6-49c1-329b-946b-1858f8f65e7d | -17.00537 | -56.74096 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9546f021-10d6-307c-8c77-b8afbd503741 | -17.00427 | -56.80793 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 30c51523-e833-32be-8efb-a52a0c802f6a | -17.00251 | -56.75966 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b00a6c13-250d-35f4-bb71-b21f93d58b4f | -16.99677 | -56.79709 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 580348e7-50a4-3114-91e4-0439df076e8b | -16.99534 | -56.80646 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| edbe28b2-6187-38f6-98d5-42966724a555 | -16.99358 | -56.7582 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| af5813d9-b359-365d-a124-19dc3eb9b1fe | -16.99215 | -56.76755 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 932ac8ec-059a-3d45-b87f-2e6a53fd7633 | -16.98622 | -56.1427 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 1e3fda38-4dfd-3986-9168-744016149425 | -16.98322 | -56.76609 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 3a53077b-9687-3f9a-b021-100080efc2ab | -16.98178 | -56.77545 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 2512d2af-57e1-3a8f-944c-6b67bddfe9d9 | -16.97935 | -56.61252 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| dae4b5ee-996b-3004-a211-5b405addec2d | -16.97286 | -56.77399 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b5b7a38e-2360-35ae-ae65-d8d697fee0c3 | -16.96902 | -56.62037 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0d4c0e14-1548-3a77-8ca7-e07343e21bc9 | -16.96012 | -56.61893 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 7ad4b37f-25c2-3020-93e2-683e3919806a | -16.94937 | -55.82944 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 50bbfb1d-cac5-354d-807c-b62a6ad8aa02 | -16.94935 | -57.70184 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fb7423f1-3eda-3bfe-bea9-16f7574fddb8 | -16.948 | -55.83865 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 08c8dcae-d463-3c18-82f0-c78853cd423c | -16.94173 | -57.69037 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 8ebdc961-dc7b-3790-b098-40447948864f | -16.9405 | -55.82804 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| e210f8fc-ae3b-3945-9967-f9f35427a171 | -16.94017 | -57.70029 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 4de4e2aa-8925-37d1-901a-2e6097a2c21b | -16.93256 | -57.68883 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 17291cf0-32d4-33c6-a94d-8c61ae2efefe | -16.87831 | -56.73271 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a679df5e-3ed4-372d-a39a-e88da6bbee12 | -16.86938 | -56.73125 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8923d973-602f-3e92-9c82-cb9031e964c9 | -16.86617 | -57.46003 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d954f7c5-6890-306a-b0e9-18845a1a53f6 | -16.85707 | -57.4585 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| decc707d-99d9-3a39-aec9-7156e01115cb | -16.84996 | -57.80207 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b3c702eb-5082-366d-999c-4fd1d9eec1fc | -16.84838 | -57.8121 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dfb57192-d7d0-39e6-9fb4-5795a39a079a | -16.79593 | -57.50176 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 554662bb-1faf-3f32-972c-b939fb159f87 | -16.78988 | -57.48068 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 0026407e-adff-37e6-92bd-30ad57e9ce0d | -16.7275 | -57.46436 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| df2d71b4-b986-37b2-bb7e-eb4277a3cf9c | -16.71839 | -57.46284 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 65691ab7-b5f2-3231-bfb5-88fb87e5e92a | -16.71486 | -55.92114 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| e3f77439-e78d-3691-8f8b-09aa7c15425b | -16.71073 | -55.94872 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 07ed5f51-5980-32ee-b72c-eedbce0c47ff | -16.70874 | -55.90135 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 1c1f0d12-16a0-3a26-9d80-dc04d76379ab | -16.70737 | -55.91054 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 558f3ec1-bfef-3cc0-876d-379dc9c68cc1 | -16.704 | -55.87237 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 953eb715-b963-3499-87ec-0b0f022dbc19 | -16.70169 | -57.45003 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| e9ea559b-5e75-387b-bd33-d4e8d05b2496 | -16.69988 | -55.89995 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| c8738a40-7a91-3463-aba0-8a68212ca1ff | -16.6938 | -55.87355 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 4fe2c6e6-f7aa-382a-bc74-a493df8b1b05 | -16.69243 | -55.88274 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c3432281-2e89-3642-9063-9f9fcf7757b9 | -16.68951 | -57.46803 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 0f9b3e1d-f48a-3970-b712-1ef0cf7ac406 | -16.66796 | -55.5588 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d6d63caa-bd76-3fd7-a6b8-4b22b2be8a0b | -16.66316 | -55.5298 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e09e2bd4-e643-3dbc-a192-76ee61518557 | -16.6618 | -55.53904 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| d6c933a4-5154-374d-ace5-5692685cb1fb | -16.66172 | -55.90609 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 039455fb-e662-3d27-8330-8205aae49c5d | -16.66045 | -55.54822 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 54b79937-7c9c-3201-8d84-27749334dd2b | -16.65909 | -55.55742 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| b72f63e0-ad86-37b1-bc8f-fd467890042e | -16.65773 | -55.56663 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 40ea7cd1-cfd7-3cb0-95c3-7a7ac674db28 | -16.6518 | -55.53165 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 377dc661-303c-330d-8473-b530e4a04a5a | -16.64908 | -55.55005 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 5808c768-ba1c-3a87-8e16-3c8465ed562a | -16.64772 | -55.55927 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 91deea1f-5e33-3dbf-99e3-0a8abd262960 | -16.64399 | -55.90329 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 533be8e2-94c5-3a20-bbba-329da65f9be4 | -16.64262 | -55.91248 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 98f3fab4-1643-3876-b581-348e63fa44d2 | -16.63592 | -57.16487 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 4dcd81d0-e3dc-31d2-9afb-663d0a9d03af | -16.63375 | -55.91107 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 3311ef1c-3655-34eb-9a48-1ca2b03dd5e0 | -18.8952 | -54.5494 | 2024-10-06 05:53:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bd5c5287-4806-32f4-8310-97eb60703f41 | -18.73932 | -57.35598 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 8e691351-cd78-320d-9166-f9a3038c8af7 | -18.73785 | -57.3655 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 6fd83bd0-1ef7-3bb5-8549-537ba4693b61 | -18.72888 | -57.36399 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.6 |
| f6b60566-f154-327f-abd5-ee401111a422 | -18.69848 | -57.26442 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 22adb3a7-4e41-3071-83bd-8709b962919f | -18.68954 | -57.26291 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 363d9f60-e55d-3009-8d48-6fbdc7c71812 | -18.68059 | -57.26141 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 6a60a29e-961f-3a76-bf64-1f4e942749dc | -18.67164 | -57.25991 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.7 |
| b6d56a04-9313-3ddb-9ca3-ba9c991760d9 | -18.67018 | -57.2694 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| f7307c0f-c06b-305a-b229-c38cad6fc3a1 | -18.66578 | -57.2979 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 2fda87f3-727d-3d86-afb9-de5d20798a71 | -18.66123 | -57.2679 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| f9299f8a-8518-37fa-a706-7a959df2ad54 | -18.65976 | -57.2774 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.1 |
| f4478c6d-b1e6-3563-8d39-451c52501fe1 | -18.65081 | -57.27589 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 97017a15-fa51-306e-b4fb-57d5c8364861 | -18.64934 | -57.28539 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e1825054-abc9-3dc0-b19d-fccc8dcd647d | -17.86789 | -57.67673 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a427843a-f3f1-34e2-9f00-9be9bc95ea3b | -17.86635 | -57.68653 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| fb9c2f85-0729-3663-9e6c-2504e6683bc2 | -17.85725 | -57.685 | 2024-10-06 05:53:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 55b26976-7cf5-33e3-8e40-281a9a4783ba | -16.54946 | -49.19803 | 2024-10-06 05:53:00 | AQUA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bf1b8407-247f-3b55-9393-919f1706455c | -16.54695 | -49.21922 | 2024-10-06 05:53:00 | AQUA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b749d81e-57f5-3eb4-88e4-57c87e41c77c | -13.53194 | -48.62214 | 2024-10-06 05:53:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 62972e08-1c64-3795-8148-f2875bc9a0d1 | -13.53003 | -48.63642 | 2024-10-06 05:53:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d95335bb-a725-35b8-bd31-a419714da59f | -13.11162 | -46.34328 | 2024-10-06 05:53:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |


[Clique aqui para ver as próximas entradas](README151.md)
