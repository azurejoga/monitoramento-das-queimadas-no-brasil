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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28c9f5c2-2378-3086-a033-061b63797f03 | -22.70391 | -48.27076 | 2024-11-25 03:44:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80d45a79-c509-3987-b8ce-699685caca2b | -21.93615 | -46.23256 | 2024-11-25 03:44:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d393dc6c-114c-3728-b9ef-89d2b0fa274e | -20.2504 | -49.68106 | 2024-11-25 03:44:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b00f778-8900-3f44-befa-81cc2e0f95b4 | -20.76455 | -46.7728 | 2024-11-25 03:44:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3834ee8-21f6-3edd-b11b-1754f98782e6 | -28.27997 | -52.82121 | 2024-11-25 03:46:00 | NOAA-20 | CARAZINHO | RIO GRANDE DO SUL | Brasil | 4304705 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 37941a1e-41c4-3ece-8271-d189af2f917b | -28.58403 | -49.4424 | 2024-11-25 03:46:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 792bdf14-98e0-348e-90e9-e4cd9fb82e3c | -25.1961 | -49.32449 | 2024-11-25 03:46:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2b3a9ea6-36f0-3510-84ac-4615454a817a | -23.65718 | -47.66315 | 2024-11-25 03:46:00 | NOAA-20 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5eb1dbf-6f46-3926-8cbd-8cbe89728238 | -25.18951 | -49.32968 | 2024-11-25 03:46:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2688a730-4098-36fb-bd86-2d24b71f689a | -28.58644 | -49.44238 | 2024-11-25 03:46:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 729bf56d-8380-3ed4-b91a-191460f76cfe | -3.2928 | -45.7384 | 2024-11-25 03:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 64e167e8-0642-3c7e-b675-9b94cfffb2e5 | -1.7726 | -52.7379 | 2024-11-25 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 9ec1d244-7fca-3943-9bf4-4717f6f10ddf | -4.2604 | -48.7184 | 2024-11-25 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 41164615-fd61-3c8f-9e9f-1fda6e0403f2 | -1.7726 | -52.7379 | 2024-11-25 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f22fe4c8-dbe1-3bb7-a4aa-7f67041b6ca6 | -4.2604 | -48.7184 | 2024-11-25 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 741cfcf4-7378-3f23-bd90-89fc02e759dd | -4.2604 | -48.7184 | 2024-11-25 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 90c8f2ab-9264-33ea-9124-fdb4f0486bd8 | -4.2604 | -48.7184 | 2024-11-25 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5334e841-bc9f-3d6f-8235-c2cea389eab5 | -4.2604 | -48.7184 | 2024-11-25 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b7ba13de-b8ee-349c-a71f-05952684ed14 | -0.96187 | -51.78268 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e75b2324-d11d-3507-aef0-a52a66b765c3 | -1.33974 | -52.24637 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fdcda08-3382-381c-9c5d-d8a7c2668f94 | -0.91337 | -51.64965 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39c2e2ce-2e93-3d0d-a6d8-2c9c8f4f4cc2 | -1.9813 | -46.42796 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea66450-b873-3b9e-9f20-2d51eb555e2c | 1.33501 | -50.61937 | 2024-11-25 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 016d49d7-0b52-3b76-b4d2-f9a05ab2cee6 | -1.27714 | -52.16958 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa695619-629d-3a9a-a69a-96a8fc158efd | -0.80875 | -52.83116 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 154c7012-71e2-3d74-8ca8-dd609d27bd4a | -0.98394 | -51.71902 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2495b8c6-92cb-3339-a52b-68d4fd3a3e59 | -1.25622 | -51.74621 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80baec57-e700-3abd-821b-5959d9457bcd | -1.24989 | -51.7864 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3f3cb5f-cc2d-3924-92e8-7b528b4fcc2c | -1.22327 | -51.79983 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d122442-c2cb-3d80-aeba-7523eebdaff2 | 1.40518 | -55.88579 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a056ba-a71b-3d09-a33b-ddce3646ba9a | -1.12413 | -52.3955 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5477b390-e0a4-34a2-8a2d-b29f651b2176 | -1.20703 | -51.74826 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceeb5771-7767-3f15-be21-1fd01f1e960d | -0.35637 | -51.97716 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0e2b5b6-5700-3893-94ae-d3ab4299b946 | 0.97669 | -50.12524 | 2024-11-25 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bc1455e-2f52-3438-a977-8ac701991451 | -0.95552 | -51.71818 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e19b585f-f871-3171-aa67-2b02a1da4850 | -1.29771 | -51.73379 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 714ccf03-d60c-395b-818f-1ee5ba139805 | -0.9898 | -47.22368 | 2024-11-25 04:31:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e871f61-d155-32f2-8ef9-686670683b66 | -0.87762 | -51.72029 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f049116-f8d4-3c84-bf1d-562ea5ff5921 | -1.11415 | -53.39227 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76931243-ce9c-344e-ad85-7633f0ad53c7 | -0.39434 | -51.4487 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e76ca43a-0900-39f8-80db-a42d9ad133d4 | -0.98338 | -51.71236 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a99ca4c4-65e5-3fb5-aaa6-19e859cdeefb | -0.8816 | -51.7209 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16cbaddd-a2dc-3ab3-a15a-e1ceba1f2beb | -2.20946 | -46.36056 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f4a62ed-4fed-3019-a562-e9299f1bbbba | -0.30225 | -51.39632 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d9698c-a6fc-3148-a326-033cd10a35c1 | -1.04436 | -51.73927 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ab5d802-6b1c-361f-bd7c-704a50014c8f | 0.33408 | -49.71947 | 2024-11-25 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58d7e7a6-9b59-3160-a92f-1a9e9eedaa6e | -0.21079 | -51.18678 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ec36352-e54f-3738-aef3-e1b1f55f42b6 | -0.90544 | -51.64843 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb86224a-3213-3402-96a1-c472d33a316b | -2.00975 | -46.50673 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 870bcb0b-a2fc-314f-b403-7651078d261b | -1.29515 | -51.7313 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f1f945ef-ec12-3900-a3ae-40111a540d73 | -0.34751 | -51.54774 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d43560b-5af7-3220-9a33-3bc38d9282bb | -1.86122 | -44.82381 | 2024-11-25 04:31:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9d2b26c-dd2a-31d8-88e4-7eee52c737ea | -0.93108 | -51.71792 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 020b0f7b-1f85-3bd9-86e2-dc7525b53daf | -0.28105 | -51.60778 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| df50c642-5a28-38e5-b392-b9fe3f30411c | -1.30564 | -51.73501 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85baf4cb-a81d-3903-9216-0730629d6212 | -0.97704 | -51.71092 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d9a2206-bb88-375c-8cec-83e9d807867c | -0.98447 | -51.71558 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcc74d4a-eef0-3ecb-afbf-0753579f0b4b | 0.59442 | -51.57693 | 2024-11-25 04:31:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1319b55a-7cbd-3f76-9f8c-8794beca7951 | -0.89357 | -51.72273 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4c42192-25fe-3c78-9927-e76af8575462 | -0.95862 | -51.64612 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36a93aa1-299b-3b48-9819-4e7f8949dde1 | -2.21896 | -46.38692 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 133e33d8-54b9-3a5e-b16e-a48e6ffc4ccc | -1.23685 | -51.79142 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 946eefd6-a4f9-3d19-bda6-2f4b38f908be | 1.3838 | -55.89642 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a0b5606-8bbf-3bb1-bc0e-8ec470cabc00 | -0.2585 | -51.64682 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0057085a-f28b-3beb-ad81-fd8169791a24 | -0.21468 | -51.18739 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 14ae5690-ff2e-360c-b8c7-7f12acba7eb9 | -0.99311 | -51.72793 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f6e4316-602c-3dcc-92e9-b3ad3126a93d | -1.8618 | -44.82002 | 2024-11-25 04:31:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 212932ec-11ef-3e01-9815-01eed6222db0 | -0.27542 | -51.61753 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc9a0e9b-9992-3609-97f8-6ca2f5d2e5e3 | -0.96854 | -51.71316 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2738e0b-fa78-3fb9-a34b-918a9da3d4ab | -1.15164 | -51.69577 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd463afa-b954-3f40-93ef-841f7273f944 | -2.2273 | -46.39888 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d23e678-ede0-34d5-a31c-ec8bfc1eafd7 | -0.23889 | -51.61551 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12fca891-2779-3fca-b8e7-18f02631b038 | -0.98341 | -51.72247 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c1de4f0-135e-3788-a04b-e61022b43a77 | -0.90941 | -51.64904 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b97d8762-4d75-3473-a794-fb8d6e25f4e3 | -0.75586 | -51.73902 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6db0825-02d1-3361-90d7-298ba6b17db2 | -1.13551 | -48.35881 | 2024-11-25 04:31:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad7fd322-4b3b-3bb6-9fb1-598f4b002bbf | -0.31914 | -51.59947 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26163a8b-74f5-3346-b456-9cbf38092c39 | 0.32213 | -51.07312 | 2024-11-25 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abff6e4c-fa55-3294-b40b-d2559d8f1575 | -1.19633 | -51.7641 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a71315-0d7d-331b-b387-eb1752ff8b16 | -1.07131 | -53.17585 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76ce8487-9605-3507-aab4-4993d3602199 | -0.92293 | -51.64066 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 309244d4-0884-3e23-afad-1ea734ae7403 | -0.75986 | -51.73964 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bade8da1-6855-3e7b-b506-50925d5f18f8 | -0.57785 | -51.71155 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1947a572-3f01-3ddc-b080-7ae0fc1c5c69 | 0.72068 | -50.86027 | 2024-11-25 04:31:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eab84126-909b-3724-acdf-5a2bf498d8aa | -1.19688 | -51.76069 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d96ffd-9d53-357e-a4dd-767ab30a82f9 | -0.24345 | -51.61266 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac1c3c4d-335d-35c3-898b-f735c56c8901 | -1.31024 | -51.73884 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97fd93b8-a3a3-3ef8-a387-0fb3bb75278e | -0.27887 | -51.62162 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38826a7f-6579-3502-ae72-5075bb2023fc | -0.92698 | -52.65322 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd13fa65-1ecd-36a1-94ce-b6c654169da9 | -1.19256 | -51.77283 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce918797-347c-3d4d-8fe9-b5df852f06d3 | -0.6275 | -51.70852 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63785614-948b-3c0c-b307-b8269343d4e4 | -0.05554 | -50.82084 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cd062103-5d8c-381a-b1f7-99be387d8757 | -1.06666 | -51.75328 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed80ff31-b016-36f1-a45b-562885a58f35 | -0.27597 | -51.61409 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2345222d-ec3e-3143-ab25-9ecbce030e9b | 0.33277 | -49.72269 | 2024-11-25 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c44763a-59e8-3aef-894c-45f09bcad561 | -1.21252 | -51.73948 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3197f5ba-67c7-3d3c-9deb-5b4910c7b02a | -1.31591 | -51.74701 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1bcbbcd2-096d-3519-85c2-a3d20936567f | -1.25442 | -51.78358 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7269f0b5-f74a-3aa0-8b4a-a7ee5b392897 | -0.36628 | -51.54842 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f164e88e-e46f-3088-bddf-0d85c519848d | -1.67113 | -46.05934 | 2024-11-25 04:31:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
