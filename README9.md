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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3194d63-bd62-3f2a-8e9f-f00d2652f2b2 | -14.3627 | -54.9081 | 2026-07-27 07:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 97cfee6a-06df-3b82-afb4-7b48d9309084 | -14.3627 | -54.9081 | 2026-07-27 07:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 9ce5707f-f9e4-3958-b6e6-14e32a742b59 | -10.9397 | -43.0593 | 2026-07-27 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| be01b70e-7bc3-3bc0-8e26-a123e11233d0 | -14.3624 | -54.9288 | 2026-07-27 07:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 8913398e-51b3-3c70-ba45-7d1c1ef16d48 | -10.9397 | -43.0593 | 2026-07-27 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 0ab63d48-fb4d-3a4d-ad86-77d96654d416 | -7.76527 | -37.59357 | 2026-07-27 10:43:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| aa3123e1-9f3e-352f-8ad6-bbd23db6f0b0 | -9.5277 | -47.1187 | 2026-07-27 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6b9e9cc7-a001-36d1-af3f-38d7b52b0745 | -9.5274 | -47.141 | 2026-07-27 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fbb6c65d-b39f-3fb5-ba16-952bd30cf061 | -7.16995 | -59.31218 | 2026-07-27 12:19:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f8caff0e-0fec-358b-8a49-84508c359a5b | -2.43989 | -51.85406 | 2026-07-27 12:19:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2b64815d-e9fe-3fee-8b66-8aca28385a2f | -9.53285 | -47.12061 | 2026-07-27 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5e2135f9-8b91-3e1d-a731-bb735fa40dfc | -9.52956 | -47.14816 | 2026-07-27 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3d67f34b-a2e1-3d37-ae0d-c46b2e70ec82 | -2.44125 | -51.84429 | 2026-07-27 12:19:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a124f5c0-d3fe-3569-8081-108436a316c2 | -9.5277 | -47.1187 | 2026-07-27 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 2413c4f9-2c02-33e9-a51a-121aa695fd72 | -9.5274 | -47.141 | 2026-07-27 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 56d91dd9-a10c-3708-bc91-25b842a1a61a | -12.3216 | -47.194 | 2026-07-27 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| f20cfd26-7a2c-3777-9fca-55acf0d144fd | -12.0436 | -47.7899 | 2026-07-27 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5639800b-3ead-398d-946a-48ed4e7a3c55 | -12.04326 | -47.80244 | 2026-07-27 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| c34f3328-3bb7-345e-8a58-80b709ed73fb | -12.04784 | -47.78108 | 2026-07-27 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f9057c3c-0134-3a48-b0d4-0e93979c37ac | -11.51008 | -50.17648 | 2026-07-27 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b5e9dd55-09a7-37fc-92bc-4773d0cb466d | -13.70288 | -51.88438 | 2026-07-27 12:21:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b12115ed-41e4-3073-9494-e8ddc113d339 | -12.3251 | -47.18687 | 2026-07-27 12:21:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 57adba0b-53c1-3661-b086-80aea6457e2d | -12.32964 | -50.40183 | 2026-07-27 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4a2e1713-ebb6-3d87-b4a6-22dc6282049a | -11.50801 | -50.19353 | 2026-07-27 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 051d2cdf-f9e7-39d8-89eb-5c2f4b976ecd | -12.0447 | -47.80957 | 2026-07-27 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 39cfb3d7-dd95-3673-8d6a-4f0901564f99 | -12.29608 | -50.3805 | 2026-07-27 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| e6e3db4e-61e3-3824-a76f-a1d43049118c | -21.89177 | -56.25837 | 2026-07-27 12:23:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33c98441-1728-3645-bc9c-7fe35c8cf48b | -18.49772 | -54.1075 | 2026-07-27 12:23:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 4d317475-fd05-3535-9920-027916ed3d89 | -18.49921 | -54.09586 | 2026-07-27 12:23:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 77ceb1cb-65d5-38cb-9f54-edd50b6727ab | -19.1756 | -55.17888 | 2026-07-27 12:23:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 072ee832-0456-327b-b875-b7a72a820cde | -19.07553 | -53.46844 | 2026-07-27 12:23:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ce6d8c83-ccc5-3e82-a96b-d6cd768a5a61 | -21.8904 | -56.26862 | 2026-07-27 12:23:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7202867-03f4-33b6-a75e-6004c3cc40d7 | -20.19298 | -56.97742 | 2026-07-27 12:23:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 59e01fc6-8074-364d-95f5-f7d1646a0da9 | -9.5277 | -47.1187 | 2026-07-27 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| d91676b4-4cac-38b4-af2e-ccfaa7c29913 | -12.3216 | -47.194 | 2026-07-27 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| a9a1af16-3f2e-3142-9259-22bf436f34ca | -9.5274 | -47.141 | 2026-07-27 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| f30be956-6af0-3d50-8e0b-6411f08b2d71 | -12.0436 | -47.7899 | 2026-07-27 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 812835d4-8e43-3693-8fa7-28dbc2c76456 | -9.5466 | -47.1167 | 2026-07-27 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 08fa3b19-f6be-304a-b9c7-0d7595f14bb3 | -12.3216 | -47.194 | 2026-07-27 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 07832188-53b4-3dfd-9416-e28448369da4 | -12.0436 | -47.7899 | 2026-07-27 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4c5e6949-abd4-32b6-a8a4-833c897b178e | -9.5274 | -47.141 | 2026-07-27 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 232.1 |
| ca396c03-e450-3713-936e-abc2288a9f8f | -9.5277 | -47.1187 | 2026-07-27 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| e2d89978-982e-3540-806c-7dde25beeba5 | -12.322 | -47.1715 | 2026-07-27 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a55f403d-ec79-331b-98c7-68dd2cd95cef | -12.3216 | -47.194 | 2026-07-27 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 357a72e0-9af3-3f5f-bb38-4562e86b995d | -9.5277 | -47.1187 | 2026-07-27 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| a4a38f6c-b759-3e4f-a26d-497771407cf0 | -12.322 | -47.1715 | 2026-07-27 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 606f2f84-b154-3a6f-89fa-c12f590f0a44 | -12.0436 | -47.7899 | 2026-07-27 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9adfcd92-4270-32ee-889d-0e07a9ccd4df | -9.5277 | -47.1187 | 2026-07-27 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| fd9694dc-4a33-328f-bb8a-eab3c215f10a | -12.0432 | -47.8122 | 2026-07-27 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1eb25071-b552-379b-aaa2-851f9ced6f79 | -12.3216 | -47.194 | 2026-07-27 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 370.8 |
| 9cf41563-b15c-38fb-b5d8-651424b279d0 | -12.0432 | -47.8122 | 2026-07-27 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b9997e52-1e4d-345f-b1ec-854fdd24d23c | -9.5277 | -47.1187 | 2026-07-27 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 01d77bfe-fd45-3c72-831c-3d61fe571d9a | -12.3216 | -47.194 | 2026-07-27 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 365.9 |
| aa5363c1-a856-3b9e-b50a-d49976d5c9ea | -12.322 | -47.1715 | 2026-07-27 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 54b9b446-1018-3f88-ac31-c3f5a77e7ce4 | -9.5466 | -47.1167 | 2026-07-27 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 881371ae-e506-3cdb-8676-266b291c8346 | -12.0436 | -47.7899 | 2026-07-27 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| babbb864-0199-3e69-9901-5d41b8f7c321 | -13.1026 | -43.5647 | 2026-07-27 13:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 11df1dc6-d231-36b4-b6b8-bbf6283defa4 | -12.322 | -47.1715 | 2026-07-27 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 5ccce437-8148-3fa6-b018-92080567a5f0 | -9.5277 | -47.1187 | 2026-07-27 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 170.8 |
| b1662288-0b2c-3aae-bd4a-0c02f4e38835 | -13.0832 | -43.5681 | 2026-07-27 13:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 8fc8e6b2-7864-3fcc-872c-a97370599c74 | -12.0436 | -47.7899 | 2026-07-27 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e579f048-d3fd-34a6-92db-f8e50e6ef24c | -12.3216 | -47.194 | 2026-07-27 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 484.6 |
| 44547e01-8b6e-33c9-83ae-cf74999c7f80 | -9.5466 | -47.1167 | 2026-07-27 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 54d97a06-1d2d-37b4-8c9b-52be613f4491 | -11.5105 | -50.1914 | 2026-07-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 760e4747-d6cd-3d74-b3ab-df7e715b93a6 | -9.5277 | -47.1187 | 2026-07-27 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| c2eaf5ef-4116-30dd-80c7-16b83e7d29b2 | -9.5466 | -47.1167 | 2026-07-27 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7eefbce2-27c5-30f0-95c2-df49f3f38352 | -12.3216 | -47.194 | 2026-07-27 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 278.2 |
| bd1db4e5-9706-325a-9b20-089e8ca43a0c | -11.5105 | -50.1914 | 2026-07-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e4c39f5f-afaa-38ff-99a0-19eb6e4a044e | -13.0832 | -43.5681 | 2026-07-27 13:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ee7ad7a4-2c76-3a27-975c-c13c4b12ba86 | -12.322 | -47.1715 | 2026-07-27 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 74ef15bd-0925-3ac4-90f0-483e0d51446a | -9.5466 | -47.1167 | 2026-07-27 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 72d4420e-27bb-3cb1-ab95-8ce9411f6d15 | -9.5277 | -47.1187 | 2026-07-27 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 048c083f-84a1-3a21-8d17-090290a17701 | -11.4562 | -47.5338 | 2026-07-27 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 70a4ceb3-d977-3754-957c-f8b581ec1fee | -12.322 | -47.1715 | 2026-07-27 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b91b725e-88d3-3faf-a372-a3289439413c | -12.0436 | -47.7899 | 2026-07-27 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 576c8c8b-878d-3c63-aef1-04ca36bfcf03 | -13.0832 | -43.5681 | 2026-07-27 13:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8e9d12d7-c149-3ca8-9fe0-604c6dd410d5 | -12.0432 | -47.8122 | 2026-07-27 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 42e369c1-839a-3666-904d-e097523d175a | -11.5105 | -50.1914 | 2026-07-27 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 80feea9f-0b31-3b08-9eb9-28e3e0e62f57 | -12.3216 | -47.194 | 2026-07-27 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 249.5 |
| b70ed75e-3e08-3e42-bfb4-38124d023e2c | -9.5277 | -47.1187 | 2026-07-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 2819e6fa-c272-356b-955f-17fca414d7f3 | -12.322 | -47.1715 | 2026-07-27 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f9358f44-0c1a-3585-a660-1c0356f3f65c | -12.0436 | -47.7899 | 2026-07-27 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9f7a1f7e-87b5-3c60-bf80-b27b2c02e92f | -13.0832 | -43.5681 | 2026-07-27 13:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7f1d21eb-8933-3a72-99d3-09228cb211c5 | -9.5466 | -47.1167 | 2026-07-27 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 458e0c1e-f92d-3c44-94e2-d6d45f84934f | -12.0432 | -47.8122 | 2026-07-27 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 433300fd-fbc5-3968-8d41-2b83897a2408 | -12.3216 | -47.194 | 2026-07-27 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 77a607ca-630b-3549-9ffd-451766efacf4 | -13.1026 | -43.5647 | 2026-07-27 13:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 5b619b28-5ede-32a5-bd80-dfed99ee9f10 | -13.0832 | -43.5681 | 2026-07-27 14:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7e6fb8ba-7111-3c7c-8912-e42f8afa7af2 | -9.5277 | -47.1187 | 2026-07-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 445a7cc7-70f6-3bfa-9a01-959e11269c82 | -12.322 | -47.1715 | 2026-07-27 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 7c37df1d-2a47-3bcf-884f-2166ed8f25b2 | -12.3216 | -47.194 | 2026-07-27 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 98e53349-dc63-3a74-90e1-c46d17bf716a | -9.5466 | -47.1167 | 2026-07-27 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3438584d-20cf-3729-8c1d-8e01a92c187d | -12.0432 | -47.8122 | 2026-07-27 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c5a7691b-0a0b-3055-b57c-55d89db484cb | -13.6992 | -51.8913 | 2026-07-27 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 735a6654-902a-34cd-b5c6-eebede73eae1 | -13.1026 | -43.5647 | 2026-07-27 14:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bbfa8f93-b1cb-3156-8dfa-43e4f7178413 | -9.5277 | -47.1187 | 2026-07-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| c148348a-68d4-3faf-b470-bede562109c8 | -13.0832 | -43.5681 | 2026-07-27 14:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 49bc6931-1a50-336b-aa7d-9cf9ccc01879 | -12.0436 | -47.7899 | 2026-07-27 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 603b433b-51d2-36f6-8c30-d95610faab1c | -12.0432 | -47.8122 | 2026-07-27 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7909dbea-8fb1-3053-8b68-7be3dc76b1d1 | -12.3216 | -47.194 | 2026-07-27 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |


[Clique aqui para ver as próximas entradas](README10.md)
