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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c63b0f7-e3b3-31d1-be4c-cd5759a791b7 | -6.94678 | -43.72573 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a8a1f5b-1a45-3f1e-8223-3858f412c0a7 | -6.92573 | -43.70812 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4b5f787e-d36f-3269-ab97-4e654baf6616 | -6.50108 | -42.23532 | 2026-07-07 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d74ef402-5d67-394a-ae38-f3acb59b608c | -4.28357 | -48.36279 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2d9e15b-0b9d-3b1b-9faf-eb231347e728 | -6.92463 | -43.71507 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| af779d8e-32fa-328e-bc95-08f15af46f46 | -4.38173 | -43.36104 | 2026-07-07 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61346204-c114-3665-a412-43b70d3f82c2 | -7.01047 | -42.78753 | 2026-07-07 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1bf162c-a817-38c6-a208-ce62b43305f3 | -7.71917 | -49.64087 | 2026-07-07 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ed47d18-bbcd-3732-a836-2e33bbe8e44f | -4.57527 | -48.02685 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 149df321-34e5-3f1e-ab13-078c9b3bb150 | -7.63828 | -50.03109 | 2026-07-07 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b52908db-caf7-34de-9355-eac766de857c | -5.80129 | -43.80056 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 802a041d-cd46-3ea1-904a-50fc4bcd8beb | -2.32465 | -48.58583 | 2026-07-07 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c9a6b14-4ade-356c-9c76-dd5839fba0ba | -4.85572 | -39.81072 | 2026-07-07 04:23:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 58bcceab-8948-3eea-8dbc-3f35b9a1dbb2 | -8.07459 | -46.6913 | 2026-07-07 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e903941-a57e-37df-9a32-dbe730776486 | -5.75576 | -43.192 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb6990ac-9798-3fa3-8ff6-d31af4f0d0be | -6.93238 | -43.70918 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0bb8f5d-9892-36eb-914f-954b740545ab | -6.2079 | -42.51464 | 2026-07-07 04:23:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4302a737-4843-35e0-bb40-e3375e95a63e | -7.64347 | -50.02753 | 2026-07-07 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e53f2a08-e7e6-3475-87cf-bb9cb2ffff01 | -5.75419 | -43.26629 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bed77c71-d992-335c-bd5c-0c9f495a5f9e | -5.83273 | -43.47392 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29414636-9f36-372b-8332-30e5d3b73acd | -6.93404 | -43.69876 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d0a9363-d4d6-3ff4-80d0-018ddb90bc3b | -6.20457 | -42.51411 | 2026-07-07 04:23:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1afce97f-b159-3c7b-8279-28aa174d2234 | -6.92518 | -43.71159 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 45a28b12-f489-37b5-9b8c-8e0e0646b4b4 | -3.87833 | -42.97557 | 2026-07-07 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb887969-9b8e-3830-bd03-3e92faf931a6 | -4.83272 | -44.07558 | 2026-07-07 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcfbe800-bd02-3f39-928f-f717ce1c06b2 | -6.9357 | -43.70971 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eba51c78-36c1-30a1-a079-3f0c1420900b | -6.9141 | -43.71696 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2c72a7a9-6a22-37b8-864d-7afa29ef2020 | -6.93626 | -43.70623 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a76ce88-2f08-35d9-9027-fc9fe9934d31 | -6.50158 | -42.20999 | 2026-07-07 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7201bea7-4c2b-3d11-ada2-a64bf682df26 | -4.23034 | -44.78503 | 2026-07-07 04:23:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb84c5d6-baaa-3deb-a7ba-7d2a448f7880 | -8.12377 | -47.11337 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d41b750b-d663-34e9-a293-af7fe265e68d | -4.57386 | -48.02975 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fff26ee-3398-3dca-8410-30020310bb7e | -6.49882 | -42.22773 | 2026-07-07 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3426d352-bfc6-3b90-837f-9a488387aa0e | -7.90713 | -48.25237 | 2026-07-07 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dad419cb-83d8-3807-85e5-55a8c4ba9eb6 | -4.82828 | -44.06033 | 2026-07-07 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e82e5d45-5f3e-3afb-bbe9-42a415e1ab88 | -9.5056 | -36.547 | 2026-07-07 04:23:00 | NPP-375D | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4965edb-481c-363f-87b8-7941d6c30a7e | -5.97877 | -43.61779 | 2026-07-07 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0f8a345-852e-367b-b987-5500991959f3 | -5.80407 | -43.80457 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 147a4d2f-bde0-38c6-a490-3688df8abc52 | -9.36609 | -40.42641 | 2026-07-07 04:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d5ae000-379c-3d46-8e8a-ac195ea1f0af | -6.29305 | -43.64311 | 2026-07-07 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3ea1ea9-c439-3dcb-b9a6-5d376e656e60 | -6.90746 | -43.7159 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7703cea9-6afd-3291-a442-04411a599ecc | -6.92961 | -43.70517 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 97ba588f-cf2c-362b-9d68-b57062887387 | -6.43972 | -44.57489 | 2026-07-07 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f956c2e8-4e50-35dd-bf29-e16841233f71 | -3.97902 | -48.42899 | 2026-07-07 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d20c7ab0-bfa6-3a16-b2f4-06d5284daade | -4.76782 | -41.79589 | 2026-07-07 04:23:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cc34109-c97f-3a7f-a13f-7d7e3cfafb1e | -7.64863 | -50.02403 | 2026-07-07 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3991358-8118-352e-8fde-19e3200b8087 | -6.90236 | -43.70813 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c66ef0b-b14e-3d4d-9964-58335c7ab7dc | -4.71102 | -47.98247 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0951de8-466c-30ad-820d-4b9e08c4b696 | -4.57448 | -48.0261 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21254228-0dad-3ef9-bf46-e381f7b754cc | -5.52412 | -50.0211 | 2026-07-07 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e04d30-03dd-32e5-bf25-f1e447da1fa2 | -5.83218 | -43.47739 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dbae7ed-4e98-3ec4-91e8-4302fddf3d3c | -4.83221 | -44.05732 | 2026-07-07 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6c98e40-4a9f-3534-a6a8-83367206fb3a | -8.07322 | -45.58115 | 2026-07-07 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aa2c83f-1342-323d-8672-21cc9046ca6a | -2.32462 | -48.58394 | 2026-07-07 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c280210b-8c3f-3112-963f-8e82243e4957 | -6.93349 | -43.70223 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e632bbed-fc32-373a-b0b2-6fe4a35db43b | -3.15506 | -48.58754 | 2026-07-07 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecdf66a3-e2b0-3fa1-a024-22f8b42b2a62 | -6.47332 | -42.93556 | 2026-07-07 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 933670a4-112f-3619-867f-41ff3ccdb4bf | -4.5706 | -48.02987 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2daefc31-78d7-364e-a3af-bee0cbcc0475 | -5.50593 | -44.08048 | 2026-07-07 04:23:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc5ef2e0-08eb-3426-8612-af1a4f4db109 | -7.006 | -42.77248 | 2026-07-07 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e07a1fb2-e830-3e52-81ae-53c4742a27a6 | -4.57855 | -48.02676 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5f4c72a-3d61-3be1-a32a-c62f32d6e819 | -4.28835 | -48.35979 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ca2e7d71-d600-3732-a0e7-3a99ff5e8139 | -4.34763 | -47.76734 | 2026-07-07 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a32ced7b-0a6f-3d3b-9990-3945ed3621dc | -5.50985 | -44.07748 | 2026-07-07 04:23:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e3e5457-6c38-3064-972b-bbfc7e49360c | -6.9058 | -43.70494 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6707239a-37ec-3df0-bf1d-522f78d624d8 | -5.52334 | -50.02578 | 2026-07-07 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a634b78b-1da8-363a-b571-fc7d4c2d8248 | -6.49827 | -42.23127 | 2026-07-07 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8089ca25-8e3d-3753-a05b-29b6e136eea3 | -6.90443 | -48.04554 | 2026-07-07 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0db7c78-dbd6-30c8-9d2b-2493e1427db9 | -4.34361 | -47.76669 | 2026-07-07 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 687fb93e-46a6-3c7f-ab96-0c3ba81933fe | -5.7974 | -43.80352 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bae6f7f-df07-3a2b-a216-1c4a9c9cad3d | -4.28957 | -48.35236 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 793d1df0-a27d-33c5-a623-0bbdf69c5839 | -4.86857 | -48.91481 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 035cbe04-a0d2-30c8-af86-33d59a9b1e96 | -4.71162 | -47.9789 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f1ffc40-bacf-3caa-9bec-8027e6d9d2fa | -4.8667 | -48.91616 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d24c70ed-6007-3728-91ca-ec5a024ee448 | -6.20402 | -42.51759 | 2026-07-07 04:23:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db868b0f-fd92-3004-8206-4f6c18770a30 | -6.43094 | -55.8059 | 2026-07-07 04:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04966e56-7eb6-3208-8755-d68178025aed | -5.79796 | -43.80002 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62f5c81d-a663-3220-984a-d23e70636862 | -7.00823 | -42.78001 | 2026-07-07 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c822f9d-45e7-3ef2-a52b-fa681a854cc6 | -6.91521 | -43.71001 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a3f9d3a6-d92e-3479-aa7f-cde183fa1e19 | -9.36239 | -40.42585 | 2026-07-07 04:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f561107d-9882-3de5-98e1-80c7432fa671 | -4.34418 | -47.76323 | 2026-07-07 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de8df499-f5a0-3a91-9801-07402afdb7b0 | -5.97821 | -43.62126 | 2026-07-07 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aab0245-62a9-35bb-9a32-4a25fbea970d | -4.77118 | -41.79641 | 2026-07-07 04:23:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8be64cec-1b06-3b28-a7b4-1bb222eddfc5 | -8.071 | -46.69072 | 2026-07-07 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 594a503a-6a5b-3d81-b032-e476e0da137d | -6.49772 | -42.23479 | 2026-07-07 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| ae1159e3-ede6-37d3-a01e-a09109a1a9a1 | -8.34003 | -46.4865 | 2026-07-07 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36582ad9-daad-38d8-931a-8d59eef15f80 | -6.90524 | -43.70842 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18e4da9c-d600-39a6-adc9-997ea3cd664c | -4.38228 | -43.35757 | 2026-07-07 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 519e6a94-3c59-3464-b9f2-9fa3973becff | -5.75087 | -43.26577 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e693c6f-b09d-36a6-8313-cce40549663d | -8.02661 | -47.09027 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d722e79a-de5e-3157-aec0-9b1794d288c1 | -4.57468 | -48.03051 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36fcbc60-40de-3356-94b5-34cd4c951674 | -5.80073 | -43.80405 | 2026-07-07 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f473902-d37a-34cf-aec4-5a6b441f7c5b | -6.93293 | -43.7057 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 511c78eb-703f-3dc6-89a7-084aa9923614 | -6.92629 | -43.70465 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a3763361-b8bb-3c80-b957-fb675fecde0a | -6.11836 | -47.64194 | 2026-07-07 04:23:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00c39788-9910-3eba-9104-9f0b4d152399 | -9.28321 | -40.46094 | 2026-07-07 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd445095-5613-333f-9370-67b262ff310c | -8.07528 | -46.68717 | 2026-07-07 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9da10953-701c-32d6-954c-a130e84b156a | -5.36732 | -46.71358 | 2026-07-07 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7717408-3428-3dab-802c-3e584893b5ed | -2.79724 | -48.57857 | 2026-07-07 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecdd209e-45c6-3445-b96d-d1bb7bf385f5 | -5.62381 | -47.10051 | 2026-07-07 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
