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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64b60d1c-9c75-39fc-81fa-e3ba005821d5 | -11.2829 | -54.4417 | 2026-09-27 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| afdcc293-a6a3-30d2-916f-c986f18d900a | -10.824 | -60.7246 | 2026-09-27 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 371f38da-f9bc-3cb6-a062-5a023f98011a | -11.0396 | -51.3079 | 2026-09-27 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| bd14015e-d2b9-32f3-950b-0ec1817d42c1 | 2.6541 | -60.1836 | 2026-09-27 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 7d452d05-924d-358b-a218-1fd10d5edcd6 | -11.0393 | -51.329 | 2026-09-27 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 58b90f40-98a0-3a3c-965a-627d2b5d14d3 | -8.0373 | -54.8926 | 2026-09-27 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c85be317-195d-3fd6-a146-258e921f0233 | -12.289 | -50.3143 | 2026-09-27 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0cb0ce31-ef36-326c-ac90-f928df1d0bf0 | -10.8052 | -60.7257 | 2026-09-27 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 936e1bd5-62cd-3386-9801-296980993f20 | 2.6359 | -60.1648 | 2026-09-27 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 39d8df67-b357-3728-88b3-76bf230dce83 | -1.6035 | -54.8341 | 2026-09-27 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 71b5e618-4930-3e2f-ae6b-15bc3e6285fc | -1.6035 | -54.8142 | 2026-09-27 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 44cbf287-cc19-3ee8-be69-2562237340fd | -12.3082 | -50.3119 | 2026-09-27 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ed70b17a-a6e7-349d-8cd0-ce7ff0a556a9 | -11.0396 | -51.3079 | 2026-09-27 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| dc24ea64-27ca-314c-bc9f-d6ebf42f78de | -10.824 | -60.7246 | 2026-09-27 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5721b41c-067d-3a45-801e-962928945b33 | -12.289 | -50.3143 | 2026-09-27 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2f803b15-acc4-3dcb-881e-d256edf180ec | -3.9228 | -43.0123 | 2026-09-27 00:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a0d88c1b-9b3b-3fec-b43b-fa3bbc917a82 | 2.6358 | -60.1839 | 2026-09-27 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a2566933-9b51-3f7d-89f6-ed0dcac009f4 | -11.2829 | -54.4417 | 2026-09-27 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6b58a246-0f70-317d-bb46-e58b3d73b435 | -8.0373 | -54.8926 | 2026-09-27 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4731bdd1-aa59-32d8-8fdd-e53e584af3ca | -11.0393 | -51.329 | 2026-09-27 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 3df30b0f-06c1-3698-83f6-6bb325ca8f19 | 2.6359 | -60.1648 | 2026-09-27 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b560264e-f7f5-3be7-a3a5-f2308ab365a6 | -6.089 | -57.614799 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b415357-fed9-3a3b-85c1-11f88e217d03 | -11.0156 | -54.036301 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3cda6b6-f7ca-3f24-8834-130354978ba8 | 2.6393 | -60.169701 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0adbd2-fc25-38a2-b465-df587208d48a | -11.8908 | -50.547199 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f75c059a-964c-3dee-866b-11cecfb48b47 | -1.6022 | -54.8279 | 2026-09-27 00:53:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc24939-059f-3c68-9dfa-4f1683dd465f | -2.2694 | -57.002499 | 2026-09-27 00:53:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0018e15a-912c-3142-93d4-fe033401e17b | -17.048201 | -56.570999 | 2026-09-27 00:53:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 345de2a5-0649-3235-9ccf-e1d18e6d680e | -6.1259 | -53.047699 | 2026-09-27 00:53:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0e67d7-3ec1-3cb7-acf2-410bc4a25d05 | -3.0679 | -58.414101 | 2026-09-27 00:53:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e873a5b-eb8b-3e8b-869b-085acbb21ef9 | 2.6411 | -60.161701 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bf535508-53f3-3199-b936-337b65ca5226 | -14.4085 | -52.790298 | 2026-09-27 00:53:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd0d614-e44d-32d3-a090-91c93eb606ed | -11.024 | -51.306801 | 2026-09-27 00:53:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2070f2a9-ed3d-3787-addb-40ee67cf6e60 | -10.8076 | -60.7216 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4a92ae0-0ee6-3d81-a47b-afbb33c5c712 | -6.0657 | -57.8251 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3e14ea6-fc5f-3660-a43a-122a50787117 | -6.6354 | -59.946301 | 2026-09-27 00:53:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad7d8f3a-8d1c-3328-ab80-4ae8387f7c72 | -2.5651 | -54.0345 | 2026-09-27 00:53:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da2f69a4-8a6d-37dc-97f4-71939a36576b | -11.2665 | -54.428699 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1675b52f-9ba2-3ff8-a781-2e043e16ece4 | -2.7878 | -57.688499 | 2026-09-27 00:53:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9860e9-9ac0-3eaa-a24f-bdfa371072d4 | -12.2888 | -50.332001 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78da5bfc-0abb-3273-a0e5-e14a2dc3718c | -11.9101 | -50.542 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec1fac6-f80e-3d43-8ceb-a5274b700788 | -11.0286 | -51.324902 | 2026-09-27 00:53:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d505bd48-90b9-398e-82d5-b6bc9c56f07a | -1.0338 | -53.567902 | 2026-09-27 00:53:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7131077-f34c-3b42-8c89-dc5ce53f7614 | -12.2504 | -50.699799 | 2026-09-27 00:53:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 738a0999-a89d-3e85-a101-a08977121200 | -3.8258 | -55.9077 | 2026-09-27 00:53:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c648245d-38ce-36d7-af37-9c5c0d7c368f | -12.2801 | -50.377499 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3203ca68-574f-3305-aad7-6f3bb92e9367 | -21.563999 | -56.732399 | 2026-09-27 00:53:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6e61130f-605b-355f-b7ab-3a19c839415e | -7.6823 | -54.757198 | 2026-09-27 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a43d0ac-795b-3715-a83a-4e6a07f5434d | -8.0259 | -54.900002 | 2026-09-27 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf6a31d-5087-3530-86a6-ca7fcf369c86 | -11.0436 | -54.192699 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94c422ad-9dd0-38eb-85eb-e0636870fc5d | 4.057 | -60.131901 | 2026-09-27 00:53:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b4c1a8e0-c157-382c-bf36-d8355a1cc2b0 | -6.0813 | -57.803902 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd0e8560-fffa-3bc0-aff4-fb3b1f50b141 | -3.8355 | -55.905499 | 2026-09-27 00:53:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9001d7b3-0eb0-3991-9a80-c215c1c99a6b | -11.8471 | -50.5378 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e9cf595-63b2-36b4-a6e3-5f4bebd6b355 | -11.9145 | -50.519501 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| defc342c-2d24-3bd1-bb3f-852995bb6c61 | -11.2693 | -54.439999 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca4e701-abd8-363b-a090-2488f0e5b641 | -11.9152 | -50.561798 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0057773b-8096-315d-b0cb-0f71862de840 | -4.5045 | -54.945202 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0184b073-11ed-3310-a016-8a71f55a8b84 | -3.2149 | -54.312599 | 2026-09-27 00:53:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e43984-b3dd-387e-8a26-474db3750b30 | -9.6128 | -55.1059 | 2026-09-27 00:53:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 071736b4-ccb2-367a-9e8f-b264dab1e8b8 | -12.2835 | -50.311798 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ddb9fc0-ebf6-30dd-b18c-300c75692963 | -10.8272 | -60.717201 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1b22386-29d2-385f-93ad-5ebc1ffa27a4 | -2.6565 | -56.451698 | 2026-09-27 00:53:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a68daee-b656-3a78-8f89-42448bf4fb9e | -11.9442 | -50.554001 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db0d5e8c-dca6-3c76-8eca-d8d0225099b3 | -10.8174 | -60.719398 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae89c2e3-f211-3cc0-bb54-c6ef59fb4242 | -9.1608 | -60.770302 | 2026-09-27 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd53a74-4d30-310e-abd7-e71d129c4176 | -5.1646 | -55.998402 | 2026-09-27 00:53:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb196b9d-c5fb-3c78-aecc-ee9549084c89 | -20.840599 | -57.709499 | 2026-09-27 00:53:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24797d7f-872e-305e-a430-4899cae8cf28 | -22.0606 | -48.769798 | 2026-09-27 00:53:00 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 309db90c-2096-3794-a30c-937f3c6a01e2 | -11.9249 | -50.5592 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8b2848-9b09-35d8-97d3-a849e682850a | -2.0549 | -56.874699 | 2026-09-27 00:53:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b80f4c3-1f22-3ebb-89c4-4ed04288da76 | -2.6573 | -56.5443 | 2026-09-27 00:53:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b51510b-9351-3a71-a575-a0a55886f957 | -17.0385 | -56.573399 | 2026-09-27 00:53:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d16ea4a-91eb-3a25-b275-b0e6494bc4a1 | -3.9567 | -50.702301 | 2026-09-27 00:53:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523db0e1-b1f2-3eda-aaa7-f66599e06ffe | -12.8947 | -61.713699 | 2026-09-27 00:53:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53f39682-2419-3b4b-a984-c27df71eb564 | -17.0403 | -56.5811 | 2026-09-27 00:53:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9ef660a-e2e0-35f8-ac03-9436d6b1ae09 | -2.2718 | -57.012901 | 2026-09-27 00:53:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a384316c-98d7-3209-be22-78d890f5ac22 | -22.051001 | -48.7728 | 2026-09-27 00:53:00 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c2d2da9-238a-3755-8628-5593dec76d2c | -6.6339 | -59.939301 | 2026-09-27 00:53:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 902f59cd-56f8-3e2c-97ae-ff356b0803db | -21.6271 | -50.065201 | 2026-09-27 00:53:00 | METOP-B | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33aa19c0-769a-313a-8249-93170f8acbb4 | -6.0618 | -57.808399 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5fafbb0-12cd-3a51-baaf-239ff79aac9d | -2.6547 | -56.533401 | 2026-09-27 00:53:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18b3bae0-f064-3950-bf2b-eefdb41c01c8 | -8.9065 | -61.4785 | 2026-09-27 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14477f73-b0e1-3fe4-ac35-d2883ee7fcf3 | -10.8045 | -60.7076 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee791d6-fbc7-3264-82e6-dc667cc86db4 | -10.8189 | -60.726398 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbe10138-2518-3bd2-833c-5009b9539900 | -6.0735 | -57.814499 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86532ce5-742e-3149-971e-60f1758a3be8 | -11.9493 | -50.5737 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f11edc83-511f-354e-ba2a-c26ec9fed980 | -11.2763 | -54.4263 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62e08ce4-d222-3f00-b439-890dd366c73d | -2.7921 | -57.7071 | 2026-09-27 00:53:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f56f6895-230f-38a8-908d-236399990de8 | -3.9631 | -50.7285 | 2026-09-27 00:53:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfa23146-6881-3f14-a5a0-b3956b06afa1 | -11.8567 | -50.535198 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30a2a591-b8f0-35f9-ade6-c46204504f29 | -5.3044 | -60.077499 | 2026-09-27 00:53:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98e5b7a8-f13e-3bae-9261-60b62051c8ef | -3.9715 | -59.342999 | 2026-09-27 00:53:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e280e7d-3b55-36ba-8e64-78260fad9e51 | -14.4117 | -52.803101 | 2026-09-27 00:53:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f795ea64-3a0d-32bb-8d16-650c6c33c56f | -11.9004 | -50.544601 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb2f5175-9c3a-37b4-9c54-4d8b3a3b541d | -9.1623 | -60.777302 | 2026-09-27 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63d99b99-e641-302d-b959-6ba1cdb48646 | -11.9396 | -50.576302 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5eee2fb5-e034-3158-a8c6-aac5bb47e2f4 | -12.0381 | -51.397499 | 2026-09-27 00:53:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b96c67f-157a-34c1-88b7-1b140cceeec3 | 2.6937 | -60.156601 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 24014d63-b0ec-3b23-8d41-6030bf188677 | -3.2185 | -54.327702 | 2026-09-27 00:53:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
