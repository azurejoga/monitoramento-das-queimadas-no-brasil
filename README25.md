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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80fd1e35-10ee-3f90-9a98-5f9d93e97cd0 | -2.27863 | -50.68102 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 424330c5-6a62-37e0-8738-5981068faf71 | -4.58397 | -43.97306 | 2024-11-13 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d621a0e9-89f2-3aae-a905-f16b942729a7 | -2.7904 | -54.03475 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d84bf3d-e88a-34a7-94e5-27ef52d167ea | 1.13932 | -60.59654 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d8f5047-5162-3d13-880b-d2e2ae4e9eea | -2.8244 | -51.95116 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9691cdc-3ba6-3009-b24d-fa6bc4632170 | -1.08246 | -53.6438 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fb00800-aa96-3532-9833-3b2af94b98d3 | -3.0848 | -53.26142 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6138f1c6-c68c-39d7-8b0b-da9956d15a59 | -3.0818 | -50.32518 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a354aeca-ec72-3431-83a0-529370e29434 | -3.57952 | -54.64511 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 434dded8-fd0e-34c2-8352-872c18a86d12 | -3.85314 | -52.38052 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5ef9032-0152-3e2e-863a-e9ba61f53b8d | -2.45606 | -53.93295 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea9f2c44-db22-3af0-b5b5-eee211928bb7 | -2.88295 | -51.79613 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d935c82a-0e46-3a69-a8aa-65e2c7707fb4 | -1.80072 | -52.04829 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ca58f82-4dc3-3b03-a310-2bf359809aec | -2.72225 | -45.29459 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b09765d4-0f02-3a48-88d3-d271f0cd2494 | -2.82327 | -54.0017 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04483481-a347-3035-9679-d9b0469a109f | 0.2749 | -50.90931 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ad63d33-1252-3ca4-bcc7-264a4d45b1ba | -3.15243 | -53.2401 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 009233c7-0792-312d-b59c-2b96b0385616 | -3.14815 | -45.97519 | 2024-11-13 04:57:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a874c882-6b5f-3e2c-84c2-9a4c317b218a | -2.81861 | -54.09621 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d508b32-978c-31ab-a6d9-083aff62be54 | -1.21059 | -51.76839 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa913b54-38ed-32c2-a805-2f0a110e2a49 | -1.64605 | -52.53822 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e761962-e3fe-3739-acff-9891ab628d7f | -2.80739 | -54.01268 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb2bccd-5173-3899-9044-5204af727702 | -1.65933 | -52.54027 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e869db30-0b0f-3a37-a67b-d76c1bc15645 | -2.59026 | -48.31295 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 742ff4b3-2c51-33f8-a7f6-2f41be896e31 | -1.57865 | -50.45014 | 2024-11-13 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c609b25-2774-32c0-a7ef-f66a8988a2cb | -2.96747 | -53.86216 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d28dc18c-2fde-3707-b44d-389143947162 | -1.17687 | -51.94896 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 521ed9d9-6c12-3bb2-8887-61bf19a50d6d | -2.61417 | -48.21212 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3da5e71a-ad5f-33ec-8b4f-7723e3f40777 | -2.59717 | -56.49771 | 2024-11-13 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e299ce30-506a-3511-a38e-96ddbfd85738 | -2.59644 | -48.19053 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46c0273c-2bef-3353-b4da-01c2444efc80 | -2.41057 | -48.93191 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc972fcc-ae56-3003-8e48-0829da1efb67 | -2.46064 | -47.83068 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3e2a117-d14b-319c-9068-7cd6eb097cd2 | -3.44842 | -54.63534 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d74b07f-cda7-3f30-ac6e-30ed1829c882 | -2.78264 | -50.29699 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc418497-3a54-3005-aadb-76ee5ccd8a91 | -2.61785 | -50.68897 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d34f4d66-91ec-3a74-a6b6-97061353b9f9 | -3.70823 | -51.8363 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c138a1d-0707-3027-8405-9d12e0a0be4d | -3.29684 | -51.59276 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f448737-5fd1-38ba-bbdb-024ca4f8bf62 | -3.25816 | -50.39345 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8ecc2663-7eb7-394a-97e5-ce3d0a0ba3ac | -2.12174 | -50.68789 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ca95917-bda2-3dfa-aa7f-eaa2fd482153 | -1.22683 | -51.75255 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e10efa30-0fac-347d-bc08-a302d34b163d | -3.25024 | -50.39657 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70fa1277-6741-33db-8c12-3714d6fc216e | -3.52325 | -54.4832 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd172204-e23c-3b90-a70c-a5fea07f49f1 | -3.05793 | -50.33117 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b67241a5-8d3d-3ee3-b0a6-f36e69fc3725 | -2.12236 | -50.68391 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88202d46-2fb8-3655-ba33-a13a49e18158 | -2.24669 | -53.74923 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8aca13b1-c4f1-3b31-9789-f30a7be119a9 | -2.90338 | -51.82174 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bd3d996-c5cd-31c9-bfd6-1d78cd5e7729 | -2.28687 | -47.92291 | 2024-11-13 04:57:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f0bd28-f83b-3ac4-9e4d-b4e614c1ac70 | -3.19281 | -53.39772 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4f6c4b8-47b8-3531-b70b-2adef4fc9d99 | -1.41617 | -51.11731 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 816dcde0-6b93-34f6-a7d4-3d24423e2648 | -2.14414 | -46.40564 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c01c2a22-4a81-3221-ba73-b0ec7a559391 | -2.15043 | -53.49487 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba2beffe-24cd-3274-8166-2831dedde409 | -4.37492 | -48.08095 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3425888d-68eb-30f3-8baa-fe2564f48bec | -2.66056 | -46.81595 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcd4e1d6-d11c-3611-b2b8-4273eaa2280a | -3.41123 | -50.37501 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a884663e-5202-3d47-8bea-bbe23fc95b63 | -1.37528 | -51.40021 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9005505c-587c-38f1-8666-502105521064 | -2.71421 | -47.72923 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4d8ae30-c9c6-3454-b694-e87b1272441b | -2.98202 | -51.24356 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 421c66d2-9eb2-3d6a-b0d7-a4c8bb7cf13e | -4.51832 | -48.92854 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 290a164f-9ae0-3932-85f0-415466357b0f | -3.24936 | -50.30543 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 236431d5-c2dd-3699-8bf8-4da9f5558cf6 | -4.23104 | -50.69825 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a41c23a-9e82-3bad-a69b-cfeac0f4221b | -2.95531 | -53.71953 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 108de573-8289-3f23-98be-1cc30776b0da | -3.273 | -48.75619 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebd15bdc-544c-36e5-b047-f8c24a841882 | -1.62111 | -53.26421 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5332cc6d-dd56-3146-be2e-b05ce152f13e | -2.12631 | -52.26902 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4b39dda-e5a4-3a9f-b9b4-e0d3712ddec6 | -0.03733 | -50.75372 | 2024-11-13 04:57:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 341d2356-1d3c-33ba-850c-dca940981532 | -3.10673 | -53.71136 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae128ff-5f62-3a36-980a-174f6a4d2eef | -2.59758 | -48.18305 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2208f51-7888-3f02-b5c0-a21cc6165dee | -2.28778 | -48.1936 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cd8d7f9-a85a-330d-a042-78f7dc1105ba | -3.66204 | -54.66142 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ecab8c2-5385-3cc3-85e0-7b9bd97636af | -3.2444 | -50.31342 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 028caf5f-b857-3de3-9273-0d54efe611aa | -1.2889 | -52.47226 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11912493-117b-32c7-84cf-7b277bb23a2e | -3.01799 | -51.24128 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98306467-7918-3a72-ac9d-2b4682554f4e | -5.35713 | -43.53065 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e06fa08c-8843-3003-8077-c42fac916560 | 0.68358 | -50.49421 | 2024-11-13 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f3b2c3-b188-3382-99fe-5d59a63d0e62 | -3.62535 | -54.11325 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 540a8cea-e7f1-3096-ae4e-07ca29625925 | 3.59759 | -59.94369 | 2024-11-13 04:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2abda6bc-6dde-3942-8e82-49ce7796e0bf | -2.45991 | -53.93002 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e69104-125d-305c-943e-f93525218517 | -2.90571 | -48.76411 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 800402e7-4e24-3935-8ae1-fad59c628f50 | -5.92127 | -42.96816 | 2024-11-13 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aebdb2e0-4630-3bd5-a251-fd81bbdfb9d1 | -4.04437 | -48.095 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4c6be63-5d99-3712-bf03-106a8e799a4d | -1.39351 | -51.44386 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66b4afe8-5b42-35f8-af44-f5258dd204dc | -4.54315 | -50.24036 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39950089-9b9e-3dc6-ba4b-12d556847028 | -3.85685 | -52.21158 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ad310d-43f9-320d-8e9c-eaecff831fbe | -1.17539 | -53.74633 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51ae6c61-c5bd-3abe-ae18-83a715ebff5c | -2.12455 | -53.24491 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b482bb10-2acb-39bb-bcd2-9116e198bdc0 | -2.38678 | -50.49969 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 641b1b56-a311-365a-b586-3b9e5587f4d1 | -5.35269 | -43.53072 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bcea42ac-0bfd-313d-bc3c-6b872d8f7b7e | -2.87853 | -54.2115 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbdd941c-06e1-332b-8b29-dbfa578e00b6 | -2.96417 | -53.86164 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ba51826-b094-34a7-a511-7cc0a9b704bb | -2.37991 | -54.28938 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e857758-83a7-37c0-9373-880e6a484c7d | -0.03722 | -50.77688 | 2024-11-13 04:57:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3059091a-af17-3ef2-90bc-dbbb64ab82b2 | -3.08927 | -53.2762 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92947936-25db-3c9e-9962-cb275760fc52 | -1.51037 | -51.92726 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b628bbd5-33ef-3a48-b204-98a98659d506 | -2.99379 | -54.12687 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b3aa0b0-43bb-3218-a194-b82fa62197a6 | -1.80033 | -51.10433 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44f605b6-f7e7-34cf-a36f-c3a4a0ef7508 | -3.85505 | -51.90805 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0176567-be9a-31a9-b587-9cb2938bf346 | -2.24413 | -53.65743 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebff8f22-28fb-3780-8160-800048296fc6 | -4.47305 | -49.62968 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d5afce-5339-3150-9865-559585ddf7bb | -1.33549 | -51.40913 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c1060fd-703f-3a5d-9bf6-ad1bd1883f42 | -3.07453 | -50.32405 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
