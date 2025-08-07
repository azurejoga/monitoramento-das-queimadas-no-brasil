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
| 07922bc6-a506-3789-9d10-1eb563e27a4c | -10.42675 | -44.39803 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e85cb273-45f5-3ad8-96a3-a89acd334bb1 | -6.44827 | -46.10652 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2581235f-c8bb-3c8a-a761-bd5fb9102fba | -4.77771 | -45.33375 | 2025-08-07 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e764a61d-7a0b-3905-965f-b69eb70a5987 | -10.4366 | -44.38699 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ce80d60-9eac-3a17-a8a2-f4ad96e3e1ad | -5.38355 | -36.9071 | 2025-08-07 03:38:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2dd77967-ef9c-3885-ba45-a2bd91bc5119 | -7.27653 | -44.32439 | 2025-08-07 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f011c747-e054-3403-8612-cc56a5589bdc | -6.83703 | -46.39742 | 2025-08-07 03:38:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e091399-df13-36da-ac81-06c322e21148 | -8.51718 | -43.29182 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| df55ffe6-10a8-311f-b5ab-ce7045c189c2 | -6.43939 | -46.1176 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f647845-4eb1-37b4-8eec-ae876175b011 | -6.44284 | -46.11954 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41659dbc-a382-3142-bf60-56c89265c463 | -4.52603 | -37.79932 | 2025-08-07 03:38:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43e0068a-372a-3813-9a3c-ff5265ebb08e | -9.55743 | -40.35011 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| fa05ab3d-994d-3bf1-9d75-7a79efbdca52 | -10.63299 | -44.74587 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 98c52aa6-1b32-3d6c-8775-e080ae90fcae | -10.4305 | -44.37875 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8e44c90-8075-3be5-87b5-29be65a6e3b6 | -9.08714 | -45.06402 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f83935f-f224-372c-a940-18ea44c83c4f | -10.44149 | -44.39178 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e09fa91-6f8e-300e-9a3b-ed85555785d7 | -10.43457 | -44.38758 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5e34b15-cc7e-387d-a433-d5adadb961e6 | -10.44256 | -44.35502 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef6d8f8b-f0f7-3569-8032-ba778d39764b | -7.18953 | -45.48106 | 2025-08-07 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3c96b69b-da9b-34d1-a57c-a34d63c646ef | -8.97442 | -40.62259 | 2025-08-07 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c439c878-c9db-3e7b-acf0-490d8edfc107 | -9.56176 | -40.35089 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 5b031b03-6f9b-3e6a-a877-591b87d1f7c3 | -10.43868 | -44.39623 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6cde38ae-59e4-392f-b573-f26832179c30 | -4.77662 | -45.33374 | 2025-08-07 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e72adff-f914-316d-b9df-0fdd6d3be943 | -9.08118 | -45.06289 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea3787b6-2206-3710-8942-fcf95f63766d | -10.44222 | -44.38786 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0175be44-e9c4-3ddd-87ac-a99e771e2c59 | -10.42401 | -44.39249 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8099fb64-b820-3ca9-bba7-233e7217d6cd | -7.38482 | -44.25103 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 44894c81-1678-3f5c-97e0-d03c8a4ac5f2 | -10.4489 | -44.35191 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0079df38-ebda-396d-bdb5-f92f7c3f1b0d | -4.99215 | -37.33129 | 2025-08-07 03:38:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d860e01a-47ed-3980-ac4a-c5bead51d666 | -8.3869 | -42.26381 | 2025-08-07 03:38:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 833f1b35-c0d8-3da3-a748-6603abf58982 | -6.44401 | -46.1134 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00bb8969-1d8b-33de-91b8-e057bdb7e23e | -9.56251 | -40.34672 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| c50ccfda-7f2b-3fff-896c-bd8bb1e892ea | -4.77115 | -45.33295 | 2025-08-07 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5bba894-0cee-33c9-9f4c-ebe8b9787b53 | -10.43941 | -44.39242 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d03ebdde-6873-381e-bfd5-a333f1b3a13a | -10.44016 | -44.38857 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ef00280-9584-3ac4-8193-26bc13fd641a | -7.23708 | -44.64089 | 2025-08-07 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c888c176-6788-369c-aed4-4f5aedc2bfeb | -9.5614 | -40.34835 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| e8e74ca5-3a44-3745-a838-c17ef292ff5e | -11.28495 | -40.97668 | 2025-08-07 03:38:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| baff09de-6165-3bcb-a28d-158b0a268828 | -6.84116 | -46.39718 | 2025-08-07 03:38:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2c7ac8b-01b9-30e9-8952-31a5f5f1024e | -8.58561 | -36.17178 | 2025-08-07 03:38:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9fca8685-f9b6-325a-8fd9-9c27e754c1fc | -9.07605 | -45.05737 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb6b01b6-6249-3021-8c76-dc2842557ddd | -8.38637 | -42.26677 | 2025-08-07 03:38:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6dc6f3b3-b8e4-36ab-9e53-2ff3c030b41d | -8.33437 | -36.31716 | 2025-08-07 03:38:00 | NPP-375D | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d78e7bbb-59ba-3950-8e06-1c1af8af120f | -10.6379 | -44.751 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62730fea-1ef7-3d26-80bc-3d7d5222d089 | -11.27978 | -40.97855 | 2025-08-07 03:38:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c9175b28-60a3-3141-941f-585ba1c41709 | -10.43104 | -44.38582 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 138beb01-7616-350e-ba00-e55968768263 | -10.43309 | -44.39521 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2d3a69e-f45d-3e87-b474-66582f626761 | -10.4325 | -44.37803 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f55a48ee-a7cb-3e7e-9a13-adbb20d4017e | -8.52192 | -43.29623 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 264d23d4-15ad-3931-9d90-3314f743ccb4 | -9.082 | -45.05854 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed7f9f94-be18-3692-8715-2d12037708ab | -10.44502 | -44.39336 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02bdd759-e59a-31ec-bfe3-6621c86ed742 | -10.42183 | -44.40411 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 734b996c-ed1d-3b8d-ae78-366438ca8051 | -10.6273 | -44.74477 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ce921122-a521-3ac5-afc7-c07f59ef38c4 | -10.43234 | -44.39906 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ade456af-b3e9-3e99-b3bd-190162db761c | -6.5194 | -45.569 | 2025-08-07 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4947b22c-138c-30f6-87ec-b30559cc857e | -21.474 | -49.6467 | 2025-08-07 03:40:00 | GOES-19 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| e2c9e53b-ae10-33cb-9f8a-4e02a4196dd9 | -21.4534 | -49.6513 | 2025-08-07 03:40:00 | GOES-19 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.5 |
| 3d2a8921-881e-3cd1-8897-21cab17ba1fb | -7.4074 | -60.0108 | 2025-08-07 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| eb5a8382-a52b-353b-8144-b9b287150b60 | -8.9399 | -60.7481 | 2025-08-07 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4a8a42ca-963a-3a56-8856-32c732df1e40 | -8.9215 | -60.7297 | 2025-08-07 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ae98b201-85b4-39e1-8946-b98d4c6bdaee | -8.9213 | -60.7489 | 2025-08-07 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 58d72033-e0a3-35ad-9d5e-839ef33b9f9f | -11.75178 | -48.18483 | 2025-08-07 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7a70881-2750-3f9d-ab99-ff72b041189b | -12.37684 | -47.04689 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38483155-ac24-3c8f-a6af-b45e2ef095ec | -12.9988 | -44.8821 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83415513-e7a0-341a-a39d-083ed439826b | -11.77693 | -47.39791 | 2025-08-07 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d508851-fc05-3853-89d9-a8ade69baf2f | -12.71153 | -47.79441 | 2025-08-07 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a35dfd8b-f309-3f6f-9b4c-b84692c36f93 | -18.89609 | -41.0042 | 2025-08-07 03:40:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9e871905-f9de-32df-a836-07bc266e0536 | -11.7853 | -47.54649 | 2025-08-07 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5fab878f-1eaa-37ef-b298-05382778e15a | -11.77041 | -47.39641 | 2025-08-07 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06e4cb1b-0d99-3081-adfc-f4e07fc7e328 | -13.00282 | -44.89078 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eff70794-d5ec-3250-b4bc-523e544155b4 | -13.00494 | -44.87992 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f869f5-0894-38b9-9c30-b572caf6edc8 | -12.55379 | -44.74752 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d2ccef3-7581-33bf-b5e7-26f0cba950c8 | -12.71808 | -47.79597 | 2025-08-07 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77a21a94-6d70-3541-8ae8-4052d60a0d48 | -17.22793 | -39.28617 | 2025-08-07 03:40:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4046b252-c0c0-3620-93f0-a7b05f443a8d | -11.77555 | -47.39557 | 2025-08-07 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5ed2b13-c314-3f81-a313-9512be2d19f0 | -11.75048 | -48.19104 | 2025-08-07 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38c49cc8-5b6c-316d-b221-9193548bf678 | -12.54336 | -47.15303 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffa1c5f6-37c6-3654-9564-5205c7b530e2 | -12.71912 | -46.38252 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae9b8355-2327-38ac-909f-f0d4a758e9fb | -15.74616 | -43.38866 | 2025-08-07 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f68bb549-acb3-3ded-a03b-85bb4068cde1 | -18.89991 | -41.00525 | 2025-08-07 03:40:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9313e460-be7f-3ed9-905e-908f710695ed | -12.51774 | -47.14842 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db244642-6739-3463-a4d4-f00381c92ea1 | -14.52827 | -45.60481 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2e226729-7c31-3b06-b622-5aa95cbff214 | -12.73173 | -46.38187 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1393d12-268d-35a4-b366-71c38ab4c938 | -15.34571 | -46.34755 | 2025-08-07 03:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44edf674-582f-3b8a-b56c-955810a95560 | -12.55451 | -44.74385 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ac90410-30a9-354c-a299-8e9a7c1a5ee4 | -12.7012 | -40.18159 | 2025-08-07 03:40:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88db7aa5-3a35-3d37-a9e1-3ccadec79ca8 | -12.71209 | -46.38604 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10ff2b3b-2ad7-3246-9227-e660dfcb4274 | -12.54786 | -47.16349 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6d6d76de-2ea9-3cfa-b545-a07baf7adfba | -12.33593 | -46.05452 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3179785-98e0-3778-bfaf-44c29221e7e2 | -17.65644 | -42.2671 | 2025-08-07 03:40:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb19f116-a140-33b8-8651-2ff744099225 | -12.33413 | -46.06351 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0e4f692-88da-39c7-b8db-20c0f3049936 | -12.71812 | -46.38748 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de82cf36-b6cf-34df-8571-929595426425 | -12.70509 | -46.38943 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b61e17bd-9953-3b88-891e-8c2d005d4c58 | -12.54658 | -47.16974 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2d153f2-b23a-3c90-9b91-c60f535164dd | -16.21398 | -41.34269 | 2025-08-07 03:40:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7038358b-3261-3f19-a15d-2d49a81c5361 | -17.68029 | -44.43999 | 2025-08-07 03:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b77fbe2-7802-3b5e-ba8c-fd99fef327ff | -14.53544 | -45.5983 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3029e59f-9f1f-370c-b5b4-9e4d424fd04d | -11.74512 | -44.96319 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8dc28ff-18ff-39fc-977b-cbe0e0b395e1 | -18.72796 | -39.8679 | 2025-08-07 03:40:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e6dda50e-cc69-32de-a31b-6fc6b58c75ad | -12.73078 | -46.38647 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README7.md)
