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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7689db8b-035c-31ac-aebf-9c90a674ede3 | -4.70482 | -47.92928 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae4f5a2d-cf4d-32a6-b109-6f2376767b62 | -3.84601 | -50.09829 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b47d1761-9597-3dc7-9258-cfa48fd0c143 | -3.08549 | -53.27495 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b52ec9-29e6-3ed6-a6f6-6e48cfa88ea7 | -2.60322 | -53.97415 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f5f32e2-a6a1-38f5-92b5-d289c003a22e | -3.53986 | -50.40102 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ad076f4-46c5-3793-8d2d-c27d78d0ef60 | -3.27982 | -48.75227 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e286c8d-9735-3abd-98f0-a60c75e81eb6 | -3.49624 | -53.81967 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4769d7d0-8b99-37c3-84da-3651c03cb982 | -3.13227 | -50.25723 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38983d12-23e2-3767-a0f0-cbb87628cfbb | -2.8477 | -49.40186 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f82e163f-f48d-3674-bc04-3ce9ec7c85d4 | -2.58013 | -51.92115 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4dbb8a5-bb04-349c-8b2a-85f37e2c2406 | -2.86268 | -46.81301 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc018bdb-d82f-3406-9482-6187de241a87 | -3.23542 | -50.17525 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e5633d1-83ad-3e59-827c-85921cd61e39 | -3.29283 | -50.53839 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b353b29-a96f-3f0f-8177-bd5fc4303165 | -1.75821 | -53.63097 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 699b9d4b-994c-3662-9066-b25779ab4a35 | -4.57077 | -45.75684 | 2024-11-27 04:18:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccba63d2-426c-3008-a77f-c381e2b751e5 | -3.27198 | -43.036 | 2024-11-27 04:18:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0777a16-d989-39a8-9744-68cf89056078 | -3.72297 | -50.1884 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eb4a3fe-1e3b-32c5-b1de-a264308efb05 | -3.94026 | -46.71368 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf393aa4-50c0-3b77-a209-e8209eba8c5b | -3.33289 | -53.72403 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0658ec76-6b50-3e8f-860a-ecf158b87a6d | -3.40839 | -53.19882 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315d427b-ef79-3d39-859c-ddec1158cc0e | -3.87386 | -50.14554 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 490ddd56-b9e6-3a5f-909b-abdfe45d62c6 | -3.24031 | -50.14531 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cca5eae5-31fb-34a9-858b-40fa5d2d5825 | -2.69729 | -48.6577 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 160de275-a7b3-3985-8e9a-66539534ba41 | -1.95675 | -50.57618 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a7f5b51-c68a-3546-8682-da5ccfdcfd24 | -2.82055 | -46.83711 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7628278b-d105-3733-a8b2-3ccee6adb908 | -4.16652 | -46.71976 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 939b12a2-e7cc-3ce8-be50-8df1e6e5d275 | -2.59373 | -54.21141 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 32d089df-f7ef-31aa-b3e7-4b664c2f8b22 | -5.31529 | -43.07207 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a1a0c6d-597e-3078-b7ee-44cb4fe10e29 | -2.99927 | -45.46828 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff87e679-7f8b-3402-8738-b9d41c9da1e0 | -3.24278 | -46.42685 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff836af9-c2c2-3582-b508-ec42a44a723d | -2.9366 | -49.12559 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e8460d-56ab-302b-8c76-c9445c971a9e | -3.88606 | -43.15276 | 2024-11-27 04:18:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a16214b0-eab9-3dfc-9415-80a77c2337dc | -4.24536 | -48.59135 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e32a44c-63a4-3170-936c-b347afabfa65 | -3.92226 | -46.50977 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2154be17-6605-32ed-8adc-1ec00ad23eda | -3.10232 | -53.27955 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 746caecc-26a4-3911-bf19-aeaa77631365 | -4.27428 | -48.61094 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12bff120-ce0b-38ee-bc2d-59c3451611c3 | -1.91778 | -48.70002 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68547152-fc04-39a5-b8ed-e16f366ed49b | -2.7775 | -48.28875 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c84eecb-5f54-3d76-ba04-2dcde5c800c6 | -3.37929 | -50.11847 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b8794f4-2c03-3313-aa1c-e3508efee62a | -3.72376 | -50.1823 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59623b30-03d8-3f95-aa08-ba2a23eac8d7 | -2.86628 | -46.81357 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a9920d1-20ca-3408-a777-7284a1fc1745 | -4.31234 | -48.08485 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9671305-92d3-3345-8a82-bed7bbd895f6 | -3.70873 | -50.43517 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c66c8547-dc9b-343a-b205-2b7ab4455ee4 | -3.00384 | -45.46152 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe0062ea-7605-3b34-b5fc-14ab57329188 | -3.83509 | -46.53675 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee7d61e-428a-392e-b713-e96c4358926a | -2.88986 | -51.38498 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffbf2a2d-1cfd-3b64-a2f8-edb9a812737b | -3.35885 | -50.18899 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8184eb91-67d8-3bcb-b426-e66fbfaa4a6f | -3.04627 | -48.50718 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32ad593a-0e36-32f3-a1e6-e3027d3d1443 | -4.65478 | -43.81829 | 2024-11-27 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d5716c9-cd9f-3339-bcb8-5d3bba4d9ef8 | -3.50678 | -49.4614 | 2024-11-27 04:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed010b1b-e6d0-3bd4-817a-b75bdbcfbcb5 | -4.69674 | -44.96794 | 2024-11-27 04:18:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59a94296-af3d-38c9-85ed-ca0012e5121e | -2.94172 | -54.79909 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e71a744-f8b1-3529-995d-aa7bc624d7df | -1.45028 | -52.59224 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 402e5965-ebe2-3d8f-8ca0-80452800e2c0 | -3.90107 | -50.11586 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d5d137d-84b3-3347-8104-e29d4131d715 | -4.17195 | -46.0834 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bc8583f5-6685-3f8a-be37-c2b8048b094f | -4.095 | -44.85913 | 2024-11-27 04:18:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a86cdb90-4667-3db1-a88c-9aac2d9e21c7 | -2.2548 | -53.75192 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9648bce2-2e5f-3969-bae9-a24bf71dba88 | -2.86176 | -46.80997 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1060b7e6-6024-3d6b-8ff5-23f3af5c4e4e | -1.44974 | -52.5956 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37804175-e457-3d52-9c6a-a5d4439e8372 | -3.08926 | -53.28617 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06e78c41-99ad-3970-bfc6-0847ffb46012 | -3.10133 | -53.28106 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caf0a466-3399-3785-bf03-7dbb78cb89bb | -3.39664 | -50.31262 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2d3b8e0-d525-30dd-9a12-5fd881797485 | -2.94536 | -48.56182 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dfba038-8488-3577-90c5-3982610b21c9 | -3.54877 | -50.20769 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4506535-b164-3e4b-9381-d3da3ccb444c | -3.09139 | -53.27781 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9983545a-620d-3137-af55-69adc7765439 | -4.27263 | -42.4365 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8f86f85-9963-3ff3-84da-4ea466edafb8 | -4.27988 | -37.99517 | 2024-11-27 04:18:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd8f3980-e582-3884-98ab-f2e98b1b769d | -3.90087 | -50.6035 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c78bf92d-0ffa-376c-a5ff-22462d1b4aaa | -4.16254 | -46.18543 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bd87ed5-9bb8-3bdf-bf86-d98e87714142 | -2.23838 | -53.63173 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a93f433-af4b-3b4f-8b09-1f4430f14412 | -1.67755 | -52.44387 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f841455-539c-3e20-804a-bb73a9278ac0 | -3.00326 | -45.46517 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 19075521-2901-3105-a25e-8e7cd490b6e9 | -3.59734 | -47.34525 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0720d413-7716-3954-bd47-2caa05380f68 | -2.77029 | -52.90327 | 2024-11-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a25f5e43-e3cb-32fb-9cb5-af73471e8753 | -3.1186 | -53.7618 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21246990-c4a8-3ad8-8ad7-6a70ec2f4b72 | -4.90895 | -38.73781 | 2024-11-27 04:18:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c35fba1-edff-31be-a16e-bf56417229b2 | -1.95403 | -54.13467 | 2024-11-27 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bae1c72-2c88-383f-9798-73a4b70cec8a | -2.58787 | -47.4772 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9c96ff8-bd2c-3563-b9f4-0b4e58088531 | -3.3304 | -53.72218 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33c895a1-ebb4-3f3c-848c-bacad74df58e | -4.30025 | -48.18257 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9202cb33-c9a1-347e-8dcd-94ec2d6b0267 | -4.92873 | -38.74857 | 2024-11-27 04:18:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e68f3e60-9227-3207-a48c-82f458a3ea27 | -5.84198 | -39.20728 | 2024-11-27 04:18:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 286ebb72-da9e-35ce-96f1-d75e0e9736e4 | -3.92844 | -45.84126 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2553f004-8f07-3c36-a354-c037d1810cff | -2.80297 | -54.12896 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35de8037-05fa-3c01-ba0b-ebcc26171d64 | -1.78097 | -52.73997 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de46a841-1a92-38d1-a7c6-8e8c458079b5 | -3.49481 | -50.4521 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ce8a027-74a8-328c-a386-956e44fbe626 | -3.11296 | -53.76084 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4cdd73a-00df-3208-886d-4c0f49570ba1 | -5.58164 | -42.92821 | 2024-11-27 04:18:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1c957457-1903-3879-8b25-50526ff801b9 | -3.07946 | -53.27751 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2490ec3-c7ca-3f17-9daf-8408ee0b7373 | -3.70489 | -51.80642 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b555537-1266-3363-9551-837e6277d1f9 | -3.93963 | -46.71769 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1cfeebf-933a-3262-aa5d-700db65dd50d | -5.83787 | -39.20669 | 2024-11-27 04:18:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 81f6f63d-20cc-31ae-9ad6-515dfb9b5ce6 | -3.1784 | -48.43268 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b6ba6b43-43c3-3154-9d30-e06626611179 | -0.98871 | -51.72143 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bc3f9ad-e064-35ab-8dbc-fb1a03151417 | -3.98085 | -48.08152 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66304bd7-8a4f-3328-af76-cf9d52724c74 | -3.80554 | -46.60848 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b98a3c21-9a9e-37ad-99f0-c4d069612de2 | -3.9778 | -48.07628 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3953e170-c32f-3330-908c-e691a1eaf99f | -3.25226 | -50.61557 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8ed6b9f-85d3-3478-82e6-d96a8b4e4662 | -2.73188 | -47.53992 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fae23270-8bc2-3b76-bdf6-996803ccccee | -3.51347 | -50.31184 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README43.md)
