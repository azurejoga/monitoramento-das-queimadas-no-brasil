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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09f46503-1de0-33e9-804c-824a704ebc05 | -7.1169 | -44.0339 | 2025-06-16 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 4251a319-1508-3c40-b32d-88e3a4e3a273 | -10.0972 | -52.7376 | 2025-06-16 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| addee394-849f-32a7-b729-14749c9a4955 | -11.0117 | -55.0358 | 2025-06-16 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3a0ef2f0-29b3-345a-b3b3-fc986ef2bba7 | -17.4596 | -48.1613 | 2025-06-16 00:40:00 | GOES-19 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6f6d01d3-69b2-3dfa-b096-9f9ca42bfa92 | -11.1571 | -53.9206 | 2025-06-16 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8fda5bd6-ddbf-3022-a5b0-3843ffc343cc | -11.1568 | -53.9411 | 2025-06-16 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| f7ddb7cf-e8b8-3a83-8791-9974456d8738 | -11.0115 | -55.0561 | 2025-06-16 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 5806185b-c678-3a2c-9ede-d74fd0708678 | -11.1379 | -53.9429 | 2025-06-16 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 2bfc5b2f-d448-3c18-9ce2-4d7adb0d52d4 | -7.1167 | -44.0571 | 2025-06-16 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 2ef74f0c-91b7-3d2d-8ffb-91136578b646 | -11.0113 | -55.0764 | 2025-06-16 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9044eec9-1218-38a7-8d18-aac3c6eb0ead | -7.1357 | -44.0322 | 2025-06-16 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 216ef30a-a898-3bb4-8f30-226c8657d3fc | -11.1382 | -53.9223 | 2025-06-16 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 822dc3ec-c43b-3aa2-9f47-d93aafef877d | -7.0981 | -44.0357 | 2025-06-16 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 96385e86-d4a1-3314-b274-e3e5ee4c01ad | -10.9926 | -55.0577 | 2025-06-16 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| c87f63bb-8f49-3720-9062-8627a3d5943e | -7.1172 | -44.0108 | 2025-06-16 00:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| dfb5a976-6750-3652-a566-265498cd5adc | -11.0113 | -55.0764 | 2025-06-16 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 38b69e57-e9df-3107-8e47-286dc313057c | -11.1379 | -53.9429 | 2025-06-16 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 186.5 |
| d4e703d8-830d-3b1f-a40b-7d82803aca1e | -10.9926 | -55.0577 | 2025-06-16 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| b8f6f3eb-38e8-3c9c-9956-d74a89320314 | -11.1571 | -53.9206 | 2025-06-16 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e7eb2e94-fd79-3a75-b394-7b13d707013d | -11.1568 | -53.9411 | 2025-06-16 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 47dd8e07-cb38-3d45-a29d-e6c743fc376e | -7.1169 | -44.0339 | 2025-06-16 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 60f17d65-a56c-33a3-81b4-ba57b4593956 | -11.1382 | -53.9223 | 2025-06-16 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| fd1c2b0f-29d0-30ae-af2a-664c3218a016 | -11.0117 | -55.0358 | 2025-06-16 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ae46b6ad-9ed5-3fff-b45f-7f541c86c6dc | -7.1357 | -44.0322 | 2025-06-16 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 46a2f5d2-7289-31c2-8563-a670774d393d | -11.0115 | -55.0561 | 2025-06-16 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 3b92a2dd-f23a-360d-99c6-1f312d2d8f78 | -10.0938 | -52.740601 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 502d98dc-3837-3da4-b626-bf861ee9afbe | -10.8535 | -53.777699 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c910f4c9-fb8f-33d4-a8a5-5766d4bbdc9e | -17.455601 | -48.167702 | 2025-06-16 00:58:00 | METOP-C | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97b742ea-3853-3a1b-9c4d-df42c4385d75 | -14.0336 | -55.123199 | 2025-06-16 00:58:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0ed60ef-cd07-36f0-92f9-2dc1880833de | -7.1105 | -44.0247 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 082d19b6-a2c7-340b-9fe6-7a1c1ab4f52f | -10.084 | -52.742802 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49272af7-a863-3e39-b0b8-a71b6f7c88a9 | -13.919 | -54.635101 | 2025-06-16 00:58:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6deec0fe-f1b6-3929-836f-34afb2b87d95 | -11.0129 | -55.054699 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa99fbae-14f2-3db6-9e00-42f441d7fea7 | -7.1256 | -44.0434 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2683036-2bb2-371f-a251-58b1b1a57979 | -11.1478 | -53.9436 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5be7ee-a814-37e8-bf0a-4eda8fd2b131 | -7.1352 | -44.041 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a882987-21fd-3f43-95d0-8118a2c0bef0 | -10.0742 | -52.745098 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5f0c06e-966b-33c4-966f-fe963bcd5375 | -10.0953 | -52.747501 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4e083a0-1e10-381f-90a4-f36724ca9ff9 | -7.1149 | -44.000999 | 2025-06-16 00:58:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a24e0ed-64de-3591-aa0f-f5f110343648 | -11.0048 | -55.064602 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7999330-b6cb-3300-b8bd-b894ff0d206d | -10.0922 | -52.733601 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d85fb944-970b-3bb6-8fd0-d7f638a80780 | -11.0065 | -55.0723 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87b7ad19-4216-3856-a72e-6fc4b9fcd1a4 | -11.1348 | -53.9314 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14183f90-f886-3531-9a2d-8ac1e207236e | -10.1036 | -52.7384 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79ad9900-493c-300d-8f71-ae6073bef159 | -9.4107 | -48.431702 | 2025-06-16 00:58:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49b4132d-aa06-3504-b053-5bf4b532edcb | -7.1159 | -44.045898 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1e6a706-d6e5-3a15-ab4a-09ee4e16d953 | -10.0726 | -52.738098 | 2025-06-16 00:58:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdb897d3-c114-3f30-b4ac-ef0120253b12 | -13.9156 | -54.619202 | 2025-06-16 00:58:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00e5e1d3-ff69-33b9-b341-c7038e9a4d63 | -11.1446 | -53.929199 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e179ebb8-7cac-3e6b-a143-30ed2e130990 | -12.9862 | -48.641701 | 2025-06-16 00:58:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 922ee0fa-4f18-3797-972c-f11bffc1e1dd | -7.7211 | -55.139599 | 2025-06-16 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e36fef-6478-38f1-8cc4-700c4061bef3 | -11.0146 | -55.0625 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 565a1882-b1e1-3d7d-9494-b1a1726a8b26 | -10.2292 | -54.300301 | 2025-06-16 00:58:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab1f2066-e2bc-31ab-b990-a171848740c1 | -12.7623 | -44.396599 | 2025-06-16 00:58:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 488f54a3-fb77-377f-8fb7-6e5cd0188d94 | -11.0163 | -55.070202 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58c80540-697e-30af-b8f7-9c2442c5f9b1 | -13.9173 | -54.627102 | 2025-06-16 00:58:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9c4729e-beb5-32aa-9b0d-1755b09a490b | -10.855 | -53.784801 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee02eef1-92e7-3933-bdcb-e7ab9be7d812 | -11.0031 | -55.056801 | 2025-06-16 00:58:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f863f17-3d6d-3950-8e41-dde803b71dd7 | -7.131 | -44.064499 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75b3048e-e3a4-3b67-8ed6-2d22bc093054 | -12.0934 | -49.490101 | 2025-06-16 00:58:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd3b0aaa-5b2c-33c4-aa5d-27100d74a878 | -11.0082 | -55.080002 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d616ba2-e10b-3242-a86d-337a40633c6a | -7.1213 | -44.067001 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc52020b-cfa6-307f-9508-c9404e2f13ec | -7.1298 | -44.019798 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2ce3be-cfa9-35b7-883b-34ffa2d6e4a1 | -7.1202 | -44.022301 | 2025-06-16 00:58:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 472cb783-3627-3926-9cee-7f0aabbc9333 | -11.0112 | -55.047001 | 2025-06-16 00:58:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60eaccde-0bae-39ea-811e-b123ee817f2e | -11.9844 | -57.193501 | 2025-06-16 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeb4f488-cc8b-340f-95dc-f6b66748a8d2 | -11.1462 | -53.936401 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70602520-6984-37b4-8292-53cf9b6df182 | -17.4576 | -48.176102 | 2025-06-16 00:58:00 | METOP-C | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca800a9-53bd-3126-a1cf-e268d7b2ffa5 | -11.138 | -53.945801 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d77ae92-8f5e-31e3-bd9d-cad241914eb0 | -10.2276 | -54.293098 | 2025-06-16 00:58:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be86b476-617d-3d83-b0aa-256fddd7d820 | -12.7664 | -44.412701 | 2025-06-16 00:58:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 622d796e-7ad2-36bb-84a2-92bbcffd9dee | -11.1364 | -53.938599 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42a8bb4f-c61b-36be-8213-0515a553b18c | -10.8519 | -53.770599 | 2025-06-16 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86bbe2cd-0eac-3ffb-982c-414bf21bc3e5 | -11.0014 | -55.049099 | 2025-06-16 00:58:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 123792c7-2c08-35da-b936-9305422e8d8a | -7.1167 | -44.0571 | 2025-06-16 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e120ee30-d6a4-360d-b7d0-68cd065b20ba | -7.1357 | -44.0322 | 2025-06-16 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 44ae4f8d-75c6-32bf-bb70-dae187a4194b | -7.0981 | -44.0357 | 2025-06-16 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 89cfa321-ee15-3073-babc-06125f4244a7 | -10.9926 | -55.0577 | 2025-06-16 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 588249ca-ad40-3b2e-925a-d35a806e0a66 | -11.1568 | -53.9411 | 2025-06-16 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f72f4850-20a7-39a8-9707-d4eb4a1fe423 | -11.1571 | -53.9206 | 2025-06-16 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 01cc0b5f-b03b-3d0d-8bab-4c4da3163d47 | -11.0115 | -55.0561 | 2025-06-16 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 193.4 |
| 532b3681-ec23-3839-a011-8d29d3ebcfe3 | -11.1382 | -53.9223 | 2025-06-16 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 42914960-9138-319b-ad09-93362f6f00fe | -11.1379 | -53.9429 | 2025-06-16 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 3e168beb-e358-349c-b90e-cb14498f79e4 | -11.0117 | -55.0358 | 2025-06-16 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 24c3f9d6-8747-3463-ae7f-4e1d49b69a0f | -7.1172 | -44.0108 | 2025-06-16 01:00:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4de24e7c-40eb-380b-bcb2-2a1dcac8bf6f | -7.1169 | -44.0339 | 2025-06-16 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 319.0 |
| 82641eb3-206b-38b3-a70a-5f738fe50f62 | -11.0113 | -55.0764 | 2025-06-16 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 63311817-5703-343a-860a-7116de3f0e93 | -10.0972 | -52.7376 | 2025-06-16 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 899f8513-25b6-3299-b28d-08171140f43d | -7.1357 | -44.0322 | 2025-06-16 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| c14fadf7-0fa1-3f11-9d49-d453897a9fc7 | -7.1167 | -44.0571 | 2025-06-16 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e609c496-d1ad-31df-8933-6a97c9814419 | -11.1379 | -53.9429 | 2025-06-16 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| ebbfb031-0417-3a19-a4a0-ec0817f252bb | -11.1382 | -53.9223 | 2025-06-16 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c711b876-cc12-3291-94a4-7284613a4d4b | -7.1172 | -44.0108 | 2025-06-16 01:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 349a1734-40ac-3ae0-8246-0239e8c19c78 | -7.0981 | -44.0357 | 2025-06-16 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 907fecf2-7e84-3fcf-a816-88ae717e53dc | -11.0117 | -55.0358 | 2025-06-16 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 80a333b7-7328-375d-8b79-5586885547ca | -10.9926 | -55.0577 | 2025-06-16 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c924a5b3-34b9-340f-8e6d-c1a2da4fedbe | -7.1169 | -44.0339 | 2025-06-16 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 99fe08d9-95d7-315d-abf7-6472556f49ff | -11.1568 | -53.9411 | 2025-06-16 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| bbabf026-3bef-391c-83dc-eb08be87fd0a | -11.0113 | -55.0764 | 2025-06-16 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 9e4e6563-a58e-34f2-86ed-85941b2f6c4c | -11.1571 | -53.9206 | 2025-06-16 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |


[Clique aqui para ver as próximas entradas](README3.md)
