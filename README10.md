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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15bfa7aa-a6b6-3700-a6c3-f2249cb8dc88 | -4.5732 | -46.5807 | 2026-10-03 00:52:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17ba207a-f2ed-34ff-b899-a504aa013da9 | -3.0058 | -53.881302 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a58cfa-84c7-3d5a-a4b7-9f225832437f | -6.158 | -49.4828 | 2026-10-03 00:52:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2654d981-d9f1-31ec-a1f8-f32f0faa031b | -11.7182 | -43.507801 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 082f14cd-f586-3871-8187-1f450f3909d2 | -15.3034 | -42.7929 | 2026-10-03 00:52:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3400d63a-bb74-31f4-bea1-d206fe3dce25 | -4.8392 | -43.021801 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ffb6b20-9ac7-3054-8705-c813c02b94cf | 1.8081 | -55.5928 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e33e1b-785a-3cfe-ba91-e20dfc0194dd | -2.894 | -45.406799 | 2026-10-03 00:52:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c38bbf09-76c8-3ccc-8c82-dd62396e2eb8 | -1.2656 | -54.565601 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335acc35-6e2a-3a1a-92ce-7092712218a9 | -4.1926 | -48.6702 | 2026-10-03 00:52:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbd7c09e-4f64-36a7-ae76-1fc3ead74b6e | -3.6439 | -55.508999 | 2026-10-03 00:52:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32cb70bc-ca50-3a0f-8b58-7fd86e10297a | -5.6124 | -44.368999 | 2026-10-03 00:52:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e596810-e73c-32f6-8488-00eb9a6c25fd | -5.5993 | -44.904099 | 2026-10-03 00:52:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0a744b1-837c-38aa-9c2e-5746abc6ce73 | -2.5629 | -54.740101 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 881c26e6-a0d9-317c-a81b-4004b91c7225 | 1.918 | -55.7868 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bbe8e9b-64e6-3cb4-8ea3-48975a74f074 | 1.9244 | -55.803699 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4658ac8b-d3cd-3115-80d9-3db68cc2902b | -4.4583 | -47.916901 | 2026-10-03 00:52:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5b6fac-3edb-37a7-8d06-811f6d07c865 | -2.8906 | -54.1441 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc358239-4ed8-3ef5-af27-68940ff701ba | -6.1562 | -49.475101 | 2026-10-03 00:52:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22647bee-f6d4-39f4-8df5-6fcb28b64e72 | -4.4485 | -47.919102 | 2026-10-03 00:52:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a823cc9-c652-3aba-bc1f-31ef653561e8 | -11.4211 | -43.397099 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b45403c2-1e03-3f9b-990d-8d4587dd0550 | -3.1289 | -53.743698 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a04b75e-14a9-3f42-bee1-c43219f59c07 | -5.7364 | -45.128601 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05058354-2559-39b4-8575-a43e18d6cf9f | -11.4502 | -43.389599 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9ce75c4-7761-325e-b045-572e61dcfc8c | -11.8491 | -44.722801 | 2026-10-03 00:52:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0a51778-b4c5-3410-a465-af641ae8f98a | -5.6163 | -44.384899 | 2026-10-03 00:52:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43832297-1d94-3608-8261-970a7d948984 | 1.7901 | -55.5812 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86c69e7f-9abb-38b2-b2e5-3b486250bd63 | 1.805 | -55.5616 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61987fc6-2116-31e9-8ee1-e0561e969660 | -3.2162 | -53.945301 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 808bbf28-2edb-3973-b03f-5d78bb0e33a2 | -5.7385 | -43.297199 | 2026-10-03 00:52:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c673ca89-19ea-37ca-8fc7-601288d30d81 | -6.8373 | -59.247299 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0a7a1f5-d46d-3315-8a7d-6a7aa736d41a | -1.0776 | -54.1059 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c11fb460-a7ff-3236-b178-47547d6c7027 | -2.9758 | -53.2551 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4728909d-8cda-308c-aec4-815267e765da | -5.7484 | -45.050999 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b516279-98f8-3f39-bef3-6160894419fa | -3.1685 | -54.097301 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 635c6f36-6f10-3801-a188-cda1d380bc65 | -4.5635 | -46.583 | 2026-10-03 00:52:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 781265a9-80e4-3400-add0-a248753554e9 | -1.8552 | -54.889599 | 2026-10-03 00:52:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0cc032-0b6a-36ba-bde2-24120e233eeb | 1.7434 | -50.801201 | 2026-10-03 00:52:00 | METOP-C | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bb9f99f7-5be4-3e38-9ffe-39c4b6ba6806 | -3.0156 | -53.8792 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd522db-a59f-3784-9605-8645c90ec50b | -2.9217 | -54.099899 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0705e936-4e0f-3654-baf9-05e3bc62232e | 1.8016 | -55.576099 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac94ec52-ed8e-3ee3-8e45-950713348af9 | -2.979 | -53.268799 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e74a896a-db8c-3189-b0f3-2b3b928d76fd | -2.9676 | -53.264198 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 812bf48b-c91b-3f93-9449-373377c59ad4 | -11.4367 | -43.377201 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02021e74-9528-314d-80ff-55e6cb5ad0a6 | -4.7432 | -43.256302 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3976f8db-852e-340c-a1cc-a8fc44d677b7 | -1.089 | -54.110699 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa2ac6d4-ce1a-3cc5-af31-b301de409613 | -6.8308 | -59.264702 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c049c05d-f5fc-33e1-b745-afdefbda04ff | -11.4173 | -43.382198 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd7461da-4bba-35d3-a0c4-b89104f5d159 | -5.3716 | -56.060001 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efba49d0-5cb9-3190-9f40-354518452096 | -3.1305 | -53.750599 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bef713b-7003-3018-a8b3-36e3f65b11e2 | -3.7494 | -45.933201 | 2026-10-03 00:52:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a643986-aec1-3d4c-b4fe-c6f920a81d4c | -11.6345 | -43.544998 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46ba6811-f1a4-3501-be51-7b4564aed683 | -4.7384 | -43.278099 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1836e50-ef36-390a-bd9a-b490e173054d | -3.2836 | -53.834202 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e504754a-b834-3f48-9746-7768827a9cbe | -4.8489 | -43.019501 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0c53057-76a6-3755-b48d-642897570ddb | -2.8631 | -51.019402 | 2026-10-03 00:52:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2e478eb-7bf6-3da1-8f6f-9953282bc478 | -11.4308 | -43.3946 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac79b96f-ea77-3df8-9eda-12a3e16390b8 | -11.7107 | -43.478699 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c34bbee9-5aeb-3e50-a689-acd7ff26233b | -11.8067 | -43.5308 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 868e7d99-ade3-3f52-ba9c-c4470ab1b970 | 1.7932 | -55.612499 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28700475-4262-34f0-bf13-90f467dd146e | -3.7164 | -50.650398 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 343506ec-2dbd-39e3-b396-1913a49d9443 | -3.1241 | -53.722698 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f697cde-e883-35c8-b120-2bd74cdf6b3e | -10.9887 | -59.140499 | 2026-10-03 00:52:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd7060c-9d70-32dd-802e-d9e804921ddd | -0.9051 | -47.914001 | 2026-10-03 00:52:00 | METOP-C | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f663a74a-9102-39a3-8bb9-14930424b4b7 | -11.4637 | -43.401901 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dec177a-92bf-377a-b6f3-f85e1b1aaa33 | -4.4606 | -47.926601 | 2026-10-03 00:52:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87965dc0-e757-3674-90f8-b59cf39e3123 | -6.7361 | -44.127899 | 2026-10-03 00:52:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54fc2ccb-660c-3de9-81db-56f6a3c03d5d | 1.7884 | -55.588402 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83362f23-d67c-362b-94e2-515f09afb0b0 | -9.6974 | -57.458199 | 2026-10-03 00:52:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a105f2a-b79d-30c6-ac2e-ff514d947591 | -4.7798 | -55.711399 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f0e4d0-d029-388b-9544-33903305e0d4 | -2.0193 | -54.300701 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11359f34-264b-3553-bc24-a3c92b86788c | -2.8904 | -45.391899 | 2026-10-03 00:52:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57b59be8-bfb8-3183-9fcf-1625bcd6bc23 | -1.2639 | -54.558498 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a81a3e-4ec6-3536-bb5a-a8b8f7373ce2 | -6.2043 | -53.265499 | 2026-10-03 00:52:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc6413ac-2b12-3212-a593-4b5905d084b0 | -3.7066 | -50.652599 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b829870-005b-30a1-b24d-7432da2b8565 | -4.2732 | -50.737999 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c57951fd-f8f0-35eb-8b13-57c416656141 | -11.6456 | -43.5882 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f076a02a-53b7-38ec-8f6d-662adc5b58c1 | -4.3647 | -43.846001 | 2026-10-03 00:52:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42555e6c-e4b0-388e-abf4-6fc2d8cd4465 | -6.8406 | -59.2626 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 654a43e7-b26e-3ed5-8211-df26bb22619b | -3.1767 | -54.088001 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd97963-4ff7-3858-b7f3-49dc28c614e3 | -5.2574 | -55.916199 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c701f2-cb15-3688-af70-70a98b4dc60b | -11.4831 | -43.3969 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b71b8d9-4d2d-39a5-a3c6-40cfc911f00d | -11.7934 | -43.518902 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55e35db7-1504-31ca-bb58-5a466cfce7a9 | -3.1387 | -53.741501 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d14b1ab-c7f3-3849-93cb-574c957c55ab | -5.8606 | -53.476299 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2738fd0-5bfe-3e7f-a051-31f2037bad4e | -11.4405 | -43.392101 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b8204eb-50f2-34ff-a137-03f35985939f | -4.576 | -46.5924 | 2026-10-03 00:52:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3da102a-1120-31f7-8db3-a3276ba3a1e8 | 1.9227 | -55.8111 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d90ca357-72a6-34a7-990f-30c0c57564a4 | -11.8104 | -43.5452 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7594b274-80d5-3be8-82d2-e6579fa8c514 | -4.7896 | -55.709202 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd37ac5a-7932-31ee-b97e-9543704e5115 | 2.3507 | -50.756901 | 2026-10-03 00:52:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 10fd1dbf-2c70-3114-84ba-f9f80aebf19b | -1.2182 | -54.538799 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5492bfb-04f7-3cdc-919c-457cb78def2a | -11.6516 | -43.571301 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a118782b-e829-371d-9a8a-9c400878425b | -3.2425 | -54.512199 | 2026-10-03 00:52:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5ce0d1-9272-31ba-976f-32cea56ac3e7 | -12.862 | -44.6768 | 2026-10-03 00:52:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce86992a-f5d9-37df-aeb5-2b78a0649e0d | -3.2997 | -50.3223 | 2026-10-03 00:52:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e60a8bc-7ffd-305d-9e94-ccf8e706f1e1 | -6.0206 | -53.545898 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 125b31fc-f548-3d58-bdc3-8071db564214 | -11.4135 | -43.367298 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b14e605f-158e-3614-a9dc-fc094ed1ec64 | -11.7189 | -43.429699 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3502b6d5-6e4a-3de3-95da-5154dcc3afcc | -3.1783 | -54.0951 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
