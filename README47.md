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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d4c0ba4-2d31-3bb0-8b38-a37b10a8d596 | -3.25607 | -52.84947 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37a6cf28-eab3-3313-ac70-5e3a28e6ed83 | -2.32323 | -46.34551 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29a99535-5448-38fe-83ad-002bfc33d4d7 | -2.03641 | -48.8536 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0952e02e-2556-36f7-98ec-7dbfcfadd87e | -1.55878 | -53.5258 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 862790d7-49b2-3a01-80c2-8418f75ba594 | 0.71687 | -50.77651 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fdffa6d-bc15-36de-bb82-d204d8a5936f | -3.83937 | -44.04673 | 2024-11-24 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33bce185-a182-3641-b20c-52c8d580d6fb | -3.57934 | -54.51868 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 290bd52b-99f3-3313-b863-1e4b1c10738b | -3.66616 | -51.57281 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e2c2c8-8085-3066-a434-4f9b47e45ed5 | -1.9477 | -49.52185 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f3a7797-5502-3e48-b671-a8d2da44f1e7 | -1.07049 | -53.3539 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31a0c720-ba8a-3b06-a5ab-8bc9a5fb009f | -3.18275 | -45.3907 | 2024-11-24 04:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1018ecd4-ac69-3379-b96c-42d93b3750b9 | -3.52283 | -53.81033 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0412a970-d9e5-3fc3-9112-8631ddac6a4e | -0.57753 | -51.72777 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bee731e6-e06e-3955-b872-cffad714ebff | -3.806 | -51.26227 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a31f439b-b689-3786-b685-b29057c42cac | -3.64162 | -52.25688 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 479275df-2f5b-3ae3-8827-1496f4cb8c7e | -2.89193 | -53.95651 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 568a51de-1879-3566-b703-e2bf6bb8121a | 0.4155 | -50.85172 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebe731d0-37de-35f6-8b65-7d1b33a21bfe | -2.47401 | -47.08781 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9ff1b3fe-737c-39b9-8149-4af18bbb39ff | -2.61252 | -54.74226 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71cf45d2-35eb-34a3-81da-1925c3cb7423 | -2.14603 | -46.74314 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33bb7b39-5d31-3804-898a-9c805a1a42cb | -1.61804 | -52.60012 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e1e04aa-e0b4-33e7-8ead-c7229e15d5e2 | -2.18304 | -54.47377 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1fb8d46-bace-3fba-a41a-9e0003a6fdb2 | -1.77575 | -53.64196 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a71b72-d0a4-309e-ad7e-0481597b6b16 | -2.54153 | -53.99751 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4decb27-59c4-3380-b5dd-3bf943c94e35 | -1.60698 | -46.88437 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8280c307-8de4-3e79-ad31-cf3c6c63461d | -4.1007 | -51.07304 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8ab8244-ffa0-32b7-b9cb-a4f07b5375d6 | -0.75538 | -51.74113 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe31ceea-d9ed-3be2-91fe-79e975dbf7fd | -2.82387 | -54.01035 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b8efd59-5493-3524-aea8-ed23434c1d16 | -1.46814 | -55.19043 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1a6eb88-d796-32f8-aaa3-e60a83bed605 | -5.95304 | -48.05779 | 2024-11-24 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8790fefc-22c4-3fc0-94ab-483eaf20d16e | -1.61743 | -52.58223 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d304a21d-94db-3661-a456-b523516a7301 | -1.65709 | -54.91691 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06b46ffc-8421-3b6a-bef1-11d97e7371b8 | -3.24862 | -54.23185 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c103cb08-1c27-3b62-92b6-55ecea9a99b5 | -2.12837 | -50.80946 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f030508-1d57-3b8f-a8a3-fbafed53f415 | -2.13898 | -50.67393 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b00ad05f-c5b7-3a84-8e60-d1eb0bc8fea7 | -1.13697 | -51.67443 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8cb9ffe-a0c7-3be1-b286-206046914e35 | -3.17815 | -54.32487 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc3fb697-9fb5-3c47-a26c-26f9510ac07f | -2.30765 | -53.87807 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1995405-1e0c-33be-bb4d-ef6a9ebf7e9e | -2.84558 | -54.00613 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b85771d-07fa-3323-ac00-7dcbae1f9bdc | -3.3413 | -51.21237 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f16c0c2-6a7e-39ff-98de-c1524b7ce3a7 | -2.03825 | -49.00721 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 128fbdb5-8ba3-3276-b39c-2bdd84c693f4 | -4.53451 | -46.42726 | 2024-11-24 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bad9eca-79e2-396b-aa15-25a5b7e83477 | -1.22565 | -53.68142 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82ea7e2e-0d01-3aa5-a820-ac25465f8146 | -3.25669 | -54.22544 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da9d4e23-97d5-3728-a474-ecb4710d6110 | -2.27949 | -46.20566 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f39ad3ba-970b-3433-a737-04945c970f7d | -2.74386 | -54.02804 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 476660cf-9d13-38d3-90ff-991e1af781f2 | -3.52169 | -53.81757 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3371f6b0-4fda-3105-9b39-daa4de2f2147 | -1.2536 | -53.32246 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb41b16f-450a-3741-9c38-de5aa1fe009f | -5.10986 | -43.14773 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4a6d52c-028d-3b41-9aab-2eeadffb0246 | -2.69745 | -46.27679 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ca181c6-79af-324d-a3a3-966c87f9598d | -2.41 | -50.31618 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ae5caec-11e2-37ae-8a62-1647e2235720 | 0.41219 | -50.85222 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 678f2db2-fa48-38aa-8b54-6076f16600c1 | -2.85018 | -53.99925 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c5c66ea-f0e9-37ee-bcab-bfe4293278b6 | -3.95786 | -45.99646 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1766a5de-bfbd-3743-9d74-cdff14972cb9 | -3.68057 | -50.08747 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7803cab-2651-37d8-8916-c2409445bf72 | -3.5578 | -50.51982 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bd3640c-f4f1-331a-915d-1ec9418ada77 | -3.70163 | -47.60266 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98bd8af6-bba9-38f3-adab-95d7da59a9c5 | -0.25164 | -51.56726 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc192159-45fb-3b48-a39b-ea97b5c4d185 | -3.22619 | -54.23995 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4a34e77-ee94-3218-ba8f-2eb4341d3e84 | -2.92735 | -51.44729 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feb349d2-d368-3223-b5f7-00ee7324baca | -2.41137 | -57.8954 | 2024-11-24 04:53:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5bcb271-7425-309b-8075-cebf03456629 | -2.16811 | -53.26212 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4ab7a2c-01fe-3205-880e-cea1a4c46408 | -3.06636 | -49.19883 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f9bf54da-f43e-32ec-a3af-ac524a83bb23 | -3.2803 | -53.78379 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77b0e5a1-8e9b-3a59-8f23-33b3190b98b5 | -3.55837 | -50.51619 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df056533-01d6-3e30-9d7f-02f55d5d6726 | -2.19394 | -50.78353 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5e06ac4-5509-304e-a8ac-67ac4cd6bcb6 | -2.15775 | -50.61879 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba5bf898-9bfb-3686-a0c1-e31f457405ab | -1.53184 | -52.45522 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9c637de-ba9a-347a-a136-75c273212f87 | -1.2342 | -51.7919 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59f13d6-d456-330a-9e7f-4e8c4ded58be | -1.32209 | -49.39435 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4922d71-5ec0-3339-850b-92001698e8c3 | -1.56804 | -52.00564 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f677208d-249f-30c0-a3c9-7d86c807d30b | -3.67367 | -54.58762 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e19b6b5-1ddc-364c-af46-42a09c55d663 | -1.22653 | -51.79775 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e7dd01a-2b7b-3067-a480-d2dc059ad38a | -3.35718 | -50.13905 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33ec5a36-ad16-39af-a85c-f9d5e58ef767 | -3.97305 | -49.94473 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c75b17-a96b-3324-a097-c2be813deb81 | -2.62818 | -54.38592 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdd89fdc-8fab-3418-adaa-eeabae62e61a | 0.40558 | -50.85324 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 50352726-8ecd-38b5-9c5c-358c0cc49cee | -4.2446 | -50.38977 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fec3abb0-3900-3da2-8e51-49616949e6ea | -2.95856 | -53.93625 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c6b0893-c43c-36c9-8568-5d9c4a324995 | -2.13109 | -50.12908 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6a30d3a-2966-313e-968c-ce5a99565f29 | -2.56554 | -54.00113 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7391193-c621-3039-87eb-94c2c398fd3d | -2.95073 | -53.71474 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3fc17a7-5012-37f2-8a97-ad1cc6b4a879 | -1.41172 | -54.90631 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef60800-0694-33c1-9163-eb55c3f3fe76 | -2.2302 | -50.50605 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbedd63a-57e3-38e6-a93c-7488fa476098 | -1.51589 | -51.07497 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b6ced3-bdee-3bf9-9255-f86fa835434c | -4.33418 | -53.84869 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3963cea1-c525-3aac-b247-b3cc4b5ce2ba | -3.30699 | -50.03267 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5298f59b-0f68-3a68-bf5b-f21f9b635c46 | -3.8247 | -52.23598 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 830bbd60-7386-3268-9219-c6901cb0250c | 0.40665 | -50.86012 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dea37918-51cf-3c4e-a261-0f53e2ce8ad0 | -2.5699 | -54.06316 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1279d651-e306-3ac7-88b5-aeeab3a216bf | -2.2071 | -53.66665 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0030aad7-3068-317c-9a50-5daa6bac1766 | -0.8511 | -48.62174 | 2024-11-24 04:53:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0a64618-7246-3084-b661-db3542f86699 | -2.26186 | -50.8263 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dfa1cb0-7799-3fbd-998d-8d96d8f6ab6e | -3.70631 | -47.59816 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f9eca45-2309-38cf-aead-1993821b2021 | -5.95454 | -48.04759 | 2024-11-24 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0650816-d98f-377e-8afe-86a21f7eecc2 | -3.04837 | -54.16638 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d73335-5be5-3acf-b936-b3add1e13b48 | -4.8118 | -49.72142 | 2024-11-24 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d9061dd-d18f-3acd-8228-de060c19e121 | -0.9096 | -51.64974 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87c8f239-92fb-35e4-9879-bca70dd98dbd | -0.3809 | -51.5493 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e801713-1f73-3b5e-9759-42444002e1bf | -1.66264 | -52.70684 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README48.md)
