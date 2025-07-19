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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9a71b5b-6b95-3e53-a86a-8f07f9b9580f | -3.1384 | -47.0068 | 2025-07-19 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5767b5c3-82ef-3dd1-a650-3959b1cd6d42 | -9.8104 | -48.5622 | 2025-07-19 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| bf053b0e-9638-3524-85df-b9441b772e76 | -5.6567 | -43.7161 | 2025-07-19 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 456.9 |
| 9fe4b384-7a2c-305b-8f7e-aa7ae3937317 | -11.7508 | -48.1825 | 2025-07-19 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cc6ae890-8fbb-3924-9b51-9d74673521ab | -7.4923 | -47.4914 | 2025-07-19 00:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 95ef40e0-6f81-37ac-86ce-f9169b4e3f94 | -10.6438 | -44.7645 | 2025-07-19 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f2772bd7-5f90-321c-8aef-cd017df6841b | -5.6565 | -43.7393 | 2025-07-19 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ea82b7f0-deac-3c26-9cd1-e2a7e45db32f | -7.492 | -47.5134 | 2025-07-19 00:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 9c4d937f-eed4-368a-bd90-bb8e5cb60388 | -10.625 | -44.7439 | 2025-07-19 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 209723a3-6ac9-3481-9292-26506285fa3e | -6.1792 | -48.0494 | 2025-07-19 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 4bcb86a6-d62d-3abc-b74b-ddcf26727ec2 | -5.6569 | -43.6929 | 2025-07-19 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| fbf186cf-dfab-3445-a60d-16fa062eb196 | -3.1198 | -47.0075 | 2025-07-19 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 25554578-8b46-388b-839d-b50dd0f489b1 | -23.9623 | -52.8642 | 2025-07-19 00:40:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| a5e12775-a0a0-3e50-8ab5-b451d496f70d | -7.4923 | -47.4914 | 2025-07-19 00:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| bdd19d6b-7752-3452-9b5a-66ae33d1208d | -5.6565 | -43.7393 | 2025-07-19 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a6ecd6c1-f066-3b30-9303-b2874b4fa3ce | -10.6507 | -49.3184 | 2025-07-19 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| cb442eff-e127-3b1b-a434-2275eeebaef0 | -6.1792 | -48.0494 | 2025-07-19 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2f40850b-d80d-3715-83ec-fac11f573934 | -5.6379 | -43.7175 | 2025-07-19 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 206.1 |
| b50052ee-ae4f-382f-9b55-9735e52751e4 | -3.1384 | -47.0068 | 2025-07-19 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 46ab12bf-fe74-357a-8369-d4cc4c30b965 | -10.625 | -44.7439 | 2025-07-19 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| dc8e195d-4038-3c0f-ba80-37cb84723a20 | -5.6569 | -43.6929 | 2025-07-19 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4f81abb0-2876-3351-8167-d664ce40940b | -2.9109 | -48.2325 | 2025-07-19 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7e8e9dff-a2cf-37ec-bf6b-907b2676d087 | -10.6247 | -44.767 | 2025-07-19 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 74a3f0e5-ce2b-3c26-aed1-bc4fdf9fcb89 | -10.6438 | -44.7645 | 2025-07-19 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 77ea7bee-1638-3927-bcc8-ef456d0ca051 | -6.1606 | -48.0507 | 2025-07-19 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 5a8f2cd3-19e4-399f-9159-c8b4c5cdaef0 | -6.1608 | -48.0289 | 2025-07-19 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 96282c77-c3d5-385a-8468-519ef601195b | -7.4733 | -47.5149 | 2025-07-19 00:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 839d784c-cd91-3d21-b9a6-b6c7944a6d8a | -7.492 | -47.5134 | 2025-07-19 00:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| cb09af48-995a-3bec-97d9-d5302173cf56 | -5.6567 | -43.7161 | 2025-07-19 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 264.1 |
| 196841ef-2e82-3f89-9af1-3122ab05eb86 | -11.7508 | -48.1825 | 2025-07-19 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fbd1b9ac-3f26-3355-b48c-2bb4ebc030c3 | -10.651 | -49.2967 | 2025-07-19 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 25db7b01-e135-329e-8f90-d78f399f9c1b | -10.67 | -49.2947 | 2025-07-19 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 2e4c4055-5f33-3e86-9b20-7ead78adec83 | -11.7126 | -48.1874 | 2025-07-19 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 05a989eb-cf40-3da3-ad1d-1791807beb4a | -5.6377 | -43.7407 | 2025-07-19 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 256ac8f5-c6c4-34f5-81a1-1924ca2f80e1 | -2.9108 | -48.254 | 2025-07-19 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 576515c9-d0ff-365a-b841-32805b9f76d2 | -5.6382 | -43.6943 | 2025-07-19 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2be64d37-f17d-3149-8377-a2ffe63de9c7 | -10.6697 | -49.3163 | 2025-07-19 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 17092020-e419-3af6-8c82-0f9318cbd70c | -7.4735 | -47.493 | 2025-07-19 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 28e5caca-43fd-3d25-b7a3-fcf295212f22 | -9.8104 | -48.5622 | 2025-07-19 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b5370b0f-d8b2-36e6-aa5b-79fded10854a | -11.7313 | -48.207 | 2025-07-19 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| bfae4c27-72c7-3b1d-b889-199648311e13 | -23.963 | -52.8416 | 2025-07-19 00:40:00 | GOES-19 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 133.3 |
| 5181b99f-dcdb-38f9-a34c-d8480c4caee2 | -11.7317 | -48.1849 | 2025-07-19 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 88002eb2-2e5c-3615-bbda-055c15c2b0f9 | -11.4786 | -47.3306 | 2025-07-19 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 7c59924c-ce3c-3bf2-99d6-b27ecd237906 | -3.1198 | -47.0075 | 2025-07-19 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 55b7f1e5-9566-31d9-bed0-995cc8b57d8d | -7.492 | -47.5134 | 2025-07-19 00:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 456be64a-0b06-3d2d-8d94-62326f5904ad | -2.9108 | -48.254 | 2025-07-19 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 29fbf198-2114-30ba-b021-8769c51d38c9 | -9.8104 | -48.5622 | 2025-07-19 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 32d68c56-db3c-31a9-bcf2-2edd27dd47b6 | -11.7313 | -48.207 | 2025-07-19 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 9bd0abb5-97d5-337d-a170-125cd47f92c7 | -6.1792 | -48.0494 | 2025-07-19 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c9690bc1-c744-3596-92d1-38ddb989163f | -14.1828 | -58.1953 | 2025-07-19 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 38823b5a-9e8e-302a-bf89-8c0465c12d02 | -6.1606 | -48.0507 | 2025-07-19 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 185.6 |
| e9068d79-6649-318a-812b-4d16928f4a6a | -5.6567 | -43.7161 | 2025-07-19 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 329.1 |
| d4244b30-f47a-380c-9300-b6a56894532e | -3.1198 | -47.0075 | 2025-07-19 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ad654f41-0997-3348-b426-5dfcf3fd4799 | -10.6438 | -44.7645 | 2025-07-19 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 5fdfbbf5-e71e-38f2-aa39-35630ae21975 | -14.199 | -58.4336 | 2025-07-19 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2848c158-c3c2-3216-85d5-a756e1722887 | -11.7508 | -48.1825 | 2025-07-19 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9acf9893-c237-3af5-ab9d-deb42c6ae656 | -3.1384 | -47.0068 | 2025-07-19 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7222078b-ccec-35e3-bb8e-755825f06224 | -11.7317 | -48.1849 | 2025-07-19 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 287.7 |
| b7dde774-5d14-3d97-84a3-6f2d1517e646 | -7.4923 | -47.4914 | 2025-07-19 00:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| eb6ec0f4-e8ae-3cfe-b74c-c2209fc90fbb | -10.651 | -49.2967 | 2025-07-19 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 232.9 |
| e82668cb-3de4-3fa9-b852-f2848d8ed395 | -10.6247 | -44.767 | 2025-07-19 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 324d2291-90b8-3c46-bbe0-a7dfbbd3f3e5 | -2.9109 | -48.2325 | 2025-07-19 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d14f3888-7fd1-3556-a1fd-e5b2e52caa59 | -5.6565 | -43.7393 | 2025-07-19 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 1bf3bfa0-52f2-3f79-b2f2-3193010be151 | -11.4786 | -47.3306 | 2025-07-19 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 53769461-3b79-3e07-8026-369c46b7f2f3 | -5.6379 | -43.7175 | 2025-07-19 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 5ed2f64e-4bf8-30ec-8d90-97aed362d7cb | -7.4735 | -47.493 | 2025-07-19 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 7dae4298-1958-374f-8c1c-263b01f15973 | -10.6507 | -49.3184 | 2025-07-19 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bdf4c8b4-9603-3ed0-8894-d90ad3c07b5b | -14.1798 | -58.4354 | 2025-07-19 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 3b4842e4-8435-30e2-84ad-2b3cb84ba77c | -10.6247 | -44.767 | 2025-07-19 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 4de635fd-047c-36c7-bf12-0fcf1b93ef59 | -11.7508 | -48.1825 | 2025-07-19 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c424e591-bc3c-3108-8a75-fe89bfe4656f | -6.1792 | -48.0494 | 2025-07-19 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9a9b7cb3-dbd5-3595-91fd-cd5a18ba729a | -11.7126 | -48.1874 | 2025-07-19 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 26697f81-152b-3f2a-a50b-5ae3f8cacff1 | -2.9108 | -48.254 | 2025-07-19 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 6433223b-d1d7-381c-b2b5-16575c850872 | -11.7313 | -48.207 | 2025-07-19 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2b596597-d48c-30c2-b01d-890326aadda0 | -14.199 | -58.4336 | 2025-07-19 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| c4e6be47-f629-39fe-acfd-3e5f24263007 | -5.6379 | -43.7175 | 2025-07-19 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| c518c141-fcc8-3e09-953e-16e0ba5033fe | -2.9109 | -48.2325 | 2025-07-19 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b2312285-d507-343b-aa8f-5cbf1e8362c1 | -10.6438 | -44.7645 | 2025-07-19 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 84389f86-34fe-3d13-95b8-aa44aef3630f | -7.4735 | -47.493 | 2025-07-19 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8bf8a613-3eae-3273-a13b-e3e741ca5332 | -11.7317 | -48.1849 | 2025-07-19 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 223.4 |
| dbfa53f2-510d-313d-9529-0468c5f88332 | -7.492 | -47.5134 | 2025-07-19 01:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c7054bd5-7491-3c5a-9667-7e2122628bc5 | -7.4923 | -47.4914 | 2025-07-19 01:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| bc326d14-3beb-3386-93ea-be25d3898cb7 | -3.1384 | -47.0068 | 2025-07-19 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| dc267165-6941-3256-9ada-167d659108c9 | -9.8104 | -48.5622 | 2025-07-19 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 08c348ef-44eb-3674-86dd-35f30d4d3063 | -3.1198 | -47.0075 | 2025-07-19 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 85e1843e-d1cd-3b96-b705-b28fc60931fb | -10.625 | -44.7439 | 2025-07-19 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 60451aff-b8ee-36fc-bf6a-0423036736f2 | -6.1606 | -48.0507 | 2025-07-19 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| ae9e9127-6f98-3ce1-9fda-fb21e897704a | -5.6567 | -43.7161 | 2025-07-19 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 269.3 |
| afd7128d-cb66-3ab5-9b3e-f698f3cecb2a | -6.1604 | -48.0724 | 2025-07-19 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 1981470e-6690-3ca3-9ef8-e0f077204d5b | -6.1792 | -48.0494 | 2025-07-19 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b186abca-012e-3aa1-a279-95e013221988 | -5.6565 | -43.7393 | 2025-07-19 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1069acfe-7355-326e-879f-8c182663cb1d | -2.9108 | -48.254 | 2025-07-19 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 2097d137-0d4e-3c2b-b0fd-4442b0462029 | -3.1198 | -47.0075 | 2025-07-19 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1e0bfc11-b091-3e1c-88a1-2a2da644b859 | -11.7313 | -48.207 | 2025-07-19 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| bf80f3c5-e27d-394f-adf6-d123a1b435aa | -10.6247 | -44.767 | 2025-07-19 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 9dbcde9d-7af4-35fc-89af-974583acf8b7 | -7.4923 | -47.4914 | 2025-07-19 01:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f45c3424-781c-3c10-96a6-f3a142918813 | -7.492 | -47.5134 | 2025-07-19 01:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f6f93e46-3c82-3479-8cb5-a6824e6721ae | -11.4786 | -47.3306 | 2025-07-19 01:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 0046a8f2-c009-31e9-b673-6404d300e6fc | -11.7508 | -48.1825 | 2025-07-19 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d1503e4d-695d-3da7-bd58-589e67a7418c | -9.8104 | -48.5622 | 2025-07-19 01:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |


[Clique aqui para ver as próximas entradas](README6.md)
