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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff1fa086-4557-3842-8612-baaa29d4b46b | -3.571 | -59.0777 | 2026-10-10 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 653287e5-c0d9-3ae3-9af6-0bb49768604e | -3.2215 | -53.8616 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 5413ab0d-67a3-3939-9b93-3998ce8e300e | -3.331 | -59.8483 | 2026-10-10 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0a76f8bb-5760-3a7d-bf21-1528354f9c3a | -1.3447 | -56.4175 | 2026-10-10 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 191.4 |
| 4dddd558-b4d6-3c89-b64e-a547a4fa0a41 | 1.345 | -56.1426 | 2026-10-10 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5e060967-7dde-3377-be4c-7af1f7e10e3b | -1.1992 | -55.6712 | 2026-10-10 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7daf1584-b87e-3dd3-81a3-683bde025a4f | -2.6262 | -56.4582 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7007f099-8ce6-3380-be99-126e7196f0bf | -2.7243 | -54.1552 | 2026-10-10 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 33111d73-844d-3411-8d59-6fb81fff78f8 | -2.6079 | -56.4782 | 2026-10-10 15:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e8a9c235-a616-3cf7-96df-3a7c74dc0c44 | -2.8529 | -54.1723 | 2026-10-10 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 61fa3339-eaee-3541-a799-2e88bc850601 | -3.0192 | -53.887 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ff54f9a3-ad33-312a-95ad-7dc735ac84f4 | -1.5307 | -54.5159 | 2026-10-10 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 7ddb6b24-3b4c-3268-86fd-a3c9bc639f45 | -10.9796 | -45.2026 | 2026-10-10 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 16d1ad36-b7ac-3965-9db1-d1b72fd61adf | -10.9388 | -45.3687 | 2026-10-10 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 3a16021b-7d04-36e3-93b3-462981111f2c | -1.2723 | -55.7494 | 2026-10-10 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 33684430-d2da-3b5c-9f50-1fa2c8fe155c | -13.7624 | -45.3519 | 2026-10-10 15:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 16c456bd-792c-35f5-bf1f-040cc08a8fd9 | -2.9267 | -54.0702 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| fbfb6021-4ba5-31e5-a3c7-50f35a955310 | -1.1992 | -55.6514 | 2026-10-10 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4b0bea0f-d35b-3897-a5de-b100940351a9 | 1.8877 | -50.6332 | 2026-10-10 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0063b6ed-708a-3cda-a5b6-1abde1df8579 | -2.8899 | -54.0711 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 59ef626d-6738-3df0-852b-fb9777265aba | -1.6579 | -55.1912 | 2026-10-10 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c4a886dd-dc71-3fe9-91d4-bc353503e7fd | -2.9451 | -54.0497 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| adc97987-12f2-3d3a-a97e-1f2b844796fc | -3.5677 | -54.6746 | 2026-10-10 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f079ab74-160a-3794-9687-35ce50de87a9 | -2.4806 | -56.0678 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5e671ee1-0530-3793-9179-7eb6d447b295 | -3.2766 | -53.8602 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 8269c953-d9a4-32f7-88a7-1bb0902ccb0e | -3.5709 | -59.0969 | 2026-10-10 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| c3afaafa-59ab-3d92-becd-bb6c81b1a8e9 | -3.1284 | -54.1857 | 2026-10-10 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| cfbfb8ea-d7b9-3786-8f01-de73baa31e6b | -15.1088 | -46.9343 | 2026-10-10 15:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 59315f18-0a40-33b2-b632-72c01b350888 | -10.9197 | -45.3712 | 2026-10-10 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| fa5718f7-4234-36e5-9726-885dbf4d2e72 | 4.2068 | -60.5915 | 2026-10-10 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9f1fa0d9-f36a-3e63-a82a-eabcea6fa654 | -3.2025 | -60.0604 | 2026-10-10 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f1a552a3-82c1-312d-bdae-9b68718c7e86 | 4.2067 | -60.6106 | 2026-10-10 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0386c9bc-895f-36c1-a1c4-bc3d322f6957 | -14.7318 | -48.2167 | 2026-10-10 15:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| dccdfb0d-5089-3342-b319-a1dfae3eee5f | -1.6395 | -55.2113 | 2026-10-10 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8ea1f725-e197-3197-92b9-9a11b65bb0ff | -12.4646 | -51.2982 | 2026-10-10 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 5f2ca31b-1b7b-351e-9ea0-623d0dc0d0ce | -3.5144 | -54.1955 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 220.9 |
| ae35c6fc-d9ef-3f3a-8d65-2e992da95b25 | -12.4837 | -51.2959 | 2026-10-10 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6fea3874-171d-3ad3-9c27-a591a9878828 | -8.9116 | -45.1833 | 2026-10-10 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| e6ca5a0a-7e62-34da-9f3b-216b50936ef8 | -3.5137 | -59.9019 | 2026-10-10 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b9c441fa-e9d8-37a0-8bf4-85c450248f18 | -1.5123 | -54.5161 | 2026-10-10 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 08cccedf-c56e-36f5-b00e-cc21de7aaa4d | -9.1072 | -67.8326 | 2026-10-10 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f4ddbbb3-bf2b-3677-b4b9-f3d4a59ae939 | -1.3447 | -56.3979 | 2026-10-10 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 254.2 |
| 8b531b36-b278-33e6-946f-96461bffa1b6 | -11.0328 | -45.4475 | 2026-10-10 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9967d7fc-81c7-35ef-9df6-47ae3af36165 | -2.5689 | -57.4163 | 2026-10-10 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 869c2399-eef3-3ac7-a6e9-b9628c3d04cf | -1.6395 | -55.1914 | 2026-10-10 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| d79989c1-afa2-3902-b6ed-76bd3aa014b1 | -3.2087 | -57.7925 | 2026-10-10 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8cfc46ad-e688-3f4a-96b2-04d6e0027f2f | -4.1223 | -54.0158 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| cf812fb2-3cb9-3737-ae27-a4ac58190ddf | -2.4806 | -56.0875 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6bc5b562-59f2-3b64-ad79-9c7788544b3f | -3.1285 | -54.1657 | 2026-10-10 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ff4f389c-e6eb-35bf-b361-92af2ffd0412 | -2.4623 | -56.0879 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 024e195f-b072-37b6-8df2-9e09720fbd2a | 1.7854 | -55.5658 | 2026-10-10 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| daa03348-5df1-3cf7-9651-db736a2296e7 | -1.3264 | -56.398 | 2026-10-10 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 679d85f2-e78f-3a54-a4ef-2d53a6ae7eb2 | -3.2765 | -53.8803 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 20319780-1363-3702-8cd0-32b9e48c0ae9 | -2.6262 | -56.4778 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| df9ac5f5-4653-31e6-9ac1-58c145ad66a3 | -3.1697 | -58.6244 | 2026-10-10 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| aa5bdeba-fa08-36b9-acc1-e1a6aae51f3d | -1.3264 | -56.4176 | 2026-10-10 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a3d6b02a-96b5-3c61-9ea5-5c4ae4cccb0e | -1.6409 | -54.3946 | 2026-10-10 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 198.1 |
| 96f73eea-9397-3781-a2e7-42392fbcf69f | 3.9309 | -61.0906 | 2026-10-10 15:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8f798133-0df0-3239-93a1-2b79e3b2b82d | -6.5519 | -61.4177 | 2026-10-10 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 27cdf593-06b1-3b2e-8c05-51f29b72b0ba | -3.2031 | -53.842 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 2ff1e97a-ec3c-334c-a03f-31b8c1fddbfc | -2.4442 | -55.9897 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 82bfd6ee-75df-35c1-b76c-aea5e5f5d0aa | -12.4649 | -51.2769 | 2026-10-10 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 75b6b2bf-ef9e-36cf-a4ae-6ad32896cd6b | 4.2242 | -60.8569 | 2026-10-10 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f2429d32-a34f-36a4-84b9-f3abbb6593cb | -1.2907 | -55.7295 | 2026-10-10 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 03774eb9-6e1f-3167-984c-42d9caad23a4 | -3.4278 | -58.0203 | 2026-10-10 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bcd81bdd-8ebc-386b-b154-f37212cb523b | -3.2269 | -57.8115 | 2026-10-10 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 11a5fc94-8a5f-30c4-acc3-c1597cc70179 | -3.1697 | -58.6437 | 2026-10-10 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fda939d3-dff3-3bd1-8b90-aefe3e42c653 | -15.0713 | -41.7982 | 2026-10-10 15:20:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 361.7 |
| e49291aa-c3c8-3405-a960-23c0bba4ce9b | -1.5306 | -54.5359 | 2026-10-10 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2cffbd36-41dd-34aa-8af9-93b05759de5c | -3.5137 | -59.9019 | 2026-10-10 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 5d897d69-8148-36c6-9c29-c481754634a8 | -9.75 | -44.7875 | 2026-10-10 15:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| fba09632-896d-3a0a-b686-df793bb0b5b2 | -3.0008 | -53.8874 | 2026-10-10 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d63e0235-9643-384a-8b03-88cc4060a641 | -1.2906 | -55.7493 | 2026-10-10 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| e897ece0-4dad-3d55-a75e-386fa589fcc8 | -2.7429 | -54.0945 | 2026-10-10 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6f04f945-f9ac-33d7-baa2-bb5fe2250d79 | -1.8986 | -53.9899 | 2026-10-10 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 9009a6b4-9471-39e9-bc37-5bdad52c7121 | -1.3264 | -56.398 | 2026-10-10 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e305567c-6a4c-3f81-9fc8-f8b27cccb494 | -1.3459 | -55.4721 | 2026-10-10 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| efd46029-df07-3001-bd43-e9b874d7dac0 | -10.9197 | -45.3712 | 2026-10-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 557.2 |
| 11ad685b-2580-35ec-b224-2701f9e0e3dd | -2.4442 | -55.9897 | 2026-10-10 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9e71d730-9ac4-3814-b239-b43e7295fe14 | -1.2723 | -55.7494 | 2026-10-10 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| bc1028ce-828f-3565-a4c5-88d2e6284b62 | -3.227 | -57.7921 | 2026-10-10 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 4eddb75a-d3e3-39f3-a52a-c5ed46b5edf8 | -9.1428 | -68.2387 | 2026-10-10 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 634affcd-47b4-348f-beaf-f367ba9dd7c0 | -2.6262 | -56.4582 | 2026-10-10 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7fb95201-5fdb-31d3-b97d-e1b1264f94b6 | -3.022 | -59.1462 | 2026-10-10 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 855b5e85-09f6-3acb-a52e-caba150bd462 | -1.6395 | -55.2113 | 2026-10-10 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f1dbccdb-b93d-3530-b82d-0148845fee25 | -3.2087 | -57.7925 | 2026-10-10 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 503e9214-575b-3617-a691-af3a7da26b31 | -3.007 | -57.8935 | 2026-10-10 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c59a1140-aa9c-3585-a02e-eb4c33c128d3 | -12.0453 | -43.4102 | 2026-10-10 15:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 61689d77-8b7b-3e19-8fd1-dbcd8ace0d2b | -1.6409 | -54.3946 | 2026-10-10 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 4fbd600d-ff4d-3f3f-9fd9-f12ff4c99563 | -3.1541 | -57.6772 | 2026-10-10 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c6105520-6526-3d39-9690-38011f4e8633 | -3.1842 | -60.0416 | 2026-10-10 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e88336b9-d332-332e-838f-5a2455ec9284 | -1.3447 | -56.3979 | 2026-10-10 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 1e3b352a-f34a-30f4-9e23-8e041b2c5a76 | -3.0254 | -57.8738 | 2026-10-10 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 59370aac-d64c-39f0-a461-6d3bfbcbab22 | -1.2907 | -55.7098 | 2026-10-10 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 31f60eb6-9c6e-3359-8cf3-9bb1df195d3e | -1.254 | -55.7496 | 2026-10-10 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f2f68ed9-b721-3593-8918-dc19d6b06af7 | -3.0219 | -59.1653 | 2026-10-10 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8b51b5fb-7e08-392d-9906-74da017e65fa | -10.9193 | -45.3942 | 2026-10-10 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| c04b6ed5-d97e-38b9-9042-000670a7770b | -3.331 | -59.8483 | 2026-10-10 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f9fd3baf-f1e4-3c2b-a321-3010ca9c17cb | -2.8247 | -57.6254 | 2026-10-10 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fa3ce078-0063-31fd-bc4b-b30d8231b0f9 | -2.8899 | -54.0711 | 2026-10-10 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README167.md)
