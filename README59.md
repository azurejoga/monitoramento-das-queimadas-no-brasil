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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc9aa35d-275a-3239-9f2f-80cf133a1678 | -14.56133 | -52.98666 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c83d191-f1c0-3a94-80e3-0bb61350b550 | -6.3811 | -54.95376 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32581ff0-8f23-3c75-9756-777cc723bb42 | -5.82525 | -57.63976 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92e84ade-7d78-3451-95fe-caa8941bfdfc | -6.90413 | -58.99605 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3d90b30-6cf1-3914-bcfe-49a1afb99ce2 | -12.03142 | -63.09227 | 2026-08-21 05:23:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebb95d85-d223-3292-a180-dc178261c7cb | -7.01025 | -59.54587 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52a1eece-a7c7-3f28-bf39-dc220e296a6a | -9.0512 | -57.07177 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f81ced7-2164-3956-88b9-af2de1bfa0fd | -2.90599 | -60.24321 | 2026-08-21 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b5935d8-d2c1-36ec-b4d3-1b883cc176ea | -9.21227 | -59.76239 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a57eca06-277b-3615-bdab-5e7334992e23 | -7.33887 | -55.68679 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2cdddd0-258e-3189-b0a4-e3bbeeceadc9 | -14.99872 | -52.67446 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44179910-23ed-380e-a134-10786d619fe4 | -6.43434 | -52.75922 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8444fa0-4812-369f-89d1-f66d12c40ec9 | -6.37234 | -54.94044 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0190f2a7-45a1-3c59-970b-3b34cda920a1 | -7.01521 | -48.03659 | 2026-08-21 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 385d78fb-3882-3a13-af47-6870626f9d93 | -5.80533 | -55.72144 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05520080-cfd3-36ab-8fe5-6e5c60e644c8 | -8.56592 | -54.79388 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b17a38c-af64-3cd9-ae74-a3bdf07d2e56 | -6.3605 | -58.33611 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f10db58-091f-31cc-a24a-6a98c20ba5d7 | -6.67208 | -52.89927 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b44913-d7f8-3687-a9c1-a9b2ab80fccc | -5.49165 | -60.1315 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a02c7d-91b1-36ad-84ce-0419e2f39142 | -6.84493 | -59.42481 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57427435-36a8-3813-bac3-47f365a5844c | -6.91052 | -59.34454 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12cd7beb-550e-3f1d-892f-af77bbd8a0d7 | -6.57725 | -58.96595 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 611d9e03-7a34-3784-9606-baae9002c21c | -6.89477 | -55.71598 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8a4fd26-b143-3d34-a8ee-bfd33206c1f5 | -7.60515 | -60.95739 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98dc17eb-80d6-34bb-987c-10bf98e04976 | -9.16875 | -57.01005 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a413ad3b-e2d7-3928-965e-39b9f6a1c65e | -16.7398 | -49.36731 | 2026-08-21 05:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 176efa6e-ac48-36e8-bcdf-d9d56c1698dd | -7.33944 | -55.68304 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3495279d-5464-3cc2-acd8-57b26487bf60 | -6.71929 | -59.09999 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c0fbe72-9e1b-3e7d-8609-70499c563300 | -9.07094 | -60.43151 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4139609-5311-3bc1-a536-11a91fe382aa | -4.58647 | -59.94313 | 2026-08-21 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd70922-da29-38c3-a0a8-641b20a1e350 | -15.55389 | -50.27966 | 2026-08-21 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b21f497f-6f2d-3ff7-9324-ef5b953ec790 | -8.52446 | -55.33152 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75457a74-f182-3214-bcca-0d6bd2120ed3 | -6.54716 | -56.26435 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdd3e600-8fb5-3d9b-a644-b0cb8f4f78d1 | -6.22927 | -55.41869 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aad84846-88d9-3897-b571-4fb82c3ca150 | -6.58063 | -58.96649 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965bfc31-1091-31bf-91a8-8197d4faa8c3 | -10.52144 | -50.77774 | 2026-08-21 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b98a683f-5d4d-3597-b46c-910bf977aea6 | -6.86727 | -59.41702 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e99a95d-5ce5-3fa1-bf89-275cf0ec121c | -5.80986 | -55.71466 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5225f8d9-7c46-3e06-a805-df97650e5bcf | -6.00008 | -57.85941 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 300a9745-61aa-302f-b606-1b0b5735fdfb | -6.88034 | -59.42298 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca7de4f8-65b3-304c-a6e9-f81fa14a136d | -7.36098 | -55.51965 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2606f9e2-130a-373c-8d35-dd13bd0319ba | -13.43475 | -51.80677 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03f682e2-8561-31ee-afe3-07ab350d8fe2 | -6.43458 | -52.74632 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 716f7a21-f770-3ee1-aad6-259fa0658efc | -6.60149 | -56.36785 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b469c4-878a-311e-9a88-3cccdfe8958a | -9.44468 | -51.61325 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c89d815-412d-3a94-8051-a6245c8bf34d | -6.9053 | -58.98884 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e103d7-91bb-3770-a464-dc828ac03149 | -4.91691 | -56.26171 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85fc67da-dc5d-3b6b-9dc8-ac1b285906e4 | -5.80929 | -55.71831 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b56e0af6-232e-3087-ba60-bf480ab62609 | -6.20388 | -55.49126 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2b915bd-de29-36df-9484-99126b22ffd6 | -6.43107 | -52.72729 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3ed03fd-574c-34c6-aaef-6b028ef2942b | -6.79223 | -59.59633 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3214077e-5d33-3241-94bb-bbe7254d616d | -6.4282 | -54.9288 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac56221-ba39-3e10-890c-3fe4dd8669c2 | -13.09982 | -51.58949 | 2026-08-21 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 693b4878-ca27-3b0e-a6d8-8798174fb51f | -9.20857 | -59.65644 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24144777-b054-34d3-9fc9-034f8d1971c0 | -6.83306 | -59.41149 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1617acf-92a3-32d3-975f-11cbfda0eef9 | -5.61059 | -44.00597 | 2026-08-21 05:23:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e82dd339-8bef-3dbd-bdcc-02c8404314ea | -8.6674 | -54.58472 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8f6d396-e650-3688-bc74-3ed0ccf6871d | -8.57108 | -54.65996 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb00cca2-190e-3cbc-8d00-ff418dc7a8ed | -3.84414 | -59.37996 | 2026-08-21 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b7896fa-2c90-3ba5-9e1f-0ddfc9ab1108 | -9.20828 | -59.76551 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf7746a9-2b1b-3ccb-a7b5-52dc7c4f1b6d | -16.30234 | -53.17146 | 2026-08-21 05:23:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a445bb4-ad7f-3715-a714-831a6a89aa85 | -6.31157 | -55.92138 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fed2d54-1d4a-3cd9-974c-295842f0e9cc | -6.60678 | -58.38667 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92232b95-41ef-3f56-a104-5509e271587d | -12.51398 | -54.75184 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bdbbefb-cfe7-361d-9891-e8ab8123899d | -4.93783 | -55.77802 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afd0bc84-c5fa-39a4-bacc-96a6ca32233b | -7.4319 | -59.7901 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dba47fe7-6396-37c0-b494-d95d4978d01e | -6.86769 | -59.4361 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35a26c3a-8d7b-3b2c-8969-f3b4a1bd52da | -6.87573 | -59.42982 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c497ab25-2813-3418-b718-3daa1775452e | -8.09107 | -51.66967 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 37194a60-5edc-38f3-a0e8-892df02d6315 | -6.11379 | -59.92125 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 761b0d7b-180a-3c2a-ae48-63c27a8e7d42 | -14.32606 | -51.9057 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f595522e-cbf7-3348-a1bd-6541f769adcb | -6.9305 | -59.35114 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2415fe-03f9-3781-81bd-fad5cdee2e33 | -6.81717 | -59.40131 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9b5a1735-79c0-39c7-bd4b-8d7bc940e181 | -14.10317 | -58.8525 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b6cf89c-b118-3e28-bce9-3bfae46ed7cb | -9.11681 | -60.34809 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 640ea294-f229-3f5d-a849-4ac04be5a4d9 | -6.5818 | -58.95927 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 987db5ec-d386-3ce1-8bc3-7cdcd4287bca | -5.8161 | -55.71936 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a665fd31-860a-31c1-9a7b-dd5198fe7689 | -9.21729 | -59.77454 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e93360e-5d0e-3079-b2b2-a75d816c72d4 | -13.44072 | -51.81421 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b671552a-012d-3b76-b423-896454311cf0 | -7.69212 | -57.4351 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d87cf90a-7ad2-3e35-977d-57d244ba32d0 | -13.94257 | -53.8543 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2992e5bb-aff6-3b2e-8914-cc1d75a0d43b | -6.69795 | -58.97387 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed80b880-5315-31aa-ae51-1431105dacdb | -6.88599 | -59.43149 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 985211d5-da3c-330b-a8ad-287cea7f279c | -15.71484 | -47.79189 | 2026-08-21 05:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72770896-ae01-3d06-8229-1296ac0bf12c | -13.3988 | -54.3814 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 57b36ee5-71d9-3773-bcb9-f7ced664f6af | -6.80669 | -59.42241 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cfd6459-1654-3393-812e-49d5db50470c | -8.09664 | -51.6622 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55698376-223e-3dd6-a740-5a14b431b631 | -6.16923 | -52.48943 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 656264ee-db03-3565-bd17-09b9186a891d | -12.93388 | -56.62508 | 2026-08-21 05:23:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ff065a1-a1d7-3c8c-b6b2-cea06522ed68 | -6.72326 | -59.0969 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 655219cf-8fe2-320e-93ed-057e88b9fff2 | -6.86145 | -59.43127 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22c4664a-9ff6-3bb6-a3a8-b0a6697292eb | -3.53935 | -48.18381 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fb816d41-5d46-3978-8440-30e4bacfdfe2 | -6.8982 | -55.71652 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d4f2dea-fc2f-3bfe-928e-454ee79afcb0 | -6.86278 | -59.03371 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 074121ac-682a-3785-8e5f-33842fa669b1 | -9.15932 | -59.65955 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 799119ed-73b0-3b6c-a7ca-a44cb75771b4 | -8.57587 | -54.75237 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8510bb5-ca23-396a-b347-4dc98a5cbc28 | -7.33829 | -55.69054 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b880037f-d052-32d8-b9ec-7722d13a01ca | -6.59723 | -59.12185 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a6fa3c-1525-3b97-82eb-039496033861 | -6.69497 | -59.09972 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 182d70b4-20e4-35d0-b68e-365712f1130a | -5.66385 | -51.64759 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README60.md)
