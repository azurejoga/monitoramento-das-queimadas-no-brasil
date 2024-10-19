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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 135ab255-e04f-30cc-823a-93ca51a4ca4e | -2.51563 | -51.81762 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df31ecbb-4e0d-3c8f-9dd9-487a3d9d8b77 | -2.51498 | -51.82188 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c688b4ec-54f4-36d1-a29c-da8ff4f49377 | -2.5106 | -51.82123 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8276aff1-fbd6-38f3-b829-53cbed2f83a9 | -3.50068 | -51.10952 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 642bdc41-ce76-386f-8016-25599f6e4169 | -3.43537 | -50.79592 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aae04028-e3f9-35d6-86cb-9a1ff64f4735 | -3.32069 | -51.06382 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70cade26-929c-3555-92c6-abdfa6810386 | -3.2856 | -50.9474 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baa462f4-fedd-3bb8-8b69-ba5f1226ab8b | -3.28164 | -50.94165 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeb91e80-a327-3973-bea3-dedfdd312d0f | -3.2407 | -50.85066 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96aaad84-f42b-34aa-9f2d-2eb15adbde2d | -3.23754 | -50.84762 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cdd671b-d23a-38a4-b196-73c8a391911b | -3.2368 | -50.85268 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 354e94b6-7a2a-303e-8020-c8b21f11b701 | -3.23596 | -50.84999 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a15ebd3c-b2a0-3b66-b4f7-7ca4a3adae92 | -3.20924 | -51.04202 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99d77f74-4474-34ff-bd09-bfb935a6c94d | -3.2074 | -51.02184 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d80796aa-ca90-31a0-b139-9186b1593738 | -3.20697 | -51.03899 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b3ae4c7-7ce5-383d-bb73-08250b2aef43 | -3.20622 | -51.04388 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd1eca1f-1117-3107-9da2-7165e37be550 | -3.20456 | -51.04136 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3482897e-4baf-318e-b0d4-0dd3ee951129 | -3.20452 | -51.02377 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdc31ded-1805-37ba-926a-110e8ec22c8d | -3.14803 | -51.14481 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6612e27-79e2-36ef-8342-c42f3b96f8fa | -3.09066 | -51.21738 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f0444c8-c8fa-356a-9e57-cf34f1aaf65f | -3.08992 | -51.22215 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 659f6ae2-af14-3020-bb6a-c523a3a0aa61 | -3.08966 | -51.21949 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6633728a-94f2-3905-9461-688681ceaf76 | -3.08921 | -51.22675 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a34396fd-8da6-3834-9a5f-7671fbfd166c | -3.08897 | -51.22417 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3201bcc7-afb1-34b4-8c3f-41d76cda1212 | -3.08681 | -51.21181 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 552d6155-8a9c-3f9a-bc58-63eafe3d9243 | -3.08606 | -51.21666 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85b0e636-46bd-34f1-a049-1b0f26c90d21 | -3.08577 | -51.21391 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b904694-dc75-3f48-a852-e73162ce93e7 | -3.08532 | -51.22146 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 722d818a-3768-33b1-844b-d82823faaf1f | -3.08505 | -51.21878 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1f81c497-8c2f-3c57-a394-c6d351240c7c | -3.08145 | -51.21599 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bca93ebb-0b9f-3e98-9879-c417637da5db | -3.08115 | -51.21328 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdff5161-1766-35cd-8098-d0a8cfebd3f7 | -3.08071 | -51.22079 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 345a43ca-b943-3947-a5c4-16941f8b258a | -3.08044 | -51.21809 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 06ba96d1-1dab-3df9-94fe-605bb5e1f628 | -3.07684 | -51.21532 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33c2cff2-cb03-32f1-9b86-8c4008bfdb92 | -3.07635 | -51.24896 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51c33158-64d1-39cd-b586-9e3b3500daac | -3.0763 | -51.24634 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d53dce3e-967a-3715-9ce0-5583cf635cf4 | -3.07584 | -51.21736 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db68fe2-2f49-32d4-b734-1a0c96f483ba | -3.07562 | -51.25368 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b532fd40-9156-33b0-a9a2-6acbd34e39cc | -3.07561 | -51.25108 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e6bee8e-ed52-38cb-bf5b-77ff50a83c09 | -3.0547 | -51.04966 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a7712a5-00e2-358b-9021-da79fb95426b | -3.05027 | -50.98372 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d806cd96-7fc5-3cfc-8178-67a81f44468e | -3.05004 | -51.04897 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33b1d89b-bdf3-3957-8d86-2dde56d5e0f7 | -3.04953 | -50.98866 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 677d9d92-262a-3157-b827-81237dfc7b4f | -3.01064 | -50.99292 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76cd1e42-9e29-3cb3-ba2e-f6ab475f1e7e | -3.00838 | -50.98985 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d5770b1-038c-3991-8f5f-d75b53d9e959 | -3.00763 | -50.9947 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36868c1b-39aa-3ec2-8e0c-5fc7bda132dc | -3.00597 | -50.99218 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99624785-32f4-3017-8522-5f932993bbf7 | -2.98684 | -51.03668 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a38c20ef-23d1-3b49-b0cd-82440e418b9f | -2.98218 | -51.03598 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a88a587-f30c-3bd2-9320-b3f856c60b75 | -2.94811 | -51.04076 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f5016a3-6618-3c43-90a7-d93873c040f8 | -3.38539 | -50.67504 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 05ac84f5-c526-3c66-99ef-bb6526278833 | -3.38529 | -50.67142 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2032a67d-1bdb-3088-8e9c-0510c404d0c0 | -3.38452 | -50.67669 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca4aae52-bc45-30e9-bc86-e71bd61a502b | -3.27944 | -50.66237 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 097f99bd-1ae5-3a9b-b0c1-ad96cf1d9a70 | -3.27883 | -50.66477 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9336cd78-fbad-3de8-8f52-185d50d4d852 | -3.27865 | -50.66755 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af470ea8-cb98-36d4-9033-a79edbac654a | -3.27465 | -50.66159 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b06847f4-634f-3816-a1a4-221614239266 | -3.27404 | -50.66397 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e745ea9-6297-3468-a221-feedeb38a60b | -3.27386 | -50.66677 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f600af4c-cbd1-334c-9405-00491e3796c6 | -3.27328 | -50.66917 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3f07ac8-f23a-3457-8b88-6a37541e6cb0 | -3.26924 | -50.66321 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26e5dbdf-b5f5-38cc-a092-5be577647d9d | -3.26906 | -50.66602 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4387fe7f-2b0e-3613-9b80-6975f987a253 | -2.38202 | -50.47687 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a09cf6c-195f-39af-8448-a7e5e800bccf | -3.57334 | -51.46404 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcba0d1c-0f72-3aab-9404-1e0819e18317 | -3.56312 | -51.63395 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9262f2a4-62ff-3d03-a584-10dbc15dda16 | -3.56097 | -51.63536 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eed12a08-dc7f-3ba0-ab6f-764c6f63a857 | -3.55861 | -51.63328 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 603e74a9-2a96-3fe9-a6a3-a78a2c4a24ce | -3.55645 | -51.63471 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d73cc0d3-46a4-3012-a6d9-799486161457 | -3.37354 | -52.17888 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0cd710d-00fb-32d1-8fca-acbabdba2020 | -3.37099 | -52.17707 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91f16101-1471-3576-ba77-2dda211951b9 | -3.36841 | -51.51385 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ac8c26c-4722-38ca-9542-ff60f57439b8 | -3.18649 | -51.29451 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 428f2dfe-203f-3ab3-ba52-9d70bc8332b0 | -3.18622 | -51.29635 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64adb6d0-e44c-3e07-bf78-c37f6104f6d5 | -3.18579 | -51.29924 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58cb89b7-7c20-317b-92bb-e6bc42dd09d6 | -3.18189 | -51.29385 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ca70e1-5a0d-3063-8900-41b879f492ec | -3.18162 | -51.29569 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b886ff60-d480-39b1-9690-e42a9e460cdc | -3.1812 | -51.29858 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25e5fda7-6fc7-3eb2-bd83-02630e74502b | -3.15649 | -51.30651 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc245287-d380-3484-8b9e-aaa45fc37fc7 | -3.15577 | -51.31125 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e92ede3d-073b-321b-9b39-0fcb63a38b0b | -3.15118 | -51.31062 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5469c05a-6772-3c6d-a874-85fdd41573d0 | -3.15046 | -51.31532 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57212de1-1144-3f6f-a25c-ada89409bf36 | -3.14345 | -51.49255 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54103230-f8d2-3a94-90b7-5c36ec6497fa | -3.14169 | -51.49382 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 945bc839-f508-3f45-a3e4-7063f5386ea9 | -3.10186 | -51.32713 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a913451-747d-306d-8f99-2f0a2f5dfb37 | -3.04433 | -51.33514 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57484fff-33ba-3f38-85fd-b7ac74e28385 | -2.97024 | -51.45601 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 058c6d1e-39b4-36fa-adc2-1dc8e8974dd5 | -2.96505 | -51.45976 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00611dcd-1a1e-3532-b1c1-1374817294fa | -4.63839 | -50.93486 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49eb00b9-5a75-3ff3-a89e-83f11ff3e11c | -4.63758 | -50.94021 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e019dd70-c2ec-36dd-95b4-498d7b2768fb | -4.63744 | -50.9363 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c4231f8-5efb-3de5-98cc-97e3722c276b | -4.63669 | -50.94161 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 702db535-d968-3f40-93ff-ab532cba8c9a | -4.636 | -50.95068 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84dd6044-d5a4-3373-8c15-beab86d3962e | -4.63519 | -50.9521 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 421f1d4a-d821-3a1d-9db0-fa7763628606 | -4.42979 | -50.92257 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80bd7322-437a-3e3b-aedf-aa97679600aa | -4.25407 | -50.98412 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51903a50-d161-3246-b99c-31e3eb5c46b9 | -4.25006 | -50.97828 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d549c0ca-47b4-3e5b-8c91-e80ec91096e9 | -4.24927 | -50.98361 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b44dbfe3-4d70-3aad-af5f-575662126af3 | -4.2485 | -50.98883 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2bd8eecb-2a23-3dbb-9ee2-5195fb8cf5f1 | -4.24776 | -50.99383 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 155cb0dd-daa7-3d8b-bab0-aac39422c475 | -4.24298 | -50.99324 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
