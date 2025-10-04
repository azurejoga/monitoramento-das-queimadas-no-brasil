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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e23b3633-da98-393e-83b3-481c7f6f4ef6 | -17.98027 | -45.01036 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e9f2b74-d39e-30be-bee7-2140d31e9d2a | -13.12933 | -47.83276 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 90f94b97-9095-36ca-aaef-1c4c29db03fd | -12.70883 | -48.55508 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb07cea0-a75b-335b-b08b-0186e8853b08 | -13.10085 | -47.89166 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d7607300-86b4-31ce-a5bd-f471183bd1fc | -14.91675 | -46.88712 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d08e5a3f-9a9b-30cd-a987-d33019fdae76 | -14.63143 | -48.25254 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eba49db4-a916-388a-a370-e06aa6b2c25e | -13.32213 | -47.79467 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb9f1fc3-2957-30da-a115-9d0742300113 | -14.84938 | -48.28943 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0c00c8b-2c7f-3dc8-9d3c-910fd36aeeeb | -13.33467 | -47.19545 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc9c9ac7-5f20-3c22-898d-6520aa261bdb | -13.10751 | -47.91453 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83898738-61ba-3530-aa0d-ddc3fce0eb4a | -17.47741 | -44.0443 | 2025-10-04 03:53:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddd73c6c-76e0-3368-8c5e-59b0f7527e3d | -14.38531 | -45.97399 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ac3ef95-0a7e-31af-a998-028bc1cd9424 | -13.70625 | -47.34263 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d395b23f-d2ac-3d1f-a7e7-c3d9592ce77f | -15.72768 | -46.28986 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5218812-a8e9-3d12-965f-82ae39331df0 | -11.80053 | -45.02834 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e998d4cb-06b3-37ab-8906-ca765afc2017 | -11.44694 | -49.71605 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e82dd7b-b1ca-3ff4-99bc-6e596950cc61 | -13.10946 | -47.90474 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85a9a367-2976-35cb-89bf-9a1e1cd4f730 | -14.68214 | -48.278 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 054539c6-80aa-3a69-aeae-0420094b29b2 | -14.91381 | -46.89593 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93b698bd-786c-3202-8e6d-f6ff453cbc41 | -14.65907 | -48.30912 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 72b8eef0-b249-338b-877f-d48ae0d4ba59 | -13.47976 | -47.23135 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8281fdec-066a-3ac6-b1f8-3a241477360c | -14.38909 | -45.95402 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9823902-172a-38e5-b046-433ca635d2fa | -12.72771 | -48.55904 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d81924dd-6fd0-3120-8d31-105a588087d8 | -14.65079 | -48.23977 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a665bc34-99d1-3fd1-af12-b0778cad3853 | -13.31927 | -47.79575 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6987b338-70a2-305c-9205-85d8804abc65 | -11.80424 | -45.03406 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04d1ab10-8bce-3fc1-9bea-92a55181662c | -11.79666 | -45.01928 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2cd4ef7-73bf-3c4d-bedb-31f9c241ad0e | -13.14626 | -47.94569 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 441cb5a1-dcf7-3782-8c3e-275793e597ad | -11.99756 | -47.19432 | 2025-10-04 03:53:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca815689-08e1-3727-b6f9-b9da2818b281 | -15.67504 | -44.51159 | 2025-10-04 03:53:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 502cc9f8-24f9-3eac-b558-6ed3984641e8 | -13.13433 | -47.80754 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1a0a92d-84c2-3427-b7a7-e514a9c819f0 | -11.91345 | -46.36056 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d71130f-8998-3fec-b2f7-0bf976a8a986 | -13.26888 | -47.20489 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bc5c789-f5f4-3f93-9a62-d580cfb52c51 | -12.69818 | -48.54939 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 61b4665b-e5c7-3c1a-913f-0b487987ee4c | -11.56306 | -47.68458 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87628439-8302-34be-b445-6832bcbde1fd | -14.45858 | -48.40141 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd840a18-7456-3028-ad5c-d69bc2370230 | -14.92165 | -46.88801 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b352702-ebe8-3da9-a2f4-8d6ebbb1378d | -13.11716 | -47.86596 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b52c881-7fe6-3777-9bc8-b34a2679c844 | -14.85009 | -48.28583 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31efff48-bf61-39c0-ade5-315c0b7fc3b6 | -14.10062 | -44.30653 | 2025-10-04 03:53:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f564e14-1a29-3bf9-985c-093358d1dd33 | -14.91941 | -46.89938 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28500cdb-46da-32f3-9476-dfe24df703ea | -13.32276 | -48.11638 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 09ab768e-097b-3831-95ae-185867239582 | -13.12254 | -47.83886 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e06cad09-43e0-336b-9b60-393ae117c311 | -11.79119 | -46.82806 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08d1ad09-3930-3eec-9810-2e6ddc996cec | -14.38815 | -45.95898 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6923f130-a697-35e5-9880-f0b1d05f1fe1 | -14.74187 | -48.40691 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90dd48d4-fdee-3b40-83cf-15e9331d51a8 | -12.91281 | -46.92174 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05d1e6a2-739b-3d41-a9f0-c87a2b55ecc3 | -13.31293 | -48.13745 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa069fbb-b645-30d2-9623-e45e07727dc5 | -12.81105 | -46.85986 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0cf1a07-e322-31bf-82e1-91f0fa7f4344 | -13.21708 | -47.82069 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15e7c73a-2c0f-3bb7-a8ba-4e075fd38bc6 | -15.32666 | -46.38218 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc5888ff-cc4a-3800-9418-6b9e9d9f891c | -17.00784 | -49.14994 | 2025-10-04 03:53:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99f4ce05-4707-3a92-91a4-4a319db557be | -13.22319 | -47.84594 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffe39bf4-ae7f-3a9b-bb48-0f60e84942b5 | -11.57053 | -47.67529 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16ca7aa7-f731-3961-8857-cfe5962a138a | -15.60817 | -52.47654 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 504f4393-a037-3b16-8cf8-867b16a12088 | -13.31369 | -48.13362 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ab2e264-d4f8-3118-bbd4-52888ae6ba9e | -13.33201 | -47.62958 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fbb8fe3-df9e-3b9a-8b6f-cd8eba57aa28 | -14.75404 | -48.14025 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61aeac20-aa05-3b65-bd30-0e6e306541c4 | -13.32087 | -48.09729 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 082cf24c-db68-33b2-a07a-43a49ab3cb07 | -13.32989 | -48.08021 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33fd0612-8155-3984-b8bb-2c764b9c7816 | -16.37574 | -40.75461 | 2025-10-04 03:53:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5adc6028-2cf3-3593-933c-4d9b26ceb4ea | -15.7251 | -46.27829 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 462499b3-272b-3075-ae04-f675ba9d5369 | -14.59809 | -46.7301 | 2025-10-04 03:53:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a26f2022-fb7b-3319-a5d7-61bffe4ed342 | -15.6175 | -46.93654 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 879ec0b6-4ef0-34c0-9478-da8b7bfe3b29 | -13.10981 | -47.87478 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 167df4e4-b605-3ed4-b711-388cc311a71c | -13.32592 | -47.18551 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb551ebb-f5e8-3797-a344-083381c8cd5f | -17.07927 | -43.36256 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49e6f6d5-63db-362d-b1cf-70683970e182 | -14.63537 | -48.25294 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a4085789-ea6a-3ff3-939f-58d6871414e3 | -14.30716 | -45.8638 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8972cb62-9fdd-36f9-9fa6-5319395e4746 | -12.29783 | -45.36145 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fced865-9c09-3d5d-85ec-77f89e246ab8 | -13.1002 | -47.89491 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b1c4597-7485-303a-b7fb-48641c313db7 | -11.91582 | -46.40277 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 559d72ec-456d-3d93-aca6-097e3a285936 | -14.67805 | -48.27055 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5af55535-1050-38a1-bac3-62f888157957 | -13.32071 | -47.575 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6bc9ac24-9593-33dd-a588-0483c895cb6b | -17.08045 | -43.36085 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46b488a5-906e-3ab7-9b00-60c7b202e168 | -14.72697 | -48.08194 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18d69357-f704-3f99-a151-3861939d535a | -15.79407 | -42.17338 | 2025-10-04 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dffdce85-af4e-3098-9c38-9a4e92e6dc7b | -14.94156 | -46.86409 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88dddd11-0b20-3f62-8381-970e68818287 | -16.39727 | -52.16292 | 2025-10-04 03:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c485fcd3-a30f-353d-9fe2-b1becabf12c3 | -12.53016 | -45.98057 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f99678c-5cd6-3668-83e6-7c27373049e2 | -13.12569 | -47.823 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9fa6b1a2-e5dd-3cf3-a560-9a6ca84cb85a | -13.7607 | -48.05612 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a20b2a39-8b07-33f8-b4af-ee7e841b2ee1 | -17.07839 | -43.36741 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c13f3bec-d48a-36e9-8c62-705d233a622c | -17.03177 | -43.43747 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 810d72d7-dcc2-3d52-bbe6-e21807a8a805 | -16.0161 | -50.94593 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf99e7dc-285f-352b-8d95-df95e503e5bc | -11.78856 | -46.82124 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 912f31ce-2fa8-3cea-93fa-9e7ebe303ae3 | -15.52885 | -46.83676 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8af3eca0-2498-3b77-936c-7e05ee54e7e2 | -17.08215 | -43.36822 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73f278f5-4db9-3787-abc8-c6528f1d8a34 | -13.14311 | -47.93313 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4c26d54-2ec4-3b2b-bdee-9d3de0305cfe | -13.22396 | -47.84203 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dee08562-f5f6-31fe-9c3b-48470facbfdf | -13.33702 | -50.95232 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed611844-188b-3f6f-a645-2406c5cc797c | -14.89763 | -48.28059 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4f3cc29-aecb-3bc9-8f81-d33bd51f1588 | -13.5188 | -47.27761 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 752215bc-3930-3cf1-9fd2-cda144d4eda3 | -13.75598 | -48.0517 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b1793964-4adf-31c9-b6ed-a3f6db3f86fc | -11.68448 | -47.49917 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 189a61df-d64e-3404-89b9-1dca0c7657a3 | -17.089 | -46.24275 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38a669d2-e71a-3f45-8785-3caf71a5723d | -14.64255 | -48.30772 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 351bdd3f-df31-3b84-8a4c-1a45f28d9595 | -14.64875 | -48.2416 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2416911-ff8c-32ea-9621-f8244c5092d9 | -14.92052 | -46.89372 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84be5c7f-d8e2-31be-94eb-4749f56dc249 | -13.92847 | -48.15723 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README34.md)
