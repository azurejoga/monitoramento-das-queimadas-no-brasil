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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a15324a5-51f9-32a6-baaa-3598d78307d9 | -9.14126 | -59.64924 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1eaa5a7-3756-37cf-b8a2-d9af9fcc4b34 | -6.84364 | -58.97429 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d260843e-0bf4-3499-af3a-48f578543d9a | -11.47891 | -46.59673 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4551669d-1259-3976-b349-dc7251ed41f0 | -3.73902 | -55.97492 | 2026-08-16 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f488c4df-a121-3ec0-b8f5-8799917f46e6 | -7.41898 | -60.01216 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 98c41d01-eea5-396c-9c9d-938335a539a6 | -6.59923 | -58.9865 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9041ab91-ccfe-3769-8103-28d7aae76ee9 | -8.90071 | -60.56555 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 042750a0-29e5-354a-a9b7-9d0fef6e1c1a | -11.49009 | -46.60215 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fb054be-aa32-35f6-8d52-2a5977ffdbf3 | -6.83036 | -56.43826 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad7d6c32-26ab-3e83-9767-fe7345ce0eaf | -9.30158 | -56.81688 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe7f62df-8fb2-3762-8502-a9716bd75192 | -12.03603 | -46.44935 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94693f81-df99-30af-ae65-174f7a378234 | -8.98508 | -60.52037 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1eb20302-62a6-3ac5-998f-bceb016960d1 | -11.48426 | -46.60147 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 939b4638-a6a6-3f24-ba73-126d9fcafb49 | -6.40081 | -45.69453 | 2026-08-16 05:16:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51600b27-a06a-369c-834f-a5407a1a748a | -7.53397 | -55.58822 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80193351-d5bd-33d7-b6af-d60bb78f94ca | -11.51219 | -54.6344 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439685dc-a471-3abe-bcc2-133049b23458 | -6.6302 | -59.06818 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd7f1cfd-2cc6-3285-bdaf-2c5b7376ffdf | -8.95701 | -60.52515 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| e26aafe4-04a7-3a5f-997f-c30c125df941 | -6.96375 | -59.28945 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6968846a-3538-3c05-aee2-df63e9a20374 | -11.0497 | -47.25252 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6d4328d-bf30-34a2-9fca-bcc64c68c28c | -6.92673 | -43.63345 | 2026-08-16 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7048097e-1a44-3158-90fc-eb3ec4f87763 | -6.81928 | -56.44363 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc0a70ca-f5d3-36fe-895b-45c38aa217b3 | -12.03652 | -46.44513 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74989feb-46e0-3cbc-abd2-699976f5e70b | -8.43154 | -62.66571 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 112a79b8-e202-3ff0-86e3-cc5fa7cb47d6 | -7.88741 | -63.75504 | 2026-08-16 05:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb9f8512-d084-365c-b22b-05671bfe9478 | -6.69533 | -58.95039 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5ec21ad6-b2ad-31ab-9380-41aab7f0ea54 | -6.64855 | -56.41238 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13d982b5-202c-3edf-9a39-21502923cd92 | -6.88024 | -56.50681 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67a3579b-a801-3d1e-b8fc-4f6b11fd58c2 | -3.50207 | -59.58167 | 2026-08-16 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdb23e52-9278-3f1c-81ba-8ff235688451 | -6.84973 | -56.42352 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c68b0a5-8ee5-36a8-a102-644f5d1b78af | -12.01665 | -46.43524 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e879a45a-0d1d-33b3-8886-3887c7739a90 | -8.96052 | -60.57368 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f111d4a-6444-39ba-8f4f-7654803a56ad | -8.89333 | -60.60059 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c38b363a-cccc-3f93-8c45-5d5d7eb7311b | -6.867 | -56.41908 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06991835-3543-358f-bfb3-83c87df22075 | -8.66935 | -54.76067 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34b3a6c7-21c4-3ed1-9f09-584b41c3ed79 | -8.65 | -54.72749 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f4603da-db27-3f88-9988-75e3fe98d197 | -6.71367 | -58.92845 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 864f7ffc-12b0-3452-b458-8afe3fe202b5 | -7.83917 | -61.34673 | 2026-08-16 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4705ef1-8d5f-3ddb-b58a-02b240c638c4 | -6.62142 | -59.0539 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83700dac-1913-3d85-b996-fca034b7f891 | -8.95923 | -60.5351 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5668f1ff-dbcf-3b69-b5c9-18cacd031dba | -6.96153 | -59.28043 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc1f7be-2250-319d-804f-bd3b471a2e7f | -9.37366 | -57.36464 | 2026-08-16 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63dce131-0eaa-353b-854d-095099f80642 | -8.66251 | -54.73701 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ba8e64d-3269-3507-94f5-ff9cb67fae29 | -7.09518 | -55.45101 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab506b63-7c0d-3122-be57-f3cd9ec67afb | -8.95401 | -60.51987 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 78e32bef-7be4-318b-94b7-eb2b784b2383 | -6.78592 | -55.84445 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a0fb151-745c-31bd-8b92-9921ab50abc3 | -11.71165 | -49.07768 | 2026-08-16 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bde0d81-fd8c-38e0-9ce5-4b7264183ec0 | -12.44933 | -46.64996 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54daef4c-de57-3221-b5b3-c208a8d924fd | -6.64523 | -56.43326 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beeb5503-0c1c-3f74-ba11-dd87f4a9d93e | -6.72306 | -58.93839 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9700302a-f710-35cf-a836-3913f096e0fb | -6.79281 | -43.02808 | 2026-08-16 05:16:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bf8e7dd-b172-3ebd-ab39-98b85ec72609 | -11.82866 | -51.79968 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c9ed3e4-66c6-3ec6-8d61-604aa3392d96 | -8.9578 | -60.52051 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8afdedf8-a543-3df4-89f1-ff4299a8bd54 | -7.49645 | -60.0796 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e4f578a9-a54b-376a-9f08-15c6fa2d199e | -6.11479 | -57.71782 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f360bed3-88e0-3f50-a2e4-7f36185e6e34 | -6.58931 | -56.35661 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a107fde-cce4-3ddd-9413-a7893250ef13 | -9.26801 | -56.90487 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5f7d02b-11a8-31c1-9db9-a8ac470871ca | -9.08375 | -61.40096 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d31a75c-8781-39b0-94d4-7e2979512fb3 | -11.89916 | -45.96859 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 088b3ca6-15e3-3f89-948e-83baeba99a57 | -8.97906 | -60.50983 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| edc05415-fd43-35df-8020-49e21ea2fe33 | -6.85863 | -58.97257 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77c14e73-0833-38a0-a837-cbb67408f9f1 | -6.7837 | -55.83698 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec8cb15-4d9b-38b7-a036-e89a2e3f2ee9 | -8.35551 | -45.97948 | 2026-08-16 05:16:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f320bd5-7e2e-3aa9-8574-3040a748ab0f | -6.6187 | -59.07054 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffdef594-c3ff-3199-b22c-9a82cba277c2 | -6.6001 | -59.00358 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5497e5ef-c061-3e2b-881d-849bf3378061 | -6.84365 | -56.44036 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51152a8c-ee77-3861-8136-38dc686a9873 | -11.47985 | -46.5887 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5345077-4ee3-3b64-86fe-11a701d616be | -7.27879 | -44.72176 | 2026-08-16 05:16:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc767a98-a2e2-3e47-a74d-1b743a2025e9 | -6.97467 | -56.46458 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c2349a2-17f6-308a-bfb8-2659e46e3afa | -12.00054 | -46.41912 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 89bd1331-93c3-37d0-b7fe-63c5ef2f3e16 | -8.60091 | -54.70518 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc5f1ae7-e61a-395b-837c-5bb5dee8ae01 | -6.78315 | -55.84045 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a983e6b-00de-37ef-b3af-15a14dca2f64 | -11.21078 | -54.81366 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b72af18-8002-32c9-b51a-14b5b2073973 | -8.89493 | -60.59129 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90457165-dd71-335e-bf99-4560f70cef17 | -6.81651 | -56.46102 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69a451f4-4417-398a-91dd-0f65ff847bbc | -9.20105 | -59.6753 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb194479-fa67-3f82-bea6-2720300e7d49 | -6.82704 | -56.43773 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95107815-0b76-37d1-bbde-5b9b57001508 | -6.86357 | -56.42218 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a481efa-4b2b-36cd-948d-72f27fca8c14 | -8.44028 | -62.66727 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d71ba981-f4a1-32dc-af6e-984d7796777b | -6.62298 | -59.06699 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ecf5de59-6f58-3611-b15f-b5c7c3c92c00 | -12.01613 | -46.43946 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7635a61a-11e1-33b1-a51b-28bd7c4ca109 | -9.3771 | -62.36536 | 2026-08-16 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7678342c-2d2f-3d6f-837f-933a0d455ac9 | -9.13394 | -68.19894 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8be8fbc8-4d19-302c-9fa8-fc04dd66df91 | -9.10904 | -46.39057 | 2026-08-16 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47d42b6e-ff19-39e4-90a7-1bc67e989ea6 | -6.92411 | -43.6329 | 2026-08-16 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1f0e251-1e45-3643-b6c6-fd8abcea023f | -6.60282 | -58.98708 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01f1a2b1-47dd-30d1-ac9a-c10b134810a4 | -6.61558 | -59.04433 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea43acc6-4171-39c4-a5d2-44c149d2ffe9 | -8.60148 | -54.70148 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30d9a995-66e2-35c8-b4d6-e612934dccde | -8.97751 | -60.51909 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 21f7b850-1f35-335f-94fd-1e3a649df125 | -8.94865 | -60.52851 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aef97eaf-ea70-3edd-b4c6-768feffa8abd | -14.90491 | -46.6437 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 836011a2-461b-39d8-b182-43fa7c138f6d | -14.78172 | -56.95246 | 2026-08-16 05:18:00 | NPP-375D | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9589a370-5b04-3c8d-a6e2-e89b810bc05b | -14.30437 | -53.05692 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2217f69-445c-3346-84aa-87dd99e7fc83 | -14.72255 | -52.88808 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 719d9747-1da0-3c1b-9fdd-7265d5a8e430 | -17.67024 | -50.48915 | 2026-08-16 05:18:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5af8634-2465-3104-9cd7-da620e72d54d | -16.84122 | -49.43667 | 2026-08-16 05:18:00 | NPP-375D | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4c2daef-02a4-362b-a5e8-949bb4ca9c3c | -14.71453 | -52.88705 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3db6e117-b0d1-3b6d-a43d-c281cea1a121 | -16.33301 | -55.38176 | 2026-08-16 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c292cde6-20a8-31ab-aa74-fcef7e2760bf | -13.8089 | -53.77783 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 861de445-0e11-3901-beb3-9e9df5a4632b | -14.32491 | -53.31167 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README43.md)
