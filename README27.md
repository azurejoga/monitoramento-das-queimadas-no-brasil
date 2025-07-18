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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d311a3ae-e6f9-3251-a428-6d5adda39e68 | -4.11112 | -48.21019 | 2025-07-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 863566b9-7d35-3d38-b8dd-8eefc28b992c | -7.4909 | -63.81535 | 2025-07-18 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df9f766c-12b0-3955-9c44-59fd7c835fb2 | -9.01435 | -59.53662 | 2025-07-18 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e90af536-4d8c-31dc-815b-879547910fb2 | -3.39578 | -47.48355 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3c79bcdc-31fa-3977-8f5a-d6d0a34fa2bd | -3.38372 | -47.48196 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 49d7c191-efcd-3f62-ae96-d67c367094d9 | -8.87379 | -50.1546 | 2025-07-18 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ee5896a-61b4-3704-9dab-646ea297ff8c | -4.48189 | -46.07314 | 2025-07-18 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6cd2d72-fbfb-3436-9f7d-0b7bf88d07eb | -3.3844 | -47.49113 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 80d10608-ad83-3f53-9a2a-5882b41ba57d | -10.71985 | -49.48973 | 2025-07-18 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed15d905-66fe-33f5-a736-eae5dfaa9e7d | -7.82696 | -63.29644 | 2025-07-18 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dc16b57-775d-3f06-8a78-62ec4aa38cd4 | -3.39442 | -47.49247 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 076792d6-958b-347f-bfe7-7d458918bdee | -3.38974 | -47.48281 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a5fa6e15-54f0-303a-8d58-96d7c62c7800 | -9.24336 | -48.56063 | 2025-07-18 05:16:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd3d1f8f-fb04-372b-b630-d57613035551 | -3.39514 | -47.50178 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7294eda-285c-3afc-ba93-06cac3ee58c2 | -3.39836 | -47.47953 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0939b88b-ceec-35f8-b7fd-80b81c5c8536 | -9.27513 | -49.63789 | 2025-07-18 05:16:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e1e160b-0258-3e67-ac07-6da4ab82c221 | -10.65808 | -49.37069 | 2025-07-18 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5028b94e-3070-3bde-bacc-b7abc9caeff7 | -3.19454 | -60.60841 | 2025-07-18 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3907edd2-613f-3aa7-885b-517b146467dd | -8.0398 | -50.08181 | 2025-07-18 05:16:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 327af740-2dc1-312d-b4d0-ddabb2c40592 | -3.3824 | -47.49072 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0d190da0-cd01-3933-b798-8ba1e57320dc | -7.71093 | -47.29114 | 2025-07-18 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a8ef621-4371-36da-a173-1b4d328cfa35 | -9.50719 | -47.56464 | 2025-07-18 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| adbb3655-53e9-3156-9cf3-74849cd7c392 | -3.38502 | -47.48677 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 65703fbf-57aa-31d7-bceb-b8c91abd174d | -3.72933 | -53.7846 | 2025-07-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d13344bd-105a-3ecf-ad08-f386a5dab2c1 | -3.86141 | -50.08315 | 2025-07-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6af08394-10d7-3677-b26b-8300fbd2934d | -9.76771 | -48.7574 | 2025-07-18 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 33418a99-d0e5-343f-926a-5faadb541edf | -8.03856 | -46.62391 | 2025-07-18 05:16:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 454f06f0-b5d1-35e0-a1ce-0c97220e1692 | -3.39104 | -47.48761 | 2025-07-18 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3ba5ebcd-0496-3256-b0ed-ad70f9917615 | -5.19804 | -45.48623 | 2025-07-18 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 541162b9-5122-3f9b-a3e4-91bca9c3ee97 | -12.03452 | -48.76653 | 2025-07-18 05:18:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93755de9-a098-30f3-8482-239b8cae7bbb | -10.89968 | -49.21191 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2049665e-7baa-38aa-beba-c66a2097d5d4 | -10.05031 | -59.10202 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97411d55-ccdb-3d5e-81a4-312b68f55b63 | -10.14717 | -67.72048 | 2025-07-18 05:18:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d35d1aac-1df0-3a2b-90a0-09e35e402856 | -12.42571 | -50.01715 | 2025-07-18 05:18:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4da143d5-db9e-3bf3-b9d5-d775e27410f9 | -12.42621 | -50.01306 | 2025-07-18 05:18:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db3405ec-1ad2-36dc-87ee-1633b66a9ffa | -11.5632 | -47.07631 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5702d4b0-a0be-3e48-83dd-b0d77072697c | -12.03562 | -48.76871 | 2025-07-18 05:18:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc27d6e5-5e2f-3afc-a8c6-81d3a6f628fd | -11.74163 | -48.1976 | 2025-07-18 05:18:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 861f716e-8414-3a4c-b67f-1b33a4075480 | -11.46298 | -48.16224 | 2025-07-18 05:18:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5786144-a21a-33ea-8a34-617387a43937 | -10.06084 | -59.10006 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae61a54d-b1b9-3a2a-9597-321e0f337a9b | -16.42091 | -53.16178 | 2025-07-18 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5a35b6a-4faf-39c8-9809-448f9f558802 | -11.56913 | -47.07535 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f87135a-0bcd-3905-b95e-c8c8295b7fb1 | -12.50151 | -57.77953 | 2025-07-18 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a84af5-8bbd-3b1b-bf6e-42d0338cc7c5 | -10.90021 | -49.20743 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07a9068f-95a9-332e-b2b4-e4f2b6ec6c2c | -10.50798 | -62.40915 | 2025-07-18 05:18:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54d93595-b2af-37a2-acf1-69de358b337a | -11.46162 | -48.15953 | 2025-07-18 05:18:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36a04e7d-c54b-3e95-9603-96883240c1b8 | -11.5625 | -47.08274 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4457b4be-7406-382f-8b30-1ebbb8b95bc3 | -12.43655 | -63.69946 | 2025-07-18 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c13fdefd-c0a8-3333-a11c-c6a6fc8c5c04 | -12.42635 | -50.01577 | 2025-07-18 05:18:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f040707-723b-35fb-837d-a7af12862624 | -10.29902 | -60.54405 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 570230f9-f7c7-35bf-b01c-8d7e1b91d34f | -12.38895 | -50.38325 | 2025-07-18 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cacf2890-7df2-324e-8d9f-7ed27c62f967 | -10.28757 | -60.53146 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c52ef29-1d00-3a44-8627-fe16bfabc627 | -10.6797 | -56.54942 | 2025-07-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1f68788-e6b1-3811-8be8-2b5b3535aedb | -9.46559 | -62.19783 | 2025-07-18 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41a1e5be-1509-39b5-b0b2-de85653a693e | -11.56935 | -47.08357 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ad4c5a44-9e43-3788-b956-eeda965d27b0 | -9.71102 | -61.28863 | 2025-07-18 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddef5124-0ff3-3150-8bc1-9448def4d2c5 | -9.43194 | -61.99041 | 2025-07-18 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fdf0c11-114f-3441-8532-b930ab3e1031 | -9.62867 | -61.45471 | 2025-07-18 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03bf236e-7c45-385e-ab8a-f2376cb6fa17 | -9.88484 | -65.15982 | 2025-07-18 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9308b38-61f9-3e48-a570-2a0152a048a7 | -11.88271 | -58.71732 | 2025-07-18 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920e18cc-34ac-3d48-8248-f1eabdc6478b | -14.14899 | -51.03042 | 2025-07-18 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12c1e57b-13c4-340f-860c-f70904f6a15d | -10.82066 | -49.28775 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ee6cd20-df5c-3661-b47b-8b86364a45e4 | -12.49798 | -57.77901 | 2025-07-18 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa0e7fad-782a-3221-8c90-93fb9b0549e6 | -8.97232 | -65.22458 | 2025-07-18 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fb4cc73-d9e3-3809-a3bc-3e493f88c219 | -11.16359 | -46.25592 | 2025-07-18 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cbaf5ed-ca3b-3883-bbe6-3a54a0b675f2 | -9.71439 | -61.28918 | 2025-07-18 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c2784cf-4aca-3f97-9612-07443cb94dcf | -12.46162 | -57.87978 | 2025-07-18 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 157b1f24-ad0b-3b1d-964d-ef7813fbfd6f | -12.57791 | -56.96993 | 2025-07-18 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b7fca20-af3d-3b90-b0dd-f30a8f6bfc7b | -11.57373 | -47.09566 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fcdc315-fbf2-3677-89ce-93ad5a33cf48 | -9.71544 | -62.33735 | 2025-07-18 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed8232f-9e72-3b51-9d3a-cd7821c93274 | -11.56838 | -47.08186 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2fb32506-1cb1-33c1-94e7-0aa9d2cb8abd | -10.90283 | -49.20918 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5bc8015-0c60-37bf-bd98-47cb97daf90c | -12.58096 | -56.97489 | 2025-07-18 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c173d3ef-240d-3be7-b7ea-28e20aa2fe69 | -12.65965 | -47.09341 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 942ddca2-2f48-32dd-a2dd-6684752435e0 | -11.57447 | -47.08923 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08d62912-8153-3550-bf5f-5840683a8ac6 | -11.73521 | -48.1968 | 2025-07-18 05:18:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7595a90c-082c-39ef-ba8f-5947e04a563c | -12.37567 | -50.35002 | 2025-07-18 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5650c780-68d4-3352-a5bd-e8dca706da15 | -11.56153 | -47.08109 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1b8cf2d0-44c0-31e3-87ea-cff433d8ed50 | -12.42588 | -50.01986 | 2025-07-18 05:18:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc98bb14-6b77-3eb1-a09f-e69ad3225155 | -11.56108 | -47.09587 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e14e6472-1fb0-379e-b3e9-0812e34e54a7 | -10.29571 | -60.5435 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c6ea270-aa48-31f7-97c8-f2166349f42b | -14.32925 | -59.89739 | 2025-07-18 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dbd456c-9052-3b16-aad1-b26b7d75b42d | -9.88357 | -65.1671 | 2025-07-18 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1572f425-f8f1-3a46-96c6-f27530f2da9e | -10.68141 | -56.54257 | 2025-07-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98ecd823-08c0-3c0d-b1df-11c557abd9bb | -10.14236 | -67.71962 | 2025-07-18 05:18:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef53aed2-3faf-388e-bcd0-cd06472ea381 | -12.39033 | -50.37161 | 2025-07-18 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58429195-1ba8-31ee-bfb4-186a3e416524 | -10.05751 | -59.09954 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9689ba15-6394-3f4f-a511-08d141b67567 | -12.47626 | -46.92174 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0fb66a2-0a1a-3dc9-bbd8-077d6eb1d75d | -11.57549 | -47.09095 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e76bfc12-105d-3a4d-9119-5978d9dde113 | -12.44016 | -63.70011 | 2025-07-18 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02d53951-7bbc-3521-8012-009e1f4b44c1 | -11.32277 | -55.21172 | 2025-07-18 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62d4619e-5ca9-39ce-a484-9c27f9426751 | -10.81686 | -49.28933 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f6ab6e9-1b4d-3039-bbab-8084453842a3 | -10.8969 | -49.2081 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df55c25a-c293-395b-bc7a-c0eb6a979c80 | -12.03001 | -48.76286 | 2025-07-18 05:18:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f53e1b21-c727-326a-b598-916aa27e6391 | -12.66688 | -47.09243 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18acc5c5-e80b-39d8-833b-c3a39b3aeeeb | -12.03622 | -48.76371 | 2025-07-18 05:18:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef17f175-2c8b-3abf-9a94-c8e8f1005f39 | -9.88764 | -65.16781 | 2025-07-18 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d26b20dd-00d7-32a9-963d-357ecce738a3 | -10.58193 | -62.36147 | 2025-07-18 05:18:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bdfff3f-7ddf-30c4-853c-22557bc7e2da | -11.88326 | -58.71362 | 2025-07-18 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1073fc0-0503-3e8f-87a6-c59711180d9f | -12.65897 | -47.09986 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README28.md)
