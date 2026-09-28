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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0191e8ab-dee9-3b8e-8479-0d6b83d1b6b0 | -10.9342 | -43.88747 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 412e9dd0-d726-3830-9877-a60389ec3a13 | -9.39883 | -46.38581 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 4cceced5-c5b6-3b58-98c9-545040536464 | -5.63845 | -43.72352 | 2026-09-28 16:26:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f115ef7-9d8e-3d4b-868c-ba4c592048cf | -10.20366 | -50.00505 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3edbccd9-917d-3fb9-a1f7-b7873683a569 | -10.46099 | -47.47952 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36025699-faa2-33b3-afb5-4c5859b379ee | -10.91362 | -43.86707 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b3bac7e5-0775-3d4e-8908-ac1303230fcc | -9.65943 | -40.62621 | 2026-09-28 16:26:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4c3c3c78-63c8-3a1f-aa21-049f0a245748 | -6.86943 | -42.84713 | 2026-09-28 16:26:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bf4bd3d9-7dfc-339e-bea3-1e9f68e5fbe3 | -3.53556 | -43.01926 | 2026-09-28 16:26:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bb9d39d8-5a56-30e9-9962-2cfe95a92d55 | -10.39016 | -46.52994 | 2026-09-28 16:26:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc099f7c-abbd-38d6-8c9c-659cba0c13b7 | -8.03582 | -42.84222 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| fd78ed58-d76b-362e-baa3-548c2e946780 | -10.91941 | -43.85849 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c4394b99-c4d5-3b63-bd03-0950b134acc4 | -7.28932 | -44.30845 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 863b0bc2-23c1-3c49-885e-1dd194a6d130 | -10.11632 | -50.19007 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0b864755-a672-317a-8aa4-ff53b72abd7f | -7.26388 | -43.36834 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| deafa062-951e-31ad-bd90-d97ca25fb78e | -8.94761 | -45.89701 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 46c69a4a-1606-3c05-aefb-7b4175d57d0c | -8.38857 | -45.46707 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6fe098d8-c733-3240-9d2d-b832e7d4cc38 | -3.38596 | -42.59546 | 2026-09-28 16:26:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18fc01fb-e49c-357a-af94-1de4647d387d | -6.34576 | -38.85914 | 2026-09-28 16:26:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7a484c58-50b5-366e-8eae-8878ea8787ab | -4.37439 | -43.06589 | 2026-09-28 16:26:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 94ed86db-f754-334f-aea4-da7e14a86a90 | -9.77279 | -44.83856 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42f9005c-6175-35e3-810a-effaff6a8599 | -10.30299 | -48.16468 | 2026-09-28 16:26:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8cc93b4b-c21d-35b4-8833-2e6ce97eb57d | -11.02421 | -49.71164 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 89cf230d-53db-3175-86d4-505fec477759 | -9.32714 | -46.56157 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 543caefc-5359-3b02-aeb1-5aaa5fbeb9d2 | -10.23885 | -49.99351 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| a01d5341-a858-3849-9faf-fe624389a6f2 | -8.66123 | -45.3621 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cd863135-a62f-3ef4-8898-2dbf0c759d59 | -9.17937 | -45.79376 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| aba68eed-180f-333a-8c9e-f2a2a00604f8 | -5.42048 | -45.91342 | 2026-09-28 16:26:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 48c8fc4a-e86e-3945-b007-dc8b065a5dd4 | -7.38818 | -42.08935 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f2e62b9b-b8b6-3054-90ac-376335005683 | -6.21768 | -41.58945 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b36011bc-ab5e-31b5-9e8a-ddc68f0581fc | -7.69161 | -54.75194 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1a46b74d-c852-32e0-9653-5e92c9781411 | -7.20462 | -45.08202 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3b46c3d4-4790-370b-9cc2-d589ec161d35 | -9.97246 | -50.14408 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 88702b58-8369-3988-937c-1cc9bef23f47 | -10.29034 | -49.96382 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4f74e526-3574-3583-b884-03d74de24532 | -8.65046 | -45.41462 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 82b4c69d-e34c-3866-b528-7fcc4f985bf6 | -11.14985 | -50.0638 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b2b0ec20-da68-36de-b7ec-18202a8b6c5d | -9.51984 | -46.36578 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 0a9f714e-9660-37af-bd89-c1a3f242a8a5 | -7.03842 | -43.874 | 2026-09-28 16:26:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfead658-13d7-36f2-8c9b-173befebd625 | -10.61538 | -53.99182 | 2026-09-28 16:26:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c67bc73b-8aec-3fcf-9544-167ce5b4471d | -3.95435 | -38.3611 | 2026-09-28 16:26:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 888b3744-f62e-3623-b8e9-2ad19932597d | -10.24919 | -44.61443 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9e995a5a-cd52-3219-94b7-af7e73afc5b0 | -8.50615 | -46.89776 | 2026-09-28 16:26:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b564855-e1cf-34f4-bf0f-ef64632e52e0 | -7.26055 | -43.36884 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d7a3791b-02e7-3772-b978-dc0aaea5cada | -6.34291 | -41.9167 | 2026-09-28 16:26:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 623f16df-6184-331d-bd8b-e313aa00bd72 | -10.08635 | -50.39188 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 338a26f6-e228-3da3-83c4-f0ecd3349033 | -8.97271 | -44.14967 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 5337b972-b081-3be1-8bc5-b29958e6599a | -6.35039 | -39.30476 | 2026-09-28 16:26:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| a301941f-9f86-3bcf-80d3-802dd1b9164f | -9.76866 | -44.83508 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 5abc10be-da19-377d-9768-ae9e21bb6a46 | -10.59608 | -50.00002 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 22e7a5a0-defb-3a2e-a0c5-dfdf51817cbd | -10.16763 | -46.56893 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 129dd4bc-61a4-341a-9103-bd7fa731f0c6 | -7.67983 | -44.79874 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cfadf5d3-b952-3757-92ed-5f0af9435857 | -6.43709 | -44.57638 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b83867b0-3b68-3fc6-b201-eb634cb7b499 | -9.07875 | -46.49803 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c5bc2391-7e4c-3461-91d5-970242ddacd8 | -5.54268 | -45.20001 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 002f4d33-59b2-3116-abe4-a3e602f3e685 | -9.77574 | -44.85891 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7e2454ed-f281-3b7e-8ed5-904859390561 | -7.522 | -44.58124 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1663b459-1bb4-3017-a380-7d09c8a1f7bd | -7.901 | -45.44686 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 2e72067a-ecc7-3e97-a5ec-c44fa62da66d | -9.51803 | -46.38097 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9926fd17-c4ca-3dad-9011-5776f68bf614 | -8.10162 | -44.00576 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c8cb365d-c8fb-3347-bab1-667ab9169e71 | -11.08012 | -48.89339 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 021c5f2b-a4cc-3bc9-a832-303a66f886d2 | -6.55637 | -40.37861 | 2026-09-28 16:26:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 91abff81-cb36-398c-af35-78bea854cc95 | -6.16446 | -44.67399 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 57e3fb55-87bc-3cbc-a59c-d8ea9f474458 | -7.66808 | -49.53424 | 2026-09-28 16:26:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ee629a12-61dd-3024-92d4-1b62ecf5e534 | -5.823 | -39.29002 | 2026-09-28 16:26:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a8c26a7c-357a-3355-808c-3736fe3e5bcf | -10.20633 | -49.98745 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9bd389a6-808d-3f84-ae72-5e1cf3b02d44 | -7.29742 | -43.32027 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a5fc4efc-98c0-3530-90e1-a82b5b77b66f | -7.504 | -44.57603 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c06bb9c0-60fe-3582-81fc-2260b2e023de | -9.07555 | -46.5033 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9ebfc6c2-0035-31ab-b392-a0c079c87a4f | -10.29208 | -49.96748 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d63c0cfe-0934-3151-83d4-51c1235e9579 | -3.88354 | -40.84017 | 2026-09-28 16:26:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 20.4 |
| f8f5559c-8e0e-333c-be42-0704204a9b0e | -11.47109 | -49.74325 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 077cdc0e-0098-3572-b87a-3f3e1b045b3f | -9.18097 | -49.65493 | 2026-09-28 16:26:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 525e24e3-4f6e-3040-8bcd-9ea0784259ea | -6.89048 | -52.47723 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cddee6bc-0e96-3993-bba7-c910631f5ae4 | -10.71306 | -44.42874 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 55f8e966-2ce5-36b8-b13e-61d76df422cc | -8.63851 | -49.47921 | 2026-09-28 16:26:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c31f99ad-54be-32a1-b562-c75c7288c9f0 | -3.80506 | -44.09648 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4c4b8af-db3b-31b2-992e-40d105122138 | -6.7347 | -43.00972 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 8581005f-aaa8-3bca-abd0-996b05376d07 | -8.3011 | -45.42149 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 12cbc3cc-2c31-39c9-9e3e-496aaf6893b4 | -10.60952 | -49.98661 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d654b85-cb05-3373-98a9-5b3db100b828 | -10.08596 | -50.38889 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| eb947dd7-6925-3f37-958d-ec67e2909ec8 | -7.37803 | -42.13358 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 80213907-93de-32a1-9a7c-c1d608b1869a | -10.01272 | -45.17957 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 31049411-34da-3c7c-a54f-7e24c8092fec | -10.91018 | -43.86756 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 10afa16c-e4b4-3794-b2b5-07ed4070b828 | -10.13565 | -43.90253 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8424729a-c9f7-3eec-a5aa-b86abfdd073a | -10.26804 | -44.62017 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 35c94481-b877-3368-a84e-cb708915efa9 | -9.44584 | -41.80822 | 2026-09-28 16:26:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 7bc3898e-a885-3505-964c-8bf918e5c047 | -9.79702 | -44.8308 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 3cf9535f-31c7-3ee8-9545-392bf8d60f06 | -6.18855 | -41.66043 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5c841c01-89ed-3f73-906c-6e092560688f | -11.71997 | -50.68513 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4624a4ae-4bf1-3ad9-9c4f-e8420b1cbff1 | -9.97095 | -50.13264 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f8bfe9a0-9af8-3cc7-899c-bda124ee0bb8 | -7.50949 | -44.56781 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4a8d98c4-9f9a-30af-ac40-22eab28052a5 | -11.17801 | -45.13966 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ccfa523-3848-3537-b094-a86607301a4e | -7.66931 | -49.53666 | 2026-09-28 16:26:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b3ef80e-ad3f-3f5d-a99d-c8fb2f7a966f | -8.30529 | -45.42513 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6edc8612-eec3-3ace-a8e1-28928ba6d630 | -10.96634 | -50.67294 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e2b05275-c5fb-3898-a164-b78441d184e3 | -7.62735 | -45.52289 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57ce6db0-29e4-3e44-903c-628b62dd0872 | -7.44729 | -44.5961 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63feb2f3-7abb-315e-abef-0f24fc19ae47 | -4.20939 | -42.98695 | 2026-09-28 16:26:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6016c340-48d1-3cee-a3b5-086ceb00cf85 | -8.93021 | -45.05245 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 82b6d3d0-88cf-3b8b-94ab-6c9c3981b9d5 | -8.73516 | -44.90444 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |


[Clique aqui para ver as próximas entradas](README118.md)
