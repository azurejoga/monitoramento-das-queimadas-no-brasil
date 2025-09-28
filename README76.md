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
| 0963a327-18e3-3443-8621-f5a3de1344be | -14.84035 | -45.38697 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b7c7d18-206c-30f6-8fa3-b9f7ec84a40c | -19.11998 | -47.03049 | 2025-09-28 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fcfe9473-b9fd-3a82-a0b5-ff54bad63409 | -17.73527 | -46.70294 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc68678b-95d1-31bf-a830-ae4179a0c6dc | -15.31848 | -56.80456 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed12d7d1-174c-3887-ba4c-486439fb59ac | -15.53941 | -47.91302 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f33b2743-c3cc-33e6-9731-e94462de4ac6 | -15.25564 | -49.41328 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2505a961-c22a-320b-ad88-337d879141c0 | -12.97767 | -49.43602 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d14998f-a50f-3fde-8ba4-660b420f2411 | -12.99346 | -49.44622 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be37f728-2110-3d43-9826-41b5366a3a90 | -15.03817 | -46.96238 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef09d5e8-959f-3bb7-b9a4-273294c9c4c0 | -16.40091 | -43.71863 | 2025-09-28 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4fc2e6a-4aeb-3958-a7c3-59c584950eaf | -13.3152 | -47.30975 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c383edbf-9e42-3aa4-99ef-00969775ebb2 | -19.85527 | -42.59778 | 2025-09-28 04:27:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| de672fe3-637a-35ba-badb-e7672a012262 | -15.46426 | -50.23222 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9f149b6-cb24-300e-930a-002ea99f7b2a | -19.32871 | -43.82811 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6756d6c-93b6-318d-bdd9-d9a3b54cb8e4 | -15.97347 | -50.87449 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2ee13ec-27d1-32f9-8254-eccc2e995c31 | -16.64521 | -47.91724 | 2025-09-28 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88b89e0c-1407-3bf1-b3ac-b1ade44e2225 | -13.62379 | -48.06823 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54c02c8e-9984-3643-a0a3-2d64bc5a8e36 | -13.51876 | -47.39746 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2064caf7-56df-3afd-a9f4-34c0844b390f | -13.40336 | -48.15154 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4056f241-3be7-385b-8c00-8ab211c6d75b | -13.32405 | -47.31841 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 266bd1e4-d551-3615-b626-2ada7a683602 | -15.03482 | -46.96186 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6d92fe3-0e3e-3060-b4be-a7cc0246ce61 | -14.07839 | -47.00751 | 2025-09-28 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfa7772c-e08c-3861-ab78-1c06521f3602 | -14.47964 | -48.58216 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93aa3881-b44a-3aaa-be1b-20dc5727b382 | -15.95905 | -49.85221 | 2025-09-28 04:27:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8705ffb4-6f1d-3c4e-8d9a-0b128e84830c | -15.5383 | -47.92016 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b08cd364-b781-363e-8741-14f4097f2ec8 | -18.17603 | -53.31836 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20b58340-d52d-316e-9da1-4757e473ff94 | -15.46084 | -50.23163 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b0c5763-4753-3c4f-abb0-c0ce45fbce75 | -13.60002 | -47.29062 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce867956-4fa8-3a8a-8879-ef01207ab543 | -12.93942 | -48.81522 | 2025-09-28 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dc2ae85-9167-360f-ba3d-737e605c3ae6 | -14.58567 | -48.25624 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff532c85-d928-3e81-bc29-705c21b0a998 | -15.31648 | -47.88407 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f07bbf1-40a9-3dcd-a406-e7e9270d82cf | -13.63098 | -48.06578 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 169939fd-7809-35d8-be5e-6d613fcab038 | -13.18977 | -47.43865 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76342506-4df9-380c-9603-707a2dbe975f | -12.96374 | -47.21342 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c09b3dc3-7d7e-336d-9c7c-d1661ba0f9fc | -13.52152 | -47.40158 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 523f2e51-b535-34f4-92cc-c2972a323202 | -14.33466 | -44.50113 | 2025-09-28 04:27:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e66dfccb-8da9-3a6e-bea2-b5c933c26565 | -15.60434 | -53.16448 | 2025-09-28 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46771cce-64f7-3f40-93a5-6c6c723bc5a6 | -13.76493 | -47.88396 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b494a7df-22a6-37a0-b783-b002557b9a72 | -15.43721 | -48.21825 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69d3264d-62bb-3115-9d8e-70038605b03b | -13.79521 | -47.92893 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13c4fc05-9499-3bc5-a1c3-4df323f27040 | -13.01199 | -49.46109 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 355657d4-c642-35b8-b256-87575d165bcb | -13.71617 | -48.34114 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6258b95c-4539-3838-a000-713fe5d5c4c8 | -13.7826 | -47.87961 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7619756a-b82f-397f-a5f1-1b0a9bd169f3 | -15.02369 | -47.1465 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f657b79-dcd0-3273-b34b-605e27462b5d | -15.03427 | -46.96546 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d79232b-7860-39cb-9774-85db3fab95eb | -18.84544 | -47.98733 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 386b7540-872f-304f-be71-7e0633a4b8fe | -14.87663 | -47.98314 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b99d880c-3cab-3ecf-991b-73c004a9517e | -13.02621 | -49.45962 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fef77c19-0ac0-300f-ae7a-580799ae669f | -13.63796 | -44.41737 | 2025-09-28 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f27fd715-bcf2-3da6-8496-e5820c2b1027 | -14.54995 | -41.66266 | 2025-09-28 04:27:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f552306c-cdb4-344f-b374-ba9c5916292e | -17.7215 | -46.70079 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dec6ed5-c0c6-33a1-959a-7afad4fb9e2a | -13.00582 | -49.45609 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d8390116-3eb4-3b1f-800f-6a058c3de3f5 | -17.18627 | -43.37441 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d959ab02-ffae-3e71-a8e2-2d6bc47a01ab | -15.53499 | -47.91961 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d465c5cf-25a4-3893-ad10-7bd50c65313e | -12.98789 | -49.4376 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fb257e0-21b1-3df2-abc5-41ec39a04255 | -13.64423 | -48.06793 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49dceaa9-9ff5-359c-ac1e-6f39805747c9 | -12.99964 | -49.45111 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ccd88a9-34a9-347e-9f7d-4ea10f6ec2d7 | -13.83936 | -47.9509 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b31f844a-fe5f-3d62-95dd-b209d647efcc | -12.63906 | -51.68652 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91a109aa-aeb2-3f88-b6e0-5fbc38a27550 | -13.62535 | -48.10123 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28c3e152-ee46-3dd5-8ba2-e0a57a484bb3 | -13.61211 | -48.09901 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eae4954f-c055-3b4e-b4cc-fe5511258bc6 | -19.66165 | -45.97788 | 2025-09-28 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b35c4108-e110-3522-a6c1-337144ff0236 | -13.83325 | -47.96806 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a324838f-78e8-33b7-87b9-f68faf41e172 | -14.78261 | -45.63375 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b3e538-880a-3cc6-b34e-c939653d2769 | -15.46832 | -50.22901 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f13fc94-1d86-3307-a652-b462ccd96e52 | -19.95371 | -43.6667 | 2025-09-28 04:27:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 806ead2d-b8de-32f7-b92b-8715b6482a6d | -13.52428 | -47.40568 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f221c4a-e066-3d78-9962-f5673e3c8cc0 | -15.52728 | -47.90366 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 068b88b3-7b68-3fa6-8ded-1791567ca285 | -14.80472 | -45.6291 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27aac36d-7095-3113-87d0-70b3eda7e539 | -18.11013 | -42.18827 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b23f10f8-0217-34b4-be7d-fda85d1959a4 | -13.58507 | -47.29918 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e697a1c3-91e2-3122-86bb-4bf225345bf7 | -16.40417 | -43.72437 | 2025-09-28 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ebbced6-cce8-3ddf-a89f-93b6cea513fb | -14.78901 | -45.63876 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb4b2694-d0e5-3198-90f1-0d2ff3190a5f | -13.09591 | -48.88194 | 2025-09-28 04:27:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0102acc5-5ebb-38e5-b5da-527187339478 | -14.70798 | -45.20444 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28c94eb6-0be8-31f9-a0e0-fedc17d4fe7a | -13.6188 | -48.07827 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e98b28db-d5c4-3a92-a03e-81644c819117 | -15.4449 | -48.23418 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f53f5dc4-273c-3508-86a2-d16b57ecae27 | -14.58786 | -48.26389 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 179a198a-0c82-3652-9060-a7f2fc186950 | -15.19901 | -48.47897 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 530ab559-beab-3612-b4b9-f21b85d349cb | -15.01976 | -46.97048 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02c8c764-55c7-3de8-ba1a-11e73c8b320d | -14.53594 | -48.41939 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 239eaebb-15e9-3dd8-b370-37503563c6e2 | -14.58842 | -48.26034 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68b16f04-00ab-3efe-be7c-adf053bc20aa | -13.63665 | -46.83397 | 2025-09-28 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1321b01d-39d8-35fc-af6b-87cb5437699b | -13.6185 | -47.32275 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9915730e-6992-359b-b4e4-07e479f413b3 | -13.76385 | -47.86926 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ec4f91e-5d68-363f-aa21-17b1d86ff71c | -13.40167 | -48.16215 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c71b059-3d6f-3e78-9a86-6b089d92b059 | -17.19949 | -56.3534 | 2025-09-28 04:27:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e99e1589-b344-333c-bb6a-7f6852e15588 | -13.5895 | -47.29263 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9813a50e-b4ba-380c-895c-7c4f21c439fb | -15.22078 | -48.06233 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68165ef8-c088-3013-8a3a-aff793aadc3b | -14.58455 | -48.26333 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d61e1a7-0b07-34d4-af82-ee044d2502b5 | -12.9913 | -49.4381 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11a64bb6-3680-38fc-969e-d2cc893183fb | -15.95185 | -50.4226 | 2025-09-28 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f2021e3-edd4-3c9d-a828-67c23e0a942e | -13.58731 | -47.30674 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8eb1442-2aaf-33b1-8aac-a7ddfe9a8d36 | -15.89965 | -46.21284 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdc0c226-e938-3bdb-a64d-3bbe50cb2d6c | -13.79801 | -47.91122 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a474eb0-3c28-39da-93d6-118f251cb740 | -13.77103 | -47.86681 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 595b5346-f879-3e8b-8c9b-0266ec036a3c | -14.87994 | -47.98369 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad801c65-73c3-34f3-a50c-c4f1e341d223 | -20.41231 | -46.46881 | 2025-09-28 04:27:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68ed1f29-1756-3cc3-8a3c-747e70590f13 | -19.94415 | -41.64894 | 2025-09-28 04:27:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6926c3bf-1983-3df3-9227-10b96ca4334c | -19.85582 | -42.59324 | 2025-09-28 04:27:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |


[Clique aqui para ver as próximas entradas](README77.md)
