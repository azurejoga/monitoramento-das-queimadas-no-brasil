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
| 8667ecb7-dc41-32a0-a2de-2a5acb5a13cf | -4.08175 | -43.95907 | 2024-11-01 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 321e19c1-55a9-3475-90bf-7c052dada937 | -4.06338 | -43.28434 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8610abc8-c257-3421-a4e3-91a83f4f2b55 | -4.06289 | -43.28735 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8714ec6-e533-37c0-b418-305faf53d41b | -3.94463 | -41.51109 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 132ecaf7-9d15-375e-bc6d-2e8723ef7fb5 | -3.94425 | -41.51186 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 465667e6-7d45-332c-8634-2d866d688b87 | -3.9442 | -41.48298 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f76ba13f-4e49-363d-a45a-879a9fb13a6a | -3.94386 | -42.63575 | 2024-11-01 03:42:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9978fb7c-16fa-31ce-beab-0c144cef3018 | -3.94383 | -41.5158 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5b265f89-eb2c-395d-b483-3912c3687d72 | -3.94349 | -41.51657 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4b401521-4b3e-3f1f-9d18-cd904cf73256 | -3.94084 | -41.50568 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d76c7a6-1ccc-3ff9-80a2-47bbf0d8e198 | -3.94043 | -41.50642 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 887e4792-ca0e-3d2c-bd54-b66701a7acbe | -3.94005 | -41.51035 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7349e8c7-6665-3c77-8ea1-f8225d49b61d | -3.93968 | -41.5111 | 2024-11-01 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 985ba394-90d9-3fbf-a4ec-3789112d469a | -3.87541 | -43.95147 | 2024-11-01 03:42:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2012b446-dd4e-3e20-8417-e9e907725b38 | -3.87484 | -43.95482 | 2024-11-01 03:42:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b77b141-535d-365a-a9ce-09d475713cd7 | -3.86942 | -43.95402 | 2024-11-01 03:42:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e9f200a-27c9-3834-a5e4-05a8a740513f | -3.85359 | -40.7071 | 2024-11-01 03:42:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7cc78db0-eb29-3971-945b-feacedf49fdf | -3.8529 | -40.71123 | 2024-11-01 03:42:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8eea98e5-8576-3a2e-a2e1-fb1694b50a49 | -3.85186 | -40.70787 | 2024-11-01 03:42:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aae326b7-f54e-3e4c-8e6e-e6c31dd811f5 | -3.8512 | -40.71199 | 2024-11-01 03:42:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51c9acc3-6664-3365-bf7d-2decf42326f5 | -3.84858 | -40.7105 | 2024-11-01 03:42:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aae58e56-5c18-375b-bcf3-b4efd9007cc4 | -3.79146 | -39.09528 | 2024-11-01 03:42:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c34ad02f-4fde-37e2-8ca1-d2ecaf03754c | -3.76925 | -43.53083 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b49edca-50f3-32ba-84de-3145b24101b8 | -3.76872 | -43.534 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d84ec50-0c83-330a-b00a-6f3e3ccbc0f2 | -3.76766 | -43.54035 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a8db566-d391-3e5d-86f4-6da6755e8964 | -3.76714 | -43.54349 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77c61537-cd34-3bba-917a-9861a0bef347 | -3.76661 | -43.54665 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3306e8bb-1f15-30b4-9f4b-beb7038c5b1a | -3.76397 | -43.53004 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60aa17d5-f4e7-3fac-a76c-f087e101975c | -3.76344 | -43.53323 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc3ae5da-3112-3ff2-8f0d-187252e6fece | -3.7629 | -43.53643 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f589ea0-8226-37b5-b984-18d41559a7db | -3.76237 | -43.53959 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 857c5fa7-b223-3c68-bdbe-37aaea8d54e4 | -3.76185 | -43.54272 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8379db42-4f26-3a37-8132-960a0c5b6d17 | -3.76132 | -43.54587 | 2024-11-01 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 331ab31e-60f0-3b61-80b3-80e3824dc341 | -3.57172 | -43.23011 | 2024-11-01 03:42:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45eb17dc-2d1e-3890-9132-ab35ff1c4933 | -3.56256 | -42.70289 | 2024-11-01 03:42:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c24cdc7b-d43f-398f-92fd-6646310c1d2e | -3.56209 | -42.70575 | 2024-11-01 03:42:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0db9d525-5350-3582-8464-ed7fae3f2047 | -3.55757 | -42.70204 | 2024-11-01 03:42:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c95b9f4c-21e5-3ec2-a424-c38c2073bc1b | -3.55709 | -42.70494 | 2024-11-01 03:42:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f84ded86-c2c6-3d64-9b08-ecd2c56dc5cb | -3.50522 | -40.75895 | 2024-11-01 03:42:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec659cd4-3b49-3d2f-8ec5-ad93a834cf2e | -3.5015 | -40.75412 | 2024-11-01 03:42:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4620c0d2-713c-328d-bbb9-4488a5d63893 | -3.396 | -41.63781 | 2024-11-01 03:42:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fbdd6ada-ca90-359a-9151-556ddb0b879b | -3.39518 | -41.64272 | 2024-11-01 03:42:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 41d8ea73-429c-342e-a9fe-734a82c76bc3 | -3.39436 | -41.64762 | 2024-11-01 03:42:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 70d6313a-938b-30f5-9a85-24d14ebab57f | -3.39133 | -41.63715 | 2024-11-01 03:42:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 943086b6-b247-3081-8654-683affd22369 | -3.36524 | -41.66077 | 2024-11-01 03:42:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5fba3515-d297-3f3e-b5ae-a46de50f387b | -3.29237 | -43.54251 | 2024-11-01 03:42:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c398993-4e44-31cc-aa3e-508c1724d5ff | -3.29181 | -43.54582 | 2024-11-01 03:42:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f64270-a87e-3246-ad3a-8045f07cf8ca | -3.03867 | -40.06957 | 2024-11-01 03:42:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb9db253-3b6f-346d-b64b-a84d029b32ba | -2.96266 | -40.24296 | 2024-11-01 03:42:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 89b8130f-7ce5-3a95-9795-414718d2e256 | -2.89096 | -39.90503 | 2024-11-01 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7ec26b09-cccb-3eb2-b27d-a7de2452dea0 | -2.89036 | -39.90882 | 2024-11-01 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0ef86943-1b5b-3cee-bd82-8c54d4219dc0 | -5.33749 | -45.1117 | 2024-11-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3921577-f5a4-313b-9f15-4d70b641cc6b | -5.33175 | -45.11097 | 2024-11-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46da2701-9ba5-3f67-96c1-02ce6f6b009d | -5.09118 | -45.49312 | 2024-11-01 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5e233cf-3647-3633-ba78-ca9a2b11169a | -5.07432 | -44.23506 | 2024-11-01 03:42:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a20b80e3-d238-3fac-809e-92909e8431da | -5.0695 | -44.23074 | 2024-11-01 03:42:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d27b0cb-1de6-3cbb-872a-7f9b991c0410 | -5.06891 | -44.23418 | 2024-11-01 03:42:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 764bf4da-f8f5-3d0e-8a53-0604ca02c74e | -5.05451 | -45.53654 | 2024-11-01 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6542b347-bd16-3e16-890f-3c8006635e8a | -5.04862 | -45.53559 | 2024-11-01 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3fb2a00-6cef-34ef-95fa-5ab14461cfea | -4.94202 | -45.70769 | 2024-11-01 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9246e31a-30d6-31bc-b37c-b9533b2935d7 | -4.93902 | -45.7074 | 2024-11-01 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df46b490-22c0-3c0d-99ae-4463fc9f31de | -4.9369 | -45.70179 | 2024-11-01 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 809ff04f-7add-3429-b722-3671c447dafe | -4.91255 | -47.0412 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 303674ec-271f-350a-8f03-524e1f71b7a4 | -4.9116 | -47.04464 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| dbe44744-9233-3364-9464-5f07c0c345b9 | -4.91153 | -47.04681 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 77805785-4af4-3cca-a1e6-eec921a2f9c2 | -4.9106 | -47.05032 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 33422b64-8247-3883-a439-ab3a53c6fb4f | -4.9105 | -47.05248 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 03e7be44-a5ad-3e21-93b1-58573432041f | -4.9096 | -47.05606 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 971ae25e-3443-3f12-99ef-c26413d54187 | -4.90944 | -47.05829 | 2024-11-01 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f88f926-35f3-3c89-a628-3e69de377aff | -4.73448 | -45.75173 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18e85a0f-974f-3aee-89e6-67c36324214c | -4.73262 | -45.74807 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55a2369f-61a2-3ddb-af8f-c1269479bdab | -4.73181 | -45.75284 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 30d0ae26-6025-34f4-be34-1b51d47d4dbb | -4.73008 | -45.69081 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53d5562d-379c-322a-823b-932ffdff5ff0 | -4.72936 | -45.74584 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9112b766-29e7-3b5c-be29-9d50ce1c2f7c | -4.7285 | -45.75065 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4020b229-2837-3e00-9668-dbc056962a4b | -4.7266 | -45.74722 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df4df70c-d779-32be-addc-f42fd18250ff | -4.72579 | -45.75195 | 2024-11-01 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f91ed7c9-62ef-3905-8bb2-5e3ffaf04e70 | -4.65893 | -46.31985 | 2024-11-01 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d653e5c-0a7f-3351-b5d5-c1867fd3d873 | -4.65474 | -46.3165 | 2024-11-01 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb7734ed-4f10-35a1-9835-3b8ac2ef2e92 | -4.65386 | -46.32168 | 2024-11-01 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c708779-fe2e-3709-9519-7aa63f3523dd | -4.65269 | -46.31891 | 2024-11-01 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d53bde6-acd4-3d6a-a02e-721826372a70 | -4.6225 | -46.50613 | 2024-11-01 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28318eee-b5a2-3e71-9bf6-d928798a406b | -4.6217 | -46.51085 | 2024-11-01 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b2be93-96bd-38ca-9a9e-93b24d4947c5 | -4.54422 | -45.71674 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40ebd8ad-dca1-3d9a-acfc-411458d046c9 | -4.54252 | -45.71355 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64ffe0b6-bf5f-3ac6-b480-d8ab0e622b1d | -4.54177 | -45.71804 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f738dcf4-2575-3b87-a6eb-3f0aac1000de | -4.53909 | -45.71075 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fee189ed-513d-3e0d-9f46-764849967cdc | -4.53831 | -45.71523 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59bd1e4a-45a4-3b63-be9c-5d0a0c1a1264 | -4.53661 | -45.71203 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a756d7af-16a7-311e-9d69-d029c8ad6af2 | -4.53584 | -45.71656 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a66b51a-0edd-30c6-863e-fe04c3c89045 | -4.45061 | -44.16518 | 2024-11-01 03:42:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 114d2afe-94e0-3549-8df1-d3d5464f620d | -4.44516 | -44.16442 | 2024-11-01 03:42:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7cd7543-58dd-3346-a5a4-543c16f2ebfd | -4.37199 | -46.01484 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b2cd66f-3133-337b-a474-3abee09a85b8 | -4.34112 | -48.59401 | 2024-11-01 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6eb028e-c3e0-3900-b8ce-bb4b6dba9319 | -4.33749 | -48.59276 | 2024-11-01 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0fe67fc0-a0a3-3b90-aec6-80ca0af1d59a | -4.33403 | -48.5925 | 2024-11-01 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55820c3b-be2f-3fb6-a5ce-1174963d2191 | -4.31336 | -45.63236 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aad6d8a-eb23-3a3b-bbb2-3f521531548b | -4.31098 | -45.63127 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ded2084-fff3-3bba-9d1a-07859e67ce94 | -4.31033 | -45.63509 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad3c4714-9c0c-3760-8b30-16a76b7ff4e1 | -4.26612 | -45.74917 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
