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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 685e99d3-9057-345d-a3e1-0bcbdbd9c92b | -2.6169 | -54.154202 | 2024-11-17 01:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3aee763-5144-371a-8369-82b61fcd1982 | -16.105101 | -60.081501 | 2024-11-17 01:09:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb37ae33-570c-3af8-9e95-4818457fb7aa | -1.1325 | -51.687302 | 2024-11-17 01:09:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ad7322-9dc2-3201-8386-74cfd80c5b29 | -0.1031 | -51.601398 | 2024-11-17 01:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 187ba415-6bc9-39b0-97f8-e735e38f8018 | -12.5525 | -57.765999 | 2024-11-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1bf0e0d-2c00-37d1-a11c-e470b4c9c98e | -3.7037 | -51.835602 | 2024-11-17 01:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90322abd-16b2-3788-886a-c014a513f335 | -12.3915 | -57.507801 | 2024-11-17 01:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8e48213-b58e-3a53-bc41-3960f1983707 | -19.494801 | -56.603199 | 2024-11-17 01:09:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 354a052c-66f6-3582-a71e-8b83e77590ef | -12.3946 | -57.5219 | 2024-11-17 01:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76f87125-c9af-3cfe-9df6-97dca094775e | -3.1751 | -53.245701 | 2024-11-17 01:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cdaadbf-d8ce-33ee-98c2-5df153d5a9ac | -16.0791 | -60.104198 | 2024-11-17 01:09:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5499e564-d563-3081-8673-c3702a324673 | -3.5589 | -50.245499 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c691c68e-52f6-3d1c-980f-bad98d6da494 | -12.5635 | -57.814999 | 2024-11-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4537e316-c944-3ed7-9914-3a78bf5a68aa | -2.2214 | -53.600101 | 2024-11-17 01:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a41ac6cc-0eb3-340d-99c5-aa6bf55b7d04 | -12.5509 | -57.758999 | 2024-11-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb99db59-71b1-30aa-8e14-94a118d5ca8c | -2.5976 | -51.791199 | 2024-11-17 01:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8c552c-550f-35af-bd93-1c852ed46c8f | -3.5148 | -50.231899 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be4bf56a-a61d-35ac-b6ce-ad753a29bbb1 | -2.9837 | -52.605202 | 2024-11-17 01:09:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f53be4d8-19ee-3169-a05a-313ea65d7cad | -3.4838 | -53.994202 | 2024-11-17 01:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 967a7714-7a61-31b4-ab86-aeca99c8607a | -3.5106 | -50.257099 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 141093b7-409c-397a-a3a0-335674067f01 | -16.0774 | -60.0961 | 2024-11-17 01:09:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f16241cf-4d67-3b51-979e-0ea456bb05e6 | -3.4808 | -53.981602 | 2024-11-17 01:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd91d2e1-b519-3e64-a093-3437eeccde8b | -16.0595 | -60.108501 | 2024-11-17 01:09:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5ebf054-df3d-3c49-a365-a37445e3f46a | -0.9341 | -51.711899 | 2024-11-17 01:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 44d6ffcc-cd4a-3497-936b-1b8ac3f8888a | -22.4072 | -54.572201 | 2024-11-17 01:09:00 | METOP-B | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fcb9d9ee-0b42-3ce8-a689-2fffc74840e0 | -12.5541 | -57.772999 | 2024-11-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99877639-d81b-3145-bda7-f0e989cc3f4a | -3.3172 | -52.758801 | 2024-11-17 01:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5029c6cb-e546-300b-9556-fd1bb9400d83 | -3.5299 | -50.252499 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b01553e-a24d-3e98-ad78-503691450f86 | -4.5614 | -48.0141 | 2024-11-17 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f6f1684a-5058-304b-a7fc-6a974fbed7a2 | -3.5851 | -50.5255 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f2b5305d-c39f-3c51-b84d-b59dbb52fc0d | -1.5073 | -47.3996 | 2024-11-17 01:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fc6d23a8-777e-3b9b-8a13-313e61f65f97 | -3.4968 | -53.995 | 2024-11-17 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 60d68327-ed10-3224-9bac-078159069031 | -2.6595 | -46.2065 | 2024-11-17 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 294e3739-fe8a-3859-917d-2096188d89ed | -2.6141 | -54.1575 | 2024-11-17 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1640de48-5991-3ad4-be86-65c2408e0670 | -2.8614 | -46.7306 | 2024-11-17 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 02a04b89-a888-3894-93e0-ea19f36861d9 | -3.4784 | -53.9955 | 2024-11-17 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 396165ba-ec53-3907-ac12-c725e61b2b4f | -2.6173 | -47.5482 | 2024-11-17 01:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b06c11be-483b-3058-80a1-f8dee3e47595 | -2.9582 | -45.7957 | 2024-11-17 01:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 943dccef-2fb4-3ebc-a80b-4e8e279b24f0 | -3.3359 | -52.7643 | 2024-11-17 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 779171f1-cc9c-386a-bfab-c515e478d6b9 | -2.8295 | -45.4868 | 2024-11-17 01:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 95e9c6ab-e63e-3b70-8429-ee8d921c84b0 | -2.6322 | -48.5634 | 2024-11-17 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c5eb24e0-5e37-32fe-ab6b-ae6827486b2f | -3.47 | -43.87 | 2024-11-17 01:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7a46a09a-9f73-3826-a5ba-e949effa7d23 | 0.6159 | -51.7676 | 2024-11-17 01:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f7139b68-57f0-3ae1-88ff-09185b0ce275 | -2.8615 | -46.7086 | 2024-11-17 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 64c0e123-eb57-3d17-a241-2e71062bd369 | -2.5802 | -47.571 | 2024-11-17 01:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| a04ef841-487e-30d0-96e7-b62ac2b961aa | 0.6159 | -51.7881 | 2024-11-17 01:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 137e6dd3-2625-31e3-8994-2a949cbb79e6 | -3.531 | -50.2337 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 46abf83e-35ca-3102-9d11-c6992d16c5d2 | -1.9167 | -46.5584 | 2024-11-17 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 184.9 |
| ec28d885-ea22-3aa8-8c35-0874f2afcd4b | -3.5124 | -50.2553 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 3d22f0ca-012b-3bdb-841a-6c66beec266c | -4.5616 | -47.9925 | 2024-11-17 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| eb5fcb69-74ad-3015-8aeb-1ee1b13a6f45 | -2.678 | -46.2059 | 2024-11-17 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6ccd2fbf-3627-3fcd-bdb5-053f8568fb38 | -4.4866 | -48.1045 | 2024-11-17 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f8fe2cef-b9e0-3994-a1ae-5b8973ef5c50 | -4.5799 | -48.0349 | 2024-11-17 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e9c8f739-d908-3385-a1fc-fba6c385eb9f | -4.4103 | -45.5069 | 2024-11-17 01:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 526d3316-8282-33e6-8079-0c774d3517e5 | -3.5309 | -50.2547 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 279.0 |
| 542287a4-c532-3760-90b7-137c6ce9ec25 | -3.5308 | -50.2757 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3a379687-26da-358a-b9c0-e60c1e02369b | -3.5678 | -50.2534 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d2c593ee-cee9-3674-abf4-a87f914fe813 | -8.4336 | -44.2019 | 2024-11-17 01:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| cad658b4-f220-31f9-b40b-b5c0c8874490 | -1.8982 | -46.5588 | 2024-11-17 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b4b1bc45-7e82-3e87-b7c6-aa56cf0dd45f | -3.4698 | -43.8931 | 2024-11-17 01:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7aeb3501-ac86-33ca-baa8-db1005cb6a0b | -4.58 | -48.0132 | 2024-11-17 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c0928576-3dfd-33cf-bf37-08673fafd003 | -2.8801 | -46.7079 | 2024-11-17 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 6051d3b2-0288-3dbb-bbe2-5409b040fb7f | -1.9166 | -46.5804 | 2024-11-17 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| a5e73a6b-451b-34ad-9353-2bb1cc9d4f05 | -2.5988 | -47.5488 | 2024-11-17 01:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| fc030022-44f0-35e8-ae95-41228bfb1099 | -3.5494 | -50.254 | 2024-11-17 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 0549ad06-9bc8-3329-aa34-e056a5239760 | -8.4525 | -44.1999 | 2024-11-17 01:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6df0fdb1-8665-3558-b3ff-c839d26a6e45 | -2.5987 | -47.5705 | 2024-11-17 01:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ac333f8f-9733-3650-a9e7-1acf77fb68d2 | -4.4101 | -45.5293 | 2024-11-17 01:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 2afe16c4-c448-3aa7-aeec-f5e8f81a99d8 | -1.8981 | -46.5808 | 2024-11-17 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8c550989-9af8-3d1b-a6f2-ea1653a3ea72 | -2.88 | -46.73 | 2024-11-17 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| cfdcd561-d7f6-394c-a877-f1bb0534f2aa | 0.6159 | -51.7881 | 2024-11-17 01:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 115ae33d-736f-3060-8cb3-7c7ccb1387ed | -8.4336 | -44.2019 | 2024-11-17 01:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 5f01eb7a-20b2-3344-89df-8cd157f15690 | -1.9167 | -46.5584 | 2024-11-17 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 60f9e279-8b17-3afd-acdd-ba244f60298e | -4.4101 | -45.5293 | 2024-11-17 01:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 6a43c951-e944-3e62-84b7-0e0080defbd3 | -4.3012 | -48.0917 | 2024-11-17 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 02835663-e2f8-3626-ba68-7b12a96b4a8f | -4.4681 | -48.1054 | 2024-11-17 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7859ae73-f115-3e67-9f7b-8467e2b26bdd | -4.3915 | -45.5303 | 2024-11-17 01:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| fceac17e-933e-3130-85af-17bec4ad5498 | -4.4866 | -48.1045 | 2024-11-17 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d82c7bfc-41a2-364e-b513-32167b4ff8de | -2.5987 | -47.5705 | 2024-11-17 01:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 8b2457bf-be01-38ec-b39e-e286ac208709 | -8.4525 | -44.1999 | 2024-11-17 01:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| ed80ffdb-33b8-3e33-a5b7-7db2ca1f8420 | -1.8981 | -46.5808 | 2024-11-17 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 7d72e7b4-1fa5-3a9b-b2dc-71fc0fe14117 | -2.88 | -46.73 | 2024-11-17 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4cb0b553-9eca-34b2-9ec5-aacbd0ee7b79 | -3.4698 | -43.8931 | 2024-11-17 01:20:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 25d4279a-7450-351e-bd80-60a106ebf575 | -1.9166 | -46.5804 | 2024-11-17 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 19f4c5fe-7171-3b94-a024-eb99e30714d6 | -12.4004 | -57.5127 | 2024-11-17 01:20:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 49d592ab-1dbc-3901-99bd-154d1bfded74 | -4.4103 | -45.5069 | 2024-11-17 01:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d7625ff6-75fd-3f53-977e-6da9237e57a2 | -4.5614 | -48.0141 | 2024-11-17 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f5fbb431-b664-3278-8434-65a8b78b6756 | 0.6159 | -51.7676 | 2024-11-17 01:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a6c2a1c3-23ac-3335-a496-311db5c333df | -3.7931 | -46.0297 | 2024-11-17 01:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9b76acfc-e56e-3b2a-87e4-709e459b1ce9 | -2.678 | -46.2059 | 2024-11-17 01:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 6b15099d-9e85-3c90-9ba5-f9a81b2a6976 | -2.6325 | -54.1571 | 2024-11-17 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 35b131bc-40a6-363f-97c0-ba487b3c81d7 | -4.5616 | -47.9925 | 2024-11-17 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8f52f7e1-5675-3b1a-9e6c-c9be27e55419 | -3.4968 | -53.995 | 2024-11-17 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c60d46a9-01d3-33ed-bd34-832d35589b5d | -2.6595 | -46.2065 | 2024-11-17 01:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 731537a9-4199-3f92-a8ed-12cca98ea64d | -2.8615 | -46.7086 | 2024-11-17 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 9699b8d9-c9b2-3d06-ada0-0ade9645ed34 | -2.5988 | -47.5488 | 2024-11-17 01:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| cc1e99c4-cfe2-3465-aea8-894731d9ede3 | -1.4888 | -47.3999 | 2024-11-17 01:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4b1494e8-7150-314f-b0c3-679daccdea9c | -2.8614 | -46.7306 | 2024-11-17 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 812c4712-5a04-31b2-8a24-c141bd55aaba | -1.8982 | -46.5588 | 2024-11-17 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b36830e4-0e7d-3475-b379-10737b094ab7 | -3.793 | -46.052 | 2024-11-17 01:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |


[Clique aqui para ver as próximas entradas](README17.md)
