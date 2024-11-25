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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fed35c5-4b2e-3df6-86d7-b8c1f60a9c5b | -2.56468 | -54.03816 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e85f826-f9e5-3cc7-a7e5-42dc5357a031 | -1.56749 | -52.01605 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa38a07d-8082-3cf0-958e-1cac8fa6911d | -4.69569 | -47.18127 | 2024-11-25 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40640749-3a3e-37e1-b273-1f3a33d6a14c | -2.89794 | -51.57468 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 39a53fdf-ee56-3105-99cc-8438c4c10e48 | 0.6686 | -50.80576 | 2024-11-25 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 550b9e0f-0050-305a-8cb9-d523c5ecf1f6 | -1.79447 | -52.05124 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f59a0082-2d4c-3c3b-a0f8-1d009949170e | -3.34105 | -50.50557 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7613a33d-8d5b-3879-868a-2e7d422e46f1 | -2.99578 | -53.73206 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bd1f12a-18e7-3737-9b16-0c6e8aacdd90 | -1.30514 | -51.87066 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea392179-df38-3243-8e45-5993dc2efbd0 | -2.8799 | -53.99786 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6951370-b7db-38c3-b772-2dcdf7efe034 | -1.34825 | -54.63201 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 757caa64-a5e8-32ad-ac65-e9d31ff6d534 | -1.31385 | -51.74892 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fb4144c-a15b-3bdd-a0a0-2098bedd184e | -1.60261 | -52.58438 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70aaf612-145e-3778-b678-6409f412a8a5 | -3.4781 | -50.43405 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62bec403-8243-3a10-a3a1-e99551b70b43 | -1.14611 | -51.67984 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35338c7d-c764-36fe-9a50-6aa4372dd9f0 | -1.5202 | -52.07695 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1ed6d9e-9921-3781-b918-b908e3a6c450 | -2.851 | -53.98621 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f934bd2c-63cd-3053-8f84-a728da4d5280 | -1.27341 | -52.69968 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38e9a5b-c8f4-3ac3-aec0-accc51d4763e | -2.56994 | -53.96752 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3109e740-7634-37e5-b803-bea9bdedfa23 | -2.75588 | -54.07498 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a2a22b2-828e-38f5-b04a-26e2dabfad49 | -2.56523 | -54.05622 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cae9931-fddb-3825-82ed-2ab9c2f9fba8 | -3.47041 | -47.68553 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38115adc-a899-31a8-a40e-ba44114ebdec | -2.32796 | -53.86874 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2d7568f-cfe8-3c0a-ba5f-1519e15d45fb | -1.23863 | -51.7376 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbf20bb7-75ac-31df-90de-0f37ed201640 | -1.20616 | -51.74709 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74285fef-f4be-326e-bc6b-837a7d75fcd7 | -3.67567 | -54.58599 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f354b5d1-3b12-32fe-802d-a183bb8b6326 | -1.44763 | -53.40079 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03726e65-793f-3759-ba36-b465dcf68a09 | -2.60159 | -54.25949 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0cd573e-2fc1-3bbe-8a8f-2b3b1e9f8547 | -1.48124 | -52.5197 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 178339b5-b87e-353e-b43a-fb9e503e1a12 | -0.21495 | -51.18568 | 2024-11-25 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42cbc842-6c73-3f88-a8a3-e39e89796058 | -4.23209 | -53.49083 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b75c963e-e90e-38d1-ac75-10a4a9526d82 | -4.2405 | -48.70619 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 537fb365-1603-36e7-ac68-938040620344 | -1.10947 | -53.39713 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a0cd4b3-0d84-34a2-a383-8e0950f9cbb6 | -3.08407 | -53.25812 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d632358f-2eae-3199-8190-27bf2a227c58 | -3.62939 | -54.73923 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac2d884-5845-3de7-bf27-ee44b647d3a9 | -1.26555 | -51.76354 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a2d8775-5898-38d6-8d7c-359c4acd9009 | -3.87457 | -52.20737 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97887e3d-0a61-3c68-bed0-9d96d97388c3 | -1.30823 | -51.74079 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9601b54-d2da-3491-8b5f-bdd2a56426d1 | -3.95776 | -50.85632 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e73601-dd25-30e8-8699-c5c54b7b6ad9 | -1.22864 | -51.80127 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8daf720-4596-3977-95df-0e62f9bed261 | -3.21957 | -53.83784 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad20cd7a-2cb6-3fc0-9538-4ba5d919efb7 | -2.79385 | -54.06656 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64533004-a632-32d4-ab79-d94839bba16c | -3.5029 | -53.82219 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 222d1435-bf62-3919-b09f-1b6c4275acc1 | -3.03072 | -54.06824 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f10f3b6-51e1-390a-838f-caf83fe1c822 | -1.36478 | -52.55134 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb27efa3-8477-3e6c-8c7c-72d5655064fc | -1.73488 | -52.7364 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6432b4fb-afeb-31ae-9d49-bc1727afc947 | -2.5677 | -53.96003 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9de0a1e8-014d-309e-a590-6418b4a16969 | -1.08113 | -53.36087 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 127edc25-0358-30ea-a8fe-109c0b5d05d3 | -1.11002 | -53.39368 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86bf91e2-8120-3066-aa3d-731cb7f1288f | -3.50013 | -53.8182 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e513e847-0e6b-3bfa-bf47-0656a36f5ab3 | -2.87601 | -54.00082 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c18fc2dd-a80a-3bf4-bc19-cfdfbe98e5bf | -2.07539 | -47.87735 | 2024-11-25 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d069027-fde1-3222-815d-caaacc880d2d | -3.31984 | -53.28767 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc632da-3b59-34e3-a349-27a804f40cfb | -2.99523 | -53.73551 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d977135-8f4e-38e5-a29d-87f9e6884bb2 | -1.47539 | -51.99097 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ff6469-f1ed-32a6-976a-5e72db444b30 | -3.01368 | -51.43761 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11e79e7d-a350-362e-8521-b404c28905d9 | -1.13217 | -53.70336 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1becc6b7-d402-3b71-87ad-699d9f12628c | -2.07949 | -47.87801 | 2024-11-25 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7739e9c8-dd56-3f4a-8583-e730f56ae46c | -3.10432 | -51.50383 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8469b72d-e81c-3194-91d2-04a57f1d25ae | -2.77417 | -54.04566 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1decbb97-5855-30c2-b736-f45e2d6a6ccc | -2.59681 | -46.55822 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 313095c5-1f9c-342d-ab51-7dff80b3513d | -4.20167 | -48.12063 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9867e7-aaee-3d6b-ad64-feb6dd5867af | -2.31118 | -52.17428 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dc9ae25-43fb-3c86-ae4b-0f29ebcb02fc | -1.20225 | -51.7501 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e1e8a60-c288-3c1d-969f-bdc218430f7a | -3.22012 | -53.83438 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ba6041e-b084-3e59-b3ce-2c87c9927116 | -2.85206 | -53.95786 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 962fa8be-a9f3-3925-bb6c-ed2c2a0ebc48 | -2.40603 | -53.84528 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9f5ef32-d043-3d34-ab77-53c13570a714 | -3.50455 | -53.81179 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc0b1c9d-68cd-3e9c-a9f9-f5fd0637c95f | -2.99368 | -52.9077 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2109cd55-f2db-33b7-9aa0-3cb7d5aa42db | -2.2353 | -53.61985 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b74e58fc-3d50-32dd-b30f-7c46416f6f6e | -4.23996 | -48.70966 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fe5762d-0481-3dbe-82d9-7b78757c62fd | -0.94764 | -51.63145 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3674a978-7d77-3907-aa44-688f7582b433 | 1.94654 | -60.85767 | 2024-11-25 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be54bc44-8f81-3ece-adb2-1f81bbfb395e | -0.81922 | -51.60765 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d62773d6-6d89-3b1b-af88-03f924b54eb8 | -3.04401 | -54.02748 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a403a63-e0b0-37f9-b0a1-3d17071797a8 | -1.0734 | -53.36674 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45515347-8134-3a07-80d7-1e060de0f8ee | -3.50841 | -53.80886 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7e4ed8a-dd1c-353e-b761-ce3f47241d22 | -3.71062 | -52.41151 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 925f55d6-adf5-3b02-bd1e-0b9ae28aecfb | -2.7697 | -54.03066 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 263092a8-3bba-3114-8bca-9c966edeec60 | -2.75309 | -54.07097 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 746d9896-dc3f-306e-83cb-bbe7a651af9d | -1.61698 | -52.57953 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37f9eac7-4344-30cc-9395-b16cd51e996a | -4.12582 | -54.20793 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e46fa92-dbff-31e7-945c-94383beb1ad1 | -3.78319 | -46.93642 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c29ca3-d474-36c6-a927-b49159da3748 | -4.24103 | -48.70272 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1127a1fe-ffea-3894-8829-ea8e36416343 | -3.75099 | -50.01174 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85659d51-3316-30ac-9eed-adbe4d247db4 | -3.42251 | -54.59047 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0d4208e-fec6-335a-b4d0-47c3b543a6a9 | -0.94429 | -51.65274 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84037a6d-5b7d-38d5-8612-a159eba24233 | -3.10495 | -53.96577 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea385968-c5b5-33aa-acc5-e985f1cac450 | -2.99024 | -51.45293 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b8b0633-a9ff-34db-8dc1-c2c3457c2a81 | -2.82993 | -54.01147 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 816b6b04-8600-3234-a261-6192d0dd6035 | -3.63071 | -52.24991 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 559b5834-e509-367a-b0af-d481de141451 | -1.44171 | -52.44623 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f7f7bb6-4634-3b08-a4c8-d6181955f47f | -2.5925 | -54.05692 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 211db6c6-aa2c-385a-99ae-3f25675d206a | -2.73315 | -54.13234 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3943d5f5-4144-35bf-847d-67edf6291854 | -4.03993 | -50.55949 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bca5b2d-611b-3f4e-9542-6617750228a8 | -2.83604 | -54.016 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a870f1-476f-39d2-8900-5bd8241d7f44 | -0.95836 | -51.78166 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 554c26ad-c97f-3f6b-ad28-e9c20a28330b | -3.2292 | -53.92454 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ecefd16-04e6-354d-bc36-0902e19d4ccb | -2.87916 | -51.58307 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 587248f3-b6e5-3b5b-a8dc-c590f44c934d | -2.86096 | -53.96638 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
