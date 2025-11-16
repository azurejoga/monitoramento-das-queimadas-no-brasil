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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 927cc62f-5b96-3655-92bf-98b4462c22d4 | -3.01351 | -49.4343 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c272c66f-d4cc-35f4-ae79-8c0ab23d10a9 | -4.01673 | -48.80841 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9dfd33a-c299-3945-8773-1727909bd148 | -4.41413 | -43.40679 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b66c2a9-9617-3d4a-addf-b43ddf744aec | -3.54973 | -55.49184 | 2025-11-16 04:55:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca0e7b6-c5ac-3e49-9906-bdc538298c5b | -3.08111 | -52.92082 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5eaf9083-5ef1-3ebf-a7c6-571692dc6a44 | 0.17281 | -51.29371 | 2025-11-16 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34047a06-fffb-329c-a573-ff1a80e1feb2 | -1.64407 | -53.66632 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1750e24-f9e7-3c14-b54f-d48ee476595e | -3.53067 | -50.87347 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c862b83a-1cbf-3afb-9183-9ed4453070e1 | -4.00204 | -44.27184 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83928f5d-2be9-366b-8f54-de3957a47abf | -3.02432 | -51.60677 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0abd30c6-7d26-3faa-8eb6-91bc28bddcaf | -4.15407 | -50.22673 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3481a49c-f6b0-307c-9fdf-51aa1bcab0f0 | -5.47455 | -40.96383 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d2b1e848-fb51-34dc-8d19-a3835c12c1f7 | -1.33999 | -54.60711 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61627d53-bcfd-3e07-a344-9a43fe4ab3ff | -4.0031 | -49.88852 | 2025-11-16 04:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| adec88ae-5555-3440-b5ea-5212b70495a7 | -2.86936 | -51.47852 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44a30ab6-a64d-3b8a-abd0-bdf61029687a | -5.48578 | -44.83974 | 2025-11-16 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae88a3ec-bd95-3dc2-be3d-dbc45ed47a47 | -2.13891 | -56.68327 | 2025-11-16 04:55:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa889aa7-9743-3789-9727-a51d74ada9e6 | -2.95339 | -48.59224 | 2025-11-16 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f15f336-e779-3dbe-9b48-7f8da1fbedcd | -5.00157 | -49.66393 | 2025-11-16 04:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e974b2c-d014-3cbb-ab82-1e60bacd261c | -2.52032 | -47.8119 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3488c8e-2595-3bf0-8762-9f622767b6e5 | -5.73231 | -42.7312 | 2025-11-16 04:55:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 171f7ddc-bd15-3b73-a486-89a854611364 | -4.94021 | -44.53464 | 2025-11-16 04:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5468f71-e632-3518-a13b-02889d29a0f2 | -2.58703 | -51.83123 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b259840d-a088-3006-b3f5-2f532f9ca7c0 | -2.54921 | -47.45695 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72fb3385-c23d-34f3-b6d5-aa47382af87f | -2.73771 | -53.20103 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8db3ca51-96db-32a8-9bf6-9ecf98d67d47 | -4.41357 | -43.41078 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ad0aae1-43c5-32b2-868e-2413bd59f74f | -1.35013 | -54.60873 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01038b23-39f7-338e-adae-4911f6d9096a | -5.45415 | -47.0099 | 2025-11-16 04:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 023c5b6e-2531-320e-b298-5e4efee9e7da | -3.38395 | -47.18941 | 2025-11-16 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dbf6ba3-a138-3c2a-83f5-c717802e5805 | -1.19545 | -53.72726 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c32225e2-ae99-389a-aa92-ffc3fa6ebb54 | -2.89154 | -53.28535 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2625ffb7-707a-3554-b290-fa7582ef4f72 | -3.54689 | -55.48763 | 2025-11-16 04:55:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d4e96c7-486c-364d-8b7b-470fb150029c | -3.73541 | -51.32339 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1914ed4-7bac-3774-a311-1b5ec53fd9df | -4.81036 | -48.33965 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 049f8436-f85e-3869-a8a5-00ee09c169dd | -3.20633 | -51.58949 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5637dfc-60ee-3906-adf1-064fb41b1cd7 | -4.69494 | -46.31956 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1157905d-a20f-326a-b926-e61c8222c9f0 | -3.60502 | -54.67547 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d419018-54e1-36c0-b52e-763279e76339 | -2.7174 | -47.40252 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 278f13d3-67d1-35c3-848f-0cd445eebf93 | -3.19919 | -53.01319 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8beada60-e16e-36d5-aead-d640c19a0b41 | -2.68825 | -49.0756 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a13858a8-719b-3a98-9c55-47adaefee5eb | -3.99873 | -49.89238 | 2025-11-16 04:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0ba6bc77-304e-30a8-b936-5de6a4971086 | -4.49974 | -50.78994 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d5b6cd3-aaf9-3b2d-afe5-c5a07d24a188 | -5.42565 | -43.26329 | 2025-11-16 04:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 120812d5-8ee3-3ed8-a6d1-adb8e119c677 | -4.25824 | -55.71648 | 2025-11-16 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9b0c81d-725b-3db1-b9db-a91bd9cf1681 | -2.52388 | -47.81621 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 024ae764-7175-3676-b933-31477f448bf5 | -3.37855 | -50.13218 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 197068da-c29f-3a65-837e-6bcd8a4a9c3f | -4.49913 | -50.79396 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0387e469-9bf0-3194-8af4-ae05a7b3beb7 | -4.7444 | -46.37846 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 90323b30-37c5-3052-93bd-a949870203bb | 1.33919 | -51.11645 | 2025-11-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 44905e1a-6ebd-3b3d-9ecc-112b6ed916f8 | -3.40843 | -46.90496 | 2025-11-16 04:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6dfa4d6-39cf-3789-ae10-388b003d8ea1 | -2.91959 | -52.51648 | 2025-11-16 04:55:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be3a6645-524b-33ae-8f88-8d8e97606894 | -3.20689 | -51.58583 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07a99864-372d-3acf-966e-d8ed0c2fbfa2 | -4.62556 | -47.40632 | 2025-11-16 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef8e3423-83d9-35f8-aaf1-1c35ee0815a8 | -1.78147 | -55.93201 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfcf04de-adf8-35c4-abfc-b0606283c72b | -5.23923 | -44.34466 | 2025-11-16 04:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 516d6792-96a8-30e6-89c7-072cf35bf53f | -4.74366 | -46.38359 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fd39039e-a969-35bb-b856-42d2e926ba20 | -3.89271 | -47.18678 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88489a7b-f2c3-322f-8807-c83992e49265 | -3.03132 | -54.60048 | 2025-11-16 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7392f925-348a-3e04-a6eb-3f1a1568e3d8 | -3.78781 | -47.47471 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59791a03-e17d-306a-848c-8b2d0c48dc27 | -4.29597 | -49.74916 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6359fe8-f173-3a60-b0ab-1ad9853c5b73 | -3.45466 | -51.02045 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 601e414b-20d5-3f08-8b27-4f1d6ac77773 | -4.69018 | -46.52195 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1edacb74-4ccb-39ea-b525-71883869b057 | -4.6755 | -50.36819 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cb4f2e8-616e-35c7-85ee-338eacadddb6 | -4.49374 | -47.65258 | 2025-11-16 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03c81810-3ec5-3662-80b1-f2050dcd475c | -3.40752 | -52.72432 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e38dfc-4c02-3ab4-affa-2ccd6c963dc1 | -5.62945 | -43.92903 | 2025-11-16 04:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 360836bb-4bfd-3319-aa0a-7e3ce81c9c66 | -4.69636 | -46.30951 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c3ad5b72-efc1-337b-ae66-90bf7031d20b | -2.57987 | -51.87759 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 012bdc1b-d088-3767-8041-6ef311badb1a | -2.52331 | -47.81992 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| b92883c7-92c5-339b-8209-8d7ccceb9547 | -4.00305 | -44.26499 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbf06b2f-fa34-3602-81b4-630439781dbd | -3.95592 | -44.84744 | 2025-11-16 04:55:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c42ceb6-9fa9-3566-b6a8-0196a077d676 | -4.3137 | -50.87038 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2496e697-0331-3b88-9e57-125dda73bbb8 | -3.93127 | -47.05077 | 2025-11-16 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 7938e5fc-9329-3ef7-b714-920eff8fd00a | -2.88693 | -51.43235 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab770813-6f01-3ec0-9b8e-e3d30a35ab07 | -5.42033 | -43.25846 | 2025-11-16 04:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9fef550-f112-39a1-8ffb-a52e0eb95753 | 1.99566 | -50.88013 | 2025-11-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a673b1bf-2d3e-30e1-a67c-733fe9308510 | -3.26993 | -50.77584 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cecbc6e-2d7c-371a-a9c7-1afbad5d576b | -3.39006 | -50.12967 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2bf7a90-512b-33f9-bc45-6ac14275900c | -3.39629 | -50.18658 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafd4726-9ace-3892-b89e-24a9ace937a1 | -3.78841 | -47.4706 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1189ddb3-aca2-3945-ab76-5ae96c380e44 | -3.08714 | -51.04516 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 341ed436-d907-328e-84ba-3a4dd7f42d10 | -2.86167 | -51.27706 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265bf6b6-a5ed-3896-937d-cd493df2a61e | -3.22673 | -50.06879 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ee94846-cfd8-3d9e-a39d-9fda9618444e | -2.42617 | -45.71338 | 2025-11-16 04:55:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fdfff66-06cb-3174-b857-9cd06e85c71c | -3.03075 | -54.60404 | 2025-11-16 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1421b37a-3fe5-317e-b0eb-747a957c3a77 | -1.32253 | -54.22015 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a698075-348e-311f-8079-304a91aae3f8 | -5.45601 | -46.43747 | 2025-11-16 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8326c37-79d6-3a37-be65-bb7f05384bbc | -5.4687 | -40.97274 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9a65a794-b0f4-3abd-aab0-8c9aac973774 | -3.57768 | -50.42293 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 286b0dda-1314-34fa-89ab-2a02bbfc3e2a | 1.61566 | -55.81621 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8c37cbe-a0ca-3526-95f7-d84a78f48537 | -1.22393 | -55.83322 | 2025-11-16 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86aea280-b8fc-38e7-9daa-33965797fcec | -5.49135 | -46.91714 | 2025-11-16 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe4ffe77-4fce-37db-8b76-8e537ce40492 | -2.86708 | -51.47065 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e79ffa8-27b1-3369-b831-f76a21e187f5 | -2.58422 | -51.82714 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a705ac0-a580-3e49-90a1-cd33b579b8bb | -1.18057 | -53.58245 | 2025-11-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50caf3b7-1052-38cd-bf99-059cfdb58167 | -4.74914 | -46.37901 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b63bac4-4319-3d79-a017-24a755221332 | -3.57829 | -50.41887 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88ef526b-0a5f-3fbc-925a-890f8a048179 | -4.42186 | -45.56301 | 2025-11-16 04:55:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ec38a8a-fc88-3289-9c44-464daa6dfcbf | -5.23277 | -44.35098 | 2025-11-16 04:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0451c229-7acb-3244-a098-94061d06277b | -1.99425 | -47.34808 | 2025-11-16 04:55:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README49.md)
