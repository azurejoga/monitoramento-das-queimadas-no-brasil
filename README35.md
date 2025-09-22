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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4774e511-9304-3842-8b55-788fa1549c3b | -8.55547 | -71.02625 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8935c6-12b8-341f-81e5-956016206e2b | -9.27338 | -64.50687 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43bc4563-5f76-3348-8a2c-6c99e6965899 | -6.63265 | -62.92442 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2ee3496-5f08-3a1c-81e5-891774c6f84e | -9.13215 | -66.0026 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa14cfe0-34a8-3055-ac75-27a1240427f0 | -5.66769 | -51.65963 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e24345bc-027a-3d73-b586-5edfe6eb221e | -6.859 | -59.96351 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d37d0f3-ca4e-3de2-b326-35c808221138 | -6.54247 | -55.03053 | 2025-09-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b836e5e3-36cb-3f9a-811b-33e2dc676080 | -9.2138 | -60.85391 | 2025-09-22 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d39689ae-eacc-353c-9dbc-49022659ff56 | -9.10209 | -64.00941 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fff7d331-3b34-3dae-9f03-f032fd9b9b5f | -5.65845 | -51.4733 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6335333e-8a13-3d30-b253-e11ca278587f | -5.65771 | -51.47025 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e65537ee-fab6-316b-a516-c96733fb1487 | -5.65905 | -51.46909 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a199a486-986b-39cf-803d-95f985478c2a | -9.02499 | -68.52315 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 242fdba6-a1cd-3f39-bb39-d51e3cc7cb3c | -15.35286 | -59.18755 | 2025-09-22 05:31:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a6ec260-21e9-39f4-9e2f-6e83f0ac4b6e | -11.33257 | -54.34803 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7537b40c-bcb5-3de2-b310-67f32b7092fc | -11.74492 | -54.72034 | 2025-09-22 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d6a53ed-8322-3155-a5f4-4bf549665492 | -15.76472 | -59.4264 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78063e0c-0051-3162-bcd9-0ef6031efd09 | -15.83038 | -59.58923 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 799aa829-cd20-3f18-a051-808b3ad22c54 | -15.82644 | -59.58865 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e90b3b6a-6727-3963-b26c-29dabd050ad7 | -10.9183 | -68.23597 | 2025-09-22 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c4b0a8a-2d48-3d06-84f1-c8c45e5b8335 | -15.94888 | -59.39126 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35a52321-9f24-3319-8200-0c10b40220c1 | -15.4113 | -58.78399 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ed19605-76dc-3354-a60b-3a5803472f98 | -15.02986 | -55.28078 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 106b23da-bef7-3ff9-81a6-f09c2a0d7622 | -10.91771 | -68.23945 | 2025-09-22 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2dfa435-1558-385c-8ae1-8c3ad5b9cf31 | -10.43413 | -61.34211 | 2025-09-22 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 45d22273-5af3-3251-b668-c7e3d2ef67a5 | -9.47143 | -67.89308 | 2025-09-22 05:31:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a95d933-4ab5-3af0-ac04-647672f27944 | -9.91328 | -63.50841 | 2025-09-22 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f65f5f0-83e0-30ee-81a9-3ef7a5118801 | -11.63009 | -52.85345 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 39893e36-fdce-32c8-b57c-dca3d95fb4d7 | -11.6468 | -52.86118 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81939d86-4e4a-3cd2-ba50-e190191a7aaa | -10.27372 | -69.49106 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d30e730-41da-379c-93b0-77dd91169cbd | -15.76037 | -59.45831 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06b2ff34-e646-385f-b7dc-93a90b5e3e09 | -11.41351 | -54.71811 | 2025-09-22 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87c7d866-eecb-3f15-9b11-bd06c13466ae | -9.87865 | -64.82751 | 2025-09-22 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcfd84c7-b411-3a1e-93be-e3c4defeff15 | -14.42334 | -60.29485 | 2025-09-22 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff7f2f27-d323-34a0-94c2-278525ffd749 | -9.02632 | -68.52275 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1792cf86-a19b-36c8-9872-b05421cc2bc6 | -11.87204 | -64.93086 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 870b70ac-0410-3644-bbf3-5b039981eb1b | -15.4187 | -58.7809 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aa14edf-2474-3a8c-8653-d8fcb275fdd6 | -9.47172 | -67.10197 | 2025-09-22 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2e293df-7ebb-3bd7-9cad-cbb576b21ba4 | -11.43138 | -55.01219 | 2025-09-22 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b02f417-3f6f-3568-8d13-77c1360306bd | -15.30243 | -56.80117 | 2025-09-22 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81369330-c684-33a4-8690-05c791932311 | -9.71584 | -69.08221 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf14c40-02eb-3716-9023-a0650abae047 | -10.16222 | -68.69351 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb7e92f-0294-38a6-a9ba-bf9bc9e96a02 | -15.77421 | -59.41621 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad2391a3-5b65-3e62-bf35-f843894228b2 | -16.02351 | -59.45815 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8a5d53ec-4704-3ccd-a56a-b3f026583ce0 | -9.79933 | -68.88021 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5981e768-9f9a-37b8-948e-eed0c75b1a74 | -11.74654 | -54.72619 | 2025-09-22 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1493937a-e1be-378a-bfd8-28b6c0d35fd9 | -15.76921 | -59.41136 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10cec1dd-ef92-391a-b3e4-cd38428e6d94 | -9.81843 | -68.89578 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a726e6c-46de-3727-8343-5c6032e032a7 | -11.42636 | -55.01147 | 2025-09-22 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b39e8c8d-9da7-3f63-ba39-1113cd01641e | -10.17137 | -68.79025 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56d6f4de-3d1f-3520-97fa-a2fcc13ba0b7 | -9.49943 | -68.72751 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d84d89a3-95b9-3a73-8aa0-55e85786a340 | -9.46871 | -67.09661 | 2025-09-22 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a68512-75f1-3864-8058-d838a2f23d63 | -15.93182 | -59.45844 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 515c1c01-4c41-3e1b-be7c-943a0aaf9199 | -10.65698 | -69.02785 | 2025-09-22 05:31:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ef741a-3d18-334f-b629-43a9bc9a816e | -15.83108 | -59.58403 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 107ca7b9-4127-3854-ac97-cfe09a8c9eaa | -9.61105 | -67.54907 | 2025-09-22 05:31:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cca9d6c0-6561-30af-8f09-cfea758521e1 | -10.86944 | -68.28156 | 2025-09-22 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18a3b286-4920-3cc8-8b7a-fc20cc401633 | -15.29651 | -59.42449 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91484b18-8c79-3491-a0f4-2bd90262f1f7 | -10.91078 | -68.43179 | 2025-09-22 05:31:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 046bf93d-493c-3533-9406-7752ce54e8b1 | -10.44886 | -61.33674 | 2025-09-22 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4b4fc04-483f-32d4-a11f-5fb4f804c411 | -15.77098 | -59.41015 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 582683d0-0eaa-3d8a-9fae-305d22a13031 | -11.87876 | -64.93198 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7e8fd6d-de2b-3dd0-bb18-7fb2ee78b34a | -11.55683 | -64.72974 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bc43a29-c670-3030-bd29-6b8c6ce5fa04 | -15.95384 | -59.38453 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 30fbf7b0-23fc-345a-b24c-ae06f96be341 | -11.31234 | -54.33901 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b3372ba-f066-3a29-9316-84ce0c876cea | -11.88431 | -64.94038 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 660cb9bb-22dd-3378-8fea-bee1abb6e9b1 | -9.19003 | -71.83847 | 2025-09-22 05:31:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b88b9824-d5ae-3fe7-8ad1-b8d46fc7d408 | -10.43469 | -61.3384 | 2025-09-22 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 349c8d13-3d5e-34d2-8952-00891eb3f9c8 | -15.03468 | -55.28464 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd1d6eb-4b1d-3a1a-820d-55dde2369df4 | -15.951 | -59.4058 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebe2198d-881e-374e-9e9c-1a87312f6d59 | -10.1947 | -68.7869 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07a1e5ab-aa4f-381c-8245-dc5c0d957c5a | -15.77321 | -59.4118 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5dafc758-970f-3170-ac17-dc538d55ca43 | -11.87364 | -64.94237 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 710f096a-b2ce-35c0-a66f-eb4ea104c1ea | -10.16738 | -64.73406 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff98ef0-c2d4-39dd-ba29-34e50f1416ef | -11.85623 | -64.94324 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61b02b26-784c-3929-ab23-d182f8198e05 | -11.74453 | -54.72342 | 2025-09-22 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0adc2491-0bef-303b-988e-a7fc132a13c1 | -10.71564 | -61.59238 | 2025-09-22 05:31:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1315e182-afe8-344d-8512-0f218d42e4fa | -15.03951 | -55.28837 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c74538b8-2b1a-3fa7-8c35-5577d83df31b | -10.164 | -64.73349 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7749d2-8324-3dca-9ff9-09ba6e1ad1f4 | -12.19249 | -62.00564 | 2025-09-22 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8de92b8a-56f6-371b-be96-a3f9440ff021 | -12.45843 | -64.20134 | 2025-09-22 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cecb869a-4293-34ef-89b3-a76bb905e36d | -11.63539 | -52.85845 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5b53e00-a04e-34fd-aece-0af602dd66cb | -15.95033 | -59.47144 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 134f61c2-53f6-371c-ac4b-e8286e99b797 | -15.97418 | -59.47473 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93140c52-ddac-337a-b299-22a81d6e1ce4 | -10.27291 | -69.4921 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e637789-d211-36bc-8903-91eac8f90171 | -9.46792 | -67.10134 | 2025-09-22 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f072ba5f-125c-394a-a722-d4e2946740a7 | -9.68082 | -69.01368 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc446b20-a0e4-3708-9e27-51f61ea81634 | -11.79491 | -64.92588 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d14b58f-30ec-33dc-914f-bbddde29c678 | -10.26958 | -68.77613 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 134b0e24-ec19-396d-a6de-f864a6f6e188 | -15.77574 | -59.40505 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 268f581d-76e5-3d98-b195-e18662380fa6 | -15.76621 | -59.41543 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36a8f96b-180d-3bb7-be46-22c053993b55 | -9.72085 | -69.07884 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c33a50-8280-3083-a6b5-828478b142b1 | -10.19455 | -69.35124 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4437b6c9-abb4-30ab-bbbd-fdeb6997711e | -15.84091 | -59.5114 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23f015a7-947b-3bba-a5a8-29d9621c6b4f | -11.12129 | -62.85514 | 2025-09-22 05:31:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ccb255c-f4a3-33ab-97c6-59b6c940c95d | -10.16091 | -68.70115 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0580e572-8893-3b2b-a2b7-59d561cd26b4 | -15.04471 | -55.28896 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d8cde4b-d455-3b2a-b979-bda5cc7516ab | -15.40717 | -58.78349 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa69fbf8-fc56-3c74-af4c-ae82c04f3f73 | -15.96227 | -59.47298 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68c4db69-14ba-3631-8d3e-897824c4e198 | -15.77394 | -59.40614 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README36.md)
