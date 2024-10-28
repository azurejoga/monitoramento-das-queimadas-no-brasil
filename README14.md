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
| 646334a9-f674-3f9a-b38a-88feb177ce3f | -3.1511 | -53.894299 | 2024-10-28 00:50:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed8ad94-b367-37f6-9c77-52c8da2aa052 | -3.1534 | -53.904301 | 2024-10-28 00:50:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd9c4f8-1d64-3fd2-8c79-1ad68295aa85 | -3.1556 | -53.914299 | 2024-10-28 00:50:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 741e0ade-64a9-36f9-9a4d-f5c985b06687 | -2.524 | -51.1731 | 2024-10-28 00:50:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58399198-381c-32d7-8e12-b72893cd5f13 | -2.5256 | -51.180302 | 2024-10-28 00:50:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5358c8-630d-3e62-9a7e-9b4010b60a19 | -2.5273 | -51.187599 | 2024-10-28 00:50:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f98cc9c-2518-3f34-a50b-ae45837787b1 | -2.5142 | -51.175301 | 2024-10-28 00:50:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cce3b00e-9687-3a27-a1d7-5833a4cc6d6d | -2.5158 | -51.182499 | 2024-10-28 00:50:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21f07b79-5eea-3f85-b19f-b57d8954d9d0 | -2.6427 | -51.739601 | 2024-10-28 00:50:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c75ef52-eb30-34d4-ab08-3c56bc73789c | -1.5291 | -47.199299 | 2024-10-28 00:50:14 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54ab786-611c-343e-a977-ef4fbed4df67 | -1.5309 | -47.207001 | 2024-10-28 00:50:14 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5b3b65b-293e-3e75-9931-79365ec53677 | -1.7329 | -54.9781 | 2024-10-28 00:50:14 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd5b3299-9271-3203-8c22-0aaa0006abc7 | -1.7355 | -54.9893 | 2024-10-28 00:50:14 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe18dd5-25af-36b3-ac9e-e807cfd5a09c | -1.7257 | -54.991501 | 2024-10-28 00:50:14 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89fb3f39-3908-3f4f-bf3c-a5d6f7cdfc1d | -1.5678 | -54.432701 | 2024-10-28 00:50:14 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eee28a2-eb7d-3df7-a9d3-526939f5e1ee | -1.5701 | -54.443001 | 2024-10-28 00:50:14 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19e209c1-f056-33dd-8218-7c504074787f | -3.1143 | -54.278198 | 2024-10-28 00:50:15 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6c69645-c2df-3981-bc35-51251cb93c6d | -3.1315 | -54.263401 | 2024-10-28 00:50:15 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c907dc6-ae46-3182-8337-f9ea07ca5040 | -3.1218 | -54.265499 | 2024-10-28 00:50:15 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30fbe5e-fc00-3768-8450-98e2a05391d1 | -3.112 | -54.2677 | 2024-10-28 00:50:15 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7453ae2-c2ed-3456-b030-e7b446739800 | -3.0764 | -54.1553 | 2024-10-28 00:50:15 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b0f366a-34cf-370b-b309-f62580c79908 | -3.0787 | -54.1656 | 2024-10-28 00:50:15 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ed5f10-90c2-3724-b78d-f4be038cd761 | -2.78 | -52.888302 | 2024-10-28 00:50:15 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b28d5c1-400b-36be-9d83-43b98686639a | -2.782 | -52.8969 | 2024-10-28 00:50:15 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d549d6cc-e69f-3fae-abe1-e258109aba6c | -3.0689 | -54.167801 | 2024-10-28 00:50:15 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e13fb045-cdc7-3393-a774-883d74552caa | -2.8666 | -53.316502 | 2024-10-28 00:50:15 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba07384-3530-3a2c-86a9-be7f6bf8d318 | -2.8686 | -53.3256 | 2024-10-28 00:50:15 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca4cba41-7494-3c0e-89c2-d644370360a6 | -2.8707 | -53.334801 | 2024-10-28 00:50:15 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0c1dc9-151e-390a-ad05-8d9bed415a67 | -1.6777 | -55.096298 | 2024-10-28 00:50:15 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e50e0c-a9f0-3c98-8a5c-787974c44c30 | -2.8568 | -53.318699 | 2024-10-28 00:50:16 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0059f9b-a20c-3357-ba69-442a18a9e0ba | -2.8588 | -53.327801 | 2024-10-28 00:50:16 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92c3875-bfce-3810-86e6-dc7897933fa3 | -2.8609 | -53.337002 | 2024-10-28 00:50:16 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3e36f9-70d0-35ae-b56b-7cd917f0772f | -2.8449 | -53.311699 | 2024-10-28 00:50:16 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 252095e4-f945-3076-a6d8-4e968cbe2aa2 | -2.847 | -53.320801 | 2024-10-28 00:50:16 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28b9e0b-4230-3c6b-8454-22635664f97d | -2.849 | -53.329899 | 2024-10-28 00:50:16 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e3673bd-500f-393b-8a68-f34a88bcd2b6 | -2.1865 | -50.598099 | 2024-10-28 00:50:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc354f6-781c-30e0-8bd1-b15951ac13da | -2.1881 | -50.605099 | 2024-10-28 00:50:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315d9185-ea1a-3bea-b9b2-4d559956ade8 | -1.4013 | -54.062901 | 2024-10-28 00:50:16 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04df305e-b4df-306f-bd77-026320cc4632 | -1.4035 | -54.072601 | 2024-10-28 00:50:16 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e71be60-892c-399a-8124-2608f9c7db84 | -1.1899 | -53.497002 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 345b1ca3-67bf-3bd4-8250-1b1e799b774d | -1.178 | -53.4902 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8cae6b-1b3f-333c-99d5-e298bf80b5ee | -1.1801 | -53.4991 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1eb85ee-6efd-3832-8c26-671740e69e79 | -1.1821 | -53.507999 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924dfe04-30c9-3c1b-babd-92b29bccfbf8 | -1.1662 | -53.483501 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd3e7f97-8c26-3e12-af3d-b953983d9351 | -1.1682 | -53.492401 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c675e3b-edcf-33bb-9f7a-1460dfb91822 | -1.1703 | -53.501301 | 2024-10-28 00:50:17 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcc0f891-3343-3038-bc0c-78a52ceafe1e | -1.2709 | -54.1222 | 2024-10-28 00:50:18 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bfaa220-4fbe-3d02-95b8-b73121a9473d | -1.2731 | -54.131901 | 2024-10-28 00:50:18 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87d92d7d-4a5b-3cc4-ad3b-8d10257efe43 | -2.945 | -54.665798 | 2024-10-28 00:50:19 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8202926-7d60-3efb-9f43-06de3717f64d | -2.9475 | -54.676899 | 2024-10-28 00:50:19 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28602780-693d-3325-86df-30e06dff11fe | -1.0794 | -53.643902 | 2024-10-28 00:50:19 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90d32e78-b428-3fc5-a3c3-f24df12b7046 | -1.0814 | -53.653 | 2024-10-28 00:50:19 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5436fc53-44b9-37f8-a58d-603eca1b124b | -1.0835 | -53.661999 | 2024-10-28 00:50:19 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a34a6049-9d17-306a-a1a5-be0398e8b3d8 | -1.0856 | -53.671101 | 2024-10-28 00:50:19 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9219e99-0782-3ed7-9da6-092c21bf1482 | -2.7491 | -54.0243 | 2024-10-28 00:50:20 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca34ce62-b503-3d3a-84b9-cf52a562ed8f | -1.0716 | -53.655102 | 2024-10-28 00:50:20 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1bf8dab-cf91-311b-8147-e6946690816b | -1.0737 | -53.6642 | 2024-10-28 00:50:20 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07853619-29ca-36ea-b53c-dbcecd932f45 | -0.9995 | -53.699699 | 2024-10-28 00:50:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f584b9-f85f-36ef-83e9-9806f4129514 | -0.9876 | -53.692799 | 2024-10-28 00:50:21 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc285122-7c6c-38bf-beef-e0f71f887d84 | -0.9897 | -53.7019 | 2024-10-28 00:50:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97796efd-934f-3c42-8319-4f05b3838239 | -0.9917 | -53.710999 | 2024-10-28 00:50:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb0d90e-f9bd-3e9d-ae30-ed7487e92d3f | -0.9778 | -53.695 | 2024-10-28 00:50:21 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3abdddd-2be8-3583-8d41-6cd5279bcad2 | -0.9799 | -53.703999 | 2024-10-28 00:50:21 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfa4720-0050-383a-b0aa-4388fee63dce | -0.9819 | -53.7131 | 2024-10-28 00:50:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30122be1-f98a-39f7-818b-08038bb41128 | -1.0917 | -47.2253 | 2024-10-28 00:50:22 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3638ec6d-0942-355c-a4e7-7fe3eda500c2 | -1.0935 | -47.233002 | 2024-10-28 00:50:22 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83cbb77a-c613-3132-ad7a-2a977437795c | -1.0952 | -47.240601 | 2024-10-28 00:50:22 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee50a8ff-44f4-36f5-8c85-6d4082d2fdc2 | -2.6432 | -54.2827 | 2024-10-28 00:50:23 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6f5d8b-386c-3b4a-8cf0-dd12252a815d | -2.6455 | -54.293098 | 2024-10-28 00:50:23 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 100a2d3a-d407-370e-834a-a233990c05bc | -2.5594 | -54.003101 | 2024-10-28 00:50:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee20e7d7-715f-3cfc-b1b0-d652e3fbfeb9 | -2.5616 | -54.013 | 2024-10-28 00:50:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aefa17fc-1f9b-3061-8d4a-4450817f5f89 | -2.0473 | -52.064899 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05002319-1219-36b1-8949-edea40138868 | -2.049 | -52.072601 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ac5bf3-3c22-3027-a20c-90c4ed5e223a | -2.0508 | -52.080399 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35521511-6873-3c84-974b-323107324ee8 | -2.0392 | -52.074799 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab805d1-b6f1-308b-a616-486e83940f07 | -2.041 | -52.0826 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 814ebcb8-ae81-3b46-8984-20915a3e1ad3 | -2.057 | -52.152599 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49280093-de78-32a3-82c8-cb0dca798d28 | -2.0588 | -52.1605 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2afe85ad-7cfc-3ae8-85ce-c4e665bb02c5 | -2.0605 | -52.168301 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0218eb20-2823-31d4-8b4f-15b43ef6eb23 | -2.049 | -52.162701 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 796a7c51-ffae-3170-99f3-b4daaaf083e2 | -2.0507 | -52.170502 | 2024-10-28 00:50:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56059e8b-7ed1-33a1-9a8e-6c953e5809b1 | -1.2917 | -55.699699 | 2024-10-28 00:50:24 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ab4712-3ffb-3c44-9f66-2cbc42f8cee6 | -1.2945 | -55.711899 | 2024-10-28 00:50:24 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf80d354-79c6-3ccd-9aea-1cb6c76377c8 | 0.0737 | -49.870701 | 2024-10-28 00:50:24 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd4418fe-34f1-3a2a-9656-005c825043a3 | -1.0589 | -48.246498 | 2024-10-28 00:50:26 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7079e9-8a17-3838-b708-fdba78cfc0d5 | -1.0605 | -48.253601 | 2024-10-28 00:50:26 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e90561-f08f-326d-b69e-adbc03127076 | -1.0622 | -48.260601 | 2024-10-28 00:50:26 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d3fa0f-7752-3347-9df5-d929754b2689 | -1.9268 | -52.1241 | 2024-10-28 00:50:26 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 729c9701-242e-3b1b-8643-3e39465d0cad | -2.278 | -53.7589 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f82b1287-fb9a-3468-9cf5-534de8e4b04d | -2.2802 | -53.768501 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd730999-dee2-3fab-815b-4e3ce50bb114 | -2.2824 | -53.778 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7fbd14b-3402-3a69-9554-2b9d14896109 | -2.2845 | -53.787498 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec359832-5c9a-3177-be94-ca1bac288134 | -2.2867 | -53.7971 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b375ca1-3570-3498-b147-78f4ed97b29d | -2.2682 | -53.761101 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c3b10c-d8ed-364b-b3a8-ae454e14fb64 | -2.2704 | -53.770599 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15c86c11-3683-39f3-a3ea-b70b2d5ffec9 | -2.2726 | -53.780201 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d26a440-1468-34d9-857c-84db78e24194 | -2.2747 | -53.7897 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 667c55ad-f88c-3721-ac76-cc18d59031de | -2.2606 | -53.7728 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d143b4a8-79c4-35bc-9740-d33134762b40 | -2.2628 | -53.782299 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caab75c3-3a41-3bd4-a882-6a415b92b355 | -2.2649 | -53.791801 | 2024-10-28 00:50:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
