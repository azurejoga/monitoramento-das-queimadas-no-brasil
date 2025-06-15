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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71eae91f-504a-3503-b01b-4f729a4f486f | -11.00564 | -55.08361 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee7659bd-a6c2-3001-a108-4d3c7ae6d6ef | -13.91366 | -54.6567 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9783d6c5-681a-304c-91db-17e17e028779 | -15.64117 | -49.37375 | 2025-06-15 05:14:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1538ab71-0e8d-3346-b90c-09646489b6a1 | -10.9212 | -54.76591 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9899af08-4d08-3619-8c93-1d7c500f2f57 | -12.02565 | -57.09125 | 2025-06-15 05:14:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fd56763-09ef-3f81-835a-ea8b18f54c72 | -10.23386 | -52.2348 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e1b8fdd-c83d-38c9-aabf-e3adf9e38fc2 | -10.85413 | -53.7849 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a27f2012-8a4d-39e8-86bf-08b763bf3352 | -13.90695 | -54.61985 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65698476-f46d-32b2-be89-554dcefb7ee4 | -13.92254 | -54.6223 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5ce36f92-eda2-311a-9c3a-d17a7b14cbdd | -12.69486 | -52.3976 | 2025-06-15 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dbf8b760-f221-3fb6-a7ad-9210620532c8 | -13.91461 | -54.64909 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0370bfa9-edf7-33d8-bce2-12901ca49837 | -10.09445 | -52.74197 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dbd9513d-eb13-3e94-acfd-9a8558d0f036 | -14.6716 | -53.13296 | 2025-06-15 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41f14cef-7c98-370c-aaec-edadf82b296b | -11.8838 | -54.67832 | 2025-06-15 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44a81d5f-e6ff-3b5f-8bc7-09108b9c7ffa | -12.46802 | -58.46872 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37941415-5b9b-3712-97fc-560a65600c1b | -10.84695 | -53.77874 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c50558bd-2fc2-3026-b28a-5cf8297cf332 | -15.07697 | -48.94622 | 2025-06-15 05:14:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6269825d-a95f-3e83-b7b9-ecb686f8def3 | -10.08482 | -52.74561 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2db502d7-20c4-3ed8-ace6-7cd30ec210c1 | -13.91393 | -54.6541 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8359892d-f202-37d1-b542-1ef2b5dce610 | -10.07232 | -52.74374 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdff338c-f8f8-3277-ac7d-593c95058ca2 | -13.23014 | -49.83416 | 2025-06-15 05:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2b0c319-3212-31e4-a5c5-260de7349170 | -13.92326 | -54.6146 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 41f2f96b-e410-3207-adeb-e60cd5b3fd97 | -10.8509 | -53.77931 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e64f4922-891d-3f76-b899-a9eb33ee441a | -11.88693 | -54.68355 | 2025-06-15 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f04fb54-de09-3959-94ec-3994b6a3e3b7 | -14.67593 | -53.13363 | 2025-06-15 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 209d8824-67d2-3b1b-9b42-75f4c65e4f83 | -14.84032 | -48.43993 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b26ec6a6-5bbd-37cd-8d24-5f07e01e1633 | -13.91022 | -54.62272 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed7525eb-965b-3683-8480-c5853cb14ab6 | -12.02905 | -57.0918 | 2025-06-15 05:14:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c74192a-caeb-35d2-b7fe-41c5c3e01d15 | -13.90377 | -54.61421 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 519d46e8-91d9-3fa7-9a42-0052b10532c4 | -13.92397 | -54.61228 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18b07c70-f1cb-3a21-a3c4-82dd40f47ca2 | -10.74522 | -48.5757 | 2025-06-15 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed3fb1a7-2541-3760-abf0-24b265428ea9 | -13.92004 | -54.60894 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52638fcb-c47f-3c3a-a46c-08dc2d3d4b70 | -11.04917 | -62.58703 | 2025-06-15 05:14:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b2791a9-1544-3aa1-94e7-e623a6bd65e1 | -10.723 | -46.56081 | 2025-06-15 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f0040c4-6b27-3f90-826c-1c9e5a4ba5bb | -13.22972 | -49.83754 | 2025-06-15 05:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fdf9543-cb04-3329-bb2a-dfb22bfba406 | -15.40401 | -47.85408 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f1981b0-819b-36b9-9ed7-3c44ce8cc5ae | -11.88248 | -54.68766 | 2025-06-15 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33b5b27e-2dde-39dc-a1d5-d4e73e32de16 | -13.91616 | -54.61109 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 12acfa0e-df2a-3ff3-941c-354f054f6efd | -11.00501 | -55.08792 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b76b7520-d0cd-362d-9a81-117db6be2200 | -11.7781 | -47.39041 | 2025-06-15 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2200b34c-b8ae-37c9-b941-6b55ae68dd17 | -13.92152 | -54.60145 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cfb7b21b-fb7b-3597-b1d5-4b37140a5517 | -13.92645 | -54.62282 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4deef507-a4d0-357b-8659-f8a143783c73 | -10.50772 | -53.5825 | 2025-06-15 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 99de4e6f-7711-31ec-9b87-66be6f45e45f | -14.54146 | -59.8736 | 2025-06-15 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb309c4b-789e-3fcd-b860-1b318fc999f8 | -15.40561 | -47.85862 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7896a07-630f-3a9c-84a1-c64a14a40b58 | -13.29045 | -57.06736 | 2025-06-15 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ea39100-23d1-375a-9d36-47fc9963f2f2 | -13.91733 | -54.62897 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e86663b3-f928-3248-9e74-88d50663010b | -13.91293 | -54.60258 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| efb69edd-4ab4-344c-96d7-701f755ba0ef | -13.91919 | -54.64462 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e33b5ff-5f95-3424-a49f-f854855d13ac | -13.92718 | -54.61512 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 418f06d7-4050-36c4-ae3f-54a586f682db | -10.91748 | -54.76533 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08331d7d-00c5-3f0f-adbd-38118b155598 | -10.92315 | -56.8443 | 2025-06-15 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9cc0133-8eaa-348a-bce8-711562743247 | -15.40106 | -47.8826 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e069ca51-74b1-339c-9d2c-1bc9c10dac5b | -14.0356 | -55.11905 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74e6d611-e086-3b4f-a7d5-f48e25889158 | -10.84371 | -53.77313 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c04c813-687d-3ee9-9178-22aa501ffeb0 | -10.91812 | -54.76087 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb34dd22-74ae-3adb-9d35-4cbcf4070e05 | -13.94435 | -54.48841 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0c09435-1a50-3506-aa4c-4c4a5a7a52b8 | -15.40973 | -47.8596 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9058215-be81-3201-b85a-426533948212 | -11.88627 | -54.68822 | 2025-06-15 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cdc489bb-b371-30fb-af36-3d7eb4573199 | -12.48741 | -58.46783 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bd7cd99-56a3-36bf-acfd-e446e0c1b0ee | -13.91508 | -54.64673 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e668f4cb-6474-349c-a1a3-e3519b333f9d | -10.92056 | -54.77037 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e48668fc-cf72-38d9-af96-f9319e252126 | -13.92395 | -54.6095 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a1c45573-e5de-39a7-9b4c-177ad83fb265 | -15.64455 | -49.37601 | 2025-06-15 05:14:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50608dc2-ecf2-318e-a077-d676eb91d20d | -13.92079 | -54.60661 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 985153c4-8b3e-3c84-bef7-7314529bb88f | -12.68982 | -52.40148 | 2025-06-15 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6df0ce6f-b80e-3d23-a9b6-6bd19fedaade | -13.91689 | -54.606 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3dc2919e-0071-3c7b-834b-0e55d87993a0 | -13.9247 | -54.60713 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b681617f-998d-32ce-a345-5f3d12ae9daf | -11.00628 | -55.0793 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74de7853-66be-3159-9b64-bbb4f8f94b06 | -13.98346 | -56.02161 | 2025-06-15 05:14:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bdeee155-7d23-3bf7-9301-4338b95dc2be | -13.91969 | -54.64225 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67f540b9-0d36-3b31-9c28-0d0da5a40596 | -13.91227 | -54.61045 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 99943d37-e457-35c1-8c58-c61c2f6760a5 | -10.62145 | -54.91726 | 2025-06-15 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4de2fbc9-b260-3847-b712-b8b375217e49 | -10.23818 | -52.23547 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cebe4cd7-ce41-3aa7-b3f9-22cfc61c60ad | -16.28986 | -52.93687 | 2025-06-15 05:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4855f362-df07-38b7-990e-e844d8d5a488 | -14.82882 | -48.435 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76e4d24f-e076-3c0c-90c6-cfed4ed65848 | -14.83567 | -48.42738 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b464fe-6846-3755-b082-a5b4989dddb6 | -10.63445 | -49.42562 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df0714a6-72d1-37e6-b302-3c163472f256 | -10.66314 | -49.36311 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4c8076f-7fd0-3177-9d16-8ddf550fa984 | -13.91935 | -54.61673 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 452de7b6-07e0-38af-8e78-ed571b2e1e1c | -13.91156 | -54.61545 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 242268b6-654b-3d02-a060-09fc14cd4245 | -10.27351 | -47.61082 | 2025-06-15 05:14:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd32b7c4-1e0f-35c1-9ac5-0efa146cebc8 | -13.9158 | -54.64169 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 170eb2f5-f9f7-3d65-a90b-c987a4424292 | -10.09372 | -52.74297 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3007b5d4-54cf-3325-9b9d-34181cfa557c | -11.77754 | -47.39519 | 2025-06-15 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40ac24f1-7b30-35ec-8f82-741180b6fd4c | -13.90448 | -54.60914 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf870fe1-7668-34fb-ab2b-0cb0b164c020 | -13.90766 | -54.61483 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 29fcbd5e-fcd1-35e0-9c47-90b857955b39 | -10.08065 | -52.74501 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8704692-139c-3ec5-a26b-185f84b20012 | -13.91545 | -54.61609 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 754f123d-1a92-3c9b-b690-ff05b017bd36 | -10.44893 | -47.95015 | 2025-06-15 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf6731c-0ca8-3beb-9083-f0119c1e762c | -15.40153 | -47.87809 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fec14432-05a9-3f8a-b4e2-13d4b4d85ab9 | -13.91412 | -54.62333 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6ec59b0-095f-3675-a44c-1bbd367a4908 | -13.91371 | -54.60027 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cf8cbcea-cdd8-3178-8884-dda342d45b98 | -15.41398 | -47.87908 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb2b3954-9f23-35b6-a3b4-8091b378b743 | -13.91783 | -54.65462 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9ea59c1-d98e-3a80-b7b8-fcfa9ea6cf46 | -10.17134 | -52.61924 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85881b38-93b9-3309-a053-572258a92a38 | -11.13437 | -53.94489 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 872bba13-eedd-3403-9da5-f505827edbe1 | -14.67212 | -53.12887 | 2025-06-15 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 076cebc3-0b44-366d-91a7-5c0c3b9a16bd | -13.91851 | -54.64964 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20170eca-8b71-3909-ada9-02fb4fc89413 | -10.93732 | -56.84274 | 2025-06-15 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
