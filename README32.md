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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b3b6313-393d-32d2-a9d5-5568184ebd68 | -9.50144 | -60.51668 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce83b37-f528-342b-b13e-40d968a49150 | -7.32627 | -60.62613 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ec2685a-9f37-37f2-bc6d-51ae11c389b3 | -6.90181 | -59.1388 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89e8120a-2e22-344a-b98a-fb828e366d30 | -7.23837 | -57.64629 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc33108-35a3-39d2-a681-60d89c9ab526 | -5.89064 | -57.74737 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a231fe3f-7dd1-3095-b46d-622d938fb5f3 | -5.74515 | -59.89859 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c68e8fa6-e9da-3f6b-900b-cb0616d15345 | -6.1079 | -59.92184 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5747e054-0936-3025-ae4d-1c7037fca6ed | -9.16913 | -59.67016 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f94fe1ae-0e4c-3e84-92b4-bbf163b6735c | -5.73525 | -59.89299 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78be9625-bde4-3ec0-8ad0-9eb77d2f097f | -6.91814 | -59.14512 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86ca70f4-c235-3e64-b909-be727550a457 | -7.24168 | -57.6468 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98b4f4a7-c81c-3aca-a3e5-0a5db24fac66 | -9.49925 | -60.50837 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4b1b595-05c1-35b0-af25-aed160c9aadd | -9.15678 | -59.66062 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ad5965b-784f-38fa-9ac4-6a931db049fb | -6.87698 | -59.1422 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c44e0760-e80e-307f-ad00-c1a6c196f089 | -9.18612 | -59.67979 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af48032b-c8c4-3297-9d37-f32e7dba80d4 | -6.9439 | -44.56329 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 339a806e-cce0-3afd-ad5b-b29b98d8cef4 | -9.50455 | -60.5411 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0efa78d7-d16c-3b8a-a285-fd5237094a83 | -8.79506 | -52.03997 | 2025-08-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d01b8e8c-b7cb-315c-a0e5-58ac1165d92b | -6.90916 | -59.13625 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62d82de6-8ec6-373d-bdb9-9a929f57b547 | -6.91872 | -59.14149 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a9002b0-c2bf-3bb9-bbca-e7587f3fdd02 | -7.46029 | -59.89311 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1821bfc-78d8-32cc-b1e0-15af04ada0c1 | -7.59702 | -63.51946 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1914086a-bcae-3737-bc36-6fcf8eb3d2e3 | -9.49824 | -60.53603 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a23a01a-b0b5-3803-b4d2-21a96867e784 | -8.10752 | -61.20767 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1381f3bf-8eb0-3a75-9c58-580ab7e67ac8 | -7.12718 | -59.63087 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a39a84d0-d058-3d25-b841-590350c37fe5 | -6.88829 | -59.13661 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 254a92c8-38e9-3e30-9f9f-38f1afa3a844 | -7.2675 | -60.6341 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb373e3a-b727-31e2-a65f-e94d55d649be | -8.10166 | -61.19793 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a9a075ce-0faf-3543-aef7-418ea5ce1219 | -5.74766 | -59.88293 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56f4b60-1992-3eb9-9384-037a61be4d48 | -6.91931 | -59.13787 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56fcfa74-8110-3535-b686-e5a0aa095868 | -9.14105 | -59.65053 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ae5e457-9d95-3338-a5ef-9ea0636a8910 | -6.88153 | -59.13551 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d51b64b6-6cba-3533-8d03-f84a21da5a4b | -6.87815 | -59.13496 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0cbdb27-c306-379e-95b7-3812c20c5ee2 | -6.08431 | -59.95072 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9ffceed2-3962-3d8b-8c82-08fe1b5f1380 | -7.4609 | -59.8893 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d853ba-044b-304b-a5f1-0e1b3b12fc07 | -7.5977 | -63.51554 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 398cd2c9-e510-3e72-aefc-23b4fb970fe5 | -6.6447 | -59.07524 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95423f43-607d-3ea5-a851-4e01388d08e5 | -6.89108 | -59.14079 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b7220a7-a9b6-3762-84e0-1aea8e650efc | -6.10247 | -59.93302 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97160f07-ef5c-31cd-8c38-dde4a850b776 | -6.88315 | -59.14694 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc34a172-c728-3877-9afe-3624139cfbf6 | -7.26192 | -59.99511 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a9dcc17-e042-3918-8693-9356de84407b | -6.88307 | -59.88012 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a2ca09e-81b5-3ff4-a415-3779612fa0f9 | -6.89329 | -59.14858 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79513f9e-18f4-3352-aa5d-e73b2597048b | -6.88536 | -59.15474 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f0127694-4247-34fc-bb4e-ac44add86f5b | -6.92152 | -59.14566 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b578fa1-0a18-3d49-b556-5d947d0cb8b9 | -7.28451 | -55.30545 | 2025-08-14 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bcd8e394-2b61-3316-876f-3f0a7d0d5c36 | -9.1897 | -59.65785 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71a96399-878b-3e05-914c-fa287857d4c7 | -9.60286 | -55.14595 | 2025-08-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e33839ca-856d-339f-a205-677445f636a4 | -6.90682 | -59.15078 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6eea3f58-bd28-3d4d-8c4c-231d4c67f33f | -7.55526 | -63.48489 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a2a717b-7605-3b33-aaec-92472f7b3417 | -6.89564 | -59.13407 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c09007d-db6e-34e7-b51f-5e4c5fd07bc2 | -5.89455 | -57.74449 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb704ded-7fbb-39b7-b266-75cd1a00304b | -6.91755 | -59.14877 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 95884102-5c2d-3280-96b2-e2c0d446ee9d | -7.55592 | -63.48097 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d503bbd5-09d2-3f6a-9db2-4180cb10dc1d | -9.05865 | -60.65002 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e46ab42-f45a-34a2-9c94-adc9c2bc9dd7 | -6.89961 | -59.13098 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e4b007b-695e-367a-8285-4134f87e3128 | -6.95335 | -44.55187 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cdea2000-1b7b-39ce-aa3d-b0c6f832ed44 | -3.45322 | -59.3036 | 2025-08-14 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83053d2e-3d82-3a70-bca0-403fcc45feae | -7.45874 | -57.64893 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34cb8b98-501e-31f7-a16f-3f283fe94542 | -6.92549 | -59.14257 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 674a742e-917c-3553-abf7-5e7fab8beb39 | -7.61879 | -63.5192 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ccd305e-4338-3888-9f7f-f2d2d23dc345 | -6.90344 | -59.15023 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 18575b9a-911b-3e01-8575-2b296987959f | -6.89285 | -59.12988 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57566973-a3b2-330f-8e54-50f60270bd52 | -7.25102 | -57.63055 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 056c3e39-09a0-3450-b286-1ca364161a6f | -11.31288 | -49.95461 | 2025-08-14 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ade4a6bc-4074-3c01-b8de-d0deb8536de2 | -8.10682 | -61.21192 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf955b6f-2daa-3934-bcb0-a1744f82baaa | -7.33764 | -60.62382 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e3b3bb0-f00f-386e-aa40-fa97cdffcd98 | -7.87262 | -61.82607 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cd35267e-dec3-3566-b91a-35d732e077fd | -9.21175 | -59.65031 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b540e5cf-7ec9-35c8-8c7d-995ce9be2c37 | -7.13783 | -59.65189 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92f504fd-0b3e-3008-94bf-70ced6f00fdc | -6.89271 | -59.1522 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 913eb24f-5d0a-35df-85eb-9118f152f530 | -6.91697 | -59.15241 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2da0a372-e856-354f-a893-d85be6d02909 | -6.89167 | -59.13716 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c0129af-ac8f-3873-844e-f5f9aff7a0e3 | -6.93355 | -59.63547 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d6deaa8-0c52-3d6c-bcb1-04a3e02f1a69 | -9.18174 | -59.66405 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aa1832f-cfed-316d-a69e-2fecbc34a041 | -7.312 | -60.62378 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e6ab077-ddb2-3ed1-8727-63ec28a2b6ce | -4.77858 | -45.32947 | 2025-08-14 05:10:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9325e0c-5138-3bac-aa49-531bb93b85f0 | -6.64808 | -59.07579 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 10252b7f-ff6d-38f6-91eb-7b67852159ee | -9.2751 | -60.76605 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1102ca76-45da-34d5-ab3c-4e82c27cb61f | -5.74641 | -59.89076 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 754c008c-d7d7-3c54-b0e4-e9f15e7b442f | -5.88788 | -57.74339 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0fe1219-5024-3888-9c08-5fcb92975826 | -6.05979 | -59.94662 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58877616-ae95-32ab-b879-114e1466d488 | -6.08174 | -59.94978 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92399a30-e225-37a0-8c10-5af2768892c6 | -6.90461 | -59.14297 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f89f0930-4c53-309d-b173-5b18311a67ef | -5.98665 | -44.1506 | 2025-08-14 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f99ab3fb-8f71-3a3a-9d59-3f68bad866e0 | -6.65131 | -58.81761 | 2025-08-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95abf1f5-bb09-3fb3-96a6-6b505d9d2bd2 | -6.07569 | -59.93716 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645063b5-ef2f-3649-b54a-b2358d943618 | -7.12436 | -59.62656 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 26901265-447f-32d7-9b5f-49049e09c3ad | -7.88095 | -61.82269 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3f262f1-1c0d-3310-b59f-b56df4b2cf60 | -9.18691 | -59.65364 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2534104-a1e9-3254-89d3-b095a1db92d2 | -7.88027 | -61.80366 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18f90f3b-5cc7-314a-8e28-ec49326cf2be | -6.92828 | -59.14676 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5703def-e75b-350d-b2d2-06a7e6279e36 | -6.9249 | -59.14621 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0dc1a91f-7fa4-355d-a432-acedbc9de18f | -6.09897 | -59.93248 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe70397-a2c3-34a7-9d39-1c36534d235d | -7.62722 | -63.52068 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ea17631-baf7-34df-b2a8-8bd98c9381f4 | -13.07498 | -57.13818 | 2025-08-14 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31a071d3-1288-35a1-849a-bf496e08eb9c | -10.47243 | -61.32914 | 2025-08-14 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20511267-db48-3abe-91c5-86a9e1221549 | -11.68917 | -51.62314 | 2025-08-14 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1d55d3-d0d3-3da1-ad9c-b08aa7effc99 | -13.07648 | -49.32848 | 2025-08-14 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4e53ae5-5467-334e-8915-a3c32f13bbeb | -14.49437 | -53.27903 | 2025-08-14 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
