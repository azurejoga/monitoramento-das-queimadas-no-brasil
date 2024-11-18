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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c99acd56-6b0a-351d-bdd9-0cef35169c5d | -1.7982 | -46.531101 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72762a25-91e3-3da7-bf8a-2c5c407c11ab | -3.9427 | -46.4044 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4b02f1-55d1-3f2f-8e79-b7e4de0880ab | -2.5779 | -51.705299 | 2024-11-18 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92205341-e30d-32b7-adcd-9bbae41fe2f3 | -3.6486 | -50.414902 | 2024-11-18 00:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734a596e-0cb3-34d0-9aae-65fd459d5796 | -4.7242 | -44.434601 | 2024-11-18 00:09:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56c15ce0-2faf-32b9-8f1c-0645fcd8c110 | -4.5492 | -45.6306 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1393e377-ada3-33cf-b17e-a67af3f8fc06 | -2.681 | -45.715302 | 2024-11-18 00:09:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eec05ddb-aa6c-34df-b86e-526f98cf34c4 | -2.7481 | -52.601898 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88d2ac8-c9df-3707-b931-a32e7a3c4db3 | -4.3442 | -44.388599 | 2024-11-18 00:09:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d10b1f3-1109-3b27-b286-1774b12b3d86 | -5.2457 | -44.056099 | 2024-11-18 00:09:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1eddce-b70f-33f3-a94f-628318e27dcb | -3.9393 | -46.7108 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f01dc0d-3028-3af4-90f8-1ef18699272d | -2.9587 | -49.0938 | 2024-11-18 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd061d1-ef1c-3fba-9bdc-11fad5d9977f | -4.5615 | -45.639801 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 707d671b-4dbe-33cc-8e69-bceab195e4b4 | -1.6909 | -45.8326 | 2024-11-18 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 050afde7-9bf2-34a5-814e-e3e3354415a9 | -3.1415 | -45.983398 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9545710f-1b62-3818-8fc6-87b9cf955c86 | -4.5738 | -45.648899 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbbdc1e9-9614-3546-a1ea-f5cc0d47aefc | -4.7802 | -46.489101 | 2024-11-18 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91313332-41d7-39b5-b444-b1a6a0721801 | -2.6614 | -46.219799 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af6414c8-8a2d-349a-b781-3163fa71adfb | -6.5264 | -35.178799 | 2024-11-18 00:09:00 | METOP-C | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9a0d87f-bc2f-3427-8e5a-0fe3897479ac | -5.5393 | -43.298801 | 2024-11-18 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34d6ccbc-c062-3f12-aa34-3e971018579a | -2.2804 | -46.077599 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4690c66-5de1-30cf-82a6-6f2feb57ca1d | -6.5213 | -35.200699 | 2024-11-18 00:09:00 | METOP-C | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfdf5f87-0bdc-3a84-bc8d-1575d4318e61 | -2.1161 | -45.3522 | 2024-11-18 00:09:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 710c2dc6-b33f-3132-8d4b-aaa5e4b3da91 | -2.4957 | -45.622601 | 2024-11-18 00:09:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48f96e64-ca68-316c-9bbb-16808a274ac9 | -3.9364 | -46.6978 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0509c4-5602-3607-a713-087547bea1a7 | -10.4898 | -36.7374 | 2024-11-18 00:09:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34e25579-35d7-3a13-aa3a-74415bfc8540 | -4.1543 | -43.908199 | 2024-11-18 00:09:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89b8643a-195b-3a57-bed9-18f91487290f | -3.7434 | -45.924 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bee0de1-556e-382b-8948-46b328c2299a | -7.3912 | -42.754002 | 2024-11-18 00:09:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d24a7c6d-e14d-3303-93d8-0c336183f0ed | -2.464 | -45.6185 | 2024-11-18 00:09:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acf89088-7f61-34dd-b256-2d2800637370 | -2.2463 | -46.3349 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f7c0df2-4502-3b6d-917f-e8d6f6991496 | -6.7521 | -35.000198 | 2024-11-18 00:09:00 | METOP-C | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27e93661-70f2-322d-b8cb-6b323f3160ed | -3.2902 | -42.906799 | 2024-11-18 00:09:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e03dfdb-31fd-3bba-9627-29dc438ad1d0 | -3.164 | -46.586201 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6063bdf2-f420-3f0b-b469-0cefa6af213d | -2.9115 | -46.693401 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da54703-ceaf-3ea7-a935-25d9e785d14c | -4.783 | -46.501999 | 2024-11-18 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 943c4e75-dde2-397f-9a4c-02bd0f547710 | -2.6366 | -46.201199 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa4dc13-eb79-3ca6-9029-d350ca9fffd1 | -5.5123 | -41.0746 | 2024-11-18 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 45162c9d-7c31-3882-8006-93ec9e4a01a4 | -7.3949 | -42.770699 | 2024-11-18 00:09:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b68c2dc7-7827-3579-9387-7e2947194cbe | -10.0981 | -36.3452 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e55bee50-5e35-3aed-834a-b13f39df4e9e | -6.9505 | -42.481098 | 2024-11-18 00:09:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87c8a138-7bf5-3c3d-96a6-cb6655b703ac | -3.1736 | -45.441299 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5fa6403-0f6b-3493-bbe2-c08aef0e342a | -2.4519 | -45.610298 | 2024-11-18 00:09:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e15e712e-8a3f-3847-ba34-f5c6bf830bc0 | -4.2905 | -45.987801 | 2024-11-18 00:09:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db039814-f46c-3774-a704-1db6fe5284ba | -2.6588 | -46.208302 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2b140a8-66f5-32dd-8bd3-da009529a9ad | -10.1018 | -36.360802 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3389a69-0e19-3f2c-8567-311339fca953 | -4.9436 | -44.4977 | 2024-11-18 00:09:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5788e81-66de-3691-a97c-d415364969c7 | -5.2575 | -44.063202 | 2024-11-18 00:09:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d60a3870-2cba-34e5-9752-5dd3befd86fb | -2.4543 | -45.620701 | 2024-11-18 00:09:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4e003c6-ac07-3c66-8949-1b1dfd661b3a | -1.2775 | -51.7346 | 2024-11-18 00:09:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 156fb519-33aa-3c14-9289-2699d58c8114 | -3.7583 | -45.944698 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcc1c356-b82c-339d-b6de-b4f59964c248 | -3.6537 | -50.438202 | 2024-11-18 00:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13eb18bb-df71-30c5-8e03-a3fb86ce6938 | -2.649 | -46.210499 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58b78fb0-e31d-37d8-aeb8-a62f4d79fe12 | -4.5713 | -45.6376 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4441af97-c451-3d45-9298-c4101b67dd81 | -3.7532 | -45.921902 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17235904-801b-3956-a0b3-9d1fdc0d62a1 | -7.3991 | -38.993599 | 2024-11-18 00:09:00 | METOP-C | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1de3ba34-4713-37d7-92c5-5b11bea31165 | -2.7577 | -52.5998 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcce0fc4-124c-3d25-8fec-6a35114c2f7b | -2.6762 | -45.693901 | 2024-11-18 00:09:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64ae2a09-2564-384b-bdf8-e1cc7414768b | -9.8068 | -39.1493 | 2024-11-18 00:09:00 | METOP-C | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 94418c76-d98a-3724-a5db-05e240e1f13c | -3.2733 | -46.159199 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 598ff983-5f9f-3a9c-99a9-dc393471f925 | -6.519 | -35.190899 | 2024-11-18 00:09:00 | METOP-C | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47cf255d-661b-3771-950b-31eb2154c8ad | -10.5093 | -36.7328 | 2024-11-18 00:09:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a93b3e7e-53dd-300e-91c8-5e1de836aed7 | -2.8193 | -46.648399 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490e77c8-1e1e-3a0a-8cbb-e8f6207b6287 | -1.7031 | -45.841 | 2024-11-18 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ecb86670-0889-3e26-9354-3903611efb36 | -5.2477 | -44.0653 | 2024-11-18 00:09:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d69c6fd-8b36-3d50-811f-a7cb2fa51124 | -1.6959 | -45.809502 | 2024-11-18 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 021c081f-a9ac-3935-9a28-5fc1d585d936 | -4.9 | -44.025799 | 2024-11-18 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8866685b-1c25-371a-b1a4-4baef27fcd49 | -6.7399 | -34.992599 | 2024-11-18 00:09:00 | METOP-C | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7fe4005-eba1-3075-8e4c-16108f17dbf2 | -2.9628 | -49.112202 | 2024-11-18 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f4d768-266d-3c23-a110-1974d3d9d8c7 | -4.898 | -44.0168 | 2024-11-18 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c854b4e-817b-381b-bec7-8fedb1d87431 | -6.2029 | -43.279202 | 2024-11-18 00:09:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 221e0b5f-1bde-3fe4-9c9b-b8ead77d88b9 | -7.098 | -39.300499 | 2024-11-18 00:09:00 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d17dbc24-f9a8-3052-98f2-52f2c7f37e78 | -3.9455 | -46.416801 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdddb901-9f6b-3adf-98c6-9a6ba4166743 | -5.9365 | -48.049999 | 2024-11-18 00:09:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c503e4b4-d12f-3aad-886c-451bdb786f46 | -6.8596 | -38.8909 | 2024-11-18 00:09:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 85e5064c-7924-35c8-ac15-9c0640a741c1 | -6.5311 | -35.198399 | 2024-11-18 00:09:00 | METOP-C | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e45e5555-2ab3-367d-8836-33cc9d50e54d | -3.7609 | -45.9562 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc4279dd-6982-3a6a-9c31-5c4b7b74644b | -4.3421 | -44.3792 | 2024-11-18 00:09:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0843317-22bc-3fbd-b1e1-b67ead06ed3e | -10.4916 | -36.7449 | 2024-11-18 00:09:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a3e75fb6-634c-31ff-90a9-97e0f02684e2 | -1.7007 | -45.830502 | 2024-11-18 00:09:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2e96500-ddbf-3d51-8b0f-765583f137f5 | -3.321 | -46.235001 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 196ebea7-6eaf-3feb-8a49-1446143de26f | -2.8504 | -51.792801 | 2024-11-18 00:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c893b61-1441-3ef1-b7ff-c69484beebdd | -4.9899 | -44.337002 | 2024-11-18 00:09:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5dd63f-2712-3116-9b91-9e4fb1a7750b | -4.392 | -44.740299 | 2024-11-18 00:09:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9eebab-4ae2-3ab2-820d-402035e37ed1 | -2.9087 | -46.681 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2212527d-2fbd-32a0-8f2b-433ecd16af8a | -2.6859 | -45.691799 | 2024-11-18 00:09:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdf905eb-c48b-349a-9775-567db41b79aa | -3.181 | -45.428799 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1573b201-b623-3c26-ab86-c518b38c0484 | -2.1564 | -46.391201 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d714afe0-e7e5-3441-9869-fa6b4403185c | -6.2646 | -42.956001 | 2024-11-18 00:09:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1f448fa-18bb-34e7-b6e3-4904f61311ca | -4.8056 | -44.4772 | 2024-11-18 00:09:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e492a6bd-2b84-31d9-a2e7-f0732d39fcee | -2.6737 | -46.229198 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fba9fc6-de19-3fe2-87dc-fb7f88f10750 | -3.6282 | -45.913101 | 2024-11-18 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5ddeb17-e4bb-3134-aa93-39e07cd8e500 | -2.9502 | -49.192501 | 2024-11-18 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8516414-7250-3888-b337-bfa643030366 | -4.1265 | -44.242199 | 2024-11-18 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d67cbd5-b1f6-37c8-b664-fe8c75e78c5b | -7.6456 | -35.326698 | 2024-11-18 00:09:00 | METOP-C | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a66407cd-4b1d-3ba6-8304-1aca13bf9e9d | -6.9838 | -39.6577 | 2024-11-18 00:09:00 | METOP-C | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f678e1ff-08be-34fb-af59-fd7a6e7716df | -2.6392 | -46.212601 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e02244ff-5099-3df8-9b7f-5b952a863391 | -2.1039 | -46.476299 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af515ced-0245-33c0-944e-de657c8f9142 | -10.8109 | -44.952801 | 2024-11-18 00:09:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9f0b5075-8a93-33b0-b9be-40ed07f3e31e | -7.4007 | -39.0005 | 2024-11-18 00:09:00 | METOP-C | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
