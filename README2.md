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
| 62d79612-0ddf-3e36-a3c2-57b3276e2df4 | -10.54988 | -56.32995 | 2026-05-12 01:11:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d1296f15-cdce-3b7a-b515-1aa11d994648 | -11.94935 | -54.67822 | 2026-05-12 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 38850812-bd68-36e3-997d-e4ed83d99940 | -11.95429 | -54.7066 | 2026-05-12 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 5a8ce503-0346-3ad6-8ddb-960099448da9 | -11.73668 | -54.2416 | 2026-05-12 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 4cb7b760-516e-33b1-bfff-f171346ac1cb | -11.94987 | -54.68473 | 2026-05-12 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2e2c2e0a-4105-3db5-9965-206eb21749cc | -11.9611 | -54.665 | 2026-05-12 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3f33e2b9-710e-3d67-8e57-2f3896d007cc | -11.9609 | -54.6855 | 2026-05-12 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 365c3c0f-4add-383b-b4f7-e912917b81be | -11.9609 | -54.6855 | 2026-05-12 01:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5b00360e-3097-3eb7-997b-5127370a308f | -11.9609 | -54.6855 | 2026-05-12 01:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a046899f-29c6-3a99-ae09-a5619c2cf98e | -11.9611 | -54.665 | 2026-05-12 02:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 4fc25f78-b148-3d4d-b246-960b7240602a | -11.9611 | -54.665 | 2026-05-12 02:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 7c93f3ca-07cb-349d-a234-05d9f9244d4a | -11.9609 | -54.6855 | 2026-05-12 02:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| e383e635-7df3-3caa-b1da-0a509737f848 | -11.9609 | -54.6855 | 2026-05-12 02:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d5d37036-4410-38e7-ac08-7ff8346e1223 | -11.73768 | -44.52327 | 2026-05-12 03:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e011385-736f-3ba5-82a1-d091a79c30a4 | -16.37234 | -42.31409 | 2026-05-12 03:34:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e4d560c2-bfd3-3fa6-b9de-f527fba9be1a | -13.36828 | -43.20609 | 2026-05-12 03:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7762d1fc-97fa-373a-b68c-c9882fc54df5 | -15.88082 | -43.09751 | 2026-05-12 03:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac62c41a-feb4-3d2c-add8-f280894f7c92 | -11.73653 | -44.529 | 2026-05-12 03:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac03463c-5417-36e6-a264-23c7431213ac | -11.52423 | -43.3353 | 2026-05-12 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46ec495b-c28e-36fb-a003-d025193e4886 | -9.6513 | -42.9571 | 2026-05-12 03:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8dd59fec-31fb-39c6-92e6-809ff1bbadf7 | -9.64866 | -42.9579 | 2026-05-12 03:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1db86e83-e6f2-3765-9a36-d8a1f4f6b9ca | -11.75431 | -43.64081 | 2026-05-12 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14118071-6c8e-3311-ac36-41e962f7f1a4 | -12.85457 | -43.76225 | 2026-05-12 03:34:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b17d03b-c46d-344e-a435-796efbad319c | -9.64513 | -42.95575 | 2026-05-12 03:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b137105d-8b4f-309e-a8f3-ee4a33dfef2f | -12.85347 | -43.76126 | 2026-05-12 03:34:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66f4948d-2c05-331a-b13c-cceff6372ba2 | -16.37751 | -42.31576 | 2026-05-12 03:34:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8555a631-47c1-3548-9495-6f088c421ada | -11.52648 | -43.33184 | 2026-05-12 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b645b99d-e04a-395a-8568-87ccc54508ed | -15.87836 | -43.09641 | 2026-05-12 03:34:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1e89bee3-a849-346f-9ecd-b250f1a49e83 | -15.87762 | -43.1 | 2026-05-12 03:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b4659d27-1777-33e8-bced-f7ce804436f1 | -11.76602 | -43.63506 | 2026-05-12 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb2c335c-edf8-331a-b761-5bc0407d9710 | -15.88006 | -43.1011 | 2026-05-12 03:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 827a03ab-b355-3383-9260-4e50a5058714 | -11.73408 | -44.52829 | 2026-05-12 03:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 610c9635-e1c9-3123-93fa-95ac1631e0ab | -13.37137 | -43.20414 | 2026-05-12 03:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 785a7186-8ce9-32b9-825b-ab8c80c8e013 | -13.37049 | -43.20854 | 2026-05-12 03:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a2848f7-2ec5-3aaf-a117-900d8f5c20da | -12.86062 | -43.75776 | 2026-05-12 03:34:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b3ede70-6c2e-355c-a692-93b025504e0e | -11.76153 | -43.63713 | 2026-05-12 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4024e66-a1a6-3566-aa66-e490df4e10d7 | -12.85962 | -43.76255 | 2026-05-12 03:34:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa93723d-fd5d-39a4-9f98-b0afa1fcc485 | -15.87528 | -43.09605 | 2026-05-12 03:34:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 538f8e5b-6f15-3695-abe0-0ca83f384ada | -11.73527 | -44.52259 | 2026-05-12 03:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9f3e5e4-b775-30dd-8184-0dff09016c0d | -11.52553 | -43.33665 | 2026-05-12 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c6a1e3c-d6ec-39b5-9301-63fb032b6fb9 | -22.74008 | -42.25422 | 2026-05-12 03:36:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b88eb8c-a403-3553-8ec3-230c0a53979b | -21.28241 | -48.60666 | 2026-05-12 03:36:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cec5a94d-8e6d-3757-bf24-2ca379656820 | -6.98045 | -42.86579 | 2026-05-12 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 089b036e-738a-3d24-8e26-7438ccf73315 | -12.85591 | -43.76011 | 2026-05-12 03:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7857b96-d01a-3b3a-9281-e2c1b5043156 | -9.65026 | -42.95724 | 2026-05-12 03:51:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aaa75dd3-492e-31b4-8d3c-93cd299a6f9a | -13.36989 | -43.20483 | 2026-05-12 03:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1bb2cbb1-f7c2-33f1-9d67-4637bd14840b | -9.45295 | -47.82255 | 2026-05-12 03:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b126e547-7498-32dc-8a4b-c1f652c17d48 | -12.97368 | -44.02334 | 2026-05-12 03:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76728827-fc90-3232-939d-975135941046 | -14.10789 | -45.2843 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aaa4d76-25cb-3c84-8240-941233a1c660 | -9.45372 | -47.8223 | 2026-05-12 03:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23453925-c15a-3887-bf2c-51f84e61f1a8 | -14.15801 | -45.42194 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3daee5a-0795-31b1-9a7d-fabd48d5e3fe | -11.75179 | -43.63691 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef045c9f-82c0-3b19-9b1b-7611f80bde37 | -9.64196 | -42.95572 | 2026-05-12 03:51:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0f02f7e-e232-3a90-b274-4ac8710bc22d | -11.00322 | -46.48536 | 2026-05-12 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a2b8604-e7fc-3a16-ad6d-c051f276f6c4 | -14.10255 | -45.28801 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3ce5ddc-d44b-307d-90eb-3b21348d5d27 | -15.30616 | -41.84344 | 2026-05-12 03:51:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d504a7e7-6884-37fa-a4a2-a243630d373c | -9.07035 | -48.65308 | 2026-05-12 03:51:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e86ff110-af53-3a3a-9db3-e5646f15a407 | -13.36592 | -43.20409 | 2026-05-12 03:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e9161e4-450e-397b-817c-d2b0949a29c8 | -11.73422 | -44.52721 | 2026-05-12 03:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c59b58-e368-3f38-ace2-add7ef10a337 | -13.18955 | -42.99598 | 2026-05-12 03:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e6dfaf4a-1655-38f9-a8e1-438f6a14d367 | -9.44764 | -47.79221 | 2026-05-12 03:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3355e1ce-14b4-3a20-9762-1d720a697a37 | -11.5232 | -43.33104 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a7f3f71-982c-35be-a5a1-deff57195362 | -9.45243 | -47.79331 | 2026-05-12 03:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb59cd71-33d6-3996-88dc-cb9a0fc10de5 | -11.27717 | -44.65133 | 2026-05-12 03:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b4eda2f-10e7-3574-b728-edd0febbc796 | -11.76017 | -43.63844 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c8c88b1-8f50-3c21-ae59-ac32255f8476 | -11.00254 | -46.48894 | 2026-05-12 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98abf5d0-76a0-34b4-a054-fee96f8dcd59 | -11.00192 | -46.49216 | 2026-05-12 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 818e119c-9806-314e-bbe7-287e520c73e6 | -9.64677 | -42.95265 | 2026-05-12 03:51:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b1a24cb-641d-3e82-b3b4-e8238e4cc368 | -11.76855 | -43.63995 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86bf0280-c2b9-3f5b-9a4a-0d3f3edf3490 | -11.97937 | -46.78674 | 2026-05-12 03:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f42cfa29-d2d7-3676-875f-c8eb6a4c9ae9 | -12.85176 | -43.75933 | 2026-05-12 03:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0fc7115-996a-356f-be32-9358c1737a60 | -9.44666 | -47.79239 | 2026-05-12 03:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf2bf088-7def-391b-9888-2b059fbec73e | -14.13712 | -45.33553 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68142985-18c5-3552-b5de-b3b0b322124c | -11.97592 | -44.36819 | 2026-05-12 03:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30a52aef-e056-3e34-8528-45e9227f300f | -12.05298 | -45.28701 | 2026-05-12 03:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 929ca8d1-3a75-3495-8cad-e58727cf3348 | -14.13518 | -45.33767 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4740c65c-794c-389c-ba97-ea61ea3923e6 | -12.86005 | -43.76088 | 2026-05-12 03:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a5079f3-9683-3cab-9515-de054a6789fe | -13.68563 | -44.29254 | 2026-05-12 03:51:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55dfff7e-3be7-38ee-ba70-529fc4a3c0b4 | -10.12901 | -47.92466 | 2026-05-12 03:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae88ba1d-c4db-3977-a177-373cb552cfe9 | -11.00051 | -46.48864 | 2026-05-12 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc350831-4f16-3733-88ae-20949501e36d | -12.8566 | -43.75628 | 2026-05-12 03:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5ae726f-3797-3513-9e84-99199e421371 | -10.12825 | -47.92862 | 2026-05-12 03:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c1bb39d-518e-3ab2-aaae-5c748640b280 | -10.99992 | -46.49186 | 2026-05-12 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a549bc2-7d8b-3e97-aabd-eda8dffb5b01 | -11.76088 | -43.63454 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30229145-3c32-37ca-9ebb-9f22f9f98343 | -14.23049 | -43.65397 | 2026-05-12 03:51:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ad5a5fb-8553-3a4d-82ce-892771c618fb | -11.00638 | -46.48559 | 2026-05-12 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b97aca-dfa5-3a6b-ae40-4fc62526c5f4 | -14.1535 | -45.42102 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a4eddea-53ba-34c7-b65b-d6c4222d0786 | -11.52732 | -43.33181 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c32bf4fe-4887-3a54-8925-56d862dff725 | -9.07654 | -48.65373 | 2026-05-12 03:51:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62d911b6-048e-3da8-a3ed-2baee58f2b21 | -11.73585 | -44.51826 | 2026-05-12 03:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1c60e66-5d25-386b-9e72-54ca2cd060fc | -14.14052 | -45.33393 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 129b6793-4d75-3f3f-8356-43c9d7fa8529 | -11.75598 | -43.63769 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eb75935-a621-3226-bb92-b9676e6887c1 | -9.64611 | -42.95647 | 2026-05-12 03:51:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6bcbca56-744a-3d8b-9716-6bf6f103a3a3 | -9.45341 | -47.79311 | 2026-05-12 03:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 136ec8b6-6f1a-3f4b-a7cc-3950e87e31e2 | -11.73503 | -44.52273 | 2026-05-12 03:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff19600b-0db5-36a1-9ad3-a072e14e4464 | -11.52253 | -43.33483 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15cce8d4-9f49-3451-a8f1-0da2f2d5cb28 | -11.76576 | -43.63143 | 2026-05-12 03:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b341f1d-e9f5-34a4-b630-8b99065674d8 | -14.15438 | -45.41637 | 2026-05-12 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6acd17d7-0c56-3606-a1fe-e16534636575 | -14.14484 | -52.88758 | 2026-05-12 03:53:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40da81cd-2759-38a1-a2eb-b81dbb5cb675 | -18.48233 | -51.70908 | 2026-05-12 03:53:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
