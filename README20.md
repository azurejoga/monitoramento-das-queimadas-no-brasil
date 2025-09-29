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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 463d059c-6d03-3702-9f23-0af276d71342 | -9.10474 | -45.84447 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eef54057-85a6-3f51-a126-dc167275850c | -19.19995 | -43.9862 | 2025-09-29 03:47:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad1120a1-cd23-304f-bf09-85f8be828f7b | -15.28682 | -49.52277 | 2025-09-29 03:47:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 899bacff-a4e1-39be-8dae-09ef2e03a6a6 | -8.30184 | -45.44409 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ae625be-d425-337a-b98e-63e42d2d07a0 | -11.72372 | -44.42852 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abafd7d4-39cf-3d44-85f5-5863534d91bd | -17.39206 | -47.12054 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d5b965-a498-3af6-98dd-cf70d7e5dd52 | -6.06883 | -43.49379 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b41fade-ff2d-3d8b-9231-0ea19a81f274 | -15.49597 | -45.87802 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cddef42f-4d67-36a7-afb4-d1111786e6c2 | -12.89509 | -45.22128 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b0b594f9-6b8c-3608-a425-72fabd476872 | -7.50464 | -44.29088 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e60f6bd7-bf2e-3897-a696-b78684c854e6 | -19.92682 | -41.61641 | 2025-09-29 03:47:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6a91e68-ea73-37dc-8485-c49cc9df64c7 | -8.86072 | -46.61983 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 76d4cc0e-21b5-3a51-b51d-701555c062b8 | -11.41836 | -44.91237 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e71a8c69-d1ee-393f-9866-cb75d0993a9d | -12.89231 | -45.21658 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f24e372e-f908-33f8-950c-72b314cc19d4 | -18.91308 | -41.12343 | 2025-09-29 03:47:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3949edfd-ce4d-37af-bed8-61d1b0b72924 | -6.1473 | -43.91091 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9416fb1-c8ff-3e2f-ac0f-cc2368351863 | -7.89407 | -44.60738 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b62635cd-ac90-3714-b1ca-a2c359f083e7 | -6.13941 | -42.65632 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b507aad-ea2c-3692-b523-66a02bdd2339 | -12.70145 | -46.91278 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47c759a0-1415-3f0a-9314-e9dd15e79146 | -7.02647 | -45.1852 | 2025-09-29 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0329041b-639f-39d3-a849-e72d0c8a54fc | -12.58306 | -41.28867 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 818f4780-7952-36d2-aae4-601cef3682b9 | -11.48506 | -43.21418 | 2025-09-29 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dfa24683-8436-31e0-b5e8-2494ee12d4c1 | -11.50568 | -44.85539 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93a75039-c82b-306f-8ec7-d1a4a04f1d4f | -11.93042 | -48.06646 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a93f9e34-fe72-373b-8803-8055665f343c | -15.08243 | -48.33547 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96fd1ba0-06c5-312e-80a7-824364636c88 | -11.45297 | -44.99487 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06f08f02-ad5e-32c2-9ed8-450b1d175acd | -19.54845 | -40.6246 | 2025-09-29 03:47:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 45196f70-50ed-3c9a-bfe5-7841c1f13039 | -11.91974 | -44.75726 | 2025-09-29 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5684412a-1218-375b-bd5d-2e2d1e2b3bfc | -8.2976 | -45.43583 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba31007d-e462-341e-b618-b1f27fbe64c8 | -6.263 | -43.64461 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 529a888d-c350-36fc-b401-85aca1710890 | -11.92274 | -48.04145 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f817d919-5532-3fec-8964-5d0d63b195b4 | -9.31185 | -45.69861 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efd22e63-fba5-3110-b796-3d68cd2f7b59 | -7.21423 | -44.77175 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 171dfe8d-6ee1-3cb1-99e8-1bf9e587662e | -10.82816 | -45.41247 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a6ef478-6919-3de4-a8fd-b939fa3c21b2 | -9.78421 | -46.93614 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e3fc0a5-2289-3357-a83e-34d8868a2686 | -9.63325 | -48.12617 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f0072e2-a9c2-3781-ab05-e1d46e73d861 | -10.81094 | -46.67441 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b65ab509-2594-31b5-9bce-57b085ea9212 | -11.43176 | -44.95373 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43e3449c-1898-3c26-9e25-474ee332f10a | -12.89121 | -45.21434 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e54dc87-cdc6-34e7-b70c-59f8dcb7e338 | -15.86549 | -46.83531 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53981428-b1b9-3511-994d-04fc278732f3 | -11.67222 | -44.29933 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63bfb6a7-20a5-3b15-bc97-04145621dead | -7.22445 | -44.77711 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 06c86ae7-e337-3f27-91c9-3b59223a0d30 | -11.45411 | -44.98888 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eeed1604-e42e-31db-901e-b71ed71fc0c7 | -8.71218 | -47.98388 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fdb63c79-9d5b-3340-8fcb-08e01b2bec93 | -8.86157 | -46.61523 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 289a150c-ccd4-3012-96d0-ddefd95f4682 | -5.67913 | -45.29339 | 2025-09-29 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9c2bf9a-58fc-394e-8741-f4866aba336a | -11.40459 | -44.9017 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f6c09f3-9951-3fae-bb7f-42f20105c4a8 | -15.25384 | -48.76421 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ccec692f-1d83-3d13-ba58-73906c8f88df | -7.28895 | -42.83245 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bcb68ccd-6941-36f4-8189-c0057d22e261 | -8.16342 | -46.4005 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 115cc930-5a92-3321-9ba5-13b78f244d96 | -9.78038 | -46.93802 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e34c508-f9d0-3f34-90fd-7543370d689a | -7.25007 | -42.99934 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cf5ff06-1bf5-3af7-888a-0146797081e2 | -9.10325 | -45.8526 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3b08af3-776b-3b11-a4ab-c6232bfe9528 | -9.27573 | -45.73793 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da9bfc51-2aa1-3cbe-adee-56b13e206451 | -7.866 | -41.05669 | 2025-09-29 03:47:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce28cde5-4ecb-35a7-af6b-b15b56dda37b | -8.27948 | -45.50357 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ece02c2f-796c-3345-a0a1-32aca6ad8405 | -15.87173 | -46.21547 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8de26557-1b7f-3bda-bd2f-ac175200e72b | -15.53088 | -47.931 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba7379dd-fea7-3c0d-9315-dc5384c88196 | -11.35856 | -45.06225 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7be01e64-85c2-315d-9a6e-b86c994c3e44 | -15.08507 | -48.33884 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e5a250-03c6-354d-8fdb-635ea7547128 | -8.30033 | -45.48398 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e9ef4f5-317e-31ba-9dff-cb7087208549 | -6.3131 | -43.44413 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 703a01ea-ec1c-34c2-880e-7c4b69f0ae1d | -11.99545 | -47.09504 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 421385a5-d4b6-30b5-88b7-815ee6911bab | -17.39804 | -47.11814 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8d7d412-e451-3ab7-8566-a1a01f4967dd | -19.73385 | -43.22385 | 2025-09-29 03:47:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8163a1ba-c8b8-3aef-b018-c10bb109b81e | -12.87829 | -44.6879 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e65b9e6-1129-3a7e-a28d-75627eae22d9 | -15.27588 | -49.50106 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c93ebeb7-c419-3f44-90b2-3b25888ff0d0 | -11.35937 | -45.08616 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f117157-0625-3d59-b79c-69c66fe29691 | -12.20864 | -43.74859 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0c15eef-2db1-3038-b5dd-ef283006c4d2 | -11.92207 | -48.04947 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d84c595c-92a1-3186-b326-e601d5d6bffc | -20.08792 | -41.35595 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e2f08ff-e34d-3a47-8c4f-62ec24ecc994 | -15.28119 | -49.50713 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45b0837c-9d56-3963-84ca-690324eb5f19 | -18.90364 | -41.1353 | 2025-09-29 03:47:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19074621-5f07-3d8b-967a-2554c4de18df | -19.32814 | -43.81287 | 2025-09-29 03:47:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 248bf115-7498-3d41-8025-5282cd6ddad3 | -11.43124 | -44.95655 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2655217-fd44-3780-8fa9-c08b06ab6516 | -15.27677 | -49.50828 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9e2e82c-cebc-302c-9de6-06b136d1b5a9 | -8.27512 | -45.49592 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f0e194dc-26c2-305d-8858-1efdcdc39763 | -7.22676 | -44.79547 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 59ae5a6b-a834-3e08-99d8-d176a0918679 | -17.08849 | -48.56816 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 00cea0b3-f02d-3e34-920b-343b1a911548 | -11.4489 | -47.28655 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ba2b7a-a01a-3cf6-891d-cac5f4af9d05 | -10.40351 | -48.11521 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d16a35b-37e8-3dfc-8564-5387067df62c | -6.28198 | -42.48323 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 39479e8c-14ac-3a30-bc52-145f31a41bd7 | -15.60957 | -46.2521 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4740a1a4-8802-3a74-9815-c0773e74299a | -7.29833 | -42.83222 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b1817f8-bc4c-348f-bc43-388cbc386649 | -15.79706 | -45.39101 | 2025-09-29 03:47:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7e8c644-34af-3848-bb19-50f8243ca2d7 | -15.78236 | -43.85531 | 2025-09-29 03:47:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f547617a-2399-346a-953d-61e941baf14b | -11.98321 | -47.12715 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61ad4d4f-c932-38e4-ba38-fdbe3bb31aac | -17.08795 | -48.57536 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b437b2db-2241-3a75-9ca6-0a1f4ea87a97 | -15.21843 | -48.05228 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 89760e6e-1e4d-32f9-9b98-0810ad2769ec | -8.8864 | -45.03337 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b626c25c-9c49-3071-86a6-a620975fdb50 | -8.29158 | -45.46886 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b584f30c-9e8f-3190-996d-b367bf36c4e7 | -15.27344 | -47.873 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d6ebfab-e29b-30e4-a1fb-71a1639118c9 | -15.27286 | -47.87513 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a79aaa3f-a6d8-3d11-aac0-525e0058a45f | -15.25998 | -48.76498 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b3e1f015-0e9a-3b90-9830-7d0391a5d656 | -9.31052 | -45.70578 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8f35398-1f7f-3867-ab97-d3dc7f6ef572 | -6.89131 | -44.52697 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 060bf8a6-a39b-35c7-8ab6-63824448536e | -17.07642 | -48.57278 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5aa14997-ecb7-3969-b198-ec706a8f1a54 | -6.29934 | -43.46389 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efa8dde6-a7bb-3e87-a598-26ac4abcdc46 | -6.89438 | -44.52839 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfe9e158-4e86-33bf-bf09-f612860d38e5 | -10.91677 | -45.71776 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
