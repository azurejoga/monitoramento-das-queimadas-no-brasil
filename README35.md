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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6b66fa1-a80e-393d-a106-b3e1e7dae31d | -4.8446 | -42.74098 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3d61735-77cd-37e6-b556-e574dd9a5c36 | -6.81193 | -44.46275 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f914ba5e-9aae-38e6-a720-8585335e5d4a | -6.28939 | -43.51328 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90ce8f42-0c3b-32ff-9a77-8e7cd404ac75 | -5.6964 | -45.39585 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f245e4d1-0ea1-3cc7-a7d8-91a5265d0d33 | -5.76727 | -44.87082 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d64b707e-0efe-3a0d-9147-60adf8e753b2 | -5.89651 | -44.34932 | 2025-09-04 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f2c2623-d34f-3999-aed2-472cec432848 | -3.72876 | -49.68216 | 2025-09-04 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74fb2864-50d7-3ba0-8024-05ca3750d1c2 | -7.9391 | -44.93574 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9bdf237-a4b1-36ef-b580-e6da15e54748 | -5.83781 | -43.00346 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e92048b-2d75-3bfd-bf53-70c8c4f270c6 | -4.57014 | -40.34929 | 2025-09-04 04:25:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 092314a3-c008-3ab8-8ece-4b4954bc310e | -6.26441 | -44.51112 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 2e9920fc-2e23-3de8-86d5-fc46ac10dda3 | -6.35205 | -42.57039 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 842c5099-7024-3c59-b86f-4fb3f658957c | -15.01253 | -50.0768 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 923de335-3a40-30e2-9546-1d2bff65a148 | -7.70781 | -50.28579 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5687a305-2c2d-3ec7-8952-9de06876ca88 | -9.32681 | -55.22438 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ebaab2e-d987-30fc-b738-fb2467a86cb2 | -10.09924 | -54.78964 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0773cfd5-da15-3284-9a4a-cbda4f10e237 | -11.05141 | -45.40326 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2bcc437-da85-3da7-81a9-ad172583488e | -6.73819 | -58.74157 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 674c8c99-108a-37a0-80e7-51721c1d9352 | -12.64381 | -57.00319 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f19c989-fa4d-3675-ab8a-64b5116d7e68 | -7.85542 | -46.73471 | 2025-09-04 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ccaa95c-9c24-39eb-ba4c-127f932b89e4 | -10.03576 | -48.35529 | 2025-09-04 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 277681e5-5723-306f-acff-2576e6201c58 | -12.90584 | -56.9367 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7c0807c-ab18-3488-982e-159f4aadd89c | -8.87029 | -52.02584 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731e22e2-534d-3d07-9084-810b1d1a24a7 | -7.98045 | -46.76143 | 2025-09-04 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a71d710-3410-36f5-819d-720d7cc2eb79 | -14.29988 | -53.0892 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2096d65c-3c51-3314-a9fd-f44ff7b37032 | -13.85468 | -47.97988 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9b5b4e53-c798-3cd5-9099-8c0ebb6c8465 | -15.0114 | -50.07641 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6debfc45-02f9-36c9-8548-4d62473abe7e | -13.00175 | -48.08293 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96bd116f-2f5e-3f42-a183-12d242fe776d | -12.46114 | -48.08084 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7400c6f2-fea0-35f3-927c-423a08bb40e3 | -13.65652 | -46.94347 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cd07712-64de-3f82-bd9d-f1e165cb42da | -9.43374 | -46.7756 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53b1c26c-755a-3e1b-878c-c8166c11f27d | -12.88717 | -56.95009 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e5f935c-d47d-31cf-b0e6-02097594a59e | -14.59565 | -48.02545 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa74b24e-cf6e-341e-b04e-f10e507607de | -10.97022 | -49.75061 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19516211-6999-3c4d-8856-9cc9ac48613d | -13.85633 | -47.96927 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16dcfd26-b959-3328-a40b-e5af3a94b3b3 | -15.0501 | -50.05989 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43400fcb-d66e-332d-9a8a-2b8be135ddab | -10.00324 | -46.89846 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05e5064e-7d00-36ed-bac8-f88d43d6bbc1 | -12.97002 | -54.77905 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da81fd9b-2bc1-3fac-b934-5301d7c210f2 | -10.98772 | -50.93229 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 707b6884-7278-315a-b45c-599921e8a192 | -13.36472 | -46.33535 | 2025-09-04 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8b7c21f-cff6-3842-8de5-d633e9a8dc42 | -10.9871 | -46.8467 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82018795-523f-3945-91bc-1fb9010592d1 | -8.91614 | -45.88113 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 531f3290-1974-3d3b-bfe4-8fffeeb89df4 | -13.7121 | -46.91559 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 208b07ff-c0b1-32a7-8b51-38765a264873 | -10.97939 | -46.85269 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c931a5e-0e6e-33d8-9b18-9d0b494f97f5 | -14.75527 | -48.13492 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1fce74a-b7d3-37d6-99b4-47ba2fdf99ab | -7.96889 | -55.29181 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb17a545-58f3-3908-bea5-a083a0c612f7 | -13.30191 | -46.84346 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccf4ee53-fdc1-3177-8dc6-016e1a5981e3 | -7.74211 | -48.77166 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 059c7be2-d6ab-3a1f-9c30-de62342066a1 | -12.49722 | -53.8491 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86e7e54b-73d8-3416-a169-db8c05848712 | -9.81088 | -45.98323 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dc5ce2c-f454-3e5f-bf63-c4605722eeb7 | -11.87041 | -51.46511 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8ec6256-7334-3f85-9190-1be23b44465b | -12.52502 | -53.81169 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41816870-6958-3485-8acb-de14329cade0 | -11.59719 | -47.75624 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2477ceb6-b9d2-3b1b-95c5-973234e0b598 | -14.81935 | -48.33455 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a176f5c2-45f7-3b7b-8603-de97b45ab0f1 | -11.63742 | -52.20679 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b831e2e2-d8ef-3e15-b872-b84b4b53bc84 | -10.14177 | -46.24314 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fbea97f-19ee-332d-ad80-dad3fa324264 | -12.93307 | -48.06403 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7789567d-3f40-3050-bf64-ae4eebb118f3 | -7.68256 | -48.72763 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 18e98239-0cbe-3b6e-8fa7-4f1c8f173997 | -9.06024 | -46.99028 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cb625f8-b1d6-37d7-8895-167a4a2f0bbe | -11.5854 | -52.10759 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 00ee21e5-f313-3811-a137-1de8f099f860 | -12.8115 | -47.66912 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e28e7f9e-465c-31d3-824b-7590be50c7bf | -10.79023 | -52.7635 | 2025-09-04 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 050e6176-4312-357e-9923-235cb7ff1f93 | -13.447 | -46.9368 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c491ad35-2640-3128-9de7-2d2fc719c5fd | -14.57338 | -48.0358 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30c51c3d-367d-3362-908f-fa692238d3a9 | -9.44413 | -46.75575 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31b847b-b62b-3bda-ae18-89e66872a24c | -15.3359 | -47.36053 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6269eed6-6517-3fad-be9f-c45b1535bc7b | -10.75286 | -48.27505 | 2025-09-04 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 99ff150a-ca16-3ef8-9801-2e3902823a1a | -7.67913 | -48.7271 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa58e65b-d5db-3b46-a8d7-1f7ba29a4f36 | -8.4717 | -43.60952 | 2025-09-04 04:27:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f59a522-097f-3ffd-9caa-7355b6256a35 | -13.30692 | -51.7743 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 733faaf0-94ac-3d53-802a-5b17898191cb | -12.89422 | -56.94132 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 02ad4e36-a58e-3665-b3ee-ec3fd65a3f96 | -7.71374 | -50.31833 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a7608d70-b675-3acf-881c-3025a9ef9ec1 | -15.02954 | -50.03707 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a906360b-6b4e-332f-b545-f9b1b5e9a974 | -10.99565 | -45.91757 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0bed47c6-098f-3adc-976c-71bd74f2cdea | -12.48663 | -53.83455 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3fa4d50-5cfa-3bf1-b072-d4ce831600dc | -11.86761 | -51.54864 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 372a7a71-0432-378f-aaf4-e2ce00714db5 | -12.93637 | -48.06456 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1786ffa0-afb9-30b8-a674-f93f86052580 | -14.54365 | -48.05269 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7806c274-ec12-38fb-844e-d17b777302f9 | -13.4556 | -46.83407 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0bb63ef-b3df-3e77-8f32-9d5145a786c6 | -12.24123 | -50.146 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c93c340-6a9e-3916-b295-ca8b901b5fc6 | -11.86701 | -51.52971 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70896ca0-26cd-3f6d-b77c-8b82b5f1d14b | -13.5329 | -47.02389 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94fed3f1-1bb1-32a7-9522-34a6010aa298 | -14.57283 | -48.03934 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13886094-0ac1-3731-b044-9500338600b4 | -15.18859 | -48.01599 | 2025-09-04 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96ad1bee-320a-3738-84f7-1f7f2e9c672d | -8.37542 | -48.32963 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00468781-0b3c-322f-a761-d79d5ce35fe0 | -12.46444 | -48.08139 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67cbe204-e295-38c5-be7f-46ad205c879e | -10.8762 | -55.74172 | 2025-09-04 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da02e6ff-1823-3cd7-b0b1-145966fdf456 | -14.39507 | -51.67117 | 2025-09-04 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0109a51-2095-3630-8d1a-d35e4ebe8ad7 | -6.83482 | -59.36786 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 6a326b2f-f2f3-3f8f-b7c1-605ceab13229 | -14.57362 | -48.07992 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8853bd1f-d79d-3378-8c7f-d3fcce378cbf | -14.56944 | -49.14095 | 2025-09-04 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87167bb0-5cbe-3d5e-839a-17f6ab2288cc | -15.00587 | -50.06769 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d59f3478-d360-3f79-b7d7-41796932b70b | -8.0408 | -52.35366 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 91175e9a-1b61-34eb-a952-af6a3e916da5 | -15.0418 | -50.04696 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42a1ebea-afb3-379a-ba33-424e9a8c4944 | -8.91669 | -45.87758 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4db4994-d26b-33e9-8eb7-6b4f0ae0c99d | -14.55356 | -48.05434 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6277fef7-56bb-38dd-a367-08e126f3af04 | -11.64 | -52.19193 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 970c7e74-d7c5-38c3-af53-4606fa92189d | -15.05073 | -50.05609 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24594c3f-6268-3dd0-88bf-c4c75395b170 | -8.08471 | -45.36134 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a920f96-f7bb-3d52-a410-627a7e23d1db | -10.98784 | -49.72979 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
