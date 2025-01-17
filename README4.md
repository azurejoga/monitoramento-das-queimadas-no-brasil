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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45410132-1108-3fc9-b548-dcab807fe6ff | 4.3391 | -59.70533 | 2025-01-17 05:25:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 884ef341-b5a4-391d-ba67-800bccb62fb1 | 4.84 | -60.60446 | 2025-01-17 05:25:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4b42660-876c-3fff-8dad-85ad098944e5 | 4.85379 | -60.62744 | 2025-01-17 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6e60b37-570d-39c1-8362-291c70d0783e | 1.3297 | -60.03337 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2172553-0b03-382d-a459-4cbac635ac34 | 4.12163 | -60.02795 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ae3819f-cc9c-38ea-8e43-fd92e2a89e40 | 2.19766 | -61.81259 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0d5cf0-5323-3e10-99d1-541f71117ba3 | 0.16382 | -60.65615 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9b905e3-2792-320a-aa62-96256d58e4ef | 3.14345 | -60.70103 | 2025-01-17 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d596b1e0-24e0-3c8f-b59e-16c0f4e14fe8 | 1.93917 | -60.40947 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712ae7d4-3633-30fe-b0f3-e30d8a32e92c | 0.72792 | -60.11713 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df0f34a5-8a8e-3d83-8d7d-1d7c0e0da9dc | 0.84183 | -59.54482 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3571c02-289e-3de3-86b2-675702a68ee4 | 2.17004 | -61.85752 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64801f9b-6b1d-3b89-bcc4-8b2d615be717 | 0.82434 | -59.71542 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b236ff63-33d5-32a6-819a-fee8b8cf641e | 1.32362 | -60.03783 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 318f359b-ca29-357b-81c6-802f241ace68 | 0.72847 | -60.12058 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb7da69e-ad9f-34cb-b1e3-e725f817bcbc | 4.02477 | -59.67374 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd30992e-c1d7-3c23-8b3a-777580cbca03 | 1.93038 | -59.96373 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47b47966-4687-3038-8079-18a827fbce3d | 3.92321 | -59.67555 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5ef50af-667c-3b2f-bdb7-d796e4fbd4a0 | 1.17357 | -60.48734 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5547d0a-fa57-3482-923c-1bf611ae8191 | 1.74073 | -60.63783 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a106f823-18bb-35b9-89e8-b590880c850e | 3.52648 | -59.89635 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20a0c56e-0930-3149-b8ed-2c6d7958e995 | 2.28632 | -60.21794 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b7c783-6b04-38cc-9d5b-fb00d6914df3 | 2.16271 | -61.85498 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af90f1bf-68bd-3a2e-bb2e-ae98c56ff655 | 1.05217 | -59.65182 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 330dba8a-6109-3d10-b1a0-dc52f6608a6b | 0.7257 | -60.12453 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e4c0e30-8dd6-3338-8a9d-9d828087df71 | 1.90343 | -60.56984 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 274941bd-8edc-3cae-b5a0-f6b770a5deaa | 2.18756 | -61.85855 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9baf488f-1524-37ab-8846-76caed775829 | 1.3457 | -60.02735 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 593058f5-4a34-3aa5-9817-ecb0316c0b8a | 2.14438 | -60.84977 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ed2701d-1196-3c70-a60c-dc4f508c6edf | 2.19427 | -61.8131 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd03937c-8980-3b59-907f-39ef3f122f9f | 0.67785 | -59.58487 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0d8d999-91e8-370f-a2e8-2f7e5a53c676 | 2.17682 | -61.85649 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eea4c2a-7f3a-3a9b-bace-24bffb3e9e46 | 2.174 | -61.86062 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf2b4716-912b-3255-b82a-61ea2d851182 | 0.555 | -59.68658 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0025c740-bdf0-339e-8151-021b29034cee | 2.19032 | -61.81002 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1224d7-92e1-3df9-a54b-22fe533f9001 | 4.0106 | -60.33879 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98c31ba3-4a74-3568-8cfa-77ffa09b1d21 | 2.36466 | -60.15652 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 238a09b2-a12a-3aad-80e0-3b030abacbdc | 2.28299 | -59.83132 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b27aa8-acbe-3e0b-973a-0aaffdd71ea7 | 0.67088 | -59.99171 | 2025-01-17 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47dffdb7-a986-33e8-8c5c-062df45e7ff7 | 2.17964 | -61.85236 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9461c39-3463-3337-9362-f5fcd72932a7 | 2.9847 | -60.25262 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212e7b76-60d0-3f2e-b673-c37b87987039 | 1.16858 | -60.49865 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0135fa-13be-3f01-9e50-c61d7c72f1db | 1.32308 | -60.03439 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5944dd1-267d-316e-b2ae-33684b28fee2 | 1.34955 | -60.03028 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0bfc80b8-3380-3d9d-a701-298c4c05814f | 1.93586 | -60.40998 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7aae0f5-1fa2-3425-86e5-7ee87bf3d6d7 | 1.90397 | -60.57327 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f28686f-b5e2-3248-b4c3-e4879dcfec54 | 3.33077 | -61.03012 | 2025-01-17 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdef0143-0b9a-3424-a45f-bc2f9714cf8f | 3.00647 | -61.2822 | 2025-01-17 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2c3f366-75ea-33f5-81df-a419b0c7c41c | 1.17411 | -60.49076 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b496c5b1-c9b6-3b99-99b9-afc2029ffd45 | 2.29347 | -60.22034 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5cc566-d5d1-31f7-8fe0-915e4a5311ee | 1.17081 | -60.49128 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed972f07-9322-337b-b0ce-bdeddef63eb3 | 2.29017 | -60.22086 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8340a72-bf7f-30f5-8baf-05a77f3c39cb | 3.79499 | -59.72418 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 038ac7e5-451c-376f-9fe5-756edbba251e | 0.71885 | -60.0161 | 2025-01-17 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381af0e8-b0c5-3bae-8e79-b080cff6c6a2 | 0.8485 | -59.54378 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8065161f-11f1-3ca4-9216-70c02414fc58 | 2.28578 | -60.2145 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6773e93-b901-3288-a3a9-0f14ce1146c6 | 0.72955 | -60.12747 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164b19c5-c836-364c-95bd-49d857d5b53e | 0.44725 | -60.62207 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ea6b004-cf95-3058-aedb-c9f35774dc84 | 0.45056 | -60.62156 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 395feaa5-4182-3399-967b-b2f189781cc2 | 3.84661 | -60.15993 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc1e25d4-28da-31ab-ab89-262b2715c188 | 2.21274 | -60.24706 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5d8e324-315d-319a-9689-8f92048cc88e | 3.60156 | -60.11338 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d8e83a0-d2a2-3507-92ce-e64c40912737 | 1.88664 | -60.48447 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 771fcd04-b448-3fb7-b815-676ce626acbd | 1.01017 | -60.57243 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b3f161c-2189-3f24-8275-a2efc7cfdacb | -0.15891 | -60.87181 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50141a4d-41d7-3b95-bcf1-3bdb1cace0a2 | 3.74532 | -59.77419 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b748e6a-d7e6-379b-9c04-b22eeb473d14 | 3.60102 | -60.10995 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33472713-9642-387f-8475-fe3009067c4e | 2.18807 | -61.81775 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ed9767-90f1-317d-8e24-de6c0ca8b16e | 0.99734 | -59.60681 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7a72f64-b41c-3d2d-b9b3-90e3554ca92f | 2.1125 | -61.82203 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c615a357-bafc-3962-90ab-934f17ba8cd8 | 3.79168 | -59.72469 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e96babb5-4a25-3eb3-9f9e-98de41ada759 | 0.84516 | -59.5443 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5cae986-c199-3751-bdb6-2534013d0da6 | 1.17135 | -60.49471 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4fcf218-5ee7-33f1-a68f-1387762bc451 | 1.13685 | -59.43478 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11c1c419-7518-31e4-b79b-d8f81f0b7f18 | 1.93863 | -60.40603 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2eef84e-8bf2-31b2-afc4-b714c1c1ea9c | 4.29334 | -60.36583 | 2025-01-17 05:27:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08e0623e-6012-38b4-9b54-fe7be7060d00 | 0.73286 | -60.12695 | 2025-01-17 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eff7668f-2421-31b2-bc72-2db666227485 | 0.86816 | -59.69081 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dfffb39-cf1c-3ff1-8687-1f12a213ae95 | 1.63723 | -60.28111 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad6e2ff2-eaa0-3779-9273-0cb4c3b47c6e | 2.09106 | -61.84723 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0efc1d6-95ab-3428-be73-d1b004c49f28 | 2.18021 | -61.85597 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e0ef8cf-e80f-3421-9c38-4854ca8a1b38 | 2.67442 | -60.41759 | 2025-01-17 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3f05a91-61e2-3b30-a583-c20fd9284ab0 | 1.17742 | -60.49025 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa6706ef-6ffe-3334-8285-1c6b9653828b | 1.34624 | -60.03079 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4c72465d-6f31-39de-8ee1-4453f4a4f5d2 | 0.96629 | -59.4756 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a0f3a47-f5e7-36a3-af2a-1f7b8addb522 | 1.08757 | -59.68196 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d74d8eb4-7447-32eb-aeca-402a368dc1b1 | 4.12493 | -60.02743 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bc284c3-c03d-3206-a34c-b3397355584c | 2.1836 | -61.85546 | 2025-01-17 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 769c0ddf-115e-31f7-abae-2368192017e3 | 4.02807 | -59.67322 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9a6677d-ffe3-3e5c-8719-2ffa01496bea | 1.16804 | -60.49522 | 2025-01-17 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e38af8c5-464b-3e33-ace1-21c242269536 | 0.16436 | -60.65959 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c5db1e3-9451-3033-8ace-3b2f892c94b5 | 0.58946 | -60.44536 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f1995b5-3643-335b-8176-7b1c143d3d68 | 2.98524 | -60.25605 | 2025-01-17 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44e70ac3-619d-378d-be98-8ca646488bc9 | 0.84057 | -60.27218 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05028ab6-945f-3da1-a813-bc7b2fbf73b1 | 4.02531 | -59.67718 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2cc2b7-3b6e-3c9f-8812-718a1b15fefb | 0.63589 | -59.81269 | 2025-01-17 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 149769da-beab-3ba2-a93a-2485ce52e042 | 3.59831 | -60.09277 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff2a184a-9d50-3471-a353-835006381ea1 | 0.50658 | -59.34093 | 2025-01-17 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4578c1f-d03d-3b76-a785-7b43f4d45850 | 0.90956 | -60.34198 | 2025-01-17 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6dede0e3-6740-3e83-b9fc-abfafec5446a | 3.59994 | -60.10308 | 2025-01-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
