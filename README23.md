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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39912a04-1456-3644-aa91-ac001ffe0281 | -11.42199 | -43.45879 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 609d6026-86de-3b50-8007-342821b40b16 | -12.01124 | -50.94329 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2aa9fb3-5d29-3fc2-ad9a-f41c5c25b32f | -9.77429 | -44.82166 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe7445e-f77b-3eb5-98a1-042987a509ed | -22.01648 | -49.56675 | 2026-09-29 04:17:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3d2a81d-4f36-3fe5-ab4b-a16ef286f99d | -11.38747 | -47.45438 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1643c555-349c-38d6-af8d-97910403e432 | -11.67902 | -44.54521 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e0cf337-980f-3061-8387-d7b07be80155 | -10.13789 | -46.68718 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4e009e2-437c-3686-9737-1030e5412f8b | -14.11434 | -46.29118 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6bf8f15d-d459-3a62-836f-bc4eb2d47174 | -10.78946 | -48.75364 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 80ae2fee-7c32-3bed-93eb-a078a41964b9 | -15.38744 | -47.91515 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23795428-9a35-3cd3-8a76-108a9ec330a6 | -14.34014 | -41.38694 | 2026-09-29 04:17:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 325a1bb7-026e-3ba5-92fe-86eb27ea6c1e | -11.9001 | -50.61866 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b3de4cc-39ee-34fd-8a9f-6be0437f7e9c | -11.67791 | -44.53068 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35ab25ce-e8d1-3559-b5af-62412099a190 | -12.02251 | -50.98081 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| df0a945c-7ce0-348d-9bcc-37fa7c133cba | -11.38684 | -43.39845 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3908dd7-312d-372b-ac55-4ced390db1dc | -11.86123 | -47.07927 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c39a7636-7065-311d-9e97-7a37ffb471f4 | -11.89397 | -47.01196 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9b1a606-9ad4-3a8b-b2b9-fa6e338b3d4b | -11.39535 | -43.45461 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 431f0f75-1d40-3a5b-b7bc-42c222ed34c6 | -11.38071 | -43.39383 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b3fe719-36de-39ea-8ff3-0cf82d852f8b | -12.05131 | -46.50554 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4519ebae-d6d3-3f53-bf43-74dc6cebd2de | -15.22267 | -46.1733 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87871b3b-061f-378f-bfd6-539aab0423bb | -11.44977 | -43.47774 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e8bc94c-293a-3bac-8345-50ce9dbeaea3 | -11.4375 | -43.44661 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc90c419-cdb6-33cb-bc66-b2834e65606f | -12.0468 | -50.9454 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2031e461-b3af-3aaa-a6ab-3b90fb971c79 | -12.71666 | -46.99464 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 534a8031-8727-3663-b3b3-66b773a9652b | -12.04831 | -50.93686 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| df0cc603-39a9-3e59-884a-c21f790665ff | -9.68206 | -49.31057 | 2026-09-29 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f804917d-7158-338b-bc74-9ba7630f70a3 | -12.55602 | -47.1573 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0b56ce2-a156-3e42-80e5-b4cf60ced0ca | -12.60753 | -47.28714 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4e9d94c-1036-30f9-8452-181ca8d82c8d | -13.38444 | -51.3258 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5c0ab14-e982-3774-9a34-eaf48cfeb7d9 | -10.69764 | -44.4473 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 272d994d-3210-33ca-85a4-e73a39b2b2de | -9.7848 | -44.81973 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6514a801-49f5-34f6-96ee-332114ed4b4a | -15.9387 | -42.33624 | 2026-09-29 04:17:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 39f06d67-ab1e-38dd-ba78-d8921b44323e | -12.88029 | -44.80172 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9897ed07-a9db-39d9-b52f-58d60a1b468a | -12.39122 | -50.22516 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 283d7690-45e8-3567-b766-2147d6f566f8 | -12.94142 | -46.65295 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e6118fe-9e56-3d57-b173-d5f733ba5a72 | -9.81938 | -44.94505 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65693e30-6e7a-332d-9655-94761988eb0a | -11.40976 | -43.44957 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d85a73c-4770-3fb9-821e-eb4f39175931 | -12.62133 | -47.2691 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 610640c0-4377-3cee-88e2-bfca07855074 | -11.43034 | -43.47105 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 898558d9-7f9b-3af2-a56d-802a2e8bc920 | -14.4912 | -43.26418 | 2026-09-29 04:17:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d32b19e4-7daa-308f-b8aa-387248111ad4 | -12.34362 | -44.27512 | 2026-09-29 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b74e5b3c-f714-306e-9b52-bc09f7557484 | -10.90728 | -43.86537 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce647bcc-13a4-3d26-9a97-6abe3b982d03 | -11.39807 | -43.43678 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83f4131f-252f-391d-aba3-39916cc6e462 | -13.47931 | -48.61555 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d24bdf23-6946-3a2c-beb8-50b6fb741d27 | -11.41078 | -43.4205 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1194efe-f9d7-32ab-9a6a-48d7dadc6c03 | -15.13558 | -43.62369 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2933575d-93e5-31b0-a550-32777eaa4e57 | -10.01405 | -45.17585 | 2026-09-29 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c04cea6-888f-3352-be5f-bfdd8cd7b589 | -11.42805 | -43.44147 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cbab38fd-848f-3bb8-ba4a-93bb823c9069 | -11.12496 | -50.0715 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0614987-484d-3649-8a6a-14082acf463d | -12.0161 | -50.96632 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8671815-1ff3-331e-b576-c3e01cac33d8 | -11.41418 | -43.44296 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07f58510-fabd-3b87-ba5d-4c3303e0be2d | -14.08348 | -46.31209 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7e405f9-40b7-3efe-957e-de57acadb3c3 | -21.10647 | -46.2465 | 2026-09-29 04:17:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ee742cb2-b940-3f85-b852-e498828e6884 | -21.24475 | -44.33348 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 885912dd-b19c-393e-b7ff-362acbc985e7 | -21.23319 | -44.34002 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9fd23c99-8a60-35a9-a8d1-fee491bc623c | -11.41139 | -43.43886 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98a3fe1d-7969-359d-9900-32a48a967de8 | -11.43367 | -43.47157 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a01c9b1c-e001-31f0-a847-282ce1cb3683 | -10.70907 | -47.82228 | 2026-09-29 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28364a96-f35d-317c-8651-4a8797281392 | -21.99764 | -48.184 | 2026-09-29 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a2fb5e3-0da7-3fd7-b0f4-0abca32489ab | -10.27744 | -44.6302 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c67200e5-df74-3549-a3bb-692e6dfbda1b | -16.34868 | -42.57825 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0eebc24-fbdd-3e8f-8fc2-772c57501df3 | -12.61735 | -47.29287 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 387c03a7-0e4f-301d-8a16-db527de4e354 | -12.94325 | -46.6418 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dbfef86d-d64e-3988-a60a-7b4ebe39ef94 | -11.09911 | -47.11518 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58a157e5-9bdc-3f83-8634-6b2b2b75520e | -10.81752 | -48.7284 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06bb21ff-be6c-3788-adf6-ccec3d1443fe | -10.81544 | -48.71715 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6685de74-8c34-3a19-abce-e9b7e574c8b2 | -11.18814 | -45.13473 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f68663e7-5120-31c1-921b-f6812a96bd35 | -15.89465 | -46.33561 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ec2eb9-827f-3ead-a3dc-7cc96a2645aa | -12.01379 | -50.97921 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c5324d7a-b5bf-3257-a48f-2ec29b463091 | -12.39188 | -50.22135 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8c185dc6-bddf-3abc-820a-ed3459609194 | -12.91427 | -52.03765 | 2026-09-29 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae242e2-c82a-3f96-9094-4bf003c15ea7 | -15.94231 | -42.33665 | 2026-09-29 04:17:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| eff8690a-bac4-3395-8b35-0306696e8c63 | -22.04699 | -47.15369 | 2026-09-29 04:17:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7e93271-2856-34db-a316-f28c1e8d83e5 | -12.0102 | -50.97411 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c1968101-1501-3289-b2db-e16ce0a16aa7 | -11.34276 | -54.11419 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73e5a8b1-bddd-3750-82f5-1e92a470edff | -14.44696 | -40.75179 | 2026-09-29 04:17:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9e498c7d-ad42-39d6-9249-0b6102f1c3fc | -11.99837 | -50.98974 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6442893d-9343-3508-8ba6-26c2bdb5a478 | -14.48779 | -43.26365 | 2026-09-29 04:17:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e1fe38ad-f6ea-3f38-8815-e1ba30d4c1f8 | -15.38677 | -47.91911 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f703056-9f57-38b6-bfb4-e27053e7271b | -9.95555 | -50.13996 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a9c7bd7-59c1-3854-a520-97b07def62d5 | -10.72017 | -44.43303 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 10219223-9172-3558-93be-548ad6eb8f52 | -15.16324 | -46.14126 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2944847-287b-374d-938f-7922fbac053b | -11.38242 | -43.40507 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89abf0e5-ee09-33a0-8c5e-c8f78a2853a3 | -15.24707 | -43.26837 | 2026-09-29 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 98e9118a-17fe-3857-a6d7-7492eda5b87c | -12.15855 | -50.414 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7779836-8ddb-3400-8df9-c3d04947ee34 | -15.3987 | -47.93367 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb0b913c-52cc-31a7-9686-bada679954c9 | -11.42478 | -43.46288 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdfa7d49-d57f-3799-8677-a671775728b5 | -11.67892 | -43.51007 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61a42a7d-61f9-3a4a-b2c8-30f49451d895 | -10.2835 | -44.63475 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20d255cf-348f-36a6-a95e-59c06ba2b8ac | -11.9976 | -50.99405 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c40f99ce-6b70-3d38-93a3-7c8d50b56bfc | -11.41975 | -43.45113 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba880221-8745-36cb-92a9-7111de7c5420 | -13.06559 | -47.45693 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d17281b4-d25d-3c71-a68b-36ba06871140 | -11.95902 | -50.93377 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f02f2c90-5a26-3ed4-a8f3-e9ad943bb80b | -13.17289 | -48.5617 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 070118a1-ec8b-38aa-a1b9-760fd25a6226 | -15.45503 | -46.14651 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aece40c3-59f7-34f1-bd63-646390c20895 | -15.17196 | -48.67791 | 2026-09-29 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20c6b6d5-b0dc-3316-9df3-fdb2f0239018 | -13.73914 | -48.98111 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88851088-5212-3ac2-910b-5d38e965fb48 | -11.34749 | -54.1189 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 489671e9-4384-3872-9eaf-2b9e7e9aeedd | -19.92046 | -45.32896 | 2026-09-29 04:17:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
