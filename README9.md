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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da41ab2b-1ca5-3dcc-8913-f810b3acbd6d | -3.8354 | -48.878101 | 2024-10-29 00:28:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e750499-d19d-306b-a54c-fb06cb6f62fc | -3.8378 | -48.888599 | 2024-10-29 00:28:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b441d12-762f-3c08-bc8f-f90b5e96ef7f | -3.8233 | -48.869701 | 2024-10-29 00:28:31 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a718676-4c21-3d3f-b268-ef7872b5e995 | -3.8256 | -48.880299 | 2024-10-29 00:28:31 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdf3e79d-c436-3294-ba3f-95c38851819a | -3.2034 | -46.167 | 2024-10-29 00:28:31 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fff4d5e3-eda1-3a46-86d5-cf2563a59ae7 | -4.0695 | -50.0196 | 2024-10-29 00:28:31 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 228f53aa-87a3-30c3-a466-72046e62ed98 | -4.1058 | -50.5056 | 2024-10-29 00:28:32 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3367e6-c075-32aa-8452-50e838793eac | -4.1088 | -50.519299 | 2024-10-29 00:28:32 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87cb1fa8-ff42-3c50-86e8-62f8536e1445 | -3.3041 | -47.02 | 2024-10-29 00:28:32 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90bbec6e-3493-38a4-84df-6531b5ebf447 | -3.2578 | -46.860699 | 2024-10-29 00:28:32 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0766b7a9-c533-3a98-9824-803eaf5e345b | -3.2596 | -46.868698 | 2024-10-29 00:28:32 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c327ec1-679b-3f80-b085-84f27920bd45 | -3.2614 | -46.876701 | 2024-10-29 00:28:32 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f16fb0-8062-3064-b285-afb4c0f8e93c | -3.3217 | -47.188801 | 2024-10-29 00:28:33 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a91994-3fcc-342a-a99a-a107b1e688d5 | -3.9426 | -49.955299 | 2024-10-29 00:28:33 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45fad775-a3a8-396e-801e-e6f25df2ae05 | -3.1792 | -46.604801 | 2024-10-29 00:28:33 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c26e1499-e1b7-3bd1-a3c5-e9c310e16425 | -3.31 | -47.182701 | 2024-10-29 00:28:33 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab089afd-df63-3d7b-9d8d-dd071f7a09f2 | -3.3119 | -47.191002 | 2024-10-29 00:28:33 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9feb03aa-db64-3f57-858f-c2fec0ad6213 | -3.3138 | -47.199299 | 2024-10-29 00:28:33 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8c31862-35d2-3617-86c4-12337dbfcf7d | -2.8079 | -45.3354 | 2024-10-29 00:28:34 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0edd0f6-88d4-392b-8ce9-974bd369a2c6 | -2.8095 | -45.3424 | 2024-10-29 00:28:34 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f18814e-054c-3e02-a38c-55abc751da0c | -2.788 | -45.9715 | 2024-10-29 00:28:37 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6073a968-a740-333e-8880-e7a05f37d0e7 | -2.7423 | -45.997002 | 2024-10-29 00:28:38 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce894b98-dac7-3c87-8d96-9a823d5d452b | -2.7439 | -46.004299 | 2024-10-29 00:28:38 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3371c4-33d4-3f69-9928-30ac1ab5741b | -3.6114 | -49.847301 | 2024-10-29 00:28:38 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f7e9f4-e701-3f99-a6ec-ed9f678faeb0 | -2.8681 | -46.6408 | 2024-10-29 00:28:38 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec2a6c5-eea8-371b-8d4a-94a24135ce6b | -2.6284 | -46.130299 | 2024-10-29 00:28:40 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4372f130-7d56-3bb9-bec8-61ca6580abc3 | -2.6088 | -46.134701 | 2024-10-29 00:28:40 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d472a4d9-5606-3e9e-8d1b-7971a2d728a5 | -2.6105 | -46.142101 | 2024-10-29 00:28:40 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b584ecf3-2371-3623-ba59-9448b94268ba | -2.7326 | -46.678799 | 2024-10-29 00:28:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d137a02-bb5e-32be-be44-cd611d0450f2 | -2.7344 | -46.6866 | 2024-10-29 00:28:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f885f751-ee0c-3aaf-ad47-a3785a5fdf2c | -2.7228 | -46.681 | 2024-10-29 00:28:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d839c57-b649-3e38-839d-ea21cd3cce87 | -2.7246 | -46.688801 | 2024-10-29 00:28:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23037e1f-f9e7-37c1-a3b3-e434980145bb | -2.7263 | -46.696602 | 2024-10-29 00:28:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c0ea30f-7510-3326-9ecf-6b124d2bbeec | -2.7281 | -46.7043 | 2024-10-29 00:28:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9ce878b-a82c-3379-8127-1a99322e3fa5 | -2.9792 | -48.039398 | 2024-10-29 00:28:41 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d334862-3d30-3562-9c6f-b0fc9abe71ea | -2.9813 | -48.048599 | 2024-10-29 00:28:41 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f083820e-e247-33ea-85f0-72a0af96219d | -2.9833 | -48.057701 | 2024-10-29 00:28:41 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7328eb-68d3-3753-883c-864c21bf5388 | -2.9715 | -48.0508 | 2024-10-29 00:28:41 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4656891-a1f8-3af5-8f7b-d2408a8eab96 | -3.3705 | -50.144501 | 2024-10-29 00:28:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf1990a-136f-3ffb-acf8-d963ef54e37e | -3.358 | -50.134102 | 2024-10-29 00:28:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afa83b87-6aa8-3d63-be64-8e2bbe1cee43 | -3.3608 | -50.146599 | 2024-10-29 00:28:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e64c6b07-01b7-3990-b2ee-cd04e8350538 | -3.3636 | -50.159199 | 2024-10-29 00:28:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10502ab4-2d88-3892-9baa-cd36af0bb1ff | -2.462 | -46.213699 | 2024-10-29 00:28:43 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50550ad0-82dd-3951-950b-c67811a8ccc5 | -2.4637 | -46.2211 | 2024-10-29 00:28:43 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 862dfb1d-341a-3385-9077-3a58166ed5e6 | -3.696 | -51.834801 | 2024-10-29 00:28:43 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65043a0b-2d16-3544-a4eb-01b05c52f9e6 | -2.9486 | -48.540798 | 2024-10-29 00:28:44 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52b0d35-6a66-3fa8-b75e-c4880596de8e | -2.9508 | -48.550499 | 2024-10-29 00:28:44 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8f575bd-2a38-36e3-9030-463b804cdc19 | -2.953 | -48.560299 | 2024-10-29 00:28:44 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de7c0573-6a3d-3115-b40e-39d24a7fa1b5 | -3.3305 | -50.285999 | 2024-10-29 00:28:44 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba211774-fd06-32f8-b9e4-c5762d8bc18b | -3.3334 | -50.298801 | 2024-10-29 00:28:44 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5c03cb1-881c-35c6-b7dd-72fa5c5de66d | -3.3179 | -50.275398 | 2024-10-29 00:28:44 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c600780-651d-3747-aefa-e66cf29977ea | -3.3207 | -50.288101 | 2024-10-29 00:28:44 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 666a5328-010a-3cfd-be0f-7f780a83f8a2 | -3.3236 | -50.300999 | 2024-10-29 00:28:44 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9682db69-400b-3796-bb9e-dc6abead9861 | -2.4001 | -46.258701 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c77b0c07-275b-3886-8030-08f0954431c8 | -2.4018 | -46.266102 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce7c8bb8-f165-3036-a0f9-df392f598e43 | -2.4034 | -46.273499 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 732e452b-2471-32eb-9d6b-ef4d663fbde5 | -2.3903 | -46.260799 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3b3679-867f-3b00-bc17-af6bded9d178 | -2.392 | -46.2682 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bad4c443-5a20-300f-91cd-6cfb1b313acf | -2.3936 | -46.2757 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c7d7797-c4ee-3bc2-b4d3-036399881471 | -3.5652 | -51.475601 | 2024-10-29 00:28:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3502abbe-eabb-3aa3-b7a9-edbcd941b56c | -3.5687 | -51.491199 | 2024-10-29 00:28:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef958cbe-edac-3c72-ab52-80be433b3759 | -2.3805 | -46.263 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a60615f-f883-3096-a73a-67a6083f0a2c | -2.3822 | -46.270401 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3545e0b2-c3df-35cf-b64e-178d5dea4b09 | -2.3838 | -46.277901 | 2024-10-29 00:28:44 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7425c42-b7b1-3a5a-bdf4-781919a4c004 | -3.2212 | -50.163799 | 2024-10-29 00:28:45 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1290b9cb-b98f-3889-ab8e-a44f7ca2bf7d | -2.4261 | -46.689701 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0bf2f77-3e7a-37b7-8645-6d94a38582ba | -2.4279 | -46.697498 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dded7575-1b36-3ca7-bde3-f56726196925 | -2.4297 | -46.7052 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 089c88cb-0b74-3abe-b000-ce38fa9c6b21 | -2.4314 | -46.712898 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 394c10a4-9629-31fa-8f7e-ee4ceeee55ed | -2.3832 | -46.546398 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41c3fda2-2079-3262-b4c1-4b10b068c741 | -2.385 | -46.554001 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5dcfc18-059a-3907-ae4d-1bb012fa2c8e | -2.4163 | -46.691898 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d233ba-65b2-3e6f-990f-4eb3fada4bc0 | -2.4181 | -46.699699 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0acb080-3ec3-3617-ae37-b254961d36fa | -2.4199 | -46.707401 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96cd1e04-94e3-3af5-96c6-4521fd7d62b4 | -2.4216 | -46.715099 | 2024-10-29 00:28:45 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a2718c-6ef5-3b43-9336-a9db65a88459 | -2.4118 | -46.7173 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c63ce2c-b769-3a83-a2a5-e3095d3efc14 | -2.4136 | -46.724998 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b607a93f-0386-3220-815d-d2092caadf48 | -2.5553 | -47.3489 | 2024-10-29 00:28:46 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57cb823f-e56d-306f-a01d-f750eb0fa7d5 | -2.3429 | -46.4599 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31bce4cd-3c32-3337-883a-3d981f1412ef | -2.3446 | -46.4674 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3749543f-cc3a-3b57-8ee3-d1c3bb6c5470 | -2.3301 | -46.494499 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6360b25d-e351-3e4a-aa8a-5c724e4a176d | -2.3318 | -46.501999 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2eb7043-e7f9-3643-8937-f4bfebac7587 | -2.3336 | -46.509602 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89f0acf0-9d56-30cb-aa0c-66fc69f44769 | -2.3353 | -46.5172 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2f801f-7e4f-34de-8ae7-679f1376259c | -3.2764 | -50.6847 | 2024-10-29 00:28:46 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f23af07-cd97-34f2-8ae4-9f56daee47eb | -2.3203 | -46.496601 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb25260-6b10-36e6-847f-11148bca1ff2 | -2.322 | -46.504101 | 2024-10-29 00:28:46 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c273a41d-974c-3c84-b393-de4d9cdece08 | -2.5331 | -47.4324 | 2024-10-29 00:28:46 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1751bbfb-06b5-3d6a-bb22-b62338acd217 | -2.535 | -47.4408 | 2024-10-29 00:28:46 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1ee3101-bf4a-308e-8c53-8538d9979931 | -2.5369 | -47.4491 | 2024-10-29 00:28:46 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac02a65-9423-3c0c-8fcf-3f4d525cd6c2 | -2.333 | -46.5975 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc90f865-f615-363e-8665-1f25da9ac435 | -2.3348 | -46.605202 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 923f9c4f-3c6a-3418-8e5e-327b355d6fbf | -2.34 | -46.628101 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75bec803-2a39-3f54-93ef-f7eb6826212e | -2.3417 | -46.635799 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc83f5e-90c4-3ab6-9e60-af08e7f25629 | -2.3435 | -46.643398 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d977c57f-8172-3b24-95db-4777dacf2ef7 | -2.3452 | -46.6511 | 2024-10-29 00:28:46 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5028127c-a810-398d-ac6e-548d9099931c | -2.5233 | -47.434601 | 2024-10-29 00:28:46 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2048595-eadd-3ada-9249-bd7f4fe09101 | -2.5252 | -47.443001 | 2024-10-29 00:28:46 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31dbd7e3-3ccf-3dbd-81a2-b3b64dd1bf48 | -2.5271 | -47.451302 | 2024-10-29 00:28:46 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe102bf0-219e-3a6a-8323-51b53799c244 | -2.9941 | -49.517502 | 2024-10-29 00:28:46 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
