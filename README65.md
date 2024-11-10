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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 269268aa-bf51-30cb-815c-bce0e0e0621f | -1.55273 | -47.69925 | 2024-11-10 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e6a926f-5c66-31be-8c21-e15131c485fb | -2.5409 | -47.37986 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f64fcf8-9487-3a58-b8ce-75a3579e8aa2 | -2.40229 | -48.49265 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3275ecf3-7789-374c-af6e-7c6a22173025 | -1.11983 | -53.60142 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2f8b0c0-8704-3b1d-bab7-5bfdb1a68d29 | -2.26887 | -48.73984 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec2b59bd-f2a4-3db2-a5c8-c6ef8e8f357e | -2.37218 | -46.8571 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956b5954-d456-3e25-ba8a-ed76b46c45a6 | -1.2554 | -51.76831 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c8b7b2c-a264-3dc2-ae30-0059adc6f0f5 | -2.23008 | -48.3842 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bbc0c22-1742-398b-94a6-3a762070f2b8 | -3.52274 | -40.90718 | 2024-11-10 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04213908-8cf9-3a89-adec-b3f02589513f | -2.01403 | -48.07882 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a195c678-81db-3a26-959f-8a7fffd46e2f | -2.53028 | -47.38183 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e580767-4648-38e2-ac35-d9e5e082f2ca | -2.21287 | -47.7413 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 83ba4cee-ff1a-33b6-8296-ff8ddbc1997c | -1.6218 | -50.68491 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35324230-c613-37f7-a6a8-893b00a5e220 | -2.17306 | -48.319 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15682024-c35e-3123-ae56-7675e1848ffc | -2.48864 | -47.23042 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c84a624a-d1cc-3095-ac80-92ae86dde8c8 | -2.6436 | -46.79387 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4688ea-2f0a-3d11-bf9f-cd5a0c485ff7 | -2.40796 | -46.7845 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 948b0055-5d12-3c28-80ae-392bcdf8b041 | -2.20903 | -48.36681 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 191b46db-4b07-3d31-9b9d-19835389893c | -2.323 | -48.52573 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b8f3fa-3364-3087-ad88-f9145712c87f | -1.5993 | -52.75245 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f975089b-a7ae-3f5a-a85f-bb27c5d94f45 | -2.37225 | -46.72307 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba38ce1-42b7-3b6d-9d21-26e7fb7748d7 | 3.36571 | -51.27039 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a30697df-af43-379c-a2e8-f93e0991481d | -2.22623 | -48.38713 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3851d30c-9124-3882-a268-e6bcc939e578 | -2.38954 | -46.47673 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be8980a1-33eb-3b54-80ca-1d841cf78cd7 | -1.3204 | -52.23829 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26562a65-2871-31ea-a201-ef2c55b68b1c | -2.23373 | -48.4906 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29fe14dc-ab03-37ca-8bfd-99157d0f837b | -2.17007 | -46.69942 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55ee6665-af8f-37ac-8ed3-c792d60b3507 | -2.63622 | -46.79648 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6fc8f8-9faf-3e86-8fc0-69f036e95f04 | 1.62693 | -56.04885 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0837751-b8b1-35d6-b147-464e5aa853f8 | -2.06247 | -48.89197 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 717af265-406f-3df5-aaea-3807ee1b2e95 | -2.56485 | -46.5411 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a62377f-7bb4-3f40-9938-2401afe3a71e | -2.1506 | -48.82399 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf840c68-1a58-366f-8e9f-62f238926a11 | -2.06913 | -48.89301 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78ee14d-8296-3b33-bda9-f5b5f7cf2c44 | -2.64019 | -46.79335 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c5931b8-52d6-380a-93c3-72145afc7110 | -2.24069 | -49.86515 | 2024-11-10 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5fc96ad-6a30-3f3b-8928-9e30bcf38bb7 | -2.16657 | -46.83274 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e17113-d8fa-3d46-8832-fed636604735 | -1.45736 | -52.34193 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7af4d913-1500-3b9f-91ff-9c7fe2cd7f8b | 1.72714 | -51.06496 | 2024-11-10 04:36:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d6f5c49-0e89-3d8e-bc3e-4e102c6afa08 | -2.32523 | -48.53315 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caf862f5-5700-3ef7-9a6b-a4b8dfb61e6c | -2.08667 | -48.82481 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0ccd0159-5afc-3bec-8f0e-73a39b5a752c | -2.14837 | -48.81656 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2b9b87e-2a52-3c7b-b730-7e12170f82bb | -1.41609 | -54.76857 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02f13f7e-1365-38f5-acf2-6efdc9080c05 | -2.22744 | -48.42259 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2afff969-803f-338c-b7fd-6d4ba5ab9f83 | -2.16253 | -48.72674 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a67e07-a02d-33f8-9190-154fbfa0f1cf | -1.03733 | -47.7919 | 2024-11-10 04:36:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2293f406-f691-380d-bb8b-aa34db5eb026 | -2.23041 | -48.49008 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58294195-e836-35e9-b461-ad479b801603 | -2.33203 | -48.91655 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9897b986-4e41-3972-ae1e-9b5c69316bee | -2.52107 | -46.37002 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feb6069a-74b0-3907-850e-feab0cd11de5 | -2.2179 | -48.74245 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963502ae-539f-326f-a542-2b1e6dc48917 | -2.08895 | -46.45799 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94d6f23d-31c6-3b01-81ba-68665cf4c9de | -2.62015 | -46.16801 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90707a77-0e87-3ca4-a35b-566403e178f8 | -2.29453 | -46.48154 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b39fffce-2bf8-376e-8fe5-26ebfda6eeb2 | -2.32743 | -49.11851 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0067eda8-0c71-3421-be09-6fada41cf9ca | 1.72344 | -51.06554 | 2024-11-10 04:36:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f43f9083-2073-30a9-9be9-a3b047c863fd | -2.10161 | -50.74971 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d5654d5-dfbe-3573-8319-41e055ff96b8 | -2.09681 | -46.5423 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c247454-cbd3-3284-8d06-55c31714a873 | -2.14736 | -46.6885 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca520d9-c00a-340a-bdf2-14f7759b7718 | -2.20186 | -48.36922 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9f86206-7eba-323d-ac41-c97302d54d0b | -0.04206 | -50.77934 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fe4c666-4b5d-372d-b08e-7f1ab1788c47 | -0.40968 | -51.9924 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39a21656-fc4a-3dd5-9c06-8a9af32acb7c | -2.15872 | -48.75091 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35fe6052-a02d-377e-9e8f-6f98f393ea04 | -2.18613 | -46.57442 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 68da0b41-faf0-3611-8223-78cbfe1bd1d7 | -0.61492 | -49.52557 | 2024-11-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8ec58ca-decd-3270-978e-6eeee1cc502e | -2.20567 | -47.74374 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cb142af-f693-35e7-8984-6393778feceb | -1.42062 | -54.76908 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb931ca7-dda0-3dd3-ab61-09a079a044a2 | 1.57023 | -56.03151 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e4ec843-4bf9-3397-89d1-39caa310b6d8 | -2.23396 | -46.62335 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54eded19-bf07-3bfb-86f4-0fc5d7162a88 | -0.64459 | -52.3644 | 2024-11-10 04:36:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84880bf9-d59c-37ec-be36-018a9cd5403f | -2.46229 | -46.32714 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e159915-3b0f-3b9d-8e76-ff60d1831a5b | -2.40615 | -48.48972 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 651b21a7-77ca-3761-be9d-68c08309437e | -1.1289 | -54.21245 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8294b5f-fc6c-335a-a64f-43b651487903 | -2.2269 | -48.42603 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 525c7fe9-1b39-331d-89d0-8f4d78cfb9cb | -2.51942 | -47.18785 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b374a7a4-ed24-3d9d-bf44-1c39bd8b8e86 | -0.02463 | -51.32051 | 2024-11-10 04:36:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88a2f808-d091-32bf-96cb-144a30ae73b3 | -2.5009 | -46.38614 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d79c360-f8b4-3429-beff-6f48a0f111cc | -2.24261 | -47.97994 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3616c5e4-ed8a-37f2-8f3a-3cd37451f641 | -2.08999 | -48.82533 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 29ca4fa7-0b60-3b4d-bfcc-516ab13c77b0 | -2.14882 | -48.34345 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecf522df-465f-3cd4-9fdf-a440612e8b43 | 2.8546 | -60.08347 | 2024-11-10 04:36:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c554d4c4-8bcc-3d06-9c90-67da7e0e5665 | -1.2199 | -51.7762 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afe42d9e-d61f-382e-94ea-d9285afd97a6 | -2.42659 | -46.30626 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 16b9d395-dfe5-3cec-bab7-249684388c31 | -0.64385 | -52.36917 | 2024-11-10 04:36:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a18d13e7-4754-34dd-8514-52c9d4d76eda | -0.30479 | -51.7 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca8ad492-fee5-36cb-a3ec-73efdf373ce5 | -1.84713 | -46.28939 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3c0d70c-d376-3af7-b092-a557392c3519 | -2.54138 | -46.30766 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d62082e-732a-3874-b837-efd916cb286e | -1.46566 | -51.47848 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6427f138-f361-3a2f-b700-6246fb481fcf | -2.09603 | -46.34476 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345d3119-c244-39b4-95ba-cd4ad2752892 | -2.08942 | -46.52233 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 900bee87-8110-3878-ae32-a9bbd2f6d28c | -1.11992 | -48.36249 | 2024-11-10 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf3c9dd-476e-3f22-8e18-aa0b7ccc01e5 | -1.23561 | -54.15601 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4761772f-b36e-326b-b21f-6e468bb38ba1 | -2.17966 | -48.33755 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c3ec3b-27d3-3d44-b95a-b6f1bcc1e7bb | -2.3183 | -46.73342 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84e9b01c-b670-369c-9d56-6aacec2f8dcf | -1.88661 | -47.96661 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd8810a5-b9e2-32ad-89f1-365d3249bdb0 | -2.67029 | -46.71173 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b824c00-c9e7-314c-9130-c1a355f7207f | -2.20517 | -48.36974 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5eaa78d8-502f-327b-ae78-744fc5f853f4 | -2.07016 | -50.90395 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c65b669b-75cc-3610-bdb7-37b3063ae9b9 | -2.08096 | -50.34269 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84b623c8-a22d-3b5a-897b-4b55943a6445 | -2.31857 | -46.48527 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 665d43fd-32d4-3b3c-95bc-8730cd01dc5b | -2.31069 | -48.47441 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b29cf101-00d0-3580-86cd-d84160b748ad | -1.49173 | -52.03238 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README66.md)
