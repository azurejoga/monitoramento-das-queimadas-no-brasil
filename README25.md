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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ebc8bbc-889d-379b-aa3b-e18e6425a778 | -6.50087 | -43.10664 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c57da153-406b-3edd-b60a-6cb3175318fd | -7.61418 | -45.27146 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7e71abf-1916-3a4e-9e42-44e8b8627f21 | -6.80508 | -50.08917 | 2025-08-21 04:17:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 636fd0b6-d365-328e-9918-8aeff9bb1a2d | -7.60592 | -44.39059 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e46294-dc6d-39a1-86f9-183693a59272 | -10.2759 | -46.76171 | 2025-08-21 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fa0cc2c-0bb0-3faa-8daa-ae347f245301 | -7.63568 | -45.24786 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a6aaea4-fa38-3fe2-9b4b-883672cd660d | -5.98149 | -42.83982 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac00c2c6-babb-3c95-b16f-9fb128b41f5f | -6.56878 | -43.00005 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54b1fe9e-4b0f-3cec-8a39-7948e01d4a72 | -12.52252 | -45.60006 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c88c619-5805-389d-ad9d-e494a4ab4eac | -5.96103 | -44.14352 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f54c4f78-4c89-3654-a2a6-0b5da58f9ba7 | -11.30337 | -44.95152 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbd46eb8-2b8f-3284-9714-cdc9a58e80d6 | -6.86435 | -43.61014 | 2025-08-21 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f84adaab-351a-31b9-a023-b62645348a24 | -8.82225 | -47.47272 | 2025-08-21 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3462430b-f095-3a15-8ba1-ae259c0b2205 | -5.22081 | -47.46896 | 2025-08-21 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 851966c6-5ebe-35a9-9ab8-5e1759cb3264 | -6.22379 | -44.12264 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09e4b26b-498b-3487-8a65-c3e934cd87aa | -13.3256 | -40.34369 | 2025-08-21 04:17:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb88092d-84f0-393f-b261-4c73164082a3 | -13.01822 | -45.17161 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 83b38846-e436-39d6-b72b-ada4dea9109c | -6.35891 | -44.64865 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9fd484a-93f5-33e1-829b-522ea99f178c | -6.49489 | -42.97774 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb061bd4-9f70-3c17-8e67-2cf4085a73b3 | -5.44403 | -45.10023 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1c1c5bbc-63dd-3089-a2c1-b4622901bf85 | -8.79688 | -45.43233 | 2025-08-21 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edfbcf15-3158-3ae9-b66d-06268729a0fb | -5.7941 | -45.07545 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cedaea3e-11a8-330e-af1d-cc2f66adc5a0 | -12.98243 | -45.20233 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8a37b81-962c-310d-8722-2bb2b3535532 | -7.19316 | -45.17426 | 2025-08-21 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45f8b7bd-af74-3c25-88d6-9b7b4c97037b | -10.72392 | -48.24703 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6337cb1d-f6a2-37cc-98eb-89f09fb2e17b | -8.83918 | -52.03962 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19325e49-682a-3211-8c69-136c45c4345b | -6.39475 | -47.33963 | 2025-08-21 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fc1e78e-e7a7-33c4-b35b-544bc3d2e07d | -8.30358 | -49.02748 | 2025-08-21 04:17:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d90dc5cd-13c3-37a1-b4fd-bef24a2ed557 | -10.39097 | -42.5818 | 2025-08-21 04:17:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d6599f7-3025-321b-8ee1-89d1be6b7108 | -6.04316 | -44.35234 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bf9c224-3af9-3b4d-aacb-7649aa4b5433 | -6.08102 | -44.42117 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7d791c5-f3d3-382b-9d52-9150b3ff7ced | -7.5019 | -46.03078 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac568e1a-99b6-33da-a559-eeaf05fc4c9b | -8.84886 | -52.0444 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feaa916b-1ab9-3bb3-b72c-1b253f20c152 | -8.07241 | -43.67733 | 2025-08-21 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94198f4f-7ade-3f54-be02-0d66fbfad850 | -13.01488 | -45.17105 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a0a6f72a-ca75-3e24-89ba-1195bc7484df | -6.77535 | -44.33887 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 105d500e-fb59-3c9a-8a9a-aab070b28522 | -6.1932 | -48.10292 | 2025-08-21 04:17:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aec6258-704d-33db-a859-6fd9bc69e53d | -7.86406 | -46.73291 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dd767b9-9572-30a1-b925-67b4c84700db | -6.1133 | -45.42249 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46dd0064-5f90-322c-82fd-0bf4aaa072bb | -9.01566 | -40.34232 | 2025-08-21 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b817236-9c5c-3c51-8bf5-4e6890568eda | -6.77592 | -44.3353 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a0fdeec-6ace-3dfb-ab0e-a071cfc81a60 | -9.87445 | -45.97971 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4efbb630-ad24-3d32-b65d-244880d2f548 | -6.01595 | -44.37028 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ba9737c-c614-39ad-ad4a-1a0d93fdd6d2 | -12.09008 | -44.7304 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bef159b-b275-3a1e-8320-2ceae198c309 | -13.3301 | -40.33953 | 2025-08-21 04:17:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c2757c8a-7dad-3e72-8eef-605fc54fbfc1 | -6.5935 | -41.39313 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d22f48e-6ae7-33ce-be76-9a65da4dedb4 | -7.118 | -44.66429 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2d2f697-e769-3a12-a1d1-37bac44cdbb3 | -9.55906 | -48.11336 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d111cf6-55c1-38cb-aa84-bf6e4eaded69 | -6.41853 | -44.66963 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7c29099-3234-3a9d-8f11-38698617d3d5 | -6.10199 | -44.63855 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 822e9387-2b06-3e88-8be5-164e53c38601 | -7.56941 | -44.40298 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f38dc90e-1b29-340d-95e1-96c16d95cc95 | -5.96045 | -44.14712 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dec56f50-12db-36dd-861b-f742da37133e | -6.21228 | -43.33111 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96dc2517-e731-3642-a72a-e22dadcfe0e0 | -5.87735 | -42.40734 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc1b6799-023c-3fb4-821b-c5a39e7f2e64 | -6.02933 | -43.77916 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e8999f1-cacf-3723-9840-7cdcf78e515c | -7.20781 | -45.31192 | 2025-08-21 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f84d2457-c98f-352e-ae96-69cb77ff633d | -6.42772 | -45.4878 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee06f998-ed9a-3ac9-bafa-69da8569b857 | -12.64561 | -46.86839 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7716abf9-4aa1-3769-b1af-d22793612e48 | -7.70629 | -44.02128 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9adcbe29-dafa-30dc-90f3-3a252d410988 | -7.41967 | -46.8683 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d462c137-c484-3f2c-8cc6-cd70c584e1ad | -6.42311 | -44.6629 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e9314e0-2e49-3b1d-87a9-a5d36d35f955 | -11.3792 | -48.99574 | 2025-08-21 04:17:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22ca6e6c-b73a-3e88-892b-a882891d44f6 | -5.97172 | -44.14156 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71361c94-c4b8-3432-ba33-39e316eb2d5d | -5.98863 | -42.81609 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 777da92a-33cc-312c-b866-a04777337153 | -10.98708 | -55.23812 | 2025-08-21 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 278c4a68-f2df-389b-8a28-e54f3aa7437c | -5.9644 | -44.14406 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c46852f6-4b15-3fb2-944f-504f6b64dc72 | -6.16358 | -42.71564 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cea9dcf0-ff84-3007-805b-f0d3b216c0a5 | -9.47809 | -47.32579 | 2025-08-21 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a56c9a9d-e9fe-333c-ad04-e6065d4de1f0 | -7.14296 | -44.18104 | 2025-08-21 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaec309a-6dc9-30cf-a3ff-405decae6862 | -7.14929 | -44.6431 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10fe82da-c601-37c4-83d5-653248bcb1f6 | -6.3521 | -44.64748 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae7410e8-8d27-36e4-a50c-1c5924bcf7c1 | -6.95534 | -44.18041 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14300581-ad2d-37ec-bbaf-247f3e91650d | -7.63101 | -45.25494 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f08e7c8-9f80-3838-b7f7-6207cbec843c | -6.17757 | -44.73428 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8df6d10f-ff1e-3062-8919-e37e7c8ddf6d | -11.57932 | -47.00594 | 2025-08-21 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de5a2229-b8f9-389e-bc35-18a4c04ff525 | -9.86342 | -45.98169 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62496a8f-ccb6-33be-850e-aa05390f4c6c | -8.17855 | -47.32743 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1394a408-095b-3f0c-8a61-6c58651376df | -6.01028 | -42.85145 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2eb5522-0c00-3953-acc3-f418a1b34de5 | -6.58396 | -44.46785 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 763eee6c-5351-3c36-9c50-b636f402c21c | -7.41892 | -46.87276 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d7f2161-ccb6-3fb8-b994-81d89dd2b0b0 | -6.28968 | -43.69066 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff465a9f-0ba5-34ca-bc3d-78bb8531d229 | -9.55845 | -48.11637 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17ada4d8-9f87-368d-8b24-543a76c36921 | -12.67068 | -44.95699 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26f716e1-2a58-3f86-baba-d820e924c432 | -10.58999 | -52.28454 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0dc81a2-3a2a-3950-b253-0563e63ea21d | -7.03095 | -44.62005 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d7772e00-9c4e-3e7a-931f-a32a2e0571f2 | -8.1528 | -47.34196 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d81cb8f-6400-31c3-bc49-97d2e07188cc | -5.88016 | -48.1147 | 2025-08-21 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1b3fc30-1671-34f6-8696-2316479f279b | -5.75369 | -45.30349 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f437988-3f02-34aa-8e03-4e6d151c395a | -5.95486 | -44.13882 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb0c0765-352a-3582-9599-3b3e73b88a74 | -7.58633 | -44.38369 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 689dd076-ba29-3cc4-9ad8-65124b0519e6 | -5.96886 | -44.15954 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e28248eb-5502-3a36-8717-e9b4aad11b95 | -11.29128 | -46.28381 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 713a3b16-be33-370f-8ddf-d60108f9a92e | -5.80374 | -42.93922 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2c71657-b042-3e28-8a02-99dcee7d87b4 | -6.4979 | -43.44795 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d7597fa-96ac-310d-9fa7-f5cabc16ab3b | -8.2921 | -47.61673 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba32b051-1dcb-3caa-8f92-34156b7868e4 | -7.79023 | -49.32399 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe45ef81-55ef-3f55-b40e-953289a65f19 | -9.72703 | -45.6206 | 2025-08-21 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bceb728-186f-3cb1-a906-4feec778f905 | -6.49435 | -42.9812 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1ffebd0-2cd0-3d82-b31a-0ac12b0c5a72 | -5.79884 | -45.00189 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9074567-9d7c-33f3-8d01-4eba1096b6e5 | -12.08265 | -47.90753 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
