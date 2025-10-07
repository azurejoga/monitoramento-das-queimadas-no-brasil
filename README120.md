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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 610b2918-4733-334c-b779-56640680d624 | -11.8221 | -45.1059 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5be90b80-c9a9-3b0d-bc69-ddfe242c8c26 | -18.0187 | -44.9725 | 2025-10-07 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f23c18d5-5b4b-3da1-ac6f-6c6caf356b57 | -10.4058 | -45.3702 | 2025-10-07 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 161.1 |
| cf087009-efad-3566-9894-67ebc40b62a7 | -12.2215 | -44.2543 | 2025-10-07 13:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 9a12a813-dacf-37ad-bb26-7af614408f96 | -14.7384 | -46.037 | 2025-10-07 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5d8c7075-1fc7-3deb-940e-6186a676d3f2 | -14.7575 | -46.0566 | 2025-10-07 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| dfee3874-7108-362d-9d80-c13563436bbe | -15.6202 | -52.5501 | 2025-10-07 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| aeba1299-0759-3035-97d6-22f989ec0486 | -14.5057 | -46.9242 | 2025-10-07 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a127e71c-b935-3a4a-b24e-07f78227299c | -11.7833 | -45.1347 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 52084a9c-ed65-3f7c-8441-6e12057b3118 | -8.8986 | -47.6483 | 2025-10-07 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 129ae735-0ef4-3f5a-8645-ad445c7d5731 | -9.6098 | -46.6416 | 2025-10-07 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 105bd035-6843-37cf-b157-0e5f5a2262bf | -17.9784 | -44.9817 | 2025-10-07 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9506a3b3-f526-34b7-bd52-0672042d75e6 | -8.5584 | -46.2387 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 2fcc7ac8-6fef-365a-b4d2-269e2edd307c | -11.1644 | -54.8804 | 2025-10-07 13:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 401.9 |
| c1e8ecc3-d28b-3634-a664-bec2ac0fd891 | -8.4824 | -46.2912 | 2025-10-07 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 0c92d0e2-8a06-3e56-b031-999fa51b39ee | -12.891 | -54.7577 | 2025-10-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 329.1 |
| 76f0c82c-452f-3293-8c42-2c94e78ca76a | -12.9103 | -54.7352 | 2025-10-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 0f06e131-61e1-3722-a746-6da929e1c20e | -12.7637 | -50.4921 | 2025-10-07 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| f8acd4c5-eba5-3175-979c-59f9a57135e8 | -12.6159 | -44.7519 | 2025-10-07 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 7f827b98-c8bd-339f-871f-d7c4f1fa37f8 | -16.2942 | -50.9868 | 2025-10-07 13:10:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 24eddb11-fb20-3314-b72e-07038e14036d | -11.7837 | -45.1115 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 943b5d81-1b13-31cd-8a91-b1ab7763387b | -11.6859 | -46.3366 | 2025-10-07 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9e294d18-c3f2-3532-8e4d-d30d58afc2e8 | -8.1055 | -44.7891 | 2025-10-07 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| f58fecc5-51e8-3ca4-a67b-477c243870ee | -9.1978 | -47.8161 | 2025-10-07 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| efe37e96-bfe6-3a21-a9a3-b1b2b436e440 | -13.2658 | -48.0632 | 2025-10-07 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c818e556-fb9e-39bc-aab0-511ce8ec342b | -8.8794 | -47.6722 | 2025-10-07 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| cec444c5-99b4-3868-a7cd-eb275eaff4ee | -11.0451 | -50.9047 | 2025-10-07 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b4ae9601-332a-31ee-9c2a-86f5b8a1e018 | -10.4108 | -50.2683 | 2025-10-07 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| cb19e692-bee4-3c16-a2e8-85296e559150 | -14.2953 | -45.8382 | 2025-10-07 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| d695a52a-7d1d-37f6-9203-442320d99b06 | -11.8635 | -44.938 | 2025-10-07 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6caeb31b-66fa-3daa-b87d-4a4da8a33d6d | -9.6804 | -45.6645 | 2025-10-07 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 82a4a8b3-e20a-303e-90f0-5328f218927d | -7.8074 | -44.5209 | 2025-10-07 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0fcc3fd0-caa9-3689-aa3f-de4fd534c790 | -11.8635 | -44.938 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 52c2150a-75f4-3c8e-9c8f-4dbfa87688b4 | -8.8606 | -47.6741 | 2025-10-07 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| af3b9ed7-3307-3ac5-b240-b7c6fd5fe8de | -11.8025 | -45.1318 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a73a44b7-b86a-3a78-a965-9a84323a699e | -10.3854 | -47.9956 | 2025-10-07 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| f8e8d835-4327-3728-aa9a-27696d912092 | -12.8913 | -54.7372 | 2025-10-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 845.8 |
| e635f2bc-7770-3c51-b805-a0a402bfc5cb | -7.7368 | -42.5906 | 2025-10-07 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 6affb1d9-2fb9-3ca5-bfdd-96b4ec855864 | -7.7932 | -42.6082 | 2025-10-07 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 185.2 |
| 0770ca76-908b-314f-89f0-e2099a3c036e | -8.4821 | -46.3136 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| b4bd375f-4aef-363d-bddc-f1c3f7e63048 | -8.0866 | -44.791 | 2025-10-07 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1f61337d-9901-329a-83aa-d56d36cb1139 | -8.6519 | -46.2964 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7c48c0e8-fc7a-397c-a6a6-1d2afcf94f40 | -9.9396 | -50.2304 | 2025-10-07 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 8e676537-04fe-3a75-8c06-c473f4febe12 | -12.8916 | -54.7166 | 2025-10-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 644aaa16-dc63-32fc-bf23-16b3f6b8abe7 | -17.9778 | -45.0057 | 2025-10-07 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 42b6c446-3923-3110-8e25-9e05c80b6695 | -9.1525 | -49.9639 | 2025-10-07 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d4200cd3-3d6b-3e6c-86b1-53ff1eedd16a | -8.4522 | -47.2288 | 2025-10-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d770bd57-a23f-3319-b015-e14d72d5af26 | -11.1453 | -54.9024 | 2025-10-07 13:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 76d4b50a-0d0b-3e0f-90b9-33466a62f484 | -15.6198 | -52.5715 | 2025-10-07 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| af1dcbd9-fc9c-353a-ae38-e160e1769305 | -10.9109 | -47.1129 | 2025-10-07 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 795.1 |
| 5f9a3e3c-3e83-3332-ad88-114baa02cb77 | -7.6648 | -45.4471 | 2025-10-07 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2c574e35-b96a-35bb-a537-a41526f26ead | -12.4669 | -45.5155 | 2025-10-07 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 46dd8886-0cfe-3e9b-91f0-0e60c2367503 | -14.2953 | -45.8382 | 2025-10-07 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 5f6bfe87-e096-3a4b-a51d-8151203fded4 | -14.8645 | -51.4158 | 2025-10-07 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 28bbc6f1-f87a-3e2c-8c45-c7ab0f161f9f | -7.756 | -42.5648 | 2025-10-07 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| fe4b601d-c931-320e-975f-e4e184c8a267 | -12.9103 | -54.7352 | 2025-10-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 263.8 |
| 2551c146-00a5-332c-8b82-a6a117bb16a8 | -8.8794 | -47.6722 | 2025-10-07 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 277b4f70-c03d-3d3b-87b0-9173a49400c8 | -11.1642 | -54.9007 | 2025-10-07 13:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d5baf43c-8381-3332-86f5-d8d5cc78cf1d | -8.0946 | -47.2844 | 2025-10-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b26dd8a2-9c6e-3dec-baaa-3443c5420329 | -9.1786 | -47.84 | 2025-10-07 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 28c2e767-b3a9-3427-aa78-a23211b47d19 | -17.9979 | -45.0011 | 2025-10-07 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 194.2 |
| eb6c4b45-5606-3c18-8621-4c2ff7342745 | -10.0868 | -50.5141 | 2025-10-07 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 834fe141-2835-34fa-9141-0a9d0e9bb567 | -13.7927 | -45.7627 | 2025-10-07 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| c76d863e-ebf5-3b22-8782-5c6da8c6c13b | -9.1978 | -47.8161 | 2025-10-07 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| de7c9552-7d93-3034-949a-209ae1bec8c8 | -11.6859 | -46.3366 | 2025-10-07 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 04d284c8-9e32-3edc-81a1-dab4b99644ad | -12.9101 | -54.7558 | 2025-10-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |
| dc036e0d-99a0-33df-9631-4662468bb81a | -8.5599 | -44.6494 | 2025-10-07 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3a092153-5a16-39cb-a25d-964a7cad1af0 | -12.2215 | -44.2543 | 2025-10-07 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| b22bb74e-36aa-351e-8f94-ed7764c4da34 | -12.6159 | -44.7519 | 2025-10-07 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 3239f3d1-4fe2-33dd-ae25-6bd862f6046b | -8.5007 | -46.3342 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 37188190-25e1-36aa-bd67-486d2d0d1388 | -11.1455 | -54.882 | 2025-10-07 13:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1180.6 |
| 667788e2-e10b-3719-930d-538ad542a0ff | -8.5584 | -46.2387 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 47f8871a-ee03-30f2-be6d-318c7a9a33e9 | -14.8641 | -51.4373 | 2025-10-07 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d42dbfbc-1a07-3a65-9052-d0f55e88e3cc | -10.9106 | -47.1353 | 2025-10-07 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| d8c9c0ba-3dbe-3f08-8036-e01d355f08da | -12.891 | -54.7577 | 2025-10-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 477.4 |
| d3fee812-46bb-3b09-abd0-c0e7dcb0f421 | -8.501 | -46.3117 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 9f4a4796-beb4-3f5a-8dd4-bf8ff9d71bf8 | -7.6651 | -45.4245 | 2025-10-07 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| be3faf9d-dbcd-3704-a45e-9c1e247fb253 | -8.4525 | -47.2067 | 2025-10-07 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4d9657ff-15f8-32dc-af7f-d3f962c896bb | -15.5812 | -52.5556 | 2025-10-07 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4b6582ff-7a0b-35ff-a56e-f74ae2c93975 | -13.1321 | -48.0159 | 2025-10-07 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9810bfc5-235c-3c1c-9e63-24cbc03ecfe3 | -15.3742 | -47.2973 | 2025-10-07 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 24e63011-572a-372d-a0b4-6ac946cd5314 | -9.1789 | -47.818 | 2025-10-07 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 92426a8e-f3da-3cff-a0dc-05abb6b0ea35 | -11.7221 | -45.3508 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 67e5e825-fa19-357f-b6ea-09a5eaf04277 | -8.4336 | -47.2085 | 2025-10-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| fc0e4799-aebc-3e19-afe5-2d2c808b09d7 | -9.2166 | -47.8142 | 2025-10-07 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a04303d5-b548-3053-b217-87e5972ae691 | -11.7833 | -45.1347 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 69bb640d-4e5e-3ab8-975f-762240587ac3 | -10.9113 | -47.0906 | 2025-10-07 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 0334ddb6-6af4-3a5a-a02c-b1beae2f565c | -8.5207 | -46.2425 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 4e0180d5-bfda-3dba-b383-c8468a2f0bd2 | -10.4245 | -45.3907 | 2025-10-07 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 3184693f-9f42-3bc6-b31d-b5b76fa49f28 | -8.6521 | -46.274 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 67f44026-8364-3106-8afd-24d81bc8d9a2 | -8.5395 | -46.2406 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 04303322-4b63-334e-bd55-aa1134aa1f7f | -14.3148 | -45.8348 | 2025-10-07 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| a7f8d125-4dce-32ee-bd40-b8a4ac66659d | -11.2433 | -50.2859 | 2025-10-07 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 8f0872e4-e385-32f4-97ca-74765bc91c40 | -11.6855 | -46.3593 | 2025-10-07 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 81e81b60-c971-3f3c-bf0f-19e333f48a03 | -8.1804 | -43.3445 | 2025-10-07 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| b6fbea3c-2844-3a27-8859-97ac8b6e3481 | -8.1879 | -44.2283 | 2025-10-07 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 1e9614d2-e339-3bf7-8b37-ec058fc2eed7 | -13.0939 | -47.9992 | 2025-10-07 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a8373de3-11b7-33a4-b07c-445d0d31a201 | -10.8922 | -47.093 | 2025-10-07 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ec7f06d2-70b9-3f19-9cb0-23d17a2b1fe8 | -8.1801 | -43.3679 | 2025-10-07 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 5bc4aa0a-edb5-34fd-96e4-b4a5c3f928de | -19.5789 | -44.6198 | 2025-10-07 13:20:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |


[Clique aqui para ver as próximas entradas](README121.md)
