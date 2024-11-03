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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 566fde05-7087-3380-9dad-7c289c7081de | -1.0513 | -47.91191 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2176d2de-77ae-3401-b71a-07f2338ccc00 | -1.05088 | -47.91235 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e742a265-7d97-3f3f-99af-9b95cec4e04b | -1.05074 | -47.9156 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 415112dd-fbd7-3268-9428-1176426e14bb | -1.0503 | -47.91603 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b092b40-5567-3627-b189-eb547735dfcf | -1.05017 | -47.9193 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 98719c31-7696-3886-a57c-64920d9045fc | -0.74123 | -47.75975 | 2024-11-03 04:44:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fba42689-28f9-36c4-80f0-2d3500dc98c1 | -2.07097 | -48.53627 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9799239b-5a57-347b-9fab-82fd9164e030 | -2.06091 | -48.55679 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78875d64-7c78-3e88-8b46-c31744f09b2c | -2.00166 | -48.79179 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d5f788d-e06d-3571-8f34-51ddceaadc32 | -1.98141 | -48.70152 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34446f5b-91ce-3b6c-a2e1-1fb3da66a955 | -1.92984 | -48.65715 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92105da3-3f75-37e2-9033-bfed71c9ac35 | -2.12301 | -48.22074 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f4b539-476d-361a-96d3-c541c7cc0d40 | -2.08399 | -48.29347 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 071a8377-9d14-3031-85f0-e2b010ac7da4 | -2.08343 | -48.29714 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d509978c-0ea4-3c72-9832-69745d40332e | -2.08059 | -48.29295 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2b3b6a09-a34c-3bf8-a680-e952653ad659 | -2.08003 | -48.29661 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2191ca73-d63f-35a0-95e5-d9f388cb61fe | -2.24207 | -48.53627 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 42116d75-8457-3912-8d8d-2ad58956a77b | -2.2387 | -48.53576 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d2bd4ed6-09ef-3f7d-8c7b-118128953dff | -2.22855 | -48.51205 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e435759c-1a81-34d0-a18a-3269bf207c1e | -2.19533 | -48.83611 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f69cf10-6c4a-31a2-990b-117f242e1b1c | -2.1919 | -48.79205 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d46c9162-72f7-32ab-884f-f47c4b0b26cf | -2.18974 | -48.828 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9af66a6-a7a5-37fe-843b-02a8c03b303e | -2.18855 | -48.79153 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3600951f-449d-35c0-a5ac-8f2ae3a205cb | -2.188 | -48.79507 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92aad712-2e3b-3125-a3b9-ac891b0f304d | -2.18465 | -48.79456 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddc078e5-da41-3e58-b17b-b3d0fe94fb4a | -2.18189 | -48.81229 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b97b2c8f-52a2-351b-b292-e93637ecdd7a | -2.17244 | -48.82897 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bbe1e53-ac96-3e8b-a96b-a66e5adfa01a | -2.16663 | -48.73359 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8b6474f-67ff-30ff-8750-6969c65a8e8b | -2.16574 | -48.82794 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b524bdd-45ae-36d7-ae58-5543a365b039 | -2.16217 | -48.74019 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25f71add-2151-35c2-bfd4-5663512ba3c3 | -2.16184 | -48.83097 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01fe1118-9a55-3e5b-909d-0eda2efaa55a | -2.15881 | -48.73967 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4a58ed-387c-351a-a05b-f2b920566bd4 | -2.15849 | -48.83045 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 2c33c4aa-23cb-3450-aa37-186a12a72ba4 | -2.15815 | -48.69947 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26d5f2c0-c5c3-350b-8f6a-4b24ed661cfb | -2.13087 | -48.74266 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be659990-94db-3877-9e4c-1879ec8a920d | -2.13032 | -48.74622 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce35a16e-12b8-3c5e-8b85-49a29c67d071 | -2.35687 | -47.91279 | 2024-11-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1017300-c0cb-3f17-ad62-0599704a8b18 | -2.35628 | -47.91656 | 2024-11-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96881d90-0d46-3d0c-a5fa-3282c1bb0e42 | -2.35557 | -47.91566 | 2024-11-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68536e07-a129-3a6c-ba3f-f3953a7de727 | -2.35224 | -47.9198 | 2024-11-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f64e91-5af5-35bb-9ead-532e5c11cf35 | -2.298 | -48.4074 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71fdb1cd-1e9c-3b74-b4c2-b12ae19dcd7f | -2.29573 | -48.3996 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45677901-7af4-36bc-8a0d-aa8c0d52705b | -2.27894 | -48.46387 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e7b7f4c-6d58-32d9-99d2-6825ca8c539a | -2.26014 | -48.26367 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e312ec0-ff64-3057-87d5-f5c8dd55a905 | -2.25957 | -48.26736 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3cee54e-30c0-3b96-9823-f73e0a16a87e | -2.25673 | -48.26315 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d886a54-4ff7-37d7-bf26-dc4e27a1794a | -2.25616 | -48.26684 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4430fbb-1fb3-3ac5-b830-648f4a86248b | -2.21725 | -48.47334 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16e5152b-6ae6-30d7-a6ca-9a56af9efd1f | -2.21289 | -48.16213 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ff52ee6-10a0-357d-9c12-a0b86fa3ff05 | -2.21233 | -48.16581 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7415693f-6fae-3a6b-bb8f-da5c651dfc6c | -2.21177 | -48.16948 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9591506-6274-3487-8b17-d35f643e1b21 | -2.20948 | -48.16161 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48ceddc1-ef90-3d77-a530-47e3374d6d1c | -2.20893 | -48.16225 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e04bee0-a4da-3877-a3b9-b6ca840f9b57 | -2.20891 | -48.16529 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a23b0803-6fd7-3385-b834-f8536b29337d | -2.20835 | -48.16896 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7fa8a02f-ea5c-3d6c-9e08-7b333e31c9ad | -2.20778 | -48.16959 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 12c012e0-672f-3234-a7e0-d530d09990d9 | -2.20466 | -48.35253 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ddabf03-3184-36d3-84a3-8701c7a7668f | -2.20126 | -48.35201 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c802dfe-a052-3cea-b2b6-35078bd0fb5f | -2.19958 | -48.36295 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| befbf533-1364-38e5-86de-fa61e407ba7d | -2.19787 | -48.35147 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6c3e13c-83d6-3bd5-a05f-563d351f29f9 | -2.19619 | -48.36242 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb700bda-1bb0-3b88-8768-cf2c8050ad87 | -2.18819 | -48.32385 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08b63487-5f6c-3321-8742-8fcb29206297 | -2.18764 | -48.3275 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc0f5c13-b747-36f6-b14d-47aaae9c54ec | -2.18424 | -48.32698 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05f5f4b2-8a79-35d0-b095-3ab18afd7ec6 | -2.18312 | -48.33429 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d65b174-0d3f-3d1d-bff5-8584e41f67bf | -2.18251 | -48.33107 | 2024-11-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed9d6985-8d04-337b-83b9-2935faf73d9d | -2.1815 | -48.3676 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24715824-0806-3c86-b6f7-a9905ee7ff11 | -2.18105 | -48.41591 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd78c5fa-8752-3a5e-8b1c-6595bdc6432a | -2.17811 | -48.36707 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a083217-bff6-319b-8fe3-3251abd0cc82 | -2.17739 | -48.36382 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11979499-6d30-3c9f-9d20-bcbd8fe3b597 | -2.15591 | -48.34563 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e063d696-6b09-34b6-862b-c296da62c5cf | -0.8054 | -48.62973 | 2024-11-03 04:44:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656f5d79-e199-39a7-9be7-38ba75295cb1 | -0.64394 | -49.40376 | 2024-11-03 04:44:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f595568a-5e8c-3f5c-9b0b-0e684146bba6 | 0.08858 | -49.86808 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd6300e2-b866-34b5-aaca-a2ea6c6eca47 | 0.08804 | -49.86464 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99a4b49-c7ac-3d2d-9c0a-8cbe5e4babcd | 0.08751 | -49.86121 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 773e749c-6744-3e35-a8b8-fea85ac3348e | 0.08474 | -49.86515 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45cfe21f-416d-3a3b-ae60-9f7996f8d88c | 0.08421 | -49.86172 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3b6c240-30f8-35a4-a193-58b0cf7821dc | 0.03506 | -49.5467 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6f7f3c5-9ad5-3834-8459-3261790b3855 | 0.03453 | -49.54328 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03ca9e85-3219-3435-97de-218a77e31907 | 0.03176 | -49.54721 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0fdaf41-034c-3a6d-b284-865e0e44dc90 | 0.0307 | -49.54036 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6ff889a-c9bb-3606-9c3e-c2ca54a61b83 | 0.02536 | -49.50614 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75557c51-5d8b-3add-83ed-082b1256de2b | 0.02483 | -49.50272 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2551e994-fe8e-3c76-b738-c12f876fc0ca | 0.0225 | -49.53111 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7058d88-4bf4-3ab4-b3c7-2d011e788bca | 0.0208 | -49.54188 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ca7fbce-0d02-3293-8576-53aedd897c74 | 0.01751 | -49.54239 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32d32454-4157-3e38-9d77-a2ed08ee8ac1 | -0.64104 | -49.6174 | 2024-11-03 04:44:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0f13d4-31ef-35fd-afa6-8b364ed4b231 | -0.64051 | -49.62082 | 2024-11-03 04:44:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5418dbeb-6e0f-39a2-b0cd-a32970518788 | -0.63774 | -49.61689 | 2024-11-03 04:44:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99b4f749-9119-321d-a43f-3004fa6c45bb | -0.56652 | -49.54903 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6b962e5-ffbb-339d-9921-834487df0b25 | -0.45757 | -49.87936 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc6ca285-ed0d-3f7b-a337-4ea209f5c3df | -0.28824 | -49.82862 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47c1f5c5-00ce-34ea-8866-b9d00672115d | -0.2877 | -49.83205 | 2024-11-03 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb8b3944-21bb-3491-aa94-2a43bcba1523 | -2.22683 | -48.84799 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 933b2ad7-cb85-37ea-a5b6-a9405c6df968 | -2.20427 | -48.84473 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4350bcbd-5be8-3aeb-8966-34c5cc1b41d2 | -2.20372 | -48.84827 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88cd22c3-4559-3d37-8394-69b436528ce5 | -2.19478 | -48.83965 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 118c95bb-6a6c-3e28-926c-97629fa0d16a | -2.1873 | -49.12634 | 2024-11-03 04:44:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68a0831c-248a-37c6-ba9c-914243209686 | -2.15411 | -48.85875 | 2024-11-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
