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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a4486a7-08a1-3649-985f-4c720d347cc4 | -3.28305 | -50.43655 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48b49554-ab23-3ab9-b9dc-42f7e81187e1 | -3.94776 | -49.95427 | 2024-12-01 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b48b746e-1d40-3f38-8f68-6f05cc3cfe1c | -2.8492 | -54.07977 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0324e77-22d2-3b13-889f-68dcb188a210 | -3.09206 | -50.35138 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d939adf7-e250-33db-b75b-e9ac02c224a8 | -2.76351 | -54.02457 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a161c4f-09b9-3ea4-8636-399c163c4dd9 | -3.11665 | -53.98478 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c416952-b7c0-31d4-b613-9dbc1e3f9b69 | -1.77567 | -55.27487 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d75938a-6b99-385b-b279-c8e1be921b6c | -1.72557 | -52.47932 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 818f9018-8f82-342b-8f56-a7974889a8cc | -4.01941 | -45.88727 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 795d7484-3672-3771-9dd3-ae69409c4b91 | -2.62845 | -54.21905 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce3e7ce6-935c-30df-93f4-a3db66ddcf5f | -4.56962 | -46.29937 | 2024-12-01 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c355987-e64a-3549-bd30-10271c14e447 | -1.60339 | -52.2905 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fddb3f4-31a6-32cd-853e-fbd7df74a8a0 | -3.51269 | -53.78754 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e00fdd7-fe97-3486-bd75-f201dbfca7cc | -3.25467 | -53.28115 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc4fe9b2-b823-3506-981d-4a070aa00aa5 | -3.11314 | -53.98425 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c6d4ecb-2d0e-3dd5-b1f7-514a9532186b | -2.56048 | -54.34399 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 28b370c7-a3b9-3477-af42-5e90fcd0bf8b | -3.54825 | -54.81767 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c1a2511-64ac-3e0c-aeb1-58fac40b771f | -1.42306 | -54.51205 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6c86a78-3f32-3f2f-bae5-8ac098d289c5 | -2.81514 | -53.94526 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca0fd7fc-1f85-37db-b231-b6b0f260c7db | -3.26723 | -53.64125 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 968a58d9-e7e2-3a29-967e-821cb97dedd0 | -3.25581 | -53.34553 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6497f9ab-555c-3003-9d17-1dcc6e88de70 | -2.97319 | -53.74252 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf32458-0a4c-38db-b656-52626e6e1a11 | -1.52459 | -52.66784 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19165efa-e843-316f-85e9-58d277f2d16d | -3.86096 | -50.5369 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d05d4a4-21ca-3940-8579-baaf8c79b069 | -1.38884 | -55.1828 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acdb2580-ff11-377a-b9e0-187f96bd73fd | -2.71956 | -54.11252 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3398d5e-f136-3dcf-ae67-62e504dc724f | -3.31695 | -50.02972 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ebec318-1706-30e7-b7c5-61df0fe35fbd | -2.76772 | -55.33469 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444fc4c7-b357-3101-a685-2649a9338f2d | -2.35859 | -54.84901 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 892df37e-77c0-37e5-8f8f-56caffca0b13 | -3.33779 | -53.37381 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bad013fc-b0a0-375b-8c4f-3632b318ec1a | -3.07204 | -53.80548 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b077d5d9-44bf-383a-ae84-fa4012f2188a | -3.3019 | -50.27624 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e21354af-a0f1-380b-aee1-2c14a676a5ce | -2.80405 | -54.06244 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a242718-bb38-3cef-b1b4-b458a5e20c22 | -3.11156 | -53.80661 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4acc0853-6e38-37cd-b570-544079355f60 | -2.84523 | -54.03577 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d5acc6b-cb36-32c8-b386-0b3289b53328 | -1.6456 | -52.75315 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64f7c35d-ddc5-38cc-a0e5-0f4e68e7cd93 | -3.92871 | -51.17687 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00c2ff18-3332-34c8-a44e-b8ecc14747ad | -2.83267 | -54.0392 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8144995-812c-3d3e-a9f0-aa4b3c64d6a1 | -3.30215 | -54.16633 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eec9ef1-7979-357b-a04d-3c6f4a5c239f | -1.73179 | -52.79983 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dd69d91-7363-3406-b818-ee6c7909339d | -2.65769 | -51.87401 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 04ef9944-924d-3d33-a7c5-e9750e05a195 | -3.23655 | -53.63326 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcd0058d-18af-35cf-8075-4a8cbcd85466 | -3.49815 | -53.83435 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ff2127e6-71f7-3299-b40b-b0d0e58782df | -3.85058 | -54.22268 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 315d70b9-d8aa-3203-9398-187e0eae175d | -1.42233 | -55.2738 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7ea3e6-fd16-39e7-9dd2-c17b8fc990ea | -2.86149 | -54.04619 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c0adb3a-699d-3c77-8907-2dd17c8465e7 | -3.06041 | -54.04057 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c2969a-07e7-3c9a-99d7-b0148b989c47 | -2.38625 | -53.79483 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 729894d5-fb51-3dd0-abbb-bbc25bb08433 | -3.49812 | -54.6665 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35302f42-8de5-3bfd-881f-409c90162187 | -1.36615 | -54.65471 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da2b63ab-0b4e-3613-bf96-15d2fe4ac8db | -2.69495 | -52.91211 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eddcf4dc-72fb-3ef1-9832-18c9f096d844 | -2.98688 | -53.88971 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2445cd82-1f19-350f-894d-47d332abe6f6 | -2.83225 | -54.10996 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe54d86a-903d-3558-8c09-676fffab5f0c | -3.28845 | -53.83331 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d501c6d-7f35-319f-81a0-3402dd087e32 | -1.91844 | -52.65901 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3ae9f6f-a868-386b-b698-3e3ca10ff523 | -3.11595 | -54.01252 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c90e06-07ee-3b37-9549-0323d66f66fd | -3.18091 | -53.2498 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c723e9d0-0073-3c18-a50f-fa5e08d3661f | -1.65957 | -52.40236 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b8d2774-bab5-3f24-aa00-7df5dc07bd9c | -2.25588 | -53.6315 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56d7e758-72d6-3969-98e6-b20aa47b2ad5 | -2.86392 | -54.00699 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 528f47a9-9247-306f-a89e-c14ce212096b | -2.30327 | -53.90572 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0f550517-63da-3965-93b9-1d207c8837b4 | -4.49956 | -49.63899 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a5fb977-6a1d-3955-9fa9-146911ea4898 | -1.27969 | -54.5561 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 573ce709-47e9-3135-b583-3b81ef5ffeb8 | -3.7042 | -51.06319 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04417d4f-0203-3c99-80e1-2d502affcb69 | -2.83418 | -51.28136 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd636248-48d9-340b-8ef1-2d55baa05949 | -3.11074 | -53.99978 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 476bf644-187c-3c6d-8fec-9d9dcf7441d3 | -3.07433 | -53.26041 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db3a81d0-8c1a-309b-835d-1dceadefd271 | -3.49692 | -53.84223 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2ab3923-1be4-37d3-a06e-b49962ec8f21 | -1.43445 | -53.398 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba24fbed-e2a2-3747-94f5-0f72374777d4 | -2.83345 | -54.10231 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 654c08fd-1d5b-30dd-b8d4-ee31e8f8d35b | -2.19262 | -53.57302 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebecbef9-bf2b-3810-b2e1-5fc550766064 | -1.56794 | -53.83728 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0e0e1ad-a7e3-3f38-bcb3-2e5309eca321 | -2.72091 | -54.13984 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a8429a3-184f-324d-9224-098572133c09 | -1.44663 | -55.20606 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3daebca2-f700-30ed-8c9c-9231e4c36e95 | -3.11111 | -53.76205 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b6a0de-b66b-3dd6-885e-4d0c7bda5d21 | -1.45806 | -54.53214 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 030c4d27-8981-3492-a1a0-de1601c57a07 | -3.28359 | -54.14782 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2388c963-d2b9-3b52-8343-e36f6150834c | -4.00686 | -54.61642 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 147275ac-445c-38bf-baa0-9ce8f211e194 | -3.0968 | -54.29652 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 02c82f64-52a5-334b-ab5a-362465ad7457 | -3.02161 | -52.35766 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 239acdd4-0217-3b51-ae5f-a5e35d6a1726 | -1.49208 | -52.43879 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 926e0365-d1f3-3b5a-aef1-258b6dd93129 | -3.14116 | -45.37643 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72c03500-c6fd-3c29-9b0d-481865f31850 | -2.26747 | -53.46576 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a80eb976-12d2-3b48-8377-dbd992e4ade0 | -2.86161 | -53.9987 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 176d4d1b-b884-3040-ae9e-91af8e90262b | -3.02785 | -54.01979 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 014aa767-69d5-3e1b-9389-ec8358d12f1f | -2.68828 | -51.72507 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ac82933-ded8-390b-8104-dd937aa95265 | -1.56772 | -53.5192 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69d6ab89-da48-3c8a-8c6a-60ce36e2e4ed | -3.54319 | -50.40786 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e013a5ba-9375-382d-a499-a73b5c8b2717 | -3.24908 | -53.92397 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d69ba84c-b44b-3f58-bea5-ed8a1befb8cc | -2.25603 | -53.63049 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa3d85a1-3c43-3dc5-acd3-15c8098ff6ea | -2.45307 | -54.01762 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03ee4bbb-f457-3e5e-8926-033aa1e1f91f | -3.12625 | -54.1761 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f30c325f-452e-3161-a2da-0dd5fe4cae82 | -2.85176 | -65.20856 | 2024-12-01 05:08:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d845391c-11cb-377f-8e31-42dd52b358fd | -1.44773 | -55.19907 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62a0c905-33ee-331d-b57e-0d0ca0b15a5c | -2.79778 | -54.03388 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da51f64f-1e9e-39dc-9a36-e0f867885cea | -4.85937 | -50.71483 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 504dca66-7b7c-318a-bb57-c4dbde300e4d | -4.55061 | -43.30361 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| b7e1d09e-e5ff-3535-a761-c6b3f6ea32d9 | -3.21489 | -54.23625 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18961d06-5908-3ba9-8114-b20416028dcd | -2.43654 | -53.88628 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4c4b69c-87ca-3644-8c1a-f4660cd93844 | -1.3577 | -54.64244 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README96.md)
