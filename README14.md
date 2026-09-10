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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97f29090-626c-3b32-b91b-05b34e5ef661 | -9.68334 | -43.48114 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56000c98-f8ce-3927-ab79-1c8024f3bb0b | -9.62856 | -40.34705 | 2026-09-10 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88852d84-a3e8-3ab3-a182-444d2db01d16 | -10.73319 | -45.91482 | 2026-09-10 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a3a79a6-0343-3b7d-a160-1bf27e361aec | -9.5503 | -46.65816 | 2026-09-10 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7886acf-0dc2-39a8-8d2e-97493b8161ba | -10.55349 | -46.0905 | 2026-09-10 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe90549f-0ab3-3adf-ba99-7baa99efef3d | -12.83801 | -44.33776 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 7451c359-5d8b-34f4-8bb5-f6fbf3cefbbe | -13.43746 | -43.83901 | 2026-09-10 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 08b003ce-bde9-38be-93ca-992caae9f03f | -10.5554 | -46.09679 | 2026-09-10 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b60f3e7-792f-3d49-bec6-6239e13990f2 | -14.20212 | -41.60832 | 2026-09-10 03:32:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7a36de0e-4d73-3058-96f5-0477f80863ae | -14.11689 | -44.01237 | 2026-09-10 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a23e8182-de36-3a2f-a71c-132b451aed71 | -12.86081 | -44.34552 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 721a1f3a-ca97-3e12-a1d4-f881c54165da | -12.84789 | -44.34843 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| f997f9f8-96d5-3ad1-917f-6175eaa940a8 | -12.85098 | -44.33485 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 9e3afa94-3c85-36ca-a5ee-f3ed49d9a865 | -11.86701 | -44.84457 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d786d5c7-62b2-3e89-9000-c88b88a9cafe | -12.86072 | -44.61552 | 2026-09-10 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70f43a49-f709-3fe2-9b9b-0e74f4b1de4a | -9.77891 | -43.4547 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72f12252-cf1b-3b35-b0c8-5df1f022fd94 | -10.46245 | -44.9484 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd0bb701-2f6d-3f47-8c92-101879423583 | -10.26784 | -45.20471 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d81950d-2256-331c-bef5-28523ce7d013 | -10.56015 | -46.09177 | 2026-09-10 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f9b2c09-bd96-3cd0-b769-2f0533c100f3 | -11.87219 | -44.85021 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d6325f7-ce04-3c58-8e0b-a305f94b8225 | -11.33082 | -45.7795 | 2026-09-10 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7de60ed4-3c79-3dbc-b6de-ce4840244d57 | -9.71759 | -43.3972 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| eded1015-7fa5-3e27-9d39-5f77c9882928 | -10.07292 | -45.47824 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41ddf38e-6c64-3b20-a852-07b4ebe12d36 | -12.85505 | -44.34433 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 5655085f-670c-385c-b137-88fd1d43bfcf | -13.44309 | -43.83959 | 2026-09-10 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 22e8c53a-9200-3d4c-a7a0-fff615e95d11 | -9.77473 | -43.44552 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44a3513a-bc04-3c08-860c-85fbc2c1e387 | -9.76847 | -43.41114 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6597bf54-a206-3c5c-bc29-acf916259139 | -12.84759 | -44.35149 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 4696095f-9ffc-3a41-9b23-1ec6b9b4c0b1 | -11.85564 | -44.8702 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7810964a-3ae5-3d2c-a272-0043d64a628e | -9.68258 | -43.48525 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20277d2e-6bc7-36a7-a01e-fe4f9ba5f3c0 | -12.86164 | -44.34142 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 21e87457-e7dc-3fec-ad28-73ad2d3223a0 | -12.85117 | -44.33176 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 30f512f1-8dbe-3318-9b5b-e55a38b54849 | -9.17621 | -45.2548 | 2026-09-10 03:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65ec3b52-d3e6-3653-be76-33a2910ff4ae | -9.683 | -43.48428 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 516a6b2d-7230-3694-bc3f-2bd423b6a25a | -9.68522 | -43.43871 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 295cc334-32fc-390e-a9fc-b4ebfc88b5d8 | -10.73421 | -45.90965 | 2026-09-10 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8910f7f-2979-3dcd-8e59-5bb4fc941ea3 | -15.78501 | -43.56132 | 2026-09-10 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f54d3b27-e9a6-306a-870e-c4c9c2574205 | -12.78442 | -44.81049 | 2026-09-10 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9d1b79d-e041-3277-9978-893c2fa40632 | -11.76662 | -37.57297 | 2026-09-10 03:32:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 707f53d1-c468-3b52-991e-43d37e72d9aa | -12.83883 | -44.33359 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0769c414-7c46-341e-88a2-64f7eb17f7ef | -12.82564 | -44.33969 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| da8b93c7-384b-33a2-93ff-5a8ae485740a | -10.46411 | -44.95182 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467822d7-df25-3287-970c-dbe90def738d | -12.64541 | -47.08802 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a49e5b8-dbbf-3bb1-ab93-2a43d046f0fc | -9.77377 | -43.44647 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1be839df-85d3-3f07-9942-5a25a0e746ed | -9.70426 | -43.40011 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfa542b0-712b-3997-bf27-5c7a3319d7a4 | -13.83576 | -39.67937 | 2026-09-10 03:32:00 | NOAA-21 | ITAMARI | BAHIA | Brasil | 2915700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0c4c338-ea7f-3375-8cab-2151d78555ed | -10.23071 | -45.1923 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f9c0623-8cf3-3bae-a93f-4b28fec47303 | -9.69192 | -43.46902 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c3c21dd0-de59-3f66-b491-f963504d91d2 | -9.70449 | -43.40347 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ff568ab0-9abd-368c-a6cf-6268fe18fa7b | -8.24053 | -44.74041 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 05a9b379-8253-331c-979e-194a5149f339 | -12.84267 | -44.34618 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 7fabc4ad-41b4-38ee-9b4b-5a2406b44975 | -8.2375 | -44.75659 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 97059b2b-5cd6-374e-9a3b-437d9a9e0b0d | -12.84844 | -44.34732 | 2026-09-10 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ac2e38a7-e41d-3828-bba0-5cb3ffc6b3ed | -9.7037 | -43.40759 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fffd42d7-01f0-332e-9572-87a4ba5c627d | -11.19333 | -42.79086 | 2026-09-10 03:32:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 275dd730-3b35-3978-8f5d-3a0a02a9de04 | -10.06667 | -45.47584 | 2026-09-10 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdfb45d2-89dd-3510-8344-a2760b7ee150 | -9.71836 | -43.39316 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| dbb186ab-5a30-39ad-9a4a-999a501dd8d1 | -8.23962 | -44.7533 | 2026-09-10 03:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 8ec2bc10-3851-37ab-b3a8-0338babd96df | -12.6461 | -47.08941 | 2026-09-10 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2879650-e731-3a55-a220-ac094695e924 | -11.87374 | -44.84842 | 2026-09-10 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e1c6810-665f-33b2-8435-117dd1efb656 | -9.70273 | -43.40839 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c9c81ef6-c339-3e24-98b3-e9e659cee762 | -18.89161 | -46.8435 | 2026-09-10 03:34:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52363dbe-397b-3200-9dcd-168a2fc25547 | -16.61597 | -43.3218 | 2026-09-10 03:34:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2da13272-3ea1-33c6-810d-5ae86c262d9b | -2.7331 | -57.6465 | 2026-09-10 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 70966488-832d-338f-8b9d-eb7567f8279d | -6.5453 | -62.8914 | 2026-09-10 03:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 00e02bdb-02d9-3e94-bcad-3d2c66bfe188 | -2.7332 | -57.6077 | 2026-09-10 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 0b9c6ad1-96c7-3fbf-ac55-445dff5fc951 | -2.7148 | -57.6274 | 2026-09-10 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 96b1c748-8e14-3f34-b4d4-894f4bdcac9c | -6.5452 | -62.9102 | 2026-09-10 03:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fe2f1e6a-8294-397d-af60-bbb59db07a4a | -2.7514 | -57.6268 | 2026-09-10 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| de83da68-f900-3fec-b963-b124a2bb5fcb | -2.7331 | -57.6271 | 2026-09-10 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 246.9 |
| 195d4f4a-9cb9-3c72-9a2c-4046ce4dd085 | -2.7331 | -57.6271 | 2026-09-10 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 200.7 |
| 2638d561-1b37-3797-a49f-b1ae87a5b14f | -6.5453 | -62.8914 | 2026-09-10 03:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ca0bf73e-d55a-3a78-95de-0d6ae590ed6e | -2.7514 | -57.6268 | 2026-09-10 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 5f2a9cf3-0e32-3488-b619-a2586bfeda38 | -2.7331 | -57.6465 | 2026-09-10 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1c759c04-01a1-3324-a388-cc125e6491fe | -2.7332 | -57.6077 | 2026-09-10 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a43c291b-d902-3b35-9301-6f7935f486ae | -2.7148 | -57.6274 | 2026-09-10 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3e334bda-1300-3aa5-a4df-338cec313935 | -6.5452 | -62.9102 | 2026-09-10 03:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c7f7eb7f-a794-3f8e-ba2d-d442c8adaf06 | -6.5453 | -62.8914 | 2026-09-10 04:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 72ad58f7-d8bb-3652-bbcb-ddf5c2c5e2ef | -2.7332 | -57.6077 | 2026-09-10 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e180f443-055b-326f-a948-3024bb7bd055 | -6.5637 | -62.8908 | 2026-09-10 04:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fab70211-4c75-36d3-8a9b-169c8766257c | -2.7331 | -57.6271 | 2026-09-10 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 249.1 |
| 998752c4-a33f-33b2-a4d1-e2c78bff1274 | -2.7514 | -57.6268 | 2026-09-10 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e7511c91-a7c1-3c8f-9131-fe655f3cf811 | -2.7331 | -57.6465 | 2026-09-10 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f5911616-0552-3b86-9248-f5ec8eeda305 | -5.41633 | -41.83353 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a7f6fea-288a-3b71-91d8-9643e6c55862 | -6.23128 | -42.85244 | 2026-09-10 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a7a8e4c-0f6a-3c71-a927-ed9d5f990ce9 | -5.6397 | -44.21907 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f17b320-599c-3ca4-8a36-43e9b3b016b6 | -6.11641 | -45.38796 | 2026-09-10 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0029f667-1831-3a57-b20d-88c072d0b493 | -5.59395 | -45.37195 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c65f937a-3f68-36d3-ab9c-94f0efb07436 | -5.76235 | -45.07949 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 39b01783-c7b6-3b86-93ff-41dd58db9564 | -5.75992 | -45.09352 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c1076cc3-1a6f-3324-a4c1-09f26c5871fe | -5.76991 | -45.09014 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| dd78607a-4679-37a2-8ab5-ddc964dd9bc3 | -4.36379 | -47.77507 | 2026-09-10 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 585fb561-e5ff-35b9-ae74-e9d097b06614 | -3.42201 | -43.16644 | 2026-09-10 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8af16b3b-d664-379e-9453-f1bcf4aefae9 | -4.36875 | -47.77974 | 2026-09-10 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb363eeb-b9b3-32d0-a83a-d1365460938f | -4.28227 | -46.5317 | 2026-09-10 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87b895da-60d9-3167-b81b-af34c01af530 | -6.163 | -44.63467 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 800cdad6-e622-38c4-b954-a348ab184423 | -5.76155 | -45.08411 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ced145a7-4a2e-3004-b123-3ee14653ff1b | -7.1263 | -42.11321 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d3073d5-02c9-3ce4-8e4d-a7a2b99aa0cc | -5.68946 | -43.40016 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3f5c3bb-c701-33af-b202-b960f4d2e37a | -7.14328 | -42.10257 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
