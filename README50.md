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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f812ea8e-8518-330d-bc9a-1f50e7f2c7b6 | -1.70373 | -52.5389 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e257b191-fa85-3601-ad38-c5c9ef0349cf | -1.70319 | -52.54235 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7825000d-6ef8-3f24-b834-294126a1b880 | -1.70265 | -52.5458 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3754a18-8bb5-3925-aca7-6cab2f9494d9 | -1.70197 | -52.50677 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db923038-30f2-3382-b42e-07492ecabb6d | -1.7015 | -52.53148 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b67dd6-3807-3cd2-8836-0d849c41870e | -1.65663 | -52.05736 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7490dfa-67ca-3381-b26e-af33e6fb8e6c | -1.65608 | -52.06087 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3cf450c-e410-3b2e-a49e-e092f32e9256 | -1.65329 | -52.05684 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ae3baaa-76c6-35d4-9550-8789ff0f4d19 | -1.64995 | -52.05633 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7626f57-d0fa-38b7-a8dd-efbf06afabd7 | -1.54195 | -51.96473 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c313fb75-c9d7-385f-8562-b48d10a0dcb3 | -1.5414 | -51.96825 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91980bfe-7795-3b70-9c43-32d9de8dd894 | -1.53581 | -51.96018 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d760f0f9-3943-3ab7-baba-2bd54b5e8898 | -1.53434 | -51.9525 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932dcf7a-e07e-3257-bb4a-4452c6e95f8f | -1.53323 | -51.95954 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 877a1e6b-478d-38b7-a2d4-9709f7b1d4c5 | -1.53267 | -51.96306 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2d5c1cf-81d2-394d-a283-49c426f007da | -1.531 | -51.95198 | 2024-10-20 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f224c06f-3bca-3474-a544-6a1a250705f6 | -1.9848 | -53.1922 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2068d58f-6435-3f02-aca8-9b7fedab4943 | -3.56161 | -53.0199 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d406071-9f2d-3a5b-9649-69e928d1e320 | -3.55859 | -53.10423 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b1515a1-be53-3185-86be-0870b4a2487f | -3.55805 | -53.10769 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a11e7df-a857-3183-a940-74d3d04e81eb | -2.79493 | -52.92449 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ade3e90-c767-389c-97d9-2d0a9620e5f4 | -2.79163 | -52.92397 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f0e83a5-5fd8-31ec-881e-574aaa983c5d | -2.74783 | -52.0514 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a97b19e0-0fdc-307e-b095-eb9cd238cc76 | -2.73765 | -52.57515 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 764a1caf-89ac-3e12-90f2-28fff4951622 | -2.73488 | -52.57117 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f03be753-c495-3178-b213-87a3327a3afd | -2.73433 | -52.57464 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d27ce48-7c33-3acd-8ad8-19cb3af9fabb | -2.69145 | -52.06909 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 51761bc2-44db-3deb-893b-87d4759ab966 | -2.69089 | -52.07265 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1265ab52-db00-3021-9eb7-58474e86e1f7 | -2.6881 | -52.06857 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea5307a5-b3ae-318a-84ad-3aa9663aed8d | -2.68754 | -52.07212 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0bef2344-68ec-350c-b154-27b49fdd19e7 | -2.66243 | -52.57771 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 590c29e2-55a6-34ff-9114-3b719efc69b4 | -2.31483 | -52.88857 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf6655c4-6f40-38fb-b07b-68b6d636d24a | -2.31429 | -52.89201 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6324f72e-85e0-3693-a550-297ae505bad7 | -2.30411 | -52.19698 | 2024-10-20 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf6e27b7-6f67-3d8a-ba8a-02dfe7941268 | -3.34019 | -53.54169 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b46bc880-c30a-3792-b893-d6fb4a6b596e | -3.28261 | -53.04297 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30a97fb4-a021-3c94-9df5-f75a68c9e112 | -3.28206 | -53.04642 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b38e1613-ffb7-323d-bd89-28cec0403207 | -3.27876 | -53.0459 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2612a294-1d45-3198-9027-64ac2b62b3fe | -3.27357 | -52.97085 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d055860-9f85-3b70-9a5a-b5d843946215 | -3.22419 | -53.37204 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baa2e263-59dd-3bbb-8d39-5172e5ef6408 | -3.1412 | -53.16557 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d997162b-203a-3424-a100-f566924bfe58 | -3.113 | -53.64658 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd28babe-b773-346d-9c4b-1705f5ca77df | -3.06387 | -53.24519 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e0db691-aaa6-352d-94d7-d8e020d4163d | -3.06057 | -53.24467 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bb25a6d-f05f-36dc-bfcc-da2ab55208f5 | -3.0578 | -53.24072 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef4a6ea0-39ab-3435-be33-db408c985364 | -3.05726 | -53.24416 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98c15297-5464-3bb5-a287-b5127efb575d | -3.0545 | -53.24021 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df9168c5-2729-3e9e-a188-2f2938974df9 | -3.05073 | -53.26425 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97cf465d-e7d3-3ec2-8d9f-76cf11e27654 | -3.04796 | -53.26031 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4798d94f-6759-3027-b41e-af5fcdfc71a2 | -3.04736 | -53.24262 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40968976-c8ac-3625-8ebf-1be0902f9f53 | -3.04405 | -53.24211 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce40138f-5983-3771-80fa-f208c4c93cac | -3.03184 | -53.03952 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f090699-c236-366d-a380-baaaec5e0e8f | -2.85587 | -53.33936 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00239765-49eb-30f8-8f33-0789f1f2a621 | -2.85533 | -53.34279 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b2785f9-9f2e-3979-a89d-70c313bec13a | -2.85365 | -53.33199 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca6ba040-87da-3670-a176-98f640df9fd5 | -2.85311 | -53.33542 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12298e8e-34eb-302a-afa3-774737aa5b36 | -2.85257 | -53.33885 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f272cab5-c7fc-340a-9e25-c41641e2bb4e | -2.85197 | -53.32117 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02514722-4f00-3247-9526-8e197d5d365b | -2.85143 | -53.32461 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a923efd-48c7-3783-8f08-441520963db6 | -2.85035 | -53.33147 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebff1038-f41a-3815-9d2d-991a875d6caa | -2.84981 | -53.3349 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdd3e820-92e4-39ec-844a-e872903b6c1a | -2.84927 | -53.33834 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71ff7e8e-d513-3dc4-8e9d-1729d11b2fc9 | -2.84873 | -53.34177 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80aa58e4-ac33-3f32-8ff7-af0a3c5a6774 | -2.84866 | -53.32066 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ec5c38c-ddb4-3335-b31f-4d3c66dddc2f | -2.84812 | -53.3241 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa8a79f8-5093-3dc3-bca7-721a1136cc73 | -2.84651 | -53.33439 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9af38fc8-756b-3604-92eb-5b88a04e3435 | -2.84597 | -53.33783 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25814ec9-4dbe-3274-83f4-decd6d6a9f8b | -3.38804 | -52.65151 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c56c1aff-0d9d-388a-aba8-c7a5e6c1bd10 | -3.01606 | -52.18749 | 2024-10-20 04:55:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8da9fba-5850-3208-ad2e-765cfe3406d4 | -3.01436 | -52.34657 | 2024-10-20 04:55:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbd6d7ab-940a-3b05-ab0e-ad019ad881c9 | -2.98314 | -52.85167 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e69ed9b-e905-3841-815c-4461db13eb6e | -2.98037 | -52.84771 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c5d5044-e22c-3e48-94e7-685b27c901a6 | -2.97983 | -52.85116 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bda41e41-ddc9-378b-8aa9-af5a124d2055 | -2.97929 | -52.85461 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e75a5e86-4ad7-3914-be47-f9667ccd5dcb | -2.97706 | -52.8472 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0b6a934-2eb3-3d9c-9496-64c3f5be6d6b | -2.97652 | -52.85065 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8a1208c-428c-3062-81d0-be86abab2d01 | -2.97598 | -52.8541 | 2024-10-20 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0270aff-06ea-33b1-9e32-d58485d6dbc5 | -2.96015 | -52.91182 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dfd940f-3e14-34e3-99ff-f4a5e6d8ac16 | -2.95739 | -52.90784 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a8f814c-7b99-32f1-9dfe-2aa8e88e3441 | -2.95684 | -52.9113 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2b06dc-3ebf-3ee7-ac56-d58c8d602e61 | -2.95462 | -52.90387 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19333da5-c481-3930-a824-7b66105ebcfe | -2.95408 | -52.90733 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22a1b39c-7760-331a-a0a1-c5ea2b576278 | -2.95353 | -52.91079 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 328dd83f-32c6-3c45-b097-b045eab677f8 | -2.95299 | -52.91423 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fda9979a-540c-3d48-9fc2-2f9511c9bb28 | -2.95131 | -52.90335 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d76af135-63d1-3d1c-835c-2e9208c4db96 | -2.95077 | -52.90681 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 949b06d3-d1a1-3018-950f-050809d26601 | -2.95023 | -52.91027 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 054d0203-2de9-3830-9a45-37982900b665 | -2.94746 | -52.90629 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 382bd2ef-edea-3e23-9658-a2f1d90ba1fa | -4.22156 | -53.75044 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b61133f8-4665-3997-95e7-d3491569695b | -4.15599 | -53.64859 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1656c5ea-a7c8-34c2-8531-aa21950ffd2a | -4.13519 | -53.50093 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68bee726-e3de-3e7c-9591-41f451fe0adc | -4.13465 | -53.50437 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5578296-9975-33f4-9992-05549c6382df | -4.13411 | -53.50781 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 933da018-cbcc-316d-b1fa-82ad9331c472 | -4.13096 | -53.74327 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4118f8be-9770-3955-a8a6-68a8e3139f16 | -4.12634 | -53.66509 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c57bb29-6bf0-31cd-a6d9-752fba5e1bce | -4.12303 | -53.66457 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b18e26-71e7-3d2b-80b7-e2f2ce9c3818 | -4.065 | -53.77188 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b548318-8c5e-30b8-9394-01a596c5e07a | -4.06446 | -53.77531 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db98d03c-1e52-3294-bf73-3251b13426ff | -4.0617 | -53.77137 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5bd9dad-2268-3a30-b0ef-24d17d577b2b | -4.06116 | -53.7748 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
