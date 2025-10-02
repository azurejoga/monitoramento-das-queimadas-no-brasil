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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0f584bf-a390-32b2-a338-ddb4d74feb67 | -11.87886 | -51.22986 | 2025-10-02 12:38:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 59cfff3d-51bf-3984-bd94-3dce4ca19c16 | -14.91979 | -47.25005 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 6efd2afd-b5a4-3e83-828c-bbf3b99fde48 | -14.97627 | -46.86171 | 2025-10-02 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3b74c069-dc40-30bd-8794-81c369064eaa | -11.06529 | -47.81107 | 2025-10-02 12:38:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 7f161422-a13b-3c51-b040-77134b72824e | -10.50207 | -49.5418 | 2025-10-02 12:38:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9951a437-1e32-3ef3-9c27-2ce0b3e39da9 | -12.58831 | -49.89555 | 2025-10-02 12:38:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b2967a4a-4391-3eaf-8f40-69f92f5b0bec | -11.92469 | -47.88284 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| c72751f8-554e-38b3-9a54-0faeeca52e34 | -12.65916 | -46.8681 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| ee0b13e7-25ee-33e8-99c6-28ddbfc3da75 | -13.20856 | -47.84916 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 854ace82-1fd6-3b69-ac78-14bb8cebac9c | -14.23647 | -43.5082 | 2025-10-02 12:38:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1da064b7-d544-326a-9d2f-e84f9e5fcf68 | -13.36379 | -48.07895 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b858c936-66e2-3eb8-9ec3-df1fd893fa1e | -15.27271 | -49.30508 | 2025-10-02 12:38:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 13897d37-8e57-32ab-be37-0688fd3cad79 | -12.91349 | -46.91493 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8a01aa30-f17d-333c-9c2d-ffa4d463202c | -12.42252 | -45.0352 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0aa45249-54bf-3324-9824-74c7205f5026 | -14.43433 | -46.13095 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| aabd9c2a-5b01-3aa0-ab8b-e7f09f51f915 | -11.18729 | -47.28199 | 2025-10-02 12:38:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| fcf8561f-20b7-3611-9523-24a712c7a0fc | -14.35514 | -43.84073 | 2025-10-02 12:38:00 | TERRA_M-T | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 13c8cc7d-f118-34f8-bc3f-3db9940e89eb | -13.69805 | -48.62453 | 2025-10-02 12:38:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5c9a82bf-5ed3-35dc-9db9-4c589c4af43d | -14.32284 | -45.88295 | 2025-10-02 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| c736a7bc-6d7c-3eb5-aa0a-aa005422e40c | -12.7635 | -50.59016 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 391e91c4-1aea-316a-a82a-1ec9ab381967 | -13.13871 | -47.86971 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5180e36b-f5a2-3365-8501-4c49a0bbaeb5 | -12.19661 | -47.80611 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 36b0b155-898b-377b-8929-f5175e88aa9a | -13.97556 | -48.14405 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 50224c7c-7a56-35ef-9436-0467f5542829 | -13.23258 | -48.50392 | 2025-10-02 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| d5aa5cf6-63d3-3d88-a29e-3aa787c246c4 | -12.19853 | -47.81749 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2241801a-95cd-38ac-bd3a-e6be573e28dc | -16.05357 | -45.71156 | 2025-10-02 12:38:00 | TERRA_M-T | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 818859ba-d94c-3cf2-940e-b4213a3730ac | -14.60458 | -48.33058 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6cc611c8-7291-3f0a-ba91-dfd9f648015d | -12.90081 | -46.91319 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 81c8aa45-dae0-30aa-b34b-a2119a074369 | -14.47786 | -48.42457 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| afb3e772-a641-3f4e-8729-30ed7cced95d | -16.03956 | -50.89277 | 2025-10-02 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| fc95be7b-f508-344f-aff0-122ff389181f | -13.00576 | -45.22172 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 350.9 |
| 0cd7221e-d42f-3c09-8610-0ff6b8d7a9c3 | -17.58942 | -44.2353 | 2025-10-02 12:38:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 8b3b6961-87a7-3b30-bd2a-cf1f9ad3662f | -14.19563 | -46.1401 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 17a41606-c889-3dcf-90f6-aadb30aab708 | -12.86416 | -54.7168 | 2025-10-02 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 596608b5-4eb6-36f9-bcad-d6947433f504 | -13.33404 | -47.21265 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 32.9 |
| a47ed117-56f4-36c0-99ff-daa6c2892197 | -16.05081 | -45.73942 | 2025-10-02 12:38:00 | TERRA_M-T | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 307.0 |
| 398ed39b-209a-35aa-9a3d-dca3c3ff61d4 | -11.27868 | -47.84864 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 31d9b540-2fc5-3d50-ad36-c4bebfb0c58d | -10.69216 | -48.57071 | 2025-10-02 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3145855c-ec9b-32fb-b12e-7607013258bd | -16.03661 | -50.91593 | 2025-10-02 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 89df3cca-6917-35a3-921d-c1cd8ac367cf | -15.01477 | -56.04572 | 2025-10-02 12:38:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b0ba539-c5e5-3303-affc-086b7a916eda | -11.9175 | -46.74282 | 2025-10-02 12:38:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 72e55eeb-2709-38b7-ac85-276985288690 | -14.706 | -49.61184 | 2025-10-02 12:38:00 | TERRA_M-T | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c8798d7b-e769-3c35-8cdf-c8fbddcfffd1 | -11.48691 | -44.99763 | 2025-10-02 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| b56b39eb-ab6c-37e2-a89c-750067bd5a03 | -12.25737 | -47.79505 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 0adf6706-4410-365e-918b-08c43ac5db4c | -11.91855 | -47.85935 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| cba6685a-7379-3b44-87e9-f84b8a1c1a9e | -11.18777 | -47.75287 | 2025-10-02 12:38:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 014139eb-1fe0-3e3e-b01f-acb0162a6ae3 | -11.09739 | -47.82034 | 2025-10-02 12:38:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b4f97f5e-1493-3501-89d6-037f374dcff1 | -14.91324 | -48.312 | 2025-10-02 12:38:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 58f66a79-6e21-3072-92be-2462dff14285 | -13.29886 | -47.18868 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0e3c2b37-b9a9-3efb-b406-1f6973fa750d | -12.80389 | -46.85237 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5e03c455-7351-3722-84e2-ef86efb7450a | -13.96372 | -48.14365 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 9c8c23d1-2112-3437-8aae-83ce9d7d9f04 | -14.71091 | -49.6186 | 2025-10-02 12:38:00 | TERRA_M-T | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 452cee98-2f98-3d41-8d7d-d8ae37edc08d | -13.80886 | -57.18473 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 67fad0b5-a771-3db3-a531-c470c7d27418 | -13.19105 | -47.79333 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 0cd2c0f1-c01f-3e73-992b-778995161d6a | -14.48474 | -48.44707 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| acc0541d-6468-3505-8b44-7c8c9d60bb5e | -14.2976 | -45.98032 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| fec1be71-e927-39e6-9f6f-5b2be50f3596 | -15.22377 | -48.00106 | 2025-10-02 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| de3b424c-131e-3604-b5e6-06ba14d563c6 | -17.16742 | -47.03094 | 2025-10-02 12:38:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 356e1d6d-6e70-35b0-b969-d375668ec7c0 | -15.25694 | -48.18803 | 2025-10-02 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 1727b83f-0cea-31a6-b470-cf9baae32a9a | -13.29651 | -46.98768 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| db746c58-3e7f-3b99-8afe-97ae3b958cff | -16.05241 | -45.70607 | 2025-10-02 12:38:00 | TERRA_M-T | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 9f907813-fad2-36a4-8f7f-d5f2e8d2abd2 | -11.91312 | -47.88135 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 576699fc-773c-305e-8984-629cc62f4590 | -14.22592 | -46.11858 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2b875701-30d7-3abd-a602-e41886697433 | -10.86928 | -47.8207 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1c917536-3543-3346-b7ea-7f03fa570204 | -14.81373 | -45.81429 | 2025-10-02 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 659f8807-2c39-35b4-b539-644b5b911acc | -14.86093 | -48.28391 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 61652416-09bc-3de7-a5c3-f9706d60faa4 | -16.016 | -50.90713 | 2025-10-02 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| e5c1c613-f3fa-37f6-b8ce-1c5c15558666 | -11.35423 | -48.32829 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 5697381a-1229-3236-b837-e2f9ce370767 | -12.63432 | -46.95956 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 86923b44-96e4-3259-ad31-577114302777 | -15.14242 | -48.02073 | 2025-10-02 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 22d65a62-b1f6-34b2-a41c-a7cb9ce72041 | -11.57057 | -47.00336 | 2025-10-02 12:38:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4d904bba-6631-320b-bb6a-ec5ce2970193 | -11.27814 | -47.8387 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7a2a86dc-bd9f-3b34-9e70-bcc50c90faf8 | -14.93268 | -49.98765 | 2025-10-02 12:38:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| da7b2e9a-d226-3a4a-b785-3d081635792b | -14.97511 | -49.96192 | 2025-10-02 12:38:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a82ebe26-9cb9-3038-b7f2-300f5678fb3c | -15.21164 | -48.00006 | 2025-10-02 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fc4b005e-942b-3221-883a-8cfe1002d65a | -11.83625 | -47.69466 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| d6496547-aab1-3b32-92b4-df9034e20478 | -12.67645 | -48.56005 | 2025-10-02 12:38:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 24eb5aae-2706-3a6b-a9b0-67d32257b2d4 | -12.89853 | -46.93228 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| ebcb76bb-edf8-325b-950a-a2cec88324e2 | -14.64522 | -48.26001 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8cb3b31c-88ce-3465-8a29-2e8703545fc7 | -16.05089 | -50.88261 | 2025-10-02 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d2ffb578-f62f-31aa-ab5c-2e19abe709e7 | -14.9112 | -48.32917 | 2025-10-02 12:38:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| aadfe793-7859-3138-abc8-034a1d9c0670 | -12.99906 | -44.58529 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f207b145-c089-3481-98fc-0184e2ff9c9d | -10.85544 | -52.09756 | 2025-10-02 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bccbef79-b74c-3f31-8903-e1fbc59cd12c | -12.98347 | -44.60653 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 23b9526e-c935-37fc-9460-3110aaf44c54 | -14.58125 | -48.328 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| de314d20-ea31-3af6-897c-6bb77bb00ef8 | -12.28173 | -45.36058 | 2025-10-02 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| bfed18d8-2251-3f98-99a9-9b25ecedf35a | -11.90155 | -47.87988 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7bf84b25-73a0-3543-a9ec-7af1e479e00f | -11.207 | -48.22334 | 2025-10-02 12:38:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c08e0a2a-731e-3b7e-8cff-2b6c6ae55ad3 | -13.31559 | -47.81873 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 7363f779-17f5-3c15-b0b3-9759a60e9ac4 | -13.37748 | -47.29622 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8a93c9ed-ac8f-3ad2-a433-3661f823398c | -11.67287 | -47.50013 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b61ffedb-a61e-321f-b53c-12c706e4a1a5 | -11.56825 | -47.02158 | 2025-10-02 12:38:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1f8b9d16-229d-38ca-a5a9-9fd73a00dd1d | -13.21015 | -48.50066 | 2025-10-02 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 1a01ae1a-cbc2-310c-97bd-dc1f06389ad1 | -11.60076 | -47.63763 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2a202468-09f3-3622-90f9-84073cbfa8af | -15.93474 | -46.22175 | 2025-10-02 12:38:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 95c4df78-8bc6-3ddb-a0da-c5cbc86581bd | -13.22513 | -47.35852 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4331717d-df88-34be-b731-412324fc676f | -11.45931 | -44.96009 | 2025-10-02 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 552e7f0c-678f-3a2e-96bf-e90b736a2671 | -11.90491 | -47.87392 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 25737425-4a10-36c1-a403-8e7c8fa3fa7b | -14.42043 | -46.12975 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| b2a6713f-5e49-33cb-9aec-8d237bbcd172 | -14.83891 | -54.78005 | 2025-10-02 12:38:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |


[Clique aqui para ver as próximas entradas](README150.md)
