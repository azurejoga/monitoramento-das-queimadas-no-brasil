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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d8da8f4-a75b-3853-b13b-f0b2680d55bc | -19.90168 | -41.44178 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bb58e144-73d5-3c7f-9e0a-9b64b81234ad | -15.17745 | -47.97945 | 2025-09-07 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07edef6c-c415-3678-9744-0153fd71229e | -20.77125 | -44.45953 | 2025-09-07 04:21:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83e53a25-70a4-3699-a950-4aec5dae75ab | -15.23815 | -52.36995 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b9c465-ede6-3a52-b542-5cb1e0f3ed72 | -13.55123 | -48.11332 | 2025-09-07 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6858d818-e91a-370a-88e5-bbcbff18d9bd | -13.91827 | -53.97755 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6b7c971-a6b6-3af6-b94a-3d0ae4bed85e | -19.47048 | -47.7588 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c8776634-7018-3447-a70a-06cc382c36a8 | -13.82367 | -46.27521 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cabd029-76ab-3115-8fc4-25f5136a2203 | -13.45768 | -48.14775 | 2025-09-07 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8a9a25c-fdda-35b4-a105-cb1075e8b0f8 | -15.01113 | -48.00382 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 437966fa-cd19-3a3c-92f8-2b7c6dc2cf61 | -16.54048 | -45.0956 | 2025-09-07 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6fad0e50-b376-33e0-9c70-465fe69e46f2 | -19.41166 | -46.10218 | 2025-09-07 04:21:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8328a0d5-bbe6-34be-a458-f29928a18354 | -14.41495 | -49.68868 | 2025-09-07 04:21:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| afe68957-4d1a-3f52-94b1-121e2408cd8f | -13.67166 | -46.95555 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba3d38b2-d2aa-3d24-93f8-536edd6d1cf0 | -17.3626 | -42.64647 | 2025-09-07 04:21:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf6ad294-13a4-376d-9a1f-aa05e3e0c524 | -12.95201 | -54.78307 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be7f433b-8da6-321e-aac3-104bdf6ec4d2 | -13.71438 | -46.87881 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7c272cc-7545-3913-8a6d-c49af88ce5e7 | -13.73364 | -46.90741 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c10d1c1-efdb-364c-aa33-27f3dd6adadb | -13.90021 | -53.99556 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63cae158-d8e7-37fb-901f-ddb947e94ecd | -17.70481 | -44.48489 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8908e96c-b83d-314d-bc49-962c031d81ff | -11.16391 | -59.1628 | 2025-09-07 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0443de10-de75-371d-a3b1-19593b3765d4 | -16.3382 | -52.94666 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b08d2ab-fa3a-3873-adb6-174658a5120c | -19.11226 | -49.46108 | 2025-09-07 04:21:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb93fa65-acd7-3a6c-904d-e14958b179d2 | -16.9063 | -45.77963 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15e0cc52-8c44-345e-b715-9589e868e549 | -17.70718 | -47.65753 | 2025-09-07 04:21:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fed29f6-430a-3079-a583-714af5eeff69 | -16.92472 | -45.78242 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ee750f6a-f36b-3716-9ff5-b03a62c34023 | -16.7046 | -45.98656 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6144e4d7-9ca3-30a9-931a-bd08146fe73f | -16.92979 | -45.79461 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a7da279-74e6-3bf6-816e-08f4f284d19c | -14.85191 | -46.68836 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 440f168e-dd78-3300-9532-ad745761ef0f | -14.56419 | -43.72702 | 2025-09-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5eec2f2-5419-3904-b72a-ec0a9f2774ce | -12.94424 | -54.76899 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| aa738322-7a9e-37ce-8687-dc057cecf9ac | -18.02759 | -47.08834 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f1a5218-74a6-373e-9bfd-9d1435af3146 | -18.00641 | -43.48228 | 2025-09-07 04:21:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b5677c5-c8ac-3578-8a98-5811672edb41 | -14.56467 | -49.12544 | 2025-09-07 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9684c7a8-6b18-3f90-a333-3c6925f851ea | -15.83656 | -52.27714 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5e45fa8-b67a-3167-a355-2dd559e737d7 | -13.90495 | -53.99624 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b049c6f0-3082-3d33-a292-e379632e25f3 | -13.04103 | -48.078 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 451e3680-a36b-3bc6-bbf1-c0ab7ead3cfb | -18.37319 | -43.89426 | 2025-09-07 04:21:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 621f2e13-d2a7-3003-9ac6-22ba05b99e98 | -13.82312 | -46.27874 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5608020-8b0d-3c19-9cd0-134052c6beb6 | -17.68016 | -44.50548 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe883b2b-25f8-3c7a-bdfc-4dd4abf1539c | -13.74027 | -46.90857 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9322ae3-9e81-3da1-9b47-48c2fe225da1 | -18.66928 | -43.7963 | 2025-09-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2aa7eb40-5e05-3d24-8197-bdcc07db63db | -20.04255 | -41.22941 | 2025-09-07 04:21:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 97ea63d3-b0f9-3739-a487-27f234e0a579 | -12.93897 | -48.03764 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 250efccf-6c8b-3224-8697-cdf70fa35ad9 | -12.94869 | -54.77306 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 46101b54-ccb6-317a-8cd0-1e89483310e4 | -13.91728 | -53.98272 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f88e7033-a1ff-38fc-a3c3-1c081874c072 | -17.86385 | -44.33287 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfe52753-a9b9-3a83-a59e-b2cc7b29d89c | -13.28269 | -51.77447 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 167e4c4b-7a2b-3648-a2e5-432ff7dff46b | -15.37173 | -46.42666 | 2025-09-07 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51756e04-d566-3b78-844f-f69da5bcfae1 | -12.94914 | -54.79824 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7d6474e-df0b-3de8-832d-03f0c289b03f | -12.93557 | -48.03701 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b52dd22e-4ab6-3784-b0c2-d9c67bed2976 | -13.54844 | -48.10902 | 2025-09-07 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6a780e2-473d-33b4-9757-e41a05537447 | -17.22073 | -46.71217 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 218252ad-67b1-30f1-bbf7-d181a7f881c3 | -15.13166 | -52.35673 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c59a9a03-d11e-3393-8326-4b348fbbf82b | -20.53275 | -46.4418 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5c7899c4-87a2-3d6b-9567-30b208204267 | -16.58074 | -48.87295 | 2025-09-07 04:21:00 | NOAA-20 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22379928-d133-39d3-9a9f-27ff44cebed5 | -14.77802 | -48.12024 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f685c4d-dd7f-3740-8e70-bda9206c1def | -16.93594 | -45.77662 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b73dda00-3282-3426-88bf-61c36edf462f | -15.11927 | -52.3543 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb1abca2-2f8f-327f-ad80-bb7510c48af1 | -13.89448 | -53.99308 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96dee643-4998-3792-8a3c-662c840f3ddc | -20.04027 | -48.90572 | 2025-09-07 04:21:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 638def7e-1d01-3449-bf48-19bc3f2ce3e2 | -20.26235 | -44.53229 | 2025-09-07 04:21:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fcc91fe5-6f9e-3a47-9cb9-293b6d37ce27 | -16.53649 | -45.09891 | 2025-09-07 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f9ee051-599a-3768-9620-e31acfb3d6db | -19.89397 | -41.43232 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8c3b977a-ac73-33d7-8e6d-4733d732186c | -13.90398 | -54.00128 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcca3ad9-4be0-364f-a6b5-e64a7ccdf851 | -13.76952 | -52.76794 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24351d88-385b-30f4-8bf9-90a554a294f4 | -13.02338 | -48.07868 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b11f66fe-0594-32e3-8c00-deb7bf107409 | -16.32834 | -52.95287 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ded22579-5cbd-3c4f-985b-2896b5a8ab5a | -14.82151 | -48.1802 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 275e0d04-f285-3a1a-a819-a5546cb4ec7c | -16.69041 | -46.80554 | 2025-09-07 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b3c82dcf-d036-36c1-bd95-6f9677b99e69 | -14.59454 | -48.08153 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d2b25a5f-6248-3df9-8979-b45758a43b27 | -20.07823 | -43.74945 | 2025-09-07 04:21:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f27a8926-4a19-32f8-92ca-196d7caa9acb | -13.00661 | -54.84623 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2b74b42-3b19-3b72-a3ae-6154e22a6c82 | -15.1747 | -47.97519 | 2025-09-07 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 794b4013-fac4-3358-9c76-d2516ef2535e | -14.58396 | -52.14237 | 2025-09-07 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bae0b32d-ebc8-38d4-a420-22b5e19bc08b | -17.71193 | -44.48581 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcae9bee-10ab-3d93-9de1-6affb6360f87 | -19.88826 | -41.43224 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 668a5971-3c18-3652-977b-78e9e4fbbe85 | -13.01252 | -48.08075 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3157188-7db4-3103-8041-da149ff9659b | -12.78256 | -52.95871 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb8a351a-119b-3220-b726-55cff69a317e | -14.82242 | -48.19574 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 100e848b-7676-3287-8bf5-a6b58738cc26 | -14.84472 | -46.69082 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2e8f028-6651-366c-9b47-0a4fd1b9cb14 | -13.83805 | -46.24852 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 934d38c5-c436-377d-af31-8afc4c8f2a32 | -15.53796 | -42.65759 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9e2673fa-4858-3c54-bef9-05d3e747a997 | -16.92202 | -45.78975 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6070a63-3917-3dfc-8252-25c68eb53614 | -13.04076 | -48.05828 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9f54a82-f76e-3bc7-bb24-72eb0e00b161 | -14.5814 | -48.09825 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997fd9a8-8c95-3cdc-a67f-ef12004a4c8f | -13.79234 | -52.74103 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3176b78e-88fc-378f-94e8-c0a76af68e5c | -18.49712 | -49.5077 | 2025-09-07 04:21:00 | NOAA-20 | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65be4694-fbe7-3999-80ba-ceabf130d3b4 | -12.81513 | -56.52369 | 2025-09-07 04:21:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca7d7bd0-c7bd-36df-b01f-f6a8ff97ea9d | -18.14785 | -45.23922 | 2025-09-07 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 440f7756-45ea-3e0c-9542-75e461e4f56f | -16.90576 | -45.73764 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f74965d6-4693-34ba-bb1c-6efab52db922 | -19.47264 | -47.76668 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a4c9a2dd-a8c4-32b5-a745-74986be9487d | -15.13577 | -52.35764 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 425bf53e-ab9b-3c99-a255-758d1c308e5d | -15.10156 | -50.10701 | 2025-09-07 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e08f44b8-6d70-368e-88ff-471b7da318c8 | -16.34094 | -52.95538 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ea59931-f0b6-33db-bbab-b9658cb20536 | -14.58504 | -48.07596 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1038047-12b9-3dd0-852c-7d21debf7535 | -16.94379 | -45.77024 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92fbd00c-2901-3b54-8e6e-904cec72bc6e | -15.83768 | -52.2731 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 908a485b-74ff-3fb9-80a1-7adf1acb277c | -19.21351 | -46.81332 | 2025-09-07 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2617b156-fb31-37cd-8239-09c62bb5ed9a | -18.03366 | -47.09313 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
