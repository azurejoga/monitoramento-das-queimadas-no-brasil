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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 348d3dcc-09a1-38cc-b473-c9dea2ad87a2 | -3.1114 | -53.7839 | 2026-10-09 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 738121c4-2005-3236-8dd5-7bed9dee426b | -8.9684 | -45.177 | 2026-10-09 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d0daab50-e7b3-392c-9006-2717e3819cd9 | -7.2187 | -55.0815 | 2026-10-09 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 257d68e6-12d0-3eb6-8f32-53fa9ced6111 | -3.1285 | -54.1657 | 2026-10-09 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b84c22e4-17d9-3073-a26a-c22616cc999d | -3.0007 | -53.9075 | 2026-10-09 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| bd12b11e-f8e6-3321-a069-26c45fe0c235 | -6.8909 | -45.8763 | 2026-10-09 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 0b43dfcc-2a91-36d8-9b25-7a67787169a6 | -6.0212 | -40.9333 | 2026-10-09 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| c880a47a-7b2f-3de6-930b-3c7a91156832 | -3.1284 | -54.1857 | 2026-10-09 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1382c5aa-d16c-3fd6-a3db-e79fa8d3fce3 | -8.9687 | -45.1542 | 2026-10-09 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 27b55963-a642-3236-b09f-64560e04fa81 | -13.1636 | -54.3591 | 2026-10-09 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7e3911fb-6aae-38e6-bbc9-cd1557e0cb09 | -9.8798 | -50.4918 | 2026-10-09 03:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ef5c49d3-e874-35fa-816a-dbef3279b0a3 | -11.3107 | -44.8105 | 2026-10-09 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 47e74abe-af4e-300f-9d78-d792e40facb7 | -6.8719 | -45.9003 | 2026-10-09 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2c2d25fe-e231-3a03-8684-52eeda64a22c | -8.911 | -45.229 | 2026-10-09 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a4ccb26b-589a-39b9-babe-a7b817fb727f | -3.5493 | -54.6951 | 2026-10-09 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| dfb4bc1e-7be0-32c0-bdcd-7aa79f9eadac | -6.0024 | -40.935 | 2026-10-09 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 166.8 |
| 0c37d396-eda5-3985-8c5a-a2a162973d93 | -2.499 | -56.0675 | 2026-10-09 03:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2143d725-2092-3b40-a577-2225d7a9bb20 | -6.7365 | -55.1474 | 2026-10-09 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0f1deffb-bf6c-3ef0-96e0-99f6f21cf22a | -13.2462 | -42.2645 | 2026-10-09 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 6bfc6145-94aa-3372-960f-5923d56ecaef | -3.1109 | -53.945 | 2026-10-09 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e4506fb3-d7b2-3ecd-9419-cb317b44c2d4 | -3.0925 | -53.9455 | 2026-10-09 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4b3e57f0-1cdf-3acb-b7cd-2ae87af39ed9 | -6.0019 | -40.9837 | 2026-10-09 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 325.6 |
| ad00f361-ce9b-3531-a582-51411bf9e440 | -6.021 | -40.9577 | 2026-10-09 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 412.1 |
| ed9c44c3-1c61-3505-9e1f-6019ced3e71b | -6.0207 | -40.982 | 2026-10-09 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 261.6 |
| 96fd579c-47dc-3b97-833d-1eeec36dda5b | -13.2467 | -42.2401 | 2026-10-09 03:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 88e7da82-e8d7-35f4-b6fc-1ba7a341474b | -7.1995 | -55.1627 | 2026-10-09 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d761fc12-2005-306a-9cd1-8f92be7b1c0a | -12.2346 | -57.1071 | 2026-10-09 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 13c23e1e-e1f3-3424-a5c2-270036830c55 | -3.5676 | -54.6946 | 2026-10-09 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4ca5e0c2-8970-3708-b828-5f7078cebf77 | -3.0007 | -53.9075 | 2026-10-09 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 74c74146-28ac-3ab6-8402-2cb7ebfa4fe1 | -8.8921 | -45.2311 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ebd626de-d63c-3148-ab68-30e853e0899b | -12.2348 | -57.0871 | 2026-10-09 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 305.3 |
| d2f6f561-c837-3c49-931e-de0352c7d886 | -12.2156 | -57.1087 | 2026-10-09 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 4868c579-16a6-328f-9787-163ec57513f7 | -8.8924 | -45.2083 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 5ce0e85e-f41b-390b-94c2-0bd43b9a5239 | -6.8907 | -45.8988 | 2026-10-09 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 90762818-884c-3c61-90cd-2e80c03c52ee | -8.9113 | -45.2062 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| a784a44f-669d-3bc5-85aa-20ef0632ad82 | -7.218 | -55.1617 | 2026-10-09 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| efaeb410-a157-38c8-835b-92327e47ace8 | -6.0019 | -40.9837 | 2026-10-09 04:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 140.2 |
| 3bdb0c2f-54ed-38ad-87c2-518bfeb301c2 | -8.911 | -45.229 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 37667865-ce2a-3582-8219-1706f6919cf3 | -13.1827 | -54.3571 | 2026-10-09 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0a817467-78b8-3d59-8e10-a636f0ef5158 | -3.5493 | -54.6951 | 2026-10-09 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2b41ccaf-af44-3aaf-b5a8-4616af72ad22 | -6.021 | -40.9577 | 2026-10-09 04:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 146.7 |
| d915d32d-2d5e-3bae-9700-1229aae325f6 | -12.2538 | -57.0855 | 2026-10-09 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a5c13e5c-83db-3c02-8136-56d165e32ead | -8.7234 | -45.1355 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 45cf22b3-bb2f-32a0-948a-3249d940c740 | -6.8909 | -45.8763 | 2026-10-09 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| bf2c3ab9-8ef6-3885-a2c3-f8307f05983b | -2.7428 | -54.1146 | 2026-10-09 04:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a75e665f-0c2f-3e5f-86b9-c83c70d0e5fe | -6.0024 | -40.935 | 2026-10-09 04:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 26db0b61-9d2a-33b7-b28f-cb0d1b39311c | -3.1101 | -54.1661 | 2026-10-09 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4a66c754-505c-3b4b-8265-31696e07b811 | -13.2467 | -42.2401 | 2026-10-09 04:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 3dd87858-11dc-3957-8f47-f479d076a748 | -3.0925 | -53.9455 | 2026-10-09 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9df5c797-ed58-32bb-9425-46259cd85429 | -8.7231 | -45.1583 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 0f4e7232-e32f-3e6e-aabb-acdffe7ed2c0 | -6.0207 | -40.982 | 2026-10-09 04:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| a908ccce-c3ee-3848-ae73-7d35cdda4f70 | -3.1114 | -53.7839 | 2026-10-09 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 345fd7a6-067f-332b-816d-1bc946b1b36f | -13.1636 | -54.3591 | 2026-10-09 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4e5dd864-7574-317c-9646-a93bd1d1dd55 | -6.0021 | -40.9594 | 2026-10-09 04:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 277.7 |
| 78005763-e749-3db8-9134-64a238df5292 | -12.2154 | -57.1287 | 2026-10-09 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 6b23072a-e378-396e-858f-767a7e29e84f | -2.823 | -58.2838 | 2026-10-09 04:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3645907f-c99c-3a63-ac3b-251c2763f614 | -3.5493 | -54.6752 | 2026-10-09 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1db05b83-133b-35fd-ac96-ccd5262a2e5c | -3.1285 | -54.1657 | 2026-10-09 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 241b2741-3dce-3404-a3ed-d29f4807563d | -7.2182 | -55.1416 | 2026-10-09 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| cdec701a-3973-306d-b638-eb3be6f0cabd | -12.2158 | -57.0887 | 2026-10-09 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 245.0 |
| 3cbed15b-91ce-342d-b9f0-d8d74d931f1d | -8.9687 | -45.1542 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d2d5cd7c-6fb5-39a8-99a7-7092eb544774 | -11.3103 | -44.8337 | 2026-10-09 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| c212e66c-4d54-312a-89e7-867c93b8b223 | -8.9684 | -45.177 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7cebbcd7-b204-3fd5-9824-ad4077a155dd | -8.7423 | -45.1334 | 2026-10-09 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 460bdf20-91d5-3351-a463-2e36dc056a16 | -2.499 | -56.0675 | 2026-10-09 04:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 295a0123-ce43-30f5-bbfc-cc30875cffcf | -3.2576 | -54.0418 | 2026-10-09 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5a913b28-28f1-3c41-b526-46136bad8715 | -6.0021 | -40.9594 | 2026-10-09 04:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 179.9 |
| 67a8d32e-cc56-3ca3-b167-2d18d271376d | -13.1636 | -54.3591 | 2026-10-09 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3548aeb2-f4db-3f51-9fd2-da88197bf656 | -6.021 | -40.9577 | 2026-10-09 04:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| f8830059-2100-3915-bbb3-c07d9b16c487 | -3.5676 | -54.6946 | 2026-10-09 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3940d4a0-44f5-31c0-a587-ccf105b89558 | -8.7423 | -45.1334 | 2026-10-09 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b5a8003c-1a58-30ad-b0b8-968d1620e52f | -9.297 | -47.4313 | 2026-10-09 04:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b7dce897-fafd-3b5b-90b0-64aae3237713 | -8.9687 | -45.1542 | 2026-10-09 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.7 |
| eb7a0f14-477c-3498-9823-d7010b8ae630 | -8.9684 | -45.177 | 2026-10-09 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 542317cc-5de5-34e5-88d3-c5a70217862b | -4.7404 | -55.672 | 2026-10-09 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 09603c3e-5c1f-3f8a-953d-cc934fa51647 | -3.11 | -54.1862 | 2026-10-09 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6d5df87f-a543-3476-8477-f912025251bb | -13.1827 | -54.3571 | 2026-10-09 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| aa8ba41b-540f-3bd1-9112-5a206ea88a64 | -2.7428 | -54.1146 | 2026-10-09 04:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1f4dd6f9-f16d-3484-8da9-f3b6d214d8b3 | -3.1285 | -54.1657 | 2026-10-09 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6452235d-980c-36d7-acda-81b84d16715c | -3.5677 | -54.6746 | 2026-10-09 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 66cd999c-ad44-356a-afa5-11a974c5a3f0 | -8.7234 | -45.1355 | 2026-10-09 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6996d690-8959-330b-9e7e-3ff5c94af11f | -6.8907 | -45.8988 | 2026-10-09 04:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 0413d147-f03a-3005-aca5-62ac764cf4fc | -6.0019 | -40.9837 | 2026-10-09 04:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 4b6d1d4c-721a-36fb-b446-faedf1923c06 | -2.499 | -56.0675 | 2026-10-09 04:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| a8a84af7-da9f-36f5-b9a0-32ddda593ce1 | -11.3103 | -44.8337 | 2026-10-09 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 33694a08-441f-3e67-a5c7-96231d560bd0 | -3.3455 | -50.4078 | 2026-10-09 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1d782be3-4a3b-348c-b9a7-640c534ca570 | -13.1639 | -54.3385 | 2026-10-09 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| be27b765-ff10-3faa-9517-503ee7db30c9 | -2.8047 | -58.2841 | 2026-10-09 04:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 569e7431-7b04-3921-8bc6-b692bfc723f9 | -3.5493 | -54.6951 | 2026-10-09 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f79329d2-13b2-3b6d-99b9-497b0163169b | -3.1109 | -53.945 | 2026-10-09 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0af1aea4-953a-393c-8642-19e78ed1a9bf | -8.9113 | -45.2062 | 2026-10-09 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b80b5790-5914-3024-b646-85a2c2e6dbec | -6.0207 | -40.982 | 2026-10-09 04:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| a511d863-6f9a-30b4-a427-452890abfb2c | -3.1101 | -54.1661 | 2026-10-09 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 251a9640-a022-3132-90d4-f37d1a858aec | -8.911 | -45.229 | 2026-10-09 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| bb764805-7c2c-3ff1-8502-8c02d0aef6ee | -3.0007 | -53.9075 | 2026-10-09 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 57611a7e-8a7f-38e9-85f8-07522dc5f88f | -3.0925 | -53.9455 | 2026-10-09 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3cbcb389-2012-3b5d-9182-fec37fb22d3c | -8.91 | -45.23 | 2026-10-09 04:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6afa93a9-227e-30eb-9e52-ea913b0b7eb3 | -5.99 | -40.97 | 2026-10-09 04:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2cde0305-92eb-3e8a-824a-acd6432b17cb | -9.2967 | -47.4534 | 2026-10-09 04:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 2ec2a9bf-fea8-3adc-9bd0-812438e18707 | -7.4443 | -63.5401 | 2026-10-09 04:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |


[Clique aqui para ver as próximas entradas](README72.md)
