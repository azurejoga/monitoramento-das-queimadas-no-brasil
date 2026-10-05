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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11fabeaf-6e13-3afc-a514-b7db0bb6a8b4 | -8.593 | -66.8081 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 182.3 |
| bc598007-2192-305b-b5b8-47cdd3f5aa1b | -9.1259 | -67.7581 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a32f9ed1-77d3-389d-90a8-ea6e8e223fb1 | -9.9175 | -65.0313 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b82b268d-bd43-36ca-87cd-02b651089be5 | -9.1261 | -67.7211 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2a7db1a3-2509-34d0-b07c-6f779f5eb853 | -8.2674 | -71.1215 | 2026-10-05 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a0609362-1833-3e47-a3e3-e96d38972598 | -8.8519 | -66.8012 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 340e9693-cf52-35e9-bedd-8c95c16c18c6 | -9.4751 | -64.3336 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f46086d9-ec59-3b5d-9395-41bf994c4b10 | -8.7521 | -68.985 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 40fb4de7-f65c-3a3b-aefd-f8db1c4acb9e | -3.4775 | -68.9105 | 2026-10-05 18:00:00 | GOES-19 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2f8d8b32-5542-3534-8d0d-e4389dfa563a | -9.1075 | -67.7401 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ab644ce3-6a6f-3c36-a2a7-6d6121089380 | -9.1244 | -68.2021 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f9c1774f-0dfe-3cda-9522-f9b7db0ff29e | -9.1072 | -67.8141 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 268.7 |
| e5111f99-b309-3418-8880-2beb3b6def11 | -8.871 | -66.6521 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2d66d64a-e239-3a85-87c2-028939f927c5 | -9.9175 | -65.0313 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5a20febc-86a3-3ba0-932e-e351a147ca01 | -8.6293 | -66.9926 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 99bb9c57-a3c5-36b9-90e7-e2f02cb5e032 | -9.0769 | -66.1068 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d9553c08-aee0-3392-9bb8-b67782fead8c | -9.1438 | -67.9428 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| cf28f6dc-c523-33e8-bf8e-541acb2fc86c | -2.5353 | -65.8635 | 2026-10-05 18:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 75a03dce-ed93-3105-8e65-bdae84cdad0c | -8.8519 | -66.8012 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 56a647d2-645e-3644-9b3b-249aa81f0a27 | -9.1536 | -65.5447 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a5cfe8cc-3f38-3814-b519-948c79bc2456 | -9.077 | -66.0881 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 138e9f83-5ea7-3a09-aa1f-26eabafc5b86 | -9.0244 | -65.4367 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| bb7547e8-a56d-3ad9-a6fa-d0b851c05f4a | -4.347 | -43.8252 | 2026-10-05 18:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| bd3ad2c0-e201-3f21-b1ad-72b885b75a43 | -9.2365 | -67.9035 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8598521a-ea43-3b6a-ab24-125a14c27db1 | -9.4565 | -64.3344 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 791ebe14-dbce-3809-b799-ae7ddfa4db90 | -5.9606 | -41.3507 | 2026-10-05 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 395.2 |
| eb2eac76-98a2-3ce3-99a3-0d89291abf15 | -9.4751 | -64.3336 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| a1bf3346-ec43-3243-ad53-4c746d963b44 | -9.1076 | -67.703 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 154.4 |
| ba89f87f-3db5-3021-a4a0-8e92c76da437 | -8.5183 | -67.0139 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 30f98a22-dd86-3ebc-a474-43b565c1d5fa | -7.5325 | -70.399 | 2026-10-05 18:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 8e1c528f-31d5-3564-b2c8-72f3209c9adc | 3.36 | -51.3454 | 2026-10-05 18:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 361b2f95-dc93-3ae9-9ae2-964483f97f48 | -9.7498 | -65.0938 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9aea8a04-6daf-34eb-b06b-c36a1e6072a9 | -8.5554 | -66.9759 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 33ed4fe7-55d0-303d-90f8-b1c708c63e1b | -8.8895 | -66.6516 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8b620038-28ce-3030-9355-29ccee33f05a | -9.006 | -65.4 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 43afe79b-1d0d-3330-b714-012851143c8c | -9.4578 | -68.2314 | 2026-10-05 18:00:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ad97cc42-6427-349f-9d45-a81b2b14c0ac | -9.1408 | -64.3836 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e8ee3969-5443-3da2-91d8-0232bb7620e1 | -2.5353 | -65.8819 | 2026-10-05 18:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 181b46e8-952d-3f22-aeed-b879da48e054 | -9.0585 | -66.0887 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ee023f96-5081-3db2-8c05-079778001f7b | -9.7312 | -65.0944 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 392ae86f-1f8d-3c13-9472-c95fec55f98e | -10.1782 | -69.3434 | 2026-10-05 18:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 900812dc-312f-340b-a7a7-fa2d7b3dc692 | 2.0901 | -50.7337 | 2026-10-05 18:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0b31276a-9f51-3045-937d-a550e91d9bed | 1.8038 | -55.5458 | 2026-10-05 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f05f440b-db59-305f-8ea8-6c51275fdd8d | -9.4783 | -67.6752 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| cba1ab31-b7e7-3e30-80d5-af9685a9f351 | -9.0429 | -65.4361 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b027296b-9822-3a46-856f-be871090a5dd | -8.537 | -66.9764 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 50bedef3-8de8-33ab-a6e6-cabe4ec0ac91 | -9.1257 | -67.8322 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 38ba0b43-090f-36a8-9a60-834b3953185a | -9.7499 | -65.075 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 18ddef59-a06c-3757-8a30-69666fc855f4 | -5.9417 | -41.3524 | 2026-10-05 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 180.9 |
| 7d3e3a69-9fef-3053-a4d2-85ebc3edb011 | -6.6027 | -37.8944 | 2026-10-05 18:00:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 100.5 |
| d3efcc67-05bf-34a7-9e97-a4b79891c369 | -9.2366 | -67.885 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2228e7d6-91c8-32d7-8cf2-a26a0eea94de | -9.0889 | -67.759 | 2026-10-05 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| a8f27935-208e-396c-adef-a25a975dc73e | -8.5929 | -66.8266 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 2e10df49-57c4-3684-84f5-0e181aa41da5 | -9.475 | -64.3525 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 323ce9b1-023c-35f9-bd95-6ea29cc3b78b | -8.593 | -66.8081 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 218.5 |
| 3cfda77d-36e4-3864-a36d-a3c2f131140f | -8.852 | -66.7827 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 170.7 |
| a776ebdf-fab4-3d28-b6a7-50420fd38de4 | -7.6805 | -69.9395 | 2026-10-05 18:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| f96bfa25-444f-3419-9afe-d56b019f9e75 | -7.4889 | -42.8059 | 2026-10-05 18:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 1ec9e7b0-4b50-360d-9080-a8b365cfbb3f | -9.7126 | -65.0951 | 2026-10-05 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 392be2b3-646f-3ae7-8413-4165dc6dfbdf | -9.0584 | -66.1073 | 2026-10-05 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 00bd0850-f134-3e6a-81ab-511120e358aa | -8.7521 | -68.985 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2a13b7d1-fd5f-3cc9-ad2f-3e89d1c98cfa | -9.1535 | -65.5634 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3f0d63af-86c3-3a28-b19c-0fdbe765345c | -9.1536 | -65.5447 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e3fd336a-4932-333d-93e2-47499f7ee960 | -8.8519 | -66.8012 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 156.3 |
| d34b1950-2f49-372e-a7e9-4eecbd8a2b9a | -9.3494 | -67.4374 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 212efb61-8d90-3a8d-9991-b0f83d3f9953 | -8.5929 | -66.8266 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| c78ec7f4-c7e2-3eb7-9a5f-bb08067f2246 | -9.0769 | -66.1068 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 384f131e-cf39-373b-a918-df82fcbbe12b | -9.0585 | -66.0887 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3272497e-a46a-310b-864f-e4e018b02820 | -9.1222 | -64.3843 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| e3cc50cd-efd9-3bf2-8cd9-7c955a0e0ade | -8.593 | -66.8081 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 186.1 |
| c188e933-cd8e-30e4-b39a-98af2b8a66c7 | -9.2908 | -68.2723 | 2026-10-05 18:10:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 842ab919-782a-3020-8dba-03575610e141 | -9.7312 | -65.0944 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d5d0bd69-d7db-3d41-8a6d-56c9ae3e05cf | -9.0584 | -66.1073 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a38ca20e-73fa-3616-ba98-cb9331264543 | -10.6087 | -68.6852 | 2026-10-05 18:10:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d7224e3c-07bc-3b75-8e6e-42089231611d | -9.1149 | -65.9006 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3ae7bec9-4768-3a99-92d4-c6cb953e673f | -9.0244 | -65.4367 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e7e4f546-c46d-31d1-9934-3778edeb3901 | -8.5554 | -66.9759 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 45de2ae4-1032-3fa5-90fb-4baa131de832 | -9.1257 | -67.8137 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| fd532302-5cfa-3bdc-b476-10c7cc21fe2a | -9.1612 | -68.2752 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b9a8dd07-d72e-339e-81cc-911f62730931 | -9.7498 | -65.0938 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2dacd5ff-5f44-3858-9756-3b2dd4cce46e | -9.4819 | -66.7836 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bfc0728a-e7f4-34bf-ac66-2b3b42f0a3a7 | -9.0429 | -65.4361 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e76d49c1-7693-3436-81ef-cd939977a1a4 | -8.852 | -66.7827 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 51ece2f3-5911-3bb6-b2e9-960e95e615e4 | -5.9417 | -41.3524 | 2026-10-05 18:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 235.1 |
| 0f3c0a8a-6574-36db-8a85-d184652d48cc | -7.8605 | -72.4222 | 2026-10-05 18:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d22c2da1-33f4-3a5f-a54f-33b836b1329c | -8.8705 | -66.7822 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7c29f8c3-2198-3321-952d-c4444942f1c1 | -9.3443 | -68.9177 | 2026-10-05 18:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 136.2 |
| bbbe1230-1e2a-36ff-ae15-5372c99e7dc1 | -4.9051 | -41.7457 | 2026-10-05 18:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| cd1c5fe4-a910-343e-8efa-98a096a3870d | -9.4969 | -67.6747 | 2026-10-05 18:10:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ca3a397a-6dc7-3069-a3dd-578472c549c8 | -8.5183 | -67.0139 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| e8f0f0ed-70a8-32fa-a2fb-f8e1aad66bc8 | -9.2828 | -65.6526 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 6da3b166-dbd5-3766-8478-847a5a405cbf | -9.475 | -64.3525 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1cdde806-38da-309d-98c5-43a80c606d1c | -8.6493 | -66.5839 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ac4d0938-f203-380d-8655-2395a26f8e35 | -8.6214 | -69.5026 | 2026-10-05 18:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 13e13f33-372a-3d36-9910-f2a3c20d8446 | -8.8704 | -66.8007 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 3b173f86-66dd-3762-8ab3-31e9143aec0b | -9.4958 | -63.9562 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 35b53a8d-d49a-30d2-8cf0-61adf03e0930 | -9.7126 | -65.0951 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a4ec2b9d-0aa5-32ce-878b-18405a603ab2 | -9.9175 | -65.0313 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 03f62f01-6f0b-37eb-b4a2-698ecdb069ad | -4.8083 | -42.134 | 2026-10-05 18:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 3cf54ab9-749d-3707-940d-f949bd0c1ca7 | -8.537 | -66.9764 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |


[Clique aqui para ver as próximas entradas](README159.md)
