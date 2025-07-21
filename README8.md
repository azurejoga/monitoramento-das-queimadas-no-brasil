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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a874e97c-9483-36c5-a48c-3874dfcf6f04 | -6.20914 | -44.30915 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c686d740-64c2-34ad-b1f5-59264b308cd6 | -6.33961 | -44.75486 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd9314b4-7d60-3195-895b-4e1089a6bb12 | -8.59782 | -48.23769 | 2025-07-21 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb62394-85ea-3199-93ca-813810c25265 | -8.08191 | -50.09996 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a0f4e3f-a021-3418-8f1d-dd4806284f7a | -7.27831 | -44.50925 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bc3e5ba-bc5a-3635-ae5b-d5054b75c110 | -12.4684 | -46.92424 | 2025-07-21 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecda7b15-5a95-3aee-bea3-e18c10ab0380 | -6.50016 | -44.81205 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a7cbd90-4743-3f2a-9e1c-bb0e1149217e | -7.05119 | -44.87477 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8438e5e-d090-3bcb-8662-67d5e273ab79 | -7.55941 | -44.5573 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00a4dac5-c42d-3457-b8aa-4d400160f044 | -9.75535 | -53.26574 | 2025-07-21 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56817e0b-82b8-3023-9d4c-05d272ebcfdd | -7.25564 | -44.28441 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3312b41c-76b0-3a75-948d-0d6357a1f658 | -11.95947 | -47.02303 | 2025-07-21 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dad063d-e14e-3f37-986c-619fdacf374b | -9.63494 | -40.60126 | 2025-07-21 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 09fdeb3c-fa00-334c-b6ff-8741b5d35756 | -12.41033 | -45.89523 | 2025-07-21 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d77832b3-3ad9-38be-a5ee-ca919001b487 | -10.14847 | -49.66212 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00b9823c-2392-3324-ba76-1f9a50385e32 | -8.55868 | -47.39218 | 2025-07-21 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92f6ee42-a399-31bc-951e-5c23bcac8d10 | -9.59591 | -48.54194 | 2025-07-21 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 799780eb-ecd3-3f92-a720-007ce57160d0 | -7.05282 | -44.8644 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3eefc43-9013-3c8d-9e14-63896fc4de44 | -7.25788 | -44.29192 | 2025-07-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4d7df4d-5791-3b72-b2d2-e7ae0d64b6aa | -5.26504 | -44.86738 | 2025-07-21 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24368c16-e1f1-378f-b6a6-302ae0e8ac9d | -7.55996 | -44.55382 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b45ae0a3-c48d-3bb0-981d-302bc6bc0585 | -6.89334 | -42.78803 | 2025-07-21 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d65d6dae-ba11-3666-b41e-54442196388d | -10.153 | -49.65815 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31314cf2-0fa4-3bc6-8fee-524543861f29 | -8.34746 | -46.63684 | 2025-07-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ed62f9a-13a4-39ee-bba6-81453fb29cf5 | -7.92948 | -43.94818 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fded40bf-f028-3eca-a3b1-e5983dfb421d | -5.61136 | -45.19157 | 2025-07-21 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29392c86-b82e-3b3c-bf8c-38610e92a47c | -7.11088 | -43.2873 | 2025-07-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 67dd9ecd-12d8-3d31-b99b-fb18dcd7787a | -6.8478 | -43.74113 | 2025-07-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f7d25fe-0f0a-3cf5-93fa-57ff484e34dd | -7.54077 | -45.36765 | 2025-07-21 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 373bf5ae-f6f0-3deb-8e39-9a9823c9f459 | -7.92244 | -43.08699 | 2025-07-21 04:19:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 015868d5-7098-3fc8-93d2-9ebd219a2737 | -11.49676 | -48.07383 | 2025-07-21 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf23d7c1-7e18-33da-af12-c4a4b03f623e | -7.70494 | -47.29182 | 2025-07-21 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f3fe217-d002-32f0-b36a-cf12e44c29e7 | -7.62895 | -44.28567 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f23267b7-99b7-3fa7-b665-743a5ae9d3f2 | -12.47834 | -45.87399 | 2025-07-21 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bf7b7cf-10fb-3eeb-a912-3dfeb65b1ebf | -7.29291 | -44.37247 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2a158fd-1af0-3798-a3be-665d9d231ea4 | -7.93003 | -43.94462 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e41ceb7-ecfc-30d1-a8f5-499d7bd34414 | -5.88638 | -45.21402 | 2025-07-21 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a69aa51-9a62-3317-b214-500cde050bbc | -9.59157 | -44.50459 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c883469a-7745-3e1e-a167-dd62a0376694 | -11.61857 | -44.22014 | 2025-07-21 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d59b030-6204-3006-87c3-8541ecc8eedb | -6.68436 | -43.00861 | 2025-07-21 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7f111df-9549-3182-b066-72ff530688d2 | -6.89391 | -42.78428 | 2025-07-21 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96b4d502-ba55-3691-a1a8-83c589d45397 | -7.94513 | -43.97984 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44946979-b5fb-307f-964a-8f5104d8000e | -8.70684 | -47.86191 | 2025-07-21 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f424427a-029c-3a62-9f1e-c2691decc506 | -6.46831 | -43.49709 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 065ec81c-2f71-33d8-b731-5c2d11718068 | -7.23039 | -44.53368 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7077a40-bc94-3d44-84c1-b6a05012d865 | -12.47779 | -45.87751 | 2025-07-21 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b3f7b21-1f08-3dfb-9020-1ee30a10c66a | -10.66362 | -46.77339 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69e8d1b6-8515-3d98-92ce-e296c4aec45b | -12.36998 | -46.43316 | 2025-07-21 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ae4abb1-2205-3785-8860-7fb85eb72afd | -10.84649 | -47.15699 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ac34821-0229-3419-a706-bd770d19fd5c | -6.20328 | -44.3898 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2301587-f9e8-3e06-86fb-c0e44bde278f | -6.50453 | -43.52113 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b0c5ae3-717f-34a1-ae6f-bbead0516789 | -8.07907 | -50.09266 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2607af5-afd8-3e26-868c-65a991b734bb | -12.13923 | -44.77493 | 2025-07-21 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| faa2209b-f6a9-3364-b23e-8776c925bea6 | -10.15676 | -49.65882 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46b0da5f-b318-36a8-b622-892aa68f3fe4 | -10.14925 | -49.65749 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc3b2a0a-a914-312d-9d97-b07e0ccb108c | -6.88705 | -42.75999 | 2025-07-21 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3788180b-ee66-395c-ab21-e68512b9d2f3 | -10.64308 | -44.48456 | 2025-07-21 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15e4a54d-7ca6-31c4-b3ca-3346a4ce942c | -8.91458 | -47.36088 | 2025-07-21 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffa98b57-26c4-3b2f-8238-d3137eafecdc | -12.38499 | -45.8839 | 2025-07-21 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d295bee2-380d-3910-a370-03c1f50dfe8d | -11.78243 | -46.4524 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06ba124d-f48d-3976-abb8-3281d64f76af | -6.34595 | -44.06355 | 2025-07-21 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d74b3b6f-f01c-3ac3-b2c6-f847767702d5 | -11.95614 | -47.02247 | 2025-07-21 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a208c5fb-e96e-3d35-9bf9-38f9bbf68f77 | -10.76805 | -46.7797 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bfa2737-5e47-3a8b-b1b4-bb958a904e17 | -8.2652 | -46.06929 | 2025-07-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a34d6be9-f745-38c0-9432-4d4bbda3f0f2 | -9.58879 | -44.50045 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 062e9b2d-a541-38aa-a167-37d4e3924e6c | -6.19942 | -44.39275 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2167a26e-2220-324d-93cb-08308f2a7cec | -8.26188 | -46.06877 | 2025-07-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5e6aa03-a43a-3eed-8c61-a138a688459d | -11.78591 | -47.55066 | 2025-07-21 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59225aa6-d2f8-3e75-9b22-65a15cca824b | -7.95916 | -43.97131 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 201bc245-5e4c-3a01-a9c1-7f1bebbd0175 | -7.27109 | -44.27251 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b26d4d-a825-3bc3-afa2-35ba16874985 | -10.12889 | -49.66339 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb429d2e-e289-364d-a2ac-718d6df87af0 | -10.68419 | -46.7731 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a90bfa5-b099-30cd-a243-7552fd718a88 | -10.13797 | -49.65549 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aac6e38-f8e1-3674-8156-db8652034901 | -7.28216 | -44.50629 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69b8994d-c4e4-372c-8275-0662e0846e1a | -7.07176 | -43.83051 | 2025-07-21 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8046f57-e5c1-3d5c-aa74-dcd974440298 | -10.68265 | -56.55035 | 2025-07-21 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80d60027-b55d-38c9-b0d9-99c6d33a13d4 | -7.26005 | -44.27794 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9cc940a-6096-3e5e-94bf-82391530bc8f | -10.65035 | -44.482 | 2025-07-21 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d0b7c80-a636-3785-a7af-faee94fe5fb2 | -6.89131 | -45.39171 | 2025-07-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5967b70b-fe6b-365f-a68c-3abfe0b88907 | -8.93516 | -44.44573 | 2025-07-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20db2163-03e7-37b6-b57c-e6b6ba3da281 | -7.0589 | -43.51347 | 2025-07-21 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 124ad4a7-25e2-3df1-b11c-d269a02e9815 | -7.92558 | -43.95118 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02b56bc9-68b6-3425-86da-254ed7f19631 | -8.2004 | -42.2984 | 2025-07-21 04:19:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0785713-3eff-36e3-8df1-a31e6027d111 | -6.75982 | -44.13148 | 2025-07-21 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90b205f5-9109-3565-b351-68631ba7a05f | -7.70839 | -47.29241 | 2025-07-21 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bea09bd-1276-339a-a71c-1c4aae49c9c8 | -12.36611 | -46.43617 | 2025-07-21 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5454c2f-6daf-3dd7-b5c9-f3ce81a3cdf8 | -12.4811 | -45.87804 | 2025-07-21 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40aca8ed-45b8-349b-ab74-187570cafd8b | -7.92614 | -43.94763 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef9d9956-fa6e-388e-a5ae-4fdb36e5aafe | -7.95527 | -43.97434 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2330f1f5-d72e-3134-b273-7cd1f75adeca | -7.26669 | -44.27899 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbfdf531-1650-30b7-95f7-ac1733fcf1c8 | -8.88011 | -46.87853 | 2025-07-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 780448d2-cf92-347e-8dd9-13f13b64c238 | -7.05336 | -44.86094 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 188ae51b-8b28-3650-8e18-ce8f472b2218 | -11.60613 | -44.23346 | 2025-07-21 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8719227-d8e0-35b6-9bfc-55858dffdc56 | -7.52181 | -46.18898 | 2025-07-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6c60547-abd6-345d-8e86-1a43086ba1a5 | -6.7423 | -44.20029 | 2025-07-21 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e5f8f5-b462-3078-a069-88e023bc256d | -11.77856 | -46.45538 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1729f3f6-2f58-3a62-bfde-dd39a799e841 | -8.00942 | -43.68823 | 2025-07-21 04:19:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a2e42e7-f6f2-38b0-b394-44a2f7b33c02 | -11.83634 | -48.20835 | 2025-07-21 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41ec77f9-de8f-3d11-a158-a59d56687fc9 | -8.5985 | -48.2336 | 2025-07-21 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2bd44e5-f677-360b-b1e9-e44087d1dfd1 | -7.95083 | -43.98092 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
