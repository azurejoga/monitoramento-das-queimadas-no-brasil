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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 663800bf-c6f0-3126-b64f-6bdf779e7ebe | -7.6856 | -44.59229 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f162322a-27d6-31de-8ce7-be96b47861a3 | -7.69434 | -44.57333 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421d76e2-c6c8-3787-974e-ab31ba14e2a6 | -9.19145 | -45.33369 | 2025-07-07 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bacde97-4fac-3eb2-a499-8e7a29655362 | -7.6814 | -44.61419 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7101cac-c110-3721-b20e-b1b65fc7e9af | -7.70422 | -44.57862 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a35d082-e8f4-3025-8f0a-76d7418b4359 | -7.68368 | -44.60323 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ecfe60e-5baf-3ed7-8ca8-c2869f54a3e8 | -10.57561 | -49.13182 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 39b0d48e-ce27-345b-bf03-5cf537db34b8 | -14.19969 | -42.76221 | 2025-07-07 03:45:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 23c2f701-cf1d-3356-baac-b20b55235294 | -13.64473 | -46.81401 | 2025-07-07 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc68a67e-8ee8-32ac-b411-041de1500e27 | -13.01619 | -46.7612 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e86d4db3-e0fb-3a7e-89ef-83208136df4a | -13.42258 | -47.87214 | 2025-07-07 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a1098c9-26d0-3b82-9201-3a316cc16d4a | -17.37782 | -42.48424 | 2025-07-07 03:45:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c1012e5-52a6-3780-95a2-13d7b4bbd5ef | -13.64965 | -46.81569 | 2025-07-07 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a67a0957-e004-3998-807d-7a42dbec69f9 | -15.07754 | -48.9477 | 2025-07-07 03:45:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 142ac450-4a5a-39fb-aec3-eab111229863 | -10.57815 | -49.11953 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 50f13414-561f-3af3-8c6f-752f5c4e152a | -16.2795 | -47.55977 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc147fbf-2fcc-3c8c-bf1e-794b8caa0e85 | -11.28462 | -46.74678 | 2025-07-07 03:45:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dceb8aca-2f18-36a3-9686-9f8bb92e0ad1 | -16.16407 | -40.31012 | 2025-07-07 03:45:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07a1560b-4ea3-3cca-b774-43ea8e4c77bf | -12.37996 | -47.01448 | 2025-07-07 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce094d41-7f92-36d0-8297-84b3049827f3 | -14.12181 | -51.30651 | 2025-07-07 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e1cc8c2-55f8-3185-87e0-20c3f996a0ed | -13.01915 | -46.77494 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1b74823-2c71-3669-9b0a-f9d5c1765506 | -11.27005 | -46.76151 | 2025-07-07 03:45:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c5f4ea0-f409-3144-b547-842b1b36ada0 | -13.65017 | -46.81518 | 2025-07-07 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98a4e9af-49ab-3e08-89c4-b87951b32530 | -13.01999 | -46.77075 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e4d131a-00b7-3afe-b4c7-9e6d0f687610 | -18.03995 | -39.927 | 2025-07-07 03:45:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2df33909-0b20-3f98-82fb-29f9b740483e | -14.01731 | -46.26075 | 2025-07-07 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb66a83c-e46b-3def-b92e-fcb596f9f46f | -13.01608 | -46.76402 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42cfb30b-e17d-3527-b4d3-cb2f0b12887f | -17.70418 | -43.02002 | 2025-07-07 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 539767e7-bfd7-3d7a-a1a5-b57409d07135 | -14.12579 | -51.30246 | 2025-07-07 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| befbd554-c6eb-365d-9cda-94ce0b7e9b81 | -14.02656 | -46.24144 | 2025-07-07 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9fc6d5f-0dfb-320c-9630-d372662ad71d | -16.27561 | -47.55106 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3e093d7-144f-36a5-9d07-9228963c5470 | -15.74715 | -47.78185 | 2025-07-07 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09815d51-af05-3af4-bb1c-00d8598fc066 | -15.59039 | -41.81281 | 2025-07-07 03:45:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 716f7a9d-5df0-329d-a340-f9df28468a99 | -13.42777 | -47.87657 | 2025-07-07 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 314f8b39-1b8e-34c1-afbf-4b1f3f68df1c | -15.74348 | -47.78088 | 2025-07-07 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c3f7592-6a7b-3833-ab05-5d7cc2719a9a | -14.03109 | -46.24601 | 2025-07-07 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e1b159d-d6a7-3a05-ae02-48d195d32cd5 | -15.74267 | -47.78486 | 2025-07-07 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 380dc4ea-daf8-313e-8848-21879f219386 | -11.87992 | -44.89233 | 2025-07-07 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9965f19-daab-30c4-b11a-9912df73801b | -17.40561 | -39.34649 | 2025-07-07 03:45:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fdf52c46-09e5-3ef5-a100-ee5b03422574 | -14.12881 | -51.30822 | 2025-07-07 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34d0d455-5410-32f1-9ef6-c6066e52222d | -13.42328 | -47.86867 | 2025-07-07 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 321c3331-e14b-3c0f-96d4-de1a5184263f | -17.40499 | -39.35024 | 2025-07-07 03:45:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 78bb0d9f-3f2d-3253-abbc-4bda2ddc3b9a | -13.01991 | -46.77381 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 906c7208-8236-3cd3-be69-2961deed6b8c | -16.32532 | -43.61739 | 2025-07-07 03:45:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb8c9b67-9d45-3b74-add6-6ba13ada7b72 | -13.02214 | -46.7623 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5527e730-fa5c-369c-9b51-57dd01491300 | -13.01541 | -46.76508 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9bd980c-fb30-30e1-b9c4-55a3a815205f | -16.27091 | -47.57383 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f61e3d78-3af0-3724-a888-73b8ec3f6811 | -14.12425 | -51.30952 | 2025-07-07 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f762c0db-d47b-3441-9aac-5d89eec27293 | -13.64421 | -46.8145 | 2025-07-07 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ad1c440-5427-341c-94ce-120e521ad228 | -12.37918 | -47.01846 | 2025-07-07 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 850de124-b4c8-3ead-8833-ac92ab395631 | -13.02152 | -46.76315 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0936a60d-b41f-3d3f-90f8-168ed6570ae9 | -14.01664 | -46.26411 | 2025-07-07 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38a8ca52-5fbd-3690-a51a-1db1938fec19 | -16.57351 | -45.14616 | 2025-07-07 03:45:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc4a0a16-21b4-3ccb-acd6-feb57823db3b | -16.27168 | -47.57009 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1187eb50-2739-3f08-8165-12f9ce065c1c | -14.03567 | -46.25034 | 2025-07-07 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2da28c0-1423-3266-83e6-ddd8cbfa6001 | -13.01523 | -46.76845 | 2025-07-07 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8a4e96d-2dc2-39d9-9f88-9281582436a8 | -14.12338 | -51.29951 | 2025-07-07 03:45:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c19484c-c20e-3dec-8110-c8f686ecf0cd | -17.59595 | -43.19733 | 2025-07-07 03:45:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c08b9275-f7a9-35f8-a184-ae72b7e6c8c6 | -16.32458 | -43.62143 | 2025-07-07 03:45:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cde6642-60f1-3baa-955b-ff547cc1ba16 | -13.42651 | -47.8746 | 2025-07-07 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 935e045d-be95-373c-972d-d7ca6c9326ba | -11.27092 | -46.75697 | 2025-07-07 03:45:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| decdd0eb-73b9-3ff0-9d6d-fe8197980c5a | -16.68029 | -43.88592 | 2025-07-07 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c36fc444-6e3b-3d78-b595-0d8051abebb8 | -16.27872 | -47.56353 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72ea9c5f-a249-3c50-988f-dae15e714b96 | -11.27897 | -46.74559 | 2025-07-07 03:45:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ed67df4-121f-3066-86cf-299b3bc5c299 | -10.57689 | -49.12566 | 2025-07-07 03:45:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d8a2130d-c81e-3e97-a3f6-d8d80ef8cb6f | -16.16389 | -40.31139 | 2025-07-07 03:45:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6687b393-885f-321a-bba1-8df5900bdca8 | -13.65036 | -46.81204 | 2025-07-07 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 964246c0-f3b9-3ce6-83c1-230856c3ac01 | -16.68103 | -43.88198 | 2025-07-07 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1d6ab14-8e8e-3979-b786-86211e7237ee | -21.4917 | -47.27337 | 2025-07-07 03:47:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 799ce749-4030-3db7-bb0b-df72dd8a7f0f | -20.76401 | -46.76831 | 2025-07-07 03:47:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 23d51bf5-ff5a-353e-8a6a-48099858576f | -25.19199 | -49.3279 | 2025-07-07 03:47:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c21759a0-3137-361a-a362-600868bf7a7f | -23.97971 | -48.91724 | 2025-07-07 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 35c63978-00c5-3aa2-bcde-26a8d60fda9c | -19.78843 | -44.10215 | 2025-07-07 03:47:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a4a9ef6-3310-37cd-8cdf-ff2bbcc5e4dd | -22.78601 | -43.75479 | 2025-07-07 03:47:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bbaa4d5b-b831-3d7b-b9e9-6ba6bac39f24 | -20.49666 | -44.19508 | 2025-07-07 03:47:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f2c556c-529b-3825-be8e-d115261ef0ee | -19.43739 | -44.33984 | 2025-07-07 03:47:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db713d95-94ab-3662-9d83-a98e673bf5e5 | -22.67801 | -42.85415 | 2025-07-07 03:47:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14deffb0-b2a4-3c74-a4b4-f66d37858625 | -21.17886 | -43.98206 | 2025-07-07 03:47:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 84589cf3-d066-357d-b163-f02bf8d027e9 | -25.4572 | -49.61219 | 2025-07-07 03:47:00 | NOAA-20 | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 581928d5-5f78-3600-a41c-f071f82bf1a9 | -23.98478 | -48.91852 | 2025-07-07 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 479edb77-6573-369c-9c40-b4c8638e27e9 | -21.18124 | -43.97923 | 2025-07-07 03:47:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7ff32e03-6096-3c8c-a950-0b87f209e2d5 | -20.62216 | -41.14819 | 2025-07-07 03:47:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ec2d3c1d-02bb-38cf-bac1-747e3b8c3b5f | -28.58281 | -49.44276 | 2025-07-07 03:47:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a11d0f87-b59e-3fe3-965e-9476550132f8 | -21.49378 | -47.27332 | 2025-07-07 03:47:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6930814-0cc1-3a93-a4be-d5f8c9dc0b44 | -21.35327 | -44.72813 | 2025-07-07 03:47:00 | NOAA-20 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a8475bb-5fdf-3c39-808c-e8b944b7c734 | -23.33917 | -46.77415 | 2025-07-07 03:47:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 26604e13-ac3e-333d-a2d7-5dcbf8e29ff0 | -27.32453 | -48.5848 | 2025-07-07 03:49:00 | NOAA-20 | GOVERNADOR CELSO RAMOS | SANTA CATARINA | Brasil | 4206009 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6930e47a-f76b-3dd1-8248-6f1562f5535a | -28.58365 | -49.44364 | 2025-07-07 03:49:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5ab90845-ea0d-37a4-8457-32fe6aa405f5 | -7.6938 | -44.578 | 2025-07-07 03:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 09ce0672-0833-3fee-9c80-0c1fa65bff7a | -6.1792 | -48.0494 | 2025-07-07 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6d6c0a47-e48b-3850-8bb6-33d5e82d893d | -14.1324 | -51.3017 | 2025-07-07 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 38aea29d-6154-3b9f-a5d4-4236d3fdae8e | -6.1791 | -48.0712 | 2025-07-07 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a1d81bcf-4259-3c2a-b3e8-c266c3fde002 | -6.1606 | -48.0507 | 2025-07-07 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 928071eb-1606-393c-84e5-d73a4c77010b | -6.1604 | -48.0724 | 2025-07-07 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 18db95ee-f3b7-3090-ae37-2c4deafe1edd | -6.1606 | -48.0507 | 2025-07-07 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ba9d122f-63ff-305d-b51e-143fca87159d | -6.1792 | -48.0494 | 2025-07-07 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| ac28b7a5-db2a-3dbb-a8b7-c63144019653 | -6.1791 | -48.0712 | 2025-07-07 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1789fd1d-cc1d-320a-8770-2fcc1cd7a76a | -7.6938 | -44.578 | 2025-07-07 04:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| c55ee6e2-2a2d-3b0b-9e2f-4d49d61097e4 | -6.1791 | -48.0712 | 2025-07-07 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d53847b7-cd40-3e05-a14f-c4cee9bcf447 | -7.6938 | -44.578 | 2025-07-07 04:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |


[Clique aqui para ver as próximas entradas](README6.md)
