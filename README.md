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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23559928-5ae9-3d75-92ee-2b63ed2fb3d7 | -21.29594 | -48.68475 | 2025-11-26 00:09:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 1dade5f5-7253-388e-934f-2732aa84db22 | -22.18005 | -46.957 | 2025-11-26 00:09:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1736a77f-41a3-3fd9-aa8f-d648cd3d83ea | -19.96749 | -45.16199 | 2025-11-26 00:09:00 | TERRA_M-M | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3d384475-404c-3d39-8729-2e39e2b229a2 | -19.50736 | -41.66072 | 2025-11-26 00:09:00 | TERRA_M-M | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b2372326-a1e8-3cc9-a360-e549b93bc466 | -22.17836 | -46.94157 | 2025-11-26 00:09:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 25648c13-c61a-340d-8736-2f88a2e3d252 | -22.65477 | -42.10596 | 2025-11-26 00:09:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2db8ebef-d093-3f88-87d5-89b311a4ba9a | -20.57336 | -45.87305 | 2025-11-26 00:09:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3b6d308d-2170-39a9-b5b1-f040a72a5aaa | -20.61876 | -45.65185 | 2025-11-26 00:09:00 | TERRA_M-M | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f0bcc918-57f5-3b78-8b0e-24ec11fa6e45 | -11.26029 | -49.47016 | 2025-11-26 00:11:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 34721060-37d4-3a9a-976c-863cf99c723e | -8.59201 | -40.5792 | 2025-11-26 00:11:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| cc412d99-0d1f-3098-879f-a6d4717d1ad3 | -9.5343 | -35.71145 | 2025-11-26 00:11:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| 5ca47330-5902-3345-ad1f-47ae053069f4 | -7.7286 | -35.05896 | 2025-11-26 00:11:00 | TERRA_M-M | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| 987ac682-5c40-3dea-8c89-f457c8cd5462 | -9.13507 | -44.40544 | 2025-11-26 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c9b7b9c7-1b61-3de1-a7a1-e344dc4d1a43 | -3.36234 | -49.50019 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 4979b950-b671-3948-8de0-4d5024654d9e | -2.922 | -48.23375 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| c15c1d0d-cf92-330f-8ce9-0086edfe9cc8 | -4.30594 | -45.37398 | 2025-11-26 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c154d525-7024-3e82-b7bc-df8c9d82763b | -7.75096 | -44.18626 | 2025-11-26 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7666ddb5-2b07-36d4-bb0b-00b61804a682 | -4.45059 | -44.30695 | 2025-11-26 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| da80b146-fff3-39bb-ada6-3d4b98161556 | -2.4369 | -45.45768 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 86800d0d-d2d8-3781-9838-63fe6f4980a4 | -7.50482 | -38.33034 | 2025-11-26 00:13:00 | TERRA_M-M | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 47c0d08c-71e4-3ad6-9ef9-1bfafa91a6d7 | -3.90276 | -45.72288 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cbc19c70-1fcd-3b87-9b9c-8eb40fa0fc64 | -5.76044 | -46.43884 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e482940-fe5e-3fe3-b324-cfb67cad6b5b | -2.94063 | -45.49557 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.3 |
| b0294324-461a-39a1-b27a-2f564b6315a3 | -5.23448 | -45.42524 | 2025-11-26 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ef2dceb1-2771-3552-ab05-c1647be49db4 | -3.65798 | -44.83072 | 2025-11-26 00:13:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6bab9404-8007-3165-bbf7-45f097bcb44a | -4.39191 | -45.26534 | 2025-11-26 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e32c5f6f-6836-3ab0-8f7f-6ecc584bc070 | -3.1853 | -46.59644 | 2025-11-26 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c858efd9-0310-3841-a91d-14b1316de518 | -8.0581 | -43.11029 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| f551a564-a706-3d88-bf43-7932bf00c30b | -3.38212 | -45.49949 | 2025-11-26 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1cfeaa8a-b34d-36b6-b553-cce0e774c993 | -3.29314 | -51.27064 | 2025-11-26 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a37a4dba-4dd3-36e7-a494-4d87cca41f3d | -7.74331 | -44.19669 | 2025-11-26 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f3ea969-5a50-3715-855b-0eb4063f6e2e | -5.41648 | -43.05355 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 67daacc3-1a5d-303d-8428-f7763ee3ae02 | -4.04619 | -48.88673 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6698e1ca-9809-3e4c-bb26-df1364958b96 | -3.32756 | -44.05101 | 2025-11-26 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ac5c2225-a037-348c-b04b-8ed84dc354a8 | -3.49363 | -44.51048 | 2025-11-26 00:13:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08bc5325-312e-3ea5-b174-4b7a69a79e96 | -3.3701 | -49.25615 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b95961b2-6383-3e5a-9570-efc31888264f | -5.28606 | -43.63504 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5421524a-45aa-3aa1-8a0d-b98dcff4f82e | -3.39528 | -47.19157 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a304c148-ed02-3a31-a0a1-095be38ff4fb | -2.49597 | -48.15745 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4e7caa98-cfda-3967-bae1-15a6760e8ec5 | -4.14594 | -43.63438 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec269ed8-09f3-3985-b514-2f5139489814 | -3.13569 | -49.41212 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0f8e90d8-1506-353d-b1d1-ebf1453b4b62 | -8.04882 | -43.11166 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 8b1adfb4-a783-3675-8f40-a15a4ffa93bf | -4.11946 | -44.83672 | 2025-11-26 00:13:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b91ba90-a564-367e-8d0b-a043ae92f90e | -4.56228 | -49.69381 | 2025-11-26 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 82abe63b-4982-31e7-a653-6ee254133995 | -3.17026 | -48.0316 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6c3c5c1-8423-3774-8351-b51a3f592b36 | -6.07687 | -39.55018 | 2025-11-26 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 37de869b-3152-38df-b249-8ce35d10ba0b | -2.82002 | -49.11759 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 02c40283-4d90-3ed8-a690-063b53448301 | -5.50079 | -45.28816 | 2025-11-26 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cf368fe4-b036-3a28-b287-3ba95cc385ce | -4.13974 | -43.28138 | 2025-11-26 00:13:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b149c708-4100-3554-a3f0-42796dcc8882 | -2.28764 | -47.0425 | 2025-11-26 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 2cf12fad-f411-328c-aeee-f3b85a232510 | -6.31179 | -43.78514 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 6b229849-f9b7-30b1-81af-9d2d39ec2280 | -6.56836 | -44.03323 | 2025-11-26 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8085776d-98c7-3093-b263-2790e0e09e98 | -6.51862 | -38.83438 | 2025-11-26 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 80.7 |
| f82e0e79-0753-3f17-a48f-56632166c36d | -5.27816 | -43.64625 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 49215ea7-e6d9-3d9a-86b3-0aff4b9e199d | -3.1692 | -45.08808 | 2025-11-26 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6ca49790-55e7-3432-a2d2-1a91325408c1 | -2.89015 | -45.59923 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe30a381-d809-3b67-b31b-507b367ce728 | -6.31314 | -43.79461 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| d503ce89-fafa-3470-8d41-ba5431c5f31b | -3.18409 | -46.58759 | 2025-11-26 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89062aa8-df31-38d4-890c-bbaea8b49f7d | -2.88947 | -51.81592 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| c32d9481-f9c0-343c-824b-2284f1b69782 | -3.25841 | -51.16988 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| efd43760-2d1d-3ded-bf6e-3598f0aa45bf | -6.1195 | -44.83996 | 2025-11-26 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f89af801-67eb-3e76-99e2-2e8e12fa3eeb | -3.22349 | -50.58204 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0def595e-eb52-35ea-9170-f2fc587bb850 | -3.77392 | -47.13303 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ac8dd80a-c5d3-3887-8641-ad3c4de25456 | -4.18371 | -43.72562 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5462b16a-8b6d-3d7e-ba6a-c5d135ccbb04 | -7.22681 | -42.19056 | 2025-11-26 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 41fe9fe1-3590-3dfc-a813-90345c2a2ed1 | -3.92406 | -43.36301 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec804400-7b0b-3e07-8252-8bd671f934b0 | -4.58958 | -45.69997 | 2025-11-26 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e7a6016a-f205-3061-b8ff-ed982a8ae8ae | -4.65071 | -45.07395 | 2025-11-26 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5e3dc61-0202-38ec-92ec-ca203a9d9db3 | -5.58103 | -46.27495 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca020a1e-b2cd-3976-bd2e-3655549087fa | -4.56263 | -43.79839 | 2025-11-26 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c53ed4f7-e0e3-30c8-988e-8fe9eb52bc47 | -5.42606 | -43.05204 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 271aa9fa-3fc7-30a4-829e-b0c7bc3c8f4e | -3.18369 | -48.62351 | 2025-11-26 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fd25e630-34fd-3e94-a38a-9353f9cba878 | -3.25749 | -51.1795 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 41819c20-2710-3e3e-9f01-a73850ea13d6 | -3.47128 | -43.76391 | 2025-11-26 00:13:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 879e030b-c2a6-3c26-a84f-8730311bdd03 | -2.15478 | -46.08162 | 2025-11-26 00:13:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e00e0b5b-4579-3615-9482-493ce61b1301 | -7.48297 | -42.75727 | 2025-11-26 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 14cd3ef3-d15b-3030-a198-b62097c43d50 | -3.21089 | -50.17051 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fbd4b293-0d2a-3761-9171-884cfde63e06 | -4.22943 | -48.36975 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2ad69344-ec08-33df-9484-37b2447c41c6 | -4.14735 | -43.64451 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 94f677ed-8d10-3f98-a258-c9b33803a6bc | -3.21381 | -45.14627 | 2025-11-26 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e56b7656-26c6-3528-8319-dcd62ed107a9 | -3.22275 | -45.14501 | 2025-11-26 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7efb63a9-c688-3b4f-b462-e963b82a0e2a | -4.17433 | -43.72699 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 644.6 |
| aa375969-4782-3c07-83bf-a8c8ca808587 | -4.77267 | -46.42485 | 2025-11-26 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1e3b234f-d5ed-3fff-93e9-1136e7f0a2ca | -4.25146 | -45.12466 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6b39a427-a95b-36ea-92a0-1a12572931d2 | -4.44926 | -44.29753 | 2025-11-26 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd4c1f25-d38e-30ff-accb-5142db0f9a0d | -3.47697 | -43.4304 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 479.4 |
| 9aed8d3d-d0d5-3cd4-a872-2bab3f81e3b2 | -4.71649 | -47.15661 | 2025-11-26 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0629ee14-4305-39e4-8c75-0d5c970f5cb1 | -4.4565 | -47.61448 | 2025-11-26 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a69d2da5-c03c-359e-a9b9-0bdaa6ea1877 | -4.86197 | -47.54387 | 2025-11-26 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 787afd68-9480-39e2-b7d8-dcfc91448dcc | -3.30615 | -50.27278 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e1a832e3-8fa3-3832-8081-8824b365ece4 | -3.69595 | -47.64199 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e39d9837-0ab2-3a33-a2b1-2f3aa50d2d2f | -6.75911 | -44.21006 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9afc70da-a8ad-3537-92ff-6ddc0606ba76 | -4.276 | -50.5557 | 2025-11-26 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 35573b30-bb9c-3241-9c2e-eb38d7f3980d | -8.16301 | -43.19891 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| ec2fe274-e7e2-3292-99ef-22c3c8f5205b | -8.07021 | -43.12857 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 3534b0cb-f8b2-327a-8a8f-64f03031d5dd | -4.7478 | -46.57407 | 2025-11-26 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d03a6802-3f51-35af-b4e9-6190067be3ce | -4.44929 | -44.75607 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7ac79020-5e5e-3e45-9491-068fddabcb0b | -4.1888 | -43.6942 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cb342727-afbd-3843-b585-eb068669afdc | -2.85825 | -45.23942 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7d79855c-3071-3af0-8a1d-97b29cd9bb4b | -8.0424 | -43.13269 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |


[Clique aqui para ver as próximas entradas](README2.md)
