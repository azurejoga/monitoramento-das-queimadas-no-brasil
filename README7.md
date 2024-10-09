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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e1e3acd-ebe9-3d2a-943a-a6e81513d4e1 | -20.7839 | -47.2559 | 2024-10-09 00:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 452.2 |
| 355e2221-1b18-30d5-9d63-a05ecf63703e | -20.7846 | -47.2323 | 2024-10-09 00:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 428.2 |
| 6e180de4-8a33-34ec-a3c7-0f0dc85f05b2 | -20.8045 | -47.251 | 2024-10-09 00:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 58c7f09c-17f4-30be-b4bc-41200754dcaf | -20.8052 | -47.2273 | 2024-10-09 00:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 9614491f-22a6-3ad1-8349-8e932aed4f95 | -22.579901 | -46.664299 | 2024-10-09 00:37:01 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 089a126c-c874-38be-bdbd-b5130918fc50 | -22.5683 | -46.6572 | 2024-10-09 00:37:02 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6949a036-b9c4-3cd6-8425-eb320b288324 | -22.5702 | -46.6665 | 2024-10-09 00:37:02 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ad115a2-005a-3fc2-a24e-b1f800085b94 | -23.129801 | -49.805401 | 2024-10-09 00:37:02 | METOP-C | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d10b351-9c42-3219-a2cf-aa8b7475a519 | -22.819799 | -48.4119 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 528ae9ec-0e7a-3871-bcdf-8b8ee31525e0 | -22.822001 | -48.423599 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cf2d4d46-9ad4-3e68-87da-0c40de726d2f | -22.807899 | -48.402302 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4552d4b5-9358-3f4d-a6f9-8f7b4a444c03 | -22.810101 | -48.413898 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b51c207e-8377-35dc-b512-ec8b5394f262 | -22.812201 | -48.425598 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57b24917-4010-3048-a658-9a9909dc4776 | -22.8144 | -48.437199 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbde8c9-8a98-3235-bedd-a27cf2abbf52 | -22.800301 | -48.416 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b0bdb269-58b7-3ef1-901e-af98ba6bdbe4 | -22.8025 | -48.427601 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 62c7698b-498d-3559-ae1b-914e0dbfcb27 | -22.8046 | -48.439301 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 71d80e9b-6009-3bb2-a6d7-d03b77d42f53 | -22.806801 | -48.451 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 980897a3-50ae-3e53-8633-1fa298a3724d | -22.7927 | -48.4296 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2a0c17-a93e-3796-bd4a-3692fa9d63a8 | -22.7948 | -48.441299 | 2024-10-09 00:37:03 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d60a7b9f-96f5-30f7-b065-e50b3f554cd8 | -21.552 | -46.9712 | 2024-10-09 00:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 0bc855c7-7417-3cb6-86b6-978461f6e572 | -21.572 | -46.9898 | 2024-10-09 00:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| ca2de96b-994d-33f6-a7fe-494a4d50cd5f | -21.5727 | -46.9659 | 2024-10-09 00:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 220.6 |
| c108bf5c-1ec3-3615-a453-628d1dec20b8 | -21.5649 | -47.9114 | 2024-10-09 00:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a2c3a0f8-3785-36a5-8e2a-054dba209003 | -21.5656 | -47.8878 | 2024-10-09 00:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f032fddc-7a58-3422-9532-5412a4f9022c | -21.5857 | -47.9063 | 2024-10-09 00:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a6baef86-9099-325b-bd56-7fd207d5dec1 | -21.5864 | -47.8827 | 2024-10-09 00:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 8d987494-bd1f-3a31-93c6-132cc57b0080 | -21.5871 | -47.8591 | 2024-10-09 00:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b0f7fff0-aebe-37df-a294-da53b08d79c6 | -21.8165 | -49.1774 | 2024-10-09 00:37:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| f6667c14-83da-3830-9d80-879959f53558 | -21.8172 | -49.1541 | 2024-10-09 00:37:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| 9334ebca-ed8d-3369-9da9-4601db01e2f8 | -21.8373 | -49.1726 | 2024-10-09 00:37:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 78b67352-292f-34c1-96e0-c365bf214f49 | -21.838 | -49.1493 | 2024-10-09 00:37:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.0 |
| ef17a682-6f95-3ba3-be30-57c3bea1514c | -22.280001 | -46.798698 | 2024-10-09 00:37:07 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e742841b-624a-3d07-a43d-96c0f91d2692 | -22.2819 | -46.807999 | 2024-10-09 00:37:07 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd273dd-f165-394e-89dc-b5a3948ec17d | -22.283701 | -46.817402 | 2024-10-09 00:37:07 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e59a5138-84e2-3902-b851-d80b5526a0d2 | -22.813 | -48.4462 | 2024-10-09 00:37:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7b569117-d382-3d8e-88c5-36e801e4de73 | -22.8137 | -48.4225 | 2024-10-09 00:37:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 690f7795-8c3b-3fe9-9606-2d8f5ea28a31 | -22.191299 | -48.0868 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 068bce80-73f5-3cce-8829-2704c4411dd0 | -22.193399 | -48.097698 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca39842-1435-38f4-876e-bb5aeb754b52 | -22.201599 | -48.141602 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 05016b24-c419-3ab0-a4b8-3b3f11de1b7a | -22.181601 | -48.088902 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 47bc3237-c170-302b-a3a6-cfb73b1f8b65 | -22.183599 | -48.0998 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 754bc73b-747f-3ded-8282-9b7789704a66 | -22.1898 | -48.132702 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b1618da8-af88-3616-a43e-80f1442d6050 | -22.1919 | -48.1437 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8131bd-ad28-33e8-88d2-745e015f4d68 | -22.193899 | -48.154701 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd6db97-61f3-3baf-9a92-4d7b68eb4b6c | -22.195999 | -48.165699 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c8cff093-f106-3551-8102-e2631392e9e5 | -22.1954 | -48.1087 | 2024-10-09 00:37:12 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 011cd968-2833-3553-8b0e-013811b305c0 | -22.1698 | -48.080101 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe46ddf-d2d5-319c-9767-6ef2e9176710 | -22.171801 | -48.091 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca0ed6d-b2c6-3ef9-ad5b-99a5ae2cf79d | -22.173901 | -48.101898 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 645ee248-47c5-37e1-87f8-697f07eadcd5 | -22.177999 | -48.123798 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 99016e68-5d1a-3ecf-8851-f2c48b4f9fbb | -22.18 | -48.134701 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cf899a7c-d467-3808-9c1c-ccc0e4a3753a | -22.1821 | -48.145699 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e5a018e6-ffab-31ef-becd-42a183c7cdc3 | -22.1842 | -48.1567 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3b90239b-e035-3521-92fa-2dd701a878aa | -22.186199 | -48.167702 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d4ca74c1-e984-33e4-a513-8bab846aefb2 | -22.16 | -48.082199 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 058e852f-9370-3928-ab83-451b3779814f | -22.162001 | -48.093102 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1c827f26-e10d-39c9-9072-17514bb08a2d | -22.164101 | -48.104 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 773a9441-5ac5-3012-9808-d836f0a02cbc | -22.1661 | -48.114899 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4c0d6f-daa6-3de4-a53e-b774e0fefa17 | -22.1682 | -48.1259 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b962f013-c541-3ee4-8057-32ad13f7f520 | -22.1744 | -48.158798 | 2024-10-09 00:37:13 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 11e43f93-d205-35a2-86bb-48bdcee1dd2f | -22.150299 | -48.084202 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aca09675-ecc7-385b-b1f7-0f4ed524d298 | -22.1523 | -48.0951 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5936e921-b7ce-3c89-809a-390021966635 | -22.1544 | -48.105999 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 47b180fa-02c0-3a26-a734-7159db4d270e | -22.156401 | -48.116901 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d945e601-9078-375a-a655-befac6d5c1a6 | -22.158501 | -48.127899 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 40182700-92e3-3ee6-8036-35a1ae65257e | -22.140499 | -48.0863 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3d943861-de0e-3847-9ca9-af5f40f680c9 | -22.1425 | -48.097198 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 06d97bed-9dc6-3121-9d01-9d60f2a7e836 | -22.1446 | -48.108101 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 238a4511-59f8-3d4d-9e76-e773770b728c | -22.148701 | -48.130001 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fe3a5086-2924-323f-b790-9c39d3e43baa | -22.130699 | -48.088299 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 770c98c1-9446-3d3e-91d2-e6533e463f4a | -22.1327 | -48.099201 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 55441a43-94d1-3aa3-b111-56f7ce3d0280 | -22.1348 | -48.110199 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b09e639f-5c0c-3f2b-a898-b7431e3c193a | -22.136801 | -48.121101 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04622cfc-e1be-35e9-8821-5271c103f749 | -22.138901 | -48.132 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ce4e78e3-8b8a-3a28-9cca-3b41c7c2e2c5 | -22.122999 | -48.101299 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 71129401-1478-3893-8e74-44de15a8ed78 | -22.125099 | -48.112202 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e20f53e0-79af-3b73-90f8-7828a39d0b25 | -22.1271 | -48.1231 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1c03a55e-b05c-3c50-8325-f986e9b03297 | -22.1292 | -48.134102 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd3b6c8-a982-30f2-85b3-e861c08ea82b | -21.8857 | -46.7122 | 2024-10-09 00:37:13 | METOP-C | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8208e40-4f85-3692-b0be-bcb48f02b354 | -22.146601 | -48.118999 | 2024-10-09 00:37:13 | METOP-C | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bcd48ecd-a371-3c0d-86a3-61ea6ee8520f | -20.9953 | -43.052399 | 2024-10-09 00:37:15 | METOP-C | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57e6f693-27d3-3e93-b1a8-eb288bc28b98 | -21.608999 | -46.6035 | 2024-10-09 00:37:17 | METOP-C | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d051642f-b4e1-3f0d-85c6-40909fb2309d | -21.5993 | -46.605701 | 2024-10-09 00:37:17 | METOP-C | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45a7d560-e1da-30d0-b50e-47afa418a1cd | -21.58 | -46.972301 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 81a0f53c-3418-31be-814e-9feb0c6293a2 | -21.5819 | -46.981602 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dc676dfa-ea6d-3ebe-a295-e9bcd30e7c64 | -21.568399 | -46.965199 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 309c93f4-b434-3dc4-ae10-06f0204ef5b4 | -21.5702 | -46.974499 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4308cb7a-1b79-34d7-abc5-9de05ec4d630 | -21.5721 | -46.983799 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1ec936-6cb3-3d75-a1ba-0a22fe672018 | -21.5569 | -46.958 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 812dac06-c122-3770-b03f-53c953827ce8 | -21.558701 | -46.9673 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b34d1c40-37bd-3e8e-a79e-79e35c5f7584 | -21.560499 | -46.9767 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a1d87576-a02a-3bf2-997b-3947f332ed21 | -21.562401 | -46.986 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 602a37d0-c22a-3cec-935c-4430b12cd9c8 | -21.548901 | -46.969501 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc492e69-ca89-3452-b53e-478949cfe5f9 | -21.550699 | -46.978802 | 2024-10-09 00:37:19 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ee2e826f-a4e0-32af-93ff-f43a4eed0545 | -21.642 | -47.710098 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 41317341-970f-3286-a9cc-36eb8b0e112d | -21.624399 | -47.671501 | 2024-10-09 00:37:20 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc49b84-0949-3a5e-b50b-d67976c5f532 | -21.6264 | -47.681599 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ac397328-b0df-3b1f-8e31-c86d0c56d850 | -21.6283 | -47.691799 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 855b1378-cced-39e5-99b9-c093d6e07b1c | -21.630301 | -47.702 | 2024-10-09 00:37:20 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
