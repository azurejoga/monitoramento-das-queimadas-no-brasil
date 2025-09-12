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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0435eb4b-0548-36eb-a248-324819c08f9f | -12.93252 | -54.75658 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81c3b84f-ca00-3d15-bc87-3810a31dacf8 | -14.32912 | -54.11958 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80ce585f-5f7e-3f62-b2ff-be9999edf93a | -15.61047 | -52.74358 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c19f31d-9773-3147-8109-ec5c51953fbe | -18.66141 | -47.66439 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bf9f453a-201e-349b-a942-cbd5ec6c31f3 | -14.73925 | -55.61428 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82cda272-5985-3e54-abbb-2b3c8fa025f3 | -15.57762 | -54.76844 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9325f9bc-5d30-34af-a2f5-6d1ce60bc480 | -17.38231 | -52.95695 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a90d0205-5307-327d-9082-1169ac51be27 | -15.11881 | -48.61704 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d252107-1902-35fc-81f5-a4a4d4bfa75a | -16.51807 | -55.16885 | 2025-09-12 05:21:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9592a9aa-dc98-30f4-8926-2c684023a3ed | -14.56043 | -54.5186 | 2025-09-12 05:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 126d3cbf-0799-3b45-b498-866e835914cb | -17.13813 | -48.48967 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1120cddc-1dcc-3364-9080-b497baced5da | -14.74431 | -55.60739 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc1c381-3171-3588-b0ab-90f26cc0655c | -15.12054 | -48.60297 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ff7d803-8d11-3c07-86eb-85c3b2d98a16 | -13.13394 | -54.9282 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 343d74ae-474a-3b50-b5fe-1877ae46198f | -15.57519 | -54.74829 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45c8d241-e71e-3c6c-b539-c2ee21356a19 | -14.92546 | -55.84034 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5de7b3a-29d8-326f-bf3a-29d4ec98aaa7 | -20.00261 | -47.651 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d67fc72-ed01-3177-948a-13bbf01c8cee | -12.96001 | -54.74406 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a779a780-a9b6-3125-a107-7938f02d06fc | -12.82676 | -61.94929 | 2025-09-12 05:21:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40de1808-7b1a-389f-9b74-39e7895715da | -14.50464 | -53.91205 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c779e99b-bdae-350a-bf86-788d642f2419 | -15.6108 | -52.74348 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce339001-9cb0-38b2-a03f-0ca53d6c7773 | -15.14832 | -52.47372 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d12830ed-780d-35d6-8174-3d412420a231 | -13.21859 | -51.75573 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39147921-0fe2-336c-9d4b-8dd55680adc1 | -15.10844 | -52.46148 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f04058-f879-3395-8d01-c196ca991702 | -18.61466 | -48.25145 | 2025-09-12 05:21:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a914c10f-5ac7-3528-96e3-860bf767e70c | -20.35738 | -49.95967 | 2025-09-12 05:21:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96bdea5b-756e-3bff-8b75-38a3fef8c7bd | -16.65219 | -47.6216 | 2025-09-12 05:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c62f73a-10d6-3fa1-9078-8da954b6914c | -17.37696 | -52.91336 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 181cbeaa-b3c6-355f-ace4-1071aa780c65 | -14.33363 | -54.12003 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| feaceef9-1a3d-328c-b6f5-7f1c6188146e | -14.4397 | -53.27682 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1983b1c-4a67-3508-98e8-fe299d14e5a6 | -13.22377 | -51.75653 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a31bd6d-3432-35c5-bf38-4dbbf0ccf783 | -15.10979 | -52.46235 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf6fca60-532d-3198-a072-31e5a584b434 | -15.10551 | -52.45497 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 830fe257-f4e3-380f-9209-1f5706b5ed1e | -19.24395 | -48.04662 | 2025-09-12 05:21:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1216f552-4bf8-3fe4-aac2-86833869d2dc | -12.62294 | -56.96148 | 2025-09-12 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e64373df-1850-3a95-8e45-a25e40a03bf5 | -17.83192 | -52.05535 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d2e1288-e73e-313f-8711-7d2683f92228 | -13.90349 | -48.27222 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| cbc0c407-253b-350f-827a-e343b138f294 | -15.88321 | -48.17941 | 2025-09-12 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51c2d5bb-cfd9-3cbb-8728-a83e18b747fe | -12.91934 | -54.75871 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c5fc7bba-c4ed-304c-b759-ae726495b3a1 | -10.79901 | -68.27481 | 2025-09-12 05:21:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3770b5b-6ef7-32cc-98dc-0132243c2588 | -15.13427 | -48.59703 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a5caa90-e9f5-3e86-9d67-117ccd50f1f8 | -15.58166 | -54.76718 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 619c3047-e644-37b1-adf1-e9e207e140dc | -19.9933 | -47.64204 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c76c251b-c637-3018-9021-d572791b5bc1 | -15.53358 | -48.55453 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb337cfe-a182-3358-aac4-4a929ec2875b | -13.19226 | -51.75522 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93eabb01-fc97-337f-b78f-229a06813f75 | -15.68341 | -52.23129 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d107248-1e28-34b6-be00-fcfa552d1589 | -16.61645 | -49.79906 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a40eb5f1-9c5d-322e-ac89-25149196f387 | -16.26599 | -50.07196 | 2025-09-12 05:21:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 033cbaad-ee6f-3290-99f3-5409c7346258 | -16.65315 | -47.62456 | 2025-09-12 05:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60ff6c3a-6911-3b14-b643-f7b6f1402930 | -14.32794 | -54.12883 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 76dc71d4-a79f-3bd2-9ace-91ae5fdaa203 | -12.92676 | -54.80015 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 908fd398-06a5-3364-a460-948ee38a11cb | -16.63712 | -49.77916 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e710f019-00b2-3ae5-bb74-9a630adcd9f4 | -15.40958 | -49.62555 | 2025-09-12 05:21:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 524b02a3-f13d-3ce8-a121-b4677b787090 | -13.90354 | -48.26739 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 3e444935-9d1d-3803-9a69-12e845346a7a | -14.5113 | -53.9006 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ffb32fe-5a09-34ae-87a5-d56475f52f06 | -13.90418 | -48.26585 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c70a99ca-544b-3ea3-8ce0-fcb707dfdeac | -13.89932 | -48.24965 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a479087c-1e07-353f-82d0-a7252d558810 | -13.89343 | -48.23646 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69fbdb0b-3c58-372b-a74e-a72ddf384f99 | -13.27211 | -51.71571 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5386464-e18d-3056-b474-8e0df49ee813 | -10.85115 | -68.29608 | 2025-09-12 05:21:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85ad4b00-74ea-3fc3-a6e7-b7a0789202d5 | -15.15167 | -52.40011 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a14abb7-beaf-3212-be8d-2c9b15392953 | -12.92356 | -54.75933 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9de3038-c2b6-343f-a0f5-4068873a7ebd | -14.50984 | -53.90782 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91b81400-eead-3a92-a361-8580c08c7cb2 | -12.92728 | -54.79621 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e60bc028-c0b4-3abf-9425-ab55f061bf7a | -19.16735 | -47.96292 | 2025-09-12 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 834db740-ab9e-3867-a947-84480b975fed | -17.37124 | -52.91832 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7058cc31-a8db-39d9-840b-998490798fd3 | -20.00705 | -47.65224 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 57a36320-277c-3836-9398-09d0891beec3 | -14.44069 | -48.42303 | 2025-09-12 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d8acf910-938f-3955-8bad-d58797dc7c86 | -14.51012 | -53.91025 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b233ce8-70bc-3d86-a4c0-7ecd23fd42bf | -14.32853 | -54.12419 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3793ada0-18f1-3cce-a824-e89da49433b7 | -16.4373 | -56.59283 | 2025-09-12 05:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dd33218f-6893-398d-bd98-6240202eae38 | -20.01545 | -47.63729 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e98ed37a-5db9-3364-8070-e214b6827726 | -12.92304 | -54.76329 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df1e8b4c-98bc-3313-9670-16bec15cf4b2 | -15.53411 | -48.54942 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d99802e-d474-3010-b7f1-c8bf3dd2d832 | -20.00041 | -47.64405 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 902fd50c-a885-3bd6-8062-32ef11c40a1a | -12.92513 | -54.74741 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f1a612-09b6-3d0a-9de7-a8a2ce7b5316 | -13.21342 | -51.75479 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ea62b46-f6ce-358c-b5c0-b1b44254444d | -15.5331 | -48.55311 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f77e693f-55f4-35a7-bdea-5b3206032677 | -12.93305 | -54.75257 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f8ed99c-673b-3b7a-bf35-f66adf7ae45e | -15.61111 | -52.73794 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b0f7221-805d-37a9-8ab0-d3a983b197b0 | -17.38265 | -52.95393 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bb4449d7-e8a6-32f5-95f2-507f8a4c9297 | -12.93412 | -54.80926 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd23f1f8-5d84-3f0f-ae81-4cc177260efb | -18.77331 | -48.54395 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9d813253-6d89-359c-99e7-cf519ab2250a | -15.11984 | -48.60731 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6c42047-3f1e-3037-b4fe-2cea1dd6d5a1 | -13.90689 | -48.2347 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7046eea6-668b-3d5c-878b-3317ed56a895 | -14.26663 | -54.77401 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5cfa427-09ce-39d9-9f68-89c53e8bf29c | -13.894 | -48.23079 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9471e6e5-3a7f-392a-8eda-ab7f162ba918 | -14.50402 | -53.91683 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f569b34c-d15f-3647-9ff6-0781358cb6c2 | -18.67867 | -47.66978 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1d68e72-efa2-35e7-9df1-cafca41a2d15 | -12.92203 | -54.80344 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f64ba2c6-c85a-3837-8457-6eecb21e1d8f | -15.80743 | -52.21854 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb77bdb-aa63-3f26-8ac6-cd61f898ddb2 | -15.08007 | -48.00425 | 2025-09-12 05:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45f60a66-99d7-35eb-a949-e8c672cbedec | -12.93044 | -54.80474 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da4b1422-6925-3881-a356-228d17733ea7 | -14.43713 | -52.93524 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68038403-44e3-3df1-93af-3eb2dbe9b6f7 | -16.28686 | -50.04684 | 2025-09-12 05:21:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dde77fe1-50a3-3284-803d-dfbc27126df7 | -15.69205 | -47.01701 | 2025-09-12 05:21:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44c3a594-61b0-3da8-bde1-ed52ab6352ad | -14.40851 | -52.92566 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63bbafdb-28e5-31f7-89f8-875f5abfd597 | -16.63668 | -49.78349 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e29c926f-cb77-3b31-8682-8ca2d42d1907 | -11.77673 | -64.93034 | 2025-09-12 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72f01dea-c11a-3de6-9021-238d08d247ce | -15.91942 | -51.79725 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |


[Clique aqui para ver as próximas entradas](README110.md)
