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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36e77372-3371-3f80-a1c2-237431c8c0b6 | -8.8095 | -60.8118 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 7b85175f-d643-3ec1-a00e-ad8f22a327a0 | -12.3824 | -47.0057 | 2026-09-21 18:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 93518a0d-8f83-36a8-bbf4-31213073e754 | -6.2585 | -41.6617 | 2026-09-21 18:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| e1e20652-3190-304b-9628-0d3cc05667db | -11.0601 | -54.1345 | 2026-09-21 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 88e2238f-f616-3155-807e-957f389c2f01 | -8.7381 | -45.4526 | 2026-09-21 18:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| bd04596e-9e2b-3a5c-976a-fce6f6a4a0ea | -3.4215 | -60.1896 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7482890c-a935-3d35-9583-3c18c95b70cd | -6.571 | -44.1516 | 2026-09-21 18:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 8aecb807-3fba-3be6-ab3e-3587acb89083 | -11.3734 | -46.7624 | 2026-09-21 18:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 347.7 |
| 70888ffc-6c0b-312b-b754-fbe6c4b1823d | -10.8924 | -53.9652 | 2026-09-21 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bb96ad27-d3e4-3a2e-9487-d2b8d9d5cbf8 | -2.6002 | -59.7653 | 2026-09-21 18:20:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f33029bf-c891-3bb7-9897-1ed94dd4d208 | -11.6609 | -43.4239 | 2026-09-21 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f2c17365-22ec-39ca-80f9-6df03624185f | -9.419 | -68.7499 | 2026-09-21 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5f76c6ed-0d79-3195-96ec-5ea993e212a5 | -3.3493 | -59.8288 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9299fbbf-877a-3d4e-b3d1-140e82060376 | -9.1999 | -60.7738 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| d44fe1aa-58f5-3160-9937-0c29f1db929c | -11.0237 | -49.7304 | 2026-09-21 18:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| ad7ca5a4-53d6-3340-82bd-5f51d232b669 | -10.2152 | -53.9216 | 2026-09-21 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 883a0aef-aa50-3b26-b557-729aeef6db5e | -3.4974 | -59.1944 | 2026-09-21 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| cdb2fda6-ca77-313a-8d5e-8321ca114a83 | -5.395 | -45.9418 | 2026-09-21 18:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| cb08d7d8-57ce-3550-ac62-2149459fd0a5 | -8.8635 | -68.8169 | 2026-09-21 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6f270ad5-5eb1-3bbb-9553-74e66e8b7189 | -6.0739 | -57.7245 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 2edccd5b-7bd2-33c9-8154-983d272abc8c | -7.252 | -55.5794 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 072d2274-1aa3-36de-88b4-06e79dc3b3c9 | -6.2949 | -57.7545 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 2b7c62fd-b656-39eb-8534-2e627ae11174 | -9.4017 | -68.3807 | 2026-09-21 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 80.7 |
| e0b74d8b-ae99-3308-9665-d06128221d9e | -6.9841 | -49.7777 | 2026-09-21 18:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| db423c28-ed99-3e5f-82e1-36974297de7c | -6.4372 | -55.6411 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d5f3e231-988c-3a84-a514-41d4d8e7ef06 | -7.403 | -55.2314 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ce6083d8-fd6f-37cb-a5e9-400005834072 | -3.6947 | -60.5455 | 2026-09-21 18:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9c0559bb-d05b-3afd-ba62-7d0e13593dd4 | -11.0338 | -46.5594 | 2026-09-21 18:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 240e5bd8-29b6-3c9c-8ec0-185d627d910b | -3.571 | -59.0777 | 2026-09-21 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 33ee53a6-0bfe-3126-9664-7d2501a353e6 | -10.8285 | -50.1386 | 2026-09-21 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 079e4ac4-cd83-3084-8a86-973bba5c2380 | -2.7826 | -59.896 | 2026-09-21 18:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cf66776e-4de7-3386-8063-bb74757c2753 | -11.6605 | -43.4476 | 2026-09-21 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 85cb25b9-7bd3-3335-94ed-e40e9fab34bb | -10.8853 | -51.5347 | 2026-09-21 18:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8f528d01-677d-385a-a73a-9305c2082f27 | -9.6111 | -43.9243 | 2026-09-21 18:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 218.5 |
| 6035dd1b-748a-399e-8b14-3e77b8731521 | -10.6064 | -69.3526 | 2026-09-21 18:20:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1fd365b6-5902-33b8-81c0-19358e09df98 | -6.2831 | -59.9394 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 368ddd5b-65b6-336a-85da-d4a454fac736 | -3.331 | -59.8483 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 68f0a1b4-1844-33f3-ae87-8d5f26e040e0 | -7.0573 | -49.9213 | 2026-09-21 18:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 199.2 |
| bba346e6-67ad-357a-a677-25a1e639c87d | -6.3135 | -57.7342 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| eb21a074-b4a3-3f9d-afe7-d96a20946f90 | -6.7119 | -58.9992 | 2026-09-21 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 287.8 |
| a59ed5f7-808e-3eb6-9e9e-b43a3cbe5422 | -5.6094 | -44.8446 | 2026-09-21 18:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d7e1852e-b8ab-3b65-afe2-a374c7fc3148 | -7.1273 | -48.4366 | 2026-09-21 18:20:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| b6c579c4-657b-317c-9a93-21433fc27e7f | -5.5848 | -45.5478 | 2026-09-21 18:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 403722b7-ff0d-361b-886f-5b6790373d99 | -10.8735 | -53.9668 | 2026-09-21 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4527c2af-ccd8-3437-939a-1ed31456121b | -10.4288 | -50.3305 | 2026-09-21 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3ad468f8-7f30-3bb5-9510-b55ef3c5ed2b | -11.0223 | -54.1379 | 2026-09-21 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 08e78fd9-58bf-33e1-a6a2-442c8afe744d | -8.7537 | -44.2821 | 2026-09-21 18:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 74c66d8f-3194-3ae5-ba8c-8662ddce3b3e | -3.4599 | -59.54 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 81ae9943-d4ce-3957-8b56-285794293b00 | -6.4302 | -59.9724 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 7b488325-1a20-3337-8198-eed323dc8bbf | -8.81 | -48.7484 | 2026-09-21 18:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 93394801-146e-38a9-b83a-fc624192830f | -7.2519 | -55.5994 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 7d2dd037-4504-3500-b6a5-835e1a417fd3 | -9.2754 | -60.6162 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 39d51ae6-9be8-3534-a35a-d5ecec4d3393 | -9.8683 | -48.4689 | 2026-09-21 18:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| dc5a8ac8-1780-3dc1-b61b-2bb57003d9e6 | -5.9846 | -44.7261 | 2026-09-21 18:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 188.9 |
| df5415e7-b4be-378b-a012-4c769d44b3c4 | -6.8985 | -41.6976 | 2026-09-21 18:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| f1672cf8-ea7c-34db-9013-f9f89a7bcb5a | -10.4728 | -51.302 | 2026-09-21 18:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ddc557ad-4e35-3bb8-967b-6db78b0ef6b8 | 0.3008 | -60.4497 | 2026-09-21 18:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5fb90df5-43f5-35f1-92ca-47cac7cfb0a3 | -8.8097 | -60.7926 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| e4662ecc-2172-36b0-adf3-1986a4eede1a | -3.4032 | -60.19 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 48b142b8-f85e-3063-96c0-4ddd7cb056ef | -10.2707 | -45.5015 | 2026-09-21 18:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 766.5 |
| bf9ba011-8fb6-3326-a1bb-e8449e8bea48 | -6.922 | -42.9559 | 2026-09-21 18:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 6444bcbf-c6ec-320c-888d-6b47f2f6a56d | -3.5356 | -58.6939 | 2026-09-21 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1a2db9b5-0cb8-3dc1-8721-82f8ae6eed93 | -2.9999 | -54.1688 | 2026-09-21 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1d636c24-8a13-3a95-877c-1dc8d35ec3e2 | -10.7248 | -50.8109 | 2026-09-21 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| be2531bd-0741-3e7e-8b78-bf21d221f48a | -9.0355 | -60.3589 | 2026-09-21 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| afb6840d-7eda-3ac6-8b90-58ae9aa57bf7 | -2.9906 | -57.2137 | 2026-09-21 18:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 868e666c-f220-3ce3-820b-1b24e9b8a524 | 0.7937 | -59.2099 | 2026-09-21 18:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 191.3 |
| ad8447ae-2178-3bd8-9eaa-318847c3e7ea | 1.0844 | -60.6741 | 2026-09-21 18:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 9d88b547-8a18-394b-b950-1ca48d91fbff | 0.7937 | -59.1908 | 2026-09-21 18:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 82a4c38d-4eba-39b3-bcc1-5e0cc0f4bf01 | -12.0638 | -50.0833 | 2026-09-21 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fb1d6834-6f5b-3c20-befc-3a9264f9631e | -6.3842 | -55.265 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 01ce1b19-2275-3118-a7ed-f225c350cefc | -6.7463 | -59.4416 | 2026-09-21 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fa3c93a6-82b2-3e47-86b7-e4f21264bab5 | -3.3825 | -50.4066 | 2026-09-21 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 6bde1857-1dc4-3c9f-95dd-12c5927f9c91 | -10.2545 | -68.7679 | 2026-09-21 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0b05eb0f-d56c-36bc-833c-ae0bc52d9e3d | -11.1541 | -42.8364 | 2026-09-21 18:20:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 40f63c37-16bc-33d0-97a3-e5572a76b448 | -6.295 | -57.735 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 3d801ffc-abdf-3eef-84f0-eb67a56812bd | -3.4554 | -50.6136 | 2026-09-21 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 57b810b0-fad5-3b2a-82b3-c00073edc4d8 | -3.3492 | -59.867 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8142f2d6-bf78-36ee-9fe5-e9a551c9a5be | 3.6729 | -61.8695 | 2026-09-21 18:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 263.6 |
| c9f0d5bd-bce0-3320-9215-cadbd02d4488 | -5.9083 | -57.6726 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 19ad70f6-bc92-350c-8cbb-e26fd6e3de9e | -3.3183 | -57.8677 | 2026-09-21 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5487a7e7-7e31-3aa7-8512-539afc26d030 | -10.1813 | -68.4361 | 2026-09-21 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 111.5 |
| bf5abdab-80a2-329f-9af0-bfe024e66826 | -3.753 | -59.419 | 2026-09-21 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c1f9ff1f-a5af-3920-8de0-a6a7f7738c92 | -9.5668 | -48.435 | 2026-09-21 18:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2da6d946-f035-3bb6-9f55-2de482248e44 | -3.4215 | -60.1896 | 2026-09-21 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 171.0 |
| e68e51d9-2cd2-36cd-9154-0a0f09521d37 | -4.6296 | -55.7551 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5064f0fd-c120-3b8e-ad96-57b5347d300c | -9.1742 | -56.9358 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 5a969e59-8d51-37f2-b777-0c0599951667 | -5.8225 | -53.5214 | 2026-09-21 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 24ff2213-3915-3f85-8427-7546f8af4cd1 | -6.325 | -55.8451 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d07e6a5e-1caf-3dca-8aa1-52338c96b547 | -5.9082 | -57.6921 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 649334eb-fd6d-3a14-8da8-99abb75b0732 | -11.8499 | -46.8105 | 2026-09-21 18:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e5b206ef-9dff-374b-84ab-bfa95e68fd16 | -5.5848 | -45.5478 | 2026-09-21 18:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a0542475-6bd3-3d10-aed2-b40752508e63 | -2.4206 | -58.2712 | 2026-09-21 18:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| b93dba9f-600b-3b8e-b6be-1f55a3fcf772 | -6.0033 | -44.7247 | 2026-09-21 18:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fd3f05f5-4d5d-35de-ac5f-37f12be02fdf | -6.0002 | -57.7079 | 2026-09-21 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 35773737-3555-365c-a468-6cd310dfd077 | 1.0844 | -60.6741 | 2026-09-21 18:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7fb836b8-6f3a-39d1-b6d5-1c9623401e4f | -10.9112 | -53.9635 | 2026-09-21 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| f20e72c3-3c0c-3841-912e-a24c3bc273a0 | -5.975 | -55.7022 | 2026-09-21 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ddb7dab6-fe53-3f40-8be6-f1d2d7725371 | -11.6802 | -43.4209 | 2026-09-21 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 128ed1fb-5c20-3b5c-8759-3b7d956d117b | -10.1628 | -68.418 | 2026-09-21 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 62.7 |


[Clique aqui para ver as próximas entradas](README188.md)
