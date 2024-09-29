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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53b3c5a7-73f9-3672-94ab-9a65e9859a5c | -5.261 | -48.8871 | 2024-09-29 00:48:57 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27da0afc-fb14-32c1-9137-9e1016807052 | -5.2382 | -48.8778 | 2024-09-29 00:48:57 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc212b88-efef-3bea-857d-f0d5b16af73a | -5.2398 | -48.884701 | 2024-09-29 00:48:57 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 094a19e2-b3f5-312d-9104-b4ccf594d396 | -4.5751 | -46.055599 | 2024-09-29 00:48:57 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6ce5b4d-d6aa-3c6c-a367-cb98fd251117 | -5.2253 | -48.866402 | 2024-09-29 00:48:57 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdc8a891-848c-347f-9455-d0468f6b58b7 | -5.2268 | -48.873199 | 2024-09-29 00:48:57 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8220f13c-6c3a-3e20-a742-079f63b5010a | -5.208 | -48.971001 | 2024-09-29 00:48:58 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 812d6d81-6a51-3e5e-b7c6-e51ca924667e | -5.0916 | -48.867599 | 2024-09-29 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66917775-6660-3847-98db-f0068a5e5461 | -5.0931 | -48.874401 | 2024-09-29 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d207e3b6-55e6-3db7-928d-73d818300595 | -4.0673 | -44.507702 | 2024-09-29 00:48:59 | METOP-C | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecac0034-646d-3471-a69d-5bd527fa572b | -4.4436 | -46.110901 | 2024-09-29 00:48:59 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9021d96f-f46d-3a87-adbe-36b6af79dfb8 | -4.4455 | -46.1189 | 2024-09-29 00:48:59 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9feb3b1f-a100-34cf-befd-67373a34fc78 | -4.4444 | -46.334801 | 2024-09-29 00:49:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b10eff6-6518-308f-b592-0563305b3cd9 | -4.4462 | -46.342602 | 2024-09-29 00:49:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24d6230f-bad8-3c6e-895c-46c5e6320586 | -4.4327 | -46.3293 | 2024-09-29 00:49:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4752686-02ee-3df2-94c7-f5cffcca779c | -4.4346 | -46.337101 | 2024-09-29 00:49:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ada8223a-9815-3801-b0bb-6d34656cd67f | -4.4364 | -46.344898 | 2024-09-29 00:49:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1135d5-5eda-324d-b8bc-7dba1168618e | -5.1594 | -49.480202 | 2024-09-29 00:49:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b2adb7-083e-3ab4-a326-a6f1ff0abf56 | -4.9179 | -48.604599 | 2024-09-29 00:49:01 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57cd8e50-222c-37de-9df2-f8983ac412ee | -4.9195 | -48.611401 | 2024-09-29 00:49:01 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0e5bebb-0068-37be-bec5-60466ded3ae0 | -4.921 | -48.618301 | 2024-09-29 00:49:01 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7228883d-79be-308e-8cf6-a055b747a0ad | -4.9081 | -48.6068 | 2024-09-29 00:49:01 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd5ccdf3-fe50-3402-9682-791e8dbb26a6 | -4.9097 | -48.613602 | 2024-09-29 00:49:01 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 980e9987-d512-3739-a30f-e1f168b65622 | -4.484 | -47.75 | 2024-09-29 00:49:05 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dccffd55-7405-397f-8672-6ccdf7db6872 | -4.4856 | -47.757 | 2024-09-29 00:49:05 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3753c37-447c-396d-8c7b-e3c6909522da | -4.6331 | -48.531799 | 2024-09-29 00:49:05 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 954f3646-3cb3-3814-b93a-dbbf2cf763f9 | -4.3779 | -47.603199 | 2024-09-29 00:49:06 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffde321-380e-366a-acf8-cb2314473597 | -4.3795 | -47.610298 | 2024-09-29 00:49:06 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a00bba-5f9b-3e8d-a095-8b51a0063ea1 | -4.4843 | -48.109299 | 2024-09-29 00:49:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0149f87-ef8e-38e6-97b4-c31251925ac1 | -4.4859 | -48.116199 | 2024-09-29 00:49:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2378648b-7ff3-303e-9256-8fccb2106b94 | -4.4061 | -48.083199 | 2024-09-29 00:49:07 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f359bc8d-dca5-3719-aa9a-3ab9120ce544 | -3.8667 | -45.936298 | 2024-09-29 00:49:08 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ceda1e9-955b-32f2-8bd7-ec6568b0d231 | -3.9156 | -46.455502 | 2024-09-29 00:49:09 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99fa26f0-e5c3-3302-9677-5933355d77be | -3.9174 | -46.463299 | 2024-09-29 00:49:09 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16446ed1-3dcc-3a23-b2d4-6563a16a98b9 | -4.8477 | -50.9203 | 2024-09-29 00:49:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf711f6-6637-3577-a943-eceaf8089989 | -4.8494 | -50.927799 | 2024-09-29 00:49:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25097f41-8765-3990-a737-74c2957e7175 | -4.8362 | -50.915001 | 2024-09-29 00:49:11 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31720f14-9ef5-365b-82da-f718e2cb095e | -4.8379 | -50.922401 | 2024-09-29 00:49:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0242f5ee-e227-3d12-bac9-a16645da3052 | -4.8396 | -50.929901 | 2024-09-29 00:49:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef81c49-4ed7-3096-86ec-6117b624d333 | -4.8281 | -50.924599 | 2024-09-29 00:49:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8414912c-660d-302e-a132-e4a12ee3e4c8 | -4.2217 | -48.5811 | 2024-09-29 00:49:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feb5d5fb-d66a-385c-9d96-f697c14cb71e | -4.2233 | -48.588001 | 2024-09-29 00:49:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5212c96a-5f52-370f-812d-6b9e34684788 | -4.1903 | -48.624199 | 2024-09-29 00:49:13 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc6af216-8b41-34b7-a8cc-d14bad0e8c70 | -4.3897 | -49.630199 | 2024-09-29 00:49:13 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b28a5bb-8a16-3820-9d14-eee6efab5765 | -4.3913 | -49.6371 | 2024-09-29 00:49:13 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0caffba3-a57f-371a-a26f-6a769349bc58 | -3.6981 | -47.6073 | 2024-09-29 00:49:17 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5743710-1d07-3169-8686-f05419b488fe | -3.6998 | -47.614399 | 2024-09-29 00:49:17 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 762b30cb-428b-381a-83e5-1a2d8b6db940 | -3.471 | -47.6511 | 2024-09-29 00:49:21 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fff804e1-d419-3330-947a-80bea269ac5f | -3.4727 | -47.658298 | 2024-09-29 00:49:21 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96c90098-87ca-3bde-894c-5d7ad9f49d09 | -3.4136 | -47.5812 | 2024-09-29 00:49:22 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 401ad786-31d6-309d-9068-4ebb5454955e | -3.4038 | -47.583401 | 2024-09-29 00:49:22 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb516456-e956-3c6d-8ae9-170d3c7dafc5 | -3.4055 | -47.590599 | 2024-09-29 00:49:22 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8640b2-c297-3fb9-8bf5-7549bdeed31f | -4.1466 | -51.0518 | 2024-09-29 00:49:23 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4baac6c0-ebe4-3f2b-8b72-1414060cc3a4 | -4.1012 | -51.124298 | 2024-09-29 00:49:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd3c7d0-27a5-39cd-9718-9bee3366b0bd | -2.9593 | -47.355701 | 2024-09-29 00:49:28 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e614911a-529e-30a9-8dda-ad18268ed025 | -3.3337 | -49.0247 | 2024-09-29 00:49:28 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83b3230f-07a6-3d08-a0c4-ace7d883e255 | -3.3353 | -49.031502 | 2024-09-29 00:49:28 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c275000-70ac-3fa8-a8e6-300cd4390031 | -3.5675 | -50.361698 | 2024-09-29 00:49:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 417398b8-82c1-389c-a548-2da85c697b75 | -3.5691 | -50.368801 | 2024-09-29 00:49:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd2e6c1-8f15-326b-833e-4c090c99f51e | -2.719 | -46.719299 | 2024-09-29 00:49:30 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a190a2f-358c-3428-b419-fa68656e6b34 | -3.5577 | -50.363899 | 2024-09-29 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e929baa4-a7a5-32ec-9808-714fbbbbee14 | -3.5593 | -50.370998 | 2024-09-29 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 610b7672-5362-385a-b455-ca1198d74fdc | -3.5609 | -50.377998 | 2024-09-29 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a30f6f0-51c8-33dc-bd1c-dc8899194210 | -3.2173 | -48.921501 | 2024-09-29 00:49:30 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f74b9a9-1e0e-327d-bfe7-f324c5cceb0b | -3.2188 | -48.928398 | 2024-09-29 00:49:30 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f9d247c-7e03-3f1f-bfa0-3be3bb7ec49b | -3.8974 | -51.905998 | 2024-09-29 00:49:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9edd89b-ec33-369b-bfbd-5c286fd69a2d | -3.6338 | -50.788601 | 2024-09-29 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7500b224-200c-3f3d-a858-74c66fbaa184 | -3.5636 | -50.570801 | 2024-09-29 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e05fd43a-d931-3df2-813d-38b276529079 | -3.5652 | -50.5779 | 2024-09-29 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 828c7c11-e052-300d-90e1-ee826c1b4809 | -3.894 | -52.300499 | 2024-09-29 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2b5e4f-4419-3cc4-ab20-60c62641c74d | -3.8921 | -52.292198 | 2024-09-29 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09162673-cace-387d-9176-28d4955b6715 | -3.8958 | -52.308899 | 2024-09-29 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd4d8779-9d99-3146-99e6-7ccfa3e21029 | -2.3265 | -45.5191 | 2024-09-29 00:49:31 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4d86fdb-90eb-3cd5-8ccd-9bf4da70020e | -3.8842 | -52.3027 | 2024-09-29 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d136a7f-4025-3593-be48-f5d820e35666 | -3.886 | -52.311001 | 2024-09-29 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 790d28fd-991a-3fc1-a6df-8dbd1c1e65dd | -3.1265 | -49.2001 | 2024-09-29 00:49:32 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 530237b0-98f5-3384-b768-6b84cc23ff7c | -3.336 | -50.2953 | 2024-09-29 00:49:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67d24528-dc1c-3e85-8bfb-3ef55f9dfa9b | -3.3376 | -50.3022 | 2024-09-29 00:49:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986435b2-d79e-3c34-b44f-22075fa58b56 | -3.3262 | -50.297501 | 2024-09-29 00:49:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b9d7ca-e6e7-38f4-acf8-03800cb3a409 | -3.3278 | -50.304401 | 2024-09-29 00:49:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8100e646-2757-3239-8708-0a4e471cb133 | -3.2398 | -50.009899 | 2024-09-29 00:49:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa04b2f-0157-3f13-a53e-4a1b4adcd6fd | -3.2414 | -50.0168 | 2024-09-29 00:49:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0937571-c6bb-36c9-93af-5488e465d271 | -3.5077 | -51.185398 | 2024-09-29 00:49:33 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8af722ff-6513-398d-8bc0-c228eb668b44 | -3.5093 | -51.192799 | 2024-09-29 00:49:33 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d122ed98-38aa-3231-a5be-8209118501b5 | -3.511 | -51.200199 | 2024-09-29 00:49:33 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1688c4a9-26e0-331f-8932-5f171e0103da | -3.4995 | -51.194901 | 2024-09-29 00:49:34 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a249314-4432-30b3-a775-f6c4b9c95759 | -2.3783 | -46.539398 | 2024-09-29 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3b6de73-1767-3ec4-b7b6-5b47edbeff0f | -3.0529 | -49.5536 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3520c0f9-bb94-32d6-af22-11468190705f | -3.0545 | -49.560501 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 826fbf81-3ce2-32a9-aa1a-cd2c99d9942c | -3.0384 | -49.535301 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a10327d4-d1ac-3303-b879-95f3ab024127 | -3.04 | -49.542198 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef6ff24d-6ba5-3df9-80f2-5eaf7e70bf34 | -3.2956 | -50.660198 | 2024-09-29 00:49:35 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c42d00b4-9270-39fd-93d7-233f8a7454d6 | -3.2972 | -50.6674 | 2024-09-29 00:49:35 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb29a09b-c1c8-3747-9e39-f923d29bd409 | -3.0286 | -49.537498 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f41f573-0df4-391f-8a04-17a3769c7869 | -3.0302 | -49.544399 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65d574cd-81ab-3495-bf8d-9eba9e1d34f4 | -3.0318 | -49.551201 | 2024-09-29 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 831e2eca-51de-38e3-9faa-0b7f382ea418 | -4.0395 | -54.000401 | 2024-09-29 00:49:35 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 852e0b74-ab7f-3367-a6b3-da844b920247 | -4.0418 | -54.010899 | 2024-09-29 00:49:35 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2a7884-6f03-38e4-b98f-f35a5884d195 | -4.0442 | -54.0214 | 2024-09-29 00:49:35 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 207ff553-78ef-311a-adf9-e826ca009d97 | -3.1916 | -50.4305 | 2024-09-29 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
