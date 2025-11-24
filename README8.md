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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 978a359e-ba87-3153-aa9e-f15a28c20836 | -2.86808 | -47.49409 | 2025-11-24 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 118453af-4ec2-3c48-8722-7576d31a96fa | -3.21482 | -44.35633 | 2025-11-24 04:36:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eb5fd73-23ef-3978-81fd-90807169b0dd | -3.71682 | -44.00685 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c1ff5e4-8fb2-33c3-a2ba-43e2aa74bef1 | -4.82141 | -43.83317 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f8d53dd-f4da-3524-9466-85dc50714ff7 | -4.41145 | -45.73743 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dda4b677-6cc8-338c-b2af-3c2c046a595b | -3.82406 | -48.98933 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b296716-c062-3031-9476-1aa0f9f690b1 | -4.61915 | -45.63714 | 2025-11-24 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9587541a-b649-37b5-a52a-eda5db113392 | -3.96606 | -46.48268 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5af2a54e-ae54-3081-9d81-edc905cad72d | -3.18045 | -50.24303 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 453af02d-18bb-3f56-8e53-f4330bbd8d36 | -6.75349 | -35.03758 | 2025-11-24 04:36:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 12e2cc71-3a23-378c-ba41-66e40ae349fc | -6.08487 | -41.68926 | 2025-11-24 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f27ad041-539e-3d88-929d-e1b252a7f557 | -5.89852 | -44.52525 | 2025-11-24 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd89555e-4258-363a-b739-9c6f971213da | -3.49047 | -46.01949 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dedd2681-fe98-324f-87f6-ecc9a22fb0f2 | -4.45061 | -44.32657 | 2025-11-24 04:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bf6cd759-e0fe-3b1a-ab92-8b4496816967 | -3.41124 | -49.46871 | 2025-11-24 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b90587e-7f8c-35e2-9bf1-63a01f17b81b | -3.17684 | -50.24245 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b919123-2c45-3325-bf56-9f10cd0280ef | -2.88333 | -45.26135 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 153daea2-6958-3fd8-8071-69536bee3f7f | -3.65904 | -43.94796 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fefd35bf-684c-34e0-a0e3-3e98e5ab82de | -4.31134 | -50.28637 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fadea435-789a-3382-bc1d-136211e37096 | -2.88276 | -45.26503 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3c4422a-8282-33d5-a56b-af6ab8565240 | -2.86997 | -51.80055 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3748bc9f-be15-36fe-9a0e-f0bb15da5c24 | -4.51283 | -47.64692 | 2025-11-24 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad903545-a4ed-3341-8152-7a38427ad7f4 | -3.71743 | -44.00446 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c770088-e17c-30e3-bffd-2a22ca79cbb4 | -4.26438 | -40.86303 | 2025-11-24 04:36:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 17679524-9c80-335a-9957-46d04358128b | -4.11786 | -50.0755 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 941645bd-e456-3405-bfa7-ec92594bef44 | -2.80219 | -45.35829 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db6b12e-119d-3d76-abb9-2a7e518ea722 | -5.04449 | -44.09368 | 2025-11-24 04:36:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5568df19-fc0a-3d16-9978-c1a0303ee4ef | -3.71014 | -44.00337 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 968455cf-69ad-3c17-b7fb-094c3c207d4f | -2.87934 | -45.2645 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f2b8e31-3571-3767-95a2-b0c1a5abe32c | -3.45144 | -49.24236 | 2025-11-24 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6ddaa4-fcd0-36fd-90c9-23eff3957045 | -2.79595 | -45.35359 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4318550-11b4-3a19-bb74-6d4c08aadd7f | -3.21419 | -44.36033 | 2025-11-24 04:36:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b74d523-a5d3-3091-8fcb-5cb61cb1c6f5 | -3.22296 | -45.92704 | 2025-11-24 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feea60f6-7194-3453-beac-d21b1bf1f889 | -4.25053 | -48.70377 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ced9ef-2f34-3332-b859-0de386364297 | -4.19526 | -38.122 | 2025-11-24 04:36:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5dddd5ee-db0e-3e3d-8264-0bc7dbf23d50 | -2.47947 | -48.8566 | 2025-11-24 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8637dbcf-206d-3232-a6cd-0dcd65a30f18 | -2.13873 | -46.41464 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 141da535-5d08-3558-abfe-e9805d69edbf | -3.59301 | -40.9775 | 2025-11-24 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c4f92395-8cea-3978-b897-cfdcc9e8b0d2 | -5.74223 | -43.78809 | 2025-11-24 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ea7827e-dcbf-3d9c-91ae-3209ea108ab4 | -5.93385 | -45.57664 | 2025-11-24 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d22d3217-d1f8-3bf2-ab3e-509644fcb951 | -4.8221 | -43.82874 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ebb7026-a2fb-300b-bba6-a11fc3cbec74 | -3.72473 | -50.47777 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3be675f-6755-393b-ba83-bea38148f897 | -6.55087 | -43.21136 | 2025-11-24 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1e512b7c-bb4a-3796-8ffe-2f536a36d4de | -3.49103 | -46.01595 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66918e19-af12-3c72-bd11-bac3c12bf5f6 | -3.80216 | -50.0203 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6704dc3f-d4df-369e-8aaf-3ab381b4d3f2 | -4.447 | -44.32602 | 2025-11-24 04:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4e7bd92-db13-37ba-9eb9-d8ead0bf8416 | -3.96861 | -50.33085 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 902bc7c6-c2c8-351d-ad02-5f6927d5f556 | -2.87991 | -45.28343 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0483661-5501-3099-8368-887ef0131655 | -1.94814 | -46.2716 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e148c139-b6bd-3f7e-8e82-4738d23b884d | -4.16547 | -50.40678 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8313eadb-90a0-3bfa-b39e-fa42a0657b77 | -4.16171 | -48.58017 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8cb2f3d-0a78-35ee-8fe7-6c0edeb010f9 | -3.81447 | -43.35836 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb9340b-b250-3ab1-a9de-1aec9692a29c | -2.12982 | -45.32685 | 2025-11-24 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 354e696c-37fa-31b4-b7fc-465336a9b01a | -2.95973 | -52.94646 | 2025-11-24 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e93756af-716e-37cc-84d2-7b8e59ac3e93 | -3.96501 | -50.33027 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12fdb7e3-c8e9-3a61-9485-cda789be25e8 | -3.2675 | -51.17582 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d50605a4-a356-3ff8-8851-e4ca1934e7d5 | -3.81137 | -43.35328 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87ba70b8-e893-3d58-a9c9-d062be34c57e | -2.16522 | -45.98758 | 2025-11-24 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 08e6691b-8c07-36c7-a84b-dd900b66eb91 | -3.22241 | -45.93059 | 2025-11-24 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb4c73a8-c79b-3bcd-9eaa-5b8e687f0610 | -2.48573 | -47.83244 | 2025-11-24 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1cd3501-860a-39a9-944a-c3020645d2fc | -2.79423 | -45.36457 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33a3461b-2397-3fce-aced-3185d8155b25 | -4.66193 | -46.05692 | 2025-11-24 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b7b1e38-1ab5-35f5-aab3-cf467575142d | -7.29952 | -45.43783 | 2025-11-24 04:36:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e2cbe59-8cda-36f9-a5b5-163bfa9d3033 | -4.817 | -43.83702 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 921c9bd2-c773-3607-b8bf-999f137580aa | -2.87394 | -51.80117 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e237f8f1-f265-355a-8b81-9cfac41d8aee | -6.04321 | -45.83508 | 2025-11-24 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ccce79a-9e06-3cba-9b25-a090ae2b4305 | -4.39104 | -45.73417 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5f50452-61eb-37b7-bc35-59d3533639f4 | -4.71675 | -46.46222 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfa948e7-81d8-3d7a-a65d-a7e58318606d | -3.86049 | -48.98012 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f53350b8-170a-33a2-be26-1c00f857a57f | -5.63605 | -49.13202 | 2025-11-24 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 645cb755-9cd9-3f16-a1de-1866eee24b65 | -2.79764 | -45.3651 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 691112a7-3005-34f8-9c48-6f758723fdaa | -2.42026 | -49.07287 | 2025-11-24 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8820a32f-e8b9-3246-89f9-b3fe06997102 | -2.87709 | -51.80688 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 81006c16-54bb-33ce-b872-20217b8c481f | -2.13039 | -45.32321 | 2025-11-24 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a079647-c285-317a-9a19-26824bcab2e0 | -3.22468 | -45.73395 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd8bdd20-3707-30f4-8257-55ac31c69c0b | -2.69925 | -49.51449 | 2025-11-24 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e416a6-e648-31fc-92b3-fd9aaff6a49d | -2.79821 | -45.36145 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80529445-9a9b-303b-8a11-f5e80c05bc4d | -4.40641 | -50.6002 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10120e91-f55e-391b-82cc-23576842f89e | -3.03421 | -47.79063 | 2025-11-24 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 850e7fe4-decd-3875-b04d-69c14286fe7f | -2.10518 | -47.09799 | 2025-11-24 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fef343e8-9998-35e3-b9e6-ab75d972e82b | -4.81769 | -43.8326 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68d25dd7-bcd7-3d16-8ef5-71fc688b0ce1 | -3.27625 | -46.0479 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19e8823e-8b30-3d81-91b1-7cb9e216aca4 | -3.57369 | -49.39625 | 2025-11-24 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23548214-5f4a-3900-a2fc-a4372e5a7dd5 | -3.59671 | -40.98274 | 2025-11-24 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 53e75b4b-2948-3868-a709-849c43c4e108 | -4.31269 | -50.74101 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a59b58f-dc52-36bd-a382-43714316b77f | -3.74232 | -47.12621 | 2025-11-24 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8fd99bd-b474-3c61-8f20-b439097e1b2d | -4.7134 | -46.4617 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aba6f59e-5415-3f49-ae62-01724c793eba | -3.2196 | -45.92653 | 2025-11-24 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4211338e-4c02-3754-bffb-f81be9102b58 | -3.58936 | -40.97189 | 2025-11-24 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0b74c793-754b-3ab4-847c-4db87227b3c3 | -3.80705 | -43.35987 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 508afdaf-c26e-3562-8e5f-ad6b89271141 | -4.81833 | -43.83485 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3198f66f-a9f3-3cae-9e64-e6d07eb1cde3 | -5.56916 | -44.97506 | 2025-11-24 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 475538a5-2d9f-33c4-9e43-1edd7ffa92a2 | -6.76035 | -35.03816 | 2025-11-24 04:36:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cf173002-ed53-32b4-9861-578e3878d357 | -3.85708 | -48.97958 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85e25c13-d436-33d1-b90d-5c2274f3748b | -1.98061 | -44.52031 | 2025-11-24 04:36:00 | NPP-375D | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50429268-bc05-3189-9bc8-30608d5b9b64 | -2.9604 | -52.9424 | 2025-11-24 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4bf2e9-13b9-3eb9-ac1c-8641419d90e0 | -3.82747 | -48.98988 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa5bafba-dee0-3fb5-a179-4fcf5a76e50b | -4.39842 | -45.73158 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0f46227-74c8-3490-805c-f64df2a1557e | -5.89918 | -44.521 | 2025-11-24 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10fda4e1-dd59-364f-b358-6d47a3a99c72 | -3.09863 | -51.50073 | 2025-11-24 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
