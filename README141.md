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
| d51d2941-114e-38be-a6f0-f8aedc12216f | -9.2657 | -57.1476 | 2026-09-21 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3768f633-699b-3f39-ac7c-c26fc440b5d9 | -10.8746 | -50.9227 | 2026-09-21 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 78d17dd2-4a33-37b5-b127-d328b1d71efd | -6.1466 | -47.5065 | 2026-09-21 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 106ae30f-4539-3b0e-8d9f-c302ce2e54a0 | -10.9547 | -50.5952 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 193.1 |
| c38b5cd6-9cb3-35c7-9fab-3361d33750f9 | -7.252 | -55.5794 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 313e4806-54ee-3dc6-beba-411a186bdd1d | -12.5224 | -50.0484 | 2026-09-21 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 10dee32f-5da2-3823-beb1-bb2b79d4d4c8 | -10.336 | -50.2119 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 334762b0-49ee-393a-8d42-43ffb68442fc | -9.6853 | -54.3318 | 2026-09-21 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ab5c837e-48ee-36ee-868b-df2d67db5d18 | -8.6171 | -54.6126 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ddd22f64-8140-3197-8c71-e55803ba8dc4 | -8.7914 | -48.7285 | 2026-09-21 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 99.4 |
| cd8c0b55-dd24-3194-95ae-17dbed677537 | -9.8686 | -48.447 | 2026-09-21 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 28c19263-da97-3496-bda0-c9d80a52f0db | -10.4725 | -51.3231 | 2026-09-21 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 4f21aad4-ca30-3722-9eee-a6a1c38dc6e1 | -9.8689 | -48.4252 | 2026-09-21 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 3f38fc3a-a84f-3db2-a744-bcc1bb7862ed | -10.5673 | -51.2926 | 2026-09-21 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4c502782-bf60-3aaf-8a78-6faa207be1e7 | -2.8974 | -57.8181 | 2026-09-21 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6e320107-3f7d-3148-8c0d-1ba2d65b26f0 | -10.9361 | -50.5759 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| f32417a3-b8f6-3324-a5cd-0a32e5b3a6da | -1.1161 | -49.2125 | 2026-09-21 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fd970127-0f0c-3ffa-9941-e57ee8417de1 | -4.5774 | -42.9512 | 2026-09-21 15:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 1c791ca9-ea56-3501-9672-ce2c4ea2833b | -7.3291 | -55.1955 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| fa72102c-d3e7-3a47-889e-65a57614b519 | -7.3289 | -55.2155 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6688cd87-2012-3051-b5d8-2f5c152b13b9 | -6.8243 | -55.8208 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8fe65281-0437-3e87-b9b1-6785ddbdd439 | -12.2723 | -50.1657 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| b5f08a76-8459-30e7-a8ac-5d818058691a | -0.803 | -48.6397 | 2026-09-21 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c72dceb6-2579-35a9-a853-d597cb3284e9 | -2.9525 | -57.72 | 2026-09-21 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 3d9c2b97-98e7-3ab1-a72c-61ed1a8d93f3 | -3.3138 | -59.4472 | 2026-09-21 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6a546431-4771-3a34-bb67-62dca3f3bb78 | -12.3102 | -50.1826 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| b8381632-7f04-34dc-b7e5-e3deaadcd8fb | -12.026 | -50.0663 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b60a6222-60f7-3650-b9d8-abcfa5b09b09 | -2.4636 | -49.2301 | 2026-09-21 15:20:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c5e09bbc-52d1-3ac6-8a53-25cdb72c66aa | -10.1964 | -53.9232 | 2026-09-21 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ac8642ab-4cf4-3119-9fe5-bf774b68e20f | -13.4887 | -51.8539 | 2026-09-21 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 84e4ca84-8b3e-3551-98f1-99d2b131522f | -7.2333 | -55.6004 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b015cf38-490f-388e-beee-01aa9ac2d79a | -11.0804 | -49.7456 | 2026-09-21 15:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 0c6a581b-3a73-30a1-a884-1c7869b2639f | -10.3549 | -50.2099 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| b4fcb52f-3c7c-3ba8-bea6-a2641bcc1bcd | -3.6449 | -58.8647 | 2026-09-21 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 6f5addac-2b58-36da-9759-99eeec255cf7 | -3.4003 | -61.2898 | 2026-09-21 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e0e750f1-7519-3795-b300-597415c7614a | -10.8924 | -53.9652 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e62b9b62-a083-3224-9789-ebffa716e13e | -2.9157 | -57.8177 | 2026-09-21 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 24ab8e24-492e-31ff-899d-e2a68b3a9a28 | -6.8263 | -55.5421 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 155.1 |
| e2fc9ef7-221a-34ff-957c-d541dc652505 | -10.7466 | -50.5959 | 2026-09-21 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| cece182c-8e45-312b-8810-b66101dda6c0 | -7.7346 | -49.3799 | 2026-09-21 15:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5ebb0354-5c6d-3eb1-a669-685545b2dcd8 | -6.4302 | -59.9724 | 2026-09-21 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 207a70e4-79e8-3167-8e2a-35254252ac67 | -6.9223 | -42.9323 | 2026-09-21 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.3 |
| fd70a6da-3487-3367-9b2a-3272d511426c | -6.1653 | -47.5052 | 2026-09-21 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 2c6c2560-37df-3726-b7de-4c07556672f8 | -3.3183 | -57.8677 | 2026-09-21 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 48ac2bba-4866-3740-8c24-514fa92cf584 | -3.3638 | -50.4492 | 2026-09-21 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 40ed8a51-2548-3022-a77f-fad8444b044a | -3.6631 | -58.8835 | 2026-09-21 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| dcac8fa9-ae78-3795-88e5-f4df4f18e73d | -6.8032 | -59.1693 | 2026-09-21 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 71df0439-fc0f-3e5b-8f51-b990dd21b0be | -3.6632 | -58.8643 | 2026-09-21 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 784dd8f3-ea7e-31a3-8a6a-935cbcf99f68 | -0.803 | -48.6825 | 2026-09-21 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b542305f-898d-3e8f-95b0-48c09075f794 | -6.8058 | -55.8217 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 52b7f076-9aea-3f62-ba88-46b798a1cc9a | -8.028 | -61.3435 | 2026-09-21 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3f8a08e9-7018-35ab-8d13-b1299f19af51 | -7.3125 | -54.9359 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4a9eec0f-bed3-3646-986c-e3d12508e351 | -12.5412 | -50.0676 | 2026-09-21 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 33cee2df-6961-3924-99a3-f4396875e5df | -10.7463 | -50.6172 | 2026-09-21 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 89329e14-1cd3-33cc-8ade-7e574954fef4 | -0.803 | -48.6611 | 2026-09-21 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 811c29c9-79ed-3b32-8888-ae75af702532 | -3.4599 | -59.54 | 2026-09-21 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 92f9a4d2-2548-3a88-8236-682866f42645 | -10.4105 | -50.2897 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| cb1c3270-3f86-3c35-9f84-e218ee9b5be7 | 1.0397 | -51.1445 | 2026-09-21 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e6f6e6c1-13a2-3c91-8318-6eaa0f3ce7d3 | -11.041 | -54.1567 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 305.4 |
| 9fb6eedd-a112-31c5-abad-1663f5adb965 | -11.7823 | -49.8152 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3755515d-0575-3d27-886f-de1167a7d59e | -11.0412 | -54.1362 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.3 |
| 359f016b-f72b-37aa-88a6-6c0c7c430157 | -8.7911 | -48.7502 | 2026-09-21 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 5a85740c-472f-3548-8eb9-23a29ff07b67 | -3.3359 | -58.1191 | 2026-09-21 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 6b95812b-8366-37a7-a124-2267ece5961d | -9.6665 | -54.3332 | 2026-09-21 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3f372339-4c9e-3ff5-8c52-9b7fd78e7098 | -6.8264 | -55.5222 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| c268756b-1fcf-3896-bbf8-76755a32b448 | -8.4922 | -47.0257 | 2026-09-21 15:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cd2250be-88bd-362a-85de-07b062d3fb2b | -10.8921 | -53.9857 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bcec6e20-b4b2-3d3c-8470-63fa3851f417 | -10.8472 | -50.1581 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c723370f-31d7-3770-a9b4-738662c6b430 | -13.5075 | -51.8728 | 2026-09-21 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 288.4 |
| 7eeb0eeb-9ce3-3f05-bedb-a3dbd6689bcb | -10.4102 | -50.311 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 7a9b6744-c30b-31f9-bb71-9929346e925c | -8.7706 | -45.8567 | 2026-09-21 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 00367c62-756e-3a4f-8a01-db05f1014cd0 | -10.4483 | -50.2858 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a583228c-decf-3a24-af9e-654048573091 | -6.3013 | -59.9771 | 2026-09-21 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6bcdcaef-e53a-3ecf-9f2e-7cbf9ce005e7 | -8.1874 | -54.742 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| d701cb76-0a04-375b-b388-6c36371d0c83 | -11.8359 | -50.046 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| fd021653-e53d-3592-95f3-9bce987477f4 | -5.7305 | -53.4446 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 129beb77-2cd4-301a-8150-da1082cab848 | -5.9985 | -45.2476 | 2026-09-21 15:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2439b47c-0944-3555-8c49-d978fa19b0ef | -4.0944 | -52.1252 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 388e74a4-0a0b-3253-aeb8-75b4f33760f1 | -10.9361 | -50.5759 | 2026-09-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 90a3c82d-6b94-3c59-9b02-0355d8a6aa35 | -6.8466 | -55.2817 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 95a3e683-7b52-3d9f-beaf-9bd910615876 | -10.8743 | -50.9439 | 2026-09-21 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b719173e-3d89-3f3b-a297-123d8b83afdf | 1.2608 | -50.9552 | 2026-09-21 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| dd47ab2d-9d40-30e5-90ac-738087480c06 | -10.5673 | -51.2926 | 2026-09-21 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 385411f2-9601-3b17-a896-062009f375a4 | -9.8683 | -48.4689 | 2026-09-21 15:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5c4f9f39-bc7c-33f1-b7b1-05a12967458e | -8.1684 | -54.7836 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 88e4941a-fe88-358a-97dd-6ad1e3e4cb82 | 1.2609 | -50.9344 | 2026-09-21 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bb5a3ae1-9e8f-3e12-97ad-409e34fd2762 | -10.2632 | -50.0055 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9538da8a-44b4-3969-9827-7fe7c60e6aad | -10.3919 | -50.2702 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| aaf62f55-2984-314a-b102-b8b165bc1968 | -3.3359 | -58.1191 | 2026-09-21 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8f1894a9-0473-3ccf-b127-1a218540a042 | -3.4632 | -58.4062 | 2026-09-21 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 095bc0cc-0f44-3fef-8a03-26b8b3150ab0 | -3.478 | -59.5779 | 2026-09-21 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 94bf53c9-220e-3721-a3a3-20f5a21bb2e5 | -12.5227 | -50.0267 | 2026-09-21 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| d5d35e45-4d8f-3fb4-823a-177ee860e1f0 | -10.7463 | -50.6172 | 2026-09-21 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 871853a7-e29c-39f8-812e-84d54a2ce09d | -12.2723 | -50.1657 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| c6b1ba0b-1c46-3d1f-a48d-f6ab2876199b | -8.6171 | -54.6126 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 612eb5ab-57cf-3eba-a6cc-2d4b3634e554 | -6.9225 | -42.9088 | 2026-09-21 15:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| 75f64654-cf95-3d9a-abd2-3c3a21626eeb | -3.6631 | -58.8835 | 2026-09-21 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e4695cc7-7bcf-38a0-9bc6-f4acaf60ae69 | -5.8226 | -53.5011 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 08f7a7ce-1ce7-32cd-a920-a3d6e869f757 | -11.3996 | -44.0995 | 2026-09-21 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| a0e1658d-9dc4-3d70-89b0-9dfbaff4e0b9 | -1.4487 | -48.9526 | 2026-09-21 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |


[Clique aqui para ver as próximas entradas](README142.md)
