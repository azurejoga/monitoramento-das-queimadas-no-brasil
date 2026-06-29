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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f6b56f9-f89b-3bf1-a771-bb8d482eea48 | -13.25931 | -54.39847 | 2026-06-29 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3827f646-b5fe-3693-9356-f0c31a155119 | -10.97711 | -49.5574 | 2026-06-29 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8eef5504-7d17-345a-8e5a-337e35491e18 | -13.70967 | -47.86065 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a29ef309-c620-3eb4-ac61-0e6fc63c34e7 | -11.2191 | -53.83451 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 50ba12cd-5382-3143-9bd6-b915137a9dfb | -10.50228 | -53.57528 | 2026-06-29 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28d076f0-6205-3993-a688-2b487d7822e6 | -9.18495 | -58.06849 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5a1efed-4bc4-34c3-989f-644b2909af4d | -11.21584 | -54.30313 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 572eefdc-756b-3778-b5ea-e058e501eb62 | -9.31707 | -58.03024 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a3636a8-73f7-3f07-94b2-7569675c1da9 | -11.88313 | -57.12975 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ae97159-e4f8-309f-9d0d-6104d6774b96 | -11.21545 | -53.83398 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2670804b-c484-3e8f-b935-172dd6cd8979 | -10.32637 | -50.17529 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8aad8791-835e-33d8-b9a0-8292437caec9 | -11.88757 | -57.12324 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 908c2719-d74b-3f3c-a292-7c9b2209fbfd | -10.39279 | -56.76328 | 2026-06-29 05:16:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72baadcd-6062-35bf-9a13-de5fd0a0d4b4 | -12.23414 | -56.55412 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd28108e-be4d-30f3-8ecb-2d04992bbcc9 | -11.89809 | -57.14305 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a40de4-32a4-3577-94fb-99becf3d6537 | -11.31573 | -51.38674 | 2026-06-29 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98249e87-8471-3307-ab7a-315e35caaf69 | -9.59172 | -56.92838 | 2026-06-29 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23151ef5-8f72-3f27-9bd6-2aad2935275a | -11.0619 | -55.76505 | 2026-06-29 05:16:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 789ef58b-857f-3381-bc5f-9f6ddd462b04 | -12.51857 | -48.29382 | 2026-06-29 05:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96db932b-1b78-39cf-b0c6-1098984c818d | -9.31369 | -58.02968 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82bb8477-1656-3853-bd73-5461889842d6 | -9.60613 | -56.92353 | 2026-06-29 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4da7d38-4734-300a-8bca-90af45101855 | -10.30116 | -57.12603 | 2026-06-29 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 835d7e33-f311-3b62-a9f0-9192795b3312 | -10.31608 | -50.18319 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f1b69330-452e-3eef-96c7-e220ec29496e | -11.31149 | -51.38613 | 2026-06-29 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40a97d56-e4e7-3507-ae5e-5402b110924b | -11.50294 | -54.49653 | 2026-06-29 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4393114c-9fb1-3977-b0ef-8cb42d15794f | -9.14407 | -50.91559 | 2026-06-29 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd30e2da-7974-3be1-91e3-936fb110f240 | -12.43149 | -58.41503 | 2026-06-29 05:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16becada-25c4-3ca4-a525-fc6440f58baa | -10.21314 | -46.50953 | 2026-06-29 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb45e9b2-508e-33e1-8610-79f27484c0a4 | -9.32382 | -58.03136 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edcde7eb-60f5-3ae6-a18c-639b2a78115c | -10.31954 | -50.18644 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bc1eaff-04aa-3591-a932-f75b76b74230 | -12.23024 | -56.55716 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 281aa05d-335b-30f7-a224-eca663f30316 | -11.887 | -57.14848 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16c088b1-6c61-362e-9773-53624bbf9f81 | -9.084 | -59.39038 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 177e9a43-4c46-3852-a8bd-77b4cae87595 | -9.08734 | -59.43659 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e7be2f0-80f0-3ed0-a612-f2f39b3b5f1f | -11.89588 | -57.13545 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c8281f4-9b44-36ef-b90a-4c46a89f48ee | -9.08289 | -59.41921 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2e6460-1ecb-392b-929e-a403f63cc3cb | -11.64363 | -48.53157 | 2026-06-29 05:16:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d188353-596a-3b72-acf9-8037d7235aca | -11.73198 | -59.35762 | 2026-06-29 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43e4a6bc-1a23-3096-9c38-3a89597f1918 | -10.53201 | -48.15779 | 2026-06-29 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37b83a4b-c594-3f26-9ce1-3444ee40edbc | -10.3206 | -50.18384 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1675d19a-a992-3386-84ce-dccdd691c3c9 | -11.20941 | -53.82428 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5c791d-2ec5-3df8-8a03-b12ece85e3ae | -12.51899 | -48.29044 | 2026-06-29 05:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd80c47f-c669-3564-af64-4a78b5efc8fd | -12.14809 | -60.80323 | 2026-06-29 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab8a2522-b55f-3de5-848f-489c32d3fa78 | -9.59892 | -56.92596 | 2026-06-29 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b6955f6-41bf-3137-bfdb-694ab3b0cc7c | -9.68801 | -47.69814 | 2026-06-29 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c500246-f76f-3aad-be36-3c1a6253fd5c | -11.51956 | -54.79509 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2b75eef-b50b-3697-a69f-afd1ddbcb0f9 | -9.09001 | -59.4204 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e1062dd-140c-3877-80d0-6d7480cd9e49 | -11.72224 | -59.35201 | 2026-06-29 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f27203d2-4a80-3740-8fde-7c2b5d4f9184 | -10.28549 | -47.59708 | 2026-06-29 05:16:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ca340b4-6875-37d3-b2ea-f16c1d5cbf2d | -11.87414 | -57.82384 | 2026-06-29 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a310b52-cc36-3c7a-8ce5-cfd357424faa | -9.18892 | -58.06541 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f50502e7-d059-35fe-ad0f-9a8f61f77b76 | -12.22746 | -56.55304 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bb58cd1-37e4-33c4-9f13-3a3687304709 | -10.32698 | -50.1707 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 479bb5b8-3e89-3619-9968-40a43b497f4c | -10.31669 | -50.17859 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f51bb7a-c76e-3cea-abfe-17827afd1b74 | -12.2308 | -56.55358 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e901c949-4f2b-3570-81a2-d88fa279cb1d | -12.2347 | -56.55054 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c68af93-1b1e-3322-8349-28d6f0562f99 | -11.21105 | -54.31072 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f430230-acb0-31c6-aa65-1ad3ab9c1eb3 | -11.9053 | -57.1406 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e440c77b-8e6c-35fe-a202-760d3e916ff9 | -10.82516 | -49.13217 | 2026-06-29 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af742247-ccdc-378f-a580-935ece4bac14 | -11.88645 | -57.13029 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19e84606-c4bc-375b-bd10-20416bbe9f46 | -10.29784 | -57.12549 | 2026-06-29 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20b87133-4c54-3ea7-bf62-4ae8ae9065ad | -9.60557 | -56.92703 | 2026-06-29 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12e934db-c40b-3932-bcfb-053e8d658761 | -13.85683 | -44.75757 | 2026-06-29 05:16:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 088f1e70-2ad1-3b59-81dc-4deb26c6a9c5 | -11.89421 | -57.14603 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3268a04c-60c6-32c1-9556-9ab81c828a46 | -9.31427 | -58.02606 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6ff9d0d-ff01-3307-b3ba-fb94eb18bcd4 | -10.57791 | -57.31887 | 2026-06-29 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03496e8e-df7c-3bfc-ba9d-a9350feb231f | -10.98189 | -49.55802 | 2026-06-29 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1a1fec9-c1cd-3081-b2f0-37d8e75396e5 | -12.54439 | -57.18308 | 2026-06-29 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30142d77-782e-3b01-8e79-0a3ea7051896 | -10.30449 | -57.12657 | 2026-06-29 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0fb75a37-b8f3-3bbb-b131-42511230eabc | -10.32184 | -50.17465 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fa78777b-0151-3ad2-8d2b-64fd4a8e65d9 | -9.33 | -58.03611 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65dee18f-2b21-3332-a493-3e3a69a6bd8a | -11.49879 | -54.50002 | 2026-06-29 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba6d572b-bf46-3b58-a506-96a10320e8e4 | -11.52715 | -54.79221 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35233aa2-b8d0-3a9a-addb-60d175ae42df | -10.78277 | -56.75407 | 2026-06-29 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ff86261-b745-3456-8890-df65b2616e80 | -9.68656 | -47.69789 | 2026-06-29 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d8712bd-6f30-35ea-8a5b-172f1fce429b | -9.33234 | -58.02161 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eefcbb97-d2f4-35c3-b741-1d54a17675bf | -9.08978 | -59.39961 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f39782f5-2ec6-3330-ac2c-3c3211cd0892 | -10.3006 | -57.12954 | 2026-06-29 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 052771fc-b5d1-36a4-b95a-196a47f608aa | -12.28356 | -57.54985 | 2026-06-29 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4132a1c-5567-31cc-9edc-c0c37f842104 | -11.73261 | -59.35377 | 2026-06-29 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65d2b610-dfee-3b72-bba5-d1d305cd301d | -11.52306 | -54.79562 | 2026-06-29 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07b8e602-aa99-3251-97e3-9cb28c32fe9e | -9.18554 | -58.06485 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddf6d042-aca0-3c49-bbf9-ab90d1fd8e7e | -15.07394 | -55.80954 | 2026-06-29 05:16:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3973a27c-11cc-30f6-b636-bc77dfd4df1e | -14.41313 | -60.20452 | 2026-06-29 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5d57ffd-8301-3112-a31d-4f7caabb9ccc | -11.50233 | -54.50056 | 2026-06-29 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61012b5c-cb47-3d81-a42c-4255921dd3bf | -12.20264 | -52.8695 | 2026-06-29 05:16:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b6b357-5ea0-333c-9262-cae90e9953a7 | -11.20749 | -54.31016 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 928a0e1f-aab7-30ff-ba4e-78de1a75ab4f | -9.3222 | -58.01993 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f69a2ac-d48e-3f73-ad8b-1198e3ebde22 | -18.78389 | -57.36381 | 2026-06-29 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 3ad53e24-4331-3961-ab0c-2806dac9e666 | -17.70642 | -46.77662 | 2026-06-29 05:18:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbe9c424-ba8c-3559-b775-750a40f5ced3 | -17.70383 | -46.77393 | 2026-06-29 05:18:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 269515d2-5120-3fba-904a-515b238bfaad | -15.38425 | -59.48337 | 2026-06-29 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d60a67b4-2559-3440-8aed-f4ff756a9313 | -18.78333 | -57.36762 | 2026-06-29 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| decc1755-43a0-33d2-97f2-2d98681da544 | -15.43968 | -59.23414 | 2026-06-29 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a4d3d2c-9c1d-38ed-94ab-8876d0f28840 | -18.78672 | -57.36819 | 2026-06-29 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| eacc1443-46d0-3165-a130-1ecfc5849efc | -17.70957 | -46.78006 | 2026-06-29 05:18:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0d213d8-4e6d-3a69-90ea-97f0312177d1 | -17.70592 | -46.78163 | 2026-06-29 05:18:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2383fe01-1945-3166-9644-e81111f300fd | -18.77653 | -57.36649 | 2026-06-29 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aa7ca0b1-11ad-352f-9fc5-a49d5faee719 | -18.77993 | -57.36706 | 2026-06-29 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 3d5ce979-23bc-33f0-88f5-af9ae1264f72 | -15.38087 | -59.48277 | 2026-06-29 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
