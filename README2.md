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
| 6a0541cf-1807-39f4-aacb-4ad7f5a344c6 | -23.6588 | -51.6867 | 2025-10-21 00:30:00 | GOES-19 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 49.5 |
| b5b5945f-2fd6-3747-9e8f-08a84856f574 | -3.2321 | -46.7836 | 2025-10-21 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 0bf25638-77f2-39d2-a90a-5eff0cb6ce21 | -4.6277 | -46.4105 | 2025-10-21 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7959468d-99f2-3d2e-ad1d-bfda4f0ffbce | -3.5154 | -45.8187 | 2025-10-21 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 163.0 |
| a585e6fc-5c4b-3ac8-90b3-a66c3ba025f0 | -9.0222 | -65.922 | 2025-10-21 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 21f3274d-08d6-39b1-bd0b-f8690acaeafb | -3.4968 | -45.8195 | 2025-10-21 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 242.3 |
| edb5221c-1ea1-386c-a6a6-48aa9c78ff47 | -3.9739 | -50.3644 | 2025-10-21 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b5e067ac-e58f-3f4d-b68c-ec4cb92d6cdf | -4.3879 | -43.3129 | 2025-10-21 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1b0749e6-0c53-3058-8121-9fd7a3888b05 | -3.5153 | -45.8411 | 2025-10-21 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 11494674-dc61-3896-bdba-3234a5b74d6d | -8.9851 | -65.9232 | 2025-10-21 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 07107ee1-004d-3cbb-87e1-77ea4c42ea83 | 1.7119 | -55.7248 | 2025-10-21 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b9895093-2efb-3b73-9045-10cb2d71f06f | -9.0036 | -65.9226 | 2025-10-21 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 262.7 |
| 89b612fe-129e-3744-b708-3942226a888b | -3.8515 | -48.9714 | 2025-10-21 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 4c91f632-e5e3-32c3-8fd0-66d18fc26d06 | -6.7399 | -44.1602 | 2025-10-21 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9db878f1-5f8e-32f4-aafb-026087597ead | -3.8516 | -48.95 | 2025-10-21 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| cc8a0644-8516-3727-9d99-7411b5d56594 | -3.3441 | -50.7426 | 2025-10-21 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 542b708f-431c-3715-aa4d-e1b5d60b654b | -17.6852 | -52.2398 | 2025-10-21 00:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| bf11807a-aa28-3a70-9922-73ca16ee36d4 | 1.7119 | -55.7051 | 2025-10-21 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 67bd9104-7d9b-38a8-896b-dac751702ef6 | -4.6649 | -46.4084 | 2025-10-21 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 060d437b-7030-37a2-bd11-d21cef7e5af2 | 1.6936 | -55.7251 | 2025-10-21 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 52e56aa2-bbe3-3afc-a220-e9e8c9089046 | -4.6463 | -46.4095 | 2025-10-21 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 191.4 |
| 4e6f4fe4-70a5-388f-a9d4-7347a6ab0252 | -4.6461 | -46.4316 | 2025-10-21 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 3aeb7d03-3d48-33c3-8e47-4e4a3b5bf924 | -3.4967 | -45.8418 | 2025-10-21 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 32c05e3e-1f88-3b1d-8d07-ca7ec8b6ac2e | -9.0037 | -65.904 | 2025-10-21 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 14ef5b4f-2567-3251-a41a-b3bb1e036774 | -3.9923 | -50.3636 | 2025-10-21 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e1b1d49a-2a98-361e-abe9-93cbab471f62 | -9.0221 | -65.9407 | 2025-10-21 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6a92bbca-9ff7-3a63-91d1-ce8d1b0ddcd8 | 1.7303 | -55.6851 | 2025-10-21 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 73130681-0e43-3921-9400-e9898ce0cb3e | -3.8701 | -48.9493 | 2025-10-21 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 13e102d7-1a1d-3e27-a578-8c6649c46e6d | -9.0036 | -65.9412 | 2025-10-21 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.7 |
| bfb5b8f0-dce4-351d-b90f-0612f1054a4f | -3.5154 | -45.8187 | 2025-10-21 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 6045f5ab-38ff-3e34-ae8f-85e9825368b8 | -3.2136 | -46.7843 | 2025-10-21 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 61dfad84-ec08-33d6-bd38-079439539549 | -9.0037 | -65.904 | 2025-10-21 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 69ac98e0-6290-3bd5-b660-50551281902f | 1.7119 | -55.7248 | 2025-10-21 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 68496df2-d7bb-33bf-a3ae-ec9fbe7cdd0f | 1.7303 | -55.6851 | 2025-10-21 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 23c8f4e0-0c66-3bd1-8b6c-ba3b9c9ba836 | 1.7302 | -55.7049 | 2025-10-21 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 9d5295b8-7e4a-3b62-9fc4-bc2c8f85d70c | -4.6277 | -46.4105 | 2025-10-21 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 7f40f3a2-6d00-3708-8fd6-2fc946847470 | -6.0165 | -43.3161 | 2025-10-21 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 66.4 |
| bd7b35d2-ceb1-3c08-9e51-4c8ec315f82c | -17.6852 | -52.2398 | 2025-10-21 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 47208b6a-e915-3d1e-8bcd-6d5903ab87a0 | -4.6464 | -46.3873 | 2025-10-21 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7a18854e-0a9b-38de-a367-8db5520e55c0 | -4.6461 | -46.4316 | 2025-10-21 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9307af47-88b8-3f5b-ad25-31bc5e0e79e6 | -6.1935 | -42.5022 | 2025-10-21 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 2f21d0b1-e331-3c73-ae27-4e8b50e8bdd3 | -17.6847 | -52.2615 | 2025-10-21 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ab6a163d-5305-36d4-8e01-afc24d3b7100 | -3.5153 | -45.8411 | 2025-10-21 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 117.6 |
| d103b517-6740-3cb9-ba15-de77020363b9 | -4.6649 | -46.4084 | 2025-10-21 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| dcfb85e1-bff5-30e3-be22-c985f3698d36 | -9.0221 | -65.9407 | 2025-10-21 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| fa537db0-d9c3-30a6-81e9-a2d61e56ea9b | -16.1778 | -49.977 | 2025-10-21 00:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5b3e6a14-fa92-36eb-970a-a532d366014e | -3.4968 | -45.8195 | 2025-10-21 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 257.0 |
| 7584e7dd-999b-30f4-984c-f653213343f6 | -9.0222 | -65.922 | 2025-10-21 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 231651e9-06e3-307d-b6dd-ddf6738204d1 | -4.6463 | -46.4095 | 2025-10-21 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 243.3 |
| 549746d3-60e8-35c9-bad7-68f680efcfab | -8.9851 | -65.9232 | 2025-10-21 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b1f58ef1-1a99-3478-9b5e-28039c52cb19 | -6.7213 | -44.1387 | 2025-10-21 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 195d9bfa-20f0-33a2-b619-ea70893037b3 | -6.7401 | -44.1371 | 2025-10-21 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6a1ad720-80be-3d5e-b071-6cff41fa7b05 | -9.0036 | -65.9226 | 2025-10-21 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 260.5 |
| b1cf59fd-aea8-32e2-9077-a683344fd6b8 | -6.6534 | -43.4489 | 2025-10-21 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8f24096d-2162-39f8-b269-c580726c2dd6 | -3.4967 | -45.8418 | 2025-10-21 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 164.6 |
| f5a46611-3d16-31ad-a770-fe3f30dc2dee | 1.7119 | -55.7051 | 2025-10-21 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 60847e4f-cd00-3eda-9a4c-8de3c64b4d84 | -3.2321 | -46.7836 | 2025-10-21 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2c81e326-0379-3bec-9a2f-01769eebb6cf | -3.3441 | -50.7426 | 2025-10-21 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| ba378806-324e-378a-9f40-d3abc8008366 | -6.6537 | -43.4256 | 2025-10-21 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| dd0a46a6-a32e-3594-a4a4-b72a62b65559 | -6.1932 | -42.5259 | 2025-10-21 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 50bd671e-7c60-3464-9e13-8360a3318a56 | 1.8219 | -55.6444 | 2025-10-21 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 30ee22fd-cc5e-3221-824c-c5e0eb52b4e8 | -9.0036 | -65.9412 | 2025-10-21 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| fe8f74d7-8697-3627-9ae7-6421c6fd6d2d | -4.6461 | -46.4316 | 2025-10-21 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7c9fceb7-653f-3fb3-a74f-4b65f699b704 | -4.6649 | -46.4084 | 2025-10-21 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 2b4cba47-d22b-3543-b727-3c31c3d11b0f | -3.5154 | -45.8187 | 2025-10-21 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 27ad7580-79eb-3e06-8101-6c48ed067f65 | -9.0221 | -65.9407 | 2025-10-21 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b3aa2c8a-0b47-328b-88ff-b30ea85ce7a4 | -17.6852 | -52.2398 | 2025-10-21 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 26b69a87-4410-398d-b5c7-cf994a2c6969 | 1.7302 | -55.7049 | 2025-10-21 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 37d0cf23-3533-3fd9-88ac-95600a019edb | -3.2136 | -46.7843 | 2025-10-21 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6887ce18-e7b0-3582-868b-bc11cfcfe82e | 1.7119 | -55.7051 | 2025-10-21 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2046b7ca-52e6-3159-8f4b-24b6cd4dd824 | -3.8516 | -48.95 | 2025-10-21 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 2db21762-f760-3ed7-bd9d-93ace3edcdaf | -3.2321 | -46.7836 | 2025-10-21 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f5dfffdf-48ea-3b27-8661-23c8a02f8498 | -4.6463 | -46.4095 | 2025-10-21 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 185c7764-e52c-3216-82f0-8df0a23cfd90 | -9.0036 | -65.9412 | 2025-10-21 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 5564a2a1-0446-3b19-90a7-cd4a85bbb1d1 | -4.3879 | -43.3129 | 2025-10-21 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 12ec6763-6ade-3403-b1ff-c5520a75ea55 | -17.6847 | -52.2615 | 2025-10-21 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| beb396c6-e314-3bd2-9652-ef4a18f73f50 | -9.0222 | -65.922 | 2025-10-21 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 63580b54-26c0-3d80-937d-d73dd318aa55 | -6.6537 | -43.4256 | 2025-10-21 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 298d1c6e-9a13-3918-883b-00b694359ccb | -3.3441 | -50.7426 | 2025-10-21 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e0675271-2977-382a-9c8b-13fa69be5c41 | -3.4967 | -45.8418 | 2025-10-21 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 139.7 |
| a05b84ca-2e97-332b-b127-9c755743610f | -4.6277 | -46.4105 | 2025-10-21 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 27fd5d25-2845-3991-b444-01e8955b66b5 | -8.9851 | -65.9232 | 2025-10-21 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| f76518d9-5ccf-3699-ba61-bc2cf780457c | -3.5153 | -45.8411 | 2025-10-21 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 22e5cebd-0d85-3a8c-a1d5-d7b585ff3073 | -9.0036 | -65.9226 | 2025-10-21 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 254.3 |
| 3cbfe20d-bcb7-38ee-b6f4-1df47f63c033 | -3.4968 | -45.8195 | 2025-10-21 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 296.4 |
| c168c249-36ac-3c96-8095-cb69413faea1 | -4.4969 | -46.4839 | 2025-10-21 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f14861e6-6763-3202-8e60-37e72113a1cf | 1.7119 | -55.7248 | 2025-10-21 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 21dc3399-a28a-334e-a2c0-64394a0908b9 | -3.8515 | -48.9714 | 2025-10-21 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| a68e7da0-f72a-36dd-9094-0df3d61ed161 | -4.6464 | -46.3873 | 2025-10-21 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 89e4c518-43b4-3693-b71f-388fa12255ac | -9.0037 | -65.904 | 2025-10-21 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| f6b07432-ec27-3b2b-a414-f0666ff94743 | 1.7303 | -55.6851 | 2025-10-21 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 49cb8f4d-4450-322c-9b39-05167b1756a1 | -3.4783 | -45.8203 | 2025-10-21 00:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| c5de0fa0-730a-318d-acf5-f4e19c94882c | -3.5153 | -45.8411 | 2025-10-21 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| c8ff79a1-9ee0-39db-ad4a-c8e901338744 | -17.6847 | -52.2615 | 2025-10-21 01:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a3a7aa92-a549-3777-a55b-4d70c945b2c0 | -3.2136 | -46.7843 | 2025-10-21 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| a9d3a5dc-336e-3798-a78c-c49ed8e291e4 | -4.4969 | -46.4839 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0233ecfe-c1ea-31de-96a8-ba307482e007 | -4.6463 | -46.4095 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 1ee5fe9f-1366-3ac2-b5af-0b0ff50f3f0f | -9.0036 | -65.9226 | 2025-10-21 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 229.5 |
| d9465c54-3afa-30d1-abb3-a74d7e679cd6 | -3.4967 | -45.8418 | 2025-10-21 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 1de9f61e-d891-3607-9d8b-10589f30b711 | 1.7119 | -55.7248 | 2025-10-21 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |


[Clique aqui para ver as próximas entradas](README3.md)
