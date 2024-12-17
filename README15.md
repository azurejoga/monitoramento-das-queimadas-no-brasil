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
| bbb6e280-4032-32c3-a54b-00d37610c654 | -4.44413 | -44.728 | 2024-12-17 04:21:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf327374-48c0-3769-acd2-c5a77049fbf7 | -4.37838 | -46.55042 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3173515-0a3c-3c8d-8f97-dd5e4e60bdb0 | -4.40387 | -45.52614 | 2024-12-17 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fab0ed8f-38b1-3ff0-8aa7-bded26143e2e | -5.44713 | -45.40381 | 2024-12-17 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 855a4d0e-eae0-31ae-83fc-580b38b22cd5 | -4.1018 | -46.698 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b87fe8ec-e7cd-3706-b8cf-f1061ff77b39 | -4.06972 | -46.72054 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc95bbcc-2761-3b33-ac2c-519d03714091 | -4.10548 | -45.26019 | 2024-12-17 04:21:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a42a641c-09a0-371d-8307-0a649eeeecbe | -4.56958 | -46.58392 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f2f616a-30c2-3e3e-8313-fa747c28d73b | -5.09806 | -43.91519 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f12fee76-8bcb-351a-950e-e229f9197a89 | -1.4648 | -46.81172 | 2024-12-17 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5356de82-d5f6-35bd-bc2f-48fdc9cd73a5 | -4.56655 | -46.51462 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e70d2c7-3e04-31e1-ac95-e6a2607d6d84 | -2.69497 | -46.60264 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e3daee8-89f0-3976-a903-5dd15a67348f | -2.58711 | -51.92167 | 2024-12-17 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e0fb6d-155c-362f-a2f5-6f6030ab4941 | -3.30175 | -53.37317 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b8e0a2f6-1748-331c-b8d5-84b1fcd684f2 | -4.96236 | -43.71598 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e7b2f0-ff67-39bf-8db7-bf9f3b6d49f5 | -4.20324 | -46.48196 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b00b496-b553-316f-add1-9b4e7b1dac9a | -3.75425 | -48.00314 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b411443b-75b6-3378-8629-19cba39d35d5 | -3.30234 | -53.36972 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0a4f5bc5-2879-31d8-b4c6-2ca72ac434dd | -4.00722 | -46.90061 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3adbde3-affe-3bd8-986f-26b39f7c4dee | -3.92162 | -46.91927 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35bf595b-5fba-3ade-882d-fbf654862973 | -3.95851 | -47.02605 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b45ece14-49b1-385d-af5c-b94a5ebdf58d | -3.77193 | -47.1741 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3495e6-0e4c-38f8-b76c-c22bf612fa18 | -2.66022 | -45.55971 | 2024-12-17 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f23d557-26a9-36c6-989f-8008c0bfa4e2 | -1.95859 | -46.48829 | 2024-12-17 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d0e602e-4027-3024-949d-2f3c3f603213 | -5.09582 | -43.90773 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3a4a91e1-c5fe-3979-a769-4aed3eb5182c | -1.46384 | -53.47972 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efa40501-4fbc-385a-94a7-c6bc82700010 | -5.39385 | -40.66328 | 2024-12-17 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f553d194-75d5-33cb-bd89-d37a85467fd4 | -3.77284 | -47.16515 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48c371d4-6a17-306c-a5e3-e4d20f6d7874 | -0.7519 | -47.75766 | 2024-12-17 04:21:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c17b661e-1030-30ad-9a6b-3766fa34079f | -4.08811 | -46.60636 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80ea6c10-a8d1-3fd6-ade9-2a1a18787ed0 | -2.61799 | -46.78867 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30b5f837-6757-3cad-9d34-e33656979e30 | -2.05475 | -46.65972 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 698cba31-100c-3f71-b703-80096ae9d621 | -1.52317 | -46.04872 | 2024-12-17 04:21:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3de5149-e90e-33fa-b58e-a8d68e0c2402 | -4.06228 | -47.10283 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6bdf8c6-d66e-3bb0-b115-faa3ec99e1f8 | -5.09088 | -43.91765 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c6e0fd8-c18d-31d4-878f-b45a0020c19b | -4.52676 | -44.04631 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b21f2f53-6201-3ea0-ac05-d9c7be9a689c | -5.082 | -43.90918 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9adf090-3f07-3ae1-946d-641f1351a1cb | -1.27446 | -53.03622 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14271530-f351-3e63-91ce-458f02fb7c5a | -4.2513 | -45.99905 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371a1feb-2d53-39b7-b2e3-469abdcf258d | -2.57253 | -45.96006 | 2024-12-17 04:21:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae624425-181a-3aed-a013-e28ef53caf55 | -4.70865 | -44.385 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79ceba63-332a-318b-8e45-95d039015e7d | -4.79311 | -46.39392 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 16b1e708-8660-3d0b-ad87-bed365e4d468 | -3.92891 | -46.89644 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d472d4-e771-318a-8051-569929f92b9e | -5.06399 | -43.95975 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adccb615-40c7-39e1-96b8-e9a8ab986831 | -4.07542 | -46.72933 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddbb9f0-b896-312e-8b67-ce9981cd611c | -3.75494 | -47.99877 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e4cf55a-19c2-34d0-adfe-f3936cb61b9c | -3.97606 | -46.91594 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a10f9110-9837-3acf-8699-f534b6b30230 | -4.96768 | -44.96907 | 2024-12-17 04:21:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de79b6f9-11dc-356c-9409-d5a092ede3d5 | -3.18753 | -46.69366 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c15b6108-07e7-36c3-954e-98dae00763a3 | -4.67764 | -44.03778 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00824561-49f9-3d65-a103-062ca64f7311 | -4.88829 | -44.16993 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e42d5b-6763-307e-8354-c313b293fd20 | -4.10422 | -46.68287 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a3a9ab9-4e93-339c-9b3a-d62d666f9f8f | -5.2171 | -43.29979 | 2024-12-17 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a45a6466-9416-3cf0-b302-77d0c9b8c32b | -2.76347 | -47.39505 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08985f04-d0b7-3956-a679-03a625e6e3f2 | -4.79937 | -43.77966 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 586bea28-2b0c-3935-aeb1-bb80a99ddb83 | -4.39793 | -41.43502 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b15e035-4a5e-32f4-8979-ff07a077db06 | -1.66623 | -48.08704 | 2024-12-17 04:21:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 864e2765-c733-3437-ad30-33ff297dedb7 | -4.90203 | -42.07736 | 2024-12-17 04:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5e0faf17-2fcb-3506-96d7-b365ba9cbfe1 | -1.46338 | -53.47963 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d4279c8-a372-347d-a95c-409e1aba9037 | -4.57992 | -46.58543 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8ed5580-c041-3d1c-8ac9-1e43e39b6b78 | -4.65512 | -44.33433 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fdb4c72-c35b-3875-ae6f-6b0418d5d096 | -4.65565 | -44.33089 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a023d38b-0e16-3684-acd4-2f267490606a | -4.54865 | -50.28277 | 2024-12-17 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82389a3f-0a08-312f-9473-16dfc0256727 | -2.87703 | -45.24343 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb3d3d88-bab3-385f-a254-361bc8951b72 | -3.15352 | -45.97016 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 768c9f6d-fc6d-3a88-aeb5-0550b81098f2 | -5.13756 | -46.15265 | 2024-12-17 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff61038c-2cdb-3a43-8b69-7c42896f31cb | -1.70723 | -46.21717 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57f327fe-7d2c-359e-9933-4e0d20d6e9e7 | -4.65619 | -44.32745 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| fdec5b99-4621-34eb-a78d-2431cbac5e97 | -1.28397 | -53.18635 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc42fcd6-7110-3d19-969f-916cf488bad5 | -3.68853 | -47.14882 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3eaf1c2-2285-3be1-abfc-8484473ed5d3 | -4.07758 | -46.61219 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ae1df59-9076-3726-ba2d-ca30cc615528 | -3.15976 | -45.97487 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 773a4879-9b9f-3fac-b369-aff89f2ef685 | -2.32914 | -45.78718 | 2024-12-17 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa41dc87-8b84-3c49-a1dd-2eeca3eeec76 | -3.43641 | -54.04618 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a79f7042-20a9-3ca5-a1be-9c21dc1c0d6a | -4.10527 | -46.69854 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29cd2a3b-99c8-3d71-bbf7-1dbbf743d83a | -5.10191 | -43.91222 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 053e520a-fc3a-38e5-ad3b-a95d5837a461 | -3.72181 | -50.16118 | 2024-12-17 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b9194b5-ce53-3fe9-a448-c205ff34db25 | -5.09142 | -43.91417 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4af1730e-0444-3a1f-b093-df429aa54fba | -5.93901 | -40.02195 | 2024-12-17 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb595ae5-fd3b-3934-bc3b-f3b8fc6aa5d4 | -5.55526 | -44.69128 | 2024-12-17 04:21:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7204c88a-dc34-3f6a-a23c-e562c82db484 | -3.87661 | -47.03834 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8922840c-0956-3585-bc71-c655dc7b5dd7 | -5.08147 | -43.91265 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6267811-9a91-3146-b004-864d0b173700 | -1.6307 | -45.85404 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e289dce-8842-3717-bac2-cbce440f1616 | -3.16259 | -45.97906 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d8aacb-2336-3388-bf09-de1a4140d287 | -3.23566 | -46.80452 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d38c6841-2356-3ef0-963b-f7ddbc1b7640 | -3.88229 | -44.25201 | 2024-12-17 04:21:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90842541-5412-3659-ad03-e6c95a9556f7 | -0.16748 | -51.3518 | 2024-12-17 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 247b8ac9-4cda-399b-aba1-38d378c79fe8 | -4.74594 | -42.62366 | 2024-12-17 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 398075a9-5516-3205-bdf5-8f4c25a91576 | -4.36581 | -44.88186 | 2024-12-17 04:21:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cab8561-55f6-3369-920c-f2cddd969a3e | -2.51775 | -49.05593 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cd27d84-afd0-3d6c-8943-0fa34c63431e | -1.63355 | -45.85828 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b26479c3-d101-3fc0-9461-984ab0799a13 | -4.89106 | -44.17389 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bec6486d-79fd-3a7d-a1a4-313729543a20 | -2.10381 | -45.65864 | 2024-12-17 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91df9a41-f9ce-37ba-8b90-e9c0c63a5a67 | -4.06022 | -46.91292 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7a4788c-78b7-3199-900c-5d5926171703 | -5.31403 | -46.4973 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b677186f-e82c-397b-b048-5f0dcc637273 | -5.3118 | -46.48943 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93e3e0cf-9e6c-34b1-b0c2-6752017789bf | -2.57734 | -49.40902 | 2024-12-17 04:21:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea11465d-17fe-3c62-8b25-4dc227ccc1a0 | -4.10318 | -46.66713 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b67f44f-19b0-31e5-bb50-b491a4bab037 | -5.30839 | -46.4889 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d40542b7-ba61-3ba1-bd0c-8f452774ab53 | -5.51249 | -36.83971 | 2024-12-17 04:21:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 12.3 |


[Clique aqui para ver as próximas entradas](README16.md)
