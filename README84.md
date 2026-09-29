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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8883a9b0-7c92-3e81-b2cd-4f7860ecb7b6 | -11.8611 | -50.8999 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 994ce44d-bbc2-31bf-a5e5-e6a2a537b1eb | -11.9596 | -50.6751 | 2026-09-29 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fbaff8d3-65f6-38b1-9f40-4d0dce2cfcb9 | -11.1331 | -50.0409 | 2026-09-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b435331f-5d05-3b91-81a6-8dc0504c1306 | -12.0123 | -50.9678 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d2dacc81-f098-3d4c-97b9-5379810b8f7d | -18.0956 | -44.355 | 2026-09-29 15:00:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b7acd578-8a00-3fe4-9ea2-eefbd6e296e0 | -15.7547 | -46.0347 | 2026-09-29 15:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 427.6 |
| 31f0f586-ec5f-3f3c-9e24-15859d22dc52 | -10.6333 | -50.5864 | 2026-09-29 15:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 86f61213-52e0-3d19-a5f0-35b72480a354 | -11.0101 | -50.6958 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ba36f789-2e9b-3264-a468-114c302effd6 | -11.1517 | -50.0603 | 2026-09-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7baae863-a902-3139-b78b-9b4acb87b5e3 | -11.8678 | -50.4504 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b97092f0-b1c3-3a8f-89db-6c9f92202427 | -10.7913 | -48.7596 | 2026-09-29 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d5003321-e7eb-32fd-86bb-d981caa7561a | -20.8373 | -57.6891 | 2026-09-29 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 134.7 |
| 35927737-bd2b-3e9b-8cdf-3baa3b1d6482 | -15.3807 | -47.9068 | 2026-09-29 15:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1b9bcedd-cea7-39cd-af60-5df62182ed7d | -6.1412 | -52.9144 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 48422d42-d586-367e-b268-c38dbf7813a9 | -11.8805 | -50.8764 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a08ff475-c466-31e0-8726-af057157f16f | -10.3894 | -61.2502 | 2026-09-29 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 13eac94c-835e-32e7-bbe3-51db43115702 | -10.9722 | -50.6998 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 44e15682-0749-3bfb-90ea-630c2884783f | -12.155 | -50.352 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ae8b87b1-7d5b-3f69-9bf8-874b1e85fe75 | -15.3998 | -47.9261 | 2026-09-29 15:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 3327ba23-44e4-3637-af69-f72bde2cd59d | 1.4453 | -50.7863 | 2026-09-29 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6cea3812-7a38-325b-a4b7-96b7ae8088c6 | -14.3496 | -52.1264 | 2026-09-29 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 88189444-d0a5-3a5e-adb8-792a1190993d | -10.9154 | -50.7059 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c8adaa53-5514-3bf9-960c-34ec1fcafaa2 | -10.8964 | -50.7079 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1a8a04fd-8aaa-3d4a-9f5b-060e5911d5fb | -8.853 | -49.8843 | 2026-09-29 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| fea21bed-f749-3db9-9a28-959d85137102 | -12.2696 | -50.3381 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c033502f-f161-358e-94ae-4c2895294e6a | -11.9138 | -49.9289 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 206d604c-18cc-3872-9f85-ecc54cdecad6 | -12.1553 | -50.3305 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5afd7506-3020-33d1-b76d-99943505133d | -15.735 | -46.0384 | 2026-09-29 15:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 324.2 |
| 011e31da-785c-3644-9a13-2a07f40d21d4 | -12.1932 | -50.3474 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 04f7b910-a0a0-3d84-bda4-b0c1597417df | -11.9551 | -50.9743 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6660f525-1284-3187-a50c-e678ad928953 | -12.0662 | -46.4643 | 2026-09-29 15:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| fe52ca69-187a-307c-8e5e-ed5c7a155eb6 | -12.0365 | -50.6233 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ad931664-0f83-30e6-97ee-7534cf56c4cb | -6.1783 | -52.9124 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 5e6dd311-a4df-3d88-810c-4c168c0149dc | -9.0969 | -49.9049 | 2026-09-29 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 76cac879-d34b-3eda-bed3-f6a2df06e856 | -10.3895 | -61.231 | 2026-09-29 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| fca9e68c-22cb-39c0-8dab-370c6f6bcc98 | -7.4871 | -44.5521 | 2026-09-29 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d3d7a043-dc6f-328e-9af1-89dd183d16e6 | -10.8106 | -48.7355 | 2026-09-29 15:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f734cd58-05f2-3408-aa2b-c9d82da1db02 | -8.3617 | -45.4013 | 2026-09-29 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 4c694747-c3f6-38c0-8c47-c5f29128c4ad | -17.6585 | -46.5355 | 2026-09-29 15:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 231.9 |
| be45349a-c7f9-314d-9e4b-592044f7c30a | -11.8472 | -50.5598 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| fabbc810-9c0f-342a-ab0b-46a4a4fcd810 | -6.1598 | -52.9134 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| c510d230-ddd8-34c9-89f0-667fdcfa30c6 | -15.3802 | -47.9294 | 2026-09-29 15:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ac9f78fa-f4b2-3c3e-a6db-2227951bfeeb | -10.3707 | -61.2513 | 2026-09-29 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0fa9d635-05e5-38bc-9911-977265dccb0d | -7.15653 | -35.08145 | 2026-09-29 15:09:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 26f948e5-210a-3a08-9cda-696981eaa623 | -9.76362 | -36.99452 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 378080db-dee4-322f-968f-fa93b503c9d0 | -6.3685 | -35.16631 | 2026-09-29 15:09:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 5acdae11-68a8-38e7-b258-7b0af0aac08e | -6.97158 | -37.16904 | 2026-09-29 15:09:00 | NOAA-21 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d8bf4de7-1116-37b6-b2e0-75b49a577516 | -9.7628 | -36.98807 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 19.2 |
| b922e45b-f3d7-3aba-bfa6-84a39b0063ce | -9.75915 | -37.12954 | 2026-09-29 15:09:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f3aaec30-7ba8-3d35-80ed-4bfa81a1db5b | -9.76109 | -36.97454 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 17.9 |
| da44eac7-e94a-383e-a7f4-100dace8d25c | -7.1551 | -35.08206 | 2026-09-29 15:09:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 930aed00-b72f-3574-9ad9-766cc7318490 | -9.42725 | -37.77816 | 2026-09-29 15:09:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9bcfbcb5-e166-389f-be79-0a88dcb17157 | -7.15462 | -35.07836 | 2026-09-29 15:09:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 97d385cd-8a1e-3190-bd08-3a1c0e7d5e09 | -9.75701 | -36.9948 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 23.9 |
| b74740c6-04ff-3805-98ac-c5e0d39a7931 | -9.42651 | -37.77197 | 2026-09-29 15:09:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ad976718-d34f-3b13-af33-417462cf105c | -10.98951 | -37.20601 | 2026-09-29 15:09:00 | NOAA-21 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4687dbe7-4720-32ca-a4bf-cd0c549691d4 | -9.76195 | -36.98135 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 19.2 |
| c4ff1b78-ab46-3c8f-840c-275a443e521b | -9.42509 | -37.77334 | 2026-09-29 15:09:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 31866e93-b925-3712-ab4b-31774aa7452b | -9.76196 | -36.98434 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 4aea9454-bffe-3c94-b298-c78ba22a7fc9 | -6.92258 | -35.35402 | 2026-09-29 15:09:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d64fdb36-cb79-3052-9188-0210b0c98c82 | -8.72808 | -36.91303 | 2026-09-29 15:09:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 70d084c9-44e7-39e0-9090-d1458e60df9f | -9.76114 | -36.97747 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 6eff218c-9402-375d-9c0f-3c871adabe5c | -6.214 | -35.38895 | 2026-09-29 15:09:00 | NOAA-21 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9e02cb2e-33cd-3f44-b4ca-b1e42687a2ca | -6.36901 | -35.16999 | 2026-09-29 15:09:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 6bc9e068-3a7c-39bb-b787-af28df972bb5 | -9.75689 | -36.99749 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 877c5971-49b0-3365-b996-dad23a255717 | -7.73282 | -36.21953 | 2026-09-29 15:09:00 | NOAA-21 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| fd392d53-b4d5-3c35-a76e-fbbe5992de02 | -8.80955 | -37.34913 | 2026-09-29 15:09:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9f45d68d-02f3-3f2d-99f1-0cbfb88dfce5 | -9.75611 | -36.991 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 21.7 |
| ab52446a-87cf-3829-a2df-a8b417d0e554 | -9.75613 | -36.9879 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 19.2 |
| c07521c1-f992-3de1-bbe1-b2b24a89933c | -9.76275 | -36.99096 | 2026-09-29 15:09:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 21.7 |
| a4ff4364-2a2e-366d-bea3-eaa0e140148e | -7.16134 | -35.72018 | 2026-09-29 15:09:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 02027f46-1d2d-3ded-a9f6-49e12dbc40c8 | -9.94335 | -37.81155 | 2026-09-29 15:09:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 145b125f-fc11-302b-a1ed-63b77ff49421 | -10.5201 | -45.3554 | 2026-09-29 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 8d28a567-ac19-300f-a3d8-91bafa4bda95 | -1.2455 | -49.062 | 2026-09-29 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 3031ab6f-a6d3-3032-ad8f-80f78b4950eb | -11.1327 | -50.0624 | 2026-09-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 36cc3ad1-4ef3-3a78-aa39-3158df8da036 | -11.8611 | -50.8999 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 439e1328-0f32-3cd1-a03f-ca14c0e570f2 | -18.1151 | -44.3745 | 2026-09-29 15:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 655ce24f-f98e-3961-bbfe-5a77f17ba0ba | -18.0956 | -44.355 | 2026-09-29 15:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 30c2b5a5-23fa-3c4a-8859-2620966f9375 | -11.8989 | -50.9169 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 04a1e1ae-88b1-3105-aabb-ea1888476def | -11.8678 | -50.4504 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6ab5cde7-6890-3fa5-9a53-7d5fd6c28301 | -10.3894 | -61.2502 | 2026-09-29 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| fde90906-86b0-3ad9-9251-054899d03730 | -12.2911 | -50.1849 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ab096925-256f-3dce-8f0f-7b8686c3d251 | 1.8587 | -55.5648 | 2026-09-29 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8e2eeb52-7bbf-3324-9907-db9accaf7466 | -11.8799 | -50.9191 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1911407b-34d7-3ab6-b4da-637a0546c741 | -11.8421 | -50.9021 | 2026-09-29 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 396dde2c-9bfb-3f7b-b99e-9f8fb0df0486 | -12.7801 | -50.6619 | 2026-09-29 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 85389e54-c1c6-3954-9532-30e09586e361 | -12.0181 | -50.5827 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7e4691cf-8d96-3b2e-ae5b-19668e08778a | -9.0783 | -49.8853 | 2026-09-29 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 54558ec0-6590-3f0a-a9b2-0eacd4206b10 | -9.6864 | -58.1258 | 2026-09-29 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| aa006f77-c7dd-3f30-8f9e-bcd0a94e2ed9 | -12.1185 | -50.2489 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bc61e328-dd02-3767-b675-5c196ac6dc8e | -1.3008 | -49.0613 | 2026-09-29 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 5fea26cd-6d5d-3aa3-bb85-05ea894a2af7 | -12.1376 | -50.2466 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9b7b2a9d-78c7-3538-a056-0c735d9178fa | 1.8587 | -55.5846 | 2026-09-29 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7527c34f-9ab9-3a7b-a095-9e3cac028546 | -9.2048 | -45.8548 | 2026-09-29 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3d546add-2d45-344d-86b6-780ff9209a00 | -11.1517 | -50.0603 | 2026-09-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a4548a11-9c16-34d6-9489-208683e4848f | -11.9803 | -50.5657 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 39e01ce0-36a0-3fda-b648-0e4049acbed3 | -1.3193 | -49.061 | 2026-09-29 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 18e561d0-7a3f-3e33-a346-ba7f7c3f53e5 | -12.2723 | -50.1657 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 84613996-930e-310f-9a1a-ae0629ff31da | -12.0365 | -50.6233 | 2026-09-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f043ac9b-dfc3-3cd7-acc4-cf87a7a013b2 | -10.3895 | -61.231 | 2026-09-29 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |


[Clique aqui para ver as próximas entradas](README85.md)
