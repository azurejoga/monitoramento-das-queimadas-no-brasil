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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5837bd39-bc95-3bb5-bac8-6da45e25ebb1 | -21.0505 | -48.6616 | 2026-04-29 00:00:00 | GOES-19 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| 968c76fa-3544-3890-90a1-1e8f508f6ee2 | -21.241 | -49.1715 | 2026-04-29 00:50:00 | GOES-19 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| d97c95a3-803c-388b-8eeb-0fcce84dacb9 | -16.6692 | -41.8544 | 2026-04-29 00:50:00 | GOES-19 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| 1484df3a-7a27-3da6-b70f-f49d6213440d | -18.00945 | -53.00858 | 2026-04-29 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 272bd5de-c997-369b-8d62-14dc2a31d9f0 | -18.49894 | -55.51366 | 2026-04-29 00:52:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 3c5373bb-ae72-3cbc-a013-41df46750543 | -18.28995 | -54.61241 | 2026-04-29 00:52:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d4b30cdf-01e9-3a7e-9917-8cae044c1ab7 | -17.99896 | -53.01048 | 2026-04-29 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bd1e768d-5588-31e0-83aa-4c811fa8235f | 3.45515 | -59.95697 | 2026-04-29 00:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 676919f9-4207-39fa-83e1-77350bb1a598 | 1.9411 | -60.37942 | 2026-04-29 00:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc6055c1-fd17-35b7-b431-5465729c65b2 | 3.45646 | -59.94745 | 2026-04-29 00:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f7ca4597-fe6a-3af2-9752-da006b156bf6 | -4.86386 | -47.40593 | 2026-04-29 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b667656f-f62f-34dd-8f0a-092693ef42c6 | -5.24907 | -37.89896 | 2026-04-29 03:42:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 30036894-12c4-3111-94da-6fad17b3911e | -4.866 | -47.41069 | 2026-04-29 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c99918f-622b-3d75-95c4-a69eba831edc | -4.86279 | -47.41183 | 2026-04-29 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88400d88-2ab8-36d8-a007-790dd234af11 | -10.78301 | -44.56143 | 2026-04-29 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e946c9c-d6aa-3046-a080-67beeee446aa | -12.83921 | -43.81524 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1f0a8ce-1122-39dc-8e52-564c12ace274 | -11.1352 | -45.14119 | 2026-04-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 097cfbda-0a73-3d80-bd81-4c620c2ba7aa | -8.5757 | -44.10046 | 2026-04-29 03:45:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a8927dc-0b36-38fa-b570-f9dc04b16020 | -6.29903 | -43.6324 | 2026-04-29 03:45:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| becf428d-a156-306f-b22e-695f8539f588 | -12.68202 | -43.82537 | 2026-04-29 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07f59dab-6998-371f-9c8e-37c3648c4f42 | -10.60545 | -44.96035 | 2026-04-29 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1e454af-9cc4-381e-97d8-5fc53a56fe5e | -12.8301 | -43.8199 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f93eee9-4a92-35ec-8800-2477a72945d2 | -9.11871 | -40.31339 | 2026-04-29 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 12b1581c-88af-360f-bbc1-1821431bac2e | -8.23332 | -43.88506 | 2026-04-29 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 369f3d22-6e8b-35c4-b589-d1bf960f76ed | -8.57516 | -44.10344 | 2026-04-29 03:45:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7aafcf8-93af-349d-af75-cfef6a7b61cb | -11.52741 | -37.78474 | 2026-04-29 03:45:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 29c4260f-88ed-32df-92ac-e9151e63ab52 | -11.13578 | -45.13809 | 2026-04-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 009ff930-eecd-311f-b039-c54935278d5e | -10.78358 | -44.55837 | 2026-04-29 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 315a1a88-7fc0-3a3d-acb1-aa34fc285ff1 | -11.12999 | -45.14029 | 2026-04-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0c7c627-709e-3fac-b26f-84dbcd69c087 | -8.23281 | -43.88795 | 2026-04-29 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9ceaaf7-0479-3396-8135-bf336da2b26e | -12.83275 | -43.82409 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9e1305b4-04ed-3bc7-9dfa-ae8fd2c2020b | -12.83472 | -43.82078 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 169a81ea-046d-318d-adcf-cb55b14b37de | -12.84023 | -43.81679 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7bfc7965-d7e2-3c46-b09d-b46ecd29fbee | -11.13057 | -45.13716 | 2026-04-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d06d9705-cf87-360a-aad8-22f3798c78b1 | -12.84383 | -43.81611 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d22b5213-b345-3e25-9430-4d14ca245799 | -12.83368 | -43.81922 | 2026-04-29 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48f11d2a-2dc0-3130-860a-43582fbddf1b | -12.68112 | -43.8303 | 2026-04-29 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb235ca4-b8ae-3cf1-b46d-1c817768855d | -20.01242 | -40.22182 | 2026-04-29 03:47:00 | NOAA-21 | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7dee3ed6-6a3c-3a85-9f27-abdd5d2c2fbb | -19.31898 | -40.05645 | 2026-04-29 03:47:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c07f3084-f888-3e56-b1da-cf2a5090d9e0 | -19.69124 | -42.03777 | 2026-04-29 03:47:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fb89854f-5f99-3565-a0a6-f484340c5e33 | -15.63025 | -41.23 | 2026-04-29 03:47:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4b7d7b4-dc48-3c90-9dd2-a513097c862b | -14.47451 | -46.99318 | 2026-04-29 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f340181-1be7-337a-b613-c8ef10496e0b | -14.05678 | -44.08898 | 2026-04-29 03:47:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 24c42bdb-7fb9-3375-9110-c266b5c223dd | -15.89231 | -43.46724 | 2026-04-29 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d883eb8e-238d-3d89-af03-8ab4603380f1 | -19.97955 | -44.85587 | 2026-04-29 03:47:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e95f1b0-dbe5-3a4c-bd73-312e7e75a541 | -17.22402 | -44.30686 | 2026-04-29 03:47:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91d5990d-9360-3764-97b5-0926f36d5e1b | -16.61243 | -43.37029 | 2026-04-29 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cfda4b0-c65f-36be-8a8c-f8fcfcc0e0c8 | -16.67039 | -41.85117 | 2026-04-29 03:47:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c7276604-2764-385b-be73-b8deadbd6150 | -20.21518 | -46.47677 | 2026-04-29 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e74ae055-3749-3f63-a388-d2adbcab58f9 | -14.06138 | -44.08988 | 2026-04-29 03:47:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0cb1713-5b06-3611-b3b8-a84fb953cb6d | -15.88803 | -43.46642 | 2026-04-29 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e17de53-ef86-3ef6-a16c-94641e25832b | -19.62466 | -40.0791 | 2026-04-29 03:47:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 346bd18c-4c7e-3d62-a0d1-87dd21d2a770 | -13.68259 | -44.29309 | 2026-04-29 03:47:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbf8921b-0583-3920-9ee2-5b268a598b22 | -16.67127 | -41.84615 | 2026-04-29 03:47:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8a98359d-6b54-329b-9891-ef798fdb761c | -20.2163 | -46.47131 | 2026-04-29 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ef11ecd-84e1-391a-8dce-ed05482ba3bc | -20.01178 | -40.22573 | 2026-04-29 03:47:00 | NOAA-21 | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f101c636-2640-3bb1-abab-5b6778c7dce7 | -15.89152 | -43.47145 | 2026-04-29 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8417ebb0-b530-375b-a01d-458a239b3f1f | -18.88476 | -41.99532 | 2026-04-29 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0367b1ae-fd60-3973-9d8a-650126d1e57c | -17.22842 | -44.30775 | 2026-04-29 03:47:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a9c9a1c-76ec-3e3c-bfa0-e1aeafc4b3d3 | -15.34867 | -39.45262 | 2026-04-29 03:47:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 00c7d3dd-b17e-339f-a08f-8b06117d6c92 | -16.6751 | -41.84686 | 2026-04-29 03:47:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7e95106f-c2d1-3d74-b570-bf8761d94f6b | -18.01021 | -48.17751 | 2026-04-29 03:47:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eb09816-3eda-3dde-9b45-e2b13815f84f | -18.89499 | -39.9208 | 2026-04-29 03:47:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1043d8a6-ec8c-3d67-b0ec-326e063e5f57 | -16.60822 | -43.36954 | 2026-04-29 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1c10294-46fd-36f7-974a-842e4533a3d8 | -18.89433 | -39.92468 | 2026-04-29 03:47:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3866d12-3471-35f1-ba2b-5cf318a11d9c | -19.74347 | -43.99354 | 2026-04-29 03:47:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54e6cdbd-7d1c-3cdf-88df-f50ec1b5602c | -18.93347 | -48.0672 | 2026-04-29 03:47:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2e5ce24-fd6c-35f2-b926-ebb54c7f44ff | -18.0094 | -48.18128 | 2026-04-29 03:47:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aec3efe-6c8c-3409-8214-5d7a7022a85f | -14.79251 | -42.81029 | 2026-04-29 03:47:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b51b7ca5-ddce-397e-82aa-648250d31de8 | -14.47527 | -46.98938 | 2026-04-29 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6c24763-a40d-393d-b904-0f5e9675cc9c | -21.25507 | -49.1667 | 2026-04-29 03:49:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 075efc1b-6a49-38a2-bc2f-11bd4292336f | -21.05022 | -48.66549 | 2026-04-29 03:49:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7adaa25d-5b4f-3c96-9ceb-eb95f7ede6ee | -21.25416 | -49.17074 | 2026-04-29 03:49:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3f3c9599-cbd2-34ec-95e4-30f3e3b7ee65 | -21.24773 | -49.1734 | 2026-04-29 03:49:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d8a02995-53fc-3cbc-a33a-1fb1cb610da0 | -21.04943 | -48.66909 | 2026-04-29 03:49:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3ecc7617-0b2c-3ed2-b447-323807f9b3bd | -21.24864 | -49.1694 | 2026-04-29 03:49:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2cd24550-c175-3420-8ff6-97c5f8b069d9 | -20.60527 | -49.75817 | 2026-04-29 03:49:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc73083b-e647-39a0-b1a7-60db2b8b03a2 | -20.60628 | -49.75374 | 2026-04-29 03:49:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 080855af-8cd9-3ea3-ae93-f5797f529042 | -21.24956 | -49.16529 | 2026-04-29 03:49:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| acca57bf-14de-3bb1-9d0c-3619816edf40 | -4.86632 | -47.40665 | 2026-04-29 04:34:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df9991ed-9776-3ebe-8fa5-d0e3dcd43666 | -0.08965 | -51.28086 | 2026-04-29 04:34:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d960429d-d5f7-3284-ba71-5df077f696ec | -6.30018 | -43.6326 | 2026-04-29 04:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8bc0475-6d5d-3fa6-829c-9d811d506f7a | -2.26007 | -47.85954 | 2026-04-29 04:34:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc53b2b8-b0c7-3fd6-a7ae-59c05bb30c6c | -5.54268 | -46.21179 | 2026-04-29 04:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7da2355-300c-30e2-a2e3-36d3e240f8c9 | -4.86301 | -47.40614 | 2026-04-29 04:34:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd3c07a-6239-3d2c-99ae-10e17a52aeab | -1.02134 | -48.04355 | 2026-04-29 04:34:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a536f508-9a38-3faa-82e7-71e887c1fbb0 | -4.86247 | -47.40958 | 2026-04-29 04:34:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e291f445-9664-3229-ae6c-6009e6b63cab | -7.02391 | -45.68871 | 2026-04-29 04:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c118b05c-cdc2-3a2c-a971-73ae715f9e71 | -6.29636 | -43.63201 | 2026-04-29 04:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4536299c-d5c5-3516-a681-151d45ad3839 | -12.82929 | -43.82021 | 2026-04-29 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 723cfb0f-5876-3ec2-99f0-aed8d0ad7d45 | -14.05976 | -44.09041 | 2026-04-29 04:36:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 675f4ec8-e1e5-3832-af37-883bd457905b | -8.58753 | -44.10143 | 2026-04-29 04:36:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 144209aa-6275-3672-83a1-33b494e5ce8f | -12.84222 | -43.81814 | 2026-04-29 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b8a9105-e856-3dc2-b8c6-dc9ac39afdb8 | -8.23186 | -43.88348 | 2026-04-29 04:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34ebb4af-fc46-392f-82f3-ede771d165e6 | -8.57986 | -44.10036 | 2026-04-29 04:36:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b3e73f0-2204-355c-8d80-4b6690adbd7f | -11.94163 | -58.0912 | 2026-04-29 04:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85c84922-6a5f-303f-8b63-2b5a797a1570 | -12.45176 | -43.73813 | 2026-04-29 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f8ba67c-10ef-37d9-89d5-1b937f3288b0 | -13.6849 | -44.29087 | 2026-04-29 04:36:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4a0fa3e-61b8-3bf3-a0a2-9baff1a1e08d | -8.23375 | -43.88745 | 2026-04-29 04:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f99861e2-b4a1-34fb-9431-90a8415a2963 | -8.0482 | -49.41698 | 2026-04-29 04:36:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
