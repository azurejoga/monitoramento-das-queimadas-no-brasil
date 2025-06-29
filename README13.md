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
| 2e94467a-4380-30aa-851d-0626b0c5897e | -12.76644 | -44.40025 | 2025-06-29 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b86ddc6-f57f-357f-9690-d0091a05738c | -10.56562 | -52.03251 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3df82533-4ef5-3526-ada0-d915c00ebe63 | -12.11093 | -54.57088 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22211fec-9227-3c9a-bd1f-5fa07f053717 | -11.54986 | -52.78012 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b047cb38-4a87-3608-a877-2408318fab2c | -9.79226 | -48.56274 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90b3f1ff-2649-3a6f-8ecd-65dae59f015f | -10.55097 | -52.04465 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| aef5437e-e0d4-37ac-9ac7-993b4d6faec1 | -7.19704 | -43.70747 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c34059f-fce5-343d-969e-1c1bffaf7717 | -10.83387 | -53.75763 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20707f7a-1dca-3f1d-8375-e95fe2765a70 | -11.03616 | -56.278 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6db1643b-0593-3a75-b99c-69659f347e9b | -10.62164 | -48.0874 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08b72c7c-f5f2-3289-a8ae-c6081518debe | -7.5525 | -45.84568 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c70e8bb-2291-3b66-97cb-6a028c9faa38 | -12.04531 | -48.08144 | 2025-06-29 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0372d87-b20a-3f69-960c-1ee9914d68b8 | -10.62462 | -48.69508 | 2025-06-29 04:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bd8d62a-079a-30b1-a074-4d5cea878cd2 | -11.26268 | -52.74412 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac0a78ff-146e-3807-ab5d-59a5a2cde85c | -11.26048 | -52.75564 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c28961ac-e2c2-3075-ae44-66904e034389 | -6.45063 | -44.57169 | 2025-06-29 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1844d701-2ca5-3fbc-b9d9-b86bb3134dde | -10.83899 | -53.76343 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab379c9-eb15-39ca-82cb-675d8237c8b2 | -8.87108 | -50.16774 | 2025-06-29 04:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aff29871-4cd0-37d9-8fad-6e91a1c46ac8 | -10.6239 | -48.7017 | 2025-06-29 04:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f696e85b-c9cb-3db6-a1aa-1bdb42579f10 | -11.26755 | -52.74909 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2608a88e-5bbd-34ba-a697-72b2504682c7 | -11.0242 | -56.25819 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b0a7c73-538b-33f6-90aa-35f37f80c2e7 | -7.18025 | -43.65873 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f9c3e3-fb70-37b4-8732-ddf5007651a5 | -11.55397 | -52.7889 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5e469eac-e78e-311e-96f0-52ec34b9a996 | -12.1061 | -54.57424 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75c167bd-a217-3992-a154-329b65e14818 | -11.02649 | -56.29 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0074ade3-8c2c-38f9-8075-4cfa6793ccf5 | -11.01306 | -56.24229 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44d98236-1a59-3802-b26c-2b61dabc1436 | -11.55175 | -52.80038 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c9baa81c-6420-3fcb-8f46-898ae777e981 | -10.6223 | -48.08355 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b48519f7-497b-351b-8a76-80752c4b718f | -7.25699 | -43.1432 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 265093df-e99b-3aa4-9b14-69fcbb8aa0d9 | -11.56293 | -52.80271 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef49cfe3-73d9-37ef-9655-daf8d3f14173 | -11.57351 | -44.83418 | 2025-06-29 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6c39f6a-b7d5-352c-bb67-c26fefea3639 | -10.55573 | -52.0493 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 58d4186a-0343-3b19-82a2-e4be8e43d982 | -11.54912 | -52.78394 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d4426e14-0abb-37f8-8076-7c69d851c961 | -11.269 | -52.74149 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 755fc15d-aaf7-3dbc-b1a5-8bbd71a44aea | -11.02361 | -56.26846 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 176887f4-3a37-3d5b-8262-a9bbf179abbf | -11.84424 | -43.79737 | 2025-06-29 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29d942b9-b355-36df-ac0e-a26eab02bbd0 | -12.11228 | -54.57558 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e714526a-10cc-3832-b03a-c7813dcc95a4 | -10.5692 | -52.03727 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b145b1f-b8eb-3024-b1eb-f7052d2026e4 | -7.5609 | -45.84219 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3dcd00f-7817-3040-a78c-b6004d6acb96 | -12.06413 | -48.47836 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77c471b7-8188-365a-b217-ff5fb2fd2a94 | -6.89755 | -43.97553 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f3ba3f2-0c3b-35f7-bed4-050efea8cf83 | -10.55343 | -52.03739 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 681b3096-eb79-3fa7-af72-3bbf68771a8b | -11.03392 | -56.28099 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ff59c6d-fee6-38ae-b162-f0011a572480 | -10.55953 | -52.03492 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef054349-92b0-3dd5-9356-88f695f5c513 | -13.69437 | -47.13149 | 2025-06-29 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 969c8eb6-3bed-37c2-b702-1bf160a2a2c3 | -7.55071 | -45.83836 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2096e10e-30b4-3bf1-b10d-5373bc633177 | -10.55228 | -52.03759 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 479121e6-5b4f-3cc5-aa95-2b7fbedc0a74 | -7.10074 | -44.36554 | 2025-06-29 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a75b6e11-ca95-3045-8f98-31016ebba799 | -7.17904 | -43.66619 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f8ffe0f-6df0-3286-97c3-a6ebbbe42430 | -11.55765 | -52.76989 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8c013dc4-a10d-369d-820b-1ed4500d4379 | -13.64745 | -46.81647 | 2025-06-29 04:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd26492e-0974-35a8-8b75-131bc22c4146 | -9.79123 | -48.56905 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75799628-9e58-33ee-bf68-743f7392fbdd | -10.5568 | -52.04905 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dad27365-8f0d-3344-b0ed-f383ba041f8a | -11.54539 | -52.80322 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a161931a-6c96-331e-babd-e8d8d6a1a6e4 | -11.26339 | -52.74039 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adf08554-ac81-3ca6-bdb5-5fb65091d871 | -10.5577 | -52.03865 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6957e96-99db-3b91-b8c8-4302ce0068ab | -7.09713 | -43.65731 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f365732-6cb9-341a-87cd-f10537900f61 | -9.64505 | -48.78924 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cfd280b-2a2a-39d1-9719-8ad30f0829cb | -11.27291 | -52.73789 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6f3fdb4-5a88-3558-a53a-78c4546bbfdc | -10.5431 | -42.5359 | 2025-06-29 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4636d99-5326-340f-97fb-bddea3cb3035 | -9.79196 | -48.56479 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ea9565e-25b7-3090-bd33-292a82888238 | -6.83353 | -43.68463 | 2025-06-29 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2a5d181-717a-3533-9b58-017883bc8f2e | -7.22441 | -43.51686 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bbdb6195-adbf-39ae-ab43-1b3b1dc24741 | -11.02696 | -56.27959 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8de7f02c-095c-3e3d-8944-c079a4c51850 | -10.55705 | -52.04218 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| db56778c-16fe-308e-b155-b428de5b651c | -9.14426 | -46.38445 | 2025-06-29 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eec32598-6172-340d-a0a0-12d60f8c1a10 | -11.54839 | -52.78775 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| dc27fed4-4239-3849-ba05-aaeac5c24c32 | -9.64746 | -48.7921 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54eee69a-1ee0-34ae-a541-83c97163b188 | -10.56969 | -52.04057 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ace1e6f-bd8a-3cca-83d0-50d6a1e81090 | -10.54685 | -52.03652 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa83334e-5f7b-3a1f-9968-6b3356bf522a | -11.53306 | -52.77694 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64b64759-c72a-3e94-a00f-367774e06ddc | -7.55867 | -45.83236 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a46fca8-6f9f-3cb2-b8d8-2292d2421b7a | -11.54128 | -52.79444 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cfa5f883-abe2-3f72-aab8-c3cb11ec734d | -10.87429 | -53.75031 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a24b7834-a85c-3f45-bb04-80a4e455e95d | -11.78911 | -48.2939 | 2025-06-29 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46483686-c979-3e79-bbd2-bc166c5ce999 | -8.09356 | -46.86256 | 2025-06-29 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68e16823-41a3-3d0e-8672-4ce95d15cb46 | -11.04818 | -55.37702 | 2025-06-29 04:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce50488c-1ef2-3209-8484-c4952bd5bd06 | -10.56427 | -52.03949 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2751473-60ed-3d8e-b359-0f5e04579b82 | -11.01778 | -56.22593 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dae6837-ac1f-3703-9e28-acb5e630e6cc | -10.62389 | -48.69928 | 2025-06-29 04:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f8fcd1-6169-3248-8d73-a70438ba3ef5 | -7.16077 | -49.51549 | 2025-06-29 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee2625d-5cd0-3239-ac4f-d042708f5bb3 | -10.55639 | -52.04573 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 88a1f837-8e93-39b8-8c3d-7617996d12f7 | -9.1575 | -46.3527 | 2025-06-29 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d41d54ba-35c9-3e94-98cd-11aeab806f18 | -10.85964 | -53.75361 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce17577a-f7b0-3de3-8fdf-757a286f49be | -11.0228 | -56.26486 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e06ece4-e943-3580-a6a9-65cec8c5916f | -7.26037 | -43.14375 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6559155c-ea67-3f60-9b5c-e572093c2b2a | -11.55808 | -52.79772 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efe87105-202e-336b-8135-89233390ae5a | -9.71741 | -56.18839 | 2025-06-29 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92090ce1-fc5d-3246-8c3b-80ff15c48428 | -12.06133 | -48.4698 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27d28bd0-06de-388d-b028-c8d0ca250dd7 | -10.98265 | -45.10958 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fd6b7a8f-03d8-3b3a-ba3f-98a4ce14bd45 | -10.845 | -53.76466 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a65c1bc3-a839-3704-b2d3-df1af84f2020 | -10.94598 | -45.6021 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7f679ac-74e5-38dc-93e9-ca46c77b4d77 | -10.53922 | -42.53887 | 2025-06-29 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ed79153-6441-35af-a83b-d2fb1b6e90ef | -10.5636 | -52.04301 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a81c3137-529d-35ae-a394-352558bed68c | -7.29872 | -55.31901 | 2025-06-29 04:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 38fe91c2-5942-38e9-8ad7-24c1b6481bcb | -11.53381 | -52.77313 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 019446c5-419a-39ea-b369-f2d29a85c998 | -12.09975 | -54.67115 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f51c430-47ac-398d-a9ff-a446c85dcf07 | -9.46651 | -40.34436 | 2025-06-29 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d938c01-fd87-3141-a399-987d39a84819 | -11.27774 | -52.74288 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 587633eb-98b1-3a18-a277-b7da6e4777e2 | -6.94423 | -43.56802 | 2025-06-29 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README14.md)
