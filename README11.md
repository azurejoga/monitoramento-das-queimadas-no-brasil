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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90c0fa93-d55e-3610-9984-6676b2694fa1 | -6.98698 | -44.54672 | 2025-09-14 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de7a860b-8efa-312c-b1f6-fee55ad83331 | -3.79328 | -47.58065 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93de7aa1-96d6-30b2-a229-e0acbc85ed64 | -2.25393 | -47.85261 | 2025-09-14 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a96890b-7276-3927-8953-9db80984c2fb | -7.37943 | -44.35091 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44e6752c-f7f8-3e43-979d-03237f1cbd5f | -8.95752 | -44.44738 | 2025-09-14 03:47:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a395f648-b4a6-331f-8f86-6d6ffa38669c | -3.60074 | -47.52286 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3b5467b0-02b3-3890-b896-4cf71ede6a5a | -7.37673 | -44.34692 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c068b1fa-a536-3bc9-917b-717bd31df093 | -3.79102 | -47.5866 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5739aaf1-98d5-3327-9fbe-23483419fd67 | -3.31561 | -44.18037 | 2025-09-14 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e4e7dac-6548-37f4-ab22-f118554fde45 | -7.47731 | -46.12691 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7689a6f-90a7-3187-b3a9-7542b4708401 | -10.75926 | -44.78567 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 102c14f9-1392-3ec9-be2f-0484444b32fe | -6.9879 | -44.54141 | 2025-09-14 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc68e3ec-15c2-333a-9568-373b38fd1dcb | -7.61069 | -46.71654 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 394a0417-15bb-3495-a357-492ce43455b6 | -10.76105 | -44.77557 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db9d3203-4d4c-3c25-a93b-580894738fbf | -3.59008 | -47.5112 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1100431-91c7-32ab-a283-2a22af68d6e0 | -7.37563 | -44.34481 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a54b9975-8f40-3b10-a3a7-af6d15520cb9 | -10.75467 | -44.7849 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4906a6ca-0dec-3c39-9fd9-3a8179a100de | -7.51117 | -44.67154 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 594e36c3-88cc-3915-91bd-7d4374764b0a | -8.08401 | -44.51604 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e164ca5-71f0-3328-a9a5-2288a2f33c20 | -6.99268 | -44.54236 | 2025-09-14 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf8f43f2-549b-3118-bd1e-9d2641877320 | -9.85782 | -43.13844 | 2025-09-14 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 53c89518-0069-39be-a18c-324d1246fa98 | -9.01802 | -40.34815 | 2025-09-14 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94c1edb2-163f-3c12-81a0-893e472dce3b | -9.06299 | -47.0323 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cc044e1-4865-33f0-9a69-3206b7cc0bf0 | -7.37578 | -44.35223 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cd45e8ee-436b-345f-b6e0-9ab6ee76f555 | -9.11371 | -46.9442 | 2025-09-14 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e93a3da2-1153-3fdb-b068-39855104dd94 | -4.79899 | -42.74377 | 2025-09-14 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f04999d1-2153-34a1-bb7e-cb73b71dbe10 | -7.92604 | -39.84799 | 2025-09-14 03:47:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a570fad-8978-3eee-86d2-9914eb5fa31b | -7.61617 | -46.71758 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a50bea07-adba-349a-830d-6efdbb252f0d | -8.35127 | -44.73347 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d46f0433-64a8-3388-bc13-ead1c433a027 | -7.37382 | -44.35539 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d9cb765-706e-33b1-8d13-45ecc19b64ee | -7.37956 | -44.35823 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dba968d-79c5-3777-bee6-84aae8ad3f21 | -2.25483 | -47.84731 | 2025-09-14 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df4d991b-2305-3d81-8239-e929f46578ec | -7.30835 | -43.93807 | 2025-09-14 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afbf8add-87ba-341d-818a-0ea0349644d6 | -3.89638 | -38.39464 | 2025-09-14 03:47:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cbb9ef68-b5fb-3b8d-b05d-c8a357b9e25a | -7.51989 | -44.36981 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c6bfe5f-dfb4-3f87-ad85-881d4fb1c2f7 | -3.59757 | -47.51072 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7b5d344c-e1da-3fbf-a137-32160a7bd42e | -9.73831 | -46.04982 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 146acdfe-65a9-3265-98b4-f76d3d3dedd3 | -7.60583 | -46.71252 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77956776-6d16-3e87-a347-65424e4ccf48 | -9.74558 | -46.86905 | 2025-09-14 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 159a2a18-9bd3-344e-9fa5-994941663d67 | -9.74763 | -46.87291 | 2025-09-14 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6205e29-3d5e-34ec-95f9-1b243b0d0ee6 | -3.22199 | -47.13049 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bacb320-921f-3760-89ff-db303a3bfd17 | -8.17349 | -46.77536 | 2025-09-14 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4afb1ac1-aaa7-365b-8dd8-b2a7793c38ee | -7.52367 | -47.63928 | 2025-09-14 03:47:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5eab0db2-3bea-3ab0-b873-09e8725241bc | -10.77016 | -44.77742 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 520f5c14-60eb-3b7c-ab27-1e6ac55d27f2 | -4.0449 | -43.34853 | 2025-09-14 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb18086-9d0a-3922-bba3-3d816c0e4d5a | -10.75556 | -44.77989 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22acda00-d366-320d-b92c-00c486cdf396 | -7.37854 | -44.35616 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3718c0b3-d0e0-35b6-916d-5ad8855e37e5 | -3.5898 | -47.51914 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a8eb0a02-067a-3e7e-82fb-c55b50d63cc3 | -7.37385 | -44.3359 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68548533-6aef-3e79-917f-e169db30171d | -9.73942 | -46.04375 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bcf980b8-0e64-3dce-8a5b-dfcb3be06885 | -8.98765 | -45.78488 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb3e5039-f188-33f7-a914-eed2bb90f1e5 | -7.3765 | -44.3397 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 635093fd-8071-3691-86a0-3effe9005785 | -3.5937 | -47.52674 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2cabe18b-d09e-3963-aedd-69c482ff613f | -8.08486 | -44.51114 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a3efe28-f614-3a7f-8dbb-994c11eddfc0 | -9.63365 | -40.61522 | 2025-09-14 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 394af6f6-b1ca-3118-8a21-e55120003de7 | -8.94913 | -44.44099 | 2025-09-14 03:47:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e671cb9b-a8d1-3d21-b0d4-109cb79ff370 | -10.59561 | -44.32904 | 2025-09-14 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb7253b1-814d-386f-b322-f89bbdc53b8c | -8.13633 | -43.66705 | 2025-09-14 03:47:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a542a819-f7e9-30bd-9668-d5c7ce8ab5f7 | -8.98263 | -45.78382 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 945b88ed-a645-3ffb-a1b0-707f154dc9fe | -8.94942 | -46.05046 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3eab31c-36aa-3b4a-a641-494805345820 | -7.92591 | -39.84685 | 2025-09-14 03:47:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 846a7c89-8f99-34bd-b569-04151fc63017 | -3.59061 | -47.51438 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ced5699e-7707-3965-b452-c9fa75a02004 | -3.79718 | -47.58774 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8da2fc1-1405-32e1-b071-eedb837bac66 | -8.98477 | -45.7722 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 794e192c-573e-343e-a12c-d7fbacde6482 | -7.56516 | -44.38811 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d3ad98e-8d2e-37b3-9f03-b616edc53e9a | -6.88401 | -45.63699 | 2025-09-14 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92600610-8608-3def-8add-f79e4f45970c | -3.90527 | -38.36105 | 2025-09-14 03:47:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ecda337-6ea8-311c-a725-dcfc24283cb3 | -8.50058 | -44.72711 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8d54d00-e8b0-3f32-8485-22059a2d11cb | -8.68022 | -47.10692 | 2025-09-14 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3d2f36f-91cf-3af2-bc43-28488950cb2d | -11.09354 | -38.52559 | 2025-09-14 03:47:00 | NOAA-20 | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ab62ff97-2afc-3fa8-8f64-599bd3a3153b | -5.19246 | -38.90027 | 2025-09-14 03:47:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 737d4c28-9d13-382c-99e6-3b78c8258f02 | -3.22057 | -47.13298 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a0efc8da-1012-30df-9c71-d20c7a97eedb | -7.3718 | -44.33887 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e5d74f0-3367-3229-a7ca-c2638308d98c | -9.8555 | -46.47266 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 225af9be-a7a5-3f94-9a94-d285d5d3c877 | -10.13105 | -47.19004 | 2025-09-14 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c942702b-600c-395f-9cad-0946f969a1af | -6.8794 | -45.63286 | 2025-09-14 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb57297c-3afd-33a2-8703-a7fb138c0b1f | -6.99084 | -44.55302 | 2025-09-14 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0fd164e-465d-393e-b48c-46b5d948b152 | -7.92958 | -39.84856 | 2025-09-14 03:47:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a50cf892-3107-3b0f-b2f0-cf35bbec1500 | -5.66289 | -37.21663 | 2025-09-14 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cdcf76b5-6cc5-3012-8105-cc6a6da84959 | -8.19561 | -46.99181 | 2025-09-14 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c213ae97-bc39-338c-a3bf-28d4cbb42528 | -7.61069 | -46.71715 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10b6398b-c618-31de-8ef8-b348c221c4e8 | -7.30669 | -43.94771 | 2025-09-14 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42a9be26-a220-3ea7-ac79-802fbd486640 | -10.76471 | -44.78156 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4474d81c-8aef-3794-8bdb-ce3479e7c5a6 | -7.519 | -44.37484 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98ce7db9-5f45-3192-9eb8-2f56ffe25cb8 | -8.9898 | -45.77315 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f697733b-0a07-3042-8dd8-c9e3e148478e | -7.61683 | -46.714 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7f421c8-abc4-3ca0-a9c4-755703a24217 | -3.59541 | -47.51704 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| bb3c7a52-0075-3386-8301-6d27dc163763 | -5.66233 | -37.2201 | 2025-09-14 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| dd96e92a-791d-3b17-8b56-00962df37514 | -8.17964 | -46.77257 | 2025-09-14 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6051f975-c9dc-3ce7-8930-3a83db674cca | -9.85848 | -43.13461 | 2025-09-14 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2c44e61-4f94-36ad-9da1-582f5eb33aae | -3.96815 | -38.51498 | 2025-09-14 03:47:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8ac0a3c9-519c-3fb9-b9f3-a3c50bc90295 | -10.59845 | -44.33887 | 2025-09-14 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b10301cd-3b98-36f8-8036-92b0ced157d9 | -3.79798 | -47.58324 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc0a447f-1df5-32dc-9133-13d46588747c | -7.61749 | -46.71041 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab0e39fe-a9c5-3d48-9b88-61848dbf7b6d | -9.63296 | -40.61941 | 2025-09-14 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 55.8 |
| e704dce7-d55b-3171-a62e-be4cdbebedbc | -3.58924 | -47.51596 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 606b84f0-80d9-3d78-9dba-8344623fbbcc | -9.49342 | -46.41222 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a0c03cf-3678-3647-86b5-b5e4d3ff7ff5 | -8.17283 | -46.77893 | 2025-09-14 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3959003-7617-3709-ac65-354d2d7f0409 | -10.1307 | -46.15606 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c551df26-6134-3924-add3-d6a2b1439db5 | -3.22134 | -47.12841 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README12.md)
