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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dbe50a9-1418-3bc2-aa7e-5a0098282256 | -21.68415 | -56.32323 | 2026-02-28 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1845fc0b-08a4-346d-acb7-805c600729fa | -21.33484 | -49.11578 | 2026-02-28 04:44:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a26b9c43-ebce-3889-a66b-957523c746db | -21.68514 | -56.31793 | 2026-02-28 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc3ee63-ab29-3e12-8db0-cf3891ed338f | -21.17562 | -56.49578 | 2026-02-28 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e70782a-a6b0-3283-83a7-9427b4872389 | -22.66191 | -50.66705 | 2026-02-28 04:44:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| add9c708-8ede-37e8-a915-0f9320886aa5 | -21.69291 | -56.3197 | 2026-02-28 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76d9e0bd-1785-3731-bc4c-673cc175a855 | -21.17958 | -56.49664 | 2026-02-28 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f65e7e9d-1e4c-3705-94b4-3a214fd7942a | -22.6122 | -51.16043 | 2026-02-28 04:44:00 | NPP-375D | NANTES | SÃO PAULO | Brasil | 3532157 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 20cee0b8-1ab4-36bd-b2f3-22dce7eb9ce3 | -21.68903 | -56.31877 | 2026-02-28 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae275182-7507-3eaa-8420-f06d5c472190 | -21.68805 | -56.32407 | 2026-02-28 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 81b3364d-13ae-36a6-b0ad-543a58fd1329 | -21.69192 | -56.32501 | 2026-02-28 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d9cfa7ab-87c6-30c4-b9f0-6617ec2ffee4 | -22.61104 | -51.16796 | 2026-02-28 04:44:00 | NPP-375D | NANTES | SÃO PAULO | Brasil | 3532157 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 108b8667-08f0-34f5-94d1-d211d04a055c | -23.64108 | -53.21411 | 2026-02-28 04:44:00 | NPP-375D | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b5a6acd0-55a6-3a4e-af91-c42452d1a90c | -22.22341 | -57.09456 | 2026-02-28 04:44:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3baa8543-a668-3101-8173-870b2c51d075 | -22.61495 | -51.16479 | 2026-02-28 04:44:00 | NPP-375D | NANTES | SÃO PAULO | Brasil | 3532157 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44bb5d84-b439-3cc8-9941-192212eadb4b | -21.80173 | -52.72247 | 2026-02-28 04:44:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3f10b62-ed33-3f0e-981c-6c3caea99abf | -22.61162 | -51.16419 | 2026-02-28 04:44:00 | NPP-375D | NANTES | SÃO PAULO | Brasil | 3532157 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f6dbdbc3-baa6-3b3f-b5ee-a8a08dd281ac | -21.17165 | -56.49493 | 2026-02-28 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7e13ef0-b9e7-315d-b691-a2689d6a1bcc | -25.17291 | -49.39898 | 2026-02-28 04:44:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8ece5d76-2067-34bf-b1bf-5a3669baa6ad | -21.80235 | -52.71867 | 2026-02-28 04:44:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6b14e12-2cb4-34ce-a6da-693b74195ff0 | -22.02639 | -49.504 | 2026-02-28 04:44:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ef50f43-50f1-3022-ba3e-edc87cab832e | -28.99899 | -52.49532 | 2026-02-28 04:46:00 | NPP-375D | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d23f42ae-f1dd-317e-9ccb-c8c2fa7efc78 | -29.1769 | -51.03637 | 2026-02-28 04:46:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bbaddb1b-4613-33b9-9767-b9405822574f | 1.87391 | -60.91812 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3f0344b-5452-382a-b824-646fb4ab3c03 | 3.15555 | -59.90963 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f85b27dd-6bb2-3791-ad54-e918a074cfcc | 3.43183 | -59.86379 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0713e800-a404-3bab-8043-00d2177cceaf | 1.51527 | -59.94348 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 084d4d37-05a0-3952-8dfc-0e371dc7959e | 3.4729 | -60.69378 | 2026-02-28 04:57:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9395a9f-2a06-356d-b449-05a04568f3ed | 1.50579 | -59.94492 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2059bd72-0701-3bdc-a4fd-16344c12ae36 | 1.59691 | -60.44458 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e124d486-b078-316b-80ea-f37ccef4ba94 | 3.06224 | -60.27374 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00a7d4a5-f7a6-3e36-80a0-0f3176f280f4 | 3.04975 | -60.05476 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beb10c24-8d2c-326c-8535-c3e3fcd6865f | 1.87809 | -60.91132 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f940e07-597f-333b-b363-87a3cb87b6dc | 4.80683 | -60.16551 | 2026-02-28 04:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39497b0f-fc76-368e-9d4d-aedcd2ded826 | 3.15474 | -59.9043 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 600f145a-16ca-348d-bc7c-91241d3ba7e7 | 1.83952 | -61.12083 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c35398ed-81cb-3022-8483-266ed3dc870b | 3.42698 | -59.86453 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f516e6b-5c5f-3abb-b3e9-1efba67d8376 | 1.51371 | -59.93331 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8642c5e-799d-38d0-9652-12d8eb3a9c56 | 3.42856 | -59.87526 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b8d6391-ebef-3806-8b2b-12ec984791ac | 1.76037 | -61.16781 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 27acc306-15af-3ecd-9325-857775b28073 | 3.37392 | -60.61101 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 651acc04-28eb-34e2-9c58-0e6c30a88372 | 3.05314 | -60.28085 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47cb7fb9-553c-3cf6-a69f-b74fed7f3b89 | 3.04754 | -60.2828 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25d2927f-4f53-3b28-8f59-714571f6e586 | 3.37903 | -60.61027 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c83382e1-c8e4-394b-ad70-73a274781cd2 | 3.37948 | -60.61324 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8757283d-3e1a-3a18-8f98-c036954663a6 | 0.67353 | -60.01614 | 2026-02-28 04:57:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 989feb58-acad-357f-ad76-98ffb8adcccd | 3.06804 | -60.27858 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d9237e7-7ef4-3d40-a5d3-464838a9b23c | 2.8763 | -60.59994 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 840e2f0d-365e-34ee-aa68-855a0e26a27e | 2.88081 | -60.60453 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 594b668d-81c3-3bd1-8841-91cfe10ebda2 | 1.87855 | -60.91433 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87b47394-660a-3189-8a4d-0dfc323fe832 | 3.42777 | -59.86989 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84e60901-f0f7-3ad7-a7b3-33057612eddc | 1.50896 | -59.93393 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a57abdd-eeea-3512-86c6-14cb58883486 | 3.1507 | -59.91038 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed17ebda-b138-3afb-aea6-92be4d46105f | 2.88124 | -60.60746 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99b22ff0-0ae6-3b58-b118-a0c288ef8004 | 1.7552 | -61.16862 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c85d992f-9daa-39b1-a3da-503bff9f4edb | 3.37461 | -60.54653 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7503d77-fedf-3fdd-954d-366f9327c5f1 | 3.05251 | -60.28207 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8f7c269-3f7c-382b-961d-78b760db5f1d | 1.50817 | -59.92873 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9409ede7-7111-3d5b-9156-bc32ffdfbefd | 2.11768 | -60.19819 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 458553f8-2416-36df-81e3-3dd893278b3d | 3.43104 | -59.85842 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d96432a-5100-30bc-90e7-d1c2076ac193 | 3.37506 | -60.54951 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ede6d72-9ca8-3155-9bbe-78bb42980b71 | 3.37924 | -60.54278 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b568ac82-99a7-3873-adec-1db724850b04 | 3.36971 | -60.61775 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08bfd27-f48d-3aed-af52-6310c99d7210 | 1.5113 | -59.94928 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94793053-050e-3ff4-8ac3-e16991236fc0 | 1.49796 | -59.92527 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4febc773-75d2-31ad-8021-1da74575b57c | 1.50267 | -59.92446 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60f747f0-606e-39a3-9b12-211029cdc0d8 | 3.37482 | -60.61699 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11e69733-1a2b-31fa-9162-a52b983c3c88 | 1.87901 | -60.91735 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 361b71a4-73cb-3448-91e4-f49dbe0b3d55 | 4.80726 | -60.16842 | 2026-02-28 04:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9dbfbc1c-242c-3c76-a471-0587ac1d587b | 3.05727 | -60.27448 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 875614e9-6902-39da-a2a7-0f462bb338b6 | 1.51449 | -59.93843 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e893417a-52d6-3631-92bf-baba23ff0caf | 3.4237 | -59.87598 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80c002af-f340-3ee7-a67d-00821fa7c2e3 | 2.87539 | -60.59406 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb139564-1558-3927-be40-22363adc9332 | 1.4987 | -59.93019 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 546cb97f-487f-3962-a5fc-72cb9ebb66c3 | 2.87675 | -60.60287 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 100bfda7-b32a-33e7-b332-e34b6dbdebb0 | 1.50342 | -59.92936 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 241ceea2-1fff-35f9-b020-8b550ba1bb8e | 3.42071 | -59.87784 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a028726-c1d4-3c91-891f-1336f89c0bde | 2.87033 | -60.59486 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0ac9a94-36f4-37f0-a6c7-5e6da33ce6a4 | 3.47335 | -60.69683 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 096dd3c7-7857-370e-9ca7-da39fb091783 | 3.049 | -60.28721 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9fa0d54c-a1b7-3587-9393-6c7a6fd43f3a | 1.87345 | -60.9151 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e21b2782-c8d7-3db6-a2a8-1cd2ebdfab63 | 1.50501 | -59.93978 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22db4bdf-277c-3fac-a36a-4fffb6a504f8 | 2.87445 | -60.59653 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6dbf9a9-b256-3a5c-b15e-ae09c37c320d | 3.15958 | -59.90356 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf7c88ee-d007-3c94-bf4f-f4b9a7ca796e | 1.48863 | -60.90602 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94d77ca5-9c34-3e53-bb88-ad42b1e4d212 | 1.50975 | -59.9391 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97dda4b8-3460-32bd-aa79-c72da6f41e5a | 4.80224 | -60.16941 | 2026-02-28 04:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b0fb8b7-7445-3638-9766-cd40ab2e80ca | 2.88037 | -60.6016 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a629d81-1539-371f-ac64-59b06f4ce90f | 4.8018 | -60.16645 | 2026-02-28 04:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 177786a0-624c-3d88-a56a-733ccd1f4ade | 3.37016 | -60.62075 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d51a6d0-c558-31f5-b8f2-8f9ae7d0d452 | 3.10124 | -60.29662 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f37a1867-8e6e-3739-a6db-705c88ed1cbd | 2.87584 | -60.59699 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d6238bd-f5a5-316c-a3d4-ab03e1877463 | 1.51053 | -59.94421 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5583f43-2410-3e68-bf94-c08abcbf775a | 3.37437 | -60.61399 | 2026-02-28 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8ab75ec-4758-37cf-9fd6-78834039947c | 3.04841 | -60.28841 | 2026-02-28 04:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d7f1481-3b70-343a-88c9-613ff09cb23b | 1.49323 | -59.92603 | 2026-02-28 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02973b70-c86b-3a81-83bd-d69a4f20284d | 1.5047 | -59.9116 | 2026-02-28 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 5681b9bb-1d4d-3f56-ad83-8d8d6470468b | 1.4864 | -59.9117 | 2026-02-28 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 5b1173fa-71cc-3bd6-9f03-48067e1072a1 | -15.07413 | -57.78095 | 2026-02-28 05:01:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bed8ef2d-4a61-3902-8fb5-04dbab5ea69f | -16.58494 | -58.21696 | 2026-02-28 05:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
