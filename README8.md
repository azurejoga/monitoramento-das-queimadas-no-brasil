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
| 8e10eebc-71d8-3ab9-a230-1adaf6c04c25 | -11.0201 | -45.059 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 3b29cac6-7e97-3ec9-92ca-6e2fcc95f478 | -22.5894 | -51.8759 | 2025-09-11 01:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| fc685d38-66ac-3651-b475-5e795d7dfd94 | -7.3401 | -49.6027 | 2025-09-11 01:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0ff846de-bf15-3d01-a4d1-918cc3482be3 | -10.0152 | -51.7241 | 2025-09-11 01:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 5649aa18-3c62-3a05-b6f6-fe54f3755cdc | -12.4164 | -63.8229 | 2025-09-11 01:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a8879495-583e-3137-90f7-ed1387cb2693 | -19.9994 | -47.6271 | 2025-09-11 01:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 49ce07cf-024e-3607-a59d-506dd9537ed6 | -22.5888 | -51.8985 | 2025-09-11 01:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| 93226b74-de6d-3ad0-8c54-22b33b765919 | -13.1648 | -45.2665 | 2025-09-11 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 17956aad-87ff-3174-91c2-88bc6ea0beef | -14.7527 | -60.2321 | 2025-09-11 01:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 65eb6c13-47a8-3725-9c71-6bdbc8354fd5 | -11.3588 | -46.4941 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a41d3c72-d680-32f9-9d6a-836611158c27 | -11.1624 | -52.032 | 2025-09-11 01:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 3a39d18d-642b-300c-ae33-e9b84928d2f7 | -11.3584 | -46.5167 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 646b1a8d-5be3-3cf9-8ece-0e9c0bf6d399 | -13.1842 | -45.2633 | 2025-09-11 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 5ef1d86b-554e-34ca-8bf3-e57bf773d6bd | -13.1837 | -45.2865 | 2025-09-11 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 1a4494fc-645c-328c-91c5-0995d78e3c66 | -13.1644 | -45.2897 | 2025-09-11 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 5801fc61-b81f-3f1d-b31c-2237655af42e | -12.3975 | -63.8239 | 2025-09-11 01:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4efaf3ea-25bb-359a-840c-5c76beaee216 | -11.0393 | -45.0564 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ffaaa7b8-77c4-3ff7-95f3-ab06b0e65773 | -11.1621 | -52.053 | 2025-09-11 01:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 602381e7-7bd4-3ff2-98db-04ba75231873 | -14.7529 | -60.2123 | 2025-09-11 01:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ebfe7826-a1fb-339d-94e4-2c0b7c7e2bb7 | -9.0753 | -47.078 | 2025-09-11 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 45ca52f5-5030-3ed0-a063-f234258dfe3d | -11.358 | -46.5393 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 82046b35-62bc-334e-a20c-f80b1438352f | -19.2016 | -47.9889 | 2025-09-11 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| d9859f81-9524-3366-892a-f80d782a0c0d | -14.7529 | -60.2123 | 2025-09-11 01:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 599ffad2-061b-3a80-9f3a-33ff0f436a88 | -14.7527 | -60.2321 | 2025-09-11 01:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 528b5a5e-05f4-31a7-b105-6a4b1a8f5054 | -11.1621 | -52.053 | 2025-09-11 01:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 786fbeb3-cb27-39fb-8b6f-b2b1c1477dc1 | -11.1624 | -52.032 | 2025-09-11 01:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d3c595f5-da84-3168-b68e-6aa1c64f0a65 | -9.0579 | -46.9688 | 2025-09-11 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ca514c6d-9e3b-36e2-b836-f95cb0c1de13 | -19.2421 | -47.9802 | 2025-09-11 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 5a6f4318-7245-36bb-8a29-abebff98b1b4 | -10.5482 | -49.8899 | 2025-09-11 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c08d333a-53de-342f-b853-4c3f41c0d037 | -13.1648 | -45.2665 | 2025-09-11 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| a6327e0b-895d-3157-b09b-7c71a17d0015 | -12.3975 | -63.8239 | 2025-09-11 01:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9409b84c-dcd7-344c-8356-67fcf9c80f3d | -19.2415 | -48.0033 | 2025-09-11 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 98b88c72-6aaa-3fdd-ba73-6398cfb8cb04 | -11.3584 | -46.5167 | 2025-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0f6d5407-ce64-39d1-b3c9-9afca16d376c | -15.1371 | -52.4252 | 2025-09-11 01:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 23310fb6-0320-35b9-8fb7-d009c2821c84 | -13.1644 | -45.2897 | 2025-09-11 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 0fdd9869-b563-31ac-8e78-9708da6d1150 | -11.4097 | -43.5336 | 2025-09-11 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9c6d13ef-37cb-359d-be85-04b4a96c28dc | -9.0234 | -49.762 | 2025-09-11 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 05cebc49-d3fa-3a70-9112-5011892e0c6e | -19.9994 | -47.6271 | 2025-09-11 01:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b886b128-865f-390d-b385-c263aab99d8d | -11.3588 | -46.4941 | 2025-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b320b2d6-b185-3810-827a-ee67d87d0947 | -12.3976 | -63.8048 | 2025-09-11 01:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d27ed300-56e3-38dc-a53d-ae6b41c3ea0c | -22.5894 | -51.8759 | 2025-09-11 01:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 29037d57-2498-3402-b5ab-f459241413bd | -10.5485 | -49.8684 | 2025-09-11 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| dc97386c-9a54-355d-9133-f3501435e7bd | -9.0232 | -49.7834 | 2025-09-11 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 58921e91-aa74-38b4-8c60-a1ab763056e4 | -22.5888 | -51.8985 | 2025-09-11 01:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| bb8776fd-2d03-3c93-9f2b-cf036f84f09a | -15.9865 | -42.9719 | 2025-09-11 01:40:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c4abddf6-72ec-3459-ac44-df7628ea3130 | -11.391 | -43.5128 | 2025-09-11 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 10dfa266-5cfb-3c2e-bee3-58ae615aae6e | -14.7334 | -60.2337 | 2025-09-11 01:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| cc1c3fdb-17af-3ffc-b629-b4eeb8e8ffcf | -11.0393 | -45.0564 | 2025-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c2279d69-12b1-320c-b56d-8b512bf1fd83 | -11.0201 | -45.059 | 2025-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d3194a2e-2c49-319a-bad1-f4de60563cad | -11.1621 | -52.053 | 2025-09-11 01:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f2592049-379c-3e7f-9f41-d671e4118463 | -17.8327 | -46.7313 | 2025-09-11 01:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ca590644-ee87-390d-b603-2f4df9829f5e | -11.1624 | -52.032 | 2025-09-11 01:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 8fd3a1d4-04c8-3d36-b215-df72bf33cdda | -9.0579 | -46.9688 | 2025-09-11 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4cf08808-1168-3ef9-804f-0065c2186a39 | -15.1371 | -52.4252 | 2025-09-11 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e471e2e3-a944-3609-a4f0-abd5e6b4b223 | -19.2415 | -48.0033 | 2025-09-11 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 94ad60dc-f9eb-3b17-891b-d0d8ce80560f | -19.9994 | -47.6271 | 2025-09-11 01:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b4b04108-7042-31b2-b662-73991149e91c | -19.2016 | -47.9889 | 2025-09-11 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 46fb276a-9c64-323a-946e-9f5319925cce | -11.0201 | -45.059 | 2025-09-11 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4e2d3aa1-addd-31dd-9fb6-3b9640bf9cfe | -11.0393 | -45.0564 | 2025-09-11 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4ca6d529-74c5-3ca2-8d49-0992a14838aa | -8.5089 | -45.6807 | 2025-09-11 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 976d74e2-f53f-3eb0-8d5a-1fc3a69f22a4 | -19.2022 | -47.9657 | 2025-09-11 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ae8eb6ed-3019-3374-8027-cce11ffb9667 | -13.1648 | -45.2665 | 2025-09-11 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 077afd10-ca5e-33bd-bd98-60bc729b56d3 | -11.3588 | -46.4941 | 2025-09-11 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 0510ecbc-0dc1-3f9e-a742-078b6e2b3d9e | -10.5482 | -49.8899 | 2025-09-11 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9d380d27-181e-355c-a016-0ff62eb0fd0d | -13.1644 | -45.2897 | 2025-09-11 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 82d47331-0dfc-34fb-be1b-521eecc6d0b2 | -22.5894 | -51.8759 | 2025-09-11 01:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 553e14b8-fd26-3481-b04a-ad9486da5817 | -15.9865 | -42.9719 | 2025-09-11 01:50:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9f837ef6-93b1-39e4-b633-b3971efd20aa | -8.5278 | -45.6787 | 2025-09-11 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| debced9f-9ce0-30c7-87d9-82b27a664707 | -19.2218 | -47.9845 | 2025-09-11 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 9f51aadb-1295-3c82-a4c6-84b8b3810632 | -22.5888 | -51.8985 | 2025-09-11 01:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| 37a04b88-7c5a-3cda-8945-b77e6da074c2 | -14.7527 | -60.2321 | 2025-09-11 01:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 37e4d119-8475-39e7-b347-6f5f56190f37 | -14.7529 | -60.2123 | 2025-09-11 01:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 3655601e-dff5-3a70-92b8-2c2a60fcc29c | -11.3584 | -46.5167 | 2025-09-11 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 7064d54a-1e0c-3e30-b9bb-baf160bf2c15 | -9.0753 | -47.078 | 2025-09-11 02:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 959bed0b-ed7a-3ee1-aac0-c7f806587d92 | -22.5894 | -51.8759 | 2025-09-11 02:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 6a2da92d-4a0b-3b6a-a7b9-e636bceb926f | -13.1648 | -45.2665 | 2025-09-11 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| bbe6a179-8b18-3032-944e-116558a45bc8 | -8.5278 | -45.6787 | 2025-09-11 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b69cba43-1714-3516-8c3d-06ba1a838085 | -11.0393 | -45.0564 | 2025-09-11 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e7e9d2c4-05dd-3c12-874e-7944c0d942cd | -11.3584 | -46.5167 | 2025-09-11 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| eb39717a-1048-3834-b88f-79fbc8f6b6e8 | -11.4836 | -43.6875 | 2025-09-11 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.5 |
| dc9f2789-81ee-32d7-9023-6bd9fb47a760 | -13.1644 | -45.2897 | 2025-09-11 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9501a1db-cf60-31ee-8a2b-ba132bd17b07 | -15.9865 | -42.9719 | 2025-09-11 02:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| abffdfd5-b07b-3347-b6b9-2326d6232876 | -19.9994 | -47.6271 | 2025-09-11 02:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ed5f1b74-849a-3e51-9e12-1e61b751a181 | -11.3588 | -46.4941 | 2025-09-11 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 92538843-55b6-39a6-8a81-47d2bf30f34f | -15.1371 | -52.4252 | 2025-09-11 02:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| af52f8d4-bb12-3032-906b-dc0745f736f6 | -9.0232 | -49.7834 | 2025-09-11 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e0e35b9e-f3d8-38b4-a1aa-db1d9045e4d5 | -14.7527 | -60.2321 | 2025-09-11 02:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| ff66479d-a751-3777-b8c4-5ad24086866c | -11.4644 | -43.6905 | 2025-09-11 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5f2768ae-6e53-30f3-985b-792d965aaa0c | -21.0067 | -48.764 | 2025-09-11 02:00:00 | GOES-19 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 6525bb60-272a-3fb2-9daa-7422bd2f2b51 | -14.7529 | -60.2123 | 2025-09-11 02:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ba326b22-3e8e-30a5-866f-739fff2d07df | -11.1624 | -52.032 | 2025-09-11 02:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2c4851f9-65b6-349a-ae69-23f4f62c89b6 | -14.7334 | -60.2337 | 2025-09-11 02:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e3fcdf5b-6b23-34e7-ab54-101c47874a22 | -9.0579 | -46.9688 | 2025-09-11 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0b440593-ee8c-39af-a62b-4d3fa62fc464 | -11.0201 | -45.059 | 2025-09-11 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| adc70b58-64a4-3606-9c84-cd63d6c32a5b | -19.2016 | -47.9889 | 2025-09-11 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| aa82a6c3-92ed-3c0d-835d-72e1c4c25d0e | -22.5888 | -51.8985 | 2025-09-11 02:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| a0492216-c055-3b26-be7f-7781e246b4a0 | -9.0234 | -49.762 | 2025-09-11 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 25330af8-8ce3-3599-bbc3-4ce7f59e0d71 | -11.3397 | -46.4967 | 2025-09-11 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| e0e97575-ddda-3b2d-8231-2613c05003ae | -9.0753 | -47.078 | 2025-09-11 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 12d0bc71-e335-3ee2-ac7d-088760c57e5c | -11.3588 | -46.4941 | 2025-09-11 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |


[Clique aqui para ver as próximas entradas](README9.md)
