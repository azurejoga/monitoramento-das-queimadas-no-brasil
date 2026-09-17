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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dbc2dff-3556-3a74-ab58-521f7bfcfe1b | -9.60344 | -45.3459 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eda4772d-0300-351b-85fd-7544945e44c4 | -8.8677 | -44.91069 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3b3fc69-01a2-3351-9e9d-7ff87bb503c9 | -7.03216 | -42.0724 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 852db975-719d-3b34-9e40-9db953dc9772 | -8.56221 | -44.50847 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9efa40c-ec7a-39eb-9e9f-fb4146d1359b | -5.28939 | -43.63751 | 2026-09-17 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9db0a23d-c014-3fb6-974d-c62ddf7d8cf1 | -7.12776 | -42.16225 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| afb0cf42-e25c-3a75-955e-503872882a80 | -7.11248 | -43.10072 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b25f6f0a-5dd8-3e28-82f7-e00d8410aa72 | -11.59032 | -46.87748 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dab24a2-9b1f-32c3-bf0b-d515a7f6eccf | -9.10688 | -45.72814 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0a64291f-cd6d-34f1-be77-ef0bf050d3c7 | -9.1233 | -45.73209 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8450c637-6012-356c-8599-fee7b63d5da7 | -11.33085 | -47.65295 | 2026-09-17 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 212a5a57-a272-3c49-af28-6691eb8cd37e | -10.83631 | -46.16812 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88eee9c6-b8e6-3f3a-bd97-55d69848a02b | -7.08202 | -41.77554 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c577fcd-0f88-3698-bc38-3969255ffe19 | -9.11234 | -45.72536 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 0266bdb1-4ed8-38ab-a2c8-64e8d382a76e | -4.51586 | -54.96889 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b82a2fa9-c9b8-32be-b085-f8f42d459bde | -11.56276 | -46.88298 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c529b6fc-f5d3-3f62-8ab2-ebdd8b60e520 | -5.83771 | -52.11543 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b910f5e-e6ae-301b-ad1b-2b8685e8f13b | -8.54154 | -47.24953 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 313fd085-b87f-3d90-8381-dadf24193a8e | -7.64965 | -44.32847 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66e2a850-446b-3a62-ac51-604a5a96e1b4 | -9.87445 | -48.35819 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9eef0a29-055d-3771-ba16-bd85e3af6dda | -10.86237 | -54.04315 | 2026-09-17 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65dd3ee6-0ecf-3e62-91a0-71c265c9566e | -7.46291 | -46.83654 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8184c381-2a96-365a-b488-23be05cfca1f | -9.96497 | -45.32495 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 380fd3a3-d2c1-3a0c-a049-afcf7e3c2008 | -10.10286 | -45.62551 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 726c3d0d-0b69-3261-bc56-93981ae3747d | -6.12992 | -43.74544 | 2026-09-17 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5750307c-a00c-35e7-b36b-4f599d968fc5 | -8.25452 | -42.17375 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0f36bee1-153e-324b-816f-7d30ac0abfbb | -11.48372 | -45.78184 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68403259-fdf7-3968-b6f9-9c67597cb3f1 | -8.47849 | -44.89951 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 937149e8-6fea-3620-94a6-75ffdb867585 | -9.90992 | -46.51141 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4f3cbc2b-c7c2-31b0-be7a-4403bb12322a | -7.6388 | -44.40416 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 447fb0a1-5719-378a-8e12-4465c3c6ffbe | -4.54358 | -54.93283 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d18220dc-0e4d-3098-b2fd-3d85be741759 | -6.96037 | -42.57917 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5de2a5f-88a4-3954-9f11-11855308d762 | -10.1859 | -48.50081 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b385378-c407-3960-842a-2a37d58e11c5 | -5.86496 | -52.06358 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 813d87a4-01ce-3743-a40e-8402b20410a8 | -4.14122 | -54.41512 | 2026-09-17 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b2924f3-d0f9-3dc5-9f48-60daa4fbb444 | -9.56217 | -46.59061 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcca8f82-f194-3e6a-9a72-571e4f049a4b | -8.55911 | -44.50016 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdf48f6a-3300-3b7c-b884-d6eef08ff57f | -6.35432 | -51.77718 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11e2a177-d8aa-3570-8487-d144e8d72027 | -4.56845 | -54.91326 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4340ef2d-d0a2-355f-b450-91cc7dbc8dd0 | -10.83768 | -46.1584 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5cec4bb-eb21-3c28-a7fc-474e4ff42f0a | -7.60241 | -46.32143 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f92860bc-664c-355b-a55c-2476f4719c5a | -5.67521 | -51.93496 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a487d982-f710-3ea0-8f63-05eadce27ec9 | -9.559 | -45.42793 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40dbaea2-ab6a-3636-ac9f-60479f6f9d97 | -5.64472 | -44.80378 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 0c25da8b-b278-3cb4-a889-288569424e3f | -6.1686 | -44.61888 | 2026-09-17 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b2a00f4-2542-3562-b54c-39644a7dcfdc | -11.54778 | -46.88071 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd2fd1a1-3937-3429-be82-dbf051b53274 | -10.40328 | -48.66298 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3fc54b6-5a43-3f8a-a2b0-6e12bbb7705a | -10.40271 | -48.66669 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 261a0591-8716-36db-bb44-087d19ac6ca0 | -7.1104 | -43.09904 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a7a322b-48b8-361a-bbc6-8f9db9489062 | -5.86152 | -51.94316 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c8ac0f4-02f4-384d-b99a-b0662b46a145 | -9.60161 | -45.34229 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03b4cf5f-7e48-399a-b177-9566a68ac8a4 | -5.46194 | -44.9563 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44eec53c-91c0-371e-a3fb-35e144064c15 | -6.96108 | -42.57422 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5f073e4d-7acb-3479-a7fd-f78edade3898 | -11.9236 | -48.2555 | 2026-09-17 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b1a51a4-35d4-3fed-8419-f3f20ae373f5 | -8.69469 | -44.87077 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c077038d-9ca6-3b62-b662-3e211de2ccc0 | -9.46856 | -45.44654 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 28a38385-8b9a-3513-b575-4c98c363e67a | -7.1369 | -42.16455 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8bb94da4-3fbd-3a90-bd80-42a4204f026e | -10.52623 | -57.45038 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 624d089b-48d9-354d-a277-7c7c9b79806f | -5.6201 | -45.24921 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56a8b1db-6878-3df5-9f6b-245904100344 | -5.61771 | -45.24609 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c616fcf9-ddcc-35a4-862f-cd9bb4bb825a | -6.65667 | -50.91692 | 2026-09-17 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5eaa5c69-1ccb-3d45-86fd-52028d9f9b96 | -4.39495 | -55.44153 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0680d7ef-7fac-3224-a1d3-8fd09b41a849 | -8.5774 | -44.58208 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 813bb99a-9cb2-364c-af52-90ca8ecda92b | -11.22386 | -43.45429 | 2026-09-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f507f568-37ef-3c2a-9e9f-c23b1835363a | -6.45794 | -52.83818 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be00224b-e1fe-3771-a9db-c4f68901c439 | -9.86469 | -48.35301 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce7fb330-6135-38cc-a47f-ffc841705d6a | -10.14848 | -45.67543 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dee0f02-d7a9-3050-9e19-452ce476ac4a | -4.5152 | -54.97282 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc353a17-62af-3014-b6ce-6c5dc8a139a2 | -6.44911 | -46.52824 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b68c58a4-f733-3270-929e-6e19f1b6cc33 | -3.81202 | -55.89054 | 2026-09-17 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19f290a9-03d7-3a3d-92a2-59af474fe427 | -7.03789 | -42.07151 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 341f8ff1-c073-36e9-9102-a086ac82cb2a | -10.39573 | -46.63264 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59b63a12-a450-31ab-97e1-ea1a07bfaf24 | -4.24355 | -54.88277 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86bfd8f3-6c8b-3beb-b8a0-920e922dc29e | -5.77398 | -45.09908 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 79f92869-ad61-3adb-92d7-354e62330ec3 | -7.28438 | -46.74984 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bc2a9b3-8e50-3e18-8822-1376a146c520 | -7.5805 | -44.9224 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb232d24-30f3-3484-8f92-dcd8481c6d7a | -6.76107 | -55.84378 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89f55d1f-184a-3efa-8197-d1f415a8ec66 | -7.44312 | -44.57703 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9ba0c99-cafb-3031-992b-db34f0aa2b11 | -7.65019 | -44.32469 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 915372ec-a0af-3a68-85b9-e2576849fee8 | -6.04095 | -44.03329 | 2026-09-17 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8d77fab2-ec01-3d2b-a6e6-04b1c6bf0efc | -9.87844 | -48.35498 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7711c3e-2d73-3c54-9aab-22a3150f6be7 | -5.90961 | -52.09862 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e781d7be-f93b-335c-b3e0-df12c8359751 | -9.40697 | -62.71642 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 99548cf7-6326-3c3d-a9f4-3f453fc42d64 | -11.56213 | -46.88754 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a2fb735-1ad2-3785-a268-6919aff18386 | -10.40041 | -58.30413 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37e06fd9-b1f1-35c4-a60a-c9182f29f843 | -9.50074 | -45.43735 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3c9d025-d8f3-359c-868f-f801ecd66b51 | -9.62279 | -45.36664 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 21b266b8-1b21-388a-a2f7-111f98a29c89 | -10.41403 | -48.63807 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ec5ddc0-1574-32e3-b336-76a797fcbe56 | -5.76488 | -45.10735 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5ec84fe2-d2f3-3c9e-9daf-89448505ff63 | -4.87734 | -56.06395 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 329085b8-4743-38a1-a130-3ff1be0d5bc6 | -10.02661 | -45.71598 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 565e39c3-676d-3cf0-9100-4d2a09287352 | -7.17296 | -42.11594 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca2f8d91-2ff0-3d50-a17b-cedb77ef656b | -6.83506 | -46.0447 | 2026-09-17 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e5f0c28-b064-341a-bba6-5033d555bc28 | -7.94348 | -44.83344 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b1d8787b-e192-3a9f-98f7-3543f65d496d | -7.06571 | -63.05147 | 2026-09-17 04:40:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02378fce-834d-317e-a622-5971aafd003a | -8.42352 | -47.75139 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68d7e89e-ff07-31f2-aed6-a0f6dcd8de39 | -10.81282 | -50.83897 | 2026-09-17 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 387b9496-b254-324d-9105-3bdc8be481f4 | -11.32593 | -46.77582 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9834c2c8-e53a-3020-95c6-cc52a52588bc | -7.36906 | -44.48473 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36445c93-0e8c-3210-be44-fddc761f0dbd | -5.80814 | -43.72846 | 2026-09-17 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README39.md)
