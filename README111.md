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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b315e1b-5feb-359f-95b7-f9ab0df53544 | -8.92587 | -61.48016 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16a57ad9-27a2-3034-957f-0367af35909e | -3.0759 | -54.39014 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7404b626-152b-3466-a267-792c877118e9 | -8.50938 | -63.3643 | 2026-09-23 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1e72ef8-b5c0-3896-b8ea-20cc5b2dcb5d | -3.24124 | -53.95419 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff8b9fc8-0b24-335d-a71a-d7df621ea80e | -9.58535 | -46.53368 | 2026-09-23 05:23:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cea4f4c0-b931-3b0d-a5f1-d353a3d1c3b0 | -12.36567 | -50.15775 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d02260-2572-3cbb-a02c-3bf94c5d483f | -10.29873 | -50.50347 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e39a5b1b-c569-3467-9211-6d561854cb2b | -11.64206 | -50.9766 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa8a0541-2bc2-3e56-8fef-800d609508f5 | -3.79708 | -57.2571 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0994ec-bf98-3b4b-b3b2-59d7d75b31fa | -3.82256 | -58.88094 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 677778b8-abbd-3102-a849-011d4cb81485 | -3.85312 | -58.66691 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| addd7ef8-bfb0-36f8-b471-eeb5d9403232 | -9.56109 | -65.98592 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41fc1d98-0c70-390b-9206-265b2371d504 | -8.59384 | -62.49924 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d624c45-af12-3ccd-831d-44406e9aa18f | -7.87635 | -61.18266 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfb7e322-04ae-3e44-bf09-229ed7a52d90 | -11.78006 | -50.98738 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bd91b5d-fff6-315a-ba4d-3e79b22fd6d2 | -9.94313 | -48.47443 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce4f2f70-f50f-3349-a8cc-d799a455c0c7 | -7.53629 | -61.5028 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3358ed-cea3-3254-8e7b-61a152b4a156 | -3.4641 | -59.551 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7551aac-5bd9-327a-9ff0-afaf352993dd | -9.30251 | -60.31214 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a06912df-7cfc-37cf-9ccd-3fa0b923ce76 | -3.14669 | -60.63122 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8820bea1-9e7c-39f2-a509-14e972855059 | -3.45821 | -57.91921 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4211a4c9-f89c-31c1-abb6-74544246175a | -11.11477 | -51.05972 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fb7da8e-5fcb-3709-bcdb-8ccb8ff61f36 | -9.70303 | -58.14039 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b664a958-4fff-34a2-81e1-77edbcdea0ff | -2.98723 | -60.94938 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a32af64-c5e5-3ab6-9ecb-81ff7725a9b8 | -3.95867 | -59.34928 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ca5f0d-beb5-3ece-8aa6-7ddfec2dc359 | -4.56347 | -55.05991 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f646aa-eedb-3e6f-8e17-fbb456231b5e | -3.38213 | -61.28895 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5563f24f-9649-3ddb-bfb9-1933e7dfaadc | -3.74625 | -58.86853 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d4472c-c60f-336e-9103-9de45df060d5 | -2.547 | -49.10463 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfaea8a9-1728-3e4d-8e8e-be228d7a511c | -4.37362 | -55.27224 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09e3b703-ae68-3151-8bd4-fec56e3662c5 | -3.68121 | -60.59778 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ede74172-1ee9-3142-a63d-66f37a324ae9 | -3.07612 | -61.21064 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1518bddb-ca74-3d4b-be81-530536178d15 | -2.55378 | -57.32183 | 2026-09-23 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e38a79f0-30f2-3de9-b196-896fde144936 | -5.12127 | -48.7958 | 2026-09-23 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da3eee01-2ca9-34f4-87b6-8c26b28dbb87 | -2.85653 | -57.79279 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecca68fd-9e2f-369a-9303-2d8541fb4360 | -3.68196 | -60.57105 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a5e4399-81e2-3469-96c1-cab5cb8daab8 | -3.82037 | -58.89473 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8da2e69-0e11-32bc-8912-4bd13ce160ea | -3.58198 | -59.06914 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859e10f8-1fe0-33ca-b700-fee80a9bd20a | -6.12823 | -52.76194 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20542b5e-2922-3905-a6ec-190e1bc41d2d | -3.141 | -61.39315 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58936b61-94ff-3d7b-a252-4eba85895f91 | -3.75868 | -59.41093 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ad11933-520e-3249-b1a4-af8ac48a4665 | -3.43983 | -60.41862 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 699b329f-8fbe-39e8-850a-9088933e053f | -9.09707 | -61.44027 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cf677c8-5651-3bc1-8627-7a2326a18639 | -4.52728 | -54.97285 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bef4af10-af62-3133-b1ce-4d99323b0be9 | -3.68285 | -60.60956 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b88dc9ca-fe60-3eb2-962c-bcad34848b63 | -3.43299 | -60.41752 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 526cff3d-bd0a-3050-b55c-4590e799a3ee | 1.7721 | -60.23552 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4fc61a43-d4b6-3043-813b-5c49bf27e8e5 | -1.30119 | -55.8379 | 2026-09-23 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d689a08-502a-31c5-99c4-adc47a1f1938 | -3.82231 | -52.4007 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f09c32aa-8316-3dd2-8fe2-67d5c9538ed6 | -10.24995 | -49.96929 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2f1c722-72d1-3d7f-9d5e-fddb27b952fc | -10.29371 | -50.49918 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8067f392-f779-3cc6-b2f7-9e8caf26e266 | -7.87575 | -61.18632 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb350e85-e72b-339e-88cd-c871146f3fbf | -2.55272 | -58.01703 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08b0b135-021e-3a82-96ba-a18b551a971d | -10.28268 | -50.5343 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2222468c-6080-30a1-b307-5917d5838126 | -8.91725 | -61.49012 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31d6ebf9-776f-3c9e-a53b-4246578d35d8 | -3.36855 | -58.0787 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccf12624-9a1a-3889-8906-928dde2351aa | -9.63216 | -61.81628 | 2026-09-23 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e811b8b-ea78-3fa0-b7af-014662c9f74d | -3.34386 | -58.1701 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e34b8337-4c3f-3854-a741-9c1fd4d3525e | -2.97393 | -57.17411 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698598e6-d95b-3f3d-a5c8-c69bbcf17976 | -3.6842 | -60.57908 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c12baf3e-86c8-3884-999e-a36ba621e5db | -9.04916 | -61.00006 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1082d5b9-38c2-35fe-8092-478a866a92de | -3.07554 | -59.13455 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c3ae556-2a4f-3e83-bb65-37f0dd167c60 | -3.88303 | -51.95807 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 230822f1-c9ea-37ac-b931-257e10a5b64c | -3.45641 | -60.25137 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 730a0d1f-2c7b-3e59-af1f-930c164e52ee | -11.63193 | -50.94987 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 502282c3-7cc8-31f8-8e90-92dde5de895b | -3.00472 | -54.17983 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c68f8683-4f89-3927-ac20-09dff268e027 | -8.23559 | -62.82906 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20944efd-be40-39e0-b40c-29a62dd1c205 | -10.25911 | -49.96654 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32c9f5c8-4783-3e9f-9f71-03263efd2381 | -6.1276 | -52.76614 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1094266-2345-34af-a2bd-58637dfb8ca1 | -9.9645 | -50.2631 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1780d08e-43d4-3f4b-940d-7c7fb65f6371 | -5.88603 | -53.62192 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a619825c-a6bb-3716-9fcc-d1f4b4c34cfe | -10.30328 | -50.50454 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d6b5a31a-fc26-3db6-9a75-c6ef36bd52df | -3.22391 | -61.05699 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1e3b4e5-ae63-37cf-9790-cdbd7e8f28bc | -5.11503 | -48.79893 | 2026-09-23 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88613757-864c-3718-8355-54abe8d7dcbb | -9.29724 | -60.53431 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5af27672-da4f-3a1e-a406-58c2d9ba11dd | -3.6939 | -58.92038 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a03e82d3-974b-3109-ab71-e6a48a6194ef | -3.69854 | -59.19056 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ce00845-0904-3940-9597-b15c54f94d6e | -3.62967 | -58.76891 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc8a29d2-617b-3d58-9629-1dbcbd50c7d6 | -3.4902 | -59.60208 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c673dff2-955f-3ed5-81c7-4f46b28d30a7 | -10.27816 | -50.5265 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cb468f4-47e2-3f3a-abcf-92746ed38200 | -2.60235 | -59.7581 | 2026-09-23 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e28f3653-6855-3939-934e-d211f0613ecd | -3.20393 | -50.91808 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52b5b21-c154-3094-bf6a-74d22d2d28cd | -3.65954 | -54.26665 | 2026-09-23 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ff0c7d1-e7d7-32d4-b5bd-eb68222aa2f5 | -4.14694 | -63.41748 | 2026-09-23 05:23:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eab24a79-a889-3331-8138-28de06ffdfbd | -1.82478 | -55.71317 | 2026-09-23 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76c74d3-a7da-3a71-944b-739fdf09248c | -9.0855 | -61.0097 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 08f135a1-9a46-3502-87df-7cc7dead108a | -3.34226 | -58.20161 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dea284c-9807-3b26-9749-38f6a54d067d | -3.22565 | -53.95185 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e42e39e9-4b44-3ea1-9e18-c38b7fdad1b9 | -6.04233 | -53.27477 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb3dff1d-f20b-3e60-bce5-37994d7dca29 | -9.16086 | -61.19613 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e63c1876-cb06-3c3b-b20e-c632709785a8 | -3.80453 | -52.36567 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc789468-6567-36d6-9024-60d8836f3308 | -4.2202 | -48.61821 | 2026-09-23 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea46690c-8ee9-396c-9d46-36f2ca1a7aa6 | -11.63868 | -50.94016 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9af985f4-fefb-3bb3-a3b3-5a300f0f35ae | -3.22104 | -61.05251 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96f28870-a810-37c3-b0d1-370f49dacf73 | -3.13091 | -57.69006 | 2026-09-23 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 378d2f1a-f2e2-3016-971e-87ff27be823b | -2.14875 | -59.23587 | 2026-09-23 05:23:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b82f3c8b-c26b-3460-9191-a960197c59ea | -10.30599 | -50.48995 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b17d7dc-4c4d-3cee-a4e7-bd3d01111103 | -3.22475 | -46.94122 | 2026-09-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 56ba4d30-ede5-391a-9502-dd679756200f | -10.28314 | -50.53077 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 66c3d5da-0ef8-3c80-889e-3012f23f5284 | -3.64191 | -60.4921 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README112.md)
