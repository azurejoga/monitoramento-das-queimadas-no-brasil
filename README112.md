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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f413dc-e2c8-3351-aa0a-f87a7d29985d | -17.96953 | -51.15332 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47ab7c10-bf42-38c0-bd3e-696d815b5f1e | -15.38837 | -47.95333 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e541962f-de59-32e7-8269-2b0c58b1588c | -15.59722 | -52.51117 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6617713d-1b72-3608-8240-fee489e045a3 | -14.00925 | -48.21315 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d20f67c-b7e2-3d6a-8e8f-af437d3f3804 | -15.97041 | -43.32758 | 2025-10-05 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a7cc3e-6c0e-3b52-bf82-65a58787843b | -16.12643 | -53.97724 | 2025-10-05 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1f3d4c7a-c9f3-3800-8185-f15e6f17cf08 | -17.95173 | -57.60616 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c9b10d2f-324a-368c-a2d1-e6fbb5adfd77 | -13.62657 | -48.68319 | 2025-10-05 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cced3fc5-d656-3834-95f4-8ec6696ca9fe | -13.98971 | -53.90394 | 2025-10-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2b4b6cc-bc80-3533-8239-b41d4ee71564 | -12.23805 | -60.33536 | 2025-10-05 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae44c702-c7d6-3e2d-bca2-79eaf216e0f7 | -19.01318 | -50.60347 | 2025-10-05 04:49:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 06200661-0785-33d6-b878-ee6eacbc3e5c | -15.3929 | -47.95012 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91078785-925e-3f9a-b5b8-651a9b3e5f9e | -19.94278 | -44.38965 | 2025-10-05 04:49:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e76605cd-7ebf-3ed9-9cff-916af3110845 | -16.01183 | -50.95317 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b23d880c-5a98-3d15-9670-6c367518b0b4 | -13.73494 | -47.96625 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34552afc-e8e3-3f01-b4f2-4ee424fd54af | -14.91971 | -46.84966 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c6e114c5-3876-3b7e-9b73-e72f88cca9ff | -15.60547 | -52.45717 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d349610e-d2f4-3b0a-9f86-2e82fcb48bce | -15.59169 | -52.5029 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 296a51ab-83de-37c9-974e-8f0c60ce2b93 | -14.85196 | -60.06869 | 2025-10-05 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68792f76-9b34-3851-bb7d-38ddde69e275 | -15.52748 | -46.87215 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bee5fde-668b-3d1e-8c98-75b3c35ea84e | -16.07092 | -50.90402 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce9cfda9-aa1f-30a3-a057-30ce0106adf4 | -18.2369 | -53.341 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72bb3b94-a58e-34c9-917a-bcb9300e6d85 | -15.17425 | -43.63287 | 2025-10-05 04:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa1bb035-b92f-3c53-8d8a-074ade7f947d | -15.6016 | -52.46027 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a855a40f-8a08-3100-9466-f0338f8f4c4a | -15.78339 | -49.09542 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4965379c-8c8b-3079-a1db-89188b7ab833 | -15.20904 | -56.84687 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fad74faf-9bfa-3de1-8a0a-de9e1f03a57d | -14.56568 | -52.47489 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f856addd-f0aa-325c-8213-c55886010054 | -18.64868 | -50.66777 | 2025-10-05 04:49:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e5f80be-e3a9-3f1d-b246-62a84e3bda02 | -15.36687 | -46.28939 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db7e3e8a-178d-3d1c-bbc5-d2fc2a55c706 | -16.1677 | -57.57633 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3b7fa11c-913b-3b64-bef3-1555b6cc1aae | -17.93701 | -57.60307 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 5575d7fd-51f0-38c5-848c-3727f88b3273 | -15.14299 | -45.754 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b5a6290d-2922-3b77-b84c-9ad3ec9dcd8f | -14.75252 | -54.66206 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edd5577b-6fc7-375d-a3e3-8614c730b06d | -15.52916 | -46.8588 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0167744-55d5-3fab-a7f0-31f0a32acae8 | -17.71148 | -56.74715 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ea3b0c5e-c52f-3c61-b868-3cb647bd24ee | -11.84526 | -63.72349 | 2025-10-05 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dab59b3-929f-3c52-bc98-2c8add0039f6 | -17.96398 | -57.5799 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 44fd90a3-508b-3f95-b1c9-befdabd42458 | -13.91994 | -48.16426 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3e089e8-a14d-35d6-b10b-4df0b5a1a7b0 | -18.33172 | -45.88792 | 2025-10-05 04:49:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 2616bcd3-3240-3f68-a654-2fb1f35b6901 | -14.25319 | -46.1068 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc25a9f8-8338-36e2-bdd5-1d0058d87441 | -18.33516 | -52.01515 | 2025-10-05 04:49:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fa36f5c-c352-3b8c-aea0-7dc22343b06a | -15.9825 | -50.91162 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 614ff3d0-61e3-3152-9e0e-bbac834834f2 | -14.0961 | -46.35286 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a864b24d-4b6c-3ce2-ae7d-412b2689e6ae | -17.57038 | -46.07676 | 2025-10-05 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaa949ad-7a67-3756-8027-edb30ed19091 | -15.23988 | -49.30741 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdd6c438-eb6d-38f5-9cf9-9de6c4088a99 | -14.25263 | -46.11118 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf5498c-a956-3a0b-9a0e-d97aa914c818 | -14.94906 | -46.84452 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0028e18d-631f-3f40-a010-4d9769e938f9 | -14.67417 | -48.36224 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 356bb3f2-227e-36a2-bcec-a52219119646 | -15.37725 | -47.9441 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b933d385-7d2e-3f79-b680-4aab0e546b87 | -18.45079 | -49.43903 | 2025-10-05 04:49:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cef8b1c2-0cbc-325a-8d36-092878926127 | -13.7377 | -51.30656 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bab5fe92-dd2c-35b7-8cfa-01cfe469e90e | -13.82785 | -48.04918 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 555359d9-bd84-345e-8d51-415e1f54dc95 | -15.3068 | -46.31224 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea3572bd-7488-3594-803a-dcfd985154c3 | -15.36445 | -47.97932 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3583808f-ff0b-3a51-9cf2-78da9ec8ac69 | -16.36627 | -51.46958 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 665d1065-8fae-3a5c-9698-fdac3d1fd75b | -15.50848 | -46.84763 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9ade1a6-11c8-342e-9cb7-30d687676a0b | -15.58893 | -52.49876 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 451813e3-6d32-369f-8065-665214111276 | -13.63033 | -48.68381 | 2025-10-05 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| add5fcd4-afe7-3fbe-8a80-6b5f2c3b6d6a | -14.3266 | -47.66662 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00217b4c-3c87-354a-8386-508a2d3b90e3 | -14.92019 | -46.846 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1df81e1d-37a3-30c2-a7be-daad7ec5b7b2 | -14.31883 | -49.9174 | 2025-10-05 04:49:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ebe0dec-3e0f-38fa-a25a-ccdf1b4661dc | -15.30171 | -46.31639 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e75ee5fa-9fae-3f13-9f4e-fc52b8c71ba1 | -15.32659 | -46.37164 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aa2c8e3-dc03-364f-8e80-6b5ca5776aec | -17.9573 | -57.55293 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f69501a1-a007-372c-b374-6b1da5201316 | -16.91494 | -52.0449 | 2025-10-05 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2c15982-c3ff-3961-b0c9-de25c6aa7f3b | -17.88012 | -57.58848 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1cc86cf0-32c9-3359-8d11-a5ca2c1978ab | -15.59391 | -52.51063 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b805e34-28cc-3fae-8932-4d17141a18a2 | -15.42674 | -50.20392 | 2025-10-05 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1cc7539-fc34-31b5-9b46-3085d01b488d | -12.92356 | -54.72776 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ef3ebab-23f2-3267-883e-0c101e36531a | -18.14844 | -53.34142 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 279e51ae-4252-3890-a515-3915d04b7310 | -18.15231 | -53.33834 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35475388-80d4-30fd-a9a2-9bf5ecd8b644 | -17.97825 | -51.14227 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4018c28f-a44d-3a3b-b11f-9b4467974c77 | -16.15335 | -57.57098 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8cda45b8-73ce-3b9f-87e8-039ef185d93c | -14.9277 | -46.85569 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1319ed9c-ccea-39cf-bf3e-7397126ae38a | -14.91237 | -46.87244 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76bb05da-1129-32a8-b580-70b7eead9020 | -13.92033 | -48.16593 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1465f519-5343-325c-84be-0b3a02677a30 | -17.02017 | -43.4534 | 2025-10-05 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d40de882-e305-35e6-86a7-44b83beccbe1 | -15.38887 | -47.94956 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5dc66af-cab7-3bc5-b9b4-f79afc736e03 | -14.97894 | -49.99656 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a00c9bf2-59e0-360b-9f2b-993b81ee3030 | -14.56953 | -52.47189 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40b50fc5-2a06-3a62-be63-ba5d2269705a | -14.94644 | -46.84648 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d0bf94e-30d3-3fc3-a838-56727e7c92e5 | -18.20099 | -53.37579 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef5edc07-45d2-3f32-9906-5bdd891e56c7 | -14.01065 | -48.20974 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b80d51a4-e759-334a-a8dd-8acbae06c96b | -18.2551 | -53.33299 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2e8fd19-414e-3a06-b233-2ec50595c75c | -15.75545 | -46.2725 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d176061-737b-39b0-8c7c-a6d88b2e04b9 | -17.96096 | -57.55377 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f65bfa1c-6e5f-3d39-86fa-74600d0af1c8 | -15.44036 | -44.29024 | 2025-10-05 04:49:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c9a75eaa-562b-3fe0-8ce8-65add63e4f2a | -13.68667 | -48.05721 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21157289-246a-3e51-865e-205a8947a3d0 | -14.58323 | -46.71531 | 2025-10-05 04:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92952105-fd4d-3c1a-a956-806147d5f69b | -15.57398 | -52.46309 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96bf2b01-b00f-31c7-b10d-6971393154ce | -14.57063 | -52.46477 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b2c6458-9734-3d8a-a5ae-ac0e9ca435f5 | -13.94174 | -48.18409 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43907003-dc92-3362-80dd-c776c02b5a43 | -15.38632 | -47.93761 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97046ccf-6437-3eaf-950f-b769cd0799fa | -15.90869 | -48.82473 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 010b9a1f-9b82-3332-9216-4f549802fb1f | -15.54719 | -46.82106 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a19e45c-1c96-38af-b0af-258f0f3803f8 | -15.60549 | -52.50153 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7faf34c1-f7ff-32b4-b014-c582946da18b | -14.3193 | -47.69077 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48609e9a-21b0-3eb4-b993-a9ee487c918e | -19.52422 | -46.4449 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd7347c3-d01c-3f9f-b40b-f5f5bd3b54fd | -18.23634 | -53.34463 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86ba7e0c-e91b-31e7-a9e8-3e4f088126f4 | -16.01895 | -50.83223 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README113.md)
