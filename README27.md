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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f07f3dd-1967-3d84-8ebc-ee55ad1ca63d | -3.72674 | -54.45577 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe48b0b-6c2a-3a3c-8249-bf475a2fe439 | -2.45702 | -53.94307 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68d6f86e-6cbe-33bd-9d41-2e984c3ddd97 | -3.58841 | -54.53192 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71006b04-3474-329c-9e81-d55ccb07fe59 | -1.14408 | -54.13856 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8dfd17-40be-345a-be3d-69578e0ef948 | -1.57385 | -53.80557 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a755513f-e834-3a77-a1da-f631a8e95411 | -3.41963 | -53.96611 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de2d7060-b797-328e-8d5e-5e59336f014a | -4.71928 | -55.98707 | 2024-11-15 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0dd71d82-41cc-3991-9e37-15a550409149 | 1.05991 | -60.60104 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a05e4835-6539-3a9b-af03-af3cd73d2535 | -1.60789 | -52.37253 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a12e951-25ff-32c3-a5b5-eacbccd3909f | -2.49639 | -56.49403 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31f3d21c-5c80-3fc1-bbe9-b54d08b82e98 | -0.86804 | -52.60618 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 946b909e-546e-3c23-bff1-e797a195aa66 | -3.19122 | -53.99296 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45590eec-c13f-3fcb-a30c-6d607d6efb04 | -1.56363 | -51.85459 | 2024-11-15 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20c1e524-7f80-3e10-9f84-196445a77c67 | -2.38818 | -53.66316 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a44a6366-9d07-38e3-8fbe-88fdd9377302 | -3.00265 | -54.08657 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d422559c-e68f-3441-aaf3-588350ad034d | -1.14292 | -54.14595 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 611b3865-922b-3f07-862e-7287f7473089 | -1.10648 | -53.0203 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57f8dc2d-7961-3d2d-bd0b-940ea9c4f277 | -2.99855 | -54.08991 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f882600-4552-3933-9d1b-60e177f053cb | -1.61311 | -52.51139 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14757b0e-a429-3d2a-afc6-614b0af4866c | -3.55379 | -54.5729 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdc6f78f-9663-39fa-a522-75fce602c2d2 | -3.72387 | -54.45143 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d198253-553b-3581-8815-2874a03b6d7d | -8.28055 | -45.96699 | 2024-11-15 05:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 812ebdf3-e3fc-3193-9f40-c6b60bcdc40e | -1.11888 | -54.16493 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9662f13-fa41-31a8-b3f4-bbd9360745c4 | -2.98145 | -54.13081 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8cf88c9-4b36-3198-8477-7d75d7968408 | -3.08787 | -53.22752 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4741b5be-48f5-3e7e-9120-a862ab7e18b6 | -2.45942 | -53.69407 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dce79c72-2280-32f1-80ce-8b32dc51b363 | -1.35612 | -52.54836 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbea9b55-9e80-3a89-a46b-ed690c8ac87e | -2.84615 | -53.97974 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 850b026f-3d2d-362c-829a-98c9f028bcc4 | -1.67727 | -52.55035 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 489392f9-d7e4-3f7f-9aa9-9e82d1c3ee99 | 1.05591 | -60.60168 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b87cd780-bcb9-397c-b50a-0b4ce6a65b8b | -3.23782 | -54.1637 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5660b65-96ce-31f8-be69-6555ee44253d | -3.17515 | -56.93084 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a7982a7-e7a3-3d17-8c3f-0a85ace85f6e | 1.05538 | -60.5982 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63944622-0d3d-3fef-abdd-884067fc1fe6 | -3.54976 | -54.57613 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9d70f28-422c-30ea-9a86-dabc53d6b367 | -3.5809 | -53.71867 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98633ecd-4299-350e-8c74-b82d08f53d4b | -3.15975 | -54.92307 | 2024-11-15 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ade98cbf-3159-34be-b5f5-bbfbcde4e43c | -3.62817 | -54.79433 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bed011e-48f1-3a95-b1a0-e5fd11ce80b7 | -3.06486 | -53.28063 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8f76c1b-f808-3c54-bb5a-54d8a1d16928 | -2.85026 | -53.97638 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| edf25d59-d1c3-3878-b802-d169a01d515d | -3.25516 | -53.67183 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e7830e5-59d0-379e-94db-cfe235cd25b3 | -3.58028 | -53.72271 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7944c5a6-fddd-3800-851d-1f6bad6683ad | -3.42669 | -53.96721 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b08e6fe3-8d3c-390d-8748-50a6198c7a40 | -1.38624 | -52.0808 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5f51b58-8758-3b04-a07c-b9687b5ff121 | -3.23701 | -54.16007 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ced73f33-87fc-36c6-9380-b3f8f3684cc3 | -2.38433 | -54.63415 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb9d71fb-e016-3aa0-aa30-bfaf87c4a809 | -3.68647 | -54.57761 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0d9a48-90e9-351f-abc1-79cedf37edb1 | -2.37013 | -54.63573 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c297eb5f-82c9-38d7-a798-64c9fcd6a87f | -3.946 | -56.06713 | 2024-11-15 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb120c7e-3517-3088-a8cc-4a95c0de7180 | -3.33958 | -53.29288 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f8db247-6b2a-3f31-967c-11ffcdb81f7e | -2.38756 | -53.66712 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75305490-b36c-3377-8ddb-1b0c19fe16f5 | -2.38774 | -54.63468 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fed4546a-4e0c-3ab1-b60b-8db9dc3068ac | 1.01323 | -60.57689 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfa1625b-069d-3f62-ab27-d7f511003b72 | -1.31622 | -54.2254 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a190a4fb-0be4-3f91-866d-1a6a2cd1b1bd | -4.24355 | -55.88097 | 2024-11-15 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3427579-d8de-378e-b964-0d681b3b22d6 | -2.61712 | -54.9187 | 2024-11-15 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 791bc76a-0c90-37aa-aade-d54beff25f43 | -2.8346 | -56.78617 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe147358-7a96-325a-8b0a-b852b5c281c9 | 1.05885 | -60.5941 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2f4522b-987c-3af6-b764-b9a3fc293ec5 | -3.42376 | -53.96274 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 007b2d83-e770-3b9a-9fd6-20dea9cbe9e9 | -3.45137 | -53.46361 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac55740a-f672-3521-be0b-dd2663d08030 | -2.99915 | -54.08603 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e0da506-e4ea-3249-83b1-c52546ddfe60 | -2.64862 | -57.10247 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 732c4947-a2d9-30d9-a837-70e51fa64d2e | -3.18679 | -54.32135 | 2024-11-15 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c431cd3d-b860-3cc2-9714-3167290861dc | 1.06044 | -60.60452 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d13c8f4-992d-343a-9089-642eddc23af5 | -2.58582 | -47.48282 | 2024-11-15 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93b4df84-ec09-3ffc-9aee-f6f0e473ce0f | -3.15356 | -53.23769 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08821155-bb7d-35e6-bbfb-b9114239e1e1 | -3.66327 | -54.6587 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da109dbb-6dfe-30f8-ae88-2ee4d8cd963b | -3.23003 | -54.15899 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f29fbaa-c155-3b47-8b1d-cf62d8b42b8b | -3.42547 | -53.97508 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d27b5c6-b4f4-3458-b0b8-02d75f72d516 | -3.62475 | -54.7938 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4adc68fb-605a-310b-b283-2a9a7daa78a3 | -1.55513 | -51.85825 | 2024-11-15 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f15185f-bf54-34ea-bce2-24eec9698d55 | -3.54211 | -54.32603 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3405b5-a570-3f48-805b-f81b4b85a59d | -2.45943 | -53.92755 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86e9ba84-6675-3718-9d4e-7eec8e508703 | -2.7498 | -54.42714 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a46a61-7bc4-341b-8576-e99b9586329e | -3.15289 | -53.24199 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28eee185-55a6-3471-83b2-f530d3b73092 | -4.29939 | -55.58966 | 2024-11-15 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e620369-359b-39ce-bc5a-b28fdeab08ee | -3.14923 | -53.24146 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a079d0f-c106-3b24-9d7b-23ba605673cb | -1.92875 | -46.27889 | 2024-11-15 05:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b9b57e5-eb63-377f-98c7-91d9b7d2495d | -3.54918 | -54.57987 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cb4ef1a-026d-310a-9e55-0f6fd2388cfd | -3.25885 | -54.53349 | 2024-11-15 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc378a9c-fd0b-303b-9c0a-cae443557287 | -1.28987 | -52.47183 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a3c718-1880-3ece-a99a-53d702e4d8a4 | -2.7312 | -54.9511 | 2024-11-15 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4452ba55-a8f9-3062-adcf-5f91516eac94 | -2.97332 | -53.85722 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e03de47-f9c7-3e62-88f5-cc6dfa8d319e | -3.27798 | -53.01548 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 614215be-96ab-3943-b2f5-835deeb7a1c3 | -2.68039 | -56.44873 | 2024-11-15 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5694d9a-3e79-33f8-a2cb-755711165632 | -3.15955 | -56.85796 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71b63794-c7b8-3def-bef7-0c3241049d06 | -1.91142 | -45.45628 | 2024-11-15 05:08:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e0ac17d-4889-38be-8c65-bd95b8847cbb | -3.42316 | -53.96665 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 390ec904-39f6-3cb9-8cde-d7f30c33d107 | -4.71151 | -55.99311 | 2024-11-15 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c13795b-7b95-3400-8f5e-5af7137105bf | -1.57794 | -53.80228 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b715fe74-1544-368e-a921-34c90769886b | -2.50938 | -56.605 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc7efaee-e585-36f8-a64f-868280408b8a | -2.98205 | -54.12695 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21b299a6-b60b-3858-b510-8809cd58ab1a | -3.23413 | -54.15562 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d99413-d115-3942-9d8e-51e970ca8197 | -1.07004 | -54.09656 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc048fe8-a79b-3453-8eee-41843cb368bc | -1.3568 | -52.54393 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53371642-3b07-3a4a-aba3-fdbec3ace4dc | -1.6881 | -52.70076 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d97de36-06d8-35a4-b01f-ab8b2fb207ce | -1.68508 | -52.69584 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5939e847-b838-30c4-8c9f-39e722d3bb4c | -3.25096 | -53.67535 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2fc5643-c522-3333-91d5-1cdd1239f54e | -2.60592 | -54.38255 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb38b25a-adee-3d53-ab42-ad84569dac0a | -3.34322 | -53.2935 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2922ea93-fce3-3369-a809-9c00c4df6685 | 1.06445 | -60.6039 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
