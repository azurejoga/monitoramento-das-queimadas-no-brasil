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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6042649-9992-391d-86f1-7586e8dc583f | -20.37791 | -45.60261 | 2025-06-08 04:06:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c2f8fe9-33d6-3e56-bb68-e8dc12e5300e | -18.72102 | -54.19099 | 2025-06-08 04:06:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9f6dc44-827b-366e-a473-d9ece36ef280 | -17.67848 | -42.74207 | 2025-06-08 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03645cb5-ae79-3680-b105-7596ca07debd | -13.88039 | -56.21073 | 2025-06-08 04:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4551a807-dd7e-31ea-a819-b7cfaf861695 | -14.04021 | -55.13673 | 2025-06-08 04:06:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a722dc2-1a0f-3efe-a104-b8a86d11deb5 | -20.31138 | -45.58691 | 2025-06-08 04:06:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 490a0292-9473-3bc5-b195-1d029ebf3451 | -18.72326 | -54.19509 | 2025-06-08 04:06:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30385182-25d1-3a37-b0b9-e3dc8f59da95 | -18.02178 | -47.38517 | 2025-06-08 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05235eeb-eb2a-3a0a-8eb1-eb0ab72791b5 | -19.17085 | -40.14038 | 2025-06-08 04:06:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba10528f-1629-353a-9038-3468b2295dfe | -19.21014 | -40.0948 | 2025-06-08 04:06:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4ee21cb5-4d91-36d6-be82-3a59bee29d4c | -19.84783 | -48.3587 | 2025-06-08 04:06:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4363b640-e517-3bc0-9f8b-aff3d14fdcea | -17.50264 | -42.28861 | 2025-06-08 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8793ec7d-8fb5-30fd-a9f1-7cffd20cba98 | -18.39086 | -44.33793 | 2025-06-08 04:06:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b41efde6-c62b-333c-b490-c454f3c5e505 | -20.31261 | -45.58605 | 2025-06-08 04:06:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c45cc2fd-1d38-34c1-be5a-82602d6dfc6a | -17.75205 | -42.89665 | 2025-06-08 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8da98d1b-d763-3848-b831-285d55dbbcd5 | -14.03483 | -55.12894 | 2025-06-08 04:06:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 833f6f49-341a-35b4-bb97-b220a33a97d7 | -13.87868 | -56.21097 | 2025-06-08 04:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94eada47-0c24-3d17-b586-32cd1cc1a515 | -18.7268 | -54.19277 | 2025-06-08 04:06:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7996bdcf-4098-38c1-8bdc-eefafaecbc62 | -21.3883 | -48.63802 | 2025-06-08 04:06:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bd5637f-f8ed-352d-8257-93089cda17da | -14.03351 | -55.13497 | 2025-06-08 04:06:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd27dbb3-469e-35d4-af3d-870cf0e0a0e9 | -16.68235 | -43.8849 | 2025-06-08 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c0494b0-80b2-3c7a-aa13-2240f21c00c7 | -16.26524 | -48.80737 | 2025-06-08 04:06:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba95a04f-5c2e-3387-b525-4607123d74ea | -14.02676 | -55.13344 | 2025-06-08 04:06:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 858a347e-8b40-3142-9d05-7b9279f528f5 | -17.75262 | -42.89302 | 2025-06-08 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40eb736c-88ee-3d26-a673-75798d74716c | -17.09398 | -43.80568 | 2025-06-08 04:06:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a0dbb68-8e46-306d-b47f-27ebfb34452a | -13.88208 | -56.20323 | 2025-06-08 04:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0ab3b89-8300-3982-9930-97e1783d9a76 | -16.06664 | -43.65524 | 2025-06-08 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d8b6926-d387-33f5-9898-ed667756a0e1 | -16.06942 | -43.65956 | 2025-06-08 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acc0e8f8-1827-31c8-93d4-5aa5c429e857 | -18.23434 | -47.93876 | 2025-06-08 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed2cd0c1-27ae-3bb7-b213-88b25ee64ded | -18.72424 | -54.19058 | 2025-06-08 04:06:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ce6377f-bdd5-38e9-8e72-291753af13bb | -17.59531 | -43.19806 | 2025-06-08 04:06:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 176b3542-cdd2-3713-828b-8f6fe45cb716 | -22.78824 | -42.94667 | 2025-06-08 04:08:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e21a5a95-6128-392b-bae9-b6e43548314a | -22.90191 | -43.75315 | 2025-06-08 04:08:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 746141f3-7dda-3156-8be6-71d796f88df3 | -21.23293 | -50.83685 | 2025-06-08 04:08:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 87cee181-1808-33e6-9c8a-5e92a85c24c7 | -20.99508 | -51.79483 | 2025-06-08 04:08:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 79ae5d39-76a0-3f0d-8f30-943f53ce2bc0 | -6.21163 | -43.33837 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e14b057-6f9e-3149-a9ce-23f623756ef9 | -7.01128 | -44.5961 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d0fc965f-e932-3b0b-94d3-14b83eef72fc | -3.72223 | -49.0752 | 2025-06-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ca5742-bf60-3e8c-abe5-a139d7d36d68 | -5.64327 | -43.72347 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9fe13ad-7d14-3ed2-9c3b-b3a427f64670 | -7.11076 | -43.70395 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24edc611-b913-3f5c-8b0c-7b98528f4a33 | -4.4865 | -43.77778 | 2025-06-08 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6a8a6a6b-606b-3baa-92e4-776fe293a5da | -7.10757 | -43.7001 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8bb0af7-071a-37d3-9561-af4b695ff643 | -3.04766 | -49.43819 | 2025-06-08 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90131e3f-59a0-3ab8-9f13-5f02e20c7e92 | -4.46796 | -41.60707 | 2025-06-08 04:23:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15dad1e8-d16f-3369-a815-25afc97c5d19 | -4.81731 | -47.31917 | 2025-06-08 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06ace82c-7223-3bdb-86de-3d406d9ae969 | -6.87155 | -47.24828 | 2025-06-08 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78820452-8c27-36a3-9797-2b4c505ecd97 | -7.10818 | -43.69614 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3bb7cac-9f17-3b36-a61f-b061b88c5741 | -2.9219 | -48.23776 | 2025-06-08 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dae82954-45df-34cc-8d64-5e17cc6cc0dc | -5.64038 | -43.7191 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05858ecf-53dc-3bae-93d4-c59ed4ee3672 | -6.6354 | -47.34468 | 2025-06-08 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c09b6e65-1f59-3dd3-a4c2-f0599d9122c6 | -3.04773 | -49.4366 | 2025-06-08 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 78489623-80f5-329f-b232-28877834a62f | -5.63979 | -43.72294 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cfb9c37-bda8-3c28-8510-48825c66f4f2 | -5.57364 | -45.20372 | 2025-06-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7a3cc32-9f3e-3b88-979d-4e456751cda5 | -7.02092 | -44.57874 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90ef7138-b61b-3c8a-a62b-65a6a86e6c68 | -7.02206 | -44.59401 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96cde2fb-60d5-36c3-b293-8876f758d50a | -2.91901 | -48.23322 | 2025-06-08 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea2d2ea5-37a7-34cb-bf67-326c3f1326e6 | -7.02035 | -44.58243 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e09a1026-a266-3ca1-b70a-b39d208935d6 | -2.9185 | -48.23791 | 2025-06-08 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03f1bdad-ea1d-3cdc-8730-b471b49b9757 | -3.98465 | -48.40971 | 2025-06-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4bed63-2a55-3536-af26-18bbc9b28a50 | -2.91836 | -48.2372 | 2025-06-08 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceb26846-1601-3957-b658-96b3cbb7f937 | -3.25646 | -47.5364 | 2025-06-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac378832-ddc9-37fc-b87a-025359cab2c1 | -7.01752 | -44.60086 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a6a25b11-7b01-3a99-beb5-fa60297016e1 | -7.02489 | -44.57556 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a880bd87-7e81-377a-8784-7cc9d74859eb | -5.63342 | -43.71802 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c030ed75-090d-32a1-aed0-2299cea0d796 | -4.6658 | -41.95988 | 2025-06-08 04:23:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b4da7e03-eef3-3f72-8999-dea5a110770e | -5.6369 | -43.71857 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a3f0e98-ad65-3adb-ae70-4be7b29a7fe6 | -7.18712 | -42.81158 | 2025-06-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a23a6a6-f7e5-3ae2-b8af-e2fa3b064996 | -3.04841 | -49.43363 | 2025-06-08 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d6ba050-5fec-3642-a726-adb19fb4b72e | -7.01865 | -44.59349 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 14b49979-521d-3c00-ac0e-31f984215f64 | -6.87988 | -47.23882 | 2025-06-08 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 20cddd22-ea21-3c39-92e4-702ffecd2991 | -7.1105 | -43.70459 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6fcdd37-7b3c-380a-bd3d-1ec9f44846eb | -6.44603 | -45.72589 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b082a491-6b02-33d9-ab52-217bd033cee2 | -6.44989 | -45.72294 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6dc2fe2-2ede-3981-8c1b-4747fc8f0ffd | -6.876 | -47.24179 | 2025-06-08 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c622bdf1-7b58-32f6-8b80-094937b1e8a2 | -4.60849 | -38.53275 | 2025-06-08 04:23:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3e4e2eaa-0983-3feb-a721-3b8ad9b273cb | -5.63284 | -43.72186 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16a3eb0d-8f95-3ec9-91cd-5dc4f7750bb9 | -3.25243 | -47.53957 | 2025-06-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab27126a-917f-317a-8394-ebcd23c95891 | -7.10782 | -43.69945 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c63b7b8-0520-31f6-bca9-6760a4a53af5 | -6.44657 | -45.72242 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a80819a9-9841-3538-a9b2-0f9f429f176e | -7.29581 | -44.03568 | 2025-06-08 04:23:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5a79cef-f3bf-311c-aa67-cb3655caa783 | -6.44494 | -45.73284 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 181d20a5-5435-3bf8-bd20-583c436e59c5 | -4.33356 | -40.18908 | 2025-06-08 04:23:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5d8f2bd-62dc-3c27-897a-18bd37de361c | -7.18342 | -42.811 | 2025-06-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23f232ec-4601-35c9-9d92-56064db8e6bb | -7.10841 | -43.69548 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e95b70df-8c34-3cd4-a317-b2d297c2739d | -7.01525 | -44.59295 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f0db58b8-0cdd-328c-9906-bed88926ff0f | -5.78457 | -43.62561 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01e15ff1-39a1-3cea-86d2-bf283ac814d7 | -5.47185 | -44.69945 | 2025-06-08 04:23:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 666ac63b-561d-3ff8-bde4-7bcb783c1796 | -4.91523 | -41.99733 | 2025-06-08 04:23:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4b8e2be-34cb-31eb-b78e-3ef9bc5783b5 | -3.40359 | -47.58142 | 2025-06-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44e400ef-c827-31ef-b61a-4dae5c4a03ac | -4.06436 | -48.11771 | 2025-06-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42d01fce-77d1-3251-b55b-fd37a365e18c | -3.72086 | -49.08376 | 2025-06-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 996d8072-f319-3f11-99e4-e44db95f5205 | -7.01468 | -44.59665 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 97d4a279-95f3-3a8f-9fe1-6f342eabebb3 | -6.21519 | -43.33893 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e1ca03d-c2f5-336b-9e2a-fc17871f7f6c | -6.54196 | -45.69823 | 2025-06-08 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fa8c912-a2d8-34b4-a01b-8e4f6401ee59 | -6.87544 | -47.24531 | 2025-06-08 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 235e9152-402a-327b-bb19-e504b0afbcec | -3.11524 | -48.96174 | 2025-06-08 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8704ea0-78e5-3fd4-af20-b9a9b67060f9 | -6.19922 | -43.32403 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a425e5e7-9302-3c19-b356-32f986f4c2c9 | -7.01696 | -44.60454 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a7fc3e49-bc71-3eed-83cc-84bcb8d98c4d | -6.21103 | -43.3424 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47537595-d154-3e00-b46a-6381dcd27e58 | -7.01809 | -44.59718 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README8.md)
