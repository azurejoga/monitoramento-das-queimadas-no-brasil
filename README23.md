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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5004e15f-2bfe-3271-b7f4-e8826c9a1210 | -8.79994 | -50.49056 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb8c796e-5a0b-36e5-98e3-7571d6f5a606 | -6.41074 | -51.68248 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d5ffd66-9243-3a5b-9b50-ed217a5f8d2f | -5.60968 | -44.00136 | 2026-08-29 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39b8d9b1-a048-300a-86aa-31be882701b4 | -11.38391 | -45.13561 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15eb7689-6488-3a88-bc8e-abadc76a9248 | -11.60583 | -46.72795 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bce578e5-0ac1-327d-8968-142acfce0a90 | -11.71342 | -37.66879 | 2026-08-29 03:55:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ea6b4034-e041-3777-a55c-367339a52b99 | -6.41018 | -51.68074 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5129063c-7457-3a21-9204-79ee0b64ae27 | -4.56192 | -44.06128 | 2026-08-29 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dcadca9-8e24-36f2-8d9b-d7acee1ae490 | -11.06881 | -47.13035 | 2026-08-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3bf61d58-ce62-3c8d-ba48-d153182a5bbe | -6.34179 | -44.08696 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6aabcb6d-e7e9-3f7f-814a-9592533ee93c | -11.34898 | -43.51095 | 2026-08-29 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07d13f85-7c42-3bea-86da-7bee5a2d7b87 | -10.82925 | -50.51463 | 2026-08-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fda7919f-a308-3827-86cc-fe87d78e758d | -10.54008 | -50.48003 | 2026-08-29 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c661111-53d2-355d-8740-3bf612508044 | -11.23949 | -45.07204 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cd37c0e-8cd4-364c-a9d3-2ca00227ac75 | -8.15937 | -46.17871 | 2026-08-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a196ba7-4ce0-365b-b7ea-b9d92535cd41 | -4.84683 | -45.39973 | 2026-08-29 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388bc68b-9158-31b2-902c-ef9110e46002 | -10.21834 | -38.52225 | 2026-08-29 03:55:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 486636bb-f7e1-3015-a560-8a97d32e2f8e | -11.03196 | -49.68107 | 2026-08-29 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f292455-a4f9-32ee-831a-a23e7e45a3f6 | -9.26854 | -45.6391 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c25930c-115c-3c69-8335-7e2d8efe609c | -8.16496 | -46.17419 | 2026-08-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6580d8e9-b51e-3643-861c-324f62f7b487 | -11.25187 | -45.07413 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c81f285d-21f2-3ae1-a2f2-d573fb935bf3 | -7.05763 | -42.1802 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d52b72cc-395d-3997-878f-e276a8833aab | -11.57957 | -45.51367 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cffd7512-3207-3761-a64d-59fb7123fa9f | -6.71259 | -44.4173 | 2026-08-29 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ab740ee-4497-3a7b-bad2-5f4cc103d79e | -5.29266 | -50.9433 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae3e604a-42fc-3465-99bf-3afd48fb763a | -7.11235 | -43.16885 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5d7d2ae3-8384-3803-87fc-af44446a364f | -6.0167 | -45.81134 | 2026-08-29 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5374a9f-7c40-3da0-a25d-08f358a7c22a | -4.56554 | -44.06602 | 2026-08-29 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 803ea5f1-982f-36ea-b86f-b88f5a02e67c | -7.21553 | -42.75724 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c8370496-d115-3c6d-bd8e-2fd3443cab1c | -5.34082 | -45.15641 | 2026-08-29 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| dd86d40a-5352-325f-8c67-33348f0c4416 | -7.25283 | -34.93718 | 2026-08-29 03:55:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d836837-ed0a-378f-a45f-d53a7f3dd8a5 | -10.75712 | -42.10338 | 2026-08-29 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c050be9d-c41e-3264-864d-b099b8e5755b | -7.07177 | -42.20938 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1baf8557-5643-3a40-8a39-8fb6f5364672 | -9.54865 | -36.99214 | 2026-08-29 03:55:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a231817-9eb8-3631-bb18-58580d8f3610 | -10.92676 | -46.61546 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5000992-e477-3beb-a2e1-6ec11b6ef4b8 | -12.43152 | -42.8901 | 2026-08-29 03:55:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c171aa8-0338-36dd-9251-cc0eccb34f84 | -5.86996 | -43.5268 | 2026-08-29 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a0f5446-91db-3faf-8630-e5bd65d5e2d3 | -7.61142 | -47.2886 | 2026-08-29 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16edc447-0558-301a-806f-07d3b4f1d366 | -8.97707 | -50.78688 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0bab88a-ae73-334d-aab2-6ad6cd2d31a3 | -9.26331 | -45.64294 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 560d6ae7-b424-3ed5-a597-8eb8267dc172 | -9.36151 | -40.49281 | 2026-08-29 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0844e7c-2e35-3aa4-a7c1-daceaa4065bf | -4.27958 | -48.19077 | 2026-08-29 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 91e45d8b-9fac-3b12-9c5a-8edc0ab09ff6 | -10.4611 | -45.14268 | 2026-08-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90a2aee4-c5fe-3574-a322-01b7f597836b | -9.42428 | -50.43616 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f455c3e-d7eb-3680-98b3-c31582e701e0 | -8.66835 | -49.54676 | 2026-08-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cd26f17-a41b-3f00-b2bb-bf4ad2024f38 | -7.28102 | -45.85413 | 2026-08-29 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8ed885e8-843f-340d-9b65-7d45012cf1a9 | -7.12829 | -42.76925 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4292525-0295-303a-b396-b45a853d3e66 | -10.83009 | -50.51023 | 2026-08-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c3131e2-192c-3466-b216-9818947e52f0 | -8.01918 | -48.00698 | 2026-08-29 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 10721956-aede-3af9-b76a-82bde7991869 | -7.07875 | -42.80938 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6a435080-1c8a-34f1-b44b-0715bed639d5 | -8.77433 | -50.07939 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 445d5d30-f72e-3301-9a85-988662e7758f | -6.62481 | -43.7371 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3599d07-a7fd-3f63-b986-2883b6cca41d | -6.33763 | -44.08617 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da031dfc-af69-35ee-b641-17ecdef4ea0d | -7.09391 | -42.21286 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f450d3c-cea3-348e-bb1b-a8e84bd52813 | -10.535 | -50.47448 | 2026-08-29 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dc96f2a-dca7-3a65-81ed-bc0a4301230d | -7.31476 | -42.96058 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d8c889b0-7af6-3d89-a88d-fbc40cf28b9b | -9.85731 | -41.72425 | 2026-08-29 03:55:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e66f718c-cb5b-38bf-92dd-fd440fe4f913 | -6.92855 | -42.68169 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 930f8119-70c2-3108-940b-0adaf32ccf19 | -5.31447 | -47.0445 | 2026-08-29 03:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e02c9a-3e03-3486-8135-c604e5b0c29c | -9.15726 | -49.9741 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e149ebdb-690a-300a-aa49-e67b0ac069c5 | -7.21477 | -42.76191 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35e63faf-1ed4-3ddc-8666-e344d87cf0c9 | -9.15644 | -49.97842 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cb30fd94-1be5-39d9-b2df-d6e661062e8d | -7.12449 | -42.7686 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dcbed136-31e9-37c4-9451-75d955981cc5 | -8.81978 | -49.63414 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45b61e87-a5f5-3593-95f4-010386ff9cea | -5.3977 | -47.85799 | 2026-08-29 03:55:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f97f3280-c85f-334b-ac78-7cbd220ca1b7 | -11.02561 | -49.68385 | 2026-08-29 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d77f79d-3944-36e2-b9a5-7755a7e8638d | -4.2789 | -48.19468 | 2026-08-29 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9c5a0a7c-9e52-3861-af95-f095b0416959 | -6.96423 | -43.78288 | 2026-08-29 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e622bd38-da51-32db-a3d8-b52be0674529 | -10.82841 | -50.51903 | 2026-08-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b22f0541-a9ca-3e85-bb88-1ebf11339354 | -11.83218 | -41.52676 | 2026-08-29 03:55:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07c0cbe1-e8c2-32d7-8ef5-a445da644413 | -7.30014 | -39.01315 | 2026-08-29 03:55:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f61f2d4-c1ff-388b-beb1-5e2cfb615d0a | -4.56621 | -44.06199 | 2026-08-29 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7e93860-1943-3f1b-9c68-d2db3f87efba | -8.66912 | -49.54264 | 2026-08-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6137129-13d9-3c12-837c-0fbe2d89bb79 | -11.4877 | -46.93832 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 676fd505-bf19-3bf1-9257-80a8ae5a1d52 | -7.17575 | -43.17719 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e924f40-89da-3450-8d86-8aee36a05696 | -9.46482 | -45.63234 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cca99183-105a-3f4f-bab4-7fefed840d6a | -7.25438 | -34.93951 | 2026-08-29 03:55:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c90e6cb2-4253-3cd0-b23e-29b7e37cf228 | -11.36752 | -45.15656 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 32877049-78fe-3f5d-ab1e-84966cd3bc97 | -7.19579 | -42.73503 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1588a7ca-e035-3bb8-b3df-b8638f3b7ecb | -7.08213 | -42.2155 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 143b9e28-f4af-3338-bbd0-52c8f05620bb | -10.45692 | -45.14192 | 2026-08-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 254b6a7e-8681-3e63-bebe-6a1966b1a413 | -5.98022 | -43.74701 | 2026-08-29 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9508a661-21c7-3aa7-89bd-6c2575c1595f | -11.48399 | -45.06398 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0079a7d-693c-3936-ae6e-84ad4414ce41 | -9.43269 | -51.6906 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e71616d-404e-344c-a3ce-68bbff4ba249 | -11.49147 | -46.94404 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34a1366f-eeca-3d23-be7f-a89ca7439e72 | -7.30374 | -49.54552 | 2026-08-29 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e281c553-7795-3669-b8b3-5c3962c42d39 | -7.52744 | -40.11671 | 2026-08-29 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 08dd02f9-babc-36de-9d46-5d053a7f54ea | -11.4905 | -46.94945 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbaca836-4682-31f1-a91e-f9109b8bdeef | -8.79974 | -50.49058 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 161e080a-9ffa-3bcf-a772-18e7d6bbf95e | -4.91388 | -43.47469 | 2026-08-29 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c03c4241-0252-3b45-a78a-25710cfb0fc8 | -10.90383 | -46.61273 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f268767-298c-3c82-81d2-90a58b3732c3 | -9.43263 | -51.69469 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9de9a745-3d14-3f8f-90d7-3fcdc07f4b4d | -9.46674 | -45.64482 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b1e705b5-389e-3d95-a318-ccf5a6032361 | -8.98249 | -50.79221 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b084021-2eb2-363e-9e77-869dabf684a9 | -8.98961 | -50.78869 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2615ad7e-51cf-3f87-944c-19bb0a5703d1 | -11.35997 | -45.15096 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06548d37-5e8f-3a9d-827d-b4b991b6f4d5 | -11.37023 | -45.14091 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 89952c5d-0546-3866-8003-dc3fd2e74d9f | -11.48123 | -46.94763 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eeaea0f9-b3b4-3c8f-9a20-fb8ff13a1372 | -8.0186 | -48.01025 | 2026-08-29 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6e89f00f-625d-31c6-9d10-e7235a8b5a27 | -7.05916 | -42.19394 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README24.md)
