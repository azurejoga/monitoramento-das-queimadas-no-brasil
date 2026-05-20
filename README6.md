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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a4248e9-a3c1-3784-8f9e-8e7fa903fb4e | -8.69972 | -47.91811 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56827a6b-7b62-3019-8886-4157e439c6f0 | -8.09442 | -44.10395 | 2026-05-20 04:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63ed49ba-41e2-3194-86f7-49aa9c91a730 | -6.64073 | -44.49351 | 2026-05-20 04:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14c36b91-d8af-311c-94e0-1807be3b7e14 | -8.73218 | -47.98066 | 2026-05-20 04:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 51c0fdec-7225-3549-ae1d-03be0660b8bb | -10.11355 | -52.41565 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d117978d-1a76-3611-a76c-6ddaff68092b | -10.39804 | -49.44225 | 2026-05-20 04:42:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc411ba5-a923-360c-8714-c232fd8d08e4 | -9.07381 | -49.66077 | 2026-05-20 04:42:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a6c7fd8-9de0-35bb-abdf-fab780aadfd2 | -9.07326 | -49.66426 | 2026-05-20 04:42:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab6eb8bc-c79a-3e95-9c36-8b1b8b408ca2 | -10.48769 | -49.36539 | 2026-05-20 04:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee787d14-a2f2-3771-8598-27fcfea83846 | -11.07899 | -48.2593 | 2026-05-20 04:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6c36f77-6368-3475-9093-b991127f453f | -6.21652 | -46.89739 | 2026-05-20 04:42:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddfedb01-6a03-3d7d-970f-5e2d92905a17 | -9.96418 | -52.41144 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97623f97-2a94-3577-82b5-16691d978c8c | -11.27425 | -49.46015 | 2026-05-20 04:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7f2dbb-e88b-3b87-9be1-86184749463b | -11.04571 | -49.5336 | 2026-05-20 04:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17e8c437-6058-3b4e-b874-5d7f5cf72462 | -10.57841 | -46.65179 | 2026-05-20 04:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23483695-a40c-383d-8f6c-70631bdc09c4 | -10.33051 | -48.28466 | 2026-05-20 04:42:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 821f17c4-7576-31e0-925a-e93b2e82850f | -6.75439 | -45.0169 | 2026-05-20 04:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6de20c90-3647-36ff-8786-37b27d192aec | -11.93126 | -43.86837 | 2026-05-20 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ad3c723-1909-3436-a6ae-c5a1275c37df | -8.09805 | -44.10846 | 2026-05-20 04:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7ffb76-e610-3227-9021-bbc5764502f9 | -7.40042 | -46.62534 | 2026-05-20 04:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39df028d-b479-3740-8b49-b0cb6e2746bc | -9.21789 | -46.66692 | 2026-05-20 04:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7316199c-68e3-3ac0-b43b-a69b07a6f84e | -6.4537 | -44.13227 | 2026-05-20 04:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56959b21-eecd-32dd-bca9-ffd1ed61d849 | -8.3222 | -48.0056 | 2026-05-20 04:42:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bda93d80-2be6-38ee-bbf7-467bb2c7421a | -11.92675 | -43.86773 | 2026-05-20 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b8fe7301-daf7-3fda-9eb8-8d705e30ef50 | -6.45423 | -44.12876 | 2026-05-20 04:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c244695-b4bb-38aa-99e5-a955abff4ec6 | -8.09748 | -44.11234 | 2026-05-20 04:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1543c27-21a7-3ad8-afc4-ab4d0cb64a67 | -10.06265 | -47.97248 | 2026-05-20 04:42:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d13d20c1-7685-3ee2-84f8-908c69ca54c0 | -8.61431 | -45.99754 | 2026-05-20 04:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27053e66-1fe8-34b1-b32e-2e9b917f1482 | -9.96165 | -52.47037 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e504d1cf-bbe5-327c-bba4-85e0c9006d07 | -11.03397 | -49.47699 | 2026-05-20 04:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d1a0563-b4ce-39da-8403-0fde6267ae7a | -8.32164 | -48.00931 | 2026-05-20 04:42:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f955201c-68e1-39eb-a6d1-cb2947ff0fb6 | -8.7003 | -47.91435 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c40bfd3c-17d8-3c16-b748-ff18921de1f4 | -8.1011 | -44.11686 | 2026-05-20 04:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4221493-fe03-3c3c-9d00-2525798638a9 | -8.09499 | -44.10007 | 2026-05-20 04:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2085ca78-e4d4-328b-83a8-3e1e7d5c533e | -7.01479 | -44.99153 | 2026-05-20 04:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9adadbe-4ec6-3cdb-9e19-fe395d95caca | -11.93002 | -43.86584 | 2026-05-20 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 74b81837-6f2d-36ea-8062-144785cc86d0 | -10.32609 | -53.57936 | 2026-05-20 04:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c0c48ff-381e-3977-b894-633a9fab80bf | -10.13684 | -49.54968 | 2026-05-20 04:42:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca63d918-bbe5-3b7e-8f5c-e3df1d1ad3b1 | -10.56666 | -46.65452 | 2026-05-20 04:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 672b199b-b0c6-3f25-b174-7e6c4cc8e59c | -8.70774 | -47.91167 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2166f2a1-671c-322d-adb1-d6a360d6a037 | -9.96228 | -52.4665 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66948b79-a49e-38ab-83fc-21c8e5c46359 | -10.49103 | -49.36592 | 2026-05-20 04:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5141e9f3-abf5-37d3-8d66-ee94cf2ca381 | -9.95819 | -52.46979 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12a8b77d-e59e-31af-a6f6-7778d3394449 | -11.34239 | -48.20796 | 2026-05-20 04:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c0f02dd-c9ed-38c0-9a7e-db2f33cc59cb | -9.63314 | -48.17649 | 2026-05-20 04:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3c3047e-5e88-3e5b-a60f-c35596c8e40e | -9.95409 | -52.47306 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c3e6b4a-93ff-3e19-a07b-dae7bfe651c0 | -10.99966 | -44.81495 | 2026-05-20 04:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c98301b-48cb-3120-893d-828f8fba5be6 | -8.61365 | -46.00206 | 2026-05-20 04:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8b79a57-4c69-3e22-8087-c82750dbdfa1 | -9.17822 | -48.99329 | 2026-05-20 04:42:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb41dba8-bfc3-3a76-b5d3-959be62d0ae0 | -9.14194 | -51.27737 | 2026-05-20 04:42:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 128b8434-b1b7-32e7-9fbf-eb436b1e619f | -8.09996 | -44.12461 | 2026-05-20 04:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caf92c13-f81b-38ef-b690-b5a0302d5fd0 | -9.16459 | -50.03167 | 2026-05-20 04:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df87d587-f607-35c1-b758-2c23e9480e8f | -11.0169 | -45.13281 | 2026-05-20 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c8def18-e676-3666-a636-fa26dcca4cb9 | -8.70088 | -47.9106 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0959e27-6ced-316c-b9ff-dfcf2dbadfa3 | -10.49821 | -42.40797 | 2026-05-20 04:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f4c1c17-7973-37f1-99de-9081f23de530 | -10.4957 | -42.40556 | 2026-05-20 04:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d43ea049-d3ab-372b-9c66-ca277521adf0 | -9.96512 | -52.47095 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05833c25-bf8f-3482-ad65-777bacb193ac | -8.31823 | -48.00878 | 2026-05-20 04:42:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18e19422-12e6-3f97-889b-2e4e469ab6e1 | -10.4966 | -48.11188 | 2026-05-20 04:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce630395-e3f3-35d6-a202-29719f0d5b1a | -9.96575 | -52.46709 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 87bf821a-7d9e-3018-809e-b2d5129dcd9c | -9.96072 | -52.41085 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7054bc24-9cb0-3eba-9798-ffe9caac5fad | -9.97046 | -52.41645 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbdaa326-1133-37fc-af1d-f0c0e5c8b953 | -9.3728 | -49.22645 | 2026-05-20 04:42:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53ff8b81-a543-3a05-9277-74e21f9f0c9d | -10.5747 | -46.65122 | 2026-05-20 04:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d40f9f6-6d99-34cf-9330-251c8fb7d0ab | -6.2981 | -43.6373 | 2026-05-20 04:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecef53ef-a098-34b5-ac94-ebfead8d7a6b | -9.95755 | -52.47364 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef481a3-53bb-3405-befb-ddba18c6fce3 | -10.49718 | -48.10806 | 2026-05-20 04:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2582902-791a-3c06-ab9d-59ae61e5d5b8 | -11.92487 | -43.86982 | 2026-05-20 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e40d0ae-981a-314f-a3a0-695decfd5cbc | -9.89143 | -52.44266 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6399a9f3-ab7e-3e46-8087-221001b64523 | -7.01398 | -44.99444 | 2026-05-20 04:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d73a75c2-411a-3bc1-b77b-4074a539f5a6 | -8.70315 | -47.91866 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e0215ea-2dcb-3668-9301-c4f8c6729939 | -8.71116 | -47.91221 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7813fb23-7ed9-3029-823b-5cc4113fbdaa | -11.60269 | -47.10101 | 2026-05-20 04:42:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d99a3e73-f7ff-3659-be87-8a49ac9989d7 | -8.71001 | -47.91973 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5a1d56-1752-344b-9326-2c430244696e | -6.75125 | -45.01135 | 2026-05-20 04:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ef9074c-ad19-3e45-ae95-e347c5d9075a | -10.49891 | -42.40249 | 2026-05-20 04:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 732c070a-eb91-3d02-88ed-ca5df2c9eb2d | -11.08011 | -48.26025 | 2026-05-20 04:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15f5057f-02c5-3cda-8e45-74d500928e57 | -7.40104 | -46.62125 | 2026-05-20 04:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9edce7c9-ef56-34d1-b5c6-ba3a8d6780fb | -11.47068 | -47.3408 | 2026-05-20 04:42:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 507d4bfc-6899-3f7a-b2c5-4a8020010789 | -11.92551 | -43.86522 | 2026-05-20 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e37ea2a-9c6a-3f21-a1c2-2a9645418bb1 | -8.10053 | -44.12074 | 2026-05-20 04:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aebdddb4-121a-3e8b-8d3f-7672fe5d55e4 | -10.57036 | -46.65508 | 2026-05-20 04:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd492daa-5a63-38b4-81a5-1eb88433720f | -9.96355 | -52.41528 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffd50b39-c39e-3a02-a1a4-d4306771080e | -8.7316 | -47.98437 | 2026-05-20 04:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4454e69e-17f7-33f5-9df3-f40810c7672a | -10.57407 | -46.65565 | 2026-05-20 04:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2740df71-6148-30d4-b1b4-8510e2449197 | -11.07666 | -48.25972 | 2026-05-20 04:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06c2d5f6-31c0-38e8-a722-6ba6e017ddd5 | -8.84713 | -49.87051 | 2026-05-20 04:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b21e3aa-1c9c-3191-be5e-11fedbb345e6 | -9.94626 | -52.41231 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c9094f4-4598-331c-974c-71576325f5c2 | -10.66747 | -48.25319 | 2026-05-20 04:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a045fe0c-1dd4-3e28-8a77-ef30836a8245 | -9.96763 | -52.41202 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4070831f-f65e-3b8c-91db-273d04a09475 | -9.8845 | -52.4415 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bbe5aef9-8fcc-3f02-899e-5ea3e19b9c96 | -10.11764 | -52.41241 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20772d20-d9b3-31fc-982a-50ba4a96efc7 | -8.70658 | -47.91919 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e9ec35b-8d1a-3bed-967e-396fcc985169 | -8.4317 | -46.92445 | 2026-05-20 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9150ac36-c957-3687-8c79-a32d9ae46710 | -11.18382 | -48.03354 | 2026-05-20 04:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b51c8412-6550-3074-8072-46ce158a2e4c | -6.2206 | -46.89407 | 2026-05-20 04:42:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb811b95-5f21-3950-9845-83bf20e5b3bf | -8.70431 | -47.91113 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa6095ea-c1cc-393e-9d66-205b28ea2bcd | -10.32246 | -53.57872 | 2026-05-20 04:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2715f082-c9d1-3c4d-b2f8-a5d3c966978f | -8.71059 | -47.91597 | 2026-05-20 04:42:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79545059-3fef-3008-a211-bb625e07b258 | -9.96009 | -52.41469 | 2026-05-20 04:42:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
