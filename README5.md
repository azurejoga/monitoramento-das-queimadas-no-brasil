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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8432254-5cf6-351e-90b2-a9b02e813900 | -6.63779 | -38.72121 | 2026-01-06 04:01:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 295914c6-58fa-3852-b5c5-58ab077dce9a | -2.52856 | -47.82789 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3da8b8e9-1528-3f76-95a3-e84dd55e889d | -5.87844 | -39.69352 | 2026-01-06 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8ee43cde-1f16-3a16-b5c9-8e76c98c415e | -8.43659 | -35.57738 | 2026-01-06 04:01:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9d82aad0-8027-3eb9-b982-940cd95caa74 | -9.67851 | -37.08778 | 2026-01-06 04:01:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83510dca-7bc6-3ddb-9410-3762b85bc384 | -6.43571 | -37.13625 | 2026-01-06 04:01:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a73e53e2-00b7-3919-a72f-e966d408c18b | -2.73444 | -47.62952 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2d73359-cd59-327f-aedf-3162f6fceb3d | -6.95907 | -46.2234 | 2026-01-06 04:01:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df1f58ea-4d38-3534-b783-36795976cd92 | -2.51825 | -47.82623 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e17b461-2000-3296-8443-afade2e5950d | -8.62125 | -35.62756 | 2026-01-06 04:01:00 | NOAA-21 | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 015a9de6-6bba-393c-9704-a72fc9a8b884 | -4.06791 | -42.53314 | 2026-01-06 04:01:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41919e4b-1051-3390-983a-b6cc6ed079ad | -9.94491 | -36.035 | 2026-01-06 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0518d95c-54a2-3bd5-8f7f-492709498ea7 | -2.79836 | -47.36425 | 2026-01-06 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8c1a43a-d7b7-3fc8-b9b0-99619e5b0d25 | -4.06433 | -42.53258 | 2026-01-06 04:01:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85a2788a-c662-3148-88f1-107b3a1f9986 | -5.90919 | -37.77253 | 2026-01-06 04:01:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e894e701-3ea5-3ad9-b3bd-c88060cf3646 | -6.33367 | -39.60996 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 08740e00-2cc3-3b1d-b81b-f34eda8043c0 | -2.53559 | -47.83012 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f133715-6c50-389a-93bd-e8a36ba2a1fc | -5.88876 | -40.06293 | 2026-01-06 04:01:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44f18729-7a9f-373d-9de8-ff65c3965be3 | -8.17228 | -34.98105 | 2026-01-06 04:01:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7086dc6f-ae54-36b4-957b-583a84934f76 | -5.8779 | -39.69697 | 2026-01-06 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23fb2ee1-400d-3b6b-a86b-0744fdac17a7 | -2.87933 | -52.57049 | 2026-01-06 04:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd2c08db-c2b6-33d1-bf71-02a393d3a033 | -9.77475 | -36.56268 | 2026-01-06 04:01:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e46ebbd-5d1c-3214-8d0f-beef3e2891a1 | -6.33313 | -39.61342 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf2e2748-c45c-3ee1-85c6-a62b4559b4ad | -6.8287 | -38.2277 | 2026-01-06 04:01:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c04a794c-cf6d-3ced-8c15-bcbbd6894bf0 | -6.80688 | -38.14034 | 2026-01-06 04:01:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61c40708-6415-37b8-821c-24bd29260349 | -2.16229 | -47.89624 | 2026-01-06 04:01:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79febee7-a848-3254-9ec5-7aa3d112a0c3 | -6.82941 | -41.32362 | 2026-01-06 04:01:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f56f76ac-c65b-38b0-b016-b9124870d515 | -4.55994 | -45.9375 | 2026-01-06 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d2d2dfe-9af7-3e3e-af25-6a7156089ebe | -9.71829 | -37.78331 | 2026-01-06 04:01:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd546132-3e41-3353-a929-baa328e88a1e | -4.11926 | -43.88973 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a8b1ef2-4d51-3cd9-a0c0-b30dca172a42 | -4.15349 | -43.65271 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 8400c21a-971a-34ff-a6ef-7f3e6d6a2b52 | -2.5337 | -47.8288 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dc84f79-d59e-37c7-894d-c653c168d40a | -4.06301 | -42.54072 | 2026-01-06 04:01:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8f97bfd9-c447-3933-80c5-f7631e426808 | -6.43632 | -37.13218 | 2026-01-06 04:01:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 20721f82-c39d-3f7d-a35d-5a623a6c51e0 | -9.50776 | -36.06924 | 2026-01-06 04:01:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 5bbf7b6a-e701-39f6-adfc-b27c94d0e20a | -6.58706 | -38.4547 | 2026-01-06 04:01:00 | NOAA-21 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2eae9730-559c-3ea1-841a-58f1ca6dd3c3 | -7.29239 | -35.17489 | 2026-01-06 04:01:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b128ce4b-fb3a-35ef-a383-e77e357c57c8 | -7.78069 | -35.19318 | 2026-01-06 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| efa19066-badd-3147-93f4-67899e29abbc | -4.06725 | -42.5372 | 2026-01-06 04:01:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1588b190-af63-3b4a-acf3-ac3e5f63ef78 | -9.50847 | -36.06415 | 2026-01-06 04:01:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 928d8e05-291e-3f26-a1e8-4a31e8f64d1f | -4.35573 | -40.72018 | 2026-01-06 04:01:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e26a8b93-31b2-30d6-8009-614944f1f0ef | -4.3515 | -46.32411 | 2026-01-06 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd9624b0-19a4-3c46-b3e5-41a7caeeaf59 | -6.5773 | -39.64139 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c4528a3-b9b2-322d-a8d4-13f183acbb65 | -6.49782 | -39.03481 | 2026-01-06 04:01:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f40b8b0-1693-39d5-84de-1bb845bf398b | -6.49448 | -39.03429 | 2026-01-06 04:01:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 707a95f7-def6-3751-a3ba-d6e31fea0595 | -3.707 | -46.9743 | 2026-01-06 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20a11a92-a5ce-37fc-9c72-35c2e7a91a0a | -3.79328 | -42.3925 | 2026-01-06 04:01:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ca28e353-dc04-3705-ab76-1932905a33d8 | -2.52478 | -47.83142 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 671c1c7e-ffe2-3df5-accc-68bdccfba9b1 | -6.50014 | -39.5471 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| edbf4bdf-1f6f-3039-8e7e-86baf06e3cf1 | -3.18347 | -51.0878 | 2026-01-06 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89c2b229-3042-3630-a629-fa219759deef | -2.80333 | -47.36509 | 2026-01-06 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20d94dcc-5ace-3299-a967-91fb24478e1c | -5.40038 | -46.53491 | 2026-01-06 04:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee80eaa4-732e-3012-8b92-8b9f5e03290f | -2.98554 | -48.58797 | 2026-01-06 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58434f04-52ea-3e17-9dcd-f78d89821bb5 | -2.64693 | -45.65089 | 2026-01-06 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7414e7ca-3c53-3dfb-830e-4a521c391b54 | -10.68227 | -40.40138 | 2026-01-06 04:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8cf4399-4d90-31bb-ba15-d4417d2002a0 | -7.78483 | -35.19106 | 2026-01-06 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| afdbf224-2d1b-3c4c-8501-1b5ec3cef986 | -4.56431 | -45.93828 | 2026-01-06 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eeee157-3568-3d35-8ebb-bc5bb59d1c5f | -4.5829 | -38.36203 | 2026-01-06 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c54e4c05-4cd8-343b-95a5-4edc0598a85a | -6.33697 | -39.61048 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 601d2459-a496-3361-979e-7337c8fae6df | -10.68173 | -40.40488 | 2026-01-06 04:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d3a32fe9-5bcd-3240-a884-c8a184cb9288 | -3.71817 | -47.20746 | 2026-01-06 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 403f8383-4f40-31a1-8d84-fefc967f7544 | -2.67119 | -49.85556 | 2026-01-06 04:01:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0480246-9800-3a2c-a2fc-05772ab0f293 | -3.72222 | -47.20576 | 2026-01-06 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e70ed5f-57fa-3a60-8d9b-67cd1028bbbc | -9.94243 | -36.03315 | 2026-01-06 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 170d245c-5a2f-3734-a786-655198e75d18 | -10.24915 | -37.27038 | 2026-01-06 04:01:00 | NOAA-21 | CUMBE | SERGIPE | Brasil | 2801900 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| efd364f6-9bf2-3b32-8ab5-f3f423f4fdd7 | -10.14329 | -36.41905 | 2026-01-06 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 812634b8-d894-3476-afb4-cc0ed336abf4 | -2.5253 | -47.82834 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 905e820a-f1e5-3fc5-9c25-d7bae391559c | -5.27156 | -40.46056 | 2026-01-06 04:01:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc39a3ff-a9b0-31e3-a036-d6ae709ee3c5 | -5.48419 | -45.43551 | 2026-01-06 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aefcac2-ef5b-3b16-86a0-0bc02048da45 | -5.15946 | -37.67624 | 2026-01-06 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c1564889-66cb-37ae-a0fd-d52c19525c23 | -3.72301 | -47.20825 | 2026-01-06 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5c2e0b7-9a96-3caf-a571-e30b563510bf | -3.32855 | -50.2304 | 2026-01-06 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11aa1bd5-70f5-33f3-860f-7db4da54f70b | -10.68504 | -40.40544 | 2026-01-06 04:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 92f7a037-87fc-3855-9451-3097802936a1 | -4.93838 | -37.79239 | 2026-01-06 04:01:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5edfd324-6816-3f14-a834-63bedf679379 | -5.66402 | -46.23014 | 2026-01-06 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ca41397-6760-379d-8308-2260e3112f40 | -2.36647 | -47.67578 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dff0917a-785a-3c40-9b8e-7b681f1fc916 | -5.23991 | -38.13474 | 2026-01-06 04:01:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fbe553fa-6435-3e40-a121-9956e007390b | -6.96337 | -46.22407 | 2026-01-06 04:01:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4f623bfd-ff13-3139-a624-86ff4a20c0ed | -6.6406 | -38.72533 | 2026-01-06 04:01:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 285e66a8-d483-3824-8108-e10a598ac6b2 | -10.68558 | -40.40193 | 2026-01-06 04:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3f7bfccb-920b-3e2e-b786-a658c659eabe | -5.48795 | -45.4128 | 2026-01-06 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 848060c3-1625-369a-b5b5-d44436d3aea4 | -3.26189 | -42.54501 | 2026-01-06 04:01:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d8d2483-377b-3259-81a8-4ea5738dd31d | -7.78077 | -35.19044 | 2026-01-06 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b09633a5-1623-3946-b5c3-b707193d3e69 | -3.26123 | -42.54919 | 2026-01-06 04:01:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 686b6e61-28bf-3863-99b2-690fd580a581 | -2.52806 | -47.83098 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b06db36-fffe-34f4-ba49-77b8ce146353 | -6.96406 | -46.22001 | 2026-01-06 04:01:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5b4427f-10d1-379a-ac8f-3ab7382c8b85 | -3.25827 | -42.54446 | 2026-01-06 04:01:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e1946806-54b2-3f0c-b17e-44e4ad6fcc6c | -10.99088 | -37.51672 | 2026-01-06 04:01:00 | NOAA-21 | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b23858d7-cbad-3369-921c-5eab2fa61bf4 | -5.20575 | -40.59641 | 2026-01-06 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 69d39615-45f5-3541-9f5f-0fe592ead371 | -7.43757 | -34.85891 | 2026-01-06 04:01:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6b497e66-3ac0-316a-b437-1cf4ee1a8deb | -5.73523 | -46.53228 | 2026-01-06 04:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f1a09e4-8a6a-3a28-be69-c618dfb3d7af | -4.06499 | -42.52851 | 2026-01-06 04:01:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e0f226bf-14dd-33a2-af56-69ef9a8b179c | -5.41707 | -38.57383 | 2026-01-06 04:01:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6be2ee72-819e-3277-829c-a66a61f169cf | -3.48063 | -47.68827 | 2026-01-06 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 968040c2-3dd3-35cd-92a7-eb7f0133f42a | -2.85708 | -45.25243 | 2026-01-06 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fd10a68-82c3-36cf-a11f-232672b445c0 | -4.93439 | -37.79557 | 2026-01-06 04:01:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e63bbae8-472f-3594-86fb-1b5a84a74ac0 | -4.12388 | -43.88558 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a2c483f-cf77-3a19-b32e-873af704a8e4 | -2.52341 | -47.82703 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab4fa30-15ca-3714-a178-cf818ab50b14 | -3.92972 | -40.53073 | 2026-01-06 04:01:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b6cbfd0-6222-34bc-9d99-1c6fc74113ab | -2.16178 | -47.8994 | 2026-01-06 04:01:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
