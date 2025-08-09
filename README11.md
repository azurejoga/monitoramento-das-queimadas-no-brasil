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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 444ec857-456e-33c1-abdb-81f06616b2f5 | -8.32432 | -45.00368 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef7e5d51-1458-38f6-88a9-3bf372a67dca | -5.08466 | -48.31479 | 2025-08-09 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e03846bc-af79-3af2-b769-13eec0ddb834 | -3.84056 | -47.7489 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 285a6f37-8e37-35d6-ac9a-a6a261e890ab | -9.08504 | -45.05628 | 2025-08-09 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee9dea5-0b76-3495-994d-7468714c5473 | -5.42664 | -41.23346 | 2025-08-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9b7f6a8-fab1-386a-8c63-229d7e930972 | -3.2788 | -48.81382 | 2025-08-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bc64420-c5b8-3f55-a418-2a6ce0dbc678 | -4.30175 | -48.07424 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79e9a834-8541-3a83-bdd6-73b21c7d3145 | -6.13594 | -42.96544 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e800363e-a745-3d23-8d0e-99f3b178ec59 | -4.8352 | -40.81028 | 2025-08-09 04:14:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 231342bd-5328-3d92-9aa3-480a459d9009 | -9.65218 | -43.83566 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8f49932-9057-303c-bcf6-a020e4dde555 | -4.47949 | -48.10995 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2063ebac-fc97-3d83-8c89-dc0cf22ce246 | -6.06097 | -43.74664 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d079e509-0ece-37ba-8823-9ea31e2cb51f | -7.32803 | -44.7044 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf6b78b-aba7-3061-9ba9-a44a7620d383 | -9.52234 | -45.41084 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36ab4745-4d62-309d-8586-95bd8d1d8323 | -6.14309 | -44.53823 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320c666b-c289-377f-9fb1-e25884edd0f0 | -8.9336 | -46.73968 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b80aca7-0b9e-33e3-8e10-872acc32e249 | -7.02393 | -42.56659 | 2025-08-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6eb72267-f4d0-3b7b-91ec-a11dc350fe5e | -6.46127 | -44.57014 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b8f5d9a-19ff-3493-bb03-cde977faeb78 | -3.43074 | -49.04276 | 2025-08-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 146bdad8-72f5-353e-a049-85a7255540d2 | -8.32767 | -45.00424 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 447bd551-30dc-3040-8051-3f5e5951a0ce | -9.06141 | -45.08192 | 2025-08-09 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0d36fe5-d27a-3dac-b7a7-62955766ecc0 | -4.75906 | -38.47771 | 2025-08-09 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c54612ed-1b48-329a-ad51-300568ad1a14 | -9.65662 | -43.85062 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92ed54de-0f62-3ea5-b1bd-1c64210d36bc | -7.6091 | -43.96133 | 2025-08-09 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d25e0e7-1d91-334b-9e14-528f9c9e6879 | -6.13817 | -42.97286 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6277c2a3-cca8-3506-92e8-48cb2052a47a | -8.05687 | -46.33059 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abe773a8-b01b-34ce-be0a-971e08fd61e7 | -3.82346 | -41.56724 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6134dd20-c852-3cf6-a8f2-536d7df0d0e2 | -7.29279 | -39.63935 | 2025-08-09 04:14:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67f20820-7f8c-3032-966f-daf7e3044420 | -7.48115 | -44.87221 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f18c94a6-ad45-34c5-a081-e8c08be53a3e | -10.35536 | -40.56329 | 2025-08-09 04:14:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb4dbc74-a8d3-3e99-ad13-be2d2a41883f | -6.90628 | -44.14567 | 2025-08-09 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 950bdfdf-b166-3bc1-bb5d-92ba46e5b378 | -6.68396 | -43.35297 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6397dd9c-fab4-3539-aee5-aa61ed20fe4d | -6.06538 | -43.74022 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba8660a5-b96f-3821-b016-f6656bf4c611 | -5.21829 | -46.06815 | 2025-08-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c442bce-1c92-338c-bac4-457c174870a8 | -5.50205 | -43.21156 | 2025-08-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3cddc3f-a872-3afa-a743-923eb7e7c26f | -6.6542 | -42.00977 | 2025-08-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b49c082e-8f60-3c86-9d14-41e0257273fc | -9.64833 | -43.83862 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f020290-77b8-3430-9d72-74eba2486aa2 | -4.31343 | -48.07986 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51b80596-c15f-3754-863e-23726639bf74 | -5.27346 | -44.94873 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ada20e3-b40c-38ad-80c8-606acdb76faa | -8.32882 | -44.99711 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52844f1b-cb94-3ad5-aac4-b85e87fcb55b | -7.60969 | -45.29088 | 2025-08-09 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 073048e1-ed0e-33f3-8dbd-ce6667e08c52 | -7.47779 | -44.87166 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b7a52fb-f83d-38ab-9e52-c9948a622c3b | -6.13465 | -44.54795 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a8af0a3-d577-35ed-b849-ddc5243e6323 | -7.26036 | -44.6609 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e56b508-8993-37dc-ba96-f4d71cfea0be | -9.51665 | -45.42479 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b228a9f-67b5-3fd3-93f9-7f37ae407b2c | -6.57583 | -44.57721 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb665a0c-2ea0-3e64-a5ef-c7a7de064c0c | -4.29591 | -48.0585 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2218a541-a049-38b3-9f1d-8f93ce06cdb9 | -8.32268 | -44.99249 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5b6e285-e416-3369-9301-f98534433e02 | -6.68113 | -43.32775 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01f22549-67dc-379e-8c26-5598794d90bc | -7.60629 | -45.29036 | 2025-08-09 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ce40d61-3f14-3b39-b5f0-9589d79589bc | -6.6845 | -43.34951 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24e5fd57-a4ed-390e-b7a3-8225237ec496 | -6.68119 | -43.349 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0b9c24d-3533-3445-b90b-c29a6a431055 | -3.18034 | -48.80831 | 2025-08-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb1504c7-d879-3423-bbad-aa9225b68b0f | -3.8414 | -47.74938 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 87ab0a5a-e299-3db1-a256-ee44dc11cab8 | -6.5831 | -44.57475 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eaa02479-ab63-3d0a-8e6d-da1b93dcbc81 | -2.4477 | -47.32619 | 2025-08-09 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de3dc032-314a-3166-b521-e895d6281593 | -6.13156 | -42.97183 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc7cb2b6-1d82-3d8a-a1c4-ee262adc5dfe | -3.84081 | -47.75296 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 76bd88c2-32c6-33c6-b255-ae35d1df20f6 | -8.05972 | -46.33531 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49114d16-0696-3a4e-8fcf-a0f06f21c371 | -8.32603 | -44.99302 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99428369-9ab7-3086-871c-cf88df9698c1 | -6.57248 | -44.57667 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e775b2-8c71-35d2-a902-72c6e3ab4862 | -8.72771 | -49.74195 | 2025-08-09 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33b49467-da47-3832-8f78-755f7cbdc08f | -7.29746 | -39.64221 | 2025-08-09 04:14:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38c67e1a-53d5-3b10-8e13-8f3e35cf7874 | -6.30675 | -42.41228 | 2025-08-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bf3fc2b-03b1-3037-8223-4df308973a31 | -4.70095 | -48.58512 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b38eb9e8-9463-34ee-aab7-5aab1b39912e | -6.06374 | -43.75064 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bb69d78-a656-3c55-9a2a-0f630690d29a | -6.05434 | -43.74561 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eef391c0-c9cc-3073-af5c-3809a1aeb684 | -9.65386 | -43.84662 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8f2ae48-2977-36ac-ad2e-90ae48c818c8 | -7.26092 | -44.65735 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3aac007-01d7-388f-a9fe-641c598d45ef | -9.65608 | -43.8541 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54ed50a8-9906-3094-a6a4-0353ce823baa | -8.07545 | -46.83935 | 2025-08-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d687ca8-d802-3cdd-bfd7-b76c8d127f30 | -6.31878 | -42.35669 | 2025-08-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 988f3234-87c0-3290-a051-9c4be552ca92 | -5.21406 | -46.07155 | 2025-08-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d2deed38-1b7f-329b-ba0c-3cf8d9914a9d | -3.82237 | -41.57429 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e6dc8b82-e1ee-35d0-828c-b18491137289 | -9.0778 | -40.48139 | 2025-08-09 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 33df5321-0106-3116-b536-4d11dd6f277a | -6.57362 | -44.56955 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08e8684a-38d2-3697-9cf2-03094ce95eb9 | -6.13317 | -42.96147 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 198610f7-2341-3834-8752-3a14dc06911f | -5.84122 | -42.95781 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7e6d5e0-6681-337c-abcf-4602f7fbf8cc | -3.82291 | -41.57077 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a654420-413d-3368-936c-5017465cc922 | -5.83953 | -42.94694 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7add9d1f-93bb-32ca-a9a9-6fdec57a2f8c | -5.81194 | -46.21726 | 2025-08-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd5a5840-adc3-34a4-a262-fdf2327ba060 | -9.65771 | -43.84366 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ca3600a-8bbd-308c-a6f4-d5aaf7e7db86 | -5.21049 | -46.07091 | 2025-08-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e545d74-e9dc-32e5-937c-13d2534ed0aa | -6.01654 | -44.43382 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71c97a3e-7029-3bc1-954c-0cc4037da4d2 | -8.72848 | -49.74286 | 2025-08-09 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6347335c-bd63-39cc-90b0-148e751ae3e4 | -7.39502 | -39.68008 | 2025-08-09 04:14:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 58fad702-d009-3fda-b33a-c5665b1ac403 | -6.54642 | -43.1894 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92690409-3dd8-3dbe-a8ab-0adfd8eb1c1d | -5.84452 | -42.95832 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 81413d0b-deef-3855-8457-bd1ac2b69c80 | -7.49877 | -44.9561 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed0b771e-8cb1-33f8-a715-6fd589ef8b29 | -3.96531 | -47.8835 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 985b1ffa-47da-3f6e-bbe4-f426a2135b50 | -7.26371 | -44.66143 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e37c9774-ae3c-377c-9037-14f85ca57ece | -5.41982 | -41.2324 | 2025-08-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 762874ac-9808-3915-850c-bd87067a7788 | -9.51328 | -45.42426 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eda5068e-c85d-3efa-a8d7-cc34701bfd99 | -7.73422 | -45.52352 | 2025-08-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6eccca0-7ccc-364a-902d-0d847449b194 | -6.5848 | -44.56404 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f49134e3-8d12-35fa-ae3d-b8d9796ac762 | -8.32211 | -44.99603 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5924d296-f878-3071-8019-f0ac711d0767 | -6.57697 | -44.57008 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdd434ff-0754-3788-ab6f-f76e8dfd1311 | -5.98037 | -44.149 | 2025-08-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c757e5-279f-3aea-8867-c66b7c734c79 | -5.82445 | -46.3549 | 2025-08-09 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f269f164-c71d-323d-9076-33aa4f174f8a | -6.55911 | -43.19492 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
