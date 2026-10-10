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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc9f528b-8c85-3aad-a2b8-8c881ed5c791 | -7.91523 | -54.71252 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 915b21c2-e1f6-33be-8293-7ec6b9446275 | -9.26839 | -47.42475 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f0eef66-6800-3997-a01c-745d336ec6e0 | -12.02441 | -43.48539 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 966efba0-c34c-33fd-8d94-f617df1a923b | -13.22692 | -54.15228 | 2026-10-10 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4053b5a-dbe9-3853-8636-15d79a53d564 | -7.91655 | -54.73145 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f68cc137-2209-30f1-8ef2-682349310f1e | -7.23106 | -55.15247 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ab3b677-b666-36f1-84c6-4b8f99a22851 | -11.08732 | -43.99169 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 036d3b99-c371-333b-af70-ef8e7c36a07e | -5.86465 | -55.69808 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183b431f-1766-3b9d-9305-df1b5ba94e14 | -7.95359 | -54.76442 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c3545c8-dc18-3a2b-be80-ee57bfdb64e7 | -12.38098 | -46.60507 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83159c53-b594-3418-a427-6bf0ebc4cefa | -7.04222 | -47.66467 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f85f731d-aab2-3aac-b87d-8cab4b09057d | -15.38223 | -41.91771 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e7c3423-a966-329d-a961-2d3b5b64b660 | -7.03279 | -47.65961 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5643bd7a-d29e-3b0d-8fa6-bc73fb7a4503 | -9.28905 | -47.39114 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4073647f-321c-33bc-83a8-8a71156dac46 | -11.12581 | -43.25168 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c94864ee-fc89-356a-b4da-40b4d133f070 | -7.23831 | -56.41918 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11fe12e5-d23e-3dbe-942d-7281455d81dd | -12.29453 | -47.03921 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8b10e9d-c521-324e-8527-f043a9f7ce0c | -6.24215 | -53.31046 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ecb9ff5-13bc-39b9-b4c5-d361c6c077bb | -11.82641 | -43.58919 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23dddece-0bd4-3ced-925d-c93f7f6ef77a | -7.50252 | -55.0028 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fa5a37ca-1828-3a66-8083-6fcc4e26cb8e | -7.01011 | -47.71666 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21ccda79-a070-32ee-8f8a-c66e55a6d8b3 | -13.36372 | -43.89491 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5d96b9f-a7bd-31e3-a5de-c7ab809aa423 | -8.35972 | -48.1459 | 2026-10-10 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4665de3b-de08-3f77-9851-2a76422cb6c9 | -15.10549 | -43.63593 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2001881d-fa1a-3e5c-b39c-40a2cbaf286b | -13.1747 | -48.12792 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9efc1e5-486a-30ff-b488-7e9a885036ef | -13.3715 | -43.89994 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c90d351d-6baf-3e54-9ea3-3539e3b85cc0 | -11.97164 | -43.46637 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9547d53-7222-36e0-929e-98f1b4bed6e4 | -11.84769 | -43.52707 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c0a0fce-4232-3a8d-b40b-4b0af618e34e | -7.01892 | -47.66099 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| bf2c7ff0-7b81-3e46-b1f9-e9939b26151a | -13.25643 | -42.25452 | 2026-10-10 04:46:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 990d88fc-e147-376b-9a28-0ba13437e69e | -13.36838 | -43.89167 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd15b85c-f74c-3560-aa1c-c03c60e609b7 | -13.36423 | -43.89107 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f839772-999c-395b-8ea2-d1e494ae06af | -9.75547 | -44.78186 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54e0f1d4-91fc-32da-8286-59b56da11aaa | -7.20061 | -55.15179 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ac97a8d-4c08-37ff-92d6-c67fa09383be | -8.2778 | -46.41401 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fcf1d6e7-e68d-3b7b-9ae2-6e4ab473f69a | -9.75998 | -53.87908 | 2026-10-10 04:46:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb9fa063-b360-3bf1-9ba8-34bf79865358 | -7.57005 | -45.64676 | 2026-10-10 04:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74844cdf-5cbe-3d26-92fa-9f6c08ef1bca | -7.26731 | -57.12373 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 653cd6a4-4c89-3e8f-9b5e-30e78327c6fe | -13.25385 | -44.01133 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc017b87-20a0-3478-9320-e05cb0a9832f | -6.65401 | -55.33586 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc048ebe-7994-3bb7-a669-e714a0bf2b89 | -12.04336 | -43.4473 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3ae99de-4d78-3451-b942-f388a88bfe6c | -7.03834 | -47.66763 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc872443-edcb-3201-94fe-791bc1ea1bf0 | -13.35715 | -43.90308 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eb385d4-c2ca-33b6-b990-8fc9298e28d6 | -11.05274 | -49.56228 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed196a59-554b-3bdb-8062-dd1c42f88772 | -8.9266 | -45.41803 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bb9ff36-4860-3755-baed-fb62366b96d4 | -12.37978 | -46.61306 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 315683bf-b96b-374a-90d7-2b0ca0bed0c3 | -7.22021 | -55.14991 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4f5e352-31f6-3c0e-90fd-a73297c5a7c6 | -11.20325 | -45.29592 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6fea833-26c4-37bc-b4d5-7047ddc13f33 | -6.13043 | -53.10126 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 612805f6-2d1a-372c-b0b6-2fd4fe21b439 | -14.1126 | -49.87046 | 2026-10-10 04:46:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6ef7aeb-5960-374b-a1c6-841d897a0bff | -13.69345 | -49.07788 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf7e443c-d9a9-3b94-ba53-49283c124337 | -7.24004 | -55.21031 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1aa18c1-d704-3bc4-b2bb-1087d944d3d6 | -7.00013 | -47.71509 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82939463-43ab-3e25-9e3e-d472ad46a318 | -8.89912 | -51.71038 | 2026-10-10 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c76d7d-9bae-33c4-be6c-4ab1cc0aefcb | -6.3723 | -56.22641 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b141723d-5548-30e5-8304-fcdc030efdb5 | -7.02946 | -47.65908 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08b8581d-0307-3685-bb46-d67ea809bb03 | -8.34459 | -45.01084 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e938211c-0419-38ca-a4c3-d1f550d60343 | -12.44949 | -51.39406 | 2026-10-10 04:46:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6aa8f585-8a4b-3d82-b888-af1c8b4d317b | -9.73784 | -44.79761 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b103a205-1929-3f26-b171-a0ca4e2d695f | -7.08773 | -52.67515 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1401c763-8495-3249-9f8d-f2ab1236e3b5 | -5.24127 | -60.19506 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94edcb28-d63d-3d1c-9334-a595800093c6 | -6.44822 | -55.28004 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 930ab907-e68a-3edb-8b91-48da61780cf6 | -8.21102 | -46.5328 | 2026-10-10 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 778ac422-5bd3-35af-af94-f7a0fdd71c22 | -13.73455 | -48.51829 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b4011ed-4464-347c-a296-bb551f18a84b | -9.89157 | -50.49096 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33334346-8f7e-3631-94ee-b55fc9350f11 | -13.3555 | -43.92492 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d227aecb-ca08-34be-ab1d-61333f46e1ed | -11.08265 | -44.1069 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb459a38-5b58-3ff4-9540-00d7efe82c40 | -12.35809 | -46.58941 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaae75f5-9254-3167-9b0a-25a103340586 | -11.77178 | -46.80902 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40a68697-5e55-32a2-9f1e-8b5fd8363386 | -12.15552 | -55.42788 | 2026-10-10 04:46:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08f89b05-7717-381a-ab12-cd20f815b172 | -9.30024 | -47.38559 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c4af99-83d0-3e3b-a68f-3fbedcc96fe7 | -9.1134 | -45.82181 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d85d3c22-852d-3225-ac43-866eea079fe8 | -8.92955 | -45.42267 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6656273c-8ac5-38d1-aab7-5858a494db11 | -6.98848 | -47.70254 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13c6ae51-ac85-3ae9-a120-a8f56a55f875 | -13.51109 | -48.60844 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe3085ff-31f9-3147-a989-91914479d6db | -7.55113 | -48.02034 | 2026-10-10 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15479bb5-2d6b-38dd-b93f-8bb236c2342a | -7.52714 | -45.31853 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 847095a6-5fc2-3571-b0cf-7a07d1c878bd | -7.21466 | -55.15418 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92aa3dac-de9a-373d-af72-270069c8d600 | -11.99996 | -43.44695 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd8e80a5-e66d-34ec-9065-df8297adc45f | -6.99791 | -47.70761 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53951dc6-5aa9-3c4d-b49b-574ded272c32 | -6.46117 | -55.48466 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 68d6d34a-e759-3f72-9469-a990d2a383be | -15.37543 | -41.9327 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2fbacfd8-4536-3b41-9f06-04a3318c4465 | -8.87251 | -50.18774 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27e203a6-a7f0-36b5-8381-391a5bc79299 | -7.9263 | -54.72861 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbbcd743-9fc5-3269-849c-3bc80ee68b03 | -6.46957 | -55.0699 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dc6839bf-1625-380a-ac55-61569e01071c | -11.20195 | -49.93608 | 2026-10-10 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d371e4c7-890f-3805-84bf-2f1d474572c5 | -8.98479 | -47.54727 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cb9163e-7b16-3689-a167-0c7ede163995 | -7.91892 | -54.71786 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26504e4c-554e-3d9d-82a5-2eb8e9160b6e | -12.37334 | -46.608 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d49ceda-4747-30d4-b3e1-51adc95096da | -6.49164 | -55.31122 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9b6999e-b501-3782-bf6b-11e31ae4b021 | -11.02004 | -49.09247 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102bba87-5bbe-3678-bd08-1fc77d186074 | -6.25008 | -52.86069 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f7b1698-75c5-38f6-aee5-e734051ce1c3 | -5.9695 | -55.38723 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48f1d463-d21e-3c47-995e-c244bd019a9b | -6.36876 | -55.174 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 556c14ae-8038-3fe5-b11e-cacd39f5f6b9 | -6.4848 | -53.61056 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c490d91-aa21-355b-860b-a691d076ab8a | -10.88456 | -44.79093 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92289011-beed-37a5-9e04-fce09d6ae3c1 | -8.97881 | -45.12398 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f5a4daf-76c4-385c-b840-f6251b8e94d0 | -6.80455 | -59.31931 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab477129-b1bc-31ee-8255-f9cf7acadf28 | -11.59902 | -43.74083 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e83a348d-266d-305b-8f96-c139448d287f | -7.21499 | -55.06903 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README75.md)
