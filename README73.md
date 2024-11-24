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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f3ef462-3fa5-3df4-9c67-6040fc6e77a5 | -1.3809 | -52.33648 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77f583b0-9a9c-3c2d-9ff6-1331a88d4d68 | -1.42715 | -51.11979 | 2024-11-24 05:14:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5f5e785-3733-3423-aaae-3fe09e75de40 | -2.84647 | -54.00703 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 963b3e9f-0487-3bd5-ac93-9122c3cf4f74 | -2.8479 | -53.9978 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ebd52fe7-852b-3eae-a99f-85e4e672beb7 | -0.91427 | -51.73609 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e206b3b9-5441-3363-a658-67a1b5ea1f9f | -2.83671 | -54.01971 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 882fe71a-a185-33f3-8e3c-1a2ab23787e3 | -2.31079 | -52.17462 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfdbee43-18a7-3e6f-abd7-98c1b98a5a54 | -1.4812 | -52.51657 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fdf997b-0835-3fd0-bc57-556b042380db | -2.10202 | -46.26047 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 054bd55c-989a-32cd-9aa1-cea7a8582ec8 | -2.71184 | -46.26412 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2332572-029c-3e7a-b5f2-6ee106e3f520 | -3.59124 | -49.35719 | 2024-11-24 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1a50b36-dc8c-3da3-b4b8-c6d551cc8a7d | -2.18109 | -54.4703 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9acc3ff5-5120-3727-bb56-0e354b4561b4 | -3.60599 | -47.51185 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30b0c180-933f-3473-85a7-2c8f26115cd6 | -2.41672 | -51.96964 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb75106-ed8b-39db-999f-0ad588870be0 | -3.08542 | -51.03518 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d6da688-e2b5-31c2-a07a-353cf2f08ece | -2.21962 | -46.39141 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b3991e0a-1ad7-365d-993e-a9b5d73e142e | -2.75006 | -49.11892 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27849e3a-93df-303a-8dc4-5eacbe64b7d6 | -1.61274 | -52.59954 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff6448dc-c81d-399b-b066-906ffe791740 | -3.08096 | -49.19745 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 564dd712-7104-3f4a-84f3-e547850b855a | -3.25095 | -50.11681 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec7cac68-f556-39be-813b-0a5c17eb24b8 | -3.23463 | -54.23989 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bde72cc-96eb-3b3c-a0d5-6efaa43c7fb2 | -1.24554 | -51.74276 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14a7765c-d4d8-3def-acc6-0817756f3255 | -0.88125 | -51.72272 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0a6ef30-8fe4-3a95-97aa-b22fd1ffa0b1 | -0.03065 | -49.64305 | 2024-11-24 05:14:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 845bce2c-4b3d-3cec-9fd6-7a006d86e494 | -3.4837 | -49.91732 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a30e3d-4d93-3c00-9d3b-113cd990fdeb | -2.8022 | -53.00922 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e071450e-cd3d-3bc8-b65a-05ab4239235e | -2.5336 | -54.86768 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f1be2fd-a7fd-3108-a891-a4bbffa9d719 | -3.61258 | -47.50847 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16f9adb5-4d01-3523-9ee8-6d35743dc0c3 | -2.44545 | -49.08665 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dde8c41c-2619-3931-9e7e-c2b8c266cf00 | -3.86223 | -50.05462 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ce6a9b3-ef29-328c-897b-4a6df88c308e | -2.30673 | -53.87908 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ac4f65e-286a-314e-8679-795376b6292f | -1.59804 | -52.58621 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b936fb08-ab6b-3003-bd94-01f7e50a2191 | -2.82293 | -54.00818 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ee74f01-fae2-3b9d-b126-db0efac538cd | -1.44457 | -54.51247 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db7723c-7c77-35f2-94a3-e492ac6fc6c4 | -3.54033 | -49.88412 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31a8d1b4-fffb-3a0e-b854-75f242404620 | -3.1116 | -54.00698 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 12a04507-0ef5-3dce-9242-37c36c1248cb | -1.07072 | -53.64297 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6726304f-e01e-3adc-bd47-e4c593a47980 | -3.49509 | -49.91005 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84d49baf-d1ac-3fec-a463-834d967b3f29 | -2.77063 | -54.07084 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f47d1c3c-15a2-3e30-b84d-4fafcea35c64 | -2.31686 | -53.63499 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 437d2f55-a864-333a-936b-cd5e4dfea162 | -3.07397 | -50.95362 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35c7aafc-ade2-354a-aa1e-c317c722213e | -3.13384 | -45.37079 | 2024-11-24 05:14:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89bfbfbc-fb1e-33b3-94e6-40143443d016 | -2.91939 | -50.32633 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b52364d-4a9d-3c7f-b5d9-d93547fe2493 | -3.06993 | -49.19907 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6bd4b6c-211b-38e4-9d05-9af24e704f37 | -2.3203 | -53.86706 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c10c3f91-bd1d-354d-a627-dc7275e04731 | 0.8719 | -54.63619 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 884a3f34-f454-3887-8b45-3f3e49e5827f | -0.29258 | -51.60596 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e044ed2c-8494-38f9-a561-9819077d3c06 | -2.75419 | -48.66758 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74719f52-e269-3abc-83e2-d556171acea0 | -3.06945 | -49.20232 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d876a431-08cd-39e4-becc-c18f323b0dad | -1.4526 | -53.40461 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 220f1d7d-b09e-3569-88f1-3d16e5ea7131 | -0.95666 | -51.71795 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74432b6e-4d26-3c39-b45a-b0a14330be3c | -2.81913 | -54.0076 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d783a018-dddd-3136-8bc3-1c86cd4a140c | -1.89695 | -53.32666 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4032c617-8c1f-3b13-a391-dc5a314fb77f | -1.69697 | -55.01864 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8151e426-1974-3818-92b4-72c0fb6e28e8 | -3.2559 | -53.26797 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9921b003-1305-34eb-a7b2-bcb37e70d183 | -1.11384 | -53.39508 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 462e5612-bcea-356a-92f1-175d2cd00552 | -1.97053 | -48.3858 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999bf111-259c-3661-b90f-8048910b8da5 | -1.45647 | -53.40522 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e8a3a43-1181-3728-9c3e-48fd802ce9e3 | -3.2377 | -54.24496 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04b37a27-ca37-3111-983e-47a05011e1d6 | -3.06486 | -49.20164 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a3c118e-5454-3fc5-8dbe-0080b71e51bb | -3.25137 | -53.27085 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd39b7e7-b3cf-3fa0-9177-bd0cb83b5ec4 | -1.3649 | -53.83521 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d40ba541-d676-3784-8c64-405804beed4c | -2.70244 | -46.28357 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaffcd9b-1b02-370c-aea2-c317ee448a7d | -2.82838 | -54.09839 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81403af7-8222-38f3-b638-0a132829861e | -2.20391 | -53.66954 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce9c2210-c185-3705-9393-016cb106fc45 | -1.48762 | -55.08978 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| deaa2881-c028-370f-8631-8f723ee55da1 | -2.94993 | -51.427 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b31df1-6b0f-3a96-889d-d2ae62b4ef6e | -1.45184 | -53.4094 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3cf571fe-8bc0-3b06-9e0b-214a7725e525 | -2.75315 | -48.67452 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e72587ae-04e0-314c-ab59-416631536a20 | -2.4584 | -49.03568 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b499a616-8e98-3469-b7b9-5c7977b49ab4 | -2.64715 | -46.85725 | 2024-11-24 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fef1c711-e792-3b58-bbdd-2fb796d53a0f | -2.26235 | -54.83814 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3601d682-8377-3cf0-80e5-4e367f5f3864 | -2.59247 | -54.05201 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 516b3010-8dab-34c8-b81e-83a9dcf5d821 | -1.8891 | -53.32215 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18a6633f-a153-3f12-81b6-27c0bdf23ffc | -0.9808 | -51.72029 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66a5bd18-e918-3abc-bcba-83d28ad2d012 | -1.04822 | -51.739 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b364371e-3b7d-3a7e-ba29-a62314cc1676 | -1.22261 | -53.68071 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a738787d-2fbe-374e-a611-d0d756be8231 | -0.28339 | -51.60862 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64f27a95-69a4-31e2-95ea-18533ea7e106 | -1.22832 | -51.74013 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 176be412-52ab-3e7f-9b7f-4e7fec0a1ec0 | -2.73284 | -47.53961 | 2024-11-24 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59bcc297-9bed-329f-8d60-f5fd8dd5d233 | -2.76754 | -54.06567 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9ecf22d-10c5-3369-a653-c910395026fd | -2.6981 | -51.366 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81ed38e1-79f2-38e9-8674-639aa8eb723b | -2.92842 | -51.44657 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6d02837-b0ad-33a8-bbd6-c14796678904 | -3.08639 | -54.5467 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26581d46-efb9-34a5-a685-c6e479478d02 | -1.81901 | -46.63667 | 2024-11-24 05:14:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a408f826-83ce-34b2-95fb-6e64e6de60d2 | -3.22709 | -54.23872 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7f8cc5b-46c7-372a-b8b0-cf5b73812314 | -3.10086 | -54.00051 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd323b4-c895-37eb-a6bc-0e3765dbae8c | -2.84503 | -54.01626 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1611f274-14f7-3962-a904-ee82cad7f1ea | -2.6233 | -54.93249 | 2024-11-24 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1228fa4-eaf4-3c44-a02e-673aed2c1b32 | -2.76306 | -54.06968 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87b95091-889d-3ddb-9b7b-04d2b94ea3a1 | -1.42189 | -46.06113 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3948b53-5338-3cd6-ac8c-391ac7a755e5 | -3.20192 | -52.57317 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9781667-216a-35cd-bdfc-84dbe4932956 | -3.10752 | -45.78108 | 2024-11-24 05:14:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2a865dc-20b2-317f-9b81-e6f2f40596dc | -1.8633 | -48.16384 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a0995f2-3bfc-3089-9103-7e9a4a41e3da | -2.86917 | -45.82651 | 2024-11-24 05:14:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 213fabc7-cfaa-34f8-b7ba-bdfbdf8643a2 | -3.31942 | -53.29155 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22654f02-32d1-3e98-afc8-b7e6a8eb5a65 | -1.22385 | -51.79717 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21bf3401-1565-3c99-a456-23f9ada9be35 | -2.75536 | -54.07088 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcc042fd-6b1c-3097-8328-1182bb955f65 | -3.7515 | -50.00796 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9893490e-bbf8-3879-99b7-4a39ebc3c631 | -1.76911 | -52.71836 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README74.md)
