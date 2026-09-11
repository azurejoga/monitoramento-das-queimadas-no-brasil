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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97f06622-d395-34ff-8fab-da8358bc648c | -8.50606 | -50.15335 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dfe6660-ca4e-3b38-bc34-10cf0bfefc03 | -14.60211 | -48.84847 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c297d096-f689-3757-a416-4a8a7fdd6002 | -8.50274 | -50.15049 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a99fc26-032e-36b6-b35a-39857d02afd7 | -9.48388 | -68.49558 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90cc61bd-1bfa-30e8-bbbb-520ebe257c77 | -10.36106 | -48.13206 | 2026-09-11 05:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fefbd6ea-1e6e-3af1-846d-6b0af5555d84 | -10.78706 | -45.94643 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97d6fdd7-8168-3908-9059-167d88fc0025 | -10.53267 | -51.34945 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7d2bf47-40a4-36e4-83cb-cee0f3bab5e7 | -9.08072 | -65.48206 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1395683-6548-34af-93f6-ff5a49468a08 | -9.23447 | -65.57464 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26ad3a5b-7cb3-3d8c-81be-8d9a473f1ada | -10.53778 | -51.35046 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6638202e-c943-32f4-9e6a-0a314c18b493 | -10.95835 | -49.64742 | 2026-09-11 05:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da1b64b3-9b2b-3ae9-830f-1d5e36ae985f | -9.03818 | -65.74791 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf75528f-f9af-36ad-9454-e5650057b703 | -11.81158 | -60.45489 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67437e41-dd20-3ecc-9cbd-adc05e275b17 | -10.53851 | -51.34495 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca2e49bb-8a6b-3efe-abbc-255d694646db | -10.05672 | -46.29004 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d27361ce-cac4-3f77-b2a6-34fcb8b2738c | -8.50319 | -50.14704 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d86e4cd9-b46a-302a-bc4b-a70df01c1211 | -9.07465 | -61.03189 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f8af36-fff7-3c75-8bce-e44c6be405c0 | -14.6031 | -48.85818 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99b57179-4108-33d8-b701-d7bed8e0f2f8 | -8.6374 | -66.50069 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 635d1ba6-09e3-3aad-a856-5bffdad75b21 | -8.48204 | -54.94425 | 2026-09-11 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26a9c9e1-7191-3bfa-9e25-27f2de3cce77 | -8.63951 | -66.51574 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dffe8554-ae17-3f33-8f9d-b28b3d13c351 | -9.01605 | -65.41033 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c847b5b-bde6-3a87-a4c8-dd31162352c5 | -11.80825 | -60.45435 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be83f78-bbb1-3a19-b678-a3b67b7bf29a | -9.04148 | -65.41492 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0b9b0be6-fa93-35dd-a833-1098a3a24821 | -12.15856 | -64.14318 | 2026-09-11 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8759918e-7b6e-3c12-b30c-3162ab8c26e0 | -9.09208 | -65.49232 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13089159-f235-314c-90dc-8a2746c88a5b | -10.05685 | -46.26986 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c6fee4e-4743-3060-a43b-b3a2add67090 | -9.08142 | -61.033 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62378afb-498e-3a42-bfcf-763d64c642dc | -13.49272 | -48.5594 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41cf55e0-0e65-33ff-89a1-bd365ddce2ff | -8.71674 | -63.98089 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a441475-3258-3ea9-8c57-2eb825512ebd | -9.1776 | -49.94822 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50d13e75-975d-3091-b37b-c275df5574c6 | -12.1564 | -64.13338 | 2026-09-11 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c9e04b89-8af5-3992-a14c-38261f4ebfa8 | -14.59468 | -48.85712 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 799389ec-3fa4-36a7-a151-295dd92267ad | -9.4099 | -65.86181 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a073d13-c7e7-3502-a79d-1720fcae7fcc | -9.15625 | -49.98699 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443b1d18-cb4c-3882-98ea-a7eceaf7bf39 | -9.7053 | -54.34521 | 2026-09-11 05:29:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ce52186-7afa-3c3d-8f64-2211a153f95e | -9.49041 | -68.49428 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d09bb12b-1c37-3761-b7e7-8b978ff8ed63 | -9.19186 | -68.20792 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e8ff18e-d10f-376b-9491-af649828bb04 | -11.81045 | -60.46195 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 418386f7-06e0-3290-b411-07f0b1f16a71 | -9.50091 | -66.78796 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f02a194-b6b2-369d-9653-cbd0983148b8 | -9.36812 | -49.37717 | 2026-09-11 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f90a388-e15a-308a-bef7-53c853052e4b | -8.98422 | -65.3924 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f49be9f-b42e-3a7f-8c3e-6d7c7076bef8 | -10.48463 | -48.64915 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 135f5f41-4eb3-34eb-b333-f8c97227c960 | -9.01832 | -65.44766 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b87b6a1f-d870-309d-808d-f449834edb8b | -10.97688 | -47.87816 | 2026-09-11 05:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 180236c1-2513-39d8-a72d-2bbd748273ea | -13.48032 | -48.55401 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 402b2c21-00d5-397f-9464-a52822a030f7 | -9.18512 | -68.216 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7724cb24-70f9-33ed-83c8-6105ed5a82a9 | -10.19343 | -68.76698 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c2dc2ac-a98e-3777-aaf1-78c117d880da | -9.41552 | -65.85774 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69c8d2ff-42a0-39cf-b3e6-2f2928d78165 | -9.18055 | -68.21208 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f9c09bd-0607-3c02-b818-93ddbcdd8b0f | -9.70967 | -65.08067 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185a8212-cac7-3c6a-ac4f-12a4207d8052 | -9.09278 | -65.48833 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5157991d-b427-376a-a0a6-d1f6530b3211 | -9.10556 | -67.68761 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fc4e3a8-b7a4-346a-801c-45739cc7d809 | -9.0848 | -61.03357 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d55f441-a49e-34b8-8520-d9edde9bdbbf | -9.41929 | -65.85921 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 156f52cc-f24d-309a-976c-c687ae4614db | -10.59954 | -60.78993 | 2026-09-11 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b9c37d9-40bc-31bd-a69f-721e822224c2 | -9.48923 | -68.50054 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efc0eab4-2e08-3dab-af0c-649de0ca011f | -9.75422 | -64.94534 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5f881a9-792d-390b-8140-3fa9ad4688d3 | -10.46613 | -48.65541 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3c381d2-e0db-307f-ace9-7a7f033c9e89 | -9.44108 | -68.26505 | 2026-09-11 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f6c81cd6-c9fd-38ef-9afe-d0f357816395 | -9.22739 | -65.59012 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b0583e-694f-3480-b1f0-d77ffbe0f1ca | -13.48674 | -48.55474 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e69a04b-e4c4-365e-8e7a-ed12e82aed81 | -9.41496 | -65.85842 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5627a978-8c50-3720-8d75-77ca8e2b41bc | -14.59671 | -48.85751 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b89ebb9-e644-30ae-95aa-f7a4f9c79f6f | -14.79167 | -48.08541 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15bdd7c2-8f08-313b-bfb9-4121577bc57c | -9.08083 | -61.03664 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7077c943-2552-3838-90bc-4934bb5226c8 | -9.18 | -68.21511 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cbd642f5-b549-3cad-bab9-b165c5dfe8fe | -9.48847 | -68.49981 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d161477b-f300-3d15-b342-51de711b8c59 | -9.17655 | -68.20505 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59047b17-420f-3297-afd4-86f8a4e68e88 | -8.53298 | -66.98518 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 838f2edf-b672-3b88-9a69-e52d741a612a | -9.08001 | -65.48606 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e4448f-1275-3ee3-b615-05c6f0c656a7 | -7.24329 | -59.51923 | 2026-09-11 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7bbcc49-2f72-3078-9937-8cc314396fd7 | -9.04455 | -60.44229 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38c0ab03-973d-395d-8fb8-5e9836795029 | -9.2167 | -65.5755 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40ca3bf5-8b6b-397a-94e2-1d10d241717d | -9.46451 | -68.83562 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e88314ab-83d9-34e8-863c-4945dbaebf54 | -9.00903 | -65.42548 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc5c47ed-c5f4-39e1-8f3a-b920742054d1 | -9.17279 | -49.94837 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 394080c2-73c7-36a2-8ab1-f0a77ea3a5c4 | -8.70583 | -49.62292 | 2026-09-11 05:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e12a6b1b-eebc-3e6f-85ed-5317637762ae | -13.49973 | -48.55477 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 124bce3f-2b76-3fcf-87c5-d69af0719901 | -10.17936 | -59.63163 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef3857a7-29d9-3519-8d3d-c7e94b21087c | -10.17991 | -59.62813 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1bf9f2c-309a-3d15-ac15-72d0e0c5dc34 | -9.02751 | -65.44519 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b4d4a75-662e-3a25-a31b-9c43867f9567 | -8.9892 | -65.41376 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9c4a0f6-b8b4-3c0f-965c-23a9e9f02399 | -9.19132 | -68.21091 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f63eb251-d9c0-3f44-b870-791655579507 | -13.50626 | -48.55444 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ce36806-999b-34b9-8411-5f550d9777c2 | -10.19282 | -68.7702 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b801ffe-5c7c-3eec-9877-34f0e283a4fc | -9.3898 | -55.97215 | 2026-09-11 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63f0672d-e89a-3c43-8973-8c67fc327d0a | -9.34828 | -65.68035 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55e29639-f178-31be-bba5-ee84dc044d35 | -14.60359 | -48.85353 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3115a36f-8403-39b8-9284-239c57b4c238 | -10.9826 | -47.8853 | 2026-09-11 05:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fdcdc54-c295-31c0-916f-3cd6777481ba | -9.34606 | -65.68117 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2921690b-3498-3c84-abb7-3d708ad6c0fa | -9.04572 | -65.41569 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1cd88c5-096c-3fe6-b3da-c747a4c33d78 | -10.54288 | -51.35149 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d9ba203-cee4-38a9-88f3-6fdd4aa95789 | -8.99275 | -65.41849 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a6c8b04-b81b-34ea-8aec-7e4bc4a87674 | -11.80492 | -60.45381 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2045d43-493e-377a-9b93-84c51b0eb38b | -10.51312 | -54.34732 | 2026-09-11 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c9f9c88-306c-3527-9cbc-80c6bd512f41 | -8.82594 | -63.81319 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6cd5096-dc8f-3822-a5f3-1a8115e743a3 | -9.1723 | -49.95203 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79f61eba-ff45-38ef-982c-968edcb4dd83 | -7.75575 | -66.91534 | 2026-09-11 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b578ec8-e429-386b-88be-71e227ebedc1 | -10.54763 | -51.35519 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README28.md)
