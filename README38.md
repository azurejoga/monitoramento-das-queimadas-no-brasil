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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 209238ef-219a-3a5d-a905-fbde61a846ca | -3.05251 | -54.41003 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d21ea12-56e0-3b1f-9846-deb48993ec19 | -3.11942 | -53.70419 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f237440b-a00b-35f7-b5ca-cb12133c3381 | -3.69176 | -51.56237 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e803ac4e-9102-391d-af9a-e94b52e3de0a | 0.63557 | -50.57774 | 2024-11-19 05:08:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173b17a5-9d78-3cf5-a91e-0e37b78a0119 | -0.09477 | -51.45769 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd5abee1-96f1-398f-895c-75469218698d | -4.55188 | -48.02077 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d079121b-242b-3bbe-91c5-9cc4d5b1876f | -4.39483 | -47.77483 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdca9223-87f3-3c4f-a7fb-5e19e2027599 | -1.37953 | -52.07712 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 517338b0-cc23-324f-b07d-982f5b2505f2 | -3.11587 | -53.70364 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aae22a39-d059-3c81-b47d-6f1d6e620332 | -5.98574 | -45.35847 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb1c8089-3e49-352c-8f89-bcbe21678cb4 | -2.61615 | -54.5385 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be3e9111-e339-3472-882d-6553c4062361 | -0.78184 | -51.75113 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83e90f66-b7e2-352b-b1f0-dedf95be40c8 | -4.1056 | -51.05121 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27f6e9f2-1294-3783-a096-9c01da564ef3 | -2.59789 | -51.79133 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf3b407-a825-3dfe-bb55-28718f116db8 | -0.00203 | -51.23436 | 2024-11-19 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b050f52-9f1d-338d-836a-1301304baccf | -3.36431 | -54.10143 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bd1f388-7bea-37fa-b2a6-3cd6e91abd33 | -1.42029 | -52.43457 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e81ff23e-0448-30e3-b314-4b6b45801803 | -2.66069 | -51.71552 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 485e91e9-23b7-38cc-a723-f586e0f2af4b | -2.58435 | -51.72279 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3076cb05-6581-3a3a-a113-3e8f21c07c09 | -3.17251 | -54.69029 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 486eea4a-ef2c-323d-8404-66596113f096 | -3.89464 | -50.07844 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb99329c-4b71-37c3-bb67-ca925d6a555a | -1.92472 | -53.34878 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64bc6571-18d9-33ed-9d10-eed60dc0858f | -2.44776 | -53.68845 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e43845f2-d954-3bc9-885d-ea5270e1c646 | -3.11169 | -53.70708 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e81bae7-c06a-3892-952d-1ba8a27c2574 | -2.85263 | -54.00716 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3edb69c3-e51e-3e43-bb3b-fb400195492f | -2.75333 | -54.06367 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1f2075d7-b48f-3309-a9ba-ab00f1787081 | -0.94556 | -51.71986 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ef5a717-72d5-310e-9e27-f5ff71fb27d6 | -1.14014 | -53.66159 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81ed2677-2520-339b-8b0e-c34a135ef6c0 | -2.88086 | -53.96397 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 215a6961-4354-335d-930d-6a7bd081088f | -0.00217 | -51.23107 | 2024-11-19 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d947613-260c-3fdb-b746-616d973f7539 | -2.87474 | -54.87283 | 2024-11-19 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc9635d8-05fa-38c0-a4b4-d8f2009f1288 | -5.12532 | -46.20243 | 2024-11-19 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42b8d6e5-8be5-3a9a-b514-3cfcb2f4e40e | -2.65674 | -51.7149 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 373b9f34-081f-3dea-b46c-e55aced916f5 | -2.88437 | -53.96451 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c430b818-e7f1-3d80-ab13-8367b6beebf8 | -2.77712 | -48.57657 | 2024-11-19 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5947c8a9-afb1-358f-92ce-db2bc21552e7 | -3.31035 | -54.16902 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef7ef85d-8f65-37d1-a693-715d58582584 | -1.62519 | -53.29642 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c27d4b41-d541-3ed9-aa9d-f1c8d229a6b3 | -3.30863 | -53.3687 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ff31680-42e6-3ca6-919e-1ce749a35f0e | -1.61926 | -53.28745 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f5d697fe-443d-332e-bbfe-7cbac2ba7a17 | -3.88552 | -52.22543 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54d07f8b-f806-315b-8572-95a412ba07a4 | -4.56284 | -48.01902 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47ae9810-5964-303a-b12d-301f97d15608 | -3.89066 | -49.98119 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e7e8dee-5197-30e4-83b4-5d156809f0c4 | -1.70078 | -52.14328 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 254937fc-86a4-3e25-a101-64c54d3a1e89 | -4.54992 | -47.99778 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aff6081-d991-3a6d-8385-e2dd1875c7cc | 0.29144 | -51.1135 | 2024-11-19 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60577431-1a37-3eb6-92fc-4e81ed7296d2 | -2.95973 | -51.41191 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b1c9e76-930d-381f-b056-02870d3de933 | -3.37833 | -54.75845 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b6147f4-68b0-33bd-b48d-a05b0e23f88d | -1.07347 | -53.36811 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a6ce184-4ba3-3b0b-b52d-9d403c2bcc7f | -0.60392 | -58.05215 | 2024-11-19 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d634c0f5-6b3f-391a-ba7b-eb91248bdc3d | -1.48449 | -52.10278 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 251ac7d7-7ade-31dc-8c77-3ce3795244c3 | -2.54556 | -53.98544 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e908fdc-cc9d-3fa3-a15e-323d541cb0fc | -2.60443 | -51.79405 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14554ecd-7c71-3b40-9f0b-b693ec9459d0 | -2.78076 | -54.04824 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a70b4110-3ded-3b51-9a0f-394b1ff2865c | -2.62265 | -54.27755 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e713c74d-f53e-3a11-8d62-6ce87b6f5f2d | -1.23179 | -51.7858 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 831d5d93-643f-3785-a164-f716c90e9055 | -3.9741 | -49.92065 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a526e3-99cf-3578-ad70-24200588c73d | -3.31659 | -54.08339 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 763e81d0-1b6a-3351-a4e7-fee1676dd125 | -2.74925 | -54.06697 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df5b3ee3-59d5-30eb-9989-75c7fa16524d | -3.33265 | -52.66816 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6db2b5ec-4507-3e81-84a5-cb3047772f10 | -3.29483 | -53.85164 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13860acb-b5e8-38cf-88b1-1ba1ad6cf598 | -1.20476 | -51.78168 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffa63aae-c9ce-310f-a366-16ccc535a549 | -2.02322 | -52.07607 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19be2e5a-d314-33ed-8fd6-07034af8adeb | -3.76687 | -52.13987 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84df6e8d-bb24-323b-8aa8-b7f15a36a6e2 | -3.76974 | -50.16171 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 545f7e06-076f-3a54-8c84-ab86e3743208 | -2.28753 | -53.7462 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43fc59c9-3d0b-37c2-95c4-e2bd55ecc059 | -1.42332 | -52.43955 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef77d6c-8729-38d3-af9d-422ce57d5719 | -2.21927 | -53.79153 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc8003c0-98d5-3694-8c04-cba80a4bfd60 | -3.59738 | -53.99197 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f867387-c98a-3209-8e53-0ecf26892229 | -0.95254 | -51.7258 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10a75948-08a1-3128-bfc6-410d4bcc5588 | 0.851 | -51.36894 | 2024-11-19 05:08:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f8b1aeb-fca5-3c88-9b68-192eeab83602 | -1.20662 | -51.7603 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7442044-0e10-3cf6-a032-581502495386 | -2.82754 | -54.00726 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9441ca1f-0ffb-3c06-be83-f7b759fe3ca0 | -3.60661 | -50.41529 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f684a667-ce6c-3626-a7e9-8256782e622c | -3.05369 | -54.40249 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bdefea0-5149-3366-aa13-16db973b2822 | -1.99611 | -45.35032 | 2024-11-19 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94edcdee-bceb-3b58-8740-b0f125fd465d | -2.43269 | -54.61929 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9a68dcc-b119-32e6-8429-b9631e204361 | -1.22334 | -51.78941 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2fc225a-5c69-3007-8608-a535db00505a | -2.36946 | -53.68131 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbe26ea8-204e-37a6-84f2-e1733c892cd9 | -2.78819 | -51.72129 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7a74be63-aca5-38c6-b1ad-c74bf3dd67ea | -3.05509 | -51.33222 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65da9583-5bb9-3850-a581-698b9c3a8820 | -1.14209 | -51.69131 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 145c9b90-91cd-3f99-93cf-434045219888 | -3.2919 | -53.84713 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2b966a5-686d-3d9e-9e50-adef89cfcfc3 | -3.28671 | -54.11412 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47816474-10b9-35a8-b660-2e8f8f43425a | -2.85204 | -54.01102 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16830187-744d-36e7-bb8a-0c7ed1b02fde | -3.76592 | -51.92973 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d34ccd46-bea3-3c8a-98fc-badbd973786a | -3.97866 | -49.92128 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 413872aa-82e4-38ce-872a-1fcfd9762aaa | -5.97938 | -45.35753 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a8525a8-ac5f-3e8a-869a-269c21f2e624 | -1.30108 | -52.23557 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8812b01f-30f8-3c59-90ed-95ab3d9442f9 | -2.78821 | -54.06903 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec57b936-3d9b-39d7-bc97-695894e7e6a7 | -4.57946 | -48.01513 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e70225d9-0ee9-3401-8810-5a88bc708b73 | -3.97933 | -49.9167 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c872e865-004e-3f27-8b4f-89c727e6f44a | -3.74317 | -54.72293 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f77fdd53-6666-38af-900f-4f91f751811f | -1.22793 | -51.78521 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aef2f9d2-16d8-3abe-98cb-e3caf4133026 | -3.28962 | -54.11843 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97a68549-aa8f-3f71-ad1a-f63eca7657df | -3.36481 | -50.82509 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98cca234-7d95-3dc9-8226-a93ba64714fc | -2.57101 | -48.03973 | 2024-11-19 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e91b08b5-ec61-3c7e-a291-380f657e9ecc | -4.37851 | -50.4939 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b6db46c-249f-3ac4-afa4-c36b2b4d1ce0 | -1.2272 | -51.78999 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66a2e1a9-0e40-3c2d-8c70-a58b3b76db2c | -2.25814 | -50.45923 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 964832ce-1701-323c-a5c5-736855e221fe | -3.82456 | -52.25853 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README39.md)
