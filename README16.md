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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb76bc33-48ec-3e44-8415-4d40d9a48def | -13.2678 | -51.2856 | 2026-09-15 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b7438302-6931-3784-bf1e-5c5b946211dd | -13.3059 | -51.3022 | 2026-09-15 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 4e7a8d00-d034-32ea-b10d-893124ba830d | -7.244 | -46.1603 | 2026-09-15 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 57cf45b4-39a3-3be4-abaa-fff51c2a50bb | -6.6953 | -58.6903 | 2026-09-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0e268286-47bc-3ae6-bd68-bbf40c123aae | -13.287 | -51.2832 | 2026-09-15 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 9b7c7b36-35bf-38af-a3bc-b004b4cce5ab | -3.728 | -61.7367 | 2026-09-15 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 07490c7e-1b35-3600-bd58-5b9f549e6797 | -13.2867 | -51.3046 | 2026-09-15 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 95f7c446-a740-370a-b0f5-3f5ed7af41d1 | -3.728 | -61.7555 | 2026-09-15 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 573d09e7-18ad-37e4-9423-5cecb18e75d7 | -3.7463 | -61.7363 | 2026-09-15 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e8696d30-1e84-3055-9083-f33e77c0d2d2 | -6.6952 | -58.7097 | 2026-09-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| bc1a4876-470a-3bcb-920e-7012f8c6a6df | -9.4139 | -50.1103 | 2026-09-15 02:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1819ae91-a3f0-35f5-9246-1f460cd79f86 | -3.552 | -53.9934 | 2026-09-15 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 13c506d5-2d2c-3675-b88e-eef039178f77 | -3.7462 | -61.774 | 2026-09-15 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 9e99229c-5998-366a-9a37-9bbb4018b1cd | -11.884 | -43.8142 | 2026-09-15 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 77cef96d-1143-32a1-9f1f-44c5421fdc72 | -18.1709 | -51.7685 | 2026-09-15 02:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ec8c099c-e1b3-3274-b416-b4ae9f65b192 | -11.8836 | -43.8378 | 2026-09-15 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e0e68317-9c61-37b1-9fa2-112e806c5e23 | -6.6768 | -58.6911 | 2026-09-15 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| adce50b6-3a8f-34ea-aa97-e3a1b32d7e97 | -3.7462 | -61.7552 | 2026-09-15 02:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| bf0eda0d-194d-3c1b-944f-2e5d5ef27321 | -13.3062 | -51.2808 | 2026-09-15 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 54cc8bfd-0f0a-37bf-ac0a-9e3194243703 | -6.6952 | -58.7097 | 2026-09-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| ae7bc751-9c8e-3a6d-a635-464562a2f9fa | -3.728 | -61.7367 | 2026-09-15 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6f5fc5bf-1606-3b36-890b-ac976b7a7772 | -6.6768 | -58.6911 | 2026-09-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 722afea3-1962-347a-961d-0df89806be37 | -9.5152 | -40.331 | 2026-09-15 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| d52e5394-734e-3ea1-bf26-da74cdf1d132 | -9.4139 | -50.1103 | 2026-09-15 02:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 07a025ac-74f7-3ed6-84c0-279f4483a644 | -9.5147 | -40.3558 | 2026-09-15 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 84496f21-7694-33d7-ac66-c9e513403640 | -3.7463 | -61.7363 | 2026-09-15 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f1677a28-24d5-3dbb-81cb-c2016a37792b | -9.5343 | -40.3282 | 2026-09-15 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.2 |
| a84c0410-2f90-36f4-878b-d893343047dc | -18.1709 | -51.7685 | 2026-09-15 02:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 90e8b916-9923-31fb-9d44-6e30e03945ff | -3.7645 | -61.7548 | 2026-09-15 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 850364e5-af79-356c-8ca2-f71c9b2b2a35 | -7.244 | -46.1603 | 2026-09-15 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 79d226f3-3498-3885-b462-f055ca1fd074 | -3.728 | -61.7555 | 2026-09-15 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 347cdf13-ca0e-3601-9e58-988f643ecc0f | -3.552 | -53.9934 | 2026-09-15 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| de95c96c-eadc-3d21-acf8-c5a313f7726b | -3.7462 | -61.7552 | 2026-09-15 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 64fdea7d-5aa7-3ef3-9316-fbb6f47cf431 | -13.287 | -51.2832 | 2026-09-15 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| fff57913-fd1a-3a5b-8b89-de75d734125f | -2.9025 | -50.4214 | 2026-09-15 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 27c6a1b6-bd1b-3e39-9996-fd02f51eb325 | -18.1714 | -51.7466 | 2026-09-15 02:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 27264d1e-ebd4-328a-b4ad-a4db41f3b99a | -3.5336 | -53.9939 | 2026-09-15 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6662d422-4dac-3bde-85df-334abd85825e | -9.5339 | -40.3531 | 2026-09-15 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.1 |
| eb5b80ea-9f1c-3731-94f6-ff16156654c5 | -11.884 | -43.8142 | 2026-09-15 02:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| e49eb7f1-8a62-3127-afa7-4190861017aa | -13.3062 | -51.2808 | 2026-09-15 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 318d4e47-6849-3837-9bef-184c4ede558f | -6.6953 | -58.6903 | 2026-09-15 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 769b5ef2-3597-3366-8d33-6430eb8fb242 | -7.06158 | -34.96456 | 2026-09-15 02:51:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2d53e4e2-a799-30df-a007-12051db11a79 | -7.05912 | -34.96357 | 2026-09-15 02:51:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 418b2ab6-58ff-3e82-9198-6555354d7664 | -6.8446 | -55.5611 | 2026-09-15 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 9d332031-fd0a-3a3a-ade2-2a3019f41e29 | -9.5343 | -40.3282 | 2026-09-15 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| e6b06c63-72d9-3e80-a2a1-e12c07875eba | -9.3567 | -50.1796 | 2026-09-15 03:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 18ce1a88-c717-3cef-aad9-b34fbf7e0266 | -3.7463 | -61.7363 | 2026-09-15 03:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2d7c9b0d-791e-39ea-8f64-99ceea1f5eaf | -9.4139 | -50.1103 | 2026-09-15 03:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9ae42c1a-6b84-3e0e-a313-0d68e137d192 | -7.2438 | -46.1827 | 2026-09-15 03:00:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 65be3f24-823e-3217-b72d-1d16ec2caf30 | -18.1709 | -51.7685 | 2026-09-15 03:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1b8696ef-a383-3e71-8f52-1114f09d0af7 | -6.6768 | -58.6911 | 2026-09-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 46595622-cdae-34e7-a22a-b6a071316795 | -18.1714 | -51.7466 | 2026-09-15 03:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 42d58c56-c1e9-3ca3-9929-300b19b5d9dd | -3.552 | -53.9934 | 2026-09-15 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 4454ab34-6105-35e5-8957-b3beaa8a25e7 | -2.9209 | -50.4208 | 2026-09-15 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 10f939d8-5a9b-3229-8324-b8ff7a39b1ca | -6.6953 | -58.6903 | 2026-09-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1cdf99bc-4841-3c6d-9718-b4191db51850 | -3.728 | -61.7367 | 2026-09-15 03:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 6b6abfe0-222c-3bd6-aeaa-cd965d5e0be7 | -6.6952 | -58.7097 | 2026-09-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| d993ef4d-60f8-3d69-a3b3-f02c0e7032b4 | -3.5336 | -53.9939 | 2026-09-15 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e06f9bb1-3cdf-36fe-b82e-418d53de360e | -7.244 | -46.1603 | 2026-09-15 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 2fcfa262-2ce5-36ab-80c6-a1d958119307 | -7.2253 | -46.1619 | 2026-09-15 03:00:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 390b641c-26ac-3353-a870-33bdd72f892e | -9.3572 | -50.137 | 2026-09-15 03:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 083cd2ec-7999-3b64-9731-32350f123e0f | -14.2046 | -47.4265 | 2026-09-15 03:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2eda1c7c-94b7-3b3d-b8ee-ecef6f20df19 | -9.3569 | -50.1583 | 2026-09-15 03:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3cb9152a-64d6-3df9-a195-ccc90da2b9c1 | -3.7462 | -61.7552 | 2026-09-15 03:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ae805bb0-4d4c-3b0c-a677-3583c5e5afc0 | -11.884 | -43.8142 | 2026-09-15 03:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| ae3cc2fd-0fa2-3586-a27f-3991798db44b | -3.728 | -61.7555 | 2026-09-15 03:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4b96ecdb-e9ac-38d2-a73a-d9a64c1f1220 | -2.9025 | -50.4214 | 2026-09-15 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2ac13b98-44b7-30cb-85a7-1e3854822b7c | -7.2438 | -46.1827 | 2026-09-15 03:10:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| a65f606e-25cc-3118-bfc8-8514e3794db4 | -6.8448 | -55.5411 | 2026-09-15 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| adaf23df-8aa9-3373-bc52-932976718008 | -2.9025 | -50.4004 | 2026-09-15 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0ae40bd4-cd88-3ed9-b447-d7fc6479ab13 | -7.244 | -46.1603 | 2026-09-15 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 4dbd8372-2f9c-30bd-88b2-ec3774a70aa3 | -3.7462 | -61.7552 | 2026-09-15 03:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4af78505-ccf5-3fa2-a27c-2e689dedee1e | -3.552 | -53.9934 | 2026-09-15 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| e7147303-a4f7-327a-a2e3-8387b3d34f7a | -9.4139 | -50.1103 | 2026-09-15 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| ec2c7071-1b74-33a7-8f59-8aff5d765fb4 | -13.2232 | -51.6744 | 2026-09-15 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b1b321ed-cb55-3150-b23f-d0732695dabe | -3.728 | -61.7555 | 2026-09-15 03:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d7630d5d-2834-3055-9fd2-4eb0ce5688a3 | -13.2235 | -51.6531 | 2026-09-15 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 68689f08-d80a-3518-9ed5-71658e80f094 | -6.8446 | -55.5611 | 2026-09-15 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a11ac143-9f99-37dd-b32d-8124b0a81c60 | -2.9025 | -50.4214 | 2026-09-15 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 83ba3492-4c0a-37eb-9c19-25eefbf2deca | -7.2253 | -46.1619 | 2026-09-15 03:10:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 12458cf2-7a5a-394e-bc4f-a9df5142ca85 | -2.921 | -50.3999 | 2026-09-15 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9d7ae89e-8e1d-33b4-b4cc-5efbfb456b5a | -6.6768 | -58.6911 | 2026-09-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 70260f22-6238-3209-99e6-5db2f2c68bb0 | -6.6953 | -58.6903 | 2026-09-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4b365178-2284-3054-a02b-2ee5be4b587b | -7.2628 | -46.1587 | 2026-09-15 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 90e53649-1dac-3e67-bc7f-c6de65d085a1 | -11.884 | -43.8142 | 2026-09-15 03:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f35b39e7-911e-3809-8b0b-5387298e80a3 | -3.728 | -61.7367 | 2026-09-15 03:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| d1eaf038-3fe6-37b0-a7ac-93dfc504c25a | -18.1709 | -51.7685 | 2026-09-15 03:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 29ef78f9-0dec-39e7-a304-71e4190c66da | -3.5336 | -53.9939 | 2026-09-15 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e0a6800c-3371-3112-890e-923397954b3a | -13.2678 | -51.2856 | 2026-09-15 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 64d9b597-238e-300b-8ffd-16972acc4497 | -2.9209 | -50.4208 | 2026-09-15 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 857e8a03-6485-3dde-abff-518bb48d749f | -9.3567 | -50.1796 | 2026-09-15 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 4321cbac-07a9-3b1f-b80d-f30ff03aaff1 | -9.3564 | -50.201 | 2026-09-15 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| fed14c72-50d5-3d86-bb0c-2f8f65c2002d | -13.2427 | -51.6508 | 2026-09-15 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 37e5f72a-69d4-3f7a-b835-797e89ae11a1 | -18.1714 | -51.7466 | 2026-09-15 03:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d8b39778-27a0-3e18-9212-3f7654422c8c | -3.7463 | -61.7363 | 2026-09-15 03:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7f4c5cbc-81fb-305c-a753-3d7a486cbb92 | -3.5336 | -53.9939 | 2026-09-15 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a2243454-b726-343f-b44f-9ba2f6d0305f | -13.2235 | -51.6531 | 2026-09-15 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| d1995ed5-78f8-3e07-9bb0-a2af16d91360 | -6.6952 | -58.7097 | 2026-09-15 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1f7b5b57-e27f-3554-9e2c-e8f52f4dbe9d | -13.3062 | -51.2808 | 2026-09-15 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1c1a7e90-7b55-3b79-be47-16b4d49fe24b | -3.728 | -61.7367 | 2026-09-15 03:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |


[Clique aqui para ver as próximas entradas](README17.md)
