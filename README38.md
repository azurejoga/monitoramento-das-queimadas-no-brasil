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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b494f98-3a24-35a7-aa76-be0b61656229 | -8.13994 | -46.78997 | 2025-09-19 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3edb83a3-d832-3a44-894c-3b2460686233 | -7.1927 | -44.42233 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 12bddb9f-6553-3b25-8e1f-2e3c619cc7ff | -5.00293 | -43.17484 | 2025-09-19 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 963ae757-cada-3127-a29d-aa76955e6b3c | -6.6699 | -44.87112 | 2025-09-19 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 62d78b1b-d68d-35b8-9e4a-d5139ed2232b | -5.92159 | -45.08294 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6ef00a5a-099e-30a5-85ee-541bbdefc5d9 | -7.36437 | -44.58118 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c78ca88-c938-3998-be36-2b8991a86cea | -12.0969 | -44.80349 | 2025-09-19 12:17:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 89efab1f-dda0-3c67-9b68-30561c564ea6 | -10.06703 | -47.23068 | 2025-09-19 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 34178479-017c-353f-b213-4255c00466bb | -7.04857 | -46.41977 | 2025-09-19 12:17:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2df3bda8-2be2-34ef-aa66-1272fc985b58 | -10.28878 | -46.45861 | 2025-09-19 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 31fa4351-f472-3f6d-b52e-19bb0900a47d | -9.72658 | -45.93301 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5632f6f1-7367-3fac-a05d-32ac297d57b3 | -8.03621 | -45.70308 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c5cbb0c0-d4de-39da-935a-9f93afa29f6b | -8.23781 | -47.83432 | 2025-09-19 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5039328-cdd5-35cd-9a85-2f6696921312 | -6.43071 | -43.87229 | 2025-09-19 12:17:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7d1b49ac-2c3d-3962-a85e-1d4edf3c171e | -5.99407 | -46.6357 | 2025-09-19 12:17:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b3dc108a-b7b4-3122-89aa-671777c388ce | -7.27385 | -44.21984 | 2025-09-19 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b09b6d9d-ad86-351d-981b-6b52875b5dd6 | -9.18963 | -45.29213 | 2025-09-19 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 63701ea8-708c-31d1-bac9-484ac43cd544 | -7.18466 | -44.411 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d1231c81-7a04-3eb8-9869-90cc9b553e28 | -8.89778 | -46.1272 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| de36ec98-d453-3c2a-a69a-c64eac49808b | -6.90986 | -44.80848 | 2025-09-19 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 334c5408-a581-3903-b663-f6096844e695 | -6.42927 | -43.88278 | 2025-09-19 12:17:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| de964c41-9fe2-3449-a935-3dd02dcd74e4 | -11.16487 | -45.32832 | 2025-09-19 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7a11de8d-2c79-3327-ac78-1b780f39b84e | -9.00788 | -46.33055 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| f2ce93d8-9fe8-39d3-8761-c3f84194d998 | -6.55415 | -47.80054 | 2025-09-19 12:17:00 | TERRA_M-T | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ad4847d-3f7d-39e4-8191-ac82422919a3 | -6.38194 | -43.33311 | 2025-09-19 12:17:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 942a52e4-158a-3a8f-b861-bad5473927d1 | -12.10088 | -44.84855 | 2025-09-19 12:17:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8fdacf06-bc30-3bc4-9b17-9e55dcecc873 | -7.36299 | -44.59109 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2d28405c-b307-3c54-aff3-b94f8d90e5ed | -10.24487 | -48.0494 | 2025-09-19 12:17:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| bed1c777-0f7f-343b-b133-4c58faa6756d | -8.61474 | -45.71659 | 2025-09-19 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 49ed933f-2ed9-30ec-9bac-479f2a009201 | -8.93482 | -46.32361 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 405e3f1f-07f0-3b90-b5e7-165b73a5b749 | -6.67123 | -44.8616 | 2025-09-19 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6f24a8f5-439e-3e09-982d-75c2ee74b6e2 | -8.03233 | -45.73058 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 613827e5-c230-388a-8bef-8a00f39e0dcd | -8.48718 | -44.72654 | 2025-09-19 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 211c399e-3e07-39a0-b719-d875c977330a | -5.97623 | -45.02115 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 98e24a37-0766-3a97-a294-cd6294b724c2 | -8.63452 | -45.70688 | 2025-09-19 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cb0a9bdb-703e-3f40-85f5-6ef276131a5d | -7.264 | -46.34227 | 2025-09-19 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5d091265-92dd-368d-bc02-ee970720ba5e | -8.99082 | -46.31297 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 272548fe-a3dd-33ea-8c15-02419ab1d080 | -9.73013 | -46.56459 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f24b2e5a-749a-3f60-82f0-aeba9ebea1fe | -7.26871 | -44.2238 | 2025-09-19 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 84904b97-c044-3ef4-8b5d-aed34a1405cf | -5.97753 | -45.01187 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f3f59642-75d8-39bd-a62c-f83455c34827 | -5.12244 | -42.90572 | 2025-09-19 12:17:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b6078bce-026f-30df-ba62-ef8ff11dade9 | -7.70861 | -44.40485 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| dac85ec1-a2c0-3375-a9f6-5ef15245c9bc | -8.49207 | -44.73322 | 2025-09-19 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ef042403-66a3-3edb-ab24-10e90d00c6e5 | -7.56753 | -46.73505 | 2025-09-19 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ed5527f0-3c74-382f-bb78-f29dfd27279c | -9.70337 | -46.75327 | 2025-09-19 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| fe1854fb-51e4-3c87-8ce1-a1a59bf736d7 | -8.98952 | -46.32204 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 3d712a6b-994a-3b53-bf95-b0ce9295741f | -10.06575 | -47.2396 | 2025-09-19 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 545dcf13-dde1-3084-a609-ac30f8e413b2 | -6.8507 | -44.16289 | 2025-09-19 12:17:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 12118fa5-da68-317c-a510-ba7b7928cbd4 | -8.55761 | -47.54028 | 2025-09-19 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b4c7215a-2711-3420-8bef-37a6830af00d | -7.17558 | -44.33677 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cc44d8a9-0246-34ae-8f00-365f7e420c21 | -8.04132 | -45.73187 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a96c7ff8-163c-3e10-89fd-bb39a74a5f3f | -9.73692 | -45.92486 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4025336a-a339-343e-abff-cc9c499d0bab | -8.79928 | -46.04239 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a6c613cd-e5c3-349c-85bb-dadcaf071fd1 | -5.7184 | -43.62809 | 2025-09-19 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 917436de-c4f4-30ae-9a46-4bb6804404e5 | -6.08027 | -44.86929 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 24a69ff8-1e0b-38a5-b5fe-69f668d9bc29 | -8.92592 | -46.25784 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93ec8bed-a1b7-3f63-9807-3d328f4aaec0 | -12.08423 | -44.82407 | 2025-09-19 12:17:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5e8a96ad-01cd-3e9c-bfab-8dabf84a3c90 | -7.57765 | -46.72745 | 2025-09-19 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 367c195d-28f8-304a-aebb-10ec98ac78c6 | -8.99843 | -46.32327 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 04b2b3b7-ae5e-3d4f-8dbb-7b908651c551 | -8.03103 | -45.7398 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 393294d2-ad3f-3c66-a6c5-8c479d01de2b | -8.87861 | -46.13383 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a3cb9372-55c5-3b44-8f12-b3acf6847b4e | -6.41287 | -43.85909 | 2025-09-19 12:17:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bd87a767-5459-330e-8114-18face396910 | -6.38072 | -43.33827 | 2025-09-19 12:17:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 37319855-6e1a-38ba-8382-05a9ee68d7f1 | -6.58826 | -45.58021 | 2025-09-19 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 56947c4b-f193-3769-9f4a-5edc55c238fb | -8.02852 | -45.69257 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 60f1eb4b-e50c-31d8-a9d3-0be6351fe613 | -9.86798 | -46.43381 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a069509-2b68-3a3b-a089-152d90060863 | -12.10668 | -44.80486 | 2025-09-19 12:17:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| eda20227-ec5b-396f-a02b-ceeac8f3fd85 | -11.18462 | -45.36804 | 2025-09-19 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d54829c8-c60e-30f4-ad2d-bbaff70e6023 | -6.97465 | -42.80828 | 2025-09-19 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ce402fa5-6ffd-31a7-9a13-e73b24e26099 | -5.72811 | -43.62935 | 2025-09-19 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 45856dca-5684-3be2-b08d-53b34450be3a | -10.35432 | -47.86932 | 2025-09-19 12:17:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1813efe8-6354-336b-b88f-bf683047f402 | -5.12081 | -42.91744 | 2025-09-19 12:17:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0d791fef-aee2-368a-b13f-3cbc3f039415 | -8.61288 | -45.33286 | 2025-09-19 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5fa98054-be45-3c3f-a7e5-e34cd9f7273c | -8.14249 | -46.77224 | 2025-09-19 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d1436016-6038-3f93-929e-1ecd1c6eaef0 | -7.26273 | -46.35114 | 2025-09-19 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c4f1854e-e0d2-3b12-93e3-ada498826196 | -10.3632 | -47.8706 | 2025-09-19 12:17:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d8341b44-3c20-3fe3-8476-6aa1c01588d8 | -10.6927 | -46.46599 | 2025-09-19 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 369de334-098e-30f6-b739-8afc693a48df | -4.96711 | -43.21529 | 2025-09-19 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aef4273a-0991-388a-a00c-17a8391c9daf | -5.02571 | -45.09427 | 2025-09-19 12:17:00 | TERRA_M-T | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6bbc1020-2044-3b54-8e65-42fb5ce0a879 | -12.09259 | -44.83609 | 2025-09-19 12:17:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a7fb86b6-6682-3ba7-ab37-1fb6c13132c8 | -8.88883 | -46.12599 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| fa787ea5-4c4d-3547-ae88-48ca803ef95e | -8.62336 | -45.32457 | 2025-09-19 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 309030e3-3969-348e-a658-eb9932c63b82 | -8.91415 | -46.26825 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 55eee15e-ac96-3918-85d2-a85986a89513 | -7.18329 | -44.42094 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 3e28d220-3cfd-31b8-a2ac-794e6936d0df | -7.65563 | -45.13328 | 2025-09-19 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 344e6f05-58a1-3990-995e-b06a715124d7 | -9.74449 | -46.98426 | 2025-09-19 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f5befc21-9d9e-306a-9315-4d38b8eeecad | -4.38265 | -46.29761 | 2025-09-19 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 2075fe93-3cf9-33ec-af40-523e1f3c8260 | -10.23309 | -44.99374 | 2025-09-19 12:17:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d948f77-73b2-37c8-abe9-8233443bf16b | -8.62204 | -45.33405 | 2025-09-19 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| dd74896e-7925-38f6-88c1-a2945ba6e7fe | -7.61897 | -44.45917 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 89a38f06-6a2e-3385-9b66-2cca421eec9d | -8.06727 | -44.08435 | 2025-09-19 12:17:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5dd37c66-103c-3685-9f5e-586eecedddf9 | -6.07109 | -44.67721 | 2025-09-19 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 746cb381-c9a6-382d-85b3-78394f9b6e12 | -8.01307 | -45.73724 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a4309de3-ff03-3e8d-b7f0-62ca46e4c60c | -8.13604 | -44.46614 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d1de8744-cbee-35d4-b696-1bc1c99ea56c | -6.90199 | -44.79758 | 2025-09-19 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 16377f69-7b25-3a34-aafd-47929599c8e2 | -9.70465 | -46.74432 | 2025-09-19 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9daebf7c-3b33-3024-a40a-7bff05a741ad | -7.55842 | -44.78195 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 677a88eb-4d3f-36fd-94ce-76d2ada98032 | -6.91668 | -44.76033 | 2025-09-19 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 62c17d8e-3ae2-3a8b-963b-4830ac79b5ce | -9.7278 | -45.46222 | 2025-09-19 12:17:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 186e8980-b09d-3baa-871f-12a8e8ccc932 | -7.23607 | -46.6004 | 2025-09-19 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README39.md)
