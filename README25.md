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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f393d16-3a77-3d64-9a69-7ed850721d65 | -14.38313 | -50.33043 | 2025-06-28 04:51:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6e20f14-0ec5-37e1-a0c8-327dc569f188 | -11.19494 | -55.92625 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 040fb7e8-7fb5-3b26-a0b2-48c281c61b40 | -10.82183 | -53.73742 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c13c1d8-cb8b-34f4-9a00-0878cff54c94 | -12.65628 | -54.10313 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fb83359-7c61-3724-848c-4670001f84b3 | -11.60476 | -55.54511 | 2025-06-28 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 130b11f6-d49e-32b9-9013-18b82967216e | -12.25636 | -46.76082 | 2025-06-28 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b496fa95-7ccf-3dbe-acf4-24c57df86ebd | -11.57777 | -52.10635 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5028f9b9-5a81-3b73-8925-794f6314181e | -10.56435 | -52.05061 | 2025-06-28 04:51:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2466637d-2908-3054-9f51-676de2e3f39c | -11.57721 | -52.11007 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62122f91-165c-34a7-9230-a735874170c8 | -8.8421 | -49.85325 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58c60088-e072-3796-807e-7f404e23f74f | -12.65573 | -54.10666 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce284001-4064-3102-bb2a-021b2479c09d | -10.83395 | -53.74654 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 699113bb-a7ef-3379-9f58-2a12c10af07e | -11.57381 | -52.10953 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5729bad-c49d-3d98-869a-565d6b353943 | -11.04606 | -55.37388 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 1279b609-380c-362a-8062-1b1d58d321a5 | -9.43511 | -63.46075 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81148208-9c98-3eac-821e-0e333fdbcfc9 | -9.11561 | -49.49554 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 57b72726-87a8-3ef0-b7ea-edab621f0243 | -11.43924 | -54.47097 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb5c7f22-a158-3663-9791-96ad354737b5 | -8.56461 | -51.57078 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72de79dd-bb1a-34c7-9afb-7e4e6fcbcbb0 | -11.06239 | -55.38041 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1711a13-1329-360f-a374-365bda88f5e2 | -10.82899 | -53.75649 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0b29e8f-6d81-31e3-a34e-3c93142012db | -9.11255 | -49.49042 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18bf2e48-e252-3c8d-ad1f-a151db205f89 | -10.28524 | -57.0151 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8211be79-6ded-3372-bde1-a5fffaca872e | -7.89175 | -61.46635 | 2025-06-28 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96819b10-71e0-3b90-aa89-ff5fd05d7e0f | -9.60519 | -63.46933 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdd3203b-f353-398a-b0c7-e8b0a4a39671 | -15.55305 | -55.24504 | 2025-06-28 04:51:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64d0d693-b0fb-38c1-9d6f-695103eb9c67 | -11.58079 | -52.1143 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a51a3ef0-f4c6-395c-980e-40e7b9d3d1ab | -11.05562 | -55.37929 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 274de9ce-b26c-38ff-be72-3bb97bf79584 | -9.11695 | -49.48647 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 352a4c4c-38e7-39b6-a67e-b8a82cb260a6 | -11.27401 | -52.75211 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42b3e80b-e4f7-3c03-9333-1b0d49de9af0 | -12.13499 | -54.66888 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a08e3c1-841f-33ea-8b9a-fae53a46fc7e | -10.86977 | -53.77741 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2555e2d8-64dd-3620-9f24-192ecbf4e0de | -14.5347 | -53.83741 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b3716de-38b2-30f3-bc18-f96e88737e02 | -12.10843 | -54.66449 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c8e5539-047b-3e95-9bf6-9f41abaeabbe | -12.59741 | -57.87576 | 2025-06-28 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 235b2b82-901a-3f75-861f-819cbcbde979 | -10.8312 | -53.74251 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02d6ccc1-901e-308c-9224-d92babb2003c | -10.82387 | -54.02463 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42c51cac-7c25-35c4-a947-e570efe35d66 | -10.50612 | -53.58604 | 2025-06-28 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8f1a754-7919-3fc1-bd5c-3d2820ec1fad | -9.11389 | -49.48136 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| be4c3295-64ae-3f4a-8c35-26764dc5deb2 | -14.89378 | -48.40134 | 2025-06-28 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 780798eb-bf54-3517-a956-580b137824ab | -10.83065 | -53.746 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbb9c8b3-bd4c-31ea-812a-e0873dcd5495 | -12.25572 | -46.76576 | 2025-06-28 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| aac15601-de2f-3116-9378-02b14844cbf7 | -12.11094 | -54.58497 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e14713e-a4b6-3cc5-8c73-d82958aab9dd | -11.27067 | -52.75159 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2dafb2b7-a665-3939-902c-78da344f3762 | -9.92643 | -59.93611 | 2025-06-28 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78ea64c0-7e6a-35ff-ba99-bb0e73fb3858 | -13.29485 | -57.08961 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1836b76f-d6e0-3710-933f-a03eea5a7408 | -10.2948 | -57.13716 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e063af-8b82-379d-86fa-ee7e60173b3a | -11.88246 | -58.73829 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00a0cb0d-c279-3711-ba9b-518bc073ebe5 | -13.94411 | -43.23954 | 2025-06-28 04:51:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7f0f2506-24bf-3c79-a898-40068bfa450d | -10.8323 | -53.75702 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 501d60d0-f01b-3a2d-bc8d-3b704f470984 | -11.27012 | -52.75516 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 17298e49-23c7-3a66-b2d1-ee7ae0eb352b | -9.18837 | -49.65949 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa44b5dd-8634-39c7-9299-2129a5a67ce6 | -10.82954 | -53.75299 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d7462e8-60af-3291-8ba0-3b9cc7417b5c | -9.7915 | -56.13184 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d09463f0-4cb6-34e4-8f6c-dc114544800e | -10.16363 | -53.92462 | 2025-06-28 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf30c961-14fa-3597-ad48-f666049bb72f | -10.82128 | -53.74091 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b8c82fd-29ef-35f1-b513-b7f225ba547e | -9.3595 | -58.85028 | 2025-06-28 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9452c7d2-4def-3def-b2f3-fdc6e0ce8d2c | -11.44086 | -54.48209 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bbf4e26-e4e5-3eab-a92e-8e9922958eb1 | -11.05342 | -55.37136 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 793eeae5-883e-34c7-b5c1-051b053751b4 | -9.43997 | -63.46575 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49af2d51-d0ed-3f06-a869-d24013282fd3 | -10.84608 | -53.75566 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9546eed3-0506-3f87-a1d8-8c31fd86a0d6 | -11.14153 | -53.92891 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c606e7f-e2f8-395b-9a5a-01fb0dc9d01f | -12.10762 | -54.58442 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca675bac-f049-3125-97fa-897786153b99 | -9.35254 | -58.84125 | 2025-06-28 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae1afd6c-8e35-36f9-a585-38da87d97310 | -10.82073 | -53.7444 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b9a9e8d-9ff5-3ead-a4fd-cb97b96c4dea | -8.56405 | -51.57443 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69bc463f-a0a3-364b-901a-2251459ebee1 | -11.44312 | -54.46799 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d88e40c-8321-3fbb-a911-2ecf914cd25f | -11.26733 | -52.75106 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| d8d540cf-8340-32b8-bbfa-b931f77ca5f6 | -10.81698 | -57.74764 | 2025-06-28 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 55404f64-80ef-3235-891e-73ba965e6538 | -9.44357 | -47.95771 | 2025-06-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a57b17e5-34cf-3c46-95ec-e82ad0a53be5 | -11.18523 | -55.92072 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d583c88-f70f-3350-a2f6-1d893c60aad1 | -12.10705 | -54.58796 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18afa879-4cf9-3f66-b3e9-e121d143a1dc | -11.1915 | -55.92569 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a05a456f-7482-336b-b3c9-3a21b450e337 | -13.30048 | -47.51667 | 2025-06-28 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d57e7a45-9785-3850-ab6b-f328a868d4c5 | -14.88945 | -48.40079 | 2025-06-28 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9cf2a41-b906-32d4-a987-1c0559add21e | -11.44256 | -54.47151 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 470f3baf-a3dd-3bb7-81fb-36dbd599825a | -12.11369 | -54.58905 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89b105dc-7c49-306c-bce8-5e95013b9d33 | -12.10649 | -54.5915 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ff17a7a-5f08-357a-96aa-3ce9f865878f | -11.05586 | -56.74593 | 2025-06-28 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42c63bd5-a260-36ed-b585-7c64c63d85e2 | -10.82403 | -53.74493 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b151f4a-7761-363b-afa0-c49ffa2579f0 | -11.04965 | -55.07417 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31ba2805-e871-3e19-afad-914cec1789cc | -10.83616 | -53.75406 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff189529-368e-32d0-b302-b43239988fa0 | -14.53802 | -53.83797 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5aff5b66-1210-38ae-939e-e4b9302f0f5d | -9.08592 | -59.49677 | 2025-06-28 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d8227e7-c589-346a-8db2-a807594da01d | -9.87157 | -48.4514 | 2025-06-28 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b033c41-aeea-3574-885e-47910e422c64 | -11.03809 | -55.38013 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8d38ecc4-a0b4-3223-b57a-4d5bcf67a8ab | -11.57968 | -52.12171 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb5c1fdd-32b0-3057-96f0-ff9a7fd216f6 | -8.85695 | -50.16015 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da1a4097-cea9-3764-99b0-39c5184b8a5e | -8.56349 | -51.57809 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdff728c-ed5b-36c3-8d46-c0660c0379a6 | -9.82734 | -48.37972 | 2025-06-28 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f38a5541-e348-31a8-8a72-69edd96fa5d1 | -10.0321 | -54.32488 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9134e917-5a04-30c6-ba5f-9c16de21dd1e | -10.83175 | -53.76051 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5e4a752-74da-3ab6-ad61-3046c9f21e56 | -13.64811 | -46.81274 | 2025-06-28 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00559b42-fe97-3402-9afe-af2a35b294d5 | -11.4403 | -54.48562 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d11c79a-b7b7-3bda-85a2-df1561ea2b10 | -9.71798 | -56.18225 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 605f3082-62db-3967-8a8f-8e3ce2895711 | -12.10786 | -54.66804 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b746dc9b-3a4b-3f71-878f-2e8381d29e65 | -9.87207 | -48.4479 | 2025-06-28 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97f26553-bcd6-332b-a905-bb1e8401af57 | -10.8345 | -53.76455 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5839538-11f9-3b6a-91a4-b12eec87a0af | -11.19212 | -55.92188 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 987799ec-8462-3543-bcb6-faed247840f8 | -11.58004 | -52.11431 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb7eeb7a-ce9e-351f-96d9-d5a302783919 | -11.01384 | -45.24178 | 2025-06-28 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README26.md)
