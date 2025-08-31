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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eeccaf7-76dd-3f75-b19c-56250d60c578 | -13.03237 | -56.90671 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171e8f00-69f4-3d30-a53e-46b83adc7f4f | -11.2843 | -63.24495 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e69ccc-783f-37aa-a899-9457c2d5aa74 | -7.94424 | -63.50101 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 302151ea-5ecf-35b5-a491-d637d42b17a9 | -15.21919 | -56.06567 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f4bd204-b037-3a05-81b1-9c179900b139 | -11.41249 | -63.23613 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 092fadf2-9394-3a59-a651-9dfb078e3142 | -11.41487 | -63.24529 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1256ccf3-e096-3503-995b-f953061b4b25 | -8.53038 | -64.00938 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8101197-2b36-382c-a3bc-00a213d44a87 | -8.74456 | -62.38586 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaa72d97-e62d-3dc0-b68f-045b8c09410d | -7.9048 | -63.01016 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6127e421-cae4-31c9-b23c-800cc5e1373b | -13.02476 | -56.89215 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3499bc7-8c3c-378e-a198-32986b1d891f | -8.7439 | -62.39026 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ed0d655-2cf1-3665-b90e-877dc7c2994f | -8.85536 | -70.62459 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1078b96-c9c2-335b-855e-f25503855fa2 | -9.07131 | -65.4324 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9808ff55-deac-334b-8355-13f06934ae23 | -9.45771 | -62.33694 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4492338-1ca6-392d-b71f-9d492b803fe3 | -9.27394 | -67.6413 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9611b6ba-57f7-370f-a578-5c262265d7d8 | -8.56286 | -63.01182 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eba39fb1-d97d-3d41-bf25-80ad336edfaf | -9.1043 | -61.20097 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64da9117-2fa8-35ca-b8bb-827983deae74 | -9.43467 | -62.33806 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f99055e-4cb5-3c1d-8284-e5f74c485d18 | -9.28069 | -67.64238 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f80cf33c-44d9-391f-8de5-98313e407b08 | -9.56866 | -66.68991 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa32a2d0-5fb1-3968-84e2-0a0858126f37 | -12.91727 | -56.98331 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba207c4a-8564-3875-bfcd-86223795679e | -11.4155 | -63.24099 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73d2119c-7d1a-3b06-a2e9-7d242a742c06 | -8.88903 | -62.39036 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ff1f9c6a-86a2-38c0-b83a-91a93f15c39a | -9.06406 | -65.41332 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b139250-3295-34bf-bd11-de17701780e8 | -9.75181 | -65.09364 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e02612a0-89f1-3ab4-be75-a92413195fd8 | -8.74462 | -62.37902 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbb96139-f832-34cd-83f1-0912844684c1 | -7.56932 | -63.41146 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ee476d0-7076-3dcd-abd8-993ca229e583 | -7.56874 | -63.41531 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23717797-fe94-3867-b8b9-d61661d17303 | -7.50129 | -63.28373 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fad27c10-ab10-30f7-a4e4-03f86d5886e8 | -8.86817 | -71.27725 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f13a144b-14e4-3a92-9389-c82360c8ca34 | -8.82229 | -72.31373 | 2025-08-31 05:44:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5cbb16c1-48c4-3a9b-99e4-cda9f191ab2e | -10.61395 | -54.91809 | 2025-08-31 05:44:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb5facdf-0d45-3c97-90c5-41c26a878a69 | -8.74522 | -62.38144 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8c545d0-a97d-3fc3-8d7e-35ccb3f51bdd | -8.53722 | -64.01044 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b84ef0b4-48e9-3a7a-af38-2facb2d3d27e | -9.06522 | -65.42785 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 902b596a-dc9b-3575-b903-349958ac6658 | -9.10828 | -61.20158 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23018acb-4617-3eec-bae0-37834a20dfdb | -8.64108 | -62.82959 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ca16514-b55b-33d8-afa4-4d2537710d03 | -11.31874 | -63.26322 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29a4a9cf-a246-3283-b831-fdf2eb6991cf | -8.38774 | -70.83594 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77f1ce05-51a3-3c15-81de-c97eeed1b750 | -8.39291 | -70.8297 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97f25093-4577-3119-b734-b984ad33dbd5 | -8.96768 | -65.96916 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2bd82aa-8f97-31a4-bd21-f3c58d83e2f1 | -8.34734 | -62.92713 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 647f216b-1394-3196-8833-34158c4b26da | -9.45474 | -60.57316 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3034586d-c5d5-32d0-ad7c-fbeb7d43172a | -8.96384 | -65.97211 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee15ec72-0d41-3858-889e-e9ade95c2c76 | -9.44344 | -62.33013 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad5ba735-1440-3bba-91eb-5c29fda8821e | -8.55334 | -63.02706 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b269b9c-0833-31f7-86f7-d13acfc09927 | -11.39233 | -63.27254 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54744c8a-ffeb-33fb-8789-ccfab4db84c7 | -8.74222 | -71.10684 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 742a0e53-ba4c-3f60-bb1c-c0605967068e | -9.43775 | -62.34309 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd4e205f-fee4-3e59-8bf1-38e2257c1d96 | -13.01548 | -56.90483 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d09e66-a9aa-3dd4-b671-05b356173ad7 | -9.44691 | -60.5682 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ddcf0f2-47df-3c8f-a2e7-223ff16e1960 | -9.89463 | -67.01659 | 2025-08-31 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edd3e187-0cb8-33fc-a508-8f47aa50e00a | -9.45579 | -60.56551 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14bb01a0-bd52-3203-8374-958dfb974bbb | -13.02381 | -56.89996 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e9b93d4-0d68-37f8-aaf2-fa89639f8d95 | -9.4413 | -62.37127 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c09c3c63-78db-399d-a809-eb3a9ba263c5 | -7.95156 | -63.33182 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac67a90-7e2a-3ba0-b5da-9b8315278cd2 | -8.56046 | -63.02815 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59de28c7-6bba-38e3-a2fb-82521892038b | -8.65987 | -70.0425 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1443bc1b-315e-3ecf-9058-02266936821b | -11.323 | -63.25949 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a695820-4604-3148-9978-a0bbf4cdc768 | -6.92728 | -71.78181 | 2025-08-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3acd46d7-b278-36c6-9801-2963354d8192 | -8.74514 | -62.4017 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 887af800-7072-3826-ae6a-9fe1b5e8532f | -8.22874 | -70.4683 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aacad01c-1116-3ed8-ba2b-edd78b9977d7 | -9.45837 | -62.3324 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccbb8b84-9c51-3d8b-92c4-39e55aabe641 | -9.06468 | -65.43135 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7184e331-eac2-3586-a61a-ddb7bf37f794 | -13.02853 | -56.89038 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e5f067d-0caf-3e3f-97e4-3aee292f47af | -9.07138 | -65.45393 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72eb6c10-14a3-3e43-a84b-c281612f60ac | -7.46253 | -70.13604 | 2025-08-31 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76e0babd-21e8-3fad-813e-a66ff5d6708a | -9.44326 | -60.56381 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 306ecea1-3b70-3c6d-a5d8-1e70d228da9d | -10.70474 | -69.06147 | 2025-08-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e96306f-1dfe-3eee-a31a-bda9757f7f60 | -9.43953 | -62.35719 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8544f75-c1b2-3d47-9aae-bc640db13829 | -8.65908 | -62.83232 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 903988ae-d602-3826-9369-781172679ad1 | -7.97763 | -71.39286 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30ebf475-9a48-39ad-b9c3-d82d88c0ccab | -11.32333 | -63.26205 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad918e17-08e6-3c89-8da7-d87fdbd1f4b1 | -8.6561 | -62.82761 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c2c4333-e868-354a-90b2-3718b5a12df1 | -9.43888 | -62.36171 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0e9e010-7dea-35d8-8fad-cf9195cde150 | -7.83079 | -71.99706 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 080b6653-dcd7-3467-8c02-8d6c560fbbd0 | -10.00801 | -68.83617 | 2025-08-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ba70ea8-fbfd-3aad-8fe3-da17e5c62765 | -13.0177 | -56.90328 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b894131-3de3-341f-ae87-261673f3cd0d | -9.44568 | -62.36733 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9ebc7ff-fdaa-32df-9fb5-ae5937644fff | -7.46334 | -70.13121 | 2025-08-31 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f5ce745-e559-3b6e-aadb-745ee8d9fe7e | -8.57082 | -70.06331 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d81821e5-135a-3356-8647-fba48171693c | -12.6344 | -57.00794 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8cd3bf6-0975-38f4-985b-1ed7578537cb | -9.44651 | -62.33527 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 762cc90f-945b-3f84-9bd8-4da8f3b1b974 | -13.02007 | -56.88366 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5df447bf-7e31-3155-8c8c-ffc9fab8e751 | -12.2222 | -64.22371 | 2025-08-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d7f13fa-1212-3df9-ab81-2a8eef5cf8b2 | -9.44119 | -60.54776 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dcb1cda-f330-3ffe-ae7e-3f49b816eadc | -13.02428 | -56.89605 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7446486a-026f-357f-9ab8-23f9cffe6e72 | -9.45575 | -62.35046 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cbd1e622-0e76-3ea1-959d-42395d7893a8 | -13.02809 | -56.89426 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd46d2f6-f262-3dd8-8e05-c8f849409dd3 | -9.2801 | -67.64602 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27c24b27-562d-3ade-b53e-8f961ab589a2 | -15.21961 | -56.06908 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f796b78b-edcc-3ebd-9234-600a83010508 | -9.95455 | -66.87486 | 2025-08-31 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2811948-85c2-38fe-91b3-3be6ac2071e0 | -7.90834 | -63.01072 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25b4e9a4-6929-34be-b1c4-1d27de3c3b7c | -8.69303 | -71.6002 | 2025-08-31 05:44:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71884451-c381-368f-97b9-07f11f422240 | -9.44521 | -62.34425 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59273006-78c8-3e6b-b1c6-0ec5da38800d | -9.45004 | -60.57638 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8b4c590f-f200-3c03-82e6-8970803c87ee | -10.64138 | -69.04758 | 2025-08-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d92e731-adf2-38f9-8223-09b5b8b55736 | -8.43186 | -62.293 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9453989-e646-3919-b671-0cdfba1619d9 | -8.86461 | -63.02422 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05a711a9-eace-3542-af2e-02c9b440b4b9 | -8.74335 | -62.38786 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README75.md)
