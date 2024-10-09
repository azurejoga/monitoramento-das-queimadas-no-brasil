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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3015e2d3-405b-3251-9b59-512f3d8f4956 | -16.87225 | -57.80843 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5ae14af1-84d9-3fe6-be22-724b6964e434 | -16.86563 | -57.80733 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a0e04249-085e-3f92-b9bb-d1f092ac0a3d | -16.86507 | -57.81092 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 82a8ebda-7a08-3074-9610-c12ca2a9822a | -16.86283 | -57.82533 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3407f612-d998-3c0c-800e-cd7aec2329fb | -16.86231 | -57.80677 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 13b7241a-ec6b-359d-ae92-7d85137d04eb | -16.859 | -57.80621 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ca097535-7303-3969-bc24-55952b700724 | -16.85896 | -57.82837 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 712b4788-6c11-3c43-b391-3e87b5734fcb | -16.85844 | -57.80982 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bc266bbb-5fb4-33b5-8ffa-b175bffc92f6 | -16.85732 | -57.81702 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a188a4db-846e-3766-9ec9-1fc3bae5a4bb | -16.85676 | -57.82062 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ad771037-d72e-3f7a-9eef-46e906ac8b72 | -16.85513 | -57.80926 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5995624f-e3da-3966-bc62-c208a114aa6d | -16.85401 | -57.81646 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| df9cc8a1-1264-377b-bef1-a31546f431b8 | -16.85237 | -57.80511 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| ecaa1e3d-3c44-38c0-9217-c98ad590ac5d | -16.85181 | -57.8087 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a3be58a1-32c9-3fe7-9ae1-28af9b3c9c9a | -16.85126 | -57.81231 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d3962513-3fdf-36c8-ba0c-9df218a1c97d | -16.8507 | -57.81591 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 87c85219-0721-31d0-a220-675e4e962a26 | -16.8485 | -57.80815 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6b4d29b9-c397-36c3-930b-f9dd3ab4394d | -16.84794 | -57.81175 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f312b0bd-bf95-33cd-98b4-acb8ffcd5cec | -16.84519 | -57.80759 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5a4dcd1f-2e38-37a1-a943-495420eba9e6 | -16.82924 | -57.42706 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 8c883e26-d3cd-385a-9ab4-8bee95247635 | -16.82813 | -57.43431 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 457b90e0-bdf7-310e-83f1-70d8a8d24045 | -16.82536 | -57.43014 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 83216869-55e8-3faf-921b-af01cb2ab899 | -16.82259 | -57.42596 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b99e5baf-5ba4-3a04-9067-fe3c64df4eb5 | -16.82204 | -57.42958 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 23b0ea16-b151-3da5-960d-f2150fb1d185 | -16.81365 | -57.85763 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9d8a5d02-b705-301f-9fc9-1789a0ce1dee | -16.80929 | -57.42376 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ba304c34-06fe-347c-b3e6-017b45a4e109 | -16.80486 | -57.40814 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f9e42125-5cab-3892-a832-c63acba17c2e | -16.80154 | -57.40759 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3690ca70-a426-3c42-a09f-b489a2e9c8b0 | -16.80042 | -57.43716 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 86b4aa04-5ca1-337c-bb57-c684c8e05a6e | -16.79986 | -57.44078 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 07fb7ce2-d1e2-3427-8d1b-2e4d4ce4367a | -16.79812 | -57.56298 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c33e7c9a-ef58-3ab6-a22a-b5f45dc1e518 | -16.79766 | -57.41067 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8299ea32-0c88-3af2-817c-58a4125324fb | -16.7971 | -57.4143 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 42e30419-73ba-3621-8b0f-3c1140935528 | -16.79709 | -57.43661 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| bdf4efb0-144f-3887-9bf4-c2bc32de431b | -16.79655 | -57.41793 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7439c11e-d5c3-3a67-b64f-acf491e6f33d | -16.79654 | -57.44024 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 5ed31b81-3086-3ff0-8622-364dd3c7696b | -16.79432 | -57.43244 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 917edfc3-c2af-3e07-bb93-9ce37cb9b93a | -16.79377 | -57.43607 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 66533314-2491-3c80-bdbd-19e65285a390 | -16.79266 | -57.44331 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cdfc5f2d-dbb2-369c-b942-93ce865144fe | -16.76657 | -57.56885 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0a80df1a-cb17-3b43-9690-1c74b9aa931f | -16.75993 | -57.56775 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 55a1ce8d-cd2e-3758-b5a3-6e7dc4e5ffc5 | -16.71769 | -57.49125 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8a487618-f3a2-356c-af2d-84c178b45fe7 | -16.70774 | -57.46735 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2e6cb1da-193b-36e4-9a88-c9ad1d3e8beb | -16.70221 | -57.45901 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a474d0dd-f9ae-3973-85fb-36c8c2f44266 | -16.69944 | -57.45485 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ed36f446-e885-39d6-9d27-001192043057 | -16.69723 | -57.44706 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 09333040-860a-3ffc-87e8-e020c2d87458 | -16.69612 | -57.4543 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 322f8c89-8ce0-3840-a2a2-5926131aee8d | -16.69556 | -57.45792 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 53e74854-ed68-3b71-8772-689a80a20133 | -16.69446 | -57.44288 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a958edc4-2383-3652-ac93-49dbe14ebec9 | -16.69279 | -57.45374 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4629823f-716c-30ff-9d4a-231d9111f6e8 | -16.66268 | -57.45241 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f319bab3-5828-3543-a3fd-1ca3ad503b37 | -16.65992 | -57.44824 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4b0e5e10-85fb-3d39-bd23-a1ecfcc5a55a | -16.65604 | -57.45132 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ee68fe1c-769d-3577-8e72-01062569f23b | -16.65383 | -57.44353 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7164a5e9-2b9f-3ae9-aff0-25ea5e4f219c | -16.65327 | -57.44714 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 233076e2-8295-316f-b128-3c2ccc9be464 | -16.65272 | -57.45076 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bf9af1fb-586f-361b-8758-78aeee57e3eb | -16.64995 | -57.4466 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a4b4eee9-f42c-3242-a989-a28754f562a0 | -16.64939 | -57.45022 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c8811e80-d595-3ccf-bf26-26ce66f8aee8 | -16.89187 | -56.71803 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b45ce1eb-f041-30c2-884d-a953d6c468ce | -16.89131 | -56.72176 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 967ed1ad-524f-3f7e-aed0-6438c2717b11 | -16.8885 | -56.71748 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5575d998-3201-3df2-8384-4bc81f0be334 | -16.88794 | -56.72122 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e1eef371-2c02-3eeb-8eb7-25599a0e4132 | -16.88457 | -56.72068 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7a336728-0e75-3d5d-806d-a12e703d432f | -16.88309 | -56.72165 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 50673ecf-efcd-3be6-a6e2-875cde4e27a9 | -16.88028 | -56.71738 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 24570aff-e308-36bc-88ef-c38cc4b36c7e | -16.87971 | -56.72111 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7e3d74c1-9e74-30cd-9548-e862a86d0611 | -16.87917 | -56.70189 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 65aa6d9b-15bf-3263-8116-1a1446bc975d | -16.87804 | -56.70936 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7bb0890c-6b02-3e29-99ae-cd1e2f196d81 | -16.87691 | -56.71683 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dd6a613d-711c-3a90-8211-04a27916aa8f | -16.87634 | -56.72057 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0065d1d1-aa1a-3f4c-b3f2-5737c6d80832 | -16.87579 | -56.70134 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f87adb9-c1f3-3d27-bc26-1bd6f00aff9b | -16.87523 | -56.70509 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6ab9ace8-ee68-35bd-aa71-a3756779f6c9 | -16.8741 | -56.71255 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 97d3a468-4a01-3dd3-a7d5-05c4e332c1cc | -16.87354 | -56.71629 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eb9994af-eafa-33bf-b30f-c6e7de0d2a24 | -16.87242 | -56.70081 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| be6febbb-d3ac-3b4b-afe1-ca759901fa91 | -16.87073 | -56.71201 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fcddb369-9e29-3d99-a1a6-bbf6eb7a8866 | -16.84825 | -56.70073 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8ca01e86-cf91-3383-a676-ae3895505459 | -16.84769 | -56.70447 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 41be3163-24b6-3ded-b03a-426c667a76bc | -16.84713 | -56.70821 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 811dff8e-7ff8-33ef-b069-9676aab88c1c | -16.84656 | -56.71194 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 73721a5f-0e63-32dd-8a34-268ebb44526f | -16.846 | -56.71567 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 52c34106-dddb-3c9d-a918-03d57d02b87c | -16.84488 | -56.7002 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 213b3840-3769-3694-bc94-02dae7c23889 | -16.84431 | -56.70393 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c93dc0d8-4e4d-3c49-90f6-b93790abd8e4 | -16.8415 | -56.69965 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5be016a2-ead4-3c5e-987f-2b2a9fbc7b05 | -16.84094 | -56.70338 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1801581b-584d-3c77-b69b-7022e3959b07 | -16.83757 | -56.70284 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8bd08dfc-c8b8-3ecc-8111-aa716e65877d | -16.77425 | -56.70043 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3b4173a5-55ba-3844-a33c-8d8451346876 | -16.77368 | -56.70416 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4ccfe873-cebd-35d3-9c8b-8fafafa574e9 | -16.77312 | -56.70789 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 97976326-8081-37a5-8d83-183fd9d1e3f5 | -16.77088 | -56.69989 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6ea5d1e2-fd10-3dc6-b150-d826d63e90a8 | -16.77031 | -56.70361 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b3f3d41b-d659-3776-8907-adacdb07a634 | -16.76807 | -56.69561 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5dfc8814-74d7-34da-9efe-61632c800bbe | -16.7675 | -56.69934 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bd81046c-522b-3421-9a8a-0ee15a380f44 | -16.76694 | -56.70307 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e483d156-6d45-391c-ab7c-047d81921464 | -16.76413 | -56.6988 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0b248c3e-17b7-397b-8162-710092e21b0a | -16.76245 | -56.70998 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5cf255fb-90b0-3d1a-b163-5f1c9d7b13ad | -16.76188 | -56.7137 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4dd6549a-d657-3098-8c4b-49273b4032c8 | -16.76133 | -56.69453 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 39d17cc9-84c8-3955-a592-89752daefb03 | -16.76076 | -56.69826 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 98da34c6-b487-31f2-baac-e1f2bd101af6 | -16.75851 | -56.71316 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README198.md)
