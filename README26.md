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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49df8b16-8573-359e-9320-588b1e76c000 | -7.8411 | -46.4646 | 2025-10-27 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b75727ed-9a0d-3d66-8326-992c2230fddb | -7.822 | -46.4887 | 2025-10-27 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0324cb48-737f-3d1e-a843-e80b732c8369 | -4.4618 | -43.4248 | 2025-10-27 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0cd4f623-1da3-3819-9858-404eea349c86 | -4.4804 | -43.447 | 2025-10-27 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f06a7745-9953-35d8-b966-e9fbc9e87d20 | -10.7484 | -44.1932 | 2025-10-27 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 108cf825-2b86-3b73-9443-84d254f12a0d | -4.4805 | -43.4237 | 2025-10-27 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 12d5d655-de6c-300e-9470-3c391a7062d1 | -7.8223 | -46.4664 | 2025-10-27 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e6d99714-4fa4-362d-9c09-30676fd09391 | -10.8401 | -56.959 | 2025-10-27 03:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c317da1f-71df-3aed-ba1c-962dd8b7b8e9 | -13.316 | -54.3841 | 2025-10-27 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 1adc5aab-928c-3064-a239-666bf25dc8e7 | -7.8408 | -46.487 | 2025-10-27 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 24f4c17c-5d57-3f18-b4a0-e7fc3d3badf2 | -13.2972 | -54.3655 | 2025-10-27 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4404022f-9e40-3d16-8748-ce83283486d6 | -13.3163 | -54.3634 | 2025-10-27 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| dd7761d1-44a3-3092-b193-beb9cd6103f5 | -8.0258 | -46.7371 | 2025-10-27 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| ff7b0732-e0a5-358f-8d3b-6bdef1678342 | -4.4805 | -43.4237 | 2025-10-27 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 2943bd46-a05b-3507-a9af-c6012853f6f7 | -7.8225 | -46.444 | 2025-10-27 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| cbdc81ef-e517-3893-ba00-0bfd0b03da6d | -4.4807 | -43.4005 | 2025-10-27 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 7c957b70-955c-3ade-9f76-8d9f4ee3e0fd | -7.8223 | -46.4664 | 2025-10-27 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 82e9e91c-335b-35c6-a3d8-8f271d06f1d3 | -8.0446 | -46.7353 | 2025-10-27 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d454f54d-b456-3eab-88df-8bbf4d957c42 | -7.822 | -46.4887 | 2025-10-27 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2a274679-b4a2-3b1b-be3f-fdc6f43f04d7 | -4.4618 | -43.4248 | 2025-10-27 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1aa5817f-bdd6-32ad-8901-1c22311d16db | -10.3594 | -47.18 | 2025-10-27 04:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 400d8d20-3f20-3c83-b3e1-c7924d265e3c | -13.2969 | -54.3861 | 2025-10-27 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| aeba2236-77a0-367f-ba68-d343e9ff562b | -4.4804 | -43.447 | 2025-10-27 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c185f158-6a0e-36c4-82e2-b55d016db94e | -8.0255 | -46.7593 | 2025-10-27 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 6e2781c8-42d2-35f3-a63f-480568ba5534 | -8.0443 | -46.7576 | 2025-10-27 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 444fd8c9-5068-3b28-b88f-3126f9b19fa1 | -7.8411 | -46.4646 | 2025-10-27 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| dda4c895-ca77-3a8d-9043-ebd422297931 | -7.8413 | -46.4423 | 2025-10-27 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 04301555-a3b0-3611-aa5b-d6a7782033d2 | -13.2969 | -54.3861 | 2025-10-27 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ca313271-93a0-3dce-8ab1-2be837dd5b8a | -5.6425 | -47.6271 | 2025-10-27 04:10:00 | GOES-19 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d442c218-50c3-3055-89b8-9ea33261e035 | -6.8796 | -45.1548 | 2025-10-27 04:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b6064d2f-201b-31ba-9af0-d99b69936690 | -7.8408 | -46.487 | 2025-10-27 04:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0b65cd9b-9cc0-3171-9001-2a8a0124050c | -7.8413 | -46.4423 | 2025-10-27 04:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7aefbc24-9dee-3954-a429-1a882bb58361 | -7.8225 | -46.444 | 2025-10-27 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f1d93ed3-124c-38d2-afee-1537e642ac7f | -7.8411 | -46.4646 | 2025-10-27 04:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 59048732-382f-3eb1-baab-6cd6ebb5c523 | -8.0258 | -46.7371 | 2025-10-27 04:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 7a31833b-bbdc-3326-8b8c-5920c167f95a | -13.2972 | -54.3655 | 2025-10-27 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3de35a99-c401-3db5-951b-5e5562dc5d08 | -8.0255 | -46.7593 | 2025-10-27 04:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 9af6b971-0067-3dbe-9b2f-ae2f67d8d25e | -13.316 | -54.3841 | 2025-10-27 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 69159396-52e6-3b22-ac90-57f5a3132fb2 | -4.4618 | -43.4248 | 2025-10-27 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 02c3e007-616a-376c-a206-25a5f8e7f33b | -13.3163 | -54.3634 | 2025-10-27 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ae32b503-0620-3825-8ce0-b42e026911d5 | -7.822 | -46.4887 | 2025-10-27 04:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 2c0ef37d-d144-3de3-884f-0df1e13b3e19 | -13.2777 | -54.3882 | 2025-10-27 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d497f616-bbea-3247-9306-8092164a3df8 | -4.4805 | -43.4237 | 2025-10-27 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 734152d2-0043-3f15-a4f4-ee8e0e3f23c3 | -7.8413 | -46.4423 | 2025-10-27 04:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a68c77dd-7a2d-36dc-ac7b-8771134f3f90 | -4.4479 | -45.4599 | 2025-10-27 04:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 34274bb6-f36e-3929-83d9-9af9b05c9314 | -4.4805 | -43.4237 | 2025-10-27 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| fafc13aa-b818-3385-a6f8-5cc654e707fa | -4.4618 | -43.4248 | 2025-10-27 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e0d62fea-b575-38e3-9a53-3e480b16048a | -6.8796 | -45.1548 | 2025-10-27 04:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| abfd7852-52e3-315d-9317-98723c2e5437 | -13.3163 | -54.3634 | 2025-10-27 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5e23398d-fd1a-3d2f-8bd7-781d32955b82 | -7.8225 | -46.444 | 2025-10-27 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3e06bf21-5490-314e-b065-6b9215bbad04 | -7.8408 | -46.487 | 2025-10-27 04:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 2232e855-f44b-3ea6-8290-77e6850059b7 | -7.8223 | -46.4664 | 2025-10-27 04:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1015b2b6-d699-30ea-aac4-dc6fbf51afc8 | -7.822 | -46.4887 | 2025-10-27 04:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ad341e96-4d0a-30bb-841e-4fe9bea466b5 | -7.8411 | -46.4646 | 2025-10-27 04:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 26d77a81-92a7-37bd-9e59-e907d145fc8f | -4.448 | -45.4374 | 2025-10-27 04:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 5872383c-2442-3326-a13f-31aaf2a38b5b | -13.2969 | -54.3861 | 2025-10-27 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f2fb0ccf-7d1f-3ebd-9c8f-12f60b73bead | 1.6051 | -55.73744 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 777ad13e-f851-3c81-ab8f-79a7565b3812 | 3.63952 | -51.83002 | 2025-10-27 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b6c3d0c-f95c-3b6e-b9f1-ad9beacc2ad3 | 0.16115 | -51.01822 | 2025-10-27 04:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 569fc06d-98ab-3a18-8e78-92193385df17 | 1.61033 | -55.72736 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e31faf58-3f96-3de7-9d60-49ecc745367b | 1.14029 | -51.062 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef01a22a-df74-3208-beda-61abc0e41113 | 1.2453 | -50.90675 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 755f07e1-3635-3804-9b06-cbff4becbef3 | 1.60956 | -55.72915 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b607455-15fd-3853-82ba-e8ccd022a270 | -2.86587 | -41.75485 | 2025-10-27 04:29:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 502f779c-656c-33e9-a4a4-4286a0841624 | 0.8085 | -50.83751 | 2025-10-27 04:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1212dc3-2941-3553-8c4c-cc44902627eb | 0.31576 | -51.02786 | 2025-10-27 04:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfc8d2a9-f1e9-3970-9d31-abe0e7d02b07 | -1.75405 | -46.54241 | 2025-10-27 04:29:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 558a4bb9-13fe-3a48-a945-7f3e368fdb4c | 3.47062 | -51.78787 | 2025-10-27 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4002d630-e263-3d29-81db-5ffb6bed1633 | 1.14485 | -51.06491 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ece7c5-a887-3ddf-ab4b-4a9cd39ced12 | 2.3496 | -51.54229 | 2025-10-27 04:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 132297cf-ec58-3d49-930a-0e936443b8ce | 0.43654 | -50.8246 | 2025-10-27 04:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fff0544b-b8f3-3276-8dab-4d7a9b76d7db | 2.5143 | -51.07602 | 2025-10-27 04:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af05d001-1a2e-3916-bc84-bea6d3fd252d | 0.80771 | -50.83247 | 2025-10-27 04:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 546d5a80-481f-30af-8cba-4665dad4ca53 | 3.02448 | -51.45018 | 2025-10-27 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4143cbdb-146e-389a-944f-bf303d4887fe | 1.15181 | -51.05668 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9b12012-b0d1-31fa-99c8-871b8a23a8f1 | 1.24477 | -50.90331 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecfa2fd4-49d3-33c1-9f8d-3e47f52f38d0 | 1.61092 | -55.73109 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28b3c2f7-805b-362b-b104-f15942dc3c85 | 1.60064 | -55.74575 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c0da7b0-c16c-3ef4-8ac7-8c16c2dbcba7 | 1.14586 | -51.0183 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b057506-7f62-309f-a50e-1462e0ba0195 | -1.23477 | -49.34961 | 2025-10-27 04:29:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd989afd-f5ff-36a7-85a9-b0d27ee264ca | -2.89824 | -42.83537 | 2025-10-27 04:29:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e5ccc7b-c52d-30e1-9235-ca7ea5c14aa9 | 1.14779 | -51.05728 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc27d774-95bd-3c65-9318-3abfef19bcef | -0.96734 | -46.78353 | 2025-10-27 04:29:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c37ecfd8-600a-352a-b7a3-e8d41a0d63aa | -2.8618 | -41.75422 | 2025-10-27 04:29:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1cd667f1-2490-3377-b0d1-6e2091c5f1b3 | 1.14431 | -51.0614 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9458a934-21e2-3d43-8bf5-1d7e2e1ac9e0 | -2.37395 | -45.57793 | 2025-10-27 04:29:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bea66122-da98-3dc1-a893-70eaae98dd3e | -2.90511 | -41.85256 | 2025-10-27 04:29:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4313542-01b7-30d5-9c34-3c92edbc2c78 | -1.36072 | -49.16782 | 2025-10-27 04:29:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2d4d437-3433-301b-b5be-9232cff414a7 | 1.14083 | -51.0655 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2f4b1fc-69ad-36c3-b8a4-5e526b9b5e5e | 1.61151 | -55.73482 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c33b754-3485-347b-ad68-fd422dc4ed82 | 1.61068 | -55.73662 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 355b04a1-e2d4-3823-b5ee-9e6b04466bff | -2.31209 | -45.47412 | 2025-10-27 04:29:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eee4d7ce-be02-3d9b-a298-afd585ca969a | -1.75459 | -46.53898 | 2025-10-27 04:29:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 82e1810d-fbbc-3029-bb00-303dd8851dcc | 1.61012 | -55.73288 | 2025-10-27 04:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3fcecdc-7686-3cf2-a1c9-8879d32d02d8 | 3.63888 | -51.82578 | 2025-10-27 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a68b556-d29b-3cce-a248-2e483badadc0 | 0.3118 | -51.02848 | 2025-10-27 04:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0529e2a3-8005-3ae9-ab92-736ec03f7557 | -2.89372 | -42.83942 | 2025-10-27 04:29:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a2596aa-903b-3770-a41b-d3322140a5e0 | -1.75075 | -46.5419 | 2025-10-27 04:29:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29048042-ee60-38fa-ac52-6cf9be9f2eae | 1.14539 | -51.06841 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 064e8b7d-ca7c-3a84-b6f8-a7b4c4a59e4f | -2.86233 | -41.75062 | 2025-10-27 04:29:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README27.md)
