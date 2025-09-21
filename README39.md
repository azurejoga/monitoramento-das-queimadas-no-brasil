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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a5c27cc-05f5-3a6f-aa46-89ff4f222464 | -12.71987 | -46.84466 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ac921adb-de65-3ba7-9034-55d64804ca28 | -12.70828 | -46.83773 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ec8bb95-5dbe-3cd3-ab6b-87a2f4e1c768 | -10.96503 | -54.105 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9e15613-8795-3aa9-8e33-9a00b15ce0f4 | -7.80059 | -47.59858 | 2025-09-21 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fb6bb13-f453-364a-bb0b-65564e4678a7 | -11.29061 | -47.51182 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0c0ed0c-8bf4-3031-964b-24cf48c086f8 | -7.93069 | -44.11134 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfbcdb52-dd43-31e6-a02c-51aecba011b9 | -12.42217 | -45.12126 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06e31472-a338-34a0-8274-450d24659393 | -10.29108 | -46.0779 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 018fc16f-1d2a-367d-9c81-c15751d0189d | -8.34808 | -44.70703 | 2025-09-21 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17eda356-70db-3178-82f6-54923556c448 | -13.53239 | -43.00805 | 2025-09-21 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0f487fe3-6b8f-31f0-aa84-dc5b108fbf42 | -10.28623 | -46.07408 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5dd12def-7f42-3d52-a04d-5bf026e3d637 | -11.27561 | -47.4759 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c57b0367-fd1b-3024-8368-4a19d3e71285 | -14.97173 | -44.43419 | 2025-09-21 04:57:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 965fdb1f-35d6-3f99-8bbf-a1cb6d96f3be | -11.49462 | -43.59164 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19d1b671-9f92-34e4-8d3f-cf4f028915ef | -14.97795 | -44.4348 | 2025-09-21 04:57:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5f0627d-f995-3790-9b1a-3dc8a2660802 | -7.93015 | -44.11548 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1025173-c77e-36d4-9729-f19bbdca5225 | -13.30619 | -47.28981 | 2025-09-21 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 478c8d1c-09b4-39a2-a22d-db2568519459 | -12.06803 | -44.82835 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ce36fa2-d506-31e1-98b5-5399bef37be8 | -7.93193 | -44.09924 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3a531dd-b0c1-3b21-b20c-32455daa1020 | -12.70713 | -46.86328 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dbb25bf-6895-336d-90ce-9b15a1286a0a | -12.06948 | -44.8164 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39cf6b1c-76d6-3e25-88bc-7e4e28087212 | -14.43075 | -47.58061 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6e93b79-8530-3461-be0e-51e0fb6be9de | -8.20008 | -61.20597 | 2025-09-21 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7605aef6-7dc7-3e1a-9447-e1454354dd68 | -9.17129 | -44.62101 | 2025-09-21 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48e078e5-1b99-3d3d-baaa-c20411abacc7 | -11.93516 | -48.70828 | 2025-09-21 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63cf3239-c93b-3101-974d-1e28ff2ee049 | -11.27985 | -47.40527 | 2025-09-21 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fd205fb-3048-3d6c-b230-f2c18a00ad85 | -14.74586 | -49.1909 | 2025-09-21 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c33884b1-0c11-31a7-8410-17bec518f980 | -9.1651 | -44.62403 | 2025-09-21 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94e89ae1-3ee3-3403-bdcd-25192757df79 | -10.36558 | -47.90501 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e086ec92-c35e-34d6-9c75-f67b66029a3f | -11.66476 | -57.3483 | 2025-09-21 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ee1a5fa-f4fb-3c52-81c3-c397871f2696 | -11.14339 | -54.31247 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a8689c1-d972-3806-9c15-790052e35dc8 | -11.38907 | -58.39384 | 2025-09-21 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95a9e91a-76d8-36b2-ab3e-18324d9851de | -14.61313 | -49.76355 | 2025-09-21 04:57:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd07b6a0-318f-3eab-8d69-48acca2918a9 | -8.27696 | -41.6853 | 2025-09-21 04:57:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9866a7ae-825d-3137-9c41-fd334d86a4da | -7.94352 | -44.10086 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e64090f6-47f4-35e6-90cb-0122d7d3d0a6 | -14.43004 | -47.5814 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96301713-7d91-36f6-bcc6-f026863819c5 | -13.53906 | -43.00862 | 2025-09-21 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 113b7b5e-bf24-3e6b-bff3-d4a421606c23 | -7.92543 | -44.10635 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6996a865-e58b-3286-8a79-fad7e609fd9b | -14.51946 | -44.86793 | 2025-09-21 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34b2deaa-a716-32a0-b2a6-920d55f8e339 | -12.07576 | -44.81364 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22be5e34-2a93-306a-9600-60ba4306ac0b | -14.31863 | -47.79138 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c12d7eb1-221b-3ac9-bb2d-3caa2da36b19 | -10.28137 | -46.07028 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bebbcc4-eb85-3bd8-b865-c07fdc72cc39 | -13.64523 | -45.7043 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1418585-d4d7-3d59-9e1e-9007f9894be2 | -12.71032 | -46.8626 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08e3c6d7-a4ef-34a9-b752-18d487fcb380 | -10.28984 | -46.08748 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c3525b4-21eb-3957-989f-3627424b32d3 | -10.29067 | -46.08109 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4851d99d-bf12-3e9c-a3d4-d354f7582297 | -13.31226 | -47.28216 | 2025-09-21 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4d830f5-9495-3707-8c9d-800cf0ee1aa2 | -14.60933 | -49.75871 | 2025-09-21 04:57:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceef8f01-3e9c-3284-b577-aafbe00111a7 | -12.70312 | -46.83706 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ae2f26-a9bf-3493-945c-c4a2cd372a86 | -10.2668 | -46.05877 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec74685a-9164-3a4d-8aa0-e25a065651c4 | -8.59919 | -45.34393 | 2025-09-21 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ecde8d2-a070-348b-a900-d4e106d7d7b0 | -14.4351 | -47.58178 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa5a0772-3774-377d-a8a3-e93a2de2c9a6 | -14.47501 | -46.50933 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cb551aa-a9f5-3251-b37b-0e585e1a5b6e | -13.31152 | -47.28825 | 2025-09-21 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8ce3940-bc41-3e9e-8a0a-012ca185a857 | -12.71517 | -46.84009 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7807fa44-8826-343b-85a3-7375ae38b08f | -14.43686 | -47.57261 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 133fe1fc-10c9-392b-aa76-57926e2fb5e2 | -12.89853 | -46.77263 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 074bb9fd-2f7d-3215-922b-6cef06de4108 | -7.93756 | -44.10382 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70728075-a47d-3ab4-b7ca-9e3c376edb01 | -11.52601 | -48.55292 | 2025-09-21 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b4ebff-1445-39b0-b4c8-8b499df8d141 | -10.29511 | -46.08804 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 98cc416b-a20c-391f-a2ff-9a5323a501af | -7.92209 | -63.49026 | 2025-09-21 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f70679a6-51a2-3e76-a6bc-3b4914bcd5d9 | -8.28375 | -41.68606 | 2025-09-21 04:57:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acbf84f8-2dcd-3d6c-89a1-06d37e582575 | -11.30723 | -47.4979 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9dea66a1-ffe6-3cd1-9e96-2ac8f562ed15 | -10.35298 | -47.89307 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc99c910-924c-3964-aa04-5f905f2636a0 | -12.31032 | -44.87468 | 2025-09-21 04:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cba947d-3bfd-3165-bfa5-32109adb0769 | -8.98435 | -65.45606 | 2025-09-21 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46129684-9aa3-3e52-b79a-264faca9fc5c | -14.46144 | -46.51118 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d945129-7065-3cbf-81ec-fb263ffc3ac6 | -13.62612 | -47.41863 | 2025-09-21 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a82ace2a-d50d-319f-9e9e-faf0fe59953c | -14.4641 | -46.50884 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96e9b931-dda3-3129-b5bb-2351e4dd68b4 | -12.08249 | -44.85567 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 093baab0-186b-31dd-ac99-6cb3619e2db9 | -9.46233 | -60.48484 | 2025-09-21 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9f70e61-4ee3-33c0-9d15-c7cff6865f3c | -10.03675 | -46.2679 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0539882-b685-3b78-848c-f19ba666ca67 | -12.71264 | -46.861 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f8b03e7-65cd-3b63-b7b6-c52d4d534f23 | -14.43577 | -47.57613 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88ae74a2-a861-3688-be87-fbbd5f548811 | -11.3003 | -47.513 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffe105b2-b2cf-3f34-8f0b-e7fe84549b91 | -7.94238 | -44.10917 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e6bfb45-50b4-3c76-a0c8-86462ca2ff52 | -12.70785 | -46.84111 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2f4ba5e-524a-3643-9833-592be44e7807 | -9.6398 | -49.65326 | 2025-09-21 04:57:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dd4cd2a-b090-3c30-99ff-a9bcffae4dd7 | -12.06899 | -44.82047 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98d3a172-6bbc-3364-8bcf-a7323c5db6f1 | -10.26153 | -46.05812 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12a92969-5eac-3817-998c-2db699733529 | -7.93122 | -44.10717 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b5b9c3bf-4faa-3904-9cfd-500bf2dd41da | -14.74133 | -49.19035 | 2025-09-21 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53e94160-c9f1-3b21-837f-d8ba39464726 | -10.38504 | -58.0034 | 2025-09-21 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4d622d9-4f7c-364d-b88e-796b342ce390 | -14.46989 | -46.50619 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b28411c-9d0a-3781-b9c4-edcd0e28a0b6 | -7.9325 | -44.09504 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98b93c29-d36c-38ac-8312-8f7fa1fca336 | -11.50153 | -43.58718 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 480d8cbd-dd77-3369-9070-99fd1c497042 | -14.20667 | -44.66257 | 2025-09-21 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47499b43-402e-3a62-8623-d0a458a7640a | -11.27488 | -47.48153 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7a67db5-2333-37f1-be06-f03d7ecb12fe | -12.71858 | -46.85529 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b372cde-35c2-39c5-88ac-4e98d2df5b53 | -12.24579 | -49.1735 | 2025-09-21 04:57:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9db8caf-f2aa-355b-abff-9635bd2615de | -11.10836 | -49.68071 | 2025-09-21 04:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 101fefbc-9826-3dfb-8cc9-ee56565fb827 | -12.41552 | -45.12805 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d703f51-e63f-33c8-9852-33b61aed1fc9 | -14.61365 | -49.75952 | 2025-09-21 04:57:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4b37b74-77b5-3400-bbdd-edebda838e9e | -14.4583 | -46.51162 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89aa524a-48dd-3ffd-b6e0-77aacf04aee9 | -11.31207 | -47.49852 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dffd4d21-9f84-3402-9946-bf99bea40eb4 | -14.97281 | -44.42416 | 2025-09-21 04:57:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 422e81cf-06ad-3480-a3d5-c9f0ac6132ce | -11.27882 | -41.85248 | 2025-09-21 04:57:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 93887e45-c268-39dd-a9a6-24ef0b67b56f | -12.70486 | -46.8386 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15e8e892-decc-3c48-b9b4-232fca490ba6 | -9.06127 | -47.01554 | 2025-09-21 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86890744-a4b7-31d6-a265-604f115311ff | -6.33562 | -56.19078 | 2025-09-21 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
