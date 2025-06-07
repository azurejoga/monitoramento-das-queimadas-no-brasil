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
| c4853b94-f493-364b-afa5-c7e6f1e74e82 | -14.73731 | -45.08981 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d93a1c7-5eda-3b61-bbe6-60af93f3968d | -14.33858 | -47.58931 | 2025-06-07 04:23:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 067628e5-7015-35dd-b507-846f61c92041 | -18.23864 | -47.94036 | 2025-06-07 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 680c5dd6-9e42-326c-9927-f2ebdfdb2989 | -16.71493 | -47.91354 | 2025-06-07 04:23:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d9f25a2-d83f-3b38-97e3-779b949fbcab | -12.28245 | -57.27104 | 2025-06-07 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c56194-6563-395a-ae56-9c50da99145e | -12.96486 | -46.76711 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13d9337e-37b6-322f-b675-ad7584988dce | -14.23726 | -45.48732 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db0d658e-ea8e-3083-91d7-10d691ebc25e | -13.66306 | -47.70475 | 2025-06-07 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dff3d859-4db1-3746-b25e-75060e336257 | -12.71134 | -58.02686 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3a0c5e0-5d0d-3f47-ab8d-f2cb747de42f | -14.20087 | -45.50008 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3156611c-ec96-31c1-a218-279de092c9a9 | -17.26453 | -42.65892 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08f511de-8317-391e-b6b0-29e5d042b3cf | -14.2199 | -45.48824 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e3e5942-0e60-3359-bc55-e1cbe80ad60b | -14.73164 | -45.08124 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2cf426e-8f9a-3fb8-97b8-d0ccbeb51f02 | -17.26062 | -42.65831 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3d9b69e7-cfb0-3920-8bd7-06c1db8fb0e1 | -12.28037 | -49.5323 | 2025-06-07 04:23:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54eae245-1a57-36f9-ba0b-7909b3d9e399 | -12.88568 | -52.20689 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce515929-3885-3198-ba38-8a3b6994de3f | -14.82054 | -40.78009 | 2025-06-07 04:23:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d4f3e5b8-bdaf-36fb-8073-5a0dfb370b3c | -18.23922 | -47.93671 | 2025-06-07 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bdb3167-8bd2-3be9-a9ee-2ac482bdddc6 | -14.2143 | -45.47989 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c86c9408-4d19-3ee0-87a7-6d5c30757227 | -11.54092 | -56.44943 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ede9357f-8878-3d2b-a661-2de59995c459 | -14.73447 | -45.08553 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aa7c52a-b12b-3b6f-83b1-10173006edc3 | -16.00156 | -49.71646 | 2025-06-07 04:23:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1c8506d-33b0-3e09-9c76-bafd2bc68764 | -12.88142 | -52.20608 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afa124fc-2835-3fba-b5f7-389b434e3bee | -15.16882 | -45.64185 | 2025-06-07 04:23:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1777396b-8be6-3373-9cec-0a8e86fffe2a | -12.6999 | -58.24187 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d991ce67-85de-335c-a586-b56ab1aabd00 | -10.69489 | -57.6459 | 2025-06-07 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cecb5929-9b6d-31b6-b34e-072ea2c6e588 | -12.28013 | -50.10177 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e69e324-66bb-3bef-aa78-4eaa19545ef7 | -12.53175 | -58.3465 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| abbef693-f3a2-39fe-927c-8178ef09a727 | -14.72766 | -45.08448 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f5a2187-442f-3a8a-b827-68ee4b049063 | -13.06491 | -49.2435 | 2025-06-07 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 098130cb-a0f5-3eab-b30c-188d434fe5a8 | -14.03969 | -55.13648 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ea9f64-32b7-34ce-8cd5-08c263a1945d | -14.74354 | -45.0946 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16ec0e29-cb91-376e-9b8b-9183925904ea | -13.65969 | -47.70414 | 2025-06-07 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b107a6db-bd27-3070-a363-9c7bf1f1fb44 | -11.37096 | -56.55441 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0c4f9499-59ab-39e2-977f-7b7fe6b8983d | -11.56698 | -54.56952 | 2025-06-07 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72d11aaf-b4ff-3475-bacf-f6c588812e7b | -14.92648 | -46.01233 | 2025-06-07 04:23:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cfbb087-20a1-31a9-86a7-6c34f4eb17b4 | -13.06849 | -49.24416 | 2025-06-07 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4200086d-fc70-333b-9894-0a896ff88d74 | -12.33137 | -52.48138 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20b05621-6109-3ac3-b95d-4956d3375075 | -12.70265 | -58.2412 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d45d9124-5bc8-3ee3-bad9-8e96128cdbcd | -13.07137 | -49.24895 | 2025-06-07 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97658b51-b604-3d48-ab3e-2b6e157d817a | -21.19646 | -44.93867 | 2025-06-07 04:25:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3a28360-22dc-3bb9-8a03-130e41eeca1a | -20.92435 | -49.09659 | 2025-06-07 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 19ba63f6-0a12-3aad-b045-63ca6c19e5dc | -20.99772 | -51.79242 | 2025-06-07 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f30e04bf-0d3c-3359-989a-b8dd3689fd2a | -20.92499 | -49.05024 | 2025-06-07 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c3f13b8e-715b-390b-a6e5-a747fd9acb56 | -18.40682 | -54.57507 | 2025-06-07 04:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83585789-05d0-3cf1-ba9f-4b733da617cb | -19.07944 | -53.46513 | 2025-06-07 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e07cf351-b811-390a-a5e5-9585a732367f | -19.05038 | -53.45922 | 2025-06-07 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 972d2f39-8674-33cc-9730-fe7c32314da6 | -19.93257 | -47.26519 | 2025-06-07 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccf47670-99ef-3015-9089-0d5623469fd1 | -20.76542 | -46.77066 | 2025-06-07 04:25:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f4c3fdc7-d613-36ec-90cf-592fbf6af66c | -21.47943 | -56.61367 | 2025-06-07 04:25:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5525aa98-572b-34ac-9810-d200cf8fc87c | -21.61384 | -54.3316 | 2025-06-07 04:25:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f48686c-19e0-37a9-baf5-d39aae398dd1 | -23.33832 | -46.77173 | 2025-06-07 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 647a5e19-9144-3a81-984b-8af580082d86 | -20.76541 | -46.76782 | 2025-06-07 04:25:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4232c482-776d-35c2-bf90-2dc063fd2fd1 | -20.9256 | -49.04649 | 2025-06-07 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 89de6ed1-7d7b-3270-891b-c36c453cc248 | -20.921 | -49.09596 | 2025-06-07 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b86cc563-cc3a-37d4-a3e6-5cd7fb3807e9 | -19.07528 | -53.46433 | 2025-06-07 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c180c154-8ee4-3511-adef-4cc5be7cf079 | -19.61486 | -46.25902 | 2025-06-07 04:25:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e39ccd3-1adf-3ed0-b251-955105d2f9f5 | -20.93989 | -56.59592 | 2025-06-07 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30ebb978-84da-3e1b-a8d8-1c72bb291986 | -23.40597 | -46.55793 | 2025-06-07 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b9b8ea28-18d9-3cf4-8caa-2106a0667519 | -20.73129 | -56.65542 | 2025-06-07 04:25:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27d60cbe-bf3c-3653-a8c1-ce04581939df | -20.92496 | -49.09282 | 2025-06-07 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 972a07f6-b3d4-3479-a970-7f52046f54fc | -23.3889 | -46.4722 | 2025-06-07 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a22cbacc-e8ad-3f58-9721-7bff5380fbe6 | -19.07869 | -53.46915 | 2025-06-07 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1540e5c3-2167-3a00-908c-546f42712c89 | -21.35574 | -44.75224 | 2025-06-07 04:25:00 | NPP-375D | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b829aa3-29f1-3791-8b09-c7cafc1bb63d | -27.45581 | -48.45365 | 2025-06-07 04:27:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7d847c74-747a-31d3-a544-0440c4d3a54e | -7.7173 | -44.1842 | 2025-06-07 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9d42bef2-97df-3896-92cb-c47957b30ba8 | -6.9602 | -42.9052 | 2025-06-07 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 3b24d192-5944-38ea-b930-68e7f4fe0ece | -5.6379 | -43.7175 | 2025-06-07 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b39a2c95-80f2-330f-912b-2405a3ef2a0f | -7.7364 | -44.1592 | 2025-06-07 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 36735ad8-12cf-3037-a24a-e4fae34e461b | -7.7361 | -44.1823 | 2025-06-07 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2241231a-77e8-35fb-8669-460020b490da | -7.7176 | -44.1611 | 2025-06-07 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9707616f-50d0-3941-811c-1a49fadb3216 | -7.7364 | -44.1592 | 2025-06-07 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f1835839-c244-30e4-b8c4-b59b4f09793d | -6.9602 | -42.9052 | 2025-06-07 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.3 |
| 965cfdf5-49b1-3ac4-92ea-ea6820cc38b5 | -7.7176 | -44.1611 | 2025-06-07 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9e47d6f9-66d4-3958-ba41-7d0098fe8389 | -7.7361 | -44.1823 | 2025-06-07 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| df3ce6fe-eef1-386d-985e-c8ffd3066963 | -4.66952 | -41.96179 | 2025-06-07 04:42:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b938e79f-7884-3492-acf0-c1aca0534580 | -4.66818 | -41.96083 | 2025-06-07 04:42:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4ab09043-97d8-3beb-bcf2-16294eb6493d | -1.0724 | -50.72898 | 2025-06-07 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 202cb117-7010-3153-a4f2-c3fd1cd468b8 | -2.44404 | -47.47426 | 2025-06-07 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67edf526-3137-354f-88a3-ee80b07fb33e | -0.948 | -51.38217 | 2025-06-07 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69ffe922-6472-3f6c-a920-a2db192d2d47 | -4.66436 | -41.96096 | 2025-06-07 04:42:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c079041a-e6a3-3dd1-86db-7c57f9939060 | -2.44344 | -47.47817 | 2025-06-07 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 139fd743-0f19-3aee-86da-d4b53816dd86 | -4.66997 | -41.95867 | 2025-06-07 04:42:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe6f48c9-3980-349b-9e09-0f2ce94facb9 | -2.91841 | -48.23542 | 2025-06-07 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53ebd78a-39e2-38b6-a400-10b41d8b2fc6 | -9.0708 | -47.14104 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92291d47-dc22-3221-a713-393fbc8ba375 | -6.96293 | -42.90016 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9a0df2d1-12c7-34ab-88ff-0a180ac9c292 | -9.50142 | -40.37394 | 2025-06-07 04:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 81f25b0d-96f3-3b18-8928-52863b7495ac | -5.64999 | -43.70742 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec4286c0-97f6-3e35-823a-05f29797ce3d | -6.23613 | -48.54469 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f2fc4cf-74c8-3b6b-8f15-6ab934bd71a4 | -8.72447 | -47.98693 | 2025-06-07 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 291ab0c9-d8fe-30af-858b-9597dedf4ba7 | -6.95211 | -42.90433 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b2636ff9-8f47-3cae-b247-82c117f58d87 | -9.07858 | -47.14216 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6b3344f-f3a2-3d53-ae4c-7f746ba4eb97 | -6.29405 | -48.50058 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c5b438-4c3a-3aaf-b597-1143db272880 | -11.81994 | -44.26634 | 2025-06-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 43fadbee-70dd-3921-aff1-826cddc5669d | -7.73509 | -44.17102 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9927a620-1df4-36f3-b41e-d50cf9a66b2f | -8.4561 | -46.49434 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a874ece9-9456-3746-81e9-e8eaacfa400e | -10.64455 | -44.48854 | 2025-06-07 04:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a03c10a9-6756-3440-a0a7-c4d1b781c00a | -10.23374 | -52.237 | 2025-06-07 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b25e1a41-70cd-3c1f-b4ed-8241bb9e004e | -3.88193 | -54.21316 | 2025-06-07 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3264032-ce06-3baa-8d20-74a4045a3021 | -9.50201 | -40.36925 | 2025-06-07 04:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |


[Clique aqui para ver as próximas entradas](README18.md)
