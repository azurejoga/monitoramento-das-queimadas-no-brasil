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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de0c70e1-903b-355b-844a-95a64a27d3fb | -4.2729 | -43.737 | 2024-10-07 04:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 331a2316-7e00-317b-9637-1885b0e25544 | -4.2731 | -43.7139 | 2024-10-07 04:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| de3d85c5-fdea-3d64-a52a-3945daf05c24 | -10.8755 | -63.8979 | 2024-10-07 04:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b3376930-5099-3538-a6b5-013d7c570c82 | -11.304 | -51.3646 | 2024-10-07 04:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| cea51179-7a8f-33f9-8f1b-74a72b77ca17 | -11.285 | -51.3666 | 2024-10-07 04:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 651536bd-646c-3b28-8b75-cd4e6d917a71 | -11.7566 | -44.4897 | 2024-10-07 04:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 27e10b62-a4ed-3ef7-aea5-3e6f4b0744e4 | -14.0703 | -45.4611 | 2024-10-07 04:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 073efd2f-e3b1-343f-9ed4-0549e6b9e0f9 | -14.0898 | -45.4577 | 2024-10-07 04:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 50a984db-c074-3855-8bf4-5ab0a86043bb | -14.1273 | -45.5207 | 2024-10-07 04:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c8fa8add-8336-399d-bab5-49fe0fd144f5 | -16.5075 | -57.7183 | 2024-10-07 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| b2b02f0e-d5e1-363e-b2a3-787f8c8b402b | -16.5072 | -57.7387 | 2024-10-07 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 9ffe790e-a2f0-3851-bea0-bdccc7661738 | -16.5267 | -57.7365 | 2024-10-07 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| b8d3dd9b-aa8f-3f50-a063-10a8e3b3e156 | -16.527 | -57.7161 | 2024-10-07 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 9a00aca4-e799-34d8-b2ae-5aa3f03186f0 | -16.5749 | -57.1395 | 2024-10-07 04:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| fd84d9d0-c7de-3533-85bf-627e3db8d153 | -16.5944 | -57.1373 | 2024-10-07 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| e05e5aaa-bf6f-3362-abe3-e0018a6081cd | -16.614 | -57.135 | 2024-10-07 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 4f27f850-3bd2-3726-adf5-5fa6c0b5d56c | -16.6332 | -57.1533 | 2024-10-07 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 3875f365-9abc-3434-a206-ebde28ff7a49 | -16.6335 | -57.1328 | 2024-10-07 04:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| bc47a5e7-49b5-3b3a-b5e4-ccc2d96ca09c | -17.1433 | -51.7206 | 2024-10-07 04:26:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 58b0075c-38b3-3898-9938-c94e976e4dfa | -17.1437 | -51.6989 | 2024-10-07 04:26:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 69c7b3dd-46aa-38b3-8fd8-447e4ead0f52 | -16.9717 | -56.7646 | 2024-10-07 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 34b28629-9fe9-3126-bea0-79b97ec37bda | -17.012 | -56.698 | 2024-10-07 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 174d7f38-a403-36d9-b61d-bc81087056e5 | -17.0123 | -56.6773 | 2024-10-07 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.0 |
| b542b0d6-17b2-320c-8596-2b7bf42d6c2b | -17.0319 | -56.6749 | 2024-10-07 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 4b2c8051-c8aa-3706-b044-bd955a39639c | -17.1581 | -57.3582 | 2024-10-07 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| b4a338d7-6433-322e-9451-01e017a25c34 | -17.1584 | -57.3377 | 2024-10-07 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| c25aaf80-4576-325b-9dad-bfc9672e29c8 | -17.1777 | -57.3559 | 2024-10-07 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 166bf0b9-5c73-3292-9b7d-436e0bfa5b51 | -17.178 | -57.3354 | 2024-10-07 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 010c7067-4c2e-39e0-97a6-15ec29e26884 | -17.772 | -53.8132 | 2024-10-07 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1ddfce3d-062c-3545-8387-3f2aaa21b05c | -17.7724 | -53.7918 | 2024-10-07 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| ce4b50e0-fad1-3e81-a4b4-4a7349c2df19 | -17.7918 | -53.8102 | 2024-10-07 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| dab1094d-1fef-3abd-82ba-33123a326ef2 | -17.7922 | -53.7889 | 2024-10-07 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| a8ddb755-6fc9-3d79-b5db-00d4c990a6fd | -17.8319 | -53.7829 | 2024-10-07 04:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 49fca7ca-1a23-30ce-b764-396beafb423c | -18.6391 | -57.2578 | 2024-10-07 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.9 |
| fc149d98-ce3f-3a31-acb8-c3aed0b4fd4f | -18.718 | -57.289 | 2024-10-07 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 0d035dfb-352e-3272-b892-f78c284c9d55 | -19.1297 | -42.7227 | 2024-10-07 04:26:51 | GOES-16 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.7 |
| 21bf1f05-4a55-3620-8676-bd091be7a75e | -20.4449 | -47.6875 | 2024-10-07 04:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 554d9633-a2d3-3704-a6d7-d3b91769a529 | -20.4456 | -47.664 | 2024-10-07 04:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 7a4fad3e-0aee-3c0e-ac2f-e958972cbd13 | -20.4655 | -47.6827 | 2024-10-07 04:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 55cc3673-4e65-3966-ab77-0e33ac3a21dc | -20.4661 | -47.6592 | 2024-10-07 04:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 878a058c-fb1f-3115-b1dc-500d6a10e70e | -20.5145 | -48.1132 | 2024-10-07 04:26:59 | GOES-16 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 100.7 |
| cfbdffd1-3725-3cd7-acf1-ccdcea1ff097 | -20.5848 | -48.5137 | 2024-10-07 04:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 714840fb-5f4d-3ee9-bf19-9786fcfc4d61 | -20.5855 | -48.4904 | 2024-10-07 04:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c7c60881-ed4b-3708-92fe-796a2e8accc9 | -20.7174 | -49.6306 | 2024-10-07 04:27:01 | GOES-16 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 49b35cef-6768-3487-afd7-7f5bd4ca462d | -21.3274 | -47.5939 | 2024-10-07 04:27:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 1e5d0aba-7fd5-3e4c-86b1-653d4ce84f93 | -21.5698 | -47.746 | 2024-10-07 04:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6249b00a-5e2b-3cc9-9050-f1e77cace15e | -21.5705 | -47.7223 | 2024-10-07 04:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b17da8cf-94ff-3a48-8c59-87ca2522890d | -21.5906 | -47.7409 | 2024-10-07 04:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 109.2 |
| acb4fb8c-3568-317d-a277-e13a8da16d6f | -21.5913 | -47.7172 | 2024-10-07 04:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5e7048cc-e282-3bad-87d9-b363644723fd | -21.6121 | -47.7121 | 2024-10-07 04:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3d19c140-b361-3ed7-b3fc-b24817f0e3c5 | -2.857 | -52.8993 | 2024-10-07 04:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d516b6ca-ce6d-3d6a-8da4-2248c873934c | -2.8569 | -52.9197 | 2024-10-07 04:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4a3b5bf8-3f58-3304-8624-109ab3f5839e | -2.8754 | -52.8989 | 2024-10-07 04:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 208ca884-187a-3a7d-a327-b4f6c5a39584 | -2.8753 | -52.9192 | 2024-10-07 04:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 0042cf4b-1f87-35c5-86a9-f56cbff11bac | -10.8755 | -63.8979 | 2024-10-07 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c94894a7-72be-384a-9740-5919f5005259 | -10.8754 | -63.9169 | 2024-10-07 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 29bcdbaa-4e39-3ce7-ba62-a6a0ec4e6a26 | -11.304 | -51.3646 | 2024-10-07 04:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fd9c0e4e-54da-3578-98fc-7558c663d0bd | -11.285 | -51.3666 | 2024-10-07 04:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 1b1334d9-3cdd-34b6-85f0-c77cdd06ef9e | -11.2847 | -51.3878 | 2024-10-07 04:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8af3e551-7bf6-331b-aa32-9b4903d88d12 | -11.266 | -51.3686 | 2024-10-07 04:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0cf891d1-ee2e-3987-a6e6-b4a129f0c112 | -13.7342 | -60.6471 | 2024-10-07 04:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ab56ed51-5f66-300d-86bf-f3a5c9668978 | -16.527 | -57.7161 | 2024-10-07 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| a6674f97-5d1d-39b9-8a29-d6f8ee500a59 | -16.5267 | -57.7365 | 2024-10-07 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| d3bee436-2c44-34a2-8597-575d2e800230 | -16.5075 | -57.7183 | 2024-10-07 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| fcc792cc-93cd-36e3-a3a4-90b34610ed57 | -16.5072 | -57.7387 | 2024-10-07 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| a8af37bd-9094-30b0-ad39-b6cdc840d291 | -16.614 | -57.135 | 2024-10-07 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| ecc65173-e267-3657-893b-3bc8250a7137 | -16.6335 | -57.1328 | 2024-10-07 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| c19f8057-401a-3f15-9aa2-c188e9663127 | -16.6332 | -57.1533 | 2024-10-07 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| d9c6ec82-1222-3ed2-b683-dca710f9c1a2 | -17.1281 | -56.7868 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.8 |
| 009f1efe-b5fc-398b-b012-496cfdd998af | -17.1278 | -56.8074 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 433.2 |
| aa657bc4-18bd-3c64-8e8a-cd2b3c33ba01 | -17.1081 | -56.8098 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 68a3fba0-6adc-3f6f-8d56-30242e28d6f6 | -17.1078 | -56.8304 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.7 |
| 764e68bc-7ec3-3d4a-b722-eb2b9ffcddd9 | -17.0985 | -57.4062 | 2024-10-07 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 6c8cdac5-aadd-3977-8349-7cbff46160da | -17.0881 | -56.8328 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.0 |
| 52be2e23-35a4-36f9-b4c1-7eebf47cd504 | -17.0319 | -56.6749 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.8 |
| 99e66d0f-2f5b-31e3-a11c-bac8a9cd0db3 | -17.0982 | -57.4267 | 2024-10-07 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 83de334d-4cdd-36cd-ae97-98105c711f6d | -17.0123 | -56.6773 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.1 |
| f7af7514-7e9a-3d2d-a559-cff401bd7bfe | -17.012 | -56.698 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| c0fde24f-5175-352b-ab7c-9b6cc54d4c4d | -17.1274 | -56.828 | 2024-10-07 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 329.7 |
| f393e578-c4f9-3518-bae3-0bff6ffcde1c | -17.1437 | -51.6989 | 2024-10-07 04:36:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3128b0d8-a196-35e4-9719-3e00192cd6e0 | -17.1375 | -57.4221 | 2024-10-07 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 3eddcea3-6575-3bbd-8d6a-9ad75b30571e | -17.1571 | -57.4198 | 2024-10-07 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 03094a61-2f26-344e-b75f-cf418797b0ee | -17.1581 | -57.3582 | 2024-10-07 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| a1c2dab9-30e4-390e-913e-0c45125a678f | -17.1584 | -57.3377 | 2024-10-07 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 0a4bddb7-4aa2-321b-bea5-d831893e37e0 | -17.1777 | -57.3559 | 2024-10-07 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| dd8dbed0-1896-30db-abf4-5b34ba94c840 | -17.178 | -57.3354 | 2024-10-07 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| ce5b6cd5-978c-3472-b17f-791efce8b319 | -17.7918 | -53.8102 | 2024-10-07 04:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| ec5ec47b-a779-367a-951f-151dbeb7712e | -17.7126 | -57.0858 | 2024-10-07 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 4f108b89-5c29-370e-ac39-ca27c01ee7b5 | -17.7724 | -53.7918 | 2024-10-07 04:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 07cb190b-958e-3d02-a3f0-7d19e210b3f3 | -17.7922 | -53.7889 | 2024-10-07 04:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3a5c1452-faba-358c-81e6-37c1aa39594e | -17.7324 | -57.0833 | 2024-10-07 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| e4feba64-dbcf-3f2e-aff7-ea24f585fc3b | -18.718 | -57.289 | 2024-10-07 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| fee730f8-e425-3a6e-962f-bdf0edfdc42f | -18.7176 | -57.3097 | 2024-10-07 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.5 |
| beb39632-81be-3f78-9138-74cec3e04648 | -20.5855 | -48.4904 | 2024-10-07 04:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c6bcfb5e-cbf8-3bb0-a02b-c3fed3b34eab | -20.5848 | -48.5137 | 2024-10-07 04:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d71324f6-e4a7-36bd-a257-a8b348b9020e | -20.5643 | -48.5183 | 2024-10-07 04:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b754db92-8c6c-3d6a-8f3d-aa61d3ffc560 | -2.8753 | -52.9192 | 2024-10-07 04:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 77979b27-64e5-3d89-bdad-b6fb2634b9cb | -2.8569 | -52.9197 | 2024-10-07 04:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f0007044-46fc-3e09-a8f5-89f810ab685b | -2.857 | -52.8993 | 2024-10-07 04:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8798cc43-666d-3f72-b564-9d04cb0ba4e0 | -2.8754 | -52.8989 | 2024-10-07 04:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |


[Clique aqui para ver as próximas entradas](README77.md)
