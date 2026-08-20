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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9f69d80-97e3-3d3d-be80-05ced6b29c36 | -6.42732 | -52.76116 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31845b6c-6e92-3c58-a93b-d5d53e54b52b | -6.38447 | -54.9513 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40b166f9-26b9-3413-8c4b-4a3e66154859 | -6.09957 | -57.86736 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7676716-b8f7-3e9c-ab5e-8a6ad9eae48e | -3.1069 | -61.20679 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ecea29f-4cb8-3d0a-a605-c754c71acd4a | -2.85061 | -60.17144 | 2026-08-20 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c38d3e-e1e7-31a7-98c5-3664fa51eb92 | -6.43835 | -52.72223 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2e3f40d-23f2-3d4a-a54c-06efa3dd912a | -5.49349 | -60.12734 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 294af1ab-1410-3344-82ca-4d4a9b122b6e | -3.09526 | -61.19436 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbbbb303-7414-3cfd-ac6f-b4ddd4430563 | -2.80375 | -48.59562 | 2026-08-20 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af27a3a4-9aa2-3294-99cf-51bb379ff689 | -6.43735 | -52.72945 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 992bf191-2250-3acf-87ae-50ae06434d70 | -5.49291 | -60.13106 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bb5967d-7e41-3145-8a81-f742597d2e66 | -6.01498 | -57.87245 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff0ee1eb-1a0f-3452-9d64-adf4ce967aec | -3.09917 | -61.21265 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31ee2248-a290-3c11-9f34-705cb6eb5d83 | -6.52593 | -55.05639 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aec7d160-2a13-3d1f-9c95-2bce975834eb | -6.95337 | -52.809 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e08a8604-6832-3e4d-a600-ed3765e55e90 | -6.87202 | -59.02393 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad877ec2-7435-3d8d-bfd5-790bd6c53d0c | -9.3203 | -68.67024 | 2026-08-20 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c87f555e-c394-368e-b8e5-b9c4e9ae0870 | -11.82815 | -58.84536 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b17e17a6-2617-3d8c-8ef3-90c854b45de2 | -8.58782 | -54.77618 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30c3d30-17c2-3284-8353-752e284397de | -8.53733 | -54.87427 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f25aba6c-988b-303d-81b1-d5e388fe306c | -6.92229 | -59.35363 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e2d17d2-9e36-3a60-af33-22bfab16c650 | -11.20427 | -54.00578 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4ac2e42-a265-35b4-af79-31a0de1ba641 | -12.04951 | -55.45575 | 2026-08-20 05:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d29834d-2abc-3734-9e1a-acce832c1401 | -6.87139 | -59.02819 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6efab22-7d49-3e61-bae9-ab0c8e002402 | -9.25678 | -56.91608 | 2026-08-20 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79abf13a-ccbc-3faa-9ebe-ff51a9dfc76f | -8.56753 | -54.66357 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80ec30f9-e812-3455-ab99-4a17a6ca9f34 | -6.75319 | -59.46289 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 257fb80a-93fb-3c59-86b9-672d32d2be40 | -6.96085 | -59.05491 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2854e49b-4f24-3079-8bb4-4de105445485 | -6.69926 | -58.93593 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c53fe291-9a11-3e3c-9a63-8a310a3f8fee | -6.59224 | -58.978 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78890a66-3183-3e0f-ab4a-45703362fdf9 | -6.75676 | -59.46343 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70fd424e-d676-32a1-8073-1ba70d9a78d6 | -9.06423 | -60.44335 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf8d1c9a-0be8-3193-b5b7-d03a0c2fe318 | -10.39865 | -61.20892 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae07ee66-c4d5-35eb-aafe-d47b3d3b7c7b | -11.83677 | -58.84136 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5d26dd4-6b98-3562-b474-1158d9d461d6 | -7.53725 | -55.57954 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfef5c1d-c2b2-3e63-b2bd-8e31502b98c6 | -7.00387 | -59.59428 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 302da88b-859c-300a-8039-796ec7b87f67 | -6.92652 | -59.35005 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a66ee6b-7084-3cde-ac7d-5529e79408e2 | -6.95419 | -59.04953 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76877741-350c-331d-be50-11306a922ec0 | -8.56209 | -54.77026 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 171123b3-3d16-3a61-bafa-3f0b8a886856 | -9.39019 | -60.59457 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9751c91-f8cf-3449-9726-cc674562fd00 | -7.87306 | -61.58482 | 2026-08-20 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6f0080b-9f48-3894-909b-e871e666db48 | -6.76338 | -59.15194 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7f7ffe7-0013-30ea-95d8-3fb50e8c7503 | -9.21139 | -59.78078 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 40ee2749-4fb9-3d48-836c-9cf8cdad350e | -8.5631 | -54.77268 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7695812b-e28a-3481-9753-e4d1eba8bf89 | -11.82494 | -58.83967 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 878d09b0-e374-3827-ad0d-f11744d986d8 | -6.86773 | -59.02763 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0856d3d6-9812-3615-8495-f50bc5501e13 | -8.5882 | -54.73608 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9402efe-eb69-383a-b184-e17f951f62b6 | -8.50377 | -54.86386 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9edba429-98c1-373e-98a1-cc6c3293787c | -7.60966 | -60.96989 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 317336a9-920e-34c6-b855-d3c1b7ac9da5 | -11.21391 | -55.04638 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 796f362e-b85e-3a59-b4f8-3c2f256972d3 | -13.63034 | -51.77737 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b17f70e-0900-3801-abac-d44bfe35093e | -8.90015 | -60.54707 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| a18de7ca-7f55-365a-8af7-29f1ada48d77 | -7.82897 | -61.60333 | 2026-08-20 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77b1a512-30e9-36d7-bf89-8a40ba0fb670 | -9.74448 | -59.31282 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58d7b71a-63dd-31b6-b3e6-1de7eadeb892 | -8.28831 | -62.89789 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70866e7b-43ad-364f-9583-955c60eb7120 | -8.68189 | -54.64531 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8f04865-8cc8-3b3f-abe6-9ec13de3da74 | -7.05578 | -59.84142 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d40060c-d61e-3abc-92c0-dbc530cd8774 | -6.79579 | -59.58359 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7174990-e1a5-3a6c-a5e3-ce7965b844bd | -11.22095 | -54.0045 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1d30c5f-1654-31bc-a56d-7b552c9ac619 | -9.21202 | -59.77662 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 103fbcfc-d1d9-3d49-9a0a-0418572b0fcd | -6.80257 | -59.01501 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d700de1-524a-3fa6-826b-3918780e5672 | -7.77247 | -61.15851 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 759597b2-2d32-3397-85c7-05743f841d07 | -9.42509 | -60.41176 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fabec79f-e95a-3fe3-83b6-65aa110d66e3 | -7.60173 | -60.95372 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51a23926-fc36-3693-bc83-2875e2b853f9 | -8.55818 | -54.79786 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83b83848-f54f-3483-8bb1-d523fd3ffbc5 | -6.69618 | -59.10482 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 610e74cd-96b6-36a4-ae2d-6ebaea512bd5 | -6.69318 | -59.10009 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aadf685c-7ae0-3cf4-b445-9f71895896b1 | -8.52913 | -54.86145 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1800858-3922-3120-8ea6-cc2a61ac364a | -8.58018 | -54.75811 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53110fa8-af91-332f-9cdc-8100d2c37e28 | -6.84342 | -59.01698 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 883d36cd-70d4-32a5-9457-fd2c68cb3965 | -8.56102 | -54.67439 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f8aec55-458d-3ed4-ba22-bb4a6154cf1e | -8.57718 | -54.78029 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b7a3113-cc4d-3f89-9ea8-32c0ef18c67b | -9.10468 | -60.93423 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5cbc64d2-f8da-38da-a80f-ad6ca35ff97e | -8.56235 | -54.66067 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 784c1b88-5e82-3c70-879c-2c479116cb05 | -6.97663 | -59.5819 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28f96353-6016-3620-a690-245f2e2a2b31 | -11.99708 | -53.43761 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 037c6848-9c52-3287-8d11-616749650e82 | -7.88625 | -61.19092 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 978d3389-d425-33ef-bb9c-72bc6fcc44d8 | -12.49747 | -54.74378 | 2026-08-20 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba38b5a0-91cd-3665-a7e3-98fcc40a67ac | -12.16569 | -59.76063 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 250e79ef-4955-3d79-877e-e990d8e45860 | -6.91869 | -59.35307 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 465c4e0e-8179-3751-b1ea-64a7ecc4e2ac | -8.54294 | -54.86998 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6592124d-47a1-36e3-9f75-d5dd59edf921 | -11.21818 | -55.05303 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5098490e-789a-3b4a-b18e-93d75d72da6b | -6.5916 | -58.98225 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47359f57-c6bb-3ab2-89f9-d5e44ac2de40 | -11.20472 | -54.00231 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 032d11dc-f6c8-3436-a8a6-aa9d682a1ebd | -9.21265 | -59.77245 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac36aa66-adfc-38c8-896c-83336df57a9b | -6.93651 | -62.88165 | 2026-08-20 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 031343e0-74fb-3e84-ae27-7d38f11583b2 | -6.70709 | -59.10643 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e755ed1a-bb01-3546-8641-7ff491c38ce5 | -11.19164 | -54.01839 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d448830e-7abc-3408-961a-b9d329138d16 | -9.07694 | -65.41127 | 2026-08-20 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eef344e-3b1f-38bb-a9ac-5f994c019579 | -8.67984 | -54.65723 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 939e93ad-a4ba-34b4-ba42-d3c273089afc | -8.40085 | -62.69843 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90accd66-a678-3498-b97d-cb216a62fad9 | -8.53325 | -54.86778 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cdf0d3f-d1f0-3e62-93ce-8186c64f79af | -9.4174 | -60.43877 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 23524925-44e6-3184-acca-fc58185dccac | -8.54222 | -54.87511 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c7c0534-8d32-38a6-9264-d790b855f450 | -11.1993 | -54.00165 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe7aee2-3e2b-3ec1-9760-64596d5dacf8 | -10.38432 | -61.21054 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbf4da2f-8e2f-3001-8f01-e17afb35b957 | -11.6948 | -62.7524 | 2026-08-20 05:42:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eb8b85d-b5c6-3422-a3a9-b7be93a663b5 | -9.42091 | -60.4393 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89f903b1-9f28-3128-876a-2a43f476de93 | -7.42722 | -60.02732 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1774cfff-ee10-3985-9a6c-6c23280cfdd8 | -6.86341 | -59.03298 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README60.md)
