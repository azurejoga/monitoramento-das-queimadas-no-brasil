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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b61e3361-0310-3bce-9d9f-77a8c36ecdb9 | -6.55256 | -43.05361 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa3f85c5-e1e9-3cc2-9326-169045ca0328 | -3.98245 | -43.23915 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e6d53031-a746-3c3b-b40d-b300ac8ab322 | -6.56664 | -43.02925 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a3d8bce3-64eb-33e3-9ac8-af3b3bd39077 | -6.94269 | -44.56356 | 2025-08-16 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1758ad5-36b2-3757-a735-2cb2765f8b5d | -6.52385 | -42.76151 | 2025-08-16 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d322a0f7-8d01-36f0-b7a0-33f88d3ac030 | -6.67613 | -43.76673 | 2025-08-16 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ffe2083-58c7-3864-8a98-ad3fbac2df42 | -6.58523 | -42.23465 | 2025-08-16 03:42:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9486ef65-6c07-34d6-82b1-8b8105b58128 | -6.53538 | -44.54651 | 2025-08-16 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87dd49de-4aa5-357f-be64-efe25dad18aa | -5.6167 | -44.80191 | 2025-08-16 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 648e4c04-e104-381e-9a8e-c121b9eb88ca | -6.55045 | -43.03722 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f75ad82a-3158-3e72-863c-a661704263d2 | -6.95866 | -42.86621 | 2025-08-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3ecf5b5f-2745-3c3f-b07e-75d6e3c3d988 | -6.54075 | -44.5471 | 2025-08-16 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd0a17df-1e41-3fb2-ae1a-8d9dc444fc30 | -3.36038 | -43.35699 | 2025-08-16 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea5d5bd-2e26-371d-a3cd-9e039f3ff5f2 | -6.96421 | -42.86205 | 2025-08-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a790a809-7cc6-31a8-ba2d-13e3488cd194 | -2.38209 | -47.66342 | 2025-08-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d55829d2-c584-3c52-859e-2dbc0fe7c76e | -5.76275 | -46.66922 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7ca4d4d-82b4-3457-8e93-42ed8b9c17bc | -6.56094 | -43.03365 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f9bdc82b-b884-32fa-918b-0ee8c97f5afd | -5.76191 | -46.67401 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f778ae6-8462-392a-bf04-600942a65c31 | -6.56875 | -43.04567 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57809ea6-886d-394e-9e66-6d5c3dedcfd7 | -6.96055 | -42.86501 | 2025-08-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| c6ca17e7-11bf-3cb8-b281-7fc863b09e80 | -6.56396 | -43.04482 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8fe54495-bf01-3fad-beb6-4268ab5a3c6c | -6.5507 | -43.0643 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bd72514-d608-3797-a2ed-fded8fff49e2 | -6.54655 | -43.03126 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23ec0575-b08d-3565-a07f-34520d8348a2 | -2.47428 | -47.21079 | 2025-08-16 03:42:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f28edbe-3c31-383e-bbd4-c8fcb715ba13 | -3.98705 | -43.24289 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84a9c74a-e801-3b76-a7d4-c2fa6045e287 | -3.32722 | -42.78585 | 2025-08-16 03:42:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43531ffb-f1e1-34f9-ad69-3a6ed7f396aa | -6.86213 | -42.80859 | 2025-08-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 05c63d28-208c-356b-b354-ba711ad6ceed | -2.47529 | -47.20491 | 2025-08-16 03:42:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 640ed01a-6993-3592-b44d-f1d15701581e | -7.01272 | -44.31885 | 2025-08-16 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1885e77c-ff60-3ea7-b557-2ca7adc02408 | -6.6706 | -43.76871 | 2025-08-16 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9401cc50-952b-34c2-b755-03dd05724da4 | -7.01787 | -44.32001 | 2025-08-16 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1472a524-cd1f-3b18-8195-3e7227c10a37 | -3.98326 | -47.89114 | 2025-08-16 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2c4fb2e-f18d-33af-a86c-26567901ead0 | -6.56183 | -43.02853 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 39fe56f7-17c7-35ba-9c32-3427dd4fbac5 | -3.98586 | -43.24097 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a2432815-790d-3aff-929d-21b112072085 | -6.96337 | -42.86703 | 2025-08-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0eb91568-3ea6-352e-98a8-00a379357274 | -2.38104 | -47.66975 | 2025-08-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 935364d0-5a4a-3146-be21-3a13286eca42 | -7.26229 | -39.67 | 2025-08-16 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6527e87-0d80-36b2-ba1b-f31a79340827 | -3.98657 | -43.24586 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e17d4df-31c9-35ff-aef2-dc8ed8350d55 | -4.54728 | -43.30022 | 2025-08-16 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 673f8c46-7cdc-30d0-b6c5-bef5422e08dc | -3.98754 | -43.23992 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3cda5851-b09b-315e-be36-2ffadf615b13 | -6.58067 | -42.23405 | 2025-08-16 03:42:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fae92113-192b-3fbf-9b15-31f5a00fd848 | -6.56272 | -43.02338 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 34952876-ae62-3ff5-be86-1a32068049e8 | -9.16308 | -45.31787 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ae57cce-9b09-33a4-a878-b987c03a3857 | -12.60174 | -46.96793 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| db094996-d8e3-32bc-be21-c7435e1a7ab1 | -8.19632 | -45.02027 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a235295d-8498-3533-aa67-ef7daf52cd4d | -12.57394 | -46.94189 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57ac48f7-18ce-360e-81e4-0c954ff5ef0f | -12.61927 | -46.93846 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 064dd4bb-ebe3-3c45-bc32-796a37339ce8 | -12.60735 | -46.94004 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d102acd0-cbe6-38f7-a95a-9d9a40c0fced | -13.12292 | -46.84757 | 2025-08-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10acf025-0e7e-383a-8d66-308607dd949d | -8.16243 | -45.02512 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9059444-2601-3d99-8e06-178ff098f1d5 | -9.19925 | -45.33143 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9f99507-6604-32e9-b465-ccf48c699755 | -12.59941 | -46.93023 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 30095948-1caa-3423-9863-260d5cbe7243 | -8.1832 | -45.03211 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9d11351-3949-3ebc-aaa8-2ebe223c7d45 | -12.04752 | -45.76725 | 2025-08-16 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6f477fcd-5986-3e40-aa46-9cc39f10eb1f | -13.57031 | -46.98076 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0ae07dc-d3f4-3fd2-bd8a-a52fb43840ad | -7.36029 | -43.83302 | 2025-08-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3eb6f06e-fda3-39fc-bde0-5ce4b5586c3d | -11.7421 | -44.9453 | 2025-08-16 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdc7ebe4-a1ac-3866-a237-b2d074f3e5c4 | -7.4207 | -44.91322 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0a90278-c7e7-327d-bd9c-a895b3cc5eab | -14.21437 | -44.78245 | 2025-08-16 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 405a0391-0afc-3fb5-9abf-8b95654aed40 | -12.58596 | -46.93974 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b783c5d1-5fe9-3527-b27f-c6f3003456a9 | -12.5428 | -46.9526 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 91af096f-9996-3546-bb87-ba66564617e1 | -12.48852 | -47.49764 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c9e949f-ac97-378d-b895-7f23bf04ebd6 | -11.25457 | -50.47892 | 2025-08-16 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 674140c1-4a6b-3303-8232-a84003e83143 | -9.70652 | -46.27029 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b410684-cc53-32c6-9eb8-0bf7beb30571 | -13.6133 | -46.90796 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6a330bc-ac6c-3aa7-8839-1ff5abc78ad3 | -13.42362 | -43.67715 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 924d0de8-c8b2-3512-a6bd-4880be1f1944 | -8.18976 | -45.02617 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29a75a33-a937-3eae-ab3e-caad58452204 | -12.62015 | -46.93407 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bd404a31-d365-3073-b105-eebdaa8eb553 | -10.18141 | -49.51184 | 2025-08-16 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09f9ada4-2287-3b25-87c9-61c4c6de8c79 | -13.87152 | -45.55251 | 2025-08-16 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ed3955d-666c-3e08-8ae0-9b0f9684643c | -13.58455 | -46.96637 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9da438b4-a124-39e1-8916-d01e3d699cce | -12.60355 | -46.96869 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8f9246ff-acba-36e1-8966-574baf8d4eab | -12.59707 | -46.94227 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f16ffc2e-19c1-3cb1-9506-5ce8b3f81f75 | -8.19098 | -45.01935 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87bb826d-28e8-3e1b-8cef-eac68e56ec01 | -12.61456 | -45.22696 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5470ff0d-970c-31ed-8c98-e4e31beb2d04 | -7.39388 | -44.90855 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9eae21d-4a12-31d5-a337-a59a9b67f771 | -11.4185 | -44.6884 | 2025-08-16 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a895ba44-99ed-3d49-a376-43bfd431886d | -12.5292 | -46.96253 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf609a6-965f-3b8c-b51a-c7edeb0906a7 | -12.59571 | -46.91943 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74663502-b5e8-310f-b7c3-d6d4eed7cd50 | -12.59929 | -46.95124 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fccc2837-6c0f-3321-983e-a55c55a067a1 | -12.60343 | -46.93938 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5f6fd160-c19e-3fae-aa9e-c474881dffd4 | -12.60896 | -46.9609 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 453f75dd-16a9-3ef4-8b1c-a07f6e0ae0ed | -12.60011 | -46.94717 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 32caf399-a8ac-30d2-98e0-c8b25e56fd22 | -12.61526 | -46.93811 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ce2bf28b-0a9a-3d20-8dfe-09424b0bc797 | -7.39747 | -44.88872 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d6f5986-0025-3a58-9416-89b7f4723f1c | -8.3481 | -44.95293 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8919c0cf-956c-3ac6-b5f4-73a0b1ec8376 | -8.1791 | -45.02428 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f391529a-d3a0-3d44-a32c-e1d496e6a55e | -12.60788 | -46.91639 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dd626448-2155-3692-8148-dded6150113b | -12.60328 | -46.96027 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5ad94ebb-6b9f-332f-b7d6-fa8874199048 | -12.53556 | -46.9598 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 04bce947-8616-3aa7-a718-5eddaf08a77b | -11.10478 | -38.16029 | 2025-08-16 03:45:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4db08d05-5091-3754-9d48-4bde0de1bfd1 | -12.6002 | -46.95602 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b6a5cdf-114f-3f6a-989b-3030301f6032 | -14.0516 | -46.2921 | 2025-08-16 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11ef8ac3-f244-3d2f-8e4e-a220b3482f8a | -8.18443 | -45.02524 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad354116-7f9a-3a1e-b38e-46bc4f9897cb | -12.60891 | -46.94101 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| aa596ec6-867f-36f9-a5ab-1e675fb5f773 | -12.8219 | -46.0272 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13191cc1-60ba-387b-87b0-452388ab0322 | -10.71283 | -41.86049 | 2025-08-16 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65f9c2b0-6b93-3528-9a17-55d158ac4a9a | -12.53404 | -46.96749 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3d47244f-ff7d-3670-88e3-231a0faba931 | -10.96336 | -49.57072 | 2025-08-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3ca28a9e-59ea-3939-b1a3-6ffdd47ca667 | -13.15796 | -46.87144 | 2025-08-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
