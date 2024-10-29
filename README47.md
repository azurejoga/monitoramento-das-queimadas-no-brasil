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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f30c1449-d7e0-3dbc-ad88-ab49bbf0ca3f | -2.97849 | -50.47357 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eec1c731-3186-31b9-827c-20e7711d5778 | -2.9779 | -50.47725 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1d293f9-2092-3549-914d-cfd186ccaae6 | -2.97732 | -50.48092 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0507c43a-3c9b-37b7-bb9f-70eba91d1589 | -2.97508 | -50.47301 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2ca05a9-8805-3a92-84e8-e0a88968af2b | -2.9745 | -50.4767 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b9e7e61-e9ab-3a08-aa24-28b94096851d | -2.97392 | -50.48039 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f3d5aa2-cd79-312f-abf5-67302d87366a | -2.9711 | -50.47615 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f71af08b-9e25-3e09-a8eb-0bd8cc554d6a | -2.92188 | -50.27375 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa813f85-3447-32c5-9d36-ee72afff01f7 | -2.92131 | -50.27739 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2f884fb-d334-36f7-8b17-b4029b5f949b | -2.91735 | -50.2805 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81dd8a67-35e4-37e6-bd41-3eb04cebba34 | -2.91678 | -50.28414 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327c3c9c-233b-3071-800b-d89bd52effa7 | -2.91396 | -50.27996 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5535e7d4-f6c5-399a-b41c-e472b60ed860 | -2.91339 | -50.2836 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acfa4d9-3d3d-38a0-8c73-ac56385d0e17 | -2.91282 | -50.28724 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63cc892e-4f97-30d9-b355-208f60563c79 | -2.91225 | -50.29087 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9fdac3-0df9-307e-bf60-4bda755d4b42 | -2.90944 | -50.2867 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a34f759-e6c8-3091-b0a8-2c4fbba7afa8 | -2.90526 | -50.40175 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f944d720-fe52-3943-beb7-27459827d007 | -2.90186 | -50.40122 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52cb7ab4-dec2-334e-befa-d489f883affd | -2.90113 | -49.49636 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af668bea-e175-37d5-af1b-b96800a5a2d0 | -2.89501 | -49.47043 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8bb5095-eb6d-3559-9eb6-c09cd2a6bbf2 | -2.89169 | -49.46991 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e2fadc9-2307-3dd2-a25f-c133f5ee9599 | -2.88586 | -49.76682 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c5aa78-538f-3412-a6fc-8181aea1f6ae | -2.86788 | -49.46978 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09912519-888d-3ddf-96d5-5d27152fc987 | -2.86511 | -49.46579 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a8ca2f-4751-31e3-8856-8cc7ac4feeed | -2.86456 | -49.46927 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ad972e-d524-3b10-81c9-71cb97e0a3ec | -2.86179 | -49.46527 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645e5883-8ba5-3278-a7b3-fcdf240320c8 | -2.86124 | -49.46875 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac2f3ca8-b72a-3b15-9de8-1ac49e1c9a5d | -2.86122 | -49.44736 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da25f249-f0c7-34e5-9185-e85177b7b89c | -2.86067 | -49.45083 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09ffddd3-874c-3316-bd04-314f60662958 | -2.85902 | -49.46127 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 817444df-fd11-344d-8b27-d977414ebb75 | -2.85847 | -49.46476 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aafba29-5081-3287-9ea9-e354555afd50 | -2.85791 | -49.46824 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4213e185-273d-342d-aa32-0a1e20a9eff8 | -2.8579 | -49.44684 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| def599cd-920a-3a3c-86e2-29afc41f6a7e | -2.8562 | -49.39317 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b623b35-61fe-30cf-a719-be5115244915 | -2.84881 | -49.3742 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45ce6c9f-afa1-3990-aa92-30e89994b065 | -2.82785 | -49.39941 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1c2ef2f-93db-3897-85b7-083caba3b619 | -2.81417 | -50.47033 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97a08de5-bb9e-3968-828d-f382b1f94b8a | -2.81358 | -50.47402 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da655443-24c2-33aa-8206-de3039cf5d86 | -2.81017 | -50.47349 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3e1af09-834a-342c-ad8b-746a953f78b4 | -2.80616 | -49.32137 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09a7abf2-2124-3aca-bea8-a34f96b659af | -2.79074 | -49.35451 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14e13a20-33fe-3f4f-b191-e23e36f9ae43 | -2.78742 | -49.35399 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10337e1d-8722-35d8-a33d-53e8b41b0cf0 | -2.78545 | -49.56064 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8a75ae4-7a89-3b6a-90fa-50eb689e0a27 | -2.78186 | -49.3247 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d537d931-889f-3cd9-8eb0-42c90787dfc8 | -2.78131 | -49.32817 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47adb2a-4f67-3ba0-97cd-0648fd6acf47 | -2.77527 | -49.36633 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60dc2d16-ad70-3cf4-9de1-c84f5b430b72 | -2.77455 | -49.82557 | 2024-10-29 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e461e65-928f-361e-a250-55d09571ce14 | -2.77432 | -49.52312 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 027812b0-b2e4-33b7-ad1b-57a31e41bcc7 | -2.77377 | -49.52661 | 2024-10-29 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e27839d1-d32c-365a-8449-b8e65cfa05c9 | -2.77196 | -49.36582 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66e6b3d7-6e50-3d6f-a4e2-d17561a2378e | -2.7478 | -50.44516 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d49eeebc-02a4-37b1-929e-3fb305f35b72 | -3.99072 | -49.27824 | 2024-10-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0745388b-391d-3c9c-9138-a2bced3454ea | -3.99018 | -49.28168 | 2024-10-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bae0c087-211b-36a6-b019-12fbebb671dc | -3.96225 | -49.95116 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b375e450-b305-37b2-aabb-078301b79235 | -3.94068 | -49.96163 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d130052e-b498-3aca-b586-406c5ec85d9d | -3.93679 | -49.96463 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ed7244d-4b02-3f0f-af76-afe9f0a1b3fb | -3.93623 | -49.96815 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a827d08f-6e6c-3955-bd80-61a6f5bca6d8 | -3.93454 | -49.89221 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f798d18f-1602-35e7-96d4-d5364c2f484e | -3.93399 | -49.89571 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ca0d9ab-577e-3659-884f-8ab7899ed3ed | -3.93345 | -49.9641 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 236f3757-b5c2-3b9b-aaf1-1016d5ce7040 | -3.9306 | -49.74456 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2abcc4f4-f061-3d11-ac82-9ed63b978f47 | -3.89219 | -50.05174 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 75b33170-e6da-38c8-bc2a-a14d6c7b08ff | -3.89163 | -50.05527 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6660edc2-a8aa-37b4-9828-caa0967a0d82 | -3.88003 | -49.95576 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7877d774-7e54-3e40-a880-343e824b72c1 | -3.87669 | -49.95524 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b190390-9f82-33bc-b940-1747af06eff2 | -3.87613 | -49.95877 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9db715ed-5c82-347d-b32b-02da5975ac5d | -3.87052 | -49.99403 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 422a7732-1c56-3a9a-bc17-567a2160764d | -3.86774 | -49.98997 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9e7ea90-9f5f-3b11-8f4c-3d44746dab2d | -3.86718 | -49.9935 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 023dcc37-c6aa-37e3-8b32-79ea0d88427b | -3.77812 | -49.95431 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2833bbc3-b39a-3ef4-9587-7f4881ce2373 | -3.73669 | -50.06382 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2b513b7-ae35-3d7a-8029-f853dd4ac0f2 | -3.72833 | -49.43159 | 2024-10-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c1ec5ae-2b98-314a-b17a-728590bfab5f | -3.69087 | -49.64636 | 2024-10-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247b5464-feb5-3df6-8095-705a2d14fb34 | -3.6678 | -50.11492 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2d005d7-e116-3f64-96e9-d50ec7fb11b4 | -3.66724 | -50.11846 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3f7afc8-a8e2-3729-84ce-576a82886d76 | -3.65768 | -50.1571 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb027d4a-3439-334f-97b4-f33bf6a37147 | -3.65432 | -50.15657 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c68e3f51-bc8c-3d6c-a8bd-bb3c74ae1fe7 | -3.65096 | -50.15606 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d29d874-a186-3b97-a03a-9662b136c772 | -3.64792 | -49.83246 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8591b2f0-d503-3578-960f-b0b04711141a | -3.62346 | -50.17739 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2da6b7e3-3ec3-3712-b0c9-f29ba6fbd9e5 | -3.6201 | -50.17688 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c304d28e-11c2-3a8c-aab7-1c4012b8bafc | -3.93393 | -49.74506 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79ced00a-50de-3df9-834d-fa55a8fbbd20 | -3.90179 | -49.75436 | 2024-10-29 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49f6cf35-9bed-3fdd-a333-e5ebe1c4d331 | 2.35994 | -50.77199 | 2024-10-29 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 206fe7a0-01d9-37ef-ad11-c420d5bf2d49 | 2.35729 | -50.75508 | 2024-10-29 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc5df88a-1975-35a6-abc4-f3b3c02159af | 2.35365 | -50.75564 | 2024-10-29 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d2499a-8a81-37a4-aa98-8ae46e853f3e | 1.3804 | -50.88504 | 2024-10-29 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f26216a0-9ab6-3d2a-adfe-1d200286199b | 1.37678 | -50.88559 | 2024-10-29 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf84a457-1a7b-3cf4-b9a6-ea664028ebf8 | 1.03333 | -49.97105 | 2024-10-29 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe1946ae-2655-39ef-9b12-ece4bc8bea16 | 1.03273 | -49.96727 | 2024-10-29 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4e06887-dd62-3f5a-9369-308b9347826e | 0.85217 | -50.73416 | 2024-10-29 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e46cef2-b083-3d30-89a9-59df815e29b2 | 0.79994 | -51.10157 | 2024-10-29 04:38:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ee1c6a-8421-39ea-8d13-ee24c8185a7a | 0.35255 | -50.39394 | 2024-10-29 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85183217-fcf4-30e3-a779-91ce5861339d | 0.17159 | -51.01696 | 2024-10-29 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1960406-e729-36f2-8ec5-b5d2c1dff2a4 | 0.17095 | -51.01284 | 2024-10-29 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4718d58-6b9a-3d76-8419-5ec7683145e2 | 0.16864 | -51.02163 | 2024-10-29 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166bea66-7335-3219-845b-e822d22c8827 | -2.24705 | -50.45871 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6ded9f-55ce-3e82-894e-77f2dc8b064d | -2.24689 | -50.45858 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ce5705-03a6-3f91-9aa6-6aea75facb9a | -2.22867 | -50.70542 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d490b76c-72cf-37fd-8718-06d9d9d1e097 | -2.22503 | -50.72816 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README48.md)
