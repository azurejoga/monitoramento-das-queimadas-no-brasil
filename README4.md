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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb65ea4b-d808-3b6a-bd2e-ec9ed6f76211 | -10.9148 | -45.669 | 2025-09-19 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 802240dc-63ae-3f95-a0b4-bd727b5244fc | -10.9152 | -45.6461 | 2025-09-19 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 976fc203-f430-3c37-8af4-4ed2fc55183d | -17.6133 | -40.245 | 2025-09-19 02:00:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 620e9ca4-7874-3ae6-9ab5-4820c8d50558 | -12.9349 | -50.5565 | 2025-09-19 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9cfd4b65-b3e1-3bd5-981d-4fc11adf0c30 | -9.1933 | -45.3114 | 2025-09-19 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c0b21144-b3de-3d22-8536-c77dbf2a1830 | -12.9164 | -50.5158 | 2025-09-19 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0bbd3bf0-add9-382a-9a0a-07e87f78fb39 | -12.8781 | -50.5207 | 2025-09-19 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b5b70734-309e-3b31-9ca3-d6fd320ec436 | -12.8969 | -50.5398 | 2025-09-19 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 904c9845-ab2e-3644-880a-7a2d6a39e16b | -9.1747 | -45.2907 | 2025-09-19 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 89d89bec-72cc-3475-9a1b-29df5840a660 | -9.1937 | -45.2886 | 2025-09-19 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 47e5a77d-eb33-3caa-9f09-3e03ff385c6f | -8.1381 | -46.771 | 2025-09-19 02:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 6be083da-915b-318e-8320-6ad1a6933c61 | -12.8777 | -50.5422 | 2025-09-19 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| de6afdc3-edfb-37cf-b343-a8b66905ae86 | -10.678 | -48.7289 | 2025-09-19 02:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 662c5702-cd60-3835-9927-a52793a9be0b | -10.9152 | -45.6461 | 2025-09-19 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 988c35d1-9e6a-369b-8c2b-0d32a9aba8f0 | -17.2163 | -45.9518 | 2025-09-19 02:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 304ff1cf-5653-35ac-b18a-33d8f0753921 | -6.2547 | -43.9009 | 2025-09-19 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e9f99d1e-cb66-3ca1-b951-22087e80d8da | -6.2732 | -43.9225 | 2025-09-19 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 86561e32-d2e3-3f22-b3bb-7760bfaf70ab | -9.1744 | -45.3135 | 2025-09-19 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 6b09cd9e-a55b-31ba-a300-ce39a1864143 | -17.6141 | -40.219 | 2025-09-19 02:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 2a0aceac-3137-35ba-b635-2f434662ed50 | -22.0512 | -45.5654 | 2025-09-19 02:10:00 | GOES-19 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 453c4aa1-0066-3f7c-943b-88e209997ffa | -25.6911 | -49.886 | 2025-09-19 02:10:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.5 |
| f342deee-6d06-3211-a49c-148aa81b3eac | -22.0504 | -45.59 | 2025-09-19 02:10:00 | GOES-19 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| f29011f9-3838-3feb-a6cd-5906042adb38 | -6.2544 | -43.9241 | 2025-09-19 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 52c3febe-fcb7-30ce-bce3-50bccb883400 | -12.9161 | -50.5374 | 2025-09-19 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4a80626c-7f6a-3dee-8ed6-bd69f35b8e08 | -12.8972 | -50.5183 | 2025-09-19 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 7e88f87b-cf3f-3466-8e06-e0605e64964f | -6.2732 | -43.9225 | 2025-09-19 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3767944a-a800-376f-8c62-c3be09667cff | -21.2831 | -54.813 | 2025-09-19 02:20:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 64900fde-552b-326c-aafc-27baeb4737b4 | -9.1933 | -45.3114 | 2025-09-19 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ad1f018e-dc81-3e46-ae18-87074314db27 | -6.2544 | -43.9241 | 2025-09-19 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 36c37ab2-5886-37e9-b6ed-f5a2cd416dbb | -6.2734 | -43.8994 | 2025-09-19 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 09c85b2f-323b-3de6-aa77-6f8390f6c525 | -6.2547 | -43.9009 | 2025-09-19 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 308555b6-dd52-34c0-9586-2137a0e16841 | -12.8972 | -50.5183 | 2025-09-19 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| bc26d428-5bbf-3d2d-96e3-a76e55e88767 | -12.8969 | -50.5398 | 2025-09-19 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 09783862-3c29-39d5-822e-1408b48f41f9 | -9.1937 | -45.2886 | 2025-09-19 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d9bcf757-8e16-3c40-a7b0-100848332883 | -9.1744 | -45.3135 | 2025-09-19 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f9e08154-f145-327c-b9b9-28c1a0f5897d | -21.2835 | -54.7914 | 2025-09-19 02:20:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f3e1f78b-99c7-3c23-934c-b680620661f7 | -17.2163 | -45.9518 | 2025-09-19 02:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7587805e-508c-3753-9ada-8e75507aa7ba | -11.2147 | -49.6441 | 2025-09-19 02:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| aaae6e82-c039-3df5-a1a1-8a01a76786da | -12.8969 | -50.5398 | 2025-09-19 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7d010bb9-e141-3989-ac70-cb7fe039f547 | -8.5611 | -47.5492 | 2025-09-19 02:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 7c88e3b7-8d39-3ac9-845b-c40ca459ba5d | -9.1744 | -45.3135 | 2025-09-19 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6196634f-0b8b-3d74-a9c1-69f7f7086e6b | -9.1933 | -45.3114 | 2025-09-19 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| eb41e205-399f-3f75-9798-504c9425e851 | -8.5423 | -47.551 | 2025-09-19 02:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0f5c77ce-7439-3856-b3c2-09b62153a749 | -22.6962 | -47.5071 | 2025-09-19 02:30:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| 09428af5-d1fc-3edd-9da0-2c1b0e702d2b | -22.6752 | -47.5127 | 2025-09-19 02:30:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| f776e00b-3173-35a5-9865-368cac478297 | -17.2163 | -45.9518 | 2025-09-19 02:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 58641792-fc92-32d9-aea7-e7a062ebbd1f | -9.1933 | -45.3114 | 2025-09-19 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| fb5b9675-ca6d-38be-b6c8-3b2159bca0ff | -11.2147 | -49.6441 | 2025-09-19 02:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2ab7f886-c63d-3155-bbd1-be53440de16c | -10.9152 | -45.6461 | 2025-09-19 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| db90c777-5a16-30c9-a19d-7f19d1c2f979 | -6.2055 | -45.1187 | 2025-09-19 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 7db00ec7-e1ed-3cc6-ba50-b1fecf2432ee | -17.2169 | -45.9282 | 2025-09-19 02:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 177.3 |
| bde0dcc3-afde-3b06-8b60-d001e2e8c67b | -17.2163 | -45.9518 | 2025-09-19 02:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 366.8 |
| 18221575-bee4-387a-823f-2e1866ce625c | -6.2057 | -45.096 | 2025-09-19 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 9c2469ef-2edf-380a-97bc-0e77dabdaa85 | -17.2369 | -45.924 | 2025-09-19 02:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 22d4834d-d6dc-3b1c-af94-25f67031d93b | -6.2245 | -45.0945 | 2025-09-19 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e43c86f0-8270-339b-8cb7-8ef4afb93f01 | -17.2363 | -45.9476 | 2025-09-19 02:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 209.4 |
| bf241cee-a1e4-3d24-9a1c-4c2809986c50 | -11.215 | -49.6224 | 2025-09-19 02:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ea3e3aa2-3faa-3237-918c-e5dfd0f50b54 | -5.1386 | -47.8314 | 2025-09-19 02:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 56071837-96a0-3127-8333-727262415ded | -9.1744 | -45.3135 | 2025-09-19 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 8774ea32-bf6c-3c51-9d76-860b5d9af9c8 | -17.2369 | -45.924 | 2025-09-19 02:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 58636155-c235-3534-aba1-c801020ba651 | -17.2169 | -45.9282 | 2025-09-19 02:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3d689dc5-ebc3-3d60-a050-f37911ee2524 | -17.2163 | -45.9518 | 2025-09-19 02:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 199d1c36-8792-3438-ba8a-a7934d1335b3 | -17.2363 | -45.9476 | 2025-09-19 02:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 261.4 |
| 7c564f90-5b0e-3080-a214-0ec658b91d35 | -11.215 | -49.6224 | 2025-09-19 02:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8bb3eb50-62dd-37fb-93c6-5a46ef53d41b | -9.1933 | -45.3114 | 2025-09-19 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2dbef9c8-7b17-359c-ada2-ca0bdaf4e18d | -9.1744 | -45.3135 | 2025-09-19 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 722af8c0-9909-3f73-90f6-3d9030b51ec1 | -11.2147 | -49.6441 | 2025-09-19 02:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 28c64989-8536-3ae7-bb7d-6c7ac0ba50ab | -7.5705 | -45.4786 | 2025-09-19 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| edecf11c-fd04-3999-a8b7-203e89d00cae | -9.1933 | -45.3114 | 2025-09-19 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2832e60a-d97a-3e67-ab99-6a29ce14d4c9 | -23.6786 | -51.7277 | 2025-09-19 03:00:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 14585205-9bf9-3920-adcb-cc596f4d97c7 | -17.2363 | -45.9476 | 2025-09-19 03:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 307.8 |
| bfa3912e-0e21-37af-a7fe-66ab0c7e69d6 | -17.2369 | -45.924 | 2025-09-19 03:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c80c0761-ce69-3dd4-bd5f-0be58025e6d3 | -17.2163 | -45.9518 | 2025-09-19 03:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 3ab19f59-5938-3d46-b342-1bdd45096267 | -8.5611 | -47.5492 | 2025-09-19 03:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 99ef6658-c20d-3b06-b4e4-12ecf913d26e | -21.2831 | -54.813 | 2025-09-19 03:00:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b0674db9-adc3-3243-996c-2da1b1dbe836 | -17.2169 | -45.9282 | 2025-09-19 03:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 50af5d51-e7c9-302b-bfe4-ff83c682175d | -6.2057 | -45.096 | 2025-09-19 03:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b8240737-fd25-3e46-a584-36307fbfdf2e | -9.1744 | -45.3135 | 2025-09-19 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d70baeda-6d79-3518-ae9c-9b866a6942da | -7.5705 | -45.4786 | 2025-09-19 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d11bbd82-52bf-32e3-b824-70c42bc22be6 | -5.61236 | -37.53447 | 2025-09-19 03:04:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 265ff3ce-1524-33c1-b35e-c9e9762f658d | -5.57957 | -35.40166 | 2025-09-19 03:04:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1f769eb-0b1c-35d6-b9fb-6a2c6e7a2910 | -6.28816 | -35.21627 | 2025-09-19 03:04:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 82849acc-bf2a-3029-b2b9-36a60da93390 | -11.92918 | -38.33451 | 2025-09-19 03:06:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ddd8ee46-6c8e-387d-bf95-382b266b980a | -11.93099 | -38.3353 | 2025-09-19 03:06:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7c237a5e-d9c5-32af-ae9c-5e4e7042ac65 | -11.93008 | -38.32992 | 2025-09-19 03:06:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b7447ded-77e4-3978-92d6-6090073ec519 | -11.93192 | -38.33072 | 2025-09-19 03:06:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0ec91a72-bc54-30c3-964f-833541da415b | -19.79409 | -43.74149 | 2025-09-19 03:08:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77610fdd-8272-3461-9d0d-e78b15383ed9 | -17.22482 | -40.92989 | 2025-09-19 03:08:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7254fb6e-c207-31ab-917b-91fa4f4e3d52 | -15.61081 | -40.79294 | 2025-09-19 03:08:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4139870-c73d-3f48-a4c3-d11a48726b5f | -15.60958 | -40.79858 | 2025-09-19 03:08:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc145f82-eb72-337b-998c-1b3f7262bd49 | -19.59749 | -42.10442 | 2025-09-19 03:08:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 74b4835b-0b1f-3bc6-9a23-a282dec27097 | -15.32371 | -42.05506 | 2025-09-19 03:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 959befeb-15c9-31ff-865f-7c40a37dd775 | -15.32557 | -42.05639 | 2025-09-19 03:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b35f38ca-1f1a-30db-a8f7-9075de106e1d | -19.787 | -43.73999 | 2025-09-19 03:08:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b5162b7-eca3-3aab-9ee0-12399bdba4bc | -17.95809 | -39.71389 | 2025-09-19 03:08:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| de2ca978-be0d-3162-9db2-7be58f0afffa | -17.95905 | -39.7095 | 2025-09-19 03:08:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 832d0203-9a00-3055-a975-b5541c171f9a | -19.59888 | -42.09851 | 2025-09-19 03:08:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 82d640b6-5e99-32b3-a988-069c495f0ff2 | -19.95126 | -42.41869 | 2025-09-19 03:08:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8eaadabc-a5aa-3a89-9b55-4c4766ceaade | -21.2831 | -54.813 | 2025-09-19 03:10:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| bf63dfe4-0afb-3594-b47a-d4af57db301b | -9.1744 | -45.3135 | 2025-09-19 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |


[Clique aqui para ver as próximas entradas](README5.md)
