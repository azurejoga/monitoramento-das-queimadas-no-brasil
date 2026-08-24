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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97137be5-aaf3-3dcc-95aa-bfddb05e4967 | -12.71727 | -48.40442 | 2026-08-24 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92dbc8a6-79f9-38ea-9069-496581da3ea4 | -18.0805 | -46.93985 | 2026-08-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e4f89d4-3b53-3f51-b3fd-4d37b1bfd608 | -15.27401 | -52.87623 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b6697c3f-c41d-3afa-9c92-ab193d7c2cb7 | -17.83582 | -44.47705 | 2026-08-24 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c867203-901d-31fd-8aa3-f0e89a72fe8a | -15.26629 | -52.84619 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b2bfa6e-87c7-3b02-9dca-d4f85b32d84b | -13.15687 | -51.39682 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8e468b2-8cf5-308c-8a0a-58eb6def163f | -16.41669 | -49.91633 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82098186-a2f5-3860-8968-cb29e10e5323 | -11.86227 | -51.69455 | 2026-08-24 03:51:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f99f3208-ceda-33b7-9727-fc7f75e2da68 | -18.53274 | -47.17167 | 2026-08-24 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b7da03e-51e6-3acc-89d9-698e9e705ab1 | -13.26874 | -51.44361 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d350fa3-ce7a-3530-9939-54fe5e0f48be | -15.22779 | -52.7929 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b6a24a93-595b-3bb1-8b5b-a4c0a84d6352 | -20.64633 | -45.84838 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec4ad31a-fd92-3c7c-8968-f3f4850c358b | -14.32538 | -51.76046 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 34f30d7d-7268-36b0-b4ab-025ff63c2617 | -12.89574 | -48.48798 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9541e103-96ac-3f5f-94f4-d216b255733a | -14.94208 | -52.65575 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6eb4ff0c-2499-3b83-bec3-4333ac6d5a16 | -15.26793 | -52.83889 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed0d116a-8923-3411-9672-44638bf489c1 | -12.10086 | -50.60706 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76493033-c366-3ecd-bd1d-5a19add73abc | -12.89219 | -48.47645 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8191323-6ef6-3034-b485-7799903c8863 | -13.2661 | -51.44435 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a07afa9-271e-3152-a251-e8ebe2544442 | -16.0588 | -50.44217 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8743ea95-8567-3591-962d-c34969b1a7f7 | -14.94233 | -52.65472 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b51bd039-f110-32b5-8514-3e1fdcfdbc19 | -16.04903 | -50.42977 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9b97eb1-cd15-3dc3-b7de-004ec2295d7e | -16.05001 | -50.42511 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c0040d2-9749-3a97-838e-40c53eb5c23d | -16.40001 | -51.82233 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be7f64a3-1fad-3f64-b3f2-c5cde93ccdff | -18.70755 | -43.02757 | 2026-08-24 03:51:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0bf9c711-f338-3fb1-9019-75233b9c9fc3 | -16.3988 | -51.82786 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2dde711b-c711-3ee4-a09b-33cf50719346 | -20.65585 | -45.84285 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b91953ee-7f3a-3614-b89e-ca985be5ca84 | -18.32327 | -47.20088 | 2026-08-24 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a38846e-8246-308f-8875-66b9d8d5614b | -16.46007 | -49.4437 | 2026-08-24 03:51:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac6b08eb-06d3-3fc9-b55a-363cbfafb1bb | -15.35457 | -52.7732 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 90c28560-890a-3754-88d4-9f2cb5e406d3 | -15.35289 | -52.78085 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 531bae7b-a246-38cf-8927-1fa584c5cc97 | -14.80054 | -48.77854 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3deb41d9-1ff3-3ba4-92c2-813ca7286c7f | -16.41484 | -51.84629 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ca75eb2-1e4a-3aa5-b7f9-cfbf1cb84f94 | -14.94586 | -52.67088 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2157c798-0389-3ace-a4cc-9a8d4aa852f1 | -19.28016 | -46.67791 | 2026-08-24 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d34d8857-cf79-3d12-a1b6-217e2eac9906 | -14.34514 | -51.76483 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b1f8863-51ee-3215-b6a7-07258b69823c | -14.33197 | -51.76191 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8eaa5962-340f-3bc0-86dd-eba80f43a009 | -13.16829 | -51.39758 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3dd5138-715a-339a-bbaa-6b016f4950c9 | -16.06474 | -50.44338 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c97dd8da-2979-326e-9559-d163e158001c | -16.1416 | -50.24384 | 2026-08-24 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 037f2fb6-5d1f-389d-980d-27b909a67d84 | -16.41594 | -49.91988 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fc76c13-1c1a-3b38-856d-683a254a5c3d | -14.79631 | -48.77114 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4eafb1f-cd4b-3d41-89ca-d13a44e9639b | -12.86434 | -48.47119 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42270b4a-41ee-31e7-ba0a-e7a0996e04b3 | -12.09754 | -50.62334 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47e0ae6d-a9bc-3a41-8399-cf28db7b139b | -18.33623 | -43.91114 | 2026-08-24 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b889cd0-27df-3f57-8133-7dcefe085829 | -14.95271 | -52.6724 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d762b4d3-c451-3bb9-a71a-92edec83e13c | -15.26612 | -52.8148 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d3715bf7-074e-3272-90f4-f1eff5f318cd | -14.93513 | -52.65467 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 617d0ecb-a17e-3486-9ce1-0af28c27598b | -16.06973 | -50.44911 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 084f7065-e696-397b-91e1-11b5f7814ff6 | -14.37743 | -51.84005 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2f7af62-e4b2-368b-86af-c91cdee4feda | -16.05784 | -50.44677 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4cbf532-1f16-3182-a142-4c0cb5ac92a5 | -14.77861 | -48.77422 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c6ac8865-b0e3-3cd0-b8dc-237fbc0ef2d8 | -14.33983 | -51.75745 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22c74512-9b61-3610-befb-58dec2a8fb7d | -13.15512 | -51.39478 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49b69b7b-bb0d-329c-9c45-5c48847ce2c4 | -14.94083 | -52.66158 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b427d6d4-715d-3e16-9e09-0cc778f9fe3d | -12.89262 | -48.46803 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81fec02b-53bc-3388-8fbf-593d4fdeb3bc | -12.89197 | -48.47127 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 584abe5c-0f81-3a3d-8fac-fbee9e8b6e32 | -20.3304 | -46.61005 | 2026-08-24 03:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b9b92db-bc17-3581-877e-661a61e671f8 | -16.40936 | -49.92276 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38fa3ed9-a086-3ec5-bec8-b1e4976653e3 | -12.89301 | -48.4948 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e503d637-80a0-3b5d-91a1-a690d55cf38f | -12.58487 | -47.94859 | 2026-08-24 03:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f9c0bbd-b24a-36f0-b43f-88beb0fa231e | -14.93357 | -52.66154 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2e9101b6-5927-3159-a8e2-1481a7e9d795 | -17.42724 | -48.83958 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d26e1473-09d5-32c6-b12f-3cb4e1e515b6 | -17.43767 | -48.84194 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8ca3e560-c0da-3308-a442-6336744a4057 | -15.35815 | -48.23201 | 2026-08-24 03:51:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7cc06f1-126e-3a71-a0d3-dd83f6320ba6 | -13.44531 | -43.84569 | 2026-08-24 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 292bd3b5-0190-3980-8d43-20cb22f3dbac | -16.42057 | -49.92611 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16ec3246-80b8-3003-910d-a83fbc3800a8 | -15.27969 | -52.81864 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aea802ae-8870-3d44-bb10-c265204df234 | -19.15896 | -44.40494 | 2026-08-24 03:51:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 044653b0-71f8-3fb7-8f7f-177aca21e222 | -14.77802 | -48.77722 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d9a2aae-a258-3999-90d1-133b14f68814 | -12.86216 | -48.48235 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc89c408-44b1-36ba-9dbe-50398a12244d | -15.12229 | -42.9206 | 2026-08-24 03:51:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ef74c131-fd3a-387f-a1fe-d430e505a3ee | -18.44837 | -48.41662 | 2026-08-24 03:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8257ea51-226a-3ec9-8423-7325868091ab | -16.86522 | -49.44831 | 2026-08-24 03:51:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a5f6a93-d2b3-34d7-9d27-3cb19507d8dc | -14.78476 | -48.77198 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f35b754a-b505-32ce-a613-4fb52f2459ad | -14.39122 | -51.77503 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd1d3220-5656-3468-9e0c-e133feff429e | -15.28622 | -52.82172 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be6231e3-bb67-301d-a47a-91edd93eacad | -17.42867 | -48.83263 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| eb4a981a-5378-3c01-8529-bcbef96886a1 | -18.07344 | -47.28752 | 2026-08-24 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 102f33da-9474-3708-abe3-c23eb665f702 | -20.23203 | -44.20615 | 2026-08-24 03:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ef0e26b5-36b0-34a6-9c6b-d72f21ee3b99 | -20.64298 | -45.8437 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4bb2934-0c12-353f-80d3-561249517e04 | -14.94053 | -52.66262 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcb02c3a-d898-30e8-b580-649c50bb64b9 | -15.12536 | -42.92256 | 2026-08-24 03:51:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eea8bf4f-9c30-345a-a8ba-fa4082a842f9 | -18.70907 | -43.0269 | 2026-08-24 03:51:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4c8507f0-39cf-37a1-9cde-0ef8a1ed1ac9 | -13.17004 | -51.39967 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c62f250-a351-382a-8a3d-e73dedad92cb | -20.32617 | -46.60877 | 2026-08-24 03:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33db15f2-229b-3f4c-8b8c-e586841da04d | -17.422 | -48.83851 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 587cffc7-b8fd-34a3-8253-bc6acf52fd66 | -14.93389 | -52.66048 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1550e34-bb02-3a4a-b9a6-c6521f56a49e | -16.38606 | -51.82496 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18d6db6f-45eb-373d-b836-ecaf8320eed1 | -16.02344 | -45.52148 | 2026-08-24 03:51:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70a3a175-edee-3922-8191-69c616dca570 | -12.89461 | -48.48684 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4628c68a-ba15-325e-bd0a-37d5c2dbce12 | -17.18034 | -44.43575 | 2026-08-24 03:51:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cebf0ee1-9ea4-314c-896f-062ba1417551 | -12.71857 | -48.39784 | 2026-08-24 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76d8a041-c411-3d08-8c29-2ca283f42ffb | -16.14066 | -50.24825 | 2026-08-24 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9c4b5af-bb8b-306c-97f4-b5a80b0153aa | -16.40636 | -51.82386 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b876e19a-5590-32f3-bfe0-8bee93492ca2 | -20.65178 | -45.84197 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b1bb617-ce25-30f0-b075-72480a8de997 | -20.63825 | -45.84629 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 165861e3-fc48-3560-a069-cd7a3c7947be | -14.78524 | -48.77177 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 697cee13-ef85-3bb4-900c-0debeb809814 | -19.01354 | -42.12798 | 2026-08-24 03:51:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ce76df76-1420-335f-b561-bf26b08e625c | -12.86113 | -48.48763 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README14.md)
