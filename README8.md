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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f752609-140f-3034-aab8-45a3be51eb0c | -3.5836 | -47.52333 | 2025-07-24 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a797e93-d838-3196-8fc5-3cbde81725eb | -7.25289 | -43.07481 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 5336f4be-137d-349f-8aa4-5bd4d06d3533 | -5.50562 | -51.14004 | 2025-07-24 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af67e3f7-d22a-373d-98a5-79af88f74d43 | -7.15841 | -45.23902 | 2025-07-24 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 188ac87b-6192-347b-a8d6-460cddb789eb | -3.59898 | -44.7902 | 2025-07-24 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6031d939-1a95-39c4-8907-665c68640b01 | -7.54856 | -44.48558 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a085910c-efc5-3cb3-86f5-8aad8d9d556d | -3.97434 | -47.56659 | 2025-07-24 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c03653ef-1ca6-3c06-9618-937fb5605f04 | -4.05491 | -42.515 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 931311df-6743-3208-a554-90a19386b067 | -6.57439 | -41.49818 | 2025-07-24 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ceee8a3-4560-3abf-8368-a6c9ba63e8b5 | -7.08556 | -44.87584 | 2025-07-24 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d81c94be-3612-3913-be60-34b76323a5f6 | -7.1611 | -40.21157 | 2025-07-24 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8a11a9e1-3ca7-396b-85f2-de923d07877b | -6.87402 | -43.10724 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a286a9d-deb5-3845-ab3b-1a4316463465 | -6.60987 | -42.33396 | 2025-07-24 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d47f356-ddb2-3acc-a8fd-af42bd857dda | -7.72079 | -43.95477 | 2025-07-24 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dad975e-64c7-3e78-9b7d-fa257873e5a7 | -6.97308 | -44.37966 | 2025-07-24 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31072d93-432a-334d-a806-350f301675ec | -2.38943 | -47.62922 | 2025-07-24 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509c1d4e-3bc2-31e3-b422-4856787de1e3 | -3.05542 | -47.38048 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f854719-b90c-3f3e-8521-71ae7ef1cd9a | -3.9349 | -41.49121 | 2025-07-24 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 896ba889-4563-3734-80b5-6d229d4a4d8d | -2.58544 | -51.92095 | 2025-07-24 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4271dfa-5b8f-33b1-983f-a4a903f2bebc | -6.3907 | -45.31516 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9c98d10-cba7-35b7-9ed3-e51507030ebb | -4.04884 | -42.51054 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c559888d-a555-32c5-84c4-07efe0162269 | -5.18758 | -44.95559 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 76a24246-c0d0-3dcb-9e05-04697a741293 | -6.61374 | -42.33097 | 2025-07-24 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95ce1e5d-895d-35d6-836c-47594a3bebad | -5.48244 | -42.14856 | 2025-07-24 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be296e8c-5f6f-39ef-9287-e0aa2f21bf91 | -3.97712 | -47.87966 | 2025-07-24 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0481d779-a50a-3157-861e-c0282ea795d1 | -6.96419 | -44.3711 | 2025-07-24 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 305e33b4-766d-3441-96d8-02a65db4ea57 | -9.06222 | -45.0638 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa86dd9a-ae42-35b7-9fd7-8ac96c1f2154 | -7.13349 | -44.84639 | 2025-07-24 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f21f6f3-dfc1-326e-8c92-3c97398e50b2 | -6.61041 | -42.33045 | 2025-07-24 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b3c020f-d277-33d0-ad9e-f43601995de4 | -6.63418 | -43.09766 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d98da4a-6ff5-3473-b17a-4d6987b8ccb9 | -4.04339 | -42.5238 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 20814783-5a19-3691-be65-954bcb51cd82 | -9.3209 | -44.85049 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 422b4613-e5f7-3c33-80cf-ddad6515d167 | -3.17777 | -49.45015 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 3fe9c61b-cffa-3c64-990d-825b0300ba17 | -3.1732 | -49.44941 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| ab2ba19b-4db4-3b07-a28b-4c6d8fa7e661 | -6.87505 | -43.7523 | 2025-07-24 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e20a6b76-3724-382b-9981-70d8651748a1 | -7.25674 | -43.07186 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| b8ea473a-25f7-3433-b725-15802db360fd | -6.26918 | -44.51017 | 2025-07-24 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e038e25c-a80b-37df-8a75-86aa15d21828 | -3.17853 | -49.44547 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b7105e80-80c7-34fd-92d6-89e81292f94c | -8.49368 | -47.23225 | 2025-07-24 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b25f1e4-8625-3b66-9ccb-5699195f3cd9 | -3.9322 | -43.16911 | 2025-07-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e88fdb1-cfdc-3930-8a6b-3649c83df86f | -7.14863 | -43.80647 | 2025-07-24 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 480bafd6-562e-32cd-9904-21070dbd3e16 | -7.89553 | -45.54598 | 2025-07-24 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e7f5ea-71f9-3982-bbc4-857ff929952c | -3.17701 | -49.45487 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| fbd81a3d-09b6-301d-98b4-bc14778eb927 | -3.22826 | -46.785 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2dd017c9-e335-3659-bf39-409b3e8b3047 | -6.4686 | -44.58234 | 2025-07-24 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6250b602-f00e-3d9b-9aed-a06a852b312c | -4.80985 | -43.21247 | 2025-07-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f3b1635-71aa-3e57-b0b1-8c9435f24c21 | -7.2562 | -43.07533 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| ba9511ff-5fa8-3ffb-9549-7d65e03d059b | -3.03181 | -49.42294 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ebaad6-b6a5-3cd4-a39c-faf4db4511de | -9.58677 | -46.3336 | 2025-07-24 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01f2b610-f7a0-3691-b87e-05ef37dbaa0b | -7.88179 | -46.89272 | 2025-07-24 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 703152f8-0ee0-30e1-a39b-10ebbc1ffcd8 | -3.93825 | -41.49173 | 2025-07-24 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86540af0-5ddc-3452-8ea4-939916c87434 | -6.57766 | -49.50925 | 2025-07-24 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dd370baa-dee0-3cf9-8c48-94cfb2b8c7c8 | -3.36017 | -47.16035 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 86c3d53d-3019-3a73-81ea-3830b307dc7f | -3.35547 | -47.16469 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5791d12e-3cef-3c35-aea2-47c5ce356cd2 | -3.59838 | -44.79396 | 2025-07-24 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdb94130-2a5f-324f-a305-443419282240 | -4.05161 | -42.51449 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a7d6c394-0c5e-3228-9378-0efe613ca3f8 | -7.35901 | -43.44244 | 2025-07-24 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f3abf87-6f2a-3682-ba4c-e687df008151 | -7.14809 | -43.80994 | 2025-07-24 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85ef6ced-6da2-3fca-9917-41717c9d4100 | -6.61741 | -42.4147 | 2025-07-24 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6067ff15-35be-3ad0-9e7e-40240e45252c | -5.6198 | -43.49242 | 2025-07-24 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4cc2840-bf64-30aa-a780-1dfc2cbfa7bf | -3.04325 | -49.43917 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df7d126c-685c-3c73-b9f9-cb83e76a55db | -9.76187 | -41.87958 | 2025-07-24 04:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8251ce45-8350-3398-9156-54055caed791 | -3.0594 | -47.3811 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2466d4cf-cbbe-3a0d-af44-62ae8ae8b9e0 | -7.54911 | -44.48206 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4af3dcb6-d841-3efe-9507-1352e7f4b981 | -4.29949 | -48.10333 | 2025-07-24 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a07b1654-a6f2-3a5a-a05a-a4cbff1438a4 | -6.82402 | -43.98975 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1b0673b-ffbe-39d2-b715-c39f76e12c43 | -4.05768 | -42.51896 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 39ca4db7-48c6-3dfd-b1c0-62feb473a490 | -3.97654 | -47.88332 | 2025-07-24 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ada523f4-5314-3d99-b00e-7730b9a7b2b0 | -6.64725 | -43.05721 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b163839a-9e9c-3cec-abab-35d36131a11b | -8.0375 | -47.65828 | 2025-07-24 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f489d8c5-c7ab-3dbb-9f1f-b63ddb51fc96 | -8.48255 | -49.55407 | 2025-07-24 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e0ee4b6c-c4eb-3a5a-b2d1-ee3b9d429cfa | -5.67676 | -43.67163 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31a7732-58ea-32ee-99e3-5fb009a2cf00 | -5.68725 | -43.6697 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01c1fadf-bc87-3374-912a-2e8f3b8bd5a4 | -7.27437 | -44.34806 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e55c7e74-fa44-3b7a-a0bc-23594df27a41 | -7.66403 | -44.48647 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9651ea07-2c2a-3840-881f-f163b17dfaef | -4.87544 | -38.26627 | 2025-07-24 04:14:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57d57ebb-b9ef-3a3d-8c02-cc6bb5b19f2d | -6.91511 | -43.95063 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f93a187c-4e8c-3674-be79-cd0c63a1c49f | -6.62426 | -43.09613 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbd25f88-d542-3ac0-ab60-6a076bd8f826 | -7.25457 | -43.08574 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 798880fe-136a-385d-a92d-dc016b528c7e | -7.01779 | -45.85121 | 2025-07-24 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b181ba8d-b6f2-3041-8fe5-c49771f34e2c | -7.24573 | -43.07725 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 02c3ec25-34a7-3f82-a8a5-89aad53adb50 | -8.92945 | -47.34349 | 2025-07-24 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00809380-38fb-3b04-a25c-de6fae5c0ab2 | -5.98388 | -45.35596 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34fa2b2c-49bc-333d-ae92-b29d49cda9c9 | -3.93274 | -43.16566 | 2025-07-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11b44cb7-eda3-31b5-b12d-169a0881bf5a | -6.8977 | -44.14788 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf61d02c-7562-33ed-a0b5-35ae8b440435 | -6.61687 | -42.41821 | 2025-07-24 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87f8ccc2-2a6a-38a0-bc9b-04ef3fe34689 | -4.05107 | -42.51793 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2cbb8fbe-cac8-3a63-b3ee-d194de1fca60 | -6.53825 | -44.65555 | 2025-07-24 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a135c156-c27e-3ca7-bfe3-c237eb542798 | -5.56568 | -39.19896 | 2025-07-24 04:14:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b49c0e68-817d-38c8-b0bf-241d524f88d5 | -8.28941 | -44.97978 | 2025-07-24 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc7eac7d-7ecc-36a9-bb5a-6dbe9a6e7ec6 | -9.05888 | -45.06327 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e2b6e7a-c38c-307a-8dfd-79ddd76bac5f | -6.62982 | -42.33385 | 2025-07-24 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 44eab156-1b34-3698-bf3f-9f3d954967a1 | -3.04688 | -47.38269 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73ab4e31-7640-3932-a0b7-b0393d85a3ef | -3.38082 | -43.12796 | 2025-07-24 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70c6587e-a4b1-3b1a-b585-314052626d0e | -8.47832 | -49.55338 | 2025-07-24 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45046f80-8c99-3116-b30d-0729eea79130 | -6.63249 | -43.08678 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73e7bbf8-2839-3c77-9709-3b0557be144f | -6.91149 | -42.80056 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7aa1c554-febe-3331-9f07-9e8da404b02d | -7.24681 | -43.07031 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7f27c2c4-d99f-32a2-9e3b-5fc94a056ecc | -3.60521 | -43.54057 | 2025-07-24 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 125f5b82-bada-3e9a-970c-15b6987d47b3 | -7.54191 | -44.46287 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
