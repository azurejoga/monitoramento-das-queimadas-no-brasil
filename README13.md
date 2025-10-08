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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35dbfeb4-d1a5-3542-b074-d63260b0ab35 | -12.3971 | -63.8811 | 2025-10-08 03:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9b0da294-c13e-377e-bdf9-039f1c631815 | -5.1414 | -44.967 | 2025-10-08 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3c207820-ae7b-33eb-9e7b-797b774de8d0 | -7.0356 | -42.898 | 2025-10-08 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| afe9f0c3-16a0-3cff-b20e-e820fbb3d9a7 | -17.8417 | -57.6254 | 2025-10-08 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| f402c96c-de85-3613-8be7-2d79fc0ed7dc | -5.1227 | -44.9682 | 2025-10-08 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9e6b3876-2127-3afb-8b45-3efdbbe529f7 | -7.0359 | -42.8744 | 2025-10-08 03:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 2ece8c04-3644-3652-a5ca-8b9cbff511ef | -8.2263 | -44.178 | 2025-10-08 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cb40dc82-9259-3c2d-b6ae-161fc74af8a0 | -11.7269 | -50.979 | 2025-10-08 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| e556bf13-7192-3524-beaa-92b6d0cb1980 | -6.9982 | -42.878 | 2025-10-08 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| a2fcc98b-50b1-3156-a677-ebb213a9c125 | -7.017 | -42.8762 | 2025-10-08 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 195.5 |
| c46ff943-9e16-3d3c-81a4-07c76e6df2bd | -7.0167 | -42.8998 | 2025-10-08 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| f54cb2ab-f047-3f42-abc3-8680016c1c97 | -4.4978 | -46.3509 | 2025-10-08 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 84fbf675-a80a-3713-af5d-305ea4ea0fae | -17.8413 | -57.6459 | 2025-10-08 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 00412fb3-9f6f-33c7-8380-f4e95ba45a21 | -6.9982 | -42.878 | 2025-10-08 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| c1f2a16c-02e5-3548-9456-02f2b85a3da2 | -11.7272 | -50.9577 | 2025-10-08 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 302.2 |
| 054ce41a-4d6b-3f6d-baa8-338cb52c682e | -11.7269 | -50.979 | 2025-10-08 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| f62bd050-52c4-3c40-a79f-51859f5e17ff | -7.0356 | -42.898 | 2025-10-08 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 83b3af54-016b-3cd2-8a99-4025afabfd76 | -5.1414 | -44.967 | 2025-10-08 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 16f698b6-781b-3403-86f3-e08945e426e6 | -11.7085 | -50.9385 | 2025-10-08 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 427ee0da-6697-3ab1-8ea2-df1ee531ed1a | -11.7275 | -50.9363 | 2025-10-08 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 9d415ea0-11a2-3a2f-85c5-0d77cb14f25e | -11.7079 | -50.9811 | 2025-10-08 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0f8127f1-a392-3e20-bef8-15183b833d02 | -7.0167 | -42.8998 | 2025-10-08 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| bb202a3b-0d86-3e9f-a870-e019caf3447b | -17.284 | -42.6479 | 2025-10-08 03:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| cf671b90-8237-3f04-9ec5-aee95eaf2eec | -7.0359 | -42.8744 | 2025-10-08 03:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 5dc791a9-9beb-396d-a66a-80661abcfdea | -12.3971 | -63.8811 | 2025-10-08 03:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5fa50615-63c6-3a9b-848e-6fdc1663f41d | -7.017 | -42.8762 | 2025-10-08 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.7 |
| 50a42959-da6b-32b0-82ac-22548c44ae35 | -12.9418 | -46.8562 | 2025-10-08 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 09cbb2e6-c63f-338b-9374-cffe51733006 | -11.7082 | -50.9598 | 2025-10-08 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 87ccfce0-e3cd-3842-9862-3d3d76e4bb11 | -15.2064 | -49.7584 | 2025-10-08 03:40:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 167.5 |
| a8740c54-bdf2-34a5-901d-319d49e2c68a | -12.3971 | -63.8811 | 2025-10-08 03:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 777c9a07-f477-3450-9c81-276e642147a4 | -12.9418 | -46.8562 | 2025-10-08 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| dc956b0f-8d16-36f0-bc66-9206de15fcb8 | -9.1718 | -46.9123 | 2025-10-08 03:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 13c4b159-8080-3a78-b3ad-a6396a4d9a7d | -11.7085 | -50.9385 | 2025-10-08 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b1e640f6-360d-351a-9eb5-6b0759b38225 | -15.2068 | -49.7364 | 2025-10-08 03:40:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| e2076c10-fa6e-3444-9be5-942b9ed0e43d | -7.017 | -42.8762 | 2025-10-08 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 4ee53fe7-de8f-30b9-8d58-a3032a37b62a | -11.7082 | -50.9598 | 2025-10-08 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 1fe18227-2341-3062-9a2e-58f6c36049be | -15.1869 | -49.7615 | 2025-10-08 03:40:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f9a8567e-fb44-3f8d-b6ab-334076acefdc | -7.0167 | -42.8998 | 2025-10-08 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| a9d17a15-c5a3-370d-92f9-36e127ba7a4e | -9.1907 | -46.9104 | 2025-10-08 03:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3572cf4c-ecbd-34dc-b798-70f714d6ccba | -6.9982 | -42.878 | 2025-10-08 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 5e4ec3a0-c508-323c-8592-faf1ef0dc1c3 | -15.206 | -49.7805 | 2025-10-08 03:40:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| e59e20b6-d369-3567-96c8-be8f9676ed65 | -5.1414 | -44.967 | 2025-10-08 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 6a4715b2-1e0c-36d7-add8-7f0db7eb1f97 | -11.7272 | -50.9577 | 2025-10-08 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 443.8 |
| b5813e27-a998-36cb-8b9b-f1a0b5307087 | -11.7462 | -50.9555 | 2025-10-08 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 8625e0a8-4eb1-32b1-b5ef-419d6803a273 | -11.7275 | -50.9363 | 2025-10-08 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 201.8 |
| ce71bab7-f4d2-3ea3-82f8-1637c8a3118d | -7.45503 | -43.12739 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d5d96fc9-c782-3c7a-b367-ec5f65f0ef1d | -7.79951 | -44.21202 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 762299d2-432a-31e6-82c3-59f217a0c5e1 | -4.69207 | -45.83987 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75d8756f-e99c-3e87-80af-820b8ebd1e1c | -7.00772 | -42.87498 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a15e6bd3-d40c-3180-934b-1fc78717f8ae | -5.38899 | -45.20174 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f283abbd-4e57-3867-ad9a-c77f3a694c10 | -7.68477 | -42.40284 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbdd1f8c-38de-3bfe-b5ce-28cd3b7b4f61 | -5.48455 | -44.61766 | 2025-10-08 03:47:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9be4ee9e-1d22-3d73-88a4-eb1ad4852b9b | -7.78747 | -44.22356 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 38745e81-2faa-38a2-9c00-5a83e70fa69b | -4.47971 | -49.7091 | 2025-10-08 03:47:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 07b9e65b-3087-36b5-828b-e3b975219b54 | -4.08536 | -48.04215 | 2025-10-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b0ac85b2-5697-34c1-9e3f-b46cf219309f | -4.6873 | -45.83505 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 47145e55-fa5e-3069-b555-38d78fa1af1e | -4.68866 | -45.83927 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a16baa59-34c3-3029-96ce-28604573d3a7 | -7.00996 | -42.88772 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ea55b088-df46-374b-afff-9c6ceefd1aa9 | -7.78883 | -42.40577 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93167e9f-f98e-3335-86c1-80ce6f5992fc | -7.80412 | -44.21277 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ca20720-81aa-3997-beeb-566ab529df9d | -5.16094 | -46.92443 | 2025-10-08 03:47:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b20998f1-8879-3238-b4b7-058d7aac2adb | -4.69411 | -46.46741 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1f10ab4-3096-3217-8c1d-531a2adc67a8 | -5.40426 | -38.18033 | 2025-10-08 03:47:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fcd932d8-44cb-3c52-9ff3-9b44ed3cb0fd | -7.01311 | -42.84298 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 869d54a0-993d-38e4-bedd-49af9eea5b01 | -7.7919 | -44.20104 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29c00f75-7d37-370e-90b2-b69bda619cab | -7.03039 | -42.87039 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 2fafa320-3c70-3194-9319-4b4d32c291d1 | -7.79244 | -44.2257 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 702b3d76-eb56-31ba-9ea1-1a9418b02862 | -6.98313 | -45.19274 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 623cb5c1-6548-35f8-bcb2-2cda735e9b1c | -7.80302 | -44.21622 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cd32b94-4154-3744-b66a-8a41cad8bdd6 | -7.02839 | -42.88237 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f2a5ccef-04a8-3e78-baa2-a5640906a112 | -7.81627 | -44.14144 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3d872eac-3476-3d38-a1b8-82c985093582 | -5.5022 | -39.70198 | 2025-10-08 03:47:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c1a0fe75-a194-3c9b-a673-7b6ffbf57290 | -4.08445 | -48.04744 | 2025-10-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 837e4be8-7cde-3171-b3b1-81d73681bdf9 | -4.85488 | -45.79151 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fecd0ad-769c-3f28-b679-577f3672b3a8 | -4.69137 | -46.46681 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47b81e53-bae8-30e0-b94a-f78aeea96cd3 | -7.79571 | -44.2065 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c4a6822-5d28-3071-a167-c68ddb2e26e8 | -7.28212 | -41.98407 | 2025-10-08 03:47:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a888d3b1-7f05-3b9e-a4cd-3ce85ffebfdf | -7.81811 | -44.18452 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86d70993-08e6-320c-9269-ffcbcd643e55 | -5.45762 | -44.17275 | 2025-10-08 03:47:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 13fd7631-b12d-3fff-a195-0c9c64474e7b | -7.6747 | -42.58479 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e8eafd1-12a8-3dcb-bcbc-a7a4176a61b1 | -4.69086 | -45.84707 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3e3c6d7b-aa75-353f-8957-a94e300cce58 | -7.45959 | -43.0327 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cd13516d-dea7-35e2-a05c-f8e7b9431466 | -4.949 | -45.59443 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36f599a2-e108-30ea-902b-ba8c121a433d | -5.45233 | -45.87404 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6607dd7-4a41-395e-aab5-0b2b200c284a | -4.9495 | -45.59146 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0117e7ee-79bd-3abd-8832-bc143048a489 | -7.29186 | -41.97489 | 2025-10-08 03:47:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9ec16360-a396-3e34-821e-4a09bf5af584 | -6.42689 | -47.24165 | 2025-10-08 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4ca50d4-7c58-3990-931e-6beb8cba3c18 | -6.08982 | -46.23491 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7b32695-8ebf-348b-9520-b67cbf7d104c | -7.00074 | -42.89034 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 79f26839-0285-3352-84f3-c2fa399a80c5 | -5.13613 | -44.96831 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35abf739-967b-3b6b-a0ca-030b9c682045 | -7.78003 | -42.4081 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b938a0af-ac88-3c3a-9f25-6a2753ee16fc | -7.79926 | -44.21069 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c47bf87d-8109-38a2-99f4-620a5445cc97 | -7.44352 | -43.14261 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6f2386a4-fd65-3578-82a3-3dbd1d7b6ea1 | -4.6893 | -45.83565 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1829e1f7-12c8-3c72-9b40-3f364a768b00 | -0.90026 | -47.54861 | 2025-10-08 03:47:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a9cb36a5-f3d1-3231-9a67-4a59236dd8b4 | -5.84359 | -44.30563 | 2025-10-08 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 748635f4-24b5-3908-a0c5-c690c6ffa179 | -7.7263 | -42.4057 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a6c92daf-0771-36d5-86a8-db7ce63b9ce9 | -4.47991 | -49.7088 | 2025-10-08 03:47:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 85c69f6c-ba4c-37a6-8b32-0c0ab421ead2 | -5.82781 | -35.47815 | 2025-10-08 03:47:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abe967b0-5a07-3726-b8b7-6a57722379b4 | -7.79549 | -44.20518 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README14.md)
