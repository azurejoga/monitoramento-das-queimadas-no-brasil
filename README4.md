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
| dc8f23ca-2da5-3674-99ec-17b215858b3c | 0.57585 | -59.91213 | 2026-03-22 04:46:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80723073-c765-3981-82e5-6972f36cc623 | 1.25304 | -60.44874 | 2026-03-22 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6f70eac-41ca-303d-b1f7-0d02eb5a5502 | -11.3307 | -55.29285 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3ea139e-d3b4-3632-9ccf-1a4f5b1d05bb | -11.32355 | -55.29167 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c80652a0-43c3-3660-b9ac-cef3fcbec3aa | -11.32571 | -55.30052 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c0c097-7545-3ba8-9473-fe5bca337cd5 | -11.31997 | -55.29108 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 23bdcb8a-0e9a-394e-8513-74b5ddf99640 | -11.32682 | -55.28083 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee2dbc9e-66e8-349e-b284-d4ff6d15f750 | -11.32496 | -55.2834 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5739ad1-69fc-33d2-9923-0d700fc59cce | -11.32642 | -55.29639 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1373c4d8-a2b2-3cf2-b122-4231410555c3 | -11.33567 | -55.28524 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4973a51e-c32f-395e-b839-899282e09d6d | -11.32068 | -55.28695 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 912ac568-e018-3255-b323-919f05cc2e43 | -11.3321 | -55.28462 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ab10fa3-61e4-3682-8291-ff5ec3928a46 | -11.32188 | -55.28852 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7f901e4-6ace-318f-bef6-0d2800c0782a | -11.3212 | -55.29266 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7faa2e49-9db3-3b5a-9287-c34d76994883 | -11.32257 | -55.28437 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f94a1c98-9d20-3f6b-9ea4-516637b0f3c9 | -11.32614 | -55.28496 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1f3295a-e5d7-3c70-941c-f21a34ec3b46 | -11.32853 | -55.284 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e124d65d-2a9a-3094-8092-098dce47caba | -11.33923 | -55.28587 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c9faf2a-5bab-3bd8-801a-a5ecde7d74eb | -11.33427 | -55.29346 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc71899b-4c2f-3db6-b210-b998ddbf6595 | -11.32567 | -55.27927 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6717ce8-dd07-310d-b3d2-12fef03718a9 | -11.3314 | -55.28873 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c450e05-d3f2-36c5-bf9e-95222ea9b528 | -11.33497 | -55.28935 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32809fa5-71e1-3f98-9351-c8b64046553e | -11.32426 | -55.28754 | 2026-03-22 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb95b722-092c-3db1-9181-cbd637cc0057 | -25.54322 | -52.9213 | 2026-03-22 04:53:00 | NOAA-20 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7cfd169f-a940-363e-aa28-fb70342ca8b9 | -20.19685 | -46.50148 | 2026-03-22 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db53606d-4701-3cc6-9fa7-63cb63f82b8e | -22.16148 | -51.36707 | 2026-03-22 04:53:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6b9e7ad7-f4f8-3993-8184-15c295f29086 | -21.66601 | -56.31908 | 2026-03-22 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c93c12-b29f-31d6-b93e-b6c9add6f8c2 | -19.98991 | -54.73847 | 2026-03-22 04:53:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49d0db18-bc5f-30d5-b48e-62e919444cd5 | -20.89937 | -48.80869 | 2026-03-22 04:53:00 | NOAA-20 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 904eab5c-2dd9-33fe-a149-5cf77003e443 | -23.41018 | -46.43504 | 2026-03-22 04:53:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8e1352bf-f727-36fe-b15d-a5e7fa07c292 | 2.64391 | -61.28524 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77aaefc2-eb44-385e-b771-5fd94defc44f | 0.72316 | -60.28917 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8afa5d49-e0d3-3e8b-9f14-f72a9fbfe51e | 1.97607 | -60.57017 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7dadf3cd-3eae-3bac-95ae-00d54da2d24c | 0.85124 | -59.98941 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296e0c40-c373-3f98-868d-dccaeb18a752 | 0.85066 | -59.98568 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f307545b-be70-3f2d-8a23-0662af0d7d82 | 2.65045 | -61.30532 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 460d3060-381d-368d-b47b-69378956ee03 | 2.78048 | -60.31401 | 2026-03-22 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b4faa2-7aea-3e4d-99cb-f9e943e80f07 | 2.06305 | -60.21323 | 2026-03-22 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a538ada8-129b-3205-af1f-448f4abeeaee | 0.61444 | -59.86683 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d86850b-8079-3edf-9805-00634a084230 | 1.03669 | -60.52265 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0567d8af-f725-3736-b0ce-973da7bde533 | 1.41741 | -60.75859 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 717ed587-2f34-38e9-8635-4f2eb4b93874 | 1.04566 | -60.35861 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74cf817-a7e4-35ed-97dd-082e72f056a1 | 2.05593 | -61.80993 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712fd93e-5990-3e89-ae8b-1b34e4e100a4 | 2.64829 | -61.2916 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| a27cdf90-fc4a-3621-befc-41707fbb56a1 | 1.86195 | -60.45017 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bc6d823-00c7-31f8-9174-90ace14a1e58 | 0.66103 | -60.60641 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66bde6c4-5e54-3681-a6f5-d368ef06bf11 | 0.57488 | -59.90792 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc87336a-4ea8-3e9f-9efc-2676ed79b926 | 0.8478 | -59.98995 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 062c8602-4946-39a4-9a6a-c739ce562442 | 0.75203 | -60.54806 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39776730-88ff-38e7-bdfa-4d62a3466155 | 4.78789 | -60.6572 | 2026-03-22 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22b1465-0679-35ae-8990-db98ad410c46 | 3.59554 | -61.73207 | 2026-03-22 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59ec4d3a-906e-31af-af26-29eec8e9987a | 0.98392 | -59.37706 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 38246b5f-f1ee-3558-bbda-d1da8f02b181 | 1.94884 | -60.78408 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db56d85c-683b-3e5e-80f6-36a931bfcc58 | 1.7327 | -60.53922 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf133ca-e71d-359e-8580-77cdef930cf5 | 1.04227 | -60.35915 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a561c9d8-f508-3e34-86e4-67add229f6fe | 1.55229 | -60.25132 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 823ab259-cbd3-3e35-81b0-9b353a7efd34 | 0.99096 | -59.37594 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2ccff5e0-b9a6-35c7-b6b8-f9fc5a33030f | 2.65213 | -61.29451 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5e137be0-40ee-3839-bc4c-d25a1c28a0dd | 0.62171 | -60.27057 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1858da08-f433-363b-ba4c-9f283b7aeea1 | 4.19938 | -61.43644 | 2026-03-22 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99b64677-d057-3e5d-a810-4ccccb1e5e67 | 2.65381 | -61.28369 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ff4b0f-d607-3713-9ba1-bb785c706fbe | 3.56978 | -61.71849 | 2026-03-22 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53b9bb8f-13d1-3e8b-9bf7-1a469a8b6864 | 3.26118 | -60.53812 | 2026-03-22 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b135fc5-fecb-370f-b13b-b207406db334 | 2.05922 | -61.80941 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6412013d-7148-348d-83a3-4c9af3f07f5d | 2.05646 | -61.81335 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff4f2b2-98db-3447-bc18-cb03efad5686 | 2.72646 | -60.57929 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89a78c24-5de2-3499-b932-e93c1f5c34cb | 1.64345 | -60.29256 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d94351b7-761a-3fa2-a56f-6e10ce3cd30c | 2.65051 | -61.2842 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 991a9302-ced5-34f2-bc89-db51ad78471b | 2.33242 | -60.38747 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b371e6b-25eb-36e5-b017-46bd0924a62e | 1.54891 | -60.25186 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a917aa0-ee92-3b0d-b86a-83d96961cea5 | 1.76679 | -61.33495 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6af398b5-608b-3c37-824f-5e5aefd5eaf8 | 4.78405 | -60.65424 | 2026-03-22 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33bf84e2-6cfd-3956-8e65-c24091e2c660 | 2.59334 | -60.5968 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c75a56a5-d9e3-3723-b950-7b38ba84b7e3 | 0.98102 | -59.38155 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 423cad84-9519-3c32-a33b-11fab0fd3209 | 0.9804 | -59.37761 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5bca796d-d8ba-34ec-9ca9-d6970c8bcf57 | 1.08073 | -59.73151 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2dfe06e-ae68-3809-bf65-6c9585cf485e | 2.65321 | -61.30138 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 69042d41-3432-3d73-86b3-29fb19a44f4c | 1.99447 | -60.55642 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c181337c-4f78-3abe-a514-ed33085ef511 | 1.55173 | -60.2477 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e31165-fb75-39f4-978a-c9497d015436 | 0.86049 | -60.22697 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 212f251a-e30c-3d29-b5e8-a601c1b5492f | 0.9928 | -59.38778 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 493e840f-eac1-3a2a-a2f2-d002693cc056 | 0.99157 | -59.37989 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 51a1686d-e7be-3d9c-8211-b3b80fbc73b6 | 4.78735 | -60.65375 | 2026-03-22 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f5755ea-74fc-35c3-91ee-63a2b4660f9c | 1.27756 | -60.11012 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e449874-e21f-3ac5-8eaa-fbffa4c8a978 | 1.8012 | -61.2307 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69b1524a-367c-31e3-b151-0a1c58b676a3 | 2.33577 | -60.38697 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15666983-a176-33bd-9136-dc60c233e208 | 1.64402 | -60.29618 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22af071d-74f2-3353-9e51-9af288144ab5 | 1.34506 | -60.02475 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05b1a681-1927-30cf-9ac9-cf54916cfb40 | 1.15948 | -60.29344 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e6f62d-015d-3030-9fe9-75a065a24193 | 1.73042 | -60.53942 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e7bdde-c440-3df6-b7d8-761354d9c180 | 3.22857 | -61.19643 | 2026-03-22 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30102f0a-e445-3248-a3d0-0bb1c8557242 | 2.64499 | -61.29211 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17f97b69-1554-36f6-8366-a1512b9d83af | 1.41685 | -60.75506 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3b7c314-9986-35f3-830f-bd48bbf5bff9 | 2.04171 | -61.26747 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eae03b9a-5870-3466-a8ad-6934d7e1a564 | 3.27006 | -61.19695 | 2026-03-22 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a5449ea-bdcb-3e46-8435-b33e272b454d | 2.64553 | -61.29554 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a6416449-54b5-32ef-88f4-f35f38f79db4 | 1.9546 | -60.62466 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ae50de05-687a-340a-86bf-620622ee903a | 2.65159 | -61.29108 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 0df03f15-b8cf-35ba-b9d3-bf854ea03ae3 | 0.86056 | -60.24953 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 938c3481-fd11-3cba-a93a-5db302022f37 | 1.21031 | -59.97297 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README5.md)
