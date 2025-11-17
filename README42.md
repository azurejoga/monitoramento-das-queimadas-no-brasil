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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c0f76d-f961-3d4d-b926-f661c3c72505 | -3.75452 | -50.42762 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fe0b327-c9f1-3c33-a939-a8373d362e72 | -3.4291 | -52.17313 | 2025-11-17 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfcd4dbe-fe7e-3078-a99e-d17c77c48f0d | -2.88477 | -53.28234 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 78a4574d-0fe6-3477-a758-e698d2f03277 | -3.20677 | -51.42284 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8c36cde-a2da-3ca6-947e-cd3679fd886a | -3.23468 | -50.5053 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a38d7e37-3876-3fd6-ba2c-9a2a288a4c1b | -3.50837 | -49.92704 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2a31b97-73c1-315d-ae36-5266028e0c55 | -9.1514 | -48.06513 | 2025-11-17 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 399b9071-4526-30f4-85c4-8845ee8c667f | -3.74856 | -51.81493 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd9d9a4e-e84e-3b2c-a179-9a74bbe89042 | -4.457 | -49.78305 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84ea366f-c09c-37a3-b565-eaed3e360cc9 | -4.73481 | -46.37873 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0a26815-807c-38be-9c46-865e9a42eda9 | -4.00755 | -49.10073 | 2025-11-17 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f95ad739-c16a-3bd4-9b08-024c336bb8f4 | -3.40789 | -50.12333 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a34f17-5199-3f6b-9ae3-feb0e597b6f0 | -7.03672 | -47.61684 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03e307b5-febd-3e34-a3cf-54b77768968f | -3.57463 | -52.09847 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b227f43c-f64d-3386-9856-ac6cfd4b1c17 | -3.87942 | -46.46138 | 2025-11-17 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f81db077-d103-3b78-bd91-ca4cd03ca138 | -4.17396 | -54.59142 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e310a6b-3de3-388d-b339-2c33abd4c5c6 | -7.70581 | -42.94376 | 2025-11-17 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a141b671-3309-3426-9392-8069c876c97b | -3.1855 | -50.64677 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aef618ca-a4d9-3558-92df-c9c34a03ce25 | -2.96507 | -53.21621 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9de324b-25b3-3457-8703-5c4d8ce0c599 | -10.93322 | -48.68182 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2897870b-da5e-3294-b898-e048d3034eb3 | -3.15017 | -50.20382 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e6e8411-05ae-3e3b-8f3f-cc6b0fdc1c21 | -10.94819 | -48.6837 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1165b178-7495-3f81-8081-3990d59c8b31 | -3.5114 | -54.36988 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9260abdf-27b3-329b-a2b4-ab8c5b5b616f | -8.87145 | -50.18623 | 2025-11-17 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a9c6ceb-6c17-3adc-ab50-97c283747a1d | -4.40834 | -45.83616 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fe1d6de-2ebb-3682-a22d-928a886b212b | -7.2559 | -48.0137 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7bdbb8f-7ad5-3a4f-9084-188a70412a65 | -3.80995 | -48.92255 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 132a98ed-98f9-3e3f-8867-7c710751d7ff | -9.71405 | -43.96402 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d1721ac8-844b-37ab-83bd-55e4392fefcb | -6.67675 | -42.04929 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 87650dab-2052-3c4b-a4be-f3b3d1712e5a | -3.17696 | -50.65049 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 376e11cc-529f-3204-a634-3b42f775a85b | -9.7481 | -43.96183 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46f768c2-6969-31d3-998c-ac32156cb9aa | -4.66062 | -46.74408 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fd01bfc4-d97b-3505-bf24-510e448970a1 | -9.80054 | -48.55975 | 2025-11-17 05:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6f2371b-4637-3a30-af78-eb6f4e8c7abb | -3.30497 | -53.85575 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aab3bc04-6f46-3bcf-826c-f4be66b8ccab | -8.73446 | -48.32438 | 2025-11-17 05:08:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b401499d-7730-3d15-a1b4-82844ccd9990 | -3.23666 | -50.49864 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 81a0e8ef-8199-3c8d-89f0-8aaabc4783f8 | -2.88122 | -53.97116 | 2025-11-17 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d96aa3b-8c4c-3918-b1ab-aeb27a598ac0 | -3.38362 | -50.16929 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67b59bde-cbed-30f6-973b-9030a3f2afab | -3.46305 | -50.11388 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a3dc9f5-b5aa-3eaa-a0c2-0d2f6b9f793a | -5.1224 | -56.04263 | 2025-11-17 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e30278-91e1-3fa1-a48f-6ba354c55050 | -10.83477 | -48.03831 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94d710fd-2240-3afa-a478-7deefe660d4d | -3.74451 | -51.39406 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a25ceb2-a7e6-3c0e-bffa-6368904786d3 | -4.65593 | -46.74006 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6955dc9-ebf6-3c29-8384-beba4fcf8f47 | -3.16393 | -50.16803 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d53844b0-2f1a-3714-97e3-15de31554e3f | -6.21975 | -47.23654 | 2025-11-17 05:08:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 980e1f03-5580-318b-b78b-6ee7da72cf78 | -6.69106 | -42.0515 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 87724364-5b56-33fc-9994-a9bbb287d66c | -2.94156 | -51.75792 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38e7c7be-4a8e-31b2-b0d8-07a3c4366ac9 | -3.46117 | -49.98981 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40bfc427-bcdd-37d6-ac20-fef6c8380e4e | -4.61553 | -50.66829 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95c30d7-f21c-31bd-add2-aa8473533eda | -6.67364 | -42.04007 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d32e9e93-4425-380b-a390-456bce6ca247 | -3.19329 | -50.64794 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42826e29-1ca1-3468-8f9b-bd4ec9ad3640 | -4.57078 | -50.94005 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e689965-ef8a-34ca-8d69-ea47be66c91f | -11.40826 | -43.33813 | 2025-11-17 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d5617a6-9828-3a96-ba17-0162f7151a15 | -3.18085 | -50.65109 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 603bb714-f5b2-3233-a343-520e2d501eae | -3.43369 | -50.1166 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 040c10c8-4d8f-3684-999f-3653528b9136 | -9.15099 | -48.06808 | 2025-11-17 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a39d2870-068e-36e0-9d45-aa766e74d50d | -2.91462 | -54.16291 | 2025-11-17 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebbc5c0d-07c8-314b-afc0-45936096bfb5 | -4.01934 | -48.81499 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b3cc372-3b58-3dad-b328-be7b2d7f8c06 | -6.67988 | -42.04834 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 18d59b99-493d-3226-9eae-d13480a9e772 | -2.89216 | -53.27974 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ef92316-2244-3f7d-adf0-17c4b49a0c67 | -10.92821 | -48.68135 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 163bdf5e-0697-3bd2-b117-446cf0c6e670 | -10.96708 | -44.53342 | 2025-11-17 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b14aed59-a409-36dd-b1f9-4e6eba1620af | -3.23543 | -50.50026 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 23df61a2-0f6e-323f-a473-038f57bc822d | -7.37068 | -45.83179 | 2025-11-17 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e17e762-02f7-32e7-88d2-584f770250f5 | -9.7221 | -43.95325 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ebe0338-9e03-327d-a008-f02e08708fd4 | -4.01176 | -48.80497 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86d1bfb6-dd47-3acc-ad46-971d01ce5836 | -8.32876 | -45.41225 | 2025-11-17 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5265e49-8c6d-3b05-821c-2c3832ea7559 | -3.23936 | -50.50085 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 19ef77b7-5515-3075-8f2e-d35415f271be | -3.24138 | -50.49422 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2410ec69-972e-350d-be06-d0764a29bed3 | -10.64284 | -44.60906 | 2025-11-17 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a4cd60f-482e-3850-b0a6-e2067e91eb27 | -6.44297 | -43.81158 | 2025-11-17 05:08:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462f43dd-9cf2-399b-8c7a-92b576db2294 | -2.98451 | -53.97981 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bf5cb82-1a73-3ca0-b0a4-e1dae0b9aebc | -4.27665 | -44.24084 | 2025-11-17 05:08:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c1b7a97-03e3-3a61-a3a0-3b62b7a71a10 | -4.27728 | -44.23639 | 2025-11-17 05:08:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86e9c0e9-5567-3126-8305-ebd64645187e | -3.2433 | -50.50143 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3697361-9b47-3e2c-b8f7-41583de594d0 | -3.76855 | -47.64656 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1e6b310-880c-3375-be1b-f8bc0ea113fc | -3.49431 | -54.05143 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4167bc5c-161d-33e3-9925-1ca79fa5ec5e | -3.40197 | -50.19047 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72f51021-eebd-3b47-8934-09a15c905351 | -5.786 | -48.58294 | 2025-11-17 05:08:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 053be073-88d5-32a9-bce9-8b83d51d8f75 | -3.82034 | -47.48977 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2711d1-a6e9-392c-ab57-7ce9781eaca5 | -6.48753 | -47.53587 | 2025-11-17 05:08:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2363c5c5-dfd0-344e-97f9-34cb66726a58 | -10.92232 | -48.68776 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca9e430a-2279-3d2d-98b0-933bf10521dd | -9.35236 | -46.60238 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a835c640-6c7e-3ceb-9a1d-a33708507af9 | -9.06174 | -44.79141 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3e6d5a4c-7b04-3b20-a07f-b8dc026312ea | -9.32974 | -46.57815 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 414b7872-b01c-34f2-ad32-2c65d4d69479 | -10.55622 | -44.82395 | 2025-11-17 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2522c288-afc8-3450-86a2-9fff4b38bd31 | -3.30161 | -53.85522 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8962916a-067a-3371-8c8e-c7b1b78c7358 | -3.2343 | -50.48803 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c88f2af-5601-34c9-86fe-d9e7a6c478b2 | -9.7154 | -43.95275 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e17610e6-23c3-35dd-8ab9-8fad2a3d9474 | -3.39496 | -50.18232 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c8fcf2-580b-3ed3-b7d9-121e599f7abf | -10.85966 | -46.74141 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 52691ecf-cdc3-3e88-a039-5a361e9a2618 | -4.72849 | -46.38494 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fa216c1-a33d-3c7f-8ff3-b979292b4143 | -4.61156 | -50.66766 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469bfc03-64d3-3dbb-a59f-f643f5762732 | -8.83017 | -47.36486 | 2025-11-17 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01166c2e-e80a-3227-afa7-27ef0a6655ea | -4.0037 | -48.97575 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfcd032-77d9-3c8b-8a8f-10a7b4301a0a | -3.6489 | -50.22766 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 309f26f7-bebe-3ad6-b12d-b6a62978d845 | -3.51473 | -54.37041 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0203a1e4-4cd9-34dd-bcd6-a8994dabf219 | -9.58029 | -49.11315 | 2025-11-17 05:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 23a850cc-4926-3871-b6db-2040a9a6467f | -9.57624 | -49.10059 | 2025-11-17 05:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b1e16ec-b45c-349c-b9d6-dfaeaff50c75 | -4.61232 | -50.66253 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README43.md)
