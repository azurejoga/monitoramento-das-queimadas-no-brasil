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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97d0c4be-a648-3006-8047-0297390c6f7d | -14.68212 | -59.84265 | 2025-09-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caee67f4-2784-3a0b-b99e-4d3365cfcdd2 | -15.25051 | -56.83781 | 2025-09-30 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 83ac0375-8b9f-3ab4-a088-6d153040dddc | -15.71395 | -59.51487 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2030a7a-2ab7-33f7-aeca-d6f93291755f | -17.90478 | -57.59514 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e3970db4-0614-3f5a-84a6-164f9ad5668a | -15.72107 | -59.52114 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6aab473-e89e-3f2f-92e2-dd6d683b764c | -17.75116 | -51.34488 | 2025-09-30 05:31:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c74e16-5c65-395e-a2dc-6fb850744ecb | -15.79738 | -59.5188 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60707fec-1d92-39c9-8da6-16a863a94317 | -15.70288 | -59.47867 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8f612de-9c0f-3cde-bd1c-14ffae0fb89b | -17.75798 | -51.34514 | 2025-09-30 05:31:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd8d2615-1042-3b00-9279-121c17ddebbc | -17.91928 | -57.59043 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a35abd6d-3028-34c9-81fc-684c1d9dfb49 | -15.91538 | -59.50151 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35b2b6bc-aeed-3eeb-a267-2ef1452edc99 | -17.92393 | -57.59037 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b8eb1ed7-04e6-31c8-a177-84b94bcf50d5 | -15.71851 | -59.51065 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f49566c-f1c8-3ac4-9130-02642f367c84 | -17.91816 | -57.59957 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bc1d79d8-f051-35a0-af83-35bfa97528d7 | -15.89413 | -57.49541 | 2025-09-30 05:31:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62911e53-b178-34e6-a34c-4a4e7f67148c | -15.84636 | -59.59805 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6023251-32b6-3088-b280-f474657d6965 | -17.91059 | -57.58554 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 14ee816f-1d73-304e-b477-dfe004cbaee5 | -15.80453 | -59.52498 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6094e50a-a0ff-3f8e-8278-c3160d16d4cc | -22.08994 | -55.97355 | 2025-09-30 05:31:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 171b436b-378e-343d-90ab-b385e0b76b5e | -18.32856 | -57.10566 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2210b7e5-4eb1-334b-8127-78b07c72ed06 | -17.91461 | -57.59057 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cfd01f6f-ad79-3376-ada1-51b729797c0f | -16.00588 | -59.5118 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 896446d3-e495-3556-a264-f00df39351ca | -17.88229 | -57.62781 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0d24a154-d63e-3fa5-9a3d-d0bd7d330760 | -17.90998 | -57.59052 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| adab6579-8999-3f51-8a7e-e2099a23a320 | -15.86632 | -59.3357 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f12b5e89-b7aa-3986-8cea-8a7f06b8b6b7 | -15.89466 | -57.49124 | 2025-09-30 05:31:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c905b9bc-a073-3487-8235-e12831ac0fe9 | -17.90598 | -57.58525 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 341dfd0c-141a-3e30-8657-4a69cb645bf1 | -15.71532 | -59.50479 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5941425-5e40-3298-a630-2e152d3c0850 | -22.09026 | -55.97026 | 2025-09-30 05:31:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0466763-7e86-3629-ad40-5322a0e458c0 | -17.88689 | -57.62805 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bd52c3eb-1a75-3846-8524-e3fd40495d3a | -15.72174 | -59.51625 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 063fa038-64bc-33ba-bcfb-c17c6d2ac683 | -15.71921 | -59.50552 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 412b5cc5-0291-301c-9cb8-966b57ff1fb3 | -15.71718 | -59.52045 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3e3d3c2-b48e-3398-8b10-7ae0c0a82d02 | -15.80915 | -59.52035 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1fcb5d7-841e-3639-aee6-3912c78f48ac | -17.89457 | -57.60283 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bb7d4dbc-e981-356d-a92f-1d57d9fe9879 | -15.8052 | -59.52008 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 360c77b2-856a-3dc7-8b8c-3baf81300523 | -15.80062 | -59.52438 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 033de816-0d2c-3776-9f6d-7b746c9a049c | -15.84176 | -59.60254 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbaec54c-a639-3ab4-9876-5be155243cd1 | -17.92283 | -57.59929 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ca3ea73c-5db2-3591-be20-b9e225e43af4 | -17.90021 | -57.59458 | 2025-09-30 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f694c9b8-f817-3eba-ac84-0d0857f35235 | -15.72311 | -59.50623 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68056e4e-fadd-3a97-815a-eb28b52a08ac | -15.71784 | -59.51559 | 2025-09-30 05:31:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7db0e009-380c-34e4-99a2-f6aaeada1fb3 | -3.0841 | -47.0149 | 2025-09-30 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d92887f7-7e33-3be5-a463-f89ea8ca2e1d | -5.84682 | -50.06559 | 2025-09-30 06:14:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f649994c-e996-3664-8d86-8976ac93f1c3 | -6.08686 | -42.65681 | 2025-09-30 06:14:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 41.2 |
| f14cbe55-fbf9-3dc6-ab4a-9bf577b3fa88 | -5.02935 | -43.60493 | 2025-09-30 06:14:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| be3c5e9b-af97-380e-8bbe-bb912d3fc4b2 | -5.51763 | -43.88568 | 2025-09-30 06:14:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 47070a20-f6f6-3706-89c0-4b71dfd7b83e | -5.32438 | -43.71663 | 2025-09-30 06:14:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f7b131db-aa11-3e40-bd09-2596c33d012c | -3.49769 | -52.46475 | 2025-09-30 06:14:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9b98cf51-227b-3a61-94b3-f8ae1b245e5e | -5.52086 | -43.86308 | 2025-09-30 06:14:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 6bc6cd00-640c-37b2-a35f-b87d951931d2 | -3.09417 | -47.01642 | 2025-09-30 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| af771a43-1dc1-3fd8-9a74-b125010648c0 | -5.51441 | -43.86963 | 2025-09-30 06:14:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 18b64f46-cbd6-3e6e-8705-74b44d5727c7 | -7.81747 | -46.99356 | 2025-09-30 06:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f6460ce1-738c-3ff2-b153-df56eaef2d4b | -3.0959 | -47.00467 | 2025-09-30 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 0fac0cc7-4bef-37d8-aab0-b04d16b0e98a | -1.28008 | -54.17398 | 2025-09-30 06:14:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| af917f19-6779-37b8-bfda-3060dca07261 | -5.32844 | -43.73324 | 2025-09-30 06:14:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| bd326e44-b084-3fc7-8cf2-b4a0b8e63da4 | -7.05154 | -45.1925 | 2025-09-30 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| dcd47e2d-6524-34d3-8e0d-d7bf3022b6e1 | -3.27361 | -50.03323 | 2025-09-30 06:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 836b974e-2e54-3f8c-8c32-35fcbe4cae45 | -5.2356 | -43.73824 | 2025-09-30 06:14:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 265be8d9-fbf4-3848-b150-7e37ae347462 | -6.83734 | -44.8275 | 2025-09-30 06:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 95220885-07fc-3c47-962d-91b8916b1b8d | -4.89518 | -43.45556 | 2025-09-30 06:14:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f219c584-d8ed-3605-8769-a982aae8983a | -3.08585 | -47.00298 | 2025-09-30 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 63cdcf17-808d-33e8-9b6a-586e21de913c | -3.80338 | -47.56736 | 2025-09-30 06:14:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 62ea51c8-3d76-3f63-9f47-1911194a51d8 | -4.25169 | -48.5523 | 2025-09-30 06:14:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7e142a15-8d09-3b99-be68-3ba08dcd1580 | -5.97595 | -51.90638 | 2025-09-30 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6ceb27fa-2d16-3584-9f9b-40ef58b54b65 | -7.04883 | -45.1871 | 2025-09-30 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5bcaaeaf-edd9-32f2-95e2-e6ba2cfc283c | -7.82094 | -46.98672 | 2025-09-30 06:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 67648e5e-ed7e-3c50-b03b-f8e490d61e48 | -7.91088 | -44.62492 | 2025-09-30 06:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 084225e9-3b6f-3e62-9105-f3b7fc530c1d | -7.81945 | -46.97963 | 2025-09-30 06:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 235464b2-5d5d-30c1-a894-b93dfe26d030 | -7.82837 | -46.99502 | 2025-09-30 06:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f5ec164f-d1a4-38a0-b004-f11bbd21f36c | -3.84796 | -48.97074 | 2025-09-30 06:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cd241c42-66a8-3aea-af3a-cb1550901bc5 | -7.83928 | -47.25328 | 2025-09-30 06:14:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 052652ae-3487-39db-8e7b-5a3e38e2234b | -7.91385 | -44.60247 | 2025-09-30 06:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 4c31a3ee-195d-3a05-8436-3d4e95a9896a | -7.11104 | -47.7776 | 2025-09-30 06:14:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| a9803d0a-4790-3b8e-832b-b6fefa766d1d | -0.09067 | -51.28042 | 2025-09-30 06:14:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 339e48aa-309c-363d-a95b-fb1c193359dd | -14.51214 | -48.42421 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3a0a5704-a49c-33c3-8807-7d989f482abc | -14.69792 | -48.15054 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cd3df488-c410-3e0a-9029-4fb654b5f3c2 | -14.53686 | -48.25719 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| fbd93ebf-2c00-382b-aafd-acf241e31a96 | -10.17392 | -44.894 | 2025-09-30 06:16:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 26933502-9eb9-36a5-bf51-dc46de4015c0 | -14.69608 | -48.16481 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 14c5be25-eacd-39ec-a9a1-ec270d626236 | -14.00203 | -49.62959 | 2025-09-30 06:16:00 | AQUA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ce7e768c-ffd2-384f-bbf1-8566c7bf4d67 | -11.16449 | -54.11749 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0431f8be-7fcb-3320-b04a-f7f383ae3c50 | -13.40206 | -47.543 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fe532be0-45be-3c1c-aa51-b23a6114879e | -14.51021 | -48.43867 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 19eef579-a71a-367d-aab8-207a79ee7bf2 | -11.75109 | -46.84549 | 2025-09-30 06:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 631e6426-16f3-3758-b37b-d93f4abb61d6 | -8.13497 | -46.36228 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 02b95ad0-333e-3a61-abc9-93991a393355 | -9.95526 | -48.79009 | 2025-09-30 06:16:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9ca66b10-1ea4-3e6b-b8e1-0309538477c9 | -8.86452 | -46.65416 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 19f06b50-e68f-3472-abc6-32b6230baf8e | -8.14643 | -46.36433 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7f320c22-2947-3e56-a7f5-0d5520671cf6 | -15.72147 | -47.58558 | 2025-09-30 06:16:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 09a96e47-1b59-3f9f-8d25-e3c0658ad4c7 | -14.54782 | -48.25916 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9b9375a1-ffc2-3779-9e3c-26bec536234c | -8.8688 | -46.62322 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 520782f7-104f-3a1e-a706-c9be85a4de49 | -13.39126 | -48.06693 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7d93262c-f888-3cad-be38-29d02ddc9083 | -14.78151 | -48.30365 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7fbbdb1a-9116-3c80-8f1b-8489af9b998b | -8.82603 | -46.18456 | 2025-09-30 06:16:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 53d37be6-b571-3ff7-86f1-4fc0156bdcf6 | -12.22102 | -47.79388 | 2025-09-30 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 69c77d03-760f-3ffc-880e-62b3d43dae4f | -11.14454 | -54.12435 | 2025-09-30 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| e244afa8-1082-3d56-95fc-9f1b13a7b439 | -8.87673 | -46.64531 | 2025-09-30 06:16:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 9f84b4bd-9a3b-3167-a036-3019d5c104cb | -13.57738 | -48.04573 | 2025-09-30 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| edeb31fd-d4f6-3493-be82-745823723b0d | -14.52061 | -48.47353 | 2025-09-30 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 41.8 |


[Clique aqui para ver as próximas entradas](README106.md)
