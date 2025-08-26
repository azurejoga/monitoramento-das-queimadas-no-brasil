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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cb61c7f-98a4-358a-92ba-235d0aba2f07 | -6.8413 | -58.9552 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c4e16b86-a7ce-3354-881a-8aed88938eaa | -11.559 | -52.117 | 2025-08-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| cd38dbc2-6e4c-35d1-baa5-e76c623e8c35 | -9.1909 | -59.4619 | 2025-08-26 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d2d04ed4-c8e6-3b68-9f41-5ce3a78b3f80 | -8.9874 | -65.4192 | 2025-08-26 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d8784a8e-02f4-3469-89c0-6da8a4b5fd51 | -8.9873 | -65.4379 | 2025-08-26 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 206a5e10-0a81-35cf-8e9e-52b8404598a1 | -4.9605 | -55.8226 | 2025-08-26 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| dfc3db3f-8b27-3c35-bc4b-5b24f2d7f3f7 | -14.2682 | -49.132 | 2025-08-26 02:40:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1260d1a3-3e78-30ad-b160-b062d7212008 | -6.8228 | -58.9753 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 232.5 |
| f201799e-3be4-3c52-b88e-d49f6b0014a4 | -6.2275 | -60.018 | 2025-08-26 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5a68095e-3c57-3140-bad5-e0bb4a15f43b | -8.8363 | -62.451 | 2025-08-26 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e518e75e-bb53-3e34-8823-f909624682d8 | -8.8734 | -62.4495 | 2025-08-26 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 12c51099-37eb-30c0-a717-c71ddb81cc51 | -6.7819 | -59.6711 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a28dfe36-fcbc-3a19-bf58-e617be76336b | -6.8043 | -58.9761 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0c9d1ad5-f0f4-3c48-829f-c456008dcb3c | -6.9128 | -59.3578 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f9b9435c-1303-3d64-96d5-33ec0ed4c2bd | -9.1722 | -59.4629 | 2025-08-26 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bcb51099-f4f4-3e44-a9cf-5f83ec26fed4 | -6.8412 | -58.9746 | 2025-08-26 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8a4fe781-5154-3412-b975-59b4632bb4c9 | -11.5587 | -52.138 | 2025-08-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 851c23e2-157c-32e6-90ed-44673ef1d6a1 | -8.8548 | -62.4503 | 2025-08-26 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 4e4c4157-d860-37ce-bcb9-45be57727cb7 | -9.191 | -59.4425 | 2025-08-26 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 038cae6d-54ea-36dd-892e-e88dcc2a949e | -11.3126 | -55.1112 | 2025-08-26 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 06efab9c-bd4c-3ab7-8a68-1fb5820af629 | -8.855 | -62.4313 | 2025-08-26 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 4fc4bd96-71fc-34e1-bf4a-c81391684b42 | -7.3854 | -64.3662 | 2025-08-26 02:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 695a764f-4994-332a-a459-07bad04d1dfd | -6.2459 | -60.0174 | 2025-08-26 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| e7fdfa3a-e917-3ffb-9d69-61486040434d | -8.8548 | -62.4503 | 2025-08-26 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 185.7 |
| bcb8b723-8829-310b-aeb9-d9027711c2fa | -20.8512 | -48.4761 | 2025-08-26 02:50:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 87f4eb53-c0f4-3f6c-ad13-9082e31a983f | -9.1909 | -59.4619 | 2025-08-26 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2ff1d736-7a28-324d-ae0d-50af12897268 | -9.191 | -59.4425 | 2025-08-26 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ebd4f2a1-f3e2-390f-b9d9-5c1943f468d6 | -11.1591 | -44.7395 | 2025-08-26 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| de7ec750-d363-31c4-8877-5e72a97ccead | -6.8229 | -58.956 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| a4d4deaa-1a31-3043-943e-9d9e755ad25c | -8.8734 | -62.4495 | 2025-08-26 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 31766629-7091-3a54-9e57-11537816d465 | -10.4241 | -64.3903 | 2025-08-26 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| dcb24d71-3ca3-3ae1-8209-3e46e746f465 | -8.8363 | -62.451 | 2025-08-26 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5870cd65-56f0-3581-af39-d2860023dd47 | -6.7635 | -59.6718 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| d943adbd-f5b2-3de5-abd8-c757fb2ab373 | -6.8044 | -58.9568 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f71fac22-5d05-35d8-a52a-9ae0a6b8cbbe | -11.5397 | -52.14 | 2025-08-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bd150741-3bd1-302e-af1c-686657642af2 | -14.2682 | -49.132 | 2025-08-26 02:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 2e48f28c-224e-3469-8dfd-b60cfa9b20a7 | -11.54 | -52.119 | 2025-08-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 8aab7b1f-8847-3542-9365-695db7d558dd | -11.559 | -52.117 | 2025-08-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7121a3ab-3aed-3152-9af7-9ebcf1e2e4f7 | -8.9873 | -65.4379 | 2025-08-26 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 421b9ed8-7753-3a7b-ba32-38c0b5cd8d82 | -9.1724 | -59.4436 | 2025-08-26 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d70e463f-c6b3-32d3-bd8c-44adf9f9b79e | -6.8412 | -58.9746 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5735458a-63df-3402-bd3a-cf445ae6f175 | -14.2872 | -49.1512 | 2025-08-26 02:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 43e7dbc4-4e2f-30b1-bee8-0328733a39d6 | -11.6351 | -44.8561 | 2025-08-26 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2193d608-eef6-30b0-a12a-10160a48fadd | -14.2678 | -49.1541 | 2025-08-26 02:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 2dbef944-f9e0-3f30-8cc9-257dc40731cc | -11.5587 | -52.138 | 2025-08-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 66897bfb-01d5-3465-902a-0b1c6b29d920 | -11.1587 | -44.7627 | 2025-08-26 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 55bf499d-3691-356c-9275-cfa2a3094625 | -9.1722 | -59.4629 | 2025-08-26 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 56dd983a-5685-3640-a3d1-95bbf79899f7 | -8.9874 | -65.4192 | 2025-08-26 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 42a40c92-691e-3855-9df2-4652af5dace0 | -6.8413 | -58.9552 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 02575ed7-c787-32ba-b79a-c066dd5252f3 | -6.8228 | -58.9753 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 70441589-4bb7-35ca-a276-7ca09866609d | -14.288 | -49.107 | 2025-08-26 02:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 04f1a1ff-4da2-3cfb-b251-a3bed367f9f5 | -4.9605 | -55.8226 | 2025-08-26 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 92ca1a4a-3015-3e0a-af20-a32cb00a8c1f | -6.9128 | -59.3578 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fa3302ba-0f37-33f1-95c5-2651d1a9e4a2 | -11.3126 | -55.1112 | 2025-08-26 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c6c69279-03f3-3eec-9b53-cb495da0bc11 | -6.8043 | -58.9761 | 2025-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d89e471b-3f7b-3af7-babd-83b38fbd8ccc | -7.3854 | -64.3475 | 2025-08-26 02:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7ecb5cd8-5866-3f89-b6d6-a0ffa09e1828 | -8.855 | -62.4313 | 2025-08-26 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 41fb2b1a-d7a0-3098-87cf-31c46c2d911c | -14.2876 | -49.1291 | 2025-08-26 02:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 213c4f82-e911-3960-9b64-a585a276fa85 | -8.8364 | -62.4321 | 2025-08-26 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ee5f6b17-5257-3e66-bb07-3b35e0556ac1 | -11.1396 | -44.7654 | 2025-08-26 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 36bf6ba7-d744-3730-86a1-880d4926ead0 | -9.023 | -65.7355 | 2025-08-26 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 22ec2950-60ed-35ef-9bd8-7fe2774cdb6c | -9.191 | -59.4425 | 2025-08-26 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0e5d0c4d-048d-3c6d-a32e-82b9491da1c5 | -7.3854 | -64.3475 | 2025-08-26 03:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8f227e03-242c-306c-b5c5-a5651afa66f9 | -11.5779 | -52.115 | 2025-08-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d74196d8-f16d-32e2-88bd-8e3ef23dcf80 | -9.006 | -65.4 | 2025-08-26 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| db784d48-1690-3675-90c3-93eab0b5b99b | -6.8413 | -58.9552 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f432a675-ee32-3d48-9c38-71b81e611766 | -11.1587 | -44.7627 | 2025-08-26 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 3188e92a-49b1-3d48-bf77-a3b08726b047 | -14.2876 | -49.1291 | 2025-08-26 03:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 1e3b3d47-d5ff-38c6-8e62-822977d0df5d | -6.8412 | -58.9746 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 06e7376c-0a67-3ce0-b0ec-cb40df8a1790 | -8.9873 | -65.4379 | 2025-08-26 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 9124219e-d6a7-3d93-adbc-8991b5c75976 | -9.1724 | -59.4436 | 2025-08-26 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d8486e91-43dd-339a-902a-98bddc50a18d | -6.2275 | -60.018 | 2025-08-26 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| dac1b01d-a660-362a-8551-9a298110b39f | -14.2678 | -49.1541 | 2025-08-26 03:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 75cbc50f-f056-39b1-bfb6-d4445f537f9d | -6.8229 | -58.956 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.5 |
| ccb2d0c9-4af0-37ac-87dc-ade0261eae36 | -8.8548 | -62.4503 | 2025-08-26 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 301.2 |
| d2526078-e464-3c4f-98b4-19d4be9f0862 | -11.559 | -52.117 | 2025-08-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 06ec3b79-9f7c-35fd-8ec6-f3677f1919ad | -11.5592 | -52.096 | 2025-08-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 42baba8a-1255-3da4-a3e4-1960c78aa540 | -8.8734 | -62.4495 | 2025-08-26 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4073a730-e768-3c82-8aaf-697579a5d0ea | -8.855 | -62.4313 | 2025-08-26 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 146.3 |
| a6b2a4ff-379e-372c-ad6d-3852ca67d484 | -6.9128 | -59.3578 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 17567efd-e738-3bb5-b917-41d51b6e1e67 | -8.8363 | -62.451 | 2025-08-26 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 139.1 |
| dae261da-ac43-30c5-af2b-aed48433a16b | -4.9605 | -55.8226 | 2025-08-26 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 55a560e0-555d-3b44-8dc2-923448df7885 | -4.9606 | -55.8028 | 2025-08-26 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| fe835baf-d7d0-37a8-9492-faaccf62276f | -6.8044 | -58.9568 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 50cde96e-8921-3f9c-963c-d7bd6569f786 | -9.1722 | -59.4629 | 2025-08-26 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f6495f29-7374-3b83-9746-d6cd8d738130 | -6.2459 | -60.0174 | 2025-08-26 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b1bdec01-7369-3a8b-8098-9b1472d019d0 | -6.7635 | -59.6718 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c4b201d5-234c-376a-9465-3d66f9e224bb | -11.54 | -52.119 | 2025-08-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2261c37e-d0f1-3a84-ac4c-01597624c9c5 | -8.9874 | -65.4192 | 2025-08-26 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 66a5a330-0d2e-36b0-98fd-48b42ecdfc24 | -14.2682 | -49.132 | 2025-08-26 03:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 1b6fc419-a837-33a2-943c-e846a77ec036 | -6.8043 | -58.9761 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d06ad56f-6073-3237-9f11-9d0626b15376 | -11.5397 | -52.14 | 2025-08-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 151a814f-ee33-342a-a056-24428c46eb0f | -8.8364 | -62.4321 | 2025-08-26 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6bbdd6c6-1d5a-3b00-a84e-fdfa1c916fa5 | -11.1591 | -44.7395 | 2025-08-26 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 5c1a49e4-b0da-3ef8-b451-d612424e4fe2 | -6.7819 | -59.6711 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 8fc121bb-13b6-3980-bfb5-e70866ebcd24 | -14.2872 | -49.1512 | 2025-08-26 03:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1377661e-29f4-348f-8ffa-218657250015 | -6.246 | -59.9982 | 2025-08-26 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 918c7abf-025d-3f0b-8daa-ca77c0154640 | -9.1909 | -59.4619 | 2025-08-26 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4ec97628-fe01-3327-9db7-aa59cee3ce22 | -6.8228 | -58.9753 | 2025-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 227.4 |
| b7d757f5-b56b-3568-91b4-e4303546fc4f | -11.5587 | -52.138 | 2025-08-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |


[Clique aqui para ver as próximas entradas](README23.md)
