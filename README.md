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
| 698ae280-0556-32b8-87bd-961874133ea0 | -18.0004 | -54.2676 | 2026-06-07 00:00:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 61.1 |
| cc73f1ac-e8e7-3ee3-9adf-b6ff21fb0ef6 | -18.0 | -54.2889 | 2026-06-07 00:00:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 54.2 |
| c7d3e072-d9ae-3c6e-a3bd-2dc02b2a3cef | -16.50007 | -43.49615 | 2026-06-07 00:05:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 952c2bb2-32b0-3af2-993c-460258b096c2 | -18.00506 | -54.29839 | 2026-06-07 00:05:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 258607a0-d2a0-37f0-a85c-042aaade28d8 | -18.00247 | -54.27211 | 2026-06-07 00:05:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e882dee4-7999-3a67-8e39-cdec9a65b144 | -16.50183 | -43.50782 | 2026-06-07 00:05:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 4433261d-b87b-3f43-ae66-dfadefde0131 | -10.54162 | -49.46396 | 2026-06-07 00:07:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e550c326-44c4-38a4-8a1f-d080a282d61d | -10.18522 | -52.65466 | 2026-06-07 00:07:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 445bfac8-5026-347d-bd85-0e2d46928393 | -12.41292 | -47.50197 | 2026-06-07 00:07:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b9dcd7d7-5d09-3805-99bf-baf574743bc7 | -9.49792 | -40.31199 | 2026-06-07 00:07:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.7 |
| db9be7c2-eaa5-3693-b53a-20454f085abf | -11.46965 | -47.34422 | 2026-06-07 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 08aa5105-06aa-3739-8330-6473fc3aca8f | -12.06726 | -48.07789 | 2026-06-07 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 2b968eeb-b14d-3e11-93d5-ebd367a48359 | -15.66331 | -43.32175 | 2026-06-07 00:07:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 12.5 |
| ae02b665-b26f-39e5-9ad7-36ae4ef41c17 | -10.89477 | -49.35165 | 2026-06-07 00:07:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d984e2f4-5010-36d9-9582-a9ba3fa68a5f | -12.06958 | -48.42901 | 2026-06-07 00:07:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 927a5133-8621-3935-b3fa-f1ab1d1ebefd | -10.31057 | -48.22633 | 2026-06-07 00:07:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 549ebdf0-eab8-36d2-96c9-05ef17045ef6 | -11.87665 | -43.9003 | 2026-06-07 00:07:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0c151290-ec8d-3312-b3fc-5e38a333f493 | -10.09344 | -47.06581 | 2026-06-07 00:07:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c5fb0e1-3029-3ae8-82f6-9ca83ff3e455 | -15.0547 | -49.46927 | 2026-06-07 00:07:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| d65473fa-6b6b-3a4b-b9ca-a7833e8a39c9 | -13.35936 | -43.21159 | 2026-06-07 00:07:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| df848488-9cbf-38df-a22f-8c2fe772fe7b | -11.00955 | -47.47883 | 2026-06-07 00:07:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4b2c66c6-803d-3545-b65f-fdf7a7002e02 | -12.41168 | -47.493 | 2026-06-07 00:07:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ab88ac08-c178-3b44-8b1e-63044660e889 | -12.49689 | -46.26358 | 2026-06-07 00:07:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f60ec8d7-3bf9-38f2-83ba-f7940d4dd028 | -11.02925 | -44.32229 | 2026-06-07 00:07:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| facc636d-210c-3dd0-bdce-ca3212eb40f8 | -10.10236 | -47.06451 | 2026-06-07 00:07:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34a64c7b-b3a2-394c-a67a-d6e56e5d8034 | -11.55416 | -52.80214 | 2026-06-07 00:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 2b914dae-56c8-3104-9b16-f30fe73c886e | -11.97733 | -47.35844 | 2026-06-07 00:07:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ea5d0ab-b95a-3cc7-851d-a860ddf1090c | -12.05841 | -48.07915 | 2026-06-07 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5b74747f-47cc-3847-8964-077e4e9bccca | -10.60235 | -55.43201 | 2026-06-07 00:07:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f59c14e1-ce75-36fd-95ea-3cac01bcd702 | -11.47848 | -47.3429 | 2026-06-07 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 51d07f7a-7eeb-360c-93e0-edd53d1571db | -8.94434 | -45.67114 | 2026-06-07 00:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 49edf226-79d8-3990-8bc8-9203461c03c5 | -13.08661 | -42.14838 | 2026-06-07 00:07:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e0e0013b-63b4-362f-bac8-6cdf5eaff023 | -9.52604 | -48.68455 | 2026-06-07 00:07:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 26943379-d53a-3bb7-a5cc-2f65a4e51105 | -10.85722 | -53.74263 | 2026-06-07 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cf301ccb-2852-3b0a-bfa4-9e56a2d194e1 | -12.36633 | -47.90005 | 2026-06-07 00:07:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dbc88f0d-9092-37a7-bc7c-6f2efea4f380 | -12.04135 | -45.27832 | 2026-06-07 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ddb86844-c343-3b4a-8d6d-8f4d7a01ff26 | -11.57062 | -48.14285 | 2026-06-07 00:07:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 44b94287-435d-31c6-9aa5-646adae57b11 | -15.05604 | -49.47992 | 2026-06-07 00:07:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 19b0b3b8-cc8d-31ed-95fd-0be6351fa1fd | -16.04375 | -50.55577 | 2026-06-07 00:07:00 | TERRA_M-M | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b745c39-281e-34e3-9788-ebc9aec97ae2 | -9.52726 | -48.69351 | 2026-06-07 00:07:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e6dc0888-5474-38da-902d-833fbf7784e8 | -9.0931 | -50.60562 | 2026-06-07 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c3eaf72b-4168-3a96-849e-853883244c26 | -9.07419 | -50.60819 | 2026-06-07 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cb93face-657a-3a4c-ab87-51f4838bd603 | -7.11798 | -48.13594 | 2026-06-07 00:09:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 53da45b6-d49f-3c98-9213-29bff3ff9166 | -5.80223 | -45.12542 | 2026-06-07 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a374c808-6f08-3e28-bc0c-1c063cc5a6c2 | -5.8126 | -45.12374 | 2026-06-07 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8fc747a4-e690-3912-af00-51a1931a4e94 | -7.56215 | -49.42109 | 2026-06-07 00:09:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65e141c5-cafd-3e0b-b60f-27866f54e1cf | -9.08364 | -50.60688 | 2026-06-07 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d48d1f2c-2cd1-3862-8967-d2f105157f11 | -9.07283 | -50.59788 | 2026-06-07 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c37ea667-916b-39ea-b182-924d4908e1de | -5.95037 | -45.50673 | 2026-06-07 00:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 25100db0-a773-3779-87e8-329f161b4d8e | -7.11674 | -48.12703 | 2026-06-07 00:09:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d6dd930a-9a6f-35d8-886c-67cb6248dc8d | -9.10278 | -49.6458 | 2026-06-07 00:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8aecd07a-24a9-3966-91c0-63e2b09257cb | -5.93856 | -45.4965 | 2026-06-07 00:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 521e44dc-41bb-3984-803c-0dcfb6e9b74c | -8.86314 | -50.19009 | 2026-06-07 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20094155-43d6-3bd9-b4ae-c2187d87d04b | -5.71898 | -45.04112 | 2026-06-07 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a2031da9-205a-3e1b-a183-f5b34b10974a | -5.94029 | -45.50824 | 2026-06-07 00:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 0d7ef90e-7bcf-3350-9d0e-4f000d802ecb | -11.5499 | -52.7867 | 2026-06-07 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 3730c5ca-cfba-3fcc-aeb0-4049df47dfd0 | -18.0 | -54.2889 | 2026-06-07 00:10:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 49.1 |
| adf02570-f5ff-3ae0-94f4-75e4c46050ff | -18.0004 | -54.2676 | 2026-06-07 00:20:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 45424321-25ec-36b8-bb63-8a2ff7c7802e | -18.0 | -54.2889 | 2026-06-07 00:20:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 98bac3cf-d0a1-3418-89bb-533eaecdc328 | -11.5499 | -52.7867 | 2026-06-07 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5dccc9d6-369b-3fee-a2b9-96a450f03bd9 | -14.0784 | -58.9026 | 2026-06-07 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 6c957ef9-55ad-36fa-bba2-8cb7e79105ec | -18.0004 | -54.2676 | 2026-06-07 00:30:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 9dae19b8-bcd1-37d4-8e7e-f15cc9b3df15 | -18.0 | -54.2889 | 2026-06-07 00:30:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 2c37fd82-2479-30f8-ae22-f46f43be258b | -18.0 | -54.2889 | 2026-06-07 00:40:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f5d5e130-8aa9-35bf-8291-3d02205c34a0 | -10.8236 | -60.7633 | 2026-06-07 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 85492510-54df-31ef-b1a2-32a96593f6f5 | -18.0004 | -54.2676 | 2026-06-07 00:40:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 6734c389-bd1c-30f6-a5d0-fff708f53ce5 | -11.5499 | -52.7867 | 2026-06-07 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d4cb7f5e-b846-3d32-afdc-e9556b8e17d8 | -11.5499 | -52.7867 | 2026-06-07 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 747a50fb-cfaa-3c36-8dd5-ad4f7a7d4d85 | -18.0 | -54.2889 | 2026-06-07 00:50:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 50.7 |
| ff4efe04-3b7e-3e75-b4c6-0902663b39b8 | -11.5686 | -52.8057 | 2026-06-07 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 798e0e40-1616-3596-aa32-fc9f2a02eb0d | -11.5688 | -52.7848 | 2026-06-07 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 06ba17f7-a3b0-3e79-a4ac-f433e86fa091 | -11.5496 | -52.8076 | 2026-06-07 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 58f79949-65da-3073-b175-2bf19368e808 | -11.5499 | -52.7867 | 2026-06-07 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fdb6b14d-f124-3ff4-9344-4c9bd44095af | -17.996599 | -54.279701 | 2026-06-07 01:06:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f99876a8-8666-3bb0-868f-f9a15c7085df | -11.5407 | -52.782299 | 2026-06-07 01:06:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f27ac13e-076a-3793-ae89-1dc1fd6f803a | -10.5922 | -55.4203 | 2026-06-07 01:06:00 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3927f456-7d18-3111-a321-71e1446c4450 | -11.5557 | -52.8004 | 2026-06-07 01:06:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ccf7df2-3d4d-38a2-a5d3-6ff2eb9c83a7 | -18.006201 | -54.277 | 2026-06-07 01:06:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 071f513b-f75d-3c12-8718-7ba353020208 | -21.9914 | -57.610001 | 2026-06-07 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 558a3bef-9230-3a90-b907-361fc33a3061 | -11.5461 | -52.803001 | 2026-06-07 01:06:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11375c2e-4e2e-3f01-89a8-d66e3a1666f7 | -14.0725 | -58.904701 | 2026-06-07 01:06:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 68d0ce14-9728-30ce-b9ab-23a7c7eb5a76 | -11.5503 | -52.779701 | 2026-06-07 01:06:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43547d1c-78fb-3746-aaf4-c2be0653cb99 | -21.989599 | -57.602001 | 2026-06-07 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4f02be4b-8ba4-33d5-b322-bc694302280b | -14.0785 | -58.886101 | 2026-06-07 01:06:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fdec8481-754b-367a-b8ee-71fd74b6580c | -10.8341 | -60.749699 | 2026-06-07 01:06:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1de1a3c0-c02f-38b4-ad18-b026a5dbd473 | -10.8358 | -60.757099 | 2026-06-07 01:06:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c44a07a1-5af4-3ba1-b927-4744de2c1b81 | -14.0804 | -58.894299 | 2026-06-07 01:06:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0f218c3-5bc9-3385-b87a-58ed5c267ead | -17.993299 | -54.266701 | 2026-06-07 01:06:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bcc242a9-235b-3422-bedc-18be9b1caf70 | -14.0707 | -58.896702 | 2026-06-07 01:06:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1071536f-fb3b-3bb1-9f08-7048eb5f01d9 | -10.8375 | -60.7644 | 2026-06-07 01:06:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf303b24-e694-3e2e-a6c4-4b952c086cad | -11.5499 | -52.7867 | 2026-06-07 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d76ef115-b9e0-3263-8519-52bd8abeb937 | -11.5688 | -52.7848 | 2026-06-07 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| a8b8c091-530e-3f74-bdb1-4a2d182fa5ea | -11.5496 | -52.8076 | 2026-06-07 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| a840fe0c-1430-3b06-b24e-a2b8e9baca8b | -11.5499 | -52.7867 | 2026-06-07 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 09adc47c-c3ea-35f3-be01-8a026dcf2130 | -11.5496 | -52.8076 | 2026-06-07 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a68ef083-cd8e-3b66-a648-301fffbc4918 | -11.5496 | -52.8076 | 2026-06-07 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 60e0ece5-c76c-3b88-b40d-b1a2a7fe3ab9 | -11.5499 | -52.7867 | 2026-06-07 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 06c52be9-ae0a-303e-ad83-584c4b294ab4 | -11.5499 | -52.7867 | 2026-06-07 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3fca6965-9b30-3337-81e6-4b09bb4d4e64 | -7.81337 | -72.79952 | 2026-06-07 01:47:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5367cdb8-e5df-30d8-989a-2cea98700831 | -14.0784 | -58.9026 | 2026-06-07 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |


[Clique aqui para ver as próximas entradas](README2.md)
