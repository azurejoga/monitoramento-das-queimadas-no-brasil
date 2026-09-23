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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f70769d9-badc-3de5-a1ed-722fc9030838 | -9.5677 | -46.53459 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb21a256-2edd-304f-8d52-fcc8aed06f69 | -6.29943 | -57.74723 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81d7c0ba-f9ff-302a-9730-bff8bcb4eee5 | -12.42405 | -46.97016 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6381e214-b78f-36e0-85b1-d30b2ecefcdb | -8.46311 | -48.68797 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a362b659-d73e-33bb-8874-fd548b969a4b | -11.28153 | -51.33371 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 276728ff-e31c-3ee2-8693-7d888f3484a1 | -6.61175 | -59.92958 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a85440e8-2b6c-3e1b-a80f-3f3b5735b4d3 | -6.6738 | -50.94225 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74b38f61-9152-3ab4-bffd-86c307687f7a | -14.37799 | -47.23814 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abad955f-c19d-3753-b66a-8dcc302746cb | -10.51467 | -44.88159 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5216c49f-93ed-3a62-a8a1-bad422bdc76d | -6.62147 | -59.99271 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abf8853a-c623-356c-aa4c-85199e78c3b4 | -9.86016 | -48.3162 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f067715-34f4-3c18-a04c-a8ecf87d90bb | -6.89648 | -46.54642 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a3bce34-61a4-3a6b-85fd-3e6b345cccd9 | -8.30263 | -44.75734 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2ce99ff-1b30-3abe-8e15-1d621abf5b76 | -6.13296 | -57.75726 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c00f86c-b50e-3048-a55c-85bff1cbb2b1 | -14.60102 | -45.64658 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0dbad34-5535-3f8f-9867-7422bf52321c | -14.62981 | -45.62176 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 336ffa51-1bd6-37af-a8ef-c248a9f2216b | -8.37474 | -45.60262 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de24d5f8-22b0-3a5b-b1a0-d625f3c5172a | -8.48353 | -44.74138 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75bdc3da-f985-389b-adc2-f7ff99f9e21a | -14.63526 | -45.66336 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8ebf719-2d25-3efb-8834-b60fb338f69b | -6.66911 | -55.05426 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a97007c5-27d3-343b-a873-10a6720f3909 | -9.04103 | -45.02055 | 2026-09-23 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8e0ba59c-12bb-3ff6-b623-4699f1c69d88 | -10.04455 | -50.2176 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6ed52c9-e4ae-3a1d-8d3b-7c4c603445e7 | -7.32972 | -55.58957 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 496f6fc3-3ae3-31b8-951f-2114dde160ae | -12.07298 | -50.04797 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf9bc7e9-7fb6-31d3-b3a9-69915da10c7f | -8.38253 | -45.59657 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b5bd799-a53e-3e25-b6dc-421caabdf6fa | -6.61738 | -59.93768 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ab6a7c4c-0ba8-3dcd-a89b-576875a691f1 | -11.40186 | -44.22165 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a7c8b31-28b7-3f0d-8908-3351b697cfc9 | -14.62472 | -45.66174 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0506ebc3-54ea-34e0-9eac-fa027342b50a | -12.76889 | -50.87055 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75583141-95b3-3eee-b810-7433f4786c14 | -6.67561 | -55.07665 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d623430-586c-35dc-9c3e-6a981474ab78 | -8.81633 | -44.27555 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2e4c1091-f3ce-378e-866b-877375852994 | -6.89702 | -46.54296 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f2642c6-72e3-32e7-a68f-3f1bd409e68b | -8.46099 | -51.4845 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1fc9d0b0-c6dc-3a11-8baa-bad38e89d92b | -8.45335 | -48.70536 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b53b6b5-f0bf-3bf0-b53c-9d5504283565 | -11.87494 | -49.94796 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7335a8eb-21a6-3205-85d8-4c77f69f64ec | -9.94144 | -48.46913 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b61ddc8e-5d55-3918-b1d1-e3bbad0da9f0 | -11.53122 | -45.35215 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 1d1e4089-21e4-3609-a668-ad48ece86b06 | -11.5301 | -45.35981 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d834371e-319a-3a6b-9844-57645f9eb697 | -6.10422 | -57.66817 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fefa7d9f-a42d-3341-a1c5-29d9071fc4fe | -12.40863 | -46.51485 | 2026-09-23 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea2665e0-bb58-31fc-a42f-bf367a7a958a | -14.40246 | -47.2533 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06317d74-d46b-3ab1-aafe-d32fba48420c | -11.47716 | -47.35793 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7196707-885d-3f46-a2d5-2efab90f636c | -10.12238 | -46.08425 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73b3cf3e-1c4c-39ad-99a3-ba1ea9c1e1de | -6.78481 | -48.68221 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7217cb31-3c0c-37e9-9dee-a3a62d8b6285 | -14.62444 | -45.65844 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7c185d6-d8f1-3a20-a57b-a8f0756b62b8 | -11.68898 | -43.44731 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3d0bcfe-dbe4-38ae-a0b9-a5db74e72f06 | -8.94819 | -50.91416 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29fee856-a6a8-30da-926a-4fc0900bf309 | -6.6823 | -55.06854 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b20910e7-d2ef-33dc-9dd6-46ecae3bc41d | -8.3072 | -44.75036 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4af30b3-3dc1-321b-a0d9-f85de7c57507 | -6.67473 | -55.05217 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be8a1dd9-df36-3fd1-97cb-4cd76e93ba11 | -11.13425 | -42.78996 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3b952f51-e488-3617-98e5-f6f8265be1aa | -12.41576 | -46.9798 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98ff3847-c609-3c1a-8edf-2ef101f58f6b | -12.60351 | -47.87796 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25d849df-0a52-3b4d-87a5-12bb17780fb1 | -6.23937 | -51.01243 | 2026-09-23 04:27:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c7dc7bb-0e78-37db-8be1-2c3a70625f34 | -6.12684 | -57.75622 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5cca7e55-efe8-391a-aba1-963255347401 | -6.89049 | -46.56317 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ed2c312-6f3f-308c-bcaf-c2e9f984a9fd | -6.93556 | -46.55605 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 450bb594-390a-3bdd-a3ea-358982ae2a8d | -6.67321 | -55.0607 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b2a4942e-ed64-3ad8-a29c-3280f60b3249 | -14.63401 | -45.62149 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 94cda8e7-ef6c-30a1-8e92-c126a30b0ae3 | -14.6016 | -45.64253 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a732db-648a-34eb-9196-5f1186e450bf | -5.89082 | -52.10139 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8832b2d6-c99d-3d27-aa64-cfaf442c8ee5 | -6.73235 | -59.42982 | 2026-09-23 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6953cf4-62ad-3a78-99d2-25ddfc6ee82f | -10.50629 | -44.85721 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab93de28-56c7-31ae-be6b-d03d9da209a7 | -12.47152 | -49.99444 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f297948-f950-3e80-992c-0a419ddd4c3b | -6.39564 | -54.88264 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0961b8e1-77dc-3fd0-8210-37990a8abb6c | -10.71276 | -48.70801 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 321603da-fb52-3d6e-a8ab-0346a2e48727 | -11.57235 | -47.7282 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 403e7b8e-1686-3974-b747-497d3646b850 | -12.42514 | -46.96303 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 437ffc59-d862-35e1-88da-8ca9e619720e | -10.00684 | -45.21762 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61b272b6-46b2-3e11-a488-459d51b8d2d5 | -6.66444 | -50.9508 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a814828e-1764-3b98-bd1e-c70f0ad195e9 | -12.41074 | -46.96804 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e60e0e15-1398-36c4-a300-3a2e92d36a42 | -6.89318 | -46.5459 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc260899-b051-3fec-a8a2-2cb125c4e847 | -6.1099 | -57.6762 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5491d4bb-7da6-3156-b026-3964480875b2 | -14.38318 | -46.79359 | 2026-09-23 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b55f90a-b0e0-3683-82e8-82537618442e | -12.109 | -50.03763 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be6f086f-d601-3cb7-a4fc-c360a798278a | -11.42445 | -45.34053 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 415a0257-0c46-388f-9908-c72d24c0a1a7 | -6.67872 | -58.56063 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b19aeefd-36b9-36c7-96dc-15df3403572c | -7.42427 | -49.86396 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 878c94a6-5e30-3632-8454-2da17511a5a5 | -12.1215 | -45.62793 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2ac4b32-1144-3999-b1ea-acb62c45e724 | -14.5893 | -45.62821 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7226aa34-bfd9-31b7-930b-0ccb47d25817 | -6.72395 | -47.79124 | 2026-09-23 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9638ec50-aad2-31dc-9c3f-b9082c28b24f | -7.58465 | -57.66666 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01182f6d-4a94-335e-abca-bbea9d61818c | -14.60045 | -45.62572 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 30e66111-a874-3ea1-b05c-820f7da0d524 | -12.12265 | -45.64371 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f102f851-fbbf-3cef-bfd0-e6b6af52563b | -10.02455 | -45.19342 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4c65362-2b6c-328e-942f-4ce47b7c5054 | -11.29477 | -51.36839 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f59b9bee-6e65-3a92-887f-41efb47ebabc | -10.27267 | -49.98121 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1186855d-2d82-3b76-81c5-9284d86a99f1 | -11.45576 | -47.38691 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77158d31-bafa-37a6-83db-cb4a07a0457b | -8.41753 | -46.89003 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff0ebd10-1bb8-3887-baf1-6e7c94172241 | -6.35914 | -58.28611 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2f88fcf-eb0f-3c38-bbf6-ef63ccb870c1 | -8.40865 | -46.86023 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f94d6f8-3a64-3e4f-85b1-77540df46d54 | -8.45055 | -48.70111 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a92ad8c3-bd6c-352e-a950-6228d276fd42 | -11.52832 | -45.34775 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 556768fd-d344-3d50-97b4-85d94fa6424d | -9.49021 | -51.90635 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3fb5878-00b6-3d54-9966-62ce4af06f68 | -13.7308 | -48.97038 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcec5bd0-e836-33be-9c83-6d6a697e2c3a | -9.56662 | -46.5416 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6369ccca-e0bb-32f4-8629-0bf2eda1e2fc | -12.0667 | -50.04293 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67a43cc8-2ae9-347d-b603-325b3f01fdc6 | -6.89924 | -46.55038 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efc3f7f2-878a-302e-8d97-ec555472b6d0 | -7.41837 | -49.85474 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2120c27-58d4-3240-b222-15f684d306e3 | -7.27359 | -45.53484 | 2026-09-23 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README64.md)
