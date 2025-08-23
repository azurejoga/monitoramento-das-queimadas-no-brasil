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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 469a9794-0604-3da9-9794-469ca91be6ca | -10.6962 | -50.1314 | 2025-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9016425a-5fa1-3fe7-9b8d-e30688c68656 | -11.1201 | -44.7913 | 2025-08-23 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 76e75c10-a6e1-37aa-ba66-8e81da5b2a53 | -9.8214 | -46.3933 | 2025-08-23 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d8fa8aa6-a7e3-31d0-a795-b234a841e28c | -7.9448 | -63.034 | 2025-08-23 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| de052212-ffc5-3339-b008-03561d33130b | -10.6201 | -50.1609 | 2025-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| dc9faea0-62d0-3f59-90f8-3cf03672a07e | -10.4784 | -46.831 | 2025-08-23 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| e3b83a7f-d873-3b16-83de-d8bb04b6c862 | -7.0352 | -44.6396 | 2025-08-23 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1e31bbba-4053-35b0-b04e-db7725a7722b | -6.6044 | -44.5624 | 2025-08-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 54371fe8-b5cc-30bc-ae73-18582573e12f | -11.6981 | -51.6603 | 2025-08-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 95b986d6-cec4-396b-9815-0c5a9794615b | -11.1396 | -44.7654 | 2025-08-23 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 969271be-15db-30fc-9c21-873c6604182c | -5.8309 | -45.1693 | 2025-08-23 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| ac346fb5-6455-3391-85db-22577e49a72e | -8.853 | -49.8843 | 2025-08-23 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| daa5943d-6e5e-3b0a-9863-192c456a705b | -12.1949 | -50.2397 | 2025-08-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 739d904d-d77b-361c-a297-44e4c9e9716b | -5.8307 | -45.192 | 2025-08-23 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a9a889eb-e292-3c15-95b5-e871c636b55a | -13.4349 | -46.2573 | 2025-08-23 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3f51e955-55c7-390b-902f-9536206e7c3a | -7.6366 | -46.2823 | 2025-08-23 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 318adbd2-e33a-3f1e-8e35-9184ddcb3343 | -6.5856 | -44.564 | 2025-08-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 539a03b8-da7b-37b0-a663-6e415f6297de | -7.602 | -44.3801 | 2025-08-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 9e7bffbf-5126-3a59-9afb-a3c0056ea50b | -5.9062 | -45.1185 | 2025-08-23 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d93dd02a-8965-3631-aca3-89828a46597f | -6.37 | -45.5356 | 2025-08-23 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d4528ff7-571c-30ca-b33c-52ddd7ea3022 | -9.1897 | -59.6171 | 2025-08-23 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ca725e3d-63ff-3be1-aa80-261bcb771bc9 | -9.1712 | -59.5987 | 2025-08-23 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5ff16d2f-d99d-33d9-b051-57ff7f1c212f | -5.7615 | -57.5807 | 2025-08-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| bbc59562-916a-3058-bc89-b1364d135485 | -10.6772 | -50.1334 | 2025-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0a63bf52-68f6-326a-9318-773a1a2ce7a1 | -6.8733 | -59.8213 | 2025-08-23 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f33c25d2-88e2-3d61-a0d5-d25749f1cca0 | -13.478 | -47.0227 | 2025-08-23 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 159bb27e-9bff-3ca7-903f-fcd2299c3876 | -6.3887 | -45.5342 | 2025-08-23 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 0db22210-3e76-3671-bf7d-499d5238d7f3 | -6.0972 | -44.6947 | 2025-08-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 707fc724-3508-3b98-a198-9f1efbe26d94 | -8.5272 | -48.8393 | 2025-08-23 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ec3fb19f-9d61-397d-9b5a-d07972e1d290 | -10.6388 | -50.1803 | 2025-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ca89562c-afc0-3557-bf6f-a2fef5d2e794 | -6.5781 | -59.871 | 2025-08-23 14:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ed882912-61f1-3811-8895-e25fd1b47648 | -5.4365 | -60.1588 | 2025-08-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4d191fc7-ff89-3265-8ff2-7e13356a23f6 | -12.7078 | -48.1206 | 2025-08-23 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ade2a313-b1b6-31f2-b923-a696b305b0bd | -6.5858 | -44.541 | 2025-08-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 80e6a20a-dd03-319d-99b0-28c852a83422 | -11.1204 | -44.7681 | 2025-08-23 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 73473bf9-1cc6-3d97-94a2-159ebac3aa73 | -6.389 | -45.5116 | 2025-08-23 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3fd46cef-f59d-3b12-b9fb-8711a81bd668 | -7.0164 | -44.6413 | 2025-08-23 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| e4fcd0d5-3881-35f0-b300-f40e0c173176 | -5.7429 | -57.6009 | 2025-08-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 54097e02-84fe-3260-a26b-718de04dbc1b | -6.1308 | -43.1432 | 2025-08-23 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 7d90b69c-dec5-3671-98da-ba4dcd14704b | -5.7431 | -57.5814 | 2025-08-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 194.1 |
| c27ed3c9-e895-3f70-a0ef-afc1edfe9f61 | -7.9447 | -63.0528 | 2025-08-23 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| aeccc32c-4837-3a09-9507-fae87b283511 | -15.0183 | -54.8942 | 2025-08-23 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6667918c-86bb-3786-b099-f283caa9ef9e | -9.1897 | -59.6171 | 2025-08-23 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 56f17209-144e-32bb-9edb-58f6520af607 | -6.6044 | -44.5624 | 2025-08-23 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a1447289-b929-3c97-b9c0-39217563fc76 | -12.7078 | -48.1206 | 2025-08-23 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 304d2edc-361e-3559-960f-5a6d68777ffb | -6.3698 | -45.5582 | 2025-08-23 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c8ef6b9e-ac51-303f-a216-53a3ba61fc21 | -8.9388 | -40.6336 | 2025-08-23 14:10:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 8fafb316-6bb8-38a8-b5f1-78403b282198 | -7.6484 | -45.2446 | 2025-08-23 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 41ed3acb-9330-3844-8670-e63db6153f66 | -12.1949 | -50.2397 | 2025-08-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| ede22c82-18db-39ef-b0e7-ee0fa8734a27 | -5.4365 | -60.1588 | 2025-08-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c6b0343c-d6b8-3efb-9b65-1e5d284f9a93 | -9.0494 | -47.6332 | 2025-08-23 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e34b5fda-004b-31bf-9ab2-715cafa29560 | -8.3197 | -47.3077 | 2025-08-23 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 292fca35-13f8-3542-938f-5043b618c724 | -8.853 | -49.8843 | 2025-08-23 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 64cfc342-cc92-30be-81b9-8bc3177b89a0 | -11.1204 | -44.7681 | 2025-08-23 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 2d4a4028-9c8c-344c-8258-ada1faefe81a | -5.7429 | -57.6009 | 2025-08-23 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 66d8bda8-239c-3f06-921e-c2f400e39040 | -6.5856 | -44.564 | 2025-08-23 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| bdddfb53-33cd-31b8-8b64-6363ad127a75 | -7.6366 | -46.2823 | 2025-08-23 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5bd5ee9c-c292-36d6-8788-8ed749b1a092 | -8.5944 | -62.6126 | 2025-08-23 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 029b79a9-1fa6-3f93-8b1b-bc4db7f8aabb | -13.4775 | -47.0453 | 2025-08-23 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0bf96f74-6a5e-3005-93b3-9b5f22685363 | -8.5943 | -62.6315 | 2025-08-23 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7721d612-b839-3ca1-a4af-805244e519d3 | -7.2715 | -43.6714 | 2025-08-23 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 80a84ddf-58bf-3349-832a-3ecf81e3747d | -11.14 | -44.7422 | 2025-08-23 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 9146d0d4-2c32-3ded-9afe-b7bb8b5e30c0 | -8.7597 | -46.7101 | 2025-08-23 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ea191acc-a207-35de-93ee-4afeda4ddc20 | -7.0164 | -44.6413 | 2025-08-23 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4f395c51-df99-35ca-b9f9-b68e785dc472 | -5.7615 | -57.5807 | 2025-08-23 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| ac3c12b1-88b8-3469-bf40-22e7c8c87049 | -11.1396 | -44.7654 | 2025-08-23 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| dd477a9b-2a0f-3455-ba25-c45beda057b4 | -6.8733 | -59.8213 | 2025-08-23 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f5d9f4c4-f279-378d-859a-88ce68413ebd | -8.3009 | -47.3094 | 2025-08-23 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 4e92a201-d1c8-3d10-b748-59a05657d30f | -5.9062 | -45.1185 | 2025-08-23 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| cb5d0a0d-0584-3fce-874e-6fc2119234a3 | -12.5418 | -45.6189 | 2025-08-23 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4918213f-5da7-3a29-adb7-fce9b3e45a84 | -9.1712 | -59.5987 | 2025-08-23 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fbcae2fc-3f6e-3169-9838-85ef95148af1 | -8.527 | -48.8609 | 2025-08-23 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 08b46ff5-030d-32db-ab21-ccdd342f8fab | -14.6899 | -54.912 | 2025-08-23 14:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 57b02e15-ef1d-345a-8b23-a32747f77382 | -13.4349 | -46.2573 | 2025-08-23 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 3ab8f81f-e34d-312a-b684-cc22fe12c5c7 | -10.4784 | -46.831 | 2025-08-23 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 1288a67e-3f8e-3aa3-a97b-b2e068823aba | -7.0352 | -44.6396 | 2025-08-23 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 66ab30f3-8935-333c-a571-633290caac0e | -10.6962 | -50.1314 | 2025-08-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 5f820cee-b8e0-34c7-946b-379228100c06 | -15.2288 | -53.8481 | 2025-08-23 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 06ea603e-4221-327b-898f-aa72d57ed19b | -10.6388 | -50.1803 | 2025-08-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6cce303c-4068-33d7-ab9d-f685349025d8 | -6.3887 | -45.5342 | 2025-08-23 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5b25fdb8-fde2-36b1-937c-8158a2e7081f | -8.5272 | -48.8393 | 2025-08-23 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 79.9 |
| b34937b4-54f5-3d28-9d81-6fce6e041ddd | -7.6296 | -45.2464 | 2025-08-23 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| be0de3ff-4102-3e92-91ab-eee38d015822 | -6.5781 | -59.871 | 2025-08-23 14:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 35cc4057-c6f6-37bc-8ba1-dacfc4e73165 | -12.9921 | -45.2252 | 2025-08-23 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 22862b8c-509a-3508-abb2-5969d541cb12 | -6.5858 | -44.541 | 2025-08-23 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 520ec49e-a4f1-38e7-844f-ffeef18cf96d | -15.0183 | -54.8942 | 2025-08-23 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 37242899-25bf-376c-86e6-b031e8e4d9ed | -8.613 | -62.6118 | 2025-08-23 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2448d483-8606-369a-85b2-a81561e762f5 | -10.6201 | -50.1609 | 2025-08-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 297e85f5-4b07-3cfd-a950-81abfaefcf4e | -5.7431 | -57.5814 | 2025-08-23 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 207.3 |
| b6c17d80-c701-393f-abd1-69b913ab6308 | -6.3698 | -45.5582 | 2025-08-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 1c28f754-2cbd-3a7e-a321-282d1e0a933c | -7.6296 | -45.2464 | 2025-08-23 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 715356ca-b163-35ae-9746-d14406b8161b | -6.6044 | -44.5624 | 2025-08-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| eb49c2d5-f4cc-3ec8-aa40-d5b061945509 | -5.7431 | -57.5814 | 2025-08-23 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 222.0 |
| aff5d316-a4c8-3603-ab8a-f62790f0906e | -11.14 | -44.7422 | 2025-08-23 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| c49d5111-9261-32bf-a6ef-56fdcc8dc93d | -13.478 | -47.0227 | 2025-08-23 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4cab4fef-0540-3d11-9f46-d24e1bd65060 | -6.8733 | -59.8213 | 2025-08-23 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 31f3e59f-a00a-3ba2-976f-7bf90ac26cdb | -11.1204 | -44.7681 | 2025-08-23 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 3c2abeeb-ddc8-361a-934f-b4372ce2da73 | -7.9448 | -63.034 | 2025-08-23 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8e1b9df9-d8be-3e25-99d3-0432dbd23583 | -14.3893 | -52.0574 | 2025-08-23 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 008a1767-de17-3188-b0c5-70ffbb5cdc67 | -13.4155 | -46.2604 | 2025-08-23 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |


[Clique aqui para ver as próximas entradas](README91.md)
