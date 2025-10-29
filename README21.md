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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f7252b1-21d9-35f9-9886-d3cd90e2c9fb | -11.99377 | -46.78005 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99143581-2e30-31c2-9dc3-af761e2ddba1 | -10.68203 | -44.58574 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae8f5ca4-9c6e-3aa0-a5f8-8c716551b0e1 | -14.31946 | -46.51432 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8db2c02-4483-32e1-b7ba-9334534bf9bf | -13.36602 | -47.38346 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 647cee18-4a34-3e9f-af86-f94c707ee25a | -13.48109 | -47.45313 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 651d0331-f01e-36bf-925a-b8b2c1fd08e1 | -13.26653 | -47.86191 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5a2f7b6-e751-3785-8d36-5e755475501a | -13.93602 | -48.43305 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02f838ea-9966-352f-84bf-8f4e7fa525ad | -10.20968 | -45.95153 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d588fb0-c9ec-31df-841a-9377aa83a261 | -13.56712 | -47.34383 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01961544-dbcf-320d-9863-97df040687f1 | -15.45839 | -47.69162 | 2025-10-29 03:55:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1abf15c-8d04-3db1-9cf4-f29fe79aaa17 | -9.28841 | -47.01666 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c0074e4e-cd99-35f8-8fbd-b7071cc94182 | -13.9399 | -48.43968 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9a550dcd-f2ff-3775-ab16-7a3806fc3985 | -15.50752 | -40.7553 | 2025-10-29 03:55:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c5d7ef19-9f38-35e3-8de1-fb06afc11f4e | -13.23279 | -47.06271 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3896d520-74ce-38b9-b2d3-ec27c9019598 | -13.6105 | -46.49244 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8a2897e-9650-3966-b4fb-d531ed7622e8 | -13.63359 | -46.51536 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cbd0b8e8-7deb-3fd1-b04e-c6bc7a32c526 | -13.01631 | -48.77197 | 2025-10-29 03:55:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a3210a2d-452c-313c-941c-423e662bbaa3 | -13.93338 | -48.44657 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f66623f-185f-3c1c-a711-5c6dabbf283b | -14.26033 | -48.11707 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31bedd2b-fc8f-36c1-82c6-6ae981b1e31a | -13.23055 | -47.73244 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac7e5b38-0020-36ea-b598-e47b0066dd01 | -13.63947 | -46.48387 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56a68148-e19a-3851-abcf-f16bf4217275 | -11.11276 | -44.02134 | 2025-10-29 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e4161b6-ed93-323c-8a17-6928916eee78 | -10.85325 | -47.89211 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f063701b-8593-3d73-855c-cff8e46d3696 | -10.574 | -49.75394 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8d131cb-f9c2-3451-8a1b-bb8d638ecdce | -12.52646 | -44.88749 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| facfc1bd-5c0a-34e5-af5f-f117d8603ef7 | -11.58258 | -47.94047 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5683729a-e043-373d-a411-f8cb162e4462 | -14.31332 | -46.52309 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea507b76-6c8a-3a0e-a2a0-b15ee16aefff | -11.58314 | -47.93745 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a43326d9-29df-3d18-bcb2-12ed69672ec2 | -12.69438 | -46.31776 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7fc9500d-309a-3c29-8e5d-350d65221630 | -12.103 | -44.59756 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c1a42e8-c434-308d-be21-c297684e0dd1 | -15.45791 | -47.68862 | 2025-10-29 03:55:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bd9ed3c-ba10-37d7-9e55-68221069e14f | -16.04989 | -43.71119 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20cfcf6b-4a06-3ed3-8a1e-8cb95628248f | -10.12704 | -44.83236 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02a3bbdd-3567-32c8-b946-f6f00e0bf314 | -12.0021 | -46.7868 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5d7eaeaf-62f0-3d61-8db4-63a3b2e2a3a1 | -15.19586 | -47.19865 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a5f003e-a79d-3991-baaf-e7c2c6c4448d | -12.69355 | -48.43933 | 2025-10-29 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cce0cd84-e8a1-3d66-bdb3-0c8aac6aa81d | -10.37227 | -44.26934 | 2025-10-29 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f766f954-ffb0-3e6e-a224-e15a38d847c0 | -15.18332 | -47.24072 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 330cf7c5-67ea-3db3-9d32-fe5fb13351c3 | -13.81937 | -41.69541 | 2025-10-29 03:55:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7403b52c-3620-31de-8d1e-e6f2afd04564 | -15.91725 | -43.52539 | 2025-10-29 03:55:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b24a95c-03ac-3368-b3de-b57a6a6ede90 | -15.09561 | -43.83683 | 2025-10-29 03:55:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e743ddcb-541f-3e2c-adeb-3170ab9174a3 | -10.50535 | -47.72982 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7036f04-78d8-3511-8be4-4a223dcec13e | -14.61001 | -48.4041 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60fddaec-97e6-34bf-8d13-313b4227ade0 | -15.33549 | -42.01026 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f1f4df8-ad1d-32d7-9cab-0626dedaa23b | -12.46596 | -43.58683 | 2025-10-29 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7407e323-b334-376b-ba8d-2701906d4b42 | -13.20875 | -47.0636 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d92fb238-4f3b-3384-a81f-e7738b0c615a | -13.25177 | -47.72578 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 97ca8e50-7bb9-3e67-b277-158f105f8086 | -15.15771 | -47.22811 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61882470-b218-3c1b-83fb-00ac9afffcc4 | -12.10361 | -44.59404 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c05e5e3-7ee2-36bc-b2f1-865d207a75e2 | -12.76831 | -46.65764 | 2025-10-29 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6cb071c9-b4f8-3b26-b010-4465f48e2610 | -10.96469 | -49.6642 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec71d1e0-da78-3102-a2c0-2c34916a654f | -10.6139 | -47.89981 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c20754f4-5b0a-32ac-9388-50a2c73aebaf | -11.7366 | -49.33418 | 2025-10-29 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05620e97-520e-3b64-b2d8-2b4ac7f4f203 | -13.62963 | -47.01648 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49f13b6a-da7e-3a3c-b8d1-85f380972265 | -15.17987 | -47.23428 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d95c60d1-ff84-3950-a0b8-f6563d5971ad | -13.62372 | -46.4731 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 094a4cad-1b9e-3a67-86b1-7b8c44d4a034 | -15.09639 | -43.83238 | 2025-10-29 03:55:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 459b782d-286a-3cdc-9ef3-8412df984a7f | -12.44487 | -43.75609 | 2025-10-29 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07b24eb6-8b12-35f9-86a9-8f9775dabb25 | -13.32301 | -47.44862 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f87a9441-21ba-363f-8399-22f777c5bf69 | -10.78005 | -44.76195 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc031839-d611-3f5d-bff2-0f7a0443f3c8 | -14.79096 | -46.17897 | 2025-10-29 03:55:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 906d8461-af13-318e-8c56-585c60f0256f | -11.04096 | -47.85099 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b2de7ca-5ae8-35ae-bcb9-246d03f76026 | -10.52498 | -47.73685 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fbabcd8-5020-317a-9f16-3793f75c7601 | -13.03847 | -46.73554 | 2025-10-29 03:55:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bd9b25e-3c70-3a9e-b1de-3fd0aa003194 | -11.10573 | -44.6971 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90b9d70c-75d6-3322-b319-098f8f760d58 | -13.31499 | -43.58668 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a82af4be-2d05-3f3b-bc0d-00ce64f36965 | -10.22292 | -47.55261 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9d26fe9-a396-3e5e-88ab-34e6a949c390 | -13.32383 | -47.44418 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91222fbf-4a6b-31e3-a9bc-e0e7fbbaad5c | -15.17889 | -47.23946 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 402c5bda-82bf-3b17-afc2-daefc69759b2 | -13.2124 | -47.06961 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1234a4f-e511-3eaa-a81d-b30442e08a33 | -12.48438 | -44.20846 | 2025-10-29 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32d9cff3-cc01-3d19-b891-25dd7425c059 | -12.38599 | -44.96956 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8969f180-09c4-374d-84ec-dc33a314d8f2 | -9.96151 | -47.14655 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2590c810-77b1-388d-a9e5-cfcd77567d40 | -12.05434 | -47.82545 | 2025-10-29 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9770e28a-e0cf-300e-94bf-0d70538c474f | -14.76827 | -43.08155 | 2025-10-29 03:55:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 712ad2b4-e41b-38ea-8523-e495b5879981 | -13.6422 | -46.49368 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 840e4df9-6fd3-3d17-a473-5f29d3b19a34 | -12.61557 | -43.30323 | 2025-10-29 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48a6748d-c673-32de-a634-8ca96845b719 | -11.79163 | -44.39005 | 2025-10-29 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 098a7997-aa86-371f-8eed-b0b0a0059b15 | -9.89145 | -44.88439 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8019d231-7ff7-3e05-b353-c85d65710a4e | -12.41051 | -44.70889 | 2025-10-29 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b346ca61-79eb-30b6-87be-e7ea552c71fd | -9.61903 | -47.7749 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 446783de-8c53-3aa8-8d37-e38f5e887c78 | -14.25654 | -48.11055 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0005a214-5b2b-3313-895a-109f1e53c402 | -13.64439 | -47.03842 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27b49391-02d3-3c3c-b59b-c5cad0b6f631 | -13.333 | -47.47973 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ec98c69-2e72-3f8d-9d64-9bf6b34188e5 | -13.64493 | -46.50352 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4420a776-3910-37e9-a0f0-2071a1728a44 | -12.58572 | -43.36693 | 2025-10-29 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 487afe56-7658-368b-b9ee-afe20f59be52 | -13.68708 | -47.19152 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcc7c683-0732-33ad-bcba-c89f98022e0f | -13.5671 | -47.33022 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44b34791-2b64-3f6d-b9c3-b94325404e6a | -13.64137 | -46.49815 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dc133c7-7494-35c3-b7c9-3c05eb64e048 | -13.92121 | -48.45591 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1a36f52-c274-360d-8c23-869bb7bb8ea6 | -11.61395 | -43.35767 | 2025-10-29 03:55:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e4d50f9-e09b-343c-8e73-ccb8d776b38f | -14.25272 | -48.10422 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10309f7c-cc87-3588-bb00-2147ba329423 | -9.73457 | -44.05989 | 2025-10-29 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecccacea-adac-3382-b9ef-cc152074f3da | -15.09928 | -43.83749 | 2025-10-29 03:55:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a81bc54c-b4fa-34ce-95c6-1a64aa57523c | -11.03169 | -47.84463 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a1950e8-120b-31af-ae0d-45d5e0287859 | -16.67457 | -41.35556 | 2025-10-29 03:55:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ce6d862-ba70-3018-becd-92ee3c71ee9b | -10.4299 | -44.99013 | 2025-10-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8340fa1-d9f4-38d5-98be-1e600eac6679 | -13.02149 | -48.77295 | 2025-10-29 03:55:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fec0f5d5-08b1-32e6-87ad-ed57327e13c2 | -13.57555 | -49.59631 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aa25fee-6276-37c2-b5c3-c1b189b978a6 | -15.11569 | -43.26024 | 2025-10-29 03:55:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
