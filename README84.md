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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47807c6-4b3c-3831-a656-54aaa5eb5b11 | -3.56438 | -54.67331 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 406dc65f-d4a3-30e4-a686-2283850a56de | -3.55374 | -54.43727 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 283b6f11-c7ad-3081-a73b-ae6906fb6b54 | -3.54693 | -54.76265 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 904fe9a6-e9b6-3909-84a1-acb86c509883 | -3.54687 | -54.74141 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21971b85-21ab-312b-9db2-6f77884f2e65 | -3.5436 | -54.76213 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce93cf0d-d59a-3567-83dd-02473cefb285 | -3.54354 | -54.74089 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e6ff2db-a2b6-362e-9d61-66ceaccd48a4 | -3.53974 | -54.76508 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74c874cf-7bc8-3468-a39a-34ad9cb94315 | -3.50668 | -54.62891 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ed4ed80-528e-3c61-a574-cd38276ba1bd | -3.5004 | -54.4363 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c1c709e-6f82-3bfd-8d7e-f1afe0b40fb1 | -3.49707 | -54.43579 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd4d6b2d-ab38-329d-8ba0-265be5b507a5 | -3.47525 | -54.5745 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5013c2a2-da8e-378c-b3da-476956eccece | -3.47192 | -54.57398 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b42e021-746d-3d11-b246-4ac9235b4cfb | -3.4686 | -54.57347 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35671d94-6134-3546-af23-1c94374ddcfe | -3.46859 | -54.82825 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 227848bd-18c7-3092-b22f-e24334a41864 | -3.46805 | -54.8317 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9751e01e-35c3-33b2-af78-6b6d990fe3f0 | -3.46527 | -54.82773 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea36b479-bd99-3ddb-83c8-32a7f9d70e39 | -3.4643 | -54.62246 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 840028f2-ae9c-3d17-9bec-19161449621a | -3.46152 | -54.61848 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31126f0f-baf1-31e6-8a66-90bfeaa84382 | -3.46097 | -54.62194 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f060973-d38b-31b4-8333-1c584010adcc | -3.45269 | -54.63129 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 702d25c4-4cf8-3504-baeb-8f34620aa606 | -3.42931 | -54.58513 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69065d6a-6043-36a6-af80-d11a0eae4097 | -3.42598 | -54.58462 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea1f0ae6-d04e-3733-9404-20974103fbfc | -3.42544 | -54.58808 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5386a87d-5c01-3327-a10a-0b5c4bc66227 | -3.41017 | -54.48985 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eb5c505-6075-3921-a20d-0600e90bb5e3 | -3.40963 | -54.49332 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e18c849d-1fca-31c6-b256-33f9a670806a | -3.67016 | -54.07937 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f89b41-fec7-356b-a7a3-be5cad9fafbe | -3.66805 | -54.07922 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d45daeb9-aa12-359a-8b1e-04c2bd8b2d1b | -3.64645 | -54.17297 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01e26d1f-6ae0-311c-bdf4-20916489257b | -3.59637 | -53.78209 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7786acd9-d299-3528-b44d-a78abdbadf98 | -3.59581 | -53.78566 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fab2b192-2e4f-3a4f-9fa4-458f6076b7c3 | -3.593 | -53.78155 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b3a18946-65e3-3cc3-af9e-ef62ef4c543a | -3.55629 | -53.99356 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21cf87e3-72e8-35cc-b3e8-8afce4f64f34 | -3.55349 | -53.98952 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f828f7-d19a-368f-8638-6af0ff98b353 | -3.55294 | -53.99305 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3078087f-743d-382d-912f-b9a3ab239e6e | -3.50555 | -54.03264 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59aa381f-fee7-3bc0-b792-75ea253272b9 | -3.47298 | -54.15348 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 105baf08-ecaf-3e51-895b-77cb0071d4b4 | -3.47243 | -54.15697 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b71f3e2a-a58b-3d14-acb5-9f2a08ede3b4 | -3.4592 | -54.19793 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7699297d-e34f-309f-84a6-53ee1a47674f | -3.45865 | -54.20142 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f60f5b8-4c2a-35ef-b17d-a5999dee91a6 | -3.45531 | -54.2009 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf458e00-ea8d-3110-b895-83ee87ca9cf3 | -3.45388 | -54.10022 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24d6298e-5174-3e7b-ab7b-fac7cd60b251 | -3.44659 | -54.25684 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e0100b4-41ee-312b-8e4a-15331bde1da7 | -3.44325 | -54.25632 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d070ed2d-4851-32ad-a051-f63c2b687972 | -3.4429 | -54.14875 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79af20d0-ec34-329e-988e-a1d9b63e26cd | -3.4425 | -54.1953 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f5802a5-adf3-3400-aebd-dadcc4ce6e2f | -3.44058 | -54.14848 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60047ac3-c184-3074-b96b-2a269beccb53 | -3.43937 | -54.25929 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 553c264a-5057-35c6-af8c-0dc0dcccfeec | -3.43883 | -54.26279 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0bf6a9f-4827-3fb0-9c7a-d91b18366faa | -3.43582 | -54.19426 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7f123d7-78d0-3fb0-9e6b-6e0d786e5e21 | -3.43385 | -54.27277 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828eb55f-a8f1-3f75-8bbd-27a9272b4e95 | -3.43106 | -54.26876 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1dc18f8-635c-31d9-970d-30e46aae9ab1 | -3.42998 | -54.27574 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92503746-556c-3b07-b352-34dd0db00cae | -3.42331 | -54.14943 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e21f57-954b-3043-ae0a-dfafc05769b5 | -3.41997 | -54.14892 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06cbcf44-326d-3ca4-9936-ecbd31381282 | -3.40362 | -54.05651 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e8fbd34-7a41-3168-9ff0-1caa7578cb1f | -3.40306 | -54.06004 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b37cbc5-d135-38db-a45c-4bafe265c297 | -3.39972 | -54.05952 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| febc82cf-0f36-3f92-b319-7a701fea62e8 | -3.39569 | -53.79841 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e425218-884e-37e7-b163-a03471d9a3ed | -2.38363 | -53.67936 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93b5545b-ed26-361a-b59e-477107f72cf4 | -2.32565 | -53.74265 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8840d9-1117-3732-8f9c-ac739d357c71 | -2.2817 | -53.7716 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 108e92e7-dbb4-3b5c-9b76-e81f93e5e19e | -2.28008 | -53.80372 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e91bfe6-dc3d-35d8-81ea-7b16161a73ae | -2.27953 | -53.80722 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ceccfa7-98e7-31f3-b74d-79dff05004c6 | -2.27835 | -53.77109 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0f0ce04-dc44-3022-8bf0-9a211dd6d0ea | -2.2778 | -53.7746 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dbc9b4d-a46f-35af-b064-5d0b431b25d6 | -2.27725 | -53.77811 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 146c1604-aef4-3f76-87ba-5be6465c0d5b | -2.2756 | -53.78864 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5dd72a8-3874-33bc-9415-9b7876008772 | -2.27504 | -53.79215 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6f000bf-3608-3c3d-8af1-71bf03d84e8b | -2.27445 | -53.77408 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02b3300d-7fd8-3747-b182-f6c8da3f9ac4 | -2.2739 | -53.77759 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9d942e4-e0bd-3e36-afad-7dcd309ed505 | -2.2728 | -53.78461 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e031b4b3-3498-36d4-bfe0-aed7cb41d058 | -2.27225 | -53.78812 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4745c19a-bd0e-3c37-a9ec-9897bc013ecc | -2.2717 | -53.79162 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b93d8cf-c1bc-3f87-977f-480e1deca1bc | -2.2711 | -53.77356 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 903e5900-d333-3ff0-81d5-2458a13c2a30 | -2.27 | -53.78058 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b4f877-aad6-383d-b987-ccd672bfaaa5 | -2.2689 | -53.78759 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e518d16-e90b-3977-9a75-6af215263c49 | -2.26835 | -53.79109 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 425a3a30-f011-38e1-8ed8-a875960255e4 | -2.25202 | -53.72018 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb9c86f8-df0b-3ac4-8f8b-9e6347d9f9d1 | -2.24867 | -53.71966 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbfcacb6-3da6-3cac-9ad5-45054a86240b | -2.24812 | -53.72318 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a9ea2dd-1a05-3c89-bf9f-bedf0e55fefe | -2.24756 | -53.7267 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0d8cc88-5eb1-3458-9c00-3a50baf8588e | -2.24476 | -53.72266 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33bdee79-4795-30a2-80ae-9b12b77dcada | -2.24421 | -53.72618 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74e858bf-6674-3780-b689-f040bc35b2b1 | -2.95492 | -53.87197 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c958744-2c2b-373d-8ad6-f769179bac68 | -2.94199 | -53.70373 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edc8c29b-26c9-300e-a5f1-ea829ecc3914 | -2.94143 | -53.70728 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b51ba08f-acbc-3a5c-8fdd-0e0d7767b268 | -3.59245 | -53.7851 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cd182a16-7f77-37b6-b4a6-ea86948c5302 | -3.58124 | -53.79057 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c2a1a33-d48a-3251-be5f-6076ba79f091 | -3.67351 | -54.07987 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d580e48-92bd-3da8-bfbb-e467a115f2d7 | -3.67071 | -54.07585 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 42bb256e-07bc-3d11-9c7b-5335cd4552be | -3.6686 | -54.0757 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6eb844c2-c99d-3580-abb8-de149ad2c4b8 | -3.65169 | -54.22031 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdcb79cb-0aaf-370b-ae62-41b398d0223f | -3.61326 | -54.03469 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2215bcb5-e696-3c23-9304-13534bf177c6 | -3.61271 | -54.03821 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10023b83-54c5-3d02-a0e1-4c841625e93f | -3.60936 | -54.03767 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4df8929-e452-3048-bffd-3c3380707044 | -3.20869 | -53.85289 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bc25241-d462-3eae-abf1-47b184045116 | -3.20249 | -53.8265 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4738889-6114-36f7-8196-4c6205a86208 | -3.1675 | -53.91876 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f95537-f7a1-3329-b0fe-961251dfb743 | -3.16525 | -53.91119 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6b6c5a5-3856-37e5-a1eb-bec9923d2586 | -3.1647 | -53.91471 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README85.md)
