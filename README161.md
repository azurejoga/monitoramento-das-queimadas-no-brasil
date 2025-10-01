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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2235d653-518e-372d-8fa1-48add391554a | -6.6978 | -42.8118 | 2025-10-01 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| d5ecdbf1-e16b-30c4-a643-f4d1c886c53a | -7.2996 | -42.8722 | 2025-10-01 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 73d0cb5d-5b89-3a85-8335-ba80be07e8a8 | -9.1889 | -48.5166 | 2025-10-01 14:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| dfa85b02-d20f-33f3-b104-97b1bee5b845 | -15.5384 | -45.214 | 2025-10-01 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 133.1 |
| d39f63e6-b1b5-3cb1-896f-22fdbe88eb64 | -14.3519 | -45.9206 | 2025-10-01 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 199.9 |
| b770f9c3-97c1-3a1f-96a9-f75da4322c22 | -13.8062 | -51.2378 | 2025-10-01 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 3dd36474-c4da-30fe-98a8-81afb51ebb83 | -13.2969 | -50.6821 | 2025-10-01 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 82d2de23-7747-3a5a-b994-0a7697fd00c7 | -10.9182 | -44.3092 | 2025-10-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 9b6501e5-0c81-3d05-b014-476c00aad5e9 | -11.8482 | -48.0595 | 2025-10-01 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 8dd7610d-eab4-3fb0-a695-50528f6daa72 | -7.8165 | -46.9781 | 2025-10-01 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3d04e1af-e9a0-371f-aa89-0b58bee50e68 | -11.8246 | -44.9669 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 4d628941-e576-3c00-8466-59533bceb56e | -9.9959 | -43.6172 | 2025-10-01 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 6d7f58c7-5f90-3482-8b57-4d40c2d9911d | -11.0225 | -49.8167 | 2025-10-01 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 11c9175d-0b54-3016-9c15-508a595a5241 | -8.6911 | -47.6906 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 80ed1a95-2dfc-328e-8e9f-d3e77b0e0d2d | -13.9848 | -44.9176 | 2025-10-01 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1b0cf866-bed1-3355-a980-a51797f21a01 | -8.5773 | -44.7623 | 2025-10-01 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 7ec8af59-26a6-3000-9092-c7e0f5ef7317 | -11.8622 | -45.0075 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 05e36bc7-6aab-3807-959b-e3493d4166f7 | -16.0221 | -50.8989 | 2025-10-01 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 184.4 |
| da2fc9d6-b075-3c5f-9349-81c3e656be96 | -13.7876 | -47.9853 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a3968bf2-f68d-390f-8614-d207f3f2eacf | -11.4604 | -44.997 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 4ff0de16-e51a-3a10-b2b2-5a298bf71e55 | -13.6707 | -48.0476 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7e5759fa-5e70-3cfd-bf27-053b642b1403 | -9.4644 | -47.6124 | 2025-10-01 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 0595661f-fe0e-36f0-9fbe-772acb8c8dcd | -7.6272 | -45.4507 | 2025-10-01 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 8f5ba776-e1ae-3dbe-b810-06a3d8d4c56f | -6.2998 | -45.0433 | 2025-10-01 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 52d713f9-ec08-337b-8d51-9e675c28dffd | -9.1889 | -48.5166 | 2025-10-01 14:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| bc6f1531-efa4-3d4c-92ed-a79aeccccf56 | -14.3514 | -45.9437 | 2025-10-01 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 158.3 |
| e325f8f8-a6a7-3440-b428-dd6d7efefe3c | -7.5563 | -46.7573 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 328de499-d4e5-389c-b4bb-82ea216374bc | -15.1444 | -48.0143 | 2025-10-01 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| cb5b7eec-9a5c-39bd-9a62-bed69ab1c20e | -16.2742 | -42.5406 | 2025-10-01 14:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 57e04edd-c028-3c24-b933-deb37eae8e25 | -12.8831 | -46.9101 | 2025-10-01 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ca1154bb-c156-319b-a570-ab486f4ad9dc | -6.5417 | -45.2055 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 905364d2-623d-32e6-b5fe-b3b5949723db | -14.764 | -45.7552 | 2025-10-01 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 587572f6-6c68-3fd6-874d-0c6b3d3bbef9 | -5.2714 | -42.7873 | 2025-10-01 14:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 364d377c-6760-31f2-8280-87a7e59127bc | -5.4907 | -43.4264 | 2025-10-01 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 2426b375-36eb-3c41-aa81-78b81abf8630 | -14.9084 | -47.1965 | 2025-10-01 14:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 97242c0e-b26c-3cb9-bef5-cf76a638698d | -15.2823 | -47.9461 | 2025-10-01 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d2093f8f-c2f2-36db-b17a-c528a3a0a16a | -8.5016 | -47.8184 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 62ca327a-3b6f-370e-8799-df37c2585852 | -15.5384 | -45.214 | 2025-10-01 14:20:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 07d46b28-5879-31b2-9949-6689b3759768 | -13.768 | -51.2214 | 2025-10-01 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5fd62aee-f801-3b94-b756-fef386cb5006 | -8.4833 | -47.7763 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 73348d54-4782-37f6-82ef-db196440caca | -8.4827 | -47.8202 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6c3dfb8b-1af4-3583-b84a-5b9017044131 | -12.7819 | -50.5543 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 290.0 |
| a931cac3-f6ad-3118-abfc-d89ca0bbc991 | -12.3669 | -50.2187 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| cd3740fd-2f7c-35bf-96ef-4dbd626e2969 | -11.7797 | -47.5806 | 2025-10-01 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 46382914-256f-3ef1-ac1d-e815ec33ed72 | -9.9031 | -45.978 | 2025-10-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 7546b787-202e-3eb9-80f5-f11473047002 | -12.3863 | -50.1947 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 751f0885-9ea3-30e2-93c5-2582da93d038 | -12.7822 | -50.5328 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 680c77e5-0742-3309-bf69-5c6dc384d14b | -12.254 | -47.7837 | 2025-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| c48adbdf-00eb-38e6-9f6c-ddddf33fc878 | -13.3615 | -48.0936 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| b1c11783-131d-38bd-b47b-d5825217939d | -6.523 | -45.207 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 1f81efa3-bad4-3406-9076-7bf0652da145 | -6.5227 | -45.2297 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6dd9f497-b6a3-3e56-b1c3-bfcac3ac7971 | -9.4455 | -47.6144 | 2025-10-01 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 97f0f580-2fd0-39c2-ad8f-0c3967a3e29e | -11.9272 | -47.8941 | 2025-10-01 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 55a3ab37-552d-37e4-a381-dd2ef5f0cd93 | -5.8062 | -43.7512 | 2025-10-01 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 26039a66-9b38-39f2-81ed-744458d6390e | -13.3274 | -47.8536 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 02c3d78b-63d9-3342-a223-9a1c8be0cba7 | -8.2105 | -47.0084 | 2025-10-01 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| d3e54b55-004f-322e-b4a8-cee4dfab37b3 | -9.8842 | -45.9802 | 2025-10-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 223.2 |
| a8869502-44ff-3f9e-8687-512ac9011cc9 | -6.0625 | -42.4422 | 2025-10-01 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 14dbe384-4f0d-316c-9ed9-5a75c154a52c | -8.5081 | -47.2676 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ab92700d-4fc0-3dbb-88c8-385276a507fd | -8.8609 | -47.6521 | 2025-10-01 14:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2f96a777-bb8f-3be7-9aec-e42a932dbdfe | -5.9271 | -44.8671 | 2025-10-01 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 8485281c-e6a7-3742-8e1d-c4f9fa6e8c07 | -12.2153 | -47.8112 | 2025-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 116a438a-b716-3645-891f-431b309c47bc | -16.0217 | -50.9207 | 2025-10-01 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e29ae4c0-b46c-3cf9-8370-3febd9f39a19 | -9.9387 | -43.6248 | 2025-10-01 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 4c478259-23d3-3c62-a875-75fa74909cf7 | -6.5546 | -43.9221 | 2025-10-01 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 1eb7badd-980a-3af9-9638-b9d6d2981dd7 | -14.3524 | -45.8974 | 2025-10-01 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| d5eb8217-ca43-3f80-89f5-87e27f29170d | -14.1732 | -46.1124 | 2025-10-01 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d4c75bae-9374-3fb2-bbdd-9d2f43ece20e | -11.0988 | -49.7866 | 2025-10-01 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 276696ef-1d10-3347-aa52-80bfa75d80a6 | -14.9738 | -46.8668 | 2025-10-01 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| bb907d63-9ab9-3710-a63b-855847a431e6 | -11.1178 | -49.7845 | 2025-10-01 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 56c172e5-864d-3d2f-a589-294959218091 | -10.8242 | -45.3841 | 2025-10-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| bc723567-403a-38de-b1a2-04ce1e1dbcec | -7.8549 | -45.2702 | 2025-10-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c8ef23b4-4099-36fc-9447-7a1a283cbca6 | -14.9733 | -46.8896 | 2025-10-01 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 87c0d024-3362-38fe-add3-1bc2ad41a8fd | -6.2813 | -45.022 | 2025-10-01 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e1078da7-ddad-3b39-8a8b-1220e77eafa8 | -9.4194 | -54.697 | 2025-10-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4273a145-fc09-3ca5-964e-25b4cf55c147 | -5.9557 | -45.8588 | 2025-10-01 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 6c81b88c-cde9-3f60-9983-d71dcddefcf7 | -8.3869 | -47.9824 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b4270acf-2b59-3ca5-a46a-e7f4b0404cc7 | -14.8212 | -45.8143 | 2025-10-01 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 0073a161-ad25-32bc-a39b-0514f5962a75 | -11.4608 | -44.9739 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e9e9c545-f564-3135-aecb-aaddd3884cf8 | -6.079 | -42.6773 | 2025-10-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| f5a1d214-c55a-316b-a0d5-7eb350d876bd | -5.7581 | -42.8682 | 2025-10-01 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 86e47827-6675-3124-9588-0afbcefeedce | -13.327 | -47.876 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 64cf1ca2-648a-3ce5-971a-cdf957b47750 | -9.4115 | -47.3308 | 2025-10-01 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3ebb8598-1e3f-3f43-9a6f-272eeaedff36 | -6.7165 | -44.5987 | 2025-10-01 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 02077914-8c42-3aa3-92c0-6c3cf699ca50 | -13.2973 | -50.6605 | 2025-10-01 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 5ff686dd-81ab-3052-b687-53923539fff4 | -9.8845 | -45.9576 | 2025-10-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.8 |
| be256d83-5c6c-3589-bb2b-978ac6a424c0 | -5.1512 | -43.7289 | 2025-10-01 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| a3f01d1e-b417-3b02-985d-494d83a5aaf4 | -12.7627 | -50.5567 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 140cfc1c-b7db-34d0-8825-8be57ac9592d | -20.1379 | -46.3264 | 2025-10-01 14:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 2bcb1568-2192-3e7c-ae58-4d993282e12c | -14.3714 | -45.9172 | 2025-10-01 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 647f24cf-96a2-3386-bc88-f9b1bfc84a03 | -6.7624 | -45.617 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 5dadf0fa-b34d-3fbf-bdd5-f05d34bac67a | -8.8923 | -46.6519 | 2025-10-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 18702487-cf87-3a09-8096-56af38379fd1 | -5.3248 | -43.1118 | 2025-10-01 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 66eecdc7-3d19-368a-aa28-1ad6c1a15d23 | -11.8676 | -48.0348 | 2025-10-01 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b53c477d-a2f1-3ef5-96ce-f3169f1ad3c0 | -6.525 | -45.0025 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4926b771-de3a-338c-8893-b5f9bd5fd54d | -8.3867 | -48.0042 | 2025-10-01 14:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 42c13593-0d8c-36d6-bb77-a9451d8fbf9d | -8.8926 | -46.6296 | 2025-10-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 01867104-f224-315d-a701-0b7e6b1d1dcd | -8.8948 | -45.0253 | 2025-10-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a89075b1-7a65-374c-a34c-04a44463f9f0 | -5.2903 | -42.7624 | 2025-10-01 14:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| b23c4667-d8ff-3983-8b55-564e9e053bee | -10.8995 | -44.2886 | 2025-10-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |


[Clique aqui para ver as próximas entradas](README162.md)
