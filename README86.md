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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a89ff95c-f4d5-3a25-8252-1f8eaa504b71 | -16.41488 | -57.36566 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 84664a8c-2ec3-35fa-b1a3-861988e65edd | -16.41157 | -57.36414 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 33c1725d-b377-3cb5-b326-743c14dae8b8 | -16.40982 | -57.35911 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e083370a-6b15-35c6-9d4c-92dc2b40a654 | -16.4065 | -57.35752 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 29383ab7-1248-392c-8507-2d46a141e775 | -16.40366 | -57.35757 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 89d34b3c-4f9d-3f73-9ac6-b20811fe2d74 | -15.72886 | -57.42126 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a51467e7-0178-3c81-9151-6d60beb4eab2 | -15.72771 | -57.42644 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e9477023-0d88-3896-99a2-bed6743f5c90 | -15.72276 | -57.419 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3efb2855-ce4a-3df3-8983-709c48f879fa | -15.71754 | -57.41277 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3116cd4c-ce5e-3e64-b221-c634e33409a9 | -15.71408 | -57.42838 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8192f429-96d1-34ec-a690-e9d2ec637efa | -15.71317 | -57.42391 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a9ac77f-2123-3b78-a9e9-8448d14b87e5 | -15.71284 | -57.43395 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73fa35d5-383f-3db2-8448-b925f98ac22b | -15.71188 | -57.42996 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6e57a4a-b59e-3112-a587-e5ce4e16e6da | -15.70564 | -57.42828 | 2024-10-05 04:17:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85873b9a-042d-3948-b895-63f1a92a6b32 | -15.57175 | -57.45647 | 2024-10-05 04:17:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb0e68d0-7974-3995-ba5a-4f877e9945ab | -15.57061 | -57.46175 | 2024-10-05 04:17:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eec542a8-ad56-39a9-8ba8-ffcbfeb74260 | -15.56947 | -57.46698 | 2024-10-05 04:17:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d6e1bb0-e16a-3c5d-aa61-aed9d3b3629a | -15.56545 | -57.45496 | 2024-10-05 04:17:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b21088d8-6aec-3c06-98c8-6d093f3878d8 | -15.56431 | -57.46019 | 2024-10-05 04:17:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14fea0dd-bc6e-3816-ba54-4cd9cc84cf4c | -13.92006 | -50.84299 | 2024-10-05 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c41d50-ddb3-31cf-bccf-280cbd34da2e | -30.88222 | -52.48907 | 2024-10-05 04:19:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 134c9212-d891-37ac-ab52-7fc5a63c4751 | -30.87864 | -52.48817 | 2024-10-05 04:19:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 33fa13fb-2bfa-300c-a4a0-93df93b1b991 | -29.81481 | -51.17616 | 2024-10-05 04:19:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| f4b57652-210d-3ab9-82f8-fa6537286e61 | -29.80443 | -55.71667 | 2024-10-05 04:19:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| b08dfd07-2abf-387f-b5a3-30dd94e70337 | -28.92301 | -55.59584 | 2024-10-05 04:19:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b6ce8af9-d9c7-36be-ac6d-596909d2e018 | -23.98401 | -48.91887 | 2024-10-05 04:19:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f5fa3d6-2fd9-3e63-b6da-ebfa7ef5b329 | -23.47721 | -49.18252 | 2024-10-05 04:19:00 | NPP-375D | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c6bf1ef-dae6-363a-bd94-d0498888d468 | -23.47651 | -49.18656 | 2024-10-05 04:19:00 | NPP-375D | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5907201d-abd9-3564-ad3b-6531c9cf17a2 | -23.47376 | -49.18187 | 2024-10-05 04:19:00 | NPP-375D | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19179d82-006f-3e85-be9a-a54232f79a6e | -23.47306 | -49.1859 | 2024-10-05 04:19:00 | NPP-375D | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e450f5-84db-3fea-ba6e-e91f65d7758a | -22.8379 | -48.41079 | 2024-10-05 04:19:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46e2d403-4782-3829-bbf0-48961de2c249 | -22.83727 | -48.41458 | 2024-10-05 04:19:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeead8d9-8344-300f-8679-70f0a680ad8e | -22.5385 | -48.81433 | 2024-10-05 04:19:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc4fc478-70fe-36c6-b259-7217cdb00440 | -22.3708 | -47.93811 | 2024-10-05 04:19:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e4a679b-0820-3b9e-9725-ed13f98b36e0 | -21.66292 | -54.82642 | 2024-10-05 04:19:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0bb4b2c7-41f5-3fc7-8741-b1ee39155805 | -21.66175 | -54.83204 | 2024-10-05 04:19:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f245d7f3-3e51-34b3-84a2-2b35042a1b3f | -21.65814 | -54.82524 | 2024-10-05 04:19:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d38c42ae-5241-362b-a2dc-a48305df93bc | -21.65697 | -54.83084 | 2024-10-05 04:19:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f72a40c0-13ef-3562-900f-0498c0c617c3 | -23.78276 | -49.92078 | 2024-10-05 04:19:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4f21dd79-2d34-3baf-977e-afcd65f1ea59 | -23.782 | -49.92512 | 2024-10-05 04:19:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| faef82dd-14e1-344e-aa20-c9fdd3f500a2 | -23.77847 | -49.9244 | 2024-10-05 04:19:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cfbb00aa-766f-350f-9246-405ab88ef6d3 | -23.65557 | -47.4309 | 2024-10-05 04:19:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cb8ca4ab-ccb8-3846-b285-aaafc79f4b3e | -23.65224 | -47.43028 | 2024-10-05 04:19:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfc23e6c-8553-3e9d-a393-86e65434285c | -22.77219 | -53.3689 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fc2583b8-cf47-346c-a11c-fe610e45f2e5 | -22.77122 | -53.36528 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 31be5d50-2f71-3041-aded-15bb1df9f1d7 | -22.77036 | -53.36966 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7e02d6e5-cada-3ace-9dbc-88b5035cd90a | -22.76967 | -53.35917 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 284c53f1-bac2-32e9-89e3-bcccba7b7a45 | -22.76879 | -53.36353 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b168bf3b-a607-3787-9a09-75c70fa54b4e | -22.76779 | -53.3599 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 527262fb-4274-30a1-8fee-ae6813f2868f | -22.76694 | -53.36427 | 2024-10-05 04:19:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8b51b5ad-b91d-3b2c-810e-2a736e1ce613 | -22.39339 | -49.27488 | 2024-10-05 04:19:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| df280ffa-2eb5-3a18-86fd-0ef07b17f4b5 | -22.3899 | -49.27421 | 2024-10-05 04:19:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 513ab77b-abce-3724-b9ff-5125e2424796 | -22.38364 | -49.26871 | 2024-10-05 04:19:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 343badc2-8b1d-31c4-80d5-d83752ef8568 | -21.90034 | -50.71996 | 2024-10-05 04:19:00 | NPP-375D | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aa16afda-d33f-345d-ac40-6c7012295114 | -2.9015 | -50.6933 | 2024-10-05 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 33c6cb4f-4e35-39b9-b3f7-4b1579c15f42 | -3.3084 | -50.451 | 2024-10-05 04:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0d73495c-063d-3c85-a024-5f4f5aa5441b | -6.9515 | -59.0473 | 2024-10-05 04:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ff9ec513-adad-3046-9869-5b7fcac4f1a4 | -6.9514 | -59.0666 | 2024-10-05 04:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 6f2d0046-8e3c-311e-b85c-64e5e510c633 | -7.5193 | -63.2558 | 2024-10-05 04:25:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b6644d98-ba85-316c-8d6c-5911d7434cf6 | -8.7844 | -44.8085 | 2024-10-05 04:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7bc04bc5-781c-331a-9ae7-26aa09ba87c6 | -8.7655 | -44.8106 | 2024-10-05 04:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 153.3 |
| c88da6f4-c6e7-3685-a62c-588edcdc1591 | -8.7652 | -44.8335 | 2024-10-05 04:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1d8ab4ce-8d15-347b-aaa8-6da550dae38d | -8.7959 | -49.9533 | 2024-10-05 04:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6f7bd61d-4063-31c9-aff0-a3a842b690ed | -8.7774 | -49.9336 | 2024-10-05 04:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 16b3b9f6-f3d6-3399-a156-a8e58867e591 | -8.7772 | -49.955 | 2024-10-05 04:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 15a88515-1f37-3f20-b4a8-5fc9931f4854 | -10.332 | -50.5109 | 2024-10-05 04:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bc6c92bb-2f6c-3da1-a988-eb6c061066bf | -10.3134 | -50.4915 | 2024-10-05 04:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c091cfdb-d964-3983-935a-521a52b747f9 | -10.3131 | -50.5128 | 2024-10-05 04:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d15bcc50-82c1-341a-9b4e-6ad48309071d | -11.2365 | -46.9821 | 2024-10-05 04:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 074054f6-ad9e-3486-9ce5-4a64015b69f3 | -11.2566 | -60.5825 | 2024-10-05 04:26:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 66d04331-5ffd-3015-bcf6-10b8b8443a90 | -14.0144 | -47.2541 | 2024-10-05 04:26:25 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d55bbabc-384d-3e13-8685-4d9e51e8446c | -16.5544 | -57.2032 | 2024-10-05 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| b453bf42-49b5-374a-92bb-17534a9c51c5 | -16.554 | -57.2237 | 2024-10-05 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 34b32d5b-6e4b-3673-902f-ce893c78e7b9 | -16.765 | -57.4652 | 2024-10-05 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| eb43b4d3-fbbd-3c5d-bada-ac287bf6e2c2 | -16.7647 | -57.4856 | 2024-10-05 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.6 |
| 46c09a25-0f96-36c7-b74b-350d45d0ebc6 | -16.6871 | -57.4536 | 2024-10-05 04:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 1d790185-823e-3af4-82dc-5a7a49f52037 | -16.7843 | -57.4834 | 2024-10-05 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| e6bf2695-d428-33bc-95af-805d49571467 | -17.1185 | -57.3834 | 2024-10-05 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 349ada97-63f2-3ce4-87d2-fb8bd53fd800 | -17.1178 | -57.4244 | 2024-10-05 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| d0efaabe-dd89-38f3-92f6-72f9aae11432 | -17.0516 | -56.6725 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 611c6429-0384-3966-a0fc-703c9cc9d5ab | -17.1381 | -57.381 | 2024-10-05 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 78d7267b-b807-3a7f-924c-315463766392 | -17.1235 | -51.7238 | 2024-10-05 04:26:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| de6b0bb0-7059-3ce7-b20a-d28ac81448cc | -17.012 | -56.698 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 68475be4-f0e9-37ab-b4f8-46eeb0f073be | -17.0512 | -56.6932 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 9dd123aa-f739-3a25-83ae-8b95d5252a1c | -17.0319 | -56.6749 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 172.8 |
| f49b77a8-6d4b-3fa8-b8ce-9f80db51c12d | -17.1378 | -57.4016 | 2024-10-05 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 170.6 |
| ff9e4ea6-289b-3ada-a4a3-93b95b5be744 | -17.1182 | -57.4039 | 2024-10-05 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 188.0 |
| 107a8b06-8236-3926-932d-78c12c1e18b4 | -17.0316 | -56.6956 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 221.3 |
| 9fd5bfb5-cd64-33da-afc4-cb194f55c3e8 | -17.1085 | -56.7892 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| cc11af21-cdef-36d3-825d-ecd8b36b98f7 | -17.0123 | -56.6773 | 2024-10-05 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| 3822f7fb-9e5b-3359-8a92-2240d039ed43 | -17.1375 | -57.4221 | 2024-10-05 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| ee383d47-37ae-3bad-a672-d028f706d8ca | -18.4158 | -49.7588 | 2024-10-05 04:26:48 | GOES-16 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 93da5cc7-faab-3ead-a77d-bced58af1509 | -18.5062 | -52.8193 | 2024-10-05 04:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c58e35ec-e062-3de9-a356-54c314fd9f2f | -18.5058 | -52.841 | 2024-10-05 04:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 623.5 |
| 6708609c-7c99-3eda-806a-d24b7c014ca8 | -18.5053 | -52.8626 | 2024-10-05 04:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 31dc8b14-c848-330e-9b93-f3998305888f | -18.4858 | -52.8442 | 2024-10-05 04:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 175.7 |
| f517c040-9a62-37fc-b76d-e2541d73d4c8 | -18.4853 | -52.8659 | 2024-10-05 04:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 37ef5628-becd-3583-b8dd-c052be95a771 | -18.6785 | -57.2734 | 2024-10-05 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.6 |
| 026e5ccc-6f7f-3987-9140-fa2f50ed5af4 | -18.6586 | -57.2759 | 2024-10-05 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.5 |
| 1668f75b-7d2e-3dba-a468-cc52e9575482 | 2.17509 | -50.69596 | 2024-10-05 04:34:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README87.md)
