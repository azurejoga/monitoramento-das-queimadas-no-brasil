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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd5dcba6-9196-3699-92ee-178b240bfc04 | -6.59957 | -56.33966 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1906297-6cbb-3832-9064-a194c02f3c00 | -13.81922 | -53.79997 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed90f7d5-73d3-392e-b4ae-0637f4b7a03d | -6.96134 | -59.28388 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce458352-5c89-3057-b516-e7f8a709bd09 | -6.83733 | -56.4211 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd158aa-39ea-39dd-9e4e-0427bccb6344 | -6.6021 | -56.34314 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b7b08c9-05fd-33e9-ac61-ab5e26b1f119 | -6.60841 | -56.33694 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea25ce48-8d4c-3e0a-89f1-e85455466da6 | -6.60346 | -56.35067 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f3068a7-58c8-3b34-ba91-1d5616725299 | -14.04882 | -53.58981 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a310094-b283-38fd-8456-b6e45a1fa591 | -6.96073 | -59.28817 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f76c1881-115b-33d6-a6df-5bf7dde96051 | -6.9589 | -59.30099 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76ca3c6b-db8d-36b6-b5ec-724b341a74ce | -6.70527 | -58.95248 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 837ebc17-2a44-3afa-8e00-e459f747b6f3 | -6.7892 | -58.75638 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46dd5d52-6f94-38bd-8bf7-9cba991a4cd6 | -14.09372 | -53.63504 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13d8c257-7b6f-37c2-9493-064d1336a6a4 | -6.60401 | -56.32907 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 553c9c4c-4739-3594-93d6-06efd1f9bee6 | -12.51865 | -55.78267 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e1f3542-3a6f-376c-9423-2af1b555b76d | -10.22067 | -68.08601 | 2026-08-14 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e293ad5-10c7-3cde-b370-6cda05cd7078 | -10.0621 | -67.55658 | 2026-08-14 05:55:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18866afd-a7bd-3b40-98f1-c3c723e39dfc | -14.0867 | -53.63457 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3339176a-54ac-3bb3-8c96-5a22ff86f24c | -13.28405 | -54.23256 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef4e4805-0fc8-35d8-800d-7b3e12fb695c | -13.82541 | -53.80031 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7d146eb-11b6-35c8-a959-8647a132e3f6 | -6.63493 | -56.26332 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e566c61-6904-3093-82e6-7c43770018e6 | -6.60938 | -56.3298 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d052bbd9-ceb2-3e88-b0e3-00fad4864f32 | -6.60654 | -56.35072 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acf47f9-d8c8-3ad2-95e5-8f4b4eabad01 | -6.70656 | -58.94351 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d92a2cb-99d4-3bf7-a9d7-4da103e34c31 | -6.60006 | -56.33618 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79ec968f-1610-3522-8a24-a2d1964acf3b | -6.79276 | -58.76378 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d33d177-7529-3b38-ba51-5cc08de4e917 | -13.81731 | -53.81103 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbae87b8-9574-3163-ba1c-19809ad7b78f | -6.78077 | -58.75045 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef495ea0-3324-3d69-9773-04af4e8cdbb5 | -6.59884 | -59.00708 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ffec9f5-52d9-336c-81e6-6503db51e118 | -21.59377 | -43.69716 | 2026-08-14 05:57:00 | AQUA_M-M | BIAS FORTES | MINAS GERAIS | Brasil | 3106804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| d5871d44-a5fb-3372-83fb-42e4c1f23c14 | -21.90273 | -55.37103 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 742d43d7-0c5d-34c1-b2ff-d70e21c294a8 | -21.89537 | -55.37689 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43c47579-05fa-3caf-8493-39078c9ab63a | -21.90401 | -55.36728 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e88ba68-2889-3993-a427-2dff8547e24d | -21.8967 | -55.37308 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca620cb3-5f1e-3ddf-a8a5-12376422dcc9 | -21.89592 | -55.37001 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2f23a232-48c8-30e6-a25b-490e612d2a3b | -21.89719 | -55.36631 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 393dcb09-9329-399c-8d9c-c6433884756d | -21.90351 | -55.37423 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf7d5a5a-fc01-3e8c-808c-c6d579f38c20 | -21.90327 | -55.36425 | 2026-08-14 05:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d562c76-fa58-3045-9d85-fdc9e337c60f | -22.67403 | -47.5278 | 2026-08-14 05:59:00 | AQUA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| c3009907-f369-3349-b0ed-1dba93096219 | -22.66834 | -47.55544 | 2026-08-14 05:59:00 | AQUA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.5 |
| 73d1db03-908f-3b18-8aae-f2df6c68b28f | -6.77978 | -58.75303 | 2026-08-14 06:12:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5e102d-e164-341b-8efe-b419f5eb227a | -3.24317 | -60.12687 | 2026-08-14 06:12:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30b5cb12-d6c8-3dd1-80b9-35ca6bb9e3e1 | -6.62072 | -58.99806 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1df47648-a6f3-3045-9557-0638bc5b0051 | -6.70272 | -58.95362 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b94090-0411-3cf8-8578-89622edc80af | -6.7927 | -58.76132 | 2026-08-14 06:12:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b648c81-9a51-3556-80c1-c8e14f40e013 | -6.61315 | -59.0032 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8361c07a-8655-34bb-b6e6-3b4228f5ec8e | -6.61217 | -59.04548 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09174742-0d9c-3021-80f2-bee5224d1c9b | -6.704 | -58.95867 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f07ed06-1333-33b3-8867-3cda7bc205ef | -6.61127 | -59.0024 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da500a98-4012-38d0-abd8-b30f1a1bf14d | -6.70478 | -58.95261 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31fa3a76-0b5a-3fa2-8623-b07cab3a0772 | -6.61135 | -59.05135 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0322517a-476d-368a-92bb-c243ac8af81e | -6.70559 | -58.94645 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4e46fc5-5817-3962-9298-6b8cbe2307eb | -3.24135 | -60.12888 | 2026-08-14 06:12:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5780f4d-36c3-3a5f-91c2-68281f5f087e | -6.71044 | -58.94784 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00ff23c1-f83b-32ae-9165-d632dcfb8fab | -6.70356 | -58.94751 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63025f54-bae9-3ef3-85fe-1fc0ad579d07 | -6.62188 | -59.04123 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 853a5730-62a0-31ee-9bd6-c350c9b039a6 | -6.6211 | -59.04715 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 68ea2147-2bc3-3fa4-a907-4e71a30b46b4 | -6.78754 | -58.7474 | 2026-08-14 06:12:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09bb19ba-1e59-36aa-8dcf-91ec1456bf52 | -6.61888 | -58.99729 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 982719db-73ce-3ff2-9f79-545b91c62d4b | -6.61354 | -59.05223 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f5d80542-635a-367f-af89-bccc147dda9b | -6.78065 | -58.74647 | 2026-08-14 06:12:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79b4b913-c663-31ee-a621-a18d0f61f29e | -6.61432 | -59.04638 | 2026-08-14 06:12:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ee590e96-b93d-3216-b966-f40019e11958 | -3.24204 | -60.12433 | 2026-08-14 06:12:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 598afcf2-7211-3e92-ac04-6903ded1e750 | -6.78582 | -58.76036 | 2026-08-14 06:12:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eaa264f-7199-3e1f-8996-a967c9664fcb | -7.90257 | -70.66868 | 2026-08-14 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66279b27-5aa8-3f2f-ad91-09907892d85f | -6.96115 | -59.28465 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ee16099-32a1-37d9-bcf7-f7d121091f86 | -7.37725 | -59.97426 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 077d94ef-3a31-3111-8917-c437ab10ee8d | -10.06222 | -67.55858 | 2026-08-14 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 985be683-0a58-3831-ab26-0a82c0adbe46 | -6.98233 | -63.01216 | 2026-08-14 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2112582-5acd-3e0d-81b3-42326453c598 | -7.37798 | -59.96877 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f14e197-b8ad-3a8c-856b-57e4a333eb1d | -9.58489 | -60.50185 | 2026-08-14 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e14e868-c9b8-392d-9feb-814a77adbd35 | -10.2191 | -68.08562 | 2026-08-14 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a6dfde1-8299-37de-93bd-eaccc32e1fb6 | -6.98279 | -63.00891 | 2026-08-14 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c5c1f72-650e-38e7-bb12-6a34783d01a0 | -6.96036 | -59.29053 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47d48f45-9228-3443-bd7b-0ec6929329c2 | -7.58489 | -61.22746 | 2026-08-14 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 218ea434-1492-3c50-af5a-0f5766badf94 | -9.60833 | -66.18383 | 2026-08-14 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0809d2fb-50e2-34fe-8f97-8fb030b22a3b | -8.45493 | -70.69699 | 2026-08-14 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40ecd0a0-4095-3eb2-ad12-3be934379d0f | -8.89586 | -60.55838 | 2026-08-14 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffbeaec4-dad7-3269-b876-417b3f94cf7b | -6.96359 | -59.29155 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d443d01f-317b-3e66-bc19-60c7457496b0 | -10.22302 | -68.0862 | 2026-08-14 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15b2fc5a-ccb8-30a7-a32c-4385219d9ebc | -9.76717 | -60.77125 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 801d9c7c-47eb-3e6f-82b6-131f1091d3bd | -7.40738 | -60.00286 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af844f5b-cfa9-3b94-aa19-8bb6565868ac | -8.88952 | -60.55753 | 2026-08-14 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 115c6f84-e907-32c0-a8a6-308ef4e74bbc | -9.76019 | -60.77549 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c1b684e-5999-3dab-9131-73ea6793a58c | -9.75634 | -60.77659 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf17155d-15eb-38d6-849e-a455a3b45d1f | -9.76782 | -60.76619 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dabb9c58-6f49-32c2-bffa-e0965766d408 | -9.76514 | -60.75714 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbf15e30-3a2f-3e31-8fd4-e578125abfa2 | -9.76451 | -60.76229 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b389291-df0e-3504-9fdd-ef12032535d8 | -7.58547 | -61.22303 | 2026-08-14 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46ab7105-2d53-323a-8b89-1c92e1ca9e1a | -9.75695 | -60.77161 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4b0dcc6-27e8-393f-b3c7-2419d3d92e16 | -7.4081 | -59.99734 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e03ffee-c2c2-323b-9d2a-07c22552253d | -10.06677 | -67.55558 | 2026-08-14 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc10c37-864c-3395-9f0a-9d0cbf6a2ae2 | -10.06273 | -67.55499 | 2026-08-14 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8f227f9-04d3-3406-a924-f64e1c78e4d9 | -6.96436 | -59.28563 | 2026-08-14 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d55c6c28-97d0-3eef-9498-4485c628b9aa | -9.77024 | -60.76815 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f099f4-bd41-37ed-b2de-46eee38e2a60 | -7.31595 | -72.68996 | 2026-08-14 06:14:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d99cfe40-79af-36c4-b2b7-d2ee46f739e7 | -9.58424 | -60.50714 | 2026-08-14 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d422d7d1-2c65-3940-b082-4d39ee96675e | -8.95268 | -60.53621 | 2026-08-14 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90302124-afde-3d7b-b404-8cd74823b860 | -8.95903 | -60.53712 | 2026-08-14 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2c0c988-08a9-3d49-ae9c-5ad3ba7afb14 | -9.75386 | -60.77464 | 2026-08-14 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
