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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e7059d9-027a-39a4-98d6-3dfc148dcbe8 | -3.12079 | -51.31356 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f37ce67-43ae-3db2-9630-5e548e91d2ef | -5.43063 | -60.18578 | 2024-12-01 05:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feb9a0ad-7767-358d-89af-7358120b3d3a | -2.44782 | -54.02856 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f802ebed-09af-3003-b5c7-b6c58196a7e7 | -2.83238 | -54.08644 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14737797-7851-38e4-9d69-6d8639129f61 | -2.7946 | -51.8957 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bd349d3-7a03-34a9-b83f-fdcf2349a636 | -2.77101 | -55.31353 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19d44907-30fa-31a7-b2c3-eadc882486cd | -2.7772 | -55.33976 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90e4e81f-b889-3888-bc82-61255b4e8ba5 | -2.92504 | -54.2706 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4599a1ce-0d55-3580-b883-960ec82590df | -2.92437 | -54.36702 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a0f3b4b-29ca-360b-bb5e-d5a873ff242f | -1.72351 | -52.49263 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44fefaaf-434e-3aa5-a778-79e8a991b020 | -2.84332 | -54.11815 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 364e8c96-55d1-34f5-b742-45e276ece10a | -2.81524 | -53.05091 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3320b333-fcf8-3e13-9977-da37661e85eb | -3.4718 | -47.68652 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 719ece9b-304d-3943-be8a-60bcebd69636 | -1.68141 | -55.0086 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d84f55bd-ba44-3db0-805e-3a3cb26cb4ee | -3.80345 | -49.72824 | 2024-12-01 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 509fd8a0-31c1-369d-b57c-2e0d2c3ad72d | -3.12056 | -53.27933 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8427a8a4-8713-3bb6-b11d-9a979dc8a655 | -2.88213 | -53.3229 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99858671-4d26-33d1-8bbc-4a1aa26ebd80 | -1.3299 | -55.66745 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54a54a92-846c-3d3a-9dac-9a53ecfba77c | -3.24397 | -53.65014 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0857e9b-2786-3a5a-8291-89e648c4566c | -3.44245 | -54.12347 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df2116af-a3c3-3959-b510-55d5ea29a835 | -3.07529 | -53.76139 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8024419-08c7-35d5-9a0b-8456d79a6f46 | -2.77448 | -54.04608 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87a5ccd4-9a32-30ea-9a40-2ab742659bc5 | -2.89187 | -54.01132 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19dfc679-530e-3867-b566-53bdeeb29164 | -2.97087 | -53.89576 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b1988c6-79c4-3294-a195-45ab4773e09b | -1.26955 | -54.55455 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d22d431-8e0f-39fc-a6c0-a2901a6ad4df | -3.09275 | -54.29978 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc646746-800e-3cad-a988-d74a40d345eb | -2.54455 | -55.22438 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8601ecf-7029-3c50-adfa-9d088b8b3bdd | -2.44992 | -53.66396 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b67ccf5b-23a9-3222-b8b5-265702d9f338 | -2.6082 | -53.9942 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 575fb0cb-7167-303d-8202-f1580a68f86a | -3.07126 | -50.98767 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d8865e1-cead-3caa-9e3f-0c73e889147d | -2.78426 | -52.86658 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 928029f2-7b68-3217-bc1c-8807ee89d2cf | -2.62866 | -51.77544 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70a2f6d6-252c-3e11-9194-47c105351b2d | -3.26632 | -50.21402 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0e7688ba-0826-34f6-8363-b20d675c166e | -3.09196 | -53.29645 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92065907-53eb-3469-89f0-afe747ccce65 | -2.29257 | -47.99872 | 2024-12-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0129b33-c4a3-3be7-9e06-7d77161d42d5 | -3.26071 | -53.63615 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29f23570-2203-35eb-91cc-a440e1c512b3 | -3.22094 | -54.17452 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc2b0ab0-4136-3f0f-b7b5-e9586f605fdf | -2.54132 | -54.01138 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e1dba9b-fb46-3324-8956-f858772499fe | -4.34368 | -50.77177 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b8149ba-0ff1-3101-99eb-899e2c7dc825 | -2.35125 | -53.92852 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b9e748b-20cf-3b48-8fea-901ae87fb69a | -2.57506 | -53.67322 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e273d076-3437-3667-be23-5c10027d46b9 | -3.32876 | -50.21911 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac1d5c9b-d20d-308d-b61c-409e56518fe9 | -2.83327 | -54.03535 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e4690b7-63e4-3277-816b-26c557f78733 | -2.84784 | -54.03362 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e3b2a66-df5c-3232-8285-2d6944e1b652 | -2.62156 | -54.00014 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 024edfad-2d85-3c50-a71b-d933bc558aa0 | -3.11604 | -53.98869 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd1c3649-1695-3afe-8334-9a1cc2970338 | -1.70337 | -52.64699 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdb7cf3d-f6fe-385e-8aa3-35f3619742a8 | -1.39691 | -53.64187 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48e2ff50-6800-30f6-9d5c-7ca7ec02beed | -3.94524 | -51.09737 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 704c340f-fd90-3dfa-8c6e-df52a594c733 | -3.28802 | -53.28195 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b58235c6-02d5-3e81-b6e9-dbf405cb53f3 | -1.62582 | -53.86521 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa83bd7b-a74d-3670-b2b0-d85c9777083d | -3.79105 | -58.97752 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5793f8c-ad14-3f7c-afbd-c5c91dab69ce | -4.39993 | -50.69113 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af1b839f-5a4d-389e-a65c-9bb84e279733 | -3.79512 | -58.97426 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af544643-09d2-32ab-94a9-76e18c0227ca | -3.24698 | -53.8675 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2991cd5-b5e0-39d3-8651-107845b3a4cd | -3.257 | -53.29005 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10badd92-c51f-32a9-9593-8a7e63c48946 | -3.32862 | -50.21786 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b61121e9-97f9-3a9b-b751-6324716289d6 | -2.36104 | -53.65404 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 827751c0-100b-3999-a629-1901ef5b128e | -2.84374 | -54.03694 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df4dd4e-9465-34d6-bed2-c02e16ebba00 | -2.8357 | -52.91711 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e77be6da-3e76-35ac-842d-2797d3c56fa2 | -3.03412 | -54.04849 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba399400-9bfd-3c8e-a1c3-df28f670924c | -4.53546 | -45.69792 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c20c3686-46ea-3d0b-b288-b3a88789cd5d | -2.62904 | -54.21527 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc15a7d0-e9b7-3b96-9334-e000ff1598a1 | -3.09327 | -50.35066 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8058aea-5d40-3b04-818c-8ee198b86ab2 | -4.03461 | -46.93591 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 29c8e9f5-6a35-3ff2-a0a4-15597917f4e8 | -2.75692 | -54.09056 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 626ccd9d-c368-3a44-a933-0f35155532af | -2.44204 | -53.62177 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e4b5d8d-16ec-3adb-8902-206ed9ef59bc | -2.60547 | -54.07994 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff866c86-8db7-3a53-8a97-9cd69ac34887 | -4.01491 | -47.00046 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03e79244-bef3-3f28-a1e6-15125c8dc0c1 | -3.68829 | -51.82104 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b27ade5-2ca9-3454-a1c6-db5ac60ad957 | -1.43407 | -55.32909 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba95bdc3-f71c-3236-8c33-f9447d7a0c76 | -1.6254 | -52.7162 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72498ffa-1754-319a-abc3-99153c673f85 | -1.47662 | -55.38235 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c95fb9c7-047e-36dd-8bf1-8bbf9da79e4b | -1.25603 | -54.5525 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe92123c-a330-3d9a-aa78-126ef882bb79 | -3.76643 | -50.17323 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 038cd9af-4db7-3781-9422-81468b6c07bd | -1.62009 | -52.70215 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47078f70-37b4-3481-9d05-c157b5af5a50 | -2.69119 | -51.99428 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f9ad061-3e88-343f-8f18-4476417831ed | -3.45715 | -54.56875 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b061cced-15c0-3787-8909-e6d46169a558 | -3.10245 | -54.03031 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64e4ece4-3263-3d20-8119-7b543a95ea6b | -1.35063 | -52.82172 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6a70231-357c-3d03-b930-ed7694ebf0aa | -1.60294 | -52.29681 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6caf1e7-3b81-3872-9191-c2979082301c | -6.86611 | -47.24104 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5f3111-292f-36df-b5e3-d0802eed103e | -3.09501 | -53.72797 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aeb84499-e14e-3a74-84c4-40bdabfa7aac | -3.09164 | -54.12363 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3da8a99-01ab-384a-b4a8-7de8cd6cf8a3 | -3.09752 | -53.28436 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5152ea52-824c-3728-ac95-7d80e6ed623a | -2.79719 | -54.03774 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d360545a-fbd2-3683-a787-4b6189bd1dac | -2.98278 | -53.3491 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa91d1ef-969c-3f9f-96d9-9c10e105724e | -3.61915 | -51.53848 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a4969a0-d19b-3383-a271-8fd0c30a07b8 | -3.10784 | -53.99536 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fab34d1-6a95-3fec-93f7-607773f41ece | -2.77106 | -55.33522 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ecb328-bb95-3e39-a910-87c827cfa021 | -3.13417 | -54.52867 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 26eb5497-ecbd-3a44-97cb-ac743125d63b | -1.42073 | -55.30564 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 173f1396-484c-3403-bede-2c07657344e7 | -2.61067 | -51.81365 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0ced5f8-3f84-3999-8068-dc613c4ffd6a | -3.28886 | -53.2809 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 017efc1e-0677-330a-8ebc-64c18e7cf031 | -2.42073 | -53.89567 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 396a4a2a-ca7a-3e98-919b-22d4899856cb | -1.74397 | -52.6532 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca850ac2-c59d-3590-8f98-5d4dc41f8c8d | -4.2608 | -50.83922 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be0cce72-6122-34f2-81f4-58e337f8e75f | -3.32798 | -50.22219 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46d6e005-73ea-3088-a573-3d4f87e6fe4b | -3.33383 | -54.66459 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0a2d11f-6591-37bb-b99e-83037e915b9a | -4.31579 | -46.54298 | 2024-12-01 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README82.md)
