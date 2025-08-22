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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cd43f8e-8b17-3ece-b046-14696798242a | -9.09634 | -59.493 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c569e66-0229-3ec6-b5bc-28c8d889a2ce | -6.62625 | -58.54041 | 2025-08-22 05:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27d7e4b3-da6f-3fdf-8bb3-5249cfdeb11b | -5.88218 | -53.62149 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1ccac32-10a4-3754-9f08-21da59bc99eb | -7.54881 | -63.8494 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b18fd65-7194-3e4e-9c76-85ef30195ed1 | -5.87709 | -53.61702 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a91562-6574-3c90-ad6b-5c665febd8fe | -10.86904 | -50.84187 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5528dae-da97-3877-82a4-86089bfe5c2d | -6.27218 | -53.71092 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ade1e3cf-bbbe-3f41-9475-d01cbeea5d57 | -9.51561 | -60.54603 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6d2dc2a-dd7f-39e4-a557-7d5bee176e9f | -7.94434 | -63.04791 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c804e793-54fe-3452-b556-20e8771af8a1 | -5.81113 | -59.21896 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc054a74-dc92-384d-910b-62661dbfea79 | -9.21494 | -59.783 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ca68f54-4c9f-3dbc-a4ae-532c186ed204 | -5.44574 | -60.17772 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 562179ef-e73e-38d7-8fa3-db2cf92411e4 | -5.80274 | -59.22256 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7286363d-473c-39ac-80d5-19b537c4ee9f | -10.86656 | -50.82585 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1c5ee6c8-2c53-3d95-b5c1-bc3c1055ad13 | -7.77392 | -66.9557 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8afbdbdd-4a96-36a8-8619-72b38b8e6c2c | -5.88918 | -53.63272 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c91da6c-799e-3771-bc49-b388b3758c38 | -6.89768 | -52.86466 | 2025-08-22 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ea13ead-b2e1-3dc4-8227-e6625e8810f2 | -8.6251 | -62.61395 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35195f2f-d817-313f-a2c8-cb16962a2f18 | -10.86822 | -50.84879 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6a0f4a91-e9a0-3198-b382-8cd569053ee5 | -7.05349 | -59.82782 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c14e70-880d-3aa8-ae39-f804d08891a0 | -6.43605 | -53.38558 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 670ca747-0817-3fa9-adb8-0e2cfd05f48d | -8.96501 | -61.67069 | 2025-08-22 05:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3eed5d9-e8c5-3a87-97a8-2769629f9ede | -9.52485 | -60.56123 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec0d8c79-b82e-3e7b-983b-8fa8b087f09d | -8.86762 | -62.42218 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 343491cb-f16e-3e8a-a04f-bc0a910dbf41 | -9.20679 | -59.45713 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecc906da-ceea-362d-8bb1-8397c9cf1599 | -9.2083 | -59.44685 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d39bf8b5-d429-352b-bf94-9ccc83ff85ca | -7.05727 | -59.82835 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a4cb9f1-00d3-378b-b638-aec250fd7ff1 | -9.64748 | -59.65591 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc20bc72-ed96-329f-84d7-bdde66f8b2bb | -9.61383 | -67.45956 | 2025-08-22 05:38:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37564a0e-f6d3-3e59-91fc-d3e7cf05a9fe | -9.81906 | -64.27545 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c102a18b-96e7-3fcf-ba77-c386cbe9f4f1 | -9.21588 | -60.79486 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48d2cc49-6b44-3175-882f-040e9c07c6ef | -5.87286 | -53.62648 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a64c387b-5afe-3f4f-94b3-b5e2801cac08 | -9.52374 | -60.54267 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c5b0711-fb4c-3336-8826-235ffd89cbfb | -7.29875 | -59.62755 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48f16647-291e-37ab-8af8-6a10021f0340 | -9.21077 | -59.45771 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6881697-9495-3e07-986d-6d1ab14a39d4 | -8.87161 | -62.41901 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52a91896-0c07-3492-af85-3a30b615e1a0 | -5.80839 | -59.22509 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1645efa6-75c0-31e8-8522-302909b66efd | -7.50727 | -63.83212 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 006c5b24-2822-36b5-ae60-9d68b978b111 | -9.58977 | -55.35178 | 2025-08-22 05:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836a3b56-cf57-3084-9fc6-9ccd41fee4e7 | -7.51114 | -63.82917 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0a0926e-eade-31d3-9aa8-dc9bee63b410 | -5.8744 | -53.63556 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ac4d529-247d-3164-a663-621379acedb1 | -9.16938 | -59.60188 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56712f4f-ac03-32f7-91e3-5abb734a10fb | -9.93467 | -60.52128 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65abbf0e-6242-36d0-92a3-17bc7a71db35 | -5.88147 | -57.76007 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35f4e5aa-535a-3967-9160-65927b467a84 | -4.0937 | -60.6666 | 2025-08-22 05:38:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 645d646c-7fc4-312c-a397-20532a9d41fa | -9.20917 | -60.78948 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 693fe12e-7945-3be3-8fec-a0909f7cbfec | -6.44261 | -53.3887 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f8444f-ddb2-3d05-ab92-b8b42145dab0 | -7.5621 | -63.85151 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bcfc268-f404-3676-8843-337ff9227b27 | -6.26625 | -53.67194 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc35a336-d654-3667-be40-48ba96693ae2 | -8.0454 | -70.19229 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca83ea08-bb5f-3d0b-b1e0-edb3286572b8 | -7.101 | -62.97094 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c4192e9-7765-3066-b306-760e93b2e11c | -9.18215 | -59.62431 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b81cc410-c1d4-3f9a-ba7f-c394d05796d4 | -9.94653 | -60.17696 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 978c1c7f-0849-3cbc-9bfb-d1ce69ca283d | -9.2172 | -59.46908 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea297a69-2d0f-3fef-b1fd-97de2df5b89d | -8.86535 | -62.39155 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6510cda-6d22-349d-b684-df1f7e392459 | -5.89167 | -57.74971 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 114711a4-dfe5-3663-87ba-55569a6f822d | -8.66299 | -70.0348 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdf0fb28-0bd4-38b1-897f-77cf9a6020dd | -8.71398 | -69.45719 | 2025-08-22 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c490ed3-5964-3a91-90a3-59f247d91c41 | -7.62904 | -69.94512 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8943dec5-3a53-36f5-aff0-8d69e475d1eb | -10.85944 | -50.82496 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fa84c740-a165-3de9-b972-10b782e28a38 | -10.87213 | -50.84068 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b19900f3-1ed0-3e2e-9546-493be8d79a1e | -5.80659 | -59.22312 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b10e284c-032b-38d3-a90b-4bdbe8c76953 | -9.65752 | -59.64206 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7d40cb1-9bdd-33d9-bcc0-b0b778378d0e | -15.8955 | -43.4523 | 2025-08-22 05:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 98cff8d6-5b6c-3283-aff4-121831181056 | -9.1353 | -46.38005 | 2025-08-22 05:40:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 866d709b-dd88-39ab-81c6-1706b239c007 | -3.62695 | -43.54178 | 2025-08-22 05:40:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| af300600-6b9d-3602-aefa-ac7f9540d370 | -7.63973 | -45.24286 | 2025-08-22 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 21dff271-50ee-364b-b73a-133d3790d57e | -7.85523 | -46.99099 | 2025-08-22 05:40:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 73d92f28-ce54-34c6-bee4-eaf140edf4c2 | -3.97938 | -43.23846 | 2025-08-22 05:40:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 290d15e2-3b2f-3971-8ec3-b147f8438cab | -6.02525 | -42.84537 | 2025-08-22 05:40:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f8d4412f-033b-318a-8dbd-9daa4ab95a6f | -6.43721 | -44.51901 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4b4ca836-6d08-3a13-b5bc-02959329f840 | -2.47296 | -47.76038 | 2025-08-22 05:40:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 11d129dc-1971-3ba3-86d2-80518cf79f46 | -6.71101 | -43.2024 | 2025-08-22 05:40:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 72fbf5e3-d7ea-3db7-b122-77bb5d0049d2 | -6.93597 | -44.28183 | 2025-08-22 05:40:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bdccae4b-4b17-3f0a-968b-64ae3dc56598 | -2.25071 | -47.84882 | 2025-08-22 05:40:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a05d6ee1-c04e-36fd-98b6-eaf973ca1441 | -7.63211 | -45.23193 | 2025-08-22 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 63f99b96-bfe1-3f30-9c14-238dda2d1508 | -7.63062 | -45.24148 | 2025-08-22 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4a19b2af-095c-3d24-8e41-6b033d26ada5 | -7.64123 | -45.23328 | 2025-08-22 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c5c686f7-4093-3fa8-96b7-e5a2c8fab7e1 | -7.60666 | -44.37716 | 2025-08-22 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5c6b2cc-8ce6-3947-bd7f-24c235ea4089 | -7.26911 | -43.67029 | 2025-08-22 05:40:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 053389d2-29bc-3dba-993d-5caada293e94 | -6.42964 | -44.50853 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 572476bd-a801-3409-b43b-dd1219c268f8 | -5.14315 | -45.1738 | 2025-08-22 05:40:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a863463a-471b-3f2c-8d57-6529db9c9e3c | -6.03686 | -44.35952 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3241727b-3d9c-3cd0-943d-56f4ec23a323 | -6.06666 | -44.10512 | 2025-08-22 05:40:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94276283-aae4-3a6a-ba03-31a915e51188 | -7.1651 | -44.66591 | 2025-08-22 05:40:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 22753f5d-f7ce-3ac6-b98b-5dc859b69448 | -6.02657 | -42.8366 | 2025-08-22 05:40:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 53678243-c2c3-31c9-8f5f-4698c692751d | -6.42399 | -44.67349 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fcf882f9-06f5-3d42-8dad-874f3d0d99aa | -6.50248 | -44.58138 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| da3f0b22-7d4a-3944-b4b1-aca0470ba383 | -6.51144 | -44.58276 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| dd86f36e-2017-394e-b8ae-de8f5d7202f7 | -6.29248 | -43.89598 | 2025-08-22 05:40:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3817456-7d37-342d-a25f-0b085fb1fc86 | -7.62165 | -46.25367 | 2025-08-22 05:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3de05ad3-181b-343f-99ea-d8ecdd67f992 | -9.91387 | -46.19687 | 2025-08-22 05:40:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b887561a-7a96-3b10-8b7f-21abd7aefb22 | -6.93461 | -44.29081 | 2025-08-22 05:40:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9607f5ee-e555-306f-809e-a117952ae20a | -2.47041 | -47.77682 | 2025-08-22 05:40:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a3790c15-9cab-341c-9c40-4a06f112f425 | -7.61046 | -45.25235 | 2025-08-22 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 34066eea-e132-3baa-b2d5-2b85abac7097 | -6.42824 | -44.51777 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a4fda55a-40ff-3fa6-91fa-6002465b354d | -3.22598 | -46.78006 | 2025-08-22 05:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 57dab185-da90-326a-a841-d89e8ce5c3dc | -3.23371 | -46.7746 | 2025-08-22 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5e42cbf4-05ca-36b7-baae-312468362505 | -8.49574 | -45.68352 | 2025-08-22 05:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4cbdc07e-18fc-3724-ac3f-b8e18d29d8ac | -6.63608 | -47.89436 | 2025-08-22 05:40:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README59.md)
