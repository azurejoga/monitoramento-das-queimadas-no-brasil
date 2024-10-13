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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ec857c8-f9cf-3dde-abd7-120ec0f449af | -4.48932 | -48.10849 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cb54ec0-981d-3f6a-8da7-28a9ed4069c6 | -4.48545 | -48.11147 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79b689f7-9869-32d6-b03a-20e77a993c8a | -4.46988 | -48.12354 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b226912e-4473-3845-8d3c-d2ab9a0987de | -4.4176 | -48.69965 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8baf7dd0-1c5a-3e1f-a06f-2767d1783d4e | -4.4143 | -48.69915 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98b688a0-a42b-343e-8674-539ffa5529ff | -4.41376 | -48.70259 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a43573b-95f8-3115-a9ca-da3394c0df0f | -4.41323 | -48.70602 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 128cd53d-9388-3601-a497-c9a38333d90e | -4.41269 | -48.70945 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6bc030-fe20-3baa-abb1-2f40edf96573 | -4.40993 | -48.70551 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47e12055-b3ea-3b23-8a79-60a8e8cb0e73 | -4.40939 | -48.70894 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16b1793-2709-3a9f-993c-5a9cbf70c2b0 | -4.3863 | -48.61381 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79e8e77f-2016-3753-8474-e4d335d0cd2d | -4.38576 | -48.61725 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a265e633-e28c-38df-82f7-e3cd2731dfb7 | -4.38345 | -47.76163 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69d61d30-8f6c-3499-9d0a-ba8432a13a69 | -4.383 | -48.6133 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8934252b-59a3-3505-a13c-a33308723222 | -4.37916 | -48.61623 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 421a88ef-2457-3eb5-a788-e85845e88f95 | -4.37862 | -48.61967 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb809ed4-9f0c-39b6-ab5c-2dce44f72f40 | -4.37586 | -48.61571 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea6eb7f8-1fd5-3c7f-a6a0-7df2e7e787d2 | -4.37532 | -48.61915 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26ce23c2-aceb-3bfd-88c4-f866f6a44be8 | -4.31875 | -48.63504 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a96489e-88cf-39dd-8ab2-d7264251a099 | -4.31545 | -48.63452 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da908bf2-635d-3d95-9e45-d6facdc6bbfe | -4.31491 | -48.63797 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fba92e2f-e9d0-3cee-8f26-c4358ed7e4f5 | -4.31437 | -48.6414 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e20c25f-cbf4-3098-924b-7d6a73c68e5b | -4.31053 | -48.64433 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 374a8400-c321-3dcc-8938-61391f09c725 | -4.31 | -48.64777 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1bc4ed5-fa47-3de7-9ef2-797292ac26cf | -4.28511 | -48.62972 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 611616da-750b-36c9-b0e4-a36cc903da9d | -4.28457 | -48.63316 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b5aec2-0015-328b-a22e-92329cd76826 | -4.28181 | -48.62921 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 317b8d7c-ef61-3de4-a51a-3b0c0bf6a873 | -4.28127 | -48.63265 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b232217-9baa-3d43-a93c-244a1b853d46 | -4.27998 | -48.22949 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ca069f6-4556-3f02-8f99-00a484d5548a | -4.27944 | -48.23295 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dd199997-e5ce-3792-b783-b15f9b44773f | -4.27851 | -48.6287 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d582fab2-9b95-3240-9b92-22b65783ccc4 | -4.27797 | -48.63213 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bef35f27-7788-3386-864a-a2ee6ac86f0e | -4.27667 | -48.22897 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9a49f6-b357-3eb2-9b3c-a0c915baa8da | -4.27613 | -48.23243 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 424cb55f-3d1f-352d-a129-e25f6dc421a2 | -4.2739 | -48.22499 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3579db01-6e91-3cfc-856e-dd8820be67a0 | -4.27112 | -48.22101 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b681e5-406b-3608-a3cd-4e80a3962bea | -4.27058 | -48.22447 | 2024-10-13 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ec8b60a-2546-39c7-a150-e2af28a10138 | -2.78903 | -49.29512 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| de011e28-09a5-3bcd-b62c-038bccfd4cb0 | -2.77809 | -49.36435 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0536351-152a-3def-86ee-4612768bedf8 | -2.77478 | -49.36384 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 457a3867-40f3-37e8-b59f-38b6fbe656a7 | -2.77363 | -49.32817 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71296c6-e7e0-32ce-9434-d4072900a1ff | -2.62135 | -49.08455 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ea2bc3f-df2b-306b-9494-f901fa4f1e23 | -0.17742 | -49.19202 | 2024-10-13 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 913a4b5e-5080-3ec4-b72b-6b9f3dc43756 | -1.27268 | -48.87202 | 2024-10-13 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36fa76f6-7410-33d2-871b-959a4df2f13c | -1.00522 | -48.68867 | 2024-10-13 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3169df59-7afa-3b7c-a62f-b75218c6b93f | -1.90938 | -49.52032 | 2024-10-13 04:38:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c55116c-dea9-39e4-ac00-5d9bfb075fa4 | -2.17581 | -48.84186 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 752f3dec-7e53-32f7-b69e-e097e17ea3ec | -2.17527 | -48.84529 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48d9b258-020a-3f93-b8c0-c388c835f57c | -2.17251 | -48.84135 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 545fbf95-22a6-3f0e-aa5f-8769121c0319 | -2.17197 | -48.84478 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4c76129-a89e-3aa7-95fc-b0815997ac68 | -2.17143 | -48.84822 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c852c110-9507-306e-8134-24c8c7774857 | -2.16867 | -48.84427 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c328ee5-b5e1-3ff5-907c-0737f206686b | -2.16038 | -48.83244 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e31590-b913-32aa-9af9-36fcd94c0136 | -2.15877 | -48.84274 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c958c6-dc71-3a46-baf2-33b04387cd63 | -2.15601 | -48.83879 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2e52eab-a304-36d4-af90-b4a6df24da53 | -2.15547 | -48.84222 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08879a35-993b-3a31-9a3c-087d6be124a1 | -1.46799 | -49.31865 | 2024-10-13 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fc3f370-5aed-3bab-a1e4-266afe5d5c63 | -1.46522 | -49.31464 | 2024-10-13 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d959bbf5-f78a-33c2-bf99-4b76b2ebbc35 | -2.74616 | -49.52313 | 2024-10-13 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a14348dd-6a47-3874-87a7-fa26d661ef1a | -2.74284 | -49.52261 | 2024-10-13 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d76ae0e-f9df-3b99-844b-01a5eaaee40a | -2.72122 | -49.65888 | 2024-10-13 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1d4b1e7-2f55-3ff8-8913-53d598b5ac71 | -2.62118 | -49.51736 | 2024-10-13 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c94f3330-cc87-351a-bbf0-0afd2dd68eac | -2.52146 | -49.67402 | 2024-10-13 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2062e2d6-6767-3b6e-b25a-624d1e06c14b | -2.52091 | -49.67753 | 2024-10-13 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4284c1a9-448f-3666-a084-05ff59cfd977 | -2.50144 | -49.69252 | 2024-10-13 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2613eff-aaf6-3688-bca1-7fd34a145b57 | -2.4612 | -49.64676 | 2024-10-13 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be46315b-d31a-335c-9ea6-1432e184af3f | -2.42674 | -49.62703 | 2024-10-13 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cc96602-a9f1-36c7-837b-23f25bedc70f | -2.42618 | -49.63054 | 2024-10-13 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c9c3dd6-8805-324d-b06e-494ccc58c50a | -2.39851 | -50.4045 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b77dc530-f1af-300c-baa6-93d458463863 | -2.3951 | -50.40396 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94d39ed1-2389-31cd-9bf4-140721458460 | -3.33818 | -49.15895 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8364a977-dda7-344b-8f2e-0f3f3435f47f | -3.33542 | -49.15499 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a707ad70-857d-3ab0-975e-3a0eb46ee9ec | -3.33487 | -49.15844 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a938a828-25cd-31bb-bd29-d026f763b447 | -3.33433 | -49.16188 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6680eb53-9b5d-376b-bf66-74df80fa5985 | -3.33202 | -49.12959 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e048996-7db2-38de-b626-05648f1d0112 | -3.32483 | -49.93037 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed65666-f99d-3771-b3bb-d25280060868 | -3.32427 | -49.9339 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97cd754e-b03a-33f0-a295-4b897d431e16 | -3.32093 | -49.93337 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4b7dd8f-826d-3716-8a5c-100c8ebd4cbc | -3.30063 | -49.11414 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72d4e8bc-094b-37e4-a9f9-8da52ff0901c | -3.29787 | -49.1102 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe684363-a262-3b0c-ab58-2fba25b55a64 | -3.29733 | -49.11363 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e77bc80-18a3-3e0a-962c-24eeeaeac378 | -3.29511 | -49.10625 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4502095d-4b80-37fe-a80c-24417bd86d75 | -3.29289 | -49.09886 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06cd7e44-a6ea-3f3c-a6c9-b635fd924951 | -3.29013 | -49.09491 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fccf0e6c-68cd-33d0-912b-f64f828526f6 | -3.28959 | -49.09835 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3fe0f6-e8c0-3bb6-b901-176e1493e76f | -3.28905 | -49.10179 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a94c317-34e7-371b-be64-13a31b6af343 | -3.28737 | -49.09096 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4da5f59b-3e50-371e-8f04-e6ab9a96a6d6 | -3.28629 | -49.09784 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a7a926-fb85-3007-996e-6d189f027f7e | -3.28353 | -49.09389 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 079cdf2e-72d1-309a-b453-079b59a671f1 | -2.79566 | -49.29615 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 372c5e0c-80cc-351e-8503-44f92e8f41e2 | -2.79344 | -49.28872 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e6a7a32-6101-389a-b51c-3f5058846493 | -2.79289 | -49.29218 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27398b81-aff7-3793-9cdc-13451eabd387 | -2.79234 | -49.29564 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 24e0335c-bad4-3fc9-bdef-8c3b55f5f989 | -2.78958 | -49.29166 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a0c493f-648b-32ce-83cd-0831a3d569e8 | -2.61805 | -49.08404 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b05f3c48-c7b1-3dbb-8e04-746301d0f027 | -2.60764 | -49.10712 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911e2b8a-add2-349a-af11-0ac9e847441b | -2.58863 | -49.24911 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 998c42ed-dde4-358e-9f42-1235d3123bbc | -2.58067 | -48.9514 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa3e4d70-01ca-38c3-8ad9-9410cca1ab45 | -2.57737 | -48.9509 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 394cdb00-783e-336c-a6dd-fd3efc3f32f6 | -2.56964 | -49.12946 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README55.md)
