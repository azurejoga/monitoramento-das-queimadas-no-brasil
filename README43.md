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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23b99df0-a2c3-388d-a699-9b2a714955de | -5.4748 | -60.25746 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3135f722-6717-3670-8b05-21e708ab30a7 | -7.44118 | -59.77791 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51c910a0-d107-3760-bf60-0ff861302697 | -6.7933 | -59.41254 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a85badb1-209e-3e7f-a718-0cbdd76f1b79 | -9.85877 | -60.12665 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d745f903-1ac5-3a42-bf13-b5130c2dac58 | -9.11671 | -61.59111 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0363bbd7-6c8d-3167-b872-5e4e1e7d30fc | -7.68673 | -50.75118 | 2026-08-23 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 68a9290c-ffe7-32c9-a5e5-4960aa26cba6 | -8.93045 | -60.72831 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18d60fc2-0ec5-3919-91f9-18dadf4c64b3 | -9.44932 | -56.90372 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d68f8c2-ec97-36b7-ac5c-cbf9064ff18b | -6.54956 | -58.53201 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6b00f55-df44-3ae9-ac34-ede88855d026 | -9.86055 | -60.11625 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c5e247d-525f-37ad-b4ab-3e343a216771 | -9.10701 | -61.59407 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c2c197a-aa3f-354b-ba0f-5fab904e748a | -10.84569 | -57.52475 | 2026-08-23 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7e065be-7a3d-3422-bb83-d20fbb3244b6 | -8.53373 | -54.85011 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec2e2255-dbd8-382e-827b-509fb19b6bb6 | -6.97055 | -59.05361 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d06e2370-d8ac-3ba3-8e8a-e77951d68a61 | -6.8362 | -59.9509 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d61845d2-3967-3085-8741-f786846ab992 | -8.5238 | -54.84852 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aee251d2-a4c0-3786-8123-6ddb787b95b0 | -8.93359 | -48.53347 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3566f6e-6f7b-31a4-b127-6bc11801cd44 | -9.39956 | -60.55685 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95b44520-b3e7-3638-ba2d-0a44a0592727 | -6.80391 | -58.9904 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49274c68-d581-377c-8581-261b95167000 | -7.57098 | -61.20577 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53a83e9b-440e-31aa-9744-bb0f9d28aeca | -8.09053 | -47.25965 | 2026-08-23 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef6b671d-f7bb-37d5-b13d-8a2fd7320401 | -6.22477 | -55.47861 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20df51c2-e66b-30ce-87a4-6b9748f028a2 | -6.66711 | -58.73041 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ac0bdf3-9a73-3d14-aabd-4e155cb5bfe8 | -6.12388 | -59.92632 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f32d59-6b98-3827-8e4b-e277383434c5 | -7.68657 | -63.34266 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21cfb432-7bb4-3470-9af6-5a85b2b436e9 | -6.68006 | -58.74721 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9fe8b8d0-e6bb-3184-8258-d2b487a49188 | -7.49987 | -60.07705 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe9ed0f-c36c-33dc-a73c-d729365c553f | -8.53978 | -54.83327 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45ca0c17-d0d9-351a-8a9b-cb05495c6d1a | -7.08681 | -45.00902 | 2026-08-23 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 196201fe-fa3b-3e9a-9141-4479413fc1ea | -6.24347 | -55.38368 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd1c0759-f28d-39d2-b616-ea4bb0f7b41c | -4.93457 | -55.77528 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89918eda-c235-3631-b28e-95388de3c167 | -6.82161 | -59.66538 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 661f7f1e-9120-35e3-88eb-0a214317571c | -6.19042 | -53.53111 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd25afc-369f-3596-9eb8-bdadd359d4e3 | -4.53775 | -55.51531 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f4a2eb3-12cd-3f23-8108-201b0ca4afd1 | -5.30566 | -49.0537 | 2026-08-23 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22435fd2-7ba1-3b47-aadb-4b59d40e0dc0 | -12.07211 | -50.59966 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32929d0e-1994-3bf5-b09a-e254375453cf | -5.78434 | -57.57621 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5034e9f-b6ee-3945-8251-f3693d7abba9 | -9.16116 | -59.47455 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae47149-585e-3bd2-8d8f-92404d3c307a | -9.44905 | -51.59173 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4e70dd5-3430-3247-8f03-bc6a22a39adf | -9.20984 | -60.76897 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54ff5478-3884-3baf-a8a5-13045f016179 | -9.03997 | -60.44382 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca5f412-f76f-3e88-a8a2-1843e585cb8a | -6.82603 | -59.96076 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 249999ef-7073-360f-bb6d-12efa0a44eb1 | -5.30971 | -49.0543 | 2026-08-23 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a22c81c-9689-38e6-9067-939955310da8 | -4.96666 | -56.27595 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 649f5f81-6897-31e0-8b12-99a96c9987d7 | -8.6241 | -54.70786 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7aa0243-a61b-32b7-8995-139026596f97 | -7.07043 | -59.97457 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c90f470f-323f-31fe-9228-57bd3da2a76d | -6.79672 | -59.41664 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52ab7260-c6d8-3c58-9d9a-2a327c2bc282 | -7.53354 | -57.65174 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecf98344-6343-3fcd-ac0e-6d0ad79b6289 | -7.65219 | -63.34418 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee3f986a-7cba-3358-a055-b792927ca3c8 | -11.61001 | -50.55489 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1ce8d52f-8a16-3bb9-960b-82e23ae28cd7 | -6.85093 | -59.43656 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 333159ff-0de4-3de4-a34e-328e095a4617 | -6.88127 | -59.41373 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64c534fa-7afc-36bb-9026-74ce06f616ae | -8.22393 | -55.02481 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6594024-4f48-3cd0-9c87-253f46887550 | -6.80861 | -58.98612 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9173c65a-4afc-30a2-ac34-d9cee5352391 | -6.69012 | -58.73429 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bfdbcdc0-3daf-333c-802b-f9202655edeb | -9.78888 | -46.61177 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7da9079-c496-3a02-963f-4c9234b15a81 | -6.15887 | -55.44617 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e7f6fe-587d-3805-bdfa-b9234c96d9fb | -10.79628 | -50.9685 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd1e6de5-1f86-38c0-985b-e3d05e4ae75f | -6.65113 | -58.80149 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd7a7ab3-eb35-3b64-93c3-161a458585e7 | -9.41687 | -60.41041 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 022dc744-a5a7-30f8-ae94-701ceacf742b | -6.79867 | -59.60218 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44581443-867a-3770-82dd-a47c63f66c4a | -9.17826 | -56.99371 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e53bc1aa-e951-3f65-b848-e29c03d377a7 | -9.85995 | -60.11973 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 066c74d5-4d07-3537-b866-bc472f517299 | -6.96583 | -59.05787 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 83a29a30-20de-3513-a741-72d111534faf | -3.85004 | -55.84861 | 2026-08-23 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| faf648a0-2483-3b7d-a56a-d44072133d17 | -6.1918 | -55.43324 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aad91d2f-164d-3a05-8cdd-cc3224c3b73f | -7.36856 | -55.67642 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49401fc4-01d6-3f8b-bcc6-faed7162d92e | -9.20825 | -59.76214 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f1211b7-3516-352e-a71d-77518a50e651 | -6.85579 | -59.46653 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0636e51e-3803-33a1-88d1-fa61cd2a370c | -8.08863 | -51.66737 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93efc2f7-5e29-392f-ba2d-06612e179349 | -9.1877 | -59.45905 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8293d07-8f19-31e2-9361-6fa38dbe4fb4 | -6.94299 | -59.07441 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b13c6a57-1e58-349d-8b07-7237bcd49bc3 | -8.52708 | -54.80631 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e63028-0c37-33f3-9c38-d0f02707f77f | -9.27597 | -60.91441 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d63f89c7-9f1b-3f7f-9e29-2ba3590c0e69 | -6.19151 | -53.52412 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18088ade-c038-3999-8680-9f3cb97bbb69 | -11.46903 | -54.31843 | 2026-08-23 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e9a07d-51a8-35bf-b529-865305f09e81 | -6.13694 | -57.85009 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 347f873d-0cd3-31d3-8907-2717fd77995c | -6.19539 | -53.52113 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5d1881d-252c-34d6-8391-6f6f80a3fb52 | -7.78689 | -61.42353 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab2eb8b5-80eb-3b04-8d28-e47d3f173a2a | -9.1667 | -59.46548 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c94d836-2822-3b76-95a9-8560af641e8d | -9.79051 | -46.61828 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8e1feec9-f31d-3887-94a5-c5066a4f22b5 | -10.53131 | -50.78422 | 2026-08-23 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7f0be7d-a941-353c-a93a-ad6d3e72958c | -8.38108 | -46.47464 | 2026-08-23 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75cffb3-bb58-34f3-85e4-18a1266a7c2e | -6.67397 | -58.73647 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 34a238ca-ee23-3754-868a-54b2be424727 | -6.82411 | -59.42483 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b71bb2c-2fc2-3517-a213-f6093d480529 | -8.52765 | -54.82421 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f75a6a-16df-3813-b2f3-d158ed0d82f0 | -9.79399 | -46.61246 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 18cb8425-ff62-3e9c-a829-d4ae15640b10 | -6.8429 | -59.46033 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4e58845-7047-3b1c-9fc1-b114b51ef7e4 | -11.58533 | -46.93676 | 2026-08-23 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e73bfd0d-9614-3f88-9d14-746bc0969cd1 | -10.70417 | -47.73232 | 2026-08-23 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d5d92f-8188-32e7-9749-53c1638560d2 | -7.39339 | -45.98708 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c56a5a0-0c9c-3f53-a23c-acc5a5b6a008 | -11.6093 | -50.55231 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e77ebdf7-c4bd-3339-8404-b3c8c3fcd0ca | -6.80643 | -59.6809 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac24a49b-48a0-3073-81b1-191bfea06828 | -6.54686 | -56.17651 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1116f210-9f25-3187-801a-6aa5ea0c801b | -6.94689 | -59.07505 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ac851a5-bdc8-38a7-8840-2e6f6006c8a8 | -7.60299 | -60.94407 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ece50ce-e08c-3a75-b1b6-3c2090643dc7 | -6.89103 | -59.40463 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3440d0e7-8c92-3c67-9577-2781bf2e7778 | -11.27779 | -50.73643 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ada9d62-a26a-3414-a1fe-b9c6a1b7a6a6 | -11.0549 | -49.50591 | 2026-08-23 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29dde339-b400-3991-93c9-c77e299ffabf | -6.95804 | -59.05653 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README44.md)
