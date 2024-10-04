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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61464a7a-f200-32a8-a77f-8840f79842c7 | -11.11234 | -46.49228 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 906ca699-21bd-3236-9051-f9d0261a8fbc | -11.11177 | -46.49613 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 54caad25-3b94-3319-ab1a-c4fa4cbab7d7 | -11.10885 | -46.49173 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eec56679-5cce-3772-9897-2a9d97f9c1e4 | -11.10829 | -46.49553 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b51e05ea-91ed-3667-8bf7-049e79ca3dcf | -11.10536 | -46.49116 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27e5c30d-f94a-326b-be24-bd82f5d9317d | -11.1048 | -46.49493 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0a591a80-2efa-3cb6-a399-d80948274d2e | -11.10187 | -46.49063 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0137a510-460a-3bc9-be67-77288f296b03 | -11.10131 | -46.49441 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8033fb6-d2f6-3198-b94c-45b69064400a | -11.09782 | -46.49391 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78a705a7-8605-3037-8384-9171b30474d8 | -11.09725 | -46.4977 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cac3b2e-9be2-34fa-959d-5252badad267 | -11.09432 | -46.49343 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e91373cc-5945-3237-bbcb-6042ef6d42d4 | -11.09375 | -46.49725 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a850bef-984b-367f-97a3-2d3c37e08d8e | -11.09319 | -46.50106 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4c038ac9-e48c-3870-90f2-3cbe99fec1dd | -11.09262 | -46.50491 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 03fb7fd0-a69e-3069-9906-aef7a9dd0f9e | -11.09204 | -46.50882 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4b14cb8-6e59-35ee-9c0d-0d481e96a36e | -11.09025 | -46.49683 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da86d5d-9aa6-3695-b401-abda9090a3c8 | -11.08911 | -46.50457 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 56308b07-bd33-3a10-a8c9-d3af49014007 | -11.08853 | -46.50847 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0bd4216-0544-3240-9434-17b08c1ff65f | -11.08796 | -46.51237 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ee2725d-085e-38a3-a5c2-f4975b5ea307 | -11.08781 | -46.50539 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5ef3c57-a7d4-382d-a957-6c30085b0ea7 | -11.08722 | -46.50928 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d27e6ffd-d748-372a-a436-d2c3cddf7970 | -11.08664 | -46.51315 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 039cc1ba-a99c-3050-937a-27a01e2b6022 | -11.06864 | -46.51421 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d3882d2-2477-342f-a0c0-a7a28e43b501 | -11.03492 | -46.50121 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26d99ca0-e9de-3fa7-abff-95e912e77d02 | -11.03144 | -46.50058 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfde8f98-a066-358b-8cec-5e7e0be5fb6d | -11.09382 | -46.52094 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b36d6db0-aefa-314e-9dd5-cb7a10ad99a7 | -11.09326 | -46.52474 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c431d5d3-f6e9-3631-8428-5e1785a44ea5 | -11.0927 | -46.52851 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f8f1585c-0532-3b08-bfab-cb0790d1100f | -11.09032 | -46.52053 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| caa4b9c5-1fc1-3195-8fc4-e4b00d81e28b | -11.08976 | -46.52428 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a4d45289-de73-3f69-9497-8e6065ba77d5 | -11.08921 | -46.52801 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a4d6b412-a89a-3db8-bd63-3a8c833b8756 | -11.08807 | -46.53568 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e665f6-89de-3da7-9531-1e3807487cb4 | -11.08682 | -46.52006 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d2c1c91e-c3a3-3d24-9c5f-ac6fd59e4306 | -11.08627 | -46.52378 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a2ef734-27aa-3cbd-8e80-61f317a85ae8 | -11.08549 | -46.52076 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 03949c25-ec5b-3a61-9d3f-b4151ff39b02 | -11.08516 | -46.53128 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bce80ef1-2b64-3aaa-a9db-2e9ed7f1c06f | -11.08492 | -46.52448 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3efe8fb6-54f7-3730-882f-0986042dc386 | -11.08459 | -46.53514 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 02c25dd5-618c-35ef-ba1d-2eda36e17e9e | -11.08436 | -46.5282 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a06d42c-70af-37b0-8ffb-20e0c9f2df23 | -11.08379 | -46.53202 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5eb2377c-7caa-37f2-aba3-ddc191a2ccc1 | -11.08334 | -46.51944 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1ec3bc21-952e-31a0-ba09-28b3b4927a99 | -11.0832 | -46.53588 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f68326c-9b58-314b-ae03-681bb7d7b8a7 | -11.08279 | -46.52318 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cce4d40b-55b2-3212-8a62-bd2c1cc1560c | -11.08224 | -46.52693 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c6cf641-1e70-3106-b29d-5cf0713264b5 | -11.08201 | -46.52013 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 894ed35d-8f8e-3512-851e-88bb3e7540cf | -11.08167 | -46.53073 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96a8563e-2403-33f6-9c9e-952efa76a1eb | -11.08145 | -46.52388 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df526524-16a8-320c-b30e-4f9f37083e5e | -11.08088 | -46.52765 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 641f1615-7073-3718-b920-cf9d6bf9d07f | -11.0803 | -46.53147 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 416692bd-5f99-33bc-8212-b63cb401cea1 | -11.07797 | -46.52328 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 825841cf-6720-3eae-80c4-576c128c7b27 | -11.06808 | -46.5179 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2ac7aa3-2e5a-31f5-afcf-bded89af79ca | -11.0623 | -46.53262 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfe55195-3450-3c0f-b360-dc97f98ddcd0 | -11.05591 | -46.52767 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 883fc518-5c22-3401-9049-7f7f3ca960b8 | -11.05589 | -46.55145 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e58c9126-56cf-3b34-9523-5ca7d045882e | -11.05533 | -46.53154 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d5f2f65-65cc-3e7d-ad33-afcdbe8874f7 | -11.04895 | -46.52657 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 359764e3-aced-3db7-ae8a-0374a698d71f | -10.91397 | -46.61298 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4eab674d-2fb1-3cee-a5fc-e73a7cd32a42 | -10.91051 | -46.63601 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ba37fbb-261b-371c-8f24-7e0a061e1785 | -10.91051 | -46.61243 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 494d824e-3e5b-3209-9f48-fd46fd4a5cbd | -10.89144 | -46.62126 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f428390-075a-3350-bd8b-eacfd1a8a20e | -10.88911 | -46.61308 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0cd885f-1e9a-3054-8f3b-ada0a9f92c07 | -4.94231 | -47.13813 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 560d6570-d4c6-3d8a-bc35-8f753656dbf4 | -4.8847 | -47.76377 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb4b8ad1-b5e5-3dcf-b690-89a974050f9d | -4.70914 | -47.20132 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a7f911c-8689-33b8-aed8-3e1f5fb3443c | -4.7086 | -47.20478 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c6ca54a-ba87-329e-ac7d-7bafe029167d | -4.65224 | -47.43686 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e50fbe57-c193-318d-97b1-f6c1b2f05d74 | -4.34275 | -47.2995 | 2024-10-04 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ab1ff25-d39a-3e43-a82f-ab8b1707ccd8 | -4.33943 | -47.29898 | 2024-10-04 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fa32c61-e404-3691-878d-c7a9f106a888 | -4.3372 | -47.29155 | 2024-10-04 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50b803b4-1fce-31f4-af06-6f8db1d9c92d | -5.0967 | -46.56563 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff08f095-217c-3260-bcc6-c2e0681af278 | -4.92577 | -46.7904 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36353e88-82a9-3d13-8cf8-24d9f71e99f8 | -4.69119 | -46.7542 | 2024-10-04 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd290a13-3cb9-320c-8a5c-f7177decc81d | -4.13105 | -46.7092 | 2024-10-04 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bbd2adc-661e-37d2-bb3e-be4af4bc32b5 | -4.70232 | -46.59494 | 2024-10-04 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7ba7603-2a0a-3c10-aeae-8f2716f387a7 | -4.69173 | -46.75072 | 2024-10-04 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d605f5-7c48-3bb8-85ec-fac239cb58c3 | -4.60506 | -46.63676 | 2024-10-04 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a3f1711-684a-34dd-aabf-8863f75593b8 | -4.5566 | -46.40658 | 2024-10-04 04:32:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 429c1e93-3427-3eaf-8f67-67058e815c8f | -4.36811 | -47.5867 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 117efaac-2bd6-3104-9d7b-7483228556f1 | -4.34052 | -47.29207 | 2024-10-04 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb6532cf-83bb-346d-96c6-8b1dacede5b1 | -4.33997 | -47.29552 | 2024-10-04 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 058abc23-d2c9-3c0e-9ec9-2e2541f8ff34 | -4.13438 | -46.70972 | 2024-10-04 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab29309-c122-371b-b488-f3bc2bcf0d76 | -3.92294 | -46.43825 | 2024-10-04 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 973e9fb5-9fea-3124-a610-adbb1e4a1464 | -3.92239 | -46.44175 | 2024-10-04 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c919fbc-b5f1-3d92-b3c8-b30184e9a609 | -3.76304 | -47.499 | 2024-10-04 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9102099-52de-3b66-b579-3354c80794a9 | -4.94177 | -47.14159 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f173ff7d-bd2b-3939-83e9-3497f4dc4af8 | -4.93844 | -47.14107 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0e32de1-7016-30f7-9d03-cd2544e25bc3 | -5.98836 | -47.45773 | 2024-10-04 04:32:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f1dc791-5e3d-302a-a0fd-83291739fb89 | -5.60441 | -47.96257 | 2024-10-04 04:32:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 237c71d1-f29c-3c2e-972b-c5f5ae753593 | -5.60163 | -47.95857 | 2024-10-04 04:32:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcee3a0b-bfbd-3cb7-86bb-12f57660012c | -5.46766 | -47.36926 | 2024-10-04 04:32:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a94ae8ae-52d2-3216-95ab-0281ec90f5be | -5.46712 | -47.37271 | 2024-10-04 04:32:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f68dfe-04e0-3c5c-bda2-f81414267cad | -5.46304 | -47.14499 | 2024-10-04 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 260ddabf-9de0-3d65-9368-de3888f662cc | -5.41561 | -47.57043 | 2024-10-04 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f769af7-0a62-34ed-ba34-4f5c1690c5f0 | -5.36229 | -47.80722 | 2024-10-04 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f948736-ece6-3a2e-97ed-f31817a2be67 | -5.31205 | -47.26358 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 350bcc03-dc2d-3f89-bbd2-0d23cd0c5a09 | -5.28952 | -47.32037 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e71de0b-07ee-3c6a-a735-9009d3cddf28 | -5.28898 | -47.32383 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7146934-53a1-38ad-8f87-102a8851a0c1 | -5.2862 | -47.31985 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5be07c33-3f38-37b7-9109-ef4f234b46c5 | -5.28565 | -47.32331 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d77af9c8-1c6f-370e-b0d7-2a1c7a207d13 | -5.60108 | -47.96205 | 2024-10-04 04:32:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README101.md)
