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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9288a6c-58a7-3203-ab59-81069ba63e4f | -12.7898 | -51.2593 | 2024-09-26 00:16:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 179.1 |
| a2e6ab07-522a-3052-ac7c-106cf22070d2 | -12.7901 | -51.238 | 2024-09-26 00:16:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 359.4 |
| f0e96622-cb9b-3cc8-ae92-bb28ceaab4e8 | -12.7904 | -51.2166 | 2024-09-26 00:16:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 7b4cd9d1-1f65-31a4-ac89-4e71a94064c1 | -12.8089 | -51.257 | 2024-09-26 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0e690267-5771-3988-8c53-2b2da7f23574 | -13.1958 | -45.6539 | 2024-09-26 00:16:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 90aa2866-984c-3ea8-9a10-27c362b730e2 | -13.1963 | -45.6308 | 2024-09-26 00:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 480e62e8-625e-37ef-8383-6e587ed6c8b1 | -13.0295 | -57.2985 | 2024-09-26 00:16:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1e5fab65-b58a-3cc8-8ceb-90f4484a4442 | -13.7509 | -51.0951 | 2024-09-26 00:16:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 7d818c83-e8eb-33d2-ae5b-a7047d16003f | -13.7513 | -51.0736 | 2024-09-26 00:16:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 12471a8b-8d2c-3cd1-9e6e-c1d1223fd46a | -15.3316 | -47.4635 | 2024-09-26 00:16:32 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ca1a7c5c-e01e-38c5-aebf-250a15c38923 | -16.7796 | -57.7898 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| ae2e09e7-0f54-323f-b622-a6ed9171d2d9 | -16.7992 | -57.7876 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 181.7 |
| 0f8049d4-baff-31d5-8694-b273b9f99251 | -16.7995 | -57.7672 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| d66702cb-c1e2-3dd1-9933-7635b9bdcacc | -16.8036 | -57.5016 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| e9f20eb9-f076-3c5b-b16f-ca253146d5a7 | -16.8039 | -57.4811 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| e5b438a0-e93f-383c-823c-c34d982b3730 | -16.8187 | -57.7854 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 9d5d2e94-ee79-32ba-b49f-f8c2fb60dbc9 | -16.8194 | -57.7446 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 3804b7f0-d894-3ad3-839c-967ba0ba4b15 | -16.8228 | -57.5198 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| f881145b-f940-36e1-9ee2-fffda1211e8a | -16.8231 | -57.4994 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| f5555b93-98d2-3c96-b9a2-5450f44e47a4 | -16.8389 | -57.7424 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 190.9 |
| 7ae50632-325a-3b16-9bf7-2302827d25dc | -16.8392 | -57.722 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 418.8 |
| 0b3b177b-406c-371a-9009-ca738c076a50 | -16.8396 | -57.7015 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| b7bafed4-3954-3575-ba1e-1860cff95702 | -16.8588 | -57.7197 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.2 |
| e9ab3622-bf36-35be-8115-29847e3e7d19 | -16.8591 | -57.6993 | 2024-09-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 7f382e23-b7fc-3ad1-9837-241ee4f9d1b0 | -17.096 | -56.3576 | 2024-09-26 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 03f8b81c-0686-38dd-b46b-604452c20436 | -16.9729 | -57.931 | 2024-09-26 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| d3cfed60-1e0a-3e87-b2a7-4470a30cd897 | -16.9732 | -57.9106 | 2024-09-26 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 08861e66-08bc-3781-94fd-359c259d0752 | -16.9925 | -57.9288 | 2024-09-26 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 24f39bc6-6e0b-36f9-a16e-26f2551e37bc | -18.1605 | -42.7767 | 2024-09-26 00:16:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| f203e500-7ebd-3260-ae8b-6a9a1f58f7cf | -18.1612 | -42.7518 | 2024-09-26 00:16:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.4 |
| 7d451bb8-805b-35dd-8e63-0ec23d7ebcae | -18.9769 | -41.1244 | 2024-09-26 00:16:50 | GOES-16 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 010e959a-7d74-3882-aa25-917021a222fa | -19.1374 | -42.471 | 2024-09-26 00:16:51 | GOES-16 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| 53b64146-42ec-3416-97f0-e623c6f8210c | -19.1003 | -45.0761 | 2024-09-26 00:16:52 | GOES-16 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6e15df07-32f3-3406-9116-b0ef9fa6c1c9 | -19.9298 | -43.7711 | 2024-09-26 00:16:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 3ac2169e-dea3-3266-adf5-3c4bea7c67ba | -20.3999 | -41.8602 | 2024-09-26 00:16:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.4 |
| cfba4f44-2e35-37ef-acd7-ac82e5de2f89 | -20.4197 | -41.8798 | 2024-09-26 00:16:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 259.0 |
| fa192ae5-c707-3903-9a7e-ed0470aad95b | -20.4206 | -41.8541 | 2024-09-26 00:16:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 186.3 |
| ea805a03-2530-355b-8cf5-b1f6dd3e5d4f | -20.4404 | -41.8737 | 2024-09-26 00:16:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.0 |
| 5fb63c91-1760-3c58-a9b0-782332adcbad | -20.4413 | -41.8479 | 2024-09-26 00:16:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.3 |
| 39d1fe56-530d-3b5e-a2e4-2d1725838d65 | -20.5876 | -51.5026 | 2024-09-26 00:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.5 |
| 4a05f57a-f2db-30f6-b301-145e089d4618 | -20.5881 | -51.4802 | 2024-09-26 00:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 274.6 |
| 3ef72f57-dc02-3bd2-9717-892e787fda4d | -20.608 | -51.4986 | 2024-09-26 00:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 199.6 |
| b678c769-3232-317e-addc-c971ab99ddfb | -20.6086 | -51.4762 | 2024-09-26 00:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 251.6 |
| 407d2e84-559a-3a46-8d56-b4c1305a9306 | -21.2733 | -51.0061 | 2024-09-26 00:17:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 7c5a6004-3586-3259-93cf-0d4fdbf44fc0 | -1.0553 | -53.3553 | 2024-09-26 00:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8da61d17-26f9-3d55-aff0-ae0fc9765d4a | -2.6496 | -54.6172 | 2024-09-26 00:25:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| c9cd4e5c-48fb-3a66-96ef-fcf5effc3542 | -2.6601 | -57.5507 | 2024-09-26 00:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3bfdae9e-03b1-3d04-a96d-9f78a94e1a57 | -2.6784 | -57.5504 | 2024-09-26 00:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9035a54a-374d-3ee0-b3e1-580188241759 | -2.6785 | -57.531 | 2024-09-26 00:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 52720ada-70b6-386d-88d0-e612d529466c | -2.6968 | -57.5307 | 2024-09-26 00:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fd04e4d2-4de4-3601-8716-6ad1e5292a4f | -3.3505 | -53.7775 | 2024-09-26 00:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 99e163ec-9afc-365f-b532-dcfa04482f59 | -3.5673 | -50.3794 | 2024-09-26 00:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 05a0c720-8393-332a-a8cb-487118e38f50 | -3.9208 | -46.4459 | 2024-09-26 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 29679bf7-94a1-3f4e-89ff-051b05125372 | -4.0656 | -44.048 | 2024-09-26 00:25:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| aaf93a18-9afd-3450-b016-d2610192b563 | -6.5772 | -60.0437 | 2024-09-26 00:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 27fdd1b3-f0d2-309b-a117-d6405994a90c | -6.7839 | -59.3245 | 2024-09-26 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 220a60ef-2449-3fab-830f-452cde57cd03 | -6.784 | -59.3052 | 2024-09-26 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 02dce6bc-aa0d-31b1-974d-e7db9c9bdfee | -6.8023 | -59.3237 | 2024-09-26 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a53a9995-807d-3fb1-9509-c3fc8677bb9e | -6.8024 | -59.3044 | 2024-09-26 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 1b0cd23b-4257-3d8d-9aa3-fc3870647e51 | -6.8384 | -63.1457 | 2024-09-26 00:25:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c56dd7a3-1c2f-31f3-a939-312fc542b4cc | -6.8385 | -63.1269 | 2024-09-26 00:25:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 134137e4-45f0-325b-a69d-31dc0c549177 | -6.9305 | -63.1241 | 2024-09-26 00:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 12fe0b1a-e389-384f-a83d-05afc1e11dd1 | -6.9306 | -63.1053 | 2024-09-26 00:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f1c075ee-c15e-321f-be79-34419dcc27d1 | -6.9489 | -63.1236 | 2024-09-26 00:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a9412444-19d5-308f-9875-751c90551466 | -6.949 | -63.1048 | 2024-09-26 00:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5dbeac00-4f62-3709-938d-2149cf7b8dfa | -7.1099 | -46.4396 | 2024-09-26 00:25:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| d2d75805-dfa4-31e4-b3ef-3f493fd6c07a | -7.2905 | -61.106 | 2024-09-26 00:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 5149d731-65f3-37a9-9e55-06988c5eff31 | -7.2906 | -61.0869 | 2024-09-26 00:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ccc3217a-254a-3b91-b562-429612288825 | -7.3637 | -55.5134 | 2024-09-26 00:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| a228d4d3-7762-3291-869a-a398f640f137 | -7.3639 | -55.4935 | 2024-09-26 00:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 278ff0e2-33b0-367d-a217-7e48993842b3 | -7.3823 | -55.5124 | 2024-09-26 00:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a66950b1-655b-3b30-8402-5ee92b0ca39c | -7.3824 | -55.4924 | 2024-09-26 00:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 199f865d-e024-3db0-8a3b-0e35b6682975 | -7.5705 | -55.1617 | 2024-09-26 00:25:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 6bd7e298-7589-3928-926b-cfa2f831a3a7 | -7.5889 | -55.1807 | 2024-09-26 00:25:50 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 978095fb-853f-3ef1-a81b-3ae6f9c42daa | -7.797 | -54.7263 | 2024-09-26 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| d6afdac6-e368-30d8-beda-28b941a4baf6 | -7.8156 | -54.7252 | 2024-09-26 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| b28e9f5b-e0ee-3f16-8cef-b23707545493 | -7.8417 | -72.7688 | 2024-09-26 00:25:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 50e25b3e-27ef-3f1f-bbc5-9d4ddd04926f | -8.0376 | -67.2661 | 2024-09-26 00:25:53 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 87b2ce22-c457-34b7-a0f9-2d4b4795d201 | -8.0561 | -67.2657 | 2024-09-26 00:25:53 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c9e9b3a7-f470-3a94-9703-4b13e1dc40bf | -8.0561 | -67.2472 | 2024-09-26 00:25:53 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| daa9891c-c86e-36b2-9fc1-7b70b0d7ec86 | -8.1572 | -61.3953 | 2024-09-26 00:25:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5894e007-44c9-3e97-a14b-dc80fd56cf30 | -8.1757 | -61.3946 | 2024-09-26 00:25:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 12488819-08f0-3b76-9024-7c2046be3949 | -8.3155 | -54.9956 | 2024-09-26 00:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| e467062d-4605-38d0-b558-ef2fabe87d7a | -8.5187 | -55.1834 | 2024-09-26 00:25:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 08d72d2f-2b08-3fa2-a9e5-c2ac78446ccc | -8.5542 | -63.1814 | 2024-09-26 00:25:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7d6f6bb7-3cd7-3703-a31a-133cd6ab2309 | -8.7085 | -54.8083 | 2024-09-26 00:25:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 90e88ee2-6a27-3619-8c3d-ddc6cf887189 | -8.7087 | -54.7881 | 2024-09-26 00:25:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| cb87b800-8f9d-36bc-8841-13a430ce68c8 | -8.7913 | -58.1986 | 2024-09-26 00:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2298480f-fbbd-335b-8622-21a9aedfa8f4 | -8.8098 | -58.2172 | 2024-09-26 00:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 85c21b2b-0246-3f63-88f7-1c0221a6cc50 | -8.8292 | -63.7179 | 2024-09-26 00:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1eabde73-3dfd-32c9-b034-c7f31ee208e4 | -8.9301 | -57.1488 | 2024-09-26 00:25:57 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 673f453d-73aa-3f84-b923-9efebe95c12e | -8.968 | -62.1415 | 2024-09-26 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| d375c5e4-195f-3ccb-be10-9c635c8ea089 | -9.0657 | -61.3743 | 2024-09-26 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a21b3de5-0d09-3c24-8831-d5bcc2130bff | -9.086 | -61.1245 | 2024-09-26 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 30ddcd08-012a-3d6a-b158-c7b394d7e9ef | -9.103 | -61.3534 | 2024-09-26 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d066055d-2bac-305d-8cd6-94a5ebb3d3b7 | -9.1032 | -61.3343 | 2024-09-26 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 6400069f-7870-365c-b4ec-8333e8518a5e | -9.1033 | -61.3152 | 2024-09-26 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 339b994f-2544-388d-b18a-ca5434ac5d00 | -9.1046 | -61.1237 | 2024-09-26 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e53a656a-e810-3e28-8678-213de1d05783 | -9.1216 | -61.3526 | 2024-09-26 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 0a7399f9-332d-382b-bb04-38ba57eff369 | -9.1217 | -61.3334 | 2024-09-26 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |


[Clique aqui para ver as próximas entradas](README7.md)
