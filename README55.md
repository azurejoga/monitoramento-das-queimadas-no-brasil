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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dda67bd-3c06-3e75-971a-58ea26695019 | -8.8506 | -71.36433 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff32335e-8e94-34e3-b748-00eb2c0be9af | -9.03606 | -65.42097 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5207bea-fb40-356b-89fd-485186c86426 | -9.5333 | -67.163 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3133f2e8-a501-3a79-809b-dfb7a489768f | -12.15173 | -64.14602 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45ac6ea6-55c7-3729-b8ff-f40ad0ff4344 | -9.17928 | -68.2204 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbaf3669-edd2-3d0c-bb21-11cb81330350 | -12.1527 | -64.13779 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 334d5377-30be-34fd-bc59-b49aa804f907 | -9.16295 | -71.84524 | 2026-09-12 06:16:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bcc0968-c661-384e-b4b0-f3658afbe07d | -8.56962 | -71.45593 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec0b953b-e2c3-3213-b3c6-a97cf33d6f21 | -9.18407 | -68.21709 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a820fef6-c7c0-31af-8c78-bc1c233e55aa | -10.27134 | -68.27596 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d22138f0-75e6-33e9-ab06-b93aaefcd545 | -9.25265 | -68.22088 | 2026-09-12 06:16:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e301c6d3-bd07-3bbb-9627-ee1001da1bdf | -8.83889 | -71.37061 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a6af116-50c4-3e20-8aa8-f61683479851 | -9.16216 | -68.24998 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0cd9662-b0fb-327a-b0d1-34df84caf512 | -8.98667 | -65.41884 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02bdc229-6646-37c2-a613-0ebb36487510 | -10.27973 | -68.87118 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3731c209-d50d-3207-b545-91fab1b3d405 | -8.75922 | -70.80959 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60e8b48f-a493-3b36-976b-a8dcd354e2db | -8.6035 | -72.71525 | 2026-09-12 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af951e31-f8bf-3475-aed3-c6dc6f75f216 | -8.84953 | -71.08204 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fb1bf16-ecd9-3383-94e3-ba61a7a7e3bf | -9.21891 | -68.93842 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18f0fa26-476b-3a65-b67d-db4f9bf05606 | -20.37411 | -40.59539 | 2026-09-12 06:18:00 | AQUA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 2f9386af-ace9-302e-95fe-7fd4cc6cc98d | -3.7462 | -61.7552 | 2026-09-12 06:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| db9a8a24-c4c4-36cb-b9ab-12fc4e304510 | -3.7462 | -61.7552 | 2026-09-12 06:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e6d55d9e-ba11-3d44-b697-041015795421 | -12.1501 | -64.1414 | 2026-09-12 06:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5d58471d-29ec-386c-8884-71ed60967b4f | -11.3723 | -46.8299 | 2026-09-12 06:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 213e4b0f-3f76-31cb-b381-a94f723bcd92 | -3.7462 | -61.7552 | 2026-09-12 06:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a2ce9841-a262-382a-9e52-83c5f40ca614 | -8.85205 | -71.08183 | 2026-09-12 06:52:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 972d46e5-affb-36c6-9fff-6d735724ee56 | -9.16758 | -68.24497 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6a15803-6bde-3e5f-b7ca-ea9a15a95cf0 | -9.18288 | -68.21981 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3b9ef19-d6b1-3ac1-b7de-c6f70ee63a75 | -9.17004 | -68.2177 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56798eb-0b63-3637-bded-3ade74d91409 | -9.19001 | -68.21543 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b87150d0-d8f8-3601-bf32-161e5ec1c48d | -8.85596 | -71.44804 | 2026-09-12 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6342352f-6173-33a4-ac1b-76a5fc3b576f | -9.17646 | -68.21878 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8a797c9-6b97-38b3-b4a1-4e20e964ac55 | -8.84585 | -71.36642 | 2026-09-12 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec99de00-074d-3913-8c92-da84afe34572 | -9.18364 | -68.22078 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ac7aca0e-77c8-389c-8355-4ccf3349b1b0 | -9.16049 | -68.24945 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2000531a-f4b0-3330-8858-2f27087ce16d | -8.85107 | -71.3672 | 2026-09-12 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3f34b38-6e56-3a4d-aeaf-76db285b7565 | -9.18931 | -68.22076 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d12f3fc-d721-3b35-b75e-59ca59c63daf | -9.18429 | -68.21545 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15cbb51a-df70-340a-b900-c7f51766199c | -9.18357 | -68.21449 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bdaccda-fd9d-3714-ac90-54f0e40604ef | -8.86074 | -71.45199 | 2026-09-12 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f13032-9364-3d13-93c7-e55709bb6993 | -9.49785 | -68.49475 | 2026-09-12 06:52:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b1d6409a-e307-365b-b994-ea749132c0aa | -8.86116 | -71.4488 | 2026-09-12 06:52:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2991f39a-2d59-38da-83dd-4c3e5ce90c84 | -8.84673 | -71.081 | 2026-09-12 06:52:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce627169-4798-3d74-aabc-a2f47fe20914 | -9.16665 | -68.244 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a34e9ff1-7eac-3f4d-b157-50bb1405218b | -9.1822 | -68.22506 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 047898bb-4c54-32ed-bcd7-64a2db54fb4b | -9.15953 | -68.24846 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85849727-c907-3d8c-ad11-6bd6ec83ba62 | -10.28352 | -68.7508 | 2026-09-12 06:52:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4500b461-f967-3a7b-bce2-feba8813d890 | -9.19073 | -68.21642 | 2026-09-12 06:52:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99f00fe0-bd14-331d-beb1-0d572bbc2f74 | -2.94 | -50.4 | 2026-09-12 07:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e55f9e-f320-3a4a-a7db-bf429c758e92 | -2.97 | -50.4 | 2026-09-12 07:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3e1da7-be88-3f24-bff3-3b119ad4732e | -2.71801 | -57.62766 | 2026-09-12 07:52:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 37c39cfe-4bbe-3886-90d3-119abe613688 | -2.73018 | -57.62937 | 2026-09-12 07:52:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ccf51873-b0c6-32fb-9ba5-95a3885ce736 | -3.72993 | -61.74744 | 2026-09-12 07:52:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 84ff5052-7e7b-3a35-ab10-ae1f75f5e46f | -3.36849 | -57.69613 | 2026-09-12 07:52:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7cb9cd6c-3878-37d1-8f11-c59e50d73def | -3.73769 | -61.75843 | 2026-09-12 07:52:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7846bced-4a5e-3624-a6a0-fde6e4aa370a | -2.72062 | -57.60991 | 2026-09-12 07:52:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 19d09829-8897-348b-9018-ce5ac345c690 | -3.73912 | -61.74878 | 2026-09-12 07:52:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| d2482544-1ad8-3386-bedd-4b7326fd3f06 | -2.72755 | -57.64706 | 2026-09-12 07:52:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 49fb8c09-2c89-3935-b585-4092640eee4e | -9.16282 | -68.24111 | 2026-09-12 07:54:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5518324f-2d69-3937-b781-76bab2bdcc3f | -12.15203 | -64.13596 | 2026-09-12 07:54:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a7c5a08e-4b88-3f89-bd41-1ecbb9049dd0 | -8.64096 | -66.4949 | 2026-09-12 07:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a6359087-2589-3dbf-8523-655fd955ae8b | -12.15067 | -64.14532 | 2026-09-12 07:54:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b747ccda-b39a-3b10-9ce0-644b79b55186 | -9.17655 | -68.21919 | 2026-09-12 07:54:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2649be67-fdbb-3989-9825-49545a0b83ae | -2.97 | -50.4 | 2026-09-12 08:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a68f9991-4f7d-3d28-9526-1184b8ff03e9 | -6.7686 | -45.0051 | 2026-09-12 11:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 11d68011-1d1f-3535-a05d-1511c80d694b | -11.3727 | -46.8074 | 2026-09-12 11:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1e73f18e-d86b-3179-9b01-ba487512450d | -6.7686 | -45.0051 | 2026-09-12 11:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 537e38aa-fb16-32fc-8ac5-03b37e8ebc5b | -11.3723 | -46.8299 | 2026-09-12 11:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 473c247e-2397-3e86-9d21-4bfbe098df7b | -11.3731 | -46.7849 | 2026-09-12 11:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 958a778f-d506-3b93-b3e9-1628e1025631 | -11.3727 | -46.8074 | 2026-09-12 11:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 07e5f977-c33b-3bab-8fd0-a7ab86582f35 | -11.3727 | -46.8074 | 2026-09-12 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 205.7 |
| b0837b99-dc3a-3f9e-a87c-6cf9508b493f | -11.372 | -46.8524 | 2026-09-12 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5872b01c-ef45-35e6-9ecd-28d6a91b5c1d | -11.3731 | -46.7849 | 2026-09-12 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0122ae83-2baa-3ce0-97e8-5b092a34653d | -11.3723 | -46.8299 | 2026-09-12 11:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| fbeb4e43-0d7a-38df-9cce-058020de0106 | -11.3727 | -46.8074 | 2026-09-12 11:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 471.8 |
| 46cddcf9-f35c-3185-8731-ef0a7eabcd90 | -11.3723 | -46.8299 | 2026-09-12 11:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| cbb8a851-ef5a-3943-9ac5-16d801e2abc1 | -11.3731 | -46.7849 | 2026-09-12 11:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 31478911-5358-35c3-a594-4f351ce6716d | -7.2147 | -43.7001 | 2026-09-12 11:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e772416e-776a-36a7-99d1-ff7870d2f064 | -10.9491 | -48.3474 | 2026-09-12 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f7f90718-21a2-3d2a-8ebb-1ec2f52842a0 | 1.2204 | -50.73043 | 2026-09-12 11:45:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ca5097d7-280f-3b8d-83d7-2c0ca20fa7e9 | 1.22431 | -50.75863 | 2026-09-12 11:45:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8af915e5-a6bf-3275-85ca-f2517dc8fe6a | 1.25538 | -50.74004 | 2026-09-12 11:45:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7cd848b6-e600-3ade-b4c8-5c3e1714753f | 1.21845 | -50.71637 | 2026-09-12 11:45:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 30.9 |
| a4878f63-3f0d-3add-bc7b-5b1c94aeb376 | -6.32657 | -43.36134 | 2026-09-12 11:47:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6350666a-88f6-39d4-a3b1-05de2c1edcd1 | -5.30969 | -48.73692 | 2026-09-12 11:47:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eab7cd22-7fef-3f21-b41b-05eb6cce28a9 | -7.53887 | -44.9007 | 2026-09-12 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6f50aa2-3f41-32d7-a47b-6e90cf0413ed | -7.59679 | -46.13371 | 2026-09-12 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f05999db-96c6-3587-b272-944cd765d77a | -8.01804 | -44.16498 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a2c8cf36-c4b4-30a3-b5f6-b9220d3378ac | -7.20298 | -44.12547 | 2026-09-12 11:47:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bcdccd52-bb8f-3c3b-91f7-af03cf2d791a | -2.9484 | -50.38993 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| b06fc0e1-40a8-3c0c-ab88-e700b5686897 | -7.21162 | -43.6925 | 2026-09-12 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| edb0a8e6-c0d9-31d1-b916-410b7d5b718e | -7.56368 | -45.17153 | 2026-09-12 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c8f51ed2-7f1e-3dec-9c8d-1e9450479a46 | -6.93786 | -42.7209 | 2026-09-12 11:47:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| fcb1bcdc-e14b-37f4-ae16-7a16f340148e | -6.23628 | -51.6967 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| cc07cc12-3031-30f1-a075-e7621a0fd7d8 | -7.42016 | -46.14705 | 2026-09-12 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 980b5fab-4340-33a0-b714-aad522b4578c | -7.99687 | -44.00153 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| cb17684c-4036-3d01-bad0-1c7f784b9dba | -6.40006 | -43.06568 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 475c56a8-4035-398b-b4c6-a64abc947889 | -7.94173 | -46.23525 | 2026-09-12 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 10be7643-0485-342e-a877-aba2704b69ea | -5.61423 | -44.84079 | 2026-09-12 11:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f6589c55-c750-34c8-bcf4-560f49803b8b | -6.81654 | -42.95155 | 2026-09-12 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |


[Clique aqui para ver as próximas entradas](README56.md)
