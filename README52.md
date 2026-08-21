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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2e2f669-1acd-3daa-b913-628f66f2e95e | -13.66808 | -51.80113 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94f99a2e-3ead-35b2-ba14-7916a2a692dd | -13.4452 | -51.81445 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78109fb4-6d11-3382-bf46-7f6b4db01db3 | -12.79639 | -48.40984 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 096ee0b6-445c-34ec-be98-6a9d3a7c2dce | -12.26836 | -43.16187 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e78c4283-2c97-339f-89b3-a9edcfacf610 | -12.26183 | -43.17057 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 53d37a2c-6105-3d23-8e72-9890f9fae30e | -12.75471 | -48.46061 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9595ad96-f7db-3857-8bb7-57ee931a9d6d | -12.85526 | -48.43332 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f7f9cc7-e656-3b47-ab9f-8a02b96ca5d1 | -14.02425 | -58.88725 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac2b92ad-ca43-3dbf-9cf3-9bfa8e99dfe1 | -12.51367 | -54.75341 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a37b96-62c1-37b1-9beb-42adfd4feaec | -11.8185 | -56.60284 | 2026-08-21 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c241470c-fee4-33b9-bdf9-056d635210f9 | -12.27245 | -43.15503 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c8d79daa-7cf4-35a9-ab06-041507ea54d2 | -16.30177 | -53.16774 | 2026-08-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 692a746e-f52c-34df-9045-8c1e14285c9d | -11.21304 | -54.00337 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c08a707-1528-319f-bdb5-1cf5d54919ea | -15.16587 | -48.78363 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21b5b8e5-8884-3ece-b90c-c96b4405ae14 | -11.18159 | -54.02489 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44242e3b-45b4-3bf8-820f-a6e988909216 | -13.25548 | -51.63321 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28a5e82e-071c-3362-a695-8412b9476af8 | -12.25403 | -43.17295 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 657339f8-bb3e-3974-8ded-e0de94f47eed | -14.02045 | -53.68626 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbd81b29-58c6-3989-a7b8-1f02071e2984 | -11.68721 | -54.56654 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b69c4d7f-ea52-3aae-881f-df545e4c1883 | -13.74692 | -51.86195 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1121862c-2455-3f1a-864c-4c76a011a46b | -13.41058 | -54.36232 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 072865cb-18fa-3dcc-a4fb-621af3140d36 | -14.22756 | -51.9152 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47d637a7-15e3-342d-800d-bc026e0f7ff9 | -14.02471 | -58.88813 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 133b3d8d-e887-381e-90eb-58048d6d9f42 | -12.44093 | -43.4039 | 2026-08-21 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 053adb3f-f50d-3d94-8721-a416d2e73a5e | -11.16457 | -54.02207 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a6f1c659-013f-341c-8fd9-c71abaca3fbf | -14.71719 | -47.14296 | 2026-08-21 04:49:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 180ebd8c-0774-3919-a1b4-ca0b7561fa35 | -14.02799 | -58.86708 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba408b0e-029c-3d02-be80-65431f27a5e4 | -16.30066 | -53.17491 | 2026-08-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5688a9f0-365c-3e8a-a952-33253ea37c15 | -11.81469 | -56.6022 | 2026-08-21 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b878edbf-35d1-3d1f-8c4c-aca854a0326a | -11.18621 | -54.018 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34291a7b-cff0-3135-a06b-76101567aa8d | -12.79009 | -48.3992 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92045ba6-abd7-3b58-bd43-fb2449386fa7 | -11.16116 | -54.02151 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a16e91a8-f327-3728-a240-74fc1244aa05 | -11.18122 | -54.00574 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbb3b4dd-a6ad-3673-9fbf-104a9ef8e049 | -13.43739 | -51.79844 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91f784df-8ec4-3a32-b9df-ea669179539d | -14.20546 | -52.87803 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f73463de-238e-3f74-a493-3bbcdedaaa35 | -12.86326 | -48.42643 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85021210-e51c-3883-bc50-92288c0468cb | -13.43351 | -51.80149 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 483d9c53-550b-338b-820c-5ed0231da0ca | -12.51114 | -54.76884 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92f9512-54c3-36ec-93e4-c95775033983 | -13.38321 | -54.38066 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 899d8763-3c47-346b-8035-4096a739072a | -12.75119 | -48.45664 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 292fd343-5073-34f8-8b32-f3c3100a4af0 | -14.51959 | -53.26086 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7899e2e-e930-3151-a301-925483dab2ef | -12.5124 | -54.76113 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d166d56-5377-37d1-8c34-1f62cdfbcb6d | -11.68658 | -54.5704 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 826f4e21-f6c3-3be9-abf6-88d85b4dd393 | -9.4257 | -60.416 | 2026-08-21 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d2103577-4689-33d2-9f36-b49f415500df | -9.4071 | -60.417 | 2026-08-21 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 291.1 |
| 186796d5-8e21-3123-a842-412959c7f763 | -8.3718 | -62.697 | 2026-08-21 04:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 87fd039c-e33e-374e-acc7-e86b8ca3a406 | -10.8169 | -50.9923 | 2026-08-21 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b2ba8756-21a1-3e41-9d73-35a8c0590119 | -3.5406 | -48.1889 | 2026-08-21 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d8bb576c-e9ea-35db-802a-a5face39a4e1 | -7.3605 | -45.791 | 2026-08-21 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e0857a07-7022-3131-a5c4-fe47912012f0 | -7.3603 | -45.8136 | 2026-08-21 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 463a1449-a3ed-31d1-b97b-4166ee1caf79 | -11.175 | -54.001 | 2026-08-21 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 48a7db6d-f528-3591-9fac-9170d66903e0 | -13.3923 | -54.3965 | 2026-08-21 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5dfccd7e-d869-3548-8ca6-edf1aafc84c4 | -6.8203 | -59.4001 | 2026-08-21 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| e66ea17d-8a95-3e44-b033-e03ec014117f | -6.8388 | -59.3993 | 2026-08-21 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| daac8991-210c-3fa8-997d-dbdd9fdd33ee | -9.4259 | -60.3967 | 2026-08-21 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8aaa3446-9bb1-314d-b511-0ecfdee8785d | -7.3791 | -45.8119 | 2026-08-21 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4c168c7f-9736-37fe-ad92-de537d7ee719 | -11.1747 | -54.0216 | 2026-08-21 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 2cc5646b-775d-3cf0-a553-4f97ba7a22a9 | -9.4069 | -60.4362 | 2026-08-21 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b71ea105-8cf4-3a3d-81f9-19437e4262b5 | -13.3926 | -54.3758 | 2026-08-21 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 230.1 |
| effd5917-2e48-32df-b92a-376519f84792 | -6.2156 | -55.6118 | 2026-08-21 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 66953bc0-f96f-3645-9d1c-9f2b33d5b78b | -13.3737 | -54.3572 | 2026-08-21 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| bc19353e-8780-3cc6-9e9d-af5cba224a2f | -13.3734 | -54.3779 | 2026-08-21 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 1d7e259d-ab00-3639-b658-d558905d6173 | -9.4072 | -60.3977 | 2026-08-21 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| fda76280-6fc2-3165-a368-fdf9b86db0c4 | -13.3929 | -54.3551 | 2026-08-21 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 85d968b4-8891-39d6-9995-9d0b788c8efb | -6.2341 | -55.6109 | 2026-08-21 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| eb1b0732-3d88-393a-a207-325b4708d53a | -6.1177 | -59.9069 | 2026-08-21 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8d5476f8-a366-3f6f-86a4-35ab6a0722f9 | -13.4117 | -54.3737 | 2026-08-21 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 18b82659-1907-3722-8e00-b58646367d81 | -19.67446 | -46.04723 | 2026-08-21 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7684e681-2752-3a9d-9ec9-06baa6e9ff82 | -17.99825 | -49.40231 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e350aa0d-5102-3fdf-b435-345694320e05 | -21.49984 | -44.8637 | 2026-08-21 04:51:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1bd8c400-12d4-3f23-a006-a129463640fd | -21.32876 | -43.80717 | 2026-08-21 04:51:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f23c9ec4-3e7e-3e7b-9801-ebbfeea4de12 | -20.44747 | -55.78617 | 2026-08-21 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a8f67d6-3570-3207-8eca-c6d5d6dafb0e | -21.05483 | -55.83696 | 2026-08-21 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36324623-1ba7-36e4-a240-f92fe44002a4 | -19.70338 | -46.91121 | 2026-08-21 04:51:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5374b3eb-d795-357e-bd6b-55d9e2241baf | -19.67508 | -46.04154 | 2026-08-21 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8336ed91-3f15-3ca6-a8bd-36c07c1ef9b7 | -18.98164 | -47.03537 | 2026-08-21 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 01a24edb-5aa7-3b91-a05f-4ddd06bd453f | -21.98771 | -48.16291 | 2026-08-21 04:51:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7468a410-e342-3519-adde-0b9c9d4a73df | -20.83844 | -44.19635 | 2026-08-21 04:51:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 23c019b9-ee06-37e6-a724-49970bc9d0c2 | -20.27086 | -46.75267 | 2026-08-21 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbc30b3f-f760-32c5-a6ef-244035cf52f8 | -18.03703 | -46.46524 | 2026-08-21 04:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f6fdbf-9194-3f20-b4a9-52f6959edde3 | -19.75063 | -57.9788 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3e778870-60ed-3dc3-bb76-fd7ddfb9495c | -19.9106 | -47.38355 | 2026-08-21 04:51:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6204611-2f3c-3e54-bfb4-b34e797b0403 | -19.70281 | -46.91613 | 2026-08-21 04:51:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e02776d-851b-3dac-9d6e-5140e3ed5b12 | -21.10944 | -43.8152 | 2026-08-21 04:51:00 | NOAA-21 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae35616c-52e1-36e0-b45a-58afe46d35c4 | -20.27137 | -46.74819 | 2026-08-21 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06b4f48e-63dc-35f6-b6d9-61e8f4e5caf4 | -19.73674 | -57.97132 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 94e9280b-67b1-3ca7-a399-1855f82bd9a8 | -19.93697 | -46.09637 | 2026-08-21 04:51:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 080138bc-ca84-3438-a5a7-ad30749f66dd | -21.57956 | -43.48236 | 2026-08-21 04:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ead165e0-cec2-37ff-89da-b5c6cdc56d29 | -19.68697 | -42.07283 | 2026-08-21 04:51:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 93b01a1c-0b47-3edb-99e1-5c55263a9de8 | -19.73181 | -57.95616 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 80d66e03-8db0-3b4c-815f-70cb7599ab3d | -19.75657 | -57.98247 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2454a5aa-74ee-3783-b4ba-39e06687e872 | -21.32304 | -43.80622 | 2026-08-21 04:51:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c465d3b1-f8f2-311c-8270-f47b4686bc15 | -20.43642 | -46.49239 | 2026-08-21 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c42bee4-8236-3f14-b77b-b68eabbc9391 | -19.74638 | -57.97574 | 2026-08-21 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3506d574-2c0f-31af-aa42-79ea2960f977 | -17.99571 | -49.39209 | 2026-08-21 04:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42def610-66e0-3287-bdfd-282cb50a30b1 | -20.65908 | -46.1934 | 2026-08-21 04:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 86fa3e5e-8f5e-3582-b27e-6c69b5c43994 | -19.66896 | -46.05233 | 2026-08-21 04:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7a096811-6d7e-3e5a-a5bd-84b333634a86 | -20.8263 | -54.95065 | 2026-08-21 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ff64f9cd-ad7d-3295-9a21-5128081352f6 | -22.62185 | -54.99411 | 2026-08-21 04:51:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 47f21edc-93c9-38a5-9e26-b62f1202158a | -20.25888 | -46.73248 | 2026-08-21 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README53.md)
