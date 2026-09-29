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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f2479b5-1792-3aa9-8864-9afc3659277a | -13.52448 | -46.91295 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f5fdaae-65f6-3cff-8bf4-1393778a467a | -14.34497 | -52.12928 | 2026-09-29 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f01acdc3-03c7-34f9-9197-ffd60b7d9a9a | -11.60625 | -44.13903 | 2026-09-29 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86fd6a77-66ef-3c07-b7c8-65a929690128 | -12.95286 | -46.64716 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19100704-5549-3093-ab50-0bf639b55786 | -11.40745 | -43.41998 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b8ea184-b645-3acb-80c6-6a68df14872d | -11.96886 | -50.92382 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7a55dbb-ebde-3ef1-bbfc-e46d8978784c | -12.73689 | -47.31622 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa6c36d-2a1d-376d-bd60-0ba4444570b4 | -10.28689 | -49.96574 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 85490196-1c84-38f5-a40e-ef8bc20d416b | -11.71481 | -43.45349 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2ee820d-1380-33f3-a1bc-bea0eb57af24 | -8.73974 | -47.87664 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5cfe321-0f1f-3f79-be43-c63f0823bb14 | -15.15756 | -43.61569 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c67df60-535b-3dd0-941c-d0e390720365 | -11.13479 | -50.07236 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67c72546-be7d-33c7-aa5a-cafe0ce2bbff | -11.43646 | -43.47565 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13f6903a-2810-3f5e-86d8-61049c1050ed | -11.43974 | -43.45427 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c63d1f8-c366-3837-87a0-0a253dbda695 | -20.09478 | -57.20425 | 2026-09-29 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7e37077d-bc91-3015-ba06-72ecdcc25f27 | -12.04604 | -50.94968 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ee844421-68fd-3bb5-9276-f9ee642ec366 | -22.16719 | -49.23725 | 2026-09-29 04:17:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eff0475b-ea42-3add-9a25-a21f0783c7e0 | -13.48299 | -48.6162 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4e71d3f-fa87-3d3e-9aae-322d2dc70d0b | -11.87453 | -47.08556 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68c32b83-18a7-33b7-8499-7458efeb0dd7 | -12.01788 | -50.93128 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 03813cca-a72b-3679-90eb-7d9ff7c938ab | -11.36462 | -47.43773 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef9cfb5d-c85e-3b5f-b291-92c4355e18d2 | -11.41691 | -43.42511 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42b2e6a5-6adc-3f02-9395-b0ae9c2c295a | -14.46334 | -45.23143 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7b883d2-6a17-39c7-974d-7e0ec89d368f | -13.18026 | -48.56304 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 910318a8-6204-3346-956b-9d9e1b024d51 | -12.47628 | -47.48441 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c5d3dec0-875b-34a8-a0e6-efc8f7593c24 | -12.05039 | -50.95048 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef59f8b5-e2a7-335f-8c6e-5b047f9e1c2d | -12.72076 | -46.99126 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b04680c8-ed9b-37fa-a9d8-e53a3765d2a8 | -14.77091 | -47.15823 | 2026-09-29 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9e77d37-6b9f-30bf-b991-aef91f55bd8f | -12.77366 | -50.67556 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ef70004-cc4e-312f-9532-d9efdccb8e25 | -16.77725 | -39.41972 | 2026-09-29 04:17:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c4fa5a11-edc5-3b75-b3d5-7dfdf2231a15 | -10.28075 | -44.63073 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f404009-d11c-3fdd-a256-b70e6f38518d | -14.96442 | -47.53838 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8936ca2d-35c2-3586-b8c9-cf3d16e6dd5c | -16.78157 | -39.4203 | 2026-09-29 04:17:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef02ca40-4313-310a-afed-ef4b48025ad4 | -12.05549 | -50.947 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ee1253cd-a809-3576-ae07-1c67a7d5e342 | -13.0305 | -42.67192 | 2026-09-29 04:17:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0e65795e-f8fa-3bef-9a43-f7b3da12c176 | -14.09076 | -46.30957 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27aaf759-4f25-34f9-99c9-d07cca5966e2 | -22.24445 | -49.56124 | 2026-09-29 04:17:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d4b29ed-bd43-37d7-9cf4-11ff6f317fc6 | -12.03886 | -50.93952 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a92a5dbb-4bf8-3917-8bba-83fecb6ea749 | -15.38542 | -47.92723 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a9e655ab-b745-3f72-b512-414a0ac9bcbf | -11.44923 | -43.4813 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8829b66-0b6d-3c1b-ba0b-0a21bf5a5ef5 | -15.17925 | -46.12523 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d129e54d-a901-3e29-a39e-ef4bae9d916d | -12.87974 | -44.80524 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa8ac4e6-4490-3624-9cf6-c32b1fff8d0a | -12.66135 | -46.98603 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27da5b14-0aeb-3e52-adfb-61ee5383cceb | -10.21295 | -50.01342 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7866f5f-0ef2-3e26-9036-f50ee1a6ba58 | -13.43441 | -48.61866 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17af80fa-8c07-385d-847a-56520caf3ec0 | -15.50883 | -46.21453 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a935131-daa5-351b-8b15-76bcb4f19367 | -15.3959 | -47.92894 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6e9c5a8-5a81-3c20-91bc-4493c1ad657d | -15.00329 | -47.86998 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48dddbaa-e181-39b6-b07b-683bf0032a40 | -12.01968 | -50.97141 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 231e91eb-3b47-365a-ab53-d982b0456982 | -11.38437 | -54.05183 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb061e6-bc78-3043-9de8-3daa4e7a0a86 | -14.09382 | -54.3019 | 2026-09-29 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae9ad514-b628-3ac5-a895-cd3ee60626f5 | -12.00409 | -44.92498 | 2026-09-29 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4561c806-f7ae-307a-9978-74ba6fe1667e | -10.26037 | -44.63101 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a5fa05b-65b1-3350-8f61-207902567bc5 | -12.02404 | -50.97221 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| cd0d249a-049c-3de4-9a03-82d7461740d1 | -11.17414 | -44.79359 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 6ef9f373-b23f-3b0e-a9ea-c0154d519884 | -12.17354 | -50.69461 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8c83d21-2b34-36f1-9615-3ec5532924ed | -11.36163 | -43.36498 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58de91c2-4223-34e9-9618-02685192e270 | -10.21132 | -46.70717 | 2026-09-29 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7dd7164-457c-35b2-a60b-b7db99634401 | -11.19727 | -44.79731 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da66c964-37a6-37f2-8993-cad534abec86 | -12.88202 | -44.81636 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a068d2-58b4-365e-86b8-0523e4bc0778 | -11.3825 | -47.44041 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5504a3f5-3d7e-319e-94ba-fbe402bd9c39 | -11.09528 | -47.11474 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1b8b10b4-3228-3975-be98-f3f180fad432 | -11.38032 | -54.04384 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4254deb-c08d-3a8a-835c-5b8d6b24b16b | -13.14571 | -48.54915 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c68cc16d-ad1b-3fa3-bbb2-c62a5e479ec2 | -11.98808 | -50.99677 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e6c1fa-6cdc-301e-a7c5-efd58495b9a0 | -12.01456 | -50.97491 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 614d8cf0-3cb7-3c8e-8496-c10486612bdc | -13.43365 | -48.62318 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1dfb4dc9-7bf3-3dd7-b384-626d44a98b3d | -13.73801 | -43.66522 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef9c985e-5d23-34e8-a718-ce5eeaaba3a3 | -15.24308 | -43.27169 | 2026-09-29 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 81.8 |
| b75f86a3-d795-3d85-bb11-c3402f669b3b | -11.39623 | -45.40886 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12fb24f2-3042-3099-90b5-7fae7bfa1f10 | -10.70477 | -44.42341 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16befa92-d2dd-3c63-9cce-c5c985bfdc3e | -12.63029 | -47.25837 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f2233e3-8af7-33b9-b275-bc8948ce7113 | -12.01405 | -50.95265 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc6e09a1-d1ae-3f9b-9224-9f0ce438309a | -13.14133 | -48.54647 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8129a4c9-a30a-3482-860a-16a646cb1a71 | -11.38814 | -43.45713 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a236c5fe-9561-3d28-b4e0-a93d4ff9ffe4 | -13.34075 | -46.81211 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c4954a2-2223-3634-a98e-94b2c1cfbb32 | -13.53203 | -46.91057 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46a87bb2-1ead-32fa-a776-4ea3564c496c | -11.97844 | -50.95057 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 138ca2b6-036c-31b7-b115-f954602d927d | -12.1562 | -50.39829 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b4de9b7-c1b0-3f52-9e96-0e93f1b4d429 | -15.20998 | -46.16739 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f93884cd-f73a-374b-b03d-85e4dd0498fe | -12.04245 | -50.9446 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4224e938-3a68-3753-8d7a-92d671aea7a0 | -10.41968 | -53.78082 | 2026-09-29 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e00bf68-7eff-3455-a769-ff7ee37c1c0c | -15.39224 | -47.90784 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ad34c08-af73-3a72-afee-eeef42a8ebac | -12.70603 | -46.97311 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fc65c56-e25f-3830-b106-f92b394c6fc1 | -11.4531 | -43.47827 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f353530-2011-30e1-a958-d967ce5dd475 | -12.77439 | -50.67157 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20949106-7146-33c5-9226-f05f06893d05 | -15.17046 | -46.13875 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fa7c538-5467-39e1-aa51-c8b84406f560 | -14.62028 | -42.53118 | 2026-09-29 04:17:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3f061493-964d-3e89-b925-b58aae52b8d5 | -11.712 | -44.50744 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9734d83a-0d4b-346b-8a4b-d587db0b3559 | -12.01815 | -50.98001 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0b71f72e-b532-36bc-830b-56e1fad89fda | -11.3851 | -45.41436 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 339bfd8f-c42e-3764-ac02-cc38541b09c6 | -11.08051 | -46.10067 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b4bf064-2d21-3545-bd78-5e6d97f613a9 | -9.04797 | -49.63293 | 2026-09-29 04:17:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a5ab53d-3405-3671-a7af-77818e82625b | -15.15362 | -43.61891 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3dfad003-1c1b-32ea-9b94-3a7c273523ee | -11.44252 | -43.45835 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96865b23-cec0-31e5-9b1f-817597e8c777 | -9.95339 | -50.15221 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b53e3622-70d7-31a7-b27f-8cd903f67c44 | -12.0381 | -50.9438 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7a8cf921-885b-3e14-bab8-bcf2820cc3c3 | -14.0884 | -46.32414 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e732027f-a26c-360d-a330-d9faf9774bca | -13.17901 | -48.54824 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a9ea4b1-e586-3c9e-8514-5fb7cf990041 | -11.85271 | -47.07869 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
