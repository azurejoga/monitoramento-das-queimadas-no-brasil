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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ff3910-9878-3613-a872-b917c9b4acef | -9.26946 | -67.87978 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 563c7a87-735b-3fbd-985d-44d6fb106a60 | -9.26874 | -67.88463 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c7c46c6-d754-3866-b7ff-c46371f86b97 | -9.26693 | -67.59565 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82b60ba2-6efd-393b-b81b-addaa1593107 | -9.26644 | -67.81946 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9940a42c-1c45-36a8-816c-9036c28aec54 | -9.26621 | -67.60071 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2313c927-35ae-3d02-b53e-91dccea5604c | -9.2656 | -67.87919 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 312f211c-d965-3b36-977c-3937a29da2d0 | -9.26489 | -67.88406 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29627f40-eded-3594-9fd3-d45cc52b00ca | -9.26301 | -67.59504 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 410bc492-c09e-319b-adb9-f9ad4ddbe622 | -9.26257 | -67.81888 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa12ff36-2cf2-3567-b40a-bd2839d4365b | -9.26228 | -67.60011 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e9c7a5f-1b05-33c6-a725-0af63151c363 | -9.26185 | -67.82378 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee011c44-f0cd-3748-a14a-2d52629974cd | -9.26156 | -67.60517 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66683b59-6f76-3dc7-9d53-ea27ee90e5d9 | -9.25908 | -67.59446 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6947ac7-5bfd-3e5c-9cf5-87cf71c5dca7 | -9.25869 | -67.8183 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7bbc392-93e0-3196-b73a-96ff371cf39a | -9.25798 | -67.82319 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbe44f08-e6c4-31f2-8423-5755dd7897a3 | -9.25482 | -67.81771 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bef77154-996a-3fc1-bcfe-8678bcc048f9 | -9.25411 | -67.82261 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deb99816-ca2d-3b36-b1e6-e50d78f0651e | -9.25095 | -67.81713 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8eec626-23a4-361b-86ad-e84bc72b666b | -9.24778 | -67.81166 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 292c7490-1621-33b4-9d18-5f41119abe49 | -9.24707 | -67.81655 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90d9fbb2-e328-3e72-b3d6-b8c86fad47b4 | -9.2432 | -67.81598 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b42493e6-c51d-3100-b752-6027bcdc3ee4 | -9.23158 | -67.81424 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71562730-94e8-3fcb-9974-fcd2d5441e55 | -9.23087 | -67.81915 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a08a0c00-857b-36d2-8c37-56432ed7912c | -9.23017 | -67.82405 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68b74b5f-4ad8-3db0-b78a-1a19bd69f23e | -9.2291 | -67.63628 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c05c15c-9d99-3067-9b96-6dd84a2b2633 | -9.22771 | -67.81365 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bc21efd-c24a-3a78-af09-875f674b9c3c | -9.227 | -67.81856 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11017361-d555-34b7-b7a9-c51c4d724e09 | -9.22383 | -67.81307 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 347a7f5d-0771-33bb-98a9-2545450b4ec8 | -9.22313 | -67.81798 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd95f9cd-97f1-3d1a-8dac-07b677f5aaad | -9.22029 | -67.7824 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de15cc0a-18b3-34b0-a900-213bf02f36a9 | -9.20638 | -67.68412 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e40a1d1-20e8-3ac3-b28f-8fef1107cadc | -9.20607 | -67.68254 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fc1c980-df45-32e2-abdf-2bb5ec29403d | -9.20533 | -67.68752 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb0543b8-0bee-36df-afcd-deab4211b99f | -9.20498 | -67.6941 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f92e56e-e8f6-3320-948e-39e8120d75a8 | -9.19118 | -67.84814 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 355b3ee4-33c8-3e9b-a490-44cb58061681 | -9.19049 | -67.85302 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 439bfd4c-1cdd-34d0-ba9b-849538ebb18b | -9.1898 | -67.85788 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36758c70-f1a9-3d24-8ef2-1a995e9b7e6b | -9.28327 | -68.36584 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b3e320-ad7f-3e64-9bd9-a6de4c2429f1 | -9.28275 | -68.29058 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e4c9f8-2dff-35fc-bc14-57ac807029de | -9.27952 | -68.36526 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509b6096-0571-3c40-a500-0fcecc0c9618 | -9.27885 | -68.36983 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0326e885-f9a6-33d6-8fda-102088e2a12b | -9.27353 | -68.83822 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85fcd515-5528-3f8e-a25b-d430c96f9a50 | -9.25588 | -68.83121 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb8a0091-24ef-39eb-8a1c-d58719d9a20f | -9.25481 | -68.4819 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc653e50-2d9f-3c02-b062-199e59af4c65 | -9.25223 | -68.83064 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b7da3d9-2554-3afe-89f8-356bceec6f05 | -9.25183 | -68.83256 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5575df25-7c5a-3a15-9975-45b4b317bdc6 | -9.24858 | -68.83006 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cf47fb0-27ff-33d1-83a6-c373c5487455 | -9.24819 | -68.83199 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb00a848-00ba-3124-93b0-0305e2f91a80 | -9.21976 | -68.16458 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d96568-f529-307f-b15c-e36694b531d8 | -9.21907 | -68.16929 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d7add97-edbd-3010-987b-d08fab7f9dab | -9.19994 | -68.29908 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93ff4f22-e8c5-3755-b51d-14a15faaf723 | -9.19019 | -68.39092 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b665f450-47e6-3ab7-a58b-69d693c3cef9 | -9.18856 | -68.24554 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d1304c-e6d4-3db5-a62e-d432623d843f | -9.18788 | -68.25014 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5739a7ec-6ad6-32a7-a1f3-3ddcd2cf08ca | -9.18721 | -68.25475 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89cb8f28-af8b-33d6-985e-a510380c140d | -9.18087 | -68.32426 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b701b38-8930-3577-a1f2-f6af71a30664 | -9.17765 | -68.26744 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f82968e6-b9c1-3df6-a3aa-1e30b0758147 | -9.05052 | -68.10355 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35d0e51-a2f1-3147-b634-c7feb0a1e1dd | -9.04985 | -68.10825 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b362e9e6-d4f9-38de-89da-f39bf99d70d4 | -9.04338 | -68.12643 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e8277ef-a6ae-34ed-8a82-e7b04c71ee16 | -9.034 | -68.11066 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7267faf4-2e74-3d84-822b-723bb071aa7b | -9.03372 | -68.11356 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a135e88f-660b-3cc8-a9a6-e3561f88cbbd | -8.91514 | -68.75629 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed7702cc-181f-3101-bc62-32e8d957146f | -8.74514 | -68.69228 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f99ef4e-955c-37ac-9e21-3dff889acc69 | -8.72685 | -68.68948 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 049ac1dd-8bab-3089-b3f0-13c49b1d7a32 | -8.7232 | -68.68892 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9fa529b-cd56-3369-90e8-41b0a533c8a4 | -8.91951 | -67.38776 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26373f47-900e-39cc-bade-96582a27731f | -8.91665 | -67.38612 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8734a46-9854-3873-901e-a74fa759eda2 | -8.91555 | -67.38717 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ebe6af9-fec4-3ab4-9bfd-5fd33b23deff | -8.86624 | -67.48282 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7759df38-6520-3420-b5d5-9a25ef131e62 | -8.83453 | -67.39478 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 634e88bf-7c47-39df-a61a-688e4b8e7155 | -8.77545 | -67.69884 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db222e9e-4e71-3fb2-8b42-c064afea9055 | -8.77226 | -67.69336 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb2820d0-c86c-3c47-89fb-eecea3c69f36 | -8.77157 | -67.69827 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bb3ac32-e2ce-383c-92b8-795eb4e4c8a2 | -8.77128 | -67.69153 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c857d57a-5ee1-3ddb-b86b-9eac4868afca | -8.77087 | -67.70319 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86a9cee4-4470-30d4-a4d6-cd113b4aa435 | -8.77055 | -67.69643 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 038e5f07-8b8c-3e2f-9b74-3eca0ba6a2c3 | -8.76982 | -67.70133 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd536b51-ef4a-3ad0-ba8e-a9aad2a23bab | -8.76838 | -67.69277 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d9c2949-5960-39aa-abdc-4a32fe1ccfaa | -8.76769 | -67.69769 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec84bfaa-bc78-3ffe-b19d-5ab63e499856 | -8.767 | -67.7026 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e544bee-b1bf-3113-a98a-744959c74ad0 | -8.76667 | -67.69585 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70203e7f-ef72-37f4-870e-8ad7fb93ce9a | -8.76631 | -67.7075 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57684227-f2b6-3bb2-903c-4f09e861c66a | -8.76595 | -67.70075 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d122f0f0-6aae-3537-bf01-711207439bc2 | -8.76522 | -67.70565 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6620a7a-832a-347a-93fb-4b26de65b272 | -8.76382 | -67.69709 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 374a90dd-1543-38fb-8e4a-a39d8cc81539 | -8.76312 | -67.702 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5801b2f1-d09b-3dd5-9c03-cc24020000e1 | -8.76243 | -67.70691 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 045bfc92-55cf-39cd-864f-c0b0aad1e1dd | -8.76207 | -67.70016 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66e43bea-2f65-39c3-8b0d-085975c30a2e | -8.76135 | -67.70506 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99f189bd-f3bc-358a-bcf7-e5bb927bcafe | -8.76063 | -67.70995 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f0ece47-a60c-3c8f-83ce-d0c253a0c372 | -8.75925 | -67.70141 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18ee978f-6226-3be8-91a3-e7d28b8a1c29 | -8.75856 | -67.70632 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 284c89a1-9e20-3df0-8b17-b1bb1e666948 | -8.7582 | -67.69957 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62ee6d3e-cb3e-3bba-aa75-4962b61ca0d7 | -8.75748 | -67.70448 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1c33c74-6728-355c-9ac4-843bd419c85f | -9.37069 | -68.32484 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c622e5ab-b010-334d-bba3-ac4e79fd1ef1 | -9.36853 | -68.20582 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64727e4b-c105-3a16-8b60-734c1fcf21af | -9.36693 | -68.32426 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d041137a-6173-3d3d-a52d-315c2ce1d2d1 | -9.36474 | -68.20525 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 429623b5-0995-3e62-9d2b-c5228a63fd61 | -9.36407 | -68.20995 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README189.md)
