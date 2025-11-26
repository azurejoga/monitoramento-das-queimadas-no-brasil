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
| c6c6c1f5-5d42-3620-9262-2e668624ce10 | -4.45339 | -44.30486 | 2025-11-26 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 68de1cf2-e8c1-32c0-85e3-2e95d6107acc | -5.60247 | -35.63876 | 2025-11-26 03:57:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 12c8c80a-c35c-33e9-a77b-649c72dfaf52 | -4.41241 | -42.91485 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65e609f8-7f73-31a5-a599-52ed1dc625d5 | -4.44489 | -48.75678 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc8deb7e-899b-35ce-aedd-0f2bdce7fcdd | -4.9429 | -41.15088 | 2025-11-26 03:57:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27710382-e626-3bbf-a17a-4fb267c5a8b5 | -5.75433 | -45.11206 | 2025-11-26 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d93656e5-db9e-3b62-aea0-c1367c758631 | -4.70733 | -43.99673 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a661af2c-dfa7-346c-8b95-2d16ea55f111 | -3.39126 | -47.18549 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cf53883-eeec-3393-be08-461a9b644d53 | -2.69993 | -47.40972 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0324888-df87-3beb-bd3b-1825ce5875bd | -3.67416 | -43.57146 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| facba17a-47b9-3755-acc9-aa5c92c4f77b | -2.49434 | -47.8221 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc5da629-6047-3ccf-9dce-27688dc725c3 | -4.44412 | -48.76131 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b9ddc41-1dad-3b22-8ebd-d0910568b3c5 | -3.39767 | -49.51993 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7258666-717b-3e87-8578-3884954dc651 | -2.54678 | -45.39383 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0d4239c7-afac-317a-9231-8d82ddc0724c | -6.85789 | -39.36258 | 2025-11-26 03:57:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0012a939-76ab-3569-97d9-f21330ef1bdc | -6.76338 | -46.51381 | 2025-11-26 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 273a3876-f448-3676-88f8-9fd948f061be | -4.91035 | -43.79778 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5575c3c5-7980-3fb4-8c7b-c0ddca8ce40d | -4.16686 | -43.7258 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 515fe36b-82fa-3ec9-ae0a-36dbfdb39b43 | -6.52043 | -38.98933 | 2025-11-26 03:57:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 143b9e0c-031c-3468-99ee-1673997ff112 | -2.49296 | -47.83027 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dfbf9de3-77b5-33b0-8354-628a38909b4e | -6.95735 | -39.13777 | 2025-11-26 03:57:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 97fc8e81-87e5-36c4-ab54-80cf75c9545f | -4.17359 | -49.88017 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 730d9794-2c88-3934-818f-b051a4517637 | -4.51754 | -37.74888 | 2025-11-26 03:57:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 21acd023-1682-35a8-9128-d644c77000d7 | -5.4838 | -37.78017 | 2025-11-26 03:57:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 351536fd-d19c-30d4-b2d5-6e6a9737194f | -7.68233 | -37.10035 | 2025-11-26 03:57:00 | NPP-375D | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ec5cabe4-680f-319a-8bb9-7e4edeb72beb | -4.56861 | -43.8008 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1ca7d01-5c08-349f-ba92-72ee97c97d63 | -4.65157 | -43.97528 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10d639ab-02a2-3a37-825d-6c837205857d | -4.72406 | -46.46416 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da0cf6ff-3434-33af-97b4-3ebdae1e3968 | -4.40266 | -42.12358 | 2025-11-26 03:57:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90f54e8f-86aa-37c5-9e9a-7f0f9418f5e1 | -4.71844 | -46.46628 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 596187f4-dca1-380d-9d80-84edf3d01a4f | -3.92053 | -49.21943 | 2025-11-26 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 258764eb-596c-3392-8d2e-9ec466cec206 | -3.43656 | -50.18479 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af46a444-be1d-32f1-80b4-26023e709047 | -5.35196 | -44.88604 | 2025-11-26 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0635983d-1c39-344a-9855-3923bc87bb1c | -2.55371 | -45.3919 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a4bb453-d0e0-3de5-8211-96a061aac3ed | -4.68622 | -38.54115 | 2025-11-26 03:57:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30e33f8e-36c9-3bca-8231-ef7c0e95928b | -6.30732 | -43.79317 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 43fdeec4-68f5-3504-82f7-88e544ba4e81 | -4.53641 | -45.56464 | 2025-11-26 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d05154e3-bf71-3556-9586-0a877e77370b | -6.04554 | -45.83987 | 2025-11-26 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 437d75d4-3594-3077-a1b9-8f55cb9013a3 | -5.41843 | -41.08128 | 2025-11-26 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b1e9a7fa-e85d-3b97-8fa6-10db00fbd359 | -5.12647 | -43.02416 | 2025-11-26 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1d5b10d-7cf4-30a1-b4fb-fecbab3cf816 | -9.12108 | -44.4385 | 2025-11-26 03:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 882b936d-32d7-3d64-843d-1189b82152aa | -8.06213 | -43.12917 | 2025-11-26 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| af99fbe4-8cde-3642-b749-07f38cc93521 | -7.74961 | -44.18855 | 2025-11-26 03:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a116088d-1e7f-38a8-8fe2-27f558f67098 | -8.54531 | -40.21504 | 2025-11-26 03:59:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88e850ab-c133-3401-a99e-bfc01c0310f5 | -10.20955 | -36.36687 | 2025-11-26 03:59:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 029fdadc-d154-3266-8932-ff2d2bd3c5b1 | -8.74623 | -39.81103 | 2025-11-26 03:59:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6234169b-3399-3c30-a83d-14bbcc75588f | -7.56873 | -45.87654 | 2025-11-26 03:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f3b733d-def9-332f-b15a-b58d83f14dfe | -8.59163 | -40.57827 | 2025-11-26 03:59:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b79512f-5b1a-31aa-9b66-a67c6cc1199e | -9.7177 | -36.29042 | 2025-11-26 03:59:00 | NPP-375D | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c9d6999-1f1f-371a-8902-ea38e93828f2 | -8.16284 | -43.19881 | 2025-11-26 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fd765648-1ea1-3e67-9b4e-f70baf52395b | -7.56318 | -45.88067 | 2025-11-26 03:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff5d6956-51f6-338e-9844-69c033da56c1 | -7.74897 | -44.19229 | 2025-11-26 03:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad876827-d3ab-393d-92c7-cc7e1997c203 | -11.4841 | -40.04568 | 2025-11-26 03:59:00 | NPP-375D | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1d10ac9f-38bc-353d-9b49-e038796c065c | -7.51265 | -45.71902 | 2025-11-26 03:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9f0311d-e46c-37c6-ba4e-70dc133d37b3 | -7.5642 | -47.11922 | 2025-11-26 03:59:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83a8131b-8ab8-313d-b74b-4c999073d9fd | -8.16755 | -43.19457 | 2025-11-26 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8d2be916-c950-318d-b37c-a30ff08ece68 | -8.16673 | -43.19947 | 2025-11-26 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f7d5a0ac-5bea-30bf-ace3-664e109c8d87 | -9.29303 | -35.59979 | 2025-11-26 03:59:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28260cc0-3a7f-30e0-87f4-eed2772ea07b | -9.13518 | -44.40623 | 2025-11-26 03:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b14ebfa8-f3be-3c7c-9ce8-e18af00ee458 | -9.10936 | -44.43231 | 2025-11-26 03:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0848c1ec-c89c-375c-b3a8-90a2850a33ef | -8.16367 | -43.19392 | 2025-11-26 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 589ca136-75a2-335c-ad6f-2a308465c52d | -7.56405 | -45.8757 | 2025-11-26 03:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f55e53f7-a651-3f39-aef7-d9d51aaeff39 | -7.56492 | -45.87077 | 2025-11-26 03:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e45b2f42-eb36-32c5-ac08-765910056aff | -9.98247 | -36.31847 | 2025-11-26 03:59:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 510ebb19-ba65-3bf8-bcce-76ebf1793e29 | -7.75247 | -44.19685 | 2025-11-26 03:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9a087db-c27d-34a6-a99e-be1e67894c57 | -7.74482 | -44.19145 | 2025-11-26 03:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0780fc6f-37cd-3585-878f-c9b55d77ca3e | -10.21312 | -36.36742 | 2025-11-26 03:59:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 10868518-50b6-3482-ab89-bc7d357c2e14 | -8.066 | -43.12984 | 2025-11-26 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2371d446-9c55-3b0a-bc54-e76e16199a54 | -7.50801 | -45.71823 | 2025-11-26 03:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25621068-9434-35da-a07c-87b7ad566f39 | -10.21251 | -36.37152 | 2025-11-26 03:59:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f4423934-c486-341a-b096-067537ba66b9 | -8.54194 | -40.21449 | 2025-11-26 03:59:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2c3681b5-927b-3a38-bce3-fe2b62b14b96 | -7.55937 | -45.87487 | 2025-11-26 03:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aefd29f0-8863-3a4b-813c-9f133d552169 | -7.51181 | -45.72387 | 2025-11-26 03:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd2fc472-0d14-34c8-bfa4-25111b2189da | -9.72126 | -36.291 | 2025-11-26 03:59:00 | NPP-375D | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5fc026f3-bb54-35b6-b0fb-cb51733111f7 | -9.1393 | -44.40701 | 2025-11-26 03:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc31968e-797b-3c6c-8c77-41ba499a1ff1 | -9.00701 | -44.44943 | 2025-11-26 03:59:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 567884c5-c2b5-33bc-b260-597c0211f296 | -7.74832 | -44.19604 | 2025-11-26 03:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2eb150b-f400-3728-b1d4-12dae079cf01 | -7.55912 | -47.11824 | 2025-11-26 03:59:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ece08bc7-12bd-300c-811b-e1443c532a8f | -18.94485 | -49.30105 | 2025-11-26 04:01:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 194ff2af-f0bd-35d9-a399-7d0cffc39030 | -20.5735 | -45.87978 | 2025-11-26 04:01:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9b45e33f-fc81-342a-a204-009dce5bbeca | -17.46953 | -45.99194 | 2025-11-26 04:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee59339c-dcbc-3666-b37d-89c76f0e5800 | -20.56969 | -45.87927 | 2025-11-26 04:01:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc50f49f-5960-3e98-890f-f48789a5e04d | -16.76639 | -51.3553 | 2025-11-26 04:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7cfc347-e436-3fc9-9224-3be7388425c4 | -20.57602 | -45.86599 | 2025-11-26 04:01:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70bfb5b2-e302-3c11-8b1d-1c050905cf2a | -16.7616 | -51.34996 | 2025-11-26 04:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4786388-448c-37d1-82a5-0e8f4d364ff2 | -18.79216 | -48.55259 | 2025-11-26 04:01:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2b9cb68-8444-3502-b3cb-d812abd29912 | -20.56673 | -45.87411 | 2025-11-26 04:01:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e20afbb-aaa4-30ed-a564-f8260cd80657 | -20.70313 | -49.11129 | 2025-11-26 04:01:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657ac5b9-beb3-310d-9173-2778f9e88b45 | -16.77447 | -51.34519 | 2025-11-26 04:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d75722f7-c016-32c2-8cda-f97a159091aa | -20.95621 | -43.29432 | 2025-11-26 04:01:00 | NPP-375D | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6db29c4-de01-3dac-8f69-d10a9928be73 | -20.58107 | -45.88109 | 2025-11-26 04:01:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a986f20-f8bd-3493-8731-96f46689e8b5 | -20.57729 | -45.88037 | 2025-11-26 04:01:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 18a3047a-d6d5-3c6b-bd66-096783ac65de | -21.29691 | -48.68945 | 2025-11-26 04:04:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 60148444-b7f4-33ea-8248-dd18f61ffb4f | -21.29505 | -48.69119 | 2025-11-26 04:04:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 887d7e21-b40b-3e59-9fdb-b813c86636c0 | -22.97923 | -48.66693 | 2025-11-26 04:04:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3ec80a6-6d30-3e1b-9b73-e1f6ea953fc7 | -25.19008 | -52.97477 | 2025-11-26 04:04:00 | NPP-375D | IBEMA | PARANÁ | Brasil | 4109757 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1ce05f46-35a8-3fbc-9cb2-87a5b770c882 | -22.47353 | -49.12931 | 2025-11-26 04:04:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84f057d7-7aaf-35de-8a9e-62b6dbbb6515 | -22.47794 | -49.13031 | 2025-11-26 04:04:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35012886-7a88-34cc-91af-6c7812d287ac | -26.10161 | -50.1775 | 2025-11-26 04:04:00 | NPP-375D | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29f953af-9f73-3ffe-99a9-d5d39b9689f5 | -22.23267 | -43.32039 | 2025-11-26 04:04:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
