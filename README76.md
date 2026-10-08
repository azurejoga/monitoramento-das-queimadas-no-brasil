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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcfdddbe-d9ac-3c53-a859-7f6e05452a5c | -1.77463 | -55.06112 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a332ba42-5e55-3c3a-b606-24be0f8793de | -3.04887 | -51.22282 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a8101c28-d913-3c09-9867-d2e0b78cd449 | 1.7138 | -55.59878 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bcd6b00-7b40-34ae-bb0d-13ca33a7402d | -2.15788 | -51.97911 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17bbf4a3-01a3-3687-adb4-b4695f444d78 | -2.56281 | -50.58904 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1907fe6a-d40b-39f5-be76-e6e7ebdc0bd2 | -3.175 | -50.59398 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b9cd9f3f-9b5a-3e0a-aba0-810719fc50c0 | -3.09578 | -51.37957 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c7aff14-df0d-35a7-bad0-d94f6cd54c55 | -2.1719 | -54.4603 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89853c05-bf60-3e1d-98ec-6e8eb3b69a76 | -1.51871 | -54.51708 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa65bf2b-438f-383d-bb5b-8ffc733ae7d8 | -2.26813 | -47.8736 | 2026-10-08 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cf9a7bb-58bb-3ca0-af1f-19f395d4dfe9 | -1.75284 | -55.12129 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3775bc1-61e4-381e-ba93-99f143484bb6 | -2.27369 | -48.74753 | 2026-10-08 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 687ccbe5-3a86-3ff0-b45d-af24093fe7c8 | -3.10469 | -50.31927 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de86bf28-3785-372e-bd23-8986bc6a470d | -3.26153 | -50.40728 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae04a3f5-d576-36c8-9d1d-94022a1f6594 | -1.97633 | -56.06269 | 2026-10-08 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d2f079f-ad66-302e-8dfb-bc01cd32f709 | -2.78415 | -51.67587 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 289ca701-7bf8-3ef7-8f9a-956b36afb23f | -1.10688 | -54.15123 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c460b1b6-ea60-3706-bb11-98a6d8d77b8d | -1.29452 | -55.71469 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1bdfc1f-b0c2-33e3-b773-14adb5a86494 | -3.19568 | -50.54804 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bf4cc95-eddc-32ae-859e-3e96132376b2 | -2.58493 | -54.62177 | 2026-10-08 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d02d0b0-2d1f-3fc8-b256-507883185250 | -0.85094 | -51.84943 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ec419d3-cba8-321c-b999-8c655ca1bf01 | -2.4142 | -51.298 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f6c84d0-c80c-37e1-8ada-f1c54981e01f | -1.38982 | -55.46322 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4acbb2b4-6043-3277-97dc-46d4a903f4f5 | -2.47105 | -46.01856 | 2026-10-08 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc6db25b-c2fe-3bcd-af0f-9452fd8ea2fc | -3.16816 | -50.45944 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c687372c-a94e-3ebd-b17e-7718f61b414c | -1.60471 | -55.16247 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c31b63e7-1111-38f3-99cb-ddda1f26fbcf | 1.33023 | -50.84651 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c5081d-0148-3be0-bc0a-ab23acfbc34e | -3.24574 | -46.95988 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82a0b396-1a82-3a29-9c6f-5419cf40e33c | -1.02396 | -53.73708 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44a3cb03-33e3-3f21-8dd4-30c3d42f8112 | -1.44532 | -52.68855 | 2026-10-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38a5f4d1-249e-39d7-a159-a747075917a9 | 0.69947 | -51.43291 | 2026-10-08 04:44:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86566dba-c52a-3336-89ea-6eec61e9acc3 | -1.20732 | -55.68929 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45bbfdce-f040-3e4c-bf54-19f88c8519c5 | 1.33432 | -50.83441 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a4903ab-6ec0-3a9b-ae29-16f8f218a3d1 | -3.23568 | -50.17836 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c8a337a5-5d6b-324d-8dee-92faaf13f068 | -3.25654 | -50.39598 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cbb49405-504d-3f88-9f10-edc539cd7a0a | 0.78749 | -59.19871 | 2026-10-08 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 493befd4-eaf3-3e22-8ee2-b3e79c7140b3 | -3.17393 | -50.60083 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d05076a-2566-33c2-9886-17325aadb54a | 1.32017 | -50.84804 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c777b1-ebfc-3efd-b7da-235cb0ed0dc5 | -1.28926 | -55.69409 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 719da646-7fbf-37e5-b091-e3b013e1114a | -2.69396 | -49.04583 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e2cf8f5-d19f-3253-8cbb-32f552e6d567 | -1.02668 | -49.223 | 2026-10-08 04:44:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4441e9fa-de37-3b04-9c30-07bde1e71a32 | -2.1335 | -54.46132 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d1ec71-f51f-3b3d-b613-7afca627ef8e | -2.33817 | -55.6949 | 2026-10-08 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a6d8c3-c003-3acf-aedb-66051c6de293 | -1.19531 | -54.20799 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ccc2bf9-184a-3494-80bc-74bed796484c | -1.32395 | -55.43361 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38cac2a9-e658-3e06-9642-cb1219ca31c2 | -1.82628 | -54.93459 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f40d5285-d037-3c5b-9065-892f603f930a | -1.82574 | -55.0378 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0e5ee547-ec93-39e0-9a20-2f1aafed7c6e | -1.83105 | -54.93016 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff00f2eb-7d43-3afa-931a-299728a67b14 | -1.12343 | -54.12057 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5f386d2-dc67-35f2-a17d-a985404bd782 | -0.04647 | -53.25016 | 2026-10-08 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 491efdbd-dd60-31fd-9283-cc97ccb0791e | -1.53657 | -54.55452 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 10b4ec3b-6a65-376e-84bc-144ab85de15c | -1.27043 | -55.39936 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 909de751-1c59-370b-8e80-4e9770bf5e88 | 1.43597 | -50.69933 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7939a244-4f13-3e93-8a1a-a6c1f62640e4 | -1.82909 | -54.99208 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd74e5ea-d5a7-3e1c-a489-4f67267dc575 | -1.83305 | -54.99272 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e03af5f4-4331-31e0-8da3-653fc2654af6 | -1.12995 | -57.28516 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e862c7c-7ca4-3cb5-b063-20d65bb94dad | 3.74293 | -51.6265 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06015778-006d-3105-b7ea-86431a3a8f10 | -2.78723 | -51.67279 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccd617b1-fea3-35b7-b150-1456768bd07c | 0.4497 | -60.53888 | 2026-10-08 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1dc9f22-a8b1-3a51-8c8f-c10e041b006a | -2.22148 | -53.7014 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4c66d6f9-1a79-3585-985b-1c8b1488ab7c | -2.0416 | -56.1988 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73543d8c-9021-3b7d-8e76-1db364bcc749 | -1.1039 | -54.16983 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 681b5b86-684a-39ac-8d84-a599b1ac8e69 | -1.19525 | -54.20578 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 018ee181-7b9c-3c75-ae4f-c7681e1a40c0 | 1.77765 | -55.5421 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1208b4f9-7291-3572-bef4-ace4edd4d9c2 | 4.31522 | -60.35469 | 2026-10-08 04:44:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8705fff-1911-3971-b752-3d7aac4ba11e | 1.05707 | -50.03585 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| effca840-c7a2-3f62-b814-1ddff2ae2604 | -2.7836 | -51.67941 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aba7a93-d438-3882-83a5-ad1be60e667b | -2.0417 | -56.37797 | 2026-10-08 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fe07246-7dfd-3a61-b591-b16d6a659e9b | -1.45865 | -54.76929 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a4c152f9-37d5-3e68-aebd-a2b606cbbfd4 | -4.15687 | -43.19624 | 2026-10-08 04:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 200e6582-5e95-3186-97bf-92c575f8b28a | -1.52959 | -54.54847 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc73ac01-a9ab-3756-bdca-8aabdbdd97cf | -1.47861 | -54.54499 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cf8d4b1a-7977-32d9-9ad6-768c71170a9d | -3.19844 | -50.55197 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5fdb8a7-8305-3e78-a7bb-9ed8a9406d7b | -3.16478 | -50.43787 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15e79f19-b6ac-36b7-891a-4cb89eb6c7aa | -1.14674 | -54.21943 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4572b30f-0870-3fdc-b7f9-21c87b4f6ebe | -3.40225 | -49.1248 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 495e21ac-0244-35b4-8c09-bb8ba2ca6e31 | -3.27303 | -50.39853 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ee3c562-a012-366d-941b-54565aa598ce | -3.17583 | -50.4536 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 593c6d8a-9c22-329d-8ff4-1632bb4bf288 | -3.17679 | -50.55551 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e25cf497-99c2-3cee-b150-bd6096db6d6f | -3.18311 | -50.56364 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed1f3a4a-be25-3bfa-bc87-5e49e21a740b | -3.20396 | -50.55984 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5033c7b4-6ee0-39fc-84f2-b7ec03844e6c | -1.10084 | -54.16462 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19448d92-7662-30af-8b66-c82238221056 | -1.22771 | -54.12447 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e266e56-c4b9-32b2-b1c2-8a7852d14648 | -2.40222 | -51.31033 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 159ce034-9e93-3c65-a8fc-8c091fdf0b39 | -1.51957 | -54.56171 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a5443b7-a45c-3b55-84d1-f500a0072e7e | -3.29994 | -49.12764 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9edc889a-ee75-3d36-b389-d113b5f6f051 | -3.23771 | -46.96321 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76e001ba-eb43-30c5-b82c-cd50fab211ab | -3.17529 | -50.45703 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46e22ff3-52e4-3752-9b94-d651e2177aef | -3.17476 | -50.46046 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46c0e15d-3e92-327f-acb5-1e13ddae2640 | -3.19247 | -50.56859 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddd50153-f26c-395b-a10e-ea45c350905d | 0.8629 | -51.35902 | 2026-10-08 04:44:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a505ddec-4419-32ec-bc90-5667562faf1c | -3.12895 | -51.14672 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696c4bf1-4ae9-3bc3-84ef-9a46f028f5ec | -3.27908 | -50.14291 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bc61955-5b91-302a-b536-1b493679cd28 | 0.78793 | -59.19872 | 2026-10-08 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fff954f4-a9c7-3a46-b560-36279befaa8a | 1.75103 | -55.57174 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08aaab82-6d05-3e28-a6b8-2935bcb8d7bc | -2.4672 | -46.01797 | 2026-10-08 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aa93d53-1172-374d-a191-fb32c253117f | -1.10159 | -54.15995 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c16f145a-7e07-3cd8-9fcd-4ba2cc1abe38 | -1.12038 | -54.11534 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac9fb69b-42e3-3a73-98d4-9ba446f6ccd3 | -2.46916 | -46.02 | 2026-10-08 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2887cc4f-9870-3bcd-bfbf-4d6cb214f66b | -3.00722 | -51.12069 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README77.md)
