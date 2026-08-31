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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 759f5a31-16e5-30c8-9d54-02c3771b43b8 | -14.3871 | -52.556499 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc6ef3e-317a-3ac9-a944-823937497178 | -10.8544 | -50.487701 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62daf58e-f5c3-3d21-9718-6d9920e55f3e | -13.851 | -54.091599 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4edaf66-3901-33a9-865e-222379a97efb | -5.4803 | -57.139099 | 2026-08-31 00:11:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b832eff-63f0-3e6f-928a-d4c43a551e91 | -14.1867 | -52.875198 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce789a8-8dc1-3197-9724-22361475bba5 | -6.2518 | -53.6688 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f36f1861-de9f-3129-a845-3d222091cdde | -6.8648 | -44.431 | 2026-08-31 00:11:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afe99fde-8cea-3837-8df3-64627f249456 | -11.2368 | -45.116699 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0afcd10-db31-3f35-93b0-935b7e48001d | -11.3406 | -45.206001 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1454699-fad5-3be9-80e3-c907fba1b165 | -18.2883 | -52.666901 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 905145af-e423-3008-9f9e-fe5a628a1552 | -4.0641 | -48.955601 | 2026-08-31 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d614b5-6904-3276-aacb-b8378346474a | -3.6138 | -60.543499 | 2026-08-31 00:11:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d47bea02-daff-399d-89af-012a0c7e7dbc | -5.5907 | -42.339401 | 2026-08-31 00:11:00 | METOP-B | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cdc822c0-dc15-3329-99cb-476410c0bd5d | -12.0964 | -45.0401 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 237477d8-4477-3272-b3ee-0d6d057c015d | -1.6068 | -54.398201 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a02dc4d-e1c4-31f3-aebe-6bbf02ea5372 | -15.6123 | -56.412998 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a15244be-2672-3f98-8b3e-d389c0a6a7d7 | -10.7793 | -50.848598 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f76a683-c89d-3124-8c42-fc2c32f62cdb | -15.6677 | -45.912498 | 2026-08-31 00:11:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ecf918ca-e68c-397a-bc82-77eb0a08864c | -1.597 | -54.400398 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 623a2894-5f23-3b0b-9955-a0254fafcbb9 | -1.624 | -55.160702 | 2026-08-31 00:11:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d2113b-8b6c-3dba-ab76-e521288f5157 | -11.0758 | -51.506001 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eca5762e-09b3-3790-a170-61d1b4642490 | -9.1963 | -51.548801 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eac4a7a-e70f-3af0-873b-6a0db58ddaaa | -14.5802 | -54.077702 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b27a226-cffe-3e8e-9fb8-773c8ad26ce6 | -11.2151 | -45.112301 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57f6f36b-3688-3fba-99ea-27072f2eabe4 | -9.1452 | -59.506001 | 2026-08-31 00:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58818156-1c82-3330-b066-71193adcd682 | -10.1547 | -45.734901 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d433b74-3b63-3a05-b12f-5171594bab04 | -14.989 | -48.152699 | 2026-08-31 00:11:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 683d3f91-c14c-3d20-97a2-9551620b0c1a | -5.8265 | -47.073299 | 2026-08-31 00:11:00 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc8e56da-68df-3dbb-9a77-405f99221342 | -5.2463 | -55.916302 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4af4665-f581-3c76-968c-a170f7faa770 | -15.152 | -48.659302 | 2026-08-31 00:11:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd92cd3-301e-388e-9e7a-b0e91bb61664 | -7.9264 | -44.259899 | 2026-08-31 00:11:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8024b791-70a6-3dc7-8cbf-c5c05c580c67 | -10.7809 | -50.855999 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d4ce0bd-b315-32f9-9f7a-3bbbc39b6809 | -14.1962 | -46.558102 | 2026-08-31 00:11:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c8a6bdc5-6e1c-3f32-a2be-f077019edad0 | -12.9503 | -45.9473 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13ef9825-5c5f-37f2-81b1-4bb613a778d0 | -1.8811 | -48.825001 | 2026-08-31 00:11:00 | METOP-B | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 904297f4-101f-36d1-b366-3e86b48c1e67 | -10.7629 | -50.867802 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8f79254-2e30-3da0-9d6c-483c004285e8 | -14.585 | -54.1017 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f41ecce-ae4e-3893-bf7c-95589272f10f | -8.0793 | -45.465199 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 19e03909-d122-3531-a7b0-65c7bf4fda3f | -15.7692 | -49.951099 | 2026-08-31 00:11:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da4d3b6f-f288-32f5-92fa-27286cdd3ab1 | -12.3954 | -46.445801 | 2026-08-31 00:11:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0100c699-afff-3d99-82e8-e84a75a0942a | -9.4289 | -45.676601 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28d2f9d9-c014-3e88-bc92-d7995e4fda3d | -13.3715 | -46.919899 | 2026-08-31 00:11:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 467941f1-b36a-3088-837c-d3322b5ff954 | -8.5943 | -46.472401 | 2026-08-31 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ca9abcd-a6e6-3a94-ac38-363919f73823 | -18.3057 | -52.651699 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 599bb601-d833-3371-a286-3402cc26243e | -7.2903 | -52.365898 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ace6e0db-e90a-39c7-80db-3cacdb28a204 | -11.9262 | -45.062901 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 239a6972-2e92-3119-a0fc-f4f8739abd76 | -8.237 | -49.0434 | 2026-08-31 00:11:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f4d97309-c004-3688-8270-7038c1f0d9b7 | -7.5117 | -55.280998 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da6b0458-a70f-3337-a0e8-730c0fd72779 | -6.5993 | -58.5737 | 2026-08-31 00:11:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50c4a954-c971-30fc-ad3b-b2b1f02e015a | -10.7597 | -50.853001 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 120df809-06c3-36af-ae7c-5c80ac7f2874 | -18.280701 | -52.680099 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c232d54d-cd99-35a0-b998-4f7eee8d36f2 | -7.4968 | -55.307701 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2baf79e5-db13-336d-8c71-fda2680889d4 | -6.5934 | -58.593899 | 2026-08-31 00:11:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63a04424-5e62-32fc-bfe0-e110925f21d2 | -10.7538 | -54.044498 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 975e2e71-b8fb-322f-97ce-4617b71a4eb9 | -1.7491 | -46.2696 | 2026-08-31 00:11:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eaaef883-20c6-3140-8c71-4096fa0ecec5 | -9.4408 | -45.683102 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1a033e2-fd1d-3a76-8787-0878c1e4b753 | -11.2249 | -45.110001 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8114b0d-ac33-3087-8f6c-73f1e90a2bbb | -11.332 | -45.169998 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2bce5f4a-680e-364d-b3b2-89a81426d90c | -7.2821 | -49.832699 | 2026-08-31 00:11:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0507723-0a89-37a4-b03a-db32ceb8e261 | -14.5923 | -54.0877 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9106e0ee-2d45-3b83-a9bc-6d2fb268d364 | -10.7418 | -54.036098 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 509cd2b5-cb5d-3109-85ec-68775b1e6f90 | -6.2115 | -53.578499 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88fd47ea-d54a-330e-86cf-87e16495b154 | -11.3384 | -45.196999 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b9852e9-4fba-3427-993d-fc2e72db4366 | -18.2861 | -52.655701 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec73997-be8e-31b2-9e5c-d744a7a2d9a5 | -5.2389 | -55.882198 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e75260a2-9ac5-3e57-914c-e47763ace4e1 | -10.7321 | -54.0382 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8e1de0d-9368-3ec8-8a06-1e56dc89c147 | -6.4844 | -49.9035 | 2026-08-31 00:11:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3e6bc9-3389-3129-9778-417767cc0873 | -7.767 | -44.068001 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52c6271d-eddf-3289-82a4-e70070106c52 | -5.9626 | -57.678299 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bce46fc4-5b70-3ed3-ac3d-ba24c5486a60 | -12.9466 | -45.931301 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67b66a92-1447-3704-a56c-4668bbfb9097 | -6.5383 | -51.429401 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae3f6b1-127c-315c-a488-57595fda5762 | -5.8748 | -52.145699 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f787d116-cd3b-338a-9945-4d3423b3db94 | -10.8414 | -50.4753 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b52919dc-a0df-3059-b860-3a4e8768d2a0 | -4.8454 | -55.813999 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c6b784-cfee-3f86-8383-bf54994c7f7b | -4.8479 | -55.8251 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c77c01c3-a467-37a0-abee-b40ede482eb0 | -5.9399 | -57.667 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 756e2013-02af-3ed6-9048-0056c0173cf4 | -9.6744 | -50.871101 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7b54b6-24e1-3966-86b3-737c1002cc44 | -14.4027 | -52.5331 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4082dfe6-0090-3e18-85f7-0d34eb34fdee | -14.1965 | -52.8731 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 673b4386-f8f1-3b2c-a256-9fd9caec8804 | -11.1492 | -50.5667 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e779f3f4-34f2-36a7-872e-90967f15ec9c | -8.382 | -45.002102 | 2026-08-31 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0962ebd1-e177-382e-a21c-dd478dff4069 | -12.935 | -45.925701 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7244425-eb06-3f9e-879c-1247fd918773 | -12.0887 | -45.051498 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 218a847c-6247-3ac3-b2be-1ee79663b46f | -10.8512 | -50.473202 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b5874cc-2b18-3239-bac5-a913c31fa82c | -1.5872 | -54.402599 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 693baad9-2237-362f-8c94-5478acd6f7f4 | -10.8177 | -45.351799 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34f0f365-0f61-347e-a43c-4588b6501c35 | -15.9043 | -56.193298 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0195357-3abe-31f5-9164-23ca7b740502 | -3.5442 | -49.477798 | 2026-08-31 00:11:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87fa3854-d765-3c04-a490-9b569e355ed6 | -10.7679 | -50.843498 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d2f3360a-013e-3bab-b667-63d512fa0d5a | -14.2077 | -46.563099 | 2026-08-31 00:11:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 479eb95d-2f88-37dd-b17a-fac041a24641 | -19.118799 | -57.382599 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 704b5767-ccca-3fa3-bcfc-9b3875207a46 | -12.1138 | -45.026402 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f73b55c9-7b5e-3684-a39b-aae37fae80da | -6.1832 | -44.944199 | 2026-08-31 00:11:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7eaf7cbf-ed02-3858-8e12-932bda988ea9 | -12.1 | -47.267502 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea31e6d-452d-3677-a9b5-d57b282afabe | -5.872 | -57.778099 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18657964-1f5f-3784-98e0-c6103a176614 | -9.5798 | -47.6101 | 2026-08-31 00:11:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5ee413-25c5-3401-88ae-f9bfe0843206 | -10.7972 | -50.5079 | 2026-08-31 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fdab50f-3029-382e-a6b8-7bd3f706ad58 | -15.2035 | -46.227001 | 2026-08-31 00:11:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ea77863e-4fb5-369f-a077-3b56b00fdea2 | -10.5489 | -46.183201 | 2026-08-31 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef6226e6-f86f-3681-b844-cb9776fb4876 | -3.6916 | -51.9986 | 2026-08-31 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
