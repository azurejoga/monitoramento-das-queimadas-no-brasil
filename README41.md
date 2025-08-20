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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38fef6a9-281f-3bcd-94bc-f253b0d54c9e | -4.9147 | -43.24073 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30214817-7481-3a37-bce6-606381d99899 | -5.48458 | -42.16949 | 2025-08-20 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c4c6e93d-95ff-3010-8ea1-64e3772c6175 | -5.6579 | -43.50411 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eee6b72-7bd0-3a05-9021-44f918ace919 | -5.65733 | -43.5083 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7864ccbc-3aff-35c6-800e-017eac5a6efc | -4.01391 | -48.06141 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13df36a6-a3d0-3a78-a60f-3fb92a4860b1 | -5.00132 | -56.03541 | 2025-08-20 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecb39a8f-3c09-37ea-8fc8-20fbdb3ab6c3 | -2.54655 | -47.70443 | 2025-08-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c276a0fa-5793-356c-b51c-2231df6b31d9 | -2.44358 | -47.32561 | 2025-08-20 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b1c9fbd-2d70-34c2-ae5c-10720f14724e | -4.31013 | -48.10296 | 2025-08-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49bfd69-7bb0-39a0-bc13-2b90a1f96c5e | -3.06623 | -54.7789 | 2025-08-20 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9316b1c3-9bd5-356d-91e2-4e1757332e89 | -3.9845 | -42.52039 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5dca2623-c3d3-385a-802a-06003c7d9cc7 | -5.78178 | -43.89371 | 2025-08-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 442ca7e1-1972-35a5-8538-bb7c41bd508b | -3.98518 | -42.51574 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db3fb9d9-cb44-3fd4-ad6e-9424799a346f | -6.13092 | -42.96019 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 78db03bc-1253-3c30-b52d-9e5f65816258 | -6.37096 | -43.26571 | 2025-08-20 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c597ba4a-42fd-3907-9eb5-3a20f44edae4 | -4.48152 | -43.90531 | 2025-08-20 04:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cd324d5-4c1a-3a91-9f7b-3c5b0cc634b0 | -6.85644 | -43.60797 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73439f84-de28-30e3-8b59-3ff960627035 | -4.91532 | -43.23645 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92eaa221-6d69-3aec-b4a5-b765f040d259 | -5.99113 | -42.84332 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 37a2841f-46c2-3e2e-a9a6-329f47e13348 | -5.9955 | -42.85402 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5a7fb819-468d-3cae-8bdf-4b9718141e4c | -4.90998 | -43.23141 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86fa6ed1-c9ac-3898-9257-c28fb8d19538 | -5.99298 | -42.82615 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df8aebf0-04df-3749-be54-796f3db4722b | -5.32072 | -44.48808 | 2025-08-20 04:55:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9308b6d7-abf6-314a-b686-34a5c9e0340e | -4.29368 | -48.06849 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 102d785b-42f1-3705-b6d1-d453245eb1c7 | -6.05926 | -44.11614 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d2872a0-3241-3990-85e3-94b884d08d09 | -3.04747 | -47.01782 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3226b03-bba6-3650-b645-63a61069272c | -4.01811 | -48.06212 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5e32c31-2689-3ed2-804d-0b25aee24f71 | -5.78752 | -43.89462 | 2025-08-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ecddb67-2c80-3750-bbb3-05638051e0c2 | -5.99609 | -42.8496 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b3b89661-a3a1-3397-af6c-7e05a520d45d | -2.58418 | -51.91479 | 2025-08-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce17aecc-6e38-3be8-92f1-c968af70aff1 | -3.98794 | -47.88828 | 2025-08-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32039d3-186f-3b63-b973-d5f3474ad4a2 | -3.39734 | -46.90251 | 2025-08-20 04:55:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 268889e0-8b9d-3d2f-aaa2-32fab67fa6f4 | -6.95049 | -42.8699 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| e7c95a51-a906-360b-8457-5e8ba52700ba | -5.98566 | -42.83377 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e83a83af-dac5-32c3-ad27-eeeb39b73f51 | -3.97906 | -42.51479 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9514e9bc-af26-3ca6-9b95-2bbe6a624890 | -2.91632 | -48.30233 | 2025-08-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46f323a9-f42e-3469-84cf-0d747df51cac | -3.81873 | -41.56971 | 2025-08-20 04:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b35c6614-b2c8-3013-94bf-2d2c7936173d | -5.88196 | -48.12646 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f846e2cd-b33a-38ea-8568-cc2b4790ee08 | -2.83359 | -49.146 | 2025-08-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff152918-7bc9-3373-bf09-bb2c1ad28185 | -5.00072 | -56.03915 | 2025-08-20 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf68b93-26a0-323e-9287-63559fc86fe8 | -5.79154 | -43.61091 | 2025-08-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37347798-14ba-38d5-b49a-de30eaabbea6 | -3.83415 | -47.73602 | 2025-08-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c330f6d-10cc-3b9e-8c6e-6c78320ef8cf | -2.83432 | -49.14119 | 2025-08-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f06006e-3c9c-3eca-a027-8f58ba715368 | -3.97975 | -42.51012 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e41b1124-6212-3d35-9694-d0e8b110ece4 | -6.12541 | -42.95477 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fc9bd27d-913f-3465-a4ba-541746a2feda | -5.98685 | -42.82491 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a00ba69a-238a-3f45-b8a6-3b56e2cac85e | -3.87641 | -50.97552 | 2025-08-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb323944-15e0-3509-bfe6-5d3c945f9a1f | -2.77015 | -48.59678 | 2025-08-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54df882f-8d8f-3fb8-bbdc-892977bf1a38 | -5.9966 | -42.84905 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5fd6276-3839-33d6-9101-0436421cc020 | -6.05866 | -44.12041 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c67b2864-ee69-34b2-80a6-2bd0d8dacf82 | -4.30954 | -48.10685 | 2025-08-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09df661b-4791-3672-bd63-5b43f5a12f11 | -5.64116 | -43.37652 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f5684da-6b73-3960-9595-fb98fcd6e726 | -4.29309 | -48.07245 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cc37c1f-a25b-31c5-8f82-cc07ea384296 | -6.23361 | -46.24525 | 2025-08-20 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bb1c32b-2522-39e1-b03c-189ff818566d | -3.03694 | -49.43697 | 2025-08-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d482c22c-da68-37f1-9da4-f9059e7de312 | -5.98624 | -42.82949 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 751833e8-3c07-3650-8697-d0e018e8dd05 | -6.86179 | -43.61327 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd03d53f-42c6-3fc9-9e39-8324fc904a56 | -2.77218 | -48.59758 | 2025-08-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ac0ff96-b9a2-36de-9087-6a99cca99169 | -2.7727 | -48.59413 | 2025-08-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f043a636-6947-345b-9883-fdf48c825bc4 | -6.86236 | -43.609 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 513116e8-0194-3f19-8e22-f3fb891666cd | -4.9141 | -43.245 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b0d282a-5e97-35b2-9eac-46ee0dcb0c73 | -6.01157 | -42.8283 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8154822d-be1e-34b9-80ab-0585893c18a5 | -4.49046 | -47.67973 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82db05b2-a6eb-3b0d-9437-b090474084fc | -6.94789 | -42.87387 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c9be1af9-7e4e-37ec-a31e-23ea04d79c26 | -5.99597 | -42.85344 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d2a4827-ba2b-3b83-b776-9d9e2c202d37 | -6.05505 | -44.14638 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 742b7b9b-db8f-3467-b4fc-06bfcb1d2ae9 | -6.23477 | -46.24658 | 2025-08-20 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53b4eeee-7fb3-35e6-9e39-e50894459123 | -3.27129 | -49.14211 | 2025-08-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 196b13ac-177c-3721-b274-bd1901d0f71e | -6.51811 | -45.4642 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 690b5848-75bd-3157-adab-b6be1a0fff9e | -4.90876 | -43.23998 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56a9ff3b-3cd2-3514-83bc-812f4eb4f59e | -4.43042 | -47.75555 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8fa1a712-6a7b-3dad-a600-772618360e4e | -5.99238 | -42.83059 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af94f63e-f0bd-3c72-a1eb-5a9d02730e83 | -3.49705 | -48.92125 | 2025-08-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57d3a7d1-960b-3b56-8135-23b63da4d159 | -5.98266 | -44.14798 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 337867d7-bdcf-38df-aef0-9ace8c3a3bcd | -5.99526 | -42.85846 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18ec3697-d326-3683-8dbb-590950d3acb8 | -5.82403 | -50.16475 | 2025-08-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e555619e-4565-3cb2-83e2-ee34e8d7354e | -2.58738 | -49.49039 | 2025-08-20 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad8dcda8-aea3-3d2a-8119-78a5799041f8 | -5.98985 | -42.85229 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e28e7083-9961-376b-be61-fc3c40f1a4b5 | -3.87932 | -50.98007 | 2025-08-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e0dd615-0936-3998-bc37-083480e9482a | -3.27055 | -49.14695 | 2025-08-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83624888-9ed8-3a7f-9a0e-283b586d000d | -4.42611 | -47.75475 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d06fec76-419f-3b59-82b4-e2e1ffb103c1 | -4.87065 | -47.75603 | 2025-08-20 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 91feb9a1-232e-317d-9a0f-83e9932d45c7 | -5.99918 | -42.82687 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 317e47bd-09db-31a2-a061-16d63c3e13fb | -6.95476 | -42.86991 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 1fe50760-3115-331e-8249-ab5d754da8bc | -5.98318 | -44.14433 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6d6aae32-63de-369c-b4c3-2b06d6a84aef | -6.0259 | -44.35571 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c7d0c0a-eba3-3562-9388-f4299eeb6746 | -5.99049 | -42.84779 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2efc80f8-c1bd-35b7-8a02-0a3837a250dc | -5.97701 | -44.14704 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bc86d36-9051-3015-b8aa-90b166209cbc | -2.54232 | -47.70383 | 2025-08-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c805aa8d-259b-3ac2-9a7e-5e82bd351d25 | -6.94854 | -42.8689 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| dc015fc2-a067-3ebf-bda6-dff73ea29f31 | -5.40495 | -45.19212 | 2025-08-20 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3dda2e6-b20e-3526-bc69-daeae508fa92 | -3.81876 | -41.5723 | 2025-08-20 04:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2838fa7e-c2ea-349e-a75c-4d147f408907 | -6.44918 | -45.49449 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 292f4769-ea56-3a3a-a4ba-c5cc34dc3a86 | -5.61563 | -43.47277 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 672ffa4f-5e36-30d4-be9c-1a5a3bfaf668 | -5.98999 | -42.84828 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5bbbc7e1-e3db-368b-8802-3c2ba11ab7c8 | -4.91593 | -43.23212 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9735b963-619c-3d7c-b6a4-4aca051038a3 | -6.71025 | -44.33007 | 2025-08-20 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a7131c2-3daf-3081-89d7-0d45ea15eadc | -5.78808 | -43.89062 | 2025-08-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 41aec6aa-e044-30aa-8345-0d64eb6e2e0f | -3.65067 | -48.45159 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a719340f-0f58-3669-8d3b-a93109cba459 | -5.60971 | -43.47209 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
