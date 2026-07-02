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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d514131-2563-3205-9ffd-1c54ed10569d | -12.8557 | -44.3154 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| dc9cbc62-c99d-3919-9b46-1ee7a81b0451 | -12.8741 | -44.3593 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5fcc6cad-2095-3444-9404-c452c1373bb3 | -12.8552 | -44.3389 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.1 |
| f5ead03f-b0ec-37cb-9dd2-68109a022753 | -12.7557 | -44.4959 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| cd51a534-268f-3a9d-9a94-c77d4bbcf5d7 | -12.7562 | -44.4724 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.2 |
| be1d7216-c5b7-3830-8826-7bc72b3cf167 | -12.8746 | -44.3357 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 37b675e2-eee0-3f31-b270-74b81736f765 | -12.7755 | -44.4693 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 175d6a59-0acd-3a60-b507-a5db8084a77d | -12.7751 | -44.4927 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 01a14827-c0a2-3548-b509-06b6cf3ff45f | -12.7369 | -44.4756 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b523e5f1-36f4-3acc-aa37-1c1287d6a4de | -22.36017 | -52.57921 | 2026-07-02 06:31:00 | AQUA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| f1a5b2eb-a8fe-3e5c-ae9e-d455513edb50 | -22.35806 | -52.59155 | 2026-07-02 06:31:00 | AQUA_M-M | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| 09fb3da7-2f71-3f6e-b9dd-7c340062c0ee | -12.7557 | -44.4959 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 80c7ca6c-34ac-3777-b447-80221dd23420 | -12.8746 | -44.3357 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 37fd4258-727d-3907-977f-63721cbe126f | -12.7562 | -44.4724 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 15184888-72e6-3072-8cd9-b944300ef4b7 | -12.7369 | -44.4756 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 483b469f-e407-3eb1-bc28-6dd6137f31aa | -12.7755 | -44.4693 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a462cb8b-b8f4-30d9-92a7-6b05e232e601 | -12.8548 | -44.3625 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 01f414bd-ce9b-328f-bfc4-c100b15a1bbe | -12.7751 | -44.4927 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9945031c-a344-3b7a-8595-8a200201f538 | -12.8741 | -44.3593 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 3a28a071-6f4c-34aa-ae44-27441ee6a651 | -12.8552 | -44.3389 | 2026-07-02 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 1cac5123-d572-3b29-aae1-87a298527b18 | -12.7562 | -44.4724 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| a8d695bf-6274-34e4-a946-b708aadcb3bf | -12.7751 | -44.4927 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| c342e9cb-27cb-3f4d-921c-1d017895e417 | -12.7746 | -44.5162 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| b232f5ec-d0c7-3f0e-8a36-e3af8232a4fd | -12.7557 | -44.4959 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 776c68ee-5e5c-30e2-80ff-e2d204667b65 | -12.8741 | -44.3593 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| e3a0a48f-98f6-35bd-81df-5478e7f52ccd | -12.8746 | -44.3357 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 241.3 |
| 49c68a3f-c4ca-321d-bb8a-708598f5e909 | -12.8557 | -44.3154 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1b0b6ace-741f-36b1-ad63-2f1deefe554d | -12.8552 | -44.3389 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 261.9 |
| 240deda3-a618-3e12-b1ae-1e8210e26199 | -12.7755 | -44.4693 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 42831c87-351e-3f76-b6ae-9392cc84d18e | -12.8548 | -44.3625 | 2026-07-02 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 0838e485-5895-3725-a3d5-44de89e2f6ef | -12.7557 | -44.4959 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 18a13460-27d4-3664-82f9-a4586f8b7d97 | -12.8548 | -44.3625 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| da3356d1-9082-3959-902b-8eb084f47b1c | -12.8741 | -44.3593 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 47f479c3-2c07-3342-8c0a-475ccf8fbd49 | -12.7751 | -44.4927 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| fb5e788e-12de-3099-9f46-10110f8f36ee | -12.8552 | -44.3389 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 270.1 |
| d9d8eb93-7644-328f-97df-e176949c971b | -12.7755 | -44.4693 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 42ba4b4b-cba3-31ed-bee6-7855b332ac4e | -12.8557 | -44.3154 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 16c08fc4-7003-375b-a97b-0ff6cd8268bf | -12.8746 | -44.3357 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 216.6 |
| 4e41add4-361f-3265-bfc6-a892494b3020 | -12.7746 | -44.5162 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 272dbeb5-0758-3b1c-b4aa-04d46a9665f4 | -12.7562 | -44.4724 | 2026-07-02 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 14dc6705-c248-39db-9fb0-71098322e7ac | -12.7751 | -44.4927 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 47acefb6-3957-3eed-a56e-a4aa526401fd | -21.7823 | -56.2976 | 2026-07-02 07:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8d3a85e2-7062-330e-88e7-823107412cd1 | -12.8548 | -44.3625 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 68e10096-956e-3f44-bfaf-303a58386c9c | -12.7562 | -44.4724 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| ba4e41b2-81e2-37d6-83d0-103eda1b3109 | -12.8741 | -44.3593 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 6b5fd467-ed97-3d46-91be-4fcaa1481d2e | -12.7746 | -44.5162 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 56fa348d-64f2-3696-89a3-da7d4ea08597 | -12.8746 | -44.3357 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| a6d81194-bd57-3666-931a-16d7442cc9cc | -12.8557 | -44.3154 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 7e162e01-8dd5-38af-8f85-06cbb81b28e8 | -12.8552 | -44.3389 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 2ba285d2-fd96-3b32-9bb2-c6bd878922ba | -12.7557 | -44.4959 | 2026-07-02 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| bcfc936c-e4d8-31ac-9230-3d7c05eea05a | -12.7557 | -44.4959 | 2026-07-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 78c33685-7709-36a7-ab33-e6c27502aca6 | -12.7746 | -44.5162 | 2026-07-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 59aa4216-0e89-3bdb-8ec1-ade4499d9a1e | -12.7751 | -44.4927 | 2026-07-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| b13449a6-e466-3d37-8aa7-a53312d65796 | -12.8552 | -44.3389 | 2026-07-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a8feab11-e8d9-3963-b41f-9a19c8213d17 | -12.7562 | -44.4724 | 2026-07-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d5bbcafc-730c-395e-871d-099154c13aca | -12.8746 | -44.3357 | 2026-07-02 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ed344f16-f59e-3d81-b04d-59951c63fda3 | -12.7557 | -44.4959 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 97ef6a31-309e-3e09-815f-6fd61893d3ec | -12.8552 | -44.3389 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 9e231070-0c8d-31b1-a3d4-653fb572fc21 | -12.7562 | -44.4724 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| a30c25e0-a3ba-3f75-af9c-3d1670862d43 | -12.7751 | -44.4927 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c0d58787-7bdb-3894-8f06-d66d216f0c11 | -12.8746 | -44.3357 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d740da03-0625-3c86-a0f1-7cad246f7302 | -12.8741 | -44.3593 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fce4e0e8-22e8-3397-9a36-596ef7196216 | -12.8548 | -44.3625 | 2026-07-02 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c50a9bc5-956f-3702-a591-c4c507b9551c | -12.7557 | -44.4959 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4c79e015-7b13-3b2c-b985-204608364c22 | -12.8548 | -44.3625 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| c80d4446-1a91-370b-8a2f-c6a206bba296 | -12.7562 | -44.4724 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| a7914dbf-bf50-3125-b955-5b39e6d7a7d0 | -12.8741 | -44.3593 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a6488bcd-64f2-39d1-a1a5-f0086b7f4f65 | -12.8552 | -44.3389 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| dd114c39-bacd-3c81-bd33-135dec45cd30 | -12.8746 | -44.3357 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 68120a17-dcb0-385e-9a0a-d6c458a3aa9e | -12.7751 | -44.4927 | 2026-07-02 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| eaa5e465-b50c-3c90-8898-5a79ca9e361f | -12.7751 | -44.4927 | 2026-07-02 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 365556b1-7644-3691-aefd-a497138325a1 | -12.8746 | -44.3357 | 2026-07-02 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c6018830-6a11-390b-9100-51cee0441290 | -12.8741 | -44.3593 | 2026-07-02 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 21e832b1-80ea-3ebc-b75d-28af5ddc2712 | -12.8552 | -44.3389 | 2026-07-02 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a84177ff-d41c-3b5b-a2be-5a533b2dd8a7 | -12.7562 | -44.4724 | 2026-07-02 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6deb945b-e50b-396f-8d12-f8ffc57a9627 | -12.7557 | -44.4959 | 2026-07-02 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b7d49544-d7df-3c7c-b125-103eee9e182c | -12.8746 | -44.3357 | 2026-07-02 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 3bc1630b-4108-36b8-b6ac-b890784cb2eb | -12.8741 | -44.3593 | 2026-07-02 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| f1cb5686-55a1-35a6-9687-edcc5ae123e0 | -12.8552 | -44.3389 | 2026-07-02 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| a38dcab5-d851-3724-81e0-fb883c78fdb5 | -12.8548 | -44.3625 | 2026-07-02 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3af1f62c-4142-3612-ade7-7915ffa65935 | -12.7562 | -44.4724 | 2026-07-02 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2c0be565-6f6e-3d50-8b8b-21171b809483 | -12.8741 | -44.3593 | 2026-07-02 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0cab60b3-0884-30e9-8d11-01bf4cced81b | -12.8552 | -44.3389 | 2026-07-02 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a437a17e-0d16-3760-a496-c30681e81315 | -12.8746 | -44.3357 | 2026-07-02 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 947fae29-900f-31c4-84da-48b74a48003b | -12.7751 | -44.4927 | 2026-07-02 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 8def12d4-492e-364d-9459-b24c02c3c76e | -12.8746 | -44.3357 | 2026-07-02 09:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e6a30905-f50c-35b4-9965-1798fb7398a4 | -12.8552 | -44.3389 | 2026-07-02 09:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 4a8a2c02-0da5-3bb3-8f96-15e13da5d156 | -12.8552 | -44.3389 | 2026-07-02 09:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 211b744e-9fc7-31ea-8cdc-8fd9db6506aa | -12.8746 | -44.3357 | 2026-07-02 09:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 9b5b799f-68b7-350d-8174-a09e98781139 | -12.8552 | -44.3389 | 2026-07-02 10:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 392d7e08-9593-3725-9d51-754e82d0a084 | -12.8746 | -44.3357 | 2026-07-02 10:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 5f82ce13-b3c8-3070-8e2b-acab5239ab05 | -12.8552 | -44.3389 | 2026-07-02 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 5cf5af4a-21d4-3929-9236-5f1c2ca453b5 | -10.7843 | -53.5434 | 2026-07-02 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 778a00a1-41c6-3267-94ff-3431e3ea6588 | -17.712 | -46.7798 | 2026-07-02 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 7fe49e48-c729-3f19-b3e3-aaaf4750da70 | -17.712 | -46.7798 | 2026-07-02 12:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 157c11b9-b7dc-36fd-b363-c66de0d76e81 | -9.0684 | -44.7765 | 2026-07-02 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 537eba73-6ecc-3350-8e26-3afca791e6ad | -17.732 | -46.7756 | 2026-07-02 12:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| e3aa58c3-7236-3fc5-b340-c06cf6a3bfbc | -10.7843 | -53.5434 | 2026-07-02 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e1f6b423-393f-3555-8e3f-441370997041 | -17.732 | -46.7756 | 2026-07-02 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 44f0817a-3383-31fe-ab71-48e3b6501145 | -9.0684 | -44.7765 | 2026-07-02 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |


[Clique aqui para ver as próximas entradas](README26.md)
