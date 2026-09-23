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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8291e359-6e6c-3c3f-bdaf-50afde82bf13 | -10.9154 | -53.9524 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8620818-1056-385a-8253-5446adb8827f | -4.1297 | -54.248699 | 2026-09-23 00:58:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab5d705c-2253-3cbb-a372-88b0e8d2a93f | -2.5626 | -57.495602 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07a731fc-14d7-3b24-a314-16c933e0285c | -3.9554 | -59.338699 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c03a34b6-44fd-392f-9e68-d3b16941866a | -7.5672 | -57.681801 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9826e941-dd48-3ce2-852e-a4f6f9e0ba05 | -3.2581 | -53.956799 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af74f5d9-7138-3882-b279-15644daf79fd | -6.6147 | -59.979 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 176e9ae0-0639-3925-9758-52bb81688c4c | -8.918 | -61.4799 | 2026-09-23 00:58:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7efd80b4-86f8-3d09-afbe-4eecad5094f6 | -3.4734 | -59.567902 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c454732f-3f80-3bc4-975f-ee8e98d08503 | -8.4832 | -57.605202 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 789d2e0f-ada7-34ec-89be-817002903709 | -10.6036 | -53.984699 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b97a44a9-2b32-33dd-8340-2e2c4a48fd21 | -12.4175 | -46.9776 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6c76d2f-f92f-3bce-b959-575ff11e0157 | -6.3576 | -58.2892 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25560315-6444-3b55-b39e-f01ec9cf6c79 | -3.3946 | -61.044102 | 2026-09-23 00:58:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25bcf870-65ab-3223-a3bc-2ba2cb886fe1 | -8.307 | -54.761902 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a87b4e5-4dcc-343a-9374-0e1ed80c9038 | -2.2825 | -56.673801 | 2026-09-23 00:58:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 337debe5-c87d-3e6d-9c6f-833f8135a993 | -6.1774 | -53.284302 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 882d2ab0-c71f-3732-9d90-d3dce76a79f7 | -4.0653 | -56.223801 | 2026-09-23 00:58:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fcd477e-79a6-3c04-9f1d-6af1f88b13df | -1.218 | -54.550301 | 2026-09-23 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b526898b-7a01-3335-b56a-b8747bab185d | -10.9305 | -47.3647 | 2026-09-23 00:58:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a70eec6b-6134-3dfa-8023-6acfdd976698 | -5.2863 | -47.240501 | 2026-09-23 00:58:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf6853c-8863-30c7-9685-50b6f938d078 | -2.1102 | -49.6828 | 2026-09-23 00:58:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 552bb43b-5cba-3b20-b7f1-661bd9a25c52 | -1.6283 | -55.123699 | 2026-09-23 00:58:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea466d95-fc14-3ed9-a2b5-59bc1856ebeb | -3.6744 | -60.556702 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1408e501-478f-3835-83b3-702117b65bae | -3.2451 | -53.945301 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b691bd2d-87a7-3c77-b55d-0e9054f48c80 | -3.0757 | -58.396801 | 2026-09-23 00:58:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50c06d08-05dd-36fb-b98e-0061280cfccb | -6.6602 | -50.876801 | 2026-09-23 00:58:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4b64b9-a872-3255-846e-f25c6fadaabb | -3.6316 | -58.9025 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce1ffc1c-acce-3d6a-8dba-6da5acbaf0a7 | -6.7364 | -59.41 | 2026-09-23 00:58:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3c40f9-0e1f-32f7-96a1-67726e005928 | -11.749 | -51.0005 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c86c5c9-504f-31e9-be50-eddeaeb12c22 | 1.7742 | -56.027901 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf366bed-4a6f-3c0c-ac5d-e633807eff96 | 1.7726 | -56.034801 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51526250-61ad-3c51-bf3b-767eb5341ff8 | -3.185 | -59.6996 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f366f93a-4505-30fd-a37f-e54f2a28d1fd | -4.2771 | -55.434101 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5eeb3c-cf79-38f7-8913-675e357dd82c | -6.617 | -57.9771 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 011b2015-3ce8-3409-bb72-ecf9e2af5f89 | -11.8904 | -45.7817 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2045cd08-6910-352e-9401-528f4a91e5cf | -5.7721 | -45.110802 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e6554de-1cd5-3a94-be70-ab0ca35ad43c | 1.5618 | -55.8297 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcfb7f74-caf3-3c5f-ad7b-c292e50dbd48 | -5.6034 | -45.925999 | 2026-09-23 00:58:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8134088e-eeaf-33d3-9251-3dfc3e022472 | -6.6092 | -59.953201 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb0e347b-904f-3b6d-8a07-99e4b1a56bd0 | -8.2043 | -54.7169 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3787abd2-6e8e-35f8-8e25-32755d261796 | -7.8707 | -61.180599 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 329e6dc1-54aa-3a2d-8b90-c131c1eb1842 | -5.7675 | -45.0923 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a3db70f-c5f2-3679-857a-a53e2556d5bf | -6.2543 | -55.430801 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47bb461c-54e0-3f31-8156-2365b799b49d | -6.673 | -55.050201 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776d3f9f-be28-3593-9450-1e8f1936d52c | -6.613 | -43.7146 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ded0e51e-26fa-3af7-804c-c0ce63b7e00f | -8.2485 | -55.235802 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8209f8c6-b4d4-3e5f-a0ce-a22c9c04caed | -12.8167 | -50.8848 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a698a151-b7e6-3d91-8568-737ada974987 | -10.7072 | -48.6964 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67b177f5-8777-30a7-a5df-0f1f645577e5 | -6.598 | -51.315701 | 2026-09-23 00:58:00 | METOP-C | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8ecdc35-de09-305a-a122-76d7b8e3c9e3 | -4.2069 | -56.348999 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 943ca25a-17e0-3307-bf03-cbe59c4dc60f | -6.1585 | -57.713299 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a28d83-dcfc-3cce-952e-d9f070bce1d0 | -6.1071 | -57.667099 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 963ab291-2330-32bf-a2fe-0a706a6b2d8f | -12.7759 | -50.886902 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a352e347-c9a4-340a-aed8-1cfc183bb9f1 | -10.6102 | -53.968201 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b66caaab-bf23-37da-ba81-bbe9e87cec93 | -8.4587 | -48.670898 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8156c6a7-ff47-360f-9b60-dcac0748ed14 | -4.4227 | -55.077999 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdad64d9-dd73-3ce6-8d71-218d8e60128f | 1.5669 | -55.852299 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcef7df2-e2c5-39e5-b61c-129cf039d6b1 | -6.6641 | -58.564499 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38f6817d-5b2d-3519-a413-5724dd87d75b | -5.6075 | -45.942299 | 2026-09-23 00:58:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50fb7ffa-8908-3f00-8d70-152efab6537f | -8.1945 | -54.719101 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab456516-e2d9-3e47-a35c-14f963cc1f7c | 1.771 | -56.041599 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1b5f8f7-018f-3f57-ae5e-7b62de8aa0a6 | -11.887 | -45.768398 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 711c5d1c-959f-3ae6-95c6-b9c6bb608eb5 | -3.202 | -50.913502 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7171f087-7930-3d78-a865-0c911fee1731 | -9.9383 | -48.466301 | 2026-09-23 00:58:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf9f7d43-eb4b-31b5-80b7-3bb302707e6a | -12.4797 | -47.019699 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae090430-35b6-36e5-a6ac-dbc586d124a5 | -12.7841 | -50.8773 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0357fc0-d7f6-3379-bca0-e18ddf9117c3 | -10.6134 | -53.982498 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 620aad6f-9b77-3595-b156-ca2eabac4f01 | -12.7611 | -50.8675 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3ce9079-4968-3388-a7fd-234a07757a8c | -9.9481 | -48.463902 | 2026-09-23 00:58:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9be1fe4a-db8b-3b05-916d-59b3deb01d64 | -6.6162 | -59.938301 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25353c4f-fcc9-3579-8ce4-af9f4256f33f | 1.572 | -55.875 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5fbc3e-e5b7-3822-8192-e924c5a1b8c4 | -12.4911 | -46.982101 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 957c486b-1421-3eeb-a30b-4b4ddda59dfa | -3.8261 | -52.3969 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8044efd6-420a-32bc-93ee-2263c8531413 | -3.0696 | -54.393299 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93eb5e14-2e40-3fd5-b50f-3fc18df0ed8c | -6.1922 | -57.7733 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fff0acb-6538-3ea9-8144-2ba9b5ceb2c7 | -3.5223 | -59.603001 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4026ee2-7601-3bac-a26a-a1993eb71fb9 | -3.9997 | -52.0779 | 2026-09-23 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d4d38c-d6d6-3447-b275-a974a6e55ce6 | -2.6175 | -59.368198 | 2026-09-23 00:58:00 | METOP-C | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 219cffe3-03cf-3ea4-9253-68b075529f91 | -11.7393 | -51.0028 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88b6581f-1918-3882-8172-65c7726ef3f0 | -9.8615 | -48.319901 | 2026-09-23 00:58:00 | METOP-C | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c63d7a12-d071-3883-95b2-61ab7339efdf | -9.7308 | -53.949501 | 2026-09-23 00:58:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6db764d0-c2c4-3c39-9513-f94355d72ec5 | -10.3224 | -50.508499 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74fdcf91-3f36-3385-a816-75abcce8cf7a | -6.3453 | -57.7691 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee113af-1d91-3da6-a945-9b072e8c88dc | -5.342 | -45.1572 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bf53264-e3b8-38e1-a297-a4a45abefb7b | -12.7743 | -50.8797 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51f33695-05d3-3ddc-82a7-12c1cdb21d34 | -8.8393 | -50.483299 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4e967fa-41db-3e5a-a2d1-3a00ff8a6cec | -5.3564 | -45.1735 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35077a05-9a95-3e2f-a3e7-2257c0aa69f1 | -10.6052 | -53.991901 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8792c471-9efd-305b-b91e-59a9803adc63 | -5.1763 | -56.174198 | 2026-09-23 00:58:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74715cae-e7b5-30de-8556-b5be2edb2746 | -3.2482 | -53.959 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 436fac6a-6833-357a-ad07-3e8748f99e46 | -3.2302 | -46.9436 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3137ec0-ea67-3683-8acb-1cbac5e80c40 | -12.4148 | -46.966599 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99970bce-0f6e-3e7d-890b-4ff3e0beeb5b | -12.7824 | -50.870098 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85d375a9-9ac2-32cf-a9f4-8f04f26fb5b9 | -6.4526 | -54.987099 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5795f9d-1f48-34af-ae6a-f7548a026455 | -6.3316 | -59.945499 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62bfb589-7abe-30dd-a69f-0c54578f6e61 | -5.9261 | -59.913601 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 136d5a01-a3bb-3aac-a8e7-882388973139 | -12.7807 | -50.8629 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c83fa91-a72d-3733-ad25-9dc3e7378828 | -9.7035 | -51.974201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae4b96e4-e334-3ea4-ac3b-e6dfbae258ac | 2.9312 | -60.419701 | 2026-09-23 00:58:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README30.md)
