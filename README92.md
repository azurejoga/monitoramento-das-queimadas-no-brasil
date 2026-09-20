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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f7443b5-e103-3894-adb4-c62ec0c4d3a2 | -3.84636 | -51.34178 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78fda88f-c622-3ca7-910a-02f5a378add4 | -8.16365 | -54.82638 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e375fc43-a793-316b-ab30-149a0bd6abc4 | -2.45367 | -49.21355 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d87433c-ee0b-31ad-ba59-cf63d9a4ba7a | -9.34507 | -61.16786 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5af9112-c9ab-38cf-9809-179796fde0fe | -2.98027 | -54.76209 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c639950-a0c1-37f2-8afa-1ba9e63818d8 | -3.34245 | -57.86523 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fac2d5a3-b0dc-3afa-b0f5-f36c23646177 | -7.55764 | -61.33131 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e6bc6c-a538-3579-89ad-3f140fcbd00d | -2.94378 | -51.97164 | 2026-09-20 05:23:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69515d88-ea38-3690-8c63-a00181b73d3a | -2.88618 | -57.8245 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b154927-1468-3daa-ac5d-8816c88b7b94 | -3.34769 | -59.86548 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 945e2b19-eb7e-3251-b599-44d09e690874 | -8.18323 | -54.75043 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72ac604d-dc63-321f-a211-e2c99791e39f | -8.88623 | -62.39959 | 2026-09-20 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a25c53a2-6295-31d1-8b82-2266912c95b9 | -3.36849 | -50.44574 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5adb985c-6592-3a4d-a3be-191df0a24979 | -7.77059 | -49.19915 | 2026-09-20 05:23:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 34a11710-3801-30b6-a4eb-cdaa51dfe7f8 | -3.37168 | -57.97343 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5165d58-4b65-3942-afe0-19d9183dfbab | -1.25769 | -55.76749 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3564f35e-b274-3e47-9316-daedefd3ba27 | -3.74498 | -51.81846 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 81508f0b-98d1-3598-a544-f5e3d40b4b27 | -3.26182 | -54.27021 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bf8638f-ceb5-38e2-9318-189ae29a5b11 | -6.34045 | -58.30082 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 297b0bc6-63f0-387e-b04d-b507b24d0787 | -3.30682 | -57.87206 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8933d0e-e912-3eb4-b971-91e876f6f23d | -3.45407 | -58.21305 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3478337-3d4e-3a27-8933-3e8a2e594fc4 | -6.72951 | -55.07391 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91c35103-0d2e-35a1-990c-8b3cd840e38e | -9.25419 | -60.7895 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ab1b85-d077-3c5b-9789-3087c962dbf5 | -3.05196 | -61.27188 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3da6ccc-4845-3417-b615-e21424d17438 | -8.2401 | -62.83971 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eb802a8-a148-3d76-b3c3-1b5535599d0c | -9.58071 | -55.10659 | 2026-09-20 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239f74eb-2d31-3403-9d59-7bf8551f76b7 | -2.97457 | -54.77234 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b52b23fe-e57c-3cfa-a7ce-c196cc14af82 | -10.30935 | -50.24902 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 52a036b2-ed76-3989-8eeb-75ac6845ebfb | -8.18141 | -54.76345 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb830be2-6f2f-3f8d-93d1-c12521bcf875 | -3.1396 | -57.67606 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbca236d-50bd-360d-8884-95132826c3dc | -7.58952 | -55.68446 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3815dcf-1350-3a43-9fd1-12641147a59b | -8.23029 | -50.65172 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7d8b5ee-f956-38e6-b10c-977f74a9619a | -3.38011 | -50.44414 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dff952b8-2ca7-3e37-ac9e-198a48d8d23d | -5.20416 | -56.04473 | 2026-09-20 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa5aa3cd-f18f-32e7-b107-5eb0ac6427b8 | -6.15875 | -57.70464 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48abeb40-541b-389f-8349-ebdf4e315ee4 | -11.72226 | -54.56408 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc938d65-1f8d-3eed-af6d-5df92b8c8c97 | -15.87108 | -49.91557 | 2026-09-20 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c60dffc-c4ba-3977-961a-c4a910631603 | -12.34026 | -50.69383 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5043d890-7163-35c7-9dc6-aaf3c57c0593 | -11.38788 | -51.41916 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ba8a6b4-a439-308c-81b9-a24851e9af2b | -10.91985 | -53.969 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30b5b8bb-d662-3813-a320-73fb9fe0139b | -6.38908 | -51.67911 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7edb5a05-4935-3b7e-a4fd-4df4543e53ba | -13.8943 | -48.58048 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30f487bd-e815-3ef4-9826-c4a9d5c9c429 | -11.37732 | -51.40936 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 141c3c56-ed62-31d5-926b-185cc79a4c0d | -3.72965 | -60.61894 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 420d4683-9805-360a-a2a8-aaa625cd0a6f | -6.07184 | -57.72477 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5c9cbaf-00a7-3ab6-92a2-4b5e6db83ef8 | -6.08893 | -56.47063 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9256cb56-fdfe-3405-bab5-c6d67354ca58 | -6.33887 | -55.29916 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d2ca6e0-04a9-3cbb-99b1-c97958b3b2bb | -10.75061 | -55.99546 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18532b05-a66d-3d47-8172-d3ba19b7dc97 | -6.39655 | -55.25079 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91096fa4-f499-3508-abf9-3308f98055ee | -5.74676 | -57.5806 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 508e33af-8338-30a7-a888-ac60c2f6e680 | -5.86866 | -51.56802 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45738434-39cf-371f-a471-d648de54b049 | -5.73238 | -52.23624 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a99bf01b-2009-3e3b-a1c8-b2c2554ee5da | -5.99803 | -53.69295 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68149809-a3d7-3a6e-a58a-9d294b396553 | -5.73189 | -53.45395 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9029f18-f6ce-315a-8695-6c120cc8fdad | -5.7662 | -57.45296 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75289677-f85e-37d0-a2b3-90c2d78af56f | -5.8878 | -53.64566 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7346a914-dcae-397a-b726-a3200e51b03d | -3.70252 | -60.57587 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60395b83-365d-3b7e-b749-36f821c3f5dc | -11.21771 | -54.07941 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3dc41fd3-b658-30b4-85c6-a7ee3a78503f | -4.20709 | -56.34113 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e206694f-2d54-386e-adbc-df7f0efe8e7d | -4.62602 | -55.74989 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5805f5b2-055a-33e3-bcc9-832ca5058a6f | -3.36354 | -61.32419 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad6a989-a143-325f-96f1-e927eb7ee9b0 | -14.04473 | -52.08035 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6fd5499-88b1-340e-9960-7e1b31a44c20 | -11.22269 | -54.08471 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c347a482-700c-3cfa-986c-3ec5274db3bc | -3.86813 | -59.0084 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9186850-7c9a-3229-b69f-01c705223060 | -11.74234 | -54.55662 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 120fa84e-8234-3f52-a680-7021036a8d20 | -4.49496 | -54.85342 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd8220ed-82a2-3e2f-bc92-c38c437c43a4 | -6.15332 | -57.71635 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 068a2095-2613-3e80-bc07-358d8a2accfd | -9.93637 | -60.73124 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9f067be-0852-3a57-bde5-85ff951c4666 | -11.20827 | -54.0825 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8621d87d-95a8-3a6e-95df-284837ba19a8 | -6.61374 | -50.06297 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42ac86ee-8c90-336d-8ab9-7f04dccc4260 | -6.75829 | -47.92606 | 2026-09-20 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 953e9a66-b621-3bad-9ac7-1b4b00064fda | -3.79699 | -59.70669 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 756b6380-a5bb-3690-a7f3-39b9fc0cb839 | -5.986 | -55.69689 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a322f83-bee8-390b-8a58-06c391e08d58 | -10.9095 | -53.97308 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4e9ef1a-cc15-3b43-a4e4-eaab6ec05d14 | -5.84424 | -53.55603 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 767c1bf4-b4b7-39b6-9c82-47e67dcbca49 | -5.98247 | -57.76652 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95b2546-429d-3359-bc66-89f11570d431 | -5.76259 | -57.45247 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3abb4dfb-427b-3aae-9ec7-e093533edf96 | -5.83909 | -53.52558 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2df76a72-f485-38c9-9df2-3d083dd90479 | -14.93212 | -49.91008 | 2026-09-20 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2faed0ee-09ff-391c-8b3a-a0a9c2896026 | -5.7539 | -57.58168 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0e231c2a-fb81-3e16-ba06-04160499a60f | -5.86859 | -51.57407 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7e049d-a0d1-3460-bfc3-b963718147ad | -3.23542 | -61.25647 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc227a59-d5ae-310b-b909-2028c20472cb | -5.84816 | -53.5616 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df464e19-d50d-3b5d-ad04-2f270122101b | -6.31179 | -47.62349 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 43d02dae-4baf-36f1-80c1-e9ed0256a081 | -5.84902 | -53.52215 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39085a91-da76-31cb-9fac-2b80422de3c0 | -5.74738 | -57.57649 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26abc0ee-94d3-3455-9105-99a42cdc376f | -14.67369 | -54.4598 | 2026-09-20 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc33c8b6-b03a-3717-9309-8599342b5018 | -10.86682 | -57.15265 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac1ffd42-55db-34eb-add5-5b5bf9d9339c | -5.84304 | -53.5311 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3bc6d84-e669-3511-9943-78a6ee1488b4 | -3.69536 | -60.5783 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 546e1334-5828-338a-8836-f11b3f8afd2e | -3.73182 | -60.60514 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 434d7a01-12ef-3fb1-a2f0-572649b76e56 | -6.81872 | -47.88625 | 2026-09-20 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e87f382-ce30-35c6-9fa3-ef1835a0cda3 | -3.71703 | -60.63466 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd551ff5-ea7b-381c-8fea-37b7ed877001 | -3.69109 | -60.62712 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7300db89-f6e4-330f-8c4d-6b609e7e6f29 | -3.7876 | -60.72712 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44cee3e1-2355-30c7-995d-32c88636d160 | -3.80193 | -60.72225 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c0c4542-c081-3f2e-ac53-534a15b188fe | -6.31893 | -47.62957 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b3ccb95a-c02a-37ab-b249-f622b04f8ecf | -11.02541 | -54.13601 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 205b321f-8f8c-3687-bf98-01716913402e | -3.38087 | -61.30145 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3143cc7-77d3-3adf-8d6a-0d748c06010a | -5.92546 | -55.70502 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README93.md)
