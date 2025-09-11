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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4b1f888-c251-3287-8ee9-82aeec98a211 | -13.241 | -51.7571 | 2025-09-11 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c8d9a177-0269-333f-a720-8dd17fcc7334 | -12.6825 | -45.2977 | 2025-09-11 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8aae0837-00f2-33b1-aa63-bb96f286bcee | -12.6632 | -45.3008 | 2025-09-11 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 1f409231-d406-3347-97f3-8d84b417244e | -8.5667 | -45.5842 | 2025-09-11 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c4727c44-dde4-3256-b073-05d77cf84bda | -14.5128 | -53.9158 | 2025-09-11 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 55dfcae7-9f80-3a56-9796-a0dc4b906657 | -14.1492 | -45.4009 | 2025-09-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c8c4f739-5c2f-3d58-a708-c8198fa65931 | -8.3302 | -44.9032 | 2025-09-11 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d2a1ea26-32b0-3cd1-8a13-0299e7914770 | -9.1331 | -46.9831 | 2025-09-11 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 0a230871-09bb-3457-bd73-9316cd8e18ee | -19.2617 | -47.999 | 2025-09-11 12:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| cc49e22f-1814-3dfc-b71a-025f8de6841b | -11.1693 | -45.2683 | 2025-09-11 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 10ed2d7d-8748-3e5e-9e57-e26cfb6d98ab | -22.6809 | -53.1309 | 2025-09-11 12:50:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| 32a636cb-9931-30e0-a2db-379fa7184b21 | -9.4804 | -46.4321 | 2025-09-11 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 401161be-ff72-3f76-b647-655a41191f98 | -15.1016 | -50.1468 | 2025-09-11 12:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 9c2ae6fe-12a0-3325-b86d-bd89d8a13fb9 | -10.0695 | -50.3881 | 2025-09-11 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 72692759-4973-331a-94d7-9ee8e009750e | -22.9828 | -49.7336 | 2025-09-11 12:50:00 | GOES-19 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.7 |
| 8b1edc0a-1d79-3c0b-90ef-73bb3be134e0 | -8.7411 | -45.2248 | 2025-09-11 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.5 |
| c5ed4f7b-520e-383c-9919-00f17d2e8d81 | -8.8753 | -49.5828 | 2025-09-11 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0980b611-3731-34dd-aec6-7441bae8553e | -11.1689 | -45.2914 | 2025-09-11 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| b7e55355-62b3-3cbe-a904-ed8227a7caaf | -19.2611 | -48.0221 | 2025-09-11 12:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a549cc9f-a628-342c-987e-8c998bd98ec1 | -15.6737 | -47.016 | 2025-09-11 12:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 9307b18f-f104-3e13-bdcf-ae20f0c58af7 | -11.4093 | -43.5573 | 2025-09-11 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 2817c62f-a9cf-3ecc-a18b-49816ed62043 | -15.1561 | -52.4439 | 2025-09-11 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e94d18e2-8e0a-36af-a1ef-0adedd38a277 | -11.3584 | -46.5167 | 2025-09-11 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| cc638526-ff68-35fe-98b0-bb0ac8ca8365 | -15.1049 | -48.0434 | 2025-09-11 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fe791258-7fc2-3688-8bc4-83f49c9e7aad | -11.7211 | -46.5127 | 2025-09-11 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 7aa761ab-f6a2-33bb-bee0-b5d30bdb5a57 | -12.6628 | -45.3239 | 2025-09-11 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 916901f7-bfa1-32a4-a0d2-b769080d0d59 | -8.8755 | -49.5613 | 2025-09-11 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| f1cf49b3-2cd0-3d44-8a99-152de6907358 | -13.2798 | -51.7312 | 2025-09-11 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 60a24cf0-7773-3276-9fcd-946f7fa6533d | -9.0942 | -47.076 | 2025-09-11 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d88742de-bef4-38b5-9cfe-c278c1ce4ed0 | -6.2226 | -43.3459 | 2025-09-11 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 70c01ce2-73b6-3903-9fa5-3c876c97c3da | -15.8006 | -52.2687 | 2025-09-11 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 21250b62-805f-3636-bd10-4e228c41b3de | -15.1367 | -52.4466 | 2025-09-11 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2046cbce-faf6-3768-80a8-557ef8fdc71f | -9.0547 | -45.7809 | 2025-09-11 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f80a6ad4-ef65-33d2-97d1-c7461487c83b | -9.0939 | -47.0983 | 2025-09-11 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e24e75e4-a061-342e-990f-8fb913e375f3 | -11.779 | -46.4821 | 2025-09-11 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 35468bb8-2c5a-34ec-b5e2-7bc4c491aaf7 | -9.1328 | -47.0054 | 2025-09-11 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 337e64a0-263f-3dac-a1e8-415437e5deb0 | -12.547 | -45.342 | 2025-09-11 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 71bf2a8a-ea5a-3b3f-af94-c47cb7eda0b5 | -13.5089 | -51.7877 | 2025-09-11 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 863b1dfc-a027-36b6-8349-8017289eee89 | -6.4364 | -44.4847 | 2025-09-11 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e3347fd7-8f09-37b4-80b5-dfb53ccc6924 | -6.8525 | -47.8707 | 2025-09-11 13:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e1cecef8-df5c-3e8f-bb2a-f1b22793790e | -12.547 | -45.342 | 2025-09-11 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8c0b7e04-af94-3d9d-ae3c-c37788e99710 | -11.7786 | -46.5047 | 2025-09-11 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| c02e3fa8-5112-38a8-945e-b7f04ac60a43 | -12.5561 | -49.1535 | 2025-09-11 13:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3590b3c0-5154-32d1-83db-3547ea6b7128 | -6.0784 | -44.6961 | 2025-09-11 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 50832f9b-d745-3ba3-8234-b2264d059640 | -10.5671 | -47.2442 | 2025-09-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 186d0ad7-3e99-39f8-8521-c70fb5e0fdc7 | -16.6335 | -49.7683 | 2025-09-11 13:00:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 54e635a6-214f-313d-9987-0cfb7c80809a | -12.6829 | -45.2746 | 2025-09-11 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7c23e424-d9f5-37be-b4e8-80c142f36d78 | -15.1016 | -50.1468 | 2025-09-11 13:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 3ea9b070-4f71-3fcf-aee3-7db874b08959 | -9.0579 | -46.9688 | 2025-09-11 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5d8adee1-d7b2-31ee-a133-27fa7ba111e2 | -9.0756 | -47.0558 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 58cb370b-09ea-3239-84f5-614e93a465f6 | -7.5028 | -48.2769 | 2025-09-11 13:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 95595af9-79f5-301a-9c53-b6a266ddc61b | -8.8753 | -49.5828 | 2025-09-11 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7d1b70f4-b2f6-3d5e-8547-51a887e445e0 | -10.5674 | -47.2219 | 2025-09-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 06b3b5fc-990e-3573-ae5c-ca313902c490 | -11.7403 | -46.51 | 2025-09-11 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b33fedf7-3bc5-3201-83e0-3ecf4672654b | -9.0939 | -47.0983 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| fda5cad8-d548-3b13-8f2a-372159a7b582 | -15.1049 | -48.0434 | 2025-09-11 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f0580208-ea71-3a78-9e74-3520b8e210bf | -9.8343 | -46.8173 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| c5a74295-2d5c-300d-8628-36062f71562d | -11.7399 | -46.5326 | 2025-09-11 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 8ed39968-52c9-3f63-9a0d-33277aa45d07 | -11.4285 | -43.5544 | 2025-09-11 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| d1065905-ad75-33dd-a651-380da0268027 | -7.8708 | -45.5181 | 2025-09-11 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| cc5dd843-7c09-32fe-96b4-edcc32d5ffc1 | -11.779 | -46.4821 | 2025-09-11 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 43c61ca1-48e3-3035-a53b-311c3ef62430 | -14.1492 | -45.4009 | 2025-09-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 463e1628-3c2b-38ff-be9c-a5b7c9876118 | -11.9898 | -47.5748 | 2025-09-11 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f05e6962-193d-3f2d-9482-184f1cadfe10 | -16.633 | -49.7905 | 2025-09-11 13:00:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 853d5401-510d-370d-b8cd-b33a596edcdc | -6.2228 | -43.3226 | 2025-09-11 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| e5960669-7df4-3c1d-806e-c9fc0a245c12 | -11.3393 | -46.5193 | 2025-09-11 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| ee34267a-4a38-32c0-a1e8-bb1f8960285d | -6.4364 | -44.4847 | 2025-09-11 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 8c7d25d2-99df-3f35-92df-8cc094846978 | -7.852 | -45.5199 | 2025-09-11 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 34aca7d0-acd3-3c24-b3f2-48c979170d2b | -8.7411 | -45.2248 | 2025-09-11 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 93c67508-c22d-30e2-b8ca-00bf065a1d24 | -9.4801 | -46.4545 | 2025-09-11 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 0dcd84dc-cab5-3bd2-a27d-6bf97a5004f5 | -9.0358 | -45.783 | 2025-09-11 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7a2a13af-ed37-3dad-9d35-656c1dcdc794 | -9.0942 | -47.076 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5ef9635a-5147-3931-a23c-aecdeb3fddb8 | -11.4093 | -43.5573 | 2025-09-11 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| bd3fd6af-eb55-38eb-9d4c-4de128e0dc25 | -8.7547 | -47.1107 | 2025-09-11 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 152c3e41-f936-36bc-bdbb-14c003a9cbf2 | -13.2798 | -51.7312 | 2025-09-11 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| d08b8acc-c6b8-3e46-8042-f4758ed5b0d7 | -6.2226 | -43.3459 | 2025-09-11 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5d91bf8e-eabf-3942-9eb6-a681a103a1df | -15.6737 | -47.016 | 2025-09-11 13:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3f26dbef-4997-32c0-b90f-6c3a9cd092f8 | -9.8157 | -46.7971 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| da60346f-10c5-3d2f-9524-4d43ec911239 | -8.8755 | -49.5613 | 2025-09-11 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 72271ea5-212b-395d-b88e-7af546d57df2 | -12.6628 | -45.3239 | 2025-09-11 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| dd13af56-3a94-3a33-bb89-e779758cbb58 | -8.1649 | -46.0983 | 2025-09-11 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| cb0b754c-77ef-3930-bea8-c28f28d7c239 | -15.1759 | -52.4199 | 2025-09-11 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8fbc94cc-3eb1-3e2d-9699-f965bd15ffce | -8.5667 | -45.5842 | 2025-09-11 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 48e4dfd8-8d1e-352d-ab3d-178bbcfa5eb0 | -10.7366 | -46.1011 | 2025-09-11 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 64907397-df18-3968-84cc-c54cd86a51d8 | -15.6732 | -47.0389 | 2025-09-11 13:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 196.2 |
| d55d0519-22d6-3da8-88f0-08bb31da614d | -15.8006 | -52.2687 | 2025-09-11 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1d9c8cfd-b649-358a-b67c-d4040d511674 | -9.075 | -47.1002 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4d195cda-c17a-3b36-a6e3-f26dcf6b96f2 | -9.0753 | -47.078 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 7dc25ad2-54c8-333e-afbe-77782f0c19ba | -9.0567 | -47.0577 | 2025-09-11 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| cc922c16-9fc5-37c3-b369-3d8ba808ea05 | -9.1331 | -46.9831 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9a4c8bf5-cf14-3190-803e-b2f8f8a23bda | -9.8154 | -46.8195 | 2025-09-11 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 150dddef-8af3-35a2-84ac-3100ec9e359e | -13.2602 | -51.7548 | 2025-09-11 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 6be4283d-3750-3d3b-9f7a-16e8c3430a13 | -9.4804 | -46.4321 | 2025-09-11 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 60cfb170-1afb-39e9-abda-c2f0e3901710 | -11.3584 | -46.5167 | 2025-09-11 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 3751f2ce-6fa2-34b3-b668-4fe1b38bc493 | -11.4281 | -43.578 | 2025-09-11 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f4764ce5-28bd-3d49-b0ff-44191456a335 | -11.7211 | -46.5127 | 2025-09-11 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 479.0 |
| 7e56e4ba-8d0c-3c60-80b4-cf4301e538d3 | -9.0265 | -49.5046 | 2025-09-11 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0e6d4317-2fa8-3cfa-8863-4052284f986d | -11.1 | -48.4172 | 2025-09-11 13:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ed1b7dd9-19fc-3656-84ff-9c9849aef6bb | -9.0358 | -45.783 | 2025-09-11 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 762102ea-9d5d-3681-9eff-9904f91b8321 | -9.7634 | -47.8447 | 2025-09-11 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |


[Clique aqui para ver as próximas entradas](README140.md)
