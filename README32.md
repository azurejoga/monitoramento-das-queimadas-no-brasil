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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81f86f79-85aa-389f-a3d4-6f05dbc9f5e6 | -5.43299 | -60.18484 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 322d6f5d-29be-3073-bdcd-6587c6f31ff0 | -4.46717 | -55.09279 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ed17d92-b204-32d1-bf31-18caaf5098a4 | -6.87922 | -55.62075 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a23145c-5e4e-3ea1-b0f6-5f998a2f4d92 | -4.55628 | -55.03936 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd1e0d3c-2e0d-354a-98f7-b19a17f03d47 | -5.36829 | -56.03018 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| f730fa14-47b1-3979-9004-283d8ef61ea6 | -6.06282 | -57.79253 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 157cd621-f9d0-3cd0-ac6e-195325de041c | -4.66452 | -55.62752 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e545d6d-8eae-3446-86ec-c6011568dc8b | -4.3524 | -56.28878 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e0ec1bf-8d00-3eac-884a-d3a9f97848c2 | -5.34896 | -56.02753 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49ddf2dd-b499-3a06-a2e2-f7e87186e29e | -4.46673 | -55.09576 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82dd662-151d-3352-8e74-161467df2f6f | -3.78188 | -59.7169 | 2026-09-06 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbed7cb1-ef68-3bd3-83bb-2ab6b1880433 | -6.02493 | -60.16961 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4d66013-ded1-3186-ba74-c58aa4695086 | -4.2455 | -62.23284 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df9e2435-b8cb-3cc3-848e-366c4199f432 | -7.1052 | -56.52053 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd5c0bb9-6f12-3e75-aa93-68e5b020b39b | -6.13131 | -57.74781 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a90f45-7721-31ab-ba09-27e58b9a46a2 | -6.87585 | -55.60811 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ff837cb-7003-3620-81b6-2c65ef4610c0 | -4.67851 | -55.6347 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fbaa360-620b-3838-aa54-ae7b4ab52023 | -5.35456 | -56.02289 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1bea8ff-a15c-3997-bba3-1169f6593cc3 | -5.3074 | -56.01387 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 021f0e8c-147b-3790-bcef-37a1a08e8334 | -5.16967 | -56.05246 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30c03176-a977-34ee-8074-d6c5b92bba6a | -5.36906 | -56.02489 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 9682c900-5fa4-3909-a5e0-65670ffadc53 | -7.27905 | -55.14601 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4564477-576d-34e3-b425-af36ea562bdc | -3.76948 | -61.76035 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f5ed223-c606-3155-8069-33a9e6d74d4c | -7.55918 | -61.35752 | 2026-09-06 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846be781-422d-3ba1-8362-33b3fee2eba4 | -4.46761 | -55.08981 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39bce22c-f011-38f1-b06e-7277abc4930c | -6.51239 | -58.29355 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da9b7df0-124f-37c5-847b-a913eb8c753a | -5.35532 | -56.01757 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c7a8aa3-16a8-318f-a03c-bc90bf1deda7 | -4.24214 | -62.23231 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59b38fe3-96d0-36ff-8d1d-880df923f781 | -5.35304 | -56.03344 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 385a199c-4d42-395c-9c17-26094559c31c | -6.87455 | -55.61715 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ba0fa61-83c3-366d-ac83-c626c15d874f | -4.55583 | -55.04242 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d0191e8-c55a-35d2-b529-7424037bfbae | -4.13395 | -56.34185 | 2026-09-06 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 918f56a5-c62d-36d2-87e0-62a32e201116 | -5.30257 | -56.01319 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3aff0b6-1a11-3254-913e-6eecdc9adf8d | -6.02865 | -60.17013 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3848bea-a642-3d33-b9c3-5905d3fac36f | -5.13164 | -56.27757 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 31fe06ba-ac7e-38a1-94b7-311a027e071b | -3.8312 | -60.76493 | 2026-09-06 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ec380cb-1750-3b7a-a4a3-37da0140aa73 | -6.5082 | -58.29277 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16208dbe-3fbb-33c7-ba26-ed7b90a2028c | -5.13638 | -56.27821 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f093cac2-50b0-3412-a323-300506f60898 | -5.35228 | -56.03871 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f3363b2-72c0-3c48-bae4-4fdbc052de49 | -6.1138 | -55.82088 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 008e2450-3cf6-3ccc-96c0-9a5468f462a0 | -5.28416 | -60.12816 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7ea474-a95e-3970-892f-f5d844694d1d | -6.83967 | -59.42959 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bf37ed6-2849-33e2-a690-0e8e69748884 | -4.09691 | -60.66132 | 2026-09-06 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 559aa5e5-483c-3ff6-bde5-beccc02ed601 | -5.64939 | -60.23659 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df40dd30-b37b-373b-a915-058546f6ec20 | -5.2835 | -60.13251 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a58341-a9d6-3f29-957e-e13caabc603b | -6.06223 | -57.79662 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d4d92fc-5700-3bff-b7b5-26148710e028 | -4.66791 | -55.63859 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea05a31c-f8a5-3add-835c-95d8820f9502 | -5.35939 | -56.02356 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f543b931-1c73-30eb-95b7-7b1b7e070bb4 | -5.36423 | -56.02421 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 690bcdb2-5989-37e8-bf63-b07eff0e0916 | -7.64136 | -67.43621 | 2026-09-06 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 549db0c1-0f59-36a7-8e10-11571be194d3 | -7.27408 | -55.14838 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e17986d1-4ecd-34db-b6c8-31efe6acbaa5 | -5.28719 | -60.13307 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f6c130a-89b8-307c-9122-76834bded3dd | -5.33854 | -56.03143 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cde2c922-f0f3-3805-a246-f2af18cad36d | -7.5598 | -61.3535 | 2026-09-06 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2c035bf-4655-3975-a666-e86c0e937801 | -6.95872 | -59.73685 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fa10a1d-e0e8-3774-82ad-5d30ff9f262e | -6.87797 | -55.61911 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc92d33f-46d4-3981-aa51-ae82ae6e4bb0 | -5.28048 | -60.1276 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 337185a4-dfea-3e2b-94ed-e6fac34bf0a4 | -6.58837 | -58.60158 | 2026-09-06 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d660188-bf5f-3fe5-8e8a-e59cccd7eef0 | -7.10592 | -56.51538 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1f36177-4bcd-365f-9fcc-4f11592099ae | -3.76835 | -61.76757 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08241d56-d093-38b0-8e92-1174bc9da1a0 | -7.27984 | -55.14574 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72575462-a20a-33ba-9238-ac7c86818e7d | -4.34771 | -56.28825 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e19ec0c6-405c-3748-868e-0358f09a4e66 | -5.34337 | -56.03214 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccad0631-ed13-3058-ac17-8b06a10daf7d | -5.365 | -56.01891 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59e98ed0-4657-35ce-8185-38513e9b5f3a | -5.64571 | -60.23604 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eddf698-82e3-3760-a3b3-accd5a0ff78e | -5.14879 | -55.95941 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c6ffa57-abab-391c-a0c4-32932f29d177 | -5.28785 | -60.12872 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2374f2e5-14eb-3cb3-b0f4-11017aaf9bee | -3.61534 | -60.57209 | 2026-09-06 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76ad5136-fe68-3ab0-99ed-63a03a6799d7 | -8.5023 | -54.65634 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7491bba-60b5-3085-ac62-d54393ee549d | -3.71966 | -59.37092 | 2026-09-06 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aca75f8-5b97-3123-8f29-77f228b650ee | -5.33558 | -56.02332 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9edbdaf8-69b0-38f0-8a17-59937e7d58da | -5.33448 | -56.02542 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2a38616-f45a-3b96-a194-b1405fdeb8a6 | -4.41552 | -59.96598 | 2026-09-06 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3e7ce6d-d22f-392e-b48b-0538fee67121 | -5.20173 | -60.03258 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35e8d824-41f2-3bdb-9b26-4023cb6f79d0 | -4.67438 | -55.62866 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe3c3575-c779-395b-a7a3-89728afccf4f | -5.3482 | -56.03281 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35702541-b252-3f70-852a-14eb93644b14 | -6.05422 | -57.79102 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5b38054-e94d-38f0-94a2-30446a7b2e4b | -4.6687 | -55.63322 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1deb63f2-3e3f-3554-a5e9-02d6dd59f416 | -5.37236 | -56.03614 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b0713757-2b1d-33ce-8186-d8027f10ff73 | -6.11467 | -55.82227 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4e13b8a-8893-38f4-b1e3-0219442470d1 | -4.47694 | -55.09689 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034a2a94-f7a0-35f3-854b-86167c8b3e01 | -3.78399 | -58.85429 | 2026-09-06 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 711b9ae8-e5b4-303f-9917-4c8269d63f6d | -6.05912 | -57.78768 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84719f97-2a49-363a-853b-8b5bc94d44c7 | -5.37082 | -56.0467 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8cbc9d7-f388-3214-91c0-a4b794599686 | -4.66374 | -55.63286 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa195d08-b382-3a58-9290-79b09da758cd | -4.67362 | -55.63387 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d0c846a-b567-3d22-b9cf-098cf85d3b28 | -4.91738 | -55.81055 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0dd2e38-17ed-3b68-a692-df70a3867d41 | -6.10707 | -57.70183 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e0b470-d6b6-3023-b183-f8a9cb79d4b3 | -6.06342 | -57.78844 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a7a2847-1d9a-3527-aa61-3b78b6b7af08 | -7.09631 | -56.51417 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db5fe77b-06cf-3f3e-a38d-12e0a5490997 | -5.25498 | -59.98209 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9caf4f76-4ae8-3385-b01b-5720e223d714 | -5.43128 | -60.12226 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b757edd3-0019-3ea7-a497-ab1ccbe41cc7 | -5.36093 | -56.0129 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8e18addd-2c28-362f-8c7a-ca43b5ab9257 | -5.33478 | -56.02861 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 080c6bfb-7ab7-3185-93cd-a5074a742e9b | -4.29445 | -59.95506 | 2026-09-06 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af9132e1-8643-3a65-914e-aa76417c4661 | -5.34488 | -56.0216 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88c3cb2-a637-3a02-89cc-3c7ddf4dc1ad | -4.66948 | -55.62791 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f728bfb-a762-304c-80fc-1f92cce7935f | -6.06594 | -57.80142 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d67bdf7-18a3-3a51-9713-4a117b1b0e68 | -6.8792 | -55.61013 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cad8f371-2736-3740-b799-ae5a39f45ceb | -5.33399 | -56.03389 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README33.md)
