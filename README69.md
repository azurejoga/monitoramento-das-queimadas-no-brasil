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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 923f8b07-e529-341a-894c-23110c1b3eca | -2.41346 | -46.03085 | 2024-11-23 12:29:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 01f91684-c706-3879-836d-3e4cc68a5bf4 | -3.45808 | -40.83749 | 2024-11-23 12:29:00 | TERRA_M-T | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 9bb83a49-8213-3039-a849-3ee21b82bd1f | -3.75997 | -42.27172 | 2024-11-23 12:29:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 59899c76-f8b2-31b0-810b-964a6ae1d833 | -3.62056 | -42.1524 | 2024-11-23 12:29:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| acabd24a-daea-399c-8a78-6d9240708433 | -2.68974 | -46.09927 | 2024-11-23 12:29:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 8e1baa7d-46de-336f-82f5-d063f830d40d | -3.43383 | -41.45138 | 2024-11-23 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 2065d794-b54e-3452-b6fd-7358e1afa5f4 | -3.10615 | -41.94618 | 2024-11-23 12:29:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2d209eb1-e81e-3d14-a87f-47517eca7f79 | -4.13914 | -41.94722 | 2024-11-23 12:29:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| bd47ea3d-711e-32ac-bf97-b22269a05c8a | -3.76131 | -42.26225 | 2024-11-23 12:29:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 1f7b6fd6-d4bb-33ba-97da-70b8d39fb872 | -3.8437 | -43.93861 | 2024-11-23 12:29:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0b141510-5333-3955-8706-4476dc3925d4 | -3.21039 | -42.6982 | 2024-11-23 12:29:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 35eb9b93-ee70-39f3-b819-bb2f24a01cec | -3.36616 | -41.5507 | 2024-11-23 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 3546af4e-623f-356a-81e0-6c7446b22392 | -4.40636 | -39.07454 | 2024-11-23 12:29:00 | TERRA_M-T | ARATUBA | CEARÁ | Brasil | 2301406 | 23 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 87eef666-f7a1-379c-a0e9-b755814979b7 | -5.12513 | -45.15806 | 2024-11-23 12:29:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 81096146-a3ab-310c-a201-92bfbf64bb90 | -4.53491 | -42.91888 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| a6e15797-2e34-3751-bd8d-4e50fd0d32de | -4.06201 | -40.399 | 2024-11-23 12:29:00 | TERRA_M-T | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d3dc1ebe-bb85-394f-a200-661ea6e78a72 | -3.36762 | -41.5405 | 2024-11-23 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 265dd1f3-dfac-328d-9257-31019befe9dc | -2.70553 | -45.23222 | 2024-11-23 12:29:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7a823298-d225-324d-9f5e-aac0ca028dab | -3.33495 | -42.08441 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ef9fd242-e31a-32e3-977e-3cf8e26f28f5 | -3.7432 | -42.65051 | 2024-11-23 12:29:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 53738582-fbd1-3c31-a3f7-073ad43bdd26 | 1.22953 | -50.73428 | 2024-11-23 12:29:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 973e7abf-e00e-33cc-8d9f-0ebdf012a34b | -5.07376 | -44.05471 | 2024-11-23 12:29:00 | TERRA_M-T | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5812541d-307a-3793-adf2-f3cacefe8860 | -1.62353 | -53.31241 | 2024-11-23 12:29:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a84b0b1a-3b1a-3499-a70f-2092ed221558 | -2.13235 | -46.39885 | 2024-11-23 12:29:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1ba28f92-80b7-3d93-980c-f5c24fab176e | -4.28034 | -43.73518 | 2024-11-23 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| bb104464-3c94-3577-b607-cc1a45fdc2a3 | -4.52723 | -42.90849 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b60c82e7-9499-3b27-bd54-fffeaf4e7c8c | 1.22702 | -50.74065 | 2024-11-23 12:29:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0291ab74-2e7e-35af-8f57-b4834a75e2a3 | -4.53885 | -42.89136 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c70f38d4-7e97-308d-9bc3-efd71c921e69 | -3.17083 | -42.20455 | 2024-11-23 12:29:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3d6fdd70-dc96-3516-b151-e38a98adf315 | -2.7868 | -43.33998 | 2024-11-23 12:29:00 | TERRA_M-T | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 66eb519d-930b-3eb2-8cb6-19ced085d205 | -5.15378 | -43.16928 | 2024-11-23 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0f49af2b-3156-3213-ae1a-6af72d8885e3 | -4.26427 | -48.69604 | 2024-11-23 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 782.1 |
| 7cf5793d-b4e8-37af-9982-039ce62e3115 | -3.52627 | -42.03492 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 3c257f93-b592-3327-89a8-8c935cecf572 | -4.61189 | -46.5009 | 2024-11-23 12:29:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 8906ced3-e5a7-35cc-b158-05be099cb329 | -3.81522 | -42.46793 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 831a3985-78bc-305b-b65c-330adc32e4bd | -3.44621 | -42.21299 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 212711bf-9ae7-3b31-9803-def5386bbdef | -3.48892 | -42.16678 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 9acaff42-eab3-3bc5-94a1-e97f7b4c3a3b | -3.41118 | -42.13051 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 39.9 |
| b4a885d7-8f29-3a4e-ac1a-fce23bc16fa7 | -3.3588 | -42.04863 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| f271a299-f1d5-3ced-a0fa-0a198ab7b647 | -3.2587 | -43.26588 | 2024-11-23 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f429582e-cff1-3c42-a945-0294fbc7c87f | -3.6192 | -42.16198 | 2024-11-23 12:29:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 59698bc3-de07-3e34-a7c3-4821003304d5 | -3.75853 | -42.02987 | 2024-11-23 12:29:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| ab56652c-2b9f-350e-a082-4482c2d4b0ee | -5.06663 | -40.60342 | 2024-11-23 12:29:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 91b90cb0-fda1-3811-8692-2186c673be4b | -4.15574 | -38.62639 | 2024-11-23 12:29:00 | TERRA_M-T | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 73cb2426-086b-3644-9ed6-1ba14dfde53d | -3.72383 | -42.65723 | 2024-11-23 12:29:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| ec42f93a-e1c4-36a4-b50a-f252002dc876 | -4.6077 | -46.49387 | 2024-11-23 12:29:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 9e38d1d3-4457-333f-b8c7-df522427ea65 | -5.28211 | -42.72186 | 2024-11-23 12:29:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4602652a-f73c-3ef3-87db-067fec313120 | -4.55188 | -43.56928 | 2024-11-23 12:29:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7e453012-98b1-37e4-bc13-91a6546646f0 | -3.11501 | -42.52927 | 2024-11-23 12:29:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 33da06fc-424f-3ba5-845f-77d765d5e575 | -3.44485 | -42.22248 | 2024-11-23 12:29:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| a542ca7b-f6a1-3cc0-ad44-722e031b5d72 | -4.41885 | -44.11674 | 2024-11-23 12:29:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5e9333a0-0ffb-327c-a633-1b571d66d7f9 | -3.58396 | -42.09202 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 40f56991-e0ec-3807-bf3b-426262d6171a | -3.35743 | -42.05826 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 561142f2-b70e-3b59-9104-84c284c0b030 | -4.13773 | -41.95708 | 2024-11-23 12:29:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 44.2 |
| e19f7557-0a51-3dcb-9ff7-39d9a4c0389b | -1.44503 | -47.34188 | 2024-11-23 12:29:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| bbb2c2aa-1a2d-3d50-9d30-e3ea94ccd995 | -3.72514 | -42.64808 | 2024-11-23 12:29:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9c82d95d-e8a0-3681-8422-4639444dc641 | -3.43634 | -42.08521 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 12744eda-b660-3c87-ac85-295c12c5e569 | -2.70742 | -46.27586 | 2024-11-23 12:29:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 068db37a-bb4b-3fc8-a667-84839df617c4 | -2.95305 | -43.77866 | 2024-11-23 12:29:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 0fa52548-59bb-32fb-9108-c2a3e91569db | -3.56785 | -42.1387 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8dc5c4f4-86f2-37fb-b9d2-99d8fdfa68fb | -2.96762 | -44.95266 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| acd46902-51c2-3765-809e-c69ad9d58fa6 | -3.61335 | -42.00385 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 002038b3-1e35-30c0-b0d2-0a39b257737a | -4.51445 | -42.86924 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 399b4cc4-6c75-35ed-b410-3b4d5f4e3f49 | -2.92677 | -43.52444 | 2024-11-23 12:29:00 | TERRA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| de58a8b4-d53c-3917-b8bc-5253004d2e5b | -4.54391 | -42.92014 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 8ac5d0b3-1b57-3ce3-a744-853026373d13 | -2.78807 | -43.33117 | 2024-11-23 12:29:00 | TERRA_M-T | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 90a17252-1df4-3b40-881d-8f5b78ad7d33 | -4.20267 | -42.33442 | 2024-11-23 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| db6c894d-7b14-348e-a720-66c1326c73ce | -3.2117 | -42.6891 | 2024-11-23 12:29:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b115be9a-cdd5-3a18-ae97-8c48a26af9b6 | -3.73187 | -42.53597 | 2024-11-23 12:29:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 89ff1047-56ea-3ef5-8d89-10ecc4f2af47 | -2.70389 | -46.26939 | 2024-11-23 12:29:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| f4dafc78-78de-396a-8973-f767b77396ee | -4.20401 | -42.32488 | 2024-11-23 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| d2459552-5b58-30f0-92c8-2660c0342baa | -2.85355 | -44.66327 | 2024-11-23 12:29:00 | TERRA_M-T | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0725c834-722b-300d-878a-bab8f411bd49 | -3.41253 | -42.12096 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a5f84704-6a48-379e-a88b-ff49a6c97c27 | -3.18937 | -41.94367 | 2024-11-23 12:29:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| fc3e8ed2-b199-3a01-b840-70680639e51c | -3.71612 | -42.64681 | 2024-11-23 12:29:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e60998e8-b50e-3d2d-a187-399cc1f4ce2c | -2.95864 | -44.95139 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 0249abf5-4104-309c-920d-4b836070eaac | -3.46798 | -40.83873 | 2024-11-23 12:29:00 | TERRA_M-T | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 130ed3da-66a7-3d25-89f0-ed9d860b8133 | -4.19558 | -42.32747 | 2024-11-23 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| ce32ecef-01f7-3338-b5d3-6ece47fbe854 | -5.2797 | -43.06257 | 2024-11-23 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2b1b5f27-4e72-3aca-80cf-f3d79ea253fe | -5.45604 | -42.13996 | 2024-11-23 12:29:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| d3586e81-9249-37c5-8b92-d2331e8a2912 | -3.29769 | -43.51139 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 969975a3-c767-3e86-86d7-f1ceaf6b07c1 | -3.59188 | -42.08969 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 498.8 |
| be269469-3723-3403-bdcd-4f8795be885b | -3.47289 | -42.28067 | 2024-11-23 12:29:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fc9d0ac9-4f4f-3e44-b6c0-6277b980ea3a | -3.74928 | -42.02855 | 2024-11-23 12:29:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 078fdb51-791f-324b-b8ad-d42c07f091ae | -3.56219 | -41.78007 | 2024-11-23 12:29:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| aeb367b1-a834-3c4a-b7b3-5403bfa11cad | -2.84845 | -42.58584 | 2024-11-23 12:29:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| bfef3a4f-1c7b-39c1-a692-e1342065efeb | -3.58535 | -42.08241 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| cb2e9762-05e5-3140-b782-b92704404a80 | -4.42012 | -44.10796 | 2024-11-23 12:29:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 282804b0-b60f-39ff-9cc8-6a4f093bb819 | -3.37999 | -42.03189 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 193.6 |
| 0d514bba-1755-3506-9aac-97a2c80a9faa | -3.76694 | -42.80929 | 2024-11-23 12:29:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 88011820-a40a-3f18-be18-fb3d80761ae1 | -3.3906 | -42.02349 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| a9ab0b20-4fe5-3a78-8b36-30b3c1bc1d4a | -3.11369 | -42.53845 | 2024-11-23 12:29:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d73d6ec5-b87e-36ea-8dee-0b3d8d06bebd | -3.23841 | -43.34424 | 2024-11-23 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9fe6c838-2fb4-35b9-ab36-f5cc818b9e02 | -3.79181 | -42.17883 | 2024-11-23 12:29:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 274.2 |
| 3e75b4b6-912e-3905-8c63-0be9ea9bfc23 | -3.681 | -42.24467 | 2024-11-23 12:29:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 7891f3e0-6c47-3224-a42b-b8234d72800d | -3.37708 | -41.54179 | 2024-11-23 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| ec416ae0-36d7-33b9-aaf0-9202e3dc4768 | -3.48758 | -42.17633 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| afbcbb0b-112f-3b67-b20d-1dde35e400c5 | -4.10086 | -42.46888 | 2024-11-23 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3251c951-6b25-3c9c-8b3c-0a207fcd0634 | -3.59053 | -42.09929 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| 129ef8ce-44be-3f48-9494-a43b568ff906 | -5.46851 | -43.22875 | 2024-11-23 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |


[Clique aqui para ver as próximas entradas](README70.md)
