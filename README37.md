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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0048576c-7d30-3a35-bd95-80538e9983f5 | -3.57776 | -54.71509 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9fe9a8f4-5a28-33cf-a603-bc3be06d5e0c | -3.24828 | -54.0237 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9930449e-aa7a-3a72-be71-eca09d9e5bbd | -7.10414 | -46.72165 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07b43fb9-8adb-3054-aadc-7407841495be | -9.31621 | -47.37061 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 724e5376-abb2-3b9b-89a5-52b2320820be | -3.26383 | -50.3942 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3a3e1f4-ca30-3941-b8f1-02403bc3d81e | -8.997 | -47.73997 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 298407c1-df0e-3f8e-b2de-06a5c0e24951 | -6.22805 | -43.85321 | 2026-10-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaeb69c6-d758-3054-9b97-7b922525754e | -6.06514 | -44.66436 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce5847fc-efda-3aa4-ba2e-028e3c446fd8 | -3.17354 | -50.59106 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f58e8cbe-e048-32b2-93b9-1f8b2fee16e7 | -5.316 | -50.06725 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2e7439-f952-3366-b064-8cd54b3ddf7c | -3.00767 | -51.0155 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dacf47d-8527-30a0-a14a-e07e6adf60c2 | -9.93927 | -44.8914 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf582153-01b0-3489-82a8-9ccffb59b098 | -5.62162 | -43.64716 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c2b213a-8195-3124-b5b5-66401fcc1f4c | -3.11163 | -53.794 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0f13168e-161e-3d5b-be62-8dbf0364aaf3 | -8.94958 | -45.12212 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d81b4aa4-ca1c-3424-8530-99130623ede2 | -3.10596 | -53.78692 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5d18f654-d783-3eb3-8f57-e95781da6312 | -3.16256 | -50.58928 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54db58a5-4257-36e6-bed3-8cb7b9f4906d | -6.42847 | -55.25785 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e778a9f4-929e-3fda-98ee-01f53c03a7dd | -3.76284 | -45.95724 | 2026-10-10 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f31f1e5-f523-3ae1-b35a-4a906224f04d | -2.75201 | -54.10443 | 2026-10-10 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ff874d0-4a53-32cb-970c-3f2dce1e93ba | -3.87637 | -52.25798 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7a4b4fb-8d40-3c8a-a5e3-9a803c360c08 | -6.32447 | -43.4948 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4c0f418-351b-3063-b5d8-a66345662e93 | -5.2365 | -50.6866 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2f274d4-b400-3325-85f6-a3be6ce2f55e | -7.56785 | -45.64746 | 2026-10-10 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 416ff1a6-35b5-3371-9ba9-29b9c9e51cbe | -7.52176 | -45.30843 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1c3b943c-8fb3-3e66-8105-a4d91ca478fd | -9.92873 | -44.78293 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5877736-506b-316c-b1c8-7df002c08545 | -5.7532 | -45.12693 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cdfbf89e-fd64-34ee-a980-80e5a735b87d | -9.93835 | -44.87533 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 801d3e35-15b2-35cb-a2ac-7312891ab208 | -2.30039 | -48.54248 | 2026-10-10 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a597d62f-3acb-33cd-8d51-7fda82220535 | -8.08829 | -45.63221 | 2026-10-10 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69219ec9-a1e8-3296-a6e5-e89d1331fb4b | -5.75249 | -45.13127 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a7962140-21c4-3a4b-a8f3-1acda9a09d82 | -9.11503 | -45.82788 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a876fed4-036a-3ee6-830c-7351efa8dc3a | -3.21475 | -50.55193 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06f8e0b7-50fd-3543-af5c-9ca147ad7d7b | -6.43652 | -55.21202 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3ac7154-6e4f-3692-9d04-8e7f55c1e579 | -3.57236 | -54.69338 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0ec3ccd8-0486-3dec-9dae-35d6c107d6c0 | -3.54271 | -54.73758 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e6fb922e-379b-35ab-8ac3-4dc5f37e1023 | -3.25784 | -50.39679 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0d8bc1f-af31-3d8d-80a2-62f3a98b162b | -3.80488 | -49.93583 | 2026-10-10 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 272a0eaa-c169-3ebe-8d3e-b5999929a87a | -7.36899 | -44.05584 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab6976e2-acc0-318b-a779-6a3b3bbcafdb | -3.27043 | -50.38803 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da8c2eff-d65f-3a51-8869-46346b878c5e | -7.19434 | -52.63154 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb699e29-35bd-3dd2-b07d-7ec171c992c8 | -7.12058 | -42.5376 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 07499cd0-cb1c-3c3c-a869-a0ec3f11e4db | -6.06288 | -44.65573 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39fa6451-4c63-3829-ae62-ee15d089d3af | -9.92609 | -44.78304 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3814e933-613c-3753-ac12-c35fbfeb1c99 | -3.18335 | -50.59999 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db41bab7-65dc-37a1-aeda-fa569209aa68 | -7.20754 | -44.33643 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03b42772-1511-3818-bc61-62124ae0f9c1 | -6.99317 | -47.72457 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db92dece-afa6-3a27-9349-bebf6e30f5fc | -6.23743 | -44.09721 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fcbb4a1-6a75-3075-8375-ca8417aee052 | -5.42344 | -39.26841 | 2026-10-10 04:08:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42e58f25-1df8-3e27-af08-11a5435ceb2d | -3.24949 | -54.02779 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1141b047-047b-3ab4-bc46-00362b8dd8ef | -3.59845 | -54.58723 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 012255d0-902b-3f3b-a8de-4b18e3879518 | -6.70023 | -40.46996 | 2026-10-10 04:08:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eeb2efc1-1ef6-3dbe-ac85-b38cd30f59d2 | -4.32558 | -41.24292 | 2026-10-10 04:08:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c56dd39c-c2b1-3cfa-8082-1041fe438c0a | -3.34499 | -50.40732 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83717022-1d5c-37cc-9017-527dc8acb38d | -6.80648 | -52.7828 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd629cb2-2f28-31f2-ba53-1a23fef40b6e | -3.21831 | -49.4414 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac47d0f-9941-3806-aebe-4b6f87d06fbd | -3.50297 | -54.61483 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d904cdab-6f08-3107-a5aa-043ec6da72d0 | -3.15098 | -50.59111 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9bcbaaf-4e4c-3bf9-9f7c-fa9fdbde2d10 | -7.08224 | -43.9377 | 2026-10-10 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42993a15-0f05-3dcf-923e-acc9007141ce | -1.62721 | -54.44167 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ee499a9-9fa8-3ecb-b4c5-61e96fcfe143 | -7.02644 | -47.68179 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 585673a0-bb61-3d84-b13c-80ba84c8dd74 | -7.184 | -46.53582 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabc3c39-f5ba-3c5f-a0d6-a8a37ca0ab3c | -6.87557 | -45.03705 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 174f9f05-8dd4-33b1-9d23-74b824725ee1 | -4.02711 | -46.98701 | 2026-10-10 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 413c4e64-6d76-3181-86ea-b57576013641 | -8.23651 | -46.42813 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe665fe-bef2-39e2-a1b5-6d3dbc76fb96 | -3.59963 | -54.58707 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 618603ce-4a89-3037-91a0-9d9924470717 | -8.54028 | -47.35591 | 2026-10-10 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adb998a0-92f4-3d85-9da7-706ea1c059fe | -6.06938 | -44.66085 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02bc1d92-6cdb-3003-8762-1700a83257c6 | -3.31393 | -53.84038 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59296e0f-ff2f-3091-a8a0-59ed1ac6e4e2 | -7.20509 | -44.35159 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68e2b880-3648-3dcb-9edc-aee51b5eb594 | -6.9974 | -47.72533 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b54b667-08e0-35f2-b11a-7f71afaec610 | -2.21067 | -50.82539 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08372cd2-7a89-3509-bca7-65018a42eeb0 | -7.22397 | -44.16938 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4db421b-40d8-3884-829f-30292c1e680a | -3.31746 | -53.83854 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9048d28f-45e9-308d-8e7e-406e44b61be1 | -6.32026 | -55.33511 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b371098-15a8-3a65-a397-68156a9c5215 | -2.39406 | -51.29959 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72b770ec-da6e-33d6-b3a4-9e74b602312b | -8.19727 | -45.74648 | 2026-10-10 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ddbf698e-2df2-3655-b612-245834c420d4 | -6.32076 | -55.34172 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26233dbe-8f63-36c8-9ea0-bb2e9fed37c3 | -6.36624 | -45.95684 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aacc0435-5e37-31e5-9f41-596b64a4e4c2 | -7.24024 | -55.22102 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4f424eb-f177-31a3-a7cc-4c14506fc4a7 | -4.13282 | -50.8245 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33eb98a3-accc-3ff7-9605-28fb62026112 | -6.87061 | -45.04471 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8221b4d1-7788-37ee-8934-7d87e39d1309 | -8.77524 | -49.61092 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fd9e06e-a068-3e09-a0c7-7f8b59025800 | -6.2246 | -43.85272 | 2026-10-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38114ade-8090-3c3b-bf3e-3ec0fc81b28b | -6.06805 | -44.66904 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5086946e-8779-37d7-939d-4e979de8637c | -7.24186 | -44.16824 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40d7e1cb-5e43-38d7-b6cc-16f9087d076e | -5.23118 | -50.68562 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 93007c6b-db37-3a57-b1c7-994607a05dd2 | -3.20768 | -53.85536 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ae74ab9-934d-3a77-96d3-96f2046c0120 | -3.34873 | -50.41846 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bf0f5f2-c37e-3242-b376-cc2e39a6e5d3 | -4.13894 | -50.82179 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1c60159-f3fe-30f2-be86-8238a0ea201f | -3.45727 | -50.59179 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e78ed2e5-9a94-305c-80f7-bd7c88270e7c | -7.08976 | -52.68056 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54f7c752-75ae-3821-82cd-0887d4572ba7 | -2.39474 | -51.29546 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f445516-dcff-3d26-998c-bbad35556568 | -7.23175 | -40.35686 | 2026-10-10 04:08:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65305d6a-b00e-3fee-8c63-54998fb6f917 | -8.27095 | -46.42673 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efd8c935-b30c-39d3-bc80-4e164edf6ded | -3.48538 | -50.49113 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3778d6c-6c26-3d9d-868c-9e86a7a92da5 | -5.84142 | -44.92993 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd7edeea-0760-3bcd-900d-f20e6d4d7188 | -8.4531 | -47.98601 | 2026-10-10 04:08:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 215c83e4-8cfb-3955-bba0-13560f7458b1 | -6.15367 | -53.30973 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f4697f-3b53-3122-9649-95ccbb4dbd5c | -3.26109 | -54.68623 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README38.md)
