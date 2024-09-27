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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0af4372-89cd-336c-b02d-0efb09d22d0d | -6.86762 | -44.2984 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a166c1ed-b0b1-300a-9d81-12c2dad57969 | -6.86733 | -44.30206 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32b56fbf-6516-3263-b6bf-2bd92e85d405 | -6.86708 | -44.30205 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5264c94f-d110-39d7-8022-cff4bfbf794b | -10.65013 | -45.8604 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41248666-4a40-3eab-9fb4-0efd2c1268ea | -6.86681 | -44.30574 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41847161-2db5-305f-a90f-fbcd8644a69b | -6.86653 | -44.30572 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1d10950-af7a-3d56-b066-79a8a01933b0 | -6.68787 | -44.16058 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36602833-4cd9-3197-96b7-c60685d97178 | -6.58103 | -44.18024 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 185b8c1f-556f-3afb-92b0-e72798b97d57 | -6.57746 | -44.17612 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df155bcd-4454-3020-8035-14860b5044f4 | -6.57693 | -44.17976 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 124b81f4-f628-3a43-8968-d25dd8a0921d | -6.57336 | -44.17558 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d92ff66e-fbf8-3626-9ed1-3df0a2609e91 | -6.56927 | -44.17502 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e446646a-3911-35ed-ab54-9fe479a7ef99 | -8.00387 | -44.49895 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae868330-2a77-31be-86a5-f5c0bc8fdd63 | -8.8324 | -44.95246 | 2024-09-27 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f17c955e-9fde-3dfb-a21a-b63de394b3bf | -8.70986 | -44.79574 | 2024-09-27 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8727094-a4f1-3cfb-9096-c61b870b0834 | -8.70935 | -44.79928 | 2024-09-27 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e576e784-5585-33f5-a4f0-7c68a4b92993 | -8.7063 | -44.79182 | 2024-09-27 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e8b66b8-ee2c-330f-95e9-51874934b3d4 | -8.69746 | -44.27781 | 2024-09-27 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2c80136-081a-357b-b5c8-7dd391d361af | -10.67094 | -45.85326 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70c78c0a-32e9-38ba-abda-f3e8b9dd32ae | -10.67027 | -45.85804 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2dab4d1-6bce-3e2b-8810-74f706a56874 | -10.66707 | -45.85259 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c65ff5ea-abbb-32ab-901f-41daf7b53d01 | -10.6597 | -45.87711 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b24e0fa7-417b-3336-8c55-fa2791f9a62a | -10.659 | -45.88209 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe36cdf7-f9db-3719-ace6-ba82ec2aaed2 | -10.65831 | -45.88705 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb1d902b-0630-3e94-a754-c2611e7b922d | -10.65763 | -45.89197 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d61ea3b-ca05-36fa-abfb-85fe04531a6f | -10.65651 | -45.87156 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 887f9f9f-d89d-3b5b-a531-cbcc5faa8cf0 | -10.65581 | -45.87656 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ca23ab8-bc1b-30ff-b573-d4b83434941e | -10.6556 | -45.86969 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3e9d118-619d-36a2-9d92-666b2453a807 | -10.65487 | -45.87469 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ec80247-cc61-3fff-a848-e84837715d3e | -10.65402 | -45.86091 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a87a544a-4fd9-3e41-8af7-7d2d41dd2ac4 | -10.65375 | -45.89141 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f71d812-572c-33c3-b581-80b12962d436 | -10.65332 | -45.86599 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71447249-b9d3-3499-ba08-815aef0868a2 | -10.65244 | -45.86414 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9babf7b-4895-348d-9eee-67c4d0e9df4a | -10.65193 | -45.87601 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cdc0eb3-fd7a-38cb-9440-2f100b48d310 | -10.64929 | -45.85855 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47be7f11-ad93-338a-8b78-8a441db5948b | -10.64694 | -45.8548 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1cb535cc-a9d2-3a69-842e-e47a210cb899 | -10.6454 | -45.85805 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31aad612-ac87-36e0-b742-2e6768cd59ac | -10.64353 | -45.96484 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb1c3be5-f27b-36b4-a6a4-84a787281d76 | -10.64286 | -45.96966 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ca4f6ce-82f5-339c-a8b2-e2d745fdc5e8 | -10.642 | -45.96286 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 815e35a1-000d-3415-bbe5-b47e5fa2b575 | -10.64129 | -45.96767 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dd84b5c-f562-3255-9223-08d6a7dc2c0e | -10.62236 | -45.98964 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 76bdb88e-0e04-3c9b-bef1-c1021a94f93c | -10.62165 | -45.99451 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ab53b9d3-abb5-39e6-a371-e55e5312e0ec | -10.61851 | -45.98908 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7c43dac6-ef00-3b1d-a19a-6d6be3d36422 | -10.6178 | -45.99395 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3bc0ca27-06f6-361c-aea9-af82546eb85b | -10.42363 | -45.81169 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c51fb1c8-518a-34a9-883b-c75e1040f8ad | -10.42046 | -45.80617 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99113719-bbff-3791-bce5-4ebb7f4304ae | -10.8418 | -44.79615 | 2024-09-27 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d95316ca-68c0-3eb2-9f15-041d32527100 | -10.72638 | -45.20992 | 2024-09-27 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae89e094-5b5e-3e6e-846a-6849f9e10534 | -10.72585 | -45.21357 | 2024-09-27 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1710b2c8-3abc-37fb-bd22-72b4d6b4c4f9 | -10.52865 | -44.87169 | 2024-09-27 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47ef64ce-f884-3b78-b95f-6b6a1fe22b40 | -10.06801 | -44.89561 | 2024-09-27 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5b11bb9-e187-380a-8bbe-8a5ac2d6d7f1 | -9.70099 | -45.37218 | 2024-09-27 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5ce20b9-cfd6-3258-bdbd-4c08716e3dc4 | -9.53625 | -45.45997 | 2024-09-27 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2944150c-ffdb-3ef0-aac9-0b6b5f33cc3b | -12.25036 | -45.4881 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba9fa205-ffaf-3417-b75d-81891e05bcda | -12.24986 | -45.49176 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7db9026-d583-3177-9c48-fa5dd60ddf96 | -12.2458 | -45.49116 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fff3662-b83f-3b07-8dfa-43caf51c5afc | -12.24531 | -45.49482 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ba19a3d-b701-35a3-9c39-1b86059a3301 | -12.24175 | -45.49052 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab78bf4f-3711-3e0d-8af2-953987095af7 | -12.24125 | -45.49419 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ea17a33f-4f51-3874-9d27-f2f3a86fa7c4 | -12.23769 | -45.48988 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 126e8a0c-c6c1-3e02-a1f8-bc81d23b5204 | -12.23364 | -45.48924 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 804d41dd-08ed-3218-9261-334a01d03666 | -12.22958 | -45.4886 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb3222b-1d8a-3b81-80d4-726823d627a2 | -12.21569 | -45.49762 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94d63600-767c-3dbd-ad08-493332fb56f9 | -11.7749 | -45.49855 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114ee38b-0325-3424-b145-6bcf20b0b274 | -11.7744 | -45.50206 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51d575a6-6b8e-3808-9bb2-e51c904fae00 | -11.7724 | -45.48706 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b092ce95-3ff3-39a8-b022-b29c9d7f6782 | -11.7719 | -45.49062 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7271939-d86f-36e6-b9e4-fa42646b40d1 | -11.77141 | -45.49413 | 2024-09-27 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2328a22-249e-3c20-ace2-d7073bf6bdad | -11.24313 | -45.50669 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6863ea40-d80f-3a9b-8123-196ef72776a0 | -11.24266 | -45.51015 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a75530b-2f3d-35d8-841b-30a0589b94ef | -11.19388 | -45.55243 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 31e69247-f4f5-3ca5-ab02-6afba0825b7d | -11.1934 | -45.55577 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f2983db9-7319-32cc-b1ad-b9e7f7c7ec84 | -11.19293 | -45.55913 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1fa784bf-83e3-3a4e-9a28-3a177f4fd164 | -11.19039 | -45.54824 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d2176347-7993-3020-ae30-a47697d1faf1 | -11.18992 | -45.55161 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2513775f-4f61-3729-9759-6d78ebf9be3b | -11.18944 | -45.555 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 90fe6a43-f991-3614-9b82-5ee7ac5a1faa | -11.14808 | -45.53048 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d42d92f-f610-370f-9568-078b7af63b0d | -11.1476 | -45.53397 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 966a18df-4c81-35a7-8275-153df5939ef1 | -11.1447 | -45.55508 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a85dd4c2-908e-382b-a094-8d4e0c94404f | -11.14409 | -45.52987 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa6e9713-ce27-3628-9316-a38ff6b55555 | -11.14361 | -45.53337 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 68abff40-fea7-3ace-a536-071934e8e272 | -11.14071 | -45.55453 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce82441f-2927-3ec6-acde-dc1820225ccc | -10.91793 | -45.66124 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a26bd40f-a566-3a2d-bd08-71035eefbe67 | -11.27803 | -46.12587 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70406236-b985-34e7-8307-ecbd12ddd361 | -11.27738 | -46.13056 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e20c0fb2-7cd8-3f42-a1a7-c679145949e6 | -11.27355 | -46.12978 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b0d01f4d-afb0-3170-81bc-e311283a0ebd | -11.27036 | -46.12445 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 14ff0566-30f1-3551-9e96-52a388f84bd0 | -11.26972 | -46.12906 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bdc2872e-fb8b-3563-9cc9-97e5db933ce2 | -11.26862 | -46.12256 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f18f4f7f-3d9e-3c86-9790-91ada95c1819 | -11.26795 | -46.12714 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27dde570-d7e9-3382-9a15-b61a0440714b | -11.26652 | -46.12382 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 09b45e5e-89a4-3f08-9a05-4dfd750fb0ae | -11.26587 | -46.12843 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b8ed3e7-9010-3361-b981-2dfaff44e8ed | -11.26478 | -46.12192 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a9b82f00-d93d-361d-9ae4-5df8ab2820a7 | -11.25499 | -46.12188 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3bfad7b-f34d-343e-9c79-724bd78b6af0 | -11.25326 | -46.11999 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c15f5d7-fcbc-3173-b75a-dc7c6f342527 | -11.25008 | -46.11476 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f44edcd-6ae5-3c77-9e11-157670480e2d | -11.24941 | -46.11943 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c815399-a71c-3c1d-99ec-7d383a040448 | -11.19102 | -46.03098 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04f1da62-3606-3fd3-9c49-c16e7aa30055 | -11.18716 | -46.03027 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README87.md)
