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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8798490c-9b39-346b-8544-41ff1df17778 | -9.44645 | -46.71298 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e244edc3-3b49-3108-bd46-276edca6c970 | -8.08919 | -54.75526 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf698faa-80ec-30e7-a35b-8b9efea2ce77 | -6.53928 | -44.78702 | 2025-09-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46066c83-e658-3bcb-a8e4-25193ce525d1 | -9.5268 | -48.26667 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b534775a-e4e3-3a2d-bf62-cc221335fecc | -9.45159 | -46.70917 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88ed20f1-a027-3f9a-b0c4-0ec2a860c4a9 | -11.66408 | -46.90818 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7ea500e-bcb5-321a-bd46-79ba96ac5e1e | -11.67015 | -46.90554 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4d4839d-ef92-3e26-ae20-16401d38e584 | -11.21075 | -54.99414 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba37962a-a181-3eaf-98f0-ad28ca197945 | -7.81485 | -47.50829 | 2025-09-10 05:04:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a267adb4-9346-3865-88f2-ba9e601f1ba8 | -11.45717 | -43.62492 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d088d7d8-bc29-3069-b17f-ad44c0c94798 | -9.03215 | -49.79045 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0807141-68c1-320e-b5e8-a4627c828daa | -10.46918 | -47.94501 | 2025-09-10 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ec6f1a0-3d3e-3aac-a0c8-b068b25d7630 | -12.20115 | -53.88503 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d84ede77-5424-37d8-a1b8-31b00a531455 | -11.6645 | -46.90479 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c33c83fc-b374-31bf-8b82-9956e2583bc9 | -11.38516 | -55.06656 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6a9dca8-7c0d-3c82-a7c1-4e2c3bfd09b3 | -9.06269 | -46.97987 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f463b6c-e1a6-39ee-8379-6f69b4be2388 | -12.41236 | -44.72341 | 2025-09-10 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c39dfc01-3ef3-3d90-9c09-04a50065be30 | -10.01893 | -48.09948 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab91df1-ff35-38b8-b45e-8b88bda73894 | -13.01455 | -48.01466 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 994ecb62-9af2-3130-99b2-2da40098c477 | -11.93797 | -51.08249 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2f52ba1-887a-373c-bbc8-f4a7445fbc9d | -12.28013 | -53.90871 | 2025-09-10 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83d6f739-0767-3233-8da4-796951b84dab | -8.48514 | -47.30307 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b29cc547-3b39-3149-8a38-3e8f89c26cf3 | -11.20385 | -54.99326 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8912d30b-090b-363f-94a4-9aabf7a0cda1 | -9.21454 | -50.52953 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8253c541-4467-39ff-b8df-d3dfcef59156 | -7.48744 | -54.95559 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d58678b-d9f9-3c6b-9db1-4d8306c939c9 | -7.8684 | -46.03692 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3ad34d0-febb-3811-a62d-eae62b534d37 | -9.31435 | -46.7334 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f272c095-2ecb-3c22-8c46-99a9a9ba1a7b | -6.87717 | -47.89922 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6a0a1f9-210c-346b-9221-af60b569ce63 | -6.68292 | -51.4133 | 2025-09-10 05:04:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e85d49c-e396-3a76-bdad-9b23f017db65 | -13.01682 | -48.04144 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 422627e3-f7ff-3d59-a209-d0778c987252 | -9.07122 | -45.7072 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6f8a44e-5664-33f1-95d9-75e40d192803 | -11.76363 | -50.58332 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10aefe65-36ad-36d0-92dd-ac7ca66cc072 | -6.84793 | -47.92846 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 661e7342-e0a6-351b-a063-b843168835ca | -8.84907 | -47.26241 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df91da84-771a-3b90-82d4-6a307d3f0eed | -9.43526 | -46.71213 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46277cfc-67c5-3eed-82c8-39e7fb911471 | -9.07568 | -45.70673 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e3ad052-5517-3939-b756-02618b9a1c70 | -9.06317 | -46.97629 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4cfd7b3-1ecf-37fb-a7a2-6d31f1070233 | -8.00287 | -46.33084 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bd48eb2-2aca-33ee-ac75-bf426b0ec298 | -9.51679 | -54.64958 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 380f4269-210f-3f92-932d-283877786067 | -10.65763 | -48.62226 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 774382b6-ebbc-3654-a4c2-c40acb51666e | -8.27991 | -47.47175 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67409046-6bd2-3819-a332-9dad4bf468a8 | -7.76185 | -50.76566 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1407fce-b541-354c-9f8d-695a22c00717 | -13.15401 | -45.28283 | 2025-09-10 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e12bcfd7-62fc-3d0c-9566-281be48b375a | -8.00383 | -46.3353 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fccd1f0-381c-31c9-8f07-801b94ba9463 | -10.02726 | -51.67141 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5d14eb1a-2c2b-3b48-8302-0d9521631ed1 | -7.5487 | -44.6664 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cec420b-eed8-33dc-bab6-7c612733b6d2 | -12.20364 | -53.86801 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 939079dc-c787-3156-8093-9147fe6a60c0 | -9.66267 | -46.64772 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66285f2a-2bfe-3313-980f-a4a75101d8ae | -7.78342 | -46.04979 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fade6070-deb8-3b0e-9c2a-d7a94e96a11c | -11.46265 | -43.6384 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c907b82-ee75-3866-bc12-8dd96e68f6d0 | -10.88112 | -55.70148 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db2c86f0-fce7-3655-a833-db914bb7aa17 | -11.21815 | -54.99144 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab6f3d55-ef9c-3566-8e28-606f47cd668a | -9.06953 | -46.97005 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00af6ae2-f1db-30b1-abd9-834a0d5b7fd0 | -9.52079 | -54.64632 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d55b76a-973b-35ee-89ae-37ad14d78a33 | -8.98477 | -45.72613 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c120d5ea-5ea8-33df-8e77-a5f49a63ffbf | -10.00954 | -48.09207 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c296e951-5fd2-3ee9-8ba9-7a958f2725d0 | -7.66896 | -50.27239 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89ff2d24-d803-35da-a28f-560cf6230f45 | -10.1605 | -48.8773 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db9d02be-dd98-3146-a914-d465babf1dce | -11.67309 | -46.90738 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 151bdbae-d981-356f-a8df-373739967e92 | -9.06764 | -46.98424 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d91607c-6b24-31c6-b173-e0699e131a80 | -11.66135 | -46.90958 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c9d9d6a-24bd-3b40-a228-046bbc47c6b2 | -9.60203 | -48.04093 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f4ddfd3-e976-31bd-a6af-a83a8cdd6049 | -11.67586 | -46.9058 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b678a44-5e6e-356b-95fc-7d5c49316002 | -8.10437 | -44.85409 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15e1037a-d566-3618-a236-b99595e4a015 | -9.35101 | -46.49856 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcec949e-0dd2-3058-b6bd-42406f1f6090 | -10.15254 | -64.24903 | 2025-09-10 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87ef3c61-a7b1-3ee9-900c-1155387f417e | -9.07523 | -50.47585 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a1d0a43-766b-31d7-b438-82905c1fcddb | -6.34092 | -47.09778 | 2025-09-10 05:04:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc51ed18-65d6-3ada-818c-15f96bc9676b | -11.42069 | -43.57482 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad28bd5c-b558-3542-b210-c05baa72503d | -9.6751 | -46.89294 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f607e0e0-1688-365d-a7fa-62b5870c6386 | -10.26981 | -48.82206 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7fc6dfb-2e6e-3e5f-8e48-a9e721deb35b | -10.88392 | -55.69836 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8299df8c-8802-3a1e-bc7c-2dd18ffd4d84 | -11.46608 | -49.25106 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03dce3d0-b357-3ad3-a938-f1b9b3fb4a71 | -13.01864 | -48.04094 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5fc2791-e1d7-31a8-b365-619286555664 | -10.00223 | -51.70383 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890b0a7f-dbf6-30cc-ab1e-d1c7555234f5 | -8.78607 | -44.41319 | 2025-09-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25219a32-c1bc-39fc-91d1-fc0a8914bf6b | -7.73666 | -50.73616 | 2025-09-10 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62394fbf-d7e6-3ed7-96ef-70261f60df61 | -12.20064 | -53.86321 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e63ce461-2123-387d-8b3e-c7d1ca074606 | -12.47815 | -53.8299 | 2025-09-10 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a65a811f-cfef-335c-a91e-5ee78af1f186 | -11.67633 | -46.90215 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca62687e-5423-3792-8877-52fcef23a2a0 | -9.34494 | -46.75616 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c57ef18-ab55-365d-bc7b-162d39b59d48 | -11.66974 | -46.90884 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 816a620f-10f9-3d64-a198-9586c5985745 | -11.21759 | -54.99521 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74bea07b-e565-3d88-9e03-b4d9558bf02a | -10.38056 | -50.53848 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd4c2c14-cbd2-36cb-8b65-6aa209a73050 | -9.09765 | -46.98011 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4516674b-c536-30af-82ee-5e2b0038e1be | -9.69133 | -46.81008 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac58b5b0-221a-311e-99cf-c1339105aaa7 | -10.72136 | -48.29519 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eab9509-277d-33ec-bade-711326fce176 | -10.88168 | -55.6979 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d77a88-7c49-39bd-b020-10a5aca61a37 | -8.03372 | -47.2798 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15f79522-5c19-3bcc-9dcd-f64640ebc530 | -7.66475 | -50.27157 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03863d76-9091-390d-918b-67d3c55fb30d | -12.08311 | -45.47519 | 2025-09-10 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b040c1d1-be5a-359c-b705-8a15d18ac4e2 | -10.38866 | -50.5439 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 517e9d26-b0c5-313d-9716-b84ef5e272ac | -7.81527 | -47.50526 | 2025-09-10 05:04:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e0e593-7468-318d-97dc-1c9e0148c588 | -9.06309 | -49.81555 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| adff3f3c-4e8a-3be4-9be9-5e82f9194124 | -12.05052 | -51.04735 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 15365322-8184-3190-859e-d4e376fdea12 | -12.82335 | -52.93914 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60eafba2-5012-3fef-a983-c70a109a5c69 | -10.71827 | -48.27937 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ec82772-c0f7-3f4d-96e9-eaeef099b099 | -10.72175 | -48.29224 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7114447a-1249-3d26-a7c4-8a7816135f60 | -7.79262 | -46.06721 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d517946d-c70d-358c-b469-01fda8850b90 | -7.98754 | -46.32962 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README96.md)
