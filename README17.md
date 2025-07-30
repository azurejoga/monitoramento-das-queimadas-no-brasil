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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b8368fb-a3ba-3bd4-ab0a-e140a2e8133f | -6.5258 | -56.2121 | 2025-07-30 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 8deb237b-40de-3cac-8d39-fa970421bdc8 | -10.6172 | -45.2282 | 2025-07-30 04:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 8180145c-3fc2-33d5-990b-e56d5b16791d | -10.6169 | -45.2512 | 2025-07-30 04:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 39b00baf-e870-39e8-9879-edb7a3a24619 | -6.526 | -56.1923 | 2025-07-30 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a3728043-c890-37dc-8872-ef2818522f11 | -6.5074 | -56.213 | 2025-07-30 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 114cd317-1fd1-3c48-bfcc-c8179905f045 | -10.6169 | -45.2512 | 2025-07-30 04:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 2f3e8f55-e39d-3b99-bf49-a7b97bc2b091 | -6.526 | -56.1923 | 2025-07-30 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ab1fae4a-6e4f-333d-ac63-5ade726af404 | -10.6172 | -45.2282 | 2025-07-30 04:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| aaafaf21-3254-3e2b-bf4b-ccac2fb06480 | -2.44525 | -47.33087 | 2025-07-30 04:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faaa1209-3914-36b0-a580-acd778ab00c8 | -3.29289 | -42.6245 | 2025-07-30 04:25:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c2abbe4-4531-3c29-84a6-06db896ebbbf | -2.66375 | -47.40706 | 2025-07-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27ad238a-6fdc-327e-838d-1da0b314acd8 | -2.44585 | -47.32714 | 2025-07-30 04:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f48999-1655-3f9c-9660-881ea1715d41 | -1.94653 | -52.08086 | 2025-07-30 04:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2d98bc1-9436-3ff2-8c49-d734126eb85b | -3.42605 | -39.63057 | 2025-07-30 04:25:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8934f80e-3bbf-39e9-a462-88028b1c9dc7 | -1.50201 | -47.47136 | 2025-07-30 04:25:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e09b08b-aed5-37f4-8fe1-396bfd37183a | -1.95037 | -52.08629 | 2025-07-30 04:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97eacd3e-75c6-36dc-93cb-4fef465781c1 | -3.42545 | -39.63458 | 2025-07-30 04:25:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53e0c28d-02c9-3764-869c-d0a3f2043b73 | -1.95112 | -52.0816 | 2025-07-30 04:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6924e4a3-def7-30ce-a4a0-51adbf07a722 | -7.0677 | -44.9587 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c670aba8-769b-3225-9bbf-4346bac0ec02 | -10.62045 | -45.24366 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4b5513bc-9786-3f11-9b44-df1a73997f81 | -6.55217 | -56.19329 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51f2328-f403-38f3-9481-fd62e1c03589 | -8.63154 | -45.88296 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 919904ac-c315-36dc-8b5b-d86a3472d606 | -4.17129 | -48.57802 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 314c644b-f8b9-3956-ace9-c635632e1762 | -6.02109 | -47.56174 | 2025-07-30 04:27:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f00de60-74ee-3c85-abc9-da621af122d9 | -3.51362 | -43.25047 | 2025-07-30 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b489627-6bb2-3d91-a537-dc6aae19ba9f | -9.40287 | -45.49377 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18822796-e9be-3e16-8671-efcd3a82b15e | -4.89954 | -44.96027 | 2025-07-30 04:27:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9bc7d0e-4ab2-336e-acc2-6e228d74a7b6 | -3.99275 | -43.22659 | 2025-07-30 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc4167ec-912f-352d-ac69-162455ea7007 | -6.48941 | -56.013 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d76e81d0-e27e-384a-aab7-e835c6be6cd5 | -6.52706 | -56.18991 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07b755a0-14c2-3061-a254-7929f2cf7527 | -6.39492 | -53.36338 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c13f26dc-11b2-33df-8089-dc033e8d2678 | -6.46347 | -44.57763 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cd67df9-ce10-3ba4-90a0-9da7dc374085 | -8.62486 | -45.88192 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7f0ac990-dc58-3045-835a-a7b2c70d8269 | -6.89949 | -45.25532 | 2025-07-30 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39ab131b-8bc3-3bfd-9664-501e81bd1b87 | -6.3967 | -53.36534 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a8c1233-e9f9-31cf-b0d3-f2c6f508a3ca | -2.9014 | -48.24875 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8fecd399-6303-34b9-bbff-54b2b62a790a | -6.56612 | -56.18038 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca9f6ccf-46c8-3bb2-a216-6d949d67c428 | -7.14993 | -44.04306 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec04d699-7ba7-30a8-ad21-4eb49e349a7b | -6.90003 | -45.25179 | 2025-07-30 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f98e1df-3fb5-318d-b672-e7f46545bcaa | -8.31465 | -55.10725 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39f9ad4d-961a-37b8-b44d-bc686ccb2b46 | -6.5012 | -56.20479 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5521268e-11f3-33f3-96de-cb1d98e5b044 | -2.9056 | -48.24528 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b583b97-9866-3206-ae8c-5e77ff0bed38 | -6.56407 | -56.19167 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94e0f8aa-8288-3cc4-9ddc-93c4d50abb51 | -8.32605 | -54.75651 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f3e2899-faaa-3e32-a94b-bf32110ed796 | -9.40005 | -45.48964 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd14e2a-9231-3045-a8fe-96b17c28f970 | -10.50711 | -43.94593 | 2025-07-30 04:27:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cec75e5-36df-3400-bc24-e9ebf5d10c56 | -7.94298 | -44.09031 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42bab31a-4c88-3484-b005-a8e8d20fab72 | -6.56072 | -56.19636 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dbfd848-6455-3a59-8642-7d02a3283591 | -6.70663 | -44.3341 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d33b994-cd0f-3e9e-945e-74223052f8d5 | -3.82338 | -41.57348 | 2025-07-30 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 19a337d3-7f85-364b-8ca6-be4f800304d3 | -10.52474 | -42.55214 | 2025-07-30 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 77c0c74f-c0c4-3f35-ac95-1b6659797e3f | -3.03492 | -47.86108 | 2025-07-30 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b778f12d-4311-392c-b8ea-1978500e1b5a | -9.62637 | -48.54512 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54b8aee1-c487-32a2-8115-94c66d8b85b5 | -3.29992 | -49.19183 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5e94b2a-29f0-3110-9db0-b9c80418ae74 | -6.40808 | -53.3707 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd4ae75e-b645-3275-98ed-7356f2066d62 | -3.99215 | -43.23048 | 2025-07-30 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e99b02ac-e81d-3ba9-aa5b-4e27937e9242 | -3.66473 | -51.23862 | 2025-07-30 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 335fea7c-58f3-3708-95a8-95ef14a6b1a7 | -7.12165 | -44.47187 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 097412f2-934e-38ec-a4ec-2e4e86ec0c88 | -8.32482 | -54.76144 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5740c10c-0cfe-3053-a72e-cd5533b11348 | -10.40968 | -47.25385 | 2025-07-30 04:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 767f6d88-9d11-395f-b53a-866975098dd2 | -8.52112 | -43.31172 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 56a56b84-f5dc-3bea-9e85-adc5c8cf3b27 | -7.13937 | -44.3558 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3494c6ae-45d5-3045-ba50-f838a5590d76 | -8.95844 | -46.7348 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78ef4e0f-a7da-371c-90a1-eabb792844b3 | -6.53268 | -56.1909 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e70de7b-3bf2-32d5-b9f6-357c7d0ca867 | -9.74004 | -48.5785 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e99dced-6c82-3254-b7df-a32b0fe042d1 | -5.40291 | -43.24556 | 2025-07-30 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 56fb38e9-ab46-32c6-8748-c14b08773a72 | -6.40341 | -53.36993 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de4895c4-d898-37a5-bc7f-43fb223646d9 | -8.02191 | -47.68158 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e98b0f95-c73d-3479-b716-f657d34abf49 | -6.39574 | -53.35851 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf13f79d-4862-3b16-acf7-263559ad3ea3 | -6.54589 | -56.19592 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19aebc49-37eb-3822-a989-d03c5aa47a59 | -6.38044 | -53.33562 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f3e3a85-404f-3efb-b846-1b6dce53471a | -9.04862 | -45.0764 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf5045a8-3efd-3e01-8456-112ee8527502 | -7.85491 | -46.7367 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9739395a-57d2-33c8-8cc0-d66587e3e929 | -4.58857 | -47.98117 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fbe0d33-87f2-39c0-a64e-5b6f61b3f118 | -6.55983 | -56.1831 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b86f0f4c-18e3-3524-92e5-424b8b8e3f30 | -7.22352 | -43.10401 | 2025-07-30 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21d5207d-5a19-3de6-bb88-158a394f7a1a | -7.36566 | -43.76505 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a591e36-ff6c-3269-bf68-a2656357d0b5 | -9.94093 | -47.98399 | 2025-07-30 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a33dcfcc-5ca3-3dad-ab0e-8b733d98cb2e | -8.30904 | -55.10931 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7af60993-827f-3877-8560-4678974e83bc | -7.94417 | -44.08241 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b24f74e2-5930-33d9-ae5a-e65f3de5558b | -6.52284 | -43.3344 | 2025-07-30 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61a8cf3e-83aa-363d-b957-16c632b84bf1 | -3.1814 | -48.80937 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eba33af8-b536-3257-87e2-6191b4e83fd8 | -7.60771 | -45.05206 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6048044a-471c-3fb1-918c-935d8b98b962 | -6.52304 | -56.21271 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03bd9622-0b5e-3423-b91e-9fffca414c14 | -8.88377 | -47.33508 | 2025-07-30 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7212cff0-9b77-35a7-ae12-c3fd311f3c9c | -6.99063 | -41.62263 | 2025-07-30 04:27:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb90d4b5-3839-3f03-9237-c4bb34299bc7 | -8.62376 | -45.88901 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f445ffef-244a-3fad-beda-80e7cdf47439 | -4.78079 | -43.37655 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7c86e6b-62ee-331a-a4b1-978672575900 | -6.40515 | -53.37186 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97ac1730-39e6-36ef-b998-7ef1849be3ba | -7.15424 | -44.04682 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2460bb5-7e31-3e55-b3cb-214ece988528 | -5.39875 | -43.24902 | 2025-07-30 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdad6e4a-0ec2-3cd7-8e83-d93c9de8daa2 | -7.08304 | -44.49717 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 881ee93f-2343-32e7-9bb5-60d25a701fe2 | -9.26193 | -50.2291 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fcb187a-05cb-3cfe-aaf3-477b52cbdb36 | -6.88987 | -44.73162 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21873252-f877-3ace-91d6-207927c51d0b | -9.75051 | -37.0021 | 2025-07-30 04:27:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 293b02b5-ee9b-3994-b639-ca65d04b4754 | -7.13764 | -44.36712 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cba27c65-0412-351d-a19f-59060c664950 | -7.0542 | -44.95643 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14cde98a-4c9f-3837-b15f-73746424858c | -9.17433 | -48.85 | 2025-07-30 04:27:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a7a9d48-6b57-3fb8-99ca-6dcd4c606dd2 | -6.02167 | -47.55813 | 2025-07-30 04:27:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6301d502-7c54-390e-8594-9d68dab0fa20 | -6.41705 | -53.35869 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README18.md)
