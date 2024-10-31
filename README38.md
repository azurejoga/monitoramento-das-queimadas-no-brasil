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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c5cc69-1cdd-3565-bc02-d649f57f5f61 | -3.04456 | -53.23686 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af0cecf2-0b1c-3a58-ab91-e3eb928104b4 | -2.99676 | -52.37697 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 098e3bf1-a2b8-3adc-83d3-149a6262ef6a | -2.994 | -52.37299 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee7f828-20da-36aa-aa05-ae6b2679d954 | -2.99345 | -52.37645 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5ddadeb-b592-3144-b087-1e83463d2de3 | -2.99123 | -52.36902 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4d24bb8-d8d1-3993-9fa1-b4c13d43f061 | -2.94618 | -52.56707 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6db554f-d4d3-3f38-86df-5824f2391b26 | -2.94564 | -52.57054 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85ae9ea5-1424-399b-b1d6-b937aa8a559d | -2.94287 | -52.56657 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe535cbe-f3ed-34c7-809e-d2ba3c367be8 | -2.94064 | -52.55915 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4b49534-ddb1-3085-a50a-54baa8f32eb2 | -2.94009 | -52.5626 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3b191fc-cd11-3cf4-b7ef-f68378c6bc64 | -2.93732 | -52.55864 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 702866bc-a876-3423-8102-e44686ffdda6 | -2.93678 | -52.56209 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36fa1b47-3cc8-3fce-bbcb-b7b379d31ef1 | -2.91087 | -52.5971 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c308bbd7-579e-3f25-907a-dae99204866d | -2.91032 | -52.60056 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7074822f-ceaf-355a-8e18-3ebedc12f446 | -2.90755 | -52.59658 | 2024-10-31 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d1e000c-fa83-365f-b71f-f54b696d5660 | -2.86984 | -53.32747 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e9604ca-684f-3210-bb79-98bf62f6fcc3 | -2.86648 | -53.32692 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f3dbe19-221e-3c37-8d40-96c0b7a071ee | -2.85689 | -53.34375 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2c593a4-26d1-3131-bccd-d884a18b339a | -2.85352 | -53.34322 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93bd3083-e7c7-350d-88c2-c914f34efd45 | -2.85294 | -53.34683 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0d2adc4-8137-30ad-99c5-7e56731534e0 | -2.85014 | -53.34269 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad3d7ab8-b537-3d40-b051-e4f6eb9aa527 | -2.84619 | -53.34578 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b406c9-ff68-38f9-bfaf-1201342305c7 | -2.84561 | -53.34942 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9c2dbeb-763c-35e3-89cc-9c0e3b1d36c8 | -2.84282 | -53.34524 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69ac2e8e-4187-37b6-9d0a-a5d3397a0795 | -2.6212 | -52.45201 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee4e8a3d-2bf4-3741-9401-b0de44cdb304 | -2.61788 | -52.4515 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea8b3c5f-39c3-3ae1-8978-51d7ba1b71ef | -2.78302 | -52.09249 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e8aad34-f5a8-329f-bbcb-dc8523e9d85e | -2.78248 | -52.09592 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7b0eba5-1317-3697-ad33-e1ed996095d6 | -2.77972 | -52.09198 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a658288f-d516-36c3-bd14-76bf6d89d96f | -2.77918 | -52.09541 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f18b3847-ce76-34ab-b3b4-1df484a26d84 | -2.76038 | -52.06433 | 2024-10-31 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17dffd8f-ace3-3f4a-b871-e8b8c504b33e | -2.24183 | -53.72421 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9562aee2-a564-3284-9b17-bbaba30ce4f1 | -2.24064 | -53.73165 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a628cdca-15d1-3e7e-b176-81be59319b63 | -2.2188 | -53.67165 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da9b91a5-8a43-380f-9944-739c6ecf0eb9 | -2.20317 | -53.72633 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b5ffd6c-749d-38b1-8469-607d57ebbe36 | -2.20032 | -53.72208 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47f8f41b-2d52-3a4b-bdf0-709f74ffa7fc | -2.19974 | -53.7258 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d23a45-80be-3e57-bc03-4b6a73200f03 | -2.19806 | -53.71415 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69629fd9-3715-3aa3-be4d-58d65a73c066 | -2.19748 | -53.71785 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a67f9e46-75d4-3bf8-9bde-1b5d82f7c6f1 | -2.19689 | -53.72156 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f3afd99-0fd4-35e4-be92-e3c146589c0e | -2.19631 | -53.72528 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5366894-7d78-3e62-8b96-50c54a83409d | -2.19463 | -53.71362 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89d15a2a-aee1-3636-a096-8325d8680567 | -2.19405 | -53.71732 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c9e3077-bd88-3266-bafd-9ba72729c156 | -2.19346 | -53.72104 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c925019c-6f9c-3230-9215-7ea1c8e6b478 | -2.19343 | -53.58819 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6259923f-c596-3a6e-8bb2-45f5f9b01bc7 | -2.18943 | -53.59137 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 86c76128-1aca-3a5b-bffe-581d2a82b94e | -2.18601 | -53.7237 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34c207d-9310-35c9-9a2c-0e12a3e38a81 | -2.18542 | -53.72742 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdcd0e00-cd9d-36e6-9e8d-1a5f51eedac5 | -2.31643 | -53.9819 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5df204ae-4c64-3f6a-86f9-8c78cfd7f7ce | -2.31297 | -53.98136 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31925222-6b36-39a5-9862-17c1a083ccd4 | -2.30916 | -53.60962 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46fa8be1-0fca-3876-ad37-8f708d2df3df | -2.28907 | -53.64803 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69473601-0416-360a-8b64-6815412f5748 | -2.2741 | -53.78666 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6d34ab9-8ff7-3366-a418-47cefc171954 | -2.24526 | -53.72475 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76d227b0-f57b-321b-87fc-2cec8ca1a9a4 | -2.94261 | -53.70629 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33aacde2-240c-3409-8718-cc077cec3634 | -2.92051 | -54.19415 | 2024-10-31 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec1bd49c-aaa1-30c5-af84-cbb09c9f461e | -2.9199 | -54.19797 | 2024-10-31 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f1c1ead-3a80-3704-b8a8-78391db3fa25 | -2.91849 | -54.19418 | 2024-10-31 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 025d80d7-c2b7-3ef8-b475-32e04594376f | -2.91704 | -54.1936 | 2024-10-31 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c1d3829-9380-3cf9-8873-427cf0c9f31d | -2.91502 | -54.19363 | 2024-10-31 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f21c333-b3a4-38b6-9388-db01b400a4ad | -2.87162 | -54.10854 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d61912c6-6bc8-3b4b-9f6b-fd7706cd8faf | -2.87102 | -54.11233 | 2024-10-31 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a126092-07a2-3343-9353-c09319a79737 | -2.86978 | -53.96503 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 796cc284-d6e0-3b5f-a96f-0c3a10aa901b | -2.83983 | -53.98081 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c09a14e-0bb3-39c9-92f7-e268a187656c | -2.62403 | -54.00896 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f6a28e9-f7b7-3414-9d2e-06b455693109 | -2.53279 | -54.07738 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f57995f-b4b9-31d7-9326-820ded0e15d6 | -2.50341 | -54.12746 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f780471e-2e68-33c0-9661-5d52c851bd43 | -2.5028 | -54.13128 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15324822-3328-3936-9a4a-f368065b619a | -2.49993 | -54.12694 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 304c1beb-d1a5-34bd-850c-f03e86afb191 | -2.49932 | -54.13075 | 2024-10-31 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72471731-7201-34d6-80ae-0f0a01fe1842 | -4.01866 | -54.79851 | 2024-10-31 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67850628-15fe-3f8f-9b18-531d785e3091 | -4.01836 | -54.79952 | 2024-10-31 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64685fa8-a930-385e-a944-0b36b4eaa6c4 | -4.018 | -54.80253 | 2024-10-31 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cccacca6-59a5-3c8d-b7ac-b544b303666c | -4.01772 | -54.80354 | 2024-10-31 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 450b19f3-4182-33fb-8278-b1c82cfaa87f | -3.9784 | -55.38691 | 2024-10-31 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a612d0a-bfd7-329e-a49a-11a0622911c5 | -3.93919 | -54.86442 | 2024-10-31 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa0662d8-06b5-3394-a16b-c75425274ebc | -2.1321 | -55.77446 | 2024-10-31 04:49:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3e6a437-389b-3b0a-9925-e3cc1b708630 | -2.12933 | -55.7717 | 2024-10-31 04:49:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b767393-045c-39d8-a439-57e61028e81f | -2.35416 | -56.51085 | 2024-10-31 04:49:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f2f4b91-c790-36bd-95fb-ac5a107ef300 | -2.35102 | -56.5051 | 2024-10-31 04:49:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58ccbfb5-d83f-374f-804b-acad246094a5 | -2.35019 | -56.51021 | 2024-10-31 04:49:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c9f2ca6-5e55-3bc1-9f65-c984a1278d8e | -3.49788 | -55.41615 | 2024-10-31 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9b2b4184-c7c2-3dc6-be33-a970fde79d65 | -3.4648 | -55.46106 | 2024-10-31 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecd3c4fe-0569-3c5d-a80a-0d35ff2e39be | -3.91146 | -55.4542 | 2024-10-31 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7c15887-10bb-37c7-a7ea-ba2e75197150 | -3.91113 | -55.45586 | 2024-10-31 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d0cc87b-7b99-3abc-9f1d-4a3a8496f5d6 | 4.96853 | -60.30852 | 2024-10-31 04:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76c54bc9-fd83-383f-b2dc-6d4181b6f385 | 4.9679 | -60.30402 | 2024-10-31 04:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b828692-5936-303e-b18f-b22000b8aba3 | -7.77129 | -63.34837 | 2024-10-31 04:49:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38e9aa22-b72f-3218-9f41-ee6f869d884b | -7.77057 | -63.35245 | 2024-10-31 04:49:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fbdc001-d438-32f7-b3f1-81124ab736cb | -7.47607 | -63.49408 | 2024-10-31 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03aab77f-6bce-364d-8f5b-58738ae52290 | -7.47531 | -63.49825 | 2024-10-31 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe8a5b8-af22-3a19-8ef4-11ae6a95ff35 | -7.47025 | -63.49297 | 2024-10-31 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae9e0fc9-5a03-384b-8782-5050becab991 | -7.46949 | -63.49714 | 2024-10-31 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36178ab2-d236-3b64-aa4e-7c8dd0f9a978 | -7.46872 | -63.50137 | 2024-10-31 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46df6268-112b-3bf5-852d-bf987185d3b0 | -7.46795 | -63.50557 | 2024-10-31 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 721b380f-0032-3a80-a8df-b5d8bde5905d | -0.66992 | -62.93184 | 2024-10-31 04:49:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e266b35-e191-3528-9688-885738631536 | -17.01234 | -51.26888 | 2024-10-31 04:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c8f44a2-950c-34c2-ae27-95bc3b07d206 | -12.78798 | -51.52322 | 2024-10-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9518f31-db6a-3996-8e90-068332fb8120 | -12.78707 | -51.52417 | 2024-10-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90d21bbc-b228-3cd1-bb94-4729fc7b3d3a | -16.34069 | -53.35318 | 2024-10-31 04:51:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README39.md)
