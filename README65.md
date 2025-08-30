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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 310d5282-33ff-330b-993d-e20d15b0ff01 | -9.4594 | -60.56551 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aecaac5c-b7da-3483-8c88-e36a55ead47e | -8.6219 | -63.95338 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 068fbae6-3b1e-3fc4-adfa-da473ffcf658 | -8.28409 | -61.40361 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b900a56-021c-3c05-811c-c4e4f842834e | -9.44503 | -62.33006 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb190e20-8b57-39ba-ab9f-daa3718865b2 | -9.45329 | -62.35105 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 527868e6-9f67-343b-9fbb-d501a7f035f3 | -9.44416 | -60.57094 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70f90e1a-d24e-3846-97be-5aa1a777f8b8 | -9.00001 | -56.35143 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eec4b5ee-a91f-32b3-975a-bd037f105413 | -12.37125 | -46.39556 | 2025-08-30 05:10:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4d44d5a3-ca8a-3a88-b7b2-75cc87384ec2 | -9.17918 | -59.58241 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 468298dd-6c3d-396e-94ae-14537ceb0eac | -9.47096 | -60.31002 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 490358e1-180a-3cbc-82d6-4e5a72ab945c | -7.58438 | -45.13062 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc36b1fe-76ca-30a7-8d6f-2c653368fdbc | -8.63347 | -67.25594 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 911d9fd3-c5ab-3e88-b9fc-f2ec1e3a7951 | -11.88403 | -46.39239 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a880a79f-43f3-32c2-ba9d-0c5f4e05ccf5 | -9.14928 | -59.5663 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c816b2fe-c8eb-3863-871d-b2241da8fdca | -11.86529 | -46.38356 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 665ba510-10e8-3150-9238-8fc6f7c5017d | -5.876 | -46.50162 | 2025-08-30 05:10:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e494ab56-84ba-3474-a22b-6d873087d228 | -10.38237 | -57.83285 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88496add-e170-3fcd-994f-a249be2d778d | -7.39528 | -45.93577 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adcce4cf-8c10-39a1-b3a5-688bdf5788b5 | -7.4001 | -45.92487 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d0556d9-9873-3ea2-a6b5-a42c018e5c22 | -8.12405 | -61.21599 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cf1cb25-4d5d-34f8-a277-e7a6a9f4004c | -10.44868 | -57.97275 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af902b4b-3273-3be3-9c00-125e7e6dc766 | -9.45657 | -60.56099 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d42208c-bb8b-38e9-95df-66ecc7b596c9 | -7.39877 | -45.93461 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85620aef-417b-3bc3-87d4-5a78e0c32ede | -10.02225 | -48.09483 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4aced557-f84c-3119-a7a7-ea6cf9a55b9d | -9.44582 | -62.32535 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec1148a7-a282-3b7b-a58b-ccabcb6a442d | -9.45026 | -60.55585 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b164b498-21e7-3165-9112-df5bc433be78 | -9.37466 | -57.5905 | 2025-08-30 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28e51b61-e660-32e4-ae32-1242126a610c | -9.82352 | -63.858 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a24327b6-01bd-31d1-af91-46ade7cb5e53 | -7.40499 | -49.51879 | 2025-08-30 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe17b74-3026-3329-ae9d-6576752e30a9 | -10.72525 | -47.0095 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4750ffb5-825d-3d7a-bff9-efbc3fd85c2a | -11.1509 | -47.1475 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e7742daa-16a4-3332-acf6-9e63677a432d | -6.34189 | -58.17027 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91831580-e857-3da1-93ee-53f70ab20983 | -11.83747 | -46.86038 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a33344b-8eac-3360-939e-32d18adb17c0 | -8.28117 | -61.42116 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4541fe7a-8d2a-3af0-9c04-f7d94d82ba67 | -5.31901 | -55.87978 | 2025-08-30 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f683a255-7005-3a48-b8d8-93269552a4aa | -9.43659 | -62.33352 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e1abec88-3ea1-3a18-af1e-e285c8143704 | -6.343 | -58.18478 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13d7eca6-864a-3da5-91ac-c4752c385d65 | -9.43585 | -60.57004 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dde593d-e99e-3cc1-a958-2510c0fa532d | -8.29221 | -61.42309 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2da092f6-44d0-3a31-9440-d36d1b0a0766 | -10.03281 | -46.03613 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eb16c34-28e8-3559-8f5d-8d54c1e7e59b | -8.8789 | -60.74083 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07d3b034-f54f-37e9-8cea-06ba8220138e | -10.02725 | -46.03183 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec4d87de-2965-3242-8f40-270102caec94 | -9.21728 | -60.86538 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4f338e-31d5-352a-a9f2-6c9464413262 | -9.44964 | -62.326 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f329d21e-8cb9-32cb-8d66-1fd5c7f8eff0 | -10.07479 | -58.36457 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd1398b9-3e14-38e8-987d-8aba7a04e6a5 | -9.69207 | -48.31038 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4216f389-8611-3714-a1b2-f6524cbfa288 | -10.37683 | -57.82478 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6103bf81-ddeb-391f-8738-71cc9142e3e0 | -10.96379 | -49.57177 | 2025-08-30 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa5630aa-4097-3cb3-87e6-77edb532c952 | -8.54651 | -63.02582 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8a3494a-527a-3f05-aacd-c4d3b4670d67 | -10.99307 | -46.85161 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec11e1dc-5abf-361e-9301-15785dd468f3 | -8.59299 | -60.58576 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b7bbcfa-34b2-3e8e-aee6-aee629fdf08c | -9.4428 | -62.31997 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40cb1ff6-7fb1-3a2b-a96e-b41d9ff592b4 | -9.81864 | -63.86131 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26cb619e-f8ce-3b2b-aa4f-3dfc25a147cb | -11.41329 | -44.6866 | 2025-08-30 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52725f35-7255-3ffc-adeb-bff0502cc7ca | -7.9617 | -46.37752 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef90c4a2-1d9f-317e-903b-395b11b3ea80 | -6.16439 | -44.19382 | 2025-08-30 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd6695aa-2c6a-3e62-a643-67513029ac1a | -6.98712 | -63.0094 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02182738-51d3-33cd-a548-faff29083a63 | -8.17653 | -61.37349 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97b9b41e-d44b-33c4-a59e-e0e1ad79e59d | -9.45244 | -60.56429 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d77ffc98-53c8-376a-a833-8bdb7e38c95e | -11.86377 | -46.45614 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0e235a00-d83e-334d-825f-9a83943f532e | -8.59366 | -60.58176 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24802eeb-3215-3699-ac19-1b7fcb340bd6 | -9.11859 | -65.78855 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cab72bf9-754c-3125-ab6f-852104b66802 | -7.42808 | -44.80581 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 027aaa8a-44a3-3c20-bb4f-769131208362 | -8.28853 | -61.42247 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fea0c13-c58e-353a-af43-e6f5d018ef9a | -8.18316 | -61.3791 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd79a21c-70e2-30a6-a8ea-a2f034775b07 | -10.47297 | -57.96942 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 203dbc4e-ceac-30a3-9fc3-0e469367ef65 | -9.70383 | -47.05668 | 2025-08-30 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a3e881a-396c-3e8a-8145-8017fc500dd4 | -9.44764 | -60.57153 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ddc00e37-5ec5-3384-8cf2-2619e53ead89 | -11.82681 | -46.48476 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6b730783-572a-3a57-a305-3e274ccf69cf | -11.88459 | -46.38743 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa4d577f-00cb-3de2-8ad0-8d299442da82 | -7.73811 | -50.26775 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 33504ef3-d911-377c-943a-ede007f4d789 | -9.48945 | -45.40668 | 2025-08-30 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2360a4d-9f85-30f1-ad9d-51cb38c37707 | -8.18612 | -61.3841 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab488ed2-6407-3f61-9f10-dd87d44e0171 | -10.37303 | -59.20142 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d55fc008-8b0e-3786-9cc3-ca9a7461be17 | -9.43862 | -62.36816 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df8ea948-e7a3-3744-8bc0-88499c3bf284 | -11.86487 | -46.38391 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f879b98-db1e-356c-9b4d-b93a3df50bc4 | -8.55369 | -51.30572 | 2025-08-30 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ba2ba93-5a0b-3895-97df-3ab9d9d02993 | -11.88995 | -46.39826 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cadd7c6d-6c6a-322c-81b5-7cba2399ff0c | -11.84995 | -46.39891 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea004d0c-a977-3dc9-b441-1873305fe09c | -9.29763 | -56.81348 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3c7b8ed-97bf-32e6-8f28-22e9d69b3fd8 | -8.92584 | -64.23423 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 852d2392-5c7c-3e5d-a052-0e0d9939f67f | -5.61231 | -45.00974 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b9e66461-12b6-3b95-bef3-30dd026acf2d | -7.72274 | -50.30767 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef2f79fa-b90c-3a8c-a1ac-a4e49dbc79f6 | -10.49241 | -51.63174 | 2025-08-30 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0d400c3-f3bc-3b4b-972b-48a8e1325ec4 | -9.80667 | -61.20055 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ac8de4c-7574-3f46-97cd-8acffa1b9d00 | -9.45027 | -62.34565 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a932b7d-2abd-38e3-8088-1e0c51ece776 | -9.45569 | -62.33674 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 4909ef47-f162-38d9-9aeb-4333a1ef93fb | -9.10684 | -46.04842 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d56959e-5f25-315b-811e-aea587332f44 | -8.87957 | -60.73682 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c6e62ff-012b-3ff4-977d-79a7f73edb20 | -9.46108 | -62.328 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 03dd2d3c-bc19-389d-912f-23cb7a4914f2 | -9.50427 | -45.39653 | 2025-08-30 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baae3cc8-2d96-3744-beb5-20e015f9d08c | -9.14032 | -49.62535 | 2025-08-30 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24f682df-9937-32c2-8992-cac35dcce96c | -9.24695 | -60.92854 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e938ae-6cf9-3648-a558-e5e7d5be35d7 | -9.10804 | -65.74149 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e11b2e2d-8fb2-35a1-9ce4-66fc598dd83a | -8.65199 | -63.29158 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb37293-32c6-3737-b0d9-7b1fef098903 | -10.66448 | -48.72991 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e5b9d3d-a426-35e1-a883-c3dd4c05e0b4 | -9.43962 | -62.33889 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a64156ea-7b2b-3bfc-93d2-dd681f2035bd | -9.44632 | -60.57182 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d708b452-b9c5-3207-bf51-1c37db194878 | -5.61226 | -45.00538 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 97c39a9d-cbef-3161-861e-ca6e69c259f7 | -11.0694 | -52.03712 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
