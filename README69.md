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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da9a6b16-e1d8-34de-a721-7b132f2bb27a | -7.78198 | -61.42636 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46557d19-4a2d-3a03-b76f-1ae0f025cb8d | -7.61171 | -60.97477 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f00f24e8-1e54-3a6a-b422-4e9607e94057 | -9.40996 | -65.94694 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d22c546-8177-3845-b48f-8b11335ee2c1 | -9.10164 | -61.59096 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2de19075-ab2b-3449-b2d8-2fdcf6fb0777 | -7.56109 | -61.20221 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d6292a9-5d16-3004-9984-8acfe3e99688 | -7.61873 | -61.61331 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5eb8036-38e3-3efe-8445-619733e6ee12 | -9.11054 | -61.59187 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d44d88-5307-3dae-be7c-14d503d1b27f | -7.78123 | -61.43192 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80d797dc-1a2e-30bd-82a4-fd398bab7ce4 | -7.62656 | -61.60338 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25cc5fd0-face-3527-8345-67c21e201dcc | -9.11409 | -61.59853 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfc240db-1558-34f7-9e70-959051185ca7 | -9.10398 | -61.59085 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bb29c91-e585-3fd6-91ad-7ed9f035719d | -7.59629 | -60.93664 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 949f4ceb-d28d-32ec-bc7e-151fe0f8aca9 | -9.12066 | -61.59953 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d44f0bd-8be3-3ddd-9a9f-e41f7365c63b | -6.79779 | -59.66979 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 139b8804-1a83-385f-8bc4-6bc20881ee25 | -8.9277 | -60.71621 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8038a9bc-532d-360d-b491-0bcf33205dc8 | -9.85838 | -60.1133 | 2026-08-23 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01eaf6d6-92f8-3bb6-9cf7-5b4d3e6565cb | -9.40588 | -65.94009 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fc18f4f-480a-3e1a-8d4f-aa67c9240d46 | -7.56655 | -61.19742 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ccce991-d96d-3a93-9465-694042cc1c3d | -9.85751 | -60.1207 | 2026-08-23 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91a676fc-3598-34cf-a004-0b49cb531585 | -6.80176 | -62.90166 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fa3f4f3-f6be-3a6b-b6d1-822d5dbd66d6 | -7.62604 | -61.60826 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08c78be1-7412-3d08-8532-70730fd9e5dd | -7.55673 | -61.18432 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ae648ef-6e90-39d1-b015-6b99e5227ebd | -7.62748 | -61.59752 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd162304-bded-3f9c-bd48-568e6f6d6be1 | -7.61956 | -61.60756 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54c93957-e72d-3849-bc7e-729bd2411a2f | -6.88351 | -59.417 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0c4a088b-e74e-32b9-a622-ebc7aaa61740 | -6.82789 | -59.96003 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff6265fa-775e-3fa1-95d5-e81bcba30f11 | -9.13506 | -65.95092 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9979950-2361-3b83-82a3-dca09b828196 | -8.40753 | -62.68897 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7be74f21-2c0e-3247-b5b9-9e9c758d4c95 | -8.40084 | -62.69273 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04aea058-f612-3a41-b093-5481bc77d13d | -8.70395 | -62.89828 | 2026-08-23 06:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3af43cc9-5937-37c1-b2ec-ddfad832691f | -8.70998 | -62.89912 | 2026-08-23 06:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7ff5d68-84ed-35a6-8225-90293eb873dd | -9.13924 | -65.95725 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0abadc9b-c243-3193-a58b-83f94e76f136 | -9.12133 | -61.59404 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94c93fc7-c9e3-3494-bf2b-79b06d1a8c6b | -6.83497 | -59.9607 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13351b36-2ca7-33fd-8cb1-1005b02986db | -6.88364 | -59.41186 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d1d5b3-7d2f-3847-b468-2789a0b904a1 | -9.85926 | -60.10579 | 2026-08-23 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eea932bc-af59-3190-8e36-16d2213ba2b0 | -8.93344 | -60.72684 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 129d4fb7-68ba-337c-8d46-c8d8a8b42805 | -6.83581 | -59.95427 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a692f7ef-ec7c-3bf5-9b31-96b5171ce6d5 | -7.62675 | -61.60293 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca982fa6-3f86-3ed9-abaf-f5dcf4bb8a59 | -9.12933 | -65.95591 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61248f46-4bf5-3fb5-818e-7dd2779fcfbc | -7.78137 | -61.42647 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ad14205-0d8a-303f-8a01-d3e079d74316 | -7.6022 | -60.94359 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5623e8fb-33ee-35d9-b9da-41e27eaa5712 | -9.10753 | -61.59749 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d78d9c95-04aa-306b-ad3a-ffc038c05395 | -6.88266 | -59.41917 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dda7ce8-104c-3a9c-9d51-ff04690dde9d | -7.70063 | -72.8084 | 2026-08-23 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe5555e-ff5f-3317-8a0c-1e2d13cc4c11 | -9.04884 | -65.45166 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51f26b0b-fbc7-3b91-ba1b-b201369b1d34 | -7.60456 | -60.94979 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0181c83e-76e7-3e8a-8875-194988330745 | -7.78776 | -61.43285 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf8d28ea-bf08-3cde-9998-400862a7fb01 | -9.03853 | -60.45074 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28923375-6b64-3b30-8e05-6d79ea730f44 | -9.40499 | -65.94618 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0513a0dc-54b2-31ff-bb0c-3aac0e2c8073 | -9.1171 | -61.5929 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 804f115f-faaa-36b1-9521-62a42ae2057a | -9.41084 | -65.9409 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a53cda-55b1-3730-9d1e-6a3f949ba0d6 | -7.55085 | -61.17792 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d844782b-2d13-3682-b53d-d583f867ab92 | -6.7844 | -59.66079 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59fbb898-492a-317e-b17b-b1fc7aed5c3a | -9.10327 | -61.59637 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 204365f1-ff15-3e06-af07-4fd186e1521b | -8.68876 | -62.87334 | 2026-08-23 06:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab4a8ba-0260-301a-9332-00c786d7c743 | -7.59599 | -61.23008 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 656f2be2-f4da-3956-bd68-32bcc69ecc05 | -7.36442 | -72.66157 | 2026-08-23 06:25:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44b4b895-4442-3d13-a668-47b6e11c761e | -7.59692 | -61.23573 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a10ab47-c478-3a59-a195-f672b0834ad3 | -9.13428 | -65.95658 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3cd8a23b-fa72-3d6d-9503-c68026465e43 | -9.6521 | -63.83916 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a6613e5-211a-3402-a633-498421f4b3a2 | -9.0853 | -65.41334 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b8cd8e3-59ce-3a52-903c-1a04f6dbffc8 | -7.57173 | -61.20961 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dc0db01-e94c-3a62-915e-b4e194a87e2c | -6.9699 | -59.0658 | 2026-08-23 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1904679a-e05a-31b4-9cfd-eafde191ae8a | -6.6766 | -58.7299 | 2026-08-23 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| bf14db8f-b34e-3b8b-b1ad-82e3d7c43f20 | -10.7982 | -50.973 | 2026-08-23 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| dac5eadd-3b94-30ea-8b31-7c40846292bb | -10.4716 | -49.9624 | 2026-08-23 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 4ce1c4dd-3207-3f77-86c5-d6ae66c3a870 | -6.695 | -58.7291 | 2026-08-23 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4cc6a09f-22b8-3469-aa63-47fe74d0706b | -16.0509 | -50.4363 | 2026-08-23 06:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5375cec3-4741-3df0-85fe-e56997bbac1b | -6.8062 | -58.6469 | 2026-08-23 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 056904ad-879d-3001-b404-a224bfc65dce | -6.6765 | -58.7492 | 2026-08-23 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 1f57ea5f-8e00-3cdc-8c0a-773782e55577 | -6.9514 | -59.0666 | 2026-08-23 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4020dacc-15c1-3fbf-bfd2-8698e63214bb | -6.6949 | -58.7485 | 2026-08-23 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c9761b53-1338-34d1-a565-110b517aa433 | -10.8172 | -50.9711 | 2026-08-23 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 83e148f8-a0b7-3f72-83b7-146383db370f | -6.695 | -58.7291 | 2026-08-23 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9c5fe72e-654d-3a22-9349-187fd668b9e5 | -6.9699 | -59.0658 | 2026-08-23 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| aa402036-9d4e-36b4-a88a-56844504b959 | -6.9514 | -59.0666 | 2026-08-23 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2f8ed885-c21c-3080-b8e8-57df0c958dc9 | -10.8361 | -50.9691 | 2026-08-23 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 93096043-ed64-3c93-bf1e-5ca9bf4a3f26 | -6.6949 | -58.7485 | 2026-08-23 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 86a79fda-8646-3a63-a5be-dc5d91f1d8c4 | -6.8062 | -58.6469 | 2026-08-23 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2e51a3c9-d34d-3a8f-95c2-b1b357423b4c | -10.4716 | -49.9624 | 2026-08-23 06:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 952ce455-e814-3d31-8401-8f4e674161ba | -6.6765 | -58.7492 | 2026-08-23 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a522d1c6-b148-3dfd-b1bb-d184a36b7ade | -6.6766 | -58.7299 | 2026-08-23 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b34e4ae7-e7d7-3f56-abd3-aa9053cf4de2 | -10.7982 | -50.973 | 2026-08-23 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 68441351-16c4-3afe-86bf-f61d6ebd706e | -16.0509 | -50.4363 | 2026-08-23 06:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b35a2520-0d15-3577-91f7-661c08678062 | -6.658 | -58.75 | 2026-08-23 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| af817839-55b2-3849-9d3d-d22044003a7c | -10.8174 | -50.9498 | 2026-08-23 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1b32480d-46f1-39f2-91f4-8423089672f9 | -10.7985 | -50.9518 | 2026-08-23 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 85e009f3-2e62-3429-9b15-62790d4e97b1 | -2.56449 | -47.24398 | 2026-08-23 06:40:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 71370da7-4d7a-396f-b753-e5219b69b330 | -2.55557 | -47.24265 | 2026-08-23 06:40:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f25cb5df-a459-3e1e-9702-9c8d907a47aa | -4.17002 | -42.43601 | 2026-08-23 06:40:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 32d5891f-cddc-35e6-a840-035d24fbd19e | -7.14814 | -42.79347 | 2026-08-23 06:40:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 914db9f3-edbe-3275-937f-612846df7d26 | -12.75933 | -48.37802 | 2026-08-23 06:42:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a53374d7-c7ca-3582-bcc6-ccf925c2fd56 | -13.1401 | -51.41689 | 2026-08-23 06:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 267596a6-e62c-3061-826a-9a1f4198fca4 | -12.85112 | -48.45952 | 2026-08-23 06:42:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e8562924-a9bd-3a99-9db8-cff54cac55d2 | -8.095 | -50.05688 | 2026-08-23 06:42:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8376d940-91ac-3123-9343-a32f03024fc2 | -9.79106 | -46.60515 | 2026-08-23 06:42:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a8d44cd-7cd1-3a88-a1a5-3139316948dd | -11.58165 | -46.92995 | 2026-08-23 06:42:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0233be3b-9810-3352-a4e8-ad28a9fe4c3c | -10.79782 | -50.9584 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 7dc307c9-c371-3990-81dc-d14bac5d2886 | -12.73032 | -48.39178 | 2026-08-23 06:42:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README70.md)
