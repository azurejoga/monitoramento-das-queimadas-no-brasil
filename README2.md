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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3fcabd-062d-3c76-a7e8-3a8ce0f5160b | -3.2768 | -53.8199 | 2024-11-21 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fe3caff2-af7d-3a8a-886b-daf460cd0069 | -3.2526 | -50.5574 | 2024-11-21 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 76072ba0-1dfc-36ba-9ad0-c37e2fae1925 | -1.7556 | -52.0636 | 2024-11-21 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 93cd75e1-fdb7-3038-85c5-47a239ce0a1e | -2.7676 | -52.1045 | 2024-11-21 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| e4267041-1255-30fe-b1c9-1292c7085a7f | -3.2951 | -53.8395 | 2024-11-21 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 89444818-4a33-3da5-a6c0-b2b9d2fb0d96 | -3.5698 | -46.084 | 2024-11-21 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a78f7851-e0bb-3674-b503-b0322a8910fb | -2.7675 | -52.1251 | 2024-11-21 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| a0ed5313-dcec-3f30-b75e-38c283a92b8b | -3.2014 | -54.3243 | 2024-11-21 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d234eb40-1bb6-3219-8d4f-072e0fcc6cd9 | -3.0354 | -49.4688 | 2024-11-21 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 581c48ab-d365-3bea-926e-98d64e54fe8b | -2.0075 | -54.5292 | 2024-11-21 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 25b875e0-bfdc-3b64-a30f-6dc7fa1d97ee | -3.7383 | -45.8537 | 2024-11-21 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3ec44b5c-91e9-3826-9b10-547edae3e58e | -10.1223 | -65.0237 | 2024-11-21 00:20:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b7eaf94c-cdcd-3841-a966-9a757a2eb86d | -4.5614 | -48.0141 | 2024-11-21 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| f102aa16-9cbc-3701-9e3a-2eb9bd4ef842 | -2.7491 | -52.1255 | 2024-11-21 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 334e6339-89a3-3b83-a6f7-cb831f3574c6 | -3.4725 | -43.4074 | 2024-11-21 00:20:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cdf687bd-4143-333c-9a23-cf7f7d036a41 | -3.5884 | -46.0832 | 2024-11-21 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ac471178-73cd-3bea-9f84-411c9e01befc | -4.5986 | -48.0123 | 2024-11-21 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 3d613c27-d93d-37af-a85b-2ca69162e9c4 | -3.3739 | -52.4773 | 2024-11-21 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 028efe72-cbf4-3def-bb10-f3b705d08ba0 | -22.12838 | -41.70555 | 2024-11-21 00:22:00 | TERRA_M-M | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 88065593-9a08-334a-867e-d6df04fd4f87 | -18.43251 | -40.54915 | 2024-11-21 00:22:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 30df1a68-f427-31cc-9c2c-3de64c036b21 | -18.4338 | -40.55919 | 2024-11-21 00:22:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5c7799a2-f6ff-3281-94d8-3b294cd05a1a | -18.4233 | -40.55049 | 2024-11-21 00:22:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b7ac38f8-c591-361e-be1b-c374aedb9d6a | -9.40083 | -43.31764 | 2024-11-21 00:24:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0e877eab-c3d0-3535-a2a1-380b1077f6a0 | -8.33624 | -43.8989 | 2024-11-21 00:24:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 219aa9ae-6bad-3e9a-96b5-c7622602bbbd | -13.92279 | -42.93601 | 2024-11-21 00:24:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f3697801-d5af-35c9-9e85-26e824317bef | -10.45328 | -40.3838 | 2024-11-21 00:24:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 864bcda7-5002-33b7-a8c5-8d9ade2316cb | -12.27712 | -43.53431 | 2024-11-21 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6ffa29e5-0f60-3029-b69d-6927e508d0d9 | -10.69187 | -44.91593 | 2024-11-21 00:24:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3ea218b2-790d-3955-9290-fe48fecc8d7a | -10.79927 | -44.95238 | 2024-11-21 00:24:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ad93c851-b498-3de8-8c2a-9ad689505434 | -9.16682 | -43.16076 | 2024-11-21 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1599b0f0-d6ee-34df-a500-4e820678518d | -10.05383 | -42.37179 | 2024-11-21 00:24:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| afb50764-e844-33d5-b000-d563e2599086 | -8.21084 | -40.94342 | 2024-11-21 00:24:00 | TERRA_M-M | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8dc6ab52-a736-3591-87f5-83664e5448a0 | -9.13162 | -43.11332 | 2024-11-21 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 26cf4fad-3d90-3575-941c-9f35ed9d8ee0 | -9.09764 | -43.18621 | 2024-11-21 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 46bfedbe-5de1-3076-b9cb-7c26f1eefea7 | -8.14828 | -43.79242 | 2024-11-21 00:24:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1d149eaa-1a06-3b1a-975d-2006b9d145b4 | -9.09902 | -43.19648 | 2024-11-21 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 317cbf92-9285-3115-ad13-c63541e984be | -6.7649 | -35.32174 | 2024-11-21 00:24:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 4aa78c1e-d60f-3cc2-806c-f93d17884515 | -9.41041 | -43.3163 | 2024-11-21 00:24:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 6aebabc3-28a0-337a-96ee-fcdf46837791 | -11.74683 | -47.239 | 2024-11-21 00:24:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9a636b05-685b-3355-a459-cb2657682bde | -8.74423 | -37.26083 | 2024-11-21 00:24:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dcbea327-15fa-3012-98a9-5b0b282638bd | -7.48211 | -35.12121 | 2024-11-21 00:24:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| b5ffd80f-7d7f-37a7-89ad-7569d201e87e | -12.08346 | -41.32576 | 2024-11-21 00:24:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2755c030-647e-3a26-bd55-70a4c2b9c6d1 | -18.16199 | -42.46833 | 2024-11-21 00:24:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b12dc5f4-3834-3e8f-afed-8508ca8402f8 | -11.738 | -47.24645 | 2024-11-21 00:24:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7f2122fd-dcb5-3087-972c-2e904314fb2b | -8.52343 | -40.7378 | 2024-11-21 00:24:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 22cf67db-15d7-37a8-bdcd-6b7c502d0729 | -16.41387 | -40.91057 | 2024-11-21 00:24:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 03129085-3bfd-3722-9e73-d017b6d322c0 | -12.44659 | -43.18654 | 2024-11-21 00:24:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bb8ee42b-3230-3037-b204-14e16c949bd9 | -12.29736 | -43.53796 | 2024-11-21 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ef2dda47-a7ff-3aa2-901c-1396f6634ebe | -9.05636 | -40.53273 | 2024-11-21 00:24:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 22114286-089b-3983-8138-afb698e0b457 | -10.69008 | -44.90192 | 2024-11-21 00:24:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ddcf26c3-b15b-3df4-8586-488b900ffed0 | -16.43525 | -42.26139 | 2024-11-21 00:24:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4b44ac64-44f7-31eb-98f7-6cfc3a7f848a | -18.16047 | -42.45583 | 2024-11-21 00:24:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 39f18c3c-eaa5-3bbf-86d0-7bd92a771153 | -9.05762 | -40.54167 | 2024-11-21 00:24:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 20.8 |
| eb583a34-bbbc-34bb-8da1-e9a5fcd5b9ce | -10.40537 | -39.91321 | 2024-11-21 00:24:00 | TERRA_M-M | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1e6d5117-b0da-35e8-b2cc-4fd1fbd1278d | -13.01299 | -40.18568 | 2024-11-21 00:24:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9cd9d6e3-ed53-3422-bef4-2f80a1c2bc90 | -12.18761 | -41.34631 | 2024-11-21 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 0ca8727b-0331-35b3-af52-76b4d57c54c2 | -9.13027 | -43.10312 | 2024-11-21 00:24:00 | TERRA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8d3db71a-999f-3488-a3fd-102c1bdbdd2e | -10.11873 | -36.20008 | 2024-11-21 00:24:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| af335b5c-9356-31ae-ab2a-f81fa8e7db32 | -12.18885 | -41.35553 | 2024-11-21 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| d4eb8caa-179b-3f49-b437-3f41bef460e7 | -9.19425 | -43.0363 | 2024-11-21 00:24:00 | TERRA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8dc7a4da-3604-3f27-85bf-1b3225b81931 | -8.74275 | -37.26737 | 2024-11-21 00:24:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ed0edf4d-bb76-37d2-971d-b80d733f8e08 | -16.43612 | -42.2549 | 2024-11-21 00:24:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0b2efa6a-8007-3868-9cf3-2835fa6f8b55 | -17.60068 | -40.63955 | 2024-11-21 00:24:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 7a250a59-4ea0-3e93-baf7-5f6438beeb12 | -7.82571 | -43.23028 | 2024-11-21 00:24:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9bb5c8f0-426c-373f-aa95-c20e2c51bac9 | -3.12317 | -45.08435 | 2024-11-21 00:26:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e352b392-ce40-3f71-ad56-d56976422fee | -4.76837 | -44.48688 | 2024-11-21 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2973c901-e4e9-3107-8e6d-e88fa397cd54 | -4.66308 | -46.4012 | 2024-11-21 00:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 67e69810-d5d6-35b1-9629-ff8e2ca2c54f | -4.00806 | -43.24798 | 2024-11-21 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9a779346-ad44-3929-bab2-2078ebf93417 | -2.76338 | -52.12645 | 2024-11-21 00:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 7a9e573a-b131-34c4-9491-7ecec5f684ac | -3.74181 | -45.86696 | 2024-11-21 00:26:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4189d660-3ca0-38aa-a5f9-a6e7698f3b34 | -4.6479 | -49.55945 | 2024-11-21 00:26:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 37645bd9-c93c-3d1e-8a09-efdab8c2b37d | -4.96044 | -49.84894 | 2024-11-21 00:26:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 38cc6a01-c437-3d8a-b58a-ce5ee817fb71 | -2.76466 | -45.1411 | 2024-11-21 00:26:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 835ee1ef-8fe8-3f9d-8b7d-c21ce2d60ae3 | -3.59002 | -43.62308 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c049d0e5-762c-39ea-b89e-291103e1d024 | -5.41467 | -46.4455 | 2024-11-21 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0f404949-06b3-34c0-ac0c-0fcbadd4e820 | -4.15264 | -43.8881 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 64c62c44-d9e8-3c37-bc58-337c43ef69db | -6.38925 | -38.16058 | 2024-11-21 00:26:00 | TERRA_M-M | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1d8fb336-e20e-392f-907b-213414241473 | -1.091 | -48.2145 | 2024-11-21 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8c505d9f-1fdd-3755-a105-662d7555305b | -4.76984 | -44.49759 | 2024-11-21 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a28cc1b6-edd7-39fb-8ec9-ad52459dad15 | -4.24744 | -46.12755 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f4d377b2-9324-387d-b7a7-dbbe1e9ecf7a | -5.19993 | -47.7509 | 2024-11-21 00:26:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 38f07a30-e958-39bd-94b1-ebff709d64d6 | -4.61064 | -45.7388 | 2024-11-21 00:26:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a82d94f6-c5f4-35f9-ba5e-1a81ca57dff6 | -4.75894 | -44.34718 | 2024-11-21 00:26:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| caa9b884-f0bd-3caa-95ce-2d96f9e6f3e8 | -5.72262 | -44.81547 | 2024-11-21 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 229d17ee-c6f6-3d88-bb26-3b7c04a5ba61 | -3.28573 | -45.60152 | 2024-11-21 00:26:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| af5b9301-7c03-3e12-ad85-5bb5c7527f22 | -2.999 | -40.23265 | 2024-11-21 00:26:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4594c155-9f26-3f31-a106-6826b93b4a1f | -5.95216 | -44.25531 | 2024-11-21 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 099f406b-3d0c-336d-ac27-26cea20e5b3f | -1.79118 | -48.46043 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b91908bb-9b42-3f73-ab29-6abe1b2c8c89 | -3.29738 | -49.18211 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 14bc35f2-b98c-3c56-8097-198b9fc8de75 | -4.10071 | -42.98536 | 2024-11-21 00:26:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1684d768-6606-3c6c-973d-f773762bed68 | -3.28612 | -45.97281 | 2024-11-21 00:26:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| d7760356-327c-3949-a176-eb718c6dcf87 | -3.57708 | -46.08582 | 2024-11-21 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ff7b2208-8ac1-3ff6-aa99-dcc2c1558f6a | -2.43389 | -46.53897 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 360004b9-c287-35e6-afcb-81912d2c3efb | -1.08419 | -48.20417 | 2024-11-21 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9f43ea6a-7ee3-38ad-ba86-369db8951899 | -4.39627 | -45.58768 | 2024-11-21 00:26:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 2938e462-9707-32b1-9e9b-6a6eeceaadbc | -1.23859 | -47.36115 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d891da35-e4ff-35e8-bcad-092b89590c81 | -3.4684 | -43.40736 | 2024-11-21 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| b2057c0f-5484-379f-982d-b0ccd5f7f518 | -6.88411 | -42.47195 | 2024-11-21 00:26:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 632c88d2-8a20-3527-b851-7f956cdb23a5 | -4.22823 | -47.18963 | 2024-11-21 00:26:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 026bf7ee-19c8-3c7d-829a-1d984e6f2f88 | -4.39276 | -47.75527 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |


[Clique aqui para ver as próximas entradas](README3.md)
