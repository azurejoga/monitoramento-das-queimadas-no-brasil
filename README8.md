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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01ca909a-333b-35d3-8d80-25342fc505e0 | -10.09124 | -52.73836 | 2025-06-16 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9ca675cf-b1f2-3a21-9a8c-f942905ef897 | -11.02808 | -44.64573 | 2025-06-16 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1809df91-80b4-3f0a-a84a-ca526843efc2 | -10.84847 | -53.77909 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea5610b0-dbad-3dd9-be87-ffba1e53a9b1 | -11.14205 | -53.93479 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c836570a-a7b6-370f-89fa-5bc480957012 | -10.7395 | -44.49689 | 2025-06-16 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a3b3068-6348-3056-ba9f-65829ea39466 | -9.40862 | -48.4314 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a22a262-230c-3729-93f6-21e7fbc6f8a0 | -11.00736 | -55.08296 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a59d67-956d-3790-a58b-75843b7f960d | -12.72361 | -46.27892 | 2025-06-16 04:53:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5baa8d91-0c6b-3f72-abe4-4bf233894f80 | -10.07622 | -52.74686 | 2025-06-16 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4c5eb07-1b1a-3d5a-b5e3-1cf4ea79b0cc | -10.85457 | -53.78369 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4911b1e-f343-3569-869d-a01f1eae8c7e | -10.09458 | -52.73888 | 2025-06-16 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 95ce7bcc-221f-34db-9f3b-a7540a190348 | -12.76649 | -44.41101 | 2025-06-16 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a27e1a07-faf2-3bc8-8993-025c87ffbc35 | -10.9347 | -55.33556 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c632a4c-a46f-38b9-a23a-1bb58e982694 | -12.0545 | -48.07439 | 2025-06-16 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 849eaff3-18e3-3058-a08f-4c15226d47d4 | -10.67237 | -56.55675 | 2025-06-16 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98797085-99cd-361f-8dfe-15dfb262cdb3 | -11.13761 | -53.94129 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 90c8d99a-f062-3be6-a473-4ac3ace14da9 | -11.13817 | -53.93777 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c99edd57-8426-3cf1-a66c-12125168e0af | -12.72416 | -46.27455 | 2025-06-16 04:53:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 995fdf51-d66f-3970-9bae-1a044321ac70 | -11.38516 | -56.55423 | 2025-06-16 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac1435c-0305-3e27-8d04-bad204c1a93d | -11.00079 | -55.05946 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee653cd9-6353-3897-9b82-303d7fbe732a | -12.72847 | -46.27965 | 2025-06-16 04:53:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbda9a1a-d4c3-39a6-b4a7-58ee75baf47a | -12.22381 | -54.2984 | 2025-06-16 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88f40cba-eb46-35c2-b1bc-b4280a240b5d | -11.00796 | -55.07932 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29237e96-aad0-3e84-a377-abc7d7bb8224 | -11.00417 | -55.06001 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 032eec7e-4a8b-3ee8-b2e9-8a8e3f0803aa | -11.00577 | -55.07147 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0fe558-934f-3e26-81a2-b48bd8b1e730 | -10.85401 | -53.7872 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcf565f3-cb5e-3be2-822b-c5194747e013 | -10.0088 | -48.22457 | 2025-06-16 04:53:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43c2140e-fa7f-33b5-8132-9c9e5c7ddf03 | -12.1729 | -54.23967 | 2025-06-16 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73fc8d74-cf6e-3e54-894b-eddbaeab5795 | -10.85068 | -53.78666 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86004893-6583-35f4-8ec3-9d03d213ca3a | -12.76605 | -44.41465 | 2025-06-16 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b505162-c5cd-353e-8829-48520cfbe97d | -9.40515 | -48.43215 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 731d3bd7-b859-31f3-9b09-57a6fd207db5 | -10.22518 | -54.2963 | 2025-06-16 04:53:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6e16e33-4a70-34d1-8224-1bceb9c16964 | -9.41646 | -48.43918 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5ae364c-043e-3ff2-921e-eb9fa8e57e1b | -11.14538 | -53.93533 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6a36420-5eef-3b9a-9841-7ee0ad9d08eb | -11.14482 | -53.93885 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b6d7b2c5-db3e-3342-ba43-a7fccc39243f | -10.8457 | -53.77504 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aabb1b60-629c-3035-bfb9-37bbab382751 | -12.17346 | -54.23614 | 2025-06-16 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eefede3-bac2-3eb1-b6a5-272182ef4743 | -10.85845 | -53.78071 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c616cc0d-8a4f-373e-b704-add1dc7ef0ae | -11.40418 | -47.62821 | 2025-06-16 04:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba080a5e-c50c-3ac2-be27-672b6de956f9 | -11.00458 | -55.07875 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fedd7f62-0a12-3230-b5c2-9c1782e30af0 | -10.99801 | -55.05527 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bd4e6b2-b2a0-3c0d-bf64-2559f2415034 | -11.00477 | -55.05637 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d12c828b-4f54-366c-bd49-665b9a90ed57 | -10.84736 | -53.78612 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ebb26a7-e1f5-3670-9790-9ba768487d97 | -12.7187 | -46.2786 | 2025-06-16 04:53:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7bdd3e2-4a52-3ef9-bf1b-aa02ebd135bb | -11.13486 | -53.91558 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d48a2df-5ed8-3f50-945d-011c40e0f115 | -10.91617 | -54.75616 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77032ded-3500-3886-a070-9c286177e08b | -10.223 | -51.65453 | 2025-06-16 04:53:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbb48826-bf61-3039-9290-7cbc2969d470 | -10.07343 | -52.74279 | 2025-06-16 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e95b9ed2-046c-3726-8d22-c7acd7d2f106 | -11.47549 | -48.54651 | 2025-06-16 04:53:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 277a54d7-be0b-30b7-a35e-ef59ee3daee7 | -10.85124 | -53.78315 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 105ef86f-a8f9-3114-a288-e57e83654e37 | -10.56472 | -52.0178 | 2025-06-16 04:53:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 745a8e7f-7ba0-3c0f-ae43-35ac74ee6b47 | -10.09069 | -52.7419 | 2025-06-16 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| bb8ceebe-de20-3edc-b357-148341c4ad42 | -10.73413 | -44.49632 | 2025-06-16 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b003b95-d9b7-397f-8299-f1d1407f3f83 | -11.88223 | -54.68299 | 2025-06-16 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea030265-83fb-3cb6-98f6-5d10edb5df11 | -10.84514 | -53.77856 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66daedef-5352-308a-9193-2809d8b3390e | -10.84902 | -53.77558 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b66257-9d61-3e9c-96ba-6e612527bc24 | -9.48929 | -48.30281 | 2025-06-16 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5f04fbda-9f7e-3d4c-b732-9b17f33e55c9 | -10.56813 | -52.01831 | 2025-06-16 04:53:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca497379-2dd7-3fee-b17d-1ce559d2d50d | -10.8518 | -53.77963 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e3afc52-5f1c-33ea-b5d3-d2d8e0910263 | -11.00139 | -55.05582 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa673dbd-8351-32c7-84d1-17c613e5bf38 | -12.97775 | -48.64124 | 2025-06-16 04:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f3851ee-2689-3e6c-be6f-f97a9da74f53 | -11.78389 | -54.76971 | 2025-06-16 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5869832a-b5e7-37dd-b328-efbd0c5e1f94 | -11.0018 | -55.07455 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88c731fe-253a-36fe-8f87-fdc939bb510a | -12.08996 | -52.57781 | 2025-06-16 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8eb0ef8-0695-3e7e-b6ce-be3fb98615f3 | -11.13875 | -53.91261 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f5b9b83-7476-3489-b7af-49000e20dd60 | -11.00518 | -55.07511 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bd244f4-f5bf-3a11-a3c3-45726187d8fd | -11.0002 | -55.06309 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70a2bbbe-86b1-3521-972b-780540e2fd24 | -11.00636 | -55.06783 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecfa5797-bd6e-3c56-8ddc-d37062a5f1b1 | -9.41318 | -48.43332 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46209b98-6dfa-3940-932b-f98c69f65b7d | -12.05395 | -48.07849 | 2025-06-16 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a3b49e6-0820-341c-a812-bd938fa099b6 | -9.40916 | -48.43274 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 856f18c5-e9d6-3c55-9ab6-63b78f45bf2b | -12.76096 | -44.41027 | 2025-06-16 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e8ba7f6-6f86-313e-a90b-995dae998524 | -11.00874 | -55.05331 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b11cc1e6-037e-3f99-8fdc-de088923dbf0 | -11.00815 | -55.05693 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 332122d3-f05d-38d8-b8a8-38a53a2651ee | -10.21957 | -51.654 | 2025-06-16 04:53:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2226cbd-8282-3d7a-80b4-bf77a05c064b | -11.00299 | -55.06728 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 337c2b6a-4a58-367d-976f-b7902449cf08 | -9.36258 | -56.86077 | 2025-06-16 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 261c9347-ff9e-30a9-b0a9-60a9a6d2c10c | -10.07677 | -52.74332 | 2025-06-16 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf85561f-95d4-3619-a65a-556a85fbe780 | -11.01093 | -55.06112 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8a6bfdf-ee79-32ab-b1eb-e802ac524d12 | -11.00198 | -55.0522 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41c078ef-2173-3e53-95a9-f066c961e5a3 | -11.00915 | -55.07204 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bed7a912-e13d-3541-b4d6-663e7129c394 | -12.72902 | -46.27527 | 2025-06-16 04:53:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2f01094-c59e-3fb2-a338-9cbee2d5d95f | -11.1365 | -53.94833 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe45698d-5c7f-39d9-afbd-2ee3733bceaf | -11.17493 | -47.80056 | 2025-06-16 04:53:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3dc93a4-318f-3f39-91e8-5969f7589418 | -12.97723 | -48.64507 | 2025-06-16 04:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7d00e6b-c533-365e-b478-cfd50b724326 | -7.72155 | -55.13922 | 2025-06-16 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c30b7ab3-ecae-3f04-ad29-8733d32f6706 | -7.11855 | -47.50883 | 2025-06-16 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72c43697-9108-35f5-aed0-6150f7122062 | -8.74602 | -47.17667 | 2025-06-16 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23266fe7-a427-3803-96b5-3d8cb1f33f7c | -8.74656 | -47.17283 | 2025-06-16 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6fa6def-b18d-3219-821e-f68d3e4e95cb | -9.04529 | -49.69118 | 2025-06-16 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7bc365e-1765-386f-9833-a74c25a8dfed | -7.13812 | -47.28544 | 2025-06-16 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08420fce-ae87-3051-b8fc-f7970452c95f | -8.4021 | -47.45997 | 2025-06-16 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91f537fc-c9df-3d35-b7af-8e2f9df66d88 | -9.16414 | -45.32764 | 2025-06-16 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84a019ac-474a-300f-bd15-2f168ceb3bc6 | -7.1139 | -47.51183 | 2025-06-16 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fad5948a-256c-37b6-abc7-f48082c422c0 | -7.11444 | -47.50811 | 2025-06-16 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2495d2d-c37d-3d32-a621-7aa3acbc4a77 | -8.7417 | -47.17607 | 2025-06-16 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab71d2c-1dba-38aa-8f2a-380696f0177f | -7.72502 | -55.13979 | 2025-06-16 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87585ef5-a167-388e-9f3d-ecb4dc15f198 | -7.64225 | -48.31643 | 2025-06-16 04:53:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 25bfe5ee-0912-343b-8b90-ca4789af2e4b | -7.92701 | -47.80745 | 2025-06-16 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a550aa1c-ac1e-3b5f-a260-918a3379dc21 | -8.9008 | -48.84478 | 2025-06-16 04:53:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
