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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 555209db-f1cf-370a-aa5c-6ee3f1029d4a | -13.80912 | -52.79852 | 2026-10-08 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5f69761-1ffe-3a7e-baf3-b862fac5330e | -15.33685 | -42.77875 | 2026-10-08 04:04:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc57270-7ea2-3bfe-b4e3-2c9e3610ba50 | -10.88022 | -49.15032 | 2026-10-08 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c7f1f02-b4c7-3804-9558-69ac2c3b6b7b | -13.17432 | -48.13724 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 446b16a3-52ed-3b35-8cce-ff476b760e87 | -11.74208 | -44.94392 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94d6f522-80af-361f-be7e-d2ccb319c673 | -16.144 | -43.75058 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71078dc5-bdc0-3a92-9904-9d8a50ef8913 | -16.85423 | -40.57645 | 2026-10-08 04:04:00 | NOAA-20 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ededa62-db1b-3dd0-b0b2-6517ed9ebf84 | -13.69332 | -49.12421 | 2026-10-08 04:04:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 161b119c-be0b-34da-ade2-591bb9f26f51 | -11.75608 | -44.93532 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6638bf33-2425-30b5-b07d-a436ad72e942 | -11.76335 | -44.94414 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adbb5e27-4491-3b7c-8371-703c9e958fff | -11.7601 | -44.93612 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd3138ea-3533-3e29-b468-450128390718 | -16.97537 | -41.22831 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fb72a8c2-3335-3f1f-9945-c0743a615e3a | -13.90798 | -43.99464 | 2026-10-08 04:04:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9632437d-41b5-3699-a89c-b71ad8148d48 | -12.2287 | -44.7161 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efeffc91-6299-39da-bb56-e625df19db1c | -19.68319 | -42.03522 | 2026-10-08 04:04:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 21187384-acab-3944-b738-13266eb03383 | -15.10935 | -43.62685 | 2026-10-08 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 900cf7b3-9c2f-3795-a51f-71b5cef83e73 | -12.23727 | -44.72975 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e7558c5-4c91-3b4b-af0e-17f6fb3244fe | -16.54115 | -43.27786 | 2026-10-08 04:04:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5731ade-a036-3789-bafc-51bce98c0b5d | -13.23043 | -43.40011 | 2026-10-08 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a3adacdd-3292-3272-a789-6cb91cbab4a0 | -17.97985 | -41.44817 | 2026-10-08 04:04:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cd3ce457-363c-38ab-8b79-770485f09e9b | -16.96936 | -45.69238 | 2026-10-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca5684a2-4b91-30a3-bb6a-da9e4ea1a0e5 | -14.91788 | -48.11212 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d53945d8-5b58-3ba3-9c86-35a6991b0fba | -16.58321 | -41.59453 | 2026-10-08 04:04:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 004c526f-c460-329c-9acd-17bbbc7a4652 | -12.20418 | -48.42497 | 2026-10-08 04:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25e1812f-ea55-3403-a2a5-30ed97ffd429 | -11.39655 | -47.55036 | 2026-10-08 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a84e647f-ae7c-31f7-8bad-01cb875f9c50 | -18.25698 | -42.17305 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 976b2c90-1c90-3d09-8417-6257da024bd7 | -12.03714 | -43.43915 | 2026-10-08 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0523d00f-5b41-3f8a-979a-c021e8a3f53e | -11.37716 | -46.66381 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94d3807d-27b5-3f8e-9987-e39957be1863 | -19.70056 | -42.01199 | 2026-10-08 04:04:00 | NOAA-20 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92ebde6c-6e54-3bd3-a727-c79083d8624e | -18.02179 | -46.20705 | 2026-10-08 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 500b90f7-1bd8-3ac0-b689-55655599a831 | -13.19094 | -47.86928 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bf7597e-465c-3591-a42a-f881307ae0f5 | -13.35954 | -43.87515 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17d62865-e4b9-3616-a221-3ba10e5dceac | -16.00966 | -43.60495 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c441f05-b76a-3633-9c70-402e80ff67db | -16.89943 | -40.89433 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c85fb528-93b6-3d50-8187-9fd5ee54a429 | -11.76528 | -44.93339 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 698f0762-1016-3f42-a915-b1083b44a28f | -16.97868 | -41.22888 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92430604-de5d-30f7-8660-993b987acc86 | -16.12647 | -46.88653 | 2026-10-08 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b8020eba-856d-3672-82ea-1ece998be51b | -12.81344 | -38.266 | 2026-10-08 04:04:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e8797be-2473-38bd-b0ef-fe39883d7b72 | -14.53809 | -40.32026 | 2026-10-08 04:04:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e94bd63f-05d4-3924-9cf8-e54c85161eb0 | -17.11707 | -41.34065 | 2026-10-08 04:04:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ff426a0b-596e-3d69-b6e7-d4948eeceefa | -17.76259 | -42.42804 | 2026-10-08 04:04:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 41b8e914-0d47-3bf6-8833-bac61f863983 | -17.50364 | -41.91337 | 2026-10-08 04:04:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1d54fed9-f402-3a53-b31d-f95e94183789 | -13.16646 | -54.32114 | 2026-10-08 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4f54d4-3056-369a-8e52-057c17de8116 | -13.39596 | -43.87406 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e9030ea-863d-33fb-a654-b63f325e9145 | -16.89337 | -40.88961 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8b948b3a-304b-39f6-9e60-2e45228b8fac | -15.68054 | -50.57164 | 2026-10-08 04:04:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dd26f1e-2688-3a03-91ea-1aa576e88da8 | -11.76058 | -44.93637 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6b6e976-a898-3fe2-945f-9802ae670b78 | -10.8809 | -49.14669 | 2026-10-08 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc143d9c-8539-3c0d-890f-5b91bf5d4945 | -11.78569 | -46.77916 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4aa683c3-5c43-385d-bed6-12ecfd4ba058 | -16.89281 | -40.8932 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 82e5498d-9401-3555-8d8e-69a81c183d9c | -12.20519 | -48.4266 | 2026-10-08 04:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddf43ab9-d2a9-3586-a481-1b1bae3f62ec | -17.11202 | -41.3509 | 2026-10-08 04:04:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4deb0d4a-ce94-39d9-8b4b-dcf6b2afc897 | -15.11221 | -43.63172 | 2026-10-08 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e912c0fd-e341-3a4b-8451-9b832c2b5fd0 | -13.80332 | -52.79304 | 2026-10-08 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1970daa-8397-3f06-ae9e-f5ad373cdc56 | -18.62471 | -41.2796 | 2026-10-08 04:04:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 957446e1-2346-3112-824a-2330e69f4d90 | -18.98453 | -46.5756 | 2026-10-08 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5224c7a-bb74-309f-be19-cc5136da51eb | -15.62362 | -42.99437 | 2026-10-08 04:04:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fa47d9c8-91c8-3741-bd26-01789bca87de | -18.72158 | -39.90068 | 2026-10-08 04:04:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f5461428-daa1-358c-81f4-e6a3fcf78567 | -18.38449 | -40.31692 | 2026-10-08 04:04:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8b41745d-6224-3fcb-8cec-4870a8e0a7a0 | -18.01785 | -46.20623 | 2026-10-08 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c9887a-5ca3-3674-b62e-dc477383d897 | -18.22669 | -47.32981 | 2026-10-08 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2075b46-72a6-3896-8bc7-d64914f2e96c | -14.89163 | -44.81319 | 2026-10-08 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a6aefe5-1ae2-38c7-9daa-5e6b0e554bb7 | -13.34782 | -43.9666 | 2026-10-08 04:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dbbb185-d010-389f-9017-2fa2319c32b4 | -13.36106 | -43.87706 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f1d810-6ef0-3821-8de8-a44dcdde5870 | -12.70447 | -45.82534 | 2026-10-08 04:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee96cc73-7cc6-334f-bcbf-9cdb340c2b2c | -14.91352 | -48.0842 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2916eac9-7a9b-3440-9c8e-ca8e1d78fbae | -11.78481 | -46.78394 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d9a2dff-e423-3d86-93cc-c4d96b0cdce9 | -16.05177 | -40.6492 | 2026-10-08 04:04:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a5123e9-df05-33b3-9fa6-d9e1483566bf | -11.91926 | -46.79774 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df212a53-ca65-3135-928e-3ffffbcddfcd | -11.35406 | -51.87831 | 2026-10-08 04:04:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3d7348b-560d-33c2-9bd6-41d8d66108aa | -11.39259 | -46.68245 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0d864a4a-39d7-3474-b92c-6ec1ab14d55b | -16.85754 | -40.57698 | 2026-10-08 04:04:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 81d8de9d-9f88-3f42-a267-f54a73b5d0a5 | -15.47653 | -45.19879 | 2026-10-08 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b632a3c7-0f60-35db-bd3a-1eb5c1e002b7 | -13.36926 | -43.87389 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dee46ff-9fcf-3119-b08a-d3e6dc7a617b | -13.75163 | -43.66418 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cceaa0e-4a9a-347b-8233-a52f12fb9658 | -17.43004 | -43.57396 | 2026-10-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70340a81-a223-3b73-bf65-ac6d578d858f | -13.19 | -47.87435 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac488ecc-ddaf-34e2-990b-c59f45677136 | -11.39442 | -46.69826 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fb56fa0a-5aae-38ec-87a3-4eed1c6b6c61 | -11.34769 | -51.87708 | 2026-10-08 04:04:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9450796a-4234-369e-93f8-cb05bff86174 | -11.35296 | -51.88372 | 2026-10-08 04:04:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e275fee9-72a3-3bb3-a07a-56eb538e46ca | -18.98219 | -46.57662 | 2026-10-08 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42d6056a-9758-30b0-80ca-b99fb0634de7 | -16.83524 | -41.04197 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 28547f65-6234-3771-842d-103b8b6b31f2 | -15.44842 | -42.02633 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 471fc098-e00c-36fc-bd63-74a7414c424e | -14.91686 | -48.1174 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04161fb6-2696-38df-b24f-cdd9b94786f0 | -14.93373 | -48.10585 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80ecf194-0458-3a86-8798-51eeb0ddd096 | -11.75655 | -44.93557 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d73169e-c82b-337b-8e53-76861e163e73 | -11.53057 | -47.59291 | 2026-10-08 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 47f9e7df-7f76-3214-9c7d-0ee1d355a2cf | -13.19056 | -47.87005 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a0955fd-d5bf-3fde-bd04-74fea19cd55a | -14.91429 | -48.10543 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9794384c-f5b8-3620-a8df-d0326d33244f | -16.89556 | -40.89735 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c67e57eb-0dfa-3dea-a23d-f6d36e2a0e78 | -11.34027 | -51.88103 | 2026-10-08 04:04:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4eb3d124-0649-30bd-915c-4612133a7e11 | -17.42822 | -43.64851 | 2026-10-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e9eba1-0f33-3c39-bf56-c3eddccf936d | -15.4235 | -46.11825 | 2026-10-08 04:04:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 026777ef-12b5-3a7d-a000-4ef1f9b7463e | -11.77121 | -46.78104 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a170924-417a-31fd-a076-274dd5f4d3ac | -11.75203 | -44.93463 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14865abc-9c4a-3e8b-bacf-9ce7a6de27e9 | -17.53965 | -41.6918 | 2026-10-08 04:04:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c359c0c-334a-3a37-87d0-68f8fdeeb6a5 | -14.45549 | -42.1917 | 2026-10-08 04:04:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cfe56f51-40dd-3b25-8718-9211ff8c22fe | -17.71266 | -42.02884 | 2026-10-08 04:04:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5dfc3655-a6cc-3e40-94fc-df0a80686da6 | -11.38899 | -46.67635 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d4f2b1b1-85fd-3c5f-81a7-70e4da7c9dd5 | -12.04081 | -43.43985 | 2026-10-08 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README73.md)
