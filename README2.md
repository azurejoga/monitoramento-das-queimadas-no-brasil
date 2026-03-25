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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d43fc62d-70c3-3414-8b83-0a72223f63c1 | 1.94351 | -60.90935 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 145.8 |
| d9a2db8a-cb6b-3594-a389-ab16fe6fdfb4 | 0.75569 | -60.23476 | 2026-03-25 01:05:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 28.4 |
| c2dcaa5a-d959-3324-b9f8-1ac17f3dec59 | 1.92891 | -60.27449 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 956b5379-6ae7-3278-add2-d0ecbd9423f7 | 1.92761 | -60.28403 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 274b49a2-f04e-3ebd-ada3-8b2c245f1ce8 | 0.74529 | -60.24287 | 2026-03-25 01:05:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac7387a7-fd34-3f62-bdec-20fd39334390 | 2.72918 | -61.35853 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 29c76fb4-c7d8-3abc-85be-a5af1ab8edb3 | 0.7731 | -59.57917 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7e8d408d-694f-3357-b1bd-9933ec095eed | 2.32647 | -60.40285 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3827736d-876f-3725-929f-5b91bb2dd730 | 0.80566 | -59.34507 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 35.0 |
| c1ec9b63-3e2c-3f1a-91cf-28de1217123f | 0.82814 | -59.91439 | 2026-03-25 01:05:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 29e65057-6bac-367f-b445-88620b009295 | 1.81723 | -60.35019 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a0514c82-9ade-3b5f-85ae-7322d5ea354d | 1.83193 | -60.85031 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9e07d710-dcb3-394d-ba00-99d7998abae0 | 0.7544 | -60.24413 | 2026-03-25 01:05:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f0f7163c-86c2-386b-a850-b7943f7a1834 | 0.81374 | -59.35673 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 9c2a79a6-c672-3e9d-9b0d-56ded5af63ec | 0.67044 | -59.51786 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a9a51c9-56f4-3a58-9168-093a64aaa9e6 | 0.7745 | -59.56911 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2b6d40f-3c65-3987-a674-a4b6b4c36264 | 0.82716 | -59.36484 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 81cbceab-f8ab-30fa-b449-b9e917921dac | 3.92835 | -61.2826 | 2026-03-25 01:05:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e2e39527-72df-3675-a761-25c7dd5844b5 | 1.94226 | -60.91845 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fb0184c7-3d50-315f-ae54-3f9d232e249f | 0.80423 | -59.35538 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ceac2b20-16e7-3cb9-ade8-303aee443d6e | 2.95925 | -61.29931 | 2026-03-25 01:05:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5420c489-b70e-30c1-bb02-b79e87e929a7 | 2.17012 | -61.53419 | 2026-03-25 01:05:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63e6bfff-1334-3dec-bbe3-f8938cc38037 | 1.2152 | -60.3768 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b0d0216d-704a-38b5-a61b-86ffa7315ed1 | 2.03622 | -61.10337 | 2026-03-25 01:05:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 49858aa0-f453-3786-b7d2-e2c49255c235 | 0.82679 | -59.92409 | 2026-03-25 01:05:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2d54dcc-8107-3221-8c89-4878c6da2002 | 2.71138 | -61.35604 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| cc244613-69e9-3cde-b3cb-2d7800a70629 | 2.70371 | -61.34583 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 74c0eb29-2a12-3502-8a2c-20eb1fc2d271 | 2.38864 | -60.95512 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8f17a877-56c6-32cb-b178-273174a923c5 | 0.74658 | -60.2335 | 2026-03-25 01:05:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60caf7c6-e64a-3bbe-8938-3ba3addbd44a | 0.66905 | -59.52795 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a68a40bf-ae32-37c7-a1ac-88500a3af8ad | 2.37966 | -60.95388 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47972e36-9043-343c-837a-775f19e9f844 | 2.56102 | -60.90733 | 2026-03-25 01:05:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2ae2fe20-0f92-3d3d-8bd3-1a78f04e2361 | 0.81519 | -59.34641 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 9dcc1de3-fc5f-36ed-bd2c-ef26406f6ad6 | 1.95248 | -60.91059 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e89b2062-66a4-3472-bddd-43c1780c9dc7 | 1.91973 | -60.27317 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1f4e234e-36d9-3cae-8a2d-a9714d2629fa | 2.66112 | -61.3158 | 2026-03-25 01:05:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0f82b96a-08e0-32db-a4cc-a1f614799ca9 | 1.95372 | -60.9015 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 885f4a75-072b-306c-b91a-899f904696ff | 1.7578 | -60.58409 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18ca1c22-9d61-3bcd-861e-0013a8f3e988 | 0.82856 | -59.35451 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9f3c5fa2-c77f-355f-991c-001af6dcc55f | 0.82326 | -59.35805 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bf2144c3-a237-3d60-a8f5-695f69eeb8df | 1.76715 | -60.58226 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e02fc545-e184-3e5b-800e-3af772d02dcd | 0.94526 | -60.33071 | 2026-03-25 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 1204c72a-653a-3529-b32d-d28481502d18 | 0.82577 | -59.37514 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 47f634e4-1a6d-3b79-8a34-c0243ba2bdd6 | 0.73941 | -59.61524 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0efe65f7-a7a7-3257-a2cb-ba53c65fa9f5 | 0.98465 | -59.38237 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a967aa00-aaa9-3cdb-bfac-d23ec64c4423 | 3.84519 | -61.28323 | 2026-03-25 01:05:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9253c326-42b0-3822-a1d4-527700fd3cf7 | 2.32779 | -60.3933 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bd9d0a59-e5e7-338d-8f8d-2197b749de4b | 1.91843 | -60.28273 | 2026-03-25 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bdc0c009-555e-382c-b50c-72e971d226c3 | 0.8123 | -59.36703 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 146.4 |
| f9432464-157d-352f-b35e-41f0e7558f5d | 3.83622 | -61.28197 | 2026-03-25 01:05:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ae6aaee-afbd-3236-b746-4cbd82d6b8f7 | 0.77725 | -60.5463 | 2026-03-25 01:05:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 49c0c001-143b-3fed-b4ed-da99b7953c63 | 1.75909 | -60.57481 | 2026-03-25 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 5d1d122d-f49c-3771-bcde-5a1841205770 | 0.82182 | -59.36835 | 2026-03-25 01:05:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 67949da0-6f5b-3ced-81b8-a56bdc76d1ce | 3.8389 | -61.2816 | 2026-03-25 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 38cb10ed-7a55-369b-b103-acc26352e5fa | 0.8301 | -59.3628 | 2026-03-25 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 2352ef64-3fcb-38fb-9b00-f8808bae987d | 0.7936 | -59.363 | 2026-03-25 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 881d3b82-6c47-3def-bb82-b17d64eee37a | 1.9238 | -60.2879 | 2026-03-25 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9d08dd38-a769-3177-9b87-ab176dbca6cd | 0.8119 | -59.3438 | 2026-03-25 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 95022df6-b886-39c7-8db0-c369bdaeb874 | 1.9593 | -60.913 | 2026-03-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a9c64e63-08a2-3dd8-b0c6-8c141e3d53e4 | 0.8301 | -59.3437 | 2026-03-25 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 2738a265-7d91-33e6-994b-0a95c1e764e1 | 0.8119 | -59.3629 | 2026-03-25 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 212.7 |
| 6210f02a-dced-3c03-bded-d0efbb187e70 | 3.8572 | -61.2813 | 2026-03-25 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 765c94c6-b69f-3257-8ace-63f359672913 | 1.9411 | -60.9132 | 2026-03-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 1adb6146-77e8-340c-857f-463461b91b8a | 0.8119 | -59.382 | 2026-03-25 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c8767413-c611-3871-8096-244f6cc98bab | 1.9238 | -60.2689 | 2026-03-25 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 59c5fe00-1a22-3633-9051-f16b82a114dc | 0.8301 | -59.3628 | 2026-03-25 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 1656fe9b-da61-378f-8f49-0dde6694dd15 | 0.8119 | -59.382 | 2026-03-25 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 61fa88df-20b2-3e69-aa6f-cd2a390b3c43 | 2.7247 | -61.3571 | 2026-03-25 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 91f1959b-fc0d-356a-9863-ee81bdf946a6 | 0.8301 | -59.3437 | 2026-03-25 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 44c602a1-473d-35b1-8107-0ce5198d7f46 | 0.8119 | -59.3629 | 2026-03-25 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 207.9 |
| 1cf01c34-69ba-304a-abc3-56adfd1fcd36 | 1.9411 | -60.8943 | 2026-03-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fc9b1084-139c-3d85-860e-9fec0e7cffc1 | 0.7936 | -59.363 | 2026-03-25 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 352d828b-b5c0-377a-bba6-6d4f5f062eb4 | 0.7566 | -60.2396 | 2026-03-25 01:20:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c808bd89-de7b-3a43-9410-2b28cc882dd4 | 1.9411 | -60.9132 | 2026-03-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.5 |
| a76ec709-48d2-3cc9-afe0-883530f34650 | 1.9593 | -60.913 | 2026-03-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ac17e0b1-3508-38fe-b9df-25aa6c9a58df | 0.8119 | -59.3438 | 2026-03-25 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 8b9642a4-d14f-3a55-8967-73a3e4e3a3ca | 0.8301 | -59.3628 | 2026-03-25 01:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 2806f565-c30d-33fe-b4c1-6cee614af466 | 1.9411 | -60.8943 | 2026-03-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 687cdd14-d0a3-3785-b4a2-56588d40afc4 | 0.8119 | -59.3629 | 2026-03-25 01:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 224.0 |
| 7d5ab78b-d032-3242-9919-f4917f950313 | 2.7247 | -61.3571 | 2026-03-25 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f79b9b8b-2ca4-3cf6-a9f6-6b5892f3b03f | 2.032 | -61.1013 | 2026-03-25 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 99642848-251b-354d-9750-a8e055231323 | 0.8301 | -59.3437 | 2026-03-25 01:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b45ea634-69b3-34dc-bdf3-51eda5bf6204 | 1.9411 | -60.9132 | 2026-03-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 94cb2930-5f98-3f49-85f8-dfa9d2f41ab6 | 1.9238 | -60.2879 | 2026-03-25 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a64055d9-dbbe-3a2a-bc2e-a715e2dcf2ad | 1.9593 | -60.913 | 2026-03-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0bc20fc0-c5aa-3cf6-bd20-6383cb2ee4b0 | 0.8119 | -59.3438 | 2026-03-25 01:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 6c0e56b7-22e6-3dda-a774-d8ffc4fe4b97 | 0.8119 | -59.382 | 2026-03-25 01:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 24ee8443-7591-33f9-90d0-758b6884c915 | 2.7065 | -61.3573 | 2026-03-25 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 80.7 |
| e8e507f0-3fe5-3625-90e9-281a5f272a82 | 3.8572 | -61.2813 | 2026-03-25 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 760076fa-03f9-336e-9d1e-a2089aa2d9f9 | 0.8119 | -59.3438 | 2026-03-25 01:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 3c260dc9-8959-3200-ab20-181b7ed43b0b | 0.8119 | -59.3629 | 2026-03-25 01:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 232.3 |
| 8cc235f1-71a8-3f7f-bdf3-21f40783ddb3 | 2.7247 | -61.3571 | 2026-03-25 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ab10dfb7-728c-3a9a-979c-2d4a146ba577 | 1.9238 | -60.2879 | 2026-03-25 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 65937a60-25ec-3243-97ef-82ba348ae88c | 1.9411 | -60.9132 | 2026-03-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9a54333f-35e5-3034-bdfc-3b14037a4256 | 2.032 | -61.1013 | 2026-03-25 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 240399a3-a10b-391b-9d00-d851713a3134 | 3.8571 | -61.3002 | 2026-03-25 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| bf032b67-0bc0-3e39-bc71-64cb95356e21 | 0.8301 | -59.3437 | 2026-03-25 01:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 97084014-8cc5-3a92-9594-ea23b47ea768 | 3.8389 | -61.2816 | 2026-03-25 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c77a53d1-0027-318c-a400-565561bb6db8 | 3.8388 | -61.3005 | 2026-03-25 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d0e5ed79-9b63-381e-afe1-6d11fb3de7a2 | 0.8119 | -59.382 | 2026-03-25 01:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |


[Clique aqui para ver as próximas entradas](README3.md)
