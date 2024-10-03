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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf011e87-c5ad-31df-8b99-afd8ad53d37a | -8.38641 | -71.11427 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c8fe0c5-a252-3926-93e2-ceeb56421f8c | -7.52692 | -70.401 | 2024-10-03 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c92d3a4d-dc21-34c0-8eac-fd20605ba79e | -7.56795 | -70.10892 | 2024-10-03 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bbb82bc-90e3-3154-a499-3775ff802681 | -7.57135 | -70.10944 | 2024-10-03 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 143fd44e-27d8-32a6-8639-aeeedaebaed9 | -7.22038 | -71.48473 | 2024-10-03 06:08:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e49a4b8c-085d-3eda-8cfd-09ba4c52b647 | -7.53029 | -70.40153 | 2024-10-03 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c167313-0437-3ccf-875e-86d1fc9200c9 | -7.8362 | -70.86924 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 857bdc00-41b4-3374-881f-4300d463db1b | -9.67105 | -69.06198 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0be3f02-a0da-34b5-85e4-f270a06e2106 | -9.70794 | -69.06331 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79694ce1-b355-31f0-893e-e71357279029 | -9.71094 | -69.0681 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bd92cc0-8516-365b-8a42-e38e1ffdbc73 | -9.66742 | -69.06145 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49a9c98c-84fb-3eb0-8eb4-ee6557049228 | -9.66804 | -69.05715 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e2c10a5-c7df-3527-9ef3-1e7e0a47a43e | -9.70731 | -69.06755 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a1fb2b-4df4-3f5e-90dc-9dbdf281efd8 | -9.71156 | -69.06387 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e411269b-12ab-3f8f-a6f7-08b80abd8f5b | -9.33267 | -68.91755 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b51abaf-7269-3b1d-8ea7-1ea1f0238e61 | -8.50244 | -70.23808 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf847a3e-b93e-330e-9d63-604e6e16f845 | -8.503 | -70.23437 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1e72801-800e-392e-9b75-609cefdb162a | -8.55146 | -69.95768 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 922e2250-5712-37eb-900a-b2c9d41b3a6f | -8.55414 | -70.26507 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c994c907-6eb5-3387-9d25-39a25b7b82fb | -8.55954 | -69.99774 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4661969b-57a9-39c6-824d-2e65b6e86071 | -8.61569 | -70.02182 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f00d045a-b98e-3773-a1c4-7d6248e3aae3 | -8.626 | -70.02339 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 960d9905-f266-3563-a896-b4f9c2b63124 | -9.28437 | -70.35215 | 2024-10-03 06:08:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 739a687f-30d9-3df2-8517-bc535e2d7a27 | -8.06171 | -69.90517 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec348b18-3802-3c79-a5f6-aff2136cdf7f | -8.18462 | -70.08832 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc86c93f-0eee-3895-a2b7-8c8ba9ba54dd | -8.18803 | -70.08885 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b809880-108e-3429-8831-ba2c939e9306 | -8.44308 | -70.14207 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91ac3848-8cd7-3f31-9337-7b522721eb5e | -8.44364 | -70.13834 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f714d65-e013-33b0-b6d8-2adb78381f14 | -8.51495 | -70.2476 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65b66bd8-7b16-3373-93b9-e548c90a5896 | -8.55073 | -70.26454 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41fab839-f792-3a78-a009-fb208c4eb7ae | -8.56474 | -70.03331 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a7aefd5-022d-3a21-abfb-3cb2ac9d4098 | -8.57039 | -69.94892 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9f409fb-edde-3b5f-8670-8dcaa2d59dfb | -8.61168 | -70.02507 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e01d7ed9-1523-3011-ae1b-2bde1cb61f8c | -8.61225 | -70.02129 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee66c2b-a127-3ceb-b3e0-45d82fe24877 | -8.62658 | -70.01961 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf9e80b-7b5b-3cd8-aebb-bee450907707 | -8.63477 | -70.28896 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c304e7-c2b1-34b5-bc80-d7e18756080c | -8.67755 | -69.63835 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44dc290f-8801-35d3-b468-5ea129843392 | -8.75747 | -68.9122 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1e3da9b-b03a-3907-b91f-163d0a0cbf14 | -8.7774 | -69.00109 | 2024-10-03 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab6e9027-fcdc-3acf-9a2b-a21c5c964a0c | -8.78203 | -68.84666 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e175a74c-f6d0-30ad-8968-f6d34fa67541 | -8.78266 | -68.84241 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65ba4f75-fa3d-3105-88dd-6ced97aba2b0 | -8.78537 | -68.79922 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e75d52c-3805-374a-a832-3b209178fbe1 | -8.78566 | -68.84722 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebb6fdb3-8d90-326f-a2a0-1f849fd23d23 | -8.78601 | -68.79495 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b101811f-eec3-39c9-8980-d9f8d9e77903 | -8.78629 | -68.84298 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db669f40-68ba-3ccd-9e09-9cbf5ea03b07 | -8.78685 | -68.93822 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c666ef8-45a1-3f42-937c-776bf177315c | -8.78856 | -68.95139 | 2024-10-03 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cdada1b-3e13-3820-a211-7c6a5420c74c | -8.78901 | -68.79977 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f93bf5a4-21a8-3b3f-b271-386a35fa179f | -8.78965 | -68.79549 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d62ca94d-3b81-33c9-9171-169d53b26027 | -8.86866 | -69.21284 | 2024-10-03 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ac29af-0364-3f2c-b074-118ffeb3d193 | -8.94428 | -68.91616 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d16850f5-9dac-38c1-87ee-f28c2d1e12f8 | -9.02093 | -69.18256 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9263fcfa-7f2c-3e09-b18e-8f1cca684bc9 | -8.86809 | -69.21115 | 2024-10-03 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b50970-1acd-380c-8a5d-857fb7a578c5 | -9.00475 | -69.21793 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ae2d135-16b5-3e67-8d1a-2958897886ee | -9.01715 | -69.25753 | 2024-10-03 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37a5fcbd-4e88-3461-b515-8158865ee086 | -9.03628 | -69.22694 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e4a55b0-4e8c-3b87-a287-25436cd83bad | -11.12466 | -65.06123 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 964a13c4-317c-3564-86ae-f161c5fcb668 | -11.28861 | -64.99925 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46461c61-e2dc-3ea7-ae51-9d00ccd0b22b | -11.28868 | -65.00404 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc80198c-7bc4-3c60-900b-34c41db3bd79 | -11.28939 | -64.99868 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f025902-cc62-3182-8f1a-e89b26918377 | -11.53352 | -65.06897 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1594956-bc7d-3ee2-b2e3-ee50871cfc4a | -11.59492 | -65.01221 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37aa1cd9-137f-3db7-8bf5-01c2ecf1c5a2 | -11.59886 | -65.01308 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8dd8802-f356-37f4-83de-8e6b4a5afd46 | -11.59953 | -65.00774 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47f471e6-902b-3d94-bec3-dcea02e0b34e | -11.60046 | -65.00755 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f44ddc6b-2007-3c29-a3f2-1d8bd21dd5f4 | -11.6053 | -65.00819 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bd4d79c-0a11-3562-a486-44d0ea2cd2fb | -11.60557 | -65.15484 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dc1a16e-9735-3e71-903f-351f9a65f886 | -11.60623 | -65.14959 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44c50bda-aaa8-3c13-b0ce-a05c39371a88 | -11.60989 | -65.00357 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc48edec-c780-32d7-ac61-082bcbd81c3a | -11.61057 | -64.99817 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 074741da-74f2-38a7-baaa-f0d3e56e64b9 | -11.61087 | -65.00333 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a95c6e73-2b34-3d51-93d2-c44d101e935f | -11.61113 | -65.18776 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b14cf8d6-7cca-3943-befb-bfc4ae64a6d3 | -11.61159 | -64.99796 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 602af65a-d0aa-3ef8-897a-4ac42178b7a8 | -11.61542 | -64.99878 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44dbae7c-30e7-3445-94ac-3745e6932947 | -11.61609 | -64.99338 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3f05d53-23fd-3ccd-bf4f-07813dce3d4b | -11.61643 | -64.99855 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1139c7c9-b9f0-3984-9bbc-b4e68ffd1d40 | -11.61715 | -64.99318 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7757ac94-d9b0-3c7f-8a4d-d261e61bd2b1 | -11.62094 | -64.99403 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b52187c5-ec75-3281-9676-7ceee2b359eb | -11.62162 | -64.98864 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 210bd168-d68e-3022-97cb-ff9970818e3b | -11.622 | -64.99382 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8ae2c95-c0a8-3dbb-bd16-f166856aa509 | -11.62271 | -64.98844 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76ac3ef7-87f3-3057-8059-69403615a83d | -11.62646 | -64.98931 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 343f74a3-4865-3176-a46a-07c6c48cea7a | -11.62756 | -64.9891 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a369b45-3b30-3dec-b18e-ca8adc8b6098 | -11.632 | -64.98452 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88534d70-3eb3-3a06-92f5-24ff0fa57e87 | -11.6637 | -65.19516 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 44c692c1-88fb-3fe7-ae60-68be70b0f68c | -11.67496 | -64.99576 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91796387-bbe8-3e89-9ff8-dd75318f795a | -11.67632 | -65.02332 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b56a89b-8de4-3ba9-a920-5061523c32d3 | -11.67701 | -65.01801 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 990f3065-fc9f-3275-bc1d-733db1feef1a | -11.6777 | -65.0127 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 90d77848-fb42-3813-ac08-1017bb9c8fc8 | -11.68051 | -64.99107 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c70e7ee2-63ad-3d24-a825-a0da21b326c6 | -11.6812 | -64.98575 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0fd62d71-d453-3678-b200-e43ba3464dd5 | -11.68186 | -65.01862 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bac0122-9d43-379f-b9e6-8b434c8896be | -11.68255 | -65.01329 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d48a6aca-ae21-303b-98ff-f3b15f4951fe | -11.68536 | -64.99168 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a0e04a3f-cab0-3507-843e-bee50dd945c2 | -11.68606 | -64.98634 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1136f649-2edc-3984-a87f-f08d29bdd068 | -11.6867 | -65.01925 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3db9a8f-ff22-3729-968d-3be187d28020 | -11.6874 | -65.01389 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb3c2db0-0b2b-36a2-9c75-b22e57978460 | -11.69092 | -64.98692 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e0cbed9f-287a-3824-a142-acc4d26622e6 | -10.83258 | -64.20464 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dac60bf-6e75-35b1-b8b5-f692c9ed79d7 | -10.83719 | -64.20876 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README193.md)
