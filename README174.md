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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8841f9b0-ccf2-3931-bde6-2ed8266b9659 | 1.2207 | -59.97507 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| effa2812-497c-3284-9a6e-cfab896acbfe | 4.26881 | -60.03461 | 2026-10-08 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 671cac0c-94a7-301a-8ee1-d600f2d4f0c3 | 1.10039 | -60.51617 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a4374a-a16c-3b8b-b47e-9c066fe86e11 | -1.29433 | -54.56157 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a864d71-f89b-3922-9c1c-a0887cab0bf0 | 1.65864 | -55.79881 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2922877-553b-3420-bd17-03cadf64a528 | -1.36397 | -56.9255 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e08a9581-0b1d-33a5-a248-ae32fd5e41e2 | 3.12272 | -60.64294 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c563acff-1e7c-3de4-8385-7af850638579 | 3.07468 | -60.55655 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0af4c44-9f23-3d9b-932b-ecc7c3c9d2e6 | 3.31071 | -60.05841 | 2026-10-08 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0886cc2-a502-3fe0-9190-091934e5eed2 | 4.43931 | -60.92813 | 2026-10-08 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5a92bbf-e658-3e78-893a-8859026dd082 | 1.69111 | -55.63521 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8146817c-240f-34fb-9d63-9a6f5ddbe66d | 0.44056 | -60.53492 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b04338c6-aac9-3072-97c9-005d096b98c5 | 4.3303 | -60.35264 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e35b1e1c-26b1-37a4-9b78-ccc29ce81c96 | 3.54099 | -51.27868 | 2026-10-08 05:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15e8904-4891-3cbf-a35b-0a87822b2a37 | -0.11876 | -60.68037 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0408c692-c9b2-3d2c-b00a-13e7a4d51c66 | 1.32142 | -50.84807 | 2026-10-08 05:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697d4681-19c4-33c6-a4c3-0e61a0609bb2 | -1.10703 | -54.15859 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfc41ea3-2a6c-344e-a42c-68d9908bdac0 | -1.47623 | -53.61898 | 2026-10-08 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fd42a26-7acb-3cc5-aba2-ed5b681452af | 3.34787 | -60.90524 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eff24cb-5090-3542-9c44-93492d333594 | -1.52697 | -54.54775 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63c2c9f3-ae67-3100-9e4c-e6ae2473282a | -2.10396 | -52.06349 | 2026-10-08 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab55aaa0-67cb-3833-828b-0769e2dbbd14 | -1.1864 | -55.6692 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 76d08298-fb5c-3ad0-b656-1d48dc931191 | 3.54676 | -51.27769 | 2026-10-08 05:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd560823-74f3-3a56-9d14-e9a2f3ecc604 | 4.31637 | -60.35112 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09c4f499-a2f0-3cdd-8662-8e83c6a10da4 | -1.12406 | -54.11763 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed58a728-c647-311f-9bbb-5517e64864b8 | 2.52122 | -61.00686 | 2026-10-08 05:40:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74f6d499-07c8-34d2-b51f-727e297b45d0 | 0.44854 | -60.54116 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1e0d5de-0168-34a1-a28c-05ec67e892b3 | 1.70463 | -55.61272 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 993ec455-ebdc-35f3-9b03-3593a7b0c4b6 | -1.13058 | -57.28455 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac209ee7-8d66-34bb-9c23-ca538fd3184a | 4.31693 | -60.35463 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5f07149-9f2d-384b-86ac-4136240b51a5 | -1.33228 | -55.42936 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b16f5bce-afe0-30d0-884b-b0e49a29d0ef | -1.28615 | -56.98306 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a1336b-6b79-3434-8995-b52bb44cbec1 | 4.68837 | -60.57215 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1cdcbb7e-ea11-314f-9b02-94ae7364b864 | -1.4772 | -53.61271 | 2026-10-08 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9796051-5e15-3ff3-bdca-9e85725ac1d3 | -1.60408 | -55.15949 | 2026-10-08 05:40:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9ebc12e-d93c-3ce4-9e75-c06506bbd240 | 1.9888 | -59.93132 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 848bbe6c-6629-360e-a710-9a3d1249b2c0 | -1.19139 | -54.13797 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2659a37d-f3b5-398c-a1d5-a502c4e33afb | -1.50207 | -54.8418 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 855d13ea-c2d1-3858-9445-86ac67eb025e | 0.85067 | -60.31409 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db203f9c-3735-3888-baf4-64698354674f | -1.62336 | -55.12991 | 2026-10-08 05:40:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a607a34-50e3-3d17-9540-b42ba99c5708 | -1.60542 | -55.15806 | 2026-10-08 05:40:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7ce3863-4bed-397b-84c5-0fd5f5db1845 | -1.39119 | -55.46379 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45421784-a0f6-37b3-94bf-16275f0ab896 | -1.32153 | -56.41094 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 413efc43-67de-3873-95ab-71e03c7778a1 | 2.88311 | -60.29869 | 2026-10-08 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c183838-f3cd-3d4d-97f0-1cfb9473c9a5 | -1.1051 | -54.17076 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df9ee600-77fd-3f21-b68e-f6b792dfa10f | 3.15358 | -60.62731 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a46fae47-61ed-335e-bdfd-3fbe4db89318 | 0.78766 | -59.19573 | 2026-10-08 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0e4485-921a-3ce5-a04e-04a0b664a050 | 1.36432 | -60.37064 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a2c45c5-3c2e-3d46-aa50-f15f457359e6 | -1.10977 | -54.17442 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d69ec06-a836-344f-891f-4c26dd14ce69 | -1.10046 | -54.16692 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0acd2169-b7a9-33db-8e38-8c4e8064fc8c | -1.62819 | -55.13074 | 2026-10-08 05:40:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbacf0c5-39da-34da-945c-95e107e574aa | -1.47661 | -54.54459 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d7591f9-1a4f-3b27-bba1-f6fdd6429247 | 4.31471 | -60.3621 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0e2280a-0f95-3eb5-911e-fc45141e6132 | 1.69049 | -55.63714 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b2be1d3-6114-3b45-8819-2418712f0721 | 1.31604 | -50.85379 | 2026-10-08 05:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 416b17b9-fdbb-38ab-9615-49e9feeefe32 | 0.87203 | -59.81305 | 2026-10-08 05:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b6ac29-6f6d-3cae-a4c1-605cc1ba862a | -1.28415 | -54.56171 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a2a6715-6bdd-3794-8ef2-055025e616ef | 3.08081 | -60.55196 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07fe3465-374e-3207-bfef-51b3ab010416 | -1.10656 | -54.16159 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 280ae422-8455-3e57-92d3-275dfaee75ea | 1.99989 | -55.87371 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c51c516b-8813-3b13-ad24-e69211d204bb | 0.79191 | -59.19928 | 2026-10-08 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56829b9c-2859-387e-8bd7-ce0ce7492631 | -1.32221 | -56.40667 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 549c1a9b-959c-3f71-a81e-6857d585b975 | 3.34455 | -60.90576 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b7b7eb5-caad-37e8-ae35-a9d53b9e1fe9 | 2.90572 | -60.94633 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac00681-743e-3e2d-85b9-71d2694c1f7d | -1.4569 | -54.7737 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d3400d3-2d97-3514-87ca-5312be970080 | 1.31527 | -50.84906 | 2026-10-08 05:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4faa865-63c2-3bca-95a0-c4971618b71a | -1.71853 | -55.43875 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3aa2e2f0-0c28-3743-84c9-a53321a047aa | -1.14741 | -54.21839 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a126e45c-e7dc-3434-a225-394f92049b2a | 0.91079 | -59.628 | 2026-10-08 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eaa19d8-b10f-3355-869a-6cb9f4008f20 | -1.53201 | -54.5484 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50259dac-1565-368e-91e2-6695e8084441 | -1.14693 | -54.22147 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dac1269-0a3c-3cbd-ab61-f464350c1525 | -1.28802 | -54.56934 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab9db207-5930-36c4-929d-9d006a03e2c2 | 4.3108 | -60.3591 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d8db709-f438-3815-a95f-e5b1dc543b7c | 1.36091 | -60.37117 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcafb833-22c4-3db5-af62-390f229f2b60 | 4.31415 | -60.35861 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d1601a-0b84-358c-9231-bd5a13cdc8c3 | 2.1231 | -50.82516 | 2026-10-08 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89a00758-2252-34de-b7ac-7c4af7f3ca10 | 2.4377 | -50.82327 | 2026-10-08 05:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa4d9fea-562a-3af7-b9b1-1f4e6b6d4929 | -1.10799 | -54.15256 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dedf163b-e261-3493-9de5-864c4893805e | 3.07134 | -60.55708 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1450cdbd-0718-3da0-a34b-739c69d52ca3 | -1.12644 | -57.28389 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1235393d-e3d9-33ab-a3d5-32d03ac61cc8 | -1.12357 | -54.1207 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 751a9cd4-c166-3d1f-a9b7-bca15e5671e9 | 0.56563 | -50.79741 | 2026-10-08 05:40:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0b5de17-6656-3edc-8f31-58912105282d | 3.07412 | -60.55302 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 436fa9aa-56fd-3869-a752-50ccfa2de39b | -1.28513 | -55.42207 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 311fd015-c7f7-3a11-a8d1-3c5a363f0f5f | 1.98941 | -59.93512 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a573763-ee13-340e-ab4d-7ee7dfe77e44 | 3.62832 | -61.92367 | 2026-10-08 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c5f0df6-344a-31a5-a0ec-666c870abb49 | 4.27217 | -60.0341 | 2026-10-08 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b87c26e-6962-3d2c-a8c7-69634e6945a0 | 3.31013 | -60.05479 | 2026-10-08 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c057b2c-e0cc-3c82-8d24-d779eb22a06a | 4.3104 | -61.05769 | 2026-10-08 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4169724e-85d3-342e-ae79-f70c83d5b7c2 | 1.63258 | -55.77699 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47674b20-d1a9-366d-9108-78a00b72e6d6 | 3.07747 | -60.55249 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8285511-3300-36ba-b049-5c7bdbff21c8 | 2.71768 | -60.19149 | 2026-10-08 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aae397bc-7d47-3338-bcf3-d27d98e0a0b1 | -1.51885 | -54.5672 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2181ed44-f370-3d12-8b2b-4b4684ef959b | 0.44795 | -60.53751 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c79e56fe-8c6a-3514-8604-b4431d34dd46 | -1.09998 | -54.16995 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d658f0bf-e768-3bdb-a4bf-d8c75c42aba3 | -1.18578 | -54.14022 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b530f19-32f1-375c-a208-d5b186e41a8d | 2.12917 | -50.8241 | 2026-10-08 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d097e9f-d55b-3a09-a990-dec801b097c6 | -1.29388 | -54.56446 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a52e9a1-091d-3cac-9b31-57cbdc545a7d | 4.31371 | -61.05718 | 2026-10-08 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b73b50c-a7cb-3244-8085-6083e35f3b25 | 1.71649 | -55.60182 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README175.md)
