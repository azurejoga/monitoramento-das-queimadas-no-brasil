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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1d35f2c-59e1-3565-9556-305bd0915e91 | -6.22471 | -55.6189 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b49c67bc-e195-3f92-9fc3-22eeb346cd7f | -6.30208 | -53.57391 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f514f28e-47e8-3f6c-ae54-2869d99232b9 | -7.39798 | -55.15731 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af964b8f-2265-3509-a577-9e46f954ea0b | -6.98978 | -59.28258 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39990e32-1857-31eb-80e6-8c285ec96d03 | -6.62805 | -58.49372 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d542b3b4-7554-3203-bab2-a19d3af3bcb4 | -6.98093 | -59.25154 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbe4b871-454c-3053-af73-72f06127e80c | -7.06846 | -59.23667 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 292be0d2-3702-36e6-9cca-d1a6edde7443 | -7.60181 | -67.41872 | 2026-08-26 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3857412-ff85-3763-be0e-57d5be9994f0 | -6.62994 | -58.51341 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 775003ea-30b4-34f0-a768-226267b02921 | -7.60122 | -67.42238 | 2026-08-26 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b582908-1305-32c8-b32d-3c7e8d7ad898 | -6.25045 | -53.37859 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f1cab33-a7e7-359a-b3d8-47ef774b5194 | -6.99099 | -59.27398 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a88a93d-f140-3c86-bbb7-f7ddb9477c48 | -7.55973 | -61.42537 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adff8967-8e6f-3762-9873-a72d33fcf988 | -6.81523 | -59.58482 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 069a94fb-48b6-3a26-b084-81f977bcf063 | -9.67003 | -55.07954 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a7a6f69-01bd-33f4-8e5e-61758f6afd51 | -7.52481 | -61.38309 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f0ff6710-3b55-3824-88f3-5f3f4e9e3523 | -7.39106 | -55.16438 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df48654e-a6f3-33cc-95d7-c88c3679a83f | -6.22757 | -55.47843 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f5c5ced-ee08-3f9f-838a-f1a2101af429 | -7.79535 | -62.38887 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6d9dd9a-908f-35d3-a090-d65779038ec9 | -8.63136 | -54.7606 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63e1c51f-c3b1-3d0f-82b8-4794c9f24fb6 | -9.48797 | -56.91911 | 2026-08-26 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17caea0-8dc4-3e9e-8505-4119f8c703a3 | -7.77838 | -61.57042 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1779bc1a-fdd3-327d-98f3-ac36df27380d | -3.78106 | -59.28065 | 2026-08-26 05:48:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0e4d331-0ec9-3009-998e-d91ea7ad9962 | -10.16584 | -55.30618 | 2026-08-26 05:48:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb6f2057-c155-34c5-bd05-9e432b821afb | -6.86377 | -59.40627 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53419fac-2320-39e6-965b-a6eefd96dbe5 | -7.3748 | -55.19683 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c55cd998-f12e-3031-8585-309f1a2a9b98 | -7.02236 | -59.24323 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dcc38fe8-10ac-3194-802f-02579b81f37b | -6.26336 | -53.38045 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7152fc9d-a20e-3b68-b4ba-2324a0f265ce | -7.51635 | -61.38677 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8360a5ce-cde3-3a70-ae49-73da30e8a6a0 | -7.47139 | -61.37017 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 286e17ae-fc4b-3e33-b099-a5ea64aa7fc4 | -6.6512 | -58.49702 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f24f2213-cda2-3d51-80d9-659e9eb5a8bc | -6.13954 | -57.84652 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2531931-45f7-3666-8d6d-cfe4f8336697 | -6.25691 | -53.3795 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a442a229-55cb-32d8-bfd0-d43918e0192c | -8.57599 | -55.278 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 012a9966-8278-392c-b86c-5904141e659e | -6.25836 | -53.36877 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2713276b-5c04-390e-81e8-14e44426dde8 | -7.54393 | -61.36113 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e77d82f5-f77e-30e1-893b-612ed9b7bd85 | -7.90283 | -63.68247 | 2026-08-26 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df23264-badf-3690-a363-c1db287310ab | -9.48256 | -56.91864 | 2026-08-26 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43f3c0eb-9996-3c45-bfa7-ecab33b6c8de | -6.33803 | -54.74023 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b54b34a-2cb4-39dc-b335-79b65aeef624 | -8.57485 | -55.28668 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7c54411-07be-34de-ac0f-0ef31c027865 | -6.99995 | -59.30614 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23af36a8-ff5b-36f9-89c4-540ca91dcffe | -6.80423 | -59.59985 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 424333af-9fe7-3c36-8b4a-712f18eb365c | -6.14416 | -59.91378 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c39a3c4b-342b-373e-9d4c-fe9a03dda530 | -7.38638 | -55.15469 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ed91ed96-1e8f-3ae4-8c51-f863d2051548 | -6.86478 | -59.40484 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454838f4-dc72-30dc-9c74-89f58087c8c4 | -9.13027 | -57.56018 | 2026-08-26 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62ecc54c-2226-342c-aa16-001fefcc3c63 | -8.56799 | -54.81923 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0db4a9dd-101d-3895-be60-9c0200b26afc | -6.27849 | -53.36607 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 258d871b-b652-3a81-bc52-2f6c12290034 | -5.98016 | -55.71442 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8473849-6a91-3ee5-b512-77eaa8bfea2c | -6.89217 | -59.02938 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d83b94c-2b6f-3897-9b5c-fdbff7333854 | -7.00529 | -59.23632 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea327c21-f800-3472-b6fa-95e77ed8a233 | -7.06909 | -59.23235 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49625f68-c6e7-3084-9179-11309465abfe | -6.54518 | -58.51901 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c40c0b4-38df-3f19-b930-4b70e585f72b | -6.5388 | -56.25811 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0413c9a3-3628-31f7-a2bc-aa06294be567 | -6.30447 | -53.57175 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b75741b3-2bde-32de-94ab-50bce54a9851 | -7.06593 | -59.22297 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1760774b-9569-3b64-acd6-e8471278b6f5 | -7.27856 | -59.6206 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc036d87-3104-399d-a58f-296c9a5d4ea2 | -6.72705 | -59.14223 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fd3cf3a-b34d-340f-9689-5c11edbf5942 | -8.81726 | -62.32871 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 512e6b2e-fa30-3e9e-b7fc-e1b50e01dbf9 | -7.48063 | -55.28931 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f31736-a76a-360a-89ac-2c682e3ea7fc | -6.99726 | -59.26302 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5022b134-978b-3e8e-9258-9ab22544a1c9 | -8.22639 | -55.0035 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c73dbf37-0048-3499-bd89-194ea8518774 | -7.00971 | -59.23698 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96c13947-146f-3e62-affc-faaf6d861d2a | -6.124 | -57.81734 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d9910672-604a-357b-a0cd-a2e45b561ffe | -6.50409 | -53.265 | 2026-08-26 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 691c2f8e-527c-3d89-bcd2-0cca44c08cfc | -6.83563 | -59.94434 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0d27b95-a7df-3c9b-be5a-e3ca5be39066 | -8.5695 | -55.28167 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 561f35c4-040e-3a0c-a236-44102db57312 | -6.40767 | -60.06275 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36e4d855-0a4c-39e5-b4c6-6ee79b4e1db9 | -9.4699 | -56.90942 | 2026-08-26 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04384fbc-d6a7-3958-958a-f787cdcd2613 | -8.82224 | -62.332 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7817c24b-ca55-3ea7-a069-60761f443237 | -6.77499 | -59.4359 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81c38464-751c-3a37-9a75-8ba59bfb03db | -7.01413 | -59.23764 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b58877e1-b9a7-373c-994f-99b0e81742d1 | -6.9954 | -59.27461 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4fbe58f-c5c4-3bea-aaf8-41178dae6521 | -7.20705 | -60.61357 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ac5ffa2-c665-35fa-8c10-40c14790bec4 | -6.14245 | -59.92513 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 196a718c-2fff-3e4f-a4f7-4abcddfd630a | -6.70193 | -56.34662 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63bb18d4-f024-3a79-bb95-2a5620491607 | -8.56826 | -54.81231 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95c600d6-110c-3451-a263-fa0817ed7c1f | -6.14851 | -57.71252 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b506722-4f76-3157-b9f9-c213cfc5f3dc | -8.16253 | -54.9579 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5bc307a-fb73-3df5-95e4-c149442475e2 | -5.94181 | -57.73122 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86d64bd7-4619-384c-87f8-900b15647109 | -8.81658 | -62.33315 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c6d972e5-b864-3210-a8f4-a04567df4bdf | -6.14366 | -57.71177 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5b0bc53-3b51-3bfc-b9f9-e61135bead5b | -9.60207 | -55.1196 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d892c377-29dc-3f81-a775-516f5eb18fc4 | -7.89938 | -63.68194 | 2026-08-26 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 230a2cdd-2269-3c0f-92cf-0609a294a895 | -5.7713 | -57.55302 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d3a9a8a-4068-3209-86f4-511558f0adf7 | -7.06529 | -59.22733 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e78a2a2c-e1ec-3835-99e2-10d71a3146fe | -6.64517 | -58.50603 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1b014369-5275-350b-aa02-8292b7b101aa | -7.09134 | -56.54574 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18134438-d0d7-3282-bcf6-e7834292764f | -6.7871 | -59.74603 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eac5d9a-d048-3c76-9059-8247bfdcbe28 | -9.09405 | -59.41048 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 661f0cd6-5f8c-3eba-88ba-18d6032a70c2 | -6.15992 | -57.80655 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 003f440e-0932-3e89-a422-268ec6276f98 | -6.33585 | -54.73906 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d7b06b8-c3ed-370c-9696-3d5358b6f782 | -9.66881 | -55.0891 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d84e0f72-ed6d-39e2-9b97-1d74431b72f3 | -6.63268 | -58.49443 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cce91f5-a991-39bc-9c58-051ee8bf2438 | -6.27055 | -53.37598 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 565c23a6-162d-31c2-b53f-1b16320664f9 | -6.62737 | -58.49849 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e21d1eac-25e7-35eb-b555-b30819354e24 | -6.8464 | -59.46348 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a9b962a-73d6-3681-b3b3-cabc64b08de0 | -9.10948 | -60.3947 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64339601-d39f-3dec-aa4c-2c7f5a0d2637 | -6.98468 | -59.25665 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1545c783-bcd6-36ac-92d3-1a81b42739fd | -8.1685 | -54.95895 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README72.md)
