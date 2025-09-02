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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c5971e7-0da0-381b-929c-8b6617ed11e7 | -6.9931 | -43.22948 | 2025-09-02 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 262b0101-d841-3887-a15d-8d8b5c49517f | -6.99419 | -43.2238 | 2025-09-02 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9598b00f-bd4c-3b0a-80b7-55d4d87b0897 | -6.25573 | -42.61152 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be4aa03c-5725-38c1-963b-8b27dfd23e30 | -11.97229 | -45.86302 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcccd844-8944-3db5-ba0c-4784694de5ca | -12.75586 | -44.41264 | 2025-09-02 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e981485b-0c3f-3e36-982d-d20680a82baf | -11.06194 | -45.3954 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1d16eef6-79b3-3be8-a5ca-92875be9cb49 | -11.05418 | -45.39336 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f5101a1-9ea7-3d4d-8161-c82f092b8430 | -11.37715 | -43.57223 | 2025-09-02 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50b3738b-9594-31c6-af27-14d256838e96 | -14.05217 | -44.55208 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5196a037-b8da-33ec-8ce5-8dbfc96ac456 | -11.97193 | -45.87692 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c61fe282-3183-33a9-aeb9-7b50389a63ed | -11.08823 | -44.63529 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 8f593724-3700-3b07-9a0e-683d25bd6188 | -11.10417 | -44.64302 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bc8e4e99-1bbf-3a6e-a48e-90bf2d5e6fd6 | -11.09365 | -44.6427 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 2152ead1-9df8-35e8-8487-abf7c9b3c9f0 | -11.04878 | -45.14564 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 817e2fdc-0591-34a1-a43f-f1c30ea3f9b5 | -14.49047 | -45.9425 | 2025-09-02 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf24bab6-257f-3e40-add8-b91e24c3d69a | -11.38167 | -43.61414 | 2025-09-02 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67043ace-e862-33ad-b5e4-3442916f7f8d | -11.10822 | -44.63903 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ad5b60cd-9a20-3bf5-b906-6b715eb85dd7 | -11.09498 | -44.65382 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a26e3cc0-a53d-353d-90a7-c2d8dda431d3 | -11.37546 | -43.61277 | 2025-09-02 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8185595-f1a3-3e44-840d-a97912b957d9 | -12.74948 | -44.41134 | 2025-09-02 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e60c9923-8546-385d-bde6-2521497d89f1 | -11.9645 | -45.79696 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2219bf2d-1f94-335f-94c4-338f36e571a6 | -11.08948 | -44.62912 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 271.7 |
| 190558c3-4616-31d7-ae74-27df66dbfe1a | -12.76223 | -44.41397 | 2025-09-02 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f77771c4-67d6-3bbc-ae68-2ee536fb1b15 | -11.09487 | -44.63662 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1fff6157-aee9-38e8-b036-a14c07649665 | -16.07662 | -43.62397 | 2025-09-02 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0799681e-9fea-342e-8c6b-055e99e290aa | -12.75475 | -44.41804 | 2025-09-02 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb70aa4b-48d9-3286-8cd1-b972ef5f29ce | -14.4958 | -45.9503 | 2025-09-02 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f15ef12-bb9b-30bb-9280-723dc6a5bcfe | -11.09622 | -44.6479 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4ebc7c84-20d3-321f-a597-37dbf5eb17df | -14.04945 | -44.54958 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68362463-66c9-34b5-87ac-27432ac2aaf4 | -11.89679 | -44.88923 | 2025-09-02 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be185734-6748-318f-913a-6ba176e960b9 | -14.25974 | -45.24839 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c22260fa-8f21-393b-b889-fc6b1958b20a | -14.73513 | -46.74893 | 2025-09-02 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3d69a39-eb29-3bac-a370-f321634c5c5c | -11.09857 | -44.61834 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4ceefa47-7257-392e-8022-275a31c44f9d | -11.09125 | -44.65453 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 14c718c9-3856-3383-8aca-0b5d4af0485b | -11.05508 | -45.39359 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eb66942e-c51e-3462-98da-c9404113c896 | -14.489 | -45.94908 | 2025-09-02 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 175ccd02-62f7-32c1-a524-cfd200a5a2f7 | -11.09614 | -44.63035 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 271.7 |
| 0f00e5ce-faf2-380f-af87-ea9aeeb2397e | -15.80487 | -43.56986 | 2025-09-02 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c051896d-c595-3355-b2b2-601cab69bc29 | -14.261 | -45.24257 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88d9234a-2513-3d2c-9e92-86b31aa6589e | -11.09973 | -44.61264 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| b3a3051a-94d9-3917-a9b1-eb5dae7dfcea | -14.04839 | -44.60032 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f708930b-fdb2-3466-a30d-c0136ceac25d | -15.43577 | -43.31493 | 2025-09-02 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ae13b21d-d225-33ce-a063-d2862c25bd23 | -11.09377 | -44.65964 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 48b99bb6-9405-3a46-b9ce-9e86d8bee84e | -11.09874 | -44.63586 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 219ffd48-43f3-3cc8-91c6-f9293c456e86 | -11.37812 | -43.56737 | 2025-09-02 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3174e5a2-2103-304a-b4bd-33d8836f4828 | -16.07851 | -43.61907 | 2025-09-02 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64818d78-1ed6-3253-8356-0928bbd4b7c2 | -14.71929 | -46.75391 | 2025-09-02 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a6ef50c-fa98-3f1d-8df5-71a46dbac2ef | -11.09007 | -44.66037 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 636e3c80-b3e0-3257-85df-3653bd000bfc | -11.10005 | -44.62957 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 64dac4bf-777d-3058-9e87-80a71a430b5d | -14.72635 | -46.75525 | 2025-09-02 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e16b9078-bd0a-3e24-b9c4-cfcbfe7d57ce | -11.10252 | -44.61777 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| cc46217c-c443-32e9-9f2d-69bc85ca9b6f | -11.1067 | -44.63087 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| efef8ee9-b226-3b83-9efe-415b199ad8aa | -11.97635 | -45.87831 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 46a31cfb-87e4-39e2-970a-c9453feb85b5 | -14.0546 | -44.55639 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbb30292-1bc5-32b9-842c-32520d5b43aa | -11.97336 | -45.86997 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16b12490-6780-3aa9-bcc3-167cd05827fc | -11.97488 | -45.88521 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| be35f8ac-c956-30f9-9294-4f4f82d17211 | -11.09193 | -44.61704 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| f14330ee-ddbd-385a-8f5f-ba32dd113265 | -12.55724 | -44.78679 | 2025-09-02 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 126eb96a-c4b0-3575-9468-9713a9fda104 | -16.63254 | -44.591 | 2025-09-02 03:25:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 672c53cf-5167-3490-82b9-f9284027f388 | -11.1052 | -44.61971 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f423dac2-d091-3cec-b032-2b059ba50ae3 | -14.27155 | -45.25682 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8912ade3-5e4b-3a8f-9b87-a4fb44728c58 | -11.9708 | -45.86998 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5fe6a273-022b-3b42-8b6e-40cb8c3a6e8e | -14.26501 | -45.25551 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ca91103-63a0-350b-b22b-dbdd38628469 | -16.07764 | -43.62315 | 2025-09-02 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05a3ca6a-c783-3346-a473-db0815e911e2 | -11.10541 | -44.63707 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 8929546c-ade1-3093-9faa-b236aa47c522 | -15.78825 | -42.12933 | 2025-09-02 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ad763f5-1fd3-3974-9cd6-fd3646d895fa | -11.05555 | -45.38688 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f11e00c-c61c-3903-a3d8-1f6ab8b9c04e | -15.79913 | -43.56862 | 2025-09-02 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad824258-82e9-344d-8205-975f5bad14e8 | -11.09244 | -44.64867 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bf2f6e28-cd7c-3783-91cf-1399ce8d9814 | -12.56378 | -44.78808 | 2025-09-02 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3493aa05-d5a4-37f8-93e8-75990a576988 | -14.49365 | -45.95207 | 2025-09-02 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3684e7ae-e298-3936-a1dc-ff3c35dd5e24 | -11.10793 | -44.62498 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 39c28059-54b5-368a-b4f3-c0d42334baef | -11.048 | -45.14788 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 268f7514-43b3-30c9-ab28-9800cedf5b4c | -15.78756 | -42.13273 | 2025-09-02 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cb1e8913-9249-36b5-a422-a7c168096941 | -14.48829 | -45.94421 | 2025-09-02 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2c340848-bee3-31f6-a16d-f3367c4724dd | -17.23804 | -40.92497 | 2025-09-02 03:25:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a10d750-2092-328e-b6ac-d49298f40982 | -14.04955 | -44.59492 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3adabdef-19e2-333f-9d72-1c267101a896 | -11.06103 | -45.39515 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e117c495-e807-37d9-a162-b4f1bf63ca1d | -11.10403 | -44.62552 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| dc9a0ba1-899e-38c1-b156-3f4dbcf3c9b0 | -11.10131 | -44.62355 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 84b5e221-2e67-30e2-bdef-88a583734838 | -11.09747 | -44.64193 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 79776204-3980-3bc5-b59a-e2fdd6a60cc6 | -11.10702 | -44.64496 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 392c436d-26ea-38af-ad51-20794a2383eb | -11.10281 | -44.63157 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c068ad40-18b3-3ce4-9604-7caffd39ee64 | -11.09309 | -44.61128 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 1736072b-e701-3d4f-bced-c9d5bf8c133b | -11.04197 | -45.14413 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3631c940-999b-3204-a724-767aada760c7 | -11.10154 | -44.63786 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1823613e-a84b-3539-9373-d724813bf827 | -16.07747 | -43.61988 | 2025-09-02 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5ca2c4c-1cf0-3315-94e1-e3cc849ad05a | -14.26627 | -45.2497 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09a3307b-f943-3457-bcee-ac9ffef47dcf | -11.06242 | -45.38857 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5cf83e09-61f9-3170-96d0-0b7e1c827346 | -11.05642 | -45.38709 | 2025-09-02 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9f7d0088-2c9e-338c-9871-067ba1ba31d9 | -11.09675 | -44.66159 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fcbb56e8-a7ee-3ba1-8441-4e8263a35961 | -11.09791 | -44.65581 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a488b364-a91a-3e3c-96d1-d5df481c0429 | -11.96778 | -45.86157 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f6476d-929c-3b57-b5ef-abbb4a0b0bfa | -11.08698 | -44.64143 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 5a077c64-6d7b-33a4-885e-fe2b6a419b9a | -14.27282 | -45.25093 | 2025-09-02 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 10c0ab3d-401a-3434-aebf-b0953173500c | -11.10033 | -44.64384 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| bddb4ecc-cc2a-3de6-9eb9-74c15ea2ede4 | -11.09073 | -44.62295 | 2025-09-02 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 271.7 |
| 7996204a-0718-3612-b03d-adbd81351977 | -11.9705 | -45.88379 | 2025-09-02 03:25:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 757b2c94-dcfd-3f60-b35e-450464c87068 | -19.82206 | -45.00602 | 2025-09-02 03:28:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d69fa57d-18e1-378c-ac97-29ce5f0d1514 | -22.39414 | -47.17975 | 2025-09-02 03:28:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README14.md)
