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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cb20aac-1c2d-3d59-aae5-0f77abf50d63 | -6.29764 | -41.9161 | 2025-11-26 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| fd126f5d-1484-308b-ba64-2c527cca5af4 | -4.18513 | -43.73563 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8babdb5e-e509-33c3-b816-6c09be282a53 | -4.41644 | -45.1164 | 2025-11-26 00:13:00 | TERRA_M-M | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a38758ad-3a73-3c10-9e5d-fc0096367a45 | -3.47544 | -43.4198 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| b2f8eec3-b78f-3a18-970a-975cb1812402 | -3.47849 | -43.44091 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 771b8fbb-0c68-32c0-8954-12fbbce69c5d | -4.92867 | -49.15367 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 84cee40d-3d71-3f4f-8967-cdae3a31dfc2 | -4.40078 | -45.26409 | 2025-11-26 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3afb00ee-de79-3342-84e6-fbdcddf177c5 | -2.47694 | -45.40916 | 2025-11-26 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 172.9 |
| cd107217-419b-3cd6-b865-f0b5d9b97120 | -2.24705 | -45.67833 | 2025-11-26 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| bc4fdbdf-d1a2-334e-bd08-a4e5187fad04 | -3.68132 | -43.5694 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 445f6669-b28f-3022-a8e8-c9253d3fb399 | -3.23639 | -50.59457 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1e2f0752-15b8-39e4-8ec1-cadf2722ce64 | -6.59052 | -44.32135 | 2025-11-26 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fce01579-73a2-360a-850d-5e041d28abae | -7.26621 | -42.53214 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e04f6195-daf6-3002-8d63-5cae03734968 | -3.39695 | -49.22929 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3f6dedb2-994a-39cf-bb2e-27a53dd9e237 | -6.56754 | -47.90199 | 2025-11-26 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ec76e843-5b74-3d30-b70e-e511228717ca | -3.31958 | -50.44995 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d81b77e1-5262-348e-9113-005b832fbe84 | -5.38966 | -46.76135 | 2025-11-26 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 978693a7-31aa-36bc-b31a-de4d727dc8c7 | -4.17576 | -43.73695 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 266.5 |
| 571e6491-585a-3a8d-8c89-b300938f93fe | -3.32846 | -49.71276 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2a848506-0f88-3971-a152-15dbaf827aea | -4.10122 | -49.07288 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 9e7e172e-824a-34e1-9abe-5055d42256e9 | -2.87791 | -45.85052 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0efc2332-80aa-31e7-af51-94f670b00db4 | -6.35522 | -41.40991 | 2025-11-26 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 16e11baf-61db-3d89-b148-f7faf45cff44 | -8.03504 | -43.13015 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 18e7c3a1-edb4-39b8-8957-2f6f50e05b61 | -2.93928 | -48.22125 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e09ee51d-9cf3-3fbd-bbed-8d9500cfdfb1 | -3.25543 | -51.16381 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 481bef3d-b273-31ef-8a44-89e93a44a363 | -4.86355 | -43.05157 | 2025-11-26 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 247a05ef-c060-3251-828d-d3738a6f40a6 | -3.04937 | -45.82316 | 2025-11-26 00:13:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 87e1865d-bb3d-311c-b27d-468c656cb395 | -2.96851 | -45.50071 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5292b8ff-6d32-3387-8b16-db156aaa8343 | -2.96066 | -45.57428 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bf013122-e46f-32b5-970f-e60c3912981b | -4.86771 | -49.00148 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e106ccca-3f19-337f-b827-b75ea820d115 | -5.70746 | -47.26891 | 2025-11-26 00:13:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7b796046-8812-3394-9bc0-e74d56aeba98 | -2.93132 | -48.23243 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 0f6c77e6-7e3a-39f6-8667-72a9cf7755f3 | -2.85665 | -46.82048 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55574cf9-872d-35aa-bc61-eda37799ea41 | -5.43161 | -45.85907 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cbb8847-9e04-3e37-bad3-51b2959ed0b0 | -4.5908 | -45.70878 | 2025-11-26 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| e4a247d5-b2bd-3562-a6ad-f89bcc2f4359 | -4.23536 | -40.38534 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1b0b6375-4f4b-3783-8cba-485ea67cab99 | -5.28747 | -43.64489 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 0066ab01-5d3a-3c70-8e9a-8821116674e5 | -4.69393 | -45.05872 | 2025-11-26 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f36de75-8187-3fb1-bd36-29d8d0759a16 | -3.36396 | -49.512 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 89f65e09-33e3-3396-afa7-c9449322e392 | -6.76551 | -46.51877 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| cc73517c-a639-36b8-ae5b-541997c605f1 | -4.15992 | -43.73494 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 92ff4304-f583-37dd-9d46-4d84a5c9464b | -5.71398 | -39.49672 | 2025-11-26 00:13:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| f3d9bde5-56d4-3719-a11e-d5862d5564c1 | -3.20574 | -50.21152 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| b8d6e5a2-9c4c-31fe-b875-3d0ea2e0faf5 | -3.04389 | -45.11808 | 2025-11-26 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5b2997df-7ab2-31ba-a10d-723d6f9f542e | -7.75225 | -44.19536 | 2025-11-26 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f6bc4f75-0505-3965-87e9-463262559030 | -4.56006 | -43.30332 | 2025-11-26 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c56fd653-ba94-39fc-bdff-8fe19eb6fa2f | -4.2848 | -45.36515 | 2025-11-26 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5d1dbb82-2ad2-31d1-a92b-b16f1c3b6350 | -2.90197 | -45.48886 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6d88a0c-286d-3794-9217-a364f683b55d | -7.51323 | -44.07087 | 2025-11-26 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3afdd73-abdd-36b6-95df-b07e931fc9a5 | -8.05952 | -43.12013 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| cef68a02-8700-30eb-a508-ec3a2c4f2e6b | -4.5586 | -43.29285 | 2025-11-26 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 237c58c7-4a46-3e09-bf21-e54e0e333f43 | -3.43522 | -44.2278 | 2025-11-26 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc82a0c5-24cd-3d48-bdc1-a2a96e9387b1 | -3.93511 | -47.63546 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db018290-04cd-3744-885a-4b0eab061734 | -4.25912 | -45.11445 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 634594e0-537b-37f3-8b1b-a8e7c2c60124 | -4.56339 | -43.29636 | 2025-11-26 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8e9aca31-3f03-3b52-a099-b069ec31a48b | -3.51571 | -43.69942 | 2025-11-26 00:13:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6c1a310d-2b57-3d49-92dd-e035152942a4 | -3.72008 | -43.22012 | 2025-11-26 00:13:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a37c11a5-6f45-334c-b73f-17fe9ee16773 | -3.33687 | -44.04964 | 2025-11-26 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d8e95484-863a-3436-9e10-4fc0b5d90945 | -3.77518 | -47.14217 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6af06c05-e9f8-3cef-a22b-97aca9429d5e | -4.21989 | -48.37106 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a650d408-b11f-3fed-8bb5-07e893df373b | -4.08033 | -45.73953 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4540f50-15c0-3492-b29a-7dc6d628b9cf | -4.97163 | -50.88227 | 2025-11-26 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| c1e01be4-5b59-3ab9-b034-a76b976bc541 | -4.08451 | -43.92374 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83debec9-e00b-36d7-a934-d2e4c1ba59ad | -2.36299 | -45.71909 | 2025-11-26 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0138f96d-86e8-355c-92a8-5fe22f322b8a | -4.26036 | -45.1234 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a2c757e1-1f0e-3cb4-b9a6-e9ff9b04d1fb | -2.7555 | -47.76277 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7c67a8a-c6a9-3105-b609-069dc99d9055 | -3.32312 | -49.73167 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f716a014-7ec1-3e00-aa36-32960ec0bb61 | -4.16638 | -43.73829 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a490c365-19e7-34d6-a93f-613ebab67982 | -3.32143 | -49.71944 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 23811757-a6ab-3158-9185-07ce4aa13d67 | -4.31237 | -50.74635 | 2025-11-26 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f20de1b-0447-3fd9-a2d1-52f9e294eefd | -4.04512 | -48.89312 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 64ff94b0-17b9-34f9-94c4-42132e7ecfd4 | -3.48452 | -44.51178 | 2025-11-26 00:13:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bcfc7787-6431-3f1c-9c4a-0afd8d5a0c18 | -4.58194 | -44.45314 | 2025-11-26 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fd3dda28-d653-3ebf-8f2f-e49083d430a8 | -7.74203 | -44.1876 | 2025-11-26 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 088d0cda-b171-3fce-b5f3-a3f148cf4cc4 | -4.41383 | -42.91481 | 2025-11-26 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e5bdf8d7-dab0-3e8c-88e8-ddca1f10ec4b | -2.8674 | -43.77869 | 2025-11-26 00:13:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bdfa4736-7e83-3a87-b9fa-5bc2adb6168a | -4.27382 | -50.54737 | 2025-11-26 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8ece41f0-9631-35d6-a02f-060898e01e65 | -7.92859 | -41.60316 | 2025-11-26 00:13:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 2ec76808-2c7d-3742-a136-27427b484e49 | -5.64069 | -43.92101 | 2025-11-26 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55ba090e-700e-38a9-9ffc-a15ee5c61c38 | -3.73336 | -43.45606 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef2a8ea6-76f2-3664-a014-4a51b4b104e2 | -5.27676 | -43.63641 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ef1237d5-b0e7-3f88-865e-66752a4c2e04 | -5.26406 | -49.77402 | 2025-11-26 00:13:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1537346c-ad83-355f-9771-ae6c035cfa7c | -4.16782 | -43.74826 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a546f38-980a-38af-aadb-890355b74b32 | -2.93437 | -49.35827 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a0f5505f-ccef-3d76-807b-c29ca2be4045 | -3.34688 | -49.77249 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 40e09dde-8910-37a1-837a-d5f6c644779f | -4.59616 | -44.42276 | 2025-11-26 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffe01ed2-3803-333f-86f0-f4236d2f6ea8 | -2.4194 | -48.59484 | 2025-11-26 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| c0277c71-f39b-39b4-8822-8b4fc5b67091 | -4.13768 | -42.55103 | 2025-11-26 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 554bd9d1-f960-390d-b61a-c5ea95d915b1 | -3.26902 | -51.17788 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d05873a5-4fcf-324a-811d-678d1b34c4c2 | -5.75921 | -46.42981 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 85c15bb2-8028-3da5-9d03-61c947709349 | -4.5347 | -45.56393 | 2025-11-26 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ea09f48-2e8f-3763-9df4-e84b7ab7670e | -6.59949 | -44.32007 | 2025-11-26 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2293f3cc-d91f-30c1-9935-6ee2a2b3b459 | -2.875 | -51.80036 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7178030f-bb04-3664-8df8-7f091a3aef34 | -3.67605 | -43.56595 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| a726d057-e8ad-3bda-add6-d80842d2c8a0 | -2.857 | -45.2304 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| ea6a0934-7b1a-3d57-ad97-247f1df8c640 | -4.25482 | -40.10175 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ee6a547c-b27b-377e-8a4f-b6970ff1c3a2 | -4.08588 | -43.9336 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a51758e7-4a65-3cf7-bd5b-a57f6c0b1578 | -6.47092 | -43.54316 | 2025-11-26 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1d7f54f-46ec-35cf-a980-35fcd5776354 | -5.57337 | -46.28512 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ec43697b-0a2c-3266-87ab-d6122b45e7ab | -8.03643 | -43.13999 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |


[Clique aqui para ver as próximas entradas](README3.md)
