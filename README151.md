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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21462050-f2e8-31d7-8ece-31c1b45452a8 | -21.79847 | -48.36193 | 2024-10-09 04:42:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 075b3743-4c47-3f7a-a6c2-81928ce46f02 | -21.79783 | -48.36016 | 2024-10-09 04:42:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e146851d-8530-3de7-b275-9c7dea020877 | -21.60601 | -48.28359 | 2024-10-09 04:42:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c89cea8d-ddb0-354b-a241-76340b8453c1 | -20.76412 | -48.5741 | 2024-10-09 04:42:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1d72f5d3-5af4-3f7c-bce5-96499c849f2b | -20.75545 | -48.52345 | 2024-10-09 04:42:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6f62b57-ba52-37dd-9cf0-2309f0bd6a71 | -20.74467 | -48.54654 | 2024-10-09 04:42:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b88f45a-9b7c-30d1-a2ef-567721af941c | -20.62835 | -49.35324 | 2024-10-09 04:42:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91a0b42d-8cd8-39b2-84d2-8a1cb70f5e29 | -20.61627 | -49.36038 | 2024-10-09 04:42:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec94a59c-f754-341d-b264-a084733078d5 | -20.61265 | -49.35982 | 2024-10-09 04:42:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 542b3a89-8971-31ed-b5b9-18a413cef135 | -20.60178 | -49.35815 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da612269-fc26-30d0-9b6f-6ecbdc4a6c5a | -20.5915 | -49.35214 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74da356d-ada6-3c89-8ee4-6e61a87e94c2 | -20.59132 | -49.34975 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f3613f-fa08-35a7-a4cc-404d39c430d6 | -20.57204 | -49.32883 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 947ad916-b5c3-303d-bc4e-0942906c5d93 | -20.57143 | -49.33322 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d23740a0-8c02-3eb6-9a0e-4327ebc208bf | -20.56475 | -49.35456 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb7c3d4e-a073-32f0-8a4d-b5dbf077e84b | -20.55751 | -49.35347 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b97a5de-1e7f-3c68-9f00-389a505cf3e3 | -20.55087 | -49.34798 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dc87a53-33ca-3722-9537-e4bb95bed38a | -20.54423 | -49.34251 | 2024-10-09 04:42:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d22a922-989f-3fe3-98eb-61d4b27c569c | -20.40483 | -48.84526 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66b41156-ffbf-328f-9748-49ef5f68f177 | -20.37833 | -48.78911 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46d7717f-b77f-3c39-b93d-ddecefd2099e | -20.36656 | -48.73506 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46fc9b91-08f3-3d33-8e20-bb74184cca35 | -20.35925 | -48.72726 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| eec9761b-b94c-3bfa-998e-e5e76544f748 | -20.35859 | -48.73197 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7704685b-6e91-3a87-82ed-77dc2a328764 | -20.35725 | -48.77658 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b6f28de-817c-37bb-a4eb-73e7e9eab52d | -20.35662 | -48.78127 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32ed4a7a-be7f-3872-b2e7-8e9c0c127410 | -20.35551 | -48.72675 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 65f04e12-7b29-3877-b673-401a32d8199b | -20.35486 | -48.73144 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| eed83ff5-494d-37ef-80cd-36d02a44c39e | -20.35352 | -48.77604 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50e0d55d-6f91-3f92-947d-04d91de3121a | -20.35287 | -48.72355 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 10c240dc-cb7c-3ecd-bc7f-7440458d09c1 | -20.35178 | -48.72623 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 431be23a-6294-3e48-86ab-c7420c8c12fb | -20.35149 | -48.78334 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c73954f-b1c9-312a-b5bc-7be818024cf5 | -20.35113 | -48.73092 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca84068b-7f63-3b5c-9c9d-d0693f0b9481 | -20.34986 | -48.86041 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5492dd6b-4495-3f84-8383-26fa3d024c2f | -20.34976 | -48.71835 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63d46cdd-bb08-3dd9-8d9a-87d078f05aa3 | -20.34925 | -48.86497 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7119a4b4-d69c-36bf-a692-6d6171e6c631 | -20.34914 | -48.72304 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7d27a1c3-eccd-3f9c-bc32-04d21f732aaa | -20.34868 | -48.72108 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82b71895-ac78-3996-a207-ae5f964930e0 | -20.34804 | -48.72573 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8dc71d25-7f64-3466-b75f-458019115644 | -20.34555 | -48.8644 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ac65a6e-ba3d-3371-b86d-51ad6bd31a63 | -20.34431 | -48.72521 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 1e450f95-0274-3bf4-be55-9a41efee2344 | -20.34367 | -48.72986 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 1c40e6bb-8a99-3022-bfb1-96164771af25 | -20.3425 | -48.71066 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf6bc27b-dadd-3134-9ab9-a2af28decb1c | -20.34058 | -48.72467 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.6 |
| ae95c5af-ecbe-3578-93d0-685b592bf0cc | -20.33877 | -48.71012 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41563c85-34b9-3835-932b-0c1a9d30da0e | -20.33558 | -48.73339 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ed3c244-6f15-3928-ba7a-5b0c323985ad | -20.33385 | -48.85599 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0e53cbc-7944-3146-8c8d-b47d7b9c52af | -20.33313 | -48.72352 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 8c166ee1-a7f9-37f3-aad1-e1afcb0edc93 | -20.3325 | -48.72814 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 35.8 |
| fe4890f8-9ba8-3357-85e1-efc009ac0b7a | -20.33135 | -48.8576 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14faf5b6-4177-3fd3-89f8-1075d4819b0d | -20.32941 | -48.72293 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 29c9c73b-d561-364a-a640-ec64c4f8b46f | -20.32878 | -48.72754 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 33c2a228-5916-3779-bbb7-bd27393460b6 | -20.32569 | -48.72232 | 2024-10-09 04:42:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a71b57da-ff26-3adb-878f-eb80ca5fd42d | -20.01928 | -48.22891 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88260a6a-08e7-3e51-81de-446abf3e5c47 | -20.01546 | -48.22839 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5822e0b1-180f-3187-b1d8-556c8db476e0 | -19.78051 | -48.2652 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3da8af7a-fa69-36b1-92a7-7380e2d872cf | -19.7782 | -48.26311 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d8a206e0-bfb3-35aa-b874-ef90e76e9f37 | -19.77671 | -48.26468 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2b350a9f-8fee-34cf-9836-0e04bfc11ac7 | -19.7729 | -48.26417 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ccb78a88-16d0-3f43-ae3d-762bd4b14010 | -19.76341 | -48.2777 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31109f7f-ab5a-3556-ab9e-cc8d75b40565 | -19.76101 | -48.27559 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94f159af-e4ce-31a8-8cf9-edbbdf33a99e | -19.75655 | -48.27994 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56b7b400-5f58-381e-bb77-b74636fc590b | -18.97588 | -50.1981 | 2024-10-09 04:42:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cd1fd9a-82af-3729-a47b-5d5bde2b8268 | -18.9753 | -50.20206 | 2024-10-09 04:42:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b7c5fa0-2e37-30e4-95e0-ad0e86d59fe2 | -18.97243 | -50.19753 | 2024-10-09 04:42:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b05f13a-6e80-3d9c-9684-299141dcfdd6 | -18.97186 | -50.20148 | 2024-10-09 04:42:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bae92cf1-e05c-3ad9-af23-fe2f7cb79056 | -18.96899 | -50.19695 | 2024-10-09 04:42:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b032dc1a-8e8f-34da-917d-e789a163a547 | -21.3991 | -57.22234 | 2024-10-09 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05a7cf8f-3ac8-3659-8417-359dc4acb0e6 | -21.39213 | -55.68489 | 2024-10-09 04:42:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2d99655-ef40-363c-bb78-79f070348fcb | -21.39139 | -55.68914 | 2024-10-09 04:42:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87d168f4-2f0c-3f30-88c4-e29706789313 | -21.38859 | -55.68419 | 2024-10-09 04:42:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e42a7b28-3010-3898-a432-c700306cb6a8 | -21.38506 | -55.68344 | 2024-10-09 04:42:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a7a9d42-bd07-30a9-a2d0-f53d0618bd55 | -21.36006 | -55.70063 | 2024-10-09 04:42:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af7eb7a-b3dc-3b75-b6eb-affb64a947bd | -21.34289 | -55.7148 | 2024-10-09 04:42:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19332a19-7b08-364b-9116-c2022ea99d9c | -21.3397 | -54.64108 | 2024-10-09 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7a4f18c-e06a-3bd6-879a-3af75ccceabd | -21.33904 | -54.64502 | 2024-10-09 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da2ad861-5a88-30b5-9dc4-7a0f317b0ff6 | -21.33629 | -54.64042 | 2024-10-09 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 347c841f-3d0b-3b12-862b-b3ccd2951591 | -21.33563 | -54.64436 | 2024-10-09 04:42:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eebcc492-9d4c-3f8d-b9f8-0c1cfb383ce4 | -20.89491 | -54.97889 | 2024-10-09 04:42:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e6f10ad-d1c4-3a1b-9fcc-c68034f89a69 | -20.89215 | -54.97408 | 2024-10-09 04:42:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6daec061-3bac-358b-8d09-cf1a7b233d14 | -20.89145 | -54.97824 | 2024-10-09 04:42:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba72811c-106c-3ab4-addb-9cffda84d190 | -20.88869 | -54.97342 | 2024-10-09 04:42:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 842ef4a4-a249-3825-9efa-f2caaa29d48f | -20.88798 | -54.97758 | 2024-10-09 04:42:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2642d71-f1f2-300f-951a-7c034a9d3dac | -20.72103 | -54.87993 | 2024-10-09 04:42:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bed8c58-b423-33c0-b4d6-2b5226481807 | -20.50001 | -54.96441 | 2024-10-09 04:42:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb9f9655-6c11-3279-bbb8-0083c47dfa08 | -20.49653 | -54.96375 | 2024-10-09 04:42:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 392a4046-cb1a-3320-a424-b09c6f72548c | -20.42402 | -54.81766 | 2024-10-09 04:42:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 225de1d0-69a5-3b09-98d9-20f578c36a8f | -20.36871 | -54.69236 | 2024-10-09 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6a9902d-73f8-38ab-8f38-23187468eb54 | -20.23841 | -56.97028 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a11bf960-b862-377c-bf11-da77232f8d07 | -20.23709 | -56.96689 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a57de85e-b166-3a57-80d3-5724d4da1887 | -20.23613 | -56.97226 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7cd2b865-3ff5-32a2-8471-f5e0ac78a833 | -20.23563 | -56.96392 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fb7d4a80-46fb-3d7a-99fa-69fae699d1bc | -20.23328 | -56.96596 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 209ad50b-6e18-3fe2-9f56-2cf289b00f0e | -20.07323 | -54.51626 | 2024-10-09 04:42:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3584f7ba-725d-3517-8b25-68b88abcf78e | -20.07256 | -54.52027 | 2024-10-09 04:42:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8854469a-911b-3941-9681-bbd6dc764dcb | -20.06912 | -54.51963 | 2024-10-09 04:42:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b55d296-94ca-3586-9fa9-e206bf58cd79 | -19.80521 | -45.60555 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adbbc7ee-8674-3576-a803-31437706f777 | -19.80466 | -45.61031 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5a10aa63-5790-3589-897a-bd206436de08 | -19.80411 | -45.61505 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 1194107a-ece6-3f2f-afb0-1923b5553079 | -19.80356 | -45.61974 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e55cb6b1-090d-35e8-85c4-d40772493c3c | -19.80073 | -45.605 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README152.md)
