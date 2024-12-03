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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e155ef9e-0aee-39d3-8a24-b58a5844cf8f | -7.80046 | -38.73599 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c1ed6e1-def0-3c76-ba21-41c0d7a6bdc8 | -4.52825 | -45.73881 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0f92b62-2ebc-39dc-a5a1-24d41d80a41c | -3.22859 | -46.44928 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e66326-b034-3480-9d4c-ccf88109738f | -2.30417 | -47.27391 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf32e2c5-a386-385f-81b6-53da32d5e5f4 | -2.43353 | -46.66735 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45ce333d-e4d0-3632-8feb-12c870f68d8c | -5.48231 | -46.34638 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d059608c-fb24-3613-aa77-8089752c10d8 | -3.93536 | -46.7082 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6782c58-9b8d-36db-bcc4-be7d3ff369dd | -3.27998 | -53.24756 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a148a7f-322a-3f4b-a9fe-8eb110abcc71 | -2.68504 | -46.60126 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8629e208-b75e-3f78-9a22-b2d85b602404 | -2.77324 | -46.0191 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64eaded1-b2b0-3624-9167-079b8199a07f | -3.1342 | -46.61853 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eea05969-f3b6-3c6f-82d4-385cc9f2eb4f | -2.60852 | -54.09233 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e7012f9-3ab0-31f8-b4e5-d778a45c8303 | -4.03679 | -46.86189 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19de3066-d321-333f-9ccf-bb45910189f8 | -3.21498 | -53.11959 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e66d2b-5133-379c-a42b-d3845654ba06 | -3.37099 | -45.84054 | 2024-12-03 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6ee126-059f-33ef-94d8-5f798fb0dd57 | -3.18139 | -54.33472 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6bd68cb-3c0b-3016-856e-ff7facb1e5d1 | -4.06889 | -46.70065 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acd717f8-6b6d-3ab9-8cbf-706e5656540e | -3.54691 | -51.45913 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e56dea70-2cd4-335a-a019-d0b145d3bc12 | -3.02477 | -54.18951 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3403ea9-6185-3b6d-ac6b-6884816a7192 | -1.69226 | -52.6325 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fac85826-ec98-34b6-bfe8-3983432ae9ea | -2.66484 | -46.12373 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36bbdde3-efd4-310e-924e-3bbefc182037 | -2.33403 | -53.81882 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cff8a17-d463-3d8b-9f09-f70e9bebcf3c | -1.66856 | -52.40089 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2c46ddb8-381f-35ff-af72-88a2792bdd4a | -3.82121 | -46.59085 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a4c77b-3792-38e1-b7ce-e35627c7f47f | -4.0422 | -46.8274 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41f78d33-b92d-36d5-8e13-eac2a3f497ec | -2.58497 | -54.23508 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dd51401-5407-38fb-9178-a31a6abd64b5 | -1.61083 | -54.24906 | 2024-12-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3023b7b5-8aae-38c9-ac2b-90e1ad47f309 | -4.05135 | -48.08501 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7367f04-09e5-3495-b91a-587324d0af72 | -3.75701 | -48.16058 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cfa572e-91d2-32df-8cfa-c5c67b8f68fa | -6.03223 | -42.52076 | 2024-12-03 04:29:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 36416bc5-0d47-34f9-923c-35b680811f6c | -2.67903 | -46.61794 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ae93ba-8adb-3068-96ee-2fbafa4aa934 | -3.83587 | -49.00359 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96dcdedd-8b51-3e2b-9fb3-f043b76af8ba | -3.18821 | -54.33255 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff2dbee9-7e2d-38ac-92d6-cebf60d7cddb | -2.98747 | -53.35275 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 767eaefe-6860-3dba-aaff-93da0097e4d4 | -4.48496 | -46.36241 | 2024-12-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4179bd2a-6a9f-3e9d-b748-9189c205f8df | -2.483 | -46.5695 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6368401b-cad8-3620-be7e-1049156e3379 | -2.79928 | -46.82664 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a20594f-d318-36ca-a6b1-cd7f5c6456f0 | -4.80668 | -44.99843 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7a06bf5-7ce2-39c3-940e-4a604d384534 | -3.82681 | -46.62009 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b5537f-9b10-3279-a3f1-5a0eecfe26ec | -3.26149 | -45.36883 | 2024-12-03 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b9f7e01-709c-3477-9d9e-42e77c5b6731 | -2.2086 | -53.78403 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d1cd915f-f1a3-3bc1-96f4-23a4aae89fbf | -2.67027 | -46.0889 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a9031a6-d3c5-39cc-b50c-286f6a0d7359 | -5.4562 | -43.58477 | 2024-12-03 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d47697ad-e9eb-3b10-8d11-46230c8faa9c | -4.35221 | -48.56194 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef5e53ea-8b26-3851-a143-8a34d3fff336 | -4.17039 | -48.19302 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e89c1a75-357e-3c13-bb60-c649dadc25eb | -3.17795 | -54.33607 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f756caa-105f-3395-9998-3dc22a885ed8 | -2.26488 | -53.60843 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ba7d6aa-2872-3f47-b946-bb49e3464aaa | -2.88805 | -54.16017 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29d22a31-5539-3d09-bef1-fd9c41b97710 | -3.5494 | -50.14415 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12c599e7-dcef-33bf-b8a8-cce7b897ef10 | -3.18057 | -54.33981 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b6510988-83b3-3320-a3b2-9949a8f2c88b | -4.03532 | -48.33801 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e386ac09-af0a-39eb-895b-7a3e3f3ba1d4 | -4.29364 | -48.20549 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3efacb9-bde2-3fbe-b928-55d121a1d3e9 | -3.58709 | -53.04675 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfa40ae8-7f35-33a2-b658-102707959986 | -2.75164 | -55.34081 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84512795-0d75-3b25-8320-945663e0909c | -2.6165 | -46.8863 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b1946fc-b16b-3a11-b4cf-30c9a0f47de1 | -1.72834 | -52.77811 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a021dd7-cd06-3dca-8879-8b96ef23e809 | -3.31998 | -49.93112 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9005e6ca-09af-31ae-b411-21503c829be1 | -1.7453 | -52.64701 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3342525-1fe8-3f88-ad55-c95b33d8856f | -2.19788 | -48.33996 | 2024-12-03 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d521763e-3b10-3877-a59c-139a8801bbb3 | -3.54339 | -50.18105 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73aefcf6-820c-329c-9e1e-8eaa50770d02 | -2.46784 | -46.53533 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6956ccff-f1f4-3345-a1e5-fa0a46eb283b | -2.81553 | -53.05003 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b789d70a-ea72-3b37-84c2-26d34db732f1 | -5.42035 | -45.11581 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae8bc7cc-f4ab-323d-8124-5f71e2e87937 | -6.99368 | -43.50964 | 2024-12-03 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 234c9d97-eae7-3a22-8651-60f0b2b94aaa | -2.85345 | -45.06392 | 2024-12-03 04:29:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deebb452-31c4-3829-9ae7-320deee1880b | -1.78182 | -52.74883 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5954de24-818a-397b-ad08-40b9af7dc295 | -5.12454 | -49.92929 | 2024-12-03 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19611714-28e1-3a6d-9afc-69a86a610da3 | -3.24535 | -53.65052 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8954e90c-ba0c-3ecc-bcda-ea612d29082d | -3.11967 | -53.98747 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f636c00b-6a6e-36cb-8178-0468364cf88a | -2.80118 | -53.05622 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed641207-a5b1-38e6-9e46-29370f8d2015 | -2.51492 | -47.42383 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dac2e454-5b8a-344f-a66f-f21da780e7ad | -2.51269 | -47.41639 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d210b878-5e13-30f3-8ffd-158e96f85b2d | -4.15152 | -48.22597 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67858ada-6feb-36cb-9597-771d7e7526eb | -6.03136 | -42.52496 | 2024-12-03 04:29:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 13280935-0e77-3823-8a94-60e94c871a97 | -2.30862 | -47.28873 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f73f20be-7acf-38e4-a9fb-ff03c5c7012f | -4.06917 | -47.08954 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 090b1fbd-1645-31be-b916-e0786824de66 | -3.32632 | -53.54651 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 175a095e-021f-3c90-83a1-cc275afae6e2 | -3.18864 | -51.1637 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c78b658-3990-3a13-be97-1a8823e2bb2e | -3.09079 | -54.29812 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62a74f6d-0edc-35b7-9ff9-9b0efc4fe8f5 | -1.94675 | -53.32907 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c6587dc-59dc-310a-a6e4-9497181bcc16 | -2.42863 | -46.50457 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0083a9dc-d331-37c0-8025-5f9b36fb6287 | -2.4863 | -46.57001 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e260fdc1-c91e-3379-82df-eb968d579058 | -3.89771 | -46.66693 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d44ba6-4476-3fdf-9996-1390c61e4cec | -3.64909 | -52.63689 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d907e6d-f03b-31ed-84c3-635881ae8579 | -4.56637 | -46.62566 | 2024-12-03 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf3cdc81-d2b5-3667-b791-7e91fb80d9d2 | -5.74097 | -44.43256 | 2024-12-03 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c56c79-3a19-30ad-be81-25c5baacbcda | -5.14205 | -43.23313 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9766924a-2d3b-33a3-b009-40bfa1d00e1d | -2.89777 | -51.79132 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c77b99b1-f438-3bef-9a77-1d91f769abb7 | -2.6005 | -46.20947 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9072da-65b5-35b0-a930-5ccc3b220ff3 | -6.03873 | -44.03712 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7149f1c6-b17c-3dc2-822e-16e42797d6e0 | -3.93873 | -46.92417 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d803341-491c-33f9-bb00-a8220a4e8c84 | -3.7962 | -48.90001 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 683c52e1-d616-3635-aa71-1bf87623fedd | -4.74777 | -46.20125 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39d78839-4e75-34ae-afcb-5add48b762fe | -4.16372 | -48.19199 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b51edad7-c2aa-3d9a-88e1-6596df7c06cb | -5.27652 | -45.45213 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8c3758b-3188-3450-8969-2c8a6bb0b794 | -3.93368 | -46.89163 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 397fcdff-b029-361f-a983-643676619924 | -3.20573 | -53.62461 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd9bc729-d60f-3e46-9bc6-fbae7efc8eaa | -3.31641 | -49.93056 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb6b613e-768a-34d5-b4e6-dcd1ab9eae77 | -1.72787 | -52.06372 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22eb89e8-299f-3689-965d-d67c854b1859 | -4.00134 | -48.29288 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
