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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5605977e-e505-3a84-a0f0-0cd4b3d76bb8 | -9.19725 | -45.73792 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f305dbc6-1a17-3500-a99f-bf56f7f35396 | -11.60789 | -43.53579 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df0d9e20-de31-33e6-829f-7ce1b4be0e39 | -11.45864 | -43.45537 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2df83cb1-9907-30d7-8a6c-83adf1a213f2 | -8.61961 | -45.37137 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34317d65-a557-3975-9661-56492cc823d2 | -6.1343 | -53.28979 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65f43c2c-8ba9-3ffd-a923-2031f7412b06 | -10.78253 | -50.52573 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a827c23-ff66-351a-a397-d3ea59628a26 | -10.25382 | -44.58247 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1dd457b7-f170-3d85-a156-2b9e04e99644 | -11.6515 | -43.5555 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 188987f4-bada-375a-96ee-ea8ab80a1e04 | -8.21718 | -45.48224 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfdf4682-6a45-31bb-bdb1-397085415919 | -7.38041 | -46.42756 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13784060-fe21-326a-9dbc-28cd495e3280 | -5.74466 | -45.16547 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 411d59bb-7a7b-368f-a02f-0cdfd37654a3 | -4.25947 | -50.74132 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6ab17ff8-dd7a-33e1-8dee-c20c7a5f0409 | -4.27812 | -50.81818 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b87256eb-251a-3f4a-b8a5-8bc305ac89e9 | -7.02547 | -44.63941 | 2026-10-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50709358-b8b8-3ef5-9f7e-0d79db4f6103 | -4.25167 | -50.74964 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 38b0eb26-e54b-3be1-bbb0-54fea2a7fb0e | -6.19076 | -44.85727 | 2026-10-01 04:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9e457c8-0c84-317d-aa07-cfbf50051cbf | -10.46454 | -51.76521 | 2026-10-01 04:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b1c106-e781-3da4-b755-384746d3e782 | -8.13062 | -43.53088 | 2026-10-01 04:14:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa202899-8f3d-3aaa-8838-623a1c8423fe | -9.76553 | -44.81354 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87606024-b23e-3088-ad9c-d55e24cc824d | -10.74585 | -50.54161 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd2c6db4-7e41-323e-bd5b-c2b520c49782 | -3.80598 | -51.02438 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8117057c-9955-33e2-ade6-1a558aa376d2 | -10.27445 | -44.64304 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29f2d3d2-4efa-39ce-a37c-6f8173987b7c | -10.46169 | -46.77294 | 2026-10-01 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 623f3e9f-972c-31d1-9a60-9083cd458936 | -4.30105 | -50.75846 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a69a62ae-7a72-3777-bf10-d75d017b2717 | -11.28584 | -50.9752 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f5ff08e-70bf-3a1e-b33f-ca0f733f559e | -4.26403 | -50.8258 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f55859b8-0a89-38ef-866e-a01e138544d1 | -8.21441 | -45.47406 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 571d3817-bafe-3f87-9801-b9d962488ff1 | -4.29538 | -50.79183 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6205374f-de13-37d0-9d5e-e2216ee48ec8 | -4.26403 | -50.75175 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 92451c57-377c-38f3-af6d-8dea62e3f402 | -4.29084 | -50.78103 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0f8c72aa-5232-331c-8048-3101027dd333 | -11.39505 | -43.38397 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ab303c2-78fc-3664-a005-fd069d5b7deb | -3.80498 | -51.03003 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 64e0c7da-5ceb-3d92-8aa1-a400150248d1 | -4.25867 | -50.74594 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c21ac390-efa5-3de2-9e27-750768d43590 | -6.13305 | -53.29633 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 538737f9-88d2-39aa-8a33-79b5dd3cf718 | -4.89093 | -48.37547 | 2026-10-01 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 928ba823-a81e-3acc-9324-ed7fd6cda55c | -11.41092 | -51.02241 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2ed8f9a-1a19-3722-91c0-4c00710ce9ac | -12.35682 | -46.37933 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f671f0e-5dae-3b37-9f85-c7e9e40f907c | -4.63302 | -50.614 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a5a0dff-aa66-3a0e-83c6-7db866a8b6b7 | -4.27167 | -50.73456 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36487a9b-08f6-3b8d-9847-c2a67ae9aebd | -5.74529 | -45.16166 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 998f5da5-2c8f-345b-b644-937859702b50 | -4.25858 | -50.77193 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 786e62de-95a6-336b-98cf-4ab4d7829770 | -8.84717 | -44.39175 | 2026-10-01 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cb73f19-1c78-36b5-9227-619079ad7781 | -6.70944 | -45.98148 | 2026-10-01 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f8cca88-9fc1-33b3-8768-2d574b239e85 | -7.49624 | -45.79662 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e89f276-151b-3ec5-9af9-1d68102bb0a8 | -8.77279 | -47.84272 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2cfe0e2-ca3e-32e9-8e05-e44caed92c0b | -9.79008 | -44.80809 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 472107e6-1ac1-3d43-abf1-41cbbfcbe7ea | -4.2727 | -50.81249 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1c37bb82-b268-38e3-a2ad-9df4d3091dec | -4.27144 | -50.7827 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 94f86cae-8188-3792-85fc-d54f7fa289ed | -11.2223 | -45.18008 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 722be52e-3f44-318c-a9b3-00b0b9b812c2 | -4.26121 | -50.75729 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1f46e29b-d7c9-31b1-a664-0074ad7fb5fe | -9.20092 | -45.81441 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdde7f69-515c-3e11-a121-8640043a580f | -4.28869 | -50.7818 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 253.0 |
| 78c19339-c9ea-3ef5-9308-a837fd51293c | -9.20792 | -45.82289 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51de9a17-2214-3149-9bde-a871ed9a7234 | -8.01377 | -47.45409 | 2026-10-01 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3626b76-3a22-3206-8179-a23e311bfa52 | -7.47308 | -49.5726 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4876752a-8b4d-33a1-b1d8-3852d93b7cb5 | -8.21118 | -45.49249 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8230349d-ed86-3a13-a1e4-64b02dc0c825 | -8.62746 | -45.32541 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6363d863-2fb1-3bda-8d09-965ca2e1bebf | -7.84961 | -45.82704 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6c631d2e-2d29-33c7-9ef5-11899b66055a | -8.04424 | -42.86194 | 2026-10-01 04:14:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d86ed8f2-7919-3424-aa13-d35f3f00fc70 | -11.41613 | -50.99611 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1df10fb7-2be4-3d60-b7d8-a7e034e8f30c | -6.01239 | -49.55752 | 2026-10-01 04:14:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e94f9a83-d5da-3390-93cd-79516a5aedef | -4.63386 | -50.60936 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e059d15-2c60-33f4-b689-9fd8b2b5afc9 | -11.45425 | -43.43846 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e37027c2-4c0d-37e1-a8c4-03010e1e5d3e | -4.29208 | -50.81119 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 36944702-332d-38e8-8f11-307746bd99d7 | -4.303 | -50.80906 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38f136ef-e978-3adc-8e86-7fb6b0bbc4c1 | -4.28966 | -48.56176 | 2026-10-01 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd57b20a-be2b-3e3d-a8f8-c2c43355409a | -9.89872 | -50.16941 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55c515cb-74bd-3833-b569-18e301789d42 | -12.60955 | -42.16978 | 2026-10-01 04:14:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 986d2484-00cc-3ccb-b0d8-bac63f3a6330 | -4.27098 | -50.74835 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dee9d8cf-afb2-3f24-87f7-62ef191dfcbd | -11.45555 | -43.43061 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d91a806a-eb6a-35b3-aad1-9cdcf84f08b4 | -8.0149 | -42.88552 | 2026-10-01 04:14:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2483ae6d-5b7d-3579-9bae-07b0b9bb4097 | -4.30023 | -50.78868 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ec74fa6b-170d-36fd-9160-cc708de54ecf | -11.38743 | -43.36301 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8dc1ac3-8ab6-3ca5-9ce7-b191a788944f | -9.7931 | -44.81349 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d98fa74e-dda5-3cc0-8a95-d25b86a322ba | -7.84611 | -45.82236 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9cca918-2bf3-3504-b8ca-1c2490e867ac | -10.75733 | -50.51055 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5caeedf7-f34d-3b02-9716-69894b5383c9 | -4.2929 | -50.80637 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a9aa9943-174e-3be7-8189-c56321cee476 | -4.28589 | -50.81007 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a8dea14a-fb24-3ae4-8b70-68cd9779fdf8 | -4.86354 | -45.83899 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ecd0d4f-0423-3044-ae7d-e02570ca65f4 | -4.27432 | -50.80307 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7591cbb2-3f9b-3c60-ba41-aa99c809dcd0 | -4.26373 | -50.74333 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ca11fef-6572-3af1-8cdf-a410e4ae9f67 | -5.76849 | -45.15048 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b6dff16-d240-3a57-8d05-3dfeb410a412 | -6.7658 | -48.68169 | 2026-10-01 04:14:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c606fd68-50d5-3088-976a-d76973eca2e2 | -11.43522 | -43.42307 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1990a4e6-0467-3bbe-baee-c8af18972256 | -5.44 | -43.74175 | 2026-10-01 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b2650e2-ce8b-3637-8ef7-aa1c699e02a3 | -11.22009 | -45.17014 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2c9cc45-d367-38f3-827b-cd662ed579ec | -12.56677 | -43.06997 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0fc1c7b5-1991-36be-8758-dfa980fbc3f2 | -4.26481 | -50.77272 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 175a381d-1358-3090-9f33-c8f5d74c94df | -9.21546 | -50.6814 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450f9472-65bb-38f4-b468-675097beb6d7 | -4.28798 | -50.83526 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f078025-591e-3846-88a5-5e41d12abb49 | -11.17669 | -45.11166 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4402b14-5e48-3321-812f-ae941c7ffe90 | -8.01778 | -42.89009 | 2026-10-01 04:14:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 01fe8092-0476-3145-8acd-69e10abd3446 | -8.7992 | -47.99943 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b539c735-76c9-3a18-a263-8f1e5b1ab94c | -7.72169 | -49.5466 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1325d6e2-8ba7-340a-a16b-418385933d7b | -11.4128 | -50.9838 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac6cb2be-e308-3fa4-ae60-45cf6e2d92af | -11.2127 | -45.14481 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a95141f-3294-3065-beef-9ebc90997ac1 | -11.88211 | -40.96614 | 2026-10-01 04:14:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b357102-bec7-34dd-9290-5b1e1aea0000 | -9.17794 | -45.60824 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3940df-5a73-3ab2-94d2-83d56a904279 | -4.25949 | -50.81503 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7f2a715-306d-3c7e-bea3-10ea7d5dcb52 | -5.74881 | -45.16622 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README32.md)
