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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d5bbb2d-d8b7-3405-b62a-24a90c5600aa | -6.93681 | -55.69965 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71dfa4b7-68cd-3b0e-843c-b239069350ee | -5.4829 | -57.14518 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4478c2dd-f0aa-3a1d-abbb-f3d82549a838 | -4.96093 | -55.84826 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 020dc003-f927-35fe-845e-a55fe31fc669 | -7.51856 | -55.28952 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c813a02-01db-3a4e-83fd-0a0569e1ac1e | -1.59221 | -54.41013 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca57bdda-b104-3cc9-8a3c-83875b7e116d | -6.80422 | -59.45462 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3d5f8ad-8740-34bd-8520-535c11ebec0c | -6.9295 | -55.72406 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81d4d66f-e37f-3b56-8a8b-3988485b1b28 | -7.14952 | -46.16941 | 2026-08-31 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5ff8670-e50e-3455-b92d-11d793370b5b | -8.13101 | -45.49331 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cdeff66-871d-3466-8a69-9405fe00e622 | -6.60291 | -58.61444 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b2e3917-011a-351d-b4dd-c5e7cb139a9f | -7.62363 | -55.29233 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cdd9011e-2608-3e32-91f5-35a5a12be2ae | -4.58843 | -55.93879 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f90f0024-9091-37da-ac9c-2ba99b791c02 | -1.60779 | -54.39812 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 424f3c8f-759d-322d-8f33-d9a8569ef323 | -7.52189 | -55.31155 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b766837b-0816-3358-b592-4bc1dfe09191 | -4.96151 | -55.84457 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1bc3027-c9d6-30ea-9b5d-f61137f8b03a | -3.19993 | -58.99477 | 2026-08-31 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95d3fe60-fabc-3bb6-ab99-b1151a3d8791 | -5.48715 | -57.14165 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 577278f4-34a0-3226-af79-29ea90c48bd3 | -1.41366 | -60.31933 | 2026-08-31 04:57:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d0c3550-96ac-32b2-9349-8a4eac23087d | -7.6109 | -55.28675 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e9e96af-e711-3125-95ff-edb81975e647 | -3.97484 | -55.6464 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2cdd616-3c81-3a9d-b72d-30a08e0cb417 | -6.49488 | -53.25723 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ecd504a-b42b-3f77-846d-e654aa2c490c | -7.31232 | -60.58202 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a6d759e2-3905-3fbb-b176-e8e10e47593b | -6.12397 | -57.6791 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e56056d4-c96d-3a2a-98a0-f6b7c2bae298 | -7.5894 | -57.68989 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1317a7a-9c9a-3949-8243-92f6c1dc26e6 | -7.29512 | -60.5793 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc5dd55a-557e-30ec-b596-c9356e205062 | -6.14324 | -53.51216 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bfa7958b-71ae-351d-9794-bb3c53fd67c0 | -7.92452 | -44.24899 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2d866bb8-fcbd-3260-9a39-6a9de087f313 | -6.92223 | -55.72654 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d07f3ece-c7b2-383a-9d1f-127a325255d2 | -7.5169 | -55.2785 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d10c42-c985-3fa6-aead-50d49935b0e5 | -6.12805 | -57.6783 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a62c6d5f-e9e9-3a23-9c24-f6adc0d3cf92 | -7.52244 | -55.30805 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1839bf15-3a0e-3c0a-a6ec-c722e6bd68dd | -3.60972 | -59.07504 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00574edc-5226-3132-8405-574d1a034af2 | -6.11933 | -57.68567 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5704158-6155-32d5-8264-832f87f49240 | -6.37147 | -54.94986 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c0c7d4-7085-310c-914e-84ac3954e3d7 | -6.60444 | -58.605 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 09e574d2-e7fc-3f32-9d0d-ba6b7d04d828 | -6.12869 | -56.38546 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 337b724d-cc0a-3f4f-90a0-ff5eab951409 | -4.95694 | -55.85138 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f2f7ed7-0bfe-357f-80a3-79a5d8eaec27 | -6.93579 | -55.64109 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71347a8e-702c-3d1f-adc1-56cb89cd2f3f | -4.96609 | -55.83774 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f39dae6-64a5-33c2-bfe4-da8033406fef | -6.6822 | -52.85383 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46678ae7-1470-3f9c-b588-bb32b06b194a | -7.33663 | -60.59497 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04ef2308-c6b8-3dbe-8417-945a0d624d38 | -7.29474 | -52.36929 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe7b59cb-e6a0-3cc4-84f3-a314b4e75d93 | -6.12465 | -57.67489 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 9e5d7c08-6efb-3a23-a8c4-fb775b3d946f | -6.26455 | -55.41385 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a57edf8-aa86-3486-8182-7bb64a1a66d2 | -6.86271 | -59.48268 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbe244ce-c28b-3cca-aba2-9f3c057912ad | -6.48404 | -49.89646 | 2026-08-31 04:57:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d296c6a9-38c5-3ec2-8429-514abdf7ed3f | -4.15697 | -60.69501 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6e0ba49-f07e-3f48-a1fc-f461358b2d73 | -3.48522 | -54.46233 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0710f4e0-dfc5-3bd9-ac08-67d7442dedaf | -5.95884 | -57.68044 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68241750-b51f-3550-8e18-ac0162a718d2 | -6.2688 | -55.42583 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa00aef8-c8b6-3b0d-bd35-e69f3d9ab44b | -1.58997 | -54.40255 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3be6e256-f693-3c1a-b716-d5e3cfe6652d | -6.03185 | -58.04104 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eeadb260-d173-3cc0-b543-74675c06ca03 | -7.52467 | -55.33709 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a57520a8-d94f-334d-86ce-2cffac6793a7 | -6.49822 | -53.25773 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae596ec-b218-3621-96c6-846cc7be37a4 | -7.52356 | -55.34411 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b91d568-b9bf-3a00-a5cc-cf7a9f755995 | -4.95986 | -55.83297 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5bd2565-152f-3811-968b-19363f5b13e4 | -5.24598 | -55.88911 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| acae474a-dd2f-3662-91c1-156d830a9fa1 | -7.9685 | -52.43357 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55efad2d-30b6-3e56-b23e-d812bd7d7c9f | -6.76948 | -52.92604 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4907796f-cb90-345f-bcd9-a4e3484cc08e | -6.66492 | -60.12099 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51e3054b-1a50-3788-822d-32a251fce868 | -6.95414 | -55.69877 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9214fa90-288e-3a10-9879-00b3eabecf71 | -7.243 | -60.0116 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73ee6074-5642-305b-bea5-42fa9d5d7889 | -6.11555 | -57.70845 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3554936-174d-3eaf-aab0-770d8500527d | -6.68131 | -58.75225 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72f83f7b-33fb-357c-9e6b-1297a4abf834 | -6.91892 | -55.70412 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30d6d096-460d-330c-acab-0455c546c5d9 | -6.90389 | -63.0587 | 2026-08-31 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7264bea9-1fca-30c4-bcd0-dbf95dfdf2d4 | -6.85986 | -59.47497 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261c5a4d-62b1-39d8-b9a2-19b7d0b11061 | -4.15011 | -60.7082 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77dcf807-1e17-30d7-9285-935ad8ecd420 | -6.95022 | -55.7018 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d94960a9-6fe6-38f7-a88d-36259eae1c96 | -7.33304 | -60.59006 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3644536-73ea-36c6-8ddb-13edc702356f | -1.5961 | -54.40712 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf429658-f710-321b-ae03-1ed3411e3bec | -5.90598 | -56.92921 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e67027-b5dd-3ed8-b087-abddbaf688a5 | -5.25949 | -55.91395 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2ba2f5ac-80a8-3de8-85e4-394ca6e82d3c | -1.60614 | -54.4087 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45977695-1294-3766-98d9-d772af81f52d | -6.9397 | -55.63807 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47f1f25b-7e99-39e6-87d5-3a159324d1f3 | -6.91215 | -59.48347 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53689e9d-e1e3-39f0-9278-aeacadb1cf78 | -4.92832 | -55.76797 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b7b0e9-1708-356c-ba29-b4097a66e283 | -7.31016 | -60.59467 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3e2aa0-9bf5-3809-97fc-12a975c9cd0a | -6.88461 | -59.45012 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35314b31-13ba-32c8-87ca-732ca5fc47e3 | -6.64256 | -53.182 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634960e1-3923-3a29-8ff7-6838eaf54f31 | -6.92279 | -55.723 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| aeb53ac8-8e16-355a-8af6-6f74c7ef17f8 | -6.2138 | -53.58379 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d5e6a54-8699-3e64-a4ee-596fa5e329ed | -7.22075 | -60.66511 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe1a5920-9807-30e2-9381-98ccd8aa14f6 | -6.27616 | -53.3322 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70799676-c451-38fb-b4bf-d9ef205bae3d | -5.57512 | -60.23019 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 004c4beb-e402-3aa0-a6d1-d9864c652929 | -7.91762 | -44.25665 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 61b4883d-a5d3-39e2-92f7-2ab710c99e08 | -6.61209 | -58.60622 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d102f20e-01c6-3108-8ced-014ee5a592b2 | -6.59985 | -58.6091 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0818fdf-a0d0-3490-8775-ea900e3146dd | -6.25397 | -55.41584 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ddd710d-d1e3-35c5-b9c0-99ee03bdd8b3 | -3.40752 | -50.12661 | 2026-08-31 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf2e6f4-c3dc-3571-9a19-2fcebafadbe7 | -7.33983 | -55.15032 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29babb54-bfb9-328e-b374-a2e28da08842 | -3.6236 | -60.56043 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| abae8917-259a-30df-be34-f1ef19f0bc65 | -8.75093 | -46.45512 | 2026-08-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94b978e7-c267-33e2-9790-8f2d5001ea7b | -7.97365 | -52.08181 | 2026-08-31 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdcc44df-285d-370c-82eb-d9103af4506a | -9.42065 | -45.65488 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7fe3628-c2b6-3b57-9a97-bca14b396947 | -7.51524 | -55.28899 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f935b01f-52b1-354f-8110-9b73aec1e5b4 | -7.33234 | -60.59419 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd31b941-d2af-317e-8848-6ab4d16ed923 | -6.86731 | -59.47982 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33a89ed3-f96c-32dd-ab79-a7eef49f7f19 | -7.30299 | -60.5849 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57e09e6a-a567-3c02-afe5-6e2628fe4e7e | -7.52135 | -55.33655 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
