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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4894376-0b77-395e-85d6-b01f66f7f302 | -8.69229 | -48.44198 | 2025-10-07 00:13:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 174ce3eb-9a91-3c79-87cf-701d246ddfa6 | -7.68993 | -42.39923 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 2e6308bb-4e74-3b80-98f1-e8ec358850e4 | -7.58105 | -45.93092 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| dbb4672a-5da5-3da7-b97e-a86055e1acdb | -6.06349 | -42.56929 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2a4d4f44-0f82-36cc-8ded-cfc10338f7b6 | -7.22999 | -46.45825 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c8c8bbb9-7d32-31e8-8507-d7cad8545849 | -6.24784 | -43.27816 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7f6e42f2-9250-3fc8-b139-8f56024c4e25 | -4.91716 | -48.01666 | 2025-10-07 00:13:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 745ebf11-047b-34ae-b343-59b461f03337 | -5.75549 | -43.38565 | 2025-10-07 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 97ee80dd-172d-3ac5-84f7-392785d8bd5b | -6.16783 | -42.58833 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cb30befc-75c5-3910-8a95-6926f85830e7 | -5.80511 | -46.55432 | 2025-10-07 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7943839e-70d4-3ec2-bb24-43b865a1df1b | -7.6979 | -46.25553 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f90203e2-2479-3205-90ed-36c3e6fcb310 | -4.49128 | -44.299 | 2025-10-07 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 94c5d733-01d9-35f0-a7c4-79aab2ae511a | -8.51729 | -46.33519 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d85ca62b-3968-3b56-9343-b8d319ba77ff | -8.17916 | -50.31673 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| a9353765-f799-390d-84c8-46e043083053 | -9.0355 | -50.58118 | 2025-10-07 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6b01e323-4722-3440-b4ea-d6fea035308b | -5.4167 | -41.08369 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 48aa12d3-7eb8-322e-87e4-9cc536516974 | -6.37815 | -46.42862 | 2025-10-07 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 08ee04cf-c253-342b-8f34-4008d8f69ef7 | -5.30358 | -41.57441 | 2025-10-07 00:13:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a77db138-694c-35ff-960e-aa0c16058940 | -6.70354 | -42.85011 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 71ca0acf-f086-38ce-9d94-8fb969a46058 | -4.61572 | -43.14788 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e4e5c647-1a9c-39ff-91b5-3a0b5430cfbc | -5.41495 | -41.07167 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 99af9d52-4921-34e4-8fac-d91289c7896d | -3.12237 | -40.99029 | 2025-10-07 00:13:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 622edb56-5c4f-3303-b2eb-e674f0c77414 | -10.38414 | -50.30455 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| e640a972-3472-370e-9b09-9d1932896c0d | -5.81829 | -39.19479 | 2025-10-07 00:13:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 0c6f9ffc-a7cd-3d13-a0ee-83a9b4f69f73 | -5.63369 | -42.72247 | 2025-10-07 00:13:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cc7b21dd-95ea-3c67-8f78-86e391fb2ebe | -8.56873 | -50.08253 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 201bb853-5e6d-3b12-b025-253ea7d9046a | -6.41415 | -43.60882 | 2025-10-07 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f066a14-022f-3c17-ba72-d3f981753bb1 | -8.4938 | -46.34432 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 91db73b2-1b03-36f4-89b0-626213b14933 | -8.54416 | -46.24861 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ede0bc9b-fcbd-3816-9321-a3ea5532b4c8 | -8.17765 | -50.29078 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e9fd3838-4a2c-3715-a790-467fc114e341 | -6.45774 | -44.58409 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 954cd026-4bd6-381a-86ad-a6e1cb28e77d | -3.0887 | -50.57289 | 2025-10-07 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a6d0029c-e216-3bc3-8591-096f042dc742 | -3.19653 | -51.01622 | 2025-10-07 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 00934890-6af3-374f-9fda-b0f6a3d214a3 | -3.52583 | -49.706 | 2025-10-07 00:16:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4ddd967d-d80d-3d9a-bd30-04363652aca9 | -3.09089 | -50.58965 | 2025-10-07 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 7cf672c8-5853-3f2d-9c89-c245c7985d5d | -3.52327 | -49.69791 | 2025-10-07 00:16:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 08d769bd-3e37-349d-b000-b22c6f0bc134 | -3.52527 | -49.7124 | 2025-10-07 00:16:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 59884392-19f0-3404-92f3-2c828153d1f5 | -4.11218 | -50.05649 | 2025-10-07 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0a53b94b-690c-36cb-9347-b419af5d41f0 | -3.14406 | -50.44832 | 2025-10-07 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7479ecfc-25f4-38ee-9fb9-59e6fd7e063b | -1.24617 | -46.03435 | 2025-10-07 00:16:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 807eef9a-4af1-355d-94f5-4ff82301135c | -3.08241 | -50.58021 | 2025-10-07 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 16154aa2-29a1-3e6a-96a1-5f87a46cb59e | -3.09425 | -50.57855 | 2025-10-07 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 52bcdb0f-d0ae-3aa4-8c7c-ada6646cf8d4 | -4.11005 | -50.04086 | 2025-10-07 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d208b3ff-8fb7-3dfd-87ba-fb041a588759 | 1.28345 | -50.819 | 2025-10-07 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9deac6f9-6949-32b7-b707-3896d59db0ee | 1.26296 | -50.9679 | 2025-10-07 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 503585b3-3fa0-34b8-bc95-9d886d39f141 | 1.28314 | -50.82535 | 2025-10-07 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5ff08014-f79d-365c-a6b9-4ff364391f0b | 1.26371 | -50.95901 | 2025-10-07 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a1417753-a58f-33df-9f62-58cfa703bdbd | -22.1621 | -49.3737 | 2025-10-07 00:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 79c4ea6f-9716-332d-9dd7-9d0600190784 | -4.6504 | -43.2038 | 2025-10-07 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 41fd5fa9-d581-3e4f-825e-ebe3465a8c2e | -8.613 | -44.9189 | 2025-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 6460d338-b097-3415-89fb-8298437905e1 | -10.8728 | -51.0501 | 2025-10-07 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 30938172-1a8f-3dae-8208-ee40c56f32ed | -10.8542 | -51.0308 | 2025-10-07 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d202808f-304b-3cf4-afbd-1e97fd21e02d | -4.6875 | -45.828 | 2025-10-07 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 3c7d4c5e-8ffc-3180-9139-1af7daaf0d7f | -6.2421 | -43.2743 | 2025-10-07 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 799fc31c-1faf-34b1-9340-90a13cfe1756 | -18.157 | -53.37 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 2aaf9658-fec1-3f30-8786-95172ef16a3e | -8.6519 | -46.2964 | 2025-10-07 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 65256a01-0c54-3818-ba09-fe311dedd65c | -22.1829 | -49.3688 | 2025-10-07 00:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 164.5 |
| e7eb9ae0-4d62-3b60-99bd-a4824351f465 | -4.6505 | -43.1805 | 2025-10-07 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| dea4077e-08cc-32c4-825c-2c4d2808ce3c | -11.9496 | -45.4783 | 2025-10-07 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1c6c1719-3764-30fc-8f59-6ad791a66725 | -16.1217 | -48.9227 | 2025-10-07 00:20:00 | GOES-19 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 0a20d502-0310-3830-bce9-87a43e72ba16 | -4.4633 | -43.2152 | 2025-10-07 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 38d766d6-9330-3373-87f8-f0c703124dc1 | -8.6133 | -44.896 | 2025-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| cca5c54e-8536-38e3-a9c5-eabbcbe1de19 | -22.0077 | -49.709 | 2025-10-07 00:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 6a8d640e-1814-3f72-8c4e-0752eb49a988 | -21.4993 | -46.005 | 2025-10-07 00:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| 93b00cc4-f6d6-38b9-b91b-e665f11a0e44 | -4.4446 | -43.2164 | 2025-10-07 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| a0b64f0d-d06c-37b0-b334-a78a39895121 | -15.6198 | -52.5715 | 2025-10-07 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 167.2 |
| ed6c330a-f02f-36a3-9e52-5ce080644780 | -22.1822 | -49.3921 | 2025-10-07 00:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e7eebb7a-7c7b-3b4c-94bf-8adea39fbe01 | -18.1172 | -53.3763 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 62e0fb17-b01f-3ec1-be78-f99bf7dcc5d4 | -8.633 | -46.2984 | 2025-10-07 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9e8e5f3d-cc20-3af3-bfcf-d13b8011c121 | -6.4543 | -44.5749 | 2025-10-07 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 364c0878-3640-3b1d-b762-15ec51468033 | -14.8832 | -51.4561 | 2025-10-07 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| c14f76b7-e8f6-33e5-bc8b-127354502e15 | -10.4102 | -50.311 | 2025-10-07 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e8050bf3-a1e8-395a-b55d-71499a0c91f1 | -4.6873 | -45.8504 | 2025-10-07 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| dcd964fa-ee50-3e5f-8f26-cc40d8cdbc98 | -3.0864 | -50.5835 | 2025-10-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fdb24923-9995-30a5-8e6e-f9d43ac5a3da | -22.3128 | -49.8915 | 2025-10-07 00:20:00 | GOES-19 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| 4fd8fdcb-4f83-3431-8771-321b0b1dd921 | -6.5849 | -44.6327 | 2025-10-07 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8238290a-e520-3128-8d58-dbf8fbcdb75e | -8.6333 | -46.2759 | 2025-10-07 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 79dcaf29-e3ea-3d89-932a-3724ca2efdec | -15.6003 | -52.5742 | 2025-10-07 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |
| ceb3ebc6-83a2-3950-903e-54212b9b4664 | -14.8835 | -51.4346 | 2025-10-07 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 288.8 |
| d29f0ed1-575f-3c77-aca6-e2f8048c33f4 | -18.1769 | -53.3669 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 920424aa-3ded-30dd-b3ec-fc81b589f100 | -5.4937 | -43.0761 | 2025-10-07 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5d8f253b-0e7f-3eff-a36e-38deeb1bf80a | -11.7401 | -43.2928 | 2025-10-07 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 149.7 |
| 61021201-fc04-30f8-9190-a7acb002efb7 | -5.5125 | -43.0747 | 2025-10-07 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 85228311-ff17-3818-af2e-386a99a788b5 | -22.1614 | -49.3969 | 2025-10-07 00:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 92.7 |
| ed056b45-6a76-3b92-97e7-45c02a2a9e7b | -22.0071 | -49.7321 | 2025-10-07 00:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| bae8979b-9a91-3fe2-9dc2-b1393de66504 | -8.1927 | -50.3019 | 2025-10-07 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8a7f491b-93fe-3ade-9b89-570fc4ddcab9 | -15.6007 | -52.5529 | 2025-10-07 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 2f29c8ae-7639-3ce3-bfea-9d222bc919c3 | -8.6521 | -46.274 | 2025-10-07 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 31ab6b24-e20e-3f3b-a12c-3a634985fa98 | -22.3337 | -49.8867 | 2025-10-07 00:20:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| dd10d8af-cbeb-3d76-a96a-96bf6bca4763 | -14.8641 | -51.4373 | 2025-10-07 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| def59d97-8298-37c7-b48e-8afe9545d06d | -8.6127 | -44.9418 | 2025-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 8b62c77e-041a-3f1c-bd78-427376965207 | -14.2759 | -45.8416 | 2025-10-07 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 7bec174e-2a48-332f-b252-fc819422b3a1 | -14.9212 | -51.4937 | 2025-10-07 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 83fb971f-6d76-3375-a604-b9435b613edd | -10.8731 | -51.0289 | 2025-10-07 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 47717139-ba03-390a-a589-c0d6fc27b67c | -10.3916 | -50.2916 | 2025-10-07 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 61236126-84d6-3687-a8e5-7bc4b181cc21 | -4.4632 | -43.2386 | 2025-10-07 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 13a956d5-c678-3305-b46c-87c0bebc0d55 | -18.1565 | -53.3915 | 2025-10-07 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d4a7d679-c16d-3b11-93b3-43311fa31958 | -14.9406 | -51.491 | 2025-10-07 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2851aaff-5fef-3eff-a440-adaf65c904a4 | -14.8839 | -51.4131 | 2025-10-07 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c3a620fe-eeda-3e58-8f9f-5ac06e687026 | -4.4445 | -43.2397 | 2025-10-07 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |


[Clique aqui para ver as próximas entradas](README10.md)
