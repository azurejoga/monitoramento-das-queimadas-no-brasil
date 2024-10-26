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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e539e0ed-3e1e-3fab-8b05-44935c5538be | -17.68266 | -57.48117 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9c8d5c46-2cb4-3ac9-b2cf-001d888e4177 | -17.68233 | -57.48432 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 92f89775-20f4-3eda-a074-9867b1163088 | -17.68199 | -57.48745 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 09610779-a590-3a60-9f87-c03d2a7518a7 | -17.67959 | -57.48284 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d79b1418-aedf-33ae-ba15-e00f8cb5cd6f | -17.67923 | -57.48597 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| a514ca90-83ba-3aac-b9c3-d751c141d527 | -17.67887 | -57.48911 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 781dcb94-152e-3ce7-8f92-720e0690a762 | -17.67687 | -57.48679 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7cf2c63e-593e-3ef6-8a2c-f10164470b34 | -17.67412 | -57.48532 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4563aff0-a5a0-3347-8226-7dc2288753b4 | -17.67376 | -57.48844 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ef611075-89b3-3757-9bc3-58f893e202c5 | -17.67176 | -57.48611 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 84e6e8ac-d31b-38a6-b72d-caed972c6994 | -17.67143 | -57.48926 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 045561d1-d46d-3eef-a4c2-89847ebb07da | -17.6708 | -57.46899 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 715464aa-0c05-3669-a0fb-d720f467504c | -17.66901 | -57.48466 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 95d5a338-4f71-3076-a9ef-1014057a74e8 | -17.66865 | -57.48779 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f11df535-01b7-3f78-8618-4166cc269a3b | -17.66568 | -57.46834 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3b799ea8-d442-3fdc-9ae3-1232c586d597 | -17.66425 | -57.48088 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 07c2159f-a5fe-37c9-9e62-556c07febc3c | -17.6639 | -57.48402 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 810be3d1-ffc0-31a9-b910-8042aea14ada | -17.25036 | -57.5004 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c2e928e4-318d-33f9-a7f7-4c70f8156fdb | -17.24883 | -57.49999 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a7930447-8c4a-39f0-b1fa-953aae9b617a | -17.24564 | -57.49666 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 879432b8-fe2f-367a-8351-ddb3c70d5a35 | -17.24529 | -57.49975 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7b55c274-76c8-34f8-a807-0455ba50e957 | -17.23549 | -57.49535 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6ad797c4-44ed-310e-bb69-4f8107899968 | -17.23041 | -57.49469 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f6084f31-cb61-3026-a1d7-7c434ca8ddec | -17.079 | -57.47873 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 87905ad3-7b19-36c5-8b0d-5160d6f31954 | -17.07865 | -57.48181 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cef64af6-7eb6-34c6-9cf5-f5e0bd05359b | -17.07831 | -57.4849 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 91b363ed-169d-3246-9727-3db3f06b1cb6 | -17.07289 | -57.48732 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6c312bc1-524a-3179-aa99-30159fb135ab | -17.06782 | -57.48666 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| de7287b6-054c-396c-b41e-29b50735c10a | -17.06309 | -57.48291 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e12616c8-6f56-3a91-8180-15adb90198ba | -17.06275 | -57.48598 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aa6f291c-3378-34ba-86bd-01b4affdc710 | -17.05802 | -57.48224 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6b608b82-57b3-372e-bd46-e260cc273869 | -17.05768 | -57.48532 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ced2dc8-9c13-3b17-9b6c-e91611ade4b7 | -17.03202 | -57.53164 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ad46e671-d509-3392-85e3-41655384d8bf | -16.9158 | -57.66081 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4498633d-f9a7-34bd-a127-ee759ceb4ca1 | -16.90817 | -57.5087 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c01d1c03-a24f-3691-9578-2dd2c13dc5f3 | -16.90782 | -57.51174 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c37c6ba3-215f-3927-acaa-338d2d10e551 | -16.90347 | -57.505 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 47c40758-e81c-3b37-9bc3-e950d3ab1bb4 | -16.90312 | -57.50805 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| eea5c6a9-c17d-3d8e-ae35-88c5aa61a1cd | -16.90277 | -57.51109 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7b08a865-1d24-35f8-84cf-0cddedbd751e | -16.88872 | -57.67535 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b80c5ccf-1962-309e-9425-e9dcaf6f7765 | -16.88441 | -57.66877 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cb29b964-27ea-3df8-b7ee-d026b2b894c8 | -16.88372 | -57.6747 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 69bbd47a-dcda-3f73-a9de-f5fb5e406916 | -18.05555 | -57.37786 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 88a5c7c5-487d-3216-a2f7-9445d29f2805 | -18.05212 | -57.36104 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c488e721-f78e-343f-9a64-29482bdaff08 | -18.05037 | -57.3772 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5970c2b9-9d3f-3d35-bfc7-7a510fb9ca46 | -18.05002 | -57.38042 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5da88969-435f-3cff-b728-c3de7fcd4a05 | -18.048 | -57.35063 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8bb05f67-0b3c-3f00-bb21-4236334f32f5 | -18.04694 | -57.36038 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 074d374a-edf0-316f-a6f1-dc73393acd6b | -18.0452 | -57.37653 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e12bc773-e9b5-36cb-aea5-e0fe699bbcc9 | -18.04485 | -57.37976 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 87fd995f-cb71-3af2-939a-36555ce803cf | -18.04281 | -57.34998 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0306428f-f237-395e-8afa-d66d27128ad7 | -18.04112 | -57.31672 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b53b7a91-c7c7-37df-bbc7-8d94180eff1f | -18.03968 | -57.37909 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c71528cc-e4e6-3dee-b709-ded4054dbbcd | -18.03798 | -57.34607 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b47fa891-1779-3405-8b99-a4fcf303931c | -18.03763 | -57.34932 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 73ed10e2-e595-3c68-95b3-dd4e98d23ff8 | -18.03451 | -57.37844 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0885514d-123d-37e6-83be-de4ab5ff08f1 | -18.03419 | -57.33238 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a5b8b2eb-224c-35f6-a769-5c35b75931ce | -18.03384 | -57.33564 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1af07267-a6ed-33d1-9a62-7572ac26efed | -18.03279 | -57.34542 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 6a8c04a4-5916-34af-b49f-875459102be4 | -18.03039 | -57.31865 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 33638374-68da-3028-83c9-fcd0e3678e20 | -18.03004 | -57.32192 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 01cad3ac-ae9d-38a3-afe0-139e0a9a5bce | -18.02935 | -57.32846 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9e0f8442-3b37-3c95-8db6-e1647da2b19f | -18.02933 | -57.37778 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6f5364d8-b926-3275-9a6f-53eaf77a4196 | -18.029 | -57.33173 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 21d4cb0e-5f9c-3d3d-b8cf-ce79562513e5 | -18.02899 | -57.38101 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1efe0a48-1188-3eb5-92e5-0fdf1e90380e | -18.02865 | -57.33499 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 18c58181-3ea0-3ddd-990b-7f50db15a5f7 | -18.0245 | -57.32454 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a35254a9-1d51-3179-846b-415c3e942bcb | -18.0245 | -57.27476 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7ab8ed79-cc62-31ca-a8c9-abb325f9eb0f | -18.02416 | -57.3278 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7661ce27-ea30-3b52-9af1-2347ac082d5a | -18.02368 | -57.31878 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6bfe856e-a8fb-3720-b09f-8d6b311102f2 | -18.02366 | -57.27233 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f6c02435-3549-3b72-b571-164625d8a3db | -18.02347 | -57.33431 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 6ffdb9ef-b00b-3166-a6d2-e901d27ffb2c | -18.02331 | -57.32206 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e08a48b6-7a98-3aba-ac8a-b020ac7dc57a | -18.02294 | -57.32531 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e4bc15d6-2347-3fef-9c51-3d89d89f2fce | -18.02257 | -57.32856 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aee4f29e-463e-3808-8a9f-59daa97ed927 | -18.0222 | -57.3318 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 53472464-4608-3695-a223-7c480619e745 | -18.02183 | -57.33503 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 63024bf3-0dcb-36f5-81ea-40dbebd18363 | -18.02 | -57.31736 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1ad6ac48-4ac0-3301-a6f0-d1994dc67df9 | -18.01966 | -57.32062 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2123cf14-ee4a-361b-813e-10f37a6696a4 | -18.01964 | -57.2708 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2d8a3ec7-25ed-317c-bebd-121a3b2ba657 | -18.01931 | -57.32389 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c510c489-6db7-3d31-a7f1-8b7185b562ee | -18.01929 | -57.27409 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ddef0953-2299-3eef-8cef-39dc39bf0c00 | -18.01897 | -57.32714 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7818f034-2ab4-3958-ae2d-862463b604a0 | -18.01848 | -57.31814 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e58da865-9a8e-340b-9b31-d8b04df4ca3c | -17.79686 | -57.36269 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3c217292-c435-31d1-8c5e-04c4524285ba | -17.79432 | -57.36668 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 67a13cdf-7615-3dca-9e82-14bfa1d7b221 | -17.79408 | -57.33949 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f4b58c29-0925-3164-a162-4068f9bf273c | -17.79135 | -57.36522 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f75fda74-5e66-3707-89ee-4598ee27bfee | -17.78953 | -57.3628 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 96c05ee5-e123-30f6-8a2c-f810be1c5f1c | -17.78916 | -57.36601 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 17ec1140-2730-32d2-8fe6-e0de76781bb7 | -17.78727 | -57.33644 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 4a30a720-ce3b-3e2d-862d-5ecb6f34423c | -17.78691 | -57.33966 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b5d0a37e-7944-30a1-bb24-bbab24528e1a | -17.78437 | -57.36215 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d9f2d3e3-7969-334a-9327-4baee05fefb6 | -17.784 | -57.36536 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 84cb18e8-e48f-3c64-83d3-4be51d173f30 | -17.7821 | -57.33578 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 809c04bd-d8b5-3d7a-b68e-b6754805511a | -17.78138 | -57.34222 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 57411e0d-7996-39ab-ac49-5c0a1b693243 | -17.77032 | -57.34733 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 71a68208-aebb-31de-bc65-ad645d4cfb08 | -17.76997 | -57.35053 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| a1f84f48-e8e6-35c2-8ff5-4e564d687b94 | -17.7648 | -57.34988 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 0fb6f139-a2b2-38fa-b328-7903b365052c | -17.76444 | -57.35309 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |


[Clique aqui para ver as próximas entradas](README99.md)
