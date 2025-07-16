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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39f9bf29-9bed-324b-9f69-5e8a6227b05c | -13.0177 | -45.06133 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1b97b938-b9f7-3a05-af9c-1d563292b308 | -11.94498 | -48.42173 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16025f44-ad47-3f87-a09c-57d93112f1da | -13.0246 | -45.05524 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1a992fcd-cc85-3e72-86ee-ddc4325486fc | -14.60502 | -48.6709 | 2025-07-16 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd86032d-6057-3333-bfa8-75b21c942b12 | -8.68434 | -51.45694 | 2025-07-16 03:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 385b2569-da00-3c48-b6ee-72cf96ca9c48 | -12.73634 | -47.07398 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1885caea-c08b-353b-918a-dfe61916ce89 | -8.53778 | -47.85219 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66b5163f-f15a-3677-9868-1ded58758560 | -14.60592 | -48.67157 | 2025-07-16 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95053308-5d8f-37a3-bf40-a0fd0bbbf89e | -11.45772 | -45.10559 | 2025-07-16 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01873493-63e6-3b1e-8ac6-e07961d53d25 | -13.65194 | -45.73185 | 2025-07-16 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa4bfe4a-f93b-35c9-9bfc-771002cf9dd9 | -13.12336 | -43.48868 | 2025-07-16 03:51:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68dabb2a-4452-3362-9c36-5dd2d29c4a5f | -12.99559 | -44.87927 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df9e7904-c23f-3388-baf1-c2a7858fdd4b | -12.48427 | -46.92796 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32821662-de25-3db5-a2a9-2536dae9587a | -11.95049 | -48.42085 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 06394272-e6b0-3289-9991-e12b79fb44b8 | -12.47174 | -46.93224 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760125a3-bf05-3adb-99eb-2cfbec8ca181 | -10.57054 | -49.11721 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff9bda6e-04cc-3e0c-9fb0-fb8508827ccd | -8.75879 | -46.59649 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b593a422-18b6-3ebc-8382-d3bf99969657 | -11.45861 | -45.10072 | 2025-07-16 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdd2c5ec-5781-328d-b6d6-5e6f24815588 | -16.26269 | -46.90924 | 2025-07-16 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61871c47-f7fe-3966-b835-ab5a61c3fa0a | -11.49575 | -48.07777 | 2025-07-16 03:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cbc8d22-87cb-35fa-b1e7-afeaa5a068cc | -9.29993 | -44.84515 | 2025-07-16 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf6e4c09-c18b-30e5-85d0-6809b316b9c8 | -10.27987 | -47.62102 | 2025-07-16 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cadef63f-d929-34d8-a740-39e227a20305 | -12.48881 | -46.93207 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34f5d3b9-5092-3eda-8c27-5611558d9497 | -9.30465 | -44.84602 | 2025-07-16 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2db7742a-753b-3c57-828e-dd2862ffb56c | -13.02301 | -45.05768 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1036b890-ea4d-3df2-b54f-8acba383b073 | -10.56582 | -49.14109 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cfd48ee-0e72-324e-b531-f4b44b03bf7e | -12.03772 | -48.76729 | 2025-07-16 03:51:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2f414ee-0f30-39cd-ae48-55ad2e67b46a | -10.32333 | -49.92467 | 2025-07-16 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a5fc739-b556-330c-8fe0-6b90df7d6722 | -10.64763 | -44.48697 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c24954fb-dcf3-37e0-a65c-ec076391f218 | -12.07554 | -43.4763 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c317241a-8e4a-3759-8f3e-6ad0a64ca98a | -10.65558 | -49.47709 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36173418-1dce-358f-b492-b594036e0985 | -16.26298 | -46.91184 | 2025-07-16 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b17dae37-0d78-38b4-ac60-8c377df12077 | -10.64843 | -44.48243 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a18435e8-91f2-31f3-bb62-a1abc34f3c0b | -14.15878 | -42.83995 | 2025-07-16 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d411bbbb-f462-3bba-bc78-9a66bface8fa | -11.46984 | -47.32169 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5309d9c5-b3fa-3955-862e-6fd47f322107 | -12.57705 | -44.75048 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 433384a2-0754-34e1-8ddc-dcae7ba28185 | -9.85073 | -47.87704 | 2025-07-16 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db0ee66a-0418-380e-a2cd-866f6e97ca52 | -14.15793 | -42.84481 | 2025-07-16 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 31b55cde-ed57-30c1-8241-6a28601e2baa | -10.39026 | -49.75905 | 2025-07-16 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5c5859b9-14f7-3acb-adf1-f1413decdde9 | -12.47407 | -46.91976 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d31bf51c-4330-31f3-ab4b-7bad5cdc087c | -11.18684 | -48.62477 | 2025-07-16 03:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ddfbab4-5e30-3775-a83f-262466ca21bc | -14.15626 | -42.85442 | 2025-07-16 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d4f11f0-072c-3ffa-9d7e-f5151120d232 | -12.48548 | -46.92176 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a245c2b-c3dd-3986-ae2b-e787dfae75d9 | -11.94558 | -48.41562 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 51b397a7-9a62-3df9-b218-ca6c88424c94 | -12.07488 | -43.48 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0433d919-02f8-3bc3-b18f-0b619fb5265a | -12.47521 | -46.91973 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2ae5c98-e2ae-365a-bafc-69b900817a29 | -12.07007 | -43.48312 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 549709c9-2ef5-3694-a052-6ff6ac3c8eda | -10.3244 | -49.9193 | 2025-07-16 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab6e9c14-a847-3c84-b3b3-93ff2d8799af | -12.47461 | -46.92284 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77511f82-1653-3cc8-8ca6-de432fac6186 | -8.54254 | -47.85167 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca8c9393-d508-3148-825e-55171c60b113 | -12.4734 | -46.92905 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1aecfb8b-632f-395b-af7d-41e60ec3ebff | -12.73694 | -47.0708 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5654447f-232d-353d-a49d-fb9ed9e018a6 | -14.91896 | -46.96312 | 2025-07-16 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 96e7578e-d7c7-3e47-ac5b-85ae222b10ed | -11.58953 | -47.31639 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a412b452-3caf-3a08-b3a3-6f45e1d331bd | -10.38919 | -49.76434 | 2025-07-16 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b1d874e-da25-39e6-965b-30638de4e057 | -13.12806 | -43.48582 | 2025-07-16 03:51:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aed6aaa-cee7-313a-8ba2-09f1697e74f7 | -13.01687 | -45.06593 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2a5c8596-f216-3d6e-a16f-a72e8cffde09 | -12.99477 | -44.8837 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5949557-9498-36d7-b9b0-22626a5048a2 | -8.53115 | -47.85541 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15fc7a5b-3343-3096-90e7-6e3f33edd547 | -13.02289 | -45.06429 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e8c9034-1d29-36a0-8d59-b3eceb21a128 | -12.48367 | -46.93106 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a126470e-3449-3748-93f6-3e382c5e178e | -11.95067 | -48.42296 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1f790d7d-e51c-3d83-814a-fcde0f839e95 | -10.28351 | -47.6212 | 2025-07-16 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8135ebf3-a3f2-330e-ad78-8a9bf5f5f9f0 | -8.65067 | -47.75599 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caed5f51-3a00-3d27-a563-46f3b4bb801a | -12.9964 | -44.87485 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db953d50-a729-3126-8d00-1dd509904a95 | -14.15709 | -42.84962 | 2025-07-16 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 646108af-021f-33c0-b86f-1db7423893f3 | -11.58487 | -47.31169 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c84e1e23-b0c5-39e5-be04-3a3b263ebd4a | -13.15815 | -50.77614 | 2025-07-16 03:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40f6b1d3-44d2-3c76-b41b-485dc3ad5443 | -11.47585 | -47.31938 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 952099dd-da30-3daa-81c9-81c88a75a63c | -12.47219 | -46.93528 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea81c987-e4bc-327b-bee1-ce0d84ad06b6 | -11.94481 | -48.41959 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 15ca3086-02af-3b64-80f2-a510308aec0e | -12.59103 | -44.79943 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0184580b-b658-3f65-a146-97babf3f9861 | -12.02316 | -47.77755 | 2025-07-16 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 943f7559-e4cf-3403-a912-a6fb10ec44f4 | -14.60043 | -48.67028 | 2025-07-16 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cad20a81-9c62-30b5-a2d0-95fcc8227313 | -8.91145 | -47.34337 | 2025-07-16 03:51:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1f3b36d-8986-3480-8460-6a393dddd991 | -10.65152 | -49.48058 | 2025-07-16 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0587e74-78d4-3167-9269-ad92585b5fba | -10.38883 | -49.76109 | 2025-07-16 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7d35177-59b4-3f9b-a043-00e89a45c4ba | -12.5632 | -48.89039 | 2025-07-16 03:51:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 813ec91d-a1ee-31eb-8660-b46b0abe3890 | -11.95146 | -48.41902 | 2025-07-16 03:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 652b2043-0cb3-3db1-bf07-4f156ff4b563 | -12.47232 | -46.92911 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df46a300-d969-3006-b775-15fa9404b3e9 | -8.75626 | -46.59277 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f7ac384-daed-3555-8dca-ce2dd85be7ef | -12.56399 | -48.88647 | 2025-07-16 03:51:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1e11128-74e6-3e14-b332-15089a6621dd | -13.5429 | -44.50223 | 2025-07-16 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 788ce703-f5c9-328c-be44-1ba8da8a88f7 | -9.871 | -40.49734 | 2025-07-16 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e2c8e92-2408-3a01-a29d-b29b7c5d3ed5 | -10.89948 | -49.21179 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcbe6c84-0b25-30d3-b5fd-361145d2f282 | -13.02384 | -45.05313 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd4c6cfb-8da8-3cfc-a054-8b34fa9bd651 | -11.4752 | -47.32277 | 2025-07-16 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 248982ed-3ad4-3f4e-a499-abe78e78c234 | -12.47854 | -46.93006 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2774815c-ea3d-3cfa-98d9-84b6041ad14f | -14.60581 | -48.66705 | 2025-07-16 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2f02fd9-7560-3194-9b61-48055b2f7a54 | -10.89856 | -49.21645 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e172a146-c11f-32f5-a5da-0289c1142aa8 | -12.48488 | -46.92486 | 2025-07-16 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7329ac6a-1396-3432-9df1-d6524caf81f4 | -8.54175 | -47.85584 | 2025-07-16 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74220467-918f-3f3d-bdd3-b41699f8cd7a | -10.96084 | -49.25048 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f964b71b-c988-3701-a462-a1232bea5cfc | -10.27791 | -47.62019 | 2025-07-16 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d29c9594-db25-3f00-9223-5b001cd946c8 | -10.64478 | -44.48417 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409ac70e-2afb-31be-9951-2fb23a686f6d | -8.76101 | -46.59703 | 2025-07-16 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68716e26-fa96-3131-acdc-fab192e52be5 | -10.89241 | -49.21544 | 2025-07-16 03:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd13f2af-bf1a-39e5-ba82-f26588087d10 | -12.0714 | -43.47567 | 2025-07-16 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c8a4162-8789-3ad6-ac03-da8b5fa7bce1 | -11.45895 | -48.15856 | 2025-07-16 03:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c1497e3-b14e-34d8-81fb-bc22211e598a | -13.01321 | -45.06045 | 2025-07-16 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README12.md)
