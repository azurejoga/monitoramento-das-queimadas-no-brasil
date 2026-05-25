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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e6166e6-1052-3685-81ea-9d7494e22db1 | -11.43608 | -52.92548 | 2026-05-25 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e408c5a-9648-3186-bf10-cf20889bac6a | -11.45835 | -46.69407 | 2026-05-25 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9087d103-613c-38dc-b00b-a713288ac339 | -11.06885 | -46.51481 | 2026-05-25 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3868cc-1303-3972-b899-20e665949db0 | -12.41213 | -47.49377 | 2026-05-25 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb5898dd-4b8d-30dd-a985-6ef4bf0cf97f | -14.01722 | -53.35735 | 2026-05-25 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bb4b7d1-127f-37ed-a420-a14ed628c629 | -11.21525 | -53.82987 | 2026-05-25 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 028dd295-8398-341a-b222-233d0926efd2 | -11.36379 | -52.95347 | 2026-05-25 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 8d9f3a1d-0fed-3925-befb-36fb522fbf0b | -11.91332 | -57.04061 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a87be810-845f-30c7-be0c-e7936faa914e | -11.94502 | -49.29657 | 2026-05-25 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4925f0d-424c-3c0d-9d67-2b8a3f312ca0 | -11.55015 | -56.9554 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52f11ae4-a72c-36ec-b01e-cc27e97e7589 | -11.17636 | -55.9179 | 2026-05-25 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 785de7e5-67e5-30d8-96c7-de6dc48644ba | -11.4748 | -47.38697 | 2026-05-25 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9caee92a-4a73-363d-bfb9-a841ddc7a460 | -14.757 | -52.67731 | 2026-05-25 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c339016-ae1d-3fd2-8b6a-1e59a9f0b418 | -11.72894 | -56.82953 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8890a70d-74d7-3c50-96a6-c07a1b11d865 | -12.54385 | -57.16686 | 2026-05-25 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeffce82-c192-35dd-b552-b5593334c1dd | -14.02477 | -56.79696 | 2026-05-25 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4267cdc0-bf55-3d91-a272-2db6f2f00bef | -11.54621 | -56.95465 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9b052d7-e62d-3632-b2c3-644cc147ca72 | -12.8897 | -58.19714 | 2026-05-25 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b88a164-2e98-39a8-8997-e8e29761d6e5 | -11.37611 | -46.72166 | 2026-05-25 04:51:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a29f8a6a-b98a-39ef-a86c-78d7e3256059 | -11.48458 | -47.40348 | 2026-05-25 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 115dcc15-40e6-39ba-8b49-30bf13546372 | -10.3944 | -49.44907 | 2026-05-25 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb8e0f9-aa88-3c2d-a65f-9ee8f46c760c | -11.90937 | -57.03994 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d740eea8-483a-35b6-b085-d5b441bdbcf2 | -12.88983 | -58.1729 | 2026-05-25 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 171322e5-9c93-3c6e-a207-5e506e98e7f3 | -11.47409 | -47.39212 | 2026-05-25 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7ce9cda-f5b9-3aae-bb2d-a1731f5d318c | -13.5305 | -46.71593 | 2026-05-25 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d55160ec-2054-3f8c-afdc-f909932d9a29 | -10.395 | -49.44517 | 2026-05-25 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 712be5f9-9739-329b-b868-c2639893574d | -10.39849 | -49.4457 | 2026-05-25 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49114dc8-b3bf-3f16-b618-143536d0a47c | -10.39559 | -49.44127 | 2026-05-25 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30939711-a0a0-36e9-b457-4868c5f9cea3 | -11.54978 | -56.93402 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b87817a2-ba76-3bf8-8a71-87baeb8bd5ab | -11.21586 | -53.82616 | 2026-05-25 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8206e501-7201-3d77-bb0d-8ee62bfe4ea0 | -11.21865 | -53.83044 | 2026-05-25 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01c70fe0-07ae-3e63-866f-aec6d219df41 | -11.54496 | -56.93843 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72c1afff-f58c-37ae-99a8-feb5502e6b25 | -13.97705 | -53.87513 | 2026-05-25 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a14cf035-d2a7-3391-8dd9-d541e1adc33c | -11.43551 | -52.92903 | 2026-05-25 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78a7d548-552b-3471-b015-350d64a42acf | -11.30538 | -47.53931 | 2026-05-25 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa7b43b5-808d-3fc6-b619-f904cfa38499 | -13.97646 | -53.87876 | 2026-05-25 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95d6cfe9-2ed8-3716-897d-6aeb6de65432 | -11.54673 | -56.92816 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97137d3d-d14f-371e-8686-15578035ad50 | -30.13574 | -52.55814 | 2026-05-25 04:53:00 | NOAA-20 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| dfffffdc-af62-3a28-b5e2-007f8f5b0034 | -20.06565 | -55.75681 | 2026-05-25 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e4fb7871-f485-3532-aea3-27854aff5230 | -17.68182 | -47.76434 | 2026-05-25 04:53:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 26c7df48-eea5-3091-ae00-2dd0298459c4 | -23.76773 | -54.50608 | 2026-05-25 04:53:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 55246c9d-27d8-3836-9079-ffce9bd7bcad | -18.09487 | -46.87682 | 2026-05-25 04:53:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65d343bd-ba70-35dd-9b85-2f9bc910c1b0 | -18.10276 | -46.8869 | 2026-05-25 04:53:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a50e24cc-bcfa-3130-a1e9-eecf37328ce1 | -18.0921 | -46.87826 | 2026-05-25 04:53:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 484f314b-8819-3b87-8528-e6a193024019 | -19.39447 | -54.58995 | 2026-05-25 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9859856-b9ed-3dce-9340-d1b07520a1f6 | -18.40743 | -52.09583 | 2026-05-25 04:53:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d523cef-5a14-3b20-bb21-373aad2556b0 | -18.09154 | -46.8827 | 2026-05-25 04:53:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b757f0e9-e8de-369e-9cec-35a8abc0d34f | -20.0181 | -44.23931 | 2026-05-25 04:53:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 254790f2-2b0c-3394-af5f-65dd54f10396 | -18.09828 | -46.88634 | 2026-05-25 04:53:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 695b6f94-60bc-3a65-b44b-9ac215b83551 | -18.09434 | -46.88129 | 2026-05-25 04:53:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f6dc2a1-b4b4-37c9-a5f1-0e4245e3aa30 | -11.55367 | -56.94303 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b735d45-1d03-3a4b-a2b7-2a73b3349837 | -14.75626 | -52.67883 | 2026-05-25 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e21e2af-f2d1-3d12-af78-6d54a1cdc67a | -12.89217 | -58.18127 | 2026-05-25 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f334f09-d7e8-31ba-bf5d-107f1337b390 | -11.54796 | -56.95837 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98504d42-b30a-324a-92b6-062c1a6748de | -11.3688 | -52.9563 | 2026-05-25 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8d250d5a-8f3d-3050-b69c-860d4781cf6b | -11.54522 | -56.94158 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5dd2e80a-0683-3fcd-9fa9-9048263b331c | -11.22024 | -53.82725 | 2026-05-25 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7bd6042-bf1a-319b-857d-83fae0979169 | -11.73365 | -56.83594 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a5a7824-4112-3035-a996-0ed9a842214c | -11.54663 | -56.93081 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e65c50ba-9e74-3fe4-9e2d-98c390ea5501 | -11.54867 | -56.95295 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a70522f8-c16f-3300-b9a5-c5dbe2ab4891 | -11.36252 | -52.95545 | 2026-05-25 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da177b4a-b66c-3053-a8b0-b47122856bb6 | -9.55876 | -64.6262 | 2026-05-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda0b142-f87b-3b3e-acc2-09c3f5fa4c70 | -11.55149 | -56.93141 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80f7cd76-7a8b-3f1c-a437-d8bb0b46f5ed | -12.89033 | -58.19529 | 2026-05-25 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 50eea793-eb02-3670-bf65-80fd0afa31e0 | -15.10515 | -57.62281 | 2026-05-25 05:38:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ade954c4-0bf8-35ae-8ff0-3fae8415a295 | -12.88885 | -58.17134 | 2026-05-25 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a1cdffe-2acb-3711-8881-33227f4f86ab | -11.55234 | -56.9538 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3fb56f2-0aa3-3ae4-9457-f9681637a766 | -12.12045 | -61.84717 | 2026-05-25 05:38:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da8e55ae-203c-33ba-940c-dad07bb413d9 | -11.36312 | -52.95026 | 2026-05-25 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4cd1b129-2576-3b85-b66a-54bbbf925f4e | -11.55078 | -56.93683 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 53bb3226-f653-36de-8a78-c57ecbe0e46a | -11.55493 | -56.94279 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 966efc82-964a-3ada-9d17-b52d9eec0e09 | -11.55719 | -56.9544 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f97bdfe1-c46f-337c-8d8b-93028cb7d918 | -11.54592 | -56.93621 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4adee063-ff99-3f47-af51-8e58977320fe | -12.88973 | -58.19992 | 2026-05-25 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a34ef3-a1c2-34e9-a58b-286bd861ffe6 | -11.21971 | -53.83157 | 2026-05-25 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ccda30b-c8a1-3c69-b40a-07da8f5a5648 | -11.55352 | -56.95354 | 2026-05-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86970327-b436-3dfb-925d-a4fddc072c1a | -11.21774 | -53.82787 | 2026-05-25 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 677d1cf4-3682-38ca-9f14-432fc867a6df | -11.36701 | -52.94703 | 2026-05-25 06:59:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 988b9624-edc4-340e-b200-d78ec39d6e94 | -11.36557 | -52.95708 | 2026-05-25 06:59:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fa9036cb-b9de-32cf-bbaa-887a6daa4dae | -11.21183 | -53.82581 | 2026-05-25 06:59:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 78e8cd15-ddde-302c-a4cc-4841743e1585 | -11.55151 | -56.9385 | 2026-05-25 06:59:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d51ef487-957e-35af-b445-d908c570e7a5 | -11.54377 | -56.93126 | 2026-05-25 06:59:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e9ceea2f-cd2c-3ed5-a632-60da026187b5 | -6.11611 | -45.53312 | 2026-05-25 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7c834a5d-63d2-3063-bd34-bace04bd3d02 | -8.93743 | -49.41497 | 2026-05-25 12:14:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 60665ede-ebd5-380c-ac25-62c93ee7d24b | -9.11869 | -48.6614 | 2026-05-25 12:14:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a0f99a4b-00fd-383a-b17e-7ff2bc0942af | -8.7255 | -48.32004 | 2026-05-25 12:14:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e6cdab1d-f1de-3e78-af7b-93ce7728f9ed | -8.05361 | -49.96893 | 2026-05-25 12:14:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8f309865-7980-3414-9eb6-34a5ee2321e9 | -5.78967 | -45.13126 | 2026-05-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 1f4a4b1b-2b26-389e-9b73-9d27f12d312d | -5.79169 | -45.12498 | 2026-05-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1467e31b-93f1-3224-9753-0426a302fe66 | -9.80127 | -47.17999 | 2026-05-25 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4e7cf4fa-7fde-3a06-98c4-c0a0bdc8395c | -9.25437 | -49.25858 | 2026-05-25 12:14:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6b53559d-89b8-324c-a496-fa2e58aa7e87 | -6.11675 | -45.53977 | 2026-05-25 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b41e2516-e4e3-37df-840a-4f710e15bff9 | -8.25659 | -43.94479 | 2026-05-25 12:14:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3a4d5292-ce50-3ac9-93d0-4b88449f7dc4 | -8.26001 | -43.92108 | 2026-05-25 12:14:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4a429815-7b5e-3aed-8d91-8cef2ce9fcb5 | -9.18118 | -50.33484 | 2026-05-25 12:14:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7eb6de41-8bac-3e3c-bca5-d0383da947d1 | -10.10025 | -50.62241 | 2026-05-25 12:14:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9866351e-26a0-38d3-b738-3bf323d00ac6 | -8.98673 | -46.82066 | 2026-05-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ec3a60d0-95ee-3f49-b065-aad16a08c4bd | -9.12033 | -48.64878 | 2026-05-25 12:14:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e6dd9b3e-4aba-367d-8d4f-10fe8fa6bb65 | -7.82778 | -42.06326 | 2026-05-25 12:14:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 567d25cd-522d-323c-ac43-997dd6665d01 | -9.25589 | -49.24723 | 2026-05-25 12:14:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README4.md)
