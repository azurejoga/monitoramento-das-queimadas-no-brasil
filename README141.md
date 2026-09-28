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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e53fbd-3a1f-3281-a067-af7f48308147 | -15.18258 | -46.17075 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2eb74f63-cf52-3ad3-a66d-d7de5517aef3 | -18.09397 | -44.37418 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 64d8170e-0a55-3d15-8a30-79f90313c695 | -14.6399 | -52.11092 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 05dc5edf-ad65-3ab6-887c-678b6f462857 | -13.92667 | -47.85746 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fb5e91c4-ffe6-3a90-bda6-b783419b6fee | -15.22382 | -46.18787 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f4c81df5-070e-37c5-a4f9-514835431d3e | -14.48443 | -53.64309 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ae7f264-76e5-3f24-84be-b7f35429cb38 | -15.15994 | -43.59671 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ea473842-4661-3af1-a829-cb2c1eb3f3b3 | -15.07064 | -54.60733 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b7d9fd5b-2d37-3f03-a900-d61a7c8ec3fc | -15.20545 | -46.19136 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 3e6194b3-77a9-33f1-b13d-023f6091e1b6 | -13.08455 | -47.44168 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 707829e9-9302-32ec-8208-18b3ab422821 | -13.15895 | -48.55606 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a753adff-8091-3bbb-8217-33eb5bd85ba1 | -15.19447 | -46.18346 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| da879cdb-1058-3e4f-b710-6f7754a4e79e | -14.32201 | -44.82185 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b8ed38ef-6d5d-3b82-bdc1-29e16fad507f | -15.19452 | -48.21774 | 2026-09-28 17:07:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7003e8ab-bf19-3d14-bbb7-7a682e2b4419 | -12.0603 | -45.74656 | 2026-09-28 17:07:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 13921ea9-3722-37c2-8287-70e953aa249d | -13.93529 | -45.13418 | 2026-09-28 17:07:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3ee5fc6-7330-38a0-86c9-b2c0a82eafa6 | -12.84013 | -43.39624 | 2026-09-28 17:07:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 79f25364-cd7d-35f6-a526-87f2afbc0550 | -15.19362 | -46.17889 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fcc561f1-368b-3318-a233-80fb64d14e52 | -15.62538 | -43.51881 | 2026-09-28 17:07:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 9cd28ba2-8720-3670-9f2f-5393dd2c88b4 | -15.2167 | -46.17756 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3251ea30-944f-385b-b938-9637ce4c116e | -11.9001 | -47.0148 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7e5c7f93-8261-3123-869b-dcf716aea4e6 | -12.79349 | -50.58865 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a0f75c44-ae1e-3e63-9424-4300bab0cec0 | -12.67868 | -45.0201 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0f832843-4a6a-3442-8fd5-54e1a02ff7fb | -15.93738 | -42.33744 | 2026-09-28 17:07:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a34a22c5-9cf3-3da9-bea3-b968dcc1e798 | -14.40239 | -41.02688 | 2026-09-28 17:07:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bbd5fb62-f94d-3a95-b823-773dcc48568f | -12.69695 | -47.32554 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8653a99a-77f5-3e08-bd40-93c6d0f67060 | -15.08461 | -48.32901 | 2026-09-28 17:07:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| e8fcc7e2-ec91-3df3-accd-9a2431f93757 | -12.00033 | -44.93205 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60d001de-1c60-377a-9d77-cc145f573bad | -16.54688 | -42.37033 | 2026-09-28 17:07:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecee7656-860b-3087-ae90-4f92a3b9a3b3 | -13.90408 | -53.66926 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| dbd56b0c-edb8-33a8-bb95-76a3b2e932db | -15.7333 | -44.84417 | 2026-09-28 17:07:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 753ae71b-a098-310a-bf0e-a60735a8be94 | -14.63039 | -52.11631 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 198d42d9-e639-3c28-84c3-f26899d77929 | -20.83305 | -57.70055 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 178c2af9-b9a9-36cb-9131-5658e382b776 | -17.85677 | -42.76152 | 2026-09-28 17:07:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 74603771-d9a9-37db-94ef-368dd3cee3db | -12.55192 | -42.04603 | 2026-09-28 17:07:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 93cc6be1-9051-320f-b529-db8b293ea76b | -12.434 | -44.15822 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8d2e4176-4456-3e32-b99e-db1ff530b10b | -13.48533 | -48.6023 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 27562dac-8c40-3e06-b057-eab6eab69dd8 | -18.65614 | -43.04092 | 2026-09-28 17:07:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b708e4f4-8b1e-3365-8bb1-9930f3b52d09 | -15.13097 | -43.62159 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 2e53eb41-650b-3dbd-ab1a-cba4189853df | -17.96725 | -47.84357 | 2026-09-28 17:07:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 02f91056-36e9-33ef-834d-39aa4b8fa838 | -15.13499 | -43.6134 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 1595ed3e-9055-343d-8397-79f5d4ef08e4 | -13.81678 | -44.25399 | 2026-09-28 17:07:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 49658a0b-a167-35c7-ab8d-9fb1770b73bb | -12.90441 | -52.04486 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e024a0b4-f2d3-3d96-91f8-874825aff023 | -13.32274 | -43.94798 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 26726c8c-12e8-3c30-8918-8aa3109a15b8 | -12.75337 | -47.31599 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 717b4449-257e-3886-9c6d-c60a14d7a1b0 | -17.94541 | -47.01183 | 2026-09-28 17:07:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d5e9a36d-c789-3db4-a992-23612e0fb8f1 | -11.67834 | -43.50869 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4a60e625-00f9-33a2-887e-51ab2c3cfbf7 | -14.13453 | -40.6811 | 2026-09-28 17:07:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cace05b1-3451-3c58-95fa-5a961894ee73 | -12.9364 | -46.63678 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| a457c101-07d4-3f28-936e-1b92b1add259 | -17.89294 | -45.06196 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cb6038f1-139a-3c1c-a89a-6140d135d694 | -16.4265 | -43.29274 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 32.1 |
| e60ee255-7adb-352a-9970-7e8174ee9762 | -15.16137 | -43.60398 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 25.1 |
| a6f10713-37c5-3f12-9238-ab31e56e03b3 | -17.077 | -41.06367 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b998bd6d-fc02-3858-8bdf-c4f1bdad0cf4 | -15.45563 | -53.95451 | 2026-09-28 17:07:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0995d389-05e8-3ac7-b966-9ecd8a11a9ed | -13.31722 | -43.94896 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 7bc7267b-2923-3574-92f3-5fa426147b18 | -12.68844 | -45.01482 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3b95afd0-d8c1-3415-ba9b-8daacd2401bb | -16.8903 | -46.89945 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b7736a47-f472-3fb2-84a8-8f0f080f943b | -13.37278 | -44.02947 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fa0a3420-3bcc-378d-a193-9a8a22c6d969 | -13.96913 | -53.96328 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 90c67207-cc03-3235-88af-4f04fe49d5e4 | -17.75073 | -47.69371 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 5445103b-1a1b-32f2-a386-1ee5f01cefa0 | -14.44377 | -40.74857 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 1517d26e-4f44-3dca-909e-88b88ac94d72 | -15.15952 | -43.62322 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 39d339d9-2cb6-3f51-827d-62283e38d618 | -20.48086 | -54.76248 | 2026-09-28 17:07:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ca21841-8981-3d1a-a8cf-6c11dc463171 | -14.1168 | -46.29086 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6bd7ac02-cd45-31f0-a780-ecd4bcaa3a5c | -12.56572 | -44.88234 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7b2b459-7388-3b99-b04b-39b500d4b8ea | -18.78425 | -48.75567 | 2026-09-28 17:07:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 50b5e8f7-3169-3691-b53e-51a94bf03933 | -13.58387 | -51.44403 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f4c035f4-802f-370e-ab58-880d485a940e | -13.51126 | -46.90352 | 2026-09-28 17:07:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 1ebb0491-bf4c-3faa-a9fd-fec776dd968a | -12.62665 | -47.26801 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 98d19bdb-53b2-3442-824d-ec9a8ec3449a | -18.59035 | -43.77277 | 2026-09-28 17:07:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 41bdd5f1-e469-3a00-b4a1-8c68083a1694 | -13.90462 | -53.6728 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3576f87e-3c4c-3d23-98ea-6819e809763a | -13.96895 | -54.00681 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4fa3f322-aca1-3758-8dce-2260f37c03e0 | -11.34947 | -43.42523 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d00ba7f-0784-3b72-b508-26f7d4541046 | -19.18751 | -46.85326 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4087a12b-71d6-39e0-9fb6-3e0abfb6adc7 | -12.61853 | -47.2742 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3a7dbe2e-36e6-3b6e-96b6-89a7982a2028 | -14.71853 | -41.59945 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| a4ecbfc8-af36-3d7e-8ba5-c73074937475 | -11.37958 | -43.39187 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f2881e5a-805d-3887-9ece-1581eef07962 | -12.63113 | -47.2672 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 84f4d159-4fa5-3672-85c9-318a2c21c14a | -14.12418 | -46.30473 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 696348c9-3979-389c-8d70-7397b9b7989c | -13.45736 | -48.58535 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 95ce2e8d-59bf-37c2-9625-8e403fee9c91 | -12.94201 | -46.64114 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 80212935-0201-3ce6-86bd-7a74c028d0b9 | -15.46292 | -46.1511 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 53275204-3a5b-321f-9cd6-ccb0c15123a7 | -17.80874 | -44.42993 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 55cf580e-baaf-34e5-a1fc-b2d1a62d0793 | -15.22924 | -46.19332 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 315e9583-c663-37f6-b3c5-dee2eea089d3 | -13.07153 | -48.51054 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5044a080-97e6-3300-a306-ca1198c6f71c | -14.48112 | -53.64363 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c72d14ce-8fce-36f1-9fa1-d861fe00cfdf | -11.92159 | -43.74197 | 2026-09-28 17:07:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a614ab88-b1ea-33da-84ab-17d49c345867 | -24.66561 | -49.61623 | 2026-09-28 17:07:00 | NOAA-21 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6d2ae3df-8fce-3030-9548-6e33e438204e | -12.05184 | -46.47918 | 2026-09-28 17:07:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1c40fa5c-6c74-36d5-909a-94cda9413dc3 | -14.41717 | -44.38084 | 2026-09-28 17:07:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 048e656a-ae22-3769-8111-a86a248307a9 | -13.94125 | -49.0764 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 51057158-cedf-3183-b6a3-f62b2e9f2598 | -12.82649 | -49.6762 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7a905b6d-93ff-3851-b216-b4b91500c66f | -14.67154 | -41.83179 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 210ab38f-e048-39cd-a099-24e067820a17 | -17.75629 | -42.17492 | 2026-09-28 17:07:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| a9092aea-ca81-313f-b8a8-2c70426bb1cc | -13.94428 | -49.07069 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ad454965-4369-37b6-9c6b-4ea9679c38d8 | -14.80981 | -40.81468 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7f0c86f0-d93b-34db-beb5-a53347ed5136 | -15.06945 | -54.62241 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| dfc2d17f-c630-3a88-a045-10927faf9c95 | -13.16591 | -48.54787 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 359671b1-c569-3a82-832d-8e8604536609 | -12.55374 | -42.04091 | 2026-09-28 17:07:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 4e31c35f-8e53-33a7-9ac4-711a2c8ccf93 | -13.97663 | -54.01284 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README142.md)
