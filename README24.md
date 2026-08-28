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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d5750ec-e10a-355b-9368-41b72feb782e | -9.61124 | -55.1226 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9494d14e-d074-3384-b6c3-30ac36f08c94 | -11.63776 | -46.73426 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb8f9b47-ff66-3cc3-a839-5a042e64610a | -12.43367 | -43.40995 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 47933b22-db4b-3909-9be8-3d488070652c | -11.23682 | -54.00251 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c6c5a666-7d68-3ca7-b671-b07e9b614ab2 | -14.18719 | -52.82838 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 164564ab-05f9-31b0-8a7c-005925fd9390 | -13.59239 | -45.77472 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d7c220b-5153-3bbf-b535-8cedf0966f25 | -10.89368 | -50.52218 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c6ffab3e-8a74-3b60-a321-215c41649228 | -14.3011 | -51.73475 | 2026-08-28 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5440c7a0-fcab-3e41-b8a9-3f51fec33061 | -10.79973 | -50.64632 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d70e1de-3762-3cb4-b655-875d722eab30 | -10.79664 | -54.00489 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de7f2b94-e53b-3cf0-a919-cdaffe674a0b | -11.56931 | -45.51055 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f10724a-b0b4-3969-b9b9-c0d7f227cfe7 | -9.4337 | -51.69899 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 41363f46-c7fc-3c0c-bed5-ea095f814a89 | -12.50142 | -43.81417 | 2026-08-28 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d693a98-a31a-351e-95a3-79b6a64d8092 | -11.2287 | -54.00816 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6834a3a4-c681-3201-86da-23cf0985950d | -15.53527 | -41.92578 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 20032fd8-591b-3598-85af-95fbc8458cdf | -11.25694 | -47.06561 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 304a9422-7ebd-372e-b9a7-d458e4ac2854 | -11.57359 | -45.54807 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d8a2f03-52b4-3e22-a0de-32c924a8d3a5 | -12.37781 | -43.44593 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4860947-cfc6-33c0-8a41-3bb901c292b8 | -9.22516 | -51.5699 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edbe6bd8-151a-316d-8220-e5d51450afbe | -13.41194 | -51.41655 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 83476987-5060-358e-a5ba-e3c328848d62 | -11.73448 | -54.5517 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 982d4991-6acd-38ce-bf40-cff103f8700b | -9.21477 | -51.54548 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08c29210-1b9c-32c3-b4e8-06d69784e797 | -12.28218 | -50.58776 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 21411593-c2a4-363e-9208-35409c162c3f | -11.20291 | -53.9957 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| face1f75-d5c8-319a-8c74-18360f72c0da | -17.04432 | -39.71029 | 2026-08-28 04:17:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 242371ac-370b-3ab2-ba85-e44e95347c41 | -10.77878 | -50.63525 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dc0c879-21e5-3e0b-a07e-38b03b9cbdc8 | -12.28428 | -50.60075 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1758c499-164a-3712-8289-4ba0dcfddcce | -16.1826 | -45.63468 | 2026-08-28 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 978e46d8-59ff-3894-868b-7c6bfbfac623 | -10.99328 | -51.08721 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd63725a-0d4a-313a-bbe8-a8c2cdd8398b | -12.23393 | -41.89623 | 2026-08-28 04:17:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2a0844e0-bcc3-33a7-bc61-e77e2ff67239 | -12.06139 | -47.16377 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 321e3c3f-8b08-3607-a451-898967b49024 | -10.75688 | -54.03512 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| da263a3c-42ec-346c-a479-1939cf33d1eb | -20.34408 | -47.59624 | 2026-08-28 04:17:00 | NOAA-21 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2d652077-5f0c-38f9-bdd7-f095371694f8 | -11.64532 | -46.73159 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f954c5a6-3159-342a-8c7a-bc80c82b1c5d | -13.58515 | -45.77721 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f582af1-f7cc-3653-bd24-e3b5c5e834b1 | -11.82464 | -47.21138 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2322b25-5401-3507-a2cc-f6b061d0eeb0 | -15.31924 | -52.7577 | 2026-08-28 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b9362ca-0064-3708-ae34-8115b24b2832 | -12.76547 | -44.26333 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc98cd06-480d-3cd5-8fc2-54d84078e7e9 | -10.94795 | -51.0554 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac0036c0-aab7-3cc6-82ac-54b86ef95c20 | -8.59361 | -54.79376 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 768f305b-226d-3481-b648-44ce2371df2d | -12.28998 | -50.59338 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9c689e91-8cc4-3a2d-86a7-84468d512ad9 | -12.27295 | -50.59026 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ff9df5c9-4c88-3b82-aa70-4a5e8118054f | -10.91525 | -50.53365 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da1ea28e-6606-34f0-a88c-f11293f3eca0 | -14.86347 | -52.59645 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23ec8133-1f56-3ee2-b3d1-6c8f636d7670 | -13.41635 | -51.41736 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e03c719-a39c-32df-81c6-9ac1b100e82e | -11.23139 | -53.99387 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 159e4d1d-46ce-3fc6-8092-f1a7b01eb891 | -12.20718 | -50.57081 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dc54c69b-bd00-32ae-b03f-50825e7ee547 | -15.76258 | -49.95214 | 2026-08-28 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a517f48e-3193-3413-88fe-fb948cf2f230 | -12.24461 | -50.5767 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 8e38505c-c58f-3a7b-96cf-b9c08f34efc5 | -8.77679 | -50.07168 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca126d0-0379-3314-9dff-c7a303c3b467 | -11.57427 | -45.5224 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 384170a4-18bc-3205-99f7-da301f51af1f | -11.73257 | -54.53174 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0caa01e-902c-3193-bd43-37ba86f623bc | -11.23411 | -54.00934 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c45de7da-b725-36af-af6f-aff901b100ec | -11.48605 | -45.07306 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39bdaa8d-f27d-35e3-98f1-0db2ff281efb | -9.9664 | -53.94237 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 31453e37-dae3-38e2-878c-7eaf80a5e68b | -11.47992 | -46.94616 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88fb45d7-811a-3f9f-8dc2-9be8102b7e99 | -14.42399 | -52.59383 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 926a2f71-9117-3030-b8c1-cfff54bb9c92 | -14.4037 | -50.12457 | 2026-08-28 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cabb5e5d-0140-39c8-ae71-bd192f9dc696 | -11.2456 | -45.04462 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e2e6a42-4ca5-3062-ac58-503b7cc1281e | -11.5943 | -45.39727 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57303b5d-89b9-3391-857a-69e6d462f154 | -10.55581 | -50.48674 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e623e1c7-1893-3b69-a733-309f38debefb | -13.58849 | -45.77776 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b94b794a-9b23-3aca-af4e-be96f571baa5 | -9.96595 | -53.94189 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 004e0b9a-b5f4-34b8-b91b-8f4cb2b54268 | -10.47257 | -46.18703 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8198296-8d64-382b-9495-c76d83be829c | -11.47925 | -46.95024 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed20cabb-4424-3b29-9161-7004a26c1506 | -14.30612 | -51.70794 | 2026-08-28 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1837114a-176a-38cd-a8e9-1c0c156ef893 | -10.63498 | -45.22586 | 2026-08-28 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c25e82-b31d-32d0-9b13-000632a0f764 | -11.02243 | -49.65638 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fca24c28-e70f-3056-a60f-13d4fb8821f1 | -10.98715 | -51.09558 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a627c79b-677d-399e-9896-03a6e4f1c5ea | -11.2368 | -53.99503 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a15a7163-516d-3192-abd8-10a4c56995fa | -9.57549 | -44.57173 | 2026-08-28 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4c6af7a-5c79-3cc9-a5cc-72f3dd36727b | -15.52375 | -41.9284 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 99a5482b-f03e-3236-9a63-98c48ca20609 | -8.59089 | -54.77508 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69135571-4250-3db4-80c6-b314955536ff | -13.45818 | -54.02214 | 2026-08-28 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b7883c7-b460-3fa3-84db-b97b813a3efd | -12.30124 | -47.63842 | 2026-08-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a19431b-1f96-37ff-84e5-96d9793913f4 | -16.051 | -47.22912 | 2026-08-28 04:17:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfe7e56a-7dfa-3e06-b41e-24cfe8c5117d | -8.59005 | -54.77959 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ffd027b0-0ff6-3b35-b70f-05be734ba9b5 | -12.28146 | -50.59182 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3c5a9ee6-5497-3548-9656-4c2d3754a255 | -11.23545 | -54.0022 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b458aaac-582f-3758-b2e0-fc667ed01861 | -14.89938 | -52.60025 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22c600b6-47e9-37c7-963b-277c194a6ef0 | -11.27211 | -54.0239 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 330aceba-b0ac-32ad-ae25-d24b7d7b11e1 | -14.87735 | -52.63945 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dadfda44-fdd8-3682-ac76-64e7fb82ef1f | -14.41934 | -52.59277 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fb713e7c-f63a-345b-9097-720b2eef9545 | -10.79174 | -50.64044 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec477215-030d-37a7-b81e-88103935465c | -14.59926 | -53.15579 | 2026-08-28 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c32294da-ae81-3495-99d0-77e10de97777 | -11.16739 | -51.22432 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83212243-915a-328c-a74f-30a5de80e8b4 | -12.27793 | -50.58698 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| cbc99302-56b1-3f38-a47a-43b6f14e8c1a | -10.33236 | -46.74884 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a06019d-a948-30b8-8063-95c87e4c1898 | -11.22938 | -54.00457 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4342486a-230f-3f7b-a080-a641b9f37c8b | -9.0601 | -45.77845 | 2026-08-28 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c45391eb-e6ea-3942-a064-c53db2b8df29 | -11.55455 | -45.45302 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60b67f9f-c508-3a19-af93-bc8239623ab9 | -10.8452 | -50.51786 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93947c72-1735-3738-981e-c15bf7b53d70 | -14.92908 | -52.59579 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d5273822-0a8b-3bed-9509-738160976de2 | -11.78418 | -47.64965 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c4416f8-6909-3ff6-9a0f-e639d995be90 | -14.1882 | -52.82313 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c06a42d5-20b0-3ae9-93df-b1c3ce807cf8 | -11.22464 | -53.99986 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 917438db-3f94-31cf-ad76-ccf01a4f8d09 | -13.40753 | -51.41571 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 327e34b0-618e-36fe-9145-40a4cc1665c2 | -9.66021 | -48.29532 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a0767bf-db51-3397-8630-f6e8d2e00755 | -11.27279 | -54.02034 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c9e63dd-e222-3367-bfa8-fec1cf1f5460 | -9.45585 | -51.71405 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README25.md)
