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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 388f6906-b25a-3e20-9e3f-95f9251de92e | -18.0898 | -42.4475 | 2025-10-17 00:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| b14d4a66-5664-3028-b78d-f73f7a17077f | -8.1996 | -43.3189 | 2025-10-17 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| a1fb59fd-e4a2-3f6e-bc29-4967aa7f7d5a | -10.5132 | -43.4289 | 2025-10-17 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 71774b33-2985-3fe8-abab-70c72627fa66 | -8.4079 | -46.2314 | 2025-10-17 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4f6f5e6d-dc58-38a4-af1c-df13dd0435de | -2.7401 | -49.3715 | 2025-10-17 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ac161e36-0b18-3f3f-be92-73de20875f99 | -4.9546 | -44.9787 | 2025-10-17 00:10:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0f8bd688-f9f0-3f34-ba8a-612167b811fc | -3.5213 | -52.4728 | 2025-10-17 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 03036c4f-57d5-3db0-b8b1-f243429af516 | -11.398 | -44.1933 | 2025-10-17 00:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 25b486b6-ceb3-33bd-b0ad-478b7a60f8b0 | -3.2546 | -45.9632 | 2025-10-17 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 1e1a8c84-91df-3fb5-b315-dcc87d3659c2 | -10.2935 | -44.0455 | 2025-10-17 00:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d96c1129-8cb3-3023-8091-d220e2784897 | -3.5028 | -52.4734 | 2025-10-17 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 47ed3da0-3d1c-395a-85f2-4512587ef86f | -11.5733 | -48.5568 | 2025-10-17 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 09264a2c-4b81-322a-b4f0-2f20d567abb3 | -5.2596 | -44.2058 | 2025-10-17 00:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 40e6c252-0831-38aa-b52c-d7bccd98f7be | -10.2939 | -44.0221 | 2025-10-17 00:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| d1e489ce-2a29-3d80-a987-4e0c4eb0f531 | -3.2359 | -45.9862 | 2025-10-17 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 9ed8594e-95b8-3502-a16e-1afa5c19bdf3 | -4.3872 | -43.406 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 225.4 |
| bee139e8-4d3a-3e99-9e75-64d67c7832ee | -2.7401 | -49.3927 | 2025-10-17 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 1c4ca089-2a02-3a4f-9084-bc9360a2914d | -9.0821 | -48.0252 | 2025-10-17 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2bf17484-350b-33d0-9bff-1cacc24a72ab | -12.9368 | -47.1275 | 2025-10-17 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1478ec6c-a525-3f91-b9a4-3e8859bff11f | -4.4248 | -43.3805 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| cd6a90bb-c83c-3be1-81c3-458bddf8b178 | -3.236 | -45.9639 | 2025-10-17 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 241.1 |
| bbae2fd7-7a52-3f36-9d42-ea55672a64d6 | -10.4941 | -43.4315 | 2025-10-17 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 37e150b7-4ad0-3dd4-87f3-06d2e48721ad | -3.5212 | -52.4932 | 2025-10-17 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 94eff14e-81e2-3b47-83dc-7d67538e553e | -10.514 | -43.3815 | 2025-10-17 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 47d85095-617c-3b57-9dd9-e5f98bbb5c74 | -10.534 | -49.5471 | 2025-10-17 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b0fa6140-e154-3416-966e-43c7036e2fb9 | -10.5136 | -43.4052 | 2025-10-17 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 178ebc88-3bf6-3d0d-9022-6ba6b32165a6 | -3.5028 | -52.4938 | 2025-10-17 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 290.7 |
| 529751d6-213c-3474-aea4-f813b04e6a80 | -9.7302 | -48.9183 | 2025-10-17 00:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8d02e638-7661-3e8a-824a-823087917e1d | -12.9175 | -47.1303 | 2025-10-17 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b4aac98d-7e68-3bac-85c5-f2c7cede17cc | -4.9548 | -44.956 | 2025-10-17 00:10:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| eaef568d-1b76-3f4f-a823-91b5497abc69 | -13.06843 | -46.93375 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4a781d41-ba83-3565-9200-2619affdd77e | -11.91604 | -46.85483 | 2025-10-17 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c53abc7d-a9f7-33ba-a208-5b14fb4c3374 | -11.5836 | -44.05629 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 20d98c13-83fd-3ebf-b0f5-ca322d23f945 | -11.39286 | -44.20617 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b77132b2-3a69-3df9-b890-f202ae6fb1be | -11.45061 | -44.2196 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 15d0e080-8e31-3963-896c-7a47a0d8c3ad | -12.96515 | -47.09111 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6792d813-fead-3b98-a381-85ddac8a7630 | -11.52452 | -43.49825 | 2025-10-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d913ad63-3222-36b8-8745-7573dfafbd72 | -11.48063 | -44.30746 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c8c99374-ba6a-3d0e-8758-d83724e2b299 | -11.47448 | -44.26223 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| c2ba1833-3044-31c0-9ec3-bf0f640cd362 | -12.05624 | -47.98074 | 2025-10-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ec88410d-529b-3d0c-8630-415452e356c7 | -11.46438 | -44.25446 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b315c897-2f39-3f50-a00b-4972fbb06615 | -11.43693 | -44.26426 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3ddf7eca-e921-3df0-ae5f-8139e5c4a998 | -18.09498 | -42.44901 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| 3d8a7244-ef1f-3a35-8eb9-3da4679d2bd2 | -11.39924 | -44.18687 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 33ddf3f7-0311-38f6-80cc-b18a9cc46a98 | -11.58854 | -44.09229 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| abd63240-c36c-3802-8174-e77683497e35 | -12.62183 | -43.43782 | 2025-10-17 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 424c710b-78db-3b38-b735-771ce45c667c | -12.44725 | -51.33981 | 2025-10-17 00:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 75c11be9-b113-3931-b8c0-f90679127592 | -12.10396 | -45.87148 | 2025-10-17 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 9e809702-ffe9-37da-a4a8-0729fa645fb8 | -14.47596 | -48.42879 | 2025-10-17 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 07ddeca5-a8b3-3170-9c0f-05efa60e5a81 | -11.45307 | -44.23766 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b11c08a6-9804-3101-bbaf-9a5d81d1bec6 | -11.4614 | -44.03446 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| de8804e9-9591-3309-b4d1-8fba427903e2 | -11.77968 | -43.73521 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 46ed9be5-d6e0-3e08-882e-a049bf2febf3 | -16.02006 | -43.50259 | 2025-10-17 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 404a68ca-d34c-3c23-9705-72045c71f5b4 | -12.33088 | -41.20588 | 2025-10-17 00:11:00 | TERRA_M-M | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9eead4f2-da1d-319e-b282-82bc6a65a418 | -17.97465 | -39.88085 | 2025-10-17 00:11:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| ee16132b-2e23-301b-a00b-66e3c5dcd39f | -11.47865 | -44.1604 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0e9ffdc5-9d0c-3de3-a13b-714fd78c741a | -11.57876 | -48.56956 | 2025-10-17 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 5dae97eb-4cd5-3c96-986b-be3d9afd79f5 | -11.47372 | -44.12437 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 763ec9ea-624a-3668-8eae-097c2f7f03b0 | -12.44142 | -51.32108 | 2025-10-17 00:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2dbce4a6-ec7c-3dc9-8d80-e107456a6251 | -15.17722 | -43.5302 | 2025-10-17 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 78ab576b-5a76-3a68-aa19-f505458738f6 | -11.39163 | -44.19716 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 04c03c9a-170f-3b49-b335-72853c95d31a | -11.46561 | -44.2635 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 6d941b58-8b01-3e42-8217-caa6d0528519 | -12.42225 | -44.19421 | 2025-10-17 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9bc353e5-dfe9-386e-ac06-fd110f4f3d5a | -12.06886 | -47.99331 | 2025-10-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae1f299c-c66b-316b-8743-85d1012d1324 | -12.93086 | -47.1288 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 2ac13762-a196-3871-96f4-b07a0b132811 | -16.59286 | -42.43875 | 2025-10-17 00:11:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 25afc87d-2f1f-3ecb-8ab1-1c2cb5eda709 | -12.15683 | -49.6942 | 2025-10-17 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 84a3efa1-cef0-3076-8821-fa968598bff9 | -18.08487 | -42.44111 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d14f4b6e-4ab5-3011-8db9-725780315861 | -12.32299 | -41.38999 | 2025-10-17 00:11:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 47eb1308-c1ef-38f3-91a4-8b2ac6205a6b | -19.07618 | -46.81526 | 2025-10-17 00:11:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 352a91a9-31bd-3d23-8a13-4260c579a700 | -13.03787 | -47.33194 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6329cc6f-c035-31eb-b604-67258c9de8f6 | -11.47571 | -44.27127 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| e27bc1a5-9852-323a-8a2d-6af3644b9f02 | -12.16321 | -45.07243 | 2025-10-17 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5e8ed730-6cd4-3a46-8360-4c597e57daea | -12.16195 | -45.06298 | 2025-10-17 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 828d56c3-54e2-3a24-9186-0323f2fa4090 | -13.82533 | -42.3535 | 2025-10-17 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 7e79db92-1081-3c3f-8be2-c2125a7decbc | -12.87537 | -46.85874 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fede7a24-088c-3405-aef9-2f39281570a4 | -11.4858 | -44.27903 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| b02c551c-b792-3e2f-9bfb-07e2a0b6c0e9 | -12.17232 | -45.07124 | 2025-10-17 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d32e1c4f-1ec9-3881-8087-6667dd8da260 | -13.82404 | -42.34438 | 2025-10-17 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 9a7662fe-492e-34d8-9107-5bb0cf977ddd | -12.15464 | -49.67519 | 2025-10-17 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 931f82d1-da14-35fe-971d-0ad1dfbfa929 | -11.46316 | -44.24542 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 45f1cb34-2a58-3dd1-b961-dc85d920452e | -12.93251 | -47.14164 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 988f93ea-1fa8-39fd-9ff9-f859cf9b6258 | -13.75602 | -48.22477 | 2025-10-17 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cd9ca79b-e3ba-341b-b0b0-5940a80c8efb | -17.38885 | -46.64573 | 2025-10-17 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 85b81458-4a68-38f3-80b4-f8151ea9d602 | -11.47988 | -44.16941 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 771ffc79-7e4a-3836-9333-1a950cf4a659 | -16.59159 | -42.42958 | 2025-10-17 00:11:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b013e991-7ab2-302c-a23f-3e32bfd5c796 | -11.44703 | -44.27202 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 72516bf6-baab-3b25-9b43-96909261abb4 | -14.5858 | -42.77539 | 2025-10-17 00:11:00 | TERRA_M-M | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f28b093a-9084-39ea-8f7d-a8d8b7bb32eb | -15.29586 | -39.66596 | 2025-10-17 00:11:00 | TERRA_M-M | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 8d91c526-73ad-3628-8b90-5ea2cd0febbe | -14.15045 | -44.3118 | 2025-10-17 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0100c8a5-fa7a-31a2-a845-12c9a6dd2c78 | -16.34249 | -46.40297 | 2025-10-17 00:11:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9dc67f29-7697-3463-bb9b-5e1958d6be03 | -14.21804 | -42.84573 | 2025-10-17 00:11:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 697e470a-cdaf-3320-a281-5e1a6286df96 | -12.94406 | -47.93527 | 2025-10-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 007c9591-b976-317a-be33-60fc43957bdb | -11.58607 | -44.07428 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2890ddd9-8e88-3841-b8ec-df6df020ab6c | -11.48111 | -44.17842 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8fe16818-9aac-3012-97b8-3bddc4c8420c | -12.93741 | -47.12181 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3338c28c-5f5a-30e5-9f24-88fc801abcd4 | -12.91983 | -41.82212 | 2025-10-17 00:11:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 065e3fc2-eb00-332e-b5e2-68ff992abfe0 | -15.16834 | -43.53151 | 2025-10-17 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 53.7 |
| f87c410f-1312-3b78-8054-9126224cce0b | -11.4794 | -44.29841 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a475eb23-5e69-3d07-ae7a-708509763583 | -12.06713 | -47.9793 | 2025-10-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |


[Clique aqui para ver as próximas entradas](README3.md)
