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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 438c47e3-2946-3334-83ba-835aeec50c82 | -9.74026 | -46.28701 | 2024-11-06 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 100c47a9-99ec-3413-abde-c7b6d13e26cb | -11.92157 | -42.66422 | 2024-11-06 12:42:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| aeb662ff-41b3-3f86-87f2-1f3311141216 | -11.33547 | -49.01228 | 2024-11-06 12:42:00 | TERRA_M-T | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| de7138de-d330-31ad-9b79-49041021447a | -10.59564 | -48.77375 | 2024-11-06 12:42:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 81cff790-e900-312b-a7ec-f5fd72f59866 | -9.7492 | -46.28827 | 2024-11-06 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0096ff1a-ec1f-36ed-97fe-8400b694f98e | -10.3774 | -45.08152 | 2024-11-06 12:42:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b6c80e8d-89bb-367d-a071-eae5a79298a8 | -10.22091 | -44.88011 | 2024-11-06 12:42:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dd41ee06-fdc0-3452-97f2-0fb1c348a1a1 | -12.12092 | -49.31453 | 2024-11-06 12:42:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 69c9471b-fe01-3b10-b2bd-33cdf285a1a0 | -10.48878 | -47.37256 | 2024-11-06 12:42:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b193f96c-3303-32df-b02e-c67f21da1de8 | -12.01379 | -42.83949 | 2024-11-06 12:42:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 731d68af-c91b-30fb-8329-ec710fa7abf4 | -12.01197 | -42.8544 | 2024-11-06 12:42:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 92d10bbc-c861-3b0e-8084-4f9c7edbf926 | -9.56425 | -45.17919 | 2024-11-06 12:42:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 915eb308-191e-3c94-8e69-90f4763180d0 | -10.48748 | -47.3815 | 2024-11-06 12:42:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fd4e9a2b-5b9f-35d7-9989-d3cc84e34941 | -10.77383 | -39.51741 | 2024-11-06 12:42:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 06be0b7f-2896-3a4d-b04e-443deab125e8 | -10.9312 | -48.9362 | 2024-11-06 12:42:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9866b44c-8638-3d9e-95dd-81c805198251 | -10.61161 | -44.92615 | 2024-11-06 12:42:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 440e5397-cb19-3cba-b2e8-8c5e54ec7287 | -12.26928 | -44.98204 | 2024-11-06 12:42:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e70b4d66-ffe9-3a09-95e8-6cc37c139a4b | -9.82189 | -45.2441 | 2024-11-06 12:42:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 00101410-5021-32f6-8c2c-9c3135b33f4b | -9.75049 | -46.27914 | 2024-11-06 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a0816fbe-d8c7-3604-a457-b9473985fba4 | -12.26743 | -49.56882 | 2024-11-06 12:42:00 | TERRA_M-T | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 8b179a25-cf99-3c7a-a89a-54bf8664ed8f | -9.8233 | -45.23398 | 2024-11-06 12:42:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 38787dfa-611a-3c16-acaa-9bda4c2d3178 | -11.58524 | -42.78853 | 2024-11-06 12:42:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| c859f3a1-f1c3-3471-9c66-a7b70566ea83 | -10.90622 | -45.98667 | 2024-11-06 12:42:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d69e3315-125b-3c3f-a3b5-564d48603e22 | -12.26891 | -49.55898 | 2024-11-06 12:42:00 | TERRA_M-T | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a61b258d-ec94-3e61-a776-cbcbdaebb098 | -10.48301 | -44.59388 | 2024-11-06 12:42:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 79287299-a18a-3ecd-bb2f-a82c924614ea | -10.75704 | -49.05381 | 2024-11-06 12:42:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 572c6a26-c7c2-3ebe-aceb-927acbd513bb | -11.893 | -42.88741 | 2024-11-06 12:42:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 94efd329-4fec-374a-98f0-d7196627adbc | -2.4458 | -49.0176 | 2024-11-06 12:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 207.3 |
| ee268ba5-f1de-34ef-98b0-2bf846350d14 | -2.8385 | -52.9201 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.7 |
| a6fa502f-c6b0-3405-b1ee-86e9c6c129c3 | -4.1246 | -43.5833 | 2024-11-06 12:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 86436f0e-9556-37e8-aa18-53e3fb44fa01 | -1.2922 | -54.5585 | 2024-11-06 12:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 4443ea1f-cba4-3c1d-88c0-d947a29e5ef0 | -3.0207 | -53.443 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 5e8098c6-27f2-34b7-a1b8-5dbd71b7ca01 | -3.0397 | -53.2603 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ddbff2ae-54b0-3b34-8f5b-9e766108e413 | -2.6764 | -51.8395 | 2024-11-06 12:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 0215562f-2e8d-3b6c-bd64-fc519b6223c7 | -2.8202 | -52.9002 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 290b02b1-0c3c-34a2-97cd-a5ab7f5480db | -2.8386 | -52.8998 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 318.0 |
| 3c5e8df3-dd75-325c-93ab-0bada9d0350b | -3.0207 | -53.4227 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 78dfc810-3a96-3d49-ade6-3f103343d302 | -2.6764 | -51.8189 | 2024-11-06 12:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 548216e5-d94b-3a50-99ea-021c0a8da05d | -2.82 | -52.9409 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| eafc7167-856c-33b1-b5de-8a27e0e91905 | -2.4457 | -49.039 | 2024-11-06 12:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 235.0 |
| 57b122ca-0c73-390d-b4a4-d88f2c32366c | -2.7243 | -54.1552 | 2024-11-06 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| bfb46d70-beb5-3d22-b7a0-f81da738d4dc | -2.8201 | -52.9206 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| c0ccbdbc-8fbb-3158-83cf-d80fc79ba65d | -2.9186 | -51.047 | 2024-11-06 12:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 508c2dc3-dbd4-3549-8c67-f68b1bf167cc | -2.7428 | -54.1347 | 2024-11-06 12:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1e9eb6d4-fcc3-3c15-a56a-4e8687a6f544 | -2.7639 | -53.2265 | 2024-11-06 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 5f647ea0-88a3-3514-b79b-17338b0270be | -2.4458 | -49.0176 | 2024-11-06 13:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| bb894565-ec94-3e98-b5bd-054ab4a7c2aa | -3.0207 | -53.443 | 2024-11-06 13:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| dc21d6d4-eb8a-31c5-b2d0-44e79c78f63c | -2.7243 | -54.1552 | 2024-11-06 13:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 8b4ed15b-74b4-3cb5-88f1-c73f393c3a21 | -3.0397 | -53.2603 | 2024-11-06 13:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 6c02b151-2a1d-3d10-89d6-136b0fd960f6 | -1.2922 | -54.5585 | 2024-11-06 13:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| d181e9aa-b7c7-3bdc-ad8e-db4e80b79b6f | -2.4457 | -49.039 | 2024-11-06 13:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 212.9 |
| 9cc88213-ed04-3405-9540-b0e55d43f5fc | -2.6764 | -51.8189 | 2024-11-06 13:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 6084502d-45ad-3f38-8f75-290707364b1e | -2.7639 | -53.2265 | 2024-11-06 13:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 92e3e8f6-0d57-3d5f-ad3d-6533d9b09ec2 | -2.6764 | -51.8395 | 2024-11-06 13:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| fe48d3f1-f084-3fb7-b764-d1a2a3a9b6be | -3.0207 | -53.4227 | 2024-11-06 13:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e551342e-36da-3bfb-ad51-dc9c24e6a5a8 | -6.6163 | -41.6528 | 2024-11-06 13:00:00 | GOES-16 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 7f97be73-a25e-368e-83aa-5bd0a84f086d | -2.81 | -52.88 | 2024-11-06 13:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa1d30f7-2b5a-3c45-9602-62e9f5d4cade | -2.84 | -52.88 | 2024-11-06 13:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e393c3-aa9d-3f53-a97e-4cc92bd52f47 | -2.84 | -52.94 | 2024-11-06 13:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8c65f4-6a65-302b-8cd3-8c006c04ddb4 | -2.6764 | -51.8395 | 2024-11-06 13:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| ec606c1d-fa75-3529-ba43-d5ba44cba6fa | -1.4244 | -52.1913 | 2024-11-06 13:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 6e64eb33-c903-3d77-8d38-282cc3e5ad6b | -2.6764 | -51.8189 | 2024-11-06 13:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 59e1db54-f948-30e9-b221-d20a3ac345b4 | -3.0397 | -53.2603 | 2024-11-06 13:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d469bcbb-6d92-325c-9d6d-c8967ecad6d6 | -2.9186 | -51.047 | 2024-11-06 13:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 2d454b86-2acb-3e6f-bf5d-ba5c91e29ddf | -3.0207 | -53.4227 | 2024-11-06 13:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c2185ea5-0d97-3cc1-9cc0-dac39c621154 | -1.2922 | -54.5585 | 2024-11-06 13:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| c94563ce-33a7-3edd-8dc5-07a3207503a9 | -4.1246 | -43.5833 | 2024-11-06 13:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 77818147-ae9b-370c-8069-4e00c8584229 | -2.7639 | -53.2265 | 2024-11-06 13:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 878896fe-c6f5-3791-a103-ab80ed1fd45f | -2.4458 | -49.0176 | 2024-11-06 13:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 2dd23039-6928-3e54-872b-bdbe2a3c18a9 | -2.4457 | -49.039 | 2024-11-06 13:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| acd11105-38a0-3622-91dc-b9a5d4d1bcdf | -7.2241 | -42.8797 | 2024-11-06 13:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 022fe13b-f181-3fff-937a-1cc7d446497e | -3.0207 | -53.443 | 2024-11-06 13:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 5b99fb82-235e-33ae-b3a7-eabee1b82020 | -2.7243 | -54.1552 | 2024-11-06 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 72712d42-a8cd-37e4-a333-ab28ba5554d5 | -2.7639 | -53.2265 | 2024-11-06 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| e633851c-4181-3145-9882-42c88dd7909f | -2.9186 | -51.047 | 2024-11-06 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 0b4dfcf9-2bf7-3fde-b736-8ce664558035 | -3.1433 | -50.2044 | 2024-11-06 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 94272f38-4cc5-3b4d-a454-e6eb8161d4a2 | -2.764 | -53.2062 | 2024-11-06 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e8dc0084-9d52-34d2-b8ed-d9272d4264ef | -2.7243 | -54.1552 | 2024-11-06 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 161.6 |
| ff2e73c9-380b-3880-85f2-3bbf6611abbb | -3.0397 | -53.2603 | 2024-11-06 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 02c2ed26-fb2a-3164-8bc7-9c8a75528050 | -2.8423 | -51.7735 | 2024-11-06 13:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8857fed1-47ca-33df-9aa5-73498c676fb3 | -2.6764 | -51.8395 | 2024-11-06 13:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 80b3d236-c3b8-3354-a8bc-2c981661f10a | -1.2922 | -54.5585 | 2024-11-06 13:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| fa175a23-535a-3eec-8593-7d26b9a72a10 | -4.1246 | -43.5833 | 2024-11-06 13:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 704fd692-71db-3c12-a650-21a770b2a1f1 | -2.7428 | -54.1347 | 2024-11-06 13:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 36f7bc5a-8f68-335e-aeab-7851814d0670 | -1.2922 | -54.5784 | 2024-11-06 13:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1cc85ffd-4a1c-3c88-b805-58853f374d64 | -4.2578 | -49.1678 | 2024-11-06 13:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 7da04c83-7121-3c82-9c1c-e9e8319185d4 | -2.6764 | -51.8189 | 2024-11-06 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 3ee29c85-98dd-3d9e-984f-32f84f420dc9 | -3.0207 | -53.4227 | 2024-11-06 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e0c72939-6da3-3aef-8365-de739d782350 | -7.2241 | -42.8797 | 2024-11-06 13:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 516bc1ec-eb33-31b7-a096-05e60fd94880 | -2.8321 | -49.4749 | 2024-11-06 13:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 7f9c0bb5-1c47-3167-8d26-09bdf7263d5e | -3.0207 | -53.4227 | 2024-11-06 13:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 388823cb-5d35-3c03-94e6-54fd78ca67d3 | -7.2053 | -42.8815 | 2024-11-06 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 9621809f-c20c-3330-8a54-db9de588914e | -2.7243 | -54.1552 | 2024-11-06 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 9ccd0b68-4429-37e7-a6dc-05b432220872 | -2.9186 | -51.047 | 2024-11-06 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f7dae24c-8daa-30d3-b3b3-28304386e5fd | -3.1433 | -50.2044 | 2024-11-06 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 659b1516-129a-38dd-8e69-c1cf5b5d9911 | -2.6764 | -51.8189 | 2024-11-06 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| b587884d-9c88-32b8-ac12-0de214f0d59c | -3.0397 | -53.2603 | 2024-11-06 13:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0d39d393-4158-30ee-9339-73a855f51f30 | -1.2922 | -54.5585 | 2024-11-06 13:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 71cb5196-81f7-38bb-95f6-cd8167428de1 | -2.6764 | -51.8395 | 2024-11-06 13:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 0e25a7b1-8384-39a4-9781-643f912fb91a | -2.764 | -53.2062 | 2024-11-06 13:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |


[Clique aqui para ver as próximas entradas](README73.md)
