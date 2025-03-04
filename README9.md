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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe443b45-96d7-3443-a883-fc58964d343f | 2.35624 | -61.04967 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc4a1380-1e70-361d-8b29-187abab362dc | 2.35784 | -61.05923 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8f9b8e-e243-3313-ba0b-3d02bbcf015c | 2.35838 | -61.06253 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9743c3c7-2590-3cb2-b91e-d40e87a3f273 | 2.35322 | -61.06322 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d4ea0ad-e0b1-372f-b215-41d9dba244e6 | 2.33991 | -61.05909 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2431e604-860f-3e17-8d4b-0cf9ae37d243 | 2.36299 | -61.05848 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b11705f9-2d5f-3153-a83a-9105aa1629c9 | 2.34702 | -61.0577 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50459766-52a5-330e-b091-5a4da1bf0f7e | 3.22413 | -60.98513 | 2025-03-04 06:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22d4d138-0647-3b2d-a60e-d1c08edf2fd3 | 2.34408 | -61.05219 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b27ffc71-cb53-3b3e-bc0c-0839375637c2 | 2.26813 | -60.25533 | 2025-03-04 06:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4242eff8-4f01-3665-8da7-7c055ceadb9d | 2.35729 | -61.05595 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9d9b4c3-cf13-351a-aee6-775b8baf1216 | 2.34808 | -61.06404 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b82fc555-860e-37ec-8e6b-eecdd94b2e1d | 2.35675 | -61.05275 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83bb1c04-dd48-3b6e-a1f2-5444d7f5c3f4 | 2.34647 | -61.05445 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba46c49a-9451-3fc2-b433-7817e24e1314 | 3.54013 | -60.10583 | 2025-03-04 06:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fbe8cee-9ea5-35c8-a040-3845875cc141 | 2.41812 | -61.20154 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e207aa4c-90f4-393f-8bc9-70402aa52fca | 3.22463 | -60.98814 | 2025-03-04 06:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92a624d6-b7a8-3a2b-b587-837204f98257 | 2.34183 | -61.05821 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05f60c60-b02d-39fb-821b-81343c4718cd | 2.34234 | -61.06127 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af7770bb-f338-30bd-89ca-6fa35c147529 | 2.36192 | -61.05207 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9096a455-1f59-3cb9-be83-833b6a401008 | 2.33943 | -61.05613 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e91e0463-70c5-38bc-9149-14cddbcf7e6b | 2.26874 | -60.25903 | 2025-03-04 06:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05c7378b-2592-3597-a51b-6f981b00d483 | 2.36087 | -61.04578 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a5aac012-2a03-30e1-bb58-f3507f58a792 | 3.54917 | -60.09378 | 2025-03-04 06:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34e2e3c-da18-3cf1-ada1-96cd1e8dd835 | 2.35268 | -61.05996 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac9679cd-cb6e-36f1-b065-01f83da435c7 | 2.36246 | -61.05533 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a45d364-67a6-3491-961e-03546fb57c11 | 2.36352 | -61.06171 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e652c38-767c-3b7d-b005-ae6b6acb39b0 | 3.53956 | -60.10243 | 2025-03-04 06:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c0cefda-3a51-3f09-ae32-72d73ec5b357 | 2.3486 | -61.0671 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f97a4a64-6bb7-3830-82f7-6c2fc11cfaf6 | 2.34564 | -61.06199 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d50e062-bb18-3795-acc6-5df53c073c2a | 2.35892 | -61.06576 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2413c0ad-b166-3a40-883e-c65b45d4fb2e | 2.34513 | -61.05876 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb220236-2d13-3254-a728-32c05f35e5ef | 2.34588 | -61.0509 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 145289bf-c7cc-3b5a-a683-93b3ee2dea01 | 2.34462 | -61.05559 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b3c32e0-99d4-3e58-b2ec-1fd9110a2558 | 2.34131 | -61.05516 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8531a504-df36-342a-a298-2e68a48af3a2 | 2.35573 | -61.04659 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d629175d-f94e-36e4-bb83-520e24203de2 | 2.41304 | -61.20239 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68ef9eb7-9f7c-30f4-870e-ae7b5f4b674a | 2.35376 | -61.06641 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca1f8965-03b1-3831-afa3-5d0bbb4e09c5 | 2.3505 | -61.04692 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10eba98a-f667-3b34-8ab1-7de8956e7964 | 2.74518 | -60.73288 | 2025-03-04 06:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01899bb2-3da0-38c1-aab2-75d68235443f | 2.34614 | -61.06509 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15a795c6-995d-3a77-b871-963c38539856 | 1.08564 | -60.67985 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82e5a02e-6507-37f2-9957-23afde0da222 | 1.12234 | -60.5139 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d173e8d3-5c96-3e57-8be6-18486120864d | 1.28418 | -60.07999 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df6b4b1-378e-395e-a462-78a84e05375e | 1.13323 | -60.5122 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4cc2cb19-6e1b-3f20-80d8-81e34ade4504 | 0.96132 | -60.52916 | 2025-03-04 06:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 993433af-4f9c-3676-add6-0280e0115d66 | 1.13379 | -60.51569 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6bd2d8fb-5d33-3c18-ad20-bd81370e257a | 1.12835 | -60.51656 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ea6551de-a800-38fc-be35-c989b526c08d | 1.08168 | -60.67268 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 461aa0bd-942a-3a02-b2f1-6f7856a4c266 | 1.07917 | -60.67386 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63dc4b3b-f48d-3c89-b3ec-562d8a173c99 | 1.0882 | -60.67867 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a796a7c7-397c-3581-a24d-a1c85b48a93b | 1.13811 | -60.50784 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fe76d92d-fc5c-3bb0-9e5c-fbae2077918b | 1.13867 | -60.51133 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f17e789-6937-3bfc-a95b-ba0265ae0b65 | 1.08764 | -60.67527 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e4669dd-b908-3e95-ae00-0dc6f50488f6 | 1.0851 | -60.67646 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b4025b9-2e72-3330-b911-7e9b3d344866 | 1.12347 | -60.52089 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 82297e7e-ae24-3da0-b103-09076b597c1a | 1.08456 | -60.67303 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55233770-e783-3d2c-8f0c-fd848c8bab77 | 1.12722 | -60.50956 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f1e0e5da-432a-38a1-a88d-8b0c0956e6c8 | 1.13755 | -60.50434 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24f3587b-d4d0-36f5-b2bf-cd00397dbe65 | 1.08707 | -60.67188 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26791035-e96c-31e2-b357-779e2fbbf838 | 1.13267 | -60.5087 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| da92638a-859a-3214-9e51-3141b9394541 | 1.28358 | -60.07627 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7ff1ce0-e4e1-370d-ad42-0ec6e2801e4e | 1.13923 | -60.51482 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8d9daff3-d0f7-3c28-9d01-f7d9d910a734 | 1.08402 | -60.66962 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e64a8171-167e-3a6c-b9bb-1c6ff3174bc7 | 1.12779 | -60.51307 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f32d803d-e5fd-32be-8523-1adacdc5e2a0 | 1.1229 | -60.5174 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 416b7550-6fba-3b61-9fdd-99a7167f61b8 | 1.09049 | -60.6756 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba698390-c96e-3f71-bdfb-b7732c4a7d22 | 1.08225 | -60.67609 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9176a2af-3541-321b-8c51-a8fbe68bafda | 1.12891 | -60.52005 | 2025-03-04 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 401ba442-f4be-36e9-a454-c2de0f65e6ec | 2.3604 | -61.0597 | 2025-03-04 06:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 854ea90e-90fd-3b79-83f8-d23e41a1c736 | 2.3421 | -61.06 | 2025-03-04 06:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e6d78e7d-4c88-3114-a4d7-bdaeb4d63ac7 | 2.3421 | -61.06 | 2025-03-04 06:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c4f1e223-bbaa-32d5-968b-1cfbb5f1884a | 2.3604 | -61.0597 | 2025-03-04 06:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8834f109-b291-3246-a1ed-138368f90239 | 2.3421 | -61.06 | 2025-03-04 07:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0e0fef4e-9e5e-3809-9747-01ff1f63427a | 2.3604 | -61.0597 | 2025-03-04 07:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 70e1e930-25cb-3261-8e90-c191cd1d6183 | 2.3421 | -61.06 | 2025-03-04 07:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9a8b1f72-f918-3860-9871-dbf2f63c3d0c | 2.3604 | -61.0597 | 2025-03-04 07:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 236e1bd2-b4e8-3957-9425-a79afafb5917 | 2.3604 | -61.0597 | 2025-03-04 07:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| cd8a3ff4-c001-3b48-ba12-4eb9af95f574 | -14.028 | -45.6304 | 2025-03-04 12:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 2a64b1a3-cbe9-3028-96ea-0f9a75b92d68 | -14.0285 | -45.6072 | 2025-03-04 12:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 65e5e95f-2b28-319b-ab53-2a661be80f0a | -14.0085 | -45.6338 | 2025-03-04 12:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| ff7807ed-65b0-3ae8-acaa-e82d0a455f9a | -14.0275 | -45.6536 | 2025-03-04 12:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c4b787e4-5ffb-322a-9487-48e5032baa1b | -14.028 | -45.6304 | 2025-03-04 12:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 290.6 |
| 796e9c9f-98be-341b-a6d0-5fd4d4d6345d | -14.0285 | -45.6072 | 2025-03-04 12:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 89751202-9549-3586-8615-45b79050f14e | -14.0285 | -45.6072 | 2025-03-04 12:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 11cb42b3-d5bd-350a-9d51-2843ac9c350a | -14.0085 | -45.6338 | 2025-03-04 12:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| a3e08ca3-5bbd-3f80-95cc-97fc5137eb09 | -14.0285 | -45.6072 | 2025-03-04 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 684c9788-2a08-3042-a141-13d9cb51ab63 | -14.028 | -45.6304 | 2025-03-04 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 342.8 |
| 75067139-b0f6-3e19-b602-5e40b738326d | -14.009 | -45.6106 | 2025-03-04 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f35ff36c-7fdc-3cba-b911-81634302de81 | -14.0085 | -45.6338 | 2025-03-04 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 083452f4-8069-333f-b0f1-6a8daa0cb5ad | -14.0275 | -45.6536 | 2025-03-04 12:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| f3253ee1-c233-3006-8816-4722b2112b7f | -14.0285 | -45.6072 | 2025-03-04 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 5a54964f-1b68-34f1-9701-dd132aa1e45e | -14.0275 | -45.6536 | 2025-03-04 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 4f1468c8-2ba5-3472-bcfc-4e815fa5ead9 | -14.009 | -45.6106 | 2025-03-04 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 10fe5b7a-a241-31be-a641-4a49853fac53 | -14.0085 | -45.6338 | 2025-03-04 12:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 43ed126a-0ff5-30ac-ab75-b9de281bb8d8 | -14.0085 | -45.6338 | 2025-03-04 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 279.7 |
| 1c44fbf4-96f5-3749-becd-4de15dc407a7 | -14.009 | -45.6106 | 2025-03-04 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 3e4b2382-404a-333d-9ca3-00443c92bbd1 | -14.028 | -45.6304 | 2025-03-04 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 319.9 |
| dfca2f47-2c67-3ea0-b85d-d8fdf8d4c6cb | -14.0285 | -45.6072 | 2025-03-04 12:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 7e70ea4f-6030-379b-a549-5b6f7d93b611 | -14.009 | -45.6106 | 2025-03-04 13:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 247.1 |


[Clique aqui para ver as próximas entradas](README10.md)
