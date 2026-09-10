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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4f76e66-fa5a-3b3e-a9f4-980a9cb060e0 | -8.71135 | -44.7171 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53b39875-d1c4-3f31-b3d3-7df2888b1927 | -7.05668 | -42.70443 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b426628-600d-33af-801b-fa11e2be1d32 | -7.26267 | -45.35231 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| adeb9ca5-5ab1-38dc-8596-3073f6ee1b15 | -9.68856 | -43.47525 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb434588-38bb-3bfe-9689-199265c65750 | -9.69431 | -43.46058 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92dadcd2-be06-37aa-bb54-af897758397e | -7.20265 | -43.6384 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24d0086d-199c-3bf5-a20b-e6fee6d056e4 | -6.17033 | -44.63633 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 711c8e84-10a2-34b6-8ca5-d2a0d5a17ad8 | -9.33909 | -45.6466 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54df5c6e-195c-34bb-bfc8-c1250b46eec2 | -9.33358 | -45.63856 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3419f6f-e372-376c-b8e3-790b2890eae3 | -2.93116 | -50.46946 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60622fd4-4d91-3d78-a552-7bc0dcdf1b53 | -9.69488 | -43.45682 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cc18141d-059c-35a4-9484-a60d857eec4d | -7.05021 | -42.72322 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ba9a654-77ef-3c27-b130-6e58ec1828d4 | -7.49447 | -45.28301 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b83113d-587a-3abf-976e-213164a2d92e | -6.33298 | -43.81895 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6c25a83-1bc1-386f-b421-8d3572ee6b7d | -4.42608 | -47.53719 | 2026-09-10 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6920fc0-9ebc-32b4-b7d6-acd6b0fbbb3c | -5.79976 | -43.64533 | 2026-09-10 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6945966-f568-3a1e-8bba-d15d11e0338f | -7.97618 | -43.98574 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 553d5596-1342-309f-bfb5-97d102af6a9d | -7.98179 | -43.99393 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f0d8265-8c6f-34b6-aeea-7f45acd39b64 | -9.77733 | -43.44978 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae2c6d0a-2907-3f48-b0c2-0f8a2f0e2365 | -8.08398 | -54.85892 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c651658b-c4c0-3b39-aae6-55e156933d59 | -8.96094 | -44.40194 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6568bb9-b74a-3018-80cb-cd839bed68f9 | -2.93854 | -50.47968 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 536854f7-1392-3ce6-992d-30926049deef | -6.16207 | -44.64565 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4ac38331-2081-3972-8ae4-79d784123adf | -5.76294 | -45.08455 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 529b7892-75de-3a13-b1bd-e75c85b01adc | -7.49912 | -46.15082 | 2026-09-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ec02a04-5ad6-37c7-a10d-a9ee21d03ebf | -5.66353 | -44.40361 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9275e35-a92e-33e8-bc48-04e70b64c9cb | -6.71228 | -45.45993 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7886e0a7-dfa3-3a01-b565-7baeb8f49c4f | -4.8586 | -56.02076 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87333d43-5841-345b-9f2e-a102837de865 | -5.85403 | -44.96117 | 2026-09-10 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed710a0-9f93-35be-8552-93e7cdf58221 | -4.85459 | -56.01418 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 063454a0-f341-3922-b9ec-730e165883c0 | -6.77428 | -42.73684 | 2026-09-10 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa32f7e2-c8e7-3e00-b597-040dc7bb4cba | -9.69374 | -43.46436 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e97dbcd-d20d-3ce0-bb14-95086ba2b03d | -5.68228 | -43.39419 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1010c4e9-752a-3378-abf9-9b3d965893af | -5.28419 | -55.9697 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 468223b8-60b7-381b-94c7-90ae9618ff25 | -4.28263 | -46.53202 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a73d943-3e61-37a4-afea-26819703baa6 | -10.18 | -42.22477 | 2026-09-10 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d0100bcf-9ff6-308f-8bbe-4687ec439c20 | -7.90838 | -46.70817 | 2026-09-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba85af2-e456-3eaa-a712-c0e1ad43b88b | -6.76442 | -58.61086 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37f9bd8a-46ef-351b-945c-23041ef706ae | -2.73589 | -57.63747 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 83f6e480-c26b-3211-9927-20fd993e8144 | -6.16647 | -44.63926 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dbd4b60-1ef9-36cb-bdc2-89971994a250 | -7.94894 | -43.79361 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4750521-2073-3711-b7c2-617d843ca088 | -9.54053 | -45.68286 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2c3af0e-00c1-3f19-9473-3c0c052e6a87 | -4.86113 | -56.00672 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a7050c3-e6ae-31d3-a3af-35b801048447 | -6.5023 | -58.38139 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5321988e-076e-3c2c-a5a2-70cfc16fc777 | -5.76018 | -45.08057 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1f1ca82-fdd0-34d6-94e8-cae92b8ddd29 | -9.33302 | -45.64205 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1da4b71-53b7-3979-ab0d-02b6fddf6457 | -6.7812 | -58.90827 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 587b743f-6e4d-3eab-bb8f-de55c657ff91 | -6.23157 | -42.85321 | 2026-09-10 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f47dc50-dd03-3135-9fd5-c6ba1ac7452a | -9.71913 | -43.38993 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 8571b3b9-6063-36e1-a97b-e9a96e03c530 | -6.77438 | -58.88438 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66b8f0ec-9008-3630-a081-e3c074859693 | -5.68846 | -43.39878 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 969c1d23-a6af-3a4c-963c-10bebc33a8de | -7.19307 | -43.61109 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b81357c-5be3-3e1c-b620-f6176793f3dd | -8.96874 | -44.41778 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bec2126c-8639-35a4-a6c9-5dd969bcc0f2 | -2.89974 | -42.60687 | 2026-09-10 04:25:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8ca8efe-3ea5-3a57-8d6f-686c7456a95a | -7.56147 | -47.81459 | 2026-09-10 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d78159cc-2c8e-3a30-90ff-10dd33c1aade | -3.24478 | -47.24584 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ca618ee5-8a02-3ae4-bcce-e67a794239e0 | -5.55387 | -43.43254 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 932acfca-5c7e-304b-b680-a2eb0e1e09b8 | -6.24862 | -51.67556 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ffbf26a-065e-34e5-b1cd-24ee9b0a628f | -9.66243 | -40.63059 | 2026-09-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d824362c-e57c-3c34-9280-5c1c7b35a125 | -5.55668 | -43.43663 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac9f8056-6a5f-3c58-8fa5-e38720f2fb33 | -7.49116 | -45.28248 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcb74466-4fac-371a-8a2f-7e51d07d4fab | -9.69259 | -43.47196 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f3ebef9-ae95-31f3-ad9f-16e4fd1cb843 | -7.46044 | -42.12619 | 2026-09-10 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 39b85eef-a47f-3902-96d5-00af9c109403 | -6.29431 | -45.88469 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc7722d5-5440-38bc-bb48-2c6cc74a19b2 | -8.13407 | -41.12527 | 2026-09-10 04:25:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb1be603-27f7-3f04-b359-c90ef5bedb67 | -5.76404 | -45.07763 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 47235e6c-f2cc-35ae-8e39-78b955c25be3 | -7.48564 | -45.27455 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b4a22fb-b3b1-3fc1-ab6f-1e51f2392ee6 | -2.94367 | -50.47605 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b415b0c4-f53d-33f5-90b4-91a3dd657f89 | -9.771 | -43.44488 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03a8cc08-42b3-37fb-a898-48050f6cf33e | -6.76418 | -44.57413 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 303232d6-1fca-3903-8df2-9b755a46eb36 | -7.10935 | -42.12681 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4092f72-c238-302e-a076-296e18e12628 | -9.77387 | -43.44924 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64e1b122-2327-3d09-b877-b7cb2b25d3e2 | -7.20489 | -43.62401 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc3e72fe-71f8-31d8-8378-a9fcd9c5a7df | -5.75853 | -45.09095 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7591379f-a755-33c5-bc34-bbc548ef2742 | -1.70029 | -53.69849 | 2026-09-10 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad609732-df84-3037-ba64-a71d7c2e727e | -7.48233 | -45.27402 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91daf0ec-80d6-3a13-bc4b-581803506078 | -9.01019 | -44.84699 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c25734b-37f6-3023-ab89-e6952f442947 | -9.70701 | -43.39982 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2a310fb6-d54e-328a-b716-ef6255a2dbcc | -8.08719 | -54.84088 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea12e1dd-0744-30c5-ac58-ef4c8bbac8e3 | -7.511 | -45.26438 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99529fbd-f95e-362c-89db-a9d7edb6ea02 | -6.17782 | -43.02015 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65eac8b7-c7ae-30a2-a26e-2f752f39abd7 | -5.76901 | -45.08905 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 80e3c5da-67f3-3625-9e81-9709216e6ad3 | -7.04613 | -42.72656 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9f30dca9-9b76-378a-9f54-8f705dd64889 | -7.68849 | -44.31162 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bbcb5f0-f2d8-362a-9e7b-70c8faf2ec67 | -8.31964 | -45.11303 | 2026-09-10 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4783ccfe-8ad0-3ac7-81f7-5aa31ca45729 | -9.30371 | -44.36006 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad83c5d1-b7af-37fc-9086-eaf0c934aaa7 | -5.76625 | -45.08507 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c732b92f-17bc-3239-aa1b-27c247c05588 | -7.56432 | -47.20528 | 2026-09-10 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23219655-7614-3cc3-9096-0243ba1b29ee | -5.60688 | -44.84758 | 2026-09-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 61277408-61ec-30c5-a587-dd95ad91347e | -7.94837 | -43.79723 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e584820-7df3-3fba-bdbb-cc758f50fd00 | -6.16757 | -44.63235 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cfe80e7f-3345-3f39-a0bc-e91719b74678 | -7.97788 | -43.997 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c85c9fc-e3cb-30d6-9406-05e6ca43449e | -9.01351 | -44.84752 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db91defe-ecdd-3c61-96dd-359ad014508b | -7.15334 | -46.542 | 2026-09-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0663fcc8-c8c2-3ea0-bf0d-5040c81d2a30 | -6.71608 | -46.3317 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76eb45ac-0a2c-347d-ad2d-9a2c52a01d2f | -2.9334 | -50.48336 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff2231a2-9e85-32ba-b325-e400ac4b304d | -7.50274 | -45.27372 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cc4cbc0-5cb1-35d5-94db-36939212e888 | -5.41437 | -41.84044 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| de376ae9-90b5-3192-afe4-79023f50eeed | -5.38235 | -46.29824 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6df1f0f-8206-31ce-85af-98341a70015b | -6.84357 | -47.90382 | 2026-09-10 04:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
