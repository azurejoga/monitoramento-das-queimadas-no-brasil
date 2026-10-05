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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55f06c87-dfe7-33a0-b210-82954443edb6 | -3.0471 | -54.21422 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b13f4cd3-145a-3830-aaec-90e3b3f7f04a | -3.46621 | -54.59682 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ea1be0ee-2885-362a-a8d6-2b3b358b50b8 | -2.82856 | -54.11671 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e88ad7-5c30-3fd6-ac5c-ea7a93d3a9c1 | -3.12388 | -53.70393 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b260f7ae-3b8b-3f26-806c-de7a94092961 | -3.98652 | -55.81727 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35ace996-d6c1-34d5-beed-f6cb5645aeeb | -2.81889 | -54.10938 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6967e1a-0289-3e68-9ecd-2608a087a91e | -1.61697 | -55.1099 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d7aae54-de7f-3700-b254-f0be1f7ba87b | -3.88337 | -55.81472 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42d275c9-ae77-31a0-852f-8b6199535f72 | -3.10977 | -53.72612 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a4b8d57c-cf09-333a-b9a8-bb6f6eaf0259 | -3.37747 | -54.11027 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cff1a84-fbb4-3378-a6e9-5daee8db4f11 | -3.07548 | -54.17732 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 49e4f209-0794-3640-8d0c-d5706ecc8b72 | -1.98732 | -54.41967 | 2026-10-05 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 834cf338-a5d7-3bdc-85c4-46835bd00932 | -3.97913 | -59.34325 | 2026-10-05 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff39145c-8968-34dd-86e7-227a4aa6d67e | -3.65483 | -55.31747 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb9cc77f-b505-36b0-b920-3dc120c19bba | -2.90081 | -54.1153 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae2a2e96-6d22-369c-bb1d-fd5a7daabd53 | -3.46978 | -59.54146 | 2026-10-05 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bb80eb7-213c-3bba-8924-48e3dba75584 | -3.10783 | -53.73978 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5e82f49b-6c93-3195-96f9-27d891032e5f | -2.95097 | -59.16023 | 2026-10-05 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0791c78-ad73-303b-83e1-33b3f2c03389 | -3.11235 | -53.70798 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b29dc574-502f-3870-993c-73b46fbf01ba | -3.33296 | -53.3956 | 2026-10-05 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6da65ed2-4abf-38d1-8a08-04933fd8b9c1 | -6.25824 | -52.8471 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 85ee76e1-bb2c-3b43-88be-d87060ffde29 | -1.62016 | -55.14129 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62d4f5aa-f984-3c7d-9999-d8942fad27cc | -3.10913 | -53.73067 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93ecdb24-f2a5-357c-8106-ab3b74ba0780 | -3.10279 | -59.74026 | 2026-10-05 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5913751c-fa7c-375b-bbbb-88b58f38c80b | -2.85975 | -53.91713 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fbc8617-eac5-3fcf-a66f-647000502cc4 | -3.64934 | -55.31667 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 065e1a2c-eeab-3197-86a2-49212372ba0b | -6.21827 | -52.68324 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e0e8ecf6-f493-3903-ae49-8cff50b9283d | -3.61344 | -55.47626 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f3d47f0-6d87-37d4-80f3-6705f6190125 | -3.12509 | -53.70536 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 09e8f628-ee88-3195-b59d-062591c089be | -3.31114 | -53.85396 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f78dad39-1c83-3d8c-90e6-704779bc6a1b | -3.57194 | -55.41871 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1632fdf-d673-3455-be84-6a2579bd17ee | -2.97935 | -54.10424 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68b41092-b168-3e6f-b854-b523274edf72 | -2.94748 | -54.2041 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e961f401-8266-3bf6-9b97-72cc54101e1e | -3.47198 | -54.59754 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 29db2063-a6c3-3112-b0d3-384b3d9c4a56 | -3.86987 | -55.80684 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9356a355-6b06-3f72-a26f-858d2f0551e1 | -3.05994 | -54.1688 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 174c2011-2477-3c0d-ac0a-ec81fe66a075 | -3.10372 | -53.7147 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9f22e2de-8572-3619-b273-4cb8f7cfa1dc | -2.89895 | -54.12794 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e2bd7dd-ed76-3bbc-a9f4-bf78ad9ef77a | -1.61396 | -55.10849 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65edbbd-6066-36d0-bdbb-5eade9b87e09 | -3.86108 | -55.82943 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0d48243-fb48-3d55-97db-140fce493004 | -3.59088 | -54.30981 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3647038d-61d7-3daf-b2a8-624793c2ea23 | -3.06122 | -54.16033 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec4fb26f-4470-3308-8ff4-01648d9384f8 | -2.82287 | -54.12291 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| decc57fa-ba52-3df0-a598-fac87f04c260 | -3.61428 | -54.60514 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b281a681-9425-358a-abc2-0d358505e535 | -2.94915 | -54.14695 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8ef65665-972d-38b5-bf9b-4810244ab62b | -2.81575 | -54.13039 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea95aeff-7251-3363-9219-db119c903793 | -3.12269 | -53.76529 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e7d53fa7-6b1b-3215-9cca-737865bc0ae2 | -3.11775 | -53.7135 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90215d32-806c-3d0b-b30c-932e159e5dd7 | -3.12184 | -53.72809 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e61c2da-d591-3f34-96ed-e34282f7fb35 | -3.10502 | -53.71609 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b91afc2c-cb0b-3f57-bb0d-48b6b1a60856 | -6.21324 | -52.82816 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a351f37-bc24-3543-a3f5-89304042aef0 | -2.94653 | -54.20682 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f248d49-9324-3e53-b5f2-ecf7a2f55df6 | -2.94042 | -54.12405 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8661ab62-17ef-36c4-9af4-0e397f8121f6 | -3.37676 | -54.10222 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b348890-237e-3c2e-a4cc-52c4fb74d097 | -3.05244 | -54.21251 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51518ed0-828f-32ae-8fef-bbe5e06ce9cc | -3.3045 | -53.85748 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6eb9316f-0e9f-37de-b8a7-0aadbe277018 | -3.1059 | -53.75338 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 23245838-09eb-3bb8-bbda-8fce7f68ec8e | -3.12048 | -53.72662 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac56d20d-76de-3b7b-aeba-9b1a10440bcc | -2.81763 | -54.11781 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03ac39a1-f009-3af6-bebb-25b8dd0d0623 | -3.30418 | -53.84497 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7288313-389a-37be-965f-f46b7a63f00e | -2.82209 | -54.12003 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97ca2e2c-75ff-39e0-a4a3-49e9e3afcd95 | -3.88433 | -55.80795 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7745adab-1278-3666-8f86-3520b5653ff4 | -3.13589 | -53.71633 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 47195943-2b52-3eb6-89c4-8bba342e3fa4 | -1.46894 | -54.53212 | 2026-10-05 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd7fa99a-2758-3e1a-8a1c-20cf51e0a018 | -3.11106 | -53.71707 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8ed47159-af9a-36be-81f0-06ad22a710ed | -3.50667 | -54.61092 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 742def86-1caf-361c-a4b3-1c66b4689de8 | -3.51486 | -54.62502 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49691e3d-1971-3cc2-9594-ab78639be2c0 | -3.11795 | -53.75529 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cf7903a3-3032-3199-a1b8-bfee829db131 | -3.10705 | -53.73378 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3242577-b45f-39fe-a42f-3e101d2c0c91 | -3.12724 | -53.73356 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15553f89-bffa-3daa-a56d-dab8cad45c7b | -2.95054 | -54.14427 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5ad2a520-825b-3e27-8e2a-b5c0f07a20a2 | -3.11905 | -53.7044 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d48faed1-5cda-398d-8f50-1a90d76147f8 | -3.05167 | -54.22354 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 51299ce8-ddf1-3cd4-9ff1-cee7dbd0e921 | -3.11451 | -53.73619 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11198c49-dafb-3b30-9591-222f5e77a9ce | -3.61347 | -54.60336 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8220b247-8d14-34c5-bc8a-f18ae5b97b77 | -3.1199 | -53.74168 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa89446f-ae46-3a70-9ab8-d1d5c2daca2f | -3.64883 | -55.32022 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9be186f-329a-3330-b79d-22ef27eccc34 | -3.50457 | -54.61532 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f20015-d2c1-31e8-9b9d-62c388442648 | -3.11193 | -53.75433 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3e5de73b-2fd7-3145-95cd-cc921a1521c3 | -3.38148 | -54.11159 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e36dbc-eef4-37e0-9c47-1c5101601d91 | -2.92746 | -54.13076 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 186c3c60-72d3-396b-8e27-2fd18cffadb2 | -3.30285 | -53.85394 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d95a973-8b01-3031-be3e-bebd8631a9c1 | -3.1198 | -53.73114 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cb18a28-ea06-36ea-9737-63f5332076e6 | -2.80927 | -54.13368 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03f7fa32-fec9-3634-97da-efc25f17d3dc | -3.51241 | -54.61182 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0befa268-7e50-3205-9d8e-41aa9fd10f24 | -3.96715 | -59.33749 | 2026-10-05 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ab040ce-c13a-3ae8-83b3-fc2df20fc974 | -3.07149 | -54.16339 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 49a99597-5ee7-32e4-b3b1-32c9920f30b3 | -2.81638 | -54.12621 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9cc3a8b-ffb1-39bb-ab0d-f878a902b223 | -2.94721 | -54.12654 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a052f79-c42b-3a9c-98e4-0405eb395028 | -3.12919 | -53.71995 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 258606d9-188d-3e19-b7f5-a40a4de1216e | -3.11572 | -53.75825 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c9e88e62-84ef-3363-9f31-6a968afaa47a | -2.98059 | -54.09568 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9268b8e7-ef82-3005-bb6e-25b319744c41 | -2.9283 | -54.13245 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 81eecedc-fcc7-3193-aaed-10e41f1c5f76 | -2.82735 | -54.12515 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7e3ebb0-6111-336e-bfed-0b2a9e5eee7f | -2.82162 | -54.13125 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bf60b57-6753-3e49-99e0-6e84c2b2a3cb | -1.61518 | -55.01384 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd8b82da-049a-3dbe-ac6a-99478ce4d394 | -3.12333 | -53.76078 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7af24c23-a6f6-34ea-9da2-e14272b17177 | -1.88625 | -56.28487 | 2026-10-05 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34a11b00-4fdd-3944-9631-4902847f2fb9 | -2.15549 | -59.22366 | 2026-10-05 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d2a323d-3305-35bc-bb09-fdcdab226e93 | -2.94129 | -54.20175 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README52.md)
