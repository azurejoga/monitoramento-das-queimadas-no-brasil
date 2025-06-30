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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b08a0fb-be5c-3ba4-87ae-5b7d92c1c8d6 | -11.20726 | -55.92001 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07c60187-051d-3128-b847-d4f0779c5a77 | -11.02059 | -56.27013 | 2025-06-30 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bc4660c-6edf-392e-99ae-08fa5bf663b7 | -12.60461 | -57.87877 | 2025-06-30 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38e8951d-18af-386a-b825-9af398a03b29 | -10.87644 | -53.77375 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b00bbdc2-b1ba-3761-b727-dcb1bb650707 | -9.09377 | -47.96441 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a4c18893-54fc-3b34-bf29-aac71c168a87 | -12.61783 | -54.21766 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ca0ff01a-92b4-305d-a86e-094b48114672 | -13.23766 | -49.8336 | 2025-06-30 04:14:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 726f6343-82b6-3317-9d5c-3b4a32827987 | -12.62722 | -54.22707 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ec0bbf9-5ce6-3d4d-8ef3-e046f9751a3a | -10.87575 | -53.77731 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beeb2ba3-4950-31bb-8d7b-05ccfa9d1869 | -10.29767 | -57.05261 | 2025-06-30 04:14:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95474833-a4e0-33c8-8443-8a624812eee3 | -9.94673 | -52.17654 | 2025-06-30 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0436acb2-421e-3c90-812c-5faddafc049a | -10.87244 | -53.76546 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c86dac44-29b6-3d2e-b51f-8d9551a3a2b4 | -11.02689 | -56.27133 | 2025-06-30 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 525adb29-a557-30a3-9b3f-d9f4dd41052f | -12.06689 | -48.45373 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 693be90f-f097-31b6-bb89-17542efa7482 | -10.29713 | -57.12466 | 2025-06-30 04:14:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6988f749-fcd2-3440-9c32-992858eb77c8 | -10.85533 | -53.75729 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d492d5a1-bbfd-3d11-8ce3-3506a3472e76 | -11.19883 | -55.92503 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b76d796e-73ee-3498-b065-5b7cfb4cc5d5 | -10.1233 | -57.781 | 2025-06-30 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e1b4861-669d-368b-8ded-248729387009 | -12.10467 | -54.66542 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba9b2d3a-a46f-3f49-b741-4e0a1b3d8fd5 | -12.06161 | -48.46515 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 34fc6367-b79b-396c-a0b8-713f61d32fca | -10.87451 | -53.75484 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0da7a546-569c-354a-a217-8b5dadfcae82 | -10.85728 | -53.74689 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1de45806-1c89-329d-b5b5-4423c2f2c602 | -13.08569 | -54.85339 | 2025-06-30 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27090a1d-3525-34e4-ad4d-fbb53bccb3c9 | -12.62584 | -54.23429 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b173324a-bfa5-3efe-8421-e90bcd1d8997 | -7.85993 | -47.12497 | 2025-06-30 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b38c746e-a2d3-304d-b517-3b59d911289f | -10.29593 | -57.13068 | 2025-06-30 04:14:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1518282-f463-3b7d-b753-b01956c5c297 | -11.57789 | -52.11905 | 2025-06-30 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a990d23-5760-38b1-9b92-14351174eb8a | -11.20074 | -55.91564 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346a4aab-3eff-38f0-a179-483a358615c1 | -11.19495 | -55.91762 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4090e85-abb8-3a1d-bcff-b8ee3531f5ca | -10.8687 | -53.74566 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad2dd521-6e95-3ac2-83af-5555cee40d81 | -12.19644 | -49.63853 | 2025-06-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 882f5ae4-c36a-3d78-8884-3cefea2eb6a3 | -10.12461 | -57.77438 | 2025-06-30 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b54fbf00-fc6d-3ef4-b5fb-a99ae826aceb | -13.08086 | -54.8486 | 2025-06-30 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb8235c9-a8ce-38c4-bd25-68fb2d5e5855 | -10.10253 | -52.19561 | 2025-06-30 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a9fdf1b-1bd1-3ca5-bf2b-322e661dcc74 | -10.12142 | -57.78193 | 2025-06-30 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bbd8f2f-b997-3bfb-8942-07030b60de6c | -10.85599 | -53.75377 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffacb13c-36f7-39b3-a163-365fc6c264d8 | -12.62791 | -54.22345 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 660e4188-5f45-36bd-b9e6-88f02f2f5837 | -12.20175 | -49.6321 | 2025-06-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8816d8e1-3b5f-30b9-9675-8d453bc06098 | -12.09197 | -54.67096 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 543a269d-856b-3dbf-a881-6f8484ce0e46 | -10.87145 | -53.76085 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cc4a8db-6fff-3d4e-b7b3-fe5aaa13efdd | -10.29886 | -57.04669 | 2025-06-30 04:14:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8eae22c8-389b-331a-a12c-a8252133f7bd | -13.42845 | -47.83158 | 2025-06-30 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c379682-d87a-3145-9752-183b7bb59aa9 | -10.86674 | -53.75611 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f1e92b-d6c0-37c5-99dc-ddc3ca6b6390 | -10.80602 | -44.23569 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bb57f12-7a11-31b8-a482-45fc68dc6fcc | -10.55979 | -52.04883 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3fd8106-3aa5-311b-9785-2353c95ce867 | -10.29106 | -57.05095 | 2025-06-30 04:14:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74054c9d-9bbf-344c-9186-c07a1855b208 | -9.09712 | -47.9629 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| be8105e4-b757-3612-9784-346526695c03 | -10.44694 | -47.44413 | 2025-06-30 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6aa9dc5-949b-3f1e-b0d9-8c157e85d637 | -14.4345 | -45.15698 | 2025-06-30 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36b85f72-c8a4-3dae-ba4e-d15ba2c73cf7 | -10.55616 | -52.05161 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c90be669-4914-35c8-b6e3-be5c482bdd45 | -10.87617 | -53.76557 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82d50cc8-70d4-3760-8c0f-3c4bb68f848d | -11.19979 | -55.92033 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60cf4ac2-607d-33e3-8b20-68dcf042f1b5 | -10.86934 | -53.74222 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f13b095-d344-37da-9fce-dbd16b93df10 | -11.92743 | -57.45221 | 2025-06-30 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 94a1b85c-bf39-3901-ac9b-f2b6f0ae5ac7 | -12.06618 | -48.46117 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc138f24-b90e-3ad6-a55f-556508bb8bd7 | -8.71127 | -47.85798 | 2025-06-30 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6931356-2d8a-34b6-bb96-f3364283c44a | -13.08011 | -54.85237 | 2025-06-30 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e504efc0-4724-3fb4-a1c4-4dfc38f2d6f8 | -10.85188 | -53.74585 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfdb05d1-ed4d-3c7b-9163-8080bb565daa | -9.88882 | -56.10718 | 2025-06-30 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c58b4f8d-74a7-3abe-bb29-be12f1a41dbe | -12.01906 | -47.77813 | 2025-06-30 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e28fd30c-5ffc-33a4-8ec9-4609ebaafee1 | -10.80161 | -44.24215 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 6438b561-63af-3518-be2b-31da732e8ada | -10.79831 | -44.24161 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| d92df9ea-b4b0-3daf-ab9a-d2b0fe8e93d0 | -7.64407 | -44.65103 | 2025-06-30 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5df47bf6-3ce7-3330-b58a-cbedd4cabb40 | -10.80272 | -44.23516 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2c5bee22-8434-31c5-a788-457cefb612ee | -10.87484 | -53.7727 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d2d790e-0194-3a4a-bb10-ef3a3f22206a | -11.27637 | -52.46668 | 2025-06-30 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 478bc4e3-0c89-3ba6-bd8b-e62d6c07f292 | -12.10392 | -54.66932 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13895d99-af1a-37fe-89de-64ea516fd7e3 | -12.62967 | -54.22344 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ab0e9f4e-d5a9-392a-8f17-60d6f979ccf9 | -10.15799 | -53.92743 | 2025-06-30 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 126abbc5-86e6-3881-a67a-c406aff5efed | -8.86668 | -47.27424 | 2025-06-30 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d99383b-961f-3ac3-ad55-8a52ab92f1b3 | -12.75962 | -44.40483 | 2025-06-30 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23cd712a-3aac-321f-8442-2f9c3458855f | -7.64464 | -44.64748 | 2025-06-30 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 120b34b7-2cc9-3611-9fca-973aeb84810c | -12.75631 | -44.4043 | 2025-06-30 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a188547-d53b-3842-b8ca-ba1be986b6ae | -12.62427 | -54.22237 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a39c335b-4eaa-3f9b-8da0-e7d3a1cac8a0 | -11.94197 | -57.44888 | 2025-06-30 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 77c04799-9fa7-382f-9bbe-f2bf04d7b986 | -10.8646 | -53.73772 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96d8d498-d102-3130-b075-c0f358b2d85b | -13.07936 | -54.85611 | 2025-06-30 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb649af1-48f7-3796-bcd5-bdc66d17f128 | -12.06913 | -48.46645 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08cb0b9b-65a5-3bbc-b8b5-f3b9fabd1bbb | -9.70552 | -56.18132 | 2025-06-30 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f42ffa9-7d16-3611-bde1-015df12252e6 | -12.62751 | -54.23428 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d01bf222-788b-39b9-8e87-bb8952bd5ee8 | -12.62321 | -54.21877 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d78ee39e-cab8-3c92-a9da-11d1812345d5 | -11.20498 | -55.92625 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d951917-c453-363d-9d4f-9c0278f3a413 | -12.19372 | -49.63056 | 2025-06-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0d9bc44-3c32-388d-9442-407c1942971a | -12.06994 | -48.46181 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 549da490-2b63-34a6-8371-ac20f4c06e21 | -10.87417 | -53.77629 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 61d4b6b6-34b4-328e-b3fa-b2d930749ab4 | -10.80051 | -44.24913 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 059fda67-bc2f-3f54-ad97-7bb2b3bac831 | -10.87587 | -53.74786 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86ae2041-2249-3049-8a6d-eccb70bbdd5b | -12.75907 | -44.40836 | 2025-06-30 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c78f3dbc-7a39-3df6-846c-d937067540ed | -10.79941 | -44.23462 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 100410de-bc37-3988-a1a3-7470a48994da | -12.06779 | -48.45195 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 421e2650-60c5-37ab-85cb-02dc937dc716 | -8.01082 | -47.40731 | 2025-06-30 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 87405164-0db7-34bc-9ec6-d9e3f43c634a | -14.43226 | -45.17117 | 2025-06-30 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12137567-d924-3566-ab57-79f02944eab4 | -10.85253 | -53.74243 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bc94eaa-965e-3d42-b212-d615cf20526c | -12.06537 | -48.4658 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83a8f0e6-efa0-3d86-afdf-d303f65580d1 | -12.62499 | -54.21876 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2145b48-e517-3112-85e1-79729729df51 | -8.08699 | -46.86369 | 2025-06-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dec92110-5a47-3d63-8047-bbe86a9147a9 | -11.20594 | -55.92152 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d377fe-aaa3-3e5b-a4c3-9ca2617121ed | -9.71089 | -56.18785 | 2025-06-30 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 818558d7-b839-3035-8e70-f76d3a844965 | -10.85921 | -53.73664 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b316cbf1-7d6e-3818-a118-e5fe9704feb0 | -12.09794 | -54.5803 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
