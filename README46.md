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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33d4ee49-35fc-3bda-a6b5-9796b7257fe5 | -1.07903 | -53.3899 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f702edf-2c80-398a-82e7-e1c3f83ed917 | -7.13602 | -46.41509 | 2024-11-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa5799b1-15cd-3804-a58e-9340a4826c4c | -2.37677 | -50.43147 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5a732e-2bee-36be-a596-c9172e3469e7 | -2.36437 | -50.42213 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 065b9a27-651b-39e1-bfed-f8f406b7c20e | -2.77305 | -48.55793 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e456217c-521d-33bc-ab5c-eb3c7be2ffbd | -3.95051 | -46.92427 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b18ec37b-f042-306f-8c59-e118aecb74e3 | -3.96323 | -49.43116 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 561b01a2-5047-3c92-855f-2bfd4352b65b | -2.32308 | -50.68167 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20abf7ab-291d-34bc-a6cc-e8fbcb1317ac | -2.26848 | -50.49324 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69438e56-36c5-37bf-b4f6-761157964ec3 | -2.13466 | -46.41483 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4896357-517d-3259-bca2-119354efd5c5 | -0.58027 | -51.69995 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1d98a72-631b-3b86-8038-c73aa16f63d0 | -3.79757 | -58.97394 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 249b85af-0a4c-3914-bc45-31b099eda85b | -3.23943 | -53.93018 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 959859f3-f8c4-381e-91c7-ff343e21ab33 | -1.68883 | -48.20207 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b7a4da5-226a-301e-8a81-11013f246329 | -2.87602 | -47.87088 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31abebe-f71e-3a7c-aa53-4e27ba3004a5 | -4.41384 | -50.82547 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11721821-65af-3599-9593-51dcf624a076 | -2.45742 | -46.52883 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f32063f3-91ab-3b3a-b84f-17fdc8a7fc0a | -1.22712 | -51.80556 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 521ab76b-1479-3835-81ec-85d4cbfd951d | -3.37612 | -50.76879 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8a5f31-f52c-3843-aa5a-42ad3f7a608f | -2.32041 | -50.65143 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fd71fc1-e88b-3fb4-8f26-928746b6afe9 | -4.20675 | -50.69306 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 040d7de7-5d06-3807-b33c-fa1ef7527c58 | -2.05661 | -51.16629 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41bb98fe-2442-3b8f-90bb-b73dc3185a29 | -0.96631 | -51.6486 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3acb4808-d4d9-3e09-a261-1135100343a3 | -2.01963 | -51.19624 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 294ae508-d074-36ad-abbd-cb3fa0596246 | -3.91603 | -49.92704 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee005406-aa6b-3cf3-9471-6e06c51df4e5 | -2.2249 | -51.43136 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c87f0faa-0cde-3bdf-9e82-75034531667a | -3.43452 | -54.11667 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af53d15e-f812-3750-a7b6-0483ed920c53 | -4.18977 | -45.72593 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd6518fb-e440-378f-9fbd-973ee67bfb30 | -3.1805 | -50.27662 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 358a562c-98b3-3875-aaa9-68648278e149 | -3.86477 | -50.16635 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa364bb-8554-3aa3-b73d-75f62f0cc3a4 | -2.38504 | -47.88128 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6da663e-01d8-35eb-a01a-8a4c3227756d | -3.85281 | -46.66711 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ea0ae16-932e-301d-9580-8abae1d24d2e | -6.90636 | -43.54693 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 7d356258-bba6-37d1-b039-8ee4f11a3f7d | -2.48264 | -50.36253 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9abf7f29-ee6f-373f-97f2-aebc9f6d0f0b | -1.19746 | -51.75808 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c07a6971-fc7a-3b63-9bd5-0c18d9142c6b | -6.91629 | -43.53979 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f0562834-250d-34ad-af44-4cde7b409a5d | -1.74567 | -52.65474 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b62a3d86-cb21-3e50-b26d-71f748e378b1 | -2.08649 | -48.55253 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4691f7f-a6f9-3ef6-af65-173c50c73593 | -3.96148 | -48.83201 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0afc06a-fd79-3134-af67-cb7284bd4d69 | -3.58182 | -46.35258 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8f393ed-e881-340d-8ce6-78062941f6ce | -2.5782 | -49.99753 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b77c51f9-7a09-31c0-9e02-4e784d39d25f | -3.93752 | -47.98036 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7026aee8-f317-37f2-b5c6-96787233cf4f | -3.04564 | -48.48778 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b1c556-570d-3b95-9eed-0bc46751b787 | -4.23325 | -47.57546 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3290da5-2230-3d5a-addb-13b1891041d8 | -4.85304 | -45.5644 | 2024-11-30 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 198e4459-5380-348d-8029-162ebbf4e715 | -6.91371 | -43.52638 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 343bbf54-4e99-3bbb-99b6-78a3c545d6ad | -3.41479 | -50.32428 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a15c75d-6385-3737-9e7f-71f0e22adc53 | -2.76484 | -54.04857 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 868fcb05-49dd-380f-b7c6-6ffc1d77e721 | -1.19465 | -53.87159 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2470f0f3-62e4-3595-90c8-021ec3dce221 | -3.70587 | -45.6831 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca780268-6516-3663-92e3-3cf9bf4a9c15 | -4.04777 | -46.86065 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6e98954-73bb-39e5-93cf-8c8c93a327aa | -2.44361 | -48.44303 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d2570a2-3883-3599-8d89-ad81c3ac7b8b | -2.22806 | -50.50151 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef5d0e8-e9df-34d9-857d-240fa4fbf9d8 | -3.67763 | -49.9287 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 518a506c-08c8-3e7a-8739-2d8be6fd41d0 | -3.54174 | -50.18779 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff30a242-2516-32f4-8c6a-9804f500f8f3 | -6.00427 | -57.83881 | 2024-11-30 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fefe2fc0-6bd1-3a3f-8f05-774eb8baec9c | -3.34014 | -53.28737 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0de31ed9-4f33-3d76-9cfd-b3e648d36651 | -3.25298 | -53.64902 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59cd4b20-2c5f-3944-88a8-54856aa7f27b | -2.49519 | -46.23518 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57b45610-add9-33e2-bf91-6e2e9a19f277 | -3.38622 | -50.35269 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00496bd1-40ea-3af3-928b-a46d7886d772 | -1.49359 | -51.9949 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e21ceda7-b28e-3578-9fdf-732949eab946 | -3.95195 | -48.16973 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9208ac85-6740-3ab9-8e05-f448de52fc3c | -1.98629 | -51.51749 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 935eaeaf-0daa-3c6f-9663-42dc55ad4a7c | -3.17994 | -50.28017 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11408494-a7a5-3e00-8780-b730c79ff280 | -3.3013 | -50.75717 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db583ceb-8715-39d9-b2f0-02ed841c7091 | -2.81059 | -54.02357 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6edfbb01-f24f-3390-b9d1-c1c2eda06374 | -1.18955 | -51.76116 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc1a4652-e496-3ba1-b8bf-9fcb1977b10b | -3.5032 | -55.40736 | 2024-11-30 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f40dcfb0-248b-334d-80b4-6ae26f5f649c | -4.35521 | -43.7053 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a60b9315-1480-3c9c-9699-a5af062478a9 | -3.60484 | -49.98171 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6be2a2aa-9c1b-300d-9788-2ddd4750de78 | -3.93799 | -46.70373 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60f4b032-b432-328e-990a-d9d600efac66 | -1.05012 | -51.73727 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9d1f4f3-9ae0-3130-a9d2-708929106058 | -2.52126 | -48.18663 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4874e547-d19f-3805-b2d9-2e92f65048ea | -3.42051 | -53.88766 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8d4734-24b5-31d2-9cbd-9baf1414e8c8 | -3.02561 | -53.41302 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ad33a1e-4422-304e-a7fa-f86b21e29682 | -2.64324 | -49.91017 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8fa6e23-b206-3632-8a4b-b3c1d7b34dca | -2.9772 | -53.28399 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f5656aa-f4de-3b23-990a-e23e66e63abf | -1.28095 | -51.73117 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 624e5f67-8b09-397c-949a-f9659287fe26 | -2.8515 | -48.09587 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 826577de-948e-31e2-821e-0d1d1aaa03e1 | -1.36916 | -52.5569 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daf93668-6930-35ee-96bb-5a143caadcba | -2.3773 | -47.88723 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04766cca-6761-3d83-9243-87ea5fee953d | -4.41046 | -50.82495 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f58e560-f533-39b1-aa34-48e57c097f12 | -3.0806 | -53.29219 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c26f434-5aa7-30ef-ab55-1bd9b435df98 | -3.69922 | -45.67771 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f505dd1-8156-3d76-a75c-38c2fa0d8a59 | -2.4643 | -50.38199 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c261e1bf-8b63-33cc-bb94-52439c9b6462 | -3.05934 | -49.53344 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb28d072-cf05-358f-a76d-766f47099f64 | -2.24166 | -50.48118 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e645d7fb-86ad-3290-8aa4-6435f499da61 | -3.7496 | -50.05496 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c8abaea-183e-3c0b-8a55-c585138184a7 | -2.71523 | -46.12225 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b80a1119-48fd-3a02-82c4-f4f3ce978b1a | -1.29524 | -51.37099 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cde986d6-f4b0-3afe-b676-84ce104da64d | -3.96675 | -48.11818 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11cd0667-8cfc-3a0c-8678-76abae978c4f | -2.63131 | -46.88121 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20edc5ad-9d61-3d58-b006-421d5ddc63c6 | -6.38537 | -44.75712 | 2024-11-30 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a87505dc-7c30-3392-b2a2-4a1c83826b0c | -8.38686 | -44.473 | 2024-11-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce1ce49-a40a-3dbb-968e-3078c7dbd536 | -2.62218 | -47.77779 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 867d91f0-ee1e-3941-80ff-7a629055d9f6 | -1.5936 | -52.28868 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 710e6817-d0db-3afd-9530-109f6bab502e | -3.42449 | -53.88833 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e089fdd-1c78-35af-bb20-c950c65ff99d | -1.36587 | -54.65587 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6cd0dcb2-4979-3aef-ac6d-f40870a13719 | -2.37452 | -47.88323 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b862993-6775-381c-849a-9bdebac93810 | -2.68145 | -46.10604 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
