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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c330b58-ad30-389b-8420-0080d703066b | -6.96018 | -59.05822 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5c04895b-ec41-304b-ac51-d37c47beddc0 | -6.132 | -59.89921 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d81e55ba-2c19-33b4-833d-289eab18398b | -9.16644 | -59.45206 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 02d63df4-cc04-3d12-8895-74e6553b3f5b | -6.86436 | -59.03381 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a6af07b-75db-3b7f-b578-6a6b4f683e7a | -6.85233 | -59.40967 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b51f8c53-4082-335b-b6a5-f99abaa287de | -6.139 | -59.89502 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd9ab312-ee47-3995-96b7-94b7e57bffd7 | -6.80405 | -59.41965 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| e92ab029-d83d-3964-9340-ed15ef478e98 | -6.69886 | -58.94369 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a67d1259-872b-329d-8a20-91b7b19d9016 | -6.88232 | -59.42464 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5db4a97-a74a-3cf1-899b-48e43f87858e | -9.21528 | -59.77987 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d868d4e-8a44-3813-a728-fb0da4f2518f | -9.16058 | -59.46288 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3197180d-240d-3555-be8c-5e15ec3a4995 | -7.87839 | -63.74663 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd626b84-1eb9-3982-a3db-7978d46d58f3 | -6.97441 | -59.05405 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c1c77158-724d-3845-8091-d38466f4e813 | -6.78941 | -59.42912 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c1876491-c174-3af1-b348-c7e6eb268865 | -8.89924 | -60.55094 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eae7a0d3-f511-3f54-a191-6b28f1b2e56c | -6.12101 | -59.91276 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b4f1f4c-7ad3-31d8-9f79-c1036ab60ce4 | -9.21164 | -59.77245 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ad9406-0b25-3a74-89ed-5ddaeefff0d4 | -7.61142 | -60.97274 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0feb5f5c-9287-3599-bcb5-48dac95e3183 | -6.86692 | -59.43998 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3984f8c9-737a-3622-bf3e-e37e37e0d233 | -6.77411 | -58.68266 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| db24d7d7-95f0-343b-be0c-796ba0609be3 | -7.01757 | -59.55828 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73f7d0b3-01be-370e-afe1-96fb7dc0102e | -9.16131 | -59.4567 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b3041cf7-da99-3a61-b620-5ed769017935 | -7.86481 | -63.77158 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804869ad-a5e7-38bb-9793-d8a7593d40ea | -9.2103 | -60.76484 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b73626e6-f6ae-36d7-9a98-3c7c88ea10fd | -6.78097 | -58.68375 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 32b3a811-3772-30e3-b809-c145c85338dd | -6.81645 | -59.42723 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15e6fc27-00f9-3dab-a81b-f678068676c2 | -9.2174 | -60.77554 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7aa06f89-477c-3685-b5da-4492c56bb816 | -6.27425 | -62.53466 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2387e66-ba9a-31b1-a41e-e7e2b48c95b8 | -6.7967 | -59.42459 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 6e3c56ab-a191-3bba-91ac-9f5313439420 | -7.86016 | -63.76791 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2d10b8f-2e6b-3a44-ad98-f99979930c83 | -7.60654 | -60.96283 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05020381-794b-3295-8ead-8cb8fd126483 | -9.18831 | -59.46062 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de539836-2d29-3a33-9cbf-beb10856201d | -6.11537 | -59.92788 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3718e594-2166-3933-b0c0-f19185092f3b | -6.80856 | -59.38554 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f973e1b-3631-3f1a-8fa5-c24c479257ae | -6.69642 | -58.94463 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66c1067f-7443-3446-a028-4e2c37745173 | -7.60051 | -60.96188 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdbe1fae-00a7-30f9-a65e-814e216199b6 | -8.39945 | -62.68582 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b555617-8202-31a8-a954-46a345675ca9 | -6.75434 | -58.67323 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86b0fd5e-ee5c-3b77-b150-556d9acee3b5 | -8.897 | -60.54102 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e23c7155-5928-3cb8-ae64-9bbcce4de74a | -5.90056 | -61.29212 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64eb1e9c-fdb2-3448-b0cb-11f91da28150 | -7.67373 | -61.12445 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f0abafe-5565-3b2c-acf9-ad6771a42564 | -6.81077 | -59.66797 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43770a7e-48c2-3d2e-b3e5-c36c1b9d41a2 | -6.7733 | -59.4499 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9658f595-55ce-3705-9098-6a1fa4cbfba0 | -6.96691 | -59.05922 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6cfe4607-6bee-3057-a5df-51e380d88b23 | -6.81509 | -59.42634 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6f71413-0432-3acd-86e0-7f313383c9eb | -6.36269 | -62.89937 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8ecf3d1-8220-3af4-bd8c-40bb5f21b3d4 | -6.85836 | -59.02691 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a83e83f-1500-374d-97b7-e568837067e0 | -6.13699 | -59.91037 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66c7c7b4-66bc-30e3-adf9-b76610e6274a | -9.21756 | -59.77911 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e70b978-32a1-374a-b9ea-fe34761eb793 | -9.16415 | -59.47038 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4a953c1c-cd2d-3e9f-8762-6a752a6f016c | -8.38855 | -62.68409 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5d483070-de05-3063-9052-3b04ac4a2756 | -7.67487 | -61.1155 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7de8ede0-65d3-3ec3-992c-790afe82545f | -6.8187 | -59.41031 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f59532e-40a1-3823-8e53-8b403294d6d2 | -6.12367 | -59.91359 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a21bf55f-98b8-3434-86a1-239ea58ebba6 | -9.21664 | -59.76827 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db046213-f019-35c8-9698-1f310a805fbb | -6.08264 | -59.95807 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa5649dd-4a90-3e0c-9740-f6d7e631cdfc | -6.79364 | -59.59845 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 836f1d4c-ea81-3877-8c92-0f0dee1d77bb | -8.40396 | -62.69374 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eda3dde6-cda1-3ec3-b95b-fa49e1dbb8f7 | -7.60052 | -60.94749 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 595ae24b-8259-3e79-97ae-582cf4fbde78 | -6.94357 | -59.31703 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aef85f85-9ced-357e-b234-57a74bd526b0 | -6.11669 | -59.91769 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 049e0b4b-406a-3527-81d2-8733aaafca8d | -6.81062 | -59.42066 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04337811-3519-3775-84d3-eeb82dcf7816 | -9.08038 | -65.41074 | 2026-08-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1a261b8-8c74-33eb-9bae-f804c113cba2 | -8.39353 | -62.68856 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a0335829-ddee-336d-a74d-07d3cbfdd0bb | -6.82375 | -59.66965 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 25653e8d-ee4e-3312-9e97-43d84ee7f7d2 | -6.81351 | -59.38555 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e58389e4-a879-3368-8487-ecbf824c34a5 | -6.12943 | -59.89841 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0bd50efc-6ac4-3fba-bd34-68fd3edd0146 | -9.04042 | -60.45075 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf887875-3bdc-3fbb-b7e4-8a0980412deb | -6.90343 | -58.99633 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9d82635-38d2-3367-87c0-b769b88f2770 | -6.90943 | -59.00321 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dfbe923-b5aa-34bf-a000-8046b2577b98 | -8.38951 | -62.67689 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4584a6f8-aec5-314b-ba0d-64ffa212393b | -9.20933 | -59.77312 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac5b738-9555-3b4e-91cb-184a82da517f | -6.11736 | -59.91255 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd9ec4a9-71cc-3eab-8d68-4bd7cc550b3d | -6.81364 | -59.39792 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6972d2de-6c24-3632-8320-ef392c62b51d | -8.89574 | -60.551 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 163a8e80-50c5-3579-a904-4c843601b1ab | -6.78349 | -58.6644 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e89878bf-0a3a-33e7-bb48-f83487404295 | -9.12111 | -61.59658 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b5a3ab3-b06a-38af-a6e4-31bc9a7d4aac | -8.39448 | -62.68139 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bb307777-83be-3ee7-b108-5bbe533b0dcc | -9.04331 | -60.44643 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5ee2a02-fbb5-3cda-a0e2-d8c2af577444 | -7.87062 | -63.76647 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 429f8818-e274-3b81-aa61-6f59dc221d94 | -6.86107 | -59.43342 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 313943bc-70d9-3bea-835f-6e015315c931 | -6.26448 | -62.52637 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ff78ddd-de8a-3096-83ec-2266d3e5ba74 | -6.13436 | -59.90952 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f89e3d7-750e-350b-875e-d99a1fc26c1d | -6.36792 | -62.90013 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf127fe9-88b6-3f54-b855-9dffce751a64 | -6.82399 | -59.66939 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a8b15194-9074-33d1-9cc9-c98e3ded1a17 | -7.0213 | -71.77338 | 2026-08-22 06:08:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3645123-3e02-3de2-a111-100959b97b66 | -9.11864 | -61.58622 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04090872-841f-3c5e-8192-ea3dbfc898e2 | -7.5968 | -60.94268 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08c6bbd3-f0bd-3ad7-9abf-8d78ab945f7d | -6.12803 | -59.90862 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7194ff29-2ca9-3b4c-afa1-b8e4ee50e55c | -6.8501 | -59.41451 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f804d57c-b6f9-3158-89b0-1e738d7f8257 | -6.88814 | -59.4314 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57256ffa-5b1b-3f01-9660-a8691f395073 | -9.16806 | -59.45768 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fad93580-7efb-3319-b082-48001de8ac3a | -6.77165 | -58.70166 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c979590d-2741-361e-83cb-2975df98b1fb | -6.93104 | -59.30961 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a18f4d16-b3f7-376a-8a55-ccef31d3bab3 | -6.12733 | -59.9137 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9d0b19a-5f94-3241-9e02-7156177cbe5b | -9.12757 | -61.59314 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20ca12b7-9b61-3703-b225-e004069e28c6 | -9.54003 | -63.56572 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 714ac7e0-0c99-30fd-965d-fb8eb894996a | -8.90204 | -60.55189 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 401a6b9d-5124-3582-8bcd-ec8d73b1688c | -6.76202 | -58.66796 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 323ccb9d-36ea-3034-8e43-12c504006b88 | -6.80171 | -58.6355 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README78.md)
