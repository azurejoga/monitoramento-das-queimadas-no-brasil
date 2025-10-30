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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed57ed39-f287-3f66-ba30-ccbe6152e4c7 | -13.27484 | -47.71766 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07454924-5930-3ec1-82df-a2af1e87d000 | -12.75181 | -43.44773 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f84d1200-702a-3fb0-ab10-8c21af40d185 | -13.85268 | -48.49632 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d15fedf4-4bf9-3138-b6af-13d0e3ed3cc6 | -14.28706 | -42.3358 | 2025-10-30 03:38:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0a7ebea8-e0f1-32c4-b94f-3f0cc39e6b68 | -18.57919 | -43.08327 | 2025-10-30 03:38:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4fef81e3-2b94-314a-b79b-429ad3783614 | -12.85773 | -48.62085 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9452251d-6d55-3594-b171-df30e2e9aecb | -13.47843 | -47.9992 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b489c292-b377-3431-9268-a15a791403a9 | -13.32594 | -47.47746 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f066ec51-d1c7-39a3-879a-5853f86add20 | -13.19719 | -44.48568 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd2d097a-c168-3275-9a69-63498090c204 | -13.37307 | -47.38001 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cfb04d6-0b5c-3169-bd08-8ab796def46f | -15.14395 | -41.58882 | 2025-10-30 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eec51167-991b-33b7-89c2-d7abdd1b2ef4 | -13.4374 | -47.36853 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d41c6330-74f5-32ff-9d44-fd2a4c9cee4e | -12.39432 | -46.82793 | 2025-10-30 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb7f4061-c9b3-3812-8535-85e3712fe935 | -19.064 | -41.12703 | 2025-10-30 03:38:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b196b946-7e8e-3754-9efa-9ddfaf66549a | -13.03342 | -47.02995 | 2025-10-30 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b29ff85-b11c-3b3e-8c76-80b72524d7ae | -12.6647 | -47.34944 | 2025-10-30 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46fe5acf-df7c-3c78-b262-db06b5ecda11 | -13.85597 | -48.49447 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b290eed6-263a-39ed-9ae1-5393f96c7c1f | -13.41294 | -43.74817 | 2025-10-30 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c11bf057-24da-391a-85c0-a9c9042fd496 | -14.97459 | -43.38435 | 2025-10-30 03:38:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 806c8858-b091-32c9-a767-da0aa983e584 | -18.35165 | -42.24639 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d227a31a-331d-3d7b-80f4-818b0997d92d | -14.97939 | -43.3853 | 2025-10-30 03:38:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd714643-aa93-3306-95e0-7221fd1d9718 | -16.59313 | -43.51258 | 2025-10-30 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 867f7618-da7b-3b3a-a66d-8834742c00ee | -4.2544 | -43.7149 | 2025-10-30 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 344.9 |
| e83a451a-8c01-3566-a380-bcf5f0e82a8b | -8.3313 | -47.9219 | 2025-10-30 03:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 397f53a7-1409-3687-8e7c-5228af65e76d | -12.4755 | -50.5922 | 2025-10-30 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 47bba1d0-4adb-3d51-8f70-2482c7b6262e | -4.2545 | -43.6918 | 2025-10-30 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b0b5b7eb-f0a1-3846-a548-8a490a57942e | -4.2732 | -43.6908 | 2025-10-30 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5e16b952-c828-3153-85ce-1dfe0d799acb | -12.4759 | -50.5707 | 2025-10-30 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a5822a09-7a92-3da9-8269-6b77a64adeba | -12.5141 | -50.566 | 2025-10-30 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e90a7473-3ac8-31cb-8eae-ff894b438229 | -12.495 | -50.5684 | 2025-10-30 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4d0edc8a-a1b5-371a-b2d8-44ad60da6f01 | -4.2731 | -43.7139 | 2025-10-30 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 9762196c-e6b6-3fad-bf11-42286dbcd8e9 | -3.7867 | -43.9011 | 2025-10-30 03:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b6de11b7-1657-3288-a90a-d2f1d668558f | -12.3088 | -50.2688 | 2025-10-30 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| abd5fe07-43a7-3b04-9c56-0774d6d7bbf8 | -12.4947 | -50.5898 | 2025-10-30 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1ab637ea-c2ef-3bed-aba0-b37144f7f376 | -21.55763 | -44.99501 | 2025-10-30 03:40:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0ed215a9-d89e-3ff4-b8c5-f5bc8c53d600 | -20.40261 | -41.52839 | 2025-10-30 03:40:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a4e3982e-1453-3922-a8d8-72a95f4382f1 | -20.88439 | -43.68272 | 2025-10-30 03:40:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ab24dd31-9151-39bc-b230-1a3fd2db89ea | -20.47461 | -40.79507 | 2025-10-30 03:40:00 | NOAA-21 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1667073b-be05-3ef2-abd5-c5fca556ad3b | -20.78002 | -43.4077 | 2025-10-30 03:40:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6402a37b-a682-3120-a59b-78709c1c9d32 | -12.4759 | -50.5707 | 2025-10-30 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 500479c9-3715-35f5-83f6-e753b21fe650 | -4.2545 | -43.6918 | 2025-10-30 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 1016f93c-ee68-3ef2-8415-d5aa54b46efd | -4.2731 | -43.7139 | 2025-10-30 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| d27649e1-5ee5-3254-bef9-5fb89f894308 | -4.2732 | -43.6908 | 2025-10-30 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0352c401-3563-3b8a-b9ce-c458ceab1c18 | -12.4947 | -50.5898 | 2025-10-30 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 260b3057-e202-342a-8608-472f73a2fa9a | -12.4755 | -50.5922 | 2025-10-30 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 45916d5c-788d-3db3-9183-59f951e22fef | -8.3311 | -47.9438 | 2025-10-30 03:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 93d719c7-b5ff-3646-b0ce-cfa7d86464dd | -3.8054 | -43.9002 | 2025-10-30 03:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 99229651-75d3-3ef7-8c41-1d93246d49d4 | -8.3313 | -47.9219 | 2025-10-30 03:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e1baf3d6-c1f2-3d4f-a291-9b8a65b13585 | -12.3088 | -50.2688 | 2025-10-30 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0d939278-69de-3087-b508-9a35b21f7d9a | -12.5141 | -50.566 | 2025-10-30 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 15530c04-dea0-382a-a3b4-001c1fee6e32 | -12.495 | -50.5684 | 2025-10-30 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| adff65c9-2330-3561-89e7-52dce0285f02 | -4.2542 | -43.7381 | 2025-10-30 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a669d418-fdfd-388f-a118-206510622da5 | -3.7867 | -43.9011 | 2025-10-30 03:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| ccd9710d-6e05-37a2-b12b-690c0d3a8d42 | -4.2544 | -43.7149 | 2025-10-30 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 425.8 |
| e86c7bd7-4487-323e-9d0e-2a43756c3688 | -5.4372 | -45.3323 | 2025-10-30 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2b440531-56f1-3973-a36a-0e9a849793b9 | -12.495 | -50.5684 | 2025-10-30 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 94fcbf78-eb09-3f79-bc00-f43fd2e10c53 | -4.2544 | -43.7149 | 2025-10-30 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 356.7 |
| 0cfee0c4-3aea-3edd-b867-3a18f4aa86ea | -12.4759 | -50.5707 | 2025-10-30 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| adbfa5fe-a9de-371e-b221-3ce44ec0cf05 | -4.2545 | -43.6918 | 2025-10-30 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 89c0a0a8-2cc8-39d4-a8d3-83f00fbb9be7 | -3.8054 | -43.9002 | 2025-10-30 04:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0ac3910a-e180-33d5-bc94-19f978cc1e3e | -5.4372 | -45.3323 | 2025-10-30 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5af2dd3d-4bcf-3606-8eb6-49d0438de889 | -12.5141 | -50.566 | 2025-10-30 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 8e7ef317-029c-34be-84c2-4902962e6fbf | -13.3361 | -54.32 | 2025-10-30 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9c9614b2-397b-3d93-b4ab-eef300654d66 | -4.2731 | -43.7139 | 2025-10-30 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| b127bb6d-c871-31b5-ba26-7701ad127193 | -4.2732 | -43.6908 | 2025-10-30 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| c6e7336f-a56d-3687-87d7-90d448a35466 | -8.3313 | -47.9219 | 2025-10-30 04:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4d733fda-df05-3eec-80d2-04af05037fdc | -3.7867 | -43.9011 | 2025-10-30 04:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6fa31f69-3b7d-31c2-b081-e58dfe2b34b5 | -6.14443 | -41.68588 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9865b6ae-338b-3ebd-b559-89b8cf52d034 | -6.71123 | -38.20587 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 896bbed2-979b-3ec0-bb20-7da4e5c5348d | -6.11114 | -41.71841 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f8a4956e-d26b-31fe-aaef-d4031969e963 | -6.1485 | -41.85396 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eea54287-f467-35d8-9adb-2fa5915a7967 | -5.57637 | -42.17028 | 2025-10-30 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f2fdd8d-4222-3988-bb41-3d7b3fc2678b | -8.49801 | -40.95431 | 2025-10-30 04:04:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19137ac1-97d8-3e52-a753-efb9c60afc1c | -6.70826 | -43.44375 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bbabf74-5f52-3ccb-9f8d-8641d36f6904 | -5.79264 | -40.81006 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4aa3772-2ae7-3c7d-a29f-85438b20f047 | -8.30943 | -40.30881 | 2025-10-30 04:04:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b7bcbe4-d14c-3e10-acab-b0a8c220fd26 | -5.53346 | -41.70444 | 2025-10-30 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 358d8e9e-a6b0-3936-b12c-44702666c914 | -6.18011 | -42.3871 | 2025-10-30 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d86f8c8-f4ab-3b96-9b56-1880a3034c43 | -7.50885 | -44.07446 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eff43195-5e25-37b4-b1e9-a6f45392e7bd | -3.79486 | -43.89571 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d872c6dc-0aa7-3320-a1bc-38c65723aed0 | -6.50548 | -42.23479 | 2025-10-30 04:04:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afbe2eb3-8380-3321-a188-ba5890ef9b22 | -4.87012 | -45.80169 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a3b9d68-aed4-3c7a-a076-6318f1b1e362 | -6.19021 | -41.57617 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5c0b79f-658b-3dc2-97bb-7820a90d6c74 | -7.78953 | -46.41383 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71ae7121-8edf-3cd3-ba0b-4d582c23d6f9 | -7.60991 | -43.5663 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70d40390-2023-3007-8cee-01bfbc476726 | -6.71066 | -38.20957 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8322c09-021e-3869-a385-23807052f5f0 | -5.0413 | -44.88249 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9516efd4-0af3-351d-b68c-3e250d75288b | -6.23305 | -42.52787 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b79cb646-3053-32ef-88ed-607f7280ec4c | -6.16506 | -41.66619 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5aa27c5a-17e2-39e3-b7bc-4f847219b508 | -5.6061 | -47.122 | 2025-10-30 04:04:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2872c105-fd68-3b5e-8c98-00b93a82ef45 | -5.45403 | -40.87638 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1b163a4-df3d-3b2f-b201-e56ae8645f12 | -6.21351 | -41.8225 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e1d8c93-4d73-312c-a9de-1ba5bd595d0e | -5.51072 | -46.23532 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 516586a6-4025-3069-ac79-b27e8d60ec13 | -4.26513 | -43.71293 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 795a953c-c09c-370b-bc73-100655142c41 | -6.01295 | -41.97546 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 042769fb-89ac-3083-a05e-d23bec62c8c4 | -5.65906 | -41.09871 | 2025-10-30 04:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eeddcaa1-1d3b-3188-be03-c22bf4ed561d | -7.78882 | -46.41792 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0e261cf7-9d2e-36fd-bf22-819ef78e0d6c | -4.76008 | -46.85115 | 2025-10-30 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e539648-58b5-3b5a-a6cd-d2f96536ba81 | -8.40805 | -39.95971 | 2025-10-30 04:04:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4c46f0b-f9cd-3006-9c10-94e109984496 | -7.59458 | -43.56823 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README20.md)
