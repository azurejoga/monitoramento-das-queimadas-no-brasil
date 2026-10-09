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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 139e362f-7bf0-3e71-bba3-378706b1a843 | -4.6096 | -49.2156 | 2026-10-09 02:20:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 497720f7-142c-3a21-86d9-d27abc8b5389 | -11.6173 | -43.7142 | 2026-10-09 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4961d48a-589b-3ef3-a52c-237e960ccf1f | -3.1285 | -54.1657 | 2026-10-09 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ae1d3cb0-c194-368b-9412-0499700318e3 | -12.2154 | -57.1287 | 2026-10-09 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8d796d35-0d18-3c54-92e4-b0a535efeeea | -8.7068 | -62.3995 | 2026-10-09 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 2da62b5c-ebe2-3d98-9d28-deb609960617 | -6.021 | -40.9577 | 2026-10-09 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| df0acdf1-3375-34ff-a557-5d07a3696f72 | -2.7428 | -54.1146 | 2026-10-09 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b6459021-7979-3f94-82c2-3d93cdb75f04 | -3.1284 | -54.1857 | 2026-10-09 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0ac344cb-2a96-3737-952f-fba8e54dc082 | -3.1787 | -50.5807 | 2026-10-09 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5c77b7c4-4e21-3f56-9375-87e36ea3cce6 | -5.9833 | -40.961 | 2026-10-09 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 6e7fe3a5-33f9-357d-ab6d-170b18db2488 | -3.0925 | -53.9455 | 2026-10-09 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7d5dfd0c-ddce-3fc3-90ba-7f1c207f5a6e | -8.7067 | -62.4184 | 2026-10-09 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d5b0e5cc-7e3f-3f18-be9a-198021300d09 | -3.5676 | -54.6946 | 2026-10-09 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 89382340-b824-31f8-a234-fe57a3c29b63 | -5.7119 | -53.4658 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a0fea06e-fa4c-3aef-8302-ef5d8db9a874 | -12.2158 | -57.0887 | 2026-10-09 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 58e6a968-4fec-3048-9ab4-8d5ed0968985 | -5.6932 | -53.487 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 54257bf0-4260-327f-a790-7856dae11f60 | -10.6199 | -60.4852 | 2026-10-09 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 032edd7b-3728-32f0-b494-3d7ddfff2afd | -6.7365 | -55.1474 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9830ce1b-f55b-347f-9abf-40227b85b5ed | -3.1101 | -54.1661 | 2026-10-09 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| dda17d64-91ad-36fc-89f2-7bfc4f55768c | -12.2348 | -57.0871 | 2026-10-09 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fba47f7a-009c-3e29-8a94-d7bd5583a798 | -5.7117 | -53.4862 | 2026-10-09 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6d313c0d-8585-3e8b-b499-520c0a88384f | -7.5834 | -61.5516 | 2026-10-09 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 0db7f52d-b252-300c-b300-35d8462e9138 | -6.0207 | -40.982 | 2026-10-09 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| b6e5e816-cd9d-3a4c-aeda-acb07f6b4e53 | -3.0007 | -53.9075 | 2026-10-09 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4e22166e-0101-3839-8cd4-863d0a0d598d | -9.4769 | -40.3365 | 2026-10-09 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 8ab19c23-6b33-343e-ae55-507aa989b3b2 | -10.6012 | -60.4863 | 2026-10-09 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d6cd76ab-75fb-3b1c-ac95-005200f89da4 | -6.0021 | -40.9594 | 2026-10-09 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 275.8 |
| 38cb680d-edeb-3bf5-bfbb-59c82c9e7571 | -9.2549 | -60.8863 | 2026-10-09 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2540d34e-2e55-37a6-bbe9-dc3c4b120ce6 | -8.7234 | -45.1355 | 2026-10-09 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 198.3 |
| f87cf94b-ab0a-3839-9f71-c18e804cb99b | -7.1995 | -55.1627 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2f3bbf98-9915-3635-ba52-7502752daa17 | -8.7231 | -45.1583 | 2026-10-09 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 59c9493f-a099-37ca-bb76-59f5f62c9795 | -10.6201 | -60.4658 | 2026-10-09 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 884e436f-ae28-328e-bb6d-c855ea07497e | -9.4574 | -40.3641 | 2026-10-09 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.0 |
| daef9dc9-5e24-36f5-b626-97fed851ac04 | -5.7119 | -53.4658 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 11fdfabf-4bfb-34b0-9905-a0be5c2dac34 | -6.7365 | -55.1474 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f1493641-37e0-38a6-9b8e-2258eb06a4c7 | -8.742 | -45.1563 | 2026-10-09 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 6c5f5b49-76fd-3dd6-ba14-ef7a72f7b070 | -6.0024 | -40.935 | 2026-10-09 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| d16894c0-7d9d-3ef5-ada6-005390a7ffd2 | -9.4578 | -40.3392 | 2026-10-09 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 0b12aef1-47a2-3651-ac66-6f90ec7445fd | -3.1114 | -53.7839 | 2026-10-09 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c89ddfd7-99bf-3dbd-a879-52997fc62e85 | -7.218 | -55.1617 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f4411a43-a352-3d9e-a314-86eb88ae6456 | -8.7068 | -62.3995 | 2026-10-09 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 98d0e06a-e970-3334-a557-520a72afbcac | -3.1284 | -54.1857 | 2026-10-09 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d4bc71cc-4a6c-39e4-af07-eb75d4adbdac | -3.9912 | -59.356 | 2026-10-09 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 47e9e8f8-c32c-356a-8842-6e7848cbe2a2 | -13.1639 | -54.3385 | 2026-10-09 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 46d55c48-19d8-3d17-98ba-a40949d6023b | -13.2662 | -42.2365 | 2026-10-09 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 72.6 |
| de588fea-7365-3106-9043-4636ea17e6bc | -3.3455 | -50.4078 | 2026-10-09 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bf3f8ef9-adb9-30b5-8b07-58aca9b16240 | -8.7423 | -45.1334 | 2026-10-09 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 323.3 |
| e1a47327-3133-3270-a607-ced6aad07efa | -13.1636 | -54.3591 | 2026-10-09 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5416e018-6d85-3cc0-ba37-5343c80b9005 | -3.1285 | -54.1657 | 2026-10-09 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 64587f91-8e57-3b11-a357-d0de867a71a9 | 2.4216 | -50.8307 | 2026-10-09 02:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 1d64df34-44a5-3fae-9f0f-e6c078316431 | -6.7363 | -55.1675 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| eb4fa3a5-919d-32b4-b758-f670d69c72c9 | -5.6934 | -53.4667 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a42222ac-3286-3a4d-9001-dfb73721efdc | -7.2182 | -55.1416 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d1062287-b043-3138-b9aa-ce9c2edff662 | -6.021 | -40.9577 | 2026-10-09 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 23e9eece-0824-38f7-856c-b9b96f288f8d | -6.0019 | -40.9837 | 2026-10-09 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 152.0 |
| 87926f27-e240-3974-b97f-67f9370c1df5 | -3.1109 | -53.945 | 2026-10-09 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a2afb5ec-d956-3783-b732-9f08ddfe083f | -3.0007 | -53.9075 | 2026-10-09 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 01cef85b-a55e-3f98-89dd-c36a14d28780 | -3.2576 | -54.0418 | 2026-10-09 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a57c562e-d749-3f69-8bc3-5f728a41fe95 | -7.5834 | -61.5516 | 2026-10-09 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c14420aa-17f4-3884-894a-c28747d423fd | -6.0207 | -40.982 | 2026-10-09 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 9a815511-540e-319f-a2b2-0ba7dab8935b | -8.7067 | -62.4184 | 2026-10-09 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| bc711c07-d5ad-30f7-b375-d61fe5c588d1 | -5.7117 | -53.4862 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 63be5ef3-ebf5-3553-a9cc-8788cf9a3919 | -9.4769 | -40.3365 | 2026-10-09 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.0 |
| 03f6defb-ce74-3aa4-abd9-a62cf52f5e45 | -7.2187 | -55.0815 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 90ae237d-0d9e-3f35-9f62-8525c225bfe4 | -10.6199 | -60.4852 | 2026-10-09 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c801cfbd-eca9-32f7-86a6-0458c44ab759 | -6.8907 | -45.8988 | 2026-10-09 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a7b89df3-6f45-3a7c-8a0f-e1a076e97f61 | -3.5493 | -54.6951 | 2026-10-09 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| df4f16ce-2d0a-31a8-8a71-0dc9f3b94c63 | -10.6012 | -60.4863 | 2026-10-09 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 07cd0ddd-5ab2-3a00-aee9-529ad649d868 | -9.4765 | -40.3613 | 2026-10-09 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.8 |
| d7eafbad-dd31-365a-a862-a94653a1820e | -3.11 | -54.1862 | 2026-10-09 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c124a751-3903-3eb1-815a-bd6ec62c9e57 | -7.4442 | -63.5589 | 2026-10-09 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a9cccfa4-01a7-3b7b-926b-893efea3be8d | -8.5183 | -67.0325 | 2026-10-09 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e5868dc4-bbac-3ab8-9d36-f60ab576c241 | -11.6562 | -43.6846 | 2026-10-09 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| c82782ec-4ca0-3907-8f0a-1c2bfb189bae | -3.5493 | -54.6752 | 2026-10-09 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7cbd2dde-75de-36bd-abc3-649ffa8bf5d2 | -2.7428 | -54.1146 | 2026-10-09 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6f2881bd-3f73-352d-a1de-f6260957bb99 | -3.1101 | -54.1661 | 2026-10-09 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 1669bf36-9340-33c9-9237-76329cf6bebb | -7.2367 | -55.1406 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| de31c9cd-d808-3b99-bd61-297d898c1b4f | -2.499 | -56.0675 | 2026-10-09 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6a387d18-0e3b-3518-b3e3-a133e48a870d | -9.6867 | -58.0865 | 2026-10-09 02:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| adc2ae9b-9083-304c-8b2d-1c6824120dab | -6.0021 | -40.9594 | 2026-10-09 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 339.3 |
| 04972fb9-9fba-3d52-990b-640e97b99169 | -8.7612 | -45.1314 | 2026-10-09 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7a950778-2726-3d92-8d43-78fc4d8b852f | -5.6932 | -53.487 | 2026-10-09 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2ba1801e-e97a-343e-a6ed-d43fc6034243 | -3.0925 | -53.9455 | 2026-10-09 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 85a4b96e-b507-3582-b5bb-9139c12b4e41 | -13.1827 | -54.3571 | 2026-10-09 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 99c10ae4-b118-34a9-a731-a74d55404144 | -3.5676 | -54.6946 | 2026-10-09 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| ca66094e-f97d-3cd9-9432-26588aeab867 | -3.1787 | -50.5807 | 2026-10-09 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 87cd2b68-2b51-3eda-9ca6-7eba4210c707 | -5.9833 | -40.961 | 2026-10-09 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| df464acc-9b79-31e9-b151-6dfa8aa64cc3 | -3.5677 | -54.6746 | 2026-10-09 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 507eea9e-92ed-3ec4-bcf8-f8671b8665bb | -7.5834 | -61.5516 | 2026-10-09 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 634236d6-42c2-3925-b22c-fa763c2a3de9 | -5.7117 | -53.4862 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 728934e2-90a9-3792-908c-cd4d94518855 | -6.0207 | -40.982 | 2026-10-09 02:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 3677422a-6f7c-3327-a4a4-bb7bf78d6522 | -3.0925 | -53.9455 | 2026-10-09 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ad30b562-8221-3aee-8f73-ce6a4610d4c2 | -10.9953 | -45.4068 | 2026-10-09 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 1181fca2-b9f2-362c-899c-44c518730da7 | -2.499 | -56.0675 | 2026-10-09 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b833f531-6a71-3646-919a-7a95dcafba4f | -7.2187 | -55.0815 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2bbb2366-1c39-3b34-aee5-c1df614141aa | -3.2576 | -54.0418 | 2026-10-09 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fb89fa12-66ea-3338-b2a8-37118faccd84 | -9.4769 | -40.3365 | 2026-10-09 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 201.2 |
| c759e17a-789b-3ba2-adff-f2e92d02daa1 | -9.4578 | -40.3392 | 2026-10-09 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 260.5 |
| 7af835ec-c3fa-3ff3-a28e-f8c4d37a9a7e | -13.2657 | -42.2609 | 2026-10-09 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 135.9 |
| 26d363b4-0dca-392d-a317-8f602b9746f6 | -7.2182 | -55.1416 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |


[Clique aqui para ver as próximas entradas](README53.md)
