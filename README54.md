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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1383fdd-9ff7-35b6-becc-a664c00852a2 | -3.19068 | -54.51043 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 937073d4-0d78-3d4b-83ae-2507262730b8 | -4.02627 | -48.89136 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e88ed117-1b77-3a14-aac2-bfb9857e96d0 | -3.69705 | -51.80111 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6920573a-ac86-38e3-8708-d5b95c952e13 | -3.83947 | -52.18131 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c2cb871-1c5b-3ff6-aa7f-e41fc991a7dd | -0.82304 | -51.60038 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bb2065d-c8ff-3c9f-a457-938661b2328d | -3.69254 | -51.80775 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d762fd2d-674f-34e7-a11a-1f081974c23f | -3.35521 | -49.56531 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 552b195e-191e-35ab-939a-939d7e311181 | -4.0044 | -49.95452 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59677aa8-b8b4-3865-8a4f-905216fe1e69 | -3.90892 | -42.41575 | 2024-12-01 04:44:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0185319d-0db2-331c-9c58-c29f1540f4c8 | -2.07098 | -55.00652 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ca87a0b-cc18-3420-a775-c41746042285 | -3.26861 | -50.0949 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07733202-9c37-34ac-b865-fc9e2ffd7c04 | -3.78676 | -52.11647 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c671e08-90b9-3b4c-bf3e-9db3b16a6218 | -2.96707 | -53.45118 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67e505b9-69fc-3b53-b758-e71cc0453401 | -1.32533 | -51.74181 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a697c9e8-14f4-3db1-9914-0efaf4759af8 | -3.91222 | -52.34011 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48204878-f60a-349b-8066-b5488a69f30f | -1.76715 | -50.86418 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 922f1892-62b6-351c-92df-e1854a4f1ade | -3.24343 | -45.37641 | 2024-12-01 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafdaa3f-f385-32e6-b97a-ed387dc7dcf9 | -3.68802 | -51.8144 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f92dc471-dffc-36c1-8e29-7976b9f76508 | -3.18009 | -54.33493 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 606be04b-9d31-33b4-8419-b2b1d6c19f60 | -1.17079 | -53.4128 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b32598b7-93b2-3138-9516-f5c363311fcd | -2.51573 | -51.82978 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a68c174-5e36-3335-8058-94942af3a65b | -2.36092 | -50.42253 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d20ce0a2-41fc-383a-9ed8-05a60630dfe2 | -3.82703 | -46.59769 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f4b408-9752-38d5-9dc0-98f0ec184807 | -3.10408 | -53.27156 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbe4f969-03c8-3ca1-9730-ef5088a05e2f | -3.95735 | -49.75861 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2e73b5b-163b-32e7-bdfe-f8c3180d628f | -4.11633 | -48.53286 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2525a763-dd2e-3664-8663-489715f292bb | -2.23844 | -50.78716 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89fb4929-4ba4-37eb-afcc-156347dc1460 | -2.97724 | -53.89894 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dd1c9b5-9146-3f8b-a6d8-e14a15047b89 | -1.03179 | -53.55313 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9f265a8-1a95-33dc-a638-21358a4e57cd | -2.58772 | -53.98945 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e717507b-bb29-3a0a-b1a3-e5196d99d9ff | -3.26239 | -50.04797 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3e2bf47-d3b0-36bf-8e0b-8da5bcd11a7e | -3.02245 | -52.35677 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 527fe4fc-77b5-3004-a27f-9ca9cd9562a1 | -3.37053 | -51.12531 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e098ec5d-9e07-34e0-a91b-a541b823a628 | -3.1242 | -53.09929 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d13a3e2-4f48-3cec-b374-a2fc031ec5c3 | -6.31608 | -43.46226 | 2024-12-01 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3e98481-f031-3faf-a035-aade14e9198c | -3.29609 | -53.67586 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1796a761-3485-310e-aea9-a15252d9bcc8 | -4.00457 | -44.76044 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 91d68812-6b06-31b7-8e48-29b526c20235 | -1.66789 | -53.77917 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efdfb545-b719-3f4f-b7ea-d9507c8736aa | -5.50399 | -42.87334 | 2024-12-01 04:44:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 28df75bd-d033-347f-a423-682f35043e00 | -3.09425 | -53.28686 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b0b652-b281-3bf1-8416-c94532ae79a8 | -2.36696 | -50.40578 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1adfe1fd-4dcc-34a9-87ff-3c27031e946e | -3.18925 | -54.32684 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2146b5-d05e-333d-b628-8396bef7ad7e | -3.21579 | -53.13321 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 230dfc6e-dace-3003-8b32-6a3cf4cba7b0 | -6.29398 | -43.84917 | 2024-12-01 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81aed42a-6069-3077-8aed-a1997bd6ada4 | -3.02378 | -54.01623 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec70b17-3282-3423-8535-b47ca133cbf4 | -3.38392 | -50.11645 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27613e5b-6963-3727-9582-03faf9c82132 | -2.69563 | -52.91203 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0ed4db7-dc04-30fe-bdfc-0dd7755789dd | -2.68565 | -51.72922 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1e3c18d-d066-3f2a-9100-ff216d3cc221 | -3.12641 | -51.79038 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fd13c67-44d4-3a02-b92a-695c4e29ac50 | -4.72156 | -45.68577 | 2024-12-01 04:44:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96cfaf3c-cd82-3166-a497-33aafa34bbf4 | -2.47773 | -50.37005 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c80a1542-7a84-32da-a6e9-4a848abb8078 | -2.8077 | -54.03862 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7a0d36c-89a7-3718-b4c0-201ff574d6a3 | -3.63716 | -51.45201 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83141f76-a852-31a6-b154-469f4450fcf9 | -3.54626 | -50.41791 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15dd1598-fdec-369d-95a5-ba44af79980e | -2.64106 | -49.91149 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5ea1a25-fa38-3a16-81c6-f11a0a136a79 | -2.97351 | -53.89837 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 398c11ef-17f1-3c94-8b1f-1182d89b2879 | -2.97789 | -53.29031 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fef36b19-8bde-35a3-a968-a2900a690f6c | -2.80784 | -49.77883 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e7f7619-f285-3188-9b65-2669528fecf6 | -3.99101 | -47.91495 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08025e67-dbd6-3b32-a7bc-d6baab67c262 | -3.91126 | -53.31507 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e35f635-f6c9-38b5-80c1-9aacae1ba2c3 | -3.39166 | -53.27105 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59bc600e-4e9c-3abe-a619-bc4bd51fc9ed | -2.40067 | -50.38628 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21e2254a-467a-33a1-a950-da76f733bb08 | -3.26506 | -50.20391 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 891d250e-9286-3a81-acd4-efb474ca197a | -1.62022 | -53.88511 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2687ede0-dc54-33e4-8935-34844b5b66be | -3.26735 | -50.57549 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b3f76e4-5f40-3176-b7b8-263ece4ebf7e | -3.35515 | -49.76122 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e50f7af4-5784-36d5-964c-2370af75079e | -2.63561 | -46.88416 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f28f38f-b774-3954-afa4-89932e0f62e2 | -1.66863 | -53.77459 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 90b14e9d-34cc-38da-8dce-7cf53bede1e0 | -3.85485 | -46.54215 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70e4acbe-b2f6-37b8-9c5f-dc4a93819fb8 | -3.40513 | -53.02958 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e18547aa-4533-3c13-a39e-4ed1b8b6ed7a | 0.07309 | -51.48748 | 2024-12-01 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1d99667-2b61-3fa3-b43c-e14aba72ec02 | -1.48525 | -52.68017 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0139c21a-f5b7-33b4-87b5-3148ffff2c01 | -3.7663 | -54.44125 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74a82f26-9a1a-3a21-b862-feb7e739d820 | -3.41481 | -50.32611 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e96fb95-8e20-3933-9699-fba2458418b1 | -3.51794 | -49.84318 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e50724a9-1331-36d7-89e4-a2175aeb13a2 | -2.95581 | -51.69747 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e5520fb-1c07-350f-97c7-3a62d3dfc127 | -3.24876 | -53.91814 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e12556e-e096-3214-97e6-f2cdfa249440 | -3.33642 | -53.31011 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac940304-8091-3e53-949f-234085847985 | -5.5781 | -43.61014 | 2024-12-01 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b580e7ad-479b-3e7c-be93-3a5db638260d | -3.94737 | -49.95278 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ff6706-b87d-30ba-be0c-f0ef793181f2 | -2.80923 | -45.94143 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c06d573-a609-3956-874c-88c1820d91be | -3.71627 | -51.07226 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a83cf9cc-875c-3eb9-9692-db417bc4798e | -3.06252 | -50.3308 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd66a5ff-cdda-371c-825a-c948e0fb6064 | -2.00419 | -51.17931 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1da5621-cd1c-3e17-a390-64b39913f4a7 | -3.17977 | -53.63902 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0173514e-4733-324c-8887-1f1351b3d41d | -2.8455 | -49.88006 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebb3a003-d87c-3229-8ce4-c39dd0f6f875 | -2.06641 | -50.72126 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dd832f8-bbf1-39bf-a871-5ac19caf4e79 | -1.06039 | -51.75864 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aaa1fdb2-736f-36c1-bc72-05cd8728f5ad | -2.30831 | -50.69111 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcc91e4e-7886-34f1-9bca-1a91f5cfd7b3 | -3.30495 | -50.03691 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 291c1eb4-7985-3137-9763-531bfaa95cdc | -1.29961 | -51.72639 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56794649-0dab-36e6-b0ae-9f1c1b292687 | -1.28296 | -51.74276 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d012c099-4bc9-35c6-ac45-4b9838867130 | -3.4327 | -54.11456 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c54a870c-c1ed-322c-b6b3-63d01e277068 | -1.43446 | -52.40509 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d97d61b-c6db-3e0e-ac5e-5b0a3db28cef | -1.27952 | -51.74223 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb8768e9-e36d-372c-873d-598c0eaa642e | -2.36751 | -50.40233 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fdf0c1b-cab9-3c31-819f-bff6feabce35 | -6.19118 | -44.42572 | 2024-12-01 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| daaa4fff-6fab-30ec-9f10-2cd92a6ba5a5 | -3.13525 | -54.52912 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 298b435a-925d-378f-9879-33f5c9d80226 | -2.67347 | -46.59638 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa7e319f-194d-376a-b1c5-91e21f324f83 | -4.19443 | -50.68575 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README55.md)
