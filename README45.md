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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afb00165-5a6c-3205-9e25-d67045c78497 | -9.18499 | -59.45514 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 603a1b56-4ba4-369d-8ace-7be21f0d16f5 | -13.66826 | -47.96935 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba75c24c-24b4-3c74-8e38-0d1830a6832f | -8.89413 | -62.43752 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8df386e-0e1a-364b-a3f4-5832083254b2 | -10.47781 | -57.93888 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd9c4f5d-af43-3a45-bc33-4b81b2248ce9 | -13.05639 | -46.33138 | 2025-08-25 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 580738a3-6a2e-372a-96cf-ac24b636ed3f | -7.62889 | -62.7296 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 982b2df1-1251-3cdf-a566-5effbf6938cf | -11.92745 | -46.72679 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf318fd8-6212-36f6-b8c1-f99eb6885421 | -12.73006 | -48.1386 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 877731d5-4225-30e8-a851-de22cebdf046 | -8.87446 | -62.43353 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df247ff2-5a21-360b-a16f-0a356d4e71a7 | -12.73645 | -48.11951 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7c437e0-f70e-34af-b9ba-19bc44409145 | -12.74234 | -48.10388 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edefb302-aa2c-3d65-9ffb-a652a95a1923 | -13.44606 | -46.8881 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5398b6f9-fde6-3b1b-bf6d-69c8b9e9e52f | -6.83853 | -58.95499 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89c5ea47-1ce8-3f2f-bdb1-fafea25b3e1e | -9.50417 | -56.1001 | 2025-08-25 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 204e7dfa-a238-39ca-9e7e-d4d929aa931b | -11.86482 | -45.11816 | 2025-08-25 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfba3987-1f1b-3bd9-a2be-598b099a1e45 | -13.43505 | -46.91507 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f3c23d-f88d-3cc7-abe0-f33a41b5eddd | -11.93562 | -46.7234 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98da7210-7500-35b2-9eb9-2e5e696c586e | -6.80986 | -58.95728 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ec37e87-a78f-3409-85d0-db98c87edf88 | -12.72713 | -48.13874 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15f17fc0-cf43-340f-a42f-2deddf099aff | -6.82208 | -59.43053 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d9f9ab22-29a8-3421-9e85-e88ce65ab987 | -11.55144 | -51.91483 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| faa07685-7432-382c-8744-5d95d8e9714f | -6.82277 | -59.42665 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc8be1ba-c513-3125-ae30-34f8961ecce2 | -12.49418 | -53.82592 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bea8e752-28cf-374a-97df-58f46a07cccf | -6.91873 | -63.00186 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd99ba6a-7582-3e78-bfad-c8c023289596 | -6.8147 | -58.96175 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32e50b09-febf-3013-adda-eccaabb0888e | -13.45462 | -46.9103 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8da25493-6361-3dae-9ffe-f92e8c915aee | -9.16091 | -59.49442 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 149b9919-83b5-385b-9640-e6b1fd1de6d1 | -9.19776 | -59.44673 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dfdd64e-d7ef-3683-bc13-d1eb86241e24 | -8.88102 | -62.43486 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c307daab-1820-36c6-a80f-05f783226b40 | -12.75936 | -48.11117 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f62ca03d-0d7c-35f9-bb35-7b3879eb5c64 | -9.18282 | -60.79481 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fd1c1833-a346-3863-8a9c-70f8a50fb88f | -12.68581 | -47.82735 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c854ef5-8a1a-3d2a-89b6-1879502a3ebc | -10.81916 | -48.33052 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8678c3bd-1ad2-3261-9815-6a28db3883d7 | -9.22369 | -59.6768 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4629087-91b2-3874-9cd3-ba8059024a8c | -13.42994 | -47.03043 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77fd425b-252f-37fc-8dfa-38367a44dc07 | -10.59863 | -44.33268 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 232ef5d0-cf8c-3b1f-b4cf-6e5c8d4b4245 | -11.2657 | -44.97629 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4db232b4-fcb9-3af6-bd36-feaba03d6a9a | -13.15541 | -53.74151 | 2025-08-25 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02cb854b-5145-321e-9886-3d56b842d6f6 | -10.61539 | -55.05783 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 736e5bbd-ec8a-3b47-a2e0-4262b9df55f0 | -8.22164 | -61.42115 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6ba0e12-94a3-3dcb-a3c1-2cf06e580f2d | -9.19903 | -59.50165 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0050f9c-4c54-386d-9683-d621c16f742e | -9.17828 | -59.46114 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffe4a7c4-2623-3466-ac55-691f0c242d41 | -11.46533 | -55.46892 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b704e1a-e28f-3fd2-824b-7dd714939da0 | -7.91169 | -63.0666 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3e3a3d00-6ddb-3444-8b30-b3c0ffb0b128 | -9.57976 | -55.37211 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b4c7f59-6cd8-330d-9db5-b2c2eec2d255 | -8.21829 | -49.56305 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d43b8565-d9a7-3226-94e0-334c2da688e3 | -9.81767 | -64.25764 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 192fd37d-7dfc-3799-a8b5-5999c25d17b2 | -13.61616 | -48.17696 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fa6daf5-062c-354b-ac3f-eea54f8cfba7 | -11.70407 | -60.1897 | 2025-08-25 04:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 911439e1-3ad8-31a0-b695-9e2a73944088 | -8.88213 | -62.42921 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa07559a-c2e0-32a5-8b3b-cbe1d92afcbb | -9.15156 | -59.5146 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 681efdc7-f844-3276-bb06-804dbf3304f5 | -11.09551 | -44.77649 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43916f04-ea98-3272-8037-5af8393fa36c | -13.45991 | -47.01054 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3b8683d8-b460-3d2d-bf03-ef574a2017e6 | -8.808 | -45.46837 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c133107-308e-36a5-b686-625d6e34490b | -11.86695 | -45.12362 | 2025-08-25 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 769bd6f7-af49-370a-8ad3-1dff34a6c6d1 | -9.18787 | -59.4702 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e2f865-edf3-3249-91ec-9e212686b765 | -11.27297 | -44.98493 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d70539a4-587c-3744-bced-c3f569b13606 | -9.1875 | -60.78775 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 32135754-1c00-37e0-98bc-6c8e9343ddf1 | -13.447 | -46.88607 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92e96da1-e1a2-389c-a7fa-075df0874aac | -10.47686 | -57.94403 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9002551-8acb-36fe-94c8-e8bbf8ae94b6 | -7.84526 | -49.99983 | 2025-08-25 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d29fa645-d753-302b-b2d9-83f3143d0b7c | -8.88316 | -62.45877 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c37a2ea6-9016-3170-a47a-af1bb4374572 | -8.90175 | -62.46843 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5e2f675-e986-32fd-8dfb-3d93e9843346 | -9.52338 | -60.53152 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 477b08d5-fe12-3215-bca6-943a908b8136 | -13.40651 | -51.78999 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b2164c-8136-3781-b0e2-0eda5eb6d5a8 | -6.69098 | -58.8629 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 306412f4-ff04-37b8-90bf-0785d493f983 | -9.18668 | -60.79198 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 62372cb0-5cb2-3d4a-81b0-c53242b13bb6 | -13.66765 | -47.97355 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b588986-45f8-30d0-92ce-948242ec6736 | -9.17073 | -60.81116 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2a9d489-a67d-3154-bced-8c7d1f0948e3 | -8.21791 | -47.17724 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65593520-f919-3501-ae6c-899a54993a81 | -13.43367 | -47.03115 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b9c7573-06d4-345d-9359-9da17dd343ae | -12.48336 | -53.82405 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7c18f4f-9010-308d-8124-e60314c33807 | -11.61595 | -46.24007 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 532bf964-19eb-3991-8483-cc3549483f7e | -8.86477 | -52.04693 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86f77ad5-a8c0-317e-874a-85d963a05307 | -8.11183 | -62.87438 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 770788a0-9159-302d-aefb-0321a6705057 | -13.50417 | -46.91569 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54c38e1b-5771-3196-af2e-3ab39b8ecde2 | -9.19148 | -59.45636 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78476b9c-a3d1-3b1b-8554-886bd345ace8 | -9.15046 | -59.45952 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0d62a2-88c2-3b5a-b8d3-c3ef42f81141 | -8.54308 | -48.86961 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a9cb6f0-5828-31a3-846d-00aa9f277eee | -13.44132 | -46.92259 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a4d0747-965d-34a5-85b5-869e73c93ea3 | -11.86894 | -45.11895 | 2025-08-25 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1675bc3-0987-3e21-a876-6bfb0491f275 | -8.38463 | -47.99713 | 2025-08-25 04:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8974ce4b-a838-348f-825b-8107fa3491d8 | -8.92037 | -62.4427 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 909c0468-bb90-3d68-a9e7-27343357c3a9 | -13.39633 | -51.81043 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15a0bfa9-7617-32dd-813e-42e1e0ca2fb6 | -11.93187 | -46.72283 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcb76249-0aa8-3ea2-916b-f320ae142c4e | -8.06502 | -49.67751 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0f11ce7-86cb-36a0-9684-1efd2e0a946d | -9.19474 | -59.61856 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b456e36-1655-376c-9fb1-ec58842f4e8e | -8.91603 | -62.42996 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f3bc483-5871-3acb-9038-6a6e11a83529 | -11.63933 | -46.2137 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 669f9333-7086-3c24-8f9a-fd71548cc5fe | -7.62175 | -62.72888 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e04c412-79c7-3738-8cca-3f050b9b9847 | -8.0628 | -49.67002 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f790953-4bdd-3f34-b16f-99adb2491e99 | -6.62949 | -58.54222 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2258ab8-1342-31ab-b576-57d9ab5aaa3b | -10.39666 | -57.68769 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a42592b6-54b9-38fe-9630-fa09dbd701d4 | -8.86891 | -62.46181 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 92268874-b25c-3234-9845-4e3657d81323 | -8.87225 | -62.44479 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db0f1681-8548-367d-bcd6-f9ee0490825b | -11.0971 | -44.76497 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5434bf5-9e1c-3184-a121-25ac512f0b37 | -9.18371 | -59.46214 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8406ad28-0476-308e-a00b-dcab7cfc3461 | -8.49445 | -63.879 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8632de28-c077-3cea-87f1-01917257dd7f | -9.16618 | -60.81841 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e37a4e2e-3c20-3800-b940-02c1804764f7 | -8.06832 | -49.65661 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
