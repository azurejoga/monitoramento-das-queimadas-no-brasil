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
| 5a03202c-c881-3a14-8841-0a99483dd477 | -7.9403 | -45.19886 | 2025-09-26 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f735fed-dbc9-3f95-9fd6-24eae30d4985 | -9.87311 | -45.91338 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b86f16d1-d877-3058-9466-dbb140b8ddbb | -8.78938 | -46.59388 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 455b2884-2b7f-35a7-a8cf-582936d28067 | -3.82643 | -50.97258 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45e29528-5abf-3699-b295-11710e2104ad | -5.82669 | -43.90922 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16ff8cdb-3b80-3c41-97fe-5679080333c9 | -10.59497 | -44.07187 | 2025-09-26 04:42:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74943037-61c4-32ca-81fa-ad9d7e01cdab | -6.42359 | -43.07518 | 2025-09-26 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d0e31f1e-ac8c-3e4a-98de-de4a63dca732 | -5.73668 | -44.96613 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 88e51037-4644-3ace-8232-cca6b53a27a9 | -5.89295 | -47.59572 | 2025-09-26 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e5809e6-4ebc-39bf-aa10-9be861316614 | -10.4037 | -46.16267 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d10da78-10b6-30da-b6a0-910f19245f0d | -5.96599 | -44.25101 | 2025-09-26 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a4adf44-59a5-391f-b8ef-cdc67186e1f5 | -6.96505 | -42.3008 | 2025-09-26 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ec2c00c2-dc4d-346d-b1cc-04bc7b7bd5a5 | -6.88075 | -44.50264 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be06c90e-0002-3e4a-983e-3fe5c6733166 | -5.73383 | -44.98532 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| dc7b60ae-d7e4-3609-b24f-63f2abfa0ff8 | -6.34436 | -43.78342 | 2025-09-26 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c795b7a9-ecda-3967-b346-3d1ef54f077a | -9.70392 | -48.25317 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8552cd52-2a38-3db8-84da-9df9b06c26b6 | -8.13322 | -44.12921 | 2025-09-26 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 692129e6-a194-3501-99de-72277789ed07 | -10.19266 | -44.84256 | 2025-09-26 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 287ffbcb-159e-3684-aed3-b56c8fd3f150 | -8.77055 | -43.04602 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7eecd1fb-89ee-35ec-8bd0-6f1783abe1c5 | -5.17996 | -48.03183 | 2025-09-26 04:42:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e051824-7cc2-3665-98b8-f41439b02469 | -8.3151 | -55.34476 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5abee4a-8b29-3ed1-9820-80ea90d99504 | -3.85066 | -50.97641 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf3f0f57-c3b1-397c-9d72-d17cf5354e5c | -9.67217 | -46.0304 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b91ca1d2-67d8-32e7-829a-6f3f46d4c51a | -6.61556 | -42.92805 | 2025-09-26 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7464993b-e2c2-3447-833a-dbdf5be71e41 | -6.82597 | -44.16533 | 2025-09-26 04:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78f67d3c-43a3-3740-a3ea-cf0a498faa66 | -10.3917 | -46.13646 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41a8f1ac-1b1d-3553-8ec2-d46b6be1b87e | -5.46793 | -43.06792 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9dd0d3dc-1d70-3833-8693-16bd66b94753 | -7.31597 | -45.7611 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87ac50f5-7679-3a13-8413-84bae3d643bd | -5.47294 | -43.06426 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ab5e703-b2f8-3634-9652-ce52ca4fe9e5 | -6.98679 | -44.84771 | 2025-09-26 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6061f88-0d2a-3604-a7b9-3b1a79f2e4b0 | -5.46501 | -43.05967 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 57c8dac2-af0f-31eb-aa5b-e3977240202d | -5.74833 | -44.96787 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 707240e8-b440-3cf2-808f-b4aacc799830 | -8.19369 | -46.38886 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b74ca71-3825-3979-888b-188390f8ed58 | -9.70922 | -48.94852 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b35270d-2c7e-385b-be13-e71775a35194 | -5.78667 | -43.83345 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5876f9b-d086-3771-95af-591de1d8a91c | -4.74803 | -43.27127 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 42f15932-b89d-3072-98ce-c881552b86a0 | -10.57192 | -44.07954 | 2025-09-26 04:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9c9d921-71c5-3b11-8477-b192a19017fa | -6.63848 | -43.82578 | 2025-09-26 04:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3678f2bb-febf-3970-a764-81bcc65f997d | -10.39804 | -46.14719 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c0d6245-16e0-3c3b-9566-3d819e9164e3 | -10.39375 | -46.13929 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96eb76b4-bfd7-37b4-bb06-7548cb95a8da | -10.5873 | -44.06194 | 2025-09-26 04:42:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01e9abed-3cef-37e3-9142-247c19f124c9 | -6.71225 | -42.74539 | 2025-09-26 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc8f8c0e-fa07-349f-9f30-f4957c32478d | -8.32733 | -49.52835 | 2025-09-26 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc2c1ee7-685e-3eea-9d09-d777be199650 | -7.58762 | -42.33071 | 2025-09-26 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3008b0b9-645b-3f9c-80a8-821c0d5d90bb | -5.62555 | -43.9294 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66dff53a-890c-3843-ace1-155f3ae61df8 | -5.73208 | -44.97035 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da8bb574-a297-3250-a6c5-a81647f780b6 | -10.58248 | -46.27979 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9f12964-2a08-3613-80c9-04e9038ef6e4 | -7.05413 | -41.43356 | 2025-09-26 04:42:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f2d36161-e8a6-3e81-af60-6c1b84eccec7 | -7.7509 | -44.9436 | 2025-09-26 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4df63743-e433-3fff-8f3e-0ba5c8277b9c | -10.10532 | -45.31434 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59f9cc87-e85b-3f03-861e-324a76bb0c3b | -10.39446 | -46.13451 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 004d0d26-b0e4-3cd0-a959-f10d1f9882a1 | -7.44407 | -41.90969 | 2025-09-26 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1beccc31-664f-31a3-bebf-fc9dc6402528 | -7.69898 | -47.80099 | 2025-09-26 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d87ff8c-f22d-3f25-bc92-fdec7a96cadd | -9.71082 | -48.25425 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8c237b0-7e35-3425-a17e-33e88e203fc8 | -7.7726 | -43.92154 | 2025-09-26 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcfe262f-93ea-320a-bf92-06e951c94ab9 | -5.80279 | -42.80483 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40aeb62c-5a9d-371f-bbbc-3bbf477e2d7a | -5.74182 | -42.55822 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9182159e-cf26-3cb2-b2e1-077c8abbccdd | -5.73842 | -44.98114 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f6eed0a8-bd2f-3ab0-a40c-cd1b10439831 | -5.76045 | -42.9057 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2755b880-3e6d-3f80-bb0b-a9cc33563786 | -9.10931 | -48.89637 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41304f6e-aada-3b8f-a6e5-24641f647881 | -9.83367 | -46.14454 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b33c3774-0076-3777-b9c2-e7ae0e969f93 | -6.86765 | -39.26394 | 2025-09-26 04:42:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee8d7368-1e2b-3208-bdc3-27b4a591f63e | -7.12846 | -42.20665 | 2025-09-26 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 569e406c-af0f-3ea5-aebe-8a712d40844f | -4.75673 | -43.61259 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 990df286-7932-34b6-b625-bab867ead7ee | -10.80928 | -44.43041 | 2025-09-26 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02840d16-0f5e-3e05-bb9e-3f7159a55223 | -5.7374 | -44.96127 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d3fce43b-f941-3b38-8619-805cd1acc62d | -5.56125 | -44.38285 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fef4468-5cff-30c1-bbe4-b073c8eb8a39 | -5.62668 | -43.92191 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0551279-af19-30af-8444-a9d391df0448 | -5.78698 | -42.75669 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 789ddb0a-f62f-39cc-8869-db4a91c1835c | -5.13518 | -45.38435 | 2025-09-26 04:42:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c9fd95c-7c63-3dbf-8941-ee1ff5a41de9 | -7.81339 | -47.33261 | 2025-09-26 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8073a41c-8d5c-3f7b-ba2a-941be6519b85 | -7.38914 | -39.11746 | 2025-09-26 04:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2eb8244d-848d-359b-ba7a-aa184f85b33f | -8.71201 | -50.05092 | 2025-09-26 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7276970e-a2f5-3b98-8521-0e74566623c7 | -9.97938 | -49.2561 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca04b6c-7985-3631-ae47-b50248fcab53 | -9.03136 | -45.52993 | 2025-09-26 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268c8c44-8ff4-30e6-94f7-5772960d63af | -6.69038 | -44.61539 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6ba1a86-c205-3cbe-8063-6884b23c6434 | -6.67569 | -43.59524 | 2025-09-26 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f42a748-a2bb-326f-a688-83386ff869c9 | -6.4883 | -43.28191 | 2025-09-26 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf3c92cb-e955-37e8-8db9-7e37c36466c1 | -7.11559 | -43.73721 | 2025-09-26 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16c06d44-4118-379c-9194-490010b738c9 | -10.11033 | -45.30807 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 80cde30d-c420-3b7e-9e79-26856b5519da | -6.31895 | -41.88054 | 2025-09-26 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d6347bf-df69-36bf-b864-ddc5de4d3e82 | -5.57975 | -48.95641 | 2025-09-26 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbff4415-6e5f-3686-baa1-a0be141f6f07 | -6.4285 | -43.08138 | 2025-09-26 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 378213ca-c40d-3304-b79e-08bc38f08b1f | -9.4754 | -48.23767 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa36eb3c-2733-3dca-bed0-527f1fb521a4 | -8.08042 | -55.22464 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7e4ec9d-8b0d-33f6-86a2-5db5b8af750d | -5.46307 | -43.07243 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b1cfa5d8-6b1f-3e49-ac9a-d5fb65bf4553 | -7.58786 | -42.33228 | 2025-09-26 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a2c7252c-1622-370e-96e3-734a02ffba9c | -7.48504 | -43.89516 | 2025-09-26 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee2992c5-ba4c-35ac-a888-f91ae83e7da9 | -5.7303 | -42.63836 | 2025-09-26 04:42:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 643b9b57-b270-3481-8376-b21fb4c9c145 | -9.32171 | -48.94713 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77db8807-4bf1-3cc7-af15-00e2aa5277b9 | -7.38806 | -39.1124 | 2025-09-26 04:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d313230-f7e0-327d-896e-c17966336c02 | -8.13472 | -42.38166 | 2025-09-26 04:42:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfea2704-e360-3f57-b055-9fa380c144ad | -5.69294 | -44.44295 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db5f312c-928e-3522-939c-dd14537ead13 | -5.24585 | -43.08685 | 2025-09-26 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e6b106f-8fe9-3549-bae8-7fef407efa1c | -5.39294 | -45.84874 | 2025-09-26 04:42:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51cb38e7-f54c-322f-8945-4f9523cea6f9 | -5.74056 | -44.96671 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| eac4167f-03b3-3cb8-a91c-eae58c3284b7 | -8.49912 | -47.83796 | 2025-09-26 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce56651a-d9cd-377c-880b-5e8c98aa9306 | -5.12143 | -45.5013 | 2025-09-26 04:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00f61077-b064-38eb-8f2f-fa39c9b86748 | -6.32377 | -41.88123 | 2025-09-26 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99d4f911-13cb-3cb2-9791-9f2207350f32 | -5.7328 | -44.9655 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
