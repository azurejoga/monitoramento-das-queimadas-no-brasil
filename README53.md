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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e58ebce4-3336-3a58-921e-97707d26cf18 | -13.16216 | -43.27465 | 2025-11-17 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 3d8abb8b-2170-322c-a3a4-88c2e50afba2 | -13.84328 | -43.05763 | 2025-11-17 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 173b54c1-9456-3f63-8e3c-57c20541a3a6 | -14.3355 | -41.72826 | 2025-11-17 11:40:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 234a79a6-fb58-3b3f-b9b4-0abf8431b35c | -12.89264 | -43.16091 | 2025-11-17 11:40:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 2e5c52f7-b794-3eb1-aa8d-150c26f1e83d | -13.61572 | -43.06853 | 2025-11-17 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6571ad96-aa6a-3c98-a2d7-9e093ab0f3f1 | -15.6654 | -41.84924 | 2025-11-17 11:40:00 | TERRA_M-M | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 5392a967-70e5-3d90-8aa8-c0c620f19470 | -13.94437 | -42.93754 | 2025-11-17 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7509bba2-885b-3f70-8895-6475dfce1584 | -16.67421 | -41.34679 | 2025-11-17 11:40:00 | TERRA_M-M | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 9f250159-cc36-3802-85ca-9c18afcc2386 | -13.94255 | -42.94909 | 2025-11-17 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 55eb92dc-81ff-33bf-bc9b-8287bd17812d | -13.53105 | -41.73933 | 2025-11-17 11:40:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6d5c0895-7ce9-3227-9522-b73151d7fb00 | -13.06517 | -42.52406 | 2025-11-17 11:40:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6ebf0641-be22-3e2f-9ed5-ad5743b7c26a | -12.85665 | -46.02514 | 2025-11-17 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 160459dd-86da-3c59-8b92-16da4e1d17ab | -14.3333 | -42.94297 | 2025-11-17 11:40:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| c7812030-e0ab-3d35-935f-2a53d1124e40 | -15.4297 | -44.18373 | 2025-11-17 11:40:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 100c8aaa-d9d3-3187-8cc9-23ce4a3e1d9b | -13.84511 | -43.04599 | 2025-11-17 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| c78eef0a-380b-3c0a-8684-4a4cd70e059b | -15.10666 | -39.68305 | 2025-11-17 11:40:00 | TERRA_M-M | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 46d7da64-c1ce-3bd1-a370-0248ebdba101 | -15.6669 | -41.83946 | 2025-11-17 11:40:00 | TERRA_M-M | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| b586d66f-47da-3b19-89ee-911a7f756c28 | -12.91813 | -41.7496 | 2025-11-17 11:40:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| aa346dbe-4c6f-3ae0-86c1-8aa9b8095958 | -13.16019 | -43.28706 | 2025-11-17 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 887f1dc7-f89d-3932-ad50-282867cfb5bb | -15.10796 | -39.67395 | 2025-11-17 11:40:00 | TERRA_M-M | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| eb292930-98f3-3068-aebf-68a1a431ed9c | -13.81905 | -42.88062 | 2025-11-17 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| db82dcab-2c4d-374b-8352-f014f9baff9c | -12.72369 | -45.40594 | 2025-11-17 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 2574c227-9e9d-33b8-9689-bdcebc744d8f | -16.72714 | -41.97856 | 2025-11-17 11:42:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d1950c31-78c4-3f2a-af1c-9dfbc8ce62ff | -3.2117 | -43.3494 | 2025-11-17 12:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| ba09a387-c19d-388a-b58a-683fde4baf41 | -3.2302 | -43.3718 | 2025-11-17 12:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 74ef5dd5-38df-34d5-aa73-ead151511143 | -6.3516 | -41.7494 | 2025-11-17 12:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 88159b40-2186-3986-a0bb-22f06542a045 | -6.3328 | -41.7511 | 2025-11-17 12:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 0d39007e-a4d5-3080-bc1a-25853588a652 | -3.2116 | -43.3726 | 2025-11-17 12:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 2b87a474-fa22-3479-8ff7-bcb2e236b3cf | -3.2304 | -43.3486 | 2025-11-17 12:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 817fbc45-4759-32b3-b67f-f95a7689df38 | -5.3254 | -43.0415 | 2025-11-17 12:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| fdfc20f2-3fb2-3fa3-8ecc-127977ac3adf | -3.2117 | -43.3494 | 2025-11-17 12:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3a77bb6d-7194-3151-ba94-38ad8344aa13 | -6.3516 | -41.7494 | 2025-11-17 12:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 761b422c-41fe-35f8-860f-c88327449960 | -3.2116 | -43.3726 | 2025-11-17 12:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 6e456e28-6b60-312c-976c-e0e8e826cc61 | -3.6019 | -43.6099 | 2025-11-17 12:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1bfb3b5c-ed7b-3094-9118-54bc84d86ceb | -6.3516 | -41.7494 | 2025-11-17 12:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 8ee62893-6691-3ef6-a520-cb82d815998c | -3.2116 | -43.3726 | 2025-11-17 12:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1e7d4e1b-ae8e-3ae9-b05c-b66f6149f9a1 | -3.6019 | -43.6099 | 2025-11-17 12:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 3a65cf64-9f6a-3e08-a6ac-1c2a53c0b4be | -5.3254 | -43.0415 | 2025-11-17 12:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 0102f594-8afa-3fae-b60d-da73faed6055 | -5.3254 | -43.0415 | 2025-11-17 12:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 56ac5fff-d549-3f06-8bb5-8e07b1835e7a | -6.3328 | -41.7511 | 2025-11-17 12:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| fd4e7205-d027-39a5-8ec4-a30f2f8c9cb3 | -3.6019 | -43.6099 | 2025-11-17 12:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5158a508-4057-36ea-a4b6-2a7a7eb0ebcd | -6.3516 | -41.7494 | 2025-11-17 12:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| c6b7013f-8faa-36a8-a5e2-02dcc1bbfc91 | -6.3516 | -41.7494 | 2025-11-17 13:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 1a061782-c654-3ff0-b0cb-8988ac541e74 | -3.2117 | -43.3494 | 2025-11-17 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4b85b718-59f4-37d2-9cc7-087a2148d793 | -5.3254 | -43.0415 | 2025-11-17 13:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7cf65d80-18eb-3ae9-ac2e-7b3fa5abbec2 | -8.1212 | -43.5382 | 2025-11-17 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6870e492-a51a-36a4-a562-a3bde3ddf6e0 | -6.1977 | -48.0699 | 2025-11-17 13:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 4f954a91-3b1f-3468-8bfd-6560f2d6df68 | -6.1789 | -48.0929 | 2025-11-17 13:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| b3adec1f-c2a1-341f-a850-2ff0c6c2b4b6 | -6.1791 | -48.0712 | 2025-11-17 13:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 2d7b2372-7b7c-3dbe-9194-d6ec9aad4cc1 | -3.5833 | -43.6108 | 2025-11-17 13:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 00232af0-dc46-332c-a509-0edf13c7fd31 | -3.6019 | -43.6099 | 2025-11-17 13:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 18715984-0f30-3bb4-90c8-963cd352e297 | -3.2116 | -43.3726 | 2025-11-17 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f4bb1f32-6fe3-39c9-bb10-868ab32df5dc | -6.3514 | -41.7734 | 2025-11-17 13:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| a2128742-f54b-3662-8c53-c8c60875e66c | -6.3328 | -41.7511 | 2025-11-17 13:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 68dc8e68-febd-3510-8e8a-77adf09b7c86 | -8.3049 | -43.9377 | 2025-11-17 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b5bd5e48-c9ea-359e-9598-9251bd0303ba | -3.6019 | -43.6099 | 2025-11-17 13:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 61bf286e-21ec-3d72-bfb9-ca579e2071a6 | -3.2742 | -42.1023 | 2025-11-17 13:10:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 35a5f9c3-19f9-3766-b3a6-c29d15fc3c53 | -8.3016 | -44.1931 | 2025-11-17 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 0edfd65a-b44c-3d5c-9f2d-7381251754a6 | -6.6873 | -42.0535 | 2025-11-17 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 9007128b-2445-3a33-a5d6-62639b5b5ffa | -8.3046 | -43.961 | 2025-11-17 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4d2547fb-2d97-3e34-9075-3e7c39ad5fd7 | -6.1791 | -48.0712 | 2025-11-17 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| e29b78a5-543d-338e-b671-cc03838c0518 | -3.2932 | -42.0539 | 2025-11-17 13:10:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1241ae91-3ab9-3ec0-b982-1a0abf696b8e | -5.3254 | -43.0415 | 2025-11-17 13:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3d431fbe-90bf-3476-8701-f5d9c867bf2d | -5.3442 | -43.0402 | 2025-11-17 13:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b44eb2aa-a2a4-328b-a3b9-954a74b6fc87 | -3.2744 | -42.0785 | 2025-11-17 13:10:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 392.8 |
| b4f25ce3-4ac3-3e9b-9463-b7e48e6ab5c6 | -0.7672 | -47.6482 | 2025-11-17 13:10:00 | GOES-19 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 844f44fd-169f-366c-923f-e69f04e37698 | -8.1212 | -43.5382 | 2025-11-17 13:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| fe496e8a-a03e-3602-9862-69f800bfbf5f | -6.1789 | -48.0929 | 2025-11-17 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 3dffb7ee-bb6a-35e2-b2b8-2d3893cafbfc | -4.1638 | -43.3025 | 2025-11-17 13:10:00 | GOES-19 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 95b47c68-9724-31e1-946f-1bdc87cd5a13 | -6.1977 | -48.0699 | 2025-11-17 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 47e6c3e7-577d-3503-b1af-7b8751af57e8 | -7.7135 | -42.9478 | 2025-11-17 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 8d26167c-9f9d-38d6-a16c-408ac72d52d5 | -8.3202 | -44.2142 | 2025-11-17 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 244cc960-028c-31e5-a70e-824373df5c72 | -5.3442 | -43.0402 | 2025-11-17 13:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 224d1bdc-2b0f-3ba2-bac4-8e967dcc34af | -8.3016 | -44.1931 | 2025-11-17 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2888919a-c277-37df-a2b4-5ac9d8818c2c | -3.7292 | -44.1797 | 2025-11-17 13:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8c627b64-0d97-3dd1-98f7-5931b819b8e4 | -3.7293 | -44.1568 | 2025-11-17 13:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 557b86b5-ca35-3305-a8d0-7670648d6519 | -3.6019 | -43.6099 | 2025-11-17 13:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| a2f3ae05-0e6d-375f-8ca1-ecd55e0f063d | -10.0127 | -39.1758 | 2025-11-17 13:20:00 | GOES-19 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 7ff2b063-d51f-3146-b749-eb4a3b2907a9 | -6.3702 | -41.7717 | 2025-11-17 13:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 10ab0a5f-68a3-31a8-a84a-6658e30f3a7e | -8.3046 | -43.961 | 2025-11-17 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1ff8c491-f2c5-33c7-a225-fb63cb6800ff | -7.1403 | -47.1243 | 2025-11-17 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 61bb2c71-5e85-3ed2-afec-fefd0e833935 | -7.163 | -44.9708 | 2025-11-17 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c24194bf-7623-3900-8a5c-4f45ad4cfe66 | -6.1977 | -48.0699 | 2025-11-17 13:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0294fdca-9823-3886-b889-8e8cc1dddb29 | -7.7135 | -42.9478 | 2025-11-17 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 1e3fbdc5-83ab-3e17-bb7b-f809ce235284 | -7.6237 | -42.5788 | 2025-11-17 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| b6178886-95c6-36df-a407-7004207b3a54 | -6.1791 | -48.0712 | 2025-11-17 13:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| c85dbf6e-562f-301d-bb63-f96adb5d1ff7 | -8.1212 | -43.5382 | 2025-11-17 13:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 64fcd730-5b72-3b38-9424-2ee2373400b8 | -5.3254 | -43.0415 | 2025-11-17 13:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 1a23d0e0-7332-3f26-869a-fc7ef50dfd4c | -8.3049 | -43.9377 | 2025-11-17 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 554beeab-96fe-3471-a294-06f90bdf5f12 | -6.1789 | -48.0929 | 2025-11-17 13:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 204.9 |
| fe0e7d6e-a9dd-36b1-b0f0-17dc1f6a6c8d | -7.094 | -42.7272 | 2025-11-17 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| b91b248a-8d49-3695-a9cb-53f011b02a4f | -3.2932 | -42.0539 | 2025-11-17 13:20:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 57028e19-94c2-343a-af44-bbc45e6e8330 | -3.5833 | -43.6108 | 2025-11-17 13:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e3c4ea53-7d60-3e46-a919-3e01adcbaf38 | -6.3328 | -41.7511 | 2025-11-17 13:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| f1f01a27-d77b-3d23-98e0-53eacb9ad569 | -3.6019 | -43.6099 | 2025-11-17 13:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 2839a5b5-511f-3566-8d7d-026d7f505785 | -3.5833 | -43.6108 | 2025-11-17 13:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| ef5de1c5-3959-398b-beb4-afe8e1339b74 | -8.3019 | -44.1699 | 2025-11-17 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 80a52b3f-ac2c-3080-a7ce-1220366e416f | -3.2117 | -43.3494 | 2025-11-17 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 52fbe4f8-8220-3374-8e40-488fbcd6f252 | -7.094 | -42.7272 | 2025-11-17 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 4bb45e40-ab7d-3f85-b139-064ded65bdcb | -3.2932 | -42.0539 | 2025-11-17 13:30:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |


[Clique aqui para ver as próximas entradas](README54.md)
