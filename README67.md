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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6a4aa4a-d36b-3e5a-90c2-dd39ae19c72d | -1.21272 | -51.76056 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33ceebb-3bfe-3d75-8fe8-8656e159a275 | -0.96104 | -51.73324 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99bbb359-d838-3dd4-bf46-468eb1089b9a | -3.04785 | -54.41022 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7530ab3-be86-3c85-996d-d3b810f276f4 | -1.00665 | -52.44957 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e87e9890-2a8c-3b63-b2c5-75da1ca5bf1a | -3.1971 | -54.32106 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd440601-e06a-3f74-86c1-921ce33b412e | -1.99537 | -46.60763 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5f951dd-3cb7-3e84-84dd-82503b34a802 | -2.928 | -48.33521 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa951d87-93da-321b-8361-fae78c5fa7a3 | -0.95801 | -51.72448 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dae1e3cf-d980-3902-97a1-3aca56140e85 | -1.25198 | -51.77783 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 570218ae-b684-30dc-a320-0716743b6b33 | -3.06519 | -53.28077 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d474ea90-b484-3414-8adc-294bfead84b1 | -1.41644 | -54.91727 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f321bef-1a91-3c9a-a8ee-b2f310d8a8ea | -1.31934 | -52.39931 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 71cb1fc4-8977-3413-b37b-50143ce80ccc | -1.99648 | -46.60585 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a8b4d3b2-5b70-3c13-bb8b-c8a2e05393b3 | -2.00223 | -46.60384 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70404021-37db-3e4f-9ab6-6d6db3777ea6 | -3.1189 | -54.305 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a0adf62-4d12-3df6-83db-ed8f3f3725d0 | -3.77915 | -53.96306 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e6b8d9d-69e3-39f7-90de-b9b8da71adac | -2.92556 | -53.07366 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 77eb4801-e849-31d7-b65f-a274016c4a0e | -1.30934 | -52.40915 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3be8b96-87a8-3e57-b1ae-4e9109cf63b5 | -1.62605 | -52.61718 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d6a5a7f-1c6f-37e8-9f29-5b4bc7bd601f | -0.96202 | -51.78297 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e13dbce8-ffb6-3eeb-b352-5c744a2ea4cd | -3.66063 | -54.65522 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 651e2300-c883-3e53-bd8e-e21a3e931378 | -2.13271 | -48.53236 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48682555-ab61-3d5f-97f8-3b6a07a5fef1 | -3.7622 | -52.14311 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46ed03c5-f76f-3633-b61b-011396108817 | -3.88186 | -52.24479 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a3a98d4a-4422-3034-916e-6f8de954f752 | -1.54328 | -52.27125 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4715c9f1-3806-37c0-ba9a-72c235012e92 | -1.39039 | -55.17733 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae2e5f92-7449-37b9-b8b9-8d0243020197 | -2.28033 | -53.64 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a58c7bf-6ebe-30c7-b1e0-215b427f9516 | -1.99607 | -46.60283 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9380096b-f867-38b9-b06d-5c5f1c06ecb1 | -1.90227 | -53.33381 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d535163-3406-3613-8fb6-13fbcf1301e6 | -0.09794 | -51.40853 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ac3bd5-453e-371a-9c11-bbb6189084c2 | -2.82123 | -54.09828 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2035029d-bbdc-3c34-87aa-f45388a090f5 | -3.45583 | -53.30449 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 285e4571-f808-39f8-86ab-0103d233e2b6 | -2.97517 | -49.2922 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c196a829-48da-32fc-867c-5a8a7e067e42 | -2.95951 | -52.46053 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51a193f9-fd2e-35ec-94fd-386fc0ba7cea | -2.35831 | -48.60609 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c960dd85-c6e0-352d-9fc5-d708054cbf55 | -1.2678 | -53.40984 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e479880e-460d-39d7-b4e1-4c620a798033 | -3.34234 | -53.31231 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ac29fb-eceb-3c5b-b0c7-7d37a2f0af19 | -3.31244 | -54.1771 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e372639-9ccc-3a6d-ab9c-1ba4f291c5a8 | -1.25841 | -53.3689 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| df7aa182-3aeb-3aa6-a332-11311f4a4e6f | -2.74273 | -54.05561 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dcdff9c-c2a1-3ed8-800c-d46468d74c75 | -0.08779 | -51.4742 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c3e8e4c-6cc2-338b-b869-9674a36584d3 | -1.13858 | -53.66437 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b978a83c-5263-3d36-a910-088d97f78f71 | -1.47799 | -54.44865 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec34f9d0-7f3c-325c-a10e-4ef7f59fbd52 | -2.21227 | -53.71074 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0441147-f736-33d7-970c-aea414b7b1f9 | -1.07485 | -53.64944 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53d8b189-0ca8-3d0f-8e87-aa6bf28a1d2a | -2.3511 | -48.60861 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dece868a-88f1-36e9-aa99-4143fab8f89b | -1.22799 | -51.79078 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 190c2f44-78aa-3c78-9359-454477adb249 | -3.33887 | -53.30825 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3f8b54a-1af5-3b57-9a98-533c2921babb | -2.41618 | -45.82476 | 2024-11-20 05:14:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 124640a6-9ab4-36cf-8d53-a365ddad8897 | -1.21448 | -51.79289 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4697b51e-5cef-3bb4-b350-bd37d8d8c926 | -1.75202 | -52.37495 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf5f47c5-c5fc-3fdb-8276-4d91423071c3 | -2.75189 | -48.57384 | 2024-11-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac46fafb-c7ca-312c-a8a0-f417ad52bc59 | -2.86631 | -51.78833 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6faf1a5c-7a04-3d8f-ab77-e51c7649081a | -6.24885 | -47.27539 | 2024-11-20 05:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c658965-c705-3170-a092-5a1b0243c960 | -2.22325 | -46.47723 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f2bd7d6-8d34-3958-ae5a-2f3c19871661 | -1.23986 | -52.02485 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d0b2eca-4dab-308c-80df-63a2f313b013 | -1.25135 | -51.78189 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e60ec982-630b-3c9a-9821-80d3018a8f04 | -2.90421 | -51.77639 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 653b671b-07a5-3f3a-b352-be6c289e8889 | -3.37723 | -44.42801 | 2024-11-20 05:14:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6f81635-cab0-3578-9beb-81e4188af031 | -1.07506 | -53.36796 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9f09b63-5f54-3c01-806b-8304e14becda | -3.72607 | -47.37208 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c307bf47-a037-3bf5-a61b-7432ee9ee936 | -2.80561 | -51.80232 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c118501-03c6-3bd8-9e0f-635f40bca374 | -2.92797 | -49.42741 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0337edca-acb7-38e9-b414-de25a49b13ad | -3.38723 | -53.26945 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 949b6cf5-25d9-3cf1-9336-ddde1ee73e62 | -3.00072 | -49.19137 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 232fa7ad-303c-3b48-a229-c5322804c9d9 | -5.41892 | -47.39811 | 2024-11-20 05:14:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a85b740-30f3-303c-9896-d0abb461db65 | -2.75268 | -54.0666 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8c580df7-58f4-3f4a-ad87-c8864eb6762d | -0.19352 | -51.63031 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eb48a09-c61c-36cb-a3e5-0aa528d4684a | -1.78689 | -53.60728 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86d3c849-7dc3-3fe3-baab-312989e87616 | -3.51212 | -53.799 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5174f53e-d651-3692-bfb8-b9a62fddd962 | -2.25125 | -53.67506 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aaf48e7-68c7-3ffc-95aa-a5f8dc696a22 | -2.91449 | -53.06488 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1f9ffee5-dc5c-35a2-a90f-1dc662bc64f1 | -1.70846 | -52.49086 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78e602a6-ca99-37f1-89e0-d3d941e7fe0b | -2.868 | -54.47983 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0d893ae-51c3-34c5-aa18-f815d4cdeffb | -1.64406 | -52.60878 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2f5ec17-f3e5-3ee5-9f0c-e1d2c28127bd | -2.25437 | -53.68042 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f4bff17-cf98-31e7-9540-d6ec0f647122 | -2.8474 | -54.00264 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb8949aa-2b6b-3919-b691-0f81f2d03dd5 | -2.00153 | -46.6086 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0f056b6-1161-3aca-bd6d-92a2bb3e3ef7 | -4.05911 | -46.84504 | 2024-11-20 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7068a04-1901-3f95-b888-861ad4295056 | -2.83076 | -54.00965 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 464a2f37-9e95-3500-adf9-ed16dab982bc | -0.9003 | -51.72808 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9ec3d9c-4ad1-3c59-9de9-1ace4878b305 | -1.47768 | -51.97105 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5dae96c-3a0b-3a8f-9b4c-67c530b8541c | -1.85661 | -54.27607 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 6baa381b-5981-339f-852a-066c7ff16daa | -2.94213 | -54.80293 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c89c7bf0-c9c3-361c-b1be-3ed5f6c0236d | -1.7367 | -53.0312 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e65f6d0b-0c97-3ae0-8db0-995efc86eb03 | -2.99543 | -49.19057 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aa885e2-f222-3964-814f-492d68520c16 | -3.19744 | -54.32358 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68a358a3-cc2f-3765-9fe1-3b1be5d85969 | -1.6676 | -52.80687 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d85ee6a-d82f-37d4-8223-9162e4576ed1 | -2.89996 | -53.05163 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5ca1d1-6580-3083-9472-9f9f9b1b225a | -2.21942 | -46.48873 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| faafccbd-fb6d-3369-b77d-130aec1f3b63 | -1.21265 | -51.74681 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7abfd394-a295-35be-998e-c8861d46ba41 | -3.81223 | -47.80393 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 266859ce-b75f-34b2-a4dd-4b657a206f41 | -1.78466 | -53.60919 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c597ecd-48cd-3baa-833b-c3f9e2b14d93 | -4.07919 | -50.03614 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f4fdf2-5d7f-3c59-b6e2-74f4765c98b9 | -2.918 | -53.06902 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 154f8427-b07f-3e8b-a75b-14b27ff72378 | -1.86652 | -46.80163 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c2f6e54-4bf0-3e02-80f6-72ebae8c7bdb | -2.34303 | -54.77993 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9da5a76-afa8-3bad-b47f-50b3a7f226db | -1.06179 | -51.75168 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f755ff9-0dd5-329e-95d7-c61355240e47 | -1.64725 | -52.6427 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af14c37d-6d5b-3709-9ed4-f52c61c5844e | -3.48013 | -50.3121 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README68.md)
