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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5d4ba1e-8798-3437-90e1-84deebe8c7df | -18.20126 | -56.51645 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| e3be3c81-7362-3de6-8793-d19cbfeb5c6c | -18.2008 | -56.47541 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f1a63cce-e189-353c-820e-44285ecca317 | -18.20024 | -56.47904 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 60bd83bd-11a2-3b04-9516-4f0c441b6abc | -18.19968 | -56.48267 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2cdeab8b-e2a5-3a77-b714-5bf32dfc839a | -18.19794 | -56.51588 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| de54c32e-009d-364d-9b79-dd07a0da31ac | -18.19749 | -56.47486 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d66b876a-b272-34cc-b384-b9dceb493f65 | -18.19738 | -56.51951 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| ecd295b8-dab4-3ea5-be71-ef5e30f135e7 | -18.19693 | -56.47848 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 408d7b64-bf5b-3258-8383-0bd69d11507c | -18.19463 | -56.51532 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 4c432be6-322b-394a-90e4-feed28d1d306 | -18.19407 | -56.51895 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| be205ec8-4757-3a40-b5eb-056ee31ff6fa | -18.19362 | -56.47792 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b414e27f-cd04-3842-a1da-17ed41fc8011 | -18.19076 | -56.51839 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 6b8dc5e9-93f8-336e-b5f8-bfd863d5fdaf | -18.1902 | -56.52201 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| fde9d828-55c4-333c-a9be-0484aad41703 | -18.18745 | -56.51783 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 00875c78-fd5f-39e6-87df-4ef4bcfe8c3e | -18.18689 | -56.52145 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 944518f6-2b98-3e61-be38-7342c68d8410 | -18.18358 | -56.52089 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8764e41b-2076-3803-8dd8-26fbc684bfc6 | -18.14908 | -55.92413 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9d4fbc73-8384-360d-813f-57e2b51b078f | -18.14518 | -56.39565 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 89596268-807a-3ca9-a61c-1852321bc017 | -18.14228 | -56.45838 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a87758c3-0cf3-37fd-8dad-a603b2e57f65 | -18.13953 | -56.45419 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| be2be3a5-30d5-3a2d-a951-7a1cf3611177 | -18.13896 | -56.45782 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f9079fb0-f887-3291-a5b2-1b909aba74f6 | -18.13687 | -56.40543 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ea0ff577-219f-3ed5-90ac-9e551c73e193 | -18.13678 | -56.45001 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 96eeab92-a673-3775-a1bd-dff02a96c8d2 | -18.1365 | -56.31963 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8b2ae4cc-c758-32c3-9ab4-94e7d8175daa | -18.13621 | -56.45364 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ba87bc9d-1255-3537-b64f-ef07240c3033 | -18.13593 | -56.32326 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 51235b3b-85c1-3294-83a1-55e5fa3c23bd | -18.1337 | -56.3378 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| baf49b7d-6ed9-3112-9585-22eb97101538 | -18.13346 | -56.44945 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| bc40f5f8-52aa-3eb9-aa75-a8aede9f7861 | -18.13318 | -56.31907 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bf3a621f-d668-3126-91de-6f592821384e | -18.13314 | -56.34144 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 159ca69d-9c5f-3014-9cf1-80f6fafe623e | -18.1329 | -56.45308 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd2b4987-e087-3714-a7ae-d30273e75ab3 | -18.13262 | -56.32271 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4ad26c1a-2ac2-3267-b573-2881b7982a92 | -18.13042 | -56.31488 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e4a2ba5a-296e-362d-8413-8508345b674a | -18.13038 | -56.33725 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 196fadb7-7630-36d7-bab6-167e355275f1 | -18.12982 | -56.34088 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f32a80de-2d3c-38f8-9beb-4614c1a0d4da | -18.12874 | -56.32579 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 686396ee-43b9-37a7-920f-5d89753372d5 | -18.12711 | -56.31432 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 13e2e193-ed04-309f-86da-2e8358edfb68 | -18.12659 | -56.29557 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 51510c4b-3aa2-3d86-8233-128916d3dd0d | -18.12431 | -56.3325 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3d368983-b29c-3a2c-af66-02c0efc0ca92 | -18.12383 | -56.29138 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a84ad12e-49fa-3500-abbf-085521ec5402 | -18.12107 | -56.28718 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b60ed8f7-8b6f-3aa9-97ff-797d838e7a18 | -18.12051 | -56.29082 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 98616c46-5045-3d9b-92d7-0cc0814cdd6c | -18.10477 | -56.43716 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 67850127-82b1-3d2b-bbd2-60377406ddb0 | -18.10222 | -56.32133 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 35b5e1e9-7f6d-3a80-94ed-394c7f44011b | -18.10166 | -56.32496 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7c181b60-4c30-3976-8478-06575bbc927c | -18.0989 | -56.32077 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 45901025-ff0c-3c2a-bfa0-b268891c8a02 | -18.09759 | -56.43967 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4e7f27c5-3e0e-38df-912f-df98b269663f | -18.09559 | -56.32021 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2a37edc3-85c0-3bb9-a537-dce79f0ad807 | -18.09488 | -56.41324 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 59bd34fe-dc04-36d4-95b0-447847fb972f | -18.09428 | -56.43911 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 68d915f7-87d5-3d20-9892-d1b004fffc0c | -18.09391 | -56.33112 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6b0d478c-d8e7-3314-9baf-d2bcf4d5f194 | -18.0938 | -56.39817 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 98d2c87d-01a8-3fb8-bef8-d70d201a1270 | -18.09376 | -56.4205 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5751b6a2-55d8-3f18-bde4-666a27f366e4 | -18.09372 | -56.44274 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dfb5014d-7b51-3608-a444-c4aa431010a8 | -18.09268 | -56.40543 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| beb3d9ee-bb9a-30f3-858e-41ffad3b0d1c | -18.09264 | -56.42767 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8d53fc20-567e-3604-81b0-0667d511ff28 | -18.09212 | -56.40905 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4df7d9cf-47c3-30d8-930a-041e980379cf | -18.09156 | -56.41269 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 56fff712-7102-33a6-b605-0ba17cb559c0 | -18.091 | -56.41631 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4942168e-7f81-3825-a195-d5595eb30322 | -18.0906 | -56.33056 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6fe8756d-25e2-3388-80a4-66db904c6e3b | -18.09044 | -56.41994 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6c34d591-8d89-3f69-8f1e-413e9c7d620e | -18.08993 | -56.40124 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e9f18bc4-2c81-3557-ad91-d4c9ecdb9ed3 | -18.08988 | -56.42356 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 97313e42-229e-39c4-995c-8e4f17728fd8 | -18.08937 | -56.40487 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1337f9db-5d47-331a-9799-ffdb53fcadeb | -18.08881 | -56.40849 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8929a6d5-7d78-3e06-899e-944778f5d648 | -18.08825 | -56.41212 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e7ca7523-3fd0-3c2f-ba66-2a0c11438adf | -18.08713 | -56.41938 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b9c9e1df-a790-3bc6-8a73-4d26098a2d06 | -18.08661 | -56.40068 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b6d18885-5db7-346f-af18-8a3ad9db1058 | -18.08602 | -56.42655 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a3296d4c-9479-3b92-a886-7dc80fe8c465 | -18.08549 | -56.40794 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b574b467-7d98-35ce-a8a0-525b6714f0a3 | -18.08278 | -56.38142 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| acc986c5-b888-3da8-b6a0-072557b6af0e | -18.08271 | -56.42599 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d9a04766-1a1f-3791-8a0f-545370ae9e00 | -18.08111 | -56.3923 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e3685035-b7e9-3d31-8754-2273852abd61 | -18.08003 | -56.37722 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d6b35d08-917d-3597-8f6e-2529121256c2 | -18.07947 | -56.38086 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 939e97a4-9b5d-3198-b262-2bfb2c13ea7c | -18.07779 | -56.39174 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9dd36c50-a898-3690-938a-55b11aee90d2 | -18.07615 | -56.3803 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d6cfed47-a32c-33dc-8611-5ae4c3fe1596 | -18.0756 | -56.38393 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 81e7580a-39ac-3438-96b9-c7f587f19573 | -18.07284 | -56.37974 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9a42e7d6-006a-3abd-9bcb-4b1399e345ce | -18.06953 | -56.37918 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8c70c73a-cce7-3f53-a610-042f67573e4d | -17.97885 | -57.36959 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 10261e03-dee4-3ad5-9f7f-e0fed393ab43 | -17.97827 | -57.37322 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 9d115c93-c98e-3dcc-8dd9-21cc8cc03ab9 | -15.95373 | -57.94522 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ce6f7708-f627-375d-9ef9-3a0e2c7581e0 | -16.56818 | -57.71294 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3572920a-c6f5-3b8c-af7f-25b2a51dc61e | -16.18691 | -57.41853 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eccd3181-e2a1-3b22-8f5b-5f5ee4f2229d | -16.18358 | -57.41795 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 972691b9-abf8-363a-b6c1-177f20fe16f6 | -16.17775 | -57.45406 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed9c7f27-b907-3421-8f44-31df1c6eb103 | -15.90227 | -57.47444 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2510e07c-a592-357b-8e0f-649220f313ad | -15.9017 | -57.47796 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4c09d8f-137e-3a15-a44b-03d21cc87c4a | -15.86342 | -57.46036 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b400b13-ed35-3687-b1a9-b72f37396b95 | -15.86008 | -57.45981 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 330b9532-0eb6-386d-bb93-5c6da6868cb3 | -15.85674 | -57.45927 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4a744e1-dc11-3c5c-8067-60a44da0ad07 | -15.8534 | -57.45871 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a7443d7-bdf2-352b-9fcb-2b863f700477 | -17.98101 | -57.37741 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d6fadc5f-baeb-3ee1-be0d-30288374ddf5 | -17.9777 | -57.37684 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 660f4196-eb24-32fa-b28f-323fed3bb819 | -17.97554 | -57.36902 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 1f14bfa8-67db-3152-af36-fed3beff3660 | -17.97496 | -57.37265 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 721dffeb-f60c-3a41-8c9e-b27d108fefa0 | -17.89447 | -57.3218 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| ee378ffd-35ff-3a0f-9100-cac85400bdd3 | -17.8939 | -57.32542 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 83e8e9e5-1beb-3bd7-8efe-e695e0744d5c | -17.89231 | -57.314 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |


[Clique aqui para ver as próximas entradas](README93.md)
