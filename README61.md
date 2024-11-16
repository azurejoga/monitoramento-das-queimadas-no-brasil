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
| b82b5392-8670-3083-8497-6aa361b37ea2 | -17.6657 | -57.5439 | 2024-11-16 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 5fb374e7-f0c5-354e-8db7-a52f4b172d36 | -17.6063 | -57.5715 | 2024-11-16 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| d947e972-ed97-35d0-a985-0491ea4f2f1f | -17.5865 | -57.5739 | 2024-11-16 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 2c620722-da23-3a82-bab0-fe0296c7b62d | -17.5865 | -57.5739 | 2024-11-16 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 182.8 |
| 84231583-0931-3ac1-a2b9-aae74f8d59f5 | -17.5862 | -57.5944 | 2024-11-16 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.3 |
| bf31e0c9-0892-38da-bbf3-429ea3ec710c | -17.6059 | -57.5921 | 2024-11-16 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 80081e7b-277a-324a-b4f6-090e492f238c | -17.6063 | -57.5715 | 2024-11-16 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.5 |
| 632f4f4e-5233-3650-9778-e7a03e30be8c | -17.6848 | -57.5827 | 2024-11-16 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 1a7e7c6e-83da-3ca3-b156-410ea6ec604a | -17.5865 | -57.5739 | 2024-11-16 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.2 |
| 48448ab0-2791-3475-a2a2-bc2e0b60ec87 | -17.5862 | -57.5944 | 2024-11-16 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.6 |
| a0e6c408-1dca-3f99-8c08-fa3d19b3a82d | -17.6063 | -57.5715 | 2024-11-16 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 02b6b09a-1a5f-3ee4-b2ec-170bdee41a5c | -17.5862 | -57.5944 | 2024-11-16 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.8 |
| f0ce193b-7fc6-386d-a3ce-b28a9a2ed672 | -17.6063 | -57.5715 | 2024-11-16 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.9 |
| 6f4e754f-8b29-3344-8ecb-89c9b10278b6 | -17.5865 | -57.5739 | 2024-11-16 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 191.2 |
| 85cf1a9b-fb20-39e0-8ae8-0665e584aac7 | -17.5862 | -57.5944 | 2024-11-16 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 0970a44a-60dc-385b-822a-b81eeb388600 | -16.958 | -57.6269 | 2024-11-16 10:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| c2543590-2008-3861-ab08-562f626253d0 | -17.6063 | -57.5715 | 2024-11-16 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 4b9ad229-b7de-3e4c-97e4-14b036284533 | -17.5865 | -57.5739 | 2024-11-16 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 201.2 |
| 47c96a11-794d-395b-bc06-b3d9ce8ec4fc | -17.6657 | -57.5439 | 2024-11-16 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 8b02cb83-9d01-3036-9acb-7e7908ed3116 | -17.6063 | -57.5715 | 2024-11-16 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 193.5 |
| f5c7a26f-8b42-3c6a-ad59-cc325e499cfa | -17.6059 | -57.5921 | 2024-11-16 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 3479f3a7-6d79-3f39-b4cd-bd83088280be | -17.5862 | -57.5944 | 2024-11-16 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 87619e4c-c17d-3cf6-9f79-eff64bb8461c | -17.5865 | -57.5739 | 2024-11-16 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.6 |
| 98af8cdf-15d3-3076-a1f6-3368185be59e | -16.958 | -57.6269 | 2024-11-16 10:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| 9910a0e1-cdce-311c-a373-a58ecc15f4ef | -17.5862 | -57.5944 | 2024-11-16 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.2 |
| fe346107-7e3c-3db7-8229-f8e4f6c1e7de | -16.9384 | -57.6291 | 2024-11-16 10:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| e313f197-3a2f-37d9-bea8-14568f680c7e | -17.6059 | -57.5921 | 2024-11-16 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.1 |
| 0249cef0-34b3-3633-acf4-e87da6a22847 | -17.5865 | -57.5739 | 2024-11-16 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 183.3 |
| 39bd3849-49cc-3b64-b199-7a59d3bb7b36 | -17.6063 | -57.5715 | 2024-11-16 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 164.7 |
| 0f7287c2-f541-3e98-a031-1ab940089e79 | -16.958 | -57.6269 | 2024-11-16 10:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| aced69ba-f92a-371e-8674-1c0d07ada6dd | -16.9384 | -57.6291 | 2024-11-16 10:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 850dde57-1194-3b59-b75e-a50daf969ec4 | -17.6059 | -57.5921 | 2024-11-16 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.3 |
| c3706f1d-a62c-39d4-ac10-6fb7c552c8d6 | -17.5862 | -57.5944 | 2024-11-16 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| dd5de07e-828c-3ef6-b435-f64d26fdabe8 | -17.6063 | -57.5715 | 2024-11-16 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.6 |
| fd4e2067-d448-3d38-8823-5373833a07f6 | -17.5865 | -57.5739 | 2024-11-16 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.6 |
| a093068f-1f79-3082-9897-c03988bfbc74 | -16.9384 | -57.6291 | 2024-11-16 11:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| a61b4c63-9d74-3e33-80a5-ee380e725c1e | -17.6063 | -57.5715 | 2024-11-16 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.1 |
| eaf5774f-297e-38fc-af39-0ee76a4afcbe | -17.5862 | -57.5944 | 2024-11-16 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| e15b3c30-e18a-35a6-82e2-2ad47eb701c0 | -17.5865 | -57.5739 | 2024-11-16 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.3 |
| e6579248-f68d-319f-9f0e-c28d05bfa98d | -16.958 | -57.6269 | 2024-11-16 11:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.8 |
| c00718c7-abd5-3938-8bc9-313d533f9880 | -17.6063 | -57.5715 | 2024-11-16 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 6f6d1f9d-e075-305d-8daa-126a42d6f453 | -17.6657 | -57.5439 | 2024-11-16 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| acbfe55c-fdf4-36d1-99a1-4a4ab13658ac | -17.5865 | -57.5739 | 2024-11-16 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.2 |
| 7a080087-36dd-3467-ad62-9a816439b3b1 | -17.5862 | -57.5944 | 2024-11-16 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.3 |
| a819a2d8-5b8b-3b0c-9ecf-ec96a1ddb5ea | -16.958 | -57.6269 | 2024-11-16 11:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.4 |
| 66abb0ba-f90f-323f-9026-92215374164f | -16.9384 | -57.6291 | 2024-11-16 11:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 453ec477-ad37-3597-9588-b9655b997d28 | -3.4787 | -42.3058 | 2024-11-16 11:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 158ac71a-0166-3ba1-861a-d56f4456d2d8 | -17.6657 | -57.5439 | 2024-11-16 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 10875a16-e92b-3937-86c3-193c2d26224b | -16.9384 | -57.6291 | 2024-11-16 11:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 251f0b4d-7453-353e-a805-1ccdc2e5f881 | -16.958 | -57.6269 | 2024-11-16 11:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.5 |
| 2046de76-2c10-32da-8094-2ea6c4718b8b | -3.4787 | -42.3058 | 2024-11-16 11:30:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| f334da95-50f7-3eda-83b7-3529c582405b | -16.0466 | -60.119 | 2024-11-16 11:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 28ea6707-d75d-3fea-8189-d1772ceb4c4b | -17.5865 | -57.5739 | 2024-11-16 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 0fb22303-601d-3d90-9bf2-d8f54815752d | -16.958 | -57.6269 | 2024-11-16 11:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.2 |
| d2621166-2178-3129-b61a-dfd27d1393a8 | -17.6657 | -57.5439 | 2024-11-16 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 28f3f061-edea-3f41-80dc-4fe872be1bb6 | -16.9384 | -57.6291 | 2024-11-16 11:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 7ee25c4f-0bd3-367c-be17-3b51c9f16523 | -16.958 | -57.6269 | 2024-11-16 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 42085c5d-b606-38c8-ae88-644378db508a | -0.9334 | -47.7768 | 2024-11-16 11:40:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 596e59e5-ec6f-3310-a22e-89a749df2a96 | -16.0466 | -60.119 | 2024-11-16 11:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| a89643d7-34e2-3e01-8c02-112f1f8e14ba | -17.5862 | -57.5944 | 2024-11-16 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.6 |
| e1ad8487-db27-3d38-951a-6ed4ced8683c | -3.4787 | -42.3058 | 2024-11-16 11:40:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 73330723-b1b8-3c9c-8b20-05ad9d4bae09 | -16.9384 | -57.6291 | 2024-11-16 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| ae6284cd-079f-31ae-885a-305acfeb8e0c | -17.5865 | -57.5739 | 2024-11-16 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 176.5 |
| a89bd6ab-61ac-3367-8ccb-a1ba924ba43f | -3.3673 | -42.1691 | 2024-11-16 11:50:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 796f67da-bf6f-3436-8690-5dc73dd85147 | -3.4787 | -42.3058 | 2024-11-16 11:50:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a98f6d04-80b5-3bbc-8dd7-350c6dadc96c | -16.9384 | -57.6291 | 2024-11-16 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 6a477723-4ebe-3526-b99d-4bdf53f637a9 | -17.5862 | -57.5944 | 2024-11-16 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 834eddb9-8dfb-3faf-a4ad-0e542277e93e | -16.0466 | -60.119 | 2024-11-16 11:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| d4d2eb86-1d34-337c-9b5d-e83a6fa0fa2e | -17.5865 | -57.5739 | 2024-11-16 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 227.7 |
| 424f3e15-a9fb-3f97-bdea-3c8172540d31 | -16.958 | -57.6269 | 2024-11-16 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.8 |
| 946f60ed-b4dd-315d-ad86-e9f42866e8eb | -3.4787 | -42.3058 | 2024-11-16 12:00:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 76f1379b-c373-3214-bae2-957491c09438 | -16.0466 | -60.119 | 2024-11-16 12:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| cac3d458-7c19-30d0-bf01-9b6279529bd5 | -16.9384 | -57.6291 | 2024-11-16 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 1985e665-b89c-3773-99af-059caff3c64e | -17.5865 | -57.5739 | 2024-11-16 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 236.7 |
| d87ab711-0b47-3103-a256-b87f6f550ab2 | -16.958 | -57.6269 | 2024-11-16 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.5 |
| cda98ce1-af1f-3288-b401-cd41580cb15f | -17.235 | -57.4516 | 2024-11-16 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| c3c43929-7c2e-31d1-a40e-ffa3143c74a9 | -17.6066 | -57.551 | 2024-11-16 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| a2650edb-e4c4-3c5f-ad7a-59ab22684aae | -17.5862 | -57.5944 | 2024-11-16 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 173.3 |
| 31999586-bffa-3ba2-b636-2ab8ca5f87cb | -17.5865 | -57.5739 | 2024-11-16 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 274.2 |
| 205b9b7d-6e7b-33be-b827-d0385827fbd8 | -19.5426 | -56.908 | 2024-11-16 12:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| c96a0bdf-b16e-3554-b32d-1e979e176fe3 | -3.4787 | -42.3058 | 2024-11-16 12:10:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8ef7181e-f272-3694-a9db-edd39fc4b0c5 | -3.3673 | -42.1691 | 2024-11-16 12:10:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 8b03caf7-1614-3854-bf1a-28d2aedfd87b | -16.0466 | -60.119 | 2024-11-16 12:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 201.0 |
| 75c04824-e83e-391f-aa51-454a06abe0db | -16.958 | -57.6269 | 2024-11-16 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 3f79c4bf-ba1f-34fe-8d10-6f97a2d94c10 | -17.6066 | -57.551 | 2024-11-16 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 7f68bf90-47f2-30b7-b05a-c128a224e2b4 | -16.9384 | -57.6291 | 2024-11-16 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 96fe7069-bb90-324e-b37f-4f0c71bb9953 | -17.5862 | -57.5944 | 2024-11-16 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 184.7 |
| 8b27bfad-5880-3a95-b5db-007889deee3e | -16.9577 | -57.6473 | 2024-11-16 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| defa3e0c-4fd9-3731-8cd9-6d199b3d6d13 | -17.5862 | -57.5944 | 2024-11-16 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.5 |
| 424f11c5-ef2f-3f76-97c4-f06bd1dfe651 | -3.4787 | -42.3058 | 2024-11-16 12:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 19fa44f7-5c6e-3e8f-901e-eec21eb3d2a6 | -16.958 | -57.6269 | 2024-11-16 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.2 |
| 69d21688-c00d-353a-948b-85db1b702ecf | -17.5865 | -57.5739 | 2024-11-16 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 265.8 |
| eaba6907-8789-3753-a66a-bb963ed6a3be | -17.2547 | -57.4493 | 2024-11-16 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 3f04e42f-c0c9-329c-ac13-4f55c1f35c74 | -19.5426 | -56.908 | 2024-11-16 12:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 00b93320-278d-3fa1-a811-0ec568120170 | -16.9384 | -57.6291 | 2024-11-16 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 7a676088-e967-370b-b894-0693164859bb | -16.9577 | -57.6473 | 2024-11-16 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| ee067060-8ffa-35a0-8a41-d4f6bafca90d | -16.0466 | -60.119 | 2024-11-16 12:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 206.9 |
| 53eb9320-69bf-3892-8c69-241dc0515b95 | -17.235 | -57.4516 | 2024-11-16 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 52d35fcb-9255-39ca-9d6b-7e0b8b929acb | -16.9384 | -57.6291 | 2024-11-16 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 74359f5b-b245-3429-9cba-4d252f296458 | -17.5862 | -57.5944 | 2024-11-16 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.4 |


[Clique aqui para ver as próximas entradas](README62.md)
