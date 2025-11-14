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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a95afb7-ea50-3b3f-9a37-be2f8a1ff15a | -12.14595 | -48.01376 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 92c9356e-e76d-335d-8ee6-3036d7c89bfe | -12.14726 | -48.02298 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| d10557aa-3821-334f-a0e1-38d38dc7774b | -11.84593 | -49.22606 | 2025-11-14 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b17ef26a-de5c-3f99-ab8c-b9772d28e8d3 | -12.55123 | -47.81795 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3889b1e5-5501-37fc-9de4-adf48717375c | -13.47448 | -46.499 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a773d6ca-44b0-3e3c-8d68-bad830a34ad7 | -12.45952 | -43.7431 | 2025-11-14 00:32:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1463db5e-fde9-3ba1-abe1-2f1cb731b4be | -15.39149 | -48.96987 | 2025-11-14 00:32:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6796028f-9d82-34be-846d-88f1217b2c32 | -10.288 | -44.35236 | 2025-11-14 00:32:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 58b146c4-10fe-3660-9254-ec539b49eb37 | -14.67295 | -46.56093 | 2025-11-14 00:32:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62b56897-aad7-38e7-bf6b-f50917cb37ca | -12.70981 | -45.43479 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ee5dbad9-e2bb-3bcf-a4b3-f50c597156e0 | -13.02886 | -46.53734 | 2025-11-14 00:32:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 628f07ee-a5ef-3cdb-a5da-50f1e18c7fda | -9.67724 | -47.88721 | 2025-11-14 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fabade19-0d86-326a-98c7-b50a3d3bb67c | -11.81866 | -47.78667 | 2025-11-14 00:32:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a0f14832-27fd-32de-b191-98feda7d2646 | -13.92339 | -42.89139 | 2025-11-14 00:32:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ed6055ae-d629-363b-88e8-929984a96cb1 | -10.62839 | -45.00003 | 2025-11-14 00:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 34f561d8-d59d-3f7d-97a5-ac253f97313c | -9.63854 | -40.35426 | 2025-11-14 00:32:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| a16d613b-af33-3e1b-a3b0-76ad88fe2f8a | -12.13701 | -48.01517 | 2025-11-14 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bec0719b-d489-3ca0-bded-65ea0f875139 | -11.82769 | -47.78531 | 2025-11-14 00:32:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 44eed76f-6814-3ee6-b29d-517ff84833aa | -15.55002 | -43.17608 | 2025-11-14 00:32:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5fa0d03e-8363-3d1a-8213-eaf6de724e67 | -9.44492 | -46.97232 | 2025-11-14 00:32:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 027af20b-7664-399f-b164-9e75bb85b62f | -10.48159 | -51.86545 | 2025-11-14 00:32:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bb4ab1fd-81ce-368d-9c52-8507d16a007d | -11.73042 | -48.52637 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c6163a2-e946-3c78-a1b3-c4bda62dd753 | -11.74058 | -48.53412 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 89081a80-aa91-336f-bfec-b5b5178aa392 | -11.92816 | -43.93967 | 2025-11-14 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2b602ac0-a301-33d3-9403-83a865d1a525 | -12.01897 | -46.76199 | 2025-11-14 00:32:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4f4958e-4001-338d-a6d4-6ed9aa710ae4 | -9.34891 | -46.58683 | 2025-11-14 00:32:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d7d3d65f-3707-3b1d-bfe1-c005f32c9e58 | -13.76421 | -43.16571 | 2025-11-14 00:32:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 7b292498-d463-3354-b93f-767119dbb2a2 | -12.45168 | -44.6325 | 2025-11-14 00:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e54e0ab0-547b-31b3-bbee-36e81dc2c544 | -10.34027 | -49.9225 | 2025-11-14 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f4bb4b4-6bfa-308f-b783-c1ddf4d59d4a | -11.6664 | -48.4678 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f95f8fc8-8604-3a33-8f26-bffe52fb778b | -11.03851 | -44.65355 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a98c5f44-49fb-3dd4-a415-7879555ffd5e | -11.72915 | -48.51732 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b1d600a-13e0-3066-8eea-cf0eeb0e006b | -12.68598 | -45.41405 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c12b4cc7-eca7-3cc2-aba9-6723df9c7c52 | -13.47297 | -46.4888 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6c35a49f-3ec7-3a84-9c12-be1bff5b84c9 | -9.63178 | -40.3487 | 2025-11-14 00:32:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.2 |
| ece5b18b-f302-3660-afe6-9150364db105 | -9.12161 | -43.9626 | 2025-11-14 00:32:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 3a25d017-90fa-3a6d-b358-eb3a4fcfb638 | -12.6878 | -45.42605 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8634d04c-d2e0-339a-bdce-1ae7e67b665d | -12.7181 | -45.42112 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 4afa8b0f-a1d3-3571-9c93-9f1a963987a7 | -10.76102 | -45.02285 | 2025-11-14 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| df568491-5504-33b1-9dff-a778b40a8136 | -14.76035 | -49.68209 | 2025-11-14 00:32:00 | TERRA_M-M | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21bb93b1-8d90-3277-844b-674ec6f7318c | -9.67859 | -47.89675 | 2025-11-14 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 02f4c483-26f1-3923-8fc0-d112cdb2e87e | -9.31003 | -47.84196 | 2025-11-14 00:32:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4de7d191-bcbe-3403-9474-24e5984ae2de | -11.8523 | -49.20679 | 2025-11-14 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 08089460-254c-3a1a-a20e-eb206ccfe06a | -12.02058 | -43.73279 | 2025-11-14 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4705ced0-c556-37aa-92ac-a375ee221665 | -12.06346 | -48.21077 | 2025-11-14 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 456e021b-1f2d-3a8c-b3fc-ccb35dbcb746 | -9.55818 | -47.76305 | 2025-11-14 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad547634-484d-385d-974c-4586aae88bbd | -12.708 | -45.42279 | 2025-11-14 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ed6c7ccf-14f0-399d-a1be-72af266d42a9 | -6.47391 | -48.36714 | 2025-11-14 00:34:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 26e66015-2b50-3774-ac88-89ab23a0de86 | -5.30127 | -45.08033 | 2025-11-14 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8dcb9536-01d1-3b5a-ad28-73aa126dceae | -4.52113 | -45.61691 | 2025-11-14 00:34:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 557dc80f-0372-3745-9a96-b19e5efd9505 | -1.83289 | -53.80981 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 32159d2b-f406-3704-a686-a73529c42d59 | -4.7043 | -46.46714 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d0a3318e-4e14-3153-8743-f96405c0131f | -3.95523 | -47.50264 | 2025-11-14 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 90bd2c8d-89d6-3624-a6c0-ff0e4077be44 | -2.80095 | -52.96213 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e73d2342-b54b-3919-b6aa-7d0619a00df7 | -7.39008 | -48.65368 | 2025-11-14 00:34:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8c45aea8-55f5-33e5-ad8a-5d6ce7818330 | -1.49239 | -47.80799 | 2025-11-14 00:34:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d9637e92-ff25-3f09-b6ab-23bdfc8f8934 | -7.78234 | -49.61402 | 2025-11-14 00:34:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e6dce01-0f5a-3e4c-b8b6-76bd44724a32 | -7.86179 | -44.30311 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 1260896f-16f9-39de-847a-3e60b2f4485a | -6.13319 | -48.05172 | 2025-11-14 00:34:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 321a50e2-db84-36e6-a469-64e6f34ff4a3 | -7.79119 | -49.61275 | 2025-11-14 00:34:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1b219114-beff-3fc9-892e-66576f6c2a0c | -7.85678 | -44.31047 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d53e472d-37ce-3a3b-bcfb-7d4813e42dab | -7.79243 | -49.62165 | 2025-11-14 00:34:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 017c8526-c5e5-3578-9619-622c88f5b331 | -2.80231 | -52.97204 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 922d6d61-f949-37f2-aea9-028f279c61ba | -2.83903 | -52.36889 | 2025-11-14 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6c5b0f61-b5c2-3e14-9b66-7da6fdb87fd1 | -4.33098 | -49.04773 | 2025-11-14 00:34:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ab2e1442-6039-3eac-b71a-839f67fe2796 | -6.14261 | -48.05045 | 2025-11-14 00:34:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 06f16065-3530-35e2-96af-e093c01b53af | -2.83566 | -45.48352 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 0fe43a34-57b3-3cb2-afb2-af3b35f90457 | -2.96732 | -45.75712 | 2025-11-14 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 60d4c680-0e6a-38bd-b2f7-15a9d13682fa | -3.31593 | -49.1595 | 2025-11-14 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 86d6e6d3-941d-3eca-8415-400e8854298b | -4.95992 | -47.72216 | 2025-11-14 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 28.8 |
| c1efc675-5496-3af5-9b9f-96548deca339 | -3.01381 | -49.44258 | 2025-11-14 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9ab78b3c-6ec2-396a-bd53-5caeeb5fbd9f | -3.52367 | -52.79309 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8257e89-8997-361d-bfbf-2576e2f16494 | -6.45966 | -45.66323 | 2025-11-14 00:34:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d3d73971-5ec5-3e0e-9a67-71c515b6bb40 | -3.82957 | -50.79431 | 2025-11-14 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70f930c1-b803-31b9-b97b-91b5f1b835d3 | -4.95658 | -47.71753 | 2025-11-14 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 72d63149-e462-301e-baa5-72142a99e607 | -1.82995 | -53.78878 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c7a84ce3-2368-3732-9f99-307e4ad71463 | -8.94408 | -49.81259 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f819cf4b-4a6d-3c60-8a48-6b075f26e5e5 | -6.61667 | -47.6398 | 2025-11-14 00:34:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b64961cd-8262-384c-98fe-1cd8fda5b90e | -3.66082 | -45.94313 | 2025-11-14 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0d0acad0-3616-3d50-b1d5-9c3d9e4fb1e5 | -5.46198 | -47.0964 | 2025-11-14 00:34:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 93b5edab-2407-30a4-921c-c453c53149b6 | -2.85456 | -51.28234 | 2025-11-14 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e11c0075-d4d2-3dfd-a2db-5f72de43cd66 | -3.11237 | -45.40691 | 2025-11-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 40dedb2d-00ec-3232-8f8f-5dd41ba3140b | -2.11025 | -45.37618 | 2025-11-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| db9fd3a0-097c-353d-b42b-5e1fc2c27e52 | -3.64034 | -44.35152 | 2025-11-14 00:34:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7610d878-ae0b-3141-9243-d024d8d66a6b | -1.93024 | -54.50615 | 2025-11-14 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 89e6b6d4-f131-3d0f-b6fe-032c4fef81d9 | -4.70237 | -46.45403 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 3904811a-46ff-313c-9c98-f29399b3524d | -7.04883 | -45.06018 | 2025-11-14 00:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 19382104-890a-3062-a3ca-adbbfbd5eb9f | -3.60371 | -54.71191 | 2025-11-14 00:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2942291f-7acd-38d0-be3a-6b5a1c4b58b0 | -3.77413 | -46.01091 | 2025-11-14 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fc264355-e8a0-35fc-b3ad-bebcbbc0a6cc | -7.33996 | -46.01438 | 2025-11-14 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f848b4f5-ad96-3430-8aad-0e0d7a20e360 | -4.70043 | -46.4409 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 945a0db4-c0ef-3d29-92d8-45c55df71c5b | -5.98188 | -42.6029 | 2025-11-14 00:34:00 | TERRA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 690ae353-05fe-3103-8e67-2463f760d2c5 | -3.91275 | -44.33263 | 2025-11-14 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6151344a-1bfb-3595-a3db-8e89e35c970e | -3.98771 | -48.00642 | 2025-11-14 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ce8681f3-5bdb-32e1-beaf-5b9d4141bd06 | -3.41287 | -52.72531 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 23245426-de77-3233-be97-aeb63f8338a5 | -5.34287 | -46.76512 | 2025-11-14 00:34:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 75987789-0e09-305d-9952-7b5440f74ee7 | -3.81985 | -52.3372 | 2025-11-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd07d813-6476-369c-84c7-2b249da2a661 | -5.7518 | -49.25468 | 2025-11-14 00:34:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d154cff9-d144-37a9-bee5-ec648080cdb5 | -7.78358 | -49.62291 | 2025-11-14 00:34:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d7417f20-0522-3edb-9775-9af83387d9cd | -5.8439 | -47.69048 | 2025-11-14 00:34:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README4.md)
