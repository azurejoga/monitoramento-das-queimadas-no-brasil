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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e67ac941-dab5-36a2-9739-2f93f85a7d61 | -9.76136 | -65.09145 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e6e43ff-f9d4-32a2-9d18-e8ef56fa26f6 | -12.42577 | -45.37867 | 2025-07-25 05:38:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 29a81252-a356-3b90-ae35-f6a79ca8af3b | -10.05086 | -59.10611 | 2025-07-25 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a78daff6-873e-347f-886e-6caa5e990f5c | -14.94595 | -46.98346 | 2025-07-25 05:38:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 94972815-acc2-308a-87f5-9fe3463f2113 | -11.67949 | -58.49701 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 592406d0-8518-3eb2-8b49-9033c81038f8 | -9.97068 | -64.94949 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7983b493-c28b-374c-83ae-b415a4309573 | -9.13498 | -63.91931 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f56e9b-e8cf-3714-a9e9-e1378fe0bf24 | -11.94376 | -58.76583 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 130c5889-f00c-3dcb-875e-4af101a1fe00 | -9.13167 | -63.91878 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1efd1f7a-30ec-3164-aa46-aa096fdeaf4f | -8.95766 | -72.84031 | 2025-07-25 05:38:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5607b7b4-bd77-3c3f-bc83-a9ce5fc2c171 | -8.50103 | -64.04047 | 2025-07-25 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff9fce30-3026-3385-835c-582fc9f81f66 | -11.94928 | -58.75803 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6986f8ad-8f85-394d-9c07-8bd69958db72 | -11.67851 | -58.49504 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09979197-49ae-3c14-ad5f-19506141c28a | -10.04722 | -59.10163 | 2025-07-25 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91a65fb8-4790-35c0-82ae-3ed6707b6ac8 | -10.04359 | -59.09714 | 2025-07-25 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20d670f9-2c75-3989-978a-f01332b9e97b | -17.70504 | -44.30895 | 2025-07-25 05:38:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9ec83044-b3bf-3c11-a8ff-3902bd18848a | -10.15513 | -67.71423 | 2025-07-25 05:38:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15c3f09a-d103-302a-9c39-acf23bca9541 | -9.7481 | -65.11084 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7fcf088-31c4-35dd-8295-3142cdb9e2b1 | -9.04084 | -61.23197 | 2025-07-25 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e20f14b2-e78e-30c1-b1f3-c70249098d0e | -15.7958 | -41.96203 | 2025-07-25 05:38:00 | AQUA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 6adb307b-6615-3efd-9a96-cfeec94dc4fc | -11.45882 | -45.11909 | 2025-07-25 05:38:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 4adaf0b0-cb0b-3f71-a565-8db3289ebe75 | -9.92366 | -63.05386 | 2025-07-25 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 522dc9e3-7c77-316f-b04a-b1091746cb96 | -8.50434 | -64.04099 | 2025-07-25 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a3713ac-8b3a-3f4c-ba5d-d87678f13e98 | -11.32012 | -55.21817 | 2025-07-25 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8111de37-7879-34e0-9bfb-00c061a868e3 | -10.29422 | -67.48665 | 2025-07-25 05:38:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de24f00c-8459-327e-bc3b-52178df4df6e | -9.73869 | -65.10515 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44e0796c-4ab0-36e4-83ff-e696bb492861 | -9.47655 | -57.83474 | 2025-07-25 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c512c144-8fda-338d-9a1e-20803f101cd9 | -11.10241 | -60.84856 | 2025-07-25 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 935f7265-cb74-34ed-979c-291a3535e51f | -9.34406 | -58.84904 | 2025-07-25 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f84878-3a84-3f63-839c-a89d8c3e4b56 | -9.742 | -65.10567 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4b841d-a683-32ab-bc87-b54a0b1a8b6c | -11.44841 | -45.12697 | 2025-07-25 05:38:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 4116e394-52c3-3e1d-9d6b-a4817a30f64c | -11.46026 | -45.10978 | 2025-07-25 05:38:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a201cd7d-2faa-3023-9a41-cfa2bfb65318 | -9.74145 | -65.10917 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c51edc-a9f2-383a-9a09-984a7d53c30b | -9.04145 | -61.22773 | 2025-07-25 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d85dca37-1658-3f05-967d-00d8ac428401 | -9.13113 | -63.92229 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8cb29f2-2e4c-386a-8203-942b0cca086c | -11.94432 | -58.76168 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 52eedd8a-344e-30ba-a9e9-b9d300e34bc7 | -11.68069 | -58.48824 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c542a2b7-8508-35a2-9d48-21f32bf1c4ca | -13.71167 | -45.67066 | 2025-07-25 05:38:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bde00c33-275d-348a-a24a-04d291041a00 | -9.74477 | -65.1097 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003d8c93-0235-340f-ab76-ee7d140f9253 | -9.73363 | -63.4074 | 2025-07-25 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 864db922-2ce0-301f-abec-551a70a92b1d | -9.13444 | -63.92281 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99ada6c1-d80b-377f-b69a-a5040b958ce1 | -12.69036 | -46.99821 | 2025-07-25 05:38:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a60034bc-dadc-3366-860f-c4446a80c517 | -12.58174 | -56.97467 | 2025-07-25 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d57d2cf7-cad5-3b7d-8076-fb7b7c5c23dc | -8.55665 | -63.70259 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ce0c96a-efbc-3a57-ace8-be9068a257d8 | -10.04305 | -59.10101 | 2025-07-25 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f13b23d0-e17f-3fea-ad5a-19250c3eb1ed | -9.34461 | -58.84516 | 2025-07-25 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d21f46-7956-393b-b5c6-a6036c24858e | -11.78783 | -57.24293 | 2025-07-25 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baecf921-3639-3e13-b1c5-4c8be1ee1d83 | -10.36362 | -57.50143 | 2025-07-25 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 76d9357f-1f6a-3d82-9829-2ff2c28e46ff | -7.6692 | -69.93269 | 2025-07-25 05:38:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 934ea43f-ca77-3c3c-b7b6-aef03e7a382c | -11.44985 | -45.11767 | 2025-07-25 05:38:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 73fcccb2-e3b0-37ce-9377-2f744bbb1db8 | -11.67908 | -58.49065 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f54624ec-9bad-3a8c-894d-8eeaba258303 | -12.58137 | -56.97764 | 2025-07-25 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68b4f730-4b22-33ff-9b63-b721ab54b446 | -9.57775 | -64.22227 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52557762-bd59-3c3f-9d68-5c73d76a7c90 | -14.94774 | -46.9724 | 2025-07-25 05:38:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8d848561-e496-3041-9499-8f81b3df90d8 | -9.20916 | -59.68189 | 2025-07-25 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ee5ebc4-a237-3833-a068-78f6e8f514c2 | -9.58051 | -64.22628 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6140dccf-e4e3-307d-9149-352d53bea38a | -11.32058 | -55.21443 | 2025-07-25 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28eca9e9-8272-3e63-bc7b-b3e88e3c7d3d | -9.71932 | -64.53397 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf67d73a-aa89-38e8-a9d5-e28b5ae9598c | -12.22204 | -64.22042 | 2025-07-25 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c553bf79-6947-34ad-b42e-9cdfceb24050 | -9.20518 | -59.68132 | 2025-07-25 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 903c10e0-5289-3801-9409-8741e778b47f | -12.69211 | -46.98726 | 2025-07-25 05:38:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0f4173dd-bdc2-3ca1-8e1c-f013032b3c99 | -8.95714 | -72.84321 | 2025-07-25 05:38:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fcdbafb-c481-30b6-940a-e5cfcf31b519 | -11.45737 | -45.1284 | 2025-07-25 05:38:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a158918f-98c3-3578-90fc-6d8b3ea2eea5 | -11.68009 | -58.49262 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1f7c02-b862-3014-8be9-df2e8b4c85b0 | -10.62989 | -55.30742 | 2025-07-25 05:38:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26f428d2-0b8b-30fc-81cd-af82edbd7bfb | -10.04669 | -59.10548 | 2025-07-25 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f5a50d10-199e-34d7-96f9-257634b178b3 | -11.74839 | -58.34321 | 2025-07-25 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fd05f51-40a0-30ab-ae93-b4cd8b380545 | -7.67408 | -69.92948 | 2025-07-25 05:38:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5717a525-0f82-3174-9b37-55a98f58425f | -12.581 | -56.98059 | 2025-07-25 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 555df3a1-6f1b-37cb-81c3-0b5dc3794f70 | -8.65287 | -68.68135 | 2025-07-25 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e15c48-84e8-3991-9d09-1d2b666cc0c2 | -9.97344 | -64.9535 | 2025-07-25 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 878a4b3d-14c0-3f18-bd10-877be11bb303 | -11.9487 | -58.76235 | 2025-07-25 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6ac570f4-a0ee-33a2-a894-fc5dfa3287cd | -11.4584 | -45.1126 | 2025-07-25 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4da40e09-2f74-343d-945b-3696a4498e54 | -19.01724 | -54.66105 | 2025-07-25 05:40:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b26516d0-7e36-30c8-a422-4b68ef8c97fb | -18.41965 | -54.56449 | 2025-07-25 05:40:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7995f29-94b4-38a8-86ea-3c532d61fff2 | -19.54346 | -46.75997 | 2025-07-25 05:40:00 | AQUA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c1f44760-4d2b-380a-a296-0b8e0a8351c1 | -19.4318 | -44.80949 | 2025-07-25 05:40:00 | AQUA_M-M | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c55e2d12-4cf8-3916-8d2e-e7b51aaee756 | -18.42014 | -54.55933 | 2025-07-25 05:40:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4c24fc5-857f-3978-bb91-ce647b403690 | -11.4584 | -45.1126 | 2025-07-25 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 65ff855b-d173-319a-901a-bbbc8a6f9c6a | -11.4584 | -45.1126 | 2025-07-25 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 13b8c276-289d-3dc3-870f-c6a36fe37c06 | -6.78304 | -61.9653 | 2025-07-25 06:01:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 723f124c-2ee3-3447-a486-168a72bb5bb1 | -6.7823 | -61.96561 | 2025-07-25 06:01:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c1bc9b5-7ea1-3f83-81e9-07c0270e0c6e | -7.03602 | -71.69458 | 2025-07-25 06:03:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3ba7e24-ae1e-37a3-a627-a93521457d96 | -10.15706 | -67.718 | 2025-07-25 06:03:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 166ba60a-4d4a-3069-8e8e-d3397303cde6 | -9.97181 | -64.95291 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4b92235-b27b-3b8d-a47d-4cc6138596a0 | -10.05421 | -59.10762 | 2025-07-25 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 819fdfda-f24a-3a2e-a72d-ffb2840236a7 | -8.45042 | -70.09095 | 2025-07-25 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e5281cf-863a-3e49-a8d7-996d605dfad3 | -11.9472 | -58.76606 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc8bc738-a434-309f-961d-fbebb9580f95 | -10.0449 | -59.10538 | 2025-07-25 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 621a2846-be65-39ec-9d21-fc2c54842ae9 | -11.68039 | -58.48831 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfc24088-3b84-32ec-8ae0-a7575fe8723f | -9.73934 | -65.10776 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37fb2621-28dd-3825-94bb-26515b7843b8 | -9.2055 | -59.68436 | 2025-07-25 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 478916d8-be8d-366b-8ed0-a1ba5c012258 | -10.29497 | -67.48358 | 2025-07-25 06:03:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0be9741b-b999-35f8-9a53-e941df75720c | -9.74775 | -65.10905 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd25c99-770f-33ae-bbd8-6f92d21dc39a | -10.04851 | -59.10168 | 2025-07-25 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d63c6a28-7be1-3718-9180-71b9e6d9df4e | -9.20706 | -59.68081 | 2025-07-25 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df0d5d20-af47-390f-9f97-dc3e017dfcf7 | -10.04555 | -59.10032 | 2025-07-25 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0b67692-3909-3716-97ae-2900f69db5c7 | -9.71761 | -64.53381 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33254b01-a413-31e1-98e3-4ce82bf28a2c | -11.67631 | -58.48742 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98f5ccaa-a937-3f51-b2be-fef7ac2f13e0 | -8.95697 | -72.84296 | 2025-07-25 06:03:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
