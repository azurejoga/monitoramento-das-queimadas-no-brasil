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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e13b6e0-7d30-3b47-8a92-9cfac4a12f1e | -1.45628 | -52.67698 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a5b32e52-0886-3f8e-86ab-4153436cf2b7 | -2.48011 | -47.0914 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f32c516-e57d-372f-99b5-ad0c566ec7f0 | -1.52114 | -55.4902 | 2024-11-20 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f44b6b2-829c-3acf-ae16-ac808d6e6554 | -2.15013 | -46.66199 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1b5ed6-d5fb-3e91-8b14-1a3f93a0e601 | -3.26247 | -45.13765 | 2024-11-20 04:25:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b86da551-674e-33c7-98ac-adc6eed63ec3 | -2.42957 | -46.52931 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a2919d7-9403-3f7d-b563-cb33f3e4f553 | -0.95712 | -51.72033 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7f7ebdc-678c-30ad-a406-008332d45c2e | -1.95967 | -48.67771 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9622aacb-c70a-33e9-884b-a2d7bb90507d | -2.67342 | -46.16636 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cbf8c27-3d7f-3f5c-b33c-2d3cc08a8e3f | -2.09832 | -46.38478 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f1c5991-6a63-3dd9-9d0f-93aa57edf37d | -2.55496 | -47.28368 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5dec67af-53f2-330c-8288-83d802b1e9b0 | -2.29366 | -46.44049 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7293c507-d6b5-3969-a329-9cce538e95a5 | -1.27018 | -53.40883 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d119bb0f-da60-3667-815c-58bae0e8119d | -2.36609 | -46.73859 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bedd44d-f59a-3148-9186-d5e244115270 | -2.30335 | -48.4977 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ea18125c-c9bd-31e6-bc8c-1373ffdfb6ef | -1.30952 | -52.26406 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17883363-5b61-3df9-ac4b-e5fe72a2825e | -2.25126 | -48.1609 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 05575a75-e759-3206-b4e8-e321376a4e89 | -2.18159 | -48.93424 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33c5c5fb-1a74-3314-86c7-d3f815ac3812 | -2.65268 | -46.23386 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 402de0c6-3ff3-3d02-966b-fa187434d1c5 | -3.37622 | -44.42531 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5e2f1284-5d7d-379b-8c5e-7c0961f5509f | -2.60814 | -48.21852 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 496b107d-84ec-3912-a5f5-5c726c398cde | -2.65201 | -46.56437 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefe0de2-a1bc-35b7-99b4-ee07adc69bd1 | -2.81863 | -46.67303 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c505391-2e5b-328d-a53c-5c074aa1205c | -2.69012 | -46.21136 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9101f905-dd94-3272-8320-78abdbbfb1f4 | -3.31615 | -42.15349 | 2024-11-20 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 753ebd92-33e0-3982-9263-1fea13624bd7 | -2.68688 | -46.08025 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3e24db8-24eb-378e-91af-ed82acf231ec | -2.26154 | -48.41696 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4cb7f45-a12d-3548-80e2-7611a1387fc5 | -2.61397 | -49.25919 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a9efe116-bcb8-3ffb-98b7-2f08e98a9963 | -1.24901 | -51.78412 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0faa08b-27a1-38c7-bb0b-4ab9eca8093e | -2.24132 | -50.46519 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8437f783-8a45-3543-98ba-c3145adca30c | -0.95645 | -51.72469 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67769ce0-072a-36f5-acfd-c3d7880902f7 | -2.99784 | -45.43951 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4cec70a-d54a-370c-a5b3-6a0fc516d004 | -1.87948 | -48.78534 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a44785a-b50d-32c0-900f-d6640954d240 | -2.22191 | -46.46504 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a4b450b-c807-3eab-b2f9-9a90c0ab324c | -2.71665 | -46.08484 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b3c4184-8baa-39e0-a408-4b54b4ddbc76 | -3.42168 | -43.16405 | 2024-11-20 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbaacc8e-16dd-3919-be8f-498e33a3a622 | -3.39138 | -44.43858 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b537d29-2371-3210-8bef-17565de119bf | -1.96155 | -49.55402 | 2024-11-20 04:25:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05965134-bd88-3663-b736-00aeef16ec56 | -2.64868 | -46.56386 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 972c63ee-28d7-3baf-b83a-4214e21319be | -1.79642 | -54.04041 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4fbb79e-2439-3fd4-b6b7-caf98d70ec2b | -2.77586 | -48.57989 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70ffee28-91f9-3088-9e87-d9d2aaf8f50f | -1.14513 | -53.51375 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f75814de-7a07-37f9-86db-47e492cbb51d | -2.92783 | -45.2766 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7b7e85f-b3ac-3a05-b04e-e302559fa3ad | -2.93744 | -48.06253 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 879346f1-767a-3b78-ad39-ed256a167a88 | -2.19607 | -49.73732 | 2024-11-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8364781-1476-399e-9f0e-8bd128a5b8d1 | -2.72888 | -49.3392 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709ffecf-d683-340c-ba98-ad03a07c64d1 | -2.60677 | -48.25037 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4309b815-3f4b-338e-aa1d-dec28d7d97ff | -2.551 | -47.2868 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dbe9189-c7d2-35ef-adcb-80bd25b3ff57 | -2.68796 | -46.07337 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c20ebe0b-0c41-3d60-b646-aed21f3aeebe | -3.08982 | -45.96372 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5083d162-ad0c-3c06-a4cb-04865f3fd3ca | -1.85784 | -47.82811 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1221c2ee-fef9-3d41-9598-95287feea124 | -2.83529 | -46.67559 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00cbd10e-9d7d-37dc-8b91-aee2d3866217 | -3.00445 | -45.44053 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8ac3155b-c589-3c2d-90a3-1c6fdca0d008 | -2.18657 | -46.99089 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4015bb48-734b-30e9-a9b9-cc46bc849476 | -2.63259 | -46.55782 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2978547-967a-3980-907b-f7dac1a53188 | -2.17997 | -48.40533 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec61dd82-89b1-31d1-9961-d9b060573d30 | -2.62382 | -48.5575 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1217b01f-7284-33d6-b756-fc18996545c4 | -1.1951 | -51.9796 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf688c9b-9910-3f4c-9f55-19fc204c7188 | -1.25686 | -51.7631 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 413c290f-3c84-30be-ad00-0878560ced18 | -2.08996 | -48.37922 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31ad387c-4915-3ce0-a228-a01b0cc36a80 | -1.24556 | -53.36336 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25bf144e-365b-3056-9313-583e9b5c599e | -1.5892 | -50.44652 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bbba728-e1b6-3154-9913-9d114c839484 | -2.26089 | -48.42097 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebacedb2-ddaf-3cc8-a1a9-e48cd7a659f8 | -2.65084 | -46.85179 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8325646a-3091-3e07-b0a1-ed628d61d812 | -2.65588 | -46.56139 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e5ec1eb-f6cd-3a22-bf10-3f577c10b64a | -3.05551 | -45.13422 | 2024-11-20 04:25:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 189ba588-ab22-33a4-bd09-229cf5a5ed4b | -2.26354 | -48.40596 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2b7fa2-ada4-36c5-b5e9-ccd839f1bd58 | -1.04812 | -51.74279 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 031ecf39-101f-335e-875c-49f50c292fbc | -2.72679 | -49.35241 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd80dc2b-b470-3b30-a505-7a585409900c | -2.70029 | -47.98327 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31c997f3-c2ae-3b24-ae27-0d2ff115c2b2 | -2.55439 | -47.2873 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04fac508-4e81-3ed8-9e7f-30748d656f3c | -2.71945 | -47.97448 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68470c93-e2dd-38b7-b3cb-3c24ad9886c7 | -2.83917 | -46.67261 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70b6ba4-da18-32b8-827e-23d60805a285 | -1.33749 | -52.23764 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4ea6dd-465a-31cf-915b-d208dee2feb0 | -2.21919 | -46.48249 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 708d813b-7e6b-3928-99f6-7238070c2405 | -2.9179 | -46.84304 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5e5095d-19d5-3e76-b5ec-63b5fcafeaab | -1.54381 | -52.27156 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45e86418-1d77-39c3-a990-108491a28916 | -2.57695 | -48.39522 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc6738d6-07b8-328d-965d-6fc0a02266ea | -2.22248 | -47.22518 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 530822a6-8f05-3de0-9759-c1b8c12b472d | -1.67162 | -46.95872 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90326ca8-e896-338b-8725-a7ce2ab63695 | -1.14598 | -51.69424 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f51346f-f748-30de-8430-3d5c7ac44506 | -2.72007 | -49.34684 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 757c2ae1-db8b-39d8-8c9d-6a517be109c7 | -2.14278 | -50.64369 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7466972-89dc-3941-84db-30255eea217c | -2.63998 | -46.22836 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89a28bf3-821f-3246-b3d5-3a0cc9e4e241 | -1.53752 | -54.90132 | 2024-11-20 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26038bb5-db6f-3e3a-b78e-0c2e2cca1f63 | -2.99838 | -45.43607 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e410204f-8cd1-3087-9332-650ed93a29f1 | -2.5076 | -46.39949 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9830bbfd-6755-3c89-83e4-7e24f380f11c | -0.96908 | -51.73112 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 667e28f8-91b8-3479-8350-ef6079c7c9ac | -1.14225 | -51.68926 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c15a6c0-da04-3304-a3c7-dcac96e660d4 | -0.97554 | -51.71869 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1079e71-5cb1-3be4-a798-797e456a346e | -2.68781 | -46.18271 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5428a3b0-d2fc-3c2c-b523-8e71ba09375e | -2.64275 | -46.23233 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6cbb591-69b0-3870-aef4-6667e57995a6 | -2.28262 | -48.49028 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00454872-a77c-3211-837a-4bec455ba17e | -3.00061 | -45.44345 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bfa2f6ed-2fb9-38a2-bfdf-e98cfbdbf8c1 | -2.24032 | -46.82418 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2681259-5d9d-3e49-bc82-309379875954 | -2.57214 | -46.55204 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7836db3e-4aae-36bb-b274-d9723cdd6fd1 | -1.13576 | -53.66757 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc1c266-8308-36cb-a4e2-4f51a51fd89b | -2.50918 | -47.23602 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff8a017d-7bec-36c3-9b30-3573bc27acca | -2.74804 | -48.57576 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c69315f1-5320-3be2-88b0-2e8071b8b331 | -2.69243 | -46.24 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README27.md)
