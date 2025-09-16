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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f24fe37-5512-3c98-bea8-9ffda6d822ca | -14.50537 | -47.32277 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d98df0d9-0f7a-3077-a71f-fbf91b8581af | -16.68925 | -49.77517 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e388f15d-3479-3103-9dd0-96530dc6cd9c | -16.01054 | -59.25972 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95af0e00-8836-392b-8be5-6c065c4345c5 | -16.42498 | -45.67196 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4db6f01f-3716-31fd-8772-9e9d00c5412d | -16.58982 | -42.90596 | 2025-09-16 04:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07d8a1ea-3d3d-365d-a3f0-50feea6c37c6 | -16.01229 | -59.45321 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 356eec73-8c3a-38d8-a72e-8404559349b2 | -16.5893 | -42.91011 | 2025-09-16 04:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b5ac819-935a-314d-8c79-414343a5e0b6 | -16.6364 | -49.4119 | 2025-09-16 04:32:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6a4113b7-32bb-3488-8edf-d57d29eb3ff8 | -14.47755 | -46.35926 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e0faea6-c9be-3119-af6b-b76e22d436cc | -14.82236 | -51.66416 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30df6532-293b-30fa-9440-b84fc43698dd | -16.68098 | -49.76223 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f736b5fb-656e-356c-a1e1-4f6a07f79cdd | -16.70998 | -54.97364 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c3c36d6-3016-3e49-a2ed-696af35702c6 | -14.28495 | -45.99984 | 2025-09-16 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d62d7517-1e10-3ebe-b9fe-be816af3a63a | -14.82892 | -51.6699 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ccc07b7-620c-3e48-af43-ab6666718502 | -14.83624 | -51.67125 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8596bd9f-ac5d-3984-9732-8b03f1265d60 | -19.88374 | -48.35074 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad2493e5-3fc9-344d-8d6f-edc4238cf962 | -16.02409 | -59.455 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f046d081-1c33-3aa2-94fc-68665b3e49cb | -17.07795 | -45.82862 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8f544dd5-e0e0-31da-ba67-1cb23af3b309 | -21.19767 | -44.36847 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 631c734f-8284-3286-acb8-e5d229a4c57c | -16.68769 | -49.76354 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b4f4c25-c286-353c-9219-49748af783a1 | -14.96995 | -46.56251 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd7077ed-70db-3d94-a274-c7bb9b019e69 | -20.41336 | -45.51184 | 2025-09-16 04:32:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42c9963a-8c09-395e-897f-5833b638c4fb | -14.29983 | -49.53302 | 2025-09-16 04:32:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d24c62e0-542a-3dce-a16b-4539dc248521 | -15.82029 | -53.47024 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49d33f6d-28f8-3dce-a71f-8123cc953118 | -16.70139 | -54.97166 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46441ddb-ca59-367c-8957-13551075dd42 | -13.781 | -54.95447 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9ef0a5b-4b39-352d-af48-e53a268a8080 | -14.51819 | -47.32864 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b146b80-0018-3876-8c9a-607587994d62 | -16.03835 | -59.4449 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d3724b0-9aa1-3e0a-b597-c34ae2537ed5 | -18.77555 | -47.63916 | 2025-09-16 04:32:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edf2abe2-7123-3918-a1e4-a9136bb71f4c | -16.00146 | -59.4468 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5381750-ed5d-3c79-9b9e-e6e1479a5444 | -17.86715 | -44.44286 | 2025-09-16 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f745fc3f-665c-383c-9013-dabf3313b929 | -20.17928 | -44.89609 | 2025-09-16 04:32:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db5137a3-5f7f-3b70-9363-3f4b51615e54 | -16.69472 | -49.78397 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0644ca11-9b14-39e6-9e1a-5e7975f10b51 | -14.92202 | -51.64869 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c265000-6bfc-378a-9ec5-fbaecc3c6e0f | -15.56551 | -44.36717 | 2025-09-16 04:32:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1dc3305-6210-3b1d-8ef7-144649ed4af4 | -13.75669 | -48.76622 | 2025-09-16 04:32:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f62d454a-c992-39bc-8913-a5a42bb44884 | -20.86235 | -46.21001 | 2025-09-16 04:32:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81ea9552-de2b-35b7-bd24-9cf1ddf4d4df | -14.80539 | -51.67467 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 10aefbaa-eaa6-3843-8835-0045766e0caa | -15.80062 | -53.45823 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d5d6626-3cd4-3a0d-8459-5778f4df2743 | -17.07735 | -45.83279 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 351af1b1-2bac-38e3-939a-ea0a743b2c63 | -16.48559 | -55.10692 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f2741967-9a1e-303b-b8cc-4beb0e8f3f7d | -14.52377 | -47.33696 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42241aff-1578-318d-a9c6-17c2bf2191cb | -15.53282 | -44.32372 | 2025-09-16 04:32:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 292bedc1-b057-3deb-9d6d-a2f42ea95774 | -15.83131 | -53.47786 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d372ece-b0b7-38e8-8a50-ebc3acff279f | -17.07497 | -45.82388 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 192f2c16-738e-392e-bc5a-ccd620df22ab | -21.15974 | -46.28268 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee0f6531-ec21-33be-b9ff-313259f8d347 | -15.16229 | -52.46071 | 2025-09-16 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89e2c98b-baff-3cb4-9d42-5a48bdc8a819 | -17.32777 | -46.79671 | 2025-09-16 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb905c68-ae14-3932-bf6f-81a3f2d5aaf1 | -16.70544 | -54.94768 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d808e82-b304-3a5e-bd02-1b04018adc01 | -15.82333 | -53.47627 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98bc63a9-217d-3843-b4cc-0aaffc3a764a | -15.99525 | -59.41844 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdbed53c-f432-3f8e-a94c-b6db17b1e77a | -15.08898 | -52.48361 | 2025-09-16 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 117a43fc-412a-351b-9748-dd1901b3dec7 | -16.7057 | -54.97256 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9d40c6a-02f1-3f2c-bb92-adeca1c6c15d | -15.99691 | -59.41056 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72a8ff48-bd35-3c10-b282-ce75feb54c71 | -17.08152 | -45.82914 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a54c51dd-4f84-35dd-918d-866ceac1a3f4 | -14.52086 | -47.37766 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44ffc7ec-f4b2-3009-b44a-22a0677a77d3 | -14.52261 | -47.34435 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31aa66b0-5010-34e2-85a3-eb6dfeb61464 | -15.84084 | -59.43569 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 737c2d10-37d0-369e-96b7-e076e07a7e5a | -14.63341 | -46.39205 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c0ff700-659c-3825-b8de-d3f0e2e275e4 | -15.82828 | -53.47181 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3524cb97-1ca5-3afd-80c9-4cbf898ec7d1 | -14.8538 | -51.67902 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 541e996a-50ea-38d4-b24d-f7a26bc863e0 | -15.77761 | -53.4483 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7425535c-7778-3113-8d76-52e4ae526578 | -16.04515 | -59.44141 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c13d19a-4d98-31e7-be16-500cfa8d76f4 | -18.86976 | -43.35184 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d91a8187-8351-3d59-97d0-4093a19799a3 | -16.00278 | -59.41153 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e05d86e-b240-3e37-b14b-70c7d5569f91 | -16.5155 | -43.54574 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 25758fe1-919e-3180-bef4-90b44828cf60 | -14.61236 | -46.39227 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 484de1b8-b152-3cbe-a03e-b9e0f0190d63 | -14.80694 | -51.66586 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e25be200-8437-3c8f-a380-6980ee6bc327 | -16.01715 | -59.4591 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4687973-b786-392e-98de-96cc1dec7104 | -16.43997 | -49.58493 | 2025-09-16 04:32:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb3ec87b-a961-3f7e-a8cb-40b474c6c31b | -15.4178 | -47.33432 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dd0e759-2bb5-32bd-af01-10bee653c7bc | -15.85762 | -59.38548 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cbfc0b3-bb46-3981-afdb-875bbb0671a4 | -20.19024 | -46.28971 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f82d9223-884a-3bf2-bc55-7c0ee4db6ec2 | -14.54043 | -47.36214 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f3a98d6-7fcb-386c-a0fb-e2a85432be2a | -17.29915 | -40.68444 | 2025-09-16 04:32:00 | NPP-375D | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 905e79ed-7962-3afd-a8d4-951b5c46a9a2 | -20.96919 | -45.94405 | 2025-09-16 04:32:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49682756-324d-3f0b-b2a9-7daff04df6a3 | -14.97446 | -46.55577 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb546fa5-b8b1-3bca-895d-ddbf059e8728 | -20.2037 | -45.36573 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c341ac28-b35b-3f9b-bf41-811e56b9da89 | -15.83248 | -59.42847 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdaab44a-9eae-39c1-8ac9-39f18766ea01 | -20.18007 | -44.89285 | 2025-09-16 04:32:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b534c419-df18-3f9c-8ee4-a45ddb135bc9 | -14.82969 | -51.6655 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d4e7331-8ffd-3a2a-97ce-c3c83cd7ca82 | -16.02087 | -59.43214 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74e0c57b-1ff9-32b6-9a72-4cfdacd0e663 | -14.51484 | -47.32809 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e208e747-9fe4-3d62-be4b-d99251f1b656 | -15.91786 | -56.27545 | 2025-09-16 04:32:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6793b6ea-40a1-387b-9b36-5a6ca82148cf | -15.76997 | -43.86208 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00a0fe18-4613-33d9-ab7c-4cf3e3f8c97c | -16.47606 | -55.10917 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| aa6826e2-5554-3b2b-821b-6c166d153904 | -14.52204 | -47.34801 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c14c773-2b14-31b9-89b8-4579ee901b63 | -18.86926 | -43.35592 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 702d713d-e493-3bcb-aac4-47f1b05bacd3 | -16.69808 | -49.78458 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5d31fac-dacb-3540-8647-289e5a1e44f5 | -18.16439 | -49.20557 | 2025-09-16 04:32:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ed576497-e498-33ed-ad7b-b94f3999312c | -18.57919 | -48.15243 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92c5c4a2-f58c-3429-9632-903e9e40ee6f | -15.59175 | -47.94181 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf4053ce-3321-3cc8-8a1f-41406376fd3f | -17.30405 | -40.68518 | 2025-09-16 04:32:00 | NPP-375D | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e6f5fa58-4b2e-3ff1-b737-cec58ad08d99 | -15.87496 | -59.38973 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 98a7b392-3541-32ef-932e-a0bfaecc3026 | -15.83687 | -59.4257 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80f1fe01-7f0a-355a-a29c-e20cb47fdf5e | -15.01895 | -47.97301 | 2025-09-16 04:32:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36613bb7-5686-3163-ba5a-860c84491e37 | -15.40064 | -41.70656 | 2025-09-16 04:32:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ab4ba1c-e550-314a-82a2-2ea9b7413803 | -14.60379 | -46.37929 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 740de7b6-e848-3520-be73-63db233ed97f | -18.17355 | -45.19136 | 2025-09-16 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7b74448-c671-3fa5-9510-a4e9e75ab151 | -18.55583 | -49.26174 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |


[Clique aqui para ver as próximas entradas](README55.md)
