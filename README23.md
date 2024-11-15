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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7bd1e1f-9d0d-3373-8e12-e2bcdb877ff2 | -17.27214 | -57.47405 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e05ce987-1339-3a50-8ffb-6e80a5d90f2c | -17.57672 | -57.55037 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 55cfd37e-f014-37fc-8cb2-ba1c7946310e | -17.64926 | -57.44524 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bfc6a300-eabb-31c6-aeec-540c02aeb711 | -16.95248 | -57.64352 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 90b01289-60b3-3a58-b7e4-8dcef84da8f9 | -17.60764 | -57.55151 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0c8d0486-c7dd-3970-93f7-0b75c513930c | -17.72177 | -57.5393 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 46b7181b-6bd3-3b32-9391-57733866ded7 | -16.95334 | -57.63865 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d0eeee7b-5ade-337c-86b6-6f366c16f708 | -16.95037 | -57.64117 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| deef5a56-bb54-3fc3-825e-72f75b868479 | -21.36492 | -55.89798 | 2024-11-15 04:48:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1edf7761-029b-35af-a717-9583919f8107 | -17.58759 | -57.48899 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1701ceff-ebe4-30a7-9558-3ec367726afc | -17.60132 | -57.47707 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 550d5bc3-e370-3d2b-b7dd-dd5af6b4f04f | -17.2362 | -57.45729 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b179cd68-3acf-39ff-bf30-6c500e858809 | -17.5734 | -57.52524 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| e46c08ac-767f-383b-9d6e-465e77838bbc | -15.9004 | -59.27428 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f6a731f-aa87-3aa8-9d20-d9c3602a4e6f | -17.22374 | -57.19768 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 86497e62-952b-3dbb-b9ae-fb25adfab53a | -15.47437 | -60.0479 | 2024-11-15 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85126809-8a82-3f07-b436-74ec62b9b6db | -15.85959 | -59.29392 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 884428a1-6234-3be7-add5-138648f28009 | -22.0557 | -56.01202 | 2024-11-15 04:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31a8f068-df71-3ae9-bbe1-41de48988f0d | -15.70829 | -59.10801 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e904fb36-1e94-3a7f-b095-29e88e5b33ac | -17.70369 | -57.5531 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f036e99b-3c12-3d36-b732-6037cea2b533 | -17.71822 | -57.49258 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a668ff64-56d7-39db-bff3-10f113786d07 | -17.81199 | -57.35913 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e21a3ddd-6b59-3604-a984-c315e84978c0 | -17.5688 | -57.52923 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 28f308f9-dd26-3443-8fce-a7a689022794 | -16.94833 | -57.6307 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1a1cc156-f6d7-3b6e-bfff-887a3b7078da | -17.58048 | -57.55111 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1c0b3cae-5c6b-329d-b949-308311ebb7ca | -15.86029 | -59.29015 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8dc7727-b7da-3942-a47d-f605cf7c60fa | -17.28805 | -57.51643 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f200d81c-9b5c-38c2-aa00-a4bb7fb1b2bc | -17.70745 | -57.55384 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9057576b-6257-36f0-96aa-d2596d846a68 | -16.94745 | -57.63557 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 014098c7-d057-32b2-9908-89ba85e49272 | -16.021 | -59.39679 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 908122f0-3b14-35ba-9e69-46cb2b457563 | -17.57503 | -57.55986 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4bd14da5-c034-3303-b7d5-d8280b13bd7a | -17.65711 | -57.46613 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4d818092-2715-3315-994a-374f5d48cb4e | -16.0717 | -59.7032 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42e551aa-57dd-3363-9ce6-5cd37be76642 | -17.7212 | -57.54186 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 738d133f-5413-3376-9934-3057f4764ccc | -17.5788 | -57.5606 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 9dbd3f47-3507-3a95-b62d-5d7506175eef | -15.91743 | -59.27825 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2034bdd-34aa-3913-ace1-3954dfe00d89 | -17.26838 | -57.47332 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7c147782-aecd-3c00-a83a-fe47e3cf9ce7 | -17.56589 | -57.52377 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| ad7503a7-f658-3f1d-a7ae-a9b01bc3f153 | -18.65252 | -57.3298 | 2024-11-15 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 95d19a02-1620-33d8-86ba-d5e651d9ec5b | -17.71243 | -57.52551 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c4688499-6a0e-3b8d-97df-e2fd995c87df | -22.18829 | -53.26928 | 2024-11-15 04:48:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 82aad951-800d-3088-9e81-7c4dee901964 | -17.62312 | -57.54716 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 009ea694-5f54-3190-904f-459aa8c9394b | -16.95419 | -57.64191 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| def76ed4-0244-3edb-b3ea-e9a21990da08 | -17.61012 | -57.55443 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ea16eaa0-4258-3535-ba29-0620f1bf5e3c | -17.255 | -57.46093 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 97c332f4-dc43-3b96-9c8d-5679f53e965f | -19.77333 | -55.41305 | 2024-11-15 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6b848109-2acd-3ada-9bc3-ffbbde4f7e31 | -17.57799 | -57.52125 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 02331a61-64cb-3ce4-a485-694a115591d7 | -17.59552 | -57.55406 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c59f76c9-d4db-384b-8ba3-c55652ad7316 | -15.47981 | -60.04408 | 2024-11-15 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36f3928b-2445-3350-8928-b3a62d0fc570 | -17.2504 | -57.46493 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 70aff59b-86eb-3222-9b63-5869008325c3 | -17.66085 | -57.46685 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e471d5ff-36ee-35b6-87de-c851517321e9 | -17.6005 | -57.48177 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1fc7cc57-0ecb-32a0-bf13-57e106c328ab | -17.25209 | -57.45546 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 309ab732-dd86-3f4d-8653-e7f8708261dc | -17.60881 | -57.47853 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aed583aa-fffc-366c-a68a-1fcc6aa0226a | -17.59009 | -57.47489 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| b7283e31-a8b4-3b37-b799-e5f6f64f6e7a | -16.95419 | -57.63377 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ef58086f-1995-3620-ba30-ae5e1d4d12bf | -17.71579 | -57.55057 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 11b66cec-adf3-345d-a88c-9f5c2407f52b | -17.25833 | -57.48607 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2e204e6d-3fbe-3b0a-b45b-8a38943b302a | -17.24664 | -57.46421 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| feeb16db-fcac-35d2-a87b-edecae8f0e95 | -21.08083 | -47.47148 | 2024-11-15 04:48:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 131a58fa-a664-35da-a823-2c325dfcdc85 | -15.90466 | -59.27521 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d50bf7f-0afd-3ce8-92fe-616eea693b1a | -22.23392 | -49.62311 | 2024-11-15 04:48:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3983d96e-396e-306e-a856-99a15ef5d7ef | -18.03155 | -57.34918 | 2024-11-15 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 06f38fc5-c4a4-3f63-9ac9-6658344042bd | -19.77671 | -55.41367 | 2024-11-15 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3da03141-d2c1-3138-b1dd-1bd04a47333d | -17.58924 | -57.56756 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 4c7409c4-d9d1-389f-b47e-e9efa0025449 | -16.94949 | -57.64605 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a865f533-8d91-3ccc-955e-80d772189274 | -17.5642 | -57.53323 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 592071c3-3c3f-3adc-b0fb-d92cff5b5c69 | -17.6068 | -57.55626 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 17a5353c-e863-3382-9ae9-4b0a5f0bb948 | -17.57548 | -57.53543 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4bef8ae0-bcc3-3ba4-85fe-12d2d3902cea | -17.62021 | -57.5417 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 52cd9da4-4589-3e23-8f65-a2c3078bfb36 | -16.958 | -57.64265 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b129ebd5-3862-3276-87f6-e12c190942ac | -15.89868 | -59.27473 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2243550-63b4-3500-8ee3-61bf21c988ae | -17.58426 | -57.46402 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ed43db65-73f8-32a1-b7e0-24552049dfaf | -17.71037 | -57.5593 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0b9ef67e-d9fe-3bd2-b640-a152dcaa41fa | -22.05634 | -56.00814 | 2024-11-15 04:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f289fd4-9e7c-3d39-a5fb-cbd335c2922e | -17.57587 | -57.55511 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1f19acf8-379b-3b2f-90e4-8a7a97b4cd08 | -21.55559 | -55.8251 | 2024-11-15 04:48:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e9584d-e011-3f4a-90ac-ce0cef50a826 | -17.70202 | -57.56256 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 32867e5c-9417-307b-90b1-61b927ce4138 | -17.58548 | -57.56683 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 7b29fd11-d076-3629-b6dc-06b6061bab4c | -17.59383 | -57.47561 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3575f381-d1ff-3709-8d57-9bc762d7d08f | -15.91317 | -59.27725 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8be2127-4e64-3111-9246-e79d4edf9718 | -17.70493 | -57.52406 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 6ce83aac-21cf-3143-b71e-93c54ac15df4 | -17.62516 | -57.55735 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| ad30a8bf-20f6-384b-b2f5-317d9d62caa8 | -17.57928 | -57.4485 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a412593a-53c7-39b8-b691-15934df6b465 | -17.58172 | -57.56609 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| f6aef7cd-e91e-34a4-ba40-6330adbf5b57 | -17.24372 | -57.45874 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| f72c3fea-40c7-3486-80ea-43003482be53 | -17.6991 | -57.55709 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 3031273d-db24-3da5-9a94-fa062e4037f8 | -17.7116 | -57.53023 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dd8600ae-b540-3fcf-8263-778eb93920c0 | -17.61516 | -57.55298 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 1b2cfba4-f953-3c6f-a789-a670eba8b6f6 | -16.94452 | -57.62997 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 40c15a1a-37a8-313d-a600-706b89bf99d0 | -17.69826 | -57.56184 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 60de0fef-3abe-395b-8f72-0f7affed7f57 | -17.639 | -57.54537 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 4a93c17f-2210-3787-b721-5f5076f089d2 | -15.7103 | -59.11166 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f85433-81e9-3077-b2a8-3c64bbd72195 | -17.58968 | -57.49913 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e03840b8-85a7-3400-bd9f-13e76c137d52 | -17.61975 | -57.54897 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 53f78060-628a-37c9-aafd-6d61fcbcd0fa | -17.59468 | -57.55881 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 231634c1-a6ee-3fb2-88af-12f83bfa073b | -17.58884 | -57.46006 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4ffb0c1e-aa47-33fb-97f3-79aeb55576ed | -17.58011 | -57.44382 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 31a1654e-b3a9-310f-b6c2-c09795f89be4 | -17.63354 | -57.55409 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 1655f65a-3e90-3688-b607-e5ffa2ce44f2 | -17.23912 | -57.46274 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |


[Clique aqui para ver as próximas entradas](README24.md)
