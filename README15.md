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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ecbb475-e175-3809-8e2b-f94a57a978a8 | -6.53838 | -44.58256 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b213ba2-5fdf-3887-b4bd-ae160254ca63 | -6.4234 | -43.97082 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 24a14225-371a-38ec-b6d6-cd13b6a1c69d | -7.62214 | -42.65779 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a0507a78-3d13-3b67-966b-ad507f724a54 | -9.47262 | -47.61111 | 2025-08-31 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8199b1ff-2c31-3049-bc99-de9628b6690f | -4.30575 | -48.09502 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962d89ee-62a1-3c5d-854f-475f2d257cc5 | -11.00589 | -46.94441 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c626fa2b-1c82-35c2-a2f4-1c8f01bf5469 | -6.83599 | -43.34056 | 2025-08-31 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3d804f22-6d84-3fd4-85ed-5ffa51ebf3be | -7.96695 | -46.40836 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01fb64b4-30ac-3b31-9b99-7411de9c329c | -6.95321 | -42.01321 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fb9f75b7-b711-35c4-bd45-6072993a7c3d | -6.51569 | -43.53666 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19ce908e-0d2f-311d-86ed-407f24a18f02 | -4.41862 | -47.608 | 2025-08-31 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b942f1e-1d2a-3e3d-bb37-d73b78267305 | -8.84296 | -47.48619 | 2025-08-31 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fda19cb0-72ac-3e46-88a1-9db3101d6609 | -10.9326 | -46.83892 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eab29428-d7ad-3d61-a588-70a9b52addef | -6.0932 | -43.32155 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b029cdf8-e1c5-367c-bd47-67245017e0b0 | -6.44898 | -43.96329 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 71b4af1e-034a-34dd-b8ba-ee272d0efdaf | -11.21443 | -45.04074 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66e8da37-64f9-334b-a3e3-0377b4c4a591 | -7.3753 | -43.39264 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9d95715-0779-31d2-a187-be9370dc658b | -6.50118 | -43.55637 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc32de5c-3184-38ff-a629-e6c353de136b | -7.44378 | -44.81047 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8c4604e-528c-39f1-a8cb-a78eb7b8e287 | -7.64414 | -42.65355 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3b938038-6079-3142-b0e3-7c1f0f492fda | -11.3318 | -43.63603 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6211c76-08a9-3255-a3f9-ccd35955532b | -9.80303 | -46.05851 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e6dad25-9bf2-381a-b78f-b1ff62170e7a | -7.78275 | -45.46257 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690d45fa-a6e0-3c60-a183-d060c57bff0f | -9.59209 | -40.35402 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 1b754168-d14e-3db5-8d62-2d6f7db160d2 | -6.18405 | -44.1307 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1135422-a2cc-3b41-8daf-0fefd4c487c7 | -7.86623 | -45.22266 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68430d1b-deed-355a-b5cd-123569facf5a | -7.70891 | -50.27187 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0173b659-b2b0-3598-890d-f188335cf4ff | -6.54228 | -44.58304 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42d3ab4b-0332-3d11-8db9-3a4f0e972b64 | -6.63781 | -44.25455 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eba8e1d0-dfa0-3eb1-9ff8-5d1ba773b280 | -8.19327 | -42.32047 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3d1c5d9-d11a-3ea8-b7ee-1fc7397a347f | -7.40496 | -49.5187 | 2025-08-31 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d47974db-7192-3dc7-99fa-bc269dd9caa1 | -7.70815 | -50.27141 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73c7505c-b13c-359a-9f33-124902519907 | -6.6149 | -41.82411 | 2025-08-31 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1ea1dc5-a0e0-38b5-b928-2e7c981177c7 | -5.91676 | -43.43481 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4f691fa-9f06-3df3-8eb7-6eb3c7bf6c4a | -11.3625 | -43.55737 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b92732e-764e-3059-bd7e-27d69cd31c79 | -6.96625 | -44.31245 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 900b3723-398a-3742-91fe-d53013b8d4e6 | -6.17133 | -43.99411 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef996390-8531-34ee-aa6e-b9f70ce37ad8 | -11.63443 | -37.53758 | 2025-08-31 04:02:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d338487f-37b8-3300-885c-d099878628cc | -11.35585 | -43.61998 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25a57949-6898-394d-897f-f7f90581d16c | -9.4689 | -47.60575 | 2025-08-31 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 221a21ff-eb56-343d-9cb1-8e5fd2100d78 | -11.08813 | -44.7401 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f12ade86-52ac-35a6-b2c4-bff10b779a09 | -6.95917 | -42.00306 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 522b1a57-689c-3edd-ae63-615b566e0227 | -8.78352 | -46.5938 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af961715-1ec4-3b3d-882f-60bce10079cd | -5.70355 | -49.14763 | 2025-08-31 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2db51ffa-a071-3480-88c9-8246a3a5dce1 | -11.23086 | -45.0342 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7db38bca-1eb8-3ede-b31e-b5342cd5d0e2 | -11.30577 | -43.66387 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16432859-05b8-36d5-a2c1-932589b4b276 | -8.4482 | -43.63798 | 2025-08-31 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf2f771c-f97e-320e-920b-042a473caf10 | -6.56859 | -43.67336 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56dc9350-4527-32f8-8120-ecaccad93939 | -8.296 | -44.91877 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0947cc39-585d-349c-9886-f908c4688b9c | -4.01265 | -47.72161 | 2025-08-31 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f454d3ac-22ae-3be1-913d-1a828f0faa5d | -8.95864 | -50.00784 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f04a62b1-49fd-3926-9152-4be21dbe9063 | -6.4362 | -43.97086 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c55e9a7f-e2e2-3c3d-badd-482b765d0d1c | -7.96775 | -46.40945 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6f53fc7-7873-3660-9930-fade3015d434 | -8.83766 | -47.48993 | 2025-08-31 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9620874f-29e5-3578-80b3-44d06047ed45 | -9.26348 | -43.40799 | 2025-08-31 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 946fb3c9-4701-386c-84f5-5837cde6ec8d | -5.85132 | -44.84124 | 2025-08-31 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdc352b3-b6e1-3529-9819-e8b5e2e1b958 | -7.3964 | -45.92782 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07c22a22-86e9-330a-80ec-040606176ab4 | -6.53921 | -44.58573 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0dee34ef-afb1-3eb1-b88a-382d5a44ac51 | -11.0217 | -46.87823 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9de7507-a773-3cdb-8056-c049a6678e51 | -5.69783 | -45.95603 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2d14bd2-fc48-3098-9269-236043dd617f | -7.64068 | -42.65299 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3f4d25c3-6b29-35e2-b07a-f5419c61c7e0 | -5.80818 | -43.86589 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 049ca3c4-956d-36d6-9092-cbee3bcecf2c | -4.48068 | -48.12186 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 808bf1ae-2593-3f1e-9c75-cc37d9593288 | -6.24326 | -41.82189 | 2025-08-31 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 722a93e6-1949-3561-8cbe-c7f022657bcb | -11.83533 | -37.56789 | 2025-08-31 04:02:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9ad3707-610d-3e5e-9ead-227312308f45 | -9.51066 | -45.39067 | 2025-08-31 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5019ac3b-1e82-3440-bf6c-ab39f56e4606 | -7.63252 | -42.65947 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb6858b2-06b7-316b-8135-8b519c2361a0 | -9.68095 | -48.30674 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baf2aec4-3248-3b66-aba6-0b20c82b8cf6 | -5.99298 | -43.33636 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50c070b4-5857-36f9-8c42-61761b073640 | -8.96058 | -50.00951 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d8c86c4-d28d-3b6a-8633-aa7afd1a63aa | -6.33212 | -42.53036 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e8ed04cd-4511-30db-a970-1134938ca913 | -11.4208 | -46.91223 | 2025-08-31 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c61e3f03-9913-3516-bc77-d19ecc4bc910 | -7.4187 | -42.04964 | 2025-08-31 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcb1c770-ac5e-3d15-a296-ebbb0c27cc0f | -11.29567 | -43.57398 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e49280-08a1-31d1-9111-7bb3f0c8ca4a | -7.96506 | -46.42556 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfde22ff-6065-3d3e-a6b0-ee8950860983 | -11.33116 | -43.63993 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49341710-bf8a-3fe5-a82e-47f5a76dfd51 | -6.9686 | -40.94631 | 2025-08-31 04:02:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d28c0746-2bb8-38d6-bbd9-3c15708f2699 | -7.97905 | -46.41449 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0ba6c44-9b18-3721-9f8e-0499fe21602b | -7.73301 | -50.26098 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c2d7322-3b12-39be-873c-bc1d82eeca0e | -11.07953 | -45.12703 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5dce077-69d6-396b-bdf3-64479d737a5b | -6.20565 | -42.7485 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 83585ae9-2f22-3662-8049-4e26f606da37 | -6.2729 | -43.85018 | 2025-08-31 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52556450-9915-3ff4-86c9-b8dca4d4b367 | -9.59263 | -40.35052 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 8f5e1198-61e3-344b-be75-33e47c1c4d3e | -6.20148 | -42.75187 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e34e6dd8-5e76-3e32-9d19-f6a32db08f0e | -6.1873 | -43.31493 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5941dc13-79d1-3cdc-83fa-7eb09f412aa5 | -5.53095 | -36.84838 | 2025-08-31 04:02:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 42e04676-9336-3aca-a985-011e715e1389 | -6.96915 | -40.94282 | 2025-08-31 04:02:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f01e36ba-e867-3834-b253-1439013881eb | -9.59019 | -46.00637 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33ff3169-9bf5-369d-8350-4e45606f5f21 | -9.59763 | -40.36203 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 135560e5-708a-3cc9-89ca-7fba4a0c6004 | -8.964 | -50.00875 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 521ad8f1-996c-3b8b-a5c4-ec33e985ee77 | -6.52097 | -44.83731 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecf39869-2620-3e8c-8a07-0829c1c1e9e0 | -8.7297 | -50.37767 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2ed58612-4e9d-3d65-9501-e8df44430941 | -10.01251 | -42.54172 | 2025-08-31 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd6bb4ce-4eff-3c31-a0b7-3b67e7810687 | -5.88353 | -42.96718 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1761727a-0030-3d7d-a952-ee8e528285ce | -6.18005 | -44.13219 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f8986b2-4cb9-3128-badc-8cf4ad7c0783 | -7.37195 | -43.41339 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c544cec-2741-3707-801d-2bae8e56656e | -11.36534 | -43.56182 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4869c2ae-6677-38ab-b763-b050aec152b3 | -8.00717 | -44.05497 | 2025-08-31 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0f29621-d455-38dd-96c8-18e9b65425bf | -7.10141 | -44.31806 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| fe675d63-8f5d-3d6a-a92a-ac67541ee622 | -7.41418 | -39.92772 | 2025-08-31 04:02:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
