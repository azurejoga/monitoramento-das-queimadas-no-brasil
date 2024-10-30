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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6201040-af76-33e1-9ecd-9dc83858325b | -2.85316 | -53.34515 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd57bbea-4da1-364e-9287-14e1568e183e | -2.84589 | -53.34403 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb29930c-7b63-3dfa-bfda-44c494b26385 | -2.84522 | -53.3483 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cb5d929-c6ed-3956-b386-b85bb1550725 | -2.78407 | -52.09404 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c67bb74a-aa84-31d0-a2cb-c6fa528e35be | -2.78064 | -52.09347 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ea2f8c-7c05-3d67-8aa0-6339dc539784 | -2.7772 | -52.09291 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c1466fc-d89a-3376-9af3-c2b4f25cb1b2 | -2.75784 | -52.05958 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48931207-cf10-3ca9-bc16-3ee65f4aa3ec | -2.2378 | -52.23885 | 2024-10-30 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 289dc3f5-d6e3-3491-87ff-c896505f3ba0 | -3.45222 | -52.86164 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 04c3019c-5867-3369-985a-89f97a612a19 | -3.45159 | -52.86562 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3c4914fd-eabe-3dba-b074-b505677ac2fd | -3.38803 | -52.4478 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f107c9ff-dcca-33a8-acb6-ead27d0fadea | -3.31162 | -53.37371 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9251827-a866-3044-8005-53f22f51d995 | -3.22395 | -52.18471 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7f537e5-9f8b-3458-b3bb-5e559507f050 | -3.20996 | -53.40086 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6556a294-57e2-39d6-b972-5c0817f04fba | -3.20634 | -53.40028 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 500337ff-6470-337a-bebf-038faaedd27d | -3.05823 | -53.25187 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dfb2ac4-fc3c-3996-9a43-7399aa81195b | -3.05757 | -53.25599 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9909e242-59b6-36e1-bdc1-855d60d346c4 | -3.00289 | -53.43562 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38923f8c-40ba-3db9-86a1-233cd990c22b | -2.99994 | -53.43072 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 822b16bf-f61c-3471-bfdb-1138311073ac | -2.99925 | -53.43499 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33c8c702-7188-3fdb-8429-1a6a2f75aff1 | -2.99857 | -53.43927 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02708570-7d41-3cdc-bd70-f972c331ad15 | -2.99562 | -53.43438 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7dda916e-79ec-32a0-90b8-af403d2f657e | -2.99493 | -53.43866 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bed2fb94-217b-3afb-b14a-d4591ab453fc | -2.98201 | -53.26538 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e8da87-edff-32ca-a0de-8ff3664cbb82 | -2.97694 | -52.8549 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ca88e37-dde7-3019-bdb3-01615b0334e0 | -2.94714 | -52.56518 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 766a25bb-5640-3f6d-95ff-6273b5a37376 | -2.94653 | -52.56901 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b3fd9d5-ee5f-3893-9a19-d9e8b0726673 | -2.94364 | -52.56465 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 064e715e-c9c0-3da5-96a1-6289910d2590 | -2.91007 | -52.59505 | 2024-10-30 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 899aa05b-ab5f-3354-8ab3-ce12cd9308ee | -2.86883 | -53.3428 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0c3c476-e62b-3518-a040-64a9835a83bf | -2.86744 | -53.35131 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c7bb556-dc3e-34f6-a87f-635249786564 | -2.86588 | -53.33799 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abbb2275-1620-3cba-bc34-6732387dc957 | -2.86453 | -53.34634 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b601ffd-e206-30e6-acad-a553a8cccb58 | -2.8624 | -53.33378 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c799d62-cbc0-3c63-adee-73da4a655ffe | -2.86174 | -53.33794 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d322167-cc06-3a32-900d-891e15fb0b94 | -2.8602 | -53.35004 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82b8026b-d6e0-3fcd-99a1-5df28768c3c8 | -2.85864 | -53.33673 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94fd79ae-bdd1-32dc-933b-4afce02767ec | -2.85728 | -53.3451 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 041637ce-b4a0-3628-9131-e48973001b09 | -2.8568 | -53.34574 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cec40cb-426c-30df-8da4-d7448a77e996 | -2.85382 | -53.34095 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dc55c91-f324-36b4-ab3e-c5f1edea97cd | -2.85364 | -53.34452 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4b4b5f2-e89d-3fe1-ab7a-7a5e40a035fa | -2.84854 | -53.32724 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 814935bb-d46b-311f-93d3-87c3c9bbc0ac | -2.84491 | -53.32667 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b02331d6-f885-3507-bf5f-8ceff6704654 | -2.84226 | -53.34344 | 2024-10-30 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dd679fa-e947-3055-836a-cd441600c84e | -3.67864 | -52.26988 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d65cab8-daba-3b18-b627-2b5662940094 | -3.67806 | -52.2736 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8778690c-fe66-3646-aebb-5ee208cab646 | -3.67734 | -52.27295 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9eaaa0ec-c032-33db-bc47-c70c4376e4d3 | -3.83094 | -52.40749 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dff115a9-0521-3be3-8200-1bbf17b01678 | -3.78265 | -52.39975 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d65b8109-eac6-32d4-8878-03faadfc65e8 | -3.7792 | -52.3992 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1a3ccc0-5963-332f-bc54-f74cfa5422fb | -3.72059 | -53.75317 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29421c70-6394-3860-8738-e1d7c24eb238 | -4.30002 | -53.7213 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9a1c56-362d-3851-a6cc-6d75d8253cb2 | -4.27417 | -53.62671 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1887fca1-348f-354e-ab99-e51ac3633c7e | -4.25537 | -53.62799 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c97d303-67fc-3241-92d4-b5cf6125affb | -4.25469 | -53.63215 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37963e47-c451-3431-a66b-20153d8875f3 | -4.25242 | -53.62325 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fbf03de-be94-3934-b82b-4d56be05a754 | -4.25174 | -53.62741 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eee0c4e7-cd16-3ecd-b638-72ce625c43ed | -4.21624 | -53.86888 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4911c6b8-3e13-3037-a227-8b4c5447ac57 | -4.21257 | -53.86828 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 977d75af-72d9-3304-89bd-79eb27e796a3 | -4.1964 | -53.46204 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60e5cbef-dd56-39fb-9f7c-aa6157772735 | -3.88366 | -52.38052 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8af55aaa-b02d-3356-a797-ef7718c9f516 | -3.88083 | -52.37619 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a6a98a3-bd6d-35b4-865e-d137862d8509 | -3.88023 | -52.3799 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53c01e1a-111c-36d2-aa2d-544f8aad6090 | -3.87828 | -52.37628 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a16ea2c3-d682-3576-868f-bce4192c46e2 | -3.87769 | -52.38002 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13670722-7c15-3065-9b72-e257ee59338a | -3.87709 | -52.38392 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84e77d68-719b-32fd-9e71-3d39545b2a81 | -3.87679 | -52.37934 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9202bb5a-6669-303c-a16a-3e500c31578e | -3.87616 | -52.38322 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8ceef1d-2f5a-3c43-9497-889680b8c407 | -3.83035 | -52.41122 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbc58a29-f0d0-3ef3-b5bd-466d231ae86b | -3.77981 | -52.39543 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64084c89-ebd9-376a-afe3-9cd30562dc93 | -3.71251 | -52.42818 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7fe940d-9770-323f-beb6-83355c6241fa | -3.71692 | -53.75257 | 2024-10-30 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d533ea0-a3ee-3d22-82ba-99f079b57cfc | -1.64736 | -53.86998 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34b6a5fb-0c77-34ec-a64c-f2e6cef1e70f | -1.64663 | -53.87463 | 2024-10-30 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da758ef0-7eb3-35d1-add8-f09a9042a06a | -1.49833 | -54.86194 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1518815-b962-33e9-a5c2-87607c9e40c5 | -1.45523 | -54.07761 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19b42244-67f1-319f-a12d-04fcec6fb5cb | -1.44906 | -54.21435 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ae137a0-ed11-3a65-921c-60c450daba17 | -1.44518 | -54.21372 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc23e089-5410-3c68-9848-e6f6ef7cf0f0 | -1.43819 | -54.2076 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e437c03-9486-3f3a-8668-d9968c67f927 | -1.4374 | -54.21246 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e7fa642-72b6-3cbb-84ad-a3b8e6dfa9b9 | -1.42188 | -54.20982 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c074c3b-6a1e-336c-b254-f45c86865c9b | -1.41626 | -54.21651 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f94f0a5f-f7f0-312d-bfb8-a48566bf206b | -1.41552 | -54.22128 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52cf9f69-17db-3637-905f-443a01311d0a | -1.41254 | -54.21816 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e40a7bfd-03a6-3010-b9fb-3ac15a8c950a | -1.41237 | -54.21593 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d14946c-15f8-361b-9c29-25c7b297c447 | -1.07121 | -53.65746 | 2024-10-30 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e2f7cfa-8b33-366f-acdc-c52c720db95d | -1.41177 | -54.2229 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dbd83f1-d5a8-372f-bd34-7289e25da145 | -1.41169 | -54.54804 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acaedc36-82af-316a-a500-ffaa88b37e43 | -1.41161 | -54.22076 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88aca3d9-0a6e-33d6-907a-ec16bfe22ebd | -1.39335 | -54.10927 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfaba638-9c7e-32ab-a5a2-3c1239b6a3b5 | -1.35161 | -54.61657 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 301459c2-e781-3483-bc06-eb0b718ddd88 | -1.3502 | -54.61443 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22f24a07-3b67-31db-926c-7046653f2d49 | -1.34442 | -54.65153 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f638c9c0-f8b6-358b-a1d6-f0481fe64b44 | -1.34388 | -54.65497 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f734cfc6-34ac-3856-9860-ae5628a0a887 | -1.34096 | -54.64742 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a29b619a-8ca4-34c9-88c9-10e279dc7569 | -1.34042 | -54.65084 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37659dca-d428-3418-8f9d-b26d7f11695b | -1.33989 | -54.65428 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce24acbf-c620-3ab9-b125-11fa016d5059 | -1.28781 | -54.67186 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7debcd79-e442-346d-89c3-478e848b00bc | -1.28725 | -54.67538 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b298e78e-15f6-302b-8a1f-0a77b864915e | -1.18919 | -53.91008 | 2024-10-30 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README67.md)
