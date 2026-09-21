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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bdffa85-b0fb-33ce-ad45-19a29c97625d | -10.7443 | -50.79868 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 799545e2-891f-3564-9aa0-a7195866452a | -7.32582 | -55.21627 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6647f85b-5ef3-30f9-8849-103a8f26149c | -11.0518 | -54.91694 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dde6dc80-0c7f-3fed-8558-02b77aa403c7 | -11.00046 | -48.23379 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f268cf1e-b821-3d92-974e-a4ead90782a4 | -10.85566 | -50.16172 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81f0844b-df76-3469-9079-9066b383940c | -9.55664 | -66.03773 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f07b984e-1f63-3bd5-970a-9794fbed9d91 | -11.75597 | -54.57267 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d5fd87-d9b5-3fb6-9b36-c3855d2462c9 | -10.87213 | -50.92815 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 957e4c2f-279d-3bf6-821f-b488fa79efb6 | -10.67253 | -50.73034 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 430ac60a-9a6c-3ccb-b3f2-9d62a030c066 | -12.10951 | -47.05032 | 2026-09-21 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db3f09ed-5564-3f12-a51b-5873decb9355 | -12.82716 | -54.0529 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a7e77c3-2b48-399e-9726-a6be52daad0a | -9.03324 | -48.15761 | 2026-09-21 05:06:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2308d6ed-6591-38b2-a5bc-65fdae523909 | -11.73847 | -54.56318 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ac26282-09a0-3eee-ab4e-bb0a9b22d835 | -9.45916 | -54.92787 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 851361dc-be68-3edf-9d12-c050d8ba9f4a | -10.42429 | -50.24158 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f509ae04-a23d-34f2-9c95-f0dc1228e31d | -10.22338 | -59.40177 | 2026-09-21 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b418116f-78aa-33f5-a826-3f09ecd6e11a | -9.61353 | -55.11632 | 2026-09-21 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33834b21-3639-3e96-937b-51309f805ff2 | -10.81189 | -50.83576 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d9089a2-277c-3d30-ab7b-57b8f210ede3 | -6.45205 | -59.98269 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c0b8656-ef93-3d3c-b40e-955808d022e5 | -6.45278 | -59.97812 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ba26231-7e95-3e6f-af25-fd2ff2e0e820 | -10.42486 | -50.24922 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 355d1a41-622b-3b93-9454-34f0fcc3c78d | -6.7609 | -59.11259 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fea0dc16-94b0-38e2-9bf5-851cd7c9aec5 | -10.5433 | -57.44486 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed877c7b-24ab-373f-abb5-2d611979ca74 | -8.54448 | -54.69207 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22055507-50e1-3b84-a921-2b24934e2fc1 | -9.94491 | -45.68282 | 2026-09-21 05:06:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e364eccd-44af-3f51-8e0f-1c9ad3aedb13 | -13.27577 | -51.7572 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c114e201-013a-3f79-ab0a-30727acd1c11 | -7.57397 | -57.6758 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b73b4ddf-d257-35bb-ad28-b9177ca29af3 | -10.43533 | -50.26152 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efc924f1-d7cd-32d2-a72b-07ec0ba8c5b3 | -11.01908 | -54.14406 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84311893-b47f-39e4-ae31-5c16e4879c70 | -9.82349 | -48.4374 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fef08fd1-c690-3e19-b9de-13dbab24cfcc | -10.67312 | -50.72612 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0443bf47-35c6-396d-aaf5-e6120a824232 | -10.67986 | -48.72264 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7d41f072-62c0-304a-9a1c-79332271f885 | -10.90143 | -54.08201 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ef6390a-eb0e-3bd1-ad6b-8a3d2fbf80fe | -11.04946 | -47.67292 | 2026-09-21 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df761af1-8d4e-3a08-8dcf-caa72a38a770 | -11.05238 | -54.91312 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf66ea9c-0b39-34ab-9fca-712644e5198b | -10.68248 | -50.22741 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ed13055-7934-3d57-bd38-7916f1b82c35 | -11.05409 | -54.90175 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 832fd0b9-b752-33ac-8562-4938d2c124ac | -8.79278 | -60.79946 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37f347fd-d633-3034-87cf-e4cea99e6609 | -10.93269 | -47.87066 | 2026-09-21 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a7673a0-33b9-3568-97d5-a562afebdb65 | -11.72326 | -54.569 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0804957-a63b-3f7a-b820-dee89e671a81 | -11.792 | -46.84535 | 2026-09-21 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a36da7ab-fd2a-3f31-bcdb-0d7ffb4b810b | -6.68207 | -59.10868 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 720d8c66-4ce2-33c8-862e-4ad64723662e | -9.67822 | -54.33065 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aff8ed04-ba0c-3c9e-b059-7b8906e21e7d | -9.55475 | -66.04787 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b53a4f25-b34e-39c7-8617-b06b25211a1c | -11.01788 | -54.15221 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f0be6bb-a2f3-3b2f-85e7-755b62632a9b | -11.47515 | -47.77315 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aac4d604-458f-314a-914b-501fe1c70eb0 | -8.78099 | -68.84315 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da14a898-b654-3329-835b-efd3d8cd22b3 | -11.41942 | -51.44413 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8508f9f-4539-3e95-993a-c63731716e82 | -10.776 | -50.8245 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8794c41a-6038-3fd0-86b5-7c89e8fb65a7 | -10.90808 | -53.96103 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 953e7c59-cf89-3b67-a839-1a0746ff92ac | -10.54305 | -54.49975 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ee8da8-b415-3b8d-a8be-ec2d52270057 | -7.58314 | -57.67398 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5856b7-7a06-3983-b022-25289949da21 | -9.67359 | -54.31389 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5d9080b-8888-3996-94d9-e0b9abe239e4 | -11.85206 | -46.89112 | 2026-09-21 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2747a814-4b9c-3059-849a-4f05a3e0ae7f | -11.09991 | -51.0655 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42da85cf-b971-3c7f-ba2e-0f2cab2a87be | -10.6774 | -50.73769 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5909459-b696-38be-8550-a1bb5fca4a79 | -8.08117 | -55.34386 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e18ad92-d364-3cb6-b575-7e424c6c5f47 | -9.45665 | -45.39788 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| eb588981-ce3e-34b5-b39a-8a700424708c | -13.72082 | -48.79126 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeef2e81-5952-35d3-b615-69500636737d | -9.44225 | -45.41431 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca345dd5-416e-34b7-b663-aaa8ac86d61a | -10.80757 | -50.83514 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cba22ed-e67c-3b60-99b4-9627ed7cd85c | -7.58813 | -57.68586 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3635b8ce-2c8e-34c2-9ffd-00ac4f207d7a | -11.09988 | -48.29607 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c783d32a-ebc0-30b0-95ee-43905a79e8f5 | -8.18796 | -54.73221 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd1835b6-15ee-35fc-a21c-e079fc3377a4 | -7.87662 | -54.70378 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45864451-5775-38d7-bc1f-5e93c4f4917e | -12.32431 | -50.69559 | 2026-09-21 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26a9e314-12d1-33ed-beee-811aa0f0cf3c | -10.88482 | -54.07117 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5ae3d7d-4cba-3607-98c3-f8560e3b5cb6 | -10.46547 | -61.31579 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48810243-43d9-3772-b0ad-f409930ee5a0 | -8.85268 | -62.36386 | 2026-09-21 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b93469c1-a30f-3ce9-bc12-7cca65944101 | -11.04434 | -54.8964 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bce5fdf-4cfd-3684-bcf0-b55c66f52133 | -10.6292 | -53.89353 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b34b3d3f-b396-378f-949c-e9674907adc1 | -10.76656 | -50.81221 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2721c1d8-2799-35aa-a69b-772eecbeb6bb | -9.55005 | -66.04343 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 368963c0-e4b3-36e2-8184-a8364aac7dac | -9.55762 | -66.00285 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a0374c8-f746-3b40-b4cd-4aae5ed1e8dd | -10.79711 | -50.74806 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28145a67-f53e-3719-8539-5b128eb46276 | -10.46165 | -61.31492 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80a70c5c-bfc8-3f93-a7bb-0e5b17a8c5b9 | -9.66432 | -54.32848 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 656f0134-c802-32f5-8d33-79d240cc723b | -12.10354 | -57.19149 | 2026-09-21 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09931659-b845-3591-a4fe-ca3e40486ceb | -11.28158 | -54.12554 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c85aa5f-09db-30a1-af3a-8c07ba12a22b | -11.27449 | -54.13024 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afc3d714-c576-358f-a7fa-1f884a093f0f | -10.38062 | -48.91319 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 87c9ae4b-2eb4-34b6-ac18-7717327169bc | -8.77543 | -44.29802 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 649823fb-116e-3fdd-9415-61fa5c62729c | -10.87594 | -54.05717 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 224940e6-e475-3f49-91eb-6aed371eaf54 | -10.12434 | -48.44222 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef257932-a3da-3bd4-9aad-6c25431c5ff6 | -8.65705 | -62.48726 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 347ac238-dca7-30db-bd24-349ef1acac88 | -10.14268 | -45.55461 | 2026-09-21 05:06:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab382ce9-4c98-344a-b7ad-268840cc83ea | -7.25154 | -55.60874 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 395f5f05-4b18-377f-a2f6-6d642cac8b2a | -11.03033 | -54.14155 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6d89a82-0dcc-30e2-a4fd-004a4eb6bd3b | -10.88661 | -53.98315 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28596c28-6574-3893-9dda-d3651110f939 | -8.18188 | -54.77237 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cceda42d-43a2-3c80-a9e7-74fb67642c5e | -7.6417 | -55.06523 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bc4df27-499d-3eba-83be-43843625f4c3 | -12.10999 | -47.04639 | 2026-09-21 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df65598d-3f2d-3a33-8319-74411c49b89d | -9.74892 | -46.24413 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65b70596-78e9-3d70-b2f2-52ba165af810 | -6.78112 | -58.60949 | 2026-09-21 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98bab765-feef-39cf-8ff0-383d36f154d8 | -10.76979 | -50.8212 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c3991ff-72ec-3859-b7f3-da72197ca13c | -13.06718 | -50.627 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1e26f23-36ff-3c0e-9aa2-0f01a998e99f | -9.02902 | -44.92078 | 2026-09-21 05:06:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0af15d67-e0af-3122-b626-4bbc42cb7c84 | -9.53787 | -45.39391 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab1cd832-0907-352e-a26e-bcd588fd5f36 | -6.8291 | -58.98002 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86df12a9-9708-33b2-9da4-04b8e3a83d7d | -6.78217 | -58.93605 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README77.md)
