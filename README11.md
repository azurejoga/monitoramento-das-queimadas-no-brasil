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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 069bffdf-0ddc-3b7c-8935-8ea8a40e9aca | -23.52145 | -46.97618 | 2025-11-19 04:06:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ec5cc3c4-626b-3039-b04d-160649c0ccad | 3.6659 | -51.29487 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abd303cf-2c84-3462-94f4-2d8560b232a2 | -2.29338 | -45.74143 | 2025-11-19 04:27:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 933d9e0b-b152-340f-bc93-c99c36834524 | -3.35483 | -43.49908 | 2025-11-19 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a729230c-8316-38f6-b60a-59c786dfa81b | -2.22318 | -44.81552 | 2025-11-19 04:27:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 858791c0-24c4-3cee-bc1d-bcad1817975a | -3.59714 | -40.9677 | 2025-11-19 04:27:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40f39950-8c51-3f71-9000-055903a9a288 | -0.98559 | -52.43708 | 2025-11-19 04:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8a3b188-b788-3a15-8e04-2feb771cf03f | -2.30774 | -46.08131 | 2025-11-19 04:27:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f36f165-d3f4-3a56-885e-47d742efc3a6 | -1.1512 | -54.10445 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bc2f302-693c-37de-9c42-09a93f7b75ba | -3.35196 | -43.4948 | 2025-11-19 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 939902f3-146f-34fa-bcc4-2446464ac0bd | -0.74457 | -47.86525 | 2025-11-19 04:27:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4e2a93-1946-3e1d-bddb-636b99baaa5c | -2.82017 | -49.12923 | 2025-11-19 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 384ae724-f220-39ea-b9de-efe2e66aa26b | -1.15174 | -54.10122 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dff061c-62fc-3ba3-a2ae-c03ca36c3ec4 | -3.35887 | -43.49583 | 2025-11-19 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c789fbba-927a-3ca5-9040-9282e6d4c817 | -1.22717 | -46.20673 | 2025-11-19 04:27:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aa6df3b-3abc-320a-99a1-a3807617e415 | 3.66565 | -51.29633 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7469bfdc-e310-3276-9182-6c4bc6032555 | -1.48413 | -54.19994 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e89ebf55-3240-32f8-b7fc-bf75f16106f8 | 3.65542 | -51.29273 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d9b402a-bb0d-36b6-8fb8-bdea781357dd | -2.98178 | -41.76393 | 2025-11-19 04:27:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 10893b3f-b0a9-36c5-a855-2c38c5bc3d94 | -2.8239 | -49.12979 | 2025-11-19 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db23e089-2a3f-3569-89e9-1d81f4c9efee | -2.97127 | -41.75776 | 2025-11-19 04:27:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a82741a-ad31-3aee-8d9a-9b295f720edb | -0.92078 | -48.06376 | 2025-11-19 04:27:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e21bc3f-5bb9-38e2-a381-51b626fd2232 | -1.14825 | -54.10038 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67f680af-780b-3129-964f-7c4b4421b07c | -1.14774 | -54.10364 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8639dc0-a1af-316e-9e2d-99a37e4c7cc8 | -3.01951 | -44.46018 | 2025-11-19 04:27:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f1a350b-af7a-37cc-a7cc-04d3179e1801 | 3.64519 | -51.28915 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa27a791-f3b7-34c9-934e-cceb41df544c | -3.35542 | -43.49532 | 2025-11-19 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86ca3fe7-b71c-3879-b2cb-a9a369412e50 | -2.22263 | -44.81898 | 2025-11-19 04:27:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71338861-5ffa-36fc-8055-53a418331e56 | -2.28727 | -46.52412 | 2025-11-19 04:27:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b63c4ae-c550-3152-801c-32db8a73ca16 | -3.02732 | -44.45418 | 2025-11-19 04:27:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25801321-1d44-3e1b-acac-6d8bc8876393 | -2.21985 | -44.815 | 2025-11-19 04:27:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2a002c39-f74b-32be-a4f0-aa93c7191d04 | -0.92187 | -48.0624 | 2025-11-19 04:27:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b160d9f-b387-3601-8878-1786b18d535a | 3.66488 | -51.29131 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d8d26e-1489-340e-a111-fe06c6894bb2 | -3.02396 | -44.45366 | 2025-11-19 04:27:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 70f24dde-2430-3d0b-8114-9f3ed0543daf | -0.72148 | -52.37638 | 2025-11-19 04:27:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c96c5149-7a75-33e8-9dcc-aedc5aacb4b7 | 3.64672 | -51.29918 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83069d4a-381e-3dbe-abda-5f588cd89896 | 0.91035 | -51.10408 | 2025-11-19 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd65924d-c0c1-3f11-b15e-3d4b2a9bf1f1 | -0.99035 | -52.43784 | 2025-11-19 04:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73a94d1c-8771-3345-9145-44849dc08be7 | -3.02341 | -44.45718 | 2025-11-19 04:27:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbbabc05-97b4-3cfb-b5b9-f12452cd8fc4 | 3.64595 | -51.29416 | 2025-11-19 04:27:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e253804-95c7-3499-bfa8-9d2857a0709e | -1.37788 | -45.79632 | 2025-11-19 04:27:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043a72f4-8ad8-38c3-9ac5-e71082412575 | -3.4577 | -40.52122 | 2025-11-19 04:27:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ff22a70-d1f6-3ac0-8b11-a7ca0029a976 | -2.26313 | -46.5458 | 2025-11-19 04:27:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b280d2a-dd0b-33dc-a13c-efc2589e4d92 | -2.28671 | -46.52768 | 2025-11-19 04:27:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af4bdc9a-f78d-3295-9287-9883d8e04d04 | -3.2208 | -46.12518 | 2025-11-19 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b11412e-68e8-3aed-a8ea-a5bb2bc8a322 | 0.18752 | -51.01115 | 2025-11-19 04:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fe8083b-e1af-3199-a736-fb62fa07fa54 | -2.22372 | -44.81206 | 2025-11-19 04:27:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fd27a125-28b6-3fdf-8bae-9ccd0da67efe | -2.29007 | -46.5282 | 2025-11-19 04:27:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ee387452-e1de-3f4f-974e-4761e17e3acd | -1.15358 | -54.10121 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ffd772-b427-32a4-93f3-bf9786d62a18 | -0.7713 | -52.49219 | 2025-11-19 04:27:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09ac8bcd-04b7-37de-a974-eb56e9a41a74 | -2.82089 | -49.12483 | 2025-11-19 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91a07a1-6a83-3ee8-98df-4d6152adfe47 | -1.48944 | -54.20094 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 017124d5-66fd-34ae-af27-7f1415918c7a | -1.38121 | -45.79684 | 2025-11-19 04:27:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 11ced551-5b26-383e-81fe-5bbe7c40bb6c | -3.35137 | -43.49856 | 2025-11-19 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39435b81-ae83-3e33-8e6f-4fe0e48bae8a | -3.46185 | -40.52124 | 2025-11-19 04:27:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7e0f290-a92c-3291-af63-cceed09e545c | -3.25071 | -43.29004 | 2025-11-19 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d73ef12d-d6b5-32db-9010-73372236885c | -2.85286 | -46.65645 | 2025-11-19 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e6c24c8-6703-33a5-ae3c-e226edc95c7c | -3.22413 | -46.12571 | 2025-11-19 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fca9c69-b255-3ff9-8b3c-d7a5f1428c74 | -0.98981 | -52.44 | 2025-11-19 04:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77583ee9-a539-3717-b09a-e447d52c759e | -2.29063 | -46.52465 | 2025-11-19 04:27:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9bfdb4ca-9bd7-3027-9635-260478bd8751 | -3.601 | -40.96891 | 2025-11-19 04:27:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 079a131e-f2c1-3e59-b870-84d5bbb3265b | -1.09459 | -54.12817 | 2025-11-19 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9e3def5-f6cb-3f0e-920e-51631f1783c6 | -6.94227 | -39.62944 | 2025-11-19 04:29:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aec1afc8-3914-3c05-b9b9-81ab1ab85e13 | -5.79243 | -42.56938 | 2025-11-19 04:29:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e697abe-51df-383a-b1aa-803ee3465129 | -5.7949 | -42.56788 | 2025-11-19 04:29:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1b652e0c-a739-3d53-a8c2-4100795eb69c | -8.87909 | -47.32532 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a68e43a0-8b5b-3cd0-a467-55d76d04f71d | -7.48744 | -42.75729 | 2025-11-19 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fe8825b-0d89-3ebd-9746-7fb5ad974196 | -3.01764 | -49.43402 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c004d1bf-0c03-3d6b-a05c-f17b8ca4576e | -5.7961 | -42.57007 | 2025-11-19 04:29:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 795260c8-0989-34bc-8b0b-2ec8c63fc915 | -4.58492 | -44.07117 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21a9cfb8-24a8-349e-a202-32603722b6fc | -7.44321 | -45.19722 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d652c40a-973e-351d-a1cb-6fc28cb8235b | -6.71866 | -42.12652 | 2025-11-19 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| b7f44325-9929-37ac-a9cc-17f78f356c5f | -5.34635 | -45.42117 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5ddb835-e3e9-330c-ba0d-35b92a507851 | -5.23244 | -49.57624 | 2025-11-19 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 185b779c-1d97-3b1d-8c38-cdda972a9b60 | -7.44274 | -45.19334 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0189c87-8e54-3f9d-9d6e-8b1bd9d42d78 | -7.45388 | -45.19522 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04ec6895-129a-335f-a29f-ff3e4cd44680 | -8.12304 | -47.59036 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fb1eeb8-02e6-3589-b4f0-358581339eef | -4.14563 | -46.78708 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4db05b9d-0432-3606-a9aa-c058d85bf85e | -8.91766 | -40.4393 | 2025-11-19 04:29:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f89d725-a6e4-3e7c-b0e2-c971b0696cf5 | -7.44941 | -45.20182 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0699cd41-e1ca-3b49-8a94-87bd05d01a7f | -2.21487 | -53.63948 | 2025-11-19 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c62adf4-7b3e-37b9-b93b-a4596840e2fc | -9.33674 | -42.44311 | 2025-11-19 04:29:00 | NPP-375D | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 38d6c5c5-9a09-3c6d-a49f-212fbb0d79a8 | -4.72585 | -45.66505 | 2025-11-19 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2756c77-330d-3d15-87bd-18ae9f03f3d9 | -3.02217 | -49.43005 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 46367f9b-90b8-3d14-8cd0-5857707e4060 | -4.99089 | -44.75401 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea59f3cd-6f42-34dc-83b3-1491ea3cabe1 | -7.18388 | -44.63618 | 2025-11-19 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6703ef7e-f5c5-3edd-bbe0-b8d6d51b9c6c | -5.71741 | -42.73912 | 2025-11-19 04:29:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8c548b0-010b-359a-b563-feac15a57e08 | -4.75554 | -45.90304 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94914927-5b1e-3a5e-9012-f4ea787c316e | -4.98978 | -44.76109 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0c362d1-b98b-3caf-8396-140176cb77c6 | -8.38375 | -44.02816 | 2025-11-19 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 861102da-2681-3d51-a5d5-7938a7d5f4a5 | -4.98642 | -44.76057 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2515ad4b-74fd-3808-a1fd-faed665212cc | -3.35896 | -48.39298 | 2025-11-19 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7a0f808-4a8d-3d2b-887f-3b0816c1b583 | -7.85737 | -39.81419 | 2025-11-19 04:29:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3cefe5df-e4b8-3145-81cc-69d9828de281 | -2.28518 | -53.64462 | 2025-11-19 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c2acff-91d6-3321-b9d3-a5eaf24ab865 | -7.61332 | -45.71815 | 2025-11-19 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d112cf9-ff94-3d56-b264-cd7cfdf02373 | -4.5815 | -44.07064 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef60ee14-209b-348b-a4b8-1776319732fe | -8.13087 | -47.58436 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 726ec9fd-fd92-3860-8ffd-46aabd9386d4 | -6.43813 | -39.27549 | 2025-11-19 04:29:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9311d444-a795-3da8-805f-9b83bfb0260e | -7.43937 | -45.19281 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab39f822-4866-3d17-90b8-8f022a5a3ba5 | -5.75009 | -45.10706 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
