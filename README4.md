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
| c08b35be-cf2e-3bdf-bcf3-988cadf19048 | -6.99304 | -42.88704 | 2026-05-31 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9df49ecf-771b-375d-a1f0-bcab35ede2d7 | -21.32685 | -47.77309 | 2026-05-31 03:47:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70f671ac-ce24-3886-a42b-ce77d0cd2723 | -24.51863 | -48.8568 | 2026-05-31 03:47:00 | NOAA-21 | APIAÍ | SÃO PAULO | Brasil | 3502705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e7d6bc5b-bd86-38c3-9d47-c12f336c7cb7 | -18.36882 | -47.57861 | 2026-05-31 03:47:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92686d2b-8927-38c2-85b5-872daa4a0acc | -13.54154 | -49.90054 | 2026-05-31 03:47:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9939069b-ad8a-3e2d-912f-3f5a27c8db1a | -13.54024 | -49.9066 | 2026-05-31 03:47:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0f9be14f-c00d-3e9f-a9f7-f371f34a9f68 | -21.32424 | -47.77162 | 2026-05-31 03:47:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e3d760d9-b3ce-3e0f-9b60-2b04634ff6bb | -21.40012 | -45.49042 | 2026-05-31 03:47:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dc7b0f72-b27d-31b8-84be-f54e358ff800 | -19.8645 | -43.87289 | 2026-05-31 03:47:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e05a8c68-c626-396f-ba03-9451ecdc457b | -21.3249 | -47.76848 | 2026-05-31 03:47:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f08badd-d45b-3cc8-a1dc-1b361baa1884 | -21.32755 | -47.76989 | 2026-05-31 03:47:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 48cc3839-806a-3791-9abe-55e70201e343 | -21.80826 | -49.13275 | 2026-05-31 03:49:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 209112f6-36a3-3b70-83c7-6a7b9d6b8e55 | -21.80914 | -49.12884 | 2026-05-31 03:49:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0d7bfec6-be7f-3fc5-a839-e93f7532d083 | -21.80824 | -49.13129 | 2026-05-31 03:49:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 03099ae5-99a9-33ef-85dd-15ba3feff800 | -21.8091 | -49.12738 | 2026-05-31 03:49:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 85e1a2ce-48ee-31b9-ada4-833c55a4acdb | -21.80367 | -49.12595 | 2026-05-31 03:49:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c1bafdd-f51e-326e-8d78-e40a01871e13 | -21.80372 | -49.12743 | 2026-05-31 03:49:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c384f614-7118-3491-b74f-f2fc2cb8b56f | -10.0725 | -51.6559 | 2026-05-31 03:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| d5114d73-25e7-3390-9da2-767f9332f02b | -10.0537 | -51.6576 | 2026-05-31 03:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 758b65e4-a21f-334e-ae49-a54c2f7af9fb | -10.0723 | -51.6769 | 2026-05-31 03:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| b2b979dc-8ff8-3208-b980-11f8a8913e0d | -10.0537 | -51.6576 | 2026-05-31 04:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d29cf0db-a08a-3e7e-b1d4-8d6aa4839662 | -10.0534 | -51.6786 | 2026-05-31 04:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 22cbe5fa-186b-3490-8252-884c0e78621e | -10.0723 | -51.6769 | 2026-05-31 04:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 1b15fac5-80fd-3f3f-9a90-4b4a183aff56 | -10.0725 | -51.6559 | 2026-05-31 04:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 1878ae91-38d2-39d8-9ca8-ff899a4df68d | -10.0537 | -51.6576 | 2026-05-31 04:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 35ae23ac-b235-3ebc-b9bd-c911258087d4 | -10.0723 | -51.6769 | 2026-05-31 04:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 37f010a0-5483-3545-8f1d-6d7b96246a5b | -10.0725 | -51.6559 | 2026-05-31 04:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 370d86fa-3892-3aa0-ae1d-b3b9213b789b | -12.317 | -47.89824 | 2026-05-31 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3b7981b4-917b-302a-b260-d9d1b3dc9c48 | -9.44853 | -51.82639 | 2026-05-31 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc1bfdff-2a6a-31b7-a470-86d9610b1fd1 | -10.06666 | -51.64984 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a80a3180-cfd9-3dc5-833f-3d77f71c890f | -10.80995 | -49.33689 | 2026-05-31 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fdf0d27-a7e7-328d-abcf-d52248f2d3c6 | -9.4946 | -48.66026 | 2026-05-31 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2297661c-df8f-3be5-9082-4e55a7b34aca | -10.80554 | -46.90495 | 2026-05-31 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 839b3d0f-f95b-3cdc-812d-645417053515 | -12.31609 | -47.90348 | 2026-05-31 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f1986fa-b85d-3f26-96df-ea9ec7a66883 | -6.83864 | -47.93522 | 2026-05-31 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73d0f1e2-4292-3376-8a02-1d792e28c0b7 | -10.06104 | -51.67961 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 423eff23-0233-3a7d-8b4d-f012cf218c04 | -6.8379 | -47.93946 | 2026-05-31 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4443dcd2-0f32-3197-9dd5-8e32228dfdd8 | -11.62451 | -55.17038 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 878d3bc5-a7c7-3de0-8b52-95c7be1d7a1f | -10.13882 | -48.0797 | 2026-05-31 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c101d5da-2b18-36ae-9ea1-b6c528082464 | -5.49385 | -37.24453 | 2026-05-31 04:17:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5599af5e-242e-3e30-85dd-524052475cb1 | -10.06542 | -51.65637 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d1f53c8-5fd9-3993-bc02-aa9a981ed32f | -10.07131 | -51.65413 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fce7d197-1104-3bed-aa99-0a2f2d1c434a | -10.07007 | -51.66073 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34873f86-6b94-33aa-ba4c-809ea73acf92 | -10.06291 | -51.66968 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b57afd9e-894c-3e47-b031-50dc5a7197cf | -5.80081 | -45.13229 | 2026-05-31 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b828f401-dd07-3c54-8fa0-038b0b345a1e | -10.06229 | -51.673 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b91a3afb-5639-3ae1-b676-ddc32d8d12c8 | -10.06881 | -51.66739 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 92b362b4-2ba4-3204-911c-aa970115ce1c | -10.62838 | -48.32698 | 2026-05-31 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69c3d684-1778-327f-875e-ffe33bb26847 | -10.07159 | -51.68169 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 088742d5-d26d-3636-97d0-8b121a0ba778 | -10.06819 | -51.67071 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5f80e172-d03a-307f-905f-137a102bb5d4 | -6.84296 | -47.93605 | 2026-05-31 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc4b621c-8163-3605-984a-d137548a2e88 | -6.83936 | -47.93103 | 2026-05-31 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4f5ff33-5142-3420-83e0-e421fb8b7085 | -10.06166 | -51.67632 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 76ddc9fd-d572-3512-a380-5315af8f7c01 | -9.49024 | -48.65947 | 2026-05-31 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a96c5e3-0efa-3833-9660-253911d969df | -10.06756 | -51.67403 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e905c17-a871-324b-a2ec-136b70fa07e5 | -12.32005 | -47.90423 | 2026-05-31 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7aa19d6d-eeb8-39dd-8c75-a63327ef20df | -10.06605 | -51.65308 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c5739968-8c3a-3d66-b664-53f809867c90 | -12.32096 | -47.89897 | 2026-05-31 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ffdcb003-69d3-34a1-86bd-3d91ed5fe6c0 | -10.057 | -51.67199 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 134e2de6-8c11-3719-813f-92a1790427ed | -9.44788 | -51.8299 | 2026-05-31 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 513f2589-0ad8-31cb-8922-c6f982989c82 | -10.75788 | -46.91754 | 2026-05-31 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f09ed8ba-afef-3dce-8a97-4f886ed4696b | -10.06727 | -51.64659 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 82efbf64-1bad-35ac-a289-cc950089a00e | -10.07408 | -51.66848 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d430e741-2aef-3ba9-9a84-f458f6ae46d3 | -6.84369 | -47.93185 | 2026-05-31 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4513b758-17a3-3a72-bbe9-1eeeef37700f | -5.80524 | -45.12852 | 2026-05-31 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70217775-fd31-35d3-96f9-d2a3fd9ea32e | -10.06944 | -51.66406 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 16aa9247-df72-333d-ac50-9645b3e93872 | -10.07254 | -51.64762 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb4eb699-1cea-322b-bbfd-5ce66b0ab2ec | -10.79109 | -46.89746 | 2026-05-31 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5742b121-92e7-3ff3-90bd-f621851e4808 | -10.63323 | -48.32388 | 2026-05-31 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d30ff5ad-9b5e-3ad9-b222-2e80bc2efd15 | -9.45392 | -51.82739 | 2026-05-31 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 125e6654-4ae4-3086-a22f-83dcdeeae29d | -12.12604 | -47.21801 | 2026-05-31 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce4feab2-d057-3752-8af1-7b06afb21eb6 | -10.47278 | -48.67461 | 2026-05-31 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b04e0acf-2589-314b-99e4-7b9e979586d7 | -10.39045 | -49.44491 | 2026-05-31 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64d6f1eb-de14-35b7-8218-141430956d1c | -7.07791 | -46.28545 | 2026-05-31 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b4fc826-04c0-30b2-a8b1-98bd0f4ade8a | -11.62981 | -55.17696 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef5c1917-2ad2-3157-9353-00bba9c082ae | -12.12814 | -47.21617 | 2026-05-31 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cbd533c-526a-3c2a-9e0a-eb442cd076ca | -11.62863 | -55.17803 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c975add1-e23a-3ee7-9136-5e0a1659d26c | -10.05396 | -49.11512 | 2026-05-31 04:17:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2af3cfd3-304b-332a-8cc4-ce5aa8531435 | -10.63256 | -48.32777 | 2026-05-31 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b44a7921-3c5d-3476-a28e-37bfc99e44a6 | -9.45869 | -51.83185 | 2026-05-31 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce091001-8708-3045-9944-40a5926a60bb | -10.47051 | -48.67411 | 2026-05-31 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1222fd8e-9797-38b7-998f-8732513c1fcd | -11.62125 | -55.18615 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2201b1f7-35e4-32ad-aa99-ecd9a756d88d | -10.05826 | -51.66538 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4d13fb43-db18-3a7c-8000-3f03b089cc2b | -10.51429 | -42.3711 | 2026-05-31 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c6a26009-1717-3f8d-ae18-da5787e955f0 | -6.04567 | -47.89217 | 2026-05-31 04:17:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8633ce2b-f486-3914-899b-3df8eef3e6b8 | -10.46845 | -48.67408 | 2026-05-31 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1a119f4-0f91-3839-b9c1-2637d7e71585 | -10.06417 | -51.66304 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 96cfacf1-25f4-34dd-9f4e-f1bb02911c4c | -10.07656 | -51.65528 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 42e9476e-45b8-3d9e-986d-459da0fed663 | -10.06631 | -51.68065 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aaed8f6c-8ace-30d1-a040-e8374b4281cf | -9.45329 | -51.83086 | 2026-05-31 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29223ead-3489-3e44-b95b-7db173ab1a2d | -10.14013 | -48.08032 | 2026-05-31 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fee492a-893d-39ef-85ca-f44a8dd907bc | -12.31121 | -47.90796 | 2026-05-31 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd95b6cb-d753-3744-b66c-e160646cf06e | -13.55737 | -43.59067 | 2026-05-31 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 466bf58d-a0c5-39b9-bece-c92ff559cbcf | -11.6212 | -55.18195 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d063d576-0860-3963-b7da-86326b9994e4 | -11.62014 | -55.18725 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69728d3b-ef39-3dcb-9746-e055ade35f51 | -12.12986 | -47.21868 | 2026-05-31 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d80e11b4-ff33-3305-880e-226200988639 | -10.06694 | -51.67735 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| be86bfb0-cd67-36a7-a971-8fe1105bdaf4 | -10.07594 | -51.65857 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f764d84-fef6-38c7-a916-51d4f7207819 | -11.62234 | -55.18087 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eee7091-a86a-3969-b599-64f70798f59b | -6.05006 | -47.89289 | 2026-05-31 04:17:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
