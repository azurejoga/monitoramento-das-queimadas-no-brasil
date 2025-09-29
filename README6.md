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
| 0f579d72-08c0-3bf6-a427-2215aa30b2cb | -8.2854 | -45.4772 | 2025-09-29 03:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| aa706d4c-edad-3e55-b383-f559eb2b05d3 | -3.1012 | -47.0301 | 2025-09-29 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 45746c7c-aef8-3fa6-b5e6-53873f7fc397 | -12.2825 | -44.0804 | 2025-09-29 03:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 07a46e16-06cc-3fb2-ba04-7490872d4357 | -20.0491 | -41.3251 | 2025-09-29 03:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| 57a87a55-c6a7-3153-8554-e8585f231c15 | -17.0938 | -48.5699 | 2025-09-29 03:00:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3605e9e1-0cf7-30fd-87a5-84b0a43448d4 | -12.2627 | -44.107 | 2025-09-29 03:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 02122fb5-b3bf-397b-b40a-3a3e13d25b0e | -8.3042 | -45.4752 | 2025-09-29 03:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 74973805-2b54-3406-b414-a574e773b923 | -12.3013 | -44.1008 | 2025-09-29 03:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 61e07151-5ba2-38a2-9c97-4e7b4000bab3 | -12.2816 | -44.1275 | 2025-09-29 03:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 49225552-8545-3889-ba13-7c0f842a1301 | -7.2214 | -44.783 | 2025-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| fd1b72d9-3df9-3800-8b64-ad1f94b392c0 | -15.2893 | -49.5035 | 2025-09-29 03:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 03258557-51ac-3b7a-a173-34394a76a035 | -15.0579 | -42.3424 | 2025-09-29 03:00:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 49.8 |
| fe6a159d-6d6a-36d3-a496-3e51ac2b578d | -12.282 | -44.1039 | 2025-09-29 03:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 483.4 |
| b2eb72e7-3395-3d29-8e55-c809be23779e | -17.0938 | -48.5699 | 2025-09-29 03:10:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 91c5f953-9684-3ca0-bded-62a05f9759dc | -8.2854 | -45.4772 | 2025-09-29 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c25a68ea-213b-34ee-9207-398eb685b5b3 | -13.3796 | -48.1577 | 2025-09-29 03:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| fe4b8703-48fd-3a7f-9ccf-20cd756a8518 | -15.2893 | -49.5035 | 2025-09-29 03:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2bee8d55-bb6f-35a1-a0a7-64bfb6860af2 | -12.2825 | -44.0804 | 2025-09-29 03:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| c0b61c7c-0236-3a12-9ca4-3fc6895ee5b6 | -7.2214 | -44.783 | 2025-09-29 03:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 1f335302-e85d-3a1a-9c04-012c5cb77070 | -0.1012 | -51.2738 | 2025-09-29 03:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 9b4d214e-9458-3f87-86ff-d0eda7f8b804 | -12.2627 | -44.107 | 2025-09-29 03:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c80dabf4-56e7-3b29-bb21-776883f38f8a | -8.2851 | -45.4999 | 2025-09-29 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 6a2d7f0b-947a-39fb-a390-06dbabf6c0d7 | -11.925 | -48.0273 | 2025-09-29 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e8b14344-8c06-3321-a203-9013be0d612f | -12.282 | -44.1039 | 2025-09-29 03:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 09f833c2-31d3-350a-be48-7e2564a8e64a | -11.3638 | -45.057 | 2025-09-29 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b5d41095-89bd-3718-a0d7-d1d1fc10493a | -12.3013 | -44.1008 | 2025-09-29 03:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e17df91e-c109-3ca5-b625-82814a6ebfa0 | -8.2662 | -45.5018 | 2025-09-29 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a1e3247b-ce40-35bf-bf79-ba9400008e04 | -20.0491 | -41.3251 | 2025-09-29 03:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| a36452d9-92db-3183-900c-b752554b2337 | -12.2816 | -44.1275 | 2025-09-29 03:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| dae7c66f-2b7d-321f-917c-0986c9f9f5c6 | -3.1013 | -47.0082 | 2025-09-29 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| ed17267d-3e66-32e5-bd8f-640aaebfe3f6 | -11.3634 | -45.0801 | 2025-09-29 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 56f87875-aebb-36b4-acce-32268de80c59 | -20.0698 | -41.3189 | 2025-09-29 03:10:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 54.3 |
| b7b16899-b475-3955-a316-507df0b9c149 | -2.5773 | -48.3931 | 2025-09-29 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b65c5967-79d2-3505-8f85-11f03eb0d73e | -15.0579 | -42.3424 | 2025-09-29 03:10:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 0152cbd5-3c3b-350e-9383-b77925e94a8f | -2.5772 | -48.4146 | 2025-09-29 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0109b146-5c63-3b80-afc0-12a25923c5fe | -7.2402 | -44.7812 | 2025-09-29 03:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| a8720b73-dcf7-3c4c-82bd-0b109acb5735 | -6.12658 | -41.81547 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 16b7ba66-0b35-31fa-93a3-77423665f503 | -6.05452 | -42.46219 | 2025-09-29 03:15:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 208b175c-2326-39d4-857a-d7856c210d0d | -6.12378 | -41.81707 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9dccf921-1538-33ce-b507-c9a0ff12aa4c | -4.50668 | -40.72474 | 2025-09-29 03:15:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9320acff-1514-34ee-8e89-7732933143e8 | -5.17388 | -41.25444 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d05cb0f7-85f3-30e0-8ae8-ed7a5cd419b3 | -2.87564 | -40.02298 | 2025-09-29 03:15:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 37f406d3-da45-322d-a1b8-5378593dffcc | -4.70503 | -41.98375 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 9b62bf54-bf6c-386f-827a-06aa0519f344 | -6.06615 | -42.47741 | 2025-09-29 03:15:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c525ceb5-c9e8-340f-b167-13110bd779fb | -6.05788 | -42.48292 | 2025-09-29 03:15:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 79e8dd53-f523-3a5e-ba33-a37ba80c3df3 | -5.17738 | -41.24723 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3b84cf0-6940-3e9f-91f7-e882eeb77afd | -6.11594 | -41.82188 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1be8a765-eddb-36c2-a7b3-3292d06359c4 | -4.71147 | -41.99175 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| a09cd3c1-92ab-3061-b63d-c0f217125163 | -5.42389 | -42.26252 | 2025-09-29 03:15:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9642cb67-4815-3ba3-a924-5e7192bc1012 | -4.71196 | -41.98503 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d1255681-7008-3a1b-a785-cc05b8eb8582 | -4.71074 | -41.99165 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 5e25cedf-47f7-376d-8b20-68acc8da9f3d | -4.14307 | -40.0158 | 2025-09-29 03:15:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9307ac0e-d5eb-3a9f-93a1-1f1f962f3dc3 | -5.17634 | -41.25313 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5fc978bd-6c24-39bc-b232-ae17ad788cf0 | -6.05913 | -42.47622 | 2025-09-29 03:15:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 991cf43e-36d0-34c3-87bb-f0e8f4bf76fa | -6.11481 | -41.82804 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9bc94760-7043-3d8d-874f-78160811372a | -4.71383 | -41.97842 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6dac5589-874e-3e45-9d80-3d6c90e865d1 | -4.14395 | -40.01078 | 2025-09-29 03:15:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 11f1f8db-f9cb-3517-ab1c-e4ac7f3b0101 | -6.11977 | -41.8147 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 952cc659-045c-3fe6-be7c-9a91f7c15f96 | -6.06487 | -42.48423 | 2025-09-29 03:15:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 99e45e45-f635-3464-8a34-00bf51a3843b | -5.78388 | -42.6499 | 2025-09-29 03:15:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ff4f2758-8055-32a1-8b56-fba8f9e01541 | -4.71265 | -41.98511 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 4a3ea14b-8a11-3f56-9f28-34cb22055fcd | -4.70379 | -41.99044 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| b792ae69-8fb8-366b-92bc-dafb7b4687c6 | -5.15598 | -35.63715 | 2025-09-29 03:15:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b7b44df-9651-3692-9ae3-13915ebd5c5a | -6.12488 | -41.81099 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 40a2c1e6-7446-3fef-8aea-aba340cb37a2 | -4.70625 | -41.97713 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 80e51b55-02aa-30da-b83a-2abaa74d626a | -4.70572 | -41.98379 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9b03f45b-8124-35f3-bfd1-d300268bca25 | -6.06036 | -42.46964 | 2025-09-29 03:15:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9654aaf8-2f1c-34f1-bcf8-e435e4223964 | -5.17286 | -41.26001 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e5cd9a9b-51a0-3de3-94c5-49293bcdafef | -4.70452 | -41.99051 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 68f3fb18-f11f-3941-bca3-af8c6f5438e5 | -2.87477 | -40.02814 | 2025-09-29 03:15:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a4876b33-9c7f-32d9-9372-675bddac4ef0 | -5.15154 | -37.71942 | 2025-09-29 03:15:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b773a4b1-a6ef-3a93-956c-e8e171c59d69 | -5.14738 | -37.71809 | 2025-09-29 03:15:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4162f31-8d59-3606-a88a-40822bcdb510 | -4.75727 | -38.47827 | 2025-09-29 03:15:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7ae8c499-308f-3d67-ac48-05f1b5708247 | -4.7069 | -41.97716 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8dcb7e21-34a6-3df1-95ac-ec4312b41b0c | -6.11865 | -41.8206 | 2025-09-29 03:15:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5cfcefe4-b276-3775-8296-62d4f1c3203d | -5.78736 | -42.65033 | 2025-09-29 03:15:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ffa79f42-9270-3181-ace5-19565331f871 | -5.1743 | -41.26464 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6ec79f59-0f5d-3d64-a521-9b46a6938e2c | -5.51192 | -42.20576 | 2025-09-29 03:15:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c919e5d2-0188-3f4e-90f2-c504c627b4b4 | -5.14624 | -37.71856 | 2025-09-29 03:15:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28dba4a7-4f55-3dbe-9382-5605f7d639cb | -4.71318 | -41.97838 | 2025-09-29 03:15:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ac9b65c1-c1f3-350c-81d9-cee6df309e49 | -5.16864 | -41.25809 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c9567374-e33c-3007-8266-e5fecdbde7a2 | -5.17533 | -41.25885 | 2025-09-29 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07e4e389-2c6f-3387-b0a8-c1db35270032 | -7.24661 | -43.00969 | 2025-09-29 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 728e257b-9c28-31bb-9051-ccb008cff3ee | -12.58238 | -41.29075 | 2025-09-29 03:17:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1bc90271-f731-3713-833f-4f8e2ce1b108 | -12.17482 | -43.56779 | 2025-09-29 03:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 809d5922-025b-357e-9ddf-35c5d800f417 | -7.28819 | -42.83104 | 2025-09-29 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e61bc237-bc14-3722-aea3-5841b26f2151 | -11.94257 | -43.91938 | 2025-09-29 03:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1fff87cc-f897-35fb-9c4d-cb52ec29bd6d | -7.2452 | -43.01705 | 2025-09-29 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44555fc2-cfb0-3b9b-9b26-b34a4fa8a844 | -7.17392 | -39.37683 | 2025-09-29 03:17:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6a576a46-ddf7-32af-96b5-ff4b1f1db177 | -12.58256 | -41.29692 | 2025-09-29 03:17:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 762c22fc-7cf8-3ffc-9f06-7b40e0e09c76 | -12.17613 | -43.56153 | 2025-09-29 03:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 170a57f2-7ebb-3a69-b22a-4cbdc95f7d15 | -7.28687 | -42.83796 | 2025-09-29 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b54243c3-ac35-3e48-8f89-bdbd8d54b8e2 | -12.58149 | -41.29506 | 2025-09-29 03:17:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b8816e0-d5bb-340a-868a-27df09dc6b19 | -12.5806 | -41.29939 | 2025-09-29 03:17:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5ab618ea-7cbe-36e8-917b-cd39578a4eb6 | -11.51345 | -43.54169 | 2025-09-29 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53ea32e6-9573-3625-ad95-e2909b35e775 | -12.58342 | -41.29258 | 2025-09-29 03:17:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28c0c41b-12c7-333a-95fa-37d711c34329 | -11.50537 | -43.54634 | 2025-09-29 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24e895b3-2918-3a59-b86a-8ed2c46565c9 | -7.70175 | -41.28672 | 2025-09-29 03:17:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd81cf54-43ff-3069-9516-afbb86539e4c | -7.864 | -41.06255 | 2025-09-29 03:17:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 52a59d46-c875-372b-a373-5802dfbf7477 | -7.86495 | -41.05743 | 2025-09-29 03:17:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |


[Clique aqui para ver as próximas entradas](README7.md)
