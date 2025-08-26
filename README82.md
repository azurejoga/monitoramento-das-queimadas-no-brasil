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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a03a0662-e5f1-3ed4-b9c9-f261030618b3 | -9.23476 | -60.92268 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79197e84-86fe-3aa2-b9ac-80737c7c66b4 | -11.55645 | -52.11623 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7175df21-48f9-3b65-bb9f-ded008cbc495 | -10.93925 | -63.63252 | 2025-08-26 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3589febf-b764-3220-931a-b6f3756b3f03 | -11.29242 | -53.96049 | 2025-08-26 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e200014a-0495-3320-8385-9cc34eb04fa5 | -9.1688 | -59.51833 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c4f49ef-2a47-34cb-a3a3-5d6690b64bf8 | -8.97702 | -63.11192 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1566d141-5827-33ab-8147-8586c83cf964 | -8.56564 | -63.93054 | 2025-08-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8e7fd1f-68cd-3cfe-9643-c2d5f1b32005 | -8.55011 | -62.64099 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 581f5a72-46b9-316d-85f5-802444fea992 | -11.69952 | -60.17464 | 2025-08-26 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44ba759a-708f-38cb-b27f-a50715388479 | -9.16479 | -59.51772 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5a7462b-164e-3cc6-a7c6-9fb42f86b892 | -9.23107 | -60.92213 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b12fc9b-7e21-3ab3-bf23-546d05ccc14e | -9.16332 | -59.52829 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba5d190d-96f8-3904-aab5-c733963ace1e | -8.94596 | -62.13419 | 2025-08-26 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc7db629-0735-324d-968d-3f4a9f40166c | -9.6417 | -59.63752 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba9909bc-1e86-366f-bbcb-99d045bcc9f8 | -9.88655 | -67.65884 | 2025-08-26 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a26a2be-aa51-3641-bbb6-2d431ad321dc | -10.87468 | -55.79098 | 2025-08-26 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0ec10ab-7cd3-3187-9ca2-b7140cfb1d73 | -8.85714 | -62.44352 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 23aa91f9-2b21-3ebf-9a7a-ec75a6152ae1 | -9.32993 | -63.20677 | 2025-08-26 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8e0640f-f852-3261-a33d-89aa3f6005a5 | -9.16464 | -59.45988 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b53ce71-e4bb-39d1-95d5-b186c158d6d1 | -11.5647 | -52.12822 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea966bc2-628a-3c7c-8894-318549aa5356 | -9.00822 | -65.40228 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d8c240c-26e3-332c-a1b3-21b7a8d50250 | -8.59356 | -62.63578 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f3f9c27-6061-385f-a588-6d9e619da56f | -11.54161 | -52.12668 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 3d623a2b-c845-30bf-975e-75d51e8cfe50 | -11.307 | -55.11292 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 22cf8a1c-698b-3a6e-b57f-7d8267bcfbe1 | -8.98764 | -63.64187 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9cbf9e8-dd2c-30e3-a54a-0bca50de2e51 | -9.16513 | -59.45632 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d39f06d4-93a0-3cd6-ba94-5d8ce8640751 | -9.01189 | -65.69798 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53ced900-f7a9-38e6-b8d2-5f0b7d33b75a | -8.87025 | -62.42631 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0fafd13-15aa-3fc1-9fef-826cdc19fd7c | -8.87085 | -62.44563 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c44b322a-e0ee-39e1-ad17-378d94962915 | -9.19487 | -59.50779 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86af87f9-bc41-34d8-8fc8-c25f10158af1 | -14.29413 | -60.36126 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abe3ed2f-4631-3791-b89c-ac921e3dbbcb | -9.10464 | -61.43077 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff9c3c41-71ce-3c70-a264-33392e48ff57 | -10.0186 | -62.38928 | 2025-08-26 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 902e486f-dbc1-3752-ac9e-491e67a44336 | -8.61001 | -62.64207 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55d2634-dd58-3641-b543-23c43693b3ec | -9.22336 | -59.66923 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac682924-d4e1-31ae-9c03-ef3eb00fbd9b | -9.15847 | -60.78205 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e203588-c24a-3f3c-b4c9-6d616f82457d | -8.84056 | -62.43714 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05e1b4c1-4ede-39b4-9400-b1b1bb04a025 | -8.34217 | -62.92977 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f61b89-d145-38f1-8fb9-b6154b8469b8 | -9.04139 | -65.72846 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 016c9e78-9397-3bad-8242-584bfef3d47e | -9.2391 | -60.91882 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6b89f2d8-face-354d-b546-e99822b374e1 | -9.02472 | -65.70371 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c180e01-4cc0-3d9d-af5c-9a5bc091894c | -9.08893 | -65.72509 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b84e8218-52b4-3a9a-84c1-9c37b1a1787f | -9.08319 | -66.06124 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5b292e9-ad48-3e22-b845-fb4a4755bc46 | -9.01322 | -65.3922 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad85e0c4-8efd-315c-8889-f2a736fe0a41 | -11.56792 | -52.09817 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0c66a0c-ac80-3193-98eb-686d2f0332e1 | -8.85028 | -62.44247 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7d6735de-1a8e-3314-9158-5a8fce568ab2 | -9.20524 | -60.91825 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2883d0c2-cbff-30f6-aaf1-a658ae123d83 | -9.31149 | -63.43865 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4acd514b-0a91-3c22-91cf-67238506cbd9 | -10.18238 | -68.15827 | 2025-08-26 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5ca5fff-4691-3318-8ef4-5ce64decc5b6 | -10.39109 | -57.69225 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94db4d68-0c9d-3b49-8897-d231fedb1896 | -8.68966 | -62.87919 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04ee63fe-3577-3a45-993f-7dae8a6a921f | -9.18381 | -60.79044 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fde69189-2329-33c1-8758-cb6e4733c421 | -9.17015 | -59.44981 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93486814-750c-39e9-95f2-27403e4001f9 | -9.17744 | -60.80775 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 301a5cb4-1a98-352d-ba11-fe6814e1dfcb | -8.9821 | -65.41623 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10954b70-deb9-3aaa-a9a0-1d49a4cd41ad | -8.56057 | -63.89762 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49db122f-dbe3-3701-b5ee-dc60b05fa363 | -9.01132 | -65.70155 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4383d6f-7c07-34ef-a81b-94d1a10561c9 | -9.25249 | -65.61994 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81e1e3ba-a5d8-3ef3-97e1-fc641c949320 | -8.53485 | -62.64993 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a58aaef-473d-3925-bb19-a93483c3b627 | -14.76382 | -59.71048 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45ea453b-78d5-38a4-b900-7564c619ae92 | -9.01582 | -65.69495 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3637780-8ece-3c01-9741-21250ffa4de0 | -8.55295 | -62.64519 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44f21c0e-4115-3fce-8e9c-18df0b8ebe2e | -9.04082 | -65.73205 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6551fb33-e5cb-3fe0-8e8f-756e1e02c474 | -9.0141 | -65.70567 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e4d87b3-1136-3609-878b-df3119250f05 | -10.24573 | -59.66207 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab7fae8f-d932-3759-8776-cfbdc2cc0bbc | -9.11969 | -60.73532 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad6a3d06-e929-3da2-a1d1-d8be7ff2ddbf | -9.6467 | -59.63117 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6a12707-dcc3-3f12-99ba-6ff9ac8b8a1e | -9.18274 | -59.44804 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ba14d47-8167-306b-888e-c634e2993578 | -10.42294 | -64.38628 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a64951df-1828-3c9d-b50c-fb06a393de46 | -11.51268 | -52.14128 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 07e343b4-108a-38c9-8aab-06f9e9d6f50f | -10.03443 | -59.35648 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 047d917b-5e10-39d0-8e67-b88917c6c118 | -9.0252 | -65.72219 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c18d519-4af5-32b8-a492-7d74e9c3cd74 | -10.4214 | -60.26449 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94c5ef0d-006f-3787-b7dc-d12afd3487e9 | -9.07269 | -65.72614 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bae94278-740e-352f-bd1c-204352ef3d80 | -8.98596 | -65.43499 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf6641c0-f8eb-3a5f-9941-f8ce2f7383c9 | -7.79158 | -66.95536 | 2025-08-26 05:38:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a07d1477-099a-37e5-8802-1393e10f5df7 | -8.97431 | -65.42224 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 597143cf-61fe-3d45-a6a8-950b75f3c0f0 | -9.25426 | -56.9051 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f4cb42-0c38-39ca-95a8-85a44f8220ea | -8.85371 | -62.443 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 78cbc197-312a-3ec8-80d5-98e70d5cc7b3 | -8.55576 | -62.62678 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 257bb7f4-2f87-3add-8b9c-31702dbde372 | -8.55974 | -62.64624 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 943b7b02-d8ec-377e-a2f2-9af646bf3c26 | -8.89963 | -60.60035 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d26678f7-bb08-3951-b06e-7d757d2ae0bd | -8.86226 | -62.43277 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10217c9f-a221-308a-9f03-902b01229f3c | -9.17984 | -60.80584 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b720872-6851-3e15-baf2-42d983dfc1e9 | -10.24925 | -59.66642 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28b8482b-d82b-3d10-adbb-f591afd426d4 | -8.99153 | -65.42137 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccbdcabb-3671-3f42-b521-ed529cf88050 | -9.06321 | -65.72092 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405d2d43-11b5-3d48-b15c-7eee8fa398b1 | -11.547 | -52.1394 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5f3dbc0-d3c4-320f-9d26-d0cbf8582684 | -8.86231 | -62.45583 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f121989-c7a6-39f6-8e41-637e9a576d47 | -8.61285 | -62.64628 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a7b57851-2110-35da-91a9-bd3ec5e46ba7 | -9.16789 | -60.76973 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dca42b28-31a6-3092-9e47-ee43073b28bf | -11.54902 | -52.12152 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5aa9f108-bbb0-3bcc-a43f-50aa58552574 | -9.80727 | -64.25603 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e066ba6-3b88-31cb-85ff-69103472056c | -10.42348 | -64.38277 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 668d0b7b-6312-3c8a-9308-6da757c84304 | -9.19036 | -59.51074 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e799ec9a-a099-3c05-a3a2-03337aebfda1 | -9.23845 | -60.92324 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c38479eb-8c01-3721-b506-b8a71e8b5e5f | -9.01988 | -65.39327 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12c17f0e-6d43-3a01-be63-5dd74bb50970 | -8.98318 | -65.43092 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1461068-8031-3ee0-8c10-4072f337aeed | -9.19129 | -59.44571 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ff834fd-da8b-3e90-9f80-7a8cbb4d835e | -8.9882 | -65.42084 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README83.md)
