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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1210bf30-5282-39e2-b2ae-dc6bdc45ad7c | -8.56702 | -54.67199 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f7c64e-1cd2-35da-9178-0ffd3743ec78 | -9.19475 | -44.53263 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5b21770-69ac-38ce-a35b-25f7131ae931 | -10.36005 | -50.83299 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50bf2824-b81e-39a2-a65d-36e1f977835a | -12.56114 | -47.01313 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 25ef5fb3-dc0d-3059-8daa-f238c662b4ae | -9.63323 | -40.58957 | 2025-08-12 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 272b1e59-292e-3b1d-9178-96848654181c | -12.55685 | -46.99342 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69483d3a-7b54-374a-8839-1005d435954c | -7.20816 | -46.25299 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78882b32-28c4-3905-85e5-418cfd552f2a | -9.71324 | -49.47808 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d425e269-cecb-3eb1-b01e-0937c8d0b8b2 | -12.86567 | -45.68293 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a5b4c47-d0ab-38fc-a15f-0b0448c74a96 | -14.1191 | -45.40386 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13a95f0a-27d2-3121-ab31-a0e607d7b1ea | -12.66473 | -46.97776 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29c74006-4eb1-3d26-b281-1a04ed4f7f5e | -14.6372 | -45.85244 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7bd59789-4da3-37dc-a76f-66f5ca32500e | -14.02357 | -47.41066 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aca189c3-f907-34f2-9c8e-5d8ca6672b5f | -11.45198 | -50.17592 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b33ade06-3454-3acc-93f8-f6e3a328e668 | -12.67224 | -46.97889 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88908c8c-e14b-3313-b241-baf2a3e2e311 | -11.66456 | -50.13502 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efad5fde-3d52-3816-a0b7-c7d6e57bf0a1 | -9.06893 | -45.05401 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4543be58-4a97-371d-a804-7c0718f9a450 | -8.0681 | -49.71334 | 2025-08-12 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fc4d083-28cc-328c-a3a5-b10132ce109a | -11.80291 | -44.93539 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7618ae8-fcf8-31ba-bd5d-3c83499c44d0 | -13.6178 | -46.92266 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ccc4518-b3b5-3d5e-914b-176037d5daca | -12.56413 | -47.01814 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c1e7532-8771-3a47-bbf9-a53d69a050b5 | -9.92126 | -46.18058 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d66d0a82-d9ef-3493-b7b7-8408bcb98c00 | -10.24325 | -48.25605 | 2025-08-12 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0081245-5436-33f4-a78c-45094460a3bc | -8.21351 | -45.04914 | 2025-08-12 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a465496f-a332-38df-afeb-051470351632 | -13.11734 | -46.86761 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dce715b-0f6e-341e-b192-fdb719e38c26 | -11.68297 | -51.59708 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6413210-96e6-3bfe-aa4a-15385dde77ac | -14.11602 | -45.37976 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb8e228-e971-3af4-a8fc-b23b003db851 | -11.94026 | -43.4073 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 408e0540-3d93-3211-b5e5-627ef56da4db | -10.76052 | -48.79557 | 2025-08-12 04:08:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 158f114e-2e75-3e74-9998-db006a922d40 | -11.75496 | -45.03377 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6eaa943-1ba1-3c08-a8c7-ca96657fe9aa | -11.66667 | -50.13402 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bc1a9c8-0685-3213-baa0-8751748aec45 | -10.17958 | -49.5096 | 2025-08-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f20fc1c1-1321-3b97-8fa7-ced3f71f1c06 | -7.209 | -46.24793 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16e2e099-94ef-376a-b43f-ff897236094c | -12.99965 | -44.88973 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec989aa5-4a7c-308c-a1a0-eee32fcc1b70 | -11.6509 | -48.3299 | 2025-08-12 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53b8f319-4310-31f1-9ede-37c57093ec32 | -10.34013 | -50.82918 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3774065e-4180-3c77-a195-4969d2aebe3f | -13.34978 | -50.24438 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c13249fa-9f83-3ffd-96be-14dd259d08fe | -11.95067 | -43.40563 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cc1d481-8f81-39c6-9f2e-44cf3e30873b | -12.77995 | -45.45774 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b6046b6-3567-3742-bf42-5606a2153b80 | -8.56049 | -54.6706 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80d36363-6811-35e6-9750-eb36c4adb098 | -11.68927 | -51.59175 | 2025-08-12 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d04a447d-dcfe-38fd-a274-346634016a0c | -12.57327 | -47.07699 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cb26136-1200-36f6-bc58-8010d12c2b58 | -6.30755 | -51.40286 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ebcd185-004f-3352-958f-c8e8152bf1c6 | -12.13987 | -44.9324 | 2025-08-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 285f956f-6387-310d-b697-44a95042d3c9 | -9.91754 | -46.18 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5b48897-22f2-3fdd-8a3f-26502f202885 | -10.96652 | -49.56743 | 2025-08-12 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 56ba1339-df84-3851-b9b6-14c188bce092 | -10.34118 | -50.82332 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbfdca62-45d7-31d7-b546-5bf39779b7ec | -11.75558 | -45.03004 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9c29682-c22e-3b73-8405-5c05ab7058d1 | -11.72185 | -50.08489 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2de230d5-5329-3939-b546-b503ab4173cf | -7.20995 | -46.21822 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec8e40f8-93db-3b1d-8bd3-d7a4398cc8ec | -8.57741 | -54.71543 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2596f44-06d9-324e-8782-91ab6798a443 | -14.12069 | -45.37275 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bd33687-237a-399d-8b64-c629d6da5f9a | -14.11351 | -45.39502 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f84b78dc-ccb3-33fd-b493-4fc70f8f0b2f | -14.27724 | -47.16317 | 2025-08-12 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77ab3843-d33c-39cf-b758-fd74ada6f924 | -8.52303 | -43.31371 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5d9446fa-22bd-3d13-bdd2-915dad1d1c7a | -11.75917 | -49.11058 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc0e1b2-d2fb-3328-b7af-66cc7fdf484c | -14.02812 | -47.40683 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d442b359-d7b5-3f4e-b774-2fdb10ee49a2 | -10.35507 | -50.83201 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ab46d8f-f4d0-3a44-ac4f-6c8ba4cc418e | -11.77415 | -44.93858 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65baba60-2c9e-3864-aa8b-84137c9fd6ec | -12.5102 | -44.77343 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef94043-287f-31f8-b014-38823298384f | -8.56214 | -54.68902 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2674807c-24c8-3aa6-a9a8-67707a7934b0 | -9.64664 | -48.14114 | 2025-08-12 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aae76f3d-b45d-380e-aad6-6b5ac31afacd | -10.35221 | -50.81928 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ad43a90-8f85-308f-a75a-a3a1f9f8f04b | -11.6998 | -50.12646 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 581475b4-ee91-31ac-9038-104abcd0a2bb | -14.02631 | -47.43916 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 024ce8fd-0cd2-39eb-88f3-12b3f78e599c | -12.56062 | -46.99399 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 184f2224-5bb8-36ab-b97c-c58959762506 | -14.10083 | -44.84945 | 2025-08-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15be8ad3-192d-35a0-b56d-032cd11d6533 | -11.4536 | -50.17884 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2633ff3-8eb4-363f-ab38-93af0c920133 | -9.19538 | -44.52879 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe66e82e-aae8-3f91-b7c4-289b1a0c1bf5 | -13.63183 | -46.92936 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e85473fd-18fb-32bf-b3cc-0bb41a8fed85 | -11.46294 | -50.15467 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18c36f73-afa3-3be0-ad31-c7707c175bf5 | -12.5479 | -47.04448 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c8f1137-292a-3dec-811b-9c2d619165a3 | -11.76502 | -49.10306 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cfb2bd2-ac28-3e9e-812e-1b19df6a7933 | -11.76782 | -49.11225 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3797b194-9d98-387c-91de-88f805c508f7 | -8.5639 | -54.68858 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1555080-e17a-3975-8677-df3425e7cbc7 | -14.0356 | -47.40838 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6c880221-cfa7-3e05-9229-d7291cf3fdfa | -11.73212 | -50.10722 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72373bda-51ce-3398-bd02-e82c3a4398f9 | -12.98328 | -44.88305 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 602fbd91-fa0a-3b51-9a87-1e02841723de | -12.66849 | -46.97831 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0ef0891-b461-3529-aa14-9c2b58733220 | -12.67307 | -46.97417 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b65d51f5-c716-322f-b3cb-3a8762405d92 | -11.67849 | -50.1377 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fbc86b3-f968-35ee-9a18-841937a6b2a8 | -12.56601 | -46.98525 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5d6e33c4-664d-3fde-8269-24c86aed47a6 | -13.63032 | -46.93822 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 091d50c3-fa0b-310a-b69d-e3218c3de175 | -8.56867 | -54.69035 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ba08bb8-47d3-32b3-a6f4-28e661d6ca85 | -8.56216 | -54.72384 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8ddbb968-2d64-38a5-957f-4720525b3d8b | -11.74035 | -44.97207 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7492a1b-b865-359f-9774-9713f2af7c0a | -10.23505 | -48.25331 | 2025-08-12 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f66d0cfe-9ed6-3a4c-9f50-2f471dab9a4a | -13.12862 | -46.88174 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 442d80c1-bb3d-3aa3-b08b-fe39592fa53f | -7.20431 | -46.2522 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3ba4140-a08e-34dc-9d4e-39eb7b299b84 | -12.63826 | -45.33348 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccbba85e-212d-3311-a31e-44ebbbc1a514 | -14.11539 | -45.38358 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 462877c2-6a29-3949-bed4-4a04de5a1979 | -8.66712 | -36.23508 | 2025-08-12 04:08:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4aed215-5b36-3e6f-8f04-b6f4c82742db | -8.98572 | -46.59438 | 2025-08-12 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d809c8cc-4708-329d-8377-757a8066f7be | -7.21075 | -46.21341 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cec62994-4f7f-32be-a08a-c1ae066bf0be | -10.3501 | -50.83104 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71be6c7c-56ff-38dd-982a-8c155ea3bebc | -7.55154 | -47.04826 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53567831-0576-3091-ae7f-4e67cf585c73 | -12.77777 | -45.44933 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f2cb5f0-ca53-362b-8a28-e8ad1001f54e | -12.73586 | -45.89774 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0bc2ae1-18d7-3e2d-9f9d-f28b1c10a622 | -11.8001 | -44.931 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ee4553-0dc5-352b-8b11-5d9b0e2689ce | -9.71445 | -49.47618 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README16.md)
