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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae940900-39b8-34af-834d-3a9491c0eb5f | -17.14 | -46.85 | 2026-09-01 16:15:00 | MSG-03 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e8d04e11-044b-3b57-a96e-944f5de77ea6 | -3.87 | -44.07 | 2026-09-01 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a66f1ae2-1390-300d-99f7-5e9d65d7a3d0 | -14.8 | -41.66 | 2026-09-01 16:15:00 | MSG-03 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 39cb3db8-3066-38ca-83b0-7ddbcafcc20a | -12.9 | -45.79 | 2026-09-01 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1c42403-9058-37cb-be16-1e8ea4bb543d | -3.87 | -44.02 | 2026-09-01 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20fe4765-7d5f-3ea7-9791-9a5eb7225930 | -9.4422 | -67.4164 | 2026-09-01 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| e912a66b-7d16-3dbc-b5b9-b29e8e1f00f4 | -7.529 | -61.3635 | 2026-09-01 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d1ba605e-608e-3efb-9924-b52b9df007ff | -10.3574 | -50.0171 | 2026-09-01 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 6890a3f1-2843-36ff-a66a-e815aaff25c2 | -6.9515 | -59.0473 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 71558f8e-7da5-33fc-bba9-14ad63e5121d | -7.1822 | -60.6713 | 2026-09-01 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a664ea1b-4316-35fa-9f41-77c91a729c61 | -5.9636 | -57.6704 | 2026-09-01 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a30f6e7b-0532-34a1-919e-e02e7ce8e5ac | -3.1997 | -61.1799 | 2026-09-01 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4331215e-8892-31c9-a0b5-6bc22661eebe | -7.5526 | -60.4651 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 54ed8f85-af94-3740-a7fa-275a71c2d28f | -6.9113 | -59.6275 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 469c63b2-eb6e-3eb8-8ae3-e4d834451c94 | -3.79 | -59.3031 | 2026-09-01 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f03b5bc4-bc03-363e-be53-aca391791cfd | -3.3872 | -59.3692 | 2026-09-01 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 59d5cf5b-7b62-3424-bc4f-f5a8e50da10a | -6.6541 | -59.4452 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| dbbccbe5-db25-35ff-8b1c-5061a6ebf97c | -7.4549 | -61.4044 | 2026-09-01 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9c3375f9-e780-38b0-9a37-198f36fc931a | -6.8598 | -58.9545 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e7036189-1923-3b7c-9e1f-50623ff0c3f5 | -4.1516 | -60.6878 | 2026-09-01 16:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cf048d0f-0f6e-3db0-b015-37052fb53a13 | -12.1899 | -50.5623 | 2026-09-01 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 940143be-8cad-3602-95c9-97663479506a | -4.1515 | -60.7068 | 2026-09-01 16:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 04421187-7201-3917-a1f9-9ad67cb5858e | -6.369 | -54.7655 | 2026-09-01 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ea4fb39f-7d01-351e-95e8-3d2137eed2f7 | -3.1998 | -61.161 | 2026-09-01 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a5096faf-fb2d-358e-b460-3c68d0343d23 | -5.5649 | -60.193 | 2026-09-01 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 284.2 |
| ee60002b-ffac-379c-b000-a8b148088eff | -8.2041 | -54.9625 | 2026-09-01 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 578dd7a0-eda5-3ee5-8492-11a57b89ca5e | -11.2295 | -51.2667 | 2026-09-01 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 937b8581-89e4-3f90-bc18-55109111ef5d | -3.4185 | -61.3273 | 2026-09-01 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| cb9307d0-ad56-33fb-b428-c34aac411433 | -7.5289 | -61.3825 | 2026-09-01 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| f08e8eb8-f035-3471-9967-2e1f09998519 | -3.1267 | -61.1811 | 2026-09-01 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 89150052-00f1-36c7-ad53-5ede4aa148fd | -6.6233 | -58.383 | 2026-09-01 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f4c0185f-d985-31c3-a034-19426109bc50 | -7.5475 | -61.3627 | 2026-09-01 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1a7e5c02-3db6-34c9-81dc-118bcaa75be2 | -7.2932 | -60.6096 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0c816821-8bb7-3770-928b-614b80fcb7ff | -8.9242 | -63.2804 | 2026-09-01 16:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b286e80d-6417-3f91-9278-9668e559b87d | -6.9482 | -59.626 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 9e2afa15-ff08-335f-83dd-7d01e19ae6ac | -6.8247 | -58.6461 | 2026-09-01 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 67abce65-476e-32bd-a598-a9aa06a3006a | -11.2764 | -50.6243 | 2026-09-01 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7626fa5c-4cc3-35fd-96a2-1486933384b7 | -6.9112 | -59.6467 | 2026-09-01 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| d4c3bb7a-d570-375a-ac34-b543132a8cd5 | -5.565 | -60.1739 | 2026-09-01 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| cdf8530c-2c88-3653-a9c2-23d058722ad7 | -8.7628 | -46.4642 | 2026-09-01 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 26fac3a1-2a32-3bd2-9711-cd1735d75d66 | -3.4294 | -64.6914 | 2026-09-01 16:20:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3cca0f6e-733c-3b95-8ce1-1773c6a40872 | -3.1266 | -61.2188 | 2026-09-01 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 66997468-c5c2-395b-a9f2-7a0f2e88f21d | 1.0951 | -50.9778 | 2026-09-01 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 267c762d-cf7a-3a37-b89f-65dd7b1cbf20 | -14.6732 | -53.5408 | 2026-09-01 16:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 97f27d3d-ed7e-3204-9af0-8434eae2f678 | -5.9451 | -57.6906 | 2026-09-01 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 5e8f53d6-87f6-3d00-958a-0927be526418 | -3.4392 | -60.3985 | 2026-09-01 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| ba9a6b66-8cb0-3204-8e99-d1ae04e81a39 | -11.2954 | -50.6222 | 2026-09-01 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 48ba7f01-8cd2-37c4-96b9-22d6dfae1dda | -7.3635 | -73.2632 | 2026-09-01 16:20:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a0c19778-a801-3f32-a29f-e5a9346fd438 | -5.2351 | -60.0502 | 2026-09-01 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 5758f75d-42fa-3edd-99e3-a2d650fd158c | -8.7784 | -62.8514 | 2026-09-01 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 61156080-e261-3419-a5ec-3e736698c3bf | -3.4002 | -61.3465 | 2026-09-01 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 1d3fa9ab-982c-3c3c-9935-5e176eaf65ec | -3.4185 | -61.3461 | 2026-09-01 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 1556213a-656a-383e-bfef-983ef37093ab | -10.7856 | -50.5066 | 2026-09-01 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 09e51d87-e282-30a4-9cac-92654c2df862 | -9.5238 | -65.7008 | 2026-09-01 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.2 |
| b3371f94-53bd-3482-b4b2-467b3ba9daa1 | -7.2007 | -60.6515 | 2026-09-01 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 18faa330-a562-3401-9f98-fe6dfb2d9f66 | -3.4475 | -64.7467 | 2026-09-01 16:20:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ed239765-2af8-34e2-bc7b-9f505b23ca59 | -7.2536 | -61.1074 | 2026-09-01 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| bb319586-effb-3276-97d2-a38720ed591b | -7.5104 | -61.3832 | 2026-09-01 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 60ce8c1c-9c43-353f-a162-868b6cb27424 | -3.4002 | -61.3465 | 2026-09-01 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1d465c3d-58ec-32ab-91a2-6bab78151788 | -3.4185 | -61.3273 | 2026-09-01 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e127af02-2ed8-3bd8-8533-8d3c0f04433c | -3.6631 | -58.9027 | 2026-09-01 16:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 2948ab87-7a33-31b3-ae06-6e3771029c3f | -7.4549 | -61.4044 | 2026-09-01 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 1bb43fb5-5718-3ded-a6b4-7d842eb46608 | -5.2984 | -62.6432 | 2026-09-01 16:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4c2fb20a-f447-36d1-92a5-ef4a58edef24 | -7.4803 | -63.7267 | 2026-09-01 16:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c8374999-2448-3118-a34c-785ebb51487f | -6.8009 | -59.5742 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 202af309-c1bf-3c52-8329-0c44bc0d1fec | -11.2577 | -50.605 | 2026-09-01 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 955adc82-900a-32f2-afe7-5f7c99af3e15 | -7.529 | -61.3635 | 2026-09-01 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b5b2d4ed-a24d-3b90-bc36-0be36d67df87 | -11.1723 | -51.294 | 2026-09-01 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f78541ae-3c78-367e-94b7-774d8cb0aa0d | -11.175 | -54.001 | 2026-09-01 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 724d71e3-6684-30af-8ad9-c3bcb31af1c9 | -6.6937 | -58.9613 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 24641558-ce0c-357f-8766-d64d1243ab6b | -5.9451 | -57.6906 | 2026-09-01 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| dd7aabe4-a2a2-3353-9465-351ac8fe025f | -3.4185 | -61.3461 | 2026-09-01 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 38fe50fd-0503-336d-8478-78bb792f2878 | -6.6541 | -59.4452 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9ac96026-17cf-312a-a08e-82ff51336ec1 | -7.4364 | -61.4241 | 2026-09-01 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2841fae1-48cd-3a1b-a98f-8dcbe97a8888 | -7.5475 | -61.3627 | 2026-09-01 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| faf8e192-9172-3084-ba4c-6ab652f60462 | -14.6732 | -53.5408 | 2026-09-01 16:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| ee200e0f-e9d1-3b55-916a-82ae390453bb | -5.5649 | -60.193 | 2026-09-01 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 234.1 |
| e39ddf10-037a-3e17-952c-824f95ee20bf | -3.1083 | -61.2191 | 2026-09-01 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| fe1f62fd-000b-3f3e-9579-951e714fd150 | -3.4392 | -60.3985 | 2026-09-01 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 041a6448-c347-32a2-8c0a-ad553637434b | -7.5289 | -61.3825 | 2026-09-01 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| b0722540-3a0b-3903-b0ce-8c083e193eef | -8.8758 | -71.4622 | 2026-09-01 16:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 47.8 |
| cde55f74-0767-3242-83df-a8efca3bc85d | -11.2954 | -50.6222 | 2026-09-01 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 1908097f-77b2-350f-ab15-5e821e8e604f | -10.1321 | -45.8825 | 2026-09-01 16:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9b8d3699-1834-36fa-b715-77a6ed18d21f | -7.2007 | -60.6515 | 2026-09-01 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 9943ddac-d139-32aa-8790-5f2312cd8b47 | -6.9515 | -59.0473 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c4a31cf1-7347-322c-8747-bb1f175e7815 | -7.3634 | -73.2814 | 2026-09-01 16:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 65.8 |
| af51868e-8188-3950-bf5d-67612b346792 | -15.1827 | -46.2336 | 2026-09-01 16:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 5eb5804a-b287-3bd0-a7ad-b0cc2b723e68 | -3.4002 | -61.3276 | 2026-09-01 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3b8bd7be-2c91-346f-a5bd-b8da32f71229 | -6.9113 | -59.6275 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| bf63ca2b-0372-33ff-a8c5-58898e650d2e | -7.2192 | -60.6507 | 2026-09-01 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 019a02ae-db5b-32dc-9007-1f14b5caf051 | -3.1266 | -61.2 | 2026-09-01 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 978f7dea-18b9-33c5-8808-b5b21f947f82 | -8.7784 | -62.8514 | 2026-09-01 16:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e3b067bc-2562-3f1e-bfce-6587085682e1 | -5.9636 | -57.6704 | 2026-09-01 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 19397567-8179-3d33-a84c-21e24fa32dd4 | -9.5238 | -65.7008 | 2026-09-01 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 2a608575-ad29-3a1b-a9cd-f8ed92426d53 | -7.3635 | -73.2632 | 2026-09-01 16:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 61402bab-5d9c-3dfd-b970-fd8c60efa844 | -7.5659 | -61.362 | 2026-09-01 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 143.1 |
| e4c7d3f8-c7d5-30c3-9a48-8ba3811533f3 | -3.1267 | -61.1811 | 2026-09-01 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 4cade49a-374b-3119-8a4b-8cd5548de4a4 | -10.1324 | -45.8598 | 2026-09-01 16:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 68f37a40-75c3-3b62-9928-0b4a1dae2621 | -7.5526 | -60.4651 | 2026-09-01 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c8535364-49ba-3304-9f21-207a07752a24 | -8.7628 | -46.4642 | 2026-09-01 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |


[Clique aqui para ver as próximas entradas](README112.md)
