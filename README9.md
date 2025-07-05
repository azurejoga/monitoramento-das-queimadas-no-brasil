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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c608ac88-7b6a-34db-9ddb-1b516e691d94 | -6.87468 | -44.33985 | 2025-07-05 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a57b05b-46f2-351d-a854-ebc35728514c | -7.89664 | -55.42116 | 2025-07-05 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 311bc388-5ca7-36bf-9252-dc751abd3072 | -10.60499 | -46.42771 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55fce72c-8b2b-3c1e-8c67-c9674e4cfb72 | -11.10878 | -48.90637 | 2025-07-05 04:19:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1609548e-9601-33b2-951e-2f61333a167a | -5.99789 | -43.73417 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a24d6f6a-e145-389b-bdb8-228354eb0a4f | -10.64975 | -46.40276 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d09aff2-2317-3538-8d6f-2387856a83e0 | -10.65031 | -46.39923 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc004f99-e6eb-32ed-b8d2-4d6638643dcd | -5.72297 | -49.10144 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4b54cd-7ed9-33ed-a817-677817c0f60d | -8.50116 | -47.46768 | 2025-07-05 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d576946-0f47-326d-bfc4-97b0f71590f4 | -6.67694 | -43.15655 | 2025-07-05 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7ece29ee-0af8-3102-8954-9c9315682b66 | -10.56024 | -49.13086 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fd5e71b-a352-31bd-8312-d664b2d1f944 | -8.09128 | -45.39568 | 2025-07-05 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b5eee0f2-6f2d-3147-89fd-9ee8fa082b68 | -11.45019 | -45.11433 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f0faad7-1a27-3cfc-90f4-e2955a930557 | -10.63572 | -46.46916 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6226b0ce-8359-314d-9c74-f277fb4308bf | -9.58714 | -44.60673 | 2025-07-05 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 511afd47-3277-313c-9870-53ecd7837664 | -7.15673 | -44.31646 | 2025-07-05 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 222bf282-9ca4-3fd1-a74a-a9d0e2e441ed | -5.87122 | -50.14886 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 878fe413-1fa3-3a86-9c9c-2a6eb83c8dca | -12.01525 | -47.76169 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fcd3d182-d864-3dd8-9069-7840cba6ee98 | -8.09292 | -45.38528 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c733b3b4-0a8f-37d5-9811-19ff85b63ef3 | -7.22945 | -43.09276 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df59e44a-77e5-376f-89e7-03e7777ef5a6 | -11.94383 | -48.42785 | 2025-07-05 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b642980-fdb1-3907-8867-80ffe947d1bb | -5.42836 | -49.08169 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 561e8f98-0989-3b0d-ac24-f8e5640d91e9 | -10.81862 | -54.02658 | 2025-07-05 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48e772fa-ad02-3be7-a221-7dbcb5f546cd | -7.01774 | -49.18204 | 2025-07-05 04:19:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7a1637a-0872-3012-b071-d59daf0bfccf | -6.88983 | -43.98069 | 2025-07-05 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd9efaca-4f24-36fb-9cf2-de8feda604d7 | -9.94977 | -55.20128 | 2025-07-05 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03cd50b9-31d4-34fa-a841-5e175bc1c635 | -8.38225 | -44.05314 | 2025-07-05 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1fee0c7-61da-3fa7-8dd8-1307e7f42f13 | -6.69783 | -44.05886 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db481e8c-8e1d-3297-8372-d63dbf3f530d | -10.36829 | -46.99192 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8d251d3-25b0-31df-a9f7-cc6e2a6a5c63 | -11.02137 | -56.26178 | 2025-07-05 04:19:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db765669-1c39-31eb-a386-a0f272353076 | -11.87625 | -44.88058 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 665c44fc-bafb-36e6-a170-633fde285cf7 | -7.90307 | -55.41825 | 2025-07-05 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 852f9cda-1b97-3f32-822b-bb9793f8209d | -7.22318 | -43.088 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83c50bc3-f6b9-30c5-9fd4-3bc25b1c3610 | -7.25107 | -43.08849 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 613cb438-22b0-3063-9fc2-5804a6721581 | -6.07277 | -44.60014 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 956ece63-71ca-30ba-978f-5846b73e2389 | -6.99767 | -44.29131 | 2025-07-05 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 473a7c6c-bd73-3c76-80d0-2405942a42ad | -8.90224 | -48.02295 | 2025-07-05 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fe7061c-fff3-3192-b439-c79d4d0f7129 | -7.44841 | -43.08007 | 2025-07-05 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e94a2cd9-131a-399c-bcfb-fe9675e4c7a3 | -10.63924 | -46.40465 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 656a11c1-a458-3b13-9770-a564adb51785 | -10.65638 | -46.40383 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 524bc478-906f-34d0-b674-cc762479dec2 | -7.28774 | -45.70559 | 2025-07-05 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cde19be-a176-3db7-98a6-763102805826 | -7.42413 | -49.53774 | 2025-07-05 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6302a45f-6928-3498-85fb-8b51c0762921 | -10.65695 | -46.40031 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f73581c7-741e-38ff-ad35-4e5bdb89ec8b | -11.45351 | -45.11486 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b6b77ad-34d6-37b9-85e9-03d733eb5327 | -7.44898 | -43.07635 | 2025-07-05 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad121951-1ba9-3b75-a126-bb35b5b178c8 | -10.60831 | -46.42826 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2a38bc6e-e97c-3937-a79c-27eec9acca2d | -10.66082 | -46.39733 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30042470-d758-3289-bb60-cd0b03de5f41 | -11.52477 | -48.95596 | 2025-07-05 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bfd7298-37d1-34ee-85e9-701b91b3c40d | -8.01297 | -49.72212 | 2025-07-05 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 204bd4cb-2daa-3bee-946d-d93921a27c79 | -6.54514 | -46.44006 | 2025-07-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19a0cc5d-a855-3837-8fb5-d466a4dc07ce | -8.01298 | -49.72018 | 2025-07-05 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 085c5ee9-a5b9-3783-a0bb-28f7bf0a2bc8 | -8.08412 | -45.3981 | 2025-07-05 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1277283d-be03-305a-bbbd-a5e42e277089 | -10.30646 | -57.14137 | 2025-07-05 04:19:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0188f13-e5a4-3c2c-8700-f79a84af4c46 | -11.87791 | -44.86968 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceed5979-18e9-3857-bd3a-0ca5e0335075 | -8.08742 | -45.39862 | 2025-07-05 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1caba753-76a9-30ed-b7ef-311d9fd96d72 | -10.37081 | -47.56021 | 2025-07-05 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84dc49a6-da97-32a7-8ed1-426862ae1a44 | -9.78144 | -48.25488 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2b8fcb5-e3de-373b-abd2-2e1a213e4289 | -7.45546 | -44.47045 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cb2f5bd-381a-390c-abee-cc87053ca6df | -7.10079 | -42.4049 | 2025-07-05 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3a88e6c9-9f51-3441-aed1-f906f783dd55 | -11.8768 | -44.87696 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 107472e7-26ec-37a5-b5b5-c229d6ea6b42 | -7.02522 | -44.98106 | 2025-07-05 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3f7645a-3187-30bb-acba-89d89601fabe | -8.99914 | -47.45084 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da320e6b-f494-3914-939e-561308d6bc35 | -11.00385 | -42.79089 | 2025-07-05 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d6d17246-e6a5-376f-b568-6e005e50d31d | -7.24139 | -43.08319 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b77209c-47e6-3c84-80af-0295e29816b9 | -7.00266 | -43.53997 | 2025-07-05 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61f2480b-1950-3a7f-a48e-710c55050e84 | -13.12033 | -46.91323 | 2025-07-05 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20a91fee-3d06-3862-a0ca-0d75b4eb980a | -9.61075 | -49.02303 | 2025-07-05 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c1bbee-eeac-3666-b010-c6d108f44243 | -12.01684 | -47.77336 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc19d7cf-0b7a-369d-97d1-fa5f512341cf | -5.571 | -46.67236 | 2025-07-05 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae9e6e0e-1260-3df3-88bc-143e80ed4ee0 | -10.56097 | -49.12652 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 848ea64a-103c-3704-a369-453e95d317ca | -6.87672 | -48.16838 | 2025-07-05 04:19:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32bcd3d6-3eaa-3ea2-ad1a-57dfd382099e | -11.87398 | -44.85056 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6286500b-e6a6-31d9-a0c3-2e0784eb0b0d | -12.94588 | -47.13247 | 2025-07-05 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024f0867-ef58-3c08-ba81-9dc3f2905dab | -7.95006 | -44.84738 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccd4f494-7fc7-3c3c-8b30-ab34b8e73118 | -8.09237 | -45.38874 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96455c71-3f22-31d7-a9fd-17ff40f9f0c9 | -11.7316 | -48.87241 | 2025-07-05 04:19:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 519c1744-d9b2-39d6-bee5-f7360b2623d4 | -10.30131 | -57.13535 | 2025-07-05 04:19:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bfa52f2-32eb-3b3c-a4cd-d243e7767736 | -7.11331 | -43.89643 | 2025-07-05 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 255322f6-09c6-3557-9ea3-2a2dd55c65b0 | -6.77739 | -45.53792 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5759f336-311f-3d82-9644-071553365879 | -5.72085 | -49.10911 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af3a5d09-d6e0-3e0d-8fb7-7e492dbe8243 | -7.24766 | -43.08796 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5113b912-d068-35be-99e2-c0035e5bf7ae | -10.37223 | -46.98885 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 102b9d71-5eeb-3b17-9c43-73e98e5b6fe4 | -7.3436 | -49.6343 | 2025-07-05 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a33d9c5-7a9d-396c-8ff5-9dffd8f210b8 | -11.04855 | -56.74376 | 2025-07-05 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9c96595-c10d-34b7-97e9-72577540ce24 | -6.27812 | -43.67734 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc18be16-8eb0-34d8-b15c-896283a34eab | -10.60146 | -52.84063 | 2025-07-05 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b2ce98-646c-3c77-a151-6a51cdc5d8dc | -7.22347 | -43.08436 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 577daaa3-c635-379c-8d8e-e55b946fe4d2 | -10.31992 | -49.93364 | 2025-07-05 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 668357d7-5ac9-3fd1-bee7-f91387440550 | -10.60555 | -46.42419 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e17633a6-ec2a-3385-856f-a5a77fc8ff0f | -6.76454 | -44.86869 | 2025-07-05 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbb323d3-776d-35ca-8009-a86aa7a7efa6 | -11.87622 | -44.85831 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e45070cb-0f14-3ba2-ba5d-9c03f6ac17df | -11.04938 | -56.73948 | 2025-07-05 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb7bb3b4-d850-3d3c-9f59-8565b4d33d1f | -8.09513 | -45.39273 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6fb9eb-6002-3c7b-9669-4eb39df74770 | -5.99346 | -43.74069 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47bc25ea-a185-37bf-a8d3-1d436a55b763 | -12.03399 | -48.75515 | 2025-07-05 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19942c32-f29a-393c-adf0-ee0ce49fcdba | -6.628 | -44.22328 | 2025-07-05 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 502ce123-2da3-3714-940e-5063f0635bf0 | -8.08852 | -45.39169 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a46a136d-4e00-3c1f-b702-10833f1acc95 | -10.2046 | -47.99699 | 2025-07-05 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d868c0-9479-34bc-82db-826da32f3a32 | -8.08907 | -45.38821 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7759b9d-46a4-34ea-88f0-400b9f9a5123 | -7.89689 | -44.53613 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README10.md)
