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

## Dados Diários - Página 208

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 436aac43-5114-3e2a-86a3-d419321ae810 | -8.68206 | -66.66184 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9650247d-310e-389a-a174-3edad8e5cdf7 | -8.68148 | -66.66569 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1719db9-cd5a-39eb-a937-94c450cc3b1b | -8.6786 | -66.66131 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e826723c-3668-3d4b-bd62-4a2963bc2d0d | -8.65724 | -66.70908 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f059b71b-0b22-3706-b3a6-e500126c8e3e | -9.95789 | -66.75172 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a01e2fa-2e80-3535-a641-0b69feae8ba4 | -9.95788 | -66.7758 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9e14082-12a3-3883-86f9-49bce9ad3f59 | -9.9573 | -66.77971 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e44151f1-7342-3542-822a-994d4e39b404 | -9.9573 | -66.75568 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c597d2f-e23b-39f8-aaf6-bbd61b817c0e | -9.95496 | -66.77139 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dcd8043-b6c2-332b-965d-67ed5f6f14d2 | -9.95438 | -66.77529 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 898ff6f8-0e12-3ece-b3cf-019be7bf57f9 | -9.9538 | -66.77919 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aed32506-35fc-3ef9-8fb8-7387fc579ab1 | -9.95322 | -66.78309 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffad55c2-1fd4-38bb-827c-26cdc2eb1288 | -9.9509 | -66.75067 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5db8bbd-cb18-3325-81f4-21fd7f617fed | -9.95089 | -66.77477 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b81629b2-cef0-3216-a6c0-3782c58d8c87 | -9.94741 | -66.75012 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3cc074-9c02-315c-a26f-5bf9b3462b75 | -9.94683 | -66.75405 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 010225a4-b0c3-30a6-83f5-ec60d8c26f3e | -9.94159 | -66.71697 | 2024-10-09 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c391425e-503e-3d45-8b2d-ac165b032b24 | -9.57173 | -66.64436 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9b35da-b39a-3413-8364-093da2820274 | -9.57114 | -66.64828 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8be49cef-be6e-30f7-89d2-d000e38b392e | -9.40597 | -66.54684 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae3472cf-eae8-340f-87a2-01ef5a6364d3 | -9.61386 | -67.15377 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 086eab64-6344-3326-ac7f-1c624ab5e3ff | -9.61329 | -67.15754 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72174147-6d6c-3f4d-ab45-3aeec50a8ea8 | -9.61043 | -67.15324 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fd7aa85d-bbe9-3ec1-8736-e525aec50844 | -9.27569 | -68.77663 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 239fa55c-b6ad-3b20-bde7-53b36ca5d694 | -9.218 | -68.77458 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd1fb1a7-4eeb-3504-a24d-f237cb7cf473 | -9.50192 | -67.15253 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17d335be-4abc-3f76-a1a0-cb0198852fe8 | -9.48708 | -67.15794 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8953de2-9f4e-320a-b2ba-764a860fd6ed | -9.48365 | -67.15742 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f86c8321-7df3-35f8-8059-89e5ff33d7a7 | -9.4808 | -67.15315 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20cefb5f-56b6-36a9-afd2-a0cfd4c8ac94 | -9.48023 | -67.1569 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84ac68fc-c134-351b-893e-e18f06b90511 | -9.47966 | -67.16065 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9778a94f-a770-3f33-bbc2-0c0b81301f93 | -9.47737 | -67.15263 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ade38b2a-651d-3450-947d-f25110cc7fd4 | -9.47681 | -67.15637 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0e84bf1-9846-3b03-89ee-ea09e588595f | -9.47624 | -67.16012 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2baa870b-06fb-315a-b46e-9a87288751a7 | -9.47395 | -67.15209 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c02dbc-0a57-3cd3-8bc6-c797065ad4f6 | -9.47338 | -67.15584 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3edf0ec7-2326-3a85-a4ed-087f2d9598e0 | -9.47282 | -67.15958 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 275128e1-783a-3cfd-8113-09ba1846e544 | -9.47225 | -67.16333 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ecc244c-e698-3e52-a1bf-d8e6ef200d27 | -9.44361 | -67.09726 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48729827-baf4-3dc2-90cf-a1839f17be51 | -9.44304 | -67.10105 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77b2170d-82dd-33a6-8ae3-fe256346679c | -9.44248 | -67.10483 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58536de1-1a81-3c88-a06f-d104c556e65e | -9.44191 | -67.1086 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77caa2d8-d79c-30cb-9b1b-942477fec3fd | -9.44039 | -67.21214 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec1f762e-c493-3094-b055-a77d15349931 | -9.44018 | -67.09674 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 13efe44b-91b7-3682-8b7e-ff0189c094b0 | -9.43983 | -67.21588 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4b1695a-1262-3946-949b-2a4ebfb78bee | -9.43961 | -67.10052 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e2fc9a1-8d03-34d3-83ce-56dc67820362 | -9.43905 | -67.10431 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7a918a1d-cb81-3a11-9169-af920f75928d | -9.43848 | -67.10807 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df41e71d-ee1f-37af-9ac2-86d9c7c3bca5 | -9.43674 | -67.09621 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aef68278-4e12-335e-84e0-c6b146df5cc3 | -9.43618 | -67.1 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70a5b0ec-836e-3566-8850-eb2a8123dc2d | -9.43562 | -67.10378 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c7290263-134b-35ee-a3c0-bb67fb7e5d66 | -9.43505 | -67.10754 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81483bef-cee8-31b2-ae13-9fbed0fe22af | -9.18204 | -68.70118 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b360a565-5c74-3587-8d27-e58dedfd8b50 | -9.05002 | -67.74854 | 2024-10-09 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49bc8fd6-42e8-3fc2-ab89-219c5606cc82 | -9.45714 | -67.46889 | 2024-10-09 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d72dfde7-8e6f-3aed-a888-e1fb5e250d2c | -9.44352 | -67.42165 | 2024-10-09 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6c34b14-adad-300d-9bff-1fbfafbc644e | -9.3922 | -67.46261 | 2024-10-09 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 754f6fb9-edd8-3251-80af-9063374b724b | -9.99482 | -68.80898 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e25af660-b590-32a0-b2e7-ea2256a23cee | -9.99152 | -68.80846 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e35be90-45a8-3414-a34d-fcd86808c1e5 | -9.97281 | -68.81983 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4c7e0bb-3669-3222-a60b-b1123dbec245 | -9.87478 | -68.75069 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36e70d9-8265-3f0c-8961-76681a8649c3 | -9.87147 | -68.75016 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea9243a8-dd95-3f9a-b2a4-172bb11aedac | -9.86817 | -68.74964 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c1e090-34cd-30fb-a3d3-51e97e406f29 | -9.85712 | -68.99445 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96131df4-f93d-3e67-970d-5a397196cdcc | -9.85381 | -68.99392 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eb244ae-0fae-3ee0-a11c-e7f1fc83d4b6 | -9.85327 | -68.99741 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 792e9f36-88b8-34aa-a116-784552cd3798 | -9.82263 | -68.82469 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ef52ba8-46b1-3d68-bb72-e799c9d52af6 | -9.62979 | -68.68642 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 05f1b852-7c25-32ce-aadc-fc99227a808e | -9.62648 | -68.68589 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ea3bce-7e65-3877-a29f-9dfe2d366513 | -9.55869 | -68.4421 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d35c8903-ce8d-33b9-bf57-56945c45e9ab | -9.55815 | -68.44562 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74ffd622-cce5-3474-80b4-5af5860967eb | -9.51638 | -68.53918 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f974a08-8c8e-3a03-abac-39aa265bed2c | -9.51307 | -68.53866 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 275fbe93-336a-3322-90cd-9abe1026f206 | -9.421 | -68.76021 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 405d4fc1-a483-3b03-a364-661083552b5d | -9.40366 | -68.62902 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39c58f70-090e-3c98-8193-793f0f81d7a0 | -9.39467 | -68.79887 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c754fd8-a7a1-3511-9d1c-c26f249f2f75 | -9.37094 | -68.79527 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c92c3189-70b1-3edb-9b2b-41a47b392046 | -9.3704 | -68.79874 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 939856ba-e7bd-3e74-af7c-c2ae6395c76c | -9.3681 | -68.74843 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3ada1593-af87-3afa-a2c7-7704c801fc0d | -9.36756 | -68.75191 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7730cee7-64e9-3424-84c2-2d20adf093db | -9.36737 | -68.66621 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bc152d29-a9fc-3f1a-9141-e7e1ee8e5d5a | -9.32248 | -68.78047 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e15c4ba0-eccf-35bc-8d09-e317b55c9e87 | -10.70889 | -69.07323 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee35b6b6-97dd-3b69-86fe-35efd3a348bb | -10.69472 | -68.88076 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c52780c-7151-3e0f-baf9-cab81abc47a4 | -10.68956 | -68.80433 | 2024-10-09 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e10a7eb-747d-3596-ad26-b8c112f85683 | -10.67041 | -69.10291 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4412fe5d-b021-3239-a5fb-b97fc4503c4a | -10.66656 | -69.10588 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0c0f0c4-1326-3959-81b7-ebbee92df58f | -10.66603 | -68.77914 | 2024-10-09 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b65a56c2-e22a-32a2-b285-6375bb301fc2 | -10.66081 | -68.9903 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35a10dcf-1f78-3ef5-9a98-a0298901a8a5 | -10.63607 | -68.99363 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 715e0192-d46e-31d3-9503-97a6cbc5a361 | -10.50472 | -69.07314 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bdeb906-c5b3-38d5-8d40-fa15de4e8855 | -10.49971 | -68.77818 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acd5619b-7ab8-39d0-ad41-7afb01cc6d48 | -10.46632 | -69.14569 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c52ca37-14db-351a-aeb9-1424c37fb79b | -10.41561 | -68.57343 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e058af1-530f-371b-a52e-1a54f44baf5d | -10.39649 | -68.65352 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ea295e7-d66c-37be-96e4-90e4f1b151be | -10.30828 | -68.74044 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4cdeefc-bbb8-34b3-bf69-c3c7f23b647b | -10.30773 | -68.74394 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6511e15-48a5-3b76-920e-21d59da5b975 | -10.30497 | -68.73991 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e0eeedb-ce41-374d-9d0c-a47c2db9b58b | -10.3022 | -68.73588 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81026e8b-de11-375e-9d2d-90abc607ba1c | -10.30165 | -68.73939 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README209.md)
