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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb8f8642-413d-31a9-9a7f-fdf526068bd3 | -10.82983 | -50.50769 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a20f485-0072-3b0d-8158-9ac43cb63d88 | -5.98582 | -57.68974 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| afa29e4e-0b6f-37ec-a172-a3f9494cedad | -11.23495 | -45.07873 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb751472-b818-3b08-afe6-074725d1150b | -12.25898 | -50.54237 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be6706f6-60b7-3c91-8ab9-2f09974f06c1 | -9.16617 | -49.98634 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2dcc328-133e-3aff-8c80-1808e1a30db6 | -11.03076 | -57.21202 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e615a473-2620-392f-b697-e36fb6b35747 | -5.9379 | -52.36724 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93941350-4bf9-3dc7-aa33-19b4bef95db6 | -10.82531 | -50.51458 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bc8696a-0650-3871-8a81-0a40e1a82d0d | -6.94261 | -58.9543 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97026cae-821c-3e88-8008-8c1e3ef496e8 | -10.81252 | -50.64492 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51db96ad-4623-36ec-91b7-d9ea004e0fef | -7.3022 | -49.53939 | 2026-08-29 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc2fa714-4a6d-34eb-a3d6-88bb981e842a | -11.70692 | -54.53679 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc38d2be-76fc-36f8-a62f-9501a3f83c33 | -12.75691 | -46.47457 | 2026-08-29 04:53:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8cecc5a-5b48-3ecc-8899-9442faa3fd38 | -10.4609 | -64.49641 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f1a01da3-38a2-3f7a-a42d-8e1fb4ae37b7 | -11.25707 | -45.05604 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57db77b7-6774-3a78-aee7-13dcd4c86c2c | -6.49239 | -49.90911 | 2026-08-29 04:53:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 540048b6-7f4b-34e3-8f50-3c3ab8328e0a | -9.42588 | -51.58145 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb8477ff-0cef-3943-919b-dea5a6a8941d | -6.41208 | -51.67302 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 034fac36-a3b2-3b12-9758-5e072c0b7999 | -15.57507 | -56.28972 | 2026-08-29 04:53:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e750e8df-22a3-33b3-a4d8-bf49f2bd5696 | -8.94766 | -62.41316 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d09260f-ac11-308f-a1d5-1cfbf49ac182 | -9.43311 | -51.68629 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a05649c2-c7ee-333a-b7c4-a3979cee49cd | -11.36725 | -45.14103 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dcd8a4d6-68a4-3e4d-ab27-9344de8c3f85 | -11.03688 | -57.2238 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e55dde8b-241d-37f2-914f-001573053890 | -12.7652 | -44.26786 | 2026-08-29 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47959052-eae6-38f9-8600-cb3ad6a52d62 | -10.47477 | -64.49384 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 23530bcf-8881-3dc0-9306-9c2b20cfaae7 | -11.70972 | -54.54119 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebc497f1-c971-3526-89c3-788d852d0271 | -11.62722 | -54.57496 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999f2488-2de6-3a17-8882-7202ddf063bb | -11.36466 | -45.1599 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2b11fbd3-e474-3f4f-818d-b214c21104e4 | -7.3472 | -55.16801 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ead5eaca-99c4-331b-b4f3-4d57e155fd1c | -11.68733 | -54.59715 | 2026-08-29 04:53:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 106b1f20-7c0c-3c74-b0cf-11b1471c13d9 | -11.02284 | -57.24662 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b5ddee4-2754-3bf6-a48b-7bd61b38c376 | -8.60573 | -54.8358 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91408751-f707-3c77-a823-f412e9cf706a | -8.62402 | -54.69208 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e60f9dc-4909-393c-9769-d0b9b04510a8 | -6.15523 | -57.7908 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a58bcea2-817f-3cb6-9012-a89719939d08 | -11.29142 | -54.03682 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7e6ffb7-1ca3-3b13-a18d-1a8a416493e3 | -12.43058 | -42.88821 | 2026-08-29 04:53:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24717d8e-16b7-3c72-9519-6d2004879cdd | -5.7684 | -57.56078 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6570dabf-ce60-39c0-b406-67cb1609b2d4 | -11.61564 | -46.72929 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 028986d7-2edd-3e36-8c2e-89bd73e016e3 | -11.72602 | -54.52832 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf87d117-ea48-3a9c-9fc0-6bfb853345f8 | -7.35965 | -55.17314 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23843b58-5fb1-3822-a34a-7f5f026da3e5 | -20.23868 | -47.36567 | 2026-08-29 04:53:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da6eb76a-f007-3e43-9a81-cc73c14d0faa | -12.22505 | -50.53739 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2542bd25-2a50-3ae4-9a1b-b16dba282406 | -10.50648 | -50.78926 | 2026-08-29 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e710ecf-4154-34ac-9632-52907abd0711 | -6.2733 | -53.13942 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ad0a28b-e40d-3f4f-9441-1ec783f20c8e | -6.76196 | -55.65454 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f1a6307c-d93d-3ece-b60b-9c590ac12899 | -8.94922 | -50.80785 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45bcca53-b333-39bc-87da-8e1c04d5bba2 | -11.20296 | -55.09448 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6329fec-0f52-3437-8812-5720da83df14 | -11.90772 | -55.89337 | 2026-08-29 04:53:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27de55b4-0bab-3dd3-8d75-05756262d46b | -9.16485 | -59.38521 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17fe8dbb-9d5d-312a-b0c5-1afd9e0526c4 | -11.02595 | -57.23905 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14fe8016-e8b6-396e-9693-37add9362059 | -11.19385 | -55.10534 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 381e1d2d-31ad-3539-b353-5709d12d5bc8 | -11.01273 | -51.39695 | 2026-08-29 04:53:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bc5f4c3-fe51-3c05-ac0a-116e3e6bf7e8 | -11.71164 | -54.52975 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c6b6b2d-d034-3b92-b186-ec636071d788 | -11.37791 | -45.13253 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ca2200a-c912-3d07-a82f-bd91fe37b412 | -11.49549 | -46.94371 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b1574df-1ba4-31cd-b555-39ebbc8fcfb4 | -6.577 | -56.5479 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21fd91b0-6321-3930-b677-72311de63461 | -11.70629 | -54.5406 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a07a34-03d5-398e-919a-cb0175b4c049 | -10.50703 | -50.78564 | 2026-08-29 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6945394-333d-30a5-bb8e-05d24bef384c | -6.76707 | -63.05124 | 2026-08-29 04:53:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033efb13-dcbc-36ac-b522-f0ab4a03a3f0 | -11.26366 | -54.03598 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9b874c8-c170-345f-bbcf-f053490f9af2 | -11.37728 | -45.13715 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13af7a2f-4f3d-3fd8-8489-e703583aed5b | -10.53624 | -50.77529 | 2026-08-29 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dea25778-c955-3cdd-babb-5239b1e22171 | -18.93543 | -52.59505 | 2026-08-29 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 095a764e-fd38-3d45-8f7b-97c340a9bf7d | -11.239 | -53.99009 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a87804f8-888b-3b65-807a-9f3538899c8d | -6.85464 | -59.44338 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7289567e-1787-3540-b3c3-029d5fce3981 | -11.27106 | -54.03338 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f298055-af00-3f98-a31e-d16807873291 | -11.71444 | -54.53415 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee97cb17-ecf2-381b-a8dc-308ff75aef5a | -6.18207 | -57.7555 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36ad288b-e313-3513-aeb4-da517343be56 | -10.38875 | -61.23654 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c837fc0f-dc0e-3f81-a239-e16cfdb88ef8 | -9.87238 | -65.02991 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c7ca347-666d-3027-835a-7008577b8b90 | -8.67372 | -49.54699 | 2026-08-29 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09594803-1018-3a03-b048-83a564164e26 | -9.18016 | -59.63101 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3abcde32-40b2-3acb-8006-55a4123f2510 | -6.76581 | -55.65519 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 59512905-972d-361c-bcf9-afb6bc6c2de9 | -6.40822 | -51.67596 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da8a8e78-b3d5-3fbf-89ad-618250dc66fb | -7.52915 | -61.37381 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57dd8d96-1eb9-36bb-a49b-946794a96b0c | -9.86815 | -65.03149 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2477a106-bcb3-3a65-9369-928112ae04b7 | -8.94999 | -62.40074 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24ad2b5d-454b-3f4d-b192-113d57440180 | -7.86078 | -56.68542 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3013b747-5f80-3c9f-9672-41262bd6927c | -10.89905 | -46.61321 | 2026-08-29 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fbe551f-d477-35e0-93a5-2a7061cefcdc | -9.46238 | -51.58762 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8ce6293-0c3c-3387-8ae4-e80c3c29d950 | -6.76726 | -55.67013 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49d73e46-ec63-3ad4-8f6d-a306b953264f | -5.98658 | -57.68536 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab3a7706-857c-355d-ae1e-e6b5492de2e4 | -9.22652 | -51.57504 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9e5a505-f23b-392e-a1f2-0a29d1aaed17 | -11.191 | -55.10069 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b992c6b4-4d7e-31da-9e92-9d6289d58f98 | -8.23845 | -54.96434 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4deba0a-f416-3f5d-83ed-8db3ffe53ffb | -11.24541 | -53.9987 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 910a6744-99ca-3cdb-b8a1-7130da5f8344 | -11.02789 | -49.68715 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bece4542-53be-3573-aed9-e7e0af5f10a1 | -17.59277 | -51.6127 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2a1d1c2-497d-3d13-a3b8-860c9c2d66ea | -6.17745 | -57.78221 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b2a3727-b4bf-354c-b106-4218444aa35f | -11.02678 | -57.21134 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9834e4b2-f316-34f0-931d-518901e94fd7 | -11.2661 | -54.02115 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32e14ebb-b66a-37a6-9b9b-18dfbd866531 | -17.24098 | -46.92265 | 2026-08-29 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6af4c5df-54b5-30b2-96af-a1fdc6b40731 | -7.94606 | -52.44893 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebf5b61e-7217-3212-b0d3-b7ac97ff1cf6 | -7.5004 | -55.30113 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 6d59e3c7-3394-363c-b8bf-818499a1f512 | -5.89428 | -57.75362 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4ce7c9b1-8c85-3011-a240-d19864806e16 | -10.86174 | -44.80592 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a4993c1-52a2-38a8-a991-0e8c47944546 | -9.15762 | -49.97409 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d098c870-911a-3987-8171-db708ea4d9a2 | -7.60537 | -47.28694 | 2026-08-29 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd50441c-c79f-33e7-a781-6b681ca59b1d | -8.94857 | -63.27711 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a663978-cde3-355b-a20c-9bcbbf002495 | -6.16044 | -57.78714 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README50.md)
