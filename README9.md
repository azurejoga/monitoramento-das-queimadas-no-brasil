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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad52dc03-6c69-3cc1-b7bc-f2f103f813a7 | -0.25683 | -51.49699 | 2024-12-21 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05dc209-3603-355b-a066-54161a33d741 | -0.36883 | -50.08567 | 2024-12-21 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0476f808-7d92-3cee-aede-08e9f8aab392 | -1.56621 | -46.77584 | 2024-12-21 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66288c1c-537f-3dee-9593-abe7f6650291 | -1.88772 | -45.55306 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6093c79a-a747-36aa-a09b-8bec5a51ef16 | -0.8585 | -47.13186 | 2024-12-21 05:08:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 428cedfd-6c3c-3aa8-9031-3077409904e9 | -1.56677 | -46.77225 | 2024-12-21 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68a25458-e43f-3b9e-a97e-5630b2ca4c27 | -1.88554 | -45.55552 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e817de8a-39f8-3d79-b981-38e470cf037f | -1.51109 | -47.27245 | 2024-12-21 05:08:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04533188-b2e5-3093-b086-d4744e5b0740 | -1.30216 | -47.7504 | 2024-12-21 05:08:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 385f3b53-27c8-32b4-bd1c-0e5bd4361eb0 | -1.88486 | -45.55994 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6532f51b-59df-32a5-b655-4a5193790060 | -0.37316 | -50.08635 | 2024-12-21 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c3e3310-ef87-3605-a115-56bab006763a | -1.88169 | -45.55212 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fbf0dc2-610b-305d-89be-facb943c9f92 | -1.87437 | -45.55995 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b740930a-0b6e-3c8a-804c-9054600c7410 | -2.44332 | -47.48331 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b80ee6d-b43c-344d-bc0e-e185c78b4c8b | -2.49907 | -51.83025 | 2024-12-21 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 281ef276-6115-3d54-8209-0091366e9743 | -2.50305 | -51.83088 | 2024-12-21 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 993dfd2c-ac41-33e4-a08b-97262512abdd | -2.8029 | -54.18874 | 2024-12-21 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d87934f4-2233-3b15-ab91-1e89e0321fe8 | -2.07742 | -52.04998 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a03d1243-5844-3364-9d7d-8f669a28b5dd | -2.54842 | -46.88181 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 666de9b4-be19-391e-9e37-37c0d55c8a99 | -2.44019 | -47.48317 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 347d4698-9c65-395c-b2d3-b4e7f2037526 | -3.94638 | -46.41671 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b2971e0-a5db-3c5e-b942-d5b8e29f71ca | -1.22003 | -53.68259 | 2024-12-21 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6c77369-8b79-3862-9571-41c56e3b3a3a | -2.89925 | -54.50023 | 2024-12-21 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc10a52-153a-39e2-a13b-41eb27bf4a02 | -1.29153 | -53.12815 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34b2a6f9-879e-3189-bad1-ae2592bb053e | -2.4407 | -47.47987 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f92c4a4-4af5-3d6e-9555-cbfc0240ce49 | -1.26395 | -53.51788 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e52d936-0546-34a1-ba2f-15d57f0feac3 | -2.84405 | -54.5466 | 2024-12-21 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd3d8f96-2d76-32af-9d09-3e5e5fb0a43d | -1.60694 | -53.88248 | 2024-12-21 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84f82b3-4c4d-379f-bba8-6d7ecc34592b | -1.73901 | -52.16401 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 762fd90a-1bdd-3779-a3c6-e425175f40db | -1.11377 | -54.1815 | 2024-12-21 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e8fd245-0e7e-30d2-bf36-72c3ecea91a4 | -1.25975 | -53.52139 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 374650cb-6c8d-397f-8c3d-451649ecf509 | -1.25832 | -53.69219 | 2024-12-21 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d04d7de0-22db-335d-9df2-b271bb90c0eb | -3.69512 | -53.46281 | 2024-12-21 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0d56d29-d489-312b-90b5-97ce7c2d20c2 | -3.69448 | -53.46167 | 2024-12-21 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb41932-ce7f-3fa5-9dd9-fdc9c2a6b72e | -2.50817 | -48.05425 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d75ebf-e2d2-3c37-9152-2c072091b223 | -2.76918 | -47.39551 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7162132-e55a-322f-bc2f-fb906a3abd18 | -3.94703 | -46.41225 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eed11bfb-76d9-308b-881c-17743f889165 | -2.5077 | -48.05732 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fca903b-b2d9-333a-8a31-177f2dbe7944 | -2.88656 | -48.28094 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c169ac92-d58e-3a14-8f76-5496f37b0903 | -2.68366 | -54.02726 | 2024-12-21 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2f33466-3865-34b7-8899-bc46f44fc3b0 | -2.73263 | -47.72948 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c816a36-22b5-323b-a06e-6d36675d2b9b | -1.34491 | -53.85287 | 2024-12-21 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cc40ba1-1b55-32f6-afe0-5593ca8a5f04 | -3.9535 | -46.40905 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6800420e-3660-32ba-80a8-8cf3b8ef94ca | -3.96843 | -47.03017 | 2024-12-21 05:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0c1bb2-70fa-38e7-a227-514a7936ddc3 | -1.99912 | -52.11747 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 777bb3dc-6b96-355d-a353-7af59cef880b | -1.26332 | -53.52192 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04960156-0833-38f0-a9c7-16b932be9ee9 | -2.44283 | -47.48661 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f8717c0-b7ed-373a-895d-2e71944a0ba6 | -1.28879 | -53.09771 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dc2f7c1-f967-32b6-aa12-368bc389ec37 | -5.92023 | -43.47902 | 2024-12-21 05:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb5f8c3d-083e-35b0-a106-4580bc0d5e50 | -2.53257 | -53.95736 | 2024-12-21 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2a94839-f7b9-35b0-8ef8-59220b2e5743 | -2.55526 | -46.88393 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73ac44d9-dff2-33f3-94e6-34d60b06ad35 | -1.54057 | -53.98413 | 2024-12-21 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fde5b93-3277-3f1a-aeca-561abc186876 | -2.43969 | -47.48645 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efe7cb68-0325-3f43-b653-1ba12a289c01 | -1.70755 | -52.58324 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a1d6c14-b7c4-39b2-9e41-34aa09465b8e | -3.07069 | -47.48135 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0da673e-c16b-39e5-a84b-b21aa65d59de | -4.00244 | -46.55374 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fa24926-524c-306a-b547-4ce7997c5cc1 | -2.8819 | -48.27719 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bf272da-58df-3082-b805-e1c8667eff48 | -2.67854 | -46.91312 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c78a33a7-3448-3140-b0ee-1e4fdb608da2 | -1.22063 | -53.67872 | 2024-12-21 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4484de36-5d31-31c4-a0ab-0e837dfcbafd | -2.88701 | -48.27796 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb12cf85-27c1-3a27-8cae-42bba9ee4931 | -1.29243 | -53.09826 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6645c0d3-3c93-383d-866e-cc71b4560390 | -1.26038 | -53.51736 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9c127a2-7840-39d5-a437-12a8c8ffbe6b | -3.97406 | -47.03109 | 2024-12-21 05:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c148854b-94f4-3246-b19b-3ec7ace6cc27 | -2.85311 | -46.73095 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6387b08-61bc-3ceb-9669-94d0ae1ddcc8 | -1.70894 | -52.57423 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42007595-1eff-38dd-bf6a-210889d59c0b | -2.90331 | -54.49696 | 2024-12-21 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94733b75-5800-3920-b2da-a95236ff2776 | -2.73216 | -47.73272 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e01f6d32-ddb6-3f98-b153-6e3e884e1a28 | -1.28944 | -53.09349 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca8fb96c-f3f1-3d83-a602-330d0c9aecc5 | -2.44556 | -47.48391 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19f0023c-2ddf-3b9b-ac2f-87147081a236 | -1.34552 | -53.84901 | 2024-12-21 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6347b775-0d9e-3746-a178-8390f977e66b | -1.5059 | -52.6393 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0982d01-f056-32cd-b016-da6b00742c65 | -3.95282 | -46.41369 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43ba8685-cc3a-3791-9815-423bb918621f | -1.29217 | -53.12401 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce9b5285-ecac-360d-bc56-09e59ddf4f15 | -3.95223 | -46.41774 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8abd885-1aa5-32bc-8648-b1f8af75c306 | -2.89984 | -54.49644 | 2024-12-21 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abe19094-cec1-399c-b92e-cf6a63a2fe61 | -2.06104 | -52.05249 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3287d724-8f0a-396a-a4e2-0fc408d67f22 | -2.07762 | -52.04679 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5f4a77a-9532-39b3-99d3-248864e3e30e | -2.43831 | -51.78787 | 2024-12-21 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc0395e8-8395-3c18-ad72-a392936b118a | -2.6287 | -48.03676 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be37ded4-5c1e-359f-ba65-d28105b111e5 | -2.88145 | -48.28019 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7139437c-097c-3a6d-a288-72ce6a5f5dd4 | -2.68305 | -54.03119 | 2024-12-21 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa452c82-b43a-36f1-8f05-d44617482da5 | -1.26169 | -54.15498 | 2024-12-21 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 536cd704-3cef-3c0d-a822-be4a07a0a78a | -2.07688 | -52.05168 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a0af390-4acd-378d-ab56-4ab7c4aaa8c2 | -2.05714 | -52.05187 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4685344-b38a-3f52-91d8-327a6815071c | -2.7697 | -47.39209 | 2024-12-21 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 447e5a18-b53d-35db-a227-987e986c79ab | -4.06004 | -46.72663 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268742c9-6f84-30b3-a32c-bfeb1e98e1b3 | -2.73376 | -47.73327 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f576248-c19f-3141-ae78-691c196ac80a | -2.67296 | -46.91227 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d47d663-5edd-3d11-996c-ce9bb104d6c2 | -2.54969 | -46.88305 | 2024-12-21 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b415541c-3d30-383b-a4ae-83da36ddd021 | -2.79939 | -54.18824 | 2024-12-21 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c65fbd7-7256-3a3f-8dbb-dad4b9a8d5f4 | -2.06027 | -52.05735 | 2024-12-21 05:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5c20019-fe82-358f-89f4-ac6e0670b114 | -4.0664 | -46.72355 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca1d3120-ab95-3567-87d9-ea02f1353850 | -1.29347 | -53.11566 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd59c6a2-f1a0-3040-b075-3b338c4665e4 | -3.21161 | -54.94087 | 2024-12-21 05:10:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 284a1e94-20e2-356f-923d-f11d43ebef0c | -2.62916 | -48.0337 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbee604a-2577-3bf2-83d6-48a47a59288a | -3.69384 | -53.46594 | 2024-12-21 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02253645-ed58-34ec-899d-fd286359e031 | -1.29516 | -53.12871 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e1f40c5a-87a8-3625-a7e9-d6109c94e0a6 | -1.2547 | -53.48363 | 2024-12-21 05:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc242be-0edf-3126-9241-011266de3f49 | -4.06064 | -46.72261 | 2024-12-21 05:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 375bbe42-6e31-3a2c-989b-f5e0b6bb6c10 | -2.63386 | -48.0376 | 2024-12-21 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
