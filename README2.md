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
| 4661adb3-594b-361d-98b6-5de5ef6e5c5d | -9.61941 | -40.34268 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e2201d7-5609-3355-b115-5ffa1dded42c | -9.5896 | -40.33793 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 456c217f-8e1f-32cc-b28c-2e999841b968 | -9.49834 | -48.13172 | 2025-05-19 04:00:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eb2804a-c341-3cb2-8534-ae78330c5ea0 | -7.23296 | -43.54216 | 2025-05-19 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 893e2597-e6d5-3b2a-b096-6c4fe785b4a6 | -10.69464 | -37.04694 | 2025-05-19 04:00:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46d7611d-6900-3e00-b8a1-cca5c23e8114 | -9.42684 | -40.37968 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8547b1a3-011f-3d2d-88ae-c38b1b037143 | -12.29952 | -52.47328 | 2025-05-19 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c08b3c4-f13b-3d67-9fc7-88e82120207f | -17.377 | -42.48235 | 2025-05-19 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e7bea68-d0cf-3e75-89f1-a5c5fdf4bdaa | -12.10321 | -44.75197 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d15a1657-1330-315c-affb-5701f5bb2b81 | -16.7538 | -48.60645 | 2025-05-19 04:02:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47718453-025b-388a-9f03-0558e42c2218 | -12.09954 | -44.75135 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aaf6fe94-67ef-3bd4-96f2-d968897448fd | -13.30637 | -47.60612 | 2025-05-19 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f6c7e72-bdb7-32e6-8953-4843dc42abb2 | -12.10567 | -44.75539 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f1a698c-b53d-3745-bdf2-ce520b22aae5 | -17.66586 | -46.68331 | 2025-05-19 04:02:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0502cbc6-e739-3ca9-8c4b-06272a2d6628 | -11.55799 | -47.87154 | 2025-05-19 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2b4f51b-0809-3128-9b43-8db4bce34925 | -12.13688 | -54.66652 | 2025-05-19 04:02:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eb549e6-3739-3e28-ae09-97d2d7a371a8 | -18.80535 | -40.50532 | 2025-05-19 04:02:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f630e3b9-4165-3a20-9e6c-d47dbb26ad3c | -17.0532 | -45.02819 | 2025-05-19 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cbb25119-1cae-3aa1-848c-f91a259f68c0 | -17.91862 | -45.52863 | 2025-05-19 04:02:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f56ba181-e3cb-3747-8dbd-62e32535a4e5 | -13.03972 | -53.72322 | 2025-05-19 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80233e35-6093-3bc2-b714-d44c9c5a0547 | -12.03674 | -54.97176 | 2025-05-19 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7bc1b70-fc2c-3981-8e85-9317404b8fb7 | -12.10858 | -44.76043 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cee4033b-93ac-31f8-8913-c819939550d5 | -17.0574 | -45.02472 | 2025-05-19 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c433ca15-70e7-363c-9d5f-6a3cb18f2dcd | -14.28507 | -41.72118 | 2025-05-19 04:02:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 507806ec-60ff-3b8a-89b2-b4a4fd187a57 | -13.04712 | -53.71955 | 2025-05-19 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06457923-9f9a-3b9f-b926-415ebf1c4ebb | -13.03856 | -53.72004 | 2025-05-19 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c3cf85-e4c0-37af-bb0f-9e37e07a1623 | -12.29355 | -52.47203 | 2025-05-19 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc6dad50-906c-3070-aaf6-8e10c00093a4 | -12.12878 | -54.67128 | 2025-05-19 04:02:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 610e84fd-8e9e-37e4-94c5-426994a811f4 | -13.30203 | -47.60566 | 2025-05-19 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8538b7f4-e71e-31c3-ace9-51d6eb85a7a7 | -17.06091 | -45.02536 | 2025-05-19 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8dd74dd-96c0-3b87-8299-440d1cfe5c1f | -13.03749 | -53.72533 | 2025-05-19 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4663151-75e9-3f6d-b846-d7b50e30a281 | -13.57572 | -47.3659 | 2025-05-19 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c20ea88-3cc4-3cee-a0d9-e0e61fa8c9aa | -12.10541 | -44.76142 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aaf2a7eb-994f-3801-86e3-8a1111cab9bf | -11.57615 | -47.61395 | 2025-05-19 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c3c82ed-c358-380d-ae03-2fad0d9cb7f9 | -13.04082 | -53.71799 | 2025-05-19 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88330a62-02b2-3c2e-ba23-ecc3e28b090f | -17.05809 | -45.02063 | 2025-05-19 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54a94524-8e81-3e8d-823c-f44dc1459123 | -12.10247 | -44.75638 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38d15095-6dd1-38bf-b800-90d029d0e3b9 | -12.13009 | -54.665 | 2025-05-19 04:02:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f833635d-2190-3dad-ab54-b46901855a8c | -12.10199 | -44.75477 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1fb3a6e-6873-39ba-84fb-3c88471a8603 | -12.10934 | -44.75603 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af07125c-abe7-3342-a0df-03491def6eee | -11.57695 | -47.60947 | 2025-05-19 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1baed3f-98ac-35bd-86c0-1c5259a0691b | -17.67578 | -42.74048 | 2025-05-19 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 918180ab-8382-3a00-9342-38b60f7f1ed1 | -19.51333 | -44.27771 | 2025-05-19 04:02:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44f31b47-4a07-3921-8f5e-dd0d47bde1dc | -19.45267 | -45.30659 | 2025-05-19 04:02:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b54d07c-fa7f-353d-835f-0238a036224b | -11.56011 | -47.87017 | 2025-05-19 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11c7e956-a83a-3b91-90e8-4de25a32e00e | -17.91935 | -45.52445 | 2025-05-19 04:02:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b759258a-20fe-361e-93e1-f546c8c1a1ac | -16.67865 | -43.88503 | 2025-05-19 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44207f3f-dd7b-3aa4-b04c-234f957159be | -17.05389 | -45.02409 | 2025-05-19 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8523f075-0040-3edf-959c-9cedd16e9a01 | -12.10414 | -44.76421 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00f87263-5df8-3b4a-983c-b1a41a24aca4 | -15.25199 | -49.52782 | 2025-05-19 04:02:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c866ee7-3939-39f9-b7df-53c40a58fbda | -12.0298 | -54.97033 | 2025-05-19 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c182be70-9976-3ac9-80b5-d8dff66cfb61 | -16.75261 | -48.60357 | 2025-05-19 04:02:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16b126d5-4153-3cf7-94ad-edc82b295a0d | -12.1049 | -44.7598 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2243970-df29-3777-a984-3a2f2e3e57dc | -12.10614 | -44.75701 | 2025-05-19 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04fd16ef-db59-3a95-9dfc-16783ef5fc18 | -23.98421 | -48.91988 | 2025-05-19 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c62968f-276d-395d-a374-22d9ca3c1038 | -21.25478 | -48.63886 | 2025-05-19 04:04:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 93d3e6f7-4277-3788-87c9-c243aca8abc1 | -21.04134 | -50.66832 | 2025-05-19 04:04:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 9b65f318-399c-3a72-ae70-267b628ffbf2 | -21.58108 | -48.36597 | 2025-05-19 04:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b882c363-be08-3e6f-bbd2-44bd03d1fc80 | -19.97518 | -44.85645 | 2025-05-19 04:04:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84062510-bdc3-3d9e-91ce-eb007ffb8bdf | -19.96898 | -44.21671 | 2025-05-19 04:04:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86877dc9-77d8-37c1-a67a-d371516268ef | -21.58171 | -48.36448 | 2025-05-19 04:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39330460-59ea-39bc-9bc4-fb1f53c83415 | -22.90132 | -43.75205 | 2025-05-19 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 719a6771-f4a8-3aaf-ba5e-10ad1911cad1 | -23.51649 | -46.73661 | 2025-05-19 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6ebbd8f0-206d-3d6a-b2d4-049f1a36cd2d | -21.25409 | -48.64252 | 2025-05-19 04:04:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 15c64db1-a85c-3e75-ab9a-3f6102e69cd1 | -21.04252 | -50.66492 | 2025-05-19 04:04:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| a6c24c44-533c-34f5-911a-6f8b8d65017b | -23.40612 | -46.5575 | 2025-05-19 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5fee3528-e11c-3307-87db-f08639036199 | -21.91248 | -42.26126 | 2025-05-19 04:04:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1bcebb13-287e-3f7b-9df3-957bb4101f0c | -21.04152 | -50.66979 | 2025-05-19 04:04:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 9c434237-f3e2-3945-bebf-1752ec4004a8 | -21.038 | -50.66388 | 2025-05-19 04:04:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 654e3074-fefd-3db9-9a6a-166c90b1e0f7 | -21.87475 | -53.29476 | 2025-05-19 04:04:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19b64fec-45fc-35a3-be56-4cbf3c2532fd | -23.63422 | -47.26687 | 2025-05-19 04:04:00 | NOAA-20 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93c66bbc-b5ea-3f4c-a3bd-7d5432db0936 | -20.76397 | -46.76897 | 2025-05-19 04:04:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1cfde4ec-2b39-387d-ad40-e37fc923f44f | -21.12992 | -47.78861 | 2025-05-19 04:04:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ddb24ad-b231-34f3-902c-14128fd5a84b | -22.53996 | -48.81417 | 2025-05-19 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4257fbcc-0714-3be3-9f59-ff5497aaf092 | -20.98169 | -50.65914 | 2025-05-19 04:04:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 21275fe9-de11-312e-820a-673f234a4810 | -19.06241 | -53.46049 | 2025-05-19 04:04:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a9506c7-abf8-3d4e-83d5-643297487b5e | -20.3124 | -45.58393 | 2025-05-19 04:04:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c644e3ee-8fb4-3080-92e3-581dfc4977f0 | -20.58017 | -44.5747 | 2025-05-19 04:04:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f90808f-ba6c-3d9a-824f-16df60cb01ab | -20.98071 | -50.66401 | 2025-05-19 04:04:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 6856ae84-4c6a-30ff-8411-8677af209f6d | -22.67718 | -42.85276 | 2025-05-19 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f5c8bf75-2e5e-3af6-895f-1d2437c726cc | -21.62573 | -43.46541 | 2025-05-19 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20e81085-a0e0-3a89-8a3e-2bb3b771e8dc | -21.26089 | -46.59086 | 2025-05-19 04:04:00 | NOAA-20 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 326d27f0-13eb-3216-b818-46de80197b00 | -23.33952 | -46.77196 | 2025-05-19 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d5e64747-94a1-346d-8f94-b50140fcd4a0 | -20.17528 | -46.9717 | 2025-05-19 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcb9e8b8-35d7-3dff-9f30-5b33d40f870d | -21.04038 | -50.67323 | 2025-05-19 04:04:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d25840d5-9d44-366b-ba55-6656014461ff | -21.2629 | -46.58853 | 2025-05-19 04:04:00 | NOAA-20 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ad52ce2-b28a-36a0-adb3-6fc0bf934245 | -23.98518 | -48.91466 | 2025-05-19 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfee3069-484b-337b-9cec-98c304b34403 | -20.57681 | -44.57407 | 2025-05-19 04:04:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b48fc5d-a759-329a-9e26-21d1aefc4629 | -21.25548 | -48.63519 | 2025-05-19 04:04:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 01cb9638-e06d-311a-8485-05191e2f7e93 | -6.2318 | -43.36216 | 2025-05-19 04:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 764da39f-2346-338f-969d-ae2aa974b8f3 | -5.41913 | -47.56904 | 2025-05-19 04:49:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e39d887e-2484-3c52-aa6d-586b9f60c196 | -5.02932 | -47.96881 | 2025-05-19 04:49:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cdce361-950c-3328-b74e-20facd9a8602 | -10.96198 | -49.42147 | 2025-05-19 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b8f3e08-6fd1-37af-865b-cb84d0075706 | -6.15568 | -48.51579 | 2025-05-19 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 679d145a-bb8e-3edb-a481-98038e200bb8 | -12.10531 | -44.75558 | 2025-05-19 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61ca07b7-1812-35cb-84c7-e1ddf976aaba | -12.29731 | -52.47443 | 2025-05-19 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e51a6ce6-7bba-3d90-96bf-aecaa874c907 | -10.76309 | -57.22829 | 2025-05-19 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 975f59e7-a051-3a06-b9dd-ca245976fda2 | -12.23056 | -54.29991 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3194452-1b93-3c0f-8880-f478c8083683 | -9.32748 | -44.83806 | 2025-05-19 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 300085e5-8ad8-3960-9395-3285f9a3cfc5 | -12.13841 | -54.66827 | 2025-05-19 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
