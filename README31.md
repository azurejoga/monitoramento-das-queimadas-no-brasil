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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 824b03f5-f978-30a1-8be2-993cea884ac9 | -13.1725 | -54.348701 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51fde806-4a51-3fe8-ba03-7481c760f99a | -3.4834 | -50.503201 | 2026-10-09 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c207dfd5-aa67-3e55-8795-b165b6cddb39 | -13.4979 | -44.367001 | 2026-10-09 00:28:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f7030612-4420-3dd3-88ed-1494fbd0a6d7 | -3.0225 | -54.241798 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2339d09-04bd-3b79-a62c-afa76b2fdb6b | -15.3417 | -42.769299 | 2026-10-09 00:28:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 445941ac-227e-319f-848c-9ab18110df14 | -7.6009 | -42.392601 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19189fe9-2552-3308-acd3-182ade0f1133 | -3.0166 | -54.079201 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff5908f-5cd3-39eb-875f-15c4e6273e20 | -18.0495 | -44.568401 | 2026-10-09 00:28:00 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 065a4c26-ee84-3c5e-875a-baa25e54de82 | -2.0843 | -46.580898 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caba7050-3790-315d-b678-ce4e58e1364e | -3.3511 | -50.4175 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2a27997-e539-3900-aa25-9a2d517e1399 | -13.1575 | -54.375599 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd0e1989-612d-371e-8f14-98167ca506bd | -9.1306 | -45.834 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 488a29fc-9441-3fe5-8993-2fcd8c9d3d5c | -3.4276 | -54.5481 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be2eb8d6-0cc7-3fb7-bf32-c2d900beeb81 | -3.1804 | -49.255402 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ab30bc-37bd-3725-bd4b-4ffb63fa1771 | -9.2646 | -47.4431 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6244cdd-c233-3e54-9ceb-f73d365367a1 | -6.4036 | -55.191002 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d30e7b6f-a23c-3cc1-b7b2-72530673ac7d | -13.5403 | -43.8255 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c19a9f88-dff1-3440-8008-2791afbe5755 | -7.2439 | -48.065399 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ccd03fd-0716-3989-aa32-42623cb32f6c | -9.7882 | -44.782299 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de3dea4b-6902-3ffd-bf74-84ec4a56b2ad | -11.7614 | -43.536499 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb5677e-93c4-3914-813d-1afc6d016085 | -7.5634 | -46.693001 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbe9e3d2-c406-35cf-83b5-21f0ea05301e | -14.4328 | -43.9422 | 2026-10-09 00:28:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 68224f27-bddc-3a4d-83e9-f363ff5148c3 | -2.3792 | -48.226501 | 2026-10-09 00:28:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec04bd7-a0fe-319b-94f9-22429c7ec592 | -10.0246 | -48.048901 | 2026-10-09 00:28:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c53fc098-b836-32a3-ba2a-0cdb11e1980a | -5.515 | -42.826801 | 2026-10-09 00:28:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93f5cee7-e911-3d59-8a25-c5f7809a1653 | -8.5936 | -49.5294 | 2026-10-09 00:28:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05518e41-08eb-33f1-bc23-8f33f34ea926 | -17.365299 | -48.183201 | 2026-10-09 00:28:00 | METOP-C | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f175ea20-c96d-3161-927b-10a6fa444b8e | -9.9084 | -44.856701 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7b584d-8b16-33d2-87ef-4be0d71c1958 | -3.0 | -54.050598 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 633bdbe4-2ae9-3813-aa34-9862adea7367 | -10.8771 | -44.809601 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba2c3ea3-dcef-3218-920f-8587570d1011 | -3.1092 | -54.173401 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c5ab2f-313c-3178-87b2-80b1be8fbdf7 | -15.3434 | -42.776501 | 2026-10-09 00:28:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd295d90-20a9-366a-b8ea-d49b53f3500e | -11.0576 | -44.064899 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3609f841-57e0-3d40-acea-e17853c1e204 | -3.1053 | -53.790901 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb68ff97-eeca-3665-8f00-417d8bb3dacf | -5.3518 | -45.181702 | 2026-10-09 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22111dcd-2745-3e1f-9869-19ac3fa766a3 | -2.8253 | -54.1371 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fb4230-5d6f-3059-94bb-44fc87a10672 | -7.1966 | -55.159599 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea47fe2-3450-335c-9207-9f74a3fe3c0c | -4.7948 | -45.764 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 146de0c2-d547-3eea-898d-7fa4b86b8d63 | -5.0867 | -46.136902 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e96065c-24f1-382e-9474-475b25f17bfa | -2.4942 | -56.065102 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd476f55-8613-3aef-a58d-85b44162bccf | -6.9938 | -47.683998 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 669a24ce-d340-3f06-a5da-8bd670c5ca52 | -8.9719 | -45.9063 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09045d62-ec6a-36f1-b75b-b1be0829f41a | -5.6124 | -44.836102 | 2026-10-09 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7c5712f-09a3-317f-98f6-632050593c66 | -11.8447 | -43.584301 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7fa65f1-f964-3051-ba84-c9dc4960ff18 | -4.6122 | -49.216499 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f86a227-0c6f-3613-aa87-b231a66f37d6 | -11.626 | -43.710098 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65454e19-b9d7-3c3f-abbc-3fc01f066cd8 | -9.8539 | -47.458302 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d56efbcc-5fc7-393a-b1bc-53cc74bdfa28 | -18.0882 | -42.277599 | 2026-10-09 00:28:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e4374a07-72b3-3c96-b0ef-af28b9138f12 | -7.1868 | -44.283001 | 2026-10-09 00:28:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c18bb3f-e04d-3391-8795-174a053f798f | -6.3835 | -45.945801 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 917a752e-d2ec-3f8c-b524-a4d58a8b6b3c | -11.7841 | -45.588501 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbfd205f-de64-365d-988a-f2da36390f86 | -6.151 | -47.917301 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6fa75a2-9e9a-343d-9e77-d4be4d390e9f | -1.1469 | -54.2206 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db4f8d19-202a-3d55-8f4d-707ed618f79e | -2.9888 | -53.909901 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9d2b54-8706-3801-902d-2d7f435f55d9 | -14.9699 | -47.549999 | 2026-10-09 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f36c895-b0c4-31d9-bde2-e5b10a9ce522 | -4.6578 | -48.962502 | 2026-10-09 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5585447b-6995-3efc-9808-73e118986d1e | -2.4892 | -56.088001 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7225889-9844-3559-b1ce-40cc457fe7d1 | -10.7032 | -44.499199 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14c3ce64-f421-3332-b536-0bf4d22168bc | -11.794 | -46.795601 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8340e36c-2674-3c9e-b792-3fab505c3e74 | -11.3979 | -46.6768 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fae336a7-2716-3d63-b13c-c95483fd35e1 | -9.2907 | -47.421299 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d3235cf-2c2b-313c-b5e9-39e9c473a82e | -4.6202 | -49.206299 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6ecde84-5034-3680-b1bd-8af95197ce94 | -11.5836 | -43.6604 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76d74895-7766-3b5a-a07c-717057b1e3f1 | -9.8671 | -47.471699 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c10e715f-4340-3fb6-8490-12efbd06feef | -4.2664 | -46.2924 | 2026-10-09 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd4f099-b99f-305c-b889-243ee668c5a1 | -2.8169 | -51.2817 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f4f9ba-c90c-3b90-b22a-38f033becf38 | -2.9297 | -54.1469 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a34a3f7b-a57c-3380-8834-44f64157bdb4 | -13.7258 | -43.870899 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b52161b5-1b4c-370a-a263-f37470946622 | -5.2639 | -50.1525 | 2026-10-09 00:28:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7599ae5a-f7f9-3e62-bc38-e75c59525e4d | -11.1412 | -54.8116 | 2026-10-09 00:28:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f89d9de6-2dec-3c8a-8f58-e8ce0016b8a8 | 3.532 | -51.248901 | 2026-10-09 00:28:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 204865af-4552-34bf-a66b-15895e1c2a0a | -14.9582 | -47.543201 | 2026-10-09 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 945de0b7-504f-3db1-b1e8-d06171b4b7f1 | -3.1128 | -54.189098 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4918e4-1923-370e-a743-4a885c5787b5 | -8.3302 | -45.0355 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9291d3f-0dc4-368a-9a39-f271cf635d65 | -3.0069 | -54.081402 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91abe49b-c62b-3499-a9a8-d036b38d2861 | -7.1078 | -42.534401 | 2026-10-09 00:28:00 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fefce040-0e60-3ae7-b318-a999e85df0f6 | -4.6254 | -50.970901 | 2026-10-09 00:28:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff2165f4-460e-37d6-89c0-fb927e5dafda | 2.4259 | -50.817001 | 2026-10-09 00:28:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e8c85c51-5858-3de0-a078-79756dea5edf | -15.5597 | -44.514999 | 2026-10-09 00:28:00 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 54bdafe4-264c-3620-87e9-83c98cda4761 | -3.5397 | -54.6852 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd44f43c-b8a9-375d-9c47-709f8ff93b9c | -12.0388 | -43.441299 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1276ca59-6f9b-3b0e-b3ec-eee714661a86 | -16.5847 | -46.7565 | 2026-10-09 00:28:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5fc67622-8961-318c-9bfd-566c44bbf404 | -7.377 | -44.035801 | 2026-10-09 00:28:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 66bee821-3f4b-3c24-a4a7-8119314ff559 | -3.103 | -54.1912 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591af74b-de5b-376b-9a1e-5e6eb0d4b826 | -14.5504 | -50.040699 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95fa2692-b02d-3178-9725-1e7f524d694e | -5.1887 | -46.221699 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0bfeb305-5310-3cee-8b8d-9601605992a1 | -4.944 | -49.411701 | 2026-10-09 00:28:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e33c2a4-5d99-364e-924f-7291c93839b8 | -11.885 | -47.402 | 2026-10-09 00:28:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 683f1a26-38f0-385e-b575-7f2104338360 | -9.2727 | -47.4333 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75fb92eb-0145-3f5f-a4aa-b25c700493ed | -11.0722 | -44.083599 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd9870f1-5e01-35aa-92ae-c9df9a11f912 | -12.0045 | -43.471901 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdae3dd4-ccf9-3d03-b2fe-851502d24155 | -8.3032 | -45.729599 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3899e353-9831-389d-a545-d99473de013f | -15.4645 | -45.442402 | 2026-10-09 00:28:00 | METOP-C | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8fceb0b5-388b-3136-870b-8322d661d9ee | -2.9776 | -54.0877 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a074cfe3-6b0d-391e-9bb0-fcf3c0af8a49 | -7.2677 | -45.3494 | 2026-10-09 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1973d692-692a-3192-9c23-4f98e2800db5 | -5.0679 | -48.408798 | 2026-10-09 00:28:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5630bf87-cf19-3acc-b2b5-680f8c73bc6c | -5.9753 | -55.367802 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e65bd05-b3cc-3807-8b52-62a7a5fb98e6 | -13.3689 | -43.887901 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7092270-14af-37e5-bd93-8078b5703082 | -4.0822 | -48.965698 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 830a54a6-10d6-3005-a56a-cac438059779 | -4.0903 | -48.9557 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README32.md)
