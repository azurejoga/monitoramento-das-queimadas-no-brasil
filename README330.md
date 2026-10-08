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

## Dados Diários - Página 330

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d963789d-cbdd-3c8b-8a15-eda1cec15d3b | -9.82173 | -44.83891 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6a0c5803-501e-3b65-8ab7-1c15510d5dc8 | -5.77914 | -42.56821 | 2026-10-08 16:37:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 79486267-feb7-3907-a40b-53f394454dd8 | -6.94848 | -43.07044 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 512880f6-7811-3bac-8b0b-bd7da0c8a940 | -13.17028 | -54.33496 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 9f24f574-68aa-358f-9f81-96e85d567712 | -8.9596 | -45.12498 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 199bf357-3089-348a-90a4-c6b9a9f6eb11 | -11.7562 | -44.93006 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| a6f5c212-6d5e-3e66-a264-a05a9acd0957 | -8.19834 | -45.78423 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fd2c3888-365a-3b4c-851f-be63182d26dc | -8.87765 | -48.10324 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 461c9bb3-0f59-30c3-9c04-8c11f0642ccd | -7.88302 | -44.96649 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b8181c17-ce2e-3ddd-97da-4fa2477ab068 | -19.33995 | -40.47371 | 2026-10-08 16:37:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| feb92810-7ac2-3169-a9df-394b31600da7 | -10.1603 | -44.67979 | 2026-10-08 16:37:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| c63c54b4-53da-35fd-b0bd-a79dad035e7d | -9.70564 | -42.80402 | 2026-10-08 16:37:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 206ea69a-7d2e-372b-83fc-df6458f502c6 | -6.56898 | -44.1113 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a34f23c0-a94d-3052-b6d1-9531d1de3297 | -18.35972 | -42.76653 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e25cf8ca-56c8-3822-8891-99d2c5343860 | -6.8235 | -39.31219 | 2026-10-08 16:37:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ef67b0e2-30a8-34df-a1f8-6ad5cf714e49 | -7.21496 | -44.27369 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 091686f5-273d-3457-89f7-fa0ec913a7d0 | -8.60842 | -45.64744 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d513707d-a70f-3850-b943-089b24c416b9 | -7.33922 | -45.29268 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e7ba1c38-d59a-3753-b6ad-c9b296327ed7 | -11.07584 | -44.01664 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f1bca696-bbc3-3958-89f6-35eaf75b8138 | -12.23531 | -44.71267 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 12fef6c0-d5c1-36e8-9c95-ea6bfc7437be | -10.61176 | -46.27112 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2920e080-fc58-3a24-9058-e9885e88e3d8 | -19.32512 | -44.02095 | 2026-10-08 16:37:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2f0b2f0-3249-3cf0-9444-29198b7ce532 | -7.92528 | -46.809 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 703ed524-1978-31ee-b18e-9f7b487800ed | -6.60791 | -37.89386 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 13.2 |
| eea80b00-c7e0-3ae4-8139-c7e178b76961 | -10.88005 | -57.11152 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 38005f44-6806-3c83-9f30-ceb33fc82e57 | -11.34111 | -41.59085 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| aa9e80be-bd95-324c-855c-04c11ae1b6a8 | -11.62552 | -43.70708 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2ddbdb5d-e214-317e-8f60-3204c6a1c892 | -6.36373 | -42.57259 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6c945a31-24d4-3a08-83e3-a303a3e2adc8 | -10.51758 | -47.31452 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87366d75-e768-3250-b8a3-7ee19e7c4672 | -7.37464 | -49.09315 | 2026-10-08 16:37:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1eddcc9-5cfb-344a-8798-4249f4369f37 | -11.11137 | -44.0037 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 4cd75357-b6f0-3458-8d2f-65ec875817b7 | -11.71904 | -43.65458 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83731f03-c162-3d48-8a26-5d7a52aa3241 | -8.53437 | -48.75146 | 2026-10-08 16:37:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e580bbe8-4a3e-3315-9357-ae2c3b76d8b0 | -9.13891 | -45.83514 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 431cc27b-a025-35b7-bfc2-79fb7b49aa58 | -7.23585 | -39.39832 | 2026-10-08 16:37:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 69a12412-addc-3bbb-a6d0-b4961b2aad6a | -9.44905 | -44.60155 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f27d1013-0004-32b5-b415-4d6d7b2261d9 | -8.03576 | -49.40257 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d9f2cf7a-5626-3c5c-9ea8-bbedd0293f0d | -6.97303 | -43.29363 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| eb750cd2-5560-3c1a-8848-1ef2629d6baa | -11.24149 | -44.84828 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8213ded9-46f0-34bb-a93c-d075212d0496 | -11.5798 | -43.67755 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 54a4e7aa-ea4a-3f2e-8632-c5281525646f | -8.96782 | -45.13441 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a890a31e-2057-3e65-adc3-e795fad4db3f | -8.94248 | -45.19214 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 248787a3-f769-3648-8f72-c9e4da89cea3 | -13.81707 | -47.84961 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3f5e292-6587-3f3c-8e41-d5acf65fe579 | -12.19405 | -44.82 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 380dad6d-8725-3f57-be85-7844dfb12bdf | -11.7998 | -43.51958 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f43e9739-b4dc-342c-b900-cc799a0b373f | -9.81293 | -45.69479 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| be3f1d7c-18b2-313c-8a0c-59e83f261a5c | -6.59616 | -44.85277 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9da67eb-1c55-36b2-bef8-9bf4a2620dd1 | -5.75505 | -41.64138 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3cd3ef68-1afd-3f43-aab1-c48f37156bf7 | -11.45017 | -43.39157 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d7531d74-60a1-3198-9a91-653652b5889a | -19.05652 | -44.33727 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b0eef0f-2415-3a51-b355-1c2e92730da3 | -5.76485 | -42.06694 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f73b440b-1c21-3df1-8166-9a5e8ca6027e | -9.21166 | -57.72187 | 2026-10-08 16:37:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| f584c221-5e2f-39cc-bdd9-7caf3517735e | -11.5887 | -43.66875 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fee557ac-13fb-3770-805d-0ef1f919c1e0 | -13.11526 | -43.48497 | 2026-10-08 16:37:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 31cf873f-0ba0-3301-b7c8-602229ea9db3 | -11.07745 | -47.48983 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e901954d-ded1-325d-a90c-d78b61bf433f | -8.6605 | -54.53224 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 05de4c72-41df-39af-940f-15700660b40c | -17.76264 | -44.52267 | 2026-10-08 16:37:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4537310b-bc7a-36f5-8174-8e192cdb3324 | -11.83948 | -43.5318 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7874d8e5-cf0b-356b-98f3-42866dc7674b | -10.15976 | -44.67629 | 2026-10-08 16:37:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| d3adeeb3-ac9a-3ec0-9830-007d92f35e03 | -6.97584 | -45.13692 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b8cfcb0a-30f1-3fba-b1c8-7f0e3615717b | -11.26938 | -45.21006 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| a82c6a5c-2e87-3f13-a33a-72ebebf95f6e | -5.99101 | -40.92826 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| acf85f23-4227-3f2f-a319-99f04a1999be | -12.2455 | -39.68192 | 2026-10-08 16:37:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b4e5401d-bf89-3cc6-b861-596594694ec2 | -6.49474 | -39.95354 | 2026-10-08 16:37:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 527eaa40-4ba4-3bc6-abf3-559be462e254 | -13.37076 | -43.885 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 240c0f2c-01dd-3868-8f47-a160e93c1936 | -11.65059 | -43.67679 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6ea46cc8-18ea-376f-9e1a-bbf6f6123a49 | -10.92728 | -49.75596 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 226cf2eb-c97d-3646-84d9-f9f43a47db3d | -10.24924 | -49.67599 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 64c7b246-2d38-3846-bc9d-197a09a3cafe | -6.68025 | -45.37756 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a17b2645-8d2d-3244-88c3-683f646b932b | -12.22958 | -44.76398 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7896a935-4c47-3d96-921e-e7725295bc53 | -6.82451 | -39.55663 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b2479039-9802-31d7-8661-22cbd0a5f03f | -8.29619 | -45.73654 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 034793f7-1923-3ff9-bdff-223bf93ada3e | -12.03894 | -43.43967 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| d82c6b22-8306-3456-b8a4-ecdac087521b | -8.89349 | -45.38122 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 28649ce5-e6c2-3abc-9167-7b039970f220 | -11.69013 | -43.68867 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 8e6ba18d-7cf9-3038-8346-89d8342c4692 | -9.53346 | -45.61823 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| a82ff2c5-d737-3baf-91bb-49d991d1d4db | -6.03618 | -37.27964 | 2026-10-08 16:37:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 16.9 |
| cae46f74-e3d6-3a38-affe-343f06e3ef3c | -11.38516 | -47.72745 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa57d039-8ade-385e-9332-8a29dd6dba89 | -6.82664 | -39.5424 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a99ee92d-f19f-3a4b-9f37-bf52b5be32aa | -11.76825 | -45.55056 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 599c6c0c-5649-31b5-b8f9-451c0ec5aec9 | -11.1147 | -44.00316 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| d6fef82a-825c-3a12-827b-c49800663a24 | -6.69479 | -44.01933 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a59fc42b-e338-3ed3-a5bf-493867807a8c | -5.7475 | -42.054 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| c47ecaf9-0735-3eeb-b782-f89e8ac18ddb | -11.8065 | -43.5185 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38140582-d994-3a59-b228-577b99f04c06 | -7.88565 | -54.98726 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 52e1cf52-6fdf-3fad-8f62-abcb0596d4a7 | -9.89388 | -44.84486 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f3c70fb1-fd74-362b-9633-367ef6508a36 | -8.10043 | -47.70674 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 90b19c71-c9ca-3d78-a084-fbe2aa4fb954 | -17.94679 | -43.95364 | 2026-10-08 16:37:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 009f71c8-4922-3236-8cbb-7195f6a164f2 | -7.87751 | -54.96717 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edb4c6a5-7c56-3130-92c3-e274c212fa27 | -8.76247 | -36.6596 | 2026-10-08 16:37:00 | NOAA-20 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5ccb5a85-87ad-3018-bcc4-237c7d1f09a2 | -11.60691 | -38.98372 | 2026-10-08 16:37:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0d238a2a-87fb-3234-bd58-cda31ba1d646 | -6.39901 | -44.5036 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 11e34b56-3458-3701-904c-17d3ceea1f8c | -11.22385 | -41.58387 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9bf15e8e-21e5-33bd-b770-064aab67a5a4 | -11.07196 | -44.03545 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 34d85091-e504-3019-ba61-f03928e5f921 | -5.98977 | -43.69777 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 66abed31-4871-39d2-9a83-1caa23f08a54 | -11.26991 | -45.21357 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 832b75c7-e666-3939-98f8-edc1928cbaad | -9.43506 | -45.97799 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bd58bca-a481-3a5a-8f56-dded1014308f | -8.84626 | -45.4497 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 139016ff-1707-3d71-8e07-210e7e7d2c5a | -6.67693 | -45.37807 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 2d5e04a4-bde7-34d1-8ca5-8b64e981f0ab | -11.85331 | -43.54045 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README331.md)
