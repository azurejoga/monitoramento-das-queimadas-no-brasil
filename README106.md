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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28ec7ec4-66be-36c0-96f9-3050036e21b5 | 0.79118 | -59.20212 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9c7e75a-5902-3138-b1d0-dae7e628b07e | -11.63085 | -50.97866 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93e4e725-ffc2-3ca8-8b97-0e8ba926d3bd | -9.70019 | -58.13615 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a83745c-6b43-3ef2-919e-74c7984a140d | -2.85434 | -57.80662 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a7b1ae2-fbde-381c-bee9-d8ba12524f2b | -10.30233 | -50.51163 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f03d0f72-fc0a-3621-bcdf-ffd8190451e2 | -4.4422 | -55.07021 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0198701-0fe8-38de-a931-dcbdc8a894cf | -3.19155 | -60.43806 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dbbbe4c-8ec3-3a2f-bed2-a5b604dfb465 | -3.07212 | -54.38949 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc6a1387-4570-365f-875c-d07b0fa5f256 | -10.29734 | -50.50736 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dfe5630f-516f-3666-9105-86c7e7d273fc | -9.14738 | -61.1939 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5693925b-841f-3063-a039-90bf2e4e7333 | -10.87533 | -54.09681 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a7747c8-4150-3fd8-b1c2-97ae9627fa40 | -9.30583 | -60.31268 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27fd292e-222d-337b-b47f-7e1fbed7312b | -4.20522 | -59.91106 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1145f5-1039-389d-9a46-6da63b1d07e5 | -3.72378 | -60.57395 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e081d3f7-931c-3fc6-bba2-6683faa5c439 | -9.86427 | -48.39948 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c616f04b-431b-376b-b37f-d6dbdfaf816d | -3.54447 | -62.07708 | 2026-09-23 05:23:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d8334e5-dc7f-319a-b110-db342a335bd4 | -4.41706 | -55.4741 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61865b3a-06a4-361c-b792-4885adc14a13 | -4.86678 | -55.85686 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5036a554-7e75-3bb0-a68e-27b380de83be | -3.15766 | -60.08188 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4897a982-f489-38c5-91fa-858fc88dd65a | -8.03973 | -61.25473 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 266c4027-e81d-3951-afd2-237caf08824f | -2.8805 | -54.08115 | 2026-09-23 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2020f64-7e03-3a10-94c4-c823f708253e | -1.21659 | -54.5513 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5acf840-848c-3f2e-849a-a2aeaee6f3e9 | -8.92466 | -61.48754 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 375553ef-7296-325d-a08a-219c9c0aaae0 | -10.29875 | -50.4967 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01b3add2-5170-365c-bde2-fbfc99665b7d | -1.69494 | -57.40501 | 2026-09-23 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19bdf4f4-4197-3ace-bc70-5dcc3e5d9cc4 | -4.45866 | -47.92586 | 2026-09-23 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24715d2c-652c-37d7-8492-ebce2ff18a3c | -3.86273 | -58.82016 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8200e318-9e36-33d0-8ec9-976c549a1b0e | -3.68884 | -60.57216 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63cb1f68-4a18-3ea9-960a-dd965602668e | -3.12813 | -57.68607 | 2026-09-23 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81f2630a-8866-3557-b39c-9037b360ccb8 | -2.51066 | -56.61127 | 2026-09-23 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fac61a2-9072-3a6a-b709-752f0d378c52 | -2.95347 | -54.07996 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db9b699-5666-360d-a232-a992b6468aa1 | -3.87 | -52.26075 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a82d1ae4-eaef-32cd-a4e9-acba89898ad3 | -3.03424 | -54.41035 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94366320-86c9-3892-95c4-20129ee3a066 | -3.40659 | -61.29218 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6634f977-008f-3f19-959b-4d245cb98c94 | -9.15077 | -59.49108 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac89be38-2640-3654-88df-7d48c8105750 | -5.80294 | -49.15402 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fe0c71f-87b1-38ba-8cde-78c10ed9cbeb | -8.4884 | -57.61392 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82d60e32-ca4f-35b8-af57-43c200fba10a | -3.46081 | -58.31239 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79907c07-045a-3935-815d-9821308dde4b | -10.28626 | -50.54917 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37802b48-6f52-34ef-ab11-e75d0d7b0470 | -3.75924 | -59.40744 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a7a6a2a-1b02-3c83-b63e-27993b6164fd | -11.70184 | -50.8058 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45991b8b-cd31-38a3-88df-34c9f5065983 | -9.09427 | -61.43603 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68306a06-4097-3e32-a879-a9ad69a2fa02 | -10.69082 | -54.48771 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2304e5b9-d06f-350f-bae6-0d986d4abc54 | -3.61289 | -59.02437 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e20d70e-409e-3e4d-9ca9-5b9d9ba70b18 | -3.14197 | -57.68466 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a37fe3-bde8-3810-922b-85105fa436b7 | -9.33423 | -65.72562 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17ec0196-eaa9-36c0-98ce-1641640d4021 | -3.78988 | -60.75322 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a89887d7-9d24-320a-9d67-b4eb15bcad8b | -3.68839 | -60.55295 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a7ef4e4-a70e-33e2-9497-877fda894d46 | -2.46024 | -57.91489 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a930e0f-c1f6-3bd6-b4aa-75d02ec988f7 | -3.36658 | -61.24958 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aaf11f8-07ad-36d8-ad27-57e107c2f10c | -10.2974 | -50.51414 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b17f9f1e-bf90-3615-a6dd-8f4c487da8ed | -3.73491 | -57.25841 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ce9e3b-da95-3ef8-85de-a6aa2e6c32b5 | -3.18622 | -59.69949 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ac633a7-109c-35cb-84c8-d585b05648e7 | -8.20121 | -62.90174 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ed7047-fd10-33d4-9eae-5e969145c749 | -3.15675 | -60.08167 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdd25c9f-a98c-3f09-ad02-eb8c2619cde1 | -12.36754 | -50.15334 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78f87ad2-9b4d-3251-b09f-f8a522e8145a | -5.78123 | -47.15869 | 2026-09-23 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af8eb001-66aa-35f6-855d-fef11a6b1173 | -3.85842 | -58.89012 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24baa2db-7669-30cd-ab57-9a9140d74b62 | -5.89094 | -52.0922 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd425305-84a9-3ec6-98d7-77dbd6e67a58 | -7.88314 | -61.18375 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 663f189b-6623-3e74-a878-f5ada28df91c | -2.94962 | -54.07936 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a2571ea-4494-3a63-bc1a-868a91b374ff | -2.5662 | -57.50253 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 241f517a-634e-3254-96ee-3408cad29a66 | -3.5195 | -56.90621 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10bf349b-ed18-37ea-bca8-6089792fb8d8 | -7.04457 | -62.93322 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b40ab5-f69a-3aa7-92a6-5f53def38a92 | -3.07791 | -61.03987 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f6360c7-2aab-3902-b653-03b02a46103c | -10.8407 | -56.21586 | 2026-09-23 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a12a9dec-fb79-3c3f-bd32-08c9196a24a1 | -3.77308 | -59.60009 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1750fb-9958-3ca7-914f-2d03d49d252f | -10.29047 | -50.51729 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d5778e47-65c4-3c28-a375-82eaf3c50d67 | -4.45275 | -55.43954 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2729c930-66e3-324e-87b2-cf93e743fb03 | -10.29785 | -50.51058 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fab8be75-3318-3c15-81f6-6f0cc1966ff6 | -3.85678 | -58.90046 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 331b49de-20fd-34b0-93cf-40acffb7ca7b | -3.62659 | -49.99619 | 2026-09-23 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 425c1640-7e19-3487-8124-0aec7c27e34a | -8.23783 | -62.83813 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 760d5045-3684-3c5f-91f4-f82e328f974a | -3.51823 | -51.63528 | 2026-09-23 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 374e9911-8049-3761-819f-dac6ccad9718 | -10.2964 | -50.51446 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ac626761-7853-3fb0-9419-6b8931a84863 | -9.55679 | -65.98517 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7452b8e6-f90d-3cff-9e98-ea4ec61cd581 | -9.58465 | -60.52351 | 2026-09-23 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fff91ad9-6e05-3b86-8c83-dd6fa9e06d63 | -9.10445 | -61.43773 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0774a585-1806-3fab-a903-71515e8e13ea | -11.71276 | -50.80722 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d49d3ddd-f563-3db8-aaa5-988874ab74f4 | -10.29311 | -50.53927 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 737d4ee2-2294-3be4-ab76-44734ab4fe71 | -3.44477 | -50.61082 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 124f4057-3c8b-355a-a440-308e76933ce9 | -2.95588 | -60.02765 | 2026-09-23 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de58fa50-cff5-3713-bf29-61a949a6b133 | -10.31178 | -58.50807 | 2026-09-23 05:23:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f6b0c47-27aa-3a75-87e7-93b61fb8a168 | -7.50653 | -63.8815 | 2026-09-23 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fc0b9f-8a9f-3cea-adf8-86fb13141444 | -11.13117 | -51.05848 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b80b38d-fafa-3ba8-bf56-8c1a542665cf | -4.34067 | -55.65712 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07e895f5-3fbb-36cd-9b16-709b2af079c1 | -4.38713 | -60.96232 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6929ca80-5a39-36b1-aaa2-cee37ca48649 | -3.82478 | -59.33555 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30c7bdcc-eb05-3c66-8395-5845aaa4664d | -3.68316 | -60.56359 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ee0ccc4-a98d-3815-afe7-a5a663be2f1e | -12.42046 | -46.96584 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8cd9a676-2478-30cb-8294-e260e2346e00 | -3.95968 | -60.00007 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68743506-337b-3e73-9ae3-64297fa549e1 | -10.29283 | -50.50629 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3c0c67f-c958-3865-9286-979b1d9e7661 | -2.87088 | -57.78829 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d79ab3a6-8e1b-3ff6-991a-9266c87f2b15 | -9.48085 | -67.1562 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79d4333d-0eec-3744-af49-95a7ec5696e6 | -10.29338 | -49.11398 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24a0fd18-81f8-3a70-b132-7f3dafbe8b4f | -8.49241 | -57.61069 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6fa63a99-ab43-3016-9442-20fdd1cc198d | -3.47022 | -59.55558 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b879bc2a-ac50-3fff-878e-fdf860a22642 | -2.88435 | -54.08174 | 2026-09-23 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69a8aea7-e936-3509-8e89-d4ce90e434a4 | -3.37517 | -58.07973 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36dd6794-fcc0-3201-b55a-e148983f5624 | -7.55312 | -61.48624 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README107.md)
