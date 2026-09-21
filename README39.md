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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65df006e-5ce8-3931-b1d2-f36e7fd66ad3 | -9.46391 | -45.41006 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 395fab7b-ec1f-39eb-a934-2f29ae4dc52e | -9.47123 | -45.40753 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b171f657-c64c-3da3-875d-570e01d922d1 | -9.45815 | -45.42412 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 848b812d-ca5c-39da-8088-6b04c839224b | -5.76262 | -47.28495 | 2026-09-21 04:19:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4b2a5d-a763-3a08-aa68-6b9dfd288963 | -6.77026 | -55.49867 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a058011a-30fc-32bc-b4c3-8e80fa60a4d8 | -5.83582 | -53.47919 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f449df-15f4-3e1f-8870-6e8ae2c465e0 | -5.83012 | -53.51123 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 553c9004-223a-3774-b7a3-6ec329be7d1b | -9.45994 | -45.41318 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8091e8b4-39d5-35e3-88e6-e7bd7f2d1d85 | -6.90975 | -43.73457 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| effa0b57-ff70-33dc-acaf-32159e33dc92 | -7.09921 | -42.07703 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2957411c-ad07-30ae-b76c-0f977bce4d70 | -9.44884 | -45.39642 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 5d3f2d7f-14ca-34b7-94a7-a00e8995878e | -5.81698 | -47.79007 | 2026-09-21 04:19:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e33d5d0e-b538-38c4-9129-d878656fea9b | -4.34589 | -55.50184 | 2026-09-21 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc73ff3b-70cd-30da-924f-fce6452a6eaf | -5.82941 | -53.51524 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e240271-57ab-379a-9ede-c2c955c975dc | -6.91987 | -42.94087 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7dfe8e76-939e-3535-8c40-b0a990d37198 | -6.91637 | -43.73563 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 923ce71b-d4ca-381c-b1a1-fce7e05475d1 | -6.99096 | -42.20655 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86e695f4-3bdc-3bfd-88de-41c0572fbc65 | -7.09584 | -42.0765 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28f7d651-cabd-34a3-87c5-3fa8b0cc8318 | -8.78351 | -48.75021 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a34e56f1-8b1b-3042-a27e-d834ea6479e4 | -7.31201 | -44.19493 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f699428a-bf71-354c-b2c4-c10a82fbdab2 | -6.91388 | -44.90319 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 590d8904-701a-3b51-9640-80aa9f69b1a1 | -9.44369 | -45.40676 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a304b9e-6f40-3209-a59b-f00e0e601ca7 | -8.77618 | -48.74516 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53b4c62c-6ead-3520-9d3d-9590ac3bccc1 | -7.44479 | -44.74494 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f52ea2c-545e-3c9a-903d-db73589d432c | -9.03422 | -48.15869 | 2026-09-21 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5cc76d0-1f7f-309b-9924-b5ca0ea14757 | -6.90438 | -42.9313 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 93d05fe3-0aa7-3421-ba0a-07c368f1da25 | -2.61549 | -51.72993 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0920b349-c29e-3b8f-9b16-60f2f9b5696f | -6.77223 | -55.63321 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c9bfc35-0cbb-35da-aa71-b61403ef4648 | -4.58704 | -45.16016 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd0116d7-e247-3d36-8f73-24d8ac81e974 | -8.79426 | -48.71201 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39e2a1f8-d47d-37b6-a828-ce9fa7bb08d0 | -8.75866 | -44.28446 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43a617ec-bfa3-3561-8e4b-a913de5ce980 | -5.2056 | -56.11141 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 536cd797-202c-3f46-acb2-65a06b7b49f3 | -6.88392 | -41.70624 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 630d2ad0-e753-3a44-8d9d-86206e45deb0 | -7.4357 | -44.78006 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c5d693f-906e-3169-a04a-aaae50ba1f95 | -5.21151 | -56.07943 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63e18790-6a40-3023-a161-3438880c631f | -5.83736 | -53.53728 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 389d049b-577b-3151-b2c2-788024458319 | -9.44706 | -45.40734 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73c09b68-ed3e-3f92-8832-e7e575bf2c3b | -6.8366 | -46.04128 | 2026-09-21 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb74e4eb-393c-349a-96e6-39a03011dd1a | -6.20846 | -53.56325 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90ad68c3-8359-3f6a-9823-e0c119d10efb | -7.58693 | -43.42733 | 2026-09-21 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a414e0f2-5c40-325c-9068-60426c0cac19 | -8.77359 | -44.27613 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bec6c0b-a6f4-3c4f-b20f-6511d94ff9b2 | -9.45954 | -45.39444 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 1811c36a-75c3-3cbc-b738-9149d0382a1a | -9.53138 | -45.39903 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81bbee48-c0a2-3b5c-a11f-e8d27e8295ed | -8.65612 | -45.4325 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f7b85c8-616b-3899-84c8-2f0aefa814b0 | -6.82932 | -55.5381 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 641b8349-4543-3266-a57e-95451ad5986b | -5.8344 | -53.4872 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dbcd285-5776-3e42-8693-d91a55be6f77 | -9.45934 | -45.41682 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da239dd9-c6a5-3e0b-9519-a753653f63d1 | -7.43627 | -44.7765 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ffe88b7-0240-36c6-a517-bff86fa02e22 | -6.91748 | -43.7287 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caba5ba3-63c6-3345-ad61-afbd0e49504e | -1.48058 | -49.01616 | 2026-09-21 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7c14a2c-9563-3d1f-a900-d8a6e471d51e | -7.98115 | -47.45088 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a959a2fe-10b7-3701-909a-14b5b7fd8abe | -9.46113 | -45.40588 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bd156d4-1b89-30ec-9580-ea23a7037129 | -7.44028 | -44.75155 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8b6bb52-3bf7-3201-97af-396fa80ced1f | -4.40465 | -55.24203 | 2026-09-21 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| def1ed89-e24c-37bb-ab76-8c27c9211be1 | -8.77746 | -44.27318 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 626b2008-98a8-3e58-925b-5018c8e4c13d | -7.76052 | -44.83216 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f024b22-7086-3309-9253-695901f1337e | -9.4645 | -45.40643 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b35ce2e-bbfa-3164-9e32-9fdf881c9ffe | -5.84747 | -53.5473 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9c13dbd-ab7e-333f-9bb0-34b19e4e02e2 | -2.45284 | -49.22138 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d827ef5-6201-324d-bdce-ddc1886a4377 | -5.82296 | -53.51813 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7219a724-b49a-30e4-b642-0eefa5096d63 | -4.68188 | -46.39523 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a0e6846-30f2-33b9-82c0-7cc4ef0eeb4c | -9.45141 | -45.423 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9cab526-dd6f-366d-9559-418e366eb338 | -7.44986 | -44.73476 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 066ee089-aef5-346b-8ddd-da3ed38acc4d | -7.67906 | -44.66172 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5943e314-7535-3464-8b52-ffc39d45d634 | -6.66479 | -50.88801 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c76bb0fc-93c7-3156-848a-6f41f8801d90 | -8.78178 | -48.73658 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08eadb47-2ba1-3317-94ea-e5cc1ad27ee5 | -6.38732 | -42.80691 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f46b789e-a684-35da-9805-a5c8bf26b56b | -7.42639 | -44.73104 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc0e51cc-353e-3a68-9e20-611882a9ee4a | -8.38983 | -37.64793 | 2026-09-21 04:19:00 | NOAA-20 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 69a0fbe6-b274-3260-b379-15c33ed2e274 | -9.4746 | -45.40808 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 037ff9dc-9aa0-37c0-ae3c-7681379665c2 | -3.34025 | -42.76397 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a29bd0a-bb74-3b60-8cdf-15a0adf42ff2 | -6.58252 | -42.55935 | 2026-09-21 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 07b4196c-6c59-3cae-ad3b-2a679cc50c17 | -7.32659 | -55.60843 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9610b7c-1b7a-3f9d-aa65-0c8cbb1898a8 | -2.25921 | -48.75437 | 2026-09-21 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71021a00-a0d2-3390-99ad-72abbddece84 | -3.87554 | -40.75489 | 2026-09-21 04:19:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c067b486-db8e-3631-8bb3-c010063c70c6 | -6.41758 | -55.01506 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fcd9c74-bcef-3a12-8869-ea8f0b537586 | -5.85327 | -49.78838 | 2026-09-21 04:19:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1e6bd74-3683-34d2-8107-9d08e40da055 | -5.83511 | -53.48319 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e96a5ee-4cc2-3969-afaa-45cf10501f64 | -9.02098 | -49.82554 | 2026-09-21 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e30fe002-c8f1-354d-beab-7b6fea55eddd | -7.55577 | -44.9463 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a522a957-acdf-3652-8248-10f136adda46 | -4.68046 | -46.40402 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 716561b6-4d7d-368a-9075-78c83d7de603 | -4.40796 | -47.85107 | 2026-09-21 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ee84cbd-aae1-3f25-ba08-83bb9c41351a | -6.56642 | -45.53823 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2a04269-bcef-37ed-882b-74abbc622c73 | -6.20967 | -53.56325 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89f4a390-c0b2-36c3-8803-2cf8e82e18f5 | -8.76367 | -44.25312 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4557e6a0-be09-3fca-9c63-5fa0981270f9 | -9.47005 | -45.41479 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f62b82a6-1e05-3b9e-9c91-a761c984ef84 | -5.3644 | -46.22821 | 2026-09-21 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676bab56-86da-37c1-9bec-c0745746b079 | -8.38263 | -45.62718 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be74951c-5e53-31d2-a73c-0cf2b71ba9c0 | -8.36456 | -44.81292 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3553656-f098-3db2-8249-6bd2af43ee32 | -7.33098 | -55.61224 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da24ea2f-bfe7-3a12-84c0-42846e386940 | -3.64202 | -40.58983 | 2026-09-21 04:19:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e97a3853-50c3-398d-bd78-45b85640f757 | -5.828 | -53.52314 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8ca46cb-1bf3-3e7a-8a99-ef5c58aafbdc | -6.39654 | -39.48573 | 2026-09-21 04:19:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93fd768e-a723-3b24-b5e7-418ae029b22e | -3.74212 | -40.30088 | 2026-09-21 04:19:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e11e06ac-af2a-370c-9e6a-ea2e490c379d | -9.46291 | -45.39499 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| ac66191f-2a4e-3056-aa76-fb1b1c60613f | -5.27849 | -49.34186 | 2026-09-21 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7a08455b-4ef3-33e1-84c5-66d8f235cee4 | -3.64374 | -40.57881 | 2026-09-21 04:19:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4bdca68a-9ab4-3b72-9dfa-78b39e2fce70 | -9.45617 | -45.3939 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| faaa3996-6352-349b-aa66-c2d74bb1b91a | -5.87319 | -52.04597 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8613c40d-8cab-3dd5-8ce5-68cb85d3c7e9 | -5.83667 | -53.54118 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
