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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1faec1-4c15-31c6-b1c8-d0bea6b5c45c | -0.87243 | -51.95036 | 2024-11-13 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cf237f3-92c8-3f55-9e93-70e054b4fc5f | 1.05908 | -60.60366 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 72adba42-03cc-379e-b7ea-e3e7827f2277 | -1.64889 | -52.53996 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59a2e32b-7c47-3b33-82e1-7edfb9df00e0 | -1.66262 | -52.54206 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af11e7da-2f7e-36f5-a9ee-bfebaa28d098 | -1.30305 | -54.13951 | 2024-11-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb1b5d9c-9797-39aa-857f-fe93f969a1bf | -2.14301 | -46.39783 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d01558-afcb-3d64-84e8-5c2b421654dd | 1.13867 | -60.59862 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d26aabf-0d5a-3f3e-9211-77ada31417a5 | -2.24047 | -53.74841 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f825e07e-bd9d-3ebc-bf13-6311c3786d72 | -2.60965 | -48.25289 | 2024-11-13 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 775fd52c-4da2-34c1-9d73-66612953b0ee | -2.34333 | -53.89535 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7974a908-b396-3a3e-a1ba-4fe0565d0b0e | 0.92359 | -59.4103 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75f36dae-e952-360c-9885-f0ee944da654 | -2.0446 | -53.95664 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b8e5c2e-1c86-3042-8aa3-5c53b2477dfd | -2.2526 | -53.75436 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3fcbe38-443b-37ab-ae56-6c2ba507eb9b | -1.39578 | -52.3931 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08199e59-e110-3700-b570-29199997fb02 | -2.37883 | -48.50958 | 2024-11-13 05:20:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1278b370-0073-318f-b1a2-23937a0857c7 | 1.06308 | -60.60682 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78612ce5-41da-3c1b-8020-6dcd037d93b9 | -2.2453 | -53.7452 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8657ec2-3739-3c9e-a0e4-a416666a7ffa | -1.42067 | -51.11412 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffbde197-39f3-3e5e-90ca-69a9c269ce82 | -2.20807 | -53.74082 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 558ea8c6-df16-36e1-8dd6-803bf450e72f | 0.92304 | -59.40683 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee0b2b0a-e9de-307c-abbe-d1aa6fd53284 | -1.76994 | -55.61354 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd6a9e72-32b6-3e03-a199-22a1113ef944 | -1.62704 | -52.65413 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10abdaf7-0ea1-3453-a444-5dcf358d8dce | -2.20746 | -53.74471 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ef64e44-c221-39d0-ba75-830421caaa53 | -1.2099 | -51.77234 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46d25e5d-cd7b-382c-bef3-6d3caae68bd2 | -0.68741 | -52.73825 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f49fd6-809b-306c-8ea5-c9cc5afa14c0 | -2.21075 | -53.74379 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 857f7efd-b4bf-397a-8af7-45865800cadf | -1.4178 | -53.47255 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b1b15a0-1a80-35f3-b6c4-d1c7182e5f41 | -2.698 | -49.34337 | 2024-11-13 05:20:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ba64399-9a6f-346b-9cfb-12ca7c9de48e | -1.69779 | -52.70683 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7870d9fa-a542-3b35-b994-ed8ebe613b7b | -1.41293 | -53.47583 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6b1c5b2-86e8-3b9b-88e7-f7bb17b974bd | -1.64105 | -52.53129 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bcea19e-ad8e-3e16-8f62-3f595e662adb | -2.2111 | -53.74921 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68d9d60c-dd4e-32e3-9c53-4e91476bb4c2 | -1.21388 | -51.77822 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70005366-8bfa-330d-a766-7840cb70a80e | -2.2447 | -53.74913 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b9541e9-2221-39f7-bfe9-6e7f02c9a796 | -1.98697 | -51.09962 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33cf1ae4-7537-319a-8311-c74c6d9bab80 | -2.37399 | -53.86442 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a5e141c-8c59-30d6-8c07-3461501fe2f9 | -2.11163 | -50.69656 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00500c1e-e2b9-3ff5-ba45-c03626b690e8 | 1.89038 | -60.47402 | 2024-11-13 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab37e47f-ffdd-3757-9202-9173454541f5 | -0.36916 | -51.73701 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81dd8c2e-7991-329a-b258-143e14d34591 | -2.73071 | -51.74356 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66fdee01-f962-3959-930a-a301021e8a36 | -1.98189 | -51.09885 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f979f675-d53a-398b-a55b-17fa7f5357c3 | -3.03065 | -48.07609 | 2024-11-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56d5757e-18fb-3b17-8b95-42d5bdc45fb1 | -2.2065 | -53.74318 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3d7ed7-5f47-3d11-a764-74619212d275 | -1.38657 | -52.39167 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbf038bd-8dff-344b-a20d-0c636c2ea3c2 | -1.66182 | -55.16198 | 2024-11-13 05:20:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af685e8c-fda4-3ebb-9400-d5b86aab2a97 | -2.77928 | -50.30512 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba54d8e7-6ffd-3a2a-a8f7-05f2f6e59ac7 | -2.43526 | -53.88423 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98eca433-f1d4-3554-b905-d02c623f0947 | -1.4161 | -51.11045 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7094f72a-5661-380c-8cb8-07bcef356218 | -2.39886 | -53.73187 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e836a671-58da-3f99-ae39-50f23810cef3 | -2.12306 | -50.69187 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0c0e20a-faba-340d-87df-5f14e11be7b3 | -2.7297 | -51.82722 | 2024-11-13 05:20:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f4dc56f-75a4-3718-a810-45adad39c390 | 1.11214 | -59.18892 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77ec085b-648a-3cf5-a9f0-082609d52f0b | -1.57991 | -53.73302 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8568f46-e55d-3aa4-9e61-889703f843c7 | -1.55776 | -51.85448 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ed7e546-3329-390e-8b68-f6bfb7100bd1 | -1.61288 | -52.53172 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afb9ef69-60e5-3505-b137-f9e531c3c48a | -3.03619 | -48.08205 | 2024-11-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6faa31ed-5b0c-32ec-8f42-ab20aa6efe26 | -1.7336 | -53.27743 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3740563-53b1-3981-af5a-9610e0aa80a6 | -2.78083 | -50.29477 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99f03f10-ca2c-3a9b-8474-cd926d4640ac | -2.72665 | -51.73733 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb12cd46-7152-3fd4-af71-5caac709b689 | -0.97265 | -51.72383 | 2024-11-13 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74b49034-bf18-3e52-bb75-0cb0ccc76251 | -1.47142 | -52.30284 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02197f94-2a6d-3892-8edc-d4840b57e106 | 1.0545 | -60.59681 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 46137f40-2a1a-337c-9eca-519f04d2fd32 | -1.65458 | -52.62569 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31fefe54-5c05-3dc2-a3f3-57337fc0a6a3 | -1.39118 | -52.39239 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4429660c-7376-331b-8c7e-39ff06b55697 | -3.04425 | -49.71293 | 2024-11-13 05:20:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ca54980-8bbd-3365-9846-80de905edbf1 | -1.22346 | -51.77964 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 306ea19d-622e-30e6-80a8-c83294acd5db | -2.45959 | -53.97843 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f674592d-80a4-330f-8722-28a4bb2c4b29 | -2.78601 | -51.75262 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eaf9b5e-2895-3a82-aea0-a9c728d2fae1 | -2.78417 | -51.39891 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97a078eb-fef2-3122-8ec5-613770e5945a | -1.50887 | -55.87809 | 2024-11-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70bd5fae-1d0b-3d3a-a240-7be4cb5b1fda | -1.69326 | -52.70613 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca6ed092-5d39-3ae5-878f-a0d86e2eea4b | 1.05393 | -60.59312 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dcd357f-7cbd-3f77-80d4-611406b269ee | -1.44046 | -55.45375 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 641e7960-3193-3b6f-80b1-b133af243dff | 0.06774 | -60.5434 | 2024-11-13 05:20:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52635e4b-2af2-3f41-8d8f-f441fcf3f5b5 | -2.78276 | -51.39893 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c33330e-433f-3fbe-b431-26e6bb21f6a0 | -1.97019 | -46.56581 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 011dcb4e-e76c-3628-a0eb-45612767bb02 | 1.05165 | -60.60104 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ce752df-3a12-3261-a8e1-8180b8305540 | -2.11882 | -50.6847 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e98678a0-4d71-35ef-857a-7a473cf5aea9 | 1.06135 | -60.59575 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b377c87-f266-38ab-86fd-273874eab100 | -2.40976 | -50.3038 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e34e902-45e7-3eb5-8e15-e623810cf90c | -2.66275 | -51.72746 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9315fd5-3e6f-34ce-9230-8063c1d0e500 | -2.40715 | -50.30722 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63064627-6746-34d0-9ebd-f09fe055d84f | -2.65866 | -51.72122 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 274dcaca-d3c4-37e2-adeb-504f784d1662 | -2.60612 | -48.24854 | 2024-11-13 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 335a1a81-86cd-3caa-8926-a880886c4321 | -2.39158 | -53.6658 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcf8168b-1a92-3bd2-888f-c659875a2a94 | -1.64572 | -52.52997 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16017ab1-f288-3f58-8d82-5bea4c16337a | -2.77386 | -50.30425 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98efb512-7235-3071-aa7b-6de66c65735c | -1.65874 | -52.53673 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ced11be7-7525-3594-9715-03da6c7a5d90 | -1.41565 | -51.11333 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 115031d2-4375-33bd-8457-ac3a93f849f6 | -1.21071 | -51.76717 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41aa8092-df06-36a4-b96b-c244faf05ce1 | -2.21017 | -53.74768 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d13af412-3845-3137-b14a-384238ada990 | -1.65019 | -52.5327 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b00c1df-7039-3eb3-bb6b-78a2168e799c | 3.37658 | -61.19909 | 2024-11-13 05:20:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd87ab95-3d92-39af-81fb-52d15b49978c | -2.37437 | -54.42205 | 2024-11-13 05:20:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1350e71d-2206-39ce-94ef-f308089197a9 | 0.623 | -60.08831 | 2024-11-13 05:20:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b86b7e0-b893-3e04-a47a-e72da8cad534 | -2.6974 | -49.34737 | 2024-11-13 05:20:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cca56e4d-2072-322f-aeaf-85e0eadfee9b | -1.7662 | -55.61294 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ef2a52f-4d55-3298-ab07-fbac025facdd | -0.36839 | -51.74205 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abe9fca0-b51d-3ad6-8c14-0cdeae965910 | -1.60951 | -52.40178 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a372c826-76ff-34c6-a0b8-331a7b378e9d | 1.6 | -55.77586 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README44.md)
