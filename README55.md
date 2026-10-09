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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cbd7cb0-d90a-3585-8c7d-217e35457ed2 | -6.021 | -40.9577 | 2026-10-09 03:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 173.1 |
| ec0afd71-4213-3da4-a7f8-c576deef88be | -3.11 | -54.1862 | 2026-10-09 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 13005cfd-4a53-354c-b473-d752e9fb3ccd | -8.7423 | -45.1334 | 2026-10-09 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| ef5717b3-faca-3548-9dbe-766b32d95544 | -13.2467 | -42.2401 | 2026-10-09 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 229.2 |
| ca897c51-078c-380b-a338-002e4699350b | -13.2657 | -42.2609 | 2026-10-09 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 9a4692b0-18a7-357b-b993-c776591002d1 | -3.5676 | -54.6946 | 2026-10-09 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 287bff27-875b-3c5a-b9df-33213fa982d0 | -3.5493 | -54.6752 | 2026-10-09 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c23d5943-2731-3a7b-a26d-a5790fd2b466 | -3.0925 | -53.9455 | 2026-10-09 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 79894520-690a-3772-b7ef-23a5389bf204 | -3.0007 | -53.9075 | 2026-10-09 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 304ade56-3c16-380d-a911-1c487abfe854 | -10.8789 | -45.5368 | 2026-10-09 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 64e592de-bc2a-3f76-b347-2c0e087dc6e0 | -3.5493 | -54.6951 | 2026-10-09 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| c77b979d-1645-370a-ba39-69656c5a3727 | -13.2662 | -42.2365 | 2026-10-09 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 147.1 |
| 9ec958af-51d6-3e84-ba04-403b83437e86 | -8.7231 | -45.1583 | 2026-10-09 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 7e5b8fb4-4ef1-3b8f-8efa-45c364b2a77f | -2.7428 | -54.1146 | 2026-10-09 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5aa60587-e994-39e8-9a20-0796d239d2ba | -13.2462 | -42.2645 | 2026-10-09 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 156.5 |
| ccbcdd3b-d9b9-34e1-8c49-1d81905a6028 | -8.742 | -45.1563 | 2026-10-09 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b3153e85-1074-3220-8e82-1b309479a8bb | -8.73 | -45.15 | 2026-10-09 03:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 042ea923-d0ba-3270-b8b1-4c15537180c2 | -5.99 | -40.97 | 2026-10-09 03:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d8c81e1-c822-3ffd-bb1f-891763f41030 | -9.47 | -40.34 | 2026-10-09 03:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 70cb6a81-53c4-3f5f-a40d-4cf348a83e1c | -9.45 | -40.34 | 2026-10-09 03:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 23b67f6f-9a0c-319f-9979-4ce15c239e21 | -13.25 | -42.29 | 2026-10-09 03:15:00 | MSG-03 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41d4802d-e582-3cb9-8fa8-bbe5eed8358d | -13.24 | -42.24 | 2026-10-09 03:15:00 | MSG-03 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8ad930a8-dded-3595-a51d-8b96e7044ad1 | -9.45 | -40.38 | 2026-10-09 03:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9e5ddb3f-8151-377e-9812-e22fe420fe0a | -13.2467 | -42.2401 | 2026-10-09 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 140.7 |
| 8520913e-3601-3e57-a552-ae279b045e69 | -3.1101 | -54.1661 | 2026-10-09 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c554b6d6-d57e-3f1f-a4e7-525e6b8c4a15 | -6.0021 | -40.9594 | 2026-10-09 03:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 577.8 |
| 21d6500a-6270-3153-9803-7e02ecfb0ce4 | -5.6934 | -53.4667 | 2026-10-09 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 4082f0c2-d1da-372f-aa62-c0a8ee70c2e9 | -13.2662 | -42.2365 | 2026-10-09 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 0f24e9e5-7267-3073-9260-fed7d6081203 | -12.2348 | -57.0871 | 2026-10-09 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 25a8ca5e-533b-308c-b1c6-f044498eb37a | -12.2156 | -57.1087 | 2026-10-09 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 247de776-4034-39f7-a40f-e3ac940d03a1 | -7.2182 | -55.1416 | 2026-10-09 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b6a0ff1c-87d6-3957-a28f-3256c74f63ef | -13.1827 | -54.3571 | 2026-10-09 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e13cd9d0-8a56-3def-aaf8-66be70a79acc | -3.5493 | -54.6752 | 2026-10-09 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 27ec3bf9-fa75-320c-a6b0-91eaed3004dc | -3.5493 | -54.6951 | 2026-10-09 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c0116ebe-e08b-3dcc-8725-7d21160c6342 | -8.7231 | -45.1583 | 2026-10-09 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| aef4c565-9811-3506-8f11-8cc877594e8c | -3.0007 | -53.9075 | 2026-10-09 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| bb03af6f-a3b1-36f9-a38b-ce6f56aefca7 | -13.2462 | -42.2645 | 2026-10-09 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 112.8 |
| be7efa12-e4fa-3e56-9e0e-5d38c87fd0e6 | -8.742 | -45.1563 | 2026-10-09 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e3e209b2-dd9e-343c-9203-04c3174c00f2 | -12.2346 | -57.1071 | 2026-10-09 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 174.5 |
| f518867b-76ab-3e4e-ad41-9e00aeb58168 | -6.0019 | -40.9837 | 2026-10-09 03:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 278.5 |
| 3022a7ed-0ac0-3038-8037-3b337bd86bdd | -7.1995 | -55.1627 | 2026-10-09 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1f5db5f0-a14f-35ce-bd0c-4b7d65d52026 | -2.499 | -56.0675 | 2026-10-09 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| b725eb61-da87-364f-ac21-89a0ee9e7259 | -8.7068 | -62.3995 | 2026-10-09 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 9698ac8d-8882-35b8-8bfc-614cdfad2c48 | -8.7067 | -62.4184 | 2026-10-09 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 949121f9-cfc4-3c04-955f-c41c5a6061e0 | -3.1284 | -54.1857 | 2026-10-09 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 26878acf-e8ee-34c4-bc5f-cd14e742469e | -8.6882 | -62.4192 | 2026-10-09 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 79c2fb7d-227d-3832-bfcc-1c386b9f5caa | -6.8907 | -45.8988 | 2026-10-09 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c8403c2d-00d1-39f8-ae13-72ecff284938 | -7.218 | -55.1617 | 2026-10-09 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 019e6059-50dc-347d-91b4-74f50000d681 | -3.1109 | -53.945 | 2026-10-09 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b8410795-cc18-323b-ad13-4b240fffd4dd | -3.5677 | -54.6746 | 2026-10-09 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 2061a0ae-b7bf-3d6d-b915-66d4d40953ec | -8.7234 | -45.1355 | 2026-10-09 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4ed95e03-7d9e-3f2b-af31-1ea035c6dfaf | -3.0925 | -53.9455 | 2026-10-09 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 85765899-8462-3d58-be32-5994c0f22707 | -6.021 | -40.9577 | 2026-10-09 03:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 191.5 |
| 40d4fd86-f39f-32bd-bda8-cc23c79c07fa | -6.1485 | -47.2871 | 2026-10-09 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 149ad3d7-7082-37ef-9f2b-b5cb9f2d1ab8 | -11.0144 | -45.4042 | 2026-10-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 95e94a47-86c3-328b-8f65-6ef25438ff50 | -3.1114 | -53.7839 | 2026-10-09 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 48fc4650-1848-3333-bd19-57d9e0e9fb40 | -6.0207 | -40.982 | 2026-10-09 03:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 901c38e5-2255-3672-b0e5-a9524c88cd41 | -2.7428 | -54.1146 | 2026-10-09 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e385a4a1-8967-37dc-8d18-fdc2e471e4a4 | -6.1674 | -47.2638 | 2026-10-09 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 00aa9431-2b73-36a9-b98c-a448f2b57bb5 | -4.1039 | -54.0164 | 2026-10-09 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ea128f47-8bb6-3aa3-b937-a55186f9f5b4 | -3.11 | -54.1862 | 2026-10-09 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1d85bc27-5150-319d-bceb-39f180891258 | -2.823 | -58.2838 | 2026-10-09 03:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 2d835fed-cb65-3149-b24d-eefe5d654d4f | -13.2657 | -42.2609 | 2026-10-09 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 0b037689-4eda-3e7e-a647-16bd77bac30f | -3.1285 | -54.1657 | 2026-10-09 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 1042ba38-c1b3-32aa-a2df-4859ee6915c7 | -3.1787 | -50.5807 | 2026-10-09 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 00cf8bbd-b4cc-386d-9ede-0d5eb2bfe9f0 | -6.0024 | -40.935 | 2026-10-09 03:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 163.7 |
| c2a085f2-fb5f-36d2-9ede-a52e1c83c6a8 | -6.8719 | -45.9003 | 2026-10-09 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b8f375ec-eb9e-3d6d-a6a3-5ec6fddd5257 | -12.2158 | -57.0887 | 2026-10-09 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| c7572d8b-1068-31d3-8b2e-8ec5a7d19731 | -11.014 | -45.4272 | 2026-10-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 57264dbd-f66c-3b9f-9fc2-2a9b692cb4fe | -13.1636 | -54.3591 | 2026-10-09 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9d62a334-896b-3c6d-8773-f4afec484382 | -6.1487 | -47.2651 | 2026-10-09 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 567fdc02-948d-363c-ad09-8c8fbf42a602 | -11.3103 | -44.8337 | 2026-10-09 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 63045a1d-1c71-3b7a-8892-904e52bfe45c | -8.7423 | -45.1334 | 2026-10-09 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| e1680904-b52e-3a34-bfc1-ba90af142028 | -5.7117 | -53.4862 | 2026-10-09 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 886ceb97-a91e-3bd8-97b0-7e08e86de183 | -3.5676 | -54.6946 | 2026-10-09 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c74c10f5-71bb-3b0b-ac13-beeee2d81947 | -6.1672 | -47.2858 | 2026-10-09 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0ba8ddf2-8b1a-38b6-a67e-119b05b37416 | -7.6409 | -35.01047 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 6501b1b6-1ee6-386d-ab69-bc62c125e5f6 | -7.40887 | -35.19369 | 2026-10-09 03:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| fb698425-b131-38f0-a99c-2998179f872d | -7.63865 | -35.01663 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6fb25a6d-2b45-304a-b62f-596575619c70 | -6.01441 | -40.97649 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bb45896a-085a-36f2-a9d5-fd494314d6fb | -5.99854 | -40.94238 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 78eabafb-17a6-32de-a146-ee389d4a444d | -5.99722 | -40.94952 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f15a05bf-a8c2-3d85-ba82-f4a47a06ee3f | -7.63611 | -35.00958 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e30c828d-2574-32b4-853d-63ebf6111c4a | -6.00431 | -40.96561 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| c9945c8e-65e9-3952-84eb-e2c3db217e5c | -5.99859 | -40.95691 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| dac1a0ab-6aea-38ac-8c1d-0d2d4b76615e | -6.00133 | -40.94267 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3f7ba794-d3fe-3f33-b488-9ccc40e54a07 | -5.99184 | -40.97844 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f2dc9023-fded-3571-a651-68be09c8ef4b | -6.01 | -40.96034 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 43f028f9-1253-36a6-a863-5b4687e9ec8c | -6.00871 | -40.96729 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 753d695c-c360-35ec-ba50-5ee085ea7556 | -5.9972 | -40.96411 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e45d3457-d0de-36c4-bbef-9d47f17303ac | -6.00428 | -40.95128 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 08dbeeae-7ec5-3fa8-ae22-08bb139b7f7b | -5.99588 | -40.95672 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8debf02f-13f0-32d5-b650-8436efdfbd9f | -6.16231 | -39.44245 | 2026-10-09 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d8fffa1a-5532-3cfc-b446-02877edc1fea | -6.00032 | -40.97264 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 98d43463-f00c-3060-a4b3-df37e5d48cf6 | -5.99306 | -40.98565 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4786e28c-75f6-38f9-916b-9a504cbb00a1 | -5.99452 | -40.96405 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9726fcd5-3e6b-3a69-b009-9871342325f3 | -5.99582 | -40.97129 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| da71fccb-9a0a-317a-af2a-524f946baed9 | -5.99899 | -40.97981 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| d4ce6b1a-e6a5-372a-9c74-f73d16b06321 | -7.64656 | -35.00628 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| c512c83c-979f-3f34-9b64-2b8e2651ab08 | -6.16129 | -39.448 | 2026-10-09 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README56.md)
