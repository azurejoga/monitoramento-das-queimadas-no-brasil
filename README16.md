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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27470d31-43c3-31e0-8fb0-499619707ed9 | -3.7703 | -43.5323 | 2024-11-02 01:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 323072e4-ce0a-37b9-96c9-e4cee925fea4 | -3.7888 | -43.5545 | 2024-11-02 01:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 4db29b9b-7c76-3c9f-b76b-4d65a3acb531 | -3.7372 | -46.0545 | 2024-11-02 01:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 16255ebc-39df-32dd-b0fa-7e82a22784f5 | -3.9473 | -48.3666 | 2024-11-02 01:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 56dbcf1a-7252-312b-a473-0bf008db1748 | -3.9474 | -48.3451 | 2024-11-02 01:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 78ae10b6-cdf6-3b3e-baec-f6987b6d5f67 | -4.3164 | -48.6515 | 2024-11-02 01:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 245b72e6-547f-3872-b3f1-deb682c17afd | -4.3867 | -43.4757 | 2024-11-02 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 94e9542e-a535-3a62-9243-347413d7b993 | -4.4054 | -43.4746 | 2024-11-02 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 615e103d-ad3d-30f0-9e8f-7f6a6cf0aa1c | -4.3537 | -48.6068 | 2024-11-02 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3942d089-455f-395f-9f8e-9a0a6ea8aaa3 | -4.5575 | -43.1162 | 2024-11-02 01:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c3ea10ef-b786-3195-a0a2-c9f14cbecc73 | -4.5577 | -43.0928 | 2024-11-02 01:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| f47c7cab-cae1-3546-9e66-38c6b44bf75c | -4.665 | -46.3862 | 2024-11-02 01:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9b21dcc9-ed44-3d6b-aee4-9cd8fcf7a71f | -4.6837 | -46.3852 | 2024-11-02 01:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ef458e23-ecf6-33dc-a3b3-8298a3578050 | -4.8068 | -44.7834 | 2024-11-02 01:05:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 71e45edd-2e93-349f-8b39-b301af3c56b9 | -4.8255 | -44.7822 | 2024-11-02 01:05:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b2ad5a1c-e9ff-3fbc-8871-2673a9108e22 | -5.1146 | -46.0264 | 2024-11-02 01:05:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 83d5269f-134c-3d86-b82e-d7c98c71d56d | -5.3063 | -43.0897 | 2024-11-02 01:05:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e756f697-0a38-36e3-a0aa-1f0bd4e06cad | -5.3065 | -43.0663 | 2024-11-02 01:05:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 4355877a-3e83-32aa-8b54-3128e7a3bc5d | -5.3252 | -43.065 | 2024-11-02 01:05:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 3b0adb3b-008b-3ed0-982b-3adea6c3bf6c | -1.5899 | -52.1481 | 2024-11-02 01:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9fb85fa5-9cdc-3cd8-a845-03eaf9ab5840 | -2.1949 | -46.4855 | 2024-11-02 01:15:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6f345a0d-5f5f-33f5-9bda-6ae5e0c4d660 | -2.195 | -46.4634 | 2024-11-02 01:15:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| bff55b0b-9995-3468-b040-f6bf7d9ac252 | -2.2135 | -46.4629 | 2024-11-02 01:15:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0df6a91a-813f-3aa0-8632-70172902430b | -2.2568 | -50.4376 | 2024-11-02 01:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 59a40d69-34ad-37b4-b563-f429eb4ebbd8 | -2.2663 | -53.7422 | 2024-11-02 01:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 1ca3b448-4232-31f3-9655-cb33fccccdbe | -2.2847 | -53.7419 | 2024-11-02 01:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 397855a0-76b7-36b4-9515-7cc1ad0a7f64 | -2.8056 | -51.7539 | 2024-11-02 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9601565d-7ff8-36ca-8fae-a77b716b0b19 | -2.78 | -48.5806 | 2024-11-02 01:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8ac678ad-9031-3b50-ad18-244ba002a1b4 | -2.8386 | -52.8794 | 2024-11-02 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a22a48de-5a86-3ae5-923b-b099aed9da1c | -2.8509 | -49.3895 | 2024-11-02 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f5bfc88e-6601-379f-ab49-fbba6d7a9e6a | -2.8808 | -51.3179 | 2024-11-02 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 05fef1ec-9e60-324e-9952-16f650de0081 | -3.0088 | -51.5834 | 2024-11-02 01:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 66cc2bb9-f236-3a4c-9f71-3d29c38224c5 | -3.0734 | -54.167 | 2024-11-02 01:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 561ee5e0-d3b4-3635-bba2-5b8fb81b887b | -3.1097 | -54.2865 | 2024-11-02 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 2eb661d6-f1aa-32b6-b3c6-cb2665cd2cd1 | -3.1098 | -54.2665 | 2024-11-02 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2b9fc193-611a-38ad-ba09-9d15eeb1802a | -3.1281 | -54.266 | 2024-11-02 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| a30867de-1a17-33a1-8830-d44d4c75cd46 | -3.1282 | -54.2459 | 2024-11-02 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7b4dd454-992c-36a9-b87d-c1c9226f7754 | -3.2249 | -44.431 | 2024-11-02 01:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 118df307-8960-3846-ae78-922de3416cd5 | -3.225 | -44.4081 | 2024-11-02 01:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 107.7 |
| d72dddfd-375c-30fe-915e-94cfb8d1df39 | -3.2436 | -44.4073 | 2024-11-02 01:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 19418cf2-c892-36da-900b-635c2ef50b95 | -3.7701 | -43.5554 | 2024-11-02 01:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 7830e1fe-5902-37c0-8300-6fd795c469ea | -3.7703 | -43.5323 | 2024-11-02 01:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 593f0c6a-a709-30a2-95b0-d6b9a8f51c51 | -3.7888 | -43.5545 | 2024-11-02 01:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a7a0eb33-2850-3fb7-9c51-82823a5d28da | -3.7889 | -43.5313 | 2024-11-02 01:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4d1b7b8a-7fad-3587-acf3-9e8908b71078 | -3.833 | -48.9722 | 2024-11-02 01:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 028cee0e-7d2c-3e10-9c44-0ab42045ce90 | -3.9473 | -48.3666 | 2024-11-02 01:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| bc4a1cfb-464b-3565-a23b-bef8abfbc383 | -3.9474 | -48.3451 | 2024-11-02 01:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a9026dbb-216e-372e-9c5d-e3e5ffa1f638 | -4.3537 | -48.6068 | 2024-11-02 01:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1bf3369b-09bc-3409-b1d4-b5e10f1e5836 | -4.4054 | -43.4746 | 2024-11-02 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0f7b47d7-b53e-3a95-a2e1-277ec9fa856e | -4.6837 | -46.3852 | 2024-11-02 01:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 96f91465-f538-3191-84b7-ce9262e79b9e | -4.5575 | -43.1162 | 2024-11-02 01:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5161ce12-1355-369f-83af-f4a64d670c9f | -4.5577 | -43.0928 | 2024-11-02 01:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 82c094e9-8730-3448-98b9-d253c9b43186 | -4.8067 | -44.8061 | 2024-11-02 01:15:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2cecc17b-0693-350c-8139-55fe8da86dfc | -4.8068 | -44.7834 | 2024-11-02 01:15:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e6221466-328f-3ec6-9411-07ee828eddfa | -4.8253 | -44.805 | 2024-11-02 01:15:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b2e5f258-d59b-33bc-8ad0-939df237f796 | -4.8255 | -44.7822 | 2024-11-02 01:15:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4359f590-3f37-3942-94a3-7ac9ca24e6d3 | -5.1146 | -46.0264 | 2024-11-02 01:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 35dc077d-d965-3e33-9877-eba4895d1f72 | -5.3065 | -43.0663 | 2024-11-02 01:15:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0801580d-33f3-3835-b221-224ad8cc6ff6 | -5.3252 | -43.065 | 2024-11-02 01:15:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a4b3162a-1833-30df-96bd-e1cc6945eff6 | -1.5899 | -52.1481 | 2024-11-02 01:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 91dca501-bb9b-385d-8d6c-23c53fb97619 | -2.1949 | -46.4855 | 2024-11-02 01:25:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2e514d9a-47c9-3e8b-ab28-1eec57ae3e6e | -2.195 | -46.4634 | 2024-11-02 01:25:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| bb18d009-67c6-3598-8f95-ba55287ae28a | -2.2568 | -50.4376 | 2024-11-02 01:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c852f090-4a84-39ce-a2a0-7b727800e0e6 | -2.2663 | -53.7422 | 2024-11-02 01:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 93adac88-d489-3e40-86d2-d393a4caf7b3 | -2.8509 | -49.3895 | 2024-11-02 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ceb3d10b-38f2-357d-adfe-0ac2c2d97381 | -2.8056 | -51.7539 | 2024-11-02 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 29dbf023-4c0f-3ffc-b07a-ebfeb2047c2f | -2.8386 | -52.8794 | 2024-11-02 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| debd0a70-bf3b-3bf9-bcd0-959cb7e77d11 | -3.0734 | -54.167 | 2024-11-02 01:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 052d2ac7-1e68-3b5d-a129-edba596eebde | -3.1097 | -54.2865 | 2024-11-02 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| dcd21677-239a-3464-92dc-cde4d16f201d | -3.1098 | -54.2665 | 2024-11-02 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c04802f3-9edb-3921-be12-6212aafbe00e | -3.1281 | -54.266 | 2024-11-02 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ee02ed10-9566-317f-8135-b9738f245aba | -3.1282 | -54.2459 | 2024-11-02 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 416dc752-470d-3194-ac6b-a729992f12a9 | -3.2249 | -44.431 | 2024-11-02 01:25:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 08da77b4-950f-3922-8f1b-25e3b65ca7f2 | -3.225 | -44.4081 | 2024-11-02 01:25:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 716378c3-4c78-3fb8-a8d3-c1c34f89a15f | -3.7701 | -43.5554 | 2024-11-02 01:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| db033e8a-4ea5-34af-95aa-993e31fed29f | -3.7703 | -43.5323 | 2024-11-02 01:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 0e6446ab-5cfd-32ad-bd86-65f311c22f60 | -3.8144 | -48.9729 | 2024-11-02 01:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b45f18ac-0619-3e17-b1e9-219a2463ccb2 | -3.9473 | -48.3666 | 2024-11-02 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 375a0726-c962-35de-9811-1670089c4485 | -3.9474 | -48.3451 | 2024-11-02 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d1fae804-0367-3993-8219-dc322262e290 | -4.4054 | -43.4746 | 2024-11-02 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d3299fe8-00be-3083-92c4-4be29569c7d5 | -4.5575 | -43.1162 | 2024-11-02 01:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 77757ded-680d-3bf2-b45a-8c8d941a61c7 | -4.5577 | -43.0928 | 2024-11-02 01:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 62dddce2-0505-3e63-9c35-0d0f733fb3d2 | -4.8067 | -44.8061 | 2024-11-02 01:25:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 506cf9db-8619-3dee-a864-4521c64503f9 | -4.8068 | -44.7834 | 2024-11-02 01:25:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 943c10aa-3b75-34db-b162-01ac1d0ad571 | -5.1146 | -46.0264 | 2024-11-02 01:25:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 26188b7e-31ee-3429-9c3f-e37fc1e19485 | -5.3065 | -43.0663 | 2024-11-02 01:25:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e228635f-bde3-3b59-8f04-6d575cad0be5 | -5.3252 | -43.065 | 2024-11-02 01:25:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 83c044d8-78e1-3bb3-99ca-ee352c9a86cf | -7.1294 | -46.3711 | 2024-11-02 01:25:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 86bfbcb8-8c1a-3454-b128-736f0d8bef43 | -12.172 | -41.8497 | 2024-11-02 01:26:14 | GOES-16 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 3f30f53d-7c63-326f-9aa1-6a61dd654af9 | -20.3321 | -48.8231 | 2024-11-02 01:26:58 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a8b61d87-ea26-323f-ae28-2905fc75a543 | -1.5899 | -52.1481 | 2024-11-02 01:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| cc73070f-820e-320f-b1ae-64775ed32556 | -2.1746 | -53.6834 | 2024-11-02 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| bdf763cf-7638-346d-a977-a91dc9a6a0a7 | -2.195 | -46.4634 | 2024-11-02 01:35:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 21f47ee4-437b-3244-bcaf-32de38e19e20 | -2.2663 | -53.7422 | 2024-11-02 01:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| eaf1d413-faec-3051-bc11-8bfd5240d8b1 | -2.2568 | -50.4376 | 2024-11-02 01:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0adb2bc1-602b-3cc0-8383-28962bf2b712 | -2.8056 | -51.7539 | 2024-11-02 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0ca286e7-8407-373e-96f1-48905d8cff76 | -2.8386 | -52.8794 | 2024-11-02 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e3e35bd5-396a-3cfa-89dc-97449d7685a4 | -3.0734 | -54.167 | 2024-11-02 01:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 99e4f1dc-4abd-3d90-a6f0-e0f0a8c35f44 | -3.1097 | -54.2865 | 2024-11-02 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ffce04a7-904a-3824-af62-509cfea616d3 | -3.225 | -44.4081 | 2024-11-02 01:35:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |


[Clique aqui para ver as próximas entradas](README17.md)
