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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 489d3c69-4b85-3038-bc9a-68417ac8aff0 | -9.5139 | -54.6089 | 2025-09-13 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 556d4aa9-1741-37f4-8d2a-0080d0674016 | -3.2321 | -46.7836 | 2025-09-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 445159d5-f179-39bf-99ac-e38c2974100e | -10.1072 | -59.1564 | 2025-09-13 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 18b6440e-194a-3bde-bb66-fd26a6bfe91e | -9.247 | -59.4201 | 2025-09-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 00d5f899-c0d7-33b6-8ced-059c180ec771 | -9.2658 | -59.3997 | 2025-09-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 43c3f6fa-2fb3-3c48-997e-c3f9bdb0e6d1 | -11.4477 | -43.5514 | 2025-09-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 86cc8455-cde7-3ba5-a850-330f935f876e | -9.2472 | -59.4007 | 2025-09-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5fad7a47-e17c-34da-b762-bea397cb5ce8 | -16.5666 | -49.2247 | 2025-09-13 00:00:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 2b2dfaf9-5b1c-3dad-91e7-9558a553b02f | -11.1516 | -51.4229 | 2025-09-13 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| ad48ac52-7b18-34b9-85cd-72b5d8e3f10d | -9.5137 | -54.6292 | 2025-09-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 651da9a1-3b3b-368b-ab47-6e0a323e515a | -9.4807 | -46.4096 | 2025-09-13 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 9f7828ef-de62-3c5d-950f-a961238c0db2 | -9.0344 | -67.4641 | 2025-09-13 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 09c939c6-07be-392c-8ff1-20d76d1120ec | -16.2541 | -50.0745 | 2025-09-13 00:00:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4d148bc8-89cb-3afa-b8dd-1e0879713e85 | -20.2899 | -46.0036 | 2025-09-13 00:00:00 | GOES-19 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| c284d7dd-6fcf-3b3f-882c-b9139b01cb1a | -22.2473 | -48.5869 | 2025-09-13 00:00:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.2 |
| 546e846f-42dd-30c4-97c0-0302972689dc | -22.2264 | -48.592 | 2025-09-13 00:00:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.6 |
| f3ccb045-8d0f-3aaa-b1dc-2643271a1232 | -10.1611 | -64.7401 | 2025-09-13 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9669f3c0-e6c0-3232-aeff-cb405b79ba49 | -22.2257 | -48.6155 | 2025-09-13 00:00:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| fbafa224-9472-3c60-b370-a3f28b3e5645 | -12.0946 | -44.8799 | 2025-09-13 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d21e8bd7-b6af-3f53-a054-937cd72c6ac5 | 0.7089 | -50.648 | 2025-09-13 00:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c28de9f7-0546-3b5f-90a4-4dfef3df46da | -10.1612 | -64.7213 | 2025-09-13 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 89fe7ac9-18c3-310d-a19c-722cb7dcd097 | -9.053 | -67.4636 | 2025-09-13 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| bc3146b9-198b-37da-b9fb-446a4766d3f5 | -12.9292 | -54.7538 | 2025-09-13 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| ec2b6712-1e04-3bfe-b084-9193b01fa14f | -9.4804 | -46.4321 | 2025-09-13 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 082b82ff-fbd6-3c79-b0bc-104ba52560d0 | -17.3629 | -42.6781 | 2025-09-13 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f652ce9e-0299-3b0d-a9dd-4151cfbcd55a | -15.2229 | -56.6782 | 2025-09-13 00:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 724eb6c6-b0fb-3f4e-a576-a3988a2b67ca | -10.6579 | -46.2694 | 2025-09-13 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 502eebf7-2a0d-3a5f-bfbf-c4c4852b500f | -3.212 | -47.1357 | 2025-09-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5fe8b16a-ef8a-3b61-8244-c958004d8b72 | -3.2283 | -47.6154 | 2025-09-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 510a55c3-2832-30eb-9440-dee65476b24c | -21.6187 | -46.8115 | 2025-09-13 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 8025b21e-0a5e-3cee-870f-6fb6eb4f3828 | -9.2844 | -59.3986 | 2025-09-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 314e4db3-d5c6-3319-93c7-a031cdda8201 | -9.4993 | -46.4299 | 2025-09-13 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0518d1d1-49cf-35da-93d5-0866f6086d5b | -9.053 | -67.4451 | 2025-09-13 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 76a57da0-7a5a-39e4-82fc-173b3a7a22b2 | -9.5324 | -54.6277 | 2025-09-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 49a7f62a-f91f-3687-92fa-fa90084d071a | -22.2466 | -48.6104 | 2025-09-13 00:00:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| a7aa98f8-fc7c-3844-8e24-0f51a18cabcb | -3.2305 | -47.135 | 2025-09-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 6352b705-2417-36a6-9a89-5474451dddd7 | -16.4906 | -55.1276 | 2025-09-13 00:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 9de0203d-0e4d-3f76-8afe-0226a2996003 | -12.0056 | -47.7728 | 2025-09-13 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 957d967e-edec-360b-b7a9-0efa21debb9b | -9.2656 | -59.4191 | 2025-09-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| eb746d71-52d8-3bb0-a600-0ca432ef3ae9 | -15.1141 | -42.4528 | 2025-09-13 00:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| eb2308b8-44b1-3fd5-9d0c-9ff84fa9e812 | -9.5135 | -54.6494 | 2025-09-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d7e8b95a-f683-3760-b5a0-879a0329eec3 | -3.2097 | -47.6378 | 2025-09-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4536c5b2-dc7e-3fa4-a424-866d3c7859d4 | -11.1706 | -51.4209 | 2025-09-13 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 2a309782-a05b-3a26-94af-596ad28a29ac | -5.2025 | -44.3244 | 2025-09-13 00:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a2106bf2-e453-3d92-9592-57f841fe850b | -15.1135 | -42.4774 | 2025-09-13 00:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 07d26892-9c19-3bc4-9058-00fdb8dc16c2 | -12.006 | -47.7505 | 2025-09-13 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 1f6c2cf6-174e-307e-855b-6359a8228c93 | 0.6904 | -50.6481 | 2025-09-13 00:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e2d0b884-2cc2-3191-8702-92b32996cf79 | -10.6389 | -46.2718 | 2025-09-13 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3a3374b7-2e2a-3891-b2a0-14d0298ccc92 | -11.9869 | -47.7531 | 2025-09-13 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 06ed1a69-b411-3793-92c7-c0f0247cb0c4 | -17.3622 | -42.7029 | 2025-09-13 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 186.3 |
| c9df8db6-1fb4-3d8a-8262-c98ca67a4f9f | -11.4285 | -43.5544 | 2025-09-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 87c7d3f7-8dd6-382f-a81f-5b3d0b86f3ca | -17.8235 | -50.4236 | 2025-09-13 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 30514a8b-fa8b-3dd1-9f4a-1068d80b6bab | -11.4845 | -43.6402 | 2025-09-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c1c81f90-f528-3ec9-ba50-86f3181ed71d | -22.248 | -48.5633 | 2025-09-13 00:00:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.8 |
| 0f292b9e-52a9-3ed0-99b8-d8627e3c4b09 | -3.2282 | -47.6371 | 2025-09-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| aa2fc054-587f-3047-9411-a1c9a8b2b2bd | -12.1139 | -44.877 | 2025-09-13 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 00df5e9f-17a9-3232-a8a4-5ca70663fb3f | -9.0345 | -67.4455 | 2025-09-13 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 29766a4b-5ab4-3268-948f-84cede704269 | -16.534 | -51.7299 | 2025-09-13 00:00:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9d7fb8e6-555a-31c2-9b95-4dace2fa7682 | -10.6575 | -46.292 | 2025-09-13 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 132ef27d-a65c-33b4-a0ca-a958f3cc4ebd | -17.8434 | -50.4201 | 2025-09-13 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9e4a41b5-5118-3790-b01f-f91abd14b6d4 | -14.9772 | -49.5523 | 2025-09-13 00:00:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 167cd248-3142-30ac-acf2-28aaf36e3a27 | -20.0192 | -47.6459 | 2025-09-13 00:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0b98575e-1477-333a-8f83-f32eb4e2328d | -16.5469 | -49.2282 | 2025-09-13 00:00:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6f32df13-aaf6-34b4-8798-d8b1b50e7a43 | -11.4849 | -43.6166 | 2025-09-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| f5c1fe92-d880-33b3-8da7-71fd46fffc7a | -16.4903 | -55.1484 | 2025-09-13 00:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 4b8aa60c-c601-3905-b093-0fe97e9371e4 | -17.3442 | -42.6333 | 2025-09-13 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f673e5bf-0fd4-389a-b23a-cca9cd8d4ab2 | -10.6385 | -46.2944 | 2025-09-13 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 95891387-2771-3bb9-b4d4-5a972a7cb8fc | -16.5671 | -49.2024 | 2025-09-13 00:00:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 09b98d61-cf8b-3bcb-ae77-8d4444d472d8 | -12.9101 | -54.7558 | 2025-09-13 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f58021f8-c9e9-391b-8d00-4054f9c1a89e | -9.2503 | -51.2472 | 2025-09-13 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ed070ba6-25c4-363c-bec2-2099bade1755 | -12.9294 | -54.7333 | 2025-09-13 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a55c60c5-d7fb-3185-b864-7fa0122584d8 | -11.1519 | -51.4018 | 2025-09-13 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| c951ae9e-bd31-3836-bc03-5d6431fcf5a7 | -9.2843 | -59.418 | 2025-09-13 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 17acdce7-e482-3c9e-a7cc-bf0afd967548 | -12.0056 | -47.7728 | 2025-09-13 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e821ac70-2992-3a8f-8333-bbbf4abf8201 | -3.2283 | -47.6154 | 2025-09-13 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 3279288c-6621-3252-a7cc-d3bb61a0a174 | -10.7667 | -50.5086 | 2025-09-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 203.1 |
| a85da5d4-5313-3689-9fe8-2a011605bf2a | -11.7196 | -46.6031 | 2025-09-13 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d3a21f39-e4ac-3cc7-bb32-f73f0f42e632 | -16.393 | -49.0766 | 2025-09-13 00:10:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 87996b8f-ad5a-3b5a-8186-afdf262703ed | -15.2036 | -56.6803 | 2025-09-13 00:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| af6fc639-c3cc-3c9b-9a51-d53f42754f5f | -11.7388 | -46.6005 | 2025-09-13 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 2be52a19-3b70-37ae-a024-51abdf112bd1 | -16.0454 | -47.9258 | 2025-09-13 00:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 109.8 |
| c3f4ec81-d9da-3672-b938-38cb36ab064f | -9.5135 | -54.6494 | 2025-09-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 84148b2e-5b95-3e1c-9323-2d33cd155583 | -10.6575 | -46.292 | 2025-09-13 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 2e4acb76-a81f-3394-a2ad-b44424becc8c | -20.0192 | -47.6459 | 2025-09-13 00:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4ece4b1d-90d2-3711-8dcb-6b2a0094ad85 | -10.6579 | -46.2694 | 2025-09-13 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 9fafc746-fbd3-3d95-9cc9-eaaa93604958 | -21.6187 | -46.8115 | 2025-09-13 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| f85358d9-75e6-3aee-9578-72c225b530c2 | -3.2321 | -46.7836 | 2025-09-13 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 44cae4e3-9b34-3ad6-ba97-59c4c12de6f2 | -10.7474 | -50.5319 | 2025-09-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 359.4 |
| ebc51eab-3b7e-3bc6-afac-2761da0e82be | -16.0262 | -47.9067 | 2025-09-13 00:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 762f004f-80d5-316d-8387-870453a268cb | -3.2305 | -47.135 | 2025-09-13 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 453ba9d6-4d67-3276-9919-3a07e48c42ac | -22.2264 | -48.592 | 2025-09-13 00:10:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| a2ffed01-b699-3639-8d6f-7d5092f78c9c | -10.1072 | -59.1564 | 2025-09-13 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 73a6f489-1ca7-3aea-85b4-b1f0a6ef6fc1 | -16.3935 | -49.0542 | 2025-09-13 00:10:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 55bfd108-948a-3c69-804b-3cbed93bdc53 | -16.5102 | -55.125 | 2025-09-13 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 4b68b668-a6ad-3c11-b77e-08e42bcf2885 | -10.1611 | -64.7401 | 2025-09-13 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4d730588-9bfc-398f-aebe-8896b5a83c3e | -10.7472 | -50.5533 | 2025-09-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 59a350ed-7ef0-3876-8594-11b00e03901b | -11.1321 | -51.4672 | 2025-09-13 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3b91f582-2e1e-3ec2-99f5-e6af750f7d14 | -10.5073 | -51.5513 | 2025-09-13 00:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| e1200959-173d-3184-a054-89fc3179a858 | -9.2844 | -59.3986 | 2025-09-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b09cd0b7-2821-3d2c-8d93-ec431529adfb | -3.2282 | -47.6371 | 2025-09-13 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |


[Clique aqui para ver as próximas entradas](README2.md)
