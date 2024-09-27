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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c56d610-d6a1-3d63-bff6-32675d7f9113 | -2.6783 | -57.5893 | 2024-09-27 00:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f76fc6b9-6de6-3425-871a-ce6223ab45eb | -2.8611 | -51.6699 | 2024-09-27 00:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b45122a5-f9f8-3820-b6ba-72eaaa99d72b | -2.8795 | -51.6695 | 2024-09-27 00:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 293f8931-bebb-30d6-8f87-84643280f38f | -3.0107 | -51.0652 | 2024-09-27 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| af0c47fa-54f9-3ce4-a745-0b835b7002ab | -3.1134 | -59.1445 | 2024-09-27 00:25:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b9408852-f554-3596-878c-a24353e642f2 | -3.1135 | -59.1253 | 2024-09-27 00:25:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 170e1db7-78d1-3539-b98e-83edbf543afb | -3.1317 | -59.1441 | 2024-09-27 00:25:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 9f054596-ba66-38f7-9e35-3f757879948a | -3.1318 | -59.125 | 2024-09-27 00:25:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f440c4d4-abad-371b-a31b-812a12e1050a | -3.6437 | -54.051 | 2024-09-27 00:25:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 36ed3bb0-a2c3-3054-a9ea-967aa9ba4127 | -5.57 | -42.9297 | 2024-09-27 00:25:38 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 5c8f4e9c-7361-306a-8034-36f2938c66b8 | -5.5888 | -42.9282 | 2024-09-27 00:25:38 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 87451fcb-fba3-3b61-a831-38676ebf828d | -5.7079 | -46.456 | 2024-09-27 00:25:39 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 77e0a8a3-0849-3e45-b7bf-aafeb45e97d3 | -6.0659 | -44.0316 | 2024-09-27 00:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5f37fb21-6afe-349a-a811-6a1e0e88db70 | -5.9689 | -64.85 | 2024-09-27 00:25:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 8454bba6-3aff-3c12-9a16-2734a1bffdfb | -5.969 | -64.8314 | 2024-09-27 00:25:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 346.1 |
| 26e6130c-e00c-324d-ad19-ef3aa37621a7 | -5.969 | -64.8128 | 2024-09-27 00:25:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 144.0 |
| eb3d2acc-45df-3a0f-b7ee-ef580e43a67e | -5.9873 | -64.8496 | 2024-09-27 00:25:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 0caf2d43-bcc3-3f63-b2de-bef652a955f6 | -5.9873 | -64.831 | 2024-09-27 00:25:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 310.1 |
| fba72bad-7681-3880-9992-f775c6b2886d | -5.9874 | -64.8124 | 2024-09-27 00:25:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 133.7 |
| e0d3e9d0-0830-342c-bdfa-872b011cb1a6 | -6.5708 | -44.1747 | 2024-09-27 00:25:43 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| dae01272-7679-3fcb-aefc-12e5e5a232ac | -6.8199 | -63.1651 | 2024-09-27 00:25:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 71712329-7bd5-3a52-b6c2-1ff8824816d1 | -6.82 | -63.1463 | 2024-09-27 00:25:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6d5db61f-f49b-3f2b-8516-2622b8f2e1a2 | -6.8383 | -63.1645 | 2024-09-27 00:25:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5b317952-0e25-3018-a019-bf37d0e88052 | -6.8384 | -63.1457 | 2024-09-27 00:25:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 0ac0981c-a5ae-3f60-ad4d-4236a91e33eb | -7.3592 | -49.5586 | 2024-09-27 00:25:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 161d06cf-cc16-38de-bc0c-27596916ebff | -7.2905 | -61.106 | 2024-09-27 00:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7d1d00b3-5286-3608-8893-61c937ef4cd0 | -7.2906 | -61.0869 | 2024-09-27 00:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e0ee1e98-c770-34e7-bf0d-24094b8a2f62 | -7.3089 | -61.1053 | 2024-09-27 00:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8aeb2869-4738-3e0a-b6e2-f89c91ea213d | -7.309 | -61.0862 | 2024-09-27 00:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8ffb5eaf-7c33-3fe2-91ac-ba8fd132b7bc | -7.4605 | -60.4114 | 2024-09-27 00:25:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 4be75448-5445-39dd-a297-e3209787f2ae | -7.4606 | -60.3923 | 2024-09-27 00:25:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9c819663-4c3b-3474-8571-25f01b396eb9 | -7.479 | -60.4107 | 2024-09-27 00:25:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8a790ed8-bf36-3941-8842-9931fdb8c384 | -7.4791 | -60.3915 | 2024-09-27 00:25:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ac9e331c-05b8-346d-ba1a-35f0256b247d | -7.5289 | -61.3825 | 2024-09-27 00:25:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| aadf985b-2a34-37ea-befe-fabde66bd2b4 | -7.529 | -61.3635 | 2024-09-27 00:25:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| afb40f5a-96b6-3248-80c1-4f2fbb797105 | -7.5703 | -60.5984 | 2024-09-27 00:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2f62136c-6629-3540-a72f-b915f344b7c6 | -7.5704 | -60.5793 | 2024-09-27 00:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e8069a89-45e6-3a7b-9352-1eeb25f730aa | -7.5887 | -60.5976 | 2024-09-27 00:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| dd0ec4d4-a3d5-33d4-beef-2517fe3e2b11 | -7.5888 | -60.5785 | 2024-09-27 00:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 32491efa-b9b6-3d4e-aa5f-696291010d70 | -7.77 | -61.2015 | 2024-09-27 00:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 78be824d-cd99-3845-bcfc-d4beddc6803c | -7.7701 | -61.1825 | 2024-09-27 00:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 7c9da088-ca69-3e5d-9149-cf8e3bb615d8 | -7.8156 | -54.7252 | 2024-09-27 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| e0fb2484-c955-3883-8707-eb33667d7245 | -7.7885 | -61.2008 | 2024-09-27 00:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| a581c5de-0e5e-34d6-97e2-1f93a5343001 | -7.7886 | -61.1817 | 2024-09-27 00:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 7ad4033f-c0f6-387f-9f38-9ef37744421b | -7.9081 | -62.9976 | 2024-09-27 00:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| db1ea999-6243-333d-a3a3-c17b2516dede | -7.9174 | -61.2909 | 2024-09-27 00:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 1e4d462a-4808-3b48-b090-29d174c52858 | -7.9175 | -61.2718 | 2024-09-27 00:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 715d25dd-1b5d-38f1-89d1-52493c008e33 | -7.9359 | -61.2901 | 2024-09-27 00:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5375fd62-7078-3100-8d09-55fd8cb9ea60 | -7.936 | -61.271 | 2024-09-27 00:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a08456ff-0fb3-3927-8eeb-ddab35ceced4 | -8.1394 | -61.2817 | 2024-09-27 00:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| dbeb105c-9b7d-3b0d-9969-0c982a8944eb | -8.3153 | -55.0157 | 2024-09-27 00:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cd2dd463-aded-354b-b066-5ba2f2c76bb0 | -8.556 | -49.6112 | 2024-09-27 00:25:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 9e411a81-5496-3084-8054-76c7e9775f17 | -8.5562 | -49.5897 | 2024-09-27 00:25:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 81b5c8b3-2288-3780-ba49-ffd08f9a5b14 | -8.4646 | -62.6556 | 2024-09-27 00:25:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 28016693-7774-3252-8d71-a8b341027769 | -8.5748 | -49.6095 | 2024-09-27 00:25:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 745840a0-1be1-31e7-9ee4-4262739892b4 | -8.9978 | -67.3724 | 2024-09-27 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 010558a4-87a5-3cf8-996c-60b0d5151915 | -9.086 | -61.1245 | 2024-09-27 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 25a3e35d-4a77-3129-980b-0198b35c2a41 | -9.1046 | -61.1237 | 2024-09-27 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1ad09cd3-ba50-3127-8131-586ca8759de7 | -9.107 | -67.8881 | 2024-09-27 00:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a05c7071-aac9-3537-b245-c6c89277aaab | -9.1255 | -67.8877 | 2024-09-27 00:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b901784f-23b0-3328-ba61-12b13c833b5b | -9.3028 | -65.3528 | 2024-09-27 00:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 0404f641-fc07-354c-b230-9d234a9d6f36 | -9.3029 | -65.3341 | 2024-09-27 00:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5e5190dc-f570-3931-a089-9d4682b84f74 | -9.3214 | -65.3522 | 2024-09-27 00:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c26a9165-2917-356a-8b51-cd20078cc13f | -9.6018 | -50.1352 | 2024-09-27 00:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 0107f887-1d7e-3428-ae1a-0a55ff7f0986 | -10.3672 | -53.7858 | 2024-09-27 00:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 164.0 |
| e0073362-8858-32ff-babf-36a8c3b3b5ac | -10.6434 | -45.9772 | 2024-09-27 00:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b0a47cbf-1c4e-3e6e-b3f5-05ac62093053 | -10.6438 | -45.9544 | 2024-09-27 00:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 4ac07698-e1e3-394e-a5ad-82c83c6b231e | -10.6643 | -45.861 | 2024-09-27 00:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 0baa9d43-e5e0-3144-b0d1-fce5fa831e29 | -10.461 | -50.7529 | 2024-09-27 00:26:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e3a43f3e-53db-30b6-829f-59e92f673b8d | -10.4799 | -50.751 | 2024-09-27 00:26:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 69886db8-40f8-3d39-908c-f552cd57ac88 | -10.8541 | -57.435 | 2024-09-27 00:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 7cd3cd6b-e9fa-3d1b-861a-ccc1f88281d7 | -10.6869 | -64.1524 | 2024-09-27 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 12d82ea9-fd09-35d3-98bd-c49fbe062959 | -10.6871 | -64.1335 | 2024-09-27 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 58664abf-f9f0-3352-b6af-86c67beb9849 | -10.7056 | -64.1516 | 2024-09-27 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7173d87d-62ae-3e3a-a7df-e6f0e99baa7d | -10.7057 | -64.1327 | 2024-09-27 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 6951c38c-59d2-39a2-994a-3a5c9444d324 | -10.8543 | -57.4151 | 2024-09-27 00:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0222e0d3-1290-3ab1-b55b-bd480d7b2340 | -10.8729 | -57.4336 | 2024-09-27 00:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9c0a92c6-e16d-3338-a903-50b2fb8cf4f3 | -10.8731 | -57.4137 | 2024-09-27 00:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ea8b46c9-3752-3029-81e1-2850dedbc216 | -10.9264 | -54.2692 | 2024-09-27 00:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 354.2 |
| 738e9a87-5731-3ec5-9941-78726dc93249 | -10.9267 | -54.2488 | 2024-09-27 00:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 411.3 |
| bfbdcfb3-b598-3736-8037-f8c767ab8d77 | -10.9453 | -54.2676 | 2024-09-27 00:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| ac62f364-7725-371e-9b0f-a5696092fc4f | -10.9456 | -54.2471 | 2024-09-27 00:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 6d880968-fbb7-399a-ba8b-da44fc2fbbab | -11.1409 | -50.8307 | 2024-09-27 00:26:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 51119368-df94-336a-a687-9820252af6e3 | -11.2034 | -54.7752 | 2024-09-27 00:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c27b9364-51ac-3caf-8aa7-377ce3a0a30c | -11.2223 | -54.7735 | 2024-09-27 00:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 03ee53b1-6b85-3718-833f-a4df27335c8c | -11.2788 | -65.2793 | 2024-09-27 00:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 9f4aa0f7-8cd6-340f-ad63-5351b9effc38 | -11.5872 | -63.9596 | 2024-09-27 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d555868a-f40f-33d3-9f99-d0d38e14ae19 | -11.5874 | -63.9406 | 2024-09-27 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9977d12b-8d17-3e0c-88c8-02752427673b | -11.6061 | -63.9397 | 2024-09-27 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a12e19c7-aba8-3271-9b19-cfd8707bbfba | -12.1533 | -40.8694 | 2024-09-27 00:26:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 2c89291d-e300-3d68-8a05-a4a3843de733 | -12.1859 | -50.8195 | 2024-09-27 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ca30809b-6d6a-32d3-83e2-afde5908585d | -12.1863 | -50.7981 | 2024-09-27 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 230.6 |
| f1c8bdf1-066a-34d3-9289-65b5f089fad5 | -12.1866 | -50.7767 | 2024-09-27 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8abd21d7-b7f1-3f8f-a1d5-df671130faca | -12.205 | -50.8173 | 2024-09-27 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e5ce7bc9-b846-3197-b802-9d62aad191f3 | -12.2053 | -50.7959 | 2024-09-27 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 271.7 |
| e52269c9-ec9f-391a-919f-f843b0f32014 | -12.2057 | -50.7745 | 2024-09-27 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0dc58913-6245-3ef5-b3b4-8f90e6944289 | -12.6633 | -54.6988 | 2024-09-27 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2c051408-835e-36f5-b210-2c4098b2cd47 | -12.6636 | -54.6782 | 2024-09-27 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| f8a644a8-2f86-34fe-8d07-a4a5026bcced | -12.6824 | -54.6968 | 2024-09-27 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| a671b0f0-02a6-30bb-97bb-c5ebdc2891f7 | -12.6826 | -54.6763 | 2024-09-27 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |


[Clique aqui para ver as próximas entradas](README5.md)
