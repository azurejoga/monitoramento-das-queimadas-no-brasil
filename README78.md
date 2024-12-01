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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65bab9b-fa04-3a8b-82cc-8a43ae7cc7c4 | -3.40591 | -50.66228 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa802efd-42e6-3b32-848d-3f286e838dda | -3.88317 | -51.41793 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fa3c345-9bc7-3326-a76c-c74f41666b0b | -2.96443 | -53.72898 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb2058f4-e062-3735-ab4f-71357065d937 | -2.97661 | -53.29252 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448852fb-5946-397a-bf74-01e6c3e44134 | -2.83178 | -54.09027 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ebec2ca-d502-3183-b98b-0945d2f6a731 | -3.7387 | -53.39471 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6166ba7c-d3b1-3123-9ce8-d34f16e88766 | -4.62184 | -48.03294 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deddd4b0-af37-34a2-91ce-4c6d37bae796 | -2.98227 | -51.45768 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393edeef-c9f3-3e79-aa06-1d7612280b51 | -3.49291 | -53.82135 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93f515ad-70a5-3c9a-8ab3-93518255e386 | -2.36043 | -53.65804 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f02f0e4-6ef9-37cd-b1cb-020c47ec0c3d | -1.59748 | -52.28204 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e1ac221-ccea-3648-b78b-973927b908da | -2.31875 | -53.85273 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f6653d-6b3e-3dc6-ac11-ef3fa2cc3d2f | -2.83523 | -54.10123 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1582ff33-d617-3afc-ac6e-211d0cfc6d97 | -1.27575 | -54.5592 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b1508d4-31ff-303b-b489-e14c681bed96 | -3.53171 | -53.78222 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ffe972b-bd22-3d95-8e5a-01dcb804edd8 | -3.69177 | -51.82498 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e9adbc-174e-37ab-8c59-2230522d89b3 | -3.0249 | -51.53602 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 870f80d0-448e-337d-83f4-7d36ae772f27 | -3.8666 | -50.17464 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0116d3d8-2432-3dfd-b0f0-f1d5c5bba334 | -1.48984 | -52.64923 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 971b003b-ebe7-3993-bbb2-f33b4dc29e89 | -1.36388 | -55.15027 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa1c77c9-0037-3dd1-8fa9-bb073cdd0cfa | -5.5498 | -50.27298 | 2024-12-01 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 765386c4-ac35-3921-a898-72ba6cf162bf | -2.60916 | -54.03368 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e7d3f5d-7f34-3a6b-9911-3cdaf5fb561e | -3.38604 | -49.8587 | 2024-12-01 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 001a8442-36ef-386c-8c9b-07d911dc7eb3 | -2.62335 | -46.95544 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46a9d73d-fe4e-31b4-8493-2acb102166f6 | -1.93573 | -54.57388 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0382016-e091-3441-a923-76cb0a99a52b | -3.06727 | -53.81285 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c269e1b-9d6b-3c77-a3e3-19db67d52e4f | -3.60149 | -50.37767 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 764d996e-a625-31eb-9f9c-cf8d50eb23a3 | -2.44849 | -54.00115 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c45ddda2-e3e6-3a9b-908d-95fa28a7d117 | -2.18847 | -53.57645 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a5e77fb-e65e-3928-b761-162b1585e485 | -2.56415 | -53.95584 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ebd4a0-bcdb-35ea-b405-e5aafcbb6258 | -2.04473 | -54.66127 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17fdc73f-c1f1-3d18-9d18-ae8be6e4a5c9 | -1.19774 | -53.8922 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56e0c81c-73a3-38a4-8abb-21c826426419 | -2.14062 | -54.87491 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c490851-4d6e-308e-9aa7-7f95235abc4f | -3.07821 | -53.76592 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dac37d53-cdf6-3de9-bd5c-b283750619c1 | -3.27231 | -53.41498 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64d26e18-6461-3aa8-b843-aca77f6b493c | -3.11114 | -54.04366 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84c729c0-38a2-3cf3-a5fc-2d3424ed2d00 | -1.49139 | -52.44323 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a41fc5d-1be5-3687-a9eb-841dd1c2ac7b | -3.25967 | -54.10937 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea71b201-0ce3-3d44-86ef-ad71fd29dde8 | -1.85126 | -55.61452 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6c3ce66-0f5c-3e1b-b6ca-e3d08a8874ec | -2.84636 | -54.05174 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a77cc0fc-1f68-34dd-a655-567e28b3c8e9 | -1.3839 | -53.64963 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8a27daa3-d27d-3c90-9214-456a8c3ea442 | -4.2516 | -50.84208 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820a6482-e6ee-3b6f-ac66-fc6a64e49472 | -2.59137 | -53.98766 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96cfd44b-d14d-3e49-8383-ec18b6188ff5 | -3.12548 | -53.27149 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d02ca318-f9f5-3057-850e-5524d40ce476 | -2.53619 | -53.975 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffb16261-d671-302d-afb4-28d829340635 | -3.24164 | -53.6415 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95933892-7a28-3e92-b1de-b4a1daac74d4 | -1.74835 | -52.64941 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 545770e5-e9a2-33a7-967f-01aa8516db48 | -1.66071 | -53.75618 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e96406d-2be5-3b93-b681-1bce5a5eab50 | -2.82738 | -52.94691 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95b96a9b-78d2-32ee-9ca7-0fc6debb015a | -2.80668 | -55.3045 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ac68d5-86a0-35cc-b760-139c6d6998fe | -3.10075 | -50.36034 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eca6a29-a96f-3312-9b39-262b6e8f4095 | -3.09394 | -54.1318 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12f10cc6-388a-308d-a8c9-44bc9e981b5d | -2.83039 | -54.03096 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f88e30e-3c99-3339-89bb-18904ce98cc9 | -1.65722 | -53.75563 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d632c200-9621-3137-b735-4260dad4e908 | -3.28409 | -50.60895 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03679d04-0f9f-3690-a60d-6e976cfdc764 | -3.01414 | -54.08497 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61489c14-1bf3-3f0b-a7ad-c65f6467a1fc | -3.06575 | -53.22023 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c0f6ea5-a94b-38db-b189-cd347c2b9463 | -2.46487 | -53.70676 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 719c544f-c137-35c6-8a7e-e73197e70364 | -3.53741 | -51.5005 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc5f91c-791e-3989-8250-c46b150e536b | -3.00759 | -52.02361 | 2024-12-01 05:08:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d71d0502-8d94-3623-bab5-3dede5f7555a | -3.81894 | -52.25333 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4feb0dcc-f749-39fb-ac18-eb0e41bdb03e | -2.82951 | -54.08207 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3492b9df-3ebe-39c1-b3e4-00ebab1ebb61 | -2.83582 | -54.09739 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 650172ac-8b3e-3a21-8487-d7bcc69a89f3 | -2.52686 | -53.98934 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0c38048-f284-32ee-8ee8-5bba3237006d | -1.33156 | -55.85095 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e1986d0-c7c1-32ee-8fa2-205bffd8aed0 | -3.52065 | -62.75803 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9265b3c4-0748-3888-bb87-01b72f1e0c75 | -3.84883 | -52.31736 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdb0a6d1-c274-349e-9028-ce441ea717b5 | -2.77277 | -55.34628 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a3fe908-5c70-3dc0-afee-96d76418ccef | -3.11245 | -54.01198 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0014bf6b-46ea-3139-946e-a01e9718cf25 | -1.21387 | -54.19238 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab584105-380f-34e0-9925-78ee6498c0f6 | -2.8289 | -54.08591 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea4b2b7e-09e9-3a1d-a2de-3980bdb6aa01 | -3.10006 | -54.04587 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1d3cec8-4c36-3d14-893d-610ca2366b08 | -3.08967 | -51.4081 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0320aee5-83ad-3c60-88ef-606b65f28b0e | -2.46837 | -53.96492 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f5d6fdf-665e-3c93-a36e-375685f0c8bd | -2.83699 | -54.08971 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29620a0-3616-3484-8629-5aeb0d847f8c | -2.85493 | -54.11209 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d16ebee-8bb8-3a09-ba6e-3b15a9f9f439 | -3.33513 | -54.06863 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a04ebe72-1964-323e-aeb8-1a58dcb5c12b | -2.06606 | -50.72039 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9289fcbb-fbbc-38a0-93fe-0654e2a76b7d | -3.21397 | -54.17347 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2b6c4d0-bb5b-39bf-8c60-23a958df367a | -3.07142 | -53.80945 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 928039e1-fa86-31cc-8d8a-e6975feca580 | -3.2435 | -53.62924 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f830ef8-f3ed-373e-a412-31e7b24293dd | -3.14803 | -53.82823 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf1028d2-e38b-35d1-8ee1-86f2f71ec0e5 | -2.73797 | -54.04087 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74a35450-c0fb-3f3e-b148-fc743339b7f3 | -3.21581 | -53.62573 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3764e42b-efe7-3b3d-a5be-39616f5e09a0 | -1.45749 | -54.53574 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bac692f0-a3e9-3c2a-9713-292e74d99150 | -1.71784 | -52.6269 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 152ed328-d4eb-3f8c-a9b4-ecbf4b5a551b | -2.77388 | -54.04993 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfd2a892-036e-354e-8d0e-30d32e4ed039 | -1.56419 | -53.51871 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac987018-34d0-38ce-97bf-2f345cda6180 | -2.95396 | -53.7029 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b089677-1d79-36dd-8286-34a6f116a971 | -3.0549 | -51.06636 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 16cdd3b7-4ec7-3e64-a43c-ea8fd5090e44 | -3.11054 | -54.04754 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5849890-396f-3770-8fb7-aa6a059c36b5 | -3.49754 | -53.83829 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 27ae06cb-a3e0-34aa-a0c6-d9ba2205698d | -3.02146 | -54.01483 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11ad3868-a932-3b9c-9be8-6d7f35371541 | -3.08466 | -54.1226 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6e73d80-defb-36c8-a095-7cee9a9e2271 | -3.4182 | -54.63918 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4348a2fa-a91d-3785-83fd-8e971754e244 | -3.50524 | -53.83537 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 310a54f7-ee4e-3d18-9805-cf00f05653f7 | -2.61459 | -51.81424 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a24f84f-1c4a-321f-bee8-97762906a7fa | -3.06349 | -50.33418 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d68f4567-7b44-377a-ac18-d3529416a8a1 | -2.03798 | -53.49778 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67d3a7e5-b5b9-3e89-96cd-3543c3b540c1 | -3.09527 | -51.26126 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
