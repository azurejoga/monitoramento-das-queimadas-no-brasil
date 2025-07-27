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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2c9d548-02ed-3dd5-85b8-f2c4aa24bc38 | -7.37293 | -43.43811 | 2025-07-27 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a302380-94a0-307e-89c4-e1b92deddb48 | -14.21649 | -43.95027 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e0ab75b-2f21-3a25-9ae0-a523722b82ce | -10.43188 | -44.18509 | 2025-07-27 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08923ca9-3376-3cb0-973a-b1026d4ff64a | -12.68664 | -46.98698 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb4d3e2c-37fd-34ca-8a0d-b728025d216e | -8.87541 | -49.00774 | 2025-07-27 04:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2dfaab4-5387-3c7b-80d2-8da9d0937165 | -9.92107 | -48.90231 | 2025-07-27 04:08:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f9797c20-b84a-39f0-9543-fd511c5063b7 | -9.43355 | -51.75386 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0766228f-a841-32de-aa29-53b81dcef7d2 | -12.71174 | -46.27785 | 2025-07-27 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1999b744-d929-3ec1-a9ca-c9c2460cf0a1 | -11.11047 | -45.11831 | 2025-07-27 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 560394bb-0410-3903-8fd5-708786765cc8 | -12.6901 | -47.0113 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8bdcdd1-6506-37c7-a83f-f2a7017e3d0e | -7.10295 | -44.90946 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31f92766-c83f-3638-9bbf-6c93fd6c77c5 | -12.70495 | -47.01455 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a06e5c0-3a17-3f93-a0d2-76fd6f2da59a | -9.43285 | -51.75775 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 424d6bf0-5c2f-3dd1-99a1-f38af171536b | -9.66428 | -40.59322 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a6fdf9e-d4f0-38de-91c2-0d6bffb5d800 | -13.12267 | -47.36327 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4801bdca-63eb-3a24-8137-ec718227ae63 | -6.88584 | -52.86655 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c6e569c-46ad-31bc-a54b-14d6e3d71978 | -7.10515 | -44.91857 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eb3dc42-704f-392b-bb20-bb1db8eea9fe | -14.22199 | -43.9585 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| faec3032-7010-3df7-a717-ea0efa5b868c | -7.50776 | -44.42737 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6cff037e-cf92-3acf-8085-9be2a522d359 | -13.12299 | -47.33878 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ef1d48f-b618-3528-959a-13dbceb737f0 | -9.12609 | -45.87106 | 2025-07-27 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 257ce41f-257b-360b-958d-cf3601793990 | -13.49766 | -45.51545 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f626501-4ac6-36ca-85f7-8c5b53457ff4 | -7.90201 | -42.63353 | 2025-07-27 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4af14609-c4b5-317d-9ffe-7973a06be15e | -8.17313 | -43.19306 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b244527-39f1-3f19-b29a-6213e62e94a3 | -8.17086 | -43.2073 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3dec86a0-3456-3952-9501-b87d12a2d256 | -13.71907 | -45.68488 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce9f6844-374a-399f-85fc-29e09ff7f034 | -8.0094 | -48.17599 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4cec6733-0d90-3751-9645-18c7609a1828 | -9.57287 | -43.8727 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd63d44b-1ad9-3ab5-a6b5-8b5bc15e1caa | -13.10073 | -47.35462 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32db1966-7fbd-3dc7-a80b-158286a71246 | -13.50111 | -45.51604 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 673c893b-04e6-3ab9-97da-50e737d38bae | -9.57903 | -43.87739 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05f14368-99f0-34c8-8905-6f58a1526b79 | -12.67766 | -46.9889 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a56c2989-3997-35ab-b9eb-b043e7e63d77 | -9.43422 | -51.75012 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b97577e-4e58-3045-a8d2-aa111f55f2c0 | -12.68423 | -47.00079 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d177b27f-be15-375c-af69-90be2328faa2 | -6.6574 | -58.8661 | 2025-07-27 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e47e5764-63b1-3bbc-81f5-98c273739047 | -6.6575 | -58.8468 | 2025-07-27 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 003e324d-6386-387b-ae5d-9dfd9d2fc50d | -6.639 | -58.8475 | 2025-07-27 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| bb8f2af9-691d-377a-ba18-d8bcd21da5a0 | -6.6389 | -58.8669 | 2025-07-27 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 46f9496c-6fbf-3937-b681-10f970892e32 | -6.6206 | -58.8483 | 2025-07-27 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 53ecd2ef-3628-3d08-be8d-b10fbf19e3d6 | -15.18912 | -43.27546 | 2025-07-27 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ef4ca325-ef15-3a05-921a-15c8df53b99e | -14.96589 | -46.97007 | 2025-07-27 04:10:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17284647-e270-3721-b0e8-3aad9bb80e62 | -15.39783 | -41.5761 | 2025-07-27 04:10:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6cf66790-1c7f-3ead-8d7b-ae4a2bc5706d | -16.25973 | -47.81652 | 2025-07-27 04:10:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 685a7059-5bb7-3d7c-a231-2552a4fff387 | -19.55965 | -45.30033 | 2025-07-27 04:10:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5eb4e8d-07fc-3b93-946d-9d186bec10bf | -17.88653 | -40.45674 | 2025-07-27 04:10:00 | NOAA-20 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1e1304b-fe2b-3053-b747-e70cb685f1b2 | -17.21185 | -44.85173 | 2025-07-27 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08fbb7cf-6171-3f07-aeb1-67a82d253ff4 | -15.73176 | -48.28732 | 2025-07-27 04:10:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 68f623c8-1260-39d7-92b7-6f0ca7325939 | -15.53892 | -47.38641 | 2025-07-27 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50ecfbf7-7dc1-3ba0-ba40-d538d600bc72 | -18.39457 | -53.31968 | 2025-07-27 04:10:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bca04a63-f5ea-3df9-bfaa-328cbe05dd05 | -18.39476 | -44.18402 | 2025-07-27 04:10:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c0309b9-c551-3ed7-aae8-070629911bb4 | -15.95795 | -49.16026 | 2025-07-27 04:10:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c9ef56c-d2f0-34e0-906b-a0044b68b19c | -21.94869 | -47.41948 | 2025-07-27 04:10:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 69fe2a50-eecd-3c26-a473-4e97664a6ed8 | -18.98643 | -48.42033 | 2025-07-27 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53b9b695-93f2-3958-a6e2-596ab1932319 | -16.40727 | -48.92567 | 2025-07-27 04:10:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bbc3ed1c-a7b1-3b6f-9085-3ed77af32059 | -20.11413 | -51.04429 | 2025-07-27 04:10:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2b5eae62-51d4-315e-9fff-8b83c8413312 | -15.18856 | -43.27904 | 2025-07-27 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 58343d0b-b723-3fea-ae52-2eb31d196068 | -17.99545 | -53.16755 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3491837a-2677-3c12-8583-3a85c407a36a | -15.5394 | -47.38818 | 2025-07-27 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e14fc5bc-b53d-3ee5-a149-469e3bfa38ec | -22.0001 | -46.80175 | 2025-07-27 04:10:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b85cb2d-109a-37c4-ac5c-46c4a79b58e2 | -17.24358 | -46.90647 | 2025-07-27 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8af938d-2b48-36e5-bdd5-a4bf97a6116f | -17.98802 | -53.17817 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d0b5a4f-ef58-3aa2-9dbd-9c1633c60c26 | -20.291 | -49.17536 | 2025-07-27 04:10:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b3aecb-a889-3886-85f5-35b2891d5dae | -16.80539 | -49.22338 | 2025-07-27 04:10:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9067bdf-4920-322e-8b60-055e73be86e3 | -15.21052 | -46.81715 | 2025-07-27 04:10:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecedb8a8-d0e5-3ca3-ba77-f4878b0bdc5e | -15.52539 | -42.65884 | 2025-07-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f6d91d8-577e-35bb-a2c4-6cf8ee52ed5c | -18.20388 | -44.61999 | 2025-07-27 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af0ad571-8862-3ad9-80f1-1958ce9d7884 | -18.42681 | -46.42862 | 2025-07-27 04:10:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a26fbee8-9b06-3a02-857e-f1745ae3ac2a | -15.18581 | -43.27492 | 2025-07-27 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50f90337-0689-31c3-bc07-3608d2bde014 | -17.49975 | -45.17447 | 2025-07-27 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25326460-983f-3d8e-b040-78f5b26ff9ff | -18.00436 | -53.17534 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1a030210-6a7f-3060-8c3c-360af3e42687 | -15.52595 | -42.65517 | 2025-07-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd911936-f98d-39d6-946e-cb3163a28921 | -16.72142 | -43.83305 | 2025-07-27 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69b65d79-b0e4-3212-8944-8321317a5407 | -19.67993 | -43.8848 | 2025-07-27 04:10:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da932e7a-74a7-3a97-acd5-3440ca327242 | -17.04722 | -43.76918 | 2025-07-27 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f7c4aa4-7a71-335e-8a1c-07a7571b912a | -17.34238 | -45.70359 | 2025-07-27 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccf84ee1-a67e-315d-ae6e-8939e747cf77 | -18.00373 | -53.17841 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d2e0286-5999-3819-bf9b-0603c9265b72 | -17.99305 | -53.17926 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7833a352-d756-3ca4-b650-6c8d6d09503d | -17.9993 | -53.17439 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f645a1d0-2ac0-3dae-b6b8-9ffd63a39fcd | -20.193 | -48.70146 | 2025-07-27 04:10:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 779c10e3-48d1-3347-b931-642e43b4fb1a | -20.11493 | -51.04021 | 2025-07-27 04:10:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4316781f-04a8-3fec-9a79-567af4e3f6df | -17.9886 | -53.17532 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 285655e9-1e6f-3d94-9eb4-b288bca9cead | -20.34856 | -45.99332 | 2025-07-27 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ebb26fd-9398-3076-80f1-e3b565d4552f | -20.70037 | -46.29235 | 2025-07-27 04:10:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51deb4ae-1a8d-3a09-a5b6-247ca9f19c0c | -14.59962 | -47.98435 | 2025-07-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 342f1748-dcb5-34b8-9dda-e38432e11c6f | -18.22319 | -54.54774 | 2025-07-27 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b44b7a32-f808-3703-929f-c8328fafa765 | -18.00498 | -53.17229 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4bf36ea2-56b3-3f74-aa60-e7e9fadd4037 | -17.2471 | -46.90711 | 2025-07-27 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 074f11ba-5d33-35c7-ae8b-742ec9e0b657 | -20.56963 | -41.72188 | 2025-07-27 04:10:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 051fe236-c3b3-3d19-9ed3-a6736acea46d | -17.99483 | -53.17054 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6eac87c1-4a10-331b-8924-e86934313f22 | -18.39521 | -53.31656 | 2025-07-27 04:10:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b5a307b-8722-3490-a1c1-f586cfa3dfb3 | -18.98356 | -48.41502 | 2025-07-27 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f205485-6ece-3112-ac98-60c4f1479293 | -20.86295 | -45.52321 | 2025-07-27 04:10:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f2b2763-57a2-3c55-aebd-1791531ad4fe | -15.03951 | -49.25823 | 2025-07-27 04:10:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff2ef7c9-2ecf-39b8-9382-900eb6a59f15 | -14.96133 | -46.97059 | 2025-07-27 04:10:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 421cdf8a-bddd-30f2-998e-75d15bb0317c | -15.52817 | -42.66304 | 2025-07-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 24076226-d86b-375b-80f1-cea8a879a047 | -17.24289 | -46.91054 | 2025-07-27 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47e051ff-bebe-3a5c-813e-66ed1c31ae02 | -17.8519 | -40.97078 | 2025-07-27 04:10:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 880d8520-1d39-3384-a0b8-804b3b21ef39 | -15.03609 | -49.25361 | 2025-07-27 04:10:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5c00481-b042-30f9-9cc7-b222f56a4da9 | -21.3405 | -45.63874 | 2025-07-27 04:10:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a3130534-c620-3034-bf65-7e6919cce45b | -18.39088 | -44.18708 | 2025-07-27 04:10:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README13.md)
