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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31743dfc-8957-305f-b00d-012ac4bbc141 | -8.08055 | -54.74562 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3924a836-a90c-34c7-96db-d32de3c1fe4a | -9.81139 | -48.39019 | 2025-09-13 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f5fa0fc-5eb5-3ea8-805b-968062878bcd | -7.43052 | -44.41383 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b08049e6-9024-3dd4-bbe6-4904aa44c7aa | -8.10742 | -50.18847 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de52be87-50c2-3fa0-9afd-4594ff754a17 | -4.28328 | -56.33069 | 2025-09-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af552be4-4ac3-3c28-aef3-0d27ff881668 | -9.96355 | -50.38036 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fa2ef31-1b4e-32ac-b8a7-fa28dee2d097 | -9.24978 | -51.25143 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3047ddbc-d5c2-3163-bae0-9d7e7efd5678 | -9.24302 | -51.24584 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04428b28-3bde-3bf3-87c3-056e4b8cb51f | -9.79244 | -48.89666 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 979ba33f-56c9-3c9f-bbcb-0f80955ed1f8 | -7.76063 | -61.1296 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0f7e699-cbb0-36c7-8efa-9a8211eef260 | -4.25797 | -53.51607 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6380e86-63f8-36b0-9cb4-b76328db5ac7 | -10.01324 | -50.39431 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bae9e5a4-5e2f-3ebc-9ccc-30de54886472 | -4.15051 | -43.88108 | 2025-09-13 04:57:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 810f9e88-00f3-3cf6-8a83-d195f6a5b775 | -6.93495 | -46.88903 | 2025-09-13 04:57:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 21ce1cd4-117a-3fe1-bdca-bea08d06362b | -9.24262 | -51.22296 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e784db5-17e9-38de-ad50-c9876e9a9ede | -7.86705 | -61.16943 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fb99589-ee2a-32fa-93f5-c3ffc0b9a4ce | -7.62348 | -46.54857 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b21b877-a032-3738-9ee1-7edbad4af5e4 | -8.09446 | -50.19016 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 974fb729-666d-32fd-91f7-273fb2e1257d | -7.90422 | -46.25193 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa5ac7bc-e9b2-3cb1-8723-bc29ec703780 | -9.9136 | -51.6165 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87717c6d-a65f-3952-be6e-985267554852 | -5.75647 | -57.57841 | 2025-09-13 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 877932b5-b1a7-33d5-b23d-f9df8f83dba2 | -6.14795 | -51.63174 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9ef3d48-3888-37b1-a14c-43aa0d718894 | -6.40043 | -45.62731 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3017ea27-ae72-3460-a4cf-26154dc19749 | -9.00671 | -45.76658 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 318a1c87-36e7-3b64-9ca1-6ba5fcd5de7c | -7.39119 | -49.98256 | 2025-09-13 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d24b1ff-8bb8-308e-bb89-5d2cc9212ca5 | -9.79512 | -48.8987 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58bc9fee-12f0-3a9c-8317-b8d42df739bb | -7.56222 | -44.08849 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92bb7682-c820-33c3-a3d2-70dcff905d95 | -9.98121 | -51.7177 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82838bb2-d726-3d50-bd6a-261a5d5d599e | -7.07105 | -44.12686 | 2025-09-13 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6eb4642-7bce-366b-bc3f-f8f27972fe05 | -2.94902 | -49.34809 | 2025-09-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0776560f-b04b-3887-98a8-af2923c7ac49 | -6.90553 | -49.41313 | 2025-09-13 04:57:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eb7db7a-13b1-3d8e-80cd-6cbdc15343e6 | -9.90716 | -51.88718 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 53e81f54-a9c9-3728-a3bf-e00baaf65525 | -10.01789 | -50.38977 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c7b66c1-e8a1-3e94-8af5-9ee57546d2fb | -10.01465 | -50.38406 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b4c25c9-e338-396a-b7b7-4c59366c36bc | -2.98115 | -48.60332 | 2025-09-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94cf299f-5fe5-3d2b-96ce-c293a6a3c4a3 | -10.33567 | -48.82613 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28e94eea-e288-3985-a29b-4f4cf6abc6b1 | -7.44906 | -44.44889 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c9dfb32-3c1c-3345-b0c7-dad1eece9de9 | -7.97926 | -43.65996 | 2025-09-13 04:57:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6177f5e2-7012-314a-b003-8609f3afa947 | -10.38416 | -48.57485 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c95742-8ae6-367b-8490-7d9e43520f22 | -9.96283 | -50.38548 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6daed66-19d6-3a89-8135-e6f0d62f3394 | -9.95447 | -51.69615 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddef7305-c2b5-35a8-bfe2-5151ae427ff1 | -9.9879 | -51.72306 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7fd78b0-92d6-38f4-9ca5-bc04d2563358 | -3.23152 | -47.63445 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42382acb-7a47-3083-bd33-a298d3a12bcf | -10.12206 | -45.4988 | 2025-09-13 04:57:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c297bdb-177c-32f7-934e-3b5d98111f1b | -7.41886 | -44.35621 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b621272d-8bcc-324e-ab12-e7d7e152dc70 | -6.19611 | -45.28236 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be29ef5c-41a9-3cc9-9429-186f089ecc0d | -9.82256 | -48.90309 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1492b51c-6d40-30cb-b099-0e6a0b88e978 | -9.88967 | -46.45895 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 149715e5-76ab-3807-bb7c-2d293ba79917 | -7.02318 | -44.89311 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be7876b4-09c5-3c68-8ac0-363a324b67ca | -9.55518 | -53.60162 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23970cb8-ea06-39fc-aeba-a7bf15b114a2 | -9.73801 | -51.01394 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f31fefb2-3596-3cee-893a-6b966c2a71a8 | -10.24663 | -48.25243 | 2025-09-13 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c40269d0-6b93-3140-afa0-1c646c9218f8 | -10.01414 | -50.39305 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c47a0e7-ac6b-3a79-9eb7-1a02fec82307 | -2.85567 | -49.50352 | 2025-09-13 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01aa6a07-aa0c-310e-90bd-4b7c8f259515 | -9.01119 | -45.77365 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 88163d5f-c7a5-3877-8493-88eaa79b7510 | -3.22844 | -47.62574 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0a2e2e02-ac1c-3ed5-9972-db2d82efd9f7 | -4.0834 | -48.0439 | 2025-09-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87d3a4c1-5aeb-33a1-b18c-a7b7560246c9 | -9.2528 | -51.24512 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 125377dd-a2fe-3dbd-8e91-810431dca8a8 | -9.00713 | -45.76346 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b49669a8-edff-3664-9004-38be01e8e4b1 | -9.00458 | -45.78263 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c70ffbb6-f935-3b9d-b330-73137838f132 | -9.80175 | -48.8932 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f44068da-f3e5-3b0b-b2d7-6f633a866b73 | -6.17171 | -42.75566 | 2025-09-13 04:57:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 787b4984-2e03-3c21-8a48-0515e32a582d | -9.9031 | -51.86472 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13efae6b-bb26-3bd7-ad6e-339fb6ec8f0e | -9.7271 | -48.35234 | 2025-09-13 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea35543c-c691-3766-8797-897b4e2b2c62 | -7.56641 | -42.64772 | 2025-09-13 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7b493527-916c-3e3a-98e5-8eabe39ad754 | -9.96868 | -50.28643 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54dadbb9-51ec-3da5-89ca-a8903b2994b3 | -8.09192 | -50.18042 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b9ef2c0-b19f-365f-bf1d-0ca2f38499ce | -5.63314 | -48.80793 | 2025-09-13 04:57:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15f02ec1-5776-38a3-8028-112a2798f806 | -6.32582 | -43.32954 | 2025-09-13 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18d6e8f3-87c9-34c7-bc44-2fbaa6d7a788 | -7.4336 | -44.85886 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77235f9a-4fc1-323c-8c96-947b44d155fc | -3.22783 | -47.62978 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ea2b777b-dfe9-389c-9cd7-2606fae1a92b | -9.74071 | -46.89119 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be80ec97-aca2-3d3f-a0ce-8164f75f34c9 | -9.95751 | -51.70101 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b050effd-7b56-3831-8a52-69938709eaa5 | -7.87005 | -61.15177 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f01cc583-f8bd-374a-b397-f1f977420a0f | -3.06069 | -58.96901 | 2025-09-13 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7e8daad2-eb73-3ca8-a5d7-f86b27ab1610 | -9.52705 | -54.63134 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ed778302-8434-3d0b-8c97-d51e62d02fd0 | -7.32066 | -46.58777 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5c306b39-2a94-3cda-805c-37513ed354b2 | -9.5612 | -53.56165 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7806ef9e-6333-3277-b5fd-04c87f5d31f6 | -3.79308 | -48.63882 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbacc18f-8d25-307a-bef3-077bd041d9fc | -9.79372 | -47.79314 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 727c06ed-b05c-3bd3-b7a5-d5d7b7ba54c2 | -9.54541 | -53.58566 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59ccc737-7778-385c-8224-432a4f2c2142 | -6.32861 | -43.44341 | 2025-09-13 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c8dcbe8-edfb-32ef-ae16-853b155de086 | -7.25972 | -44.59597 | 2025-09-13 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6defb2a-dd16-3608-89e9-6064963b7a9c | -9.52375 | -54.63083 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 793b41f0-e752-3d7d-9560-1cd15beed604 | -9.24038 | -51.26366 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 460397b4-bfe2-3731-9eed-a6440a18abcd | -7.43626 | -44.4143 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90357a38-aa96-3463-9047-4163857c4dbc | -3.21995 | -49.17381 | 2025-09-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4333fd98-8afa-3dd5-a8e1-fc0fd8a73837 | -9.24719 | -51.25786 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 23be5774-e30f-3745-962d-b905f3ded403 | -9.81496 | -48.89371 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f45c30ed-3e68-393c-8d6d-e8429b446e7d | -8.07503 | -54.73766 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba65e2c7-ddfb-316b-8d18-edfe45f94f03 | -8.08803 | -50.17981 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b9c5e60-542d-303b-ac28-4f36c803b5a7 | -8.3086 | -44.88165 | 2025-09-13 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ae4843-fc44-330d-9f95-beafa81dc757 | -3.77006 | -59.35637 | 2025-09-13 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7e48c474-a41a-36ae-94b3-4da436c67bf6 | -5.09321 | -56.16273 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33ccc0c5-a7b5-3481-8cb3-298da8a0f01f | -9.80007 | -48.89508 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8daf29b7-92f8-3a8f-93de-1f9d7e90cab1 | -7.56187 | -44.09159 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00237cba-18a2-3d9e-8cac-79793bba38f0 | -10.34495 | -48.82545 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a16d90e-d019-3a93-87a3-d7f473d76c1c | -9.73497 | -46.8903 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bfdabcd-ae11-3fe4-960c-0b3546ffd250 | -7.32274 | -46.58834 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 01aa1fc6-f33c-373a-b82e-011f87cabcc7 | -5.54347 | -46.41953 | 2025-09-13 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README74.md)
