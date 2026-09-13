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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 794979e4-6d02-3a15-bbd5-33fb7d684b27 | -2.68078 | -57.54945 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7ddfe15d-6ef7-3128-8a9b-f88a31a286f4 | -3.16235 | -58.64369 | 2026-09-13 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d7e9e2b-827d-38ae-9da2-1987483919b5 | -2.53562 | -54.66202 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a9c8fd15-0eab-3e61-bcd0-a67775e7adea | -3.79027 | -48.93852 | 2026-09-13 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5a5339d-616b-3aa9-bd52-ed9eea322516 | -6.50096 | -43.92836 | 2026-09-13 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0486a813-8b99-3564-a08b-1760984a47cf | -3.22053 | -50.58823 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6e950ea-49f7-35f9-90f4-269d5fd7410e | -5.12199 | -55.96924 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b58561a-fa79-3518-84d7-83b630c952c5 | -3.64275 | -58.62442 | 2026-09-13 04:49:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2137c6c7-38cb-3b13-a666-8dc73ae01c49 | -6.07864 | -51.75583 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9784bcb6-1ae1-3f4e-8b0c-e665c12d02dc | -5.76421 | -45.09359 | 2026-09-13 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6dbfc970-800a-3e68-acff-22214a0f4607 | -7.14925 | -44.72022 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42f434f5-c536-37cb-bfca-950ab2d443b5 | -4.45762 | -50.16679 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50c575f9-2e25-361e-9ecb-040dfc52173f | -1.22937 | -54.12502 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac5b6d53-b05b-37ab-bd0a-e21657013634 | -7.14978 | -44.71667 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5458e599-56fd-3515-b741-13c3645b5b26 | -7.01394 | -44.62637 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b6f416d-a77d-372e-bd3a-ace025d86faa | 0.17631 | -51.48199 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29be859c-071c-3c94-a2bb-71a3dc8c38e3 | -4.35864 | -54.77761 | 2026-09-13 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bede1653-e107-335c-9f0c-449159040de2 | -4.39698 | -42.34028 | 2026-09-13 04:49:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36ee1435-d0eb-3749-a9f4-5ef5cbb48da1 | -3.33258 | -42.3015 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c2e73649-4b4c-32b4-a5c7-6495a3a9f0c4 | -7.1365 | -43.7544 | 2026-09-13 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5f09bcef-bdd8-320b-be35-469ce88baf57 | -3.40428 | -48.8959 | 2026-09-13 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a96f17d-c899-3791-9ad2-8adf9bf855e1 | -6.51109 | -47.60124 | 2026-09-13 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ae1fdd1-6681-37a1-902e-088987dec041 | -3.6389 | -58.62747 | 2026-09-13 04:49:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83ae2800-7ea3-370e-9716-9c713aceda28 | -2.82532 | -49.23716 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db92ee2-a77c-33da-ba23-c63299c83c7b | -7.15719 | -42.10194 | 2026-09-13 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ffdd4da4-0bec-3720-8fd7-8d09dd716067 | -5.89633 | -45.54594 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1350fc96-d633-3434-83e3-99886d7b3c13 | -5.88798 | -52.06321 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ae3f0e-8865-38b8-8d7d-27678640c733 | -1.22572 | -54.12043 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd2ca336-86e3-3cef-b288-0bac0118aecc | -6.8633 | -47.42203 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82d10465-194b-308c-80c2-a43e3d29215c | -4.00295 | -50.86927 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d999f40-d0a5-368b-a81c-f4036962a662 | -2.8292 | -49.23422 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3ed021a-7b2d-31b1-ac3b-e92b804b603a | -6.78857 | -48.65796 | 2026-09-13 04:49:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9acd087e-6852-3f56-a396-08027cea4c0c | -6.83115 | -43.51643 | 2026-09-13 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4960ab7d-a3e4-3c30-81ae-b4dacd54400a | -3.19646 | -51.01464 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a53c78-9f0b-3e0a-9081-1b8fcce5098f | -2.93817 | -50.38598 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 079746e7-264a-34df-bbec-b01bac175f70 | -5.81676 | -53.79673 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff260de8-9e6e-316d-977d-31bdc4402906 | -4.41319 | -54.86311 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b55dd5e-59ae-304f-8c4f-2b34e7005a4a | -7.01498 | -44.61931 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b25440f2-3992-3589-9816-10927d7eac81 | -7.15327 | -44.72086 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4414232-fcbf-3f75-8e66-06714fa48363 | 0.14553 | -51.46717 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45cd456d-10f1-3690-b22a-6e5df0c7d283 | -2.67713 | -57.53889 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 25d454d9-9a64-3859-ba5d-13410fc1c584 | -6.76735 | -45.4617 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99e699f7-9795-3c1f-bbd6-e8bf878f09f5 | -3.8757 | -51.18561 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dde6657-2931-394e-90b9-7613e1a4083c | -6.76421 | -45.4565 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6ce9f93-bf1b-3358-90a9-0492268c762b | -5.79372 | -47.77111 | 2026-09-13 04:49:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ec6c566-9176-3330-be0a-8fdfca8ec7ac | -2.94554 | -50.40558 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb390752-6710-30a3-9220-81136eb3ec90 | -6.22625 | -51.69582 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b762bdab-8188-39d3-9b6c-f6f3d3b37e99 | -2.94954 | -50.40245 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de6ac053-5e35-35e2-8e1a-83c6326f61bc | -2.94895 | -50.40611 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71150761-400e-3ea6-8709-7703933670fc | -6.7205 | -45.41816 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eda1fa84-e610-3529-a05e-7e0b8b383d36 | -5.12121 | -55.97387 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb794cb9-2366-329c-9296-f4171247d5b3 | -3.04487 | -51.26099 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed0e9eda-be4c-3353-8748-2bd0d37e3665 | -3.91045 | -55.73214 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b8b6ac4-6d15-383e-ad86-d9ace5560c1b | -2.66402 | -57.52015 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d94ae5f-43a3-34a7-8b07-e2b25099a5c8 | -5.02304 | -49.99604 | 2026-09-13 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| efdb304c-a1d5-3da5-b55a-1cdd494dee33 | -4.15706 | -50.21096 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6351f1d2-9d46-34a8-aeaf-01e89f532e7d | -2.94494 | -50.40923 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dafc674f-f4cf-3e67-abc0-6eaade8492bb | -5.4933 | -49.50636 | 2026-09-13 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b137b443-8de3-3825-9fb2-e0838729d5bc | -2.95696 | -50.39987 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24fce4a6-46ab-3727-9380-73ffd9e7400e | -3.89536 | -55.82054 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e74c0d15-c6f0-3e64-98cc-94f0ea506b8e | -6.15811 | -47.71447 | 2026-09-13 04:49:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbee4fcc-a9ec-350e-ae30-1af73177abbc | -3.04712 | -51.2694 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1e4748a-a403-30ba-8133-beadb04b2d01 | -2.82561 | -51.3447 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e4772ca-c73d-390e-83b4-dd4d08363bad | -7.38576 | -45.35008 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cdcb838-5c07-39bc-899a-607225b5e5f4 | -6.09746 | -49.66327 | 2026-09-13 04:49:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03a2e82-cdb1-31de-9a2d-1ded1656bb2a | -3.55141 | -48.18129 | 2026-09-13 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b880d68f-fbfb-37e7-84b3-ae1e34282a55 | -2.96379 | -50.40094 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e50b02be-aaf0-36e6-9ddf-5814be4e9881 | 0.14275 | -51.44994 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e0e612c-047e-3c1d-995c-5100e4074fa1 | -7.40279 | -44.54797 | 2026-09-13 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f5c47a4-cb69-363a-aa99-a715ed187b65 | -4.35438 | -54.77698 | 2026-09-13 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c91322c-acc3-3405-b8c1-9e6bac95236d | -2.64409 | -48.57069 | 2026-09-13 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4de4c34-751f-3225-a9ec-25b6cb3dadea | -6.65789 | -44.96107 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21728f3e-f6b9-3101-a4df-1536f34e29e4 | -6.15922 | -47.72972 | 2026-09-13 04:49:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7c7f228-0879-36d7-910f-936bdd0516b3 | -7.13708 | -43.75039 | 2026-09-13 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 926a185d-f3fe-347c-a36b-cc4c27345a04 | 1.06777 | -50.95992 | 2026-09-13 04:49:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2174d0d-add8-31b1-8882-8ea9f1a6e6f6 | 1.07103 | -50.9808 | 2026-09-13 04:49:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 504e22da-1616-3e7f-86f5-8e3cde9a0802 | -6.08281 | -51.75546 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a48c0c2-70e2-3021-a681-0cec2d682cbf | -7.19945 | -45.92027 | 2026-09-13 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b665c600-6c9d-32ae-94d1-a44c06ac7bb7 | -2.67874 | -57.52924 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36d93d79-1ba9-3582-8d7f-214dc4e83973 | 0.14184 | -51.46775 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef621159-ddf1-3fa3-82d3-91aaea223ae9 | -5.12809 | -55.9608 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 758dc32d-e1af-3baf-924b-bda194063831 | -2.95072 | -50.39513 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46c1998f-1ed8-3fab-8026-2a2b97fbfe82 | -3.90966 | -55.73682 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb9dea41-c848-38c9-a95d-bd008a9bd39e | -7.00946 | -42.11555 | 2026-09-13 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c392c50-ec1c-3084-869a-50def177968e | -6.00049 | -44.25829 | 2026-09-13 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aee3c4ad-e5d4-3e02-bc4d-4de0fdf5e43c | -2.11259 | -48.99655 | 2026-09-13 04:49:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48f0d3d6-c3ea-3009-b009-9d367add5ea8 | -3.6445 | -58.62837 | 2026-09-13 04:49:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 336ed48a-aa49-357c-8b09-23d9942fb468 | -4.13636 | -56.3266 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2d85525-58fe-3bff-b337-0398f60f70af | -6.72741 | -45.42418 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f3bfd63-160e-37f8-ae86-3dd73ce4fcea | -4.39245 | -42.33958 | 2026-09-13 04:49:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2b213fdc-3019-3876-ac72-3f068ec966bc | -2.68132 | -57.54623 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0679e7e1-8fd8-3a71-82d9-4a755273be8d | -3.16198 | -48.60978 | 2026-09-13 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e51edb4-5f6c-3332-ab5a-11d87b7558a4 | -5.81594 | -53.80167 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a272adfb-f380-3be2-8b41-1b78c0a78cd8 | -2.96155 | -50.39309 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a2d7078-d00e-37e5-bac2-08db98e4cd6e | -3.98582 | -51.08597 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2c32bb2-3447-36de-a14c-572cda4f744a | -1.79223 | -47.838 | 2026-09-13 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0edd445f-813b-3928-96c2-b7a040764fae | -7.36953 | -45.35252 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef4b567b-4050-3a97-babd-d31677f245e6 | -2.67131 | -57.54121 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0896e539-f862-35dd-bc47-29159861f22e | -4.45426 | -50.16625 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c2f3fa1-7dbe-35b5-9989-eb177c7fa9a2 | -2.83031 | -49.22728 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README31.md)
