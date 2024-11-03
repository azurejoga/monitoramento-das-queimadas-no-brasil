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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad0714c4-4e9a-3344-be9d-1fe73516e4f8 | -3.55072 | -54.60103 | 2024-11-03 01:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca9a76e6-eaec-34ab-8bf6-6d8ef161f73e | -3.55067 | -50.86952 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| cabd7f82-1f59-3704-9220-607e7af0de1c | -3.54369 | -50.89057 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| d03c193c-261c-30a7-b8bf-201c08850023 | -3.54265 | -50.29889 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 61c391a8-a8b4-33ae-8467-f9d1a63e8402 | -3.54185 | -50.2923 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 0e14f9c9-a0f1-39dc-ae69-6a032531f4f5 | -3.53981 | -50.86568 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5831b348-8b02-3a18-9a5c-1edbd3511e61 | -3.53647 | -50.87183 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e9c9fc2a-3204-3703-ac0b-5c05d14b35f3 | -3.4812 | -50.39848 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| fbe1f45c-0ec8-30bb-8fa9-405c4542830c | -3.48112 | -50.39303 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fcbe022b-dec2-3256-91d4-98c626d4ab22 | -3.47713 | -50.3709 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5bd4c149-1c9d-327f-8214-5e306f307b1d | -3.47683 | -50.36541 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| b0c23acf-3c41-3d18-aec7-88208e2edb05 | -3.46232 | -50.37323 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 533d0e72-1798-30af-b4d2-a3f4885d9942 | -3.44559 | -56.93699 | 2024-11-03 01:34:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a369b21-9ada-3851-971c-4daeae3d0527 | -3.4042 | -53.81094 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0ed57ada-4228-306a-a9e1-7486f289b667 | -3.38072 | -50.95838 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 8b9da184-6df0-3794-8d5c-5c0a16494174 | -3.33324 | -53.79778 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b6ff4a43-f530-3935-b1a5-7c8b45ccf7eb | -3.33108 | -53.78266 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b5fe34bb-363f-3f85-a3ba-a485307f0b45 | -3.32718 | -50.28676 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 78c29a7c-5b03-3ef0-b75b-a7f84599ab9a | -3.32292 | -50.25861 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9daad6ee-86cd-3e85-80cd-05bc2d096c01 | -3.31499 | -52.85771 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 088e25d5-3e69-3af2-b2dd-3573a07c65ae | -3.28143 | -54.53436 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 52c6ffd5-a930-39c6-b435-f6e210846cb5 | -3.27712 | -54.54134 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| fa9f236e-27a7-32af-9283-4a4d4b386292 | -3.27584 | -52.73126 | 2024-11-03 01:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| bcec7282-9deb-3c6c-8d9f-5ba09453786e | -3.27527 | -54.52817 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d9cdacd6-98bb-366f-9a56-3529237c55e7 | -3.27278 | -52.73714 | 2024-11-03 01:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| fd6b2151-0005-32cd-83be-3c42e7c146f9 | -3.26821 | -53.74678 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b644f53-a180-3bd6-adc3-7594a9ca3021 | -3.25906 | -53.763 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9f3affb1-de50-3047-ad8a-d5874ce412c1 | -3.25825 | -53.75363 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f498c460-31c8-3ef0-9291-b37076d8d507 | -3.2569 | -53.74847 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3f87ad11-7dde-3c07-9351-31938b6cbb9f | -3.25508 | -53.41789 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 46d7d2eb-7f3a-35e0-b232-b0999c0caf21 | -3.25281 | -53.40231 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f21b7e6e-571c-3505-806b-fd4c7c3bf02b | -3.24872 | -53.07804 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bee54994-7771-37c6-9b5d-7ec4315e40ef | -3.24116 | -53.40388 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| a63d4f67-9754-338d-b124-5cb9053b09f4 | -3.2365 | -53.37211 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4dbbc418-5f1e-3ee4-9e9d-4ee1c4ed5435 | -3.22949 | -53.4054 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 88c709b0-556c-338f-88ba-379dfe115e17 | -3.21032 | -53.41425 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 01a7d4f7-f3e5-33e7-a86d-95853d208216 | -3.21019 | -54.94461 | 2024-11-03 01:34:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| f548cfac-4cde-3513-91a2-09afe2288b83 | -3.20866 | -53.42513 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8b146bda-7ad1-3a49-8620-2bff9cb6f414 | -3.20631 | -53.40937 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 1db3e6f1-0e50-37d2-9c79-332b96b7f89e | -3.206 | -50.28859 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| d56119d9-d5db-35cf-bed8-3d36367917d4 | -3.20468 | -50.28223 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 4b68eae3-9f8a-378e-8898-1c6a991ff0ca | -3.19871 | -53.41611 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d7ff7e25-ef4a-3a56-a573-ad94b15ef8b5 | -3.17231 | -50.58085 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| fdcf79ad-baf1-3b17-b972-d0b878287710 | -3.15345 | -54.47066 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c0be5e2c-f1fe-3262-93d7-d69197650739 | -3.12274 | -54.25485 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 36f6a8a2-3761-38d6-8dc8-3de96fadcacd | -3.12136 | -54.4756 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 997656db-631a-3878-a6b7-e979b15e93f2 | -3.11755 | -50.30767 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 2f3d5ed6-0ac4-3f2b-959c-355f08203742 | -3.11612 | -50.30235 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 38379227-e058-3f08-81f3-eaf1d1420431 | -3.11341 | -50.27925 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 62124436-5453-3367-b4df-db8e928e3494 | -3.11175 | -50.27392 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| e9611539-7a9f-3cfe-bce7-1093560cc534 | -3.11062 | -54.47694 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 981ed56b-a9b8-35e7-b563-73946647641a | -3.10692 | -54.29938 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e2f284a5-d45c-3e7b-ad1c-121fef0e6f47 | -3.10495 | -54.28571 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3165b01c-e53f-3898-b2e9-b07661d3567d | -3.10257 | -50.30994 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 9e9967e1-b551-350a-8419-f37bac08fbfa | -3.10113 | -50.30457 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| def0356c-2ed1-3091-ad74-47389423d29d | -3.0984 | -50.2816 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 1687acf3-cfe7-3b77-af6c-8507cdda1d80 | -3.09675 | -50.27626 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ab483d5b-0487-3d98-b15d-c1be18579be4 | -3.08691 | -54.16064 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 23993e7c-768a-3406-8c24-d59fbb6648b1 | -3.08489 | -54.14662 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 35614bd0-698e-3bfa-ac3d-7f2c6dc657a7 | -3.07595 | -54.16233 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9be66530-8d30-3555-b789-d47d0c50bd18 | -3.07392 | -54.14837 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 4c6865e8-bf98-396d-9f70-3e17800d9545 | -3.06499 | -54.16407 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0180c133-9698-3f6e-8ed1-8a7f0837cfd6 | -3.06294 | -54.15002 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 164b773d-b69f-3a41-b397-8fdc0e01facc | -3.05737 | -50.51545 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3672e44d-e35c-32ac-896d-9922a1690004 | -3.05326 | -50.49469 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b815e664-90f4-3ee4-8539-93abc1692951 | -3.05195 | -54.15168 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 530a63db-e29d-3f0f-9a93-3f10e86557f5 | -3.04988 | -54.13758 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9f5db8f9-4057-3e3a-a6a0-5d20778c450a | -3.04923 | -54.20921 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1259ce19-ae10-30da-8c20-1ddb1d012d5a | -3.04717 | -54.19525 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2f5a7812-78ad-370a-8836-a50622c280e9 | -3.04559 | -54.20191 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| dfd49087-5ec0-3a7a-90a1-958aa0270980 | -3.03938 | -53.28114 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| b38380fd-9d76-3c6f-8c22-bc93210ad84a | -3.03829 | -54.21081 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2335d93d-acb3-34a8-8c86-b5b7f2908b56 | -3.03695 | -53.26456 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 4298fed9-007c-3327-a22f-f6e7a7eab1ad | -3.03621 | -54.19687 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fdcbb2ae-b2fb-3fda-b1d1-88397c328ecb | -3.03464 | -54.20354 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 384c54bf-a249-32f0-b576-0a39d9fc98e9 | -3.03211 | -54.49501 | 2024-11-03 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 92242527-a09f-3438-9d52-dffcd3803001 | -3.02369 | -54.20515 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f641670c-01ef-39ab-bc85-25e9be319538 | -3.01219 | -56.93299 | 2024-11-03 01:34:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87bb6215-9a12-368c-ad62-99cec5176499 | -2.98594 | -49.51858 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| c4385d09-1e77-394c-b40e-d54a8a2b0921 | -2.95203 | -56.77462 | 2024-11-03 01:34:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93c07377-fda7-3647-af9f-4cd852eb6f2e | -2.90773 | -51.481 | 2024-11-03 01:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4d30154f-9db5-3669-8183-53164472f6e1 | -2.90437 | -51.45786 | 2024-11-03 01:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 09fb7585-7409-3483-8770-054fb29e8043 | -2.88403 | -51.31776 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d1a94f68-5df9-3236-979c-0b6643c33534 | -2.88132 | -51.74267 | 2024-11-03 01:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 54725d8a-b206-34d6-ba90-c8b4ff57e397 | -2.87547 | -51.31359 | 2024-11-03 01:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 95baa633-2f65-3fe8-9d76-0c6e9bdc7de5 | -2.82755 | -57.71449 | 2024-11-03 01:34:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 986f279a-3597-3e7b-8e57-a0fc77a0afab | -2.82627 | -57.70545 | 2024-11-03 01:34:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b8b4162-be2c-32fb-9ba0-4c8821fc8e48 | -2.82603 | -49.16808 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 82be4890-e987-3c68-869a-4b691c9ac2a9 | -2.80287 | -52.47153 | 2024-11-03 01:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 49c06b57-4215-3a80-9d2f-6f9e90c1a4dc | -2.80255 | -52.47819 | 2024-11-03 01:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b0bf5707-7143-34af-b78f-2047675bace1 | -2.79985 | -52.45909 | 2024-11-03 01:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| efbaf539-7380-3e37-a677-fd86880516d0 | -2.79458 | -51.62016 | 2024-11-03 01:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 37ca81f5-d4a7-3e19-b2f5-10d799288841 | -2.79123 | -51.59758 | 2024-11-03 01:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b3aac8b1-6255-3f8d-9902-69acdc111c51 | -2.75775 | -54.43019 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e0949be6-5391-3b95-8935-d045a92219ee | -2.75581 | -54.41663 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e39bb918-d8b5-3044-ab64-f4b141409cde | -2.74692 | -54.43161 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 371.4 |
| f40efb64-0bc0-3410-86e6-c013661b205a | -2.74496 | -54.41801 | 2024-11-03 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 624a4944-994e-387b-9bc6-e907e6afcb13 | -2.74314 | -53.22363 | 2024-11-03 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 959b8878-363f-397d-82cd-1be2562ca93b | -2.72592 | -49.33043 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| f002635b-0e41-377f-b781-2ae2c487f37e | -2.71892 | -49.33829 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |


[Clique aqui para ver as próximas entradas](README15.md)
