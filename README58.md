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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7e9beaf-56a1-3fb1-9484-36aea5a07d7e | -14.57985 | -48.01955 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02d6b727-7fc4-3d5e-803f-f7082978de18 | -15.0669 | -50.06286 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b7afd1d-8d21-3368-9d58-05a30e93236a | -15.75179 | -53.68083 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47c168ea-c7ac-39e1-a929-286079c038aa | -15.22071 | -52.37526 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb281e4e-b233-3f36-baa6-a2b35dca4bc3 | -15.72773 | -53.62366 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23b251a9-9b79-3aeb-9b00-7622a7aeb405 | -15.54878 | -48.41225 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f64baf48-c226-3541-9287-1a5076de075d | -14.55928 | -48.08768 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 939408b7-79f0-3958-91ec-c09f41dfac1d | -15.73953 | -53.61715 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bb5e26d-3a40-3757-a5c6-645fc9148de8 | -15.73892 | -53.62124 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5049ace-bc1f-3466-810c-ed060157df84 | -15.85326 | -52.29066 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a3c2d2b4-075e-32a9-87dc-75727ed00805 | -16.37363 | -43.03797 | 2025-09-05 04:59:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0efad443-8d55-3ca9-8781-fa31fc57ddc9 | -15.16095 | -52.39349 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d51e921-525c-3ce6-9443-13671db93509 | -15.87209 | -54.92887 | 2025-09-05 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c61034d7-48fc-305e-ac22-38a096811335 | -15.2108 | -52.36416 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b459243c-9503-34f3-b1e4-7a406c67c5d2 | -15.70888 | -53.60422 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea0f3b27-9dbe-329b-ad63-707789b07a13 | -15.54396 | -48.41138 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5c56db3-5cad-3024-91fd-47ea9a31ebe4 | -15.19828 | -52.37186 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ada43a0-4f27-3d7c-9ae7-67f221f7ccc8 | -14.56471 | -54.53222 | 2025-09-05 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d982ab9f-8bb8-3534-85bc-de4c7dcb2692 | -14.3749 | -53.12596 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 797a536e-87b1-3d6b-b7cb-3accfa2ce747 | -15.74243 | -53.62194 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0e64637-0bdc-3eb6-a3b8-3027c5d307c9 | -15.13673 | -48.16394 | 2025-09-05 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 805abb98-5f37-386e-bafa-baac9cda72d9 | -15.19698 | -52.38121 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f937fdd-5a31-3300-b3dd-a93c1eed8a58 | -16.30196 | -45.69376 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6eaa4a8-bf0f-384e-a928-91e3d4a5c3ff | -15.74062 | -53.65807 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9670cab-6761-3ebc-b229-6cc4440ba91f | -15.04745 | -50.04315 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5409c400-917e-3fb4-8d81-5bc170804b7b | -15.31809 | -52.74298 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c48c379-076e-3797-8697-73123a68acf2 | -15.04697 | -50.047 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00cdaf31-2e0a-361d-98a7-50d277d1273e | -15.61889 | -52.90787 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 97f52aec-a834-37b5-bba6-35f41f072e68 | -13.11397 | -57.1171 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdae41c6-39ed-33a0-a566-bae9f9cb63e0 | -14.58535 | -48.01536 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44de26ab-6a26-350a-a16a-efa478b33ae3 | -15.85581 | -52.30027 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18071435-cf58-317b-855b-4657501bd673 | -15.72478 | -53.61908 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1089ff8-b93c-3505-9786-5742679a126e | -15.85202 | -52.29973 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e8db83d9-2d87-3f82-b3b9-26e338fc1b20 | -14.56642 | -54.54392 | 2025-09-05 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5119adcb-0142-3073-8c21-37a2d0b1d980 | -16.45622 | -45.26327 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adfc243d-0656-3a99-a3b2-18ec529cb647 | -15.79015 | -48.70193 | 2025-09-05 04:59:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f62582ab-0185-36fe-9f79-8271115895c2 | -16.30782 | -45.69447 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46dd12ab-4778-3652-af6a-233634c0b04a | -15.04853 | -50.08478 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67348ec1-3b81-31d5-99ab-4893e238703d | -15.1458 | -52.38328 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cfec63a0-fe92-3173-a28b-071f36256398 | -15.75414 | -53.66446 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecd1576c-6745-3949-8e5d-0b2861f6ca4c | -14.54558 | -53.06323 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| deffe7dc-509a-3440-b910-41198b9b6754 | -13.1106 | -57.11652 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3a12742-6834-3122-af94-dbf6b431f0ca | -15.56947 | -50.33214 | 2025-09-05 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a75ae08-c709-34d0-8c22-be028a28f8e8 | -15.06739 | -50.05904 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55ba854a-5454-317e-a967-fb626c9c1ed5 | -15.6317 | -52.89453 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97b8e17b-0443-3809-8b10-a63bf29f8b82 | -15.16468 | -52.39413 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51f049c8-f5ab-31fc-8434-403a18d30c51 | -15.73127 | -53.62414 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b8647d-c5b6-37e5-80b7-23497ae9f04f | -14.58279 | -48.03654 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 576d1239-ead8-342b-934c-88300fe65e83 | -14.58608 | -48.00934 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a92df30-0982-332e-a639-f1ad4653df7b | -12.34931 | -63.65042 | 2025-09-05 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2b648c0-affa-3348-85e8-2e50444261bb | -13.10664 | -57.11961 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69b6e98c-5799-3d10-aeab-dbcabea4e1ec | -14.56162 | -48.08805 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2165590-ac22-36d8-8993-005ce943b9a7 | -16.30689 | -45.69237 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b41ceecf-5c69-3ab0-a9b6-4478f86a10d5 | -14.99579 | -50.08606 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fa80ebd-a7b4-3beb-ac6f-6e6004762884 | -15.86871 | -54.92833 | 2025-09-05 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6fdc7a6-d29c-3982-ad2b-0aacb3d97512 | -15.06211 | -50.06602 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e78819-4287-30db-b05c-ee5c585906f4 | -15.7183 | -53.61395 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9909ff3f-ca55-3eb6-9b39-894c177844bf | -16.45669 | -45.25862 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5712f65-6fe3-3604-b04f-1863463769f3 | -15.13661 | -52.34024 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5615a5d-d6c0-3931-ab47-936d173eaa6f | -15.75591 | -53.67725 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bf7bc69-22ec-375b-a32f-d9ae2bea74a6 | -14.56528 | -54.52848 | 2025-09-05 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 462b732b-364c-3444-bf97-a43bc0da4517 | -14.28004 | -51.87334 | 2025-09-05 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b74e3f47-167f-3419-b712-56ac1f42a489 | -14.55679 | -48.0869 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f78d387f-8c42-35d5-a5fa-920dfb01d3e7 | -15.04474 | -50.04746 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6b82f90-478a-3786-b3e0-e8008366d10e | -14.98388 | -50.0766 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 716b5b5a-4ee1-3ba0-ac74-d9651bf6f75f | -15.56899 | -50.33592 | 2025-09-05 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20071054-f6fe-3b69-9bbc-d46c8b28199b | -15.74943 | -53.67214 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8818fbe9-1983-3917-aa89-102e1ced25c9 | -15.2159 | -52.70243 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd8671d1-f41b-3454-8b78-71be27df53ea | -15.85642 | -52.29582 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fde5b270-22ca-32de-a352-e5c9c603324b | -14.57189 | -48.08538 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d2768bb-df37-3aa0-b45a-3c134f4f7f22 | -15.04954 | -50.04442 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3347a742-863b-3a1e-98b3-0ee3afcfc33d | -15.78539 | -48.70119 | 2025-09-05 04:59:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 958f6bb4-8a90-37c4-b67a-e7094f67c81c | -15.75237 | -53.67675 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e74c907-edf1-3396-8544-67618492043d | -14.57845 | -48.03116 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddb1cedd-85a1-3aa9-a434-2f69144705d9 | -13.10783 | -57.11229 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cfc24f3-74c5-3ee6-ae6f-3ba503f4305d | -16.30646 | -45.69655 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4151d331-82ec-3219-96f2-9a558c78f449 | -15.04316 | -50.04235 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d45337c-b54b-3f55-a246-03ba4f49dead | -14.4691 | -48.4876 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb3d3cdf-3500-3d4d-9893-e69b0606d576 | -15.61286 | -52.89785 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13366982-eaec-3909-b26e-2dadafffabde | -14.58767 | -48.03744 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02422cf4-e8cf-3749-84bf-1b87fddd5f67 | -15.05373 | -50.09733 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73001b5b-ac15-3897-9a65-40d6ebd87838 | -15.61525 | -52.90725 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| af2ff5c0-b783-3577-92f3-89f6d20cf7ec | -15.14708 | -52.37421 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af5e1fe6-0a1c-3cf7-9e66-95315806df48 | -22.68262 | -47.1343 | 2025-09-05 05:01:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea99f6e8-c452-3e54-8962-278ae43438e5 | -22.33199 | -54.7833 | 2025-09-05 05:01:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5bb2674-ef15-3506-a369-9e8352f8740e | -20.75212 | -47.13524 | 2025-09-05 05:01:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73247538-684f-3037-a95f-d17db9e897d9 | -21.8043 | -46.79699 | 2025-09-05 05:01:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ac5169e-913b-369f-9880-3c9bf2de9151 | -21.79815 | -46.80011 | 2025-09-05 05:01:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 911d5eaf-e34e-3719-89d6-5f347abefbd7 | -22.65722 | -46.82041 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7279b10e-4c42-3572-a149-2814a0996358 | -21.01697 | -47.67868 | 2025-09-05 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07efcc10-a5b1-3785-928b-759a0ef1739e | -22.5084 | -47.69501 | 2025-09-05 05:01:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3cb5b8ed-a1df-3c95-9d04-7e1a5dfe3a40 | -23.44007 | -47.04786 | 2025-09-05 05:01:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96143378-895a-3424-a3a4-d3cfc8097452 | -21.79858 | -46.79734 | 2025-09-05 05:01:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6f0798b-d765-3703-9eec-03b56324fa72 | -22.27144 | -49.56814 | 2025-09-05 05:01:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bde302e6-1f3a-36f4-bf7a-abc85bd310e7 | -24.64533 | -49.99368 | 2025-09-05 05:01:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cad0416e-99d1-3b99-a936-78c58f3fd01a | -22.51659 | -47.09316 | 2025-09-05 05:01:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86373cd9-a32b-3d8f-b076-d3e6dba82441 | -22.66304 | -46.82164 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 81477256-e859-37b7-84f9-ace054638798 | -22.91822 | -46.57694 | 2025-09-05 05:01:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 572c2b8c-4531-3293-a524-e8187cee1cd8 | -21.80437 | -46.79831 | 2025-09-05 05:01:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b82b9758-1d8c-3539-bc50-b4e8c9366e31 | -22.66338 | -46.81761 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
