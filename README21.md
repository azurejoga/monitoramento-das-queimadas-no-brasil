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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dffcffe-9fdc-3390-abb2-7fcbf5aaada5 | -4.55844 | -48.01676 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7d3046e9-96ae-33d5-9590-b084dbeaeb71 | -2.25912 | -53.72686 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27ce97ec-b1a3-3975-96ed-094448a4625e | -4.61334 | -49.57617 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b944f5d1-8f5a-32f9-8aa7-4edbfb2af408 | -3.23725 | -50.45224 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab7537d-f259-3730-a020-e3d7188ba4b0 | -1.37761 | -51.41326 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1481609-dbe3-3413-b785-52119b9f441b | -4.68194 | -46.44394 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f979aab3-af0f-3f2c-b12d-df6b5c9693f9 | -3.33539 | -50.08594 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 969e2d67-f2fa-3b92-8fa7-d789600e1303 | -2.82531 | -52.94693 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a6501ec-74c4-3ed1-a9eb-75b58a2a75ae | -3.15461 | -54.47838 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6f9bf67b-a6eb-394c-8e7c-4b2bf2b5c231 | 1.00997 | -60.5836 | 2024-11-08 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a0f62e-3378-3c00-97c8-79fc4a9277fc | -3.01873 | -54.05223 | 2024-11-08 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e15b62bc-fe14-3190-b3f1-0c4b650c4988 | -1.25443 | -53.35098 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 836016cc-da63-3d41-bd11-134dadc0dad2 | -10.73198 | -49.52064 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5363937-9eee-3dcf-afb3-776d2d66f212 | -2.40283 | -48.50056 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c755244-92c5-3837-9b0f-ff354ea358b5 | -3.96517 | -48.12924 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc227f32-4abc-34db-a23e-9b9274e7a8dd | -2.90704 | -51.46589 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ebb7b49-1f47-36a2-88ec-437fabf6ed83 | -3.19536 | -54.31162 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70f12dcf-4d7f-3075-9f03-24b5d420c4af | -1.65087 | -47.82038 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a07a7cb-3a1b-35a0-9674-c2d93ee4291f | -3.01037 | -53.4369 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c93b3876-9731-3240-8932-3cbb333d4bfa | -3.03296 | -54.0736 | 2024-11-08 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e0cd9ad-1cb1-3294-b6d9-8c7cd57ed303 | -2.86709 | -50.32247 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c611ab40-84ce-33c8-aea7-e8d60592c577 | -2.88426 | -48.28758 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7325fd0-3335-3281-87fb-8ec3e0bf3b48 | -4.99557 | -46.81623 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a115348-2d12-324a-b18a-d66166ba4d8e | -2.53135 | -48.20103 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 217d5353-0e26-3963-9c82-740814c0685c | -3.9737 | -46.41079 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e6162a-2150-3131-90bc-c031449f4564 | -1.50324 | -52.06891 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77a570e4-5166-31cf-8795-62d44e30ef8f | -2.8035 | -52.93644 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcf368bc-e566-3077-aa3a-b290bd84e60b | -1.30109 | -54.22324 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 877216c0-47bf-30b0-ab8b-8dc49a032080 | -2.15314 | -53.66145 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cd098bb-ca01-3258-939b-25f7e83208d0 | -1.27054 | -51.94785 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7575abf-c6a8-30d7-a985-93ba01a902fa | -5.20458 | -47.46374 | 2024-11-08 04:53:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a579c08-c2e1-36a0-87d8-27e86933ca5d | -9.16786 | -61.53376 | 2024-11-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3d9ecda-0bc8-3aef-95b1-fc3baf96b1ca | -3.49738 | -51.58632 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5ee3f09-12af-3c2a-9c63-f86d929239a2 | -3.72295 | -49.0037 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db9e04a2-645d-348c-baec-148350defcf9 | -3.01576 | -51.38013 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bcde3ef-8d03-30d6-a66d-26b7aff3f90f | -2.93128 | -51.04751 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e49f6a-b870-3028-b006-de386dd41145 | -2.8152 | -52.94895 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121a4896-139a-3ad0-a378-4edf21742c18 | -4.32623 | -44.83973 | 2024-11-08 04:53:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 13c86f18-0704-351b-9a10-38bf72074e09 | -2.80131 | -52.95043 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 79f349cc-0fa1-3156-9436-8065b711af4c | -1.53933 | -52.01107 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9efb1f88-f332-35dc-9681-4a5b872f16cd | -1.59361 | -53.73961 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e9d2864-cec6-3e04-85d4-e7e9909d434a | -3.30461 | -50.08125 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9907fd24-f37e-3335-b74f-25923241dbdd | -3.95409 | -48.15117 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 367ad1d2-0f1c-3eff-831d-bb6701f0c4c9 | -1.23624 | -51.77376 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 057d1978-733b-378e-9cf8-6a25d6124492 | -2.67271 | -51.81604 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c7faebd-0e4c-3505-9388-33e385ce14fb | -2.91798 | -51.04547 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e5947bd-8c8a-31ce-a875-44a6bdae454a | -4.181 | -48.8008 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13de6512-c2c8-3a77-8719-4d49f6821851 | -4.17028 | -47.46458 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e45898f-4c21-385a-87bd-d5a5ed538511 | -1.50378 | -52.06547 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7b3bdf3-eb0d-3c7d-9637-eca44d4237cc | -10.72231 | -49.83058 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb836128-64f8-3985-8b4c-fefc4cbf0634 | -4.77891 | -45.7314 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b849bb-9d5d-3438-a56b-0077426a6648 | -6.40011 | -47.14542 | 2024-11-08 04:53:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14cde7bf-fd5b-32ba-b046-613fe7484a1b | -3.88933 | -52.12645 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71b8e897-a302-399b-a123-89d69b17ab11 | -3.54843 | -51.54118 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b578adf-7af3-39dc-94af-4b0972abfbf1 | -1.41734 | -54.50029 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68088c43-756f-3314-bfab-678109ee78e5 | -3.19069 | -54.31869 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce87f46d-73bc-3755-bf69-646f34c4a110 | -2.81296 | -52.94145 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eeecc5d-e1b4-30a2-9138-ab5a8634c919 | -1.24288 | -54.18148 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec9e9bd3-acff-3a3f-8746-319e9ea9c6f0 | -2.28039 | -53.81368 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c68922b9-2686-3a6d-b4d4-aa19aa521450 | -2.1756 | -46.43883 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7aa7d904-5f1f-3ad2-9449-1fe26bdc6dd2 | -2.87776 | -51.82729 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e7273c-ef26-34d2-8cdd-5ac5dd3363ff | -3.22804 | -50.37684 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 625d244a-0723-3379-9000-99e99b164751 | -1.85323 | -46.28457 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd99df24-e42e-3a48-89a6-8a0630b5a349 | -2.81301 | -52.96302 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e363e788-f457-394d-af36-364107aa5821 | -2.07381 | -53.5666 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34a86264-ec9c-37b0-af98-b57e13022c6d | -6.93027 | -52.86969 | 2024-11-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a114354-4530-3dab-83b7-a81fd8ca525b | -1.62678 | -52.54153 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b42cbdfa-4fae-32e8-9a15-2a0f41f77a53 | -3.47924 | -51.59413 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b0ce0c-e5b3-35fe-ba93-ecd901833d87 | -3.01486 | -53.43025 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2ddea37-fab0-33f7-9be8-505455d1a804 | -1.38082 | -52.26475 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e77b4f-7404-3eb3-a24d-e9096bf0fb70 | -4.84707 | -48.75389 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d60641b-42c5-30cb-b4bd-09c7442ed55a | -1.81835 | -54.43926 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5e3c606-8206-3a01-807a-a523d9ee6a8a | -2.30145 | -46.48342 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6789d246-5b62-342d-8b17-65bef895bc28 | -1.12431 | -48.38131 | 2024-11-08 04:53:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee8a0e3e-8d60-3165-af23-b58ab943a227 | -1.19987 | -53.65214 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b87bed73-0f2d-3627-ad06-c634ce9713fa | -1.34979 | -54.61039 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91e4aeac-c4a2-376e-a7de-bad31fecac39 | -1.5469 | -51.85408 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04942f11-db77-3f59-9d64-88abaef2bdf9 | -2.15486 | -53.65041 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c51bc68d-5ec8-3271-a63f-73dbfee04762 | -2.1577 | -53.65459 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efeec90d-10ee-321c-9d4e-aa83c965d0ca | -2.7628 | -53.21915 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 630e6b92-4148-3dc8-b859-a57461da4f68 | -2.18703 | -50.82458 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b56dec-55b0-3ef2-8642-c042186a8f1c | -3.23415 | -53.39863 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03717dc2-596d-39d1-8021-df81549d350d | -2.16164 | -53.65547 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bdb35ce2-d10e-3b60-a995-5591af223ae4 | -7.2178 | -45.08287 | 2024-11-08 04:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ae8e6ba-ea01-3040-934b-f5cb32d872bd | -3.96026 | -48.16149 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 725d1685-82bb-3aed-b229-93c037d606aa | -3.24738 | -50.01997 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44708ebe-b5fc-329d-845a-9141af8f9b4f | -2.28784 | -53.81097 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4658df4e-85da-3459-a015-646028715f85 | -2.05568 | -53.27792 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43cc122d-5ec1-3fd3-aaf3-8c274b5298db | -4.18774 | -47.9374 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bba76df-37a9-38ce-9f2f-4acd02d1c650 | -4.51252 | -45.6846 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 291680a5-53d6-376b-a555-e3a1b6d146c8 | -2.55626 | -54.0008 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbfa8a98-f0bc-39d8-9bf8-0d124064243c | -2.62363 | -51.29791 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99c09faa-f1f4-354b-8385-6ef23081416f | -1.32575 | -54.18616 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac89c57f-2ac9-3ec8-bbcf-92bb6191b096 | -3.97018 | -48.17251 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 426f6ce8-2356-3ce9-ab95-7f4117b71528 | -2.25879 | -53.72706 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6305489-25e8-3633-a9e8-1ad5d065e982 | -2.75833 | -53.22578 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed214bf4-f513-3b1d-8771-5863d1b9fc29 | -3.03344 | -51.5276 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 69ecc03a-3856-3c91-b018-093473181f17 | -2.73035 | -49.38423 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d04adb92-b182-3876-a964-8807c722a545 | -2.62416 | -51.29446 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9578f3a-dd6e-3153-a82c-e2a4eb7a6edf | -2.81975 | -52.96048 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README22.md)
