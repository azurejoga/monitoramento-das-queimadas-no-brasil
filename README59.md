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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d395d7-849f-336e-8c59-b0022efe09d1 | -3.67661 | -54.27433 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb18a8e-8b0d-3d1b-8a6f-74d1ad81b856 | -5.20528 | -56.07897 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d40d217-d454-3320-b8d2-898fba2ed6dc | -3.41857 | -61.29933 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29b98594-95f0-35d1-bef4-98ec2f2db150 | -3.65085 | -58.90124 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a9f1047-c170-3981-9ec6-0eedc4483aa4 | -5.98227 | -57.77209 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27f965ea-7660-3013-9ec8-72f8922d7766 | -6.40563 | -55.25249 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb9685fa-d82d-3761-8d99-64dfbdaa5bac | -5.7522 | -51.93243 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b67a0f-ee15-3be7-a2a6-b6f3fa00a7e6 | -3.91936 | -55.73157 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 790bbc26-35f6-3782-af6e-63fe326f3628 | -3.54179 | -58.69197 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65634747-c739-3346-b92c-766fac47ecf1 | -5.38355 | -55.89863 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24d2e93e-5159-36d5-ba3c-05a0008df99b | -5.83684 | -53.47741 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f903e331-bb04-375f-a92b-91d2089b15f8 | -3.49087 | -54.68463 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 871f2992-313e-3349-9bd1-6fadfd55562e | -6.8494 | -55.28559 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2a624b0-11b9-36ec-a2af-dfdcc7253539 | -4.35377 | -55.65183 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1672f165-5dc6-325e-a0e4-9b89ebf03a92 | -6.28374 | -59.92018 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89bc8cb4-2061-3d41-a9ec-53fd050f65c0 | -6.36783 | -58.28366 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 414e6a66-3bfc-3f7f-8895-7f86b4bc4537 | -5.42477 | -60.21521 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da97205c-849c-3ef3-9d9a-8fd465748662 | -6.7326 | -55.09539 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e43e264f-a615-3f24-85db-345720534fe9 | -6.77837 | -55.63419 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a427959-ee68-32d7-b900-6a4e4ac1d5c5 | -6.15062 | -57.84041 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9340061-8598-333b-8d98-d916aeee456f | -6.09032 | -55.55465 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad5bfc63-8c0c-37ad-869a-bc20c43a3118 | -6.93012 | -55.64416 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a14e5b57-7964-3277-816f-573081ab2372 | -6.15888 | -57.6977 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2631de47-163f-35d7-968e-4070cb3dc353 | -5.76275 | -57.5866 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4b6982a-37d2-31bf-bb71-2b129a1f0446 | -8.31184 | -46.00463 | 2026-09-21 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4fe79eb-82cb-3182-8818-392e9d5ed7b4 | -5.84255 | -53.5485 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96a15000-d4f5-3582-9335-5e6dd078bb5d | -3.60972 | -54.04716 | 2026-09-21 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6c6a3b1-339c-3a95-924c-32625f81ad31 | -3.39538 | -50.43663 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d918fb49-af7d-3b04-93af-1f0bb5a4a97e | -5.37971 | -55.90157 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cab4bff-3049-3691-9fa4-210ff6221774 | -3.39138 | -50.43612 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2109a16c-122a-3afa-ba7f-bcde89afb261 | -5.83728 | -53.48883 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fbd66f7-8678-3e73-b682-f9ad60b5f10f | -5.21196 | -56.10123 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74afcec5-e8c6-3628-9bef-e3a10cdbb3cd | -6.15483 | -57.72339 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a96f847-0e9a-3701-a0e0-1aab65767235 | -3.69091 | -60.58743 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3fc4c6e-cde1-3330-8126-78a8f4dcf6da | -6.44902 | -48.44955 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 171ed070-9382-3236-aabc-ebadcbc22e21 | -3.34319 | -42.76576 | 2026-09-21 05:04:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fb617e8-4f15-3cea-9428-958d543408a4 | -2.90476 | -59.22417 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| c2a9d6fc-a962-32f5-bac5-9da7aa0099b0 | -6.42016 | -56.10176 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2821a067-8332-3740-b826-7a8300f96116 | -3.0993 | -53.16672 | 2026-09-21 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2838f455-cf27-3cb4-b692-450134548faa | -3.40099 | -54.91103 | 2026-09-21 05:04:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b33f28a2-df79-3bac-bf34-8c0d3270f26b | -6.33245 | -55.72363 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 964315bf-2099-3b54-8b5f-2d4bfb190b07 | -6.11835 | -57.75537 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1780e01-3c31-30e8-8c9e-b56debe50f90 | -5.20534 | -56.10022 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ce51f2b-89f8-3a20-894a-f504fb1cf138 | -6.12267 | -59.95408 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78d08bf-9829-31d1-a432-7481af7ba084 | -5.97351 | -55.36297 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 681076a6-8d78-30c4-a37d-6a6e73d5707d | -8.13434 | -46.8181 | 2026-09-21 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a92be276-a91b-3b93-849d-386a7e66db14 | -5.81506 | -47.79266 | 2026-09-21 05:04:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45e40f17-bede-398f-a9f3-c94636b31486 | -7.41845 | -44.76567 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f4336e66-7b09-3708-a627-d8c461f4a79f | -7.24929 | -46.91466 | 2026-09-21 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a71df4e0-379f-3086-9603-8ebb6f6eadfe | -6.93057 | -55.61937 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e125199-7ddf-30ac-9e6b-c05683b4c652 | -6.12853 | -59.94331 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d3b45d4-747e-3c67-a37a-191c7eb6bcdc | -5.93241 | -59.95389 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7b3a6bf-e7c1-325a-9ccf-38837fe14e3e | -5.08557 | -56.25871 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6853d9b2-b802-366a-a504-39f812766445 | -4.59341 | -56.05654 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caec8a64-d9cb-3055-8ebe-ce10c41c9797 | -6.08632 | -57.69369 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b949e71-4e0d-3303-9ead-b231820bab93 | -6.65915 | -50.89019 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3901f71c-6775-341b-b212-17bdd1e52a83 | -3.60637 | -54.04663 | 2026-09-21 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5de3b462-519d-3344-94cb-12607ab72aa7 | -5.8564 | -53.52711 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4ae17f8-4457-3de0-a70d-3a5d5fdde199 | -7.44119 | -44.78461 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e8f0bf5-a1fb-37fd-8a9c-2320dc5681cb | -3.68915 | -60.59831 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96df8305-52cb-3dbd-a894-2309e243e221 | -3.75485 | -59.41893 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd073037-541b-3ce6-afa7-cbf04fe89012 | -5.76217 | -57.59026 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef0c373a-4611-395f-a0a1-c86e7ff15d81 | -5.85913 | -57.54937 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a76ce172-e2c6-363f-8edb-097e18789b57 | -7.40299 | -46.14845 | 2026-09-21 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c922f8ef-5afe-3f9d-8b16-79ad278eb9db | -6.09255 | -55.56206 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a1d3bcb-3e92-33d5-a460-5b69bed5e7f9 | -2.97733 | -54.77042 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5930bc01-44f0-317e-87ba-735672028d3d | -6.19883 | -57.77982 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9932663c-49c3-3c5d-802e-d869be809b33 | -6.1496 | -57.75654 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d907fcd8-db0f-300a-ba43-851fcc572715 | -3.29979 | -57.86555 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e539ccb-015c-3b6d-852d-2d7850046926 | -5.9811 | -57.77943 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db487574-a4e0-3ad4-91ee-1fc8caf55b5e | -3.78673 | -51.92297 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81e2ddce-f0ab-3519-a35b-ffe7c1ceddb3 | -2.82941 | -50.46737 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d14a219-c8bf-3948-8e1d-28144b6f5885 | -5.86851 | -52.03597 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5f37bff-866b-3cf1-9de9-1d380edbe4bb | -4.09458 | -52.1167 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea8884e5-5337-32b9-bdb8-c6f9456e881f | -3.01047 | -54.16446 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b98a89d-5305-3666-b51c-7fe2530d373e | -6.83359 | -55.54326 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db57b4c2-5153-3088-bb91-79c2bc33f098 | -3.33745 | -42.77167 | 2026-09-21 05:04:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 055ccf48-0f5b-3d7e-afb8-ad1c7bf91937 | -4.06154 | -56.23533 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2e82527-1387-346b-9cad-8ca99e0f03c7 | -4.22141 | -48.61692 | 2026-09-21 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a8ddb0-e7e3-3b61-a9e3-3b27e135c7dc | -6.30344 | -60.0131 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3386eade-5e10-3b62-8d37-6fac1c0d1ba5 | -6.30713 | -59.94272 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fe70417-5eec-3382-b242-31c56ab994e7 | -2.19877 | -58.15354 | 2026-09-21 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bffadd1-947b-32ef-8be1-df02c05769c7 | -4.34994 | -55.65475 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a9d34d5-d936-3336-839f-073179899036 | -6.10761 | -57.62588 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0141ad3d-7258-3946-b4c7-1ba4dd67297c | -3.33478 | -59.80319 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 548b49f4-d57a-3e83-bf00-14fdc5508874 | -6.67913 | -50.92865 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c0b022f-934d-3e2c-b21d-d59d31da29f2 | -7.70889 | -49.37061 | 2026-09-21 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4268187e-c3ea-3f08-9aaf-2179fac3c1b0 | -5.83674 | -53.51626 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5af26cb4-7245-3dd9-9181-2359cb843965 | -3.07578 | -51.20216 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22e66bf1-3d21-3921-b42d-a1ed825ec138 | -7.31796 | -46.77295 | 2026-09-21 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f38541c7-2c53-3cf6-a341-c104982d7d84 | -5.81243 | -53.52078 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6224c67-62c7-3e9f-98ba-a8f90093b899 | -3.17495 | -58.59177 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb69150d-2df9-34bd-bf82-f229744480ea | -5.88232 | -53.63652 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59b17c93-6dbb-3c72-9b37-44de43702abd | -5.85856 | -57.553 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26dbd750-4d1c-3687-9ee9-3fb1d7182f5d | -3.10273 | -53.16725 | 2026-09-21 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 314b5865-511f-3af3-86ff-e8de24ce0fdb | -6.44502 | -55.63493 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab1308a3-8b9d-3169-b9fb-8dba73d49e05 | -3.3942 | -59.58426 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4c9be98e-2653-352f-b933-2e34494fe956 | -5.97945 | -57.76787 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d4bccc-7a74-3548-8ef0-42923a1ba8da | -6.19879 | -55.44804 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f9be4d-96f3-3a1b-bf08-0c2113d14fe1 | -5.86543 | -52.03098 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README60.md)
