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
| 4e293174-e4d0-3c2e-8772-45c25a3fe78b | -3.5491 | -54.7351 | 2024-10-23 00:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 0691ce5b-4bb6-3f9a-83e3-4316a2d64abd | -3.7254 | -41.6987 | 2024-10-23 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 6b72b3a1-ff42-33ed-ae5c-773717a78807 | -3.7255 | -41.6748 | 2024-10-23 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 26f93059-1ece-370a-9cc9-7ba6c8af22d4 | -4.1719 | -47.9894 | 2024-10-23 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5c45c776-a685-3a71-8795-838e4b2065f6 | -4.6775 | -44.6089 | 2024-10-23 00:55:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 797bb556-6b34-378d-8829-d4790c249d14 | -4.7254 | -45.7363 | 2024-10-23 00:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| dec009d6-de17-336c-8381-3a240c7583ea | -5.2305 | -43.1886 | 2024-10-23 00:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 003ed4a6-1654-3777-9e55-ee7e538744b5 | -5.5671 | -43.2576 | 2024-10-23 00:55:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3a5cfd0e-9293-3bf1-b7cb-b1ba530bd2f6 | -5.5858 | -43.2562 | 2024-10-23 00:55:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 18bb9c60-ebbb-3fbb-bf61-0705e911547e | -6.6765 | -43.0491 | 2024-10-23 00:55:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 27b1281f-f609-3744-a53f-0d6747eaa190 | -7.1801 | -45.1285 | 2024-10-23 00:55:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 9b71aa58-966f-3d2f-8d1a-91fa12b40519 | -10.6725 | -58.749 | 2024-10-23 00:56:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7ad5a66c-47b1-3294-aae7-609cb2b73a0f | -11.3217 | -54.3564 | 2024-10-23 00:56:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| bcdb7caf-60a4-3fcc-b458-11bb79555c40 | -11.3406 | -54.3547 | 2024-10-23 00:56:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9d238013-748b-3f25-b851-58bee6dc724e | -11.8261 | -47.0832 | 2024-10-23 00:56:13 | GOES-16 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 143e99e0-293a-3e84-b1b4-bad3585536ba | -11.8265 | -47.0607 | 2024-10-23 00:56:13 | GOES-16 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| f7d54607-0328-3daa-9a6b-e0637ef25f7d | -17.6865 | -57.4798 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 1600d2c2-ef7b-3aeb-980b-7828282206ef | -17.6868 | -57.4593 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| e659754a-840a-3df0-aba3-162664623fe5 | -17.7065 | -57.4569 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 9f140b9e-6d79-3f42-8721-b81d3bd66657 | -17.744 | -57.5756 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| ca03b59e-6c2f-36d2-ad67-96c7d22335bf | -17.7637 | -57.5732 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.4 |
| 43ec02a0-707a-3857-9eb4-5d1972fe7b20 | -17.764 | -57.5526 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.9 |
| df9094db-1559-325c-a00f-8e60ab4d9fc7 | -17.7644 | -57.532 | 2024-10-23 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 6289faeb-4a06-38f4-ac15-eea7c6a88f43 | -1.3879 | -52.0072 | 2024-10-23 01:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b25fd522-7933-39cf-aecb-b73de691eb9f | -1.388 | -51.9867 | 2024-10-23 01:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| f0bfbef9-98c5-336e-8fdf-f29cce071aa1 | -2.5225 | -54.0992 | 2024-10-23 01:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6e9ec619-ca60-3765-a4c9-7ef20a7ac1cf | -2.7589 | -49.3072 | 2024-10-23 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0e604095-6ca0-305c-a959-4bb053bc9b7d | -3.109 | -45.3194 | 2024-10-23 01:05:24 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3b0ed589-940c-34c1-bfec-54e0aab85627 | -3.1091 | -45.2968 | 2024-10-23 01:05:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 126.0 |
| f24401eb-fa72-356c-b561-243bfbb498dc | -3.0917 | -54.1666 | 2024-10-23 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ab7c949f-edd8-3d3c-9988-b6b4d7c2f1a8 | -3.0918 | -54.1465 | 2024-10-23 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cc1a79f2-b240-3aee-bbfe-809a45bc540d | -3.1276 | -45.3186 | 2024-10-23 01:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3f0786cc-cb4d-3500-b775-58af5cd3e612 | -3.1277 | -45.2961 | 2024-10-23 01:05:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 0ab2979b-0f94-31c2-9d16-980915a82d63 | -3.1101 | -54.1661 | 2024-10-23 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 4348b163-224b-3064-8bf4-717194517ac6 | -3.1102 | -54.146 | 2024-10-23 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 98903568-9730-3ae9-b818-a75d6a08c226 | -3.5307 | -54.7356 | 2024-10-23 01:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9e754e53-4d40-3648-9ed0-826803d9eebc | -3.5491 | -54.7351 | 2024-10-23 01:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 77787c6c-ac26-35f4-af13-8674afdd4325 | -3.7255 | -41.6748 | 2024-10-23 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 423e3384-1003-3cab-ac8b-af7f66f52f23 | -4.0052 | -44.7596 | 2024-10-23 01:05:29 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8c7c0a7a-90e5-30f8-8096-f10ccb71237b | -4.1719 | -47.9894 | 2024-10-23 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0108cbd2-49aa-38d9-80bc-335cd93f793e | -4.6775 | -44.6089 | 2024-10-23 01:05:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 65e59fc5-06a6-38f4-8ea9-5dd708b7df45 | -4.7254 | -45.7363 | 2024-10-23 01:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cdb3474d-d7be-388c-92f4-019a48159979 | -5.2305 | -43.1886 | 2024-10-23 01:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cd14cf5c-38fd-38a6-964d-eaed68dfe8ac | -5.5671 | -43.2576 | 2024-10-23 01:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 02553f19-118a-3271-a62c-d51ccb1d4c19 | -5.5858 | -43.2562 | 2024-10-23 01:05:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c07791a3-f245-38f0-8803-49fd33f80427 | -6.6765 | -43.0491 | 2024-10-23 01:05:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8d051159-d255-3b3e-9ac3-03f9fa605f53 | -7.1801 | -45.1285 | 2024-10-23 01:05:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| eb854945-e269-3ae7-8142-5603ae5c868e | -10.6725 | -58.749 | 2024-10-23 01:06:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4ad13815-f671-333e-8cfe-ad15d86d41c1 | -11.3409 | -54.3342 | 2024-10-23 01:06:11 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 00dfcc1f-bf47-3ef0-8d61-f46d65162a04 | -11.3406 | -54.3547 | 2024-10-23 01:06:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c9606857-e385-36ba-b8ca-b27e1ffe6b03 | -17.764 | -57.5526 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 73d552e4-18ff-351c-a271-949fcd613efd | -17.6671 | -57.4616 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| aeda274c-caab-35a5-b2d8-138c308e7427 | -17.6674 | -57.4411 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 36ba5c44-8a85-303f-b5cc-13bd7df71692 | -17.6865 | -57.4798 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| aa9b2803-acb4-3d70-bf1d-fdbd496c9515 | -17.6868 | -57.4593 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.7 |
| f9409f44-4005-325e-9465-b476ff3f28b1 | -17.6871 | -57.4387 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 3116de88-2bf6-38b4-8c6a-edab3f6f38ec | -17.7062 | -57.4774 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| fbd88b63-5b31-3344-b986-a1ad532ba5f6 | -17.7436 | -57.5961 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| a881e73e-6349-3169-8c25-b5d9ad290956 | -17.744 | -57.5756 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 173.3 |
| 08f4fbea-39a2-333b-8b49-20c8f6540792 | -17.7634 | -57.5937 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| b505ca94-29fe-3832-af14-f27ac18d053b | -17.7637 | -57.5732 | 2024-10-23 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 215.5 |
| cdbc7e32-cd96-3f6a-94d5-05a5bdda32e7 | -1.3879 | -52.0072 | 2024-10-23 01:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 664d9e30-37c4-3e6f-977a-9d290620a967 | -1.388 | -51.9867 | 2024-10-23 01:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| faf64f5e-c88c-3ea8-aec6-d91318947927 | -1.4063 | -51.9864 | 2024-10-23 01:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 38134085-b640-317a-b18d-8e6b5300732b | -1.6931 | -47.0686 | 2024-10-23 01:15:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 39f93224-ba19-367b-b89d-6f10999d48dd | -2.5225 | -54.0992 | 2024-10-23 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 86953651-291d-37f1-89a5-342b4053f0e6 | -3.109 | -45.3194 | 2024-10-23 01:15:24 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 07bd6288-06aa-3c2e-8bee-fead2d46ec1c | -3.1091 | -45.2968 | 2024-10-23 01:15:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 761c448d-d439-35c1-a44e-785466d34fcc | -3.0917 | -54.1666 | 2024-10-23 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 293767c2-e287-3f1c-b822-4568700b5e51 | -3.0918 | -54.1465 | 2024-10-23 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d28658c1-d2ac-34db-83d6-18cfb88425a8 | -3.1276 | -45.3186 | 2024-10-23 01:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 590573f0-517f-3979-8842-4b3273d28da2 | -3.1277 | -45.2961 | 2024-10-23 01:15:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6b7f38e9-0fec-3eb4-ad53-d276a15098f6 | -3.1101 | -54.1661 | 2024-10-23 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 85e2a42d-1c85-3cb4-a0d3-854ad3aee020 | -3.1102 | -54.146 | 2024-10-23 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 16867cf1-5e4d-31e0-928a-7775b56e438e | -3.5307 | -54.7356 | 2024-10-23 01:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| eeee1e79-4dce-3f25-a4db-8df89a9adad8 | -3.5491 | -54.7351 | 2024-10-23 01:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a6536c04-7377-3810-8e8f-a2753a91d550 | -3.7255 | -41.6748 | 2024-10-23 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 86059e36-397d-349d-92d1-f9d1e43fa985 | -4.1719 | -47.9894 | 2024-10-23 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 717fe660-ba53-3eea-8dc3-3b469cca1df0 | -4.6775 | -44.6089 | 2024-10-23 01:15:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2c5a3181-6b12-3576-bf80-a42a7988f95e | -5.5671 | -43.2576 | 2024-10-23 01:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7dc1ede3-6052-3a33-a34a-0a9b6352a4df | -5.5858 | -43.2562 | 2024-10-23 01:15:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0739a62b-a8b6-3365-93c9-a0db45f7475a | -6.6765 | -43.0491 | 2024-10-23 01:15:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| df0810a0-1df6-35c3-9077-98cbbb5c7878 | -7.1801 | -45.1285 | 2024-10-23 01:15:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 547c2af7-d5c6-3d8c-b2e6-b393439a1817 | -10.6725 | -58.749 | 2024-10-23 01:16:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e352c380-fe9a-332f-872e-5d85f5c1883b | -11.3406 | -54.3547 | 2024-10-23 01:16:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c48e2cad-8484-378f-b00e-4002e5fcc57a | -19.5477 | -56.6353 | 2024-10-23 01:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 9ab32a9b-aa54-328c-9dfa-adb331a6b6aa | -19.548 | -56.6143 | 2024-10-23 01:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 2004bf37-28fa-3f93-89b8-746f3812835d | -19.5677 | -56.6324 | 2024-10-23 01:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| c976da68-c30e-3d1d-958c-94ff85f32e41 | -19.5681 | -56.6114 | 2024-10-23 01:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 50927e1d-f91a-33ef-9bc9-72ca8b61ebc8 | -1.3879 | -52.0072 | 2024-10-23 01:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f5e2877d-8031-397a-89f6-4aaa0111c5ec | -1.388 | -51.9867 | 2024-10-23 01:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f9dbdff8-4eec-3526-9566-1d1185b84e76 | -3.1091 | -45.2968 | 2024-10-23 01:25:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 45c1535a-b2d9-3722-b907-01b1584e6bb5 | -3.0917 | -54.1666 | 2024-10-23 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a53e8766-6459-37b1-a336-e75c489c2dcb | -3.0918 | -54.1465 | 2024-10-23 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ac33a998-ab89-3a30-b29a-f2269166ddea | -3.1276 | -45.3186 | 2024-10-23 01:25:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 06aa3582-0df6-3f0e-9b16-d734aa647249 | -3.1277 | -45.2961 | 2024-10-23 01:25:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 6579083f-aaa1-3547-aae6-9f6f0b8828d9 | -3.1101 | -54.1661 | 2024-10-23 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 697ddcc0-b0cc-3d79-953e-ff62adbc6dfc | -3.1102 | -54.146 | 2024-10-23 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f49bc1ac-9fbf-32a3-a56f-9d3433edc6bb | -3.5307 | -54.7356 | 2024-10-23 01:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e440dba9-411d-32d7-87dc-d62fb111f4a5 | -3.5491 | -54.7351 | 2024-10-23 01:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README10.md)
