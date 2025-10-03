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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fdeba19-cc14-328c-9a56-bbdf410c2e50 | -11.81174 | -45.03039 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d54a6881-46e6-3b68-8c36-c9551f94aaca | -9.9173 | -43.76852 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 97a6348e-4f0a-35fe-bc1c-99dbfea8dd56 | -9.06408 | -46.65553 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd4ef0b-7cd0-3db9-a380-d54680ee1e68 | -11.14864 | -43.40065 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4de30c9e-3877-3181-9eb9-4d5dbbe386bd | -8.53914 | -50.15811 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ea6ba1a-591e-372f-80c1-4c5011400639 | -11.6187 | -45.06057 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77c175fe-4f52-37ab-a282-b1b4a8f819ff | -10.59313 | -48.71735 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21040e78-3d06-3aaf-a9b7-39f77c425451 | -10.87367 | -47.04643 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eec9b491-24bc-3226-b87f-96580fd63063 | -11.21425 | -49.95489 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0e973ab-dca2-3c32-8f62-525cf3c31b4d | -6.28232 | -44.05203 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4ddc146-fcea-39e4-9dcd-921142608fc3 | -7.44755 | -46.46598 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6e35eb7-80f7-388a-bd1e-da607d643820 | -11.28786 | -47.83507 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ae026af-a482-3721-acdd-987e5cba941f | -9.34254 | -45.75653 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85756f12-e0a2-39b1-9e5a-dd951341660a | -12.53923 | -43.1882 | 2025-10-03 04:32:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5cd6f6b-0dbe-3296-af0e-edde48712ae4 | -9.77018 | -46.22591 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be440e6-5e08-3ae6-8994-d00dde92d5cf | -6.05277 | -44.63557 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c87fa170-0ae7-36d8-a683-08c00b3da260 | -7.78009 | -42.57693 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8b45c6a4-770d-3767-a13f-1151e72d2d18 | -10.00107 | -48.2714 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c2374bc-6b92-37ba-ae3a-a78901b3d9e9 | -11.18269 | -47.25187 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 457d1edd-9504-3adc-81c0-377c29883423 | -10.00696 | -50.2347 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5954a171-5276-3c77-965b-b62f533ff582 | -8.18815 | -47.00621 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3421c83-7ff4-3d52-a4b3-d7aa819e069d | -6.94154 | -38.57203 | 2025-10-03 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71154060-e3c1-384d-98b7-fe78290831b1 | -7.75626 | -42.56571 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1d6ace54-7d88-3f18-adf8-e788837c672a | -4.67239 | -45.79627 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 127f6509-39f4-3d7b-b20d-4e05b0749c5a | -11.68079 | -44.27601 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aefbe1ad-bab4-3d88-921c-f63a64a4a6fa | -5.62347 | -44.70419 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 608c39f3-3b5a-3bc1-ad59-a676fb784fed | -8.64765 | -47.72001 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ce7fc4b1-5728-3318-b31a-77fd1042fb25 | -11.86245 | -44.97398 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ceef05b0-9b4d-3da4-9ec2-64d971782af0 | -6.04796 | -44.64319 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fe7aa97-7273-3335-aad1-9aaba020661c | -12.29228 | -45.36527 | 2025-10-03 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d617ebd-34cb-31dd-bd15-df57998d4346 | -6.7337 | -44.57812 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21a85400-5e05-3ff9-b692-ce67ec9b4ef3 | -5.3723 | -45.70764 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a6ab7da-18c9-3c6d-83a6-cdb5fa5783fd | -9.14292 | -47.63639 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0acdddb7-a556-303b-b0ab-e7ad45baffb7 | -12.0012 | -46.57922 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 568a654c-1c0b-317c-baf6-c6c31f806caf | -6.04858 | -44.63906 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcabc9ca-22b2-3d07-9a4f-bf6bb04d9523 | -10.16438 | -45.49783 | 2025-10-03 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3525630a-6c0c-385b-8358-b5daf19041c5 | -11.47201 | -45.02894 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb0d3909-7bb1-3414-801e-a172b5d35e8d | -5.48593 | -52.13135 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1705159-ce21-3dda-9884-a9b29142c4d6 | -7.78486 | -47.37624 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99afe83a-d96e-3d8d-9240-702e0013da73 | -10.87425 | -47.04271 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08daa82c-1f9f-384a-ab44-4ae1e9fb61e6 | -8.01725 | -47.25835 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f66ea118-5681-3cf2-b5ae-1d28dd7244ef | -6.56247 | -43.8842 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38541f3e-4b82-3f89-aa05-a985e964f40f | -11.68342 | -47.50427 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ddd3878-965a-3783-a0a3-f2738ad5711f | -9.91361 | -43.79401 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ce44505-d707-33ba-9dd9-86b27465594a | -8.90373 | -46.60847 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 270bdb03-1279-3d53-a799-429b928e314e | -6.54098 | -45.80331 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0af4051-5441-3e78-ad5e-8431783cbd12 | -4.67127 | -45.80353 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04659257-efcb-3f58-91b6-68c55510c278 | -6.05696 | -44.63208 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4028dd7-ba9b-3a02-bf55-05945b2199c9 | -11.19126 | -47.73603 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 778612d5-4509-3481-bcff-bee646d07cfc | -10.90005 | -46.71345 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccea877a-dffd-3c9a-9a0e-0126ef601f4c | -8.90033 | -46.60797 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5144c15-cac4-32e4-9b2d-a2677c08ae7f | -6.41672 | -43.9283 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5be41737-872e-39e9-a2b1-67a4d863e939 | -6.20222 | -45.77566 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b37799b5-70d5-3af5-a18a-e37045941766 | -7.78839 | -47.3732 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 927cefd5-78b6-3aab-ba1c-334e92011c02 | -6.41298 | -43.92776 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7135a14c-cad6-3615-8007-fc0d26659e9c | -8.07986 | -48.22148 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b59b3b73-1942-39f5-a3f2-b4fcdff5e1f5 | -6.3559 | -44.75867 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 738eb5da-f475-3ce1-a68b-d398d530e1d0 | -11.91202 | -46.74846 | 2025-10-03 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8068624-a9fb-3762-9a1e-e80ea4fbca77 | -5.87536 | -44.12664 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c400e32-158a-3a8c-8138-91904fafc36e | -7.76139 | -46.24799 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a0cf2856-aef0-362a-8c0f-1c4166bf9a2d | -11.14372 | -47.1816 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fec18702-316b-34e0-b61a-cb8b8d2a3ee6 | -7.15916 | -44.99579 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21d52e79-cd7d-3f53-9b33-ca56437aec57 | -7.88689 | -47.35279 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7db624b6-0197-3643-9568-6885c472224c | -5.83934 | -53.67524 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ff8855c-29e9-329f-a47f-54157790bafd | -7.74373 | -42.59451 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dbd4a804-d9c7-359b-9b56-79ee6f733769 | -6.22774 | -42.93944 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| daca83fb-ff2e-39ac-8624-8912874f3267 | -8.61349 | -54.98029 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6f03ebb-f1ad-33ad-b5e5-a55fe4b78b79 | -10.30747 | -48.28742 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f238155c-4a31-37ef-8df2-5aaacc151fd8 | -6.53063 | -43.37827 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 235aaeef-0510-3111-b08a-d321afab894a | -10.89719 | -46.70912 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9b5b68-67e2-33b5-9704-573ac553e056 | -11.07136 | -47.80837 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e5eeaa7-08fc-3dee-b0ee-d871f77ee580 | -10.58817 | -48.7058 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c151be9b-f6e1-366c-a3d5-6b56111c26f6 | -8.89598 | -45.02975 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c2d2357-095f-3c7d-98b0-218aed6930b5 | -9.91201 | -43.72092 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 86c587f8-2c7b-3a8a-b4fb-08789450ef05 | -7.00265 | -48.63008 | 2025-10-03 04:32:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d17fe99-57ca-330d-aa78-0155fca929c0 | -5.64352 | -43.90273 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 210e77cc-57d4-35fc-b105-12450793cfed | -6.36306 | -44.75965 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b50f81f9-b522-373a-8e02-15cf1f5c63cb | -6.24057 | -44.25484 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c94bc33b-7bf7-34be-a2b2-0fed5696af5a | -11.47269 | -45.02431 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eabc67dd-295f-3a6f-8389-f37280ffae06 | -8.95868 | -40.6086 | 2025-10-03 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a249e994-51ab-3bb7-9ab5-809fb01e044d | -10.90693 | -46.71452 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb6ef7fd-ab1b-3f83-96c7-1bbacd825fe7 | -7.76912 | -42.59444 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 28cae719-f779-33d6-a848-8ed3a4c7630e | -9.90659 | -43.73046 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3b6ef95c-2c9a-3408-b2c9-1586d212fb6b | -10.87817 | -47.82552 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20b43307-91ac-35e7-b63f-4ac9bf92351b | -11.47577 | -45.02938 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd68b9b9-8329-3405-9b72-61e2708680f7 | -9.08156 | -48.02816 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9ebb6cb-835a-3485-bff5-59ad224987cc | -11.83525 | -45.00111 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d9d46af8-1fee-35d2-a3f7-fce89d9e80ab | -6.95002 | -45.34856 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15c5d183-cc6c-32ff-9852-8dda3e6fc189 | -7.76082 | -46.25174 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 69e0b9b1-8497-31b7-b225-0ae2c469d6c0 | -4.95237 | -45.77146 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0221bc6-27bb-3321-b851-a808e3efac2c | -7.78171 | -42.56559 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a4952128-87ad-3a1a-b47c-995c3d69fdbb | -6.03762 | -44.62614 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 950edc00-fba9-3650-9faa-a9c74ef18f7f | -6.05399 | -44.62743 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83d7e9a3-5948-3de6-8b3c-a65702513b77 | -8.56608 | -48.64802 | 2025-10-03 04:32:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaa62966-2387-3f81-9651-e879476712fc | -11.09692 | -47.70984 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9654e245-1eb9-38bb-91be-7da20aa1612c | -7.74836 | -42.57632 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89e28b6c-fdf5-376f-bd2b-d34bf360f88e | -11.90639 | -46.31879 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b089051-0c94-30d8-b7e6-61319ade9922 | -6.68394 | -43.71958 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cab7ac2a-cfff-33bf-ad9a-b41d0ae53b6b | -5.1339 | -45.437 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf232c83-d519-3c4b-9abe-b3ee74633194 | -6.37733 | -44.63991 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README95.md)
