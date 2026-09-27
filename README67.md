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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe602afd-e5eb-3869-98ca-5d4a3a5f8c11 | -11.7322 | -50.6158 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7fa4322f-94d2-31de-b1d7-aa6092a83816 | -12.2723 | -50.1657 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e6777b81-15b9-3632-b84b-b15ccbd8e9f0 | -11.7141 | -50.5538 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ee39bcc8-181d-341d-9e02-5150d45aa644 | -10.6889 | -50.6658 | 2026-09-27 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| bcc01798-6995-3d2b-9ab1-a1fb565cb442 | -11.2853 | -51.3454 | 2026-09-27 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 5dcd91a9-d810-35a1-977b-b31ca13d318e | -13.3247 | -51.3211 | 2026-09-27 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 63d31c82-8346-32e2-8ef9-36a44c377123 | -11.6764 | -50.5367 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 46879892-b699-3f38-b212-12aa494a877b | -12.7225 | -47.2937 | 2026-09-27 17:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 227ab47b-3179-345c-9e59-0622ec58a3c9 | -11.2859 | -51.3031 | 2026-09-27 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 5d96f64d-6831-317b-bfc7-6d1cc3255646 | -11.1714 | -50.0151 | 2026-09-27 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 054121c2-57f4-343f-9939-346d02ac5de3 | -12.0178 | -50.6041 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b19bd625-30cf-3c5d-b965-b3b250f8531e | -11.0991 | -54.0285 | 2026-09-27 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 91616f0d-7f0c-38db-b82a-7593a64d7201 | -11.1178 | -51.1304 | 2026-09-27 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 2fb292cc-5428-36d1-a2a8-cb4f72797c3e | -11.0424 | -54.0336 | 2026-09-27 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 554.3 |
| 9d3b1d0f-22ee-37da-ba0e-64afe5b8d3dc | -11.247 | -51.3706 | 2026-09-27 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| da54a4a1-f610-351c-a9c9-0ac2653eeb0b | -11.1524 | -50.0172 | 2026-09-27 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8e955a98-eb53-317f-981b-172f42b7c393 | -12.1106 | -50.7643 | 2026-09-27 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| ac7113c9-1374-3882-b1cd-6e791df3f784 | -13.3439 | -51.3187 | 2026-09-27 17:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 02d86c60-dc73-37f5-ae6c-57ce2b6e54f0 | -11.3037 | -51.3858 | 2026-09-27 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 35f3d24b-bb3a-3e95-9c5e-6ff85b9386ec | -12.2887 | -50.3358 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2deb5d5a-900a-31c2-838e-5f2c58db7d46 | -12.8662 | -44.7579 | 2026-09-27 17:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| afb8ee81-8815-3510-bffd-b6099a6b28a9 | -11.2663 | -51.3475 | 2026-09-27 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 85718449-70e1-324c-9220-5216ad52f6c2 | -12.4351 | -44.1497 | 2026-09-27 17:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 851.2 |
| a7335683-9a96-3bad-951f-866689cc6060 | -12.2699 | -50.3166 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c7ec806a-06d8-3802-ad4f-13adcc787979 | -11.8672 | -50.4933 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7cf05354-0005-30c9-bee8-b4ab27e7aeea | -13.2057 | -51.5703 | 2026-09-27 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7cea917b-a17c-3a01-bba6-a829f1673961 | -12.1109 | -50.7429 | 2026-09-27 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 48da0cdf-cd55-3b5b-b90b-cf5598e6b18b | -12.2639 | -50.7034 | 2026-09-27 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 639ec986-35ab-3260-86b6-a4fb77c95934 | -12.1188 | -50.2274 | 2026-09-27 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |


