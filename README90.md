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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db30efbb-12ef-3772-85f0-d332730277cf | -6.2959 | -43.5263 | 2025-08-31 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1834a27b-af7e-35e6-85d6-6ae60cdac126 | -11.0658 | -44.6137 | 2025-08-31 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d45c087e-4361-39c6-8109-53c744e21e09 | -14.8208 | -46.7337 | 2025-08-31 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| facbbbad-23e7-300a-aaf8-a5a5b9a2ae35 | -14.5448 | -51.9943 | 2025-08-31 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8e55555e-a8c4-3872-be41-474955e115cf | -7.9729 | -46.4301 | 2025-08-31 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 56e60f3b-f270-3fb2-b667-a26809c211a7 | -7.8543 | -46.9525 | 2025-08-31 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| beb7db1c-d6de-38a9-b215-e8b59750c694 | -5.4824 | -44.3969 | 2025-08-31 13:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 0a60847d-8759-3201-baf8-0628ba98f151 | -7.0951 | -44.3128 | 2025-08-31 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| ea47cdf5-26cf-3ad3-9e95-83d94f48a0fa | -11.3312 | -43.6399 | 2025-08-31 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 278.7 |
| 60b5fc8e-0aa3-3c53-9ec3-f0c816a5d65e | -11.8357 | -46.5194 | 2025-08-31 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4a56125c-af71-397b-ad95-da86b34303c1 | -7.8541 | -46.9747 | 2025-08-31 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 88414ae7-076a-3656-9b51-2a31dd53b488 | -14.3532 | -51.9132 | 2025-08-31 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3100b066-eb3a-3446-ad8d-9bb41c727e08 | -6.5021 | -43.5553 | 2025-08-31 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1aa26190-2a43-3669-9fcd-397bf3628efc | -6.2599 | -43.3662 | 2025-08-31 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 5dfd7e9f-c60e-3921-8966-0435c35dd4d5 | -13.3443 | -46.953 | 2025-08-31 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7a128508-1b5d-3c3a-bb9f-4c886dbb1747 | -12.3099 | -45.7 | 2025-08-31 13:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a3feb5a1-9e8c-372b-903d-6a4b25b03135 | -7.1139 | -44.3111 | 2025-08-31 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4bb94775-0c6d-3fb9-bb0d-a2f7befea07c | -7.4466 | -44.8079 | 2025-08-31 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 29618423-ca40-3d48-a4a6-b90fda6bf342 | -6.2597 | -43.3895 | 2025-08-31 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 7eaac9a1-4845-31f2-bc4a-56a6d5385c11 | -14.8013 | -46.7371 | 2025-08-31 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 8b9f699f-c4c2-3efa-85f4-872ec1839b64 | -12.3924 | -46.4399 | 2025-08-31 13:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| f6debe6b-f72d-32b5-be34-81d79fcbf4c1 | -7.4178 | -47.4537 | 2025-08-31 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 698df299-a823-3bcd-882d-33bc70cca406 | -6.2409 | -43.3911 | 2025-08-31 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 5b3c6638-8222-351e-be86-3d26551ae8e6 | -15.7102 | -48.9479 | 2025-08-31 13:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1361e9f8-455d-302e-8a71-d24faf6bdd12 | -5.7696 | -43.6613 | 2025-08-31 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 52cc0fc3-3f59-3224-ad67-2e425b602a2d | -6.2411 | -43.3677 | 2025-08-31 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 0a3d7d65-edda-3ddc-baec-bb062e8be279 | -11.0845 | -44.6343 | 2025-08-31 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b87d7834-8697-3fc9-b061-6e2225f82978 | -6.5211 | -43.5304 | 2025-08-31 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| abba0779-2070-3491-a8ac-454893e20229 | -6.2769 | -43.5512 | 2025-08-31 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0d19ca3e-629c-35a0-8e38-d9be7bbdbe80 | -5.8696 | -42.9768 | 2025-08-31 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| cdb260d2-e3e8-38db-8b7e-77a8e84534c9 | -14.0508 | -44.5543 | 2025-08-31 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 4661ef34-6a1f-306f-b043-173661801bff | -11.8181 | -46.4314 | 2025-08-31 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1348c1c4-a682-3d14-9ca0-87fe8e30bc67 | -14.0307 | -44.5814 | 2025-08-31 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 366ba300-53e9-307c-86fc-3850e6e30e6d | -14.0313 | -44.5578 | 2025-08-31 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 334e264a-1986-3915-b657-a7132c2732b4 | -9.2642 | -47.0582 | 2025-08-31 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 16d75f70-9f7b-3ead-9e70-2977591b8210 | -6.2771 | -43.5279 | 2025-08-31 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8108249a-427a-3bda-981b-a0aadd1a5695 | -15.7098 | -48.9702 | 2025-08-31 13:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 0931dfb1-3315-3d40-8414-f05543b16be6 | -13.3636 | -46.95 | 2025-08-31 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6bb90ece-4774-38fb-80f0-4b401f4b1a92 | -9.245 | -47.0824 | 2025-08-31 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 12590da2-1c33-3e59-a48a-c538d33f6aa2 | -11.8361 | -46.4967 | 2025-08-31 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 217d212a-0555-3a35-b30e-7a28f35688c3 | -7.5002 | -45.0538 | 2025-08-31 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 9bd96755-e27d-3cae-a2d8-02f5134e5365 | -11.9143 | -46.3953 | 2025-08-31 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 15ff5b99-b6f8-39b0-9cfd-f66f55888353 | -14.5642 | -51.9917 | 2025-08-31 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e1b431f9-81e6-345b-9ee0-ee9a19bbf360 | -11.0849 | -44.611 | 2025-08-31 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 4ca137dc-7f93-3890-a302-b60e711d0366 | -6.1663 | -43.3506 | 2025-08-31 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 7a34db87-db21-3f41-a93b-32655874a91f | -11.3705 | -43.5868 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| b9b22e21-86c7-3ea2-9a17-63846319805d | -14.5448 | -51.9943 | 2025-08-31 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ad328daa-ff5f-3b2b-8e47-9cefe02920ef | -7.4178 | -47.4537 | 2025-08-31 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 79ca5858-207e-37db-85a0-541ab478912b | -15.7093 | -48.9925 | 2025-08-31 13:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d511cfb6-e25b-3ac0-a912-be0468b7539d | -12.6294 | -48.2201 | 2025-08-31 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 388.9 |
| 12f56632-6354-37a2-b827-b5a8ed832f15 | -5.7694 | -43.6845 | 2025-08-31 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| a00c5b31-e07b-37c4-b944-4e76560a62e9 | -14.8208 | -46.7337 | 2025-08-31 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7ddfc96f-201e-3ee9-819e-c3ad0fa7cea0 | -7.1139 | -44.3111 | 2025-08-31 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 1c3eae25-cebe-3b25-8bad-62e0d9996195 | -13.4006 | -47.0347 | 2025-08-31 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3c31bfb1-2e1a-36f7-ba17-2e048cb2973a | -16.2221 | -52.6778 | 2025-08-31 13:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b1de8c7e-4ed7-34e3-8a07-523ff1e081f3 | -5.8696 | -42.9768 | 2025-08-31 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 227.2 |
| 6ae7f2f6-c2c1-342d-86d5-2124fae65136 | -9.4432 | -60.5692 | 2025-08-31 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7c3b9f28-0512-3f84-b5bf-68dd771cb922 | -11.8181 | -46.4314 | 2025-08-31 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| fdb6fb5b-264e-3d44-b325-95d0b3e47ab5 | -11.3709 | -43.5631 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 819cb5d2-9741-3f48-87a7-a5df7a4d49ef | -11.3116 | -43.6664 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 41f8f847-ad82-3cfa-82d1-a27210841764 | -11.3701 | -43.6104 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 259.4 |
| 432600b1-a628-304b-b0b4-ebfff7c311ae | -15.7107 | -48.9255 | 2025-08-31 13:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 51d9a80d-9bd2-3efe-a769-a178f05890b1 | -7.0951 | -44.3128 | 2025-08-31 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 21b34ef0-b46f-3008-b0f5-5f5507a51bd6 | -14.5452 | -51.9729 | 2025-08-31 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 155204e0-c514-3b53-9625-be5c302e386f | -8.421 | -48.2847 | 2025-08-31 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 9a34d373-f9f9-361f-8ec9-114f3a261e5a | -15.7098 | -48.9702 | 2025-08-31 13:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 184d09cf-8906-31ea-9bbc-80d4ad31225e | -6.1853 | -43.3257 | 2025-08-31 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 189.2 |
| cae716ed-59d3-3b7b-887d-8134d2e68dff | -12.6486 | -48.2175 | 2025-08-31 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a537d83f-4544-3dc9-a5e9-48761d632858 | -6.2956 | -43.5496 | 2025-08-31 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 69765e63-d292-3b2b-b35c-05e53893d993 | -7.8541 | -46.9747 | 2025-08-31 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 24da4cda-983b-371b-a59e-172034349db8 | -5.6573 | -43.6465 | 2025-08-31 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 419.9 |
| c15d9b98-c2db-30df-a92f-7ec23ba1763f | -14.5642 | -51.9917 | 2025-08-31 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 36555768-9b98-333b-a761-6574b6172087 | -17.1536 | -46.0817 | 2025-08-31 13:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8ccc0657-4a15-348b-86f1-5ec1fed456c2 | -11.0849 | -44.611 | 2025-08-31 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| d523e894-3aed-32d7-9d76-e63dbe8bbbb2 | -14.3346 | -51.873 | 2025-08-31 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 141f4045-d694-3992-8e0c-dba1959176c1 | -6.1855 | -43.3023 | 2025-08-31 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 127c6c2f-76f1-3f3a-bc75-97172666e177 | -14.0307 | -44.5814 | 2025-08-31 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 259b897e-ae2a-34dd-b113-5c63520b8441 | -5.8884 | -42.9753 | 2025-08-31 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| d0c05cb0-c99a-326c-8c13-f9523b78faf7 | -21.1919 | -51.7836 | 2025-08-31 13:50:00 | GOES-19 | PAULICÉIA | SÃO PAULO | Brasil | 3536406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 376.1 |
| 84146fa3-f339-3984-9f21-902eaeb7c64c | -12.3099 | -45.7 | 2025-08-31 13:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| db79b72b-d5b3-38ff-82d8-c735a153cde4 | -6.2411 | -43.3677 | 2025-08-31 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| bc470972-00f0-3a01-bc9d-e12b8094b68d | -12.6298 | -48.1979 | 2025-08-31 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 583dc26e-b78f-308b-8aff-3dd471cddc9b | -11.0658 | -44.6137 | 2025-08-31 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9ff85014-b56a-3a34-ba97-00d289787fc9 | -6.2597 | -43.3895 | 2025-08-31 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 75761c6c-167b-3c41-ac63-0d3534bd48d1 | -5.4824 | -44.3969 | 2025-08-31 13:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| cb71844b-0142-3290-a9fd-d2836ca41a3f | -6.2409 | -43.3911 | 2025-08-31 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 41abf610-bf80-399a-97a9-2399a987a82a | -5.3472 | -47.2952 | 2025-08-31 13:50:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 72ccb5f8-cb80-3841-a3e1-120a47b38680 | -11.9143 | -46.3953 | 2025-08-31 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 52643932-3e6b-369e-b452-c8002f607639 | -15.7102 | -48.9479 | 2025-08-31 13:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| e70a7a64-246f-3ce7-aced-768f813a37c6 | -11.3312 | -43.6399 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 510.4 |
| 17aa9f85-aac1-3c45-a9ba-27f1dc599ab7 | -6.5211 | -43.5304 | 2025-08-31 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4c86c882-11fb-37cb-bb0d-b92d80a4c652 | -11.0654 | -44.637 | 2025-08-31 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3f2816fa-1313-34ec-8840-53c0965055e2 | -14.0508 | -44.5543 | 2025-08-31 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 343967a4-971d-3875-be05-008c763c3aaf | -6.5021 | -43.5553 | 2025-08-31 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e659a358-a8c5-3970-bcd1-4ba22ed073e7 | -9.2639 | -47.0804 | 2025-08-31 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| cd5e240a-f325-3ea4-8803-7a0784e2118f | -9.245 | -47.0824 | 2025-08-31 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| fec60b6d-a2a3-3d8b-92ae-7e5a04fa7e0a | -13.3636 | -46.95 | 2025-08-31 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6e4f4bd4-0a15-31be-9c6c-68c37698e185 | -14.8013 | -46.7371 | 2025-08-31 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 49549e82-5bda-331c-b0de-41006be3a934 | -11.0845 | -44.6343 | 2025-08-31 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 4479bd37-2bd5-3039-a492-4aac1344efd6 | -11.3317 | -43.6162 | 2025-08-31 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |


[Clique aqui para ver as próximas entradas](README91.md)
