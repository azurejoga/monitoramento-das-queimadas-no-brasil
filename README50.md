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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0add7d3-eef8-37bc-9ecd-f3c38b4848aa | -11.21962 | -53.86268 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17b18a7b-4220-328d-8671-01880012971f | -11.21907 | -53.86619 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5da3f17d-cfda-3fe5-97aa-ef2d1b4e3c4a | -11.21631 | -53.86214 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7fa374-9b21-314e-99e3-eca6833449e8 | -11.21576 | -53.86565 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80c07031-9001-3a54-95b3-c8effe7fdd32 | -11.21245 | -53.86511 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44a77b1e-18bb-3cba-811f-433683329c88 | -10.88782 | -53.01153 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27069b57-752e-34b7-8b7c-4168960064f7 | -10.8845 | -53.01101 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 350082e1-9043-3907-9847-187aff33c54e | -10.83716 | -53.76785 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73f67238-30ed-3814-842b-9168ea85fde6 | -11.19976 | -53.85946 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4104acd-4a24-3865-a8b7-55d2895c97f2 | -11.19645 | -53.85892 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 204420e2-a248-3a83-b7f2-1072cf6f0a51 | 0.12559 | -51.74538 | 2024-09-29 04:49:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95703654-c02f-3b4d-90d3-5406bfdee927 | -4.37141 | -53.64451 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80716d3d-67bb-3cf7-9025-f533ed0cafb7 | -4.20676 | -53.84327 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 138b9a43-c2b4-3fec-aa2f-ed78f1747a42 | -4.20618 | -53.84689 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a441fbe-e8fc-39f9-b095-59e0049c0dd6 | -4.18049 | -53.69713 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2129ee66-7401-36b5-8d92-f9f508980dc9 | -3.89324 | -52.30738 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08317c5b-86a5-37bd-9edb-a716b865109c | -3.8927 | -52.31082 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ebe08c9-48bc-349a-924d-f0bd2ed034ca | -3.89216 | -52.31426 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c393f50-089b-3925-a490-5ba265497792 | -3.8873 | -52.36656 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| af3c4f9e-5de8-3e69-94a8-d9a8b33a4d0b | -3.88676 | -52.37 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e06bd51-46e4-31ac-9204-e2ccc4728d5f | -3.83193 | -52.30841 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8f0b1f-17e3-3767-952d-eec15c4fa968 | -3.82862 | -52.3079 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dce9a91-2eb5-3f76-af85-4b2143e85ee1 | -3.7768 | -52.31394 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48ecafe6-9893-32fd-a06e-3f08c92d649a | -8.71136 | -54.81725 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9883ec17-3c94-37e6-a2b2-cd0208fec5b5 | -9.89285 | -54.49245 | 2024-09-29 04:49:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b173f9-c0c3-38f2-bb42-14fd78de0441 | -9.74187 | -55.08216 | 2024-09-29 04:49:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 086ef532-11a3-3b29-942b-55b49dd42e8b | -9.59751 | -54.25742 | 2024-09-29 04:49:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36a7cd0e-58a5-30c5-976a-86f420b8e89c | -9.59694 | -54.26099 | 2024-09-29 04:49:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 905b0413-e603-3041-a9ec-fa35537b47b4 | -9.5936 | -54.26045 | 2024-09-29 04:49:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f0298a5-c658-3dc5-8294-5ee2187750e1 | -9.57595 | -54.0503 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a477ff3c-8a14-31e0-ba3d-fc7926e082b9 | -9.48818 | -54.55197 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1c62401-44f2-324f-be48-37afb2ee2853 | -9.48003 | -54.44045 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6579aa7b-d9b9-3d60-8fc3-74cfd0c6be80 | -9.47667 | -54.4399 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10e5e932-78c0-3f0f-a79e-f5b27d84e43b | -10.61006 | -54.23618 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf2fb64-8307-3d5f-89f9-148608aabde8 | -10.6095 | -54.23972 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed8f7e4-9eeb-3ba9-9369-d5443f5a5e7b | -10.60674 | -54.23563 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa76bfc-9394-36d3-89d8-03ab7fccbfcd | -10.60618 | -54.23917 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce640d7c-bc46-31a5-b05e-ae619c19f0d5 | -10.60561 | -54.24272 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66f4afec-3d39-37e7-accb-b9d1019520f4 | -10.57405 | -54.22665 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6d94a72-4323-396c-a06d-abc906d04e36 | -10.57016 | -54.22963 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b21d6d1c-6e20-3392-8d49-8b2703499b1a | -10.46533 | -54.22715 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1235afc-23d6-38c9-a941-32848f5fc0fd | -10.45811 | -54.2296 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c90383-7aa5-37aa-a56a-f93e9359bdab | -10.39219 | -54.55524 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a25a8c8-e30b-312b-a777-601f00274232 | -10.23823 | -54.24473 | 2024-09-29 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8016f029-cf40-3f82-a4b4-90e634bc7bf8 | -10.40542 | -53.72697 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1164745e-cdbc-3d4d-8e80-9b0636982b0f | -10.40487 | -53.73046 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05115788-1fee-39c2-8c01-3eec3f18a90c | -10.38275 | -53.78431 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff1a8807-b465-3669-8bf0-138a0ff53ce8 | -10.3822 | -53.78781 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de9e52cb-0185-37f1-b11a-b025400c98bf | -10.38 | -53.78028 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 000572eb-eb42-39c6-b76f-84f4b402ab06 | -10.37944 | -53.78378 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc2466ce-a863-37fa-8924-5e769cd6229f | -10.37889 | -53.78727 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bab3c257-1d7e-3f2d-b670-f6a954ae3915 | -10.37833 | -53.79078 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 33ad68cd-2c8d-3c12-b045-1d8e807b7ccb | -10.37778 | -53.79427 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f419ed23-fe3e-3735-ae8a-1bee53731005 | -10.37669 | -53.77974 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65a32671-cb6f-3b2a-bc92-b7c10f6e6bec | -10.37613 | -53.78324 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c5f8b44-9b2a-3d9a-9572-8e2b49df2d4a | -10.37558 | -53.78674 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 50d24ea4-fc5f-3291-8511-c5b8c86331c0 | -10.37502 | -53.79024 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| baf878a9-3ffa-369c-a02b-9629bd5cd44e | -10.37447 | -53.79374 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f6f2056-7fe3-3652-b4b7-2b350b26eb4b | -10.37337 | -53.7792 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51d74aa6-9298-39b4-b8cb-f0f497a56efd | -10.37282 | -53.7827 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93715f4d-3a24-35a5-8d98-cc8cebc570fb | -10.37226 | -53.78621 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 27e344fe-de5d-3bcf-ae4a-68e60ccc2037 | -10.37115 | -53.79321 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc4df8c5-c3fb-30e1-b3bf-1134454f060c | -10.369 | -53.78574 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62a4cf74-fa17-3070-8aec-6376b8009827 | -10.36845 | -53.78924 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27513c71-b050-358e-ad57-6dc7cb01761a | -10.36403 | -53.79571 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6343d591-24ed-30e3-b29c-ce9c414cac7b | -10.36348 | -53.79921 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e947a95b-b979-3615-829d-b263d391553b | -10.36127 | -53.79168 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc96fe99-a725-34be-89f2-8d0fd2e9218a | -10.36072 | -53.79517 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8984655-a5dd-3738-a213-495fd99ca2d2 | -10.36018 | -53.7556 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ac7c838-1e3a-3c93-80cb-1c866d0a70d2 | -10.35851 | -53.78764 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8a664cc-b09e-375c-b4bc-2d02b1f48ddb | -10.35796 | -53.79114 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30a98838-8ad1-3d05-b662-806a83c75c6b | -10.35741 | -53.79464 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c352de-be16-3166-8a21-192440dbff42 | -10.35687 | -53.75507 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccfbcbe9-b09c-3f8d-906c-0ece3e3fd8d9 | -10.3552 | -53.78711 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8f6b902-8153-3301-b8da-8160552d22ac | -10.35465 | -53.7906 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91e5b905-2bbe-3366-b811-8d5ad427e3a3 | -10.35356 | -53.75453 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8219641-f70d-36e5-849e-55fa29f1e0bb | -10.35301 | -53.75803 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa585f18-11fa-3eee-8a27-35cc77d956eb | -10.35025 | -53.75399 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb42ae73-d7f1-3dfb-9358-1ab4080896dd | -10.34694 | -53.75346 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61dd13d0-8640-3929-8eca-87609f0fddaa | -10.34638 | -53.75695 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 408e8ff0-42da-304d-b40d-6c3f30d5d4bb | -10.34583 | -53.76045 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07bfa612-7fba-3bd7-a52e-d06810660f5a | -10.34528 | -53.76395 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d01258-5dd7-3f82-b53c-b7d036ebf7bc | -10.34252 | -53.75992 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a30a41f-9023-3aad-98b4-99f38f313390 | -9.66078 | -53.53888 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f80b4f8-0a9d-33ac-8cdd-fd4e9ac20d75 | -9.66023 | -53.54236 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b102314-6d23-39c6-97c5-69b8aef6f282 | -9.65968 | -53.54585 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31142643-e47d-3e83-a60f-d27b61427313 | -9.65913 | -53.52788 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd0c6295-2f30-3d76-ba7e-948b8da6335c | -9.65748 | -53.53834 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4fcb4e-f08c-380e-9f00-6f1b585fea7e | -9.65472 | -53.53432 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94db0081-e061-357c-8a21-e7b3bfc62aa6 | -9.65249 | -53.59124 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2abc629-01ed-3f29-b813-5f00f882958c | -9.65194 | -53.59473 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0981ef3-9668-3d5e-a1d8-936e2275f31f | -9.64974 | -53.58722 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f623edad-a721-3f9a-9d54-7e56417cf686 | -9.64918 | -53.59071 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bf794b8-cc94-3a35-b11f-0129baabd0a7 | -9.64863 | -53.5942 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf53367-8e3f-330b-9441-1caa48433399 | -9.64642 | -53.58669 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5db54c3a-583a-3003-93b6-d3371ce07790 | -9.64587 | -53.59018 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2cbc40e-75d3-30cd-b34e-02a2b966ef90 | -9.64532 | -53.59367 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda5e787-6a61-318b-bce6-7d8714d3d906 | -9.64367 | -53.58266 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9197d2e0-c91b-300b-ac59-f6caa6185cd5 | -9.64311 | -53.58615 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 606881f7-d728-3fcb-aa8c-33d7012eb861 | -9.64256 | -53.58965 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
