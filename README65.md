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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 537fcfcc-824d-3a17-a081-16022a099925 | -7.52534 | -61.32364 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7c16f82-aab0-339d-a614-20133507d61d | -9.50737 | -60.53607 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c232ba02-3087-3623-9740-4023e3dde687 | -8.98313 | -60.55496 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb4b8e7a-cd88-38b6-a25a-779c497c9b24 | -9.51057 | -60.5397 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af7043b1-41a6-37a8-9c3d-4fdc1416bd42 | -7.94653 | -61.75072 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08cbd6e7-d758-388a-8d67-f462adf87905 | -7.07307 | -59.23502 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5d9ad67-f26b-3b5d-b58d-aa72546fb609 | -8.98375 | -60.55034 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c3f098d2-b214-35c6-848d-1567f313c4f4 | -8.98617 | -60.5617 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0c74c2f-00fb-367f-aad0-206c65777f27 | -9.50849 | -60.52015 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b84de708-647f-37fd-9f02-54a37bc0a1ac | -7.5661 | -61.43132 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58241b04-c3f2-3521-b893-9a374555c4fd | -8.99399 | -60.50919 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6680b03e-ae3f-379a-bb46-68c8d05899ff | -7.61272 | -63.32766 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88710d8c-4483-3276-b2a0-54ef6121a478 | -7.95427 | -61.75569 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34c4e651-1cf8-3ce4-856b-6bdab643d9d1 | -9.50149 | -60.51121 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 134f19ac-05f7-387e-b634-b523e9217e48 | -8.4692 | -64.053 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 62e843db-5ac3-3b36-a51b-a71c87bfee2f | -9.16098 | -59.6352 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 063af6c5-cb26-3c72-8d96-93d406233f59 | -9.39824 | -60.54781 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4836f76-d3cf-3a72-8f32-91bc46dc6a24 | -8.99018 | -60.5372 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7990dd87-fde3-3744-9e3b-762e8fc2ad4a | -7.42712 | -60.02625 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 184d1436-40b6-3018-9435-8cd3b017270d | -6.66908 | -58.81501 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba183f8e-a467-3272-b39c-ba5bf0c91e03 | -7.6283 | -63.32545 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7291a0ab-c163-3e1d-81f1-23a159b6aea6 | -8.98767 | -60.55568 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31ac884b-8735-31fa-a97b-ad2ac36050ce | -8.9955 | -60.49675 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bba159ea-2ec2-39f2-82e1-48283ffb4cb4 | -9.50211 | -60.54017 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a62d659-323e-3006-aaa9-c2c035d10408 | -8.59012 | -63.87039 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b855e3-67fd-3e81-9975-374d1c489e0f | -8.14743 | -62.77412 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4648cafb-fa2f-30d3-875e-c48c6aa607f3 | -9.216 | -59.64938 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45c8ce50-a554-3acc-97d9-a3d3aa14f66d | -8.99213 | -60.52018 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1dd82cc2-ee80-3f5a-a935-be2f0688861b | -7.53574 | -61.34121 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfb1b3b9-b2f5-3cfa-8e3c-9c37764fd541 | -8.15131 | -62.7747 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2713fd79-21e6-323f-8778-5c6d63f833f3 | -8.9857 | -60.50005 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 586b7ef9-8b8b-37b3-83f8-af46b5554c7a | -8.66804 | -62.45956 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b57843f-10c8-30ba-a7e5-34ac0f67ff9e | -9.50277 | -60.53546 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8539d13-8f1e-3187-9bcb-0454a2e22e22 | -8.97982 | -60.54506 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 829f845e-4549-311b-b6cb-ad256a0c02ef | -8.90037 | -60.74402 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1716e5b3-fef7-3db5-9f01-f856e7c36a61 | -7.61076 | -63.34105 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 978d5a9e-00b8-342b-a092-8c3f259606cb | -8.99726 | -60.51936 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4fa1ad3-6325-3ad2-af0f-d93b8bdc4122 | -6.95318 | -59.52838 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24a1e3f7-f490-30ee-ad5c-8fedffa113b7 | -7.8748 | -61.82302 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e07085b-066d-3c37-9aea-d2ccd3053e49 | -8.98358 | -60.51726 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ea92cd5-e255-32c7-9206-745147df7b94 | -7.67643 | -63.30983 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76afe467-cf92-3d32-b222-52bc4f51acda | -7.56536 | -61.43229 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b1e3e55-4802-3fdb-a35b-025bb2e1f2c3 | -8.98689 | -60.52721 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0a7980d8-7c02-3972-8da8-963cacd0fc02 | -9.50538 | -60.5502 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 155355fa-7fd3-34ba-bc97-3323033a0e83 | -8.99463 | -60.50449 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 860c5190-e779-3152-bc9e-d17069056e40 | -8.9883 | -60.55106 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e79f1a31-0ca1-3503-a3c1-4167ff449066 | -6.9328 | -59.53556 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a06f0913-238f-32fb-8186-775a6d3cb9ee | -6.65256 | -58.81744 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7893750-6587-3c43-abe3-837dcec85611 | -9.3884 | -60.55129 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 506eecfa-581d-38f2-a092-d02b33bea579 | -9.16172 | -59.62975 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e0774ae9-3852-3dba-8015-e2cc50728767 | -8.94017 | -62.23876 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a06ed2de-fe5a-361c-90d3-060ddeecbd39 | -8.99207 | -60.52331 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70ff6a80-547b-3b19-87bf-21c31de4c7ea | -7.6226 | -63.33826 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e92b10-f333-3b03-8116-6b3e82425f35 | -9.21184 | -59.64335 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df576f6d-f582-39fd-9035-f015ae5958b6 | -8.92799 | -62.23699 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e98a9c78-b455-310e-9df1-08b243575879 | -7.91761 | -61.73113 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f5724f02-7713-3a69-89d4-4715c09903ba | -7.1255 | -59.65281 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6e7040b-04b4-3ee8-a2d7-ee9eabcac4de | -7.81677 | -61.32999 | 2025-08-16 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc2dbeb-5369-383a-9ed7-4b48e8ea10d1 | -9.00182 | -60.52007 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e85f21-50a4-35b2-8281-c86efdd436f9 | -9.50406 | -60.55954 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 366181b1-7cec-3ab3-8f27-6e1628accc81 | -8.98236 | -60.52342 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb3adafb-8f85-3b28-a6e8-ec139b7be03d | -8.98637 | -60.49535 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f627ed50-7e70-3b23-84b9-25c2339dd86e | -9.39365 | -60.5472 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df048731-fcc7-362f-9a1f-8f46a9492e7a | -8.66729 | -62.46473 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c3f300-8309-36cd-9cc7-79b0b40d2003 | -7.61645 | -63.32822 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1340bbe5-f4ee-3035-b33f-548c20a20a75 | -7.62764 | -63.32991 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01999758-0d04-395e-a113-785d48857381 | -8.99537 | -60.53324 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4985c3c6-d545-3deb-9596-675acbdd82a9 | -8.99014 | -60.53403 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e2a18554-4979-3422-bd97-73499f211d9d | -8.06095 | -70.58263 | 2025-08-16 05:50:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 366a8860-36ab-395d-aadb-c2f844aa1a93 | -8.99652 | -60.49051 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc2d41a4-46d1-3481-9193-514171c13ec8 | -8.89651 | -60.73893 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5759edd-687f-39c3-b67e-288b5f16b356 | -8.97971 | -60.54193 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26f82a9e-dd61-3d6d-85c9-1a2909eb7c3a | -7.61514 | -63.33714 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ea15df-c1e3-389c-b192-cc8943fbccf6 | -8.11677 | -61.19201 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac98e66f-62ad-3e66-ac70-f9471b2a0b94 | -7.6109 | -63.33436 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53194b68-20a9-36d3-9eff-311e197f7e42 | -8.46557 | -64.05245 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8a675081-b304-3b8f-a165-76239498f6d0 | -6.64848 | -58.81768 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dbfc4aa-e52c-36cf-a16c-afc5d047321c | -8.98045 | -60.54046 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 97f23585-1890-3985-b272-664f6f15d422 | -6.66329 | -58.8133 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4057dc4f-d6ba-3def-aa57-8b470169d89f | -7.9548 | -61.75196 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7b2291e-63fa-3243-bc75-17a582154efe | -8.996 | -60.5286 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 48c08a5d-7b51-3254-ba94-0b3ff211144f | -8.98692 | -60.5241 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 10de21ba-7d22-3278-9acf-3e4b3678b84e | -6.95177 | -59.53819 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1ddd44d-f29e-3701-a183-10fb7d9c6516 | -9.21297 | -59.65346 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8b0398a-4840-376e-89fc-f7a83063d46d | -7.56354 | -61.41908 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a874e0f-0ade-33f8-9056-31a5335da4a0 | -7.61952 | -63.33324 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9938905-f89f-395b-aba3-d32b2b8b74c0 | -8.97009 | -61.6789 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 07fbd854-2929-3b98-957a-8f02659cc5b0 | -8.98751 | -60.52262 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7022df4f-099f-3f4b-8154-515a1c695f2a | -7.24683 | -57.62854 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 093b1c9f-4bc8-3f35-93f1-d1e3c45d1747 | -7.92892 | -61.74044 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ec79f08-8961-35e2-826d-93c9575d35ef | -7.2473 | -57.62506 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a1580a7-1b86-3139-82f7-92637e52b7e7 | -9.50543 | -60.51657 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02542539-c76b-3269-acac-2733bede95ef | -8.98749 | -60.55249 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9749232f-b829-34aa-bc7e-60dbb0328d8b | -6.13541 | -57.9287 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a57a487-7992-3970-8a90-21cefaaa70e6 | -8.99147 | -60.52478 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 603a3b96-f7d1-3fd9-8716-107c66a2d5ad | -6.95104 | -59.54326 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f11099fc-9758-3644-9f4e-fafb76281237 | -6.94958 | -59.55334 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0f516fd-6e24-35a2-bace-e123d912e608 | -9.20067 | -59.65293 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35a77c81-ec34-3fc9-a8ac-c23212916b1f | -7.61449 | -63.3416 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 882cbb0e-43af-304a-a173-639f54a92d6e | -8.98046 | -60.50413 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |


[Clique aqui para ver as próximas entradas](README66.md)
