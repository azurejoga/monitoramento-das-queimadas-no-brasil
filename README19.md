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
| 37d16b22-8cc3-37d7-a08d-cf9da39a291e | -7.49208 | -42.55552 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f9f30400-dac8-33bc-bd8c-eb482f74abe5 | -4.05227 | -46.21632 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8381b910-a351-3173-a254-96a7b167df04 | -7.33525 | -40.37167 | 2025-11-15 04:04:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99c631be-7208-376c-8681-58e0a13c8587 | -7.3518 | -43.34818 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a358528c-3f76-319b-a850-bcced85a09c8 | -5.88821 | -42.26955 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ed44c41-9c9c-3079-a536-9e22f20dca65 | -4.8796 | -44.96289 | 2025-11-15 04:04:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b06f603-aba2-3743-8a0f-a3f5897abd83 | -6.29245 | -41.75287 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c24b466-80ac-30cc-ae87-2c6d571156e5 | -2.63647 | -45.76376 | 2025-11-15 04:04:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6a54b9b-f687-3153-ae43-8da190b053bf | -3.66418 | -44.81244 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60a3b71e-9bdf-3076-b4b3-0832df28409b | -3.7537 | -45.87015 | 2025-11-15 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cd2c302-e0e2-3319-8b36-edab1665c29a | -4.59618 | -44.32138 | 2025-11-15 04:04:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c4ce5b0-6e95-3633-b42e-cfafd764c9b2 | -1.9163 | -47.91521 | 2025-11-15 04:04:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 605e4cca-33de-37bf-a1b9-ac36711aeb60 | -5.43098 | -42.57801 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e1f855d-c47d-3a3d-94de-6662b6d30f1e | -5.38573 | -44.84309 | 2025-11-15 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0feb90e4-ba85-34fe-8c96-c8076e6b1b13 | -7.72396 | -42.34445 | 2025-11-15 04:04:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9317cc5d-2472-36da-bbbd-c59f1992edd0 | -6.51809 | -43.3997 | 2025-11-15 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 67f7cadd-d306-37d7-8de9-72b96ddc3f87 | -5.51513 | -40.98061 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 970bcb25-c350-3f15-bd59-5a1e23fe9355 | -3.99417 | -47.99721 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab4aa823-bf09-3b3a-a007-2ace54c0bf31 | -5.51907 | -40.97758 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fba61cbb-9c85-3f8d-9ab4-d6d9bafca68f | -2.71505 | -47.40293 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a2c8452-f261-37fc-adc0-b996a5c1bf31 | -3.28607 | -45.463 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc4a2491-3b7a-3789-abd3-37ed28b52287 | -4.91802 | -44.78171 | 2025-11-15 04:04:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2b1ad72-32d5-3d3c-8ff4-cc8faad83ba8 | -4.41255 | -50.82936 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2131a6e-729c-3190-975b-27382d922f99 | -3.38527 | -47.19312 | 2025-11-15 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23ec9109-a5d6-3a66-8928-851d3cbe1225 | -7.34817 | -43.34759 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 343b4d37-6538-3faa-adf8-f2d1bba96ec4 | -6.26317 | -41.41381 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b606919-df87-3bf3-b1e0-0919ac4bf5b1 | -6.58946 | -43.62036 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ce9bca1-88e4-39d6-b4cf-78f0395f4565 | -4.86529 | -47.38068 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c6dccd7c-b329-3a5e-8983-410a0dc6ef00 | -7.33193 | -40.37115 | 2025-11-15 04:04:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db6664c1-47ac-3405-80a6-558f2993cd64 | -4.11325 | -50.05831 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acdf995d-8207-3b5d-a1c0-528bd56086b6 | -4.35246 | -46.48908 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d358b1c4-85e3-33f6-adb7-26ee9e598238 | -5.48209 | -40.97154 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5f52638-90b1-3cb3-95f1-7d5bf4219ee6 | -6.31319 | -41.82095 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20e7f6c7-7be8-3dd7-997e-ef8ebcdffbe4 | -4.91457 | -38.68595 | 2025-11-15 04:04:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bb20d09b-4b90-368e-92c3-00fd890c23a6 | -4.3933 | -44.07824 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04baffcb-03f1-3e5e-bdc8-f77101ec6c2f | -6.16925 | -48.05104 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 885e24ed-9812-385a-9d1d-415be1edf856 | -7.29512 | -45.11612 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb561f7-1341-3c39-a45a-0ac0898f9392 | -6.03959 | -39.49117 | 2025-11-15 04:04:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04b11590-0fbf-3076-ba60-3b7cce8517c5 | -4.11076 | -48.01219 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5286a5bc-94cf-35d2-98ac-fc1dfcf95745 | -4.94383 | -44.75212 | 2025-11-15 04:04:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbfa3e4d-3eda-3ce4-a515-fad735260633 | -2.73736 | -45.30242 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddd04464-5540-3a73-8853-82d7d1fa174d | -4.89758 | -44.0551 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1eb6f4b3-bfb6-3e10-bf41-36b5bde8f245 | -4.11251 | -50.06254 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f31dc319-a163-35ea-b326-bcfc3b9e591e | -3.22513 | -45.48116 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 17e34e15-7dc7-3b42-a3d8-7626b9992783 | -6.4804 | -43.95284 | 2025-11-15 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bceed261-1e4b-32dd-a336-0069e9049c23 | -5.36823 | -44.06661 | 2025-11-15 04:04:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43ade8bb-be9b-3cc0-9e15-a4ff2468e39d | -4.68057 | -45.27655 | 2025-11-15 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57af5769-49c7-3df1-9052-511b4b0e0107 | -4.91683 | -44.7889 | 2025-11-15 04:04:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 505920d6-ea8c-30cb-8b02-6c7a68999c87 | -4.68207 | -45.85081 | 2025-11-15 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94179ca0-59c9-3927-9d23-9633cc50c70d | -5.58131 | -46.15062 | 2025-11-15 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a881c39-6f70-3bfe-8173-7c10f3959650 | -6.28963 | -41.7486 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3ca8424-9ebc-3a07-90b8-83a88785e412 | -8.23613 | -39.98036 | 2025-11-15 04:04:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57781e5b-4620-3334-b417-ab4fa98cc805 | -4.732 | -47.16262 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| da7c9e17-91d5-3ee3-926b-3f90680f097d | -6.28843 | -41.75601 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ef4be2c5-91d6-3700-a783-5a86799fd1f0 | -4.53769 | -43.21291 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f64a9ed-baf5-39ca-9fb9-ceea69db2033 | -4.8695 | -47.26966 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 373c47fb-6f4e-3ff5-be86-e2da1610bd27 | -7.08127 | -41.58485 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b84afe27-2867-3a38-8d31-ab60b5de8732 | -4.3516 | -46.49409 | 2025-11-15 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ef4b054-66aa-3fdc-9097-0ed7ffbbd460 | -4.86681 | -47.26825 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f91e9821-4a85-3912-937d-46bb7defd79a | -6.09347 | -41.60004 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5f6ff81-6a8c-33b7-9240-5004199c7a0d | -6.30171 | -41.82672 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 381166c5-b44b-30e2-9920-9e4b201a83aa | -3.6594 | -44.81555 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ea0352d-785f-3c19-a9a0-b51be2d09e92 | -5.84172 | -46.66768 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7942f430-526f-3401-bb38-bc3752111c3d | -5.60412 | -45.18156 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6914b5c0-8132-3ff6-a451-a81541b151fa | -7.2148 | -38.37006 | 2025-11-15 04:04:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad04cc60-e351-3ed4-a080-8c98d4c0132b | -6.39087 | -40.1823 | 2025-11-15 04:04:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8f12142-1d05-3c71-8ba4-133a11c741dd | -2.51295 | -47.80787 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 98b5c072-38b1-33a7-893e-050b53f31781 | -7.43392 | -45.2275 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49fe1776-ebee-3978-b52e-36bdc7131392 | -2.51832 | -47.80941 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4260f011-2983-3f8b-bf4b-878797a19504 | -5.16922 | -44.84884 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bfa0503-8319-3ee4-9857-25ba98ce06c1 | -4.42253 | -43.35329 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e6fa2d0-bd3f-3b12-aad5-3d3847fff32c | -3.26467 | -50.09614 | 2025-11-15 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c9c3e23-bf5a-3767-82d2-72c3b3fb50d0 | -4.65872 | -45.04405 | 2025-11-15 04:04:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f31cf01f-2e4e-3848-8b0e-b7694bacc474 | -1.3251 | -49.13666 | 2025-11-15 04:04:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96f76843-7b4a-3e83-9c42-af9e40e5b73e | -3.7063 | -47.63323 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4776df1a-a78b-3a86-81dc-b85418f0bb7b | -5.23431 | -44.34668 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0bb74ab7-250b-3139-81c0-e4e31230d6d6 | -3.99021 | -47.6746 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 510f9858-3956-3288-b1bf-0087f7ebb7ba | -5.77685 | -44.38514 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a9faecd-bc70-3fbc-8560-b96f49cb0059 | -4.54744 | -43.22368 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 00a64473-d690-3a91-8d96-608b9f9d9bc5 | -6.88014 | -41.59684 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 00e58ead-4a4d-3075-b6bc-791845026d7e | -6.31265 | -41.82042 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58b07d00-05c3-3ff4-ba9f-5a570885a452 | -6.53316 | -39.06754 | 2025-11-15 04:04:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 73b2c68c-54dd-341b-a24d-f6d28545e8e7 | -5.0665 | -43.68763 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85a52e3d-b2f3-387a-90cb-7e871bb80af5 | -3.67875 | -45.83694 | 2025-11-15 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41a6370d-9f82-33e2-95c8-8022d79e354c | -1.05302 | -48.94993 | 2025-11-15 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd9aa73-baff-3712-858a-e78b7e9cfecf | -7.21515 | -35.02931 | 2025-11-15 04:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3db1f2d-94be-3466-bcdd-f2d33cd035f5 | -5.74928 | -42.72025 | 2025-11-15 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92dd5169-9099-3789-803c-89e2136e639a | -6.25922 | -47.07966 | 2025-11-15 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1326fb5-effe-3afd-979d-477f7e8f3d86 | -2.51256 | -47.81173 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ff22049d-9995-3758-984d-24e27b4edc1e | -3.69437 | -44.16152 | 2025-11-15 04:04:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cace983b-1610-3ccb-83e0-abf2b2dc7d37 | -5.43047 | -40.66271 | 2025-11-15 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af9dc791-f152-3eb6-8172-d1260306bf92 | -3.37561 | -41.16355 | 2025-11-15 04:04:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d3af9f6-4880-3e91-a4f1-d581b4fea31f | -3.1412 | -49.23918 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b182946a-c461-3471-938e-0c0e576869e6 | -7.35199 | -43.36993 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9114d8ef-cca1-3c68-a12e-58d995680ce1 | -2.52289 | -47.81277 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304bc615-947d-361b-8005-204c11b3702f | -5.84336 | -46.66127 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4740f33-0b01-3c2d-8eb7-de758436a5e7 | -6.28784 | -41.75971 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 39d08adf-2f95-3e93-a09a-9dbc22caf2e2 | -4.32507 | -46.37966 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5d0e5bd-af95-3a3b-b268-085317b0cf42 | -6.73581 | -42.96037 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 236a4522-f6c9-3364-b6a6-0639358c7767 | -6.87909 | -41.58166 | 2025-11-15 04:04:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
