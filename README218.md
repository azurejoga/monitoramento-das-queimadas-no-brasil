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

## Dados Diários - Página 218

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe294cf0-a42d-38cd-9e15-3a1c425135c3 | -13.42491 | -61.91957 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de18b770-6ef2-3b40-b8f5-2a2567836703 | -13.42421 | -61.92526 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2be244c-8d5e-3dfb-8ad2-e7acbc4c82cf | -13.41996 | -61.91891 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 162c3e9d-3904-327c-8540-bae40ec1e18c | -13.41433 | -61.92393 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f48171f0-708b-3782-8eb8-7d2df0e605ec | -13.40939 | -61.92326 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2679e623-0ad0-3f7e-9af9-427574105422 | -13.40869 | -61.92894 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| abd5ca74-d31e-3b9d-af09-ae4e63780440 | -13.40445 | -61.92258 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 81739eb7-b2f6-3fff-9f3a-7db5a3fb137d | -13.40376 | -61.92827 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 04e70723-7cf4-32d5-9def-284e4a4fba18 | -13.40307 | -61.93394 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ffda0c9-4193-37fc-87eb-6f2d31aa2e16 | -13.39951 | -61.92191 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9bfd073-d12d-3716-972f-6329b10c1c36 | -13.39882 | -61.92759 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4caffdcf-7292-39d0-987e-7ff45bffb9d8 | -13.39813 | -61.93327 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b743cf0-0d4a-387b-a04e-2ce4dedfc47e | -13.39744 | -61.93895 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df7df473-922b-3136-9bd0-71b2ed9909c1 | -13.39389 | -61.92691 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 53f1c595-9e9b-3e92-bd5c-a19c9e04e09e | -13.3932 | -61.93259 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e489875-4143-3f9a-a45d-22d6c22c09d2 | -13.39228 | -61.92513 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1c089e0-d6de-33ff-8904-f13ce70f8f59 | -13.39155 | -61.9308 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16b1649d-0766-3b9c-8a39-9156cbfe4d70 | -13.38895 | -61.92625 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a4837dc6-fbdc-306f-9d80-27f83a886f77 | -13.38839 | -61.97227 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 01d0df5f-33d3-3235-9286-268de31763af | -13.38827 | -61.93192 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a016d5f4-7aed-3711-9c31-079af1f43c9e | -13.38734 | -61.92447 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ba3d325-d31d-3ce5-af00-4a0679b715e6 | -13.38662 | -61.93014 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e78367e2-e682-3621-a6a6-9ed06e389f82 | -12.98713 | -62.46313 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98e5c837-3bad-30cc-84af-fce6b7d957eb | -12.98649 | -62.4683 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af5b0c05-4937-37bf-b39b-6fab21778ca8 | -12.98541 | -62.46584 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ac2b06f-56cb-3d3f-b20f-5956a9a4ddc4 | -12.98474 | -62.47102 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad042a8e-c78e-39b8-9c2b-13cd78fb2e73 | -12.98113 | -62.47282 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0afad0f9-f8dc-359e-bfe0-2e1ec4e7520f | -12.98001 | -62.47035 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87b28135-e0f6-31c9-8aa6-b1d76416ef2e | -12.97663 | -62.45939 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a52ddc1-d27a-3589-b05f-39aee52a3adb | -12.9764 | -62.47213 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c722a036-dcd4-30d6-b1e1-82651355e0de | -12.97529 | -62.4697 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c060784f-ad48-3213-affa-7cc7ae01aa9b | -12.9719 | -62.45873 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 470774b1-c3a4-39fe-99ae-ea223d4c2059 | -12.97056 | -62.46906 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49da70f8-1251-3e28-a8e3-e8ef2b2505db | -12.96789 | -62.4896 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ffe0221-7188-3a9d-827a-656cca006b7c | -12.96717 | -62.45808 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 995b5f38-7b6f-3a56-876e-5fcfafb2d4ac | -12.96383 | -62.48383 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b32b49ea-bf80-3194-944f-c206a0ddebc5 | -12.96317 | -62.48897 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 897ece40-b782-3d46-ab8f-25fa82959acc | -12.95911 | -62.48318 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49aa3b4b-a821-3305-a7b3-7727a7f26b48 | -12.95845 | -62.48832 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1656f23-dca9-338c-adf6-97c6a6441571 | -12.95779 | -62.49342 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad0aae8a-e177-3fbd-8011-d207824598fc | -12.95373 | -62.48766 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a95ca933-27a3-3746-af4f-207e75642fd7 | -12.95307 | -62.49277 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 422aa053-7409-37f9-a72c-cdf1bc72b813 | -12.94352 | -62.4548 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22335c6e-6330-3429-84e0-60b5d2c217c2 | -12.93878 | -62.45416 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b4f86fb-d892-3b1a-bad4-97ea180f4ec1 | -12.93761 | -62.50103 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b6b57fb-c019-3c0a-b696-f08e91677f72 | -12.93405 | -62.4535 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 278e802b-4e1b-3f39-a3c0-e4940fba94e1 | -12.93289 | -62.50039 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a03b379-9b91-37f0-97aa-eecbbca1523f | -12.93144 | -62.47408 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a489cd6-12cb-3b10-bb76-fc7288212dd0 | -12.92671 | -62.47342 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d629f7-7725-36d7-a549-84a673e667d1 | -12.92394 | -62.45735 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a9b0559-375f-3332-a040-9cc2cea3dc7a | -12.92121 | -62.59174 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a4b19cb-689b-3385-b397-c5aac7f042fd | -12.88673 | -62.44707 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af3c9270-2a3c-384d-88eb-b7cdd7a834a7 | -12.88534 | -62.4461 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c329db62-72af-3886-a8bc-489bc4292671 | -12.882 | -62.44641 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70eca3e3-19f0-370f-b341-d14dd0c420d2 | -12.88061 | -62.44544 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4090e8f5-50e6-3d4c-9fdf-9048520e7906 | -12.87727 | -62.44575 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1be271c5-935f-3f15-a409-ced32846f237 | -12.81656 | -62.45738 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d66d1c29-3f43-3f17-a879-afc6c5762370 | -12.81591 | -62.46247 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3433e42c-f1e7-3ce0-a169-ffdd4922eac7 | -12.76716 | -62.26965 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2985114-797b-383d-902f-ed3b386c3eea | -12.76306 | -62.26372 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d74e5be4-132f-34ca-9d34-610cc71d7eae | -12.76238 | -62.26898 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd744b8e-33f1-3355-ab1e-2d89aa5eab45 | -12.75962 | -62.25255 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca630d31-b06f-389a-87ce-579590dd5f8f | -12.75895 | -62.25779 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18479e30-b689-3f4d-a050-cf16f7d93c34 | -12.75828 | -62.26305 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44d6e6fa-8cff-3e86-a89f-27e43b64d0aa | -12.7576 | -62.26831 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8f09e04-ce79-31fa-b526-fb7b6d610312 | -12.75693 | -62.2736 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 18a81612-4940-359a-be1c-77e09ad08ce8 | -12.75417 | -62.25711 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45c6c399-9acc-3c07-bf2f-75adf86f3e5a | -12.75215 | -62.27296 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 80d69c78-fdc3-3b94-95b8-784b429cbcd5 | -12.74939 | -62.25645 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea903cef-bdff-327a-96ec-206874b090db | -12.74872 | -62.26173 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6db520a4-1f50-361e-a3d6-b34f3730cbd6 | -12.74394 | -62.26108 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82e75b48-79ca-31e6-92c0-0c59326f7afe | -12.71731 | -62.90637 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15a7fb08-c2a9-3281-ba65-881c2f3cc96c | -12.71656 | -62.90958 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cdcaf96-bb11-31c8-95a8-e981fc38ea3c | -12.70049 | -62.96042 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73b053ac-d45f-38a3-9cd5-48298ae1de34 | -12.69987 | -62.96513 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b9f8887-1a38-353d-b637-fe92a033bdd1 | -12.69532 | -62.9645 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af873979-72b8-3974-8972-4f8a0b0f37b9 | -12.69469 | -62.96921 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 287e4707-f465-3460-8661-1015e704a9c6 | -12.69452 | -62.93552 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d123dedb-532d-3e0e-b0c8-fb23a4dbc19b | -12.69201 | -62.95443 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af08db50-6da1-33bb-9027-9146d0304f01 | -12.69139 | -62.95915 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 360c6f4c-b105-3027-98d1-37b7374cc15c | -12.69077 | -62.96386 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7c2ad12-688b-342a-b6c5-5e3b694ef13c | -12.69014 | -62.96857 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34328d50-610f-33f7-a23a-2ba1da882450 | -12.68933 | -62.93962 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3201a0df-f245-3a6f-9a7b-b7505ec5101a | -12.68871 | -62.94435 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7d522d34-a4c7-34ae-b2c9-d64813eb5c16 | -12.68684 | -62.95852 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 514e0958-cb76-3f28-96ac-91a5c41e1160 | -12.68621 | -62.96323 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6aa71909-61d7-3e5f-8ee8-65ac105ec68d | -12.68415 | -62.94373 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c2ec338-10a9-3ae3-a695-d70eb0f742e1 | -12.67525 | -63.0808 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4532e71-8f22-397b-bfa8-a3ed239177f4 | -12.67464 | -63.08541 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8646519c-c86c-37fe-b6c0-b05434a1555c | -12.67074 | -63.08017 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1a593fa-0b84-3352-8e33-2104f3a525c8 | -12.67013 | -63.08477 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4fb0473a-9871-3e97-b96a-614fabfbaf31 | -12.66951 | -63.08939 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cc601e4c-6017-37a8-ae6f-2e93897f1f9e | -12.66562 | -63.08413 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a109969a-0fab-3870-b18d-78c492eee40c | -12.665 | -63.08874 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a10bd2f-004b-3b31-bda1-758944b0d0e0 | -12.65537 | -63.09209 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cb46f66-ca74-33a5-be1a-502d67463053 | -12.65477 | -63.09671 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cfb4898-fb84-3ad1-ac61-deac5165af02 | -12.65087 | -63.09145 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbf452c9-f776-33e1-8fb7-28a03df5618d | -12.63402 | -63.14996 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e242dc33-e61e-3fc5-9955-f024cb6a8b53 | -12.62953 | -63.14933 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79292b2a-ee71-3d2f-8c83-4b582d378292 | -13.00508 | -62.73801 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README219.md)
