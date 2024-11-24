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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3e375bb-7858-334c-8813-b0ee5ac50b5a | -2.2712 | -47.972099 | 2024-11-24 00:21:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed6c8747-b429-3e84-9a34-bb851f599511 | -2.7435 | -49.105099 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9488dc48-7f3e-37f7-9733-f2f66dc949f0 | -3.0626 | -53.202702 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f72b82-0be5-3711-97e9-60f2841708e0 | -3.7833 | -52.2841 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b62d3cb0-f10e-3b71-81eb-7f8e59207949 | -3.5405 | -51.5144 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a95d855-8560-3ad0-8c61-9a08d5ceb6dc | -3.2243 | -54.211498 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5f7e302-64b4-324b-8b96-c9acdebfc479 | -2.3884 | -50.3204 | 2024-11-24 00:21:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e06aaebf-4b30-3690-b37b-6b90d8df23c1 | -2.1738 | -53.776199 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59e1ff32-b8b2-32f0-8401-929d22ec0ad4 | -2.097 | -46.2519 | 2024-11-24 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4416a2-d6c3-3039-9c8b-8e41fba655eb | -3.2183 | -53.906101 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420f702c-6fa3-3ba0-b09f-d8956d6bf433 | -6.6419 | -47.3368 | 2024-11-24 00:21:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91625d17-4e16-3927-9b5c-7058879c6221 | -3.2482 | -50.664799 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae11c817-bd60-384c-a8bd-f6a5538e22f0 | -1.8569 | -47.9175 | 2024-11-24 00:21:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21250d35-9635-30c3-837c-f7f04b54a44c | -2.6211 | -54.911598 | 2024-11-24 00:21:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 000967d2-b892-3035-a450-d1460ad93123 | -4.1037 | -51.040699 | 2024-11-24 00:21:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a625fc83-6fbf-3b38-abcc-5d765147fbe1 | -1.8349 | -46.6395 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a63729-fd4b-34d8-8033-d4b8b869af17 | -3.1665 | -45.297699 | 2024-11-24 00:21:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6caf390-d2af-3157-a42c-69aca07c1a4c | -1.8118 | -46.628502 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc78c6e2-e32f-3f67-9e0d-416dba85e3ae | -3.2087 | -52.565102 | 2024-11-24 00:21:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02307334-3db3-3a5d-962c-6649e228d85b | -3.5387 | -51.5065 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d374ca6-abe6-310f-9fc5-19725c6c73a3 | -2.6155 | -54.239601 | 2024-11-24 00:21:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e10651-4e8b-3d1b-8b73-78dff7214d93 | -3.3563 | -50.504002 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c714223-426d-3f5d-9e30-e2461a8d754c | -3.6144 | -52.449001 | 2024-11-24 00:21:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9e660e-03db-3e03-916a-60ffedcb338a | -3.4808 | -51.985699 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70eb5682-3296-3ecf-80da-9ac318251c1c | -3.4924 | -51.991798 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ecd341b-9364-37e3-9a48-ac19d5d2a1e0 | -2.5789 | -54.213402 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0abd9b4-377e-3167-986b-7e567a5f46f9 | -3.2463 | -54.218201 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb1f3ba-b737-3c52-9a40-67751cabe343 | -3.3013 | -50.350201 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22e04eab-af81-30c9-b204-8dcc13d2c837 | -1.81 | -46.6208 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac45fbf-d814-3520-bdd6-46ded752d1c3 | -3.2512 | -54.194 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b9498e-7a65-389a-9683-b2fae263ab89 | -2.2698 | -46.1964 | 2024-11-24 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e589919-ab61-38e1-af3c-664ce61ac1e8 | -2.3527 | -49.063099 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2ba1327-c175-3dde-9a3c-b1dccbf424db | -3.6687 | -51.721199 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd491fc-2dc9-3f42-ba9f-6b6484e7e6ae | -2.7605 | -54.0611 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f12ee8-961e-35f7-8520-378c97e95d43 | -2.0124 | -46.287498 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdd36b41-d72a-38d8-9059-e9ef84899556 | -3.223 | -53.927299 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec738940-e34a-3146-a2d3-f4199cf67d47 | -2.6237 | -54.923698 | 2024-11-24 00:21:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59fba560-4e63-3deb-aca5-5255dafd2874 | -2.3466 | -49.0359 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a707a895-6714-3277-85d8-4df075fd8eb5 | -1.9718 | -48.380402 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52bfd570-1ee4-34fa-bb83-2e0b684c4e8d | -3.6669 | -51.7131 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f18957e0-4859-3033-9209-445036addd12 | -3.1567 | -50.578201 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28b22f0a-d048-381d-81d4-743cdb75ba43 | -2.5814 | -54.2243 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a39ade8-892f-3b7c-b291-b950683507b0 | -2.2096 | -46.3843 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d31bf98-fdec-3287-9f19-41f3b09efa6f | -7.5775 | -49.402199 | 2024-11-24 00:21:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d34cda0-da85-3d8f-875c-af012510465a | -2.5822 | -49.212399 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8d1b79d-9515-3003-833e-3c185640c04f | -4.6991 | -45.689499 | 2024-11-24 00:21:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5591e286-5105-3d72-9ebc-dea349121c57 | -1.8615 | -48.165501 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af65c382-7efd-33c1-98e8-cac4db79af98 | -2.3134 | -50.582699 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43068460-a26c-3800-bfd3-1458596c55b0 | -3.0528 | -53.2048 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9776008c-e804-39d4-9cdb-7edada96387d | -2.1886 | -53.657902 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77b14401-2a2a-36b0-9df9-c3e8246f6afb | -2.2078 | -46.376499 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7024e060-ee2e-3ecb-851f-e241049dbd4c | -1.4255 | -46.061901 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 432b98d1-10b2-327f-9d4b-d8bdd12a9b01 | -20.323601 | -48.817501 | 2024-11-24 00:21:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 079ccaae-edf7-34bb-b682-fba5c96ba087 | -3.155 | -50.6166 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4427b041-3a01-3a54-9bde-438495d2eab2 | -3.0717 | -49.189899 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f46dec7d-d496-3bf9-9d03-ddc4e6dab580 | -3.6289 | -52.236401 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7991e1d8-9664-302e-a10b-6bc498acd1cc | -7.6857 | -42.9758 | 2024-11-24 00:21:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5edd12c-d9f1-3d80-abdb-cb854383cd88 | -2.5776 | -49.191898 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59d3c239-784c-3683-9ea4-c66e5b9df4c2 | -7.5759 | -49.395 | 2024-11-24 00:21:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9c5421-3de4-3e53-bf1d-663d10577adc | -2.5137 | -48.361 | 2024-11-24 00:21:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e49aec-f662-3a90-89c1-fb07fa18108c | -3.3855 | -50.726799 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35d3f7da-ed7c-3859-8cab-cf7e3b0d26c4 | -2.0485 | -49.725101 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb51dc0-464f-370f-8724-5d2c15cc10a5 | -2.4592 | -49.032299 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b03e103a-4f44-390f-805b-1d06ce8865fb | -3.055 | -53.214298 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ced063b6-e609-3b10-9a14-f1e7cc48b2c3 | -3.2586 | -52.8368 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af68102-1a85-326d-8bcc-be3702d6be88 | -2.8664 | -51.812 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f570898-a677-3c6e-863f-fedf7cbaf8bb | -3.0751 | -50.950001 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3a014d-c6e4-3227-95bc-1398f5a690c5 | -2.1563 | -46.648201 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 221b70ef-b16c-383d-9585-d8a1840fd1c1 | -2.1798 | -53.6185 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57db8607-4f91-31b9-900e-992905ed0469 | -1.9653 | -46.850498 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73521c82-2140-389f-bd90-002c89626ef1 | -3.4691 | -51.9795 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a3d7a0-8f5f-30a6-a670-355c35351802 | -2.7368 | -49.120998 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe19ba5-6eec-3864-91c6-e88d2607a816 | -2.7337 | -49.1073 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aedece6-5f72-3a25-b544-f618b0309f37 | -3.5171 | -53.494801 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5a4a217-a10a-3ca4-a1a3-4efb7f77b785 | -3.0014 | -51.5415 | 2024-11-24 00:21:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b84e461a-5834-3f7a-ad08-625efc0d51a6 | -2.7391 | -47.535702 | 2024-11-24 00:21:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3ef787e-a11f-36b8-9af2-6061bc812ba4 | -2.1687 | -47.929001 | 2024-11-24 00:21:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b285cd2-c809-39ec-b9fb-2d958105df7f | -2.234 | -50.458302 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25826e69-a7e9-3505-8c32-bb95d8bcfb8a | -3.2561 | -54.216099 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcbd9412-1e63-35ba-a3be-b8923d6b3b1e | -3.1828 | -54.3022 | 2024-11-24 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f976e21-329c-3427-a663-d22fde7a0362 | -3.1342 | -52.970001 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb4396c-441b-3bdb-b7ea-0b356d1de70b | -5.077 | -44.158298 | 2024-11-24 00:21:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1085516-e6b0-3c0b-9c30-9bb6c99048a6 | -2.4626 | -49.138802 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0de57826-17b8-3d9f-9fd0-5ab6cc00942d | -2.5898 | -54.031399 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de3826ac-8d6d-31c6-be12-2ab1e618f4bd | -5.0792 | -44.167801 | 2024-11-24 00:21:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae4ca5b0-94a6-3e2e-8fcd-07c485f26c91 | -2.5153 | -48.367802 | 2024-11-24 00:21:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4d6a1b-bd09-3fef-897b-0185b1fdd041 | -2.2782 | -47.1394 | 2024-11-24 00:21:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26dbcd24-0548-3647-93d6-34d31af23d87 | -2.2138 | -47.764198 | 2024-11-24 00:21:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59d1857a-c63b-3090-bab3-0ccacea92cf6 | -2.2594 | -48.740501 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef036076-d491-3859-a289-e80e3a70f5f3 | -4.7691 | -44.7859 | 2024-11-24 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d79e3822-2c66-3d03-b001-9d77a0e2eb8f | -3.2427 | -53.274502 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aea75ae-7581-3209-ad1a-759e31f7cc28 | -4.0249 | -46.662701 | 2024-11-24 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 171965b2-c606-37e0-ac46-4e496b67f212 | -1.8713 | -48.1633 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecf368fd-6a8e-3bb8-992d-e3b7032760bd | -20.319901 | -48.798801 | 2024-11-24 00:21:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 01dbd5b6-db22-3de5-bca3-ee49372c889e | -3.6406 | -52.242802 | 2024-11-24 00:21:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13122574-9310-3a81-9697-9287edab33e2 | -2.247 | -50.470299 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f11eca81-345b-3171-852e-91646b73bc61 | -3.2207 | -50.910198 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9537577-c79e-33ee-a294-c40f9b853f4c | -2.4586 | -49.075298 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fa6a4e-0d35-3c89-9a88-e4b785563adb | -1.8181 | -46.610901 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3167715e-3e61-3512-97be-cef10c93d94f | -3.2267 | -54.2225 | 2024-11-24 00:21:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
