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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce47e41c-458f-35f6-bb15-d201fa4b0297 | -1.9728 | -53.754799 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa8304a-dfc7-35c4-a329-24cca2ea9576 | 4.2749 | -60.566299 | 2024-12-12 00:50:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d500101a-84d9-3686-8609-6e73058d70dd | -5.6208 | -44.130001 | 2024-12-12 00:50:00 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecc8b064-562b-353c-b54e-53f2fbe14a97 | -15.6541 | -60.095501 | 2024-12-12 00:50:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05866ceb-c792-365a-b693-957af2f7c9da | -1.8319 | -53.542702 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1f872d-ca49-3ab5-b019-4f186f305590 | -14.6583 | -59.650501 | 2024-12-12 00:50:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0798f64-0b9c-3a32-b0b8-c66d7e999e9d | -17.6066 | -53.042301 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5abe17b-ee78-3b77-8107-bfcedeaa647c | -17.618401 | -53.001499 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 48d194c7-1006-3afe-979b-836957f522ba | -1.2614 | -52.8447 | 2024-12-12 00:50:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d561b9d-c365-3ffc-b2f2-767d687c8e6a | -12.6289 | -52.1007 | 2024-12-12 00:50:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b91f7a38-09d2-34bf-a76d-694630ca8dd9 | -2.0233 | -53.704601 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05bd28be-9529-31d9-95ee-1dffbef87095 | 4.0647 | -60.403999 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a3449232-c3e9-34ae-98a0-29281e6a04bd | -10.6874 | -54.706001 | 2024-12-12 00:50:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1914a169-32c8-3f1c-82fa-993b4aa36627 | -3.6669 | -54.7262 | 2024-12-12 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e20f0ad9-83e6-315f-9b8d-d349852fdea0 | -10.6859 | -54.698898 | 2024-12-12 00:50:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4278ca5-8d8a-3d7c-8af4-39a37992f401 | 3.7278 | -60.120098 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c41c17d8-ec97-3ea0-9a26-d8e293e0da25 | -1.434 | -54.742298 | 2024-12-12 00:50:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10fc737a-6747-3a75-96f6-e3c3f8cf2b98 | -1.4785 | -54.2104 | 2024-12-12 00:50:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c663e5c1-06df-3731-a70f-bc3a0f1ae1ec | -3.636 | -54.3619 | 2024-12-12 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 515f57fe-96f2-3731-b869-9378a4769679 | -13.2597 | -54.808201 | 2024-12-12 00:50:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78e6681d-0631-30de-8d34-9a3cb818f7de | -17.6082 | -53.049599 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff714453-6328-3b47-b6b9-c5fc62789cc0 | -17.605101 | -53.035099 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| abb014e8-2984-377f-b197-f36e12ea9cf8 | -2.0188 | -53.7756 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7190bcc6-8ecc-3b23-9982-b9876b63802b | -12.1111 | -57.762199 | 2024-12-12 00:50:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03a8ef6b-20d9-3fac-9187-85883b98b216 | -17.320299 | -56.361099 | 2024-12-12 00:50:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| defc06e3-3cce-3a0e-9bfb-cfa13d5ad5d0 | -1.6398 | -52.336102 | 2024-12-12 00:50:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07d4645-d855-3bff-a931-8ffc6e9653f3 | -21.7111 | -49.7351 | 2024-12-12 00:50:00 | METOP-B | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1fda92ea-547c-3ad1-b7fe-a56211fe1d05 | -14.3252 | -52.721199 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d47a020-2361-3916-8123-b4bd8af579d3 | -6.496 | -43.625099 | 2024-12-12 00:50:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f78e782-d100-351f-ba96-f865aa332073 | -14.6556 | -59.636902 | 2024-12-12 00:50:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63ed04d1-dc57-3418-87eb-a5d79a8f12d0 | 4.0588 | -60.385201 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0232eefe-c81d-3dac-9970-95678791ac94 | -10.7725 | -53.882 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04354d3e-71d9-3b38-9966-f8e71826e8ba | -6.4725 | -43.572498 | 2024-12-12 00:50:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6e1fe6-89d8-3807-b4ac-3295c4405def | -6.4795 | -43.600101 | 2024-12-12 00:50:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce65513-e241-3baa-9033-bf9ac49d26e0 | -7.8746 | -55.157501 | 2024-12-12 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e80b107-7724-3355-8648-f4b0366b7851 | -1.6418 | -52.3447 | 2024-12-12 00:50:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41093e4d-831b-3a34-89d3-adf10e150938 | -10.6776 | -54.708199 | 2024-12-12 00:50:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7f9201c-5ff6-38de-9704-5cd9cee068f2 | -2.0101 | -53.691799 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83b855d6-5352-38a4-a58c-13e4657d60e1 | -4.732 | -44.4599 | 2024-12-12 00:50:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f80ed3c-5a98-3397-bb21-9d43abf7f0a4 | -14.3123 | -52.7094 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f193228-0efe-37ff-87eb-d0fc23c49287 | -5.495 | -48.119999 | 2024-12-12 00:50:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c95f2e91-04f6-3a83-a560-67bf25c7dc2b | -17.620001 | -53.008701 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fbc2a451-1e8f-37ff-abe3-e8d619c3a88f | -6.1423 | -51.173199 | 2024-12-12 00:50:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084e1c7a-87df-3e93-8ba8-40f56bd6b910 | -1.176 | -54.7407 | 2024-12-12 00:50:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2778df3-958a-3046-bf91-7fd2851ca202 | -8.7605 | -49.542801 | 2024-12-12 00:50:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbf886f-8f28-399a-81d7-adc64020339e | -7.1366 | -49.479599 | 2024-12-12 00:50:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80bd2e74-09bd-3e76-b69c-6b18a183adb7 | -8.2589 | -50.257099 | 2024-12-12 00:50:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d756200-8798-3a9d-8259-5132ad792664 | -10.7823 | -53.8797 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5753ea23-1e71-3595-88dd-615729c0cfe3 | -2.0351 | -53.7565 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9783af3f-1379-3634-96c8-10b82a32437f | -10.4501 | -54.377499 | 2024-12-12 00:50:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acd1c809-1e12-30ff-886e-16133aa9c35a | -5.6143 | -44.103802 | 2024-12-12 00:50:00 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41630857-bbfb-3a06-92db-f1b6a689b121 | -2.805 | -46.944599 | 2024-12-12 00:50:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d538876-bd54-3a17-8c3a-d9ff7b7334f9 | -6.4864 | -43.627499 | 2024-12-12 00:50:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7efa447-1e3f-380a-b70a-d3409389b38d | -17.614901 | -53.032799 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1998f9d7-200f-303c-8e58-f198e365fdf0 | -11.3437 | -48.989101 | 2024-12-12 00:50:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60544ec0-3bc7-3c21-87b1-90022860ce34 | -12.6387 | -52.0984 | 2024-12-12 00:50:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f56d877e-aa3d-39c6-b827-ed64dd956718 | 4.0569 | -60.393501 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad337b4-5f92-3dde-a9c9-4bfc32210441 | -6.5289 | -43.068802 | 2024-12-12 00:50:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d175be85-d489-343e-b035-ac12f26a446b | -16.870001 | -53.8256 | 2024-12-12 00:50:00 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdc3138-0f57-389b-b7be-538b6e811114 | -4.7257 | -44.434101 | 2024-12-12 00:50:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae8425ee-1b76-33dd-a0b8-487571c6fd75 | -1.8369 | -53.746201 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d39b3ae3-cd56-3e1a-9836-8665dd507982 | -14.3237 | -52.714199 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90c49049-e751-3708-beca-bd41656b9a0d | -17.6133 | -53.025501 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 51e33a5a-c2bc-3546-a47c-af74931092fe | 4.5041 | -60.2869 | 2024-12-12 00:50:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 707a5735-37bf-38a6-a51d-c6287d9acc64 | -17.318501 | -56.351601 | 2024-12-12 00:50:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6af1b0a9-5741-3eb5-958b-78f38c9fff86 | -8.1873 | -50.084702 | 2024-12-12 00:50:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 223e1d0d-090b-33a6-9a34-f21ac83c4c12 | -1.4356 | -54.749298 | 2024-12-12 00:50:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ce64a5-a786-3893-9e38-4b4c02edc241 | -14.2288 | -50.395 | 2024-12-12 00:50:00 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cdcee93c-c9d8-35d5-b511-0004fbf77b89 | -2.6768 | -54.086601 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961ae245-cde4-3662-92fe-aadd738d48d9 | -3.3368 | -50.7593 | 2024-12-12 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490b5f0d-0b42-3b3a-a07b-cf89712f68b4 | -5.4853 | -48.122299 | 2024-12-12 00:50:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9524abfc-ad87-3ab9-ba63-7de480a28ee7 | -7.1341 | -49.4688 | 2024-12-12 00:50:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a081cfdf-d4cc-3d26-9e76-3c34a6831633 | 4.0607 | -60.3769 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 005403ea-964c-3679-9deb-97c00a17e7fa | -13.223 | -52.9991 | 2024-12-12 00:50:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e617d14a-5d7f-3060-82a6-b4bb82b90ab1 | -14.3221 | -52.7071 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2ff69d-9591-3df6-8656-aa1207195e9e | -17.624701 | -53.030499 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 42f14b54-b994-3914-8057-af1600b413b1 | -8.2611 | -50.266499 | 2024-12-12 00:50:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 298deb63-7fc0-389c-a88a-76667888b05b | -10.7808 | -53.872799 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d97266f5-dd11-3a80-b443-cc2d6f514078 | -14.3107 | -52.7024 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c08ba0b1-b138-3509-b85e-69addef7effb | -14.3189 | -52.693001 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 330f5beb-c51b-37eb-89c8-e1bbb969eef6 | -14.3205 | -52.7001 | 2024-12-12 00:50:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a891a532-e63f-35d0-9193-16a76ddaf266 | -3.6344 | -54.3549 | 2024-12-12 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 430c2180-e379-304d-bd77-720b886690ad | -13.2629 | -54.822899 | 2024-12-12 00:50:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9046347a-1eb1-3319-8e65-c3ef4d84aea5 | -12.1366 | -57.7868 | 2024-12-12 00:50:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db865ccb-64f6-3009-800e-67ca720b106a | -8.1896 | -50.0942 | 2024-12-12 00:50:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2408bdf-1652-3c39-9484-6d6fd924e40d | -12.1131 | -57.771801 | 2024-12-12 00:50:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3e9f50f-6344-3960-af80-61ff597dee75 | -13.2711 | -54.8134 | 2024-12-12 00:50:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 677a55e1-fe69-3def-98a2-5b6c9f33be94 | -6.1402 | -51.164398 | 2024-12-12 00:50:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da4d8e1-5808-3b1e-8e70-49db8e44f019 | -17.621599 | -53.015999 | 2024-12-12 00:50:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db244970-6085-3955-b644-0a3926314404 | -2.0303 | -53.7808 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f597187-dd3d-3f95-9a52-8ce8c15532da | -12.4916 | -55.7742 | 2024-12-12 00:50:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb02e260-c153-3d65-9e1b-4912871e3003 | 2.9173 | -60.734299 | 2024-12-12 00:50:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ed43bf6c-ac12-312a-bd7a-aeb87f6ae684 | -4.7224 | -44.462299 | 2024-12-12 00:50:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b08df65e-ab30-36f1-974d-8b3eed4ba94b | -2.8093 | -46.9631 | 2024-12-12 00:50:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467b0ebf-7dfd-3d8a-975c-d585e153698b | -16.868401 | -53.818199 | 2024-12-12 00:50:00 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7940a3a5-6f0b-3cab-a3cc-fa549c34bef2 | -10.7694 | -53.868099 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1829e6bd-cbba-3b15-870c-7bdb63121ea3 | -2.526 | -53.785801 | 2024-12-12 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818a7846-4f45-3ce9-a0eb-d390b86956db | 3.7377 | -60.122299 | 2024-12-12 00:50:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0937a814-f3d5-3616-8ef4-90788b94d30e | -1.8676 | -54.063 | 2024-12-12 00:50:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe4aff5-eb1f-364b-b6f9-e5e94a42b65a | -10.7756 | -53.895901 | 2024-12-12 00:50:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
