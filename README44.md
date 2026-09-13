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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce20c5f5-dae2-3581-9cab-1bce45c1152f | -2.94809 | -50.39757 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 231fcb9b-c46a-3da9-b2e4-c4a1039fc45c | -2.67496 | -57.54439 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 32eaac46-9c1c-374e-978d-9ca39199a972 | -4.10678 | -54.90372 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b45ece8-2fd0-3c7f-9c63-e168c0335b30 | -6.09993 | -59.9001 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2307857-45b3-368b-a419-a5e6c9c0e931 | -6.09614 | -49.66378 | 2026-09-13 05:10:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f488a947-2a59-35bf-925e-d8e7f5e1eb09 | -3.38947 | -50.75819 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc2a2ea9-0bfd-389f-a194-d903d0df162a | -2.86594 | -49.62724 | 2026-09-13 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d91a729-3d4c-396c-8181-133ac552ea9b | -3.44834 | -59.51777 | 2026-09-13 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d1bb815f-060f-3a68-b443-4cf96b63194b | -7.18676 | -50.83753 | 2026-09-13 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf37d4d-e081-32a4-a765-f584f9ed2772 | -7.87066 | -54.71045 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee2bb0ac-470d-3786-bbb5-1303d3523cdb | -2.67515 | -57.52077 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de931908-3515-3879-9855-33c60630fb54 | -3.045 | -51.26277 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bfaf468-6dc6-3ceb-b0d2-e9ddd2008fa1 | -5.96551 | -57.77282 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39def2de-eab9-354d-bdc1-e65d08d5b78d | -8.02251 | -54.85686 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9776d768-4727-3e83-98e0-08a52560e7ba | -8.11904 | -54.80021 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21537005-a3cd-3fdc-8de9-dd85471cbee2 | -4.80219 | -42.89534 | 2026-09-13 05:10:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 61f40ead-c8ed-374e-b4ee-69cd90e9e8ed | -6.30381 | -59.95751 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 055d5a98-ccc8-376e-9bc7-09ed51b948a3 | -8.01969 | -54.85272 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 503934d5-20fe-3e29-9207-37d6fe78e424 | -3.87743 | -51.18472 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d619ef7d-0c44-3aae-bf5b-d967ac75fdde | -5.96491 | -57.7765 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb97a42d-8fd5-331e-ad28-224a84efa853 | -2.84784 | -49.54239 | 2026-09-13 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74686f72-ab1c-33b7-9441-9a03fb137dc5 | -6.17217 | -57.71056 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36e86b75-756a-3d07-9a49-ba7fa99c0660 | -3.44758 | -59.5225 | 2026-09-13 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9de56522-6e5a-32ad-864e-45239eb7d89d | -6.15019 | -57.69205 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47746711-a5ce-3770-bd7e-b2a22a82245d | -3.73141 | -61.7519 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7418b3f8-f1ba-38e2-bcc8-eca16352b42f | -4.53538 | -54.92133 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f8a4f14-eb7c-30db-9ad5-62d50db3a8ba | -3.70698 | -45.38914 | 2026-09-13 05:10:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 246af654-35e4-39fd-a45a-946dbcd9b960 | -6.77234 | -59.43224 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 378783ad-c4cf-3bca-b9df-0ed6a82eb54c | -4.51206 | -55.4557 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f45fac4-a89d-3e74-82b3-710f31ffb54a | -6.59096 | -58.8455 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fa4e31a7-bfdc-313c-97f7-f7248785dcf9 | -4.87407 | -56.00061 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f22d836-a5ef-30fc-87e6-0ec24ffb79e9 | -6.84867 | -47.44085 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64917b96-af6c-3056-a1e0-30d295b1371a | -3.19615 | -51.01688 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34478cce-6add-3689-bac0-bdda2b19d560 | -2.53896 | -54.65771 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7c99784-1ce1-347a-8224-0cfa12918249 | -3.44375 | -59.52187 | 2026-09-13 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 34f00c8b-b91b-3a8f-b39f-0b2072932fb4 | -1.22997 | -54.12629 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80616b7b-91f3-32c4-ad94-2f099fa46903 | -2.8255 | -49.23205 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5442980d-1558-3d61-8bf9-f4a94b4a5a06 | -2.21482 | -60.08616 | 2026-09-13 05:10:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be72b3d-cd37-3c35-9b66-ffb4c5685511 | -2.67783 | -57.5488 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09217d7d-f1e1-3b18-a3bf-c063a6952214 | -5.90418 | -49.9616 | 2026-09-13 05:10:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 692292a0-3f0c-31ed-87ae-8b663bf2d8c5 | -7.52825 | -47.3345 | 2026-09-13 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3fba6090-61e9-33d7-9a02-6dd5e848fc05 | -3.76621 | -58.84521 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8751ec01-938d-30e4-b6fa-30c76d2eee45 | -7.86786 | -54.72868 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 629ce108-5a96-34ec-9be0-b0a6b6744d42 | -2.67967 | -57.53725 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e24c84f3-eeec-332c-aeba-38f3d3052cd7 | -6.06915 | -57.86855 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4608fe1-ea75-3329-b6f0-ba812313d6a2 | -6.95578 | -59.7488 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 512a33d3-edac-3df5-b826-91f58cc2d8c1 | -6.66111 | -58.88111 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15251585-987a-37bf-90e9-1d879c290faa | -7.86557 | -54.69839 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2051812e-66db-3adf-9759-61180317968b | -5.61488 | -44.8505 | 2026-09-13 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18073253-22ba-3279-9159-c84cb2a74fff | -3.4067 | -59.24705 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 73949848-e268-39a3-b75f-7cf15f79c9bc | -5.76654 | -45.09608 | 2026-09-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb02a21b-048f-3739-b4c8-a3afbf27d9f0 | -6.50934 | -58.28607 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78d80ec4-85b9-3270-b632-f45cd61e7a06 | -8.02645 | -54.85376 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5d91272-e5d8-3d19-908f-de2032532650 | -4.87462 | -55.99716 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922fbca2-44f5-3965-becb-1ede511962ed | -8.01913 | -54.85634 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c027a49-b4d9-37ed-8058-6d73fc5c3563 | -4.66639 | -56.00342 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 242f4844-82f8-3016-8142-5e55e721a23d | -2.94331 | -50.40206 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cd55e77-94e0-3e28-938b-f791bc011eb1 | -6.2782 | -59.92495 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f1ba086-7e75-33ad-ba53-d62e81dac30e | -5.85358 | -51.94909 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c2651d7-9566-34d1-bd7e-3ac14fcfd1bf | -6.30986 | -59.96795 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d59f188-0951-379c-96c0-0540734e093b | -6.30457 | -59.9529 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 727fe3c2-d759-38c6-aa81-7b05532eaf20 | -2.96547 | -50.3906 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76074561-b228-33ff-9bca-081f08ee7ffd | -6.38367 | -58.29097 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8a13791-a180-3f59-94ac-f9cddfa77006 | -3.04805 | -51.2679 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2924978d-7ac0-3847-b5ef-a51b748318e6 | -8.53702 | -54.70262 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46fcebb1-b08a-3bed-b572-2c53d2de70ad | -6.18381 | -57.74641 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78f85013-6b42-34db-9f1b-155eea9b1d38 | -6.33785 | -57.87743 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aac83bb-fda8-3e0e-8e71-d63678ce36a2 | -4.41207 | -54.86254 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1b6e2e54-7183-33c3-b1c2-fa09342fd594 | -2.95287 | -50.39303 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63cc0492-7504-3853-bcc8-73ab8ea176a7 | -7.13316 | -43.75831 | 2026-09-13 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1616e90-b87a-3816-85b4-214edf775339 | -6.56487 | -58.98281 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba7a6972-271d-3643-863b-4cb9e9b8bba8 | -6.37673 | -58.28981 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dd02db2-d214-39e1-9bdb-a357f953a403 | -3.82557 | -51.88943 | 2026-09-13 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 883dd93b-35bc-3925-922f-aedf05f238e8 | -8.04184 | -54.85149 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc83cbfd-5338-3b2f-a558-39e946886018 | -3.22346 | -50.58643 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9263227e-aa46-30e7-b9fe-e53c5edccd14 | -6.64427 | -58.82882 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f4d5129-5fe8-34c5-a4ba-acaa2755d9c4 | -6.23203 | -51.69049 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c79896db-5de8-37c8-8c61-ae5621f22227 | -5.98773 | -57.70066 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cb15cc2-04f2-3acf-9511-82160ea381a6 | -9.36917 | -50.10052 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| da40b5ef-81b8-34cc-a7bd-80ca9cc19093 | -8.12524 | -54.80489 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 173f3dd1-b2b4-3bb9-8687-f0c71fe6e999 | -6.79213 | -59.96192 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3f00e0e-2406-3b51-ac84-28538ceec444 | -2.95685 | -50.39364 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d08e45e-285b-31ff-88a6-8bd9c387fa7c | -2.94649 | -50.40776 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3e56c43-8dcc-3c18-a7ea-6aef599e6c3e | -6.85805 | -47.42469 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da7f4190-e560-3bf8-aea1-b8f179a409d1 | -7.64032 | -47.18682 | 2026-09-13 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8407b21-d9ea-389c-bfad-f152c5ef95d7 | -3.59759 | -59.07575 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 168b3860-a89b-34e5-a98a-2c38269263b9 | -2.96133 | -50.40715 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f6c8b18-1941-34c1-9fb5-ab243ac61d61 | -6.30911 | -59.99617 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b47dbc06-8857-3994-85d2-a585dcd09172 | -6.76506 | -59.43103 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7987309-7be0-3ec1-948d-17d98620d44d | -3.76254 | -58.84463 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cdc70ea-19be-3f51-b5df-0a40954d5454 | -7.18732 | -50.83368 | 2026-09-13 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ae98f34-eb22-3df9-a8e0-75b9791accf3 | -7.07928 | -49.94706 | 2026-09-13 05:10:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea18ebf4-4aad-3957-b480-a45401e83056 | -2.9441 | -50.39699 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c12b40a4-f37b-3f97-b1a4-9d3025cd8bbe | -2.82919 | -49.23672 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cccbb0ea-20c8-35b4-8136-6a6fcdb4e7a6 | -6.95947 | -59.74944 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7afdbed-7ebc-318f-8996-d44d9dfd904e | -4.39357 | -55.04432 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7acae927-f883-301b-ab65-f0d8cf6974a8 | -6.65689 | -58.88459 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11268fe1-710d-3ab7-b660-cf050b623c64 | -4.53489 | -54.96745 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4418a744-6b03-3474-92e0-d876c22560c1 | -1.72743 | -57.15362 | 2026-09-13 05:10:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f90d229-a8d2-3f5c-a039-cbba7b61e9c4 | -6.79615 | -58.78699 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README45.md)
