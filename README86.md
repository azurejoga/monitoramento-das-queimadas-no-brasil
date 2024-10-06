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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbc63bbe-dcde-3c82-aa0c-d195fd33be02 | -17.09513 | -56.79768 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 52eedccf-69b3-362c-bd17-5acee56be281 | -17.09438 | -56.8012 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5688cea0-8a88-3f8b-ace8-0b811c351b38 | -17.0925 | -56.79751 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0bca83ea-6b86-371a-ab75-32678d280aa2 | -17.09178 | -56.80104 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d54e7b94-ca4c-36ba-8018-794eeb185b3b | -17.08906 | -56.79997 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 091f1f8b-2405-3dbe-ad75-934571e6fc7c | -17.08646 | -56.7998 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2fa384ff-057a-3ae0-a8ae-5deced8e7ab7 | -17.08041 | -56.80211 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2d853be0-c76d-3045-9ad4-08fd7ae9d2e5 | -17.047 | -56.80178 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 48c754a7-f64f-3878-bb31-05651b24d595 | -17.04167 | -56.80056 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fe03dd47-1213-313a-8e11-b81029c2856e | -17.03422 | -56.72911 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 53f8a065-acc6-35a2-a6cc-71a43631ceb8 | -16.68962 | -57.447 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5773a62d-9a64-3e75-a2bf-1058d8f5704b | -16.67347 | -57.46805 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fd9d722f-260a-3d58-b1e3-e1275ff98256 | -17.14329 | -56.7538 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 577c5483-744c-3390-8072-faa084a132c0 | -17.14256 | -56.75728 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fedd5cc0-da3a-3fcb-a0e5-fb5d1ac0c526 | -17.11843 | -56.76634 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| da5cd131-7fdf-3d72-bff6-2b7cd932a43e | -17.11768 | -56.75565 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ded1c7c5-92b1-3fbf-a641-51b50ab299e7 | -17.11751 | -56.74421 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f9d779e1-f894-34c7-85a9-0ee40d26d085 | -17.11698 | -56.75914 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b8048a75-f5d9-349b-8422-d0740da81b00 | -17.11623 | -56.77681 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8e024b9a-f0ca-35da-a524-9cc220e157c2 | -17.11556 | -56.76612 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6f67894c-a5d5-3916-91c9-1c3b37967317 | -17.1155 | -56.78031 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 98e7fd6a-2d1f-38d4-a500-51906afd3a4d | -17.11532 | -56.75465 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6c5acc0e-fc43-345b-9625-7f9ded74a185 | -17.11385 | -56.76163 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5ff458ab-6282-32e9-b527-50b3c3604cb8 | -17.11308 | -56.75092 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 133ceea5-193e-3802-8db3-dcfcd6e64e72 | -17.11239 | -56.7686 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| acc5621b-86eb-3dcc-aff5-7bd3b7af254c | -17.11238 | -56.75441 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 76963da6-46cd-39dd-a342-bb6153c365c3 | -17.11096 | -56.76139 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 574ae2bd-6af0-32ee-9ef3-fb474874015d | -17.10954 | -56.7684 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3cd03969-238c-30b1-9af3-88b0386699d4 | -17.10855 | -56.76041 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 045fe6ae-416d-3d39-86a2-bd01d4d8bd25 | -17.02964 | -56.72442 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5502425a-0ad4-3788-a340-7d9ddee8d5b2 | -17.02891 | -56.72789 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b0f075a-bc51-3d6f-9b67-c57f50329523 | -17.02868 | -56.70238 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 37e32478-22e6-397b-b799-4849b17dec8e | -17.02818 | -56.73138 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 08b1b572-9872-3148-80c6-4033c16f884a | -17.02796 | -56.70584 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 55ffe01d-7f89-345c-a2fc-28a8a5963f08 | -17.02746 | -56.73487 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 944ee70c-944a-36ad-9aec-fd54b50ad9c4 | -17.02723 | -56.70933 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| affafcfb-c1ad-3785-be05-706d891abc39 | -17.02673 | -56.73837 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8c93b11c-35b4-3d96-9ef3-effa63a05584 | -17.02578 | -56.71627 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| af8eb298-4775-3e39-91f3-ff04368e51bf | -17.02505 | -56.71975 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 378362d8-8645-3616-8895-e63dd7180d98 | -17.0236 | -56.7267 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3558b0a4-8c0b-35ad-b6c9-05fda0d10cb0 | -17.02266 | -56.70464 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 160287a3-1424-3481-9ded-b2df1d13de51 | -17.02215 | -56.73367 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| afe78b2e-48ce-3a9b-a120-991cfb427e0e | -17.02142 | -56.73717 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 98cadc5d-ce6a-33cf-8274-7277e924d70a | -16.79738 | -57.39495 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9019d6bf-a17d-3c4c-8a81-1e5fa274fcb0 | -16.79656 | -57.39884 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2785209f-a5aa-3c39-9f00-66b6af552615 | -16.92587 | -57.70226 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7e7c2da1-8b37-3929-ba41-dae0f4a6a66d | -16.92501 | -57.7063 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7d5fe0ec-b1b4-3505-84d2-fe1e04556576 | -16.92383 | -57.70342 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7da7371f-e34e-33b9-baca-da925f2b3b5d | -16.92109 | -57.69691 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3848b910-0fcf-35ed-840f-2ed108d25344 | -16.92023 | -57.70096 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d3a0758f-d5a2-339e-9196-3cba44f2e37f | -16.91986 | -57.69398 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0f796edf-6913-31de-89e5-adf8fb15d6c2 | -16.91422 | -57.69265 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5252e461-cbd3-307a-9a76-a654ebd1b8df | -16.91068 | -57.69024 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fa99e4fa-ca9b-31ab-81d0-ea6b5d5ee4f5 | -16.90981 | -57.69427 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a507732e-ae7f-3b2e-89c1-0be60f2f4deb | -16.84796 | -57.45998 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| efc20155-ebc8-3c60-b2ff-ae9abf277449 | -16.8402 | -57.45819 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3b2e91a5-9b6b-3edb-be58-f52953a328d8 | -16.83682 | -57.45737 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 004df2c5-ad80-3453-af1e-51e9788d6cd8 | -16.83665 | -57.80737 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 05c32f23-6246-3934-a1f2-d0e049d88542 | -16.83207 | -57.45215 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 030263d7-2abd-3504-8394-dfb53754eab8 | -16.83097 | -57.80603 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 582878da-7860-3325-9a96-05624ec8cee1 | -16.83009 | -57.81015 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 7908ad6b-d101-3b55-88c6-7cd70290df04 | -16.82568 | -57.45476 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f4ef3181-17d6-3e59-b15a-83619ccd96f9 | -16.82487 | -57.45867 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7eea30d8-0c35-3374-8d7f-7c757e910111 | -16.81848 | -57.46129 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a52b3645-d5c8-324c-8c0a-ef4277179914 | -16.81454 | -57.45216 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1921e304-056d-38ae-8251-72ceece84202 | -16.78834 | -57.43783 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a3799b7c-d31e-3ce4-aa49-39975d1ac391 | -16.78669 | -57.44567 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cde8bea0-0943-33d4-a07a-1faf5929267d | -16.78112 | -57.44438 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 45b3be87-a213-3e65-bb54-763f74afb07e | -16.77305 | -57.45484 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2a280751-568c-3e64-ba30-3c7ff7811794 | -16.77281 | -57.48364 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a1a7744f-fc0e-39e2-a793-11c4a9cf9338 | -16.76973 | -57.47054 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ca8adb29-8d64-3ab5-95cf-1606af3bb986 | -16.76723 | -57.48235 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 47f3e485-5d9d-341f-9b92-5779bc6b7278 | -16.76639 | -57.48629 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 01e05a72-e6dd-3252-9c0a-391c16a16504 | -16.76555 | -57.49023 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 99e60b18-d873-3601-af6d-89ee11730a0e | -16.7608 | -57.48499 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c74ebb8a-9173-3f2f-a8fc-ab06cc87f249 | -16.75828 | -57.49685 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 562601b8-2b2b-3e34-9184-91d36aee3625 | -16.75579 | -57.46658 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e4347abc-5c13-3842-b8db-b6bbe4ed0a90 | -16.70225 | -57.4706 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf083b4d-eee6-3b4e-85eb-9c0be780c429 | -16.69666 | -57.4693 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| cac5fe05-2215-3a3b-be84-d73f35c1b4e2 | -16.68714 | -57.4588 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0590065c-ab75-344b-8abd-9ff7eb8c0efa | -16.68632 | -57.46275 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 956b922e-f0b3-3ea7-8fa8-313ec8e9bb18 | -17.16574 | -56.9703 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f2291eab-7caf-3819-9683-69e70b18526d | -17.15963 | -56.97266 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 087900f7-adc8-3bb2-937f-de1af2c68e6c | -17.11567 | -56.80611 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c4f1ab9f-11a8-31a8-81cc-7d8ca900a585 | -17.11493 | -56.80962 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9dadb2a6-a83d-3c5d-b508-96e19a90d290 | -17.11035 | -56.80488 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5410cfc1-f632-3b08-9145-0f9909880d54 | -17.10961 | -56.8084 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 47593eb1-eca3-3d4d-97b4-23ec62ce6ce9 | -17.10887 | -56.81192 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 423e878d-9217-307a-a86b-55cf01f4a685 | -17.10775 | -56.80476 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 842fc9c3-fa4c-31cb-8422-ceaf3ef58ee8 | -17.10703 | -56.80829 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d9d0e052-f4b8-3970-9c7d-a388c27fabf6 | -17.10632 | -56.81182 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6d03edc4-df32-3198-9c5c-52f6164d012c | -17.10503 | -56.80364 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 35d03789-e1b5-3f4e-aacd-12b5e26db8cb | -17.10429 | -56.80716 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b407dafb-0464-3d03-a6f8-1fef90675454 | -17.10354 | -56.81069 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 6a6b4949-47d5-39f6-b411-0b9e56a97034 | -17.10242 | -56.80351 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c18b571f-0fac-3414-9efd-1085cec89e25 | -17.10171 | -56.80705 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fda32a21-4402-3bd1-a7d1-813bae8a4c28 | -17.10099 | -56.81058 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0b34a572-261e-3b3d-8b7d-5e258a90278f | -17.09956 | -56.81763 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 08cfb863-4949-3a9e-bc1f-28cb3e26dd19 | -17.09896 | -56.80595 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 52c711d1-f621-30a9-917b-6ac536f4e642 | -17.09674 | -56.81651 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |


[Clique aqui para ver as próximas entradas](README87.md)
