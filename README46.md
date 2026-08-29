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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dcb94cb-7921-3e94-958f-5b216d761c99 | -11.48284 | -45.09905 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc5081d8-7139-30d7-bf7e-42fb443029a8 | -11.22861 | -54.0111 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54332ba5-63ea-32ea-808a-d0ec104af515 | -6.57021 | -56.54345 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4aa9edf4-6c2d-3d00-a878-42656bb57ad2 | -8.82128 | -49.63104 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23bf35b4-8aa1-3671-9faf-de6db21395bc | -12.22103 | -50.54066 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 902f44fc-fc89-31c4-b33c-c9c5c167867a | -8.66739 | -49.54212 | 2026-08-29 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79b0bf5e-1885-3dc3-8683-6234d6c3be9f | -6.00253 | -57.83514 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc2ae87-bd22-3853-910c-50107b3cc1b4 | -17.28542 | -46.0192 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cad6c988-ce8a-3237-b7d7-da8d85f6da37 | -6.86329 | -59.40063 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e193942-ccf1-3f91-ac05-8d2ad0623185 | -6.18941 | -55.41628 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1839ec74-c9d9-36b4-ae30-93884d327847 | -10.40729 | -61.19466 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5f0c39c-203c-3c9d-96ba-56a60389a147 | -8.60402 | -54.83692 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1fc26c99-38d9-3aad-a11b-b4ab7b640270 | -7.9751 | -52.07657 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91116c4-4922-30e9-96a4-1351397f8333 | -5.87698 | -57.77393 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5f80aec6-5eaa-3254-884a-6c38991e1b04 | -6.02592 | -57.6966 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aeb1620-4d3d-306c-b4b9-e6b98c0202c6 | -6.37333 | -54.95939 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46568f1a-d122-3195-bbce-05ed61469bbe | -16.47614 | -49.4281 | 2026-08-29 04:53:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06eb5d9c-4ad8-3ae5-ab31-623853410782 | -11.71507 | -54.53035 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eddeb05-e88f-3f65-8083-2303bee3e173 | -6.74991 | -52.44918 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58de4476-42cd-3062-8a87-7ac8e9c663c7 | -6.42803 | -55.52551 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05bbe2f4-a97f-3ce1-b9af-044654930b5c | -7.5131 | -55.29396 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 04aa266e-1a2e-35be-8b56-6be69b30fcdf | -11.19311 | -53.9937 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 046cb650-c7d9-3b4e-850a-d1c3187fd4bb | -9.92128 | -60.44083 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 348acff7-51f5-3f2b-adff-52dce548d6f8 | -8.9472 | -63.28284 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9e4e3ba-6d74-3d9f-9366-d4bcf65c69b2 | -6.94169 | -58.9595 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df4b878f-8db4-32c5-b89d-c04c9ee2960c | -8.33113 | -47.62768 | 2026-08-29 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22f9af78-69ae-3036-a373-46c530ca1d7d | -9.1542 | -49.97356 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e600b492-c69c-39d0-95e6-cdfbf7596ea7 | -7.58615 | -61.33871 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4560dec8-0647-32f1-a327-8312fb3731d7 | -11.26828 | -54.02911 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9664692-087a-3d56-82e7-fe90198ec8a5 | -8.33073 | -47.62957 | 2026-08-29 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c1bc68b-379d-30aa-b6d5-f2782fbf8fd5 | -17.61229 | -51.61477 | 2026-08-29 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac8904c4-ceb6-3645-83ad-f2aa3c553f68 | -7.04264 | -55.68922 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f3ba0b-28bf-3444-9062-f54b067e6f4e | -5.09252 | -56.14595 | 2026-08-29 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04fb73c7-3a62-3cd4-bc43-37f4e7c1e035 | -11.03606 | -57.25159 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28e6d19b-ed96-3600-b736-6f929f6e8a82 | -20.38628 | -47.4113 | 2026-08-29 04:53:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a1b24b9-b452-3a8a-a509-4306322d2376 | -9.26629 | -45.63885 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ccee389-f98e-3a68-a0c8-65849d789890 | -11.26644 | -54.04026 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17a9c07d-ebd8-33ee-a5ac-17509fbc0218 | -9.96371 | -53.93788 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4795a2c-06b3-38a9-b0ba-07be5db91076 | -13.31683 | -48.20778 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e0d7158-e0b1-3cc3-a3f3-1e28fae1f420 | -9.4902 | -45.67968 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d3274e98-7cea-3a01-bc70-030ffdf54855 | -7.49147 | -55.28563 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46ca74e-2d36-38e8-ae2d-e2abb3a439a0 | -11.71036 | -54.53738 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60c99d27-fe04-3c2c-b7cb-465e2b0c341a | -9.88139 | -60.26583 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d2418bc-2cf8-3e0b-9c84-37dd6d5bef3b | -9.66596 | -55.08781 | 2026-08-29 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffc0802d-646b-39c7-8b3b-d4b071db8006 | -7.51086 | -55.28439 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e1c77bf-666b-349b-9bd8-679d8c553598 | -11.83828 | -46.77003 | 2026-08-29 04:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb028884-f4d0-3e7e-90ae-a80a23da516d | -12.19009 | -50.55918 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ddba0d5-6cd2-3f7d-b6f9-30130ddc7bcb | -7.50489 | -55.29723 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01119cda-1217-3fe0-9d4b-e03eeea7783a | -8.31976 | -47.62601 | 2026-08-29 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 471a025f-58d7-3895-ae12-103bf4da9d11 | -9.3031 | -56.80312 | 2026-08-29 04:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59ff46d4-130a-325f-8708-998db56790e4 | -6.57778 | -56.5485 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cd8e96b-b8b3-34e0-bc30-41583fc72864 | -6.53917 | -55.24811 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9028ee08-20ff-3ca0-a78d-ea82a6ebafec | -11.36748 | -45.16087 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 08f41a70-74dc-3e0b-a5c0-7fa82bcdf622 | -8.97869 | -50.79435 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 237e5034-753d-3b9e-86cf-e95804843500 | -8.53571 | -55.27055 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db05a0af-c0fe-3233-9601-a0b551737573 | -11.364 | -45.16471 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1c69c1c0-3651-3e30-8098-69a0727dc17d | -10.5517 | -59.61757 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44dcd70a-fe6e-306a-a72a-d9964652b6c4 | -5.88908 | -57.75708 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| b4272551-57e3-34be-a9b9-9ba5451cccb7 | -9.16209 | -58.31355 | 2026-08-29 04:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94619f56-a55b-31d5-af70-c3933c41bca3 | -11.63003 | -54.57938 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3075352e-817b-3cbd-8a7a-62004ec4d73a | -5.18284 | -56.0537 | 2026-08-29 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b70b7c64-b478-37dd-a5d3-6fae6b7ef4d2 | -6.15823 | -57.80043 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b3bf916-164a-3886-8912-0de2c83be559 | -10.54178 | -50.46833 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b7e5024-a1c4-3285-881a-9baebf9e2cc3 | -10.50106 | -59.62874 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26979f84-3ae1-324b-966a-b02df7950312 | -11.78035 | -47.6535 | 2026-08-29 04:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b99ef1f-0d9e-3b58-b140-0e6bc3e67b91 | -19.27706 | -49.51483 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bed0929-783d-3b02-ac96-83b13279decf | -10.90743 | -46.6144 | 2026-08-29 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66d1b4d6-e674-3e3d-9746-07f200bbea20 | -7.2797 | -45.85212 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 796f7e10-eac5-37f9-a94b-3aca8f2cbd3f | -8.60216 | -54.83508 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28485ddb-3917-389f-a126-2afaaeb72503 | -11.032 | -49.68371 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed110116-ec9f-358c-ba0a-a83d77d1645b | -11.26671 | -54.01745 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89656e5b-dcec-3b8b-ac6f-b0c21e8e7ff1 | -6.75895 | -63.06007 | 2026-08-29 04:53:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4da88713-e0c1-3028-8635-af87964274d5 | -7.28247 | -49.96045 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4992f9c-5960-3c62-abe3-75c99e9f6d5f | -6.77966 | -55.66709 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| d211cc13-0e63-3d18-b251-610b2ac25e77 | -6.75924 | -46.13587 | 2026-08-29 04:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1be1452-92ba-35bc-82af-4d85d85fcec8 | -7.11421 | -43.17042 | 2026-08-29 04:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c725ad1-a3d8-3de8-a6a8-e16467ca0251 | -10.4854 | -64.50745 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 39159067-93ff-3556-bbbd-a9a73e8efe5c | -7.34646 | -55.17256 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a010e477-3138-36df-ab2a-0cb7304a6703 | -19.00334 | -47.44408 | 2026-08-29 04:53:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 859e9321-c81b-3fb1-8116-99b0c68bde0b | -7.28467 | -45.85646 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f53238b-1171-32c2-8b9e-5183fa588f78 | -11.24119 | -53.99806 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 823994cf-0072-38f5-920e-617a5087fbf1 | -7.50786 | -55.30243 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 90271925-a375-3a21-b182-33b6dd700a7c | -12.25611 | -50.53802 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 882071a3-4849-3c19-8371-73f19809bae8 | -6.54822 | -55.24023 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 064ddd91-fe88-3f33-86a2-8ef35aeb39f8 | -11.37258 | -45.13678 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ae6a6f8-e91b-3632-9bd2-4baa6b3d5f27 | -10.50567 | -64.30603 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 81bf0123-ee17-3e5f-8fcc-0527479b1d8c | -6.58402 | -55.4436 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfec0e4b-46cf-3fa0-8882-1091cf42860f | -6.16117 | -57.78275 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24f7020c-4afd-3eaf-a523-80de8a5ecf21 | -7.04563 | -55.68301 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61557f88-8c4f-3095-9490-09a8e612dd9d | -11.04086 | -57.2245 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bddcd23c-70f3-39fc-beb4-6178b01f890e | -11.71914 | -54.52713 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82d20498-5ac3-34e4-8a68-a25d9e21dfff | -11.71227 | -54.52595 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1692c83-8fe7-3c38-aa3c-2377fde1e67f | -10.28944 | -62.81977 | 2026-08-29 04:53:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9df26e6a-f9d0-369c-85b8-5faa2a853e4f | -7.99952 | -61.40972 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8197a3c5-7e16-3c08-b1aa-7e1dddbcdde5 | -8.53352 | -55.26121 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ab5a744-30ab-307f-8789-fa43c7cf12f9 | -5.88831 | -57.76162 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| da60f24b-0484-3df9-82b7-f2aa1d206fe0 | -11.22484 | -53.99146 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72ca793c-2756-3455-b4ae-fcea2edc2bbd | -5.88671 | -57.77102 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37b0fa59-80b9-3a4a-b677-a6c42823c588 | -13.31431 | -48.1975 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 660a89d2-4b53-3e5d-aa8d-1c7f11009250 | -6.72095 | -56.34361 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
