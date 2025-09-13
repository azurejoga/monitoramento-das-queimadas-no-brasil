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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 682e6408-20cd-3e0b-99f8-83f9a221a21e | -10.36135 | -50.50644 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b81fafe0-7dc2-3910-9a50-3e9d64d278ac | -12.90916 | -47.96285 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 90c4e5aa-43df-3949-833b-c713e4b1d227 | -11.72985 | -46.61214 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 282aa00c-89ff-34eb-b6d5-f1c809fa6d08 | -11.44368 | -43.57318 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f291038-1b68-3a9e-9011-2fd2b56168a2 | -16.533 | -51.74577 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50b008b9-ae47-38f3-953e-c779a7f08d4d | -14.2195 | -46.28748 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 979d2cc5-1783-31c9-85a6-bb54ab223c66 | -17.95582 | -45.26986 | 2025-09-13 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 003a1de8-96bb-3354-8441-423fb099e6f5 | -13.88671 | -48.25584 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e20ce4c-0e5a-33b4-b4ad-8acd1fadf24b | -12.85077 | -47.93873 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f79a06ec-4ab7-3f84-81de-69cc2a55742d | -11.41812 | -45.61423 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bb4cc290-9e7b-3ccf-9416-739859d61694 | -13.00016 | -46.75378 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14ad6d7c-239f-37d3-b5f0-0339d1810ba7 | -13.08621 | -48.26821 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0e8e361d-39c7-30b7-8003-2204e189243a | -14.6996 | -45.14888 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca04e7f1-88df-3636-aaf2-cf184e44385d | -12.80724 | -47.99735 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34c3b16b-ba6c-3a7e-a262-125fc9b1add6 | -14.19194 | -46.24158 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d26f4b28-9b3f-38ac-a6c5-da718e4c6cd1 | -14.21811 | -46.29432 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 502213c1-901c-3a8b-b36b-5f9d1670a20b | -14.20197 | -46.27443 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb647a59-af06-3c82-a4c5-ca68c9b9d627 | -14.20644 | -46.2797 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fde56ee9-f772-3f3e-84d8-1d7f858077fd | -11.13118 | -50.71308 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 993b7480-2758-3e8b-bdca-1d9cd792ccba | -18.85091 | -46.83063 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71672907-f653-31d5-9f68-c3298250f18b | -17.13329 | -48.48532 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ee21c90-249d-3c5c-a6a6-c75faa7accd4 | -14.18675 | -46.24005 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea362b8b-2c46-3aeb-bc14-68fcd91ba7ba | -18.6083 | -48.20811 | 2025-09-13 03:47:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e647ae84-f613-3047-ab83-58118c14b857 | -11.73951 | -46.62288 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4940beea-c618-3b5c-bee6-d0d7840fd094 | -11.8671 | -46.76859 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e3f17bc-df30-32d3-906b-25501fcc9eef | -11.7419 | -44.21593 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0d67c78-e58b-3e4d-8fd3-4dd49f3eec2f | -12.83617 | -47.94871 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8c73608-7e47-3d37-84ce-8ae3879534be | -10.59458 | -43.02483 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28a2a45c-826c-37d4-b929-07d2c182599f | -17.41455 | -49.2603 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd3f12b6-497a-3e1d-a13e-3d6fac159f3e | -14.21269 | -46.24788 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e163f92-481d-34bc-aa56-815b0296405b | -17.41646 | -49.25167 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a34b5d7c-e7a7-3125-ac46-99684e74a585 | -12.12302 | -44.84232 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5effb266-73b3-3566-b582-c170d36b7c4c | -7.55966 | -42.66137 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dfd5bae3-c2a4-331d-9a3e-e448d7243188 | -12.57654 | -45.6702 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 951980ad-ca99-36e2-adc7-d07f684a8465 | -13.91878 | -48.222 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2752d751-bdd0-325e-9cdf-0ad474e1b5a6 | -12.56227 | -46.93867 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a67db897-f6a1-3a03-a190-f48d257a2210 | -9.65367 | -45.81266 | 2025-09-13 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f1f2844-71f4-3192-b1da-df5e6facbe36 | -12.08135 | -44.89829 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 815009fc-c61b-3a5f-a1da-60d03993c817 | -17.28594 | -47.2424 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6aae05-34d5-32f2-9181-f2071443e41b | -14.22798 | -46.30006 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19d5d384-82d7-3f85-9468-683ba2292eeb | -11.42401 | -45.61231 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0d0a2ae6-d1bd-37c1-8203-1b36b25b9b47 | -10.23966 | -48.64577 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| edd89187-92d4-39f4-9c6c-c3705bee4bc6 | -10.84851 | -48.18417 | 2025-09-13 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 316ff4fd-379d-3902-9d6f-2b5ed279ead4 | -13.94598 | -48.18609 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4a8e05b-1649-3b47-902a-60af8e5f4a1b | -20.1 | -46.91324 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3d4fd16-f15f-39be-8709-41f12fb23fa2 | -11.85775 | -50.58218 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 892c278d-21f8-37e5-8a7a-9efed1c9ccc0 | -13.91831 | -48.28561 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be0eba21-ece3-397a-b22c-5657a0657235 | -16.40998 | -49.24598 | 2025-09-13 03:47:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e324c4f-955c-3d1d-9bb0-d5882be5d8f8 | -7.55184 | -43.95442 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9531a1-559a-3d95-9302-968174864dcc | -14.21289 | -46.27489 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d62f2467-8317-3b07-8a38-e17d9d6b7686 | -11.84698 | -50.57563 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bd02569d-363d-3cd9-abcb-1969e55f9333 | -10.72625 | -48.62395 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5020a7f9-429a-3632-bd55-e9251d4c6d4a | -13.95104 | -48.18661 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b366454-a4e5-341c-b1ce-bdfeb57cee27 | -13.9137 | -48.27934 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 32924f28-c78b-3b35-a530-71654e0ace89 | -18.42819 | -43.65319 | 2025-09-13 03:47:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0db8ada4-19d0-3af7-8889-c7d43816b514 | -11.13683 | -50.72225 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37bb59c2-1c70-3457-af9b-c844d55980cc | -8.46824 | -47.25034 | 2025-09-13 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a128fc54-7489-3fda-a65c-27ec147b183c | -11.4228 | -45.61873 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7facd945-0943-395e-a8a0-ee96c9a05104 | -11.72863 | -46.58842 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f48e11e-0738-3e5d-8cb8-4090fedc8d75 | -12.82807 | -47.95749 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df7979a7-1ee4-3d5a-aa32-2efabb63471f | -14.18138 | -46.26712 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 33c81e67-460b-3688-a466-e8d2dedd7161 | -11.20168 | -48.42586 | 2025-09-13 03:47:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a10aa91-b554-3cc4-860a-28fe624b9e2b | -18.44028 | -45.93632 | 2025-09-13 03:47:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b27d528f-100f-3d10-9f88-d100604cbbc0 | -11.83988 | -50.57403 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| b791d11c-9a67-3efe-92fe-88dcd5f5f99a | -11.40484 | -50.74784 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dffeb452-c801-3dbd-a69f-765b81d64821 | -16.6082 | -49.46833 | 2025-09-13 03:47:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0db1c1e0-bb47-3694-92d9-bda070fbcc9f | -20.33334 | -46.66682 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ddc692bd-0826-373f-9124-cbdba2661b22 | -13.13933 | -47.13564 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af6f2acd-7cb7-32ab-ad66-70a6cbf8c03f | -10.36949 | -50.50089 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2aec7e18-8ce4-3fab-88c1-0b2a1ae9a01b | -10.79154 | -50.55344 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7fa2fddd-01c6-346b-86c8-0113d30797e0 | -8.47004 | -47.2538 | 2025-09-13 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e4c9878-790f-37ce-9b27-98315dccaa98 | -13.91533 | -48.20831 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02a1fe1c-374e-32b9-9c05-c233bd4a6a8d | -14.19012 | -46.25077 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf9fe4b9-0318-3aaf-b2c9-533b5eaf5384 | -10.77865 | -50.54276 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6204b391-055c-35e2-bbff-c36f36b61b7e | -17.995 | -46.93825 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de6629ed-23af-350e-a4a3-298466a8ebf8 | -12.1156 | -47.59921 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0613158e-b464-332c-8c6c-bb23bea74568 | -18.33314 | -49.44507 | 2025-09-13 03:47:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88b10403-e944-3e0b-baf1-19861ead61e0 | -12.11584 | -44.853 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33bc8796-26b0-3300-8075-54ce6c279bd3 | -10.78136 | -50.53538 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 76335821-fbbf-3bd7-90c3-7980e5e16380 | -14.19741 | -46.2696 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa164459-497a-33eb-840d-e426d377ad49 | -8.94176 | -44.44676 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce50639b-bbaf-347b-a097-c637e28f26d0 | -10.8521 | -48.1885 | 2025-09-13 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9ead28f-b499-33b2-901f-458849e8f6ff | -14.20389 | -46.26465 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e704483f-54f0-323a-a6d1-a48f16b023cf | -11.62445 | -46.60242 | 2025-09-13 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d1cf661-a802-3b3a-a85f-1eae89158741 | -14.19538 | -46.25198 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9f11ed3d-3b0a-3d6b-a881-5abd3317ae5f | -14.21411 | -46.26868 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 178a98e3-55c2-3894-a01d-4866b706f3b5 | -17.40755 | -49.26348 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b06219a-e8bd-3639-ba04-6e1fe1568cdf | -7.94287 | -46.9047 | 2025-09-13 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52773875-8d81-38d1-94e5-2490e2820e21 | -14.19996 | -46.25666 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4b2ef91-2f22-3207-a2d9-c46995215fea | -17.30322 | -48.73424 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7ad93d8-2560-3644-9d7d-32f2d5f4e4d1 | -12.99459 | -46.75263 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fd08c14-d281-355f-ad73-92a9b775b702 | -11.42929 | -45.61367 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77f49931-613f-379b-bb91-d4d4c6f4da75 | -8.05197 | -44.51822 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f95be538-de34-3ce1-bd89-e1f37cc4a976 | -19.98831 | -46.9041 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 83cbe25d-7754-3271-ab60-addd4e53c38c | -18.17998 | -45.20982 | 2025-09-13 03:47:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3750caee-f47b-3ca6-912d-2da9717a2914 | -17.41327 | -49.23246 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 259378e0-67df-38b1-9adb-ace58da8d193 | -18.33601 | -49.4415 | 2025-09-13 03:47:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8adbef93-41bd-3422-87ed-7d52da8b8f37 | -20.10262 | -46.92543 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a1a16e96-2ddf-320b-b77e-2589461a6fb2 | -14.21333 | -46.2446 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20869ba9-61b6-3965-bf7f-cf881ef9c69d | -13.77831 | -46.28946 | 2025-09-13 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README31.md)
