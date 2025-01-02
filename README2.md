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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d0f55dc-4506-3077-8f8f-e722ca48d7ed | -2.2796 | -46.4058 | 2025-01-02 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a896764-67fe-3e39-9ea9-5893bf3e2a1d | -1.73868 | -45.87573 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ca29803-9010-3257-add8-0ad8f8cc77ac | -1.71808 | -46.23456 | 2025-01-02 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1580a7a9-26a2-38dc-9cf1-262e69483fde | -4.3866 | -47.75193 | 2025-01-02 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88b8560a-309b-3a5a-9031-c4b71dfa0ca2 | -1.58801 | -45.98405 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4b54b3-7032-3612-9863-ee17f1f19ddd | -7.00069 | -34.94212 | 2025-01-02 04:21:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| d991e3e2-5013-344a-a43e-3176bcc337e3 | -2.32956 | -45.556 | 2025-01-02 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6edbc5cf-bd90-3dd2-befe-4fef9016e51f | -1.45113 | -45.67188 | 2025-01-02 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0213cc45-5e6d-31e1-a037-51cce2694b70 | -4.38727 | -47.74772 | 2025-01-02 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5f43d24-ef40-34ec-adea-6a67875b3f20 | -3.90684 | -47.05333 | 2025-01-02 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22865548-6ded-3453-9555-f90de806a714 | -2.27898 | -46.40968 | 2025-01-02 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28538abc-dbc7-38d5-a009-0f68e138d322 | -7.03675 | -39.21242 | 2025-01-02 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7eb4c3a6-5c3c-302c-8e56-ee1e1c2e7187 | -7.82355 | -35.17988 | 2025-01-02 04:21:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1022a47f-93d6-3be2-a141-1672d0769d07 | -1.32795 | -46.64595 | 2025-01-02 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 764e19e0-ea2f-3768-82ff-9f5336b543ac | -7.82868 | -35.18446 | 2025-01-02 04:21:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e5946ec2-dcf7-3cc9-a837-1c385526b4e9 | -1.777 | -45.92023 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56a5de87-9ee6-373c-b757-a1a78277e9e6 | -5.99629 | -43.57657 | 2025-01-02 04:21:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e2c8a448-1b94-341a-b0ff-2f9f59a3a502 | -6.80736 | -35.29647 | 2025-01-02 04:21:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 0e987e9f-2c2d-3a36-893e-7c64030de86a | -7.03256 | -39.21165 | 2025-01-02 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 160b825b-fbcf-3785-84b1-40d5ad16bd3e | -7.03737 | -39.2082 | 2025-01-02 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b23d44a9-84d2-37c1-8fc9-b2921af3a8f6 | -7.03304 | -39.21094 | 2025-01-02 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 67b607b9-259e-33b7-92ec-16568488b369 | -1.71459 | -46.23401 | 2025-01-02 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b3cc90f-1b23-3879-b871-9c709cf9366c | -1.74438 | -45.88427 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fec34d90-fd42-336a-b252-f9821c7a52a4 | -1.61638 | -46.21164 | 2025-01-02 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce396767-ac20-358d-bede-072f84b892d7 | -1.77756 | -45.92008 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a2dc0a7-06c8-387a-a97c-acaaa59e7916 | -1.69208 | -45.90308 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0fc2dcf-7fef-33dd-914e-8cadeaecc30f | -4.92783 | -48.56641 | 2025-01-02 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6d3c808-c746-3766-a9e2-3cec98a56d46 | -1.61507 | -46.24311 | 2025-01-02 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75736a8b-5d81-3f2a-836c-d4fcbb0d54ec | -1.73524 | -45.8752 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97861eee-7f89-36a1-8931-f034c9c1b5d5 | -6.80234 | -35.29218 | 2025-01-02 04:21:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 180aeb81-a1eb-3fe4-8d86-5f82857f94c3 | -6.80282 | -35.28866 | 2025-01-02 04:21:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 3850988a-9b30-35fe-a0b9-888de718cbba | -1.44771 | -45.67136 | 2025-01-02 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d16dd325-b2ef-3b7a-a0b0-d62eb0ba3ce2 | -1.78044 | -45.92077 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd0f01b9-35cb-3333-ac37-3e2195db2391 | -6.95312 | -43.00666 | 2025-01-02 04:21:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a069b88-756b-3ae7-a2a7-9637da29f975 | -7.82917 | -35.18065 | 2025-01-02 04:21:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 096a2c4f-897a-3b2d-9566-193a04e40d3e | -7.82305 | -35.18367 | 2025-01-02 04:21:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6b7af35d-6739-374d-a93b-48424219dc7d | -1.68863 | -45.90254 | 2025-01-02 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a8bf05-6732-3301-854c-7ffcab86cfc8 | -4.05172 | -41.64071 | 2025-01-02 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3a1caa40-3a93-374c-8f6b-102fca2b5822 | -5.24079 | -36.18523 | 2025-01-02 04:21:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7892dd06-9413-36fa-8700-bccf3c5e023c | -6.80836 | -35.28922 | 2025-01-02 04:21:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 65ff0be8-c864-34f3-854e-4ce3d6cc9788 | -7.03784 | -39.20741 | 2025-01-02 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| aa62cf69-d770-3d76-8875-7a36066be999 | -1.61669 | -46.24261 | 2025-01-02 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 547fbc7e-716b-3298-b8b3-1bfe2fd5e3b5 | -6.63901 | -38.73596 | 2025-01-02 04:21:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1e8d43fc-6788-3ae0-8ca7-ef0fb9ea107a | -7.03725 | -39.2117 | 2025-01-02 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fe8124e6-6b0d-3ca8-a139-d1321af1bd2f | -1.86649 | -45.53295 | 2025-01-02 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc8423fb-625f-3880-998a-4c8786a2adbd | -10.06567 | -36.14685 | 2025-01-02 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2486ebd9-a15c-3c67-99ff-cf64bae49d47 | -13.13802 | -41.77325 | 2025-01-02 04:23:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 742a93bf-3db7-388f-979d-2e7662affe30 | -8.62672 | -35.79095 | 2025-01-02 04:23:00 | NOAA-21 | BELÉM DE MARIA | PERNAMBUCO | Brasil | 2601508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| afdfd983-719b-359d-aab7-17d3848bf09a | -10.32455 | -36.72086 | 2025-01-02 04:23:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b528780f-4fa3-3a90-9a32-0daa668746be | -14.98031 | -40.41453 | 2025-01-02 04:23:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 06338dab-0eb9-3cfb-8e50-fcd1d6d2e937 | -13.13869 | -41.76844 | 2025-01-02 04:23:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d51b6e36-0972-3681-8780-5c00db78ee00 | -9.50444 | -40.32106 | 2025-01-02 04:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7243f5c-429e-305e-a488-f895bbbd400a | -19.34085 | -54.17102 | 2025-01-02 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 461c7815-0111-3155-bfa1-59f84979e9ef | -20.41647 | -43.55149 | 2025-01-02 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 26bb4dd3-5980-3f69-8dd4-3919c7df9fff | -21.19512 | -44.93695 | 2025-01-02 04:23:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 72c68cd9-c893-3aaf-b5e7-d2535e35cf5a | -10.5016 | -42.42706 | 2025-01-02 04:23:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 70b529e9-f92d-33fc-9dc5-42355763e924 | -10.06612 | -36.14326 | 2025-01-02 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 50d2f566-1b26-3b9d-875b-20d708f2fc94 | -19.33658 | -54.17016 | 2025-01-02 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b74010b-d181-3e19-81f5-f40ed54060eb | -14.97536 | -40.41858 | 2025-01-02 04:23:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53a4f4ae-76d8-3a7a-ad97-1dcbeb18cac1 | -10.2163 | -44.76297 | 2025-01-02 04:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cc395f1-e42c-3f33-b722-d3592783aaee | -10.93911 | -49.43159 | 2025-01-02 04:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 457df157-fdf5-3725-bfea-93755c7c0e54 | -11.23955 | -41.88923 | 2025-01-02 04:23:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf97b38d-f8ed-39b5-a1e4-aac691b46e64 | -14.87826 | -40.78387 | 2025-01-02 04:23:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c76f141e-5191-322f-86c8-ac1b6402929c | -14.97972 | -40.41925 | 2025-01-02 04:23:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6d1cdab7-d0f5-38ed-b3e8-41bb11abb6ad | -18.14773 | -54.26599 | 2025-01-02 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4140f9ea-86ca-358c-916f-773ea37aefd9 | -10.82401 | -37.16702 | 2025-01-02 04:23:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c5bf67df-d804-3e1e-83f5-2056bba1bc86 | -13.1426 | -41.76896 | 2025-01-02 04:23:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 370043a5-6099-33d9-a988-2b9225859a73 | -9.50393 | -40.32468 | 2025-01-02 04:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 79482c9b-54b4-335a-b179-9c9cfb97b383 | -23.52225 | -46.97307 | 2025-01-02 04:25:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1202f6e8-9180-3f74-ad7e-c8381cc2bcf2 | -22.67635 | -42.85728 | 2025-01-02 04:25:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96deca03-59d8-3eb4-8b81-67f419b756ad | -22.78579 | -43.75738 | 2025-01-02 04:25:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e87ca6c1-107b-3593-9eef-92a242d67a3b | -25.19356 | -49.32584 | 2025-01-02 04:25:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 27ab1d80-3fb7-3188-bb65-ba390502ae21 | -23.59417 | -47.43966 | 2025-01-02 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e3b616c0-db1c-3544-b3c4-39b63b2735aa | -23.40714 | -46.55514 | 2025-01-02 04:25:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 14e19d3e-25cc-3a52-a704-1d2b0647bfa7 | -20.59788 | -51.61113 | 2025-01-02 04:25:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| af4ed348-9a0e-34a0-a340-47251d8bd69c | -22.67683 | -42.85326 | 2025-01-02 04:25:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94ee634e-8484-3621-ba3f-eacf98084d0e | -23.98557 | -48.91606 | 2025-01-02 04:25:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22e833e6-c220-3a05-a701-278d880d4c7b | -24.24269 | -50.73796 | 2025-01-02 04:25:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3ac22f3c-51a6-33ca-9523-0d585460ec42 | -23.34107 | -46.7723 | 2025-01-02 04:25:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8636929b-105e-333d-a6bd-395530be5955 | -25.56804 | -49.36752 | 2025-01-02 04:25:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4fb0921b-317e-3fc1-8cdc-d7d6a8a09155 | -23.33765 | -46.7717 | 2025-01-02 04:25:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 675730f6-7f21-3fe6-87b3-357eb5bb662c | -3.9068 | -47.05286 | 2025-01-02 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efbc803a-76be-3b93-97f6-68fe16790847 | -1.71632 | -46.23307 | 2025-01-02 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe9e2b8-dc37-368d-90cb-d851a01acf34 | -4.69392 | -47.04559 | 2025-01-02 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3889434d-082e-3aa9-8c67-fbed66af4b20 | -1.86681 | -45.53139 | 2025-01-02 04:44:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb046d21-09ba-3c83-9d54-d77ec288700e | -1.73775 | -45.87461 | 2025-01-02 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2abb14e9-fe36-3ff2-aa3c-d2db5edd05b2 | -3.10906 | -51.99794 | 2025-01-02 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08eadca2-2ffe-318d-ae02-92c89f60e76d | -1.69016 | -45.90136 | 2025-01-02 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a92dd15-1c42-305d-93c9-8b9e30630ee4 | -1.73389 | -45.874 | 2025-01-02 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3127fd7f-3536-3f5d-ac36-edf5f2d9b6e8 | -1.45513 | -52.64076 | 2025-01-02 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d599449-e2b7-38aa-bfb5-0914684af519 | -4.69017 | -47.04504 | 2025-01-02 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ab62ade-6c37-3578-a1c0-07e201edd7e8 | -3.07098 | -41.88251 | 2025-01-02 04:44:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad592b6f-d188-3a9e-8368-bea3933b4b55 | -1.29082 | -52.10439 | 2025-01-02 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df706d38-f9c3-3eb6-9da5-6bc374714094 | -1.44878 | -45.6758 | 2025-01-02 04:44:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eee8bdb-67f9-3e78-95d8-9d1fa682c3f8 | -1.32905 | -46.64621 | 2025-01-02 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5a5fc1f-f223-329d-a0e0-bb50ff642105 | -1.77888 | -45.92183 | 2025-01-02 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cc37880-7caa-3b07-9e5f-70d3e4090e25 | -1.58873 | -45.98493 | 2025-01-02 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56db9fc2-0b76-3590-899c-10e247307807 | -2.27894 | -46.40824 | 2025-01-02 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00dbb38c-33c8-3afa-89b7-77af03e8f574 | -10.50322 | -42.42776 | 2025-01-02 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 01662284-723e-3de6-998a-139bae2b5163 | -10.50252 | -42.42846 | 2025-01-02 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README3.md)
