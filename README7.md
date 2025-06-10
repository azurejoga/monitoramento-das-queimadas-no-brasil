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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 660bf3a0-b3b6-365e-866c-5b4683186a30 | -5.2108 | -43.3067 | 2025-06-10 04:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b92ff558-babd-37a5-89f2-4ecdb3e41b8f | -6.20214 | -43.32843 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5481c654-c29c-3e4e-a4a1-68c858bd9cc5 | -2.52175 | -43.25358 | 2025-06-10 04:38:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6d2a0aff-838f-371e-98c8-745eb14ac557 | -5.20563 | -43.31076 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 689b73bf-aad1-33d7-a769-94cd1b1af710 | -5.20813 | -43.3236 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6abb2ef-3038-3a45-8cdb-5927c777d4ad | -4.30778 | -48.0789 | 2025-06-10 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95196f0c-f89a-30b1-b27d-780b61ab3306 | -5.20931 | -43.31552 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f80367ba-9e10-3ce1-bd84-5cf876501d25 | -5.20989 | -43.31148 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27b8f562-dd5f-370f-a36f-f474dec9502b | -7.0242 | -44.57074 | 2025-06-10 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab99e72-855f-3d6a-a8f2-58f893009311 | -4.30832 | -48.0754 | 2025-06-10 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69702a11-f46b-3779-bbfc-3bbb807e12bb | -4.15859 | -50.2273 | 2025-06-10 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74003940-22a4-39f7-ad1b-a85a837965bc | -6.20914 | -44.51286 | 2025-06-10 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f176d002-c067-38f6-a367-5604bc7fd310 | -5.78339 | -43.62173 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40ce5254-8e22-3951-b699-46495980ca50 | -5.21533 | -43.30415 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb20af3d-184f-3bf8-a123-4b5ded48b854 | -4.41898 | -47.6652 | 2025-06-10 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7831c38a-bf30-3ee3-83c6-2d206faafa91 | -4.42536 | -47.73553 | 2025-06-10 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1dc5342b-cd74-3575-a8ba-5992c02c6ba4 | -5.47719 | -46.22905 | 2025-06-10 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee8c0a5-2bd8-35a2-9611-d3d9611d7906 | -6.75758 | -44.98955 | 2025-06-10 04:38:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff975f8b-59ff-3e4b-a627-0ebda38d29f7 | -6.34393 | -43.3698 | 2025-06-10 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71439b36-051d-3022-a91d-7439c50133eb | -5.64842 | -43.59664 | 2025-06-10 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 59337759-339a-3b64-80c4-ae4d0c461d57 | -5.79467 | -43.48724 | 2025-06-10 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4311bb4a-392d-3dc9-9867-53b8bcaf7f62 | -6.22009 | -43.32685 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e46839e-05b4-3e71-924d-07e6fde27daa | -5.21284 | -43.29121 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17f8060e-dd65-3a58-901f-da083fe4b6fa | -5.65206 | -43.60119 | 2025-06-10 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bff5a33-c467-3d6a-a833-4e9109e03604 | -5.77994 | -43.61478 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6cc3ef5-2656-3b01-9b2e-c9c9cf0b6f79 | -5.20386 | -43.32292 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e185d01b-8871-3aa0-a75a-f41eb64f4c76 | -5.65148 | -43.6051 | 2025-06-10 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4c8c596e-18c0-39ae-b3f4-6fb2da287a59 | -5.22079 | -43.29674 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 785eb012-44f9-32db-9f8f-6198a1f1963a | -5.77439 | -43.62432 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c98f8e6-ac76-3686-8212-89233487ddf1 | -7.01285 | -44.61988 | 2025-06-10 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f638f944-7788-311d-abea-31ab78f1cfb7 | -6.3455 | -43.37194 | 2025-06-10 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83b99452-e661-335e-b132-b442b0505768 | -5.78706 | -43.6263 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6aab2d3-928d-3bdb-8c3e-51bb2cc54664 | -4.305 | -48.07488 | 2025-06-10 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1395b817-8461-35b0-bd50-046c29aaad3c | -5.21416 | -43.3122 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5818a5db-3379-3ca7-aef9-826bb0276ac8 | -5.21357 | -43.31624 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 58074815-4f4b-37ce-966e-d2ef4cd77da0 | -6.32797 | -47.33666 | 2025-06-10 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20aca46d-1cb9-3424-aa18-a36325bb8c50 | -6.21513 | -43.33048 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28a39d1e-7e18-38b3-833e-6fc588743c7e | -6.20964 | -44.50944 | 2025-06-10 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab09222b-2cee-35f5-befd-6fcd4a47f38d | -4.42201 | -47.73499 | 2025-06-10 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 07e77a38-4785-373d-b79b-1c1086658be7 | -5.64784 | -43.60056 | 2025-06-10 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a448bd8f-83c4-3fe9-9886-e803c394d259 | -5.21106 | -43.30343 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 667879c6-6bd2-3c00-8494-80e04e2bfec5 | -5.21784 | -43.31696 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 062e88f4-dcbb-30b5-a925-7c1de12fec17 | -6.33645 | -43.74476 | 2025-06-10 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e77d15b-506f-3092-bb53-be783da41b1f | -5.81761 | -46.48911 | 2025-06-10 04:38:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6002ed-e640-3ac7-9e78-057ad45e88e6 | -6.19349 | -43.32697 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 465200e5-0890-3bc9-964d-5a33c13befba | -5.20679 | -43.3027 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e5f527f-1c4a-38e5-a908-86d897390c61 | -6.20154 | -43.33254 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9a249126-85de-3a17-994d-2defa0e32832 | -5.77572 | -43.61414 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b19c2fee-b773-3b62-9494-9aa7040af6f3 | -4.24824 | -47.5839 | 2025-06-10 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8dbf4531-4a9e-3f17-80dc-fabb3b2b816a | -6.9531 | -42.80151 | 2025-06-10 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| becc6336-d5f6-376d-8fbd-151936dd8f56 | -6.21013 | -44.50597 | 2025-06-10 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8ad60fb-5c40-3b89-a421-0c8bc181f2f8 | -6.21139 | -43.32573 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e9d0a1a-85f1-3192-974e-b10c1b4c66db | -5.91426 | -45.52237 | 2025-06-10 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7877aa89-310b-3cc6-a99d-fc4d8475c344 | -7.02263 | -44.58141 | 2025-06-10 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4fe012f-466a-3b48-9128-fb391ef07028 | -5.20855 | -43.29054 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 767f8f0a-57ed-3e19-ba30-5bb43c98ed60 | -5.21223 | -43.29535 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63e60fa5-bb2f-39f1-81e2-84ab2d17a19b | -5.20445 | -43.31887 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eca3bfd6-b729-3f9e-9f56-8f6e50ae0c0a | -5.64902 | -43.70819 | 2025-06-10 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a015a730-813d-3420-a236-f28f16a94d79 | -6.21574 | -43.32632 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd16ca1b-876b-33b8-afaf-36ef28eb9482 | -5.21165 | -43.2994 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e9a8a40-0366-3040-bc6f-ce3926e23d63 | -6.19721 | -43.33184 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 78a155ae-2018-3fcc-b475-fa949fc1b7a1 | -6.49126 | -42.85131 | 2025-06-10 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| a5b70813-e69f-3356-8b83-fe35528494d7 | -7.01233 | -44.62341 | 2025-06-10 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 695277e0-0b16-37f2-af21-89e3a9efec21 | -5.21711 | -43.2919 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7758c03-023b-3ba2-b397-97804644b818 | -5.77456 | -43.62193 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c29bf5e-0ca4-3297-b378-ffab5d4a5d97 | -5.21901 | -43.3089 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45f072df-92c2-334f-a6f8-a91a2a849a59 | -5.21475 | -43.30817 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee00de1c-5583-358d-a4ed-f2e1bb31a65c | -5.81821 | -46.48512 | 2025-06-10 04:38:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b395374-a877-3301-b8f3-4a629644d1f6 | -5.91732 | -45.52744 | 2025-06-10 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bd84280-5d92-38af-b05b-e9fe1dd074d4 | -6.85012 | -43.5743 | 2025-06-10 04:38:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22110b22-c763-3b1b-8577-f7b26ae195e4 | -4.81851 | -47.32179 | 2025-06-10 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50444d3e-5e9f-315e-b10a-11908e618374 | -4.82045 | -44.35426 | 2025-06-10 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f19dff71-1205-3883-9990-f30c71a6a47e | -5.77397 | -43.62583 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f12692e9-803c-3ce6-b799-0b7e870686c2 | -5.77861 | -43.62497 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 497d11af-4cee-3183-8536-863e676ba384 | -5.21048 | -43.30745 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8a84cc8a-f542-3784-af53-075a4d69ea35 | -5.20135 | -43.31011 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f197a3b0-0ebf-36a5-a6c1-85e9d83972ad | -5.21592 | -43.30011 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f428b6-402a-38f0-9704-4407cfad2bcc | -5.21298 | -43.32028 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0bda806a-22e5-3793-b9da-3ea832d2058d | -5.78028 | -43.61325 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cd0c3cd2-de58-357d-bf4e-fa225ba9425a | -5.41437 | -49.08165 | 2025-06-10 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0ae2439-6c84-3bfa-9d14-106de02dbfe7 | -5.21651 | -43.29605 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78e644bd-2a77-3d25-8229-222a771dcb51 | -6.19288 | -43.33114 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8544f6b-4b22-3856-b926-e5099392d954 | -5.77605 | -43.6126 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38e13556-5189-3905-a4f7-084bd0e69cd1 | -5.20872 | -43.31957 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5757333-8ea5-3594-b0d4-56c26b6cc320 | -5.20076 | -43.31419 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fe77129-7800-3fb4-94dc-bd392878d3fe | -5.7782 | -43.62645 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c98a031-d86e-3ff3-9105-4d7933bfd940 | -5.20621 | -43.30672 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d3690b0-a0f5-3437-a927-80fac956891a | -5.20504 | -43.3148 | 2025-06-10 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c23d8510-05c9-3830-ac79-eb5331f9a390 | -6.33142 | -47.33718 | 2025-06-10 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18f4d2ea-2ae9-3f58-8c41-67c3ae702006 | -6.19781 | -43.32768 | 2025-06-10 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 68a1cb6e-04e3-3d23-83da-7734fa601932 | -5.2106 | -43.33 | 2025-06-10 04:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 8addeee2-db18-3904-bfd3-6335b525c675 | -5.1921 | -43.308 | 2025-06-10 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ec4d0018-97e4-39fe-b653-45afed85daf0 | -5.2108 | -43.3067 | 2025-06-10 04:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| fd780f3f-30da-3c85-af1e-c344f1dc1cc5 | -13.06518 | -49.25433 | 2025-06-10 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 228abe78-3d6b-3105-a235-15edb8422419 | -14.21653 | -45.49608 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e81c6e-5ef2-3494-94ef-3b431713c340 | -10.8434 | -53.76662 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 17e6626f-fad5-3fbf-bfa8-66c8bdfc8ffb | -9.86348 | -47.88384 | 2025-06-10 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64dd052a-a61c-36c2-90f9-42ce727a9488 | -12.20797 | -49.61816 | 2025-06-10 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88fc4c57-69c5-3e1a-afef-c833b9ff18ee | -9.21319 | -48.86486 | 2025-06-10 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de4dc8e9-4c7e-3d38-bf88-8fd2bf9202ce | -12.10912 | -49.4845 | 2025-06-10 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README8.md)
