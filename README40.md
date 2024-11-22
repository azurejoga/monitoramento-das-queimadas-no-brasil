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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce4ac9d-f3f9-3779-b475-5f9085ffa171 | -2.65216 | -48.78468 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11aec652-c3a1-3ef3-a67a-3ea80b6b26e7 | -2.68351 | -46.25272 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac268d3f-9d99-36ab-95b4-b64ffa70fed6 | -2.05882 | -48.25901 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60e18ff8-3367-39bd-8cb1-89f1a2b57963 | -2.6077 | -48.2462 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c3bcd79-940d-39c4-8adf-6e17eb784173 | -3.4122 | -54.66671 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a2a5254-1d26-3cf1-9b33-d24c5346577b | -2.69392 | -46.2543 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80197526-5684-3822-869f-9eb905a4b1f6 | -2.86427 | -49.14229 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cef0ce6-028c-36ec-b583-9138260933b8 | -3.25283 | -54.24009 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f3d9b38-a996-3877-8a0c-471e6e28f4d4 | -3.74727 | -54.47505 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef63b52f-1b34-36e1-ac7e-2977474641d1 | -6.1162 | -42.51779 | 2024-11-22 04:36:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 40cfaab8-13d7-3e00-b24b-ba5b0b3a47da | -3.1936 | -54.33352 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cdb320e-8d48-38e5-9860-3fbf76dd20e7 | -1.09837 | -51.74792 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c5eced7-eee3-323b-9313-316f5c39b5cf | -2.49925 | -49.00017 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76aa196d-9f04-3f76-869e-f2f7a82c8eb9 | -2.36391 | -46.73496 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8377ce8a-441d-3e3a-b48a-db3f506fb072 | -5.70988 | -43.83219 | 2024-11-22 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8083e1c2-45ae-3593-847f-9d083f4526e4 | -2.69187 | -49.17929 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b84c8c3a-490d-37f1-af3a-09b0af3d1b11 | -3.9161 | -46.48883 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61ea68a8-6736-30ad-bc88-772fb030554a | -2.11069 | -50.12781 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22b3f944-7b9a-3e29-bf81-dd2bef548f07 | -2.17845 | -50.58834 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5911167-18a8-3ead-ac93-e6bfd91503a6 | -1.25091 | -51.75117 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ef9686e-3682-3433-8888-356d3d067e05 | -1.42202 | -51.11808 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01e2eac9-390e-3a06-a53d-df85c86e7bbe | -4.63534 | -49.54513 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7843d5a7-8437-3f5b-9a30-9dd01f832241 | -2.56545 | -46.15317 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7a67cb8-abf0-39ef-8f80-5fff4abf1cfe | -3.75662 | -46.11984 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5235858e-1f30-33ad-b963-47d401cc38c8 | -2.60162 | -46.26435 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0838385-e199-350a-9308-6fd0b6c034aa | -3.11405 | -54.28904 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0fdabbc5-553b-3e7b-a592-87c5d84899c6 | -3.06537 | -53.22902 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7159cb53-4096-3501-97bf-415fe360a57c | -3.21489 | -54.25427 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86a7558c-10b8-36c0-86a8-f80f4976c502 | -5.5886 | -46.46234 | 2024-11-22 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4343e804-4ebd-3806-8d6b-a3e7ecae8b8c | -5.92276 | -44.60248 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76465721-3ca8-3021-ad0e-51cf153b52a6 | -4.63257 | -49.54115 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdfe50d5-72f3-3142-9b53-47a6a74afb3f | -4.70399 | -45.80962 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2e5bf0a-ff1f-3a7c-995d-a4029df47872 | -2.28277 | -46.55737 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe1c195-8978-349a-8226-6390590f6876 | -1.63985 | -52.61685 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66b17ff6-7972-3ff3-9336-a3233273668b | -0.26314 | -51.53753 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d92ed15f-5504-3e18-9157-1cae607a2ae7 | -4.52033 | -48.72179 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6193cd16-0ea9-3ff9-b469-3a4ada4a40a4 | -1.93802 | -48.65812 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc89ef70-f8de-3131-a0f6-ff6fa89c8257 | -4.39292 | -49.93896 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f99b06d-5802-320f-beea-3676fbfac1b3 | -2.69266 | -46.8518 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43596e6d-8a0d-3f70-bac3-dfed87e26b62 | -2.5359 | -48.50944 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c8c53c27-fb9e-35d8-9a91-54d805a147db | -2.42802 | -46.68107 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0caa6a11-dacd-308c-89ce-be1d3bc35aed | -2.68649 | -54.9903 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a70c2b17-5a24-3930-a238-4067b3e123c6 | -1.61022 | -52.48129 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9d7a8ab-278c-3c22-95d4-77f90eb1cf74 | -3.28815 | -53.84782 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4889aed1-6fb3-3731-82f5-c41eb17d8138 | -2.21251 | -49.86627 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b1802ca-32ec-3dc0-8b51-35a1d124400d | -0.26944 | -51.56963 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71b94cce-bc35-35be-ba4b-68b952ee0d98 | -1.63352 | -52.40853 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89c3bdc2-9f05-350b-b644-302496d89808 | -2.69557 | -46.08151 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83238d84-a96e-36bb-b5cc-67d00e656b0c | -1.2526 | -53.36299 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0208a60a-e027-3234-b3e1-5687c9ea90bd | -4.10525 | -46.91385 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73b7d29d-906a-389a-b527-c9284290939c | -1.74698 | -52.37676 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06c1ba3e-3cda-3a70-b0d7-27df2ff66cc8 | -2.05348 | -55.45934 | 2024-11-22 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e849d05c-ec82-3cf5-af94-f93b298b0e89 | -2.4781 | -49.17741 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e7264dd-6c76-373b-8f86-36a695e51260 | -3.10642 | -53.70601 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71b78944-eb68-3c33-aadb-12d792b51224 | -2.50256 | -49.00069 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb9c40f3-4bcb-38ee-8349-e7061f9c4f9b | -3.32356 | -54.09375 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5b54140-cd75-3d3c-af15-fed2a3033552 | -1.20583 | -51.75423 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56720e81-428b-38b8-9de7-b7783a80f08b | -2.41116 | -50.31243 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e32f5b32-227c-3725-ac3f-97ab046b31e3 | -2.10156 | -48.82847 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 551eea27-0de6-3ca2-9b0a-5795d2ac97c3 | -2.34385 | -48.79974 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2433392a-ba9d-3692-bd71-2e1b8734d5cd | -4.73313 | -45.71508 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a355a2a1-04a9-37b2-bf1f-6562a47141d0 | -3.04012 | -52.43546 | 2024-11-22 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1a19ae1-9822-3f0c-8c4f-1704b2c8ea5f | -0.80707 | -51.7858 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9631e71c-e0e7-3990-a2b3-39198ed6e19b | -2.72145 | -49.07772 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23cea0f1-a95b-30af-81d6-7a1347b58f00 | -3.5556 | -54.58588 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a43019be-d774-363a-83f6-1fb3c4b170bb | -2.70568 | -45.23168 | 2024-11-22 04:36:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 549a77f7-ecf2-3873-9bf0-5b597adf5347 | -4.90683 | -47.41724 | 2024-11-22 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32159f82-e1db-33d3-afc7-81d5086372af | -3.23967 | -54.24204 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6d2040ac-5ec0-3129-bb67-e0870e0b175a | -1.22325 | -51.73927 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b329254f-d906-3109-953c-54f4859b21a6 | -3.22938 | -54.2524 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 63acda86-07f1-3b93-8a84-ee94fe6a6024 | -0.95303 | -51.71753 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9bcaef76-ba29-3171-ac1d-9a0322e4c2f6 | -3.18643 | -54.32452 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 105cfdf2-f488-3b34-8c60-6d24674256e9 | -1.19874 | -51.77526 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d2f8319-c93f-3628-a905-0544676226ea | -2.65955 | -46.14401 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 136c068c-506f-3baf-8e31-1039cffa00aa | -1.62972 | -52.40792 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e23f44e-85e0-3015-be7a-1acee69c4557 | -2.98055 | -45.12107 | 2024-11-22 04:36:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a0da8fe4-1954-3e86-aee8-16cbc6bbd272 | -2.52591 | -46.3881 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48d9ce03-11d1-3f8f-bc05-ba4e22dc1037 | -3.47209 | -53.29782 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3646d1e-9756-30de-903b-2d8588d0895e | -4.78824 | -45.6229 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287c06e3-5ef4-3d90-bc9e-fb84ff3863a1 | -2.56302 | -46.15709 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aef296f4-6fba-3963-bd91-8dc330a4b635 | -1.64902 | -52.66948 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc2ae35-5691-37a1-9b96-ee6f3a369917 | -2.21813 | -50.46756 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 665c1728-9acd-3c6e-8def-03655eb3118d | -2.20915 | -49.86574 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80144ee4-c2e6-37bf-bb80-e5f8f03b447c | -1.60144 | -53.21427 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6cee0c33-2979-3e94-95d2-3dc085817870 | -4.13735 | -54.66011 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ddb6320-a8f2-31ed-8990-1e9d697d67b3 | -2.78999 | -48.10201 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2a165ba-90c7-3586-a687-02c09f548125 | -2.68196 | -49.19901 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5fa63bf-e417-3d26-b47c-84de8f1a499b | -2.42476 | -46.52189 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc8cb24-0c76-3a93-bbed-bc81f435bb28 | -1.18659 | -47.66806 | 2024-11-22 04:36:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73eba356-bff4-36a5-af34-56ce78aaa240 | -6.0301 | -46.10788 | 2024-11-22 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed586550-d6a7-3751-9812-9975928c00a5 | -4.39552 | -44.11806 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d0ab30f-869c-3a62-90df-101f8acdacb6 | -3.17622 | -46.26649 | 2024-11-22 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a203ec8b-2d33-376b-8e45-831b2b940145 | -3.00496 | -45.13359 | 2024-11-22 04:36:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 659a201d-0d1a-3526-91e9-46bc9d289a98 | -4.06899 | -46.83271 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03a43c98-b3c1-3c6d-815b-fa0ad14a9508 | -3.50327 | -53.80573 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cd2ec989-58ee-308f-a16a-28af9f090bfa | -4.63588 | -49.54168 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2707b025-bf83-325c-b49d-f8ab4e63c80b | -0.30249 | -51.54571 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b51238a-1867-36b4-899d-af68dd5070b2 | -3.52335 | -53.80973 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a68b1f1-a634-39a5-a4e5-4862a4cb1702 | -2.83845 | -46.67845 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55ab7d47-1705-38ed-840a-44295ffc1254 | -2.76008 | -54.0695 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
