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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a1cdba2-a72f-3494-9aa0-aadacfbde739 | 4.07878 | -60.255 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c2531e2-3b3e-3b19-88bb-5fdaa4ec666c | -0.34959 | -51.55737 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 127627fa-8866-3ed0-a89c-94c76d2212c3 | -1.73762 | -52.73834 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1492b219-b5ba-3cdf-b459-79ed0e2c5eb0 | -1.78952 | -52.74254 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70d09c9e-e796-3e4d-99d1-fd7b73a0a97d | -1.68771 | -52.60942 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ac94380-8022-3853-9cbf-75b1004a7259 | -1.77925 | -52.74096 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2fe0f2e-fa35-3918-b431-c8be26fa1fa0 | -0.98665 | -51.71929 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb7e924-b503-3fe8-9371-ac499de93fb2 | 0.9478 | -50.73752 | 2024-11-26 04:59:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e1eddcf-b773-3ac4-9319-d044c0808abb | -2.69333 | -46.875 | 2024-11-26 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 327525a2-87ee-346d-a539-50f38f41cd94 | -0.98728 | -51.71532 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fd7d457-0d50-3ea1-bd6d-1f3998298abd | -1.73874 | -52.79897 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4571b1bf-aded-3aba-8614-e444ea9cf54b | -2.54434 | -46.40443 | 2024-11-26 04:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76403ff7-af1c-3464-b30f-1eb9ea14bdbd | -1.18626 | -53.88237 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb12a6e4-ecb4-3d1b-8427-1b68130a9ccc | 0.66451 | -50.79442 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eceb0895-732e-3c79-ba73-cda56cedf7ba | 0.48628 | -50.9487 | 2024-11-26 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14dc6b32-5a83-30de-9125-553e5490c6aa | -1.10223 | -53.20903 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c04873-dc16-3859-be4d-208b4be03ff5 | -1.10582 | -53.39827 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dfbe329-6e45-38e0-8eab-b16b452b82c7 | 0.67749 | -50.80226 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87b3632a-983a-32c3-ba6a-8d0fb83a27a9 | -1.48622 | -53.8114 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab8a1b60-74a4-3119-8a81-8e389d2a4aa9 | 4.24735 | -59.86138 | 2024-11-26 04:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f05dfd-12d5-3161-8a43-640843cf0c25 | -0.98603 | -51.72326 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bec918f4-6b5e-363b-bbdf-985d47e1916f | -1.77356 | -52.73251 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63116347-7ffe-39b6-9329-f8bae96d61bb | -1.29599 | -51.73067 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbde56e9-c1b8-39f8-8dac-c707fe433f6b | -0.88095 | -53.68555 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b80598ad-5968-3234-bab5-050db00d5b0b | -2.38516 | -48.51553 | 2024-11-26 04:59:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b4b4fef-0440-32b6-920a-b4afc0cec5fa | -1.55983 | -53.79792 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 06be5bca-955e-372c-87a5-741337580273 | 1.93304 | -55.75116 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e775fd4b-cd16-3529-b9fd-5b65060fae1e | -1.82512 | -46.28975 | 2024-11-26 04:59:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2161d0f-1031-39c2-954a-77a2de3b977b | -1.18958 | -53.88287 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05ec18bb-f7f1-3f5f-ad18-b96bcc295220 | -1.43125 | -47.31789 | 2024-11-26 04:59:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8ad990f-02b0-3f75-8a58-288c62635611 | -1.23856 | -53.39715 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 786dba38-b847-3029-9d64-e4b88e43ec0b | 0.94846 | -50.74174 | 2024-11-26 04:59:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dfa6196-2bfb-343d-8968-81d44ef8d7fd | -1.77983 | -52.73726 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55d75404-40c8-323d-afe3-923b49fc17ab | -1.63748 | -53.30585 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef0895bf-247e-3377-9cdb-9159e7987fc5 | 0.9749 | -50.12462 | 2024-11-26 04:59:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb3d2741-2a3d-37fb-b36e-a08365991161 | -1.36036 | -54.63498 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c048aee8-2d16-3c35-96a4-cb2b7a966664 | -0.37402 | -51.54068 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b889f83-e721-3100-aaf2-c996cbb76c1c | -2.50133 | -48.34689 | 2024-11-26 04:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d0c6afb-cc06-35d8-9570-e66ae9e6cc67 | -1.56428 | -45.68037 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d38243b-b643-3653-88d3-f465997fba1f | -1.56477 | -45.67716 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8480a6fe-6b4b-32b8-8ade-0ae1f0dd0f1b | -1.08468 | -53.64259 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffba9f8d-e931-3583-bb4c-d3fd9b9eb822 | -1.27403 | -52.69961 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dc34063-31b5-3fe0-a71b-23211284296a | -2.38564 | -48.51291 | 2024-11-26 04:59:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf4d156a-cc2e-3e43-861f-bf4ab5d096dd | -1.6689 | -53.20454 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8be3a29f-d0eb-35d8-9557-c9b990cc2763 | -1.73931 | -52.79528 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56b8b546-7e00-363c-90a8-b790313edfaf | -0.91534 | -51.64353 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0775fae7-6dd0-3fdb-acf4-54cc47855f95 | -1.3829 | -53.62387 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7baa12e1-d299-3646-9236-c99ff3237c2b | -1.19289 | -53.88339 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c368c914-1e76-3caf-98d5-cf5aa4dee76e | 0.59765 | -60.46881 | 2024-11-26 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f577f44-90e1-39b7-ace1-2153a9f44e8c | -1.04836 | -51.74001 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4550d14d-45fc-3570-a28f-483785846df6 | -1.04128 | -51.73891 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1444172a-06b9-3f76-92fe-9cdfb391635f | -1.11417 | -53.38869 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7327079f-bbd7-3b87-8256-b035450926f1 | -1.63276 | -53.87337 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e19404a8-2402-3e84-bd51-3d67c5c20c08 | -1.18572 | -53.88584 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b9ef946-779e-3990-8cd0-cf70d0aa3b95 | -1.61094 | -52.35876 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 789c681a-6db9-36dc-8e02-4a12b9959b56 | -1.43383 | -52.44148 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe39abb2-8857-3c23-a37f-5bb9a61f6d60 | 1.81615 | -55.9477 | 2024-11-26 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c35ea35-a5ad-3e82-acad-b01331407bef | 0.67681 | -50.79803 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48243ddd-3daa-3b20-8565-271e5e64939a | -1.58635 | -45.46365 | 2024-11-26 04:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cf249aa-4226-31b8-9578-5978e599e3f1 | -0.97373 | -51.70914 | 2024-11-26 04:59:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a7da127-cd0a-344e-afb1-7ee72a3ed1a7 | -1.7194 | -52.72082 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef4a3575-7a23-36d3-abe6-527f494c3f38 | -1.11082 | -53.38817 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618632e2-6ed5-3079-96d6-c7fab233bc76 | -1.62806 | -52.27147 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd45ce4f-a862-300c-9476-0494036aa28d | 3.15511 | -60.5027 | 2024-11-26 04:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63916eb5-7b55-31bb-88f1-f99603c2fdff | -0.9398 | -46.78489 | 2024-11-26 04:59:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384c411c-d3bf-39df-a3b7-493483c875db | -1.19365 | -46.19952 | 2024-11-26 04:59:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aceb6cf7-f009-39ca-81b1-f1c954537142 | 0.66087 | -50.79499 | 2024-11-26 04:59:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d86aba44-95b4-3068-a137-2dfce23b8adc | -1.34992 | -54.63686 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7879a5f7-83a6-358d-9509-9b7c3de4145b | -1.06526 | -53.20354 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6989aa30-c9d9-3d2f-a4ff-f75b020e2e45 | -1.42246 | -55.2756 | 2024-11-26 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cc535f6-93d9-3270-b5b1-27da4df7f821 | 1.94153 | -55.71592 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a13fbd4f-6c8d-33de-903d-38fe97213e5c | -1.10638 | -53.39474 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06a5baea-e648-3902-8775-95e7c2b32a80 | -1.56038 | -53.79445 | 2024-11-26 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 24c23139-88b9-31e1-9af4-b33a0e5c7e38 | -1.1303 | -54.17371 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25575e6a-3ed4-3968-98aa-29a129976ace | -1.78609 | -52.74201 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8d9198d-85d4-3abf-b045-b13934773e5b | -1.30256 | -52.54076 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482ee717-a6cc-3d29-9ee0-1c539dab0aee | 3.82293 | -59.60092 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db322813-0990-36a1-98e1-906057e8d103 | 4.07804 | -60.25013 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 371d9028-865e-3092-8ca8-edc528fd5525 | -1.39432 | -52.5582 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dd04e98-2370-3656-a958-ed9bb0dadd23 | -0.27259 | -51.51752 | 2024-11-26 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e3c9f0-3a05-3575-a86f-f214f2da8666 | 4.23534 | -60.07756 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e0d9d9c-98f2-3aed-8470-3ce7c2cdbbc1 | -1.36685 | -52.55398 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7cb9ea6-69cd-3e76-83f5-cd460b1a9298 | -1.17475 | -54.12786 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a1ab968-bf2d-3c50-9bc5-d8f99726387e | -1.46753 | -52.29546 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 683b79fe-4c08-33cc-a3ba-3bdf4b0a5fa5 | -1.08523 | -53.63907 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d9c615c-2b18-3b68-9716-404413a5bbd2 | -1.55899 | -45.67961 | 2024-11-26 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21842445-767a-30d6-9c66-1744481535df | 4.23073 | -60.07763 | 2024-11-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5e3965a-af0b-3441-8d0f-41ae870e5d5f | 1.93588 | -55.74695 | 2024-11-26 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0b59074-b93b-3bc4-8aad-bd74d167aa14 | -1.4716 | -52.29219 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a590f56-b214-321a-b60a-ae615f1f9deb | -0.91953 | -51.64007 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b177a53a-8247-3835-90c9-0f8a5ad48d71 | -1.07596 | -53.37534 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49cb1992-7f88-3835-8ede-694bbfafd22f | 2.68844 | -60.42629 | 2024-11-26 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72e3385d-4062-3f5d-8fb2-99fef8b5c7f1 | 1.81429 | -55.95509 | 2024-11-26 04:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e46ee34-e929-3742-b198-569567085a75 | -0.94989 | -51.65227 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 960e91b5-095c-300b-a9d1-889c5a48728e | -1.82635 | -45.58389 | 2024-11-26 04:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71dcb19e-3d69-331b-b13a-7e531bbd7e3e | -1.56686 | -52.01352 | 2024-11-26 04:59:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f03de742-2958-31ba-b726-da39b5b0439b | 2.68774 | -60.42171 | 2024-11-26 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d89968d-1830-3d39-8bcd-ab25d422947e | -1.36674 | -52.08786 | 2024-11-26 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42494194-f334-3e26-aa83-43c1e4fce192 | -1.13306 | -54.17767 | 2024-11-26 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2826f8af-d1fc-3db7-bdcc-c12f0dfb3147 | -1.66647 | -52.25379 | 2024-11-26 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
