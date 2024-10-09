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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a03eb485-f853-3c18-ac48-d7a1b6ea7f52 | -21.29457 | -47.21128 | 2024-10-09 03:25:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1fa5631f-83ac-3f6f-ab3a-f681739c9b11 | -21.29372 | -47.2114 | 2024-10-09 03:25:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 45a08d02-33b0-3058-9781-19a448f37f35 | -21.29319 | -47.21705 | 2024-10-09 03:25:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 391253bb-fa70-3fbc-b715-57a68dc1cd90 | -21.29227 | -47.21731 | 2024-10-09 03:25:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dabe53d5-c3c8-3b2f-9082-8d6660f940a8 | -21.26803 | -41.78669 | 2024-10-09 03:25:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fb6bbab1-058b-3352-b90e-e3b8a084dc89 | -21.26549 | -41.77523 | 2024-10-09 03:25:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 73ce6bdd-ffc3-3e0f-ba5a-40ccac403d64 | -21.1135 | -47.23129 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcdc56ff-7dbf-3569-98cd-2e0bfe2dc8b2 | -21.11293 | -47.22787 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1970c606-abff-3580-b94b-85cd1fa07206 | -21.11186 | -47.23819 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b288a80c-3081-3b14-8c6d-2eeb555cc4ad | -21.11135 | -47.23434 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9691e6a7-f1a3-3415-bcc0-9adc4c331c43 | -21.10751 | -47.22754 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92fa0b09-84cb-3dc9-afd5-933f914520ae | -21.10596 | -47.23404 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd8f5b64-9f49-3de3-b596-f3f4dd365c6d | -21.10554 | -47.22993 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c81ceb0-41b6-30a8-8bcc-7870fc3aa714 | -21.10411 | -47.24185 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50ca187a-2f7e-36ef-8700-b67b276cf0c9 | -21.1036 | -47.23787 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 391e7da7-5018-381a-a9b0-c4947b304bf9 | -21.10115 | -47.22535 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3391f0c9-d7f9-3885-b248-5b3c96bbb6b9 | -21.09994 | -47.23042 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1fe4941-eac9-381d-a8f6-72f9fde53169 | -21.09919 | -47.22774 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7b76fa2-d6a4-3b54-a2ea-32adb67a404a | -21.09347 | -47.22873 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 184af73a-69ba-36ab-852c-807d71baefc9 | -20.81243 | -45.63217 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 624c80a3-b132-36be-b551-9dfb81fc0af1 | -21.09271 | -47.22609 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b7966b1b-b8eb-3a7e-b70e-f95220b56460 | -21.09141 | -47.23741 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef8a143c-0ea9-3d5d-a7e5-ad9d9e20d701 | -21.09103 | -47.23296 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3fb52cc1-989f-3b58-b82b-47eb803d3ac3 | -21.08709 | -47.22663 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 87a9cfdb-52fe-35f5-bd9e-bd3def5d1980 | -21.08319 | -47.21419 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 39d69a8c-b52e-332a-a051-d711be960547 | -21.08202 | -47.21908 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 151d7034-1e81-3840-9b30-dc7512235173 | -21.08119 | -47.21695 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| edf674d0-c5a7-32bf-9ce7-a55900a76805 | -21.07995 | -47.22196 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0a66ce02-af0e-3314-8c2f-709e1eda06e8 | -21.07519 | -47.21891 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d18c13bf-cdc5-32f3-aff2-54df8495115a | -21.07434 | -47.21682 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| fda3fc99-0a80-34e3-9f81-28bcd6d150d5 | -21.0739 | -47.2243 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 9de76076-5b4e-3911-b138-e52d50cb51dd | -21.07302 | -47.22216 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 53bd9fc6-2f1a-3b72-91a5-ece2689b013b | -21.07262 | -47.2296 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 8de45f2c-e8da-3a7c-9513-bf56f97b3715 | -21.07176 | -47.22725 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 263310fc-5215-3c89-8835-eee81f623f2e | -21.06837 | -47.21869 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59012219-4590-3cfb-b879-79288f954d3e | -21.06714 | -47.22379 | 2024-10-09 03:25:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7ae8821-2c99-365e-9a51-efe6c62d5385 | -21.00533 | -46.10253 | 2024-10-09 03:25:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e97d1afe-22de-3e11-8dd0-5a50bdc050df | -20.99972 | -46.09885 | 2024-10-09 03:25:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ddb7cf0f-c33e-3a92-afa4-c99b9e6226ff | -20.99392 | -43.06583 | 2024-10-09 03:25:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fde69c4b-49ae-3d2a-b104-cf9898d04ef3 | -20.99102 | -43.05439 | 2024-10-09 03:25:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5343181c-2f03-3a1b-8384-b483681764d6 | -20.98886 | -43.06444 | 2024-10-09 03:25:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4fec9f06-4315-373b-a48d-935dbad76417 | -20.96165 | -43.98266 | 2024-10-09 03:25:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 65fe47a4-ce5d-3f10-b677-87096722d7dd | -20.9196 | -46.46973 | 2024-10-09 03:25:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f7a84ae2-e5d4-3351-8d2d-a4ed67bc3b14 | -20.90398 | -43.30654 | 2024-10-09 03:25:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8085d9b1-230f-3974-b8c8-9c74869e8451 | -20.90357 | -43.3082 | 2024-10-09 03:25:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 25bbdc6e-ff0b-36f8-90ff-be5d92a28c3d | -20.90323 | -43.31008 | 2024-10-09 03:25:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ea607766-8542-3bd2-baf3-bd0258d02048 | -20.81577 | -45.62493 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eab05854-2578-3d0b-bf9f-0b093fc0ce4e | -20.81466 | -45.62968 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c17c0b03-996e-305c-b06a-2f1d9bc567df | -20.81353 | -45.63449 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d23a9d99-1894-3a0f-9e7a-a363addbb331 | -20.81352 | -45.62735 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 4ca32687-6eb4-32f6-b493-cff6c9023db8 | -20.81238 | -45.63938 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1798eacb-9c7f-3b1c-a732-38a7c73ed0cd | -20.81132 | -45.63705 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b7e91fec-43f6-3347-9cbd-41bd29e6c55c | -20.81122 | -45.64436 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 633dab76-ca99-3e15-85e2-8ded879fcfb7 | -20.81018 | -45.64203 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0022b300-3964-3a14-bfc3-37a7a47cff43 | -20.80984 | -45.62332 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3acbffca-d41c-3a3a-b3c6-c246fe528ecf | -20.80874 | -45.62802 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 4edc2e8d-4c22-39a6-90e0-1baa3699900e | -20.80761 | -45.6328 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| b3f8b05e-516f-3a11-aa7f-dea5cf82470b | -20.80646 | -45.6377 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 84376295-b3e4-35a9-bf02-4e83b149554e | -20.80528 | -45.64274 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dab5ac4f-3fa7-3f06-b7ce-c0ace258579a | -20.80411 | -45.64772 | 2024-10-09 03:25:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95f2dc03-dee4-36ce-8629-a0ab90cb649f | -20.79855 | -47.20661 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 631ae1ad-c3c4-3071-9b97-dacd67ec181a | -20.798 | -47.21595 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36490abe-c54a-36aa-a76b-4bf2fb927421 | -20.79724 | -47.21199 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f9aa4f7-e2a0-381a-89ad-f97f99881f28 | -20.79677 | -47.22115 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d2e3987-9685-3dd9-a96f-673c0bde52ad | -20.79598 | -47.21715 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a295ede6-898c-3eea-bb21-467deb470c84 | -20.79455 | -47.22306 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10dfc8cb-5ac9-3f49-b472-689fda11a16a | -20.79387 | -47.23344 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1418b33-1c42-35b5-b328-431e98e83d62 | -20.79285 | -47.20854 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78e2d6f9-78c2-355d-81c7-c5d2e78c6243 | -20.79157 | -47.23532 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3bdba891-9e89-3bc6-adb1-0869814e5cc4 | -1.11 | -53.6173 | 2024-10-09 03:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 62614797-bedd-35c0-bd6f-66e8525f0b77 | -3.9021 | -46.4689 | 2024-10-09 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d3005e5e-6b7e-39d6-893d-b1fd77ac734b | -3.9023 | -46.4467 | 2024-10-09 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7172e6ee-1d64-31a3-ac3c-5e7df18cd0e9 | -3.9208 | -46.4459 | 2024-10-09 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4fda70ef-d050-3d32-9374-7a49455fac7c | -3.9394 | -46.445 | 2024-10-09 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4a90657b-9ecd-3c4d-b116-d72f9f64a366 | -5.5905 | -44.8687 | 2024-10-09 03:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 5c2f35b5-0722-3fd5-af9e-400504655f1d | -6.7614 | -60.0559 | 2024-10-09 03:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 132fdf9c-0f75-3dc2-b988-7382e13edf14 | -6.7798 | -60.0552 | 2024-10-09 03:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 34e14fdf-1008-3cb4-ba01-fffbe4b1a082 | -6.7799 | -60.036 | 2024-10-09 03:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1a790dcf-d8ea-3ffa-9cee-26d698e200e0 | -8.4919 | -48.6476 | 2024-10-09 03:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a8732231-e780-3b87-9a85-8a6bcca112f6 | -9.5817 | -65.2497 | 2024-10-09 03:26:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.9 |
| e14e39ef-8ee3-3963-b5a2-ff5e8879e07a | -10.3894 | -61.2502 | 2024-10-09 03:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b9f8acbb-1869-3cb9-b62a-d85523d76724 | -10.3895 | -61.231 | 2024-10-09 03:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0d61ccf0-96b8-3cd0-bd9c-0e730ea19c45 | -10.6068 | -55.9169 | 2024-10-09 03:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0c6b44a1-7d78-3683-adba-e1fed0013488 | -10.6253 | -55.9355 | 2024-10-09 03:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| eb0d5f11-8583-3d60-b965-7ac61ff14ac5 | -10.6256 | -55.9154 | 2024-10-09 03:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 243cba51-8e1a-340b-b5e0-29621663f695 | -10.6258 | -55.8953 | 2024-10-09 03:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f598d43b-f8fe-3adc-aaf7-8628c709b361 | -10.8567 | -63.9177 | 2024-10-09 03:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3d5eefe8-8413-3fde-a0b9-554b9a9bdca5 | -10.8568 | -63.8988 | 2024-10-09 03:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d599d057-294a-35aa-942b-51b8ad1223b5 | -10.8754 | -63.9169 | 2024-10-09 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e14fa4d9-920c-398f-8dc3-c8eda01071b0 | -10.8755 | -63.8979 | 2024-10-09 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 78cd079d-2a93-3e41-b933-8d395eb72ab1 | -11.2583 | -60.3885 | 2024-10-09 03:26:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 14460b72-a7f4-3061-84e5-66576762ee3a | -11.277 | -60.4067 | 2024-10-09 03:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 95631898-ac26-3682-9e4a-bda1b12f13a8 | -11.2771 | -60.3873 | 2024-10-09 03:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cd64715c-d832-3f6c-a402-769aa559044f | -11.6806 | -64.0312 | 2024-10-09 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f6158410-016a-3ea5-92cb-b6049b32e927 | -11.693 | -65.0163 | 2024-10-09 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 112.4 |
| b7e2f47e-824c-3789-a4c9-180be4a3b649 | -11.6931 | -64.9974 | 2024-10-09 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 03d6a319-f92d-3355-b3ef-a0aa6954b1ba | -11.7117 | -65.0155 | 2024-10-09 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 166.5 |
| a4297b18-9eb6-3cba-a986-115f3dd326b9 | -11.7119 | -64.9966 | 2024-10-09 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 0aa8a4c3-9084-391f-813d-bdac37f91b0b | -12.7501 | -62.269 | 2024-10-09 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7c30c298-3969-33df-9329-d90e12bb860a | -12.878 | -62.8007 | 2024-10-09 03:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |


[Clique aqui para ver as próximas entradas](README66.md)
