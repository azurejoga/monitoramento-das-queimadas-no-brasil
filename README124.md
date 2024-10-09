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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75f0cf51-c3d2-38ff-b2be-3bfcac41d4c5 | -4.00949 | -46.53766 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef3572a7-c9e7-33fb-a20f-c07f84d05372 | -4.00891 | -46.54146 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcb511a5-c0cc-39b6-8036-e5a53f7c850c | -3.99938 | -48.38078 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 548d0897-32ed-33cb-b8b9-7f30e898e409 | -3.99884 | -48.38424 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0582fa7f-d5ce-35e2-beac-659db0f0b9eb | -3.99192 | -46.06646 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84f38cd-9cc2-3c35-a9a1-f134ef7ae2bf | -3.98833 | -45.34185 | 2024-10-09 04:38:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dbe0240-4b28-3fea-b0ba-720997ac3844 | -3.96539 | -50.05035 | 2024-10-09 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38292e9f-e96e-384f-b328-a14ef41be0ab | -3.95425 | -49.03587 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a57b006-5126-3b5e-bec4-ca8c8c7162ee | -3.94404 | -47.96225 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d68f2fa-6841-3a36-bac3-389c6a890cd9 | -3.94349 | -47.96576 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9216ab6f-2b64-386f-a51d-dcde7ca0b430 | -3.9407 | -47.96173 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f07e505-c47a-3f01-b5f3-8b0918a73ee8 | -3.94015 | -47.96524 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85ed7bd6-fddd-37d2-be11-2fc2ff49067e | -3.93973 | -46.4497 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5270c561-8bb6-30d1-911a-b74b765ab810 | -3.93914 | -46.45351 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 43908d4b-c9cb-305c-899d-1c0b03065175 | -3.93735 | -47.96122 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7a6b333-52e7-3616-80e5-8f8c2d0745d1 | -3.93688 | -48.95167 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db897e03-42f1-39be-abaa-bef9d7762ec4 | -3.93681 | -47.96472 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e72f02c-2771-300b-bb84-7108fde021ff | -3.93624 | -46.44917 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a062e80c-678c-3999-b8a7-016a08b0cf08 | -3.93565 | -46.453 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d11dada7-a805-34fb-a6b7-537a0ad927b5 | -3.93507 | -46.45675 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58f31b94-58aa-3bbf-9fef-60a81aff7ea1 | -3.93335 | -46.44481 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 17029832-7860-3f0b-963b-dcb448e94055 | -3.93276 | -46.44864 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7fd56aff-6eac-3fc1-a8c8-e8ca98146de2 | -3.93216 | -46.45247 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c164fd88-1fb0-3d6d-aff7-345bde87be2f | -3.93158 | -46.45625 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f61a33c0-356e-34ae-9e9d-27f52eea9f14 | -3.93106 | -46.43659 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9f8faa6-f047-388e-9a85-3907a5963e48 | -3.93046 | -46.44043 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df80869a-e96b-31de-b170-64897b9c2216 | -3.92987 | -46.44427 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9083956f-c521-36ad-b94f-0eed7042af72 | -3.92927 | -46.44811 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 63104c7e-d8f6-3e70-bc6b-f5e14a010dcc | -3.92868 | -46.45194 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e3f3fe51-e362-3f58-9e58-19ad14799b21 | -3.92809 | -46.45574 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 60bf748e-8163-3afb-8170-5bb5697dc51e | -3.92638 | -46.44374 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 50da56dc-4709-33d0-ae60-6a9caab5d48e | -3.92579 | -46.44757 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 79f8ad6d-6407-3319-ba5d-47600a00754c | -3.91949 | -46.41903 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 711d945a-ac20-37a8-b2db-b1296777d9d8 | -3.9161 | -45.32741 | 2024-10-09 04:38:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a201884e-3168-3aa7-9406-1751387dce9c | -3.91321 | -48.34986 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21d00f7f-801e-385f-aa66-6261fe68c204 | -3.91074 | -46.42954 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c64ce94-71db-3eca-b892-895da15a623d | -3.91068 | -46.45307 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f1ae850-2ea4-3400-af28-8c42a753a710 | -3.91043 | -48.34588 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6d2d41e-3366-36e0-88ad-d1546b12bcde | -3.91009 | -46.4569 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| acedde84-b6e2-3fc1-8339-be49feaff95e | -3.90989 | -48.34934 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df568314-c014-3f6b-887e-fa4005bba278 | -3.90935 | -48.35281 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aab0e3c9-53b3-3e83-b5bb-a3bf2d33e550 | -3.90765 | -48.34191 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9a625b7c-093f-3ec6-82ec-c2d49cf64ab4 | -3.9072 | -46.45251 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2d12fab-f975-361c-b4e4-184cd4548743 | -3.9071 | -48.34537 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5698e8e6-3653-3fd7-95bd-e6f5c9893f55 | -3.90661 | -46.45634 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89340e46-eb6c-3531-901c-f5893d6395f9 | -3.90656 | -48.34883 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7845efe7-219a-3d27-9954-f4ff3cba9fc2 | -3.90602 | -46.46019 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6679cec-0d83-3b5c-aaae-dc8bca665e5e | -3.90543 | -46.46402 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa9fe169-2327-372c-bad9-8e1bc9b3046b | -3.90432 | -48.34139 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2405c6dd-362c-394a-bbf0-4368a2d14a19 | -3.90378 | -48.34486 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dd2e3dd-8902-3e5a-9e42-55393a231a50 | -3.90313 | -46.45581 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0e9ad956-1e17-328b-8a04-5f7eaff68a63 | -3.90253 | -46.45965 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b59108ad-1869-3530-83ef-8ea257363b00 | -3.90248 | -52.31556 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2005215-5854-36b2-a1bf-6e41e8393f9f | -3.90194 | -46.46349 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 333c79f8-755a-3393-9700-9a5a01027c5d | -3.901 | -48.34087 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cf1d40e-8c5e-3d76-9cd9-9e4d4e49f9d5 | -3.90045 | -48.34434 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a7a04b-5e91-3420-8507-1c5b729ffc1f | -3.90043 | -52.38515 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 946e6d2f-b6bf-3d4d-9bb9-77a09ebdce81 | -3.90023 | -46.45143 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ebe462e2-f42d-3e42-a1da-df2e1357c301 | -3.89964 | -46.45529 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a59eab0e-2e2b-3657-b468-ba9ad87779a0 | -3.89905 | -46.45913 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| beb129ab-d091-3b78-ac95-fc9c030b68b5 | -3.89767 | -48.34035 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc2391c4-98f6-3b6f-859d-ab538d658dc7 | -3.89713 | -48.34382 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c858c57a-580a-3c7e-82e8-0e862ca39e23 | -3.89675 | -52.40749 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14467247-db8b-31c6-aa51-721b5ec88729 | -3.89675 | -46.4509 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5c84dbe6-1631-3fa8-bffc-9b462a05e694 | -3.89616 | -46.45478 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4f019216-acef-3140-9089-e766997f2ff5 | -3.89557 | -46.45861 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5efd0b64-9ce0-3163-a82c-fed8ca6935f2 | -3.89522 | -52.40942 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 324d5444-3de2-3500-913e-1883cbd66524 | -3.89173 | -48.36013 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c0a0fd-a18e-39d3-88dc-c2b4ff88cc21 | -3.88895 | -48.35616 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cba94504-7cc9-3574-b87e-c17562afad1f | -3.88841 | -48.35962 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c38a7023-e67c-3f93-a024-482307bf18e5 | -3.88833 | -51.9353 | 2024-10-09 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69c093b8-38bb-310a-9fe4-8ee11ddeb943 | -3.88465 | -49.98669 | 2024-10-09 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0942916c-9051-3b71-8ff8-d1da77a53684 | -3.88409 | -49.99026 | 2024-10-09 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcc84a28-0b2e-358f-8d3a-b21da710600a | -3.88352 | -49.99383 | 2024-10-09 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0578f8eb-b159-3de9-bc89-a608bef8dca3 | -3.87204 | -51.18964 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35e518c0-ad85-3b9f-a991-b5733065ddc8 | -3.85094 | -46.46439 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cae0710d-cbd5-3a73-bb4a-0ee41f4a2288 | -3.84746 | -46.46389 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17617d1a-8011-3d8b-8dff-179d7220dc94 | -3.84728 | -49.4533 | 2024-10-09 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b3e9c3c-c1a6-3709-a17e-61e8774e8614 | -3.84394 | -49.45277 | 2024-10-09 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff05eb92-c1a7-37c8-b01e-27972371241b | -3.84339 | -49.45626 | 2024-10-09 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ebaccf4-3e61-3f32-aba5-c4d73887939d | -3.82663 | -52.40755 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a46d634-8e64-3a49-a2ea-2d079607fe5c | -3.81245 | -47.48767 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eb6b08e-9d9b-3b06-91a0-18f322d65d82 | -3.80916 | -49.48696 | 2024-10-09 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc4fcc61-2ea1-315a-a998-885df2d97304 | -3.80908 | -47.48715 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61bc53c9-e4c6-3193-949e-ee8dc7c08cb0 | -3.80861 | -49.49046 | 2024-10-09 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb9503a6-fce0-320a-ac87-fa54c3c1f142 | -3.80852 | -47.49072 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20d2ab76-5fc6-30d7-9112-93add45ec092 | -3.79559 | -52.21477 | 2024-10-09 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd92977f-9c62-3e7d-92e2-0fb49933119a | -3.79311 | -52.42511 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db47dda3-2f83-3fa9-9796-ab228d8f7836 | -3.79248 | -52.42646 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 251b5a21-6389-377d-877a-5a8895344203 | -3.78937 | -52.42452 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c6b0f30-ad9b-392b-b099-aa0e814f4790 | -3.78874 | -52.42586 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a3f8d9-ec1e-3072-865d-a2973ab3b8b0 | -3.78494 | -52.25772 | 2024-10-09 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4eb675b-9f0f-3c2a-9525-81c0e33da8a5 | -3.74983 | -52.31052 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a160da30-ac4e-36a0-a6c5-48622e146791 | -3.74912 | -52.31492 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3517b71-b46a-3c9a-b117-67fd496fe101 | -3.74539 | -52.31437 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46a2ffdd-666b-3818-913f-a923a51e63c8 | -3.74167 | -52.31378 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a6edab-d68a-3ef1-bd97-8fbbc345fed0 | -3.70453 | -50.17236 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f4b74aa-c2dc-32ec-8dc2-2eb3e069c52c | -3.70396 | -50.17599 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2250df64-fb3e-33c2-97eb-eb3018906848 | -3.70226 | -47.59782 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb731c86-2af6-37a4-81f6-c21e5084221b | -3.70171 | -47.60135 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README125.md)
