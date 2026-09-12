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
| 100f2631-dda1-3d65-ab88-e3e42000a150 | -9.90981 | -46.23196 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad5c8b92-46c2-3f4d-b421-e9aa8a061513 | -7.11031 | -42.11136 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec5f9182-4beb-3584-95e8-7ce716dfbf2c | -7.42792 | -44.56248 | 2026-09-12 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1adb9ef9-168b-3154-91e0-7c84a34d4f36 | -9.54795 | -45.47826 | 2026-09-12 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 24c9edf2-3802-315c-91bf-9d79bd4643e4 | -8.11041 | -48.76397 | 2026-09-12 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03c31291-3c95-37c7-8aa3-e305820ee519 | -5.8249 | -53.80538 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dc79446-7b51-377c-b294-ea1dcd90858f | -10.05276 | -46.26531 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be8dc212-e649-30ca-a690-3b4b4ee38e2d | -9.91899 | -48.52858 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab3d973-c224-363d-9caf-70b6bfa5309c | -5.57821 | -48.68558 | 2026-09-12 04:34:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b05508e-6da1-3666-a401-2dab5dc8a3a5 | -9.49602 | -48.16483 | 2026-09-12 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91d44c2b-38d4-3952-843f-3c33d497cc86 | -6.50335 | -47.59746 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea1611d8-12b7-3b54-b2ef-f3864da02137 | -11.19273 | -46.31173 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c2b5c27-c7d7-383b-a98a-604e9390cc9f | -8.53533 | -54.69659 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c650a8b-b1d2-3677-8bc8-15710607b911 | -5.93438 | -46.3544 | 2026-09-12 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a6193b7-7a19-31cc-9771-4082d33767e6 | -9.72951 | -48.08315 | 2026-09-12 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b4acacd-f09e-304c-b0ff-7bdf74b586d3 | -7.94343 | -46.24211 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40661196-fde4-393c-86dd-1677f74c04af | -6.11259 | -55.63342 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c724f4c5-ea33-3750-af4f-62fbbbe70ec7 | -7.19659 | -45.9238 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 104c8231-aa24-3af3-991d-420b78cb95cb | -9.89991 | -46.22603 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 372b0efd-69d7-32b4-b96a-081fed3d14be | -8.50498 | -50.15093 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43dd9e23-0f8e-3fa5-bee0-07061bef2283 | -9.67376 | -46.01582 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 856adce1-300f-3a16-85f5-59f7b81c193a | -6.88551 | -55.63485 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb5eca3-0256-387f-98d7-dc9324c127a5 | -7.18215 | -45.92556 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7919fe1-1e55-3840-b74a-b157a48c2530 | -4.53297 | -54.96124 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4df8e4b9-3b30-3f10-9a20-76bb18b39199 | -8.11072 | -54.79394 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 536fb2bb-384b-3bc0-8905-5fc7f28d8bf4 | -10.22296 | -45.18705 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6f6533b-fadd-3134-af3a-9e8c64cf5b7d | -11.35572 | -46.28522 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5d52916-f107-3a96-b2c8-39bbd0536c0d | -6.06827 | -53.48794 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94862f88-d204-3732-9bd6-868488c53449 | -5.8269 | -53.79318 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8a33685-5a1a-3bec-8fa1-a0b99a41b7d1 | -11.39015 | -43.9579 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7890ce48-1d97-3f1d-b2a9-9f2d1cc7c8bf | -6.85234 | -55.25232 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1c1cdc0-3fa0-39ef-989c-715f238cddd1 | -10.17459 | -45.33779 | 2026-09-12 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f750af6-6366-3e26-a6e4-f15db8cb69d8 | -8.32218 | -54.77545 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef4135cc-400b-3db2-b330-5d07ecff656e | -9.36816 | -48.41993 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19530616-0359-3115-9b08-a690bf3f0239 | -7.17988 | -45.89389 | 2026-09-12 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03114db4-fb72-376f-98a1-9dce0fb5524a | -7.60705 | -43.96355 | 2026-09-12 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc9722b9-a9ef-3b0d-9283-ace1b0807e0e | -11.24355 | -54.14424 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac62d676-bc9a-3aa7-a464-f00a83a32343 | -13.41355 | -42.48547 | 2026-09-12 04:34:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30d5333b-30cb-3b68-babf-371a91004ef6 | -11.7177 | -47.73881 | 2026-09-12 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 601e362d-0fb2-396a-85da-8f50419f4cde | -7.30837 | -45.9896 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3420ef0d-6b89-3360-b51a-19a02035c544 | -6.72977 | -50.81438 | 2026-09-12 04:34:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 450fc9ee-a8bc-39e9-b605-7eed31c49f5c | -12.38243 | -47.39017 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7be0d105-c09d-3971-acd4-1ab8fdd16f07 | -11.23806 | -54.12859 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb36b18c-b6cd-30ec-b7fd-e344426f6382 | -8.90777 | -43.88676 | 2026-09-12 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d00d9f36-5772-31dc-a9d9-c78750c85fa3 | -10.54006 | -49.45103 | 2026-09-12 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42d175e9-0305-3deb-940b-620bc24da8a4 | -10.95622 | -49.59463 | 2026-09-12 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e73cbf-e0bc-3542-81e3-68116e1ff4eb | -6.23294 | -51.68213 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da738316-6a40-3269-99c2-e4b606239e30 | -4.82155 | -55.76801 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e547d11-8c2f-349a-afa1-482f2290f01a | -7.92891 | -49.73521 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 943312eb-7320-38bb-acc6-308ed423040a | -6.23374 | -51.70049 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23a3aa5a-359d-378f-bc08-27895690d4ec | -6.28275 | -56.01953 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f88c0be-8cba-375a-89fa-41d7ef8ae4d6 | -10.74985 | -46.19983 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8daf52f-280e-311f-934f-ca62a09e9ecd | -7.45508 | -42.11869 | 2026-09-12 04:34:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3eea56a2-a889-3643-9213-040a74949824 | -8.53893 | -54.70149 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baa53c4c-2dda-3b0c-ba59-65e884996a79 | -10.46545 | -48.64439 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c8023bd-dffa-349e-bf57-6102694426eb | -9.90633 | -46.23122 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27c259bb-3f1a-316b-9b89-320e530bfa82 | -7.82933 | -47.9273 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 030925a8-c230-312d-9be8-0c4708769859 | -9.15992 | -49.98095 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f9446fb-fd04-3844-8d1f-836bd949ee2f | -10.5504 | -51.38021 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3fb8339-eda8-3e17-bc3a-ca7817452d54 | -6.88079 | -55.63393 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58a45b21-e82d-3be3-9dff-217f612ebe5c | -6.42686 | -56.10694 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69d08794-9bbb-3ca3-b801-431750ede362 | -8.61296 | -47.38416 | 2026-09-12 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 433b53f6-785f-3d73-a58b-87165e7b9d31 | -12.64377 | -51.42789 | 2026-09-12 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf499c7c-1894-3168-a2a0-49852aa4cdd8 | -7.96071 | -44.00829 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52bfb28d-d315-3f7e-a80e-810cfd3be810 | -5.85146 | -53.87626 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 598fa144-46e5-3384-b135-612d2d0e13e9 | -11.36414 | -46.79397 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab76eed2-7a3b-3de9-a9f0-fbbbc4e56b05 | -6.2285 | -51.68597 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c285cf74-cfd5-31bd-a671-a5ddb2f0b8e2 | -12.13439 | -48.9542 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3cb622e9-8e93-396d-89e4-b26161ac5a03 | -12.65093 | -47.0921 | 2026-09-12 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc6f6224-8b8d-3360-88af-bab58c27e755 | -8.61684 | -47.38111 | 2026-09-12 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28b68d0b-9752-3431-a583-1e8c6e2e2abe | -6.23519 | -51.69163 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb3f5d1e-8588-359a-9b2a-0ed717245f8b | -10.56188 | -45.21045 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aacc22d-fede-3e10-b1fd-271c034817e2 | -11.24665 | -54.12652 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c27ac694-1d0e-3066-9c80-7884da0566a0 | -12.1377 | -48.95472 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 689e367d-918e-3237-9c4d-c719260ec808 | -10.56245 | -51.35011 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66b2e6d0-f930-39f3-9984-e8a249bec1ee | -9.23203 | -51.7344 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aeec3f4-0d5b-3f4e-80b9-02dcb03f7e94 | -10.90851 | -47.84167 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76f8b243-a1f8-3d9a-8bfe-dddc2510394f | -11.24018 | -54.13997 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8633f11-4ec4-3142-b22b-230acb33d6db | -8.38032 | -47.55103 | 2026-09-12 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d2de232-cd93-3e3a-b98f-224eb5be035c | -7.70078 | -55.44564 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 754756a9-5274-3207-935d-465bcb9746de | -12.29544 | -40.56769 | 2026-09-12 04:34:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45667bff-c935-33e0-a34f-2abd0373f719 | -11.79956 | -46.38834 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82f664f2-78d4-3da0-8c8c-65911f8d85b7 | -6.23302 | -51.70492 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d664a262-d7cf-3f7b-8a8c-ee44c0ce6057 | -9.53358 | -45.45032 | 2026-09-12 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d029dfc5-064e-3e4d-b7b1-8209b18ea188 | -5.82754 | -53.78926 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5aa8774-7139-3fcf-b863-a62c96a93ab9 | -10.04925 | -46.26482 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89106566-62fa-33cc-96b5-661fd295d947 | -9.31509 | -44.34954 | 2026-09-12 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c2c347b-7889-3cb5-9fad-d4733126a7a5 | -10.8962 | -47.83243 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600a5e54-1205-36f6-9a35-c6cac1eed578 | -7.21453 | -44.5653 | 2026-09-12 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c0aea85-098e-3a76-93ab-c9dbbe828d9c | -6.07528 | -53.49723 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61178c2c-ea3a-3d3b-afdc-5515359ea225 | -8.10008 | -48.8728 | 2026-09-12 04:34:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 443b2b97-148b-3046-baa9-5a7f066191ce | -8.11877 | -54.79967 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f44dadf-298c-3539-b9a2-3cb6fd81d111 | -6.2036 | -55.27165 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1b76912-1464-3f9a-8972-5cf9f8c643e7 | -6.10688 | -55.63784 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d74f860-c271-3fda-bf4f-b74d1bcecb3a | -11.36761 | -46.79448 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3b74a75-7832-33d1-a446-98e207907119 | -5.97964 | -57.76751 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7eccc6-6f14-3f09-b893-601ffd7389fb | -11.72108 | -47.73934 | 2026-09-12 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c759ca48-83e0-3cd8-be4e-217acd205e3e | -9.70954 | -54.34806 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a98fdf-1bb4-356d-9db6-cb311da74d49 | -7.17693 | -45.93659 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb81a53f-f4e9-3c8d-a683-09ac7250afe9 | -11.40885 | -43.94205 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
