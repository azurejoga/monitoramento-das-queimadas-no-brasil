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

## Dados Diários - Página 269

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6ca33a2-cca3-3830-8e11-e4ac8fb485b4 | -10.41493 | -47.27436 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4951af89-0bcc-3ea4-b012-f8d3806e00d3 | -12.25106 | -38.63008 | 2026-10-08 16:18:00 | NPP-375 | TEODORO SAMPAIO | BAHIA | Brasil | 2931400 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 59a4a81d-134e-397d-afaf-9de6594a7d2b | -6.81803 | -34.91588 | 2026-10-08 16:18:00 | NPP-375 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 72f5ba87-788e-3600-9f5c-f35fcf109cbb | -11.84854 | -47.30493 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8df520a3-3a9c-3ff6-b46a-c503981fe650 | -9.08182 | -45.12049 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 277d0ca9-2d65-32e9-b2e6-849f54b79424 | -11.59809 | -43.6767 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fdff4160-6aed-3990-93b5-0dbe2067094f | -11.87113 | -47.39955 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d4120c3d-dc8d-3371-be7b-ac5da96ab474 | -12.98655 | -47.06037 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 235ae38a-467d-36f5-8100-c755b3613dbd | -11.76745 | -44.94851 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e2fda6a2-5ca6-374b-a9e3-d7ed6c60f910 | -9.00696 | -50.8573 | 2026-10-08 16:18:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 48065914-1b7e-35f8-aecb-a4de19d4a256 | -12.61674 | -44.54873 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7fc5f451-7701-337f-9890-c084d114b3ee | -9.0774 | -45.12128 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c898e35c-46d1-3b51-88af-c62441dae527 | -11.36331 | -46.70008 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d47890e8-7e33-3e24-8f78-33454280fb41 | -8.96716 | -45.12956 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a42edc33-650a-3aa2-9adc-5866c733c9e8 | -9.7642 | -44.78511 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 635967b8-c4dc-3c61-806b-6ea20e7b99dd | -11.60598 | -43.64099 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 752f1ac8-3bb7-3555-8702-782fa24049f2 | -12.04095 | -43.4345 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b8403533-882e-323b-bc59-ebfa4d6c4e97 | -10.07575 | -45.6908 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 118c7ce6-9f70-3ae1-b581-f771472fd362 | -11.10067 | -43.99833 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 81a48d6b-9439-39d2-a73a-19ca5455c22b | -11.15584 | -47.29443 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b71d4c58-fcb7-33ce-bab1-39b75c94fb54 | -10.12852 | -46.84035 | 2026-10-08 16:18:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 50e452c3-f561-3f41-a295-212ff5bd571d | -10.46832 | -47.23766 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 081de427-5357-334c-bdeb-4d7f921cf2f7 | -9.8868 | -44.86017 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| b8c36812-8e58-32e4-8ab7-765d8e53f110 | -8.95744 | -47.5738 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3839f7c-faa8-3e05-ae11-be90afb2683c | -11.00394 | -47.97626 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8493c211-15c4-32a9-a5ca-6b1328acc531 | -13.6972 | -42.29112 | 2026-10-08 16:18:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c9409f6b-c611-325f-8f67-820f185f1107 | -13.98665 | -46.36591 | 2026-10-08 16:18:00 | NPP-375 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b788ee1-ae1a-3cf8-96af-056dbceec19f | -9.43387 | -41.73859 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 58710eb2-bc58-3d20-906e-0ab7925b730f | -9.81369 | -45.68638 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 4f04caa2-ab14-306b-8eeb-da6ee6c78124 | -11.07791 | -44.02164 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 24d27e24-d633-342a-aee8-5189586baf22 | -13.29431 | -41.52172 | 2026-10-08 16:18:00 | NPP-375 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| f9754419-da32-3483-9cc4-aac4ab972cf8 | -11.71885 | -43.6526 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8399326c-fcda-3780-8f0b-78d63992b2f4 | -10.81164 | -47.3389 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| df8c50bd-c664-3aee-bc76-01c88f85e82a | -7.28923 | -35.77462 | 2026-10-08 16:18:00 | NPP-375 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9c20d96a-cce2-3686-9f25-e9abb6c1ce53 | -13.9652 | -44.84932 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ee2c47ad-91f0-3c5d-9bdb-4c0ceabc7fa1 | -11.74285 | -43.64157 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6383b665-cc9e-3cf8-9e64-ae55494455ea | -9.90338 | -44.82339 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d045d1be-923f-34ef-867e-f5832845fb15 | -11.96688 | -47.7672 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 897675b3-528a-3e77-888f-064f1fa7af19 | -8.29926 | -44.1697 | 2026-10-08 16:18:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8d25ff9d-ce39-3b16-a3ba-aafca57e11a1 | -13.72187 | -40.34783 | 2026-10-08 16:18:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8d8cc2c4-41ef-3015-80f8-35cdba0833e9 | -13.61662 | -43.27934 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6fc25d7f-c5fc-35c5-96f0-982b50ae3223 | -9.03051 | -44.36548 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b28ec571-6691-33a4-8861-5723325026f6 | -9.74986 | -46.94578 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 062f1934-d01d-3fdf-8942-b7f7e050c245 | -9.82434 | -45.69504 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7b458b5f-c377-3d87-b9b0-240d4f82c80f | -9.89617 | -44.80303 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| b424ec4d-ad84-3f00-bd11-87c003c2ed2a | -10.86534 | -45.55429 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 329d4466-6e7f-3a3e-b7ab-984d8a80d5eb | -13.11794 | -46.34631 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ca88572b-ac2d-3f74-a13b-7cc6bcfe349d | -9.96833 | -43.53988 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d966d2f-d68c-3887-b539-db2210715f78 | -10.5099 | -47.31146 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a9c4336-a84a-3d61-910c-12a2e88868a2 | -11.22853 | -45.24092 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 390d3d51-c0cf-3bc0-8e6f-ef7a59853669 | -10.57875 | -47.30772 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 40c3ff74-a157-3143-a15f-6d1e6432f16d | -13.12646 | -46.37349 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 380de638-2ed2-338e-8680-cb02d3b697f8 | -11.64095 | -43.71002 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 0178f02d-ba85-36b7-92bc-3b818dfd1be4 | -11.39435 | -47.57228 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 832a6ea4-4785-3c07-a988-3767c9c7cd48 | -9.43472 | -45.98029 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fb006731-2c58-336e-a45d-e6d06cf34eb9 | -11.84787 | -47.38859 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67f64405-aeb2-3e58-95dc-98457fb9a1b0 | -12.24671 | -44.73664 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1a258744-418a-38f7-91f7-fcbb2e008cdb | -8.95693 | -45.14742 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 81c2df96-47f6-36ed-959d-114ee3eea392 | -11.62838 | -43.71157 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 443ea774-637a-38a7-9504-795880053d6c | -13.4399 | -39.14993 | 2026-10-08 16:18:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6192b31b-1348-3b5f-aa48-693e123398cb | -9.84001 | -46.17172 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 191acd9c-f7cb-37db-aa55-b067c21642c9 | -9.80362 | -47.81324 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 277d7cfd-78de-3d0c-81e7-5d9c787e9072 | -9.73235 | -46.95266 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 68d62d13-51fa-34c2-b376-dfa0364166ca | -11.45538 | -43.38801 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 121543af-05f2-3dac-820f-0f5fda727af6 | -11.61379 | -43.63605 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8bacc815-1bf2-3fa0-b51e-5431b12a8c86 | -11.86562 | -43.5581 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cc10aeaf-cd45-3f06-821f-451b2a5b2939 | -8.96388 | -45.10526 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ccaf7155-524b-30fd-a395-4ea1884f916a | -11.27092 | -45.20607 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d9ff49d0-1071-3200-aafe-28eb797f4ad5 | -8.77738 | -47.2628 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb20983a-f190-394f-a72b-9c8142f34d69 | -12.28558 | -45.31385 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e26f17a2-8587-30cb-8d9a-94a683a9c99a | -11.62002 | -43.61965 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 583dd323-850c-38d6-ac34-baa9f5b6545d | -11.85349 | -47.30091 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5275a80-0dd1-3ea4-bed1-0a1f28e83f56 | -12.22073 | -44.74957 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 57c80dea-b511-3352-8a64-0c1a4eedf140 | -10.47763 | -47.22736 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7380a920-2856-33c2-b561-f598132d3456 | -10.60277 | -43.8436 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9eeeb4f1-1589-35a9-b538-e123d2cba3cc | -11.85949 | -47.39404 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4ae3bea8-caa0-34a7-aac9-93f9191de55d | -11.31164 | -46.70221 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7ba3a7a7-0035-3812-9bee-c5a654b5d55c | -9.97809 | -45.97221 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b3961d54-b5a0-391e-91e4-ba9a9817e458 | -11.24153 | -47.72801 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c69f776-f8d7-37d2-84a3-b911f9faa31a | -8.94424 | -45.15361 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 410db8de-cccf-3c1e-986a-d37081a2bf9b | -8.97105 | -47.55528 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5660ad9b-8b26-3a46-a112-822feadeace3 | -11.0977 | -45.66107 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b596c935-b367-31b6-b2f2-915af1ec91ef | -11.59555 | -43.65799 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b4b0c9dd-c454-39c2-85f3-55216da3c0b5 | -11.59189 | -43.66233 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7c490b3f-6b8f-3ea4-a112-2175ae15e279 | -11.11051 | -45.68537 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c314afdd-b09a-3126-90a6-b2915f80466e | -11.82611 | -44.68694 | 2026-10-08 16:18:00 | NPP-375 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7745f0aa-5c2e-34e2-87cc-02e59e80606b | -11.64718 | -43.68935 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 942d4c2d-32f5-3c18-8f8e-a623b77f608a | -10.48328 | -47.22988 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a27ddb3b-c78e-3453-b8a2-82122ea7263a | -10.80593 | -47.33628 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 166a7365-dfad-3b06-8b16-ab861f0d6f6d | -8.99313 | -45.9132 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d2022a3d-0f4b-3910-85ef-1f25d5a05bc3 | -9.35216 | -46.57438 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9e5c3214-4e1c-3810-aa68-aae0cfb51965 | -11.38649 | -47.55372 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20d32a1c-a424-35df-a3e6-2be653790a17 | -9.00728 | -45.94733 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3b215e77-e40d-365d-befe-877cd6feca25 | -11.7736 | -47.7458 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b8568d1c-1915-3423-a414-b60142bfc448 | -13.45302 | -41.92256 | 2026-10-08 16:18:00 | NPP-375 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 096ea46d-8b11-33d4-9234-eb094f6d9297 | -10.74785 | -44.79837 | 2026-10-08 16:18:00 | NPP-375 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed8e746e-ebc4-3828-b45f-de1284a34ad6 | -9.10512 | -45.12564 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7e67250b-62cb-353b-a8a6-e58a6bacec3c | -11.5992 | -43.6536 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8d2713d6-159d-352c-9114-19ebf95a4ac6 | -12.21983 | -44.74807 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 28e152ec-27ed-3826-b0b1-fb3b0dd22a12 | -8.28397 | -45.72643 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README270.md)
