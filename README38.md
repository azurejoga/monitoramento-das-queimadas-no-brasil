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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffd6812b-8977-3d59-94d3-54be042d6292 | -11.1609 | -46.9471 | 2025-08-18 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3af60db9-43d0-3160-b829-371db84d2078 | -10.5418 | -50.3615 | 2025-08-18 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 2732d0f6-54c8-36be-82af-398307275d66 | -6.5203 | -45.4787 | 2025-08-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 273.2 |
| eaa3c44c-2fb0-30f1-b0f8-da2daf5b38d3 | -3.9819 | -42.5396 | 2025-08-18 14:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 6847cedf-3cb8-3a9c-9ce8-4c317187bc01 | -3.982 | -42.516 | 2025-08-18 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 5b8e70df-2bb1-3ad8-b8a0-e18a86fd446d | -13.1746 | -54.9337 | 2025-08-18 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 218.3 |
| 718b3d22-ac1e-307b-aae3-5626e346269a | -9.3989 | -48.2994 | 2025-08-18 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3abccac4-6a35-32e1-bf40-d2c390e711f3 | -10.5415 | -50.3828 | 2025-08-18 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 300.7 |
| e8ebf15f-b368-32b0-96d7-32a2defaacd7 | -13.2375 | -50.7972 | 2025-08-18 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fbe996a7-14d3-3cdc-be06-753674326fca | -11.1425 | -46.9047 | 2025-08-18 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 6f818061-ac9d-3176-b340-fe9448e90622 | -13.1558 | -54.9151 | 2025-08-18 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 834d2134-2236-325e-8f37-e91528ef70c5 | -13.1555 | -54.9357 | 2025-08-18 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 225.6 |
| f25c7242-2701-3f6d-b8fd-c09c19737423 | -5.7949 | -45.0132 | 2025-08-18 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 68b642da-1312-356e-842a-d2d1ff44e80a | -8.7602 | -46.6655 | 2025-08-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4651267e-52f1-3ca9-9792-cd26e3d46f47 | -6.3609 | -44.5367 | 2025-08-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 311f6fc9-249d-3947-ad09-adb5bece2d6e | -6.5016 | -45.4802 | 2025-08-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 743be917-5fa5-353b-94c0-fd63bec81f2c | -12.6435 | -45.3269 | 2025-08-18 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 9da9da82-3912-3115-9f4a-20773c7b96da | -13.1994 | -50.7806 | 2025-08-18 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 01972662-bdf4-36dd-8a8b-c2f3f68f3bff | -12.9366 | -46.1076 | 2025-08-18 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ef0b0758-55bf-3176-ae44-5d0b8c685a7d | -6.9715 | -43.5833 | 2025-08-18 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 611.5 |
| 05e141f7-24ca-3ef4-96bd-19d853cdb938 | -13.1746 | -54.9337 | 2025-08-18 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 272.1 |
| 3c89961c-7359-3d8b-8213-9f5334798a59 | -13.1558 | -54.9151 | 2025-08-18 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 42277116-9be5-3c7c-ab10-84e1bae0ffd5 | -12.9968 | -56.8597 | 2025-08-18 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4cf266cd-554d-3f17-94ee-7afac4bef1cf | -12.4849 | -45.5817 | 2025-08-18 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5c067e1d-bab2-35d0-ae1b-9b1cd0b61b0d | -6.3609 | -44.5367 | 2025-08-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e0783c25-504b-3062-b6e1-1fb9d3239438 | -13.1555 | -54.9357 | 2025-08-18 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 193.4 |
| 8e05c7f4-0665-3c4e-a738-01d4b6a32b34 | -8.76 | -46.6878 | 2025-08-18 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 72875741-f429-3193-a213-5b143fccf9ce | -13.2375 | -50.7972 | 2025-08-18 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ee1bf152-70cb-3aa5-ad65-5ce0a7f8e995 | -8.7602 | -46.6655 | 2025-08-18 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5523cf67-022c-3a83-9f3b-e2caf2bf54b3 | -6.9712 | -43.6066 | 2025-08-18 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 408.0 |
| d57f995f-dcd3-3d2c-86ca-35141c11843d | -13.1998 | -50.7591 | 2025-08-18 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 077b2275-df55-38be-93ab-19c2e3f75920 | -6.5203 | -45.4787 | 2025-08-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 782599ab-ce00-3d57-98cb-1cf2c4534d82 | -12.9971 | -56.8395 | 2025-08-18 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c2b426c5-a3d3-3ab2-bc08-8db9d3992688 | -6.5016 | -45.4802 | 2025-08-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 146094f2-7e03-393e-a8d3-47f78b0c4123 | -12.6435 | -45.3269 | 2025-08-18 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 6949fbc0-c05f-3510-9173-2137afdb038c | -6.9715 | -43.5833 | 2025-08-18 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 597.1 |
| 33914ff3-86e1-3549-a4dc-52693bcfe649 | -12.8422 | -46.0079 | 2025-08-18 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1c42472a-fb9b-3b36-8f43-3613b382ce74 | -11.1609 | -46.9471 | 2025-08-18 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c2a4d7e4-464c-3335-b233-9a5f0ccd71be | -13.1994 | -50.7806 | 2025-08-18 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 3d1c209f-7327-3f0b-bc66-036560e45818 | -11.9104 | -43.4319 | 2025-08-18 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e541cdc0-0dd7-3f3a-aa5d-822b74da5c48 | -13.199 | -50.8021 | 2025-08-18 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 82322880-ea9a-3bbf-9552-46cde3cc9190 | -10.5415 | -50.3828 | 2025-08-18 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 53e7a35d-5fd0-3cab-a8b5-e43936ef2683 | -6.5016 | -45.4802 | 2025-08-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 98a56c75-a1a4-3e90-964a-d88466982ced | -12.6435 | -45.3269 | 2025-08-18 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c787d5f8-9816-3f6c-bdf9-cae5185059bf | -14.1707 | -45.3042 | 2025-08-18 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e0a57580-e6ef-3615-8fa3-72c35304606b | -6.9712 | -43.6066 | 2025-08-18 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 475.0 |
| e86a495a-06b3-3ee2-916b-10fa1641186c | -7.5742 | -45.1607 | 2025-08-18 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7035e7fc-fb68-3e0d-9244-975458777652 | -11.1425 | -46.9047 | 2025-08-18 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 1257d39c-b583-37e5-8d98-d43aa1d7725b | -13.1994 | -50.7806 | 2025-08-18 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| ab015fe6-7846-3bc2-b615-aea2de5e1456 | -13.1558 | -54.9151 | 2025-08-18 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 8c3da777-4da6-396b-bd5e-d05f15167a00 | -13.1746 | -54.9337 | 2025-08-18 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 227.3 |
| 9da8fb0b-a6f5-3fe4-b91a-5df66ab8cb00 | -10.5415 | -50.3828 | 2025-08-18 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 203.7 |
| dab25c92-2647-3a69-96ef-2d6629b0b028 | -11.9108 | -43.4081 | 2025-08-18 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| be9c6b05-69d0-3f2d-92b5-32d796e6d779 | -13.2183 | -50.7996 | 2025-08-18 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 904186c9-9ca8-369f-973e-51a1cee100c1 | -6.3609 | -44.5367 | 2025-08-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 6dc5ab84-f072-333b-8826-400532af660a | -13.2375 | -50.7972 | 2025-08-18 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 816e4ef1-42d8-37d9-8ac5-2d3180a7a628 | -8.76 | -46.6878 | 2025-08-18 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8430e3cf-32b4-38cb-a5b6-1d9eb2d585a6 | -3.982 | -42.516 | 2025-08-18 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| adabd560-eae8-397e-875d-84b76f13da1a | -13.199 | -50.8021 | 2025-08-18 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 578ecb95-fb16-3564-9a9a-4cfe1a008037 | -13.1555 | -54.9357 | 2025-08-18 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 208.6 |
| 49dbb3a8-4db9-3dbe-91ff-5fcc9a876c55 | -8.7602 | -46.6655 | 2025-08-18 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8fcee016-70da-38f5-9f9f-d1a8ac88f0bf | -6.9715 | -43.5833 | 2025-08-18 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 518.6 |
| 0e266663-f82f-385c-825a-e99070bff650 | -11.8512 | -51.5801 | 2025-08-18 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 1e2b006e-767e-3f0e-9dc5-26792502ffdb | -13.1558 | -54.9151 | 2025-08-18 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 24a65f1b-5e9f-3d69-8d66-745744c1fbe0 | -13.1555 | -54.9357 | 2025-08-18 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 480fee78-f4b7-3f79-9d7c-09ddbe09ecac | -12.9971 | -56.8395 | 2025-08-18 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bf7f568f-a19a-3d91-8d3c-c1fe148571e7 | -8.3857 | -44.9888 | 2025-08-18 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 067e5342-e272-30f5-8750-56b03010d96b | -15.8798 | -50.2009 | 2025-08-18 14:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 40409170-0848-3d75-acb2-90116df25e51 | -11.9108 | -43.4081 | 2025-08-18 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a9c47b78-3562-3bba-89a7-bd486b9ed283 | -6.5203 | -45.4787 | 2025-08-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 69de99b8-db88-32fb-bc26-8e301b9285c5 | -8.1875 | -47.3641 | 2025-08-18 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 206b0039-f17d-3590-bee4-d59e5218dbeb | -6.5016 | -45.4802 | 2025-08-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 52e94847-1a7b-3029-8c56-4e5d7212b9c1 | -14.1707 | -45.3042 | 2025-08-18 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a996d330-b16c-3c8d-9190-6d57a9132ca9 | -7.5711 | -45.4333 | 2025-08-18 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d0795baa-3f75-3963-9301-98d5eb95fc85 | -9.3989 | -48.2994 | 2025-08-18 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 731e657a-118e-3768-8b61-8aa5099222df | -8.7602 | -46.6655 | 2025-08-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c8ca46b9-5102-36fd-bfe6-ecaba9362829 | -3.982 | -42.516 | 2025-08-18 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 8c3c6151-f1f7-332d-9527-7c519ed9ed13 | -6.9715 | -43.5833 | 2025-08-18 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 425.2 |
| 319a04fc-e1a6-3d57-9dd7-de53f2a77fd3 | -6.9712 | -43.6066 | 2025-08-18 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 309.4 |
| 66bf2550-369a-3872-a4bd-2b8b86468e78 | -8.76 | -46.6878 | 2025-08-18 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 701ea470-c986-38b6-b1a1-b6967182ef54 | -9.38 | -48.3013 | 2025-08-18 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 5f3653e0-60ae-3723-a371-e2ea8ab6f3e7 | -13.1746 | -54.9337 | 2025-08-18 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 222.9 |
| 44833eab-6ffe-34fb-97c6-a7974444c009 | -12.9968 | -56.8597 | 2025-08-18 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2d5017d8-1b0b-3b35-a393-e3ee7b241cb6 | -13.1998 | -50.7591 | 2025-08-18 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 362084a7-1e08-3d9d-91d6-523a6172e1b0 | -7.5711 | -45.4333 | 2025-08-18 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 85caa994-d181-39cf-a08f-108f2acb9784 | -20.8724 | -54.9685 | 2025-08-18 14:40:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8c7c4147-61b2-3ba5-85a7-2951d1f63b34 | -11.1429 | -46.8822 | 2025-08-18 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1bf95bae-f6de-3f48-9bd5-73ea52852072 | -12.5289 | -48.4988 | 2025-08-18 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 93bf8575-e91f-3b0b-917c-d0365067c471 | -8.3349 | -47.6145 | 2025-08-18 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 69ead47c-5401-3a1c-8f04-01fa81137482 | -12.9968 | -56.8597 | 2025-08-18 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 6bd40760-853a-381e-ac0b-2c9db16255ee | -13.1994 | -50.7806 | 2025-08-18 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 7bd5c18a-ac2c-383d-9449-aa6214c8c084 | -12.9971 | -56.8395 | 2025-08-18 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7d1bcbb4-e883-3fe4-b0c3-22e5cd978b69 | -7.3773 | -44.2865 | 2025-08-18 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| d68e136d-ddcb-3427-8f18-438aa4753654 | -3.982 | -42.516 | 2025-08-18 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 07286b0d-f87a-3d6d-bdbe-422aede0fcb0 | -13.199 | -50.8021 | 2025-08-18 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 385d7ff9-85c7-3f3c-9a5c-b1c179c4c3ef | -13.5945 | -46.9819 | 2025-08-18 14:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0fae4c49-fcb9-3b94-90b7-dfd85f52a50d | -12.5481 | -48.4962 | 2025-08-18 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 2f7cae7b-2fe2-3a05-aada-4100679ca974 | -3.9819 | -42.5396 | 2025-08-18 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 2d3aac40-0565-3c51-ba9d-0f66522ec260 | -13.2183 | -50.7996 | 2025-08-18 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 644e1bc2-73ea-3964-80c8-6f91afb79c67 | -13.2375 | -50.7972 | 2025-08-18 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |


[Clique aqui para ver as próximas entradas](README39.md)
