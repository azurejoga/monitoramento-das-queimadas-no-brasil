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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87e90cd3-68d3-3eb1-973d-5757a0634590 | -10.11684 | -57.76318 | 2025-08-16 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 778627b1-007c-35e4-aaa9-7669503a4d1e | -7.62534 | -63.32965 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b844b667-fbb7-30bb-ad0f-be41b50b710e | -7.94898 | -61.74444 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ca03e89-0c23-3477-a94b-cb2751ae3bbe | -7.91578 | -61.73919 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d56a5a4-fb7e-3dbb-ba40-759f9dfd0c24 | -7.95174 | -61.74846 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce0d0aec-3152-3cff-805d-4411892f298b | -8.99563 | -60.50796 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b1df1f8-2666-30b9-882a-bf31ede566ee | -7.61304 | -63.33951 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edc077c5-61de-3198-983d-f5f0d4c2b9c6 | -7.43654 | -60.01627 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b66e8a2-6354-37d3-afb5-008d0967b30f | -2.58704 | -51.92202 | 2025-08-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da1469fc-aa69-39ba-a08a-c3c279bf3029 | -7.12517 | -59.65234 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a094e4eb-2cea-3eb9-bdbe-045221940911 | -6.80388 | -59.82067 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be65eb6a-daa6-3f8f-b52b-c811cca550d6 | -9.7934 | -61.50079 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f91861a-8d6b-3fb6-b128-a80a2e3f4c4f | -9.51025 | -60.54164 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d15fbe53-43b7-39dd-9e12-f093b68742e2 | -8.98355 | -60.5421 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a3bbb4c4-4de1-345e-8fab-27b1f546506b | -9.16202 | -59.71574 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 625ce99b-ea13-34b0-bd92-a5c9f30192eb | -7.45736 | -59.92551 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 141c7ffa-f387-3538-b26d-fd522033778c | -7.61511 | -63.33598 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52105f06-dba4-3810-a903-ede550e7f92e | -8.99509 | -60.51148 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 463b14f6-b4e6-33ae-898c-8c178cc1f31d | -8.55934 | -63.9185 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e355762-47c7-368a-9b4e-40a00016cf2e | -8.10559 | -61.18124 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50fbb298-9bdc-3692-ad6d-09517cd6227c | -7.60469 | -63.52128 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08455e82-29e2-3f94-8301-e8106e0b3153 | -9.50412 | -60.53707 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 966aa26b-b0f6-3e4a-b4d3-a34fe11cca1b | -9.15465 | -59.67322 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e0d37c0-e1e6-3e20-ac85-344c86e27982 | -8.98681 | -60.52101 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 395bf55b-eb8b-3dfd-8c9c-7b87bffb1f06 | -9.16932 | -59.62271 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6e3374b-825f-33f3-8e2a-fe18d04cc0e3 | -7.5251 | -61.32658 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99aa3d39-2ee5-3413-9ebc-b3782162879f | -6.9498 | -59.5345 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac2bd791-4f22-33c1-be68-b2eab35bd07b | -7.04115 | -59.62518 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 660525c3-4f6b-3981-b4c7-4d18d983ca30 | -6.95199 | -59.5202 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d8b6100-1ea6-33f1-8c43-049981db8998 | -9.50529 | -60.55172 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e79bc39-2507-31a2-9f7d-4ef2e7ca7f4f | -7.91689 | -61.73219 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29936a90-b5fb-34fd-80a4-282a5ef7b16e | -7.95229 | -61.74496 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7feafa1e-9fff-3458-b6db-bb73690b782a | -9.03558 | -67.42765 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2e70c16-52c3-3773-bc0d-031a3421f0f6 | -6.94027 | -59.52936 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39ba59e0-cfc6-3042-bed1-fb32cfe823a2 | -8.98023 | -60.54158 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c99a57-7dea-39d5-9b79-f59ab3815ba2 | -8.56129 | -63.90655 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d77b3f2-cd34-3a5d-b5b4-9fdde7e27f15 | -8.99732 | -60.51905 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbdffdd4-0d4e-3592-9541-e098c59d596c | -7.83133 | -61.32581 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea51482c-6845-37ed-84a3-23c046f46e57 | -9.28397 | -63.48019 | 2025-08-16 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4282059-1d00-3205-a2e2-dc0ee9c53792 | -9.50188 | -60.52948 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e92581e-0db5-3b88-9d0d-9807472c4a33 | -8.99115 | -60.49283 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c76bdbcf-7bcd-3cd7-a1ea-ac80a95035c3 | -9.34604 | -62.58903 | 2025-08-16 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 839caafd-872d-36ad-80e2-514ec9b6b876 | -7.91689 | -61.7537 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5da2c670-0973-3ac9-9f57-ff52e93a9a3f | -9.20348 | -59.63188 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21bc8a83-d20b-36c4-a382-55f3eddda93e | -7.62187 | -63.32909 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6df4f2bd-0b9e-3c95-981d-1ebf56f8ca3c | -8.99013 | -60.52153 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9bc7f3ba-66bc-33bc-913b-0343c5291a8f | -8.15926 | -62.76905 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 712de608-10c4-314c-b8b3-686da484454f | -6.63306 | -60.00262 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4af4f3da-d5d0-3089-976d-cb069c4ef478 | -8.67244 | -62.4583 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97d06260-d473-34be-92a7-c3f5cb076b1b | -8.46166 | -64.05125 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cf5b7c7b-0272-39e1-af93-5f2eb053aaa9 | -7.61633 | -63.32829 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2711b021-55dc-3cac-a0e2-19d4568d97fb | -6.93972 | -59.53296 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39458c70-15a8-31dd-9df4-f2d19700c690 | -9.17159 | -59.63061 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a579af20-c2e0-35cb-b6fb-c678bb97e648 | -6.79613 | -59.82666 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82ef6c52-b0ef-3475-84a3-aa5a0db5a9ad | -6.8852 | -59.15429 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd0450a7-d08a-3043-93e3-92559c1ca855 | -7.43049 | -60.03334 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dba8612-ed9d-362b-94eb-7c4c53cc0870 | -9.37099 | -47.97977 | 2025-08-16 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aeffaed2-9305-3ff8-ad0a-ed191c47793c | -9.16764 | -59.65642 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de72b46f-05ba-3f72-81e3-0ece6822fd3a | -7.31546 | -60.62258 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76f2a2c9-b0a9-3173-af06-8b11158c3ed9 | -7.91523 | -61.74268 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eca8f112-220a-3bf0-adab-b8218e9e4156 | -10.04744 | -59.11739 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f99c4081-6750-39aa-8e85-25e50219f0c8 | -7.69846 | -63.31779 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dbeb841-4135-32a2-8808-0054d55073e3 | -7.8831 | -61.81656 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60ccbc17-ece0-334d-a867-20347b21d454 | -7.43158 | -60.02631 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fd740be-0451-3114-81bb-0d6b83fc7f25 | -6.94808 | -59.52326 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffb5c601-8078-36e4-acbe-acb769832159 | -9.17299 | -59.64974 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4bc75c44-3be7-3e77-a8eb-16f16a71ddbf | -6.933 | -59.53189 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d6375e4-08a6-387c-bccc-067e5c0b1f1d | -9.18782 | -59.68971 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ec79d37-ab3a-3329-88ce-27baa3e0aa79 | -9.16031 | -59.68162 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0c058b1-e8d5-3817-940e-14dcea15b60f | -7.42995 | -60.03686 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386e33fa-2ac6-37c4-a727-d6d2026c0be0 | -8.75009 | -55.01929 | 2025-08-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff942d46-7ea4-320a-ac53-33966b82af79 | -9.16707 | -59.66011 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8709005a-cf52-3dd9-ab03-207345c6a4ce | -7.62061 | -63.33678 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90bb2171-8866-3a9b-81c7-ee7b89738397 | -8.90288 | -60.57996 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc24ce5d-7544-3fab-9ff0-b3ab25c4f7aa | -9.50126 | -60.51126 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc3e75f3-d70e-397b-9fdc-0d8c95274d69 | -7.91467 | -61.74618 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86869bfe-745f-31fb-92dc-8a72f209b8eb | -8.10451 | -61.18817 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ade2ede-f67d-3f9a-9942-dec33f436868 | -8.97465 | -61.7122 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b891d931-15c5-3ad4-bf85-73a3252fa53a | -8.99339 | -60.50039 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 56322be9-0727-32a1-ba4f-c871523a0f40 | -7.68112 | -63.31499 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca19098b-5b41-3474-95a4-fd610e18e9ce | -9.17215 | -59.62692 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d72b12c2-079d-39c0-a960-ac2e8c15c7b6 | -9.18553 | -59.68186 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1806b13d-82b7-30c1-9a84-9690e156c6c1 | -6.94253 | -59.53706 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 581d83ea-ad1e-33cc-9733-dcaaa63027d8 | -8.98688 | -60.54262 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b777f7c4-17dc-3e2c-be35-45a4d41a53f6 | -8.90624 | -62.16478 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f937e04-9120-3321-9247-534af6c67222 | -7.90748 | -61.74863 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbfeed69-c46b-3b45-857c-8675d3355e7d | -6.92896 | -59.64804 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0c22088-cadb-34ba-b78c-b9971584799f | -9.16709 | -59.68267 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f364955-1bd5-3f8d-8ace-113b8ca8e872 | -3.82968 | -47.73858 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a3622f06-d52b-3639-ae6b-9f04e3c961ee | -7.08981 | -59.21544 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a5010c8-691e-373e-8570-80b11635be44 | -6.8028 | -59.8277 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a447442-ba60-3a6f-9e2f-ef76d48833ac | -7.24431 | -57.62827 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e59ecd77-bb7e-34df-9d81-1fa1db84fa38 | -6.6292 | -60.0056 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9c7cda9-1366-3557-a71f-9a3d3d3793b4 | -7.28466 | -64.69438 | 2025-08-16 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d74e63e-7a98-3554-93b8-e6917f577d6c | -9.00113 | -60.49439 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8590667a-8f0b-35f5-b09a-15bf0c7492a5 | -7.41879 | -60.02074 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0114da7-8b5c-3b0f-8a81-b5f79bb837ba | -7.6009 | -63.50061 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6adadff-afec-321d-8267-c93375f38008 | -2.47915 | -47.20802 | 2025-08-16 05:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 512081f4-11c7-3918-8d3b-bf7b74510acc | -3.48647 | -51.19019 | 2025-08-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f99d62c-1a5a-3f08-a31a-65dc25464d43 | -7.5295 | -61.32016 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README52.md)
