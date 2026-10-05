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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaff8b90-91c9-34d4-aef6-e37bd0720a4f | -3.83795 | -50.31767 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c97d74aa-a294-33e9-9cfc-803599511e28 | -3.70762 | -50.6478 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 134079be-6c28-3d3b-8ee8-23ec16322e47 | -10.96623 | -45.42698 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbd366d7-23cb-3319-9868-4d05a1a8656e | -7.09555 | -41.756 | 2026-10-05 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c994e064-0562-3a76-9d9b-d32bb36d8b0d | -7.19446 | -44.3087 | 2026-10-05 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf548215-0ffa-3eb4-bf0c-29accd4a19a2 | -2.85555 | -51.3011 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 36a5dfa7-86fb-3dc0-ac88-00857e71ca70 | -3.71369 | -50.64874 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 96264847-48d8-3e84-b02b-1896c8fd94bb | -3.47356 | -50.10215 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b154e0de-6312-3de2-899d-77a0a647c35a | -6.90138 | -43.67106 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d0bad55-2507-3c8a-804e-7a029fa9b117 | -3.20418 | -50.74819 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb45cfb5-a19b-36f7-a5df-f7b7d1ce69f7 | -6.33702 | -43.35925 | 2026-10-05 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a78a9f3-10ff-3501-a5da-0d09fda4ea10 | -4.3099 | -50.78193 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5a82e634-d197-37af-be02-91cecf585217 | -3.20951 | -50.75401 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae89121-d9ee-3667-9795-6630ad003bf8 | -6.89774 | -43.67046 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f98f6c6d-5050-377b-9c82-b916af45bf70 | -6.89635 | -43.67902 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c3108d79-b25f-3e25-80d6-57207337aaa2 | -8.58781 | -41.44529 | 2026-10-05 04:02:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd30b91c-bde6-30f9-bfcc-2804f1fb8704 | -3.28037 | -50.01596 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a124b067-c474-3031-a964-712d0cc9838e | -9.85714 | -44.8044 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20932818-46cc-3bd9-a6ea-ecc9eaae1792 | -7.7173 | -45.45849 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df805b5f-a1cc-33a9-9809-cb8a78a77fb7 | -2.67697 | -49.02954 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 73f8a38a-5ee6-386c-949c-fdaadad73b82 | -3.71327 | -50.64181 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3e32432-145b-35a0-9d38-8b0414d625f8 | -5.96947 | -41.32417 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45fd5000-8107-3de9-9781-286abc10fdc2 | -2.6983 | -49.0362 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07a78f15-525e-3709-a830-a8345083c5bc | -10.97082 | -45.42299 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5164a99-3d86-3415-a9b8-a53a7d10e667 | -4.11029 | -49.0695 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 648d19c4-9649-35e3-91e5-59efe1685415 | -6.87809 | -43.67617 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a79d7a78-ad57-3073-88e3-ff65a73c8bf5 | -6.92029 | -43.66988 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25ebc058-c39a-342a-a580-3116e204fcbd | -6.61582 | -41.77245 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b37d69b9-8cff-38aa-b6db-1755ea2c625b | -7.09498 | -41.7596 | 2026-10-05 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 26da0a94-9ecd-3be9-b9a8-0326fa0055da | -6.17808 | -52.92982 | 2026-10-05 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 24a55235-54ad-3172-9908-cfcc18574a44 | -2.69768 | -49.03988 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 524d4360-cab4-3bd1-bb61-da1689f52393 | -6.90207 | -43.6668 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8258403d-11e0-30e7-8430-2d5ed3a60816 | -9.84 | -44.79213 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae8a906e-4103-3944-a3e5-2c7f551eac54 | -6.913 | -43.66865 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53c50ea9-3054-3f9d-acbe-8a67035205f1 | -6.00348 | -53.51857 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb8ef1eb-2310-31b4-bdc9-65a78be52a97 | -6.82003 | -38.52529 | 2026-10-05 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4911e734-5fb9-3ad0-b3dc-de44c418bc97 | -4.30387 | -50.7808 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 34e30692-493c-313f-85b7-88a68373ccf8 | -4.1091 | -49.07652 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bcf75e7-094a-3d22-a058-63e7d4a1551b | -9.77627 | -44.79779 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2bd334-404c-3eeb-b674-55b9a15c818e | -6.18379 | -52.93622 | 2026-10-05 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9d60633b-7764-3a1e-962f-b09fb5836bc1 | -3.27969 | -50.02011 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ecf84c8-dd57-3765-8548-b118adb45749 | -3.61308 | -50.97686 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31fd2954-3fae-31d5-be9f-c38b276da011 | -6.65919 | -35.07319 | 2026-10-05 04:02:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b192452d-da5f-32ad-8533-be66198dfbc8 | -4.30113 | -50.78739 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 681d19c8-476a-3ef4-b0f8-f27aa345658c | -3.70609 | -50.65664 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d1d3510-ca81-3d80-9e83-bdf571db6b70 | -6.06571 | -42.91129 | 2026-10-05 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a96f1de2-e7d5-337a-8265-9e1d20555dcc | -3.27449 | -50.01513 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b188d090-5c9c-348d-a77a-1def51ca0121 | -6.82285 | -38.52952 | 2026-10-05 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a7c4bf3-9260-3e8c-b09b-09d30922d975 | -6.7144 | -45.98417 | 2026-10-05 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83692ac3-83e1-325f-a236-568b00fbe90c | -6.00222 | -53.52532 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed3a07f0-cf7e-38d7-ba77-0328b28633f7 | -7.89392 | -44.19011 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ae2b7653-cf00-362e-91ae-fc61692bc653 | -7.71672 | -45.46205 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7f5a647-f417-3ef0-87cf-f6cae04f93c5 | -6.91824 | -43.68263 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c87bd11-0ef9-3613-bbf3-a315b1d08979 | -3.47452 | -50.10369 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc0ef5be-447a-3ee4-b378-f47046866353 | -6.63998 | -39.05648 | 2026-10-05 04:02:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93e85c35-84b1-32a6-862d-0b74f7e85beb | -8.86521 | -45.38291 | 2026-10-05 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c472ffbf-d746-3237-b1a6-f06e58ca877d | -2.85099 | -51.2996 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 801ef313-f43d-3124-b1d6-e79e93da0543 | -6.9303 | -43.67883 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 867abddc-02f2-3d0f-a7e6-6ba08065c7e9 | -3.47572 | -50.08964 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e61c527-6852-3fa4-8a4a-a5475ba134a8 | -3.07305 | -49.54041 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8236235c-3d43-3bb9-a924-c4cf09e1ff18 | -9.23391 | -46.68716 | 2026-10-05 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02f6d8d0-3743-3ee5-a3cf-b9d7fecf7d9d | -6.06574 | -42.91021 | 2026-10-05 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 3599a7a9-2b88-3b17-abee-06d9d77cdc2c | -6.59888 | -41.5628 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9d3c822-de63-3c4d-a784-e5a437ab9bb1 | -6.62314 | -41.76992 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f747de8-5d6e-3d0c-8e57-4b25d1451021 | -6.89496 | -43.68764 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ec753c65-b7f0-349e-9c4e-dd75d3852991 | -9.81527 | -44.80216 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78103395-da9f-3241-b11a-0b39eabb47a9 | -10.96922 | -45.43254 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d0fdd59-850f-3045-abf2-46d0b97a6e1b | -4.30795 | -50.78388 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a60b5573-2177-321e-a40d-78d2996ff43a | -10.73969 | -45.29372 | 2026-10-05 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da23ffa7-eb78-3849-9a73-4206fbdcc646 | -3.40056 | -50.14835 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1355d3-ae02-3415-a32b-41ee3991d9dc | -4.30225 | -50.78994 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7b589f0c-2513-3300-baad-629342997701 | -6.9 | -43.67961 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 276f7aba-3e6a-3e8f-9c3d-17be4a4126a3 | -2.57927 | -51.87691 | 2026-10-05 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84b42063-4024-3def-b289-414f986568ae | -2.59072 | -51.84941 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a02a4f7-2e96-3b3d-acb1-b28dd247bfaa | -3.47074 | -50.09007 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 565c481a-aab5-34d8-99c7-e3a25fe236d0 | -6.90365 | -43.68019 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a0b97f3b-b9ce-3620-826b-386b83710b91 | -3.71178 | -50.65075 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b5d90eb-6390-3b0a-8227-44203f8a40d2 | -6.92958 | -43.68312 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e776d9b5-7c5d-3056-a13c-d4def0e5b7a8 | -2.75396 | -51.55419 | 2026-10-05 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12e694b3-289e-356e-ac5c-1bc1108d3e9b | -6.90434 | -43.67592 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8229f427-dfb2-3fd4-867c-4413fa8a38a3 | -3.84992 | -50.31883 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9bee6558-1484-396f-9dd4-26ec097724e9 | -6.01037 | -53.52008 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb70fb05-5901-3c60-86a1-6d653ef02ec8 | -3.80636 | -47.49109 | 2026-10-05 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b51ff8d1-596b-3a98-8c76-b5df4727d797 | -7.11243 | -37.60268 | 2026-10-05 04:02:00 | NOAA-21 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 09f8d3fa-9a00-338d-b587-37e16c393b17 | -4.11572 | -49.07039 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7201a5d-7696-3789-93b1-70ea2322863c | -4.64661 | -46.31285 | 2026-10-05 04:02:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9edb6db-a6b6-397d-afe2-4d05c4808ca2 | -10.95647 | -45.41512 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f07396d-91cf-3727-b41f-33a71c019320 | -3.84654 | -50.32602 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e7d44c42-9bb7-303b-8a71-fe980e24696d | -3.46696 | -50.1054 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b40212-4ef0-3658-aa82-3fcf3828e3ac | -6.93395 | -43.67939 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a5ec9f70-3051-39ba-950b-ea855c238b44 | -7.26629 | -44.29888 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f9f91d-d71b-3a01-857b-1b3ac7bfaad7 | -6.91935 | -43.6771 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f324155f-1a03-372b-bbcb-5cecefbdca07 | -5.94602 | -41.32051 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4aa24b53-042b-3252-9655-b1cef57cf034 | -6.60852 | -37.88759 | 2026-10-05 04:02:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9f77e66a-b172-3705-b9a2-1f72f890e208 | -9.2346 | -46.68312 | 2026-10-05 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c664a5a-46ef-31f7-9d99-4801ed6f1e9d | -6.61074 | -37.89624 | 2026-10-05 04:02:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9c9d0a64-c1ea-3ab0-9715-76e7a7d813a2 | -4.07879 | -48.96133 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cc3cbb7-3724-33b5-8821-52954779b2ab | -3.46915 | -50.09277 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78c7fbaf-3511-35fe-87d3-5424a0da6e1c | -10.96542 | -45.43176 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e2eb43d-e9d8-3056-b816-abc28b2ac5e1 | -3.83868 | -50.31332 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
