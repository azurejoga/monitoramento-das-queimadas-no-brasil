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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c84819cd-af82-3950-9458-12f2794d456f | -12.18591 | -47.17428 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7744f3dd-62fc-34f6-9307-82de717eef13 | -4.30185 | -49.10308 | 2026-09-11 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b4fc732f-dd93-37a1-8fa4-799ef5b9fd98 | -5.68581 | -43.38971 | 2026-09-11 04:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8770e65f-bb3c-3e27-b2cf-c3291064d8f7 | -7.34877 | -44.19197 | 2026-09-11 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55db5145-33b1-3f51-b231-757d969310a0 | -12.38038 | -43.4358 | 2026-09-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59f3fc79-4bd1-3cb7-b231-b2b9d5ddbb79 | -6.12168 | -42.5662 | 2026-09-11 04:08:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 73827b51-f040-3d97-8fcd-96ab545f1217 | -10.05855 | -46.28477 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5df98b8-f698-38e5-b503-4892a675899c | -10.05704 | -46.26895 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbafb78a-8f2c-3dc6-9e6a-ca90732c29da | -10.46873 | -48.65533 | 2026-09-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c5fc34e-ada2-31df-9fd3-e2b4cbe21732 | -9.15491 | -49.98589 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd4edbae-2dc0-355c-8ce3-acf4b6bfa3ff | -5.66794 | -44.94384 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f20dd9c4-73c5-3be0-8e96-2269517337e8 | -8.38997 | -46.29764 | 2026-09-11 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa800ec4-e96e-3b81-a0d0-d10174980dcc | -6.9499 | -45.21377 | 2026-09-11 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c66ffc88-85c3-3728-9eb4-3a167501942e | -9.3148 | -44.35364 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0251efde-3e7a-3c28-b921-285052899318 | -7.33194 | -38.91927 | 2026-09-11 04:08:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99789ac1-7188-3f75-9b76-7aaa4ec74f09 | -9.36794 | -49.38015 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| badc0b08-fd24-3807-8ba3-ad7414af9e27 | -8.50522 | -50.15142 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7574707-69b3-394b-82a7-b53126ae3970 | -5.48249 | -45.12903 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d19078c3-3dbe-3348-aaeb-2f2a3c6044f4 | -10.72908 | -46.14948 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a988a3-d864-3771-81a9-0edda63feb67 | -11.10768 | -47.07609 | 2026-09-11 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae98fcc4-8f3c-3ebd-bf65-8c0a706392b8 | -9.36341 | -49.37621 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 373a855e-be5f-3b47-b7fc-0c1444eccd05 | -7.1792 | -43.60697 | 2026-09-11 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c9e090-08f2-3dcf-b467-e615b03ba69d | -10.75679 | -46.18788 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b6470c-d0ab-3e68-b3cb-ee3c25b4c0f7 | -8.78164 | -44.18379 | 2026-09-11 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1078f24-cf0e-34df-9398-d0376f5d0aea | -8.07704 | -38.22308 | 2026-09-11 04:08:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0eb9773-b174-3322-a07b-5ee6f7d4ba29 | -10.97588 | -47.87813 | 2026-09-11 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba4a16df-b2ea-3c08-a6a1-9170a6df00d4 | -9.7831 | -43.4464 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b59d98a1-e8a8-3fa5-a942-6bae25e9200f | -10.36376 | -48.14035 | 2026-09-11 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9542fe32-b12f-3570-88e8-0058cc10f90b | -7.71917 | -44.62645 | 2026-09-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de72fc31-acca-3c80-8f32-167591f26edc | -10.75147 | -45.92335 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d00f70c-2b8c-31c9-acfa-d9940015ced6 | -7.96776 | -44.00262 | 2026-09-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73021b9b-311c-316f-b3de-dbaa667a0782 | -8.49915 | -50.15399 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb72eec5-1ea2-315b-a60f-04be5f0f75d9 | -10.54862 | -51.35544 | 2026-09-11 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c231878-c3d8-3361-9845-56194a2dae0d | -10.7877 | -45.94282 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 323e53b7-679e-301d-8cc8-e22809941d8f | -10.21909 | -45.22122 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbb323ab-7a7b-32a8-894a-3793edab0e36 | -8.15804 | -45.57815 | 2026-09-11 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae1eed1-b51c-33e3-9e2f-20d41f5765c3 | -9.32844 | -45.65155 | 2026-09-11 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91c08ca5-02ce-336c-a848-b748d9290132 | -12.57549 | -44.09949 | 2026-09-11 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f706c57-72b7-3629-a96b-f716e22e3bc6 | -7.18283 | -43.60756 | 2026-09-11 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c1ad51d-566a-3e7e-8984-b9cd6c1d2537 | -8.03083 | -43.8504 | 2026-09-11 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1f1b0d77-de4f-3d7c-a1a4-bff31d5ad640 | -8.49979 | -50.15042 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a93a36-f995-35d3-9da5-1e136b347590 | -4.7753 | -46.49735 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43051a33-0406-3bb9-9396-b4879ecc7b16 | -4.23932 | -49.94784 | 2026-09-11 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8dfbc4ba-eb1e-3ee0-b683-5f76c5f2534d | -10.05575 | -46.2765 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 370c294a-4c96-3dd7-a4b8-27717f1fe6af | -5.47796 | -45.13285 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecbd072b-4d00-3f05-b9cb-6f90036a087b | -10.78042 | -45.9444 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4880eed-66b3-3d84-98c3-14f9d32a54e5 | -6.02467 | -51.33411 | 2026-09-11 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a194779b-f7f7-3035-9b91-91513cdeaf64 | -8.63359 | -47.42213 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39579a24-a82c-3846-a71c-fd39c749a78b | -5.38595 | -45.64269 | 2026-09-11 04:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fad60616-dd8c-3483-87d4-b6efe417f2a1 | -7.97068 | -44.00766 | 2026-09-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65220512-8bbe-3ea3-aa52-a19d6af8c68b | -10.60238 | -45.22556 | 2026-09-11 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9df60105-f0eb-37cc-952e-b1ee6aea9ee4 | -4.77078 | -46.49663 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54a81423-34c1-3ec8-89f8-4a29538d0e67 | -8.6299 | -47.41667 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1403430a-355c-3ce3-8ccf-0d03845a8114 | -6.12549 | -43.75037 | 2026-09-11 04:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a480dc72-d785-3c0d-8382-bbea32558853 | -4.30064 | -49.11008 | 2026-09-11 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f7ad5be8-6964-39d7-b8b7-0ad3f611251d | -6.23832 | -51.687 | 2026-09-11 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec439d53-5c56-393d-8c69-28a45f0d8a56 | -6.12621 | -43.74594 | 2026-09-11 04:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ab34a07-70da-317a-bd40-54c5ffbf3763 | -9.68831 | -43.47498 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd28cf10-3090-3e33-981d-7be35144f332 | -12.11441 | -47.28005 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a3f0235-9ceb-3954-905f-0a064e168604 | -10.77732 | -45.93869 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| ec6ad2a8-3304-3a90-a0cc-0852e7326067 | -9.89845 | -45.9011 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e51f825b-99b5-389d-874a-2db29518f8e0 | -10.67098 | -49.08157 | 2026-09-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0b3a7f2-bb57-3da4-988c-581c11fb6a8d | -10.64172 | -46.12958 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1a8121b-2237-3bcd-90d7-78f820900074 | -7.81172 | -42.78002 | 2026-09-11 04:08:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6cb38f1d-918b-3cdb-a161-731584ccb02c | -7.9306 | -49.7339 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19406a24-1cf6-3d8a-a825-b7cf5ceedda1 | -10.74064 | -49.59384 | 2026-09-11 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14cc87a9-e61d-383e-9a50-c8d33187e9c9 | -10.53588 | -46.34988 | 2026-09-11 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 438637bb-f66c-37d0-a043-f472a78f6565 | -8.91069 | -37.36337 | 2026-09-11 04:08:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a310bba-6818-3d20-8a8b-108cbfcd773d | -10.35927 | -48.1389 | 2026-09-11 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 724aff0d-0040-3253-a470-87ff3594abf2 | -10.53652 | -46.3462 | 2026-09-11 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2804670d-cb70-3a05-bcb6-27bcd9c4f476 | -9.39486 | -44.58823 | 2026-09-11 04:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93ff4cb9-e98a-322a-a075-7427f7ac3a2d | -10.05511 | -46.28026 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9603897b-8dd4-3de6-86f9-aef8ba75789c | -7.7616 | -44.57798 | 2026-09-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2219bf78-1a4a-3da9-9e94-369012d65557 | -4.56293 | -47.7615 | 2026-09-11 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36ca473-9579-3157-baba-c3bad87fb37c | -8.62538 | -47.4159 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85a6be42-751d-3f5d-bc6c-36f689c842a2 | -7.97217 | -43.99886 | 2026-09-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f287b09-abbc-3dca-9e20-5f3f65614ebd | -9.60453 | -46.7799 | 2026-09-11 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bad401be-3764-379d-9b7d-0068aa4a200e | -8.70766 | -49.62402 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4babf9cd-4b16-374f-a9fb-ac69ccd2cfa8 | -7.1571 | -44.74291 | 2026-09-11 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45bcdc3e-e89e-3d28-a631-2ac91d6784a9 | -5.20053 | -45.55973 | 2026-09-11 04:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e57b3328-00dd-3026-ad7f-8a9bdf8518cb | -6.29037 | -41.71408 | 2026-09-11 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7aad72be-5cb1-30cc-bf2d-4b7802dbeb68 | -6.01835 | -51.33368 | 2026-09-11 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 009f4af6-0a0c-37d6-bc16-5dcd90bd0a83 | -7.80888 | -42.7756 | 2026-09-11 04:08:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b29419ea-3b84-3415-9a04-a9097889448d | -6.33102 | -43.75209 | 2026-09-11 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f775213c-7b9e-3e12-af72-322fa2ca2f0c | -6.71732 | -45.48243 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b87f2c95-99ce-3ebe-adef-cee9ce468790 | -9.05932 | -45.78259 | 2026-09-11 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0299dbb8-86b2-3a53-9f28-593248f4f9f4 | -4.24003 | -49.94382 | 2026-09-11 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8d791b2-159a-3cef-adc8-21e0a0f39bb3 | -11.40751 | -43.95001 | 2026-09-11 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2f75769-2728-3ff7-995b-9cacc9a853a3 | -7.9905 | -44.00203 | 2026-09-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e90f0df-3044-305e-9ae2-c43c906a546d | -9.32447 | -45.65092 | 2026-09-11 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd4145f4-97af-30b5-baac-95520ed5e5e7 | -7.92526 | -49.73298 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74765a4f-9c20-30b2-b702-7bece7b67509 | -8.48605 | -44.74654 | 2026-09-11 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1b12420-ea8d-3443-9b8b-d0ab6bf48b31 | -10.13518 | -36.31645 | 2026-09-11 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.1 |
| d19caaef-ee4d-30b3-b9ec-aa0eb1f5fabc | -7.19362 | -43.58753 | 2026-09-11 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80cab29c-d64b-3ae4-878e-847e09e20d31 | -10.77339 | -45.93792 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b62a7b49-fb3d-313f-853e-cd21293b944c | -4.8218 | -46.80949 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 307ec508-ef2b-3a29-a454-7e2a6581b8d0 | -6.7202 | -45.4904 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6878bca-4411-30cd-b8d5-bf4bbd8eb984 | -9.89905 | -45.89751 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1b68bc7-8fc5-386d-9ee3-3834cf4729ac | -11.41103 | -43.95062 | 2026-09-11 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38ea9c86-5a0d-3338-b3c0-3f1ec2b36831 | -10.97511 | -47.88251 | 2026-09-11 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
