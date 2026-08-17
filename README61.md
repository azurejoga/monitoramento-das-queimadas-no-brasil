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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31a9589d-6e5a-38ee-9185-742b609ea4f8 | -6.77362 | -59.4776 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed4ad075-e6fa-3b0b-b89b-17c64fc7b8c8 | -8.42458 | -62.67796 | 2026-08-17 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 429f02b1-8bb4-3451-8fd3-ebda43bec669 | -8.9693 | -60.52187 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa446fc7-af09-36de-a8ab-f6ebd357f067 | -8.95171 | -60.56754 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7439a572-5ac2-3fb5-ba3e-bc1705506d0a | -6.7136 | -58.92934 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e3b67dc-a53c-3990-91fa-ecb8b658151a | -9.17403 | -59.67273 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60b91fd9-e095-34a2-a45f-c0d98ee8c3ee | -8.97321 | -60.50716 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3399452d-3183-336b-a714-71e9e787641d | -6.71183 | -58.94205 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79b6c69e-4d6a-3c07-88a7-038d611e919e | -10.07436 | -68.29244 | 2026-08-17 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a1ef73-2705-3171-92b6-1990e4dea76c | -9.17344 | -59.67729 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62f41044-9ef6-319a-a623-4aa6575b098b | -10.05713 | -62.45832 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6635208e-f14a-35f8-b73b-10937ff5e799 | -6.7191 | -58.93493 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bf24389-c1e2-3be7-8dc9-96942c6079d0 | -9.35027 | -63.56735 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0556524a-da9a-3385-b1ab-1576d33fa0d8 | -8.89251 | -71.26517 | 2026-08-17 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c23f583-491a-3928-8b9d-b7af4a468bb8 | -8.98485 | -60.53621 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c73816f9-39ee-37f1-bb88-bfc8c1fe6332 | -6.86392 | -70.0608 | 2026-08-17 06:01:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9fe9a80-9395-3c38-ae00-7bcb5f2a1885 | -9.08286 | -61.4026 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a276dc-4f8d-3682-b14c-c66822a25391 | -8.97398 | -60.53051 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcf8962e-c58a-3ac8-b482-cfb4d404adcf | -8.74035 | -62.90888 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf9f65e7-53ac-3cff-939f-e6be4a9bfa41 | -6.7866 | -59.47078 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7265ca9-a1a2-318a-91aa-734fcb801d40 | -6.62119 | -59.06255 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 435b33f9-a1bc-3e57-9613-996c5ffe1362 | -6.60089 | -58.97976 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| efd3e25e-0f9f-3663-96ee-867e65a56840 | -7.55434 | -61.18173 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 22bda675-d009-3de4-a87f-abb0d897c394 | -6.62708 | -58.96984 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0c2d7f32-cf91-3a49-849f-34a4974226db | -7.43029 | -60.02105 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f77e7a35-df6c-3d9d-92b3-93632144e6e4 | -6.98714 | -59.03492 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f899ad7-6718-303b-88b6-270b3855a3e3 | -6.63213 | -59.07355 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e3999a4-6eb2-3478-90db-f8bb336a1165 | -8.95918 | -60.57347 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d26a79bf-8cb9-3092-9840-57fffeeb64aa | -6.62769 | -58.96515 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7ce1d4ca-d8fe-3973-b437-07ecf6109956 | -6.9743 | -59.03774 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b369d48-1d22-3d6e-8705-9008d81f6d65 | -8.91248 | -67.48658 | 2026-08-17 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10958212-2b17-3d41-92ce-471075581bf7 | -6.77134 | -59.76686 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17c678aa-ddcb-33d0-a49c-04b26b6c5bcc | -6.63152 | -59.07814 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91868615-4fed-372d-87b2-5fd180678a58 | -7.59576 | -61.22406 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f82becf7-218c-3e03-916f-be025749bf99 | -8.95639 | -60.57601 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bd2fed0-bc2d-3818-b351-1c264cdb0f01 | -7.59402 | -61.23748 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae26c756-8da9-3e69-92c5-7fd52d63756b | -6.60149 | -58.9706 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 62781a05-10cd-3a96-8b24-a685d3617b95 | -6.64729 | -58.9583 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| afd63da8-8bbe-3bda-8393-6183b242ba06 | -9.32823 | -62.33655 | 2026-08-17 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94b00f21-bb09-3346-9b2a-4ab90127c80c | -8.96153 | -60.53681 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a0471ea-d7dc-3ca0-9b3b-279a6440bd2c | -9.20214 | -60.79417 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d28bba6f-dbcc-37a5-9f1e-ea4a373034be | -8.74594 | -62.9042 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd013dc2-9a41-3eb9-b6d4-8f1ad41808ad | -6.62845 | -59.05444 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34d85b3f-8254-3736-b520-dce651a78e8c | -6.68931 | -59.06289 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7daf283c-8371-3000-a521-5b80aa2b9518 | -6.64118 | -58.9573 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e85e2c1a-4ff4-340f-a9c9-80ba4cef40d2 | -6.72038 | -58.92412 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d98c578b-44d3-3b43-8983-2742ad851211 | -8.72581 | -62.90679 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0a418a1-9f5b-3015-a329-f09937e19ba8 | -7.34448 | -59.59746 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfa29dfd-d895-3bc5-a106-26bbb3eb16ae | -7.87963 | -63.74778 | 2026-08-17 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b7f2251-27e1-3eaa-bfaf-54d2036151dc | -8.94699 | -60.51459 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be7505b1-4a91-325f-b14d-a4166b8a13ad | -8.95116 | -60.52726 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5bf1e54-17f0-32a6-8537-d39784190db8 | -8.54339 | -69.99355 | 2026-08-17 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38f93657-b9de-3580-b068-32070d423e65 | -8.9522 | -60.56375 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0736f5a9-354d-3be9-8d0c-34a4c84ca943 | -9.94929 | -68.62394 | 2026-08-17 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e17c96-24e4-35be-af9d-feb7b31ac4cf | -6.71243 | -58.93731 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 755673de-1996-378c-a8a5-6979ae4f8900 | -6.84997 | -58.98623 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9631836a-dea9-392e-a762-7e1569b67f05 | -6.60758 | -58.97614 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ae8fe73-99a8-3192-a28e-114248298455 | -8.9037 | -60.58049 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee46f97a-27b6-3a84-a46e-ea66d0de450e | -6.61978 | -58.97812 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d566f77d-3730-3fff-8656-9aef946507a0 | -9.19403 | -59.67188 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31770b5c-fff7-357e-b4e5-8252190892af | -6.98836 | -59.02569 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad6b016d-6446-3454-bbc9-a11753d57e62 | -6.77698 | -59.46877 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54f8657d-8b55-3288-bb4f-bc4dc410fad2 | -7.87898 | -63.75235 | 2026-08-17 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4596ac12-8ea8-3077-900c-e8875f15a906 | -8.96454 | -60.53021 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87a1a419-335e-3482-85f0-ec9198fd04d8 | -6.62668 | -59.05877 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01b1f78b-b692-3010-8ad1-e1b74f5038b2 | -7.61259 | -60.95462 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59d65c85-b34a-396f-83b4-3e55ee3b9995 | -7.40829 | -60.00951 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a9fa09e-e302-3c5d-814f-7954a4a1db66 | -6.77643 | -59.45607 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 423a25c5-a272-31f0-84bc-1972bab608a0 | -8.39108 | -70.82114 | 2026-08-17 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a766125-5378-3951-9713-5a88e14d840a | -8.9587 | -60.57735 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a1db0b1-e8bd-3954-be8e-326cb1cd7614 | -8.9771 | -60.50682 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63b53cd6-c14c-3935-9c69-627754160012 | -6.77224 | -59.45929 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eddaf2f-98c1-3827-8263-307fd3216d80 | -6.59538 | -58.96972 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5eafe7fa-52a1-38e4-8002-3f63d3da966f | -8.95893 | -60.51226 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 459e9663-e71c-3b14-bc0e-202ea51ebe67 | -8.96976 | -60.53491 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741ec169-8ba5-3d53-845a-c51da66d5170 | -9.20263 | -60.79031 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc72fcaf-8c47-3622-bc40-410ea72be623 | -7.42451 | -60.02026 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1672727-29c1-3e8d-8c81-eceffccc7c48 | -6.77528 | -59.46484 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c4fd5f5-2b7a-3ff3-89c5-1fd1127d4b40 | -6.70486 | -58.94774 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a5cc00f2-92a1-3a2a-aa6c-bb38fc135855 | -6.63878 | -58.97128 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bcbfe8dd-1fb1-3d9f-905f-a5c3b8ebfa22 | -7.88373 | -61.79976 | 2026-08-17 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69d20487-6ff2-3956-b7e1-09275f5bd313 | -6.63394 | -58.96116 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66231dcb-ed23-36f1-94c7-18801a94bd53 | -6.77079 | -59.77098 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b10f9cf1-2a90-3e41-ace3-69228861fd9d | -7.42485 | -60.02169 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60c92ae-af81-3a7d-9143-8de1ca78a071 | -6.85179 | -58.9722 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed6377f7-b9de-34cc-a44d-79936219ef15 | -6.59475 | -58.97432 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4d544671-246a-3a12-a438-4268a4067fe6 | -9.20065 | -59.66802 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa9cc1f1-4322-3f21-a41d-849255ebfa37 | -8.97222 | -60.51513 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bb1f117-545d-3b29-9c22-cadcfe0761ec | -8.9608 | -60.51345 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de410e15-aa51-3800-b212-a04cf69f6ed4 | -7.40094 | -60.02042 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfa88071-1cb6-386a-aecc-b02228b691a1 | -8.95835 | -60.53329 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50d4f907-ae67-3c8f-973c-57787a13326f | -9.08137 | -65.4221 | 2026-08-17 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4a5aa48-f85d-3476-b51f-c9f540192150 | -8.95738 | -60.52416 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0996436e-2ad2-3106-8258-b8cb5b3c746e | -6.11899 | -57.73213 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38fc1a8f-5fdf-33f1-9aeb-9d8069899534 | -7.49994 | -60.07687 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30af89d0-fdc0-3d67-abc4-c86b4d9ce8cc | -8.68018 | -62.87832 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9e28bf4-ddd7-3b18-9119-b225f8b2215a | -7.88931 | -61.79741 | 2026-08-17 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 709cac11-2360-319c-8342-21767df4c932 | -7.59212 | -61.22501 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dec873fa-f19f-3c5b-8443-9808503c1f2f | -8.95981 | -60.52145 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb91890c-7999-3bdf-8efe-9948c991c92a | -8.89582 | -60.55136 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README62.md)
