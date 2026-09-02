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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68f7ad55-94de-36d5-b835-82caa497486e | -6.8757 | -59.3978 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 065681b7-bf7d-3188-99e5-efb25a1c5030 | -6.1844 | -57.7395 | 2026-09-02 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| d2cdc1e6-caec-3ce0-90de-b063cbb0df2f | -6.6937 | -58.9613 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a4c743c0-4247-37b2-b005-dc21757bdec4 | -7.2934 | -60.5713 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9addc018-f6ce-310c-84c7-135441bf0213 | -15.3852 | -53.7652 | 2026-09-02 16:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d0ef9aa8-24c1-39ef-ac79-9e660973b101 | -2.9447 | -60.9002 | 2026-09-02 16:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| eb8aa7f3-2826-3a89-987d-f3f85d3aa922 | -3.2361 | -61.217 | 2026-09-02 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 170.4 |
| cecda34d-661d-31d5-86b4-ab3a081238c6 | -3.1267 | -61.1811 | 2026-09-02 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c9b18c06-098b-364b-a451-47fe843d6d77 | -15.2863 | -53.8827 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c11e7e15-bb00-3a25-9a2e-d440028ae5f6 | -13.9664 | -58.6736 | 2026-09-02 16:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e7499d85-f4a5-35f2-a5ab-4f804a26edbf | -7.5293 | -61.3063 | 2026-09-02 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 9e05793f-e70f-3025-85ab-70f837e8bd5c | -14.2989 | -51.7072 | 2026-09-02 16:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7259c3c5-d569-33ee-96b8-9ac43bdb9558 | -10.1267 | -50.3398 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 6093f850-43b9-309a-9cec-4209f697380c | -15.2669 | -53.8851 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ebe401b4-5e9f-3c28-afa0-50d94c078998 | -6.8784 | -58.9343 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 061f522e-25fe-3e01-8406-3cd8a1c6a39c | -7.2007 | -60.6515 | 2026-09-02 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e0bb62ad-f7f5-3182-a9e7-28e158cee6a8 | -3.1998 | -61.161 | 2026-09-02 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e30fb005-32d4-33d0-84d7-a3b822d9eb26 | -7.2192 | -60.6507 | 2026-09-02 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| fd70882d-9251-3f2b-926f-e9a2e34cd247 | -3.8073 | -59.6092 | 2026-09-02 16:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 753a1ca7-a5e5-34bc-881c-b23a6a10d4b5 | -3.7533 | -59.3231 | 2026-09-02 16:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| fa014e3f-929b-3d33-bcc5-90696f4e7d1b | -6.8386 | -59.4379 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4ea44cb6-1821-3e6c-bd8d-6ca74a2ada33 | -7.2933 | -60.5905 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dabd0379-ba4e-3df8-a45e-fc9a93fefe55 | -5.9635 | -57.6899 | 2026-09-02 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3a63d979-0d5c-3020-872d-1fa0096e464b | -15.2669 | -53.8851 | 2026-09-02 16:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d732966c-fec8-3843-b839-1b389f9e3cc8 | -10.1456 | -50.3379 | 2026-09-02 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| cb2bb085-fb1f-3b64-bf21-1510608ca3d4 | -7.3119 | -60.5706 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8e7a3038-8370-3deb-b870-0027dab62797 | -7.2007 | -60.6515 | 2026-09-02 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5325ed6d-8811-3018-93aa-4adcb0040d9f | -13.4519 | -57.039 | 2026-09-02 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f4d93f5c-6c0c-3456-8886-c5cf4e74663a | -3.0347 | -61.4846 | 2026-09-02 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 693d306d-a4df-3985-b9eb-e32dbe63e388 | -8.2606 | -62.7391 | 2026-09-02 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b49ae564-9007-346f-823d-6306a66f289e | -7.2931 | -60.6287 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| bdd2f105-1c8c-35b2-80c9-c9388b38bbf8 | -3.4002 | -61.3276 | 2026-09-02 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 019a5118-935c-3528-a95c-68e95fdaaa11 | -10.1081 | -50.3203 | 2026-09-02 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 38414d02-a407-3959-9ab8-8db63410846a | -13.471 | -57.0373 | 2026-09-02 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 7f880e15-93b8-30d2-9ec5-eb9ae5eea9c8 | -3.6399 | -60.5466 | 2026-09-02 16:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b8365f59-f8fb-33d9-9972-ea51b1eea033 | -8.7842 | -71.0419 | 2026-09-02 16:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 106.4 |
| bf4c7f6e-3b7a-3947-b09a-1fae7e3dc74a | -10.1645 | -50.336 | 2026-09-02 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 0604ef26-1646-3616-a4df-3188a4754e04 | -15.2672 | -53.8642 | 2026-09-02 16:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 1de3a063-ae33-3af6-8a6c-2aeeefcb0811 | -3.1998 | -61.161 | 2026-09-02 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 95d7274e-72ab-3530-8f5a-d4a3b23ff6ef | -4.2383 | -62.2349 | 2026-09-02 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9d5c35bc-cadd-3beb-8219-6ab3225cd74b | -6.7692 | -58.6679 | 2026-09-02 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| a8bfa7d5-ee32-3088-8d3c-612e77c04389 | -13.4516 | -57.0592 | 2026-09-02 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 065cdebe-f82d-39c7-8313-87c96e069ab2 | -3.1267 | -61.1811 | 2026-09-02 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 23ea4536-dc51-32d1-bc46-e127f452c7ba | -6.8019 | -59.4008 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5bb54e11-1497-3ecc-a2c7-36a35111c778 | -15.2866 | -53.8617 | 2026-09-02 16:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| f53c0a9e-250e-37f5-96f8-2ca3a91264cd | -7.2932 | -60.6096 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 73692ea5-7e1b-357f-85af-c9dd211c1275 | -3.0347 | -61.4657 | 2026-09-02 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 44fdf0b2-0836-34b3-b3ea-cd45ed2704eb | -6.6766 | -58.7299 | 2026-09-02 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 1b2f59e5-4c14-35d0-b004-6b62b03296cf | -10.2209 | -50.3517 | 2026-09-02 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7a40b34e-9631-38cd-af5e-72838c9b6a88 | -7.4736 | -61.3656 | 2026-09-02 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d9238be4-6423-3ae6-abc8-5990483f1834 | -10.1267 | -50.3398 | 2026-09-02 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 923df442-2d4c-3682-bb79-ad81a9f63e19 | -13.4707 | -57.0574 | 2026-09-02 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 3be36c93-2715-3cc2-aa8a-3f1d46378177 | -3.4185 | -61.3273 | 2026-09-02 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e3302a32-1ab4-3057-a52e-f3ed5a98d715 | -3.1266 | -61.2 | 2026-09-02 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 560cbb40-2637-3237-9285-76e3fa57fea6 | -13.4134 | -57.0628 | 2026-09-02 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ef7b93c9-415a-3a37-a9d1-7519dfbc73cb | -7.2193 | -60.6316 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 458f1169-c9ee-310e-a6b9-e94e0bf4a37f | -7.1822 | -60.6713 | 2026-09-02 16:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1a1b27ea-7678-3b59-b946-7cb9afa0f44c | -5.9451 | -57.6906 | 2026-09-02 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 6ef933f4-a0a3-3cea-8113-8de49f62802d | -1.4761 | -54.2365 | 2026-09-02 16:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5502bcdd-f28b-3cc5-a802-69a9688358b9 | -7.5526 | -60.4651 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 59fffa73-eab2-307f-b4f0-db90a5dc84ba | -14.2989 | -51.7072 | 2026-09-02 16:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| af651944-5e64-3321-881d-3770cb68876b | -3.1997 | -61.1799 | 2026-09-02 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6c235467-6b68-320c-aa32-ab1467938c17 | -7.2934 | -60.5713 | 2026-09-02 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| dcc05e11-6671-3317-b64a-56c1a2a4e547 | -14.2989 | -51.7072 | 2026-09-02 16:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9c5e8c41-e6a9-3f57-9536-969bf8a705c4 | -7.2933 | -60.5905 | 2026-09-02 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9524fa91-9c07-3c75-ac0c-46fd84d5d160 | -10.1081 | -50.3203 | 2026-09-02 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 631e5277-48d7-376d-8f34-018e3d2c7ad9 | -15.3651 | -53.8097 | 2026-09-02 16:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 896acce6-b142-3039-800c-01faa92957dc | -13.4516 | -57.0592 | 2026-09-02 16:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 1d11674c-93ed-3417-b63e-e327660732ba | -7.2192 | -60.6507 | 2026-09-02 16:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 45e6e457-938e-3ea0-9aa3-7d720f64621a | -13.4519 | -57.039 | 2026-09-02 16:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ebdfbc45-ff9b-3c6c-826c-e3b55e4136e0 | -3.1084 | -61.2003 | 2026-09-02 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ba3c2259-6b94-31cc-98db-617f9b5ca1c0 | -15.4429 | -52.681 | 2026-09-02 16:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 1aea9014-3042-3353-aa0d-810e31f65bb6 | -7.4736 | -61.3656 | 2026-09-02 16:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0c3dcee2-99e9-37e8-8556-ec1fa5595f49 | -3.1265 | -61.2377 | 2026-09-02 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0bc0ece5-5c49-37b8-a06e-33df763c8283 | -7.2934 | -60.5713 | 2026-09-02 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d906d33a-47f4-32e8-b744-1f5cf7d6d52e | -3.1267 | -61.1811 | 2026-09-02 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 11e8528d-dbe5-39e5-8f3f-09f975a102f1 | -15.2866 | -53.8617 | 2026-09-02 16:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 0525dcfb-ce1c-33af-8d58-e7281022e0ea | -10.1535 | -45.721 | 2026-09-02 16:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| ecc9c8b9-ddb9-3faf-acc1-f92ebe887d76 | -15.2672 | -53.8642 | 2026-09-02 16:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3a71482e-b60a-3a01-940d-710c9c76aa52 | -7.1822 | -60.6713 | 2026-09-02 16:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6c4b026a-4467-319a-8827-97b3b8995004 | -15.2669 | -53.8851 | 2026-09-02 16:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2ffda4c5-0934-3bf2-b7b5-a905097d470b | -7.3119 | -60.5706 | 2026-09-02 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 29bf7453-1abb-3347-bc57-be25c222f9a1 | -5.9635 | -57.6899 | 2026-09-02 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 28e65436-0f3f-377c-810b-209b5373f8ad | -3.4002 | -61.3276 | 2026-09-02 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a5938897-3d1f-3f6c-97c5-d69d5abad8ff | -3.7533 | -59.3231 | 2026-09-02 16:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 33c9afe4-766c-3ad1-b70f-f71dd36baaed | -3.4185 | -61.3273 | 2026-09-02 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0c287414-a269-3d2c-aec4-d0275b10355b | -3.8073 | -59.6092 | 2026-09-02 16:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 74aa0c8c-85e0-3986-a573-516afa33abcb | -13.471 | -57.0373 | 2026-09-02 16:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| affe6d77-0d8c-3f52-9e82-c062c2f1006e | -3.0347 | -61.4657 | 2026-09-02 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b46285ef-5616-3e00-80bb-1a43fa12a76e | -15.3841 | -53.8282 | 2026-09-02 16:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 97ea38bd-0d1a-3db2-bb32-42a40fe6582d | -3.1266 | -61.2 | 2026-09-02 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ea43cad2-cd1f-354d-b0f0-b6397d8a2efc | -10.127 | -50.3184 | 2026-09-02 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 11e80448-cac1-3fcb-b94b-d0c5ea8f5fcf | -15.3651 | -53.8097 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3a444fe5-b6af-3935-935b-c4500f75c33c | -15.3841 | -53.8282 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 943f806f-94df-309f-bdac-bb3b3293cc74 | -5.9635 | -57.6899 | 2026-09-02 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 75db9273-349c-3b45-983c-c73d8bf50d30 | -3.2361 | -61.217 | 2026-09-02 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 75b73fc0-5258-34bb-9260-917b85a0f530 | 4.1131 | -61.2949 | 2026-09-02 17:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d64d84f5-9ac2-39bb-82e8-fc7a004e16e1 | -3.0347 | -61.4657 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 270abec7-5d30-3409-930b-a84fa2f83335 | -3.4002 | -61.3276 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7a0ffbbb-822c-30a9-af26-165b8cb8daf5 | -3.0893 | -61.5403 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |


[Clique aqui para ver as próximas entradas](README90.md)
