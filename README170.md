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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc2f9c53-fb09-37a4-9c1a-3b49bfb8889d | -3.18776 | -50.56501 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dfda0bd5-6b48-3226-9535-f432be906818 | -4.40314 | -41.57627 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1b8424ce-cfb5-3a7a-ac10-b48eba038151 | -5.72733 | -41.74895 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7c7e22dd-6ffb-30e3-8824-f05b880c66df | -4.07065 | -38.31898 | 2026-10-07 16:03:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 11d057ef-40f9-386f-b83f-1eb85cb26005 | -6.83312 | -48.84145 | 2026-10-07 16:03:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a8495772-873b-3130-bd7c-77e2f1a382d6 | -7.28183 | -46.16165 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 374cdbad-17e5-3f06-a9f5-2760f2ade3c6 | -5.14937 | -37.33012 | 2026-10-07 16:03:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 17.0 |
| d51b4a57-6956-3890-a89c-ee14201c75a8 | -7.81721 | -45.5015 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b72dd0a0-0b79-36cf-9e76-0d44a3efc55f | -5.97426 | -46.3919 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2592d90e-147c-3778-a2dc-2b5cd28a8054 | -6.07284 | -45.31093 | 2026-10-07 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fe38e259-3ce0-3668-801b-1a0ba32bf8ac | -3.81164 | -45.39871 | 2026-10-07 16:03:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| df74e7ad-0987-38ab-89ee-9c9bc0d4a9b0 | -6.82847 | -39.54714 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 44.2 |
| efbb62a8-827c-3e54-a133-4dfe6d8ee9a8 | -7.40772 | -44.45184 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d8b45f96-9f1b-3394-9165-b086902b5389 | -0.96162 | -47.66049 | 2026-10-07 16:03:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1fa38223-3415-3920-ae2b-65ade8a22135 | -5.45125 | -42.89768 | 2026-10-07 16:03:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| bab0a06d-6219-368a-9fa0-3afa4ee0fbe1 | -7.77227 | -43.81974 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 43188f9e-f20c-3bcf-ad05-61f35c05ec55 | -6.41975 | -43.46127 | 2026-10-07 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40c4d9cd-585b-3d51-91a3-af4da69bfe4b | -1.88326 | -45.43528 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8bb0cce5-8fa2-3bb4-8b5b-6e188f1d6476 | -7.16085 | -44.01254 | 2026-10-07 16:03:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a9eab6bf-1c46-3c9f-8567-2492e2373049 | -3.11178 | -42.96172 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ba0884d8-fddd-3b3a-84f1-9044dc123105 | -3.89009 | -44.11578 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2d414a49-e0ad-385d-96f3-a595f26a3bbb | -4.52648 | -42.88952 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6094cbd9-2032-326f-9777-93b1f449afd8 | -3.27447 | -50.43389 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 11f00f85-ae91-3e93-afc3-4a9d90406abe | -3.80398 | -40.45936 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| aeec5af2-c0cf-34d9-864b-03e5f243db25 | -7.27448 | -45.56902 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a1843be2-2d5a-3e44-890d-e84be91f106a | -1.42586 | -49.10835 | 2026-10-07 16:03:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9fc277e4-2aa9-3330-b2b7-a2f5e536ad7b | -6.68224 | -44.95736 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d1b933b2-aa2e-3e77-a7bc-bd4c7a619c9d | -5.7895 | -42.65559 | 2026-10-07 16:03:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| a8d7d0de-efec-3d5e-8d95-7ba5599f1549 | -3.18622 | -50.55479 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 3a2c6875-01a8-315d-941f-3fc9c17e0256 | -5.9479 | -46.38642 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2ce9d2f9-e683-38f4-bf7c-688d48c552bf | -7.46291 | -42.99461 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bac1803b-fc80-3ba2-9bff-36527b636806 | -3.68325 | -38.81337 | 2026-10-07 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7db8c39f-8242-3a7e-b29d-27eae45f000f | -6.33397 | -43.82381 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 31ead518-83e2-3afb-aed0-441a47f9cbf7 | -5.89305 | -44.03532 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| b60c41ee-ee72-30ba-b4f9-7c24f6785f90 | -5.9483 | -46.38928 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| adb227e1-86a0-346e-9c18-fc316afa7784 | -3.76115 | -40.04001 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6cf8369a-f24c-3404-9577-ab8601535374 | -5.72272 | -45.16281 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 95985e28-8e17-31bc-8fcd-ee3453be40f1 | -7.87936 | -44.23024 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| b21e71d6-90f6-3b65-b203-95b20ba2a31b | -5.97087 | -40.95251 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 285727bd-2ed2-3e03-9a49-93729dee617e | -7.25753 | -43.51122 | 2026-10-07 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 705e657d-3cf7-3ec3-ad74-8fdcc8e21f35 | -7.75761 | -43.80945 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 69f1b427-6026-3b7f-80ec-8593b08f6c3c | -5.96944 | -43.87141 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 40ac3b42-23b5-3bcb-bc9a-4ac6b73f0fb2 | -3.75778 | -40.04051 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| afaaa86f-a538-3c36-93ee-3bcc7cbd9f77 | -3.20016 | -44.48398 | 2026-10-07 16:03:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| efedc398-951b-3395-acce-c32f18a83091 | -6.00074 | -44.12624 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 046bc5d8-8175-3aa3-b90e-c7aa9022c883 | -6.61759 | -37.88159 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 9e6a5c49-9845-30d8-9981-6abe2cd0b264 | -5.93846 | -46.35559 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ea63106-a1f3-36df-a428-8c443065b39a | -3.42852 | -45.04788 | 2026-10-07 16:03:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 25.3 |
| b72cbf86-d33a-3dc7-8dcf-9d03436aeff1 | -4.36613 | -41.82536 | 2026-10-07 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f3199cc7-f3b2-3b45-ae4c-5bb5038a04f8 | -3.1918 | -50.54888 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c6e202b8-71dd-3389-bfe7-d57d2bc64672 | -7.29218 | -47.28557 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7d66cb4e-9dd6-3a3c-95a6-5309120e3895 | -7.45508 | -43.20179 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4b52342a-839d-3228-8a1d-53bfc38a77c1 | -2.87595 | -43.71093 | 2026-10-07 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a5802f4f-b238-3543-bcd3-b569cf0ad1d3 | -6.93541 | -45.26742 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 287cd231-6b30-3c03-8db5-59695874ea31 | -3.26819 | -50.40885 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 4d097aee-736d-318e-85df-861cdfd3ddc7 | -5.9487 | -46.3921 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 501acd0c-6e1f-3f36-9b63-1136ffbc10ee | -3.90031 | -44.09885 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 342ae3e8-7489-3993-8f80-983ecd12a33e | -7.4036 | -45.64496 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 98958039-ce0a-3bf6-aa71-0aed3b4a9825 | -8.01361 | -47.17717 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 33f9bfd4-8203-375e-bd67-e5fd3c6a0205 | -3.76941 | -44.3555 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ab382e4a-dfb1-3e0e-8def-a871d0f014e6 | -7.73252 | -45.45006 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| abb3dc0d-c7ed-35be-b9d7-5d3119748f8e | -6.98496 | -43.29053 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| b558ccc4-f9b5-3383-a533-739cd01ac78c | -6.69134 | -45.34906 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7a9a70a1-c6b3-3f02-84f5-7cd07a084a2e | -3.964 | -38.6916 | 2026-10-07 16:03:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f5f1177a-0c9e-36d9-9027-29394f1f3fd1 | -6.05132 | -47.32009 | 2026-10-07 16:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 12bddc43-7982-352d-8d7d-e694d9032b2c | -3.42623 | -43.07201 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 34f6769b-bd27-3e90-a531-2e04a4a4d3f7 | -4.57973 | -40.77177 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 0edf3710-0848-3819-8bc8-5ae192fee4d2 | -5.96191 | -40.94138 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| d2d5710b-76a8-3eac-a0ec-2a0ea01d0332 | -5.71579 | -41.67098 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 57b78e7d-7890-3138-97ee-6720734bddbe | -3.47393 | -44.78046 | 2026-10-07 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| abbf9598-d617-378d-8814-97e159177e53 | -4.56441 | -38.30479 | 2026-10-07 16:03:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ff13843f-509c-302b-a8f1-a0366badb647 | -5.9529 | -46.38558 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 308c9c00-988b-3908-84b7-e776c597086b | -4.63012 | -48.85635 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 81c182ba-f1b1-3031-9ed3-e21328f899b9 | -6.91897 | -44.56339 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54b0a55f-2e87-3efb-9baa-9bf6b27b363b | -2.06137 | -45.97456 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6cff13af-dee6-3600-b2f0-483a63906b60 | -5.32653 | -40.89921 | 2026-10-07 16:03:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 2593eb10-d7f0-3226-8850-2173d8298f58 | -3.18141 | -50.56587 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 12bfb7fb-4584-3ded-a105-18294f537d78 | -7.42196 | -47.37664 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2cb568c-46f1-38ec-b582-22b292690b8c | -3.38424 | -43.38054 | 2026-10-07 16:03:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d223bd25-2bc9-3c02-8691-dd57c3b3c838 | -6.86618 | -39.09788 | 2026-10-07 16:03:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 21b2a4f9-b9e2-3bd3-9271-d28b8d2df2dc | -2.02002 | -47.75404 | 2026-10-07 16:03:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 46b799a8-79bf-3812-910b-474f75196629 | -6.3393 | -43.83094 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| daaab662-1c22-3dff-953e-9cdbfa30791b | -3.96069 | -38.6921 | 2026-10-07 16:03:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d46b5d0a-be92-3de0-a765-97265208a36c | -5.9666 | -43.52241 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ea165536-b0a3-3e0e-8723-a12cdf3d00bb | -6.04335 | -42.58464 | 2026-10-07 16:03:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 2ee86966-bd7b-3e6f-8157-e57aaba1d721 | -7.17398 | -47.79838 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6d6a8e9b-a938-3bc7-ab26-7e54935e1472 | -7.8743 | -44.22638 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d0de166a-629d-303f-a3ad-a4cc44fcc99b | -7.92624 | -46.81237 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e62e4d5c-5a8f-3301-9e77-2a2641f156b5 | -4.101 | -38.38485 | 2026-10-07 16:03:00 | NOAA-21 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd1fab71-e55c-3688-91b9-051c7dca9add | -7.21851 | -44.32396 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 83e34d8f-8f1b-3512-8431-afe9538a583e | -5.74076 | -45.05725 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 61fc6985-0271-3451-8fa4-66cbe71c27af | -5.97281 | -41.35908 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 85b3da7d-a5e2-3f20-b90e-13ea51e31747 | -6.68663 | -45.34977 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 54b91009-8cd0-303d-8c44-bbbe29a0eb4a | -8.46529 | -48.68961 | 2026-10-07 16:03:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ad9ca17-43da-3ae7-a084-d92d3d3b51de | -7.29421 | -47.27436 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d711d05-3f78-3c79-80a2-b70a6c37f4c0 | -3.22098 | -42.65675 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e9b5b1bd-3778-3f08-8626-f7c548c9f55b | -4.421 | -43.73595 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0cf66688-7ae7-338f-a467-14354d364997 | -6.18778 | -44.6539 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b72f4588-63e0-3c59-b186-00059e74197d | -6.82022 | -43.68678 | 2026-10-07 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4de78c3c-64c1-3698-9b0a-99d9e76de03c | -3.81024 | -42.21605 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |


[Clique aqui para ver as próximas entradas](README171.md)
