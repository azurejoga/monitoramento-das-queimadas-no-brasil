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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 379d7633-47fc-3560-8d4e-32461c4bc7e9 | -2.81518 | -45.93243 | 2024-12-23 04:31:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 220d8afd-807d-3d04-bfe0-3ccad8185fa9 | -1.37669 | -55.13956 | 2024-12-23 04:31:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beab4cd5-3bc4-3e2f-92ed-c272419d711c | -3.0922 | -46.56536 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 245cd856-0b49-3dc6-930d-76e566381c0d | -4.0838 | -46.79494 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8348305-b51e-3ac5-861a-3957d0aaa529 | -3.94224 | -46.87566 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 209f743d-1dac-312f-832c-f6eaf589e8f2 | -5.9331 | -45.48922 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f5b80b-7ba8-31d3-9502-0140d5b71c64 | -4.77743 | -46.40082 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f2b035f-d202-33b7-8bce-9b03ebd59c17 | -3.87296 | -46.91128 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d306eb3-07be-3ee2-abea-2fd20be1b5b0 | -4.03417 | -46.79022 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 022e2813-40df-3748-b3e5-e6e5c58b9235 | -3.09817 | -54.60489 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9284f085-aa6c-39b0-8242-ca216994ac98 | -1.68152 | -47.07863 | 2024-12-23 04:31:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eccf8fa4-e7c8-330b-b755-e93be92d3cda | -3.92247 | -46.93657 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 664e97ee-3fdf-331e-b4c3-e032689fb9e3 | -4.15986 | -43.64978 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4f558bf8-1e69-38d3-a7f5-34fbaef100e7 | -4.09947 | -46.62914 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 598e1613-4b5b-3de2-af36-06e7e4da4016 | -3.84948 | -47.03898 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7c829e1-d1ce-3645-950a-191e5c11dfa0 | -4.71824 | -46.46092 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d04e6e2e-7618-321b-9428-05f0c2832db9 | -3.9872 | -46.6757 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 050c6f3f-60f8-3742-9666-18e40455c229 | -3.85614 | -46.66991 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f229e695-9fed-39b8-b2cc-4c77a8a28df6 | -3.80164 | -46.71864 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7155c5c6-d4cf-300f-adae-84387e30dbc8 | -3.95633 | -46.76382 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 591ad58a-14c7-36ca-84b0-650d046251f5 | -4.04482 | -49.76982 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c752cc-641e-3dfd-a6cb-bdd3cf29f2f0 | -3.80885 | -46.71621 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c8ca8f-a1ba-3ce6-881d-b51cce427ae5 | 0.06497 | -51.10561 | 2024-12-23 04:31:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d615bfa-1adb-3fc6-922c-06189fbc34bd | -3.84061 | -46.6818 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04ffa9c4-9b3f-374c-a358-734517d62e71 | -2.99654 | -52.01056 | 2024-12-23 04:31:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0bc4a1f-1c19-39eb-b7d5-ac34bf8ff729 | -4.03363 | -46.7937 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a48852f-51a9-3a79-8f74-29be19fb0c92 | -2.40566 | -54.20051 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| da0aefa4-8a6c-39d9-a698-9fc65dd3a5af | -4.10497 | -46.81241 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3737dd2e-3683-3209-9bff-c23ed0ec8797 | -2.53597 | -54.14882 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e75ba89-b331-3b95-b76f-eecef00fc8da | -4.01138 | -47.06112 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58e7513b-4b82-3b01-b8e3-92f4d376d5e0 | -2.74135 | -46.2069 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42fc50f2-4901-3261-8d32-e226fdb9000e | -4.0158 | -47.0547 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1198b27-2e4a-388c-b8fe-da5a0e95a40b | -3.91045 | -46.99157 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6f028ef-62e8-38be-9b0e-12ee1b850bcb | -3.80305 | -46.83996 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51b1ee0e-b188-36a6-bb22-10c6ce8ac169 | -3.90495 | -47.00491 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7ea0162-58c1-3120-ad57-a108c8d43fcc | -5.2431 | -36.18483 | 2024-12-23 04:31:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4f0cdb21-417d-3815-b429-1326059d692e | -3.09428 | -54.599 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 982878a3-95af-3114-9b97-abab6bd26163 | -3.79028 | -46.83439 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc521c08-6535-3af0-9137-ea4b14bc68ba | -4.17114 | -43.65149 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8b4ed63-9007-340c-b58f-7048a6364500 | -4.04269 | -46.79568 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7a2544e-15ea-3131-bac8-0e2c68e11b04 | -4.10721 | -46.8199 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af56d58f-bdca-3254-8a83-cc872f207f88 | -3.9243 | -46.99015 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 845e2818-25de-347b-bbff-a755907ac17e | -7.38355 | -35.27262 | 2024-12-23 04:31:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a8619cdf-bddc-35f9-a584-a7383b2b4bb1 | -4.00805 | -46.56421 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4db485b-96e6-31ab-b730-475e1c8f510b | -3.09803 | -54.54602 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4162d5a0-c6b4-3e3e-a72d-f865e6a9952c | -4.08046 | -46.79442 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7f4809a-cc07-3a15-bfd2-3f80191488c2 | -3.98019 | -46.56709 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a35c4f4-06c4-3b3f-8e15-1ad68f3a6cca | -4.06188 | -47.08672 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b977886f-8de0-30f3-8f82-0a9ebc22a299 | -4.03696 | -46.79423 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c72cd0c-da6a-34b2-8fbd-afb2374c5d46 | -4.09387 | -46.81784 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fad341b7-513d-3fdc-b6d9-0c22df0a8adc | -0.20469 | -51.60334 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98555b54-6107-3ec6-8c9e-485e60e1acb6 | -3.98386 | -46.67519 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d0d6f069-e567-33bc-bdeb-537b0a360b87 | -3.88824 | -47.03085 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fde028c-8a05-3068-bf06-603467c3625f | 0.65351 | -59.7388 | 2024-12-23 04:31:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74279193-c9ec-357e-b566-51957def7355 | -2.12044 | -50.70464 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e119baed-96c8-3525-bec7-7ef089c31360 | -3.8105 | -46.70576 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d74c191e-5aee-3cb4-80f5-29da4ac3a5f9 | -6.94904 | -43.53163 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 899aff96-d11b-3b5e-8017-6875c3867122 | -3.18073 | -50.57046 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7ad8e0b-3637-35c9-9b9a-ec20ad8d0f73 | -4.15165 | -43.65314 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e4b29d21-4362-3d3b-ac90-a3e46abe4e1d | -7.83823 | -35.22178 | 2024-12-23 04:31:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| effbfbb5-e833-3a13-bcd1-770e65bce6f2 | -2.99255 | -52.00992 | 2024-12-23 04:31:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73c815eb-85c8-38de-8d68-8c301223149d | -3.86201 | -46.58844 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a8c4d39-2932-3497-aaf2-761342c2d517 | -0.20985 | -51.5969 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7906b68c-4e24-3817-a52f-1bb450b9916f | -0.96625 | -46.8497 | 2024-12-23 04:31:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ebcdc57-f0df-3dfb-838c-89c39fb426ca | -3.75033 | -43.48035 | 2024-12-23 04:31:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec5327bd-b767-3cc3-9260-a1a423cd7224 | -2.2805 | -47.95457 | 2024-12-23 04:31:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a147cab1-dc87-39ec-a90a-126e6a4d52e2 | -1.45294 | -52.6599 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fac19a32-162d-37a2-8917-a150813da347 | -2.48788 | -54.18043 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed14584-afc1-32ea-b438-f83684b1e669 | -2.08043 | -52.04821 | 2024-12-23 04:31:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce33acae-26bb-367d-b578-88aced101814 | -3.09846 | -54.60371 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 215ab2c2-8a93-3590-8320-8de956116a57 | -5.45368 | -44.80782 | 2024-12-23 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b98c30d4-bdb3-35a3-be43-df447548e231 | -2.98953 | -51.44332 | 2024-12-23 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36572e91-d9e3-3b0e-b354-bbc93a91fc31 | -4.01999 | -46.902 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d2f13dc-1a54-3ee7-94c1-1979326dc241 | -3.75913 | -47.20206 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebbe83e5-9963-3d9a-a8e8-1584bd8540d5 | -1.56882 | -54.76793 | 2024-12-23 04:31:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7213b7cb-4ac6-35fd-bfc9-87c20e9abb88 | -5.35909 | -46.22468 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b1aa5e-93d3-3fd3-83d4-b6af32953bf3 | -3.14855 | -54.56622 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01006fd8-2103-3362-8afe-567dff62156a | -4.09054 | -46.81732 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cb963d2-6612-357d-b895-42fe914daeb4 | -3.83546 | -46.67744 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a675adb6-b162-3153-b228-1e5dfb0ac89f | -2.64292 | -46.10187 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 252c9a78-8845-3266-83e5-515779d97534 | -3.91954 | -46.8899 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e26b281-6ce1-3f3a-9857-6ad765edbda3 | -4.01143 | -46.8045 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25949298-fd0f-358d-9837-98ca26f78c92 | -2.72239 | -46.18624 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 987d9b3b-5f7e-3ce3-a6f7-b33a7ab17792 | -3.21938 | -45.44574 | 2024-12-23 04:31:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac516712-2b91-303a-8134-595ed82ef81d | -4.18075 | -43.63906 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96a840ca-450a-396a-93fe-dda28fb6ad70 | -3.84334 | -46.66432 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f6235ec-9780-3cc9-8e03-0d63bf340f44 | -3.81219 | -46.71674 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f410c0b9-5647-3828-8abf-95b45aa57e77 | -2.62695 | -48.63213 | 2024-12-23 04:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed76f1b5-5fa5-384c-b690-5e033365c011 | -1.62904 | -45.84042 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d24638f-1f0e-3306-ab26-48a1360766af | -4.37278 | -44.00126 | 2024-12-23 04:31:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00aea182-8824-3e8e-981a-e7e60cd1a9b5 | -4.15096 | -43.65767 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2c560c8-48ca-3a58-8498-797e7ab20b61 | -2.52046 | -45.54207 | 2024-12-23 04:31:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d1b27f7-bf69-3e7f-bef8-3a1d66926bb0 | -4.18005 | -43.64361 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8cfa070-1644-36ac-b160-fcbe8e126c21 | -2.46172 | -45.80883 | 2024-12-23 04:31:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aaf43e8-3f51-39ec-94db-f15c29e8d810 | -2.26265 | -46.3904 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35e0baee-4944-3916-8b06-4709929d54a3 | -0.20874 | -51.604 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ea53a3-1001-3b43-8bb7-a6cfcc7cc778 | -3.86146 | -46.59192 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738d3201-f84a-3bc2-8d24-b215b7c2d051 | -3.90956 | -46.67819 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 37fed206-34b1-35ce-a452-6897dec0ed9b | -2.81799 | -45.93651 | 2024-12-23 04:31:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1540ee7-b33c-362c-afe0-b6a5a3ac881d | -0.2093 | -51.60045 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
