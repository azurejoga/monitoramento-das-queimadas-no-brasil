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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 728e0092-4c36-3c6f-bc84-9f1dae0f6b2b | -3.1932 | -50.437599 | 2024-09-29 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 985806b3-ce22-363f-b3d9-346561926d6d | -3.1948 | -50.444599 | 2024-09-29 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf7f4dc-afab-36ae-92e4-49a188ee6125 | -3.1435 | -50.264702 | 2024-09-29 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69b6cf4c-174b-37f4-8d59-ac7291e09703 | -3.1451 | -50.271702 | 2024-09-29 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c23b5e2-a361-38fa-ab8f-e0ec2f7e61eb | -2.6392 | -48.246799 | 2024-09-29 00:49:37 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff7cd0b-3815-3d7b-a825-cea159b0d7c9 | -2.6408 | -48.253799 | 2024-09-29 00:49:37 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d104d0e-397c-3a88-addf-0e00992efa6b | -3.1098 | -50.478298 | 2024-09-29 00:49:37 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7568e793-471e-3d33-80b8-4e03727207ff | -3.1 | -50.4804 | 2024-09-29 00:49:37 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4f53997-1b24-34d4-a59c-9a17b8b4a4fd | -3.087 | -50.468601 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c04000db-c6d7-3065-abc4-e12ac535fe10 | -3.0886 | -50.475601 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abbadfa4-b6f3-361e-b0bd-55f1883a3dc6 | -3.0902 | -50.482601 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce0c905-5299-339e-9c7c-588e182ecae0 | -3.0772 | -50.470798 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416c3c36-b2e8-3627-b77a-e30949f68e8a | -3.0788 | -50.477798 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e593398-f96e-3418-b333-3e65889db0ba | -3.0804 | -50.484798 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5962f32c-32cd-3238-84fa-7ca078a37237 | -2.4614 | -47.833698 | 2024-09-29 00:49:38 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42696f58-e665-3f61-b357-940f393de54c | -3.0673 | -50.473 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31fe2554-915b-3a57-952b-154f1575bf0e | -3.069 | -50.48 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ea2193-4e48-35b3-a888-d5dc7439b9ac | -3.0706 | -50.487 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd79947b-d068-39f3-8909-6cb07dddd7fa | -3.0592 | -50.482101 | 2024-09-29 00:49:38 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70f0b6f7-717f-3448-a03b-10f909298409 | -2.3638 | -47.59 | 2024-09-29 00:49:39 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0d93b2-204d-375a-a69e-414d905aa9df | -2.3655 | -47.597198 | 2024-09-29 00:49:39 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3f301a-a604-3592-aeb3-f4b255a9e700 | -2.3672 | -47.6045 | 2024-09-29 00:49:39 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdae71aa-7ee4-3cbf-a232-b177cc24b5a7 | -2.354 | -47.5923 | 2024-09-29 00:49:39 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd394c9a-90e2-374c-858c-0c8cb2e772e9 | -2.3557 | -47.599499 | 2024-09-29 00:49:39 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42003890-43a9-3b9a-96cd-575eb349ef8c | -2.3574 | -47.6068 | 2024-09-29 00:49:39 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc1b8bab-0ea3-343c-b974-9f3f75d11dd9 | -3.7256 | -53.789501 | 2024-09-29 00:49:39 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ae7c5f-6f63-36d0-bcc3-6d333ac5292b | -3.0131 | -51.048 | 2024-09-29 00:49:41 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae568141-ba47-3382-9260-fee49d68c402 | -2.4747 | -49.145302 | 2024-09-29 00:49:43 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1c9c12-6794-37a6-95df-2f484a774c92 | -2.4763 | -49.1521 | 2024-09-29 00:49:43 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7998280b-9edb-3c89-aed4-203d283f17df | -2.4778 | -49.158901 | 2024-09-29 00:49:43 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61551193-ab6f-3658-8995-7cefd74ca0c6 | -2.2569 | -48.2887 | 2024-09-29 00:49:43 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ec7f0a-7f9a-3c90-92ee-1162b92a6304 | -3.4578 | -53.785099 | 2024-09-29 00:49:44 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358619b8-84a0-33a1-a3e0-f4d0fb49a972 | -3.46 | -53.794998 | 2024-09-29 00:49:44 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d4f0b6-e77b-3801-b86f-a4b8162c7acd | -2.952 | -51.639702 | 2024-09-29 00:49:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 454c152c-848f-34ba-91a0-77c0da52c114 | -2.9537 | -51.647301 | 2024-09-29 00:49:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aef7958-0379-342a-8e29-7d3ed55b5555 | -2.0273 | -47.650501 | 2024-09-29 00:49:44 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7bb298f-b63e-3c51-a131-bd7d5496db0d | -2.0289 | -47.657799 | 2024-09-29 00:49:44 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b66342a-037b-3fc0-bba4-ae7908c51334 | -2.8823 | -51.3783 | 2024-09-29 00:49:44 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f8f443-fe3b-3f54-9ce5-96e2382ce2f2 | -3.4533 | -54.084499 | 2024-09-29 00:49:45 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17f19214-75bf-3be2-89e0-d2bad1c18b01 | -3.4556 | -54.094799 | 2024-09-29 00:49:45 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dfb151a-db8c-35b0-8e23-d19400d14588 | -3.4411 | -54.076199 | 2024-09-29 00:49:45 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9429ec2-3899-3ea9-a467-d1f5f6b7078b | -3.4435 | -54.086601 | 2024-09-29 00:49:45 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22d9e896-ac87-35cb-be73-f61f266b909e | -3.4458 | -54.096901 | 2024-09-29 00:49:45 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9144d37e-636d-3196-b872-4b74ff5843bc | -2.8736 | -51.657101 | 2024-09-29 00:49:45 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09272aad-9ab2-3647-aa14-23fe1f903717 | -2.8753 | -51.6647 | 2024-09-29 00:49:45 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58972d75-124e-317e-bab9-907fd952f7c2 | -2.8771 | -51.672298 | 2024-09-29 00:49:45 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba03ae5d-f87b-3eb6-ad70-779192014b2d | -2.8655 | -51.666801 | 2024-09-29 00:49:46 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3721e0f6-c726-39fa-ae5e-f0e56b9cdbf6 | -2.8673 | -51.6744 | 2024-09-29 00:49:46 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2de0dbd-8672-3856-9ebc-a0a11e8bef58 | -2.8121 | -51.929798 | 2024-09-29 00:49:47 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4e15b3e-d472-3aa1-99d7-202ccd91e7f0 | -2.756 | -52.090801 | 2024-09-29 00:49:49 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8c028f9-8507-376d-8e91-45dd86a9b632 | -3.1279 | -53.7332 | 2024-09-29 00:49:49 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f44cc8-62d3-3d23-9a54-0231c83462dd | -3.1301 | -53.742901 | 2024-09-29 00:49:49 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a1313b5-c56e-3061-8e4c-a65af1c003b5 | -3.1323 | -53.752701 | 2024-09-29 00:49:49 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf384eb-5c97-3123-9aff-87ab6b16b7ae | -3.1181 | -53.735298 | 2024-09-29 00:49:49 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d925e9e-f300-33f1-bf61-96c44b0ea936 | -3.1203 | -53.744999 | 2024-09-29 00:49:49 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5638f89-18eb-3035-a2b9-a0f3539a8b85 | -3.1225 | -53.754799 | 2024-09-29 00:49:49 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b862832a-68c2-3bda-9610-f4f104c41ff0 | -2.6767 | -52.421101 | 2024-09-29 00:49:51 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a509dd-18b1-393b-8aef-862532e222ba | -2.6786 | -52.429298 | 2024-09-29 00:49:51 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5e8555-9ca2-34a3-8c74-341cb09aa6cf | -2.6805 | -52.4375 | 2024-09-29 00:49:51 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a735cfc-2179-3d32-a422-23b7e7175614 | -2.7559 | -53.223801 | 2024-09-29 00:49:53 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11064544-c84d-3b7d-aee7-d6a74060c64c | -2.7579 | -53.2328 | 2024-09-29 00:49:53 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 688b1026-54c8-3eb6-a567-00cc5180127a | -1.1711 | -46.710899 | 2024-09-29 00:49:55 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a79c542b-fad8-3abd-be1c-ee218f003cf8 | -2.6294 | -54.253799 | 2024-09-29 00:49:59 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed8ffec-f4f3-3d65-9ef2-91825c73c7f3 | -2.6318 | -54.264198 | 2024-09-29 00:49:59 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3407d41-d9d7-38d7-a473-5f7b473aff96 | -1.3834 | -49.332001 | 2024-09-29 00:50:01 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0e78530-a4fe-3fc6-b455-c8e87b52c9a9 | -2.1451 | -53.6576 | 2024-09-29 00:50:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d10890-5f69-3d10-b89d-c12003010933 | -2.1473 | -53.667 | 2024-09-29 00:50:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7caa0344-d6e5-362d-b84c-08533ff9c5b2 | -2.1494 | -53.676399 | 2024-09-29 00:50:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e10ce0-2b56-3868-9162-8b716b350770 | -2.1353 | -53.659801 | 2024-09-29 00:50:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ff9bb8-a480-3dbc-a1cc-a0211675775f | -2.1375 | -53.669201 | 2024-09-29 00:50:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd9fd151-25d4-3436-a20a-fe3d402795dd | -26.28054 | -50.27765 | 2024-09-29 01:02:00 | TERRA_M-M | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 47c85ffb-91e3-33a7-b9de-8eaf4d26f33e | -23.37903 | -50.22587 | 2024-09-29 01:02:00 | TERRA_M-M | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| d0c17202-a305-3fed-82ee-7307c4197047 | -23.37879 | -50.23246 | 2024-09-29 01:02:00 | TERRA_M-M | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| c3b3bb3d-95f9-32ba-b386-7d556a1caebc | -23.37731 | -50.22042 | 2024-09-29 01:02:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| eeb9d672-dab4-36b6-ae3a-322007fe92fb | -22.78017 | -46.80359 | 2024-09-29 01:02:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 6148c08c-a9cc-3cb5-8b0d-f262e307afb4 | -22.38152 | -48.74577 | 2024-09-29 01:02:00 | TERRA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| eaff9e74-af46-3010-9a92-b4b3c5dcd729 | -22.29742 | -48.66206 | 2024-09-29 01:02:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 72ed66eb-c1c5-335c-8619-b5b43e01327f | -22.29611 | -48.65202 | 2024-09-29 01:02:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 18be2a6a-3977-31d1-9c55-0bf78991fc2d | -22.28963 | -48.67344 | 2024-09-29 01:02:00 | TERRA_M-M | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 7e2f09c6-69ad-3f17-be5a-db956d4c32ce | -22.28833 | -48.66343 | 2024-09-29 01:02:00 | TERRA_M-M | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 161.7 |
| 7ce88fae-bdf5-3b51-800f-0c191ff445cd | -22.28702 | -48.65338 | 2024-09-29 01:02:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.5 |
| 144bb73a-7b53-37c4-a7d1-cc4e3ca0145e | -22.28055 | -48.67485 | 2024-09-29 01:02:00 | TERRA_M-M | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 083d4a94-e5a8-3c2f-a492-8ab03d397fa9 | -22.27924 | -48.66477 | 2024-09-29 01:02:00 | TERRA_M-M | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| 2c97a117-fb1e-3d83-ab71-60efdba6167f | -22.27793 | -48.65472 | 2024-09-29 01:02:00 | TERRA_M-M | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 621041ea-fc9e-3a99-a2ec-a0c68ea34672 | -21.93993 | -48.45866 | 2024-09-29 01:02:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60cbe882-4c41-3e8e-8fc8-607c95335779 | -21.88587 | -48.4669 | 2024-09-29 01:02:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 92346905-dbc5-3a3a-8c90-e65be3a57f63 | -21.71208 | -46.36149 | 2024-09-29 01:02:00 | TERRA_M-M | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| c6914be8-8bc5-3efd-a838-8ba6a5101646 | -21.61008 | -47.78391 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f4c13f60-6ac0-3e85-9a4b-554222f97361 | -21.60877 | -47.77437 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| dd4cd298-89eb-395b-a78d-b8ef82c44dcd | -21.60119 | -47.78533 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 4aa02194-d222-3cd7-9a09-5700143f308e | -21.59728 | -47.75676 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f9421e4b-ba20-3867-8f69-d801e225af33 | -21.59597 | -47.74724 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 915a51d5-d5ef-3635-ad12-aec9eb896c88 | -21.59194 | -47.79321 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5793b091-6058-3a9b-bdc8-bdb40162b317 | -21.59063 | -47.78368 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 6bba3749-5e1a-37e1-ae24-3691d947925d | -21.58931 | -47.77416 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 973718fd-f939-3455-b098-90a481b2ebbb | -21.588 | -47.76464 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ad280a30-efbf-3f86-ae9c-7fda1cf61d57 | -21.58174 | -47.78512 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 18fec1b9-9090-38a2-95a1-9befda189072 | -21.58043 | -47.77559 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 46e9f36c-cdd9-326b-a2cb-8a8d7d66c3c0 | -21.57912 | -47.76607 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 6f3db478-1452-38ec-a67b-fe6717ea3f52 | -21.5778 | -47.75655 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README10.md)
