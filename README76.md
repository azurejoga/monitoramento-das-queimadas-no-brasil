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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9107f440-4405-3683-b493-db53dc1ed800 | 3.12531 | -60.56168 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8013746-c559-3bad-9731-0ab72ddc78e0 | 0.44203 | -60.53976 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9bd4766-7a0c-324e-921f-27a679fc0818 | 3.12602 | -60.56596 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a6134de-0369-3c2d-9d2c-e239902835be | 3.56037 | -61.34222 | 2026-10-06 06:18:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a4ea1cd-104a-302e-bd7c-7a7f9cca0146 | 2.01575 | -61.08956 | 2026-10-06 06:18:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7819da4-2323-34db-a28b-527296e3607b | 0.44135 | -60.54013 | 2026-10-06 06:18:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da88fbb9-4d1e-3b0e-a392-54204b6df1f3 | 3.12591 | -60.57544 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30354964-c808-3f2d-b043-af67eb24f6cf | 3.12517 | -60.5712 | 2026-10-06 06:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 557562dc-def9-32d9-bea1-51ef4cb997bb | -6.96127 | -71.49756 | 2026-10-06 06:20:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 310600d3-c706-3891-9ac6-51d36f8c8f6c | -7.44243 | -63.56253 | 2026-10-06 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d40a5ce-dbd0-3f3f-b18d-265f374ab168 | -7.44812 | -63.56331 | 2026-10-06 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcaa4ae7-8aa7-34e4-aaa4-6f61c402cd52 | -6.48353 | -62.86111 | 2026-10-06 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c0d8336-313f-3a25-9ef8-508d092225ba | -8.34494 | -62.82805 | 2026-10-06 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c14c48-9e15-360e-a165-d0ff5d262359 | -8.34977 | -62.83786 | 2026-10-06 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e05ac01-0a29-3fde-9919-240e8ba3d380 | -6.48296 | -62.86533 | 2026-10-06 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb7a5e72-d743-33fd-bc47-3dad8b94ce7a | -8.34434 | -62.83256 | 2026-10-06 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63468ac6-c14d-3c05-af27-73e6147e6191 | -6.96954 | -71.76138 | 2026-10-06 06:20:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55cecf1c-c78d-3bef-81e8-77dcd989e90b | -7.43675 | -63.56171 | 2026-10-06 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df242e5f-e5c5-3ed1-aa22-e93fb3bbe4f9 | -7.44863 | -63.55943 | 2026-10-06 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b103a1ac-7bb0-3a8b-aeba-3e3ae5e2603b | -8.5159 | -67.00734 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 505e3ef3-6925-37ad-82f5-c11ae6a98deb | -9.15618 | -68.26231 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 088dca98-5a81-3a69-bc3a-d9fa48b9a8f7 | -8.54276 | -66.98246 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2030011a-b45b-3ba8-bcc3-8c81e6281a70 | -7.66512 | -72.43211 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94d25fc3-4cb4-3b49-b745-1eb1d2259e4e | -8.79895 | -68.70935 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1686a6bb-85b0-397d-a217-1ada819fe8dd | -9.16462 | -61.40662 | 2026-10-06 06:22:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c799453-58fa-3cf9-8126-42b9d43b882f | -9.46272 | -64.33197 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fc46e3e-288f-324e-8c6e-14ad6f9a461b | -9.72858 | -65.08568 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1a39cd4-fcbf-3722-bbd6-1e9bc32edd87 | -8.60373 | -70.20062 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fbe480b-4c26-37d4-beda-db3a02a1920e | -9.67074 | -66.82832 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a72cc31f-e358-3190-8f20-68c490d6621c | -7.35969 | -72.61036 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49cb471b-9e16-3854-b9b6-fa280a97c6db | -9.15047 | -68.24131 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7488b4dd-b95f-3063-bf1d-742bde7b2bdd | -9.33444 | -68.79635 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143cd5b8-fc56-3960-8d01-15466397f60c | -9.4614 | -64.33481 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ac0d3b-970e-3dff-b40e-e2652e86353f | -9.72815 | -65.08894 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81c2e459-9c14-3ac3-9f58-f0889a53fdf9 | -9.33995 | -64.70922 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b40db60d-9a68-3ce0-886e-1b197b4bc664 | -8.41566 | -70.11205 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc74c01b-fcfd-3277-af65-ac9af2b7e59c | -8.84914 | -66.79743 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56545bc7-ee2c-312a-b610-65d13186466b | -7.36303 | -72.61088 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e42eb1e4-ab85-307c-942a-b003f67b205e | -9.13471 | -67.77162 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64795fc1-b7a9-37f1-a86d-350dc4eba2cf | -9.54439 | -64.82034 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22cd2ee7-0550-3133-beb7-d7e84c669ae9 | -9.73303 | -65.09282 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd4e7775-e8f7-3805-aa9d-b990cda005e7 | -8.93493 | -67.34723 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57e9b5c0-0f7b-3583-b7f4-deed137090db | -8.62641 | -69.50665 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129afd4d-a6bd-335e-99d9-15b281d78cfa | -8.84981 | -66.79256 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83772b6b-2f0f-38f7-ae29-1540dc14ebe3 | -9.12808 | -68.27829 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f74ac39-f746-35d5-8609-43477bb2c2f9 | -9.72114 | -65.10118 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51018718-3d09-3219-9d66-e8f3bdbe3450 | -8.92549 | -66.85007 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56101df2-de85-3519-ab7a-0d11fd2ede50 | -8.96818 | -65.4458 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd28aaee-52f5-34a1-9896-68e1dbc27c29 | -7.89107 | -72.35263 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ffcb80cb-2f56-304f-9a63-d76a5124c813 | -9.11388 | -68.31718 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab0224ba-7f06-3131-9d21-4a6f7d82a57a | -9.10207 | -67.74957 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e32e1512-3a82-3724-8b0e-d9fbf824945e | -9.15543 | -65.56652 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42367b10-3af5-3188-bed1-d7c9c04cd28f | -8.60714 | -72.72801 | 2026-10-06 06:22:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a8b1c5-3687-328c-94bd-6f332c8f2222 | -9.36801 | -65.80351 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4042bdfe-f156-3d86-8846-5cf4ce881af7 | -9.72242 | -65.09142 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd37e414-b750-3dd9-8560-d069f12a8e17 | -7.36325 | -72.84883 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fb61ddf-6005-3531-9190-fcfd884a0629 | -9.17048 | -67.67621 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548cdba2-b9ef-3e03-87a5-8c010a6e7d61 | -9.12873 | -68.21486 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8acd1078-531f-3808-9a8c-e8a5c6ecf145 | -9.12801 | -68.27925 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31c7f877-0c8a-3726-9e0f-d446d6e785f4 | -10.82901 | -69.26141 | 2026-10-06 06:22:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9484d7e-5e50-3877-b10f-a2a51b4f5d58 | -9.11066 | -65.35481 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6970c36-b24b-3ab1-a92e-fc5475da8f46 | -9.07776 | -65.39068 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16e5e41c-cc02-3a1f-9296-70fc07a081f1 | -8.87623 | -67.00466 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7080758f-ba18-3cb2-bc08-4d1f22804e37 | -7.81949 | -72.83739 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2de0b644-12eb-3cf7-9801-7827abe3ce5a | -9.34912 | -68.92482 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16bb93ce-4b5e-36d8-811e-ebb8f32a6908 | -8.62714 | -69.50176 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cab6aa9-44a9-3713-b781-0dd41bdda80e | -7.37258 | -72.72437 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db5c5b81-36f4-3c12-9f9c-a5cda03551ea | -9.14755 | -68.29321 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cecd4a71-c8a2-3aac-a114-2f3a7440ca8b | -9.09403 | -67.67647 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec4eae01-459a-314d-ac59-724f8d34de70 | -7.36358 | -72.60735 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b30b643d-9ae9-3cca-a690-138007bb7178 | -8.87464 | -68.53527 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c3b9a36-1f26-3533-a26d-b67b36e2d8d3 | -9.15673 | -68.25837 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a061d9c7-f488-3617-93d0-f6ea1b1411c8 | -9.15584 | -65.56351 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58377cec-0f2b-3631-9b90-e26473c511de | -9.48437 | -63.95538 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9d4f339-b2e2-3e19-8919-f3ff3d6994cc | -9.33497 | -68.79268 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b701ba-3d37-3e50-a2dd-d9506321b07a | -9.41246 | -68.88976 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 525b0296-6697-30fc-acff-1cca4af01bf3 | -9.50223 | -68.49802 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257911f9-af9d-3ce0-a397-685e24464831 | -9.67613 | -66.82388 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d69c538-0195-348f-96e4-1f88799d2e91 | -9.11078 | -67.81562 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3418ecbe-dce8-3529-867d-10c87b1568d0 | -9.82311 | -65.05455 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f643e6b6-a031-363f-b9d6-b35e731c5771 | -7.67709 | -69.95611 | 2026-10-06 06:22:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64e0d717-b267-3ecf-bf4c-32459f38ba4d | -9.10864 | -65.35706 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5abbad8e-2a8a-30bb-b3ee-c8095351fec7 | -7.88895 | -72.87349 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 638ada2d-513d-32fa-b29c-76d98f52e1d7 | -9.19319 | -65.3282 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf03e846-ff68-36e7-8816-8b9ae95e52ef | -9.7326 | -65.09606 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3ce115d-db40-32f7-a5aa-5bc5d325ec35 | -8.95068 | -71.83237 | 2026-10-06 06:22:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58d9ba1d-208a-3414-a9f2-bb1383a58f06 | -7.78631 | -72.09573 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a644cf8-093e-3643-9d64-5d8adaef2bf9 | -7.71605 | -73.04469 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c2c975-c42e-3770-a133-fd46d0d3f880 | -9.48313 | -68.94672 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 370adf81-40bf-3d41-9dcd-7569872d3055 | -9.13245 | -68.24669 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a488e3c-c66c-3aa0-bb13-fc77bd07f41f | -9.15894 | -68.24257 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1476890a-b33c-38dc-ab79-da11a846af71 | -7.36844 | -72.46642 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e762a759-7d14-357d-be4a-02dc6236520f | -9.4381 | -67.10021 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cec46ed-33b8-3628-96e1-9cf805685454 | -9.35318 | -68.92538 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdc15859-52d0-3c7d-bb7a-56cbf9f5eeb4 | -8.45205 | -70.21112 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06ce7d46-8af7-3f6d-92b0-67ec54486bb2 | -9.04066 | -65.43259 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99b46704-4f18-3c8c-a6fb-2faf32b64975 | -9.10306 | -65.35944 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef67df0-c010-3671-a0da-a47690570224 | -9.33905 | -64.71609 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56eafecb-5c8e-378b-9bd3-7753db8f96cb | -8.59364 | -66.81734 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb25bffc-f925-3e71-a5d5-d02d9082c5f7 | -9.1453 | -65.41027 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README77.md)
