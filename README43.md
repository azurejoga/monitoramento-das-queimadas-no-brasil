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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2691f064-1176-3524-995a-6341ca56e87e | -8.37542 | -45.01662 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b21c8027-00b4-3009-b7c7-18d9e8d7f735 | -8.05497 | -48.65383 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aeeae53a-aa96-333a-9726-c915ec82c980 | -10.15595 | -46.20347 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c2263b27-b132-3a8f-9782-8120c6f23857 | -11.38091 | -43.53737 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6affbf0-da53-32a7-acbb-999dddbcf3c3 | -14.1691 | -48.98461 | 2025-09-09 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1c4a0b25-c20d-3f8d-9db4-26213730b1f6 | -7.56008 | -44.66466 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2611fac-fb8f-3369-8baa-0ad97030dc39 | -8.03444 | -48.62937 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49d54ea8-7996-3805-9885-807c9cdb220a | -12.62264 | -56.97623 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb324a0-a536-312f-a3be-e4c8317a22a0 | -12.81982 | -48.18028 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3c7128e-f06b-3c35-a3b3-a55e56af0f41 | -9.47009 | -60.50397 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d772f7c-bba7-3191-bf96-96c7c8012e62 | -12.88802 | -47.97903 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e7969e6-29ba-390f-bc12-35aa9082876b | -9.92686 | -45.47866 | 2025-09-09 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63c5db79-181a-3c09-8fba-24e5ee09cb1b | -11.43389 | -43.59871 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1f3c2c41-47c1-31bb-8a86-42761d007b21 | -12.61985 | -56.96527 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a658e66-fff4-3834-aa3b-8edacb242492 | -9.93093 | -47.87326 | 2025-09-09 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95e19be1-5352-3863-9371-a8f0bd8e96c8 | -9.43338 | -46.73523 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36718c38-3240-3a28-9f34-153664690916 | -13.65836 | -46.98338 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cea6ef83-d159-323c-b483-4eb62e821236 | -13.0394 | -48.02761 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 214cecb9-c1df-3247-bb04-ee1f89b4c2c1 | -7.7898 | -46.07848 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b45a9590-ce80-3a5e-9a5e-05a49304fd26 | -12.63177 | -56.97057 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aeb4668e-d5a6-3574-ad48-22914394937a | -12.81354 | -56.51685 | 2025-09-09 04:34:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89eb19b6-207b-39dc-8592-eaef154c1095 | -11.30483 | -46.50919 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8ea0897-8afc-38b7-a186-830706c58101 | -13.94978 | -48.23656 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de036268-af93-3d37-848b-8215629cfb24 | -9.29926 | -60.85826 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8baf87d3-ba93-34c2-9508-7c72fd745812 | -12.81311 | -48.17919 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37e60135-7445-3327-8b4c-a65e19e69c4e | -8.19217 | -44.76612 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0817bcee-aac7-340c-bb2d-e6645dfcf994 | -11.3076 | -50.41483 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ccb4e2c-d266-3f6b-8f13-4a4153ffd22b | -12.95893 | -54.77099 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 589cd31c-f328-33e4-8248-d19d847987bd | -9.01468 | -49.79083 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e5bbc66-58fa-306a-83c8-075e36dd2ef8 | -7.38681 | -44.8471 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a733da7a-f2b4-34da-89de-72ded3c2b25b | -9.55417 | -48.79128 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 133aa37d-208a-3d1b-9023-a280317ceae8 | -11.12085 | -52.02224 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8998daf-d018-3d47-ac91-d30159f117aa | -7.7881 | -46.08994 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6cf137a9-3f78-3737-a03f-22c256373f9c | -11.22481 | -59.12697 | 2025-09-09 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf2a13d6-4c49-3901-bcf2-76538d07d5c6 | -11.19636 | -55.00627 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71012fab-1916-3887-9824-74dc997bcf2f | -8.40248 | -49.10185 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b5b474a-f34c-38bc-8726-2c13df63fdfd | -10.18466 | -46.22811 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 176a2bb5-61e6-3e39-a952-d7bd11b861c0 | -11.81233 | -48.23733 | 2025-09-09 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0eec3aa8-d5ff-3e37-b55a-2450bd14dc05 | -13.74641 | -46.89827 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9745c29f-75bd-3192-a2a3-c9c31b6f21d2 | -8.02641 | -44.51001 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48cf18b4-d686-36d5-bec8-c3360f44205f | -8.02928 | -47.28686 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee6653dd-b198-3015-9f94-b912ef07875d | -6.33007 | -53.40656 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42a65778-efb8-371e-a7a3-3bfdc936f0cc | -14.34921 | -47.30903 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e8d4ad3-403e-3d18-8162-f3df15a37eec | -12.81349 | -56.51295 | 2025-09-09 04:34:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b20b1349-046f-366d-83fe-90a03f79ea04 | -9.47402 | -60.48395 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99a61eea-639f-3443-81b0-05234d54f7bc | -10.80804 | -48.29314 | 2025-09-09 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a479031-338d-3636-99fa-97dcbbb0f0de | -8.093 | -54.74885 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e34d74c-fd55-3da6-ac20-b17f780afbf7 | -6.87847 | -47.91047 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed7751bc-dd0e-3e20-9269-1427ed3f0655 | -11.21186 | -54.99246 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2d1f7c2f-c436-3065-be44-d21489ffd386 | -9.45277 | -60.52629 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e1a5bec-e7e9-348a-9c59-2c30117b7295 | -8.11696 | -44.86725 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7877011-25a6-3185-afb6-68868286d34e | -12.95958 | -54.76733 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 486dcc71-6147-3da8-adc5-a2bd1ad74ccb | -13.72809 | -46.90011 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a27b975c-54bf-39f8-bbc1-67a36c15d4d4 | -7.86856 | -46.25686 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec58c305-28f7-3fa2-acb9-93a8be9fd081 | -11.37258 | -43.53618 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e765c13-d823-3aa0-a12a-a88e1eca774a | -7.86825 | -46.25679 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ca9d6ed-453d-39bd-8fec-937d2d7d6b16 | -11.15616 | -45.26851 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a878d3ad-cc69-3dd7-bcb2-bbf703cd909d | -7.25629 | -48.25744 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b241b2c-e94c-38fa-80f4-7b0c23454d04 | -12.84463 | -52.94209 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b31c10b6-1c07-32e4-b36b-d5d73481d581 | -9.25259 | -57.06421 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf9508b7-5cad-3cb6-a9a5-1c775e86f5fc | -12.20554 | -53.89235 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 21898485-09d9-3b56-84c2-1c30115de6df | -13.72936 | -46.89149 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7faba30b-2418-3d29-88d5-ca2656c38852 | -9.45901 | -60.52748 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 606da33e-e89e-3d7f-9b35-a20df4dc5e05 | -8.00618 | -46.34292 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a1d1af1-2d39-3058-919b-ce2970c9f261 | -9.47525 | -60.48735 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8395ff67-10cc-3696-8525-7d8390673aa0 | -9.47304 | -60.48895 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b27b79c1-e8c5-3002-953e-81263ffe1ab9 | -11.38144 | -43.53351 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3352a7ad-f9af-351f-9487-8b12fe63451a | -10.33397 | -47.72853 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07f290c0-7f0d-3953-991e-f80e8f780cc0 | -13.0467 | -48.02486 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1f02c29-7cc0-309c-a750-ac58ee46a583 | -8.06452 | -45.5178 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f646c60-ab33-3b1e-9816-7143339e0616 | -11.33636 | -46.56312 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b904027-9351-30a2-a954-e075dbfaaca3 | -14.34979 | -47.32987 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64077d98-f06a-399e-8c2d-daceef89585a | -13.73934 | -46.89728 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e01ac365-660b-31da-a08c-b9935ff516dc | -11.30842 | -46.50275 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 680af9a7-4d48-30db-8af7-161f89fa6fda | -12.62329 | -56.96369 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 298dfb64-65ea-30b2-8fe0-252997499368 | -14.43451 | -48.46635 | 2025-09-09 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 714110da-0c8b-33af-8c94-c62677ba44ea | -7.28201 | -44.56812 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d695e161-64b4-3ccc-9086-60930d6ab2dd | -9.82014 | -46.02477 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0af455e5-dfca-32df-a613-c8fef2dbac93 | -10.15209 | -46.19949 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3069b298-26af-391f-9eee-bf75087f265d | -8.20481 | -44.82838 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63ac39e6-7379-3431-82df-4bb7778f127c | -8.70106 | -48.8713 | 2025-09-09 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 597b1e86-4b22-3cd2-9214-c0376106936a | -8.05382 | -48.63951 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b8b2424-e515-3846-8a08-0d11866534b5 | -13.74287 | -46.89779 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc95fb7b-ea99-3b77-9f52-724c9b13b47c | -13.81606 | -46.2431 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5cc413d-50c1-39e0-b299-7d776d4fe479 | -9.72066 | -46.80506 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 326d5b90-859f-3e92-8b9f-93cfe9f02fca | -9.78142 | -48.33526 | 2025-09-09 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9341be13-5e5b-3515-a841-418a3baabc55 | -11.30949 | -46.50171 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| daf6c0e7-e5bd-3df5-8b31-92132b13ada1 | -11.40009 | -43.55199 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c5313e5-6091-3fd1-b397-8980f2626f59 | -9.0913 | -47.04993 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98538b4d-0e02-3ce3-aff6-b68eeb00ea5c | -8.0588 | -48.65093 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05e8c16d-fbac-3bd6-b6a5-4e1126664801 | -6.61655 | -53.37083 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c61ee891-30e9-3b09-b236-29f999a1502e | -8.37458 | -45.02397 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96e504ee-fd3b-38d7-ab50-527586dd2ad1 | -9.78881 | -46.235 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b861a348-7569-39b7-8be2-7407cde506e8 | -9.71393 | -43.51311 | 2025-09-09 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aea46e6-f21e-3b50-8bb4-7d28a047e13c | -7.99701 | -46.33401 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4278718-507b-31e4-bc1b-894cc54df3fa | -7.66526 | -47.9893 | 2025-09-09 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ec6158-0490-371e-b6eb-8ff166cb2983 | -12.6236 | -56.97118 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f39c9e14-037a-3804-8832-52cc956153f2 | -9.01746 | -49.79494 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cf71bb9-58ee-3116-8f9f-733b1dd2cd30 | -9.69469 | -57.80682 | 2025-09-09 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6b4d9e3-bdd3-3682-a815-ed86523600cc | -12.94747 | -54.76501 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README44.md)
