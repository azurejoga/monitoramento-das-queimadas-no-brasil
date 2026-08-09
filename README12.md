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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ed142e0-f2e0-3af5-a7cc-fc523167bcfd | -11.62266 | -51.09362 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 504a3259-42ca-3c77-8005-6844e54889cd | -6.98148 | -42.90359 | 2026-08-09 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a16b5ef-ca28-33ba-80c4-fbebb202371a | -5.72785 | -49.14166 | 2026-08-09 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0adf0c6c-9e29-3279-9081-40b58e4c4470 | -10.24726 | -45.81079 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1b84648-7cac-3e2e-8745-1f4240585f0d | -7.58398 | -45.20797 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 316f4603-5863-3aca-832b-60b84ba5f576 | -6.91024 | -41.9287 | 2026-08-09 04:25:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d945f30-759f-3978-bdad-914267c79679 | -6.82364 | -56.42154 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8afb6353-a9e9-3f0f-adb5-9f98ac198533 | -9.46189 | -40.32115 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 24041d7f-2c86-3866-a488-e83c6dc1e8c8 | -10.25663 | -45.81588 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ba307b2-1fbf-3c21-9112-0d50459f16bb | -6.87788 | -44.9256 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acf2d7c9-a558-3546-9401-7b0d203d8999 | -12.10476 | -47.21905 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a0f00cf-9066-3625-bcdf-753834d39788 | -6.64411 | -56.4322 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0c6bcf0-0b1b-3fe3-aea8-4c9ef7f556c5 | -5.22326 | -44.79683 | 2026-08-09 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e3204be-2617-3986-b65d-85c6daee653c | -9.63167 | -45.51477 | 2026-08-09 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab6cbe84-239b-36c4-b117-45259aad1edb | -6.98452 | -41.47756 | 2026-08-09 04:25:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 92f5d458-84c1-3c1d-8d27-85fa3fb47e70 | -6.81927 | -56.44534 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e96ae520-2591-3a23-a66d-00c4c67d8e96 | -12.95664 | -41.81831 | 2026-08-09 04:25:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 01b25375-d77c-3602-b618-6d90da5e85f1 | -6.84027 | -56.40009 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fab9ae81-4a80-3ed1-81c7-74e008c223d3 | -7.69375 | -55.16193 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6406d0c-be7e-3296-bf85-38be6b1073b6 | -9.47769 | -40.32721 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 366f69c8-4b06-308c-8cab-2c3d90a6a035 | -9.66159 | -43.85122 | 2026-08-09 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 436363a0-b7cc-36e4-a786-9e49026d6166 | -6.87843 | -44.92214 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec7306c9-4e31-396e-8ee2-908b519f2470 | -6.8447 | -56.41062 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6594b39f-b067-3ca0-822c-13ce31a00ed5 | -6.83686 | -56.41874 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 410f372c-b675-3dd7-aa90-f61c9379cfc8 | -5.43081 | -47.25631 | 2026-08-09 04:25:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d502a29f-a4d3-323a-af22-1185b8235011 | -6.8149 | -56.43445 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64e6b00f-f7f3-3e9f-a6f0-64ee9e2eb787 | -9.46953 | -40.326 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 34ac3e28-5ab7-3a80-a453-0e7227353e32 | -6.83335 | -56.43797 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0186dcd0-e584-39f1-bf96-9f873df21658 | -7.57131 | -44.38365 | 2026-08-09 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a1fadfd-e10f-3142-a101-8af8ca17c688 | -6.84559 | -56.40572 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f22e656-eb62-3c9b-bd67-caacf4727d5d | -11.2737 | -44.86988 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ab8fa3c-3a7d-3137-b5d7-6626a0eb05c5 | -8.31948 | -46.39061 | 2026-08-09 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b13fb3f-cc1f-30d1-a100-f30e69b54b8b | -9.46649 | -40.31808 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| aac09804-9df9-3ebd-b437-9de6219b8ef4 | -6.47124 | -49.87181 | 2026-08-09 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c9a2f54-8c68-3e4c-b009-a1501fd0ec93 | -9.46597 | -40.32175 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f809c590-3511-364a-856e-6fae5fae196c | -6.83068 | -56.41782 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c03aa00a-6f50-3479-8fef-c41b04688bdd | -6.96207 | -41.50673 | 2026-08-09 04:25:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0dca06af-ae81-3221-9ab5-a2217e639078 | -7.29097 | -38.93671 | 2026-08-09 04:25:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9de022de-b9f8-3b65-9f30-f868dc7f03f8 | -7.58012 | -45.2109 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 72107a01-3a02-39fd-9ccc-6780d5bfb043 | -6.81664 | -56.42504 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7e925b1-cc71-3785-a043-4a0f80601773 | -11.03911 | -44.27557 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d3b3cad-40a7-3e02-8471-99d3dee264ea | -12.11812 | -47.22128 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eb90c09-7bac-39f0-9a0d-4d0453f7c10b | -6.9809 | -42.90734 | 2026-08-09 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fd113f38-491f-3f24-8bd3-52e66e61231e | -7.57463 | -44.38417 | 2026-08-09 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f174e1d4-a241-37d4-9271-38803f0f86bf | -7.00849 | -42.02184 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec245ed5-6621-3985-a46b-d237d207ccc6 | -9.47413 | -40.32296 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| deb5b314-2663-3231-abb9-dbc2369fe400 | -9.63112 | -45.51826 | 2026-08-09 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7b4b05f-fa9a-3468-adac-50c8594af745 | -7.00599 | -42.0224 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 358975ca-6f06-3af4-b306-2d7bd92b98b2 | -6.82015 | -56.44057 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 911c60e6-4712-3959-8b5d-42a64fe697e8 | -5.72864 | -49.13683 | 2026-08-09 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06f9f381-f936-3a1a-adaf-023ee0abe439 | -9.47309 | -40.33026 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 74d44595-34ef-34f0-9311-e0d70e7d128e | -6.14193 | -57.72239 | 2026-08-09 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 296435bd-0c23-3c15-95a4-2ea61b2fabc8 | -11.62349 | -51.09776 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eba16e81-1277-3702-b159-7f29c5b23cc0 | -12.11027 | -47.22735 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98e371be-0d9a-395e-a9bf-75343bb9dcb4 | -8.15262 | -55.40671 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 317b0d50-3e88-30e4-90ee-5cd561128b08 | -10.87413 | -50.3699 | 2026-08-09 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e5cb44f-10d1-3a10-bcc0-dcf1bc337926 | -6.41448 | -55.78713 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ffd6924-027a-3795-9b39-c30124f3278c | -6.82188 | -56.43111 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 886ec7ad-edb7-309b-ab3d-b15cba2debb5 | -9.80811 | -45.25743 | 2026-08-09 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33e68ab5-0d72-32e9-9d2c-8e02131a14a4 | -11.04194 | -44.27979 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ba45a09-e691-33b7-90f7-e80640fde1ac | -7.37872 | -42.86914 | 2026-08-09 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 266f837a-11a0-3ed6-b666-a57be16e3e94 | -11.26532 | -44.85752 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c286118-2f29-3fd6-b349-53a6f28f5665 | -8.1506 | -55.40355 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 870cd79e-3bac-3a40-bdd5-bf3fc2055d0d | -6.84114 | -56.39534 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a87d2e6-e7a9-3b6c-887b-dfa872d6a871 | -6.82804 | -56.4322 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a1c11b2-4c81-3e38-8bf1-7054255001dd | -6.85883 | -39.88129 | 2026-08-09 04:25:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d15cdad-73dc-3556-9a47-485fc7869720 | -8.15334 | -55.40285 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f6b5fab-ae90-340b-8a47-06c03662dacb | -6.77639 | -46.47364 | 2026-08-09 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19ea2324-da81-32d8-9dae-7c9862ca58b1 | -5.53014 | -45.77334 | 2026-08-09 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ce68e5e-a5bb-3fb7-b1f3-8360f1ba00af | -6.70896 | -58.95182 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ade672ac-a54e-3a1d-8745-57e1ef10cc47 | -9.4711 | -40.31501 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 8825b183-a90b-3d4d-834e-d1a0ec67ed27 | -12.102 | -47.21491 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edfa3b8d-b104-3fc8-bc4d-169d3aa0ab4c | -6.70194 | -58.94981 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e840d94d-352b-3936-8b57-8ce3ceee36b9 | -8.07913 | -44.34806 | 2026-08-09 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 758301a1-3b89-37d2-bb9a-f1c513e9a085 | -7.58674 | -45.21196 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f8015a2b-3b9f-3b5f-8a7f-d1c82a09b326 | -9.47466 | -40.31929 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 017b85b9-e71c-3cae-8e80-f2f2535a20bb | -6.84125 | -56.42957 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c22e0266-2c01-3c6d-a1ee-4704d2b2b412 | -6.60702 | -56.36306 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2bee0e0-b0d1-3a7a-98e4-ffb752b0f5f1 | -9.80866 | -45.25394 | 2026-08-09 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc812c78-b419-3669-90da-dea8f01f56d9 | -7.00894 | -42.02699 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ad8a421-4080-3df9-9557-68e93d82fb90 | -6.13528 | -57.72078 | 2026-08-09 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d48af50f-8030-3ba6-95fa-1367cdb93372 | -7.37813 | -42.87296 | 2026-08-09 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1a17b60-e243-3c89-8eb3-1590e8ea40cb | -8.9176 | -44.24259 | 2026-08-09 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e7bc713-41c6-36a3-86b1-19121c114b9c | -6.98574 | -41.47495 | 2026-08-09 04:25:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cc56660f-868c-3346-846b-dba41b4e3bbc | -6.70589 | -58.94523 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49055651-4291-3638-a97a-b6c8ec170943 | -10.25057 | -45.81133 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79beaf05-a480-3c77-9513-fc9977bb51ea | -4.92832 | -47.49588 | 2026-08-09 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6e6389-b310-377e-b013-59489c931206 | -6.82546 | -56.44633 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c1aad5d-8fe3-3495-b4c8-62f5e40d6469 | -9.47821 | -40.32355 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93270071-5b2d-3f93-9f74-b4fa04e1b85b | -11.03855 | -44.27926 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cfefbff-b56c-3394-8e8b-f855e0fc931b | -8.55333 | -45.3952 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1af0df2-f135-3db7-b53e-09dbcd133b89 | -6.77697 | -46.47002 | 2026-08-09 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6622169d-8233-3de8-b80e-afc5fe8a2af1 | -10.25608 | -45.81938 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e89e0377-1f80-35e7-b7e8-d79f94d1f7e6 | -7.58619 | -45.21542 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4669b5a-cad4-3953-8ec8-c6556c37b164 | -6.8254 | -56.41197 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 193f540b-02eb-38fa-aad7-6a419c2893f7 | -4.79982 | -56.13507 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83b941f0-7c94-3b75-8d5b-df4077abb019 | -5.00172 | -45.94851 | 2026-08-09 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c717fa6c-f3db-3e70-bdb4-b2918572e914 | -6.90824 | -41.92966 | 2026-08-09 04:25:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24127b00-db73-3732-b5af-97d2680f4027 | -8.14842 | -55.39795 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f85c4e2b-5404-3ebb-bace-f0411791cee4 | -18.64488 | -49.8499 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |


[Clique aqui para ver as próximas entradas](README13.md)
