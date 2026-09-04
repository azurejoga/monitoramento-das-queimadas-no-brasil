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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf011b3-9136-3e87-8a2e-8fa25dea366a | -7.08239 | -56.51083 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2ae1ffc-3dc9-3f3f-a80c-b54aa891e9c3 | -6.52767 | -59.94001 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35fdf796-302d-38b7-a7c9-9cf759a67654 | -7.55143 | -61.34316 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2d608bc0-688b-3576-8887-283a0ffa046d | -4.14644 | -60.69653 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfafa46f-a559-3b81-a7c3-39832003639a | -4.81435 | -62.78225 | 2026-09-04 05:59:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03b756a8-548e-392d-9010-37df9134f559 | -3.27743 | -60.17027 | 2026-09-04 05:59:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4ee7a34-d3bc-35c0-8ed6-bf9c2ae8ddbc | -4.97076 | -55.85692 | 2026-09-04 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58ce301d-d951-3065-a7b0-1e3a33eb1d26 | -3.01786 | -61.48231 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e049438-405a-3d52-9751-4447a55daa9b | -7.79491 | -62.34509 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c9a721b-e13e-397c-b04b-c1d70caab46b | -3.34172 | -59.45657 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1970fc0-784f-38b5-9f06-a6b8c20f11ae | -5.76914 | -59.1716 | 2026-09-04 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b124c572-a6d2-37b8-9058-869892b09ddd | -7.46905 | -63.74815 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d1bbea-10a1-381a-b89e-f79144887864 | -3.21343 | -61.15378 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c554cd0b-f7d9-3937-9f12-28764cfebe46 | -3.02502 | -61.48861 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fcbadc4-4046-3770-a52a-11b24a28dda3 | -6.99408 | -62.99124 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbbbefcb-15ff-3bfe-b85e-c3bcb31a2e18 | -6.68839 | -59.98275 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fffc61c2-ead1-3a89-9b55-67315b2b8314 | -6.31656 | -56.04642 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 211165e8-05ef-3f0d-8b28-bd3eaa4434d4 | -6.1531 | -59.94285 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 383ebf2e-87f5-3933-b0a2-02d862440526 | -3.61136 | -60.56457 | 2026-09-04 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec21e7eb-88ab-3812-bbb2-70fae1302361 | -7.08125 | -56.5191 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e826ab2-4cbb-3637-bc6c-07b86fa93f97 | -7.55884 | -61.3524 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1ac330c4-3582-3e4f-ac1a-c6c2ca172e9e | -6.59916 | -59.11503 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd7501a9-a48e-3ba1-a819-e10779ff9016 | -6.67859 | -59.95198 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ba8d40e-c78e-3d14-8c69-36c8aece6732 | -6.68444 | -59.97731 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 48ca4761-a60f-3c36-a95b-fa453aaf1488 | -3.77718 | -61.76218 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a02f5fd-6e84-3389-b7eb-44b80e80e906 | -7.08769 | -56.51601 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fb9364e-44bf-302d-8c5d-9205f608132e | -7.67429 | -62.54655 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd06383b-ae02-3ab2-8355-67b78893ab61 | -3.13761 | -61.21482 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25972a04-8023-3c00-9b92-302e8e568221 | -7.47273 | -63.7487 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95b7309d-be13-333a-9ad7-ad16a44aec9d | -7.01008 | -62.98884 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0539e16c-85e7-3728-a4c4-cc63f0207599 | -3.75858 | -61.75753 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ca0eba6-f6a9-312d-ad96-bf9d557fa336 | -7.08827 | -56.51186 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 439ca79b-7f25-36d6-99e7-b1391387ccaf | -7.24166 | -59.52529 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 639185d7-005d-37eb-9825-94d75db44474 | -6.67911 | -59.98138 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08413a41-7439-3d53-be4f-5da772b2b90c | -6.68048 | -59.97183 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6813c06-d36c-318b-b315-dddd83f420cd | -7.55943 | -61.34836 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 284e04dd-00d7-3a24-981b-c373fabc50bf | -6.48485 | -61.71609 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2063fa1-ca95-3970-b54f-b153e0723182 | -4.24083 | -62.23796 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82fea5e-5597-383b-b39e-dd54a371f856 | -6.64343 | -59.44721 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e28c4600-ec70-39ed-813d-f663b72fe997 | -3.47253 | -58.43125 | 2026-09-04 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1c91bae-46e6-3824-894c-0e31b673270b | -6.53302 | -59.93596 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 772a3158-b871-3672-88d7-f9846d1272e3 | -3.07828 | -61.08979 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 221d5292-b8ff-39de-93c7-dbc9bf706fde | -6.68013 | -58.76474 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c533cf9-8c54-368e-8f0a-5de2aaf9d17f | -6.6779 | -59.95677 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac76a54e-77db-392b-bd44-97dd02112240 | -6.6977 | -59.98396 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 026b6cf5-ecd8-3d34-9ef7-180aa41f4541 | -8.11055 | -54.79396 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 29ba4178-f0b5-3286-8be9-438748ac9baa | -6.686 | -59.93347 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95ac1c2b-8466-3729-9db3-ff83e47f2b6b | -6.14916 | -59.93751 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3d6f4c3-4c03-3d87-bc13-41dd53715813 | -7.01772 | -62.99 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6388b04e-2d05-31c4-9fc8-671aef163c87 | -7.42611 | -61.72805 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 086d422c-5c10-317a-949e-82ee4d187a7b | -7.55201 | -61.33911 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35efcc58-59f8-3dc1-8176-1c71c07eb6b2 | -5.56495 | -60.17063 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95ab5c67-ce16-35cd-8dc6-0568426d88d6 | -3.77829 | -61.76052 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74152f71-873f-38f3-86c3-e8fcce881ba4 | -6.6753 | -59.94178 | 2026-09-04 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c216c35-7c91-3515-96c2-0c8bad005897 | -7.7826 | -63.38401 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53c3f6bf-9e09-3459-8535-48e7ac2519d4 | -3.29046 | -57.88221 | 2026-09-04 05:59:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34b68125-66c6-326a-8a23-13887cc6337f | -6.96123 | -59.74434 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e1f463-d5f8-3dca-ad84-6d89688a04ea | -7.24453 | -59.52686 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b13d9b4-4ec6-3cc3-b2c8-ec2d40df25fd | -6.68375 | -59.98208 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1b826c8b-8849-3e92-a4bd-87caafa626d9 | -6.68908 | -59.97799 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| b348ca00-2a76-3ded-b534-3a3a275aa201 | -3.77793 | -61.75717 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75eb79cd-1eab-3898-96bc-cadc7b9f237d | -3.36799 | -59.49847 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3bff7b9-0ff6-382e-8c64-bc27b1433bb7 | -6.67254 | -59.96106 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afb85386-1f07-3592-a921-7ec3719fbb70 | -6.70173 | -62.86411 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19da8f30-c0f3-37e2-a0f7-829b44a92620 | -6.70244 | -62.85938 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f652afe6-7601-3707-92c0-500f598ee90e | -6.11804 | -59.95716 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4060023-5c6a-38ef-a8dc-29796a71dde1 | -4.47725 | -55.08077 | 2026-09-04 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6904f742-d129-3935-9cf9-b84a5c5c5c0d | -6.15379 | -59.93808 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba5395e3-7312-3aa9-899b-5b9543da95dd | -7.56059 | -61.34032 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 884a8f2a-00f9-32d3-a66b-edcfec2fe916 | -3.75541 | -61.75193 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec929a05-9106-3512-ac01-9412cadacd84 | -6.53042 | -59.93818 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db384261-1cd9-33fc-a7be-a53a9b03ebc1 | -6.69444 | -59.97377 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5ea61679-40be-389a-8772-68afe56fa0cb | -6.67461 | -59.94662 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f846b71-6fbb-31a3-b99f-da648773ef01 | -7.01843 | -62.9853 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e0bce0-5b5a-3621-9cd0-e31576d46aec | -8.10747 | -54.79338 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e89a18af-25f7-3538-8768-01ffe3cdf4dd | -6.77962 | -58.95591 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf00446a-a443-3f67-8873-00c3d0593e0e | -8.11278 | -54.77647 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 568d73e5-5f4b-37d9-b23b-cddd3230d567 | -6.67927 | -59.94723 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce8d8f7e-94e7-3ae4-b1fa-1a1de493422d | -5.55979 | -60.17445 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 980828ea-5c21-3558-9bfa-0e57d60935ab | -7.03133 | -62.97762 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e84bdd25-b47f-3033-a7e9-ea2079997cc7 | -7.61711 | -57.61957 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80748c55-f288-31d3-a85e-e7e6c70ec323 | -7.4715 | -63.74631 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2268c6b-6590-3237-9392-37cccbea1336 | -3.75464 | -61.75693 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fddb9474-a0e9-3459-94cc-119c8cabe8bf | -3.02105 | -61.48799 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f5d39d-f038-370f-9817-162886f09d99 | -3.67843 | -53.75401 | 2026-09-04 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 162ab3d7-244f-3b6c-943d-80e56e3fa768 | -6.76726 | -59.43499 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6225ce7-027c-3a8d-8b15-d943c6105a97 | -3.34243 | -59.45193 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 531de614-541e-33c3-9825-8352637069ab | -6.7094 | -62.86527 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd0963f-5363-3b85-8d5a-2549fc728467 | -3.07474 | -61.08564 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a55f9c8-581f-3142-a6b2-1a9ffd90af8e | -3.39533 | -61.31816 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abdc2a7b-d9ff-3fa5-a09c-7bbf2cd0f047 | -6.6696 | -59.9827 | 2026-09-04 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 55eea7fb-1776-3228-91d7-39e301fdbd77 | -8.5916 | -67.1788 | 2026-09-04 06:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 13822a31-6043-3e09-8252-89f3b1f79990 | -6.7065 | -59.9813 | 2026-09-04 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 78898155-35b3-31c9-93e4-53efc850361c | -6.6697 | -59.9635 | 2026-09-04 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 1d35ebf4-cba5-38fc-adfb-81c2c1925457 | -6.6882 | -59.9628 | 2026-09-04 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2b2adc25-54f1-3a9d-87b5-578b65d4e2de | -6.6881 | -59.982 | 2026-09-04 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 33d12d14-b862-38ea-9434-198faf9b997c | -8.6101 | -67.1783 | 2026-09-04 06:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2ae908d1-447b-369e-8c71-332822d85c98 | -9.20224 | -65.91254 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbeab50b-be6b-3e50-b635-3cd3ec244908 | -8.71276 | -62.94589 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae31b7fe-30a6-335d-9be6-9aa1e1bceb93 | -9.17282 | -67.34859 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
