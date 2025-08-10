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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be49b2fc-8d2c-3a01-a775-aac3cca26109 | -6.3477 | -55.56307 | 2025-08-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c84798a-1dd2-36b2-a9cd-678cf9947777 | -6.98832 | -44.79509 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0bff8ae-dd3d-32be-b09c-5cc51b1dccb7 | -7.69944 | -45.54051 | 2025-08-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0636aea-9217-3f9f-b475-690ebe862cbe | -4.29315 | -48.27677 | 2025-08-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e1b1c6-2655-336c-bd58-e17d750290e7 | -2.58332 | -51.9115 | 2025-08-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb72c4a6-8e60-3544-a2bf-b90eee00e7fe | -5.35061 | -47.23709 | 2025-08-10 04:44:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9446f983-1b52-364c-88df-5c198f5513f8 | -7.73871 | -42.33452 | 2025-08-10 04:44:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 98f73d4d-3006-3638-a7cc-61dd0c031873 | -7.59478 | -44.41905 | 2025-08-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adb41d91-2b8e-398b-a6e8-4e5c67810648 | -7.34462 | -44.59667 | 2025-08-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01bb3416-31a5-3c31-99a2-e6e83d626ee1 | -8.10925 | -47.4409 | 2025-08-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b72b0329-ffdd-3f09-89a2-c99e837119c0 | -7.02472 | -43.55012 | 2025-08-10 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67e4e4cd-893d-39a4-bdfa-45c986578ada | -2.37386 | -51.90488 | 2025-08-10 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 911610b8-c570-38a3-946a-d5a46c339e53 | -3.43078 | -49.04341 | 2025-08-10 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 527cb50a-232f-3868-ba16-7d35d0b1b310 | -3.83604 | -47.74559 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f430a86-92ce-392d-9c6f-1ed571d54c86 | -3.42742 | -49.04289 | 2025-08-10 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e4f4cf32-a236-325c-9f1e-23f7252df305 | -4.06201 | -46.93437 | 2025-08-10 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c167273-ae6e-3585-b52c-740fd3243fee | -6.94382 | -44.56133 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1951ca6d-7dbf-383f-9668-9110c38d2e5c | -3.23564 | -46.7908 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33170556-8dff-3f06-8e16-9c5bbdabd5f4 | -6.19506 | -46.10057 | 2025-08-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e59c5b5-c618-383f-b58d-32efe4d78217 | -6.05298 | -43.75375 | 2025-08-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd2887a5-e2c7-36bc-9133-a6ca2ee9ca4d | -4.29972 | -48.07142 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bb7db04-004b-3cd9-b5b2-f3a258213942 | -7.344 | -44.60097 | 2025-08-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ba41f4c-3193-3f99-acad-77a9f978f413 | -6.9877 | -44.79942 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a45bc0-4cea-3459-b605-59aef8ab52fe | -6.94754 | -44.55424 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5f17a1ec-5827-3bf0-89b3-8e8183defc1d | -6.33848 | -55.56388 | 2025-08-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6146335c-8ad5-31f4-8e38-49874d5c84bf | -5.82402 | -44.10528 | 2025-08-10 04:44:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae8ecbf0-d38d-3e48-b46e-a0aa3d73efec | -6.58033 | -44.57332 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b089b468-fceb-34fc-ae1a-62e148d74910 | -3.42287 | -48.89497 | 2025-08-10 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4774fc1e-fcde-3432-8bfc-0fd5487e928e | -3.96329 | -47.88218 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393f77f0-8c1d-3751-afc4-8961fc8be163 | -3.5868 | -47.52783 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff972f12-d2a7-3e51-976d-40b6e60fb79b | -8.11064 | -47.43155 | 2025-08-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02485319-a7b5-338b-a5de-3778c5c91c1b | -3.42343 | -48.89136 | 2025-08-10 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6404b9c-e497-3b9a-a932-8a9539ce1d63 | -7.42656 | -43.99082 | 2025-08-10 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 167f3db2-d652-35da-883c-d1a48ffb1060 | -4.35144 | -47.53946 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f103919-49ea-3d46-a630-d2586418c585 | -7.88659 | -45.5564 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72a5e3e8-f322-3495-a337-f450805d9149 | -4.29621 | -48.07087 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5bd30cbe-ffb0-3c89-80fd-78bab01d085e | -6.97689 | -43.85678 | 2025-08-10 04:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af70ff33-2299-3e95-957e-b68d8e8fb1b5 | -6.19105 | -46.0999 | 2025-08-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7775b6fc-601b-36fd-8962-c2e846b58e70 | -5.05655 | -38.13877 | 2025-08-10 04:44:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 570fee94-13ab-3c5a-b320-dc9342c69710 | -4.95887 | -47.59538 | 2025-08-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66c272b6-130b-324c-a768-2d27ad4f3870 | -7.16292 | -44.06314 | 2025-08-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| da140967-e2ca-3e56-bfed-4f9462a57dfd | -3.58742 | -47.52378 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7f81d0a-7c22-3642-a3d0-45f3f6271d5d | -3.22447 | -49.33915 | 2025-08-10 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73dfe890-03db-3baa-b2d6-ca583f2a14ec | -5.59343 | -51.12626 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c12b2c6d-deb4-345a-a88a-dfed071f9fa7 | -6.96379 | -44.48409 | 2025-08-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6f70346-4e43-388b-a26e-da391ceff815 | -3.64883 | -48.3218 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60d627ab-7bf6-3c24-a8df-1c9ab42511d1 | -4.30203 | -48.0798 | 2025-08-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 381ec668-3342-30cd-aa25-53e891fbabbc | -6.19005 | -45.44615 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3626680-404e-3d43-acab-dc3657b104f3 | -6.64935 | -42.0166 | 2025-08-10 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 01e2c6ec-7f28-334e-bfbb-95e8e868cf7a | -3.83898 | -47.75011 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e981049d-076d-3665-b9f3-5dfdfd6472da | -3.98767 | -47.8884 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0f4d43b-0f4a-3a61-b9ab-fe2a9b381e50 | -8.51221 | -45.70592 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0d8089a-b102-3f27-99d9-4c07c8971295 | -3.96742 | -47.87883 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ab0eed72-d711-3b3a-b173-6e7a9ef86def | -8.11443 | -47.43214 | 2025-08-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61eb1512-31c5-3b73-9676-c4749ba574ef | -6.72976 | -46.30845 | 2025-08-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87242ec5-ff03-30e1-89c3-9f8e53db2d73 | -3.62084 | -47.52059 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d3e5c11-e455-3c6b-b319-1e3ae0bf7f16 | -4.14716 | -46.45332 | 2025-08-10 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a441837-9ac5-347b-a9fb-68befec005d3 | -6.34384 | -55.56237 | 2025-08-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4cd0b2a-37dc-3cf6-b06b-44d09f94dd0a | -6.52433 | -47.43226 | 2025-08-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4739d3b-2f2f-3861-89a5-e745677d3c3a | -6.07092 | -49.57526 | 2025-08-10 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47434e94-9e91-3f1e-bcba-347282b2f61c | -6.06161 | -44.89994 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a49a27dc-0eef-3b9c-8fdc-5113c7b52dab | -6.0584 | -43.74952 | 2025-08-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1340f943-bb23-3ea3-935a-f3793818fa01 | -6.94897 | -44.55744 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79c98728-f3df-3acf-9873-68f83e08e9f5 | -7.88174 | -45.55989 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd6133d2-2c00-3be2-a2b5-cc999e54323e | -6.96825 | -44.48529 | 2025-08-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8848cb0-4fdf-3ced-8052-c794462d9def | -6.94618 | -44.56353 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fb7211b7-cb85-3fbe-aff3-eebd061c1cc3 | -6.96225 | -44.48565 | 2025-08-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b258dcdd-6dd3-3368-a765-e45ad5b0f4cf | -7.51666 | -49.56177 | 2025-08-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa8d5ee4-1143-39a1-b6c5-bf166ba47ea9 | -4.30263 | -48.07588 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81cba4ef-ab8e-3560-bf3f-e7070e9b3a20 | -3.23126 | -46.79463 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6a89744-9c9e-386c-a52d-62fede95c5a0 | -4.14334 | -46.45275 | 2025-08-10 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baf03e88-594a-33ca-9ba7-d4886555b8b9 | -7.88952 | -43.54168 | 2025-08-10 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06f58f99-5f18-36a1-9929-26d206095671 | -5.39089 | -41.32806 | 2025-08-10 04:44:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d673043-df23-33ae-8cee-e4ed0190ba39 | -3.5891 | -47.52181 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 894ecccf-1076-300c-949d-0ffff35f1b8e | -3.88188 | -54.21379 | 2025-08-10 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b68a6989-c2a7-3bf1-96a1-058d54f28098 | -7.3453 | -44.59188 | 2025-08-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12fd12a5-58ff-3b73-9fb4-008c8fc05bae | -4.95525 | -47.59489 | 2025-08-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e44ed3db-9296-335a-8797-d416aa411e77 | -3.59099 | -47.52432 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89e865bc-bf5f-360c-a1b0-fa9c0544f003 | -6.5264 | -47.43091 | 2025-08-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85ffca46-4093-39c7-8887-7cb84eaaba7f | -6.95204 | -44.55499 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| faeffff8-5ee8-3731-886d-d7e048a56b68 | -6.99714 | -45.6213 | 2025-08-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4728af64-f088-3e35-a726-f36ba5d46027 | -5.91648 | -46.47495 | 2025-08-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a345a7cf-d673-3dae-a16e-d7da796830f9 | -7.87474 | -45.55539 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3725067f-505d-3adc-b9ff-70c5642bdc39 | -5.39147 | -41.32396 | 2025-08-10 04:44:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48612af5-4796-3de9-ba30-25523151adfd | -2.58555 | -51.9193 | 2025-08-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 331602b3-6c4a-30fa-aa0c-40c9e71a1104 | -7.26743 | -45.37134 | 2025-08-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30b0baef-f59e-3c28-b43d-1f0a854fba2d | -5.41094 | -44.43092 | 2025-08-10 04:44:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d640cbf-6d17-3558-a20e-cdaae6f463f4 | -6.94686 | -44.5589 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 372c9bcb-8537-3ac6-b992-8d7fec9c577f | -4.11181 | -38.17352 | 2025-08-10 04:44:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c89c39cc-2831-31fd-a338-3ce949d03a91 | -3.23194 | -46.79024 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0840b720-3eed-3449-8fc2-137c195e59c0 | -6.41099 | -44.56989 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a744214e-d9c1-350f-b402-df671b520198 | -6.18583 | -45.44564 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1148bb1-2d67-38c3-b42c-7c69624e8e84 | -6.19536 | -45.43903 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b62809f-1946-3183-85d2-8130860c1719 | -5.2805 | -56.02013 | 2025-08-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2754ea55-7abb-3b35-91da-01e067efc646 | -7.27041 | -45.37103 | 2025-08-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e621596-a465-376e-a2dc-7b253d8c2273 | -2.96152 | -49.06649 | 2025-08-10 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e361a900-2c2b-3d6c-8874-4671d5d50b7b | -5.3413 | -55.90564 | 2025-08-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75d96b3f-29f3-3d02-aea2-c38299d3c6b2 | -3.9671 | -47.88116 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4a8dc76-f994-3314-9bb2-fc505c707dc7 | -4.29852 | -48.07926 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95396cdd-fe67-3ab8-a5c8-f32c6184d4a8 | -1.22074 | -50.69514 | 2025-08-10 04:44:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
