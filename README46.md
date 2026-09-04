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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9bdbfa0-3abc-33ec-b587-a993a4e75d5a | -13.4137 | -57.0426 | 2026-09-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f9c4d5c9-fca2-30bc-86c1-5f549310db60 | -13.9477 | -54.3971 | 2026-09-04 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9a0e69d2-d248-3055-8a88-feb02fae96ba | -20.8573 | -57.7072 | 2026-09-04 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| c2689e4c-6930-33f8-b898-698a03832d8e | -3.234 | -50.5789 | 2026-09-04 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 94cc00d4-bcb7-3642-ab4e-376cbdd97009 | -15.3852 | -53.7652 | 2026-09-04 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f75c3123-7844-3753-b0e8-05858e8597d6 | -15.4994 | -53.8973 | 2026-09-04 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| dab58b19-0ded-32ea-ac24-3f46907c074f | -13.9477 | -54.3971 | 2026-09-04 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a1482a47-6081-364c-87f8-ce43ace61194 | -3.3688 | -59.4079 | 2026-09-04 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ce586ca6-97d0-3c82-bad9-2fc3a4a16759 | -1.4761 | -54.2565 | 2026-09-04 15:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8b6d05b6-7274-36e1-a6c4-0269e5d8513e | -15.5188 | -53.8948 | 2026-09-04 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 67a8fc3b-5a11-3b21-97f2-5ffb3e58c060 | -12.1363 | -54.3202 | 2026-09-04 15:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4c0a7ae8-58de-3b7f-9568-ed4fe5676b08 | -6.5224 | -59.9499 | 2026-09-04 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| d20a63b1-28ea-31e6-b838-c167221555cd | -14.1361 | -58.8776 | 2026-09-04 15:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a7c2f314-4bf3-3e0c-becf-ade1cb09b4c9 | -3.3504 | -59.4465 | 2026-09-04 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7791171f-73ad-33e5-bdd3-ecaca946ecd9 | -3.6033 | -60.5664 | 2026-09-04 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c5d92910-d789-3e87-96c6-dca5660566fc | -3.3871 | -59.3883 | 2026-09-04 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c25a10f7-d561-32a2-8456-0b8557b2503d | -3.3872 | -59.3692 | 2026-09-04 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f8dff14b-8c32-3aa1-83d3-d90780d14b82 | -9.6939 | -65.1145 | 2026-09-04 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 57442837-a74b-3d77-b69e-a56e7387d0ed | -3.3685 | -59.5036 | 2026-09-04 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 901fc540-40e9-380b-803e-159520382671 | -13.967 | -54.395 | 2026-09-04 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 561bebbe-1a84-3fdd-b699-581880ed76f1 | -3.7645 | -61.7548 | 2026-09-04 15:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 163.9 |
| c852ba1c-b66d-3b0d-9669-15acd6639517 | -4.4855 | -55.0848 | 2026-09-04 15:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b9169691-1f60-328b-840a-b77a6aee337d | -11.2877 | -54.0522 | 2026-09-04 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9007bbf7-1978-3234-b082-27c473fea02c | -3.3688 | -59.3887 | 2026-09-04 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 02eae1ec-54f0-38a9-85e8-190fcfce73e3 | -3.5162 | -59.0405 | 2026-09-04 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 942f8e72-af25-329d-9931-1f55e22f5da4 | -20.8573 | -57.7072 | 2026-09-04 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| f664f8c5-ffcd-3082-ad8f-0a66edc5875e | -20.8776 | -57.7043 | 2026-09-04 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 2ab2fbdf-a6ef-32a8-a51f-09d39f8e8cb8 | -6.5225 | -59.9307 | 2026-09-04 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 0dea2cb2-32b3-3a74-bd23-a50c3b4ba430 | -3.1462 | -60.6317 | 2026-09-04 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e4f680ff-241e-3f0b-8241-3bba75b80c6d | -3.332 | -59.466 | 2026-09-04 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 78244bdd-be95-38ee-bbad-73651e51ee67 | -2.9886 | -57.9132 | 2026-09-04 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4fb66276-a31e-3ec0-b8a0-a551147a29ae | -3.4082 | -58.446 | 2026-09-04 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 3449aed2-acdf-3427-929a-91df5a083684 | -15.4994 | -53.8973 | 2026-09-04 16:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3e137290-1c9f-3b47-b532-914745126987 | -9.0981 | -65.5091 | 2026-09-04 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 23414604-8148-3cb3-b5f6-7d8765e8cfa4 | -3.7828 | -61.7545 | 2026-09-04 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c1189176-4d69-3a7a-b878-77666f04cfd3 | -3.218 | -61.1607 | 2026-09-04 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3aa2cfcf-a384-390b-8104-9c1212c67233 | -3.9363 | -59.3381 | 2026-09-04 16:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| fc199afa-368f-320e-8020-941199736f73 | -3.5346 | -59.0209 | 2026-09-04 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 4598733f-da3f-3bad-ba7a-0a671e2bddcd | -3.3688 | -59.4079 | 2026-09-04 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 4587111a-36ab-309f-b35d-a5617834b2f3 | -3.7462 | -61.7552 | 2026-09-04 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 4761b86f-3fcc-326a-949f-f9effbee1631 | -12.1363 | -54.3202 | 2026-09-04 16:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 6c371adb-79b1-39a6-9e00-1c4d9764fa97 | -6.5224 | -59.9499 | 2026-09-04 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| cfd3db1c-ba8d-3356-a2db-120c7fe3c891 | -19.1755 | -57.312 | 2026-09-04 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| a0a3796f-35bc-3a88-af95-f4922baca993 | -9.6939 | -65.1145 | 2026-09-04 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1131d70e-d2fa-3a1d-a5b5-98f09057fefd | -3.2181 | -61.1418 | 2026-09-04 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 06a14996-4412-3975-a563-1c976cecfb46 | -3.0347 | -61.4657 | 2026-09-04 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b5ad4f19-7ccc-3250-8ae7-83976935e58c | -3.3871 | -59.3883 | 2026-09-04 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 11bca338-3a5a-3993-a533-e127d31561d2 | -3.6033 | -60.5664 | 2026-09-04 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6f411d2f-d809-3bec-acf1-a0c819865800 | -3.4003 | -61.3087 | 2026-09-04 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ba56c2ac-3413-3c7e-8944-db9898ad8b1a | -3.7645 | -61.7548 | 2026-09-04 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 18168642-05e1-329c-8504-b0b6db3c140a | -3.3872 | -59.3692 | 2026-09-04 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8ec29976-87f4-3f5b-a042-98c96cf30aea | -11.2877 | -54.0522 | 2026-09-04 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5b0ab082-922d-37b5-b772-34f14c7b4611 | -13.4386 | -51.3921 | 2026-09-04 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 276b509e-b02a-33ee-a5d1-9eccf44fece0 | -3.0347 | -61.4846 | 2026-09-04 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 96426ee2-e01e-365e-94c5-7371b12e37a6 | -3.1462 | -60.6317 | 2026-09-04 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 945fbd01-65ac-3025-8510-8a1202151fd5 | -8.5363 | -67.1617 | 2026-09-04 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b75fd9f8-8b7e-3b7e-8e78-4f255731a8ca | -13.3946 | -57.0444 | 2026-09-04 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ccd85c64-0066-33bb-b5a8-2d03454ffa21 | -13.9477 | -54.3971 | 2026-09-04 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d4656daa-a248-359c-a113-7ac25c31941c | -17.0875 | -56.874 | 2026-09-04 16:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| eba2567d-0294-3583-ba48-0783a6ad33d9 | -3.0616 | -57.9893 | 2026-09-04 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 74ac1004-735c-3485-8b61-d0331edbe590 | -0.4872 | -51.8094 | 2026-09-04 16:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d99cad47-bf9a-3e08-9cca-c95998e3ed6e | -3.0616 | -58.0086 | 2026-09-04 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ef9b5725-e31e-3116-bfe4-6c90b265752f | -3.5347 | -58.9824 | 2026-09-04 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b778f114-06a0-3a7f-95fa-15a90c7e159d | -13.0897 | -45.163 | 2026-09-04 16:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 66dca1f4-c332-3454-81a3-7fe3775fd0bd | -3.0347 | -61.4846 | 2026-09-04 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0c7f9a2c-3e26-3e04-8a08-e62f605b540f | -20.8573 | -57.7072 | 2026-09-04 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| eb9dfcdf-aa77-3013-8b9e-2ada5477456c | -17.0881 | -56.8328 | 2026-09-04 16:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 717.7 |
| 6aa6011e-406e-3abc-8515-208374a02456 | -3.1633 | -61.1238 | 2026-09-04 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a06dfef4-279d-372c-b689-d88d8c2da15d | -14.5025 | -52.2126 | 2026-09-04 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 237af678-7a60-30de-9b01-981cf526e897 | -3.1462 | -60.6506 | 2026-09-04 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 43020906-da70-3813-a3f8-9de3199a56cb | -17.0878 | -56.8534 | 2026-09-04 16:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 229.7 |
| 4e5530e9-fcd8-3280-9e48-85243abbc4f6 | -3.7828 | -61.7545 | 2026-09-04 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5c965ac6-4e8e-30bc-a3e8-5ba2b79cd8e5 | -12.3798 | -53.1793 | 2026-09-04 16:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 80516c0c-70d0-3053-8b1e-f72d394dd8f3 | -6.9657 | -59.7791 | 2026-09-04 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 256a27da-8d31-3b36-bcff-42a252e1bd1a | -3.3872 | -59.3692 | 2026-09-04 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 78a182a7-2de7-362b-a399-ba68ebad7d58 | -12.8848 | -58.2885 | 2026-09-04 16:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 7635c596-9cdc-3a70-83b0-d0c04b482ce7 | -17.1074 | -56.851 | 2026-09-04 16:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.3 |
| 670eae81-56b4-31ec-8ab7-63aa0a8dd089 | -3.9363 | -59.3381 | 2026-09-04 16:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 8ca4d6ad-5008-3e52-8fa2-5c681e8f9121 | -20.8776 | -57.7043 | 2026-09-04 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 9bd9866e-7d30-3759-8493-3e00203d71c5 | -8.631 | -66.5473 | 2026-09-04 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4e133fa7-b1b0-3d1b-95c1-f67aaed38e50 | -9.0983 | -65.4717 | 2026-09-04 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb0a0ef6-039a-322b-a7f1-a9b48578f65f | -20.7951 | -57.7788 | 2026-09-04 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 8701ca3c-253d-3767-abbc-cfbc2f6b86d1 | -3.3871 | -59.3883 | 2026-09-04 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0cae4ffa-0490-34b9-98b3-4de594acc7bd | -3.4081 | -58.4653 | 2026-09-04 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 3770b7b7-e706-3f99-a6cf-b959fd26261b | -3.4003 | -61.3087 | 2026-09-04 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fd2f72a8-39e4-3b2e-90f4-24208561fc71 | -3.4264 | -58.4649 | 2026-09-04 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 754bed58-0ece-3a0e-bf26-d26d55c8de4a | -3.6033 | -60.5664 | 2026-09-04 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| bed4614d-5e1f-34d1-bee0-9f6ccdc916e7 | -3.1462 | -60.6317 | 2026-09-04 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 288c5979-4988-35c7-86f7-92860386f6dc | -6.7648 | -59.4408 | 2026-09-04 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 1c8f5ca9-8ce4-3856-a181-193f67070bca | -19.1 | -57.33 | 2026-09-04 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c18d8bc9-23a5-39cf-8a84-7c8c7ac5ad6b | -8.6849 | -66.9355 | 2026-09-04 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9e2ec324-6a81-393c-9a3a-90fba1277222 | -3.1462 | -60.6506 | 2026-09-04 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 78ef4015-3223-37fd-96c7-af08c0dfa287 | -3.7462 | -61.7552 | 2026-09-04 16:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 3ec58554-c14f-36af-bcd4-d38bb55d731b | -3.2181 | -61.1418 | 2026-09-04 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c696da7a-400d-3042-99db-185464e7cf62 | -3.1998 | -61.161 | 2026-09-04 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 46ad122f-ddda-33e7-901d-c0a907998340 | -3.1449 | -61.1808 | 2026-09-04 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d801007d-ccbe-34f2-be0d-662e1244b0b4 | -3.9363 | -59.3381 | 2026-09-04 16:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| f083fea5-38f1-37e0-a37e-ce43c074cf21 | -3.218 | -61.1607 | 2026-09-04 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a0c11732-3c4b-39ec-b4d0-f38ef510660e | -15.4994 | -53.8973 | 2026-09-04 16:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b5e0f1f3-c2fa-3b08-b0b7-6ce1c2fe605b | -3.1633 | -61.1238 | 2026-09-04 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |


[Clique aqui para ver as próximas entradas](README47.md)
