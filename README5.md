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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11a95cd2-eaac-3bbf-b8bb-50cdbccd1267 | -11.52178 | -47.5497 | 2026-07-29 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38451464-a878-32c9-b301-4b498b2be7eb | -12.31205 | -46.75019 | 2026-07-29 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94ba59e1-59d3-3b0e-b48d-0a2275d7f754 | -11.53249 | -47.56416 | 2026-07-29 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8918b200-879f-38e7-b6b8-a60425ec2fd0 | -11.96311 | -43.37642 | 2026-07-29 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77de2cd8-0d6c-3753-b7f1-5303c7e91e84 | -10.93169 | -43.05804 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a7caa2f7-588b-3942-96d4-db5ee253a407 | -9.60883 | -47.76907 | 2026-07-29 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4fbf1c22-ca36-3d56-8fb3-6c836b0c128b | -15.06723 | -41.21914 | 2026-07-29 03:38:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5fd14331-2fc4-3afa-95f1-3e3c0e8788ae | -12.37539 | -43.90559 | 2026-07-29 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa14fe52-9bec-3f5a-83cd-700a486c06fb | -7.3413 | -45.8377 | 2026-07-29 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 7fd1ec28-73d3-3153-a8dc-1499c44eb55a | -7.36 | -45.8361 | 2026-07-29 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 242bf8b9-0586-38e5-a975-0aa5a3a96018 | -10.9397 | -43.0593 | 2026-07-29 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2afe07bd-eae3-3823-a215-be0447af6508 | -21.42848 | -41.2424 | 2026-07-29 03:40:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a41b6918-a81e-36de-a82d-cf552f729f2a | -21.02941 | -42.36579 | 2026-07-29 03:40:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a43dab6e-3aa1-38e7-b309-4b18a832cdff | -20.03499 | -46.36643 | 2026-07-29 03:40:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388e9cdc-8b7a-3608-904e-405f44e3146d | -20.23893 | -41.50041 | 2026-07-29 03:40:00 | NOAA-21 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52698af8-6ec3-3d51-b607-a35480754b09 | -20.3785 | -43.71334 | 2026-07-29 03:40:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c5f7dd91-2ec1-3d6a-9e80-8e338ed1541c | -19.68926 | -42.02696 | 2026-07-29 03:40:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 145e1994-7c9b-37eb-9a97-90c6b58281bd | -20.72744 | -40.59955 | 2026-07-29 03:40:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bbb10ec8-809f-3a44-a7f3-0d98d5182607 | -20.67108 | -40.51347 | 2026-07-29 03:40:00 | NOAA-21 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 578bcc43-de16-3510-ba6c-4bba49a03e4f | -18.52051 | -46.17781 | 2026-07-29 03:40:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d2586bd-9a76-3c0d-96ad-8204873bf691 | -20.30473 | -46.35653 | 2026-07-29 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 069c401a-5877-32a1-b15a-66aa93e26b30 | -16.1526 | -48.61798 | 2026-07-29 03:40:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d21f571-dc7c-34e6-a38f-7da371d19434 | -21.0851 | -44.01147 | 2026-07-29 03:40:00 | NOAA-21 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 32c5a45e-12eb-3043-975b-828e9156e87b | -20.30543 | -46.35329 | 2026-07-29 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 685a3ebe-092e-3430-bef9-e6c2ae618781 | -22.87967 | -43.75434 | 2026-07-29 03:40:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2f3ced0e-8d8a-36f4-8f50-12ff0f081ca9 | -21.35931 | -43.75441 | 2026-07-29 03:40:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 84003ae5-1999-397e-9454-d2f5ef299298 | -20.79225 | -42.83621 | 2026-07-29 03:40:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 70266a49-1821-3143-b3fa-2be79528642e | -16.15386 | -48.61228 | 2026-07-29 03:40:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75586e20-ddea-31f5-b748-42183dc61f2a | -21.35787 | -43.75578 | 2026-07-29 03:40:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8275c432-1d76-3f08-87e7-5ed5d12f10f9 | -22.70203 | -43.36332 | 2026-07-29 03:40:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fbc1b2d8-2252-3946-a886-4acb5e7e6ac7 | -21.35231 | -44.8201 | 2026-07-29 03:40:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 20e4586c-1734-3e8b-b17d-6e1f29494ff2 | -21.45086 | -43.79302 | 2026-07-29 03:40:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fd6b310b-1a6a-3169-8271-575c201d1c73 | -21.58343 | -41.24686 | 2026-07-29 03:40:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4f586a17-082e-3f71-8379-4aa2b7121adf | -22.87547 | -43.75339 | 2026-07-29 03:40:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c8e597b7-2a61-3dbb-8ed5-3cc5610668bc | -20.01491 | -44.23832 | 2026-07-29 03:40:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d77a7469-4cf5-3ca7-b05a-b7826919b8bc | -21.02035 | -44.57814 | 2026-07-29 03:40:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 850948f5-fad5-302e-a50d-5dc537f63213 | -23.40596 | -46.42472 | 2026-07-29 03:42:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 998ad64e-0b7c-30b4-b60a-0bf14a177bee | -23.8457 | -52.86349 | 2026-07-29 03:42:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2c150799-610b-3d9e-8760-0c4feb332d53 | -23.09939 | -52.68805 | 2026-07-29 03:42:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 85d7796d-012b-35b5-8f1f-3419de60652d | -23.10128 | -52.6808 | 2026-07-29 03:42:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| f20a7d90-7725-30c0-a32f-e6567e01316f | -23.0153 | -47.36843 | 2026-07-29 03:42:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e677625-09d7-3efc-899b-fdd06fc5e8a3 | -23.01422 | -47.37015 | 2026-07-29 03:42:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf8a63d1-8a46-399f-8ff1-aed2a77e5c84 | -23.01501 | -47.36666 | 2026-07-29 03:42:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e100314f-b113-34a3-9a6d-d92e700d24c3 | -23.01009 | -47.36709 | 2026-07-29 03:42:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 17a39f87-db2c-3b78-8aff-596039df383b | -7.3413 | -45.8377 | 2026-07-29 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 4916e9ef-6ce9-3cb4-8a03-0f4cb21a4b0a | -7.36 | -45.8361 | 2026-07-29 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 6a1cbff7-5aba-35b9-88f3-b635c04a65db | -20.3058 | -50.5981 | 2026-07-29 03:50:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.4 |
| 0f9f3a44-7c01-3e84-b8e6-ee6e1418f2d2 | -7.341 | -45.8602 | 2026-07-29 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 4062bba7-462e-3107-8e8d-e1f4f2410c46 | -10.9397 | -43.0593 | 2026-07-29 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b879ee09-9081-3618-a331-083e5150e4da | -20.3052 | -50.6207 | 2026-07-29 04:00:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 155.6 |
| f745f268-90ea-3815-bf6d-669eb4cd3152 | -20.3262 | -50.594 | 2026-07-29 04:00:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| 7461eea3-418e-3667-95c2-b634225b1937 | -7.3413 | -45.8377 | 2026-07-29 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 950b9c70-c644-3006-81aa-ee6ce3d41f6e | -20.3058 | -50.5981 | 2026-07-29 04:00:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.7 |
| 2178f8c4-0811-3d22-b409-5a5f979fee7f | -7.36 | -45.8361 | 2026-07-29 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d09610cb-76a4-34e4-b02b-e75225081e3a | -10.9205 | -43.0622 | 2026-07-29 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| e655bc9e-5bcf-329e-87c7-995af5a28d1b | -10.9397 | -43.0593 | 2026-07-29 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ab678944-1dc3-3e46-8c25-2394afee4d2b | -7.3413 | -45.8377 | 2026-07-29 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 78024d30-25e9-3a2c-a902-f07100acf9aa | -10.9397 | -43.0593 | 2026-07-29 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0f584252-b3ce-30ba-ab82-f6a9142f1158 | -7.36 | -45.8361 | 2026-07-29 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c0a0b137-0287-3e47-acde-b8af17b328be | -20.3058 | -50.5981 | 2026-07-29 04:10:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 194.1 |
| d23de9fd-e8bc-3a00-8b66-63e73afd4fa5 | -20.3052 | -50.6207 | 2026-07-29 04:10:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.1 |
| fff4b19f-8542-39c5-a757-1bc489aea7b6 | -10.9205 | -43.0622 | 2026-07-29 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9691bb81-33bd-3b68-8921-1275e61d6ef9 | -20.3262 | -50.594 | 2026-07-29 04:10:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 02da1e4e-5212-31cb-942f-077403760718 | -0.98976 | -48.08476 | 2026-07-29 04:10:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8404b79-054e-3e53-976d-88fba271afa3 | -2.85726 | -40.08027 | 2026-07-29 04:10:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb3769a6-da4f-3069-a1bf-291cb94efd12 | -0.99515 | -48.08562 | 2026-07-29 04:10:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68a775f9-bb73-3b86-9665-0787834af195 | -2.95094 | -39.92035 | 2026-07-29 04:10:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ebc97ea-7c29-3ac4-9870-e30c30c4ce5f | -2.95375 | -39.92078 | 2026-07-29 04:10:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0c991acf-cb23-3370-b489-dacc54a6aed7 | -4.36618 | -47.76544 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d6c27ac-cfba-3c61-8c80-6f6f67f993c5 | -6.87732 | -46.01741 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3b3ea6ae-00b1-341e-8319-782119e6c6e9 | -5.84043 | -44.89722 | 2026-07-29 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70700971-94cd-3e5d-8390-26e670df79c0 | -4.94291 | -48.24796 | 2026-07-29 04:12:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb835ef5-4e36-3f3e-a901-6a084051c958 | -3.6792 | -47.64768 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f87b7d59-2052-3ffd-a419-64fcc21fa275 | -7.40928 | -43.77222 | 2026-07-29 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e2bce29-2c5b-353e-bb1d-39e434d7caff | -7.71218 | -36.319 | 2026-07-29 04:12:00 | NPP-375D | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1742f73f-06f1-3d25-8397-9669aebb5f9c | -4.91235 | -43.4675 | 2026-07-29 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92df89d6-8333-3a73-8e83-bef8c334454b | -3.03411 | -48.41673 | 2026-07-29 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76187ab1-c925-3a85-b1e2-32a7cd8e9bd1 | -7.34966 | -45.83368 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 94bd2ddc-1dab-351d-a36b-a69eb0f7791f | -7.73104 | -47.24909 | 2026-07-29 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb44247b-1f99-31c0-9adf-a8cf7d523081 | -6.15447 | -44.65555 | 2026-07-29 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b97f9f6f-07f4-372d-84cd-299f6ddb1133 | -6.878 | -46.01345 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8101a628-c545-3c58-9de3-9cfb6c07e6b4 | -9.30242 | -38.19595 | 2026-07-29 04:12:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ab6655d8-3c62-370f-81b2-566d2cf7f997 | -7.45889 | -46.15418 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58578dcb-96f4-3255-8457-547cb05e89ee | -7.34291 | -45.84814 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b5d3008b-d58c-3c80-8572-5c6aacfc2fd3 | -9.01209 | -40.99318 | 2026-07-29 04:12:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcc9fee3-db5a-3138-b17e-5cc736069ae7 | -7.34837 | -45.84129 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7762844f-d406-3695-9b0f-f06534353cc9 | -7.34356 | -45.84433 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6551dbb1-267a-3655-8e57-783a322d3977 | -5.82248 | -44.74937 | 2026-07-29 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a4fc6df-c394-3c14-a8b3-f3765d3f3d62 | -3.68919 | -47.6495 | 2026-07-29 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb41c6af-8947-3f32-8ebd-30907d67f2da | -6.87507 | -46.00505 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7647cd20-401d-335b-8c72-b3e9fd2c9f3e | -4.37117 | -47.76625 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c28da32e-2559-3fd3-8397-2db5a6afca2c | -4.37021 | -47.77204 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7a330ff4-45ce-3b95-9c32-2d139e8e141d | -6.33466 | -44.60718 | 2026-07-29 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 786c0d01-4bbe-333a-815a-86228e7e208b | -7.35382 | -45.83443 | 2026-07-29 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 22d255b6-5634-3479-a974-0a29171a45f9 | -4.8742 | -45.30951 | 2026-07-29 04:12:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 133740b4-2440-39bb-a78d-b957e3b0b243 | -4.36963 | -47.77224 | 2026-07-29 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 69d4e09f-199e-30d2-afac-67bf30e742ad | -7.40561 | -43.77161 | 2026-07-29 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5b7e565-5ba6-384d-81e9-d35b4a5f96b1 | -6.86948 | -46.01221 | 2026-07-29 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c63d5b3-4feb-3f3f-91ed-06382c7c4fd1 | -4.11792 | -49.08601 | 2026-07-29 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f54dae9-fc87-33b0-af6a-39e960e0e98b | -5.73049 | -39.03665 | 2026-07-29 04:12:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README6.md)
