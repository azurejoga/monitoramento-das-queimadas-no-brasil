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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4194f616-c29b-38c5-9e38-597f9100c00e | -12.1952 | -52.7821 | 2026-06-17 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 295.5 |
| 55b39304-c85c-3a12-b900-944597745f9d | -12.1949 | -52.803 | 2026-06-17 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 157.6 |
| c88f5db9-519b-3526-8c4b-e619e9ce7dda | -12.1762 | -52.7842 | 2026-06-17 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4dc58cbc-9eef-3b73-8355-86b8ef8095a8 | -10.9971 | -46.4741 | 2026-06-17 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 2531d008-4d83-3d5a-bbca-02c6297a0726 | -12.2143 | -52.7801 | 2026-06-17 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 436.1 |
| dd2f73aa-3600-36fe-8c60-5ea820bbe3b1 | -12.2333 | -52.778 | 2026-06-17 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0551fbe1-fd77-3549-8138-b6a0870e1fac | -12.214 | -52.801 | 2026-06-17 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 241.9 |
| daba870f-3004-3ffe-8106-5a1e166251f1 | -12.214 | -52.801 | 2026-06-17 08:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| bfe7b158-e611-38eb-a0c4-8b893367247d | -12.1952 | -52.7821 | 2026-06-17 08:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 16a09ddf-dc33-389c-824d-48ecda769369 | -12.2143 | -52.7801 | 2026-06-17 08:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 274.6 |
| 497c9b3d-ea7c-3528-980b-0e380c60be09 | -12.1949 | -52.803 | 2026-06-17 08:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| a2f786f9-0177-35a0-91e4-e6a73db74a4d | -10.978 | -46.4766 | 2026-06-17 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f1ae3506-ca59-3d0f-8ae7-2f1e403a8d39 | -12.8548 | -44.3625 | 2026-06-17 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0b8f4bd6-2c4f-36b9-874c-621e1d45da83 | -12.1952 | -52.7821 | 2026-06-17 08:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 27481b32-f936-356c-a402-089c688192c7 | -12.1949 | -52.803 | 2026-06-17 08:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| e3f85707-64ee-3db9-8ea1-3cdc3f65f531 | -12.2143 | -52.7801 | 2026-06-17 08:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 20c3601d-9d73-3179-bd30-6b6e395f1415 | -12.214 | -52.801 | 2026-06-17 08:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 9550e936-c484-39c1-9077-c8143f837ded | -12.1949 | -52.803 | 2026-06-17 08:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1b9b6e33-afba-31ef-bdc1-6baef6b1302a | -10.978 | -46.4766 | 2026-06-17 08:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a4c5d04b-5625-32db-9cdb-cb0dca3eee21 | -12.8354 | -44.3657 | 2026-06-17 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 836d8d20-06a4-3a44-86fc-358aff190698 | -12.2143 | -52.7801 | 2026-06-17 08:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 426d9e8b-f716-34b1-9a2a-e892bf203de6 | -12.214 | -52.801 | 2026-06-17 08:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 06cea50e-69fd-30d5-8390-5b908f9291e5 | -12.1952 | -52.7821 | 2026-06-17 08:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 60b4bb4d-22ab-3964-8744-a0e18b74108f | -12.8548 | -44.3625 | 2026-06-17 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c62f8677-2af5-3005-bffb-dcf8f5383fb8 | -12.2143 | -52.7801 | 2026-06-17 08:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 49a6d917-d82a-3630-86e3-117ecd41b3de | -12.1952 | -52.7821 | 2026-06-17 08:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 48e623d4-47de-368e-bb39-a00c6cfe291a | -12.1949 | -52.803 | 2026-06-17 08:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a525c7bb-df56-3858-9b8b-61bfe041a2c6 | -12.214 | -52.801 | 2026-06-17 08:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| b990349b-4363-3e00-953a-c007e9c042fd | -12.1952 | -52.7821 | 2026-06-17 08:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d8a0d248-47b1-32ec-95ab-b2dd3067df7b | -12.2143 | -52.7801 | 2026-06-17 08:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 6c87d88e-1343-3fad-87b0-03d696f81e35 | -12.214 | -52.801 | 2026-06-17 08:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 5618c007-ea4d-364d-b2b6-0aa5b7aeb00a | -12.2143 | -52.7801 | 2026-06-17 09:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| bfe8a983-d7cd-3ffb-9e9f-8fcf77504b2c | -12.1952 | -52.7821 | 2026-06-17 09:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1b57f549-eeff-31f4-9fed-26fb8d870fb9 | -12.1949 | -52.803 | 2026-06-17 09:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 82d613b4-9bb9-3953-a3cb-7d1b0566b15a | -12.214 | -52.801 | 2026-06-17 09:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 0c936b9b-358f-3452-a405-7d1fe5eff736 | -12.2143 | -52.7801 | 2026-06-17 09:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 8458afa0-ba17-3f17-acf9-01d7e35455a3 | -12.1952 | -52.7821 | 2026-06-17 09:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 7ae83496-0cb3-330a-9f70-1dca454cb4f2 | -12.214 | -52.801 | 2026-06-17 09:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 009ec221-720d-346b-992a-1a9a3eb04506 | -8.9821 | -46.9988 | 2026-06-17 09:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 553.1 |
| 87e375ba-ad1c-305c-9e87-192f940d37cd | -9.0013 | -46.9746 | 2026-06-17 09:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.5 |
| ff44279a-a661-3834-b4b6-af0bb322b9bf | -8.9818 | -47.0211 | 2026-06-17 09:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 8126bff5-fc81-3f1f-9e9a-383a9ec931e6 | -8.9824 | -46.9766 | 2026-06-17 09:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 508.1 |
| 4e2057ab-97e7-38bd-8d0e-265b3ff07305 | -8.9632 | -47.0008 | 2026-06-17 09:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| c151ef68-e692-3f86-831b-0b41a4702a7b | -8.9635 | -46.9785 | 2026-06-17 09:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 4bf4cfd6-43ff-31b8-a343-08b7e5714afb | -9.001 | -46.9969 | 2026-06-17 09:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2d948994-8706-3c64-afe3-ca410467bb3c | -8.9821 | -46.9988 | 2026-06-17 09:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 340.5 |
| 029fd5a1-4727-3c3f-b649-22cd6ace8a76 | -8.9818 | -47.0211 | 2026-06-17 09:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 64714874-d210-38cc-b3ce-ca0a9b75fee7 | -8.9824 | -46.9766 | 2026-06-17 09:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 332.4 |
| d12a35d2-c24e-32d1-be4a-c0cd2170c36b | -8.9635 | -46.9785 | 2026-06-17 09:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| be77787c-f910-3316-aa29-7bf38cdb6c31 | -9.0013 | -46.9746 | 2026-06-17 09:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 8aa09511-37be-3a51-952b-ccfcdb0be2e4 | -8.9635 | -46.9785 | 2026-06-17 09:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d9cc5b7f-12ae-39df-9ed5-b3b0f2d5d118 | -8.9824 | -46.9766 | 2026-06-17 09:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 344.8 |
| f896c6e5-b42f-3446-b309-9dc7d31bddc7 | -8.9821 | -46.9988 | 2026-06-17 09:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 389.3 |
| 7c5f06c0-5ea6-33a8-9f4d-a1dd5af82e4a | -8.9818 | -47.0211 | 2026-06-17 09:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6438c53e-b846-3452-8557-b348b3fedad4 | -8.9824 | -46.9766 | 2026-06-17 10:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 251.9 |
| a59b91f9-bf1e-30a3-a855-6e404474d80f | -8.9821 | -46.9988 | 2026-06-17 10:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 8fbff4e1-8990-3dfe-be9e-cba2d625bc8b | -8.9818 | -47.0211 | 2026-06-17 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3da9bce3-0616-3f5e-a7ee-5911d656c318 | -8.9821 | -46.9988 | 2026-06-17 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 9e5e3e8b-fff1-3293-9796-55a83bf32462 | -13.2651 | -46.0559 | 2026-06-17 11:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 56313605-efc4-3470-86da-cdfa2a8be483 | -12.2143 | -52.7801 | 2026-06-17 11:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f540e2e6-ef69-3534-8cfb-78338718ec13 | -12.2143 | -52.7801 | 2026-06-17 11:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6e3301ec-4ce0-3880-b308-cb6247bdc668 | -12.2143 | -52.7801 | 2026-06-17 11:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f70c7894-55a7-35ee-924c-1807a4b4823b | -12.2143 | -52.7801 | 2026-06-17 11:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 2df62906-23cf-3f65-8a90-bbc73a2a20b1 | -12.2143 | -52.7801 | 2026-06-17 11:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| a3f19e78-bcc4-3467-a980-a2e2ffd9d150 | -10.1493 | -56.6115 | 2026-06-17 12:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e7dfe1ac-094f-3e44-99ea-773697e03d78 | -12.1952 | -52.7821 | 2026-06-17 12:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 84862dac-1c5a-3ec2-8de7-871c1897e350 | -12.2143 | -52.7801 | 2026-06-17 12:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 6e9bb732-9ff5-3df5-b8e6-d2c2472c05ea | -8.9821 | -46.9988 | 2026-06-17 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 317.9 |
| 58879295-94c1-3ab2-8f51-3fcb65e96618 | -8.8883 | -46.964 | 2026-06-17 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6c95fcbd-a44d-3e9c-94cb-3472fecc093a | -12.2143 | -52.7801 | 2026-06-17 12:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| d0e4afc3-b112-3f0b-9876-1213be949936 | -8.9824 | -46.9766 | 2026-06-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3245c7af-7aee-3fa1-a826-4c2ef3206993 | -10.1493 | -56.6115 | 2026-06-17 12:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e4de57f3-9b31-3fec-8d11-cb32692327f2 | -12.1952 | -52.7821 | 2026-06-17 12:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f5560ac4-0548-3452-b0a1-cd277ae385b6 | -8.9821 | -46.9988 | 2026-06-17 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| cc55dd30-8cb6-3416-90f1-0f873a4d20ac | -8.8883 | -46.964 | 2026-06-17 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 882a2364-02a4-31f1-8e6a-67ec17e39a24 | -10.1493 | -56.6115 | 2026-06-17 12:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 2cc720a7-2d8c-36ff-8680-8eb1f721f68a | -12.2143 | -52.7801 | 2026-06-17 12:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| eb8fcc87-694f-3a29-a540-b5b3c331bff2 | -12.1952 | -52.7821 | 2026-06-17 12:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| cf7d1848-86aa-397e-8a78-30846f5ef0b1 | -10.15487 | -56.61177 | 2026-06-17 12:29:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 0668880c-1e07-31b9-8641-8cd14f3feaf2 | -10.14733 | -56.60165 | 2026-06-17 12:29:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7fd0f946-93c6-325a-bd57-294605ab0697 | -10.57166 | -57.3162 | 2026-06-17 12:29:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1c7fed5d-0d5c-3a8b-9116-c6741260251c | -8.89893 | -46.97305 | 2026-06-17 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| e12f1ba2-0a77-3a4a-b394-9a3bf4d4caed | -9.52973 | -50.25512 | 2026-06-17 12:29:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ee607bdc-01a7-3bcf-971f-63c3669e0a56 | -1.32132 | -53.13782 | 2026-06-17 12:29:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f738f8ee-e42e-3bc7-945a-becbbc14cbe2 | -6.90209 | -47.95325 | 2026-06-17 12:29:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 3d5f29a3-670c-358a-8756-98fe692ab936 | -8.90314 | -46.93716 | 2026-06-17 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| b888038d-a58f-3f76-89bb-d6df5e731590 | -10.94564 | -46.46642 | 2026-06-17 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4d999ef7-da81-3376-a4ee-1bdeee9bf9d8 | -8.34142 | -47.48569 | 2026-06-17 12:29:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 6fd87d3c-f319-3ef4-8ef6-65ec0d9a2c35 | -10.14606 | -56.61053 | 2026-06-17 12:29:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3a65d069-f7db-3f62-84a6-941ccda6716e | -8.9089 | -46.94453 | 2026-06-17 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| e83089c9-7f83-3fc9-9d57-f3623c390746 | -6.16297 | -48.50221 | 2026-06-17 12:29:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5f776aca-f49a-3c4c-a86d-fdfc529b188e | -8.90494 | -46.98024 | 2026-06-17 12:29:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 3cdcce39-5679-38a1-b017-eb23f9a55d72 | -10.15613 | -56.60289 | 2026-06-17 12:29:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| aae920ca-f77f-3dac-b2d5-02c5f6df8298 | -9.20631 | -58.06943 | 2026-06-17 12:29:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9384d0fd-e686-3d71-93a6-936362bc23dd | -11.27033 | -53.95683 | 2026-06-17 12:29:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b0427f3b-c980-31c5-959e-14b8c048a1ff | -6.90223 | -47.94799 | 2026-06-17 12:29:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| f3741c00-9520-3aa2-b0f1-f0cb3e19e6c0 | -10.1493 | -56.6115 | 2026-06-17 12:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 16af0fc0-6b04-3033-9baa-bc039a1c1b51 | -13.2651 | -46.0559 | 2026-06-17 12:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 00ac6438-5f4e-37bf-a121-b916e61b5909 | -12.2143 | -52.7801 | 2026-06-17 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 93718019-42e7-3738-b37e-e9db4d192574 | -8.9824 | -46.9766 | 2026-06-17 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |


[Clique aqui para ver as próximas entradas](README18.md)
