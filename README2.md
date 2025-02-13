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
| 26f96fca-c6bc-366d-bb2b-a1f7890f1456 | -8.11326 | -38.89425 | 2025-02-13 03:40:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b0009647-162a-30fd-b94b-2ea8d87bd8c7 | -8.95688 | -40.57833 | 2025-02-13 03:40:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c7ef04c5-b0c6-3531-857a-29306199fa11 | -6.51034 | -37.41782 | 2025-02-13 03:40:00 | NOAA-20 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59645952-5bcd-3c6b-86cd-989a3e9aa089 | -9.45156 | -35.57597 | 2025-02-13 03:40:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd5d8268-7636-3614-ad3c-51b5c436534a | -8.63285 | -40.44659 | 2025-02-13 03:40:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a2b8010-5e00-3323-b15e-53d07dcce2be | -9.00607 | -37.30528 | 2025-02-13 03:40:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b58fc7ce-ac48-3a4a-9832-b8363fea5990 | -9.47142 | -37.76503 | 2025-02-13 03:40:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8ae55699-03eb-3d3a-868d-0401fc469d09 | -7.39025 | -35.2494 | 2025-02-13 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5c98063-62f7-39d1-8d02-69b6d573bdce | -6.59822 | -39.38692 | 2025-02-13 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5cb5d97b-25c8-3880-ad9e-fc8cc6eaa9a1 | -7.04268 | -34.97449 | 2025-02-13 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bb061fd6-fdb1-3f54-ad0d-a7bb649cfe3e | -7.38586 | -35.25581 | 2025-02-13 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9c21920e-dc50-3896-8235-0bfe0e6dc590 | -5.14638 | -39.71972 | 2025-02-13 03:40:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f6af421-eb41-3d3e-a65d-d27bc96337d4 | -7.25194 | -34.93953 | 2025-02-13 03:40:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3034c26a-480c-3817-bfed-fd624c5ceb53 | -7.04213 | -34.97796 | 2025-02-13 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1057058c-b9d3-3183-8347-ede1d39d41a7 | -6.59901 | -39.38226 | 2025-02-13 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b23878bf-a870-3969-8f8c-bf9fd74e73d6 | -6.34395 | -41.91986 | 2025-02-13 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3dc5a6ba-3e62-33f1-907a-00b79df7fcd2 | -9.34125 | -36.87429 | 2025-02-13 03:40:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0e2da84-76a9-3d06-a8de-7474af1cc7be | -6.59521 | -39.38162 | 2025-02-13 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 362940a5-1364-3ed8-afc1-982ab601a2f5 | -8.10963 | -38.89365 | 2025-02-13 03:40:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b7e9ede8-d16e-3258-9950-3ef3cdad4160 | -6.99087 | -34.98056 | 2025-02-13 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f7540d0-55cb-38f9-8fc1-e63cb2a8f673 | -7.43763 | -38.06618 | 2025-02-13 03:40:00 | NOAA-20 | PEDRA BRANCA | PARAÍBA | Brasil | 2511004 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1519a28-dff2-3544-938a-5c38bf652aa4 | -10.4248 | -40.42855 | 2025-02-13 03:42:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b793833b-edb4-32ba-9ecb-1dc4bb36f5ae | -10.53503 | -44.67603 | 2025-02-13 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02c95647-78a6-38fa-8079-eba2b68185e2 | -9.44037 | -40.57324 | 2025-02-13 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f69e5768-82df-33e2-876a-8bc0a373f086 | -13.55611 | -41.84628 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2d9097f-de92-3e98-b63b-b727ea68c7c0 | -8.71915 | -44.00846 | 2025-02-13 03:42:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e43a5338-853a-37dc-a480-8ce11b10a2c0 | -10.53446 | -44.67902 | 2025-02-13 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc0bacec-cf55-3d46-bbbb-12ffc4e0ba7f | -10.53094 | -44.6767 | 2025-02-13 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdca2e7c-83f9-339b-9707-9254840e168e | -12.41877 | -43.80428 | 2025-02-13 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea8a20fe-236b-3c0b-8d31-eb3cb28208e4 | -10.69592 | -37.0505 | 2025-02-13 03:42:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95a6ca58-af2c-38b6-8040-14d3c630236d | -12.76523 | -39.80869 | 2025-02-13 03:42:00 | NOAA-20 | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da4a7544-ffdd-3f35-8776-7df804ad62af | -13.27675 | -39.69898 | 2025-02-13 03:42:00 | NOAA-20 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 185e4c05-c2d9-36fe-abc0-200d2acff794 | -14.9626 | -42.89038 | 2025-02-13 03:42:00 | NOAA-20 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c50193d9-8608-3bea-983c-fe532070b40c | -10.53148 | -44.67369 | 2025-02-13 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bdb3a68-dea0-3713-8882-80253a3536cd | -9.23832 | -40.55405 | 2025-02-13 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a85e464b-b59f-3d71-b707-8a662b7c42c1 | -10.57594 | -36.80302 | 2025-02-13 03:42:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37109a48-4a68-3083-aec7-3ecf5636388a | -8.72433 | -44.00971 | 2025-02-13 03:42:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f951acee-5011-3088-9d96-0058e0137235 | -13.5607 | -41.84357 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f9fa38f-46fb-3a88-b388-b484566435ba | -10.42587 | -40.43106 | 2025-02-13 03:42:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f7c6f40-f021-3047-b4df-2af954239c0d | -9.43646 | -40.57254 | 2025-02-13 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5237fc3-cfc4-3356-9f4f-06423da24ba9 | -10.53559 | -44.67302 | 2025-02-13 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82eb543b-079c-3245-aa43-119a68ba5f26 | -8.71935 | -44.00876 | 2025-02-13 03:42:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35fc6d49-4810-325b-965a-ad8ca6dfd5cf | -9.77924 | -36.91969 | 2025-02-13 03:42:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b97c43f0-50a0-3302-8147-741783cd1ec0 | -9.83688 | -37.17398 | 2025-02-13 03:42:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 40d35fca-5ff3-3d19-9ce7-1410307d1b3a | -10.32386 | -37.08464 | 2025-02-13 03:42:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c04986a3-2c0e-3790-94f5-9fc54b6aae37 | -13.56407 | -41.84765 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0faa524b-c1ad-3214-9330-d2ee484cefe1 | -12.86148 | -38.36709 | 2025-02-13 03:42:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1eff4fc2-059c-3ed9-a832-b8c19c674841 | -10.65299 | -44.48788 | 2025-02-13 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b330e36-e553-34d4-bd4f-a98078912b6e | -13.5653 | -41.84087 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7c094454-5388-340c-9f6d-7ee4ca2d70d5 | -13.55672 | -41.84287 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f1c7b0dd-482e-3566-956e-46a43ed2fb36 | -10.65195 | -44.49361 | 2025-02-13 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7dd14c3-b703-352e-9222-6e28e93f8504 | -13.56009 | -41.84697 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6dc88080-783a-3c65-9b45-d1123c2daeb4 | -13.56132 | -41.84014 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 90d50c7a-9a3e-371f-96b1-fb06fee2ee4f | -12.41418 | -43.80333 | 2025-02-13 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84365bf1-09ba-3e66-bce1-66cb5ac4262c | -13.56468 | -41.84427 | 2025-02-13 03:42:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 974ae4dc-4bd1-3e71-a53e-656756e79c34 | -12.66121 | -45.03961 | 2025-02-13 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dae2fae-4620-30a0-9fc5-ebb9dd018741 | -19.16475 | -40.1408 | 2025-02-13 03:44:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5d425874-2308-3659-bd39-4caad18559ba | -17.22062 | -44.43347 | 2025-02-13 03:44:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74a9f916-d177-3f04-9d64-6f2af570a90b | -22.73786 | -42.95863 | 2025-02-13 03:44:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2e643246-7951-37e6-8cf5-f62d7619942f | -17.22105 | -44.43586 | 2025-02-13 03:44:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5aadc8-d397-30f1-b8a2-7469deee3119 | -19.83829 | -40.08189 | 2025-02-13 03:44:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b9355d55-c929-3504-aa1c-88d094e99e9e | -20.95057 | -43.17221 | 2025-02-13 03:44:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 84c49f71-f8d9-3bb8-9304-c01729bc0a75 | -18.13682 | -40.83088 | 2025-02-13 03:44:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8857d80-40db-3a31-9db6-cb5ce2dd3570 | -20.94905 | -43.16998 | 2025-02-13 03:44:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0d58cf67-2ba2-3070-a47f-1afd492c1102 | -21.17909 | -43.98011 | 2025-02-13 03:44:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4522c45c-3b5a-34db-aa4e-2805b39711ae | -6.82106 | -45.4963 | 2025-02-13 04:31:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f0e2343-49f8-3499-9cc7-f5b535de53fd | -8.95423 | -40.57878 | 2025-02-13 04:31:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f363bdd1-fadc-3eef-91cd-dfb231c85deb | -5.85638 | -44.24471 | 2025-02-13 04:31:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d2f1805-4d4b-314a-a457-7fd8acc50e98 | -6.3443 | -41.91792 | 2025-02-13 04:31:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67b34118-4bd3-3b51-bab7-d51ef9083ca7 | -5.85209 | -44.24842 | 2025-02-13 04:31:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78d859e5-178d-34dd-92ee-57884f4036ce | -8.11454 | -38.89587 | 2025-02-13 04:31:00 | NOAA-21 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73147cdc-99f8-338f-98ad-6512cd77f2bd | -5.85273 | -44.24415 | 2025-02-13 04:31:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adb09a29-311a-378d-8917-73e45b4bcae5 | -7.54381 | -45.86776 | 2025-02-13 04:31:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d76839-f9f1-3c98-84dc-814ff8e218c2 | -6.60069 | -39.38212 | 2025-02-13 04:31:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fea8d53a-cd3c-318a-969d-d461b2b4fec9 | -8.11683 | -43.1183 | 2025-02-13 04:31:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af579521-218d-3b0f-8c7b-791f48a19ffa | -6.60026 | -39.38517 | 2025-02-13 04:31:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f792bc63-aa05-3934-8ca2-23f6bc0f1f00 | -7.5484 | -45.86063 | 2025-02-13 04:31:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d4bfbb8-fad4-3659-bd94-a0073a92511c | -4.55282 | -43.57783 | 2025-02-13 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51507bad-3912-3480-9192-2003808a9873 | -8.18331 | -44.49572 | 2025-02-13 04:31:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d55adae5-2a63-3e1b-b710-dd06677f2065 | -7.25296 | -45.70427 | 2025-02-13 04:31:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f724987-2cca-3ade-8ede-7b43a296c9fa | -7.14252 | -45.2784 | 2025-02-13 04:31:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce91f967-7bc4-3a3e-9a9d-ef8d84b3b51b | -12.64222 | -43.8104 | 2025-02-13 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8465f2c4-ac0a-3235-a557-2190c78fa840 | -12.9038 | -45.08207 | 2025-02-13 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4691990-1db7-39bd-af19-5dd2cbf81334 | -12.7575 | -49.32098 | 2025-02-13 04:33:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8802efdd-b538-3c6e-96b3-f03d12cf411b | -11.59391 | -44.85704 | 2025-02-13 04:33:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e862da7b-3834-3b69-ad43-bf0314650a95 | -9.24037 | -40.55008 | 2025-02-13 04:33:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b51b409c-9eea-3d80-b85d-a8a0227799ec | -11.88407 | -44.37863 | 2025-02-13 04:33:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5c5d239-9df4-394e-8aed-7fe83b4476e6 | -12.41899 | -43.80278 | 2025-02-13 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30e1204d-f399-37bb-8df5-3dd28a6e136a | -10.47736 | -42.46906 | 2025-02-13 04:33:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c2de3a6-7d2e-3943-8911-9ba9ee79ed87 | -12.41489 | -43.80221 | 2025-02-13 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c89bc62-6b50-3f86-ab99-0b14b0a00d4e | -15.57028 | -47.85576 | 2025-02-13 04:33:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0913910a-c296-3a60-ab5d-4f045af029a6 | -12.34497 | -45.18054 | 2025-02-13 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4856c7ac-7a1d-3d5f-b5b4-c4258712294e | -13.56349 | -41.84235 | 2025-02-13 04:33:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 90da704d-5123-3dda-9bc0-052953f98cfe | -12.65996 | -45.05582 | 2025-02-13 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0d0394a-3374-3976-9d65-674f26a4b412 | -12.66259 | -45.03682 | 2025-02-13 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1775f28-125d-3dbd-bd5a-e4230ccf8e66 | -10.653 | -44.48933 | 2025-02-13 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b673de0d-9020-3156-8c9d-fbc3d7bd1d0a | -15.1668 | -45.64682 | 2025-02-13 04:33:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf40fa51-2866-3b1f-83d8-29b3295c8d6f | -10.53715 | -44.67431 | 2025-02-13 04:33:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fcd57d7-e56f-3455-a074-3fcde459be61 | -10.77178 | -44.73785 | 2025-02-13 04:33:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e821ace-1f08-3c03-ab5d-984c2d696089 | -9.43933 | -40.57284 | 2025-02-13 04:33:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
