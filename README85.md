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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 980a07ec-d465-35da-b0dd-23b01fbff5b3 | -4.09713 | -51.11236 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d9bb320-bacd-333e-80df-408321c476ee | -4.05174 | -51.11213 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d459e7a2-7de2-3e15-90f7-4d3674f6adee | -4.04708 | -51.08899 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88b73b81-5ffb-3554-8029-d598d3c04ce7 | -3.95413 | -50.8915 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81c7ad22-6225-3e8b-8fbb-30a97c1d640c | -3.95148 | -51.00986 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2590886d-1f76-3bc4-ab4e-6ca7476b2ff7 | -3.94694 | -51.24651 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed2a9677-cd83-339e-ba80-b3920646a8b4 | -3.94157 | -50.99339 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3053ebc1-6d47-3e34-b878-ed4383ab3e1d | -3.9353 | -52.20846 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796fbe8a-bb2a-35cb-839b-e2a62f7bd99b | -3.88215 | -52.09354 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9738c3b1-7b25-3adf-8464-d0cbedf73f0f | -3.877 | -52.09732 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35de6c7a-6222-377a-873d-bbe33b7752ff | -3.86424 | -52.25781 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b81fbdd-7226-38c1-9866-8664a71a8774 | -3.82686 | -51.34457 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9e3cbfb-9f88-3cf1-9d25-12b7c4406ed2 | -3.76265 | -51.86257 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da20d989-5ce1-347c-abdb-d46f7ececd92 | -3.76003 | -52.26071 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d42b30-b7b7-34f5-9308-fe435e864575 | -3.75559 | -52.2598 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 611785c3-75e1-3646-80ca-7470b9b7e1d9 | -4.10125 | -51.11296 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bdbbf7d-a101-3ff7-8ba1-755bbacc6cdd | -4.09809 | -51.11273 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b653090-1a43-3c64-b94c-477cbd3e212d | -4.09693 | -51.11997 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6b48e4a-5e2e-3efb-b36c-7245ab12d128 | -4.09652 | -51.11598 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 925b571d-66b1-305a-befe-f88d9ada4190 | -4.09592 | -51.11959 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5aef129-9989-365b-a838-813e1d838f86 | -4.09281 | -51.11937 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d5fa593-57fc-3091-8ba2-c5c928a44895 | -4.09221 | -51.12309 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d0812c7-0502-30e5-ac80-7b51c5f3ec43 | -4.09179 | -51.119 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ac95611-51c5-3b58-b4ce-0221f1289c72 | -4.09117 | -51.1227 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0f3f061-443a-3e25-9b08-8097e4b86f35 | -4.05119 | -51.08964 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e15a34b1-e0e2-3679-8107-84a0a592fe1e | -6.47788 | -51.50431 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e4f31b4-665d-3eef-837a-6b18d76a4c89 | -6.47727 | -51.5079 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2c89d87-ba48-362b-a628-b998908431bc | -6.462 | -51.44983 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0c4713-5536-346c-9966-3813e9dd55bb | -6.38407 | -52.70498 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3dd22c7-5998-3d6e-918e-dd6e5a6f7623 | -6.38333 | -52.70937 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53d35b1d-542a-3021-b4de-f8ead2647988 | -6.37892 | -52.70861 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91917859-7c7c-39f4-a1ec-e0f36d49d159 | -6.32202 | -52.75386 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e50a1a62-622f-33c2-8d53-b3fe9aae1d9c | -6.32133 | -52.75236 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ced6da18-b812-36b3-96b1-faed7d71c1e3 | -6.32128 | -52.75834 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 837e1ad4-ee96-3c37-92fa-4d5750e2a09c | -6.32057 | -52.75678 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 627c9bac-284c-3d76-8013-f2e4f71e63fa | -6.25321 | -52.35255 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0ec8210-cbed-3f21-b1f3-d0b5c39e501a | 0.81349 | -51.85013 | 2024-10-03 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68974d58-7328-3398-88ef-78a7c1557ac7 | -2.95027 | -52.91279 | 2024-10-03 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb14520c-0f17-37ec-9420-9ef84bb7e0e7 | -2.94941 | -52.91794 | 2024-10-03 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfafba62-66a5-3358-b2fa-d570f0c89597 | -2.94467 | -52.91719 | 2024-10-03 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af913e58-d50d-32c5-9ed0-d7ebbaefdc13 | -3.29711 | -53.69975 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7be1f6b0-e7d2-31bf-ae11-8c5c702683eb | -3.29213 | -53.69895 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06dc7e92-acb4-368d-99e7-9cfc7f961d93 | -3.76624 | -52.33549 | 2024-10-03 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85f7f740-4220-35dd-a8bb-7f33e1f88b19 | -3.76551 | -52.33999 | 2024-10-03 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cce5e95-16db-38b6-b27e-702bb60435be | -3.75487 | -52.26416 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83356b09-9afa-37fc-8d6b-9ea162ec82a2 | -6.19621 | -53.28292 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9c34c482-412f-3fd2-aeaf-58bf908d8742 | -6.19161 | -53.28214 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e6f9d3b3-c6e6-352b-9410-3cb48e004ade | -5.87646 | -53.88997 | 2024-10-03 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44b32b89-527f-3155-a9d2-630a3c5ff8d6 | -5.8509 | -53.55431 | 2024-10-03 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f86f93ab-68d3-3b84-8d40-f2b48029de85 | -1.7606 | -54.44901 | 2024-10-03 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89b51ce5-10f4-34ce-bd62-837e098b1f90 | -1.75524 | -54.44813 | 2024-10-03 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 448e7fde-f347-3865-a10e-7c22cab448f3 | -1.75468 | -54.45154 | 2024-10-03 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9a5e53f-b39f-303f-b8b2-7af37402e4a9 | -1.14254 | -53.64028 | 2024-10-03 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22ed0da9-cfc5-3b60-98f3-1f8580993ed9 | -1.142 | -53.6436 | 2024-10-03 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6759a158-df5e-3f7b-9d51-f7c44d7b067e | -1.13828 | -53.63403 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5b23379-db38-31d6-9b97-1ff0c2f49b25 | -1.13777 | -53.63721 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca11a7f0-993e-3c00-b4a9-f5296e44c243 | -1.13726 | -53.64036 | 2024-10-03 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4198fa97-c065-3f5a-836d-a0eca3b68c28 | -1.13676 | -53.64349 | 2024-10-03 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4276e5aa-40ac-3d9b-8a78-b37c170c0f97 | -1.13261 | -53.63659 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9888aabc-7cc0-3dc6-9b0d-f7992b00639a | -1.052 | -53.53201 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc29dc5-0c7a-38b5-8bc0-a8cfb8160478 | -1.04787 | -53.52518 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 990427ba-0e6b-3ba6-b13a-faf4f4225e68 | -1.04736 | -53.52829 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5106d9b-c0fa-35cb-800b-1eb8998811ee | -1.04687 | -53.53137 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dba91b16-03b7-37de-b62a-3383963f9704 | -1.04421 | -53.51543 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84788462-8a59-392b-be88-dbf503462276 | -1.04373 | -53.51841 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2f7cf9f-74aa-300c-8928-37038a0bd0c0 | -1.04324 | -53.52144 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d97ecc2-33f9-3874-850a-89464b23ee25 | -1.04274 | -53.52455 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdcfa4b9-bd07-347d-b0de-ac47d0aeb4cc | -1.04224 | -53.52766 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35a30cb7-b584-310a-b119-d01b91b1a891 | -1.04175 | -53.5307 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 464f71a0-ca5f-3d07-ab64-3facebfa2d99 | -1.04004 | -53.50888 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3d331e5-ae26-3f40-af1e-3cee8007cf17 | -1.03956 | -53.51184 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9317670-3e48-3b6a-8581-2b2b9e7e3276 | -1.03907 | -53.51486 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e9cb4e8-4c80-3393-b449-8b58eb369f1c | -1.03809 | -53.52098 | 2024-10-03 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54374d00-4fa8-3b21-8919-2f073471447e | -3.50899 | -54.03025 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5033b7d6-416f-31b1-a9af-182dea7c00ed | -3.50555 | -54.0283 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7740b997-06d9-32d9-a323-d532d3876b08 | -3.50508 | -54.03122 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b82ae61-aa68-3ae2-a1d6-7cd0e4a44963 | -3.50443 | -54.02647 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73afcfa1-0e9d-302e-9215-a0a18740dcd9 | -3.50393 | -54.0294 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cf36798-93fa-3640-a896-fb55f4c2a0cd | -3.50343 | -54.03229 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 010816b7-485b-3aa3-814b-31941291515f | -3.46578 | -53.98551 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c7e6d28-5904-3f65-b6f0-1568add6b260 | -3.46123 | -53.98161 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eebfe8fc-f733-3b65-bc15-efc5aff4c0d5 | -3.46073 | -53.98457 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4f13a16-0aff-3b9e-a129-74f5b96a5559 | -3.46024 | -53.98755 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c98b4986-17a8-3ddb-8868-712eb2dc238d | -3.4567 | -53.97763 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb069b1c-6e7c-3137-8ae1-e23512360d61 | -3.4562 | -53.98063 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f62ac035-1a65-35cc-a9dd-f5c30d80e3a7 | -3.45569 | -53.98364 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ee105b6-44a7-32d6-b0fb-a55d79f3b773 | -3.45116 | -53.97967 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5376716a-c3b1-3658-9722-194bb3bf1ec0 | -3.45065 | -53.98273 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b117a05-21f8-32ed-a098-0063d0facc12 | -3.38111 | -54.11591 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 499a2d08-82d2-31bd-89cd-f05c628d0465 | -3.38062 | -54.11881 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adfc111b-76a0-37ed-ad1c-08307a1217a5 | -3.38012 | -54.12173 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1951941c-c333-32cb-a6ec-57274761b77a | -3.37955 | -54.10675 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ded1e237-1e5b-318a-92e7-5ef4bec53b33 | -3.37905 | -54.10986 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1837025-7d3e-3a54-b6f0-27af0eaaa350 | -3.37855 | -54.11291 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8932e57d-b5ef-358a-88bc-e3615380871e | -3.37807 | -54.11582 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 561d98c7-7b1d-34ab-a8fd-74bae9a7f4c6 | -3.37807 | -54.10297 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea6a22ef-fd22-3053-923f-ba27c9144024 | -3.3776 | -54.11872 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1685075d-8fc7-3003-854f-a8e974c5ec1f | -3.37756 | -54.106 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3446f45-b2b0-3427-a9c1-da275c733baf | -3.37713 | -54.12163 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9af9eac4-e13f-370a-b2d2-0078dd3952a9 | -3.37703 | -54.10908 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README86.md)
