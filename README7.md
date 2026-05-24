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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6edcdb96-d7eb-3021-98a0-d0c7e9ecd5ba | -14.01348 | -53.35782 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89577d2a-385a-3c75-831b-8a464fb179e3 | -15.0988 | -57.62565 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a031f28-9a76-3087-980d-d0cb2dbe1597 | -15.10211 | -57.62621 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a71aeb53-705d-3ecd-a847-1e64be484358 | -15.10268 | -57.62264 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 145fb850-91ba-39d1-831d-7af632fb3fbc | -15.08055 | -57.63357 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e986ced-83d0-319f-9ec8-0ba2923ce5f0 | -14.707 | -48.3372 | 2026-05-24 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eed44dd-1971-39d2-96c7-bc927a3187ae | -14.7381 | -52.66032 | 2026-05-24 05:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f9293b4-4976-3cf1-b5df-603114d48e52 | -15.08774 | -57.63112 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d5d1ad1-0998-3f5c-ac44-266451507aac | -16.86832 | -52.43946 | 2026-05-24 05:10:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24f43871-6fea-3506-827f-743639aca58a | -16.43313 | -51.77736 | 2026-05-24 05:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e990c54-5dbf-3954-b3c8-dd35a733a0c2 | -15.08717 | -57.63469 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fe9eda-1534-3704-b77e-b22b00249aaa | -14.7718 | -52.68201 | 2026-05-24 05:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cb69486-a87b-3609-ad9b-0169857ffe20 | -15.0833 | -57.63769 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89115012-c18c-3bd1-9fe9-80d2dd75cb0b | -12.55345 | -57.16443 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc286d1f-bcf5-321d-afe3-73ea6e2f79d2 | -12.55078 | -57.17535 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62327f73-c6da-34cc-b8a9-be36b02c61ba | -12.55139 | -57.16959 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66b55a33-4ab0-3183-9222-a27bbcda3165 | -11.54902 | -56.9381 | 2026-05-24 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91908a91-0218-30df-8932-0ed9dad5d075 | -9.57877 | -63.50006 | 2026-05-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 745b5f55-5df1-337e-b84d-002735303b9d | -9.74418 | -63.3361 | 2026-05-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc5d2aa2-9765-352d-826a-9730c4f69832 | -11.54712 | -56.9551 | 2026-05-24 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78ad0cac-f771-342a-a9e8-b0fcf2811a53 | -9.74032 | -63.33482 | 2026-05-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 053f1910-5bb0-3565-9f61-6c8220316093 | -4.43562 | -64.91321 | 2026-05-24 05:55:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df521dce-73ab-3bc4-b0db-f1aae49be599 | -11.17703 | -55.92112 | 2026-05-24 05:55:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8c704847-237b-34bc-bd2d-217e8c901b52 | -12.55148 | -57.18177 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fe8f263-32bc-3c01-98f1-fd4b02222cb1 | -11.53988 | -56.96008 | 2026-05-24 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93ab851a-1486-3183-b4ac-343282960e65 | -11.54776 | -56.94938 | 2026-05-24 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03a895d1-54f2-3d24-bb08-702f5f86a0bb | -12.55017 | -57.1811 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81c70106-8f43-3b58-8395-a23b2a732667 | -9.73996 | -63.3355 | 2026-05-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5b9f3f-ab1e-374b-b668-415a06e01c77 | -12.55278 | -57.17031 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ead67100-7911-310a-8f38-93ba342b0f16 | -12.55213 | -57.17602 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d4ca759-2ae9-3e14-9fbe-3ae1d07b8bf9 | -12.55203 | -57.16366 | 2026-05-24 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 148d0739-5426-389d-b119-4fbbf98745a4 | -11.17778 | -55.91412 | 2026-05-24 05:55:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9976b09e-a328-3007-a527-b05e37dc0225 | -11.54839 | -56.94372 | 2026-05-24 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07733f4e-ea55-39c4-b3fe-b6ca7cec373c | -11.17875 | -55.9166 | 2026-05-24 05:55:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b1d26c07-fac5-34ee-addf-3e2f8e21b446 | -11.54647 | -56.96087 | 2026-05-24 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 901247e3-c597-3abe-b339-f4ab7fb3be3e | -11.17797 | -55.92354 | 2026-05-24 05:55:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 066beb89-5a57-3677-b34d-44486d14aad5 | -9.74455 | -63.33543 | 2026-05-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1479b987-1dba-3100-b399-4486bd9577c3 | -12.88986 | -58.18283 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9359dac-847a-3446-acf3-5c2bf0808686 | -12.89093 | -58.17312 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| acf089dd-b040-3cff-ad4d-21d141820d25 | -15.09717 | -57.62529 | 2026-05-24 05:57:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bca1000e-3b5e-3419-bc0e-d19baab544b8 | -12.89147 | -58.1683 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3c14f61e-d6cf-318f-9f73-71639c4e7ce9 | -12.8904 | -58.17794 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4ae6588-b46b-3a35-9ce2-8494be68d3f3 | -15.08404 | -57.63723 | 2026-05-24 05:57:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57f35915-9184-3de9-9565-f26d597d32fd | -15.10376 | -57.62614 | 2026-05-24 05:57:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfc7dd11-e732-32cc-9ce3-aa7ed30fee8f | -12.89715 | -58.17391 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ef374eb2-08c8-3632-abb1-ad5edd86489c | -15.09841 | -57.62707 | 2026-05-24 05:57:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcd0312f-8dbc-3ccf-a1ab-22e0917d4359 | -12.88471 | -58.17231 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfb65811-be05-30b7-a203-b2a372f779d8 | -15.09122 | -57.63216 | 2026-05-24 05:57:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60137369-4860-3e58-90ef-2abd7a75f25d | -12.89662 | -58.17873 | 2026-05-24 05:57:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98d78e2b-132b-36da-a802-e286b5ca619a | -15.105 | -57.62786 | 2026-05-24 05:57:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f819ad51-4f73-3aa6-a34f-9a37a918ac49 | -5.47576 | -38.23943 | 2026-05-24 11:34:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 3340cab5-5b1e-37a7-912e-eb5b3bcaa063 | -6.07896 | -44.007 | 2026-05-24 11:34:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2205494f-5dd1-3e81-b704-950de2af83c9 | -3.95482 | -43.13062 | 2026-05-24 11:34:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f9efe7a2-4778-3881-919e-664305ba4597 | -8.86178 | -46.93007 | 2026-05-24 11:36:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 596a274f-fbb1-301e-9eb8-fadcee30deb0 | -8.87263 | -46.93191 | 2026-05-24 11:36:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 68976fc9-1610-36b1-87b9-96a66f2a032d | -13.43727 | -45.83244 | 2026-05-24 11:36:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0aeaf5d6-911d-317d-a447-11aa96dfb5ba | -8.14454 | -41.1833 | 2026-05-24 11:36:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c7183c43-f568-3904-b503-0864122ef1ab | -7.46889 | -45.50033 | 2026-05-24 11:36:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 849e5b72-d845-3c5c-b61e-ea76d5f04bf8 | -21.06208 | -40.87522 | 2026-05-24 11:38:00 | TERRA_M-M | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 61d6af67-eafe-3ec9-9f54-fcf800a3d117 | -21.06041 | -40.88906 | 2026-05-24 11:38:00 | TERRA_M-M | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| de048e2d-9606-3e09-b6bc-e7a1766476bb | -21.05595 | -40.88031 | 2026-05-24 11:38:00 | TERRA_M-M | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| c841025b-9532-3649-8256-df81ba878aef | -18.10848 | -46.8707 | 2026-05-24 11:38:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b8a95dbf-b1a6-300e-8862-d54170c65926 | -8.8697 | -46.9437 | 2026-05-24 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 591528b4-b184-3657-ace5-23c9ca26311e | -8.8697 | -46.9437 | 2026-05-24 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 43c51939-6c90-3801-9c97-acdb61d8ef5d | -12.5372 | -57.1614 | 2026-05-24 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 576afbb7-fe14-3674-8f02-ff238c66dd90 | -12.5372 | -57.1614 | 2026-05-24 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 9b0e5880-ed6e-386c-b9fa-789055e7dab4 | -8.8697 | -46.9437 | 2026-05-24 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 19e0976a-be0e-367b-b7c2-9f0c81506ba4 | -12.5372 | -57.1614 | 2026-05-24 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 1b5b73f6-df05-3a74-8100-87e4d02b4db2 | -8.8697 | -46.9437 | 2026-05-24 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| bf553490-aa99-374f-9221-071141a27b01 | -8.87 | -46.9215 | 2026-05-24 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a8fa094a-d73d-3ab5-9127-5ddbeaa5a7ea | -12.5372 | -57.1614 | 2026-05-24 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 079717ae-37f9-3a90-8bee-7f571549b826 | -8.87 | -46.9215 | 2026-05-24 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 53f3c6a4-cf6d-338c-babd-7e424041d280 | -8.8697 | -46.9437 | 2026-05-24 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3e1676d4-e4b1-3363-a6f3-69fc8d5afcaf | -12.5562 | -57.1597 | 2026-05-24 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9eff7d6e-d2a1-3e6a-9b0e-33a0eb649a76 | -12.5372 | -57.1614 | 2026-05-24 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 01c1be16-c636-33a8-ba9c-27c3ae2ee0f0 | -12.5562 | -57.1597 | 2026-05-24 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 54c3e112-bad5-3f61-97fb-68cf372c6ec8 | -8.87 | -46.9215 | 2026-05-24 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 082b9522-b9fa-32f3-9dbd-f3c3091cbccd | -8.8697 | -46.9437 | 2026-05-24 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 144fb619-7a6d-3048-ba1a-05e391e6fced | -12.5372 | -57.1614 | 2026-05-24 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 7efd46b0-e8cd-39ac-9d11-570bc54a56d5 | -8.87 | -46.9215 | 2026-05-24 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 47fa3277-ee73-3507-b461-a2fd8b16c52c | -12.5562 | -57.1597 | 2026-05-24 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 7625e83f-1142-314d-8a8a-9ae1fd594849 | -8.87 | -46.9215 | 2026-05-24 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b76593f5-23d6-326c-9d03-f2965a831778 | -12.5372 | -57.1614 | 2026-05-24 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 89ebdc7c-f197-30d8-a647-70214579098e | -8.8697 | -46.9437 | 2026-05-24 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 708a80c2-fcc2-3f12-a85f-fa5900d1e373 | -12.5562 | -57.1597 | 2026-05-24 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 1e90e9ce-6a5f-32ad-a424-dab8079cdecb | -12.537 | -57.1814 | 2026-05-24 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| aece233d-ed04-325f-ae88-5600d78f4ea3 | -12.5367 | -57.2014 | 2026-05-24 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 674be8f9-d2ea-32ea-8258-564beb227dda | -11.5557 | -56.9632 | 2026-05-24 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e1c143eb-514f-3c25-b755-a129abb1209b | -12.5562 | -57.1597 | 2026-05-24 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| de01741e-8ec8-3c52-9708-f27456794423 | -12.537 | -57.1814 | 2026-05-24 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7426a9b3-01d6-33fa-83ac-32420c19f04c | -12.5372 | -57.1614 | 2026-05-24 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 6f190c9e-7843-3f92-8d6e-ea7b0a22fcdf | -8.8697 | -46.9437 | 2026-05-24 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7e524db5-d3a0-34fc-9e54-ca870e7603e0 | -11.5559 | -56.9432 | 2026-05-24 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 054a0849-dfe1-3f5f-9a5c-bc8f68f23ea9 | -8.87 | -46.9215 | 2026-05-24 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b68dc2ba-1097-3e4e-aa50-e653aaa0c732 | -11.5559 | -56.9432 | 2026-05-24 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4fb5b040-3104-3f0e-8d85-3153ff2384a1 | -12.537 | -57.1814 | 2026-05-24 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5804fb8c-5de2-3ded-9b55-af300bce9763 | -11.5557 | -56.9632 | 2026-05-24 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d31edaf5-ab0c-34c0-ad75-8019800f2614 | -12.5367 | -57.2014 | 2026-05-24 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 880394ec-d235-3472-ac8f-2d5ef0f366ba | -8.8697 | -46.9437 | 2026-05-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 14d73163-7981-331f-900b-9ac9f2a8e778 | -12.5562 | -57.1597 | 2026-05-24 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |


[Clique aqui para ver as próximas entradas](README8.md)
