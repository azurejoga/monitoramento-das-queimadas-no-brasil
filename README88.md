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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1560bbaf-e699-3a36-b57b-0a1f95c7c143 | -4.77266 | -55.72914 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ab24567-f240-370f-bc2f-d064e2b947e6 | -7.43744 | -55.57408 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45777bb5-bde2-3e6b-8384-336b2bd31812 | -11.302 | -44.83068 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7168928b-aea9-305b-b6a4-d08a23785a69 | -2.48555 | -56.10643 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6314f73b-d53e-37d9-83fc-06f0622330e8 | -6.39301 | -55.19066 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 29c8d76e-d941-3cb1-b357-ffeca2dc2f62 | -3.7375 | -54.65166 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ca30cf65-ee46-31fa-9764-a203e103b3bb | -3.55751 | -59.4799 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 811a6939-d918-34fd-9398-75146240cd71 | -3.29202 | -54.06874 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfe5b223-2c4a-32dc-8905-f64a1a2be8ba | -7.90167 | -54.71743 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e3a6b6f-0d9e-389b-a4ad-de4b2bcb3607 | -6.05603 | -44.02515 | 2026-10-08 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6050a6da-e250-365f-86ac-2af8f224b5b5 | -8.72568 | -45.16883 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e828e705-7dc4-3cf0-a657-45099b3b3253 | -6.07796 | -53.76633 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0521086f-247d-3477-bbc1-bf9ec3ef58f5 | -7.39059 | -55.19914 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6644d2db-df83-39de-ac1e-db99a64f4322 | -8.08119 | -55.28827 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4cfbddb-a597-3d85-ac61-5fe2ba43f01c | -3.05458 | -54.03127 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 753ec96e-2fd6-3352-bcdf-a5bb73f1c155 | -3.28959 | -54.03737 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f635a5eb-d04e-3689-b367-a317b8d7f111 | -5.24818 | -50.91291 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6993d92a-2850-36ea-804e-f27b4576f2a6 | -3.36869 | -50.48355 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbb22233-1a1d-3751-9739-463c63ed6e1f | -7.20824 | -55.09934 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 020fecc9-0555-35d2-ab5a-3130eedfea91 | -8.08189 | -55.30661 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a7ecca6-e922-3afb-8d49-8cc2b400c3fc | -2.94447 | -54.17567 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62822771-0c3d-3868-800a-46ef9ab66c0f | -3.08076 | -53.96008 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ef72c3d8-2f8d-326c-bf01-58f9f944848e | -6.5098 | -55.40226 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4eed8b0-1176-3032-b129-e368ae140bf1 | -2.58437 | -56.16651 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3897f55c-6b6a-3df8-9a1e-a588a4b87401 | -3.79192 | -50.87017 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1de19e-7dad-34fc-9f98-d5c8b7286eb4 | -5.91774 | -52.11106 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48cd106d-e1ba-3627-addc-3d2265caccea | -3.01412 | -54.09627 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 269d949c-41df-39f1-a37d-f21d2754f3d9 | -3.59069 | -54.67026 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86f7508e-e3d1-3344-971a-079ff8cc9bbd | -6.3705 | -55.46886 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e335a2-8a29-3636-ab93-f1d4241b8112 | -3.29727 | -54.08288 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a0e95d2-0e37-33ba-b265-fc4e72549c00 | -6.23158 | -52.85578 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50813a1b-e5db-3e40-be54-6b4bac163c3c | -3.65531 | -54.28699 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e189eb98-9944-338e-b36e-1f07be73b6be | -7.00715 | -59.12701 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7b4cf8c1-d868-3ccf-8dab-60c6e3b4090d | -3.99746 | -56.25619 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1381de6a-eb01-3e06-ac1c-2b03bf89d82d | -3.05019 | -54.15587 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af6f874e-f718-3530-b7da-33828ba0be8c | -3.27197 | -54.0316 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 266d7af9-904e-3040-b86c-152183da240b | -3.84782 | -55.98701 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1eafb7b-7f23-3c96-8001-f85437b6c2d1 | -6.23613 | -52.84904 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2d996aa0-ee2d-34ad-a619-227ac8113059 | -3.1895 | -58.65177 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 947b42fd-1870-36cb-82ba-e65fcbb3ac3f | -3.31318 | -54.05428 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 28b8925c-c6a9-32ff-9c64-48cbb6936045 | -3.57703 | -54.65854 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0895057-fec6-3cec-8668-35e50a19bace | -3.80287 | -55.70205 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e41ea745-045f-318d-bdda-b3230f74b4b6 | -3.00194 | -54.05412 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 76e0b270-f202-3539-b74d-f0d9b49a099a | -11.20139 | -49.4211 | 2026-10-08 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6222d1e2-754d-3b52-be64-af754ca06b6e | -3.0588 | -59.2658 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19535a00-2063-3f4e-b17f-4bcf2a3c6591 | -4.81295 | -42.749 | 2026-10-08 04:46:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf89a5ca-d44b-35f0-bd16-7ccce82ca32b | -3.05187 | -53.92916 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33388189-9d5d-3221-9384-5eadb3b38c0a | -8.25221 | -54.72932 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f28b4d48-1a7f-3aad-a14c-2f79d8de6525 | -9.89981 | -44.79837 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b76ebff4-5804-377c-8a9e-660a8405a5d1 | -2.77597 | -54.10685 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80183115-47a2-39c9-bb5d-130d2423adce | -3.55435 | -59.49908 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20229cd4-948a-382b-8cad-a07bd8027436 | -3.32815 | -50.17511 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8cc898d-3e92-34b7-8348-6033add10137 | -3.27969 | -54.00636 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6d1a936-b2f3-3732-b64d-8d8bceff2db4 | -6.51057 | -55.39758 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53db9424-d9e6-346c-8676-6091aa863935 | -11.24734 | -47.55327 | 2026-10-08 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc394f21-6482-35c7-8907-379abfb469f8 | -3.44484 | -56.94231 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55efedbb-3ff4-3260-a98c-b3983479714a | -3.71601 | -54.23204 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b37fc780-c918-3f6c-9cd3-92f272a27533 | -2.7793 | -54.06227 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c631d911-536a-378b-b808-81e3a479db12 | -4.03591 | -48.21445 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2a5df27-de56-3906-b2ae-f6c2e7009e56 | -2.8428 | -54.0677 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6015b448-914e-38c8-ae80-a6fd15f6f6e4 | -3.24976 | -56.80766 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67ed877d-deaf-34ee-b486-79048b6bd2ef | -3.01664 | -54.1281 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8f57b07-4aec-3c37-ad72-65cac51a7ba6 | -10.42412 | -47.28101 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2f88887e-84a3-33b9-8542-5e25b1e140f8 | -2.50784 | -56.18289 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9723e72d-3a3b-3230-912e-51bf118b1335 | -3.83736 | -55.97399 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82a491da-5e31-37f9-9d64-ae1cd0cca361 | -2.8369 | -54.12986 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fd716a7-ca03-37dd-a9a0-4c1e4c351f54 | -3.71077 | -58.549 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8fbd6fc-699d-3130-9f9c-90733bb36ee3 | -2.9312 | -54.07616 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4629052e-63a6-3f48-986c-261a677aa74c | -5.28925 | -60.09202 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75aed53b-fc9c-396d-9ff1-98789f33f01d | -2.47836 | -56.09727 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51a9064d-5093-3b10-8ac6-c67a47ddb1c7 | -5.23936 | -50.9045 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f4454c8-ccbc-3c13-8571-e5e7502e722b | -3.546 | -54.65835 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cec0f18a-9057-3ff5-90ee-af1bb70853c1 | -2.77579 | -54.08421 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6aee3bfa-c76e-3b59-8c70-2ffbe9b204d7 | -3.83961 | -55.98571 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6df54a94-8117-3ecb-b28e-f1356769c0c2 | -6.09456 | -55.72617 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b63ad8f-d43e-3881-b295-0febcf6532ce | -3.48629 | -54.61823 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 372c66f8-94a4-3a11-9c3d-4d72a7ed2922 | -4.11428 | -54.01829 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afae4a8d-7e07-312f-aea3-2754ec0634ad | -5.75126 | -42.06411 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a5c4a50-fc7e-3e8f-8026-fed1276dae5f | -3.51242 | -59.32558 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efbdbf20-38b0-391d-9933-d29d64bdbc84 | -2.93051 | -54.08054 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3f0dd6-bd29-34d2-b21a-8d31e5e77d2d | -3.12988 | -53.70217 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26515822-b84c-360e-99a4-90df8dcaf727 | -6.23893 | -52.8532 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8a590c5c-e9bc-3a03-9b45-933d732f2162 | -2.7684 | -54.08305 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37885cf5-6f03-3a70-a8a5-2528d53cd06f | -8.08135 | -55.29461 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba1317c5-f721-392b-abcf-a1cf2feac800 | -4.11789 | -54.01892 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a74fef5e-155a-3aa3-8fe3-59dff6f3de00 | -5.50592 | -42.84248 | 2026-10-08 04:46:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a2d33b09-6bee-3025-acc4-f0a70132f792 | -3.28701 | -54.00752 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3f0cc0d-e09e-3352-8f7d-9bc40b5b882f | -3.84023 | -55.98203 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eb22cbe-f5e8-3c4d-9195-8e52e786ba0c | -7.8267 | -44.17974 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f92293d-a7c5-3874-9e2f-a2e5bb5553ed | -3.10796 | -53.78579 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2c6ecd5-6607-3238-b2c2-c557c226acea | -3.72822 | -55.98251 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa805fc-6cdc-3cd0-b562-88d311c57e99 | -3.04916 | -53.94632 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b9e8cf3-f1ee-38aa-83a0-d4a5fa2c6bad | -6.32181 | -43.34962 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4b3faeb3-41ee-3dc2-9ff4-5184141435da | -3.52406 | -54.65004 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45c9391a-4849-3dd5-807f-b21ddae0f5e3 | -3.11203 | -54.16402 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 82a83b46-3767-3627-9650-00bba0d7de7c | -3.53924 | -54.67616 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed9b4561-8e79-30ee-91bc-eb9515448816 | -3.54755 | -54.67284 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b47b0c18-67fb-3695-98f7-446107c78caa | -3.28802 | -54.0239 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b0fedca-9ad9-395a-8e1b-f1a3b88f2462 | -2.93694 | -54.15178 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 931a83d0-9591-3ced-8917-cafacdd2ab26 | -5.95697 | -46.3746 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README89.md)
