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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc51d57e-11eb-3478-80ee-e1db4de41325 | 4.0053 | -59.81572 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aac2a76c-042b-34d5-8ffb-86964ef4c2ae | 2.87417 | -60.2663 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a504771a-f326-3c42-ba40-3f6bbca6c75e | 1.83553 | -60.6109 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2eeb33d1-d134-3729-a9f4-dc72d9a5d770 | 4.79364 | -60.28339 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa8c95d4-b382-379f-a154-1c7206bd4466 | 1.94622 | -60.35647 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bfa2184a-6298-36ad-a54e-4a05a8fe0c66 | 1.92487 | -60.37449 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e739ee82-b7d6-36d3-9ce9-c9c4d5d73e35 | 1.94398 | -60.3642 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63ce7a6f-ecde-3b9d-bbe6-b6cb5b280ab3 | 1.8361 | -60.61456 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0c388ea-9bd5-3661-b019-e0d6d3befcfa | 2.71159 | -60.2432 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29b537bb-e430-3ff5-8bb3-e32385153d67 | 3.15292 | -59.98014 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35c62b51-c2d0-3169-b745-d81ae1ea4cc9 | 1.92936 | -60.35907 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef72f910-01d9-3c32-9ae6-c65d1f484d66 | 3.1927 | -59.94845 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe169d0-0a3b-3488-ae03-68dd708ffe7c | 0.90591 | -60.0603 | 2026-02-24 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b8a2461-22f1-32ec-8830-ac3bf83653e9 | 4.007 | -60.35002 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74a50abd-d100-380b-bb88-d129523ebfd8 | 0.05337 | -60.98447 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e789ed3-0e3e-3039-bab5-56c39f184e08 | 0.06073 | -60.98711 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df94a1a7-a43f-3394-86e5-335c02c1b482 | 2.71216 | -60.2468 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22c195b1-05cc-374b-8a49-5f465f6cd75a | 3.28116 | -60.01576 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7009fdf-e4b1-31c2-ae9f-541709990860 | 0.11065 | -60.72049 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404f7712-e3a3-3413-898f-7d1955081dea | 1.19495 | -59.97216 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27159625-b50f-3e5f-a85b-a1c64c91dd1c | 4.79655 | -60.27949 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1ae52a5-d656-37b7-a9b2-573d64b77ba2 | 1.82685 | -60.85022 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1b12010-9564-36bb-9073-a9833670348a | 4.34176 | -60.17312 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc376129-1a1a-39d8-9b4c-eba1ffb9852b | 2.54522 | -61.24146 | 2026-02-24 05:22:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 129961d7-795a-3873-baf5-4744dbeaf932 | 3.51214 | -60.39452 | 2026-02-24 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4dc9271-a3f6-3403-9cf5-e4cbbcacfe76 | 3.18934 | -59.94896 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e841b148-75d0-3cde-86f6-9f018a02eadb | 1.94228 | -60.35339 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a42f5ece-0f0a-3844-a1b3-6e277cd9ce51 | 1.94735 | -60.36368 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 255c9aa9-28cd-3fa5-80bb-fe05518416df | 4.7937 | -60.28386 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da72eaff-f3c5-3ca8-8d6a-ff25706e4faf | 1.20761 | -60.6176 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c15e8f63-3915-31c7-8340-2e3695cbe976 | 1.93273 | -60.35854 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb64053e-6364-370d-90db-acb328439651 | 4.33654 | -60.21191 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4f6bc2f-8790-37d7-ac69-aec1fd25df45 | 3.15628 | -59.97963 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c5f87b-851c-3a09-a4d4-8d1a02492ff2 | 4.0104 | -60.34935 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dbe04ac-5389-3390-bf22-7329ad7d2747 | 1.71222 | -60.29718 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 836aaec9-1619-3f80-9167-5ac2434842d2 | 4.33993 | -60.21129 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30baeb0e-6e4f-3403-890f-ff44c42e64b2 | 1.82969 | -60.846 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92203ac8-5977-3edc-9141-af4769463580 | 3.15011 | -59.98423 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12bd06d4-2590-34bc-936a-4c577900b33a | 2.87699 | -60.26216 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad6599f-1035-3dda-80cf-6906d0bc38cb | 3.43234 | -59.89693 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1494168e-61c1-3490-b962-e93405b0d2de | 2.71891 | -60.24577 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84fa0c40-7d5e-30dd-9333-eed89aaf6456 | 2.6357 | -60.58738 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb0e9a30-d17c-3531-807d-be6b69f374b3 | 0.87242 | -59.69567 | 2026-02-24 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb0e4fde-5232-3737-87a2-0cd0f31156dd | 2.71553 | -60.24629 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2af6c25-15b2-366f-916f-209614918ef7 | 1.94678 | -60.36008 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f74f593-2648-389d-82a1-7a320403413b | 0.16219 | -60.48573 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b3c9eb-a6eb-376f-94a3-7a58ebccf635 | 1.20818 | -60.62122 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e180aee4-f8f7-3103-8ed2-5a857e0dd74e | 2.71213 | -60.22462 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dda77e4-3b50-3f04-9242-463a62895a71 | 1.93948 | -60.3575 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1295c37-b7c7-33ff-a6c2-964c41039036 | 1.34273 | -60.06776 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 69d23f73-2d14-3c1f-ae20-976e7784666a | 3.17086 | -59.96276 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f3787f-ce13-3d23-8ab2-639d849fba8e | 1.8327 | -60.61508 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0211ec82-1b2b-3623-9dff-bde96549210f | 1.94004 | -60.36111 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 91b1da30-52a4-3935-9d23-7e0e48d6044f | 3.42898 | -59.89744 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69fd43e1-8c79-3939-a44e-aa214fb3a44b | 1.94285 | -60.35699 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3f4d9b89-6a6b-3135-8053-dd81b1fa507a | 3.17983 | -59.95407 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf1cd80e-a391-395b-981d-2aa9c060beae | 2.87079 | -60.26682 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3f73c37-cc6b-35e4-a5e6-0a3cc16a9d08 | 1.95072 | -60.36317 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80b98637-1931-3490-aa13-cb5dcf1516c5 | 3.6026 | -60.36943 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 120a8b0d-f9c3-38be-b016-6df6c3000047 | 4.28597 | -60.74615 | 2026-02-24 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 034abd4e-7ec1-33f7-b57e-2e806aa2cbda | 0.31268 | -60.44446 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74b2c7ec-01a1-306f-8d26-214066fec650 | 3.14505 | -59.99601 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1cb3458-f843-39f5-8bcb-309daf528cd0 | 2.71931 | -60.23779 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1f6e0bf-28c6-380b-abe4-44553c745b41 | 1.92768 | -60.37038 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2bc46eb-f30a-397a-a99a-3fcd9929531b | 1.92431 | -60.37089 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf4fb1dc-a49a-3022-b24a-ce16085f53ff | 3.18318 | -59.95356 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c560627d-b1d5-349f-b955-c196d7ee0b5f | 1.9406 | -60.36471 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 99b8fa02-c66f-3ffd-99ce-e6fc5b37289c | 1.94565 | -60.35287 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47ba6516-e573-332b-8d5a-201893d5bb9d | 2.7127 | -60.22823 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72b8ae88-cf1c-3874-912f-8eda61f988c0 | 1.22638 | -60.39392 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a01a64fe-30fd-3f6b-8aa3-654804832582 | 1.93723 | -60.36523 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 977118fd-d77d-3d90-878a-ff0be33a2dfc | 1.19827 | -59.97164 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4764c02-af33-3739-8a80-948a706dae2a | 0.95626 | -60.22868 | 2026-02-24 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a324ac8-add8-32bb-9b73-9f3041a8f74e | 1.94454 | -60.36781 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf16add1-d58c-3f86-b714-01929962f696 | 1.93667 | -60.36163 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d99c356c-3df2-3c72-bd63-5a48d6b78a35 | 1.0249 | -60.47645 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 30209bb1-de91-391c-8807-4a6db3091521 | 2.5465 | -61.2414 | 2026-02-24 05:22:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1568226-cff8-30e1-8f3a-185588dfddc5 | 2.63912 | -60.58686 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7415969e-511e-3610-b0b2-cd46cd27751c | 1.20423 | -60.61812 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0142eed8-03b3-3d27-85c8-2a216bea0b91 | 4.00641 | -59.82293 | 2026-02-24 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8e06009-4471-3c50-8083-8159edba8848 | 3.43399 | -59.90765 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adac3077-29ce-30d6-b623-590956998993 | 1.89892 | -60.81621 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 147451b1-7be3-3a2e-a5c2-bf3065177d39 | 4.79713 | -60.28336 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec94a058-1545-3cae-9e44-8ff26a1aef76 | 4.33375 | -60.2164 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142a7e60-8ba9-3913-8af8-82bec9c629e3 | 3.15909 | -59.97554 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d5911e2-56db-3fe7-b389-5a74fcdfee7d | 1.2048 | -60.62173 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8da7da1-80e4-395d-80e0-5ec66f5943c9 | 3.17702 | -59.95815 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0ef0fe-e5be-3823-b6f5-a007010f8d63 | 3.16245 | -59.97503 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f2234ce-8da0-3713-9e5b-9317f2fc66b5 | 3.16855 | -60.44608 | 2026-02-24 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ad0a51f-4edb-32ad-bee5-75fa5fb7684c | 0.31658 | -60.44749 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 285a8b3e-771c-3742-bb09-23249a19f5c8 | 3.19606 | -59.94794 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96021d99-a46b-3b88-a78e-58d92952ecf2 | 0.10784 | -60.72459 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22aaf76b-81bc-3c18-b06d-b43ee3bf5eaa | 2.71043 | -60.2138 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bdf8756a-15af-3d71-ba9d-f4388ebe9294 | 1.32015 | -60.6413 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba958276-70e6-34db-9f26-440652eb1ad2 | 1.9215 | -60.37501 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ac55c49-6f01-31c4-ac31-5efb4e7fa268 | 1.51981 | -60.02557 | 2026-02-24 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bd2b5eb-7c8b-3648-b126-cc0cef68ad10 | 0.05676 | -60.98396 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 232e3454-7cf0-390e-9caa-f82cc6ae8fc8 | 0.06016 | -60.98345 | 2026-02-24 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d3bc634-c490-38c9-bf64-fcc85a1e7797 | 1.92656 | -60.36318 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eee18221-e40c-392d-8855-f9bbf16fafe2 | 1.94511 | -60.37142 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
