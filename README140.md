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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7c6e2af-540e-394a-9863-9c05de8874b8 | -3.5645 | -54.69394 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f418812-e825-30d0-b3b3-02d64916ac8d | -0.98127 | -52.44847 | 2026-10-10 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| de7e35b4-2c31-389f-832e-35c5f273ff5e | -3.10385 | -53.78284 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09753e42-b6d5-34e7-92d4-b88455703654 | 0.00786 | -60.57964 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f024f09-2da7-3987-8cb1-a0cb1a9c9f5a | -3.58128 | -54.7118 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3905a7ab-6367-3c06-8839-6859747ac9dc | -5.97495 | -55.34889 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59dc4daa-5cf4-3fcf-b748-f8d6a44d2650 | -2.7266 | -54.1437 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74726366-99c3-3629-b0ab-45b3db8015fd | -3.21272 | -53.85827 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e7f07e4-45f3-3dfb-88f0-3f997054dd57 | -2.55297 | -58.03046 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c025b695-9d9f-354f-b9fa-d5ca89209583 | -6.44406 | -55.05914 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3fc73e8-0ba7-3241-8605-f111f303f441 | -2.99842 | -57.75779 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7755a842-8315-3924-8558-d7e568ff55af | -3.87853 | -55.83859 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac153da0-74be-3883-b6e6-5e10edef7332 | -2.99454 | -53.8992 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95320f55-5fb9-34d9-a1eb-8f63fa7717be | -5.06864 | -60.21944 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7539d27-dd59-38a8-b96f-4815d5e1ef15 | -3.31497 | -53.83863 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f66bea31-dbeb-3611-af4d-cea7f8c293d8 | -4.73436 | -55.67316 | 2026-10-10 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4f73560-0023-3e28-8ecd-f5a5b49e3e8b | -6.42928 | -55.27122 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb6ceec4-6f84-3c88-81cb-ee3dee68a502 | -3.24894 | -54.02748 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72887876-8740-3f22-9f95-e7017ec56b5a | -1.2581 | -55.79247 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a303ccb-f81a-397d-83d7-f895e89e5836 | -3.806 | -58.88772 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e9a9aab-3a1d-32ec-8cac-6f985db72c9b | -5.25662 | -60.34023 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e0af763-c5be-3cc8-a270-da17c561d73f | -3.88104 | -55.99086 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8eb6233-7b23-3a97-a707-ae819a10cfb5 | -3.11788 | -53.79528 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a870bd08-0974-3d6e-8e08-8e61b2c00530 | -2.51507 | -56.14076 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf305ae-5da8-35a0-9d28-28d826db84aa | -2.99374 | -53.9048 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92fb2ae8-f556-3a48-aaa4-d81ea7e1005c | -3.92821 | -56.03644 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f96229b-3c5c-3ba2-a1a6-bb145ad914e8 | -3.18683 | -58.63441 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d37181e7-36d2-3ec4-8b7f-263df48773e4 | -5.30555 | -60.07972 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 168b2b2e-9a23-356a-bbe1-1e533d682d27 | -3.53205 | -59.57143 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a714773-fbca-30ff-a543-274f3b378f01 | -3.18198 | -58.63367 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dab33988-0125-388a-bdee-9c62c7293a84 | -3.19088 | -58.64049 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30b36dd8-c410-3902-9b13-4b559bb62a3e | -3.12662 | -54.18272 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a55ecadb-8219-3c44-9eaa-314f304c9ba9 | -2.83792 | -54.81331 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd6578c4-2654-3e71-94e4-275f951bdb6f | -4.29027 | -55.13171 | 2026-10-10 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3581f08c-021b-3cb5-abf6-8c983b2aeb2d | -1.88609 | -54.67495 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dfca48a8-496f-3198-91f6-233017d5dd60 | -3.5876 | -54.71278 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bb84798-21ec-3203-a9c6-33fce42dfb1b | 0.00731 | -60.57613 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d614ec-fb96-3e54-b716-e26b16993f40 | -2.99694 | -53.89435 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8175ff85-e1b0-3aa7-8b04-34014efa7db7 | -3.43637 | -59.36047 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d122fda1-ef96-330f-9892-3ab4a8911114 | -2.02253 | -61.26998 | 2026-10-10 05:48:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cb0624c-540a-3f75-b6ac-4ffe54571f28 | -3.53538 | -59.57544 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20d59020-7a27-3af1-8418-d9c7f6b1874d | -6.37519 | -55.17278 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5af70af-e9d0-3453-a667-3e5df1c6fd1b | 0.00272 | -60.57324 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6127e100-f95c-3bd0-9245-a586669635af | -3.43289 | -59.53911 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a59bd5a8-52a8-349d-a4c0-56af675d8dfc | -2.86256 | -59.10985 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c504ffee-7da1-34b5-a01b-acc02eeb13c0 | -5.08077 | -60.21882 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d47dfaaf-d2e6-33ca-ad49-e40f63143258 | -2.063 | -61.1381 | 2026-10-10 05:48:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65077232-e962-3161-989b-6597e145d943 | -3.4387 | -54.54199 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4c3b89a-9a63-38c8-833f-72a08ff869fe | -5.19444 | -60.30656 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b468cc75-9d98-308c-ac07-cd352e86c021 | -6.49487 | -55.31186 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e1e78b4-d3cd-3321-a816-8ccf4ee5b7a4 | -3.8869 | -55.9917 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| afd59af7-3dcc-3bcd-9d8a-1ebbe290b873 | -6.46742 | -55.51304 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 81bdf3c6-2bb7-39a7-8aee-ae32eb008c43 | -0.5175 | -58.09982 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b16e5b5-8d98-384d-b66a-1ec83fbef560 | -2.40313 | -57.89923 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af1c05db-7783-3e83-80b4-2b30a361a9c1 | -2.93514 | -54.08424 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b862dbba-f6af-32ae-b83a-17ddf4842adc | -4.52153 | -61.13163 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 065839d4-94bd-3a07-8dfd-83a9a8c6ef49 | -3.49638 | -54.60937 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a1082c6-e151-3308-986b-f58bc0fa1b5a | -3.37138 | -59.38482 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0578e065-ecd9-390b-8d87-f18f90adba69 | -3.58352 | -54.71943 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2e0b2af-6ad0-33f8-bcef-6afcae52cea7 | -2.4941 | -58.08284 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ad5b3fa-1d41-3d81-95fa-32855020cd12 | -3.12679 | -54.18265 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0228a576-b6b8-3427-a04a-7d3caa05349b | -3.84425 | -55.79497 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4993546a-7220-398b-91ba-fca207d56d2a | -3.58983 | -54.72045 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbbcea79-45a6-37e2-8f03-cfed2480624a | -5.87085 | -53.51229 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34afdce0-157c-3106-82e4-d94b7eaf234b | -3.43316 | -59.54081 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1487e76d-1bb6-3e5c-8cec-07183a6304e1 | -3.98522 | -59.36266 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eaf19a7a-326a-33c6-ac26-6c7f3a085aed | -1.64055 | -54.40184 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9bbe5068-083b-3dd4-a928-96412e7ff46d | -1.51321 | -54.5256 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f87f44b4-fd34-30ac-b03e-7cf7fb5452b2 | -3.73047 | -59.46451 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3f717846-fa9c-3f2f-bf92-5408871372d4 | -1.27493 | -55.75889 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a05e0f73-2c1e-35b5-8992-9d707555b66a | -5.18936 | -60.3103 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3030ec9-d2b4-3884-965a-2b2e651199f5 | -6.36952 | -55.16661 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d18ba4a-3e37-319b-90e2-5479a7642c19 | -2.49495 | -58.07711 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e420436-9306-38c9-a52a-2c9e3470b1d4 | -3.7497 | -59.39874 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e75a202d-f29e-3147-bbec-a6196fae845f | -3.07135 | -59.16945 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec56290a-8051-3a34-bccd-15de7f44d8b5 | -3.56943 | -59.09558 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 473e469c-0dc1-3124-91ab-663f5fba31f1 | -1.9539 | -54.40371 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ca75044-0e84-3bd3-b791-5206ba8fd222 | -3.22278 | -54.29655 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dbddfd88-48f0-32c3-b680-609b4174ec54 | -3.77797 | -58.58471 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6c4a75db-4e5b-3a0b-95e2-d18a29c1104e | -3.01621 | -57.77931 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7096487-019f-3184-bf0d-db49a631f5a4 | -3.10156 | -53.94132 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f52485b8-517b-34e2-a67e-219ec1958b04 | -2.4552 | -58.03146 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 718fdd22-60d6-3e10-a357-f7e4d2a24350 | -3.90375 | -58.95688 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 254fdbeb-c37f-35c3-b1ef-9b8b53f65517 | -2.4191 | -57.99953 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14a0f9d5-0836-37b6-acb0-fe77b819bb9a | -3.57644 | -54.70072 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98d49dd4-0b36-3dda-aa6f-f5f16e5cce21 | -3.12088 | -54.17661 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 33977117-acb7-385e-b87d-614f7569f128 | -1.18883 | -55.66056 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b1d6f5-ff83-3a1a-9155-8040f20a0870 | -3.58426 | -54.71409 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07370259-c69a-314b-aa61-872f39356dd1 | -1.61107 | -55.16062 | 2026-10-10 05:48:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaf281f0-0346-3c93-b545-49c182c50731 | -1.32723 | -55.45643 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aad54587-af84-3aa8-81ae-fb231e19c313 | -3.11206 | -53.78875 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06fb0f29-5a28-36b3-9c5a-320d3222c5a3 | -2.55211 | -58.03617 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4677e1f-ffe9-3cba-919c-a01ebeb0a186 | -6.36882 | -55.17181 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48209970-3cb2-3529-ad6f-2f02f996447b | -3.95879 | -55.3481 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44d935a6-861d-36fc-9e5e-8039351a7d6b | -5.70673 | -53.48056 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db6caed4-0b5d-3abf-9ce8-67b2060f0a08 | -3.30549 | -54.00064 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cef753f-07c4-3ba3-a564-78be3c3ab8dd | -3.20818 | -53.85778 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8ddff36-d2a2-3ec4-89fa-877ca9965f33 | -5.70596 | -53.47758 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d919502-bacc-39c0-9f24-28d3fac9a8aa | -4.11124 | -54.01807 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56c1bb28-387a-3100-833f-8cccec04eade | -1.73033 | -56.06159 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README141.md)
