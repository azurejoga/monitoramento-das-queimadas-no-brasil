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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02c43872-c714-3755-8941-fdc9fd9113b0 | -3.34359 | -50.35863 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4974f8fd-170b-3fc4-8267-8f955933a235 | -2.89139 | -51.75355 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fff8282d-3cb0-3826-a2ba-1928461dea3f | -4.42475 | -45.623 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 872dd072-ea19-3f19-b47e-d617ada8b247 | -5.96899 | -45.36531 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0615b234-bf72-33af-9127-a118b956dd1a | -3.24086 | -50.58459 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c30e0b87-4c36-3cd9-b7bf-33c172ac3a49 | -2.17814 | -51.42799 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ecca748-f0c8-300b-bc9e-fe4b5f68413f | -3.24562 | -48.74771 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ded6c70-34d9-3c97-8f14-29b8d15c8dd1 | -2.69988 | -49.32983 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7097713a-1c41-38a5-b0ff-88279f34efcc | -2.65733 | -48.48621 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff3926f-664b-3b11-ae5f-685a73c2fea7 | -4.00524 | -49.01927 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e30cddbf-88ac-3e61-8043-bd1f83950778 | -2.82876 | -48.47058 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74427a14-4d92-3ae8-b5b3-0ae6b510f9d7 | -3.0366 | -50.42062 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84efe032-52ff-3f93-8b83-947603ccf7e1 | -3.05095 | -51.09013 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bc0f9cd-44e9-3997-878f-667a7fece080 | -2.87747 | -51.4719 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3ee3a43-6e2c-3561-9ecb-e5d583f0b622 | -2.93591 | -49.51075 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 557e6a44-6984-30d5-ba3c-af35701760d9 | -3.03778 | -48.04734 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b53ce9bc-8e37-3c22-8ce4-ac864b11d58c | -3.11761 | -54.27632 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db4517a-1611-3a0d-b346-889be526ecd7 | -3.32857 | -46.41296 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46cb2d4-0700-3456-a723-c9a8e4199783 | -3.03354 | -54.20763 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49e264f6-0ac7-3e80-8682-18d48ebad461 | -2.31261 | -50.671 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e28257-4429-355b-b834-b119b72f40e8 | -3.24616 | -48.74427 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f11985d-ac3b-37d0-b31b-3684fd547360 | -3.35382 | -50.11835 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 993949c6-b705-3ab7-a2ce-cd8fd74b77f5 | -2.81783 | -52.96504 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dad9b4e0-abcd-3786-98b1-4d10cc5bd790 | -2.85432 | -49.70042 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44f634d8-cf50-3921-8ae2-fd586adc4102 | -3.08158 | -49.56904 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0637fac-8e60-3c59-8706-6e34b02d48ba | -3.25889 | -48.74979 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 82c4a2bb-0c8b-3152-9471-2b649a427f20 | -2.13932 | -50.69971 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93754c93-dc3c-32f6-ac4a-0c8a26be24b6 | -3.89409 | -50.08111 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c8a0dfe-a0b8-3582-9c5f-543b65d2aa72 | -4.19413 | -48.39756 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848b3edf-a3f5-3ac8-a63b-47fca5f19a9c | -2.15669 | -50.51215 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39635eb9-fb54-3ef2-bce2-9a29dd5ac2ec | -3.22767 | -53.24942 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56a672eb-83fe-398a-9761-7ce291783428 | -3.70007 | -54.62151 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a769f3d-fa76-3073-973c-ecab162e62a8 | -3.0338 | -50.3069 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2529510f-5e65-397b-bcd7-6283d78f7f3b | -2.21362 | -50.7271 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ce9478d-e21e-338d-b1bd-ad379c8a58f8 | -2.65511 | -49.87355 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eed6b993-8b12-3423-84fa-0346cfe33c81 | -2.87082 | -47.83968 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9926798-7065-348d-9ffd-28f19b74abfd | -3.74049 | -44.54088 | 2024-11-10 04:38:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63188698-f6fc-3f77-b7e1-0a3e022565fd | -4.69734 | -49.62589 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1661c536-5fb2-3df0-ad46-23aa1d74b65f | -4.78111 | -49.90802 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0228d4a4-4631-3761-b21a-8f4f2aae9cf4 | -2.42631 | -50.41426 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b96ce404-6721-391f-a34c-b2346e12c09b | -2.31669 | -50.66773 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41c7114a-57bc-3b61-be26-26f174c399e5 | -2.26209 | -50.67478 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c15c1106-fd8f-32b8-bc1c-b2c3664c0b66 | -4.12756 | -48.24168 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eb4dab3-3d3b-3893-85ff-15527572fe1f | -4.08787 | -48.51579 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1db4c4e-7dd2-382b-8b2b-793534a70936 | -3.242 | -50.44857 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b368775d-e6c9-3e8d-a4b3-e119f0848745 | -3.24171 | -46.44626 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d81250c-5976-30f1-8333-6e78b3d8cbec | -3.5107 | -44.03278 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 65b89114-f3c4-3347-be97-da93530d2f30 | -4.37901 | -47.2833 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e65e4a7-5aad-3bf2-a42c-6e926e8e88f7 | -4.9786 | -46.88787 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3a80b82-e19d-323a-8925-d64a1da73f3f | -2.63819 | -49.89294 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d00730f-8071-3fb5-9edb-6a6a10c5fa4b | -2.23673 | -50.51251 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbe8d464-b676-3be2-abb3-4390cb4f9e7c | -3.82231 | -48.97289 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 645ffc2b-8000-3d9b-bc63-49d4691607d1 | -3.12849 | -50.43884 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7dd43e31-191f-3573-aa80-8edeb7ea52cb | -2.9247 | -51.47519 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e825cf45-5da4-3e58-a10e-e2aff5d7532b | -5.41551 | -46.41311 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0788e56-8368-3608-899e-4e86a35e1dce | -3.0132 | -53.26294 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4519d10a-0f5d-39a4-8d0d-e5ebcacb792f | -2.31957 | -50.67209 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64754d3b-3518-37b2-aa4a-fc4cc2c5e8a5 | -3.62416 | -50.61349 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d864a209-53be-3910-ba94-6ba2ce267f37 | -6.2501 | -43.55875 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db21077b-4fe7-318f-b8a2-4e39ef788dc6 | -4.61567 | -45.987 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d1af18f-e51a-3f16-8fb5-ac19d0ed4854 | -2.59904 | -48.19141 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a98ecf20-64ee-365a-bbc9-20953a956e68 | -4.11813 | -46.87606 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e5a463e-f94f-3329-94bb-e427c4db67e7 | -2.76392 | -49.35777 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| aa057e1e-4796-313f-85c3-592f03ff872c | -3.08585 | -53.88381 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 755e5e47-d137-322b-aa8b-530c02209734 | -4.16853 | -46.59885 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1bb1f1d-2d1a-36d4-9e29-7fc4d43409c9 | -2.86474 | -51.82685 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dee32572-8c69-3151-aed8-6a07053a61ef | -3.10051 | -49.42833 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff24ef70-5cd2-3841-854b-43afa91e1c1b | -2.66795 | -48.65399 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f386a2-36e8-3a0f-9fa3-eb0443a89296 | -2.87655 | -51.3028 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3a397dc-4778-33b7-9b62-00b12bff6b45 | -2.87219 | -49.80517 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56530e9a-472d-316e-a67b-c5e1713a0a92 | -3.61479 | -55.47787 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcf6c6f3-d8a0-36ed-860c-36b4ce78c250 | -2.91138 | -49.53572 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cda16d1-81d0-36d1-8796-906cf66d2f1f | -2.98765 | -51.45878 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acabafeb-e4b0-3e46-827f-00a0fca33b2b | -4.88183 | -48.65081 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c38d95cc-130a-39b8-86e7-a5d5ae12f1ae | -2.84491 | -46.62484 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92616824-8269-3c78-9ff2-aaeec3103781 | -2.46151 | -48.59011 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21afebe2-1703-33d3-96de-1c310e96ce67 | -3.83424 | -48.87573 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0ac1082-f165-3bee-bcba-0a8b567515d6 | -3.0143 | -53.26554 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60a8b006-aaf5-359f-96ca-6c6697bdc0d7 | -4.3786 | -48.57934 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00cd24d7-be9d-3f12-9699-83a460cb0898 | -4.92607 | -45.35962 | 2024-11-10 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 773822d3-ad30-3073-b198-40a7ae6c7690 | -3.82817 | -44.84303 | 2024-11-10 04:38:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b44566-b1ec-3f0f-a5b4-bf2a6cf7c324 | -4.09552 | -49.13244 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b92f2279-0749-3da7-ad9a-b1fb8c0c265d | -2.77928 | -53.96489 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 175753d3-e157-350c-8a59-abb96c33add4 | -3.90155 | -51.92208 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 887ddd9f-cd0e-312e-9088-6b0acac3b770 | -4.40616 | -49.41227 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04e696ad-0b38-3c94-9abb-31a5bd928bcc | -2.8728 | -49.22525 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47e07205-48e8-3ad5-870a-d1704ba4edb1 | -2.56116 | -50.68148 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd08f71b-cf0a-3647-a554-d31ee78d0ca6 | -3.95847 | -46.70625 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8624da57-bac8-3022-a6e5-4a2787c60d98 | -4.05571 | -48.3087 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98a4a1f1-8217-3511-b6f0-c7c8c023590a | -5.31452 | -46.23184 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba6a819b-ef69-36f8-9dd5-4f3b24dd56c1 | -3.276 | -50.23266 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32ab919e-96fb-3a26-a0b4-a9fc88f050f8 | -3.24803 | -46.47432 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1323eb91-da33-35f8-972b-2cabc65e03ef | -4.1146 | -46.92116 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f0a2178-e474-3e5c-b24a-7f5c657c3687 | -4.78935 | -48.65767 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05249697-503f-367f-9f9c-1f20455a9b30 | -2.86617 | -49.51783 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afb7632d-111c-3dfd-afa1-a1ac59a51ae0 | -2.3098 | -50.84779 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93bb8377-7f93-3fd0-b2ae-de166a62ee22 | -2.29924 | -50.39848 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cd55e74-c034-3dfd-b1d6-d676b759af93 | -2.60847 | -49.81854 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3a161bd-0fa1-3fe7-bcba-8b582a0fa55e | -2.80292 | -49.34295 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3d6df3ad-fca9-3666-a289-9023c644e5b8 | -3.07738 | -50.49527 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README97.md)
