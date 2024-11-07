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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64c6e810-1f3c-31e2-ab5f-24ea1ee99298 | -5.96011 | -46.30811 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 159ea31b-6ede-3778-a5fe-e7a1bbe1cf19 | -2.19328 | -48.79623 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bc4d6a20-8ab8-3902-bc07-a10bb913c2bd | -2.09001 | -52.29685 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a82f7c8-5648-3f4f-a65e-ad16613c8180 | -2.4825 | -49.0827 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1dce2a9a-3725-3bd6-86d4-7d78bc4974a9 | -2.14736 | -48.79358 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbb087a6-050f-3afb-9c77-e3c5a9494282 | -2.30615 | -48.54651 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 86043b74-98c1-3733-ba57-5f2b02ec62c0 | -4.85006 | -48.75035 | 2024-11-07 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6c1cef36-74ec-3795-89cd-261930c8f01f | -2.19453 | -48.80522 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3cd7b416-bfa4-31bc-a569-c0dcced44b78 | -4.67812 | -49.6305 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e6260bb-7313-33d5-b1b6-2478ec017f7f | -5.02286 | -46.84018 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d2b5070d-f60a-34f0-b178-822e51b15ce1 | -3.94933 | -49.43122 | 2024-11-07 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 55248b4f-8ca8-3a1f-ada3-57c6f0265d85 | -4.11006 | -48.85941 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d7f55927-268f-3883-8223-780f05ff3567 | -3.27684 | -50.35242 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e2855ebc-9cc1-31cb-b85a-2e69a76256d1 | -3.15225 | -48.72999 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c2010ffa-a73c-38ab-a441-ce9e815a2d46 | -8.03135 | -49.63679 | 2024-11-07 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 98585aa7-2ad6-3790-a907-6b67b5a05e9d | -2.85833 | -48.67136 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e6e156cd-bd1d-3420-8ea6-056d6b67a528 | -2.61866 | -51.73358 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 33837f63-8af1-3c7c-ab2d-6e62a58abdab | -6.07638 | -44.72921 | 2024-11-07 00:56:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b3ae2f2b-79c9-3893-8088-0f4d854aee0a | -3.24575 | -50.46383 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c2448cf7-3261-3212-8b12-0a5894ea38d6 | -3.65929 | -50.25607 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6e68cf2a-f158-3fca-b11a-80968a1646f3 | -2.71646 | -47.73502 | 2024-11-07 00:56:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cfcbf9b0-64f3-3879-88c6-93c88216e98e | -3.37699 | -52.3601 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| daef6354-6460-3703-a49d-541ee92d6bad | -5.83763 | -46.23505 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 24401ce2-0b73-3186-9175-58fe596b4b75 | -4.9408 | -46.77509 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 10d3753f-1f3b-32fe-9338-dbd245491ddf | -2.41493 | -48.53397 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00b4ce6e-97e0-3619-9ebf-170630bc6d51 | -4.28326 | -48.6505 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ad58000d-f4a4-3ff0-8e40-815701691038 | -4.56026 | -50.30864 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| acccddc9-74f8-329b-8193-d66b603ee55e | -4.46424 | -46.52349 | 2024-11-07 00:56:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 198dfd0e-0a58-3adb-8185-ce674268ade6 | -2.18695 | -51.73382 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78e9c3c0-d0fe-324b-acc8-f2e5c83444cb | -5.6165 | -43.96284 | 2024-11-07 00:56:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| adeabe49-bf75-3863-af3e-17614fe95c77 | -3.66953 | -52.33473 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d8716c06-dc29-3a9a-8ff6-10e3f2964c4e | -3.00803 | -53.23903 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1978e537-7a3c-326b-bb0b-bada05d1b6ee | -5.02168 | -44.37214 | 2024-11-07 00:56:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0b1d1480-cca1-3840-be0f-133bd5ad57d2 | -5.03229 | -46.83878 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 4a81bff2-22ce-39c2-8808-602103d717fe | -7.90402 | -46.69515 | 2024-11-07 00:56:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| f3cf4dfe-8aac-3f0b-925e-bea8d3403e90 | -4.75532 | -45.69217 | 2024-11-07 00:56:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3df0ab6b-f6ce-3526-8bba-b154ebd0c6fc | -3.19394 | -53.4054 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| db3fd5db-771b-3f3a-a590-f115871dce0f | -2.48126 | -49.07383 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8062a50d-9cbc-3eab-9c07-83c5a841eb99 | -2.75878 | -53.22329 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 95e31fd9-4f2d-3686-b3e5-d8e8726c396c | -4.02214 | -48.29712 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 33f9c103-e75a-34d6-9379-0b3a8688f3d9 | -2.81226 | -48.6747 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7d81631c-fcdd-3ff1-b40e-e6bd343381cf | -1.93203 | -46.47742 | 2024-11-07 00:56:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 33c4f17c-1825-38d6-a0fe-6f62d4af547a | -2.00799 | -46.94463 | 2024-11-07 00:56:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1cea157-d366-3bf5-b290-49267f2d8288 | -4.19669 | -51.01652 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 667c2d29-ce7f-3034-a7ee-92d5ed163bf5 | -3.64315 | -50.13958 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5dfb6654-fe10-3694-a5cf-89f844a87725 | -2.96694 | -48.7229 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a920e258-b4b9-3e58-91ab-5c375a0c673f | -2.74849 | -53.22483 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9a3bb480-b152-3ceb-b006-bb46c2003f1e | -5.70539 | -45.95969 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2485c77-45b7-3321-aa3b-609fc91b525f | -4.7161 | -43.79758 | 2024-11-07 00:56:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8d6022a9-89e3-37de-81ad-002b76f07acf | -8.02235 | -49.63807 | 2024-11-07 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 809c2271-87ff-3f8c-a6dd-53fbc1e25c68 | -3.70524 | -49.0017 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 01b0c202-eb5e-362b-83d1-bf2eea766cde | -3.47958 | -49.68954 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0dc56d57-3d4b-38d7-817d-acf14586ea8e | -2.60681 | -51.76179 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9ebca04b-24e2-3fb2-8221-cae02fec75b1 | -5.05255 | -46.84597 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5c82ee61-74ba-3ba7-8acd-dff306fafc10 | -6.50305 | -44.68195 | 2024-11-07 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4c857027-bdbe-3d2a-a627-48555c1ddeb1 | -3.58641 | -50.2631 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af4a5740-fc45-3f4f-8f0f-26045d7707af | -2.90558 | -49.53805 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a50c500-ab5a-3c1c-91d7-c746bb69f903 | -2.8494 | -48.67264 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 3a886aad-5b42-3475-8568-f0788d5839ac | -3.62386 | -50.19705 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 7bd02662-0cdd-380d-ae9a-bbdc0086bc3d | -2.67826 | -48.50625 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| beb4d08f-33e7-3520-a2b1-6e3ae1913d86 | -2.88211 | -48.90514 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92283fb7-711a-3b8a-9667-62b67fa5a2cd | -3.62722 | -49.62056 | 2024-11-07 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a750c97-f544-3ef9-a65f-b217e4b55a99 | -4.35373 | -48.62553 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7fb8c513-e0ff-3710-8c33-b01c645017fa | -3.17672 | -49.09799 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb1a34ee-cb61-3260-9def-945b39a20900 | -4.38158 | -47.24679 | 2024-11-07 00:56:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfbdae01-2ab7-3fe3-8dc7-8a74c1f469d5 | -2.85689 | -51.77967 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5e1fa471-17d4-35bb-92c5-deb28fde168e | -3.45444 | -50.37045 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5325a664-7656-32cf-a22e-d1ee8df7e7a5 | -3.24301 | -53.40547 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 32ce49e6-e3fe-316d-8ee8-4a7cfaf1a81f | -2.2291 | -46.90605 | 2024-11-07 00:56:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe5a1359-ad00-3c90-a635-703c9a58797c | -4.04817 | -49.27038 | 2024-11-07 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7ea10e4b-7ebf-300b-ba2a-061b510f1b8f | -5.02431 | -46.85033 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6f20ca69-13ed-3526-88db-6c4a1d492ed1 | -2.90487 | -49.40362 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 43073576-35aa-397c-856b-544a3e905b47 | -6.17649 | -44.85587 | 2024-11-07 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0725bc53-1cdd-3a43-8165-8d1ba4f267c2 | -3.21293 | -49.22782 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| db7862de-6a93-36bc-a5f1-64c650114a48 | -3.70401 | -48.99287 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e0d83e43-0d9d-39c2-be8c-8b1ba7487ca6 | -7.46416 | -48.33497 | 2024-11-07 00:56:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b64a230-4db3-3116-9756-fcfb7ae4ea79 | -4.21397 | -48.68486 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 55241de8-a452-3b0d-8f7b-8b0e573bee3e | -2.83948 | -52.91387 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5673babd-f0e3-3b30-b00e-3b62d2f3bf6b | -3.52344 | -50.34239 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e396d596-7334-361e-ab7d-867fbf78be31 | -5.70376 | -45.94853 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 87d02e8a-c411-33e3-adaa-b8c5fd5d16bc | -6.2994 | -43.84212 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b4188561-3caa-3ea8-b786-e8c349dfd88c | -6.48502 | -39.75884 | 2024-11-07 00:56:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 22.9 |
| a86e96fc-c258-3e45-a942-377ee5166d71 | -2.8225 | -52.94007 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ee52f0aa-5c66-3a9b-b60e-215b331b5c7d | -5.4883 | -43.18921 | 2024-11-07 00:56:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 12c40e99-c497-3fbe-aa92-9e88c1e7b8da | -7.48912 | -44.64946 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2f8a76f6-ee2f-3102-aabf-745b1b3b78ff | -2.81399 | -52.95318 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| bd075d18-858a-317d-a02e-045a5048f092 | -5.44742 | -45.52773 | 2024-11-07 00:56:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2324bc7a-b3dc-33d0-af7c-870a4e351957 | -4.21521 | -48.69376 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c322532f-5d8f-39cd-9167-21aca9a9e32b | -3.14937 | -51.69052 | 2024-11-07 00:56:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b810566d-947c-3e62-8eb3-c346402f07c9 | -4.25412 | -50.69508 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4f9ee223-b3b7-38f0-8c99-23f858436a9d | -2.8124 | -52.94156 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8ce39da5-07b7-3ca2-9c0f-851b530159fe | -5.55557 | -43.71439 | 2024-11-07 00:56:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 18b819a8-b63b-35d3-a8d2-1ef0968c83db | -2.1524 | -48.82954 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3ed5f3b-2ed9-3597-863a-d90287363d7c | -4.70718 | -43.78771 | 2024-11-07 00:56:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6cb9e50e-7991-3a80-8522-fde2d468cbce | -2.85706 | -48.66237 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 289456a8-7f20-3ea7-b42d-af6fd4acd63f | -2.87147 | -49.55184 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e123d477-6d8b-3865-8da2-15f80053366c | -4.11656 | -48.50756 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 12652a38-bb8e-3716-a6e0-f2bee9fac75c | -5.15832 | -49.64068 | 2024-11-07 00:56:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 41abde5f-0e4e-31f2-a9d1-ec73da75e885 | -5.04314 | -46.84744 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a4b5357b-44c8-3b19-b7cb-03ffb21d674a | -3.19696 | -48.65968 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README14.md)
