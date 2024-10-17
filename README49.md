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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9af5ce3-40a1-3332-bd7a-c8c3fe13b1a2 | -17.74176 | -57.12539 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 42239faf-117d-31e7-9cac-d58c11d6dc78 | -17.22847 | -57.31144 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b70b687c-a706-3b64-bde9-5159c3f7b42a | -17.22791 | -57.31509 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ce44ed23-3dfa-34d2-b847-57913dea5939 | -17.22569 | -57.30723 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9f461f2b-a61a-34f2-b2eb-3c25b912ad80 | -17.22514 | -57.31089 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c81b0a27-f296-3821-b570-2f1d9aa1b9a9 | -17.22458 | -57.31455 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1399fec7-11c6-33e1-bbf3-2f817a5f4700 | -17.22402 | -57.31821 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 12283e29-93de-3ba7-9378-db36eb22448d | -17.22236 | -57.30668 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| abb81962-ed8c-302b-8674-3691eede064d | -19.47154 | -57.55008 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 49c359ba-3874-3f86-8627-0b79998ac2f2 | -19.01156 | -57.3982 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 63820db2-fc3c-3520-bbc4-269e4d6a973b | -18.67996 | -57.34464 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9d1c401d-81ac-3851-baaf-28243085ab31 | -18.6794 | -57.34838 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6c22c788-b559-3422-ae18-e3d3781cfc37 | -18.67661 | -57.34409 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8b3f353c-e961-3154-9e29-8021633f75ed | -18.66486 | -57.33065 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ac04cdc0-443e-359e-8b6c-688fb3b97202 | -18.6615 | -57.33009 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d6b86b6c-c6af-361c-ae09-769748a3c74d | -23.36691 | -47.3698 | 2024-10-17 05:10:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a15f79c5-e5dd-3b1a-8d58-cc4e2e577fff | -23.19745 | -50.67414 | 2024-10-17 05:10:00 | NOAA-21 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb4816e4-9664-3fd9-8198-880c6caea8d5 | -23.03976 | -52.45717 | 2024-10-17 05:10:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c2675313-5076-313d-b558-fc5b70e76dbb | -21.36018 | -55.89895 | 2024-10-17 05:10:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27a9f001-d645-3de6-980c-6cff274b1f0d | -2.9674 | -47.9931 | 2024-10-17 05:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6f3a81d9-b771-3fdc-9253-f27d505cbb8f | -3.5086 | -51.1122 | 2024-10-17 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 59399bfb-ee8d-35aa-8b62-777c663b7859 | -3.5087 | -51.0914 | 2024-10-17 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 049fd402-6e26-3556-b238-11d9195fd3d5 | -2.42289 | -48.51014 | 2024-10-17 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c12e7f0-01c6-3870-ae64-3dd405ae7e76 | -2.422 | -48.516 | 2024-10-17 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c18f8e-e816-35f1-89e6-556164c8114e | 1.00941 | -52.21775 | 2024-10-17 05:25:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5821c827-6394-3fbe-b873-48ef289cf2dc | 1.00852 | -52.21736 | 2024-10-17 05:25:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0aa80383-b51c-327f-a07e-18857801811d | -1.71273 | -52.70042 | 2024-10-17 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d1c6b8-1ce7-3a5a-8027-3b2b8c425dfd | -1.70899 | -52.69088 | 2024-10-17 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e02975dc-b6b6-3f75-9932-49da04cb4fcd | -1.7048 | -52.68425 | 2024-10-17 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f898ecd-0e38-3b74-82fe-d530f5a15790 | -1.70437 | -52.68717 | 2024-10-17 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50c986fb-4eda-356d-a247-fcc9542646a4 | -1.7013 | -52.68647 | 2024-10-17 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f241f64-1bc3-3ca8-a4f5-c5ed6996ae03 | -1.14039 | -54.16874 | 2024-10-17 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b897f53b-f023-3deb-a985-a08b459b6022 | -1.13968 | -54.17324 | 2024-10-17 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a7f069e-ab83-3e95-99b3-7721c22af27c | -1.13588 | -54.16796 | 2024-10-17 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 450daede-18f1-3bc9-a14e-71c4ebcb5b6b | -1.12008 | -53.70906 | 2024-10-17 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f96733ec-5646-3ee8-b623-5d0d37f42562 | -1.11716 | -53.7099 | 2024-10-17 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f8ceb75-2f2a-3871-b81f-1508bbec8c53 | -1.11541 | -53.70831 | 2024-10-17 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d729d716-acea-3a55-88cc-ecadd1cd74e8 | -1.28618 | -55.51989 | 2024-10-17 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 015062bc-67a2-371d-bb30-83e833563229 | -1.28204 | -55.51923 | 2024-10-17 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24bd87d2-3de3-3571-b2bf-dff8ca9d43f8 | 1.30581 | -60.41382 | 2024-10-17 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec389516-c0eb-35fd-a771-bcc1e43695b2 | 1.30249 | -60.41434 | 2024-10-17 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2911db2c-3df7-3f48-a2c1-408fe160440b | 1.29802 | -60.42913 | 2024-10-17 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e3a8bd1-2990-34fd-bd0c-4e080f508aa7 | 1.29748 | -60.4257 | 2024-10-17 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b040ff0e-6756-36d9-a7b1-2797fd37ce30 | 0.97261 | -60.40246 | 2024-10-17 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd2a9f20-2fab-3ba5-b91c-b105a74032ae | 2.60417 | -61.31387 | 2024-10-17 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd74b38e-2c87-3187-9abe-77d7c8bf107f | 2.60079 | -61.31439 | 2024-10-17 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828daccc-6cb3-3c8a-969a-c9cd9db84291 | 1.94484 | -60.85948 | 2024-10-17 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f9528e2-bba1-3563-8380-6a9106b20e1a | 1.94151 | -60.85999 | 2024-10-17 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8382d6c-b644-33a4-adea-650c54b4e49d | -3.22034 | -48.92012 | 2024-10-17 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa7c0579-f7fb-38bd-988b-9ddaa7b7c7ee | -3.2195 | -48.92569 | 2024-10-17 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cf4128a-de76-3c80-9562-1e2e71f170f6 | -3.21375 | -48.91902 | 2024-10-17 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07697db9-5776-3cc2-98bb-1d99b2bde70c | -3.46864 | -47.66888 | 2024-10-17 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8af6b481-9a82-3846-8321-8f0264a85904 | -3.46152 | -47.66772 | 2024-10-17 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56023986-47fa-3bcb-9c0a-b775b459531f | -2.97419 | -47.98458 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20b17c69-b4f5-3181-a784-6acf06c05787 | -2.97331 | -47.98445 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 48118b7f-d1e4-32a8-9544-7b6a46c5b29e | -2.97238 | -47.99082 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 14d4a8da-61c2-3ea6-9f3d-9bb4cb50a3f7 | -2.97145 | -47.99721 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 69ea4b08-b9e1-35f7-b750-c1f0431c5d9e | -2.96626 | -47.98991 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6ebe1e9-00dc-32f2-91c2-a5e1213c566e | -2.9653 | -47.99627 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e48aa8d-31d6-383e-b54e-ce2d83c7c9b6 | -2.9645 | -47.99612 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3d07701e-0f9d-30e3-84b3-f8a03048b7d9 | -2.96352 | -48.00282 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4330b1c0-15e9-3897-a8b2-2c05135068d0 | -2.97322 | -47.99093 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3a96eb07-14a9-3165-8762-1e9f8bd044d1 | -2.97224 | -47.99735 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 063ba8a1-c174-3838-9d49-11c770f48e9f | -2.97122 | -48.00402 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 98159e0d-d379-3f18-8006-76c7cf641f63 | -2.97047 | -48.00394 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 15029a13-771c-3503-8d7e-d2d36a958f97 | -2.96722 | -47.98362 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c852ee3b-748b-3d8e-9bcd-995b0903a09c | -2.96542 | -47.9898 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 579f6e27-ff32-304d-9c6e-13e6831a924f | -2.96428 | -48.00293 | 2024-10-17 05:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7847c303-cb4b-3fcc-9227-e15d9ebc8eb8 | -2.60993 | -48.25561 | 2024-10-17 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 838905d4-175e-37f9-9075-4a4770c9aeca | -2.60929 | -48.25618 | 2024-10-17 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e1ecf039-8f99-3ff6-abff-ae6856098440 | -2.60313 | -48.25446 | 2024-10-17 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8e024b4-f28c-3a33-9690-b87af8613907 | -2.60249 | -48.25505 | 2024-10-17 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b68930fc-d863-3645-8571-5dfee5c4e0f4 | -2.60219 | -48.26088 | 2024-10-17 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73ce2a1f-16da-3c67-bd89-96c6ece483f9 | -2.6015 | -48.26147 | 2024-10-17 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04ebf91d-c5e1-3d9e-ab55-9249de6410f1 | -3.92535 | -48.34303 | 2024-10-17 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 405134bf-1216-3efc-82ee-1cad3664f05c | -3.92507 | -48.34339 | 2024-10-17 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7a3694d-ad41-39e9-8d73-0977c3702f68 | -3.9245 | -48.34916 | 2024-10-17 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3bc5222f-1ead-3c42-8d9e-e71f8c10534a | -3.92418 | -48.34951 | 2024-10-17 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06f1a82d-1b79-370a-940b-d0a44a51a292 | -3.28938 | -49.07812 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8ffd856-c244-3bd0-bf4b-f0e321077120 | -3.28739 | -49.07841 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa9721b9-181a-38ee-98d2-73649645b311 | -3.2828 | -49.07733 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9421f013-f868-3ede-a881-b528ebb44421 | -3.51013 | -50.32134 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10e12e9b-883d-3f01-8b5c-3b7b0906b622 | -3.50946 | -50.32589 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e051a93-ae4b-3a3f-8d5c-9650d075647f | -3.43403 | -50.15653 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31fc9d17-783b-3828-88be-ccffc208687b | -3.43333 | -50.16124 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85bcf213-d42d-325a-8254-5f6352eea7b6 | -3.40551 | -50.39109 | 2024-10-17 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 772fab9e-9c40-3288-ad93-962029b257f1 | -2.84297 | -49.14583 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86afa2e2-66f6-3a83-99d7-cc910900f221 | -2.84219 | -49.15102 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd47c54e-22b7-3b3d-9e0b-7530c860a97a | -2.83648 | -49.14487 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5543bc7-5349-3386-8210-bd5f2b17e441 | -2.8357 | -49.1501 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2801da4b-8699-3884-b6c7-c81df0e4fb3e | -2.83366 | -49.52325 | 2024-10-17 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be510719-c75d-3cd3-bf30-d3e5f9f0710e | -2.83199 | -49.52191 | 2024-10-17 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc5ffce2-909e-3220-b8bd-ff7ecf110757 | -2.82735 | -49.52215 | 2024-10-17 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb6054b4-92c6-371d-a72c-b2e16eff322e | -2.81397 | -49.52516 | 2024-10-17 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5eefb836-6138-39d0-b8ed-19ed3f8c6b96 | -2.81225 | -49.52395 | 2024-10-17 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c0655a9-1b6b-308a-8a43-2c004db34130 | -2.63993 | -49.26552 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e70d3561-ebee-3f08-9da9-b60f7c521480 | -2.63972 | -49.26434 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bc9442f-fd93-30d9-9d10-ab68c609e720 | -2.63917 | -49.27078 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44ffa8de-d969-3d7e-b8f9-9657f8f1b06d | -2.63892 | -49.26958 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8c11d86-261c-363d-99a5-0f3fea003045 | -2.63351 | -49.26454 | 2024-10-17 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README50.md)
