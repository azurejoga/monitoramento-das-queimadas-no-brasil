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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95e5a84a-5419-3b00-99de-e6bd95607ced | -10.06941 | -54.3665 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7564c644-6379-371e-a378-24de63f963b9 | -10.02568 | -54.33708 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2ad5594-b6ef-381c-9f4b-a1519f2048f8 | -10.02509 | -54.34094 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f29c285b-cf48-3301-85ee-7b65cb460301 | -10.02435 | -54.33612 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 417c2a9d-b205-3ac5-b31d-0ae1c4a440ad | -10.02378 | -54.33998 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86605bd7-5103-3c0c-99c6-c597e07248d3 | -10.02221 | -54.33661 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c11e04ca-8103-380c-8f25-bb4f13e801fc | -10.02162 | -54.34045 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6675807-f3da-3de3-8235-66ea9f5d797a | -9.65063 | -54.31317 | 2024-10-25 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f595ab92-d023-39b9-ab04-341526ad4b6a | -12.1567 | -55.42878 | 2024-10-25 05:04:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b68d1b7-8c49-3552-8a47-837f0bd99f09 | -12.14785 | -54.26358 | 2024-10-25 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 678736d8-879b-36f5-92a1-5ee8ab413bd5 | -12.03667 | -54.65548 | 2024-10-25 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8296e046-04ad-3577-95c9-abeadb4faf98 | -12.03559 | -54.65188 | 2024-10-25 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3c8d613-f8f1-38fe-848e-e3470d683a16 | -12.035 | -54.6558 | 2024-10-25 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ccc44cc-7415-341c-b678-f2b16b620575 | -11.9167 | -55.51295 | 2024-10-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3afffc1e-978d-35fe-9e84-f547331b0e1d | -11.89394 | -54.80222 | 2024-10-25 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8280dd96-e2e6-3212-9fb1-08ef8fd0971d | -11.35299 | -54.48471 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 411d8931-c7b3-3209-8c30-717d8a08d9cd | -11.34951 | -54.48419 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28f8f34f-f988-3da2-9a68-98a110d903f3 | -11.34892 | -54.48812 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a95c14f-0e68-38e5-a936-23f4193e9b3e | -11.34834 | -54.49205 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4df24294-97e8-3bd6-bb5d-554f9a12adf3 | -11.31404 | -54.33138 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e252a72-8464-34c2-b2e5-0a8cbed131ff | -11.31344 | -54.33535 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce460a1-c111-3a3b-b69e-180c02107b26 | -12.61783 | -55.22186 | 2024-10-25 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 311dfc3b-af18-30c3-999d-d19eb8284972 | -12.61726 | -55.22565 | 2024-10-25 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dce86b7-c0bb-3720-a337-2717697c48fd | -12.61384 | -55.22512 | 2024-10-25 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01668fc5-1202-3aa3-b077-7d7ba6f7c31d | -12.50281 | -54.35498 | 2024-10-25 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94009f1f-d90e-3a53-9ba5-ac837079d44e | -12.50221 | -54.35906 | 2024-10-25 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ba78ad-febb-392f-af51-5ebf2e6c9edf | -12.38835 | -55.60759 | 2024-10-25 05:04:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5eb5139-b6f4-3c6b-8ce0-201eea689d00 | -8.36442 | -55.1413 | 2024-10-25 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 143c8771-99ef-3f91-aa0f-cf7b59da8858 | -9.91885 | -56.25961 | 2024-10-25 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaadede7-5237-3671-8f28-23a3324fbe8f | -10.62238 | -55.90659 | 2024-10-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fd3489c-e255-3904-99ae-1dc1398ff14e | -10.61905 | -55.90606 | 2024-10-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a99f41a-3e76-3267-b333-f4d7cb16e900 | -10.48562 | -55.62257 | 2024-10-25 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41ac8d8b-e9c1-3c2c-be5e-5db9bf95547c | -10.48228 | -55.62205 | 2024-10-25 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78c60813-ab34-3fda-87ea-38df51833c99 | -10.4453 | -55.33284 | 2024-10-25 05:04:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c0fbe11-09fb-3815-84db-1714abc9d905 | -10.08696 | -55.38867 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7693c14-67a9-3d0a-be3d-b2b2d2ebd592 | -10.08361 | -55.38813 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37368c81-da6f-3d9c-a8d6-cdc2010b4baa | -10.08116 | -55.49416 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c63fd87d-6fec-3034-8a36-47a50dbeb266 | -10.07836 | -55.49007 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd0345cf-59cb-35c5-b118-d7bed900b7ec | -10.07781 | -55.49364 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0f99941-6899-3785-ba64-b4b981825915 | -10.07727 | -55.49721 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fbfc15e-5a47-3d77-8e0b-fd98b3546566 | -10.07502 | -55.48955 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7417d8f-20f0-3722-a55b-9528d16873c0 | -10.07447 | -55.49312 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b7ac26e-b203-35e2-b44d-c8ded2cb034f | -10.07112 | -55.4926 | 2024-10-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82716339-0840-38f8-a490-a8f53290e4e9 | -12.19045 | -56.63192 | 2024-10-25 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ed78d61-5842-3f04-89e9-2a0fcbb6e887 | -12.02464 | -57.08424 | 2024-10-25 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9155e26e-2ed5-3f6b-843d-28eaf724c3fa | -12.02409 | -57.08775 | 2024-10-25 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 434e0e93-c9b4-3641-9953-873bf7ff2d32 | -12.02354 | -57.09125 | 2024-10-25 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f71dd1a-fd0e-3e8a-ada8-407ce5f8f27a | -11.89329 | -57.05641 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c843811d-5c26-364d-8ec5-0180d2c69fb0 | -11.411 | -56.73067 | 2024-10-25 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba778d0e-6c73-3d7e-a51c-d786ef186f10 | -11.13668 | -56.79042 | 2024-10-25 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db9d5ab2-1ee5-3807-88a0-869d50fd7627 | -11.90237 | -56.40885 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c564fa4b-e379-35da-ad88-d6c76230543f | -11.90183 | -56.41239 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16a310ef-0af8-30b5-88b5-a9b9a197b433 | -11.89906 | -56.40832 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2bba886a-021b-3763-bfe0-fc8ff876c94f | -11.89851 | -56.41186 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a02ad4d1-ad4f-3864-83ed-7c8c6d9bb0d4 | -11.89574 | -56.40779 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36fd6c6f-a72a-3447-9664-039f81b8c9e8 | -11.89519 | -56.41133 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22d0196b-9576-3f86-99e4-ce3774422f5f | -11.89465 | -56.41487 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c88beed3-5ab5-3497-8834-bf7d6bc7d640 | -11.89187 | -56.4108 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bbece4a-d728-352f-a71b-bcb81fa94933 | -11.88856 | -56.41027 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b595c7f6-0a67-3dec-8926-764137bb120a | -11.88524 | -56.21375 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fceca903-5323-3d8e-a466-6829e37881e0 | -11.88469 | -56.21731 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed4ef004-3fb9-3c3e-a402-4dc196d96d03 | -11.88246 | -56.20967 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc2869bb-aaf8-305f-b76e-3665a6bd9e55 | -11.88191 | -56.21323 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8692b7e-3915-39d1-9f09-3213a570759b | -11.88136 | -56.21679 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0034f888-227c-3c7c-b275-7cb46065f300 | -11.87859 | -56.2127 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aad0f64-b2b5-39f3-aa6b-8f9506c0775e | -11.87804 | -56.21626 | 2024-10-25 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99f2d0a0-5e62-3eed-83ae-462110502798 | -9.84017 | -57.72046 | 2024-10-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9c0aca9-0e9e-3e55-8bf5-7972d56f9a4b | -9.75829 | -57.23549 | 2024-10-25 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3cf1eda-4dfb-384a-bc17-39a96419b9d7 | -10.45926 | -57.46401 | 2024-10-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9986f09-768a-3090-ba66-3a9e0b6d3be7 | -11.06107 | -57.82393 | 2024-10-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b35a21-63cd-3df1-acc0-16306e32008b | -11.05831 | -57.81983 | 2024-10-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504525bd-3492-35b7-a524-0a0ed31615e5 | -9.74096 | -59.31751 | 2024-10-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 296a966a-8e63-3a68-85c1-ff82b76f67a7 | -9.51654 | -59.53764 | 2024-10-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61298413-e4cf-3ea9-9d18-dba529feb332 | -9.51296 | -59.53702 | 2024-10-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff3626ab-b9ad-3f77-ab27-6305a656c212 | -10.39024 | -58.41689 | 2024-10-25 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e39bc724-4f6c-3849-af82-4c7d37ecd537 | -10.38963 | -58.42058 | 2024-10-25 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cea852d-fd53-3d6e-8342-3141e71a9263 | -10.02819 | -58.46133 | 2024-10-25 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdfd038c-5ede-3f1b-892e-b33c101faf0f | -11.49267 | -59.07767 | 2024-10-25 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370ac4bf-22ec-3a17-8a4c-d3c06f4d4bcf | -11.4582 | -58.62532 | 2024-10-25 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37e653bd-bdde-31c1-844c-a82532c5924b | -7.32095 | -59.71875 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90d4b3e7-ecc6-328c-a68e-79fde20fb2ec | -7.29175 | -59.6414 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2dee53-dbfc-399e-ba37-38dcdf3e77cc | -7.10044 | -59.77147 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 181603ba-c278-3911-b874-0ba012257104 | -7.09877 | -59.77289 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39092dcb-dbfd-3ba3-8253-42b97a7cc4f7 | -7.09288 | -60.04737 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5234f929-8f30-3e47-9774-14a732e7fb54 | -7.09223 | -59.28238 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcf1e009-6a26-32b1-9ea9-b3f056efcdaa | -7.0893 | -59.27753 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faf5397a-3f4c-3652-a6fb-c53171efe316 | -7.07246 | -60.02973 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02a1fe20-6c77-3d87-90d5-6a6891a2f53b | -7.04923 | -59.33809 | 2024-10-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 253d5fcf-bd7c-342b-bac6-f0e63cd51ec4 | -10.42549 | -61.29085 | 2024-10-25 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da688f80-0fc6-3ccc-812c-2e95fd181e9e | -13.49476 | -61.62132 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 75c3cbba-de52-39ff-8518-3c99ea745fc7 | -13.49394 | -61.62606 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3a91b60-29f4-3d42-a1ff-5fdd6aa1558d | -13.49311 | -61.63083 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a972fa4-81ff-3f43-8834-050ddbc71a4b | -13.49097 | -61.62061 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| da332f77-9d64-3c32-be52-e888daf531c4 | -13.49014 | -61.62537 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7af271b3-7639-3089-8189-37e7158c03f7 | -13.48932 | -61.63014 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c34ff7d-cc9e-357f-8d73-454e98a1cf1c | -13.48718 | -61.6199 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92732c10-6886-3123-b687-b747f2ce6386 | -13.48635 | -61.62468 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ace659c3-d22e-3cad-b317-56d69d71908a | -13.48552 | -61.62946 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cec4fe8a-7f6f-3102-af9e-49ed4ee2744e | -13.48255 | -61.624 | 2024-10-25 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 42b37c62-a740-3cba-9288-437ee8c6bb9b | -7.92888 | -61.55663 | 2024-10-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README99.md)
