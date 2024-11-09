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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e42ed766-8d38-3ddd-8a87-6c027e4966c1 | -3.74603 | -51.95039 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec7010a1-5aaa-3edf-8459-fd93a5ce6538 | -3.92595 | -50.25034 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c68481f7-e253-30cb-a1a9-3f5a08bf49ff | -1.51045 | -52.16733 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f31e5ec4-62a8-320d-b2f5-594698e9fd09 | -2.89038 | -51.74954 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74f753b8-547c-3ae4-bf60-04736fa4bed4 | -3.17471 | -57.0865 | 2024-11-09 05:20:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 226dec21-1d2a-327f-990c-b6d4e7a4abc0 | -2.72982 | -51.72263 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 366b471b-bb84-33cb-b984-ca1b01774403 | -1.95845 | -53.06841 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25ee0381-97a7-3a1e-adee-e96da0c568d8 | -2.54352 | -47.12908 | 2024-11-09 05:20:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34bad593-f8d6-363a-8a3c-b0d52d1cee7b | -2.4647 | -50.40446 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a856877-8c30-39e4-ada0-2263f14da9ea | -0.18897 | -60.76978 | 2024-11-09 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c4b8a0b-f8c7-3631-a004-cfc17ddaa203 | -3.04481 | -50.37033 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3cddb9-a5a6-3c14-8704-79df9422ef65 | -1.14766 | -53.66599 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29e5f3cb-5ff0-356d-a94e-d82fef472cec | -3.83987 | -50.03537 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6666b404-1012-315a-9f1a-ad53539cdb23 | -2.28232 | -48.74539 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 608401c1-8fc1-34dd-aece-7efe4af600f2 | -3.02518 | -51.53231 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0487f3b-2427-3786-bcd2-f77018964069 | -3.53045 | -50.87412 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7afcc265-99fd-3e46-abf1-e9f6b32d5928 | -2.93575 | -51.05645 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d65c2c0-c977-35b7-982a-ece60bb55c12 | -2.67927 | -51.82244 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ede825c4-45bb-3114-b79b-3d661c952cae | -3.05048 | -53.27716 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26ed8c1e-2615-3648-9e26-9a4742403862 | -2.83676 | -51.80465 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a17d0de0-4402-308f-8f86-e555d7bf83bb | -3.25753 | -51.01707 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2bade24-ccb6-30a8-b018-a1d30382aa9a | -3.85147 | -51.24488 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 248991e9-6ad0-3a78-b671-987c7e2a2cf4 | -1.14048 | -53.65637 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 905f9c0b-2cff-33bb-817d-b1e0c7cbf6d5 | -2.2373 | -50.52455 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 304bee18-5c4c-3412-8189-46eb56f6c9da | -3.58334 | -50.27692 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34c0a26a-d429-3c35-992f-8a058e43d988 | -3.45 | -50.37857 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1fe25dc-4fb1-3620-8484-ef9f85c4ac4e | -1.34729 | -54.62402 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06229ab2-014e-3463-a3ac-820c20dedb9e | -2.87996 | -51.47923 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea1f90a-9b33-3a76-b165-e0050e626ab0 | -3.72912 | -53.40344 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f72380-84f8-338e-b459-51eca934885c | -3.01227 | -51.04223 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ce5ef9d-b9cf-395a-adbf-b08e8ed36418 | -0.0798 | -51.40804 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcdca938-79a6-3d1f-acfa-ce1612ca2475 | -3.92041 | -50.24939 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f4e06c8-762a-3785-a2f7-05fc729265ca | -3.0472 | -53.2781 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| caa9b4f4-4e7f-38ba-aaf8-ad74e1ee3862 | 0.67959 | -52.16343 | 2024-11-09 05:20:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12d18b5f-51e9-33b9-b696-d4f6d3aaccf5 | -3.16148 | -51.12547 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f32bcb-91cc-3c84-b3b1-c586d5bd2a41 | -2.58015 | -49.1321 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98dd3325-79bf-30f5-8500-74e368e380e3 | -3.02299 | -51.2297 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce951957-ae7e-3f21-93de-f3dc5184dd6d | -3.46355 | -53.82103 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11515af8-2a1c-3d8b-a46d-cfd3810b265e | -1.18362 | -51.9918 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b4729f2-8007-3161-8ca7-ff1318242dfa | -2.57888 | -49.14038 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1436e44-7fc8-3544-8292-bfb3c606aa6b | -3.66841 | -54.23653 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98b0b4ad-e197-3733-b775-92c17776e713 | -0.22438 | -51.63859 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 55dae81e-9daf-3bcf-bfc3-25c4019d3abf | -2.61936 | -51.3018 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2fe07e40-9bd9-37a4-a5e0-be1f3f159860 | -3.58924 | -50.27829 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 379fb161-b576-3210-8ef9-724d5708d58f | -2.05122 | -52.08837 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbe84adc-3bea-3641-9659-3b2bf94ab32b | -3.53092 | -50.32916 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46a5a2ee-e50d-3943-9f6d-404fc3cc715b | -4.89393 | -48.61231 | 2024-11-09 05:20:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3615b293-0d12-3a56-8192-e127c036dfe8 | -3.96962 | -48.18325 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8d1a6f8d-efd4-360f-a95c-584f939adc1e | -3.00832 | -53.44099 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb5b0b2-6536-330a-9baf-117c3b2db675 | -2.39835 | -50.31654 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18e84a5b-36a4-3b66-a144-b21fe37efc94 | -1.53783 | -54.30303 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38af3a73-dc56-3458-aafd-300b5731bc70 | -3.97525 | -48.18919 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 192235db-d159-3bd2-b1e3-3b0e912ad034 | -2.99667 | -49.24338 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| efcfce21-e95e-3984-b3ea-69d38b1a6747 | -3.2243 | -50.30513 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbe9c05a-5f61-355c-ab71-b385405baed1 | -1.18917 | -51.98741 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec17cd35-6da2-3040-8d8d-5f47def922b6 | -3.09861 | -53.32083 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ddc64e5d-7b3c-39ef-9dbb-ec0ccce39106 | -2.22375 | -46.5532 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032c098d-2432-3ced-b91f-c40ea5e728da | -2.67075 | -53.02212 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d0a2388-82b5-3d8d-92d1-02096a5ac4a3 | -2.57302 | -49.1395 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84b27d7a-c82c-3e64-9737-557100bb3781 | -4.05787 | -46.9429 | 2024-11-09 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edce4fc9-8061-3003-bfea-35cba1391bd5 | 1.32025 | -50.72694 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96bcdc54-e47c-37ec-9286-80c732c2934f | -2.36753 | -46.86404 | 2024-11-09 05:20:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 13a44621-36de-3fa5-bdcb-f6a00b0483fa | -3.27257 | -51.06179 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 654c1d70-0762-3d35-b498-04daf47e879e | -2.83429 | -51.80784 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c269738f-86e4-3cf8-8d0c-3ac6e09c94ea | -2.24693 | -53.77314 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c85557b-1d4c-3c89-83a7-077a87a1e7ac | -3.11764 | -50.15127 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d022479d-5c8e-3f8f-a344-fd8459e046ea | -4.86248 | -48.11628 | 2024-11-09 05:20:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb7a42d-0799-3a16-8ced-7d4b446450f7 | -1.03416 | -53.73067 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e246131c-b888-3cef-b762-c5edd2d7de12 | -2.2257 | -46.5441 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c869cc8-fbd3-3290-ab73-e7dd1966104c | -3.12533 | -51.10941 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 593f1c58-639d-3fe8-90bf-c4aa8516b9d7 | -3.23045 | -50.45024 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90a0a282-3ee1-33ed-aacf-bee962d07204 | -2.77764 | -52.86949 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1040085-b263-39dd-8298-e954b468cf38 | -0.19292 | -60.76669 | 2024-11-09 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15185db2-6ade-36c7-bf29-5c9572223e7a | -2.8752 | -50.41645 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da426348-c104-3e90-829b-0ca7ebf43490 | -4.39952 | -49.41555 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8578d443-db15-3f58-af97-ec77c3c01fee | -2.18531 | -53.64169 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70785d9d-59d6-3d9b-8b36-b7fd4539c77d | -1.33745 | -54.60865 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd1c5f2b-9e56-33e4-a6e6-7dddf863ae52 | -2.39942 | -50.30962 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c974c916-7856-3d31-8320-0399c16a5d2e | -3.8202 | -49.85515 | 2024-11-09 05:20:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc29ab45-e505-3ccc-9dde-0e2a174b1d28 | -3.15676 | -51.12151 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8895b0ec-c60b-30c9-a843-f7b13b712f4f | -1.2173 | -52.94247 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f83de4c-9fb4-3933-b364-a429e94673ee | -3.83931 | -50.03912 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa2b195c-6568-30b1-99d8-6fd809950b5c | -4.60122 | -49.5808 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c32a65e6-8462-3ac4-a6fd-b7b15457d05e | -3.28335 | -53.6733 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53608f11-34d0-33fb-982a-914234efaf44 | -4.11031 | -48.50318 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1631f39c-d5e7-371a-a11b-5547293c10e7 | -1.83052 | -53.72561 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa4a00b3-90a1-3a19-8b1a-db31381022d9 | -3.27052 | -52.73999 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8eb25728-3019-3b32-b91f-fa80f4824072 | -2.19087 | -53.63418 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cd215e6-3ffb-3a4b-a785-6bd7bccc9e81 | -2.2927 | -48.55374 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e7d146f-4ab6-3302-9023-3a6787945006 | -3.03384 | -53.276 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8e318e7-495d-30d0-8ee5-633848a769bb | -2.92537 | -49.36014 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 774db262-8573-3685-b094-bef602fdc90e | -2.80968 | -51.80412 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b969b690-2f0d-3e62-9b7c-4bec790b1599 | -2.45399 | -53.68815 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9617c359-4a26-390d-ad8c-225f4d3c0a93 | -2.71477 | -47.73171 | 2024-11-09 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 383d024d-7c8b-3ae2-bd33-10e41290afe2 | -1.42507 | -53.90915 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec6b184-8b03-3f3d-bd8a-bb05d26c71c9 | -3.76105 | -51.02193 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9741e34f-b6cb-3cb4-b12b-43995730b3ce | -3.03989 | -50.36604 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a2f2d6e-66ca-3afd-a053-9b29d2309d5c | -3.75111 | -52.40433 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76c5b888-045d-3cab-96e5-31e7869efa46 | -3.58424 | -50.27394 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72ea5f32-e4cb-3590-9fd7-600a40ae9041 | -3.75881 | -51.7625 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README103.md)
