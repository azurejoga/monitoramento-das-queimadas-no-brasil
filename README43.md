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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23d4e48b-66a4-3b7d-aeb6-75e6ec92cac0 | -3.05538 | -47.99615 | 2024-11-18 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a5f374-8e53-379d-95aa-11c4178ffb53 | -3.59178 | -53.78204 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c73fc1-f44b-39ac-a828-789935ddc218 | -3.31471 | -54.17264 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11e9f588-af1a-3fd1-b6f4-e76e08065378 | -3.68872 | -50.11039 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e26643d2-58ec-3b13-b65d-5e2ff88969f9 | -3.31083 | -53.36382 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1bb7c5e7-16f7-3a52-8176-4ea85bc764f8 | -3.13851 | -52.98209 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d97dae1c-a428-3de7-aa74-38e7076252bd | -3.3452 | -50.4917 | 2024-11-18 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 05c95713-fe8f-3d82-b68d-1690ee1a151b | -3.5678 | -50.2534 | 2024-11-18 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 660612fa-6e51-30b5-b964-f77da2148435 | -1.3148 | -51.7408 | 2024-11-18 05:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d1701383-9ae8-3207-9072-cd7286d5ef43 | -1.2964 | -51.741 | 2024-11-18 05:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5669143b-5599-3064-9b07-53eaee46f0a5 | -17.08673 | -57.47306 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0dc93aa2-694b-34dc-bc8d-08bb7c90a247 | -17.11748 | -57.48689 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aefa60d0-340a-3d69-9496-20587bc3f519 | -15.65661 | -59.84419 | 2024-11-18 05:31:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 532860dc-87b8-3dbf-b95c-fa5f08cfe186 | -16.07508 | -60.09642 | 2024-11-18 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afda4942-89bf-343a-a8f1-1a33d2c2375d | -11.37216 | -55.12605 | 2024-11-18 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 69aa1444-b8c2-3ca7-a30a-48375ef05cd6 | -17.11293 | -57.48628 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e8b720c8-28d0-3004-a6da-719d3b2bd57d | -15.6521 | -59.84849 | 2024-11-18 05:31:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e62329e-6c37-34d7-90d1-8e5dad065158 | -17.10779 | -57.49043 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8932195a-b9c5-3f77-a2ff-4fbb2e409945 | -17.09129 | -57.47367 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cddb03da-cbc9-3b27-bb92-37855ac2f9a4 | -17.61759 | -57.56792 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7c3b42fb-2df4-3b7d-a19d-4a11627310ef | -17.08616 | -57.47783 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e40c5227-d620-33c4-baa4-a47909224b24 | -17.61188 | -57.5769 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3080cf52-8904-3928-a3cb-3756c7f57032 | -17.10837 | -57.48566 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10fef1e7-d913-3328-a44c-4d82eed0b891 | -16.08649 | -60.09812 | 2024-11-18 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a608608b-a92a-360b-9b7b-5fc68d4e848b | -17.3598 | -57.44061 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9ae43694-9c73-36b1-b39e-9bbf51c84d63 | -15.15904 | -59.72634 | 2024-11-18 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35abe926-3170-338d-9192-7d82e848fb49 | -17.61245 | -57.5721 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 49160c63-e36d-3a5b-bcb4-7955a851cf0e | -17.11235 | -57.49105 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d9ddbc5b-55b0-3419-bbd0-dd8e6051b3a0 | -17.1169 | -57.49166 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 536f6dad-b870-3b7f-8e84-322d3c80aa61 | -17.621 | -57.57812 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 02b4d02e-fa62-3d67-9201-e40ceb5ca286 | -17.61701 | -57.57272 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 54b9be2f-9c7b-3101-b3d2-f9140156b9d1 | -17.61303 | -57.5673 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2797c582-125d-3cce-9e50-57d86098d4a6 | -17.61644 | -57.57751 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 53efbf24-c6d8-321a-b529-39592efbe1c4 | -17.62158 | -57.57333 | 2024-11-18 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b445f3b5-cd72-338c-93ed-189a43160f2a | -16.09743 | -60.09685 | 2024-11-18 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e368afc-224e-324c-8c9e-75e779210eae | -17.09187 | -57.46889 | 2024-11-18 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 42962b35-ae72-39a6-8423-0ed6abc59f59 | -10.35937 | -56.35084 | 2024-11-18 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e46f318-021e-3b84-b4be-1a4521b069fc | -16.08269 | -60.09756 | 2024-11-18 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a4258e2-cdf9-3a65-8716-94eb30258d78 | -1.3148 | -51.7408 | 2024-11-18 05:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 078e6e87-3e19-3a7f-9e03-f20a903e3bbe | -1.2964 | -51.741 | 2024-11-18 05:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| fdf1085a-9c9b-3495-a3a8-88061eabf7f5 | -1.2964 | -51.741 | 2024-11-18 05:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 21bcc47a-d13b-3de1-91c1-ed5cc4f887ee | 2.67634 | -61.17546 | 2024-11-18 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1bb434ab-3e99-39f8-bb00-36c121eeebc2 | 2.23874 | -55.82989 | 2024-11-18 05:50:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 383b9bc3-635c-3a14-8194-811970e80ab4 | 1.18016 | -60.22247 | 2024-11-18 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d8c7bd8-5d45-3b2a-810f-db5c30cd5cf5 | -3.07865 | -54.66568 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a37ef326-c0e0-31d7-914b-1b96aeadaf98 | -3.06004 | -54.40396 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32675ec1-869e-34f3-a76a-f0fa72c5e63f | -3.08415 | -54.6679 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7480e3b3-c920-3c6d-adc3-f3cb78560f45 | -2.5244 | -54.8839 | 2024-11-18 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10e8be91-d6ab-3e48-98d8-51a5ed44c812 | -3.0521 | -54.40972 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c393a7d1-6faa-3b49-9fa0-aea3e9cd2859 | -1.21041 | -55.8242 | 2024-11-18 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45438e05-ba34-3b86-bd4d-b2ca3ce980cd | -1.62311 | -55.14801 | 2024-11-18 05:52:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5414638-096a-3287-baab-7d9278b3e514 | -1.6239 | -55.14698 | 2024-11-18 05:52:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 630f438b-4461-3d6d-914b-65d3d2c6813b | -2.522 | -54.87979 | 2024-11-18 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c34fd11-1a55-3af0-9a65-c3e205465a76 | -3.0392 | -54.40082 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5668e2e9-b0c5-388a-8ba8-a6cd2a2d7eda | -3.04619 | -54.40161 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 979d5c7a-4247-3305-aa35-61a35e818b12 | -3.04522 | -54.4082 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38eb27db-3749-3fe5-bb3d-f6ce9c22e480 | -3.05901 | -54.41097 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9135ea97-a44e-3a5a-b74d-e6099ab35f50 | -3.03827 | -54.40723 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26945872-f82c-3bb6-a5bb-e0ca27e70856 | -2.52112 | -54.88554 | 2024-11-18 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e48da53c-e3c6-3ff2-9566-119b8ce1ad24 | -2.42657 | -54.62767 | 2024-11-18 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca1422da-d436-3abc-b957-058f5c72ab83 | -3.16025 | -67.99857 | 2024-11-18 05:52:00 | NOAA-20 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3da7510-c9ef-35ca-addf-a4d3bbcf9087 | -3.50376 | -54.03529 | 2024-11-18 05:52:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61ef87c4-fecf-31cb-844f-e48f3114ec0e | -3.0855 | -54.66665 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc2b0dba-1eb2-3dd4-a0d4-c7084b66c0f8 | -1.21115 | -55.81951 | 2024-11-18 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 541921db-ed05-32e0-a075-581f5da6b14e | -3.05309 | -54.4029 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45d85ad0-d4ed-3e2d-884e-12233141d04c | -3.07731 | -54.66688 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f69987b1-c7ea-3279-b25f-1b1f11619d9e | -1.62305 | -55.15247 | 2024-11-18 05:52:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5481a261-ebcc-3fd1-a5e9-60997130faf4 | -3.08509 | -54.66168 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 023eb2d7-27d3-305d-a5d0-3aef26cb476e | -3.08641 | -54.66032 | 2024-11-18 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fb17e85-bdde-32aa-9657-e866c52102ef | -0.1841 | -60.68391 | 2024-11-18 05:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 839ca4f3-e922-3d95-9916-346962e6f090 | -8.68584 | -67.04029 | 2024-11-18 05:54:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 057e2624-8b8d-3019-a0ac-1b6c9b65480a | -13.01871 | -56.45825 | 2024-11-18 05:54:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f799f76d-5b57-3b1c-a9bb-7e126d486a11 | -13.01801 | -56.46484 | 2024-11-18 05:54:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2981beec-a9ee-3cae-8b6b-d7b7a9df9dcd | -12.55219 | -57.8278 | 2024-11-18 05:54:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69a4dd1f-5641-30ba-8e1f-740fc283124f | -14.64772 | -59.62357 | 2024-11-18 05:57:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e35b2d7b-5d47-33f8-aee7-847a79da1275 | -17.61543 | -57.57508 | 2024-11-18 05:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 02112ac6-3e41-343e-b614-c5f8972d0ddd | -14.29178 | -57.64262 | 2024-11-18 05:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0f6260d-1371-3230-99cf-a6f0f457f3c8 | -14.65356 | -59.62435 | 2024-11-18 05:57:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d211940-8b17-30cd-9d15-cb568adad41f | -14.28389 | -57.64378 | 2024-11-18 05:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a2bdffd-9ad2-3215-9077-fabb63afb148 | -17.62169 | -57.5822 | 2024-11-18 05:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 769bf702-deff-3b2c-88d2-d49f6bae25d6 | -14.29105 | -57.63877 | 2024-11-18 05:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f84f4ba-cbdf-3a6f-b004-54761a291968 | -14.28446 | -57.63805 | 2024-11-18 05:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e204a4aa-dfa6-3b4a-a796-fb623915f1ec | -14.2852 | -57.64195 | 2024-11-18 05:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe55aacc-b4ee-3443-8bbb-c9d1298def8f | -14.28582 | -57.63614 | 2024-11-18 05:57:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d87103d-a626-3689-925e-f96ac16beabb | -1.2964 | -51.741 | 2024-11-18 06:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 54abb6c5-0819-3c96-aa3a-86340b7e212d | -4.9059 | -44.022 | 2024-11-18 06:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7f58d141-31d6-3b7a-8340-1eb69c5e9a72 | -1.2964 | -51.741 | 2024-11-18 06:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2ed2ec0a-3f2e-3f64-87d7-72298998a1ee | -1.2964 | -51.741 | 2024-11-18 06:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b61a3a1b-58d7-3179-afd4-b0e69c23b5d0 | -1.2964 | -51.741 | 2024-11-18 06:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c7c3d953-5273-3127-b4e9-976b248267d3 | -3.05026 | -54.40296 | 2024-11-18 06:37:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 948e6a16-79cf-3896-ab3d-7a756ee496e2 | -3.04621 | -54.39489 | 2024-11-18 06:37:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 53f9e1c8-b253-3bce-9e0a-77155fd8c87e | -14.28314 | -57.63489 | 2024-11-18 06:39:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| ad50bb3c-208f-307e-bc34-c00dc66bd8e0 | -1.2964 | -51.741 | 2024-11-18 06:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ccc926ac-97fb-3b13-bafc-9990e605e36f | -1.2964 | -51.741 | 2024-11-18 06:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 982abdd0-b7e9-305b-91c0-959cdbea5891 | -1.2964 | -51.741 | 2024-11-18 07:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b764c142-31f4-3e08-8b4b-477e6f784b0e | -1.3148 | -51.7408 | 2024-11-18 07:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1873f6b7-a22c-3e86-90a8-2f23c7976c49 | -2.5847 | -51.7181 | 2024-11-18 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 39296abf-b7a4-3319-8e53-f0bf4556f898 | -4.9059 | -44.022 | 2024-11-18 07:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8bd6146a-b666-3107-95a1-ceafe27a168a | -1.3148 | -51.7408 | 2024-11-18 07:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4891c2fb-8d63-3b02-bd9d-e501fa0f1d19 | -4.9246 | -44.0209 | 2024-11-18 07:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |


[Clique aqui para ver as próximas entradas](README44.md)
