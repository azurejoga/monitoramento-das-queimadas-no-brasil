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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1374eb9f-64ce-367f-8aa2-1c2b32c9217e | -11.0845 | -48.27483 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11a808ee-d34e-3d73-a639-33154c5e3317 | -11.06422 | -48.26758 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14447670-0d89-358d-a3ca-491b56c29135 | -5.74359 | -57.60466 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 808e3046-4f7b-3b9e-afbb-53a44ce0f21f | -10.53791 | -46.74439 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ab95866-cb90-3079-867f-cb5a7981b0e8 | -2.83849 | -60.26577 | 2026-09-19 04:57:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff3bdbf1-0af0-33d0-9a62-8da2f4febd70 | -9.99578 | -50.27974 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ae195ed-38a2-3674-b1b1-d4b5eff8b625 | -3.77931 | -49.82608 | 2026-09-19 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7211be67-6ddb-389d-a587-ad4489d74283 | -8.65869 | -45.4503 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2fd5e9b-1f79-3137-9b9f-c00a5408d376 | -6.33476 | -55.27833 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8166c90c-9a31-3f60-a9f3-910edf7a43df | -11.32744 | -47.35028 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27a4ec36-62a6-3f28-a22d-c5d2c74b149b | -4.50354 | -54.97063 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc62a5c-5008-3093-bea5-7b4727e0294a | -5.89281 | -49.79226 | 2026-09-19 04:57:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc215b66-fd36-3b4d-bb98-59ac8ff5eaa9 | -3.38035 | -61.30297 | 2026-09-19 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e62189e-bc19-3061-bb7b-24b3b419c424 | -3.36478 | -50.46001 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90964c48-a305-3097-bf42-b6083319b462 | -10.98791 | -48.29597 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1745f21-317a-3f6f-8c60-c7b7c5fe7e5d | -6.36318 | -58.29296 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bd34233-4b68-3cf7-a37d-8cd0a33db37d | -8.77819 | -48.67118 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 984132d2-bfdd-3805-9b50-6cff07885e70 | -11.18194 | -45.38662 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2745bb05-2d03-336f-95d6-225c84e3a248 | -9.79349 | -48.32961 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05daf0f0-9e91-3ee6-9d80-28474df6c3d4 | -5.83171 | -52.04688 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 109bfb13-77c1-307f-b860-d9e3f59de2e8 | -7.55979 | -61.33513 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39a6cbe3-c70f-3c8b-bccb-500117e28b1d | -7.86278 | -46.44635 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 71445256-de68-3c57-bcf5-f95f6a23781c | -4.49081 | -55.49703 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7204c6b3-5972-35c2-90a0-3f38d543123f | -9.57312 | -46.55781 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55c14311-d963-384a-b626-eb973ce31cfa | -5.81011 | -57.73125 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6d3cfb1-0b51-3373-a5b1-627635d11409 | -10.47074 | -51.259 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82904ecb-f478-391c-b515-edce189cfa3c | -3.45312 | -50.61057 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08cef518-ad43-3a56-beda-dc52ab3af8ba | -5.14189 | -45.77332 | 2026-09-19 04:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a900472-b52e-3ead-86ee-c57330558604 | -10.59258 | -46.5436 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bca1c21b-3253-3dc1-a3b6-2ecb0a7c174a | -6.02192 | -52.15464 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e75ba3ab-a135-3246-adae-98fe1bfe7af7 | -4.14778 | -48.22425 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c490c8f5-4ba7-35ad-80df-bf11c2068850 | -8.49638 | -57.62444 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fab64dcc-87ea-3df9-88f1-3196131ee5f3 | -8.76883 | -46.91763 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0d380676-8f6f-3152-baaa-78a516ed8777 | -11.11992 | -45.27946 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3932ced0-4d09-3225-8f02-bf0032f1b13e | -9.15727 | -59.46806 | 2026-09-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3efcd248-e3b4-3b7c-866a-11e63d0684df | -11.1168 | -45.30344 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70092622-9910-386f-84ae-0bc154b456e1 | -6.70901 | -59.45816 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f60d22b-83a0-317b-8fea-5b4e2b8c9d93 | -11.07795 | -48.29073 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbcde06b-98fb-3d59-b08d-903ff2a59061 | -10.55303 | -51.31465 | 2026-09-19 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd7fbf78-d88a-3cd4-beaa-9e39dca9182c | -3.4503 | -50.60643 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 69e0388a-e470-344a-bb3f-0a07e1100f92 | -10.44873 | -48.68358 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bec1042d-d339-321c-a8d4-474226e42d52 | -10.48344 | -46.30194 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89521988-efbc-32a2-b40d-8eb716046f77 | -10.50243 | -46.2674 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1e3b8e3-1f66-3102-b5dd-37c1d26b4d87 | -3.35573 | -50.45117 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1884347c-fe3d-3d00-887c-d12464cd7723 | -2.89188 | -57.79069 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9b2a6db-3710-3b4d-8e0f-c9a5ab7179a5 | -11.48367 | -45.7324 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8adb39f-f846-3e81-8bed-61c447865104 | -6.93072 | -55.02689 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5b5f80b-66a1-3743-b357-69123ec3c4f4 | -4.35609 | -55.42997 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0388d57e-12de-33f7-b3d6-e6dd3ab8ea30 | -4.49508 | -55.4935 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6384f37e-4184-3730-ab83-75dab4ca4edc | -7.77624 | -44.89456 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb0428cf-d694-303f-8688-1116579ae169 | -10.79977 | -50.8957 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a942c5c-8fa7-363f-8d0d-8de9a7c7f0c4 | -11.00449 | -48.32975 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ad79b0e-3670-3522-bbf0-2b75e4b95d79 | -11.33453 | -47.35423 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3bdd9d6-f4da-3284-9238-58aa64a759b5 | -7.57523 | -44.90954 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9fac822b-f6c7-3e66-bc43-ba827d2cc836 | -5.8971 | -53.56343 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb9abe90-c99f-3201-866d-ad543e798cb1 | -9.95548 | -46.56178 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3d685c8-6f00-3974-b90f-c8912e0c1584 | -11.08351 | -48.29034 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2844ba5a-5346-3f98-befa-22026f4f080a | -7.85591 | -44.87316 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5ba7f69-73c7-35d6-9f79-f53481f0ea38 | -9.55543 | -46.58409 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b642dfb4-2c02-3858-a3e1-aa0ad7c34ff0 | -11.32228 | -47.35463 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0eb4592-3f6e-3fcb-baf9-0597e2672dfa | -3.04634 | -61.27081 | 2026-09-19 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11681147-a078-32be-a670-58351a66f437 | -6.67521 | -50.91056 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c1fbe3-51c7-3818-835c-1d915ec2288f | -8.73722 | -52.35806 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27eff1a1-7152-3d88-a31a-f146ee8b2b1e | -6.74187 | -59.4276 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bee9cbd-c533-3534-b589-85861136514f | -8.84271 | -50.45324 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c36107bb-3aed-3213-b8e9-242d82198647 | -6.5853 | -44.14897 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 762075aa-2797-376a-a301-7b78378a2690 | -3.35913 | -50.45169 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a92a4d14-2c2c-3f3b-8639-9b043ce56591 | -7.81423 | -44.95279 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e83406a-81bf-308c-921d-11fb62a12f32 | -7.56443 | -49.60505 | 2026-09-19 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dca8211a-f16b-3efc-8ee8-98891d8c3869 | -10.17218 | -48.52781 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1b65b2a-2d4b-3e69-9369-d6b6e19bf3a7 | -9.78834 | -48.33666 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfeb8b3d-29a5-352c-95e5-b17477e5a2f3 | -9.23548 | -46.18681 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bce5ada2-3625-3c1c-be6f-cb2418b7b95e | -8.73276 | -52.36464 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 436a9ddd-b12a-3f43-b6c8-2fbfff808c69 | -9.05084 | -48.72526 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f00b25a-3537-3ecf-b6d0-725f0d0f104b | -6.36733 | -58.2937 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fd1b4a5-9edb-309b-b68d-4293f0998275 | -4.71394 | -55.68997 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f06894f-e813-35b3-9b14-4e6f37839774 | -11.32556 | -47.35338 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0cfda4a-2e65-314a-b681-97080e0a7d57 | -3.33558 | -59.813 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4d3167d4-3362-3c62-9549-34a7c8791bad | -7.36255 | -50.32655 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb221514-d50e-36c9-a0f4-296503ca2315 | -6.10478 | -55.64106 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f0d414c-b8fa-33a7-a03e-e901760734a8 | -10.46031 | -51.25694 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ad2c3a8-1716-3d36-85a6-8a2a9504f176 | -8.77179 | -48.6632 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 88e78044-33e2-36da-b79c-853664739f94 | -5.33461 | -48.98671 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92229331-f7fd-35cc-b05f-f9a8f5381bb7 | -10.13933 | -45.56463 | 2026-09-19 04:57:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e9dbf90-bf49-371f-b396-a72256cc8de1 | -11.30153 | -46.76535 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 822001fc-ec3a-32c1-9aa7-cb0606a74ac4 | -3.21172 | -53.95136 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f5db044-c765-37e3-bd80-fa66ee127908 | -5.65134 | -51.70312 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d2df6fd-3246-398c-9207-9a68e3254c3a | -7.40207 | -49.84329 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99386ee4-3764-328c-b371-1761f31d5bae | -3.3347 | -59.8183 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 22014b67-bb0b-3505-a1cd-f79f66f4c6cb | -5.76192 | -57.44798 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f6ce8d8c-dd9e-3c9e-bee0-fbe1dcff5450 | -6.92728 | -55.02633 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 154e4d7a-cb47-3903-837d-64b28f39c839 | -9.80901 | -46.40766 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0bf3fe-5ff6-3900-bfe7-77500e3ffc47 | -9.00211 | -44.91832 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deca5422-65a1-3303-ac20-d6e1144c9444 | -8.11824 | -54.82113 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb7571aa-ba44-365d-acfc-2176e0584ead | -9.95344 | -46.54209 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9749fec-d632-3408-9712-9550a5151baf | -11.06366 | -48.27147 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46d0780d-c9cf-3598-af1c-c0b1158e1ac6 | -4.59912 | -42.95869 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f5dd562-3609-382b-b0c1-5fe4c6434dcb | -6.00575 | -51.80565 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b85483-2f62-3d6c-9969-4ead348c9b29 | -4.49935 | -55.48998 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7825ea88-2151-31ff-93b8-bcf683fb00a9 | -5.74418 | -57.60118 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README76.md)
