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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1625de9f-ba10-3d98-95e6-ce187c992f2d | -3.46599 | -53.29161 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f5b9bd9-7e2d-383e-937b-5b1fcdeca31a | -2.83275 | -46.66074 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcda5370-30cb-39e0-bd70-879d81ad3226 | -3.23274 | -49.12812 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2708209b-e1ac-37b7-a9fb-19e40814a62f | -3.37623 | -53.32807 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 130cfdd4-1f05-30a2-8ff2-e4a6f9c9bdce | -3.67218 | -50.10315 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c8f22d8-efb9-3a1e-b6cb-b0d9377eebd7 | -1.11798 | -52.39404 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fc70513-60d4-36be-acac-632bc2169625 | -1.76702 | -50.74261 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19564a16-c8b3-31dd-af64-822f849f0e24 | -3.57619 | -45.21325 | 2024-11-18 05:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b25645ba-5218-3022-9ecc-b256d85a2ed9 | -3.06602 | -54.40358 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 048e74aa-4dcb-3099-8009-04b12c258590 | -2.60578 | -51.79511 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5ad7a243-3bf0-3582-937a-7b227b9ebe33 | -1.98442 | -53.13844 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e7f96bd-8ae4-3f43-90f0-41dc30ad225f | -3.56231 | -50.25638 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1e78c4f-c423-391c-8c59-aac4600d5aa6 | 0.2941 | -50.85323 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32a06ef9-5457-367a-b6c1-15065671b26f | -3.37681 | -53.32437 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d759276-02ab-3d26-bcae-1da1ae72727b | -1.21571 | -51.79202 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4955d699-4e0f-3f7b-b742-86858ad53bdd | -4.11042 | -51.04965 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a64c1a-a492-36cc-bd6f-8ec92412e32d | -3.7989 | -51.97706 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3317b72a-82de-33f4-ac29-79fe5f84b555 | -2.628 | -54.26764 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbdc56b8-33d5-3156-a933-8c8221d6845c | -0.12623 | -51.61863 | 2024-11-18 05:03:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 685712cf-fbf7-36b3-879f-90300fdc0050 | -3.17466 | -46.60104 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6c55e28-fd03-3bf1-bdd6-13bb9c8e947b | -3.39234 | -53.26963 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67c69745-df33-3ff6-91e4-8ef0bc56b285 | -1.06863 | -52.39028 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 015556cc-07a8-3729-b841-b46d124ea598 | -1.62 | -52.6164 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c711bd5-dff4-3c6b-8ef1-9f8494b16c6b | -2.9752 | -53.85202 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fab4946-6713-3845-af96-f80935b3b5df | -1.41351 | -52.05517 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e44da2dc-f6a0-3561-a845-df501ce1f40d | -3.37299 | -54.81327 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9570edf-a595-3be6-9eed-b42ca505dad3 | -2.927 | -54.33524 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282586e1-f364-3966-aedb-adbe3e9b3d22 | -2.7807 | -51.75348 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf6a1ee1-4ec5-384d-8433-94eda6943da0 | -1.29927 | -51.74034 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 7ee0239f-0547-32fc-a2c2-dbaec8cbb70c | -3.34711 | -53.31222 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d4ae2d6-f484-34ec-8d7b-45a61a2a91e1 | -2.85404 | -53.97555 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb7cfa5-9287-3371-9abd-fc5925b26fcd | -2.59566 | -48.30717 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a76eb799-6486-3708-91f7-7b0c8fbdeb33 | 0.79711 | -50.22336 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25017fa2-9437-3c82-9078-500fa92f82bb | -4.27012 | -50.6775 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27775e5b-ffb3-386d-a05a-6bcfe1268aa9 | -1.21565 | -55.82075 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51f338b3-db98-3bc0-9a1a-f8275d4e485f | -3.08772 | -54.6591 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18b3a077-f07a-3f4d-923e-345601747272 | -3.06465 | -53.27784 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 325102d5-ad6b-395f-a012-f37c0e40a619 | -2.28791 | -53.62983 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1a15b28-087c-3d25-a9b5-2426f81a47e5 | -1.7574 | -45.69036 | 2024-11-18 05:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20fcf711-f18c-379b-9e78-561c37667134 | -3.4328 | -53.32473 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf067ca7-11d3-3915-ac65-51a65e12543e | -3.44992 | -53.46361 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1761c5f-1b41-3d22-8e5a-36f799f1f15a | -3.06107 | -54.41355 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4848567-8f55-3d23-890f-797f7a5922a9 | -3.34425 | -53.30799 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb18b0b2-be20-33b5-83da-cfc742bd6927 | -2.52586 | -54.88172 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| acafbf74-47ec-3174-9993-e3a6d4908e02 | -3.45612 | -53.53616 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141d8827-1916-31d2-857a-5224d76997cb | 0.29039 | -50.8538 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7428facf-97bb-3a2b-b1c4-27e13727134d | -3.38593 | -52.37498 | 2024-11-18 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97c95965-ab6b-318f-8975-b5bfac47c553 | -1.43851 | -53.38263 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c7de6e09-1176-3e0e-8b69-826b190fd0aa | -3.56583 | -50.2606 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2150e77-e4d7-30c7-8f1c-0af9c791788a | -2.58633 | -51.72675 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cff2a80-31ea-3a01-a3ab-170569a85cba | -0.93035 | -51.63652 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31f5b1e0-d4d8-3e6b-9bed-57ceef5e2c5d | -2.83903 | -54.00583 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38d35b98-da7b-3553-a06d-0cbcd3023b70 | -4.27443 | -50.59322 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 42295e6d-4bca-3465-86c1-03c45018d393 | -2.68332 | -46.18421 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75d471a6-a123-3ea1-97ca-91964768dcde | -3.1858 | -53.24249 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 006cab00-8654-395d-aa8e-6b5b88c45a33 | -3.52861 | -50.25565 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e818801b-5216-3e1c-abe8-7c3ab32fea4f | -2.68239 | -52.98373 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 206db288-382d-3067-9619-7c760f624015 | -3.66186 | -50.20206 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5909b896-f820-30d6-9492-023cc60d5518 | -2.15702 | -50.7069 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0a19e7f-592f-3b64-9b1d-35da07c51c60 | -1.13396 | -54.16422 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 161408eb-6c65-3f0f-aa11-15d70b30db2c | -1.20391 | -51.77343 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 512fb41d-1c2e-3a17-9e8e-9d5dc4fc8d7a | -1.29991 | -51.7362 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 1e7d8d20-52f5-39c9-b83f-47221821bb38 | -3.51817 | -49.93734 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 065d9a0a-6f6c-3c8d-abc8-1c14f2d2ecce | -1.30223 | -51.74503 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b17fa817-fb31-3df9-97c9-df96502481bb | -1.20981 | -51.78272 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02aebd32-46fa-3495-a538-658a1ef7632b | -3.30027 | -45.6761 | 2024-11-18 05:03:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ee2a9c7-fc4b-376d-9863-f4a04cac022f | -1.30583 | -51.74558 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 8b21e958-6e72-3ace-821a-737492bd1193 | -1.39476 | -51.99129 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5f533447-3e55-3753-8c1b-f3b22a5e6e24 | -1.90119 | -46.45099 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b77e0181-87cb-3b4a-8add-4d14f486a2fc | -1.68814 | -55.08104 | 2024-11-18 05:03:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 666f34c9-2190-3d6d-94e6-1632d695a268 | -3.37738 | -53.32066 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf48d068-a096-34fd-b048-13066b032985 | 0.97252 | -51.13826 | 2024-11-18 05:03:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c1b6271-3506-3ebb-b990-8cb259df4ddc | -2.60975 | -54.53844 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a368150f-d6d6-3aee-b5d2-c09153289d95 | -1.15885 | -52.0396 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ec54b9-faf7-3eaf-ad4b-87e1a2dfe870 | -3.58753 | -50.52536 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 107d4d11-0cf4-3ba7-a78f-a27952ca1a5b | -2.64131 | -53.98228 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 326d1737-3e3a-39ba-985c-545380382cf9 | -3.51513 | -50.2353 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e98bcafa-3c73-30d6-bb37-eab13fdffdbf | -3.30718 | -53.36686 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 70165f29-267c-3d74-a9e7-c5feb14a4e2a | -1.28723 | -51.95969 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90a55ac9-7265-304f-b042-6f2b805f1630 | -2.19858 | -53.66031 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1beb8f6f-4ca7-3d18-8c5c-2cb43d655355 | -1.70429 | -45.82726 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2bddca59-d53c-310e-8526-d256a9d960b3 | -1.27315 | -54.66827 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70a9a184-a754-3a21-88b0-b3a58d1ef684 | -3.0494 | -54.40102 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbf30187-2645-3723-be02-5f7f5d2523b6 | -3.18662 | -53.23873 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b831ebf9-0e28-3590-aebc-328e28ad634f | 0.8243 | -51.2262 | 2024-11-18 05:03:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c2707fe-81ad-3673-bb0f-edfaede98c10 | -4.78854 | -46.50581 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 4839ed4b-312a-3653-b4e4-4807413d9890 | -2.75103 | -54.02117 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| add65cd1-3db4-30a3-b5e8-f1b0e25b86ed | -2.93982 | -48.32813 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63ce8ddb-76b9-32f8-9060-28ae9abcbae1 | -3.53626 | -50.40429 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7c88d7c-d618-39b5-b07b-f6f9b26c4e6a | -1.38022 | -51.55865 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de918736-be3d-36bc-afa6-105d8fd5d9ab | -2.63357 | -54.27564 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e48f6d4d-6522-3a4d-ab46-c89f7a777521 | -3.40819 | -53.302 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34428697-f52d-3e6e-b061-6c8dd24f5d3b | -1.7038 | -45.83057 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5469a50-253f-3a4b-9ae9-9651ed75df27 | -2.17455 | -46.39346 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9ec6464-a791-3baf-8853-3c338220e5d4 | -3.10245 | -53.09915 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 929f6692-e2fc-30db-aef8-f66e5dfdb91a | -2.54815 | -47.29202 | 2024-11-18 05:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c0dbb12-39ba-3819-bebd-8df68d3a4ca0 | -2.79389 | -54.00975 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2569e05-a114-3cc1-9bcb-0317a18763ce | -0.95014 | -51.72391 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afbaa230-ab55-3661-81ef-07c29846c2bc | -3.3889 | -53.26912 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 239b5084-ee85-3c8c-b9c6-e12e3a329c0c | -2.60912 | -54.2576 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
