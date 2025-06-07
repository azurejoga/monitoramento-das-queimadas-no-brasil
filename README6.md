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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e60fbf3-65b1-36db-a50e-2b65b112ef5a | -7.7361 | -44.1823 | 2025-06-07 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| d00b1cba-d942-39cc-8680-49bd24429cd1 | -6.204 | -43.3241 | 2025-06-07 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ee8b3ab4-bd1c-3197-b087-05e3087398f2 | -7.7176 | -44.1611 | 2025-06-07 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| eda1a635-20ad-38ca-9a2b-940857e4909a | -6.96 | -42.9288 | 2025-06-07 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 8a45b2f3-5be0-3adf-ad6d-80f91f634d28 | -7.7173 | -44.1842 | 2025-06-07 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a3c3c26c-e19b-3c61-8674-70a64417eca9 | -5.6379 | -43.7175 | 2025-06-07 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 9c70f327-eefc-3cf8-ab7f-27524ff1c6e4 | -13.4733 | -56.8557 | 2025-06-07 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| bb7f3ad4-aeec-3dad-b7c5-b5ecfa357c3e | -17.2639 | -42.6527 | 2025-06-07 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 8c851f78-b304-375c-98c4-1357624a9f9f | -6.9414 | -42.907 | 2025-06-07 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 5e6eb459-5b07-3f95-9e09-e8741b00eb3a | -7.7176 | -44.1611 | 2025-06-07 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 07b7b16c-3e0b-353c-ad09-e044da74a8c1 | -7.7173 | -44.1842 | 2025-06-07 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a445a4eb-6a1b-3d37-9907-0419ba0736c6 | -7.7364 | -44.1592 | 2025-06-07 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 16730553-0d28-35d1-90c2-a3dfbd729a8a | -6.9602 | -42.9052 | 2025-06-07 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| c469a6bb-67bf-32d1-9ab0-189d13e9fb4a | -5.6567 | -43.7161 | 2025-06-07 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f2e56392-ece7-348a-91d8-a64b99064f50 | -11.2548 | -60.7957 | 2025-06-07 02:10:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| fb70bdfc-f57a-3c5e-9127-b47480575544 | -5.6379 | -43.7175 | 2025-06-07 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 666e3fce-df55-31b3-b836-25723e880b89 | -12.5238 | -58.3378 | 2025-06-07 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| e30b401a-09c5-338e-b3a0-17210171ca43 | -7.7361 | -44.1823 | 2025-06-07 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 5b7cc81c-21bd-3120-902e-0f1ee076974e | -12.5236 | -58.3576 | 2025-06-07 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 186f97cc-ab16-3344-8c88-4998cc0b1cff | -11.7826 | -47.402 | 2025-06-07 02:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 81fd3f9f-b104-3763-802e-b093fbafc632 | -7.7361 | -44.1823 | 2025-06-07 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| e2733d7b-d7d3-31f0-bad1-50695ebe1aad | -5.6379 | -43.7175 | 2025-06-07 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| da48fb9b-ddd1-35ef-8787-22b9e3974b98 | -7.7364 | -44.1592 | 2025-06-07 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 161c4c79-fd9a-3279-8ead-18456a4d9658 | -7.7173 | -44.1842 | 2025-06-07 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1dfe45bf-478a-3cbc-8caf-08bdc3bd7cc1 | -12.5238 | -58.3378 | 2025-06-07 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a5b33019-13dd-3cd4-b938-03ff841f5887 | -12.5236 | -58.3576 | 2025-06-07 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f3e457e0-b84b-35db-b888-676880108192 | -6.9602 | -42.9052 | 2025-06-07 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.0 |
| 06c84485-05bd-36ae-9b8b-cb533d6b914f | -7.0169 | -44.5954 | 2025-06-07 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7fa5ca0e-50e0-395c-bf38-478b114b6a94 | -7.7176 | -44.1611 | 2025-06-07 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| ae7e07a4-58dd-3d69-9ce4-7bb43019f21c | -11.2548 | -60.7957 | 2025-06-07 02:20:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6002d471-69be-3c55-846e-1d7f5dfa2994 | -7.0169 | -44.5954 | 2025-06-07 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6eed0119-af28-3474-b3df-83f2b28a7499 | -6.9602 | -42.9052 | 2025-06-07 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 33859a0f-b747-3a85-8f17-6ce7cab93dfe | -12.5236 | -58.3576 | 2025-06-07 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 6268a8b9-d0e5-36c2-835b-d1a962516fbf | -7.7176 | -44.1611 | 2025-06-07 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 74a2e4a9-b39c-3a53-8b93-6e5119c07ca7 | -7.7364 | -44.1592 | 2025-06-07 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 250cd740-8b05-383e-82dd-376d7dda90df | -7.7173 | -44.1842 | 2025-06-07 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 380eafbb-9b9a-384e-83e4-1ceee37a39ff | -6.204 | -43.3241 | 2025-06-07 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f1208af0-490b-3955-8bad-f03288c5b31e | -6.96 | -42.9288 | 2025-06-07 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| adfd5570-d880-330b-aea5-07ad646841f7 | -11.7826 | -47.402 | 2025-06-07 02:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1e1291e4-3c74-3785-9c03-b91c37e082c6 | -7.7361 | -44.1823 | 2025-06-07 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c642c5ce-75f9-3a3f-b16b-458910179dec | -11.2548 | -60.7957 | 2025-06-07 02:40:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d9b6f536-2a9b-3917-a58b-40aeb9444664 | -7.7364 | -44.1592 | 2025-06-07 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 95ce486e-41ea-3297-b6eb-ced5e9021a9e | -12.5236 | -58.3576 | 2025-06-07 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 65d58f18-3d07-3fb7-91e1-5f761b1fcc23 | -6.96 | -42.9288 | 2025-06-07 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 60ebf742-e952-3ae8-8082-d3d2a55389cb | -7.7176 | -44.1611 | 2025-06-07 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 99e08ac9-1669-364c-80de-3754b9a0c21b | -11.7826 | -47.402 | 2025-06-07 02:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 9c247e78-65e0-3de5-9c58-a7d5e4b3e0b0 | -12.5238 | -58.3378 | 2025-06-07 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| ff463f56-bf68-3c7f-ae48-3fb124ae6957 | -7.7173 | -44.1842 | 2025-06-07 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9d358eb7-07e5-388d-a93a-f73d0e27e933 | -5.6379 | -43.7175 | 2025-06-07 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a4d53b94-7b01-38da-8bac-25e6602cff44 | -7.7361 | -44.1823 | 2025-06-07 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 2b50f0cb-f66c-3a98-bc0a-b3cb2c3a0e9e | -6.9602 | -42.9052 | 2025-06-07 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 5583f72f-4836-39c8-8018-75e05f4b4566 | -5.6379 | -43.7175 | 2025-06-07 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| adb4ebba-20f4-337a-979b-19fc286eb0af | -7.7364 | -44.1592 | 2025-06-07 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8bac3e97-04ad-3637-b2b3-292e92b640dd | -11.7826 | -47.402 | 2025-06-07 02:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2f4a6e3f-ec33-33b1-9037-7944003f7c39 | -12.5238 | -58.3378 | 2025-06-07 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| d7c67b98-fb1b-380b-8ce4-fe57464c0a0e | -11.2548 | -60.7957 | 2025-06-07 02:50:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4786504e-f38a-3c42-892d-ed3147ee318a | -7.7361 | -44.1823 | 2025-06-07 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ca95cd5a-8ac6-3038-b61e-1bce2efbed5c | -7.7176 | -44.1611 | 2025-06-07 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| b981d844-9be0-3cd5-8c8d-e422f69fb5f8 | -6.9602 | -42.9052 | 2025-06-07 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 161.1 |
| c271a324-4af1-3a48-9508-66677b54c23a | -7.7173 | -44.1842 | 2025-06-07 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ec61f092-76e5-39ed-954d-9b2b6d385d12 | -12.5236 | -58.3576 | 2025-06-07 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 650ad4d4-4413-35f4-88b4-4cfab2091985 | -7.7364 | -44.1592 | 2025-06-07 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e1f9b382-4ff1-3b67-ba70-2585a07b65d8 | -7.7173 | -44.1842 | 2025-06-07 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| eb8ab8da-86b9-3450-bbaf-7792f5e8bd36 | -7.7361 | -44.1823 | 2025-06-07 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 3b401d03-c0e6-33cb-a597-9c9c89a4b6f8 | -6.9602 | -42.9052 | 2025-06-07 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 157.2 |
| e7039679-f209-3d3c-843a-5a2bd1bbfc51 | -7.7176 | -44.1611 | 2025-06-07 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 38ae4c0b-bf37-30ea-b9a2-2c75f3f92cd6 | -11.7826 | -47.402 | 2025-06-07 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| eee17960-7a27-3bc8-a2b4-3be94e9593a3 | -9.4964 | -40.3088 | 2025-06-07 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 49.8 |
| 68f432b9-4d3b-3b74-b0a7-ef2ec2f6c44f | -9.49692 | -40.308 | 2025-06-07 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e5f60729-3a7c-3e55-a7ac-6f50c398ca7f | -9.49549 | -40.31512 | 2025-06-07 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e36eee82-af43-3552-8bbf-ae2bbaf1b7ef | -9.48842 | -40.3137 | 2025-06-07 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4cf0bfc0-cdbb-30bd-bd40-c0c4d4eb02be | -7.7361 | -44.1823 | 2025-06-07 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a4e87c38-8531-3324-bd4f-576e05c612f3 | -6.96 | -42.9288 | 2025-06-07 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| c189b0f6-8bd0-3214-b417-03f3f89cee49 | -7.7364 | -44.1592 | 2025-06-07 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 4aaf826f-97b2-3457-87f8-ac7af205a9ee | -7.7176 | -44.1611 | 2025-06-07 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 17b7bdcd-f57f-398a-b5f8-98a1957654f2 | -7.7173 | -44.1842 | 2025-06-07 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ed1d1e6f-4374-311e-9cd0-f29ea330c2b3 | -12.5236 | -58.3576 | 2025-06-07 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 48e6c2df-12ab-348b-bc61-90ebb269b808 | -6.9602 | -42.9052 | 2025-06-07 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.8 |
| fd0aa112-0860-3a92-be5b-7b4b46b05f2a | -7.7176 | -44.1611 | 2025-06-07 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0128219d-06c5-3334-bcd2-ae22332481d0 | -7.7364 | -44.1592 | 2025-06-07 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 0bbc7f1b-412e-321d-9e8d-9c3e4d3c3f14 | -7.7361 | -44.1823 | 2025-06-07 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 04db72ad-b657-3a0c-bce5-ae396e821b32 | -6.9602 | -42.9052 | 2025-06-07 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| ee18c2f3-d18c-3d42-8b3f-300a1ddb58d3 | -7.7364 | -44.1592 | 2025-06-07 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 8f82fa61-44c8-3def-8678-91b19fc5bab0 | -7.7361 | -44.1823 | 2025-06-07 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f4f54695-db99-331c-bda1-acfde02097e6 | -5.6379 | -43.7175 | 2025-06-07 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 01a17d69-2c6d-30b3-bba3-895207178e27 | -6.9602 | -42.9052 | 2025-06-07 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 5ff01e0b-23e8-354d-857e-b68f40ef4ca3 | -7.7176 | -44.1611 | 2025-06-07 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| abd842e8-7691-3188-b7df-c7e81e816d47 | -7.7364 | -44.1592 | 2025-06-07 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b5216200-f64c-3537-8c96-65f3c7d1b756 | -6.9602 | -42.9052 | 2025-06-07 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| c24fbc6f-7d85-3214-85e6-917bae37d280 | -5.6379 | -43.7175 | 2025-06-07 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 633a3a62-7154-32ea-b48a-e4b290ee00f3 | -7.7176 | -44.1611 | 2025-06-07 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 413655e4-2eee-3d2f-88b5-28cf4c2d24e8 | -5.6567 | -43.7161 | 2025-06-07 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| db604776-cfc1-385b-a6d9-0214dfac3a12 | -7.7361 | -44.1823 | 2025-06-07 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 90e045dc-500c-3988-b4df-d9b5753ff562 | -5.6379 | -43.7175 | 2025-06-07 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e339b17e-1a97-308c-9994-db06b41ddbd0 | -7.7364 | -44.1592 | 2025-06-07 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 11c7fb25-e09d-3f1d-bfea-cb272a21445b | -5.6567 | -43.7161 | 2025-06-07 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 00a389c3-968e-3caf-8779-591f6623156b | -7.7361 | -44.1823 | 2025-06-07 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 5462bf4f-97da-3eaa-9086-c9e88fc8ef69 | -7.7176 | -44.1611 | 2025-06-07 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 2addc15f-a7bb-3661-a974-124f81a68ee1 | -5.78341 | -43.61989 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f59c728-b7e3-3068-9271-b9909ced83a1 | -6.21442 | -44.5074 | 2025-06-07 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README7.md)
