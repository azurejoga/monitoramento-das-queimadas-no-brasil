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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe4bf2f9-d32f-3a59-80d8-016c352dab4f | -12.1115 | -50.7001 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0aa8d2d7-38ac-332d-925d-8b54402cae6c | -11.7903 | -50.545 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a90165c1-414a-3859-b2ad-813b0612670e | -15.4194 | -47.9227 | 2026-09-28 15:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9179d1fc-7de5-33d7-a0ab-7adf562dcd3a | -11.9402 | -50.6987 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d940395f-80b5-36e3-b3fc-492ba1320a32 | -8.2807 | -54.7158 | 2026-09-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 960cc3c6-445e-3980-ba6d-ec882d7181fe | -11.9399 | -50.7201 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| a2dc2662-b6f2-3990-b8ea-f611468cbe83 | -10.6094 | -53.9902 | 2026-09-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 041eb2a5-5fcd-3180-98be-debd5e6fe485 | -11.1181 | -51.1091 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 6b565e80-0bc5-3c3e-9f17-d3347d6827a8 | -12.1557 | -50.3089 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 3a0b6ff7-4da7-306c-aa96-811ad9792354 | -10.9156 | -50.6845 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| db2aa59d-94c6-3af4-bef5-763884281938 | -11.7325 | -50.5944 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1b35785b-16b5-36f7-88d2-0f8f0218613b | -12.0921 | -50.7237 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c694d1b9-128b-39f8-9c9b-2db0d2ce8c13 | -15.112 | -53.8838 | 2026-09-28 15:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 77c32326-73d2-3c89-a29a-be205312085f | -15.4003 | -47.9035 | 2026-09-28 15:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a7083630-8ebf-3dab-99c8-bf9b525a0fe0 | -10.11 | -50.1708 | 2026-09-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 72e5680b-3175-3a1e-8e35-f12610c95289 | -10.8187 | -57.2192 | 2026-09-28 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| a342220f-e1e5-33d8-9840-c7508d52c594 | -12.1178 | -50.292 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 284de8af-1c89-33f4-953c-aad4b08c500d | -1.2818 | -49.3803 | 2026-09-28 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ff25cd90-88cf-33a2-9159-5ff99902c6d9 | -10.7114 | -60.7505 | 2026-09-28 15:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5483ddac-9121-3c0c-a3cb-2d8aa89dc18f | -10.1095 | -50.2135 | 2026-09-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6f8a372f-1ccc-30c2-9fad-8fe970b46032 | -9.9784 | -50.1412 | 2026-09-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| f7dee0a2-18b1-337c-9c2e-aaec8aa1cff6 | -10.9536 | -50.6805 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| f4a80654-e849-3e40-bd5d-9804f7ce1611 | -10.9861 | -49.7131 | 2026-09-28 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 659f7e5f-ad6a-37e8-aa01-aed0dfd3d5ca | -12.2827 | -50.7226 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a8c108e6-35e4-3272-80fe-c77d2d4d9cf6 | -11.7126 | -50.6608 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| dae426d0-efce-3ca7-81f9-5cc46a9a5e22 | -10.8967 | -50.6866 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 50ea4014-c22e-35e2-aac7-9bdcc4adfd70 | -9.9393 | -50.2518 | 2026-09-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 79578532-073c-3a4c-92a3-5a6ee547246b | -10.8191 | -57.1795 | 2026-09-28 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 22366483-72f3-3bf0-8bec-6d7865a16cae | -12.2442 | -50.7485 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1a481e0a-fc4a-38d0-b16c-cefcef616771 | -10.6928 | -60.7322 | 2026-09-28 15:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d6f30597-cb4d-332d-aa69-daf9034868c5 | -11.8094 | -50.5428 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ad4291c2-6cd5-3ab5-ac37-cacc03bc354b | -12.2311 | -50.3643 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| d445fb29-c72c-3e55-8fc3-53da565a4f41 | -11.1364 | -51.1496 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9aaacf41-8b89-3ab5-8e22-74a9a50189b2 | 3.7504 | -60.2782 | 2026-09-28 15:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 65b04eeb-591e-3c27-88c4-a59981330c95 | -12.3088 | -50.2688 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ed2d17fa-311a-38ec-94a9-ac85ac9959cd | -12.0615 | -50.2343 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 9a23ba70-611a-3e47-8456-b33bc57da5ca | -10.1713 | -63.0571 | 2026-09-28 15:40:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f2ef7cf1-2787-30d8-bd0e-2a1f7664a753 | -13.6866 | -56.6131 | 2026-09-28 15:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2b5775bb-f66c-3e00-a5b0-61f3a8400b5b | -14.3693 | -52.1026 | 2026-09-28 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4044ed56-660b-3c42-adbe-cc715c16ebee | -11.7138 | -50.5752 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 7a33e6cc-54f6-3d02-ba7c-37bcef7cd481 | -11.9971 | -50.7135 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 8848b835-2d28-3ecb-bd3e-c5b5b68001f9 | -10.9538 | -50.6592 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f93e7047-d832-37dc-84d2-42144ac4ddde | -13.4325 | -57.061 | 2026-09-28 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1947f880-1ac9-343f-8b97-2c4505ceedca | -7.7086 | -44.92 | 2026-09-28 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| fa4b4c29-79c8-3c4e-b963-aebc9d626eb2 | -11.7332 | -50.5516 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 91ca783c-dc36-3556-8e17-437af3a634d5 | -12.1678 | -50.7576 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 929bd86f-dbe2-3cb5-9ecb-1a936a824147 | -11.0424 | -54.0336 | 2026-09-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f8b2cf18-5a3b-3c66-b0aa-060fc1b27310 | -12.1863 | -50.7981 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0b17a7b7-2fa3-3125-848f-b2d0cb7aabfd | -10.2067 | -49.9898 | 2026-09-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 5f71b020-7687-3544-a387-be4be49bdb16 | -10.8944 | -50.8569 | 2026-09-28 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 26f8c1ae-96b5-34f6-9ac0-ad36e1cb8cbf | -10.8184 | -61.4191 | 2026-09-28 15:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ff31851e-59d3-3af6-9581-44ff77e5e8a6 | -9.9396 | -50.2304 | 2026-09-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 439d47db-27e4-3832-8414-9a1475ee65a6 | -12.2897 | -50.2712 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e9c13cc3-ef7f-30e2-9a42-4cb2bf998856 | -13.2186 | -54.5182 | 2026-09-28 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7bd0f597-c65e-3656-8135-f5aad3aed3fe | -7.6852 | -54.7532 | 2026-09-28 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| e63572a7-ad73-3c65-bc84-b28e43282ab4 | -11.9586 | -50.7393 | 2026-09-28 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 688c2ce6-7469-3411-8ad7-c3f2d25acd64 | -11.7357 | -54.5227 | 2026-09-28 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a074e5a7-4684-33d2-a7fe-2d77696f6b69 | -11.7322 | -50.6158 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c29a3d71-1d9d-389c-8472-d0f26e4f83f5 | -11.0962 | -51.3231 | 2026-09-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 46e93285-3072-383d-84d0-69039229e6c3 | -11.0772 | -51.3251 | 2026-09-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d3ee313e-91ca-3e2a-9937-9345059b282a | -10.9864 | -49.6915 | 2026-09-28 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ff373ff0-6cb9-39a2-9a1e-237c24735586 | -9.9582 | -50.2499 | 2026-09-28 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 55a8aa18-2f4f-318b-8fcc-dccf087fbe47 | -13.6866 | -56.6131 | 2026-09-28 15:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 50776214-ef10-3b37-a3cb-83169e0a63ad | -11.0583 | -51.327 | 2026-09-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c77f3c00-fba0-3073-9783-00a429d148be | -12.6459 | -47.2823 | 2026-09-28 15:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 3df1298c-57d6-335d-8f75-cb2dea6cf32d | -10.9861 | -49.7131 | 2026-09-28 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 09081317-a3c6-3ed4-a1a1-0d59902ad657 | -12.9457 | -51.0695 | 2026-09-28 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 514e3208-875e-3358-b1b4-00721b144b5a | -12.2123 | -50.3451 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b59a53af-1dee-3268-bf88-20a81be1c234 | 1.9241 | -50.8202 | 2026-09-28 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 29f6f4eb-0a6d-3108-a6f7-e86ab164fcb2 | -13.3439 | -51.3187 | 2026-09-28 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 01e3b19f-e6ff-3d11-9094-86f17a1f5330 | -10.6928 | -60.7322 | 2026-09-28 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e702de57-46f1-302e-9dc6-2e35906e1a2f | 0.3219 | -51.4389 | 2026-09-28 15:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a302359e-fc07-3170-9f40-e4bcc287adde | -11.7138 | -50.5752 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6d34bed2-29bb-38c4-a4a9-bd4af9e16076 | -13.4325 | -57.061 | 2026-09-28 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 28be703a-1797-3fc0-8746-1278b0a958e6 | -11.9968 | -50.7349 | 2026-09-28 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c7a31331-4868-35eb-adb6-1378bf59f2d4 | -13.5911 | -51.458 | 2026-09-28 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 57a46f83-9d5d-343c-92a9-b3de2b2c7921 | -12.2897 | -50.2712 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 363f093d-c9aa-3987-816c-ecbec7bb8329 | -11.9777 | -50.7371 | 2026-09-28 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 70c483b7-4713-3f9d-aeff-5afafee9110b | -12.7674 | -54.0502 | 2026-09-28 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d5412b72-3468-330b-b5d4-fae70080bfa3 | -12.0365 | -50.6233 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4bab7a80-0940-301e-95d3-33e30b029c7e | -11.7132 | -50.618 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8972b63c-a57d-3c78-9f58-a7cf4f1cbcc3 | -10.9538 | -50.6592 | 2026-09-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 471fb883-9d29-3614-bc3a-c8bb2abf4ae8 | -10.8184 | -61.4191 | 2026-09-28 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 95386106-2179-304a-be46-d717536c0d8f | -10.1713 | -63.0571 | 2026-09-28 15:50:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a483f966-ee2c-3aea-aaad-6258aab9319b | -11.8281 | -50.562 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| d017f285-d0f6-3212-99b1-82fc682d5e7b | -10.8371 | -61.418 | 2026-09-28 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 0ac5a455-e142-3471-9e5d-84c76461abde | -12.1115 | -50.7001 | 2026-09-28 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 446dce45-231e-3bf3-9023-87aaf91e67e6 | -10.9154 | -50.7059 | 2026-09-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 727b89bb-c47c-37ce-b130-f5b320680e5f | -12.3088 | -50.2688 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| c6f95ff1-156b-35bb-b1c3-a8040812b376 | -11.751 | -50.6351 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e56f8c7a-d257-3df6-8847-175acf70b55d | -11.8659 | -50.5791 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 148068fd-c6d2-3984-b19e-7138e75d3c48 | -11.6186 | -50.5861 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 055dd262-53dc-3919-be5e-54df7ae4f048 | -10.8191 | -57.1795 | 2026-09-28 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 27394fce-5676-31e9-9948-b70055c6ac4f | -10.6035 | -49.9913 | 2026-09-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0e045618-5164-3b2d-a801-0bfd72fa7018 | -11.0424 | -54.0336 | 2026-09-28 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d1eb4ddf-9634-394e-af34-5608854eb89a | -11.6951 | -50.556 | 2026-09-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 8c2a9c13-a8d2-3eb6-b1b0-aae97ec119ca | -12.8658 | -44.7813 | 2026-09-28 15:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 95d4335c-cdf3-3fd7-9603-95c9e52c4aa2 | -9.9976 | -50.1179 | 2026-09-28 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 04d59749-c07f-357f-a859-ffb8904813bf | -11.1178 | -51.1304 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1d304e8b-eaa0-347d-aa17-0ff0b61a73ad | -9.9396 | -50.2304 | 2026-09-28 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |


[Clique aqui para ver as próximas entradas](README90.md)
