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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59a40b42-acbc-336b-a7c3-021486f507f2 | -2.24526 | -53.80119 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 0a374475-ad6c-3ca4-9680-e07ac93c178b | -3.02044 | -47.95576 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b8fced2a-1714-3120-a502-f5e061ff2521 | -2.40534 | -50.3096 | 2024-11-09 00:39:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a04e9bc7-23f7-32b7-865e-f5e13195d084 | -5.44899 | -44.81713 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 30cbc79a-97df-3686-a710-a177f9ff21bd | -6.21469 | -41.6728 | 2024-11-09 00:39:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 39a9647d-28ce-396a-b3ea-16c9a6779cd4 | -2.23814 | -46.50484 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e0d9ffb1-24b2-3317-b11a-dd04593095d6 | -5.47097 | -43.65354 | 2024-11-09 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 370.4 |
| d1cdf483-098e-35bf-b42b-38d5600adb5b | -2.66274 | -46.77593 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4d2a93b-658d-3112-88c9-2d34fa7e88e3 | -4.15765 | -44.40432 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c55e555c-704f-37b2-a1e7-d4ba58893d04 | -6.49696 | -39.55005 | 2024-11-09 00:39:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ca384111-6bd7-3627-97ad-d661d73aec76 | -5.57805 | -41.79857 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 63f27463-df1b-3033-9ffd-03cb5c4a929f | -2.86799 | -51.48549 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f1c44539-f8a7-3fbd-9b71-0457b05420a4 | -2.6215 | -51.31009 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b197f81d-9cfc-3fae-a5f2-b47fbd86ee5b | -2.46528 | -48.45253 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d355fc1b-4fe0-3385-bd39-9aea8cb8e551 | -4.24633 | -47.57772 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 281.5 |
| 5c53d0c8-5c20-3f36-894e-3804986d8bd5 | -6.16259 | -43.58777 | 2024-11-09 00:39:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af4c61d8-0acd-3be8-92da-98be85d34ba1 | -3.75526 | -44.56418 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fb198e0b-0c14-3c85-9524-849fccba8388 | -4.94505 | -45.56324 | 2024-11-09 00:39:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3578a93b-af92-3c12-bad3-ba957ecfc0e2 | -3.5936 | -47.37374 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5735000a-539f-30fe-9ae7-fe4db8f7608c | -2.30576 | -46.72423 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 286e7ab0-e0d7-3247-b8a6-79f80aad0b4a | -2.20455 | -46.79308 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 445166a5-ae5c-3751-9781-4aedc951648d | -3.27215 | -46.32168 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 4c4d6359-818c-3b14-a2a0-ed59f2d4b1c5 | -3.07432 | -45.0325 | 2024-11-09 00:39:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f7afc090-8e52-328a-b018-cdf701b88881 | -3.72135 | -41.69086 | 2024-11-09 00:39:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 7c48e7fb-3835-354d-8ecf-5182cd289221 | -3.09027 | -51.29461 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e3627c0a-65a0-37fd-81a2-e22fc089502c | -5.56172 | -46.29518 | 2024-11-09 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 13858883-e460-30b9-ada1-5181fdae2238 | -2.33925 | -46.57013 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6fdeee40-4f3f-326d-ac17-f17adbb9d5ef | -3.07147 | -45.40146 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd5db790-9086-36b8-8eb1-f4642d9c84f8 | -2.29438 | -48.54824 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| edc7816d-154c-3bf8-bf54-634c9349f2d0 | -3.06725 | -48.06901 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5889bea5-2556-37a9-8ec5-b82aa4574a12 | -6.18931 | -45.43928 | 2024-11-09 00:39:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1360f548-3450-3b2c-9d7c-0d165685272e | -2.28062 | -48.73998 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d0d7f5c8-7a5e-37fd-8c3c-8bf1d36307c2 | -2.49373 | -47.22953 | 2024-11-09 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| bf84f26f-8074-3db5-9950-b00b9425aa22 | -4.07877 | -49.28625 | 2024-11-09 00:39:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| cc5d07f3-0e4f-333f-a0f7-1c89331b0221 | -4.27481 | -43.66479 | 2024-11-09 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c3f6688-93ed-3640-8054-3ac2609984ae | -4.08139 | -43.98943 | 2024-11-09 00:39:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 206c305b-b04d-33eb-a6f4-b892311ada56 | -4.08066 | -49.30037 | 2024-11-09 00:39:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6070e258-531e-39b4-8e0f-a6bbc9e6cdde | -2.80023 | -45.97356 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4dad84d-3ff4-3e8f-99e2-7fe3668883d3 | -6.23958 | -47.2831 | 2024-11-09 00:39:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4b9099d6-9bec-3168-8383-1b7ac9101ffb | -2.98665 | -50.30311 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 358a70eb-f368-39b7-b8a1-4b1ca591cc26 | -6.27586 | -44.73533 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6051e410-6630-3446-8470-6b87eb5badf2 | -2.08499 | -46.529 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5f186954-2a11-303d-a25b-2636121f2ed6 | -3.53922 | -50.32594 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f15c466b-1735-34e1-bb1d-f728af8297a2 | -3.76518 | -51.75283 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 5f20e93a-f845-367a-9770-5703b69f5ba6 | -5.45022 | -44.82598 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 444037a6-47d7-3953-b072-3553ec6674cc | -4.11845 | -48.50299 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4b516ba6-0507-3e02-8a41-fd0e4cd248f9 | -2.87923 | -51.4774 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| bc99fcd3-9c8c-355e-91df-b49f33398fa6 | -4.89623 | -48.61475 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6c3c27b2-689d-3ae2-9269-eb300ebac279 | -3.98446 | -46.41277 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f7f657ef-00a5-32b1-bfe2-6ed1a97a054b | -4.01696 | -46.18161 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d14ed097-38f2-3dd2-a085-9cfb0cefb5c1 | -5.11688 | -47.14504 | 2024-11-09 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 232aecba-c10f-3319-a9c8-bb49c72aa34e | -5.84229 | -39.63286 | 2024-11-09 00:39:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| dc0b5804-fb4c-3957-84d7-ff8c74f8da70 | -3.56093 | -43.56736 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e87336ed-16d7-372b-9596-d9c3277c6bb3 | -3.13565 | -52.97638 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 878c426e-afe5-3b2d-bd8c-0b1d6901e7e6 | -2.08709 | -46.34461 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08a701b1-81f1-3269-9b60-ec923b771488 | -3.16371 | -54.48278 | 2024-11-09 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 21d5c623-2263-378a-b48e-2065c1fe6a09 | -3.6037 | -47.34469 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 454db3e2-13fc-38cd-b143-212babd2e8e2 | -6.536 | -44.47498 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c42981ab-f4eb-3a21-8367-adb134a76b44 | -4.25462 | -47.56554 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 23261d16-ff60-314b-9ee6-22e7dd0d331d | -2.63779 | -46.79892 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f248a467-8392-33d1-8579-1d4a0e92dd9e | -3.34308 | -50.37033 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7032af68-7f2b-3d44-879b-b76dc1c3a67b | -3.58893 | -45.61532 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f0d59b0b-89fc-31ec-bb07-75579c3f2299 | -2.42646 | -46.13335 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f5d0d9ab-8ffb-3c6d-859e-fa9d71cadb88 | -2.91846 | -49.36696 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ed27b92c-6d2e-3671-990a-a09756165273 | -3.4109 | -50.02514 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f80e3cb7-2856-3239-8772-37ef739c2f8d | -5.17914 | -43.99586 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06bc96f7-a062-3ac8-8fb3-c51a77161c62 | -5.74136 | -49.11423 | 2024-11-09 00:39:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 29aaefc1-b6bc-33d6-a833-89c1310ef1c7 | -2.57773 | -49.13061 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0dbbc5c4-d68b-3ea9-8619-59a9c4d18229 | -3.74641 | -44.56544 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78959b2b-7ea1-3b23-89c8-a3b39214febe | -2.97497 | -47.91693 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9d9f478b-7fc4-3afb-aa8c-9e6bc7ab302b | -3.33604 | -50.08381 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| de8a8bc7-89c2-3400-942c-6b75c1e8c914 | -4.52159 | -45.69903 | 2024-11-09 00:39:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49dbec81-0fc8-35a0-9ebb-3d145acc39cf | -5.11544 | -47.13457 | 2024-11-09 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 16bb7d4f-e894-3a7c-bb2a-5cb82c397ce1 | -3.07309 | -45.0237 | 2024-11-09 00:39:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 65da22dc-fdfb-3595-9e7b-af571c39e286 | -2.61426 | -46.15961 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 126af75d-9ac3-3903-95cf-e98a8c90ac68 | -2.80113 | -46.64748 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef0987a0-0fbf-3b83-bd60-90b7cbbfdc9d | -2.11567 | -46.21991 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8f0596df-f741-34ad-bd1d-98e49ddb4224 | -4.93567 | -43.64122 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ee7f5b11-15fc-377c-882a-4e92dd9a3295 | -5.2754 | -45.08942 | 2024-11-09 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d03249b3-7634-3df5-be21-606d1fd29cd0 | -2.29092 | -48.73854 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9535b971-2d06-37ee-a673-d4196b460adb | -3.24742 | -46.47774 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59222d14-b724-30bb-b23c-f55d5bb3f0bf | -5.04028 | -46.79762 | 2024-11-09 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| f97dc0db-7d90-3082-baae-ee8ebc2f77b4 | -4.25612 | -47.57643 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| 1ac39520-4819-3ebe-b934-06c348ae4314 | -3.45321 | -45.4318 | 2024-11-09 00:39:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ce40e643-c906-311d-a745-b562b7f633b2 | -2.37953 | -46.59304 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0583189-924e-3ff6-98a1-62f3db2d024c | -3.73488 | -54.23158 | 2024-11-09 00:39:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b71eb068-e501-3886-a3e1-20ba84aa9a6d | -3.3595 | -50.26149 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d8c281be-f4ff-39f3-8caa-63bd5a804710 | -3.31138 | -45.67285 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 36bbff4a-51bd-3966-bbd4-ab0535090dfc | -2.15361 | -46.69427 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 408dc648-9775-3a4a-999e-18d41087256a | -2.89389 | -45.38455 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e738c4fa-fcb7-36cf-9760-fc92bcb1332b | -2.31167 | -46.04187 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 451f0fdc-9629-30c9-b7c1-d85be09bd54e | -5.34603 | -42.17852 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 229e357b-34a1-3adc-a5a2-beba30d01cc7 | -2.79992 | -48.28152 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 72aeacee-55b0-30e0-9cd1-1899fd83d6f0 | -2.03289 | -46.08995 | 2024-11-09 00:39:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| caeb2bbc-3152-3c0f-831a-793571163587 | -2.918 | -45.36314 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e62cf13-fb60-31da-a6ac-3bdede3f60e3 | -2.38755 | -46.78427 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6183f91b-b039-3b62-abd7-d0ad1514a69f | -4.38797 | -46.80836 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b30f2168-b8ab-343e-ac23-fd59441117a8 | -2.30954 | -46.48892 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 223aae2c-3a84-37bf-9ba9-43cd85771a35 | -2.91657 | -49.3532 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 039b985d-a570-37f7-a060-cff8c67aceb3 | -2.46528 | -48.44686 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README10.md)
