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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 642673de-3f4a-300f-9982-e49e10ab5414 | -9.5858 | -47.32548 | 2026-09-28 16:26:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da9200fa-545f-3f26-b9b0-21fb3b069993 | -9.99652 | -50.12827 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2be47969-e2de-3ef7-a624-3bf1a5e66f32 | -10.73742 | -48.77079 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb882aea-3c4d-32ec-9d55-1e0c612edd7a | -9.08943 | -46.83659 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66cd36dd-1a18-3af8-adfc-de43f088054b | -6.21191 | -52.90419 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 459930fd-8426-3805-8806-b5c3f8a32489 | -10.97966 | -50.69427 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2a1efd25-78ab-3454-8661-4f06186891a5 | -11.13401 | -51.1681 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 5b4eacf5-5d8a-3653-9980-307f9ad86ee2 | -10.94391 | -43.90569 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0bdcfc4f-e3fb-34e3-90d7-736494d51938 | -11.13976 | -50.06509 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 332952f6-09f6-3d6a-b90a-4f6a9bdd69e0 | -9.85424 | -44.95629 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ac5d09e0-17d3-3aad-81d6-5136d208e9f0 | -9.00521 | -47.59159 | 2026-09-28 16:26:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01b4553d-931f-394d-923c-3b76bccfd7ea | -7.43948 | -55.63784 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 9900bf72-3d94-3f8c-89d6-c9ea2f968f21 | -4.20886 | -42.98351 | 2026-09-28 16:26:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0e732714-a7f8-30a5-8ad1-98e2332a1405 | -8.24826 | -47.66825 | 2026-09-28 16:26:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07c52149-bba2-3839-a298-a9a5c52960ab | -6.39 | -43.22081 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a07f7dca-d330-3e25-ae74-fdfbcb179fb0 | -8.19647 | -50.15773 | 2026-09-28 16:26:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1451aaf-9784-371a-8eb6-7d024b267167 | -6.35958 | -45.79199 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5a280083-a1e5-396d-acdb-e8703ff132a4 | -8.58575 | -45.09319 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 79a39b4b-d7f7-3de0-aaf9-09b89fc687a9 | -7.26421 | -45.33908 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 81c6a371-415c-325b-8b11-316ef54e0715 | -7.43862 | -55.63138 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 40ec9ff2-1db2-3fc4-bdfb-f6d3fac68a62 | -6.46393 | -45.91287 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 05515f79-57c5-344a-acc7-a2c9682164e0 | -6.35839 | -45.78396 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1804424d-d794-3380-a48b-4e60b1cb6690 | -7.29303 | -55.59252 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa5233f3-6eb2-3e7f-bae8-73a8b0c6f617 | -8.77289 | -45.82662 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| cfed5453-433c-327c-be09-ccf18ff10cb6 | -6.65871 | -55.09496 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d066bc38-a3bf-36c2-accd-e7c538947721 | -7.25232 | -43.35935 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b96d4881-ac53-3f09-989e-1d4d012c10d8 | -11.08477 | -48.89277 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 76eecb37-2da2-33b6-85b2-851c821ab987 | -7.19978 | -44.85791 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6d61054-45c0-377b-a5ff-b86f60196e0b | -7.99795 | -44.97778 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 28ab17d6-64ef-30cc-882f-5d923017066b | -7.68123 | -44.8811 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| c17deec6-32b4-33f9-bc37-01ca7eda2edb | -3.80997 | -44.10641 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ff8b5d6c-5568-3d30-8e1e-016d278e9794 | -11.07018 | -48.88969 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 3407d14b-00ed-3bf3-a161-b6cc134734d8 | -9.07874 | -49.87309 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 3681a534-8505-374e-af7c-149d58c8e51a | -9.29764 | -46.44922 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f33ca24-94e5-35ac-b62e-0b15c39751b1 | -7.23753 | -44.85957 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9682422b-4e12-377a-aef0-e8b2263c14dc | -10.79011 | -48.74607 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| df712939-9119-3f33-8fa6-809828b6642e | -8.72812 | -44.90549 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d4d156bc-58dc-3a0b-adf7-e5187ce79077 | -11.05152 | -47.67033 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 0e69a67f-bf36-3dd7-b3ad-e1973a0a35cb | -7.03896 | -43.87757 | 2026-09-28 16:26:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49c7f678-274a-3f41-952a-76416480f1c1 | -10.78981 | -48.744 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bdddc42b-5c67-32b1-a2a9-67dbfb1b18d8 | -5.98154 | -53.52626 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1f9a191a-865f-3bc5-93e3-23be64659ba8 | -8.39001 | -45.46698 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9298df10-eb35-3e21-b1c5-20a9145dea13 | -11.07771 | -46.07528 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 61793e13-7a25-38d0-aa21-e181d6a91958 | -6.22199 | -46.63349 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 079155fd-d8d0-3c6a-a15a-8bcc358e7a8b | -10.27158 | -44.61967 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6caff20a-5070-3675-b47d-f49a2975efd2 | -11.13396 | -50.05984 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8d2189c0-42fc-3fbb-a9c3-45d707550518 | -3.66401 | -44.80286 | 2026-09-28 16:26:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 66bbf6b9-4908-3f51-afeb-c219b5df7f03 | -7.68179 | -44.88491 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.9 |
| e82344b8-441f-3153-b994-36c6225113ab | -9.82991 | -44.93897 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 23fe7b74-c464-3ed1-b36f-277748b2fc20 | -9.97941 | -45.34032 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 2a64114e-b915-3dd0-a2f2-49c43f203c42 | -11.75645 | -50.76213 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3dc4ae71-63c9-3f39-9d24-500fd342b5b6 | -10.99057 | -50.69617 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b0ab829a-558a-3bcf-bef0-17c7df4e4923 | -10.9409 | -47.58661 | 2026-09-28 16:26:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 979b7146-e397-3cbf-9a7f-17c9f1312024 | -5.85425 | -45.91391 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 440d2574-a7b2-3505-8dd0-249d78986394 | -9.77278 | -44.86352 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2e53c0c5-fdc2-3c5a-b3c1-541f35942014 | -10.9354 | -43.87162 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 7da7b1c6-67bd-3e67-9c33-0ab191cb18c0 | -9.33285 | -46.54575 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6319199-480b-32ca-afea-2a219098b7d7 | -10.55128 | -49.77143 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f6d1c41b-cfba-32f5-9a4b-96466e08fd85 | -9.76628 | -44.84373 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 66658e11-6ece-329d-8f7e-a925c03f5960 | -11.15023 | -50.06675 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d6a52640-010c-3420-b48b-ba03f7c336b8 | -10.49389 | -51.29676 | 2026-09-28 16:26:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1135a97b-7d65-3588-8f24-eb1b51b7e3ed | -5.72877 | -53.44662 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 01ae90b4-c8bf-3388-a3d7-41120ee35838 | -4.71396 | -43.1995 | 2026-09-28 16:26:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e5e49e5e-8d33-3b95-bcca-084e67f47289 | -8.63869 | -37.29148 | 2026-09-28 16:26:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a187ddcc-f3e3-35b2-a26f-20bcb6db9f18 | -9.15834 | -46.75727 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f42119ba-a593-399e-b4f6-ec204987fe60 | -10.24861 | -44.61039 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f717e8a7-64cc-38cf-b429-8225d5140bb5 | -3.40695 | -43.04307 | 2026-09-28 16:26:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f71502b-749a-385a-a5ab-18a36155d512 | -4.27124 | -43.9945 | 2026-09-28 16:26:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea6b6047-a0fb-3aab-bd17-dc31ea2d7b0b | -8.44502 | -47.2062 | 2026-09-28 16:26:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30c43ab0-5f60-3113-9c79-2f5c05496a7c | -10.948 | -43.88549 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 91b65cc6-fb83-3469-a7b4-1c9fb8a90de9 | -10.97885 | -50.68779 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d31b8769-29e9-3630-a11a-bc192f97cf0c | -7.57795 | -44.79407 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d6ef4ee7-2880-3102-8065-6d6ee7013895 | -6.35363 | -45.80119 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cc4c882c-d31a-3da1-af21-77d4ec41a784 | -8.86226 | -50.65377 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 369a9893-e231-3c08-a40e-084d65ba22ea | -10.24031 | -50.0049 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bd64a2e5-fe53-3b94-8928-f3e02233086b | -8.6702 | -47.21496 | 2026-09-28 16:26:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4c3366b1-99a8-335b-941b-d85c2fbd5485 | -7.22893 | -44.84913 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62936348-16f6-39ce-a1a4-93a73be68e5b | -8.37241 | -45.48229 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5bb0bfce-ae43-306a-b447-4ccdbcba3ecb | -9.85067 | -44.95684 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7771aa84-947f-3213-b6dc-8aa5710bc80c | -5.25781 | -45.42508 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9ab2f01-5c8b-301e-b9e8-f957a1f32aef | -10.74137 | -48.7654 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e16ea8f6-3fbb-3072-9ca3-618731522867 | -7.62174 | -47.06709 | 2026-09-28 16:26:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c02b4450-186e-315f-bbfc-3f0cc51fc852 | -11.84676 | -50.84951 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c33ff680-ab87-3d0b-a1e7-ec5afb81de88 | -6.35601 | -45.79256 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5db1ff19-a223-386d-aa56-53b76e6dc8ff | -7.20811 | -45.0815 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| d1eef9ad-7e29-3482-bee7-bfed0a48c828 | -9.77811 | -44.82534 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 13f67dd2-37e2-3adc-8ccd-1a71689a6ac9 | -10.79435 | -48.74311 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 66e2d880-f2ad-3353-9528-86b55738f5bb | -10.89817 | -45.11152 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| edc63010-94df-312f-bebf-24578f8986d1 | -11.19516 | -46.28246 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e36d131a-f520-3227-b356-72cf8c09cde1 | -7.13085 | -47.60655 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 42216f3e-4aaa-3548-9b3f-fe34018f8b7e | -7.8471 | -46.93144 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9306d67c-8fc4-3900-ab12-8c216c1c4d31 | -10.21852 | -50.0031 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 08b53b17-632c-3583-9444-fa7cd8c6d0ea | -7.67886 | -44.88926 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 9e0ab703-3256-3fe1-8cb6-75f344332c0f | -9.96823 | -50.15048 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 477c0b11-12fd-3a03-8335-db546b9d89a5 | -6.69231 | -45.67907 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e8247d59-9ba6-34c6-ab8d-88745bd49b2b | -9.98513 | -50.12492 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 264cf474-162e-3ff2-9496-c99d8628e8c2 | -7.5878 | -44.78886 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5d95c47-77cf-302d-946e-e247f67027b2 | -11.1161 | -47.70765 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea1587c8-6482-39e0-9051-f45b9368d345 | -7.44006 | -55.63655 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 233c070c-383d-3b09-8f80-c171b02d7595 | -10.45846 | -45.08913 | 2026-09-28 16:26:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README110.md)
