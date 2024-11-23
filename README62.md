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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79ad3efa-7680-3fc1-b00d-7083cbba37ae | -4.26255 | -48.69514 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4ee7c5d6-b182-33ad-947d-2abee2f75d8c | -5.57142 | -46.28856 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 372df80c-d0ea-3367-815c-64250b5b0e05 | -3.16464 | -53.28234 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 500a3bff-f642-326a-9dfe-4de837a0cfb2 | -3.21269 | -54.02372 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d47490f-a314-33a8-bfb8-8a850f60a166 | -3.50966 | -54.73631 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3016860-e9f9-36cd-b791-9788d648015e | -3.30576 | -52.57385 | 2024-11-23 05:12:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04015892-d883-3071-b8be-a8726f92d95f | -9.70975 | -63.31915 | 2024-11-23 05:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0864bc4-99af-3239-b134-931290b81a60 | -23.31445 | -47.67818 | 2024-11-23 05:16:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c9a40dc1-f0d5-3d1d-877d-a1718c559e4c | -23.31565 | -47.68205 | 2024-11-23 05:16:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5b5c91f1-ac5f-36d0-a775-f521783acb27 | -23.31399 | -47.68487 | 2024-11-23 05:16:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 41699cbc-6961-3cd4-ac43-def59f8ba0e0 | -4.2605 | -48.697 | 2024-11-23 05:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e741df2a-a9cf-37be-b84d-38f2b6e4d4d7 | -3.2385 | -54.2431 | 2024-11-23 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 29b8f019-132d-315a-b8cb-5744c1a5b6cc | -3.2569 | -54.2426 | 2024-11-23 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 8492d498-8bf6-3626-b096-d433662bccdb | -2.9982 | -45.1658 | 2024-11-23 05:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1241c7f9-4af1-3241-8ec8-ff89e2ab1703 | -4.5216 | -42.9078 | 2024-11-23 05:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9761c0d7-c421-3f0f-9194-02194f3d204b | -4.5402 | -42.93 | 2024-11-23 05:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 702e35c5-0fc6-3e53-95e6-b62b4b32ec62 | -4.6271 | -46.4992 | 2024-11-23 05:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8373cf77-8397-3a23-b967-1dc1ebe98ec4 | -2.8166 | -54.0326 | 2024-11-23 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 87cdea09-c739-39ff-a78f-b2149b48b2a7 | -3.2386 | -54.223 | 2024-11-23 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6da48802-a7a1-3ba9-936c-eff01ca691be | -4.5403 | -42.9066 | 2024-11-23 05:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4b400602-0d6b-3ff5-817a-8b981ea7bfcb | -1.7359 | -52.7181 | 2024-11-23 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 202439f1-89f5-3cca-ab34-4ab16f410f09 | -4.6085 | -46.5002 | 2024-11-23 05:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 900f6141-48e5-3f22-9306-a0bb3cbb3211 | -3.2569 | -54.2226 | 2024-11-23 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a6295cf0-f040-35c6-9a51-835fa4d36d81 | -4.5216 | -42.9078 | 2024-11-23 05:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c98b4b20-ace3-3dca-b388-fd650bf7ed1c | -4.6086 | -46.478 | 2024-11-23 05:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7e792981-b750-3c96-9a51-906bc93ac7c7 | -2.8349 | -54.0322 | 2024-11-23 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 90463211-5004-32fc-ba34-7bbab16136da | -3.2386 | -54.223 | 2024-11-23 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| adbc6aa4-5fe6-3daf-8de1-c98edf528b46 | -3.2569 | -54.2226 | 2024-11-23 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0e4c352f-0678-359f-8aa8-fafbbb397eef | -4.5403 | -42.9066 | 2024-11-23 05:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b50f1b3d-3b44-3b55-88bc-6c02b8a0ba6f | -4.6085 | -46.5002 | 2024-11-23 05:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 152.0 |
| f0023e49-ddf1-390f-93d7-a3ad4cd44ebb | -2.8166 | -54.0326 | 2024-11-23 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 064c06e2-8f33-34e4-984c-bd08cef5c6b8 | -3.2385 | -54.2431 | 2024-11-23 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7d7ee49c-9662-3fd8-8542-6ec1e15cbc0c | -3.2569 | -54.2426 | 2024-11-23 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 09b8ad07-5e05-3f60-b265-5efb0140e07a | -1.7359 | -52.7181 | 2024-11-23 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 97fe0893-a629-3bda-8999-0f7cca5f3add | -4.2605 | -48.697 | 2024-11-23 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fb512729-4370-33e9-8a43-ba9a9c271c35 | -3.0169 | -45.1426 | 2024-11-23 05:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f19f3575-89ed-3ca5-bc2b-a4a0de75bff0 | -0.17935 | -51.6046 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c53169bb-2a01-3523-9251-9c6e3b0a5e4d | -0.26105 | -51.56692 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4605e71-e2e7-3046-b3b4-d927c184a342 | 1.40434 | -56.00888 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcdc7b65-9a6e-3501-9615-a85f86cb5cfa | 1.36358 | -55.94586 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 481ea282-fd0d-3a35-bc71-11d1145e8774 | 1.36722 | -55.94119 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab912a4a-c5fb-3a34-8c52-c6505f8ec11a | 1.94336 | -60.86617 | 2024-11-23 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bac1bbd9-27da-332b-91cc-f39e625092cf | -0.26305 | -51.55414 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2e145c7-5b73-3c10-8bb3-53ccb8c9f21d | -0.10473 | -51.65727 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbf1a578-0c35-3f17-8bd7-1b306087f39e | -0.18525 | -51.60554 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9508e3-a9cd-3197-a88f-b7b391d8f1a1 | 1.81853 | -60.69513 | 2024-11-23 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33fccfd0-da4b-3683-9914-7c92d7017170 | 0.7638 | -50.80379 | 2024-11-23 05:31:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdb6587a-d585-3d91-9ab2-5b0e22f7008e | 4.00349 | -60.1088 | 2024-11-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dab91ea1-7ef9-3da1-9952-44f95d835e1f | -0.26039 | -51.57114 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e545113-bcfc-3f96-8b75-6f03fd26015d | 1.36293 | -55.94185 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fdc3923-ce00-3c36-8794-d2830f8c7710 | -0.25972 | -51.57544 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef232561-8d03-3414-8538-902c69186cfb | 0.95677 | -52.10485 | 2024-11-23 05:31:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a699c22d-556a-34a2-b2dd-b87724a65b26 | -0.32394 | -51.53689 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fd13a52-d46c-3d3a-af1e-88366a5271ed | -0.3265 | -51.53756 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd039980-367a-3d9c-b3fb-0958cc1b414a | 4.00405 | -60.11231 | 2024-11-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62f2c649-8cd6-3bf9-8582-b35ee0f1bf38 | 1.40503 | -55.90227 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 071f644d-8bf9-3430-8102-b765dce6ea19 | -0.32056 | -51.53662 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ed334a1-0d4b-3036-9f99-1539dbcd2c28 | -0.11061 | -51.65815 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7387e31f-4e92-3c1f-be50-d9412d23c540 | 1.37516 | -55.93589 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aedc3c-e48a-3c4d-9be3-b7ec097ef5c6 | 0.95739 | -52.10869 | 2024-11-23 05:31:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5572c7c-26b1-3605-8a5b-6ba2f78a3593 | 1.40007 | -56.00956 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95b0a789-402b-32f9-9850-060e091c68b1 | -0.10576 | -51.65954 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 765b1f8d-b1c8-3b5c-bd6a-f6696afcd155 | 1.37087 | -55.93652 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f4ae8a4-8412-3c95-b5bf-f6741f619e12 | 1.40136 | -55.90696 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48e593af-83ec-3ee1-80b1-bd9698f8a8b3 | -0.26371 | -51.5499 | 2024-11-23 05:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aa0eb81-388a-39ef-822d-9474441b8b22 | 0.15639 | -51.23023 | 2024-11-23 05:31:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab4ccf49-d507-3869-a7e6-4c0807e0b45e | 1.36658 | -55.93718 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 652e45e3-da35-31e3-a4af-fd771c7a7038 | 1.38976 | -55.91706 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aa812b3-9735-3c45-97f6-bd8e62f2d89c | 1.39039 | -55.92106 | 2024-11-23 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcd02a41-d3e5-3a0c-b18e-da2398ab1984 | -1.11921 | -53.40042 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70dc4796-58fa-3e18-bdd5-7fe3f15c1873 | -0.92644 | -53.10183 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 252240ce-a660-3c93-9f9e-df35f4d3f6a7 | -3.00347 | -51.54944 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25267b9e-278b-36cc-a5e8-6d982fa02986 | -1.12597 | -53.40163 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac2d1e9-c4c4-339e-8c0b-2bad11f9a066 | -3.06428 | -53.27904 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b1931e2-85bf-3651-aa1b-a1bb3b4457ae | -1.4246 | -51.61603 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8101df00-44de-35ca-a7ba-098e693f53e4 | -1.78281 | -53.64778 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10847e70-608c-3954-b814-5721bc4c7d75 | -1.66899 | -52.65932 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d24c9d8-05a9-3bcc-ab4b-6be818e817a5 | -1.04939 | -51.74125 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 633311e2-7d28-3654-aa0c-d13771ccbb4c | -2.45742 | -53.70117 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34d8be9f-01d6-38eb-94ea-7b2787bdf996 | -1.64135 | -52.70464 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10b4e766-ac21-3d39-96ec-9cbea86c1baa | -3.80031 | -51.76269 | 2024-11-23 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c987097-13b1-316b-a8be-77134210d087 | -3.24397 | -54.2366 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e5d5e9b-3f90-35dd-ae3c-1f34db714d44 | -1.1379 | -51.68008 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5facb978-f061-3eff-9c02-471ac15bf34b | -3.24924 | -50.66965 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76310ba0-036d-360c-8050-6896ecc4d5bf | -0.14541 | -60.86461 | 2024-11-23 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 883167fe-230c-33a5-9725-73f0ba40e87c | -1.13441 | -54.17617 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92d53fbd-0372-3615-be30-6f3060d13c05 | -1.24639 | -51.74774 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ebce28-b33e-38bb-a29b-eaec213c0c7d | -3.24588 | -54.22412 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7de732b7-0980-359f-a47d-4fe05e6c51da | -3.11262 | -54.28924 | 2024-11-23 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e72fcf05-e042-386a-bdee-c971d31ba672 | -1.72673 | -52.73363 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4489d7e3-c3f6-3cbf-b3c1-71a3f27bccf3 | -1.03958 | -52.99379 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1b8de0e-f8c3-3cfc-92c5-a28c7894d31d | -1.25897 | -51.76237 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1753131d-0762-387a-83fa-8baa2df416da | -2.75589 | -54.0716 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a032650-a7a0-3157-bad8-2f890ee432b8 | -1.63977 | -52.10144 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ff86915-730b-347a-be88-b6dfa92bdc57 | -3.23926 | -54.23265 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a28412dd-bf76-3280-8c66-97f00352f97b | -3.22013 | -53.93286 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88d13f43-58b0-35c0-aafa-697b6a45c9f2 | -3.06365 | -53.28186 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 727a3cca-5a5d-32b8-8d47-932db2a111f6 | -1.11693 | -53.38993 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2faef7d-d7ba-39a9-ab1c-189d3f2f9fcb | -3.11712 | -53.1106 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 12eb2f08-c152-33e4-9bfa-fed7f5dad36d | -1.6752 | -52.65641 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README63.md)
