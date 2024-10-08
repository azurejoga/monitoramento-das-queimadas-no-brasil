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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c8cf992-9c03-3c27-8e63-7b917de75b1a | -12.5717 | -53.0753 | 2024-10-08 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 0942f15b-59a6-3826-90cc-9e6862aa7503 | -12.572 | -53.0544 | 2024-10-08 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 196.8 |
| a306ce8e-474a-3f20-8d09-e32cf340be35 | -12.5907 | -53.0732 | 2024-10-08 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9876dc25-63b9-35e9-b741-33ba59e006a1 | -12.591 | -53.0524 | 2024-10-08 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 424083c8-cc3b-3b18-b099-331e1e32cbdd | -16.5512 | -46.4592 | 2024-10-08 04:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 062c7df5-0423-3eb7-820f-0ea2c6dfe7db | -16.571 | -46.4553 | 2024-10-08 04:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 7f791e60-cbdf-3866-87d1-a49028ff5fc4 | -16.8048 | -57.4197 | 2024-10-08 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 3e8e39e3-563c-3f25-b6a0-170de75e3209 | -16.9211 | -57.4881 | 2024-10-08 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 2ac8748a-24ec-372a-bfde-a92e7599f5b5 | -16.9214 | -57.4676 | 2024-10-08 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 3cd41739-763d-3e5c-a656-7414b0168cfa | -17.0123 | -56.6773 | 2024-10-08 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 29cf0b63-6e21-38d9-bcd8-9c8a84b7b46c | -17.0982 | -57.4267 | 2024-10-08 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 260d370f-c0bf-3698-99e4-968447fd18fe | -17.0992 | -57.3651 | 2024-10-08 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 7fcc6d53-791e-3ea8-a249-6188fdc13663 | -17.1074 | -56.851 | 2024-10-08 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 8f19a5db-b89f-33ee-8c22-345b16b4a21d | -17.1178 | -57.4244 | 2024-10-08 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 34eea580-f8a9-3e29-83bf-ef75d50bc410 | -17.1274 | -56.828 | 2024-10-08 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| 2c71f491-1ae8-36d6-842c-4bea5dacca40 | -16.9407 | -57.4859 | 2024-10-08 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| a20f0245-ad45-3565-93f4-b28e4407b6b8 | -16.941 | -57.4654 | 2024-10-08 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.5 |
| c82c3735-41f5-3d6e-b9c6-9ca10dc3005f | -16.9924 | -56.7003 | 2024-10-08 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| a21ce570-8eca-30ec-9ede-46991f754cf5 | -16.9927 | -56.6797 | 2024-10-08 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 46607525-c430-38d9-9b3d-85a79c88c761 | -17.1471 | -56.8256 | 2024-10-08 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| e608388e-3c9a-3fcb-a7bb-4d839745ba32 | -18.4931 | -53.4457 | 2024-10-08 04:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 3e37765d-f00f-37b5-828f-b07da1b8c028 | -18.5499 | -52.6391 | 2024-10-08 04:06:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 011ed4f4-60c7-3fa4-ab8c-57b0ebbcd415 | -18.5504 | -52.6174 | 2024-10-08 04:06:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| dbbc0dff-ca9f-3b2c-8722-effa219441ed | -18.5699 | -52.6358 | 2024-10-08 04:06:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 9fe3b963-947d-374c-b781-dfbe836a9e11 | -20.3938 | -43.9412 | 2024-10-08 04:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 1f5108a5-6c0f-3cd7-85fc-3901c100fee5 | -20.4144 | -43.9356 | 2024-10-08 04:06:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| aeca5860-e22b-331f-acc6-615fcf1e9a23 | -5.5718 | -44.87 | 2024-10-08 04:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d074f6aa-6154-32f6-a5a4-4cffe4e39aa9 | -9.4087 | -66.5438 | 2024-10-08 04:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e8ce6a6b-0d92-3cc1-bfee-f9df432781c2 | -10.6256 | -55.9154 | 2024-10-08 04:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| aa44e398-685f-337d-9753-edb4907a417b | -10.8755 | -63.8979 | 2024-10-08 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6e90ed71-8f62-35ee-a96a-a6514092662d | -10.8754 | -63.9169 | 2024-10-08 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0a3c9333-3cbf-300c-b405-f801e9a740d0 | -11.3081 | -51.0676 | 2024-10-08 04:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3f4cfa14-1bc5-321a-8226-f1f790c07645 | -11.5233 | -65.137 | 2024-10-08 04:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 60dfdc25-fc50-31cf-8c32-0bade9577d40 | -11.673 | -65.2062 | 2024-10-08 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 6cffb381-0950-3fd1-99b1-956d72c68ad8 | -12.591 | -53.0524 | 2024-10-08 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7587bb0b-41b6-38b2-9434-4588e62dd6da | -12.5907 | -53.0732 | 2024-10-08 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 14292e3d-b89f-39b9-ab07-e2f820c64a80 | -12.572 | -53.0544 | 2024-10-08 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 4c43a26a-bba4-3bbc-901b-dd11a126ba90 | -12.5717 | -53.0753 | 2024-10-08 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 19953ffa-b06e-313d-b6c4-2ad61488aceb | -16.571 | -46.4553 | 2024-10-08 04:16:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 21d8539f-4be7-3614-9262-3cf1dc961a46 | -16.5512 | -46.4592 | 2024-10-08 04:16:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e5eaa12c-6d8f-3bd7-b013-3a6d3895abdb | -16.9214 | -57.4676 | 2024-10-08 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 28f45e25-718a-39c9-b8ab-758faff547d9 | -16.9211 | -57.4881 | 2024-10-08 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 9a0a368f-9455-3d4c-bb37-a10b41b166c5 | -16.8048 | -57.4197 | 2024-10-08 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 33e3c77e-ef3e-3d0c-8dce-c601c03ec4d8 | -17.1274 | -56.828 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 3f42eb33-4f37-3bf5-ac6b-48866dea7cdc | -17.1271 | -56.8486 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 71bca4eb-e1fd-338d-bc31-66dc4db63433 | -17.1178 | -57.4244 | 2024-10-08 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 1fad3ab5-4061-333f-a818-bf07798f5a1b | -17.1078 | -56.8304 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 6362e2d9-0b34-3f4a-aea5-7693477089dd | -17.1074 | -56.851 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 637118ca-c4d6-3a77-8199-391fd143e861 | -17.0992 | -57.3651 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| ce2f84a3-3f26-3bd3-8098-7da2be8f6bff | -17.0982 | -57.4267 | 2024-10-08 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| e3259809-d5ec-3b54-96be-33842e3e5d5e | -17.0881 | -56.8328 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 3a87b1b9-e1b7-3ef7-83e4-3f9e8ff8bc0c | -17.0123 | -56.6773 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 2bd09ace-2ca0-30c3-b577-f20f09edc4b3 | -16.9927 | -56.6797 | 2024-10-08 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| b69545f9-9702-3c86-82f3-0165ad29e7b0 | -16.9407 | -57.4859 | 2024-10-08 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 38bada38-73d5-3702-9cb0-8e7da4df3082 | -17.1471 | -56.8256 | 2024-10-08 04:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 6201ddcd-94ee-3147-889e-e81b39ea64da | -18.4931 | -53.4457 | 2024-10-08 04:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |
| de0dd6ce-941e-3541-b76a-fa656bb12a18 | -18.6192 | -57.2603 | 2024-10-08 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.5 |
| d92d4536-a142-38dc-b147-9bfda96afef7 | -20.4144 | -43.9356 | 2024-10-08 04:16:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| da3da5c4-41c9-3f70-91cf-e0f801bf2b49 | -20.3938 | -43.9412 | 2024-10-08 04:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| ce6b6b78-55da-3d16-ada2-9c5980eef21e | -5.5718 | -44.87 | 2024-10-08 04:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 01433957-0934-34e8-b170-3d3ac3cfc9f5 | -10.6258 | -55.8953 | 2024-10-08 04:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fd1e0890-d5b8-3565-bb78-6447a66cf204 | -10.8755 | -63.8979 | 2024-10-08 04:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 68f4a0ed-ee66-36e0-a785-7e2b0067179d | -11.5233 | -65.137 | 2024-10-08 04:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 41733f7a-193b-33dc-aa24-4de1ad590daa | -12.572 | -53.0544 | 2024-10-08 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 7b7de582-c38c-3490-9e6c-09bf48957ddb | -12.591 | -53.0524 | 2024-10-08 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| a1031cca-b260-338b-8954-77c2c4b35c47 | -16.571 | -46.4553 | 2024-10-08 04:26:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 8a69c2b2-f521-3e7d-b140-4d43b3a5e49c | -16.5715 | -46.4321 | 2024-10-08 04:26:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2284b9b6-6f0e-3a5a-91d9-d4c65623bffa | -16.9211 | -57.4881 | 2024-10-08 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 35184a8b-898a-3668-b29d-ca13e28996a4 | -16.9214 | -57.4676 | 2024-10-08 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| ecba7cb9-ebeb-30fc-8512-63d96c6a4171 | -16.8048 | -57.4197 | 2024-10-08 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.7 |
| f621001f-8b4d-313f-83ef-5245730f65df | -16.9407 | -57.4859 | 2024-10-08 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| bd0eeada-48e3-342b-b258-5b9f611a789c | -16.941 | -57.4654 | 2024-10-08 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 0c7ed806-d3b5-3866-bf8e-ded3686015d4 | -16.9927 | -56.6797 | 2024-10-08 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| e1be64c3-d3f7-3bd7-9858-7e2f1f7f5d67 | -17.0123 | -56.6773 | 2024-10-08 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| b4b20e91-b27b-3e15-8432-9e99fb758691 | -17.0881 | -56.8328 | 2024-10-08 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 6b756e85-8de9-3f6b-8753-7c71d1588368 | -17.0992 | -57.3651 | 2024-10-08 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| a5f8900d-1c36-39d5-8844-a18154704c5e | -17.1078 | -56.8304 | 2024-10-08 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 747adf4d-ed03-3bc4-93a1-36e64ec520be | -17.1178 | -57.4244 | 2024-10-08 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 9eb9e4d3-a411-3afe-8172-5d54a3cb6c66 | -17.1274 | -56.828 | 2024-10-08 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 0c35b284-83b8-31d8-a1ab-403dfaee4a59 | -17.1471 | -56.8256 | 2024-10-08 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 68c1c72c-2e97-3d79-91ea-1e837343ed29 | -17.1474 | -56.805 | 2024-10-08 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| 37f4e82f-aac1-33ee-9d95-3eb28b59a1dc | -17.1588 | -56.1222 | 2024-10-08 04:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| d7c770ee-0246-38e6-a9eb-6248e327934c | -17.1681 | -56.7407 | 2024-10-08 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.5 |
| 38140d72-3a47-3832-aee6-1fc65d5ecf35 | -20.3938 | -43.9412 | 2024-10-08 04:26:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.5 |
| 2739c7e6-0c80-3fca-8b0c-c53ec05556bb | -20.3946 | -43.9163 | 2024-10-08 04:26:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 04ab733f-2246-39ed-bb74-1f0632d16afa | -20.4144 | -43.9356 | 2024-10-08 04:26:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| faf3a030-4a85-321d-835a-89bb751a5f99 | -20.4152 | -43.9107 | 2024-10-08 04:26:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.4 |
| 14051893-eee9-3961-aef7-e08e4048b0b0 | -5.04655 | -42.48233 | 2024-10-08 04:32:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ed19ae0a-de13-3f8e-af61-b22f74a50e79 | -6.43838 | -38.83565 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59166ac2-97da-382a-954c-7be1ab922119 | -6.43407 | -38.82784 | 2024-10-08 04:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e39b752b-e474-355f-b043-35a54b423bcd | -5.3915 | -43.57141 | 2024-10-08 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23184179-12bd-3d23-9309-1771b600ac17 | -5.32442 | -43.73165 | 2024-10-08 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1eb4c638-5c5c-3474-991e-171e1035d8fa | -4.65942 | -43.77074 | 2024-10-08 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96b7a48c-6800-37cc-be41-e54030b24623 | -4.1377 | -43.8036 | 2024-10-08 04:32:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8daccd1f-9ea5-3df0-90ea-ef374a63ca15 | -4.13703 | -43.80791 | 2024-10-08 04:32:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f02a0a08-7651-3fdf-ab04-f99b8515a289 | -4.13402 | -43.80307 | 2024-10-08 04:32:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7dc600e-6fd9-3ce8-8ddc-db91ab9651ab | -6.41943 | -43.34719 | 2024-10-08 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f453fb6-6238-371c-b5c7-d16f93366071 | -6.3153 | -43.37316 | 2024-10-08 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e4780fe-ab8d-30ba-b233-83268ac2a222 | -6.31459 | -43.37801 | 2024-10-08 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4245e177-72b7-33ee-b104-981f0b012d18 | -6.48319 | -43.35337 | 2024-10-08 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README48.md)
