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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0891bc08-b251-303d-a548-c76891f4502f | -8.87926 | -44.79267 | 2025-08-03 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 80bf83fe-2280-3407-8afe-c9c0a3db65b1 | -8.41867 | -47.46393 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b24adbf-948c-38e5-8dc4-709a1447e62f | -12.42499 | -47.04296 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96e96f5c-717e-3988-b26f-c9ba04f0874d | -12.45241 | -44.85783 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| beb03fbe-11df-3b6f-8b2c-f5624a97d9b9 | -11.94892 | -44.96696 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f12ef062-16a7-3af5-9911-ce901385b1a8 | -12.67199 | -44.49206 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb10613e-bbf8-31b6-8fc3-1707ea78846e | -13.67838 | -41.36548 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bac755c1-6c25-3fbd-8b39-e4b53cfff2c7 | -12.46693 | -40.31388 | 2025-08-03 04:27:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d15de9ef-f3b3-352a-b8df-a2c3791899ec | -13.07647 | -47.42356 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0077109-9a54-3d75-b851-3d0ae5ce9a84 | -9.66638 | -45.75438 | 2025-08-03 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba419a31-48c5-3153-9435-46e3416b6158 | -11.77566 | -47.39535 | 2025-08-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ed2d8c4-c890-357e-a704-f9fb1608fdf3 | -7.88377 | -45.52843 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7276338-af75-3d25-87b8-0e6bdeffbdb2 | -13.69123 | -41.37223 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7878b091-27c0-38eb-bd49-6fa11e7954f7 | -8.72684 | -45.6583 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b62353-a714-351b-8b9b-f93852c1efc7 | -11.93655 | -44.95277 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd2b1fe6-9942-350c-bd7d-335d2797e139 | -13.52927 | -44.12296 | 2025-08-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5fbabad-b396-3757-bd81-860725e8a795 | -14.17364 | -45.45155 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34be6044-d55c-3e5a-a65b-41acdd815f52 | -11.75624 | -44.97349 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 10fcaeaa-bb2a-33dc-ad92-87894fb9e40f | -12.66278 | -44.53029 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fe6f160-95fe-3349-9378-8c74c8c4e678 | -7.96281 | -45.11156 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97eebbb8-bb39-3eb9-a5a7-8e6c33a21c00 | -12.67377 | -44.50555 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef6454f-aa3f-3cf0-9990-e552739c31c4 | -14.14065 | -45.42982 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47e58eda-cb6b-3bcd-a8ff-3dce5b841041 | -12.66533 | -44.48664 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3662cdb3-194f-3bd8-8a50-01df8b37ad2e | -12.65618 | -44.49852 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc6e7b53-2391-3e21-8bcf-e79242574ea8 | -12.62706 | -44.49411 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 110c9687-081b-3f0a-8864-c2cb6b26a9e6 | -12.66401 | -44.5217 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb8bf622-d1d0-3f89-9383-34c91551f293 | -12.63917 | -44.51355 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d11e991-868d-338e-a2e5-a17c83b8e09e | -12.6319 | -44.51244 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dbd1702-0b7f-318c-9eda-8c3c6d088277 | -15.16626 | -47.03207 | 2025-08-03 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1f676a6-843f-3200-b9a2-b1d17889c4d3 | -6.81724 | -59.26781 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bb583465-9b08-3283-a5aa-f6340c3249ec | -10.45927 | -48.81141 | 2025-08-03 04:27:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b521547-2da2-38b4-91bb-b6984969a146 | -11.94008 | -44.9534 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a14c0d97-142f-3537-a785-a73432f28a8f | -7.88487 | -45.5213 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fc122b0-267d-3e90-b819-571733af1b1d | -12.44175 | -44.8621 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef51a349-58af-31c7-9cdd-8fce9b0ecf4d | -12.44652 | -44.85443 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec572013-c8c1-3d6f-a961-7f607a0fa533 | -8.33478 | -46.91626 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c82d455c-0bca-3d3d-b978-a08e9ba94d6c | -7.59987 | -55.20465 | 2025-08-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98bec296-718d-3dac-ae55-dd340df3dec6 | -14.16128 | -45.43712 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7082f05-7352-3ce2-99de-639e7c795ff9 | -14.16951 | -45.4551 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b7ff60f-0a3f-3362-bacf-afd9f5778818 | -12.61857 | -44.50162 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c90f835-f1a4-3e2d-8ff0-dbfcfaa80016 | -12.49972 | -47.1749 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7954dcb4-1f6a-3cf7-af6d-66fba0f34f23 | -9.10646 | -48.90099 | 2025-08-03 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c7d0d92-ccda-3649-958c-3832e9fff83d | -10.48093 | -46.97615 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99df77b6-18ee-32f6-991c-8ef7b7f4cb76 | -11.75564 | -45.00181 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcbbc816-74df-3758-9c64-2548feb09d82 | -11.94309 | -46.72947 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d9b0c33-2081-339c-8929-fd3fa2282446 | -13.0787 | -47.43111 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f861c1b9-6d0a-30fd-8365-6cac5d4d281f | -12.67137 | -44.49637 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd0adb14-1052-34e2-a01c-e1973aeb0a07 | -13.08137 | -47.39178 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05ffa10c-e420-3ff2-818d-29cfff82fc75 | -12.64649 | -44.48824 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0d3b2de-4eb1-37ae-bebf-e46ea0bcbf3b | -11.7078 | -47.50321 | 2025-08-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4e8ff48-4e32-310d-8a59-f3de0fb036d3 | -12.44826 | -44.8614 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad7dfd7d-ecf7-3fbd-a262-ca703337c0d7 | -7.96391 | -45.10423 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b82ed42a-120d-36c3-877c-e0d9cbca24db | -11.15388 | -49.70053 | 2025-08-03 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14e67563-b1d1-37c7-84d9-4c3be711f56d | -13.68228 | -41.37082 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e99374f7-c060-3434-b944-5433fbe3e451 | -13.23715 | -47.24108 | 2025-08-03 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d386ad03-54fe-377a-bbc9-9569e443c452 | -13.0279 | -47.40851 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a79faea5-d3d8-3415-b90f-3abb8640371b | -8.94225 | -46.74923 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8250759e-769a-3bb2-8909-1f7af2857be1 | -12.63614 | -44.5087 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 458c4d25-3c38-3492-a70b-e31264989230 | -12.65921 | -44.50338 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f28e8775-094b-3038-9c08-092475ad00ed | -7.95721 | -45.1257 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e96d7afa-c06e-31e1-b8c0-3c4deeb13742 | -12.44587 | -44.85258 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e8e586c-0a78-39da-81ce-2cb76ea13975 | -11.20465 | -51.51268 | 2025-08-03 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65068add-486d-3a34-99c8-5c7d7a113b11 | -7.88602 | -45.53612 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d1a467-a746-3282-997d-63eae33d63cc | -12.68536 | -48.10148 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6d7f48b-3b02-3429-a98f-46d10cc13e68 | -9.40023 | -45.49781 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26c46539-6366-3483-b05e-5767a044585c | -12.66525 | -44.51309 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de2f9693-2dfe-35d5-9cfc-16ce8626767d | -11.7757 | -44.9916 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bfcf43e-0cec-3af8-9d65-7b0d0027b887 | -12.44471 | -44.86676 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eaa9f2b-fcd2-3993-802f-24a13edbb0fb | -14.14123 | -45.42573 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8deef829-1471-3e50-8b91-379b814e3f3e | -12.64526 | -44.49688 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10d84827-65d2-3721-894a-aa4b8ae29324 | -12.42986 | -44.86855 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 565a1ef9-84fd-3f7d-9e71-83bdb026c899 | -10.36767 | -48.10957 | 2025-08-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 974de87f-2954-33af-abb7-9e8d61570a96 | -14.17658 | -45.45617 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5305ad0d-650a-35ad-a8dd-3c8293cebdf0 | -7.96336 | -45.1079 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e75b6785-b78d-3d0b-b898-f51fcc46c8e6 | -10.47984 | -46.98315 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d70d971-7293-3d4a-be60-82c4f65b4cd3 | -14.17539 | -45.46434 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a65eb96-829d-310c-aa1a-736ce0b9ab31 | -8.37999 | -46.93048 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbdf7b46-0341-3f8b-8a52-78f599acbdf7 | -12.6222 | -44.50217 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6764a190-a3d9-38d9-94da-98bb2cb0cac5 | -9.39572 | -45.50462 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc8299b8-634c-3d37-ad49-76536c3ad7bf | -12.65612 | -44.52489 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ee9ee72-13c7-3980-ba38-853bff45bfa1 | -7.96509 | -45.11944 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74422e25-5ba5-3cd4-a000-07164f09b20e | -9.58638 | -43.84149 | 2025-08-03 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e05c0912-d3b6-39d3-b3d4-e26e32a91a89 | -13.03231 | -47.40195 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e6522b6-a61a-3ff6-99df-074e47e70629 | -14.17952 | -45.46078 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba3927c-142c-3922-b7cd-7570d8da796d | -7.96225 | -45.11523 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95427d10-30be-344f-9928-685bd18756a9 | -12.48808 | -47.16212 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 513769e0-46cd-3438-ab2e-8b896ee6bdd2 | -11.05346 | -49.54416 | 2025-08-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 363a8784-cce9-3a3b-8fac-1ab9477f974a | -8.59772 | -45.49855 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c11a997a-baaf-32b1-9d52-46f96710010e | -12.65976 | -44.52544 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d0b99e1-3f05-33d3-bccd-11fab4498202 | -12.66579 | -44.53514 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ac02025-5823-34a7-9498-84a2a02e26e1 | -14.14772 | -45.43089 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75adc606-c8d3-3779-8b9f-e405c16df11e | -12.61844 | -44.65885 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feb22366-e984-34d4-93bd-171d22b13581 | -8.93948 | -46.74523 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5912280-3103-39f9-93c8-d4ac49d0bc35 | -12.68647 | -48.0944 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4adb1e83-cae3-3f72-a860-96c56e7b61e0 | -14.3793 | -50.32649 | 2025-08-03 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea38b01d-d6bc-3101-8d7d-8f3c55e092aa | -7.96786 | -45.10109 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f862141-fed9-3c94-b41b-cfe8349360e6 | -11.93478 | -44.96492 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c64edc2a-126e-3885-9ec5-76021edf7fd8 | -8.34687 | -46.90395 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1763a1c1-e4ee-3ad4-abb9-ef1442c058fc | -13.06711 | -47.44009 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e55d4e1e-7be3-3d42-b2d0-2c45faccca12 | -11.05284 | -49.54796 | 2025-08-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README19.md)
