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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad90880c-5fcd-3dfd-bf99-914e68d141be | -14.0217 | -48.75659 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5d6edbc-308e-3f0e-86c3-7b24e99d5851 | -13.35287 | -43.91293 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ca45743-1a22-3605-b7a8-e07b7200e1f2 | -13.50942 | -48.59713 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7348b9c9-6d8d-3317-ac07-9ff24166c7f2 | -13.73734 | -48.52246 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 958ec4c7-d576-3d03-bd67-2ee6d37b8ea6 | -11.94486 | -43.47508 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89c2320-a78a-3ff1-82b3-f19d37436b31 | -11.02934 | -45.43614 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f1aa864-31cf-337d-9ea5-199f1086ece2 | -8.5409 | -47.35441 | 2026-10-10 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 280a3a72-40be-34e1-adbd-49c7a99bc3d0 | -8.25044 | -46.43256 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 489db46e-5fc8-39cc-9170-2b9fe51a8b4d | -11.28359 | -45.19647 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85e7176e-b612-3d92-ad9e-a1b32df1fa0c | -6.43748 | -55.05907 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 15f5ca25-0b64-30bd-a19a-68893d68f048 | -11.85705 | -46.78609 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16f09460-64c9-370a-9029-7cba0d2cf09d | -11.95329 | -43.47577 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92f2aa66-71a5-3324-8c9e-ec048790b96f | -9.35245 | -46.5687 | 2026-10-10 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 866768c9-95b5-3889-b497-d93c91fb5860 | -8.65818 | -47.08782 | 2026-10-10 04:46:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 097fafc4-87ae-39c6-9d22-5950be65500a | -11.51761 | -48.72885 | 2026-10-10 04:46:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 349faf0e-3296-3138-a605-6e965eca9b21 | -7.23394 | -55.1633 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af36145d-9a1c-3855-88c2-abaf0959e442 | -6.80778 | -52.78398 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1157db8e-3659-3e9c-97ec-68a3581f7277 | -13.75524 | -48.51796 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f706eb7-249f-3d04-a38f-9bc19d6b5196 | -7.90627 | -54.71087 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10446fd0-c5af-38e7-b017-9ea716ae391e | -11.08159 | -44.10397 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98b4b5d3-945e-3112-a401-4b0dbb3af497 | -12.93131 | -47.43835 | 2026-10-10 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11863188-4a4f-32d5-ac8d-637ea4fad1a6 | -14.44476 | -48.11967 | 2026-10-10 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbc35fb7-17fb-3ce0-b25a-3838d4df3571 | -13.77178 | -48.12053 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e2e7e5d-2877-3f0a-823d-bacf8f0e519e | -12.22869 | -44.69462 | 2026-10-10 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecd7d5cb-5e4a-3e2a-9bda-df4e2cc1e846 | -6.37636 | -56.2333 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 328f9184-1d9a-3a97-bee3-115fd89cec77 | -7.08515 | -52.69051 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dfec3c8-7e1b-33c7-a533-c96ce8a83069 | -10.45924 | -47.84486 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7250a586-90a9-3a5b-a333-9656bde8bdb3 | -6.12911 | -53.05877 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d225bd67-83a2-3d62-b807-58c37eb5365e | -13.89576 | -43.91672 | 2026-10-10 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd084299-5048-3b47-8e00-4f2647bdd9f2 | -11.56275 | -43.70137 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b245b0f1-6c8e-3c12-b66b-96b15dc67133 | -12.04182 | -43.42715 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 266065d5-a8d6-31e5-a08a-d22394220af0 | -11.90155 | -46.56404 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5ad744d-4220-3184-8639-b9dab49cabb9 | -7.76863 | -46.39399 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1e51492-b9b9-3300-a097-e8f84b623898 | -7.00346 | -47.71561 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e40a346-5501-3855-a423-ca2ff05bde49 | -11.79205 | -46.72099 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70173a81-70e3-35a3-bd3e-1e263a63fd41 | -13.38083 | -43.89351 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a89bdcf-d1fe-330d-aa29-a4a5a4c49ced | -13.77685 | -48.13264 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cff41e5-0f6c-3e1a-9bd4-4547f3754808 | -11.9617 | -43.47654 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 018b7bf0-aab4-32c7-af84-8b93b1614c65 | -9.76412 | -53.8797 | 2026-10-10 04:46:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 987c3c0c-da75-3f99-8d18-af10e6b2f788 | -10.97572 | -45.19722 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7593541e-f05a-303d-b028-6131817e7687 | -6.45933 | -55.4951 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c57ba22-a8cc-3764-a6fd-8dd173c43505 | -13.17526 | -48.12426 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede31159-462b-39ab-9f1f-47b1595b9997 | -9.11752 | -45.81846 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c28a9cbd-7cf8-3221-93fb-57a20aab71bb | -11.60617 | -43.71955 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 131eb77a-04f1-312d-ab90-27460c3e56b1 | -8.26695 | -46.41622 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50d3f70f-d45e-3138-8d63-dd457f4784a7 | -13.37668 | -43.89289 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38a8c263-aab0-32a5-9938-bb1f6a777b9f | -15.37737 | -41.9169 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb13fd0f-39f7-3f9c-833c-28f7b97e842a | -7.40204 | -55.1512 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c95c4323-bb60-3caa-a0ff-6b8872aca607 | -12.0147 | -43.43337 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12258ed4-e568-30c0-bd1e-7219eeb9940f | -9.73527 | -57.36389 | 2026-10-10 04:46:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4d7f752-36cd-3810-86dc-46a82f26f7cb | -6.6501 | -55.32993 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5521ee8-7d10-38d1-aa0f-fea7b9b4c287 | -9.21334 | -51.87834 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db6e3026-1df6-3c47-a460-ab6bc070adb3 | -6.75173 | -52.94573 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0316fcff-e733-3fc9-bbcc-df9d798fc129 | -13.7481 | -40.83811 | 2026-10-10 04:46:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e11a836-381e-3bf2-b699-7a74fa4db154 | -7.19459 | -55.18645 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93fec851-4028-3306-90c7-44a3ef98aef7 | -7.01505 | -47.66394 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4ccc2830-909c-3f06-bf61-64dfd9e7f640 | -13.37565 | -43.90057 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d79e65fe-ea78-3dd4-b1be-f253005f2e11 | -11.59752 | -43.69164 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cd6cd25-a634-3c77-a855-13c244a6f6f0 | -8.23731 | -46.43132 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20b30022-4d22-3540-91cb-839507df4086 | -14.05083 | -44.81923 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45971821-87da-3bc5-a5bc-b9dd462d6610 | -6.32208 | -55.30329 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ba4b056-4e42-3571-9f2f-57d2ab84d511 | -12.04129 | -43.43103 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a9312db-2a57-3f03-bdd5-07a7b67eef37 | -13.64844 | -49.40634 | 2026-10-10 04:46:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75374db0-ae95-3248-bc28-086ba7fe1a72 | -6.45447 | -55.49432 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 382ac620-6dd9-3877-b52e-8db48323cda0 | -9.30751 | -47.38308 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 178d8738-2d35-3231-9430-a08f03bda0d8 | -19.082 | -48.14182 | 2026-10-10 04:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0713fd1-a1ca-31d4-a01b-1caf126ba30e | -16.64636 | -40.53865 | 2026-10-10 04:49:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| af438598-c422-3d52-8479-52590c5e081c | -19.0814 | -48.14595 | 2026-10-10 04:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89b44022-41d4-3a2f-9b3a-2397186c4429 | -16.00644 | -43.59778 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a59f8d49-29e6-365f-adbe-305cd513296c | -15.24043 | -48.56721 | 2026-10-10 04:49:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36a01c17-6112-3984-a254-c79a64e15379 | -16.76246 | -47.07223 | 2026-10-10 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7cc4e86-aa19-33de-aaab-e610459b1168 | -18.08729 | -42.25616 | 2026-10-10 04:49:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4231ee96-8dba-3125-a0d9-62646bbecd8e | -18.31963 | -42.38738 | 2026-10-10 04:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 82bae1a4-a22b-3bb2-a532-30768d477d80 | -18.91393 | -47.91492 | 2026-10-10 04:49:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3ae598b-e5f8-31ca-867c-5fa07bf0ebd0 | -14.56097 | -48.01934 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e69e96a-1f6d-3a70-a068-f493b226fbc4 | -16.50108 | -52.60532 | 2026-10-10 04:49:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ca19b7c-5766-315d-903b-30d41dfdecd7 | -15.5771 | -44.52798 | 2026-10-10 04:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e3c8085-396d-37c1-b0a0-d2d9b2336d04 | -14.71412 | -48.22633 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ce6d9ef-6ede-3b27-88f4-f43aee9157fa | -14.89608 | -47.22627 | 2026-10-10 04:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ebdc2e5-d8f0-3f54-a751-560d14a2afea | -14.89549 | -47.23028 | 2026-10-10 04:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb6c89ec-6718-36d0-b078-d9e84622d6a6 | -17.45823 | -45.08007 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6733f04-074b-3d47-93f6-2199e40049ae | -17.46585 | -45.08511 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6949bd39-d579-3081-a52a-acb85e2ef66b | -18.785 | -46.46745 | 2026-10-10 04:49:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89f3ff39-aca0-38d7-8c22-ea3cb8e6aa36 | -19.6479 | -45.92883 | 2026-10-10 04:49:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2819043c-42c6-3e28-884b-1b564df99f06 | -16.75825 | -47.07592 | 2026-10-10 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a099a4c1-19fd-3781-a1a0-ec9ec2de754e | -15.08912 | -48.32637 | 2026-10-10 04:49:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f3a1eff-b793-33c5-85c3-ece4f12748c5 | -17.95372 | -42.49599 | 2026-10-10 04:49:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3d229ce3-2453-3ee5-b6e4-72c1b44ad3e5 | -16.59744 | -46.74893 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ba2dea1-052e-317c-8234-600eaed32171 | -17.09816 | -48.6335 | 2026-10-10 04:49:00 | NPP-375D | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26f8377b-d555-30d5-8d3e-1ffc05e83679 | -17.45469 | -45.07558 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fd3b6da-e643-3bfd-9895-45cbc25259ee | -17.45924 | -45.07251 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| befc41b7-eb03-3337-b3fc-4d95b9f8bfcb | -14.55757 | -48.01877 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd9dbe56-ac30-33e9-b065-77495faec87a | -14.70312 | -53.07893 | 2026-10-10 04:49:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6739190-ed97-3729-9729-063c7ae59775 | -17.34717 | -42.67601 | 2026-10-10 04:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b6a5a14-ad35-31a4-bb32-5a9a1f53e841 | -14.71693 | -48.2307 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4946f538-43ed-32c2-af2b-107432a0d3cb | -17.97457 | -44.34076 | 2026-10-10 04:49:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15db578b-4494-34f9-9ebc-b24f197c95f4 | -14.55699 | -48.02256 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e35a27b1-4cb7-3674-94e3-9a9f9ed33571 | -17.98644 | -47.21418 | 2026-10-10 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 929e4951-2df0-3f87-bdbd-6762df5fab27 | -16.60109 | -46.74952 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8d8b2d-54d2-3fb2-a6cb-e1967a8e7298 | -16.57167 | -46.79851 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README88.md)
