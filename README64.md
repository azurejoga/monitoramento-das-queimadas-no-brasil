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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 923fe426-a25d-3856-ab6d-cb75902df0ef | -2.56638 | -54.09348 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8265429d-4c47-393d-9b2c-dc04e124415b | -3.42654 | -53.28769 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ac82ea-c5bc-3961-b85e-b1e16fe76877 | -1.66956 | -52.4281 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd545bb-7a52-369c-857c-035f7c222943 | -3.37113 | -50.82221 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15296114-7ce9-3842-b28d-164d86ae005a | -4.11904 | -54.23505 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a48e273-a9c7-3957-873b-2e8fdd28f06b | -1.71332 | -53.06257 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b67a806-c709-3236-aba7-903c3a9a19a2 | -2.6393 | -49.9098 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b58f1fa9-13ea-399e-848e-cfacd09fab13 | -2.87811 | -53.9906 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9354f83-b1e8-318b-bac7-5f2c891ce47f | -1.15817 | -53.67809 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d534ac4a-d63f-3bf1-bc36-0e681ab06874 | -1.58992 | -52.24017 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a16cf0-53f3-302d-9419-e3c8413ec006 | -3.87482 | -48.3637 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cac00ef7-85c0-307c-a80d-7c6d1354279e | -3.16261 | -50.58065 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8eeac1f7-7d56-340f-9b8e-07f56eceb481 | -2.83914 | -54.02336 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bdde9be-c479-3e0e-a3ae-5c54ff0db228 | -2.53725 | -54.03936 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1070fb17-f0b2-36ad-a2c5-4859f955db52 | -1.8816 | -52.66082 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bc94f14-0ea2-38dc-ba7c-4a244503a301 | -2.83161 | -54.07155 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66aa0f78-6ae0-3e39-84e6-63e3b64c7fe9 | -1.42396 | -55.26036 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d56b1420-7d86-3eeb-a88a-34039f3c4ef2 | 0.62709 | -50.56928 | 2024-11-29 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2460de68-b240-3158-9985-b5a6a69cce1f | -1.61994 | -53.88136 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 186c91e0-d832-308b-8014-9cd7c75b6a37 | -2.5878 | -54.06497 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae4c858d-c035-3e85-9736-3f67546453cb | -1.60111 | -55.42831 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60da9bc6-1451-34a7-a071-0a6a7164259b | -1.16808 | -51.93288 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02bed72a-88c1-39da-ab86-b48fa2500c20 | -2.60245 | -53.99308 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e13717b2-6513-388a-9e7e-783ed97bbc2f | -3.02569 | -54.02764 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce2f1937-2fc8-3d51-a11c-923f91b08428 | -1.35051 | -55.01278 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f3a5ea-e907-38ec-af36-f9d2c22c18b6 | -2.88839 | -53.94646 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26ed1b81-16cd-31da-8f49-0a4d151f058e | -3.09916 | -53.81729 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91d2f2cb-004a-34f2-96ab-ef1b5cd9e6bc | -1.1511 | -53.70169 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c66735-51cc-3d21-9038-399ad313316e | -5.98064 | -45.35988 | 2024-11-29 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72bc31d0-5351-3058-a8b2-8582cbaf1852 | -2.95503 | -48.34051 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e64bde90-e81f-349d-b06a-c1410dfb5478 | -2.20204 | -53.7474 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7290a8a3-a672-3bbc-9cb4-80f499d5ea72 | -5.44412 | -45.58176 | 2024-11-29 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a39ae136-9ff1-3458-9de0-ab41a6a1c498 | -3.28264 | -50.62691 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f494f5c-734a-3fad-9046-0cf8c47c301a | -3.95969 | -48.08038 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e4ddf39-31a9-35a1-bc6c-dd4043f93ee2 | -4.09307 | -50.74417 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8776de95-bf4c-309b-bc60-a5049093cd32 | -1.10139 | -53.38818 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e91e8035-683c-337f-addb-15ae10ab699d | -2.87007 | -53.34501 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56cc3012-7f69-3f5e-a55e-4d281d286ead | -3.96414 | -48.82991 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a53b626e-91c8-3465-b267-547a9ee6f3f0 | -3.43965 | -54.12134 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb015df-abcf-34e8-86ce-1ef2b8727da2 | -3.31944 | -54.17265 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 931888ec-afb5-3440-946f-e8e1b8628305 | -2.5983 | -51.91921 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f580c95-3c20-3169-b00c-fbb358bf00f0 | -2.77476 | -54.04515 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55869fbc-59c7-34f7-8884-f24a9161ffd3 | -2.84645 | -54.06326 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dae2e71-3c8f-3d3b-92dc-d889cb7efa1c | -2.54056 | -54.03987 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77fca081-48d0-37e1-b65d-99d9d47a2178 | -1.66426 | -52.50588 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bef5d75-80a3-373b-ba02-d4f34f1fb472 | -2.59968 | -53.98913 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 420ac99f-1c95-36a1-a4aa-ed670f75c7a2 | -3.08441 | -53.30133 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4440d81a-13a8-3a8e-945d-3601a55c5151 | -4.10102 | -53.9822 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9fd4da-4626-3e98-bcac-4b5df30c3b0c | -2.99051 | -53.36088 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b2d426f-26b4-3e69-b8f6-8f2b1865a349 | -3.09422 | -54.13404 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf93169c-16af-3254-a812-5080594173be | -2.79792 | -54.04872 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 196abe61-58c4-3341-8919-c70299bfc93a | -3.61156 | -49.85337 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45d09fb4-9c27-3c25-93c8-1785b59866c6 | -1.12981 | -53.09772 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 771a847e-b586-3f4f-8ca4-815a6ddec0a4 | -3.70473 | -50.51508 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a95b841c-d32c-3900-8211-5892fc06a897 | -3.10549 | -54.04055 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8971f61-4c2f-353b-89fd-45ecb6854e0c | -1.61365 | -52.45884 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63589286-a6c3-332d-9889-9c6fe1b235f5 | -2.90075 | -54.1741 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6bb23a4-4ce3-3e01-84c6-1bc28c513589 | -3.22621 | -53.41891 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e5aa56e-a649-3e33-a002-7322ea3faaed | -3.52586 | -50.38654 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 249bdb5b-d3bc-3040-b917-5033018ad681 | -2.42441 | -54.60925 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de8f3e40-6480-3ae6-ae0d-21537e4f8665 | -3.27842 | -53.6734 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830d539f-f464-35da-8265-dc14b477369a | -1.62101 | -53.87447 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53821ef0-caf9-3973-b0c6-d1c059ea7f3b | -1.98672 | -53.29525 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94842596-4d4d-3ccd-8fc1-4e1abda8cda4 | -3.0601 | -53.28347 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d775ba63-6736-3e24-a643-540f7c2f1cb4 | -2.25598 | -53.61862 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23b36ec0-a62c-38a5-8c89-be728b989200 | 0.63055 | -50.56875 | 2024-11-29 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f6040e90-0474-34b2-b6d6-88595a359594 | -3.24534 | -53.92857 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371da996-0273-36d7-80af-346a3d1386d9 | -3.59888 | -49.98581 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc8ed32a-f101-3930-af91-ac7e352b7095 | -1.94247 | -52.96761 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb30e757-55c2-32ab-a2ab-dbe43e0766f7 | -2.53571 | -54.07093 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 836e0825-f629-360d-9df3-96d90bb9ef39 | -2.5928 | -54.07633 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a770eccf-56df-31e5-b2b3-7ea463d49d3e | -1.62717 | -52.37146 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c278dc02-ed4a-3fd8-ae75-6b30ca0b71b4 | -2.4282 | -54.01847 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67bbac21-3279-3205-9263-3ab51eef39c9 | -3.01991 | -47.79768 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e86b8062-e32d-3288-b2c3-b2047b0f830f | -3.04668 | -54.04497 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32a5d1f7-0216-3f77-9f64-56c85034de38 | -2.7489 | -60.23431 | 2024-11-29 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8de989b-bd7f-3e3b-b947-24271752daf0 | -1.1035 | -48.37129 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6247e580-c404-3bfa-b93f-0544e310decc | -5.62962 | -46.9643 | 2024-11-29 04:57:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6260a502-1829-3a1b-95ae-3755c0f2e5bb | -1.74283 | -52.08976 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c460a04e-500c-36a3-ac18-c375bbd96cbe | -4.17738 | -48.62846 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0688df1-a852-3331-bf1d-fddead918283 | -1.68675 | -52.42717 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c0c30fc2-af92-3738-a5ce-06b778f9eb31 | -2.20536 | -52.04784 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5639a238-707f-3b49-a6fb-e35bc02e2d52 | -5.39345 | -46.11041 | 2024-11-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dac427aa-0e87-3377-a90c-8352c85e1910 | -1.67622 | -52.42913 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35524ce6-7eb8-31e3-a921-240fc2b15865 | -3.58103 | -51.32301 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 714be251-ed3a-3330-ac0a-efa161e93183 | -3.03052 | -48.50126 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c10478b-5564-3582-9b20-d897a8d80211 | -1.20905 | -51.62325 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a292e9df-74ce-343f-81ce-29c1d4d1d9e6 | -3.26582 | -53.81916 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dda1faa5-af14-367c-8d79-2960e4195e0d | -2.80007 | -54.03495 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ec00f5f-5d7e-30b6-b419-0b48eeaa8f72 | -2.8384 | -49.88906 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73a2bd4a-7789-3579-a258-ba6044b4f279 | -2.23206 | -53.68522 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d4bdebe-1958-3556-9801-4de72e3d7aa4 | 0.0784 | -49.87365 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73f9f8ff-3bea-3bf7-8494-e9705c860078 | -1.33106 | -51.42464 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fb7840e-1956-3202-9fe5-b4a2ccc71a3f | -1.61716 | -53.8774 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b15b3b9-512f-3e04-8341-8172e739c435 | -1.716 | -52.63189 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5cf0e0bb-b5ea-3fee-969d-a08d3cd477b3 | -1.3774 | -52.42586 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd8cb16e-faf9-322f-b3c8-75dcb0b01144 | -1.07184 | -52.33549 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88ec528e-a2a9-312e-b6f9-2a6fadf562fe | -2.82082 | -54.48836 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df192a69-89a9-381b-a409-c0e930531207 | -3.10845 | -53.10365 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3da8830d-5dc3-39cb-9b54-f5dd6e780b58 | -2.61952 | -53.99219 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README65.md)
