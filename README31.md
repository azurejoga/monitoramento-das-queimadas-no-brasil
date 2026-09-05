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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eab0d3ce-3c38-361e-bb2d-917316e4db8a | -6.67462 | -59.94157 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79cf7570-a2c7-3491-b6e9-778abd932653 | -6.66203 | -59.94859 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d1fc7a1a-95b1-3d8c-af37-a78789d92bd1 | -5.43492 | -60.18529 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055ccafe-5e3b-34c2-a947-57f7b7712a64 | -9.46451 | -67.42574 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c18ebf-b0de-3383-8f70-e4d699b4973f | -6.13017 | -59.88999 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e955f7d6-20cc-3682-b09a-a3226a37df4b | -7.54795 | -61.34226 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff7dd137-9c17-3731-aa04-9dd8c4ddf7ae | -6.12887 | -59.92107 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c13cd22-159a-38b9-a8c4-26ce3379e754 | -6.15546 | -59.94378 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b0a5d19-4e19-3404-84a7-e2a55207df76 | -8.5235 | -67.16128 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d12473e-b00e-3a4c-aef5-4faa0a428abc | -7.55131 | -61.34277 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa0179db-9cfd-3f89-bf40-07b25bee40de | -6.58593 | -59.90923 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff30a64b-8c8d-3704-84a4-eac2928937a2 | -5.42807 | -60.18423 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2cd3eb6-6faf-32b5-8997-00b5a7ecbb9a | -7.25767 | -61.09987 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54b1d122-ad0a-36db-b26a-62dbc966adc4 | -9.13464 | -67.80447 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a5a311-c1f4-3448-af60-59e070225ab5 | -9.65231 | -69.00394 | 2026-09-05 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b3f6f15-3694-3a02-ab9f-ba44573329e2 | -9.46367 | -67.43073 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 008aeecf-c242-393d-8bbc-0bd32b6dec12 | -6.67113 | -59.94103 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04a7cf91-fb6b-3fc5-8361-8b8313efaf4d | -6.65326 | -59.95905 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c69d15e7-1178-34e2-acd6-8a0e15fd5ea3 | -6.66492 | -59.95295 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| dd590692-e19d-35e5-b17c-213649f11532 | -7.5485 | -61.33868 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c7b9869-7eac-39db-8381-2ef172c668b3 | -9.36036 | -67.5623 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef50b67e-9850-37c8-b759-b8aa6f0cdd70 | -5.46889 | -60.05383 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e67e0730-653a-39d8-94a0-5290afc51260 | -6.13175 | -59.92542 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf202c8-b863-3be3-8b80-a363fe9baadb | -6.65158 | -59.94694 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccf1bb1-62c4-3d16-8c30-79073adf5a50 | -5.76723 | -59.18571 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 534fef67-41fe-3298-80e1-a86bef65324f | -6.68449 | -59.97059 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecf756a8-01b4-344a-9aae-cb42ec137897 | -10.12987 | -55.90091 | 2026-09-05 05:42:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95c555b6-85fd-3951-a1bf-cf86f5ede0a9 | -6.65626 | -59.93978 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6fca0754-095a-3d73-9c19-1d101f7a4816 | -5.83939 | -60.25357 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fd0747c-9998-3e24-8f17-84ee0f90dbdc | -6.02971 | -60.1721 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef5954c7-614d-3b9e-bd10-1331e204e4ed | -9.46483 | -67.42277 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1545a328-4eac-390e-b884-e0ff82dec3cb | -10.32023 | -59.14817 | 2026-09-05 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 074bff05-4cb7-32f7-bf67-3779e7c91a9a | -6.65386 | -59.9552 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| da732f5c-f32c-3ca6-8432-b9550f337f6c | -6.67054 | -59.9449 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 326317d0-771d-34fe-bbfe-fcf936936c5b | -6.66612 | -59.94528 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b76de775-bb52-3a7b-bb00-6c7ea111e6b8 | -6.65914 | -59.94419 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 65917451-96e4-3f79-9b34-977d44438bd0 | -5.43106 | -60.1203 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 333ccec5-64b8-31fb-b83b-e93664626bf6 | -5.46047 | -60.04491 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aeb7d6b-44db-3456-860f-987f8d44062e | -6.66901 | -59.94965 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 985b15ef-648d-37a1-a5e1-8e9d68ae45de | -6.12005 | -59.95477 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c5d81af-4565-3f26-9bf3-87d4c555802f | -6.67928 | -59.93439 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35c121e5-b0d1-39ed-b64f-18ab818a9295 | -6.6839 | -59.97444 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8ffe67-8c65-3b3b-8a0f-d08e83122230 | -9.5323 | -68.63287 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4c16bc-0277-326f-b2d7-697bc9a5380b | -6.68273 | -59.9821 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26b4de62-20b4-3a95-abbf-f73c10b85084 | -6.66938 | -59.95259 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5e1ca2f-b8c4-3cbc-a4f7-b1d8b1fc6501 | -7.54122 | -61.34122 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 228e385c-21e5-3dc5-b380-a838ed4699bf | -7.24549 | -59.52782 | 2026-09-05 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94fadc52-deac-3b81-872a-cf6e318dd71e | -9.84253 | -68.97701 | 2026-09-05 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7acfb4cd-07ed-32a5-9cb9-694e70c95d14 | -5.84281 | -60.2541 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e8413593-eb4c-311a-83cd-7ef164dca3f3 | -6.66996 | -59.94875 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a87767e-5e19-36fe-872f-9d105e08c0b5 | -6.20283 | -57.76598 | 2026-09-05 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044facb0-dbd1-3880-829c-77bd4891977e | -9.54916 | -60.83083 | 2026-09-05 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bb11377-a5be-3f94-9e13-fa9dbe2f3c5a | -6.66323 | -59.94091 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 03fa1fb9-b388-3286-ac3e-dac8c917414b | -5.83596 | -60.25304 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de4f93d8-a6dd-3b26-9b00-90b5b10ee568 | -6.15257 | -59.93945 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72703521-da64-33f7-9d3a-0e3e3301bd27 | -6.52989 | -59.94084 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80f5d1e8-540c-3152-aadb-c5dcfb12b152 | -9.5316 | -68.63683 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c3f70db-5c8e-32b4-b623-a19acee511bf | -9.46571 | -67.41778 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8edd00e-67c3-3d16-8ffa-761e3ba92cdd | -6.68797 | -59.97112 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3291d315-681a-38c3-bfed-160db738e5af | -5.33182 | -60.13218 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798d3453-640f-3d6c-90f7-d408abbb316d | -9.98834 | -67.57195 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ced1d252-7de0-3a79-8407-3058c65cdb9c | -6.07315 | -59.98241 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d8cae59-5616-3751-8a3f-a9d3c940e910 | -7.57987 | -61.33628 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a38c2fa-2051-3055-a687-49f7e0f9cfae | -6.68277 | -59.93493 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c61d4cf6-7f61-36f3-ac0b-38813053341b | -8.86524 | -68.4869 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57251035-c3f4-3da8-a9ee-de3b51849d12 | -9.46396 | -67.42776 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18c30d34-ea7d-3a31-bcdc-260d7b09412a | -6.5264 | -59.94031 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b41b9e90-d1f5-3cf9-8b95-818ccfed19ee | -10.19997 | -69.08913 | 2026-09-05 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfb6062d-af1e-388d-813a-b23f43a4cd8c | -10.22964 | -68.65402 | 2026-09-05 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73f66a39-bd0d-3bee-b972-e81289c013ba | -11.90748 | -64.99522 | 2026-09-05 05:44:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 110f2b68-1219-314f-bf2b-3b0536929d65 | -14.52461 | -59.80245 | 2026-09-05 05:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8ca16e2b-cb62-3795-bcd9-8125d3c625b0 | -14.52537 | -59.7971 | 2026-09-05 05:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e7599fcd-d9dd-315d-8408-d5117a139984 | -10.60589 | -69.14128 | 2026-09-05 05:44:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9712c8f-b78f-3067-a55a-85f303331b5a | -17.10214 | -56.83921 | 2026-09-05 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 17c9e284-bdfc-3984-949d-53cdfb24432b | -18.16427 | -54.84394 | 2026-09-05 05:44:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155dafd1-1668-3f43-ba4a-6c65720b48dc | -17.10348 | -56.83802 | 2026-09-05 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5f52d640-51e4-3d4f-9177-5217bfaf5dc0 | -12.00893 | -64.88718 | 2026-09-05 05:44:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e436ca-0372-3ca4-91ad-4ebfd388a2d3 | -12.00833 | -64.89084 | 2026-09-05 05:44:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1ae954-c683-329e-81b5-bd555cda3804 | -11.90409 | -64.99463 | 2026-09-05 05:44:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f04d18f-e84d-38f1-b8e0-fa48b2a06f0c | -19.16678 | -57.34183 | 2026-09-05 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 658107b6-1841-377c-ae8b-3ea3d0976ca5 | -14.52843 | -59.80324 | 2026-09-05 05:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511d4762-259c-3745-ae38-909a8311bc5c | -14.54248 | -59.75935 | 2026-09-05 05:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fbc9a13-b39c-33cb-af2a-c4c7a0b80bfc | -10.19645 | -69.05915 | 2026-09-05 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6fe8d04-eaa2-3256-900a-09ef99e08b78 | -20.79397 | -57.87687 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 26f9ac46-4488-3a3b-9672-a1b353433710 | -20.76773 | -57.88831 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7fd42b1d-ddbe-3e54-baab-e31b535b9fce | -20.76639 | -57.94168 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 87d9605d-afb0-331b-95fb-e760d29e7bc3 | -20.75232 | -57.89708 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c11188a3-5a03-3550-bc59-1b96a937e090 | -20.79257 | -57.75578 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 37e17562-a07e-3ce7-96d5-c0701964dfcb | -20.79871 | -57.87747 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e1240c70-7f22-31f3-ae66-161f4125770b | -20.78778 | -57.75522 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 072f5852-966c-33eb-875b-61d41c5527d7 | -20.77172 | -57.93704 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5c9a9648-314f-3cd1-9fec-b30053f17415 | -20.75705 | -57.89769 | 2026-09-05 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d179a915-bd67-3cbe-8545-ec2db1782978 | -5.346 | -56.0454 | 2026-09-05 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c1f674b9-f80b-3c47-941b-b96602e33559 | -6.6698 | -59.9443 | 2026-09-05 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 2bb3de4d-c1b5-31d5-81f8-7e5d9d7b4d53 | -3.7645 | -61.7737 | 2026-09-05 05:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f734397b-635e-3aa5-ae47-36ea4714ca4c | -6.6697 | -59.9635 | 2026-09-05 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 392f71af-ab83-3395-8f55-047256164864 | -5.3462 | -56.0256 | 2026-09-05 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4af3dda1-e25e-3f86-afa1-1d2b3ca16a6d | -6.6514 | -59.945 | 2026-09-05 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 467dc2d2-cde1-3546-aa80-299793a2fdb8 | -6.6513 | -59.9642 | 2026-09-05 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| cd68ea81-ca82-3d2b-a083-bfb3d1e9e15d | 4.27243 | -60.04558 | 2026-09-05 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README32.md)
