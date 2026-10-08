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

## Dados Diários - Página 216

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd46ffda-299b-3426-bdf2-8d4c3d9c4c32 | 3.128 | -60.613 | 2026-10-08 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e5c8b52e-01d6-3e94-82e9-6c102b45f2fe | -1.3277 | -55.4327 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| fa5cc36c-b3bc-3d60-b78b-708b0aa398e9 | -1.5306 | -54.5558 | 2026-10-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c626d3b1-f219-3e29-bc35-ffb3189fd251 | -7.0066 | -59.1029 | 2026-10-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| ad419a57-f35a-30d1-8215-4fad788dd3ad | -7.0065 | -59.1223 | 2026-10-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 364.3 |
| e97a3d76-e2a9-337e-bf80-a9428a716e06 | -7.2082 | -44.2794 | 2026-10-08 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 7818a201-b377-3f8c-826e-cb552c38168e | -1.494 | -54.5363 | 2026-10-08 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| c87cd1ad-f9ac-3728-82bd-56a7af2a1e76 | -15.5216 | -42.6588 | 2026-10-08 14:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 148.5 |
| 5dfdf802-c18c-3c07-b54f-517a6c434b0b | -6.4568 | -55.4609 | 2026-10-08 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a739af22-567a-3f98-bf4f-d402d22e0634 | -11.3176 | -46.6798 | 2026-10-08 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 51fe327c-a5a1-3d27-9624-257848917e84 | -7.3054 | -43.9931 | 2026-10-08 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8173a5df-71e1-3ddf-b73b-02d1fd60a6a4 | -11.7935 | -43.5215 | 2026-10-08 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 63759448-dba6-3b43-b524-dce62728eb26 | -1.5306 | -54.5359 | 2026-10-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 303bfee1-7494-3123-84bf-445ce90b9ab4 | 3.1463 | -60.6127 | 2026-10-08 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8baadc11-b269-3516-a4f0-bde6c9b862d9 | -6.3283 | -55.3276 | 2026-10-08 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 273b8693-0a27-32b4-b679-777f0e94dd3d | -15.5743 | -44.5235 | 2026-10-08 14:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 48ea1dcc-7ad3-3aa0-9a24-c99bd7e8919c | -8.1807 | -46.3433 | 2026-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f10ebe13-4adb-3cfa-840f-8c938e08e047 | -1.3277 | -55.4525 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4afded2b-d4e9-39f7-9a6c-4e996595074c | -10.4334 | -47.3046 | 2026-10-08 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 514f5078-acf0-3fe0-85df-f428950baa13 | -3.86 | -44.1274 | 2026-10-08 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| f1cad879-0301-37fa-8049-4885fa39723d | 2.7641 | -60.0106 | 2026-10-08 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c3af7466-196f-347c-a711-0634f6a2416a | -6.8602 | -41.7494 | 2026-10-08 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 199.9 |
| c42a7e17-e85a-3794-9ccd-3007b881daa8 | -10.4527 | -47.2801 | 2026-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 483dd8ab-281d-359e-aea1-8986bd4d324f | -3.7818 | -41.6479 | 2026-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 145.3 |
| e6f8824c-c560-3504-aa45-367381aeca6e | -11.3986 | -47.5635 | 2026-10-08 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4993b71a-c023-3261-9643-1f92c62e83b3 | -6.8762 | -43.7083 | 2026-10-08 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 0111110d-c198-37a2-b87d-e08d3192f374 | -8.6107 | -67.0116 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 78fede37-680f-37a5-8bcd-4fecc96cc073 | -11.0953 | -44.0037 | 2026-10-08 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 202.4 |
| f12d1c26-5012-3144-a494-2a4c9686028f | -9.4306 | -44.5959 | 2026-10-08 14:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b8064b65-420e-3685-85e4-5c6c42bfdbec | -9.4749 | -64.3713 | 2026-10-08 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 8e205ea5-3ecb-3acb-83b9-4582602dd564 | 1.6568 | -55.7847 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c2274968-9c4b-3f89-aee4-eedaf67ec187 | -15.5222 | -42.6342 | 2026-10-08 14:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 182.2 |
| 42ee8a5e-c0ff-3057-88da-b83e389b97d6 | -7.3361 | -50.0286 | 2026-10-08 14:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9571dc97-e3fb-367c-9dfd-eac9847842eb | -10.6722 | -47.83 | 2026-10-08 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 203eb0c8-2495-39b5-9d3e-28dd8f50a6ad | 1.6568 | -55.8045 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| af1ddb2e-f5b0-374d-bf4b-701ed3c7812b | -4.3285 | -43.8032 | 2026-10-08 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 84cbd0f6-88a0-3b63-b4d5-5eccc7237125 | -8.2181 | -46.362 | 2026-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 725.4 |
| 0eaf08e4-cd0c-3822-8391-3f3081184db8 | -4.3471 | -43.8021 | 2026-10-08 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 2c9bf84d-9b54-3489-97d8-8581d2eb6b4b | -10.4337 | -47.2824 | 2026-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 0bd47aa0-4dc1-3341-9973-6a6cb1e8be8d | -8.9054 | -63.3378 | 2026-10-08 14:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 25f7749e-bcf3-322a-b227-501e8fb4c2c1 | -9.9014 | -44.8147 | 2026-10-08 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 85667ee0-ec17-3ebd-a675-5af1b3f529b8 | -8.5313 | -46.911 | 2026-10-08 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4ff2da6f-1f48-3b30-be31-6b969c4c76f8 | 1.6385 | -55.785 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dfdd3f09-d017-3fd7-a659-99dec80ec483 | -11.983 | -57.6066 | 2026-10-08 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 12a058b3-18f9-3401-b7ad-f487e0ea35c2 | -7.4694 | -42.8551 | 2026-10-08 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 148.4 |
| 6ea2709f-6d06-3e1a-830c-f2ad1934d078 | -1.146 | -54.2199 | 2026-10-08 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1ddd7423-cd38-3761-83ee-d237af45946c | -8.6107 | -67.0301 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 328.1 |
| c073bb36-c13b-3d01-a627-c46501149582 | -11.8404 | -47.372 | 2026-10-08 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f74cb413-9401-3c46-8ce1-d83135ec0bdf | -8.1996 | -46.3415 | 2026-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 2b6963ea-f90f-3da6-89ab-3b1c05561c1c | -9.9398 | -43.5542 | 2026-10-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| a4a40232-6b12-396f-bf82-ed490bfdda7d | -5.3907 | -44.1738 | 2026-10-08 14:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| d44b5cfb-b9d4-31cd-bb8d-564b4dde8f71 | 3.0916 | -60.5567 | 2026-10-08 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 537a857a-2796-327f-b3ee-2db437ee7b81 | -6.8762 | -43.7083 | 2026-10-08 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| d57b2b19-dea1-3b6b-82e9-d5709f2e51da | -15.5222 | -42.6342 | 2026-10-08 14:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.0 |
| 29b21bba-86f5-335d-9008-0f3206257507 | -9.7881 | -44.7828 | 2026-10-08 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 25bf0f42-c9ac-377c-9599-fc0cdfcfbba2 | -1.4756 | -54.5365 | 2026-10-08 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a0df7b33-3c4c-338b-8db6-735b456293c9 | -7.0066 | -59.1029 | 2026-10-08 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 1a96e390-5ba3-3d9a-b12d-a84622f86ced | -1.4752 | -54.7759 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 40e2f067-d1cb-3a55-8c56-14fc880b801b | -5.7321 | -41.6349 | 2026-10-08 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 271.2 |
| 0de3f233-bee5-3655-8315-a210cdd2008c | -1.4755 | -54.6363 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 49e88c7c-bc87-3ef2-8c89-bdf3f23b3730 | -6.6901 | -45.3519 | 2026-10-08 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| e9efeffd-7a5a-3e95-9277-0f23379755d3 | 1.7672 | -55.5463 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1ccd1cf1-d569-386a-be7d-08ddc24219a5 | -7.8876 | -55.0023 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 487715c1-ff7a-3047-b82a-e92dddfacb79 | -7.9086 | -54.7194 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 25963dab-201b-34fe-a2f3-f2b8788a1df5 | -8.1113 | -50.9417 | 2026-10-08 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1e03e776-3841-3f98-859d-6e92c88543b4 | -9.4819 | -66.7836 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 14b6d032-8200-30ad-8966-19ec929d4df7 | -3.1951 | -42.9538 | 2026-10-08 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 563b5cd6-f5fa-33d5-b62c-fbf9e203a1ef | -1.146 | -54.2199 | 2026-10-08 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| f126f2f2-1c5f-3130-9846-2e1f51621792 | -10.9575 | -45.389 | 2026-10-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| cc4fb7a3-12e0-3a0f-a3be-b11b41020b2b | -1.1094 | -54.1601 | 2026-10-08 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c042eb32-c070-390b-be1b-ab2a5bad77cd | -1.3277 | -55.4525 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 45db8181-3379-3621-bc4c-8e8b71a2996b | -4.3658 | -43.8011 | 2026-10-08 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8d027788-b1c2-330c-b645-8eb417907018 | -7.2185 | -55.1016 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 124b1986-a334-3cf0-87de-46b8c714cc6d | -10.9384 | -45.3916 | 2026-10-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d9c36835-3ff1-385f-b733-6b4e706fb3f4 | -6.457 | -55.441 | 2026-10-08 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 75ebaa0c-bc17-3569-af25-5cf22cb509d9 | -11.2295 | -46.2403 | 2026-10-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 44b0666c-5a1b-316a-ad54-fe80aacdc142 | -9.9589 | -43.5516 | 2026-10-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| eccaaac9-b574-3380-8c82-b496bdfced8e | -3.8973 | -44.1255 | 2026-10-08 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f6bdeaaa-ca3e-35c6-81f2-8551ab0825f8 | -7.2371 | -55.1005 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 7e24c090-cb86-3759-9455-54d0e1a45efb | -13.1641 | -54.3178 | 2026-10-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 0e6c204d-24e8-3e15-87d7-d290e3f69757 | -7.3472 | -50.8301 | 2026-10-08 14:40:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e70a002c-69ab-39ae-949e-82424d666932 | -9.475 | -64.3525 | 2026-10-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.8 |
| a8ad5f2a-ee37-3339-a85d-a7a0a81a1f93 | -11.7935 | -43.5215 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f2c6be0e-fd44-3ddc-8a99-e6018420fb8b | 3.128 | -60.613 | 2026-10-08 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9468d0d1-47f1-3d32-99a0-435568b7e1ca | -1.494 | -54.5363 | 2026-10-08 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 4778a9a7-dec0-37b7-a2a5-86ba60ec940e | -8.5313 | -46.911 | 2026-10-08 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2d5c2afb-b3c5-3189-b6e2-7e9f32ce70c8 | -8.1876 | -54.7219 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d48a4151-3c43-37e8-bd4e-3e960a5dc64b | -11.6181 | -43.6669 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 307.8 |
| ef9d3ea1-4454-35a4-8c25-501d7f1f4700 | -9.0592 | -65.9209 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d9e44a8a-5666-3a0b-a6bd-62f6ab5c1c03 | -13.1639 | -54.3385 | 2026-10-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 1f64befe-5b46-3543-8643-6cc7061655ec | -6.7366 | -55.1274 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 165917d0-7da5-3dbc-8074-8261c996e1d6 | -11.47 | -43.3824 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 6fbcac60-356d-3ba2-a008-7621b46eb7a6 | -11.1145 | -44.0009 | 2026-10-08 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 932df90b-31a8-35e5-b3c1-bc31e4a4dadb | 1.6937 | -55.6461 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 499b5ff7-73f2-30bd-929b-b6f14d44ad59 | -7.2 | -55.1026 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5f5d8e34-dcc0-319a-af9f-b8f42a381276 | -7.2179 | -55.1817 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| eacbef4f-8993-3b59-8c0e-63fdf8aaa2d8 | -10.6722 | -47.83 | 2026-10-08 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9d5ca6a5-02e5-39a5-82ff-4b6846f27ad6 | 2.7641 | -60.0106 | 2026-10-08 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 8ab78234-3876-31f5-a00f-10fefd1dee7b | -1.5306 | -54.5558 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c8199a85-ce01-3a4a-8583-c77a06ae9efc | 1.7121 | -55.6063 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |


[Clique aqui para ver as próximas entradas](README217.md)
