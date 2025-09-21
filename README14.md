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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7ad6c1e-3c29-3caa-a9c4-6b8988c09b63 | -14.47264 | -46.50163 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0bce47c-7841-3bc3-b662-2365160e8223 | -15.69079 | -46.98793 | 2025-09-21 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 72b4aa26-b8fd-311c-ae38-2c2233f0f7ac | -12.71814 | -46.84129 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3b390a8-d345-38ea-895a-bf350f49a8b7 | -11.29795 | -47.49846 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bfd713a-6a9e-3c57-bf81-1b78c9ce5624 | -12.72186 | -46.84185 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| deacb9f5-2da5-3167-8f0a-8842eb018d8c | -13.77498 | -43.70578 | 2025-09-21 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c832259c-5d85-36b1-ba3b-acd6bdcd44ae | -12.07015 | -44.82239 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53da38ea-23b1-3208-b977-ae92c6289845 | -17.6277 | -46.43459 | 2025-09-21 04:10:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c7b8e3a-0682-3fd6-a166-cefe4c648094 | -12.72953 | -42.90894 | 2025-09-21 04:10:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 608b9737-f5bc-3079-9313-a16a00f9e333 | -14.45478 | -46.50361 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8e7e593-8de3-32b0-ade9-6286d2b347f7 | -19.23079 | -43.76535 | 2025-09-21 04:10:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe1ed1f1-d66e-3aff-87ac-19570df6868d | -13.62698 | -47.42055 | 2025-09-21 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd945e39-df01-3e3b-9015-4f6a8dc0204d | -17.34103 | -46.82404 | 2025-09-21 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd98c8f9-9740-37ad-b764-b2552addc53b | -17.44897 | -44.81022 | 2025-09-21 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5906a1ef-dbac-3e4c-9062-0b10ab42439e | -11.27694 | -47.47977 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d01f7206-42e8-387e-b29b-f0e68477ae88 | -12.7263 | -46.83813 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82ed6b1e-38c6-3869-82bf-a502e79f4c88 | -12.07294 | -44.82672 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1f841b2-4c1b-3aa2-b5df-edd50a1273dc | -11.30011 | -47.41581 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 39ee0b28-c79c-3f3b-ad4c-e71a4254a82a | -12.71667 | -46.84991 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dcde0b6-a735-35f6-a0fc-afd9d2e63978 | -14.74369 | -44.33512 | 2025-09-21 04:10:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 143a0f56-ae25-3c4d-9e42-4fdab10adbe5 | -14.80723 | -51.38178 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f35dc782-ceba-384b-a3b9-e99a175e10c9 | -14.54509 | -45.53152 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ffec78a-6591-376f-abe0-80cad17fa506 | -12.70627 | -46.84387 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8851ed4-4cd1-3200-890c-a250d4ac8ac4 | -16.60609 | -43.6797 | 2025-09-21 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daaea9ce-7e79-3bdd-8c5d-fda374d14c16 | -14.45335 | -46.51214 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 216514a0-94ec-3772-aa14-f9b2493ace4f | -15.36014 | -43.71027 | 2025-09-21 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 818d84ea-4bbd-3b52-b6ee-a6dcc56d94cb | -11.28622 | -47.40312 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8b6e2223-db61-3cf1-a84b-fb20555f29aa | -12.71443 | -46.84072 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b31cb7e-799a-367e-8e87-b3f2b0381521 | -14.52463 | -44.86767 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f667b841-5201-3765-855b-c4f473ac6cb0 | -13.31263 | -47.27942 | 2025-09-21 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c822461-a702-3874-b1f6-ab6c119e8e47 | -18.36655 | -43.70521 | 2025-09-21 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6376d7d9-af28-3e95-afa8-bfc0a5373c11 | -13.38754 | -43.59411 | 2025-09-21 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b75df2e6-bbad-3739-a4a5-3a2e874fe0d6 | -12.35108 | -43.75663 | 2025-09-21 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2d3939f-110a-3608-a539-7a824ecaf59a | -12.13513 | -44.29485 | 2025-09-21 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e393ede4-d10b-3dbb-ba6e-b965059d5a55 | -12.42318 | -45.11354 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be5e7e85-84bd-3624-b9c4-416c2082203f | -14.45833 | -46.50428 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9323067e-5f88-33fd-bdc0-410d5c45c8f6 | -11.61186 | -50.60069 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af0e746a-664e-3438-9aeb-babe39ec1678 | -12.08965 | -44.81005 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea61054e-4d4a-3a87-a0fb-4738335d73f6 | -15.7278 | -49.55858 | 2025-09-21 04:10:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad9539d6-ea64-3a1e-abc2-0c659b947009 | -12.8995 | -46.76768 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2c3374e-bac4-3a4f-bf95-007ba1607e46 | -13.68302 | -43.81343 | 2025-09-21 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3ca6bbf-0ddd-3f1b-b36c-bc728f9ee9af | -19.63752 | -43.72613 | 2025-09-21 04:10:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 612da392-9d41-339e-8f7f-efc8613f9ed2 | -14.20838 | -44.6601 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4412d5f3-ee4f-3144-9caf-3b7b346768d0 | -11.61957 | -50.58567 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0838eaae-70e6-3ba1-bf29-470eda7e0da3 | -14.43837 | -47.57008 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d25c14c-7c09-3852-bf78-37e77e52194b | -14.21173 | -44.66066 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1ff8f55-37c8-343b-8b77-708adacaf065 | -17.16861 | -46.83558 | 2025-09-21 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eab383eb-1dcd-3fd5-9d63-5296283ca066 | -11.30188 | -47.49913 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13673f62-f61b-3b7c-89f2-7c1ea1ac2f2c | -11.60707 | -50.59979 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54272299-4b5a-37fe-bc48-3ce201819968 | -12.72263 | -46.8597 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6523a0a-cce4-3f9e-918f-f31c4789ef27 | -15.90759 | -43.04988 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ec4697d-6e56-33b4-9a27-a618d77d369a | -18.89987 | -44.2823 | 2025-09-21 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea0c1e6d-ccde-3a0e-96cd-d1c0ef872d07 | -12.08908 | -44.85658 | 2025-09-21 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d599431e-b397-363b-921c-f11cd976e2b4 | -12.07512 | -44.83484 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac086cc0-86a8-3c34-8e9e-9c4eee615975 | -12.72113 | -46.84615 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f6f0ec3-5ea5-3a74-89c5-ac8165be53c6 | -11.26976 | -47.40528 | 2025-09-21 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3da1c463-3422-3ee6-bb25-dcf4ca4cff5d | -13.64911 | -45.6947 | 2025-09-21 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4037237a-aa9a-34dd-a83a-6a7179c0f882 | -12.70998 | -46.84446 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1028a0e0-e8e7-3193-aff8-7357def9ec84 | -13.5386 | -43.00098 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 3b3ac6cf-deae-352b-8fc2-516e2f173e18 | -12.91493 | -46.76603 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de2e554f-37c2-3272-be0a-bf296dc42230 | -14.81673 | -51.38368 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d233fe1-753f-37ba-bae4-030c8816bec7 | -12.12174 | -44.78445 | 2025-09-21 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8004323a-cddd-36ad-a868-c9ab7471e19c | -14.45982 | -46.51222 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b236596a-8552-3005-b009-9870790623ed | -18.97928 | -41.09639 | 2025-09-21 04:10:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8de0b7f1-dae1-37d9-910c-ea20cb144a8f | -12.08748 | -44.80191 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88b34d7e-c48c-366f-b838-bca3cc68a1a8 | -14.74307 | -49.18874 | 2025-09-21 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 661ce08a-6cca-3a67-803a-c44e635f6379 | -17.11662 | -45.93167 | 2025-09-21 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d205519-9d15-3d07-8167-35e1e3015f2a | -14.62664 | -48.26971 | 2025-09-21 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 115b91f7-fb7f-3c5c-8c12-2cd7024f3c22 | -11.52418 | -48.55228 | 2025-09-21 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5ad681a-1de2-3bec-b666-e7e6d4c138ba | -14.45775 | -46.50297 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 760c5103-11c3-3c55-b177-8a0d4427997a | -12.48363 | -46.69308 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36a65557-35e0-3277-ab5c-0c300f847bf6 | -16.21151 | -46.69038 | 2025-09-21 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 879ade14-0762-3a95-b79f-fac0484c413a | -12.48286 | -46.69754 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea690cd3-0a46-30a8-b621-ccaf12802b25 | -17.06818 | -43.28277 | 2025-09-21 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37070a49-c114-3f4a-87b8-68ba553c859f | -14.78869 | -51.37474 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6d1646f-cf74-3163-8cb7-a1a45e91e8cf | -12.81093 | -46.86905 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8cb2dd1-a505-30f3-a828-a539684cb3e3 | -12.42192 | -45.12119 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f86b1fed-d641-311b-a779-cdd621840161 | -11.30885 | -47.50565 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80d0f65d-2ccc-39b8-82f1-1e3f98009519 | -11.29705 | -47.41022 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 12bd2ac0-7bf9-3de8-87dd-8c94507ca02a | -13.52395 | -42.56671 | 2025-09-21 04:10:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 21c26ff4-f837-35fc-8c71-9d6c54e557ae | -14.97934 | -44.41565 | 2025-09-21 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 472e5269-05ee-31b1-97c7-e005533516dc | -12.08567 | -44.856 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bead26cc-6b26-37b4-840b-27163607c60d | -15.48758 | -41.91819 | 2025-09-21 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e199dac2-5228-3b84-becf-e6e1b3f43a86 | -17.53721 | -42.3212 | 2025-09-21 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bc7dec1-d213-3962-a667-01216b8bf39c | -14.56501 | -46.17165 | 2025-09-21 04:10:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf164efc-6844-3ffb-b922-980c45ec9f3b | -13.5408 | -43.00857 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c3cc30bb-a850-30b7-b4db-e835b0f59da3 | -12.89873 | -46.77215 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d651850-9a39-32af-8c79-d40965c12a06 | -12.96222 | -46.38163 | 2025-09-21 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fd01765-6428-37f3-a769-163693b6f2ff | -12.4962 | -46.68612 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6134fab8-bef4-3ba5-84e5-2548d7c5593e | -18.46313 | -47.2408 | 2025-09-21 04:10:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3111cd94-a50f-3046-9721-ed40ea170dfd | -12.38915 | -45.83936 | 2025-09-21 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fd1d61a-a6d4-3cd4-8980-daeb444886ea | -13.53805 | -43.00451 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 398bebc9-3186-3551-b2f5-429dea5c0419 | -12.71741 | -46.84559 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3f5e0be4-966d-3a80-9dac-82d2b8e7e17a | -13.40321 | -44.39105 | 2025-09-21 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c96ad5e2-30a0-3f8a-bf83-669573f867f6 | -14.43711 | -46.52158 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4af2e41f-a11d-3ff3-82f9-fece6c1e233d | -18.87687 | -43.34362 | 2025-09-21 04:10:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2651805c-bd75-3ff5-9aed-accb3279b004 | -12.7204 | -46.85044 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa4c1d95-b654-3151-95b8-bfbaf8699919 | -12.47627 | -46.69176 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 723ad1f1-4d23-3f18-a2c5-335649e16073 | -12.71072 | -46.84012 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1267798d-789b-3f8b-99e5-b87f0605f7fd | -13.36621 | -44.28507 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
