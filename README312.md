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

## Dados Diários - Página 312

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fafc130-0642-3ba9-a690-a6f672cac3fb | -8.58641 | -38.50084 | 2026-10-08 16:37:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 05a57729-0582-3108-be55-1be41afc6d4c | -11.76973 | -46.76847 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf5b3b80-6243-3021-b50e-a45124003620 | -10.47973 | -47.24901 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a4420b3e-335a-3054-a0e4-72a644252366 | -10.4439 | -46.88251 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1ec597e2-238a-332c-95f2-ffd037649116 | -6.40558 | -44.95913 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| c9c81bd7-570f-3eec-afde-4a5b542a04c8 | -8.2946 | -45.72613 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 9ff06236-0540-3f56-bfec-fa56d36bcf34 | -10.88028 | -57.10949 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 64a6f619-be5c-3f5b-b186-3ab3732a093d | -18.22791 | -42.31383 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 917b1bfc-88ca-3435-a76e-0f292034d12b | -12.15816 | -44.71761 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5245935e-9553-3eff-96f1-f4f314cda605 | -6.17183 | -44.85169 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| efbc24fd-8977-3ccb-bf6b-dcda026885be | -11.20506 | -45.21048 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2985de3d-a657-3482-992c-6458a5216ba0 | -11.21331 | -44.86346 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c29d5daf-6565-39da-a80b-c0e2f1088dd3 | -10.47309 | -47.20316 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 09397750-d67c-3127-8693-e9c5414f6c55 | -8.28587 | -45.71325 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 891e722f-fbaf-337f-8d76-c731dbe2771a | -11.27825 | -45.20147 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| dcc10561-0387-3c9f-aad9-aa465c7bbf49 | -10.52985 | -47.27717 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f51e128b-475d-3d39-ac67-49175ccd8e80 | -19.77637 | -48.53763 | 2026-10-08 16:37:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 23fc8d4d-ac95-34a8-bb00-a359006a5251 | -7.54044 | -42.08891 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 87611409-74f5-32ea-950e-d969ca38a929 | -11.77938 | -46.78628 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5c6f037-bc7d-3252-9884-62783fae54c7 | -6.84643 | -41.75434 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| c0cd6b36-51c8-389a-85be-1e9639789ce3 | -9.08406 | -45.11858 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5fc1a001-881f-313b-bfa6-ea0f7705243b | -6.31585 | -45.06023 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6ba47717-efe9-3e3d-bb52-1bdc6075108a | -10.67888 | -47.83055 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a4ee5009-427a-3606-9a43-1c412abea3c0 | -11.77545 | -45.55314 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f1c7188a-21ae-3197-bfce-17e54348b231 | -8.76804 | -45.76122 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 19eec9dc-d0e8-300e-b14c-ad5059c10684 | -8.09067 | -46.84572 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e3b95be-c98a-3588-b61e-c99a2eb77c21 | -10.48029 | -47.25283 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 597577f2-aefa-39a7-bac7-5be40227456e | -6.37206 | -45.80267 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c8e98e3f-627b-321e-9cc5-c8d43d8ca364 | -9.78054 | -45.88376 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91204b2e-321f-37ef-abf8-0e3a9146ad2b | -6.37708 | -45.79129 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fdb8a31d-7c8b-30a1-835b-b9d7e1bb577e | -7.35194 | -44.366 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 781b0f68-f541-3a3e-afd7-a5fb5c00a9c7 | -11.08916 | -44.01451 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3dd42e9-aa39-3979-9893-5a9b142e286a | -9.90067 | -44.80085 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 03d0c1c1-ee89-363d-91ce-21c9fd790d36 | -6.20902 | -41.58454 | 2026-10-08 16:37:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 0973b1fd-5e73-3830-b0e1-76ac7241b4c7 | -7.71842 | -44.73727 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c087e19c-068a-30aa-b7d7-92916763a6d4 | -18.92136 | -41.01938 | 2026-10-08 16:37:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ceddd2d6-909a-33da-8e47-e4ad9b5a46a7 | -8.37248 | -47.65822 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 994e9472-887a-3651-8c28-7b69dc11684d | -6.83477 | -39.56436 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 793dd03d-54eb-3277-9bdb-04a8f486b2d0 | -7.76783 | -54.94365 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de65e588-19de-3d49-830b-2c3d42c5dcc0 | -9.40191 | -45.89317 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1538191c-83ca-35bd-9b06-431a779600df | -6.1604 | -39.44135 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 10c00854-b164-372c-bf50-e784f639898f | -6.67149 | -45.36469 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 582280a9-46c1-3733-bc30-b89fd6326904 | -10.1759 | -48.04688 | 2026-10-08 16:37:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db01158f-63dc-3e38-aece-1db2e5b9923c | -11.09328 | -41.31804 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a6efa418-d3bb-3f89-9d4a-6a0a94200c60 | -11.24178 | -47.72935 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4095f3e6-ba7e-33a9-906e-f60dee7ee190 | -18.26001 | -42.17556 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 12d99940-98a1-3d03-999d-487c66286674 | -6.71875 | -44.10636 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d05f44f0-52fd-3cd6-b9f6-3b9e10722c76 | -7.28712 | -38.61159 | 2026-10-08 16:37:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 53294077-ba8b-39a8-802d-37a406c59655 | -8.04699 | -49.40094 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fe099336-1abb-362b-b48a-63326e14b666 | -5.73357 | -41.77855 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| f128f722-2b36-3d65-9f58-e6c7a669850c | -18.82601 | -46.92445 | 2026-10-08 16:37:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4b44cd30-673f-3690-94ae-c979c23e306c | -5.24129 | -38.54845 | 2026-10-08 16:37:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f4e14efe-28dc-356e-9b15-5f7549025880 | -11.0086 | -47.97021 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 522f91e5-ec28-3ce3-b58a-b972b4a54e48 | -8.54214 | -46.91639 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9b28b7c7-22f5-3939-9568-34721fbde550 | -7.20657 | -45.0927 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0de510ec-c3aa-3d48-af8f-7b0736e687f2 | -18.98269 | -44.45698 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5233482f-a92b-311f-a1cf-dc418be9b827 | -8.96868 | -47.54669 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da9c0022-e2c6-3d5f-a965-aff116d85b81 | -5.71544 | -41.6427 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4bc51cb7-e990-387f-be07-5537a5d8b7c9 | -7.06115 | -40.94645 | 2026-10-08 16:37:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 0be74a65-64ff-361f-a4fe-f825ebfacd8b | -6.29149 | -43.19706 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8050a98-192b-37bb-9ce5-35806e2bf0cd | -12.4173 | -46.43939 | 2026-10-08 16:37:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c550932d-a65c-386d-8663-3d7d464dbbb3 | -9.65658 | -45.58074 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 69dbcc94-1330-3425-af5b-d1248011e982 | -8.30611 | -45.73503 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9e7a1df-e765-33c4-92d1-146070e2db21 | -7.09339 | -44.03547 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ba22c3d2-590d-3335-86ad-b798066e1c9d | -6.99586 | -44.12933 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7cb86095-4e62-381c-94b4-de5421b8f22c | -13.389 | -43.47961 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1d65dd17-b336-33d0-a7ab-1b974f7751f1 | -7.53355 | -45.87667 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 77c67c44-115a-3e9b-8693-0aaff91f0db5 | -5.97622 | -41.36879 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3b49e239-e28a-3d17-89f2-f65e3f126489 | -12.31411 | -47.84203 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b9d40bb6-69ae-3eb1-8c23-be54cd6780e5 | -11.08583 | -44.01505 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a9bb5ea-3277-3bba-832c-aa1f8d0ad22b | -6.56316 | -44.38482 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6acc03c-6835-3d97-b98c-b9bd193b4342 | -8.93544 | -45.1683 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 944a460a-046a-37df-ad55-920018560f8d | -6.23944 | -43.86133 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4aee4928-763e-36a3-9b6d-f2a8e01aba7b | -8.597 | -44.86489 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85322012-23f3-3895-853d-65ac3f9785bd | -19.04518 | -43.77173 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a7e12ed-df6d-33dc-80c3-c2de2851c523 | -9.8894 | -44.85986 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e1d4ff36-0c45-3550-86d5-63b75cb026ef | -6.21582 | -44.85525 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c7000c07-54e0-3136-84f9-7eaf8d79c62a | -13.1763 | -54.33797 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d5d4f047-97f3-393e-8b12-aaa56c44d15c | -11.25203 | -45.25229 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce095e30-b010-3d85-b792-e5dfef8c3062 | -6.88909 | -43.69654 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8738f31e-b342-303c-9f15-94ca0d2aa9a3 | -10.58502 | -47.30112 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 942febd8-ca07-3f91-91bb-2f4218824e33 | -8.3272 | -51.30594 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c5298ca8-7024-3285-ba94-ebf49bbb2cfd | -12.32596 | -47.08747 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0fca1f8e-2b2c-35c7-ae83-a2262b6e4b7f | -5.73412 | -39.64711 | 2026-10-08 16:37:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d75d7cf5-52ee-3aed-a7b1-263d2ba975a5 | -11.07639 | -44.04202 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b4797479-9c56-3406-966b-baa7c0e73b6f | -7.19143 | -44.34383 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| daaf0d99-779e-3cd4-8f01-ef43dfedff2e | -9.39474 | -45.89069 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3376ca2-74d0-3552-aa89-dfd3c2cf16e5 | -6.37913 | -42.5279 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 3daa5017-ea12-36b8-a2e3-593adeb40ad0 | -6.89193 | -43.69222 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| eaee302b-76cd-37e1-8618-8d5e0d9ff214 | -7.7123 | -44.74183 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a43425e5-8c13-3934-8c00-762cf0df048a | -6.92972 | -43.66294 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ab4c6a5c-19e1-3da5-8896-fec7938b16cb | -19.20769 | -48.15791 | 2026-10-08 16:37:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7032d102-a814-34d2-bf3b-3fe181296c88 | -10.25929 | -44.63885 | 2026-10-08 16:37:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ff1c522f-8296-3bc3-958c-efe8f02f38e6 | -9.4601 | -44.607 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3c9484b8-9b0a-36f2-978d-2e4151dbe425 | -6.8266 | -46.42573 | 2026-10-08 16:37:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 90ecd99e-41ed-30e5-ae35-03d1529b2579 | -11.13556 | -46.12317 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d8f95176-519f-3fbc-bb36-4c14b877cad7 | -8.29249 | -45.71223 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| afc98b03-77b7-36e5-8835-c384011f33ee | -13.13068 | -46.36944 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7c09b80d-b65a-3f34-996b-579c57d6fec3 | -12.31386 | -47.05293 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| eac40949-3dca-33a9-abb9-b93a02ec723c | -8.61014 | -45.63651 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |


[Clique aqui para ver as próximas entradas](README313.md)
