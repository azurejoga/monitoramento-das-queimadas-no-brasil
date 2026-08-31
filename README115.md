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
| 573ae5b7-a12e-36bb-b26d-81937756e266 | -10.08578 | -46.61262 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0c35079a-b964-3821-b570-580c084c45b9 | -13.84159 | -54.09815 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8d354e0a-6a5b-3405-892f-453352db5d2c | -9.4234 | -45.67973 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 44935d85-3319-3a2c-9461-d4830daf4164 | -9.59708 | -47.60418 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8b6876e2-1514-3b33-bbb7-9464f5773ac2 | -10.34976 | -49.97377 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56042058-38d5-3c0b-a907-d867311d133d | -8.76996 | -46.44779 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 040b840e-beac-3a73-890c-9966826524b5 | -9.8377 | -47.83197 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e70279d9-08f7-3d67-853b-ce4e81322f33 | -11.2385 | -45.14106 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4fec7339-0c52-39ed-9cba-d3449fe2a415 | -10.10723 | -50.29428 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb7d2f4f-fa5d-3724-bf89-63ac5a732ded | -11.37745 | -45.20374 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bb6925a4-650d-3996-b629-5cb719b2a456 | -12.96106 | -45.93243 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| d322733e-4696-3efc-b185-4dbae4f9c256 | -10.84766 | -45.34081 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| c230a69d-c2b3-3699-84b3-846b7c381e02 | -8.69825 | -39.2329 | 2026-08-31 16:30:00 | NPP-375 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6eca3199-d20b-355c-b1fa-fab81155a0f8 | -14.58727 | -53.61462 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 1de91898-dcd8-3bf7-b1b2-37c4fa6de4d2 | -11.07908 | -51.5279 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 4876f1ec-da39-387c-91e3-2b286dfbb67d | -8.65711 | -39.26028 | 2026-08-31 16:30:00 | NPP-375 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 52e5ab2b-08f5-348a-a08e-d9f94de6522e | -10.82106 | -50.63109 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0a703882-fce8-36cd-b7a4-bfd6731e4a69 | -11.96235 | -47.74408 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2fba987b-ba54-3e2c-a7c5-00e353c6633a | -9.57065 | -48.33171 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95b5d82e-01f2-3c3f-9828-71db9db67aa0 | -13.38631 | -41.32877 | 2026-08-31 16:30:00 | NPP-375 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 983936d4-b6ed-3c61-bf60-2ff794c7b38d | -11.19818 | -46.09904 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 39203334-93aa-3001-a3b3-692c144d0ceb | -13.43121 | -39.87925 | 2026-08-31 16:30:00 | NPP-375 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| cbb30d67-e159-332e-acf3-66e8c9e712b3 | -8.87264 | -46.02652 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| aa6f3730-8868-3375-9f87-973bb6aa3224 | -12.09439 | -45.00041 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 7e148bb6-75cf-3366-8e32-72833f30c639 | -10.73769 | -47.95678 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3f82cc65-acf3-348b-942d-a65348983a14 | -12.0963 | -44.98722 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| dbba7d72-ac44-38ca-b90a-d30a18ca0cc2 | -10.01988 | -46.15832 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b7c1119c-e904-3b27-a2c1-85730a9650c8 | -10.08533 | -46.62472 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5c01099e-57ef-38fb-8f00-7582a54fc0c4 | -11.92473 | -45.08192 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e00e6d2c-8ced-36fc-afeb-04b06d2cb053 | -8.93013 | -45.03081 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9072134c-c341-381e-bb87-ed59036edf7c | -11.37186 | -45.19119 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9abb6b8c-1b95-37d1-a5d4-eb861f4d3853 | -12.09146 | -45.74637 | 2026-08-31 16:30:00 | NPP-375 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f9d63336-a43f-3bb7-a67d-5ccd4f2e577b | -12.09197 | -44.98337 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5088d3fc-6ea2-3e52-900a-2c02861f2d14 | -10.73334 | -41.84909 | 2026-08-31 16:30:00 | NPP-375 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 26950af2-fd96-34d5-a66c-b06f7770e66c | -11.6526 | -46.75212 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 41b1b38a-304f-37f9-a30f-57f8aef2f29d | -11.20323 | -46.11086 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 55c09adc-1bed-325e-a607-9ec4d27a3e78 | -11.96206 | -41.86848 | 2026-08-31 16:30:00 | NPP-375 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bc697092-5344-37ba-a345-b55e501c3db9 | -12.17402 | -50.52802 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f264f4ba-9e13-30b9-be50-8542255fde38 | -11.92152 | -45.07922 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bc7c6e16-7905-39f6-9106-43bc8d7fbb4f | -11.31973 | -45.19834 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 823dd659-f97e-3926-bc6c-614f3d557cc7 | -10.73822 | -47.96078 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0546cc0-8de7-3656-8202-9f06396cf8ee | -10.01958 | -46.16526 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 16021900-5a26-39b6-b646-3073c3bc9e9f | -10.85523 | -45.36718 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5a011de2-9198-3835-9d54-3d2e6d359515 | -9.20232 | -48.00232 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9e867cb4-852f-37b6-a346-1c584b0c717b | -14.96441 | -54.56928 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 945a00dc-8656-3ae7-9567-965f0c025649 | -11.19987 | -46.08595 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 9968cbd3-d858-3b2c-829f-91ede14e5b9f | -11.2228 | -46.10791 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f543cddc-66b9-376f-bad0-d8fcbfb38044 | -13.27465 | -51.60827 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2a90dfa6-4dfb-36b9-9252-c96646481153 | -15.2607 | -53.87951 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 74353e8b-a30e-3455-b73d-5584247ff0bf | -14.20105 | -46.57306 | 2026-08-31 16:30:00 | NPP-375 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcc85b62-cc8c-34d3-83bf-7aab21a61fa4 | -10.74094 | -47.9812 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4703417f-88b5-3cd3-a8bc-04b4290e06ad | -10.10057 | -50.28291 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 25e59973-3706-3a34-b8a1-507424a9be45 | -9.20904 | -51.5702 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 40f25f11-5197-3b56-823e-17db3576714d | -15.50602 | -55.13974 | 2026-08-31 16:30:00 | NPP-375 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8804c237-77b4-3a81-aacd-c0f9cc6bebf2 | -11.79697 | -47.66919 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| d45ddb33-c801-3b02-9a69-f2bab1d407ff | -10.15847 | -45.76866 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cf241337-9270-3b4d-ba4e-5356e56e6e45 | -11.03159 | -49.67049 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6e8cae5e-ba38-34f1-a975-0888d1a5f6f3 | -10.75023 | -54.03305 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c5de180c-4359-36d5-bef3-0ff9b13bfdfc | -12.98169 | -40.71435 | 2026-08-31 16:30:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fb78ee8e-9042-30a4-84e9-c36b84d841c3 | -11.20387 | -46.08295 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d2a869ce-b3a7-382f-9c95-9e7efb8739cd | -8.73436 | -46.45598 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ad9006bd-8bbe-3adb-a330-cddca9b63137 | -9.44272 | -45.68168 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 06d12968-0253-396b-8538-fc876281f96a | -13.44384 | -51.76023 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 607aeeae-b6a1-35e3-ab03-0ebdd7d83bca | -12.95639 | -45.92785 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| aa1e769a-fb70-3d31-ad10-388d584a3c7e | -9.56874 | -48.32842 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ab7b7827-0d9b-340a-9930-2e512d5dbd6f | -11.64341 | -46.74598 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39af531f-5aa5-3079-b0d2-a152ad301f0e | -13.42454 | -51.69426 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 51951863-b1f4-3061-b3ef-c2dc44026f22 | -14.50193 | -52.19324 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d12c4e45-9623-3c1c-8bcc-27d56ee5f00a | -12.09426 | -47.14183 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a2995b7d-1b71-3919-9de5-bea8189b8750 | -10.98569 | -48.38902 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fe823238-2d50-3d8f-84f7-79e3c74a4201 | -11.37739 | -45.17672 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3aefda2a-fdc3-310e-b872-71ac3360c5c3 | -8.64512 | -47.31202 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c6429ea3-89ce-3a74-a07a-bd8a3ff38e13 | -11.54521 | -45.48863 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ad0ae0d0-69aa-300d-bcf3-482aed1f49f5 | -12.17319 | -50.52129 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10c3dcd3-ab66-361f-b6a2-04ee928f5a1e | -11.24961 | -45.13944 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| accb73ab-0646-3b15-9281-1071462878af | -11.2485 | -51.25922 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b0bfc514-f5fc-3bcf-a89b-200a3fb17f71 | -8.38596 | -44.99474 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4ef239b1-722c-3dad-b07c-2d31c65e058b | -10.74732 | -50.88113 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0900dca8-9903-3457-b7c6-279f923fe614 | -11.02944 | -49.69378 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6d0e5cf1-6a0b-33fd-8ffd-802e6c43278c | -11.24764 | -45.09917 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 35d420b5-f0df-39bd-bbee-346e5f74c5e9 | -10.28342 | -52.37366 | 2026-08-31 16:30:00 | NPP-375 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c53b22f8-0739-3c17-bd0f-d5d3e4538c46 | -10.15721 | -45.70617 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d7fd7b0d-6d43-357a-85ff-f47926face95 | -10.32751 | -49.95909 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6dfe4c50-c8f8-305d-adc7-e95bdb55141f | -11.07029 | -51.52587 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 5a7c7047-51c0-33b6-bd79-efbcb76ea200 | -11.09079 | -51.53026 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3cc04288-ed21-35a8-8bf9-7dc5f819d4d8 | -11.37808 | -45.20812 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6b58c664-4178-3278-8c2a-92bcddcbf938 | -14.47281 | -52.21083 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5d53e8f5-8993-31e8-b980-ceebd3b04bab | -9.59287 | -47.60477 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0fe6535e-1d70-360a-864c-4d1d63bd01d1 | -13.39937 | -51.66697 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 141c25e1-48a2-3518-9885-982b78d46c69 | -8.76494 | -45.38058 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 04bd7f30-0845-3ba9-92e3-1be5dcd84c6d | -10.13391 | -45.89634 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 335a092f-b0ab-3160-999d-e3cd9a6d65e6 | -12.10571 | -45.02667 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9fcb98d9-26c0-3443-b685-0acccbb165db | -10.98758 | -49.68406 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b787b738-7c08-3281-b17e-7cb39e2be64c | -10.74503 | -54.04493 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 82994dc2-2987-35f0-82e9-f2a7e1f5f93e | -11.0315 | -49.67254 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3149f23c-c91b-3bf8-9758-01066b240d6a | -14.95616 | -54.59128 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 199a3961-7a1a-3e19-a2cd-6c30ccbae0cd | -10.85448 | -45.33531 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 57362509-5ee2-3dd0-b29b-e1c8618aa85e | -9.83588 | -46.35686 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea3799dc-5921-3d57-9b85-79e8d999b913 | -9.61611 | -47.61765 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32d88369-870f-3e45-b694-277938ea6af4 | -10.06283 | -48.69385 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README116.md)
