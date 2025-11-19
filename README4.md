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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cc09482-514d-3ec3-aa8f-b2be4c5fb612 | -12.8807 | -50.152 | 2025-11-19 00:35:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba41dbc-8df0-308e-8034-2b7d027190f3 | -3.7499 | -51.819599 | 2025-11-19 00:35:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9989f8bb-d2e9-3802-9257-ff07245f3138 | -5.8367 | -44.915501 | 2025-11-19 00:35:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2ba288a-3804-3ebd-93bd-d60ef7963ec4 | -6.1113 | -42.960999 | 2025-11-19 00:35:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aa05959c-6455-3c23-bfde-b4db28f80072 | 3.6486 | -51.3009 | 2025-11-19 00:35:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f7d53d6a-c962-35cd-a1cf-f403533bad5e | -11.0084 | -49.040501 | 2025-11-19 00:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 060611d5-269c-3451-8b1a-da17a01e6e54 | -12.3475 | -43.971001 | 2025-11-19 00:35:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| abff5d49-70da-34a3-af43-7da90bd28e01 | -10.5442 | -44.119499 | 2025-11-19 00:35:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64ff6e9f-335f-34da-949c-adf9d38d2727 | -12.6028 | -48.876801 | 2025-11-19 00:35:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8772c9c7-f225-3bfc-b6e8-f05d52858e55 | -10.6985 | -44.786499 | 2025-11-19 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0617c5b-5ba1-3e65-a4af-a3e0e7d13f9e | -15.4859 | -43.165298 | 2025-11-19 00:35:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d5265505-8247-3607-8172-e4909a99d9e9 | -13.4973 | -44.348202 | 2025-11-19 00:35:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a80385a-b677-3035-8d09-b735f1fcbc2d | -13.4985 | -44.5341 | 2025-11-19 00:35:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06e9c8bb-2bad-3ba5-b5a6-deb408b11946 | -8.8747 | -47.3316 | 2025-11-19 00:35:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9696992d-1f3e-3a40-be7a-6b82bcadf5fd | -1.3773 | -45.793201 | 2025-11-19 00:35:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23190f42-5926-3b9c-97a6-2affd39c4512 | -15.4842 | -43.157902 | 2025-11-19 00:35:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3ff33b57-ab61-33bc-88c3-59cc20f03362 | -6.3449 | -44.217999 | 2025-11-19 00:35:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 791c991c-739c-34e2-876a-b358a4a34940 | -4.6785 | -43.2276 | 2025-11-19 00:35:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f425a9ba-87f2-352c-bfce-811e8062a68c | -6.3111 | -43.8092 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 338060bb-e3d5-3d74-8eff-b46538591a22 | -11.8263 | -44.620602 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2eebfaa6-565f-3946-bac0-37a77b5b7bde | -12.698 | -45.3694 | 2025-11-19 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7064895-74ea-375e-ae7c-279f4262f9b2 | -10.7489 | -44.915699 | 2025-11-19 00:35:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83d63a65-14ee-385d-a086-a64cef11caf9 | -13.4874 | -44.395302 | 2025-11-19 00:35:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04c12105-9c22-3152-be0c-050e5d52d455 | -5.6278 | -45.171101 | 2025-11-19 00:35:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63701cf1-1a08-30d5-9402-15aa3df25fe6 | -2.9418 | -51.8344 | 2025-11-19 00:35:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cdc13af-8c35-3627-a931-8b59afa8993a | -10.0624 | -47.905899 | 2025-11-19 00:35:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e3900a2-fcdf-336f-8983-e0aeecad8e28 | -5.0498 | -45.125999 | 2025-11-19 00:35:00 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c85aa4c-e82b-3a4b-928a-d365dd745907 | -5.0455 | -43.604 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da0604a2-611f-32b0-8cb0-e0b6f7890fee | -11.0276 | -43.8895 | 2025-11-19 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51018992-9907-3bcc-80b4-dcd377f47a67 | -1.6843 | -53.175201 | 2025-11-19 00:35:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a3db89-d088-32e1-844f-bf66ed7d1b03 | -7.8297 | -42.157799 | 2025-11-19 00:35:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b461f45-88ff-337b-afe1-8a167b52384a | -12.4058 | -43.1576 | 2025-11-19 00:35:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ca48c20b-dc43-33ea-8d6f-4dbae7b8012f | -11.6647 | -44.7253 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb5c295f-a459-3ac2-b103-a2305ce0aa93 | -11.8003 | -44.597 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf5418f0-097c-3e29-9841-f389725fa0bf | -11.0293 | -43.8969 | 2025-11-19 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3942ad2b-37c7-3c2e-b9da-a1e7a2527a6d | -8.0321 | -40.941002 | 2025-11-19 00:35:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 952a9033-0590-3776-a159-b77abb0663df | -5.3545 | -43.032902 | 2025-11-19 00:35:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 8a849d2a-9db9-3323-ba2e-f46ca3a3b7ce | -11.7872 | -44.629799 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a361002-7b9b-3aa7-a2cd-d1b420341907 | -11.5157 | -44.8857 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaca9e22-1da5-3319-a4fb-89cff27f1b1d | -12.4303 | -47.881901 | 2025-11-19 00:35:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27524042-8153-3773-865c-04ba30d4aa03 | -2.5389 | -45.374901 | 2025-11-19 00:35:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5385b6e4-6a1a-38f3-a47b-eba69b316740 | -10.1 | -47.889801 | 2025-11-19 00:35:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5b49607-a4fc-3c86-a99f-8e31b4e5556f | -11.6669 | -47.959702 | 2025-11-19 00:35:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a01356e-478c-3a42-a214-ca1f8572f788 | -3.2501 | -43.027 | 2025-11-19 00:35:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e863873-985c-32da-a2a4-0104e98bcf09 | -10.0983 | -47.882301 | 2025-11-19 00:35:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1198bd07-9f5a-394b-9064-a30f74dc008e | -6.7156 | -42.117001 | 2025-11-19 00:35:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2855a5b0-17ee-38df-a39d-91009cf884a8 | -10.3446 | -48.911999 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d379423-7b42-3d3d-a668-9cd18e2c171b | -13.0626 | -42.1325 | 2025-11-19 00:35:00 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bac7cc07-3911-3127-86d1-8c0f982e32a0 | -13.0646 | -42.1408 | 2025-11-19 00:35:00 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7401b08a-4229-3655-aad2-ebf9df0afeb1 | -4.1133 | -49.095699 | 2025-11-19 00:35:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f33a537-1f3c-3999-8a48-5cc564f9b6df | -7.8274 | -42.1483 | 2025-11-19 00:35:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f97f5e40-66cf-347c-aec6-4d69c58115a2 | -5.169 | -42.684299 | 2025-11-19 00:35:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9feac7b0-05f3-3ebe-b78e-0b5cadd0338f | -5.4446 | -42.759399 | 2025-11-19 00:35:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 14de57fe-45f6-34a3-993e-8191280930b7 | -6.7165 | -42.510601 | 2025-11-19 00:35:00 | METOP-C | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fc2453a-41c1-3648-a804-b545767c7c38 | -8.9106 | -40.4375 | 2025-11-19 00:35:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a0f947df-fdb1-3e45-92d3-917b9a1e5bb1 | -11.9319 | -44.8111 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1646fda-9b41-3279-8283-9dff633b68e5 | -5.0515 | -45.133301 | 2025-11-19 00:35:00 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87dc2775-7eff-3f96-a323-156da741430b | -6.1232 | -42.967602 | 2025-11-19 00:35:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57f1eadd-912c-3e20-aa34-05961513bd5f | -5.2387 | -43.988602 | 2025-11-19 00:35:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9835dcb9-14fc-3caa-8087-bd981f4bcacd | -12.1469 | -45.166302 | 2025-11-19 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd3482c9-a553-39e1-bec8-69652ace9012 | -10.554 | -44.117199 | 2025-11-19 00:35:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28f74a8b-a157-3bd8-a137-85fd53b93dde | -11.815 | -44.615898 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2d0dbb3-e64e-35a6-9838-3708d03fede1 | -11.6198 | -43.9049 | 2025-11-19 00:35:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d5a7c4e-6a3f-3fb4-8fa9-f3807e2a5194 | -5.7915 | -42.569 | 2025-11-19 00:35:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85131ca1-2cbe-3d86-9edb-d4cbac9948c0 | -12.1454 | -45.159302 | 2025-11-19 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b81d7490-8f84-3a60-9b60-f3faf21016d4 | -4.9241 | -48.174 | 2025-11-19 00:35:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 584a3afb-d63b-30de-af0e-85630bddcd18 | -5.7152 | -42.7258 | 2025-11-19 00:35:00 | METOP-C | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 545ab0b5-3244-34a9-b8a8-add8af663654 | -9.3881 | -48.436501 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b983d33-876f-3cac-9669-0dd35c282bd5 | -5.0337 | -43.597801 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b113266f-7c6e-3917-b2a5-577bb53d44ca | -6.3152 | -43.7827 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30bb7dd0-eac2-38a6-8e1b-a85b7a7147e3 | -4.6666 | -43.220901 | 2025-11-19 00:35:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d17b272-f6ee-3efc-b77f-6dd6d20af909 | -12.7659 | -45.441898 | 2025-11-19 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1acd764-4799-3534-9cc3-1cb205dd336f | -10.3464 | -48.9203 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0e2872c-b252-311c-a120-906df809e93e | 3.6521 | -51.285702 | 2025-11-19 00:35:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1489cc7c-0a6d-3144-b77f-24133e964378 | -11.5173 | -44.8927 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a01d87d3-fcd9-38d2-aec9-34ded9ca634f | -4.9828 | -44.748699 | 2025-11-19 00:35:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e684037a-5f86-3611-878a-3493c3ee7825 | -6.7188 | -42.519901 | 2025-11-19 00:35:00 | METOP-C | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6564432-00cd-33b8-aca9-918acd9bdf2a | -5.3448 | -43.035099 | 2025-11-19 00:35:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 865e870e-4e64-3c3c-87e1-92bf146b7cc4 | -3.3614 | -43.502102 | 2025-11-19 00:35:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5a4ef79-e918-3eaf-a442-cd496b4c0be9 | -11.5103 | -44.997501 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad6b0bee-d331-3f89-b98f-09f067c74e35 | -10.3482 | -48.9286 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b790b5b-f76c-32c3-b8bc-2db08ce6688e | -4.2702 | -42.109402 | 2025-11-19 00:35:00 | METOP-C | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 215808b7-78f6-3d24-9689-a0d8c9710df6 | -11.6197 | -44.979599 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efbf8ca0-4404-341c-b22c-6d28ec89aa2b | -5.0046 | -50.9091 | 2025-11-19 00:35:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ae393f-9b26-3d0e-8996-bd8c4cf80942 | -5.3524 | -43.0238 | 2025-11-19 00:35:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 34776339-291f-3fc8-9793-e57e49c6d959 | -13.5001 | -44.5411 | 2025-11-19 00:35:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 009272bd-a86e-3d32-a492-611dc280e73b | -6.313 | -43.8172 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41477351-bcc6-3e9e-97aa-d59328d82361 | -4.9926 | -44.746498 | 2025-11-19 00:35:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44a5fe79-2ff8-3be8-89c0-81e2cecd63ea | -0.9022 | -47.9445 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c1afce-5f71-3eb4-99f1-b2a1274451b3 | -11.7938 | -44.6134 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9febef5f-61ab-30e4-a819-c67ca05c4743 | -12.427 | -44.450401 | 2025-11-19 00:35:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 309716d5-c5fe-3b68-b508-9ab933fb9064 | -1.3581 | -47.009701 | 2025-11-19 00:35:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e0059f-7f62-3dae-8da8-629a62266307 | -4.6722 | -43.2005 | 2025-11-19 00:35:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef453ae6-7cc2-3228-abcd-82efb47d8339 | -12.3128 | -47.907799 | 2025-11-19 00:35:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3583b4f2-f16c-3473-974f-d4dcbd96a279 | -2.8542 | -45.445202 | 2025-11-19 00:35:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e65f92c-2443-397c-960a-b04a8a7dd65b | -4.6058 | -48.4515 | 2025-11-19 00:35:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1898d51c-05f2-3927-979f-dd1e92bdd467 | -11.8036 | -44.611099 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bed499b-0c63-33e3-b18b-b0c9f5b2b4a4 | -8.9204 | -40.435101 | 2025-11-19 00:35:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 483ae3aa-1493-3f40-ba0d-e6b4edf0f9be | -11.7856 | -44.622799 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09720c25-291d-3cf4-8598-2623da0a413d | -12.1387 | -45.175598 | 2025-11-19 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
