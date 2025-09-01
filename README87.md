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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a094709-00a4-38d0-837d-8a0392671ae0 | -7.10799 | -63.02883 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d17a8be5-fba3-33cb-abb1-1e12fd6cab58 | -6.43011 | -55.61673 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd4e7915-ad73-340a-8eef-48b4531ab84c | -6.99058 | -63.01375 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f1e2a7e-4b2a-334b-8870-78cedfe77829 | -6.83242 | -52.80967 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ebf0eed-113a-373f-8081-f94513527f1e | -7.28454 | -60.66319 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5eb4c1dd-0b65-32c6-b269-ef5b8685a37c | -6.82947 | -52.83136 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 323f7536-ce12-3df5-a821-dd545b0769c9 | -6.82512 | -52.81822 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c9896cd-7cb5-37e3-84eb-d87ab3f26399 | -7.27759 | -60.6488 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e374b01-4422-3c34-9bd8-d514fae4d7c2 | -6.82419 | -52.82543 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d6117f8d-928c-3908-8b0c-0364336be10c | -7.69159 | -61.10012 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4060317-07d5-3079-afb4-c90acea04edc | -7.54095 | -63.84396 | 2025-09-01 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 682e89c6-9174-3c23-b35b-45a1540a0d50 | -7.5901 | -61.63196 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b1372af-a888-3554-a7c2-89892b579d13 | -6.81677 | -52.81556 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29cb0193-c92b-33b1-9db8-ce57b6714515 | -6.83968 | -52.82037 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0c7ae5f-4d58-38c5-850a-1f40aca8f149 | -7.59843 | -61.63312 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90196e80-eaaa-3220-990a-b56d7bf91ce1 | -7.67523 | -61.08265 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b41b05d0-781f-3383-837f-3ef0b37c18be | -7.06726 | -63.06952 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e96eb970-c317-37aa-b72d-3b8ab87c8b94 | -6.33181 | -53.44069 | 2025-09-01 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81873670-60f9-3fd1-812a-0566799c0b4a | -6.43627 | -55.61746 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dff0f4b3-bd45-31cc-931e-ba13d3634b34 | -6.82604 | -52.81109 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5590fa01-2922-3905-b1f2-082dd0e07be1 | -7.09625 | -63.13432 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fce9e9a5-3af8-3ff7-b1f0-887a9a249adc | -7.70313 | -61.47602 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c29b72e5-6b64-3c4c-8f4e-64315a084ff7 | -7.07579 | -63.06396 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7070e028-2e84-3bfe-8daf-a24ceddb5ae4 | -7.07858 | -63.07123 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6753690e-6b37-3a29-8c2b-aa6ddf22f68f | -6.9097 | -62.9383 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf71aca-618e-3341-a70e-60fc84debaf7 | -6.44179 | -55.62292 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c43e639b-21b4-3393-9c6e-9892dcebbe57 | -7.08249 | -63.20138 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a31e26-41e3-3519-8489-3271284b69b2 | -7.5753 | -63.04669 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2b7668-9fd4-3ee7-8a7a-b41bf5025476 | -7.68093 | -61.0817 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d29d8ac-5b81-3bb6-89d3-556e58677eaa | -6.85613 | -52.80811 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54904f11-464c-321b-9056-dfe3386d6620 | -6.34128 | -58.18036 | 2025-09-01 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d75f28a-a4aa-3e78-8126-59cf8eef8983 | -7.68035 | -61.08588 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8b9ac9c-3e06-3f1e-bf80-0cad7c24bd7a | -7.28517 | -60.65884 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f9506ca-1afa-3bd7-8731-a8c97c95fcab | -6.79495 | -52.81228 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5949b95f-fd6c-309c-8e25-0bf3abd5cd78 | -7.67894 | -61.08746 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 285b011f-7c65-338d-8ebf-addf932e1818 | -7.06516 | -63.0577 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5583a04a-a5ab-3015-b7dd-e4bb3bd61d54 | -7.5676 | -63.40995 | 2025-09-01 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a234ef28-b746-3869-856c-aedc2c74c2ae | -7.59427 | -61.63253 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74400d2b-269a-3446-af9e-0b9447447d3a | -7.59122 | -61.6244 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a51cfa-33a7-3086-a634-1e3442ab374f | -7.0583 | -63.052 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb740c8d-0d60-374c-b169-abb8265a3da9 | -6.8085 | -52.82185 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00a748ee-5ae8-3aaf-930a-6d1bf4d730ff | -7.09529 | -63.0363 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14433468-b1d1-3fb2-84fb-98617863fa07 | -6.84792 | -52.81407 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d36ee31b-2993-37ad-be98-c4be3402e40d | -6.79687 | -52.80707 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d790288-e6b9-37b3-87bd-baea7a69b1fd | -7.65736 | -62.54841 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aa504e4-d99b-3bdd-a75d-4609e083e07f | -7.07103 | -63.07009 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2582622e-1ffe-31c5-940b-d92f0f57ce90 | -6.33354 | -53.42769 | 2025-09-01 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9dfd0d6-8846-32e2-8297-8fbdbb9ce58d | -6.34172 | -58.17728 | 2025-09-01 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b999148-5425-336f-ac2e-79bf468b1e27 | -6.81578 | -52.82286 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f2f8b1c-6242-3c42-a6b1-b9a0e47846f4 | -6.43001 | -55.61765 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f30e7b43-9243-31ea-8713-7f88eb8c92ee | -6.84066 | -52.81285 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d901991a-8eef-3184-8c34-5d02e9a71d82 | -7.69836 | -61.47926 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fceb886-45bf-3bd8-a3f4-ab3f4c82a945 | -7.67955 | -61.0833 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 17c7225a-bd87-3717-90d4-53902386ed0e | -6.83876 | -52.82746 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 37c736aa-6e3b-3d8b-ad3d-45aa2841a48f | -7.54158 | -63.83974 | 2025-09-01 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6ede3b3-2407-3925-82e3-9a96ab1a3a1b | -6.33267 | -53.4342 | 2025-09-01 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d64647db-2986-3627-90e8-06dc88dd4a9c | -7.27696 | -60.65317 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 204e5002-2a46-351b-ab0c-d241894f2f5e | -7.73256 | -61.57338 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7da51007-f6c5-369d-9d65-9329f405b0f9 | -6.80219 | -52.81358 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33b0107c-510e-330f-b16a-297cc12bd5e8 | -7.07481 | -63.07066 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43212e7-6b76-39bc-bd45-d2640cb860be | -7.6841 | -61.09065 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c452285-12a4-37e7-b18a-5e817755b591 | -6.34084 | -58.18344 | 2025-09-01 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af3e253e-13a9-324e-aed2-ca59228485b0 | -6.43689 | -55.6128 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d0d583a-14bf-3fb3-af77-fc8a5b33031e | -6.82314 | -52.82333 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c31401e7-49b5-3e58-83ee-706cdcf0ca97 | -7.28202 | -60.64946 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46b8824a-6cdf-3e14-a0df-84b82a854420 | -7.5865 | -61.62758 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebd12bcd-daf4-3390-a4bc-d542232d24b9 | -6.43067 | -55.61298 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609a0788-be64-3b95-9387-f8f6d5e69f5f | -6.3404 | -58.18653 | 2025-09-01 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9297b721-c44c-3d15-a4a5-b257f7227098 | -7.70023 | -61.10138 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a9a25dd-1dc3-32ef-8fb5-62ad05b7ae11 | -7.10731 | -63.03342 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac7f467-2bae-32b2-b81b-7266dca0bf7a | -6.43074 | -55.61205 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53ca9d6-c653-3868-89bf-a7b251a7343a | -6.83337 | -52.8118 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ec2f6e1-d5cf-3759-b962-685d873dbc01 | -7.67834 | -61.09156 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0601cef-d76f-3e96-8584-fa78be066b5c | -6.84697 | -52.82136 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a08cc7b7-1c7f-3da0-ae39-c0e4a39b9b4d | -7.58706 | -61.62379 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06963df6-3a3d-3743-ac51-88fb613a0983 | -7.09182 | -63.13828 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f8df4d3-9786-3099-817c-f143bf4501cc | -7.69533 | -61.10487 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfdcd9fb-2d7b-3fbb-a2b6-e961e60a630d | -7.07063 | -63.07253 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 702374d8-cc36-3d79-9e36-bf0b79ab63ec | -7.09558 | -63.13885 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7745fc2d-6741-349f-bbfa-93ad90405dc6 | -6.86342 | -52.80912 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17bceb5e-eb57-3096-905f-0a564ff0e39c | -6.33967 | -53.43517 | 2025-09-01 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f33b7de-8400-31e5-b070-95189333c2cb | -7.69415 | -61.47862 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bada492-6050-3e71-9597-55a5c9a1cb5f | -6.82216 | -52.83055 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 685d6a98-4bc6-38ba-934a-bf2795c1d612 | -7.28581 | -60.65446 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f591501c-c67c-3cdb-b4c0-a95091fb3f21 | -7.28265 | -60.64506 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c560b2fa-574e-3fea-889c-9af72a349a9e | -6.3388 | -53.4417 | 2025-09-01 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb3d2af7-5c85-398e-bf02-715a789a0826 | -7.69892 | -61.47538 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5e7599e-12b4-3e6a-9cf7-750f48755738 | -6.83242 | -52.81915 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e95aa08-42d3-3305-9d5a-d3b6ee4f3cd8 | -7.07547 | -63.06608 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c7ede7d-bda5-3bb2-abfb-d6bc7112b8ad | -7.28075 | -60.65819 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc907de1-beff-3dbe-96da-988ad6400ad4 | -7.10285 | -63.03745 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad617da1-a498-36aa-bf76-611cf3b665c5 | -6.83143 | -52.81692 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e8bf83cc-9396-3996-87fb-55bdf6e47c06 | -7.69591 | -61.10076 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10693ecb-723a-3640-88f7-c9bd7dba69f6 | -7.09839 | -63.04147 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecc7fdf6-73fe-33ba-b1c2-e158dd1ae90e | -6.83149 | -52.82635 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7ee06f5f-fa15-3d87-b49d-71396537bb41 | -7.0751 | -63.06853 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca03ea61-25b3-388b-a57f-88cd02608574 | -7.45068 | -63.15762 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2952ed83-b405-3384-9dd5-4c445e2916f3 | -6.83056 | -52.83353 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e7e3a7df-a9bc-3126-872e-e50cece4faf0 | -6.85516 | -52.81549 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9615e1e3-efd5-3500-a47f-1cf4b1da6d8c | -6.9135 | -62.93887 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README88.md)
