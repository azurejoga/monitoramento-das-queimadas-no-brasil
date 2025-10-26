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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22d3181c-9d97-3597-8fab-1c94bdfea2b2 | -12.85102 | -50.32371 | 2025-10-26 04:51:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3089aec5-dc32-3c45-b1c0-ab9a74ac7adb | -13.27511 | -54.39611 | 2025-10-26 04:51:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33eaa217-12e6-36e1-a732-574c1b328ad6 | -9.45162 | -56.65111 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e673265-9a33-357d-b767-c5efbcb6a946 | -13.05007 | -48.66745 | 2025-10-26 04:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f420bab2-5ea6-3fc3-a096-76cccbf33b87 | -11.61837 | -50.9922 | 2025-10-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79f25891-0c28-3f78-913e-05f4847d5485 | -9.44096 | -46.33357 | 2025-10-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fcdc324-528c-3baa-8aa6-8926959c9d79 | -10.42714 | -44.4926 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fd923505-29a1-344e-8a63-6e7770d9c1bd | -9.43705 | -46.3282 | 2025-10-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7279edaa-161a-3895-a30b-4badd98a9150 | -9.4358 | -46.33748 | 2025-10-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a51a9d32-7b99-36dc-89fa-3776855a8dd6 | -11.62287 | -54.99947 | 2025-10-26 04:51:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50f13f2e-2b04-3609-a838-b4d6a0f2a4f9 | -12.89219 | -54.72854 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6986bafc-8a6f-3b81-8fdb-9bdad702efd8 | -7.64523 | -42.16957 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e16d506-2340-3ae9-b11e-33a70a15044f | -10.41358 | -45.32382 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6b04a444-6a5e-3379-abfa-45da032452bc | -10.76465 | -44.22803 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e9c9330-4f50-36d2-a066-6802f3bbdc29 | -10.83495 | -47.63121 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bcfda3b-281d-326d-95e3-e91f2b223729 | -13.34665 | -47.41527 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20e9396d-c73c-374a-9bc6-d70f3aff2ca1 | -12.10143 | -47.27319 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ff303e9-04bc-3f53-89fa-3f8d09393764 | -11.33049 | -53.92906 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5dfdb9d-717e-3c8d-9d78-546f8396fc3e | -10.88245 | -48.03189 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9052c87-4dc5-3beb-84ed-ea292cce14c8 | -14.19755 | -48.18671 | 2025-10-26 04:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee67e3fb-c571-3468-a8af-b720c78c1854 | -10.9403 | -50.2836 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 715ee5a8-c8e8-361d-9f04-a89db29da55c | -13.20005 | -48.45106 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 025d233a-8ec0-3b01-810a-423c7fb5d8f9 | -11.00546 | -47.83359 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f09929-b191-3b95-ba1e-d9647e9bfbab | -11.47171 | -46.12302 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e28e799f-b7e8-38fa-9115-a3ef8e1375c4 | -8.79039 | -46.56416 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bddfe318-fbf8-3082-ac18-60739494fa09 | -9.94793 | -47.58183 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca430a1e-b6ea-3623-961c-758c468f8664 | -11.24707 | -49.86681 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0704989-e7ed-368e-93d3-2951fc1ab476 | -8.05166 | -46.74275 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 264b5506-2d3b-34b7-aefd-cd8b643e1d17 | -12.16908 | -46.99894 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 002d1ae2-26d3-3f86-a9fd-c0427bc65653 | -13.64304 | -47.62339 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a827fd3-7031-3e1c-8da9-3d472a746c92 | -7.61905 | -46.81434 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3f1da51-a36f-3164-8630-ba4bf8d07285 | -10.51357 | -47.67383 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 740e41e5-be4f-3e06-ba97-c03f02e070b4 | -8.18005 | -50.48318 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65b05ca5-17f7-3c04-8fc9-7192594c2642 | -8.60916 | -54.66105 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 448e43d0-f42f-3dd5-8be3-2ee7a5ad975a | -7.61521 | -45.68204 | 2025-10-26 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04e65350-094e-38c0-9baa-86d64b790c4e | -11.63603 | -54.40852 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5fcbbdd-b6c7-3770-b21f-4b1409f7abd2 | -12.99724 | -43.81171 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90ed6e35-2074-34cb-b636-7a8738dd99a2 | -8.33262 | -49.31366 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61d0a1c1-0b9f-33e2-8b0d-0b2369b60a55 | -11.54397 | -54.32421 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c807f3f-7e38-3e90-996b-9b8e7ee6e527 | -8.95986 | -47.17546 | 2025-10-26 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbc9eabd-e383-376a-9581-53f45131ed33 | -12.30474 | -47.46844 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 172f6871-e46c-37bc-8d75-5b68a5115d28 | -10.42634 | -44.4989 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c123ec78-c977-3c83-99f0-67064d682b08 | -11.10648 | -55.5572 | 2025-10-26 04:51:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59fa1747-ae2e-3b0e-aea8-028b6f9349c8 | -9.9449 | -48.59759 | 2025-10-26 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aad059a-43ee-38e0-8215-ab01570c0bf0 | -8.14503 | -47.03803 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f06f7219-b83e-3a5f-bff1-74a94c15852d | -13.40026 | -43.02218 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6d97bd88-b9ce-3dce-9ff6-374263263d69 | -10.82702 | -47.62595 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7863f519-0aa6-36a2-aee9-ba416c5d23eb | -11.24772 | -49.86231 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e382991b-de00-3c07-b523-b1a7a5eb3a72 | -12.25338 | -47.75903 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1143145-10b5-3640-91af-63c8d7a7f272 | -10.40943 | -45.31685 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 65ba137d-194c-3442-9b10-57cd710e29c5 | -11.05996 | -48.33636 | 2025-10-26 04:51:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97fbccb6-c2b1-3d97-901d-3cfe7d4f3c20 | -7.99635 | -47.92217 | 2025-10-26 04:51:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ae3b952-93aa-3408-ad1a-5022a56fefe1 | -9.63412 | -57.01588 | 2025-10-26 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca77e49-2919-38fc-acea-57e8c1debb36 | -13.9204 | -48.42372 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3fd6d6d-bf7a-363d-bbe5-24e29c59d6e6 | -11.33376 | -53.93373 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a13f7741-6953-3dd7-a21e-b0668427bbd8 | -12.9081 | -48.51542 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b2c3c1c-1acb-3bfa-9691-1b1e05a227e9 | -11.36525 | -54.3133 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 448baa4b-8ead-33a2-a7b0-4615c090900f | -11.6009 | -54.65008 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4424b6f8-79a9-383d-bae3-025b4e0ba991 | -7.69111 | -42.18435 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a8bf81a-4715-3b90-80a1-da5e3dbe98a1 | -11.6954 | -55.45819 | 2025-10-26 04:51:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aac0f80-bb42-38ba-996d-5d7cc374ac3d | -12.10776 | -52.4857 | 2025-10-26 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e8f209f-c8ca-31f2-aa54-10969aa3d588 | -11.14274 | -49.94393 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abe7cdea-9ac3-347c-b891-285b47105300 | -8.15755 | -47.75024 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59c84a23-1c5a-3d75-a438-1867c143b2f7 | -10.8208 | -47.89478 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 783be9c3-c8fa-374c-9151-3993eab7daf1 | -10.89221 | -48.02255 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1335064c-b914-37df-bb31-9c4b9069bb79 | -7.93646 | -55.01434 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21ae40d6-6d79-3a81-baca-248398dfbb62 | -10.9781 | -52.02492 | 2025-10-26 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fceb9887-f0ac-3f15-9580-16f8abdb296a | -10.81843 | -47.87098 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 533f5816-e6d4-36a7-b99d-a4a12a3ba866 | -6.5373 | -54.97453 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1daf2a2d-74f6-3509-937b-01a409e8f0ee | -8.45754 | -51.08696 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fb5f6ea-1455-33b5-b2d8-09f62074d769 | -13.90498 | -48.44334 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64f1f9b6-e46d-35c7-b3d0-791cf5fa197b | -13.05416 | -48.66809 | 2025-10-26 04:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 609aaae6-1750-3b54-a149-c7c360f96eea | -10.86021 | -47.94855 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a444e37-53fc-38f1-851f-ee2f3ca50014 | -12.89437 | -54.73619 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34fc4a57-9443-35dc-96f3-89384f7d4f67 | -14.51283 | -42.99966 | 2025-10-26 04:51:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 184d9542-ef01-3e0d-b235-59d5f8031851 | -10.33796 | -45.15472 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5cf1836-f7b9-3da5-8408-9267ff5eb56f | -14.5063 | -43.00321 | 2025-10-26 04:51:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 32.6 |
| b81519e8-60c5-3e4c-8bfe-0b0ce6279424 | -13.21357 | -48.44518 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7eb49a0a-4d54-3e5f-9a9a-958aac54636a | -10.95143 | -48.07068 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bddbdef8-f867-3dfb-ab07-78b1ce48175a | -7.7978 | -45.38629 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4367d055-3544-3bd9-a7d7-edb31d1a28d1 | -10.41429 | -45.3182 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 39d77de5-ca11-356a-9f31-a058a32d1f73 | -12.30577 | -47.46063 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47ccef83-f319-36ed-8f6c-9c24a575cb26 | -11.32994 | -53.93256 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4344b634-9c6c-34d0-82bb-8012c23551fa | -11.63271 | -54.40798 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81704418-ca33-352b-a393-49d80d299d00 | -7.85471 | -45.36931 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b30d6949-b2ad-30d3-9704-3b60e70201ff | -8.77114 | -49.61666 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba06f02-c7e5-3083-9049-a279212a53bd | -8.1535 | -47.74965 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fa5711d-672f-3220-a2e8-4a7cb0bb3a9a | -11.03125 | -47.87094 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52cc6f0e-8a2d-3db9-b419-01d0bf8a4c5f | -10.76848 | -44.50052 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65155379-60f7-36df-8cdd-231ca97c2324 | -7.93929 | -55.01867 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b704301-8e76-3b21-82f0-0c5b47773c28 | -13.32132 | -47.92957 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9d37aee-5657-319d-84a5-768157aec105 | -11.84418 | -49.86266 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35dbb7c1-27d3-3c9c-a56f-70de9523c2f9 | -7.78838 | -45.38449 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4f6524b-8a28-3ab3-904e-da01b71682a8 | -11.84044 | -49.8621 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e28f893e-e95c-3706-b48c-02407e8960fc | -7.33827 | -47.11579 | 2025-10-26 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7523b7f-0b9f-33b6-9ce8-62997b4945e3 | -11.10112 | -54.24102 | 2025-10-26 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0953155e-5523-3794-ac38-c3ce2acecfe5 | -12.83267 | -48.64723 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d58dfb10-81ea-398a-bb4a-bebd6b305035 | -13.5519 | -44.01065 | 2025-10-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6de1a0c-d8a8-3fcb-937e-9047f2d9ceac | -7.04228 | -46.74263 | 2025-10-26 04:51:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fb4b11b-44a6-3d97-896a-e734cc744164 | -9.28682 | -45.18217 | 2025-10-26 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
