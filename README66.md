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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f54f9c3b-f0b2-373d-b6a0-4a1ac32d22a4 | -12.30849 | -50.74525 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c8facda-fe22-379b-b55a-4ef4677ef571 | -8.86971 | -45.85979 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09107407-68ba-355f-b6c5-f6c3287b0cc7 | -7.45629 | -46.15958 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd6bc763-ec46-3049-a17b-3e9e4b82da57 | -6.93916 | -43.11438 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| affa9b10-c1e5-3db0-b91a-274e6c0fd385 | -9.92323 | -46.57247 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8d8970a-9082-329c-b826-15acd2ebb086 | -8.67739 | -45.3022 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fd519b0-a0fe-3d46-b6b1-77202ff92291 | -9.37093 | -46.9007 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 557c2d07-36f3-3f21-abbe-624a4f4dddb7 | -6.09787 | -57.68621 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1dc2b29-150b-3b08-8c45-d0e43eca08bd | -11.10839 | -47.10216 | 2026-09-18 04:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e4f8d43-2896-3b37-848e-45c944bcbfe2 | -9.61617 | -46.75319 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01190eeb-399c-3bc1-a748-4de518d00402 | -11.8854 | -47.57631 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a909664-07f6-3376-b289-a72f468c85de | -11.80299 | -58.17555 | 2026-09-18 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 941c6d02-cc20-3263-8832-218a6985acc3 | -11.53663 | -46.88526 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b14937c7-a74c-3d01-b3a2-7dde7474775a | -12.28463 | -50.76437 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a743f3b-0c2f-3e26-9c5c-53e1d574cd65 | -8.48063 | -46.88006 | 2026-09-18 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 243d31c0-045d-33aa-b6b8-12b3cee1e4e3 | -8.87453 | -45.85645 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b36288f-43f1-3006-ad37-861a17a00982 | -7.55509 | -45.67836 | 2026-09-18 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 052ff3b4-fbe3-345e-a967-8545b0a59574 | -5.66035 | -51.89148 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35cdc45a-1e3b-3d54-9a88-3b973df4168b | -7.8334 | -50.23301 | 2026-09-18 04:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78d3f3d2-fb45-303a-94fa-2dead87a7003 | -12.68047 | -43.91258 | 2026-09-18 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f28469b-a52a-3595-a87c-e8b4939332ec | -10.1082 | -45.64502 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 188dcf91-7936-3e48-b466-adfe791c288c | -9.93608 | -46.54139 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53544f2b-9ca8-3075-9fdf-caeeba47c740 | -7.57821 | -46.34478 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b539ab6-69a3-36b2-8892-6a9d13d24b58 | -10.61073 | -46.07992 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 134ed70f-e8ca-3ed0-b442-943864c989c6 | -9.09671 | -45.7143 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee54b7f9-9d24-35d6-b516-686aab0ce2a4 | -12.26871 | -50.75423 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3c1ca34d-1f1e-3989-ab37-01c1e93adc3f | -6.67132 | -43.63935 | 2026-09-18 04:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70af129e-343e-34cb-b127-efbb2b6d3017 | -12.41647 | -50.67804 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60c96427-70fe-34ba-8654-d93822421de3 | -7.79498 | -44.90829 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9a1f85e-9179-38a5-9062-03d3dc41d269 | -10.67238 | -50.27615 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cd41233b-2f44-3082-b5a7-f6bd6fac9912 | -12.05479 | -47.51324 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b10e6882-6dd0-3696-acd4-5954b521050a | -10.51918 | -46.73758 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f07b8371-c7a0-3a93-9a52-5d6b8a53e5e5 | -7.93561 | -44.83707 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4a4766d-5fc1-3d49-b543-f454cdbc9916 | -12.17202 | -46.98014 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28b8cfbf-6664-3e10-8697-21a65647dfac | -10.66782 | -50.28307 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 577e5398-a464-3be3-b672-0fd08cd2e605 | -7.65646 | -45.83739 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64a2fbed-ded8-389d-b6ef-4e17ec424aa4 | -11.33095 | -46.76229 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| debbdc04-72be-31cb-8298-5fecdf4869bc | -9.93714 | -46.53398 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 959fd029-a167-3ae7-9c34-d26feb836888 | -9.94749 | -45.28442 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be89d30b-8b7c-397b-8cdb-4801086e6c6f | -10.64155 | -50.22546 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9eee31eb-b127-3d9e-98a3-f97672c58adf | -10.67979 | -50.27349 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61ad2c7c-da49-39ce-949d-04eeabc0afb9 | -10.69707 | -54.17705 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f7d30ad-e97c-3405-b240-e95e0b5510e3 | -6.95267 | -42.55157 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f86e4ea0-1a05-3049-a2bf-d2f80b7f2033 | -12.17689 | -46.98764 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc9d4c18-f7a9-3ada-aa0e-e80517cb399c | -6.91706 | -41.72202 | 2026-09-18 04:57:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38c8427f-f100-3fbb-b9ca-ef1207e6e1e7 | -6.52251 | -49.88792 | 2026-09-18 04:57:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 94e5605e-d185-3f97-9d94-b83ed742039a | -10.8767 | -54.00342 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c61eeea9-e5ba-30f7-831f-a0e800a01e67 | -10.12777 | -45.56722 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87a55772-3429-31cc-948c-d01d9587cfde | -9.93918 | -45.32584 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f58a1ac4-3c0e-3563-8934-81a08236aba4 | -13.00305 | -46.93553 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2fcb59d-3b3e-3162-924e-24427b34a300 | -6.45325 | -52.8471 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 343a359b-8abc-315d-8f78-6cfe48a3b84b | -7.1962 | -41.8079 | 2026-09-18 04:57:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 149f30db-bda5-380a-8b25-004732bdfc79 | -8.44812 | -45.83367 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3f422ae-8248-33a3-830a-d4bfebf85f1a | -8.91191 | -45.01202 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 372febb5-e061-3e65-bd17-3d51519851ff | -7.47552 | -45.29822 | 2026-09-18 04:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f410714-69ee-3af7-8590-f04844e263a0 | -9.09183 | -45.71774 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcdc9014-35c1-333c-b6b7-a730ad558e93 | -6.65494 | -51.48923 | 2026-09-18 04:57:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 648064c1-3a1e-31a8-a8b4-5207c6557dff | -13.24931 | -46.92023 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 802abd01-a127-3550-96ec-14dd2ccc57e7 | -9.76148 | -46.60306 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e25cedb3-5f71-39aa-bd69-7177147d756d | -4.88046 | -56.07002 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b964263b-de58-37ca-af08-a262fde3b52f | -10.66668 | -50.26762 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9174047b-a568-3ad6-abff-090bcec7a9de | -9.70872 | -54.82199 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 736ea7ab-8d56-3c1e-b5a6-9de9760ba2a9 | -6.66676 | -50.92482 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15df4ed0-2c27-33e6-9c19-979e29860b68 | -8.8827 | -45.88947 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43a702f3-aa40-350c-8ecd-1a631f6a91eb | -10.89791 | -53.99516 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d07f4520-27f0-3810-a14e-d3f56d41a0de | -9.83509 | -48.34481 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74e941d8-54a9-3723-9aba-66a434f78a73 | -6.66343 | -50.92429 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e321b0-fcd8-379d-bd01-dd7115675d4c | -8.45925 | -50.90026 | 2026-09-18 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3d90924-37bc-3ef5-90d3-32b7bd195da0 | -9.77322 | -46.08617 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30e57e49-f151-3b11-8d3e-15da2730fcfb | -7.63093 | -45.83701 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8384dd2-4fae-368f-be36-87ae589956c9 | -12.51481 | -47.08698 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 94aebc69-86d4-3c4c-a292-50454edaa089 | -13.23732 | -42.33364 | 2026-09-18 04:57:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 64a97642-9fdc-3a7e-9feb-a5b0ad3b63c7 | -9.92273 | -46.57596 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 637c6fb5-af72-300e-99c6-1c4352edae49 | -11.31171 | -46.77872 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d757222-dabb-3a12-a4f8-375cd94ff7db | -12.61806 | -50.88819 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1627a6f4-7833-3283-b315-5fcb344d9b0e | -13.00359 | -46.93163 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab48c2e2-c0ce-36e9-9be4-90f22cf732c8 | -10.99946 | -57.05705 | 2026-09-18 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df08b08b-35fb-31bc-9ee2-d8296f192a6c | -10.94387 | -53.05773 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfa09d46-b461-3298-9353-a530e709e65e | -9.18972 | -46.75724 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c75820a-40b5-310a-ad69-4770c021913d | -13.61326 | -46.95927 | 2026-09-18 04:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad40f2a9-1ae9-38e8-9368-4d7fd9d5fcdb | -7.66526 | -46.09341 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ac5a8ed-4917-3c9d-9257-0be7011da502 | -7.45786 | -46.83725 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 628ab1fc-16d1-31af-8fc5-bc985b00205c | -12.40281 | -50.69891 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 375748e5-cb51-3fb6-8c2d-833c27c2ea71 | -12.33636 | -50.76872 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 532cb9d5-4d4c-30cd-bfda-5cb82005bd7b | -10.67124 | -50.2836 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2801f37c-178b-3691-833f-74f79481eb49 | -7.05762 | -46.22643 | 2026-09-18 04:57:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0075f8c7-c6e9-38ac-8c0f-a1753ae8af2e | -8.5074 | -48.49879 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 461ddcf4-e242-370f-8537-d3a3eb1df8be | -10.99884 | -57.06061 | 2026-09-18 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60fc7bc8-ebe5-3181-91d2-d45d55af3e5f | -10.66435 | -50.48717 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c44369dc-5547-38b5-9d3d-68aa6a4e6beb | -12.52769 | -47.08509 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f211516b-76d8-3934-b1d9-b7f288fc989e | -6.65161 | -51.4887 | 2026-09-18 04:57:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2131bbe6-469a-3d0a-8242-c7695f330b64 | -9.93973 | -45.34157 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04db3682-e51a-3cdb-b30c-94cb8e80a728 | -9.18619 | -46.74932 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c6fb22-7e4a-3983-8e09-f5d286e90d25 | -7.06217 | -46.2235 | 2026-09-18 04:57:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 391e71ce-59d2-32ae-97d5-6f242720f5c0 | -10.02843 | -45.57399 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88fbe439-946c-3732-9735-05011b510554 | -7.74883 | -54.74739 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d72e357-4a52-3496-aa1f-002d05ff311f | -7.05641 | -47.47847 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95e39596-6719-3aa6-910b-75f999b1c4e9 | -12.31012 | -54.12378 | 2026-09-18 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc643808-3e3f-36da-98bf-90d49076e8ae | -12.53181 | -47.08571 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f2f6d19-5828-3b18-8029-cc77f4aa2228 | -12.39538 | -50.67855 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README67.md)
