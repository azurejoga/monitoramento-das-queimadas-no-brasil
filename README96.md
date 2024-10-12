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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a199d6d7-124f-3b37-a523-23ea75284648 | -3.70393 | -47.92652 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b8a63f4-552d-3aae-8b61-6628b2d0e146 | -3.70283 | -47.92445 | 2024-10-12 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fe8f77c-a3b1-39f9-8cac-069155d66fac | -3.16531 | -50.4383 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09412217-97c9-34ae-9c0f-cef99a737c9f | -3.16282 | -50.34351 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4901d8c-ab46-347f-8a04-c6450a385ffb | -3.16231 | -50.34695 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3195c3b5-4a5c-3a27-9774-00ec1da632bc | -3.16181 | -50.35033 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5c9baa0-f887-308e-8170-da8ffcdd8cc4 | -3.1613 | -50.35375 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28f1bf4d-e563-3bbc-8f03-43a9b19f570f | -3.16079 | -50.35722 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3600f53d-e05e-35b1-8d47-9ba03e8fff4a | -3.16043 | -50.43402 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15fd5fde-c23d-30d6-8739-9d7c6c32c024 | -3.16027 | -50.36065 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b5ad576-5ef4-3e49-8e04-f67f85e77954 | -3.15989 | -50.43759 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57d68178-ab05-3c17-9ff5-a28e58abbf2e | -3.15976 | -50.36414 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 289886a5-26b2-3317-995a-6ec70d4c1749 | -3.15935 | -50.44122 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bcf6267-0a74-3c38-9eae-93691f5d43fa | -3.15923 | -50.36768 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24164d1e-2040-326e-ab12-80df734fb60a | -3.15686 | -50.34621 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42c133e0-e2de-3467-b92b-c3319b8cdabb | -3.15635 | -50.34967 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b313b293-fe1e-3132-ae1d-510bfcfdb54a | -3.15584 | -50.35312 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 125dc2e8-8c7b-3257-9fbd-a147ce6efd5d | -3.15533 | -50.35653 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a74e7254-8858-3bc7-8f0b-1f2205508e03 | -3.15484 | -50.35985 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6afe5384-79c2-398f-b321-ee14d603a4da | -3.15447 | -50.43687 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e2a7675-079a-30f2-8a66-a5e5fe66d744 | -3.15433 | -50.36326 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee85f28c-47ea-3a50-8f07-42848b254ef1 | -3.15393 | -50.4405 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27fedbea-7232-384f-9dfc-0e21b5dc00c6 | -3.15381 | -50.36681 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd481919-9036-37c0-a94a-6dc76b654afa | -3.1534 | -50.44405 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42c5d7d2-4dc3-3906-b4dc-8c5be764bca7 | -3.15328 | -50.37035 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7452ea51-28b2-3f99-a7f6-5d61dc10511b | -3.15277 | -50.37382 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfc694f8-45f1-30c3-8047-574adb3f92ed | -3.15226 | -50.37727 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 695307a3-fe7c-3385-980d-df71bcae6fcd | -3.1504 | -50.35232 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4fc022f-a65c-34aa-bbb1-e2f58701cbc2 | -3.14989 | -50.35576 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20ef2f90-5107-3275-af5f-5eba6ddf84d8 | -3.14939 | -50.35915 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8e62dc68-fa72-3e7f-a539-b16430fee4fb | -3.14888 | -50.36257 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d6f1e39-0af6-3f85-93c6-8b8a96a5446f | -3.14852 | -50.43972 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 476d67dd-c4c2-3e49-b017-0331b1f5ec5d | -3.14838 | -50.366 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12657bda-8de0-32f1-9f53-6627e807b0cb | -3.14787 | -50.36942 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cff63316-64fc-360b-9057-44e766a1df1d | -3.14736 | -50.37287 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3386a09-f72b-36f0-95f5-03fbe064f91a | -3.14685 | -50.37634 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e176e74-913e-3435-a3fd-e31dcd89c252 | -3.1426 | -50.44239 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c01119c-ceef-384c-afac-c7fac6b0356c | -3.14194 | -50.37197 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cacf606b-9ff0-38df-8739-be843e24b5d7 | -2.83484 | -49.52473 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3f3cd7b-f3e7-3433-9913-1c82c9fb1a98 | -2.83424 | -49.52877 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bea2a1f4-efef-3137-83a7-b2d2578acf4e | -2.83367 | -49.53263 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 99b8af3e-93b2-3f06-b761-fd04361f31fd | -2.82855 | -49.52777 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79bf60b2-1b59-320a-8483-002341fa7e6f | -2.72289 | -49.47935 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4ada500-a443-3f7e-a2a4-10d6249e6730 | -2.72266 | -49.47654 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78dd2efb-cd9f-3f59-bdca-69a7f1523f27 | -2.72232 | -49.48323 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71c79eee-b00a-3dd5-9b4f-2b46f9e84d52 | -2.72207 | -49.48038 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf50628-b160-3f70-9f45-ac8a34c2d465 | -2.71774 | -49.47456 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c85bae75-18ab-3be9-9ff8-61cbe75171f7 | -2.71717 | -49.47845 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d618aa9-78b9-368e-adbc-59b033524e5e | -2.71695 | -49.47561 | 2024-10-12 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc4550b7-518d-3a66-81d1-1e6636311072 | 2.22263 | -50.72551 | 2024-10-12 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64a9ba63-e22a-3a9f-93b3-f3fc7d15a265 | -3.0453 | -51.13213 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bfdbfe5-e9f0-355c-8158-586cf1647c5c | -3.04485 | -51.13517 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ccb2c24-7b0f-37a3-b46d-637873ee4086 | -3.04061 | -51.12831 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 473711de-8cd3-39d9-a63f-2b7ad3664e13 | -3.04015 | -51.13137 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49cc793a-8125-3835-a719-142364a7adf8 | -3.0397 | -51.13441 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70e1c4df-7d33-31ec-a51e-a4acf3c7ed2a | -3.03923 | -51.03085 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a11ae4-00da-33b3-b171-8117964a4fcf | -3.03877 | -51.03397 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92f9f61f-9377-3a95-89ca-ae1b2e55ed0c | -3.03547 | -51.12749 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10d1b6fb-4efd-3e3e-94cc-2565b2931ee9 | -3.03501 | -51.13056 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd5a5568-a200-33cd-8769-d1c840431280 | -3.03033 | -51.12665 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0060c0f0-fb9d-39d5-b406-6517bae0de54 | -2.9755 | -51.35646 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bfdd490-d33b-3506-90e7-46c9fa7dafac | -2.97464 | -51.36229 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7434efc2-e841-3f7e-8d98-095b48379ae0 | -2.9742 | -51.36525 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e1c68a-bd89-36bb-9a8e-a369c7f98570 | -2.97044 | -51.35566 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e6eb541-e11c-3c6b-9ba6-1998b3670254 | -2.97 | -51.35859 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5949e5f9-3ca7-3777-9a10-cb768b6bce3a | -2.96957 | -51.36155 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 873939ff-29ce-39ea-8b32-519831fc65fb | -2.96914 | -51.36451 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 754edc76-93d0-3892-b497-c94f68b5d5f1 | -2.96394 | -51.0299 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f169b340-ccab-3eed-bc66-0bd5ef1c847c | -2.96348 | -51.033 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 366f6883-b3bb-331d-90ce-52aac645d880 | -2.95171 | -51.28399 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14f5e91b-df7a-32d7-9e08-0f7bfe366e52 | -2.95126 | -51.28697 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5652d917-7d8c-3173-b0b4-ca3c55b77643 | -2.9508 | -51.28996 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edf53bc8-40fc-3d60-8a86-37f48416fc60 | -2.94617 | -51.2862 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 016ea439-195a-3be3-b705-6a4df94386dc | -2.9017 | -51.75472 | 2024-10-12 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecfff87a-1e11-3d0c-9e60-a984297f82a9 | -2.90092 | -51.76003 | 2024-10-12 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ce83d17-069d-31d8-8e0b-a5be7ce95d87 | -2.89959 | -51.75713 | 2024-10-12 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d013b4f1-056e-30c6-965b-1d36cf01f4a4 | -2.87349 | -51.66372 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38f7cc86-356d-32e2-88c8-67385f1f25f5 | -2.86854 | -51.663 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad9f92cb-6cbf-3d38-96b4-4accc1b834ea | -2.86771 | -51.66849 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe7c4a0e-af42-3503-85ec-369dc28e5ec9 | -2.8636 | -51.66219 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e698cc47-5df7-3342-b8d2-3778f2b5b986 | -2.86276 | -51.66772 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 642a1613-4cf2-3734-a0e3-4b82604dba8c | -2.82637 | -51.33924 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e94e9a3b-8f73-3e2f-8899-af9e46e17958 | -2.8222 | -51.33263 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 804632cd-b689-331f-8913-60d7b8af1c07 | -2.82176 | -51.33555 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 18eff531-d5f7-3e3d-88f8-737afffab4f8 | -2.82132 | -51.33847 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 6424eff0-a8e5-3011-8fb8-223e629a1991 | -2.82087 | -51.3414 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 45159dc4-fb6d-3d61-ba63-c51219dde2d6 | -2.82043 | -51.34432 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 331c4f11-63df-33dc-b03b-9ebf4e638207 | -2.8167 | -51.33479 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 678ba32d-eb03-3dab-8086-adab38e312db | -2.81626 | -51.33771 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4b55927d-993a-3124-9abe-4d1997433b52 | -2.81582 | -51.34062 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9997d1a6-be18-30a2-81a2-bbb89bc4eaa8 | -2.81077 | -51.33985 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47c15e0b-7fcc-3359-b50e-805356210cc1 | -2.80741 | -51.01134 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4a23fe0-36fa-35ad-b03b-cb4b91f19ce9 | -2.80696 | -51.01441 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5379c718-c032-30f1-8f78-914f4b940d12 | -2.80693 | -51.60041 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cac9f7e-b795-36cd-8815-ea8b08968e25 | -2.80666 | -51.60179 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf9e8e8-bf32-3b4b-b848-2a021e6ad11d | -2.80652 | -51.01743 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f829b243-122c-33e5-be1e-d3a0c2e531e4 | -2.80604 | -51.01057 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dd0df37-b158-3e43-bb6a-5c7de2915a70 | -2.80557 | -51.01361 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca17a10-03bc-33ce-a833-b31ff886fddf | -2.80511 | -51.01661 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8cf1c18-4265-33a0-8a63-0574eb06a62a | -2.80225 | -51.01052 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README97.md)
