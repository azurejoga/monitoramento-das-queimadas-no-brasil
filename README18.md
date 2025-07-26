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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87401b67-fb8b-3de2-bd52-a266c569a1b7 | -7.99763 | -45.04313 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d41f99af-2df1-3f3f-9b73-cc6640daa5f7 | -6.92835 | -43.95102 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c8051ac-e759-386f-90c1-ab045ab509f2 | -7.6383 | -44.27766 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2149d71-e253-3a00-8e8b-97b8e3c6ff4e | -6.66288 | -58.88401 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 55452da4-4fbe-3ecd-a6ea-eada4c2e25ce | -10.67509 | -51.88995 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a8a898f7-1068-371d-b439-be8d7fd6441f | -10.89267 | -44.20859 | 2025-07-26 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4afdc06f-488d-3f7d-add2-eb9501b105a7 | -5.43967 | -46.28762 | 2025-07-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf12bbf0-2e4b-3938-9afb-89976eddcbd7 | -4.30323 | -48.10267 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05642c01-ef29-312c-bd86-e80d06f769b8 | -4.30729 | -48.09944 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c83ee90-26fa-3572-97da-db20993cf48d | -5.74017 | -43.05647 | 2025-07-26 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b1072fe-70b4-35c7-8456-4379bf83035f | -6.65741 | -58.87695 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d972bba-dfef-37d0-bfd5-9f3922279970 | -7.2332 | -43.0695 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a916344-19e9-38ec-8b79-cfb48a0198c9 | -6.65942 | -58.8659 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 6cafa0b6-7084-3764-b7f6-f3c2b1a3bd78 | -6.64305 | -58.84203 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 09af3bf3-6138-3ed0-b764-b6ec32a5e27e | -9.58059 | -43.85853 | 2025-07-26 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d362e9d9-5ed1-3f05-aea1-204be706f53c | -6.65937 | -58.86263 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 6437d705-3507-3132-bb8c-8f65529f9b9d | -4.7768 | -45.33808 | 2025-07-26 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f4081cb-f5fa-3873-b661-379f567b61f6 | -9.60038 | -43.87472 | 2025-07-26 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6dd66acd-6711-3659-9b49-45abaf2ee46c | -8.17413 | -43.22186 | 2025-07-26 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d455ae71-341a-36a2-9af6-9ceada379980 | -6.7074 | -44.09444 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 165278ed-eecf-388b-82ab-210fe02a476b | -4.77735 | -45.33461 | 2025-07-26 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e76dcb62-0d28-3b67-a39f-01da74730a64 | -6.90435 | -44.29522 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5dcf1fd-d7e5-3cf2-9615-eb3ee46e54bc | -7.24309 | -43.0737 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 34d7d1ad-dbba-36c8-94b9-d82f55470284 | -5.73942 | -43.96797 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98f4dcec-4166-35bc-84c8-22e470d0d331 | -9.3614 | -40.31239 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| ceeeae28-4e14-3ea7-99fa-1660bd356090 | -5.67515 | -42.79266 | 2025-07-26 04:25:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af26ca12-081d-35a0-b44f-78968880131a | -6.86723 | -43.68661 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2ff101d-18a8-3cad-a8b5-6ea2c7ad394c | -6.64093 | -58.85646 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 20f62831-6ad8-3f9f-9608-1cbd2086d585 | -6.8797 | -44.20132 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae4371ab-6a73-3c5d-9aaf-4645c1a0bfd9 | -6.61701 | -58.84003 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6e99fab3-0763-318b-b010-dbd07bbce8e3 | -6.66797 | -58.85584 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 971.7 |
| 2c787069-bd61-3652-a550-1d3376d89876 | -6.66999 | -58.84466 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b4980c29-4a4b-3025-871f-574d8b0897ec | -7.07919 | -44.04982 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4ec496b-da81-3439-bd6a-0851bce50f27 | -6.65832 | -58.8682 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 697a8ce7-d501-35ba-b4aa-fe66b613102f | -6.21153 | -44.80932 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fb62a97-8a5a-3641-8fa6-e6b90446adfd | -6.6451 | -58.83123 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 121f494c-3955-3119-aae4-a20e077351f4 | -6.65572 | -58.92361 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b8ac974-adbb-30e5-9d77-fcfba5c6ff4e | -9.13126 | -45.87433 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05074c44-ee16-3c87-a3f6-75a8dbcdec37 | -6.64845 | -58.85211 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 296.7 |
| 8140d551-c0ce-3541-83f5-2da5d0cbb18b | -11.94767 | -43.82949 | 2025-07-26 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5f50cd6-26b0-3f2c-ab5c-78a7194145e3 | -6.6385 | -58.8329 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7bbfa29e-0574-32a5-83b4-c073a9efa775 | -6.2121 | -44.80571 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1ebb2c6-0cdf-3343-97d9-09f434c6fa01 | -8.00559 | -45.01408 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c78ea427-cd28-3ced-85a2-d2045ac5acfa | -9.35688 | -40.31176 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 747d0622-1f51-3ceb-9b63-1f85abeda5de | -6.68296 | -58.84731 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| a05afa48-09cc-3dea-bfef-09aa840676fd | -9.36526 | -40.31763 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 2b537aeb-4c9b-3cf6-8f7a-f2e4a319308e | -4.07491 | -46.90015 | 2025-07-26 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8597ac4f-f788-3a90-9f11-59f730897413 | -6.91385 | -38.56046 | 2025-07-26 04:25:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c90000e5-9045-3cbf-a38c-303a470cdc5e | -8.87057 | -45.58494 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d2ebecb-b9dd-3782-8d46-11029674c4d6 | -5.91404 | -44.97009 | 2025-07-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ea12fc3-71bd-3004-8f82-12b898ea38e7 | -5.05842 | -42.81694 | 2025-07-26 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38485669-f252-396f-a907-333119cddd2b | -6.66146 | -58.85463 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 971.7 |
| dd1dff60-3221-35c5-9ead-4cd9e70c22e0 | -6.63204 | -58.83149 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 20e1168a-e1ee-3c7e-8744-34bf6ec95e03 | -7.09844 | -44.8802 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f33be36-992a-3883-a4aa-4fb293701342 | -8.81892 | -46.74628 | 2025-07-26 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c01e803-64ff-3d6b-bbb3-c191c56e5eaf | -9.01861 | -45.35146 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9210cc3-a466-3661-b057-42ab0f41b93d | -6.7824 | -44.10465 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b05e794-59b2-35c0-9ebc-fca1d844153e | -6.90567 | -44.21723 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38e013a6-b200-37d8-b6af-a80bdeaa502f | -5.73884 | -43.97174 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72c3bb67-13c4-30c7-b4d7-fec9521e7ebf | -9.35874 | -40.30844 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| cd906242-ab67-3d1f-b46f-923478b0532b | -4.61944 | -43.32134 | 2025-07-26 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 745f5a1d-195a-3035-836d-adff59cea3ef | -6.9156 | -38.56274 | 2025-07-26 04:25:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 005b034a-0d34-34d9-b0e8-367b800ad615 | -6.66031 | -58.93559 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7283dad-ec5f-3506-99e0-f18e3e07c52f | -6.67201 | -58.8335 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 14d61bbd-46b0-3b70-8fb0-9181a1a30488 | -7.24122 | -43.06625 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f71e22f7-f0e3-319c-875b-7bb4a6f83c73 | -6.87554 | -43.67971 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f45a2b7-52d3-329d-b354-2963621445f7 | -7.97331 | -49.69084 | 2025-07-26 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef0f97e0-70d2-33e9-9c89-78961a89c060 | -8.17348 | -43.2262 | 2025-07-26 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b94b4c86-5773-3c99-910e-ad4c70e14d98 | -6.66775 | -58.93182 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b1b7de5-131c-3da4-8eea-64d0c8a8da16 | -6.66393 | -58.87819 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d1ae742-1a02-3765-a8aa-43df9fa8ca81 | -6.65181 | -58.86697 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8167437-e6b6-3131-b5fd-81ee970a593c | -7.52342 | -44.225 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a8bc2e-d741-3e93-bab4-667e0db2216a | -6.63489 | -43.04513 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de774a4c-35bd-3290-878c-77c459d31337 | -6.76326 | -44.11353 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a01269dc-cf50-362c-8c41-1857232e2783 | -4.30384 | -48.09889 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fff58579-a963-3049-bb4e-f10b58d09058 | -6.6602 | -58.82246 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 66c73df4-e59d-3b90-ac4c-171fecf28831 | -4.61531 | -43.32476 | 2025-07-26 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ca96504-b81c-3dc8-943d-993a469e801d | -6.67133 | -58.8707 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 994c52ed-6e45-3162-a7c8-e488a9b6e629 | -6.61598 | -58.84563 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6f3609df-9375-3375-9ac8-0350020aeb8a | -9.00903 | -45.36869 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ceb8dc8-4fd6-36ad-bf82-74ae85ba0429 | -6.63761 | -58.83522 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 4f5481c5-0d78-3b0a-b878-0758a0c571b6 | -4.96404 | -43.21973 | 2025-07-26 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5363bf0-0b48-328d-9530-8976fab46aa7 | -6.66349 | -58.84338 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3d76054c-be15-3661-8267-9daa3af3cd02 | -6.88895 | -43.11975 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71371e3c-90bc-339c-b196-65cfe6260eff | -6.15645 | -42.59837 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c5169c9c-6ada-3e91-87e9-44f8f8d87b21 | -6.62902 | -58.84791 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 35e14ee3-13c3-3829-91ad-8f71593afa2f | -6.14901 | -42.59718 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 734ec882-f779-3b3d-9239-5d5360cb04e8 | -6.98937 | -47.07994 | 2025-07-26 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66db4e5a-4fcd-322c-bff4-da06d483df1b | -8.17176 | -43.21259 | 2025-07-26 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a29739f1-bff1-3000-aec8-db41b27046a2 | -10.67981 | -51.88572 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17fcc8e0-620e-3ede-a9eb-bf39995b38f0 | -6.6567 | -58.91816 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19c651d0-22c1-3243-9203-5ec24f3f21a0 | -8.30389 | -55.10813 | 2025-07-26 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2309236a-e0bf-3f17-b3e5-8a7747695375 | -6.23303 | -43.71967 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a468269-2300-3d55-8de5-7c3badb17f06 | -7.24245 | -43.07804 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4b46cbdc-53d5-32c0-a33d-b925f672e96e | -6.64884 | -58.91849 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9694139e-318e-3c9a-a36b-e3bf92736544 | -6.65329 | -58.93082 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16568b47-f611-32cf-935c-a40517b394ce | -6.2295 | -43.71922 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e4dbcb4-6068-3b0b-8e0f-088804f6c812 | -7.24373 | -43.06934 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 9745e0de-daf4-3eba-b15e-3a7c4f4a06a9 | -7.24005 | -43.06878 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ea6d1c08-1c02-364b-8a74-c6636afd7f4d | -6.65048 | -58.84097 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |


[Clique aqui para ver as próximas entradas](README19.md)
