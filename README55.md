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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77469848-7ffe-3f27-8ec2-b40cae715b35 | -9.53456 | -62.40217 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d070dd0-7522-37b3-8f26-ca7c06ac1ebf | -11.16977 | -50.54039 | 2025-08-28 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b5c515f-fea4-3d29-9a53-d7477aee91ae | -13.42926 | -46.97745 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 15044fdc-7f17-3cea-bece-37aa5bd086f2 | -9.4128 | -60.50333 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4addc369-f240-34a1-a86c-fb901254b38d | -10.47463 | -57.93846 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e0a4009f-e143-3a3f-9566-eebfc46aeae5 | -15.63015 | -52.75349 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52c377aa-355f-39ac-82d4-a9222ec39122 | -12.6797 | -48.18647 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbcc47f0-4928-3f62-a0fd-1a5a02971111 | -11.36192 | -63.26707 | 2025-08-28 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 67c98ac7-e47a-39fc-9000-c5fa5d0e5f39 | -14.11718 | -53.97146 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 006331bf-b97b-37b8-9be2-217a33bbcf66 | -9.80127 | -64.2709 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0329d1da-732c-30bb-a4ea-d09befb3a350 | -9.49257 | -62.39478 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d00b81c2-d85b-3781-97a6-ef4666d5d649 | -13.52613 | -46.88344 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9890f0e1-bc93-3606-a253-f85b85ea3ed9 | -13.35808 | -54.38926 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f06bda-9d18-3def-be4b-35dc291a393d | -14.81996 | -49.21242 | 2025-08-28 04:59:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f756acc3-159d-39b5-954f-da5c89c1cf8e | -9.09406 | -65.73676 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14f6f290-6759-357b-b09d-4281265d7132 | -13.42463 | -47.01542 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2129fb64-0e54-3d07-b90f-bf9993c3f447 | -12.22323 | -64.22681 | 2025-08-28 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f3fff3-a98a-3f70-922d-58bc691256e2 | -14.23252 | -48.03563 | 2025-08-28 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e4e221b-08bb-3578-b606-4c2485d8fbe9 | -9.10567 | -60.32039 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30428616-50c3-3751-9010-781e4a8baaca | -9.12513 | -65.7645 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c91a567-2511-35cd-a495-ddbbd7a7e796 | -12.11782 | -55.19664 | 2025-08-28 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e2ab815-9d11-3adb-87f2-10cb0dd56e88 | -8.92759 | -65.92772 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98fb66a4-08ac-3c3a-bf99-a3a36130888b | -13.01446 | -56.89053 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16aa6ee8-5306-321b-bfff-61b85e99704e | -8.95238 | -65.95979 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 49884e18-8589-3203-8cda-eaa8b56b235a | -15.21355 | -53.79718 | 2025-08-28 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfdaf832-b038-361f-9ab9-55ee76e30620 | -13.4215 | -46.9976 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 42956747-56d3-340c-b160-c19f11bb722d | -8.57446 | -63.93354 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 028dc86f-7f2b-3e1b-a854-b73343357c09 | -9.46024 | -60.30295 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e491995e-3e65-320a-88e2-608149d6e440 | -12.80983 | -48.15812 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb892971-14b3-3d0a-aa9a-0fa85191fcc4 | -11.3289 | -43.53989 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cb5871f-c96f-3a3d-b483-8b4d4b24ffc5 | -9.14714 | -60.77818 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 208c6b27-76c7-3dbc-890e-303c7bbf4ccb | -12.40946 | -47.78821 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfc8c90c-66d2-34c2-8218-9c276e3ce7c3 | -10.47257 | -57.94708 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b7f5cc4-6bd3-30d0-a398-99f21faa7f0b | -10.60295 | -54.90068 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f9896d6-5ba5-36d9-816c-472401e9eb1f | -11.53109 | -54.39064 | 2025-08-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c05b6c-5e4d-3422-b907-b4cac13afab8 | -13.01779 | -56.89109 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92ede199-b0c0-3eb4-9d8b-c6bda21925f0 | -14.34568 | -53.34939 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f1da1f3-3525-31f4-b8ce-ccb123812eeb | -9.23225 | -59.68359 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33cdbcc8-e0a8-3695-aa2c-5d14fc406bbe | -10.47801 | -57.93579 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e79f9efc-5123-3211-ab9c-b09d7c08087f | -14.1397 | -45.41103 | 2025-08-28 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee5d420e-0b84-32f7-9f7b-fc6d2e79d6ba | -9.08572 | -65.7172 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d6ea5e5-6134-3727-a6d0-7fcb87aae3e7 | -10.46426 | -57.95382 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f389689e-5aef-3bed-bbb1-e3090263c03d | -8.88954 | -60.75915 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59b7244-e06e-372a-b394-502a13ffd021 | -13.0821 | -46.31763 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a82fddd-6984-34b6-b38e-68931bd175f3 | -14.44047 | -53.19468 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1264cfc-e54c-3622-b30b-928d90b79129 | -9.46837 | -60.30427 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cc08d3d-9a04-32f8-9e7d-a2902d4eafc9 | -15.64065 | -52.75961 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c580de6a-d7c0-33c0-a84f-7a1c572cc7b5 | -9.54397 | -68.57499 | 2025-08-28 04:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84a7afc2-7c49-3e27-b8be-41c1d67f1289 | -8.94643 | -65.95868 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 004b1220-77db-3329-baa8-36b069da9b98 | -9.0874 | -65.73984 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 854e1a84-31a2-3e0d-b96e-271d5380286f | -11.56858 | -47.61647 | 2025-08-28 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1faeeeab-8235-327a-8f75-eaeb1a360f27 | -12.88761 | -48.12043 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3e01f9f2-6c42-3aef-9121-05c16e4ea050 | -9.4775 | -62.3833 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e65273bc-b4cc-3ea0-9fa9-3ddc0851fe36 | -12.52094 | -53.82283 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 904b441e-53ef-31f4-bbeb-f8b353e66173 | -9.16587 | -59.55211 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 121cbac2-54f9-3b49-8031-be4c719a93f8 | -9.71061 | -61.28485 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9a2f2ab-a89b-3052-aa1c-88e305709c4e | -8.94296 | -65.94423 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6297b273-2b61-39cf-a67a-3cc1858f9b43 | -14.14066 | -45.40244 | 2025-08-28 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adc71f3c-2334-36d2-8b77-b97a95b4ad2f | -11.23183 | -55.05491 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a367ff26-8de8-3758-8fe9-928cded9b463 | -10.84247 | -54.02869 | 2025-08-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4c9df68-6b76-3153-b3a0-6e817e1ace4a | -9.48978 | -62.39562 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fb56861-b68b-33e0-8559-f798aaf5f68f | -15.60982 | -52.7207 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11c7fa72-c16d-3c0e-a84d-bcccabf4eb26 | -13.08014 | -46.33388 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1f11ea9-177e-3fa0-908b-b1ad5408065f | -8.94993 | -65.95739 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e387cd25-aa1c-3368-a329-04ecad40c84c | -10.80633 | -46.36723 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49257983-e9a1-3058-8a0e-689dbc6560a9 | -10.07654 | -62.89961 | 2025-08-28 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f20aa171-5c8c-38af-bab1-a16a3a8244ec | -15.62595 | -52.71379 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10097188-861a-3ad0-994a-41ba96e87c04 | -12.70888 | -48.18603 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8de38192-92ee-3602-aaf3-da6874435258 | -10.78912 | -60.79802 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5506bcb-526e-3cdc-926c-8fa13b109477 | -9.24559 | -64.4149 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5b33a5df-409e-3977-ab40-35a85b839352 | -9.10503 | -60.32407 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6eac3e5-1e6b-3630-8bf3-0c7f77111de5 | -13.54676 | -46.88994 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35bce027-8ef3-38a8-8483-44e5d8d93450 | -12.89243 | -48.12091 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d8179c4f-aa4c-3520-b8be-980b7116d0cb | -14.29127 | -53.04402 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 3125f588-f632-3217-99bd-acaf11647d86 | -10.28942 | -46.73805 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a2a6b85-f278-3def-90e5-4983ad340dd0 | -11.34853 | -43.5373 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8e3f5856-52dc-3c43-a3cd-8993922ac8fe | -13.43911 | -46.85212 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1e2a7f5-30fb-3a71-8ef1-7497fde1ce73 | -9.48684 | -62.38488 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41f0ecb3-3a24-3d84-9894-08d9d659cec2 | -10.4901 | -51.61372 | 2025-08-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe3e658c-616f-3a61-a977-0db28a67d2a1 | -8.87552 | -60.76491 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b212c6c0-55d2-32ca-90e6-ddc9f0aa5df6 | -11.80891 | -51.41433 | 2025-08-28 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4046717-6ac0-3444-9bec-94415915446f | -9.64954 | -59.62659 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34a411f2-4fa5-32b9-9d39-ab2e21dc7cb3 | -9.31903 | -57.70167 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf11061f-6a92-3e2b-9e5d-2a607bbc8a1d | -8.8909 | -60.75116 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be9c2528-48cd-3b3f-abec-162cbc9f67ed | -8.95758 | -65.94959 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 096eba93-d815-3517-9a89-cd28f024495e | -13.01389 | -56.89412 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0029c343-23ef-3ff1-b5ba-0953c7e931d6 | -9.16031 | -59.5613 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f34540a0-fa5b-33e7-95d5-80d6b8060765 | -13.41737 | -46.85473 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9be40f9-ae0c-39b3-9247-502cb1c69f41 | -10.33139 | -46.7741 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 452d3403-5eff-385e-8b64-3e8282c057c2 | -12.88786 | -48.12005 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6ea471b3-3cc0-36a7-891c-33435a814611 | -13.45528 | -46.85131 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 367faf03-7037-3c8d-90f2-a736530a4707 | -9.64426 | -59.62766 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c209fcd-fdf4-36fc-9b87-6c76cc6bc5c5 | -12.78397 | -48.16896 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb5bc910-be17-3b39-bb6a-af2635aa03cd | -13.63698 | -48.24548 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b24a7858-9324-3391-b695-ec0d23900fb2 | -15.62223 | -52.71332 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89f97dd9-cc53-38ca-a213-8ddb3548bda3 | -9.16139 | -65.79746 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 816edd9f-93fd-317b-9c36-7e95fe294c53 | -9.48971 | -62.38406 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b627a8a-7238-395e-80e2-037e3f46ad65 | -8.9616 | -65.94312 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b727bf5-370d-31ba-aeb8-c8c85fa96358 | -12.79216 | -48.14361 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d60809e6-e737-34f1-8788-8f4b24e7460c | -11.56153 | -46.3966 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README56.md)
