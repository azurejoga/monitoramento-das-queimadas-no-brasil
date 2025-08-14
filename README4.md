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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d765fc31-1af4-395f-9d28-a5fc84e3a5de | -19.88666 | -44.60659 | 2025-08-14 00:45:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 685c241a-9fca-3e73-9176-c20ca395759b | -18.5344 | -46.06388 | 2025-08-14 00:45:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 15128622-68ec-3268-b497-c34638a47be4 | -18.53404 | -46.05735 | 2025-08-14 00:45:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 89b1b0bf-263b-397a-93f7-0bbdaedf2939 | -22.30159 | -49.54768 | 2025-08-14 00:45:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| 4f1329b6-8930-3659-acc2-e1fd12c82ff5 | -20.34794 | -45.98698 | 2025-08-14 00:45:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 488c6262-0f71-39d9-a1d7-f3a50b9c1524 | -21.79354 | -49.25576 | 2025-08-14 00:45:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| f37887eb-d930-3fad-b4f0-2b3df8bd8c85 | -20.00471 | -42.19979 | 2025-08-14 00:45:00 | TERRA_M-M | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| cad9d9ed-cdb3-3a3c-afac-0ebfcc097c4f | -22.31054 | -49.5463 | 2025-08-14 00:45:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| a0a81110-2ac3-329d-b918-52d015aa757a | -22.80054 | -55.37962 | 2025-08-14 00:45:00 | TERRA_M-M | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 98613ff1-1a76-3865-8df4-acfcccb94697 | -18.54247 | -46.04987 | 2025-08-14 00:45:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 2e8b50be-2a66-33f9-87fe-5fa2b09fdfec | -22.30289 | -49.55742 | 2025-08-14 00:45:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 4ab72333-ec5e-300b-a150-7736f993de47 | -19.88906 | -44.62089 | 2025-08-14 00:45:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 1a302b93-d210-362c-8cec-aad4b8aee5c2 | -17.61926 | -46.70737 | 2025-08-14 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ff58bd31-da49-3fe3-a9e6-970e0be54735 | -12.58431 | -46.95951 | 2025-08-14 00:48:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e0398b1b-1583-3076-8321-5896d7684535 | -14.48364 | -46.0725 | 2025-08-14 00:48:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| e83c7563-84d6-35aa-b98a-778247b3552f | -16.30856 | -52.92002 | 2025-08-14 00:48:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 78e8a48f-1412-3292-8c80-9b24d547b86a | -12.4287 | -48.70083 | 2025-08-14 00:48:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 59c6c917-3b40-3774-87ba-30e204c699b5 | -10.9702 | -49.57394 | 2025-08-14 00:48:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2aa3919c-d78c-3d59-b20e-f6a11e0f5fab | -15.58155 | -47.32245 | 2025-08-14 00:48:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 3eea3930-65ed-39fe-a616-f37478b8d234 | -10.96881 | -49.56437 | 2025-08-14 00:48:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9a8aa540-f56b-3d10-830d-ba88df6589ea | -12.30558 | -50.01407 | 2025-08-14 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9c770ed2-b70a-3e6b-9a0a-bb9662c1dd74 | -17.04761 | -51.78875 | 2025-08-14 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 5eff6472-e418-3a83-8347-b060993b579d | -12.34611 | -49.91385 | 2025-08-14 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fcccfaf2-28d8-3937-8e89-9f45fdd9a3b5 | -15.57187 | -47.32417 | 2025-08-14 00:48:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b67bdfa1-018b-3a5c-9635-efc6dc9581d5 | -14.32788 | -48.64373 | 2025-08-14 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 753deecd-e9f6-3666-81e8-936005295bc4 | -15.54777 | -43.1519 | 2025-08-14 00:48:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 16.6 |
| d586a984-bb19-3be4-81dd-bbd785d55c60 | -12.34743 | -49.92309 | 2025-08-14 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bf22de53-14ec-357b-86c9-689026bd9a20 | -12.58631 | -46.97223 | 2025-08-14 00:48:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| acedded1-5825-3d6c-82f3-e67237843643 | -12.32432 | -46.0567 | 2025-08-14 00:48:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 67719f10-e08b-32d3-9ece-334e5246ef35 | -14.32642 | -48.6339 | 2025-08-14 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 25a5d95c-ec19-3ba3-89b7-7e29def52018 | -13.07303 | -49.3266 | 2025-08-14 00:48:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 315b0592-5c2e-3714-82de-7f67fd4cd4c3 | -12.57845 | -46.96603 | 2025-08-14 00:48:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ce745e0c-031e-3d37-ba43-36c0a463944f | -17.0563 | -51.80198 | 2025-08-14 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 19285262-8ebd-395d-a72c-e9a90a90be22 | -18.24637 | -47.26273 | 2025-08-14 00:48:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 0e76c568-4f9c-308a-a21e-c20f627421c8 | -12.57649 | -46.95307 | 2025-08-14 00:48:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 23e6bd54-d7c9-32b0-bc9e-ef601b531f34 | -11.31383 | -50.49654 | 2025-08-14 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 141e15be-90b3-3885-b706-af3f2d3fd77a | -11.80324 | -44.27132 | 2025-08-14 00:48:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e7a7b98f-457e-3c82-939b-5d53359effff | -17.60947 | -46.70897 | 2025-08-14 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4cba85aa-bebc-3a0f-90fb-96fc19018a0a | -17.04895 | -51.79893 | 2025-08-14 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e7e64984-4bbe-327c-a97a-466ccfd7ece4 | -14.3172 | -48.63527 | 2025-08-14 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 069fbf74-46c7-3912-9970-a0b14e65e597 | -16.68628 | -49.46523 | 2025-08-14 00:48:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8975ad9d-2952-3c3c-94e9-20800d7e974d | -14.47861 | -46.06506 | 2025-08-14 00:48:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 142b9af8-5aba-3d61-b824-ac09b4a640da | -14.31866 | -48.64511 | 2025-08-14 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 94f7ad64-2219-3b55-8452-b3173e3140de | -15.07791 | -55.43111 | 2025-08-14 00:48:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4c1b1410-1564-3123-8bab-2b69ac308c89 | -18.24479 | -47.25216 | 2025-08-14 00:48:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7de2489f-b238-3cac-a71b-2942085108e2 | -17.055 | -51.79176 | 2025-08-14 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 96193f8f-6a17-3177-9d15-3680cc8a9515 | -16.31974 | -52.9301 | 2025-08-14 00:48:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd78d78c-9d83-30f9-98e9-865d391045ca | -16.31827 | -52.9184 | 2025-08-14 00:48:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 73ef1853-55df-3075-80be-1db76e4cf8d4 | -12.31314 | -46.05847 | 2025-08-14 00:48:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ee69a449-ebd7-3bb5-9d89-9d13d4cfd90e | -7.6102 | -63.5348 | 2025-08-14 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d3dbe899-f8e1-3780-ba2d-d3919608657b | -8.5208 | -43.3298 | 2025-08-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 87476e4a-dc7a-3714-aec4-eb5e3e289f98 | -7.6103 | -63.516 | 2025-08-14 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| a4e4f370-4594-3f75-9921-23d93cf825d0 | -8.5211 | -43.3063 | 2025-08-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0c202b91-f967-324e-bab4-7a8cbd8bd1fd | -5.9899 | -44.1528 | 2025-08-14 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 62eb98e0-5e35-3591-b80f-5c97c60db942 | -6.9422 | -44.5562 | 2025-08-14 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d1b1a337-b9c3-3d10-99ab-80add82f2f88 | -7.6287 | -63.5154 | 2025-08-14 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 9915753f-3ddb-3bde-99cf-632b57b610c4 | -6.0991 | -59.9459 | 2025-08-14 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| abd7268b-edde-3cb8-a7fc-3c5d89ef9623 | -6.0992 | -59.9267 | 2025-08-14 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| db044c2f-fcff-334e-949e-283f63afed40 | -8.1028 | -61.2069 | 2025-08-14 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d8ac8baa-97ef-37d9-aab0-f37fd7fcfd31 | -6.0807 | -59.9465 | 2025-08-14 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 200951a2-3542-35e9-8894-d8b150d1aae0 | -22.302 | -49.5486 | 2025-08-14 00:50:00 | GOES-19 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.9 |
| c80eb96e-dabf-3273-ade7-8158589d4a84 | -6.961 | -44.5546 | 2025-08-14 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9d6cdd8a-ce72-3a75-a404-ce3a83801c5e | -9.1522 | -59.6578 | 2025-08-14 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 86855b68-188d-3243-a661-1792acc536aa | -7.5918 | -63.5166 | 2025-08-14 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7a5c5277-90e4-37a2-ade7-21f77a140d27 | -7.8775 | -61.8063 | 2025-08-14 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| b960ca20-f648-3743-85e6-b9f4d1875209 | -7.8774 | -61.8253 | 2025-08-14 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 4366c094-106c-3173-8ec2-c418f69d9992 | -6.88412 | -59.15194 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1082.3 |
| 6c680ab7-d175-3f4b-9f06-a42c7a0c1ae9 | -10.36312 | -50.81424 | 2025-08-14 00:50:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 82b06277-be5c-3334-8aaf-b718e206b4a2 | -5.99253 | -44.14812 | 2025-08-14 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9013dfff-e337-372c-b1ef-c9cd8dd44c36 | -8.5187 | -43.33164 | 2025-08-14 00:50:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 6ab9cace-019f-3659-b8c9-178018c00cca | -8.11135 | -61.21219 | 2025-08-14 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 47e78b33-a27d-3596-8e2c-1beca6fc51e9 | -7.88106 | -61.84677 | 2025-08-14 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b14614c4-7856-31c2-8b22-7dac9347e1b4 | -6.2777 | -53.64596 | 2025-08-14 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a4251a33-3043-3177-ab27-1703f5933fae | -6.87342 | -59.17616 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| cac55a82-b0ed-3551-9a86-e45d3e811b1b | -7.87315 | -61.81586 | 2025-08-14 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 1df1a176-a7f8-3bd7-afeb-bac7b4821cab | -6.95208 | -44.53999 | 2025-08-14 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 042b6442-e8c4-3873-94b7-d9f538f0e51b | -6.91885 | -59.14227 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 0b8c25a1-2310-3946-ab4c-f08aaf1238f1 | -5.97787 | -44.15034 | 2025-08-14 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| bf17e9ce-7bde-3d1b-a0e5-60b0ba3d1851 | -7.12932 | -60.11962 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 095fa82a-5dcd-3eb0-9be2-91458c022dc3 | -6.0951 | -59.96316 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| a4b07d30-2fba-345b-9700-6f0a23d3e505 | -6.08081 | -59.9653 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b5b8b448-f222-3fb6-8ec7-b65b441467ca | -6.65122 | -59.08076 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4729a005-c117-32bd-bf62-ca9a3217c43d | -6.27365 | -53.68475 | 2025-08-14 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 107dd22c-c5cc-36ef-a3cc-4b57a6acf658 | -6.77813 | -59.47723 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 0d437580-fc66-381d-a5c6-de88fd09a03b | -9.77178 | -48.74611 | 2025-08-14 00:50:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8441f560-8d86-3d4a-8977-0088d30eaf90 | -4.77623 | -45.34087 | 2025-08-14 00:50:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 65bc9b27-b239-371f-b0b9-36f327f5bfcd | -6.91131 | -59.14862 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 301.9 |
| e9b15c7e-1347-328c-9c47-f9283bc86415 | -10.17853 | -49.51102 | 2025-08-14 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 97ff191c-114c-3ee2-aafc-30e82dfc0be7 | -9.1827 | -59.66983 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 0d5bfd6c-0842-3efc-bba8-bc1b6a6327b9 | -9.13779 | -59.68097 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| ddfcee22-4aaa-3e5d-b318-ad637d30f52e | -6.62328 | -43.89256 | 2025-08-14 00:50:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| df83b599-45d9-3520-94fd-637946a3b3c3 | -9.15334 | -59.67365 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| d680ff53-62f4-33cd-9627-3995de0ee7ed | -6.88124 | -59.12962 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| cb6ab05c-8547-3050-a566-e1545b305ae9 | -7.13597 | -59.6572 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fb4dec52-0efa-3092-84ea-1d9c9bd98d5e | -10.36186 | -50.80523 | 2025-08-14 00:50:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d28f2bc-eb43-3721-b800-776f23a80e5c | -5.99186 | -44.15462 | 2025-08-14 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f2772b62-184b-3ba4-8e54-8c327f41823f | -6.89772 | -59.1503 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 620.7 |
| 14876fcb-b433-3b07-990c-66970c446eda | -2.9051 | -48.30469 | 2025-08-14 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a2dd6c81-2319-3e51-b141-162c056df242 | -9.13447 | -59.65382 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b90ecfe3-21ec-31d1-b2e2-d6e1651ba502 | -6.13754 | -57.82898 | 2025-08-14 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README5.md)
