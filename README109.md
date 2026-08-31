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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef8bea0e-6c01-3d96-9200-15ef7adde493 | -19.75519 | -43.28596 | 2026-08-31 16:28:00 | NPP-375 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5d8ae565-d820-3144-b947-d2aa5798c9cf | -20.30283 | -47.83118 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5d31edd9-7420-3548-95c0-59a89a7d2e90 | -16.2089 | -39.6105 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 40a87b63-4f29-3a6e-8856-e93dcb88530a | -17.15289 | -39.46706 | 2026-08-31 16:28:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 78daf9a4-7eed-3ade-9443-4a26aeab6bd3 | -17.31446 | -42.6967 | 2026-08-31 16:28:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5e6f191-eed0-3157-a08d-bca6f6c1c249 | -17.53226 | -39.94376 | 2026-08-31 16:28:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 75cd2ba8-dba5-3663-aef9-7fa550883b05 | -18.29906 | -45.08932 | 2026-08-31 16:28:00 | NPP-375 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fe64ffb5-e682-3106-9f39-88d8d8c28b85 | -17.85108 | -50.50872 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 864c6cd6-7156-352a-bc9c-0907bfca8b93 | -16.56557 | -52.514 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b05fe8c5-983e-3927-9ff0-d89c98f39efa | -18.91217 | -50.87685 | 2026-08-31 16:28:00 | NPP-375 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 25f5ffc6-f1e2-37b1-ad6d-d3af3603d10d | -15.20155 | -46.22506 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2b161108-c0c4-3648-821b-c87934ec4a9a | -14.98899 | -48.14174 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4e7fcb8d-1c0b-3bc7-a5d7-42666a6cfb9e | -16.71723 | -39.16483 | 2026-08-31 16:28:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 78e652ea-645e-3496-b660-a813242b48d7 | -14.15674 | -42.09736 | 2026-08-31 16:28:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9481a95d-295c-3115-9224-a619e3e787fb | -17.72715 | -44.28121 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ca73b2d2-a7db-359f-82b6-0aa5078f1569 | -15.39691 | -45.62832 | 2026-08-31 16:28:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91dfcfa8-1a44-3720-bcb5-e5cfa7109e6b | -17.86643 | -52.10191 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 0bcedca5-2c14-3722-86c1-0c92c6f053e7 | -15.8303 | -42.6149 | 2026-08-31 16:28:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ba1759d6-b8c2-34b8-924f-8a59c8bdf2e4 | -16.89191 | -40.21967 | 2026-08-31 16:28:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 09495780-3420-3ab2-9f6e-bfb9068ee62c | -18.16723 | -39.79416 | 2026-08-31 16:28:00 | NPP-375 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c423884e-87aa-3228-bca5-b303a75025eb | -14.20806 | -41.96992 | 2026-08-31 16:28:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 75ddcfe6-45bb-3596-b9f6-d90dc3c33065 | -17.85494 | -52.09485 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| cc96318d-c327-370d-86ea-058542b1d893 | -18.26937 | -40.54819 | 2026-08-31 16:28:00 | NPP-375 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| c4b9e4f9-55ee-3197-b79c-f1567d4a9502 | -18.55469 | -39.78379 | 2026-08-31 16:28:00 | NPP-375 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d719b13f-9c0d-379d-9cf5-b3e1128063a2 | -17.50664 | -44.2279 | 2026-08-31 16:28:00 | NPP-375 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1b6a0eb6-3d94-3ef3-aed6-c176c4848054 | -19.1496 | -45.49653 | 2026-08-31 16:28:00 | NPP-375 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 07f25bcc-f9d4-340e-8951-77fc09d3f82b | -15.64949 | -50.09828 | 2026-08-31 16:28:00 | NPP-375 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0ecec53-2154-31cd-9c14-f7f0d47506a0 | -18.27008 | -52.71157 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c9d6c18d-229e-3c6c-b6e0-17ee215ecb7d | -17.85476 | -52.11349 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| af5832db-e7ad-3dc8-ad9a-c11e93d202f6 | -17.73486 | -42.07138 | 2026-08-31 16:28:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cf64d86e-57ab-357a-9335-dbb412a63ee3 | -21.27899 | -43.80585 | 2026-08-31 16:28:00 | NPP-375 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e0d20173-779a-3535-96f1-46852231f1e2 | -18.26803 | -52.68843 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 43b98076-08d1-34fc-886d-10150ad586be | -17.55454 | -46.97805 | 2026-08-31 16:28:00 | NPP-375 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e2a02a41-e7ea-3e18-b38e-416cebab50ad | -17.54365 | -44.61425 | 2026-08-31 16:28:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efb0538a-fcdf-39d1-aaec-e8ba77b24c6b | -14.91545 | -40.04645 | 2026-08-31 16:28:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 18a47824-a4ce-3002-bb76-665b778689b4 | -18.12626 | -51.61203 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f9ad1b84-c667-39b0-a7e9-be0d6eb792b7 | -17.85637 | -52.11065 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 145.9 |
| e10c8aba-b5fb-3ff5-a856-4d4f03d41a61 | -14.98834 | -39.52892 | 2026-08-31 16:28:00 | NPP-375 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6e568c4f-88bf-3a57-b4b2-b7c82912ac07 | -17.84576 | -50.51356 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d39d351c-433c-3a50-9ae2-2ad9fe1ea02f | -19.04694 | -48.54627 | 2026-08-31 16:28:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b77bfd98-0e84-362b-9623-4faaed66cdc5 | -15.26164 | -40.62858 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 390f89be-f498-3fe9-b86a-8937c128f5f3 | -16.48389 | -42.306 | 2026-08-31 16:28:00 | NPP-375 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 987e2515-d01a-3ca7-9bb7-82c9f3481020 | -18.64949 | -47.53664 | 2026-08-31 16:28:00 | NPP-375 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ddb5fa7f-78e0-3ce0-a4d8-4b44b91a3966 | -17.16706 | -41.32864 | 2026-08-31 16:28:00 | NPP-375 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a7e7c88f-6749-357e-85f3-e58be0769585 | -17.37285 | -44.88676 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d70a7a32-045c-3b10-b904-bb3b65d003b2 | -20.28351 | -47.83926 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0bb43724-e7ec-3d75-92f4-a4c2ef0c8d73 | -15.21205 | -41.7466 | 2026-08-31 16:28:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| d70eccc3-1fbe-32ae-84f5-7dc688d038ec | -19.84805 | -47.92633 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 1df4cb19-68b5-32d1-8f10-97e8190ae60e | -15.11241 | -48.15785 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bf7c13d-89d0-31aa-98d7-7b0b83965f59 | -17.79207 | -44.44905 | 2026-08-31 16:28:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 874e3724-dc10-3333-afb3-41de5eac4e21 | -17.6186 | -49.05445 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 550e8cc4-bd33-36ed-8660-e1282dbcef5a | -20.29846 | -47.83763 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ad7a1175-69ab-3b01-a9da-82635f4aaf2c | -14.98888 | -48.12994 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 794091d0-518e-35d9-81d8-5175cd7148db | -18.1259 | -51.61396 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| c3ffcdba-022c-3471-a01b-cb8f923c67e3 | -16.26974 | -39.46473 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3983810c-cc5b-397e-bbdb-13ce2899c8f3 | -16.00188 | -43.54129 | 2026-08-31 16:28:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4539951c-5d78-3078-830b-bec6dd89ec88 | -16.58646 | -41.49824 | 2026-08-31 16:28:00 | NPP-375 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e9ea6807-f061-3273-99ce-b19266d4acd9 | -20.14456 | -41.96778 | 2026-08-31 16:28:00 | NPP-375 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ffd21424-55f1-328e-9707-1ff6645f4849 | -15.19292 | -48.97866 | 2026-08-31 16:28:00 | NPP-375 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a486e182-bd6b-3d0d-9715-095ce0bac3e0 | -19.37239 | -43.43815 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 105a1e1f-ed67-3f77-b5b8-feac59540f14 | -14.32137 | -42.21842 | 2026-08-31 16:28:00 | NPP-375 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b2ec5230-c020-3efe-8db9-a632d90e1ac2 | -15.66105 | -48.69418 | 2026-08-31 16:28:00 | NPP-375 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 34feb03f-3a8c-3d70-b5b4-f4df09212a3e | -20.28754 | -47.83479 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 41.2 |
| a7bc35cd-872a-39e5-94a2-01e7ade06031 | -17.87543 | -52.10912 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| df3603d1-8a89-3041-9900-69d428d3a88e | -15.58534 | -42.07855 | 2026-08-31 16:28:00 | NPP-375 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6e0f02f6-aeaf-3bfa-bea2-e92b7c4f546f | -15.16195 | -40.32918 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 326f4bc2-1719-3b87-9081-fd0c4f9e8988 | -17.72198 | -44.26008 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 695a2012-e7ee-3c60-adca-f87641244ebc | -15.66574 | -45.9142 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6a33564e-8b43-3f80-a38f-bd656e978b58 | -14.95645 | -41.4003 | 2026-08-31 16:28:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0cb5e0eb-3603-3c34-9a0a-72d578b02d7a | -15.99048 | -48.04759 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 34044382-47ee-344d-8618-b0b7ca8efa8f | -18.41154 | -47.95654 | 2026-08-31 16:28:00 | NPP-375 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 85d3ef8d-02fe-322a-91a4-812aa26f858a | -17.71629 | -44.27558 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08248b3f-d39e-3b18-a4b4-a6b463e02c1b | -16.55083 | -52.51337 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e30a7774-312d-3e34-a9a7-2db10d64e285 | -15.64618 | -50.10368 | 2026-08-31 16:28:00 | NPP-375 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4fe3f99a-a099-37d9-b7ad-cc9bf0ff526c | -16.28181 | -42.58362 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d32ac62b-2b2b-313b-8665-35609a24a4e3 | -19.83441 | -47.93991 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 80cfe233-dc35-3574-a8af-fecac16ca70f | -16.02519 | -54.4073 | 2026-08-31 16:28:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5919badd-f062-3321-9a6c-f245d46bf72d | -17.30629 | -46.96206 | 2026-08-31 16:28:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f7837e9d-520c-36bb-b61b-d85927607aed | -15.96536 | -39.11116 | 2026-08-31 16:28:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f00a5474-b846-3b7f-a3a7-9e5eb078a142 | -16.57841 | -52.51294 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| a34fefeb-7c41-3fef-8f54-dc542a63ff2f | -17.5307 | -41.3131 | 2026-08-31 16:28:00 | NPP-375 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 4b8a29a5-2c94-30b6-adb7-fe7ff529a4cb | -17.87967 | -52.10635 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| bde501e0-98ef-322d-8d71-abf7da8cebaf | -14.32376 | -41.34463 | 2026-08-31 16:28:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee3098e8-fbad-3068-a9a0-b8722e9c9b75 | -15.60994 | -41.51835 | 2026-08-31 16:28:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d0da2977-b44f-3869-8102-63fcffbf1299 | -19.36987 | -43.44786 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a7cc8d75-c6f6-3bb8-a28f-c142013198bd | -17.79225 | -44.15593 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 222e2645-65a1-361d-aaf4-47d22b11db2b | -15.64578 | -50.09991 | 2026-08-31 16:28:00 | NPP-375 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b770fcd7-53f4-3a56-9f3b-f30377800bab | -17.85579 | -52.12406 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7bd087a1-0da1-3113-a4ca-cedde63161aa | -17.87446 | -52.09858 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 6cb8639c-5c9b-3e4b-8d9b-60aa8a09e4b0 | -17.18563 | -48.83647 | 2026-08-31 16:28:00 | NPP-375 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4cef2817-43ec-38d8-b9ba-6ce3e7f87307 | -19.66732 | -40.2248 | 2026-08-31 16:28:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f61bbec3-60fd-3dc4-8270-e7e472460692 | -15.01887 | -48.18043 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9b2772be-631e-39cf-9762-f7e3b7ae4108 | -17.82433 | -44.45462 | 2026-08-31 16:28:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c42ee86-15a7-3b80-90cb-c0ebc064ce16 | -17.30177 | -46.96261 | 2026-08-31 16:28:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2252c60f-d5e2-3ab2-9d07-9cd15ecaea6a | -20.82326 | -42.75606 | 2026-08-31 16:28:00 | NPP-375 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2e2b4f39-d63e-3fb7-8845-2536ac698bec | -16.71665 | -39.16113 | 2026-08-31 16:28:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4c0a9d41-b15e-30db-8e31-0ef19e81a022 | -19.59288 | -46.53862 | 2026-08-31 16:28:00 | NPP-375 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 227f6bfb-8192-3870-b843-875502ec5ddd | -18.69403 | -48.22695 | 2026-08-31 16:28:00 | NPP-375 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 8943924e-fee6-3607-815c-537daddbbe5c | -16.39618 | -40.91787 | 2026-08-31 16:28:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| aec342c6-d8c9-3d9b-aca8-c4e1ca667e42 | -20.30105 | -40.86321 | 2026-08-31 16:28:00 | NPP-375 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |


[Clique aqui para ver as próximas entradas](README110.md)
