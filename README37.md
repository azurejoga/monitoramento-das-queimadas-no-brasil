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
| 6803ffcc-9b50-325b-adfa-bdff7f8a49f0 | -4.55076 | -45.72559 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdfcccfe-e729-3ad3-85b6-dd740904f11a | -4.20132 | -50.68893 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8b12e96-93c7-31b9-8c22-317f811986c9 | -8.13294 | -44.47972 | 2024-12-01 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af666569-c10f-347b-b5aa-31b30d35fb1c | -4.94318 | -49.93392 | 2024-12-01 04:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 195bc1bb-e90b-3595-ba89-5c8e2a505bf7 | -3.74405 | -52.26365 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1724e30f-6e13-32e7-9a26-f340e35f9a12 | -11.39946 | -43.14579 | 2024-12-01 04:23:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba96ea63-88b6-3f19-9e55-aa92274f6e1a | -3.31511 | -53.86115 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4c26d3a-8d7c-3e17-a66f-baed80b7aced | -10.65641 | -44.48692 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9844e1c-3792-3a66-9802-2613f5e73d1a | -5.79986 | -47.07836 | 2024-12-01 04:23:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b263915d-21a4-362e-97a7-1baaec647a68 | -6.63787 | -47.34977 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29d6c392-dc78-3ddd-8598-3f34f6310b74 | -5.83596 | -42.9874 | 2024-12-01 04:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7c3d3bbd-ac96-3cb7-82bc-ad225a40bef0 | -4.38705 | -47.22849 | 2024-12-01 04:23:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3635ab5b-6476-3409-9865-91bf21cb0aa0 | -7.54993 | -46.87112 | 2024-12-01 04:23:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 668060f8-842c-3fd4-91cd-477230d52a3b | -3.6963 | -51.80827 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1daf298-7831-3ee0-b227-98a5976af117 | -5.41917 | -46.11078 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62a86a68-7692-36fe-9ada-713d988c9d64 | -3.25079 | -53.63819 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a94f9c87-0ad3-31dd-80ab-f1c0c5c5fc0b | -5.42312 | -45.11203 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f412d30e-ce97-3cef-811b-e8237ecbe5a9 | -4.56193 | -45.72003 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc48786d-e863-3993-8788-75d0e5be6b88 | -3.69545 | -51.81341 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d8f1376a-eb4f-37dd-9fbb-961db9c84e2c | -3.84254 | -52.02246 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06af8156-00cf-3953-9364-4242137b0692 | -8.74 | -47.02706 | 2024-12-01 04:23:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 911d9862-27c7-3e2f-9f75-53066532ae45 | -3.30331 | -53.82806 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f810a01-826e-307a-96d8-bc6cb9932a0a | -3.25252 | -53.62799 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27271335-b780-33ef-9411-eb649011b70a | -4.06785 | -51.06503 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde9f889-ac7c-356e-8918-70ce2c56d9fd | -4.00902 | -54.6198 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a675581f-ee44-37a2-9053-6da49695bac7 | -10.45421 | -44.94352 | 2024-12-01 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92bccee8-da6c-37ec-846f-9d38b2bd5c84 | -6.91809 | -43.54233 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08d84129-ce26-351b-828e-606740610cd2 | -4.70366 | -46.55262 | 2024-12-01 04:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c088aa90-66f0-38f8-82ae-f7cb36f02594 | -6.76127 | -46.5289 | 2024-12-01 04:23:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2af9c9e0-84bb-36d8-ba19-d5821d0c9548 | -3.49532 | -53.79814 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a63ecff1-d67e-3f89-84f5-b7e4fd8894a7 | -3.3333 | -53.54324 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d46802f4-58cb-39ea-953a-9bedeca237be | -3.30273 | -53.83164 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81abe03a-a368-33b8-9d5c-76d8cf1cc169 | -5.25211 | -49.9388 | 2024-12-01 04:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04d0ca56-13d4-3856-af7a-352f26b49bca | -6.92547 | -43.55039 | 2024-12-01 04:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 258ed25b-9750-32a4-9252-ff8e895a86e7 | -5.89344 | -48.27533 | 2024-12-01 04:23:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3da062a6-ccca-3bbb-955e-8840e83cb648 | -8.93577 | -44.25193 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdc4fb95-9ee0-3503-902e-b1e8450f4c56 | -3.50565 | -53.83761 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8a5e0b25-526a-3c62-b599-f7103581defd | -3.33921 | -53.37433 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6acfe4f0-bf8a-3f1b-b1b7-3dc407b52456 | -3.29605 | -53.83794 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3144aed1-8d19-38fb-91a8-78ba37d46eaa | -3.75784 | -52.27173 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 576ca5cf-813c-3321-8a77-5a3490da3a98 | -4.56473 | -45.72406 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88a43ea0-bea5-365d-a127-7b6e8fa6f5b3 | -6.05461 | -46.58155 | 2024-12-01 04:23:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c69db9f5-ae9d-3fb7-ba06-492096113a96 | -4.56082 | -45.72709 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f12fcb4-d328-3ead-b4aa-24c717c180d4 | -3.46426 | -53.88309 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8323885e-1e3f-32e2-b6d4-a99fd85fd3fa | -3.42939 | -53.88877 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43cfbda2-5dbd-35b4-9059-64255a964ff6 | -3.26823 | -53.63395 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b1d226eb-40d9-3ed9-bd8d-3bc25ba11921 | -6.06535 | -44.15435 | 2024-12-01 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c361ed9-75f1-3252-942c-951533728a9b | -4.39976 | -50.69254 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44910129-5891-3b47-83b6-43ded67976fd | -7.38475 | -45.83268 | 2024-12-01 04:23:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b504072e-bca3-3da0-acc9-7b5d5309bce0 | -3.48194 | -53.81102 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d659e53-c8e2-3bb2-b2ec-52af8f6a2f5c | -10.6654 | -44.49576 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8f4436b1-0ebc-3ed9-8d3e-98d8f0e3b789 | -3.22323 | -54.17585 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78c7a01b-f411-376d-a048-2ff4ac7c8ef4 | -3.31394 | -53.86675 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5b7cd40b-1b23-3c76-b79f-f2c219b855b2 | -3.77276 | -51.62125 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d71e988a-a5c4-3894-99b2-082ce4aeaba0 | -8.13348 | -44.4762 | 2024-12-01 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef8dd987-5ad1-3e37-9aab-1a0f7513d13a | -3.30822 | -53.83253 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177262eb-e233-3e27-8a01-12401af7bb1d | -10.6553 | -44.49419 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bcdb3e5f-62dc-3479-bc47-fcb2ceb86664 | -3.5008 | -53.79896 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eb52a1a-5035-38b5-abcc-7736ccf54f94 | -3.69459 | -51.8186 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 05383979-039d-3a6c-a461-ac6cfe7e7848 | -8.83986 | -44.76691 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3783ad64-65f3-3547-a934-9e11c5fcac5d | -4.85909 | -44.23534 | 2024-12-01 04:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f16994eb-5460-3c51-90bd-e50c81e22f48 | -8.93297 | -44.24783 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3679d687-f150-383b-8f5f-cc81a7da135b | -4.55802 | -45.72306 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b26535b8-d55a-38ad-89cd-c814166c007f | -4.10679 | -50.98387 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7812779-f9d5-3867-bc5f-3c84780d47f8 | -3.24358 | -53.64782 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3341c0d-7c86-3456-afc5-fe65acd4dca9 | -10.65812 | -44.49835 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9bb54080-be22-3e2c-90aa-554c395b4d21 | -8.8404 | -44.7634 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d37c2334-6396-3b29-ba66-9cff1b0d4211 | -3.77568 | -51.6194 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c52271a-fa8d-38dc-8a15-6639d5cddc7b | -3.33274 | -53.54664 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fb05556-d690-3dcb-a2f7-04ccdde587f8 | -4.31848 | -48.08897 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f435d4f-6d52-3ffe-9e1d-8bb04797d0b0 | -3.25564 | -53.64251 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec5fe3db-041a-3850-863b-7a52e20af33d | -3.74899 | -52.2643 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04527774-ff7a-3ed8-a90e-c32fa8e6ba5d | -15.07958 | -48.94543 | 2024-12-01 04:23:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8bd4306-26d3-346a-b3ef-d0243c525115 | -5.31026 | -50.57022 | 2024-12-01 04:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b3e7b1c-bd72-30a6-95cf-47ea81967c67 | -4.10949 | -48.88766 | 2024-12-01 04:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 44298ba3-3ef1-3a40-8685-c0bcffc4c777 | -3.25623 | -53.63901 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e8d2cd5-19e0-3664-b860-8423840fdaaa | -10.5324 | -42.52825 | 2024-12-01 04:23:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c4db3682-8494-3dd6-9327-fd95a98cf8eb | -3.29664 | -53.83435 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4546b638-d7e2-3b43-9ac2-792867be51fd | -3.26048 | -53.64686 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5d67096-8be7-31aa-b9e7-3f0cd9ba784a | -3.25368 | -53.6211 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 047f4be7-8eb1-3edd-a546-62dc93b76785 | -6.82552 | -39.38954 | 2024-12-01 04:23:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bafc1336-a9e9-3e00-aee7-f13c8405ed0d | -4.40942 | -50.82424 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04942a32-6d1c-3596-98ed-b2cbfa97b64d | -4.32147 | -48.09395 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bb7a85c-d199-3626-a1d4-93c7aa24a7ff | -4.47243 | -50.76888 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca658440-7d33-35ed-8d9a-4bff6a5cbc50 | -3.68899 | -51.8229 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3e1769e4-68bf-31c0-8004-4916f4c82cc8 | -3.30899 | -53.86386 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 71b67c30-860f-3f0c-822a-bb15632391ee | -3.5002 | -53.83655 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 993ab0c9-38d5-3f19-83ab-587672e77d32 | -4.0755 | -50.0299 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b8926d8-8284-3c6f-843c-e650bfd7ade8 | -3.71975 | -51.15077 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04238af8-48ce-394d-9a24-0e7064025cce | -4.55858 | -45.71952 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 92c17a04-e115-31f6-8492-6c24338a5ef3 | -3.94546 | -51.09443 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e15268fc-bdfd-35bc-9d4b-d29423ba0f03 | -5.97168 | -44.77767 | 2024-12-01 04:23:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e5f49d8-2ea8-3a35-99f7-edd5bc3506b2 | -4.17605 | -51.23681 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6c77b1f-b030-3440-97ab-2841c4dd95bd | -4.31778 | -48.09336 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b470026-fe8b-340a-8af3-dae28f9fe8de | -3.49412 | -53.83924 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 081d7ea0-d9d4-3b3f-aad7-74ba674e1dca | -5.35132 | -44.08935 | 2024-12-01 04:23:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0519b7be-a11a-353a-9550-754cf9512b58 | -4.5502 | -45.72912 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f3d999d-b4ab-3b1e-87bb-f0856bfeb02e | -4.33767 | -50.76601 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7183be3-8a17-3e62-9232-a22bffaff546 | -3.25311 | -53.62452 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 343e363c-7ae8-371d-9b03-5c94af21658a | -3.12868 | -54.53194 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |


[Clique aqui para ver as próximas entradas](README38.md)
