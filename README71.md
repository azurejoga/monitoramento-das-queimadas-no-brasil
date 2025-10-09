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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 368b8c68-acb4-3b1b-83ab-10d7e03f58bf | -8.1618 | -43.323 | 2025-10-09 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| 402e1e9c-4a4d-30c7-9b7d-18192d625b0b | -14.9699 | -49.9263 | 2025-10-09 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d467cf25-6654-3633-8142-5e07b386e427 | -11.993 | -45.1958 | 2025-10-09 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| a81fb4bb-0230-3193-837f-daff19110bb0 | -13.0976 | -47.7982 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 39d12d9d-340e-3e13-b89e-43528a40df20 | -13.0775 | -47.8457 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 3ee94ef3-a54c-3dc1-a997-7d59d7f6bcb9 | -12.2754 | -47.6473 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| e69952bb-65cb-3ab9-89bc-ef319598b286 | -14.9562 | -46.7786 | 2025-10-09 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8e77f51d-f14f-3ec9-af0c-f91dbf2d3423 | -13.7548 | -45.723 | 2025-10-09 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 1771b449-2bf5-3f4e-97d9-72cd61ec057f | -13.0779 | -47.8234 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 84f45bca-55ed-3ee9-af07-44e9992c9f5a | -7.5041 | -44.7109 | 2025-10-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 5378e867-4b79-3483-989e-f899ffbd15be | -11.7833 | -45.1347 | 2025-10-09 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| f78549b2-fc1e-356c-99fa-894e999d5451 | -14.3543 | -50.7551 | 2025-10-09 14:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| fc3c6272-14cb-36a2-b3f6-ce3935c8762a | -10.1386 | -45.4497 | 2025-10-09 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 8be841b6-a09e-38e3-ba1a-612eb0969eb8 | -14.9367 | -46.782 | 2025-10-09 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 205.8 |
| cb2a6039-e90f-3041-b876-4c9833a0ef1c | -15.8288 | -43.7555 | 2025-10-09 14:30:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 518e94a7-887f-3916-a7ec-16f4eb49f34b | -8.5941 | -44.9209 | 2025-10-09 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 483c6b19-e7a5-3e8f-9c36-fbb971e71885 | -15.3988 | -47.9712 | 2025-10-09 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2e106b2d-2405-325b-a58b-e240964041cd | -3.8948 | -41.5458 | 2025-10-09 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| deaa096d-941a-3af9-9d99-c770a26dcc03 | -13.1361 | -47.7926 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| a8a94b6c-fe9f-3250-9d2c-1e9cde321731 | -17.3781 | -45.0687 | 2025-10-09 14:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 1bb17806-9f0e-3387-bf5f-667df5483c2b | -15.4772 | -47.9578 | 2025-10-09 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 148.3 |
| fcc51f3e-b1aa-3512-b620-cd69d661a10c | -8.5602 | -44.6264 | 2025-10-09 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4a86ca0c-47cf-3103-959d-bea7d37f6be0 | -8.6292 | -45.1228 | 2025-10-09 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 6ac21367-de3b-3347-908a-5006f191e37e | -17.9002 | -57.6594 | 2025-10-09 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.5 |
| edbad37c-0d52-3614-8d55-917862d132aa | -7.7115 | -44.6681 | 2025-10-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a06e47bc-6501-3df4-94dc-124aeb6ba14d | -14.3349 | -50.7578 | 2025-10-09 14:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 1c12a1fe-3dac-32b1-ae59-ff65ca739b46 | -14.9985 | -47.5434 | 2025-10-09 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d4e060f3-e0f2-3d11-a20b-375071bdcf12 | -13.0783 | -47.801 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 2ec61a5e-f3ac-3e3f-a39b-229f9b38b435 | -13.4101 | -47.5506 | 2025-10-09 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 98ff920a-652b-380b-ab76-e575982ca0b0 | -14.4452 | -47.9943 | 2025-10-09 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 92f26f8d-5c0a-383c-88d4-36c2258ba32e | -14.2754 | -45.8647 | 2025-10-09 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| d1eb9c1d-5d19-3964-a5b8-b2abc00f9c93 | -13.8307 | -45.8024 | 2025-10-09 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| bf9eb9c5-d880-32f4-a34c-aa6cc11ecc8b | -14.4452 | -47.9943 | 2025-10-09 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8ed83090-253b-353f-95ff-1ec51937b7fc | -13.0586 | -47.8262 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| d49ec1ab-08ce-355d-a556-9062ac857c1b | -13.8108 | -45.8288 | 2025-10-09 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 584bc044-4899-301f-8984-b59317090510 | -14.2754 | -45.8647 | 2025-10-09 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 73d9e9dc-7402-3b86-8fec-a5d28fa65667 | -15.8091 | -43.7597 | 2025-10-09 14:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 39db0815-96b1-36bb-8fc2-c62cc076dbd5 | -13.7913 | -45.8321 | 2025-10-09 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| b8bb1bee-f947-30b3-ade0-5a44b6a5b88d | -13.3631 | -48.0044 | 2025-10-09 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 448a9b7f-419f-3816-90e0-9de87524c7f6 | -11.7501 | -64.8814 | 2025-10-09 14:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a4c6d762-d5d4-3639-a1c3-659ff698510c | -13.1361 | -47.7926 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 58113519-cd24-3a95-ac60-3ea8abda38dd | -17.9029 | -57.4947 | 2025-10-09 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| d419c16a-035a-3208-a774-d4bf6001329c | -14.4457 | -47.9719 | 2025-10-09 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 8e698a3a-ef8a-3207-b9a7-282946c4a1b2 | -14.9985 | -47.5434 | 2025-10-09 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 50abd74e-76b9-3951-a9ed-350b0714c11f | -10.1576 | -45.4473 | 2025-10-09 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d303aeec-9a2c-3aa5-a9dd-9792867a85e0 | -11.7221 | -45.3508 | 2025-10-09 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 7e6019e6-6a3f-32e5-8483-f29288b7db45 | -14.3349 | -50.7578 | 2025-10-09 14:40:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 62299650-923d-3c47-a1cf-cf05c27005b1 | -13.2971 | -48.4579 | 2025-10-09 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 171.9 |
| ecbdb9cf-e294-3e1d-a85a-85bfb3e6c4f0 | -13.8302 | -45.8255 | 2025-10-09 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 299.8 |
| 5d12478d-bec2-345c-849c-54635e79a831 | -11.7833 | -45.1347 | 2025-10-09 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 994ba095-9f8a-3d0a-8c90-39dd8838ca8e | -11.993 | -45.1958 | 2025-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| e6a1e99a-9752-3946-a6fd-f6770da3ee4b | -13.4101 | -47.5506 | 2025-10-09 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 2ca35955-cb41-3f3a-a1bf-8409967c75f5 | -17.9224 | -57.5128 | 2025-10-09 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 496ad613-33cc-3424-a803-d8fae20f4bc6 | -15.3984 | -47.9938 | 2025-10-09 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 9b363436-eb74-3a6c-bae2-e3e01e7b8f96 | -10.1389 | -45.4268 | 2025-10-09 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 157.5 |
| ec35a42e-eff9-371e-9b4c-196313e4dd3f | -8.5602 | -44.6264 | 2025-10-09 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 8c00d205-5a95-32e5-acca-6d18056d0363 | -13.0189 | -47.8988 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 66601e2e-5990-3330-8046-3eec4125a1f3 | -5.5882 | -45.1412 | 2025-10-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ea2cd29e-162b-3ae1-ae37-2af5b14da4f8 | -13.2967 | -48.4801 | 2025-10-09 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 161.8 |
| f95f4803-ec2e-3d15-a2b3-a880b64d1090 | -17.3781 | -45.0687 | 2025-10-09 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| eaafca4e-31ea-3bd8-a4c5-5041b69c63b9 | -16.2788 | -47.1556 | 2025-10-09 14:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 47bd9afe-707b-34e3-bc88-af313b8f3a12 | -12.6964 | -47.6776 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| c68704fb-9c8c-387f-ae19-b828f361e5a6 | -8.2083 | -44.1105 | 2025-10-09 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 504bb778-6a75-32b4-9feb-aa03153578eb | -8.1894 | -44.1125 | 2025-10-09 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d8d1e2bb-8f30-32ac-87b4-abb95311954e | -4.6095 | -43.6711 | 2025-10-09 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a7bc5ac5-7308-3d0c-a4ed-b8d6ef091c97 | -16.2986 | -47.1519 | 2025-10-09 14:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 85454db6-ad2d-3c97-802d-9f3bb0d77205 | -13.0783 | -47.801 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 0847d674-e09f-39d5-8b91-eef933c98bf9 | -8.5599 | -44.6494 | 2025-10-09 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 796cc661-4873-380b-8b58-a1f972fc8158 | -15.4772 | -47.9578 | 2025-10-09 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 4f1030e1-cae1-3ce3-b2b4-d0a58d570055 | -15.8288 | -43.7555 | 2025-10-09 14:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 65e81180-8f71-3cbd-acda-692ed988221d | -11.785 | -45.0421 | 2025-10-09 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 5eafd0f0-8599-3111-851a-b7c035528431 | -13.0775 | -47.8457 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| f121052e-5711-3a74-98c4-7de300cd2188 | -4.9011 | -42.2464 | 2025-10-09 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| a828a429-15ea-34ff-92f2-ec879adb9341 | -13.0976 | -47.7982 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 422e0139-9b3c-378c-93c3-2fc6293fd269 | -7.8119 | -44.1516 | 2025-10-09 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4079081f-5962-3857-958b-88820d5a40cc | -13.0582 | -47.8485 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| c83e123b-7034-3cf3-9eb9-6dc04a3f26e5 | -9.3209 | -45.6607 | 2025-10-09 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| a958636e-b4f3-33d8-b4c0-21e82b022919 | -13.2779 | -48.4607 | 2025-10-09 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| c5f0b91d-47bb-3f4e-ba5d-ede471d692c1 | -10.1569 | -45.493 | 2025-10-09 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 5ba5eaba-be2b-35d5-831a-15f2728d9b2e | -8.5944 | -44.898 | 2025-10-09 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1d0a220b-40e8-38ad-9cad-40ae393e1104 | -13.0779 | -47.8234 | 2025-10-09 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| c44acbbb-ef7d-35b6-8687-fe4a08f6c237 | -15.3988 | -47.9712 | 2025-10-09 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 6ffee95a-8cdc-3ed5-b4d6-eb7717e23548 | -8.1687 | -44.2534 | 2025-10-09 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 030f6454-4f04-3100-9a93-5ded18988413 | -7.8687 | -44.1227 | 2025-10-09 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8a0d0bfe-3301-3be9-be6a-d28a0450a9ad | -8.1804 | -43.3445 | 2025-10-09 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 173.2 |
| 7715ff5a-04e7-3648-9c00-868334fee330 | -13.3052 | -48.0129 | 2025-10-09 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 58f39dd1-5b8b-3078-ab4b-d83d99f91b43 | -10.2136 | -45.5087 | 2025-10-09 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |


