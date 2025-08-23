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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e617abc-0c48-3ed9-84c5-77e993c77a68 | -14.72993 | -55.38184 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 03760d27-a5dd-3d3d-9816-cba0e591b471 | -14.30392 | -58.55494 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26f86c75-3d51-3ecd-9945-91c312c37034 | -14.76394 | -55.98702 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baeccefe-e328-3b6e-9c7f-ccfdf22461b3 | -14.25905 | -58.54015 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e20e2945-35c2-3b93-81c9-ce4022b0413e | -15.54369 | -55.01548 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5065814-9569-35db-8452-29f12d30b90f | -14.75217 | -55.99231 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dd00e95-dd73-366d-b92e-9aab209ed1ce | -13.02185 | -56.8218 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9cb8252-bf29-36fd-b1da-b352e8ddba30 | -14.26452 | -58.5377 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c66ea796-1b9a-37ba-8dc6-88c1e4d1d95b | -14.69321 | -54.90937 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b7316fb-788f-339b-a2d8-8982a8eef227 | -14.75295 | -55.40513 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc8a2ffe-1abc-39b3-9eb4-1115e0e7c425 | -13.02513 | -56.84199 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 574f52d9-dfd4-30db-91ac-008b22f892c7 | -13.0256 | -56.8381 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0131915-a893-3dc2-9704-7acadf07dd89 | -13.42763 | -57.17303 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7a09108-da44-3e15-bd94-430c2a7f2f21 | -14.67367 | -56.61307 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c219450-8b8b-3a39-ab55-84dabd6a81fd | -14.33225 | -58.57727 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c11934c2-cf6d-3c82-8d7d-40aabdb507f1 | -15.02952 | -54.90239 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 891bbd64-9e84-3743-bf03-66a22f9a6074 | -14.66547 | -56.58582 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0cc0c05b-9bcf-36ad-af60-ba43cd9c8efd | -14.66498 | -54.92909 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 309ad7ee-51b7-3071-a5ba-4d1052f3fa05 | -12.58307 | -60.34776 | 2025-08-23 05:44:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce581535-59d9-3b4c-9ef3-dad52107e081 | -14.26489 | -58.53458 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9c9a143-c638-32db-b1ec-d647cf4d4832 | -14.6704 | -56.58871 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f35c2af-eba0-3903-9364-0bb8dbb808c8 | -13.03265 | -56.82701 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4068367-8709-3e54-9c68-d5e9a7b0a421 | -13.01997 | -56.83743 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98c3b62a-0314-3f1d-b8ff-7c4ca04c87fc | -13.68497 | -57.75658 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4a340fe-2042-3619-b477-e53cdca9cb17 | -15.0342 | -56.38099 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80883dce-6b35-3859-9f60-f6e0431a1d05 | -14.28311 | -58.5556 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1cdda6f-3466-304c-9e1f-76ab43cd5a61 | -14.81293 | -59.62809 | 2025-08-23 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e252719a-fbe9-3b4c-8804-249376bac3dc | -13.37241 | -54.40221 | 2025-08-23 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84913366-5d51-31eb-a31a-4809763377b9 | -14.61349 | -54.8554 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8837f80-fb92-3b40-ac70-fb7f37075e99 | -14.67067 | -54.87368 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a47073c-c45d-3bcf-a2c9-05f7b9b52d02 | -14.76478 | -55.9892 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0dcac20-e57a-3d96-8647-ab50df79dc5f | -15.58889 | -54.29406 | 2025-08-23 05:44:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7636fe64-4434-3f21-9424-67658c835511 | -14.66456 | -56.58805 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfb5a80c-24a4-318c-8bdc-383caf4713ed | -14.69915 | -54.91524 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4603110c-e7d6-384a-b625-62de2d9da60e | -14.29881 | -58.55427 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42af6658-2b48-3ce5-8b71-db95204d4291 | -15.05657 | -56.39662 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 451ae537-113d-39d4-80af-d9dec9af5e71 | -14.28611 | -58.53071 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba4a8fbc-c512-3206-8b52-83a65219a49d | -14.27 | -58.53521 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd92d2c1-4b08-3123-b9ad-43c3d0a9d127 | -14.27587 | -58.52952 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88dc540b-4493-3816-aabe-e9b6a1b83fb2 | -13.68716 | -57.75527 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55c75a69-5e25-3fb2-bebd-5c7060a869a8 | -14.85813 | -59.61658 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c793c0-1ab7-3f87-ab9b-a030e6777f04 | -15.03034 | -56.38201 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a7d4edb-4117-3984-94b3-53be4ab131cf | -14.67205 | -54.92404 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dccf72c7-380d-399f-bbff-d497eaa30cb8 | -14.28285 | -60.38876 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4e643a8-04fb-3102-9d98-bc77c2232fb3 | -14.858 | -59.6189 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dc0f897-2274-30ed-bb90-850182ac8087 | -14.28687 | -58.52443 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0fd0dc8-2105-3a3b-bc64-73a0a48c8a74 | -14.99921 | -54.8772 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba3178f6-88cd-3da8-95ad-23f6f6e73947 | -12.58688 | -60.35283 | 2025-08-23 05:44:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9ce61a6-12e9-36d4-a11f-f4ab058817b5 | -15.01925 | -54.87447 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a19bd04-1343-3252-8abb-6561d7e2cfc5 | -15.06205 | -56.4015 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6defc567-84e3-39df-99c5-80bfe19af07b | -14.68017 | -56.61222 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90b30ee1-d5b4-375b-874f-05ddb5c711f7 | -13.02138 | -56.82571 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cbbe7cb-53f6-3d9d-9a4f-a8567d02f818 | -14.34129 | -58.5878 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 18389050-f7d9-3048-bf9e-ad9045f9bbff | -14.28649 | -58.52757 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77532de5-f31a-39c4-924b-ab6afdb990c4 | -14.28344 | -60.38419 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 48ab9da2-4748-3b10-91db-664ceacd9b9f | -15.01333 | -54.86794 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c1e6249-73df-3238-8a51-33fba8eace05 | -13.02701 | -56.82641 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd6feb89-d369-3147-ab0e-da50363a987f | -14.75735 | -55.99095 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01c0bbbb-cff5-3138-8233-edd71ddc510e | -20.4042 | -45.592 | 2025-08-23 05:50:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ada6767b-196c-3c76-8e11-20ee168222f0 | -9.9492 | -60.2141 | 2025-08-23 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 31203548-bd18-3613-98a6-4d503d1c2cbf | -9.968 | -60.1937 | 2025-08-23 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| c23141f6-ceed-359b-b950-0b13735f7a8f | -9.9493 | -60.1947 | 2025-08-23 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 204.3 |
| 17b3f438-64d7-3df1-8c3e-defd6c207d5b | -9.9495 | -60.1754 | 2025-08-23 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d76e394d-f953-3596-9b60-3ad8beb63e0d | -12.9921 | -45.2252 | 2025-08-23 05:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c03e230d-1d38-3e2d-a3bf-a2324b91122d | -5.7614 | -57.6002 | 2025-08-23 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| d7226423-0bd5-3a93-a4c0-ba0a4947012e | -5.7615 | -57.5807 | 2025-08-23 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7e231502-988e-3ab9-a0a6-2f9ec91176d7 | -20.4035 | -45.6162 | 2025-08-23 05:50:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8ec65201-fb3a-330b-99b5-556d296d9d52 | -5.7431 | -57.5814 | 2025-08-23 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d72afa8f-60c3-3002-bf08-f7cbb09f1129 | -9.9681 | -60.1743 | 2025-08-23 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 66cbca41-926e-3dc2-b011-12f7f02e70bd | -5.7429 | -57.6009 | 2025-08-23 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| da0f9388-b9d8-37e2-b686-33544c526af2 | -9.968 | -60.1937 | 2025-08-23 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 83500408-8685-3f00-8741-c849bfbbd901 | -5.7429 | -57.6009 | 2025-08-23 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 2a0a0b88-76d0-3035-9406-ccc83a08f12f | -9.9493 | -60.1947 | 2025-08-23 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 79820328-d811-340b-a659-85f35a4fa44c | -12.9921 | -45.2252 | 2025-08-23 06:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c41e9e65-a4cb-3dc7-960e-26be14cb9b72 | -14.2742 | -58.5466 | 2025-08-23 06:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 36d3a5a6-e6a6-35ae-bda7-32473cf0f36a | -5.7614 | -57.6002 | 2025-08-23 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ae6647e1-3d90-3533-99ec-c878b892f561 | -5.7431 | -57.5814 | 2025-08-23 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b8bbd372-6093-38d8-93b3-78476cabacd8 | -5.7615 | -57.5807 | 2025-08-23 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0d7831c0-d4b2-38ef-9b85-3c33adc1a6a4 | -20.4035 | -45.6162 | 2025-08-23 06:00:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 54bafa47-153c-3c86-88d6-0ad23c24255e | -14.2744 | -58.5266 | 2025-08-23 06:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4f7e416c-c757-3554-9b06-e777ff86f3cc | -9.9492 | -60.2141 | 2025-08-23 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a5cadb04-5bd9-3236-ac20-e6639d7a824d | -9.9495 | -60.1754 | 2025-08-23 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d99cf5ab-2de9-3284-97ff-e295f83803bb | -11.1208 | -44.7449 | 2025-08-23 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| a63a98e4-710e-3ad5-888e-494d39382751 | -14.2936 | -58.5249 | 2025-08-23 06:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 1ab14139-d62e-376b-af0a-f3fc817a528c | -9.9681 | -60.1743 | 2025-08-23 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 61ed2a31-b97c-36fc-8339-a1482664bbf4 | -14.2553 | -58.5284 | 2025-08-23 06:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 0a8b473b-db5c-3cf8-931d-ce4770f5f854 | -14.2744 | -58.5266 | 2025-08-23 06:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| e21a9a27-cc56-317d-a3fa-5cc98b4dab76 | -5.7431 | -57.5814 | 2025-08-23 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 20f25ffc-8e17-3dff-b177-dc4bd4c028df | -20.4035 | -45.6162 | 2025-08-23 06:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b06a06de-d1f8-331c-9eb6-f831675d38e9 | -5.7615 | -57.5807 | 2025-08-23 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 20e6bc83-b8e6-3d79-b6b8-30bf802abad5 | -14.2742 | -58.5466 | 2025-08-23 06:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 04087764-50f2-3aa1-9d78-0a60c7e06b67 | -9.9495 | -60.1754 | 2025-08-23 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4c298a65-9a93-3314-81e1-f4507b669e0d | -9.968 | -60.1937 | 2025-08-23 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 692a0e70-57e0-3dac-b6da-949a9afb52bc | -5.7614 | -57.6002 | 2025-08-23 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d9ec0680-d45a-34d0-80a4-92c53a39f4e7 | -9.9493 | -60.1947 | 2025-08-23 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 636c13b1-9508-3445-83a9-ee923fc66f53 | -9.9492 | -60.2141 | 2025-08-23 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| f978632b-8252-3876-b170-2acc24897d54 | -5.7429 | -57.6009 | 2025-08-23 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 850fa0e8-83bd-3c3a-ba51-f184321f0fce | -20.4042 | -45.592 | 2025-08-23 06:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cde381d9-6070-3f35-9b90-e8958b636151 | -12.9921 | -45.2252 | 2025-08-23 06:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7a9bbc94-3727-342d-a2a7-3d4851364a7b | -7.0164 | -44.6413 | 2025-08-23 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README82.md)
