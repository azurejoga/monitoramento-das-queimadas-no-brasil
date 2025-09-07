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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d98c855-c301-3304-a2d3-b9fc82a10522 | -5.9901 | -44.1297 | 2025-09-07 11:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c9e66e91-c696-3c1b-a13c-54a6e2b1659d | -19.4898 | -47.7646 | 2025-09-07 11:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 7a420bb1-70a1-3e7d-8d56-0a3383214abd | -12.8248 | -48.0155 | 2025-09-07 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 6d151009-4f0d-36a8-ba7a-f1eeb0899b9a | -12.8248 | -48.0155 | 2025-09-07 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6762752a-9bce-394f-9edd-d2ad8214970e | -19.4891 | -47.7879 | 2025-09-07 11:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 8e4e67af-8559-34a7-b9e3-6b3849d20047 | -5.9899 | -44.1528 | 2025-09-07 11:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| a681aa63-962d-32fa-9c38-97bfb1ef6727 | -14.4882 | -48.7671 | 2025-09-07 11:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 368908f5-af12-31b8-8056-119f8da83690 | -14.4882 | -48.7671 | 2025-09-07 11:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 175b1b8f-8b0c-3823-8e41-41dccc16536b | -12.8248 | -48.0155 | 2025-09-07 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 2eb630c6-8ff7-3474-9c67-b9d527ed15d5 | -19.4898 | -47.7646 | 2025-09-07 11:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 16c860e5-78b3-3a6f-ae0b-b77dbca28fe4 | -12.8059 | -47.9959 | 2025-09-07 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6aea4234-d768-34d1-a607-851b2ab4beb3 | -19.4891 | -47.7879 | 2025-09-07 11:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 184.7 |
| a42f6902-aeae-3b83-a85f-270d0726fc36 | -12.8055 | -48.0182 | 2025-09-07 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 740d7585-f0ff-37d4-af8a-7a00fd334a7d | -12.8252 | -47.9932 | 2025-09-07 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 4aea72ed-4dc1-3a90-8f79-a52186aa7bc6 | -5.9899 | -44.1528 | 2025-09-07 11:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 323c172d-cce9-3549-a1c9-31f9c1a9d94a | -11.2636 | -46.4843 | 2025-09-07 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3d7d0b0d-6c5f-3fa6-b41d-4213fe068280 | -10.5869 | -48.4772 | 2025-09-07 11:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b374c9b1-cfde-3db2-962e-a32fa3d6a38f | -11.264 | -46.4617 | 2025-09-07 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 98245d63-c316-3dad-8e51-aec3ff2a4198 | -14.5076 | -48.7641 | 2025-09-07 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 56f3058d-1da8-315c-8489-596d227824c8 | -10.1002 | -48.0936 | 2025-09-07 11:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| bc7881c3-afe0-3b3e-a1d5-601c8d0698c8 | -5.9899 | -44.1528 | 2025-09-07 11:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| c6b2ac2b-ea84-31b5-8f45-76960e8cb5c5 | -8.6832 | -45.3221 | 2025-09-07 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3f1c3b57-bdd7-3fa5-9c6f-109b6e97ca3f | -12.8248 | -48.0155 | 2025-09-07 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6c520222-3e42-3eb3-b091-74c4da602a5d | -10.4632 | -53.6132 | 2025-09-07 11:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 95c50406-a128-3178-bfd6-4f429cbe7922 | -14.4882 | -48.7671 | 2025-09-07 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 2bb83068-1eb6-3930-9596-61bfdbbe57d5 | -10.5869 | -48.4772 | 2025-09-07 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| fa2663be-f331-3ed2-b383-2fd0365fa1e0 | -11.264 | -46.4617 | 2025-09-07 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f1345b0f-84cc-3acb-90ef-de9c3a23e593 | -13.2404 | -51.7997 | 2025-09-07 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b63c9388-48c7-308e-a566-ff315f3d48eb | -11.2636 | -46.4843 | 2025-09-07 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0f7aeccd-5290-3379-9ee5-0e78a614a2ff | -12.7641 | -52.9498 | 2025-09-07 11:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 212d40ae-2e1f-341e-94b0-0cc711ebf5c7 | -12.948 | -54.7724 | 2025-09-07 11:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6dd949ba-302a-3d77-8d4e-cc190141b430 | -19.4891 | -47.7879 | 2025-09-07 11:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| c6c910b5-86f7-3409-acc2-06e842d0b261 | -11.5669 | -47.7638 | 2025-09-07 11:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 74c448e2-a0d2-3b83-8608-825041fc78a3 | -12.3016 | -47.2416 | 2025-09-07 11:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 6f3ddb20-5162-3a4f-a7e7-e0401229041f | -10.1002 | -48.0936 | 2025-09-07 11:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 98429256-83cd-35d0-962b-d1dbf277d6ae | -11.586 | -47.7613 | 2025-09-07 11:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 63113fe5-92a6-376b-8379-5f3bc9471311 | -12.948 | -54.7724 | 2025-09-07 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 02897077-2c3a-39c6-bc42-842744948592 | -12.8248 | -48.0155 | 2025-09-07 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 01b93007-9c73-398b-9a16-d0907612e1d8 | -5.9899 | -44.1528 | 2025-09-07 11:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 1dffb19e-01f2-33d9-a0bf-1552c88171c0 | -11.2636 | -46.4843 | 2025-09-07 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| bc299b76-4891-3c0d-9f47-140c5c302316 | -10.5869 | -48.4772 | 2025-09-07 11:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| b8f13a47-0d92-3d49-9fe8-96331b121229 | -8.587 | -45.4687 | 2025-09-07 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 90fe08ac-b0e7-3446-85fb-c28ca43d1b88 | -12.8252 | -47.9932 | 2025-09-07 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 89d9f5a3-ba70-3b26-bf98-01686da82def | -14.2747 | -44.9827 | 2025-09-07 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 8e71d207-7cde-3606-869d-e702fa91599a | -11.264 | -46.4617 | 2025-09-07 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| aafb6f4e-5afe-36c8-a7c1-b304062dfb75 | -11.2636 | -46.4843 | 2025-09-07 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.3 |
| f0ab61de-e383-3a42-9c5f-1874e653db2a | -10.5869 | -48.4772 | 2025-09-07 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 36d1b850-ff7a-3be2-9f3a-edcb64ac1cde | -5.9899 | -44.1528 | 2025-09-07 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 80e37af7-ccbd-336a-9fa3-5df38c232476 | -11.264 | -46.4617 | 2025-09-07 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 5170c85f-dc25-3bbe-95ae-efc5432d7fcf | -11.1575 | -48.3883 | 2025-09-07 12:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 188f3134-6281-3ec9-833e-6035669dfe21 | -11.5669 | -47.7638 | 2025-09-07 12:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d927c103-fbdc-3d4c-b56f-b909bfadd17b | -12.8252 | -47.9932 | 2025-09-07 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 98277fce-26ed-3673-9ffe-38d37d7df6fe | -10.1002 | -48.0936 | 2025-09-07 12:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 9153b02b-7ee8-36b5-9a05-a3a59659fcd2 | -6.2127 | -42.4532 | 2025-09-07 12:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 3c788dfc-8eeb-3781-a21f-5ab8444d3745 | -6.192 | -42.6442 | 2025-09-07 12:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 95d83939-d810-3d07-b821-bf1c286a9474 | -12.9289 | -54.7744 | 2025-09-07 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| fd09c43d-1f82-3e5a-8df0-c8deae46e2d6 | -11.586 | -47.7613 | 2025-09-07 12:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0c43a014-f62f-397b-90fc-f2a6ce38e004 | -12.8248 | -48.0155 | 2025-09-07 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c616facd-02b4-3912-89b4-f39bbad57669 | -12.3016 | -47.2416 | 2025-09-07 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 65492a4d-4643-3a42-abc7-79f492a5880f | -12.948 | -54.7724 | 2025-09-07 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| a04187b3-1c79-3fc5-97d9-a4e5ad17b4dd | -19.4695 | -47.7691 | 2025-09-07 12:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 1762b85a-1469-3525-bd70-ebd843700ecf | -12.948 | -54.7724 | 2025-09-07 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| fc127998-f5f8-3c5b-a08f-8cf7a3579866 | -6.8937 | -45.6061 | 2025-09-07 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 49e0175a-fa59-3d21-90dd-93ae59609dee | -10.1002 | -48.0936 | 2025-09-07 12:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 10566c9a-dda3-39b6-ba79-0bfd153492ab | -6.192 | -42.6442 | 2025-09-07 12:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 9b4144ef-55e9-3c19-967f-208b36fc7e1d | -11.264 | -46.4617 | 2025-09-07 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 504.3 |
| d79c3a4f-3038-3d0d-b8eb-c41a31744b4c | -11.1575 | -48.3883 | 2025-09-07 12:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d275629f-0e87-331f-8f47-86b6dfd68846 | -12.3016 | -47.2416 | 2025-09-07 12:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ff118d74-db20-33fa-8bde-5bc1ea595ff5 | -6.8939 | -45.5835 | 2025-09-07 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c575d8ee-1c00-3720-82f5-c60c4ff6b4ce | -12.7641 | -52.9498 | 2025-09-07 12:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c9abf998-9294-34fa-bb0e-5618d4519519 | -11.586 | -47.7613 | 2025-09-07 12:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0ccfa341-c56c-385c-8d3d-638c97f89a8c | -5.9899 | -44.1528 | 2025-09-07 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 4d2d45a6-b4d4-3990-9306-ffbee376db99 | -12.8252 | -47.9932 | 2025-09-07 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| fe79d8dd-ba09-3d9b-9465-dd9568a29fa4 | -12.8248 | -48.0155 | 2025-09-07 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 47f70e34-0421-3c0e-85c3-f9a7f6e0216d | -11.2636 | -46.4843 | 2025-09-07 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 3db55d16-4a78-3c64-8d00-d64f0b84cdb9 | -19.4898 | -47.7646 | 2025-09-07 12:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8164cc9f-d5ac-33de-a175-508a62cacdf5 | -10.5869 | -48.4772 | 2025-09-07 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1a2ff1ed-8137-36e0-8a73-c0131c663c1e | -11.5669 | -47.7638 | 2025-09-07 12:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| df23ae57-e5f9-33ca-9148-4c751fe4c350 | -11.3548 | -45.5863 | 2025-09-07 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b955b0f0-0bce-3337-b3a8-3a8b1ff65693 | -11.2643 | -46.439 | 2025-09-07 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| da414b17-4d99-3ea4-acc5-7c0d9ae44b7a | -12.8059 | -47.9959 | 2025-09-07 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 573ebc12-9e5b-37b9-949b-5d38fc54b6b6 | -12.3016 | -47.2416 | 2025-09-07 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c68a334f-a025-3987-8fc8-3a3379a51f0a | -12.8252 | -47.9932 | 2025-09-07 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 12f1e3ba-8316-3737-b58b-0b53678632cd | -13.9153 | -54.007 | 2025-09-07 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| cc623a6a-aa6d-3c55-a121-a99b6e001e31 | -12.8055 | -48.0182 | 2025-09-07 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5d176528-8278-3778-bfdf-0a954e8e869f | -12.8059 | -47.9959 | 2025-09-07 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 763208c1-e3d3-31bd-9937-45ce2d76ea45 | -14.4882 | -48.7671 | 2025-09-07 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 223.2 |
| fa045092-7e1d-300b-b005-7c0d1ba4dfab | -12.8248 | -48.0155 | 2025-09-07 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d83aecdb-b924-3c66-b377-306977272ab1 | -6.192 | -42.6442 | 2025-09-07 12:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| bc3ed4f6-5f6d-3b34-a7c6-0c71b47165fd | -6.2108 | -42.6426 | 2025-09-07 12:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 87991e78-fdc0-3978-bc00-4345b2f4d113 | -10.333 | -46.3999 | 2025-09-07 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 05049be9-09d4-30a4-8c05-b5ee4ed681d8 | -13.0542 | -48.0716 | 2025-09-07 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 723670be-f8b0-3add-b118-4de349f6f791 | -5.9711 | -44.1542 | 2025-09-07 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 774016ec-28e4-3bde-a601-1cb815c835b9 | -11.1575 | -48.3883 | 2025-09-07 12:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a79284ec-4b14-3d7e-af45-09557e1bb719 | -10.3334 | -46.3774 | 2025-09-07 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 2885c768-1a2c-3f6c-9f53-a8d70d08dd49 | -8.1421 | -44.8769 | 2025-09-07 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| bb7bad05-3058-39d4-8208-5a1ea95c3a27 | -14.5076 | -48.7641 | 2025-09-07 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 0f697eb9-f35a-3047-9f3b-d14fb16e640b | -11.2643 | -46.439 | 2025-09-07 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e086b0c4-6015-349f-a38b-561396b09be0 | -8.161 | -44.875 | 2025-09-07 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| e0d7c815-911c-328a-8661-fe22f6444692 | -11.2636 | -46.4843 | 2025-09-07 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |


[Clique aqui para ver as próximas entradas](README85.md)
