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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eae2e23b-f2c2-304a-b0e2-f2af16dd8925 | -6.91783 | -43.63068 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9512c58c-57d5-3d52-b4aa-e540607f2343 | -6.79252 | -55.83887 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52a0b564-96b2-300a-a5e1-eed2d6f4323a | -9.11786 | -46.40493 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20cd773a-0c1a-39aa-a7ce-892b44a87c53 | -6.8398 | -56.42663 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccc44f85-321a-32c6-a0c9-00d2157fd9d5 | -7.0574 | -56.51501 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae1f2e88-b965-393c-b1fa-1835f0463809 | -6.86765 | -43.87086 | 2026-08-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9db3094d-fb84-36bd-b647-af89808c5e38 | -6.6054 | -59.00408 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fadf9a48-0c9f-3607-a991-5a9c5fbf3b7d | -6.59754 | -59.00281 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 419a2771-4a64-3b96-8adf-8242aa902e7c | -9.11358 | -46.39806 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 067c66f1-d5a4-32a8-850b-27b7b4150383 | -8.76161 | -47.45183 | 2026-08-15 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 416c0e99-f9a1-3794-8108-477e4585a3ca | -6.93457 | -52.78912 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbfff878-cbfa-35f7-90a9-1d8fb1929a67 | -6.91135 | -43.63393 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7919dc9b-c04e-36fd-82b2-2a7961d7638b | -8.01978 | -55.12934 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffb69202-59f0-37c0-ab6e-54a93f0110a0 | -8.52041 | -46.51987 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b052fe45-6b07-3043-a67e-74a71e2fd3ca | -3.93598 | -56.25152 | 2026-08-15 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 121a1402-2219-3fcf-ade3-05069187aeef | -3.11449 | -47.91048 | 2026-08-15 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aadcbb49-c00c-383a-84af-a5be450879ad | -10.81576 | -50.32242 | 2026-08-15 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f9c1a95-a48e-3eb0-989b-96880633c29a | -8.61139 | -54.67168 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b123566-c5ff-303f-9ebb-3cfcf925a62c | -11.40635 | -46.33397 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1afffe83-ed8f-38ac-8791-87526c7dd9f3 | -8.61085 | -54.67515 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3f92c86-9712-384a-b7e5-14fce9e2eca0 | -11.41155 | -46.3354 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d481260d-c724-3203-9925-b4643e099a26 | -11.42048 | -46.35041 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| b06000a1-2291-39b5-8285-e62083be8b26 | -11.412 | -46.33783 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de6bc24b-243b-3b5a-8b29-428e472a9e84 | -11.37154 | -46.27482 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd934153-0068-3d06-a64b-51ac8aa6ad0d | -11.14225 | -49.03913 | 2026-08-15 04:59:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67f576ff-5359-3f73-9149-b2a3ae762d66 | -11.42573 | -46.35136 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 9651b471-2334-3c29-af2b-dd4eed709067 | -9.47684 | -60.53763 | 2026-08-15 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daf7e116-026b-3063-a072-15da18d53f3f | -8.6037 | -54.67758 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9825e324-0cb0-3dc0-9538-7e83a4427c3d | -8.95529 | -60.53504 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ad4fc9a-4946-3540-b6e3-2738473b0691 | -8.65317 | -54.71077 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33130373-802a-3f45-ae9e-36da92469c3f | -8.98213 | -60.53584 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c035c60e-1ad3-37f3-8291-a6a0bbc01316 | -11.41081 | -46.34152 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| bfa2a75e-ba1f-3861-97f3-0d51172a4057 | -11.40486 | -46.3463 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c82c494-2c3e-33da-92a5-d838cc42a37c | -8.64932 | -54.71372 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4899e53e-f62a-3c2a-bb88-d0ec3e06cef3 | -11.41081 | -46.34705 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 46753e91-b63f-3222-ad1a-67ba092998f0 | -8.60261 | -54.68453 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e51eda55-3432-3799-aa42-e8f2d02433fa | -8.96877 | -60.51381 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 124c9aa4-c111-331c-89d0-d03888c13530 | -11.42496 | -46.3576 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 7c293a10-2e73-3eec-b666-8d1d5fd50167 | -9.98299 | -53.95548 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69244ee8-b796-321e-a176-6595f8dfc845 | -10.68817 | -50.52055 | 2026-08-15 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6a26990-4daa-3347-9ebd-9eaca8eb6860 | -11.40111 | -46.33285 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 389e86ad-8ea0-3353-9855-757e128c6627 | -8.95984 | -60.508 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7eeb6bd-46bf-300f-8462-87a6ad2b6811 | -8.26235 | -57.34155 | 2026-08-15 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0faee2a1-269c-346d-bfb9-8d9ead62200a | -8.97795 | -60.53516 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd476f3b-c8a1-3ca4-b65b-ca13f48df512 | -11.40795 | -46.32745 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8d21eb70-dd88-3a68-8ec3-ce81e7d554b2 | -11.41239 | -46.33477 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8475cb3-b798-3fc0-826d-4e3ecdf6d7cc | -11.41974 | -46.35646 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 119623bc-55fa-33b1-8dcf-4f8117a48537 | -9.98688 | -53.95243 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22d50d5d-c9b2-3dcb-8fbf-59ccec5dfc86 | -10.40633 | -47.97585 | 2026-08-15 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ff2eab73-81c7-3ac9-b078-e807c257c426 | -11.41938 | -46.35934 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c03326bb-56e5-3a07-9e0e-dc8eb9b2525c | -11.42459 | -46.36061 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 121742c1-8edb-388d-9e2a-4c13805bff4e | -11.93699 | -46.31441 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9e779ca-5341-3c41-a823-ec4ea8941df3 | -11.41118 | -46.33844 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92ba0d3b-221e-3810-bf56-4fa18822ad47 | -8.89975 | -60.55757 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 40f2c323-69f0-3f1c-9947-f04c437adef6 | -11.3289 | -46.22647 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e48d5d3d-8d3e-30e2-9bda-113bf483b93c | -8.95882 | -60.53963 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ffff300-8fcf-3885-9992-ffea097746a0 | -11.41601 | -46.34837 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 5f8d99ec-0601-33f1-8eff-9ecfdd9a1df1 | -11.41641 | -46.34529 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6afb40a6-4cd1-33af-80e6-3cc3f06bfe31 | -9.08038 | -61.39704 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9b18f5-2864-3f0e-93d9-7b8ab1735f72 | -11.40271 | -46.32639 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a446bcbe-ddc9-3de9-b96d-4f029ad8e0a3 | -9.48711 | -51.61216 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ef323df-4dc9-3cc1-8c31-51bb35450557 | -11.41722 | -46.33896 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8966b395-e2b0-3ce9-a2d0-0673cf6433df | -8.95919 | -60.51184 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b7b7a4d-bbd1-3035-8088-dc37103f1581 | -8.64986 | -54.71025 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb7093d-1a7f-3a06-9981-63d99ab56173 | -10.6112 | -46.57345 | 2026-08-15 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1ad5639-c521-3063-a587-dab427772c04 | -8.89622 | -60.55297 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7a7fe31f-f9e9-3aa2-a2e9-ac1ff6ff75de | -8.65203 | -54.69636 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f47f922-98ed-3d12-904f-e8841c1fd299 | -10.21744 | -48.47862 | 2026-08-15 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 094ab0e7-4eff-31ff-a4b4-f64967f2714a | -11.3236 | -46.22562 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 248a491f-9745-3c04-921c-057f22bf9799 | -8.98347 | -60.52816 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 666de3da-09e9-3108-a0d3-2d8544748d1e | -8.96944 | -60.50998 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4389e05a-9e04-3f3d-bc36-8ac7fff00b7f | -11.41042 | -46.35009 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| babc0476-77e2-3972-8759-9724415fc556 | -11.41641 | -46.33966 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7021cf04-048f-32a5-9e33-1a3dbd20b770 | -8.95098 | -60.58628 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6c8e15b-f041-3df0-9c7d-c03410e5dbb2 | -8.9828 | -60.532 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2599cd18-98e1-3750-b610-9d1e96f77b1f | -12.02853 | -46.4059 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f27adf5e-2845-3d8c-893f-1e9b911c0643 | -9.92688 | -56.10311 | 2026-08-15 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ab8672d-52b7-3593-803e-aad45cba0a77 | -9.98634 | -53.95601 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96374a7d-43bd-38af-b42d-7fb3a09e4d17 | -9.98463 | -53.94473 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38a8e056-6ca3-3b2d-95a3-c746efc86230 | -12.0005 | -46.41458 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdf672b5-b493-3677-b58f-a809ef570513 | -8.2617 | -57.34553 | 2026-08-15 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88f97528-b6bd-35ad-9a31-33689770a08f | -8.61031 | -54.67862 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 053f88e7-13b5-37ff-aa13-499445fe230f | -9.98073 | -53.94779 | 2026-08-15 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 73702065-e4c1-3b4b-b44b-970a082f00f2 | -11.36631 | -46.27347 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47c3a869-55f8-3223-b3b7-6307a8fad670 | -11.41763 | -46.33577 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf623169-d9f0-3110-a104-950805d5d2e1 | -9.07596 | -61.3963 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9c9975-6a01-384e-baec-d3f0e534712a | -11.40969 | -46.35075 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 3b36ab94-52b3-34e1-8951-3ffb5f832542 | -11.40182 | -46.32696 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c83f6580-223c-32b1-80f7-233ad22b23ed | -8.96465 | -60.50489 | 2026-08-15 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c498f8a-2d65-31a9-a83b-f839194afc80 | -11.41524 | -46.3544 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3b547aad-3fc3-3225-960b-6c91a3e82383 | -11.40196 | -46.33225 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a8f560b0-b814-3013-b8eb-2418970ff90a | -11.4067 | -46.33106 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6035368d-8994-36ee-85b9-37cbc22e6ffd | -8.64872 | -54.69584 | 2026-08-15 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94b70d44-e7b8-3b85-be58-904398ddf4b0 | -10.41565 | -47.97709 | 2026-08-15 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 98207246-2502-309e-bc04-e1ca51f5bc77 | -11.93662 | -46.31756 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfb73a3d-92a8-3807-b402-3c60092a4248 | -10.51856 | -50.15732 | 2026-08-15 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b88a234-b8b0-3fad-bc0b-104a66429751 | -12.00089 | -46.4114 | 2026-08-15 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f764dc1-8a8b-3e64-a0f9-30b387abeec7 | -11.40234 | -46.32932 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcf6790c-76a7-3274-b3b3-bec526076f3c | -11.41564 | -46.34596 | 2026-08-15 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 16556069-d3e6-3e76-a432-013d61bfa64b | -10.51807 | -50.16088 | 2026-08-15 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
