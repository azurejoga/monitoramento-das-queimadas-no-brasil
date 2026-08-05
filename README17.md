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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 447a9a4c-f91f-3a6d-a2f5-af39c14bb37a | -11.21291 | -54.90583 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e177c85-ca26-3938-8a01-028b0228979f | -15.44714 | -41.37974 | 2026-08-05 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 449ebaf5-34d0-3abe-a7c0-130b04d5aa42 | -11.24998 | -54.83385 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 609ef59c-b904-3af3-a9b4-8d27969ae1c4 | -12.20753 | -52.86856 | 2026-08-05 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d28a83-dbdc-3cbb-97fb-196d2d1254d2 | -11.17968 | -54.88771 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7c2e7d9-df7a-339a-9810-bd49e97b19a1 | -11.20454 | -54.9127 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49d4c9dd-9959-389e-9195-d4fb37eb2cc2 | -12.44923 | -50.37993 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7628ea0a-9b5e-36d5-8e36-d366f617e767 | -12.59403 | -46.94845 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4f03fce-dd0e-3f0d-9706-f7edc993332b | -12.00322 | -49.27138 | 2026-08-05 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8eadf6e7-6ac3-3a81-9bbb-2ef8991fd262 | -14.38282 | -45.85151 | 2026-08-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90d6330a-a5da-32da-93cc-08514e018702 | -14.16692 | -54.39835 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be3f108d-797c-3eb1-b222-b6739fe525d6 | -12.45724 | -50.37336 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f966e6a5-ee06-3ef0-94c3-9cdfebd67b13 | -11.16492 | -54.88935 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4f405a7-3265-37b3-9b64-8c3c9830db7e | -11.177 | -54.90388 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3085eaaa-c169-384f-8251-61cce0a9fdd1 | -11.16979 | -54.88187 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 699dc629-1bca-3465-965c-d5145f46da23 | -11.18405 | -54.90507 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a03e8cd-c931-3f93-ad18-c6f1c87ab8bc | -11.22786 | -54.85877 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b14930c1-c9c8-3b1e-a3f7-c7f4cf03c45f | -11.2052 | -54.90866 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14a57fd9-3e0b-31a3-82d2-792dee7bde9c | -12.48361 | -50.38523 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af7958e3-e0cd-3c5b-a52b-f280c6df55ba | -13.4373 | -43.85278 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcfddc3b-8441-3be1-880e-61c825e983ba | -14.26696 | -45.2981 | 2026-08-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1823069c-24e9-30b0-9172-f65ca057445d | -11.19595 | -54.89883 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90e083c0-5f89-3f0f-8366-eb3768f1b375 | -11.18652 | -54.86826 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b92216f-ab02-31c6-9028-3b0c75588d2b | -15.14554 | -42.15862 | 2026-08-05 04:49:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 591c1792-704a-34cc-b675-6a7015bb921b | -11.2074 | -54.91737 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc352c37-5b0a-31b1-97d7-f82405a3dd24 | -11.20806 | -54.9133 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2b0330a-a47c-37f5-8d29-ceb1839a1b3d | -11.18472 | -54.90103 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af44d416-69fa-3194-8303-a152a18a2644 | -11.17197 | -54.89054 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0193733a-880b-3a52-b6b9-d89d82d5d9b7 | -11.20147 | -54.88733 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0451413e-00df-3f61-aabe-5c5a60361eed | -15.70549 | -46.75464 | 2026-08-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 433818ca-bd7d-38ab-ac4f-566601bed8b6 | -12.48018 | -50.38471 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44c811f6-5d33-33dd-b5b6-0c1d9fac5663 | -11.25063 | -54.82986 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9197e4cf-d25d-3146-9635-bc9736a09288 | -11.18453 | -54.88027 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b23a4e3-067f-3640-9d2a-5a2032fac09a | -11.19004 | -54.86886 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8424eb39-f6f8-31e4-8eab-8d861c985005 | -12.32189 | -53.17765 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f3a104f4-192c-353a-9372-22c5bbc7c062 | -11.17244 | -54.86587 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 992ef875-fff1-39c5-a25d-56abcd9cadb5 | -11.22654 | -54.86681 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77e0b658-b6f6-30f9-93c6-e311f8bcbb32 | -17.95328 | -43.8891 | 2026-08-05 04:49:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2920e74b-a165-3d65-9f55-d6971765b4c9 | -14.19425 | -54.42219 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc053bbf-1301-3d44-8394-700b10f8d112 | -14.26291 | -45.29991 | 2026-08-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e11b8e82-bbb1-3665-8632-be37a6080a7e | -13.44253 | -43.67719 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e74dcd56-aacb-327c-83fe-43aa10d161cc | -11.18137 | -54.92127 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 89187b87-2274-3d13-9f6a-79acefc5bf4a | -12.43861 | -50.52203 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b56fba6-bd40-348f-8f3e-01fa4ee80f4c | -11.17347 | -54.90329 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43f827f9-16bb-37c4-8d91-4bec7c774200 | -11.91831 | -55.90646 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3509dc17-3a9f-3489-a50f-f5f8f1421b8d | -11.34271 | -62.21806 | 2026-08-05 04:49:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6819d83c-4fbf-3c2e-b403-bb9e40e281fa | -11.1753 | -54.87045 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b8bf1ad-40d8-3d20-b14c-5b444c5dbfd0 | -11.19948 | -54.89941 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f4a289d-af3c-3fa1-9051-f4420f20ecf8 | -11.2008 | -54.89135 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffcab694-daaa-3e1f-bcb8-1f6f941bbc8f | -12.60067 | -46.93052 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4837bb93-5fb2-32e1-8258-02e735eadad5 | -11.17882 | -54.87104 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26267c63-8e83-3643-9bab-c47958ed9f4f | -11.16777 | -54.894 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2cd16856-6abe-3a7d-8a8d-293929ec3a3f | -11.1634 | -54.87671 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b57fbae-e51f-36f9-b939-fb07d702eadf | -11.16995 | -54.90269 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6352e138-7d0a-3fbc-a01b-59e8992bf72f | -11.17852 | -54.91661 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5203f266-20c3-3c46-a495-8522951709cb | -11.16424 | -54.89341 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94419a72-70f5-36c7-8ec2-20726860794e | -14.18595 | -54.40924 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfd785a2-d6e3-3bc6-8207-02f91466120f | -11.16473 | -54.86872 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e509ba60-ef36-307f-a391-4529c0e12d8f | -12.58671 | -46.93998 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b566e783-300e-317c-9f23-75a9381abcb0 | -11.19968 | -54.92023 | 2026-08-05 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47842277-3498-36a0-9f9d-caaa59a950ef | -12.32182 | -48.55887 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2d03e0f-56d7-325d-9601-4314faa037ed | -12.93186 | -49.4802 | 2026-08-05 04:49:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e129c74e-79a2-3a7a-a384-7f51750c4819 | -17.98759 | -47.15722 | 2026-08-05 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9252b02e-7ff3-3064-b49a-6be51e95ecae | -11.16709 | -54.89806 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7bba702a-5864-3518-964e-f85633bc9637 | -11.20653 | -54.90059 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03013915-6fd4-3213-9add-ca071f33e838 | -17.33831 | -42.63195 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0f276cea-ab63-3026-b511-f74f750019bd | -13.2527 | -54.26858 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2c6e2cd-c790-3fe2-8eed-70a657b68d8d | -11.17816 | -54.87504 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b83cdab-4f73-332b-8c83-dbe000a939f3 | -14.18932 | -54.40984 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6856d236-50f1-3819-9640-3eaaa5e90131 | -11.20014 | -54.89538 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c58d1bb-a47a-365c-a045-955d0320ac1b | -11.21709 | -54.90244 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e848e65-8912-341d-9627-146b64cffd07 | -11.19422 | -54.86546 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd85aa63-83b8-30bc-9138-986ae6f434dd | -11.17129 | -54.89458 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b29c8a82-4213-3997-8278-8ec24e178a2b | -12.46068 | -50.37389 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89ad01eb-5987-3855-8e3b-df41349b2cc4 | -12.58568 | -46.9477 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7196024c-31a2-3034-85af-69e383721244 | -12.43688 | -50.51017 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f6f098f-90fd-3596-aa71-5e9b66c1a0dc | -12.60639 | -46.91946 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c356191c-9083-3a0a-b86f-7e9c461e712f | -11.17045 | -54.87786 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c3680b-4c1d-39e3-ad0a-37a239febdfb | -11.21864 | -54.91513 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dae5df3c-96b9-392e-93b8-7bb825e4e795 | -13.68429 | -51.98446 | 2026-08-05 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cccd01a5-5830-3415-89e1-f3b94e32076c | -14.198 | -54.44178 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2123d03-28ec-3e38-a2fa-ccd7df7389db | -14.18258 | -54.40865 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4544acc-d334-3a41-a0d2-1011928f8ea9 | -11.71653 | -56.88766 | 2026-08-05 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c966fb87-dee5-3ce3-9154-391dcaf014ee | -12.59035 | -46.94437 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd3a0630-fb22-3569-87e6-b89fb4314c3c | -11.25414 | -54.83047 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34f55104-2da2-38ea-85de-96ff40e5bbf7 | -11.19442 | -54.88613 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddfa2f7a-12e0-3f88-85a0-44b791870cc5 | -11.21511 | -54.91453 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8091a5fa-8fcc-3357-84ca-677444fb2fae | -17.98321 | -47.15641 | 2026-08-05 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f3df9ea-6866-320f-a460-6f04298affb6 | -11.17498 | -54.91603 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e0eae92-2208-3c1a-8732-6313033f9640 | -14.02766 | -54.08492 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 638ceedf-1713-3e46-b60a-64587b757697 | -11.20367 | -54.89597 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04b2fc3b-2109-3c06-98be-0329a156b8b7 | -12.59191 | -46.93269 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12c77b00-5436-3e38-bb35-1832b1306c39 | -11.19043 | -54.91032 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 153d46aa-632a-3301-a67b-177950b8ee67 | -12.59299 | -46.92459 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0116d7e-3840-3395-82aa-8820fcdb062a | -11.19462 | -54.90689 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec4359e1-0431-3bee-a69b-97de32977486 | -11.1686 | -54.91082 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8c7429aa-5e37-389c-8d45-1c18bab6c904 | -17.8372 | -46.5154 | 2026-08-05 04:49:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb69ea38-8b73-3d1b-b7d5-d4e776ca2afe | -11.18672 | -54.88893 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bddba69b-0de3-3649-8a50-1baeff61f90c | -11.203 | -54.83413 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8aa17c5f-197f-3662-95c5-378d850fb906 | -11.18909 | -54.91843 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README18.md)
