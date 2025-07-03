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
| ff32cef4-bec1-3024-9b66-0c0cf2ba9315 | -6.28733 | -43.68503 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8e056be5-50cc-3ffa-8275-b65c684fd005 | -3.29283 | -49.19695 | 2025-07-03 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4aa9c4c-7ec8-3d0c-a3dc-da18bf6d38e5 | -7.21173 | -43.17414 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cf8a17f-3a03-33de-bb44-ec82b326b2ab | -5.4975 | -44.38911 | 2025-07-03 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c40e944-6990-387b-ba27-a7f4ac780361 | -7.21933 | -43.06429 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d507ca5a-b994-3d00-b97a-3968fcec0d47 | -6.70971 | -43.18001 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 604be217-c3eb-352b-8a8e-1932995de37a | -6.69058 | -43.17186 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5f20e750-8fe4-3512-80d3-6e0860c5dc19 | -9.51952 | -45.43959 | 2025-07-03 04:34:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9d94014-af3c-3f5f-b52b-4b4237deeecf | -5.99462 | -43.74241 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| e2bbcc6e-0104-3f37-8c6d-c9ddde70bc34 | -4.40114 | -47.63095 | 2025-07-03 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59a896a9-ddbd-3d83-8c2f-48a273db4469 | -6.19294 | -42.64491 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 47727c59-7385-3fb0-bd0a-583c05fa854d | -4.39782 | -47.63044 | 2025-07-03 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4141f5ab-81aa-34b3-8ee0-463301d16aaa | -5.90741 | -43.4471 | 2025-07-03 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a498300c-dc1b-36ef-b33a-6541827538da | -7.09447 | -49.16997 | 2025-07-03 04:34:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fda14e82-d661-3f7b-8ef7-53c1cbc9101f | -5.7208 | -49.10622 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73656d6c-159b-3368-80c8-3dbdca517e95 | -2.92394 | -47.81074 | 2025-07-03 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4f7508a-912b-3f03-b6c2-34c0c5e82b54 | -7.23042 | -43.07323 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9c817492-a974-33af-9b46-4cb0daeb46b1 | -5.87626 | -50.14549 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 26c46b1e-e6b4-3191-8dd1-3702950fa821 | -6.96128 | -42.87763 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 92fc53b8-0c70-3499-a5d5-e4de71e93ec3 | -7.61117 | -45.75361 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 054d0420-e8fa-331c-8f27-e6449fb727d9 | -6.29571 | -43.68142 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 62335e2e-6395-3b22-89c1-7768d9193cea | -6.54046 | -55.04663 | 2025-07-03 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ce4cff5-0692-37f3-ab46-978e73371006 | -7.22791 | -43.062 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 639373f6-de1f-364e-98b7-7aef6877c90e | -5.07762 | -42.51143 | 2025-07-03 04:34:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de609ae3-830b-3eb3-bde6-b444cfe36756 | -4.2814 | -48.19214 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3bb680c-28cf-3e47-803e-3761d466130d | -6.9643 | -42.8854 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 8ea413f8-fb21-3cce-8301-5db0315b1f45 | -7.61235 | -45.74586 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ee6fa61e-cb35-38a9-a212-02fae6a78fd9 | -7.23093 | -43.06971 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 34d40216-e0dc-3eb3-9006-b89f4eb6c6ba | -4.38325 | -41.91391 | 2025-07-03 04:34:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16e7e9f7-10a9-334a-bf6f-b07169b50c1c | -6.29187 | -43.68087 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 56970028-3f64-3723-832e-016182a82606 | -7.22035 | -43.05719 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| f22b34d3-94a7-3923-9b8c-155573708d4f | -6.5358 | -55.04582 | 2025-07-03 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72184ef4-ac70-3eaa-b864-77aed2c118c5 | -6.53832 | -55.03125 | 2025-07-03 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d46ef489-b69b-399f-9cbb-3e6e24d2200a | -6.17169 | -48.05633 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8d440c82-1973-3c7e-ab83-c4d3698ddc46 | -7.67172 | -44.65766 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 761f0873-90cf-3a3d-ad8e-ae6673effbd8 | -7.60826 | -45.74918 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ef20425-e187-30ba-a3a9-9afdd92b5398 | -6.6108 | -43.89703 | 2025-07-03 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b58d11e-5ccd-3ba1-ad0c-b05ee7323482 | -7.61176 | -45.74974 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a15304cc-60a4-3fbc-8d07-2c1c948f3351 | -6.96483 | -42.88181 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| b1231da4-4834-392b-9d98-5417f2e678dc | -8.43525 | -49.20266 | 2025-07-03 04:34:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88b64628-8ab7-39ca-889d-b06b84fe1141 | -6.70159 | -43.15229 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54cbb25e-33df-3c30-8c56-808a1e74ae0b | -6.69286 | -43.15631 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 12.3 |
| a3cbc480-071c-37a2-8539-cc4aee5b0013 | -7.19533 | -43.58963 | 2025-07-03 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957df8d5-980d-3a3e-95c5-5eb9570c3f9d | -5.39867 | -43.24619 | 2025-07-03 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 78386937-cd23-3d10-b62b-1ca4da09564a | -6.95156 | -42.88724 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 7cb3ddf1-7804-3100-b160-56d95b5e0d5b | -2.89221 | -48.03154 | 2025-07-03 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e038889-c535-32bd-acb6-aad530a4a7c3 | -8.58701 | -48.21197 | 2025-07-03 04:34:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1afc3368-4d50-33ca-8a08-82643b37e12c | -7.20338 | -43.08763 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb980075-56dd-3ab4-908f-cf1386337b52 | -6.95616 | -42.88425 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 1978b077-f6da-377c-a285-9b54fe63a138 | -7.40197 | -45.42186 | 2025-07-03 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78343adf-97be-34e9-857d-6dadadad7fbe | -6.60275 | -43.03442 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57bc3450-b48e-3e70-a752-e74647a44cee | -6.2842 | -43.67973 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1341eec0-3609-30ad-ad79-69d872737e77 | -7.2575 | -44.33675 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6aec9d6-3fcf-3c4c-94e4-fa7f0e9ed59e | -6.28873 | -43.6756 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d9ddf3f3-52b8-3466-ba92-4aa2b8a023eb | -9.24616 | -48.74996 | 2025-07-03 04:34:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5adb30a6-2f70-37bb-bd84-6a1f0c0d5d3f | -6.00294 | -43.7389 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 287bbf99-494c-3655-ab48-075dffe39d83 | -6.20618 | -51.45191 | 2025-07-03 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a432d15-e151-3574-8e08-3809c6a5e32e | -6.94908 | -42.87576 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0e6bb79-c166-3d53-a2de-740a6310a427 | -3.60228 | -49.44984 | 2025-07-03 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea237d4f-ec9c-3bc4-ad66-9ffc7cde36b1 | -6.91122 | -43.05094 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 709a29d2-ec75-3a2b-bab7-ecd586a006cb | -5.99533 | -43.73774 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| abdcc3d0-d2c6-35dd-b657-5d23e61e2225 | -6.94803 | -42.88298 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1386e292-0a16-3ca1-90ff-0d77847b78dd | -6.33559 | -43.75444 | 2025-07-03 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 740f355e-38db-3157-ab0e-898e308c588e | -6.18146 | -42.61003 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2959d9bd-1fcf-30b8-9ceb-f77dcbbf0664 | -6.95261 | -42.88003 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 0e1cbbd7-72bb-375d-894a-1caed9d159a9 | -6.28803 | -43.68032 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 00cfced2-7b99-387b-8b1c-6e54d0882639 | -6.18165 | -48.05791 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e930c19a-1e38-39be-bf5a-dcd6e0c199e6 | -5.40255 | -43.24681 | 2025-07-03 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dfb640f8-af6e-3431-8fb9-7636b6a1a203 | -6.72228 | -43.15015 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95df1b58-c325-34a8-90a2-d46bbd91efb1 | -6.20804 | -43.35969 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51b0f7a0-53c0-3986-b50f-e3b1108b13cc | -6.1957 | -42.64567 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2417e9f3-954f-3fa4-b1de-1f160fee7f65 | -7.22337 | -43.06491 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bd6e034d-8a33-3c53-952b-c34b37181fe6 | -2.90895 | -54.4856 | 2025-07-03 04:34:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 407f9f2d-c1a7-3a43-a8a5-5a88bac92b7b | -7.84017 | -46.87772 | 2025-07-03 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf4f8f6-8102-3d64-98a6-1015bd33ec4f | -6.92752 | -43.88846 | 2025-07-03 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b064a95-f32d-31f0-88dc-c7d285652b22 | -6.96378 | -42.88899 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 09b2cac3-4ae0-31c0-a480-ea1dfafca173 | -6.72305 | -43.14498 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 928ae095-7123-3b97-ad8c-0cd982a77493 | -5.49413 | -44.3897 | 2025-07-03 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b6f057-c70a-333f-8248-68a172f221d8 | -2.91111 | -48.23693 | 2025-07-03 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f9f8b81-f549-36fe-802c-964045d11c5b | -6.92823 | -43.88375 | 2025-07-03 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5620a5b-b337-34cb-ba7d-673e164426b1 | -6.71769 | -43.18106 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 92da0f81-a5d3-30d9-985a-2f72e8606c17 | -6.29954 | -43.68201 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 597bdf2f-c97d-3827-834a-0ab405d1f5d8 | -6.4635 | -43.72773 | 2025-07-03 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f7f1d5d-3ade-3860-bd9c-d7410c997395 | -6.9597 | -42.88842 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| d2761c8a-e424-3cc6-9e3b-9b2c5859bd6d | -6.60699 | -43.89653 | 2025-07-03 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| afe4ad73-0433-3a49-a3bc-e80ff5da9e53 | -7.60885 | -45.7453 | 2025-07-03 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abfa3546-ddef-30a1-9f23-06aea91405a0 | -4.53925 | -48.01876 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcefb127-2ff3-378a-b60e-55dc36e43be0 | -6.19756 | -42.64198 | 2025-07-03 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed7e7af2-098e-30c7-bb77-6690d019c3cf | -2.91727 | -48.24152 | 2025-07-03 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b2b37e0-37bd-3e8e-a9b3-ec40dea16262 | -7.22439 | -43.05781 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 2671f271-d7e9-3544-941a-bbf3d6b408ee | -6.95563 | -42.88786 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| bf700919-edbe-3ef5-8daf-62b9b6e5287c | -6.69685 | -43.15688 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a2723fd2-7dde-3a2d-bc14-e7b988eea935 | -7.67477 | -44.66251 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0883975f-59c1-3933-ab9b-983cf9786726 | -8.31967 | -42.21497 | 2025-07-03 04:34:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 910cbb0a-80cd-3ed8-bf8f-bc6a0c86c0c4 | -6.9475 | -42.88659 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6dfe14af-b9e1-342a-8ced-ff95153e849f | -5.87564 | -50.14935 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03e4b691-b521-3b6e-bd23-0027140eaaba | -6.58506 | -43.04337 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a81b4ada-6f1f-3226-bdea-e431b0e8b64f | -6.58431 | -43.04852 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd58f6b6-0573-36e1-8503-5e123a1e8fef | -4.02853 | -48.06324 | 2025-07-03 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73160b52-87ae-31bf-9221-c17d4733d2eb | -4.03186 | -48.06377 | 2025-07-03 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
