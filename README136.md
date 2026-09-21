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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035ebea0-bc59-3901-8dbd-7932582bf305 | -10.5906 | -53.9918 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 616cda5a-a7e4-339c-a277-33bb2c0d6ada | -6.1466 | -47.5065 | 2026-09-21 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8ffc503c-b26e-326e-b36e-f72ba30e1c9d | -4.3542 | -55.6455 | 2026-09-21 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| be599742-490e-34f7-9b2d-3fd3a3d873dc | -8.0465 | -61.3427 | 2026-09-21 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 43dd186d-195f-3ff5-a139-9ebe779dd614 | -12.5764 | -49.0852 | 2026-09-21 15:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dfd99921-1a05-392c-a293-edf8354f10fe | -4.8683 | -55.8457 | 2026-09-21 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7aef9ded-63fa-3245-8821-38fc19498655 | -7.5661 | -61.3239 | 2026-09-21 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0d7129c9-fbfd-3a61-984d-36647b932e9a | -10.7652 | -50.6153 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 5e812d37-e26d-3c8c-a41a-9947db3dec33 | -6.9223 | -42.9323 | 2026-09-21 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 92d1f570-6157-3921-ad80-9350f7f2929c | -12.2532 | -50.168 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3809c846-5637-3ef3-8119-eddaaa0de048 | -3.1698 | -58.5859 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 68b0b8f1-4ead-374c-bdf9-c4239a86377f | -6.3196 | -59.9956 | 2026-09-21 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a94a5a64-96d7-3e36-8717-5c44638e0054 | -3.3824 | -50.4276 | 2026-09-21 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2b070257-3cb8-3642-8d90-6b9f1fafa35d | -6.0033 | -44.7247 | 2026-09-21 15:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fe299177-37e6-31c0-8c59-2a7c13efbc1f | -10.0898 | -50.2795 | 2026-09-21 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 0d9249bf-da1c-3abc-8ced-81bc8123f2b3 | -11.8168 | -50.0482 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 59a35ed1-7c13-35e9-b1b5-9ded48cb026f | -11.3813 | -44.0554 | 2026-09-21 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 8a773546-220e-3ef0-8065-97f7900b5e0b | -6.0194 | -51.81 | 2026-09-21 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 12a58ae4-70ee-30f7-86c5-b176b77d55d9 | -5.841 | -53.5205 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| c9404a48-0c38-327f-901e-ead8c655a109 | -11.8559 | -49.979 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b18388e8-af7a-34e1-bebd-a26a33323b09 | -8.5989 | -44.5531 | 2026-09-21 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| eff428df-14ac-3c35-991d-18775b6a9f4d | -2.4636 | -49.2301 | 2026-09-21 15:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d4af8ece-f26a-3445-b8f7-fa3480207b5a | -5.6594 | -43.4139 | 2026-09-21 15:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a17c84e0-5171-3e14-b9b2-abd38b54ae3d | -6.183 | -47.6133 | 2026-09-21 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| b8fc9259-31b4-36f4-a117-a1caf21b388f | -2.9525 | -57.72 | 2026-09-21 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 259ffa8f-03c7-36c1-a4ba-e062c5616a0d | -3.4369 | -50.6142 | 2026-09-21 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5cb28950-2fa9-39f1-972b-58dd2a58ba26 | -4.4303 | -55.0867 | 2026-09-21 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b5e26a9b-82ac-3e62-9b0b-a9edf2629d99 | -5.6411 | -43.3687 | 2026-09-21 15:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 0bdbec9c-5b5b-3e96-86ac-cb62aa957bb6 | -10.8002 | -50.8243 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| a3ee8592-267b-3fc0-95dc-e78112ee5cb1 | -1.4302 | -48.9529 | 2026-09-21 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ed509520-c91b-3d6b-b3e7-f0dea8b29b4a | -7.5889 | -57.6757 | 2026-09-21 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| ea1adc53-f329-361b-ae95-4fed8836ab14 | -9.6665 | -54.3332 | 2026-09-21 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| bad30c1a-e6ae-3b90-989a-3fb99b85c4dd | -5.6221 | -43.3934 | 2026-09-21 15:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 5e10cbfd-4257-3d4b-a74c-f7051232904b | -6.5759 | -45.5419 | 2026-09-21 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 5c85b525-4011-3cdd-a69a-4e266a2dd802 | -3.3358 | -58.1384 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 37afc815-6fd8-34b5-be0c-ac623fc86072 | -10.6889 | -50.6658 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 3df7064f-8e1c-3a89-a836-02e372d817a1 | -8.845 | -45.9391 | 2026-09-21 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6065de3d-0bfb-3789-bd6d-378a4cba2648 | -2.8608 | -57.8188 | 2026-09-21 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 736df794-5dc3-3872-81e6-e7a3c63a397d | -11.3606 | -51.3797 | 2026-09-21 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 233d1f20-4780-3bc1-ba98-c4d0fdcaf0bb | -5.757 | -47.2915 | 2026-09-21 15:00:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9819a778-6c38-3ebd-82fd-49c25101c6e6 | -6.9949 | -52.8453 | 2026-09-21 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ef2ae2df-d683-3952-a234-b8b9a185122e | -12.8899 | -50.9695 | 2026-09-21 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 93ea5480-e851-378d-931a-0d05ca9cdab5 | -11.7162 | -54.5654 | 2026-09-21 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5ee4d083-643b-38bb-a663-572d52c7cd7e | -5.5463 | -45.6853 | 2026-09-21 15:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ee619dcc-46bc-368e-8641-5e1b20b22b39 | -6.8448 | -55.5411 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 8c64e45b-c384-383e-bb45-f4e41354cefa | -11.0614 | -49.7477 | 2026-09-21 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d22aabae-9773-38cd-8f3b-9437bc22f7da | -3.3359 | -58.1191 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 8f6eba82-3f50-314a-9669-c1942888982a | -3.753 | -59.419 | 2026-09-21 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9dcfefef-f599-346d-afb1-4ec5a2b48207 | -10.4288 | -50.3305 | 2026-09-21 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| af2df60d-f485-310f-91b5-281f7dcda52f | -8.1871 | -54.7824 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6b7a51da-0432-3217-b077-b1716dfde85a | -3.6631 | -58.8835 | 2026-09-21 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 52b89ae0-4b70-3c90-ae8b-804aa5800c2f | -8.1874 | -54.742 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 0bb08ca9-a594-3094-aa45-988d4b86c55a | -11.3606 | -51.3797 | 2026-09-21 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 99b0d3b2-c93e-3e4b-a71e-88bd9c0e36d4 | -11.8354 | -48.8526 | 2026-09-21 15:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| bec2ac5c-af22-3c06-909d-d51afa72e61c | -2.2619 | -48.7445 | 2026-09-21 15:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| da63a84c-994d-3119-9bf8-ea5437b72773 | -6.8466 | -55.2817 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 247752b7-b7a1-344d-8b8e-f4e20166797f | -3.3 | -57.8681 | 2026-09-21 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 4035d3e6-92fb-340d-a4cd-a93cf58b25c4 | -9.6853 | -54.3318 | 2026-09-21 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 331263f3-f28e-33f6-acf8-65bfab87564b | -8.1684 | -54.7836 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 90c7462d-19ea-39c4-994e-9ee7c91c9f10 | -11.0614 | -49.7477 | 2026-09-21 15:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e377e155-5d3b-347d-a08f-d7b2c4cc394e | -8.0892 | -55.3511 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0433d7c1-cf55-3b8d-bae1-a8b34fddbdee | -3.5356 | -58.6939 | 2026-09-21 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1b863bb2-8831-36e1-bf51-3fda6177a0e6 | -6.9225 | -42.9088 | 2026-09-21 15:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 863149c2-c15c-3d80-b97f-51b889f7e885 | -7.252 | -55.5794 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 71952b05-c220-3203-823c-3934516cfaad | -6.4107 | -45.1934 | 2026-09-21 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c5cb4699-d7bc-3500-93a1-6b6f4006ea89 | -10.9547 | -50.5952 | 2026-09-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7dd42f27-e19d-3e6b-803a-4982b9c8badf | -10.3357 | -50.2333 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d297d9f0-5e08-3ec7-b3c1-48cf609b4a42 | -4.4112 | -55.2466 | 2026-09-21 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 22a032b0-285a-3e35-bfce-7dceb6125cc4 | -6.0196 | -51.7893 | 2026-09-21 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2e3a8ef9-1dde-3cb1-99dc-77df79029f45 | -8.0279 | -61.3626 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 69e9f518-5d2e-3750-b99a-d5eb6dd696d3 | -7.5705 | -57.657 | 2026-09-21 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 07c63d85-3288-3d70-867e-b171bb930642 | -6.5829 | -58.9851 | 2026-09-21 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ba34c2b0-ee22-3ee2-81f8-9dfb3977f2cb | -10.2976 | -50.2585 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f9df3e0d-8127-3c12-86de-fae184356b6a | -10.7463 | -50.6172 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 3356cd13-c25b-36d1-822d-5f916f692103 | -10.8665 | -56.2377 | 2026-09-21 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 37a65fd4-0db2-3ca7-95ad-9605cc7be980 | -7.3259 | -55.6153 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| c6c2e768-11ca-388e-9263-3607dff8dd87 | 1.2423 | -51.0178 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2085ef5e-ee72-3c64-a3c0-bffec97c2b77 | -2.4636 | -49.2301 | 2026-09-21 15:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 4ec5ec63-7b48-35a4-bf0b-698355d7cc94 | -12.5412 | -50.0676 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 8b8892f8-a181-3788-b024-fafad44be419 | -11.118 | -54.0268 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| dddf5023-497c-375c-ab03-f88bfbe656ba | -5.6781 | -43.4125 | 2026-09-21 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 31800969-6e1c-35b4-917c-836b6e36a469 | -9.5595 | -66.0172 | 2026-09-21 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 67cb6d66-c570-3d2b-8583-88f16d1d0f75 | -7.3376 | -44.4744 | 2026-09-21 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 8289bf51-b552-33d0-a9b6-a9c9b0442399 | -5.6594 | -43.4139 | 2026-09-21 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 44df906d-a7d0-3e33-9d07-6adbfb0b8a4f | -5.7615 | -57.5807 | 2026-09-21 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 55633af4-1ddd-3f40-a5fd-7908524b87b2 | -7.4283 | -44.7639 | 2026-09-21 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3b752514-d6c8-32eb-b8a1-19a0dc79fcdd | -6.3196 | -59.9956 | 2026-09-21 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fd8dd315-b84e-3456-b6aa-1f43ef2dfc52 | -9.8692 | -48.4033 | 2026-09-21 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 90793326-49dc-33ea-97d6-db8e15e10d3d | -3.1698 | -58.5859 | 2026-09-21 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0ea8d349-471e-3ebe-8b79-5d1055936df1 | -6.001 | -51.7903 | 2026-09-21 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| aa147890-5370-319e-a7d2-e026513b3cca | -4.2964 | -56.2596 | 2026-09-21 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| b4714739-9db5-38ff-95b5-88e34004010a | -9.3986 | -48.3213 | 2026-09-21 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| cf43c995-e444-3fa3-8313-1b90dbcc6ed0 | -4.5774 | -42.9512 | 2026-09-21 15:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 7c4a99ed-ea0a-3ed1-84b2-be763893b480 | -9.2759 | -46.1852 | 2026-09-21 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 2dfa2414-eeef-3971-af1a-160061843f67 | -11.8362 | -50.0244 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| e24681d0-7bab-3c97-acdf-cd004e2edfff | -10.8924 | -53.9652 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| daef6d77-c4a7-34de-b43e-fc4a40a1f100 | -8.1876 | -54.7219 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 9f7902cb-f649-32c0-bfef-e5d41961c9a6 | -11.0804 | -49.7456 | 2026-09-21 15:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 7b89e6f2-e3de-35d4-8cc2-451651f76697 | -6.8243 | -55.8208 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ca8a0e7c-e5e0-34de-a216-4eb581547033 | -12.0649 | -50.0185 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |


[Clique aqui para ver as próximas entradas](README137.md)
