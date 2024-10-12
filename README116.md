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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2299744-3ccc-311a-9369-0e98446bab44 | -12.97111 | -62.79211 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f6b6dec-7f0e-3d8f-8a09-a219b1a9834c | -12.97063 | -62.51639 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a195d600-2bb1-37de-a257-26db10c9cffa | -12.97053 | -62.7957 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5803b97-772e-3bf9-8db4-01d9f8b661dd | -12.96995 | -62.7993 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f6ca33f-baf3-3838-8e43-c3a0ac7179de | -12.96776 | -62.79155 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed0c15c4-732c-307d-a06b-cf56b01b6acb | -12.96729 | -62.51583 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df0c089e-dbab-3399-a4e4-f15f75c9f870 | -12.96598 | -62.69542 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d20a2d7-1e71-3aa5-8f46-0ef283e8bc59 | -12.96541 | -62.699 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4939d841-13ea-32c2-a9ce-dfe6d00983a4 | -12.96483 | -62.70258 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46f924e-f7f2-3ff7-a95a-1bc8b3f992de | -12.96379 | -62.68769 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6146db67-d0fb-39eb-ac13-1e4f76bb7c42 | -12.96321 | -62.69127 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d29f98f-9c85-30f6-b838-9a0b4e292a43 | -12.96264 | -62.69486 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da920434-f169-3c13-84e5-a5432ed5d270 | -12.96206 | -62.69844 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92a34763-073c-3743-8777-d18cd47306f8 | -12.95987 | -62.69071 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a08bcff-9927-3813-905f-2b8168be8fc1 | -12.95892 | -62.65379 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7867294d-3ba5-3d21-a2df-e0ebd17b98d2 | -12.95872 | -62.69788 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05c8b71d-b521-36ee-940a-872028c8b792 | -1.93107 | -61.73806 | 2024-10-12 05:23:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0e8096a-f72c-317f-9b00-c6ab54f0ab8f | -1.92757 | -61.7375 | 2024-10-12 05:23:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76e200b0-d2e5-3f51-b77b-01affc006f27 | -1.92592 | -61.72545 | 2024-10-12 05:23:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db91e367-03dc-3333-9612-0dd5e9544da4 | -1.92408 | -61.73696 | 2024-10-12 05:23:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60d00380-22e7-3786-b2bc-7c6068edc329 | -1.9212 | -61.73258 | 2024-10-12 05:23:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b81212cb-de38-3733-a902-84e1b2ab12dd | -3.34341 | -61.55584 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 08cfb75e-b94a-3e49-bc86-88eb9dee58ae | -3.34282 | -61.55953 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 521cd68e-828f-3527-9b2d-a82ba6d96dab | -3.31066 | -61.56572 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5875a678-a092-3d4b-9956-84b0ce789af3 | -3.30724 | -61.56518 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e2a840-2e50-3d6e-9dfc-0d59023ff699 | -3.29343 | -61.58577 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 209d20f5-a736-3cb9-958a-aed1895843d0 | -3.28742 | -61.51285 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13f374e0-4518-3c95-8512-e0b37a168c3c | -3.08546 | -61.68799 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cb2f923-4cb6-3f88-8cb7-7972e43d5e97 | -3.04751 | -61.68197 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01168678-1552-3698-90c9-e3b84aee8542 | -3.04691 | -61.68571 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84704b30-cf85-3939-931e-16852d385f18 | -3.0412 | -61.67714 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a04e6639-5018-3707-ab93-a251e9eda9d5 | -3.03251 | -61.68728 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ed5fbc-a0e5-3051-99a7-dcdcfb35f814 | -3.02906 | -61.68674 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed2b8fb9-3109-3836-8b9d-7df5deb355d7 | -3.00308 | -61.41307 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520524ac-e8c8-3b06-aaf2-4c698b30e1b0 | -3.0025 | -61.41675 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a8d2d1e-5937-3dd7-8233-b5fb9c3adc67 | -2.99966 | -61.41253 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbd05ee4-70d9-3af0-b003-0c5c947cedb8 | -2.99908 | -61.41621 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 132d9590-02cc-3fa0-9d38-5c4e4dafcde1 | -2.98933 | -61.43354 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5effff94-305e-3327-a5be-5d029df8fe5d | -2.89495 | -61.87189 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b89bb7-cbda-36f0-9ec7-75a07d03a590 | -2.89434 | -61.87568 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9264f3de-4634-3a1d-b985-df912982da65 | -2.87858 | -61.88499 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4663126-b333-3c6a-9963-ea091dc22c63 | -3.29628 | -61.59001 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b61ea3da-5934-3e62-9d23-550cb54f455f | -3.08891 | -61.68853 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83234f8b-653e-3eee-be76-e531289d008c | -3.05096 | -61.68252 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 542c833c-2c5e-3585-b27b-87312e12d299 | -3.05036 | -61.68626 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6d0f176-8927-329f-8108-af22b9c201d4 | -3.0481 | -61.67823 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7bbd7171-1fb8-3bb7-b792-41041e26fb35 | -3.03775 | -61.67659 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb36108-1e10-3270-8f81-653edf1c93c2 | -3.03715 | -61.68034 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af3ce88a-5a67-322e-9c75-ff2b4164cd60 | -2.93735 | -61.76183 | 2024-10-12 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84c61661-edf2-377e-bf57-60808b77ca48 | -5.05579 | -62.52766 | 2024-10-12 05:23:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe7142c-f9ac-30f8-8259-22f035fb08e2 | -6.24886 | -62.47283 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fc476f1-7aef-3711-a894-f0f6691176d5 | -6.24825 | -62.47662 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1073f3c9-07d0-3f45-af91-7a211aa29ee4 | -5.71726 | -63.19149 | 2024-10-12 05:23:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff9225ab-308b-3880-af41-beee7e7d39d4 | -5.71368 | -63.1909 | 2024-10-12 05:23:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d99cbcf-7e0d-30b4-9ff7-800cf84d5fdb | -7.83887 | -63.59179 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79ba0cad-d5c6-34f7-a046-9320c0d30526 | -7.83597 | -63.58714 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a56e7928-fca4-351b-bbd1-3e9c62f3763f | -7.83531 | -63.5912 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17eaa976-7d7a-397f-a24d-e37011146f99 | -7.8324 | -63.58654 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b46002fe-628d-3ea7-8ec2-4c443e3cbc2f | -7.83174 | -63.59061 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8df31859-6a66-3176-ac75-11f7f66a6f5c | -6.70021 | -62.84893 | 2024-10-12 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 713afadb-5c24-3a11-a8f2-cd0b4b7941a7 | -8.78689 | -63.09053 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72cc870c-20c3-38cd-ac25-0da9f3c63792 | -8.70373 | -63.40253 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab86869f-0ec7-3ad9-a864-c5b15e33860e | -8.69178 | -63.09523 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f5df39c-e943-3088-a3a4-32c3665bb3a2 | -8.6877 | -63.09848 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f4fd4ba-3bd3-3477-bf93-ad54ce6b1e5d | -8.68602 | -62.86861 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eebf9a2a-6343-36da-9860-8de2e444f96a | -8.67792 | -63.09294 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d242b6-915d-3ab5-ab37-eb622fe49677 | -8.67445 | -63.09236 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c1a09c0-8889-3997-a67f-8a26b55055c9 | -8.67055 | -63.49422 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7da60661-eb10-3b19-be17-297d91d6e498 | -8.65961 | -63.27189 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 497eb257-d8e5-3321-b7fd-ef13eda0fa09 | -8.658 | -63.25966 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 059d28b1-a861-3eeb-a4b7-64f734d89183 | -8.65611 | -63.27131 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a335d5d1-516f-39e0-840d-e1eca9f37781 | -8.65451 | -63.25908 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3715059-7055-3605-8c68-10e582938a61 | -8.65262 | -63.27073 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c980ee59-271a-3b3a-b52d-ceb94fc2b35f | -8.64913 | -63.27015 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79908df4-1b66-356b-bdd1-59a2c36695be | -8.64754 | -63.25792 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0705372b-8627-3732-a25c-eb303883265e | -8.60196 | -63.10004 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98ab9462-7489-3c20-9beb-c28993c4c189 | -8.60089 | -63.25817 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b4b9fc-d59a-3467-bd6b-adc6ebd55a9c | -8.59753 | -63.12683 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 232b2034-ae41-30b1-a4d5-da6105bd3c8d | -8.5974 | -63.2576 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 763dc6ca-7cbb-376e-809b-503c7fb7c75a | -8.59705 | -63.10025 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 598f8eaf-9516-3fe7-ae76-d0338939cbd1 | -8.5962 | -63.12764 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec05be9b-9909-35fa-84e3-63d01ab3e8ba | -8.59391 | -63.25702 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35df684e-f9df-3860-abaa-88a88102f43a | -8.59334 | -63.12323 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77f4e4b6-9b29-3312-9821-6d80d4948421 | -8.5854 | -63.10618 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 568abfa2-07b4-305c-a167-d2ba433cdfb8 | -8.57511 | -63.41443 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ab85e12-d074-3f60-a524-5107957a54f8 | -8.57225 | -63.40991 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| befd3254-d368-3a69-af89-c725fd47b25d | -8.14985 | -63.92963 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9129e7a-eaf9-35fc-8860-70e2e2d31d78 | -9.29111 | -63.21008 | 2024-10-12 05:23:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd1e8f13-5205-33a9-ab4d-42b327943c9f | -9.26216 | -63.34342 | 2024-10-12 05:23:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4de85012-33b1-3aa1-adc5-f3c8e2096d72 | -9.25868 | -63.34285 | 2024-10-12 05:23:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1db1baa-9b1a-3ab7-a2ae-710ef9307ce4 | -9.12209 | -63.58164 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4407373-e18d-3f0a-bc8d-451881357cd0 | -9.12144 | -63.5856 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9ac83d1-ca45-3ac7-9e21-2e1bc66400ac | -9.02734 | -63.60759 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f023c9a-68ba-3c55-aa1f-b8387d450998 | -9.02669 | -63.61156 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 784e2216-88cd-3f6c-b083-0ba8e7cf92b1 | -9.02545 | -63.7305 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e042c90e-852a-3a63-8cb4-c532ffb1fe2e | -9.02316 | -63.61097 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73114834-112d-3eed-9166-f7e886567b49 | -8.99341 | -63.48423 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2f07b98-01e9-3290-b0d7-be2187f6c75f | -8.91205 | -63.54073 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e6c2b53-0cda-3730-a43b-ea5207a668ca | -8.9114 | -63.5447 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ca79b6-27d4-34b9-bf7f-770c4d768d6d | -8.81313 | -63.17704 | 2024-10-12 05:23:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README117.md)
