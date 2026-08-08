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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b350192-094e-3f28-a9a4-0b0100052350 | -11.2662 | -55.8635 | 2026-08-08 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 651e14cd-1fcf-3610-b91a-6584f6de2f9b | -4.3588 | -47.7636 | 2026-08-08 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9d353e33-32a9-36bd-a911-88fdc5a8d4cc | -6.2807 | -64.157303 | 2026-08-08 01:27:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 476575f0-ccd9-36b3-b179-d19563739473 | -8.683 | -62.864399 | 2026-08-08 01:27:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00820fc3-bf3b-3864-aeb9-dee1734e0a35 | -7.5444 | -61.1474 | 2026-08-08 01:27:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 755889de-6f1d-37b9-8cc4-9b3669b7944b | -8.6732 | -62.866798 | 2026-08-08 01:27:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 272a4407-b263-31f0-9505-0719416c3fe2 | -11.2531 | -55.8605 | 2026-08-08 01:27:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45b80498-a180-3035-9a73-10e5363763e5 | -6.2783 | -64.147102 | 2026-08-08 01:27:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1045ac2-9b72-3b03-99fe-060fe0179e40 | -11.2626 | -55.8578 | 2026-08-08 01:27:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8abd2d9f-dee1-3bcc-a691-f98d591d4ed5 | -7.5482 | -61.1628 | 2026-08-08 01:27:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c19f00a3-85b0-35a8-8424-6d116ba825bd | -11.2662 | -55.8635 | 2026-08-08 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 582f4a02-73db-3302-b6c5-c7d865a79025 | -4.2634 | -48.2016 | 2026-08-08 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7b920ab6-76e8-3989-90a8-ee8d0c052dc9 | -11.0334 | -44.2696 | 2026-08-08 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b9235b93-f99b-3602-9860-cf20ff09d5af | -9.3817 | -40.3252 | 2026-08-08 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| a8cf893f-cefa-3eff-9b5c-d18562b088da | -11.0334 | -44.2696 | 2026-08-08 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 16e052a7-3711-3514-b284-7f53bac17d35 | -4.2634 | -48.2016 | 2026-08-08 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7337a3d4-ab0a-3a55-9c2a-9f1d5c51a69d | -11.2662 | -55.8635 | 2026-08-08 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 80bd9e0f-68e0-3dda-b2ad-e41e0a135769 | -4.2635 | -48.1799 | 2026-08-08 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8c3bbdd7-620d-36d2-bcdc-a3b00c9a45a3 | -11.0334 | -44.2696 | 2026-08-08 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f20512ea-3255-3ecd-a06b-19375d839f33 | -9.3817 | -40.3252 | 2026-08-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 224.6 |
| b43e7e32-582a-3a3e-b452-1564d2395285 | -9.3821 | -40.3004 | 2026-08-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 07469a42-34a3-3e0c-9c58-667aab1999e9 | -4.2634 | -48.2016 | 2026-08-08 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| dcfc218f-0bef-3d2f-a4d8-1f256e58e5c3 | -9.3626 | -40.328 | 2026-08-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 85b034bf-5769-303a-b3cc-d1e10383bff2 | -18.3533 | -50.7266 | 2026-08-08 01:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e6a95337-28da-333c-afba-1935d16b6915 | -11.2662 | -55.8635 | 2026-08-08 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| da1777d8-7c17-34f1-bbee-7582dcd193dd | -4.2635 | -48.1799 | 2026-08-08 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b5ea4d55-ff73-36a5-8e0f-1e54814c3cdb | -11.2851 | -55.862 | 2026-08-08 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f51cfff2-fc13-3a51-a368-a2603265daa6 | -6.8929 | -59.903 | 2026-08-08 01:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f585f46-ecf5-3277-be8f-b6827d500836 | -8.7886 | -64.210899 | 2026-08-08 01:51:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19b8dcad-4873-32ff-8d57-f157263642de | -15.393 | -53.807301 | 2026-08-08 01:51:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b5cf8cb-0b81-3126-8d0f-d75bc181f471 | -7.5586 | -61.158501 | 2026-08-08 01:51:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5aba40f8-e4b1-350b-910a-75b9981ea43b | -7.5559 | -61.1474 | 2026-08-08 01:51:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a128432f-2d4c-3726-8377-67c5b0d1d1eb | -6.8896 | -59.889301 | 2026-08-08 01:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae807061-0fbe-3e16-a9f4-3282ca218a2d | -6.7092 | -58.944302 | 2026-08-08 01:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d021a1b8-49aa-3d06-b43d-3938760cdadb | -6.2855 | -64.144402 | 2026-08-08 01:51:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64c206c9-156b-3cdf-a8c8-68dbd3165d99 | -8.7904 | -64.218399 | 2026-08-08 01:51:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e121c68-ba69-31c6-9652-948d111f946f | -6.2892 | -64.160103 | 2026-08-08 01:51:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c29a3c22-d752-391d-ad7c-a287275fbe32 | -11.2643 | -55.8428 | 2026-08-08 01:51:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 702cfa79-94ce-3c24-9d23-98c96dc5f514 | -8.6897 | -62.8666 | 2026-08-08 01:51:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 741fbad8-c273-32d2-b198-4670b09c8c52 | -8.6917 | -62.875099 | 2026-08-08 01:51:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61d69c83-b7e1-3262-83f3-aab357d18634 | -8.68 | -62.8689 | 2026-08-08 01:51:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 994b62f6-66ea-3ecf-8797-0cfea4b8c2c8 | -6.7132 | -58.9603 | 2026-08-08 01:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5fe51e5-f308-33ca-a316-5b04e62f22f2 | -11.2739 | -55.840199 | 2026-08-08 01:51:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 182049f7-9639-339f-ab15-21c8e170dabd | -6.2873 | -64.152199 | 2026-08-08 01:51:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecb09322-9c48-3f0e-8dbd-ae8c10614864 | -11.2797 | -55.862099 | 2026-08-08 01:51:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2a84afe-1eab-3a93-bb39-23e5cbde73a9 | -11.2701 | -55.8647 | 2026-08-08 01:51:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 114fdf65-8b59-3d58-94f2-3c37850b8148 | -11.2662 | -55.8635 | 2026-08-08 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 41cb31a4-cc38-3c48-8f1d-282884a596e9 | -9.3821 | -40.3004 | 2026-08-08 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 9ac34c64-37d3-33ee-8b32-1049af6bdd3a | -4.2635 | -48.1799 | 2026-08-08 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fcbffcce-99d4-3807-9de0-7163ae345259 | -4.2634 | -48.2016 | 2026-08-08 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c66513c6-1916-35d3-9cf8-7de8c36c255f | -9.3817 | -40.3252 | 2026-08-08 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 188.9 |
| 749b16dd-f077-3cd3-b427-34b98084bcae | -18.3938 | -50.6972 | 2026-08-08 02:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 02e7648a-7150-3153-a744-0b183fd8bf9c | -18.3533 | -50.7266 | 2026-08-08 02:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 074534a2-142c-38c4-a007-7a289c80e93c | -18.3533 | -50.7266 | 2026-08-08 02:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 216.4 |
| dd07b52c-e60b-335f-8fa0-18ab8c908952 | -18.3733 | -50.723 | 2026-08-08 02:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 757e6f71-c6d1-376b-aea0-5853176ed082 | -9.3817 | -40.3252 | 2026-08-08 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.6 |
| 0a7216f1-410d-353e-b80c-81c4d349633d | -4.2634 | -48.2016 | 2026-08-08 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1fa8ffa4-872e-3522-bddb-b9d45982a921 | -18.3538 | -50.7044 | 2026-08-08 02:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f07385de-9a0d-304a-90f0-7a8cf279144d | -11.0334 | -44.2696 | 2026-08-08 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 02c719d7-9b86-39f9-8e4c-ec5b42d6bcf8 | -18.3333 | -50.7303 | 2026-08-08 02:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c026fb44-8037-3955-a3a8-984352283c4e | -9.3821 | -40.3004 | 2026-08-08 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 3ad6ef05-cc63-3055-96d2-28617035f305 | -18.3938 | -50.6972 | 2026-08-08 02:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f1b9c5f6-422a-3eca-b9ad-578cb260b036 | -11.2662 | -55.8635 | 2026-08-08 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 64efdcad-b7ea-36bb-a72e-c62bd6f1943b | -18.3733 | -50.723 | 2026-08-08 02:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 88f48236-5de3-3c86-8cf2-593702941039 | -18.3938 | -50.6972 | 2026-08-08 02:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d73631dc-136b-3cd9-83ff-d40f980e769e | -11.2662 | -55.8635 | 2026-08-08 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ca5ee009-411b-34ce-a31c-e89c9f2f2358 | -4.2635 | -48.1799 | 2026-08-08 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 54662639-473d-3ad4-8604-e884324b51f2 | -4.2634 | -48.2016 | 2026-08-08 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| fc2604ac-6ef8-3711-972f-5c83cfe459ad | -18.3533 | -50.7266 | 2026-08-08 02:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 183.9 |
| e969cc5e-ae59-3170-ae6c-02367d3f28a8 | -18.3738 | -50.7008 | 2026-08-08 02:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 63412fa3-c090-3039-9ee0-c435185eba8a | -18.3538 | -50.7044 | 2026-08-08 02:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 10c03a00-3ad6-3dbb-826e-0ab84f031dbc | -11.2662 | -55.8635 | 2026-08-08 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 65d91f95-90fd-3ddf-8092-0e9ef2bec03c | -4.2634 | -48.2016 | 2026-08-08 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1312d23e-ed20-3d5f-824c-dec85f05f4d4 | -4.2635 | -48.1799 | 2026-08-08 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a7f24f06-fb14-30dc-bb58-6029a51914c8 | -11.0334 | -44.2696 | 2026-08-08 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 9ca99b42-7fb4-3d60-b305-d5ea900f3a09 | -4.2634 | -48.2016 | 2026-08-08 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4bd6124e-b5ee-33ff-986e-dd35e102b54d | -4.2635 | -48.1799 | 2026-08-08 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4d6b9758-6962-3188-9c41-cff5b8437dce | -9.3817 | -40.3252 | 2026-08-08 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 23a5bed8-a4af-3409-86ce-c00a996f48d5 | -18.3738 | -50.7008 | 2026-08-08 02:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 06af6b28-9f7d-3013-8309-e2f81a1ea010 | -18.3533 | -50.7266 | 2026-08-08 02:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 08c46c14-9826-3bb6-bd88-58e8a0e7b298 | -11.2662 | -55.8635 | 2026-08-08 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 934c840c-c18e-36d9-abcf-ee7df7ee325a | -18.3538 | -50.7044 | 2026-08-08 02:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 331.3 |
| 83f534b6-3fbe-35bd-8e5c-ec6583afe2eb | -18.3733 | -50.723 | 2026-08-08 02:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 524673f0-688b-320e-976d-769598731882 | -9.3817 | -40.3252 | 2026-08-08 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.7 |
| bb01c472-c5d5-31b1-ae43-78912dc63ac8 | -4.2634 | -48.2016 | 2026-08-08 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 82c3885b-23e0-3f3e-99cc-4bcd4a15f442 | -4.2578 | -38.0284 | 2026-08-08 02:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 62a21962-4305-3835-b60d-d2452d539551 | -4.2635 | -48.1799 | 2026-08-08 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1a5f831c-3a15-3063-bc10-689520ea690d | -18.3743 | -50.6786 | 2026-08-08 03:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 2356f047-321d-30e5-8cd4-1ed0a6f715b2 | -4.2578 | -38.0284 | 2026-08-08 03:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 09829be3-af6d-3972-aec6-b491a6f84665 | -18.3738 | -50.7008 | 2026-08-08 03:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 1283c96e-73bc-31b8-8cf8-4a8b5f7a46a5 | -11.7205 | -50.1241 | 2026-08-08 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 13786275-aad1-3e38-95b2-7b55e5c76650 | -18.3533 | -50.7266 | 2026-08-08 03:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 448453f3-7383-3c72-b64d-952ec3137540 | -4.2635 | -48.1799 | 2026-08-08 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 40df4e2e-33d8-3447-a845-e132361d5086 | -4.2634 | -48.2016 | 2026-08-08 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 03a6e894-5894-3312-9b49-52386735c0fb | -18.3538 | -50.7044 | 2026-08-08 03:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 097661a0-e798-35de-9bc0-5593442b657b | -9.3817 | -40.3252 | 2026-08-08 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 5e038dc2-04e3-34e1-b5cf-9f6e8bf54796 | -4.89151 | -37.50426 | 2026-08-08 03:02:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b5165608-3dd4-3a15-9f34-137ff69acb50 | -4.88451 | -37.50298 | 2026-08-08 03:02:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2965a9b0-055c-33f8-ba04-4688edb933b5 | -10.45868 | -37.14825 | 2026-08-08 03:04:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0ec1788-8ad2-329d-a6e6-800a15b37722 | -10.45342 | -37.14198 | 2026-08-08 03:04:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README4.md)
