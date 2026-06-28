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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df33b0dc-a8b2-32e3-89c5-9fd597b4eb78 | -10.06027 | -59.10781 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9deb40f-c543-348c-81c9-fdb98ef6bfde | -9.16399 | -58.06875 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d92d4d61-adcf-39b5-8bf8-807674557eae | -11.20873 | -54.30709 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a096d401-9c66-3c43-aa47-a68c8d235dc1 | -12.16875 | -57.12917 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5644a8d-893b-3dd6-8790-9c8fd886e89d | -12.20454 | -52.87934 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e41bf42e-e2c5-31d0-9113-ed5f40cea144 | -10.30677 | -57.13686 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6c0b77a-bc51-3439-aede-b6c007f01122 | -11.8786 | -57.81754 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c1b9cc2-a911-3cb4-b3f9-7b77ea681243 | -9.12544 | -58.2503 | 2026-06-28 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d0fe102-4beb-317e-910d-13edc3d2daf4 | -11.71824 | -59.35412 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aaffb55-fd75-35e7-9e5e-dd57ba0c66f7 | -11.93254 | -58.6349 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eae69f4-ae5a-3323-8eca-c64d5f043ac6 | -11.849 | -56.84384 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a712c8-21d6-3ccf-958a-96193f027b9e | -11.88244 | -57.81808 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50404bc7-5e41-3ab2-9f91-a9662fdb5343 | -9.09092 | -59.4019 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aecf26f8-abfa-3b73-8870-663588a156d0 | -11.2199 | -53.82222 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| df9a1647-96ef-3d46-8c99-67a690e74c95 | -11.65922 | -57.26152 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddb8ff98-c12f-3937-8ed0-feb1c4b71f0b | -11.88667 | -57.11199 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29bde68a-5c8d-31d3-a6c9-5ed7ac06079b | -12.18849 | -52.87709 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80be171c-d9dd-3825-8dc1-39da2ffe84cb | -11.21489 | -54.29727 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77c67107-802f-32b6-9826-bd4fb9bb3195 | -12.1979 | -52.8888 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2fb4899-ea30-38cc-b19b-4a9ab4d81444 | -11.91835 | -58.65515 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b325049-cc83-3266-8109-d1c66ff3d2c1 | -12.18892 | -52.87368 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f0d0986-1dbe-3673-aade-72f996a4c902 | -12.20411 | -52.88275 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f04af17-458d-304f-92d1-51a7f9831142 | -11.2094 | -54.30187 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 421e4d25-74a0-3d29-a207-6e12209a8801 | -12.18907 | -57.15913 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f29b708b-1349-36ad-a43d-9ef742320361 | -11.20926 | -53.82645 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59618f75-b382-3c66-a531-dc42e54072b4 | -9.02997 | -61.34155 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 858ecc5d-4ee9-3f6d-8db7-5fe53bc166fc | -10.90125 | -56.85619 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f316a3b-6e5e-36ba-9db4-8ec34fadba23 | -10.3629 | -50.18669 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4df94f94-d7c8-3193-944d-446872cd797b | -12.16474 | -57.12855 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a386e11-83c0-31b3-8f9e-429e5003589a | -12.19514 | -52.8676 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec25796a-5eaf-3467-811f-da7bd7af31bf | -12.18999 | -52.90829 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24c8a8e1-e90f-3644-af0e-997cdf570197 | -12.23207 | -56.55748 | 2026-06-28 05:33:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1199361f-0d34-350a-b3fe-eb4ddd36069a | -11.32335 | -54.46669 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c3336eb-8b41-3d1e-afca-2e1730466ff1 | -12.18957 | -52.91166 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc63eb83-7288-3dc2-8a83-34adcc50fb3d | -10.78481 | -54.10262 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41cf8eb3-1b7f-35e2-9992-41628b8b4355 | -12.17854 | -57.14684 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02625ee5-72b4-3781-ac48-56e0f9c3159a | -11.88052 | -57.81491 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44abd17b-11c4-3b09-b8f5-b5b89705f586 | -12.18806 | -52.88051 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7c5420c-8ae5-3914-80a4-bd6cc9a24e22 | -12.23314 | -56.54972 | 2026-06-28 05:33:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea0c1e74-96c1-373f-b52a-51ba88778dcd | -10.81147 | -56.61235 | 2026-06-28 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 540991a8-989d-3c0d-acc5-4ce6ed45a028 | -9.02479 | -59.54214 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31c42e8e-8447-38a4-aec3-3268a4358598 | -10.30285 | -57.1363 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45ebbb72-0316-3a0c-bc48-f4e3f8a3caaf | -11.90596 | -57.1203 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e524c0ee-87da-3e91-935d-96750162682f | -12.46122 | -58.49334 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f9fffb11-34fc-3a65-929f-e482afea34ea | -18.47608 | -54.09791 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b304b0c-53d6-3094-8b40-6c1a6c52762d | -12.59464 | -57.88471 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 82bd0a50-1904-3bf3-9003-180c9fbcf75e | -12.62274 | -57.89087 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45486a04-e495-3bde-ad1a-93edac56c930 | -12.62162 | -57.88882 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 930fa988-45b2-395f-b8de-e1a258691b5f | -12.60305 | -57.88105 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b50876b-831e-3fc9-a7e0-a27c2e349efc | -12.4575 | -58.49278 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4635cee7-a33f-31e2-bfbf-4f2a4a367df7 | -16.19125 | -59.3301 | 2026-06-28 05:36:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09d31780-a562-3532-9eb8-244c2a2d59bc | -12.54922 | -57.18845 | 2026-06-28 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de952ace-2c01-35a8-86b9-dc8943bfbe0b | -12.58573 | -57.8087 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 534f2246-e70b-390c-965f-1beaaed988d4 | -12.60235 | -57.88587 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0c4a708a-3800-31ce-b78f-1a8064fb0139 | -12.46186 | -58.4889 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14cafc71-ceed-3885-b191-2fba4fd5f365 | -12.60621 | -57.88646 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 48aa2aa2-419f-3a6c-adc0-4a7716bb5b54 | -18.47532 | -54.10507 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6b10a30-1ace-3e39-859a-d6a29aaa1ffe | -15.37496 | -60.1618 | 2026-06-28 05:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18c72d03-d334-316a-acce-571c67152bac | -12.6266 | -57.89141 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9bd33c29-aa80-3f2a-b9fa-7baa80e67577 | -12.98808 | -57.77934 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad50bd3a-56cd-37ad-8dbd-55b27e01e832 | -12.77046 | -59.0038 | 2026-06-28 05:36:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c613849a-e46d-3c91-95e9-58b3d2af1bc7 | -12.98419 | -57.77872 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d24c674-9b20-3bcf-8a2b-5aae551486a6 | -15.43841 | -59.23443 | 2026-06-28 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d22e6ca5-bed8-3e14-b1f4-ec362df1546e | -12.79264 | -54.8839 | 2026-06-28 05:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9bd95eac-b0a7-31cc-b7b7-98fe0804bc79 | -15.44276 | -59.23051 | 2026-06-28 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24205f8d-b128-3741-af97-b8d474938da8 | -18.4757 | -54.10152 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1435fb5-a199-3cde-8037-80c5bb409f4f | -12.45134 | -58.48272 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cf27f6aa-8552-374f-881b-d8c406ab8b50 | -12.46058 | -58.49778 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fd0607ce-9a7a-34e1-a56c-29701fc1dd82 | -12.62548 | -57.88937 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb3fea81-e703-339a-b328-40803adc605e | -11.73144 | -62.62737 | 2026-06-28 05:36:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5a8bfbe-20ec-3438-9900-86e880de143f | -12.59533 | -57.87988 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 83b022ad-cbdb-34f2-ae9b-76cce9faf28f | -12.45623 | -58.50165 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3616fe8e-d3cb-3232-bdae-0773a4cd9235 | -16.23228 | -59.3082 | 2026-06-28 05:36:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28015b7e-10cf-3c1c-b626-4930d5e303f7 | -18.48567 | -54.10984 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf019658-4dec-3913-92b9-aa30be3b98df | -12.45814 | -58.48834 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e97bd519-3623-3224-b380-468cc6266cea | -15.92886 | -52.28577 | 2026-06-28 05:36:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d60fb53-081a-3cf7-af87-dd402fee3a2b | -12.62478 | -57.89419 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 264460ad-a52f-323b-a233-ca94013d5905 | -18.48031 | -54.1092 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11d21da5-3914-37de-ac0e-85db3d312550 | -12.45995 | -58.50222 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fb13fb0-5387-37aa-94b0-3b49788a1c14 | -12.59849 | -57.8853 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fcf3de68-c2f7-3f8b-b460-e1caed4d4042 | -12.61006 | -57.88705 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbd49647-f8a7-3cec-8001-d4f52cfb80b1 | -12.44698 | -58.48665 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0fec709-875b-320e-9e34-e207499e95b0 | -12.78794 | -54.88319 | 2026-06-28 05:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c20249a-801c-3aae-979b-698f00ed31b9 | -12.58434 | -57.81845 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b425969a-ef25-34c1-a63e-b08cb7bb6631 | -12.4643 | -58.49836 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a4e06391-c122-3900-ab4e-45e2326318e9 | -12.45687 | -58.49722 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bc5358e-959c-39cf-981f-2f09a0fa2018 | -12.45315 | -58.49665 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1526c9b6-95b4-380b-9de4-5baaeffcec11 | -18.48603 | -54.10648 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 031925a3-a2b0-38b5-9f96-fbd09a168d67 | -12.61076 | -57.88222 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfaaa69a-4a0d-3beb-a26a-f3d125b8fd75 | -16.19059 | -59.32776 | 2026-06-28 05:36:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdf5e819-95a5-3372-af9b-de4901d377e2 | -12.58116 | -57.81306 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 442ba1b5-2087-36ae-80d1-6f4ee45eff91 | -18.48105 | -54.10233 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f23ce05-03b3-3f64-8e8c-e9100a77e200 | -12.5978 | -57.89014 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff834fa6-39f4-337d-877c-9f86cd1d8454 | -12.59919 | -57.88046 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b8ab831-6013-3f0c-a4bc-a181974aa062 | -12.46367 | -58.5028 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c72090a0-6cf5-3d88-9188-e20a85710cee | -12.45442 | -58.48779 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33339146-b7cf-3d86-8d57-e0a3c41eab58 | -12.46494 | -58.49391 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 42f6c158-8fee-325e-bf3f-015961fd3733 | -18.48067 | -54.10582 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7a23e83-54c8-37b7-8796-7eb0f33da533 | -12.45252 | -58.50108 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16181e6a-0507-3928-9fc5-9bfbbab9a1ac | -12.60936 | -57.89188 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README23.md)
