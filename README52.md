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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da96a38e-f87d-3cdb-8d73-e744d77ac26a | -8.395 | -44.1606 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d36afce-5277-3508-af63-f7d259ec8bda | -8.39662 | -44.12878 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f0909a9-a775-3110-91d6-7e4de228dffc | -7.12982 | -46.31488 | 2024-11-10 04:16:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 871bb165-b053-3e66-a62a-b03d4c46f2d1 | -8.36986 | -44.14538 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e35632cb-0bfd-3f1f-b4bd-b7f040a58429 | -7.47266 | -43.59726 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a47c7de2-af62-3f64-b542-872f760bb9f3 | -8.26349 | -48.49496 | 2024-11-10 04:16:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffc08795-a13c-317b-8221-df58129fa6d3 | -8.37317 | -44.1459 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e568d7c-9d55-3d4b-8399-6d763ca991d1 | -8.40767 | -44.14476 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 910957e4-5815-3383-87c8-1b93e59cdedd | -6.67588 | -43.53845 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4884b70d-234c-37a4-9a0d-6fb91d00d8ac | -8.39167 | -44.13869 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e3025bc-3ac9-3245-aa87-c83d6b5a77b9 | -8.39112 | -44.14216 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cf30785-d09d-3fd6-bdae-8149b17d1517 | -8.38122 | -44.16199 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bad0d274-aa47-32b0-a0d2-2b6f6a37d030 | -8.84664 | -47.70582 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4afc33c-c4c2-3f5c-9f07-f0d60152b1a7 | -8.40988 | -44.15224 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff73f238-98bd-3dfb-9021-525e9c7f7f3c | -8.37791 | -44.16147 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c49883dc-9faf-3e93-9a4c-29c3edff6a51 | -8.38284 | -44.13017 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a81ae28e-c072-33a8-ae13-dc6869099bed | -8.38175 | -44.13712 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9c9cfc24-a5c3-3fe2-826a-1b7c480f3731 | -8.37429 | -44.16035 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8eb0839d-15b1-3642-b006-2ef914491060 | -8.40821 | -44.14128 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e4ad3d6-1451-3f81-b27f-90e243d55d0b | -8.36492 | -44.1553 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d68ba8d4-0510-316e-ad3c-b93a903d8906 | -8.39884 | -44.13625 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 455a9dcd-835f-3e16-b9de-db6d2a95e707 | -8.36822 | -44.15582 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0aed6533-9401-33af-9292-b1cf012462d9 | -6.22817 | -47.27831 | 2024-11-10 04:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 495525c4-36ef-30c8-b007-d3625fcbb3fb | -6.41106 | -47.51613 | 2024-11-10 04:16:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47305dc9-88d6-39fb-ad28-ffff3b79594a | -8.37153 | -44.15634 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1ccf8c8-eb02-357f-a32b-7643ced0b97c | -8.38948 | -44.1526 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2e15da8-49be-372c-8e0a-03b6239327dd | -7.45722 | -43.58776 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f8bb618-9842-34b6-91ce-f2e0a7d9036f | -8.38727 | -44.14512 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ac3408a-2ed8-3d9b-8ae8-7d5310bf33be | -8.3878 | -44.12026 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebafbeb0-6a3f-35f6-b916-5d3b2fb9daa6 | -8.39445 | -44.16407 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eceaacb-8cde-3e10-9787-d9cd91e1905b | -8.39717 | -44.1253 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f093c5a-f94a-3995-ac1d-487348a4c954 | -8.36601 | -44.14834 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ad634eb-1fb7-3e3a-89e8-d9375e19edc8 | -6.31403 | -44.28044 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6d7c075-4f86-337b-9b01-8a1127704f9b | -8.40438 | -44.16564 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8eeb1df-61be-38eb-86fd-3032e87dee02 | -8.69126 | -47.96252 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eff06a63-e556-3b5b-91cf-b84868c3aa1c | -7.1053 | -42.7016 | 2024-11-10 04:16:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4779e6eb-eed9-3060-8bbc-2d02a5524c31 | -6.28643 | -47.3486 | 2024-11-10 04:16:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 461c720c-ced4-3417-9b04-a2d179e8e6db | -8.3627 | -44.14782 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccedde88-9c74-3aa9-9dd1-306f2c272d9f | -11.70717 | -48.98448 | 2024-11-10 04:16:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef0a072c-21b9-3bad-9bef-480deb39e87e | -8.84365 | -47.70063 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b206d210-6ed2-30b7-b4bc-57e014d36013 | -8.38451 | -44.14112 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a08ffe53-ea42-36e0-9b9d-1e851e19ae51 | -7.22104 | -44.99976 | 2024-11-10 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f4dff95-204d-3a34-85d9-8ae69f4de466 | -8.39498 | -44.13921 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d779451-eb11-3db1-89cc-621bbf1a361f | -11.19167 | -37.33499 | 2024-11-10 04:16:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 155629ab-c4e8-379e-ab0b-64cb5a98fcd1 | -12.94624 | -46.62135 | 2024-11-10 04:16:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43b3b74c-5046-36ef-9555-1a09169e43f7 | -7.47873 | -43.60175 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25a71a8e-194f-3163-b773-1a01ba8509ec | -6.79879 | -43.40554 | 2024-11-10 04:16:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 33e68d52-a134-34fb-be6d-591ca897094f | -7.22838 | -44.99717 | 2024-11-10 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb999fac-a78d-37a7-9d45-fba371796a44 | -8.85114 | -47.70191 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4925b5e8-59c0-3ea4-aa74-2c11362e61a8 | -7.46329 | -43.59225 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e06d8cdc-4ef3-3129-9c3a-bbb10ede3327 | -8.41428 | -44.14581 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 505326a5-ab7d-3595-9fda-6b7f5aba00c8 | -8.39389 | -44.14616 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e4105a0-efc4-3529-b0e8-89218b745070 | -8.39608 | -44.13225 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e74bc294-51c4-3be9-b298-7a4e56fbc80d | -9.58604 | -44.80476 | 2024-11-10 04:16:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bf0b108-1b3e-3181-900a-160976a902b7 | -8.38339 | -44.12669 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e2e1bff-b2f5-3518-b2eb-b6217a295488 | -8.36546 | -44.15182 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b827c97-d7b7-3794-a0ac-311d5baedf0d | -8.40545 | -44.13729 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 830c2393-d7eb-3b27-ac38-1f7936b93870 | -8.39056 | -44.12426 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 182ce13d-f706-3ad0-96cb-5437196e2cad | -8.40162 | -44.16164 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4800bf93-bc91-3a1e-a7b6-c56e0b89d141 | -6.27233 | -44.54276 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f18df699-0b36-32fd-9a11-89b72f5a37fc | -7.46249 | -43.51065 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2918711c-db14-3807-8006-eaad5478f711 | -6.26898 | -44.54222 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2796b57e-fb2c-35f2-9cbf-552b59f85db1 | -8.39441 | -44.1213 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a3ba5b5-dbe0-3611-9ac5-998e01679e4f | -8.85189 | -47.69736 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19879dd2-fcc3-3843-ac1b-2213d6042060 | -8.40548 | -44.15868 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84d7a8a5-afe6-3e86-a5ea-860e089f9660 | -8.40326 | -44.1512 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffde08ea-9547-3688-a0f9-94055724f284 | -8.38617 | -44.15208 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| babedc5a-b692-3fe7-bc1b-377c80ab1b38 | -10.69428 | -42.69387 | 2024-11-10 04:16:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31fc75d1-f62f-31b7-a710-0f66b970ffc8 | -7.14388 | -41.10772 | 2024-11-10 04:16:00 | NOAA-21 | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f796f994-1235-364d-aed8-160c666b18e9 | -8.1529 | -43.59952 | 2024-11-10 04:16:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79de4c74-570d-3e47-9ab5-62e87d24d090 | -8.37539 | -44.15338 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27239767-3caa-3692-b1fd-ab0ce3350c9e | -8.84739 | -47.70127 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b4a5724-c0e2-30ee-99a0-0fd46cb2054b | -8.37811 | -44.13599 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ad5d026-1bcc-3eae-8fbd-3f4970400143 | -8.37866 | -44.13251 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb2093ec-e413-3e01-9fef-225c56b832cf | -7.11683 | -39.7239 | 2024-11-10 04:16:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d9a456f-5721-3ed2-88b0-40c2c900810f | -8.40933 | -44.15572 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a17bdd3a-7e2b-3083-b872-051361bb4d59 | -8.36655 | -44.14486 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ce0a166-f1e3-3603-9979-faa067db0b2e | -8.85038 | -47.70647 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6bb4bbb-8e88-3392-9ce8-56fb3db33c99 | -7.48515 | -43.60698 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 614d16b8-ad08-3ad3-a967-7db5b6d7247f | -8.40381 | -44.14772 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92593f05-e01b-3231-8eef-ca6b165f8182 | -9.02449 | -37.7896 | 2024-11-10 04:16:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51e04db8-0dea-3657-9dfb-cbcb3e7bc7ee | -8.406 | -44.13381 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ebd1f2b-3fa8-38ed-8a41-35481428ec78 | -9.59805 | -36.02617 | 2024-11-10 04:16:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a8260650-b724-3ddf-ac65-58bc3e624615 | -7.11748 | -39.71945 | 2024-11-10 04:16:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9750a40d-8e57-3eb1-8822-481e1e5bd194 | -9.82977 | -36.16032 | 2024-11-10 04:16:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1363808-2ecf-3cca-b2bf-65258933cc7f | -8.2983 | -43.62585 | 2024-11-10 04:16:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab2e1d4b-093b-3d8e-80e0-93d888af7212 | -8.4005 | -44.1472 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 244a5ec0-ec1a-3ab1-bb36-8a779532ad75 | -8.40824 | -44.16268 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b54c2ba-a22c-3694-8945-4773f3aa982f | -7.47596 | -43.59778 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 317c6d93-3abf-36fd-acbb-44b4b4a12acb | -8.4104 | -44.12738 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fc12c30-59e7-39f4-a925-08c022d47f91 | -8.40214 | -44.13677 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a87ae05-50eb-3656-bd6b-77c3523392f0 | -6.32552 | -46.71988 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dafaa1f5-62c2-3a6c-a3b5-412bcd07042a | -8.39169 | -44.16008 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64c085e3-9510-31a5-ae7c-d106ca90850b | -8.39386 | -44.12478 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d58b4200-e73e-396f-909a-cb8a7cb29698 | -8.37371 | -44.14242 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1555c580-aa41-344a-a2ae-0b8266d7a3b7 | -8.3792 | -44.12902 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 572a0335-e09f-3eb2-ab6e-7d388a406f5c | -8.36325 | -44.14434 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c258de0b-7dfb-3c55-9fd6-5d6728a1723c | -8.3867 | -44.12721 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb1e418b-3a40-3193-8805-ed6f853ae4f9 | -7.40058 | -43.6037 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d0ed87d-45a3-366f-a8a8-85795ca1ee4f | -8.38946 | -44.13121 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README53.md)
