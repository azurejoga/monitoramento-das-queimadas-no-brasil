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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01a52abd-ac29-3edb-b37d-50d8f57c6a1e | -13.6531 | -45.97 | 2026-09-16 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 8e2fca0d-537b-3645-a782-7ca81802701d | -6.8032 | -59.1693 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 412.9 |
| 19b9f46c-b3e5-3699-857e-4e18727df2c5 | -9.3707 | -60.3032 | 2026-09-16 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 86bcbb7b-e08f-3199-8c5c-29ed707bc571 | -6.5837 | -58.8498 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3f8be5ec-2bdf-31f6-9618-8a591f2d0e66 | -10.7015 | -54.1663 | 2026-09-16 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4264acc0-01bb-3872-ad9a-e34b6c2e139d | -11.9906 | -52.4695 | 2026-09-16 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 56b82625-b6c7-3459-898e-c801c505a344 | -9.7979 | -60.4734 | 2026-09-16 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 461413ce-49ca-39e2-b7a8-c0a247355cb1 | -9.3893 | -60.3022 | 2026-09-16 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8d8e6416-865b-366c-bf7f-52d8464e6696 | -12.6826 | -54.6763 | 2026-09-16 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6eb5a83a-9f94-3e38-8111-2c7966e95eba | -15.3602 | -52.9678 | 2026-09-16 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| eaa050d7-49d2-3a9a-baaf-2f40bc0cefa4 | -12.2131 | -52.8637 | 2026-09-16 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 09120805-58ba-34e3-9473-85f05f372de8 | -6.787 | -58.7834 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 12d0e8a7-c299-3ae1-b897-ec31be3089ed | -2.7149 | -57.608 | 2026-09-16 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 68973300-6f16-32bc-aa99-83aa4315a50f | -8.5497 | -64.0477 | 2026-09-16 15:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 20dcdfec-eb75-3694-ad9e-fbc2058b7f70 | -13.6085 | -48.2794 | 2026-09-16 15:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 5a7c9823-3bbf-3894-851b-23e8515b5c2e | -13.3754 | -51.7406 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 91e54642-f494-3632-8f25-a9a4815c8918 | -9.0868 | -61.0095 | 2026-09-16 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 42b2d37e-eac4-395b-8987-1deb2e446fde | -6.75 | -58.8043 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8755e1d9-bf48-3060-b8ef-deda0c239c0f | -6.7648 | -59.4408 | 2026-09-16 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f8ff5a97-d1e4-30cc-8b7a-20f0ab5bc2cd | -5.1256 | -55.9352 | 2026-09-16 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0c58e8d8-6838-36ae-9a4e-c9383a2237aa | -13.3391 | -51.6176 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 68d57b9c-e675-3f7c-af0e-3499f3df6c1a | -13.3758 | -51.7193 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3039f78a-4fff-3bf5-8593-b49826be2367 | -2.7148 | -57.6274 | 2026-09-16 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 511bd69f-45fc-35ed-9285-259bcefe851e | -8.5428 | -44.5132 | 2026-09-16 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 474.1 |
| 5a73bb03-22d0-3ddc-975a-a1796452298c | -10.3953 | -58.3159 | 2026-09-16 15:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| dea2fca2-a80b-3347-bc9e-157a372345f2 | -15.3804 | -52.9227 | 2026-09-16 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b6ef18fc-60b1-3dfc-b866-b89742a446ef | -13.4471 | -54.5761 | 2026-09-16 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f8e281fb-e57e-303a-99db-0fd00ed909ad | 4.1516 | -60.6878 | 2026-09-16 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 114cce15-3ba0-3e35-a5af-24ac2947473e | -12.1457 | -44.196 | 2026-09-16 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 931512dd-a6c2-3a45-9c42-32fd9a61ca50 | -11.9734 | -49.7705 | 2026-09-16 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 53f9527d-0d5e-3815-a213-d4eab34fa825 | -9.7793 | -60.4744 | 2026-09-16 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3d4f578d-ea0a-3efd-b1c2-d868173aecdb | -9.5725 | -46.601 | 2026-09-16 15:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 2290ccd8-0d2d-3591-be2b-6fd78e5b8509 | 3.859 | -60.6561 | 2026-09-16 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 5241d297-308c-398d-a13f-506d9df29281 | -6.2916 | -55.2895 | 2026-09-16 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8fbaaa58-42ab-3512-a529-f4af14b6220e | -14.6342 | -53.5666 | 2026-09-16 15:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 49969bf4-d139-3044-af76-9d239f7306c9 | -11.0617 | -49.7261 | 2026-09-16 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c1caf790-9f33-306d-87e5-8a42a49555c8 | -9.0962 | -65.9384 | 2026-09-16 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 01193522-1e37-3c4d-afb3-d0bd62d1cb1b | -13.395 | -51.7169 | 2026-09-16 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| bd0abbd4-01be-38d8-a0c7-7aab70c02120 | -12.126 | -44.2225 | 2026-09-16 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 392.7 |
| 2b77b3fa-d164-35ec-ba93-ccfc0907648f | -3.4461 | -58.0005 | 2026-09-16 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 16a751dc-5351-3829-a7c0-5c9df24993cb | -12.6821 | -54.7174 | 2026-09-16 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c9883020-7636-3d02-b431-4ac8af3ea7ca | -5.2023 | -49.3348 | 2026-09-16 15:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fa2faca6-8a18-357a-917d-57225669df85 | -11.1925 | -42.8305 | 2026-09-16 15:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 178.5 |
| 155c8161-d653-301e-b064-e8a42a2dc9fe | -13.5127 | -51.5532 | 2026-09-16 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 38022c0f-ec01-3419-b51c-ac31197dd9d4 | 1.1872 | -50.956 | 2026-09-16 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 20b71271-bde3-3241-a896-a0a8fab79960 | -12.6636 | -54.6782 | 2026-09-16 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4f7ad0f6-499c-3655-8fb1-96ac8d8c1ea9 | -1.6206 | -55.5679 | 2026-09-16 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 4f4c3056-e961-3a9b-b2eb-201f8563819c | -1.861 | -54.4315 | 2026-09-16 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6f93182c-ddf3-3425-bfcc-0148acf438dc | -10.3955 | -58.2962 | 2026-09-16 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| c9dfee76-004b-317a-869b-74973083c402 | -6.3196 | -59.9956 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 5b7108e6-d368-33c9-864a-92a9271dea26 | -5.3646 | -56.0249 | 2026-09-16 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 62924066-f27d-301d-a2cb-a0bbfd9ce23b | -5.4546 | -60.2155 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6ac361c6-c042-359c-9eda-87ce670e5488 | -6.8216 | -59.1686 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 280.4 |
| ee3c23f4-5d58-3c89-a9e3-1a78386934b8 | -10.3953 | -58.3159 | 2026-09-16 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| ad63403b-7570-3903-8983-244e43249534 | -6.7683 | -58.8228 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8c647322-1b2a-383e-8c43-4f9e6ff22a98 | -6.7648 | -59.4408 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 50a84089-2f07-3113-a973-2295fc59d780 | -7.9639 | -44.0435 | 2026-09-16 15:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 6d21976d-0750-36d9-bde5-8dc0e3470fbe | -6.3014 | -59.9579 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 094dd546-1ce3-3156-a367-7db6ddaef371 | -10.4769 | -50.9846 | 2026-09-16 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 61f94e62-24ed-3174-ae8f-f7697f5e9e78 | -15.3602 | -52.9678 | 2026-09-16 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d8d1e2a9-62d3-3256-a7af-166a5d33baa0 | -6.3195 | -60.0147 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b2dd5f23-db18-36cd-9438-799c8a3d23cc | -8.2831 | -45.6585 | 2026-09-16 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4a86a6d2-93ac-3d9a-8a54-2bb61aa9c1c5 | -9.3379 | -50.1814 | 2026-09-16 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3cb2b97c-7500-31ee-9c0c-aec3af46e136 | -8.6311 | -66.5287 | 2026-09-16 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e3b9227d-6648-34b2-9e7b-cba212488be0 | -6.2916 | -55.2895 | 2026-09-16 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d1dae944-156f-3137-9392-b1ac386cba05 | -8.8456 | -45.8939 | 2026-09-16 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 191.9 |
| cd363b32-750e-3600-a18d-7c8265bc1b84 | -10.876 | -50.8163 | 2026-09-16 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 51000543-083d-390e-9ebf-d7916ee80133 | -12.126 | -44.2225 | 2026-09-16 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 541.8 |
| f96421d6-7a22-3696-91e9-5b54dd4f1b1d | -6.7863 | -58.8995 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c6f9e52a-35cf-345e-a76e-13f58f0b9043 | -8.8585 | -44.9149 | 2026-09-16 15:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 3656876d-aea8-3e6c-8a87-23a6b7d6b7c6 | -9.3707 | -60.3032 | 2026-09-16 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 09de132a-d6b7-3497-8afd-369a23924296 | -9.0309 | -61.0314 | 2026-09-16 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 99f38d26-39de-3489-a597-78a5a07aa4ca | -2.6783 | -57.6087 | 2026-09-16 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 8206e8e6-fc69-3b1b-a4c0-a78646f859d5 | -11.193 | -42.8065 | 2026-09-16 15:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 265.8 |
| ce361904-67f0-3e6c-8f1a-732d0761471d | -6.3197 | -59.9764 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 613400a2-c668-3786-99b0-ca6b2538d935 | -5.1256 | -55.9352 | 2026-09-16 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a13f5419-421f-3d26-9756-03f2f4abadb5 | -6.338 | -60.0141 | 2026-09-16 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7748ee69-83ae-3122-8863-89a361676d28 | -9.3572 | -50.137 | 2026-09-16 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 43044405-b9bf-3fe5-a705-cb99c821cda9 | -10.4772 | -50.9634 | 2026-09-16 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c25a1190-05a7-3050-aaf7-792e842e8354 | -3.591 | -58.5384 | 2026-09-16 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 964ca516-d95e-3985-8d17-7b1936525a72 | -9.7793 | -60.4744 | 2026-09-16 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e1a87601-e0cb-3efc-b0af-3a27f037c079 | -11.9734 | -49.7705 | 2026-09-16 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 895e10d1-2589-3617-bfaf-09b7381fd1c6 | -9.3755 | -50.1779 | 2026-09-16 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ac5dd6a1-2c0c-328a-bb24-7a273ce4e914 | -13.6337 | -45.9732 | 2026-09-16 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 11a66da0-7aea-3d88-b288-a19c67a5585f | -9.3892 | -60.3215 | 2026-09-16 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f40fc023-3e44-32fc-90da-dd13e8783493 | -6.7839 | -62.9782 | 2026-09-16 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 82c446b6-137f-3ada-95dd-0cff6c6a3252 | -11.9906 | -52.4695 | 2026-09-16 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 239248c7-7327-3f40-b473-7aa5839967cd | -9.0868 | -61.0095 | 2026-09-16 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 198f9657-2b94-366b-9b87-beb30d824c13 | -10.3766 | -58.3171 | 2026-09-16 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 6a16b2b2-ff44-3c8b-bc26-c3604492a172 | -10.6335 | -50.5651 | 2026-09-16 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b423b7b9-b43a-347f-bf2c-398fdfffa8b9 | -6.7869 | -58.8027 | 2026-09-16 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 438eb42d-051d-37ed-af60-9358af4997e1 | -10.9674 | -49.6936 | 2026-09-16 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f880979a-ac10-3494-b2f8-73bd83b1ff0e | -11.9543 | -49.7728 | 2026-09-16 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 24978a51-63d8-3ff9-a93f-e3728799c523 | -8.2052 | -54.8416 | 2026-09-16 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 142c7a8a-9f47-3da2-b212-bfaceac587c1 | -12.6821 | -54.7174 | 2026-09-16 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| db502c23-34c9-302a-b4c6-55481333f010 | -9.7979 | -60.4734 | 2026-09-16 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1a9d4046-07be-3a36-aa8b-b775ff64ad0b | -9.2311 | -46.7055 | 2026-09-16 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 6aaea692-d601-3e76-852d-7b3134eacec7 | -11.4167 | -51.4371 | 2026-09-16 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 39eb84cd-af82-30ae-991e-f09bd71005c8 | -9.7322 | -64.9067 | 2026-09-16 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 075292d8-5141-3748-b6c0-912ded66637e | -12.6826 | -54.6763 | 2026-09-16 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |


[Clique aqui para ver as próximas entradas](README81.md)
