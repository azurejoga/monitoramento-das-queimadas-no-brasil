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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddcd2891-c116-3cfd-a4d0-80694192dbee | -7.6749 | -44.5799 | 2025-07-07 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 3a878308-d4fa-3d62-8015-afb6f1bd8ecf | -6.1792 | -48.0494 | 2025-07-07 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| a9fde174-c0d2-3827-9091-94919107971c | -6.1604 | -48.0724 | 2025-07-07 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 01d04c73-18b8-3d62-9b2b-75595547a496 | -6.69224 | -43.15051 | 2025-07-07 03:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af4df98b-5605-387a-a829-b7785b3539c0 | -6.69944 | -43.15222 | 2025-07-07 03:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb8044d5-1530-3aaf-97de-c1ee2f99c920 | -8.06224 | -43.11917 | 2025-07-07 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| d3fece8e-c585-3296-bec0-ff24fa1341e5 | -7.6938 | -44.578 | 2025-07-07 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.4 |
| c71177b3-7dd9-381c-8083-9661d4b5ac09 | -6.1792 | -48.0494 | 2025-07-07 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| db1f9427-2dd7-395c-8457-fd01d681060e | -6.1606 | -48.0507 | 2025-07-07 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| d66632aa-7de1-3d16-aedb-eafb3730469b | -14.1324 | -51.3017 | 2025-07-07 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| fdbbe985-d25b-3e34-873b-ea7a595dd6f2 | -7.6935 | -44.601 | 2025-07-07 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 68fac7eb-bbf5-3b19-97e3-de1f16d828a5 | -7.6747 | -44.6028 | 2025-07-07 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 1c5b29e2-b575-3f39-a569-641f3d62aa71 | -6.1604 | -48.0724 | 2025-07-07 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 11527674-e59c-3da5-9c28-b281eeb3a8b2 | -7.6749 | -44.5799 | 2025-07-07 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4e577247-7905-3f62-8c2c-22b3f2c8384a | -6.1791 | -48.0712 | 2025-07-07 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 952ff7fa-8484-36d0-8f6e-0fa7efd822e5 | -16.32699 | -43.62049 | 2025-07-07 03:21:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fedfe914-fc33-3818-a218-7843d4725188 | -7.6935 | -44.601 | 2025-07-07 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| a51c478d-b8f3-37a3-8730-9225972e0c52 | -7.6749 | -44.5799 | 2025-07-07 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 0b2a8a26-56bd-3baa-a2ae-33ca399ee0a4 | -7.7126 | -44.5762 | 2025-07-07 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 6abc2bbf-ee5e-365b-883a-8ed20cdf497e | -7.694 | -44.555 | 2025-07-07 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 151e3505-2016-3d13-8bc8-7eb1d70aa541 | -6.1791 | -48.0712 | 2025-07-07 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 58b82fc8-52a9-39a2-820d-7fc524084c9d | -7.6747 | -44.6028 | 2025-07-07 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 3d010055-ecf0-3af8-8079-e87b21642aa1 | -6.1606 | -48.0507 | 2025-07-07 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| c1bd4f52-8102-38f4-95e9-28d37c34c36d | -6.1604 | -48.0724 | 2025-07-07 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3ca9f997-a4fe-3cda-a928-c10b240b3a0c | -6.1792 | -48.0494 | 2025-07-07 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| fe6aee41-88e0-3cdd-9d9a-a61b8259c35b | -7.6938 | -44.578 | 2025-07-07 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 254.2 |
| eeb0bdc3-f3ad-32d8-9877-7ecc8d26ac98 | -7.6747 | -44.6028 | 2025-07-07 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 404f6d9b-6ca7-3d5f-9c2d-99e55b904fe8 | -7.6749 | -44.5799 | 2025-07-07 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6d71bff5-f041-311c-8c57-3810dd3d1a61 | -7.6935 | -44.601 | 2025-07-07 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 843425c9-1a5c-36ac-93ee-dfd77eca5c0c | -6.1791 | -48.0712 | 2025-07-07 03:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 09a4adfe-4d5f-3e59-8740-572e4ee8c881 | -7.6938 | -44.578 | 2025-07-07 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 253.0 |
| 40cb688e-6842-308f-a97a-7aa38c4173a6 | -7.7126 | -44.5762 | 2025-07-07 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 12c04136-aead-37c0-bb5a-f2597e2b57e5 | -7.694 | -44.555 | 2025-07-07 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 1b608b72-91f3-3e56-a322-d71c6d65afe4 | -6.1792 | -48.0494 | 2025-07-07 03:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| f3be60d4-c722-3e2d-9def-b1bd4108c914 | -4.81702 | -44.35476 | 2025-07-07 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71c608f5-92d6-3fcb-8037-7b763975ca9d | -5.13414 | -37.36184 | 2025-07-07 03:40:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9bf9a286-b891-36fd-8bb0-ae30d0090112 | -3.92774 | -43.16555 | 2025-07-07 03:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9351feb1-eab6-3f28-988b-c62ef00f3749 | -4.82971 | -45.20085 | 2025-07-07 03:40:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba54bc01-dd50-311f-aa5c-1c3f59dfcc6f | -3.92217 | -43.16768 | 2025-07-07 03:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a09701f8-0354-3400-be11-2cf31ba682e4 | -4.81861 | -44.35478 | 2025-07-07 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7847c3ca-95cf-3c9a-9628-ad8287c0de30 | -5.1663 | -37.7426 | 2025-07-07 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 12810cde-c0e7-37ac-9d75-8df932f15b9f | -3.92725 | -43.16856 | 2025-07-07 03:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9de2442f-005a-3b1b-a610-8789c7860f8c | -3.92267 | -43.16468 | 2025-07-07 03:40:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f40bb352-0fef-37c1-83ab-3760168b76c6 | -5.16606 | -37.74323 | 2025-07-07 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 49b6d456-46a2-31e9-8777-c834f059bd90 | -4.82398 | -45.19988 | 2025-07-07 03:40:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1794f68-7f9b-31b3-a0ef-5b03b4b43a2d | -5.6028 | -37.46189 | 2025-07-07 03:40:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fe981408-4cbf-3ec8-be6a-5537eddd1dae | -7.69302 | -44.61176 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b1e0833-0052-308d-8ca1-6157fc9531f3 | -9.20152 | -45.33921 | 2025-07-07 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 613ae937-4178-3ef1-87c2-85e684479088 | -9.79602 | -47.74113 | 2025-07-07 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 431eda59-ac87-342d-9de0-85275e51f14c | -6.95007 | -42.7078 | 2025-07-07 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7cd72739-6eab-3806-adbd-508ff1c7b2f9 | -10.65062 | -44.48167 | 2025-07-07 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8783f1fb-cc69-36fa-b022-92eb5940dba1 | -6.9528 | -42.70582 | 2025-07-07 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b881cc8-7fd6-3740-a4f3-e800412751f3 | -10.57199 | -49.13052 | 2025-07-07 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5dccceb-3dee-3bdd-9e42-adcbd8462fd3 | -7.69105 | -44.59116 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e507fc35-217c-38fe-91b8-5ffa323ba9b9 | -6.70722 | -47.80738 | 2025-07-07 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 62023d94-5369-3abd-b470-6cf88bc0cf30 | -7.68387 | -44.57139 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a41d90ed-9cb6-3218-a950-fc6c62900657 | -7.70074 | -44.59737 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87427ac1-ff36-3449-9d9e-001bda10ccfd | -6.87671 | -42.79766 | 2025-07-07 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fde59d3d-b39f-3c8f-a46e-c22d705b7435 | -7.6935 | -44.5778 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f152a17f-06b5-3511-ab50-8508293b4447 | -7.68853 | -44.57563 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 910222db-d2c9-361b-9391-f8bde59861aa | -10.5708 | -49.13647 | 2025-07-07 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61ce3594-5618-337c-b1a0-6d6407b2d481 | -7.6925 | -44.61283 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc2f84fe-982c-362c-a2e6-413617478060 | -10.64225 | -46.3816 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83fb4ebe-380e-3ffa-81c3-57dfa0a62d55 | -7.68738 | -44.58218 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 0aa6fe21-78dd-34f5-8bca-8806f77a2e77 | -7.69358 | -44.60858 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0372b29b-6703-38ce-9c29-de60103d1819 | -7.69229 | -44.58435 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| dd19ea1a-aab1-3acd-8d11-8c563b716e97 | -7.68841 | -44.60551 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f17bdf8-32d7-3c39-a53a-7c61c58592b8 | -7.69414 | -44.60538 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909e407b-d51d-3063-9b1e-1e54fb81bd15 | -7.68646 | -44.58665 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 31db3ed8-d7cf-37a4-8bc5-0b4f4c28a11c | -10.64893 | -44.4863 | 2025-07-07 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d9789858-9446-3af0-98ea-7857a6f4a096 | -7.68664 | -44.61517 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a416db1-5e69-32b7-a7da-3cd38e0d4831 | -7.699 | -44.57758 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60758e8e-fea8-39a5-a96b-03078ce44151 | -7.68251 | -44.60988 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62a079c4-daa7-3c0d-9a20-21bc5e363132 | -7.69376 | -44.5766 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d9c6c041-e3b7-340d-899f-c615a9f2cdbb | -7.69841 | -44.58092 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e42dd119-b9bf-3398-8807-c741a3e86189 | -6.57037 | -43.0366 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c400cde-d62a-3c98-b212-aa75191ceefa | -7.68621 | -44.58883 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8106e468-8f2e-3367-b24f-adbe8c74deeb | -6.64049 | -43.17194 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca911fb7-d930-3279-a5e6-3a52d9e9131e | -7.69539 | -44.59822 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95f915aa-02db-34df-b4f9-15a84b4d1b4d | -7.71098 | -44.5709 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eff45e2d-9d08-3013-8279-b16940cfd7d8 | -7.69663 | -44.59109 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f094436-fa23-3f37-8aaf-84ad15d06d23 | -7.68826 | -44.57684 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 57dc250f-6415-3786-b47a-1ffe24ca3727 | -7.68214 | -44.58121 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c45068e5-f4ef-3c56-9907-5a5c93a4c641 | -7.69602 | -44.5946 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cda1b965-0791-3e35-a5a8-e7bf46bd8c88 | -10.64956 | -44.4873 | 2025-07-07 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 289d7db6-2e04-316f-bb6e-b5ec9f785f19 | -7.6769 | -44.58023 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dee7e25a-29e5-3438-a581-29a420dd82fc | -7.67612 | -44.61537 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6df55c23-5e5f-3224-b036-0283d6b1a9bd | -7.69751 | -44.58545 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb9217d-e09a-32a2-9f26-1daf2bf9c251 | -7.68795 | -44.57891 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a654e760-5451-36f3-adf6-1e55a8112c83 | -7.6703 | -44.61765 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f2f6cfcc-6984-3532-8849-8763f0a759d5 | -7.69689 | -44.58883 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb35c6b-3172-3616-b5d4-8f921a4797a7 | -6.95557 | -42.70377 | 2025-07-07 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c1b3367-8371-3526-8b1c-b400be926120 | -7.68199 | -44.61098 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4671c205-ced3-3a4b-b53b-fdd7c7dc43f2 | -7.68886 | -44.57358 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a281d202-10b2-3e00-a67f-e0b0b4864db3 | -7.69625 | -44.59232 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6219f8f-4a77-3ea5-b52f-aefd3310e979 | -7.69427 | -44.60314 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0bcf9c6-a419-3210-98f4-4f955efcb5a9 | -7.67086 | -44.61446 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90e8a887-5fb4-3547-8566-955d6c33a02a | -7.69409 | -44.57454 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66112903-8fa7-333c-b635-65bfd469aa30 | -6.87199 | -42.79693 | 2025-07-07 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0579b4f5-e234-336b-ab4f-35ada8866aca | -7.67726 | -44.60891 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
