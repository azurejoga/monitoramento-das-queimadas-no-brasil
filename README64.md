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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4609bf3d-4b4c-3f4d-a600-7f5fa5827205 | -6.12969 | -44.13044 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d282a5d4-e981-3b9f-becf-85dcc362c454 | -1.87776 | -56.30799 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83bbc350-94a1-340a-855a-a602bc0c5901 | -3.56673 | -54.67829 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ad19845-7de4-3412-ad23-2124a24a68e9 | -4.81795 | -56.07972 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9df4e91-24f7-32c9-9130-5d8c3f090a22 | -3.23546 | -50.18278 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4e22519-37ce-306e-8bdd-634cd047dd7b | -2.86205 | -54.17624 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 296ad9ef-3a93-327a-8523-5812969b667c | -1.6247 | -54.42357 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76818334-4332-3975-a2b1-a2abd9239ab0 | -1.32551 | -55.44788 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fb6cc5b-2e4e-36c8-a83f-f2f5abaa9d14 | -5.59815 | -47.27946 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e41299c1-911e-39aa-be90-aea0dc6c8362 | -6.7038 | -47.38597 | 2026-10-10 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e511d4d4-346f-3d37-b73e-62a4990bf26b | -3.33824 | -49.6636 | 2026-10-10 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7798cd85-4254-3a4f-82d5-23ab80b94698 | -1.27498 | -55.75748 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e243d1fd-8fe2-3966-9ea6-c66ee2fe7c02 | -6.13036 | -44.12597 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bca0cddd-5d15-3661-96ed-e471980d6cde | -2.75164 | -54.10389 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a285044-7eb2-33a8-987a-0058f1a3d88f | -3.90361 | -55.90367 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3077ef5-b2e9-30af-be70-68889ee13691 | -4.93603 | -47.44506 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c648de9a-8b63-3d6b-91d0-e4b381227721 | -6.21354 | -45.42836 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 543831dc-0729-3d18-9aaf-74843b5aa464 | -3.23478 | -50.18695 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ff948a86-7d08-3ecf-8af9-b990303256d0 | -4.88987 | -49.0503 | 2026-10-10 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50c2bc9c-aeb3-381c-80f8-de98b4f3c7f2 | -4.39845 | -49.77684 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a52489a6-5e07-38ed-a5cf-a49951af467e | -1.44677 | -54.47714 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a6e2624-45f9-38ea-9dfd-e62292d2fb76 | -3.55457 | -54.69219 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e951cea6-c1b5-3fa8-aa7c-76cc58be9392 | -3.43496 | -59.3624 | 2026-10-10 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57087072-7c27-39cd-9c21-b1e603a87534 | -5.51963 | -50.02558 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7f5eef1-8b34-398d-9951-1f43d1740d2d | -3.54891 | -54.6965 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54fbb877-21f8-350b-b941-eda31ee121ea | -3.78155 | -52.06605 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c84a15-db8d-3bf4-897e-4c000dd6bd38 | -5.46039 | -44.78163 | 2026-10-10 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b8092df-e567-3577-b373-5e899517ee8a | -2.98895 | -54.17413 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7da800ec-80e7-3e8a-9757-d3ad0088b19f | -3.34463 | -50.4059 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c159a5de-4f35-3648-8386-a09e91cceaa8 | -3.897 | -55.81492 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d50bcdc-7395-389c-af08-07e247db5e34 | -5.84108 | -44.92587 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12bc08c7-efb5-3d78-8bcb-06d3b033e0a3 | -2.51321 | -56.14263 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6dbf2f1-65aa-3a9e-b5f8-a185d1dc7528 | -5.09432 | -46.22636 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70bf3d92-257b-3dab-bee1-4afa211d377f | 0.48202 | -50.79034 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0353777-223e-3efb-bbef-f72001e290b8 | -6.64529 | -43.44745 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13ec30e1-a055-3470-b633-4f5cfc225182 | -2.4011 | -45.57321 | 2026-10-10 04:44:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76972aa0-180d-3d9a-91ae-91ab3f724770 | -2.73661 | -54.13673 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27cbe2e6-16d7-3bd4-bbef-f79b7e87a18b | -4.58572 | -54.95039 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c7f404c-19a1-3502-af61-20f1f3f7898e | -3.03946 | -53.89059 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6310f1d6-c4f1-30d2-8d34-ad118735d5e9 | -3.4866 | -50.49193 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f3cf54a-2ff6-372b-b656-0cbb7f36d175 | -3.1057 | -53.94252 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9f688b2-6fdf-3afd-ae5f-e647d2261855 | -4.43019 | -47.53875 | 2026-10-10 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| e77e56a7-c43d-38f9-b412-349515d271cd | -3.12129 | -54.17939 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8676331f-ae85-3c0a-b05c-6f812191a1d7 | -3.53719 | -54.73788 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6494c3db-5796-3c0b-9588-39ba1b5657f6 | -5.75542 | -45.13082 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c00e77ee-4814-3847-8018-4031630a7bad | -2.56033 | -57.4198 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c88d7498-ead1-382b-b9d7-eeb7cca66973 | -5.11175 | -46.22539 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e575d562-f532-337d-b6d6-95c36f8a3399 | -4.02828 | -46.98574 | 2026-10-10 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91950bb2-68c6-3caf-85c8-a429e2d0736e | -2.3027 | -48.54522 | 2026-10-10 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3bdb543-2121-37a6-8c42-0f256e79e959 | -3.95369 | -55.3479 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6922c218-c0d1-3807-ac10-febf50afcc06 | -2.2386 | -51.92488 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fed4f43-0b69-3e76-9a49-98d593417789 | -6.06376 | -44.66715 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 463f8e0e-2833-3346-9e9b-31e6f4c95886 | -3.56336 | -54.69907 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db7cb2a0-4677-3772-916a-c830b1f3b4f3 | -3.77763 | -58.58288 | 2026-10-10 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3b2e407-f59c-3d07-8417-ca06dbb706ae | -3.57244 | -54.69682 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e8c5055-f462-392d-99c1-c1b77008d556 | -5.74546 | -45.12537 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6f273f0f-b346-3c04-b570-b0d62ac46be2 | -1.87693 | -56.30655 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b58736b5-be4e-3681-ac40-13f5b5e3d7a9 | -4.23747 | -48.72043 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1893b629-c45d-3a0b-acad-2c2e34f91b91 | -4.05687 | -50.96586 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8960c133-26f1-325b-8010-2759e24124c0 | -4.81689 | -56.08603 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 093d2aed-66d2-3fc1-80e6-da92547451f9 | -3.76186 | -45.9547 | 2026-10-10 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d975af40-3e1d-33a5-9fff-1675f51b9140 | -3.12759 | -54.17052 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6396cb2a-1d83-312e-ae17-7721d8e2f2c3 | -3.53454 | -54.74435 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0b365831-52a2-3bf9-b860-e76cd6511631 | -3.3167 | -54.68103 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4867702-5a51-30d9-a795-264555f4b6d5 | -2.39194 | -51.29682 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15428146-9d69-3ef2-9382-c31260c73cb5 | -3.76944 | -60.71798 | 2026-10-10 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90925aa4-01ed-3538-99a8-cb6eb93291e3 | -5.69649 | -53.4664 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78876dd2-8254-343b-b594-e35d9026cc4d | -3.24401 | -54.0346 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a10fc25e-a5d4-375f-8f3c-1e82992c5933 | -1.26423 | -55.7557 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34424bd3-1ab4-31f6-a4cb-6031e26ba592 | -4.66981 | -50.44366 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1feb3c19-cb9c-381d-8943-ee35ebccec85 | -3.91125 | -59.59697 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25ad64a7-b5c5-3499-948f-ac34bdef91ad | -3.88369 | -55.9881 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ee80f42-0245-3d22-b381-be69f17c536f | -5.9916 | -41.36799 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e4b7650d-621f-3dc1-b43a-820b65c10412 | -3.84835 | -55.78783 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c48879b-f89a-3629-baec-717097df8b98 | -5.0842 | -46.22477 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d368d41-f01c-3be5-b3cd-a6b5803e0c8f | -3.03153 | -59.16069 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e03e3e8-418f-3aa8-9023-d6d2eae48569 | -6.09116 | -44.26197 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28bc4b02-9c6b-3023-b4f3-dc5cc9ba5579 | -1.63618 | -54.41455 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 661b3fdd-8a6f-3f24-b633-001a90fb3954 | -3.25622 | -54.19027 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac89e820-d892-3ba6-b151-7a8719eac11c | -1.27129 | -55.74628 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d226e304-ee4e-33d3-94c1-a898967daceb | -3.45714 | -50.59111 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74885554-3797-33da-af2f-ef3f15d7bf26 | -1.28675 | -47.1383 | 2026-10-10 04:44:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94ba1024-6007-3952-a966-c82e3a4a9b5a | -0.87802 | -48.72031 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b5a1273-626b-3d95-bd43-141de530f7d6 | -3.18315 | -50.57224 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45a7e1f1-d5c4-305e-89a6-0c26535387ce | -3.73036 | -59.45646 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99795534-36b3-3b38-a194-966947faa96d | -3.50296 | -49.93756 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a769f09-3e64-3df2-88be-4cc95be4b713 | -6.04191 | -46.41626 | 2026-10-10 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9d4466a-231a-3067-b845-3f12005da72e | -6.81857 | -39.54814 | 2026-10-10 04:44:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1ee3c8ad-c904-3cc9-94e5-1d24dc8895f4 | -3.20821 | -50.55833 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 835a8314-a746-37cc-b4a1-663144c39885 | -2.75552 | -54.10962 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37c0dcae-8a27-3032-99c1-6dcc3f804078 | -3.00114 | -53.89375 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c23cc1e9-77ea-38bc-bbcf-00a5ad442878 | -3.49098 | -50.48822 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8ce1092-8e86-3e74-af9b-14d5c97ae7f6 | 1.68235 | -55.6072 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8962a81-488b-3eb5-ac12-6ca7371ec468 | -3.45414 | -50.58616 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f055085-4934-3370-a742-537e8fd74aee | -1.33474 | -56.39639 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24946bb7-c4f7-3e2e-a643-1aba5b497b00 | -5.87486 | -53.51682 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e7208ab-d5c5-3ff5-9ce4-ca8653133da4 | -2.83485 | -54.81476 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4122b0f7-7a90-39f7-8c1b-2b3b8d840a21 | -3.1736 | -50.5841 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb26f41-79b4-3278-ad00-23618c054330 | 0.42214 | -51.788 | 2026-10-10 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92544c8c-d099-34af-842f-514b121b6334 | -6.81817 | -39.55104 | 2026-10-10 04:44:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README65.md)
