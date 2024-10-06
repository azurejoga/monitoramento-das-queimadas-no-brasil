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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2078a301-47b5-3916-b7fd-13192b85959f | -10.87878 | -52.39377 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bd5ab6a-322d-306e-b910-077df7308ea4 | -10.87709 | -52.40297 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48aa1386-1258-3be1-9646-10ffbe3d5193 | -10.76463 | -52.47385 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0b72fd2-84fb-321d-891f-c6747f0c49fa | -10.76368 | -52.47263 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 680af0b2-ef42-30bb-b3c9-7df0bdaa54f7 | -10.76287 | -52.47723 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01a69388-8270-3c6f-8143-a817de6c0f2d | -10.76012 | -52.47297 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 250539c2-0393-30c8-8afe-d1756d0fb08c | -10.75928 | -52.47754 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4920ee2e-3248-3354-93d0-4f593478890a | -10.75837 | -52.47632 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509848db-116f-3daf-b86f-550721ae3ed9 | -10.6998 | -53.0363 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cc3f5bb9-8907-3e8f-95d1-6c15bc90bdc6 | -10.69886 | -53.0414 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cb109dc-bb0a-3188-a1a2-0375df099066 | -10.69512 | -53.03532 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f829f0d7-2e25-3399-9e90-bbd2dbe90ea9 | -10.69419 | -53.04044 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32912228-35ee-3f68-9545-7b2d5592e26f | -10.6895 | -53.03952 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3a720a5-7bb2-35d3-b60a-3edb046447c4 | -11.23412 | -53.86069 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 084cff08-87e7-303e-a3b3-9df2d05dfb28 | -11.23023 | -53.85416 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd43394e-e42b-3e13-a874-5ae83e689cbb | -11.22922 | -53.85969 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcd31cd5-7ddc-329f-8cb8-66dbe478de53 | -11.52726 | -53.44407 | 2024-10-06 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2162b5cb-9978-3167-852c-de54f24860ce | -10.94066 | -52.41004 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07a123d8-9855-3fe4-a1fe-66d8cd0d5f7e | -10.93618 | -52.40916 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9fdc1b5-f7a3-37f5-9bd6-66782286d88e | -10.93536 | -52.41373 | 2024-10-06 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd9140a4-5ec2-35e5-9a5f-239344effb65 | -12.6347 | -53.11606 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bdc971d2-3652-36c1-ac13-40149f1ee616 | -12.63382 | -53.12082 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 966d2641-395e-3dd1-823f-9aef36cf71e7 | -12.63103 | -53.11042 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bebd41d9-0ab4-3454-99a8-f487ae592bf1 | -12.63014 | -53.1152 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c76e1460-e32b-3476-8e75-b972f1e5c193 | -12.62925 | -53.11997 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5595e006-0932-3911-b0ea-7312bd05965d | -12.62837 | -53.12471 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7650a42c-ddc3-343b-b490-12e2ce7747d7 | -12.62558 | -53.11432 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b8b8a5fc-4fe3-3d19-9719-6f57c5a207a4 | -12.62469 | -53.11909 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e06d6566-5792-3de0-864e-415f79519806 | -12.62381 | -53.12383 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bbc16d75-b800-36e3-a4dd-48cd15b9648c | -12.62103 | -53.11343 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc2c16e2-3d16-3bbc-ab47-dbb46d3d7141 | -12.62013 | -53.1182 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1fc163ff-743c-37dd-a8c1-01ce768bd1c4 | -12.61925 | -53.12296 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82c0dc1c-99cf-3107-9f90-227b590f2539 | -12.61836 | -53.1277 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ba7d7ff6-a028-33ac-8ec1-653a9d1def08 | -12.61558 | -53.11731 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08b9ba3f-c1a2-3ea8-b553-b7deb94ca6d5 | -12.61483 | -53.14663 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71e361d7-b756-34b0-8bac-3fc96bfa73e6 | -12.61469 | -53.12208 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25a5255f-be88-3d11-b1fb-af35f02a1fd1 | -12.61203 | -53.13628 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5cb761c-1ff6-3beb-8a2d-e224746bfd97 | -12.61148 | -53.11448 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2852952f-e167-3c7e-ba39-287e3c65185d | -12.61102 | -53.11642 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73168487-2da5-3640-a4b6-a4bb543505f5 | -12.61061 | -53.11927 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 978368ce-5716-3121-9bba-b1cbcd81c619 | -12.61025 | -53.14579 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47d77419-bf3b-3abe-a978-6008e2564b17 | -12.61012 | -53.1212 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 174e6581-1a5f-3eb9-a300-282854927277 | -12.60976 | -53.12407 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 337ca1c4-f863-3300-a8ae-3dccb555298e | -12.60923 | -53.12598 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 26acfb4f-7c6b-3c9b-a7a5-a35da672c6a4 | -12.6089 | -53.12885 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46e418db-9765-38b1-80ab-54486dbeb9e3 | -12.60834 | -53.13073 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 096bb466-8130-3010-a518-ba69a0387d03 | -12.60805 | -53.13359 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 182e7309-ba70-378a-91f4-8a6cc51fa2e1 | -12.60745 | -53.13546 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8a00ed4-3e31-3744-ab94-61612a3c51fd | -12.60736 | -53.11071 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c74bf4a-e4fd-39d5-86e1-93f42c997779 | -12.6072 | -53.13833 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92dae66f-dc66-35ed-a6d1-7fc124b41e60 | -12.60692 | -53.11356 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5c588d5-0518-3f06-a876-6e046c6a7792 | -12.60656 | -53.14021 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2848fadf-a8eb-36e4-95b8-0e09bba02636 | -12.60606 | -53.11837 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b030845-db63-34b2-be54-6eb49f9138e0 | -12.60567 | -53.14495 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4121ea01-4489-330d-b66f-1b27e83219ac | -12.60556 | -53.12032 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fcdbb1cb-b020-35cc-accc-0e59f34f942a | -12.60519 | -53.12318 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8092c901-d97c-373b-be3d-addce46317be | -12.60467 | -53.12509 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60e96d7d-87fb-3aad-8095-24602329560d | -12.60433 | -53.12795 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af9af9c4-3e27-3adc-9528-241b9dc0171a | -12.60377 | -53.12986 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7b33c0b6-1e17-314e-b39a-01ad6bc7c4cf | -12.60348 | -53.13272 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f84a766-c309-377b-8670-9593fa3dce4b | -12.60288 | -53.13462 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 584e1a87-b09e-33d2-bf40-8821ba670817 | -12.60262 | -53.1375 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c960016d-e141-3591-9801-530e2aeed82a | -12.60199 | -53.13937 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61acd724-ee0b-378d-888d-f175ce88d8c1 | -12.601 | -53.11945 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20829846-0110-3f55-80b6-4c84c81b3851 | -12.60063 | -53.12231 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c7d4864-8376-334e-8064-e6c8ece26d1f | -12.6001 | -53.12424 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e0a1c8e-194d-3dc2-8b0d-e6c19455188c | -12.59976 | -53.12709 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0417c506-aabf-36bf-af1f-3cb2632e7999 | -12.5992 | -53.12901 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b4ebd4f1-3625-3c8a-9799-e47f9e909025 | -12.5989 | -53.13187 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d1713142-6182-39d5-b72c-900fbda1bdfb | -12.59831 | -53.13377 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 484df9bd-ddc1-3819-8a2e-184a70d1c520 | -12.59805 | -53.13663 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cd819167-bb76-31bf-91d3-31e923874820 | -12.59742 | -53.13852 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3ff468b-f499-35d5-8246-35d52899d635 | -12.59606 | -53.12144 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44ab64b1-5862-3785-9a3c-904758bc9907 | -12.59553 | -53.12338 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5db68acc-e29c-3b07-9b85-309571f69f69 | -12.59519 | -53.12623 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c82bb935-e534-3549-942a-955ea7e937f6 | -12.59463 | -53.12817 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 685d1e3b-0b61-3858-a409-c0a134d96907 | -12.48302 | -53.14399 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32cc3fb1-f8c9-3830-b28c-c8ec7d65264e | -12.47667 | -53.17773 | 2024-10-06 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d19adee7-72f5-37d1-bc32-7660035288c7 | -15.38234 | -53.74004 | 2024-10-06 04:19:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4502ab0e-d719-3b8b-b224-b78ec2638090 | -15.39139 | -53.74184 | 2024-10-06 04:19:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bad1b23f-8af5-3359-b717-425af1a86f11 | -15.3905 | -53.74659 | 2024-10-06 04:19:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7e3a633-7e1a-39e0-849b-89ca07930cae | -15.38597 | -53.7457 | 2024-10-06 04:19:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 839de3f3-284d-3b80-b433-fc1323ddb80f | -15.37782 | -53.73914 | 2024-10-06 04:19:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dc1262e5-da9c-3f25-b947-e3b5008f192c | -7.97729 | -54.77823 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d817a3e-2f16-3b98-bfe8-22f6c439f55f | -9.65854 | -53.59304 | 2024-10-06 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a9f7a76-ae09-366a-9d30-4a00b8665057 | -9.65565 | -53.58063 | 2024-10-06 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a9d1f09-dca7-3e1e-8eb1-7e26e696e98e | -9.6507 | -53.57969 | 2024-10-06 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 038f4b91-c2bb-3e23-a070-a9d1c5277d6b | -10.59369 | -54.3415 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09136258-bc75-305b-bb29-79c3f1ca4deb | -12.14914 | -54.27072 | 2024-10-06 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0056e52b-ec59-3cc9-b5d3-f3fbc037f842 | -11.69628 | -54.55991 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7797d3d2-2026-3b67-bf6a-2902a80a335a | -11.69117 | -54.55896 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94b328ae-0549-34d4-b839-e3b3a867c2ad | -11.68892 | -54.55812 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bf46b91-83bf-30d8-9545-789cc87d6398 | -11.65154 | -54.53165 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c2ffc85-ad82-353f-b331-586f1dd7ce57 | -11.65098 | -54.53468 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0dd6168-3302-33e0-9b73-99fbe4d02168 | -11.64759 | -54.52456 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b29cc953-65bb-3a78-9f2b-8d7df7594874 | -11.64703 | -54.52756 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9e5dbad-add2-3930-84b9-0452c0f4a8ab | -11.64646 | -54.53058 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 318e449e-401d-3860-b720-339e202a0f3f | -11.64589 | -54.53362 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84698d46-fd0e-3d6e-8c9c-ff63f3d2f25f | -11.64193 | -54.52655 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dd40947-183f-3ffb-bf2b-04e99e7fe507 | -11.64137 | -54.52957 | 2024-10-06 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README82.md)
