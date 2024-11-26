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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d83fea0-fa92-37db-8425-933125737205 | -3.07791 | -49.20021 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ba4bbba-5646-3083-a446-1c0c894f8b9c | -4.31978 | -47.521 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b800aa84-bbe9-3baf-8874-b6915be2c1fd | -3.3883 | -44.17492 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a272097-2414-3fcc-91f4-e63107ffa596 | -3.98764 | -49.96805 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b744873-0d2b-3e4a-b8a6-b6b20033af75 | -1.35127 | -54.63317 | 2024-11-26 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af79f3dd-613c-372c-ad57-61d2a7e302e0 | -2.71794 | -46.28129 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0557e02a-abdf-357d-84e5-54152116416e | -2.54595 | -46.40726 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4afa6d6e-17f6-3612-98be-197a86bed253 | -5.1268 | -47.74263 | 2024-11-26 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b14b2296-670e-3a46-b42d-03e74ba560b0 | -6.18306 | -43.41389 | 2024-11-26 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93d2edd2-1a3b-39d7-816c-988ddc94e72b | -4.54496 | -43.29634 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 110ec1d0-8caf-3927-88c0-b837caceedf1 | -3.34106 | -45.85694 | 2024-11-26 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1382398-9730-369a-b8a7-c57e47038b4e | -3.51412 | -53.81827 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f77f16a-ffb8-395a-9852-082975e4fa34 | -3.26234 | -46.43948 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8f4ce2-e3fe-35be-9e5e-e60696d5803f | -3.48203 | -48.22598 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17e72eb6-18ec-3a15-bd4c-af49c2486a36 | -3.28403 | -48.75409 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d322137-733f-3a16-89c5-b462a77b7cc5 | -5.76544 | -47.81085 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b1e05e4-b6a0-379f-bfcf-c32c490919cf | -3.28071 | -48.75357 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be107d96-261a-35f1-b2b0-b41692a36507 | -2.45339 | -53.70153 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e30f666-0433-3bb8-8e96-4cd50aae5230 | -1.98757 | -53.29138 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4774a2fe-5a68-329d-8a42-c2033c93597c | -2.63234 | -51.7738 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43dbf684-8d99-3e18-87e9-91e5b379e8b4 | -3.96836 | -46.72601 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4f82c8-cefd-3bfb-87d1-7ec5822a78ef | -9.86269 | -44.11633 | 2024-11-26 04:38:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8873b679-b338-3afb-b09f-b739f09b1e7d | -1.99104 | -53.29552 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da969bac-0dab-3b1b-a920-72a524f231ce | -3.79602 | -49.94138 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f921c7-e883-397e-9d3e-e022ccb510c2 | -2.79491 | -53.0228 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16017747-1806-37b6-9cbe-d49ed19de890 | -2.38413 | -48.51404 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4eb54aa1-f0b8-3a0c-abaa-820f19233eb8 | -3.94995 | -46.91394 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22844e5d-3e40-3600-a548-a73bb319f2fa | -2.4734 | -49.10865 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af74b4a7-750e-3ba9-aff0-761450d91aad | -3.18936 | -48.42836 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b64b8b6-3e99-3983-bbd5-dc194f1f9a25 | -3.98725 | -48.06606 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 97e3eca0-fb65-3554-8e24-17c23675dfef | -5.23727 | -48.05821 | 2024-11-26 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| faae80e5-f229-3a0f-b4ef-b63dc2178720 | -5.76206 | -47.81032 | 2024-11-26 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1341fba2-6663-304d-97d5-4b91ec2fa612 | -5.67156 | -46.49615 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e42cf3f5-b4be-3f42-aa54-bd32208d69f5 | -3.6866 | -50.23281 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9229afba-021d-3493-a19b-c0dc52d773c4 | -6.12614 | -46.91742 | 2024-11-26 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54bef437-c02b-3ac3-b705-63c79cf9fa2d | -3.72566 | -50.18681 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5678bdf1-4b2b-3dd2-938b-de3991dbd794 | -4.11388 | -48.4881 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6bed1c-6bf9-3fff-9007-0057ed84a24c | -3.03832 | -48.50685 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba5cbf00-a22e-3fdc-95a7-5e81d50a0ff1 | -6.79741 | -48.89287 | 2024-11-26 04:38:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb152ffe-f97e-3b3f-a244-e100c9a1f069 | -3.37971 | -50.09681 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 187a1b08-c557-39ae-8964-8080c36f06dc | -4.36629 | -48.56267 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d503017d-0d26-3304-a569-5d68e30acd74 | -1.63094 | -52.76901 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 732b31f3-f129-3605-b36b-bb7972f26109 | -3.07146 | -50.95357 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3bcf02d-8e8d-331a-ace8-9e60b6ca1cc0 | -1.78454 | -52.7352 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf089a5e-940e-32d9-a444-d399d254becb | -3.34389 | -46.61343 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f87060d-fa87-397c-8078-7f66e8de7eb8 | -6.37569 | -47.35815 | 2024-11-26 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89918eb6-181e-3955-840f-2858df045bfa | -4.37831 | -48.50784 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6170f843-5363-34bf-865d-60820f078c07 | -2.50125 | -48.34863 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d207a29a-8374-372a-a44f-2c78ec8aac3d | -5.76488 | -47.81445 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eecc3d9d-4528-3dea-8a78-ef6df1c4a769 | -1.51759 | -52.62895 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac5a5df2-6143-35b1-9662-e9ef661939cc | -4.05082 | -48.32872 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60bcf2f4-2a55-32ec-9d18-ed482952806e | -4.35301 | -48.56061 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9da61b8e-9840-3126-ad16-0526108c2d26 | -3.59658 | -50.38231 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 712c914b-f5b4-3f00-b837-bcb738348fd6 | -2.80353 | -53.01911 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efb5c657-e7f2-3d35-92ee-d984fd3a445b | -3.98676 | -48.09106 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d564e0f-2638-30f9-a1d8-6e145e09eb82 | -3.28867 | -50.76105 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69b11a9c-7652-35b9-a115-4ebf037e48ab | -2.54654 | -46.40348 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6be4a5e-023e-3ac2-a3e8-9bc6a06ef26e | -2.93444 | -48.82269 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62069468-d1ef-3a56-b89a-ff2cea87f56d | -5.94816 | -39.66413 | 2024-11-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a8682804-1678-348f-8460-40849564f311 | -2.9664 | -49.20018 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8a7fb9d-2fb6-3909-a523-00b7ee8d8bb9 | -3.96669 | -48.06647 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| fc31bc97-d954-3a72-9409-7d10a5d5d98a | -3.80791 | -46.594 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebf97352-b76c-381a-b831-961383bee827 | -3.41392 | -50.10558 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b1b7a74-570a-39f4-9427-41707a4b34cb | -3.42625 | -49.22612 | 2024-11-26 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83d9dab2-7099-3c54-a3ba-75d320cce9cc | -3.96778 | -48.05951 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 29e811a7-a998-3eb3-88d0-ea051ddaae45 | -3.03554 | -48.50289 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c60f0293-e720-3c11-a677-7af646848348 | -3.28926 | -50.27168 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad079b2c-58f2-315e-b48a-88b2f07b3910 | -5.65206 | -46.64645 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b3a600f-f12b-3c87-884b-090789dfb259 | -1.78767 | -52.7407 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33aa5c92-aceb-38fc-b603-bbcf118a6d17 | -3.97009 | -48.08845 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3676f296-8b6a-330d-8c7a-a707289cd8dd | -3.39043 | -50.09481 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b365650e-cfb8-31e8-b698-bb9c81d61b8b | -3.98895 | -48.07706 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a55e589f-62fa-33dc-8ec5-6994217e2dfe | -6.19664 | -44.43017 | 2024-11-26 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3e3a42f-ab3c-338c-89ef-082b2e2c7f76 | -4.32541 | -48.58467 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8910d63-19b2-33da-8976-cd499778959c | -3.43956 | -50.01034 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b85efd9e-5c49-329f-9ed4-3b40cb5301dd | -2.07106 | -52.28685 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d081065-ed5f-36cb-92f2-01cce317855a | -3.22959 | -50.31818 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcd7147b-a2ad-30c1-9704-6042994ece77 | -3.9739 | -48.06404 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f09e1fa4-2c9f-34c4-831f-01a792417e83 | -2.70151 | -51.99384 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84021093-b48f-3b41-b2ac-b5b450210900 | -3.89095 | -50.06992 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77faddfe-dffe-3bca-a441-700d38112b47 | -3.28394 | -50.01892 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a830ef6d-7e56-395d-b4e3-309bd27e0851 | -3.96839 | -48.07748 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a890ee91-9dc5-3303-bee7-0d3126132927 | -3.18441 | -48.4382 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b527458c-0293-360e-8e65-8569ca909e71 | -6.00622 | -46.54852 | 2024-11-26 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86bc3f91-c3d5-3fe3-9c06-01086416ddb8 | -3.25139 | -53.29008 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4537acf3-df2a-378e-acbd-98be941870c8 | -3.27739 | -48.75305 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3519424a-fcd0-3198-a888-83ddd7c3ea69 | -3.83062 | -46.53932 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 372f0ea7-bd82-3209-8652-2a21d1ab28a9 | -2.16027 | -53.77331 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae781935-ea30-37c3-8a6e-17d9cf6e7c58 | -1.71904 | -52.71975 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8ff3deb-ec28-38e6-9716-bccb2f972ac4 | -2.70221 | -51.98951 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9e83865b-8631-32cb-b72c-a12ebd082700 | -2.71504 | -48.6684 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffacdbef-1bd2-3376-b0c6-1e96ac932868 | -2.96695 | -49.19671 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce831cc7-f422-38d3-bbde-3b31b6605582 | -3.73364 | -49.95738 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54dea968-057d-322b-808a-5e8a391813fc | -4.35633 | -48.56113 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 479b1064-8a21-3ba3-8938-49308e2432bc | -1.78377 | -52.74008 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9b51c45-6ca1-316e-8097-3e55ec322a61 | -4.27443 | -48.60855 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 249b1557-187a-3b0c-8a31-100c4709e04d | -4.24562 | -48.59698 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21e490ca-1866-3b7d-a191-92337cd45073 | -3.15934 | -50.58317 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f39b846c-c49d-3c63-9494-9b06f7d6910f | -3.29807 | -47.02169 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bba49e80-16e2-3840-95ba-326dc06a0e52 | -2.99349 | -51.45837 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
