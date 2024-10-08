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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04296a02-128e-3cc8-bd64-99c9445b7df6 | -10.6256 | -55.9154 | 2024-10-08 04:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ae028762-f8d6-3a38-a77b-f8221733cded | -10.8755 | -63.8979 | 2024-10-08 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6ea9747f-84b5-3b2a-9b00-a6543951b3cc | -10.8754 | -63.9169 | 2024-10-08 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8c132da3-99ca-362d-81a8-48248a886599 | -10.8941 | -63.916 | 2024-10-08 04:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| a961e942-135f-30ad-ab43-a37d8c7570b7 | -6.21835 | -55.65411 | 2024-10-08 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8613819f-c360-36ed-9f99-41e463ff46f8 | -3.61752 | -42.75363 | 2024-10-08 04:55:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f2c0f83-ca2b-32ec-969e-42a47b1365b7 | -6.31384 | -43.37207 | 2024-10-08 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2034a9f3-28db-32f3-a1fd-f4f481b1528b | -6.31327 | -43.3763 | 2024-10-08 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cf6d496-463b-3ace-a81d-0f8d7170aabd | -7.78512 | -43.08581 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d8540c8-6ad2-3a44-b833-44f7f54bad4d | -7.7845 | -43.09044 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e41c5dd7-763b-3dc0-b303-fc6bf47f124a | -7.78377 | -43.08415 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3cbd9250-9100-37fb-9245-8a86d831fefc | -7.78318 | -43.08882 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 810c825c-4404-3a62-ba2e-28007e0123c4 | -7.78259 | -43.0935 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2b8da3e-4758-3510-98bf-10aaedd49829 | -7.77767 | -43.09455 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0e0f6a6d-68ea-3034-ac0c-ec6bef554b28 | -7.77155 | -43.0934 | 2024-10-08 04:55:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3cd7ff6a-f3f0-3c21-b6e5-6a57656078ae | -7.6609 | -42.49025 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e91b59a3-4152-34af-be73-10b5d564a3c1 | -7.66025 | -42.49542 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03a8fc3a-d42c-3bdd-9ced-bcc5dd968ca9 | -7.65997 | -42.48988 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38b785dd-6a56-3aa2-8d0f-cf5ddb7b7d63 | -7.65959 | -42.50059 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b243cd8-7e60-3434-a8f2-5e04398f4db5 | -7.65927 | -42.49505 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d5c7d6e-d4ce-3a33-bf73-9b3efa9ef909 | -7.65858 | -42.50021 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1f684d6e-ccbb-346d-be43-cb126d121745 | -7.65518 | -42.48409 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a179d93-32de-3f2f-a45e-6f4a136bb6fc | -7.65451 | -42.48936 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31ad598e-da89-3aa2-a54d-27e188985f00 | -7.65358 | -42.489 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a9318bf-5254-34a4-8bbb-4cde35585f70 | -7.65255 | -42.50492 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cb3df61-055c-3058-9c09-e36704567290 | -7.6519 | -42.51003 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf3a433e-96b7-3a8b-b932-7d9142658d16 | -7.65126 | -42.51511 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd5b1929-2e44-35fe-a780-0f2e35340474 | -7.65062 | -42.5202 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d8533ec2-dff7-3f04-b9ea-9a2acfc0f210 | -7.64947 | -42.5198 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23f8fc71-33ce-3d6d-b586-f44a1c6bfeff | -7.6488 | -42.52485 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98b20045-2de0-3d3c-b9fb-1659bb3ecb98 | -7.64361 | -42.52428 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cf3ef4c9-89c0-32da-aa09-e868053aa1e0 | -6.83315 | -42.80063 | 2024-10-08 04:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| eaa5e3d8-8081-330d-8ca6-c6025adeeaa4 | -6.8325 | -42.80545 | 2024-10-08 04:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc57d2a1-6a78-350f-8047-ee9aba62aa42 | -6.54169 | -42.70654 | 2024-10-08 04:55:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 800ed33c-06c8-3d4b-ad2e-a645a839440b | -6.48023 | -43.87995 | 2024-10-08 04:55:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fde97b2a-19be-3633-b132-f204acb1c962 | -6.16322 | -43.52706 | 2024-10-08 04:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cb65d39-b821-31b7-ab72-f0db64b70768 | -5.89142 | -43.87865 | 2024-10-08 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cca0ef4-b0df-39c5-ac28-221e3f2849b8 | -5.89019 | -43.87403 | 2024-10-08 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb19492b-df1b-393f-8bf1-8a0d6ee3e10c | -5.88962 | -43.87797 | 2024-10-08 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9627e751-60aa-316f-a054-2741946ac74f | -5.88626 | -43.87374 | 2024-10-08 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16eea873-8717-3cec-916a-6ab770b931a2 | -5.88572 | -43.87772 | 2024-10-08 04:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b92c5d6-1d87-3615-ae82-9a60913cc592 | -5.98829 | -44.43987 | 2024-10-08 04:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 680cd027-19a4-3a54-b639-588edef49929 | -5.85298 | -44.87497 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb18adbb-a4b1-3c1b-95bf-945160628918 | -5.85083 | -44.87108 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c6dd51e-b1dc-3626-b26a-54225b00fde8 | -5.85038 | -44.87434 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25936046-e960-30be-80aa-acc690a1d467 | -5.84808 | -44.87114 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b3714b4-b4e3-3188-91c4-d35df5a24f0e | -5.84761 | -44.87437 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3c5a874-4e3e-3b45-8e66-e7ebc4635b6b | -5.81982 | -44.12487 | 2024-10-08 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15ae6888-36a6-34cd-968f-9fae88d39c97 | -5.81874 | -44.13245 | 2024-10-08 04:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17f562e9-30ca-3128-8244-8211345395f5 | -5.81421 | -44.124 | 2024-10-08 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43e32022-e64e-3889-93e6-72b8ef5cadcb | -5.81367 | -44.12783 | 2024-10-08 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dab39356-c23c-339b-b7bf-4fe078a7eab1 | -5.7111 | -44.81318 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a9eb981-ca56-3ac5-a8c0-2b420ab36a7b | -5.57917 | -44.87908 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 92844089-b552-3ec8-9b8a-33086e4e5ffd | -5.57478 | -44.8717 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1c042fd-d8d0-30fd-ae1b-ab0376b8f5e9 | -5.57432 | -44.87498 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dad51a63-f786-3d64-a047-44fbb1f3ac50 | -5.57385 | -44.87826 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8be570b6-0ca2-3ace-a47e-f4864563c074 | -5.5734 | -44.88152 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b303a5a7-bb52-3788-8953-f9249180f805 | -5.57294 | -44.88475 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 81c8b6f9-3755-3e7e-aca7-b93b00dc170e | -5.56902 | -44.87402 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c44be127-33f1-35ae-bbff-dc01d8eabe1b | -5.56856 | -44.87731 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b4d52020-bc62-3301-b89a-e9b467c16d61 | -5.5681 | -44.88058 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3a51d3c9-9f70-3ef7-a389-b2dd5b14cf22 | -5.56764 | -44.88385 | 2024-10-08 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7e8e21af-551d-363f-a7d3-78bf3a6c2290 | -5.48314 | -44.24932 | 2024-10-08 04:55:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 323d5601-c76e-323f-b68f-af369ad999d4 | -5.48261 | -44.25307 | 2024-10-08 04:55:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5905a9d9-e146-3320-ae5b-dc979edc2d7a | -5.48209 | -44.25669 | 2024-10-08 04:55:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0fbd555-91bd-3d03-87ff-7b033ae28e95 | -5.47706 | -44.25232 | 2024-10-08 04:55:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebdac8a3-5703-3706-bf60-a32a4ced325c | -5.47655 | -44.25595 | 2024-10-08 04:55:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e637b242-4839-3cc5-89e3-a3bff49b2a3f | -5.47605 | -44.25948 | 2024-10-08 04:55:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4b7f81d-cc74-347a-a8d1-585b103e86fc | -7.84722 | -45.35323 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38e8ccd7-7519-3426-950f-20a91c3a6dcd | -6.69424 | -43.95366 | 2024-10-08 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e282d7e-d485-34e7-9d44-e77fe34f41a5 | -6.69369 | -43.95763 | 2024-10-08 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85bcdf0b-3c5f-35cb-9345-39f7270454ce | -7.27731 | -44.96719 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ba1c402-b708-3c77-abef-77923936202f | -7.27686 | -44.97056 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59cee5be-3688-3843-be93-58d010abb5ea | -7.27189 | -44.96644 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ed13d13-f64f-38eb-acb0-c58316b14c72 | -7.26694 | -44.9623 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f9a0e99-c44f-3d42-9dfa-e623eb58244b | -7.26648 | -44.96564 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86914f29-e061-38ff-a455-3e314a9f81f1 | -7.10019 | -44.58038 | 2024-10-08 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dad8a42-bdde-3bfb-a62e-90672f1ddbb1 | -7.09517 | -44.57568 | 2024-10-08 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bea61e0c-e3b9-37a6-954f-4299691c1201 | -7.09466 | -44.57944 | 2024-10-08 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b91194d-8eab-377b-98c8-3e7ca4908534 | -7.08311 | -44.5813 | 2024-10-08 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 756fd023-556f-3214-b1c4-c43d5942f58a | -7.08263 | -44.58485 | 2024-10-08 04:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6207b659-628e-3b06-b049-85fe1e865e54 | -6.58059 | -44.17657 | 2024-10-08 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03fa80c4-16d3-3bef-ba36-eece223b5190 | -6.58006 | -44.18033 | 2024-10-08 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 877eea8b-8941-3ade-89f2-dafd113ae3fe | -6.5749 | -44.17606 | 2024-10-08 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e16548c-2596-384d-9398-86bb56dbd0e3 | -8.14072 | -44.42021 | 2024-10-08 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93fa3080-7557-34f3-8545-2b4cf95a4c88 | -8.13606 | -44.41179 | 2024-10-08 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7430526-0f29-3658-b7e5-f98e871e3666 | -8.13554 | -44.41563 | 2024-10-08 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5339a6ec-9426-3ad4-9e54-208bb50da5b8 | -8.0066 | -44.37252 | 2024-10-08 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 956cb2d1-9840-3358-b07a-cf9cf49ba078 | -8.00609 | -44.37637 | 2024-10-08 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd8170f8-3305-3586-af67-62a512da4cba | -8.00557 | -44.38023 | 2024-10-08 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19042e03-6d32-3589-9c13-bb3379974092 | -7.86319 | -45.35545 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c8a3e6d-a7e1-37e4-9d9d-b084a42558a6 | -7.86274 | -45.35875 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb7298e6-1595-333c-9b1a-7362c5aefe3b | -7.85786 | -45.35472 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61c55abd-e96f-334c-8313-bf8a85715ceb | -7.85742 | -45.35801 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8db3ac8a-33b8-3db0-ac1e-ee77a57733b2 | -7.85698 | -45.3613 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7e45378-63c1-375f-b039-ec74b39c0bc0 | -7.85254 | -45.35397 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1cda1e39-dae2-3ce8-9201-7253f2564678 | -7.8521 | -45.35727 | 2024-10-08 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4fcbf52b-c878-3e4f-9fed-d00c5b05e274 | -4.92466 | -45.64902 | 2024-10-08 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e14b5551-ee69-303d-ab3a-d8a08e17d33e | -4.92383 | -45.65477 | 2024-10-08 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a4362f8-1766-3ccd-99fd-ccc650cfedb7 | -5.71302 | -46.46297 | 2024-10-08 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README79.md)
