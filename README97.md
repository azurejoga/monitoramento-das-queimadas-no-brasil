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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e50416e6-3b4a-3846-9709-bd43a1bd415c | -2.93434 | -53.91144 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e071006-3d30-34b6-a128-04fade7f1daf | -2.93373 | -53.91539 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3a49d49-a19e-36cb-b4ec-27473dd28272 | -2.93349 | -53.91018 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a10bb044-cff0-3e8f-91ba-e18527e4270d | -2.93311 | -53.91934 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd32be5d-205d-3842-be57-4a916a6de37e | -2.9329 | -53.91416 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32920d60-1291-32e4-abc6-90a51668454a | -2.9325 | -53.92329 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b2d102-c551-3d87-b322-e48dd276a00f | -2.93188 | -53.92727 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ce3aef-05e4-348a-a4cb-ecdb39877441 | -2.93126 | -53.93126 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acedb26c-43b0-339a-ae28-875b01c5d619 | -2.93114 | -53.92607 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d7ebccf-3d71-3b77-a552-2712b3709fa0 | -2.93055 | -53.93006 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08724b1e-7f50-3b8e-95b4-82a4ebe30f8c | -2.92996 | -53.93407 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27985b22-4400-378d-85db-3fdace4a84b8 | -2.92824 | -53.92266 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff660117-da08-304b-aa42-a7320a732c41 | -2.92762 | -53.92664 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2749386b-173d-33ba-9f16-6cf5c05456dc | -2.927 | -53.93063 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f155a047-9904-321d-858e-f7d3174224e4 | -2.92688 | -53.92544 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53c9f648-4d22-32c2-a49d-77067ca2b47f | -2.92629 | -53.92943 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0f32090-44a9-34a7-8922-60b815b1bc13 | -2.92336 | -53.92603 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b1c23c-54d3-35d9-b8e6-91e65b2e18fc | -2.92274 | -53.93002 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e54c8d4-65bd-3e3a-98b2-6c1119b86a38 | -2.92212 | -53.93402 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5dcb7b7-911d-3115-bc12-889857210844 | -2.9191 | -53.9254 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc1134e2-38aa-31a3-8dfb-a3c99f6157dd | -2.91848 | -53.92939 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bcf3ff9-a274-3809-9471-8d5ae13744e4 | -2.91786 | -53.93339 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 365b3fd2-8c6d-3e86-8a7a-bf412b1d616c | -2.91422 | -53.92876 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eb96017-52f5-3a19-8dbe-c637fc4145ef | -2.91361 | -53.93276 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d1982c7-5b19-3b2c-a838-49201dbf89b5 | -2.91299 | -53.93674 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 019db9bb-6f4f-386a-b525-a7864c00708b | -2.80567 | -53.98661 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47ada7d4-4d73-315c-a59a-c2e67c1af4b1 | -2.80016 | -54.10504 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d64092-7036-3030-b65b-c0a540e1b256 | -2.79701 | -54.10326 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cf7d683-f7d6-34f9-b1f3-2ac0858f9794 | -2.79596 | -54.10439 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b360fea1-99e8-3295-863d-7a666f6aa6d2 | -2.75925 | -54.03552 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87711160-164b-33a5-9e51-4cedc9153979 | -2.75082 | -54.03423 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dfdbc1b-9839-32b1-93df-24b6361f4c0f | -2.73323 | -54.14985 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24c6b6f5-7b5c-322b-b836-ca1ff3817318 | -2.73266 | -54.15361 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb7d7209-63f9-31b0-943d-aae633408de6 | -3.65275 | -54.21813 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f83d1153-9b44-3b84-a74e-d0575286c6db | -3.65217 | -54.22208 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff8fd942-672c-3304-a04d-aa20dd7e2cab | -3.64851 | -54.2177 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bea998f5-f410-3f01-b350-5d68560b9507 | -3.63403 | -53.96854 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb015a4e-6123-3f3f-addf-e978816a29e7 | -3.63345 | -53.97243 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1acd6b81-0a10-35f3-a83e-eb985698bef6 | -3.63035 | -53.96388 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4c35332-0922-37b1-bb9d-6aff123b5e9e | -3.62976 | -53.96779 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd22dab0-df14-34ec-aa15-e3837d67ab9a | -3.58906 | -53.78687 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e141c48-5a93-3973-8c64-aa891b3d28d2 | -3.58474 | -53.78609 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4b75507-1ebb-3b2b-8706-80630b23a85d | -3.58412 | -53.79014 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d5d3956-e277-3f3e-ab1f-7ecd95cbc16a | -3.58041 | -53.78532 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b6c02cd-d88a-3e2f-9eac-ec320623738f | -3.32842 | -54.19024 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb90978-4fcf-3f64-aba6-52fb5516fcac | -3.59065 | -54.66679 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e041e5fd-4311-338a-8e22-0a52177d8e35 | -3.56041 | -54.75843 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 156dbc87-656f-3051-a3e3-217162416b29 | -3.56023 | -54.75817 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2802c212-bdba-339d-ae3e-09607c1bb60d | -3.5421 | -54.74085 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28fabf7c-a699-389e-884f-02dbe72cb03f | -3.54155 | -54.74444 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffd615fc-18a7-3f94-b28d-c53a25e4d7dc | -3.53803 | -54.7403 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b565c76-1fad-3b3b-98d5-6bf2a6d738f1 | -3.48525 | -54.46222 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c3ec04d-3fc2-38df-8ebf-15d0892d8dff | -3.48453 | -54.6807 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28115469-4435-3bcb-9cb5-0569ae423239 | -3.48097 | -54.67652 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad95591-6c2e-3b7e-945c-92594ff5d782 | -3.48043 | -54.68015 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcb654ba-8d12-3826-8a5d-5f191f9608ae | -3.4242 | -54.6687 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02905b38-7eca-38f5-866a-4422698b3a05 | -3.41958 | -54.6716 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02967bbb-32dd-30f3-884f-63b552b5c668 | -3.41913 | -54.27928 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2ac7e99-f4c4-3116-8a4d-f91861445dbf | -3.41797 | -54.27931 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06ac8788-7b50-3101-84c5-3e3a29e5db4d | -3.41757 | -54.57429 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f7f4a5-3c71-3d43-8cfd-fa7331d4eeb2 | -3.41701 | -54.57797 | 2024-10-24 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18a8b960-e54e-359a-921c-c7b04a36cfac | -3.13775 | -54.27799 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 352b191c-a08a-35d6-9580-7091c22b6a19 | -3.13717 | -54.28181 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f76a54f5-5735-3c6a-842a-cef5538cc2ee | -3.13415 | -54.27354 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4fe4429-9773-3082-8ff2-71aed296fc7c | -3.13357 | -54.2774 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7956dcea-52b1-3a51-be52-7b5ccd9eee3f | -3.06902 | -54.78686 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29f39f5a-af21-3234-a150-82029bbc7ff9 | -3.05043 | -54.85519 | 2024-10-24 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48bb3ffc-0428-32c0-9a02-36989c2652bb | -2.86101 | -54.59499 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c261e2e-f38c-37a3-860a-e8152d614423 | -2.85694 | -54.59437 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16f576df-61cc-348f-a50a-92fd4c35828f | -2.73677 | -54.53647 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fec2e639-64ac-3f44-8091-e3a76c416248 | -2.70897 | -54.5548 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a9aa5c7-f9cd-3278-87ed-21ef0dbc791a | -2.64443 | -54.65104 | 2024-10-24 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fb58ef5-f066-3167-acb2-432ace1c6420 | -2.6229 | -54.51994 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c93be1-503a-342e-8059-024b2a381e17 | -2.62271 | -54.51963 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a45a0cca-053f-32f9-84ee-28107e95b7b8 | -2.61884 | -54.51926 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c9b4ea3-9629-3998-bce2-9bf75cdce11a | -2.60566 | -54.55041 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd151834-da1f-3c1d-8145-b2653476157e | -2.56043 | -54.29773 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09feae43-a067-3f2e-997d-93c980cb734e | -2.50154 | -54.69054 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca2f9c75-d460-38d4-a7f7-2cc314a9ad58 | -2.41809 | -54.28304 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 67a3047f-cbef-3377-b644-6379789c1323 | -2.27662 | -54.88137 | 2024-10-24 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 108978e1-56f5-3fea-b3f3-3a8112b5561e | -2.58078 | -54.01376 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7e4c818-b517-3d30-91dd-a0e125b127f5 | -2.57597 | -54.01699 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59033418-be68-3445-850a-98e0413d1ac8 | -2.57103 | -54.22683 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45bafb86-6a92-33e0-8d9e-414ebeb47e68 | -2.56696 | -54.01958 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e08d730-a722-3e9b-a3d3-b26ec09032f4 | -2.56334 | -54.01509 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09e7b021-6cdb-38d7-a97b-b6eb0e472b84 | -2.4969 | -54.14157 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d690ca53-12a9-324b-85f0-5587d3414799 | -2.49273 | -54.14092 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c417a23a-9736-359e-9ca2-ebce54f65f36 | -2.48857 | -54.14025 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adb71874-4e42-3fda-87e1-d9893350a434 | -2.48441 | -54.13955 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d8c0a22-f37d-3cea-ab62-2dad401b8859 | -2.41806 | -53.80433 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc6713b2-75af-31b3-a451-2da81d923b16 | -2.41747 | -53.80828 | 2024-10-24 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8baf6004-d19c-3302-bc0c-570bbeedaea8 | -4.42599 | -55.43756 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff04d00a-b98a-36c6-96b2-468e61e4645a | -4.42585 | -55.43436 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c190bdae-aabd-3bf8-be36-62a854743059 | -4.42282 | -55.43193 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532cec25-3372-372b-9397-f7b77cbefc16 | -4.42205 | -55.43696 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a8c85b3-0e70-387b-83d8-ea9fbf56a385 | -4.39511 | -55.04684 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e68d380-6f87-3933-b71c-a0b7648c15ef | -4.38699 | -55.18523 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 934a5a97-e7c6-3bed-96c6-5a8c48b1005c | -4.38647 | -55.18875 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 988c0339-ad9c-3dae-ad33-1a7829f3a8fc | -4.14498 | -55.15158 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86bb0d15-1a0a-300c-a521-e5990adf2143 | -4.14445 | -55.15499 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README98.md)
