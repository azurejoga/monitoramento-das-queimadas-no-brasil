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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f56b9ef-2f7c-3f32-ba49-a3fb195f1401 | -12.81153 | -62.88292 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2faf84c4-76d8-32dc-a84b-0ccd072f81cf | -12.81098 | -62.88649 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c51fab73-b3ca-3f6e-af7e-023a2d154f9c | -12.80987 | -62.89362 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 742d29ef-c79e-3999-83ef-49a15e1fa524 | -12.80874 | -62.87881 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0611872-ef4e-3e90-a2ae-02accbd2979a | -12.80819 | -62.88237 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e14236e6-6e6b-3c39-9a01-57604553b712 | -12.80764 | -62.88595 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bf8c6d7-fd23-3817-8272-d1b35e2bfa17 | -12.80653 | -62.89309 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37e6610a-6e99-3821-a216-2f19141f9942 | -12.80596 | -62.8747 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a590c69-de84-3fcb-898d-eadb014d7099 | -12.8054 | -62.87827 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97cb6dac-3e97-3950-a038-63b8602896cb | -12.80485 | -62.88184 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea208b62-958f-3b05-a8f9-b2222a5c7213 | -12.8043 | -62.88541 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0fe8018-65df-3f55-9a33-a98853076b28 | -12.78928 | -62.89397 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4192b17-cfda-3a9d-8fd1-2824de006e0c | -12.78818 | -62.9011 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6af7c90-13a4-310e-b600-85ef27466ec6 | -12.78539 | -62.897 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66bef165-a24a-3f52-992d-01d9f9d3c7d9 | -12.78484 | -62.90057 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 032d09a3-d73c-360a-be04-7ae74cef49c3 | -12.78205 | -62.89646 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01878ff2-465a-34a3-bcfe-491b27f5918d | -12.78162 | -62.55162 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79988d05-0035-3a7e-9336-4bbacbde2dae | -12.7815 | -62.90003 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8539d50-60f3-3591-9bb2-a7d3293fc535 | -12.78095 | -62.9036 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1067a3c8-a284-392b-b3cf-139ce19b882c | -12.77886 | -62.59179 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 419931c1-e028-352e-a8db-5b520aab8429 | -12.77871 | -62.89593 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1552210e-eea8-371d-96cc-0d8016d66a83 | -12.7783 | -62.59539 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938392fe-070d-3a7c-9caa-59612188363c | -12.77816 | -62.89949 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97c3f731-6996-323c-a753-ffe37044bd0e | -12.77774 | -63.0345 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b2d36fd-44af-35f0-a149-d729b03d3d7c | -12.77761 | -62.90306 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a477c28-1126-3bd0-be81-b6125a88d3a5 | -12.77538 | -62.89539 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc34700-f6f7-32dd-95c5-bbad36474848 | -12.77482 | -62.89896 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c57fad23-7552-3ce3-beba-6c4067dc67fb | -12.77427 | -62.90252 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61ff8a06-f364-3736-8db7-bc64e4a5861c | -12.77292 | -62.75582 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 07823d7c-d888-327b-b804-406640da5fad | -12.77237 | -62.7594 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1124befb-557a-35b6-8580-419675587fc6 | -12.77204 | -62.89486 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f45d3a-1cb5-380c-b6ea-f34af9e58842 | -12.77182 | -62.76298 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10f38d46-1c19-3f0d-a0ad-2745c8e5fb5b | -12.77148 | -62.89842 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c078c76b-6a54-3908-95c8-20f819a31416 | -12.77093 | -62.90199 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 459d7f5c-cc7c-3881-837b-ee54843f8187 | -12.77038 | -62.90556 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b875336-b89b-3558-9fdc-fcee506d33d8 | -12.76903 | -62.75887 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| deca566f-2f58-38bf-b608-9c360b86c426 | -12.76848 | -62.76244 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7e52013-889c-38b9-a8fc-822266510a1c | -12.76649 | -62.90858 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bd4c8df-7811-3398-ac68-2badb810b739 | -12.76371 | -62.90448 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a82b426f-aa58-3032-9c0a-c8be8cc34a76 | -12.76037 | -62.90395 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c0513b4-abcc-389d-b391-637eedde3a0a | -12.75758 | -62.89984 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57df1698-5b6e-3355-ba7e-ddaf45e5ac12 | -12.68099 | -54.08029 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 315222c8-747a-3ef4-829a-92bc3d780596 | -12.68066 | -63.09214 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f9f29a5-f3ac-36e5-bda4-77058b19b654 | -12.68058 | -54.0837 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ea798a5-c680-3fea-b6ef-2e4a637c5898 | -12.67946 | -54.07886 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f12fb9a-e68a-37e4-9b38-ce61b9393f97 | -12.67597 | -54.07614 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c241be61-ff19-395b-9d8b-3d497b593d73 | -12.67447 | -54.07475 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a82e7b6-3cbc-38e6-8011-948d07e266a1 | -12.66593 | -54.06784 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43220ff0-1db4-3d73-af5d-25b7533e30b8 | -12.66552 | -54.07132 | 2024-10-01 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86d8ee37-74e0-3788-ac60-d0c68c34fb31 | -12.41793 | -50.96149 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 960638c4-d251-3b3b-9bc4-a34176e20219 | -12.41646 | -50.9616 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b90a9627-b171-3bcf-b847-f44b3002c7cd | -12.41134 | -50.96071 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbf992e3-2b3c-3131-8a24-baf9c7ded49f | -12.40987 | -50.9608 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dabb5920-1df0-3bf2-949a-c1070536b52d | -12.40345 | -50.97121 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d25c6d67-1152-3fbb-b154-bd0529908500 | -12.40279 | -50.97687 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 644fc76e-8c27-345b-b897-39be3fef9d0d | -12.40204 | -50.97132 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f70cde3-e317-3200-8024-136f65aa2e31 | -12.40143 | -50.97699 | 2024-10-01 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfb3e27c-4e8a-3841-80d3-bb4401efd809 | -12.38048 | -63.00391 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca38f397-97fa-3e82-9780-a204d38069aa | -12.37714 | -63.00336 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48e4b676-e67b-3b55-9954-f1fa865e4b0d | -12.31233 | -54.11784 | 2024-10-01 05:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aae90d7-2947-33ce-8f9e-10c63de307c1 | -12.30694 | -54.11717 | 2024-10-01 05:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54e3adb-e596-3f63-bb19-f6e90cba5beb | -12.30651 | -54.12064 | 2024-10-01 05:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df48073e-387b-30b9-9d2b-249a69138ea0 | -12.27107 | -62.31313 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51285a2b-ba60-368c-b092-87d7ca57ff43 | -12.27051 | -62.31673 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f05b5c-4078-3f35-b873-e09ff2a708d1 | -12.15097 | -50.06952 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57593c92-4072-3768-8679-26f3743c6848 | -12.15025 | -50.07599 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 242d9e9a-6712-3326-b11e-a4b082d6bdb8 | -12.14952 | -50.08249 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f7b6cd6-40f9-3bfb-9935-5dc0ba4ab52d | -12.14548 | -50.05578 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71374751-f486-3742-ab85-76dc7a5f01ae | -12.14476 | -50.06223 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9d1cee4-f02f-389c-8d35-59a3f77ea02e | -12.13855 | -50.05497 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 68c93eb6-5626-3426-8622-15ea6c420eae | -12.13844 | -64.3177 | 2024-10-01 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88cb4b0d-549d-3421-b62b-9effe6f35f3c | -12.13784 | -50.06141 | 2024-10-01 05:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c07d6ac-8cb5-34ca-bab6-20455ff9fe28 | -12.13567 | -64.31354 | 2024-10-01 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 23ab86ee-a3bf-34af-b665-8359f411cc34 | -12.13509 | -64.31712 | 2024-10-01 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff0d7636-e1ce-3cb0-9435-d3de80553896 | -11.85461 | -62.7499 | 2024-10-01 05:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d861e85a-c15b-3dbe-92dc-1fccc22683df | -11.85127 | -62.74936 | 2024-10-01 05:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 18da3022-0056-3870-ae18-1ed80eb02d36 | -11.78369 | -62.6661 | 2024-10-01 05:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c44939a9-915f-3afe-9d9e-8f2ef7ee6b70 | -11.78313 | -62.66965 | 2024-10-01 05:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba7e2a76-75d9-309e-9cfe-67e725cdeed8 | -11.77178 | -64.2762 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d663a734-f805-34ec-aa40-ae697359e5a5 | -11.7712 | -64.27979 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13e6255b-7fbd-35b0-8139-8e0bebc03eff | -11.7168 | -64.07316 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1d8e7c-1aea-32da-a6d5-24d9bbc0680f | -11.70848 | -64.06083 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b94aaa1b-5eac-3ead-a073-a1af08b361be | -11.69846 | -64.05917 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c79c1663-d5b2-3b40-b00a-30b404bae916 | -11.69569 | -64.05503 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d8d6342-ace0-3366-9140-ea3a0c8774f2 | -11.69512 | -64.0586 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d55c21ca-95a0-39ae-9519-b776754f5eff | -11.69235 | -64.05446 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7112740-03da-3f06-8055-e7edfe1eac01 | -11.68682 | -64.05337 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b35f4c-79aa-3d34-b877-fb6774278d9e | -11.68404 | -64.04926 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8033cc9-0671-3056-9ed0-8ca5695a4a85 | -11.68347 | -64.05281 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe6567e-1937-3446-8cee-9065f3e9f300 | -11.6807 | -64.04868 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6d3ef9c-4cab-3080-b00e-e09ea52a052d | -11.68013 | -64.05225 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c916e4fb-ef2c-32b9-bf36-a444cfaa2c42 | -11.67679 | -64.05168 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72ca6532-448a-307d-abeb-de90b0107c40 | -11.67288 | -64.05472 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c41ba693-0411-374f-81d8-ff04b2bf9d27 | -11.66856 | -64.99453 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1e532a9-b2eb-3d6a-9e19-91f3644a9059 | -11.66795 | -64.99825 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f7876b-4559-31d4-8770-176a979b137f | -11.6673 | -65.19499 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c217fce6-96ca-3d22-9a8e-78cdf41532a0 | -11.66668 | -65.19878 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 689f26ba-ab9d-351b-8ece-fcfe91b1b226 | -11.66576 | -64.99023 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e9162b4-76d9-393e-b5d7-5a4941c80ab2 | -11.66515 | -64.99395 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4086e494-728e-3998-a8eb-e2f137c6ae2a | -11.66453 | -64.99768 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README143.md)
