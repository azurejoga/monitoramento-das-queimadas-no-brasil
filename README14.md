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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9c0d50b-0921-3a41-adf9-1f95b615c439 | -15.18548 | -55.21492 | 2026-06-09 05:10:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42613390-8423-3bab-8581-05b9f8d34f53 | -15.1757 | -43.85589 | 2026-06-09 05:10:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8f054ab-c289-31fa-bdc3-e85acd4ffa4b | -12.43744 | -58.47367 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88bdb61a-da49-3e8b-8fec-31d85a3acdcc | -12.85041 | -44.37449 | 2026-06-09 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 527d4ca8-e592-3e27-b226-cb1147757b9e | -11.44823 | -55.10965 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfa089e2-1cb9-3008-b596-bc2f3f1693bb | -15.18488 | -55.21896 | 2026-06-09 05:10:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31d0e32e-3256-3c0d-b730-fafac2d1d0e2 | -13.94331 | -57.97086 | 2026-06-09 05:10:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0a1a893-8282-3a99-85ca-bc619467a4b2 | -12.43685 | -58.47729 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2308cec6-d41a-33a3-9cf4-58e488615c7e | -12.84838 | -44.39225 | 2026-06-09 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b70e0bc-4c26-3342-9f98-3b640dbcfe33 | -11.62482 | -55.19056 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 94ce1bb5-42bb-320b-8612-2c57569f5232 | -12.85327 | -44.37531 | 2026-06-09 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f8601633-66d3-3861-89a3-cd1abea34561 | -12.44021 | -58.47785 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d7f397-a089-3aee-af50-1f43c3d78105 | -11.59916 | -55.33493 | 2026-06-09 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db5973b7-37bd-359a-b71b-088a69a1cab9 | -14.29363 | -57.54105 | 2026-06-09 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44d88d7c-2640-3d58-a32c-054914131f65 | -11.90131 | -57.77731 | 2026-06-09 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11fadd7d-afad-35e3-8f38-f4476771eb11 | -11.67165 | -56.76553 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a1bed7c-5151-365e-8305-03055a8fe2ae | -19.03071 | -52.80276 | 2026-06-09 05:10:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d15a3f4-420e-39a2-a474-d44fb4901479 | -14.29032 | -57.5405 | 2026-06-09 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7a58d78-0a89-3865-8666-8518862672cd | -12.43863 | -58.46643 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b53f045-f747-3e6b-8411-e3de2a1690e0 | -15.67571 | -56.33074 | 2026-06-09 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c05b06fa-45f3-366a-bb23-e60ab3c924b5 | -12.46473 | -51.46264 | 2026-06-09 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e41d24b0-a497-309e-affd-6d9e62f6f3e5 | -15.2247 | -50.85684 | 2026-06-09 05:10:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29c21b74-d11b-3ce9-90e9-ec99daabd5d9 | -11.57365 | -54.58113 | 2026-06-09 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0cdca762-842e-3378-aafe-1916e3403ed3 | -17.59232 | -46.64575 | 2026-06-09 05:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c692a9b9-6f45-35a9-a7e5-e65e7b60f5b9 | -15.17885 | -43.8568 | 2026-06-09 05:10:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2a9dd08-d6ee-3ee9-917b-40b1e44c09e3 | -11.4488 | -55.1059 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77960c8c-dd3a-30f2-a703-8cbc93eceea5 | -13.68583 | -52.96298 | 2026-06-09 05:10:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3fef980-30e3-3238-b798-cc4690dfa2e5 | -12.4702 | -55.1319 | 2026-06-09 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b95bd1ec-b4c5-35bc-925d-0cf40782636b | -14.29366 | -57.71195 | 2026-06-09 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1031bc7-db53-3ce8-a4d9-d305117cda3a | -12.47364 | -55.13242 | 2026-06-09 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09e7bf00-3911-3f90-be5a-06ad8ca9ab83 | -12.43803 | -58.47006 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f35a4cf2-5a5e-3702-964b-5896b59dab0b | -11.57713 | -54.58165 | 2026-06-09 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ae72521-9aae-3898-9f47-bd2e49bf804d | -17.45002 | -47.19064 | 2026-06-09 05:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a59ed5bb-0493-3708-a70d-087476747d13 | -12.85392 | -44.36935 | 2026-06-09 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4848e7f7-3854-37ea-a65b-29420ea9fca1 | -14.32741 | -58.45663 | 2026-06-09 05:10:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eef52b5-c0be-3c1e-86e0-7ec5569b913b | -11.58892 | -58.50934 | 2026-06-09 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6de47514-b49e-398d-ad7b-88bdddab9084 | -11.4772 | -57.11533 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a9c8e77-94e1-38ee-b52e-cdcb32fefd18 | -11.73868 | -54.78409 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eda20d16-9363-34e0-9ebd-7785d334e677 | -12.47307 | -55.13625 | 2026-06-09 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e6def1-c07f-3339-a521-a203b8390ebe | -13.49473 | -56.56842 | 2026-06-09 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae95ffb2-3f72-316c-ae46-802867c78635 | -13.49417 | -56.57201 | 2026-06-09 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b66a8b7f-0db2-395a-a5be-4e24f06b294e | -12.4408 | -58.47424 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 394dd42c-1095-3284-8818-fa5864b3ec2b | -13.11114 | -51.71997 | 2026-06-09 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bb6d2c9-5755-3146-a008-203c873e6da7 | -20.07923 | -57.1974 | 2026-06-09 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb268637-7086-3e94-a30d-ab2331297bb4 | -21.547 | -47.04321 | 2026-06-09 05:12:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6a0c402-8665-3ada-b393-58f11dc75a3e | -21.20539 | -48.51929 | 2026-06-09 05:12:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d37c0946-6b82-3a29-be09-c8c328f2e006 | -23.56596 | -47.51031 | 2026-06-09 05:12:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4c778811-aef8-3dae-82e9-9913fc108042 | -23.55973 | -47.50944 | 2026-06-09 05:12:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b0adbe00-dd6d-3de5-8d72-791e3f143881 | -21.2058 | -48.51499 | 2026-06-09 05:12:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1f3db8-b359-3eca-894d-59c4ba966fb3 | -20.07981 | -57.19349 | 2026-06-09 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd184c5-bf26-3ea3-ad15-3558700c7057 | -20.08039 | -57.1896 | 2026-06-09 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 834baa3b-8404-3ef2-851d-9304b9020099 | -13.2597 | -44.388 | 2026-06-09 05:20:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 267263e5-77a7-3423-92c9-a75348a55429 | -17.5961 | -46.6415 | 2026-06-09 05:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 052b2548-d93f-3cd6-af92-aaae8c750386 | -12.44062 | -58.47297 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 139c9d41-78e9-32c7-89d6-be9cfd11c1d0 | -12.43456 | -58.47214 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 961b92f1-f11a-3838-abaa-4c3e7d0a6c5b | -12.43509 | -58.46733 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68b75eba-dabd-307b-b92a-e89dd23e0fd4 | -11.59183 | -58.50781 | 2026-06-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27430497-f92a-3fc5-913e-580e4dac9158 | -11.43114 | -58.70614 | 2026-06-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a3526cd-f575-3b6e-9700-6b5f74ee5ca8 | -12.44116 | -58.46813 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 280d972a-c2e8-385a-a822-f84e173d8ace | -12.44005 | -58.46695 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e235ab4a-547e-3af2-9247-47f80a3e5ecc | -11.43062 | -58.71036 | 2026-06-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b7f889-0e6b-39fa-98f2-f88843602627 | -11.58835 | -58.5083 | 2026-06-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4defc570-ffd4-3dfd-a6ad-a6373c8f8361 | -12.43342 | -58.47095 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68968dad-ba54-310f-8306-d12a0f2b6600 | -12.43891 | -58.4766 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 986c8557-ee17-3896-8528-a8dcf780a210 | -9.21025 | -58.06683 | 2026-06-09 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48bfe06d-713d-307b-84b6-bae327f5794e | -12.44008 | -58.47785 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5a03fea-3ad7-3c7b-af88-9fe94c561dfd | -12.43948 | -58.47173 | 2026-06-09 05:55:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa049ae5-7f39-3568-9c75-b760b3ac692d | -17.5961 | -46.6415 | 2026-06-09 06:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 5cce7428-e942-3895-9cfb-529685edb5bb | -5.03947 | -43.26319 | 2026-06-09 06:37:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8ee1fa0a-ea10-3dc4-a603-ed0784bd53f2 | -6.64861 | -43.91428 | 2026-06-09 06:37:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2fc12278-8300-31d3-8a55-db47e26109e8 | -3.49982 | -48.0392 | 2026-06-09 06:37:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 66384afa-cbd9-3f9b-8597-67a9821826dc | -5.83692 | -43.47762 | 2026-06-09 06:37:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e60f1b10-e548-3548-8b37-1d89b81240ba | -12.05968 | -49.75336 | 2026-06-09 06:40:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5649ecaa-6ed4-308b-9fb1-c302f808a615 | -9.07454 | -50.59683 | 2026-06-09 06:40:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 9fb474ef-e241-3fc5-b0cc-5fba7a57eed8 | -12.03286 | -47.79821 | 2026-06-09 06:40:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5e7b697c-f728-3054-9865-6d5f778a80dc | -9.30574 | -45.48434 | 2026-06-09 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aed96379-bb08-38db-bf45-abb9d880920e | -12.04956 | -49.76094 | 2026-06-09 06:40:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17fb0b45-2bd3-396e-82b7-8cf2a9e0af17 | -6.6482 | -43.9196 | 2026-06-09 06:40:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a92ab5a2-5ee4-393c-a36f-46efd2d9a607 | -9.29704 | -45.47011 | 2026-06-09 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f8b3d6db-82c2-33cc-abf0-b942d3e9e516 | -13.26005 | -44.3968 | 2026-06-09 06:40:00 | AQUA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ccb12697-2619-35c3-9dff-1924aa8c874b | -10.42524 | -49.43938 | 2026-06-09 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4af91680-11e7-3920-997e-d0d409c1143f | -12.48145 | -46.26936 | 2026-06-09 06:40:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 670df518-87d1-3689-b684-63e73a4b3df3 | -10.64518 | -49.38504 | 2026-06-09 06:40:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 9eca6c8f-ba38-31c0-b54e-3baa2bd00c4b | -12.84741 | -44.3749 | 2026-06-09 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| aa7876c1-c13f-37df-95e4-314dfa355301 | -6.84843 | -45.00694 | 2026-06-09 06:40:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 2536b676-f712-3fbb-9ff2-4c737b55db2a | -9.07313 | -50.60604 | 2026-06-09 06:40:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bc7a3e5a-71ba-33a2-ad9b-cf6dfeeabc14 | -12.05699 | -49.77121 | 2026-06-09 06:40:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fb80d7f9-4262-3cfa-a3f2-0694527645f0 | -10.64651 | -49.37616 | 2026-06-09 06:40:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| acefca4d-eda4-3bcc-a9b2-60415b6363f6 | -10.42391 | -49.44825 | 2026-06-09 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1aaa0737-e83a-32f8-a93e-fb222d0803eb | -8.97939 | -47.97948 | 2026-06-09 06:40:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 296ffdae-d61b-3ad5-8c94-8bfe0683c8bb | -11.55094 | -52.77955 | 2026-06-09 06:40:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c332e999-ae71-3814-bd10-d52c3810b5c5 | -6.85884 | -45.00836 | 2026-06-09 06:40:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e53cec95-688f-3485-8bd0-16cec88c11a2 | -11.54128 | -52.778 | 2026-06-09 06:40:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 15ae659b-9aee-396f-977c-55b771207fc8 | -12.05834 | -49.76228 | 2026-06-09 06:40:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6eb398a3-d562-30a0-b920-ff89fe1244f1 | -3.57681 | -49.20231 | 2026-06-09 12:10:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bef9af88-04e5-30c3-9976-e9df8449ce48 | -11.96057 | -43.39032 | 2026-06-09 12:12:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a17e5246-a92d-3b5b-baf9-e819b16f9349 | -9.15744 | -47.48017 | 2026-06-09 12:12:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 932542c9-1e52-3cdf-8c6c-485be0c358fc | -6.90956 | -42.84375 | 2026-06-09 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 2c935652-bae0-39a0-8920-ab0859bf7915 | -8.97863 | -47.98387 | 2026-06-09 12:12:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d2dde88e-bec4-356d-843d-3970e7933c90 | -6.78559 | -42.99535 | 2026-06-09 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |


[Clique aqui para ver as próximas entradas](README15.md)
