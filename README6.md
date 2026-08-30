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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0df0f50-9f20-3452-a23c-bc8af7a37a52 | -9.1981 | -51.547901 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfd905fb-a8e6-37c1-b40f-4455b99addfa | -4.1533 | -60.687901 | 2026-08-30 00:32:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49409191-4dbd-3558-b523-9bd6b0354c77 | -10.7858 | -45.306702 | 2026-08-30 00:32:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03dba668-192c-344b-8f2d-b6c41cf4ed57 | -14.7647 | -48.729801 | 2026-08-30 00:32:00 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d914f2f3-ed91-3978-99f9-00adf84191c0 | -9.7551 | -48.142899 | 2026-08-30 00:32:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53a9e53e-aa28-3d9d-99fb-dfd4ce8480a0 | -11.1871 | -55.078701 | 2026-08-30 00:32:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89b05697-0679-3cfe-a690-f66d56d4f036 | -19.082701 | -57.376701 | 2026-08-30 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 944d925d-9958-3193-a071-c7998c88802d | -9.1646 | -59.488201 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7be668c9-03fa-3383-b098-3d7b15346360 | -19.080601 | -57.366001 | 2026-08-30 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3d16bfdf-8eb3-3915-abb9-62fb83995b11 | -15.1236 | -53.571701 | 2026-08-30 00:32:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc6d4a4b-d88a-3ade-b935-68d42e740399 | -7.5531 | -61.281101 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa67589e-13b4-39d1-b279-fde4cd32e64c | -10.9908 | -50.5271 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6c2fccd-0594-3b39-99cb-fe56bfbbc262 | -9.1625 | -59.478001 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2492cda8-8514-3fc0-b149-88eb0d006041 | -7.0067 | -59.634899 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc7d14a7-1a54-3f3a-a469-9a9195fd5ade | -9.204 | -51.528999 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4434378f-95f2-35a2-bd25-5582487d89fb | -8.6168 | -54.722599 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73cd5921-2673-3d09-8009-faefa621dabe | -6.8808 | -59.431301 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 521fafc4-8130-3c87-8003-bb4baa785416 | -24.6703 | -53.718102 | 2026-08-30 00:32:00 | METOP-B | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b31e3aa-3a87-356c-9d82-7b967ab558e0 | -9.6475 | -58.919701 | 2026-08-30 00:32:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e12a948-1541-3773-9e69-7cce78998b28 | -11.0424 | -57.200001 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69a6a707-2529-3c24-8646-18d55a582cf4 | -11.1804 | -55.095001 | 2026-08-30 00:32:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9544faa2-a8c3-3b65-9421-bf1b8c472cab | -10.9358 | -43.010502 | 2026-08-30 00:32:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b906a0bc-94e8-30d8-8e6d-2b354d04dec0 | 0.1445 | -60.3866 | 2026-08-30 00:32:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 184d1472-7070-39d4-ac6b-3d75626f94d7 | -14.4327 | -52.552898 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5123d38d-cfbf-37b2-b5f9-84d6a315d865 | -11.4354 | -61.466599 | 2026-08-30 00:32:00 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e27780c-6d1b-31e4-ae70-729dd449dada | -9.9454 | -53.9907 | 2026-08-30 00:32:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 064b6ae2-5aba-3410-b232-e37cc1d2aba3 | -9.2804 | -57.068901 | 2026-08-30 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc2d29a-2263-3c6b-be91-139b8388ea8c | -10.343 | -49.973801 | 2026-08-30 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57e76917-a7af-3fcb-9804-9342f22bbc82 | -6.878 | -56.566299 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0a6dbfd-ae71-3d88-a196-39070f33f023 | -11.1602 | -51.2896 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0a3225-2ae9-3d84-88d0-6e9d8205b937 | -14.2827 | -57.029301 | 2026-08-30 00:32:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59439a08-1293-3737-b357-242d7e0467c8 | -9.4126 | -51.671101 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af94e82f-640c-3f8e-8e58-17a15615a2ff | -3.7663 | -59.310501 | 2026-08-30 00:32:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70d25622-c639-36aa-9a32-2352dff59fae | -5.9621 | -57.6749 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8997f08d-6cbe-3ab7-a479-94ae18e7aa44 | -6.9381 | -58.940399 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25302eab-9469-3b4a-be92-910dcba6126d | -9.038 | -65.359001 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5dfedd-e32e-3174-86fc-07615d6d9b63 | -10.9866 | -50.509201 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2adc5d13-0700-392a-8402-eb483bec744a | -9.4221 | -56.965302 | 2026-08-30 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95e2de1c-284a-3ec4-8a84-fd9bbcb54405 | -14.168 | -52.841301 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6ba3f06-f0da-3aff-aec3-728d2ae92a59 | -15.6536 | -56.3895 | 2026-08-30 00:32:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1909f24-d2da-3aaa-b91a-999e8e4ab482 | -10.4822 | -64.471901 | 2026-08-30 00:32:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a05eb230-1e28-39de-81ce-cbeaf031b7d9 | -10.7602 | -53.994801 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54318855-a3c2-3823-961a-72749103edb6 | -6.9433 | -55.706799 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd4533d-7ef5-3483-93d8-bb4c783b953d | -6.7679 | -55.659 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20229c7b-1ae5-354d-9af8-3bf2ac6d2b9a | -14.1486 | -52.8009 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 80358646-3009-3a65-b238-7d1da8df8f1f | -13.8437 | -54.112499 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3210f623-3074-3d29-800d-5fe33a15055c | -11.6306 | -54.5728 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8dbe37b3-1bd0-334a-9a23-4c9ca2ea80e5 | -8.9468 | -62.3531 | 2026-08-30 00:32:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4b51c89-3b70-3b2d-b52a-df9ea5d0972a | -19.0847 | -57.387402 | 2026-08-30 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cd0214ad-c672-3c7e-babf-8d18eb1e1882 | -3.628 | -60.537601 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9b5aaf-9c82-323a-aeed-7043ebc56387 | -6.8673 | -59.463902 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5ddd8d-dedf-313b-be16-f7b2379d5f3d | -7.5249 | -55.316002 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 772c24e0-05cb-3036-86fb-7687ff4ad283 | -14.1712 | -52.855598 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79ffbf7b-9eb4-38ce-8722-dfcd5a6b9c4b | -9.7841 | -59.4217 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4896c5-5c78-36b9-8f09-1c1c02d0cf55 | -5.4794 | -43.998299 | 2026-08-30 00:32:00 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29005c80-591d-3ced-a138-c90971a390f1 | -9.1495 | -59.610001 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8f4efc2-6277-3309-acb2-f3a377ec1c1d | -10.9263 | -43.0131 | 2026-08-30 00:32:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3adef77-3a9f-3122-8a38-1beb1b90b0f9 | -7.0809 | -51.579102 | 2026-08-30 00:32:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdef4330-e55d-3681-8256-c6ba0c1d0271 | -21.318001 | -51.316502 | 2026-08-30 00:32:00 | METOP-B | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3ed17b4-47e5-372c-84c0-759b4d940398 | -5.4796 | -57.123001 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3829bc-2c48-3093-8822-f52f9fa55485 | -18.881001 | -53.023399 | 2026-08-30 00:32:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 86c5dbbe-211e-3844-9f75-bc8b6167b103 | -6.7451 | -55.649601 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d91f39a2-c9ae-34f4-ae84-b0088d3bf401 | -14.1924 | -52.858101 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11baf0e3-37cb-3ec9-9269-df5b1a621791 | -14.16 | -52.805698 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 236ebcb0-8adc-3e9a-ac28-7d947aac27b7 | -10.7586 | -53.987801 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb825cbf-122c-36b8-8214-8ec676dff5b9 | -15.642 | -56.383202 | 2026-08-30 00:32:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50520dc2-e847-3028-9a92-8d356a8340a6 | -17.5986 | -51.599499 | 2026-08-30 00:32:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ebf1d66-da26-3ac3-9471-1227c2d6ef92 | -10.7598 | -54.038799 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 791dcc0b-3637-3558-8a29-2d59b460c0c3 | -6.7694 | -55.665901 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae012de0-0f07-3aad-bbd9-4fb01144b070 | -18.818899 | -47.445 | 2026-08-30 00:32:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd4cb7a0-1344-32e0-a9f3-a0137c8af8ee | -9.1473 | -59.599602 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d25e379f-b503-3d63-bafc-08d9b3394b2c | -10.4916 | -59.582298 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2e72c9a-aad7-30dc-a2d9-36de5b1dc379 | -9.7939 | -59.419601 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f78ab69-6732-35e4-b786-27d83e01e99c | -6.9028 | -58.966499 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10e26961-31b7-3bda-9b9f-58f99c492a81 | -7.5584 | -61.3064 | 2026-08-30 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8069355e-e4a4-3b53-aabf-20e576e9ed16 | -11.2424 | -53.987 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 431787ae-7722-3717-a5dd-1618bf619bca | -13.8745 | -54.112701 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bd22d51-ce19-3192-9e8a-539102cda724 | -15.6438 | -56.391701 | 2026-08-30 00:32:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e4ef95e-e656-36ee-a0df-4723fa2ff3c1 | -12.5619 | -55.727001 | 2026-08-30 00:32:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd7710ae-b834-37a3-abdf-895707119421 | -10.7462 | -50.671001 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64844f52-22b9-3225-ab4a-17d3ad02f8bf | -11.7125 | -54.524799 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4993af0a-2b4d-372b-b654-2df018bf3970 | -5.9685 | -57.6576 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd9300c0-040c-3bbc-900c-477e40cf1fea | -6.114 | -53.549198 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38889dd9-ba4c-3c34-af32-436caee83b3c | -7.5053 | -55.3204 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4924b81f-d673-335a-9047-7067c016c6db | -16.3563 | -50.993999 | 2026-08-30 00:32:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5e7eb2f-dc89-3734-95ae-aaa810091f34 | -16.339399 | -50.965698 | 2026-08-30 00:32:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ecde3ba5-a07a-31af-b7eb-45c00d15c7f0 | -7.5331 | -55.582401 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b69104-bec0-3f9a-bed9-b25e7bcad130 | -9.6608 | -50.838402 | 2026-08-30 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14b8729-346c-31ae-a1b6-0d309ebf66a2 | -4.6965 | -55.652901 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00c31ad6-1f2a-3925-a8d9-15245493dae5 | -10.7483 | -50.679798 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 266e0c41-722c-390b-bac4-9dcb7f8b256a | -10.758 | -50.677502 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 418c8b27-c4fc-336c-894f-9fd2c6f195c4 | -9.6704 | -55.059601 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3071c557-b376-362f-8afe-4fb1771f6db1 | -7.5233 | -55.309101 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db3eb265-9c4e-3668-a9a7-6e41ba90115b | -4.0707 | -45.944302 | 2026-08-30 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 255417c1-8da2-3a4d-92cf-d37a0bedebda | -9.0213 | -57.529099 | 2026-08-30 00:32:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f29f98a9-cfcb-36c5-9382-f2be0c9a2ed4 | -7.6953 | -61.133801 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cdd786a-8983-34ca-88ca-5e6b8b989bd7 | -11.021 | -51.400398 | 2026-08-30 00:32:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd62b7e-fb0e-38d3-b8d2-630bf9559105 | -6.9319 | -55.702099 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f31a3ce-6086-3145-bb7d-126b95147895 | -3.7682 | -59.319 | 2026-08-30 00:32:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de3f448f-6e57-34c5-899a-ef9d7cbff709 | -10.768 | -54.029598 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
