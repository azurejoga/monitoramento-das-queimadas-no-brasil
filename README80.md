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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6971df95-6f06-3752-b6c0-1d1fc2c6c974 | -9.20217 | -59.51566 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fa98154-2484-3702-92ca-ab9093144fbe | -8.87576 | -62.39252 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26b8e7a2-b170-3c2b-85fe-1d69f4f9506d | -8.98457 | -65.41088 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3e913afa-094d-3e3d-b5e6-e6106bca2eb6 | -9.03873 | -65.72919 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 98b94cb9-2fc4-3b13-8641-2cc4c4183369 | -10.03722 | -59.35849 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 992d9c22-234e-3f4a-bdff-6f5642508808 | -9.07909 | -66.06532 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2bc011f7-227a-3f74-a70e-c3cabba4278f | -8.54607 | -63.51102 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 798352f9-b562-3b06-b15b-e28529686ed0 | -6.629 | -58.54719 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee592683-feb3-3195-b77c-b92983cafdb6 | -9.07241 | -65.72986 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f17ab321-3a67-3c41-afda-334dd1384e0a | -8.62985 | -62.64208 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d586f987-bacb-3f66-84b8-068c675d8a1c | -8.61256 | -62.60354 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9572f0b1-894b-322c-a591-f79c9d6920c4 | -9.02291 | -65.70906 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94551f3f-0a9e-3452-9b7f-97868a5f769f | -9.0827 | -66.06585 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ccad7341-6593-3a41-94e8-6baf6732e9a2 | -9.15696 | -59.51879 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| adf50d3a-5e6b-3da3-84a1-c52017fb9c1d | -5.79423 | -59.2133 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0744ba5d-872b-34a8-b46b-bb035f1c945d | -8.62602 | -62.63704 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 733cd0c6-7415-381b-a61f-8f73454d8eb6 | -9.01315 | -65.69871 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9e6e91-0178-3d99-95c3-34fe4213b009 | -9.96649 | -60.18445 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfafe7c8-df2f-3b7f-a017-2991617dba13 | -9.19901 | -59.451 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 690dbbf3-559e-383f-91d1-e9906cecd54d | -8.90926 | -62.42743 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd2fbd89-d1dd-370e-853a-1094bb5be1eb | -9.15481 | -59.4921 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11e1dd3e-45bb-3572-add8-711de6aab44f | -8.94834 | -62.13512 | 2025-08-25 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959e187d-49c9-31d0-9b71-39486ec5b63f | -8.90289 | -62.44049 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f84d3540-4362-3609-bb1d-fd04a8660512 | -8.88627 | -62.46147 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6adb75fd-4c05-39db-9ac7-27b2794a1337 | -9.17955 | -59.60561 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98fa3575-2876-39be-ba1f-a546d3ad838b | -9.1667 | -60.82404 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c60bfa29-22c8-3fb3-838e-ff4e480c8a7b | -9.01251 | -65.70309 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 702c6d45-c908-3370-acdd-8d5d4909b759 | -8.87387 | -62.43916 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d46c8b3e-b621-39b4-b9f5-632b3871bcfc | -8.23962 | -67.36988 | 2025-08-25 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8296f491-d7bc-33de-94b9-de2f3d1dad11 | -8.51237 | -63.87361 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab894f31-3a08-3f3f-a402-8148e1c5214e | -8.91503 | -62.41885 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 563cc1aa-13e9-3344-8ce1-86ef656f3d32 | -10.29782 | -64.50568 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 51c0fad6-0470-3f8a-9990-ede620c8db1f | -9.16346 | -59.51226 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac547d9-e031-372c-9d5f-59c765e9c613 | -8.87512 | -62.39711 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5e9a078-08dd-3a4a-89b7-b1c473dcb44f | -8.10933 | -62.86365 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 406a22a7-fd1b-3099-9834-148806a5f7fa | -9.67372 | -67.50574 | 2025-08-25 05:55:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7519c779-72d7-3d4a-b382-ca2e0d3faed4 | -9.0788 | -67.7513 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38ee912d-34aa-38e8-8603-cdc4a96693e2 | -8.88936 | -62.46011 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 046ddeec-2d5f-31d0-b19e-9f0429f1e658 | -8.58523 | -62.60409 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d66bcc-9f08-3a55-87b3-32f2e1d4e70d | -7.91421 | -63.05991 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b50db424-1402-3421-b10c-b498dca0dfa4 | -8.89776 | -62.44442 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8f302de-d8fc-3a43-aaa3-2d19bc57c484 | -9.17909 | -59.60926 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a72c2a47-3c6f-3f9f-9250-6b3174f55cf6 | -9.17998 | -59.46735 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66316b0d-39a1-3969-b60e-526c8dc055a1 | -9.20535 | -60.92015 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f60cff5e-ba5a-3356-a2d7-2a4b820d7a0e | -9.21006 | -59.49788 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2bf35ef-f401-3be5-84a2-25bcce76e956 | -9.18205 | -60.78633 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f7eaaa02-2947-3345-bc97-6dcdb0f0c5ea | -8.9839 | -65.41538 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 111525ad-5429-32de-a5e5-a4d2c98f4164 | -9.20495 | -60.9231 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce55b1fe-76ed-3bdc-ace0-54166fc5bb73 | -12.99814 | -56.89513 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fc5a3d1-0abe-3590-910c-277e8010aa4f | -9.18673 | -60.79008 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 06c43b7f-d1ac-3f1e-a19e-07eff56f99f7 | -9.1896 | -59.61477 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 945242a4-8833-3d20-982b-ef9f8e302c49 | -8.88721 | -64.19437 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32df505f-0767-3978-bb38-526ef60613f6 | -7.10554 | -59.77712 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0fc4e57-91b3-3415-8af3-ada12d3edf52 | -8.88771 | -64.1908 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f1f7720-8018-3009-83ad-6450fb2b78ed | -8.67822 | -62.87331 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f0e351c-f95d-3208-9b01-166dd1340d88 | -8.61146 | -62.64392 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b24436b-51d1-3b8c-ba89-86bc45387125 | -8.11945 | -62.88639 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd88019f-89ea-3e64-a96a-fc6728d7397e | -7.99883 | -63.45992 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05537550-c660-3ff8-9153-e7f2f3f47331 | -8.8953 | -62.46279 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8820f28-543f-3322-aaed-640248f303ce | -9.20705 | -59.60981 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 500f78ed-1fe1-33d5-996e-4901c08a6141 | -5.80945 | -59.2227 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdda6929-7ce4-3994-9854-e351019ead18 | -9.25931 | -59.63904 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1ef13a4-1907-3709-8490-6e8feace1619 | -8.87903 | -62.43523 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45817fe2-ce18-3e6c-b105-fa1d12e07c4e | -9.9607 | -60.18711 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fb58273-0e32-33ce-a47a-353a7704401d | -9.17297 | -60.81578 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4ab9667-bc09-33f5-9f86-bf9d7db022e6 | -10.105 | -57.77176 | 2025-08-25 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54e8b57b-378b-3840-82e1-415b6f18eab6 | -10.48299 | -57.94133 | 2025-08-25 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7546c2ab-c217-3707-8303-c47fd4662966 | -9.18139 | -59.46203 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1b2ec1cd-6f6e-39a5-b6b1-44686f17da9c | -9.09978 | -65.71852 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08ed1b3b-4d51-35b9-ae71-380824b4bfe7 | -6.78822 | -58.64777 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f9c2fef-b6e7-3e53-b309-a48f1353e039 | -9.25333 | -59.64194 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65ba288a-efac-330d-8703-ee66435b8d0c | -8.8881 | -62.4477 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab295b44-8721-3d62-aa8c-d53c54bc2de5 | -9.82156 | -64.28461 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f98a9938-8592-395c-962c-532bf168df0b | -8.98523 | -65.40637 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 69493bd1-0536-3082-8a37-6ab11241c191 | -9.16084 | -60.82928 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab2810ba-d6a6-3720-a9a9-b0e5ae904bf7 | -9.24285 | -60.48687 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe5d3b26-8b3c-3fdb-a84e-bcbe7941044a | -6.69209 | -58.86155 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc2fdc0-cbf9-34a8-93eb-1e7defdcc99a | -7.54879 | -63.8382 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f32e8832-776e-3b64-aaeb-d6ae367888da | -9.15916 | -59.45883 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75bc594d-f592-34db-a889-c06de0db3901 | -7.90396 | -63.0707 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 71b3ad7f-83b1-3478-856a-83596a0d3fbd | -7.65211 | -63.52658 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f387360a-e99e-3bac-8735-9d027d06f8ef | -8.49962 | -63.87542 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d8246ee7-cde4-301c-af18-b366967b6415 | -8.89839 | -62.46141 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5567d5c6-702a-3cc1-befa-1c4ecc86631f | -8.63873 | -62.64338 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| deb59300-6b05-3102-9e98-4dff9ff1b48b | -6.80011 | -58.64548 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2395ee3-03d9-3d3a-8028-ae43d90a7f06 | -7.57549 | -63.4425 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1a79678-3f95-38de-93e3-f28dc2926953 | -11.70136 | -60.18771 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7b3aded-1f43-324f-a344-65f0f9219558 | -9.01098 | -65.38715 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18201980-6f23-38e5-87b1-c72ffdef5869 | -7.56288 | -63.85478 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d29cc9a0-3694-3e7b-8498-533f22935262 | -6.64585 | -58.82434 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5d04ccb-973e-30e7-bcc6-dbbeefe567c7 | -6.82516 | -58.95251 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2de2a82c-edf1-323b-acfa-23893e4f2aa0 | -9.1659 | -60.8301 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be71220c-553c-30a3-99b3-22803dc8102e | -8.12494 | -62.87873 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c69d2131-4b30-3c83-a5cb-f17553a93123 | -9.51834 | -60.5542 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 468ea18d-e813-3eaf-81d6-1ce2f94333b9 | -9.82207 | -64.28102 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5c94ecd-a5e5-3c7d-b8cc-f76f50bac2d5 | -9.16423 | -59.46335 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| becef64c-86cf-35c7-ab01-e8bfe40812b6 | -8.89982 | -62.46344 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c970b6b-cd5d-33f3-9d21-c54bf649fd4f | -6.92479 | -62.99915 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30630ed2-1834-3ee8-87b5-420db92dfc22 | -9.16035 | -59.4929 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34465367-6698-3a78-b2aa-65b125dbb5b4 | -9.18125 | -60.79237 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README81.md)
