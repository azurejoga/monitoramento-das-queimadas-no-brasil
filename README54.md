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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413e3f94-905f-39e9-835e-36916c7b1cf7 | -4.41207 | -48.59319 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f22c73d8-40e0-3dd5-8c15-f1b89724dcd7 | -3.81118 | -46.60695 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 193a91b9-2681-39dc-aae2-56a692a9b5bd | -3.07992 | -49.21172 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3d6375f-8e25-3d0d-90ba-52254591228b | -9.77368 | -48.21181 | 2024-11-28 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc739365-9653-355d-9e60-077a454e18b0 | -3.93987 | -46.69217 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25ac1e63-a893-3362-98e5-31cbc70c2899 | -4.11107 | -46.10586 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23e6d29d-0574-36e7-9717-922ed4ad65e4 | -15.10133 | -54.62954 | 2024-11-28 04:25:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b84fe2f-f227-3dfa-a8b0-53791dee2566 | -3.9587 | -48.19214 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 089ac45b-0423-3837-a51a-688d38f00b5a | -3.59178 | -50.35582 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48a11099-23fe-3dc3-b2e9-e1befe7744da | -2.59014 | -51.83243 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae100a00-1b0f-3979-acb7-da64217e7aac | -3.33615 | -50.51545 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 991178a3-c5b3-38df-b4e3-b5edc774c868 | -2.61564 | -51.76036 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4c16a7b-0d83-3e23-a6a2-32c5ddfdbff6 | -2.84413 | -46.85204 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbeefe07-df7c-37f5-bf79-6fe79ed4994b | -3.18423 | -50.219 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8736b4b0-4da7-3469-8b27-3c32e4c9c596 | -2.71508 | -47.70253 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c40151ea-8a80-376a-a4bf-45f4e786d9b0 | -3.73102 | -49.86755 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05e54ffa-ba12-3b01-8688-b76a218b5a23 | -3.80672 | -46.59198 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfc41388-1c0a-350d-90c6-5d599b0f4fe4 | -2.7225 | -51.74037 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7b7e22b-9be3-3d91-ac64-dc8158b9292c | -4.10843 | -48.25072 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcb48fc8-3c31-35cc-887f-579fd48a68fa | -4.17238 | -48.62383 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45a25eda-d60f-3460-bc93-0ae777766b4a | -3.24716 | -50.62507 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 281214c6-bc5a-3509-8cba-1186c003ac2a | -3.29305 | -50.31734 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63864896-011e-3eb7-a010-b2cce64f8c6b | -3.24569 | -46.42215 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f91fc7c6-c923-375f-aa99-58e80cc2c428 | -2.75465 | -54.12305 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| aeb59823-b7c5-3aee-954c-929a1432d450 | -3.94781 | -48.17055 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4208ded1-b158-3cec-89a9-89e5c3cb77d7 | -2.85315 | -46.83875 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e83304f5-0bbf-3215-afb1-b1226e1ce2e1 | -3.94599 | -46.69673 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdad0b26-d381-3c55-a092-2e7032f2255e | -2.86322 | -53.96165 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6a25435-03f9-3a9c-93f7-066d5b8931ce | -2.83407 | -54.1266 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 265d38cd-82c3-33c7-9e0a-7d75b8903a54 | -3.13076 | -51.05028 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 970b043a-70ab-3563-885b-0f9cfe0f0ff7 | -3.69862 | -50.21946 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a83735ba-4dd0-339d-a43b-e4d98fa5b01e | -3.24285 | -50.2077 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d6981b8-5c95-358d-a8b6-b8f288275d25 | -4.12868 | -51.07182 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5541b65a-163c-374d-abf0-9182cfbbe8c5 | -2.93233 | -48.01745 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 361e1666-7d4b-3075-99d5-eded78da02ef | -2.84584 | -46.84128 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57945cc2-40e6-3737-9375-4c0422a817dd | -4.03933 | -46.53902 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b76e83a1-1c4c-3ecb-8fa6-9ec1f41ee96f | -2.66054 | -49.50741 | 2024-11-28 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a2d14e5-600d-3bfe-a379-ab0411ec3f12 | -2.25704 | -53.7504 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8da0e6c-6df9-3988-95fc-75974e007135 | -10.02312 | -49.63174 | 2024-11-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0d298b-8099-370c-b39e-b4367307d0ce | -2.43821 | -50.41895 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb29db34-f718-3a4c-8310-51e78492a706 | -3.09731 | -53.73523 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eae830af-d8c0-3a75-83e8-23b731b05f3d | -3.09427 | -53.81764 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6424c352-ed23-37b7-b35f-1943799154c9 | -2.25603 | -53.75639 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de0e8205-2fc9-32e6-a173-975f00bf04b7 | -3.96077 | -50.19005 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| b3fba3eb-feab-31bc-b3b5-dab1c7c27bce | -2.93113 | -49.44073 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82412185-17de-3882-a705-885b67db202f | -4.9314 | -45.42685 | 2024-11-28 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbd81a52-ac17-372f-8ce5-b5f527e5500a | -2.72889 | -48.89545 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 452eeee9-5fde-38f2-95a5-b47d0e5e5df8 | -4.73144 | -46.6735 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84e5ae36-e8a5-311b-93f2-dad6930076ab | -3.04957 | -49.52174 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f224e3a3-d00c-3be6-8f45-d9bd45d82731 | -3.10338 | -53.26833 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33adc689-08d5-32c8-b910-3fb0363cf447 | -3.49511 | -50.45925 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5ef8f22-9139-3df6-9161-790d5758f47f | -3.59009 | -50.36611 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5900de0e-f18d-3a30-afa2-3516649b0479 | -3.10606 | -53.10489 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1309504d-ec4c-3eab-b734-a3d784fc5ab2 | -3.80727 | -46.58849 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50979a61-deed-36d0-a478-b3f0d8965d9f | -3.71617 | -47.12029 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70b4431c-3433-304b-a442-3e6a4c54a505 | -2.95382 | -51.2844 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdfdd4b8-6351-3f28-8b2c-d552c466799c | -3.38497 | -50.12169 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e0b841e6-7aff-380f-a5b2-e15254ca80ae | -3.80132 | -44.4652 | 2024-11-28 04:25:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 655a73b3-9aef-3ba9-bfad-8e5a81ac20e8 | -3.55815 | -46.33863 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b82c3bf-1995-311b-96cd-faf4cc244fa6 | -3.12053 | -53.10713 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7ea8f16-2b90-32a0-ab88-818374204b6a | -2.92082 | -48.33756 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 792a152b-f400-3159-a83e-51b30f46a579 | -3.5753 | -50.33235 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e76bce14-83b5-3b60-8f9d-c50844fa3c89 | -1.59957 | -55.39096 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8095fb2-b6ca-3d53-a692-f7d9d383ef7f | -3.94149 | -46.72491 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2489508-3439-39f6-83c8-93e9ce64f542 | -3.38709 | -50.10986 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 325e9876-5a0f-3e9d-a2b4-d1a79544c6a4 | -4.17087 | -48.62693 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ba325b9-c6f2-36da-b1cf-21bbaa8e43ba | -3.91956 | -53.67196 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1522421d-211e-32ff-8ed7-c8e6c137ea81 | -4.47725 | -46.36905 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d52e2ca-7651-3f67-9646-30af01b94ec9 | -3.51178 | -50.50873 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad10fd5a-fb6c-3eb3-a900-e8b042327d6a | -4.19641 | -50.68754 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b26efa8-a8c4-3db1-935b-5bd4e17a60e3 | -3.26829 | -51.26691 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70ab4f8a-dea5-3f9a-8d45-9869a1b45257 | -2.25704 | -53.47387 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18124f7e-fd09-3149-9921-69ae723611e7 | -4.83727 | -44.29068 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a574839e-89c6-33a3-bf61-3aaf25e5b290 | -2.77919 | -48.58552 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fdc24a8-02f6-342f-8b98-b04e8d91c0e4 | -3.40529 | -50.9854 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d242205-0775-3bf7-8f07-ad6112cf64bb | -2.86156 | -46.85106 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85efd3d3-61c7-34f4-b75f-1485382c4190 | -3.10094 | -53.26658 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbdaf7fd-7654-37ae-b955-7d259e4b8878 | -3.81481 | -47.47155 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf3d050-d06a-318d-88c7-411d95eefbf9 | -4.23132 | -46.03326 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec51a37f-0242-33a1-b67a-6cfc7fe9e374 | -2.91032 | -51.58296 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e3974a9-81ee-3959-950d-1f583dbe6109 | -3.53014 | -50.19366 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e1b8a34-469e-3157-a2bd-b8de4ca90649 | -4.38447 | -46.01115 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3bd188e-377b-3de6-8316-26c934289ce2 | -4.18142 | -44.27191 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 704d4f52-1658-3037-992c-84e6b90f9719 | -3.49627 | -53.80576 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ee1eb86-0c1c-3c60-a834-3415088e0c2e | -3.92976 | -47.014 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3894d7e-aea2-3d27-9fb0-b0d4dc7d4e69 | -2.80126 | -48.67927 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab8c28d-8b45-33a6-bffc-49f7cbcac89e | -2.86041 | -46.85825 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27432d82-bcfd-3881-8fdd-af328411cfb9 | -12.14891 | -48.10242 | 2024-11-28 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8d3bb29-0535-3375-953a-e24896f2f0eb | -3.02949 | -54.02142 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3931867a-b24f-3411-9540-f446db2cf175 | -4.49564 | -46.48948 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ebaccc-7138-31b9-8a0f-a89027c56ed5 | -2.94286 | -48.33692 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2fed957-de85-317a-b8da-d6f37f4df88e | -3.78369 | -50.14159 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f73e26d0-cd69-321a-9469-fd7f9a663a94 | -4.61701 | -45.76194 | 2024-11-28 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 253ff6f7-08fb-3462-a2c6-04fe2cb0ac23 | -3.47051 | -51.62893 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1f6dae6-82fa-3f69-9cae-24790022e938 | -2.86606 | -46.84444 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5be469e7-f4cf-3b93-b089-7e7c6aa681c5 | -2.86772 | -46.85572 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dc4b0e9-4a52-3b34-a915-5abce3ed0315 | -3.94209 | -46.69971 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e118e1e2-c608-3ec8-8a1e-0462b91d2ce6 | -2.79681 | -51.80911 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71eed1dd-ff22-339f-b955-e13b7160c8de | -1.92057 | -54.44078 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac89678a-c51f-3a01-bace-e60a854fd6ef | -3.50088 | -50.49979 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
