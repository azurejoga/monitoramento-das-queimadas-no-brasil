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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 832a7d36-18d3-31a5-9b53-30e2c0a8a963 | -4.88242 | -41.30419 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d7c01910-d9e9-341f-bf45-8fa1ef5ec320 | -4.857 | -41.30467 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b262bb4a-0ef6-3d11-a4ed-63d0118ea8c8 | -3.98255 | -41.52079 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 314949e0-0f3c-3d31-8ea2-4e602ac35f40 | -3.97712 | -41.51471 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 20f35ef2-6b99-347a-b87b-bab7c08eee8c | -4.86982 | -41.29665 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b600a67a-02b5-32ec-953a-90e330ff827f | -4.86759 | -41.30904 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7f74ec9c-e814-32b2-83bc-8bea27962bcc | -6.90466 | -43.55223 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1176fc9a-252e-31f3-9444-f94b1f49bd88 | -3.97507 | -41.51368 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 064584fc-18cd-35dc-b956-833711ba58c7 | -4.87387 | -41.27414 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| af8e4dd7-567b-3391-8279-ab00a84d0766 | -4.86828 | -41.31269 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 00312be3-7815-3bb8-8fb4-795f1c5ab13e | -6.9091 | -43.5658 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be403688-cc76-309b-a69d-02e1e3718daa | -4.875 | -41.30307 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 88394aaf-3e05-34a8-8eea-7b51464fe38a | -3.97965 | -41.52496 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d88adca8-96ab-3399-9a92-ee06dda46b76 | -7.21665 | -39.77472 | 2024-11-30 03:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3a954da5-0264-3cc4-b51e-b83289d2d97c | -8.80696 | -37.12153 | 2024-11-30 03:21:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 96cc9296-1ef6-3cb0-9d23-03d2cdc8e2c5 | -3.99574 | -41.50671 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d541ec42-ad4b-3e9c-a47b-ca66a3d2da4f | -4.83397 | -41.2554 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7790731e-0249-32ef-9ead-1d1dbbea1294 | -4.69953 | -42.38862 | 2024-11-30 03:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f060781c-bc01-3a11-92b0-e18cf35bb091 | -4.87712 | -41.29817 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 52c23f14-5ba4-333f-8a35-7308ae87088e | -3.98526 | -41.50552 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 74445bcd-d7bd-3fa3-aebb-77794fb40f20 | -4.86686 | -41.31309 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b69a35cf-165a-3d1a-abb5-0d5443b87c57 | -4.87354 | -41.28224 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| d2d8c30e-4caa-3a1e-b6fa-dbe1e70b11de | -4.85852 | -41.2959 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6562df69-7933-38d8-a435-393e74623100 | -4.83485 | -41.2504 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f219ab95-e314-3559-8882-659d7bb4dcc2 | -4.88166 | -41.30862 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 98b37d6f-9764-306d-950b-d21d789c6fb4 | -6.90382 | -43.55121 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ff95f26-4236-39bd-8f88-5fc9939eb56f | -4.85577 | -41.27526 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a8912bcc-9240-3e82-b798-e148b5968030 | -6.13386 | -43.95382 | 2024-11-30 03:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d870ff35-3fbb-3224-bd7f-525f7072d8f2 | -4.85559 | -41.30531 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 542f29e2-bfdd-3b15-a731-029bb2a80b75 | -7.21698 | -34.99046 | 2024-11-30 03:21:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b76852a3-4118-3a52-bef4-c3aaa3d7846b | -3.61719 | -42.73657 | 2024-11-30 03:21:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57da8925-bb08-344f-a468-554d457db484 | -6.9103 | -43.55957 | 2024-11-30 03:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 403ec2e9-bb7a-3ad4-8e8e-adc6bc05b3c6 | -6.91975 | -43.54119 | 2024-11-30 03:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 59b94c16-a5ff-350f-a7be-29aa2ab91cde | -4.87142 | -41.32302 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d48291e8-8411-39c9-9069-8263cf9b4790 | -3.98943 | -41.5056 | 2024-11-30 03:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 59fb00d0-a46e-3778-a3c7-798d85b53f4e | -4.884 | -41.29499 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e04ad3bc-05fc-35e3-b688-00a7717ae865 | -4.86864 | -41.26807 | 2024-11-30 03:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f5611225-f44f-3f78-b631-ca8a9e709fb8 | -10.44954 | -44.94808 | 2024-11-30 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 371ea4df-e762-3a1a-ac16-ed525a688016 | -9.65138 | -36.1247 | 2024-11-30 03:23:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5134c586-8d0f-313d-89cb-bed88670e5bf | -8.37927 | -44.47385 | 2024-11-30 03:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68633730-4ba4-3b05-85ab-808d4a072e63 | -10.45135 | -44.94796 | 2024-11-30 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b30e522-11cf-3ea6-b214-79e6f9cf0f8e | -11.07891 | -44.31465 | 2024-11-30 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c14b833-8498-3116-9584-7d47793df810 | -8.37794 | -44.48059 | 2024-11-30 03:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1240ead0-28e8-3ef9-bb8a-9dcd7e1b72ed | -10.2199 | -36.65639 | 2024-11-30 03:23:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6215a0cf-db71-36c6-8418-df925464b627 | -10.21923 | -36.66013 | 2024-11-30 03:23:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bc1dbff3-9bad-381b-916a-91d141e5ba14 | -10.45272 | -44.94121 | 2024-11-30 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f10010-7e2f-35ab-8994-24c9327b81c4 | -10.6932 | -40.33255 | 2024-11-30 03:23:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a52aadc2-dbea-34f8-9e99-57fc98cda68a | -10.75362 | -40.44118 | 2024-11-30 03:23:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47612f7c-90df-304e-bc76-3c34d08e7d22 | -10.75289 | -40.44506 | 2024-11-30 03:23:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42aadab2-0325-3614-a8f8-3f2a6c7a286f | -10.75888 | -40.44221 | 2024-11-30 03:23:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f19c8e30-4a3d-3a8b-bb5b-b3e4e035a6dd | -10.69902 | -40.33038 | 2024-11-30 03:23:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1d20281-136a-3fdf-b01c-db6f159c4ab0 | -10.69843 | -40.33355 | 2024-11-30 03:23:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44c71101-eba2-3ed2-afd3-7606616c7177 | -10.45095 | -44.94134 | 2024-11-30 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6070523-0509-3be2-8121-b80a1d9e9db1 | -9.10223 | -43.19604 | 2024-11-30 03:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 770c439f-5bef-3e22-b3e1-aefb8cec34af | -10.75825 | -40.44559 | 2024-11-30 03:23:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37410944-7615-3b64-ab33-44819daa053d | -9.10217 | -43.19803 | 2024-11-30 03:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5db1a3e0-e218-3ed7-b7c3-f5b7a459aff9 | -9.44864 | -35.92285 | 2024-11-30 03:23:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9ce31ba8-bc0c-3ce2-b107-54af391f3189 | -9.64735 | -36.12403 | 2024-11-30 03:23:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c51d4f16-bed7-3744-a023-50b78963d2bd | -11.07771 | -44.32055 | 2024-11-30 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6ff335b-fef8-3463-b15d-aebcb74e7341 | -11.07103 | -44.31933 | 2024-11-30 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d7d5c90-d6d8-321a-b5ed-7c4140594bce | -9.13937 | -35.78306 | 2024-11-30 03:23:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c55e05f0-2e2a-38aa-8a2c-1d13abbd9b8c | -19.71692 | -40.35438 | 2024-11-30 03:25:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| abf16903-7213-360a-ad8a-5e7f052a1c8e | -19.17242 | -40.13673 | 2024-11-30 03:25:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 3be2e777-9960-3290-ad48-de66156c6d5f | -17.67568 | -42.74432 | 2024-11-30 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0c1b0f2-42a4-36e1-a04d-d08fbd86ad3b | -19.71913 | -40.35656 | 2024-11-30 03:25:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76716fab-8603-3abd-ab01-8ee979704f27 | -18.31063 | -43.30089 | 2024-11-30 03:25:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56943e3a-0ad3-327e-bdd5-fea8ac2c2074 | -19.17152 | -40.14132 | 2024-11-30 03:25:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4b9bd33f-80b4-3c58-a5ba-3b0ce2f59610 | -18.31606 | -43.30241 | 2024-11-30 03:25:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f6914c9f-7347-36d2-924e-90196e2e0256 | -17.39644 | -42.65864 | 2024-11-30 03:25:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20b94480-b1bf-3e63-ac26-08b9933ffd63 | -17.6654 | -57.5645 | 2024-11-30 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 8a474c63-e982-3bfe-ba6e-af7b0cfa08e7 | -4.8713 | -41.2915 | 2024-11-30 03:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 29c26488-ceb4-3b61-a3a2-c8269ed8b693 | -1.6419 | -53.8731 | 2024-11-30 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 693b97c9-7acb-398c-8bdc-0dd6d55afba9 | -3.259 | -53.6388 | 2024-11-30 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| efc733d9-bb43-39db-9c31-3acd6fefce2b | -3.6758 | -47.1176 | 2024-11-30 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 06c3ccd8-0af7-3c23-b85c-84b41e50cede | -3.2591 | -53.6186 | 2024-11-30 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e978b5f7-e39f-3edc-ab5a-a74091073afb | -3.0171 | -45.0974 | 2024-11-30 03:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 76f09915-1ee2-3e71-b9b5-84db730e422e | -1.6938 | -46.7833 | 2024-11-30 03:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a8b0daab-4e9a-318b-8bbb-a4985e906093 | -3.4791 | -53.8142 | 2024-11-30 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 991c77ec-dc4a-37ce-be49-8f8e9f089db7 | -3.6757 | -47.1395 | 2024-11-30 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a2418fac-dbbb-39e5-a71c-dec7d150280f | -3.0689 | -50.3326 | 2024-11-30 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 19c3b06e-ed15-364c-9e1f-7b86539b327c | -17.6651 | -57.585 | 2024-11-30 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| b1829873-0662-377a-bfa2-3bd45da42a3c | -4.8715 | -41.2674 | 2024-11-30 03:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 979220e6-93ba-30d6-a98d-d003724116af | -3.4975 | -53.8137 | 2024-11-30 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9dd940d0-99a8-333a-b993-7a4fd99faa37 | -3.2406 | -53.6393 | 2024-11-30 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8371e88e-504a-3e9e-bddf-0104894c9d92 | -1.0733 | -53.6378 | 2024-11-30 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3c6c47f1-0bff-3ac5-b695-1529469abc40 | -3.017 | -45.12 | 2024-11-30 03:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1aaeed31-90f9-3fec-9535-35aee899c4d1 | -3.0356 | -45.1193 | 2024-11-30 03:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 56b07f27-5a8c-32b9-b83f-8dd1b5bcb0b1 | -3.4975 | -53.8137 | 2024-11-30 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2151f36b-68be-359c-97ea-ee6a4decaf6d | -3.0357 | -45.0967 | 2024-11-30 03:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 82870aae-f36a-31c9-9d29-0f9117107021 | -6.9344 | -43.5401 | 2024-11-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3febef0d-bea2-37d6-ae22-1e8163ec6ce4 | -3.259 | -53.6388 | 2024-11-30 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| ca0dd907-13c1-3ef9-ae26-1dfe342d7cf3 | -6.9153 | -43.5652 | 2024-11-30 03:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| ff92e2e6-cafa-304e-aacf-1c6e16102e60 | -17.6654 | -57.5645 | 2024-11-30 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 8146ad13-8306-3d13-b7f3-ba4f0debb700 | -1.0733 | -53.6378 | 2024-11-30 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 893577b3-f142-3538-b5de-83e11d2ac634 | -3.017 | -45.12 | 2024-11-30 03:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f6e08013-c78b-3755-92f3-1c58db02653d | -4.8713 | -41.2915 | 2024-11-30 03:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| ebd58f71-4f49-386a-9a0f-6840ef796560 | -6.9156 | -43.5418 | 2024-11-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 421.1 |
| d9404d7b-b4db-34b8-b67e-fce8199c3ae8 | -3.0689 | -50.3326 | 2024-11-30 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3ae83f8c-6925-32d6-ad45-6b1ccc5f1bc7 | -1.6419 | -53.8731 | 2024-11-30 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 37a2ac46-5efa-3486-9645-65282f0fda6b | -6.9158 | -43.5185 | 2024-11-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |


[Clique aqui para ver as próximas entradas](README16.md)
