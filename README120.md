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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a49a5cb2-6987-3f23-b3ce-1bca53758202 | -6.5546 | -43.9221 | 2025-09-03 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0d230b34-1b7f-347c-9506-e66bc36cbff7 | -7.5302 | -47.4443 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| b2d4cda5-987d-3ff1-a4c6-e52ea8694884 | -5.8455 | -45.6421 | 2025-09-03 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ce588971-94a2-34c5-955e-246039afbc3f | -9.402 | -48.0585 | 2025-09-03 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9b90b6f0-1984-3b85-b534-83c1fb4a4f63 | -6.1234 | -45.9139 | 2025-09-03 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3288ce3a-bded-3a8c-9d41-a839c97aa890 | -6.8367 | -45.6784 | 2025-09-03 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0599152a-62bd-3f95-8697-49fad675be06 | -11.8708 | -51.5357 | 2025-09-03 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 93c12f94-2f1c-3481-9860-deef10d1100f | -8.8845 | -45.7994 | 2025-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0bd5e860-39d9-38d0-bc8a-79d4bcb28720 | -6.8279 | -52.8348 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fb3cc736-120d-3b5b-91b4-4babf0059c73 | -8.3832 | -48.3099 | 2025-09-03 14:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a8df3234-48ef-302a-bfb0-01294e07bc41 | -8.0197 | -44.1072 | 2025-09-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f59a0e5e-ec73-399d-9a10-de164f2813ad | -10.4632 | -53.6132 | 2025-09-03 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ecf6ec46-35b5-3758-8a08-af4417682918 | -10.4818 | -53.6321 | 2025-09-03 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f3ad3d34-e7d2-31ba-9c31-e6cbb517a3c0 | -8.0197 | -44.1072 | 2025-09-03 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 31b7e715-656e-3b73-9fc9-d138a6440311 | -7.0128 | -43.2525 | 2025-09-03 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| ff4cabd4-7aa7-311a-86a4-ac1d7704821d | -8.3834 | -48.2882 | 2025-09-03 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 42afc008-3f62-3858-8d9b-87d2fd94d858 | -12.6341 | -56.9926 | 2025-09-03 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5b0593e0-cf77-3cd2-9cf1-6513a5166c18 | -6.7741 | -44.4792 | 2025-09-03 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 62fd1abd-bc86-3df7-8e2f-91dec21b24ab | -9.6226 | -47.0861 | 2025-09-03 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 248.3 |
| ac055715-db2c-34dc-8a2c-ee504a496955 | -12.7926 | -47.6638 | 2025-09-03 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8d8da5d8-2fbc-3de1-9a4c-e65a4eee1b7c | -11.8843 | -50.6197 | 2025-09-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f187e0f7-5c36-3bcf-8d17-6178bfc29b77 | -25.0202 | -49.4037 | 2025-09-03 14:20:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 153.8 |
| 27397d14-e045-387a-a187-80a2c8228045 | -5.7922 | -43.2405 | 2025-09-03 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e6a56256-3837-31de-9ad8-dc1773e2847d | -13.5167 | -47.0167 | 2025-09-03 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 92a3c0c6-cdff-39d3-afca-420400494626 | -9.6232 | -47.0416 | 2025-09-03 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 38cb6698-312a-316f-bb68-bf8f0d6e35ca | -6.0699 | -45.6259 | 2025-09-03 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| b599577a-d028-3287-8f51-ee5805cc39ca | -8.0723 | -47.5946 | 2025-09-03 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 75aaf686-2956-3376-bc2c-cebb6839c1b5 | -5.2575 | -44.4581 | 2025-09-03 14:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| f9a41899-cec9-3fd7-8ab1-434f22750689 | -16.3145 | -52.9628 | 2025-09-03 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| bcc298cd-e913-310e-9783-8d6e2a899f36 | -7.3793 | -49.4075 | 2025-09-03 14:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 811c69c6-2498-3d8c-90b5-e97362fc9130 | -12.18 | -53.8836 | 2025-09-03 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 429308d2-2852-37ea-a6b6-086008b24e12 | -12.6339 | -57.0127 | 2025-09-03 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 0a841dcc-8238-394b-9594-3b8710725006 | -11.8537 | -51.4106 | 2025-09-03 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0ae1cc3b-4a63-3007-a1ac-84c3294aa35d | -6.6213 | -53.1536 | 2025-09-03 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 08d3aac9-8f1f-3e6e-ad53-0dd0774b654c | -10.913 | -50.8762 | 2025-09-03 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 1b0c11e1-805c-3279-b27d-65ac7776f3dc | -6.3315 | -45.6512 | 2025-09-03 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ae80cff4-2aab-3d2d-a18a-586178d25d14 | -10.9509 | -50.8722 | 2025-09-03 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a2b22825-6ba1-30b7-aad5-6dd78886a05a | -5.7736 | -45.3091 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 369.1 |
| f64818f0-b3df-388e-882e-8b5dfbbaa14b | -7.7036 | -48.7587 | 2025-09-03 14:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 115.2 |
| d4b9d5a8-558c-3d22-bf5b-d8fc1d78dc8d | -8.8278 | -45.8054 | 2025-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| dc6afdaa-c7e5-3f45-b92a-7d95ffeb2f07 | -8.2006 | -49.5559 | 2025-09-03 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 2e624be3-d822-32f8-81fb-7c2cb9c356d3 | -5.7738 | -45.2865 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 34e40251-15d9-32a9-bfc6-1041158f2284 | -8.8839 | -45.8446 | 2025-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0b46a4c1-d064-3b83-9b9e-d06c966b47a4 | -6.7407 | -45.911 | 2025-09-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d61154e8-3ef6-3b97-b917-b6a5803c238d | -15.737 | -53.635 | 2025-09-03 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6144ad17-d993-32eb-a184-620e88ff7e99 | -8.8842 | -45.822 | 2025-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d5d687f1-bc88-392f-b67f-f9fe4a7a8b5b | -11.9034 | -50.6175 | 2025-09-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5bd86c93-7f7c-3580-8d68-b092bd95b865 | -8.3646 | -48.2899 | 2025-09-03 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7801a9cb-7bbd-35e4-81e0-99c744c67a16 | -6.3689 | -45.6483 | 2025-09-03 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2f0e34a7-b16e-30e9-99ad-6e8ecf69f2df | -11.6647 | -57.3533 | 2025-09-03 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 6df7234b-5fb8-3085-b2eb-c8e8bf2af5cc | -7.5157 | -45.3478 | 2025-09-03 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 4006df88-ae46-37b3-8d2f-de5d0d7134d5 | -5.8297 | -45.3051 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 071290f0-9385-33a7-9c23-2ec60e8ad708 | -6.6538 | -45.2417 | 2025-09-03 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| dffd646c-a15c-3b9f-a880-bb9ce19904ac | -5.8882 | -42.9988 | 2025-09-03 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 202.7 |
| 34f1840f-7a58-3974-a4ee-27af9231f74b | -11.3893 | -43.6075 | 2025-09-03 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 018bf322-3cc2-3289-835b-de99eaac5e92 | -15.7175 | -53.6376 | 2025-09-03 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3d23d984-26a4-31c2-92d4-8cf25ffb4ec3 | -6.8569 | -45.5415 | 2025-09-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d31366f8-9485-344c-92b0-5d3acae21d5b | -6.2411 | -43.3677 | 2025-09-03 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 3d59525f-931f-33d6-9a03-ab23be5c879e | -8.3832 | -48.3099 | 2025-09-03 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d364bea9-966c-30f5-b819-7cad11e7daab | -10.0932 | -54.7667 | 2025-09-03 14:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 159.7 |
| e6c80ed9-8d3a-385a-895f-d69c85024527 | -7.7039 | -48.7371 | 2025-09-03 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 112.7 |
| a1e550e7-e046-35e5-89d2-6c5c6b670d85 | -6.35 | -45.6723 | 2025-09-03 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| edf879b7-16eb-3e73-a0b2-382a6a0f63ca | -5.7549 | -45.3105 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4bfbf3a2-0b69-3b93-869c-45a16ad34999 | -11.6836 | -57.3518 | 2025-09-03 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| e7d75815-2d62-35ec-8b67-cf187efc891c | -5.7181 | -45.2453 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a86b6634-b449-30fa-b40f-ec98e0e07b94 | -11.8533 | -51.4318 | 2025-09-03 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 27495d26-50dd-30e0-9510-4cd900626a06 | -5.7923 | -45.3078 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5233b1bd-ac70-3398-be86-4abb3a7a0937 | -11.2005 | -55.0195 | 2025-09-03 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 85d4d7ba-2af7-3dc1-b05c-0ec7f646a7e3 | -7.4842 | -44.8043 | 2025-09-03 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 828d5f9e-0a55-3fa1-842a-a6e787054b89 | -6.8466 | -52.8132 | 2025-09-03 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 95725f44-ca9f-37f3-b875-e90a0654458d | -6.8381 | -45.543 | 2025-09-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c4a294c5-e7c8-378b-9abc-65e697edee14 | -8.8845 | -45.7994 | 2025-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2ef9aba2-4105-3a34-ab68-df789b8a9302 | -6.7595 | -45.9095 | 2025-09-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 75f875d8-40d9-3d43-836d-577ce3e34496 | -5.7343 | -45.5375 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 680f7931-542a-31c0-a2b5-51769e315afd | -10.9326 | -50.8316 | 2025-09-03 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b7a481ee-52e2-3212-87df-4b10fc649526 | -7.484 | -44.8272 | 2025-09-03 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7dae74de-c67e-3f5b-ad19-25bb4efe4dfe | -5.5253 | -43.7489 | 2025-09-03 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 911bf13a-a302-3589-8667-8bfb30e149b1 | -12.1125 | -50.6358 | 2025-09-03 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 46a4a620-7ed7-3880-9897-049567bf3a9e | -5.8455 | -45.6421 | 2025-09-03 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c96a72e3-58ee-3004-b864-d9a732f77d6f | -10.4816 | -53.6527 | 2025-09-03 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4a6b5c10-0e91-3a0e-99a7-124385c50e27 | -10.5045 | -50.3226 | 2025-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 68fead73-1741-3d5a-af5b-416b6d638b52 | -11.3709 | -43.5631 | 2025-09-03 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 14df6fb3-0ac9-3fe5-8b5c-93febad3863d | -6.8279 | -52.8348 | 2025-09-03 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7a4b64ce-071a-3b68-92ed-aef34069cf0c | -8.3644 | -48.3116 | 2025-09-03 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 4f26a1ee-d5ce-379c-85a2-edc32a61fcc2 | -14.3952 | -51.7157 | 2025-09-03 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 063b587f-ac1a-39ee-b690-eaadf007bf2e | -6.3502 | -45.6498 | 2025-09-03 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 6d650800-ea1f-32c7-b58d-7eb94deaf197 | -9.636 | -46.1221 | 2025-09-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e08da75d-6db6-376e-a1be-04ffbb8cec76 | -11.3705 | -43.5868 | 2025-09-03 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 9a8aefb0-ac47-3ffe-ac7b-462d01f79130 | -11.0181 | -51.5001 | 2025-09-03 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 4c397069-bf6d-3ef8-abe8-708af9ae8213 | -9.402 | -48.0585 | 2025-09-03 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6ef8a1e2-2e53-3e36-ab85-2a8c687b9404 | -5.7154 | -45.5613 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 2fbe4232-26e9-3eed-9c6f-a97b741835c0 | -25.0418 | -49.398 | 2025-09-03 14:20:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 130.7 |
| 8492e12e-786e-35b8-ae14-ff4dcee77f25 | -12.9189 | -57.0074 | 2025-09-03 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 512aa68b-7d9a-3841-b0ab-855ed7fb162b | -7.5302 | -47.4443 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| bcc0e0d3-a277-3447-a82d-ea47f9ab0aa8 | -6.797 | -44.0859 | 2025-09-03 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 878fb1b7-fb2f-3601-8f98-df17bc4bcb3f | -6.7928 | -44.4776 | 2025-09-03 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| a22635c8-49f7-360f-963e-383edc05535b | -9.6415 | -47.084 | 2025-09-03 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ef4a0016-1560-35c4-b653-101c5ed90be2 | -5.829 | -45.3955 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 78939a9f-faaf-35cb-b4ce-5f13dbc59de6 | -7.549 | -47.4427 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 796f9d6c-2f7a-38a3-8b9e-8bb1125ecf70 | -6.7967 | -44.1091 | 2025-09-03 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |


[Clique aqui para ver as próximas entradas](README121.md)
