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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a963edf1-2898-3371-a944-0a43432c1947 | -4.48059 | -47.67213 | 2025-08-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 232f6329-2ff0-3ace-b317-2754e44c5bd2 | -7.31608 | -44.68977 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f10684e-0798-37b2-96b3-7e719467e4e0 | -4.78469 | -45.33178 | 2025-08-15 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccbcae89-4245-3637-b5bf-c3d31dffe10b | -5.27741 | -45.17253 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4166d4f4-9840-3993-81b5-a924e28f1004 | -5.31995 | -45.22115 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55a97f6d-47fb-37c3-83fb-0eef1a15d344 | -4.59846 | -43.31526 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d69707c5-feb0-37ee-bbf7-7c6a43f64078 | -6.22338 | -43.34012 | 2025-08-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3bd5ac09-eacd-30f3-8645-dc7565fe2bba | -8.30469 | -45.01192 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e914c4e6-ac83-3286-a53a-120c24f780d1 | -7.37753 | -44.89624 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 918cdd09-b428-3ab4-9ce8-674a21646f47 | -12.24264 | -38.82209 | 2025-08-15 04:02:00 | NOAA-21 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9faf6c0f-e51e-3b49-aacd-2dab82c38be5 | -5.53961 | -42.66286 | 2025-08-15 04:02:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3250f93a-8d8a-3933-a639-d5d397ad4a7e | -10.5371 | -42.54866 | 2025-08-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ed6882b1-cc67-321e-a34c-e0001152ad83 | -9.02746 | -40.5239 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e150323-37c2-32fc-84fa-fc898aa1d17c | -8.31631 | -45.01391 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f95242be-9612-39d9-8e66-3519111911b5 | -5.61314 | -43.46901 | 2025-08-15 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b74ec39f-239f-32bc-ac9f-bceadeff04b8 | -11.74142 | -43.37609 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8875ca18-06ef-3ba9-8670-e761a0addd8b | -5.23365 | -43.19334 | 2025-08-15 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 130c7010-88f7-37c2-8476-116bdf5da177 | -5.23001 | -43.19273 | 2025-08-15 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d4ecce2-f326-3e00-a45c-5b899007aea3 | -9.028 | -40.52043 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cccb3b2-c0a6-3eb5-b7e1-9851d0f5536f | -5.37284 | -41.24314 | 2025-08-15 04:02:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe8ddfab-cef9-3e77-99c1-3acb7613f9dc | -8.3373 | -40.98009 | 2025-08-15 04:02:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1b0c3b8-af38-370b-a98a-b334a64bf28b | -10.53989 | -42.55285 | 2025-08-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4410398f-e722-3610-82a3-d814c595fbcc | -4.0681 | -47.98348 | 2025-08-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05513c38-c802-3720-af17-0051d09d82df | -7.38633 | -44.87038 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ee8b145-7426-354c-9ae3-b2598959ad6d | -11.91716 | -43.43942 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 408b41c4-7b7f-3251-9db1-32f97ae9e601 | -5.37341 | -41.23957 | 2025-08-15 04:02:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50d2c1e3-a47f-38c2-af29-6ff039987b64 | -11.02737 | -45.06651 | 2025-08-15 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c61fc36c-2345-3ee1-a4ea-224eefacd0b9 | -9.83718 | -47.80722 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35147dd3-07c8-3aae-be0d-56e8b82763ed | -4.29707 | -48.06135 | 2025-08-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ef8aaff-3d3c-3aa4-b66f-33f3a1f018e1 | -9.03185 | -40.51747 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5729f87-e6cc-3257-8b98-a8dce8dce996 | -7.61283 | -45.20159 | 2025-08-15 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b536350a-9ae6-3129-a7e7-ac8b717af3a4 | -5.76089 | -46.66715 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0e9c6602-5841-39ab-b8bc-6b4e20790d5f | -8.31937 | -45.01949 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23e6025e-fa78-3a1a-85d5-bd12af0fc44f | -7.39879 | -44.86774 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd8d3494-b5e9-36f9-a9a3-363d79708eb1 | -10.86222 | -48.49377 | 2025-08-15 04:02:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e09871c2-75b3-3098-b6a7-d203b40892e8 | -8.30937 | -45.00773 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2a98b06-dced-3376-9be7-39c716277ce0 | -5.76461 | -46.67242 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ca299ca9-c649-3b31-96d1-21b1fdacad46 | -8.51244 | -43.32645 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 85ce019a-4814-34c0-8178-d583f6092f09 | -6.9471 | -44.55385 | 2025-08-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5b2723f-bfd4-3b44-9b40-51a2e4e315cc | -17.56917 | -52.53149 | 2025-08-15 04:04:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c44af968-5e7c-33fc-a5a6-67f49c5a93c5 | -11.77699 | -47.39805 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bea2aa6a-51c7-3c04-ace4-6a22f8eaa353 | -12.59426 | -46.96944 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 596737bc-670b-39af-a16e-1cf5e84306ad | -12.3513 | -49.90898 | 2025-08-15 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1d4eae9-7ad0-303e-b171-eed93349d2ef | -13.46768 | -43.75545 | 2025-08-15 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b332a06e-bf40-3b65-b082-3ffc20f8f12d | -15.93112 | -48.15633 | 2025-08-15 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 7173b4ea-8125-3189-bd7d-a58f4ecfa27d | -15.39872 | -46.59404 | 2025-08-15 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b425c0f7-a2ec-3fe8-b107-44c0e5b77096 | -12.59026 | -46.96817 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2636dd0c-a814-3381-a405-5b55792d40b6 | -19.10443 | -40.25371 | 2025-08-15 04:04:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1520aefd-e416-3b7f-88bd-031df273dd56 | -16.38041 | -50.89539 | 2025-08-15 04:04:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b0cdca3-1337-346f-af8a-8c555e1f1967 | -14.23773 | -44.5813 | 2025-08-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 149fbeaa-6207-3339-8f28-0229c534c0ba | -11.34651 | -55.40524 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9008145d-c244-3ff4-9bcb-20a9ae0ba0e0 | -15.32834 | -51.51433 | 2025-08-15 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56132e91-335b-3f76-855f-756eec1b9139 | -18.6374 | -49.08711 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9986e4ac-00f7-361a-a60d-6eedbd5cb6a9 | -11.36035 | -55.42735 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ae69b4e9-e8d7-3c4e-a853-645387ae11e5 | -15.66723 | -56.38797 | 2025-08-15 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73c56668-29a7-3760-9138-846f6c3ba293 | -15.39159 | -55.78162 | 2025-08-15 04:04:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3f8af60e-d9f5-3c34-aee4-d6c31d45f661 | -19.03242 | -44.64906 | 2025-08-15 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87d7911f-82b3-3b40-b976-89e333e29080 | -12.58611 | -46.94417 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e6519157-0089-3033-b784-cea0ca161ece | -12.3563 | -49.90995 | 2025-08-15 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5071f9b7-32c2-38bb-a3eb-beb40fdacd4f | -12.7625 | -44.41033 | 2025-08-15 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 86eec2e6-c523-3b2a-aae2-a1e7c02a539b | -14.31713 | -48.64833 | 2025-08-15 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c1aca38-538b-322d-bcd3-7a525a5c6d04 | -16.30365 | -52.92562 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fb2e352e-00e2-3cfa-b1b5-cf540ab3f116 | -11.34901 | -55.42818 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3f84ec21-cf28-3cf0-9444-6cfae34328eb | -11.34053 | -55.4159 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 89848148-54b7-3c91-9855-99ae65be3d73 | -18.30128 | -49.55683 | 2025-08-15 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ce68c73d-7f08-328a-9052-0b66414ebb4e | -15.67457 | -56.38153 | 2025-08-15 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c3244f1-4608-3ec7-b4f0-00f210f87e04 | -16.6816 | -41.35287 | 2025-08-15 04:04:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5bf9b04c-0a54-39ec-a65a-2e9df61f6a2c | -15.23471 | -47.62438 | 2025-08-15 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b68b5f1e-c6fe-3035-9f43-ff7247f8265f | -14.06929 | -46.32012 | 2025-08-15 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c37cd990-cb2d-3bb4-b0b4-c9c549b3f2f7 | -11.45279 | -47.33661 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cb72d51-d3e5-3122-83ac-12df49a5380b | -14.06412 | -46.30421 | 2025-08-15 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d04c8df-f220-3f34-b85c-87a5f1c9607c | -19.67357 | -44.59948 | 2025-08-15 04:04:00 | NOAA-21 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9f46134d-72d9-3825-943e-24da13765680 | -19.37226 | -42.93051 | 2025-08-15 04:04:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 34f574df-6523-35e1-8e64-e05ce494ff7c | -11.55063 | -47.32364 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f9f47b7-51bd-3065-95ec-7ccf15d5881d | -11.55135 | -47.3196 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea085095-c60e-33d7-8088-6e393a40a2fa | -15.9274 | -44.79797 | 2025-08-15 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 893b331d-14bd-31af-81a2-0fe60656be6d | -19.37169 | -42.93415 | 2025-08-15 04:04:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6bb16443-8dc1-3ff9-927c-e4cd5936bc3f | -12.58687 | -46.96346 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e76f7879-e47c-3050-a40a-c866716d0df4 | -16.3934 | -50.91167 | 2025-08-15 04:04:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15d7d086-7dc5-3438-8350-e2e1ca4a07ff | -12.7576 | -44.41789 | 2025-08-15 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1d3fdda-c3dc-3243-a8ab-a41d9b5d51ae | -11.3477 | -55.41701 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8a7f75aa-fb16-3326-a9b2-03161fc9cc4a | -18.53564 | -45.45168 | 2025-08-15 04:04:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5586678-4db6-3895-88d0-0280e604c434 | -12.2625 | -48.78736 | 2025-08-15 04:04:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fcd46447-95d5-3158-bb76-43c10437f322 | -16.69292 | -41.01306 | 2025-08-15 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a6c820b2-ce39-34a8-9a6c-a7b27c4d0a81 | -16.29983 | -52.92892 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e4a29e69-6d25-3019-94ed-3050252b5e4d | -12.79116 | -45.9679 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1553e04b-c566-3f37-9526-eee363436cb8 | -11.54954 | -47.25639 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16d0db49-cbf4-39c8-8786-0711b0369238 | -12.12491 | -45.1403 | 2025-08-15 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d2ef2af-3020-30a7-8ec0-42b1764aff78 | -16.30459 | -52.92107 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5fed5e65-5a43-3856-a941-cb569b695d81 | -12.59967 | -46.96283 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb0ff6d-1754-3dd1-b63b-aa8117f38dc9 | -15.89737 | -50.17277 | 2025-08-15 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d9c9ed8-d278-3ea5-a0db-9605da599e9d | -12.68302 | -44.95407 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e36ac61-dd06-39c3-b975-806272753f05 | -13.12206 | -46.85093 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b56e5292-ce89-3753-baca-ae2bf2fbd3f6 | -18.2986 | -49.54693 | 2025-08-15 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5183d26f-6e5d-32ec-8f80-471238586cbd | -17.64771 | -44.49818 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b7e3000b-fa4d-3182-99cd-f644dfe223a5 | -12.42151 | -43.49169 | 2025-08-15 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1cabbcdf-0024-34e9-bac3-1919a8b75d7a | -17.05582 | -51.79607 | 2025-08-15 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e360ea5a-ebe7-3b09-9880-498b93cfd110 | -13.11805 | -46.85012 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f4c7fcd-7164-3239-a9f8-92ad104842e5 | -13.31185 | -45.23464 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 87eb9103-0ab8-3b32-88a3-87f492413b0f | -14.5685 | -52.04564 | 2025-08-15 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
