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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0522dd1a-680c-3cb9-bf68-5dbae3862fc4 | -11.4627 | -44.87155 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24bf179a-cb4d-3ef5-95c4-595496338768 | -8.9319 | -45.04309 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 76947be5-5bd1-3303-abed-dad5983e5bb6 | -10.05363 | -48.69467 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84bf1c3a-e35c-39b3-8cb6-78d8ebb4268c | -13.70887 | -39.65087 | 2026-08-31 16:30:00 | NPP-375 | ITAMARI | BAHIA | Brasil | 2915700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 89e1ab6b-3044-3b3b-8f31-fffb842c9500 | -11.91417 | -45.05342 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 21432364-2e1b-3317-9e31-89df32715a19 | -10.15918 | -45.71992 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c7206514-cd05-3b98-82ec-5d4d95c99139 | -14.47894 | -52.21006 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2a5a33f6-2d0f-391f-9777-24c94bcb2c14 | -10.11549 | -50.31776 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 6c1e69a6-1d05-3cb0-a5e0-29787a3e373f | -9.83198 | -46.35743 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7a8f89b5-7363-35d1-a452-38603fc024dd | -8.74347 | -46.46445 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3dad92d4-8d48-3166-8900-2d45dac362a5 | -14.51771 | -52.2921 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d1248e5-0bd3-32ab-a59e-5dd6e2d54aa0 | -10.56561 | -46.16389 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| aaa1c355-86ba-3500-90c2-bdf25ff7c872 | -10.10174 | -50.29193 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8d379a79-5acf-35c4-acfb-81b63d24c9d7 | -14.79679 | -48.26566 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bb686b0d-9458-3a35-8534-2b97072451ce | -9.97085 | -46.83382 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6d9fce1b-87e0-3ce9-911a-4951e009459b | -14.04439 | -42.39381 | 2026-08-31 16:30:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a7041db0-20ce-3fd6-b2b9-a077f937afb4 | -11.91557 | -44.8461 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b184951d-283f-370e-b2ba-749d79d8fdf0 | -9.99705 | -46.39901 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0f863292-3146-391e-ba96-6b82c4e962cf | -10.98021 | -48.41832 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9de0be52-12cc-3223-9b58-8d98db675198 | -12.10666 | -47.27115 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c6a54e7-d166-370c-b97a-33ca76d78aa0 | -12.18387 | -50.51998 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e264032b-361c-3786-914e-793f8a473ad0 | -12.10378 | -47.14863 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ac9eb84b-2d83-3561-9c18-3be3a2d917dd | -11.0323 | -49.67612 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 03e299a0-d2fb-3e15-85ab-5c0c5659486b | -10.85203 | -45.34477 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| cf722792-f513-38c3-aab0-81d9ccc30ee5 | -11.92537 | -45.08641 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4cff1caa-038b-357c-ae68-f4583074ee61 | -11.21751 | -46.09834 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 25966bda-50d9-3d24-83b9-3949b970f6b5 | -10.40272 | -45.08854 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd92a7d0-8272-3a7a-b1d4-9fb5aee58c8b | -15.01665 | -52.75518 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2f983e84-87ad-3edf-b3ba-9271e35f56e8 | -10.15269 | -45.75528 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3bd8b317-797a-3525-835f-46d27fdc7422 | -14.45058 | -52.51429 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 28d193d2-93ba-3f7e-abc7-ac7472f68df7 | -9.16217 | -41.19065 | 2026-08-31 16:30:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fb24254c-3eaa-3b4d-b8f4-632630a755b7 | -11.93633 | -45.0764 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c0440aac-de2a-3e98-9a80-d3b1bd390af7 | -11.25023 | -45.14376 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| de5150c6-74c0-3a96-801c-a0902d4122b8 | -12.09025 | -47.14085 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 94819598-04c0-3fb2-b594-809bb261fa62 | -8.92831 | -45.0436 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 08384a80-29d5-336d-be97-1a9fd1523704 | -12.10505 | -47.24896 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e5a89da7-0fba-358e-9111-78b31ff40df5 | -11.70415 | -47.61207 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 04a03d5d-13c5-3c4a-a619-687dbd921cb8 | -11.07345 | -51.52862 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5dd87e1f-5b95-3aa2-a6bb-72f02024e2c5 | -10.99477 | -48.38784 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 9ae290f1-9eae-3deb-b8e2-229a2fa87991 | -11.07954 | -51.5317 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 58d1aa90-08a6-3e76-869e-e42dd24bb85c | -9.65523 | -46.06543 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8493f51f-ed37-395d-8c05-00b297d47616 | -11.63352 | -49.41026 | 2026-08-31 16:30:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 728d8671-20a4-3d16-a1c8-89dccd96eb2e | -9.21409 | -51.56606 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 836f1f9e-9627-3e24-bb1a-1b91c355bbf7 | -9.68915 | -48.12384 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 50874c90-0d47-3716-8eac-8b71efec6937 | -14.37517 | -51.1218 | 2026-08-31 16:30:00 | NPP-375 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e182d8ce-24c6-34f9-89f4-7a36ccf05b7f | -14.58389 | -53.61766 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8bd9a33f-6469-367e-93b9-8f027a031010 | -10.9268 | -50.62321 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 0f672048-e970-328c-9fe9-b2180ec9a444 | -13.54708 | -48.2314 | 2026-08-31 16:30:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b4c31ce0-a75a-3cc3-847c-45e422b1322a | -9.67474 | -48.31849 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d06e5d7d-faff-3f0f-a32f-e152ae304d03 | -12.45279 | -47.80899 | 2026-08-31 16:30:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 425b92b6-d307-3b0c-9dbd-0dd8d91dcb00 | -10.15403 | -45.76466 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 27796713-0926-3c1b-b9ca-c77eaff80c37 | -11.18688 | -50.62814 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9af686a9-7d4e-330d-8c0e-fadd73d794f8 | -10.40825 | -45.0799 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0e4a2c3-5777-3ccb-a3a5-969f53f0ac3b | -12.09634 | -47.15781 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 76f753a2-61f9-392c-ba34-b6d0404d500e | -11.49842 | -50.35128 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d83107de-a28f-353e-ad5b-d00b6519a7ce | -8.76209 | -46.45653 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f77739f9-eeb4-352e-bfa4-ae7d7ab82120 | -10.74301 | -54.02841 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 4d301b14-6f81-35ac-a825-df45111d1312 | -11.2524 | -51.25447 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 293785ce-1b68-36d1-a1fd-dbb26b7d6889 | -14.5655 | -53.59965 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3d86f6d4-428c-3fba-a6c9-f5e01b3caa93 | -14.21831 | -48.6502 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 79080c74-f84a-325e-9aef-5139cdf14222 | -9.68302 | -46.54358 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f6068bac-4524-38f2-a5a7-df8629eb827d | -9.65838 | -46.06013 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 023ccdca-f025-3f93-a283-5f1461d5467b | -14.96335 | -54.59146 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| aacbfb40-a7dd-3734-a624-f87d2f80b372 | -8.87415 | -47.08599 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 668b1113-d321-39d7-a385-9a4813c4ce70 | -11.25193 | -54.00698 | 2026-08-31 16:30:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0757cb7a-0c05-3fa1-8e85-a36c70839bd5 | -14.57212 | -53.5983 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| cb60aeaf-d83b-3016-b637-087e56a5021d | -10.6471 | -50.68771 | 2026-08-31 16:30:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eaabb01a-550a-364e-bca4-2693eef52d7c | -13.48076 | -49.18147 | 2026-08-31 16:30:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bad30060-6d54-37ab-93c6-b83641035fcf | -9.40786 | -45.65678 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0214a156-5f0f-377a-9ed1-38d465958265 | -11.91474 | -45.08514 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 3fab9e6e-59f5-3348-b8ed-44223da91650 | -10.08785 | -45.86295 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2812bb1-68d9-344e-b819-dec4d8bce45b | -10.14714 | -45.77049 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 8a33facd-54c7-3dca-afb6-619ac7de6b59 | -11.21496 | -46.10901 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4ecedc1d-6fd8-31a6-8b3f-ba9f59fff871 | -12.8778 | -45.8422 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f3ca2fb5-e6fe-3293-9268-bc848f516ef2 | -10.10135 | -50.28892 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4838c9c9-abbe-39ef-8e02-0ca173569875 | -8.76557 | -45.38495 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 441d58dc-ec65-39c5-b605-b95874b88265 | -8.92953 | -45.02672 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4406f297-d1fb-3a70-9667-53213cd2693a | -9.68121 | -47.93512 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d8d7e670-a93e-3463-9546-b564fca32192 | -11.67246 | -47.6069 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d37b30c9-9c52-384e-bae2-7863025c5510 | -14.79102 | -48.74509 | 2026-08-31 16:30:00 | NPP-375 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff09a973-a876-3ba3-9c84-38908a206c03 | -13.84776 | -54.09129 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1b337841-211a-37c1-b213-b15a78beefb3 | -9.65073 | -46.06126 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 34f904ca-3f3f-37bb-98b0-6d11cf936ab8 | -10.67009 | -46.2836 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ab718711-6379-3ca6-b32b-4ceeb1b908b6 | -11.32785 | -45.17506 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c485d2f1-cc29-338e-9636-71f4f8ae57c8 | -14.568 | -53.59542 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6564b469-19dd-3a93-809b-3cf27fb2cb59 | -11.32659 | -45.19312 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5af3cc6b-7681-37e4-b074-0aafcdccbcf7 | -9.30254 | -40.56684 | 2026-08-31 16:30:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 212b8f28-59fe-3d18-9500-25f207245452 | -14.21924 | -48.6468 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8958ba15-257b-3228-aac9-cfcc5921def1 | -14.58129 | -53.59338 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 39d1bfea-e645-346e-8b9d-2a175ecb4c44 | -11.3664 | -45.42289 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 51a15832-4c14-3d93-8ca7-4563d052519f | -14.06 | -41.74796 | 2026-08-31 16:30:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5b4ea969-f0ff-3755-b072-ba7b1a36aa0e | -11.93511 | -45.095 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d23832de-ebf0-333e-92f5-73514b38e097 | -13.01083 | -39.73862 | 2026-08-31 16:30:00 | NPP-375 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6c8160a2-61cf-339c-a18f-65075d957c41 | -9.46633 | -48.19247 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 12a8691d-d769-3fb7-91e6-371c741b556e | -14.58322 | -53.61139 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ef2c7157-ee99-3dbe-b568-b8e47f4774cf | -11.17876 | -50.56255 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5d2abc3d-5795-322c-9c86-e840e2972482 | -13.4638 | -51.41187 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d871d58a-1650-3140-8b2f-e586c54968ea | -9.21002 | -51.57779 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 86427abd-3236-34d1-9cf0-e1e8550766ee | -10.93302 | -49.61135 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 089305b4-2a88-30bd-bcaa-62873a4ffb11 | -11.33642 | -45.15524 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README125.md)
