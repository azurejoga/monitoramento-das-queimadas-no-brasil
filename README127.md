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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 370d5baa-7943-3fc9-8fcb-0eb90b7e70d7 | -7.7118 | -44.6451 | 2026-09-19 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 276.2 |
| 72ba0e5d-378c-3991-a130-a0ceefce645f | -12.3206 | -50.7394 | 2026-09-19 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 1273d326-efea-3e4b-9711-451c7d48072e | -6.1838 | -47.5258 | 2026-09-19 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 43fa3e0b-0efc-343e-a7f8-00eaef25f3b1 | -10.7715 | -46.3001 | 2026-09-19 16:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| e9d795fa-df70-383f-a26c-dae8491eb67f | -3.7311 | -60.6018 | 2026-09-19 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| cef6a39c-99c2-33a6-b649-f07f59c586c4 | -10.932 | -50.8742 | 2026-09-19 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 284.4 |
| e3a6b6d6-eab4-3719-bc02-c871a002f75c | -7.7844 | -44.8669 | 2026-09-19 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 33fcf19a-3c1e-3b82-8a8e-003497fcf72f | -2.6966 | -57.5889 | 2026-09-19 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e004e3f8-dcc3-3d34-aede-d0f86a724399 | -11.3437 | -44.0141 | 2026-09-19 16:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 4ad15013-699c-36bf-a68a-8503b951ae5a | -8.8639 | -45.937 | 2026-09-19 16:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| edc2c0c1-5bc2-3a63-9910-1aa464dcc6e5 | -11.8553 | -50.0221 | 2026-09-19 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 17621596-67e4-3cb3-aafb-e3a6676fb862 | -12.5032 | -50.0508 | 2026-09-19 16:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 469.2 |
| be49efd7-3549-33ac-a940-eab9d3b37b7d | -3.7311 | -60.6018 | 2026-09-19 16:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| d780a5ae-7f5c-3758-96de-bcf9af94a864 | -10.8367 | -50.9266 | 2026-09-19 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 0789001b-664d-3848-98cd-15ef5d298c73 | -10.6189 | -50.2466 | 2026-09-19 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 82d3d7f1-4a29-3b4b-aae8-2cde5a23e900 | -7.7844 | -44.8669 | 2026-09-19 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 50772e9c-c1f6-38c4-9220-045e87e16d34 | -11.8553 | -50.0221 | 2026-09-19 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| b1b1b01c-7a69-3ab7-a0c2-840b1f0957a3 | -10.913 | -50.8762 | 2026-09-19 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 3f0ca1b7-2ee3-3982-abc1-7d2b14cbcf16 | -6.1838 | -47.5258 | 2026-09-19 16:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 007b3e10-71e5-32da-a022-9e5f2f71f436 | -11.8549 | -50.0437 | 2026-09-19 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d0089c71-acc4-3da7-b833-ef6f03f9861c | -10.7923 | -46.1845 | 2026-09-19 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.5 |
| d41257ec-ce18-3a7f-9617-6d89595a1291 | -11.4715 | -50.2603 | 2026-09-19 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 87ba1197-6862-387e-9642-eb96e40c0fcf | -10.932 | -50.8742 | 2026-09-19 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 4ad7cce2-5ea5-3ea9-b286-029487851fde | -10.7997 | -50.8668 | 2026-09-19 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 8478ff1b-fc64-3d26-bf3a-344670e1d697 | 1.3817 | -56.0636 | 2026-09-19 16:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a3b85ee8-6a53-39a2-ba76-1f09ef62b9bf | -10.7994 | -50.8881 | 2026-09-19 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 3450000c-840b-3013-b51b-bb2d5075b2a7 | -10.7133 | -50.258 | 2026-09-19 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 19c58b19-95f0-316f-b952-72842ee5342d | -10.1145 | -48.4205 | 2026-09-19 16:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f734fdcd-6536-3a93-8d22-435a03ee48d1 | -10.7546 | -46.1667 | 2026-09-19 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 308.6 |
| b800cd6b-a6fc-3b4d-9ce0-6119b2971c56 | -6.1836 | -47.5477 | 2026-09-19 16:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 2ccfa077-b82d-3f1b-929f-a37889362d01 | -12.5032 | -50.0508 | 2026-09-19 16:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 289.7 |


