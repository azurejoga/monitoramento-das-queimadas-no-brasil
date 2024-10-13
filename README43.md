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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd3255af-db4a-3c39-a8d3-02fcc624a1eb | -5.1178 | -47.352 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b94e148b-d0b1-3972-94a8-792109959b1f | -7.01773 | -46.82063 | 2024-10-13 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 832dcf41-b233-3f02-b816-cbd10847e8a5 | -7.01704 | -46.82444 | 2024-10-13 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f94d514-6569-34c2-8492-75643f2a03e9 | -7.0128 | -46.81601 | 2024-10-13 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d90b4bb-37bd-301d-90d6-a7c8e72fbd76 | -6.74323 | -48.18069 | 2024-10-13 03:47:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59267f34-77ce-32c0-b91b-12f35bc390f7 | -6.73709 | -48.17968 | 2024-10-13 03:47:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 435d55e6-fc82-3f4a-8c85-90140ad472d8 | -6.6841 | -47.37023 | 2024-10-13 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4628229f-b9dc-380d-b13b-0e8309a8e6d1 | -9.74818 | -48.30352 | 2024-10-13 03:47:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 524ce05e-b9f0-3605-be67-946759e250fc | -9.74745 | -48.30742 | 2024-10-13 03:47:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d12c33-1177-35a8-a4e6-317f3ca3a726 | -9.52845 | -47.80915 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b0753d-ef85-3a83-a4ea-cfe064bfdfe4 | -9.52425 | -47.80813 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d0fe789-aaf2-3101-bcc6-4b1d6fd1c925 | -9.52201 | -47.81202 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8e7cf42-163f-3153-a1f2-be77365f8436 | -9.51778 | -47.811 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc521e9-89a8-3103-b0f7-7a2781671336 | -9.51629 | -47.81099 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5a44c0-7558-341f-82e2-71f15772a7ff | -9.51206 | -47.80998 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50fd1bec-081c-3759-b431-93b40df31b61 | -9.51058 | -47.8099 | 2024-10-13 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83ee38e3-807e-3f46-9183-a5a5012d9b97 | -10.08632 | -48.19025 | 2024-10-13 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 921d9a84-fc00-36fa-a77a-f3ba8a75d792 | -10.08052 | -48.18915 | 2024-10-13 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8085832f-1b37-3da6-9d9a-b167df9f18ed | -11.20569 | -47.8514 | 2024-10-13 03:47:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5b75c52a-7185-3a5d-baf4-c11ad26690e1 | -12.17298 | -48.0539 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94872ce4-3250-33ee-9737-7ec6f9ee77b5 | -11.74265 | -48.36914 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2c8833d2-09f8-3bd6-8e77-67db5f896faf | -11.74187 | -48.37319 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 886caf70-7bcf-32f7-bf29-b021f81ca04b | -11.73696 | -48.36802 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5e157f0-dae1-3652-9f8e-503e6120c974 | -11.66235 | -49.06481 | 2024-10-13 03:47:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2240b6a4-34de-3dfa-bf05-1c9c612d9a26 | -11.65936 | -49.06321 | 2024-10-13 03:47:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 000b4a50-1a77-3e18-be07-d01365110a0b | -11.65846 | -49.06767 | 2024-10-13 03:47:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56e03111-50c8-30ae-9243-c78dcb593f40 | -11.65639 | -49.06364 | 2024-10-13 03:47:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b680abf6-f242-3d01-8563-8ebc4f2753d8 | -11.65552 | -49.06812 | 2024-10-13 03:47:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a6985b3-9010-3f2c-87f3-8ce042cb116d | -11.6373 | -48.38652 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd97c485-a471-3047-ab10-85cf59bbcf9e | -11.63652 | -48.39058 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ea64cba-5792-3b9f-ad02-db71667dedd5 | -11.63573 | -48.39463 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a21c0f6b-8d44-31fa-88ae-96737e08abdc | -11.63494 | -48.3987 | 2024-10-13 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7224e1d-eb2f-3761-9bdb-df57e6b3d9b1 | -11.63318 | -48.37721 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f4f0084-aa2d-38ce-a7ec-78c19c530fd9 | -11.6324 | -48.38124 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5505bed3-d480-355f-bc40-2a2133a233e5 | -11.63162 | -48.38528 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dd4dcd4a-d490-3692-939e-cda7c7f62fa0 | -11.63083 | -48.38932 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0100f1c7-a944-35d0-9a79-18712e1b6185 | -11.63004 | -48.39339 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 874be90d-8ed8-3af2-8b1c-9bce64c9cbf1 | -11.62925 | -48.39748 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63043bba-d5a3-38b4-b70a-d30ab7f16f45 | -11.62749 | -48.37601 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b8a658f2-77bc-31d1-ab6f-e4b4dd0a8f62 | -11.62671 | -48.38004 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e4d94911-9a35-3e6a-9011-1d81d5c16bbc | -11.62592 | -48.38409 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 188b3aa2-861f-3880-9899-c14a4d9b7b46 | -11.62513 | -48.38813 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13b4badf-f061-3614-93b7-30d2545f1128 | -11.62434 | -48.39222 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a135a7a-9af3-3335-b5ed-0da61c8c8aaf | -11.6218 | -48.37483 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b342048c-c687-3705-8154-6dbbe1f2552f | -11.62101 | -48.37887 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6f6119dc-ffff-37cf-b053-d5efdc7406ec | -11.62022 | -48.38292 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99bc10e7-03ab-382e-a130-1c027168c3d8 | -11.61943 | -48.38698 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 300d80f6-bca4-3a97-9b48-23eb3d791b2a | -11.61531 | -48.37769 | 2024-10-13 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32214006-0bd7-359f-925a-abd27611b6ef | -11.59549 | -48.47912 | 2024-10-13 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4695cce-2c1f-33a6-b086-bb76c15ec858 | -11.59469 | -48.48321 | 2024-10-13 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf744e6b-ab4b-3055-bf72-a96d83448c51 | -13.02867 | -48.64758 | 2024-10-13 03:47:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34c6f08f-3597-3022-b9b2-3f39f308c9db | -13.02527 | -48.65317 | 2024-10-13 03:47:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cb350bf-bcd8-3d13-a1d8-e50bbfe1329f | -12.83744 | -48.56818 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b523ff5-bbeb-33f0-bf55-d800ce7c9108 | -12.83669 | -48.57201 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a651047e-0670-3da6-9857-73e797a78e4e | -12.83499 | -48.56351 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48315b54-350b-3fcb-ac48-edaabccb130e | -12.83345 | -48.57114 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 342ce369-8afa-33f4-b9ef-44f8cde5c826 | -13.02787 | -48.65152 | 2024-10-13 03:47:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a5fdfdd-37fd-3275-b7e9-77bd9c5b2d36 | -13.02604 | -48.64922 | 2024-10-13 03:47:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff379621-0e12-3fd1-a5b6-6794b2577651 | -12.83422 | -48.56732 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8772113-cf04-370a-ac9c-2978eba246e8 | -12.83253 | -48.56321 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 462f7454-4c3b-3285-91ea-1861e9aab425 | -12.83178 | -48.56705 | 2024-10-13 03:47:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3808eb22-ceb0-3ff6-b4f9-07e33dda9ac1 | -1.04959 | -47.93209 | 2024-10-13 03:47:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 950d29a8-5e7e-3a0c-b86a-7a53dbcd3df5 | -3.21765 | -48.92465 | 2024-10-13 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c08148f6-8a13-3c47-b245-ca605c42528f | -3.21658 | -48.93081 | 2024-10-13 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb7e7ace-7827-3a57-b6e0-3fa323f2bb70 | -3.21588 | -48.92386 | 2024-10-13 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 87f624fa-7a31-33d2-adc0-c2216534d475 | -3.21485 | -48.93 | 2024-10-13 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ee8e7858-cd83-3838-a09a-3316dfac8192 | -2.78583 | -48.70302 | 2024-10-13 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52436a59-5e69-35b6-ab53-eebcb3716767 | -2.74955 | -48.40596 | 2024-10-13 03:47:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1ae96c5-6496-3ce8-892b-95892528399f | -2.7486 | -48.41164 | 2024-10-13 03:47:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 67a3c74e-fb53-3214-a08e-eea08924ce03 | -2.74723 | -48.40784 | 2024-10-13 03:47:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d0fb005-39c8-3826-8d43-d1881c6055b5 | -2.74625 | -48.41347 | 2024-10-13 03:47:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a99ad79c-0f50-3da5-b280-9098fac5b974 | -2.16481 | -48.81606 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0fb8e112-be7c-34cb-95f8-503bad69c0fd | -2.16387 | -48.81581 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8c81c835-a843-3c94-b11f-5c8c3090850a | -2.16375 | -48.82225 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0e7bcf7c-d75b-31d0-8975-b9e6f51ff33e | -2.16286 | -48.82202 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bfeace45-3f87-31ef-b627-144502b2796c | -2.15799 | -48.81492 | 2024-10-13 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 382c04f4-3284-3863-8f89-c5ecbae9c71d | -4.11804 | -48.27727 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3975c9f-7cf5-3960-b92f-86981f3b9413 | -4.11732 | -48.24338 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c3ecc5a0-a379-3485-887a-bdcb7acae918 | -4.11643 | -48.2485 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8c768cf0-115a-3b10-9d67-f8f91ca3dfbe | -4.11093 | -48.24219 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 60709088-7d7b-3374-a18d-ef8bd7a9ec65 | -4.11065 | -48.28171 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f68cffe-9a52-37f2-914c-080465c3f924 | -4.11003 | -48.24734 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6cff5613-1e0e-3cb6-9e0d-d6e2ed82d62f | -4.1091 | -48.25267 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b2a16ae9-3921-3025-baca-b78549536c05 | -4.0509 | -48.23812 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bf8a13a-a446-3cfa-8edd-61882483601e | -3.91717 | -48.35755 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f79add4-050c-3b3e-bd1e-d90bb39d8b3f | -3.91705 | -48.35849 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a6e4983-1dcc-3eb4-9efa-6c42a9f04299 | -3.91622 | -48.36308 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e2658ea-2b49-35c9-a037-073fa3d6bf5a | -3.91606 | -48.36404 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b88462a8-fe84-3903-abac-8ee268785ef8 | -3.90976 | -48.36187 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3452e058-927f-3c45-93fd-c5864126a2ae | -3.90332 | -48.3606 | 2024-10-13 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51a78de2-b00c-31d7-9bdf-b4214c487b20 | -4.28339 | -48.63132 | 2024-10-13 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c291e421-6b02-368e-bf5a-4c700f6e835f | -4.28239 | -48.63708 | 2024-10-13 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6248e7b-f21f-3065-aabc-d960813ea2cc | -4.27818 | -48.23515 | 2024-10-13 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f576b73-c111-3ff0-8529-8e3ea7c536f4 | -4.27288 | -48.23764 | 2024-10-13 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e11e170d-8e8d-34a4-ba77-5fa70f5e6828 | -9.30227 | -49.64171 | 2024-10-13 03:47:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99a291f1-fff5-3ab0-9e49-3668c7e87824 | -10.52884 | -49.96031 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94231a51-3901-31c3-86db-52d060a59cbc | -10.52245 | -49.95895 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8afe313d-2893-3f9c-bf58-871b1b18b644 | -10.52137 | -49.96435 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 245ea236-070c-3cd4-b6ff-359fd5963cdd | -10.51921 | -49.97514 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0848b048-a644-3b72-b135-551944529ab8 | -10.51438 | -49.96184 | 2024-10-13 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README44.md)
