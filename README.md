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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82042eaa-0690-3d9d-aa65-21e345d19ded | -14.7851 | -43.9434 | 2026-03-19 00:00:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 595392d3-6046-36e2-b62e-d32d753c3deb | 3.2017 | -60.3458 | 2026-03-19 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5ce12f37-7bd7-3eef-9a5b-c7446d166199 | 2.2523 | -60.2841 | 2026-03-19 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 07df752a-8a19-3f48-9377-c24dab84d465 | 3.2018 | -60.3268 | 2026-03-19 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 52afe5a2-9ac6-3a90-9cc7-0176d28fce3d | 3.2017 | -60.3648 | 2026-03-19 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 13190402-a23f-333c-9b7e-1bfc6573b940 | 3.2017 | -60.3458 | 2026-03-19 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 1228a975-2391-3bcf-adeb-2e54007579e1 | 3.22 | -60.3455 | 2026-03-19 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 310c1e34-7aba-3cb0-a93d-893ce2f60af7 | -14.7851 | -43.9434 | 2026-03-19 00:20:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 5b2b80d0-ead9-3552-b589-808bb93cfe70 | 0.7751 | -59.8592 | 2026-03-19 00:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 397.9 |
| 92b9e4ce-bd53-3cab-856d-199dd8bc8134 | 0.7568 | -59.8783 | 2026-03-19 00:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9e922d30-eee7-393c-b9cc-1ea29725f11e | 3.2017 | -60.3458 | 2026-03-19 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 97d875f1-3ec3-346f-bcf1-48e8e8038912 | 0.7933 | -59.8591 | 2026-03-19 00:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c7c2fad3-8c6e-3822-af2e-426bb39ed961 | 0.775 | -59.8782 | 2026-03-19 00:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 225.9 |
| 6c6e95bb-f62c-3209-b1c8-b004b14d1e7d | 0.7568 | -59.8593 | 2026-03-19 00:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 8960f7bd-1682-349b-9111-43a3874bb2e3 | -25.0478 | -51.19368 | 2026-03-19 00:20:00 | TERRA_M-M | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 87c9631b-9a88-3e71-8316-6caa4e921bb6 | -16.40925 | -39.74512 | 2026-03-19 00:20:00 | TERRA_M-M | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 593acb31-f478-3507-9a47-d5107b57643a | -14.77519 | -43.96716 | 2026-03-19 00:22:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 16e584e1-15fe-356d-ace8-39c6c93c0ea0 | -14.78392 | -43.95034 | 2026-03-19 00:22:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 35.1 |
| cc41a2ee-cdfb-3106-9b2b-089875a54e92 | -11.80089 | -47.09339 | 2026-03-19 00:22:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac1afb69-b723-3950-9a1b-b2e70e9fcde3 | -11.80241 | -47.10367 | 2026-03-19 00:22:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c23dd2c5-2a37-3b6e-9673-5eaedeca3087 | -14.78627 | -43.96523 | 2026-03-19 00:22:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 76c64ec5-39ee-390c-b221-0e3312ae1bad | 2.95552 | -60.70625 | 2026-03-19 00:26:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e8f5e583-8cbd-3770-abcd-b6aa054fe06f | 1.98501 | -61.39801 | 2026-03-19 00:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ec079fd3-a829-3165-80ff-839e62c6b7e1 | 0.87224 | -60.26401 | 2026-03-19 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 99b3422d-39fa-3dc0-bb9f-f16fb05a509d | 0.77579 | -59.89008 | 2026-03-19 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a4b5e866-fb87-31c3-ba3f-4b2260ffd519 | 2.95529 | -60.71142 | 2026-03-19 00:26:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 6ec02f7f-b98c-3eba-ad27-c0c6ea0c7862 | 3.20549 | -60.347 | 2026-03-19 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 151.8 |
| c9e11c35-e000-303c-97d0-332c715cb978 | 3.65275 | -60.63615 | 2026-03-19 00:26:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 4f4843ff-9a21-3633-ba13-f9d3b385465f | 0.77365 | -59.88303 | 2026-03-19 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 279.9 |
| 4a832b3f-37dc-3635-a792-e4eecc88e394 | 2.95149 | -60.73395 | 2026-03-19 00:26:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 3ea44cef-648b-3608-824b-e12150198647 | 0.77964 | -59.86415 | 2026-03-19 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 442.8 |
| 7bf008c3-0e3d-3d6b-8ee4-0607b03ca2cf | 3.2081 | -60.35268 | 2026-03-19 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 151.2 |
| f1072ebd-0425-35a6-993b-84a651c5b045 | 3.41969 | -60.16535 | 2026-03-19 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c02b5548-e634-3e73-8800-f4650c2fff25 | 0.77731 | -59.85709 | 2026-03-19 00:26:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 410.1 |
| d7fadb5b-af74-3705-bcba-1539fb6a1a4a | 0.7751 | -59.8592 | 2026-03-19 00:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 314.8 |
| 27c24488-27a7-3106-a0c2-b641908be8d4 | 0.7568 | -59.8593 | 2026-03-19 00:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| e62f1b7b-ca43-355c-8601-653cc25a8f17 | 0.7933 | -59.8591 | 2026-03-19 00:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 14548c2b-2092-3577-8aab-2e5ef1e16eac | 0.7568 | -59.8783 | 2026-03-19 00:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 43a41c22-e2c5-33c4-a02a-9d54aa3af9e5 | 0.775 | -59.8782 | 2026-03-19 00:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 221.3 |
| 35fffa5a-d36f-34de-8ba9-78cb5fa33b8e | 0.7933 | -59.8781 | 2026-03-19 00:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 386a044a-4974-3cc0-aa59-6f84498bf060 | 3.2017 | -60.3458 | 2026-03-19 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2e98c490-dd60-3c1a-83a3-18c7546820ea | -14.7851 | -43.9434 | 2026-03-19 00:30:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 54a01e73-e663-3c49-b44f-35e5b0a717ad | -14.7851 | -43.9434 | 2026-03-19 00:40:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 8a8119c4-338a-3f69-ac92-d6ca31180f73 | 0.7751 | -59.8592 | 2026-03-19 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 543.2 |
| f1ca26c2-a94f-3759-b632-490e6fbe5bfb | 0.7568 | -59.8783 | 2026-03-19 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 882cd6dd-876c-3f38-a0a7-67e4261605eb | 0.7933 | -59.8781 | 2026-03-19 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d9077e36-0f52-387a-b60c-c2d7a64dd6d7 | 0.775 | -59.8782 | 2026-03-19 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 334.4 |
| aa6345fe-fd7d-36d1-a4c8-8daca149ba7c | -14.7851 | -43.9434 | 2026-03-19 00:50:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 59.0 |
| a05cccda-ed9d-3390-8492-d07ed6043342 | 0.7933 | -59.8591 | 2026-03-19 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2c86b7fb-76a4-3e16-ba9a-bd562642bc93 | 0.7568 | -59.8593 | 2026-03-19 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 154.9 |
| d76b5b3f-3f89-3cc5-9321-25551c0a6ccf | 0.7568 | -59.8593 | 2026-03-19 01:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 134.4 |
| aacb9556-222c-364f-b87d-8206bcfe39ce | 0.7568 | -59.8783 | 2026-03-19 01:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 108.3 |
| e3fa1b13-bff4-3fa0-b93b-eac2b9ede69f | 0.775 | -59.8782 | 2026-03-19 01:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 62385d0c-4fb5-33ed-b82a-48d5dfc6bcf0 | -14.7851 | -43.9434 | 2026-03-19 01:10:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 02021568-6ee5-34bc-b1e6-3dabba5c11c1 | 0.7933 | -59.8591 | 2026-03-19 01:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 111.8 |
| db4c580c-eeaa-38fc-9621-a645b8256048 | 0.7933 | -59.8781 | 2026-03-19 01:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 91.1 |
| cd8654bb-9183-3cf9-8a09-7c571c052e4a | 0.7751 | -59.8592 | 2026-03-19 01:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 310.3 |
| 66f14ee5-1f19-3c79-aaaa-d55f45d28c1f | 0.7568 | -59.8783 | 2026-03-19 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 73cdac5f-3fbd-3c4f-9643-bedf038baf44 | 0.7933 | -59.8781 | 2026-03-19 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9d3f7360-9a32-3878-a896-e1dce3f25529 | 0.7751 | -59.8592 | 2026-03-19 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 286.7 |
| 60246ed3-ba93-3611-8692-b32923ec80e4 | 0.7933 | -59.8591 | 2026-03-19 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 95.4 |
| ac5bc470-95cc-3ab7-afe6-4650fd9b4ed6 | 0.7568 | -59.8593 | 2026-03-19 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 6711d9cc-93ce-3729-9f06-57a12e43320b | 0.775 | -59.8782 | 2026-03-19 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 0d2de30d-9a6a-3e84-95e8-92b348ce592d | 0.7568 | -59.8593 | 2026-03-19 01:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a2c40c1f-5aa7-37fe-9c2c-da52e63e8444 | 0.775 | -59.8782 | 2026-03-19 01:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 218.6 |
| 5437a097-0a45-3dc6-8ee1-0e211c53d89d | 2.9451 | -60.7108 | 2026-03-19 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6529e095-7cfe-3578-9c8d-918a80297880 | 0.7751 | -59.8592 | 2026-03-19 01:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 262.8 |
| af224311-e9e8-300c-85f9-9a645252b057 | 0.7568 | -59.8783 | 2026-03-19 01:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 53d376e8-7a60-3543-8678-2428191ae5e3 | 2.9451 | -60.7108 | 2026-03-19 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9a9c7c3b-962a-370a-a1b5-f2ee27d80587 | 0.775 | -59.8782 | 2026-03-19 01:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 214.4 |
| b6502fe8-c2c7-3850-a628-ce62bf076065 | 0.7751 | -59.8592 | 2026-03-19 01:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 241.7 |
| 62e9f8bb-4566-38a7-afa1-788721a521a9 | 0.7568 | -59.8593 | 2026-03-19 01:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 11a33fd7-6a7f-3fe1-9550-8fd2d6e46434 | 2.9634 | -60.7105 | 2026-03-19 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9ec8a795-3a69-36d9-8cf7-41297b13701f | 0.7568 | -59.8593 | 2026-03-19 01:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3c863e87-c5ee-3ad5-89e3-9ef5f8b0c8e9 | 0.7933 | -59.8591 | 2026-03-19 01:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6f419651-e9f3-32b3-9c86-00e72af83c86 | 2.9451 | -60.7108 | 2026-03-19 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5c240f7b-6c6f-34c5-a838-d6a1b21c46ff | 0.7751 | -59.8592 | 2026-03-19 01:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 254.3 |
| 2afdd77e-b40e-3f16-8132-56495c91e548 | 0.775 | -59.8782 | 2026-03-19 01:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 155.9 |
| b33d923f-3909-32b5-bb2b-2b940a9dea9f | 0.7751 | -59.8592 | 2026-03-19 02:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 01b50c1f-64bc-37f0-b5cc-94763a4b5ae5 | 0.775 | -59.8782 | 2026-03-19 02:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 49431272-6d41-3e58-a70a-6a2ecaff017e | 0.7933 | -59.8781 | 2026-03-19 02:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| adf68125-25c6-37b0-b8dd-b39f182d575e | 0.7933 | -59.8591 | 2026-03-19 02:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 223dfe51-050f-372a-8b4a-d4f59ba4ed8e | -14.7851 | -43.9434 | 2026-03-19 02:10:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 84875015-af24-3708-805a-a342f59779ff | 0.775 | -59.8782 | 2026-03-19 02:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 4609610a-3e1a-3a9c-8f8c-d425866cc98c | 0.7751 | -59.8592 | 2026-03-19 02:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 206.9 |
| cd305da7-1f31-3f00-95ef-209336d18701 | 0.7568 | -59.8593 | 2026-03-19 02:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 898127ba-ebc4-3cee-86df-e184abbdb100 | 0.7933 | -59.8781 | 2026-03-19 02:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e262f122-344c-3241-bc8d-8c890260bdc4 | 0.7568 | -59.8593 | 2026-03-19 02:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1cc1fe1f-694c-342c-ab00-4a435420f439 | 0.7751 | -59.8592 | 2026-03-19 02:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 155.8 |
| dcd5a858-8400-3974-aab0-1c16d6db4e2c | 0.775 | -59.8782 | 2026-03-19 02:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8b05a5bc-2b32-3364-89be-5648033fd55e | 0.7933 | -59.8591 | 2026-03-19 02:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| cde20222-3fb7-37f7-9914-5080cfae70bd | 0.775 | -59.8782 | 2026-03-19 02:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 5a48efea-d446-364a-924a-9c18999ca6d4 | 3.4215 | -60.1706 | 2026-03-19 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4bd25cff-3db8-36d3-ad68-7fe00003cb17 | 0.7751 | -59.8592 | 2026-03-19 02:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 54611e3c-df9d-3348-bbc8-c16473dede44 | 0.775 | -59.8782 | 2026-03-19 02:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 7bf28e31-69f0-3205-8297-67743d943886 | 3.4215 | -60.1706 | 2026-03-19 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ce9c3682-a73b-38d2-b83e-c48db326ef3c | 0.7751 | -59.8592 | 2026-03-19 02:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 3eb3ba53-f83a-3ff7-95fb-f49c5b980153 | 0.775 | -59.8782 | 2026-03-19 02:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9d6ccbd1-db52-350f-92e7-cde37ff432f3 | 0.7751 | -59.8592 | 2026-03-19 02:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 96.0 |
| d0e6f85b-bf36-3109-a5cb-b250e7763792 | 0.7751 | -59.8592 | 2026-03-19 03:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |


[Clique aqui para ver as próximas entradas](README2.md)
