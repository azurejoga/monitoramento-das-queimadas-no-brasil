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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33ea7746-7aeb-3fc4-95d5-d0ca82e9c0a1 | -2.50406 | -54.16505 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63e524f0-6f22-3c52-9313-70ec7c23afcf | -1.32575 | -55.83875 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca9dd0a4-bed8-3daa-9fbb-adb35ed6081f | -1.62555 | -52.38196 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d7f9e3-87cc-3b34-ae38-dcf52a3ae5bf | -3.48054 | -49.9243 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aee25c79-1e45-3c5a-a9b5-3f232834d9ad | -2.60299 | -53.98964 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3a2b54d-8dc4-3271-8520-fe5551c3be37 | -3.05274 | -48.51941 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efdca51f-0925-3999-a5f6-3498298b3d2f | -3.29164 | -53.67544 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d125015-61d8-3f5f-86f5-6777a4f9f668 | -3.10024 | -53.81042 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab232ad9-9593-39cd-ac93-a925a2b01aa4 | -2.77084 | -54.02693 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7caf6a0-0b3d-35b2-90e9-673a732955ef | -2.29024 | -51.3247 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ca87828-145a-35d2-85c8-ade88875967f | -2.41093 | -53.82552 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1e87f36-efdf-31f4-ae7c-4885a6e142ab | -3.94738 | -49.76049 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4aadfce7-6fcb-31ce-b1fa-3c5642134d1d | -2.20623 | -52.09899 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c66f2715-6da5-379b-aacb-4dd0dc51f3b0 | -4.69808 | -47.18509 | 2024-11-29 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44dee458-1f7b-34ee-bd26-08e84d66e504 | -1.6233 | -52.37444 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 044ee345-70c7-3435-925b-8064b070f23c | 1.32502 | -50.67569 | 2024-11-29 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be3eb65-37e6-3e86-9801-017c91cbca68 | -3.10495 | -54.04399 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8ba03ea-224d-3f9b-b653-61be350c4a52 | -2.59672 | -54.09461 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e13bbd09-e5ee-3ad7-89b2-b211d658866e | -3.55994 | -51.03496 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed6dcf8f-2d6a-307a-a338-0682ecd8d325 | -3.11122 | -53.10761 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f759854-ad1c-3220-ae0f-3b6da5bd8b1f | -2.8765 | -54.00092 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 526c9382-6712-3a74-aa38-b867d8ff3f05 | -3.03569 | -48.49467 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccc9af92-933e-3513-a4d3-c2badbc6bf6c | -3.17754 | -46.31047 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9651cbfb-fb2f-3cdf-b6ac-e34785ed0499 | -2.87865 | -53.98716 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a369deb-8c2f-3c4a-8a3e-fdb65414eafe | -1.58445 | -52.2753 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba6a4d6e-3e40-38f5-b858-7cd287290583 | -0.25363 | -53.76352 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d874830-7dc3-39a5-a92b-40e7dad4ccce | -4.11583 | -48.48399 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73c71236-a33b-3422-acf1-be80bae02536 | -1.53414 | -52.66369 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 64989a71-332c-3f81-ab6b-8d9ff79cdfd5 | -4.41343 | -49.70436 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| faf7b381-4beb-3fd3-bf4c-a9b2e873630f | -2.82884 | -54.0676 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bcda40a-c775-3599-9d63-63dc069c3acf | -3.08342 | -49.20877 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d7dbf9c-5c78-33cf-8b16-866890fffeb2 | -1.0717 | -53.64362 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a3fe5b8-2ccb-3df9-aac0-894c70d883c4 | -2.09055 | -48.55062 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08df74fd-dd96-3ab1-bec1-7fd377bdf4fa | -1.24318 | -53.35461 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03372fa8-e049-3117-afa2-43df24dede9d | -1.27003 | -51.63265 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9db8a86c-62d3-3604-9e44-16e8591e4971 | -2.56932 | -54.33479 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba0a6ca4-fceb-3cd9-adcf-c7f65caf80c9 | -1.64498 | -55.68155 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b09ecad3-8ea7-3e08-8956-ac26eb69fedb | -0.27914 | -51.63963 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d87bfb0-141a-3f76-b1dd-fbe0049c32f8 | -1.46629 | -52.68515 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09b3a668-20f5-3002-9206-971d242f82f8 | -3.64923 | -54.6935 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58352d60-e146-323c-8027-0537d77f69f9 | -1.60563 | -52.29295 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f16ee56b-01cb-307d-9f24-adb1d964a136 | -1.46155 | -54.50203 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 710a78c5-1d06-388e-8809-04f6fff3a1cb | -1.07498 | -53.38412 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 905b4f61-7b27-31d4-9dce-a5ab0843dc4f | -3.2398 | -54.22379 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a8fecd1-5efb-3665-a97c-374d2d2e1efd | -2.70327 | -48.65131 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d94a9b27-4869-3e23-9c46-081f957edf3a | -1.5651 | -55.79159 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d160b842-0d63-39e9-9797-99571ce1fb85 | -1.56878 | -52.24409 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2d5c24a-3c18-3b38-b64f-cc13d71a8812 | -2.25366 | -53.46019 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9ef22e14-ee76-3b7e-854d-4f2c638a698f | 1.47612 | -55.72142 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15de7677-4049-3493-bb01-3787c62a50b9 | -1.6804 | -52.53333 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d8fa4be-8dfc-30ad-9852-832d23d4e18f | -1.20013 | -53.8898 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c87f794-a4aa-3656-8703-a1d675d5a5e5 | -0.11913 | -51.7247 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b565805a-6412-3690-8690-746924a7681c | -3.2289 | -54.09861 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84c6a5e8-0d2f-3be1-90f1-1652d6591b42 | -2.35181 | -53.92205 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3735f6-542a-3b54-b6fb-6268d9952bc3 | -3.03115 | -54.01439 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e14506b-1963-3410-8663-5bc8212a184a | -2.81661 | -54.03751 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c677f9ae-0e57-3ed4-b9fa-87e44159126f | -3.67743 | -54.44817 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bc32a11-4196-35f5-8e05-19b2f7466dda | -2.87534 | -53.98665 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34781c3f-cba0-31cf-a9e6-a844b06d9096 | -2.6689 | -49.86451 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f1202c4-527a-31d5-aaaa-0399dc2f3c12 | -1.3725 | -53.63458 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49f96577-4fe4-3e50-9bd0-b023b13c6507 | -2.57559 | -51.8636 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c25d6b-365e-37f7-af19-74de3cb270b2 | -3.44858 | -53.12467 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2a835f1-8d2b-31b9-bc0f-38a2a0a673d0 | -1.73697 | -54.1759 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47de5653-5960-332a-b263-33edf5ce78fd | -2.85951 | -54.02298 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2152b98-00f2-3c52-97b5-d2ef9fccfa8e | -2.70409 | -49.83348 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9567ef36-4613-3e9b-a95c-8a60987f1fc1 | -2.72876 | -54.40287 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48630e24-efbe-34bc-8938-eb0018b12128 | -2.582 | -51.72656 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce8ba5df-085b-31ac-98d2-12a248d064e9 | -1.19521 | -53.89961 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 653eafec-a9ca-35ad-8957-ac97e5990fba | 0.3378 | -49.71698 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 64c97fd9-347b-3074-bacc-b5285655a29a | -4.07277 | -50.03346 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6de7ddca-adb4-3668-bad2-10b55ea7dd5b | -2.56987 | -54.33132 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52ece25e-996e-3d2d-84cb-b6fe7907ced8 | -1.99659 | -52.09229 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e95fe2f8-4055-36e1-839d-ccb33638234b | -1.69287 | -52.43169 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eff9ce2-fa59-38a3-8233-ccbe70ac541a | -3.31782 | -54.18301 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a49e7e24-ed5b-3dac-abda-09d21d78736b | -0.99388 | -51.7195 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 115e98a0-6337-3512-9c38-87040cbd5913 | -1.53243 | -51.6202 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a470609e-14c4-3921-8e93-1e75c4899140 | -3.32697 | -50.21851 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec846663-5e40-3409-82bf-48f6ee86016e | -1.09787 | -53.60909 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ede1470-7b47-3f0c-b7c8-2c20254476e2 | -2.8446 | -54.01011 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d09853f5-eb70-3003-9c38-2e196759fb78 | -1.9975 | -51.1769 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6af854f-dad8-3ceb-b848-bbab91a1f39b | -3.41429 | -50.15937 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 501a314f-96b7-3f69-98ae-776d9885dec0 | -3.08923 | -54.12267 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00b1c6dc-edf5-3830-a7cd-38ca772b0dfa | -0.96244 | -51.64499 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f377152-23dc-389e-ac7c-d42437beecd3 | -4.69408 | -46.66282 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29017b4a-33b2-3d90-9e11-9bd5451a45cc | -2.87427 | -53.99353 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2393b05-2c56-3922-bcfd-4eed581375e3 | -2.86353 | -45.53844 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ef2f7ce-4376-3a04-aef8-ff50420200cb | -3.26912 | -54.10124 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2610ad7b-39e8-3e05-ba39-f95ed066d796 | -1.37944 | -52.12812 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 78cb40b1-70ac-3521-a789-13fb3c6d67bd | -2.76551 | -54.08254 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 327e6e20-2654-3693-86bd-24013b5b8d6e | -2.88258 | -54.00896 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05a6b21d-5da5-3dfe-acb6-38bd4b42e6c4 | 1.3313 | -50.6709 | 2024-11-29 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ea983b6-8deb-3c06-b563-33ff949c48e9 | -0.56541 | -51.69814 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfeab07d-dca3-318e-b27e-b438171480fd | -2.61172 | -54.28095 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ab98cb4-e74b-3243-b87f-3c57e58d939c | -2.57529 | -54.29664 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58c959b8-f597-353b-9c3b-e29fe7fb8555 | -1.0947 | -53.3661 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8a24e4e-1d05-3df2-916c-f6c406342f63 | -3.11437 | -53.2637 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d70d34b5-c127-3989-9af9-da8d16a754da | -3.2464 | -53.63665 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb7e83fb-f080-37aa-b3e2-537d7246c51b | -2.8233 | -54.05969 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f5e675-8cfd-3f2a-94dd-19976eae3bbf | -2.96732 | -53.85663 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d49c43b-86a2-3304-b0c7-ae1503559ca6 | -2.73673 | -54.11263 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README78.md)
