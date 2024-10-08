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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 914520da-fb9d-3d82-8f48-4eb43374e6cf | -16.9407 | -57.4859 | 2024-10-08 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.6 |
| b27d8a82-6e1d-38bc-a338-811cc99abfe1 | -16.9211 | -57.4881 | 2024-10-08 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 3c4b298d-30de-36ed-ae2e-1c4d44fab7b8 | -17.0992 | -57.3651 | 2024-10-08 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| c357ba9b-8bf4-3e84-b0b0-80800238ba13 | -17.1178 | -57.4244 | 2024-10-08 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 17104c41-db74-3a9c-8c37-8ec56702ef75 | -17.1375 | -57.4221 | 2024-10-08 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 00ec1925-3dcf-30f5-b310-8d36029ef61d | -18.4931 | -53.4457 | 2024-10-08 08:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b84ea774-d080-3478-9188-e0058266b3bc | -18.6192 | -57.2603 | 2024-10-08 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 8f28e6c2-9121-3f8c-9216-179ea9b48e26 | -20.3519 | -48.8417 | 2024-10-08 08:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5f574801-a905-3320-9d33-d06a6c77e8c9 | -20.3525 | -48.8186 | 2024-10-08 08:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f7228142-a4b0-30c9-a869-39e30a2f50d9 | -20.3724 | -48.8372 | 2024-10-08 08:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6ad365c3-0a77-38ad-9f71-461f8fe0bceb | -10.9113 | -64.1426 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 29617557-c471-39f5-8932-b669d1f2a7d8 | -10.9112 | -64.1615 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 185.4 |
| 7264214d-77ff-3be1-9120-d2498819bd07 | -10.9111 | -64.1805 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ae1fb33a-549b-3def-ac18-82d55d9bb86c | -10.8926 | -64.1434 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6ada1e3f-5116-3f76-b5bf-4273a9a490dd | -10.8925 | -64.1623 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 44ec57ad-3c8e-316f-9c57-2d1126a111c7 | -10.8924 | -64.1813 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 63a7bddb-a794-36bb-9fd9-71db74e936d4 | -10.8755 | -63.8979 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 4a2f43ab-aa8b-311f-879c-8c6ccc5d02b4 | -10.8754 | -63.9169 | 2024-10-08 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 179d1cdb-c01a-3b7f-bae8-73ecf6dabd7a | -16.673 | -57.1077 | 2024-10-08 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 69f13d2a-3ac9-3081-b194-7f53cf57d293 | -16.8048 | -57.4197 | 2024-10-08 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 97859b48-33e1-301b-b7b4-2f38a0235ef5 | -16.7852 | -57.422 | 2024-10-08 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| a41b14d8-2064-31c2-95c2-3cda41b91cc4 | -16.8045 | -57.4402 | 2024-10-08 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| bde20b2d-43b3-3eed-a1a0-f6f7b8818f77 | -16.9407 | -57.4859 | 2024-10-08 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| a4c9fd5d-b31d-37c7-b8f6-94a612aabda9 | -17.1178 | -57.4244 | 2024-10-08 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| ae6a49e3-4ad5-384f-aa67-4bec4c349d27 | -17.0989 | -57.3857 | 2024-10-08 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |
| 4709f9ac-0899-3887-a53e-bac587d293b4 | -17.0992 | -57.3651 | 2024-10-08 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| b04e707a-d7a8-3f76-a88e-6ab1b6ba022a | -18.4931 | -53.4457 | 2024-10-08 08:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 88588cc2-7c8a-3e3e-ac02-57d11c30b0b2 | -18.5993 | -57.2629 | 2024-10-08 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| acee356d-0696-3204-ba41-c5acdf4bc90a | -10.8754 | -63.9169 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 31ef959e-0514-3db5-8506-02d66023ec4a | -10.8924 | -64.1813 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d2e3b2ae-7584-319d-873e-1bd07dac35b7 | -10.8925 | -64.1623 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 163.3 |
| a11b7580-401a-384b-8673-ebe7528cde33 | -10.8926 | -64.1434 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7e45e4a5-50f6-3746-8dfb-a2a2e2db975c | -10.9111 | -64.1805 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| fa4a078d-3100-3d41-b13a-07d1a92c4e2f | -10.9112 | -64.1615 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 744e5c50-4a77-33dc-9bf7-7084fb820a26 | -10.9113 | -64.1426 | 2024-10-08 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 48d439d2-0668-3947-859a-acce0cc9a7d0 | -16.673 | -57.1077 | 2024-10-08 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 6c184e64-f192-3cc7-9147-655523cc86af | -16.8045 | -57.4402 | 2024-10-08 08:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 52d37a06-958f-3fd5-b634-6bad16e89f4d | -16.7852 | -57.422 | 2024-10-08 08:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.9 |
| c50cf1a2-b1b8-37ef-91fb-2c521e7ec899 | -16.8048 | -57.4197 | 2024-10-08 08:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| a9262cd6-cb03-3e34-ab88-7d9d76efce91 | -16.9407 | -57.4859 | 2024-10-08 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 0b298b60-ebda-3922-8552-150c7962a8d9 | -17.1178 | -57.4244 | 2024-10-08 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.8 |
| 1c3c91d1-f1bc-3e80-897b-bdc51ce03c00 | -17.0992 | -57.3651 | 2024-10-08 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 97dcf8a3-897f-3882-a98f-d63c41ed8c94 | -18.4931 | -53.4457 | 2024-10-08 08:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0671ca1d-dc36-3233-ac15-65bd1da1b7f6 | -10.8926 | -64.1434 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 231749f2-fb8e-3a7b-82c4-3c1325f92ed0 | -10.8925 | -64.1623 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 149aa486-e728-30e6-b888-9531b72e640b | -10.8924 | -64.1813 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| b2bde51a-7c52-3e50-9bd4-2f91e61f955c | -10.8755 | -63.8979 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| e756b72c-2b4c-3be4-9df0-983dabeb881c | -10.8754 | -63.9169 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 9d338fcc-6e5c-3ad1-9832-fe65405dc868 | -10.9113 | -64.1426 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 0a39b0ac-1381-39e3-96d6-900600db2890 | -10.9112 | -64.1615 | 2024-10-08 08:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 64501382-6501-3c56-bb8e-94436b61fed1 | -16.673 | -57.1077 | 2024-10-08 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| e544baa8-394e-30c5-917a-4e2b7c61cb3b | -16.8048 | -57.4197 | 2024-10-08 08:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 7adffc31-eb07-3b71-94ce-86e69d691de1 | -16.7852 | -57.422 | 2024-10-08 08:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| baf820d9-abaf-3043-b12f-370ff4bfb825 | -16.8045 | -57.4402 | 2024-10-08 08:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.9 |
| 8204c328-1b74-33dc-a314-2453390783ee | -16.9211 | -57.4881 | 2024-10-08 08:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| d500d1aa-2a57-3258-bdd0-f963038d30af | -16.9407 | -57.4859 | 2024-10-08 08:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 608ae23a-350a-33fa-b63f-e1be7e55e962 | -17.0992 | -57.3651 | 2024-10-08 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| df7f4448-78b8-3469-ac90-1cff12addac9 | -17.1178 | -57.4244 | 2024-10-08 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 9f806e11-f0d4-3501-a323-ba3c2d33c733 | -18.6192 | -57.2603 | 2024-10-08 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 426e3881-ab8b-3ed9-ac90-00a723fd3ec3 | -10.9112 | -64.1615 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 1f1150b3-f4d7-3715-a384-426e308f20d2 | -10.9113 | -64.1426 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 36d44c04-30e1-3909-991b-f96ec2d6040c | -10.8926 | -64.1434 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 70ca249f-0828-3c3d-88af-4535d5a7c018 | -10.8925 | -64.1623 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 150.2 |
| ca14d818-beaa-32f6-9880-836dc3060889 | -10.8924 | -64.1813 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6dab275d-8bfc-37f6-9dc8-81d26556fa5e | -10.8755 | -63.8979 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1bb5a36f-d866-31c4-9955-bd22f80e026b | -10.8754 | -63.9169 | 2024-10-08 08:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 12697991-7d4d-39a8-a6f7-efc0e30be219 | -10.8754 | -63.9169 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 601080ef-8786-39d7-a4d8-9e7043a88628 | -10.8755 | -63.8979 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fd64a683-336b-3307-be57-126ddc1eb736 | -10.8924 | -64.1813 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 666f28fc-4b04-36a0-a364-7343c8f7f149 | -10.8925 | -64.1623 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 160.2 |
| d097d59b-37db-3949-9680-da41f6c28799 | -10.8926 | -64.1434 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e95090a0-c893-302b-8f2b-bda0984dd39b | -10.8941 | -63.916 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 6517b3e7-4015-3cdf-a8de-f6075d6ce4ab | -10.9111 | -64.1805 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6c55cd93-afd0-3deb-81c9-6b53730288bf | -10.9112 | -64.1615 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 2697a4e6-eae9-3959-9718-aee038a27b7c | -10.9113 | -64.1426 | 2024-10-08 09:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 18e266c4-6cf1-3127-968a-e1ca6628862e | -20.3513 | -48.8648 | 2024-10-08 09:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 95c2387f-8a5e-3400-9651-159c40ec92b4 | -20.3519 | -48.8417 | 2024-10-08 09:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 037d9b7a-06f0-37e2-84f3-35404cbec3a8 | -10.9112 | -64.1615 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 217.5 |
| 42fed4fb-10d0-3dce-b2ab-da04b7f9b3b4 | -10.9113 | -64.1426 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f081f975-dd29-3cfa-818b-09633bd8a46c | -10.9111 | -64.1805 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| dec78411-ee54-3ce5-a73a-f3afb17ea40f | -10.8926 | -64.1434 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 65e8fc75-fef6-3b9e-9531-87e3b661ad55 | -10.8925 | -64.1623 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 8428c7ce-9385-3919-9b2b-f9d12493ae65 | -10.8924 | -64.1813 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 946c97e7-1014-374c-94bf-44918821d612 | -10.8755 | -63.8979 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e367ddb5-f439-31d8-8539-67480c687414 | -10.8754 | -63.9169 | 2024-10-08 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f0066b7d-a6af-3745-95fb-50d490957bdb | -16.8048 | -57.4197 | 2024-10-08 09:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 567da963-fbc8-368c-9d89-ab9c230c8d11 | -16.571 | -46.4553 | 2024-10-08 09:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8eb1264f-f3a1-36bf-9b71-1dcb30109538 | -16.8048 | -57.4197 | 2024-10-08 09:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 427e9ebf-bc91-346f-a058-e8fae052f317 | -16.571 | -46.4553 | 2024-10-08 09:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 112.9 |
| feeef8ed-17e4-3f09-a550-afaaa25bd5b3 | -16.6726 | -57.1283 | 2024-10-08 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| fb88f998-7d31-3e2a-860d-3eac32be3c6a | -16.673 | -57.1077 | 2024-10-08 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |
| 49472ff2-38a0-3004-8af3-db02c398ad28 | -16.8048 | -57.4197 | 2024-10-08 09:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 2d828a7d-cc33-33c8-8bc5-a079432a8b6e | -16.5715 | -46.4321 | 2024-10-08 10:06:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 67e92088-736e-3f01-81e6-c99c70804e07 | -16.571 | -46.4553 | 2024-10-08 10:06:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 157a6e59-bded-3e6f-8f61-0b3aa3f76167 | -16.673 | -57.1077 | 2024-10-08 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 85598dc0-551e-3eb2-9c30-d67434a123de | -16.6726 | -57.1283 | 2024-10-08 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| f9356e57-db36-30b5-a7e1-8f3252bb989c | -16.8048 | -57.4197 | 2024-10-08 10:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 82bd95fa-bef6-3cab-b65d-df2b0da05cb5 | -16.571 | -46.4553 | 2024-10-08 10:16:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| b26d307d-7351-3ac1-a0de-a63b6d096655 | -16.6531 | -57.1305 | 2024-10-08 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| e6b04caa-88ab-34de-84e3-06a3eac073e7 | -16.6726 | -57.1283 | 2024-10-08 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |


[Clique aqui para ver as próximas entradas](README135.md)
