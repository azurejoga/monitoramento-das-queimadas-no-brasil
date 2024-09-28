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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c5f40a4-9003-3709-862a-1fef220bea87 | -12.5188 | -47.97241 | 2024-09-28 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7caf6d72-1d9f-3d3c-b9f7-c7cda7a12df3 | -12.51827 | -47.97672 | 2024-09-28 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0692f949-15a9-3c00-958f-41856c02f7d2 | -12.51777 | -47.9729 | 2024-09-28 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16db221e-3d52-3aba-bda9-47426719aa45 | -12.51727 | -47.9772 | 2024-09-28 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec739ce8-3920-3fc1-b2b8-7b7c9890d224 | -14.86118 | -48.92974 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3e2d9f3-bc7f-3df6-a77f-ff0e57e136c5 | -14.85548 | -48.92929 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9ba2c53-a39c-3b7a-b3a0-9bd8c4994d3d | -14.85513 | -48.93248 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2254727d-5789-39e1-91d3-715800b79059 | -14.85023 | -48.92482 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1358c2a-5078-3a4f-b9c2-d80cec283db1 | -14.84986 | -48.92821 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5c6ef0f-8aa0-39d2-ab21-2898467a0d02 | -14.84742 | -48.92424 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43882f3f-81d5-3510-a29d-ee349c3b903d | -14.84702 | -48.9277 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd48b1c2-915f-3a2e-9afa-1f65cb2a9e1b | -14.84422 | -48.92724 | 2024-09-28 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd8ae6d3-73b8-300f-9ebe-8379f1f1e9df | -8.97226 | -49.82577 | 2024-09-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28bf6f99-bd59-3773-ae32-5a1d80456647 | -10.76252 | -49.85984 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d9c62a3-3281-32b8-ab64-b265babbe8e2 | -9.89519 | -50.13854 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b48a014-6cfc-366d-8395-5cc9c1eb4107 | -9.89289 | -50.13683 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 82a4c72e-44f8-34b6-ba08-282e9f042814 | -9.57623 | -50.1337 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9440db0-a933-3765-863f-779ec4712912 | -9.56725 | -50.12694 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b00d3e54-c53f-3610-bdc1-98b7a8738867 | -9.56648 | -50.19508 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75e8f1ea-8997-329e-92e5-23d7078c6693 | -9.56527 | -50.12884 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2223e4c1-c497-3fe5-a889-76f5682362a2 | -9.56312 | -50.19238 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad4236e0-b090-3ab7-a200-12aa573650e3 | -9.56237 | -50.19774 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1ed8c1e-bd12-3f04-a8be-427755631030 | -9.56234 | -50.18903 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba0154bd-76b7-3b41-ac9a-ccbc3db38ca7 | -9.56164 | -50.19441 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db7fc043-1057-32f3-8340-4dd54537e457 | -9.56164 | -50.13168 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d49f5c4-6457-32a5-a8c6-1bd3428a1821 | -9.5604 | -50.12816 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6db530ce-9421-3f22-af1b-2f70ef873984 | -9.55753 | -50.19707 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abffa67a-e080-39f4-b84a-a63765e28367 | -9.54636 | -50.20646 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b92186b-cf69-38cf-b7a8-838f21bbe4f1 | -9.545 | -50.2085 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f04c53bc-0908-33fe-9470-31e3e523cb08 | -9.54152 | -50.2058 | 2024-09-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bd7e701-48c0-3cbe-9358-8f37b41e1750 | -9.4183 | -50.03298 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6d7d8bd-367d-3b92-a67c-b544a034c456 | -9.41756 | -50.03845 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63f2b7b2-2531-3ef9-aae8-de434cdd7363 | -9.41267 | -50.03781 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6cc41e3-7ad6-35f5-b5fc-91b892416d00 | -9.38625 | -50.01183 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3c602862-e5a0-3723-a3f6-744069a32d9b | -9.38552 | -50.01735 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c7c00019-c7a6-3f04-b7df-2975c763f3f4 | -9.38479 | -50.02285 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee7a34b4-29c7-379b-97a8-f891a582ab5a | -9.38135 | -50.01116 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a624fef9-5651-39f3-84af-560f87aac27e | -9.38063 | -50.01667 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf135b0e-fbdb-3695-a7da-e916f5165767 | -9.3799 | -50.02216 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4a00dd7-0501-34a6-be28-286b3b7687d3 | -9.37824 | -50.01417 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 506057d2-df25-3735-b885-df8d21309a3b | -9.37747 | -50.01967 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4baff431-b85b-3d25-abb0-d3f14d25ec2f | -9.37646 | -50.01048 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc484329-0f7a-3e77-94ba-8ac1fcfea8ac | -9.37573 | -50.01599 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 069fca6c-5043-3c97-a04e-e2e193abf623 | -9.37501 | -50.0215 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe534c02-3e16-3ccb-8723-a9eceafb40bb | -9.37335 | -50.0135 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8b6a76f-0db9-3f8e-8db3-99123821b9dc | -9.37258 | -50.019 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82896461-948f-3b49-8128-27caa831ea45 | -9.36667 | -50.00912 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d87743f-8c99-3cc4-9d0b-51b5d1c63a62 | -9.36433 | -50.00668 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcb265b7-1ad6-30de-b713-2e130c334d0e | -9.36357 | -50.01217 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e97c4168-110a-36a2-96fb-9dfb316e810d | -10.14199 | -50.00377 | 2024-09-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f6c9e66-0d96-3773-96b6-2bf59de9386e | -11.02032 | -50.18475 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdffe26f-3cc7-3724-ba9d-db49424e1eca | -11.01958 | -50.19041 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c37c81c-2627-34da-962c-f13a90017c10 | -11.00968 | -50.18909 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 334f1450-b6e5-3346-b457-02f7d143296e | -10.98712 | -50.16876 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a99fb798-6988-3510-ad54-7f64973f7b17 | -10.98639 | -50.17443 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3dffc0ae-0aac-32ac-8a08-5c5c7e2391af | -10.98493 | -50.18577 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d87d5914-bdf8-3cd8-96b7-0b7add447954 | -10.9525 | -50.1236 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 971bf4bf-7ae1-37f5-99cd-b576fa6a4ae9 | -10.95188 | -50.12261 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35b178a6-7875-3a65-bd64-cd4dfdc22404 | -10.95112 | -50.12831 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 049b2747-4dd7-35c5-aaac-f3f906156ef8 | -10.95036 | -50.13401 | 2024-09-28 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27002237-9f37-35e2-b61c-24529d359b43 | -13.56105 | -51.05183 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39bbb955-022e-3857-a8fe-b6ff2db66cfb | -12.70585 | -50.96375 | 2024-09-28 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 242921af-7620-37eb-8b02-d51a2b5d31d6 | -12.43423 | -50.95516 | 2024-09-28 05:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f377dbc-a549-3e14-a966-458d343da582 | -12.53402 | -50.62877 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9343081-9c58-345d-ada7-871b08230c4a | -12.53332 | -50.63435 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bee70c44-ccfb-356e-a19d-bb7ef8a83369 | -12.52911 | -50.62812 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad48fd68-c81a-391b-b75e-80a549ee7249 | -12.52841 | -50.63369 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13c96699-7dce-3616-b146-7032633b9df9 | -12.52771 | -50.63926 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| caeee76a-70ac-32ee-901f-52b38e956443 | -12.39615 | -50.46413 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00329c0c-11bb-3e92-9eed-6d4e67de28e0 | -12.39541 | -50.46982 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7afead9-403a-39cb-8753-008744a2c3e6 | -12.39193 | -50.45779 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| af117fac-e59d-3811-89eb-b4bc7f81a763 | -12.39119 | -50.46349 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be02cbe8-8ca7-3a63-ae5d-f2255ba263bb | -12.39046 | -50.46917 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebf315f2-1b6a-362c-a167-f97e18f13af0 | -12.38899 | -50.48053 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5f9cce6-c282-323d-8d1b-76a2d03e74c6 | -12.38404 | -50.47988 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8edfa8e9-ba62-39a6-b28b-91640cd6dd5b | -12.37356 | -50.44378 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 140b2cf0-2fc6-3ec8-8665-4f791b88319c | -12.32822 | -50.44361 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ce71d3ff-faa6-33ec-8586-4783a13f9e2e | -12.32327 | -50.44294 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2c4b711e-0d2e-3909-bc50-3cf1df12956c | -12.32256 | -50.44864 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c5aead50-a6e2-32b0-b1a5-e96aac1d09cf | -12.32221 | -50.44087 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9e586a6b-ed33-3faf-8035-44680b1d00c7 | -12.32146 | -50.44655 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6f0e879c-5e66-3f56-a274-f98c1651d98b | -12.31831 | -50.44228 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e6211ba-c5f7-3447-9c73-700c3ed27b1a | -12.3176 | -50.44798 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 79ec4d38-5deb-3a3f-aea4-a17c3c3be4ea | -12.31651 | -50.4459 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8159bd47-5ede-37c2-893f-8dc42777b8b8 | -12.27672 | -50.63434 | 2024-09-28 05:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9805dbf-6468-38a3-83d6-794ab321ca30 | -12.27432 | -50.63612 | 2024-09-28 05:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ca6fd1c-7ab6-32b5-b360-8426af8286dd | -12.24384 | -50.65795 | 2024-09-28 05:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f2e6775-c6eb-327f-b2c5-973036834779 | -13.69716 | -51.09317 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 663b24eb-0a9a-3828-b851-ab92f47cc755 | -14.98478 | -51.45628 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ee9d474-156b-399a-9ebf-056efcb337de | -14.97216 | -51.44147 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20a17007-4408-376b-ad59-e4ba42f81389 | -14.96736 | -51.44085 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c66f9f21-b411-375f-8f21-0b41b465a1b4 | -14.96685 | -51.44304 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe6f9399-86e5-389f-87fc-32a0560eb9fb | -14.96141 | -51.44778 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f977b541-a2d9-35d9-ab5b-793d4ddd2357 | -14.87632 | -51.54749 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 41c0bfcc-81b8-373a-825d-2723ee41b5b7 | -14.87289 | -51.45563 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07afd263-28b7-3ffe-affa-c7ad2790339e | -14.87284 | -51.53634 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92e034d-9715-3962-8683-81d3ac5bdedd | -14.87224 | -51.46097 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24f34771-539d-3ab2-8755-552a4614fdba | -14.87156 | -51.54686 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d657fc28-c1be-3649-8724-7ffd7ecda037 | -14.86854 | -51.45356 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 44dd417d-a4c3-374f-a2f4-c0c627a6f562 | -14.86809 | -51.455 | 2024-09-28 05:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |


[Clique aqui para ver as próximas entradas](README78.md)
