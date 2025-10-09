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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a0c093f-6934-3c4b-8f8d-bedc41f99ca2 | -15.37096 | -47.33524 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e23ebfd-4731-35e5-80a1-10bd68ea8ba3 | -11.76923 | -45.15019 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f598ece7-c6a2-3ab2-acef-dbfceab8d06d | -16.37727 | -46.38509 | 2025-10-09 04:00:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d8673b5-9d5c-3880-99c9-077ac171fd3a | -14.79656 | -46.08966 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf416bc4-f628-380c-9527-de7ca7a615db | -15.31767 | -43.85004 | 2025-10-09 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54f13c3c-4a07-3702-b829-b0bce9556875 | -15.07706 | -46.60698 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0dd8728-9bec-3380-a01e-835e15f0bcd1 | -10.87471 | -50.95874 | 2025-10-09 04:00:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc595c7c-4e46-3a62-86ba-c05310498fb3 | -10.85447 | -49.92028 | 2025-10-09 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3815a7f2-a51e-38ab-beaf-fef0df580c4b | -14.83875 | -48.36453 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d418c060-7b96-3be1-be6a-de0c3a750c20 | -15.06509 | -46.62303 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d73a094-ab16-3d98-a509-65ad736dffcc | -12.86582 | -42.62683 | 2025-10-09 04:00:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9182531-9b20-3051-9ce0-8087bb1a0cdb | -13.48282 | -42.02052 | 2025-10-09 04:00:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec26e4c9-4a21-3d82-b141-c1c88c5dc453 | -13.79367 | -45.83821 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29a07d01-cb8a-3318-9e57-b2da864ca16d | -11.77825 | -45.05295 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 403773e3-da14-37a6-9155-5a0c9c1b1c6f | -14.96601 | -42.85476 | 2025-10-09 04:00:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc688f3a-a399-3071-93b1-69f5c998a547 | -11.87569 | -44.93359 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6945eb15-3ddc-3e12-afb0-8a8f6caeebf9 | -15.05942 | -42.33429 | 2025-10-09 04:00:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 0386be3e-8ddd-3073-96b8-2ec957577114 | -13.79434 | -45.85869 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02e91f7c-42b2-3181-b3d6-d9145b40df4e | -14.43603 | -47.50437 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 493ec716-88ca-392e-8aab-bad13757a0b5 | -13.79072 | -45.87818 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 99df22ec-ecfb-397b-9f5c-d6102980a3f0 | -16.29038 | -45.24494 | 2025-10-09 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 576325dd-ae27-33a6-8187-82ffe38c7835 | -10.52898 | -50.02464 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 23ca639e-098a-3310-a8c5-d6a1f99a914f | -11.78168 | -45.15247 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 707eea7f-c690-3d3e-9ea1-2f5672fe1e97 | -12.43522 | -45.72929 | 2025-10-09 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89478ff3-edfa-38eb-97df-c0cd5d70f4c1 | -11.86068 | -44.92308 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c89a20ec-8a7c-3d52-8981-5a827832a0d8 | -10.85528 | -49.91621 | 2025-10-09 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6df5cd8-34c3-3f32-8124-de2a0d8ada40 | -11.65869 | -47.52828 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 800afda0-3923-391b-a968-b29999e6afb3 | -15.22165 | -46.37493 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90b33741-5c4d-3458-97dc-1a54c14e6033 | -10.52233 | -50.02765 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab6371c5-f5d9-39a7-bf9a-ed751137db15 | -15.07625 | -46.61131 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2130b27-a527-3d19-ae00-b5c2c35100ac | -16.39539 | -46.35655 | 2025-10-09 04:00:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc102dc4-58ae-362a-b5b7-a134f11953e2 | -15.39217 | -48.0418 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96230271-b0ba-3e3a-a43f-ec2945e30264 | -15.07181 | -46.61115 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4537e1d6-2857-3e99-b4f4-c56394a9eddc | -10.52289 | -50.03477 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 535631d9-d112-3adc-9931-6abb4e3ac483 | -11.25168 | -40.33366 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c111708-a60b-3821-9010-ac3b07702226 | -14.41745 | -43.97558 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6529d7ce-c621-3221-a95d-f9dc38134c70 | -11.23772 | -40.33503 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a266b036-4d4d-3a30-8ca0-8699323a7670 | -14.80189 | -41.62722 | 2025-10-09 04:00:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8e8139c1-541e-3e1c-a6ac-e30b4e50a0dd | -10.86341 | -44.62812 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e42c354d-f30e-32c9-93b3-804225c8e65d | -16.75076 | -43.97499 | 2025-10-09 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1acf7df7-648b-341a-80a3-428d2b014313 | -14.41295 | -43.97943 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1021e99f-bd0b-35cf-b58c-e7051a45392f | -11.56851 | -44.66522 | 2025-10-09 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df4042ac-6ebe-3c7a-a914-e8645a522b6b | -13.7909 | -45.85379 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5413422b-2f0f-316b-8b20-a5e39ad997a6 | -15.22012 | -46.3834 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae9435f5-08a8-3266-9ece-6b873a6f636f | -12.23968 | -43.78878 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7999d902-b918-307c-84ea-c4e1fce963f6 | -10.35461 | -50.2889 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c501ea32-4274-3441-b8d9-2f4ed4b7ac72 | -11.77415 | -45.0521 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b9bbece-8091-3633-803d-a2a0451dea8a | -15.44303 | -47.03572 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b11c254-7df3-3e7c-9d5a-c696f7a7b130 | -13.80064 | -45.84779 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 100b2d9b-5fe7-384c-a178-043831d1c2d0 | -13.79996 | -45.85178 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1c3726-fe74-3007-b197-4deea5ec4e8c | -11.24776 | -40.33667 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 3508331e-3ef7-3e56-8fa6-1e5eacf0c0de | -14.85122 | -48.44292 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6db3695-0567-300f-8ec0-68c0f4d85b28 | -14.44065 | -47.50524 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b4bde44-a1da-3068-8e6a-94057c0196ad | -15.4667 | -47.95709 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73dcf784-9b83-37fa-90d1-fca46f1885ad | -12.23276 | -43.78362 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73ecc5e7-0739-3eda-b36e-c2d03ae1af1c | -12.22813 | -43.78776 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc8551dc-92c0-391b-a5a5-98409bd08d6c | -11.84745 | -45.09479 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f944fee2-1570-3ca2-ad4b-484beb690c72 | -11.87223 | -44.92929 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a0eaa25-ec29-39fd-b9ec-cf95160d8239 | -15.48699 | -46.85149 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62a41c6d-d994-3c9a-8b01-00bcc641c018 | -15.24819 | -46.36862 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd45fb02-8ca2-368d-baee-d63c2e92978a | -12.05365 | -43.50098 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b333bf5-3ac0-357c-8b56-e077433576e4 | -12.92889 | -43.43356 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 404fbf68-bd77-3765-9366-df56b6f25b68 | -10.54983 | -50.04196 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 492eaf88-8718-301e-9719-badb174c208f | -15.47158 | -47.96427 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1eac51c-34c2-36ab-b7d3-9be8cea51e7a | -16.08147 | -45.78897 | 2025-10-09 04:00:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24d418ef-c19a-35a1-8911-3fa4aa676068 | -14.99481 | -46.28616 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e2a7024-d0ee-3452-bff0-271844852c8e | -13.12923 | -43.90391 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44cdff39-7435-3eea-b127-896b2efb9277 | -15.78508 | -43.2678 | 2025-10-09 04:00:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0fba149-d2c5-3c8d-ac9f-ad13ed85a05c | -16.08133 | -45.78969 | 2025-10-09 04:00:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd43d884-08ac-37c8-8f1f-6ba1ca743661 | -10.22879 | -46.08944 | 2025-10-09 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 966e6e0d-e3fe-337c-8707-438a8adfed1d | -11.43408 | -43.4797 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3760ce4-7394-3d7b-8a51-90058f5e12fa | -15.22334 | -46.38427 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 53015419-b37a-324e-8c70-cd0305349a40 | -11.98642 | -45.21858 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cc5e46d-54c1-3720-ad42-d34528eec920 | -10.52449 | -50.02634 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81964806-91ee-3933-a2e5-74d92cee047d | -14.78384 | -46.11179 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 880e63e3-35d5-333a-a5d9-e7eaddf11b7e | -11.99209 | -41.41563 | 2025-10-09 04:00:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db640b5a-8eaf-365a-8034-4a1fccefe34b | -13.821 | -45.83173 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e96185d4-ca09-3cdb-83fb-d6bd6f6b9c50 | -13.12843 | -43.90853 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06097a24-d441-387f-9e2c-cfce9cc47ecb | -10.86684 | -44.63258 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c34efa88-b5a1-3f99-8a6e-fa9add3af9b7 | -10.65797 | -44.15865 | 2025-10-09 04:00:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4de160ca-eef2-3785-b66b-9f4751af4b62 | -12.19874 | -40.33571 | 2025-10-09 04:00:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8140ff7-29f2-3f31-9b5f-94fb59bbd768 | -11.05691 | -40.93603 | 2025-10-09 04:00:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e94d950d-e020-3568-afbe-95d528fb2002 | -11.87628 | -44.9302 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf16fc5-cb50-32ff-9afb-ec40249a7838 | -11.77338 | -45.15094 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672bd305-34d1-360e-89e9-bbac125a567a | -11.9749 | -48.89285 | 2025-10-09 04:00:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fd1accf-2252-3790-abc9-dd1e16c76806 | -14.42488 | -43.97694 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fc8a8d2b-413f-3391-9620-4455d9b63702 | -14.42116 | -43.97626 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6836fc40-1b25-362f-988d-9c4bbac633db | -16.07731 | -45.78889 | 2025-10-09 04:00:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02cb7e5e-464d-34e3-8be4-6ad28dbe1f54 | -11.68713 | -44.26064 | 2025-10-09 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea8909fc-d680-34ef-9960-be5b342112c8 | -15.05807 | -42.33715 | 2025-10-09 04:00:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 57e9661c-6191-3dc5-86a5-0d70c0c2b695 | -13.61749 | -44.44228 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b62453bb-ec24-3050-8a9a-398a6d7b9ee1 | -15.55773 | -45.31811 | 2025-10-09 04:00:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a395495-cc51-3364-b5b0-a55cd3739107 | -13.80342 | -45.83212 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a227a943-c6f9-30f4-8e1a-bacd4e52cbf2 | -12.42615 | -45.7067 | 2025-10-09 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 75bd16a0-6fa2-3bca-beb1-6e67bd0d87e5 | -10.92648 | -42.84519 | 2025-10-09 04:00:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 275ea4d8-05bd-39de-8aa2-1f35b032bb25 | -11.65178 | -47.53814 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2917cb69-e959-30bd-ac1c-e29944ee061e | -13.9409 | -42.35516 | 2025-10-09 04:00:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b28d0fc-a450-3e0a-a60e-000ff0c900f9 | -11.98433 | -45.20636 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e52ed13d-9fa5-34a3-8586-1231a30a9d5e | -15.47046 | -47.96288 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d9e3cc4-9a0c-32d4-87a8-a39db439c84f | -15.46786 | -47.95847 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README24.md)
