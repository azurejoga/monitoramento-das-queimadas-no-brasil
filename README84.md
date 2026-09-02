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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bae8cf54-83c5-3513-8f50-2271416f865b | -12.1316 | -47.1084 | 2026-09-02 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| a384b6c6-0535-38ac-a45c-69e27632e3ac | -3.7533 | -59.3231 | 2026-09-02 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ba7bccf6-81dc-392d-9109-68764999967f | -7.3117 | -60.6089 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1b28e0b5-9a37-33a0-85a5-c25288bda068 | -12.3626 | -48.1459 | 2026-09-02 15:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| e661f42c-7e5e-3808-8721-d760def45885 | -7.2536 | -61.1074 | 2026-09-02 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a8ea5c6f-22bb-38d2-84f2-10dc109bca95 | -9.4538 | -45.6228 | 2026-09-02 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a9fe36c2-e2be-3567-a0e0-2705be544a70 | -8.7628 | -46.4642 | 2026-09-02 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 03993876-e816-3281-ade6-1dbd91f459ab | -11.5287 | -45.4703 | 2026-09-02 15:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 20ea0e9f-21d3-3df5-adfc-36fdaf704ac2 | -10.3953 | -50.0132 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 08fb159b-59e1-38a2-ac97-da04d958c168 | -12.1504 | -47.1283 | 2026-09-02 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| d291ff6c-cf0f-3fa9-b547-ff4d3601dd34 | -3.2361 | -61.217 | 2026-09-02 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 2e44b959-a85f-3253-ae14-6668728537ff | -10.4145 | -49.9898 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 302.1 |
| 15d7ef9a-d1ce-374a-9d9d-4e4a55689329 | -6.8018 | -59.4201 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 98807cfa-7ea0-3992-b163-0c82e578540d | -6.6542 | -59.426 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 49190685-c3bf-3921-b091-398c28faaa66 | -3.3452 | -42.8067 | 2026-09-02 15:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 591.1 |
| 750096d0-7d8c-3e6f-98fc-4fedbb3970cb | -7.4735 | -61.3846 | 2026-09-02 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 23d6e73d-34a3-38d7-a511-1e00fd672dd0 | -9.043 | -65.4175 | 2026-09-02 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| cd046c1d-78dd-3f62-b865-992092c72eaf | -12.132 | -47.086 | 2026-09-02 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| e73ac0bb-64bf-3204-a507-118ec93463e1 | -10.3385 | -50.0191 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 59244f7b-c517-3527-9ee4-1661ee11b3c5 | -10.3769 | -49.9723 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 224e8d80-1cb4-3d06-a76f-25004101f1ba | -6.8203 | -59.4001 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 290c5202-6130-3272-b4ed-2e7f25e59d67 | -11.3615 | -45.1955 | 2026-09-02 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| afbff78a-fac7-3bab-b011-a639faab3c33 | -7.2006 | -60.6706 | 2026-09-02 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 8f2f1fd3-5a99-3660-8a7a-5c3db3c30da7 | -9.8619 | -64.9958 | 2026-09-02 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f775d456-c065-364b-a11a-ae8859b553b2 | -13.5531 | -59.7574 | 2026-09-02 15:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 734fa79f-a5bd-36ff-9d54-deb1a2290820 | -14.6145 | -53.59 | 2026-09-02 15:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fa437f04-1bee-3ef7-aa64-6f7b815a77e9 | -13.5533 | -59.7377 | 2026-09-02 15:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a2d28f31-d6e5-3896-a192-0248552000f5 | -7.688 | -67.1262 | 2026-09-02 15:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c5c8efdf-d76f-31a8-83bd-2871b092a576 | -10.1134 | -45.8621 | 2026-09-02 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 562bc251-2861-3f02-8336-ed235cda0f2a | -1.0182 | -53.7189 | 2026-09-02 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 9697d5b6-a69c-33a9-b64b-ae49890d6ce9 | -5.5649 | -60.193 | 2026-09-02 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9912dfad-d12f-37f9-b67c-073c6e054dcc | -3.0347 | -61.4846 | 2026-09-02 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ccdb2317-43d6-350c-97e5-d072ea2da114 | -6.8757 | -59.3978 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| db977a8a-ffbf-3d96-bfb1-e39720e693a1 | -8.8925 | -62.3538 | 2026-09-02 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 56df41cf-1566-3d74-92fd-ae9d344cc53d | -5.9451 | -57.6906 | 2026-09-02 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a2e7c2e2-f000-3f77-b9e4-57c15c7fc50f | -5.9635 | -57.6899 | 2026-09-02 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 007efd99-1313-3e2c-be24-19a016f99b7a | -11.3806 | -45.1928 | 2026-09-02 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 6a2b1900-6bcc-3a14-952f-b2b0d662c6d7 | -6.8019 | -59.4008 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6d729782-8f44-34f0-a21b-70ee701451f3 | -3.8263 | -59.3982 | 2026-09-02 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9bdf5404-6032-3d49-ba7e-6ae638218a3e | -3.1998 | -61.161 | 2026-09-02 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9e3a9587-dc6f-343a-8240-2e09b927009c | -3.3871 | -59.3883 | 2026-09-02 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 5f1170c1-90f0-3ec2-bcd1-0d07cc29b10f | -3.6215 | -60.566 | 2026-09-02 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 142.1 |
| a6229117-57cb-3666-8bb8-5ff0e39fefc0 | -13.5724 | -59.7362 | 2026-09-02 15:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 8066649e-9fad-31db-a4be-409ec1ee661f | -3.6216 | -60.547 | 2026-09-02 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 45265384-76a1-3148-b318-1fd5b6b4e787 | -1.5116 | -54.9546 | 2026-09-02 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 69246c91-4126-377c-a22e-b995cf1f693f | -6.9872 | -59.2582 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c860bcd4-81b9-35b0-a603-bc6c9936aa99 | -8.7814 | -46.4847 | 2026-09-02 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| d53dcfd3-a68f-38e8-94d5-68e075de62c2 | -10.3574 | -50.0171 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e8f8179a-e665-3fed-b799-8f767ff170d6 | -11.0244 | -49.6872 | 2026-09-02 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| dc3394d2-7d89-3e1b-af4c-52c6b8062326 | -13.9853 | -58.6919 | 2026-09-02 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 68461e4a-755a-37e0-ab89-f427220d7a2d | -6.6358 | -59.4267 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b7abed2d-acac-348a-8ea2-47d14eeefae3 | -6.7463 | -59.4416 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d9d78f0c-35a3-3dac-9426-274166c3e5a2 | -12.1312 | -47.1309 | 2026-09-02 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| a3db6a70-8b41-30d5-89f7-da1e66a75ca0 | -3.3264 | -42.831 | 2026-09-02 15:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5a555453-831a-3219-9e87-24b48b9d8138 | -5.975 | -55.7022 | 2026-09-02 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 46622476-e579-3352-8c74-4049f7fb62a5 | -6.8183 | -59.7658 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2ddc87d2-ec3c-3991-848a-51dd02178880 | -3.8446 | -59.3977 | 2026-09-02 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c331935d-9fa3-3378-ada5-fbd9bb23aace | -7.0428 | -59.2173 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| afc17c2d-f270-3740-85c2-088f121b54ae | -7.0427 | -59.2366 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 7b2ddc64-89cd-3ed3-9d56-51483a84346a | -11.1534 | -51.296 | 2026-09-02 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2eac3985-4e22-307f-b923-eaf2f36ca5c0 | -9.2144 | -47.99 | 2026-09-02 15:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 167c88cb-4802-3bd7-8f76-d0e64f00a5bf | -7.2007 | -60.6515 | 2026-09-02 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 62153024-83d9-3f78-801e-abea92bd5d65 | -14.6342 | -53.5666 | 2026-09-02 15:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d2e7a636-1efd-31ec-a400-5cf1022d4ca7 | -6.7833 | -59.4208 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 38608795-a2b6-358c-bf58-d20b500a2dd4 | -6.7648 | -59.4408 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 208.5 |
| f2cfa4cd-10d9-3164-9e27-519c2d874183 | -11.0434 | -49.6851 | 2026-09-02 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 6f1176e7-e400-33a2-b10b-ef501bd75a1f | -15.3841 | -53.8282 | 2026-09-02 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 664ce2ef-7050-383d-8def-709d23b280bd | -15.3057 | -53.8802 | 2026-09-02 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d747e9a8-54ac-3a39-a0eb-c4b2674b07db | -3.3688 | -59.4079 | 2026-09-02 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 4ff23945-a77b-3ed6-b464-5604d18340aa | -6.6883 | -59.9436 | 2026-09-02 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| e2da8c3e-d28e-311c-aae4-43481655dbab | -3.2179 | -61.1985 | 2026-09-02 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6f91c7d6-0f03-3a88-b4f6-fa4b1adc118e | -8.5542 | -63.1814 | 2026-09-02 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1bfb33f1-840c-3917-9ad8-97eb1d9b763e | -7.3672 | -60.5875 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 7537fc34-decc-3cb8-b2b0-9a69f7fc8996 | -13.9855 | -58.672 | 2026-09-02 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e6cc22ec-04e9-38dd-a7f2-48f0a63a66e8 | -9.0245 | -65.3994 | 2026-09-02 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a75f0aa3-515a-3051-807b-e620f7643753 | -15.3647 | -53.8307 | 2026-09-02 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3650f7d3-a342-313c-b152-46483db5a25a | -12.0933 | -47.1138 | 2026-09-02 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 3748af62-1d7c-3ef4-8765-bcaf5881f24e | -11.0437 | -49.6635 | 2026-09-02 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d306263c-0e61-33f9-a0ff-24f9968559c9 | -10.3956 | -49.9918 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3e194f59-13e5-336e-9bc3-41973c2f55e7 | -10.4142 | -50.0112 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a3d47369-d0f3-3b60-8b81-050e4c422db3 | -13.5075 | -51.8728 | 2026-09-02 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d260de1f-caef-3b1c-90cd-6419e559da7a | -11.1531 | -51.3171 | 2026-09-02 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 30d2e2a9-bc03-33c9-9c9c-b749d1a96a10 | -7.2005 | -60.6897 | 2026-09-02 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 160ec5f7-ac68-3851-87fc-466f46b85701 | -2.9447 | -60.9002 | 2026-09-02 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 27285745-f978-386a-8347-3245362f6401 | -8.7817 | -46.4623 | 2026-09-02 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 1288fc09-105a-3a48-bb30-503ab6ec0747 | -3.3871 | -59.4075 | 2026-09-02 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 2bc288cb-59b1-3ed3-8e0e-3e9f1092828c | -11.5479 | -45.4676 | 2026-09-02 15:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2c29dfd8-f5f1-3389-9810-30de5e4febfc | -14.6532 | -53.5852 | 2026-09-02 15:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 849d138a-d518-32d3-b640-d9706f886fde | -8.739 | -45.3844 | 2026-09-02 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 839fe900-b5f4-3a80-b0ce-773ee964cd70 | -12.1128 | -47.0886 | 2026-09-02 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e8811adf-95e7-3611-ad6a-00889acc8e95 | -9.5004 | -66.7831 | 2026-09-02 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 8940d972-3f98-3135-b1cc-2bafaa647c69 | -11.0247 | -49.6656 | 2026-09-02 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 57a48d97-bcc3-3f38-b665-0e058851b411 | -1.5805 | -47.7462 | 2026-09-02 15:20:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 87fd05a5-67dd-36a1-9b55-a090e71c8a7e | -8.8925 | -62.3538 | 2026-09-02 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 57e122e2-561e-36da-a129-d4710b09860c | -9.6676 | -47.9429 | 2026-09-02 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f70d0750-134f-33b3-91f5-39ef038428dd | -12.01 | -60.5345 | 2026-09-02 15:30:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 48a72df0-2715-3387-932e-7518261d608c | -3.4595 | -59.6548 | 2026-09-02 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2e8cd623-40e3-3697-bee5-81fd6f3b89bd | -11.3615 | -45.1955 | 2026-09-02 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| d71901b1-2b08-3cb4-b9b1-df31bb2f2038 | -5.9451 | -57.6906 | 2026-09-02 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| db359ddf-84d9-32ac-9148-069bb57e9b47 | -10.3953 | -50.0132 | 2026-09-02 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |


[Clique aqui para ver as próximas entradas](README85.md)
