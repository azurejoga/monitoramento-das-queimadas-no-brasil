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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d2f3da9-586b-3f91-94e9-6bd1fc3b522b | -6.7213 | -44.1387 | 2026-09-23 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| db88431d-749a-3b85-a6a8-1bc1b213ff07 | -4.0925 | -62.0874 | 2026-09-23 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 797f6d3a-6482-3906-827e-e844facf9765 | -5.7752 | -45.128 | 2026-09-23 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1466d33d-c091-3ac3-9caf-fb3bfb741a5a | -11.7278 | -50.915 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6e5d386e-28cc-3aa7-8897-fecd2f0048e7 | -11.3232 | -51.3414 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| db86fae3-69c7-387b-9854-e7a89dbafe7c | -3.2128 | -46.9602 | 2026-09-23 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 91f5ac65-33d5-305b-ad3b-d17de445c5fc | -8.4799 | -57.6085 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| a51ffa2b-bea0-3696-8d7e-10f2950d8878 | -8.1876 | -54.7219 | 2026-09-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8628bd5d-f5af-397f-ac0d-c1034422da5d | -8.9165 | -61.4767 | 2026-09-23 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 1992e0bd-141d-3527-820f-075869bae3c3 | -8.4983 | -57.6271 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| c05a6002-0abc-3644-9bd3-65ebc9589186 | 1.7846 | -56.0393 | 2026-09-23 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2e39b0b2-9486-35a3-a786-d2fe6cec8195 | -6.3105 | -43.9426 | 2026-09-23 00:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e64fdf66-ffed-3273-b12f-5062e9c699ac | -15.6574 | -43.527 | 2026-09-23 00:20:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ac32be9f-9c48-3ea6-b668-633258eca2ba | -6.9401 | -46.5648 | 2026-09-23 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ceaca626-94dd-360c-ad5d-f7c95664882b | -5.7565 | -45.1293 | 2026-09-23 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f31d2b2d-7064-3876-acca-7f971a3f6990 | -8.5982 | -54.6341 | 2026-09-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 7740720e-4a8e-36f3-bda5-f19454f97f42 | -11.3976 | -44.2167 | 2026-09-23 00:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 2d5533df-f4a3-3fb2-827a-31c50e65a826 | -8.4797 | -57.6282 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f2cd0b5f-1560-3063-8e31-37be23812575 | 1.7663 | -56.0395 | 2026-09-23 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a13e8ec8-c8b1-3ab2-b158-20370296469b | -8.4726 | -48.6927 | 2026-09-23 00:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7973d6f7-907d-3e69-a21f-b4ff9bf97377 | -3.6947 | -60.5645 | 2026-09-23 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1eee51e1-d01b-38ea-9ab7-12f31edce127 | -9.0839 | -61.4308 | 2026-09-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ea56e178-c138-39d6-9829-cab40422b223 | -8.4538 | -48.6944 | 2026-09-23 00:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 30a5be75-114e-3cdb-bc32-88062396ddde | -8.4985 | -57.6075 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| e8325396-a81d-3d5c-9566-dfdc270ea375 | -8.9164 | -61.4958 | 2026-09-23 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| f785de8f-1729-3883-a4e0-5069ca882c03 | -5.7567 | -45.1067 | 2026-09-23 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 450a177c-bce1-3aee-8004-dfc133947ad2 | -4.0925 | -62.1062 | 2026-09-23 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 32f47e72-121a-357d-a5e9-39973572b95b | -8.2062 | -54.7207 | 2026-09-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 20109dab-e6db-399c-bf7f-6f47edc38f56 | -6.6776 | -58.5554 | 2026-09-23 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| e8d8ac66-a45d-32eb-92cf-f4f9e891d0ed | -11.7088 | -50.9172 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| da3d0e14-68a0-3c0e-b88f-2ce740d34aaa | -6.9214 | -46.5663 | 2026-09-23 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| a70c7574-5ee1-3b35-8d65-79700d951b7e | -5.3451 | -45.1803 | 2026-09-23 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 706bc8ef-6ac6-30a6-b66c-d756230aa2e3 | -3.4597 | -59.5783 | 2026-09-23 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| de393a47-0445-37a5-b871-4fe1cd208812 | -8.935 | -61.495 | 2026-09-23 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7aa49d8d-fbf1-3ce0-9684-d7103b43d164 | -6.6129 | -43.7317 | 2026-09-23 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 91548486-c92b-34a4-a955-9f0d99911dff | -5.2475 | -48.1941 | 2026-09-23 00:20:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b07401a5-1f78-3d9a-a1dc-3421b018c39e | -3.6947 | -60.5455 | 2026-09-23 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c0e583fd-5e8e-32be-9d25-b955a332359c | -6.728 | -59.423 | 2026-09-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 4bc04326-0692-3004-b0f6-1d4455dc1a1b | -6.1289 | -57.7613 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 330fa4dc-5994-3f0c-8ee9-45a719cba823 | -11.304 | -51.3646 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 4bf9c852-2dc6-3dc4-9f66-f8869fed1c9f | -8.791 | -60.8127 | 2026-09-23 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f5b5718a-41d4-38e4-9978-2aacee32efaa | -8.8275 | -50.482 | 2026-09-23 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 696d5d1b-393c-3cb9-bb4f-ab6740764df6 | -10.6094 | -53.9902 | 2026-09-23 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 4b801eef-0603-3775-9a74-e8c7f5501a1e | -7.8811 | -61.1779 | 2026-09-23 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d0c0b611-80d2-3c38-921c-2f0e7bcb6ecf | -10.5091 | -44.8517 | 2026-09-23 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4b5071ae-9e1f-302c-bdd7-eb4903f501e8 | -3.6763 | -60.5839 | 2026-09-23 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| e1609ae0-c7ea-36c4-9f80-90a0d5bed098 | -6.7211 | -44.1618 | 2026-09-23 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 01206fb1-c8dd-35e2-82a2-31f649b7c460 | -4.4488 | -55.0662 | 2026-09-23 00:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f1bd7c26-c33b-31c1-b7ab-7d92b3fa99c1 | -10.5087 | -44.8748 | 2026-09-23 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| f7fc094f-2451-3cf8-9ebf-897ad2ea6de5 | -8.5796 | -54.6354 | 2026-09-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 45515bad-3f9b-310d-8697-ee335b9161a7 | -5.3453 | -45.1576 | 2026-09-23 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e3b18f22-2c07-3dd5-be54-90ad7cb07e56 | -6.6775 | -58.5748 | 2026-09-23 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 48cd9df4-6a4c-39d0-9589-ed91d71a204c | -11.7784 | -50.0743 | 2026-09-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| cd784e6f-0447-3af3-8865-a1885a77c34a | -6.6317 | -43.73 | 2026-09-23 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fcd95cdc-f26a-3a3c-88bc-65d921d445c3 | -6.0925 | -57.6847 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| eef23348-187b-33eb-b0c2-8b1181c215c8 | -5.7567 | -45.1067 | 2026-09-23 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 94bdf9b6-745d-3e8a-82e9-e212cac23cc0 | -3.6946 | -60.5835 | 2026-09-23 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f7f6e430-81f9-306d-a84b-155b2e6b5251 | -6.5939 | -43.7565 | 2026-09-23 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| d56d781f-042a-335a-9c56-ad34ac9e851d | -11.7085 | -50.9385 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3b41ccc0-cea7-345f-bf1e-a6f714a9d4f5 | 1.7663 | -56.0395 | 2026-09-23 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 956d43e2-582f-3e50-9cc9-195a501fd9f9 | -11.7275 | -50.9363 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 63802943-798e-390e-8f33-d84d9d05fdaa | -15.6574 | -43.527 | 2026-09-23 00:30:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a583d410-f9a8-3cd0-b770-8bfe5f846b52 | -11.6895 | -50.9406 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bf954727-0fbc-39a5-9e12-f9d112f6a1aa | -3.2579 | -53.9613 | 2026-09-23 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7be6ee97-2740-3e5a-84ed-b01f19b8381e | -14.6497 | -45.6367 | 2026-09-23 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fa18b6ce-70d2-34e4-8497-fc57cf976d87 | -3.2129 | -46.9383 | 2026-09-23 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| bd4cc483-6cb3-31a6-aa0c-6f8729af752b | -8.5982 | -54.6341 | 2026-09-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 7670fe27-9d34-3891-9334-44965a37efd2 | -7.0352 | -44.6396 | 2026-09-23 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f288f016-1f7d-306c-8cd4-2ff485bf4f9d | -8.9165 | -61.4767 | 2026-09-23 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 1870e39b-6998-362c-98a9-26f49db6e5f6 | -4.4488 | -55.0662 | 2026-09-23 00:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4fae3f8d-6948-309b-983d-2b0f217248ea | -10.6283 | -53.9885 | 2026-09-23 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 8479893e-9373-37d5-8355-638d1e537d52 | -11.3043 | -51.3434 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 7898531a-e2bf-3cc3-8c9c-f8d67d1de929 | -4.0925 | -62.0874 | 2026-09-23 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 00a8cfe3-fbba-3277-a92a-ea916c8be10d | -6.728 | -59.423 | 2026-09-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b9256d39-23e3-3143-8bd0-38bd16512d72 | -8.4799 | -57.6085 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7f13b267-5a67-36ce-9055-7a981c9434a2 | -6.1111 | -57.6645 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| daab9823-55ae-344b-81c3-0ad2cd6b1a09 | -11.7088 | -50.9172 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 997d7bd6-7db8-32e8-902e-af6e40d0363d | -8.4985 | -57.6075 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 6d0d25af-fdb9-3a61-9e03-008794d4fd1c | -5.7754 | -45.1053 | 2026-09-23 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| bcfdf8c8-2eed-313e-97dd-b108b506d04e | -11.4168 | -44.2139 | 2026-09-23 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ecdc8393-f3bb-37af-9c3b-1ee96192b482 | -4.0925 | -62.1062 | 2026-09-23 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e55fd118-2b5a-3a91-a53f-8c6a6df1070f | -9.5332 | -45.3633 | 2026-09-23 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 8ddadce0-8c3c-3895-bec5-5280c2a297ee | -8.8463 | -50.4804 | 2026-09-23 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ba07c740-b7b0-3700-bab8-3c20734f9f99 | -8.9351 | -61.4759 | 2026-09-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7299d9cc-0e86-3a12-a054-8162c1dee122 | -14.6302 | -45.6403 | 2026-09-23 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f4d915de-26cc-3da6-b705-7777c2a787a4 | -8.4538 | -48.6944 | 2026-09-23 00:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 0ae7e592-e588-3ae0-9ee2-f71b8a9a6d7e | -11.3976 | -44.2167 | 2026-09-23 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 14c13464-92b7-3a60-9f11-456b906ca28b | -6.3293 | -43.9411 | 2026-09-23 00:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1b033298-9def-3cf2-a349-70a9b9780d29 | -6.6775 | -58.5748 | 2026-09-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 14632043-19db-3427-9e96-dd39345175a1 | -8.935 | -61.495 | 2026-09-23 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 765de76e-af62-3769-8ed6-ebd264938df5 | -6.467 | -59.9902 | 2026-09-23 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 3afd355d-1357-3376-85f9-ea60dbf5e5d9 | -6.6146 | -59.9272 | 2026-09-23 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 876e71ad-68f8-371a-bcbf-388537462202 | -8.4726 | -48.6927 | 2026-09-23 00:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 92.3 |
| b5a640a6-91aa-3acc-9858-4a855ca8a5e6 | -8.5796 | -54.6354 | 2026-09-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 17bc1e66-ca2b-340c-a8ba-2f0ccb6c091b | -5.7752 | -45.128 | 2026-09-23 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4657c03a-5ba0-3bd3-8639-6794bd515964 | -12.4024 | -46.9579 | 2026-09-23 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 7c4feeba-a484-3b4e-8d5b-302bf9a77520 | -6.9214 | -46.5663 | 2026-09-23 00:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 31d3de52-9512-39ad-a4c4-f52bffbec960 | -6.0926 | -57.6652 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 5fbe9f1e-0373-38dc-8760-4c8ba62a54b5 | -12.402 | -46.9804 | 2026-09-23 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 299f1fda-f992-349e-9c11-cf67ca59ccce | -12.4212 | -46.9777 | 2026-09-23 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |


[Clique aqui para ver as próximas entradas](README10.md)
