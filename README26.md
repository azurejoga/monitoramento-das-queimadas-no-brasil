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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c70f3b26-db8f-3aa2-9c1a-44089024cb6e | -2.6255 | -49.22839 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a2309ba-d605-3ebe-b3c9-7986e4dddf1b | -3.50358 | -50.4641 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fad77803-0994-3a0d-b410-066ce3847c7d | -2.83144 | -49.41335 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a8b3dab-1c04-3850-b428-00813677fb57 | -3.92319 | -47.69768 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4f6a55f1-c597-34e7-889d-0d5c65e7fef3 | -3.24193 | -50.79494 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b224b61c-5c7e-3132-857b-2f4fda007eb0 | -3.91674 | -47.69668 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a2e5cdb8-8c0b-3d86-a450-8e7d87d6edbc | -3.91658 | -47.69191 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1b0e2788-2993-3e0f-9592-69b85646edb6 | -3.40787 | -50.1795 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba50e4f5-398d-3dea-9594-68feaf349954 | -2.23843 | -56.94987 | 2025-11-04 05:22:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e451cc50-7456-3d5f-8935-c4ae482dc31b | -3.50529 | -50.46895 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96a0a954-8935-32cd-8e45-461376d3484f | -3.24557 | -50.80288 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2eed9b2-413f-364b-a10b-64565b3c08c2 | -2.62097 | -49.22705 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa7099e9-d111-3948-b940-5707ea63136d | -3.44656 | -51.47433 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711ac293-6723-3c35-86df-9f9a4713897c | -3.43818 | -50.23839 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0097216a-e33c-3f67-bd87-363331f82a61 | -3.43929 | -50.23946 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5024296e-3edf-382e-b73f-c51a4b19e7fc | -3.43765 | -50.24194 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 723495f1-f83f-31f5-a7cf-605336cdf75e | -3.49841 | -50.47824 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9548fc2-3f40-34fa-bd04-6d7f236b4dd5 | -3.92303 | -47.69291 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 16f644af-143d-335e-8773-5566200dd1b1 | -3.59281 | -55.43842 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e982d09-c307-3c1b-b188-4086707d04c4 | -3.91929 | -54.51894 | 2025-11-04 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b047f9d-58c6-3c20-9533-85051603ab00 | -3.24034 | -50.80214 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f8a82ac-1581-3dba-939f-b59048ae3107 | -3.52372 | -55.42759 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ea573a5-1c86-3ba7-a00b-4d8f24cb7fb7 | -3.01222 | -51.39582 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa60535a-23cb-3816-ac5e-dc6fd0d18884 | -3.48519 | -53.28143 | 2025-11-04 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 838c2638-d39f-3b92-a760-40567bd282af | -2.84424 | -49.83161 | 2025-11-04 05:22:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aef8ac0c-19b5-3fbf-8294-5ddd1b985dff | -3.0075 | -49.47426 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 486ed9be-1722-37ff-aa83-7c45ae2d3950 | -2.90495 | -51.45983 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8cd83fe-5b6a-3539-b99d-27daa637f96f | -3.92392 | -47.69246 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c76d52e5-aac5-3565-914f-8b75cbde2d85 | -3.87804 | -51.95742 | 2025-11-04 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a457ab0f-2942-3a50-a677-2f54aa06d98c | -3.98562 | -47.07797 | 2025-11-04 05:22:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0af406d-abda-34c1-9a8a-192fcabc8916 | -2.82575 | -49.4124 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fda0c2d-ede9-37f2-9fb7-413d9b538b20 | -11.82222 | -65.00831 | 2025-11-04 05:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab7d0f49-5066-36b8-88ac-b9e3fa93b31a | -3.44362 | -50.2393 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 48f63d03-39b6-3580-91d4-b28fa196afc8 | -3.91747 | -47.69143 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3633a2a5-3756-324c-bb42-14beafe66846 | -2.83813 | -49.83445 | 2025-11-04 05:22:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2a24db2-099e-37e2-978a-35dc7fc655d8 | -3.41334 | -50.18032 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4cefdf4-5e9d-3711-b489-48bd02f5b66a | -3.77453 | -51.92957 | 2025-11-04 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b44eded5-d0e4-314d-84d8-b9ea2990f567 | -2.90409 | -51.46553 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d44229b-3eb9-3560-af2e-67cab1162f14 | -3.44423 | -50.24389 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 84eb3b7c-1e5a-38c7-b2ba-f1e61d2b7f75 | -2.94903 | -51.58186 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2e6d2bc-dcf5-3dcd-b9e4-8737b73d3bbc | -3.2458 | -50.80521 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11f19c88-ca94-3b20-bd7c-0f1d92e10210 | -3.59665 | -55.43903 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4535fe87-5a0c-385a-b5e9-bad983dec95c | -3.24147 | -50.79811 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a39189e-6f41-3dc4-a128-569165e7ac6e | -3.916 | -47.70195 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3f964c08-d2b6-3661-ace0-6888c822bca6 | -3.98479 | -47.08372 | 2025-11-04 05:22:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8511afb-e191-34c5-8d4a-745917b635f4 | -3.52756 | -55.42823 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 602e3849-b07b-362b-870c-a7e77761c189 | -2.8383 | -49.40636 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 597dc455-28a0-3884-a97d-335ff87b37a7 | -3.50312 | -50.4674 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c138c064-9f8e-3a22-8a9c-f753e89191e0 | -3.22741 | -49.49866 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51c3ae2c-d8f3-3abb-9266-6ac9350a1217 | -3.54833 | -54.69114 | 2025-11-04 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f3d6f97-89e7-36cf-bc8b-b5e9e88cade5 | -3.07211 | -47.77439 | 2025-11-04 05:22:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 048459ee-033e-36be-a8ac-f5c78553c909 | -3.52482 | -55.43081 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| def55b8f-a161-3ff3-b680-71f2e23a2ed4 | -3.5017 | -50.47734 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcfed6e7-2be1-37f2-9769-ab58e84a5a39 | -3.25027 | -52.91286 | 2025-11-04 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2024540-23e4-3c5a-b5c3-15cb412028fa | -3.43878 | -50.24302 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fcdb3e4c-3629-3df5-9fcf-b0e0d8e5fd51 | -3.77578 | -52.32405 | 2025-11-04 05:22:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 259c031c-1b98-3ef8-a39e-9676a84c91e2 | -2.61913 | -49.23156 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 423caef7-8df7-349f-b0e7-3523bcf360f3 | -3.43511 | -51.51674 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18331c88-b57a-3cd6-b46d-cfcd4a9d393f | -2.83089 | -49.41716 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e43588be-e3d0-3b18-9df7-843034e53977 | -3.38833 | -54.2795 | 2025-11-04 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba9dbd0c-4754-360c-b6ac-3cb19e92c3c6 | -3.2535 | -52.91176 | 2025-11-04 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 183e94a2-3a5e-373e-ad97-0c3a5cb37b53 | -2.94986 | -51.57621 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8fddb3-6d8f-3664-a3a0-96e21e59c952 | -3.77505 | -52.3229 | 2025-11-04 05:22:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50290130-50ce-3f16-968c-4d3acbf6e777 | -3.52865 | -55.43145 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55723889-4e66-37fb-8977-5903e24ad2d7 | -2.62039 | -49.2311 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cade8630-361d-39c5-b3c1-0bcdbceff784 | -3.24057 | -50.80446 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a94c9a37-93f3-33a3-97fc-72e007ff12b2 | -3.3175 | -53.8506 | 2025-11-04 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8babe20-1f74-3847-871f-219997f09d53 | -3.89831 | -52.31713 | 2025-11-04 05:22:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db99de8f-bc4b-36b5-929e-f6a95ee3ed78 | -3.50218 | -50.474 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95ddf52f-3daa-3e8d-bd2b-28adaf7ea5b0 | -3.75412 | -55.52096 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee13f0e6-9d29-3fdd-afd7-65094903c890 | -3.49549 | -50.46104 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93a5dc15-e191-3669-a0cd-7118a976c02a | -3.02349 | -51.38892 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0e567ed-c873-34de-9da8-c750f52f8768 | -3.02308 | -51.39168 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b2027c-019f-3990-9ad5-a6f856bcf637 | -3.24081 | -50.79897 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02f5faa7-17b3-39a8-a2c0-70fd7e079e19 | -3.53508 | -54.86314 | 2025-11-04 05:22:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa69ba65-383b-33d9-8b41-ed0c1ce906b1 | -2.50868 | -54.74927 | 2025-11-04 05:22:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d37c6fc-a3b1-3286-a20c-0be24bbb8682 | -2.83201 | -49.40942 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9c0da11-4370-3160-b729-6acc7222d95e | -2.25969 | -53.91817 | 2025-11-04 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25076cc2-98b6-3b72-93f5-98a607fec964 | -2.26328 | -53.9226 | 2025-11-04 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 353231ab-621f-38cc-8103-4a1a5beb46d1 | -3.43979 | -50.23592 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f4a9d615-5736-3901-b46e-fbdaff2facff | -2.84368 | -49.83529 | 2025-11-04 05:22:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 741bf7b4-9476-354d-933b-058867dc68e9 | -3.4473 | -50.21487 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 539d271b-6ed3-3279-aaa4-844b1df31913 | -3.45201 | -51.47216 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ce8c94e-cc5f-3f49-8aa6-bc2899378b45 | -3.44473 | -50.24039 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f9f82d1-1759-3c5e-8cb4-fd2827098a82 | -3.32174 | -53.85125 | 2025-11-04 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42b87115-c8f0-3aec-90d5-6f6b5c2906c7 | -2.94082 | -55.83022 | 2025-11-04 05:22:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0124eb97-2ca6-3648-ad43-e02a30a93a21 | -3.50089 | -50.4617 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18641ab8-022f-3ac8-900b-f3d49ba0f445 | -3.22972 | -49.49819 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b3109af-4baf-38a6-8091-e12bdae23804 | -3.50138 | -50.45837 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d97a6d21-bd5d-36bb-a023-54b62e08e204 | -3.01764 | -51.39377 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51fe01c2-992c-3efa-baee-4042d3bdc750 | -3.24102 | -50.80129 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a0bb48d-05ef-329b-bc43-6d55c6dbdfe0 | -3.43872 | -50.23483 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e285357a-c4f9-332f-bb08-ad64fc0d3ba9 | -3.49891 | -50.47489 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c8ffc8e-b19f-39a6-98c3-abc8c23f3d73 | -2.61974 | -49.22754 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8369c2bf-42d0-31b2-aa0e-f4683ef38326 | -3.57054 | -50.64246 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d3c1e41-ee94-3e00-be0d-64be653791d1 | -3.43272 | -50.23767 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4e882d3-f596-3fdf-acfa-58df5dcb9dbb | -3.9182 | -47.68618 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5546aaf4-89bc-3a8a-a877-4c1d09cf2302 | -3.91734 | -47.68666 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d9c1c3a4-d55a-3ca2-83b2-74dbe82eadd4 | -2.63962 | -54.57546 | 2025-11-04 05:22:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 2c1b9f3b-7496-3232-9247-5bb2751a7f8b | -3.50039 | -50.46499 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README27.md)
