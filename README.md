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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f465df5-7c2f-35c0-95bb-ab844a0688e5 | -9.6136 | -47.7508 | 2026-07-30 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 5272becd-62d8-3994-9b26-204856217435 | -9.6133 | -47.7728 | 2026-07-30 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4d7d0a08-9ca9-3d38-97b1-9dce6fe3e90c | -6.6559 | -59.1174 | 2026-07-30 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3ac422c2-bca6-3276-a971-c67566004bc7 | -14.1797 | -43.9875 | 2026-07-30 00:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| e040f793-66ca-3a82-9963-6c0a2c5174e5 | -9.6136 | -47.7508 | 2026-07-30 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3a6bc8b4-2dfd-33a3-972d-5a5f9d0a51d5 | -14.1993 | -43.9839 | 2026-07-30 00:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| a54c68af-10ff-3db1-b402-8e841cbc1945 | -9.6133 | -47.7728 | 2026-07-30 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 97c6060f-db7c-3dde-9e67-0507fd1230d5 | -20.72917 | -54.59723 | 2026-07-30 00:11:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3344da12-edd1-3d5a-8d3c-7eb3fc64d124 | -19.18124 | -47.3571 | 2026-07-30 00:11:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| acdc65db-2616-31e5-9cd0-777fdbf71390 | -21.8027 | -53.37471 | 2026-07-30 00:11:00 | TERRA_M-M | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4c9393a1-86bf-3b4b-8d05-4cc885cc3638 | -21.06606 | -48.54566 | 2026-07-30 00:11:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| c009f420-c551-3365-a5e4-d962498406ff | -18.22856 | -42.21091 | 2026-07-30 00:11:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.5 |
| fc715540-7c60-3cdb-876e-2b6b4c65f244 | -18.22437 | -42.20435 | 2026-07-30 00:11:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| 89b096c4-87da-334e-a5e5-ef021b4ae3e8 | -21.06738 | -48.55508 | 2026-07-30 00:11:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.3 |
| a6073590-e5ce-34c4-b207-aed900b0a341 | -18.5191 | -46.17669 | 2026-07-30 00:11:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b5b8bcd3-d5bb-3c22-a32e-9959dcc62d0d | -18.90247 | -46.07291 | 2026-07-30 00:11:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3afe7d7-11a7-3fd7-baff-ecfb0e903054 | -19.17972 | -47.34693 | 2026-07-30 00:11:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6ec7bd32-ab0a-3f50-9f6d-a406cff28a7d | -18.04324 | -51.31217 | 2026-07-30 00:11:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1429fa6d-aa35-39ae-9704-7c896fcdc689 | -17.84048 | -41.97267 | 2026-07-30 00:11:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 28143649-ad30-30e6-83c5-1e8c6f34e873 | -20.3333 | -47.53822 | 2026-07-30 00:11:00 | TERRA_M-M | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50d7d800-293d-324b-9a27-a29dfff9ac85 | -21.20371 | -48.94154 | 2026-07-30 00:11:00 | TERRA_M-M | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2502b01e-3e77-32b1-8924-bf6453d3e0fc | -20.73112 | -54.61489 | 2026-07-30 00:11:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 48cfcb24-033c-319b-8781-7c5a6f1a407d | -20.59983 | -48.17189 | 2026-07-30 00:11:00 | TERRA_M-M | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 27de73f3-9055-3df1-8f3b-e1f2ae27de83 | -21.04539 | -48.46216 | 2026-07-30 00:11:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d1caed0-4b46-3416-91bf-2178ab5af535 | -18.35687 | -47.20559 | 2026-07-30 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 02c0d806-bca4-33a6-979b-9f4669eb3cdf | -20.34449 | -40.9478 | 2026-07-30 00:11:00 | TERRA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| f55070e3-2b1d-3bbf-aa66-00502bdc84f5 | -21.03654 | -48.4636 | 2026-07-30 00:11:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5ac318cc-f554-32c5-9f42-bc9498064dc3 | -18.36461 | -47.19352 | 2026-07-30 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8f85d268-c52a-37ca-a8c7-5f144de73b80 | -21.35095 | -44.82956 | 2026-07-30 00:11:00 | TERRA_M-M | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 0531e3a1-bd39-3043-b4b9-648e8bb96b2c | -20.72512 | -54.60903 | 2026-07-30 00:11:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 7a79ea5b-64f9-3570-974a-0a4c57b59efe | -18.36616 | -47.20396 | 2026-07-30 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d4817ea1-3997-3d97-9655-bf5991e2a2d2 | -20.59848 | -48.16239 | 2026-07-30 00:11:00 | TERRA_M-M | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5955dbc3-7a7b-3b9c-a898-19cff8837631 | -18.5954 | -48.20515 | 2026-07-30 00:11:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a7664d61-3e21-3996-9166-19477e03bb8d | -19.83024 | -48.20682 | 2026-07-30 00:11:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 801e6994-b68e-32a3-ab39-96adf8ee3ec1 | -21.80433 | -53.38968 | 2026-07-30 00:11:00 | TERRA_M-M | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f848f547-3046-3341-a943-3d515ebe99e9 | -21.34883 | -44.81674 | 2026-07-30 00:11:00 | TERRA_M-M | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 4d3cd3ef-98dc-3071-918f-05b68c6971a3 | -21.20242 | -48.93208 | 2026-07-30 00:11:00 | TERRA_M-M | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.8 |
| 1712cf88-63f4-393f-9c36-7502c0348ba0 | -17.73721 | -50.45668 | 2026-07-30 00:11:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1c8972b2-beec-320d-a3f6-834cc433a0b6 | -18.04194 | -51.30213 | 2026-07-30 00:11:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3988c75d-6ff2-37ca-ab87-c0173791e695 | -19.27049 | -42.14518 | 2026-07-30 00:11:00 | TERRA_M-M | SOBRÁLIA | MINAS GERAIS | Brasil | 3167707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.9 |
| 45ac0a82-4112-3f0c-acd5-140be7589321 | -18.3553 | -47.19511 | 2026-07-30 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4de5a0e3-5380-3189-a77a-7c594ad97c18 | -21.04671 | -48.4716 | 2026-07-30 00:11:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0d420b94-5c4f-3bc8-b84b-389bba1473c2 | -20.87422 | -43.38206 | 2026-07-30 00:11:00 | TERRA_M-M | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| fb72f434-1897-3714-8db3-a8147f544050 | -14.1879 | -44.00031 | 2026-07-30 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| cb4eeb41-1cbb-36cc-8e34-95acea2e56b7 | -15.67978 | -54.95903 | 2026-07-30 00:13:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| cb7a4239-5638-3513-88f9-2dd4b8aa9004 | -12.14896 | -48.95487 | 2026-07-30 00:13:00 | TERRA_M-M | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b0f07f96-1be7-3dc2-9f93-19c41253f38c | -15.67804 | -54.94387 | 2026-07-30 00:13:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 77ea01b0-efaa-371d-9497-731ed11b9bf4 | -11.08745 | -47.79959 | 2026-07-30 00:13:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4d5d8fb0-261d-34e2-9bb6-3b8da7f83343 | -10.77834 | -50.86911 | 2026-07-30 00:13:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0300519e-e2f4-3a48-8215-1f25d0162cdc | -13.31418 | -43.58914 | 2026-07-30 00:13:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| fef0421c-b011-3dc6-8f9c-f5816b915a64 | -10.63291 | -47.4988 | 2026-07-30 00:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| efdd9496-bf6a-390d-af8e-e5ee144f48c4 | -11.08914 | -47.81107 | 2026-07-30 00:13:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 83283325-03e4-3096-944d-cab98ae59441 | -14.46859 | -58.60271 | 2026-07-30 00:13:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c5bf6522-2724-3fba-88c2-39ee8812ced7 | -13.1029 | -51.36585 | 2026-07-30 00:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9c077579-88b3-3425-a8bc-260f2b9c365d | -13.96469 | -49.14587 | 2026-07-30 00:13:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 25b05369-fbff-3800-8fbc-40c2b41e31a9 | -11.2986 | -44.76556 | 2026-07-30 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c6b903b2-0b41-315b-97ba-94ea56f43e08 | -10.63109 | -47.48677 | 2026-07-30 00:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f81555f6-4634-3788-8a60-d091863590b8 | -10.95346 | -49.81161 | 2026-07-30 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67efe2f0-c351-3398-a96d-ff0b65c4b21e | -13.41601 | -42.49403 | 2026-07-30 00:13:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 56131281-d0c6-3b5c-8e6c-adedfe068ef1 | -13.68275 | -44.38486 | 2026-07-30 00:13:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6e1f2cee-3ba7-307f-ae38-62a088b941a3 | -16.68597 | -49.22646 | 2026-07-30 00:13:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ede2c42d-5676-3848-b28d-b9800497cfa8 | -11.39373 | -50.12442 | 2026-07-30 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 44b4afd7-6afb-3b44-94b5-8c498b15adc5 | -16.79539 | -49.15593 | 2026-07-30 00:13:00 | TERRA_M-M | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0197fdef-2191-3728-8706-dff67e4b0e86 | -12.62863 | -44.62492 | 2026-07-30 00:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a1d02058-d90f-3cff-98b8-e7b0d073a954 | -13.95571 | -49.14725 | 2026-07-30 00:13:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| fab10921-f326-3ea6-854a-0fe6b73842da | -13.67984 | -44.3669 | 2026-07-30 00:13:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3a11ecec-9d79-331e-a5d3-9fa7c1c0b875 | -12.31452 | -46.75629 | 2026-07-30 00:13:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 36f1649f-3f36-3d6a-9d72-b4829f5ee30c | -13.31726 | -43.59495 | 2026-07-30 00:13:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a53c39c4-6ad7-31ce-a4d4-25bdc1ad4e59 | -11.41658 | -50.09319 | 2026-07-30 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 02013274-3dcb-3316-a235-9da72e6e61cc | -10.77957 | -50.87805 | 2026-07-30 00:13:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a8434d1d-6794-3c8f-9de2-c014627a54f6 | -13.41314 | -42.50037 | 2026-07-30 00:13:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 20333ef3-6e62-392f-b2cc-847c5d76b33a | -13.10413 | -51.37505 | 2026-07-30 00:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 47ad0432-7848-3873-a214-191c102a7d76 | -13.95437 | -49.13784 | 2026-07-30 00:13:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e2c2eff-b77d-3f9c-8635-af8fb03079fa | -16.68727 | -49.2357 | 2026-07-30 00:13:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 02937cb6-c1e1-391c-b2f2-5ad9adedb7f0 | -12.61641 | -44.62699 | 2026-07-30 00:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6e42f9ba-033c-328e-8bf4-3f9470b61380 | -14.20634 | -51.9204 | 2026-07-30 00:13:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 041f9e67-38ac-3749-b887-cbb9a7122aab | -16.75338 | -49.38545 | 2026-07-30 00:13:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| aa56dcfe-f120-3126-9258-d30321dd67a3 | -8.00416 | -50.00941 | 2026-07-30 00:16:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 954ffbb0-d3fa-36fe-8680-868a2659d15b | -7.24324 | -46.05687 | 2026-07-30 00:16:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 42ed7cd2-a356-3115-aec3-2e49f252eb6a | -7.70392 | -49.32352 | 2026-07-30 00:16:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d0544290-d175-3e53-bf32-bd3c52b79252 | -7.3759 | -57.19155 | 2026-07-30 00:16:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 08b6982f-96d6-38fc-a7fc-34a30b0fe010 | -9.61859 | -47.7669 | 2026-07-30 00:16:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6bb2499d-03af-3e4b-b8e2-b2e187191bd1 | -9.61686 | -47.75505 | 2026-07-30 00:16:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 0c241950-7f23-3e79-8bb1-112aa35ba473 | -9.60848 | -47.76862 | 2026-07-30 00:16:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f3fe8a9a-e51a-3056-807b-7b076e176ec5 | -9.44741 | -50.30692 | 2026-07-30 00:16:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76023070-8cd0-39f8-818f-8fba7dd4056f | -8.44285 | -51.49915 | 2026-07-30 00:16:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 21ba97af-17fa-36fd-bf36-ec9339203168 | -9.54481 | -49.30642 | 2026-07-30 00:16:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| cb71ccbf-64b7-373b-96fd-1e6b3a8b6d91 | -8.00549 | -50.01889 | 2026-07-30 00:16:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 05faa22e-f60e-3715-a41f-569962451ff9 | -9.55422 | -48.66264 | 2026-07-30 00:16:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e8c2bea4-5003-3983-9ef1-0265bd8b78c0 | -7.58733 | -49.55315 | 2026-07-30 00:16:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 23d9aa98-9cc5-3efd-bd8c-f84c7bdfa717 | -6.59083 | -51.71024 | 2026-07-30 00:16:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3922a58a-0769-3d78-8e46-7a1dd27b1d97 | -9.60673 | -47.75665 | 2026-07-30 00:16:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| cd03c502-cbdf-3311-a23a-d5d56eb25b11 | -6.86208 | -46.00432 | 2026-07-30 00:16:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ff503df0-50e9-3f0d-9839-30fb66ab5035 | -9.4487 | -50.31605 | 2026-07-30 00:16:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dd109a48-e1f4-315c-9e78-8475eacf854c | -9.54339 | -49.29652 | 2026-07-30 00:16:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d07ca892-591a-3bc5-a701-7092d189d258 | -5.76738 | -45.78564 | 2026-07-30 00:16:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 812893c7-e515-3e82-a2f9-bfc7d6ba3126 | -9.55576 | -48.67331 | 2026-07-30 00:16:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c6476eba-2f75-3c44-bd57-43be0adaa96d | -7.2387 | -46.06425 | 2026-07-30 00:16:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 14de8ed0-52bd-3217-8103-1d363fd248dc | -7.19483 | -45.50355 | 2026-07-30 00:16:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| dd8ebf05-b029-3f7e-b537-9f778cf3604e | -6.99583 | -51.30593 | 2026-07-30 00:16:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README2.md)
