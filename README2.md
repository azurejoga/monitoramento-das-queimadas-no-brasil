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
| a8e680ae-942f-3c50-ad3f-fd8385f3420d | -21.40778 | -43.8817 | 2026-07-16 03:38:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6e11a4f8-b8d7-334f-b6ad-61f911326c83 | -17.59214 | -44.60045 | 2026-07-16 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a327b9b-2805-3f3c-bd5d-ccd36151b358 | -21.6194 | -41.21324 | 2026-07-16 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66091568-5d2e-34da-ae61-63ce3e81a2ef | -21.65687 | -41.32425 | 2026-07-16 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a1656d5-546d-3e75-9839-0f83d401c8b8 | -17.70489 | -42.6586 | 2026-07-16 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 49f8900c-05f1-3f56-a67c-475d46e168fd | -16.14501 | -43.6343 | 2026-07-16 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b747ba1-4d9b-36ca-b48b-26d9b88c1cd7 | -21.40689 | -43.88358 | 2026-07-16 03:38:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e96a22db-7b9a-3688-9a12-db091c2d1652 | -21.6196 | -41.21247 | 2026-07-16 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c303dc20-9afb-388a-bce9-7dd2ff417c04 | -21.40186 | -41.2094 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd918c4e-d601-3146-9095-19bb3d4b48f4 | -22.37688 | -49.79509 | 2026-07-16 03:40:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6f7bea57-c4ca-364b-a539-dbde898d1d66 | -23.55893 | -47.51981 | 2026-07-16 03:40:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6852a53a-4591-3e9b-a461-416033303b50 | -23.55999 | -47.51535 | 2026-07-16 03:40:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 07980aac-311d-3ab7-bb94-2d849d7e02c8 | -23.55855 | -47.5172 | 2026-07-16 03:40:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ba6c977b-40c2-34c8-b235-ed273220219f | -23.56423 | -47.51867 | 2026-07-16 03:40:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ebec3bf9-6a95-359d-ab70-086fe44ae565 | -22.37359 | -49.79383 | 2026-07-16 03:40:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a9f45fd5-fd93-3d3d-8b30-099137f3216a | -22.38176 | -49.78912 | 2026-07-16 03:40:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 815a0d0d-c2d8-3567-89b2-10d6027d3127 | -22.37857 | -49.78836 | 2026-07-16 03:40:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b45d37f7-48c3-3d44-90b3-f8912fb4decf | -0.09097 | -51.2824 | 2026-07-16 04:17:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c493cf7-54c2-3cb3-9e76-03752928bdd3 | -1.64353 | -54.46423 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56d9220f-1b66-36c1-a73b-9c8613f00d8d | -4.66195 | -43.22137 | 2026-07-16 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 318bda68-efb5-30aa-af46-f75bd4b97f81 | -0.99729 | -48.0881 | 2026-07-16 04:19:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b93183a-de9c-33ec-a235-b23e33cf9ec7 | -8.76361 | -43.93968 | 2026-07-16 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc0686ed-7674-341d-9e24-3d6bbe813092 | -1.63752 | -54.46343 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52e764cb-53e9-3862-aaee-d3f4e7b69492 | -1.82469 | -54.48095 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 667811b2-6c00-3de9-8fad-4460ef2e08c5 | -1.48931 | -55.28312 | 2026-07-16 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc5925d8-a8e9-3699-b80d-6dff55f54bf8 | -4.65862 | -43.22085 | 2026-07-16 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea25b08b-7a6d-3b04-84bb-a3a8248c82f4 | -4.80806 | -43.0018 | 2026-07-16 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b71457da-432e-35a6-b691-105bfd7b1a2a | -2.76674 | -48.57427 | 2026-07-16 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d0c897e-6576-3f39-8e63-f9595ff1e0f6 | -1.57636 | -47.75327 | 2026-07-16 04:19:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 222ca33c-db1c-3687-b6a0-c3cc9a21f90a | -1.64285 | -54.46835 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ee72041-61b4-3855-aacf-c4fcae0a3587 | -8.75917 | -43.94634 | 2026-07-16 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6d008c9-d1e1-3d38-aed7-82520e658c7b | -1.48299 | -55.28218 | 2026-07-16 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f94e82-2227-36d5-abfb-9a9fabb9079b | -1.82154 | -54.48185 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43fe163d-d92e-36fe-a302-a3168292c887 | -2.79538 | -49.52531 | 2026-07-16 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce2dc02c-e74b-3edd-940f-19a219945eb0 | -9.30098 | -40.3686 | 2026-07-16 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6c3dfbcf-b9f0-3607-9485-5faea06328eb | -7.73284 | -44.56319 | 2026-07-16 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae063480-dd95-3cd9-aab4-a6fee71d3303 | -3.05495 | -39.92818 | 2026-07-16 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 429af7a8-5eea-379a-ab19-bafa6af7ec7b | -4.66032 | -43.2319 | 2026-07-16 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f47f4d0a-4d43-3935-9f7a-1777146de500 | -3.09743 | -49.35403 | 2026-07-16 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a37bcc8a-1288-3f90-8f7b-c9f52222281c | -5.30938 | -43.05647 | 2026-07-16 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 315efadd-54ac-35f5-9749-d34b6bb08e22 | -1.48622 | -55.28215 | 2026-07-16 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80a39c42-692f-3675-a5bb-493cde386cb2 | -3.09682 | -49.35777 | 2026-07-16 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9cce5a-ceaa-39a9-91fb-1daad1c7f9ee | -1.63681 | -54.46777 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c8b829f-f55f-3723-a2d8-54ec1abcb560 | -0.99777 | -48.08514 | 2026-07-16 04:19:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abdad9a4-94a1-3bb0-82c2-e89bb46fc293 | -2.76644 | -48.57134 | 2026-07-16 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f6024b5-0396-3fba-aa76-4a2f1fa3941c | -2.50328 | -48.35836 | 2026-07-16 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d8beb26-aa98-3a59-a4e7-6f2cabff8da6 | -1.63609 | -54.47216 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd7a4b3b-8e8a-32a1-bc2b-96df069929fb | -4.65753 | -43.22788 | 2026-07-16 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a9731ed-2df6-392d-b298-dea935793233 | -2.9402 | -40.0976 | 2026-07-16 04:19:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f261833-198b-31fc-9e80-9197dda4b7e5 | -8.15929 | -42.94908 | 2026-07-16 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06535741-bee0-324e-be9e-a853b7aee33c | -6.4815 | -42.22478 | 2026-07-16 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3850ef5c-f016-3b2c-8834-afce59c59b56 | -2.79475 | -49.52919 | 2026-07-16 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b1bb431-314e-392f-8938-12072b6d76f3 | -5.13183 | -37.84182 | 2026-07-16 04:19:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dcae7226-3897-362b-b771-717dad7db558 | -3.05872 | -39.92873 | 2026-07-16 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5f00d4ae-5635-3a9a-a431-84ca86b21273 | -1.81873 | -54.47998 | 2026-07-16 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbf3fc70-1592-3e71-bbce-c9a311b4624d | -13.26004 | -45.14071 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c355403d-724b-3921-91d6-71456195da80 | -12.45296 | -49.58928 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a6cf3ea-82c8-36ad-85bb-d1d02a1b2c29 | -15.3991 | -44.22742 | 2026-07-16 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bedf9a69-25a8-3ae8-892d-4e11a695b4e4 | -11.09742 | -47.80472 | 2026-07-16 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bb4ab44-fb19-3c50-bed2-8b6981c0a10b | -13.27011 | -45.16446 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89d2fbba-3102-3a6b-b184-b45ca22ac1cd | -13.53957 | -47.76301 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 824db959-882e-33a1-96d0-ceeffe0652fe | -10.405 | -44.98498 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4c9a8e-b323-3f2b-9c96-21ecd17f9911 | -11.18355 | -50.14463 | 2026-07-16 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f2b09d70-0fa0-3d49-b3ee-aa73b0c93aca | -16.14439 | -43.61891 | 2026-07-16 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15b58873-0237-36e2-bd51-786faf86fe00 | -11.09804 | -47.80091 | 2026-07-16 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afbfd1e7-8c7e-3c00-83aa-61c367e08595 | -10.03433 | -51.66514 | 2026-07-16 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ac63497-798e-3b66-88f4-8e8cba503f43 | -13.26453 | -45.15617 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3a209b2b-f496-30e0-aad7-9e2a3ee29cd1 | -9.68161 | -46.84095 | 2026-07-16 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 771a8d38-017f-362a-90c7-c2f0ed775111 | -13.52869 | -47.78753 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d649720-d536-3608-9390-1ec9b81b8a0f | -13.44066 | -43.85052 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e4a382e-0a0d-3cb8-99dd-aeef71143ffb | -10.88861 | -46.44003 | 2026-07-16 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84432b52-1c8e-38f9-9723-b37200c72a2a | -12.3255 | -45.29673 | 2026-07-16 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0d2b96e-9524-33a7-8bb5-93aaf5477a6d | -11.78865 | -47.09254 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f97f4ff8-ca5d-30c9-be0c-28da7c729b40 | -16.14556 | -43.63664 | 2026-07-16 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0343d4c9-b138-3ba9-8c90-9df03fc6f872 | -13.26732 | -45.16032 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 76a89378-68d9-3c41-b2ab-2a8d966e5b84 | -15.20293 | -44.05983 | 2026-07-16 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ac0e942-4654-3508-9221-299efbc2501b | -11.54346 | -50.30909 | 2026-07-16 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bb3e612-01bd-3c30-8d2f-dcc12d5283d0 | -11.78923 | -47.08894 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| af510114-52ce-3df6-9a32-58a6e892382a | -13.43719 | -43.84995 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96e709a4-c5e1-342b-972a-fc80020c1a6d | -13.44123 | -43.8466 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 696f1f88-65a8-31b1-9820-5c2e379f9fed | -10.40554 | -44.98147 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e30d195-7981-36fe-8e24-c9af814a60ce | -10.03938 | -51.66173 | 2026-07-16 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ad1a1d2-1547-3050-8625-475558426cd5 | -10.88805 | -46.44356 | 2026-07-16 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4808ea30-2aeb-3850-b35b-9281bcc3054c | -14.19351 | -42.8116 | 2026-07-16 04:21:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a9b449c-80cc-3677-8921-24f1c15e9d2a | -15.20819 | -44.04831 | 2026-07-16 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 633f54c0-a649-3ec9-a2ba-e07a4c80a975 | -13.26671 | -45.14178 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 050f7530-1849-3c7d-b6cb-dadf41507382 | -12.45371 | -49.58488 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf9eb00d-3a10-3e05-9063-efce7de30399 | -12.45736 | -49.58556 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3493d3c9-9ddc-31fc-b2f0-c92e71d98c95 | -15.2041 | -44.05179 | 2026-07-16 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c9b973-487d-3855-81a4-b843e504f87d | -13.55066 | -47.77993 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66367f01-5c5f-3db0-ac6d-67e66b5d6a40 | -13.26337 | -45.14124 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| cf38b230-034b-3939-9825-f4d6a0c50836 | -16.74456 | -43.8667 | 2026-07-16 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2868583a-e612-344a-ac4d-29f057dfc72b | -13.52692 | -47.79843 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d024ad95-82bd-32ad-b345-e12e420910f2 | -11.11796 | -49.77346 | 2026-07-16 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97dc2705-71ca-3ae5-bbea-b962d983be10 | -11.8894 | -40.95279 | 2026-07-16 04:21:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 709fba53-84c0-3e3d-b217-a04bb3543cbb | -15.20352 | -44.05582 | 2026-07-16 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47acfcf6-d635-36af-9222-19c39cf6a806 | -13.43428 | -43.84548 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a59c296-a57d-34d7-ac58-d478abd69f30 | -14.14333 | -46.27429 | 2026-07-16 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0c146fc-6da8-3e99-ac53-6f38bbee01bc | -11.18053 | -50.13909 | 2026-07-16 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d3fbc25f-71c3-35c0-81a0-282d74facd74 | -13.26228 | -45.14843 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README3.md)
