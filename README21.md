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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 776cbad1-677d-3b8f-b118-94995ea2f5e6 | -4.22801 | -47.21021 | 2025-08-15 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 196ff93d-f7e1-35fb-94de-2affa8565bba | -8.31083 | -45.02298 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9094cd7-f17c-3187-b8f9-879f4ffcd78e | -5.76011 | -46.67165 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 031ed478-3969-3d05-addf-7cc4a380092b | -6.95173 | -44.54973 | 2025-08-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b164e99-3ae7-3588-af96-72b967281b53 | -8.30549 | -45.00706 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26bc714d-92aa-3911-8b75-2c9c8bec6ade | -3.64883 | -48.32625 | 2025-08-15 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5e2f138-d41b-3b6f-9a50-4fe103e4c16c | -4.98462 | -41.71565 | 2025-08-15 04:02:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7fd1b64f-898d-3918-8375-7daf2c7d0137 | -5.78202 | -43.60568 | 2025-08-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0558abb1-0c3e-39eb-859e-1f647a7e393a | -6.59042 | -44.64153 | 2025-08-15 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da754984-cbbd-3a55-9c49-96f9915ad7db | -7.14569 | -44.40847 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebe17b9a-7b4c-3341-8815-753e3fb2c6db | -8.30776 | -45.01744 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb1165b0-0849-33f0-9dd7-ab78f1d8ec67 | -7.38855 | -44.88093 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41a0b0bc-c17e-3d34-b3bc-889fbdb9eb7f | -7.38716 | -44.86552 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 396800a6-a4d2-3af3-b515-16d49bd2e0bd | -8.74255 | -44.04155 | 2025-08-15 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93df6acd-6ee7-357a-b60b-f731bf13e30f | -8.51663 | -43.32303 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 84008132-3c96-3a9d-a1bc-d7e866e7f87d | -6.3296 | -42.80398 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85cd9605-3981-3aac-a4ba-c24b8a879fc4 | -6.10475 | -44.60899 | 2025-08-15 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8983ebfe-cb3b-3818-a805-cd190eb4c59b | -8.19999 | -42.2503 | 2025-08-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1c852ea5-732c-3fd9-9b33-e696b8f85b7e | -4.59702 | -43.32401 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa944dc-d1fe-35ec-8afb-2a2f2bfe083d | -9.03407 | -40.52494 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d56b8110-a165-335b-9f25-4b2511393722 | -6.96781 | -42.87405 | 2025-08-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4faa2c1f-da48-3b90-bef6-be6d682d152f | -8.52632 | -43.30824 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e1888cf-849c-3381-9b92-a9572e5ef80a | -5.60271 | -45.37857 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aeff23c7-e56f-307d-87c0-742d0d347197 | -8.52016 | -43.3236 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ed4fc32-b789-323f-86fd-aa2b41d705da | -3.44744 | -48.96872 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d454db2b-ede4-32af-9e56-631d153b5fdf | -10.18436 | -49.50421 | 2025-08-15 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dffc9950-80a1-31aa-a670-dd7e1ca33ac6 | -7.85631 | -48.23908 | 2025-08-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c362a7a7-ccc4-337f-b092-ab7bef6e7664 | -6.81162 | -43.93856 | 2025-08-15 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d52d9f40-8a59-3590-8171-3e1eb3aa8738 | -5.54133 | -45.37632 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15c11932-38d0-3252-9351-bd335b3e1766 | -6.33666 | -42.80508 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af693a11-4c28-3906-a212-c479ad6c3de0 | -12.09162 | -43.33999 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985a54f3-304b-3c42-aa6e-28068576cab4 | -6.55654 | -49.49493 | 2025-08-15 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc7ed462-3bc0-3dc6-8c2d-b763304bd052 | -11.18762 | -40.95512 | 2025-08-15 04:02:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c502097d-ba7a-3e7d-ad8b-ee577acfb68d | -11.03111 | -45.06717 | 2025-08-15 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43a45ca1-62f7-3c75-8121-1ebaabde3cf0 | -7.29257 | -43.82188 | 2025-08-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ab4895-9f19-3382-a859-c412aac1f60d | -4.59476 | -43.31469 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 34886f36-c375-3ff6-b8e0-191f784e1ead | -6.27872 | -44.96257 | 2025-08-15 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c9878d9-e9ff-3a77-8909-b4b5128abd0e | -5.36611 | -41.2421 | 2025-08-15 04:02:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 473acb13-e907-333e-9ee6-0ce946c9848a | -5.68388 | -41.4061 | 2025-08-15 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 509e13c7-1c84-3853-b87f-5cecf5ceaed7 | -7.09196 | -44.42969 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84218755-9c15-3022-87f9-4894c20517f8 | -7.42693 | -44.58385 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9718965f-499e-34f8-b139-8946f257eb86 | -7.39654 | -44.85732 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2748748e-6698-3140-bb0d-7f2690d90e79 | -6.97197 | -42.87069 | 2025-08-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 77977bbc-bfc4-36e5-aaeb-6db567b5bd94 | -7.86302 | -48.22911 | 2025-08-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cc071178-f932-308b-ac15-31f82bd77a72 | -6.33026 | -42.79993 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09837e57-a51d-30f5-8390-1fab15d29378 | -7.39797 | -44.87259 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f49b2dc-72cc-358a-944b-16ac311e52e8 | -6.33313 | -42.80453 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c09d7ce-9d70-3e42-ae55-78fbcb62dcac | -7.42879 | -44.58079 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf7fbe3a-3a89-32b3-8c49-b3a2ea91c36a | -11.91595 | -43.44681 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42813d77-9983-3c52-820d-908f5734adb3 | -8.52345 | -43.30369 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bbfafc6-8696-301b-b689-0af51ce4cec7 | -9.18251 | -45.32976 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64bf0367-19db-3acf-89e7-ebe29fa22f36 | -8.46756 | -39.17706 | 2025-08-15 04:02:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1495c0d-a3cb-3ad6-b300-0c3856567828 | -7.29137 | -41.58846 | 2025-08-15 04:02:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b78a14d5-61cc-3094-a41e-9a881c210910 | -9.81228 | -47.7564 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c206840b-885e-3e73-836d-903d43744e2f | -8.32174 | -45.01294 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ade1bda0-5f39-39bb-b564-32bcf70ecc01 | -7.29186 | -43.82626 | 2025-08-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59a4bba8-2738-3dde-ae10-843473ec41b9 | -5.2733 | -45.17192 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5faf93fe-be4f-38ad-8b5a-40fe6c42c526 | -6.21975 | -43.33954 | 2025-08-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| decd2dab-69e2-3689-9937-1eacb698e049 | -5.84801 | -39.36791 | 2025-08-15 04:02:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c37a81b-8f8f-35cd-a7fe-4209ee264919 | -8.52541 | -43.29179 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e24d9c38-6ad9-3acb-8a99-29ab22d4eb09 | -9.03131 | -40.52095 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68ba0538-149b-3e12-b9ea-d07b698b4946 | -4.12239 | -49.4369 | 2025-08-15 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c59bd666-f5c6-34c3-8380-f0cc1b3456b3 | -5.76786 | -46.66899 | 2025-08-15 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 53e1311a-3cf0-3dc2-b0ee-aab6b191a80b | -3.42795 | -49.04816 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2dd1e3e3-ee43-322c-8f28-5f4d17bbae14 | -7.61369 | -45.19643 | 2025-08-15 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b44036b2-d027-30c4-aeec-d5a736d8ff2a | -7.02673 | -44.28268 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf622cf7-2461-3585-a9b8-17f41554301e | -7.64076 | -44.93682 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 94d8d5fd-8cd4-3781-b1c4-fc6f76d6f876 | -11.02662 | -45.07104 | 2025-08-15 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31d48ae5-4931-363b-bfb9-ffdc731c0177 | -6.60982 | -42.77457 | 2025-08-15 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c3700e7-6317-3ef0-8977-5be21796ec1e | -9.81394 | -47.75459 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38b68ab7-7871-367d-b6ac-811901f850f6 | -8.30857 | -45.01258 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb3f24f1-bdb9-33e2-8db6-ef15ae294fa4 | -5.59472 | -37.83078 | 2025-08-15 04:02:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 160764f3-cbb4-3151-9def-b7778ebbbf41 | -10.96726 | -49.57207 | 2025-08-15 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29e4056e-0a79-317f-81c3-701aa98b818c | -5.68416 | -43.65514 | 2025-08-15 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c56daa3-7cb7-3765-b1da-4e815d53c2b4 | -6.94632 | -44.55857 | 2025-08-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d39893ea-3b1b-3322-89c0-0fcd4b13dd88 | -11.81011 | -44.26465 | 2025-08-15 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4e6695e-e68a-3200-83aa-798f5625617f | -8.3147 | -45.02367 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efc64d64-ea95-307a-8cda-a9764f3d7ff9 | -8.32018 | -45.0146 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea2580bf-9815-3320-b12f-105c03ff4ae6 | -8.52908 | -39.63924 | 2025-08-15 04:02:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49de093c-9756-32c4-9504-01ab646d59fc | -10.17743 | -47.91024 | 2025-08-15 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45bd9e73-16ab-343f-9438-97d6b183ee5a | -6.6063 | -42.77403 | 2025-08-15 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 737b0663-ea2f-34c8-9f33-922bf9736196 | -9.19811 | -45.33244 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdd2d219-172f-39e5-b4ad-7d9dba85a73a | -9.02415 | -40.52338 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9810abf7-8ae4-3afa-8c5b-87e81d2db48a | -6.95095 | -44.55442 | 2025-08-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1831527-209d-31bb-b810-b4ced6998889 | -4.60144 | -43.3202 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 919aa7ae-4c21-3a8c-8783-5ed126a5f69b | -4.60514 | -43.32078 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d616a1dc-3b15-303c-b3e2-4a5412968a42 | -9.00611 | -48.72089 | 2025-08-15 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 979c64ad-a382-3f5b-bf90-eec9b6576271 | -6.90574 | -45.21075 | 2025-08-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a2b77dd-2c64-3fc6-85ee-8ecafc8ab24f | -7.8621 | -48.23442 | 2025-08-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 333984f7-c8ad-34bb-b755-abd564fb3ff0 | -8.31163 | -45.01811 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d7f57eb-afec-3cff-949b-2b4b474ce5e0 | -7.01198 | -43.85948 | 2025-08-15 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8538e6e-f525-3edd-9f9f-93f61f94c4a6 | -9.0357 | -40.51451 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bfff41fc-7970-34a2-bf2b-3e9e3fac4d38 | -5.59858 | -45.37784 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5638aa6b-a7f4-3342-91a3-7cffe425bd13 | -6.96845 | -42.87012 | 2025-08-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e20305e1-e4d0-36f2-97d7-a2c94c7eee94 | -6.90975 | -45.21143 | 2025-08-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7fde28fc-b820-39cc-97e8-db9172612df8 | -4.12682 | -49.43718 | 2025-08-15 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeb37b36-be0a-3fe9-a957-f9a1f5de51b1 | -11.03036 | -45.07169 | 2025-08-15 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1deab056-8e6b-31a4-850f-f79f998dabb0 | -4.60216 | -43.31583 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05342e2a-dff9-3e61-9271-5a39d5e0a9f0 | -7.85817 | -48.22842 | 2025-08-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4286746e-574d-3b6b-915f-e78df48d56b9 | -3.44687 | -48.96679 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README22.md)
