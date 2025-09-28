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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3f32626-5515-3a25-9bec-ce24d67e2ec4 | -12.30036 | -45.64633 | 2025-09-28 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a7b4a51-4334-3ba5-9380-2e655db39cb5 | -11.62653 | -44.42525 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 037d242a-3f35-3f43-ac39-029f01735f51 | -11.98645 | -47.99158 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f7551cca-8f2f-3609-96d8-75986ce01a5b | -15.20812 | -48.05816 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba261fab-d98d-30a1-ba04-20d87776e3da | -10.30083 | -45.40562 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d86dac4-2ba3-377d-b997-886a49890295 | -12.90511 | -45.16466 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 24e64608-72d3-3a7b-845a-4c57377c3ff9 | -12.97874 | -42.65406 | 2025-09-28 04:06:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2b67d718-213b-36dc-bf24-d5d8e17d7da8 | -12.0187 | -47.92649 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9cb6fc90-e4a0-3e89-a195-e470a151f6b2 | -12.00492 | -47.08994 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11ca9667-4fd7-38aa-ba55-724d8bc854a8 | -13.80207 | -52.79004 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bccf1f75-3230-35aa-b915-c9d7bad187d1 | -15.32007 | -47.8977 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 420aa539-792d-3f65-b8ac-0f86c0a18034 | -13.62622 | -48.06783 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4345eefb-36d8-3210-98d8-66308a97a046 | -12.98207 | -46.85099 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b69eaa7-1407-3a91-a559-e9c37cfa4e6e | -13.32036 | -47.31442 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b2dc58b-cea5-3420-8243-51c2bc0d1b90 | -13.02574 | -49.45969 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39fa338f-9b26-308b-9168-191ba064a220 | -14.88341 | -47.98415 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aa5dbca-ce04-395e-9bc3-3d2fef61dee1 | -12.92741 | -45.16867 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 729c4767-8736-310f-aca4-2b4163dc0dbb | -13.57341 | -44.44463 | 2025-09-28 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ef67849-1b62-39eb-934b-1a5f0ede4b65 | -12.97864 | -46.8464 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71c6f2b9-5787-30fe-af03-74425ff12b1f | -12.69339 | -46.87508 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba0a5f30-ecae-3864-a622-0610df72ec4b | -12.0598 | -44.86061 | 2025-09-28 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43c10c90-66d4-34a6-ab9f-44b15c024f44 | -13.58877 | -47.31388 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ab3faff-f381-3b62-9173-76b73750a993 | -13.60856 | -47.32403 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ca09d88-613e-3782-ae87-11f824150139 | -10.91551 | -45.74365 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bd931c9-5958-359e-9f90-42120669fe8d | -15.32778 | -47.90319 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 801f865c-cb14-3fdc-9d2a-30551f076ef1 | -13.79514 | -47.91381 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f83109-e8b3-33a8-8092-ba3c1f195c39 | -12.42264 | -44.11164 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8cd9068-1b29-33eb-9640-2b8b14294c1c | -15.03573 | -46.9693 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfb89599-185c-38c8-9031-63759f7f3d80 | -11.9247 | -38.33334 | 2025-09-28 04:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44076bd5-f689-3a69-8144-ab2bb207dcf4 | -11.42721 | -46.6399 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a455472e-3ba6-3d45-adb5-3a634fcfefef | -11.36514 | -44.96247 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 775af36e-280a-349c-8cdb-845c8bc59b80 | -13.80187 | -47.92598 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e22b685f-5f91-358d-9f85-5fa6b654d40f | -13.00432 | -49.4535 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e976bcab-b49a-3c7b-b08a-e839568a40f4 | -12.0163 | -47.05093 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce621f40-303f-3d35-b315-bc60a76a1124 | -11.97952 | -47.08527 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a88a5f41-ce7b-3b71-8dc1-81681785deef | -11.94945 | -47.91467 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5ed29b8-cd05-3521-811c-d4b297232d68 | -14.83623 | -45.57545 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdab8930-06fc-3c23-a89b-8665e36e6a35 | -13.57411 | -44.44051 | 2025-09-28 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd5a324d-3aba-336a-9c7b-ecf54fa99496 | -11.99145 | -46.60596 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ce71dc6-4cd3-3ba7-8e51-0548a74b2ad2 | -10.58558 | -46.27379 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20297f73-89a3-36bb-a309-ab40d1e40a46 | -10.91994 | -44.29565 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b0dba95-ecf2-3436-806a-e19b53607410 | -15.43235 | -48.23368 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 526abdec-cfe1-3ca2-8c7e-8262efe58fb5 | -12.41909 | -44.11105 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3396ae4-8c62-326f-9f4b-d0a636996154 | -12.28167 | -44.0465 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88640b26-b811-3ae7-8131-6eb83e021575 | -11.69389 | -44.40078 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af30ad20-b9b7-3e1c-be88-698db858b9a8 | -11.09632 | -54.27991 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbf4a3d7-3044-38be-99b3-91596e1d7175 | -10.45241 | -48.20327 | 2025-09-28 04:06:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6950963d-5c01-32a7-ab6b-b6466b6d7da2 | -15.70592 | -44.86789 | 2025-09-28 04:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcf63ea3-4b8b-3572-8d27-efbcefd4aa55 | -13.58311 | -47.3212 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc80eb73-8ce3-3fd1-bcca-2104e6c946bc | -11.98901 | -47.87516 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2cdac99-43c9-342d-92a1-3ef57d736356 | -10.94772 | -44.26369 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2976b7a6-1df5-38e6-81ff-3909691c753c | -10.64583 | -44.75864 | 2025-09-28 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7e12c7b-c063-3989-bb56-f635987018be | -11.42306 | -46.63911 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67bd7a1e-a090-3d9b-9076-2d202b2ec06f | -12.01027 | -47.97166 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9b26b61-6ed6-3060-b8ce-7af083f0a313 | -11.09585 | -44.81974 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 78100101-046c-3000-8c00-51dee8f9e6bc | -11.95126 | -47.98063 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b834769-65d6-310f-85c4-d7a55e0eaa14 | -11.68952 | -44.42635 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd19babe-6ee6-3db8-ae6e-8b7c7f3f5282 | -14.75759 | -48.37029 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ab1a26-4534-30be-b3a7-10480d6cd015 | -13.52466 | -47.40733 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32e77044-f8fe-381c-8787-5935cbe0e739 | -12.688 | -46.88135 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 37149efc-90be-38af-b089-5c2ba7cbd234 | -11.99192 | -47.88453 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b588b07-7ed8-344b-be62-b219a761bce2 | -14.78866 | -45.64271 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ca783fe-fa78-34aa-b7a1-3e2c132603a1 | -15.53044 | -47.90805 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75ea42ca-0bf2-363c-bcd2-9e707ad1134c | -11.66838 | -44.46225 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2436ed88-2035-38b7-a905-27995f73594f | -11.4462 | -44.98582 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14bd44b8-b50c-3157-8999-c3bbd016baad | -12.89923 | -45.15432 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 97322f49-a25c-37b9-8843-b418c278342b | -13.52397 | -47.4067 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f7e825e-d194-32ed-b9a6-b785d32a99c7 | -13.60633 | -48.10801 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 181690c0-a198-3ab8-be41-861e64e22786 | -11.36127 | -45.05167 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a324a443-9a7b-39fa-86af-6c3de7d90863 | -9.45254 | -50.9016 | 2025-09-28 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26eab716-5531-39ae-9e61-7b3f67781cb7 | -12.88799 | -47.09269 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2bbdcf5-cee5-376c-843a-7663306f898f | -12.69269 | -45.4751 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2f15df7-e133-32e7-b557-1843fe7fb0d0 | -11.36591 | -45.04733 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d33d2dd3-76c5-3548-a045-ea615fbf901d | -12.84491 | -46.89331 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17eb3fcb-b6ca-3c68-910d-4921d4731d0a | -10.91019 | -44.81853 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cd701af-5f61-35d2-a85a-bbaf9cd05018 | -15.53315 | -47.91689 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb7bc77d-eb65-332d-bc88-5863379c6ed5 | -12.92817 | -45.16417 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21c73b8d-6eb2-3a77-ad3f-67f1007203e5 | -14.43709 | -44.88339 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da3f5fd7-2164-3cbd-bfaf-f2ce0a291160 | -11.38398 | -44.96532 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57b1576a-4cc8-3018-adb8-5be271dc35a6 | -11.44089 | -44.97154 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8e52a93-3ca2-37ad-bfde-57106e7c9380 | -11.37736 | -44.93662 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f7dcb86-5e52-3735-8ea5-615c87961c65 | -12.01827 | -47.91771 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e5943860-2579-3453-9319-e8d09905e583 | -11.60176 | -44.32899 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b279374e-521d-3839-b261-ff6d91ea21e8 | -14.58838 | -48.25939 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 089f86aa-7108-3097-90be-016d738c437b | -10.26648 | -48.07879 | 2025-09-28 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30baa5ab-b8ba-37e2-b707-87a25480c905 | -15.28432 | -49.48562 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd12e4eb-4947-3810-b9ba-77d1f1069be0 | -11.38692 | -46.93857 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85466e31-8735-31fb-b235-6e73b30a47b0 | -13.56277 | -44.09803 | 2025-09-28 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0efe81c4-c9e8-3b25-8d50-ea64c550f2e8 | -15.8839 | -46.2016 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d47cda2-712c-3fcd-837a-e660e78f0bad | -12.93951 | -45.12 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be58d339-d6be-3343-978f-7b09a380cb85 | -10.30021 | -45.40747 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ff72780-7847-3220-9d2e-f621a31879bf | -11.95475 | -47.911 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 084a8491-e1f7-34ec-9798-88bbd3425785 | -14.53699 | -48.41772 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 143f1d57-6a78-357f-98ce-d64293f1fc4f | -12.21271 | -43.74866 | 2025-09-28 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 178baaa7-6cc7-3254-8a9b-6ec722bdf68f | -11.40984 | -44.90481 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f043cf8-912d-3d66-9c99-f624911caf85 | -13.78458 | -47.89825 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e3c1278-b9d6-36c6-96b3-845c82838db4 | -11.92827 | -38.33389 | 2025-09-28 04:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13a16992-0111-3950-bc56-e50c13c57a0d | -14.5385 | -48.40283 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7574803f-76cc-36c8-be54-80ba0ee006c8 | -10.79399 | -49.58888 | 2025-09-28 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3117b92-cf09-328e-89c4-06e7911f04af | -11.35762 | -44.96124 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
