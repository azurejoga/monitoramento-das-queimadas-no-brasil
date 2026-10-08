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

## Dados Diários - Página 339

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9e6069b-9c22-3bcd-b921-06f827e01b8b | -11.2405 | -45.24331 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e60e68f8-88dd-397b-80c4-ade0ee6b86ed | -8.9968 | -42.3388 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| fceb0800-0cd0-3943-8629-11b6b0b5b23a | -7.34521 | -50.8302 | 2026-10-08 16:37:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0b93a67-a8d7-3512-81d3-8348b6369885 | -9.89164 | -44.85236 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8fc95158-292d-3005-b999-93fb86b6e64f | -9.13613 | -45.83914 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf4cb38d-3622-3896-9a68-4cc6e66a0b37 | -10.8642 | -45.55976 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 04c61d88-4408-3a3b-b224-4a5f5d0d85cd | -8.59422 | -44.86889 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eb4b3004-632b-3561-84bf-f8ea3bab9f94 | -8.61067 | -45.63999 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9bdff34f-f400-3db8-a054-65524e154a75 | -13.22393 | -54.49977 | 2026-10-08 16:37:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7e79caaf-ca3f-3b9e-afca-27efa683e3c8 | -10.53565 | -47.26836 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e6a37e8e-a292-36d0-9786-cd17bd5eaeea | -7.69922 | -45.4483 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 2fa44241-7478-3ec5-a4f3-c0cb3949cd5f | -9.81571 | -45.69077 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 977e96ad-ad50-30d3-baf2-1100f3e04b99 | -10.76049 | -46.61079 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 466d6bfc-8646-3aed-87be-a0793b9e92cf | -11.38795 | -54.04446 | 2026-10-08 16:37:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 301fa512-6bd7-3bd6-8cba-c66e51d1ad32 | -6.54098 | -45.39938 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| da8130a1-1fd3-3953-babf-a05d9414d7b9 | -10.36823 | -44.24596 | 2026-10-08 16:37:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e434fca7-46b2-383c-b28c-50c3869d11b4 | -12.17975 | -44.81504 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fd825a9d-8edd-3b3b-a3a8-82e0e5149460 | -11.41054 | -47.57367 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7234a9a4-4ade-35b3-a4b7-9cd6f49f3711 | -11.16922 | -49.47736 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 79e9ad69-d896-35ba-82d3-3b97595f5037 | -6.85021 | -41.75366 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 152303bd-a8f0-3842-9471-36434b5135e7 | -8.95907 | -45.1215 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7da199bf-265f-36d7-9932-86399fc1c4eb | -8.2066 | -46.42334 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 69bf4fe3-43ad-39c6-9dfc-5f61b7a071b3 | -8.3992 | -46.91593 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56952cae-24f0-3fb2-b2eb-76c32e123aea | -6.6882 | -45.29729 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d65038d0-7c43-32d7-82cb-0599239239e1 | -10.52506 | -57.75721 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 792326d3-cf56-372d-9033-51aef9f2a3b6 | -8.07637 | -45.60795 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7fa8a04d-235c-349b-9559-8dfdf2cc4b35 | -11.76027 | -45.49726 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 103a8f65-82cd-3203-bb57-4c5beefb6393 | -11.11525 | -44.00672 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 2f9c6670-b320-3a62-865e-1437c1728137 | -9.81518 | -45.68726 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 41e37d98-2c4c-3585-9204-9fea04f70246 | -6.32145 | -35.1529 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1adf130a-125c-3537-9d37-1fbb242816e0 | -8.0395 | -49.40202 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eb58135f-a074-3fdf-8567-d6817ccf3464 | -14.4094 | -52.87847 | 2026-10-08 16:37:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca07c40f-a94a-3fd5-bb3b-80219776f2f7 | -10.43438 | -47.29189 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 228b38aa-14c3-3952-b6cf-bb1acb93fe84 | -10.84705 | -47.94411 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1f1f32cf-3da2-37a9-9de4-4e4a787a1969 | -9.08957 | -47.58361 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5dcbd522-54bb-3385-b5cc-8aeea9f5cddf | -9.84109 | -47.8511 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a76b430b-7909-3b53-a870-8aa82515afaf | -6.88441 | -38.54982 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 52757696-c842-3445-81bb-79de688c5ccb | -13.1352 | -46.32996 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9acc2460-db2f-3f9b-98c4-08232b197872 | -7.83769 | -45.51142 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f9319021-a0b9-3835-a4a2-46c7cf87aff5 | -10.25152 | -49.66252 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5732e9e0-0dfa-3247-8ee9-9498306e6ebf | -6.06684 | -44.10381 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ba1caabb-c106-35b1-a871-6887a11001d0 | -19.07774 | -48.64565 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c9284eb7-3230-307a-91fd-fafc7e9db8bd | -10.07292 | -46.00378 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ccbe87ca-5377-3aa8-a2ad-e2863d623909 | -6.53393 | -45.37555 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b68caa11-13be-36ff-bced-43d6cda0e69d | -6.50346 | -44.2086 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcee7a10-6f49-3e1e-8d65-50c0b81f5923 | -5.74429 | -41.72263 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 3db4eda9-2b8c-3c10-bbb9-1ef105356db6 | -12.935 | -48.61879 | 2026-10-08 16:37:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1c7208ba-0f00-31ec-95c4-1deac96bf84e | -6.29324 | -43.87235 | 2026-10-08 16:37:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| bca6b35a-a2fa-3622-8ecf-4f42db150e16 | -11.96995 | -39.04148 | 2026-10-08 16:37:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2aeced0e-31da-3593-a870-688eba7ca98c | -6.52719 | -45.39794 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 014998d7-af9a-3e8c-9fa1-70ef9da8cbbc | -18.98324 | -44.46078 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 659ac1fd-23fb-3bb6-8273-74320de28c7d | -7.76243 | -54.94434 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 205fde00-b193-37d1-b2bc-a87c9738bf7e | -8.88994 | -45.60312 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7850e012-9900-38d7-8f91-3afb78fca686 | -11.21883 | -41.57598 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9a4036e3-d8c3-323a-971e-be61b245973e | -6.57722 | -44.863 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 136505d3-d9ac-30e8-8ded-dbbef069b85b | -12.19378 | -48.41877 | 2026-10-08 16:37:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 21d39e67-869e-33cf-9d2c-596c15140979 | -8.71067 | -37.91082 | 2026-10-08 16:37:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 598fd74f-1f82-31a8-9096-905ede96648e | -7.77793 | -43.81911 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 824fdc59-3952-3741-b85b-e22034828da6 | -8.51261 | -35.94178 | 2026-10-08 16:37:00 | NOAA-20 | AGRESTINA | PERNAMBUCO | Brasil | 2600302 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fe3ef21f-f4b7-335a-a17f-f41e7649d450 | -7.2805 | -47.25395 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d62ab31d-390a-3877-a721-d34eaae07c42 | -11.64221 | -43.70434 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| e71b12fb-4694-3557-9ee8-e2d683bb16d9 | -5.99339 | -40.94246 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 9ff6e20e-52a9-33be-b350-6a12dbcdbb27 | -11.72683 | -43.63861 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| d1362b64-e02a-33b1-97c9-d82fd2d3c717 | -9.45895 | -44.62157 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f870753f-498e-37f2-a0ab-f28339b1cd03 | -9.70771 | -45.69367 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 2541d9d0-198f-3bf9-b380-cdeec6aff34e | -9.01413 | -45.12717 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bb4fd39-1283-3410-ba09-01f55fd28f81 | -6.16849 | -44.8522 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7c85a5b3-c6e7-3fed-819c-ce4ee84034ae | -9.8006 | -47.82014 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a5d9f4b1-e32f-3896-b120-b6df2c647604 | -6.43026 | -43.82802 | 2026-10-08 16:37:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 72b68186-8997-38f9-8b09-143a88d211a0 | -17.33901 | -41.38425 | 2026-10-08 16:37:00 | NOAA-20 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| eeb49d81-700b-3346-b9df-4501dcf580b3 | -8.95666 | -37.82418 | 2026-10-08 16:37:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 161621eb-0b9b-38f1-a582-8e40c9eb5c5e | -9.50814 | -46.84702 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 162c9d3d-119c-38cc-a2e3-f4522824dca7 | -6.35829 | -42.91244 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9461cfec-57c8-3866-afab-9fa5c66b0d18 | -8.88716 | -45.60711 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2c6ac176-1bb6-3dd1-8ce7-b7e18d049e00 | -13.69646 | -49.08436 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b3fdefe4-6078-3ca6-ad82-a64eb456ddf9 | -6.88444 | -43.6895 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 19ef3a57-80aa-37f3-b122-ce0a992744e0 | -8.27579 | -46.90881 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d4fd1923-262a-38ff-a1d0-16e71b827201 | -11.77119 | -45.52473 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0cb9b6a1-ecac-3fa8-bb52-5aa5bd471df7 | -7.94535 | -50.95984 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6e8eadfb-30f4-387e-b13e-712a9c9dec22 | -8.29949 | -45.73603 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b519ff63-682f-3f66-86e9-20339186e204 | -8.53931 | -46.92052 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c44262b9-481c-3e5b-b810-7c1fb38de632 | -11.00502 | -47.97085 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0be9fae4-0235-302e-81e4-32dd2083e22c | -7.11957 | -40.56278 | 2026-10-08 16:37:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 22706b8c-ee22-3789-88f6-cf84acdfb882 | -10.22394 | -58.02773 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cd4604ce-0650-375a-b4ea-beecc1779c66 | -7.22228 | -44.27625 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 749fe640-c515-3a78-97d3-856d0a5565da | -13.18935 | -47.86279 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 41755ac4-e9dc-317a-bc47-cc31547b722b | -11.77584 | -45.57853 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| eb855241-0855-3a34-af37-2e72e0a7ef95 | -9.8458 | -47.85869 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 959c0c5d-c265-3db1-aec8-9ea3a2f9041a | -5.89332 | -43.42575 | 2026-10-08 16:37:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ce0c11c-3c54-34e7-b121-85434c9beca7 | -12.15802 | -42.26562 | 2026-10-08 16:37:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 56bb76cf-85c5-3499-a7d0-cbc7af4c2952 | -5.75117 | -41.64203 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| bf38d6bb-1cd6-38fd-bbbe-1fed4c5d1027 | -6.31531 | -45.05673 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0de853f9-0b91-3512-aeb7-a770a415bd9a | -12.18306 | -44.81452 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5714f042-c7b8-3d42-88e7-8f7d19ee4d51 | -13.70042 | -49.0838 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4c9fe2d3-ee94-3ad5-8e10-8c8e73cfd367 | -6.45437 | -46.00933 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4c652218-bb78-3a68-a9ea-08149b506028 | -8.58759 | -44.86995 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0a7e7a54-f404-3024-a167-92b20dfb676b | -6.96804 | -45.26307 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5dbd6faf-a15a-3047-908e-87b7076b7eee | -20.58338 | -48.45959 | 2026-10-08 16:37:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 67ffc581-0b90-37fc-ac60-4cead5ed9ed4 | -9.36544 | -45.94238 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 69881890-cab4-33e0-bbbb-a3d38376e899 | -11.82717 | -47.30924 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README340.md)
