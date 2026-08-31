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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8a97417-3252-39d2-92e5-3f8994724845 | 1.55448 | -56.07035 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa83057b-42ed-3a8e-b4c8-dea541d0717c | 1.56021 | -56.06023 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f84887d3-1e29-38e0-bc07-09947c77a49f | 1.4962 | -55.77444 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 770652b6-7039-330f-b88c-2d8f4d5b6e32 | 3.23337 | -51.32626 | 2026-08-31 16:54:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cd6a48da-2a6d-31c3-b722-c0e8efffd047 | 1.55742 | -56.07816 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 25dfaa48-1dbb-3d8c-8093-1fec06ef06ae | 4.03107 | -60.49194 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c7f1ae72-16fe-35c5-89d9-7a39e6cc0533 | 2.04601 | -50.96285 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8a305473-ae8d-31ae-b28f-3bcae937ee73 | 2.23154 | -50.74959 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75a46901-7886-3bee-a64e-795239543f1f | 3.2278 | -60.14215 | 2026-08-31 16:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 91abe95f-6676-3f2f-ac3f-cb7c783f5b44 | 0.3141 | -60.44308 | 2026-08-31 16:54:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 36cfad53-3621-3f34-afb7-342889ec7070 | 1.55965 | -56.06382 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8814b9d1-b03c-34d3-812d-026228838991 | 1.5626 | -56.07158 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 53458ebc-b33f-3c81-9cd0-031faf0609df | 2.04323 | -50.95892 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e569ea96-e91b-3c5f-beed-83e3b1be7bbb | 3.92682 | -59.64896 | 2026-08-31 16:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 278e982e-bbe3-360e-9b4b-ee8ecce90830 | 1.55392 | -56.07394 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f177c20-ff8a-3a4e-91e8-9b3a111cf868 | 4.03052 | -60.49518 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bde2310d-23d0-3f4b-b00b-284a8e918ea8 | 2.33056 | -50.90211 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70577b46-176c-3248-a72e-92f10d3ab8bc | 2.0427 | -50.96236 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7086b95c-7a7d-3044-a7f2-5d75db73e5f3 | 2.04548 | -50.96629 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| c0d5d55c-c9d9-3285-ad1d-a9c2b1967ec8 | 2.19272 | -50.84923 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4373166d-142f-3c68-9d9d-97b0c36244e6 | 1.56371 | -56.06444 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5cdf3b31-ded9-38b2-a5be-a19aa12370bc | 4.00675 | -60.47775 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 061ee6ad-c6d7-3eb2-b48c-4cb5f1b64ea0 | 2.71917 | -51.04808 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b295017e-4727-31bb-8f3d-4bd94d4e52fe | 2.24145 | -50.75108 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc89326a-4d75-3070-92bf-93615cceb1d0 | 2.53778 | -50.94568 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d7541893-b68b-3d76-a714-3838d3d08c1f | 3.93134 | -59.65259 | 2026-08-31 16:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3cd3ea94-9389-3730-b211-d26400191250 | 2.19115 | -50.85954 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4db9d68a-226d-3d68-929f-970b7355fe76 | 4.21862 | -60.00327 | 2026-08-31 16:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d1b38b5-51f6-3ffe-b5a7-fa2f50a0e225 | 2.18758 | -50.85821 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4afdd55e-f67b-38c4-a133-19b734a627e1 | 1.52316 | -56.05825 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d22a9ee7-525c-30ab-bab4-55a11fbafd3c | 0.31351 | -60.44682 | 2026-08-31 16:54:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 464f53f8-f857-3dbd-8ac1-8bbdc3bb2476 | 4.03151 | -60.49186 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e88d37d-0339-300d-bad0-74220e71e003 | 4.06105 | -60.50687 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81096479-52dd-3451-b321-c0a76f42bfdf | 1.55854 | -56.07096 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4bcfbf3a-b09c-319e-9ecd-22a305aaf19b | 4.01202 | -60.47861 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1c35bb21-0f2a-342a-bb34-1352275fc311 | 2.04705 | -50.95599 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 11d6b12c-62af-3691-85e1-e9514d906eec | 4.01149 | -60.48187 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32e7756a-2f87-38c4-ab41-bc2cb1cab663 | 3.9223 | -59.6453 | 2026-08-31 16:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| deabb26c-1613-3051-a043-b908f31235ff | 4.2452 | -60.33762 | 2026-08-31 16:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 366930ae-388d-3558-9dd1-1c819659cbba | 2.42939 | -50.98804 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4866e2bc-2e49-3685-b3fe-0a223035831a | 2.74652 | -50.89047 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 151c66d1-3eb4-3da9-b8f4-8298e895cdc7 | 1.74443 | -50.91478 | 2026-08-31 16:54:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b745964-978e-395b-9701-ab0cd0cc10c2 | 4.6286 | -60.62462 | 2026-08-31 16:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c5b924ed-eaea-3e53-9b0e-a948fe8435e3 | 2.23815 | -50.75058 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 88bfd09e-b1fc-3c12-afe4-419062ec2e78 | 2.723 | -51.04514 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 01a139e9-59f6-32d9-be1b-062069345c7c | 2.1881 | -50.85477 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4f75850-fee0-3594-9307-0b2d6de17d2a | 4.03098 | -60.49513 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8aed066-aff2-3ba9-a102-69c2394bb1bc | 2.19167 | -50.8561 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 000b8ac4-cc06-346b-bb8e-e108af8fe546 | -10.8022 | -50.6752 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3409021b-4c60-3a38-98c4-83bfaad2ce34 | -8.2229 | -54.9412 | 2026-08-31 17:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 86c4d3da-ec9b-3b12-9363-c973d7f4d5f4 | -11.1726 | -51.2728 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 51b9646d-cca9-3c2c-a490-4f55cbaf4b90 | -11.1824 | -50.5706 | 2026-08-31 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c362f065-3825-3457-9404-8c989885924b | -10.4794 | -64.5012 | 2026-08-31 17:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 06c9cac1-b1f2-387f-b388-1a6e84867013 | -10.8614 | -50.4985 | 2026-08-31 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 875cc2a1-9dfa-3c3e-939d-2383fb7a5d45 | -9.4345 | -45.6477 | 2026-08-31 17:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 839f6943-aa01-3253-be82-b6a80762c13c | -9.1523 | -59.6384 | 2026-08-31 17:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e6faf5f6-5f67-3e2d-86e2-4da9da937fa2 | -10.8025 | -50.6539 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 91be1bf1-9a8b-3e70-a4ca-eb52d68af51d | -10.1531 | -45.7438 | 2026-08-31 17:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d8f9423d-e94d-356e-8395-be273ce391a6 | -3.4002 | -61.3465 | 2026-08-31 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 15f9de82-3492-376a-a1b8-2e2f331918ba | -7.9233 | -44.2789 | 2026-08-31 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 27c84652-1a8e-3ea8-9423-961ade3e33d3 | -10.1084 | -50.299 | 2026-08-31 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| b2722b5c-ff2b-3de0-a5b6-a6ceb6d9a8d6 | -10.7428 | -50.8727 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 36a67473-9daf-330c-b8e6-9bfbada3014f | -8.9873 | -65.4379 | 2026-08-31 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b53ce9e0-02a3-3ebf-bc29-9900a17cca44 | -9.4156 | -45.6499 | 2026-08-31 17:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 2eb439da-1db1-3a42-8cfd-1d8dcb7549bf | -10.7827 | -50.7198 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9edb97a1-67ec-3ed9-8230-d396f5214aee | -10.8043 | -50.5259 | 2026-08-31 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d81bdf39-8d8d-3cc8-954a-d85a52b06fc6 | -11.1913 | -51.292 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 46daee0b-aa99-3bfd-b490-41aee7629ecd | -10.7836 | -50.6559 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 04413140-3822-3329-a440-6d7fbe549486 | -5.9636 | -57.6704 | 2026-08-31 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8b00817f-5a5f-3638-9dfd-ddce7d264c67 | -10.844 | -45.3356 | 2026-08-31 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 4a56948c-09e8-3ce1-99f8-d347153f84a8 | -8.5555 | -66.9574 | 2026-08-31 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 967b7d0b-1222-395d-8445-e423e8c37027 | -10.8436 | -45.3586 | 2026-08-31 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 97a0bf0d-7231-35b5-8abf-cbbde2b49d7a | -10.5598 | -50.4236 | 2026-08-31 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8da3e6cf-40e6-3387-84d6-0a5b14ac53b7 | -7.2933 | -60.5905 | 2026-08-31 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 07c0eec4-610f-3e8f-af6f-54b4801b03e4 | -11.1995 | -55.1008 | 2026-08-31 17:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| acc77ad0-8c49-38ed-bf56-612e320154fc | -8.3717 | -62.716 | 2026-08-31 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 756ec4e3-a283-3d55-a250-8f3873066201 | -10.5793 | -50.3789 | 2026-08-31 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 1557de58-b78c-34bc-b299-b73d874903a9 | -9.4342 | -45.6704 | 2026-08-31 17:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 55ad514d-97e3-38ba-875a-1bb3d4f6c826 | -10.8215 | -50.6519 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| e1f285e4-26af-394e-a3c6-e7be47dde95d | -3.1998 | -61.161 | 2026-08-31 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3b88e1ef-0861-38b1-a4af-72caf35808b3 | -10.1528 | -45.7665 | 2026-08-31 17:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| dc7fceda-831b-38c7-894e-1c7ffae7d228 | -7.9425 | -44.2538 | 2026-08-31 17:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 5b4a929b-2f8c-3d10-8f92-ebd4fc415e76 | -10.7618 | -50.8707 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0677b486-fb1b-32f2-bebb-4be49f1134a8 | -3.1267 | -61.1811 | 2026-08-31 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 38e4da8b-bdf7-30a7-8bc5-91ebe2d7d6a5 | -7.9236 | -44.2558 | 2026-08-31 17:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 318.4 |
| 555ebded-baea-3de4-aa69-fa93e08b067f | -8.574 | -66.9569 | 2026-08-31 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 5ffe194e-47cc-3c3f-aa6b-e03eea4199ba | -6.1295 | -57.6637 | 2026-08-31 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| de1f01c7-4d5d-30ad-a784-d5094fcffbab | -9.12 | -61.6011 | 2026-08-31 17:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 10c71f00-098f-3f0f-af0e-34a0de487d1d | -10.7833 | -50.6772 | 2026-08-31 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bdfe4a14-7230-3100-b1f0-0b4f337fcd5b | -3.6399 | -60.5466 | 2026-08-31 17:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a569e907-c6d2-302e-a8d1-d6b1f82e7db6 | -3.4002 | -61.3276 | 2026-08-31 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 08ff5a0e-90e5-3945-a2a6-69522c5847ec | -10.5793 | -50.3789 | 2026-08-31 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 38a600c9-e763-3cbf-bcff-cd4807af5f4d | -9.1523 | -59.6384 | 2026-08-31 17:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| c1d54840-d2d1-316d-8f75-c51373c69900 | -10.1538 | -45.6982 | 2026-08-31 17:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 060b9e10-ed50-34ba-958d-3a6fcb997f8a | -13.4707 | -57.0574 | 2026-08-31 17:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| be741e32-2ef8-395b-877d-f102a2ff13c9 | -10.783 | -50.6985 | 2026-08-31 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 344f0fcb-a301-38f6-b968-17c98c58fd91 | -9.4342 | -45.6704 | 2026-08-31 17:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 7ee8ace3-6526-365a-baf2-675d9da2bf9f | -10.844 | -45.3356 | 2026-08-31 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 28991ec4-2010-3449-8568-add7cb347b29 | -8.3717 | -62.716 | 2026-08-31 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d6c5d7b8-fab3-3355-a970-d5eb792c279e | -10.4981 | -64.5005 | 2026-08-31 17:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |


[Clique aqui para ver as próximas entradas](README177.md)
