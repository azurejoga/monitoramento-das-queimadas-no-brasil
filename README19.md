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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffd85158-a629-342a-a0d5-7c1ea9a131a3 | -11.7794 | -46.4594 | 2026-06-26 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6ca68b6e-808f-39ca-ac19-163b2a2a3890 | -14.6973 | -46.1364 | 2026-06-26 14:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| cbb372f3-c958-3878-bdc0-4c6dab702912 | -9.0687 | -44.7535 | 2026-06-26 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 91c7e834-3585-31a3-9563-bc586d206c5b | -9.0876 | -44.7513 | 2026-06-26 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4c82b18d-f9bc-3ee1-bcaa-fe430000b86b | -12.5138 | -48.2581 | 2026-06-26 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6b0a440b-b688-3a0e-8c2c-110351aaa79d | -6.9791 | -42.9034 | 2026-06-26 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| e8142953-b29c-3915-b6a5-406c6c084107 | -13.258 | -54.4315 | 2026-06-26 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 219.3 |
| f8520806-003d-30fc-9c42-c3dad2566d41 | -8.3218 | -47.1307 | 2026-06-26 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| dbac4b91-789f-367f-93e6-ffc4b3e538dd | -12.5135 | -48.2802 | 2026-06-26 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 68c1cb04-d04d-322d-835b-9b5f34a42cc3 | -10.5374 | -53.7094 | 2026-06-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d15ae0b7-29d6-3be9-86bb-9ee0c1795d7d | -9.0876 | -44.7513 | 2026-06-26 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e459f876-bc91-32dc-a3c6-cb068c873175 | -9.0687 | -44.7535 | 2026-06-26 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 0a73d81c-4e31-3b5d-ab30-d67042137ff8 | -11.7794 | -46.4594 | 2026-06-26 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7c4bdad3-f16a-3268-8017-547b4c493546 | -12.5138 | -48.2581 | 2026-06-26 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 085f5583-0647-3a0d-9be4-4447c0287db8 | -6.9793 | -42.8798 | 2026-06-26 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 077d4259-1b3a-3cd4-b585-222eeeb68a89 | -13.2583 | -54.4109 | 2026-06-26 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 7880673a-59a7-3a6a-b85a-10d1bf9a640a | -13.258 | -54.4315 | 2026-06-26 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| cb170bc7-a6e3-3d33-8e16-994a1621344b | -12.5135 | -48.2802 | 2026-06-26 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4d818c26-76dc-3baa-8655-3ad28fcec62f | -10.5374 | -53.7094 | 2026-06-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 86fa7fe4-ba70-399d-8d73-1e0223d784b6 | -6.9979 | -42.9016 | 2026-06-26 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 818585be-cd9c-3061-9448-9a6e8010edfc | -13.2583 | -54.4109 | 2026-06-26 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 1c6f9722-5bb2-3416-8931-eaba0779ff7b | -12.5138 | -48.2581 | 2026-06-26 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d35e440e-9d4c-384f-9830-ad12b6aceaab | -9.0876 | -44.7513 | 2026-06-26 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b374e0ca-b87e-3206-98b4-41aba1958cd3 | -13.258 | -54.4315 | 2026-06-26 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 4b929742-ad74-3153-a309-194e7983256a | -6.9793 | -42.8798 | 2026-06-26 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 9b244f7b-504d-33bc-ae43-97918ce50b15 | -6.9793 | -42.8798 | 2026-06-26 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 3e083438-58f3-33b0-975f-9cebe751082c | -9.0876 | -44.7513 | 2026-06-26 14:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| db843641-8346-32c2-ae13-7dba9f570c5f | -13.2583 | -54.4109 | 2026-06-26 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 70006b35-10f3-3d21-9a21-68f285b8c560 | -14.0864 | -45.6203 | 2026-06-26 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1a25f711-06c6-3fe9-8116-a64937154826 | -13.258 | -54.4315 | 2026-06-26 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 9bbcb073-186e-35d1-8485-967183a7b891 | -10.7326 | -50.2346 | 2026-06-26 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d708133d-2548-3b75-929a-6ec23b203d08 | -10.5374 | -53.7094 | 2026-06-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 0b8b02aa-7796-3879-8820-b5679d9a2f0e | -13.2772 | -54.4295 | 2026-06-26 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1dd4b311-1c6f-30b9-be20-af036a840f9b | -12.5135 | -48.2802 | 2026-06-26 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 84fcaca2-0bbd-3ced-99e9-3a559409bc88 | -12.7247 | -63.0403 | 2026-06-26 14:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| f8d57c0d-60bf-3ddb-b635-7d0e21deba0a | -6.914 | -43.6816 | 2026-06-26 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 593ae029-f7ca-35e4-b41d-d6f62405fa2b | -11.7794 | -46.4594 | 2026-06-26 15:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c7556f50-bafe-30f8-bdea-b2fba777fe62 | -8.5878 | -46.9054 | 2026-06-26 15:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 48d14926-f961-35f7-9d71-8620ce412dba | -10.5374 | -53.7094 | 2026-06-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 6aeb7e4f-cc91-3bd7-b219-23616ef06ddf | -12.7247 | -63.0403 | 2026-06-26 15:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 650be175-7eca-37b1-b19c-f5851933d11a | -12.5135 | -48.2802 | 2026-06-26 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 388ec431-3917-375a-967e-3e0c99742505 | -6.9979 | -42.9016 | 2026-06-26 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 00dfc6b1-c349-3cd8-897a-e5106a723e4d | -9.0876 | -44.7513 | 2026-06-26 15:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 540932c8-534c-395b-8bb8-e9b74e8832d3 | -12.5135 | -48.2802 | 2026-06-26 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c4187fba-414d-3a38-9ddf-cdbb2fca8204 | -6.8952 | -43.6833 | 2026-06-26 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 93fca250-4286-3681-95df-183966a1b687 | -9.0876 | -44.7513 | 2026-06-26 15:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 6b1ac399-c8c7-35a4-9c11-7148170758ac | -10.5374 | -53.7094 | 2026-06-26 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e99af5de-047b-3281-8e72-a0e16f708461 | -11.7794 | -46.4594 | 2026-06-26 15:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 72944774-b590-3e2e-a3ae-762606b26cad | -12.5138 | -48.2581 | 2026-06-26 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 59c279d4-3ac6-335b-b3da-2d82a4800be1 | -10.5563 | -53.7077 | 2026-06-26 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 81a5411a-959b-3161-9ac1-06eab9df2d3b | -9.0876 | -44.7513 | 2026-06-26 15:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8347112b-a234-3470-beaf-1504d3195918 | -10.3749 | -50.1224 | 2026-06-26 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 21098a95-9db3-3d96-9932-9c2b8e5e4658 | -12.5135 | -48.2802 | 2026-06-26 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c5eabbee-fa76-3c6b-a4db-b3d1c60e689b | -10.5374 | -53.7094 | 2026-06-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5aeecbd6-15f5-3f6e-ba54-ce6124653538 | -6.9979 | -42.9016 | 2026-06-26 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 2c33be74-1c32-314f-a0d6-dd4106478434 | -6.8952 | -43.6833 | 2026-06-26 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1b96dbd9-d94d-364c-946f-02f66d344241 | -10.5563 | -53.7077 | 2026-06-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 5f1ceb01-d952-32b7-8802-b4e6e8efdeb7 | -11.7794 | -46.4594 | 2026-06-26 15:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 38a32abe-c197-35ae-bdf9-800ec7bced33 | -10.5372 | -53.7299 | 2026-06-26 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 0af9cccb-3f3a-303b-a0c3-b72532ab4054 | -10.3749 | -50.1224 | 2026-06-26 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 554f73d5-ada7-3ec1-92a7-8a387faaf951 | -11.7798 | -46.4367 | 2026-06-26 15:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| dd3e112c-3773-3593-9743-95f97816e718 | -10.5374 | -53.7094 | 2026-06-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| eaeb8a6d-6c8f-3d42-9d06-5b5e28f33f9b | -10.5563 | -53.7077 | 2026-06-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 3b774a5f-9b39-3021-bcef-595d505af726 | -11.7794 | -46.4594 | 2026-06-26 15:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 240.9 |
| c6892483-93d0-31c0-bb10-5ca38b3e782f | -13.258 | -54.4315 | 2026-06-26 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 2eb29d9f-a73f-36ac-8e5e-adb227b0d447 | -6.8952 | -43.6833 | 2026-06-26 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| dc9e93c4-5e5a-3431-97ab-b3e082d10fc7 | -13.2772 | -54.4295 | 2026-06-26 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7c474d13-9670-34b4-abf2-e0fdbe4c82ea | -10.5563 | -53.7077 | 2026-06-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 00ad47e1-ca25-3822-af9a-b24f2e256aac | -10.3749 | -50.1224 | 2026-06-26 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 20368a57-94dd-37d1-9a3c-92af304e1fe1 | -10.5372 | -53.7299 | 2026-06-26 15:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0c8efa1b-af26-38a8-a0b6-addc3cfe665f | -10.1235 | -52.1114 | 2026-06-26 15:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| adafab6a-97e7-3dbe-8ad3-9cda3c46a05f | -6.8952 | -43.6833 | 2026-06-26 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 745d606f-15b7-3763-9a5e-b3acb9021976 | -10.5374 | -53.7094 | 2026-06-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |


