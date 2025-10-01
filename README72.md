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
| 422ac99b-9c26-3028-9920-1ac001bf2943 | -10.91297 | -44.3394 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9692f2bd-3ccc-306d-93db-6973e121ebef | -14.75364 | -45.76941 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 085c1c64-711a-3159-ba8d-de974b3ff21e | -12.87614 | -45.26519 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d086bde0-99cd-312c-868a-eddf08d6c124 | -12.80228 | -46.8957 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f1ed163-2e35-32a3-9300-dc04a9865128 | -15.14694 | -46.44104 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f666f1f5-7a64-32a3-a449-e194902d5b12 | -14.71117 | -48.21771 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b33ba79d-5dc0-34ef-9467-b3cb3b17f2e9 | -11.83082 | -44.96533 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c370f072-87e6-3da5-8db1-55e6ebaaaba9 | -10.19046 | -52.55419 | 2025-10-01 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 899fdf93-a083-3bae-a461-3829540717a2 | -14.95311 | -47.51885 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc3359bd-f686-31b4-8a6f-94aeba093328 | -16.21017 | -48.2768 | 2025-10-01 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9b8e8c1-8df9-35b4-8a85-64edaf4121f0 | -16.02412 | -50.88158 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4b0802d-1ba0-3b1d-8f9f-9dd358a70a6b | -14.43528 | -46.35747 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27f1bb47-910d-30aa-ae6b-7f85163d236b | -14.89736 | -48.11608 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac39dac4-caa2-38e4-8d22-26bead958de2 | -10.97062 | -46.51094 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2c56e8a-19a8-3bae-b7ae-67a297d6e7aa | -10.3813 | -48.14784 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b56da262-88be-35ea-9b77-23bdaba6e031 | -14.92815 | -47.82141 | 2025-10-01 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7caaf017-caea-3047-bd95-4251fa00ec01 | -10.97666 | -46.5372 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db96573d-8425-3e53-a688-b5d49651aaf7 | -14.13666 | -43.45912 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d0350c8-d965-3a6b-8fd8-c08c6bfa133b | -14.78542 | -48.30288 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c52da93-267a-36cf-b855-32ce97b89535 | -15.31137 | -46.40958 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a2cd0d-14d5-30fc-8a00-bc9e76876624 | -15.48967 | -45.91291 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12c52399-7fd2-37ed-8a10-7be66f1897ce | -12.4597 | -50.23643 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 106735e7-b1f6-3be0-aea4-05147449994e | -10.97557 | -46.52257 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77ef9e3d-2fc7-3c7d-b7cd-13c2eec35e0e | -13.77361 | -47.972 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 225af753-2f2e-3da6-8612-5f0801d68f85 | -14.61449 | -48.31255 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c81c36b4-d06b-31e6-8e5c-c87af013bce7 | -11.08545 | -47.83632 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 983b0220-28e6-315b-be2c-7594262f45ac | -12.83214 | -47.02832 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 144433da-e3b9-3d03-a601-a8e072458117 | -10.90209 | -44.27439 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 598023f8-3e69-33e6-93b8-c6f756c4d813 | -15.27393 | -46.41068 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fc0dacf-2ef7-33cd-960a-6ff2f07d866b | -10.33125 | -48.19122 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2eb80c71-b42d-331b-bcd4-70bf721d580b | -13.34437 | -43.75665 | 2025-10-01 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3c738ac-bb89-3ff9-9da1-4e52f3016ee3 | -14.35152 | -45.93224 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7c399d01-e7ca-3471-8cd1-808d3dd2fb0a | -12.87323 | -46.76952 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b9221f8-8d71-3c31-a917-c8d99f781b08 | -11.80445 | -46.61902 | 2025-10-01 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11035914-2c3c-36c6-9bcd-df2f4406e15a | -12.83271 | -46.87526 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff214033-868a-3a00-98f7-767e52e17212 | -13.71151 | -48.6311 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54622e8f-0819-30ee-936d-dc073f436c6c | -11.81532 | -44.9775 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88b3d612-2ce7-3d51-bd0d-8b1b84d6d566 | -9.51326 | -54.74959 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 996ab8be-6114-308f-ad6f-b3e1980d41c1 | -12.49102 | -46.84082 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9445582a-60dd-3959-807c-8469f30fa96b | -13.33718 | -47.8685 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 539d88db-9ade-3d67-b02b-688d7d0ae833 | -13.37045 | -47.32327 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11e4ed7c-c873-3dcd-b131-f9b46140968e | -13.53328 | -44.84752 | 2025-10-01 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f698c5a-33d1-378f-a539-af67fb76871d | -15.24107 | -46.22642 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3383a29d-bb85-3092-94e6-ce56d4b55ff4 | -16.51008 | -46.94807 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db939538-40ac-38d0-95b6-b36e0e91b8bc | -16.91887 | -49.79214 | 2025-10-01 04:21:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6c8e595-4631-3928-8ee8-abbd162254a9 | -13.34543 | -48.145 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5990408e-4245-3e12-9922-959fd5c10310 | -10.81826 | -46.63486 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b1bd56c-0f31-3f41-89f0-bca19efde6a8 | -16.53813 | -50.27614 | 2025-10-01 04:21:00 | NOAA-21 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70db8e81-463c-3569-94b0-54b19eec699a | -11.76508 | -46.86679 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 41c7c29c-34be-3cc8-90a1-8b52f66a51b3 | -12.0047 | -46.64436 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29483766-e8d7-3997-965b-66f4a7b4ab5a | -10.81153 | -45.35658 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f97a908-daa1-3fe2-8da9-7392f15eb5dc | -12.24477 | -47.81985 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 25b30245-27ce-33b2-977e-c694190868dc | -14.43802 | -46.36154 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53538483-26bf-328d-8adf-fd048763b8af | -11.44187 | -47.28831 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b9acec6-90b2-3ba6-947e-948e23b643bd | -9.42899 | -54.70851 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 895df35f-54dc-39ea-9f9e-1a21bbf838d6 | -12.68835 | -43.19434 | 2025-10-01 04:21:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dfc7de7-6a0e-3fa5-9885-f6e0cd89f979 | -14.02562 | -44.96929 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63f8cab2-ead3-3a00-934a-d88488563dcb | -16.66499 | -49.12723 | 2025-10-01 04:21:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51f0dc2d-d53a-3b04-ad2f-640a44510229 | -10.92058 | -44.26606 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9be68f4-f68a-3def-af32-acb7c136cf9e | -11.93842 | -47.08162 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eb1a8a0-690e-3fa5-93cf-4fee80ae341e | -14.52908 | -48.36719 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bc8fa69-fc0c-3af3-8f7a-a1173c89b888 | -11.81308 | -44.96985 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 884e1b43-12c3-3937-9c83-d7c09033e60b | -11.45587 | -44.97183 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c7a9c4f-fe18-3cae-9dcc-10361a1b243b | -12.79612 | -46.91298 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a71f3a8f-1809-3520-a9f0-bc76a7687331 | -14.71007 | -48.26709 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8449459c-f71a-3d19-a275-cb7e4918a4ef | -11.57091 | -50.17706 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f11ed95d-7c87-38b1-8c63-1d175ede926d | -14.10324 | -49.75658 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a02873-e038-39f6-8c33-3e806191fa46 | -11.82144 | -44.98209 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3144bd57-e2d8-316d-90c8-498ad7ac5c1e | -11.51282 | -43.53954 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f940c3f4-f182-35e4-b187-e4c119e10d74 | -15.76097 | -43.68936 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34769534-f485-3e09-8ae6-b1d77fbc66c6 | -14.50126 | -48.45118 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e3297fc-771c-3289-9afd-e1ca773bcfa6 | -15.23719 | -48.74323 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 90d05030-9c90-35f6-98c9-a760accaf89e | -13.6287 | -47.64722 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7962babd-f376-3210-9d1c-9943e5642c23 | -14.18014 | -46.11604 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc229ff8-78c3-3f77-905b-7b816f9e5b3c | -14.95425 | -47.5117 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bcd8fae-54b8-36c6-bf3d-d5c6132f0369 | -15.08822 | -44.96811 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b81a6cd-c08c-3b16-afa5-94b1fbbc8962 | -10.34673 | -48.20617 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 68ff735b-6546-3500-a720-c203809cf598 | -13.61938 | -47.61986 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76ee1ef1-9db6-3dc6-99f5-413f476f2828 | -15.36368 | -46.11412 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac01611e-22a9-369e-9571-300328446608 | -16.3693 | -41.38554 | 2025-10-01 04:21:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ffe6b213-fc44-305c-b64d-c88b64d321bc | -14.02506 | -44.973 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70d91b84-10f4-397b-8fdc-b6efd89b7896 | -12.84321 | -46.8733 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5cb2d7d-f20a-3f44-adb1-9b3e6145a7a1 | -14.89859 | -48.1086 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 081abffa-0fb8-3bf8-a18f-3e9d2cdb5f75 | -13.66395 | -48.08372 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e55f4f6-f455-3935-bd60-27fb6ea49585 | -12.66502 | -46.88013 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f77601a-ad0f-3e4c-9652-c0a642f7e250 | -13.30584 | -48.70359 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02f6a818-5e41-37c1-89d9-40a2b78bd431 | -11.47278 | -45.08363 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cc2c770-45cb-35da-8973-5eef8441142c | -11.65757 | -45.31916 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1df8273-0f80-3a20-aeb1-62704bb89f77 | -13.37133 | -48.15717 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6f6d6df-dafb-3c22-b6ef-1f0ad37f9fd0 | -14.03218 | -47.98944 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6005aea-c866-34dd-ad03-9d9f2bb29327 | -15.93488 | -46.3578 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98751676-7fb6-35dd-be18-ce9428555c52 | -13.37554 | -47.31291 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70ed35cf-9e3b-358d-96cb-a786b03678b9 | -11.9439 | -43.91376 | 2025-10-01 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aefdc84c-22f5-3175-ae64-16b829a088db | -10.28752 | -50.47007 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f558345e-409d-3601-b53c-8309c04f67e8 | -16.03004 | -50.90105 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e9af08b-cb4c-3072-ba4e-c989e4e96586 | -12.24257 | -47.81199 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0eff2f72-0d18-3ad0-b134-6d21a0cddbc8 | -12.85762 | -47.01794 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af08aefc-6634-3ed5-9e1d-efcb9f3e97f2 | -9.56969 | -50.94686 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fdad54ea-ba52-39ab-889c-79090c056718 | -15.76522 | -43.73799 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d595e4a-409d-3dd8-8006-46b21ceb4c10 | -15.41218 | -47.04999 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README73.md)
