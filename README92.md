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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d92e0d5-44fb-3ed1-adc3-5d43d582a3ed | -9.48614 | -55.9729 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2c05fe9-ad6f-3427-82e1-e459eb1bfd1e | -11.42327 | -50.7389 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 10c27f37-ad63-3c9a-bbc2-ea0a98be51c2 | -9.49391 | -55.96693 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6ad3e61-42fe-39b6-879c-cfd15c6f324e | -13.77558 | -46.2904 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 857d7751-ea3b-3640-a15b-73941cb9de8f | -11.99488 | -47.76754 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7ee7f6e7-4c01-35ea-9c18-af2822ef00aa | -9.90636 | -57.06002 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a233426d-692f-3518-ad15-d8d0eac6938d | -14.21762 | -46.25066 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f4b0c0e-fb84-3a46-a432-364f79664cb0 | -9.81076 | -61.5248 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4accd2b-d01f-3bf4-846c-13bed9cb0f1f | -9.26572 | -59.41212 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 8e5551d0-7483-3f02-8aab-8936d9f36bf7 | -11.15968 | -51.37735 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 487071eb-1aae-3c82-b52f-bd5cced003d1 | -13.00432 | -47.99366 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d8ae558-a932-347d-8405-57748c687b10 | -11.09701 | -51.43899 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 3f9d9548-c86e-3542-911a-bf3a1a86129d | -15.55601 | -54.78704 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abcdcdb1-fc46-39c9-b9e9-50b8aa5f94ec | -12.49557 | -53.8826 | 2025-09-13 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 944b5a19-cedd-3b85-8583-cf904f084480 | -14.44004 | -48.43896 | 2025-09-13 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 61e8570c-78bd-3060-bf54-20c76793d4a6 | -11.5706 | -50.57239 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1e75703d-2f3e-36a4-a0fa-df5b259df6b5 | -11.15901 | -51.382 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 31366520-4e1b-3e30-ba6d-b20f12ffe444 | -14.13143 | -45.37082 | 2025-09-13 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b022921c-1f72-3e43-aed3-f80b27764aa7 | -15.17858 | -53.82541 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19e0d9e3-0b69-3a45-af9c-59945c9952a1 | -12.10669 | -47.58165 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f38fac2-ee74-3c03-8e65-38ef4956b55b | -10.42101 | -50.60236 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7dceae14-89b1-33f6-a111-115e65c639c2 | -11.40103 | -50.47251 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 359e107c-9ae2-34ee-9df5-244e808e2fb2 | -11.8674 | -50.56443 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 32d1efff-48f2-35bd-af4e-a2f537a77c20 | -15.71668 | -50.58294 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b17d9581-889c-3c9c-aa8a-c1781e044c7c | -10.76764 | -50.52784 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0e9784f-3067-3f2f-86af-6788872e2418 | -14.419 | -46.40386 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c303c89-245b-3ff9-ab71-b1de6a801737 | -10.79232 | -56.29813 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a2e2822-26d6-3390-8864-cc7da7c1b990 | -15.7836 | -52.24923 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9080ec5c-8c68-337b-a533-0ecd89b5a42f | -9.11511 | -59.49535 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71873d09-eaba-3721-bb2a-a704f6117180 | -15.79076 | -52.22539 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe506ebe-24bc-3742-8d4b-4ceb2c7cc345 | -13.77683 | -46.28505 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e181649-11d2-324e-83e9-21f0ac39751d | -10.01774 | -51.72308 | 2025-09-13 04:59:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c2f5096-7e10-31d3-8119-fdbb83cb50a1 | -11.38097 | -63.35826 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f5d9cda-ac9b-3b0a-a6a2-c3690b2861cd | -14.41356 | -46.40266 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c1e79ab-d67f-3590-aa6d-c4dfbeb5bef9 | -10.69256 | -49.1725 | 2025-09-13 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0afd058a-a8e0-32fe-bff5-5b9ed75ca005 | -12.97285 | -54.74807 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9acca03-c6dc-37fd-b812-e24701ba0e26 | -11.18158 | -55.08115 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d139ed2d-3126-34e0-a0fe-2d555552359d | -15.07258 | -48.01695 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2c4d778-ac08-36d7-b64d-3e2b82c3e6f1 | -11.57459 | -50.57298 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ba5274fd-2b81-31e3-998f-6da6a5b1a6cc | -9.8378 | -54.53339 | 2025-09-13 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 234345e0-e6c7-334b-9d03-4de298aac2c5 | -11.73176 | -46.58247 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae6ff1b5-3f8b-3b07-b648-2aa843f8bcb6 | -11.76356 | -51.50955 | 2025-09-13 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d55a038-8c62-32be-a0d9-1c4d6b8137f2 | -11.15524 | -51.38143 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 593abe45-fc08-31b5-bfb6-7f779dd0b5a5 | -11.83089 | -50.54904 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7d568df3-15b7-31a8-ac4a-0fc883a97e84 | -10.91332 | -55.75037 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8606bbf-138c-33be-956b-9cdb892986c0 | -9.29188 | -60.18538 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674bcf5b-4c77-354b-a5aa-89f33e50f35a | -12.92217 | -54.74799 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9449dd39-e973-3f93-b2cc-f03e6c74aa90 | -10.52932 | -51.54253 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 34a62c35-b48c-3484-937d-8d01b999b657 | -12.94014 | -47.9954 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 798329ce-fdc3-3839-b0e0-7ee78653a618 | -10.50454 | -51.53025 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 236c84ba-3217-3210-9941-6cf24f6e16b4 | -15.02737 | -50.14387 | 2025-09-13 04:59:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8870ab6f-b39f-3dfe-9370-c4e84d575223 | -16.55803 | -49.2229 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3afd5fd5-976b-31d5-a45c-734ab25449ff | -15.29289 | -53.78481 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b5931e6-b652-37e5-8bd8-5a1d14071d10 | -11.81486 | -50.5467 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 224c3126-a8ae-3341-84e3-d12367d54a73 | -15.14715 | -50.11705 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67602af8-1add-3764-94de-0d2b5b999f26 | -12.12677 | -47.59778 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0228f00-21a2-3917-becd-22e07d81a2ee | -11.11967 | -51.33325 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35cb40b4-1707-3526-85df-8422004e4f40 | -12.11043 | -44.8871 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59780301-69dc-3139-8a72-ce0bda02edd4 | -14.19642 | -46.28951 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c8811ff-4e2c-3d74-b703-5dda6c90a009 | -14.21624 | -46.2641 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b19af9cf-8401-3c91-a6ee-00ecadcd07a5 | -14.43079 | -46.39811 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1794a268-1da9-39e4-9708-6bfffc2b6ce5 | -14.29374 | -46.07653 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67ebaed2-0bb9-3a83-ad86-b60cc9780224 | -14.1829 | -46.26159 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fa83e716-6355-3ed4-8e30-4fca8cb951d7 | -10.78924 | -50.5468 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ed30e21-dc6c-3fb7-9b6b-f43dbcb80d37 | -9.25495 | -57.06679 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea8fa21-ed51-3e99-ab58-d7025c6025ac | -12.93218 | -54.74957 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 406d10db-2ebe-3175-b886-34aae337ce28 | -11.12345 | -51.33382 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e17ba6dd-fbc5-301d-b876-d076eade9bd8 | -12.92551 | -54.74852 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e87da31-f9e5-3751-ad9f-542458fd609f | -12.11201 | -47.59597 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 368471f4-0742-3f1e-b02f-fddfac561cbb | -12.00117 | -47.75724 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 11f1c7c0-f6df-3bd4-b86a-468513e6df82 | -13.119 | -56.79863 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97d03a5f-f905-3879-8c7c-c8ead0cf4824 | -15.86662 | -51.84749 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c296302-f813-301d-bc25-caf253505c90 | -10.52747 | -51.5289 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9dbd496-e665-3322-8d5e-65986ef1c328 | -12.86534 | -62.14078 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dadbf796-2cd5-382e-add9-4ce493a7b85f | -14.22145 | -46.26665 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08919ba8-1ef7-3742-870b-265db2bfbb91 | -16.28333 | -45.68106 | 2025-09-13 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4746a9e7-a7cf-3796-b44e-0d2bf97cb8f4 | -9.24385 | -60.41496 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a815361-df1e-3a66-8eb0-6478a6e75a53 | -14.1909 | -46.28888 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ffa20d9-c634-3420-8033-4853d2b2036b | -14.28387 | -46.06346 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cedc1b45-2f19-31fa-ab29-54cab584549d | -9.79838 | -61.5182 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d011792a-99f8-3c68-97e2-6d66b52a2074 | -11.60865 | -52.22853 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccbea5f6-22ea-3a15-a8d3-3e017c58c4fc | -11.64053 | -46.91895 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20fc2ac0-ca53-3fa8-9978-bfac7e049a5f | -14.73632 | -60.23093 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eae7da6b-3349-3872-bd2b-cfb2f0b73b9d | -12.17113 | -60.74874 | 2025-09-13 04:59:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc4d660-22ed-3756-8e02-860a74d19661 | -14.44049 | -47.33751 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c26c898a-3f06-37d0-b859-150d2d996f92 | -11.45302 | -43.57251 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 002358a8-b6cc-3118-82b9-fa6c522bb29c | -9.27665 | -59.39401 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88067a1a-b09d-3339-9053-603869b75727 | -9.49002 | -55.96992 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c39dd77-331d-3bb1-8f6e-57746f4cfad1 | -12.89692 | -62.08979 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3548f698-1f38-37fe-8fe4-50f20cdd776a | -12.99329 | -46.75103 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5762abf3-294c-3935-b0d6-3dfafe1c43cf | -11.78293 | -47.40185 | 2025-09-13 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c9ff587-c34a-321c-b3e4-7652f0e79219 | -16.40738 | -49.04916 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f9e6d82-353d-3f1f-aea8-71c0db402464 | -11.18711 | -51.43094 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 450f475b-ab39-3211-b594-a748f57565fa | -11.71361 | -46.55279 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| da158f7a-17d9-3532-888f-6ab3e6c1d090 | -13.40899 | -46.80122 | 2025-09-13 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b19c7ce-6e6c-3bb4-a121-0b6e7db2f5be | -12.8015 | -47.97876 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85355868-1951-3aa7-9fc9-0bd41068f0df | -14.44784 | -47.31935 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a850fbc4-0962-38a0-a487-744fdf3024d4 | -10.91168 | -55.67479 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fde4efc-cfb5-3f89-8e6a-41d12afbb264 | -9.2445 | -60.41121 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f25cbe47-7cdc-3409-8bdf-2e17fea978a7 | -13.45776 | -51.77616 | 2025-09-13 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README93.md)
