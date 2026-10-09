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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34aa9f42-488e-358f-b085-7cbda757114e | -11.28488 | -45.20558 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98f29313-0cab-3df2-9904-2488ad0dacf7 | -7.56297 | -46.6858 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9c24a8f-65bd-3385-a8d3-5f2cc1a38766 | -11.76279 | -45.47651 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97d71059-2c84-3c50-8fbe-2e56e6292478 | -6.45225 | -55.05439 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3707a2bd-d64d-3bc2-b856-dfa7793787d8 | -7.40456 | -44.75769 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80e67c62-0f00-3b01-a194-5e9ecd7eed21 | -7.40569 | -44.75024 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b39a170-0287-34e6-aa70-dd78bc5a03e6 | -11.00263 | -47.47385 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb57b7b1-c3f6-3e4b-b658-f70ae195f2d0 | -6.17146 | -52.8598 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2032d120-370d-300a-854e-ac8ddd7416e7 | -11.06452 | -44.06929 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 983d4133-a711-328f-a561-5df1940037fe | -8.52275 | -46.9021 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b35d76d1-6cb0-3ad2-b7ec-4effe1b71cde | -13.15166 | -54.33697 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8e1a811-6071-3290-ad05-b135e45d6bac | -9.8737 | -47.47086 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d49998b4-1fb6-3cd6-b6c7-b6b016afae93 | -12.00753 | -43.44508 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d230cc6-f4cd-365e-84b0-1a2606c30a97 | -11.61117 | -43.70481 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3055b0dc-813e-34f0-b2b0-034462847b86 | -9.80355 | -44.77507 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ece8e2d-a004-3f60-958c-61b44721f331 | -11.90458 | -46.5625 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 859ad27d-0ac4-356a-a367-a286cbb93bc8 | -7.18543 | -52.62245 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c17e638c-e6e3-3a0b-bab3-3ca2586bdee2 | -12.21122 | -44.61788 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdaa3f64-0cc7-30bf-8932-bd98d5c6e3fc | -9.05368 | -47.31741 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f15d77fa-bc09-34d6-bb45-4651a2a09485 | -6.01636 | -53.49279 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f34455fd-eea4-3cee-a4d8-4054cbeeb55b | -7.25426 | -48.06645 | 2026-10-09 04:27:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c69bc21-b944-37a5-b4f1-13542acca448 | -11.01703 | -45.42485 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dddb6835-0a28-3622-b4d6-eb948fe1c990 | -8.96249 | -45.12358 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa227100-8b61-30a2-a5b9-81aa3f6ab541 | -13.1141 | -46.33404 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bd00f0b-4f2e-3b9f-bf28-599b4a9eae89 | -11.18118 | -45.30813 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e30cb5f4-59a4-3528-9378-0e7feec5109a | -8.73131 | -45.14559 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 87bdffcd-5f32-3fda-8bdf-f9e633f247a6 | -11.05667 | -44.04588 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19912f04-7b7a-3cb9-9d7a-8a2b183e0756 | -9.27736 | -45.6438 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0abad6f-d395-3c89-8bee-434de2ade734 | -11.67781 | -46.77939 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 736a9f7e-0b97-3280-8267-d2a1a673ba3c | -8.18101 | -54.72139 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 581d9f3d-203c-3a87-ac13-b6ff0c84fc1a | -12.37195 | -39.47763 | 2026-10-09 04:27:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78d746fb-c538-36b5-a19c-725b033f51c1 | -10.46538 | -47.86304 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1da0298-53f4-3955-ac61-fc8d911c8d8d | -6.92807 | -59.26637 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d88e355-75dd-3016-b7a1-305ef4f5bd8a | -7.1868 | -52.61445 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89fe9d9b-5728-3ddb-88ac-fb9ca34fafaa | -12.21472 | -57.09681 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf14f714-377d-3203-8fb0-1b2e8a5deadb | -8.73812 | -45.14662 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a4c606e-f58b-3b36-b755-a2b516b38da5 | -8.32914 | -49.12682 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18cad602-cf75-3e34-baa4-cd0f79becbb7 | -11.1116 | -45.68523 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b922fa89-2264-3e09-8c5d-1d6ced22ce43 | -10.58009 | -46.29025 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4924b09a-9b30-3ad4-9195-d9a6e66a3817 | -11.86739 | -43.56297 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f249112-58bb-3b2f-8209-21298a564ac4 | -7.4822 | -42.79145 | 2026-10-09 04:27:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee4b9e0a-051b-3b1c-b66f-4dbe20964a4b | -8.18967 | -46.35598 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a86201c2-da2d-328b-9a3d-323dc00ffabc | -12.22017 | -57.13182 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b22bd9fd-b502-39f0-b4ff-7c89feff7389 | -13.16128 | -54.34201 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eae46813-f7ab-348b-b866-c578ce7287c0 | -13.16745 | -54.34868 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3799620d-28ef-3ebb-9538-d09e8be0751d | -9.3019 | -47.42513 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 074592fa-0d08-31d9-98e6-cfb7becd64d1 | -8.96202 | -45.17295 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18689d84-e3c4-3709-b93f-388b16dc63ee | -9.29812 | -47.47084 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 18bac99c-38bd-35fa-9dcc-ef3bda6ce79e | -12.01525 | -43.44578 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6971e859-8487-3b5e-9b2b-3362893d3926 | -8.91336 | -45.21867 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f160b01-0bbd-3c7e-8ab2-f069e724daf2 | -13.16593 | -54.35727 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 68cfc982-8ee2-3e46-a3d4-c0e36cf86206 | -13.48426 | -42.48503 | 2026-10-09 04:27:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7584e59b-aa3a-32d7-aa17-b66f10f28ce1 | -11.75933 | -45.47606 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a02bd5f6-afa4-3825-af44-d80d4c994d65 | -14.60594 | -46.57598 | 2026-10-09 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f3ead9c-0f29-37e0-b290-812c89de863a | -10.69921 | -47.783 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b5fb86f-6f59-3754-85b9-a9817a533760 | -6.99741 | -59.10562 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7da338b-a2bc-3c76-92c0-e2db141d2807 | -11.99771 | -43.48769 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1cc7c816-ab60-3109-9fcf-b31bf25a4398 | -9.90294 | -44.78979 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcf134b1-09ed-3c65-a244-6e1a62e72e11 | -12.20997 | -57.09866 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4966bfc6-d287-363d-949f-38ce14bc20a1 | -8.14093 | -49.43723 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 189c062f-d4bb-304f-a402-76160efa7d23 | -13.16805 | -48.13803 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7df9707-7360-3048-87a4-a0b0aa67f82e | -12.0011 | -43.46325 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98750289-8e78-33ec-a296-ebd2fc236477 | -11.9966 | -43.46751 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 531fd283-5cd4-365c-b5e6-5deb0533aeab | -6.84564 | -59.39488 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54bda7b7-fa0a-3d56-b5e8-29e64c8a29d6 | -7.05893 | -50.00626 | 2026-10-09 04:27:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88818bae-ab3c-37f8-898e-1b319004c5db | -5.95307 | -55.34127 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 514f5080-c66c-3093-8574-ba3bd057af74 | -13.1719 | -54.35714 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7f4b55c1-1535-3855-a70a-2eec1023a20f | -9.76294 | -44.7847 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc21f12f-149e-3aae-8027-bc15a3fbb6a9 | -12.00625 | -43.45424 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ef87f064-5a71-37e3-8b99-90cdf34f13fd | -12.09579 | -57.15809 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fb9a1ea-8162-33f5-983d-3ef27eacb4ed | -13.25654 | -42.25512 | 2026-10-09 04:27:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 10e32fda-4ef8-35cf-b5dd-97d5d89f766b | -8.74096 | -45.15083 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bdbe94d2-282a-3be2-a724-2fae35a07e2b | -13.15091 | -54.3412 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c99e106-f650-32c7-8daa-7b922aba2cd8 | -11.11553 | -44.00113 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e8a10a45-8029-354a-844f-91c763ec3ee4 | -8.73298 | -45.13445 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 352acb1a-87fe-3f38-a4a8-3c9c2d311f33 | -7.53889 | -47.12532 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61760bd7-4ea0-3fab-bea0-f84b4deaa144 | -11.5828 | -43.66198 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f20d9bf6-3afe-30d0-b408-451f8e27aea9 | -8.72852 | -45.16408 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee2723aa-4932-3de4-bf1f-61b86771888f | -8.30553 | -45.7337 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62892184-8dc3-374a-b3df-5c68f538e423 | -13.11858 | -46.32724 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5983c2e6-d8ab-3183-9dbd-61883e8d74dc | -7.27619 | -46.16945 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9f6beee-a99c-3cae-bc54-fff6ae29ef70 | -9.29751 | -47.43155 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 8f997a1a-672d-35c3-ba93-1c0e27dd4f06 | -6.10111 | -55.72663 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53bc5a23-4381-3532-94b5-92ea00d92b49 | -9.91399 | -44.78743 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52ce5918-411b-3ac9-8746-fab95a9ce399 | -9.28101 | -47.42892 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d1eaeb0-68b3-3e30-ba71-64290b81aa6e | -7.89978 | -54.71845 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e5f114b2-deb6-3c51-b275-6002fc356302 | -9.24499 | -45.63951 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d926ec6-a658-34f1-895a-a405e9fea30a | -11.61145 | -43.6764 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f10d73f-cbff-3da3-8e6a-71a3d6e1c29b | -13.1695 | -54.36237 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2bf78f37-0a29-397b-a066-aed0bc9f669e | -11.66515 | -56.76721 | 2026-10-09 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32fd8998-a3e0-3a5b-94e4-c762acb36a56 | -13.15749 | -54.3294 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7419a9-5178-3ab1-b7a1-bb24b4387890 | -14.44416 | -43.92693 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b6bc4c0-1575-39ec-82e1-7c0ae58d1b9f | -11.71831 | -43.63277 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1eb5cf12-3ac4-3813-8c59-e7d1bd918c7b | -10.31868 | -46.26462 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8420277a-6484-3e8b-bdce-5a038a6d0371 | -11.90403 | -46.56609 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 722a046c-c4b9-3ed2-8536-e8fe41064496 | -13.17026 | -54.35806 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 24e39fa2-4d35-3540-b3f1-5933062f467f | -9.89946 | -44.78924 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7511f456-4936-38ca-9325-3bffdc51be56 | -8.33491 | -45.02967 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3bff64b-ce03-3965-9dd4-5de4c8df796c | -11.06515 | -44.06494 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e25a4eb5-a61d-3e02-95c9-e3bb78654150 | -8.90601 | -45.22131 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README116.md)
