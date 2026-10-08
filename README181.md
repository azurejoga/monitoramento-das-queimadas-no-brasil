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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cca592d-a47f-3bf5-87da-23a5ff2482e2 | -2.92874 | -54.12283 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 278bfdaa-24e9-368c-b719-13d5c7b4af95 | -3.54971 | -59.4726 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61065632-9e44-382d-bf75-c0d543677f6c | -5.28972 | -60.10411 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e85fd0cd-d426-3074-b464-ca9449f89f68 | -3.07581 | -57.75264 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3bea0f83-18d8-327a-ac18-44d5a461ad9e | -3.97604 | -56.1195 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4969f823-5ed7-306e-a4c3-7206d5893c5d | -3.86533 | -55.99865 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b4e2b89-bb42-35e3-a797-fb871044e99b | -3.22873 | -54.30376 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b656cf6-1807-3272-bd22-be4167f86ebd | -3.29774 | -54.05086 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4cf7cb9-5fa5-37b7-9607-37babd1a4b5a | -3.56329 | -59.48384 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a771d28-e150-341e-9184-ea9f196b240c | -4.77441 | -55.74049 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a49bb09f-a088-363d-8b1e-21152e469d1f | -3.01077 | -54.07581 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afdc91e1-b2f5-38d9-94b1-1980ba8a1c45 | -5.29175 | -60.09108 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79201986-a16b-3d89-8d68-6dcd1ac98cbc | -3.0965 | -53.76305 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8f414c53-0d39-3b0a-9ce4-a2306c40daa2 | -2.86866 | -54.16316 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c461a16-0d61-31bc-b956-42138c8f75ea | -3.27652 | -54.06129 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd1f560a-87c9-3ef1-a0f1-3b37f8ff8369 | -4.05633 | -55.32402 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5aa5229b-628e-310d-b587-7ba239002726 | -3.10947 | -54.16795 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c0c523d-f99f-35ea-a87a-9f64c1393353 | -3.959 | -56.12057 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c1fb41e-56a9-36e9-8dfd-1946f8888b3e | -6.23879 | -52.86084 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e8a60619-a7b5-3bec-9ad1-416182674c7a | -2.94514 | -54.12181 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f5880b-a120-3414-9c11-fc0368093de8 | -2.85703 | -59.26722 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47319d6c-96b0-3354-93df-b937d38653f6 | -3.24961 | -56.80628 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b927f41-d4a6-3308-90f7-ffef799ee022 | -2.76925 | -54.11154 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9a6efa8-8a88-3044-8c78-4348cb928955 | -3.03077 | -53.94236 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b67c4bd-b429-34bb-a8f7-72f50232b500 | -3.3036 | -54.02738 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31249519-afb2-35f2-b36f-c2b21daf5fa9 | -3.07387 | -54.26197 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64f1d9d0-ceb1-332b-9eed-109ff94adc86 | -3.05425 | -53.93224 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fe752cb-f884-3c3f-ac79-abd81ad12105 | -2.79428 | -54.08883 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a493e26-97cd-3edd-baf9-6e1976401300 | -5.82232 | -53.83688 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2e637d1-8a63-3aee-9835-b46db94b4c79 | -6.72937 | -63.04988 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a64403ba-082e-3da4-852e-239366e2abfb | -3.58059 | -54.67686 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ef007ff7-534b-3659-831d-516a765d8fe0 | -3.00645 | -54.06841 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 744f065c-36fb-3beb-805a-640e1e63e0ab | -3.84841 | -58.89944 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79576235-59d2-3492-a003-13b2eade0f86 | -2.49399 | -58.07656 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e724342-1d28-3a81-843c-4074fc48ec7d | -6.26191 | -55.99412 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7a12c18-0d6e-3fed-8d7b-1eb598cde5fd | -3.16279 | -54.73638 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 048261e4-f2c6-3739-b56a-aa2f6889d2ad | -3.04918 | -53.96572 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 5de8115b-e5ca-3419-b309-b598a96f5468 | -2.48487 | -56.1294 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9eb0e62-f5f5-3139-86ea-437ef063b51b | -3.04276 | -53.89909 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 631d22e6-0c47-32b6-bc2e-6992553af6a8 | -3.27119 | -54.06048 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35c13d94-8c8b-3d9d-93c8-09c5e41b087f | -3.67768 | -55.95215 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba035f1-c46a-366b-b403-2402f0c25d48 | -6.23405 | -52.85088 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02acaeb9-7d84-3ced-9178-83664313930c | -3.18525 | -50.56301 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e35d851-24ad-3312-8fd1-33ab60e7f76d | -3.01892 | -54.09389 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bb7ae96-a13b-3505-9052-c567b9306a05 | -5.29912 | -60.08632 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9aeb215c-125c-3c9f-93e1-b8112564f386 | -2.0394 | -54.48565 | 2026-10-08 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53e5fea3-9b6c-37ba-b5c1-fe7e3b540ced | -3.07315 | -53.9523 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5ebbde58-c0f7-325c-b7e2-e286ac0cafa2 | -6.98824 | -59.11894 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c2cf1ca-458d-3495-bcb1-9cc5ec2e296e | -3.46394 | -59.57491 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccc1b69f-500e-3389-9650-2d29100cad78 | -3.01707 | -54.07005 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 054962e5-ded8-3908-9c9f-f5a92a7bcd23 | -3.00448 | -54.08159 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0c672148-f7d0-3c5f-8e53-a15b97906082 | -5.34152 | -50.98619 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b639a834-0e3f-34ae-8684-3902b66b688b | -3.07721 | -54.27553 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9d487b3-b9a4-38d7-8c6b-a8622fa1c5d5 | -3.688 | -60.56047 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf7d352-0a26-31f9-a00d-dbb32a1199fd | -2.47469 | -56.10394 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe0d2d7c-acfa-344d-8067-0ab4902f81bc | -3.01807 | -54.06345 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6a15ef5-785f-36a6-a154-13e5f60f8d44 | -3.52347 | -54.67199 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b68051d5-5503-302b-9e44-0c9cfe32da95 | -3.56159 | -59.46987 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc96ac2d-1c63-3e69-b982-e70b1be105e3 | -3.96816 | -55.83955 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0d766e3-46dd-311b-9d4b-3b6edda791ca | -7.90371 | -54.71653 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be7902b8-2759-340f-b47c-41105dddd26e | -3.11955 | -54.17279 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 887224d0-9f7f-3608-bee2-cc36ad1d013c | -3.24519 | -56.80561 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 085a46a2-cc14-30fe-9c4f-74940696c18f | -3.5792 | -54.68612 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1a9a415c-80d9-3ab7-b86d-5e1fc254c2e6 | -6.99325 | -59.11263 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe3a7016-5183-3414-9f56-8dd8277905be | -3.25922 | -54.03126 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 55fc924b-4077-3873-8ea6-7c314877569c | -3.51409 | -54.66423 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e950e4d-5034-390d-8423-df01fd22f36e | -3.28388 | -60.99123 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb34533-26f2-35d8-8efe-1ef3921dcec2 | -3.13919 | -54.3657 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4343ef43-e10d-3f1f-956b-c469dcc8d5e7 | -3.54741 | -59.47885 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 757ef444-92a1-35a7-b85d-aeba137d3ca3 | -2.94256 | -54.06787 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d7bafc0-3730-3b61-bf17-f8c37bbb9431 | -2.84601 | -57.46748 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93b49350-9b34-3f4a-bc76-60ed5bd20868 | -3.30112 | -53.86382 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c0f0ae9-cd72-3f58-98b1-9c4aaf9d3fd5 | -3.25767 | -54.68066 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91e60b6d-b761-39d6-a49e-9c65c864612d | -7.21374 | -55.08854 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5437a51-1a07-3056-83e7-32db14d3832a | -2.99086 | -54.13647 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32805096-e3ea-3dc2-a851-1a1caaeccba9 | -3.54116 | -50.10417 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22cbbf7-a29b-35fb-8e4e-528a007bd0e2 | -2.51571 | -56.26159 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fbe7f66-1dd3-3db1-8d91-3a5225959433 | -3.05863 | -54.22316 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39e2fe71-6b00-3d95-aa51-ea96d95cbb5e | -4.75707 | -55.67085 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a615969e-5176-3fae-9dc1-22d89877072d | -2.97798 | -54.04032 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ee35f09-42c4-36da-b0c5-a079bd0a93b5 | -2.77022 | -54.10505 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 729dab59-8e48-38ab-8755-470a57b76da4 | -3.02289 | -54.06755 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a29120c-e78d-35f8-98c4-87268832c860 | -2.98558 | -54.1356 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e94d06d2-af91-36e3-9343-1e3ddea36acc | -7.00423 | -59.12136 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7e401668-0f6b-3c9d-88b6-0c03f72e57c9 | -3.0563 | -53.91866 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dec9b986-d36c-3704-8ba4-d0e4847da095 | -2.88998 | -59.20305 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b20e3f34-1502-34c6-b37f-1ffe4768fc82 | -3.02945 | -53.91452 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c91ef71-993d-3aff-9e91-dfd46b0698bf | -7.00372 | -59.12481 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a7930bdb-27f0-30b4-8d46-b7a67adcb3d2 | -2.99574 | -54.10376 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e501c0dc-bfef-34ac-b248-ab1ee05b95b4 | -3.69403 | -60.54513 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3870f890-9074-3e63-ab46-c12ff0d03e64 | -3.30744 | -54.05924 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 932e4f8c-e19d-3590-8dda-fe73594f295f | -2.72481 | -57.46943 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa402be5-e31e-33c3-b0ce-6c33e3b7edff | -5.70903 | -53.49924 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 95df324f-f032-321d-a94e-b823bfc8ee33 | -7.74738 | -54.95052 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a9e4d51-c8ac-3817-a9a1-d47d95ff0245 | -3.07671 | -54.24281 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90e4dfe1-8309-3f5b-9ce8-28d890cc3098 | -2.94424 | -54.15942 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 908d5e6d-3b09-3f54-b3e1-40104f49ef87 | -3.58969 | -54.58078 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95fe715f-3796-32c1-a2c8-04e435ba590d | -3.72381 | -54.2171 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 686cc8a0-75a0-3e41-9971-d5f404226f45 | -3.10961 | -53.7863 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1fdc2ce-1182-3749-80bf-9f9604bab175 | -2.94306 | -54.06459 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README182.md)
