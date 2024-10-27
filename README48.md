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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaf0f505-fd35-3474-a422-84e9f05191ca | -2.69919 | -49.05012 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be346e6-fdb4-3c45-8bf4-24b8e8ed5bcf | -2.69895 | -49.31389 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0138346-6b22-3983-a6ac-7b7b0875dff3 | -2.69823 | -49.31841 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 886a1d07-f225-3067-a6c3-b819782da41f | -2.69751 | -49.32293 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f34db84d-9daf-38e7-982d-39dafefb5599 | -2.6955 | -49.04953 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b826a254-7307-3439-87ef-58159aaa80b1 | -2.69448 | -49.31781 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e5fa792-1988-3e7d-9853-3afe871b7759 | -2.69376 | -49.32233 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be12e6fd-b000-3efe-86f9-1bb536c7e4ff | -2.66208 | -49.28031 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7563446e-b687-35b6-86fe-725bfd7f9b70 | -2.66158 | -49.33115 | 2024-10-27 04:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c362b3e-473d-3f23-8286-60b4fe4f1e9f | -2.65834 | -49.27971 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff22a4d5-e933-3dd6-a971-67dd494bde55 | -2.65783 | -49.33052 | 2024-10-27 04:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c798871-efe7-39b2-b849-3a59bacfa80a | -2.65761 | -49.28424 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e5c4588-8540-3fcc-a030-b3b120cdce67 | -2.6546 | -49.27912 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5388c00c-37e5-35e5-9b5d-ec9535df30ae | -2.65387 | -49.28363 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c67adfe3-d534-3b88-8970-ab35c40bc8b7 | -2.65159 | -49.27402 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8a4e010-6498-3b96-a25d-68a97e215eb2 | -2.64784 | -49.27343 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9374b5f7-4b56-3840-be80-272eea692420 | -2.64173 | -49.24027 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 10cf992b-7de2-39dc-9092-c2b0d736ee58 | -2.64077 | -49.23722 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0122fe67-803c-3b6d-a84b-69a1a77535d6 | -2.64007 | -49.24171 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4dceab5a-0146-3c12-8055-b529f579c660 | -2.63873 | -49.23522 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 021b2032-69d7-3ab7-a33b-bd1ed41e309c | -2.638 | -49.23967 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b3482056-6b02-398a-8b75-a8e77c6a1b7e | -2.63727 | -49.24415 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6e9686b-01f9-35cc-a1fb-59173b5a33d7 | -2.63704 | -49.23663 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ead878b8-8c11-3b89-96b5-239568e63346 | -2.63634 | -49.2411 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3702f94-514f-3c93-ac56-300034c1853e | -2.63499 | -49.23463 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a622e3d6-8f9f-398e-9d60-b140a7fd85d4 | -2.63426 | -49.2391 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6efa5ae-3e3f-398c-89c5-d5adc1f45c7d | -2.6333 | -49.23604 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 629aa2f6-7f82-3125-8986-3a344ef98e17 | -2.58603 | -49.1964 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd2e9f3b-cef4-3703-b9b0-76c3be1bf5ef | -2.58334 | -49.23719 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8259451f-7a42-330e-b308-050b05c43971 | -2.5823 | -49.19584 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cfc7fc4-3e9c-30ff-a690-9618cb8c403f | -2.58159 | -49.20028 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e231346a-6a54-375b-964e-f4e9d523b6af | -2.57141 | -49.23988 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0812fa8-340b-320b-8d56-a03eb6ea1f0f | -2.56855 | -48.95749 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f37157e-78d9-3db2-86ab-642e638f2d79 | -2.56839 | -49.23481 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3078495-8aa8-3d94-adc8-812a4ab1cd75 | -2.5681 | -48.95488 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74a04fd1-1507-38c9-bd13-02e9f1357fba | -2.56767 | -49.23929 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a01a5a21-4a3e-38a8-b608-446055d57b81 | -2.56739 | -48.95922 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce3e14c7-a933-309f-a484-9561e8f0fa40 | -2.56487 | -48.95689 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86f5c693-7b44-36b8-a156-90ade032abb7 | -2.56466 | -49.23422 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91593268-a3e6-39c8-992c-f3ec85237e50 | -2.56092 | -49.23363 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ee64342-c5b5-334e-98d1-217b1523dfa6 | -3.47695 | -49.5898 | 2024-10-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a599b692-4476-382b-9d40-3019cff519c4 | -3.43896 | -50.09218 | 2024-10-27 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f78f8e-2dfd-3c7d-91fd-1835d04b4ff7 | -3.43818 | -50.09704 | 2024-10-27 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfccfc3c-f71c-3a49-9b3a-9668a045c556 | -3.43539 | -49.67929 | 2024-10-27 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8e3d092-5a67-3c55-ac1e-2d4cba6f0b9e | -3.43087 | -49.68331 | 2024-10-27 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dda02595-691f-3db9-953c-b1983ad30c1c | -3.33036 | -50.09228 | 2024-10-27 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d7588e77-6dab-321b-9643-4f95db342db9 | -3.25549 | -49.49719 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbe04d92-ee58-3386-97c2-c0e43d5487f9 | -3.21391 | -50.16768 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3f1f8c1-a812-394a-a454-e75e51d6dfec | -3.13555 | -49.1797 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07b46829-b909-370e-a9f7-1731f74c7350 | -3.12886 | -49.17411 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf12ba8e-dec5-329a-a85f-655582c890fe | -3.12015 | -49.29956 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39182927-be68-3ecf-be50-c749b0e140f7 | -3.11642 | -49.29897 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04f9115d-11f7-3b5b-8434-2b481933f599 | -3.49021 | -50.37233 | 2024-10-27 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4fb5cbe-033b-37ef-b299-057f677c2cbb | -3.44285 | -50.09279 | 2024-10-27 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d28dd1c-bf50-3737-9561-ebbae6ae6806 | -3.43973 | -50.08736 | 2024-10-27 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14a25154-af26-31e1-9b31-fa7f7813e418 | -3.43473 | -49.68194 | 2024-10-27 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 503fa163-6306-3aa8-bccf-721742559287 | -3.43467 | -49.68388 | 2024-10-27 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44fb2ca7-0b6c-36fd-9b17-02a8f59cfcd1 | -3.43093 | -49.68137 | 2024-10-27 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9106f07-ac75-3e71-b4a5-7d15b465c1eb | -3.25622 | -49.49268 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0d41ad3-11c4-3ac9-8440-7276e63c50af | -2.86306 | -49.45251 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f5c965f-8030-390b-ab40-8d4fe65df221 | -2.85929 | -49.45192 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d78468f2-a7b5-32a2-acbe-899fe4dd4001 | -2.51125 | -49.20107 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 481fac0d-9d93-3d4a-879b-0f218fcd4017 | -2.49346 | -49.12068 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d9d686b-bf09-39c1-85ce-3c1fbab8bd4f | -2.49116 | -49.11123 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072f8a9e-1c9a-32f1-a7a2-a76044b1cddc | -2.49045 | -49.11565 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38deb189-92d8-3884-8b8d-b9032f0d5cf4 | -2.47631 | -49.10887 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76e1a904-fd57-308f-a0c9-87cf5c5a4fbb | -2.47259 | -49.10828 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14235c7a-6fa8-31e2-8b7c-2a260d113e66 | -2.46959 | -49.10326 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 583e8286-00ee-3994-8569-d86384723724 | -2.46888 | -49.10769 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9ef7ede-f3cf-3aa2-a524-c922b307d3b8 | -2.42509 | -48.89166 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c8b1b8a-e411-346f-95c2-1dd86bf1adea | -2.42142 | -48.89106 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 551c20ca-ea47-3427-8475-d89122278479 | -2.41507 | -49.21961 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe96b0a2-6118-3c28-9604-7ac812b23171 | -2.4128 | -49.13666 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ced026c-a487-37fd-9476-d3d43e2f8bb8 | -2.4121 | -49.14111 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1a80ddce-54c3-39ac-aeb3-ef0605d57ada | -2.41203 | -49.21452 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ecdbe95-fbe9-3a91-9255-d02d43618f85 | -2.41132 | -49.21902 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fc9a625-4db4-331e-8390-135f2142107d | -2.40838 | -49.14051 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 957647b3-0cc2-3057-a056-aec43e4d851a | -2.40829 | -49.21392 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebadcb3f-e897-3321-910c-a6f5eb2e7053 | -2.40526 | -49.20884 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da7c3d53-de52-346e-b179-57c66a12556e | -2.40455 | -49.21333 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b665c9-6f35-3a06-9d79-44fcb3165536 | -2.39622 | -49.02537 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db8db3c4-fad8-3768-9e31-0ec884a6929b | -2.38565 | -49.38254 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da741b7a-b6ad-3c0d-8619-39b8143c4096 | -2.38187 | -49.38194 | 2024-10-27 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f9c744f-8980-36da-8829-b3c6e6708484 | -2.3199 | -49.16764 | 2024-10-27 04:23:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04735463-9572-38cc-b934-0e78e962a298 | -2.30497 | -48.94103 | 2024-10-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f08e0f19-1c16-3b45-9ea0-e7cbedc38a96 | -4.98853 | -49.90648 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eabba7a-8f17-318b-89ec-ca5413c1edc8 | -4.98477 | -49.90586 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec48ff38-3307-3e73-8c94-97290487ba62 | -4.62978 | -49.60322 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83525f37-bd0e-374a-865c-a422684f921d | -4.62679 | -49.59811 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 837b0a10-2ab7-3013-aac9-18ed83a11984 | -4.40111 | -49.77505 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6972613f-bdfa-30dc-a66b-1a156f24f3ec | -4.40109 | -49.77264 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b03ab7a-bcf8-3e88-aba9-d9d3200cd400 | -4.39501 | -49.76233 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5875be5-c677-35ba-89e5-7732b68b875c | -4.39359 | -49.75057 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93e6cd11-2bd4-38f9-b175-924216ce2785 | -4.39342 | -49.74814 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06ce6d64-3430-3fa6-a25e-7c524573b3ce | -4.39284 | -49.75507 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 830aaee5-b7b2-3f23-876e-874023be34d2 | -4.3927 | -49.75263 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b653532-67c7-35d0-9df4-5ee851394f9f | -4.39198 | -49.75717 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b28d853-878e-3230-b300-8a8925592e18 | -4.39125 | -49.76175 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecc3c31e-7393-3d51-96dc-6e40f210f436 | -4.38966 | -49.74752 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43542724-a04b-33cc-bf21-b3ddd0f5ab7c | -4.38895 | -49.752 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README49.md)
