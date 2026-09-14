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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d5b687e-711d-3176-af94-cb11a539788c | -6.32146 | -59.99508 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 597c9553-fe0e-3a74-8d04-b0ba75cf53e5 | -6.29621 | -59.95885 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e57dc67-5a70-3e8a-af5c-806adc2c144c | -2.89301 | -50.39804 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 872d0bf1-2af6-3972-8bb6-13e7db7c4dd5 | -6.32213 | -59.9906 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c7e1b90-157c-31a1-b433-63962acd0f2a | -6.79423 | -58.78897 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b32c9212-2ee9-3186-bc8b-3788935e5516 | -6.69193 | -59.12651 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93eeb9d6-662a-35be-9501-19ecef355101 | -6.27329 | -59.93208 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c40e51b-5ec4-3738-99e0-0ed972366407 | -6.27773 | -59.92807 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d791cdd-cf0b-3c17-a6a5-3099d117e1ef | -6.31989 | -59.98769 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4fe24fa-77b9-37f4-9a6d-ca65358da4b4 | -3.15079 | -60.26999 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f01d0eb-ca3a-321d-9fa3-5528d9e0ec1b | -3.60585 | -59.07128 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83fe6439-05bd-3c12-acc3-2232589d9fec | -2.89792 | -50.43414 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 905a53c4-4af5-398a-b73d-d78f19fd3a6a | -2.66428 | -57.50777 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7be22b5d-97bb-36a3-aab6-e9038dd376e2 | -4.38382 | -55.20327 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| df0f8b8e-8b25-3215-993c-463679af73b9 | -6.30179 | -55.27789 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3464df63-34d5-3c91-b746-cfced56fedc3 | -3.21738 | -56.83752 | 2026-09-14 05:36:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21a59ccf-ac90-3b35-8231-c5e23d5c5b7e | -2.91175 | -50.36463 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8be0eefb-f13d-3aaa-b1c8-00bf856ccea3 | -3.35615 | -59.82558 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faa83614-b87b-398a-99c2-a0a578ffb531 | -3.33365 | -54.18987 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57995a7a-8301-3707-b2d7-da9207190b64 | -4.21085 | -59.99099 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b4fa3f3-ac90-3103-a163-1a5c075fe8e6 | -3.54274 | -53.98129 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6cac1674-42a7-3186-be53-fbc352087191 | -3.38698 | -50.77209 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 943b6aa2-90ae-3ed5-9036-3f8083504535 | -6.7464 | -50.92694 | 2026-09-14 05:36:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53730678-e70a-3dd2-be35-1178173b3f95 | -3.38338 | -50.38997 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0828ab6b-52b3-398f-98d1-507db896ec36 | -6.11032 | -57.67089 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b1c0e165-0a87-317d-a53c-c118a3e7d64a | -3.59821 | -59.07012 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba1e8ef1-6468-3065-aa5d-496d2e5095b9 | -2.89801 | -50.38579 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 44abc6da-b7ca-361c-a27b-e2688d9ee859 | -2.90462 | -50.41192 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2011bacc-14ca-3d00-969a-a04201c440a0 | -2.48346 | -58.00591 | 2026-09-14 05:36:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a070b966-7104-3321-84ab-9408c5a35e29 | -4.13267 | -54.00967 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93ecb085-4001-36c7-8519-e653dcb49750 | -6.27841 | -59.9235 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 466c7aee-c79d-3ec5-8d95-0e194cbc6328 | -2.9114 | -50.388 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 04e802ee-dbb9-394f-a06d-5be8449a32eb | -3.86598 | -51.98127 | 2026-09-14 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a08ef90-ce09-3e15-9fc4-269b4230293a | -6.02078 | -59.94005 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0aa7851-3088-314d-864f-96d48bd47a0c | -4.3671 | -55.03254 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e5c0a97-1e9d-30fb-abce-6f973d4ae9ac | -3.08399 | -60.71115 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf0b634e-58ca-3b14-98c9-0180a7cc034c | -2.99967 | -60.80826 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b6c7924-0790-399a-ab2c-c12aa3bd7deb | -3.21706 | -56.83963 | 2026-09-14 05:36:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1972c111-3068-33ba-a9e0-9249d77dd444 | -6.684 | -59.12521 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 199d6f2c-83c1-3c99-9668-f22f6e7efcec | -6.11159 | -57.63198 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83e23319-0d24-30b8-b8d8-9286f859a559 | -3.60513 | -59.07598 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9176cc1b-e52b-3a7d-b542-a56747a4455d | -6.30651 | -55.28165 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9f1856c-0eac-353b-99ce-f9873f7dc88e | -3.85983 | -51.98023 | 2026-09-14 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c504651b-6f7a-399d-a3ef-a90fb1cafb52 | -5.08775 | -56.25607 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b8b2984-74ee-3105-84d9-481661280521 | -3.73094 | -61.7541 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3ad7696-b13b-37fe-b0e2-7a2010cb59e5 | -2.9713 | -57.8967 | 2026-09-14 05:36:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46b3fc38-7f4a-39eb-a30a-49ca58963e72 | -2.90642 | -50.37493 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f232935a-225a-39b5-959a-f88dbe8f0d4f | -2.89657 | -50.37431 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2512d530-47ee-34f9-8a64-0271186ea5f8 | -2.89046 | -50.39071 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b277d99-b345-305d-a06f-49051fb244e4 | -2.9289 | -50.40897 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d71a6e08-f66a-3572-a75a-a71529650c2b | -6.30817 | -59.95596 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4955be5a-fb1c-3cfc-a22c-ca071e38acd6 | -6.32169 | -57.73291 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82f62273-0e34-3018-9fbf-7bf28b1c9d9d | -6.31037 | -55.2915 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70d0a7f1-e9ef-38db-afdd-381888997b49 | -6.11638 | -57.66967 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 734db7b4-a1bd-3425-affe-1960a1ff7dfa | -6.79718 | -58.62504 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7c1a58-184c-3a55-b429-f6f919c8785e | -3.38246 | -50.39627 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3bea2040-a7c4-30ae-af38-729ebc7c4f27 | -3.1762 | -61.11989 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76dc4d6b-0e25-382a-88d6-eab1de1f9182 | -7.58163 | -57.69944 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 770e3e71-5967-3aa8-92ec-fc874cb536f5 | -6.37708 | -58.30369 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c07df45-c12e-38d2-ab6a-20d7eef3becc | -2.93474 | -50.41589 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e922d2b-5c3d-3eba-9fa1-6f42d401e8e6 | -2.9113 | -50.4361 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 54e0d99d-0138-3a8e-ac13-e0dd96064413 | -3.74838 | -61.75308 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf5e524f-eb61-34a0-8c0a-f57b4ac6545f | -3.7332 | -61.76184 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7294cfad-8212-3b6e-bf33-c32dee727922 | -2.89746 | -50.36836 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee7922a8-35f0-3f30-bba5-480fcdc37174 | -6.13721 | -59.88553 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3610870-6af3-35f0-a5be-35cf3da1f65d | -3.44976 | -61.09515 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c53f5ce-cd6a-30ea-8ef5-7c848debf769 | -4.12381 | -60.68269 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f0e17325-c960-32f8-9bac-0a62c04f5a5a | -3.60887 | -53.84953 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc596c6-d13e-3996-a734-cbb1a3ce507d | -3.01733 | -60.90038 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 915dc1c7-24dd-3cdf-b7a0-3e413c62594f | -6.02012 | -59.94458 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4e8a4969-b828-34ec-8c10-1f6bfd98973f | -7.10594 | -55.63369 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a38d5358-a93a-378e-8878-9f469dcbc081 | -6.28081 | -59.93327 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60b6f44d-2d95-37ea-b790-bf0735fada1f | -2.88683 | -50.43927 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 546c56a6-c2f2-3bdd-9560-bd70c0b99350 | -3.17555 | -61.21487 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c03a413-f648-3563-b33c-d4a08dde3a64 | -6.02144 | -59.93552 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cea6d9f6-97b2-3cbf-9c91-fffeb20adf62 | -6.69914 | -59.13284 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ebf074-e370-3772-b8e1-6d78df7cd4ff | -2.90997 | -50.37643 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 185ab9cb-b0b1-30b2-b181-e15f7ab4c7eb | -2.92805 | -50.41484 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab7cae48-867d-39c1-b0ec-6456e65a19cd | -6.28638 | -55.27572 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b35e76a9-d762-3666-b802-edc009e7500b | -3.16155 | -58.64145 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 03749cd2-b5da-381c-93d4-140f601a01b9 | -6.1153 | -57.66719 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0cf4787d-c611-3f2b-8da8-c20775ae0b18 | -2.68557 | -57.5758 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13407de7-55ac-3324-9e39-03a177f02543 | -6.10526 | -59.88797 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f99af2ec-aea1-3407-a607-381f4fe06599 | -2.89886 | -50.37991 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c8b39c8-8cf3-33cd-a43a-78e6cd25d504 | -4.13755 | -54.01416 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 787f099c-edcc-38a0-8cd1-9914bcebf773 | -6.58139 | -58.84908 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54b09751-f107-31a3-9c4c-281fc6ab1e18 | -2.87876 | -50.40179 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af642d0a-7d73-302a-93d0-90ec29a99e8b | -3.3568 | -59.82133 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9f6919-15ef-3259-b67d-644f03e4dd46 | -3.04067 | -61.24778 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38d78f1e-8e57-3860-af63-73e828d613e7 | -2.70308 | -57.54372 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fa8d421-ce5d-33ca-b03a-4fa191439a2d | -5.80433 | -52.1186 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 644af453-d051-3e14-b9c5-bd4ea8c3d97c | -6.32054 | -59.98319 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5c9c909-2d27-3613-ad3b-e7d4a7baa281 | -3.13949 | -60.6285 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9256df03-58ef-3e75-83e6-ade837b0f3ab | -3.16434 | -58.64511 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3c73ffb0-24e8-3db8-b911-dab8ea371a9a | -2.91213 | -50.43036 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| d74ab5b7-1c8c-319d-b621-d96931daaef2 | -3.22251 | -61.2063 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42190601-601d-3d6c-98d8-221055297683 | -8.11969 | -54.79902 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41f2cec7-38fd-3686-83a9-fa4899160285 | -6.67712 | -58.87731 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c05700a-1794-3d39-a789-00b2835bd68a | -2.91894 | -50.38318 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a014e05-abca-3d39-b8c7-3854e9288947 | -2.66738 | -57.54309 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README55.md)
