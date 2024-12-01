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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0c5895f-3778-3b3a-947a-5098508159cd | -3.10773 | -54.04573 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de65b491-315e-33dd-b8a2-bc8d7ec357f0 | -2.83626 | -46.86424 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77fcb13a-6f82-3899-b75e-9a7c94977973 | -2.70813 | -52.00252 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e161e10-0828-3d18-be16-a647f9d4ca96 | -1.70632 | -46.14444 | 2024-12-01 04:44:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| beb29ed9-3e44-3ec7-beac-0cc3e6170f93 | -3.14219 | -53.82857 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fdfdbda-d997-301f-b3bb-1a7b43079d06 | -3.01555 | -51.43481 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 142253cf-25ff-3928-9ed5-c3a6f480cba5 | -2.68623 | -51.72559 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7da3dae6-91de-3dde-b100-0eea72c6ea5b | -3.0946 | -51.26224 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e085fcb0-a8ba-3409-a886-49b1b391251f | -2.7679 | -55.34846 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a213f21-8b39-3e0b-b648-0607f652b614 | -3.25313 | -53.62257 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c721039-8fe8-3e2c-a141-e06975ef3be8 | -1.36961 | -53.64001 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15856089-9764-3b2a-9254-fee045e21b66 | -3.26625 | -50.04504 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 256bbcc6-ffcf-393d-bac3-08199b7c7036 | -1.29377 | -51.36578 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5440081-9153-3f62-8f0e-c8144a2c7c57 | -2.08385 | -46.6684 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ec0dcf4-3650-335c-a32c-56b1bc7b194f | -3.02251 | -53.87882 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 637b8c76-55f4-31fe-aa2e-f010262d9a76 | -3.59478 | -50.36893 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d1ac9a1-ce69-3788-9fa1-95d68cf5d86e | -4.00559 | -54.61479 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34732247-0b60-3001-8947-08a4c8a7e501 | -0.59899 | -51.69215 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08be817d-2b81-33b9-996a-75df53d7db4f | -1.19104 | -51.77476 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53fbb09c-0932-32cb-adab-5412cd56e44f | -6.87034 | -47.2429 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99f27288-7a36-323d-8df6-53c912959360 | -2.58282 | -54.21023 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f366b10-ec9c-336e-9ba6-b5ab11007289 | -2.10812 | -50.73848 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12adf3c5-6687-38a0-b11a-a18a5d424c2d | -1.37153 | -52.41497 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba972f6-84ee-3ae6-8651-9ea96e775f35 | -1.09713 | -53.38917 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1631564d-7de1-31a7-aee5-47b792187687 | -3.09415 | -50.34347 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17c30441-6ddd-375e-bf9d-9a75617c7f2d | -3.07658 | -53.25877 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1329e344-6816-3810-95c7-98bf2a58d3a8 | -4.45809 | -56.18509 | 2024-12-01 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caaf79fe-e3be-3d6f-99dd-d2d546253ceb | -1.49799 | -54.95544 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73808a7e-d08f-3703-aa6f-8f7013366acc | -3.08877 | -54.01982 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f3b5e0-d627-3e46-8fa2-cae3b89986b8 | -3.70473 | -51.80209 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a53f59a3-fc6e-3f59-96b2-5d86d3d847db | -4.69381 | -46.80676 | 2024-12-01 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ebc48de-e9f4-3cfc-a9fc-8027b31a53db | -3.27352 | -51.47852 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca783ede-3ae2-309c-87bd-88b2e69b3724 | -1.29903 | -51.73009 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 373534b6-0485-35f0-be99-c341238129ea | -1.1974 | -51.75668 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db7c1b87-66cc-37eb-a70b-0672018422f5 | -3.46549 | -53.88349 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59aa35dc-f86d-3209-b8a3-8ed7c45a4195 | -2.72567 | -46.24005 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e82bc6d8-6801-3e5c-b5f2-433859bebb88 | -0.87723 | -53.67912 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77de6c2b-7628-3c15-a2cc-fcb3e6b4b913 | -4.11637 | -50.31969 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c802a5a7-ac51-39ce-8c51-40331424a82f | -4.89597 | -41.3245 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 527dcf7f-fb23-3a53-a03f-64cbbb539838 | -2.24178 | -50.78768 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4cb4805-9a98-37ed-9649-a5cc7741868f | -3.19046 | -54.32973 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ea4259a-d439-3001-8258-cd32b755e1a7 | -5.18759 | -43.94933 | 2024-12-01 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30854795-356f-3d23-8b06-b1ebf18a6707 | -4.10647 | -50.98408 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a0c0806-3379-3d4b-9581-e8bbba74bb17 | -3.67582 | -54.04663 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 960528f9-8af8-3d37-a0a8-a63f92158912 | -3.8301 | -46.60271 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f69402b-50f2-361b-80ca-7079698d1692 | -1.62987 | -52.37798 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 849c2099-a660-340d-8360-a8bdf6debff4 | -3.0888 | -53.71243 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58cc983a-14e1-3011-8229-ab744bb5374b | -3.84678 | -52.02491 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7304cbbc-6890-35cf-a6f2-b978e4c757c5 | -3.45675 | -54.56834 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc824225-5585-35b3-8921-f2ee0de4dc7c | -2.64547 | -49.90511 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b5f2bed-e76b-3921-8f40-ce9c2f0b10d4 | -2.87883 | -53.32719 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db388da2-eaf1-30cd-8042-ebace4fbeb19 | -1.09128 | -53.64296 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e1540bf1-1168-3087-b667-f6159fc2cee5 | -2.82165 | -51.79479 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aaf47dd-12e0-3e88-972b-b8e841ce3497 | -1.18071 | -51.77314 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac790b4-38c0-3a4f-bc62-803464606e24 | -1.9665 | -54.13156 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 973d8009-a7ed-3bd8-82f7-9845bda91132 | -3.73793 | -51.83314 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb126ff8-66cc-363b-846f-69088ad9ea52 | -3.41988 | -50.3587 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d347fc77-1166-3349-a13b-35e7abc6d541 | -3.20993 | -53.12406 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e769ac97-a1e1-3f89-9969-df236c890b42 | -3.67498 | -50.24343 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b97034a-cccb-3d6e-8010-367242d09d0b | -2.74024 | -47.98337 | 2024-12-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3aaa6b-0ffc-3299-926b-f8842e120a5d | -2.11979 | -46.41341 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7716a9-6e0b-3dcc-93a8-634011cd625e | -2.29363 | -50.54667 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82508e75-d9b0-3f3f-999a-ad1ae02f8a46 | -1.65842 | -52.40241 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa753e54-b3e3-39b5-b7f2-26b9c69c17bc | -1.44763 | -55.189 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e1660b0-8537-302b-b757-4831dc580ea0 | -3.27447 | -50.20891 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 558aef23-9bd6-317e-bf45-f7c95122ef8f | -3.2694 | -53.63826 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12d53fab-30a9-30ce-bebe-5aea4bc69e37 | -2.99377 | -45.57165 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b86c9e3b-6de0-3643-b887-0891ab91a8b6 | -2.57735 | -53.67131 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ce5573c-3f72-3b74-9b60-d2961037f86b | -3.09422 | -53.33342 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ac6c87b-f791-385c-bf43-c3bb0ca2df80 | -1.65284 | -52.25488 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b33c644f-df2f-3aa7-bd48-397713451621 | -1.97262 | -51.95098 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9f83cab-4218-347a-98e6-9555758ad00a | -2.48214 | -50.36367 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e18646c4-5864-3b10-8366-f24cb8450048 | -2.80506 | -49.77485 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb254435-4d7b-361d-bf47-c4590969ad37 | -1.04269 | -51.73677 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 158e0bb9-c55c-3e5f-86db-7c8ef48437b7 | -3.06873 | -53.81239 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 146b2ddb-ffe7-35db-b3e3-4c6771785636 | -3.57281 | -50.42205 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41e38f03-db41-39bb-8b7d-1f696993856c | -3.43003 | -53.89137 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b533f44-2b57-3e05-8727-2c62b33fc309 | -3.05867 | -53.67481 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7bb36c6-4515-3f37-b1a1-be072876eed6 | -2.75987 | -54.12245 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29c5f3a7-885d-371c-819a-2011a0706c63 | -4.50338 | -55.83245 | 2024-12-01 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efaa94a4-ae16-3178-884b-7faca59a0062 | -3.2481 | -53.63054 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea99a43c-edde-3f07-bc91-f823f244b6d0 | -5.42455 | -45.10679 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f011304-3cd1-3fd2-b8dd-c01440a40bac | -7.38222 | -45.83539 | 2024-12-01 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e0fb255-e40a-32e4-9475-2acfcbc818c1 | -4.00485 | -54.61937 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0653329-b0a9-3f83-9bcc-0c4144837d80 | -4.34622 | -50.77309 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eeb9223-f16c-33f9-ad32-6847932da341 | -4.07646 | -46.68493 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a2ecb0d-b3c3-3c06-b3a5-b5330bb4d80a | -4.02042 | -49.93925 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51a3f494-e739-3e8e-8bf4-5d79ee5b7594 | -1.36324 | -51.85401 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aee9488-8484-3b3c-b6ae-f47a284aa638 | -1.42483 | -55.27703 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6053c511-9727-3838-83ad-6aea42655522 | -3.10795 | -53.10927 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99e1c9ae-5702-3db8-84b0-05f1e18baf0d | -1.26628 | -51.75917 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da226e45-958b-35e5-ad39-7c6abf37d2cd | -1.9813 | -52.89315 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 119d1e84-1da2-3aa7-b1b5-69599282cd30 | -3.79596 | -58.97312 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c922018-77bf-3edd-a09e-8c7c1e9a9411 | -4.32149 | -48.08642 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20d35026-3351-3386-89a5-0c755d66f438 | -1.90382 | -52.87265 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6d5a968-37a3-35c1-aae1-ec3574795021 | -1.53055 | -52.66132 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e8b0ed1-4ed8-3278-a900-d1af37c07ce1 | -3.0944 | -54.27092 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 111e193a-a7da-347d-a944-25a94dbee68b | -3.2568 | -53.62313 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c5894900-a80d-3017-a856-3cad748e7a86 | -3.67444 | -50.24688 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ab0c336-ba63-3e4c-8767-13c938e32ee8 | -3.26185 | -50.05143 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README62.md)
