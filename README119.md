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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c426ec0a-425d-358a-bc55-ae50ebbfe7ab | -12.86803 | -51.18543 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90a1fc14-7111-3e4a-bb61-94c61cebbfcf | -12.86773 | -51.21549 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| bdbb7a05-7185-3178-8ea0-5314c409dadc | -12.86734 | -51.19035 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5bba2335-c08f-371e-9776-6db06637e252 | -12.86704 | -51.22039 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| a5a90656-4171-3751-a0b1-c6acf64a1a01 | -12.86664 | -51.19526 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a14fc79-6073-3d5b-b3da-21e5cfbb859f | -12.86634 | -51.22529 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a6ffe4ae-d154-38b6-ae43-71ecea08dace | -12.86595 | -51.20018 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac4ef984-6d26-3ea5-afc2-7494b71ec659 | -12.86565 | -51.23019 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 7aee7c90-2768-35c6-b162-1abb95597956 | -12.86555 | -51.175 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 630eae18-b755-3ec2-8f37-1a71119f34a6 | -12.86526 | -51.20509 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0228b99b-e3e5-31d2-a28b-ed4b046bfb6f | -12.86496 | -51.23508 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e846b9ff-9bde-392e-9fc5-4b334c8c42e0 | -12.86486 | -51.17993 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15cc6abf-5182-38f4-8a30-6bd7fc33920c | -12.86457 | -51.21001 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 54610bef-530e-3738-bd70-f3b24083fabd | -12.86427 | -51.23997 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14a3fcb8-c8e2-305b-a9a3-ddcba8ed2eb4 | -12.86417 | -51.18485 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 98a8ec09-150e-3ce4-8dc9-59b46ab10931 | -12.86387 | -51.21491 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 14689298-ca02-3dc7-9d5a-f7e3c463ba76 | -12.86358 | -51.24487 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85bbdfe3-ec6d-3da9-875d-0433f25f6402 | -12.86347 | -51.18977 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 25c048a4-557e-3a3d-8d71-8947b5296fbe | -12.86318 | -51.21982 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 88180445-a173-32ec-9744-d62d2e2a64ed | -12.86289 | -51.24975 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d1b8507-f572-3868-aed3-0b5b7e2241e3 | -12.86278 | -51.19469 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 517c9f20-fa08-359a-80ae-fd69a2a6e856 | -12.86249 | -51.22472 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d5b70caa-06f8-3a5e-930f-06f53e77ba9e | -12.86238 | -51.1695 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 956de199-2a60-3ee1-bbce-f2ff7c49f20c | -12.86209 | -51.19961 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 267.1 |
| bf07cf68-31e8-3895-8276-65c39d93ed86 | -12.8618 | -51.22962 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6d020c21-c224-3e17-8c26-c35fbd2ded86 | -12.86169 | -51.17443 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8b83570-8e83-3dd7-b3ac-867a3ae2daa1 | -12.8614 | -51.20452 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.0 |
| af5c4e97-7c84-3d2c-abe9-6ce30dfe1dd5 | -12.86111 | -51.23452 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a689bcf1-f2cf-3233-b384-7f5464ecbfa2 | -12.861 | -51.17936 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a30e6b8-b030-3ef2-8a92-31b7d4012f0e | -12.86071 | -51.20943 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 75f090d7-bf3a-329e-bc17-52e283e667aa | -12.86042 | -51.23941 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 037136b2-56a5-35b1-9bb6-587a6b414486 | -12.8603 | -51.18428 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 0895e6fc-5294-38a1-b3a1-31db0c016b6b | -12.85973 | -51.24429 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d40433fa-b8ba-3375-862b-452629203da1 | -12.85961 | -51.18921 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e0732061-bf33-35c6-adde-47358c117a20 | -13.64129 | -51.48021 | 2024-09-26 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3312ec6-7255-3185-8ad2-1c72a9671982 | -13.63745 | -51.47965 | 2024-09-26 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5c52f81-f3ca-3520-b1f2-27fe676b2725 | -13.30416 | -51.3448 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ca284e4-d6fd-356c-bf65-33037faebc22 | -13.30219 | -51.34312 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06e315aa-aa11-3658-a16d-d451887a3efb | -13.3015 | -51.34801 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28c7aedb-bae0-3c12-a0f1-eb56f956f331 | -13.30098 | -51.33932 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58ae7977-ff9b-3fe6-9477-da2c79d1113e | -13.30031 | -51.34423 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28989616-7155-3205-a017-ca966d7cbce6 | -13.29965 | -51.34912 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60ccb13f-cf91-3150-8f24-ee90ab79ac0b | -13.29904 | -51.33766 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5228bed-209b-3016-bcfa-6a99b4131b7e | -13.29834 | -51.34256 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9b1910d-74e4-3fdc-af90-9405df6b5779 | -13.29765 | -51.34745 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3667b70-3653-38c8-a338-2f7875a0a43e | -13.29696 | -51.35233 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09416d94-9de8-3484-9d54-7a8f4ce4e180 | -13.29588 | -51.3322 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7c6197d-f997-36d3-babd-50da005bfc07 | -13.29519 | -51.33709 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc926772-1319-3ed2-b76a-740b28d9fe88 | -13.2945 | -51.34199 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 861c5a41-96d2-3f63-b6ab-b30e7cd98582 | -13.29273 | -51.32671 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2bd00ff-1641-3ae7-bcb3-e3bbae90f259 | -13.29203 | -51.33162 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42a79406-e35f-3c71-b016-51ecb6613819 | -13.29065 | -51.34142 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4e1d778-8304-3a02-917b-afbac0014195 | -13.28957 | -51.32122 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5fc463cd-db15-3c95-95f1-f585b4b2b79e | -13.28888 | -51.32614 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faa6433f-3bf3-3d54-ac74-d0e49b3cff5b | -13.28749 | -51.33596 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10fa2429-ab61-32bf-93f8-e3fd84d9a0a1 | -13.2868 | -51.34085 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d47e277-a4ca-3f89-8707-1333278ee884 | -13.28572 | -51.32066 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54d232ba-d203-33d3-bb84-59b288e48d2f | -13.28502 | -51.32558 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b17fb6a7-ba3c-35b9-ad8c-48ed4ac235dd | -13.28117 | -51.325 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83c65438-830b-33a9-b675-ce96a3f7bc01 | -13.27237 | -51.30363 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a3721e0-870c-3a40-a975-20d3d09bebce | -12.87673 | -51.30874 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a94cc5c-9403-325b-9b47-437275654f39 | -12.87449 | -51.3061 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c59b7adc-a200-3f6c-ae20-0e62b4ad51b5 | -12.86406 | -51.32434 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73d1d207-3742-3bbd-a38f-a389a835ccfe | -12.85463 | -51.30811 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14901537-7521-389d-b0c4-dfc169375d8a | -12.85395 | -51.31296 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a66edc7-1ba9-3033-9b12-7c81861e1165 | -12.85011 | -51.31239 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36f9448f-f2ae-37a2-856c-7c9b8ff78c6f | -12.84628 | -51.31183 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3aaa186e-9709-3845-850d-11face4638ce | -12.84245 | -51.31126 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f058243-8ad7-3afa-9f35-1c82f53a3601 | -12.84177 | -51.3161 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dd57c50-22f1-35c9-89ac-95b6f7582f56 | -12.83794 | -51.31553 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08406847-c3b2-3000-9fb9-d4ada7220588 | -12.83683 | -51.29557 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7c55a14-0c91-3b94-8484-0c5c096b2c72 | -12.83411 | -51.31496 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35bc0f8c-7e46-3685-9074-efcc54a976b8 | -12.83343 | -51.3198 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6e9509b-4348-33e9-83f3-4d6b62ec8599 | -12.83299 | -51.295 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 03515a08-ca87-3509-9fde-edc584984ec4 | -12.83231 | -51.29986 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae394712-485a-3a30-b954-614c92eb6a8d | -12.82916 | -51.29443 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| dc99c8aa-6526-3396-9b06-36a0a0f95301 | -12.82848 | -51.29929 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8424b22-ba27-3225-a376-3d7bc0c88362 | -12.8278 | -51.30413 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9123e19b-9d2a-358f-ad26-73de67177e4f | -12.82464 | -51.29872 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 307.1 |
| baf4a0a0-88bd-35c9-b79a-f2377f8d9fa9 | -12.82397 | -51.30357 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 1cf50471-4122-3df5-97bf-f9116faa5298 | -12.82329 | -51.30841 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a29a56a-9a49-3686-91c9-043aa5192a70 | -12.82149 | -51.2933 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 56bbd2d6-7cf1-3d3f-a6d0-f218105875c7 | -12.82013 | -51.303 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 37079ab0-ae14-355f-8146-211a9ecd24ce | -12.81946 | -51.30785 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1acacc53-a7cd-3016-99e8-03cb5313b3fc | -12.81765 | -51.29273 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed6e54d8-a7a7-3bb0-acc9-e0ccb264cac3 | -12.81698 | -51.29758 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 1c4bb8b6-eaca-3485-a1ae-ebe91bed5432 | -12.8163 | -51.30243 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9bb58f0b-13ae-3835-ac0e-c27e6d933aba | -12.81563 | -51.30727 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| bcee58ab-87b6-3cff-8d75-4c1dd74c819c | -12.81382 | -51.29216 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b4ed0c6-8c60-3e28-8b3b-6272f9b326a0 | -12.81314 | -51.29701 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 758a0dd6-1e9b-3e8a-b0fe-01252fea8806 | -12.81247 | -51.30185 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2df9442a-b63e-39ee-9098-e4a2352277f1 | -12.8118 | -51.30669 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7bf6a35e-ae8b-34f8-b5ac-2695af78cc58 | -12.80931 | -51.29644 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6db4f76-2f0e-3d28-b775-bc8f77d1fece | -12.80864 | -51.30128 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9c0b364-2dff-39ac-9272-64784123e826 | -12.80796 | -51.30613 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4daa5884-51a1-395a-95bc-f030b6fedf4e | -12.8048 | -51.30071 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 521fd87b-c27e-3a88-a956-21a6dc8a9fbd | -12.80413 | -51.30556 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 511236fb-47df-3735-8356-4cfcb2ef1265 | -12.79963 | -51.30983 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e319655f-f3fa-38d1-8ea8-1f6b77717f24 | -12.7958 | -51.30926 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0505d6d9-9d37-388f-9db7-60fa14aa1fbb | -12.77333 | -51.3386 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README120.md)
