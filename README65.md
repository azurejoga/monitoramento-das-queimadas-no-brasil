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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b6d19c3-2472-30c6-a6e3-5b7c1480f9df | -6.7648 | -59.4408 | 2026-09-12 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 1601d70f-bd60-3fb0-b39e-daf3920bcd85 | -11.2299 | -54.1396 | 2026-09-12 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 13930031-02d6-3c12-b0a8-adb5e6776bfc | -2.7148 | -57.6274 | 2026-09-12 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d2ea492e-997c-3718-8cf8-e05effe197ea | -11.4021 | -43.9585 | 2026-09-12 15:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 193.2 |
| a56087a3-ccd7-3ec1-9306-874a698d123b | -9.6755 | -46.0047 | 2026-09-12 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| e4f2c286-0122-3b54-8c53-ab65163ab93a | -9.7041 | -54.3303 | 2026-09-12 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 9300f0d1-aa6e-3b6c-b6a3-432fcdd56d9e | -6.1845 | -57.72 | 2026-09-12 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 3a899b17-0c2f-3300-8d48-daa1e15d31aa | -10.9491 | -48.3474 | 2026-09-12 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 8a17c276-7e54-3d3d-8854-7714ed21f199 | -5.8021 | -53.8061 | 2026-09-12 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 143fd60a-c5d6-3fdc-a84d-e2d2906dcf98 | -6.3847 | -55.1851 | 2026-09-12 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| bee67aa5-7f3e-36f2-8cc7-3c5e4f7534fe | -3.3504 | -59.4274 | 2026-09-12 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 0cba87de-f105-3c2d-a090-4eca2ccb7eae | -7.6008 | -46.1288 | 2026-09-12 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 222cae6a-eff4-3bb7-ae3f-66767c5991ec | -2.7331 | -57.6271 | 2026-09-12 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9b7f2e08-4e99-3742-a805-3bf93d560355 | -3.3687 | -59.427 | 2026-09-12 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3ea48dd6-5e74-3616-8931-3acef30f9ad9 | -8.002 | -44.0163 | 2026-09-12 15:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e5aea675-3d87-3da3-aeff-424267955724 | -10.5664 | -51.356 | 2026-09-12 15:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 6bd9c90a-9c33-34e1-9926-1d5710fe5e5e | -13.3559 | -51.7642 | 2026-09-12 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 637d58cc-aabd-3401-bc86-ae244d3707c1 | -2.7149 | -57.608 | 2026-09-12 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a0b7da6a-9bd5-35ad-8597-0cff4b3c7968 | -9.1339 | -51.5927 | 2026-09-12 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| d0a372e7-ce0d-3875-9bc4-dd471fb265e3 | -2.7148 | -57.6274 | 2026-09-12 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 0e3a8703-aa08-30de-a716-cfceb03a4fcb | -5.8206 | -53.8052 | 2026-09-12 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f8b39b7e-160d-3f77-a058-fd12743bd268 | 1.2244 | -50.7266 | 2026-09-12 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 74746bfe-f88f-345b-9b4f-2bab4cb8a11b | -2.7331 | -57.6465 | 2026-09-12 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2f038b3a-699b-35c2-b2b4-f2030ec5c461 | -3.3504 | -59.4274 | 2026-09-12 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 897af61c-c4a6-31d1-8493-3487f96e4bbc | -13.4503 | -48.5022 | 2026-09-12 15:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7b6166a2-9dc8-39ad-9e0e-faf3f355d7ed | -12.0468 | -49.956 | 2026-09-12 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f7c142a8-8e43-32d4-9075-c8f669d5c5eb | -7.9645 | -43.9971 | 2026-09-12 15:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| dcff29c5-1f1e-397e-8b09-9923c4b83c51 | -6.1845 | -57.72 | 2026-09-12 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 709045e8-3c91-3210-a1b0-123a504804b6 | -10.2735 | -45.3185 | 2026-09-12 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 274.1 |
| 178888d0-f3c2-3650-9179-0709e473dd75 | -11.2299 | -54.1396 | 2026-09-12 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 4168e4cf-9af8-3c2b-a562-7c6cbc373509 | -9.7041 | -54.3303 | 2026-09-12 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 8dc428a2-4c76-37f1-9b43-049157d24f0b | -5.3462 | -56.0256 | 2026-09-12 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c3df7b6c-c34c-3b69-8df8-bb5671430a03 | -10.7274 | -50.6192 | 2026-09-12 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 198dc8bd-74cf-3fbd-ab99-6b162f2c31c4 | -5.7836 | -53.807 | 2026-09-12 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ba1e5216-4b33-3df1-9c2c-059ad7bde89f | -13.3761 | -51.698 | 2026-09-12 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 8d5f0833-27e7-3b52-b1e1-d74e7c84d45c | -10.07 | -46.229 | 2026-09-12 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e578f930-df4c-3040-9b73-f86acdd714db | -4.4654 | -55.4435 | 2026-09-12 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a7f14122-d35f-330d-b559-e1986a6aaa6a | -4.3582 | -54.77 | 2026-09-12 15:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 4aa90a8c-3e42-3a35-a072-163a64421002 | -10.1006 | -45.4544 | 2026-09-12 15:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 40e748f5-47b8-338e-9083-40e6eb6effef | -3.9127 | -55.7382 | 2026-09-12 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| a86b1251-031d-3bbe-bd2f-69f06839b496 | -13.3953 | -51.6956 | 2026-09-12 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 054de36b-66e8-3039-8ae3-5375c6926483 | -6.583 | -58.9658 | 2026-09-12 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 774ad4f4-3667-3f6a-97b3-8be36f1207c3 | -13.3387 | -51.6389 | 2026-09-12 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 2440df22-338a-3304-810e-e98d917ff3b1 | -13.4696 | -48.4994 | 2026-09-12 15:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bf4466cd-567a-37ac-9b1f-638d7643c27f | -10.0507 | -46.2538 | 2026-09-12 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 211.7 |
| d8d9fc32-a901-3aab-8ace-0fcc2b3490ad | -6.1993 | -55.2739 | 2026-09-12 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0186a93a-06ef-3dd6-adaf-c631d79c0669 | -2.7331 | -57.6271 | 2026-09-12 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 5fb0332b-e20a-3717-ae2e-1b8b6b28263c | -9.6755 | -46.0047 | 2026-09-12 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0546e8a6-f530-3d7e-941b-bb34ff0b461e | -10.0815 | -45.4567 | 2026-09-12 15:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 6f8da71a-7c30-3f71-ae18-938b73666646 | -10.0697 | -46.2516 | 2026-09-12 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d09fc7ed-31a7-35fb-ab06-b55c8754728a | -5.1254 | -55.9748 | 2026-09-12 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 4bc7ff07-6335-34ac-93e1-0829e1588133 | -8.8132 | -46.9495 | 2026-09-12 15:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f18922c9-74dc-3b02-a5ed-5af977a3d014 | -10.2206 | -50.373 | 2026-09-12 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| c7367869-193a-3ebb-a3fe-a20d57b553c9 | -7.6008 | -46.1288 | 2026-09-12 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 9c4cd325-dd05-3eca-8edf-831794641c08 | -3.3504 | -59.4465 | 2026-09-12 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 4e58a9a6-d3fd-3ed9-8c75-2c6ea894e2a8 | -2.7149 | -57.608 | 2026-09-12 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 619b5374-2054-3347-a8ee-03e3baff62ce | -6.583 | -58.9658 | 2026-09-12 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f1cbffae-5c37-3001-a964-a52c6c43aba7 | -13.4696 | -48.4994 | 2026-09-12 15:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9116bf69-964c-36d9-90f4-ebabbe0c4265 | -4.3582 | -54.77 | 2026-09-12 15:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| a358e884-da55-39fb-acd3-4ffaa716731a | -5.8206 | -53.8052 | 2026-09-12 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ed1a1688-ee9a-38ee-bd87-4157d5fcbcfe | -10.0507 | -46.2538 | 2026-09-12 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 321.3 |
| 9a7c58fb-da19-36bf-9142-f69006d79a1a | -3.1697 | -58.6437 | 2026-09-12 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 22312856-b918-3f84-a0f6-e1ad56cb6652 | -3.3504 | -59.4274 | 2026-09-12 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 1ad0b192-3bc2-365a-8c22-a7f69d4e2ae0 | -11.9547 | -49.7512 | 2026-09-12 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 87c60c54-a60d-3eac-a57b-989841518ad8 | -10.2206 | -50.373 | 2026-09-12 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 43481433-9bd5-341a-b7f4-c4ea582a949d | -10.2171 | -45.2799 | 2026-09-12 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9a780767-9889-326c-9519-39ecf7c4872f | -6.6226 | -58.4995 | 2026-09-12 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ead30ec8-6e2b-39ef-b845-953dbda58de5 | -4.4655 | -55.4236 | 2026-09-12 15:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 98a624f4-4d16-3fa6-942f-d9d568823b5f | -8.0427 | -43.7798 | 2026-09-12 15:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 234.4 |
| 44897cd7-c83a-381d-b2c7-e849ea3c17a2 | -5.8021 | -53.8061 | 2026-09-12 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 310d8bd8-101e-346b-ae14-82c4c6296ced | -11.3513 | -45.7922 | 2026-09-12 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 910d07f7-1c32-3bba-8488-3c3d69d037bc | -3.3688 | -59.4079 | 2026-09-12 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 45adb45a-59bc-351a-a9a4-6e08a77b3222 | -12.0468 | -49.956 | 2026-09-12 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| afcdb008-3876-35cd-ab71-a0c5fcd3777d | -9.1339 | -51.5927 | 2026-09-12 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 7c4d7d45-9b66-3cbc-994d-b7632e1dc6be | -11.1029 | -50.8348 | 2026-09-12 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 50f6e812-f024-3355-bb9e-e8e8438beb49 | -11.2488 | -54.1378 | 2026-09-12 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| d9572633-31e7-3813-aa1a-dd97a3c04858 | 1.2428 | -50.7264 | 2026-09-12 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8db07a57-d48f-355e-b308-aa4ce28c2650 | -11.2302 | -54.119 | 2026-09-12 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 751faf07-36ec-37fc-8099-b4373ed0131d | -10.2746 | -45.2497 | 2026-09-12 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9eba0387-c414-37c2-b07e-bf0c62d32c84 | -5.1254 | -55.9748 | 2026-09-12 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 97a353ff-dc30-318e-844d-8a83ab3806db | -11.0839 | -50.8368 | 2026-09-12 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 06980ed7-d0c2-3a85-9f30-eba8f8aad114 | -10.7274 | -50.6192 | 2026-09-12 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 1e276775-6ac2-312a-85ea-8a4a9e86b4eb | -8.8132 | -46.9495 | 2026-09-12 15:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2dcb2564-8b70-34f4-b0e4-195c5b846c9f | -6.2029 | -57.7193 | 2026-09-12 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c5453265-364f-3be6-845b-9ff22e73626f | -4.4654 | -55.4435 | 2026-09-12 15:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 268991f7-2c89-3562-85d1-47436353325d | -3.3504 | -59.4465 | 2026-09-12 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8d7c4b9f-e046-35f2-a6fe-3fbcfa84f5e2 | -10.8028 | -50.6326 | 2026-09-12 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0547d400-b075-3f50-916a-1dcfe1f224a1 | -10.7274 | -50.6192 | 2026-09-12 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 9ec84372-a619-3ddd-aec6-91c9dfc1b1b9 | -10.8223 | -50.5879 | 2026-09-12 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9b3cc5ef-d9ad-39cf-ba3d-d3b85a95c71c | -9.1524 | -51.6121 | 2026-09-12 16:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ad8c0f1e-e021-3136-9261-cfabccdbba58 | -5.1438 | -55.9741 | 2026-09-12 16:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| dece493d-14e9-3d73-8fa5-388b51ffeefe | -11.1029 | -50.8348 | 2026-09-12 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 3076b9c2-68f0-300e-8b03-6fbe8bf7fc68 | -9.1526 | -51.5911 | 2026-09-12 16:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 2c3f287d-2582-30bd-b6ad-5bb57126e59d | -10.5159 | -57.4593 | 2026-09-12 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 42faf05c-1629-39d4-ba8b-5e51f157cc7a | -3.3687 | -59.427 | 2026-09-12 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 08cb9777-2f12-3913-a0f2-292e582f2ced | -6.5131 | -58.2905 | 2026-09-12 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| e3fcff68-7cd2-3bd2-b5cc-a3278b258391 | -13.3761 | -51.698 | 2026-09-12 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 49ca585f-1f62-33f0-8baa-200afe76b367 | -3.4059 | -59.2155 | 2026-09-12 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 47a62e1b-3d6a-396a-86a2-17e4ca5be2df | -10.2206 | -50.373 | 2026-09-12 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 296.9 |
| d9571589-f3b7-3dd1-99c2-6f083c6b8974 | -2.7148 | -57.6274 | 2026-09-12 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |


[Clique aqui para ver as próximas entradas](README66.md)
