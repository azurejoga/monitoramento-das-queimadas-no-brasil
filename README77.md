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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4853cc27-5652-34c3-96f5-1aa463c7a846 | -8.8734 | -62.4495 | 2025-08-25 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 4cbd6152-245e-37ab-ac0f-3c25581f33e3 | -5.0994 | -43.1977 | 2025-08-25 05:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 989795fc-8634-306d-a623-6814874e4e6f | -8.2129 | -61.3739 | 2025-08-25 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ffefebda-3db8-34b2-ab67-d5dfd35b1bfd | -8.8733 | -62.4685 | 2025-08-25 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.9 |
| c2a9f2a9-9935-34d8-a78b-1f80ed3ab7da | -6.8229 | -58.956 | 2025-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0c8622ac-ae03-3f85-90b2-73069e63ecd6 | -8.8734 | -62.4495 | 2025-08-25 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 158c6121-3007-3685-923b-4d69bfbb027f | -8.0683 | -49.6738 | 2025-08-25 05:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a54fd539-97c8-3638-82f2-398123c5fc3d | -8.9689 | -65.4198 | 2025-08-25 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d286351f-4147-3ffa-a6e6-609cc04b4cc5 | -9.006 | -65.4 | 2025-08-25 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 84aaa5fb-48ea-32da-9741-537aef3d3339 | -8.8919 | -62.4487 | 2025-08-25 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| e60a1f5d-285b-314f-925c-7d3f35e141fc | -6.8413 | -58.9552 | 2025-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| bb8673a4-fa97-3b00-961e-1188e0d9f9dc | -8.8918 | -62.4677 | 2025-08-25 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b7ce93c1-53c1-3945-8fbc-83f693903760 | -8.8733 | -62.4685 | 2025-08-25 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 8c9e5097-6ed1-385d-bb38-e30028df1b24 | -9.06 | -65.7344 | 2025-08-25 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4ab54975-308f-32c0-bc1a-46185c3257a3 | -12.7459 | -48.1375 | 2025-08-25 05:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ebdf43e1-35cd-33b6-866d-9d1539332b26 | -6.7819 | -59.6711 | 2025-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 56e9bffc-957a-3a5a-95c0-82b2881296e6 | -8.9875 | -65.4006 | 2025-08-25 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6928e374-774c-30c0-aa6d-aec1657cb74b | -8.0681 | -49.6951 | 2025-08-25 05:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d28e5361-917c-36e7-aed4-87157f55d6be | -8.9874 | -65.4192 | 2025-08-25 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d97cd3a4-fa46-3970-8902-76619b23c1ec | -8.8734 | -62.4495 | 2025-08-25 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 39608217-0526-3c18-95aa-4cd653176bd9 | -9.06 | -65.7344 | 2025-08-25 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e13c8b61-120b-3aff-b0b9-d014b2d57b2e | -9.006 | -65.4 | 2025-08-25 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| cb705a62-0df5-3491-a3f4-33ce513da900 | -8.9874 | -65.4192 | 2025-08-25 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| ac22dbc1-9f93-36b5-ac3e-31ddcdc9b3a6 | -9.0786 | -65.7338 | 2025-08-25 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b38715cf-7e7c-3e74-a410-c2a9ee510ad2 | -14.5072 | -51.9354 | 2025-08-25 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 8326284b-31db-3d9e-92c0-c06dd1eab03d | -8.8733 | -62.4685 | 2025-08-25 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 4bb81fcd-7984-3357-9045-2a8f4bf711a5 | -8.8919 | -62.4487 | 2025-08-25 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 7b149241-a370-3899-8071-ebf11afc34ee | -8.9875 | -65.4006 | 2025-08-25 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e0411146-e54d-3761-b55d-53f402c8d3a8 | -9.1722 | -59.4629 | 2025-08-25 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0e57ab93-c034-339a-b5b6-458eb91a60e1 | -8.5136 | -63.8799 | 2025-08-25 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 925e242a-e480-3f1f-97e6-c388d0f7725a | -8.4951 | -63.8805 | 2025-08-25 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 138711d6-a3dc-3d45-b805-3fb402be79cd | -9.0415 | -65.7349 | 2025-08-25 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| c24ee8ab-1444-3510-9e1a-8da5d9853732 | -6.8229 | -58.956 | 2025-08-25 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 0854195d-3273-31dc-b721-19967740dc1b | -8.8918 | -62.4677 | 2025-08-25 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e1881d7e-fa0b-3fcb-8a2b-ad5c9db14c65 | -14.3912 | -51.9508 | 2025-08-25 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 77fbf6e0-cf3c-3bae-82bb-7c42b50881ad | -6.8413 | -58.9552 | 2025-08-25 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 281ae0bf-2326-32e8-bfcf-819c862f722b | -9.006 | -65.4 | 2025-08-25 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a43c9c7d-82b3-3df5-8b5d-1ed4a14f03b0 | -9.1722 | -59.4629 | 2025-08-25 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5a1361e3-d919-3741-b392-5159d3c2d0c1 | -9.0415 | -65.7349 | 2025-08-25 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 79a0a659-285b-3192-8300-b3aaa267f8a9 | -8.2313 | -61.3922 | 2025-08-25 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| bb790d96-c7ea-3369-b91b-41d2057fd963 | -6.8229 | -58.956 | 2025-08-25 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 9b5e216b-b800-3fdc-9726-4f19c93fef1f | -14.3912 | -51.9508 | 2025-08-25 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 07c22f1f-47f0-390e-8672-adb48b81cf99 | -8.9874 | -65.4192 | 2025-08-25 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| ae7b6cc3-4fc1-3c21-9353-46f15dae175f | -8.8733 | -62.4685 | 2025-08-25 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 25185143-23ff-3a06-a220-f2051f72960d | -8.8919 | -62.4487 | 2025-08-25 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 52dab5fa-775f-34e0-ae05-8394188453a2 | -15.1451 | -59.5838 | 2025-08-25 05:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| cfa68bbf-74b9-3242-8b35-41488fc2dcee | -8.8734 | -62.4495 | 2025-08-25 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 28effd60-f86f-35a3-9219-c3239297ae49 | -7.9077 | -63.073 | 2025-08-25 05:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cfeb06cd-d44d-31eb-92df-8d7f5e1616b8 | -6.8413 | -58.9552 | 2025-08-25 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 52e95599-d653-315c-bb6c-d058092f51ac | -9.0786 | -65.7338 | 2025-08-25 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| aeb8f2ef-f067-3ec2-9e55-501de771946f | -8.9875 | -65.4006 | 2025-08-25 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0305589b-ce90-3702-82a3-32858e5e2d5f | -9.1722 | -59.4629 | 2025-08-25 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b376c584-b691-3dcd-9085-95de1b361255 | -9.06 | -65.7344 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| fd141ba0-46a4-3a18-b38c-b361a0927bcd | -8.9689 | -65.4198 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 48d0c788-d095-3c88-bf24-e061e0e20e74 | -9.0415 | -65.7349 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 826fcf05-fdcd-3e42-acda-e58338039db1 | -8.8734 | -62.4495 | 2025-08-25 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 7d96236c-78a2-3c0c-bcc6-879885c47dcb | -6.8229 | -58.956 | 2025-08-25 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 82e37152-39ce-393a-999c-c0e749ebcbdc | -7.9077 | -63.073 | 2025-08-25 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 00134d50-a4ad-3d38-9202-b411e41759c6 | -8.8733 | -62.4685 | 2025-08-25 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 9c074642-3486-3b42-bd84-8d137cccbd52 | -7.8892 | -63.0737 | 2025-08-25 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3164d6eb-8d5c-3807-8852-ecce0d2aff0b | -9.1812 | -60.7939 | 2025-08-25 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 5bd6baf0-a9c6-3e26-aeea-f703f65928cc | -9.0786 | -65.7338 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| d24a6f82-a676-3665-99d1-4d9bb8056965 | -8.9874 | -65.4192 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| a03cde7b-9a6a-3d49-9b4d-0d05359efce7 | -8.9875 | -65.4006 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 28ae2f14-8cf0-3bd6-a1e1-8279d4c06c8f | -8.8919 | -62.4487 | 2025-08-25 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 61c9334b-da4f-3946-be48-8afe84efd721 | -6.8413 | -58.9552 | 2025-08-25 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e8f5f0c5-714f-350b-b928-91667d096a39 | -14.3912 | -51.9508 | 2025-08-25 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| bf4a46fd-4761-311a-96c1-382f879515e5 | -7.9078 | -63.0542 | 2025-08-25 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 25c06587-db2a-3a0c-a455-643d72ab5f03 | -8.8918 | -62.4677 | 2025-08-25 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5ee6b89e-0ac8-3fee-96d8-71ad2dc188e2 | -9.006 | -65.4 | 2025-08-25 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4216b7bc-4274-373c-be0b-f80d57299597 | -7.9262 | -63.0724 | 2025-08-25 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 669e0111-8b9d-36a7-a7dd-f5920314e58d | -7.9076 | -63.0919 | 2025-08-25 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8d411509-167c-3596-acb8-7c7f3f4401d4 | -4.95994 | -55.82167 | 2025-08-25 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 353ec485-93ad-3a94-be89-adb5a9dc5a3f | -5.74176 | -57.58177 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dec0cfe4-2dcd-3b3b-ac21-444f4fd5bb07 | 1.10315 | -60.47543 | 2025-08-25 05:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f49c1af-9506-3260-8881-c26343c61633 | 3.83533 | -60.90769 | 2025-08-25 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a49411ca-7f68-3f59-82b5-6e1cde9adce4 | -5.7531 | -57.58824 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebdfe33f-5de3-367e-bb35-c42cdecf8882 | -5.74835 | -57.57831 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49841aa7-592a-37c4-b61f-43f3e2fe7f5c | 3.81899 | -60.91158 | 2025-08-25 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35d678da-8a8c-3eb6-a6af-94efd2ee285d | -5.74773 | -57.58281 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0b89f91-0f61-3192-9afc-23a67ee4379a | -3.83764 | -55.97003 | 2025-08-25 05:53:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 919a98af-147d-3789-bcad-074579274014 | -5.7453 | -57.60062 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e69c05e9-9d62-3a27-9278-97ad765a1013 | -5.75189 | -57.5971 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bb376bd-0d43-3194-ade1-403039a62abc | 3.83942 | -60.90678 | 2025-08-25 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8919f7f9-70b6-3037-829f-e8aacccfa420 | -5.75434 | -57.5792 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a0eb01f-3b3d-3d5a-834a-b52c444a8264 | -5.75372 | -57.58372 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddcb9f12-a653-31e8-bc1f-dcb46ed88447 | -4.96657 | -55.82251 | 2025-08-25 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 225a7d11-1a6f-3f18-874a-0789f681b4c1 | -5.74237 | -57.57732 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c2ac83d-80e3-3410-96aa-d43de536a9c3 | -5.74712 | -57.58727 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c227bcd-f9fc-3a25-a435-887b9e2301b6 | -5.75249 | -57.59267 | 2025-08-25 05:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c72ecaf-081c-3d2a-b9c1-e00149ed451f | -9.82061 | -64.26243 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ffd7748-985c-3964-9888-76bf186efccc | -9.09056 | -65.73037 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6cc0b41e-8906-3c60-a4e9-fff8b49f1b40 | -9.05995 | -60.6236 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a8bcc1c-d59a-38ba-807b-64e96980f906 | -8.59798 | -62.61046 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 795287a0-1637-328e-b2f2-ab8a95461673 | -9.16277 | -62.34983 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55941b4f-34ef-3957-a38a-3e511753bb3d | -9.1969 | -60.79155 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5005344d-cb73-3909-8df2-001a8a716abf | -9.08751 | -65.7255 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 143f829f-a183-3627-ba07-d8eca6764db8 | -9.06938 | -65.72498 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f9da5c40-58c3-34f9-ad80-9ef03a009de2 | -6.68089 | -58.86007 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54e3c2a2-2566-3f05-be9e-ade8b85cf653 | -8.99776 | -65.39904 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README78.md)
