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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14e7aa0d-44eb-3ae2-b948-eefaf81336f5 | -7.5982 | -43.4409 | 2026-09-21 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0bc17e66-0857-3062-8397-4530bb36af82 | -5.61131 | -44.84473 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 1d65feca-8b2f-3950-bd43-9e4588d0658c | -7.0605 | -49.91541 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f222d079-e43f-3ff2-94e2-9ff4e27ddece | -6.53424 | -44.86352 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 05aba644-4fc2-369d-9f90-502dfb7b2e83 | -6.32205 | -43.37799 | 2026-09-21 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1350f28d-2935-3461-882e-d0f5b1a5cd47 | -7.40555 | -44.79503 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| bea31640-37df-3bc2-9c24-cc24cebc8e37 | -8.49325 | -47.02261 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2c971dff-aca7-3566-a125-2ecc03d3d09c | -7.73137 | -43.89076 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a945569e-9afe-3776-9a2d-e5da1b194eb6 | -6.14163 | -47.5063 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15a749d1-c041-3ae9-8eb8-790bcecfc69c | -5.40453 | -45.70513 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 35fa6214-24e5-365c-a456-5f66e3962353 | -3.71753 | -41.10928 | 2026-09-21 16:03:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 80b29e7c-1cf3-35a8-8abf-e273d24ac643 | -5.83371 | -43.85904 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 73aff8ec-b0ba-359c-b84f-bbdba6a03ff7 | -2.24857 | -48.75148 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 731372a3-03c5-3036-9289-db88cf24023e | -4.39338 | -43.04669 | 2026-09-21 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 79abedf9-865f-354a-b36e-9e4bd7b156b9 | -6.97716 | -42.58329 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 8669046e-6bdc-33de-bc7d-de1a67b12c39 | -5.56889 | -45.51871 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c09da0c2-2e3f-39ae-99bf-696e3e1cca55 | -6.88489 | -41.70253 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 21aa57ad-f9f7-3493-b80a-da9ae7543620 | -6.01055 | -44.97118 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e0d2d135-d078-3e8b-b739-760b2256e259 | -6.64649 | -47.69829 | 2026-09-21 16:03:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| def7eb49-6bcd-3775-86cc-ff06c773d137 | -5.74375 | -43.71944 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bcdacd82-d121-342c-9c4e-b2bfaac169c5 | -4.95216 | -37.41851 | 2026-09-21 16:03:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 59f9ac5c-5c52-3765-86ce-6614d59578f0 | -6.55436 | -42.57251 | 2026-09-21 16:03:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ce1bffa2-80c7-3dcf-980a-a3d582a6b907 | -7.06486 | -43.67417 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c26a8842-b8eb-31dc-88ab-5d99c35644c8 | -5.6339 | -40.87297 | 2026-09-21 16:03:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 00ddb9dc-ba75-3493-88cf-b9557aa4a89c | -5.56815 | -45.51362 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b11ae009-08bd-3e37-a72e-896920e8b9d2 | -7.05769 | -49.90687 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| bf4eeda6-d77f-3f65-9000-939758e31e01 | -7.4514 | -44.68477 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95630370-5e4d-37d1-8367-384c37eee47e | -5.76487 | -43.6898 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4febd102-0423-35ee-b99f-15a46471668a | -5.82641 | -43.86802 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 791bef5e-0efc-33a6-871c-621a2d904ac2 | -7.74894 | -46.72541 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| c8a70b43-b210-3589-bd3b-ea70d563f759 | -3.33304 | -42.54539 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2709933f-e691-3101-95af-407145df07eb | -3.45004 | -50.61585 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| b6123ae4-4c3e-31f7-b721-b23b2f08bad1 | -5.6533 | -43.41441 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| af45b805-c315-387f-8e94-a3b4c9a7c0ba | -6.6421 | -41.71971 | 2026-09-21 16:03:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 246b1df8-18a1-3393-a774-5f9ecd0f308a | -5.76223 | -47.28558 | 2026-09-21 16:03:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52b96ca7-c5eb-38bc-9a3e-3733da6a6d62 | -7.41013 | -44.79428 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7fa32b00-ebde-34f2-a4b3-09b156a3bd3a | -5.76709 | -43.70479 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7be6759-0136-36d3-9877-cf2a5aff893e | -4.79585 | -43.64329 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4bed014f-2f85-3232-9f45-383746f5c452 | -5.99418 | -45.24786 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 811ecdc2-e1c2-34a2-9d0c-70671133b658 | -8.79762 | -48.74797 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 35cd7887-bc09-3a96-8dde-7331e85af573 | -8.37294 | -47.26921 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b669827d-0dd9-33c3-a174-317a31c85b88 | -7.12913 | -48.43723 | 2026-09-21 16:03:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 2fd7a5fc-63a9-3e04-a54b-785e1199abc0 | -4.17033 | -42.00637 | 2026-09-21 16:03:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 447a69c2-ccc9-39d1-bfe0-cb8889f508e2 | -6.85799 | -44.57346 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d81d2e93-20cc-3cd8-bcd4-e2e1b858b410 | -6.79824 | -43.89767 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 450ce58e-11c0-38b5-9e38-43074ae956fe | -3.81186 | -40.71199 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 32.1 |
| ce66bb61-27cb-35a6-aa1f-3eec90332b22 | -7.31989 | -44.1896 | 2026-09-21 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c6bb642b-d5ea-3414-801c-4a031fbf4dcc | -6.53555 | -44.87275 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1aa476e2-1503-38d3-96c7-202fddffd751 | -7.13816 | -44.04393 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5a5a46a7-1f63-3142-bd71-bd2cf72440b2 | -5.34256 | -45.98328 | 2026-09-21 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1c493e6f-2748-3616-825a-b21f9881b64c | -6.16434 | -47.51035 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9b3b5a12-d807-392a-a348-6977fcf8aee0 | -3.9748 | -43.286 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17d5ce98-a5f2-3d99-a355-74312d5d2039 | -6.01247 | -35.46212 | 2026-09-21 16:03:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f8f0ac38-a7b7-3d84-86fe-73f4c8f5c7ec | -7.54323 | -45.21415 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 27c14ca8-5cad-3af4-89bd-f233a6c4d4ab | -8.43415 | -45.81912 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5b851ee-a366-3e7c-9662-6d36c469c16d | -5.90088 | -45.9956 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6aa666db-e250-3771-8431-76319d2a210a | -6.16931 | -47.50623 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 64ad5e38-cad4-3e4b-a15c-1d211dcc424e | -3.21291 | -42.46534 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cbab7268-c3a5-3a84-8ddf-b3d48b01d7b0 | -2.45702 | -49.23341 | 2026-09-21 16:03:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ed153f51-d697-3b0c-a7ab-94d942acf88e | -6.28985 | -47.64306 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 748d8181-8a7e-306d-aef1-39337c0dbd69 | -5.29991 | -45.75917 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5c25005-8771-3801-973a-07dcff3f82d7 | -4.51686 | -44.96409 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 966058d1-98b6-36eb-b4d3-f9a5a45e99de | -5.97876 | -45.07639 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 423b9165-1a33-31a1-85e3-fc8455c65fba | -5.75209 | -43.71834 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6f39d3ce-1384-3e59-aa9b-c47963562b77 | -6.4821 | -43.70867 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fd046865-8431-31fa-a95e-7b0a4a15eec0 | -7.05267 | -49.9053 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| db612aba-3fd8-308d-bcfd-be863afa3c51 | -3.44924 | -50.61048 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 85be014c-67b9-3510-beee-10bdda9d359b | -5.61559 | -43.38296 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 32552762-d46d-3465-81ec-217ca9f4ec0f | -6.24336 | -41.6569 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| d99ed540-500b-3e9e-84d8-98363fedbab7 | -6.71466 | -44.00816 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cd6e5f37-592b-362b-b049-daaa2962f893 | -5.55174 | -48.44277 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e154fe50-11eb-3019-87b9-3a65db107cdd | -7.39766 | -46.16678 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c6801bce-a425-3953-85c0-6931e43eed3c | -5.81632 | -43.85753 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e5da724d-25fd-3f67-86b2-5e8b6d0678e5 | -7.53164 | -45.41474 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ec55eebe-31db-30bf-afb5-f65806f5e88f | -2.6226 | -51.73146 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 818f631a-c89f-3fd9-8687-0443d1d4e0d3 | -6.56359 | -44.8413 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b52dafac-28e7-33df-91a2-da0d733e4832 | -5.2146 | -43.1486 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9c120bf3-431c-3ca0-b855-b343ebfd7e5f | -3.78529 | -40.13933 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5787489c-4ab5-3f89-a9ee-541aaa717286 | -3.32141 | -42.55419 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a48e3a53-83d2-305b-a2a5-11c7aa538a67 | -6.54972 | -42.56804 | 2026-09-21 16:03:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b609d688-289b-341e-9a5c-0adce3fccae6 | -1.7726 | -48.55204 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9937df6e-6116-3391-9042-32e51ddf251c | -7.16382 | -37.71493 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 669a10c4-58ff-3c5f-b2c7-5a262760f482 | -5.61306 | -43.39435 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 15870420-c1d5-3a74-9988-fab8163fc87f | -5.80901 | -43.86653 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5b1b3f28-47f4-3747-a654-272fd0dc1260 | -5.62069 | -43.38966 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| dfff413a-02e5-37ab-af4d-52105e87df74 | -6.10784 | -35.28377 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 842e2b6e-c8e7-32ed-9d05-b4f74ed6b47f | -5.74153 | -43.70426 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0036d95d-5701-3db2-bee9-ab9e9d93b109 | -5.59067 | -47.43695 | 2026-09-21 16:03:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| baa041ec-8d41-3b9c-ab8a-c7eead679847 | -7.40065 | -46.15139 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d9b3b09b-6aca-3c19-bb7e-58191b8694fc | -7.59192 | -43.42653 | 2026-09-21 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 524e40e1-b602-3e64-9421-36201df0bf02 | -6.23095 | -45.42599 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c9ef9c39-f8c7-3f48-84ef-4a22b2b3c690 | -3.83755 | -40.60206 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |
| ba46c7b1-3d59-388c-b6fe-c389e5a2be28 | -5.19082 | -42.95957 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5a9a9e23-f507-3bc0-8499-4c970400e1d0 | -4.52732 | -43.88534 | 2026-09-21 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3781a46e-53ec-37e5-a53c-3400aaf6a252 | -5.53468 | -47.42715 | 2026-09-21 16:03:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab934286-5bad-335e-bda2-5c921461be7f | -3.33574 | -42.77513 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| fc5c12c2-317b-3ae2-a6a8-b2652f328f8f | -6.47577 | -42.77602 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 61115445-2dd5-38ef-aa66-dc347e79a66c | -6.54729 | -44.85723 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| d020732d-3a55-3e3e-bc30-d6d5e9f9a2eb | -6.04072 | -44.85947 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85569f33-24f8-37d9-94c5-6c0d26b8abee | -6.42782 | -36.21025 | 2026-09-21 16:03:00 | NOAA-21 | JAÇANÃ | RIO GRANDE DO NORTE | Brasil | 2405009 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README170.md)
