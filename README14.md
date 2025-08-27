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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c244a636-0ea5-33fe-9b3f-a9a658e46ec8 | -6.8412 | -58.9746 | 2025-08-27 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e3312590-b0c5-3975-863f-3138c36ba01a | -8.9028 | -60.7498 | 2025-08-27 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 314c6d5e-3e55-331c-aad7-f9722ec50980 | -9.1007 | -49.5835 | 2025-08-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 158.3 |
| ee9f9842-f0cb-3ab4-bcd3-e1b6c0df8ef6 | -10.2742 | -64.5096 | 2025-08-27 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c99de756-8b6f-3d28-94dd-f171242902e5 | -21.5776 | -47.4852 | 2025-08-27 01:20:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 78.9 |
| aa2b7dd6-77e1-3b78-9123-edd946941411 | -8.8842 | -60.7507 | 2025-08-27 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7546346f-7175-3e17-895f-dd8ac4001131 | -6.8228 | -58.9753 | 2025-08-27 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0c4326b5-d3da-3ae3-a1ce-d9e35663a444 | -9.7915 | -64.265 | 2025-08-27 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e0164657-8edb-3ca6-8479-13fb905f5516 | -8.5386 | -62.6716 | 2025-08-27 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| e4d77349-4275-3c67-b7ea-30c7937fca72 | -13.1644 | -45.2897 | 2025-08-27 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 3c7207e1-5239-3dd4-94c8-d6914ebd1768 | -10.2743 | -64.4907 | 2025-08-27 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 34e6dac3-8345-3c9c-b0a3-62c5cd0cf78b | -9.0821 | -49.5638 | 2025-08-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 22b31805-efc8-33c7-a14e-fef24264f366 | -12.9068 | -44.658 | 2025-08-27 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| da57d3f2-84ba-3db4-becd-9885f097183f | -9.0816 | -49.6068 | 2025-08-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 000605e9-9598-3fee-b861-f167978821a4 | -9.0821 | -49.5638 | 2025-08-27 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6085b1a4-9c0e-30e7-8247-fb0c3b5544fd | -9.6108 | -40.3171 | 2025-08-27 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 95042a6f-3881-3790-83c1-89e32665adcc | -9.6104 | -40.342 | 2025-08-27 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 295.9 |
| 50b1d5e2-fa2f-31a2-ba74-19679ad02eb6 | -10.2742 | -64.5096 | 2025-08-27 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5f44d32c-45c9-3c53-9c3d-197ba005adcc | -6.8228 | -58.9753 | 2025-08-27 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e356553f-cc89-38a7-b22a-2004960ffb7d | -13.1644 | -45.2897 | 2025-08-27 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 169d562e-8aa7-34b8-a548-1e7edfde2319 | -9.1715 | -59.5599 | 2025-08-27 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| cb0252e4-ae3c-3eb4-bff2-62c544cb720c | -9.4249 | -60.5316 | 2025-08-27 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4d8d6cc3-cea8-3bc1-87c2-503d5a0328d8 | -8.8842 | -60.7507 | 2025-08-27 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bc6b7354-559d-367b-9601-f5f9bdf98278 | -9.5913 | -40.3448 | 2025-08-27 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.2 |
| 8e856a3e-d0f9-3207-959c-1563d7825bf0 | -9.425 | -60.5124 | 2025-08-27 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| de6d8249-81f4-33b8-9d37-a3aaf8c1fade | -9.4062 | -60.5326 | 2025-08-27 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 83aeb8ea-5352-38a7-b563-1675a3873783 | -9.0819 | -49.5853 | 2025-08-27 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 8ea4405a-be39-35e9-a563-b07fa31b3b40 | -9.1009 | -49.5621 | 2025-08-27 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 36e59d41-b077-33d8-8c76-5495ab6636bd | -10.2743 | -64.4907 | 2025-08-27 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 9d87943b-7a2f-334f-a904-080a7ac8d9fb | -12.9068 | -44.658 | 2025-08-27 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7b6ffe6f-4568-3e77-81b0-27908d86f3c4 | -9.61 | -40.3669 | 2025-08-27 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 23a53499-53bc-3c30-9fbd-8603a5e18a36 | -9.4064 | -60.5133 | 2025-08-27 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 184.4 |
| c3836bbf-6dee-3f49-a03f-03b30d681d4e | -9.7915 | -64.265 | 2025-08-27 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 7d907a4f-454b-3e81-9cc4-2c25b58c49c6 | -21.5776 | -47.4852 | 2025-08-27 01:30:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cc7cc04a-0881-3587-8cce-4d4f12c7a071 | -6.8413 | -58.9552 | 2025-08-27 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3d3c8424-3793-3895-81fc-ccf79c6a95f5 | -9.1007 | -49.5835 | 2025-08-27 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 10d7752d-6c71-36d3-b73e-301fb6d05cb2 | -9.3329 | -63.2073 | 2025-08-27 01:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 36d8aa7d-42d8-38aa-bb66-ad14c9f371ca | -5.1181 | -43.1964 | 2025-08-27 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 28ed1096-e187-3b28-a591-3fa41ba8badf | -8.9028 | -60.7498 | 2025-08-27 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ac4911b4-71f5-3dec-89d4-215deb20577e | -5.118 | -43.2198 | 2025-08-27 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| af0c9a3d-a906-3cbf-b0fc-08788b084660 | -9.7916 | -64.2461 | 2025-08-27 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| b0ebfe08-a075-3663-b85c-45fe2df742f9 | -13.1837 | -45.2865 | 2025-08-27 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4fcb9aba-8dc4-3207-a6a0-b74ee93be4c2 | -6.8412 | -58.9746 | 2025-08-27 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| efc0b10d-b62e-3a6d-aaaf-7100e48af62b | -8.8841 | -60.7699 | 2025-08-27 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| f065e50a-541e-37e9-badf-1c1c319cc582 | -9.1529 | -59.5609 | 2025-08-27 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0af08e0e-4dc5-3651-989c-c701e55cd71f | -9.4065 | -60.4941 | 2025-08-27 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 9acf6b56-e5b1-33ca-bce3-79d400c63b37 | -8.9026 | -60.769 | 2025-08-27 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 08fa36de-4bb8-3e7f-8053-1c5fd46703b3 | -5.1181 | -43.1964 | 2025-08-27 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 3375b8d5-3512-33e6-aab0-ee82e2b6cd8a | -9.4064 | -60.5133 | 2025-08-27 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 793e2dca-87e1-3f66-9e38-507d260b8e29 | -9.1009 | -49.5621 | 2025-08-27 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9d400d42-7cda-3cde-b9a8-5500884fcef9 | -21.1325 | -45.8848 | 2025-08-27 01:40:00 | GOES-19 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| d50739d4-8075-378e-9df8-d8868e86391c | -12.7643 | -48.1792 | 2025-08-27 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 40128e6e-2978-31df-9b0e-de3e34bb1b8a | -8.8841 | -60.7699 | 2025-08-27 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 52e336d5-efa3-3994-a591-4c301e36d954 | -9.4249 | -60.5316 | 2025-08-27 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 28f51923-5b45-37c9-9b5f-e3f5ea2c6e28 | -13.1644 | -45.2897 | 2025-08-27 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d3ca4b5a-1509-3ed2-a645-589a4aac5da4 | -5.118 | -43.2198 | 2025-08-27 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8b3b6ffb-21c6-39fd-aa78-fe064a4935d6 | -9.3329 | -63.2073 | 2025-08-27 01:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9ccfa8d4-e815-3b19-b9e1-e804089239a9 | -9.4065 | -60.4941 | 2025-08-27 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| d4733ac2-5b7a-3075-949a-223036c0752a | -13.1842 | -45.2633 | 2025-08-27 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 90b232df-3098-3dd5-9506-b97fff7f6c81 | -9.0819 | -49.5853 | 2025-08-27 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 576927de-8cea-3f52-9c33-faa043d95580 | -8.9026 | -60.769 | 2025-08-27 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cc021cb0-02aa-36fe-8e23-0a4089637b2b | -9.0821 | -49.5638 | 2025-08-27 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 049d657f-738c-3187-b6da-c24707a3258b | -12.9068 | -44.658 | 2025-08-27 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ad252424-4773-305b-bfb6-60de37c3fb4b | -6.8413 | -58.9552 | 2025-08-27 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 63bd59d4-3121-3696-a697-5c3e83ba3db5 | -9.1715 | -59.5599 | 2025-08-27 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 23c0d270-59ac-37cc-b067-0c3fcf03a811 | -9.1007 | -49.5835 | 2025-08-27 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| bd9009b6-c5fd-3975-96b7-3ec44eb18043 | -13.1837 | -45.2865 | 2025-08-27 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 64e9f2bd-a865-39fa-8a11-024b51477cb5 | -6.8228 | -58.9753 | 2025-08-27 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f40c4194-d780-3d16-bc28-d2161fa4936b | -9.425 | -60.5124 | 2025-08-27 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2791abaf-4603-3429-b487-0332a571bd4e | -9.7916 | -64.2461 | 2025-08-27 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| d4dcfd8e-0f09-3d8a-93ec-dca4e1716748 | -9.8101 | -64.2642 | 2025-08-27 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 71f80c77-af2e-3b66-ba4c-25eb4dc87910 | -9.1529 | -59.5609 | 2025-08-27 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 718297fd-0100-3a5f-a5ee-56d235c3929d | -21.5776 | -47.4852 | 2025-08-27 01:40:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5ae108ff-d34c-3e4f-a8ac-b34e4f2827e6 | -9.4062 | -60.5326 | 2025-08-27 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 078128bc-a0e0-363c-981d-d7e820ca5486 | -10.2742 | -64.5096 | 2025-08-27 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 25b39479-851f-33ea-a1ed-75b097499acf | -13.4032 | -46.8987 | 2025-08-27 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| de6edd4c-953c-32e4-ba99-9b8de7105aef | -8.8842 | -60.7507 | 2025-08-27 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7c4c10df-f026-30a3-8397-588d5d77341d | -10.2743 | -64.4907 | 2025-08-27 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.1 |
| db37ca7f-d47a-3b7f-9783-c7c316bc11de | -6.8412 | -58.9746 | 2025-08-27 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1d35d9ee-4434-3ac5-8d13-d83f682e72de | -6.8229 | -58.956 | 2025-08-27 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 36bf93ca-f398-391f-9c72-b3893a8f0b5b | -9.4062 | -60.5326 | 2025-08-27 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| c22a6101-64f7-30b9-8869-35051214a680 | -8.7164 | -64.0231 | 2025-08-27 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4410f3fa-5b55-33b2-81df-63cbcc735c4c | -13.1644 | -45.2897 | 2025-08-27 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| be2ae6f1-3216-3d81-9223-d1524a243ee5 | -9.425 | -60.5124 | 2025-08-27 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9cc77886-1ac4-3d53-8e60-466119f1166f | -9.1529 | -59.5609 | 2025-08-27 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 91c558b2-d399-3ee6-9b01-57de42a25048 | -9.4064 | -60.5133 | 2025-08-27 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 3492df04-abca-353d-9b26-47d9c178efa7 | -8.8841 | -60.7699 | 2025-08-27 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 7c84ac7a-10a8-37a8-9003-77ab9e626d05 | -9.4249 | -60.5316 | 2025-08-27 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4460e2bc-927c-30ae-895c-66175c6e7d9c | -12.9068 | -44.658 | 2025-08-27 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 794ea0f2-9dc6-3361-8511-37d4dea0e9f1 | -13.4032 | -46.8987 | 2025-08-27 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fa9d54a8-9394-320c-bcd2-eeec14e2a418 | -13.1837 | -45.2865 | 2025-08-27 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| e39b96b8-cbff-35dd-825e-2804ce398f79 | -9.4065 | -60.4941 | 2025-08-27 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| ef5adc82-c015-3e08-9be0-6cdb36426cd3 | -9.8101 | -64.2642 | 2025-08-27 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| f6a74a3e-287b-381c-a11a-37f3a2f74fed | -6.8412 | -58.9746 | 2025-08-27 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c345a3bd-e503-3fe2-b66d-90aeb00f60fd | -10.2743 | -64.4907 | 2025-08-27 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| ccd2c696-669c-3f76-8753-80815ad6a30e | -6.8413 | -58.9552 | 2025-08-27 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 18f75ee0-2459-30b5-9246-105b2218b66c | -9.1007 | -49.5835 | 2025-08-27 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| e1f0dc28-3cb6-39a7-805b-3b1b00f643cf | -13.4027 | -46.9214 | 2025-08-27 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 59262a12-aaf7-39b0-9d64-0e8d6a3ab563 | -10.2742 | -64.5096 | 2025-08-27 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b6f24499-bbf0-397b-9920-d1250964e922 | -8.9026 | -60.769 | 2025-08-27 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README15.md)
