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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b85e8026-1e42-3a6c-bc7d-a810a9d76a2c | -2.16612 | -53.6863 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84ca99a8-3955-39f0-8ee1-e43a26ffbcd7 | -2.16498 | -53.67173 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8b49c95-65a6-3b9a-8f2a-bc07309498f6 | -2.16443 | -53.67524 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 408d56ff-373f-3e73-9308-1ea45c02063a | -2.16219 | -53.66769 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30661ba0-db18-36cd-aa31-a35da5a13465 | -2.16164 | -53.67121 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a6107e2-e616-3dcb-b62a-6b06cf010594 | -2.16109 | -53.67472 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56c7ef31-7ac4-30a0-843b-eb78d917416e | -2.16054 | -53.67823 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79cf6d7c-978c-3be5-8bdc-9dfbf04ab66e | -2.15885 | -53.66717 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78d62589-c366-3b5f-b10d-159d13d873d7 | -1.15285 | -53.63794 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84c888c7-91bb-3eff-9ed7-d44b83e74344 | -1.15231 | -53.64144 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd386658-d55f-322a-ba46-3be0090fedb2 | -1.15153 | -53.3824 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f08ba44e-3389-375e-abf8-d599519bf611 | -1.14952 | -53.63747 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62987c3f-3a26-3fa6-af54-8abb6d7f926e | -1.14819 | -53.38186 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ef2bf6-cc32-3d32-b747-19cb745a354e | -1.14674 | -53.63347 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 150cb428-0b22-3c01-9073-b9a56cb65058 | -1.14341 | -53.63292 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f657f1-02cb-30ea-b153-c9e0e99bdd4f | -1.14287 | -53.63641 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a35311fd-5472-3a7a-b0a2-d6250e253274 | -1.14118 | -53.62537 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b409662-5de5-3200-8ddd-49247f76db66 | -1.13573 | -54.09952 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd4109df-2e63-3655-9357-3ca05416b1fb | -1.1352 | -54.10296 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32754819-4661-30e8-9d53-32dc1159e701 | -1.11898 | -54.16384 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00919ad1-dc45-3ac0-8d1e-daebed6cf9e5 | -1.09308 | -53.65017 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dddaefc4-d397-3fa4-a63d-e876581c29be | -1.09254 | -53.65365 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d786029-87c6-3a76-a001-01f967376192 | -1.08975 | -53.64967 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9b121bb-d389-381b-a0ac-3b3fbf148e40 | -1.08921 | -53.65316 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44feee04-17bb-3da3-b51f-578237e4064e | -1.08321 | -53.64871 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2900ebef-d362-39dd-aea0-cbb8538447b5 | -1.08266 | -53.65222 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75b8b59b-ec59-306f-914c-a66e5e7cdbc0 | -1.07989 | -53.6482 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1272383-cf4d-3e26-8035-fefc93afad3f | -1.07934 | -53.65171 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2720e02-14f5-3188-b570-e086eb1844d8 | -1.07662 | -53.66909 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7436d1c-1848-334a-bacf-01a373f8ef1a | -1.07215 | -53.65413 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6c4b54-2c2c-30c1-bb0f-905e806e6e1e | -1.06828 | -53.65713 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15d6884b-7c6b-3f8b-b211-78000dc5ddd2 | -1.06773 | -53.66063 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bac9f66c-8100-3c71-9833-dd5f851a1464 | -1.06643 | -53.36219 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4af8a35a-cf80-31cb-8f2f-d95491a638bf | -1.06309 | -53.36168 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a6f0485-18da-3716-aab0-1fb6bf7cfb17 | -1.03639 | -53.73078 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3eabe5d-ecfe-33fb-86d7-3b4b143d3a33 | -1.02312 | -53.72871 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1bc3db4-2167-32ad-b900-1362b425766b | -0.98654 | -53.70166 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 274fa6b9-a174-3099-8c56-8084e39fe727 | -0.986 | -53.70513 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e941749b-48c5-3a1c-96dd-f1ee89349774 | -0.98214 | -53.70811 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14cf90b9-5a50-32a5-bde4-3dc8b7cad0c8 | -0.9816 | -53.71161 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c8cbf8-275e-3e72-a82e-7446a3187d86 | -0.97828 | -53.71111 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59a81c9c-8068-3718-8341-9575de5c908f | -1.19881 | -53.91157 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ae1b5ee2-3daa-354e-bc9d-27b1ad5820d8 | -1.19827 | -53.91504 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| a4744af5-0c2d-375c-93d2-7271f050ad71 | -1.19554 | -53.64804 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7060dc0e-8dc3-3b38-8a5f-9a3703c54575 | -1.1955 | -53.91109 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d2c4ff0-7e4a-3b43-9a08-3a2566a28b6b | -1.19277 | -53.64399 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58dafaf7-f877-306f-842c-8cbb8a5879c5 | -1.19222 | -53.64751 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3a9e6c12-f6b2-3966-bc5f-9bad9f5b7c95 | -1.19219 | -53.91058 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afacfa5e-2742-31c6-ade5-1e9cc380b503 | -1.1897 | -53.51093 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4e07113-9ec2-38b3-95b1-3d10c553198d | -1.18952 | -53.68652 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2b4b129-73c6-3053-8c07-26374e7fc5c1 | -1.18915 | -53.51443 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2787b966-67d2-3a2b-96c6-78f03042c395 | -1.18897 | -53.69002 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36d3d0cb-95ae-3e6f-909c-2d7e8d437361 | -1.18892 | -53.66858 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c5f2a74-e149-3f71-8117-ffdc4fdb7c98 | -1.18842 | -53.69352 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cda0944b-1622-3699-a924-b69cea64a08d | -1.18619 | -53.68602 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4ff2643-d236-3859-9822-75a32696f5fa | -1.18582 | -53.51392 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| affe2898-763f-3d08-a4d2-e94ce85537ff | -1.18564 | -53.68951 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d209f484-5b1b-37f2-b8e0-0c2aa9adcde3 | -1.1856 | -53.66805 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6826ef15-610a-3208-9947-3ae15d962d88 | -1.18527 | -53.51738 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adf20ed1-efa3-3e84-99e4-e105b5377104 | -1.1851 | -53.69302 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 63081920-72fc-3512-ae87-422feedba2e2 | -1.18485 | -54.13174 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41ebe1a7-53f7-3338-8c8b-cb3fb60021a2 | -1.18287 | -53.6855 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ad27025-45ce-3cd6-a944-28fe39072390 | -1.18232 | -53.68901 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35ccbcf7-6720-32fc-a791-d3eb0299a4a5 | -1.18177 | -53.69252 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e700589d-660b-39a8-bea0-f79bfcb0a95b | -1.18155 | -54.13124 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 35040474-ef2b-391a-8130-1ac2c15bb0bc | -1.1801 | -53.68147 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36bd822e-72a4-33f3-a447-0580824df859 | -1.17955 | -53.68498 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 988f6aa2-2325-3941-bc77-0bb9001cc1bf | -1.17733 | -53.67744 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd970791-42b1-3499-b26f-caf34b1c7efc | -1.17678 | -53.68093 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2252dd79-fabc-3d2b-acfb-519c2de613d3 | -1.17445 | -53.63047 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4bff780-df01-3eeb-82f3-14ebdfb2a307 | -1.17346 | -53.68041 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d98c52a9-0284-3ef7-8105-8d142f0434b5 | -1.17291 | -53.68391 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc6a63ca-0521-336c-9d4e-e2c92ca174b0 | -1.17285 | -53.90414 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76a18f4e-86ba-3b3a-9881-44b9436c30c5 | -1.17236 | -53.68742 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e14f63d-b682-30ef-ba9d-8e4adc24ea0b | -1.17111 | -53.63002 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9f68afa5-2197-3533-8662-257b56822f7e | -1.16959 | -53.68341 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f291cc7a-99cf-31c5-b67b-a8ed2b25c83e | -1.16904 | -53.68693 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc8cdf26-9068-3583-989b-be74f5bd1b11 | -1.16626 | -53.68294 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3f520d1-f525-33a8-a4bb-928feb96e2cc | -1.16571 | -53.68646 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3d672e1-d4c4-32d5-92a8-89426a890664 | -1.16261 | -54.07896 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b8ee171-1d15-31cc-ac3d-eb3e809b584f | -1.16208 | -54.08241 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e599395-52ee-3d0b-838f-541a222e40dd | -1.16154 | -54.08585 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abcaf61a-75bb-39dd-88dd-1968a3cfdcc1 | -1.15931 | -54.07846 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d172f8ef-3d96-36fb-9e06-972c9de57e61 | -1.15824 | -54.08535 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca42ab3-5e5a-365c-8125-8486a43c3dde | -2.2008 | -53.74545 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fb67a8b-b867-32c7-85bc-511b89067a2e | -2.19459 | -53.7193 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fb886e0-e82a-388e-b9b9-ef49edd57aee | -2.19405 | -53.72282 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c5c07cc-7fdd-3549-a425-3839a35de092 | -2.188 | -53.73986 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04e5d1c1-54b8-3033-a3ee-eb6a065a3bc4 | -2.18737 | -53.72178 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c4770da-309e-3572-8c6d-08792c1cc990 | -2.18574 | -53.73233 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99a0b41b-d5aa-3dea-be2e-a3d01395db3d | -2.1852 | -53.73584 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc498cd3-c7d5-3f40-a6af-77f08fdb6b32 | -2.18466 | -53.73934 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 408c2665-27ce-317f-850e-8181b0164248 | -2.18349 | -53.72478 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55cfb277-cc50-3e1d-94f3-af77b4b6d5f9 | -2.18295 | -53.7283 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff6bd3b2-6daa-3498-9a83-01d5b7afadf2 | -1.9605 | -54.04429 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f31925d8-99fd-3c88-84ee-dddda59f69a2 | -1.95996 | -54.04777 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa27440f-f5ae-33d6-b12b-6215746a5bc1 | -1.81618 | -53.70413 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff802bce-93d5-3ef7-bb38-1b68b0e8fa2f | -1.7145 | -53.74591 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58485d23-b7bf-3c72-b49e-df5ad0a13300 | -1.49705 | -53.56886 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e82caca3-5a3a-302c-a526-81e4af8ce77e | -1.48085 | -53.54123 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README79.md)
