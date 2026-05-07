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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d603b0cf-4e1e-3d3c-916f-f82d54f02a5a | -12.9143 | -49.48517 | 2026-05-07 04:36:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1ab936e-9b17-3a82-abd4-a3aa4863b501 | -11.73834 | -54.81342 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 949391b4-5b23-34b4-874d-4295288acce8 | -11.73554 | -54.80468 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20095f29-6f7b-3863-826a-341672a19174 | -13.21512 | -47.88371 | 2026-05-07 04:36:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0692a52e-f326-3e4c-8cf4-92c3d1a82094 | -14.12701 | -45.34891 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db0bfb10-f005-362f-9fec-c9a852ece401 | -18.16841 | -51.10934 | 2026-05-07 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0655c427-3958-3121-bd90-6e35163c7e99 | -12.50286 | -58.47245 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b58c2d6-644a-3870-aa83-69b307d2f5a3 | -11.73624 | -54.80069 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac04d1ef-32ad-38bf-a860-7a4a991d08ad | -11.73133 | -54.80394 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 636ed9e0-24e8-33cc-bfec-7df43d2c7993 | -21.35806 | -45.13879 | 2026-05-07 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b79a39ef-e0e8-3484-af39-8bbca632719e | -23.62848 | -49.29319 | 2026-05-07 04:38:00 | NOAA-21 | CORONEL MACEDO | SÃO PAULO | Brasil | 3512605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7678b40-f7fd-3d99-a749-6a82aa03ebb9 | -21.95172 | -57.58974 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d76fc34-ce1f-327d-8b36-0c05e4d38287 | -18.43682 | -54.70393 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a554d239-2c96-3b89-af70-c2013b9edda1 | -20.79611 | -51.65938 | 2026-05-07 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c66f4221-9869-325f-9ce6-fc49e57bf0e2 | -21.33387 | -47.07645 | 2026-05-07 04:38:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bab10fc9-2be0-37be-994e-003e7edbe8d5 | -22.74417 | -48.2123 | 2026-05-07 04:38:00 | NOAA-21 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f1b8b4f-6c92-31fd-99c2-da484168b545 | -21.15676 | -50.22588 | 2026-05-07 04:38:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 158d2480-00a8-3c72-b56f-e2e268b5c9d2 | -20.23123 | -46.84201 | 2026-05-07 04:38:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5c67a47-292d-3236-aa5c-1aa9dba5c687 | -20.22683 | -46.84638 | 2026-05-07 04:38:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffc674b8-4f03-3118-8608-9b3325b239f4 | -22.97476 | -52.69296 | 2026-05-07 04:38:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7832f451-91b5-39e1-b18d-8f448a244187 | -21.70444 | -48.4153 | 2026-05-07 04:38:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e2f0a564-576e-3aa4-8179-8f7d5146b7fb | -21.33322 | -47.08139 | 2026-05-07 04:38:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc0ac775-8791-3d88-95f8-8d4d8d0dea43 | -21.70798 | -48.41586 | 2026-05-07 04:38:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2e8e7060-3170-3882-a677-76b683a46092 | -18.44346 | -54.71018 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e8f0a3c-8a1b-346e-a2b9-5c32de7cd751 | -18.78428 | -51.93664 | 2026-05-07 04:38:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d5438c8-0828-32b7-983e-321ab59fd87f | -18.43531 | -54.71028 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9afe4779-44f3-3081-bf1a-017fb28059d6 | -20.22744 | -46.84171 | 2026-05-07 04:38:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09a9d59c-8c49-3df2-9ded-941e4c894bd3 | -21.97779 | -57.59068 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e06d7c8-b357-3948-9f3e-6c45c297f0f8 | -22.01275 | -48.42863 | 2026-05-07 04:38:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 048819f8-8848-3d94-85b8-7e2090d8f12b | -18.33161 | -54.52605 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 732bc759-9afb-3b95-b695-cb5be879cedc | -21.97358 | -57.58981 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f322ab9f-169a-3dad-8497-e957d6921cf0 | -22.71064 | -43.32011 | 2026-05-07 04:38:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 035f65fc-20fd-3474-b588-5855a977f813 | -21.97702 | -57.59455 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b09100a0-c3d1-37e0-9a2c-4d1c000ffab9 | -18.4399 | -54.7063 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 519195c8-749d-3228-b0a3-dcc77e48f73d | -21.90584 | -50.73199 | 2026-05-07 04:38:00 | NOAA-21 | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8cccb6e4-41ca-3ca9-a5f7-b92355c4831f | -19.94905 | -54.38086 | 2026-05-07 04:38:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eed65aa2-e780-3ec5-accc-7e4c75ac3409 | -22.74778 | -48.21291 | 2026-05-07 04:38:00 | NOAA-21 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb0cd4b1-8b2b-3961-8d13-d14014747372 | -20.71022 | -55.18152 | 2026-05-07 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9491273f-232b-3c0c-bde4-1d3efecc8aa2 | -18.43907 | -54.71103 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 385342dc-d16d-337f-ba3f-5fa9cb2daca3 | -21.70384 | -48.41963 | 2026-05-07 04:38:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f336a59e-805b-3097-86e1-294600742a64 | -21.95508 | -57.59488 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76075c63-2fe4-35d1-986c-c4ebb885a254 | -23.07977 | -48.61756 | 2026-05-07 04:38:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c46de2-5241-3cdb-b51b-15b9d667eb1d | -18.44057 | -54.70469 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7418caff-79fd-31e1-b8c1-00f6ae7f512a | -23.32737 | -48.86319 | 2026-05-07 04:38:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6579a30-241b-37dc-9ce0-b15df65ed372 | -23.76972 | -49.16039 | 2026-05-07 04:38:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f6a0001-1182-3de6-9db1-bc9d906484f2 | -18.22562 | -54.59591 | 2026-05-07 04:38:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e315d028-05ee-37a5-a659-11f70ceaf8d7 | -18.77972 | -51.94352 | 2026-05-07 04:38:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4faa662d-c38e-3584-927a-2b38f1dd6490 | -18.44432 | -54.70547 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f727db20-8eeb-3a20-92e3-f1942dc3d299 | -20.71394 | -55.18232 | 2026-05-07 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dc1405d-b0ad-3c66-b5dd-e4a14903d646 | -18.44073 | -54.70156 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 58408299-ed1d-3cb3-b6fa-57b7443cd355 | -19.77795 | -54.09179 | 2026-05-07 04:38:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd5fcc7-9cdf-3133-a823-295870c3be19 | -21.95177 | -57.58986 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46a974c5-0f3f-32bd-a73f-e781f7139eaf | -20.71502 | -52.0804 | 2026-05-07 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 615e80a1-ac22-3b92-83ab-d94f244e399c | -18.43615 | -54.70554 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 31d6c927-3254-3aa3-99de-e0889335c1b3 | -21.70739 | -48.42017 | 2026-05-07 04:38:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2146170b-9aa9-3864-8044-b2420b1b9a02 | -18.78764 | -51.93725 | 2026-05-07 04:38:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 530cf087-b86d-3c19-a915-f066590c811b | -18.28808 | -54.12986 | 2026-05-07 04:38:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23b1571e-02be-3454-86c4-52754e34aeb7 | -21.98198 | -57.59158 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb36f833-a605-314a-8cb4-55c8e462a532 | -20.71481 | -55.17749 | 2026-05-07 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 964b224c-6b81-3015-a2fa-d77dcba7e28f | -18.43971 | -54.70942 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2b471b34-64a5-3d96-8a4c-6ba637f97569 | -18.78368 | -51.94038 | 2026-05-07 04:38:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e34aa8f-740a-3148-9bac-ec7ca2eb9f6a | -18.43596 | -54.70866 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43535567-3c22-37e8-820d-50cec2d413ff | -18.44365 | -54.70708 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1d41f85d-baac-373f-ad62-be37a6f905af | -22.97143 | -52.69233 | 2026-05-07 04:38:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 076f21e2-7f3c-3cd6-8088-7ab3f415d843 | -18.43698 | -54.7008 | 2026-05-07 04:38:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cbc7155d-c80e-3601-bb44-a8a921f615fd | -21.4126 | -45.9498 | 2026-05-07 04:38:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f73a8439-5e4f-3442-b601-8920406ff00b | -19.94827 | -54.3853 | 2026-05-07 04:38:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 551b98fc-089a-3e4d-896a-4abf83dacffc | -19.98626 | -49.70303 | 2026-05-07 04:38:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fb66755b-aa36-3602-ad64-326c1860fa9c | -22.0092 | -48.42808 | 2026-05-07 04:38:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20293339-60a2-35d8-a955-352cd745df65 | -21.95592 | -57.59067 | 2026-05-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef2642f3-012a-3f9b-9ccd-041bc5c4df3d | -21.1544 | -48.7139 | 2026-05-07 04:38:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4222369c-945c-37bd-b8fb-c5e3aca0f64f | -5.7792 | -45.12569 | 2026-05-07 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7880070e-f8dc-3e68-a2a2-2680747e96ff | -5.77741 | -45.12176 | 2026-05-07 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb43c2d9-aaee-3be3-b849-31814df330d9 | -5.77649 | -45.12836 | 2026-05-07 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 485691e4-d059-3f13-a0ca-a69daab13c62 | -7.2779 | -46.79367 | 2026-05-07 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a4faa1d-4bb7-3bee-b03f-e1eb2e67f3ab | -8.30604 | -45.39248 | 2026-05-07 05:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1adedfe-44b9-3063-a78c-4270807da1fa | -5.77871 | -45.12897 | 2026-05-07 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bacbd6f-fc58-32dd-b407-d586947dc4e9 | -8.31092 | -45.39752 | 2026-05-07 05:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 539166f5-cba1-35b4-a6af-70ed10cb5315 | -7.15301 | -48.23912 | 2026-05-07 05:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab61016f-3177-3d0a-84e6-8d9db758b0bd | -5.77968 | -45.12239 | 2026-05-07 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c8c22cd-ed92-318a-a1f1-29d3593fc876 | -5.77695 | -45.12506 | 2026-05-07 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6817a6e-4eaf-3336-9172-8f05ffc0a543 | -8.0364 | -46.45131 | 2026-05-07 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cf51a5e-4bb7-3521-93aa-b94221d137c9 | -14.13535 | -45.34866 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2f7a340-b006-3a5f-8ef2-a3ce2769b215 | -12.34712 | -50.01594 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df9d8a4b-93a5-3e6f-9715-18bbd6c6a5bd | -12.35336 | -50.03284 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83b75ab3-7306-3f4a-84ae-07da44e8eedd | -10.63353 | -59.42177 | 2026-05-07 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2844d4f-1ef2-3b32-9a43-613a6f2da0aa | -12.77396 | -59.01086 | 2026-05-07 05:08:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6243c790-320b-3467-8707-1c745c46ac48 | -14.13185 | -45.34911 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cc71721-1f6d-3803-84ac-109e1c83965f | -13.71346 | -56.88201 | 2026-05-07 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eeb5a10-0760-3dbf-a1ca-bf1d2b15fb11 | -12.15175 | -54.64705 | 2026-05-07 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4deea63b-726e-3776-80ee-c8375bbd0b34 | -12.34658 | -50.01986 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c9e24409-8cf6-3f25-8cb2-cfdea03c1cd8 | -13.95841 | -47.54578 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41546e77-2628-36f6-bafa-849c5d7ce479 | -8.68232 | -49.08797 | 2026-05-07 05:08:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 860d1532-2f76-32a5-bb61-365baff28d19 | -14.86098 | -48.55826 | 2026-05-07 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efa99c48-968a-343e-9ca5-510d77d3b056 | -11.61665 | -54.17777 | 2026-05-07 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ab70c0f-3974-3316-91d2-398bce287bb3 | -12.49773 | -58.48394 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2c0d220-51c3-379d-a79f-e77679619977 | -11.48035 | -52.91885 | 2026-05-07 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7800f46-c42e-34ab-a147-cbf0a716d1ec | -12.76599 | -58.99207 | 2026-05-07 05:08:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68a6ce90-8b09-35ea-b62c-1813ae21d7b2 | -13.94102 | -54.80136 | 2026-05-07 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ca93471-8739-34dc-8f79-1e5f79be8aba | -14.03702 | -47.60581 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
