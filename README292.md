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

## Dados Diários - Página 292

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10b114cc-7c4a-3e96-929d-ced13016520b | -7.88544 | -44.96247 | 2026-10-08 16:20:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 571a5837-5634-30ee-a38a-f94e793fb7bd | -4.18966 | -40.40063 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b2d592f5-21e8-3e28-b764-eabe2be551a0 | -6.41037 | -44.94889 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 892bf135-a8f6-3190-9bf4-7fecf0c0e0ec | -5.50151 | -40.53916 | 2026-10-08 16:20:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 53d41440-9e64-3a45-aaef-da1b526be834 | -6.17946 | -44.95749 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4efd72c0-d4d7-3242-8ffb-eef6f193920c | -5.51316 | -42.83025 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 81673dd3-d438-391e-b464-6209d97d392c | -6.05961 | -42.92172 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 207bdd12-40ca-3ce9-b66a-4a7d0b47c588 | -5.98314 | -41.35826 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0282286c-e208-3b93-9d29-a9f3c71f3f67 | -3.44444 | -45.0994 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 762298b4-11b0-30e9-8e7c-74d0f61d76c7 | -5.10011 | -46.22437 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 7207d57f-3bf9-3c9e-9e57-05856ea8ac19 | -5.9292 | -43.88807 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0e5e8636-6be6-3dd2-946a-0c3c3ec69575 | -3.02109 | -54.04097 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4c91cca5-7166-3f2b-b82b-04e4760aa591 | -7.73747 | -49.59608 | 2026-10-08 16:20:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f1344c89-95cf-35b8-8081-942407bb5c74 | -3.85482 | -44.11834 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 373635c5-c2c0-35ab-8e6d-e07c86b2e7ab | -7.96571 | -47.26909 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f376e77-c523-32b0-962f-464c1869ee4f | -5.5162 | -42.82548 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a3274c19-767f-393d-a71c-ea11367cfb62 | -4.3382 | -43.16055 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d19c4e2b-990b-33c7-8ce8-c3ac45872ca1 | -6.15236 | -52.64851 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 0386ff61-8979-3594-81c4-631eac3ff2dc | -6.43939 | -45.93537 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3ef2ede7-d13b-352f-800a-92d8d8df2ce5 | -8.18668 | -45.76577 | 2026-10-08 16:20:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 52539eff-2e64-3416-a86c-0cd15d73704d | -7.56443 | -46.70882 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 47ead8bd-f7eb-3ddb-bf00-92e21a70da86 | -3.17485 | -50.5899 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 397e6ed0-4da0-3b7a-92d5-0afb1a64a10a | -5.6284 | -45.79925 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5ff16a35-c6ef-3840-8fd1-3db713d40b84 | -6.36254 | -42.90736 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 70aba086-06f7-3aef-81dc-ba66c87856a3 | -3.51886 | -44.32279 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ea29d27-4407-3c4d-9be9-cc7fd1e82a01 | -6.20024 | -52.85011 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e6ae4a5e-9e37-3965-a17b-77ae32a7188e | -6.21955 | -52.77976 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d677e3b7-fdc9-37d5-acc7-13021638dfab | -5.70555 | -41.73925 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9d5c73e2-08c9-39cc-a671-a83d81484982 | -3.26605 | -54.02571 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 68c10f3f-6d1b-3593-aa54-352216656f2a | -5.69305 | -53.48902 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dbae4193-bf9c-331e-9444-1f4d417fecc1 | -6.67567 | -45.58477 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 289ac46b-e71d-3c3e-9e45-a4264cb7caaf | -3.14861 | -53.72282 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39c2d657-03be-3862-bd1d-fb4c00831291 | -6.3338 | -46.94777 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d1526acf-02a3-38b3-ad05-5b2f1063abef | -6.1286 | -47.93464 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| c8a583d1-ddb9-39cc-b45b-a3f94e9419cb | -6.81705 | -38.5301 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 0541970a-a9c7-33d5-a2ab-693bf9784743 | -3.43929 | -45.09285 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ae370046-8a3a-345d-a6c9-ede9a4154cda | -6.19615 | -51.43298 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2f2d1bdd-a5da-3983-9fc8-9ba9c57b2cdb | -4.29509 | -48.60248 | 2026-10-08 16:20:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8ae981a7-659f-3796-b5e9-b7f8229ec4c2 | -6.58876 | -41.58102 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 26d6c22e-7945-3700-96c5-81080ce82393 | -5.48339 | -44.6056 | 2026-10-08 16:20:00 | NPP-375 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 95ffb4b3-11af-32bd-9901-570ef1dbb3d4 | -6.53419 | -45.40576 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5a85cdd0-d3ed-3f17-84e6-5ef716184686 | -4.44146 | -41.46924 | 2026-10-08 16:20:00 | NPP-375 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 628bce46-f635-39ac-b194-1a23ad590dd4 | -4.16597 | -40.77844 | 2026-10-08 16:20:00 | NPP-375 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d6d60df-39f5-3438-9025-32df9b0a3512 | -6.67484 | -45.35677 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edd032ac-b02d-34ff-abd7-d7c284a50b7d | -6.53362 | -45.40162 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9795aabd-ad6d-33fd-b2ed-2d61bc08ae50 | -6.34017 | -43.94511 | 2026-10-08 16:20:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56de8f8f-dc75-33bd-a57b-ed8009b782f6 | -4.08667 | -44.10938 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 281.1 |
| bc4e84c4-b15c-3b0e-b566-1e3250cbcd4e | -5.53165 | -45.2082 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec977697-3649-3d51-9631-1889cdb661dc | -2.40553 | -51.30029 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 12f94d76-6fbf-314e-aa77-a3244a13f273 | -4.08016 | -44.10345 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 08e42554-e245-3c04-aa98-bdd662d10dc0 | -8.21473 | -46.41186 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 13033930-7913-350d-a261-ba5b5486fe6f | -3.50658 | -42.58854 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 21ea6a69-d3de-3a7a-a4ad-79ff6b5dbcfb | -2.76246 | -54.11372 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c8c0c38-cec7-3385-afbd-5a2a546e98d5 | -6.82551 | -46.42434 | 2026-10-08 16:20:00 | NPP-375 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f8ec078d-e16e-389a-af9d-c4841e42c0fb | -3.15439 | -43.03329 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96bf00c5-a90e-3c45-a712-5db1cf6de244 | -6.32359 | -35.12889 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| a7173ba7-6252-3a6f-891a-a711aefd034d | -5.23611 | -36.87306 | 2026-10-08 16:20:00 | NPP-375 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c1ed67a9-9a31-32e0-a104-c1f123fd2d3d | -7.48726 | -42.82679 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 97a1cc18-e29a-3615-8a98-71085e2b1b3c | -6.16896 | -44.85452 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 19af50f5-23ef-36e6-b59f-c0b41f86f343 | -1.95389 | -54.05281 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0540b95c-f37f-3eb4-a142-112e07a82fb8 | -3.7791 | -41.79241 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 25a7cb2a-da25-33bd-9276-1c4246f403fc | -3.02477 | -42.92664 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d32e7fc0-37ad-385c-af75-4019ddbb2245 | -6.59559 | -39.0651 | 2026-10-08 16:20:00 | NPP-375 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1d6d39fe-3d97-3429-b18b-e50fdb280133 | -3.19393 | -42.85754 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba722aab-f076-3b9c-98c0-9846d40f355b | -4.15279 | -43.19156 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b05f4543-6d8b-34e4-8612-8f9c1327fd23 | -7.82301 | -44.57516 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 194d93b1-1abc-35bf-9ed0-97e25ebe8366 | -4.08984 | -44.10405 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8970d781-9c14-3701-b3e5-5bf98a42e430 | -3.1674 | -50.45922 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0385dc71-f082-3049-bc5f-59e0d7e98d6a | -6.20532 | -37.87756 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 666bad35-a14b-3aea-b3a2-1b54718a79eb | -2.45118 | -46.02564 | 2026-10-08 16:20:00 | NPP-375 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d7370302-1150-39f3-a969-6f37006703af | -7.59129 | -46.68876 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 29bb50f7-8124-31e5-9c12-be28d06b40d4 | -3.86011 | -44.11457 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 041c8fb9-f623-3295-aec6-dcea6891767c | -2.98854 | -54.08384 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 37d50d8b-d865-3e17-98b3-c18523e7a461 | -5.37453 | -44.18983 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 6836efa9-eed9-3737-9b45-149b3d9ed7dd | -6.58697 | -44.86098 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4ccd9bc0-00b2-3b0e-9e8a-d1f6500fe365 | -4.05702 | -44.73759 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cb022b6-8535-3c9e-b3fb-b2e112fdaa76 | -5.74907 | -41.65087 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 48f6e77c-2224-315e-94e5-21bf8d92dcc4 | -7.03207 | -45.44924 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d10ff540-46fc-3b69-81b6-118bd5f0e864 | -5.37579 | -44.19212 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 889b1dc5-dd92-3c79-bb92-bf2271c33358 | -4.77043 | -49.12124 | 2026-10-08 16:20:00 | NPP-375 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c7f79705-c6ff-31f3-adf2-8fc07f03600d | -7.31294 | -44.00285 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef12a3cc-8cec-38b1-b2fb-507a95644467 | -7.18825 | -44.28958 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 616e709f-1ba8-37e0-986a-8fcaa58f692b | -3.06294 | -53.92463 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 79aa06a7-1ab1-3e89-903d-6d8bd3668082 | -4.944 | -42.72592 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c799d89-20fa-3aed-b336-5fc64995ff02 | -3.07667 | -53.95768 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1a732aa0-d62a-3b9a-8276-e71629b7278a | -3.34819 | -42.49579 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43b80b69-13bf-30f1-bdcf-f299a13bf16f | -8.36718 | -47.66055 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0d3efeb2-e9f6-3d9d-a2ad-5830d1c48780 | -6.96584 | -47.66077 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f9fdaeb5-9fe4-3e7b-8098-86ec2de0645e | -6.38876 | -52.72985 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 40a054c1-95d4-30f3-847d-c8973762571b | -3.00673 | -54.09517 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 52e82028-d5d2-3e45-9deb-f4f923d64242 | -6.82263 | -39.5549 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| af08efad-48f8-3c50-9303-c8223e9dda67 | -6.22589 | -44.86512 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| b447231d-bf7c-36cc-be36-e7377b291a66 | -5.99035 | -40.93865 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 6fe738d8-9b49-328e-b694-a9a58bf84632 | -6.53188 | -45.3892 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| fdbab101-d9b2-309f-a7e9-7301eaccb5b6 | -6.57359 | -53.02556 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 7074b1a3-4bd2-3471-b1db-15d43f122193 | -7.5775 | -46.69604 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 34d614ae-985d-30e1-b486-dd3c489cb9de | -7.77858 | -43.82143 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| ce1b118a-41fa-3317-b604-61d1a03818b0 | -7.86621 | -44.14611 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 43.7 |
| dc2314f3-a059-3162-9803-805bbbc181d8 | -6.92986 | -45.26051 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 077c29ab-9c43-3fe2-97ff-a4a6d87beaf4 | -7.76275 | -44.17301 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README293.md)
