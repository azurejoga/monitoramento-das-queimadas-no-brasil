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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8642ad9-9d33-3ba5-8ae9-e6f1a57bd809 | -5.923 | -44.60224 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f40517d-b832-3fe6-8cfd-1db1af311771 | -4.91288 | -47.85737 | 2024-11-22 04:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59c93ef9-f125-3ebb-8573-3595a104240e | -6.11906 | -42.51069 | 2024-11-22 04:12:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce6768f5-d224-3d52-b1ac-6168f615c424 | -5.13717 | -46.10067 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d85cff9-8e92-340f-a4b3-98d9473ad1cc | -1.20439 | -53.68628 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0e170bfa-426d-3572-8c9a-e23711d15d64 | -4.95683 | -45.62616 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edfc56fe-f082-3821-a5fd-91820b476fca | -3.83379 | -52.25345 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91d7f95a-3b90-3c7e-934d-42e2eabe27f0 | -4.52166 | -46.46548 | 2024-11-22 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376113e4-e13c-3470-ac67-7647b46d3c71 | -3.72887 | -50.43877 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d229d339-1877-3f2f-998d-ca34d34e0b65 | -4.71051 | -44.25457 | 2024-11-22 04:12:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ac37ed6-86a6-30a4-be70-a00e64dbb02b | -5.0076 | -41.95887 | 2024-11-22 04:12:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe03f4dc-85bc-3574-9b1a-4904c576505a | -1.82818 | -46.28703 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f173f49-f556-3be7-9522-098fec0a3f70 | -3.76003 | -46.11605 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 50fb6566-642d-3765-b9bc-05407f32111f | -0.95957 | -51.7218 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b5e978a-e38a-3cc4-a6a3-b4e16d314d01 | -3.00289 | -51.55597 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d508f61-51c2-3a13-878a-fea47b734bbc | -3.3349 | -53.3349 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cfb51da-6cba-3302-8a3a-48c43074b636 | -4.62708 | -44.23011 | 2024-11-22 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 125878c8-7cc2-31d9-be83-fae0e3dfb708 | -2.44113 | -46.53236 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73426a42-600c-3f08-bb8e-3d2ccc0b226e | -4.67157 | -46.37575 | 2024-11-22 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d00b36df-39e4-3348-befc-1adf5c174df9 | -0.9217 | -51.73936 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 697bd520-4039-3ec3-abce-0bf233458c4b | -2.44658 | -46.54831 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eaa0726-3303-368c-86ab-d6885906faa5 | -7.2155 | -45.07955 | 2024-11-22 04:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 697d492b-9b71-3b99-824a-2d8802297153 | -2.56274 | -47.32409 | 2024-11-22 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f2e0968-d04c-3c09-b220-daa63fefbdb1 | -5.81949 | -44.74953 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 903e16ef-308a-31e4-ad2e-3528b50ea721 | -5.75362 | -46.18758 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 201dd8bf-ec94-380f-9b5b-c3401e27d800 | -1.79938 | -48.46679 | 2024-11-22 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c4bbb5c-3b6b-3eab-939b-f217ab502c23 | -6.11797 | -42.51762 | 2024-11-22 04:12:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 38cef19c-fd29-3b2c-ac3c-d7a53fb22164 | -6.19544 | -37.43473 | 2024-11-22 04:12:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1df7c4fb-64c6-3a4e-aeb6-c7f7f93d8036 | -1.18558 | -51.93629 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3c79642-3d8e-31e2-98e5-15d08ec4a26a | -3.85372 | -45.70686 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2cc94b2-8a95-34c3-bd4e-9c7bce2d3a77 | -3.46972 | -45.90649 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a114275-01ad-3ab0-810c-e77cc74e7c90 | -3.67795 | -52.37393 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b13f169-5a0c-35a5-b449-ccb065bd27ed | -1.19922 | -51.96317 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 88cf1b90-7e16-3b90-beaa-66ce05ddcc7b | -1.72624 | -52.7077 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df2d71a5-2cb1-36e5-86ab-496654b50500 | -1.215 | -51.97386 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b59c145c-aa8f-395c-9b56-bf7d21fdfbc3 | -3.03284 | -45.66271 | 2024-11-22 04:12:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d81613e-5fc9-3de9-ad64-7c0cf226a2c6 | -1.19453 | -51.95415 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d67782af-7884-3971-9580-7569bfb80c5c | -2.1627 | -53.79641 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb45dd66-ab2a-3881-b4ce-16087e3cea95 | -1.70672 | -46.69963 | 2024-11-22 04:12:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1c11377-5f9f-3e6b-9af1-ebdd8779cb9a | -4.77248 | -44.1745 | 2024-11-22 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b9613d-8e7c-3ab8-b311-3b017ac31f23 | -3.03776 | -54.84813 | 2024-11-22 04:12:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b9c820-a017-3ce0-b379-67ad724dbd54 | -1.23363 | -51.74439 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2343f84-db00-33da-9401-496aa118505f | -4.95116 | -47.80399 | 2024-11-22 04:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8776a658-ff5c-31d7-8938-34572d6175c6 | -1.18971 | -51.94941 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e27ad12-030c-3e32-ab18-292d51ca6042 | -2.69886 | -46.08286 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53d56cfb-d163-3a06-8efc-6b50dd533a0e | -0.04974 | -51.23338 | 2024-11-22 04:12:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 878d53a4-1a98-352f-9703-b36585bd4260 | -5.24013 | -42.63511 | 2024-11-22 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d2042b-503a-3bdc-9e1b-a2d87d773368 | -5.83575 | -44.01748 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e9a783a-5164-3405-b8c0-1bbebdfbd05c | -4.0124 | -43.24903 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56128c43-adf7-3b40-b001-7d032f768a0c | -1.80779 | -52.16108 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 73e897ff-dc7d-30b4-b9b9-cd61d9088b9f | -3.23213 | -54.23362 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 37342a54-fa89-3fb4-95e9-0dd654be0004 | -1.20119 | -51.9513 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec003ab1-d292-307b-ba09-c96bfc666f4b | -4.99673 | -50.50474 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27d17ff6-d028-3d03-bace-39a88c57f1cd | -1.33359 | -47.96194 | 2024-11-22 04:12:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55f86775-0cbd-3f2b-96ba-a4ec0170e98f | -1.81292 | -52.16606 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dde9b05c-6739-3a26-9d5c-8e8a39720331 | -1.18495 | -51.94028 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0f4660c-999e-3d38-a5f7-d1e679554a33 | -3.34044 | -53.33926 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcc8f205-7580-3e0a-87a2-f6e5360b2993 | -1.22292 | -51.73868 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3e832e3-0664-3b50-b1c8-f2d4def8690a | -1.19611 | -51.94641 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8db85839-9aa1-3aa6-a1f2-a332568d17bb | -2.55863 | -47.32346 | 2024-11-22 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6857b97b-5a88-35d3-b9ec-7566a7ce89e4 | -2.01688 | -51.17692 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2bb4208-0fd8-3354-b064-715845c6ed01 | -2.21447 | -48.20884 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc79f955-c502-31a6-8fdb-f2df7559f4b5 | -5.24345 | -42.63563 | 2024-11-22 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 64cc9eb2-b189-3072-8e27-482b952a2e88 | -3.49584 | -49.96262 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 045c26c8-5160-350f-8fa8-fcf4c43765ce | -0.937 | -47.5574 | 2024-11-22 04:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| aa87f746-cb4f-38e5-9ea9-459942a126dd | -2.66208 | -46.55245 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac6c775b-a170-377b-95a0-adaa6cae1a33 | -2.83738 | -46.68028 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d616c94b-f64e-3dab-9117-8e4c6942a49b | -1.50757 | -53.12997 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c25f97-702d-33f0-946e-7001547273b5 | -3.18326 | -54.32509 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 80c2a31b-04dd-3cb1-9fc6-2ba0ac43b9b2 | -3.84388 | -52.34831 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b58704b-c773-3746-af7e-41bacc803c9b | -2.7239 | -46.09624 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9797d1-5c36-3fe0-9a5d-a0ce9b82604e | -2.63133 | -46.21664 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76c044c0-4e68-376e-9bf3-3d958df9884f | -5.59301 | -43.73914 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dc39033-00de-362e-8b86-f47b451b6860 | -1.74156 | -46.30091 | 2024-11-22 04:12:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 149d3901-01e0-3369-b6d3-d2ab335f1229 | -2.69414 | -46.84511 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91ec8a36-a323-3633-acb8-6bb318c130f7 | -4.01271 | -49.91727 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 00ba71c1-1fc7-39c1-9833-e6105ce86f02 | -0.3448 | -51.56039 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f4e7d4a-4e9a-3846-be59-254d6a3b7b36 | -1.22231 | -51.7425 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 146ea736-0771-3eca-9106-a3fcece22b72 | -2.21132 | -52.23262 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b88a8128-77a3-3c61-9daf-07c444f33912 | -4.99834 | -50.50653 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 640c4619-e846-323f-99ea-d2c2e3344c78 | -3.32391 | -54.09009 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19dd0ade-010f-364d-9340-cab6a9b7b831 | -3.50505 | -53.80629 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b00c7b84-12f0-3f7a-892c-22ba4d968ca3 | -3.66094 | -51.56738 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70d6ab74-a8bc-364d-ab6a-5961c1162b5d | -0.27735 | -51.56802 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 999e824b-c52a-3ded-8870-c941e49b7f73 | -4.21117 | -45.4817 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 666c0f8c-b01d-30cf-9c45-c849a161f4bf | -1.64207 | -47.36262 | 2024-11-22 04:12:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 853917bc-2b42-31ba-aabf-6f8149db9be7 | -5.10499 | -43.16735 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a43018c-985a-3458-b084-2ace6e853fb4 | -5.94712 | -46.19016 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec476d40-46e3-39ea-aa20-3c8bcf2571a3 | -5.12645 | -42.81925 | 2024-11-22 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 194f90f0-8297-39d1-8297-9fe6682a2c9d | -2.70142 | -46.23527 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a06a7b9e-6dfe-37d0-bc1c-12b75712f930 | -3.46504 | -45.90344 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1cab63eb-2a5a-38af-8d54-1ad59ae82c94 | -1.81375 | -52.16006 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1919e949-2d82-32e6-b7c0-0d9e865661e2 | -3.32296 | -54.09555 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32bf6dc3-a703-3dd7-b991-61a0d93a3837 | -3.76262 | -46.11845 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e3991f7-1486-3675-9ab6-359752f491ac | -4.79456 | -46.45175 | 2024-11-22 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 262ffb30-b0e8-3e1c-9679-57b9ea27e565 | -4.40644 | -44.1247 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f111a37-af13-38b8-8e51-d20722d2a0b8 | -6.11573 | -42.51016 | 2024-11-22 04:12:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72aa623f-088f-3602-a5c2-8137fa43816b | -2.39648 | -46.0645 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e34922f-1fb2-3ea8-b2c6-7d9703939e23 | -6.18357 | -45.45163 | 2024-11-22 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e28ac66-5dac-3dd8-8b96-8e4a58e1cdac | -3.53569 | -51.10236 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
