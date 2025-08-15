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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 036b6180-bec4-308a-8976-74aefa7de706 | -6.9303 | -59.5305 | 2025-08-15 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a6b3f3c0-5e07-342a-bfa8-bd5062d7e7ee | -7.5292 | -61.3254 | 2025-08-15 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e31d92b7-95e9-3cbf-8917-f95274a62bb4 | -9.1894 | -59.6558 | 2025-08-15 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ec0f8e55-df3d-340d-8dec-9ab4fa7650e0 | -9.1892 | -59.6752 | 2025-08-15 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 87bdec84-6921-3227-881e-4e1fa3ccdf6e | -9.1708 | -59.6568 | 2025-08-15 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 9358d57e-a779-3e1b-ab30-eb91dffb3e91 | -6.9302 | -59.5497 | 2025-08-15 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b3ce25f0-1ddc-3c82-b14a-577c1531b970 | -9.4994 | -60.5278 | 2025-08-15 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f5351ba4-360f-3226-ae6c-3407cde7d6ed | -9.1706 | -59.6762 | 2025-08-15 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| cfe7489f-86e9-3adc-997a-e1ce7ecbf25e | -7.53184 | -61.32528 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f27708fb-0274-3595-ab2d-b7e1067b5b3f | -9.20982 | -59.66697 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0660c99-b928-34fb-b562-b559eed83c75 | -7.96159 | -61.76719 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b5d174-a29d-310c-a01b-704c985674e2 | -7.42047 | -60.02517 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 857c08ad-97e0-35e9-afca-2ff7a517fd77 | -7.34133 | -60.62646 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb98e820-65a3-39ea-935c-817db07a76b4 | -9.39189 | -60.53981 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd1bf34a-9447-3005-a2c1-14c92336fa79 | -9.17535 | -59.69136 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91a083fa-acaf-3e7e-9358-623c2121a102 | -7.28135 | -64.69323 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19dfdf86-24f5-35ce-b575-4eba5ddfcf6e | -7.09376 | -59.21922 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 424ee712-f87a-3aee-bbb3-710117ab5e0e | -9.15102 | -59.67062 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa830412-18c3-3ec1-82c5-3eebb5b3ace7 | -6.94872 | -60.00966 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0aa3fedb-f3df-3abc-9bbe-7171b54ea3bf | -9.19142 | -59.67042 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 318cdc24-2106-3afa-883f-cb6061621c79 | -7.95919 | -63.46194 | 2025-08-15 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fe93518-a87d-3da7-bb48-58f1c7f4165c | -7.62545 | -63.51724 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a8ca4d9-48f7-3ac8-8465-a3196b807e5a | -11.40596 | -58.53983 | 2025-08-15 06:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1fd3eca-80ef-3f97-a41f-0fa3e8df29d8 | -9.16354 | -59.6782 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cbd711b-5789-34b8-92ec-8d3f23abacf0 | -6.48442 | -62.94412 | 2025-08-15 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c627551a-5d68-3fd7-ae92-6abfa1aaa657 | -8.11227 | -61.20409 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1d90264-5ffe-3bca-a45e-5f05f5e8ee7c | -7.42811 | -60.01616 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25c0566b-41e2-3129-9a49-18102e82b06e | -7.60362 | -63.52608 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1452bcf0-df76-349e-a75d-f080af919b04 | -8.91998 | -60.73202 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137f438c-791f-3c09-9792-63eaa240322e | -11.43881 | -61.45549 | 2025-08-15 06:10:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b1043b15-a327-3413-a429-c9b4df461ef9 | -7.87243 | -61.80986 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8026661d-e8a9-3fc3-8d4f-3e4c5a06041b | -6.88596 | -59.14813 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ccea978-c364-3e9a-8045-d3e961f91971 | -8.11396 | -61.19113 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca57314b-f224-351c-b615-315f107aeef1 | -6.92544 | -59.52854 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96988350-4aff-3983-a4c5-143681c1373c | -9.63487 | -63.09601 | 2025-08-15 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8e95fd3-ade6-3600-ba57-1cd39b360f50 | -10.32028 | -63.62474 | 2025-08-15 06:10:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd96017-5ddb-3608-ac3d-08512732cae4 | -9.16567 | -59.66103 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| affdf4fe-0bf0-3186-86c9-87983f60ee25 | -9.16144 | -59.69517 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff65e5e2-f69d-3047-9fe3-3d439a857090 | -7.08109 | -59.24076 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2427f165-4703-3004-8b19-7be2f90cbbd2 | -6.9319 | -59.52965 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f9bedaf3-ce57-3e75-aaad-360873bd6e0f | -6.87453 | -59.15839 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64d1bc5f-ef05-38ec-acb8-acc9aa3088ae | -8.40488 | -70.43668 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37c0e80e-df52-3dab-a368-39aa0e6a3585 | -7.4325 | -60.0318 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e070f87d-726e-3f5a-87d4-fb5a8729d110 | -6.72707 | -58.83267 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dfca536a-1fe7-35e3-81b3-9d2f723521f7 | -6.87187 | -59.1523 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5d52565-be52-3819-8572-bbad0e562794 | -6.89341 | -59.14318 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde1a8ad-04c2-3184-b9a8-f749e63b837f | -7.13524 | -60.12759 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb350f64-3b94-3b74-a42c-23e51973396e | -10.47235 | -61.32994 | 2025-08-15 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fdb9fd28-b0e1-34a8-9338-ad8aebf59f77 | -10.33704 | -64.44307 | 2025-08-15 06:10:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd2d2bfd-8e1f-3cf1-be28-26f03b6b9f02 | -7.07592 | -59.22857 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 168a6e67-c2e7-3c53-a61c-02a9f3d38a6c | -7.88433 | -61.80761 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c81ebe57-3fd4-3230-9b6b-cb15c7e60bd9 | -7.43445 | -60.01697 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35c280ae-d8de-3fbb-b11c-51df0f9b2683 | -7.07667 | -59.2228 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 232a67bc-e0ac-3236-a23d-5d44947b0dd2 | -6.89083 | -59.13695 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a3577c4-e1c2-3ab7-a33e-191baf0c565b | -6.89595 | -59.14955 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea483f07-8199-3aca-acaa-86b7bee37e45 | -8.55677 | -63.91858 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6816366c-7a1d-34d9-b477-5e6198aaa4de | -6.91738 | -59.1409 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 443ec9b2-8487-3f96-9e50-d3172c320cda | -6.93816 | -59.63393 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1302dca6-8ae8-37c5-9067-baf23c372d7e | -7.07233 | -59.22797 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43092d27-4fbc-3706-bbbf-7d70fb6d4770 | -6.99688 | -59.98526 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f7cf4a3-3e9f-3c00-9c4e-e3ca89a1e32e | -9.16425 | -59.67245 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8a77bab-5e0f-3269-af69-657f428a1bdb | -6.72111 | -58.82565 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bd73a8a8-1a2f-3f55-8139-c3c3191af3ce | -9.15624 | -59.68284 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9e1fe85-25c3-314f-aa67-c06472482e13 | -7.29807 | -60.625 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c64d48b6-46c6-36ed-92f1-181068e019d3 | -7.28684 | -64.697 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ecc7ad6-eb11-328e-9a1e-4dc3f92729c1 | -6.88266 | -59.14778 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69567047-6102-31b5-a46e-343a253a876c | -7.94446 | -61.76481 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd2a289-4358-3fff-801f-d37a3bead65a | -7.29148 | -60.62778 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d33bd6b-2e17-3b06-9667-91ca874f80d1 | -10.32646 | -64.44721 | 2025-08-15 06:10:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2c6146c-3ba9-3cb4-bf1d-36e3957e52d2 | -9.49935 | -60.5211 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e220feb-2a58-3efa-b265-c77f7ec82d9e | -7.61454 | -63.52166 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 620d6436-36ef-35bd-8f25-9130d2adeda6 | -6.94643 | -60.00858 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4aa854b9-574d-3b77-9cf5-2a8c9b83c010 | -7.94603 | -61.753 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fece081f-1ec0-3d03-8477-67d5b7d2e67f | -9.20089 | -59.6487 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb75a00d-5d81-3787-bc6d-6e1877983379 | -6.71516 | -58.81855 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f137a8e5-d38e-30ef-91fc-b3fd4a635e12 | -7.08329 | -59.22376 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce3f3ec-6d7e-35ba-87ac-b65541041fb5 | -9.50568 | -60.52178 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f6ccd1ff-bf8f-3629-89f5-f88b2f18c461 | -9.17228 | -59.66198 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 644c37cf-bd6d-30db-8b9a-d87bc5115d7c | -7.88272 | -61.81931 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d81db723-5552-322e-9774-a3c3e6377d7c | -9.15694 | -59.67716 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141e593b-42ed-31af-90cf-10cff540b94a | -9.61105 | -67.28891 | 2025-08-15 06:10:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d88c1e3-2b51-3edc-8d75-6a6cf091809f | -7.32989 | -60.6194 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9fef61d-e264-327a-83bb-f2c71574f959 | -7.32317 | -60.62307 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f9264b-49c5-3c89-9545-eca83f1b2c96 | -9.21352 | -59.65544 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3179beac-29c9-3d97-b3ac-d10b3d5bdd7c | -9.15765 | -59.67148 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7bc0cc0-28a5-38ea-b0d9-cdd67b046d02 | -6.93759 | -59.53633 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d59df0c7-16a1-3dbf-a082-62705f5f0b1b | -7.59858 | -63.52535 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f62bb058-825f-3a10-aba3-31de7d303215 | -7.60949 | -63.52094 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9d33959-9ad7-32f5-a490-efc83a85af27 | -9.17748 | -59.67428 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8d2aebe-7d00-3bc8-a364-a5cfed0731cf | -7.88029 | -61.81139 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1af69f47-7288-3e0a-af57-4b800124b0c3 | -7.60484 | -63.51729 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c73126c9-11df-34a3-9cec-1b185ef8ce92 | -9.17677 | -59.67998 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4264a535-73c5-33f4-acbc-e06c23e51727 | -7.87598 | -61.82626 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2d823fe-9e8a-3168-b3a0-502e58a79800 | -7.95279 | -61.74599 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2532a91-2a68-3d95-98a7-31370c2d4ebc | -9.51009 | -60.53756 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a8d0e786-1237-3adf-83ed-a3d124664573 | -6.93912 | -59.5252 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd7c5561-00f7-3f10-8cd2-0f5e57d1e76c | -9.83016 | -60.76435 | 2025-08-15 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b3ac8b1-f312-3603-b948-6d18f3deff4e | -7.31085 | -60.6222 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c52eae29-1a9f-317a-8334-3133e17d1b54 | -9.62996 | -63.09199 | 2025-08-15 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 434f31b3-903a-342d-8ec0-07b6e3a6ed69 | -7.95878 | -63.46492 | 2025-08-15 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README67.md)
