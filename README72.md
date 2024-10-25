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
| 23acc641-5ebf-34d2-aab0-8d1c428e6380 | -11.5965 | -48.59609 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a68550a-4fc4-3361-8497-ef4ae9bbc02e | -11.59593 | -48.55344 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3c65d67-6950-3a46-8a93-f3c540181e1d | -11.59307 | -48.47901 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df700aea-8712-3925-96be-5330bdc4af39 | -11.59248 | -48.55291 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b7e77fc-9c34-3b5e-87f2-9ec2a069d089 | -11.57018 | -48.65371 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c6a332a-4c07-3907-bd5d-2b5baf38a7ff | -11.52721 | -49.07269 | 2024-10-25 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 303fd27a-5101-3a46-bfb7-7a6995275673 | -11.52665 | -49.07633 | 2024-10-25 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e47db8c-d8cf-348d-abc4-a1869eccb01f | -11.50459 | -48.71673 | 2024-10-25 04:40:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35d91ccd-2668-372a-bca2-ea16b13c7d2e | -11.43552 | -48.47865 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee9fd1c5-5401-3c62-9ebd-a1c83b55e343 | -11.3076 | -48.47915 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da2a086c-abd1-33a5-bc73-01cdd799d4fd | -11.30702 | -48.48295 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 624b53a7-51d3-3d5d-a6b7-e1754fb5ccda | -11.30694 | -48.64125 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f516972-6db8-352e-9de0-a358ecb68405 | -11.30602 | -48.4828 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ed226179-c968-3556-ac1c-b629918d60d7 | -11.30357 | -48.48243 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ef4944c-485c-3331-8d4b-681c60871a64 | -11.30299 | -48.48624 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baa09755-ed2e-32a3-9d5a-a7dc3466f1d2 | -11.30121 | -48.63274 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c782ae1-42d2-31de-a209-22f03899c350 | -11.30071 | -48.47809 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6604705-13ee-3bb5-86cd-d99423b2091b | -11.30064 | -48.63654 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29639258-d653-3895-aebf-c426e71e117f | -11.29896 | -48.48957 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 161856da-ba8e-3990-9aa7-a58736f0dec6 | -11.29837 | -48.49342 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3fc09a3a-b9f3-370e-bead-862dfb91c08f | -11.29778 | -48.63225 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 157f529f-c5c8-3c82-bd2d-16fd09dd1135 | -11.29668 | -48.48138 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec079f15-994b-3346-a59d-d5d9791eecfb | -11.29551 | -48.48907 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7f02259-4fb2-315e-aa26-d658016f3fe2 | -11.29492 | -48.49293 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d68b9de-2de6-33a3-8d38-42dd776b7c58 | -11.29149 | -48.49237 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37581a71-b5a1-3d77-a11d-667c3e7274f3 | -11.28863 | -48.48801 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b10cc5f3-f50a-39c0-b186-22f57019bdd2 | -11.28805 | -48.49181 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e2d8796-74f2-3963-a17d-8adecd3414a8 | -11.28578 | -48.48361 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a20205fd-adb0-3d8a-bc96-bb6d6c9f89e7 | -11.28519 | -48.48743 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 091057ba-51f5-3202-8bb4-bc09083f3447 | -11.28234 | -48.48303 | 2024-10-25 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55f0a5ed-bf57-3173-9866-71e691d6d5cc | -11.28208 | -49.01268 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01735333-d460-31bb-b2dc-8ed32fd5dcaf | -11.25547 | -48.72861 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 457499c9-23b6-3541-9f85-87c0be0ee356 | -11.25318 | -48.69781 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbeba583-993d-3b6e-af98-39d103fbce5f | -11.25149 | -48.7318 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64acf888-2e69-3c38-9470-4702e12f9859 | -11.24976 | -48.69728 | 2024-10-25 04:40:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5535df50-bf3e-37f3-8304-1b49e7b1ae79 | -10.88105 | -49.14505 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34a80126-c0ed-3339-b5b6-4f5399f39746 | -10.8788 | -49.1373 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 022eb0c5-22a2-37c2-a606-5e08192ba1d5 | -10.87824 | -49.14091 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bec7c17-c01b-3272-b95e-79acd3bdede5 | -10.87768 | -49.14452 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4b5462e-0d73-3d69-8aa3-d6c1bea0b3d6 | -10.87487 | -49.1404 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d403843-6fa0-3a5c-aff3-061bbf5d323a | -10.77237 | -48.99053 | 2024-10-25 04:40:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dac86657-c838-337b-a9b2-13ca2b7add57 | -12.3291 | -48.00935 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3331aab-8ebc-33b5-b1be-6796e45f5ab6 | -12.07695 | -47.98592 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3168650-0f0f-3543-824b-157f56c2e028 | -12.07341 | -47.98537 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc60b9c8-8be8-3c14-8162-24759887442c | -11.85508 | -47.9291 | 2024-10-25 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c34fafa-f27e-30ed-9a60-11d6c9920d1e | -11.72973 | -48.35788 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31d046fc-5ef9-3966-b6a0-32f2e776bba4 | -11.72915 | -48.36174 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d239c7b-6c54-3ce3-b85d-cadd318f0334 | -11.72626 | -48.35735 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4621acc-27cc-3ebc-8a2b-a5e297dbe9be | -11.63057 | -48.3947 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b927d116-78ed-3f53-ab98-b78d778a472e | -11.62711 | -48.39417 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1f9648c-1d1b-3c78-9bcb-e5d1cf4f4bbc | -11.62423 | -48.3898 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19c85490-4a70-3ff6-9430-f358154c2ea1 | -11.62365 | -48.39363 | 2024-10-25 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad6e00d7-69e0-3e83-b2f8-8ac247faf36c | -11.42594 | -47.81517 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d5caa8c-01cc-3c59-9a3d-a5273bb86ccf | -11.4224 | -47.81465 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2970f63-8bbb-3131-af41-b1fbeabd4c04 | -11.08169 | -48.334 | 2024-10-25 04:40:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbc42595-e625-3b72-b5ce-a13c076e5b35 | -11.07929 | -47.89631 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d76c359-a424-314a-8930-119cd82c36d2 | -11.07871 | -47.90022 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4679529-9e9a-3f08-8bb5-54ed38d03ff1 | -11.07814 | -47.90414 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2c0fa6d-82bc-3b74-9e3c-91a529df80c0 | -11.07578 | -47.89572 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cd2b523-7ab7-3fec-9fa1-31e0f9716281 | -11.02009 | -48.27297 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92de61d9-6634-3e05-afbf-89063d2fbb23 | -11.01938 | -47.88884 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51bc3ec9-0be5-3cea-bdf4-9621ac59fe1f | -10.94711 | -48.03808 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38050df2-6eb6-39b5-bee6-b0c68e475544 | -10.94651 | -48.04213 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58f73519-8ea8-3828-8b4d-910ceecb693d | -10.94598 | -47.80079 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a618f03-07e7-3040-9ab9-9fb16bf54c20 | -10.94361 | -48.03762 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b57e9a6-c427-336e-b8bb-d6a0795487e5 | -10.94251 | -48.03773 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f7f8c10-d9d8-360f-8e52-23c26bf68f02 | -10.94245 | -47.80034 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa099268-5fb0-38a0-9476-1707cc632095 | -10.94242 | -48.04569 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cc6a02a-374f-3f05-b05e-5d8fe970f76c | -10.94128 | -48.0458 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d153ada4-c5ff-34e6-8d34-b4399e7036a2 | -10.94011 | -48.03716 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6a4a23e-2d3d-3708-8b62-9cdba639b242 | -10.93893 | -48.04524 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cffd1be8-7306-3203-8053-34da081f082a | -10.93891 | -47.79992 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d78b3d79-6e38-3245-8365-b20c167654c2 | -10.9383 | -47.80395 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4d0f7b9-f2b5-365f-b6a7-9be19d2433ad | -10.93778 | -48.04533 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed47504d-7699-3b9e-88eb-2986013c39ba | -10.93478 | -47.80339 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7ef6c61-534e-341e-b58d-5b9092746df6 | -10.9341 | -47.83204 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cd185d1-8b90-33ba-9758-2e24fdc9bbfc | -10.92106 | -47.9668 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b5ee12b-130a-3a0f-b3b0-f8683ec66c76 | -10.32988 | -49.35649 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a25f0a7a-680b-3b21-936f-d3254c6a784b | -10.32933 | -49.36005 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e2f38ea-a095-30f9-b952-023b3f610957 | -10.19754 | -49.14557 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 316b4f51-ef35-3394-9a1b-afa64f7c85c4 | -10.19698 | -49.14915 | 2024-10-25 04:40:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c78d797a-cbba-3832-8c08-ae380d61b43f | -10.87359 | -49.53603 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 769fa54c-bb41-32f0-a8a4-5570d1fed669 | -10.87304 | -49.53959 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b95bd0dc-99a4-30ba-a21f-81d4e98448d2 | -10.54638 | -49.79632 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a4d5fcd-6f0a-3b4b-9ef9-f105a608b2e0 | -10.51293 | -49.46127 | 2024-10-25 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eca66e6e-1f81-3ad4-97c7-d7557f5553ad | -10.37479 | -49.91686 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e9a320a-5ffc-341b-8875-fa6e4e13322d | -10.37425 | -49.92037 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c9e7d6a-223a-332a-b577-1a2640422b8a | -10.17776 | -49.5064 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f441ddd2-df7a-3f2d-9543-95e29e41f395 | -10.17634 | -49.50285 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c599a27-3187-32fe-905e-c6feeb5034db | -10.17579 | -49.50639 | 2024-10-25 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61ad82db-806e-3f28-8014-96f540f82b08 | -11.25487 | -49.95565 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f869f584-097c-3ad8-b5aa-d0bb35b9e783 | -11.25432 | -49.95918 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4bcc9c4-9459-353b-8072-726d8430eac5 | -11.25377 | -49.96271 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11f8b139-c424-3148-a2a2-a52f8a86377d | -11.25322 | -49.96624 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 336512bb-bdb5-31c3-8b2a-bbbf49d58576 | -11.15297 | -49.69655 | 2024-10-25 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3118af88-a4be-38c5-bd74-90d55875549c | -11.15242 | -49.7001 | 2024-10-25 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0670470-6d30-3a8d-ba6d-36a9c095d164 | -11.14116 | -49.94858 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8fbca05-f964-3d8a-b631-d9311ea19854 | -11.04639 | -49.4753 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b99051a-0c32-31f9-9808-afdd4237aed2 | -11.0436 | -49.47119 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 261fddb2-1eeb-3905-8871-c2e0a53d7347 | -11.04305 | -49.47477 | 2024-10-25 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README73.md)
