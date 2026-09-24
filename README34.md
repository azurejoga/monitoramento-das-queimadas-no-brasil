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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d6c174-8b56-39ee-9a14-3047c4b47c19 | -6.12401 | -44.59822 | 2026-09-24 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98753d9c-6dc9-3199-b1a5-d3b544885aa5 | -2.3919 | -48.52001 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aef642a8-97b5-3dc8-8ffa-5caa86bbcc47 | -5.22948 | -49.22748 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d061ded9-bb65-3c8f-a539-6151252979d4 | -5.83488 | -53.85453 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbcd2782-8965-34e7-84dc-e510b01f0a89 | -6.51835 | -52.82722 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c93d99c7-7886-38cd-a1d9-3f3dfe5e6892 | -6.68432 | -55.05322 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d94605ea-10e1-3721-ad8a-f4b90ba56166 | -7.4074 | -42.63593 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aab1f274-b805-3ba2-8bb1-1c7e5b091216 | -2.96808 | -52.14982 | 2026-09-24 04:08:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28af70c7-7ff5-3378-9ab1-b4ddabe37544 | -5.32285 | -43.41844 | 2026-09-24 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 46cc06ac-5ae8-3603-8722-663cb450aefa | -5.77538 | -45.10417 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 26e49b61-5f2f-33b9-82bb-458dcba03fe4 | -8.22984 | -48.20889 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91d5f099-bcaf-38f5-a7d1-a32c3bc152a6 | -4.35113 | -47.76468 | 2026-09-24 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| effffeeb-1100-325a-b48d-5f42a94fa8d2 | -5.57778 | -42.30559 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3f378caf-b1f4-387f-9e35-aebe4afd36db | -6.57864 | -44.14806 | 2026-09-24 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfb2e719-6878-305c-90a2-644bed02f2e7 | -7.42865 | -49.86738 | 2026-09-24 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dafc0b28-a088-3ce9-9909-f2215628ef0b | -8.28573 | -48.21844 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1eb0600-7436-3719-a083-7ec84817d329 | -7.40332 | -40.58228 | 2026-09-24 04:08:00 | NOAA-21 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b75bc76-2b6d-355f-8e57-0dc990ff4919 | -5.60029 | -45.95781 | 2026-09-24 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e733d26-e9c5-3ce5-ad48-a2e4001c8829 | -4.76006 | -42.7408 | 2026-09-24 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4c15bcc-7f3a-32e4-9452-4d033be3b0dd | -8.90532 | -45.91124 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b650d2-8184-309d-93c1-2e6fc31df7fb | -2.16901 | -48.32157 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e601097c-4ebd-367b-b899-6b4ebc33fb08 | -3.17643 | -48.02321 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1da8cb6a-8059-31ba-a4c7-f79cbdc3978d | -7.34981 | -39.30874 | 2026-09-24 04:08:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58eff479-f39a-3f99-a665-d48ec945e5d2 | -4.42175 | -55.07264 | 2026-09-24 04:08:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20e181fe-b8aa-31c3-8355-83dc0984bf6c | -8.14065 | -46.81955 | 2026-09-24 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f343d9a-b884-36df-ba29-b5a02b3b58e8 | -7.67543 | -45.48979 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef0c24db-e691-3ccb-846f-3d8236d88d87 | -8.2636 | -54.7747 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bcf1c76e-3ea1-3045-850d-0b188dce39cb | -7.35278 | -42.05436 | 2026-09-24 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb89bccd-900b-3f44-be2c-f3d02d57e641 | -4.11564 | -51.08299 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 354d1b89-79f5-3e98-9baa-25ba2219ab98 | -8.35602 | -45.62048 | 2026-09-24 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffe886a3-c48f-3472-a004-95c1b177e84f | -8.82341 | -45.92495 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a921772f-ffe3-3f09-bb37-fad065d29b0c | -1.19729 | -54.14867 | 2026-09-24 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a5f4aff-99d3-3091-9961-ae41dc79c04e | -7.40613 | -40.58637 | 2026-09-24 04:08:00 | NOAA-21 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9d113ceb-97fd-3179-aaef-a643643c9a24 | -9.15183 | -49.95741 | 2026-09-24 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ef25f1b-62b1-3440-be11-f8a44c45309d | -5.92199 | -42.98935 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3d37fe20-3b33-3657-8fa7-ab3f3f93d868 | -8.90604 | -45.90683 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dc8092e-2bb3-3ee3-89f3-400755d0a884 | -3.45189 | -50.08706 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6ffb621-f88e-38b3-8930-9dc2a3484b4e | -7.42784 | -42.63558 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6b9b9cd-0505-3ebb-a55b-f76ff73da22f | -5.98814 | -44.42885 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 268028a2-2380-3a35-8958-6a2670bafe76 | -7.50637 | -39.27588 | 2026-09-24 04:08:00 | NOAA-21 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71a7e6c1-ae4f-3ce1-a9cd-fbe6c5044006 | -6.32112 | -43.04548 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddfc49ac-6f7a-3d14-afe4-f849d7c8bc0e | -2.64893 | -54.68625 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| f47592d5-5b95-3648-a1d1-f222f879ebdb | -5.98809 | -44.42793 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 726cbadd-d4d4-300f-8ced-d1191a4497c2 | -4.7567 | -42.74027 | 2026-09-24 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c674393-f648-39b3-8127-a689b26713eb | -6.61056 | -43.73453 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb02f404-864d-378e-aebd-392c604fb7df | -6.46685 | -54.99786 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e4a7578-2fa5-35e5-a1a6-a80a3c870607 | -3.44606 | -50.08938 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b0d725fc-9a2f-32e2-8646-8e93c9906898 | -6.6855 | -55.04693 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46e25751-27cf-3bdd-97a8-edae423cde2d | -6.97514 | -45.04848 | 2026-09-24 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35f1aeeb-5ef7-3bfc-adec-4303e6bc6af8 | -8.92388 | -45.95319 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4714e51-f655-380a-b095-5b31cdfcd37d | -4.6755 | -45.97604 | 2026-09-24 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 622b4e0d-cfdb-3e20-8407-2e6472592052 | -7.78407 | -50.22424 | 2026-09-24 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 821adb5c-c22b-380b-8410-ad59e23f478f | -2.89302 | -54.09887 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad7efcd5-236c-3d9c-a626-32d5ec60e665 | -3.42011 | -54.00028 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b77256ad-6e65-3fb6-b0ba-3cf1ccce94b4 | -9.26385 | -46.23979 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6f25389c-e488-3da5-a967-55d883b14513 | -3.23064 | -54.3247 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b121f3fe-f749-3408-bcb4-efaa5caa1a61 | -3.76217 | -47.50422 | 2026-09-24 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a26c6fa4-765e-3de8-b104-9b71792d9402 | -4.28428 | -48.61443 | 2026-09-24 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4289085-d88b-3b21-bb82-0c0d0908e67e | -6.53303 | -51.50658 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cba940a-dba1-32ac-bfaf-06868d8943ef | -7.32781 | -46.74387 | 2026-09-24 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4ad1526a-54fc-3f6a-9ffb-8b3fe8f76448 | -3.3588 | -43.24568 | 2026-09-24 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 844dd820-d59c-3463-96c4-d496c77af437 | -5.77611 | -45.0998 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bddd725c-6a3b-37d0-bee7-1ed96d68a560 | -6.19928 | -47.50064 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c77fd2c-e426-35f5-b6a1-41e2d4b7c8b5 | -9.26311 | -46.24433 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 481d65fb-8ee9-3e20-93af-09cd1035e8d7 | -11.9906 | -52.4695 | 2026-09-24 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 71107877-6e5b-31ef-ba03-3d2172060896 | -7.8996 | -61.1772 | 2026-09-24 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 9bed0f55-afac-3786-866d-dd594823296b | -11.9908 | -52.4485 | 2026-09-24 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 93ed92bf-f865-3ff4-bcd9-fd0568b71649 | -5.1058 | -60.2639 | 2026-09-24 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8e7a79b4-fa22-3870-b03d-a279c28f6b80 | -6.6146 | -59.9272 | 2026-09-24 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2f8f63ee-5986-3208-a970-d71909fc48b4 | -12.0099 | -52.4465 | 2026-09-24 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c8161db8-1c13-3671-bec8-dd2955c2c850 | -12.0096 | -52.4675 | 2026-09-24 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| fe3e08bf-64c2-3026-9a86-90361e2feb23 | -10.1098 | -50.1921 | 2026-09-24 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| ced48059-1054-3d6c-a830-b6f07e337286 | -12.13 | -50.7407 | 2026-09-24 04:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f4afc187-04ab-38cb-98cb-7137b1762daf | -10.07841 | -46.05685 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b377422-a7c3-3bf9-b1a8-b2ad9720fe49 | -11.41019 | -47.39196 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3939c33-117f-31b9-9523-3f13749f205d | -14.72771 | -45.60001 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f140c51d-6f18-39bd-aa13-ce21af70fbc1 | -14.62526 | -50.60485 | 2026-09-24 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af3ae6ca-85a5-3e63-8886-02be145de5dd | -10.61357 | -54.00198 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c67af2-6a0d-30e8-8143-d2a9cf027a78 | -11.41509 | -47.36356 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b0b7c84-87d1-33cf-be35-d648fd71a081 | -13.82359 | -51.85638 | 2026-09-24 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cb596d5-cab8-3f47-b231-8752f79092ae | -10.94273 | -43.83989 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca76ab17-026b-3125-ae5d-554474660731 | -11.47061 | -47.38859 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4ce33f8-ffdf-34e2-982d-b04fa7eb5a70 | -10.84947 | -43.24739 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1532a43-478d-305e-a189-2cee32ac157d | -11.41709 | -47.39825 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d998a206-b6b1-34f8-b863-fcb5a1f3771d | -10.97745 | -54.0918 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75023a0f-ac79-3e57-a069-9219b8bd4904 | -11.23782 | -51.39012 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4beda1a-2203-3988-b68e-4b28faf500c4 | -10.27161 | -49.96608 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f87c1171-8d19-39d5-bca8-d42f6d35df50 | -12.13836 | -47.3643 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6bdb2e70-f811-38c3-840b-d1e63c1d5f5d | -10.71861 | -48.72611 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41fb7325-7faa-3382-973c-d47757c2c478 | -10.41853 | -49.36343 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8137c55d-0cdc-3033-b3bc-930f3d20b057 | -10.27619 | -49.95428 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76305a4b-f9b4-3c50-b1ef-1e030ae6b815 | -10.61268 | -54.00667 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00c21111-d253-3d39-baf7-0c10e4ed4c74 | -11.24118 | -51.40009 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 816d0834-7a97-3a32-8095-869c19e8f7a5 | -10.26785 | -49.96029 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49c961a9-8ccb-3c96-b111-32d44f41d4e9 | -12.05154 | -50.28896 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78b8d559-21cb-3da8-83df-00efcdd4d3c1 | -10.10673 | -50.19213 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e0d4426a-e42e-3005-aeb1-cc5afc35ad2d | -13.85126 | -48.57287 | 2026-09-24 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e802f837-00a9-396a-ae1c-ab8083c76092 | -11.42097 | -47.3989 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d8b3974-1ce5-3d30-b313-2510c31e637f | -14.71531 | -45.58995 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1db506a1-c3e9-32d2-a873-eb3d285647ec | -10.08421 | -46.02297 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README35.md)
