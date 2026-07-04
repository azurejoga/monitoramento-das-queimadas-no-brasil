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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b3b5eda-3f38-39f3-96c4-cc52da089bd6 | -18.36717 | -47.57225 | 2026-07-04 12:08:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a1c82e20-ad0f-3529-8e7d-6a021ffff172 | -15.70072 | -45.57796 | 2026-07-04 12:08:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| da6603f4-9a29-38d5-adaf-174d8fb9df48 | -15.69481 | -45.60653 | 2026-07-04 12:08:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1af80dbe-c116-3d55-bd64-902b1c3cab2b | -15.69717 | -45.58432 | 2026-07-04 12:08:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| de10ee66-b7b2-32d0-8c3b-7a7d6a7d8461 | -15.69818 | -45.6002 | 2026-07-04 12:08:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 9f3b6786-25f2-37f2-9bac-796b05657579 | -8.6912 | -54.6682 | 2026-07-04 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3ea16774-0165-3521-9d45-e1087d62f3d1 | -11.333 | -46.9024 | 2026-07-04 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ec71b70a-199d-3338-820e-366707624a46 | -13.2404 | -54.3303 | 2026-07-04 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a9377996-6099-329f-a781-79d9b2332f4e | -11.333 | -46.9024 | 2026-07-04 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b1cb09c8-9c11-39c0-bac2-7d3c6ed44a9c | -13.2592 | -54.3489 | 2026-07-04 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 969f412e-9815-35f4-a6b7-faeb4f8b2bdd | -13.2595 | -54.3283 | 2026-07-04 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5d3a87a6-f33d-38eb-ab43-ad5900ca01b7 | -13.2401 | -54.351 | 2026-07-04 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b66a5dc4-de71-3d66-b0eb-3ac1857611cc | -13.2404 | -54.3303 | 2026-07-04 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3f040396-d3a5-3bef-93bc-a9197c03d121 | -13.2592 | -54.3489 | 2026-07-04 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| cc5dfcb5-d49e-38e2-98f3-3e1cd008b265 | -13.2404 | -54.3303 | 2026-07-04 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1d52dd99-1321-3b32-8675-7e759ced31ce | -13.2595 | -54.3283 | 2026-07-04 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 662cb024-d141-3564-bf50-44cadba0a866 | -13.2401 | -54.351 | 2026-07-04 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ac312fc6-8d87-3311-9c7b-f1b2b0f8be41 | -13.2592 | -54.3489 | 2026-07-04 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| fda96915-6272-3a68-9fb4-c41c6b960aee | -13.2595 | -54.3283 | 2026-07-04 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| cf9b5324-6b2f-362a-8ae8-7e1b102e2b0d | -5.9812 | -45.0903 | 2026-07-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9fc939d7-724c-3131-9c54-c7a7fe35a153 | -13.2404 | -54.3303 | 2026-07-04 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ff05c6e9-517c-3a61-8017-193b62db77ce | -11.4341 | -46.5517 | 2026-07-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9f972acb-5675-3c8d-9aaa-363f465befee | -11.4337 | -46.5743 | 2026-07-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 06d09f4e-0948-3ae7-b466-942963a9d674 | -13.2404 | -54.3303 | 2026-07-04 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| b2a10984-6828-3f69-95aa-422ef7b8093f | -13.2595 | -54.3283 | 2026-07-04 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 863f564f-2499-3b69-90bf-0ba0f7e78b60 | -13.2401 | -54.351 | 2026-07-04 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f183ae03-a383-36e4-a2a5-29b9e66797f9 | -13.2592 | -54.3489 | 2026-07-04 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1da69478-64ad-38d1-bb5d-75fa75f5a489 | -11.333 | -46.9024 | 2026-07-04 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 06281b94-40c6-3444-b2ac-c16fc22c6b6d | -13.2595 | -54.3283 | 2026-07-04 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| dbb34c23-20dd-3e37-9e9d-76645524d266 | -13.2592 | -54.3489 | 2026-07-04 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 37ff9b96-eaa8-35a2-b6c8-fcffbec28b9d | -11.4337 | -46.5743 | 2026-07-04 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 509caca3-5fff-3872-9b1e-c7358485f996 | -13.2401 | -54.351 | 2026-07-04 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 575af319-455f-38d7-b525-6d2fe8b6988f | -11.9305 | -43.3812 | 2026-07-04 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 92ba93fe-b569-3528-bfc1-e822fc430424 | -13.2404 | -54.3303 | 2026-07-04 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 717a3a6d-1fb9-3be0-bdf0-7bd2c36415e7 | -13.2404 | -54.3303 | 2026-07-04 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 2e863eb1-9683-36c9-84a7-ac53483b88cf | -13.2401 | -54.351 | 2026-07-04 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| ada1f5bc-3fea-3731-8ca6-b47f52f7adcc | -13.2592 | -54.3489 | 2026-07-04 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 04eb3204-83e8-3146-9084-bf17033b4663 | -11.9113 | -43.3843 | 2026-07-04 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| e4bdfbc4-6b29-31b9-a316-543c39c02c6d | -6.014 | -47.7558 | 2026-07-04 14:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3f2b3ffb-9ee3-3604-98d5-1ba0f80dec4e | -13.2595 | -54.3283 | 2026-07-04 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 3e6bd55e-c3b0-3bf1-bb8e-4b727855134a | -11.333 | -46.9024 | 2026-07-04 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ead6a7f3-580a-3b79-a136-73e616a52391 | -11.9305 | -43.3812 | 2026-07-04 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1a0dfe41-f0f1-33eb-b023-cffbff46462f | -6.9323 | -43.7264 | 2026-07-04 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fdb4ca64-0359-37ec-a244-38d3db0663c9 | -8.0315 | -46.2457 | 2026-07-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b987062e-54d2-3f69-b8b6-f89b1b534c56 | -6.014 | -47.7558 | 2026-07-04 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 20b27588-003c-364f-9c6d-5db926b07133 | -11.9305 | -43.3812 | 2026-07-04 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 996ce0f6-7a20-3714-916a-592835128782 | -11.9113 | -43.3843 | 2026-07-04 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| b65041b7-7d14-3042-8814-d0f1ef1d2c91 | -16.5215 | -47.7257 | 2026-07-04 14:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a97d2ee5-fa0f-365a-860e-67fc9ca38ccf | -11.333 | -46.9024 | 2026-07-04 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |


