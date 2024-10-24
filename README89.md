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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10cf6bc0-c7a8-3fd6-8f57-6b6fbd9ea799 | -17.26355 | -57.24256 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 77a03b58-7083-35c2-882c-6dc53b4f7102 | -17.26334 | -57.27628 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e77fc860-fc04-3923-b62d-12ce045af16c | -17.26256 | -57.30237 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8bde1ea-917c-38ef-9d11-ffde0190731e | -17.26197 | -57.30601 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9fa0635d-82e3-3bf9-9894-d21465d9e57a | -17.26196 | -57.23106 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e990afff-cc49-3d06-991c-7a01c493f0e1 | -17.26138 | -57.2347 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a6d94282-3364-3288-91f0-9de677c1a598 | -17.25923 | -57.30178 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9c78f275-722e-33e0-b8dc-5525750ee5e5 | -17.25846 | -57.2529 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a27dd0bf-0b41-36e1-ba20-0bcdd08624d3 | -17.25824 | -57.28663 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6efadf0a-f670-3ac6-8eaf-cdbcbbec6540 | -17.25804 | -57.23412 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0013b0a2-0cd7-39cb-8cd9-2c8c303219ae | -17.25765 | -57.29027 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad737472-99ca-3315-892a-b79413cfed8b | -17.25655 | -57.28627 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b3db6ab5-65d5-3f71-9623-b86826878018 | -17.25648 | -57.29756 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fa9d9337-33cc-3315-9f1b-11fad299778b | -17.25571 | -57.24868 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 005e92b9-4e23-31e1-ab0b-9e7383dfcedd | -17.25512 | -57.25232 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 66c667d6-d240-3053-9546-866d93cc2398 | -17.25454 | -57.25597 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| fe022ae7-c6ea-398f-bb2a-3de0fa141f5f | -17.25179 | -57.25174 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bfafc7c6-593b-39c7-87eb-c6a72d43e1c6 | -17.25121 | -57.25539 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| ce9798b8-ba8b-3ed9-899c-054b797f519f | -17.2502 | -57.24024 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 0494457e-0150-379d-afa1-cd135525d617 | -17.24845 | -57.25116 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e354636e-93ac-3cc2-8edb-ab62a6c313c0 | -17.24787 | -57.25481 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d7c7c160-de7f-30f1-8d5a-0dcc1996be20 | -17.24687 | -57.23965 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6a099ed1-5759-3f7e-ac39-77cda6b78d5a | -17.10076 | -57.47361 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4f18688f-a7e6-3240-8049-1b9abf1b170e | -17.06987 | -57.43054 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f44052ea-e2d7-3719-934d-825580f60fb6 | -17.06886 | -57.47933 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4019aae3-ff32-390f-8874-85a334c39305 | -17.06491 | -57.48241 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1bdfe5e1-defa-34bf-a8bb-97d60887ba9f | -17.06216 | -57.47815 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7b8ca142-5e6e-3b1e-86f8-120ffcd95e40 | -17.06178 | -57.45925 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5fa9e0fe-e8f9-379e-970c-5fecd0de6110 | -17.06157 | -57.48181 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d1714202-7070-3dd3-8cd5-3ca61c57cb53 | -17.0614 | -57.44035 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 73997741-7c0f-3d6f-960d-5e2a42cbb69f | -17.04564 | -57.45265 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| efe3542f-ba22-3764-8816-80d30cf73e71 | -17.04445 | -57.45998 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5c847522-8071-37b7-a916-0c1c47a8d81b | -17.04229 | -57.45207 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 1e60526c-47b0-3dfa-85b4-99e93c054f65 | -17.04111 | -57.45939 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a920237d-e231-36b6-8768-a101c94eb4e8 | -17.03992 | -57.46672 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7281d9b1-74b0-3edc-b0ba-d20b3260d0a9 | -17.03872 | -57.47405 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0b71cfa4-43c5-36a1-86d0-247e85d304a0 | -17.03813 | -57.47771 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c352a200-6b77-3c36-956d-0e67ed8592b0 | -17.03716 | -57.46247 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| daeae04a-375d-394d-bd04-224130104fa6 | -17.03657 | -57.46614 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 39b1f300-3add-3420-967e-0831b4f0a82b | -17.03441 | -57.45822 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 3337e42c-4a19-3ef9-8bef-c6b90f951a25 | -17.03322 | -57.46555 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 21bcf063-928f-343d-95b0-8e9754f014ed | -17.03203 | -57.47288 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1727d0af-61e6-3772-aca6-6ecb77d4bb7f | -17.03166 | -57.45397 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d7c46fb5-b02d-356e-8751-bf07cb2c6d18 | -17.03106 | -57.45763 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1dab4801-ee50-317a-8b61-01de1faf0d5c | -17.03084 | -57.48021 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 96a6f9a9-919a-33c0-aa55-abc2f1539482 | -17.03061 | -57.5028 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4b872eb4-3808-317f-a923-f638bb2f9bae | -17.02942 | -57.51014 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| bc8f0f53-49cd-3ea1-a34c-37c6bdf2f4d6 | -17.02882 | -57.51381 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| b1ab3bf6-d3f8-307d-b04f-880a37dbad8c | -17.02868 | -57.47229 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e3ed1a53-f533-3e50-a2f7-68221264b86d | -17.02831 | -57.45338 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d25b0a46-9e27-3833-ba9d-f45a6000d96c | -17.02822 | -57.51748 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2b2526fe-da44-3cae-8136-b05e179c2145 | -17.02786 | -57.49854 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ef138cac-a3b4-3242-869d-9f024455a350 | -17.02763 | -57.52115 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6ff7d2be-72e5-3d73-83dd-d8882c3d7598 | -17.02726 | -57.50221 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| bf31fe20-1cf8-3de9-b0d1-0af6c31a00b3 | -17.02675 | -57.44181 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2650385b-0660-3ca9-969f-ef9c3717d95a | -17.02666 | -57.50587 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 62f2f890-c34d-31b9-8ce0-fec1ebaa856f | -17.02547 | -57.51322 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 38c4e8fe-cbbe-3dbb-bfda-f871decf7608 | -17.02533 | -57.47171 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 445dcf61-cbb2-308e-ae1d-4da5e56680ab | -17.02487 | -57.51689 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 5c241be6-cae3-3289-b53d-f7cb6a6830a4 | -17.02451 | -57.49795 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 48a39d08-593b-3851-9a86-cc8d0e0637bc | -17.02414 | -57.47904 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d41c734a-385b-34b1-9b12-1fb4bf1a766c | -17.02391 | -57.50162 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 3f4bdbd7-6b4b-3da3-80fd-0dc818d529c5 | -17.02377 | -57.46013 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a1da30f9-6efc-3b2a-b9e2-4992ec8be043 | -17.02354 | -57.4827 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8c2bc648-a9e5-34cf-b429-9673c0e846c5 | -17.02331 | -57.50529 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 9e29c3e7-9fa5-33ee-b539-c9458d9a45ff | -17.02212 | -57.51263 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| dba8aa9a-6739-3790-9156-38b1197dfb2a | -17.02176 | -57.4937 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fbaca224-8c42-3874-be8a-0dbacc8cb18d | -17.02152 | -57.5163 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d342cd94-b161-3326-bc20-92a238b78876 | -17.02116 | -57.49736 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4b3b3b09-92a0-3f3f-a112-6cec1bc14074 | -17.02093 | -57.51997 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| cafd8928-242a-3e7c-b9b0-b9097ad3c5ff | -17.09741 | -57.47302 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 752b8ed4-2ec9-3c0a-bc66-070d20cb1b4d | -17.0722 | -57.47992 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 065ffe46-35b5-39a5-804b-5cf1cbd40516 | -17.06945 | -57.47566 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 30d0f810-1b49-3926-b839-e720c4b10d2a | -17.06826 | -57.48299 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 363c052d-7dd4-3fdc-aaf2-eab64550ce9d | -17.0661 | -57.47508 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c5f38648-75c1-322a-b173-859a06111a51 | -17.06551 | -57.47874 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2ceb6dc0-25c4-3919-b134-d029b84c9b2e | -17.06276 | -57.47449 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2530158e-569f-355a-b043-80985ecf0c0e | -17.06237 | -57.45558 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 06ca7413-518b-3c72-a51c-af2f7a790811 | -17.05941 | -57.4739 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f826c857-3a09-3078-86ce-27b61f60aed5 | -17.05903 | -57.45499 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6425f63f-217d-38b5-9523-003a302bb4dc | -17.05881 | -57.47757 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8b560876-f748-3600-b804-ce5eb032b178 | -17.05606 | -57.47332 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0648ba33-d726-3741-85d0-0c9e2f77e09d | -17.04505 | -57.45632 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 5354c875-568f-3ddf-b99e-8b0c21e1ea68 | -17.04207 | -57.47464 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4013d144-3ac0-38a8-9e7f-8f9f1831515c | -17.0417 | -57.45573 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| e3afdf63-e446-3f93-8594-d73cbfdc374a | -17.03954 | -57.44782 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d7667545-7ec7-3e57-9ba1-16ed1978bb4e | -17.03887 | -57.51557 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8ee83b5f-e1ce-3c12-8dcc-1ce083c26f54 | -17.03835 | -57.45514 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 30a7be6d-82ad-3f3e-8d3f-b50db9e72bf3 | -17.03776 | -57.45881 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7c35bb47-81e7-3b23-8b64-ca10a2ad5367 | -17.03679 | -57.44358 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0e3a5064-7d4b-3420-8d0e-7993b9921676 | -17.03619 | -57.44723 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5923120a-4365-3ec1-a581-74f4f55ce6f8 | -17.03552 | -57.51498 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| f027878d-f211-35e4-9d2c-bce470bea03f | -17.03538 | -57.47347 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 11eff31d-75cc-3751-a448-62e9067e2d7b | -17.035 | -57.45456 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 294b6529-8dfe-3ac9-acaf-daa7749ec878 | -17.03478 | -57.47713 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b406d502-91bb-335f-936f-b8de655e85c2 | -17.03381 | -57.46188 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 60765eb6-1ca2-320a-b08e-9fcea717c42e | -17.03263 | -57.46921 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a4334725-6888-3318-97d6-cd253fa0a8fc | -17.03217 | -57.51439 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 98edf58f-f572-36d4-a107-f5ff575e6892 | -17.03144 | -57.47655 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 822cbea2-eb9e-32c5-9b2d-888d1d2796ba | -17.03047 | -57.4613 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |


[Clique aqui para ver as próximas entradas](README90.md)
