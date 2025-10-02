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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e410e0f-ba8b-3945-93e0-084fa0024279 | -10.26551 | -50.34292 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91fca543-54bd-3a1a-a31f-5b8143fc8663 | -11.27788 | -47.83026 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 16272d2a-913b-30f1-a501-8dcb1dc2651c | -7.41094 | -45.19405 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2edb3725-2eb9-395b-90fa-a8b9a9f5c2e7 | -12.84123 | -46.9496 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd97cc37-1ed5-32d6-b381-0bd7005fbed8 | -6.24004 | -43.07347 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 32747512-7b7b-3409-b6d5-087ecb2bbf7a | -6.24295 | -45.32934 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77925eb9-7c57-3912-8abc-9cd903ed8443 | -11.13847 | -43.38711 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 46edcc6c-94ed-3b35-8693-cde137cf2626 | -6.48686 | -44.29241 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5e6b5f7-1746-35de-be9a-b4440500e554 | -6.96317 | -45.32571 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5bfe21a-527e-3e8e-a2f2-7c9db8583ede | -8.88009 | -46.5966 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72e2d512-c4e1-3556-9b4b-8f251833576c | -7.04492 | -43.34528 | 2025-10-02 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 056ef1ed-b0e8-3dac-9056-cffad902cee5 | -7.77712 | -42.52954 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 1be6cc4d-2f0b-3306-bcbd-0493dfa73834 | -9.94142 | -43.72803 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a1097e2-841b-36f6-bd33-cdff2b74cdbf | -13.41318 | -43.49752 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff814c0-43ce-3a07-af86-84c72030f234 | -6.96678 | -45.32659 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c073afe9-8e87-39bb-a62f-ef7733abd42a | -11.46384 | -45.12964 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b516454d-9628-3ded-913a-ca54be094919 | -11.52742 | -43.54285 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d341460-9ead-380d-b1ab-d097cc89fa78 | -11.53351 | -46.95353 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7b28314-e6cb-3510-9844-653bbea81faa | -11.43346 | -43.49517 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 987b050f-5725-3ded-83d1-720cb9c42a86 | -9.38434 | -45.83108 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a44c57a-b0c3-363d-b823-583b4ff5ac55 | -10.84073 | -46.63151 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fba36127-95fc-36e5-8c40-51f74e6729bf | -9.93096 | -43.74736 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 7a8679c6-da2c-3a95-a5d9-6d3397c301e9 | -9.40363 | -47.58417 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f259af96-2be8-3986-8df4-f84b9fb770b8 | -12.82143 | -47.06102 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d557f58-3b6a-39f2-89e7-2e7bba0e22f2 | -11.81091 | -47.5903 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f69fc8f-58f2-36d0-91ee-c4df27e699e5 | -6.11528 | -43.12706 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2c40c73b-3825-39a6-9677-28de2f5084ee | -6.71305 | -44.56618 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bb35059-c4e3-3fa3-affb-befb1ec05ec7 | -9.9328 | -43.64728 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15a0716b-8044-3597-a651-626a00276c45 | -11.97928 | -47.01795 | 2025-10-02 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55046d44-6d38-3576-8d33-2804fcf354b3 | -9.95421 | -48.7874 | 2025-10-02 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 970a3255-a3aa-3953-89fa-0732f72a4ac7 | -11.09856 | -47.82298 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f01d80f-eb8b-3ff9-b09d-5ed254051bdf | -10.6417 | -47.45705 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a8fc811-d9a1-3413-90b8-dc0758629dbe | -11.80465 | -47.57539 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a436ef2f-6827-37d4-8893-0abe2b489122 | -11.80654 | -47.58961 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d2f90fe7-f83e-388c-9582-1bb54e4f63f6 | -8.7366 | -47.34397 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f0c360c-ae0a-36ad-b4fb-6abaa3ff14fc | -10.91601 | -46.46062 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37028eeb-a287-3df2-8c9a-7ba8167cce32 | -11.43629 | -43.49961 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51badc1f-11c5-3c4b-b3b9-e9470f2c1799 | -10.25802 | -50.32362 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 33628b88-39c1-3e29-8bcf-d1816b450fb9 | -11.14256 | -43.38388 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b558600e-5009-3f5f-9cd4-27331c0be2a3 | -13.00834 | -45.21052 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 06749d35-325b-312d-b6c3-37e238973e86 | -8.84304 | -46.5817 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59f90f0e-9c43-3ff2-af36-70ca7637b954 | -10.89776 | -44.28912 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bf0e99e-7c99-32fd-8686-c62fc68a109a | -11.59841 | -47.22621 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e2363f7-81bc-3271-9908-4f2c1bb6a168 | -11.0916 | -47.82524 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1a681a8-90c0-3ea0-8edf-65dd6f2bc65d | -11.58957 | -45.05146 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0107edd-4ad5-350a-ae3a-bb0c89975fb1 | -11.26416 | -47.80413 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1393ee57-6773-3135-8885-a487a2373b57 | -11.48058 | -44.99432 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7ea49c1-d079-3156-b85b-d7e3dbbf3013 | -10.18636 | -42.6089 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 73c4cdae-f764-3fa9-8315-0be7fb72320f | -12.25919 | -47.81855 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53d2a92a-18d8-36cc-b0be-af60bacb8b4b | -10.23933 | -50.33442 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b841686c-4394-3413-a060-0317cebdcba3 | -10.24989 | -50.30783 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ef1778e-0019-3719-b6ab-eddb3a70a316 | -8.85991 | -47.66257 | 2025-10-02 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba8c1190-6250-3a99-9960-4ad3a2c73129 | -9.93674 | -43.75668 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 0b7ca288-5766-3df6-b5dd-a83be4c69e8a | -6.13832 | -47.27863 | 2025-10-02 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6278680-6517-3ae1-8e6d-2835a17196f1 | -12.25754 | -47.82772 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d22f5c1f-e5ec-3780-89b5-c611cf39c1a8 | -5.79261 | -45.73364 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30e64f8a-6374-342a-8684-bd14835e5f3e | -12.65553 | -46.86298 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bff7b41d-b791-3e47-873b-de1af8dbbc33 | -6.3101 | -43.43285 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a39378f-4049-3994-8c9a-5f08d88530eb | -5.89853 | -45.64487 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| febc0a0b-72f7-343e-ad65-9e219ecfa98c | -9.58414 | -47.08154 | 2025-10-02 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5863837-a665-396f-a860-7e66d3ce364d | -12.5124 | -46.84117 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38123795-02fc-35c9-b8ae-db2049181aee | -12.80281 | -46.85785 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 089f2026-6104-3112-805c-33b545524913 | -12.63714 | -44.85303 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a4e3092-cc79-343b-95ba-1544da04d4c1 | -11.83068 | -44.99468 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 39c33a18-a03d-32e3-b3d7-b73e624c736e | -10.26061 | -50.30983 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfe017f1-b841-3e7f-90da-4a2ccf38cec0 | -5.51443 | -45.16076 | 2025-10-02 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5944661-5dcd-3ca6-b2bc-32a22cbaa656 | -6.08903 | -42.49855 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 41042a3a-d238-336c-8436-3f25c86afc0b | -11.81253 | -44.99789 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43df468e-59a7-3200-8bb2-45f95dad7e13 | -9.93607 | -43.7608 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4e1767a6-1013-3f0b-b467-dd614bcb2bcf | -9.3329 | -45.71489 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1fa0b7f-90b0-3d81-9bc5-8358d794cfd3 | -11.86965 | -45.03432 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d86444a0-4c0e-3e2c-85b5-c639574fe664 | -12.2635 | -47.81972 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76d4ce1d-7a11-3923-9743-1bb25cc2f6e3 | -12.94066 | -46.43237 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 075f0420-5195-3e39-98a9-7b0b6467e663 | -10.34738 | -48.19763 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1d94fae-52e5-3992-b81a-bc6b0e0f23bc | -11.16534 | -47.2638 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a09233ba-8032-3f13-8e0c-4c55c1e6ec9f | -11.4807 | -45.00564 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc49723e-12e8-3188-affc-7d5a6f812047 | -9.90489 | -43.68423 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a472db3f-02db-31ec-a343-fe8fdbce59a8 | -12.00788 | -46.63838 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9033ccd2-2a1e-3f94-bdaf-ea47e9e15bdd | -11.81573 | -45.01507 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcdedfa2-a238-33e0-98f4-fe661281dfda | -11.46733 | -44.97131 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8b9d79e-9fdd-3153-a44b-44a9dd1e0d9c | -11.59341 | -47.22958 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91263be5-f4e4-3896-b478-4ab42b07df42 | -11.06374 | -47.81116 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8413ace-138d-3529-b8d9-bc7c38d55e68 | -7.13499 | -46.17669 | 2025-10-02 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331498a5-cce7-3a00-a436-cf11617156af | -7.55541 | -42.63958 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0b9fa23f-daa0-3743-b217-dab4e4e93e9e | -10.83525 | -46.63842 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ced19447-1157-3333-867a-0e49952adc44 | -11.19109 | -47.75888 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2da64034-cd11-33f8-a472-c78e0c0e9311 | -11.82852 | -44.98509 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fe16659-3586-3eb4-8a23-264bb07a797d | -8.82602 | -44.78564 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d4d0d36-bb34-373c-8033-f9e1b3e46024 | -11.59694 | -47.23448 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98fc6262-53a5-3d08-bad7-fc8cfecbd32e | -11.92089 | -47.88407 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d169172c-d05b-3bbf-8179-33d82d55d803 | -11.59295 | -47.64029 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 168bcad3-a6af-3cdf-9adb-84fa656e340a | -7.62912 | -46.55513 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a92dbbf8-1495-3965-95e6-4adbe11a691c | -11.81171 | -47.58592 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 031c2f25-54bb-3cfe-9c60-e8a975f3a65c | -11.79029 | -47.57325 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 852d91ce-efeb-3661-b758-1e99425499b1 | -11.17316 | -47.26982 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3d46881e-28df-3c0d-bcb3-75c660fce9b5 | -11.47031 | -44.9763 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc180c8b-efd1-3406-8c88-f2a1ac42e228 | -10.99669 | -46.59531 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 7e7bb6b0-5e6d-3783-b986-ae62b4f37101 | -12.89728 | -46.91888 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e65cf13-6cb2-38af-8b17-0fda906bbfc4 | -10.2486 | -50.31472 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e2610f5-fc59-3d71-a0fd-7fae0b94fa77 | -7.39418 | -41.87332 | 2025-10-02 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
