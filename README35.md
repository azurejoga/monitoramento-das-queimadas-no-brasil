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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 841e21ae-83aa-369c-94ec-9d7ee4fdbf62 | -10.80344 | -43.9503 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d57a46-8ec5-3355-b705-9b92678ec532 | -7.56298 | -42.68491 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7435aa40-7685-386d-96cb-b2b9690d7da0 | -7.55797 | -42.69321 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9cf1528e-7b00-32f4-a183-5390caa72fc9 | -7.03088 | -46.25419 | 2025-10-14 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ee2052f-76e8-350f-9fbf-c39dd581248b | -7.26893 | -47.90734 | 2025-10-14 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45990ce3-209c-375e-9a9e-bb485fb5d3a5 | -7.42367 | -45.41801 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 803dc644-7f93-33fd-9099-881b744b8d2d | -7.75142 | -45.73193 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dde1334b-8a3a-3c50-9918-e368690afdc5 | -7.9415 | -44.11143 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 365325c2-5f7d-3db9-8578-f0917cae129c | -8.53388 | -44.58636 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08656335-9380-3d1f-affd-9ceea595f867 | -10.04 | -43.81073 | 2025-10-14 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0495a0d9-c979-3dd5-89f5-5531f2d740fa | -14.75519 | -40.6115 | 2025-10-14 04:25:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2dba88c-7005-37aa-a14c-17e97806c50c | -12.63045 | -44.12409 | 2025-10-14 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae8e434-6689-3e05-b3cb-c82def0b3d72 | -11.29643 | -44.02925 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7b8b859-a00e-3a23-ba12-77620dc62d6f | -15.31845 | -43.09784 | 2025-10-14 04:27:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 207d6a0f-aa53-3e2e-8142-d87d26654733 | -16.08063 | -41.45311 | 2025-10-14 04:27:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ad4ed35d-0e9c-3414-a826-b3bb4c191f16 | -16.35179 | -42.38338 | 2025-10-14 04:27:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f6ebda-67e4-34ee-8260-25164d775188 | -15.14888 | -56.45264 | 2025-10-14 04:27:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8446f7de-5c2a-3251-a7e5-9c497496ced6 | -15.66287 | -43.90484 | 2025-10-14 04:27:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0de8d28-980b-3e79-b395-8dfc6ae319e8 | -15.37672 | -43.04072 | 2025-10-14 04:27:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 11855219-1280-3158-84fd-cbf285e42a16 | -15.14774 | -56.45841 | 2025-10-14 04:27:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e372c4d-229c-3c52-8b62-c7bc765062c9 | -15.3727 | -43.0401 | 2025-10-14 04:27:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 475d0612-5ebd-33d6-993d-8e2847ac1943 | -15.37135 | -43.03974 | 2025-10-14 04:27:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 422aea69-2da6-3d5d-80ea-1b28987a95cd | -16.26066 | -43.18145 | 2025-10-14 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b46bc3c-2367-3fd7-93aa-a0b5237233dd | -15.31445 | -43.09727 | 2025-10-14 04:27:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c91e85d-a541-336f-adc5-532df2425f5a | -15.0298 | -42.26093 | 2025-10-14 04:27:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1adc8e50-9922-319c-9b1b-b37ed425f754 | -25.85784 | -50.4031 | 2025-10-14 04:29:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 619be67c-b25e-3a06-a773-2a722aec88b6 | -27.44256 | -48.44872 | 2025-10-14 04:29:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 998129ab-2374-3fd2-982f-75de22fdaf05 | -25.85452 | -50.40248 | 2025-10-14 04:29:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ba34ef9a-443a-3b15-b1e4-517b06fd2374 | -27.07244 | -48.97128 | 2025-10-14 04:29:00 | NOAA-20 | GUABIRUBA | SANTA CATARINA | Brasil | 4206306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 72ca4e38-5958-3f04-97ac-c226724ecde0 | -7.9442 | -44.115 | 2025-10-14 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d8516e4c-ee82-36e7-bb8d-aa20ee49cc5d | -4.6696 | -43.1326 | 2025-10-14 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9a9740d3-df93-3729-a273-e919ac8c3183 | -29.62543 | -49.96914 | 2025-10-14 04:32:00 | NOAA-20 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| a41e15eb-c05a-3684-b760-5b1f22d1f755 | -28.67603 | -49.40266 | 2025-10-14 04:32:00 | NOAA-20 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f195f053-fbc5-3808-bf7a-ab6a62a64367 | -29.66598 | -49.97886 | 2025-10-14 04:32:00 | NOAA-20 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 2b101535-455f-3cb4-b49b-b15b50fe8efc | -28.59166 | -53.62365 | 2025-10-14 04:32:00 | NOAA-20 | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf443555-0c4f-3412-8fba-bc26726c14bc | -12.8376 | -50.6547 | 2025-10-14 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a469b87a-da65-3c2a-aaa9-8b5ccea7f6d6 | -4.6696 | -43.1326 | 2025-10-14 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7c5f0d60-64dc-3ddf-8ef5-813b4aadbcde | -12.8188 | -50.6356 | 2025-10-14 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9a7113e8-056d-3dd1-91f6-562e75bf7b52 | -4.6509 | -43.1337 | 2025-10-14 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a0b71a68-bb81-333a-93b7-8f63caff6e50 | -12.838 | -50.6332 | 2025-10-14 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 37d16663-e203-3902-bd0e-c1a2be01627b | -12.7996 | -50.638 | 2025-10-14 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 46e9f864-7a3f-3c45-aaa7-040ea4cf8328 | -12.8184 | -50.6571 | 2025-10-14 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6b194b76-f3fe-3d64-8dfd-5b1101b4dd7e | -12.8571 | -50.6308 | 2025-10-14 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0aa4ffb5-22b3-3d79-a8a4-abc2e358d4fe | -7.9442 | -44.115 | 2025-10-14 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e0d11a8b-9914-39eb-b03c-7b5a9217fe6b | 1.75724 | -55.81094 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17cb4420-5dc4-391a-9218-6070aea4eb9a | 1.10243 | -50.98701 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ece7ef69-d5f1-3d63-9517-37005eca75ef | 1.89817 | -55.66562 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 873ae981-d2ee-3dfa-a895-fe3b9c36ba3b | 1.45067 | -50.84925 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fba97442-1e8f-355f-a15b-b3a73a4c3488 | 3.8671 | -60.05522 | 2025-10-14 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4075fa1f-0661-319d-bae8-86bf23812b71 | 1.89482 | -55.66614 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe48ef78-5b26-345a-b4ab-af2e26c26c3c | 1.09438 | -50.99271 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e9215f7d-06c6-39ee-a11e-2ef4b5804f4c | 2.18303 | -50.93516 | 2025-10-14 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e4d618c-0e77-3970-8cf9-9de27984bba5 | 3.86775 | -60.05944 | 2025-10-14 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0eaa71d2-8940-31dc-8c6d-6b7dfcd50d3d | 1.11049 | -50.98135 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb99adfe-7b19-300a-8b9b-de0006d34b2a | 4.35379 | -60.75668 | 2025-10-14 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d30df139-fd24-395f-afb4-764d19de86af | 1.09507 | -50.99694 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8393fd23-a41b-37f1-b519-38ed118ca9ca | 1.74889 | -55.82309 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45b2b1e1-8440-3ff9-a6aa-a7c3cf107428 | 1.75279 | -55.82611 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac15474f-6253-3d3a-aa59-b0ea0aaa5bc0 | -0.89996 | -47.54789 | 2025-10-14 05:14:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 73fc5271-6f18-3663-8113-f23b5293b70c | 1.10379 | -50.99551 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2971326-7b6f-3515-bbf0-1c7e76f86247 | 1.46346 | -50.87342 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f21d117-7a93-3873-a74d-ae16f9d3d635 | 1.45975 | -50.87838 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c04598e-c0d0-337f-8e4c-c873dfd3e85f | 2.2342 | -55.94216 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3295543b-cf92-3220-9104-6fa0483cfd28 | 1.09943 | -50.99623 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f6f9dfc6-385b-3306-9ab0-1202ddb2a347 | 1.75335 | -55.82964 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e90a84fd-00a6-39e7-a116-caaad119bab8 | 1.88085 | -55.68653 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcbe7bf3-71a3-309d-8156-36875c3c3c64 | 1.88811 | -55.68904 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cef3b38a-475d-3e21-8332-d0a0941dbb2d | 1.10612 | -50.98207 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d66527d-04ad-39a6-b3b9-3bf6011e144c | 1.75446 | -55.815 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cec9359d-910b-3590-add4-7aa2ebd3029e | 1.12697 | -50.94374 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 391299f5-2308-312a-b776-7fb2d3ec74a2 | 1.75167 | -55.81905 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7845980-87b4-3c73-b8e1-a3ee0d0874c5 | -0.89936 | -47.55185 | 2025-10-14 05:14:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4e651605-72d0-3fd6-9d16-1a38eba7eb1f | -0.90056 | -47.54396 | 2025-10-14 05:14:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ab6643e9-639b-3f83-a7ca-a2cac96022e8 | 1.75223 | -55.82258 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8556e70d-0794-3129-8b75-f06a9b7b6e6f | 2.1837 | -50.93928 | 2025-10-14 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5f8f6ab-5dc9-375e-9558-5106a6050eb4 | 1.89426 | -55.66257 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5371fd49-03db-3b3d-a2a1-ac3931be533a | 0.85218 | -52.51566 | 2025-10-14 05:14:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e82290e5-d24d-39a8-b5f9-b4e5f6cf6eb4 | 1.09875 | -50.99198 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a5201cc2-4fbe-3d5c-8c65-5adde29f611e | 1.75947 | -55.82508 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fa90f9c-0791-3926-b37e-e3c62831a366 | 1.1068 | -50.98631 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2756d7c6-e413-3fbf-afcc-a8dc6b4156b7 | 1.75 | -55.83016 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c1e3f6-2cb5-3e2f-973d-b83f3ee1b668 | 1.74945 | -55.82663 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3667b2f8-1abf-3210-bd1d-48bc8784f61b | 1.89762 | -55.66206 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f6a4169-e888-38cc-ae99-d3c04f3287bd | 1.75111 | -55.81551 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9450bc-e564-33e7-b4c4-f56e9acf5ee6 | 1.88476 | -55.68956 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66bd869c-98e9-391b-b2ef-609f3d5a901c | 0.39147 | -51.03039 | 2025-10-14 05:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b725c73-a49c-3d25-a778-b9142a1f8008 | 1.75613 | -55.8256 | 2025-10-14 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2877452e-33a7-3663-9f2c-14dc953442e9 | 1.10311 | -50.99126 | 2025-10-14 05:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1dfc34d-634b-3bd7-a391-49e90a2c2ce5 | -3.28769 | -52.547 | 2025-10-14 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ac8311-270e-319f-9b8f-ace699ccfc34 | -2.5336 | -47.80134 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 201bc964-c0b6-30a5-8f73-42b411c6b0f1 | -1.89675 | -51.0127 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7f8df64-bfd7-3831-89a0-2a686a6aae22 | -4.10859 | -50.05305 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19a4364e-6fc4-39cf-837b-957cc23d0284 | -1.96115 | -50.80761 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 657ed065-fcd7-3b5f-a9f6-9c8bf61e0018 | -1.54095 | -60.18896 | 2025-10-14 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cbabbd5-61c0-39b8-adf5-5539f30a5a7d | -2.83655 | -48.83432 | 2025-10-14 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f054386f-a239-351b-9420-b968f818cc03 | -1.9604 | -50.81245 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f90cf43-7ba8-3368-a190-fb34a9950918 | -4.70726 | -55.9868 | 2025-10-14 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61c117cb-e692-3f27-9c59-cf7f1fbc01d0 | -7.74542 | -45.72447 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 24c6cf84-54fa-3c60-b624-740485d043b0 | -2.18988 | -54.47945 | 2025-10-14 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b77bde8f-fc3b-3240-b25d-9d9514732748 | -1.59859 | -55.15053 | 2025-10-14 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
