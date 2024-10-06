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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 908fceaa-ba9f-3b43-8c24-513969518a05 | -16.50774 | -57.73783 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 05784fcd-1291-3dee-9350-313dc0ca1ec6 | -16.50288 | -57.27406 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a4573e04-31e1-3a80-a881-643880f11040 | -16.50208 | -57.27789 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 230e76f6-8150-3884-b1ef-77c0aa78d17f | -16.49116 | -57.24687 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f67d5ee9-62b1-3b58-98b1-5c4268ae63c2 | -16.48792 | -57.26228 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 3cf751de-fa8b-35a6-a685-01905c94b32f | -16.44786 | -57.3141 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5f5597fd-c04a-383a-837d-5a1f024e4116 | -16.4443 | -57.31329 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a60b2e27-012d-3dda-8de3-e98d52fca130 | -16.43879 | -57.28347 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d6f15108-776f-33c3-9611-a09d5cf9f543 | -16.42512 | -57.34979 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0aec4712-96c2-3133-9b70-4f97a1fefe1c | -16.41398 | -57.34714 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8c914d3b-affa-374e-84b6-5460254f4145 | -16.41224 | -57.38383 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b1c33e9a-f019-3494-b5e6-415cdaaad099 | -16.40188 | -57.37728 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2a82554-4e53-339c-b2a0-3851eb2ccd1f | -16.3812 | -57.36409 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cb773c14-47ea-3532-83e8-b72f62cd898c | -16.37397 | -57.37064 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9bef4cfb-2eee-332c-b7d8-dfdcc73741ef | -16.61646 | -57.16702 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 88778960-55bb-3d3f-bb7d-036e3fb724ba | -16.60218 | -57.2075 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0a8bbe8d-a445-30f0-8b98-92a53d73c260 | -16.60138 | -57.21132 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 66ee212d-22b7-3cf2-ad63-0dec72b5b042 | -16.60058 | -57.21513 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 57197702-3e77-3573-8736-9d6764f93add | -16.56694 | -57.16049 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 065370ea-80a3-3181-a697-efb1bebf5038 | -16.56146 | -57.21516 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 483b5e3c-fc10-3ad9-a9c9-03e81c095e9c | -16.55673 | -57.21006 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| c62af22b-3684-3461-bfb0-279a6d928161 | -16.55122 | -57.20879 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| b66ed171-140f-38f5-9f63-3eea8fff5202 | -16.55043 | -57.21261 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 656aa22f-f7b8-30a4-9b8e-1818a480a954 | -16.54964 | -57.21643 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f63a96f9-edab-3c55-b720-cc867f8531f0 | -16.54491 | -57.21133 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e4113531-d084-3109-9a94-b8941e2810ab | -16.54412 | -57.21516 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 00049b52-cc44-318f-8544-4c43a2859cbd | -16.53543 | -57.22919 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5835de6a-2087-300d-94f7-4fe96dc8a551 | -16.53385 | -57.23677 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b6efe26-40a9-3f3d-9afa-fd0faad91228 | -16.50862 | -57.24662 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f981a3fe-605b-329c-a006-7c169ffc1e15 | -16.5039 | -57.24146 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 380e611c-58c9-3790-9c87-25f5738abe7d | -16.50226 | -57.24928 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f7fa1c5f-b512-3318-a920-f26065527262 | -16.49587 | -57.25207 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 35361b16-e2e3-3110-b0a4-15c965b79183 | -16.49425 | -57.2598 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7d704fa6-3df4-3912-83c5-b0a7106155c8 | -16.44595 | -57.27692 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 197a9944-d22c-3619-a551-3ea20a17f0b9 | -16.44419 | -57.27659 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| af7d58d4-a88f-3176-b9f1-3e52032ccb08 | -16.43404 | -57.27826 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 12c6857c-a356-3eab-996d-3d2a0ec73ba1 | -16.43324 | -57.28217 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f7b74d43-6d02-3a6f-9ab5-e68c7f1c9458 | -16.50688 | -57.74188 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 365b14e1-4746-35fe-bdfb-63ecc465bde2 | -16.42593 | -57.34586 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dffa330a-7f21-3e5b-811a-a21722f8f46c | -16.39629 | -57.37597 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a0ac01ab-80b6-3f3b-af32-e1a363e70bf2 | -16.39071 | -57.37466 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 865448a9-ce88-39a9-bb19-c77cea60f011 | -16.38841 | -57.35757 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 99578003-c428-32ae-8c7e-03a50f527c8b | -16.3876 | -57.36148 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 429804fe-4f7e-3038-b700-ae6b3b922b1b | -16.38512 | -57.37334 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6c646af3-11dd-370e-8746-8cae6c4e2022 | -16.37872 | -57.37595 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 99296472-c57c-3ff7-9e5b-6afb363f13ae | -16.37231 | -57.37857 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 29467642-b507-3538-8705-12e1932f27db | -17.84675 | -57.68089 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 163e7f53-60d1-3fb8-8eb7-d4c0a388fb61 | -17.84591 | -57.68481 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d234de2e-b199-3ac4-a551-64a56794a42a | -17.84508 | -57.68873 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4a822850-b8eb-3c7b-a79f-befa53000f79 | -17.84425 | -57.69265 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8e5e188e-c2f2-30f6-a77e-0af35b2de20b | -17.84038 | -57.68346 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 51a65b24-5a8f-3fa1-8431-fc8c949e0e39 | -17.83954 | -57.68744 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a43c30ce-1b80-30f5-91c2-189282624333 | -17.8387 | -57.69137 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 00de9815-f637-3594-b0dc-fa98286ad5c5 | -16.92467 | -57.69937 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 220f0fba-d913-3786-aba8-c92b1234e8b3 | -16.92299 | -57.70746 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e1df077b-34ee-35c8-bacf-df6a03e85b30 | -16.91903 | -57.69804 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 525cee3a-30cf-3e50-b599-5b66f0110e21 | -16.91545 | -57.69559 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1e1934ba-8c78-33fc-908b-d8aae42576e1 | -16.90858 | -57.69131 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4344c075-00fe-3667-8d09-b777f50dc766 | -16.83601 | -57.46128 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8b41039a-1c0c-33a4-ad46-db6b2b337694 | -16.83125 | -57.45607 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 228dd95f-2000-3141-aa21-411654b107ab | -16.83044 | -57.45998 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3c8b3734-59c3-3a7c-b700-8ade5dcbc90a | -16.82405 | -57.46259 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5d904afd-c78e-3c93-b5c5-86b7b2a71224 | -16.82012 | -57.45344 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5f04d8b2-0965-3760-91fc-85bd2d5c1e48 | -16.8193 | -57.45736 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9e322497-01b8-3f38-9b18-7394ad634e65 | -16.81536 | -57.44823 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 395aa155-8985-3e46-a6e8-8cc26b9b11ae | -16.77506 | -57.50076 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8cc25301-c99d-3dc0-98f2-6c911ef58ba4 | -16.77422 | -57.50471 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 82329a9f-5e6a-3ccb-9da5-2ee1b0fb6c03 | -16.77222 | -57.45876 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 42b9e7eb-91b3-3465-9fe7-b09eac021f45 | -16.77198 | -57.48759 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f9dbdd0b-361f-3d9b-8d83-5dade5161b6c | -16.76914 | -57.44569 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d12efd6a-49d3-3cc2-a853-20cf8c2cb6e3 | -16.76889 | -57.47448 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 79f23304-2a7e-3a33-8b17-d5d0c5ead956 | -16.76472 | -57.4942 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5590fe08-631a-3742-8056-50bd5b8cc2aa | -16.76387 | -57.49815 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ab22e39c-56c8-3e7b-b3c3-870bdeee9858 | -16.75856 | -57.46796 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 84572f11-ed06-36b4-8959-2dd54401c5da | -16.70784 | -57.4719 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 95399b94-8be2-375e-94e3-23740c396ff1 | -16.70308 | -57.46666 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 0cb2b675-e4c0-37a0-8e3a-04ba101534cb | -16.69831 | -57.46142 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3b4cfe6a-5be8-315e-af05-0c42dced75b2 | -16.69749 | -57.46536 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| a0e52133-00a2-35a2-94d2-147e436d79e5 | -16.6888 | -57.45094 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 072d2eee-6b33-3c54-82f4-147b63697e9d | -16.68321 | -57.44964 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cde840ef-9d49-3cad-891a-7bdc700213bf | -16.68156 | -57.4575 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 754c4024-dcaf-38fb-9b40-1af1feb54440 | -16.67264 | -57.472 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f9f579ca-15a4-3ca5-af25-97cf9c3c0eec | -17.14787 | -56.75849 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 76e31056-6798-35c5-a2de-0bb61905a5d4 | -17.12008 | -56.78504 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 233b5de0-16eb-3090-8b06-da155c377cdb | -17.11979 | -56.74519 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d0749c49-4a01-3a87-9fee-91ff244251b8 | -17.11627 | -56.76263 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3faa4415-a0e2-39c3-b035-7cdb1baebcb2 | -17.11486 | -56.76962 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a87ffd94-8ca2-36ee-a1b4-d164f3fdec07 | -17.11477 | -56.78381 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0d4780e2-d897-308d-80ac-86d06ac29b40 | -17.11458 | -56.75813 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 50e59e81-7807-3fa6-a09a-2e64e91670a9 | -17.11379 | -56.74743 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 15a8dff1-e4bd-3d72-9392-ab9dee4a7b44 | -17.11312 | -56.76511 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 419fb3cd-87d6-3168-9edf-9eba7f2b3831 | -17.11148 | -56.74646 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 82f58f2e-002b-3bec-ba2f-617a337a1fb1 | -17.11025 | -56.76489 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3339f696-1007-3e1c-a1ec-ba527e6f1684 | -17.10846 | -56.80122 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cd14bac1-8cf5-3ea9-a4b3-9d2ec5a0f484 | -17.10577 | -56.80011 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 17e99a4c-29eb-3f1c-98a6-99a43e21af0a | -17.10314 | -56.79997 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c6a0f9a0-1a0f-340a-b123-e3899fb139fa | -17.10045 | -56.79889 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bc9dc3bd-4b95-39e3-880a-822ce9c34016 | -17.0997 | -56.80243 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b4345b62-7589-35cd-affc-f281a563af93 | -17.09782 | -56.79874 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 51af3ec3-5e96-3434-9225-cb51ef6216e7 | -17.0971 | -56.80229 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README86.md)
