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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c3c1a36-07e9-3f7f-9aea-9335ad6063c2 | -10.48712 | -43.42873 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 79949732-1226-3566-bdf3-8bfcbc0a9871 | -7.35066 | -43.85473 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 41355b1b-ee3f-3e88-84aa-93bc3ff23da0 | -13.13037 | -48.03366 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e75a5e-1d56-378b-a1d4-40dd16227ab3 | -7.34415 | -43.86178 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3ebbc081-05c0-3435-aa27-418e99d65ee3 | -12.1604 | -45.09023 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 42c9b164-36d4-3aaa-a3dd-f0dbc15e1cd2 | -10.74583 | -47.29805 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e871465-5011-3904-b46e-9bf13ab0e49e | -10.63216 | -42.30231 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7b633830-f3b6-3cb2-9a01-194f93a4f2b2 | -11.32623 | -44.93528 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e388b2c8-6084-3ee4-a699-34bc1a4ef230 | -7.39815 | -44.7542 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9ba1d779-da1a-3d3c-97be-f32b1d8ccb6f | -8.36564 | -46.20191 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc4f6059-d2b0-372e-8a18-98d10321562f | -10.79147 | -44.0934 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d344665-6b12-37f5-8e7f-212e78ff8a04 | -10.24838 | -44.06232 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6c590c-d83f-34b9-b584-4cc3ae558489 | -10.25047 | -44.04959 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7491b144-d6c7-37d4-8a4d-c6715cea92b1 | -12.15608 | -45.07097 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ae13d5a-5bc0-3545-93db-1e666ef7dfb0 | -10.52262 | -43.40962 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8f334df-42f2-39e1-9679-f46bde32cff1 | -12.39498 | -47.20343 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b1e3aab-cd81-3b4c-91a9-9bf15584f41a | -10.63274 | -42.29868 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6206556f-2070-309f-8e6a-6ba4d9ee720e | -10.7111 | -44.55227 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c686b9b6-46ae-3634-8240-3baece880a74 | -10.70437 | -44.55289 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f44cdb58-a77a-3d1f-ae20-68b2f00595b4 | -8.53795 | -49.59814 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cde1b7a-a975-36d0-9ff9-f20d23b35a5d | -9.61443 | -49.02482 | 2025-10-18 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 262c4258-71ee-363d-b223-755158928545 | -13.03541 | -46.94303 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bdb1e92a-0c11-38c0-b728-bee89a4f7cc9 | -10.49014 | -43.45375 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beb94d2a-ca5d-3c29-bda3-408b54a4e03c | -7.14346 | -46.42552 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3707a34f-fade-3819-9d20-a7b13e21ce4f | -11.00215 | -47.90069 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13583903-6745-34b2-bc17-b967abcd263a | -11.38183 | -44.25248 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9e07bcc-c03c-32b1-a656-0b59b174a3eb | -10.14537 | -44.52574 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 701b9aa4-b9b5-3200-922f-5be980c43712 | -7.44922 | -42.68391 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 563f5152-ed85-3cc7-8399-bb79d68722a9 | -13.02654 | -46.94514 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 62c52ceb-89a6-3679-aa80-f712b5e6eaf2 | -7.24855 | -49.51742 | 2025-10-18 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeec4b69-70d9-3e5e-a983-ee1d21701921 | -12.39426 | -47.20744 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ed9513d-79e6-3964-bdd9-280d97337f0e | -13.53478 | -48.00589 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1396b6e4-6db9-3b1a-bf82-7e185146d8b1 | -10.93154 | -47.55473 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e59dbfb1-09b4-308f-9929-2811fb333fde | -11.09557 | -44.70597 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c83f43af-185b-3e48-a625-eccd5e42feca | -10.41908 | -44.91142 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8b8842a-bdfc-3964-9081-ef383a6b3a13 | -6.97561 | -44.86929 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28eadd1b-e595-3bf0-a408-68a8fcc609ae | -10.42901 | -45.01288 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 730c89f1-5b85-3bf1-9e85-d3e98ec49a34 | -12.20683 | -43.55664 | 2025-10-18 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4811dd0d-b6aa-3631-9ef4-ff90062c6497 | -11.61609 | -44.08843 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e0453a17-adee-3945-84a0-0a8c95225366 | -10.48995 | -43.43329 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c1965382-4a04-3354-b665-89468acbe735 | -12.16132 | -45.06282 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0c666a-3ea3-3579-a30f-ccf6339f12ea | -12.57047 | -43.76564 | 2025-10-18 04:02:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c540cea-01e7-3df2-bc48-abe210293353 | -13.49102 | -43.63961 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02a04b19-0155-3e60-8482-b56a9553d84f | -8.09575 | -45.44272 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7eda5898-2431-3648-ae34-95a4c3d0e0c8 | -6.93688 | -43.69826 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ba7565d-01c7-3392-92d9-3c899fa54965 | -8.3954 | -46.2312 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64e0cc54-c789-3990-957e-d65d859f0491 | -12.5062 | -43.04466 | 2025-10-18 04:02:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d641fa49-06a7-3a7d-b0c7-db1e82246c61 | -10.24042 | -44.06558 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c2b86a23-7ef2-35fd-a234-d8547492d11c | -7.47174 | -42.74395 | 2025-10-18 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b60e8708-e102-3ac4-ad43-4f9b2536b6d5 | -11.45771 | -44.20786 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65b9684f-7702-38cf-8192-64359e40030f | -8.35797 | -46.22076 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5af23ec4-09a0-3975-8c67-863b2e6d7142 | -11.19963 | -47.82933 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fe17da72-d1b1-354f-b57f-2ff6349b318f | -14.48799 | -44.60403 | 2025-10-18 04:02:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b27f14e-cf80-36ff-99c9-895b681e3b82 | -12.39004 | -47.20667 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27106ff2-39ba-3193-af0e-074717afd35d | -7.17702 | -42.17741 | 2025-10-18 04:02:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9be1a6e5-7b30-3d40-8d46-5eb9ef4d180c | -11.00049 | -47.9101 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58c393e1-f2b3-31c8-a832-3000fc5287d3 | -8.53874 | -50.08208 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf41becb-804c-38d9-878e-b6b9003bbc7a | -12.91771 | -48.57903 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9aafd1ec-3d9c-3a98-a115-dda7e39d62b6 | -8.09615 | -44.1068 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e5099d7d-380c-34c8-bef4-886b56501724 | -9.0101 | -47.84258 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afc6e053-ded6-3e46-8093-df3cd4e31cb5 | -13.30164 | -40.5597 | 2025-10-18 04:02:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 616bb180-40e2-38ed-9658-6ebb8cf48ebf | -10.15046 | -44.587 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b3980081-2ce3-30ec-a4c2-174522b5af08 | -10.74506 | -47.30241 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b754aa6-2da8-3fe5-9a77-eb9a5b1b4ee0 | -10.12198 | -44.61991 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55b439bb-69a6-32e3-a985-d6a538c8e222 | -7.23597 | -45.73409 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7427632-b996-3727-9156-f327cbb5f606 | -12.17466 | -45.07428 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5157ab2-ecac-38f9-91d3-063a2f748405 | -8.55121 | -50.07912 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15d7416b-254d-3b09-a448-b9ace5fbfb77 | -8.38129 | -46.23705 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e70536ec-e470-3733-abd2-2d4c61b3f771 | -11.3594 | -47.29179 | 2025-10-18 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf7a9091-fd17-30bb-9bf7-be418c4357e6 | -6.74148 | -47.37111 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be4d952-b47d-3869-ba07-6b4096d1b17a | -11.3646 | -44.26691 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaf61e51-e3c3-3f12-b9e8-82d8a6c8c9dd | -9.81474 | -47.75234 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0a18476-95c5-39f8-a929-799139f10743 | -10.49847 | -43.44697 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d822fbf-61e2-3438-be0a-c8463c9b5040 | -13.60513 | -42.42427 | 2025-10-18 04:02:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f38f913-7fea-375f-a9c5-da00b034bcf8 | -10.4282 | -45.0176 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9659f84-9a0e-3118-a6e9-e805d15f9274 | -10.50996 | -43.39937 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9014553-cfc5-387c-bb41-668c62b275e2 | -13.4268 | -47.97613 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15c0a6cb-8aeb-3691-a1fa-d5cddf4d7c89 | -10.29934 | -44.03127 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a8122fd-486a-333e-b167-7cbd41583016 | -11.00129 | -47.90558 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45016c95-bf3c-3fa1-9d5d-65474496db5c | -13.42022 | -46.69421 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e55ec90c-22f8-3aa6-9942-023ca360e357 | -10.48845 | -43.42071 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41cf48c0-22aa-3974-8891-71591f5ae18a | -7.66971 | -44.62929 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cec24d7-3a7b-3e42-98d1-0bb1bcbceec5 | -8.11037 | -45.43011 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 040d5d3f-4460-3286-a7ed-fa608d703664 | -7.16877 | -42.37811 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e828fd6c-e685-3518-9c10-34e13688700e | -11.20862 | -47.83102 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63eb2736-febb-35ae-aa9a-620d4cbb5282 | -13.04156 | -46.95598 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9e436c13-a69f-37c1-af65-f5695aaae08e | -12.17542 | -45.06989 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68a5fbd5-1951-321e-b262-bfe6dbdc6fa4 | -7.71599 | -47.85376 | 2025-10-18 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b49104e5-7d02-3b8e-b824-1530581d2695 | -10.84322 | -43.95046 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c62061a-ebb2-3079-a015-8a2d2dfd4ebc | -6.95189 | -44.87222 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90346029-ae35-3745-aaef-0228e9ccfba3 | -13.30109 | -40.56326 | 2025-10-18 04:02:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4bedb839-3c0a-343c-bda1-da0ededdf080 | -13.4209 | -47.98364 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdd8454e-44dc-3f0c-8bcb-a5bb796a9087 | -9.08063 | -48.0299 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cf6f4ec-4a27-3929-88ec-3d8a1e9e1a36 | -6.89232 | -45.45778 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48f5bbf4-8546-3c9e-9bc9-90e1171417cf | -8.82541 | -49.68148 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfe795d5-dd0b-3d99-9940-0456fe3e08c6 | -10.23167 | -44.05107 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d313e00-4647-353a-ad3d-08d8b14b7c83 | -10.08674 | -47.65968 | 2025-10-18 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f00dd067-0c8c-32a6-8487-e8857abb01b9 | -10.17395 | -43.89645 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c88b98f-accd-3a71-92a0-52845d4dfdfd | -9.24701 | -43.76245 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 080eea40-e980-311f-b52f-1b61af3a0eaa | -13.61374 | -43.9622 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
