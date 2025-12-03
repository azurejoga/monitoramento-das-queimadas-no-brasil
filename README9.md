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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aac04056-5fac-3b05-ac13-a5ea4cc94e1e | -3.70408 | -42.13799 | 2025-12-03 04:38:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82159357-f7f4-32de-bb81-f0cac4b5fba3 | -1.95808 | -46.41233 | 2025-12-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e964399d-78f7-3ccc-a546-b893b0ce8e5e | -3.57535 | -50.29544 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e432c9d-e436-3073-a19e-85e79d80a86a | -2.84898 | -46.732 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3a783be-554a-357b-826a-931206c070fa | -2.38107 | -49.38774 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc0544f3-512d-3bf3-bf4c-684c451c86d4 | -2.28564 | -47.97866 | 2025-12-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d01c614-a73b-37ec-91e3-4097053ff808 | -3.21734 | -45.53238 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efa9e6bf-29f8-3b8f-a48f-2dd4bdb17f1c | -2.96595 | -48.58634 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21ea2672-55f4-316a-837b-816eb6e4a7ce | -3.25494 | -45.56186 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 190a81eb-8557-3d8a-8401-7f842abbd175 | -2.99869 | -47.89898 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 555d41ba-7954-324b-a348-f7de3da94498 | -2.95993 | -51.01136 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed19724f-c9fc-383f-9828-aa6ff03f65ba | -3.24135 | -45.54452 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 524b091c-ad98-3084-83ad-06703c27967d | -2.38475 | -48.95209 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34dc5628-3f33-3f18-8243-1bce4a290aed | -1.86376 | -48.02215 | 2025-12-03 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb35b7ce-c3c0-3360-af37-e424b4d7bc3c | -1.74047 | -46.86914 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9063f92-b8d9-39f4-beaa-4a895c24507d | -2.21125 | -47.99897 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 64e2e5b7-0c2c-3c79-8bbb-5efe195f2da6 | -3.22754 | -45.53818 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96838457-a154-3c46-92fd-02e73838a09b | -3.23938 | -45.5424 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1a3c028-eac8-31f2-b463-6aef1dc27420 | -3.23876 | -45.56113 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d4491d86-20de-3cac-935f-038f5bd2b4aa | -3.25258 | -45.55296 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f328ce0-02e9-3500-bc04-7fad50f6d7f3 | -5.38374 | -46.75589 | 2025-12-03 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7bd41dc-e8c1-3bac-93c3-e356311c60d1 | -3.31076 | -52.56806 | 2025-12-03 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0c3f19a-1966-3c81-9828-8cd3ef60829c | -1.05589 | -53.01733 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add58701-1a20-3a11-8f94-88000fe05472 | -4.1834 | -46.48544 | 2025-12-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62a6b0ab-075f-3e46-963a-c13d60218c31 | -3.23314 | -45.58398 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 811e5350-686b-315f-84a8-8394875e4f0c | -2.38046 | -47.08484 | 2025-12-03 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4e336e-7133-3741-ac08-b367464b2a0b | -3.23709 | -45.54813 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ca93cc3-6281-3a81-8509-1ffabe8caac5 | -2.60534 | -49.25954 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07cfcf40-1d81-3426-9d18-47b66016bc94 | -3.56544 | -47.18095 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e14e7c5-a3c2-3213-a5e6-9acf5d80a008 | -1.20095 | -53.08681 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 18ff596b-c6d8-387c-9cb8-c660918b8ca0 | -3.38975 | -49.82994 | 2025-12-03 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eee7335-a408-35da-b508-bc7ef7aa1a92 | -2.98633 | -49.51871 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 67b89aa1-2a4e-3f50-b898-aef9b96c67f7 | -2.61747 | -49.24722 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eaca7fa-d313-399f-be53-f2b5bb9eb124 | -2.84578 | -52.61271 | 2025-12-03 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64d9ddca-42de-36ed-a0a7-cca4234374a7 | -3.24474 | -45.55598 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a44784d8-cc92-34a7-a48a-026ac68ff2cb | -3.25855 | -45.56241 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5099d5d-780b-3f9e-a801-effacb7582ff | -3.24348 | -45.56433 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d0c0c3d9-d5db-3297-b7cd-826747bf9460 | -3.22857 | -45.55535 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9247b22-7527-3296-a5d8-c833367c1364 | -3.59764 | -47.26379 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5a77c8a-526a-35be-b1a1-81541bafee79 | -3.24396 | -45.58566 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0226dfdf-4e21-3536-99b7-b8beb133b8b3 | -2.50324 | -51.8005 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 335d5ed2-5dc5-329e-bd09-c239b74a90eb | -2.76801 | -52.11213 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6339183a-5514-3650-9f1e-d4a5b99799be | 0.76727 | -50.80295 | 2025-12-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 914a9e10-f815-344b-8f2b-4ec8416ef9a6 | -2.54593 | -45.39515 | 2025-12-03 04:38:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40d15936-4b37-3f03-aec2-b9e682e88ab0 | -4.39475 | -43.13165 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53fa68a1-eb13-3cbc-905b-75f9c85e2f9e | -4.51498 | -44.65162 | 2025-12-03 04:38:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ed0f41a-924e-30bf-932b-ceea02a4aeb4 | -4.28735 | -45.93946 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec60c999-5e6d-330d-aea1-bbffc573c519 | -3.71358 | -49.45877 | 2025-12-03 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54f014b0-ab60-3b96-b798-54dbbd6124ee | -3.24302 | -45.55753 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3f3b5cf0-3d89-31fa-97a6-b273e1ff2f05 | -2.60975 | -49.25312 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1d4355c-1caa-3b86-b771-06f4f6cd3c02 | -2.842 | -52.61213 | 2025-12-03 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd4680d-8c9d-3cdd-8e92-a9dfcdc0fc92 | -4.07366 | -50.49916 | 2025-12-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18ff35ef-710f-32bc-b23c-37f474fce8a7 | -3.23051 | -45.54288 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a59e2c22-57ed-31d0-a835-87829f5ddae0 | -3.24107 | -45.57001 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 06c19b80-492e-371f-ab84-2b2a0f49f75d | -4.38507 | -43.13831 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe8a3c5c-9de6-3011-868d-4e596cf23205 | -3.22031 | -45.5371 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 3919aca0-77cf-3084-846b-0519de5abbd6 | -2.84785 | -46.73938 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c36caad-22fb-3323-bb13-cca9e0e7634a | -1.4795 | -45.78392 | 2025-12-03 04:38:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76a8d361-f419-3a51-9d8f-91acaa07a616 | -3.31444 | -50.26249 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3d03071-3aa0-3646-af97-96773d710c92 | -2.57304 | -45.14446 | 2025-12-03 04:38:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa75de80-7d83-3dc0-a690-5deb86d7c0ad | -2.89239 | -53.30081 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46db7d4b-a013-3477-ba44-0806120793e2 | -3.27151 | -50.7542 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7109e757-f0ef-3cc3-afd7-e8a6a2faa8ba | -3.8629 | -40.64487 | 2025-12-03 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e85a429-87a7-3cdb-91c9-7e04cbcb25d1 | -3.25133 | -45.56129 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8245b5aa-d394-37ef-b6a6-2eb8c132f3c4 | -0.29562 | -49.76482 | 2025-12-03 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2bec0dd-c9fb-3394-b549-872a92fd94f2 | -2.54727 | -49.06629 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 055a590b-1849-3cd5-af85-e1f754c7120b | -2.98965 | -49.51922 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e1e06ce0-0881-3acc-bb15-613dc45f267d | -2.61693 | -49.25069 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c20f6a3-3594-33df-8a20-74fbbe32efec | -4.38991 | -43.13498 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ffcc4fa-18b8-3132-9939-74352b4c053b | -2.78477 | -47.41702 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c86d057f-3216-3ad0-8887-41c75fa0be89 | -3.8632 | -40.64457 | 2025-12-03 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1dc6c305-ec83-328a-8bee-29cf9393df33 | -3.03311 | -51.1008 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33563dfd-9c6e-30b1-9fce-032b548223a1 | -3.63553 | -48.89577 | 2025-12-03 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0215941d-0cd4-3f37-af4b-d853bfaf96d2 | -2.46685 | -51.25923 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cb698a4-ced5-3b75-a9b5-d109592e5e26 | -4.42352 | -45.9506 | 2025-12-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d7c6f70-d5f6-3393-9acc-0151692707ec | -2.5721 | -46.88549 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cd7340d-9d4d-31a9-ada9-ee6d4ce34fdb | -2.89679 | -53.29935 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1668b52-7dea-3562-a074-73938d076a38 | -2.96055 | -51.00753 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0c08e72-f3ac-3081-917a-dad0bdf9e2e9 | -3.76327 | -50.15663 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc50ca56-a3e0-3c6a-8b25-3cf8d9c21d13 | 1.97783 | -55.72726 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b860f19-b9d5-3877-8c4a-98543149108d | -2.69076 | -51.79432 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea746a64-821d-32b9-80d5-2c048ae08767 | -3.05829 | -49.62336 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4a89d8-7cda-3ae6-8665-a098b6ff3286 | -3.31004 | -52.57258 | 2025-12-03 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2691d44d-e5cc-34a6-a21f-ca14352ef9d0 | -3.2256 | -45.55065 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c16ab62-7c90-3756-85f2-ccb155dd379e | -5.02903 | -41.00999 | 2025-12-03 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e8726c5a-e794-3491-93a4-62018804531f | -3.66896 | -50.48803 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57544923-162b-3f07-bf2f-36260d70eec4 | -3.24161 | -45.57679 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c40e9e8-328f-30ea-9193-30567a40739e | -2.99243 | -49.52322 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1166d719-60a1-36c1-bf82-8649a655d3e6 | -2.62707 | -48.05682 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74542b20-8a6c-3cb5-90c7-328a08501602 | -2.5695 | -47.15791 | 2025-12-03 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88bbc12c-08c8-3282-a781-32b7c49c2114 | -6.26075 | -37.2323 | 2025-12-03 04:38:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc0057a1-24cd-3407-b106-f43d86f76be1 | -3.92495 | -47.21335 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 447eb88d-fd24-3703-ba5c-5c60850202b9 | -3.25305 | -45.57433 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dee1e39-635d-337d-947f-24638ded60ec | -3.3072 | -50.0119 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04aae1de-ce34-328a-9bbe-2fdd504d5bc1 | -2.57768 | -49.08867 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf5c48ce-cdba-3985-aacd-35047d4cfbbd | -3.04683 | -48.41938 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51cac2bf-f402-3c81-915d-97a3b558a11a | -3.22625 | -45.5465 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef267766-bcf3-3760-90f5-c6486502dc14 | -3.24237 | -45.54711 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5744f4f-a81d-3071-8732-0419dc0778f4 | -3.63116 | -50.23841 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 318e731b-1612-301f-8032-d997f0403e60 | -3.2496 | -45.54823 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
