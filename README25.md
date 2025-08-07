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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c8d5497-1c2e-353c-a0e1-eab6c32be373 | -9.70353 | -61.29893 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 332e2088-4ef3-3c54-917e-897dd9097cb1 | -5.81811 | -59.22692 | 2025-08-07 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24cb71f2-4c41-34d5-908f-3b3bd717a3fc | -8.90934 | -60.57109 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdfdbd7f-94a6-349c-a4ac-24d7c66ec051 | -9.94017 | -60.50295 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cffcfba-58b1-3d45-9d9b-edb4536229cc | -8.90695 | -60.54185 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fcbdf574-b130-3f0c-8b4d-8c938993e6c5 | -8.92068 | -60.5804 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| babd9968-ca28-3f78-b7d8-ce6bc740c32a | -8.92375 | -60.58855 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fee156b-0ca5-3e52-81a9-043276474b4f | -8.91333 | -60.58474 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194969f4-4d6f-30f8-83fb-6f359812505b | -9.94144 | -60.46308 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edd75b07-06fe-30f9-95b2-ac5869b08a3a | -8.90727 | -60.56855 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db0c65d8-dda1-362a-939c-7b17188de35b | -8.91555 | -60.55676 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f87984-885a-353d-98df-dd5523faecff | -9.93612 | -60.47036 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6c90a4d-2a73-3c80-96e9-83bfedf49bbc | -8.90517 | -60.60119 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6c5be61-fd62-3b5c-84a1-7cd04a1976d8 | -8.91057 | -60.6035 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 127ce0b3-d576-3f22-8fff-c7f3f823cb3c | -9.93135 | -60.47374 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22056c6e-4c0c-3c56-bfeb-568ec8eef24a | -7.40094 | -60.00682 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 57a1dcae-71fc-3565-97e0-94d27571d435 | -7.40512 | -60.00751 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| af0cdd53-b554-3184-935c-4ecd4676150d | -8.92177 | -60.54239 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a953b8f3-fa7d-3acd-aad4-e9818a485c2a | -8.91771 | -60.55484 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35c0eda0-c869-3887-b9f7-accd48a0d53b | -9.92809 | -60.49725 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11972ade-2d8c-3878-a201-9b5427f8258e | -9.709 | -61.28906 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cebbc343-5375-3f2d-976a-f957904aee97 | -9.70427 | -61.29372 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b888c758-232b-301e-9944-be5e6ee72715 | -9.94034 | -60.47093 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc3cdfec-ae37-31cd-917f-b42a458d93f8 | -8.91108 | -60.54246 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13e94f8d-1ff0-3a26-8ae7-9c23d6610ddf | -6.76091 | -59.47871 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca47ee9d-e9e9-30a6-8da0-955eb984871d | -8.91661 | -60.56236 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5eb69fc-dc90-3df8-88c6-4e7ec6d11b84 | -9.7115 | -61.30005 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70a2c412-ddcc-37b2-b7e3-e6843dbe00fe | -8.91835 | -60.74591 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7dff78b4-178f-3212-82b1-3d938b316c6d | -9.26285 | -60.77671 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b5b2788-9892-3b25-9560-f79453be17c6 | -8.90981 | -60.59805 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 012d0ac7-fda4-31ad-9547-32982b63b602 | -8.91033 | -60.5943 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17cde9df-1047-3319-85fd-e5a4c7482ea6 | -6.63781 | -60.00114 | 2025-08-07 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3594bdba-55bc-3f9f-9b35-5bbb92ae5d12 | -8.91194 | -60.5524 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ad69a7c-4d29-36c3-a34f-c7934c0c2970 | -8.90673 | -60.5899 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcd4cd52-49e6-32e4-a62c-aeaa02a6ae1d | -8.91054 | -60.54619 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ede41c4e-5974-34fa-a388-e71e0d679606 | -8.91989 | -60.73496 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d0729264-64e2-3b23-a7f5-7d88d1ba2c02 | -8.92398 | -60.73557 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cc68f6e4-2d31-3198-aa01-72de270ed06a | -8.91607 | -60.553 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68f34bb-4284-3ad4-b655-ed0c0069bc4f | -8.92295 | -60.74283 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| aaf59477-cf65-3bcd-aa8c-fd8749ec7a9a | -9.9323 | -60.49783 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19c6eda2-0841-32a8-b5d4-a8aef28aebbc | -8.92015 | -60.58418 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d71a89c0-cae6-395b-a04b-a4bd9d99eb44 | -8.9214 | -60.75375 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e683f515-0729-3828-ba1d-c8cf793ca5f1 | -8.92346 | -60.7392 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 212c76f8-d864-3b23-aa39-4ccafc15ba87 | -9.93596 | -60.50235 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f4ce267-8235-375a-8813-d82d8b9569ce | -7.40458 | -60.01133 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dfc1470f-b8e5-38fe-88ee-9c940592eb95 | -8.91242 | -60.57924 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e3b12ed-228f-3585-8aff-4d9f65036646 | -8.92224 | -60.56922 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1d2f429-b36d-3b2e-a75f-732728a81ade | -7.40876 | -60.01198 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d0a7b17-b333-3d21-82aa-2739be7ad178 | -8.91167 | -60.59605 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65713a18-7eb6-34dd-9576-d1d16902b0e7 | -8.9191 | -60.59171 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6127f14-22f8-3199-8ed8-9525be1e6d21 | -8.91 | -60.54992 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 112e3186-d767-380b-9af9-341161a8085f | -8.91498 | -60.59112 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 071bf487-0efc-36af-a8e1-4187b0e91fb3 | -8.91194 | -60.56547 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab7db996-fbbf-32b7-a582-ac6707929aa6 | -8.91222 | -60.59227 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c801a3b-b176-3524-98a8-aeb4fd4993db | -9.93761 | -60.49057 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a82a9a14-b8b2-3943-8e32-bba96e2db601 | -8.90315 | -60.56795 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e09c16d-7920-329a-9463-2c1273f90073 | -8.91374 | -60.749 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33b3c7d6-d014-3de1-91ac-c2ece1b50055 | -8.90621 | -60.59367 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec1b1975-6cd2-3322-98da-e80afdd6aecf | -9.46791 | -57.85265 | 2025-08-07 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db0c6753-d3b2-3b94-b765-c11ad38e94d8 | -8.90369 | -60.56424 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ff79d50-b3a1-309a-a31a-0d35382cbd6c | -8.92036 | -60.76105 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4871448c-ec62-3a87-b187-818d26c465f1 | -8.91968 | -60.55738 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb96555b-5784-3c71-b1a6-57989c11ece1 | -8.9119 | -60.58298 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9462385-1c7a-3c01-aa32-f0f8d0c12a7f | -8.91576 | -60.76415 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49c042d8-ba5a-3a07-a0dc-a01a2675391f | -9.4683 | -57.84978 | 2025-08-07 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2770c0a-30a9-3623-bebb-e859d151db91 | -8.91858 | -60.59548 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d2a2f69-7b55-30ea-bc83-795501e21a55 | -8.9155 | -60.58735 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5863d54-0236-3b13-9f20-b05da3ba2bdb | -6.91813 | -52.84327 | 2025-08-07 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f2b04fc-1566-32d9-aa09-9ef093b73538 | -9.92931 | -60.45743 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e7f7640-d11b-3c9b-ad14-ee3c33e7a93c | -8.90398 | -60.59106 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61aa978b-df40-3bac-8df8-25d5904d67b3 | -9.70752 | -61.2995 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79842599-8dc2-37b7-ae4e-a9ad4d9fbae5 | -10.09795 | -63.18971 | 2025-08-07 05:42:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df98a849-e6f2-3f48-916d-857e3b069a74 | -8.91498 | -60.5735 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fef0222-c50a-3c79-870e-9f59a085fb11 | -8.91552 | -60.56977 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 697521a9-c4e4-3154-9fc2-355f1dbc4126 | -9.70678 | -61.30469 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83a98b9b-7fcb-365e-a12a-b726f4d3fef8 | -8.91358 | -60.55424 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf8833a1-f10b-3e51-b57a-a079cd3d5524 | -8.91138 | -60.58673 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7e7574b-4a86-3aac-aaf1-488bea5568c0 | -8.9202 | -60.55362 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c6128b6-4ffc-34f3-a6f6-b71d6f432c2c | -8.90781 | -60.56486 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d25e376-0882-3783-a769-0425fc3b849b | -9.71224 | -61.29486 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22446e42-2708-3ee9-a53b-0b81c054fb6c | -8.91467 | -60.5468 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3b1c2fd-facc-3a71-9b23-4d2e64281989 | -8.90725 | -60.58614 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d1d4671-3e2d-352f-8ee7-0f65e072b871 | -8.90929 | -60.60178 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 140db6c3-57dc-3b8b-a4e0-49e363697274 | -8.90975 | -60.58041 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72885e7f-a8bc-375c-ab20-9ee5df9a1f1b | -9.93503 | -60.47818 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ace60a9-acff-335b-b47b-bfae986ee70d | -7.40822 | -60.01576 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5262bf3-2d1a-3c21-899b-8016f8f64e18 | -9.93189 | -60.46984 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8285c1d6-f38a-32db-8f83-af7cc0b86e07 | -8.91477 | -60.74172 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 292054ee-7020-3457-bf76-938e52bb9046 | -8.91426 | -60.74537 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c71ddc0-d78a-3afc-9e7f-3ad6af5ef6b1 | -10.05912 | -64.99894 | 2025-08-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ed3d5e-7117-3b6e-bed6-765d44720c66 | -8.90465 | -60.60493 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08564592-b87b-3e3f-a21f-926d0fa51aa1 | -7.43753 | -60.0202 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| def8fc39-c44a-38d3-a0c4-b3475cf7130f | -8.91863 | -60.56488 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c112cc-b0cd-39b9-8f5a-831b8f2d3cac | -9.93339 | -60.49 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4d11d85-8975-3823-a293-6c8cd1707136 | -7.41294 | -60.01265 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 159c6b49-d4c5-3435-b967-2db39bda70bb | -8.91655 | -60.57982 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e28e015-dd3b-322d-a0b7-dd000265adaa | -8.91711 | -60.54554 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9ee2d56-7205-3b65-82c7-9b12e83fbda3 | -8.91399 | -60.56799 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63a7df0e-495d-3617-975a-0846fd0d9130 | -7.40403 | -60.01512 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 706b3e53-5b44-3d12-af53-959d83c29227 | -8.91142 | -60.55615 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
