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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15cf93af-dbac-3be9-bd25-3207ffd86365 | -16.97889 | -56.82495 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b1aacb19-5464-3ead-b73e-63cc907f7040 | -16.97709 | -57.52819 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6b28769e-4d4a-351d-aadf-16b21c64553d | -16.97654 | -57.53182 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fe255235-61fa-34d3-98f7-2d2448e6d951 | -16.97433 | -57.52401 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 5ac8840b-0576-3bd0-802f-aabbefb8ece7 | -16.97377 | -57.52764 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| ea959f29-483e-32b9-b9b0-e99b071b5181 | -16.97159 | -56.8276 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 24b43a67-407e-3a90-95a4-93a264aa6ab4 | -16.96768 | -57.52291 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 0a2a9330-e9a0-34a3-a86e-e703f5e26239 | -16.96547 | -57.5151 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 146a2e50-711f-38a9-a72f-0536e3bf8569 | -16.96485 | -56.82651 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ea016de6-2e2c-3c7b-8ff6-2da3b0e5a817 | -16.9638 | -57.52599 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| a62a7993-dbc2-3a0f-8163-3238b5129ded | -16.94772 | -57.54191 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 55870396-b4a5-3374-893b-f376f8d96971 | -16.94481 | -57.69361 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6f8c3b89-b89d-392d-a8d7-718c7511a42f | -16.94163 | -57.53719 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| aa517387-cc60-358b-856c-d66735280834 | -16.94107 | -57.54081 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e1e8de3e-6303-3c5c-a8fb-fb91275ccaa8 | -16.93831 | -57.53664 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| ce1416ff-ec0b-34ca-9f30-26a7bb06836b | -16.93721 | -57.52158 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 89d6ff84-ed72-3950-92ca-d4b6bf4d0866 | -16.93499 | -57.51377 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ac1725c0-93a7-382c-b757-984d48e40b91 | -16.93444 | -57.51741 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a1a6ed0a-d9e7-314e-8305-40bb0ff95ed3 | -16.93333 | -57.52466 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bf26daa6-ad48-3a73-808d-2c3039356644 | -16.93166 | -57.53554 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| da920b01-5fda-3d57-b0fd-c4867c952731 | -16.93111 | -57.53916 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7004892c-ca38-3736-b8db-02e8ee872901 | -16.93111 | -57.51685 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a8de70bf-a5f0-3c1d-a9c2-a857e6b920e0 | -16.92889 | -57.53136 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 12a85ea2-94a5-35c6-aec5-7ed1ebb816dc | -16.92779 | -57.5163 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7b18293e-5989-328d-b0ef-f580ea18c3ed | -16.92723 | -57.51992 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f4409ab5-88df-35cc-99b8-863f9584b869 | -16.91837 | -57.49276 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0e818ce3-8044-3c78-99be-9f00f76e4eeb | -16.91725 | -57.50001 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f2c66aec-5c4e-30d1-8b41-727e2547c9bd | -16.9106 | -57.49891 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 26944219-85f5-3a72-b428-d173502038cc | -16.90888 | -57.68392 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9ed79dc0-41a1-386d-b5d8-4651e3ed5616 | -16.90832 | -57.68753 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8c1ed1da-b59d-34da-9cf9-bdf5f7f3cfce | -16.90783 | -57.49473 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 22f6b679-9729-326d-8d5a-1dc65ffc72ae | -16.90727 | -57.49836 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 1e81e7b7-a165-3b3f-b84e-8791485b592e | -16.90339 | -57.50144 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| bc2e79c6-e894-3acf-94a7-8ba29139622b | -16.89522 | -56.75109 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 391cedcd-32b0-353e-8228-2a7290da5613 | -16.89372 | -57.67428 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4bc462cc-6f5c-3a14-af68-5ff7b59b403c | -16.89241 | -56.7468 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 05421725-dad2-325e-87a2-343b05c335a6 | -16.89185 | -56.75055 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1baf2828-af42-3179-bf2f-c5aa8a6e8087 | -16.89076 | -57.27173 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5aaf1fe6-2158-3798-8a8b-7ee01a9a2ca8 | -16.88904 | -56.74626 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 85fdb849-6261-3213-a87e-107b4b4d9d00 | -16.86607 | -57.67709 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5d03fd64-be79-3ce0-aeb2-3174f4b24bd9 | -16.85832 | -57.68321 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 664e8fe5-6a52-3325-85ab-4bb5347bf2bc | -16.83665 | -56.68028 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 44fa9bea-3c81-33ee-adef-9902627a1195 | -16.83613 | -56.70706 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7ad5705c-6a49-3d7a-a379-1c314fcd8941 | -16.83558 | -56.71081 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6a9c0764-27d7-3000-8449-00964b8437ba | -16.83498 | -56.69154 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 77afd1bc-64fc-33ae-ae93-f6402f7b98f9 | -16.83383 | -56.67598 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fc1b7351-fa0b-37e1-b4f1-a24f5d7d935c | -16.83327 | -56.67974 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 31a50f0d-0e1b-38ac-abed-4b307d6e879a | -16.83265 | -56.67641 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 09ae97fb-7a4d-3645-b6e0-4faf2b6b0490 | -16.8322 | -56.71027 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f1271e09-a21a-3ff4-9e2d-fcc07780e464 | -16.83209 | -56.68016 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3f063948-db81-3a25-b0c1-aff0d56a993f | -16.83105 | -56.69474 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8578cf0f-ba4b-3ffc-9bfe-ff252560f9d7 | -16.82871 | -56.67961 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 62aa5bfa-4627-369f-a268-701c7f8eb37e | -16.82814 | -56.68336 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 93b2c348-e0ec-3e93-bd0b-8375246b022b | -16.78819 | -56.71909 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6678f776-be4d-3ab8-b351-533e8cfadd0f | -16.78481 | -56.71854 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9faadaeb-0460-3f40-9242-d3a687ba4c18 | -16.77807 | -56.71745 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5e1cc995-fa8e-3d03-8fca-7c6033375bee | -16.97488 | -57.52038 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2abf4042-e8fa-35c0-99fd-70cf5e6d32c1 | -16.97321 | -57.53127 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 6ed75820-aee1-3315-ac5d-78a3d0cf13a2 | -16.97045 | -57.52709 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 8715cde1-01e6-3044-b95a-ac20e8eaec45 | -16.96712 | -57.52654 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 40d57dfa-ec08-369d-b230-6da905d6ba13 | -16.96435 | -57.52236 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 134faff1-096b-30f5-b8ed-7c3c7a606da5 | -16.96103 | -57.52181 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5c819c81-c72c-3fab-b574-cc6c88a6378e | -16.96047 | -57.52544 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| cb3a825e-9438-3d93-a856-c3f1d28f1066 | -16.95992 | -57.52906 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f127065c-073a-389e-9470-ca5afedb72a2 | -16.9444 | -57.54137 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 56cdadeb-11a9-36ed-8c61-b53faebe52c8 | -16.93499 | -57.53609 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| ec5aebf3-0c5a-3ac4-a5f5-8f6f3caccf67 | -16.93443 | -57.53971 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7c218c54-c75c-3984-94a5-5fc39be3bf76 | -16.93277 | -57.52829 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d56c9674-b12b-37ac-b43b-fbf5c8571b5b | -16.93222 | -57.53191 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 504b13e0-e206-3e15-a4ba-b18f8611e66e | -16.93167 | -57.51323 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1ee02d27-345f-39c8-8605-e85a598a8831 | -16.93056 | -57.52048 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 029e0fe3-3765-3fec-8f88-e333ec17ab59 | -16.92945 | -57.52773 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 54602c76-a861-35d8-b4ae-655eb135d50b | -16.92658 | -57.67946 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4ffdd1a9-2d1f-35c0-a77b-47995afcbead | -16.92612 | -57.52719 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ca37e8a3-5b64-36a0-b5d4-3ce8661f0704 | -16.92557 | -57.53081 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5be49cb2-6abf-3e35-98d6-5b800cc0a584 | -16.92454 | -57.43047 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8f99800b-a46d-3b6c-9576-b868ac82ead2 | -16.91504 | -57.4922 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5305e64a-c891-32a2-bcbb-c5800a4574c5 | -16.91392 | -57.49945 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a2ebaec1-a4e5-39e6-b0b3-cce11aed8f46 | -16.91336 | -57.50309 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1ac7bdb6-4e0f-339c-9134-98a2d59fcada | -16.91004 | -57.50254 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 913840f5-3187-3e20-ba5f-c07df4be7914 | -16.90671 | -57.50199 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d393b959-ef98-3c62-8698-78c2a1954f95 | -16.90507 | -57.49055 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 53cd6917-acc0-30fd-bc13-0dde57704b00 | -16.89317 | -57.67789 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 42338f9c-e99b-3e7a-8623-7f96922a606d | -16.88489 | -57.6654 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e8a61bba-91b2-33d0-9b95-3d9fa255a203 | -16.88433 | -57.66901 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fa958d78-a896-39e7-b83e-6ea4f282ef30 | -16.88157 | -57.66485 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f8485594-cb30-3706-b196-9aa513697aaa | -16.88045 | -57.67207 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2ea81f77-777e-3859-b243-9e655d6be0ed | -16.86052 | -57.69098 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| a0a7f00c-7570-310b-b90a-60d6e6b3ed16 | -16.85776 | -57.68681 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0d5147bf-147d-3426-8449-2a1ef6383ab5 | -16.85388 | -57.68987 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 031f520b-9bd6-3e76-8ab0-965caca9e1ed | -16.85001 | -57.69294 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7b925d59-4f07-35af-a3d7-6959f2564ee8 | -16.80361 | -57.64077 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7720ea55-6b43-35f3-b9b6-0e57fca74ec5 | -16.04487 | -58.25869 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| acd56f95-87dc-327f-a469-52ea11da1468 | -15.83455 | -59.01841 | 2024-10-25 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72a3d9db-5867-3154-a5e1-b7334ee28448 | -15.16523 | -59.7142 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38009995-4cfe-30e4-9091-02ae28a067c7 | -15.16332 | -59.72562 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 441b76d2-e724-30c9-84eb-b37181ef8b71 | -15.16182 | -59.71359 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 485c86eb-eeba-3203-876e-f169fd3cc3eb | -15.16119 | -59.7174 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689d7f09-6b01-382b-9675-6bb909de1005 | -15.16055 | -59.72121 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e474cb8-c427-316e-86fc-51dc59610b19 | -15.15991 | -59.72502 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README105.md)
