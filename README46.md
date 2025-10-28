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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04a185c3-44cd-334e-985f-5c7b1bc931bd | -4.01094 | -43.2153 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c4221c-fd36-3b1a-a16c-3de9b326d90b | -1.49692 | -53.13196 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17275b25-4bba-3db0-bc27-384d16b0db77 | -4.50749 | -42.83873 | 2025-10-28 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f7fcb86-c8b8-348d-a007-7d38b64e2075 | -7.97939 | -46.7542 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3bdd47c6-312f-376d-bd43-b0f084209845 | -7.35502 | -47.64602 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b1886d2-0a42-385a-b56d-033fc7fd450e | -5.06779 | -47.55449 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07d95a20-4282-3045-ab81-0811fc31c017 | -7.35212 | -47.64179 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33b2bf62-d89f-397d-921e-2cfb99e582b6 | -5.82771 | -53.44984 | 2025-10-28 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ab83f5-2962-3040-8a10-6b4adf091e91 | -6.11041 | -41.73888 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ed3a322-8dd8-3c2c-ba18-b2448e3c7211 | -2.86473 | -44.37707 | 2025-10-28 04:42:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4183e29-927d-37f3-93c9-ebccfe5a5876 | -4.31095 | -48.06494 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc6d426-2be6-301a-80f5-f449667073ba | -7.45142 | -49.41146 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d6314c73-4456-3f64-9e6c-3dc3961c4965 | -6.11265 | -41.72316 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6a99e7f6-c01b-3683-80f9-7b556338f325 | -4.90185 | -48.56873 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4be17147-4bc1-3a8d-8cbb-6305a409f4ec | -6.83783 | -43.99302 | 2025-10-28 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4601d637-bbb6-3005-bc97-6711d67307fa | -7.83685 | -46.4165 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 352c8f9a-e7ae-3906-847b-3bfd15ae9edc | -3.86432 | -55.6885 | 2025-10-28 04:42:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89a9f22f-b742-3bcc-8f86-329d100d6b96 | -4.71328 | -46.42741 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75be1e0a-a167-307b-b44e-36e10083f5ac | -2.19376 | -56.9783 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470cbe57-ea6b-3b8d-98cc-37a9877c8ae6 | -3.85617 | -54.08303 | 2025-10-28 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edf36c1a-4f27-3ee1-8240-8d3de4b2abbe | -4.5677 | -46.88172 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80f487e6-2195-3862-b30c-c9faff6ded78 | -8.15918 | -46.99418 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 824dc696-b512-344a-8d74-aeb2fd27e692 | -7.98983 | -46.19185 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| caaeda7c-8adb-32d5-b5ef-f4db612db1a2 | -7.31574 | -47.21175 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 556a12c1-1b04-3d5a-a046-21c02a13efaf | -7.67733 | -47.41616 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c2cd413-8010-3f2e-ae1a-c0c163e3a28b | -3.41857 | -50.36829 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dab85ed-6b1b-38f0-bd6a-d2f336ac973c | -7.81987 | -45.38509 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42d339cc-755c-3361-b9bc-3996c94bfc8a | -3.53535 | -53.31382 | 2025-10-28 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d38c75be-6ed1-3350-ac21-6fdb9556b309 | -4.92682 | -48.56192 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67173239-3f50-37a2-87e1-43037d26b129 | -1.50031 | -53.12405 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ac2a8a1-3c8d-3b53-89f7-cadf6cbd64dc | -7.97493 | -45.52401 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11676f26-40ce-3872-9cb1-96e6e4769f0f | -3.29322 | -50.19364 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5a98240-45be-3940-b1e0-8e653f1c1f6d | -7.32627 | -47.21342 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 73e8dc53-ce37-31fd-a537-318220c2a181 | -3.57742 | -43.63056 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8e59410-72f8-3317-bd55-2b3c77e1486c | -5.56484 | -51.01427 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 823c4e57-e7a0-3173-8a39-de574615a610 | -3.15513 | -50.33479 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d046a16-2f78-33be-afbe-2250e4b1fd86 | -7.9602 | -45.4631 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8862118-ae93-3d60-9412-2ddd9d723bf4 | -4.37506 | -49.67234 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7318f370-613d-3258-b5cc-772fc9132a5a | -6.09014 | -53.50304 | 2025-10-28 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0d378aa-c6e9-3617-99d7-1793fe170dd7 | -6.62164 | -44.62518 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54c3f8a5-6540-3955-98b2-414b81cfc7d3 | -6.61042 | -44.64508 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9117261f-3e67-379b-a306-59e09794055a | -3.59308 | -43.61044 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f13536b1-e122-30b0-b95e-aa8fe5fdc31f | -6.87626 | -43.58853 | 2025-10-28 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e4d09ae-651e-3e1a-afe9-a39f648fe1e9 | -7.50958 | -46.28755 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e35d209-3ea8-3892-93f6-544966e2be58 | -7.15005 | -47.78061 | 2025-10-28 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ff5ab1b-b0fe-36ae-a14e-e79942b1701c | -7.07634 | -44.93794 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e27d812-f954-38bf-8122-933b50de0186 | -4.20835 | -48.35375 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e096f451-a34e-3925-a98b-04d77b1c144e | -4.84402 | -48.07129 | 2025-10-28 04:42:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b12671ce-b4e6-377a-8838-51ef867a5338 | -4.36064 | -50.66061 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1485b093-c95b-3b84-b4a0-b635c6a102e5 | -3.04196 | -49.44075 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da6b913f-a25b-32c2-92f1-97037990b1d0 | -4.18357 | -48.18542 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fa11a2b-bb96-328c-a7d7-b582775b511f | -7.61979 | -46.69558 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 690333c1-8d04-3e2e-9650-39199517f0eb | -5.58769 | -45.33818 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e7873ca-c3ad-32dd-8efb-2c39bc53ec4c | -3.75674 | -54.65409 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab7b724e-96a7-3e99-8131-85aabe30281f | -6.58073 | -41.40178 | 2025-10-28 04:42:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c842b06a-2c68-3b86-af99-aa0f1d10eeaa | -4.86733 | -48.52768 | 2025-10-28 04:42:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f062d7bd-b344-36e7-b9ee-af9bd9f8899f | -7.94541 | -45.50955 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16c79cea-f016-3320-b384-3bb32bb5fa65 | -4.72531 | -46.81608 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebfe2cba-0f79-3118-b367-52ff77de4619 | -4.36003 | -50.51161 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ca18149-023d-382c-9d20-c1f782b67154 | -7.97889 | -46.73294 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f29ec34c-de36-3cb2-a328-0844774df8ca | -5.65509 | -51.10345 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36d4e732-ecf9-39c2-a2d1-8f6864ac2872 | -7.94714 | -45.52467 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5beb2174-926f-30f8-a809-d85a57b91c25 | -7.67614 | -47.42393 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce85aa70-340e-3c48-b32a-172efdbad865 | -5.5839 | -45.3376 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c54145f-fac9-32a3-a78a-a212829dd293 | -7.81701 | -46.44861 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d7108179-d528-3b72-9d60-d71afe399cbf | -3.57688 | -43.63419 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 34f1b98e-33b4-39a4-92bd-630b1ce2c0fa | -6.14128 | -41.8334 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6e3ea16-563d-3b95-bd25-3ec003ccdeed | -5.83115 | -43.49206 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77b64284-267f-307b-9a76-77e8d60e6ea1 | -7.89478 | -45.69347 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b50caf5e-8a60-33f2-a378-385571fdb321 | -5.6604 | -41.10722 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 844c7c0e-7e27-3245-b0f8-91a8ce0077cb | -3.0851 | -51.28323 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c2acfe-4da4-3b57-8755-e2e7037de930 | -6.42337 | -42.33072 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7fa1f1c5-d3c8-3d06-9321-85fff8cc37db | -6.45052 | -43.81768 | 2025-10-28 04:42:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b482b7b-4d9e-3313-9254-e491c2fa22d6 | -7.9764 | -46.74954 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5f5675db-4fb5-323c-be0a-6291299c217d | -3.60497 | -43.55989 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14abea04-45aa-3037-aff9-6108ec569146 | -7.97528 | -46.7324 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42147dc4-1821-36f8-9522-9d1acf714734 | -3.2115 | -50.81202 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 084dd754-2edc-32e6-b336-22e55f2c1e13 | -7.97736 | -45.53421 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 585dd858-0cf9-3fa6-91ec-30573d396c60 | -3.27484 | -52.5708 | 2025-10-28 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a8b8b18-658c-3321-848c-4aabecf26faa | -7.94083 | -45.51377 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a6e73304-7994-3efe-b6f1-fcc678893613 | -5.75976 | -48.68495 | 2025-10-28 04:42:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c2b9a8d-d969-30aa-9714-ddab5eac1ed4 | -3.52866 | -51.57647 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| debec9cd-ba1a-3179-b4e7-c70d281506f1 | -8.16508 | -47.00356 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daed985b-015f-322a-9433-06d066fa1c47 | -6.6064 | -44.64452 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73bda4e3-7423-308d-a601-73a3681a3fcd | -2.97847 | -51.3389 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c2f1675-8e8b-3da2-9911-9a4f1c8a2474 | -3.54311 | -49.43394 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e72c3e93-0d72-35de-90ec-e6a36019568e | -7.94506 | -45.48504 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fefeae0a-bb18-3921-927d-d938bdbe48e6 | -7.95631 | -45.5162 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9455fca-64ee-3d8d-b168-76f4cf142a34 | -4.80438 | -43.43099 | 2025-10-28 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be80e0a-e337-39e9-97f5-c40ecf4fb7ec | -5.04437 | -45.13131 | 2025-10-28 04:42:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b073582e-11eb-3e5f-8d33-c22052f752d7 | -6.68526 | -42.04053 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e827e26f-dda2-3f19-b9f6-3253b9a90168 | -7.87018 | -46.39506 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8faa1bad-4c47-3cdd-92f5-faf3c2ab9de5 | -3.02612 | -45.37012 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f50593bc-5179-3cae-8fbf-4909be323497 | -4.23334 | -47.57954 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a16b8f5f-c0f0-321b-958e-d29dc526669c | -3.7525 | -54.65332 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cb76469-551e-383b-9454-77c113219eab | -6.64704 | -43.38438 | 2025-10-28 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd4fa102-b986-359c-bc67-3eb9b190997a | -3.2372 | -50.65185 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00aa9a1f-c217-3ff8-a833-a8518d7387ec | -6.08375 | -47.00155 | 2025-10-28 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f026ee7-03cf-3fe9-8275-be15facb9ac6 | -4.71563 | -48.33268 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6e80dde-f7db-3331-96bf-299bbac5a1eb | -7.03027 | -47.62534 | 2025-10-28 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README47.md)
