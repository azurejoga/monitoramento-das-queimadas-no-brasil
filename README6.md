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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ace96c7b-4fdb-3706-93d2-b0409d27554b | -7.0169 | -46.4375 | 2025-11-14 00:38:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60b39c90-e145-3109-b5b0-6ee42686c9be | -3.6612 | -45.935902 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4c6e2b7-3121-3290-98b7-edab73b2f3c9 | -11.1678 | -43.566799 | 2025-11-14 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5423eea5-593c-32a4-8a0f-05212955bfbc | -12.7049 | -45.4203 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc25e88-5b29-3915-a839-33a9e3d8e38f | -10.9229 | -44.588699 | 2025-11-14 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf81f04b-b856-3783-8d47-f9581c5307ef | -10.76 | -44.908501 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b60d486-2034-3370-a3fc-2065e0c0c674 | -6.4309 | -47.2985 | 2025-11-14 00:38:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef8a92b9-488e-3e2d-861c-a41e5c8936b4 | -20.1028 | -41.686901 | 2025-11-14 00:38:00 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c95f458-ac72-3f59-a220-3e5955db4683 | -11.8621 | -49.220699 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36190c97-6aee-307f-a837-785698ec43da | -10.7505 | -44.558102 | 2025-11-14 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b71d089d-2cc2-3966-a760-53ba2e7f2acf | -2.4471 | -48.8153 | 2025-11-14 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5853f109-860a-31d3-84d7-5065b4cee75d | -4.7605 | -44.457699 | 2025-11-14 00:38:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 277a2bda-f313-3a32-a148-51a022e0310b | -17.632601 | -46.702301 | 2025-11-14 00:38:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2dc72041-e21f-3f48-bb93-80d2b577d2ed | -10.3738 | -47.689499 | 2025-11-14 00:38:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12e09e32-5644-3893-8aeb-ebde9ed195dd | -7.9308 | -44.3354 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4d594e4-b565-3022-aeb6-e594773045c0 | -13.5002 | -43.641201 | 2025-11-14 00:38:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4627a987-fea8-373b-aad9-7f4c10b78424 | -7.3555 | -43.3452 | 2025-11-14 00:38:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 481b766f-8083-3589-803f-de1e918e5676 | -12.6654 | -46.748901 | 2025-11-14 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85d12228-de61-30a2-a035-d986a1d37853 | -4.6969 | -46.443501 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f76cddc-1af8-31a2-9305-0493c50be931 | -2.8345 | -45.484299 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1d0146-1125-3755-ad95-74c89a60edd0 | -2.4678 | -48.230999 | 2025-11-14 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e56ca19-1b42-38ad-83fd-d6ed840ad47a | -4.1012 | -48.023201 | 2025-11-14 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4d11202-b6fc-35d6-ba32-9b485932d440 | -3.6514 | -45.938202 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3db23f0b-858e-3de9-aa4c-cc85e6c2dd75 | -7.0153 | -46.4305 | 2025-11-14 00:38:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09d821d0-56d8-3e6d-bcea-1ba68a03f25b | -6.8524 | -46.753601 | 2025-11-14 00:38:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec7a5203-ac27-3e40-8949-465a4bd488ff | -11.9471 | -44.597099 | 2025-11-14 00:38:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48b47af5-f9e3-3adc-b294-c0017b55a36c | -4.5349 | -46.412201 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fa71499-83da-3c8f-8585-d2fe2b2838bd | -6.8863 | -42.849701 | 2025-11-14 00:38:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dbd266d5-3779-333d-adab-9c73448873e1 | -2.8327 | -45.4762 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffb29df3-fed4-3eb2-8cc5-cc1a8c8ec76b | -10.1071 | -40.893501 | 2025-11-14 00:38:00 | METOP-C | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 278ab153-562a-3806-a5a7-7ac752164de2 | -11.2477 | -47.500301 | 2025-11-14 00:38:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae38e1c1-8432-342c-bf40-08c809d6561f | -16.5837 | -42.2099 | 2025-11-14 00:38:00 | METOP-C | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c4196d2-437a-3ac7-8617-6b14eb8770c0 | -4.5366 | -46.419399 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab4641f-1ba7-35b6-8fe9-667662f78a79 | -9.9077 | -47.860901 | 2025-11-14 00:38:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e7df030-9440-3124-b7a9-5050d5c7db23 | -4.4577 | -43.915699 | 2025-11-14 00:38:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed32f88a-d64c-3936-ae02-b0fdbd5b7128 | -9.8105 | -48.347599 | 2025-11-14 00:38:00 | METOP-C | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03504441-5ea0-3039-a29a-31d78a7c9dea | -6.4211 | -47.300701 | 2025-11-14 00:38:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56738a04-bd19-3451-9218-76c01c1bd89a | -11.7415 | -48.524601 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79d20840-2c7a-333a-a83e-d43bfc8e3632 | -3.7497 | -45.739399 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e65d4635-6bf9-3fba-95a2-541aab13984e | -11.9292 | -43.946701 | 2025-11-14 00:38:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da5bba1e-daa7-3a99-b53d-e03c0d66f5b4 | -2.9594 | -45.755798 | 2025-11-14 00:38:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dde56a36-54ac-3ac5-81d0-1a218fc84c9e | -3.3492 | -46.860699 | 2025-11-14 00:38:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e08e1935-32ee-3d44-a5c0-465673773477 | -7.6603 | -45.872799 | 2025-11-14 00:38:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fecafe52-977d-3274-a22e-b32628e76257 | -11.817 | -47.793098 | 2025-11-14 00:38:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee84107d-7910-3d36-84f3-d51841582438 | -8.9127 | -41.0756 | 2025-11-14 00:38:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c71a3d97-e39e-30fa-b438-6bb909540767 | -12.8222 | -43.439701 | 2025-11-14 00:38:00 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39d42446-326c-354b-9fe1-910aecdc9854 | -2.6247 | -47.298 | 2025-11-14 00:38:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f7fff9-99ec-304d-b72a-bbc4eef9da0d | -3.4822 | -45.653599 | 2025-11-14 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c264ae5-6392-338b-adc3-feb42f031e39 | -5.8369 | -47.676998 | 2025-11-14 00:38:00 | METOP-C | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0dd537e-e032-394c-9dac-2b0bfbfdfb8c | -4.959 | -47.716099 | 2025-11-14 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9fe2e1c-e4c7-3dfd-b209-421233df4434 | -12.7017 | -45.4062 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40a0d053-39e9-3ba1-9950-7ca39dbb0275 | -12.1347 | -48.021198 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 989f2cd9-7740-332f-a3f4-cfbd230ad9b1 | -4.0981 | -48.009602 | 2025-11-14 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc6d17a-167b-3f01-9b09-08489144adea | -8.9098 | -41.063599 | 2025-11-14 00:38:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9694d37d-0ad8-3e41-8206-2e260ac99f1b | -4.8995 | -42.907101 | 2025-11-14 00:38:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1d807ff-807e-38de-b2a5-c473968dad32 | -10.7561 | -45.025002 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8b380c2-f3f9-3bee-acd5-4b1cb29c73dc | -7.4577 | -42.564499 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b9ce1b0c-3574-3711-83ed-0d5c0b1b0603 | -3.812 | -44.238602 | 2025-11-14 00:38:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7da9e38b-1586-3eac-9fb8-5594e3ac1abc | -3.9494 | -47.496201 | 2025-11-14 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63ce636a-9cee-3b08-b3d0-2d28e426f919 | -11.8064 | -44.259602 | 2025-11-14 00:38:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22ff91f8-3482-3219-ad61-27eda6a52629 | -10.7617 | -44.915798 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32782f90-f3d6-3f1f-989e-ee475bc12a88 | -3.105 | -45.405899 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86af79aa-770f-3511-8650-ea60edaea10e | -10.3722 | -47.682499 | 2025-11-14 00:38:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71b26121-57c1-3015-b301-b39603f13662 | -3.7203 | -45.834599 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7d20eb9-7b9d-3f1a-b58f-01bf69bea448 | -7.8625 | -44.308701 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 309c01ab-f56f-3178-8fcb-0ad21478606e | -9.4967 | -47.4533 | 2025-11-14 00:38:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c466261e-0e80-3f49-9c61-2ced8bb6b64f | -11.73 | -48.5191 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74d9cd82-727f-3673-bcb1-ded01a901fa4 | -6.1059 | -41.577099 | 2025-11-14 00:38:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 75a3404e-7dc0-3527-b2e2-8423f4a8fa6f | -7.0267 | -46.435299 | 2025-11-14 00:38:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08ae79f8-25b4-3039-b323-8014691abb04 | -4.5904 | -44.304298 | 2025-11-14 00:38:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81f216fc-7f5f-3d92-9822-875dcad94f0e | -6.4452 | -45.662201 | 2025-11-14 00:38:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 660fbd3a-8e3d-3778-b37c-a36bd2e167f7 | -11.7431 | -48.5322 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42878f68-3479-31b8-a6f9-b6b87455d36c | -11.8523 | -49.222801 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb724261-5cab-3767-9dc7-65a1aae5f837 | -6.4533 | -45.652599 | 2025-11-14 00:38:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 000d5265-39d9-33ff-b1dc-9df78f6091b0 | -9.6381 | -40.3344 | 2025-11-14 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88d76409-9566-35ff-a164-2afa2026c10b | -2.6346 | -47.295799 | 2025-11-14 00:38:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c85e3c9a-ccb1-389a-a902-5eefdb898a62 | -5.2966 | -45.073399 | 2025-11-14 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6dbd39-97d3-3476-abd3-043870b82eb1 | -7.286 | -45.461102 | 2025-11-14 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aceb64b7-f4bb-3ce9-bb81-5ae93e1d6fb4 | -2.7943 | -52.9702 | 2025-11-14 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 086d196c-cbbe-34ec-8370-721eac543aa0 | -2.8425 | -45.473999 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de0e7d8e-dabe-3ffc-ba47-42992a420d63 | -10.7255 | -44.0117 | 2025-11-14 00:38:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc219730-4e69-37e2-b6a7-e7320ed79142 | -6.0991 | -41.591702 | 2025-11-14 00:38:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f6f602e-a054-325c-9cc3-21d48c10a6ed | -20.0989 | -41.670399 | 2025-11-14 00:38:00 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 249b2bdc-a213-3484-b087-162400f31ba2 | -5.5997 | -45.177799 | 2025-11-14 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c17e33e-29ec-3f93-ac78-09077470ca71 | -4.2182 | -49.1222 | 2025-11-14 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f528b3f6-0923-3c17-bf85-316fafcc2169 | -2.4486 | -48.822102 | 2025-11-14 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2ccef44-28da-3647-8e6e-74eb6c9d3c28 | -4.7182 | -46.446201 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73326c25-9d6d-3408-af12-8d05040d7907 | -11.8252 | -47.783699 | 2025-11-14 00:38:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d63f2b6d-703d-38e6-9ec6-065e656152f8 | -8.7577 | -45.665401 | 2025-11-14 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a85a673-4912-3d9d-aa51-34ab36a262e5 | -12.7147 | -45.417999 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6573428b-c1af-3210-8887-18f5ec3a838d | -12.01 | -46.7659 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 048335ea-bfd2-3b4c-b438-54c4fdeb5ff5 | -7.8353 | -44.2808 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0ca627-fe17-3a54-9c74-b5578bb2cd12 | -12.6885 | -45.438999 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c5fec00-15a0-3679-90b1-2734f3907aa6 | -5.0193 | -44.5061 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65d20b38-0cda-3710-a3b2-33d53ad1e5e0 | -16.0368 | -44.969299 | 2025-11-14 00:38:00 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a026d925-4420-3353-8d3e-b96661fc4db8 | -4.5246 | -45.611301 | 2025-11-14 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55fe93cd-e40e-31ea-af06-365af66838ef | -12.7179 | -45.432098 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dca42f04-c461-3d58-b5e6-343af11e8ff5 | -3.663 | -45.943501 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30022e8e-4933-3ab6-a473-e2f51a38d1eb | -11.9454 | -44.589699 | 2025-11-14 00:38:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09df0f55-06fa-3558-b32f-e779a157622a | -12.4584 | -43.737 | 2025-11-14 00:38:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
