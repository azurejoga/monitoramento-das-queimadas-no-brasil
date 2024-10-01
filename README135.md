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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97fa88ac-d987-3607-9599-5ad97208d639 | -2.9019 | -50.74736 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4d65f23-05dc-3158-a672-1e0eac9cc7fa | -2.90127 | -50.75151 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b647ca6d-55c6-351e-8982-1164fd859886 | -2.90064 | -50.7557 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f89e671-8269-39e1-8c85-481424b65986 | -2.89919 | -50.72533 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ddf94cf-a8bc-3fb8-a607-fb71a37ea105 | -2.89885 | -50.64708 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23f8aad6-e377-3fb9-b52e-1e2c542865a8 | -2.89856 | -50.72955 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f434531-7161-3be0-8f85-0d24f9a3f7e4 | -2.89821 | -50.65136 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82cca88b-cbe4-3e65-ac79-c133d1e1ebab | -2.89757 | -50.65562 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dccf558d-edf0-3ec2-be31-06f0fe145527 | -2.89694 | -50.65983 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edfe846b-247a-3163-8989-ab1eb6949be9 | -2.89566 | -50.66838 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6454c88d-8893-385d-a800-fa55b83cb3c0 | -2.89537 | -50.75067 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad70146d-34a0-341d-a0df-09c60cea4ec1 | -2.89474 | -50.75486 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96bd381b-97bd-3ce2-8c6a-68e53ec9ccc9 | -2.8933 | -50.72441 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cc2b26c-aea7-3ba9-99bc-5a26a3902210 | -2.89164 | -50.65475 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937290c9-32f0-3551-b974-faffaa6e9131 | -2.89101 | -50.65895 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be8131be-8bf7-34a0-8898-e271e1bfb3a4 | -2.89038 | -50.66318 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 13a23fe7-0b89-3ab7-82f8-23a412773baa | -2.8891 | -50.67179 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9795b7c7-09f2-39cd-9659-604711a36940 | -2.88857 | -61.88447 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f2037d8-a5dd-3524-aded-ac777ffa31f7 | -2.88803 | -61.88795 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fba1ad5e-044e-34e4-9769-6fb85af17fdc | -2.88634 | -61.877 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d7bdd34-935c-3cd8-b84a-7d96554ded0c | -2.88579 | -61.88047 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b575e010-86d6-3caf-9ba0-165257d0f803 | -2.88524 | -61.88395 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd27213f-2c7a-33f0-a84b-ad35f51594b5 | -2.88509 | -50.65808 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cdb7410-dc5f-3f9d-8564-8e8d2f9842d2 | -2.88469 | -61.88742 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2148e6f7-e606-3716-909c-608291b85d39 | -2.88179 | -51.66134 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3129d2e7-4b96-3048-bbe2-b05003316ebd | -2.88123 | -51.66499 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63a0ad65-5f91-3af0-b5ff-e0b7fcc81c04 | -2.67723 | -51.70842 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e3f3704-95f8-31f7-8391-d30fde1ca145 | -2.88022 | -61.87248 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d53bc44-7424-36bc-8b25-8fad4ecbf9f0 | -2.87986 | -51.66349 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5285b73-9928-3b9a-9289-9f12f7c5746f | -2.87735 | -51.65316 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6320d52c-b102-3cd3-9398-9bd49602c238 | -2.87726 | -50.66999 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4f00397-30d9-3085-8a0c-ebd28d0c7e39 | -2.87679 | -51.65685 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e09e18-56af-3288-b34c-97e0ca268a0e | -2.87623 | -51.66053 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c678319-28d3-37c5-8e7b-4d1e598433c3 | -2.87568 | -51.66419 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1529eef0-39bd-39e1-a282-e73c14a25e80 | -2.8718 | -51.65238 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbfacd49-03bd-30f4-9b64-256d6c149781 | -2.87134 | -50.66908 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b3c98d6-1d1b-369e-bc5f-431eebd66d2b | -2.87123 | -51.65614 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe741f02-19cf-34b2-8a33-d3ed3a45eb38 | -2.86907 | -50.72504 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c11672ee-a0e3-3f52-81c4-c15b3ba9cff5 | -2.86379 | -50.71998 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 565231c9-6d6c-3cec-9bc6-f2747020c69b | -2.86317 | -50.72419 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8294da80-abb9-35c8-8947-1fef4e8fddd7 | -2.86255 | -50.72837 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abee580a-0041-3b9b-a5e0-ec8071a1fac0 | -2.86192 | -50.7326 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a52d1ead-e8b2-3073-b70a-e8d61cd6dcd8 | -2.8596 | -51.65798 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05908722-d54e-3616-86a6-02e72868ee07 | -2.85904 | -51.66166 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33955bb8-3ab9-33eb-9f2d-9c3005d85cd8 | -2.85727 | -50.72328 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ecba7fa-2870-3e7e-8e87-dd7654cf9b2f | -2.85665 | -50.72747 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ee374f-3c7e-37f7-be43-64fd72f8d3a9 | -2.85603 | -50.73169 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815fe69e-1710-3ca7-9eeb-60fe11507178 | -2.85295 | -53.31708 | 2024-10-01 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 901b360a-d6ea-3b98-b746-85ab440327b4 | -2.85292 | -53.31486 | 2024-10-01 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80d32b8f-84f9-3ffd-8517-23e4b1dfcd13 | -2.85206 | -53.32041 | 2024-10-01 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9728836-732e-38fd-a865-86cc9fff8095 | -2.68273 | -51.70931 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66db9e7b-866c-3b80-b3de-d6108d751d1b | -2.6784 | -51.70612 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91f0200d-66ef-32ff-b10a-fee4c4cb58d2 | -2.67786 | -51.70966 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 206ca34a-7341-32eb-8987-edf241f1ac52 | -2.33563 | -60.06776 | 2024-10-01 05:27:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22a0d10-614b-3f3e-bbd1-ea050f99cefd | -10.98728 | -63.95741 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca2d523e-ee24-3924-8397-c71c307a18bc | -10.88932 | -63.89398 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67a7f2b3-d45f-3a47-9f77-1b74676d58a5 | -10.731 | -69.47389 | 2024-10-01 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efed640d-0c14-3072-98a4-548a45eb6f5b | -10.71311 | -69.42142 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b264fcf6-afc1-3773-b8f1-1c588595c81b | -10.71233 | -69.42579 | 2024-10-01 05:29:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18b1b1e1-3028-3bd0-b0e8-76661fbca882 | -10.71102 | -69.40779 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f64689c9-5b50-3015-b6a1-6597da1a001d | -10.71026 | -69.41206 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0727def-0d11-3996-98cc-8868b523c4d3 | -10.70949 | -69.41636 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc3150e4-a179-3043-b208-db41cdc337d3 | -10.70871 | -69.42068 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11660e22-6bd0-38ef-be94-32464105c56a | -10.70509 | -69.41562 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ef59dbb-8f87-3492-8d11-95caa7783e66 | -10.70431 | -69.41995 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1066bfec-3740-3df8-a40f-07313d021b2e | -10.6846 | -69.38291 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f34f1327-143e-3a27-b8b1-02d6de7d4807 | -10.6842 | -69.38086 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3343ab12-bd7e-333e-b6ec-b92563b71528 | -10.61238 | -69.04689 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2848a54-bd3a-35fd-83ad-04f3911d0ed4 | -10.6081 | -69.0461 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b36ec42d-45e0-368e-8b00-1979b9ce9901 | -10.54466 | -69.30569 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4407a124-da4e-3de9-9227-b28fa1610a3b | -10.5403 | -69.30486 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d873187-d1ff-348f-ac98-5ea382645a52 | -10.53593 | -69.30405 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd8bf5a7-85ab-3638-8ba1-d70aefe1a4e2 | -10.52438 | -51.08892 | 2024-10-01 05:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c27a47d8-ac45-39df-88d4-86d35790a14a | -10.51796 | -51.08834 | 2024-10-01 05:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33ee3b3f-10bc-39cd-bbf5-ebdc7260fab3 | -10.5154 | -68.38248 | 2024-10-01 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d80ee10-f7bb-3faa-8cd9-c492e37a1693 | -10.48408 | -67.9103 | 2024-10-01 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a4f2dc3-6655-3aa3-94c9-64a778a55f0c | -10.44993 | -67.8935 | 2024-10-01 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4c85c30-6aca-39df-ba25-11272a8128cb | -10.43137 | -69.23425 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6337bfd0-515a-35fa-b08c-e602de532959 | -10.43062 | -69.23849 | 2024-10-01 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e609ac01-c19f-3f32-b0b3-af8dd0e09694 | -10.42399 | -68.58854 | 2024-10-01 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 150550f7-041f-323c-8583-e1c352d23de8 | -10.41633 | -67.94448 | 2024-10-01 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 669c7f02-eb55-3087-bb9f-9e41607fb1d1 | -10.35168 | -68.00198 | 2024-10-01 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f932a93-6a26-3ca8-a1a8-61393e23d54e | -10.31924 | -67.76158 | 2024-10-01 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe1054c8-71e1-3423-9acf-3a1d1e14dfeb | -10.27265 | -68.75974 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e031c4f-6433-3c4c-9052-b3ff5e1500ef | -10.27195 | -68.76369 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a600f0-c8f6-3c07-a840-0744807c41d2 | -10.12882 | -67.8942 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f28fd9ee-d81d-3c19-b93b-7fc0e17e1d3d | -10.1248 | -67.89351 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d672fb5e-e594-3bfa-8325-bba0da2022cb | -10.12139 | -67.88931 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdff8377-87f3-3ffe-86df-677b9c1bc440 | -10.12079 | -67.89281 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a303aa13-90ad-364e-8d39-e94d363a91e1 | -10.11338 | -67.88786 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed3f8fac-66b2-3144-8e76-bc76fb8bd0d6 | -10.07836 | -69.16544 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f57d3c45-9891-3a8f-9237-056f9194a13e | -10.07809 | -69.16757 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed058ed5-e776-3852-b2d5-cc1e03cb14c6 | -10.07489 | -68.23018 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c49bbe-b8ec-3afe-99a0-81b9ec3b4e61 | -10.07425 | -68.2339 | 2024-10-01 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c801be0-0989-3a11-b0f3-46c4fb46a5ed | -10.04832 | -50.3005 | 2024-10-01 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19771bcb-d9f3-3c3e-9356-440cd3befbb0 | -10.04472 | -50.29949 | 2024-10-01 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc25bbf7-4112-39a0-be3a-679f27b91aef | -10.04237 | -50.29386 | 2024-10-01 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a73eab-4388-3bc8-ba64-2a1549eec4f2 | -10.03873 | -50.29279 | 2024-10-01 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25391e0a-408e-3537-90f7-f19d1acbb66b | -9.96506 | -64.93843 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 060911c6-d601-3423-93b8-4b71d3db3c20 | -9.76063 | -65.65495 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README136.md)
