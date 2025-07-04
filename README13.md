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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3cadc29-5264-3804-9d5b-c10c1622625d | -19.7857 | -47.47129 | 2025-07-04 04:19:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 612459ba-f2ae-3cac-a13c-f38cdf822cdf | -18.44578 | -54.67142 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1175368-c24e-37d0-9cac-77b04e3ad1e7 | -13.39036 | -47.82928 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 330a6a89-4dd4-3d49-b5cc-00fdc55c83d9 | -18.45079 | -54.67255 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 221a06af-4b8f-3f53-98f1-4ebfddd7b50c | -22.67064 | -47.46192 | 2025-07-04 04:19:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed8a445f-fc2c-313c-b04d-a2d169e43399 | -19.79206 | -46.30469 | 2025-07-04 04:19:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef5341b7-0e15-3cd3-83f5-5dcfe402472c | -12.10436 | -54.58893 | 2025-07-04 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaa99738-4537-39d4-b48c-feb320552927 | -19.63674 | -45.18885 | 2025-07-04 04:19:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cb18cef-cb16-35ae-85f5-4519979392c6 | -20.99538 | -51.79243 | 2025-07-04 04:19:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb21ef93-ed8d-3d29-a49f-fe88433fcc4f | -18.65789 | -55.74201 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8fb556a8-dfa0-346c-af12-e355f34e226c | -19.86914 | -48.32714 | 2025-07-04 04:19:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd1b3634-8587-34fd-b71f-bf352f76df24 | -21.20314 | -55.70696 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a127803c-2016-3fde-b962-2550ac8612cd | -19.72314 | -44.89096 | 2025-07-04 04:19:00 | NPP-375D | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a93e0e45-7442-3db0-ab99-c83ab6b55978 | -12.94035 | -47.13433 | 2025-07-04 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd818182-3502-364e-ad23-234db50b7974 | -18.66487 | -55.75113 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 057e2234-ad8b-3e37-bc01-d0e4a9cc360f | -18.66635 | -55.74404 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 12ada3d3-7a7d-324e-ac5f-596e2b05d579 | -20.72732 | -56.65591 | 2025-07-04 04:19:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5690518-e5b4-332b-a998-cb5274cbd627 | -14.60912 | -48.24652 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02f5195e-f319-3526-8d4d-5bbbd4205ca4 | -20.30985 | -45.58285 | 2025-07-04 04:19:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8543edce-3aba-374e-84ba-e15ea8fac174 | -14.80437 | -48.30785 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac3fe393-da97-34f7-afb9-bd858d103bc8 | -13.45698 | -47.83656 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb512c1f-4f19-3327-8edf-9acaf891a4d5 | -18.66249 | -55.73566 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0a55e145-1df4-365b-be77-bede8552c0c7 | -23.9838 | -48.91734 | 2025-07-04 04:19:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 863edbd2-b032-351e-ad5e-5dad0a0cfbb0 | -18.65569 | -55.74146 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 947a5d08-fa59-337b-a64a-d6e2cec612eb | -12.17011 | -56.54784 | 2025-07-04 04:19:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3924a0c-0588-3a0c-9402-ac13557d6ab6 | -12.57738 | -56.98024 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e5c62f4-464f-3a72-855b-517e3c257205 | -24.24227 | -50.74125 | 2025-07-04 04:19:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1d86738-1def-3d68-ab0b-cd9aa857617a | -22.67397 | -47.46255 | 2025-07-04 04:19:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 413c0479-5195-3b10-9780-43965b58d0ae | -18.13994 | -53.29158 | 2025-07-04 04:19:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e523755-cebe-3606-8c1e-c86c5c071a94 | -14.47945 | -46.35233 | 2025-07-04 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3c05cefa-f173-325c-b8a8-bddf0ccda171 | -13.23605 | -48.03446 | 2025-07-04 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57d59096-2d45-3294-8696-01f78cf707da | -18.1445 | -53.29289 | 2025-07-04 04:19:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15128cfd-089e-3f89-9861-b311a6c246b8 | -13.44927 | -47.81683 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e58ca5c-3b1a-328b-8ec1-f35ff0597810 | -22.66731 | -47.46129 | 2025-07-04 04:19:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9356443-f2de-314a-80cc-b3260211b0bb | -13.39888 | -47.84464 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e21d2a93-5319-3f0a-a8c0-03b40220aebb | -13.40246 | -47.84544 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 882f7471-cf73-3a58-bc60-27aa19eb307e | -13.40038 | -47.83575 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40979420-a2ec-3fe6-b9e9-342b9d4447b2 | -13.39964 | -47.84014 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a655083-6086-380b-9a17-6e86e921c2d8 | -13.38963 | -47.8336 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dc10ee9-6e75-3dce-bd5f-0d0fd3fe017a | -15.1726 | -42.3779 | 2025-07-04 04:19:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6331537-e819-3c48-866f-2ad5183f399e | -21.20825 | -55.70795 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9eaf299-4024-32c0-ae7b-2c0d2a67e512 | -13.23681 | -48.03 | 2025-07-04 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7be96eb6-11bb-34fa-9ce5-cd58cad41717 | -20.76438 | -46.76928 | 2025-07-04 04:19:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c6150d48-aabb-3cb7-9713-c231bf80cded | -22.67124 | -47.45817 | 2025-07-04 04:19:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 45f5fa5e-f12a-3e67-8d61-6b37e39fcadf | -18.44685 | -54.67263 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5b88d56-4672-3820-935c-a55e3c749759 | -14.61201 | -48.25144 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 397df0a8-35f2-32db-9e3b-e7ed0f6e29b0 | -12.57885 | -56.97294 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 737bfcf6-96df-3bf1-870b-a9e9ab3395f0 | -19.72371 | -44.88719 | 2025-07-04 04:19:00 | NPP-375D | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd48e8aa-57b5-3f3b-b902-0814a9f9d41a | -19.8493 | -43.84296 | 2025-07-04 04:19:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ca806f10-41a4-3345-afc5-c52558df8ec5 | -21.34763 | -45.51369 | 2025-07-04 04:19:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e9dd8a7-b02c-3ff8-b3a6-01440035855d | -13.23969 | -48.03513 | 2025-07-04 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9950f2e-09ae-30ba-b636-943091b1f2ca | -18.65717 | -55.73439 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be882e89-9d90-33b8-8039-d0369def1c9e | -22.66791 | -47.45754 | 2025-07-04 04:19:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| cb98614a-09ad-3bb4-9e6e-55aaa7d2f23f | -18.66779 | -55.74809 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b21e2951-f94c-323d-945f-136d95c37ec0 | -19.86846 | -48.33112 | 2025-07-04 04:19:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c3c05b3-77da-3870-9d36-8b1675c9a6f2 | -12.17117 | -56.54271 | 2025-07-04 04:19:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb8b0d5-90e4-3e77-8596-54a6d9ba71e8 | -18.65409 | -55.7337 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8e9c98c7-cf72-335d-bc54-135153cfa554 | -13.43568 | -47.80986 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5d0e93c-40b6-3aa0-84c0-104d325f53ed | -19.62811 | -48.94822 | 2025-07-04 04:19:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e68157a8-4ed6-3971-a95b-36b5572716ce | -19.78441 | -47.47115 | 2025-07-04 04:19:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 679fda56-53b3-35a8-a31c-c6ad0f470ebe | -18.66561 | -55.74758 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ee4dab77-228d-3d67-9fa5-ac79fa2cf38d | -18.65643 | -55.73793 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 28b8497f-3e76-3831-9d6f-d9d45d1196f6 | -18.44745 | -54.66966 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3d3f98f-622c-3daa-b0d7-2ea70efc15b2 | -14.2411 | -43.66325 | 2025-07-04 04:19:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5548ebaa-59e3-3511-ac93-1ebb43753f07 | -20.54399 | -48.75153 | 2025-07-04 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9d235508-529a-32a9-85a0-d6faf0588f80 | -12.57775 | -56.97829 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 598f4f01-85a7-3d86-9ca4-6bf03edbd6ac | -19.44502 | -48.53842 | 2025-07-04 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71c893b7-76a3-3131-8079-5389a1670417 | -19.81486 | -54.41023 | 2025-07-04 04:19:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca6ea003-cec7-3e0a-9e20-39af70ba1fac | -13.45731 | -46.72081 | 2025-07-04 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c401415a-ed40-3ef9-ab4a-5763f13e7f0f | -18.44063 | -54.67749 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b368c98d-7169-3b99-a47d-1d2185e5c982 | -12.10997 | -54.59007 | 2025-07-04 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e491b26a-a631-3ca5-b81c-9ea5ff9ed3be | -19.92008 | -44.02754 | 2025-07-04 04:19:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ea951a0f-0c5e-32d4-b7fe-87c9956d10b8 | -18.44183 | -54.67154 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcfb20c7-28a3-3d45-8a44-d7803e38d791 | -18.66931 | -55.74104 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| df1229a2-41ca-3c7b-9a0a-8ffa4f03a454 | -13.10109 | -46.90635 | 2025-07-04 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d866582-08e6-3ebb-a4a6-c7518d889ad6 | -12.58196 | -56.99064 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b2c7b1b-c3ab-3910-aba1-2eeed9e300c8 | -19.44849 | -48.53912 | 2025-07-04 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24cb098e-3f76-3ebe-b8ed-e3fa05bfe9f2 | -18.44516 | -54.67439 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 99964481-705f-3f4b-92d1-e542b2e4dcb6 | -12.58307 | -56.98518 | 2025-07-04 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3c490c6-3917-3014-af2e-3c7c3af4c5aa | -19.81672 | -54.40919 | 2025-07-04 04:19:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5862863-847b-3d0a-b1c1-cbd98dfbfa6b | -19.1453 | -54.39561 | 2025-07-04 04:19:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f72f385d-7e6c-3b23-b100-ecbdeb079c26 | -20.37554 | -45.60189 | 2025-07-04 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6f1ac78-1567-3000-90d5-35496e95c871 | -19.90993 | -44.69069 | 2025-07-04 04:19:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68968dec-efb0-38a2-aadd-f70c758b777b | -18.44565 | -54.67858 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 821f86f3-0cf5-399a-a412-02b438c3e34c | -14.63712 | -45.12688 | 2025-07-04 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b53405-a428-35d1-98e1-7941fd2ae610 | -13.69318 | -47.74587 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12b44acb-3d6e-33e9-9045-320625f9f4b7 | -13.44129 | -47.81258 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc026eea-5726-34ff-b0d2-7487d7ab14a3 | -13.39753 | -47.83071 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef74abd8-58b2-3f3b-9a64-7d44fcfd3574 | -18.45697 | -51.24128 | 2025-07-04 04:19:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f774766-4dc4-3b96-88d2-e00c8dd858b2 | -14.888 | -48.36662 | 2025-07-04 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50e6ddba-c362-3e1b-a8b3-ef7321fa5705 | -12.11075 | -54.58617 | 2025-07-04 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e88f6126-d9eb-3b5e-a621-6aa8cbe54dc8 | -13.43771 | -47.81187 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6325b15e-e341-3c2c-bba1-fd785aea4ad5 | -21.03734 | -55.99769 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c81622be-bd0a-30d8-a714-ad0e3e5219ca | -18.44625 | -54.6756 | 2025-07-04 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5155955d-40f7-302f-a2f9-ccf3e1c678f5 | -13.40321 | -47.84095 | 2025-07-04 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 108bb3da-932b-3894-b586-92d9f50c9dc1 | -19.79596 | -46.30161 | 2025-07-04 04:19:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adebd0ed-47af-38b8-9674-bef36a89a5d6 | -18.65866 | -55.73849 | 2025-07-04 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 12d78ce1-9a72-35d2-aead-c3a2c5257bac | -18.29145 | -52.44307 | 2025-07-04 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3c5fdd9-7347-31c4-aeb6-1581b11a0522 | -13.34031 | -43.37306 | 2025-07-04 04:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6eef16df-cb5a-3730-bdf5-a531c8ee21a8 | -21.04181 | -56.00216 | 2025-07-04 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
