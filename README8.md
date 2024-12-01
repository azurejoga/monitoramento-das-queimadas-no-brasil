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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9270543-6087-3691-8577-0f1bd4e57aec | -3.6846 | -51.8209 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0bf212-a587-3b48-8d92-79644ce30803 | -3.2769 | -53.342098 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b131e71-9bd4-3f62-a588-d2eb22c33e6e | -2.6192 | -54.203602 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df4d50a2-f84e-328c-9861-0e461c9ff3b1 | -3.1215 | -54.5233 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2dccf1-9421-3fd5-85ce-be077fdd65f8 | -3.3729 | -51.533901 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb04e20a-2fa7-3ee3-ac27-9cc2399c4d98 | -2.1088 | -46.234001 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0106735f-15e7-309d-91f1-86e9dac309de | -3.2464 | -53.617802 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee4a06d-6963-38f2-8153-b620137d100c | -2.3737 | -50.3983 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186cca93-b270-3f98-adf2-a657806cd030 | -6.7583 | -46.528999 | 2024-12-01 00:34:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b432c9bb-6794-3cd4-8838-bed8300f71f7 | -2.6464 | -51.869598 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f87314-93f7-3113-ad21-fa92e87f746b | -3.4917 | -53.796902 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7351217-9a78-3fc8-b61e-608941142b93 | -6.2837 | -43.836201 | 2024-12-01 00:34:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 401d9202-022e-3e61-ab69-274d9dc967ba | -2.6342 | -54.2248 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9c99d26-10bd-300b-a749-7b2c9901fbd9 | -3.7436 | -52.265499 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acbe2f2b-4613-3f07-822f-c5d5066f83bc | -3.0345 | -51.539001 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f178686a-dd88-3a27-8a97-5078142fe161 | -3.0672 | -50.321499 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d803b41-dd3f-3469-885f-e6a6589fcc6c | -3.8239 | -52.257599 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb494f0-36e8-351c-bc39-1bdc4ccede9d | -3.0917 | -54.299 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3f9182-a597-37a4-b17e-b295a65ef00f | -4.8775 | -41.316799 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bdeec325-1e7f-3154-a7fb-329986d4a4d4 | -7.0267 | -44.842098 | 2024-12-01 00:34:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| deeb3a28-678a-301a-947a-2f85ef1606f4 | -3.2161 | -53.117802 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed1c1f2-3960-335d-8506-9792df0ab1be | -2.6846 | -51.720299 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88089694-e972-3fc5-8efd-292598dcb89e | -2.7592 | -51.686401 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aaba0ab-7590-3271-a3c8-bdc40cc2e7f7 | -2.1129 | -46.563999 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c60b2a-654f-31eb-abc9-60f1f395eafc | -2.6057 | -54.2803 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92081903-eb48-3b73-843b-4331a714114d | -3.3135 | -53.8713 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f44c16e4-f501-3fce-bd27-2458fd537b5c | -2.5992 | -46.570499 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f25bc7-cfe6-3b3e-b743-10f660458db4 | -2.1134 | -50.341702 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c0a6da-f577-3ef7-85b6-0b107986f519 | -6.2879 | -43.854 | 2024-12-01 00:34:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce1728a7-0507-33d9-b907-d43b6a0d1947 | -3.6925 | -51.810101 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 449e5119-c5de-329b-8814-5d20a1cecb3d | -4.55 | -45.7285 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebcef16-7113-3cd3-8a44-29e37e0b8a7e | -2.1203 | -46.239399 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e7ac633-68b9-321b-8339-69549812b85a | -5.7305 | -43.9841 | 2024-12-01 00:34:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bde638e-6833-39f5-8d31-832c3dbe7e06 | -2.8103 | -53.049099 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8cf686-a646-36ca-b3fa-115106027a38 | -2.1221 | -46.247002 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3224040d-2f71-35ae-939d-acd2a8f0db7a | -2.6417 | -49.901299 | 2024-12-01 00:34:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ccc4df-cb01-3394-bd41-6dc7a6793d22 | -5.7283 | -43.975101 | 2024-12-01 00:34:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5d47035-ee3b-3342-9e0e-0bffc8c08a48 | -10.6629 | -44.493401 | 2024-12-01 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| def77e0d-7ee8-3734-a3aa-bf16a8a60881 | -2.8444 | -49.886002 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24147f8b-0561-3cdc-be9b-ad73b3fe4801 | -2.9302 | -51.442001 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8921efe6-4de5-37f7-8abf-db9cc379f08f | -3.294 | -47.032902 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f774b732-6bfc-39e2-8be1-255138aa8884 | -2.568 | -51.886902 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f3facd0-c07a-3bc1-a8d2-25e7e7bbda8f | -3.156 | -50.6217 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d8140b7-5e5a-3ae4-a695-6d77179f2ee4 | -3.4663 | -50.264 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c763ba50-b6d0-30b7-9737-71332ec3a719 | -2.473 | -46.560398 | 2024-12-01 00:34:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd28b25b-a395-3b41-96ad-1ba5e52ae8f9 | -2.1095 | -46.549301 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9ea512d-8c20-3535-b740-b2af86a22d92 | -2.636 | -46.194698 | 2024-12-01 00:34:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f304b0f4-8857-3adc-a8d5-7f8ffd51f64f | -1.7089 | -46.154999 | 2024-12-01 00:34:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 976a9591-0729-347c-ac0d-75c4e15f4be1 | -6.9144 | -43.535702 | 2024-12-01 00:34:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c90a527-f234-33aa-9d25-56ce71076e13 | -3.4679 | -50.2714 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef43aab-089c-3e61-908c-7b6e9e4778e9 | -3.1105 | -49.516201 | 2024-12-01 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd8445c5-5796-35f8-a4e2-9bf0bcd5d34d | -3.3004 | -50.033001 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b212b32-15f6-355c-92c9-ddcb22acf51c | -3.4359 | -52.040501 | 2024-12-01 00:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f8c3d6-ebf4-3ece-a176-e3403a0c4178 | -1.9661 | -46.464199 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3b244c7-cca7-30d3-a882-d013e8640434 | -2.6516 | -46.5741 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a035e54e-6845-3c3e-adaa-2796d44acf4b | -4.2625 | -47.609501 | 2024-12-01 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dad5048-0cec-393e-ad83-3fa42d1ff25e | -2.7536 | -51.661499 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d077fdf-812f-3272-848d-946a8c1dfc76 | -2.0173 | -46.507599 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81e42a79-f433-33e5-96d2-e7eadbb6a5a2 | -2.1105 | -46.2416 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7874dfaa-9d39-32df-a0e0-962ae0ce8cae | -2.5661 | -51.878399 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58809375-a134-3fc2-b118-ce6dc69b6a18 | -5.6122 | -45.061298 | 2024-12-01 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5ceb437-5231-377a-a228-0ea1d44cab4c | -3.8864 | -45.006001 | 2024-12-01 00:34:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7d18118-3904-317f-a31c-646069c05d6f | -2.0978 | -47.6175 | 2024-12-01 00:34:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff6fe89-e880-30d4-8a10-5dd2c911c113 | -1.9653 | -48.4324 | 2024-12-01 00:34:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68d4197-d906-3373-b3b7-6c1ad90fde44 | -3.204 | -53.109798 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9a94a41-27b7-3d93-a7e1-8b9c9180c575 | -2.629 | -54.2015 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8dda405-6592-3ab8-9967-afc37473d78b | -2.1244 | -46.569199 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3459ed-99fb-3617-beb8-b2e94d99c70c | -3.8198 | -52.239201 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f521d39-f263-3a6a-aebc-e9b02327c11e | -3.6986 | -51.061901 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4eaf26-a56d-3f7a-8e52-256a1144734c | -3.6614 | -51.7178 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea1b57ce-f3dc-34b3-a1a1-24bf92cfff03 | -3.0092 | -45.1362 | 2024-12-01 00:34:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66f78e21-535a-320d-a897-d2426d7fb9cf | -2.3125 | -53.845001 | 2024-12-01 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c181c261-874a-3c7b-b14e-600a17be782d | -3.6905 | -51.801498 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8ac781-3243-3769-9b6e-c1568c356382 | -2.0156 | -46.500099 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982958fc-7b4a-388e-9ce6-0c132178e5fa | -1.8187 | -50.902 | 2024-12-01 00:34:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 391d53e4-65a5-3283-a731-5d6397dc80e2 | -3.3153 | -50.143799 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a9a62d-a71f-325d-86c8-283a0940fa1f | -3.72 | -51.065601 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34454b07-f451-3473-8d51-2a5ebb535dda | -1.7054 | -46.139599 | 2024-12-01 00:34:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce4b5c19-7c5f-3501-a499-5e7874d71289 | -3.5929 | -50.368099 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea7352e8-8603-3c64-8fc3-5e7592a3488d | -2.7246 | -49.361198 | 2024-12-01 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76f6c8f-44bd-3792-a6a2-469722134283 | -1.5183 | -45.909901 | 2024-12-01 00:34:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c17252f-0a57-3177-b588-7cf4015ee631 | -6.7113 | -47.2668 | 2024-12-01 00:34:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b204f8e-4e5f-3c52-8330-a8d48cb2eb1a | -2.5778 | -51.884701 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30513142-3b61-3833-b75a-1eef5d86fea9 | -3.0327 | -51.5308 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d36b3b96-43e4-3727-8649-920800172a32 | -3.0866 | -45.513302 | 2024-12-01 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6aab8cc2-f1de-3ddb-b2d4-9f86cb7cb84f | -2.8005 | -53.051201 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62cc38d6-9d2d-320a-9737-0a8012684162 | -2.7138 | -46.129398 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35107d5f-cfaa-3ddf-b208-5ae309a3a691 | -2.8056 | -54.0298 | 2024-12-01 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6d943a-c91e-3dbc-b1e5-10d3a3ab5c40 | -3.7534 | -52.263401 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e7c68b-04c9-3a74-a436-a3326fcae933 | -3.4005 | -53.024601 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b914ede-9421-3f64-adc4-c36715c9e0f6 | -3.4169 | -50.182598 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e9b3a7-8b54-36d4-aec8-d14e3f509ae3 | -4.1756 | -48.626099 | 2024-12-01 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 047c056f-1148-3531-a2dd-1c0bbf623d9f | -3.0487 | -51.056198 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce22a979-c3fe-3985-8370-0504e4b5ca5b | -3.0732 | -53.805801 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0205c8af-579b-38f1-8089-3226ee4ac0d4 | -1.5628 | -46.7729 | 2024-12-01 00:34:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b854d1-6a97-376d-9491-dfe48af4f063 | -6.9242 | -43.533401 | 2024-12-01 00:34:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b2c13a3-593a-3d46-bb48-3881b566f14d | -2.6543 | -51.859001 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7456c289-2d00-3f1a-b3fa-641641450814 | -1.4467 | -47.119202 | 2024-12-01 00:34:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8181976d-146e-355e-8873-cdc3f92dad0f | -3.2612 | -50.041698 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4acf9a3-5316-37fd-9bef-562016acc403 | -3.2645 | -50.056099 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
