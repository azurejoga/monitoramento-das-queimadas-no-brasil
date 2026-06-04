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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b935b0b7-2eca-3a7e-904f-190fa11f98f3 | -12.2136 | -57.2888 | 2026-06-04 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9c891d1b-ab6d-30d6-97f1-3a9b91354b36 | -12.2138 | -57.2688 | 2026-06-04 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c9bf1afb-9b93-32ee-b8dc-00a6db8964af | -12.2327 | -57.2672 | 2026-06-04 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5063a396-eec8-34d3-8d38-57031b99a73e | -12.2325 | -57.2872 | 2026-06-04 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 822acce1-8470-36ad-8c6e-117897bee0cf | -7.94168 | -71.46185 | 2026-06-04 06:22:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 345c2294-3426-3f34-b6c5-f41b4d428b24 | -7.94578 | -71.45849 | 2026-06-04 06:22:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47f24133-92c2-3a56-bb59-aa6831b8220f | -7.94675 | -71.45773 | 2026-06-04 06:22:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff6cfc55-d6bf-3ac6-b5e2-e93cf3ae9248 | -8.39724 | -70.48391 | 2026-06-04 06:22:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76b0efe0-37df-3439-83c9-5dea84f58627 | -12.2136 | -57.2888 | 2026-06-04 06:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5acbe134-3d99-3cb0-bd6c-a209c00b8ce4 | -12.2325 | -57.2872 | 2026-06-04 06:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 27226e57-f525-3e46-8fcb-0878628466d4 | -12.2325 | -57.2872 | 2026-06-04 06:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 24dda333-b7f5-340f-a858-a953022dba0e | -12.2138 | -57.2688 | 2026-06-04 06:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4f446547-5e8a-3485-9750-0d24dadde374 | -12.2136 | -57.2888 | 2026-06-04 06:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f60ee66c-3ebc-399a-94cf-3fe84b1e563d | -7.94197 | -71.46002 | 2026-06-04 06:42:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff6fada5-cb87-304e-9e42-e383b9da4a3a | -10.38492 | -49.44477 | 2026-06-04 06:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 304c6f60-a132-3401-892e-483644cb5a39 | -10.39413 | -49.44612 | 2026-06-04 06:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 795cb8f4-0b37-33f7-ba3e-945c740b7772 | -10.38636 | -49.43496 | 2026-06-04 06:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| fbb5b580-d6ed-3b1e-b7fa-21b582459bc9 | -12.55993 | -48.348 | 2026-06-04 06:46:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a0ea86b8-c9bc-3694-8f06-44ec6279617f | -12.21025 | -57.29533 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| dc8238ea-0316-3fda-a1af-f683588b848e | -11.78331 | -52.5083 | 2026-06-04 06:46:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5be07af1-ff50-316f-bb60-cc73f237d1e3 | -12.45889 | -58.46667 | 2026-06-04 06:46:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 6c0c9c31-fd94-3f9f-b5ae-4754ab08e808 | -12.22745 | -57.2643 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 1704a013-dc37-3c06-8aad-c9ce319e9094 | -14.08145 | -53.38831 | 2026-06-04 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 76b63cde-44e5-38e2-a3fa-4da250e512f4 | -12.20735 | -57.28475 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| cceaf2b0-6909-3fa8-8d9d-28f0125a3cc9 | -14.08291 | -53.37901 | 2026-06-04 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 01c082e4-8b4e-314a-a57c-521beea895ae | -11.53777 | -52.78428 | 2026-06-04 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 38bef944-9d06-3a07-8bd5-fe3ab3701f43 | -12.2219 | -57.27033 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 752cdd56-8fd3-306d-8c63-0eaaf18df258 | -12.30385 | -47.90081 | 2026-06-04 06:46:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ec8047ed-98c8-3027-88da-f70226a77139 | -14.06215 | -53.39475 | 2026-06-04 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d7b23cdb-87cf-3267-b3d9-af4df69b1e5f | -12.21303 | -57.2787 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 90d99f48-4454-3474-ad10-090a0933a9c2 | -12.21901 | -57.28683 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2511079e-a3dc-36e3-bdbd-627ddfc9919f | -11.54668 | -52.78565 | 2026-06-04 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| d2a6d321-7be5-3b68-8632-fc71f3272721 | -12.2247 | -57.28078 | 2026-06-04 06:46:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d59f41a7-e3d7-3652-8958-0c42eb4eb97b | -16.18111 | -58.4683 | 2026-06-04 06:46:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| f7791c8c-88f9-3fc8-ae1e-045d592f60d7 | -11.63291 | -55.18016 | 2026-06-04 06:46:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7813bd48-a320-3f5b-8ecb-dd34335c2e7c | -16.79923 | -54.16659 | 2026-06-04 06:46:00 | AQUA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0d54070f-a4cf-3185-a3cd-d8e6f1b9fd67 | -11.55559 | -52.78705 | 2026-06-04 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 07ff73f6-5350-31ef-9b6e-c973a4c4143b | -12.45919 | -58.47165 | 2026-06-04 06:46:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 61552a99-4c17-39e0-b933-e2cf9b400aa6 | -12.2136 | -57.2888 | 2026-06-04 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 47f2d394-2bc2-3628-ade7-8710eeaa16b7 | -12.2325 | -57.2872 | 2026-06-04 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 7d7dbf34-53c2-3fa9-835b-cb6a86f5e72d | -12.2325 | -57.2872 | 2026-06-04 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| ee79fe70-253b-368a-b00f-d08e86f22fed | -12.2136 | -57.2888 | 2026-06-04 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e652ab61-f925-3c08-9a69-3c04169ee52f | -12.2136 | -57.2888 | 2026-06-04 07:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 9fbabcbd-a1fb-3d4c-9dcb-eb08ebcf9321 | -12.2136 | -57.2888 | 2026-06-04 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 588765e0-f386-3ab6-b52e-ededbb09d152 | -12.2136 | -57.2888 | 2026-06-04 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 03c4188f-f7c2-3ef6-a04f-3591d711688e | -12.2136 | -57.2888 | 2026-06-04 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a2f4764a-8a61-38e2-b039-ad78c4392898 | -15.3047 | -41.8955 | 2026-06-04 09:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 189.8 |
| 864830b9-5075-3c84-a2f1-df5acbb17cea | -15.3244 | -41.8911 | 2026-06-04 09:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 244.3 |
| e4ea3f65-1072-3d4c-bd41-e85494399919 | -15.3244 | -41.8911 | 2026-06-04 10:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 225.9 |
| 2dd968b3-0c1d-3ec1-9a12-70ecc7d516b0 | -3.99277 | -47.92284 | 2026-06-04 12:12:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bae7ed09-0955-360f-b14c-a433e3722138 | -6.9892 | -42.87865 | 2026-06-04 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 1a267d2f-9b53-3938-ab8e-ff0452e410f7 | -6.7683 | -45.01175 | 2026-06-04 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| e1954e15-483d-31f4-8a47-250d4e204c07 | -6.75529 | -45.00999 | 2026-06-04 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cb6d05e9-9e68-3659-9af9-e97fc2e4cff0 | -7.00078 | -50.47057 | 2026-06-04 12:12:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f1c3e603-953f-3f43-a8f8-07db6d621227 | -6.39858 | -44.83597 | 2026-06-04 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 59b8c9f4-e8c9-3080-aedc-9fe9c01e8e4a | -6.99368 | -42.87223 | 2026-06-04 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| a37f0d83-e1c9-3793-92aa-f0fe64cb48db | -3.99122 | -47.93401 | 2026-06-04 12:12:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 2e62d4b3-ec00-3c23-818a-df2b41b41164 | -5.11602 | -46.94803 | 2026-06-04 12:12:00 | TERRA_M-T | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| f02cb53f-ff36-32c4-a0c0-5acad803a27a | -5.11419 | -46.96175 | 2026-06-04 12:12:00 | TERRA_M-T | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 593d4ebd-b148-34d5-bc45-cbacefbb9aa5 | -11.61349 | -52.55236 | 2026-06-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88f22d80-6699-38c1-a91b-dd0dc271085a | -10.76909 | -54.09941 | 2026-06-04 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e3901a9e-6fb6-3fa9-878c-1fb4cc262ae2 | -12.46193 | -58.47349 | 2026-06-04 12:14:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 28.3 |
| fa45aedc-a357-3c21-8b5c-1b7fd444b3c5 | -11.63214 | -55.17916 | 2026-06-04 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 46d3aa7c-4537-38a6-85c6-48f735089365 | -10.98087 | -47.05812 | 2026-06-04 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 74d99961-51c3-322e-8e76-84c505adcb82 | -8.40545 | -46.88253 | 2026-06-04 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9aae2416-9696-3551-a30c-e5bb26142b4a | -11.73656 | -54.23486 | 2026-06-04 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 55ced458-df4c-3551-baac-2ce12095029a | -13.96291 | -53.84649 | 2026-06-04 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11bdbf75-57cb-3c92-8fa9-e14792a054ee | -12.65697 | -47.66351 | 2026-06-04 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7202a359-c7d6-314b-97f6-2bf32cf4958e | -11.67584 | -56.76314 | 2026-06-04 12:14:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b3f82699-4387-329b-9c21-20646ca2523c | -14.08662 | -53.37996 | 2026-06-04 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c99fbb00-a4cc-33af-b164-9c4d27b1c62d | -11.73513 | -54.24442 | 2026-06-04 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c1843cc5-ad4b-39b9-bd27-8a2f125a8b32 | -12.23036 | -57.27409 | 2026-06-04 12:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 402b316c-84ec-3025-a4f7-ad751fb7e2a7 | -10.5729 | -57.32605 | 2026-06-04 12:14:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 38d4d56f-f82a-3993-935a-92c40f8d17e6 | -12.73795 | -54.20582 | 2026-06-04 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e7fbb2f-c089-34a0-a187-323dec5a3133 | -10.85807 | -53.74635 | 2026-06-04 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7562d0c0-94fa-3cef-80c2-b8e78651abe1 | -16.84304 | -53.82997 | 2026-06-04 12:14:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b32c5560-af52-3640-b45a-d77cff2319cf | -11.54995 | -52.79197 | 2026-06-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b3202b8-c972-30b8-9e59-a8b869aa4ff0 | -11.62262 | -55.1777 | 2026-06-04 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 89924dc2-698c-32f8-ab6f-14f1f5d1ed0f | -11.59995 | -55.32655 | 2026-06-04 12:14:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a9233c3c-c66e-3012-8777-4fd048070d6e | -11.78381 | -52.5098 | 2026-06-04 12:14:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d3351ea-e7a2-3d7c-9008-32a029fcaa84 | -11.33375 | -51.3918 | 2026-06-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b4bcedb3-f636-3e23-b016-f4355b6499e4 | -8.4922 | -51.53233 | 2026-06-04 12:14:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 8d50fd96-4dc7-3630-a3aa-9b267f77257e | -11.32477 | -51.39055 | 2026-06-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 09425a85-f2fd-33df-ab24-5933930e6bb9 | -10.39176 | -49.43793 | 2026-06-04 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3807fcac-3995-3e7b-ad2b-3c86cae31f54 | -11.63054 | -55.18969 | 2026-06-04 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d3ad340d-df50-3fc3-bf08-946152987432 | -8.40328 | -46.88783 | 2026-06-04 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 15e968ee-ae1f-3b82-b98a-e18d964c2511 | -7.7641 | -47.5903 | 2026-06-04 12:14:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a77b5f92-0bff-3808-b89c-03124a8645be | -11.32605 | -51.38127 | 2026-06-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a1ae108-20c1-3b01-945f-41f11c6255f4 | -12.6685 | -47.66497 | 2026-06-04 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e05a1e3e-0c89-38a3-88c2-72d314670f9d | -11.62102 | -55.18823 | 2026-06-04 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 11393df8-c938-3817-8569-4d315a6717c0 | -14.08532 | -53.389 | 2026-06-04 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| bd7c42db-73e1-35de-a260-730d6785e24b | -8.39402 | -46.88077 | 2026-06-04 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 644382f8-c9de-3ae3-b7d9-33b6fee5d59b | -12.66363 | -51.43468 | 2026-06-04 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ac649679-90fb-3708-acae-fdf89c81a438 | -11.59831 | -55.33728 | 2026-06-04 12:14:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8f022edb-41c5-3865-8579-d1a7413b8c08 | -11.55124 | -52.78303 | 2026-06-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 28cacd26-fd9a-3b6a-a060-bd1f1beb07c0 | -11.73393 | -54.80089 | 2026-06-04 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7a65ef2e-5dbf-3af2-b6a5-5bdbbbfb0505 | -11.26024 | -53.96179 | 2026-06-04 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee660b05-61d0-3552-ac46-ceff8114e2a4 | -10.57529 | -57.31086 | 2026-06-04 12:14:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b0e5143e-4ade-3d84-9da1-fcc71c98237d | -10.59379 | -53.472 | 2026-06-04 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eac70607-9e7e-33b0-a0a6-54a7efb2427c | -15.40937 | -51.0571 | 2026-06-04 12:14:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |


[Clique aqui para ver as próximas entradas](README18.md)
