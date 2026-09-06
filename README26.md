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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e178603-e19a-349d-ab31-974e3fb3058d | -6.83514 | -59.42995 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 119cb883-7a57-30d6-ae8e-9a938fc75f50 | -4.34659 | -56.28809 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 030f8f05-f486-3e05-9598-ebdf59764e55 | -5.85262 | -52.04964 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e8d0d86-401d-3e5e-8aea-bda89e5d1ff8 | -5.14982 | -55.95514 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 284a6f80-7d06-3fc5-887e-eac0da5fbc10 | -3.07854 | -61.17988 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c03f84b-9f97-3f1b-b9ae-3920fc063a19 | -5.33833 | -56.03503 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb97c6aa-2ecd-3b57-bb63-d2954eb8482c | -2.25199 | -53.76364 | 2026-09-06 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c90a7fb-4cbe-3f81-b0c5-4d2fa1a01acd | -4.66577 | -55.63149 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0358a9d5-a0df-32c5-bf28-a8537e5e3030 | -6.16028 | -57.76561 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be252bd6-8085-3ef7-b4c0-20953b6909a8 | -5.3556 | -56.02283 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8b175fa-eda8-3e4c-b8f9-cc78853eec2e | -2.45708 | -57.91499 | 2026-09-06 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5ef77e4-2c5e-3023-8fef-1d1071013d38 | -15.49455 | -50.36434 | 2026-09-06 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0b6ccc4-194e-3ff8-956f-7fc8df93ff26 | -6.15639 | -57.78994 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7b7ae28-521c-38ff-abae-4158218a2d72 | -2.58577 | -49.49055 | 2026-09-06 05:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbc3b7f0-373a-3768-8e08-e2218d2292c1 | -3.08002 | -61.53383 | 2026-09-06 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71557cd5-ec35-3da6-bb0b-a198b606361d | -2.48386 | -58.00758 | 2026-09-06 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1165b374-6fa5-375b-bb0a-27534e64fb4c | -4.47741 | -55.09473 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2db73a4a-3e80-3535-acd4-22b004259eb3 | -5.65136 | -60.23643 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2579a7f7-c6f0-33ce-863f-bc615cfeeff2 | -5.35002 | -56.03656 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 048a4071-af90-3d1a-ba68-cf7bc4535336 | -6.9595 | -59.7357 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3792eb4-146c-3b75-972c-96779321b517 | -3.23359 | -58.89098 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f78bf4-f49f-3eef-9943-ee711c3eb443 | -5.35168 | -56.02587 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb88f7ae-7878-3723-8440-467b4850201f | -3.90139 | -55.87749 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00abd7db-95cc-353a-b299-25181b1a6326 | -5.33945 | -56.02792 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15e3623d-85c3-35c7-91fd-8dc3d65ef314 | -6.09251 | -55.591 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bed83c6-5ced-3be5-8a9b-87a1de879af2 | -7.09756 | -56.50757 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f2f6870-f81d-32c2-ae9b-5d4379f93412 | -3.61591 | -60.57442 | 2026-09-06 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 609db83e-9954-3687-9553-f8de25ab092e | -3.24416 | -47.24651 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ae5857-de03-3b5c-b931-14a83e93d3e0 | -6.84261 | -59.42736 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f84b35c9-f59c-38a2-b235-991bdc76c091 | -3.81421 | -55.8962 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7570047e-20c1-34ed-b2af-d40da16e77b4 | -6.94945 | -59.75357 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99c38da-ffc8-32b8-8f55-f78c9bd37543 | -7.34255 | -55.21399 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7760cbaf-2843-3d10-a44a-069b27e33988 | -9.37025 | -70.49972 | 2026-09-06 05:23:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9b706dbb-3d4e-3fe0-9165-78c544f22f73 | -2.86934 | -50.46542 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78ce4566-df8f-3717-bed3-d6e4d58bf1c6 | -2.87811 | -50.46669 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 831035b0-8716-3649-a708-912eaa9007c7 | -5.64911 | -60.23446 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60a28b01-d78e-39b2-8575-95d859e00b25 | -6.16851 | -47.08341 | 2026-09-06 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1c0785b6-9f95-324a-a1de-906d82fa6810 | -6.94882 | -59.75738 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52c95969-8473-3600-ab2d-df621e0843f5 | -5.30342 | -55.86137 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c8e52f-f1f0-3b9f-a814-ba65a2327b24 | -5.43197 | -60.18638 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9fcf949-e3a7-35c2-9298-42fac4710386 | -7.11421 | -55.12893 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ea0c84f-750c-3386-a30d-23595e24d722 | -2.51794 | -57.9026 | 2026-09-06 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bdd1a58-f17e-375d-9afe-65c49a6ce46c | -5.36123 | -56.031 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09084ae3-c5dc-3e82-a6e0-c6f94c088d52 | -6.87785 | -55.60954 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 135d7208-84ea-3d88-b305-93bf55911dee | -5.30748 | -56.01201 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b34320b7-2557-33dd-898a-2c233747f743 | -5.25388 | -59.98299 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 107a1c35-c096-3916-85e0-46e16c29984b | -5.17072 | -56.04199 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 997722e4-c669-3c5c-bdde-6dc65a04d212 | -5.35279 | -56.01875 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 582e0e0f-2258-3490-9788-dcad6ce65ee1 | -13.82563 | -51.66804 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d7080be-3d34-3a8b-82ac-8eef92781876 | -6.05843 | -57.78801 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc6133a-a42e-32ef-8975-24e5a8f2fbc4 | -5.65201 | -60.23915 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 075b4043-73fd-3c73-a4b7-17b2e8332dc1 | -6.87669 | -55.61703 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96c17973-a6eb-3df1-85a0-415b6807f785 | -6.0234 | -57.69361 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d066861-b219-33ce-a444-a4d8b591ecc0 | -4.55826 | -55.04173 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d26be786-7ea4-3001-9f9b-1e26ca89ecd1 | -5.36626 | -56.02083 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 698fd955-feb5-3d2a-8359-1bdb196e2373 | -2.98947 | -47.74881 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34ca29f4-93f3-37bb-a6d5-33616f373fda | -3.83506 | -60.77258 | 2026-09-06 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27993b56-4d0b-3e32-8f4a-2a17125f0de2 | -5.36907 | -56.02491 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| da54fb41-eb03-395b-a41c-c349bd083e3a | -5.85008 | -60.25439 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 394ed8e8-7c77-36d3-afaa-2db4abfce6fb | -4.45492 | -46.13504 | 2026-09-06 05:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49e4e895-87c6-3aaf-bb61-b6fd00bae00a | -6.87441 | -55.60901 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52ae2582-d23b-3222-8e5d-d38b585227f4 | -5.303 | -56.0186 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1832f43c-9af5-36df-b766-6b26770a7704 | -5.3473 | -56.02186 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 340f5246-9766-36d7-af10-d8614de6265a | -15.08858 | -52.52221 | 2026-09-06 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1bbf471-30dc-3048-a212-c91ef52d2425 | -5.13809 | -56.27201 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c67107d9-8627-3508-859d-cda60a4687e0 | -2.98187 | -60.93756 | 2026-09-06 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe5275d-8309-3fc6-84c7-fc960daf2960 | -8.50352 | -54.64684 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db0bc8a2-8ea4-371c-8bb2-185088ddf53f | -2.99477 | -47.7495 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aa2ca7d-c738-3c5d-ade2-33d35cbf5efa | -5.92198 | -47.89099 | 2026-09-06 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78420015-a893-3e54-aa47-5f7408d7df3b | -15.49046 | -50.36996 | 2026-09-06 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| abb50893-240a-3af9-8889-f94021d9f16c | -3.07933 | -61.17498 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14a83e95-6545-37f9-8c8e-19de967ddc8f | -13.33582 | -54.05639 | 2026-09-06 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72539daa-42fc-3748-a0b2-4b9d2238b35e | -5.57171 | -60.16053 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9db59226-b74e-3f95-8168-a6af6247e5b1 | -10.74575 | -60.70905 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ef96f58-5a54-398b-aa9d-24848f7b083a | -5.36459 | -56.03152 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f190a68-26db-32bc-adb8-d9d26af64732 | -1.86029 | -55.43833 | 2026-09-06 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50629828-a85c-35a3-b4fc-4a093cd50d0d | -7.10261 | -56.51926 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 317f4d7b-433b-324b-bf5c-07f6e2666039 | -3.76475 | -59.42297 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ae7820-f80f-3091-9c73-c1e69588c260 | -1.48556 | -54.80847 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a5fb934-d4c1-3adb-a81b-4812d2b55285 | -6.0673 | -57.79654 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83337090-cb41-3e4c-8a93-4ffcd8e694b0 | -6.16794 | -47.08751 | 2026-09-06 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8eeabd49-6b97-374a-ace2-eb7e633cc4bf | -15.08919 | -52.51754 | 2026-09-06 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cfce06f-f775-34b5-9570-15057ab0763c | -4.5554 | -55.03744 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 590f2f7d-3be8-3325-a914-bea8fe25939d | -10.7527 | -60.71025 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8ffba40-ea6b-3a07-b2dd-e86b255c1e25 | -5.34666 | -56.03604 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8da4bdb1-3e27-3010-ab41-62895a9864d2 | -3.26911 | -57.88102 | 2026-09-06 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78b23668-4442-3c66-8a99-1706b4ab5068 | -5.36966 | -56.04325 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 851a0278-8de9-3b8e-af7b-ccb82302a9dc | -5.3657 | -56.02439 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3629815f-a296-3876-bdfb-7b6dccc47d52 | -3.08402 | -61.53447 | 2026-09-06 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b3333e8-78b0-3a9b-988a-b694bb605190 | -4.66465 | -55.63866 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bad037c0-8f8f-35fd-9896-ee0e05afca2e | -2.30181 | -48.58914 | 2026-09-06 05:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a4919b6-8ed4-311d-a7ac-9153b63347a1 | -1.39272 | -55.17799 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9701b4c-9023-3088-bb96-c5a8824b0586 | -2.70793 | -59.68371 | 2026-09-06 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b3754d-369a-3e9e-a58c-48150851e4aa | -4.47397 | -55.09422 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b179eb59-0789-3038-b955-1a48b9a24784 | -6.20351 | -57.77249 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0316925-c22c-3fa9-94e7-326700638c9a | -10.74731 | -60.72128 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b7703b-eaeb-351c-a766-cb2b55af3050 | -5.34337 | -56.02489 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fa95351-a137-34b8-a869-3846c44aebac | -4.11543 | -49.07773 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 563888db-ad89-3d92-a59e-feb89a6c2847 | -2.71062 | -59.68577 | 2026-09-06 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4971641-f3de-36d3-835d-d5c91b690e75 | -6.09113 | -57.68985 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README27.md)
