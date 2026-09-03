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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4cd7148-caa5-3245-af27-10d21ecd2f7d | -8.0924 | -50.9642 | 2026-09-03 05:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| c24ec776-cfbc-32e1-baaf-d6ec1c28cc4d | -6.6357 | -59.4459 | 2026-09-03 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| d3744465-82a2-360f-88a9-9a9a21a7b79f | -6.3237 | -56.0434 | 2026-09-03 05:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 07b86286-b0b1-3092-a5b6-54c0dd88280b | -6.6882 | -59.9628 | 2026-09-03 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2c7e3e0f-9cb4-36a9-854c-9ba3201b1912 | -8.0922 | -50.9852 | 2026-09-03 05:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4751ebc1-1130-320e-abf3-00a4128d7e16 | -6.6541 | -59.4452 | 2026-09-03 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 605fe742-a296-31ca-b281-d6143098518c | 0.00948 | -60.59751 | 2026-09-03 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b14fc931-48f8-3f09-8d10-148445d4c428 | 1.09733 | -60.24393 | 2026-09-03 05:40:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61413d4f-2866-35ef-85f2-2c8c02f5d92a | -1.02833 | -53.7249 | 2026-09-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40469dde-8a3a-34fd-95ff-c652cc1a255a | 1.91124 | -60.58169 | 2026-09-03 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb21beb1-564a-3747-ac78-8c8e5946eb5b | -1.02229 | -53.72527 | 2026-09-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 691ea7d3-c174-3669-b945-1beeff04bac7 | -1.0216 | -53.72973 | 2026-09-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee3156f8-bcc8-3a79-84ae-c3da8fd928a9 | 2.02772 | -55.87202 | 2026-09-03 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0142bd-374f-32f5-972d-6bab4aff984a | 0.00992 | -60.59872 | 2026-09-03 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d9b284a-d73c-3364-8735-66b92dc256c9 | 0.00518 | -60.59383 | 2026-09-03 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 765feaec-e47c-39c1-befe-9ed64690d853 | 1.67325 | -60.13999 | 2026-09-03 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e59a715e-6178-33c8-b78f-7c127cabfd30 | 1.66959 | -60.14058 | 2026-09-03 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 421baebc-5603-305a-bceb-06b06930cea6 | -5.25242 | -60.18362 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc6aca61-6f60-353d-bc1a-a078456e20d8 | -3.75447 | -59.32057 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fe2e7c6-6dd0-37bf-950e-3866d4af26f6 | -5.46228 | -60.06203 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cee5cbf1-b46b-3740-ac18-24e16952eb69 | -5.55377 | -60.23152 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 364b365d-35f0-3386-be1b-b6e50e4f32f6 | -6.82006 | -58.86834 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f8f17e4-47aa-303f-9c21-97e044d44768 | -3.61869 | -60.56006 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b786dfd8-8ede-3d66-8c87-5656a4a26514 | -5.21231 | -60.03614 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b530f5a-4b00-32c8-9b9a-ab42cc7d448f | -4.96362 | -55.85777 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ba243aa-024a-3d5a-9315-d2fcc1f5627b | -3.02361 | -61.48154 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc31c6f9-be14-31db-b57e-fdb311942ec5 | -2.95406 | -60.9059 | 2026-09-03 05:42:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d939743f-2528-300a-af0a-a1afd994bf92 | -6.75191 | -59.4362 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc01fe6-e0e0-3aff-b2f5-2b2adf6ec502 | -1.84357 | -60.0038 | 2026-09-03 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08b06b5e-fb7a-3ed1-b8a4-88bc384d81fa | -5.25644 | -60.18423 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72db5955-8c6c-36ba-a2ac-ec2ef33b7f72 | -5.32559 | -60.14332 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef9f8bf8-c594-3496-a3c9-c1277d114f57 | -4.26796 | -55.15601 | 2026-09-03 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1ab51ea-40c9-35c0-a05e-84e14a1f7892 | -4.23781 | -62.2389 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e5409c9-01dc-31ee-9ebf-52fdef38c04f | -4.24074 | -62.24341 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc360f85-9d66-3fcd-9c9d-9532da995a50 | -6.11725 | -59.96539 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3393be7-9a8a-389e-a627-48c35164603d | -3.14608 | -60.63797 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1477882a-30d0-34d2-a691-d2aef7f2c74a | -6.76857 | -59.44309 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28360084-5b6a-334d-9d6a-300dba0f87d4 | -6.42252 | -58.30004 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0c1e0868-be49-38ea-906d-5f4d66f8551a | -3.20285 | -61.21167 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 452cda2e-397e-37ee-ae1e-edbaf5bf3ab6 | -4.4182 | -55.77105 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f84465-6fa7-3aac-ae64-9ad788c01b5c | -3.75031 | -59.31993 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73311628-5a8e-3bc5-8c1f-0baa28cf3c16 | -3.75922 | -59.3174 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97f1b59e-f87c-3706-be19-6f8e533a085b | -4.14912 | -60.69049 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e6d8618-e490-343e-b708-7217b3f0e52f | -3.1251 | -60.70096 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e4d3541-38e7-3459-af00-5f5a5dc5dcc5 | -6.78027 | -59.4235 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4207c247-bbc6-3e23-aed4-b02a12fe909e | -6.67696 | -59.95152 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 780e7a79-b8a0-3ae4-b1ba-78385d8c5406 | -6.68696 | -59.94138 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef49babd-8c37-339a-b11d-e3ee4c7affdb | -4.80018 | -62.85174 | 2026-09-03 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef64d9ec-de87-317f-98a8-8ff089e3a17e | -3.12547 | -61.22841 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cefdc53-0f77-395a-bf1c-611d9d7c1920 | -2.93306 | -54.09643 | 2026-09-03 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56e44e21-5f00-363e-9152-4c223a5fcf98 | -1.51482 | -54.96026 | 2026-09-03 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fec304ae-5ec4-3071-a7a0-dbb12fc3923e | -4.97635 | -55.84549 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ce313b-d206-34e9-87c9-05b088fa4530 | -3.40013 | -61.31783 | 2026-09-03 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 333f4984-4762-3e52-b255-f62e1ed2ee89 | -5.58767 | -60.20348 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb2284a3-d97e-3109-b70f-a19d95de900c | -6.74009 | -59.6377 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5885ad5a-e615-3960-8177-d28237321e12 | -6.2611 | -55.42684 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e60fc5dd-3336-323d-8389-18d20ce0e67b | -6.37822 | -58.28735 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f764c7b4-e883-37e7-b285-fb7aa1a2c1cb | -5.266 | -60.18485 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ee06205-3c98-393b-b2fb-1a5cb8c00d95 | -5.20721 | -60.04268 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b602313-6ac6-38df-96fa-eccbef33d5b1 | -6.83835 | -59.4316 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b05caf7-1d2c-35d5-903e-40ed6295ddf6 | -4.97538 | -55.85237 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05251a76-c148-3fb1-9b2c-9fe20e91f1a6 | -6.68279 | -59.94078 | 2026-09-03 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6fd52ab2-b635-330a-ad30-58391d24e53e | -5.56624 | -60.17548 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce2e8971-d6f7-3b29-8fa3-4f3f1f4b8b8d | -6.31903 | -56.0432 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d2e3ce4-1b1a-398a-a6e7-d13d6e412541 | -6.65517 | -59.44903 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c9ed71e-77f4-3bda-b1ae-82fd7e0d953e | -6.84714 | -59.33903 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f2b626-742d-3166-8b33-cef1651923bd | -6.60037 | -59.11602 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fbea45f-f58a-3d7d-8c44-00477daf876e | -4.40235 | -59.8547 | 2026-09-03 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c788f48d-1ea6-33bf-b86e-700c8b4b8b2c | -6.77781 | -56.41695 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a0e943-7dc9-3a26-84aa-fa893e99ae7a | -5.51059 | -60.1889 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 40d91469-a5c3-3842-a5bf-7e7baffb9a92 | -5.21179 | -60.03973 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23ef6358-eaab-3449-abbc-2b473795b2d8 | -2.41105 | -57.89859 | 2026-09-03 05:42:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 091acaf6-2033-3327-a6f0-641892add4ff | -5.21283 | -60.03256 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a6abc39-4026-34e8-927e-c3c1bb89e3f2 | -4.23841 | -62.23493 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b817574-8d36-3256-abb6-67c5b4fb08aa | -4.97047 | -55.8482 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e163cf54-8eeb-383e-88fa-be7dab18d575 | -5.46688 | -60.05904 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 479855ab-40d8-34dc-b6c2-5da4cb135336 | -3.20692 | -61.23438 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3850cf2c-226c-38fb-840d-79980ac0365b | -3.758 | -61.74919 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdc85a72-ad06-331a-8ed0-082f54fb398f | -4.10272 | -60.65911 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad92784-f902-3983-96fa-fb77da35fc32 | -6.64712 | -59.44383 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55f6aa11-e52d-3a30-b3e8-10c3ba1755ed | -6.74638 | -59.44394 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 057d007d-701b-38f0-bbb9-761afb5a02b4 | -5.20826 | -60.03551 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b83fbcb-7e88-30cf-a88a-dc5c4c77398e | -5.60326 | -60.23831 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e2b5710-8a8a-3df2-b737-0f446cf879fb | -6.11779 | -59.96168 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64fa1277-1cda-3730-b7dc-fa8d00cb8a41 | -6.6477 | -59.43987 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5428aaf3-9d6c-3958-b838-ad78a40b58a1 | -6.76115 | -59.43344 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf8e2952-f9b6-3bbb-8eb6-10b96aa48d3b | -6.77412 | -59.43536 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91db5a40-88bd-3c47-9f5a-6cf545d8ab7f | -6.62869 | -55.24474 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca590070-8dca-377c-9c5b-41dd69f925eb | -6.68641 | -59.94516 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb7ca538-4c69-3819-87b2-81ca5b4e97a6 | -4.63264 | -55.73068 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e8a81c9-89de-3aac-9326-9ff6bc54470f | -1.36204 | -54.63351 | 2026-09-03 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3110678b-3a0f-3378-9a2c-ea3abb84cd71 | -3.59502 | -55.37435 | 2026-09-03 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a3eb114-6ead-3705-b9d4-39382a3b1de6 | -3.38376 | -59.42721 | 2026-09-03 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9af343a7-7f44-3626-919a-f56ad0158c9b | -6.84016 | -58.9706 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c50bbc1f-202a-38f3-8fbd-561b393f24ce | -3.20758 | -61.23006 | 2026-09-03 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 282357e8-e48f-384c-b5c5-2b5a3161a8e6 | -5.16531 | -60.27388 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57a469c2-d80d-3311-82f1-a7d4f2c303f2 | -5.58378 | -60.19624 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9554b33-e182-3c0e-833b-12f6ea42556a | -3.59334 | -55.37564 | 2026-09-03 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ec6b479-0929-3335-b1f7-4408cec1ca75 | -6.30865 | -56.03817 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a23c7e5b-0ddd-3c98-8ce7-8f5feb18f39d | -6.6379 | -59.44666 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
