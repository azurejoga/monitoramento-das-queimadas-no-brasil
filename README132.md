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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abc2a735-bd59-3849-a9df-df1d4d352022 | -10.912 | -44.6816 | 2024-10-14 12:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d7b2df7c-5f38-3a03-a75f-57698c722a1c | -11.245 | -44.1924 | 2024-10-14 12:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 398f6c52-8d86-3e4d-afe7-f60bf40b8b46 | -10.349 | -46.6002 | 2024-10-14 12:26:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3bc24502-3a25-3e54-8611-0184af608fde | -10.8925 | -44.7074 | 2024-10-14 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1d4b3dfb-c7f1-398f-af09-fefba75d3aad | -10.912 | -44.6816 | 2024-10-14 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 46795d06-622a-32aa-8fb4-860c4d44c2a0 | -10.9116 | -44.7048 | 2024-10-14 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 4c915090-6c37-344c-98ca-7a4a318d1875 | -11.245 | -44.1924 | 2024-10-14 12:26:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 22965780-6ab9-30fa-8cee-d1b8aa4082e7 | -11.4602 | -43.9263 | 2024-10-14 12:26:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 36ae7adf-b13f-3123-a541-425fd4395ef0 | -11.4794 | -43.9234 | 2024-10-14 12:26:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| f73fd1c5-1cd8-3cc9-9519-faf05e4f8800 | -11.4597 | -43.9499 | 2024-10-14 12:26:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| ee587158-70ba-3d11-8055-382d948f3e11 | -9.9411 | -47.2949 | 2024-10-14 12:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 58efae32-d395-3fbc-bc73-62be9684e65e | -9.9392 | -47.4281 | 2024-10-14 12:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 08ef2a52-3463-3542-b832-2abeaceeece2 | -10.0622 | -44.2391 | 2024-10-14 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 86b74651-79af-3a44-84e9-d402cfbf5b6d | -10.0626 | -44.2158 | 2024-10-14 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ea0d75cb-6605-30f8-8fbd-cf4459816221 | -10.082 | -44.19 | 2024-10-14 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 180.8 |
| f3e41c96-3a7a-31e4-8f51-eaed7a24ffc1 | -10.0816 | -44.2133 | 2024-10-14 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 316.9 |
| bd37f613-5cfc-38df-8fa4-8f4099fcc337 | -10.0813 | -44.2366 | 2024-10-14 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 4210b0b9-b199-3af8-b527-125d6966fa2a | -10.0629 | -44.1925 | 2024-10-14 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7ed4822a-ca76-32c9-8780-08c743fd0a2e | -10.349 | -46.6002 | 2024-10-14 12:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 99cc6807-b9cb-3618-aa64-543e69128616 | -10.3303 | -46.58 | 2024-10-14 12:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 351109a5-d75c-3f26-826f-a3300fccf365 | -10.9307 | -44.7021 | 2024-10-14 12:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 379132ef-8c4b-3f01-878d-0e813b723cb0 | -10.8925 | -44.7074 | 2024-10-14 12:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 7fe9b5b3-a178-3a8c-b5aa-fe92195d9307 | -10.912 | -44.6816 | 2024-10-14 12:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a1c4ed9c-5fc2-3199-a3d0-e949e2f10155 | -10.9116 | -44.7048 | 2024-10-14 12:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 854fe51d-74a8-31ad-99c6-bc3ca48b7fc8 | -13.3889 | -44.694 | 2024-10-14 12:36:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2682aeec-c577-3512-85ef-aa3a617a86c9 | -21.5414 | -48.0108 | 2024-10-14 12:37:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 47b6d392-76b9-3c59-a35c-a07644df0806 | -9.7825 | -46.4651 | 2024-10-14 12:46:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6bf693b0-1995-3959-84ae-9bde1084a3fa | -9.9411 | -47.2949 | 2024-10-14 12:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ee5cac78-1d02-306c-9856-030325c0e5a3 | -9.9392 | -47.4281 | 2024-10-14 12:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8c3adb2d-0a15-3f3c-9ae4-6ec8e703f3f5 | -10.8925 | -44.7074 | 2024-10-14 12:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e2105c42-dc00-3a0f-9d44-5adeea4381c6 | -10.9307 | -44.7021 | 2024-10-14 12:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 02874bb8-3483-33dc-92a2-4bd23a47ff3f | -10.912 | -44.6816 | 2024-10-14 12:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8ed4b801-bc97-3959-805c-03ea07a243c5 | -10.9116 | -44.7048 | 2024-10-14 12:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 193.6 |
| d3b02ff5-5bf8-3cb3-9904-a34b99aee5f9 | -11.4597 | -43.9499 | 2024-10-14 12:46:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8f2ae6d7-47e4-35c4-a9e1-dd26ce8835d7 | -10.0439 | -44.195 | 2024-10-14 12:56:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9cd757d8-7b5b-3b07-bdea-83ee4d9d7096 | -9.997 | -47.3551 | 2024-10-14 12:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 1f478b19-5491-3766-acee-3408689d21de | -10.082 | -44.19 | 2024-10-14 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| d8620387-5e3f-340a-9ee7-3a1cb54c4982 | -10.0629 | -44.1925 | 2024-10-14 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 92b11ef7-55cb-38aa-8823-f109c6297297 | -10.0626 | -44.2158 | 2024-10-14 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 1a7b5cfc-8caa-331d-a66f-533226a3734c | -10.0622 | -44.2391 | 2024-10-14 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 972e7e27-22d7-396b-a5e5-68c4a8cfa5cf | -10.9112 | -44.7279 | 2024-10-14 12:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b4515504-f67e-30d5-8c77-f3358eb74d22 | -10.9116 | -44.7048 | 2024-10-14 12:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 361.7 |
| 88a7d05d-3030-3493-8439-b19004088839 | -10.9311 | -44.6789 | 2024-10-14 12:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7ba23ce1-4fe1-3eef-b725-70558ac16f1e | -10.912 | -44.6816 | 2024-10-14 12:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| d0badb62-a8c3-3d03-b2a3-aa296407af15 | -10.8925 | -44.7074 | 2024-10-14 12:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| afce4f1a-1cb5-3b3c-8579-3e0c97545be7 | -10.9307 | -44.7021 | 2024-10-14 12:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| a278fbb5-de1e-3c9e-8d55-4a470409cdad | -11.4597 | -43.9499 | 2024-10-14 12:56:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1d3bd963-9a6b-39b0-85f9-ef62d8e1e77c | -13.3889 | -44.694 | 2024-10-14 12:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5da7e727-5db4-345b-8200-f2706fd3d418 | -13.817 | -44.5961 | 2024-10-14 12:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a04e5364-d177-32a9-9d0c-4fa6dd5adb46 | -17.93 | -57.38 | 2024-10-14 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bd31957d-6e92-3734-83c6-e2b0307b64f3 | -10.06 | -44.26 | 2024-10-14 13:04:28 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c768d19-7df9-3a7b-8823-13701faebe68 | -10.05 | -44.22 | 2024-10-14 13:04:28 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 676a7082-92bd-3234-95d6-e1e1f9ec516b | -10.08 | -44.22 | 2024-10-14 13:04:28 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51550a76-f75e-375d-af11-d7ea5ee1c515 | -10.04 | -47.33 | 2024-10-14 13:04:28 | MSG-03 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eba3504c-cb16-39e1-b62d-3c73d042ce9c | -9.72 | -46.46 | 2024-10-14 13:04:30 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f8a3e81-c9aa-3bb8-b8b7-75085b9e55ac | -7.57 | -42.51 | 2024-10-14 13:04:41 | MSG-03 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51d6f314-dfb3-3101-b2ec-811f54917b64 | -9.4888 | -45.8228 | 2024-10-14 13:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 406f63d1-be77-3168-b9e4-fa8d1c2957d3 | -9.4885 | -45.8454 | 2024-10-14 13:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 77e7ecba-5322-3e1a-8efd-f61d5748b709 | -9.707 | -46.4513 | 2024-10-14 13:06:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3ff0c84a-51d5-3b77-a449-1dfe1398d0c6 | -9.997 | -47.3551 | 2024-10-14 13:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 94ca1c2d-c48f-34e2-b9e0-f77df7341b27 | -9.8504 | -47.0162 | 2024-10-14 13:06:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5544b573-2ccc-3882-af76-651ece64d59a | -10.0432 | -44.2416 | 2024-10-14 13:06:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| cd0e465b-c12b-37f5-81a1-6ab386ca6ea6 | -10.0439 | -44.195 | 2024-10-14 13:06:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 681d5412-3a91-3cda-9ab0-79260225b0e3 | -9.8501 | -47.0385 | 2024-10-14 13:06:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 47bbc63e-934e-32b7-926e-8ea60e70449a | -10.0629 | -44.1925 | 2024-10-14 13:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 0d7ae41b-73d7-3e8c-b3c1-1c1e604a8bcf | -10.0633 | -44.1692 | 2024-10-14 13:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 58718ca2-4519-35b5-b8d9-4ec7ace37291 | -10.082 | -44.19 | 2024-10-14 13:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 625401d7-493d-39e7-ba0a-083116ea6ce7 | -10.0626 | -44.2158 | 2024-10-14 13:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| fac8636d-db7d-38a3-ba84-89b449ba552e | -10.0622 | -44.2391 | 2024-10-14 13:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 226.4 |
| cf8ab8d6-14fe-30b2-bc34-477396f89ff9 | -10.349 | -46.6002 | 2024-10-14 13:06:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| bad4db1d-4aed-3f81-9821-59f79a0db3a6 | -10.3493 | -46.5777 | 2024-10-14 13:06:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9f058029-cf63-39ab-8af3-ac8a7eb809e0 | -10.6795 | -47.3419 | 2024-10-14 13:06:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e3dc988b-26b3-36d7-8e16-8f07c069ea37 | -10.912 | -44.6816 | 2024-10-14 13:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| a6c9a6de-f717-356c-820c-626e1cd553fa | -10.8925 | -44.7074 | 2024-10-14 13:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 17998b5c-1434-3573-8ed5-1d1a2e4f68e8 | -10.9307 | -44.7021 | 2024-10-14 13:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 54ad9133-aeb5-359a-8527-568ba87e8e20 | -10.9116 | -44.7048 | 2024-10-14 13:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 5076c528-9e2d-3e71-860a-87af832057da | -11.245 | -44.1924 | 2024-10-14 13:06:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8ee2043c-232a-341e-a85a-85a699151cf9 | -11.2476 | -51.3283 | 2024-10-14 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 26a035fa-cf90-3007-85a8-4fc433a2b40c | -12.5962 | -44.7783 | 2024-10-14 13:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| af7c6c5e-71ce-3124-ba7f-34a48505809f | -12.6159 | -44.7519 | 2024-10-14 13:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| eebea84b-0305-3283-86d5-fbf62129e553 | -9.4699 | -45.8249 | 2024-10-14 13:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| f422310d-5830-39dc-8c17-2bbb5aa2f88f | -9.4885 | -45.8454 | 2024-10-14 13:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cde39d43-01c4-30f4-8efe-a3abf3f70243 | -9.4696 | -45.8476 | 2024-10-14 13:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f4df00b6-f879-3351-8c83-9e18bf5bf0fd | -9.4175 | -45.5134 | 2024-10-14 13:15:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5ad320ed-52da-38a2-afb2-73feb937755d | -9.4702 | -45.8023 | 2024-10-14 13:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2e2537d8-8d5d-36b5-95e5-487ec393812e | -9.4365 | -45.5112 | 2024-10-14 13:15:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 11ea10fe-f65b-3128-9c6e-1584758adc0e | -9.4888 | -45.8228 | 2024-10-14 13:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 857ec6f3-e5d9-3f52-a1c1-fb8a3f88bd67 | -9.5648 | -44.4873 | 2024-10-14 13:16:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b7fcb089-4cdb-349d-a798-09e8a2f8879b | -9.8504 | -47.0162 | 2024-10-14 13:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b476904b-b942-3f0f-9641-53d9b9dbb5ba | -9.9222 | -47.297 | 2024-10-14 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| acab97de-66d6-3abe-8b07-77a3482e9d52 | -9.9408 | -47.3171 | 2024-10-14 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| c7d03fdc-a8e9-3d76-9764-2a09b7cb0cb5 | -9.8501 | -47.0385 | 2024-10-14 13:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 617af735-87e3-373e-b869-9693bf4d165b | -9.9411 | -47.2949 | 2024-10-14 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 28adfede-f6b9-3cc4-99e5-9b76dbead3d7 | -9.9414 | -47.2727 | 2024-10-14 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7d693ffc-ffc0-38eb-af6a-0b6c5b006ab1 | -10.349 | -46.6002 | 2024-10-14 13:16:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 04fae1b5-2f69-30b0-a49f-a013ad2d8b9d | -10.3493 | -46.5777 | 2024-10-14 13:16:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6661d5ae-caea-3535-a1fe-30a4a59236cf | -10.4716 | -49.9624 | 2024-10-14 13:16:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| aed4e896-ac83-38bc-8b08-d12cc4032ec4 | -10.6795 | -47.3419 | 2024-10-14 13:16:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| fe48d338-5c6e-30bf-9de1-f59a5e799cc3 | -10.9116 | -44.7048 | 2024-10-14 13:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 21c2eb51-ab98-3b87-9da5-e56e6d04dce7 | -10.9311 | -44.6789 | 2024-10-14 13:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |


[Clique aqui para ver as próximas entradas](README133.md)
