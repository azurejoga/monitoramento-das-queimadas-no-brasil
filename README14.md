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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2414049-e307-3f8e-8292-4d705c22d94b | -8.90624 | -60.59123 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0abc4a46-4318-3367-9c27-8d9b6de24a8a | -10.4776 | -44.39352 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dac1c40f-2bc1-3bba-b74a-812818ca11f0 | -8.22285 | -47.33648 | 2025-08-07 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4140a05-f853-33f5-a651-e5ed20b83add | -8.92049 | -60.55709 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 631737c4-1d9c-34c6-829f-fd23def714a8 | -8.92056 | -60.56361 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b110904-aea6-3982-a9cc-42d68acd8e0c | -3.93844 | -48.90996 | 2025-08-07 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea76f398-8c24-3248-8e53-6c5a68509db9 | -6.52396 | -45.57804 | 2025-08-07 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20a4d096-1a3e-37f6-91e8-87b8855455ba | -8.25535 | -45.07568 | 2025-08-07 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4e3aef2-f98b-3fce-8134-0df9fd855ba9 | -8.91761 | -60.54655 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62cd0c11-1957-3216-a21e-3eb5a777d41a | -7.53299 | -45.15055 | 2025-08-07 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12342f38-e009-3f55-b6a0-53a7b88921ba | -9.07022 | -45.05675 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3346bf5-e02b-3578-b5c4-78f720836a4c | -4.02985 | -48.06319 | 2025-08-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e798900-c39a-3294-b96a-688656549512 | -8.91585 | -60.55629 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c313aa6-4c3b-3515-ba29-f052349e3cfd | -8.91803 | -60.57833 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03a9e1f0-e58e-3495-94f0-7d3bba3bfb16 | -8.97988 | -40.62289 | 2025-08-07 04:51:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ba35b4db-ebb3-3062-aa76-a24a40e86129 | -10.43966 | -44.39085 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b23a02d-79cf-36e8-9bab-eb3cfe4b9c2f | -6.76326 | -59.4816 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1193377-6bd8-318a-91a6-7e22fec97622 | -8.52945 | -47.45856 | 2025-08-07 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e267d9bd-75cf-3ad7-8487-f9df7f9c8579 | -8.91261 | -60.60078 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 776252a1-5cc0-3949-8950-d994a62a60c9 | -8.90971 | -60.59031 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e5b1777-f04f-36ae-8920-a681c02ab657 | -8.51825 | -43.29817 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b6cc06a9-a5e2-3130-867d-30a7093b3e9d | -8.24962 | -45.08054 | 2025-08-07 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f0ca4bf-b8f4-3e7f-b3bb-0f630ad2a698 | -6.42048 | -53.36772 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b420704a-6506-3b70-9396-5f84eb4ab7cc | -6.55103 | -56.19902 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0865dde1-332b-35d8-8975-02da6d762527 | -8.91339 | -60.57749 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d4edef-37e8-3f87-b1b6-73d1c63b3fd4 | -8.90456 | -60.60094 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ece86a9-31cf-3e5b-abc0-1bae4e514b3f | -8.51615 | -43.29896 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12a11cc3-2b4f-3768-943b-172ef32352d5 | -8.92136 | -60.55223 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b874df8-31cd-3e74-bc4c-7f880709b2c4 | -7.02484 | -42.55029 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d0143a4d-1974-3971-945c-ac9b2fd0c179 | -9.08493 | -45.06192 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7e57f33-6e07-3c3c-a909-3b179b39c310 | -8.90708 | -60.60485 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2342a73-2d99-3f65-896b-10255718cc74 | -8.91423 | -60.57264 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14e24a71-284c-3818-b5cd-f3695f0af763 | -7.43502 | -60.01771 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4885094-f9f8-3a0c-ac52-9f85018f78bb | -10.70492 | -48.86657 | 2025-08-07 04:51:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 921e9251-fe53-3bb4-90e0-2c558a2b9404 | -8.91035 | -60.56032 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e07f0834-9e5f-388b-a26d-b20adfe5c46c | -8.91436 | -60.59111 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa251738-018f-35fc-b8bd-8bb3d8fed3db | -10.43472 | -44.38665 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70b57d85-938d-3c37-85e4-d271fae96fdb | -3.8444 | -47.75057 | 2025-08-07 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c510274-9a09-31db-baec-cdde770d8808 | -6.64999 | -58.81979 | 2025-08-07 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ba022d-90dc-3663-bf30-3c136c075758 | -8.91929 | -60.5433 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b64456dd-8204-3272-84f1-3f24cf5ebdad | -8.91987 | -60.58709 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 133a9a6d-ac25-38d3-b81f-36d0794fea0c | -8.91385 | -60.60259 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15d31ae4-b873-3989-a594-b8040da9ec1b | -10.43303 | -44.40018 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc6c40a4-7881-387d-aa75-26ffed9357da | -7.3917 | -44.62404 | 2025-08-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9768821-67c3-3cda-903d-d0dde90cc132 | -10.43218 | -44.40701 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4f0dcbb-acf2-38b3-8786-7fe0191d2001 | -8.92249 | -60.57253 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5fb8b5c-301c-33ad-8291-92d7762de107 | -10.64044 | -44.74982 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17b4d947-6dce-3488-bcbf-0245e15c9fc7 | -8.91771 | -60.76037 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 668c2476-4f3b-352c-8f52-69200287029d | -8.92224 | -60.54735 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78d7b8a6-1b85-3500-a4ab-d991980557a1 | -8.91933 | -60.59854 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f62cb66b-42d6-334a-b99c-305911d60422 | -10.70939 | -48.86367 | 2025-08-07 04:51:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dabc92d0-81f5-37e5-a237-a06ed68e1f50 | -10.6331 | -44.76538 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b78d0d5-90ad-33e4-b282-8fdcfdcbe9ee | -7.53044 | -45.15118 | 2025-08-07 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9ebcb09-f455-36bb-ba5c-2ed829be7a7c | -8.90959 | -60.57185 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ec4d178-33f1-3ac8-8590-956d44a3c8b3 | -7.41295 | -60.00907 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 828a3c6f-181e-3543-b061-acf10eb1e238 | -8.91887 | -60.57344 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e4b8ea8-3927-3d18-bbb6-9ab060acf6f2 | -10.43059 | -44.37595 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 219972c9-62f8-30c7-be90-5c63bd750efc | -10.44996 | -44.35247 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04f932b6-4ce5-3ae6-b25d-fbf6f5efad5d | -10.43514 | -44.38332 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2ebc864-8d7a-3d00-8621-f16b12ef5d84 | -10.42809 | -44.39602 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8af39a4-c321-3384-be5e-120190b26974 | -3.51703 | -47.20804 | 2025-08-07 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1414907-001f-386d-8197-0b17ce25b78d | -5.81636 | -59.22678 | 2025-08-07 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f585499e-f6b6-331a-86c2-85c3f537789c | -8.91677 | -60.55794 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d742ec66-6f4a-32d8-9a80-38fb4030e346 | -6.91742 | -52.84351 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08ef4b44-a28c-3067-91fb-f8b282d966d1 | -6.64074 | -58.82244 | 2025-08-07 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58e299f7-508a-3e67-8a6a-69e8d1b086dc | -5.00151 | -56.04019 | 2025-08-07 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af65b491-1747-3f87-a44a-726d0a7a7da5 | -6.68237 | -58.86274 | 2025-08-07 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56a778ea-19a9-3ff9-b270-13e37dc2c0e0 | -9.07989 | -45.06123 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b04905e7-cdb9-348c-8ad3-7ade91ca8b92 | -3.51651 | -47.21148 | 2025-08-07 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f87b8380-3611-3ce9-9600-700e1b8ba1f0 | -7.91362 | -45.53258 | 2025-08-07 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d2463e8-de64-399c-8065-5df4e8066886 | -9.65393 | -43.84803 | 2025-08-07 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e998e10-7f1a-3a00-9419-89c3cd092f77 | -10.47882 | -44.38398 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c00b067-71e3-3274-a5a2-58a8e19ce63b | -10.42189 | -44.40191 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87968944-e0e3-3098-98b8-1680bc81ce81 | -10.42356 | -44.38845 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c17ce119-9f4b-3c96-b668-b882067d684e | -6.41607 | -53.37415 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d34ac19-11f4-3125-b109-c30e365fecff | -7.40836 | -60.00835 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| df41237c-06a2-3467-a933-3060a3bfb7f0 | -8.90924 | -60.54005 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a60d34ad-e522-3494-9c0a-6a469632a617 | -10.43881 | -44.39765 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25cfc775-30bc-3fcf-9c2c-3ea24b996fee | -8.91044 | -60.56692 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a1cf4bd-33a2-319b-847c-537094d9fa85 | -6.53799 | -56.21007 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f52de27a-f29f-3728-bc7a-00a553efc6de | -6.95295 | -51.62787 | 2025-08-07 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0df256d2-0be3-3ef5-a905-928fc55bb91a | -9.72844 | -48.2999 | 2025-08-07 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa824458-8d0e-3acb-a7d3-2adffe8e60a7 | -3.65333 | -48.32364 | 2025-08-07 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83c2b133-1f29-3c46-bea7-e549b3885cbc | -8.92039 | -60.74538 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 78e36f99-ffb8-32d3-9b24-0a6175f9e2f0 | -8.50968 | -44.74694 | 2025-08-07 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04524741-7c25-321b-8a7f-dda0db570483 | -9.46192 | -40.37737 | 2025-08-07 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 870b0b61-c1a0-383e-adcc-3b2f47cf6ee3 | -10.45746 | -48.81279 | 2025-08-07 04:51:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf1339c3-05ed-3326-acd3-5be30fba0db4 | -6.85929 | -44.30576 | 2025-08-07 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b9d056b-5c1b-31fa-96fe-a784e857a7a9 | -7.91701 | -45.5437 | 2025-08-07 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f4d139-0878-382b-87e2-41f6b1597051 | -6.91357 | -52.84644 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06102226-f284-3ec1-87cd-714c8c8457c5 | -6.51247 | -56.20592 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9508adc4-9649-35db-8dc0-4a8aa44fa038 | -8.92312 | -60.54248 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7b16e85-8e64-3f1e-a651-50ed0c870c78 | -10.43345 | -44.39682 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecce3402-d06f-31d8-becb-19922e6f9ca8 | -4.82114 | -47.31689 | 2025-08-07 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0825852c-34a4-38f5-be9e-a5fbe8cb3cbf | -6.92734 | -52.84505 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697cd0a3-7b81-3232-a933-851221fbf351 | -7.39681 | -44.62443 | 2025-08-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91ea883e-dad5-3623-8d6a-87028fed567a | -8.91553 | -60.59285 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97c5b25a-0755-33f0-afd1-c64947e2d328 | -8.91299 | -60.54573 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ba2664f-bdb6-3adb-9c1e-f26e139536ae | -10.44417 | -44.35488 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0955d7dd-bae7-3479-b69e-68e3d7af25a0 | -7.24214 | -44.63851 | 2025-08-07 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
