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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a04265d-f106-3684-b50a-fbbec10f9ca3 | -4.82815 | -48.10183 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d7299478-b369-3e86-ace5-5afc2c8b5925 | -5.0433 | -45.87648 | 2024-11-09 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8a0f071b-4405-3598-8924-e150c4815b9f | -5.1967 | -44.92508 | 2024-11-09 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 271f1955-4235-331b-a67f-0e024f7f14c3 | -2.46537 | -46.88411 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67931f8b-34ac-35ba-8873-24e10b75d3a1 | -5.1196 | -37.56227 | 2024-11-09 00:39:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 90827518-558f-3f33-ba77-21034e951068 | -3.79766 | -45.85888 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ede26696-3c22-3f2e-9d29-6d48e590127a | -2.29638 | -48.55429 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c6288054-3c6e-3b12-9d1e-2ffe5fcb1529 | -3.14812 | -45.15939 | 2024-11-09 00:39:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5fc68a82-3cc1-36ef-8e8a-dd796134012d | -2.89577 | -46.8038 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| beb90c80-3c1a-3e3a-8b69-3c7478a1c84a | -5.93812 | -39.65802 | 2024-11-09 00:39:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e5d369ae-df0f-3e6c-937c-05afe45f201b | -2.11693 | -46.229 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 230b6599-90e0-3424-84b0-8938c7b3eb9e | -3.95936 | -48.99885 | 2024-11-09 00:39:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 279d8a0b-cf45-35de-a0b4-d79e6a456314 | -1.95188 | -46.30132 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0dd316c0-6981-35cf-aaaa-83f03f6a591d | -5.93225 | -43.65719 | 2024-11-09 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ca805e7b-31d0-3e05-b5b7-7fbc08594548 | -4.21658 | -48.54739 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 45530733-bfef-38e5-b0a8-ae492dfe6a2b | -2.08118 | -48.40628 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 736ff87b-f5dd-3081-9cac-069ed319b5d6 | -3.30191 | -46.40652 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0beb87b5-95c3-32c7-b539-0c60fca57e0e | -4.19407 | -45.8625 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5099967a-9540-3f5a-bed0-560b60a19e44 | -5.50888 | -47.17556 | 2024-11-09 00:39:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7267f9a0-55ea-37c4-9535-23d51f14b353 | -4.61902 | -46.54647 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b396dac1-d93f-3063-9d85-8a7026c92279 | -3.04276 | -48.0436 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 15d76ffe-099f-302b-9526-8c2edef4036e | -2.08759 | -46.4815 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7b807a09-bb0f-313b-936a-f64e176c4d3a | -2.51051 | -47.46024 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 786fdee7-450b-3b98-90ad-046d4cb777dd | -2.99277 | -49.23901 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 1bb1b7c7-64c7-3cad-beb3-7e16fd0f09af | -3.56353 | -43.58573 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 353e52e7-70ac-36c8-89e4-376f541e1c8e | -3.33779 | -50.0729 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bfb395ef-f8b7-3cc9-a2b9-9e388d15c328 | -6.99962 | -46.32056 | 2024-11-09 00:39:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c630dbfb-d7ab-3f66-a244-b521d7476078 | -3.10495 | -53.31741 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 3b61a0cf-8b3a-39ab-8140-ed4ee0223fa7 | -2.53292 | -47.30577 | 2024-11-09 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e69e9bfb-a9b4-3fef-833b-da5c6d8623ec | -3.63656 | -45.89358 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b66a1488-51b0-3f16-a9be-7227d313f7c8 | -3.96173 | -48.18419 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 81fd6e46-ae4b-33f2-8c86-4407b7fc51b3 | -5.46971 | -43.64454 | 2024-11-09 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 248e1a90-9b08-383e-8cb4-528300b1315f | -2.31732 | -46.47837 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0f458ed8-e8fe-3226-b123-1af650cd8c4c | -2.24592 | -46.49429 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1061455-4f0c-3853-b934-2dbf5718a449 | -2.86649 | -50.41526 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c68a1695-269f-3bf9-88f4-4422520534be | -2.59672 | -46.10314 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8560f33c-dd8d-3552-928b-1282b533effb | -2.37048 | -48.57393 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 12352c6a-b3cf-3a1b-a5cb-0298fbfeb5e4 | -5.1443 | -46.21073 | 2024-11-09 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| baac3a7a-5087-356f-b9d9-c67a88c0cb57 | -3.03284 | -48.04498 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ac07b936-0192-3caf-a9dc-cc4689530264 | -3.26178 | -46.31363 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 26e74772-6984-3185-8fe8-ef0a764f6cfa | -3.2542 | -45.92533 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 807f50d8-5274-3430-8917-d12c6e90510e | -4.18514 | -49.99492 | 2024-11-09 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 40f6b378-8fee-3fc9-941d-7ffde25a9676 | -3.82679 | -46.00372 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75f43179-eb11-38c0-971b-b3af2e3d8f1b | -3.95851 | -48.16074 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| bf293f6e-ed46-3a32-b51d-1db59eb94ac8 | -3.27392 | -52.75765 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9d5a0d15-ac03-3e50-b80f-c7cc2f46095d | -3.2301 | -44.42575 | 2024-11-09 00:39:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3c0438d7-bcbf-384a-81e7-ccd83b91eef8 | -3.53342 | -50.33226 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 467bc197-d72d-3602-b6dc-082cb11b0599 | -1.1469 | -53.66182 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 5868f117-10ff-3504-8f70-faef89d90861 | -2.97647 | -47.92796 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 2608f9f5-df6d-3150-9e4b-0146e4592148 | -2.09735 | -46.35249 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 53663efb-fc2b-354f-bf20-e0260f0e920f | -2.83191 | -45.47124 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f50d25ee-0aa8-39b8-8605-98f7e2281f0f | -3.54156 | -43.56073 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| aabe91c9-460d-316a-9d51-c003b05d354e | -1.95315 | -46.3104 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 326f9fa9-390b-3afb-bdb6-8fe13db9370a | -2.46467 | -46.2114 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2874c516-a25f-3ef0-8471-3e6a08958a80 | -5.85444 | -44.08299 | 2024-11-09 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ec192dd-a9c7-3283-8586-20ceb48d8794 | -2.57198 | -48.18547 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 13ce66f2-6b94-3eee-aa50-408be34e2abe | -3.31014 | -45.66391 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 71bdbb74-9bf4-3430-82b7-11d8b2d313b9 | -2.36923 | -46.85488 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| c12b815d-18c5-33b1-b417-2faa09563b0c | -3.49947 | -51.03284 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e111c204-7a8e-319f-a069-719118f45a9e | -6.2771 | -44.74421 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6a4ccee2-ef23-3c36-8083-6e24205451cf | -4.88521 | -44.59402 | 2024-11-09 00:39:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3cde466e-bbfe-31bd-ba5f-f017c66dbb91 | -4.49836 | -45.99872 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d97486cf-5249-3ac7-9652-de2fc54ef50e | -3.97531 | -46.41413 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 53d85c57-1e50-3b30-a648-8a4abf8b145c | -6.23806 | -47.27191 | 2024-11-09 00:39:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e9f2560-8514-31af-9dfb-a7943bc84370 | -2.41638 | -46.13135 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5c7de74f-d68c-3483-886f-f627231c103f | -2.43547 | -46.26786 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 116ec915-cbba-38d7-92c2-9f1ea3e1c008 | -5.56843 | -41.79995 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| cfff10e9-35ed-3204-aef5-418c04f48bf7 | -5.80911 | -44.48283 | 2024-11-09 00:39:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 44e2b174-8268-3024-9024-8fb8eceeb6a5 | -4.35607 | -46.82848 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 5965cd76-cef5-373e-9a13-b140881d83eb | -1.72552 | -47.91117 | 2024-11-09 00:39:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c9bdeaca-d617-31cb-bf1d-7fddb24d98e0 | -3.22886 | -44.4169 | 2024-11-09 00:39:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 26.3 |
| ca1a57b4-2212-3dc4-805c-98ccdf49ca31 | -5.44013 | -44.81839 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 04287930-d72e-33b5-9567-fae63b430d3f | -3.96378 | -48.12415 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 133522e9-a9e3-382d-9b22-ed9c18411d34 | -2.8891 | -51.73476 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| fd9d3bfc-013d-3c05-a8b2-6e01d25aacf4 | -2.2342 | -46.54323 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8f054f84-8c1d-37e3-8287-6a67a205eabf | -3.08209 | -50.56249 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| b16d5c38-38aa-31e0-8e15-48acf0371b15 | -2.23668 | -46.62844 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fda535eb-2654-37a9-90c8-1ed3ff6580bb | -1.18622 | -51.99755 | 2024-11-09 00:39:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 7a968885-6966-329b-a0d1-9484371262d2 | -2.40832 | -48.40721 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed6acad3-150f-3fbf-b64d-a5daa51c2cc6 | -4.41016 | -43.38103 | 2024-11-09 00:39:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 03b69dd4-329f-3a32-b38b-c2f55d54c2ea | -2.92523 | -48.67036 | 2024-11-09 00:39:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8d414674-a6ea-3b1e-bf97-8bbb184cb54d | -2.09609 | -46.34335 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3081c587-9017-309e-8a4c-11464856cd97 | -2.57952 | -49.1438 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 38079d66-31d7-3e0a-b5f9-1b975c0ee046 | -0.40483 | -51.48068 | 2024-11-09 00:39:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 26.7 |
| f7be32d9-72bc-340b-882f-a63f31e2ac77 | -5.58607 | -41.69336 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c29ecbff-f50f-3050-8df3-fe3b014928b4 | -3.78995 | -46.13722 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 52f5fc2c-b080-3516-bb5f-c3fc437a50d2 | -3.39051 | -52.37188 | 2024-11-09 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| cf3d6f07-700d-3681-a391-1539bd7002f8 | -5.26396 | -45.8746 | 2024-11-09 00:39:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3cd3f3bd-73ff-3814-8bab-da6502bab445 | -4.21206 | -45.85997 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 269e639c-a17f-313d-860e-6bf25575077c | -2.26283 | -49.68502 | 2024-11-09 00:39:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 325e65c0-4a04-35be-96c6-74303edc8e49 | -2.56507 | -46.53587 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5b408f28-8fa9-3c14-80cd-6d0d14fa6358 | -2.67704 | -51.81864 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 006919a3-ba47-30b8-9148-312ffbef0451 | -5.04165 | -46.80769 | 2024-11-09 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ae33037c-2b68-38da-a8d1-57100b66c529 | -6.18031 | -45.4405 | 2024-11-09 00:39:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5b850e67-4134-3e2e-8ca2-c5a3274bd3bb | -2.36265 | -46.80716 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| efe78154-6e4f-3bdb-98ce-b0dcd24a92f3 | -6.18158 | -45.4497 | 2024-11-09 00:39:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| fd7912c5-d09e-37b6-9e1f-45f97f677307 | -2.36913 | -46.58498 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ea1e2b48-e525-35e1-9c51-b50d661c838f | -3.79576 | -51.29288 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4cc69a9a-5026-3e3a-98a9-45947a4a0541 | -2.23677 | -46.56185 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 7e6fc0a5-c5ff-3ed5-aa84-ee01c79f125a | -2.45662 | -53.69091 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |


[Clique aqui para ver as próximas entradas](README7.md)
