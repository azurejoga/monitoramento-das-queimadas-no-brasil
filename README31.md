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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d162e0a-5eb5-3496-bc09-3f063459ec44 | -0.26892 | -51.61916 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0181ee35-0794-3e60-8ba5-d75ea8a4d1f9 | -2.68692 | -46.17152 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 356961d8-2235-3168-8f18-469e0714ea82 | -2.63369 | -46.21427 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bae182a-6e99-30a6-889d-1abea5134cf8 | -2.62406 | -46.84383 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f82ef84-3cc9-305a-ba5a-9e21a33a5d47 | -2.93968 | -45.61995 | 2024-11-23 04:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b382667-a614-34d9-8053-2a5574258970 | -2.69802 | -46.07935 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfba789f-13ea-338d-8a35-8538d375882b | -1.6721 | -52.66237 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f604cb94-74b2-307b-9ba8-18d89a1a7e25 | -1.77707 | -53.61634 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53fc08d8-95c2-38c7-a682-d2f48beb3ebf | -0.92318 | -53.10526 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d39b3e8-1731-3549-8a7d-d88f440ba3b7 | -1.62246 | -53.32121 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d31e0690-603b-3b65-bbb4-4fe4724ad280 | -2.14793 | -50.91505 | 2024-11-23 04:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 37f8c494-6130-32ea-8425-94ba4271accb | -2.6753 | -46.24464 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 598f2554-227e-3a94-ad73-7bf240489dd8 | -2.74651 | -45.97451 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dcc1872-690d-3a62-bcd8-209cf3582cdd | -1.83215 | -54.52532 | 2024-11-23 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a670eca-4d22-38a9-9fbf-8b6c0365a0b6 | -0.88401 | -51.72315 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78341ae0-c7cb-303d-9f45-35e1f152db20 | -1.55853 | -53.53418 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f3a40ae-605c-3864-8604-4be30c01b11f | -1.52933 | -51.62811 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 171df9ca-3372-3565-bc84-f56bc14765b3 | -2.55108 | -46.54723 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b4c7c2f-ca6f-33fc-ba05-310cb01ccc67 | -1.23867 | -51.74568 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3003329f-1387-3d1d-85fa-a7ea003dad52 | -3.26981 | -45.1306 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c8c4f1-1b1e-3112-bbec-2588e61b858e | -0.23871 | -51.62181 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d63db5a-c619-381e-824a-befa429c2baf | -2.21153 | -48.91218 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3036d5e2-4436-3de0-82bf-21a1358df19a | -2.70303 | -46.27285 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11b41f8a-3630-364e-a50d-ad8557837d15 | -2.70435 | -46.08426 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09fbefd0-9977-37e0-b56a-dac3c52cab06 | -2.63121 | -46.22967 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e46c73a-5f05-3355-a783-3381a29fd578 | -1.60343 | -52.58887 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed5fe54b-6aab-3171-a2b2-967ab74e4ae1 | -1.42231 | -52.67443 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef43f973-be68-3ced-9b91-cbae3e10a45e | -2.73206 | -46.08863 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1fe9542-4de3-36e1-bff5-acf2b9455e59 | -2.13202 | -46.40351 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 16ed6922-d89c-3618-8c47-5b3a850f794c | -2.50848 | -46.21943 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc785f4-80f5-39c1-88b7-5477b6d34c84 | -2.76835 | -48.60802 | 2024-11-23 04:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0028f41-913c-3ddc-aa9d-97b0770c3102 | -2.3803 | -49.10334 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bca4d8af-da41-317d-9ace-cd3e9b555453 | -2.66832 | -46.24353 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac06cc18-de14-3fa5-a0a9-3d8f7e9381e6 | -2.71866 | -46.10601 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b9bb8ce-0cf8-3f9a-82a9-b12b900bf82c | -3.16362 | -45.90792 | 2024-11-23 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86bbfe9f-90ed-3610-8523-8379e63bfc78 | -1.30282 | -52.28082 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04bb867d-9aa7-3a7a-bafe-240113c603dd | -2.79247 | -45.94654 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a08bb25-06e5-3dea-8902-2a161288fe8d | -2.75992 | -45.93429 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9e915551-cca2-3095-b4f0-7c64ee6a7219 | -1.72972 | -52.73358 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5426541a-a5f5-34d9-9d96-3bc982db919e | -2.56247 | -48.16269 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae55c86d-cf85-31a6-abf5-b88b392e65ce | -2.15367 | -50.49802 | 2024-11-23 04:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f0f4c74-9ac2-3a4b-93fe-b2c18594e96d | -2.5842 | -46.54364 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99bff552-5bac-3b1d-902f-2862a7dd3dbb | -1.28127 | -54.54995 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01fdcb9d-5a09-3652-8dae-c55bc52a8071 | -2.70941 | -46.27782 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa4fd146-bdb7-389b-9dd9-2b1db78c2506 | -2.69666 | -46.26788 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 236f060f-4cef-3e4e-9a10-66834e179def | -2.29009 | -48.42956 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 127f76f1-27d2-3126-89be-505d3f57ab7e | -2.74049 | -47.54354 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8755be7e-3297-3110-9015-76bc30fbac3a | -1.11395 | -53.39707 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a138bb85-becb-322c-a0cb-0689c62e02ba | -1.72179 | -52.71509 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17fcec46-9942-3268-bd40-10d9feea5f2e | -1.55914 | -53.5305 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc6a9f72-a453-3aaf-87e5-2b7489b64843 | -2.53492 | -47.3633 | 2024-11-23 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0d1f35e-54ca-3c75-ae8e-99e606df9f20 | -2.41572 | -50.31081 | 2024-11-23 04:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81ff9472-33d2-388d-ba86-4e9b2bff0774 | -1.11896 | -53.40189 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e85d317-6896-35f9-9862-a53dfbcdff94 | -3.17737 | -46.5034 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3220041-aa64-3b2d-87a8-6eb2ec13bff4 | -1.20753 | -51.7466 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 345c048a-0652-301f-b40d-b3f3e41bc539 | -2.66156 | -46.15177 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6244d99-6917-39b0-8e8c-78ba5c2da201 | -0.25885 | -51.55846 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b84a8b5-99ed-316c-b428-6c680ff88245 | -1.6027 | -52.58649 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b21384a-50b7-3dac-a0c4-c36dc76c383b | -0.10442 | -51.66043 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c889fbfd-424e-39b7-b90e-4c0e8b078ef1 | -2.93925 | -48.01545 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3585768f-8c7b-31ba-b738-9c7645fd94a6 | -1.74278 | -52.38781 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5591f77b-5ade-378c-806e-24f0de5d4eca | -2.70826 | -46.10435 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 422c28b9-ddf8-319c-bccc-9d17356a3fb5 | -0.87849 | -51.72527 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1030ea41-bcd6-3398-aaec-b05612cbefd3 | -2.59978 | -46.26077 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b75193e-4604-356f-a6f7-fcef30aa7b61 | -2.92508 | -46.83753 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8a2f3db-b449-3e4b-b1d7-2b3d42daa876 | -2.6956 | -46.09455 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2ecf390-7e09-3953-a5a0-20ea0f13da67 | -3.60703 | -41.67669 | 2024-11-23 04:16:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11b04618-9041-3c41-bc83-4efa827b45d1 | -1.7475 | -52.39186 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91e304ba-dd84-31cc-a5d3-f0846b37d226 | -1.67157 | -52.66569 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 76ec2dce-5bd7-344f-980b-0ef1f66fe1a7 | -1.24323 | -51.74944 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 194e8c5d-f5a8-3d33-8781-75fa2b2fbaa9 | -2.70601 | -46.09617 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2833af07-1c37-3ab7-92c8-2c607eb4962f | -2.61861 | -46.26339 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fb76dfb-6e53-3d44-9df3-034434d5a3db | -3.60355 | -41.67617 | 2024-11-23 04:16:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 352b390e-e2bf-3edc-8f75-4fca7b1da2ac | -2.69214 | -46.09402 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 476cd786-1988-370c-b293-0705aa0d3955 | -1.62306 | -53.31755 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3e3ea58-77a9-3932-a813-44cf4431c606 | -3.16702 | -44.40636 | 2024-11-23 04:16:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30bf02e8-5e66-3196-bc0b-9d90bdaff706 | -1.25529 | -53.36314 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90316228-a057-35ed-92fa-9bb970bfc4d6 | -2.63055 | -46.5715 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8c112f5-10f1-3665-96b2-9dcbee308df0 | -1.22405 | -51.7403 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8952e903-1650-36e8-9414-3a1c66604e72 | -0.76632 | -51.77684 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f17550f-8f12-3e5c-8260-ff9506b40652 | -1.53042 | -47.29753 | 2024-11-23 04:16:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69c71866-e0d8-321e-89f5-948346495f42 | -1.29219 | -51.73359 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc2119c-40f8-369a-bb9d-1bf7352fa31e | -2.00151 | -48.52983 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e2a3913-28b8-3b86-9b2c-e02057dddfc8 | -2.66565 | -46.14848 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 181558cb-f3c4-3922-9bdb-187935040bc1 | -2.68753 | -46.16768 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c344c09e-b701-369b-85e5-235de5748009 | -2.4519 | -46.55716 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 467ba6e5-c268-35b4-8a24-dbd3e3dae50d | -2.53859 | -46.37508 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e2e50e5-5ad2-3015-b42e-4df733171f33 | -2.15822 | -50.49875 | 2024-11-23 04:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c39ab680-e551-39a0-8e97-fc52ab6225e9 | -2.71002 | -46.27395 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 21e53901-55da-37a4-a12d-022f24139ca9 | -2.19525 | -48.34484 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a80d5f7-493a-3285-a873-8d3f374f0b58 | -1.21962 | -51.79949 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef5ed218-2f8d-3e0c-99fc-8a6560adafab | -2.44504 | -46.53151 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34226abc-c248-315c-a27f-24fc72a565c3 | -1.21902 | -51.73948 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39b1a0db-64c0-376f-be11-9cfce0e2a469 | -2.56045 | -46.55686 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bc49fcc-c009-3055-8814-467339d103c3 | -1.14141 | -51.68127 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3366003-7646-3e8f-bdee-c2fcd362d1d7 | -2.79307 | -45.94279 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc4d0140-4e6c-3fcd-93a9-d8816af04c21 | -2.64453 | -46.23577 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03bd8932-9e5d-3742-bf09-d3b7d80ccb89 | -1.44171 | -53.39479 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe2724ed-25c4-3c06-834f-dff76511fbc1 | -1.71517 | -52.49183 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa21608e-fda2-34bc-aa6b-390a4c4f49be | -0.26085 | -51.57259 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README32.md)
