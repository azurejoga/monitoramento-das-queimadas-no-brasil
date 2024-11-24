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
| 911a9a93-968c-3e35-8b37-00bf93dcd4db | -2.6709 | -46.148102 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1b40b96-8159-35ab-a746-ae73b6af33aa | -0.8131 | -51.604401 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd7cc55c-4553-3f94-a17c-723c12f55f37 | -1.9631 | -49.5284 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 850b6be8-766f-389b-97b7-248eb065322c | -2.0123 | -51.167999 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f092a434-1f75-3d1d-807c-39ce7a933b78 | -4.2276 | -44.627201 | 2024-11-24 00:25:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64077ede-5264-3c70-a70c-327cc9a40935 | -2.586 | -46.5439 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e2d2eb-47ef-3e8f-898b-e5d52ac618c7 | -1.7334 | -52.035198 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b49ba8-7a03-3f3b-a64e-f69b022908a9 | -5.0992 | -43.150398 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 567a5a47-1e2d-3660-bf11-e8004a8f4e19 | -5.6614 | -47.331001 | 2024-11-24 00:25:00 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ec5f465-2f71-3c8f-ba2f-3c68a6895f84 | -3.3101 | -50.021301 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d8bd1d-ad06-3a1f-b510-beaeb81c56dd | -4.1884 | -45.619701 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47b489ec-5111-3292-b0f4-625b38b0ced8 | -3.9166 | -48.091999 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb4488d3-920f-36a7-bd53-a96fdbaff68b | -1.266 | -47.8564 | 2024-11-24 00:25:00 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a86d4d88-a56a-34b8-bb4e-01c05d766100 | -2.6437 | -46.571201 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb1a5521-8577-3933-b567-7d5ce6ad91b5 | -1.0653 | -53.183399 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd76a5a0-35fb-330f-bccf-5d0acd779247 | -1.7402 | -54.499298 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f3c306-4070-3bc6-9b3f-d7c7e5fc0e64 | -3.1314 | -45.3689 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 651c89da-0995-321f-8687-6105da24c935 | -2.6419 | -46.563499 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97d6a7cc-0268-373e-a4d4-835ace2c8f13 | -5.9458 | -48.042099 | 2024-11-24 00:25:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f6a4642-7b0c-3e7b-81c1-8df67e9aa5d0 | -0.9124 | -51.725399 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0040e3a3-24c0-3082-a342-e762d17363f5 | -3.9072 | -50.573799 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 999c50ff-822a-3918-97ce-56d2af99b10e | -3.7047 | -51.7901 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ec8118-11af-3c8b-aaeb-bc7763cca30e | -3.9541 | -45.991402 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe8c2a3-4ce2-30da-8d5f-15cf1ad0d6e3 | -5.1926 | -49.138302 | 2024-11-24 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d198605b-20eb-3dac-aaa4-33b7bcbb3dfa | -3.8068 | -51.324299 | 2024-11-24 00:25:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7bfc73-edcb-397c-b433-8f426f885786 | -0.1871 | -51.477402 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0caad117-6590-3c5d-87cb-c9ced1870de4 | -2.9237 | -45.361698 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| faddd9aa-9cc7-3bcc-a87f-d89a61b339fb | -2.4019 | -49.0522 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05d8af5d-b332-3969-9655-564777101e73 | -2.7108 | -46.097401 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08a15f3e-feb2-35eb-9b13-651cd10290a0 | -0.8114 | -51.596802 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36469771-9a4e-3cdd-94b9-a1c53d18f8c0 | -1.5051 | -52.026901 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77f0b9ee-f76d-346f-bd4c-7d4f55abbe2a | -0.9426 | -51.631199 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12daa70a-3672-38b9-8d52-7016745d95dc | -1.5023 | -54.169701 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceed0e88-9e7d-3b45-bf93-02edf01dadd6 | -1.2067 | -51.9356 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d433155d-4b21-349b-a0e9-0f151b4d8c3d | -1.7253 | -53.238899 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591d06d4-dd87-3000-af32-c89b118fb6e6 | -1.2247 | -53.664398 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2226340-35bc-3ac7-9647-120fc32bd728 | -1.4264 | -53.372299 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f77759-e5ea-3baf-bafd-7223f8363c42 | -1.6164 | -52.569099 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 259245db-04f7-3049-8ef7-d77dc8684d35 | -5.0659 | -42.571098 | 2024-11-24 00:25:00 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61bd7f3b-ff89-3f44-a3f5-70cf817ec6f0 | -4.3786 | -49.734299 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58dde2d6-f5c7-33c5-97db-9ffb09d4bdd1 | -4.3094 | -43.206699 | 2024-11-24 00:25:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ec91109-ec00-3658-bdc5-aedb1f120839 | -1.6015 | -54.9342 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7353b071-f61f-325d-898f-fb2d843e2a90 | -0.3954 | -51.5788 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e52532ec-22a3-322e-84e8-024814ce21d3 | -0.9695 | -51.7047 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 73f5603b-357d-3cf7-b981-ebbd1f4f3981 | -3.4262 | -49.9883 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4d2b1e-e27b-3867-bbf4-0315bd60c5ea | -2.1958 | -49.097801 | 2024-11-24 00:25:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf1de5a-9acc-3f83-b860-7d138691e057 | -3.8618 | -50.047699 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66831778-02ca-32b6-aba5-a924893b08b3 | -1.4454 | -52.448601 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c87769ef-30b3-3fb6-bb3a-47b1151b13a2 | -2.7126 | -46.105301 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d37adf2-ac7c-3a15-a387-c957c93f5ed7 | -0.8796 | -51.716599 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 957f61c1-502b-3130-9a9c-7ef9a70df191 | -1.6034 | -54.392101 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 786edd18-a8fa-3e74-8be7-6816bd00858d | -3.8094 | -51.983898 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9308c3-7edb-3f3a-88ef-6be779c16c2d | -2.5722 | -51.8764 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| febb71c3-9734-3ab4-adba-757ae70e05a3 | -3.1681 | -49.068298 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbc04313-0aaa-3c67-99b4-b5bd4c00e168 | -4.6975 | -47.1716 | 2024-11-24 00:25:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9191a183-3168-3cc3-9dac-b566d807f7b9 | -4.1805 | -45.630001 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6bce1d0-46c3-3cd9-8550-ea8c1a233ebf | -3.8347 | -46.010201 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8528226-4148-3b7a-a3fe-d8dafb66fa3b | -2.912 | -45.355301 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff8f9282-c220-31bc-8027-fc095ec14838 | -5.2813 | -48.111401 | 2024-11-24 00:25:00 | METOP-B | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2f1e97c-6e5b-3ba1-860c-576ebbf72874 | -1.4641 | -51.111 | 2024-11-24 00:25:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd6034c4-0eaf-333d-8323-ffea34d60ab4 | -0.333 | -51.5303 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f91b8699-c0b8-36ba-8ae9-ebf85bcd4e61 | -1.3597 | -53.8083 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e05d38a8-b74e-37d8-8e21-b5bcc608981d | -3.4424 | -50.014301 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d100495d-bc25-3f1a-bff0-0110683042a7 | -0.0386 | -51.595299 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 84489539-5109-3e84-be57-2386d0562cd1 | -3.5688 | -45.614101 | 2024-11-24 00:25:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22c013f8-fb01-3893-ab11-752b8f646ef6 | -4.2402 | -48.658699 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e763521a-1fa4-31bc-a70c-349350bcd9d5 | -1.2745 | -52.237202 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf6e0eb3-2fcf-3311-a85d-ec54d2093cb6 | -4.6991 | -47.178699 | 2024-11-24 00:25:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae883b4f-11a0-3fd9-bec9-3b9120850c1f | -4.4021 | -49.655602 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c55bd056-aa54-34c5-864c-83a348548d6a | -1.6221 | -52.594501 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c98caef3-52b2-3014-a06e-0ee6179f6899 | -2.5221 | -45.407001 | 2024-11-24 00:25:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eea2a768-25f7-39c6-ba1f-a46ef099c71e | -4.083 | -46.827 | 2024-11-24 00:25:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b7b74c55-0a95-3e18-987e-1330022a0ac8 | -3.2328 | -45.541801 | 2024-11-24 00:25:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3989f50-5185-3f82-98e5-a03afff90501 | -3.7723 | -44.039101 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd4fd6bb-f5a3-32e5-a628-5cd77dd1ebe8 | -3.6848 | -50.638 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c40f457-cfe1-3048-a064-5ad453a8dc1b | -4.624 | -46.035999 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5a74e60-8473-3038-9849-086adacb5bfc | -2.5295 | -46.386299 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cffbfa02-bff4-3965-980d-a5965e4ebf01 | -2.5531 | -46.535099 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13bb2e7f-2f3a-3044-a1ac-9e4f66901d65 | -4.3718 | -49.7505 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb17f9d9-7620-380f-8feb-571053ee40df | -2.0714 | -49.597698 | 2024-11-24 00:25:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6b327b9-66a9-3e56-b072-c9bf633b4ba4 | -4.642 | -48.841999 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 535b5182-0ab9-3a73-badf-c35a70b900c3 | -3.272 | -48.751999 | 2024-11-24 00:25:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f29d0fc-361f-3b8f-8712-36e013cf81d4 | -2.574 | -51.884399 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f687f1f-e90b-3d27-b364-16205d926554 | -3.6418 | -50.215302 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb83be5-e424-3bee-b9f2-448ed188e015 | -2.5779 | -46.553699 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98ba8896-2bb6-3b4d-81c4-a649e77eeaee | -4.1901 | -42.9604 | 2024-11-24 00:25:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0449b8b1-cbf4-3c02-b706-fcc4c1564456 | -2.5058 | -46.101501 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a79f0018-90e3-34a4-bd8a-6bb7ddae88d9 | -3.3865 | -50.316399 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e152792c-4cf6-35ca-85e8-59039deeb8d6 | -2.8294 | -54.001499 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbfffd4e-57ae-360d-bdc0-3adb23d622a5 | -3.12 | -53.090698 | 2024-11-24 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a171870c-7539-382f-8ced-fa04f1923b7a | -3.8525 | -45.997898 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6ecfd1d-0f94-3dfd-8c4d-bd9be9b0accd | -3.1799 | -54.7528 | 2024-11-24 00:25:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8838405d-bd64-39bc-b471-3b1b30c97e2e | -0.8156 | -51.478298 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f9467f-6e22-39e3-b2be-01975a1c77a5 | -2.6979 | -46.266499 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14ee67ac-d932-3b30-aeff-8685301fd432 | -4.346 | -48.671101 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a964f7-3d78-3011-80fd-cdacdd26420a | -1.7002 | -48.7285 | 2024-11-24 00:25:00 | METOP-B | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322b0968-e028-3004-af4c-71508c6787a5 | -2.6881 | -46.2687 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa6093d-81bc-3f18-8c78-dadd1d591919 | -2.5704 | -51.868401 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5520d99a-5df7-3fcd-bcff-340419fa5f8b | -3.8602 | -50.0406 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5668864e-d305-3e06-906e-afcbe7f63d3f | -2.2619 | -50.444698 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
