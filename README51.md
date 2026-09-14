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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a34654c-51d4-309b-9ab1-621b88cd9470 | -14.82183 | -48.14515 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8196831-2a8b-3fe5-9c85-6de346009d65 | -13.39982 | -54.61409 | 2026-09-14 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 612ce93d-3db1-3df1-b1b5-0d64fc2643a4 | -14.1751 | -47.40166 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4625fb52-2b79-3594-80db-669202e0f093 | -14.83425 | -48.14389 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae3b985d-4e5f-3447-a168-ed9a309fd6f5 | -14.82627 | -48.14242 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76e65084-02e1-318e-9a9d-c71a6b68d740 | -15.27698 | -42.80072 | 2026-09-14 04:55:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24cfbfae-145a-3d00-8880-6a48f2efd8df | -15.24924 | -42.79765 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81f699e9-28bb-30b6-8ed1-6fc8a591fe3c | -13.5609 | -51.45942 | 2026-09-14 04:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af51577d-dd33-3d68-bd7f-fed6974ba66e | -12.66896 | -54.66195 | 2026-09-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6be194d4-f1c6-3817-9c4a-4b467431b3bc | -13.59012 | -47.90229 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3319de7c-f5d5-33f8-b777-fbf5216e1f26 | -13.29367 | -51.3125 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fa419dc-5058-3181-a8eb-34192bee9e78 | -13.56026 | -49.90443 | 2026-09-14 04:55:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e139753-6b51-3a04-a75e-ab93586be6a5 | -13.49021 | -48.4836 | 2026-09-14 04:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15fc07d9-eaad-37a6-9bc1-160887e64d71 | -13.62718 | -47.8999 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ed36148-a94a-3f4a-bf56-b3c35a86da24 | -13.58304 | -47.89435 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b84df59-e669-34e9-87df-da06fcd60cdf | -15.26688 | -42.79601 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d453684-4090-3e1d-912d-8fb0f8324f79 | -14.17771 | -47.41405 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12bde592-13c4-3624-9c66-4e2f16750e76 | -13.61868 | -47.90227 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65bc8b80-b7a7-3057-a003-2cf450e26799 | -14.18483 | -47.39227 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d07463a-311d-3f3e-b028-d29da50ec447 | -14.18803 | -47.40017 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edf8c27b-27a9-36ed-a2cf-ec945eab7186 | -15.25054 | -42.77728 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66bd2401-c479-3887-a55c-26ac80af61c5 | -13.45866 | -48.4724 | 2026-09-14 04:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36feae8b-c170-3eea-9eed-c242d414caad | -13.58805 | -47.88754 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc1c20ba-65d8-3992-aa45-7f572cb2aa73 | -14.18327 | -47.43604 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 905199b8-68ed-3204-8565-14a0416bff93 | -13.56428 | -51.45995 | 2026-09-14 04:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81cd1bcf-1ee9-3ed0-a4c1-ac1d798bae6a | -13.63164 | -47.89713 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 15da3850-e6b5-3b70-b55b-a80d58fcafbd | -13.3235 | -51.7172 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dd02338-6085-320e-a85c-1e9ea4e3db29 | -13.78461 | -48.80828 | 2026-09-14 04:55:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0f9705e-dcfa-3c57-b211-b82929ee41ce | -14.83026 | -48.14314 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07693e75-0bdb-385c-a1d9-d95988ebcffd | -13.32629 | -51.72137 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e353d1ed-f36a-3307-afb6-3a1d361ab731 | -13.593 | -47.88123 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3599344c-a88f-3dc5-a607-a2436c040cd7 | -14.18276 | -47.43989 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c29992c-6aa9-3eb3-89bc-9735d4228634 | -15.26621 | -42.79313 | 2026-09-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e840468-81d3-3f73-a65a-69028ec006ab | -14.17462 | -47.40528 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 056fcacd-52fb-3c67-b8cb-46101b8ef065 | -15.05739 | -48.562 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb3565d4-a028-3dc7-811b-36bd7b7f8fcc | -13.62221 | -47.90625 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7cc82c4-c8ac-38b8-ac63-1711b0a678fa | -13.58656 | -47.89849 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a72da0a-9665-3167-a1b5-9fc0a1730e4f | -13.32122 | -51.71743 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6567b21-82bc-3c88-94a5-cb3dec4d45e3 | -14.81478 | -48.15554 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6163ba37-8ac5-3bdc-9d62-1986e35e4262 | -13.30043 | -51.31357 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f347f760-ee5d-3902-a013-c6832d0a588d | -11.95924 | -55.26001 | 2026-09-14 04:55:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcec8476-1dae-3a19-b68a-4b1ad438f3f8 | -15.05417 | -48.55646 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4632502f-f576-32ff-b82e-a0d013e3946d | -14.81427 | -48.15918 | 2026-09-14 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 629ca2fd-5da0-3b6f-a0c4-a7b4924b5aaf | -14.17603 | -47.3946 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ebaa1fdc-9589-3b17-8a7e-f5b22a8a766d | -14.17972 | -47.39882 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f55c892-d6cb-3ad7-a5b7-5cfb0ae1aaf8 | -12.66553 | -54.66136 | 2026-09-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8acddb1-1fb3-3be0-935e-2acdca91f74c | -2.88 | -50.45 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20038d6c-3b01-340c-a421-88bf514d1909 | -10.69 | -54.13 | 2026-09-14 05:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c264bef0-165d-3d1c-8c42-c7d95d6fc6f6 | -2.94 | -50.46 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186aa440-06ec-3225-add1-beeeb6d7f01b | -2.91 | -50.45 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ec2a00-c349-3130-b299-dc60f4900642 | -2.88 | -50.4 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aeb25fd-ba62-3097-bbaf-c0c52585a2e2 | -2.94 | -50.4 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d42b5383-b4fd-3d1e-a752-01f46615ce52 | -2.91 | -50.35 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66d8bfc7-7e97-34ac-8d14-f8ab8bac723f | -10.69 | -54.2 | 2026-09-14 05:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e828416-0796-3e75-9c3b-424a8010e737 | -2.91 | -50.4 | 2026-09-14 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec17171b-4d7e-3568-9399-de0dd975a501 | -10.66 | -54.12 | 2026-09-14 05:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55742cda-7855-3b43-a355-657b2a6275ef | -10.66 | -54.19 | 2026-09-14 05:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af333316-7523-3da0-a08e-7b4dfbc24fa3 | -1.22362 | -54.13598 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53525667-2097-376c-8f14-2a33b3949e57 | 2.72376 | -60.44198 | 2026-09-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70fcfac0-63fe-3023-ba38-98bd2bc015ae | 4.27893 | -60.94078 | 2026-09-14 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36745448-2215-38d0-b29b-403869029f96 | 2.58592 | -60.30163 | 2026-09-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5edff61-7d6a-3cc3-9f29-30c902965d3d | -1.2365 | -54.20626 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4031f21-01c4-3b77-8a1e-d161e924c3f1 | -1.19406 | -54.12272 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db06030d-ed74-3dd4-84af-9dfa927e0863 | 1.71104 | -61.14436 | 2026-09-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fef08ec-904f-3c29-a9bf-b572bcad553e | -1.71427 | -54.95447 | 2026-09-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e97d9b5-d836-3b32-baed-385915856c4b | -1.46529 | -52.96527 | 2026-09-14 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4aaf113-47ac-367f-8a4e-6285f1ac4ab9 | 2.58311 | -60.30576 | 2026-09-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc50c294-7dd7-3e7f-82fb-5f00a6ec677a | 2.58254 | -60.30215 | 2026-09-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77f70108-fc31-32c8-8c6f-461006e34b7b | -1.8648 | -54.42718 | 2026-09-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cdd3a5a-59cf-3002-addf-b8239e8899fc | -1.23429 | -54.20261 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f26016e-e518-3c8a-9cfe-32d3d0a9eb80 | -1.86525 | -54.42416 | 2026-09-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c07fe0af-19da-3276-86bc-a7e5b971a2b4 | 1.17318 | -60.49295 | 2026-09-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ce99c62-b1e0-33e1-9ff3-858f55d08eae | 2.7204 | -60.4425 | 2026-09-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ce70606-4ad4-3f00-ae1f-514165302b44 | -1.22411 | -54.13277 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 957b075d-4941-3869-9593-716c30c242a6 | -1.71999 | -54.94976 | 2026-09-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1076f0aa-9f68-3cff-8dd5-ee9dcb88252b | -1.22462 | -54.12949 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b23d557-eeec-372e-b671-da5d249b1aa5 | -1.19451 | -54.11978 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 641eb76a-4a9e-3f19-bdf9-7f27d61f4a7f | -1.22515 | -54.12603 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4909a610-f0ca-346a-8e95-2fda0107486f | -1.23382 | -54.20562 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d767c777-11e1-3d2c-acaf-9658f8524467 | -1.1992 | -54.12352 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65d7d1c-24a9-3e73-be2f-3390cd002f67 | 0.82828 | -60.57537 | 2026-09-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58996eb3-482f-342d-9dac-9df1a7566d86 | 4.1179 | -61.23816 | 2026-09-14 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 530834c4-becc-3eb9-9c65-c33ffe571951 | -1.23696 | -54.20317 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b1b862-3f44-3078-b010-fd0163fe69f6 | -1.19965 | -54.12056 | 2026-09-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d57b7b9-3946-39d7-ba6f-8cb92f788c0d | 2.31897 | -60.92079 | 2026-09-14 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f51c08d-2cef-3b06-a3b8-56d9bd006101 | 0.63293 | -59.75782 | 2026-09-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06bf644-d519-343b-9918-e64586314bc6 | 1.17375 | -60.49658 | 2026-09-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca839abd-4e37-3daa-86dd-6905e802d1d4 | -6.58999 | -58.84673 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ab221a2-d849-3279-8cca-8a15b56a7b9f | -6.29312 | -59.95381 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f509b720-7080-37ff-b678-7a9eee4231e9 | -2.6827 | -57.49894 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5afdbf4f-5055-3a85-9c89-9ba288d36ff2 | -6.3108 | -55.2884 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1fd3087-4f37-3084-81d6-8ac003dbfcd6 | -6.29208 | -59.93503 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f6c3436e-f248-37e0-9c9b-561c22bf374d | -2.88138 | -50.3842 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5669e6de-3608-3e1b-bc88-46539022fc67 | -3.53309 | -59.06789 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c780c56-b48f-3583-a675-253b1949552e | -2.90417 | -50.36936 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32fd1ec1-09d8-334c-aab5-2983462a5696 | -2.90238 | -50.3813 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a9ad0e3-91fd-367a-bc3a-c6e1f52ae1a2 | -6.50326 | -58.3846 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8f8ffa1-dee4-3d77-9f00-77438e7fdb44 | -8.23269 | -55.22591 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00ae3cae-1176-3085-98c7-22a31c899f08 | -3.17215 | -61.19159 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235cb760-e907-39d1-8126-f1e1822803e7 | -3.81278 | -58.90228 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README52.md)
