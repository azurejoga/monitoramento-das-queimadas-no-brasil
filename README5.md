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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cf09608-54a9-3c84-b579-8dd2e273407a | 1.50505 | -59.91092 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d7e9b82a-548c-37d9-b9d3-a32b6ed52f28 | 1.45556 | -60.0743 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90b9db58-555a-314f-847a-a7130ca75d0f | 4.0641 | -59.89705 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7b713f9-8eca-36e3-9ca8-2d8649108c77 | 2.85944 | -60.81608 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e464921e-bfb1-30ee-bff6-deb831ead7ab | 1.09672 | -60.17951 | 2026-03-02 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb237697-74e3-3d9b-b6a6-93c93f3d03d7 | 4.37613 | -60.62214 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00e68f4e-4993-34eb-abd5-08df3fe6f99f | 1.47593 | -59.9251 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41021521-2e11-3fc2-b3ae-dbc8a13c9bb4 | 1.50654 | -59.92045 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1b8121e4-a0b0-3dd5-8da2-8b40abd61c83 | 3.04277 | -60.67155 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0238a4d-85ff-3a8b-a3ff-0191a5b67998 | 2.85138 | -60.83606 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| febe9202-cea3-3c18-aa8d-0e569bc20100 | 1.09983 | -60.17411 | 2026-03-02 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 624ba3dc-2f44-366e-bc49-e44ba761edeb | 1.48978 | -59.91343 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a513db35-fc34-3cc9-a62a-b91b2ba783de | 0.19249 | -60.44512 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 438e4667-fbc5-3061-9486-58f01054020c | 2.86166 | -60.83106 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4dfc4cd-a529-316e-9820-5b8a2c04f8ee | 1.54973 | -61.02387 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 600f5a0b-2819-3ca4-9a22-a1295aaf9779 | 0.09398 | -60.6343 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ffa98c-554a-3ee1-8733-80321d7b2dac | 1.11334 | -59.20618 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2be86b90-cbae-3a02-8cbb-b5d5a56a826a | 3.05888 | -60.67226 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0833ebb7-676b-380f-b16f-98fd10064519 | 0.89252 | -59.79095 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3e9db9d-8906-3607-bf6c-6a3dded7ea35 | 0.65141 | -60.31286 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7dfe1b3-d99b-3d57-945f-91e5567cf4af | 1.11933 | -59.19653 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bce96f3-1828-334b-ab5a-845541b330b4 | 1.07199 | -59.25477 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0dba7e4-7523-32e0-9f50-213a6dd14cfd | 0.49323 | -60.51263 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a2d0ef4-0e59-36ab-818c-cfdc2e9c80d5 | 2.85255 | -60.84356 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6eaa99fe-a8dc-3555-b1c3-3cde138f36fc | 1.48048 | -59.92915 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ec2d75a-fc63-3a8a-911a-c36a319b9118 | 0.30946 | -60.4922 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd369cc-97d5-3b9e-b36f-c35f17fb90d0 | 1.48669 | -59.91871 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b76e4f1-4057-3f45-a360-fc241a2dd04f | 0.09005 | -60.63491 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 185a1c15-c565-3959-a692-dd4d3f908767 | 4.36779 | -60.62349 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c99bec8b-e523-3176-92fa-819a2a0a28ac | 0.30536 | -60.44581 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c1d4040-f527-3129-966d-88a0b3b6b801 | 1.50579 | -59.91568 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 006e3771-0982-30db-928f-e079cdd27cba | 0.3105 | -60.44677 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36e25ca2-aff3-3d04-818a-c6f8063978ff | 1.11633 | -59.20137 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95c77726-312e-35d8-b2bb-a563637826e1 | 2.22478 | -60.74953 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9659a1b0-dc57-3f04-8386-501ef57febeb | 4.59946 | -60.75692 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccacba8e-0653-36e1-ad4f-62c3d375bf13 | 1.50877 | -59.9347 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31cbe885-63f6-3ff9-bbf5-3baa28266d28 | 3.02804 | -60.68501 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b469e17a-2f2a-3ada-a069-5d7445260fdd | 3.16713 | -60.69268 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ca09a6-344c-353e-8633-052e65358e2a | 1.50802 | -59.92987 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8c198be-5ee3-32bd-b578-b06a033513e5 | 3.166 | -60.69312 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 153018ae-b118-3246-9ecd-069acc5557f1 | 3.42387 | -60.82906 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50443ef3-4c79-3cfc-96f2-c853aacdda85 | 0.91824 | -60.53036 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6e6f10a-e251-3a8e-b755-f7fc8a28730d | 4.256 | -59.89297 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2d1c74e-ceba-3d1b-b085-b02d0882422a | 4.50688 | -60.54457 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ec86266-f316-3e09-acc2-4ed2a44cee00 | 1.02191 | -59.79994 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 946d8559-9c53-3cd4-8099-01bbe16a15d6 | 1.45483 | -60.06953 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3b9139e7-6ec4-3680-a52d-43b21f73e3a9 | 2.85889 | -60.81236 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df7521d3-dfc6-3354-a181-410ec32dc3bb | 3.60553 | -61.66006 | 2026-03-02 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d885248a-14b4-3324-b51b-1807afc923dc | 4.25698 | -59.8996 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de1aa49b-2d49-3e87-a851-670946f5936d | 3.17058 | -60.68778 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2966acd-c5ae-3c9a-84d4-c6b3cc0a446e | 1.11998 | -59.20081 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58fc02b4-85c1-3c20-96be-276a889c7f2d | 1.83104 | -60.84643 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc7be45f-6591-3c2b-b13c-f21a94b4d0ee | 3.60996 | -61.65941 | 2026-03-02 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 80784c98-a965-3b4c-a278-f6e295afb86d | 3.0174 | -60.6979 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0d0dab80-49ca-39f2-8e58-d28f45916d85 | 2.85966 | -60.83484 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c77e9d3b-8acb-3c17-9d6f-96d3d732cd41 | 3.57906 | -60.33168 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8ee0ad1-0a83-38aa-b586-ac0bbc5d423e | 1.16463 | -60.66669 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb758431-d91f-36bf-8b51-1bf020bbe4ad | 3.41496 | -60.82649 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 252fff1b-2708-3361-9e77-383b0bac76d1 | 1.49653 | -59.93163 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 840fa848-3c71-3cb4-bc01-1ded8bcbddf5 | 4.50634 | -60.54097 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e103a8f1-076c-3b0b-846d-44af7de16b70 | 0.7109 | -59.51452 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b5686a0-8978-3752-af53-e62536262dec | 1.8583 | -60.39746 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 25.0 |
| ca69a870-0f0a-3762-a184-5f0b5c3a641a | 2.86221 | -60.8348 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c847e46f-62e0-3317-9495-5b4336b95d81 | 1.4989 | -59.92169 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baa11891-88f6-39a1-853f-77390bbcca64 | 1.51111 | -59.92459 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dee70829-91f2-392e-bc2d-ba62e5de8aa8 | 3.46454 | -60.2908 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cea8f299-978e-3e00-bd75-b6cb02ef62aa | 1.45241 | -60.0672 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 576320a8-3190-35f2-911e-2c7b322b9eea | 4.08299 | -59.88811 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 596fe430-2088-399d-b4f3-17e7913a523e | 4.3714 | -60.61904 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4ce82ac2-c733-3a07-a7ba-e58b61b749db | 3.98875 | -60.0906 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87317b5-b1b2-3882-914c-db302ec7a65f | 2.86055 | -60.82356 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23549940-1215-3d6d-acfe-2d074f075509 | 3.4197 | -60.82969 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c243200a-e61f-3441-8561-6106b48ae345 | 1.4958 | -59.92693 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 590cdb40-194c-3dac-bf42-886d2083d590 | 1.02465 | -60.54304 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d6311ac-1c0c-3f45-bfaf-52ed154134c5 | 1.49508 | -59.92228 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b109ca1-8100-3426-a4c4-be26dfd4826a | 0.85426 | -60.40191 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d4c62d8-571f-39fb-8e89-2c933459c0e8 | 3.19084 | -60.69031 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2489eb1-3adc-3cc3-a8db-f6e00eb98960 | 0.05718 | -60.98358 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a566caa8-1bf8-33f6-93d9-721a3ea68a49 | 3.05977 | -60.6728 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 048a8757-3988-32b3-8ce6-1a256d75a6a3 | 1.72226 | -60.29585 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3065481e-9d4d-3215-9a1f-06eb3276ce2d | 1.07931 | -59.25364 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2714ba34-f3e0-3606-8032-c1cd0c4e4560 | 1.48742 | -59.92339 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646d500a-8da7-3496-9e66-a278064ba694 | 1.50049 | -59.90681 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 35630ecc-ec5f-3781-ada3-1afa5e71f968 | 3.99881 | -60.07584 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a475fe4-f264-380f-b56a-61ca6f84ae43 | 3.02393 | -60.68562 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf55a86e-cfd6-3752-bb4b-7d31cacd7a2c | 3.42026 | -60.83349 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0eee26a9-74c8-3a1f-acc6-fd65899612bc | 0.3178 | -60.44892 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02781168-a726-3ce3-ab0e-aa5fe96e8b16 | 1.48887 | -59.93274 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1ebfede-a1c6-33e1-a2e0-908f000a2a4d | 4.25502 | -59.9138 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf9a004f-88fd-3f7f-9774-15ca383df95b | 1.73024 | -60.55103 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac89d054-1cf1-377a-8cea-ec254adbc9f2 | 3.60618 | -61.66437 | 2026-03-02 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c3fdd49d-5d8b-3dd9-9e65-039f22666564 | 1.47975 | -59.92447 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dac260db-df5e-3f0e-bd0f-01de26076111 | 0.30924 | -60.44522 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d2114f-2650-3a38-b6c9-4ef1fbc2701d | 1.49285 | -59.90803 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c50f4e41-f94d-3c22-9a94-648359e46920 | 3.41191 | -60.8347 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2784bc52-f583-3029-b671-c2a8720ab17b | 3.05098 | -60.67034 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3e07950-96ac-3be9-8fdc-53e649bb3825 | 4.3792 | -60.61407 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 811a4940-a9cb-30d6-a481-fbd86e4310b5 | 3.45987 | -60.78495 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c47045ba-87bd-36ae-afa8-1a3cd134e698 | 0.09239 | -60.62433 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3509211e-1a99-37d3-afc5-3becfdb05443 | 3.16995 | -59.90695 | 2026-03-02 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README6.md)
