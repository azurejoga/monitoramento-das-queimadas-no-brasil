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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d094fcbf-78fd-3db9-b7c6-cd77e0369cf0 | -2.15522 | -51.96266 | 2025-10-18 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d91425a-2cd1-30c0-b2d2-e136fbe665f1 | -8.36352 | -46.20059 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c186ce4d-1104-3e5a-92a9-617da9924e0e | -1.83264 | -57.11035 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47df276f-059d-3847-9c41-23bf7e78fdc7 | -3.79748 | -51.76323 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 110bd5ed-9119-335a-8fd0-e440ee74e4e8 | -7.58293 | -44.98444 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e84dbab-46aa-3cd2-97df-823bda78dfe6 | -6.60954 | -44.21995 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a60ad67-6d5f-3cee-9342-0b665e7e95bf | -3.14134 | -50.24998 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45e50fc3-478e-3f92-ab46-617601ecfe63 | -3.75253 | -49.03662 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22830ba7-0ec3-3724-8161-1681729b1a61 | -3.45315 | -51.64164 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 101bc613-f2bf-3a4a-90b7-824aad90ecc8 | -6.24131 | -44.9676 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f67c11d-8c86-3017-85e8-acc24a2193e7 | -6.68339 | -44.27564 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3561cb5-092d-39c6-9651-c3027868781a | -6.14563 | -44.4533 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3a7aa71-cbd7-3d95-b333-e059ec4dc9a0 | -8.35652 | -46.21829 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f37c9271-bc81-3b23-893f-c67fa8ad1b39 | -2.87066 | -50.72221 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3339cff-b13c-39ae-a709-403e2563e324 | -7.01749 | -41.82034 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ef11ec18-11d8-39b2-8e7a-abcacee34fc8 | -7.82672 | -44.12371 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 578af2ae-144d-348e-a2fb-73bb629706d7 | -4.2467 | -48.37199 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314c50f5-5386-366c-8528-8c9845beb54a | -4.97635 | -48.36587 | 2025-10-18 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c31c85c0-7bf0-33b0-aa5b-5f4aa93f1a24 | -4.29197 | -48.26558 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b87bc9e-c916-33be-baeb-32aad003baaa | -8.23765 | -44.01039 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb72ed57-92ad-3d0e-b754-356aab675198 | -8.38098 | -46.24015 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15a9a479-186d-3b13-8806-5c1ce1aecba0 | -9.66731 | -44.55268 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da6ab562-5959-33a5-98df-b3fb6b8275c1 | -7.80109 | -54.9353 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc867ccc-2f95-3962-822e-55ca93b8afbf | -7.0699 | -44.73296 | 2025-10-18 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 140e0ef6-1ba5-3b37-822d-39e5f3613ad3 | -6.59183 | -44.16488 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a75ee07-6241-367c-bd79-995c90d04b73 | -7.99199 | -44.15951 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39e40196-34fc-3122-9477-ce26b160b9db | -9.35392 | -46.98887 | 2025-10-18 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3472238e-3e24-3e30-9b13-e5839b782a8d | -7.16885 | -42.36191 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 15bf541f-2a08-3587-b0a7-30ac4595749b | -9.50572 | -47.26642 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1edd11f1-704e-3681-aa0f-dfda0600529c | -6.60356 | -55.53986 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6986eb7d-d096-34e8-bc82-90c0b0793925 | -8.55746 | -50.08025 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dad26b63-9199-3a9b-89b9-c4acafde119c | -8.60774 | -40.20037 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 714b67e1-579a-3e45-ae54-c93c05236e44 | -4.99512 | -43.85939 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1caa598-611e-31a9-810d-e85a39f5d673 | -9.68055 | -44.54883 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13dcf6b9-3600-3df3-83f8-06904a8a1c1a | -2.37057 | -57.21291 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11dc4969-5c71-3bd5-a0e7-d5f02c02a580 | -8.83067 | -49.68857 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d283037e-0477-30ce-bad5-49fa85b42875 | -8.36163 | -46.21441 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5131e035-5b00-3de0-a0c0-dfbeaf19ab17 | -4.21483 | -48.35843 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a29f1d61-30c6-372d-a85e-bfa8a9953e30 | -8.04439 | -41.10537 | 2025-10-18 04:49:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba74e4b5-2619-3292-9217-5f43b0a4a7a8 | -5.84148 | -45.7328 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f35d98d-51ad-3348-ad38-6003b9167b3b | -7.16694 | -42.36728 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5edcb824-0671-3fd8-afec-f0faa0818447 | -3.42486 | -51.66885 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 020a590c-6338-3fb6-9231-d3801416d36d | -2.87458 | -50.74069 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15ca66ad-ce35-3689-84f7-c6a14642534b | -3.25025 | -50.81336 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bce228af-c91c-3bc8-ac41-0f3784e96177 | -4.5397 | -48.41089 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f31f219-16a3-39dd-a63e-a4dda2b3e33b | -3.2103 | -54.74723 | 2025-10-18 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da243ce-b049-38e9-95d3-0ffb4ca97da7 | -7.35774 | -44.23146 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6225a7ad-6dff-374e-bf2f-3ceecd9725a3 | -3.806 | -51.64476 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80be277f-a247-369c-99b3-7fcd8049f91c | -9.25121 | -44.34834 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e8031b-df21-35ef-8682-f9ff644280a3 | -6.73709 | -44.36499 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce1c22bb-ce3e-32de-a228-7387564d56be | -6.84081 | -42.4272 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5d7c60d2-16ad-33f5-bd44-0750def62e67 | -8.35242 | -49.95739 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44551303-5367-3121-bb17-4f0953f38db9 | -5.94643 | -51.598 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47c19494-103d-39dd-9cfb-03b4402292e7 | -3.51495 | -45.98727 | 2025-10-18 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 598b2565-b16d-3529-95a3-8de4d2ae184a | -5.86842 | -44.84563 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb043c36-1266-3bdc-a030-3b9b8d58603a | -8.83453 | -49.66312 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbdf1a41-05d4-3eb3-8f3b-25017175ab2e | -3.34624 | -49.25159 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 760018fd-9ab7-3291-87c7-7979047172fd | -2.95332 | -49.33883 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c729554-abdc-3219-84f1-6995475d8e7c | -7.02403 | -41.81675 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 23745fa0-d56b-3b3e-8ff4-8575ec83fbbd | -8.36509 | -46.23916 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03a5563f-cd59-3cf2-8881-653cde5637d0 | -2.91065 | -52.73026 | 2025-10-18 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e800ed6b-890d-3da3-8714-c42dd494bc64 | -4.4065 | -43.44315 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2e20677-c83b-3513-bbad-6e26f3368c1d | -2.77856 | -58.14487 | 2025-10-18 04:49:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8079c8f0-af96-3251-84ff-8b40f776edd7 | -2.59863 | -51.34908 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2a351b-4132-3bdb-af83-f38733e0af8f | -8.58481 | -45.4308 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e553e6d8-8d07-3405-867c-9f4bb1d5642d | -8.16154 | -43.30549 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4499e70-b9dd-3484-88aa-309759ab684e | -7.42713 | -46.89682 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed208ba3-5230-3c9a-b615-6914e5e8f788 | -7.3488 | -43.85985 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b2dec415-255d-3698-8925-ec765d1a5efd | -4.37097 | -46.53358 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c66de869-351e-33e0-9c32-4603f4f7a7a1 | -7.1436 | -46.41986 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f45a734-0d64-39e1-b5c8-0f204dbc0f62 | -6.17357 | -47.87231 | 2025-10-18 04:49:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b009918-7d7a-399d-a88b-cb316bd3a5d7 | -2.87845 | -50.73772 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e695c781-0873-33ca-bad6-1ff512e7b94d | -4.64155 | -50.94979 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ed34d03-7ea7-3281-8474-68d6fcdbb0c4 | -6.83242 | -42.42813 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b5e4591f-6721-3c6b-be72-ab4ab17f0616 | -4.82083 | -45.23756 | 2025-10-18 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef3a79a0-928f-3e0b-86b3-49fd121143a2 | -3.40977 | -46.89962 | 2025-10-18 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dfb2c6c-c7d6-3ef4-a081-935c36ccd9af | -3.05997 | -43.21432 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2067f88d-fa99-30a6-86a7-04da4332d318 | -8.78555 | -47.93911 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50968f69-45b1-3228-b40c-3001e040a0a9 | -6.41738 | -43.4728 | 2025-10-18 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8859366-bed1-3123-aca2-0c00f7a5b00d | -7.36361 | -44.22633 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce421c7a-f598-3722-8e8f-e91a1900fcb1 | -3.79418 | -51.76271 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfc4f52a-b556-3531-bbc7-7b940ecb9b52 | -3.81033 | -47.46038 | 2025-10-18 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df80f103-7085-3c6d-984d-8f2bd4a63438 | -9.19897 | -46.87258 | 2025-10-18 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b484c7d9-7337-376c-82d0-5df47ed8c02f | -6.76794 | -56.8618 | 2025-10-18 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41a4556f-6d59-3de4-972d-53f8b01592b1 | -7.86587 | -55.37487 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccc4fab9-a34f-3b2b-a86f-cb12c456ef77 | -2.68917 | -48.70916 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1670d36b-3f19-3647-a005-af1fce22d9ab | -6.3591 | -58.20937 | 2025-10-18 04:49:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ae163be-11b9-3cfc-a183-3da259b75306 | -3.44955 | -52.82567 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73ed89fb-e643-37e0-8ce6-bd8643f8bc1d | -4.00475 | -49.02031 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 019f22e7-861e-3d52-a8e0-1b8f5c613982 | -3.93887 | -48.08724 | 2025-10-18 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d0cc188-7204-3d2e-8783-4002f6e660e0 | -3.8466 | -41.57567 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5d4cc1b9-968d-3565-8167-55096f2845a9 | -8.83462 | -49.6923 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c88061e-1420-3d79-91db-c45b685cee55 | -7.99156 | -44.1626 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 710a919d-9a0c-38dc-b2f7-721fde25b433 | -9.12241 | -46.62051 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee8eaf01-c821-3e55-92b4-26bd83a4ac2f | -4.40226 | -43.4363 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09fb97e9-fd58-32a3-86c0-61d642d7a416 | -7.376 | -50.79918 | 2025-10-18 04:49:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb003b04-d125-3903-af28-9886b58af338 | -8.82768 | -49.68379 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0714a08-75ce-37e7-8dfd-046e51b120f0 | -3.83475 | -47.4045 | 2025-10-18 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 22d52fba-8242-3b10-93f9-aca299cdca9a | -7.1154 | -44.72823 | 2025-10-18 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f66e2cbc-6d6f-33b2-9e59-effc842584e9 | -8.35925 | -46.21621 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README74.md)
