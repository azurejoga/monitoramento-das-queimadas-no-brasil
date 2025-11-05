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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c257a3-7d42-3ba7-874a-e060a88beb22 | -4.29506 | -43.79473 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98486110-7bbc-3dc9-889b-c837c176ad77 | -5.28365 | -43.62641 | 2025-11-05 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd121137-a629-338e-9d34-bb41aaa5fcc1 | -3.96551 | -41.81866 | 2025-11-05 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1ebe77b-46bb-30d4-81a0-fdad95454c13 | -5.12916 | -40.62646 | 2025-11-05 04:12:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48f0fef9-9a78-3142-b1b2-46df0d3c32cb | -4.3562 | -45.7628 | 2025-11-05 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c925f4fb-1aaa-3ed7-a5ee-648a01e1963c | -6.11988 | -41.63407 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26f117f4-b886-3d65-b184-bfab1df94449 | -4.50238 | -45.43689 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fd920a1-b02d-3ec6-967e-9641c0ccaf56 | -6.13686 | -39.76365 | 2025-11-05 04:12:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| defe5823-da12-3557-9ac9-2c6512dfc963 | -3.80977 | -51.29124 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c92bd19-62f3-35a0-af39-5a4cb9982567 | -2.97785 | -48.70595 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f26c83b-e742-3c85-a537-6eb8455d7e53 | -2.83908 | -49.41107 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30441c4f-9fe3-3cb5-a5d8-4b604a1d752d | -4.00323 | -45.2963 | 2025-11-05 04:12:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6cce76-4d5a-3b65-b388-eaaa51359ad0 | -5.03637 | -43.62343 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eef7d30c-b0fd-3197-a7d9-de1fb7630c51 | -4.02797 | -47.95891 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aea6a569-f122-37d9-b4ad-a12d29097f7f | -4.29841 | -43.79525 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 455e546d-9a7d-3f22-a12a-85481a847cb7 | -5.26476 | -44.81475 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bd822e4-34c0-324b-a5c3-27f4503b59bf | -4.5782 | -43.34009 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7a5e4bc-2639-3933-9c77-5a0291b72840 | -2.97343 | -48.70523 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678551ea-1238-3211-b784-157c7c48672f | -4.06515 | -49.36248 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36ef3fbc-9083-3d88-9116-c3998859edac | -4.94857 | -48.10016 | 2025-11-05 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6cfe38c-c9cb-3643-ad70-f65a7b2f0eab | -1.21453 | -49.13977 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdd57d37-c0fb-386f-b03a-0bb2bfeff166 | -5.14919 | -41.22107 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4da9df00-6af4-38cd-856d-552dfc3b5916 | -6.04178 | -41.04628 | 2025-11-05 04:12:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec436a87-4be4-3a04-ad2d-281b0aa74bec | -1.28959 | -49.15195 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bc1b85e3-d043-304d-850b-35bb9537b66d | -3.48881 | -43.63185 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23c83ccb-439d-34f6-ac9e-c2c8fb2a0656 | -4.47315 | -43.23067 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 438e97d6-5471-3060-9966-bfda44131d06 | -2.58019 | -48.40617 | 2025-11-05 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3917a381-0a62-369e-ab22-8dffffaa1d9e | -3.7967 | -44.03937 | 2025-11-05 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26ba7d27-63bf-3e32-ac77-c6e44ab2c8e1 | -1.29349 | -49.15768 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d3a90141-c6d9-3b0c-92d4-e74ef63a239b | -3.58743 | -50.17071 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93656975-bb6c-3f21-be64-61a2a8704c18 | -3.49683 | -49.55875 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec2ef9eb-bfe1-35c3-8c21-b9b16a1c9c1d | -4.04548 | -43.48449 | 2025-11-05 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1d6868f-cc1a-3ec0-b656-01a8799ac344 | -3.47428 | -43.63684 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e47e34a0-3363-312d-8554-f14485110d79 | -6.1044 | -41.71219 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fdad28e5-7acb-3374-9ab3-5962530778fc | -2.42425 | -49.30451 | 2025-11-05 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91ec4b41-a9e9-3b97-8368-3ad95fd2f223 | -5.94389 | -40.57203 | 2025-11-05 04:12:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7d8f199-78e7-3442-a405-d86730a9b918 | -2.83361 | -49.4152 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d2e9c18-3f7a-3d65-b10a-62d6027d8680 | -5.51428 | -41.14721 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3245a0c1-7fb6-3098-96fe-11e7d70a5b94 | -4.67049 | -45.76672 | 2025-11-05 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257d9260-550c-37fd-920f-236e99fdbd1e | -6.10039 | -41.70111 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c52eb9c4-9f99-37bb-9d79-88270238c47e | -4.71521 | -46.43563 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eecb5121-6187-3ad3-a766-fd4125748614 | -5.78021 | -40.81198 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5db55874-d5f9-3959-ae22-aaac130e9178 | -4.33388 | -45.87924 | 2025-11-05 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3488ad09-d348-3c93-a64a-4eb8e04a0119 | -2.79168 | -50.32091 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d4728b80-2b32-365e-bedc-8ce7f2139ee6 | -3.13438 | -40.98925 | 2025-11-05 04:12:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d66ab3a2-e3ec-35b7-982b-7760dcdc39c7 | -5.92622 | -43.36892 | 2025-11-05 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4e45d6d7-aa2c-3ec0-8a66-ca8734877654 | -4.91749 | -47.32629 | 2025-11-05 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 220847cc-4a3d-3b5f-b592-b93d8b413d26 | -4.47038 | -43.22669 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2fc27127-d44d-3685-99b1-c45625915db0 | -2.65385 | -48.50845 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 55224518-7ac5-372c-a7ed-c7573f99b9d2 | -6.135 | -41.64753 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2a806b0d-1bd9-377d-b909-d6f41d09ad87 | -5.62222 | -41.08529 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5594f94-f49e-3328-beee-3a402148251e | -5.55393 | -44.76074 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53e0b787-97e8-34f1-b979-b8b343f3d167 | -2.6199 | -49.22751 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5304eea-cd86-351e-8407-cb4b5fbac6a7 | -4.71075 | -46.43953 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c273e26-6c99-33a1-8599-74d30fc61eb5 | -1.26614 | -49.14812 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4b6fa63-49e4-3514-ab19-7b9c1a0d4cb9 | -4.71149 | -46.43504 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a006199-0713-3928-aa8e-99303f8cb9f0 | -6.1277 | -41.62801 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2728dcc2-6831-3f39-bc8f-35e244e25bfe | -6.1027 | -41.70101 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b249c82f-a2ea-3e24-a3dd-0b5df7771a5b | -3.56981 | -50.64711 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 384d00c6-a4a5-33f7-8722-897e1a523e52 | -3.4821 | -43.63079 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d4d1937-3bee-392f-99af-20b26117791e | -3.88453 | -42.52627 | 2025-11-05 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 51ecac54-727f-36ee-8d30-db634d1b4d8d | -3.31479 | -53.85006 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0d05035-6c45-366c-9294-37bfed195752 | -4.41834 | -48.94309 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b3d67a3e-b54e-32f7-b5c2-eac53e11b33a | -4.86797 | -43.05576 | 2025-11-05 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7db4cbf-7ee1-3c4e-bc37-4f1d2d3eb92c | -6.66229 | -34.97387 | 2025-11-05 04:12:00 | NOAA-20 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| bb68ff48-2bf1-3682-b040-c8a4dcdfe96c | -2.84295 | -49.83384 | 2025-11-05 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd37adec-bf27-396e-a2f5-cc72f28edadf | -5.92236 | -43.37185 | 2025-11-05 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1fb7b962-091a-3d4d-b6f9-fc94a181e2ee | -4.58207 | -43.33714 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6de9b323-30bf-3b85-a931-73c4cd2d24d8 | -3.79612 | -44.04298 | 2025-11-05 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8c9b972-a91b-316f-960f-ac4a4a6e3546 | -5.42927 | -46.40494 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c9e7893-09f7-3eb9-8514-619a047d6bdc | -2.61892 | -46.8546 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c9ee847-9879-397b-a088-a5e61b7548fb | -6.12393 | -41.69693 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a7ed820-596f-3b0d-9008-52e1668234ed | -4.45724 | -46.63468 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6f45d52d-367d-3f64-a0bd-15505b16b4cc | -5.03249 | -43.6264 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ae33bcd1-d1ac-3ec7-899a-361fd396e472 | -4.45346 | -46.63406 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| caaa5cf5-f40d-3bf2-aa18-e4367564ce19 | -4.58119 | -46.29901 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce6ab82a-90eb-3ba4-bb50-cc2c4390903a | -4.47858 | -45.9822 | 2025-11-05 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17be44a4-66fe-364e-a00d-e889b1cd6bda | -4.58151 | -43.34061 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ce27f7c-a195-3068-8c57-4452de782717 | -4.86404 | -44.62262 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d97adcd-1a7f-3b3a-90bd-991a0663389b | -3.49282 | -50.45795 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1576ceca-01f6-38d5-a535-3694b8bd97b6 | -4.27516 | -44.40158 | 2025-11-05 04:12:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ea6585-81be-3a3f-97c1-e6fd1bcbd3d1 | -1.20984 | -49.13901 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5805eba3-7342-3a28-98fd-84b49dca10af | -4.31049 | -41.45733 | 2025-11-05 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad711712-ad70-37f6-a6f1-fcc3afeae5cd | -4.6077 | -42.85213 | 2025-11-05 04:12:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27986572-3af9-37f2-be1f-43595f5178ad | -3.22213 | -44.40559 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad5570a-d45d-35c3-90b5-089f746a5fd5 | -5.05148 | -44.19221 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0ac5ca9-3732-3a79-8158-64b7dc2a648c | -2.61911 | -49.23229 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30c57299-57e4-3309-8649-9c5052787dae | -5.03581 | -43.62692 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f4bf88b0-7689-366c-b9f6-e745ff2ba1cf | -6.09313 | -41.7036 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c97c7dd3-6338-3d13-8369-7c28c40392a8 | -2.79262 | -50.31526 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 89620629-efa4-3947-94c5-5829113e6df1 | -3.49683 | -50.46466 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cee16c42-dc11-3031-8f80-55ef7d746864 | -5.26947 | -44.14538 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 486267dd-64bf-372c-b664-edd06299c5c6 | -4.67007 | -42.71774 | 2025-11-05 04:12:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 024903bd-044e-3bf6-a9ea-2b23ac90baa0 | -2.26663 | -47.85616 | 2025-11-05 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b11f238-c1aa-360a-afea-f8cabc601ebd | -2.78861 | -50.30874 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4782657f-ca9d-3874-ae34-a6a58588c770 | -4.55174 | -46.76678 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b707b561-c790-3f4d-9791-1c7d5d836b80 | -2.42504 | -49.29965 | 2025-11-05 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca7e39c0-15da-388d-8b5b-50f02a367c68 | -5.26725 | -44.13767 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dec487c-4702-3d46-a2e4-0446c40d918b | -4.28332 | -46.93213 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b37efb95-e057-331b-8302-d8fabfb1e5ba | -4.54173 | -40.64212 | 2025-11-05 04:12:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README23.md)
