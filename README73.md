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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23d6eee9-0af7-39f5-8613-8a69a0775188 | -2.7428 | -54.1347 | 2024-11-06 13:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 99344c9e-b4ce-3571-828c-92d475955cff | -1.802 | -47.937 | 2024-11-06 13:30:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 347.1 |
| 64063c31-622b-3b15-9190-855d74024ea0 | -1.2922 | -54.5784 | 2024-11-06 13:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 779c104e-909a-3015-8e67-afe8bb3c362e | -2.7243 | -54.1552 | 2024-11-06 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| af6caee6-f9c4-3dd2-9468-2a40de32c735 | -2.764 | -53.2062 | 2024-11-06 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 91c8f56d-a16d-37d3-b0d6-f8e20c1384c2 | -8.0909 | -44.4461 | 2024-11-06 13:40:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5ecccbad-bef2-3b36-bbdf-a1c0e6c04e2a | -8.3091 | -43.6112 | 2024-11-06 13:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a971027d-7391-38cb-bfd1-7fe09f8eb14d | -2.6764 | -51.8189 | 2024-11-06 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 9b2346cc-3fa0-34a6-b5d7-1a2adcd97061 | -3.0023 | -53.4232 | 2024-11-06 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5d4c7bf5-9558-3d9b-b250-71954335ab69 | -7.2241 | -42.8797 | 2024-11-06 13:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| f001afa4-2cac-3936-9d70-ca4403c9e0c6 | -8.1101 | -44.4211 | 2024-11-06 13:40:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 79045712-c565-35e0-8b32-14e387c3f1ef | -2.9186 | -51.047 | 2024-11-06 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 05cbea23-d218-358e-9993-56538fb84669 | -1.802 | -47.937 | 2024-11-06 13:40:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 736.8 |
| 9db7e68a-e510-3867-a2de-fc45ffdfebeb | -1.2922 | -54.5585 | 2024-11-06 13:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 334.9 |
| 0d365a79-ee87-360d-b733-10f1ed996031 | -2.7456 | -53.2269 | 2024-11-06 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 2d9aefe7-ce6c-3fcd-9073-8953ef05816d | -1.2922 | -54.5784 | 2024-11-06 13:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 0cb695a4-b775-3384-ae74-76aa44af08d0 | -7.2053 | -42.8815 | 2024-11-06 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 0cf5e6ef-6aff-3f35-b40e-2e5f96f8ccae | -2.6764 | -51.8395 | 2024-11-06 13:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 2b6879db-309c-3ad6-90f4-33a1d0e6bcd1 | -2.7428 | -54.1347 | 2024-11-06 13:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 3e067174-9afc-3fba-a7ed-b66cb4789a16 | -3.1433 | -50.2044 | 2024-11-06 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 52332940-ccf8-346d-839f-58ece15d857b | -3.0207 | -53.4227 | 2024-11-06 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| bf4b0b4e-06e2-301b-a150-b9693b9aa634 | -1.7835 | -47.9373 | 2024-11-06 13:40:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| e63715b2-b7ba-3bfc-ba2a-fbf3b4f196f4 | -2.8321 | -49.4749 | 2024-11-06 13:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 9ecddd3c-6fc2-36cc-8ec6-6a3a7e29a240 | -3.0397 | -53.2603 | 2024-11-06 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 4870437f-5f98-337d-b23b-d65b889f83b4 | -8.3281 | -43.6091 | 2024-11-06 13:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| c6f73565-c326-3f41-9554-a14f9621aab0 | -1.3876 | -52.1918 | 2024-11-06 13:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c7f4b815-d86c-3473-a7dd-a861609d5fe1 | -3.0207 | -53.4227 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 6beae305-4625-3a14-959b-f289fc713077 | -8.1101 | -44.4211 | 2024-11-06 13:50:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a713ee19-cbc5-30e4-ac76-c703c256adb8 | -2.8202 | -52.9002 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 1c5eb7d6-328f-3e1f-b776-8722a59d3ff6 | -2.7456 | -53.2067 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f98833cc-f736-3e3e-ab0d-9ab1ba35b177 | -2.7243 | -54.1552 | 2024-11-06 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| e7724688-ef09-3135-ac75-dc9b056edcbe | -2.764 | -53.2062 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| e094d890-bffb-35c7-b1af-8f216d3068ee | -1.2922 | -54.5585 | 2024-11-06 13:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 351.3 |
| 7ae2f14d-b618-39e7-86d4-d2c1c709baa2 | -3.0023 | -53.4434 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 9a4f8a0e-4770-3a3b-a82e-02d429bb78d6 | -8.0909 | -44.4461 | 2024-11-06 13:50:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 641066c3-7e65-3103-87ff-655d82bebfa7 | -3.0023 | -53.4232 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d3bd6353-5255-30df-866b-aac21a8d9ac6 | -3.0397 | -53.2603 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 67061ee9-e55d-36bd-9c1f-cb3c526615bc | -3.1433 | -50.2044 | 2024-11-06 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 65d62778-9987-3e6f-97d3-b9b23c1e0b34 | -2.8321 | -49.4749 | 2024-11-06 13:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 870ba457-e616-3ea8-910b-1d472cb234b9 | -2.8386 | -52.8794 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d1ce5984-b421-3651-aadc-432466a4163e | -7.2241 | -42.8797 | 2024-11-06 13:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| ba5d6916-af57-3c00-8047-e7cae3477d3c | -2.82 | -52.9613 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 1d8a02d1-1d9e-3c03-96ba-e2b196aa9f7f | -2.9186 | -51.047 | 2024-11-06 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| b7a855b1-a39c-32d2-ade7-3d16d4bc45a5 | -2.6764 | -51.8189 | 2024-11-06 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 86282fdb-934f-3459-a4e6-d9cceb7d9bf9 | -2.8016 | -52.9414 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 980a61dd-05e3-385d-9aad-d915bb0a50ea | -2.7428 | -54.1347 | 2024-11-06 13:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 4f761a57-3f45-3fba-98c9-b1d4f572911e | -2.8385 | -52.9201 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 2a671c0c-a939-3e95-8d85-932bf46f2212 | -2.7456 | -53.2269 | 2024-11-06 13:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 12dfe6d3-c8b8-3363-bf95-0a586b4a1d2d | -7.2053 | -42.8815 | 2024-11-06 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 7c725941-d2ec-3245-81e3-f826ce4fa5bd | -8.1101 | -44.4211 | 2024-11-06 14:00:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ce1640c1-a69b-39dd-b50e-11483095fa46 | -3.4565 | -50.3622 | 2024-11-06 14:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| aab97a83-fd4a-3583-90a6-bbd688336000 | -6.9424 | -42.8126 | 2024-11-06 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 7ef6fdf8-b20c-3b96-aaee-55881ea00e0f | -2.8386 | -52.8794 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7aed7733-bfea-3c7d-860d-a326107512ad | -4.2578 | -49.1678 | 2024-11-06 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b6525ccd-1260-3d82-9577-22821a6927f2 | -2.8054 | -51.7951 | 2024-11-06 14:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 307d68cd-ce29-3332-b4cf-dba158959c91 | -3.0207 | -53.4227 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 76dcc060-a2d9-38df-a9d3-cdff3c032209 | -2.764 | -53.2062 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 28cdc563-50e5-3634-8813-97bd923fe9de | -2.7428 | -54.1347 | 2024-11-06 14:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| ae7c7c90-a79b-3c7e-a710-87d619679da7 | -2.8202 | -52.9002 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 190.6 |
| b99f1af0-05f9-3881-ad44-225ace2f30de | -2.7456 | -53.2269 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| ec471b71-d9e6-364b-937d-42dc3d3239d1 | -2.82 | -52.9613 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 9cb6b14d-6971-3208-8bf4-5fb83784a039 | -8.2745 | -44.8403 | 2024-11-06 14:00:00 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5cfa5dbd-12c9-35c5-8dd7-0d40c958ee47 | -1.8021 | -47.9153 | 2024-11-06 14:00:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 539.0 |
| 19f9a974-a6d7-3e33-9dfa-2bf7fdd833cf | -8.5002 | -42.0747 | 2024-11-06 14:00:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| bd1f06f0-4db6-38df-8aed-f2d8fd5d6b7a | -2.9186 | -51.047 | 2024-11-06 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f24c1964-26ed-33fd-8e07-450631bacbc8 | -7.775 | -44.0859 | 2024-11-06 14:00:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7beaf2da-c873-3a29-961e-fada2d33fe29 | -2.8016 | -52.9414 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 306f8224-b215-3596-a48b-cd4896e5949b | -2.7243 | -54.1552 | 2024-11-06 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 446c8fbf-7a09-3de8-8736-67870bc195c5 | -3.0023 | -53.4434 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d05e5b75-ed23-3376-85ce-4aede26db5bb | -3.0023 | -53.4232 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 1063bbc8-50e4-31e0-9bfa-a67a1a85fdbf | -2.8608 | -51.7731 | 2024-11-06 14:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 07d5ba51-90f7-3140-bfa6-9caa3f73daec | -2.8385 | -52.9201 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 174.4 |
| 89774c54-5a67-3a47-8bfb-5f3adc6d348c | -1.535 | -52.0053 | 2024-11-06 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a9896cc4-0473-3c69-900b-40bd7a315eb3 | -7.2241 | -42.8797 | 2024-11-06 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 3b95a441-53d4-3ed1-ab64-5a8ba9f1026d | -3.0207 | -53.443 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 8ef82294-3d6e-3db3-9e26-579f801a8f30 | -2.7456 | -53.2067 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| afc02cb9-2ae0-34da-8935-b343e2d2dcf1 | -2.8017 | -52.921 | 2024-11-06 14:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5a9de07f-49c4-3e11-b3ac-6825a27a20a1 | -7.0856 | -41.8231 | 2024-11-06 14:00:00 | GOES-16 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| a15716c8-1d5e-3f60-8ffa-605ec6eb37bd | -7.2053 | -42.8815 | 2024-11-06 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 6879407a-5212-33ec-8170-f212ae604bf9 | -2.6764 | -51.8189 | 2024-11-06 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| e30338e4-842b-3895-845c-a57dedd4c2bc | -1.2922 | -54.5585 | 2024-11-06 14:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 338.0 |
| 8f1745df-e117-3989-8bf1-3b5e17830986 | -2.81 | -52.94 | 2024-11-06 14:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8214cade-7156-3ba5-9bbc-d93b0039f54a | -2.84 | -52.88 | 2024-11-06 14:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8905e44c-daa9-397a-b9f7-94f758193ab8 | -3.8 | -42.34 | 2024-11-06 14:00:00 | MSG-03 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c3daae7-042e-3673-bdb2-e82d31dc0321 | -3.8 | -42.38 | 2024-11-06 14:00:00 | MSG-03 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a950366a-235e-317f-bc80-8068ebd43b9d | -2.81 | -52.88 | 2024-11-06 14:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc00697-5317-38b9-b675-dc20836d66d2 | -6.48 | -44.68 | 2024-11-06 14:00:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a46757a1-022a-38a4-aada-544a6b0d295a | -2.8016 | -52.9414 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 38b95545-41a9-3a80-bf53-43bf4c3bc561 | -1.3876 | -52.1918 | 2024-11-06 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| be4d3986-22df-3e20-b5f4-87056f2c0b39 | -7.775 | -44.0859 | 2024-11-06 14:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f0b39ccc-6aca-3280-ab79-eb1fd96ad8e5 | -6.9424 | -42.8126 | 2024-11-06 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 2433834f-8ea0-3787-8ad2-09e9e293e0da | -1.8021 | -47.9153 | 2024-11-06 14:10:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 366.9 |
| 51894fdb-677d-389e-8633-9793e00d4357 | -2.8608 | -51.7731 | 2024-11-06 14:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 51e3dc94-a42a-3e2d-8dce-267311e3b90e | -8.1756 | -43.719 | 2024-11-06 14:10:00 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 820350a2-af71-3ee4-afb4-7b9fc033a4c9 | -8.1101 | -44.4211 | 2024-11-06 14:10:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 028b9d1d-1c63-357b-a7b7-1e83915f5bed | -2.7428 | -54.1347 | 2024-11-06 14:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0e5a10ba-f1cd-341e-b495-40a57116d867 | -4.2578 | -49.1678 | 2024-11-06 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| adb90fac-9d32-35d1-aa86-7c56d9407c60 | -8.0909 | -44.4461 | 2024-11-06 14:10:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| ed2a5a14-f61b-384e-8365-006ee82925bd | -3.0023 | -53.4434 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 8fcf58cf-db55-3001-8622-7699fb1412dc | -3.0207 | -53.4227 | 2024-11-06 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |


[Clique aqui para ver as próximas entradas](README74.md)
