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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ca4b037-bb43-395d-9308-ea1868909a75 | -7.96935 | -45.64388 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f93ab9c-96db-35c5-b96c-e56e9a7b7b28 | -11.07436 | -49.74117 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9566143c-7ab7-3bc5-9253-d62d58bd3d9c | -11.15673 | -57.18539 | 2025-09-15 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a418d55-3426-3cc6-90b7-794888f9d624 | -11.08207 | -49.73653 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d44e7e6b-ac80-3f93-906a-caaf3fbe8ca0 | -11.86422 | -50.52206 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7e78cf7f-1529-3dfb-b714-fcb403e1048d | -8.10327 | -50.16066 | 2025-09-15 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03d2177b-ddf8-3624-9b24-3855c9f2eaa2 | -6.9714 | -44.55441 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8a943207-be68-3c21-b584-c752f7f816fe | -11.81333 | -50.43902 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ab605cc-4279-3ae0-9498-bddc98afe899 | -9.00456 | -47.04119 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11e01f67-fa99-3237-9853-80fd8468d8b0 | -10.98153 | -55.31144 | 2025-09-15 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d2c0edd-ee83-3f6d-9ac5-d1e1980f8ff3 | -10.13735 | -46.16241 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f120a6d6-1d4f-3ed9-b12e-15014a7ad3d0 | -9.01327 | -48.02843 | 2025-09-15 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 417319dd-bc3c-3338-906e-10e3460f53ad | -5.6998 | -49.1985 | 2025-09-15 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6431db9-b2bb-34da-b6fa-95c0d9aa31df | -7.88914 | -63.70326 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5166620-ac77-316a-a8dc-265fde917ee7 | -10.32493 | -58.72952 | 2025-09-15 05:10:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae3058f3-5fd8-353d-97b8-92c02f5558a2 | -5.69858 | -49.1964 | 2025-09-15 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3c4e12d-04e9-380a-9d44-6dfb6fc2725f | -10.16674 | -46.14817 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b141b7ac-38d5-37aa-9775-ae274e2f1418 | -9.73606 | -51.87871 | 2025-09-15 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 571d0ad5-1128-3900-a8dc-09ecf7a4f806 | -7.79496 | -66.91934 | 2025-09-15 05:10:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f395fb28-5889-3279-9b27-c3789ea7c7ce | -8.45359 | -64.14423 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c94eb94-a75b-3050-9868-1cdfc01d0feb | -7.88556 | -63.69847 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1d5017d-5ee5-3347-95a8-496cb98719d0 | -9.01375 | -48.02473 | 2025-09-15 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 341267d9-0beb-3b41-b78f-d7c4e7788806 | -9.68622 | -61.99681 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df89505d-15e9-3f85-9998-8117b0dc3b26 | -5.5774 | -51.97298 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b7f5573-fb22-3039-a3ce-356692b65e1b | -8.78555 | -46.04618 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dd5256e-efb3-33fe-9a42-adbe0bcf2c85 | -8.63751 | -45.69101 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 88ef1347-ce34-35ce-8ebc-40f0aef43038 | -7.80029 | -66.92033 | 2025-09-15 05:10:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87fc3f2e-6fb1-3775-a818-177a24f59bcc | -12.64995 | -47.94036 | 2025-09-15 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdd2928d-7919-3c28-9765-c1548daae152 | -11.31062 | -50.85625 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f52e717-432e-350b-b07a-0ace324744a5 | -5.84214 | -44.16668 | 2025-09-15 05:10:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa6b7e80-4726-3055-ba54-07f387a69f3d | -10.89203 | -45.44544 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2511c354-4d4a-3ee4-a56b-755fb96ed264 | -8.40876 | -47.22893 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8089d4b0-17d1-38a0-b047-b63ece43e944 | -9.68663 | -61.99852 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 942f3d12-1827-3570-8f3f-38e1fcc088a3 | -9.68997 | -61.99746 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3a136ae-328b-3356-9244-452fb26011b7 | -11.16401 | -57.18283 | 2025-09-15 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1deec28e-5e6b-3e94-93ed-14a08a39c88a | -5.57332 | -51.97234 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ae67cf-d7c5-34dc-b658-231fa6178e6f | -8.6269 | -46.37225 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5118d7de-6a31-3fe4-a0e7-f33d79ab2aae | -9.11761 | -61.48727 | 2025-09-15 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da9a2c20-255f-3ffb-91de-0b30e3a27ad4 | -8.43932 | -55.62922 | 2025-09-15 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c136338a-db01-31eb-828a-6029f0618806 | -10.13816 | -46.15591 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d8fbac31-be42-371c-874c-ca07c65684e8 | -8.64774 | -46.3675 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 417a2e24-2e59-3247-a6df-6a9b0bfe7279 | -11.79534 | -50.50013 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1393e702-2a60-3b9f-8785-4974068e5f92 | -7.6355 | -49.74146 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8b2ad3bc-8727-3c92-8283-a12f4578b592 | -8.09293 | -50.16474 | 2025-09-15 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 24734ecd-6677-3c6d-8838-57ca3379b757 | -11.00734 | -51.25085 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3935699c-c1e0-35ad-900e-01a0a9a47d7b | -7.43626 | -56.51463 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a09c1828-7b5c-3ba6-9dc5-b47765c0b829 | -8.98319 | -45.83257 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 185675f7-9a0e-3f4d-8f42-c12d2f92a020 | -11.07477 | -49.73807 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec2ee141-e5e9-3dee-a0aa-185ff33e46c2 | -10.92358 | -45.60732 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 170da9be-55b3-3e7f-a6d9-cd81a52d2516 | -6.55559 | -43.99315 | 2025-09-15 05:10:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a44fb7b-8876-377b-8cc5-195fb0d3b61b | -10.91745 | -45.6017 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e1b6f59-319e-3a9d-b505-a38e89f244ad | -10.34411 | -57.85467 | 2025-09-15 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a57756c-ef85-371f-b809-9c7eca7681ab | -6.20253 | -55.63055 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a079ca9-843c-3cd0-a44d-d9bc264a0184 | -10.98512 | -55.31199 | 2025-09-15 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0042dff1-8f38-30ed-8f9c-21361eeb2136 | -9.01044 | -49.77099 | 2025-09-15 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 778c5da1-8983-3279-b487-19ff6ea07ecf | -8.98385 | -45.8273 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aca1747f-d0bf-3091-a213-78f0fcfb2397 | -6.40628 | -46.94332 | 2025-09-15 05:10:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fe66e11-5691-381f-94e0-60030b46cebd | -8.96451 | -45.7719 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed94f663-e23d-32dd-b766-10fcfcc87f62 | -8.10811 | -50.16102 | 2025-09-15 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e194834c-49df-3e45-9ba3-caab8ccffa05 | -9.1208 | -46.94574 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4c997d1-fad7-3228-8a68-9327e3ece57e | -7.97504 | -45.65041 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04d2871b-de72-3f46-bd8a-4ed52cf5e221 | -8.62459 | -45.74323 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84a92241-536d-3850-9601-65a16e8d283d | -9.63922 | -58.94008 | 2025-09-15 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24c7852-aaf2-37f0-851b-a7a90c27a8ec | -7.6404 | -49.74218 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4251a09-9a57-39b9-bea3-800dcb85f717 | -7.63628 | -49.73594 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b0ce83a-953b-3323-bd97-663a85075aff | -11.79347 | -50.43637 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9b006bb8-165f-3c56-9641-cf7d2930c940 | -7.63137 | -49.73524 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 413e1d26-2640-36dc-b1eb-c4e860da08f4 | -8.92884 | -54.44482 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7ecf7a-2cd6-3a6c-914a-32c3b9bd0e47 | -5.85496 | -48.15904 | 2025-09-15 05:10:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3781263f-e40a-33ae-a983-e07320e4dec5 | -4.28396 | -56.33231 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13008885-9fe2-3096-b35b-c43bbb13e1d3 | -9.69334 | -62.00437 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea12384f-07e7-31e5-98d1-2d6d1aa150ad | -10.15211 | -46.14858 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01e55199-f83c-307f-9d13-b4d9c45c548e | -5.23246 | -56.04018 | 2025-09-15 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 358badb5-3648-3a51-b921-08618990c91f | -5.84355 | -44.16059 | 2025-09-15 05:10:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2af5988-ae7f-34c1-ab57-848201b784e1 | -10.66909 | -46.24349 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e475bdb-446c-355b-bb61-9015de688317 | -5.45048 | -55.71291 | 2025-09-15 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feda24d4-0376-3460-90fb-d2d39318787e | -10.87797 | -45.44838 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 147bfede-4746-388b-b9ee-e3d83cb2ceb2 | -9.11811 | -61.48917 | 2025-09-15 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b57002f-c15b-3dd6-a19e-377281ef0179 | -10.3408 | -57.85413 | 2025-09-15 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d469c84d-5970-3fdf-b491-bb549fc885b1 | -6.62892 | -51.00609 | 2025-09-15 05:10:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1a54342-6c3d-3ef7-b08a-dbb30cf7f0a7 | -9.13939 | -46.95803 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4748d48-d1a1-38bf-912e-78b872a8aa0b | -7.79435 | -66.92273 | 2025-09-15 05:10:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 641fb702-0635-36ca-9ec1-4dbc8c57b6f8 | -10.92487 | -45.59639 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e60edb9d-3c76-31ed-8ed3-b0b6d1360ac9 | -9.05573 | -47.02219 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ebe102a-f978-3b36-b2dd-572d71daaa52 | -11.72143 | -46.49211 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2709f45f-9ce9-395f-8d2d-640216cc8f65 | -5.63755 | -45.94747 | 2025-09-15 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcbb08fe-9ad6-3705-9322-5c68c32f9527 | -9.23561 | -45.66405 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fb4ac7a-3e65-3dc0-9b72-707360da9dbe | -10.39648 | -48.61039 | 2025-09-15 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50cacb6d-e6a9-3ef3-83e3-f9108408b814 | -11.78354 | -50.43504 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| eafd9df7-c3b2-341b-9efb-cb903a767575 | -10.14381 | -46.1629 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6271610-5816-35ca-a63b-f53c1b578686 | -11.43776 | -46.92661 | 2025-09-15 05:10:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d092ac-b4a2-302a-91f8-571c98b86128 | -7.6306 | -49.74075 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bfb95e60-630d-3c39-b2f0-a68f6cf2eb9a | -8.4216 | -47.22223 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36cac975-a866-3792-96e4-13a72a5a5d9a | -6.11177 | -55.58345 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 260254b9-a695-3553-9f3c-208e991d0e87 | -10.89442 | -45.44767 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bf0d06b-750b-3ee4-b979-ebf025e34b43 | -8.96317 | -45.78266 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3e814ea-de27-3948-8997-0e43886838eb | -7.9802 | -45.66763 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73298f02-0eba-3730-b482-fc799f3467c2 | -11.79704 | -46.65499 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d88a1209-a03d-32f0-9637-aeb9cea1eaf9 | -8.97736 | -45.82673 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fbbe1f8-ba46-3fb8-a5c4-8a9dc1105b14 | -7.97573 | -45.6452 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
