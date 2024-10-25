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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14e7de82-7549-3837-a49d-a6f400ad59a1 | -4.24842 | -48.54877 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 55f97087-dc2b-30ac-a5b3-f87e84b9b284 | -4.24614 | -48.55705 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b278df29-dc5c-3179-88fc-b5d9ae17c44e | -4.24493 | -48.54931 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b0ef3364-6f01-3244-8503-db46d24e6080 | -4.24432 | -48.54543 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ebbff048-08f3-3968-bc86-a6da95acf928 | -4.24266 | -48.55761 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4eaaa534-ae31-3e60-ba0a-a724ac19e0de | -4.24205 | -48.55374 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3109e161-380f-3a8c-b03e-1acce2a56bea | -4.24144 | -48.54985 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 671ae56c-d5cd-3db6-a597-d21b07b83ee9 | -4.23917 | -48.55816 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b3310459-726d-3a56-b65a-b9f76a276698 | -4.23857 | -48.55428 | 2024-10-25 16:52:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 367722c0-4e89-34c5-bb33-b2aa306a9c9f | -4.19105 | -47.77341 | 2024-10-25 16:52:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30ae9747-8bd4-310c-bcc9-9bed3b7c0f17 | -6.32806 | -49.23771 | 2024-10-25 16:52:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dbe1ea68-4575-3aa6-a94e-5bf58abe2d0d | -6.30397 | -49.30354 | 2024-10-25 16:52:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f039f3e0-a473-38bb-9df8-6fee341500fe | -6.30061 | -49.30405 | 2024-10-25 16:52:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fd49d43d-e8e5-3fe0-8dd3-66dfc745d513 | -6.30018 | -49.08051 | 2024-10-25 16:52:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35e95747-b169-32aa-bf25-07ce37dcd650 | -6.25891 | -48.83797 | 2024-10-25 16:52:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5d7f37a1-552e-3a1c-8171-538056260348 | -6.21335 | -49.39805 | 2024-10-25 16:52:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1174bc4e-0254-3b96-9e56-330d6f449c82 | -6.12273 | -48.81832 | 2024-10-25 16:52:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 01b09b95-dae1-316d-8f13-eda0fb8801a9 | -6.11822 | -49.46439 | 2024-10-25 16:52:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 46739dce-5276-3a34-9211-8037ebe542f3 | -5.97664 | -49.09856 | 2024-10-25 16:52:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 429c656a-4469-3073-8d1e-c6ce4bc8a77f | -5.97034 | -49.41114 | 2024-10-25 16:52:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d042523e-abbc-363f-9b50-d2f405077025 | -5.8708 | -48.26175 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38f62a11-b2dc-39e4-80e8-d393419eb2e8 | -5.86058 | -48.19622 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f09d618b-d3cb-30fd-8569-629afab5a7b1 | -5.78822 | -48.67814 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4632113-d36f-3981-9b65-d9400993c681 | -5.76652 | -49.23546 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02c33cdc-ebd8-3de1-9de6-41f58e118037 | -5.74905 | -48.49604 | 2024-10-25 16:52:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd32d225-cba8-3ee2-8495-25c463f15c9e | -5.73289 | -49.30681 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 2ac67497-965f-338f-ae04-13b29a8ba57b | -5.70346 | -49.07532 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 58d3b76a-5403-3116-a1fb-1c677368713e | -5.61776 | -48.19463 | 2024-10-25 16:52:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bb5402b3-c51d-34cf-a240-060d2583aa1f | -5.43755 | -48.25011 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 9f8fd107-38f9-3daf-837a-aeac2b672d9f | -5.43466 | -48.25455 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 31.0 |
| b51cd120-5413-3891-b126-a9d90db4360c | -5.43406 | -48.25068 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a7b652ae-91ae-3850-9e68-800bf74cb1d8 | -5.4166 | -48.25343 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55e94844-26bd-3cee-b14a-865a0dc1da6e | -5.3864 | -48.57595 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 06285372-28cf-3c5b-9c5a-af210e4138f8 | -5.37801 | -48.23564 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 56c61749-86a8-3586-b5dc-d8bc8b98290e | -5.34409 | -48.2251 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| befc7704-bb4f-3952-9e19-103a63c093bc | -5.25374 | -48.44425 | 2024-10-25 16:52:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 037c724e-abf5-3d47-bc78-f8b6c0604eb0 | -5.24363 | -48.30054 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 318c8046-6e6b-3026-8733-d9122b8b3a8c | -5.24076 | -48.30496 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e5dca494-3b1f-3b1f-816d-c4c064553de9 | -5.24014 | -48.30109 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1ad84ac6-a1bd-33ab-a819-03b4175e61e6 | -5.23919 | -48.30441 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 28ab3e50-4e5d-3292-804a-95c6d732e1ef | -5.23859 | -48.30053 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3af5c6d7-2566-36a2-a949-a3e536cd94f7 | -5.23665 | -48.30164 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e87ccf85-30bd-3f97-9aa2-7975cdb27cf0 | -5.2345 | -48.2972 | 2024-10-25 16:52:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef2c0114-ddf3-3bd2-abf6-8de164526565 | -5.20429 | -48.21815 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 63d1e82a-1d75-346a-aa86-7e7255813e24 | -7.97543 | -48.81271 | 2024-10-25 16:52:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c1333401-437d-38ac-881d-4d47ad996ad8 | -7.97486 | -48.80912 | 2024-10-25 16:52:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6f00f3a7-a33b-34ff-b27d-22f3b513bd0b | -7.97207 | -48.81324 | 2024-10-25 16:52:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e14e8f99-9b71-3c4b-ba66-d3774ae8e354 | -7.90395 | -48.67601 | 2024-10-25 16:52:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6169f0ed-303a-3b7f-a0fd-4cdb012d5d46 | -7.87738 | -49.603 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b5cca913-2bf8-3851-90eb-3152075f2802 | -7.84474 | -48.95782 | 2024-10-25 16:52:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 185be3cc-2a7d-3b80-ae64-0fba7d859567 | -7.8424 | -48.95885 | 2024-10-25 16:52:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16bf5d21-2bb4-3ba4-9ac2-779a09c4690e | -7.64851 | -49.61805 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac441a5c-f525-3668-a8a3-70ecff4a6471 | -7.4953 | -49.20024 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a777787-6bd5-3efd-9684-a273f7607dc1 | -7.41302 | -49.65622 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 435564c4-6880-35a7-8244-7f2663feb02f | -7.4097 | -49.65673 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 397cdfbd-28eb-3d92-95e3-909b9f037914 | -7.24036 | -49.37526 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a94b94f1-aafa-30f3-81f6-1d53d1d40760 | -7.10879 | -49.13901 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 913ad651-cb06-3da8-9cb1-a81bc31f5542 | -7.10599 | -49.14309 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b3265cf9-49f7-31d6-8612-a66a62fa26cb | -7.00708 | -49.34011 | 2024-10-25 16:52:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c18a55b-b55b-34be-b490-a9d4a17a7d6f | -7.00429 | -49.34417 | 2024-10-25 16:52:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 800287c7-4c3c-3485-8911-3146d47886f4 | -7.00374 | -49.34063 | 2024-10-25 16:52:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d09a9aab-ced8-3fbc-ae16-6a7e197cc9bc | -7.15769 | -48.43478 | 2024-10-25 16:52:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b510ceff-ac9e-3e8f-b4e4-19c29a0bb13b | -6.78629 | -49.20885 | 2024-10-25 16:52:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 02bc698e-52b6-3c75-9d73-81c444d32732 | -6.74489 | -48.82044 | 2024-10-25 16:52:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f49a0c6b-7334-35ab-b7bf-4035943607e8 | -6.74431 | -48.81681 | 2024-10-25 16:52:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 6930222b-e557-3811-87d9-7a213689aaed | -6.74374 | -48.81317 | 2024-10-25 16:52:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 995ed92d-c85f-3024-935f-1ef77a62e218 | -6.70478 | -49.30173 | 2024-10-25 16:52:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 3d45fd3c-bbc0-33c3-8fbd-b110246fe8e1 | -6.70144 | -49.30226 | 2024-10-25 16:52:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2ad59c00-88c5-3181-987a-c1bbff3976b0 | -7.79705 | -50.02884 | 2024-10-25 16:52:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36e8ccd1-fbf9-33ce-8b30-988cf46e1edf | -7.55259 | -49.90162 | 2024-10-25 16:52:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb52871f-72fe-34bf-a70a-61fb0e290227 | -9.1214 | -50.04394 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 749defdd-f468-3984-8243-54d00b9de0a2 | -9.11784 | -50.08718 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b188da34-4dd7-3ddf-addc-db14471c022f | -9.11506 | -50.09118 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d941117e-6166-3804-9000-d05218295e37 | -9.11453 | -50.0877 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7c8e32a3-30a7-32c7-8cec-0e25f597f230 | -9.09459 | -49.80247 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 64ac6499-5dba-3685-80cc-9d842b490ce5 | -9.07976 | -49.7941 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b0598595-521e-3c51-b2e1-e9c8e584ef89 | -9.07251 | -49.81303 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25f50f60-1395-31e0-9651-1605c28eb2be | -8.99444 | -50.19324 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 215fc14b-e8c2-3d2d-87b2-76899261d526 | -8.99391 | -50.18977 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c6a61d2-3e7d-301d-b019-2fc61f126514 | -8.90341 | -49.92979 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5fdf68f7-4d8e-34f8-850a-89132610e553 | -8.90285 | -50.23959 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 8a42a787-44e2-3a19-a774-2e76c9ba3146 | -8.90231 | -50.2361 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e375fa10-004e-3be4-83fc-e4949af6173e | -8.89297 | -49.81755 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 885b11b1-76d4-3861-be02-f56fab979dd9 | -8.88689 | -49.82206 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| db0107b8-b8ad-330d-b792-6e609ea58d98 | -8.88582 | -49.81511 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e535abbf-6d92-3802-a988-cdad0a394b23 | -8.74893 | -49.78679 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0465966c-ed6d-338a-be0d-39358f05352f | -8.72531 | -49.94407 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76dd53a1-e35a-306e-8aa3-34bcca3a4d2d | -8.72477 | -49.94059 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 429b430f-eb6b-3c96-9e0a-9b916e73cc0d | -8.70914 | -50.08167 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a4c6248e-2cb0-3ce1-8331-720a430bbbcf | -8.70861 | -50.0782 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 589c7970-5c49-30d0-816d-af62ffe8b0c0 | -9.46712 | -49.06639 | 2024-10-25 16:52:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1961b494-0f89-3b63-9ff6-e235390379c9 | -9.46657 | -49.06288 | 2024-10-25 16:52:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c2c6a58a-e5c0-3c43-8289-0e095074b0b4 | -9.21327 | -49.44882 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 699011c8-02bd-36ae-91f5-b0d0c5bba8b4 | -8.96387 | -49.11118 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cae78b9d-10cb-309c-a45b-bf4b0a89a96d | -8.92681 | -48.93685 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4f0f245-e550-3b45-a143-edd8be541ecf | -8.92626 | -48.93331 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22d1b6b4-517e-35e5-b076-b2317344cd16 | -8.92293 | -48.93383 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b449dfe0-b8a0-37a3-aa9f-56adfed7952b | -8.48961 | -50.13487 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| ce850d5b-e04f-3826-ba69-d46010e15615 | -8.48631 | -50.13538 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a4394dca-5ea5-3e02-9a32-02169f4a2648 | -8.35024 | -49.73729 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README151.md)
