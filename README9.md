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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a7846d3-2ebc-3815-90c7-177bba976aac | -12.26696 | -44.60474 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eed90f23-4c86-35e3-bb67-3fbc26f3a796 | -12.78092 | -43.91836 | 2025-06-20 03:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46ad135c-8942-358a-8944-e59384315857 | -14.43447 | -48.92733 | 2025-06-20 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c85e925-f0e1-34bb-94c0-e097f5442d2a | -14.42921 | -48.91902 | 2025-06-20 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ece676f-a301-349d-872c-c140eaa23b0b | -12.75574 | -44.40668 | 2025-06-20 03:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef6c4bd6-5c95-34a1-a52c-a01402cdfd1e | -11.12175 | -46.67274 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20400f31-81b7-3d22-91de-8c519ca7f0b2 | -19.83696 | -40.08358 | 2025-06-20 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 824c29ac-0a35-36ec-88ed-952b45796751 | -12.21408 | -45.53028 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cef0012b-5c7f-33a3-8504-2a2c257795be | -16.36742 | -46.46233 | 2025-06-20 03:40:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eac83564-8e39-3022-a3a9-56ed086271ff | -11.13503 | -46.63961 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cf52c6a-1f52-3dfd-9c27-d84be22199ba | -12.26765 | -44.60114 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f0e41936-e9ee-3076-8e90-3ffc50fec691 | -11.14458 | -46.65705 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4738e10c-3209-30c6-8beb-7488f93d572d | -11.93601 | -48.4242 | 2025-06-20 03:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7dbf648-b166-3d5a-b752-8703eb5acd14 | -11.13348 | -46.66931 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb67435d-8976-3684-a10f-35fa9a9b5e2b | -16.36827 | -46.45832 | 2025-06-20 03:40:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7057a33-1783-3b32-a5fe-4618bf3d05a7 | -12.2181 | -45.5375 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ebb0b16-bd89-348e-ac5f-9048eb18a31e | -11.14238 | -46.63557 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 966d4c94-a3ca-3fba-8340-a2552e754864 | -13.39157 | -48.45661 | 2025-06-20 03:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d01a6169-9202-35e6-98e8-e1c97f260758 | -11.12068 | -46.67799 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc36f9c3-93ba-36ac-a429-4519bd9ef944 | -11.11896 | -46.67661 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1dfbc4-7493-32e5-a47a-0a1c3e3aa5db | -11.12627 | -46.67273 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7510746-e343-3511-8435-8177dfe23351 | -11.57948 | -47.87601 | 2025-06-20 03:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b31c1bfd-ad1d-3e7f-9c52-d391b238d759 | -11.13203 | -46.64339 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccaa405f-7716-3398-85ff-400436e1e0b3 | -11.14166 | -46.66094 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5d8f09a2-29c7-3054-b1f7-c4cd99d96ed9 | -12.21398 | -45.52814 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd665d16-0db6-39fc-81fb-2bfaf44a8c97 | -11.79932 | -48.09327 | 2025-06-20 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4cb93fd-f3a5-3003-b131-56ff0f14d299 | -12.20833 | -45.52909 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2146b4d-f070-3d08-92a9-ebd6dc3ac5bd | -22.19962 | -41.64327 | 2025-06-20 03:42:00 | NPP-375D | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 736e1ced-b0c7-3fde-a6fd-7feb6383798c | -20.99578 | -41.7915 | 2025-06-20 03:42:00 | NPP-375D | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5a324c8-ec29-3d5a-a0fb-f7fc1a161ca8 | -22.78471 | -43.75757 | 2025-06-20 03:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1791b526-1ee5-32a3-b058-d7bfe0597743 | -22.67722 | -42.85411 | 2025-06-20 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8991c84b-87e7-389d-b89d-5b925439142d | -21.20859 | -48.6404 | 2025-06-20 03:42:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 74d85093-6022-382a-9139-4eb88ac6b323 | -19.64193 | -45.19655 | 2025-06-20 03:42:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efb8b1be-3d1c-3783-a558-e39592ab066c | -22.5394 | -48.81524 | 2025-06-20 03:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe7cab7d-bed5-3402-bf89-7043d308083f | -21.20961 | -48.63597 | 2025-06-20 03:42:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0f9e0d1d-16b8-3c71-803b-bdd9e2f40661 | -19.63714 | -45.19768 | 2025-06-20 03:42:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac53b925-7f1f-3fd2-90d3-24a6f867ed61 | -19.76297 | -48.29105 | 2025-06-20 03:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4cb2309-1dc0-3bd2-a2ba-b16bfa2ef9d7 | -21.20277 | -48.63877 | 2025-06-20 03:42:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6b6ac8af-488b-3357-963e-60e7d7ddc59f | -19.54639 | -49.66679 | 2025-06-20 03:42:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e0654e6a-037c-39ed-a114-ff8ad80e0653 | -22.70163 | -43.45327 | 2025-06-20 03:42:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a2322f20-85fa-3463-9a18-ecd12f0be84b | -19.63703 | -45.19539 | 2025-06-20 03:42:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37750ea5-885c-31dc-9707-11c6ee34b8a7 | -19.54001 | -49.66506 | 2025-06-20 03:42:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed6037c5-0727-3964-94cc-52a5c04a5e2b | -22.1987 | -41.6482 | 2025-06-20 03:42:00 | NPP-375D | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 0042ea31-b9e2-3d50-bc8c-3ed53c2f692f | -22.6765 | -42.85787 | 2025-06-20 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d18b19a7-1282-37db-a302-880428f49b4e | -22.69948 | -43.34856 | 2025-06-20 03:42:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8087ab5-e92b-322c-be7e-7b4049f1e075 | -21.23921 | -44.05168 | 2025-06-20 03:42:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b7a44b2-1f50-37fc-8596-76ee89b4af17 | -19.76881 | -48.29275 | 2025-06-20 03:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21ed8683-1c0c-3935-b147-3ecb3ce146cd | -19.76402 | -48.28643 | 2025-06-20 03:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a63c1f7-e1ba-3560-bf08-f1b8d42e6159 | -19.63842 | -45.19156 | 2025-06-20 03:42:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce20428f-1e37-34d0-8475-c440827b2b8a | -19.76988 | -48.28803 | 2025-06-20 03:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57f0f65b-da1b-32a2-9f0b-d7902941f07e | -10.4754 | -47.0325 | 2025-06-20 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 341d21b0-198c-363d-9543-ce64352227c3 | -11.9518 | -58.7574 | 2025-06-20 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 2b0f1718-c828-3444-9275-9c57b0265cf3 | -11.952 | -58.7376 | 2025-06-20 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 86bf7e64-fdc5-300d-9801-9de4129d5043 | -7.2219 | -43.0682 | 2025-06-20 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 30416b0c-2728-3b30-a086-07699ed93ed5 | -10.456 | -47.0571 | 2025-06-20 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ef1a0808-84af-30a9-8700-34720cc06ef8 | -10.475 | -47.0548 | 2025-06-20 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 770744aa-1d23-3ab6-91d9-98db61fa81f2 | -16.3047 | -58.2676 | 2025-06-20 03:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 76d0925d-ff1d-3bef-85df-7711f8a29a95 | -2.91729 | -48.23599 | 2025-06-20 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86e8ade6-a4f1-36fa-8032-8e7ae1e1b5ae | -2.5473 | -47.70358 | 2025-06-20 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 780e42a6-eb74-3df1-ac1e-ba71298ba25d | -3.04411 | -49.42713 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccf946d4-a126-3d68-9b74-84922d969840 | -3.03127 | -49.43315 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae18f7dc-3eaa-3fcc-9670-26aadd91897d | -5.15864 | -38.00004 | 2025-06-20 03:57:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45465b89-1920-3592-a32e-b24f9fc98663 | -3.61015 | -47.53715 | 2025-06-20 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea463aa8-fcc4-3442-ad81-b986cf4583f3 | -2.28826 | -48.5763 | 2025-06-20 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55eed298-5504-3e2b-bb7c-043d6d3f0287 | -3.03022 | -49.43436 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dde9ba7-bac9-31fd-b3cc-3e207ac406c1 | -2.96322 | -49.06684 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f506afe1-0e98-3358-a1dd-14ae00fa9db3 | -2.2881 | -48.57683 | 2025-06-20 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20526073-9032-3101-87a6-b1da23c2dcdb | -3.03152 | -49.42637 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76404475-ac26-3975-9edd-c3926d8c68f6 | -2.91673 | -48.2393 | 2025-06-20 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8aa0017-75f1-3e68-8558-d58c410f9894 | -3.04343 | -49.43112 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63be6411-e40f-32d3-9761-a6d1b6b22de3 | -3.10946 | -47.49292 | 2025-06-20 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 943248e5-5e25-3643-9bf8-22fa01168a65 | -3.03701 | -49.43413 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bd689c1-4fb6-3569-a702-067a77dc2858 | -3.10993 | -47.49004 | 2025-06-20 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c156ef65-ebdb-37cd-8a04-a59fa49ddc5b | -3.41944 | -47.60576 | 2025-06-20 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05248e7d-9b73-3626-ada8-f4278394bc5c | -4.49337 | -43.77481 | 2025-06-20 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48f37a7c-3ba4-3862-b0ca-5c6bd625b5b0 | -3.03837 | -49.42616 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 063d1c8c-7769-31c4-9821-b699b1f669b1 | -4.68168 | -43.26215 | 2025-06-20 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 358a054e-ed77-37c9-8686-f53ac6b039f4 | -2.91141 | -48.23843 | 2025-06-20 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de13e542-ea0c-31c5-b77b-ce3d38af5cd8 | -4.68408 | -43.26074 | 2025-06-20 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79b650a2-369d-329e-b9ba-fa89bb7a6faa | -3.03195 | -49.42915 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5c8a2af-68e6-3b94-a5d8-1df2d9a51687 | -3.41895 | -47.60872 | 2025-06-20 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d7cca3e-eda8-3942-8894-1cdb2944cc99 | -3.03088 | -49.43034 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3df1d3db-8468-3c7b-9728-397fddd87d26 | -2.91784 | -48.23269 | 2025-06-20 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebbfef64-4796-320b-aae8-93bb023338f4 | -3.03769 | -49.43015 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78026cd3-8e99-35ef-934e-12c9d11f9102 | -4.49261 | -43.77961 | 2025-06-20 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83df703a-16f5-33aa-9ff8-ca0f65fe50b8 | -3.03262 | -49.42519 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f22ee78-a23b-358d-8963-4a8520526391 | -3.60967 | -47.54005 | 2025-06-20 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c220a7de-b4c7-3ba8-872b-5e2ea4795c20 | -2.91196 | -48.23515 | 2025-06-20 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 450f5b49-73ce-3ef0-9ea4-9e5c1c150e79 | -2.95973 | -49.06621 | 2025-06-20 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc24e75e-7b90-3821-b978-28b50e2e82b9 | -4.49501 | -43.7778 | 2025-06-20 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6f9c64-8a30-3490-b46f-9e3d9acdbdc6 | -16.305 | -58.2474 | 2025-06-20 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| a95239c9-2a9d-3eee-bed1-8a9793b88f38 | -11.952 | -58.7376 | 2025-06-20 04:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 547e0bb8-40cf-3df5-9ce6-eeb59e34f5f5 | -10.4754 | -47.0325 | 2025-06-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d7dc69f6-c1dd-36c4-b98e-b54e6877ddb5 | -11.9518 | -58.7574 | 2025-06-20 04:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e3e01892-0a65-31a8-a11e-d5322e5d03c1 | -16.3047 | -58.2676 | 2025-06-20 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 90bdd773-f27d-3c81-90eb-0915ef153e71 | -10.475 | -47.0548 | 2025-06-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 785dd19b-7bc5-3471-b4a5-7e5aaec0f50f | -10.456 | -47.0571 | 2025-06-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1e4b5025-27aa-39ed-9ffe-21333ac146e4 | -6.84392 | -42.79482 | 2025-06-20 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec50e22d-5032-3e8a-9c84-dfe2015733b3 | -9.31484 | -44.8303 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb3f3251-e7e7-3270-ab5a-f2e90a4ecc07 | -8.91049 | -49.84775 | 2025-06-20 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
