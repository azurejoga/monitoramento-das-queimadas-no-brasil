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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c85140a-ef28-3c2d-9c5e-7afdf46d335d | -17.74937 | -44.48462 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8bf7cb9b-e155-3f56-aa73-72864c157c21 | -16.47149 | -50.66667 | 2025-09-10 05:06:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| daa5d9d4-f9c3-3722-b1af-e8c65e009133 | -16.62324 | -49.76551 | 2025-09-10 05:06:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bd8e0c7-3ae0-3406-a9dc-fd6b5e2758ca | -15.27435 | -53.78249 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a51ef4a-d94b-38e7-bbc0-bb6528c8efba | -15.80763 | -52.23458 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6ed2851-91c6-3241-b73a-2d9bde47a067 | -16.57253 | -47.78798 | 2025-09-10 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6965387-d7b7-332c-8a1c-064e11ef38c5 | -14.32821 | -47.29858 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff45b0e5-2d4d-3473-a5ab-fc0c64a3001b | -16.47087 | -50.67181 | 2025-09-10 05:06:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6f2d9b3-3662-3314-932e-478f51920e5b | -15.5232 | -48.38115 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfacf185-0fef-305c-b2f5-a1cc802c1e9c | -15.28126 | -53.78832 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ba8413e-0946-3f01-8ab9-5f75f0c3457d | -18.13234 | -51.72696 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 256c6841-c99c-3f6f-bdd2-b8058f8c4ce7 | -15.526 | -48.37873 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a876178-21cf-3640-8936-09600b8b4e16 | -13.22676 | -51.77269 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 491bd1b7-b77d-3347-ab36-e5cac3a03eb9 | -13.28423 | -51.72521 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25b06c4a-c791-363c-ad6e-bee7ee81f25f | -15.2737 | -53.78725 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f447cc9-72a4-3366-89ae-e30384f9e220 | -12.61094 | -56.9718 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38028fad-41bb-39fa-bfa5-b4a3ef19efb8 | -18.0027 | -47.11402 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 594a51b5-5953-38f0-8a5f-5a8e1253c897 | -14.90392 | -50.12054 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 043c3b21-2fe6-393f-8499-bdc2fd3550bb | -12.92688 | -54.76546 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e01141e-f47e-3c35-ac5f-779412f22f3d | -17.23959 | -46.07337 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef393af-3c82-31d3-944b-d44cb99d7b6e | -15.26012 | -53.77305 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaadb1da-0711-38c8-ba7f-c79245ea10ad | -15.6592 | -49.93455 | 2025-09-10 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf58ea2a-d021-3d16-b3aa-df4659e93a82 | -16.34542 | -52.94572 | 2025-09-10 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0f5de8b-d93f-3391-b4b0-8fda0b35a2c5 | -12.60874 | -56.9642 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0db7db3-d228-3e4a-af30-cbca7e28d680 | -15.09436 | -50.07233 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c80e5b5a-f081-3f72-bd0d-0946bdb07326 | -17.30532 | -46.75297 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e43c3f7d-2b90-374a-81b4-da7dde837493 | -15.81018 | -52.24726 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12342230-17c0-34be-8f8f-7672160bbf5f | -15.02374 | -50.09298 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 50680f57-e9ad-32bf-9493-5ff6da3b83ef | -14.88897 | -55.86428 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5782c322-a19e-37d0-ba21-27e0d136838e | -16.57495 | -49.22489 | 2025-09-10 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46aeea38-5754-3a6e-afad-4ba21a125f45 | -15.10855 | -50.07581 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88d1dbff-e9be-37e5-8d45-0587e431d4cf | -15.02123 | -49.25889 | 2025-09-10 05:06:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e404663-aa5b-3fae-a36a-89ae9454d95d | -19.29693 | -47.98933 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47d883bf-ba81-386d-ad31-7d0e13b83c40 | -11.78125 | -64.93503 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a0bbc5b-9749-36b4-8a3c-63d5be08b4dc | -15.09018 | -50.06685 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15f8d769-4a1f-388c-8609-b90672aa32a4 | -15.80772 | -52.24062 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b34e613-103b-33ba-bfc1-b415406035fa | -15.4792 | -49.3858 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b74065a-4cb3-3dc6-bab1-7e9baf8304ba | -14.38891 | -47.32338 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31390fc3-f654-373f-bc14-685397e3f2f3 | -11.79559 | -62.74298 | 2025-09-10 05:06:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5eb5a4d-8039-3799-80bb-a601416c6ec8 | -14.38762 | -47.33432 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9517973-0b62-3f77-a340-335a387cc3e7 | -14.5562 | -48.76608 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62964f4b-726d-389b-aef2-e3dc13cc5dff | -13.13185 | -54.91677 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 221ec068-437c-39d3-9521-5db046324552 | -15.10815 | -50.07888 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c85fe8ac-6691-3d64-ab9d-0084697c4ed2 | -15.10619 | -50.09566 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5fb457aa-e8ec-3cae-9d39-45ad9037a825 | -15.65981 | -49.92934 | 2025-09-10 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad2e770e-da31-3a65-a457-1649f2b5633a | -15.47628 | -49.36731 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea41d64a-f3b3-331c-b5fd-8da0ffcf7ef4 | -15.16453 | -47.95426 | 2025-09-10 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3deb22c5-4ef5-341b-adf2-38f96d4f22e3 | -15.80823 | -52.23665 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14115956-c96f-3cb9-b84e-d73edc0a4225 | -18.4525 | -49.57127 | 2025-09-10 05:06:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7288b77-5587-3236-9c8b-c382f6e3272e | -17.25535 | -46.08545 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1570113-1135-3932-ae38-e1b58bd16c33 | -14.91884 | -50.11725 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 91c8c5c4-fd19-3730-bcf0-1e53c16e2efe | -18.45318 | -49.56519 | 2025-09-10 05:06:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e9acab8d-d5cc-383e-b079-87b01e72404f | -17.30527 | -46.75491 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dce93c4-6f00-32e0-b067-c7ee159d6318 | -19.2972 | -47.9873 | 2025-09-10 05:06:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a962a82e-a078-39ba-b995-b5745d5f4918 | -15.83278 | -48.96494 | 2025-09-10 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8358826-fc27-39d0-b418-8b2e2e8fe075 | -13.92498 | -48.25251 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62ee53db-ce6c-35a2-be84-7e6e9a745582 | -15.80987 | -52.25724 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 788dc7cf-960a-33bb-80ba-16e250ad17ee | -15.83808 | -48.96476 | 2025-09-10 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6fecbf3-abd2-3ec3-8cdb-651a37157aaf | -15.91056 | -52.20478 | 2025-09-10 05:06:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60366868-c613-3032-bf91-25f91c7ce335 | -18.35472 | -49.34756 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 597bbcb9-7c79-3e92-a44a-add90770cabc | -15.00516 | -48.02718 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1c0a877-420c-3bd8-9cbe-26592241c19f | -15.74885 | -53.51991 | 2025-09-10 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 269caa64-c335-3a98-824c-af31d9344e94 | -15.22571 | -48.24412 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 053a8a34-f59d-349d-9187-70b1b63360a6 | -15.8072 | -52.24471 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 430f6c33-bc53-3336-8b10-9bd5af2a00af | -16.57458 | -49.22803 | 2025-09-10 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4feaffdc-982d-3bad-818f-414f6f2e9a2a | -14.89805 | -55.85024 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fb37cd3-1594-3b1a-a853-7f254caf3203 | -17.24262 | -46.08407 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13e8dccf-3df7-3c6a-9449-f1788477f1ae | -12.93155 | -54.75807 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96504cd2-7f49-314a-809d-cea9e816addc | -19.64413 | -45.04165 | 2025-09-10 05:06:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d778a77-6c84-3657-a00e-4357b1bc4c78 | -13.12487 | -54.91568 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cab44b06-1c62-38d7-8f19-ca48991cb340 | -14.61243 | -46.36595 | 2025-09-10 05:06:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1bb0190-b63b-3524-b779-da7acd88bebd | -13.34028 | -51.69617 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b5ac16-df17-367e-ab8b-152239313a45 | -15.33333 | -52.89627 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2007d49-8e50-37a9-81b8-0ad1116a99f4 | -14.45723 | -53.33942 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e1f6352-77ec-3f31-a143-b658d4b6e097 | -17.30635 | -46.74303 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afbd1500-a0a1-3795-8c0c-490a5db2485d | -17.32323 | -46.69769 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79c41f60-e45c-3af3-a808-2c0a24d51d61 | -17.74358 | -44.49284 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c4a03c3-ad71-3094-beae-36b6f0e900e3 | -14.56215 | -48.76025 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 151e8700-1831-3765-be4c-2243af404207 | -11.79142 | -62.74217 | 2025-09-10 05:06:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 72634845-f38f-30b6-bbb8-6e3408d64858 | -17.7499 | -44.47845 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2e110540-f2f5-3ad5-ab8f-8a3f161fa9bb | -19.51366 | -45.02188 | 2025-09-10 05:06:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e194380e-a82a-3a24-ab77-5bb6ede95514 | -16.67215 | -48.5176 | 2025-09-10 05:06:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5169fe1c-6eb7-3f9e-8dc8-1b784820073a | -14.2448 | -46.6925 | 2025-09-10 05:06:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a333d63c-f16a-341e-b1bd-c723c76a45f0 | -17.74512 | -44.47602 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c365bd2b-1960-33d9-a998-dd43ed1af0a5 | -15.13859 | -52.4043 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9996c814-08a2-377d-a751-79346ed26c74 | -13.12197 | -54.91119 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 22a884cc-ae55-37ba-b0a0-9ba502de483b | -17.24597 | -46.074 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4043cc05-8be0-3d49-b44d-06961f4b00ce | -19.28561 | -47.98595 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b63d505a-5dfe-3855-83a2-5fd639b58353 | -18.12934 | -51.72845 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 373c5e0b-cdb8-3faa-9d13-f0190cb9199e | -17.71408 | -44.42713 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d37b6eab-4738-3189-b699-297a12410150 | -14.93027 | -50.103 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d36252f-0a18-3ede-ae5c-642f8f1f2d17 | -14.88841 | -55.86808 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30efed74-10a7-3093-a56f-92732c670c4c | -13.92962 | -48.2589 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1bd546e6-c7a9-36ce-be72-62327aa1034b | -14.38807 | -47.33052 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a981912-e1ce-3082-98be-33d4a710a8dc | -15.48422 | -49.38666 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 718c19c6-af4c-3fe7-9f49-03e66c3c028c | -14.90772 | -50.12364 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36e06055-0c77-3ad1-b50b-3b4d0c10e74a | -18.13381 | -51.72911 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd0758f-081e-397a-9ea1-d19751e3c490 | -15.87593 | -52.20796 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e1e55f5-056f-39b1-81ce-c2b979ed6ca3 | -15.79977 | -52.26143 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b15a4b73-348c-3ee9-bee6-54060fa7872f | -17.72985 | -44.48809 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README99.md)
