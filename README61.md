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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76ad1c41-1812-34d8-ab44-dbd694206da5 | -8.35756 | -70.30811 | 2025-09-05 06:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 941342cb-b1c4-3a3b-aff2-a2befe501e06 | -8.3572 | -70.30643 | 2025-09-05 06:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d05371ae-7885-3db1-95eb-9b2f03a444b8 | -8.35201 | -70.30739 | 2025-09-05 06:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de0fe94f-fad2-361b-acc9-dbbec67340c2 | -8.75957 | -69.33997 | 2025-09-05 06:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fea9aeb-1bd6-3968-bea2-16a1f4ef5085 | -8.5258 | -70.73676 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba82fc29-9557-3b37-9d09-3af41235d94c | -7.9939 | -71.00486 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 189c3af4-93ec-37e6-9138-b6a992e83c85 | -7.57188 | -69.89626 | 2025-09-05 06:37:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d5aa18f-18ae-3def-9de0-88d227598e8d | -10.9856 | -46.0007 | 2025-09-05 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a0db4ed7-95fb-3887-b4d9-6ed73e48f4cd | -9.22905 | -71.89635 | 2025-09-05 06:40:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a5d3efe-ff2c-3f98-96aa-45c96e4ca95c | -16.6048 | -50.1925 | 2025-09-05 06:50:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a91e0403-97b2-37d7-82ea-890375e02c2d | -16.6245 | -50.1892 | 2025-09-05 06:50:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| db5b839d-0cfe-3c92-9303-6e49c6d2aad3 | -23.7658 | -51.6169 | 2025-09-05 07:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 116.0 |
| 38067b25-8de0-3d53-be35-bb0eeab961a2 | -12.9859 | -54.7891 | 2025-09-05 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| eaf1b3eb-58bb-3528-b861-4ca33f0e6617 | -12.9477 | -54.793 | 2025-09-05 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| c7b437b6-0249-39ee-98f2-df8d5c77e58e | -12.9665 | -54.8116 | 2025-09-05 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| c7cc8c48-4eb3-3a86-9fbb-7ff250e9204a | -16.6245 | -50.1892 | 2025-09-05 07:00:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d52f234d-a16a-3053-8bae-4ba637aae563 | -23.7651 | -51.6399 | 2025-09-05 07:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 8de9b7b5-4f2c-3a90-b30e-6e7984e8d03f | -12.9856 | -54.8096 | 2025-09-05 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| dcbafdad-4f62-36fd-b7b0-0c5c58b0ac30 | -12.9474 | -54.8135 | 2025-09-05 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e972706e-ddb3-317a-8f59-db77a9d39158 | -12.9668 | -54.791 | 2025-09-05 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 208.4 |
| 17e2baa0-800c-3821-a3af-778e1a230e65 | -23.7658 | -51.6169 | 2025-09-05 07:10:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 70c146d0-2433-3c7c-96e6-0016dab1b3ac | -12.9856 | -54.8096 | 2025-09-05 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 60128ef3-45af-3f0d-8790-6557a58d37d7 | -12.9665 | -54.8116 | 2025-09-05 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 37f01415-d81a-3113-a0d3-93a1dc1c43bc | -12.9477 | -54.793 | 2025-09-05 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 21e62bb6-0737-3572-9c2c-00092b2b05c2 | -12.9859 | -54.7891 | 2025-09-05 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 6be5e0fc-cc9e-3ea8-a05b-53e19e1dbb8f | -12.9668 | -54.791 | 2025-09-05 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 1e8ba6f3-d214-3869-a2f4-dfedf3b14e09 | -12.9477 | -54.793 | 2025-09-05 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ed6601a7-b741-3fc0-a4f0-8626211290ef | -12.9859 | -54.7891 | 2025-09-05 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 64cabea0-485d-3e4d-97a9-5b486b06f0e0 | -12.9668 | -54.791 | 2025-09-05 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 52509a40-b70e-35f8-b715-c1ee5f5aae79 | -12.9665 | -54.8116 | 2025-09-05 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 54a9a81a-5513-30ba-8bdf-aa2362b34b95 | -12.9856 | -54.8096 | 2025-09-05 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9f812053-267b-370b-b2f8-fdacc2ff27fb | -12.9665 | -54.8116 | 2025-09-05 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4a183606-d0a0-3387-8b80-d0fcb23f3d40 | -12.9856 | -54.8096 | 2025-09-05 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2dfc5316-2ac5-36a1-a80b-7f5ce836ae32 | -12.9668 | -54.791 | 2025-09-05 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 0a74d253-0971-3d5d-8d80-de2bd32d32fd | -12.9477 | -54.793 | 2025-09-05 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 18db7957-bc08-3b2e-8c24-4cb6bf345efd | -12.9859 | -54.7891 | 2025-09-05 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c0a09d02-d8c5-348d-aa13-30d79cd7e9f5 | -12.9668 | -54.791 | 2025-09-05 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 392c6d8d-33e3-38a0-a08d-0182ae4ccaba | -12.9477 | -54.793 | 2025-09-05 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 06ae82d9-bb0d-3e72-b46e-9b02c4dc83e6 | -12.9665 | -54.8116 | 2025-09-05 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| d8a911eb-114c-3f5b-bd73-c8b6518d3bf9 | -8.9034 | -45.7973 | 2025-09-05 07:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2c89211b-ffba-3b14-859d-f5fcf37eb3b4 | -15.0644 | -50.0651 | 2025-09-05 07:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 58eae304-6aee-34f8-88a6-d3452a619be0 | -12.9856 | -54.8096 | 2025-09-05 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 24640904-b65b-3491-a937-204a1afd83cc | -12.9856 | -54.8096 | 2025-09-05 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a82ab927-9062-3ccd-941b-bbdad097dfd7 | -12.9665 | -54.8116 | 2025-09-05 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e964fe43-ce7e-30a0-84e5-0ab9afce020a | -12.9477 | -54.793 | 2025-09-05 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5487e2ff-41e0-35a6-a23a-e36ddd2a9688 | -12.9668 | -54.791 | 2025-09-05 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| bb868d83-4036-3e46-adca-7d2232333f00 | -12.9856 | -54.8096 | 2025-09-05 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 46603353-7936-347b-bf10-60bc2e63e96b | -6.5856 | -44.564 | 2025-09-05 08:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 66acf18b-a311-30f1-ac26-0b1dda5c9f6e | -6.6044 | -44.5624 | 2025-09-05 08:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 14353225-5b14-3a44-ba09-1e1ce1d31ba9 | -12.9477 | -54.793 | 2025-09-05 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 85d3bf6e-4c4d-31d7-b7d0-d79ff627d160 | -12.9665 | -54.8116 | 2025-09-05 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 480edee8-7ffc-35a2-ae0d-b7563501044e | -12.9668 | -54.791 | 2025-09-05 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 340fa5d3-2da3-3ad8-b116-0f1c891688e5 | -12.9856 | -54.8096 | 2025-09-05 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6efb93e3-0448-3971-b21d-51365f8d4744 | -6.5856 | -44.564 | 2025-09-05 08:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 61b15dea-3e1e-3182-bc75-ea4c61a7c7b8 | -12.9668 | -54.791 | 2025-09-05 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| eb83c2fa-906d-3abe-a7d1-31eaf1969cc6 | -12.9477 | -54.793 | 2025-09-05 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 663a01c0-d109-317f-a491-76dc0ce22990 | -12.9665 | -54.8116 | 2025-09-05 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f9f18f6e-9e66-331f-83ca-bc27adb918a2 | -15.1378 | -52.3826 | 2025-09-05 08:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 34a0225d-7dde-30bb-9872-46e2e0353ab1 | -6.6044 | -44.5624 | 2025-09-05 08:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c84eb580-4852-3ab6-965f-bb2e1bdcc315 | -6.6044 | -44.5624 | 2025-09-05 08:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e9bd6c4d-36e8-3ada-be80-df465f3b757f | -15.1378 | -52.3826 | 2025-09-05 08:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 811a5293-ba61-3d7d-8792-674a9e8db954 | -12.9668 | -54.791 | 2025-09-05 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 3d9b604d-c59f-3d36-9da0-19cdde19e60e | -12.9477 | -54.793 | 2025-09-05 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 37b37cbc-a4e0-3ea5-a623-676763cde098 | -15.4077 | -55.9622 | 2025-09-05 08:20:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 26501f0c-41b1-34da-bff2-3d297135ccb0 | -12.9856 | -54.8096 | 2025-09-05 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 64ec9d4e-f05e-37e5-ac1a-9d5254046f04 | -12.9665 | -54.8116 | 2025-09-05 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e4e10d60-7a39-3ece-a41f-04d9d6ae5874 | -15.1378 | -52.3826 | 2025-09-05 08:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| efda214c-3560-352c-ae35-804c515a347d | -12.9477 | -54.793 | 2025-09-05 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 55fd2ea5-6fe5-35ae-b874-2f41c1c70811 | -12.9668 | -54.791 | 2025-09-05 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 5b8845df-406c-3490-ab1b-cbb2f9fdfa26 | -12.9856 | -54.8096 | 2025-09-05 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0facf420-a743-3c13-a131-c74b5dd53265 | -15.4077 | -55.9622 | 2025-09-05 08:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c1f4f880-930f-3e63-bc30-107dfed5ead3 | -12.9665 | -54.8116 | 2025-09-05 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f00c0241-3e43-324b-b11d-0898bf3793a4 | -12.9477 | -54.793 | 2025-09-05 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7bfcd6da-96a9-3165-9a9f-d403629b3b68 | -12.9668 | -54.791 | 2025-09-05 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 7d928746-bede-3d90-ad2f-343662c5be91 | -12.9665 | -54.8116 | 2025-09-05 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b16f1b55-4b93-3b09-8b9e-815ad661f17c | -12.9856 | -54.8096 | 2025-09-05 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 16631c24-5d44-3dc8-b304-3f26984a4f36 | -12.9665 | -54.8116 | 2025-09-05 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 03ec76a4-2aa1-3f2a-905e-7ba81bd58102 | -12.9668 | -54.791 | 2025-09-05 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 4fb04592-b78d-3778-9bb4-48168fab889d | -12.9665 | -54.8116 | 2025-09-05 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ef939d04-fa9f-3a30-95ed-26f9a030a230 | -12.9668 | -54.791 | 2025-09-05 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| afd55b63-bd4a-3306-9158-4185bba747a9 | -7.8967 | -44.9244 | 2025-09-05 10:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 894d193f-83e6-3d2f-8e40-9a3a0a9188e8 | -6.1519 | -44.8501 | 2025-09-05 10:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d932bf1b-2552-3e14-a5c3-2feed4072fc1 | -6.1519 | -44.8501 | 2025-09-05 10:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 6feb1f4d-ed5e-35a6-a310-77203e15cb04 | -15.7111 | -46.2281 | 2025-09-05 11:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 1021b215-d12b-3ed6-9dbe-85434db81abb | -6.1519 | -44.8501 | 2025-09-05 11:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 257.5 |
| 2e01072f-57d1-3245-8bba-2d03e5952095 | -6.1519 | -44.8501 | 2025-09-05 11:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 07891290-333a-37a5-b334-faa52d0473cd | -6.02925 | -36.53738 | 2025-09-05 11:17:00 | TERRA_M-M | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7f3e84c0-bc30-38a2-b278-4e4ed052396b | -4.9818 | -36.92249 | 2025-09-05 11:17:00 | TERRA_M-M | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 16.8 |
| c22f111b-4923-3b39-81cc-01bcb5160dd9 | -15.81662 | -43.48163 | 2025-09-05 11:19:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 3e9928f5-e145-3024-908c-14f09f31773d | -12.30799 | -42.6087 | 2025-09-05 11:19:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 6abb6c37-a4b5-3e0e-9b2a-a18486c98fa6 | -6.1519 | -44.8501 | 2025-09-05 11:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 8d2e185a-307d-3a9a-9aad-a8403aae1ab5 | -6.1519 | -44.8501 | 2025-09-05 11:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 29b2e90b-42ea-3019-aac6-c2bf55822fdd | -5.608 | -42.8798 | 2025-09-05 11:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| cf7fddd2-e22e-3cf1-9a3b-3146a0ed775a | -6.1519 | -44.8501 | 2025-09-05 11:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f09c7b39-747c-3084-955d-d951a9acb37a | -6.1519 | -44.8501 | 2025-09-05 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c7350120-3696-3f82-b412-56640763e478 | -9.0762 | -47.0113 | 2025-09-05 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b7dfb716-b172-3890-b109-751c45c1eb6e | -10.9856 | -46.0007 | 2025-09-05 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| c5dbfc7c-83ae-3cd2-9468-23ea6c53ddcb | -12.9668 | -54.791 | 2025-09-05 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4a946d6a-b7fd-3411-80db-7ce8cfa2902d | -5.608 | -42.8798 | 2025-09-05 11:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 1bc42129-308b-3e31-83ab-3482d22d49fb | -13.884 | -47.9929 | 2025-09-05 11:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |


[Clique aqui para ver as próximas entradas](README62.md)
