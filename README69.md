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
| b42848ec-3ff2-38e8-afa9-1bd85de33a1b | -11.60068 | -47.15878 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b43ac3a-ed57-323c-8942-95ebad499ee3 | -13.67337 | -46.95771 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f0151b5-fe88-3db2-b1a6-02df4131b4b5 | -10.76792 | -59.85179 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ff6aae7-fa71-360f-88b2-093cdfbb216e | -12.93484 | -54.76901 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 69fb3020-6577-31ba-bb38-8e4a257789b9 | -12.95312 | -54.80587 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1d9e5bc-deaf-361f-a655-6387f06fe344 | -8.46226 | -47.33192 | 2025-09-07 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c09d791e-1a4c-3a5a-af29-984ea9362765 | -9.94918 | -60.15403 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09f80cb8-5d19-377c-aa97-62e3cea8362a | -12.8069 | -48.01717 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6e83335e-35c6-3d05-9760-3068cfea2884 | -13.82085 | -46.27705 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f78f83e6-cfeb-3ae2-9f45-2ac9b6bd6f6e | -12.15714 | -60.71043 | 2025-09-07 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 418053b6-2908-34a5-bf65-cfac99df478f | -12.95012 | -54.77126 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 157144c4-13e1-3996-92f7-2fd25834551b | -8.34902 | -52.55315 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a70f9fe-91e8-3f4e-b0e9-8b1bf5608219 | -9.39553 | -54.74524 | 2025-09-07 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb319079-f9ad-3564-956c-15b5adab0343 | -12.94945 | -54.77608 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 9dec5f17-f284-3f61-9857-4da960ae61b6 | -10.73754 | -48.5967 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e47838d5-40e6-3086-b718-e87cc9816169 | -8.38335 | -52.53793 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1db2a9bc-8712-30e2-a3e8-fd23b88c494b | -10.34095 | -46.40804 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b11ec45-319b-34fe-8322-3931f8b3844d | -11.32111 | -46.55376 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ccec41a2-2504-39bd-bd37-0dc13c1612f8 | -13.6668 | -46.95832 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fea7ce6a-f410-35dd-9f22-5f82e60b8093 | -11.31532 | -46.54756 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c47cee78-480b-3135-8624-e384b8c60870 | -13.82522 | -46.26829 | 2025-09-07 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 695b6754-d022-3e73-8e0e-bb7ecd08065c | -11.02456 | -52.04082 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a7fdbe7-e6c3-3d4c-8290-f3eb5466dd1f | -9.98356 | -51.6502 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9112d2b3-6475-3b18-aad2-a500711ab5ec | -13.01553 | -54.8267 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cb15879-44a0-3cc1-8be1-e3aab7212c1d | -8.68516 | -54.66738 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4084dd3c-63ac-3e03-99ef-51518fe67315 | -10.3299 | -46.3913 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f3e52fe-6714-3dec-9daf-463f18cb7ffd | -11.15889 | -48.39525 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cb925459-77d8-30df-8c5a-7b4de7e6d1df | -11.22725 | -60.44236 | 2025-09-07 05:12:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51ddefd9-b3ed-3a2b-87be-ec9adbb65032 | -12.47663 | -53.85013 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65345b6b-b04d-320a-829a-4207ad3a46ec | -12.95642 | -54.782 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a80c172-425d-3f44-9aa6-c08f273cab8c | -13.82745 | -46.27896 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 653c82f2-340a-30be-b6a3-64807e2b57fc | -10.33382 | -46.39521 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cbd5cc4-d8ea-3ce2-b63d-dd06b563f019 | -13.91888 | -48.04156 | 2025-09-07 05:12:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3473f65c-77a2-34cf-a4a4-e0d66b092a88 | -12.64403 | -56.98595 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59386ea6-7d61-36c9-92b7-a2c4a38d59b4 | -11.62476 | -47.15905 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11815c1f-2a4d-3b6d-ba23-ef951bd382f9 | -13.7942 | -52.74244 | 2025-09-07 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eef66486-3c20-3262-8fb2-50ca2ebaa969 | -11.57026 | -47.74936 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 479d6f41-4076-3f7f-b548-f6eb61ab3851 | -8.06593 | -52.3842 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c6a37e65-c9bd-311b-8cc8-845596a262ae | -9.46236 | -56.04911 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14af50ac-31e8-3331-a2ce-05d4283e1317 | -11.08553 | -51.99069 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 812b81cb-7331-33f6-812e-8e2d282674d1 | -8.70728 | -47.87233 | 2025-09-07 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab76cf8e-02b4-3139-aa27-7f75152093ed | -11.97679 | -50.40195 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e87187-195d-3e5a-bed3-2b572adb948f | -11.21334 | -55.021 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea10d616-91c1-34d3-ada3-6b792907718b | -11.08998 | -51.99141 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b698bfc7-76ba-32ef-86c9-fac4827ab0da | -12.94181 | -54.77498 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9e6c84a2-c260-3edf-a382-2fbf44110bc8 | -11.1593 | -48.3917 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5e04a74-3fb5-30a8-aa26-107c789c9c93 | -12.82839 | -48.01248 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6cba58bf-6a5a-3929-93db-d5ede637ae1e | -13.04824 | -47.12173 | 2025-09-07 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e98dd43-10e0-3f63-9824-a71e70225e9a | -8.37562 | -52.53291 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7765c4c7-1cc5-395f-a87b-93748c49e331 | -12.82533 | -56.51553 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f68684dc-a106-3057-8ee8-435e227c9d28 | -12.82514 | -48.01611 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d1fc15b-c067-3594-bd9c-208b5a17b219 | -10.74478 | -48.18547 | 2025-09-07 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7b4c939-b65d-3940-93a4-7e3a069e47a4 | -11.61959 | -47.15835 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 814d79b2-5770-391a-8593-cdd8fb29b753 | -11.09871 | -52.06112 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2dbcbf42-346c-3c8c-95fd-d86b4f71b5bd | -10.72112 | -48.59174 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f031415d-d800-3348-bf37-d143db638524 | -12.95062 | -54.79578 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a7f7bc0-d404-3b6a-ac7d-9026e25d697d | -11.00614 | -52.05008 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cccc5b2b-b6f1-320f-a56c-5c955368fd66 | -10.58517 | -48.47311 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0908f6d1-d147-36e8-a60e-fb92da433433 | -8.35675 | -52.55788 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e43ae35-cb42-3bf7-8367-b2c4bb2b12a9 | -13.78473 | -52.78095 | 2025-09-07 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce398a29-c5f4-32cd-96f7-c599a3e096fd | -10.84298 | -55.10073 | 2025-09-07 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b6f2a70-b58a-35d4-9546-ff6b6ad437bf | -10.74319 | -48.59695 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4de458fd-af0d-3eef-a902-7d5fb524d955 | -13.82464 | -46.27373 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7cdfc2db-7a29-360b-8e7d-fc4b505c6b82 | -9.7309 | -51.10367 | 2025-09-07 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf36c48a-2de7-39e5-9ac0-9efad2f32eb3 | -10.81018 | -47.74042 | 2025-09-07 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80a91a4d-4cc5-33b8-bf3b-6f8348e8fc6e | -12.71687 | -56.56424 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba0d38a4-534a-32ba-99ee-cd827895970c | -12.47613 | -53.85369 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a57127f-d4fc-3961-bd12-03fbefb8ae64 | -12.80336 | -48.01968 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 81198168-0f8d-38a0-bdac-16ae67d38d01 | -12.98471 | -56.90836 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 686e6aa6-957b-3e17-a830-fefdbd427691 | -12.00971 | -47.77656 | 2025-09-07 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e2dd25-789b-3af3-8c9f-abcdb6fe6764 | -12.81322 | -48.01464 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7c56560d-fd35-3b15-be99-7e4d5e319e7f | -9.45833 | -56.0524 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 529e4586-9d22-3abd-9665-5cbf255c72a1 | -12.82126 | -56.51896 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2ef19f-b368-3e1f-9368-1d397b1e0cb3 | -8.93797 | -48.65667 | 2025-09-07 05:12:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa94813a-12b9-3d05-9ed8-117d326a18c4 | -12.93866 | -54.76961 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d6ffc8aa-6b9c-3243-b84a-84cbf9529173 | -10.17995 | -46.24195 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1b083ee-6683-3c8a-994e-e71a019c54cd | -12.95377 | -54.80112 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f9b5a84-2480-3190-8fb2-0035d2e85c21 | -12.8093 | -48.02055 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a32b77a7-603f-348d-a105-d6236fa48c5f | -11.62583 | -47.15873 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9de348e-acf6-3424-8a8c-d49a6db42a57 | -8.55338 | -51.36567 | 2025-09-07 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6d6f782-68b2-3e04-8514-e04d938da613 | -11.15834 | -48.37949 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed458915-0096-3d5d-a3ed-d5248f98b33f | -9.61032 | -47.88934 | 2025-09-07 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c820d41-e900-33ab-88f0-1fa325c12dcb | -12.54844 | -48.07478 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 077c857a-01db-3d1c-adba-398e97b8bad6 | -10.16261 | -46.22349 | 2025-09-07 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 062f50a9-0306-3d4b-bbfc-f8bf5855766a | -10.3396 | -46.40098 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfd7cf78-fee3-30ff-adcd-d4b19b478101 | -11.48419 | -55.54808 | 2025-09-07 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83eeb539-da3a-3676-b829-cb44fc138f29 | -12.82164 | -48.01842 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db181403-8ff6-35c1-8276-7f563ad4fd34 | -11.0213 | -52.03839 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e6caf28-7db0-326b-98fa-91e3f7748096 | -11.1795 | -55.04731 | 2025-09-07 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88f83fbc-7101-3707-9f21-3238bd7404c0 | -10.35183 | -46.45965 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4db13578-f185-321c-945b-edbd3b9427ae | -8.6888 | -54.66792 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 906a66a1-1b64-37a5-aae9-3083592f6b52 | -13.02687 | -48.07862 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aab7e9c-5d32-3550-a752-c1578fd295df | -10.72635 | -48.59544 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 848f9d0e-d88f-37fb-ba2e-ecc81d4fee37 | -12.19566 | -53.90693 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57126b43-32f5-3d29-9fda-e2db7befa7db | -11.58666 | -47.17126 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c57d150-8e58-3fcc-b39d-bddd0cfdd268 | -10.58031 | -61.23711 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f5ff396-b359-361e-8c03-bb1206e504e2 | -10.17349 | -46.2413 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d9fdaf-eab7-3567-a1cb-6f7e23791042 | -11.76165 | -47.74762 | 2025-09-07 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc943d31-ff33-32b4-a0fa-5d670c408b9d | -12.81568 | -48.0177 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 166f829f-8d7b-387e-8736-b10120c7135f | -11.58765 | -47.75604 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README70.md)
