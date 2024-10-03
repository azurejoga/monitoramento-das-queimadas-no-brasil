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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c221ace7-5cd0-38ca-ab89-2c38efc232b8 | -21.63141 | -46.42426 | 2024-10-03 04:32:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c5fbebff-142e-3b1b-bb81-6c4abea87aa3 | -22.38417 | -47.89174 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aeccf20c-b218-3fa9-b3e7-2ba830773b84 | -22.38359 | -47.89579 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfe57a9f-0e61-3d56-8626-c805b90bdff7 | -22.38301 | -47.89983 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 7671f3dc-83db-3a04-8d39-73498ff17cb4 | -22.38244 | -47.90387 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 94.5 |
| c482b996-abf7-34fa-80f5-cb8219abf459 | -22.38187 | -47.90786 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 62181016-1c9c-3622-aa22-36071d554311 | -22.37959 | -47.89923 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4ace52d6-3d91-3614-aac7-b3ad2c0e8570 | -22.37901 | -47.90329 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 09b9ed9f-b7d0-390c-b66d-9a25aebe0dcb | -22.37844 | -47.90729 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8dab10de-0900-30c4-b3e1-f35441481379 | -22.37559 | -47.90271 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6db32603-cf3e-38b4-9d78-ff7ea479a938 | -22.37501 | -47.90673 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b7f8783-a47a-3c02-b166-d9945857ed1b | -22.37444 | -47.91072 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3290dffe-9171-3703-b34c-53c7da063bd1 | -22.37388 | -47.91471 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92aa4ebd-74fe-3cd0-9a63-f6e03c326d68 | -22.37216 | -47.90214 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dc9c1ca-5ab1-3ff0-afd4-6157daa9a6db | -22.37158 | -47.90617 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e74c4411-be32-32a0-ba58-e00f3a9dd08f | -22.37101 | -47.91016 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a935d835-594e-3999-a817-e830891ad2c4 | -22.36816 | -47.90558 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 058c006c-de54-3b8d-9c0b-e756bde6349e | -22.36759 | -47.90958 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b36536c8-6cc7-371d-a0d2-2b1b26dfae4b | -22.36647 | -47.942 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b0e6ffd-e871-3389-b5bd-66ee8997f53b | -21.74464 | -47.52483 | 2024-10-03 04:32:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba094ce4-4a45-367b-8605-0d100360d51e | -21.39206 | -47.63915 | 2024-10-03 04:32:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 033c96a2-f394-37f1-9bf6-efcc997cde7d | -21.39148 | -47.64316 | 2024-10-03 04:32:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce21f5bb-0dcf-30e5-b412-76a44cd135ff | -21.38921 | -47.63456 | 2024-10-03 04:32:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3fd230a-5579-3241-b914-60466e34c198 | -22.18533 | -48.60899 | 2024-10-03 04:32:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8ca9e087-6ff8-35ae-a0a0-dacabd26ea36 | -22.17642 | -48.5761 | 2024-10-03 04:32:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a57acfc8-4f43-3442-be21-24ea7a49833a | -22.17529 | -48.58376 | 2024-10-03 04:32:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 94276be5-21ed-33fa-b238-3e3396d3317f | -22.8901 | -48.41095 | 2024-10-03 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31a86b70-85b8-354c-8a3a-b1ae045360a1 | -22.84097 | -48.4144 | 2024-10-03 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 686d5eb1-6cbf-3c23-b4ae-cd85db886819 | -22.84039 | -48.4185 | 2024-10-03 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1ad27c4-9ffc-3512-ab08-dc9bd7aae499 | -22.83759 | -48.41381 | 2024-10-03 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0151c246-4518-3108-8302-6ba3e724b527 | -22.837 | -48.41791 | 2024-10-03 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c168899-2697-3160-aa6f-334126a16fb9 | -22.54507 | -48.54212 | 2024-10-03 04:32:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 504e470d-44da-3d56-8763-29b7fe55eb07 | -22.5445 | -48.54599 | 2024-10-03 04:32:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| a2d1cc32-ca70-31db-ad64-fb2dee7110e1 | -22.54394 | -48.54985 | 2024-10-03 04:32:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 07f67912-d7e5-31ce-b452-13b36b0b86d2 | -22.54171 | -48.54153 | 2024-10-03 04:32:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ea9047b-db54-36cc-8aed-3f3312f65079 | -22.39787 | -47.89413 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1fc1b6d8-5d78-3890-8c4f-969bff45d0ac | -22.3973 | -47.89816 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| aa43a5a7-8d50-3a8c-9c23-45b12074192e | -22.39502 | -47.88952 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3796e820-0d2f-359e-87be-1637ec8f8ca6 | -22.39445 | -47.89355 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 92d6c792-6cee-33ad-aa25-5dc4fb5b8375 | -22.3916 | -47.88891 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fe7c65d3-c6c1-330b-8845-5158919eb459 | -22.39102 | -47.89296 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5821d474-a3d7-3d8a-95b0-637275b7c1e4 | -22.38644 | -47.90042 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0816ff84-ac06-3cb7-9c85-f5ed2f0d6883 | -22.38587 | -47.90445 | 2024-10-03 04:32:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 28556df8-3b70-346c-ba4f-e3c73e471681 | -23.98213 | -48.91847 | 2024-10-03 04:32:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c916b3c7-ab8c-3c76-ad2a-ca3f0242529a | -22.39116 | -49.27311 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c1e419c-4f14-3ed9-9a0a-12340a48181f | -22.39059 | -49.27687 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 735dfd7a-0213-34e2-a975-d34cf0e29cc3 | -22.38622 | -49.26064 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 399b8bd2-7c97-3c0c-b4f4-94af7e084850 | -22.38347 | -49.25631 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 24ae3e62-362a-3e5f-b845-fc53c66d17f9 | -22.3829 | -49.26006 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cfb587af-8b03-3582-9653-63b456ca7d84 | -22.38233 | -49.26382 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7b3b048a-4f1f-3e82-ae28-131f97a717b1 | -22.37009 | -49.27708 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e1b1968-877d-3b49-98bf-c85baaeafbd3 | -22.3662 | -49.28024 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf9538a6-19fd-3197-b284-08ca50e5d3c3 | -22.36392 | -49.27591 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cb60fdf-c67e-382d-a2b4-9e6f221e3b93 | -22.36335 | -49.27966 | 2024-10-03 04:32:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 1b569b7e-e8fe-3c65-9df7-8c3176f7f273 | -22.35531 | -49.33218 | 2024-10-03 04:32:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65993385-8fbc-3a97-8563-9cf49a423994 | -22.28507 | -50.00431 | 2024-10-03 04:32:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1628bf25-16d1-32cd-a2bf-e6ef831ab5b6 | -22.22764 | -49.63136 | 2024-10-03 04:32:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 587bd776-b0a6-3903-b4bf-1ffe4cad44b0 | -22.16235 | -48.62475 | 2024-10-03 04:32:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c3650b2-5588-365b-bbb6-5ce67a7110c7 | -22.15842 | -48.62803 | 2024-10-03 04:32:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 223106e3-5425-3612-a933-d4aefc6297a5 | -22.15507 | -48.62745 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b62e710b-b880-37f8-84c8-5e3175e52f6b | -22.0343 | -48.73214 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 4139f1ed-34ba-39f8-9bef-f0016d032372 | -22.03095 | -48.73158 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 2c16870e-c1a7-37e6-baf4-511ccb5574bb | -22.02425 | -48.73044 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 27317726-86a0-3324-8f40-f1068908cf29 | -22.02369 | -48.73425 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 46cfcaac-14d9-39d3-8bc8-88005a272ceb | -22.02091 | -48.72987 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| bf04f49f-8786-3f2d-b272-cca05a854a30 | -22.02034 | -48.73368 | 2024-10-03 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| cbd16355-4c56-358a-89e0-1103471ea31e | -21.23789 | -49.41371 | 2024-10-03 04:32:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0cdf0600-b87b-3762-a87c-443135a0cc84 | -22.98007 | -49.17613 | 2024-10-03 04:32:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3e32a82-fe50-3f3f-a6ff-45c11807273f | -22.53915 | -48.81351 | 2024-10-03 04:32:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d12b5865-852c-36d2-aa53-78cf598d532f | -23.53907 | -49.83496 | 2024-10-03 04:32:00 | NOAA-21 | JOAQUIM TÁVORA | PARANÁ | Brasil | 4112801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1a8388f-232f-3946-ab2c-fbd4972300e2 | -22.99979 | -49.60498 | 2024-10-03 04:32:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9e8f75d1-b6d7-33f7-832f-1984f72d727c | -22.9959 | -49.60814 | 2024-10-03 04:32:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 56953f47-ac17-3213-8be5-abd6e6f97966 | -22.99533 | -49.61189 | 2024-10-03 04:32:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| daf8bc54-3f4d-35fa-87fb-4437407bfb6c | -22.392 | -50.23309 | 2024-10-03 04:32:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 967864c0-8907-3c7b-b6a8-dea94fd27645 | -22.38928 | -50.22877 | 2024-10-03 04:32:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9caec01d-f653-307e-a535-8f75121a453d | -22.38869 | -50.23248 | 2024-10-03 04:32:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f49efea-5127-39b6-8e31-6c3aac19219f | -22.3848 | -50.23559 | 2024-10-03 04:32:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58384595-05c5-3584-b4f4-971f6be4aac2 | -22.38208 | -50.23127 | 2024-10-03 04:32:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80b40b83-e10d-370d-9bb8-c29e9326aee3 | -21.6207 | -50.7953 | 2024-10-03 04:32:00 | NOAA-21 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| db46e8d6-f76f-3fb1-89db-45b456fc25b3 | -21.42004 | -50.98347 | 2024-10-03 04:32:00 | NOAA-21 | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ff4db916-ce31-3cad-ac3d-edb2a00f986f | -22.68718 | -50.47404 | 2024-10-03 04:32:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 461feb14-dc37-33da-a60b-e8fa8da4a3f2 | -22.68387 | -50.47345 | 2024-10-03 04:32:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 445131c3-d925-32b6-90a0-f7ff512f9ca3 | -21.34744 | -55.66936 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 420193d7-0524-3fc8-900c-3763d1b05d2f | -21.34667 | -55.67339 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b46767bc-5ca1-3576-ae63-5ad60fd851d6 | -21.34487 | -55.66032 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcb76019-ebb0-316c-a4d8-9b16021ab1c1 | -20.77927 | -54.81104 | 2024-10-03 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 578b92aa-1e19-3fcf-9e7c-2d5fecadbe35 | -20.77821 | -54.81658 | 2024-10-03 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afcee906-f12d-3b23-885a-598c4387ab8c | -21.37113 | -55.69074 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f421f8af-58ea-3bd2-a918-7cedda217273 | -21.37034 | -55.69478 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe1cbcde-b591-36e6-b161-1f47c635a67f | -21.3698 | -55.68732 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f349a0f0-6b80-3e09-a818-d262cd8668fe | -21.36955 | -55.69882 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a3c9a5f-157c-3815-8e0f-954367cf8735 | -21.36904 | -55.69129 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b62697c-4b0e-3f7a-8e69-acfda9d1cd62 | -21.36829 | -55.69529 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16471b1b-b3fb-385a-b17b-0b0da13995f9 | -21.36781 | -55.68579 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bed9eec1-24f9-3d91-b1ef-3635e756a53d | -21.36751 | -55.69939 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83e48bbb-7ceb-37c9-a103-0c0f285d6504 | -21.36702 | -55.68976 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f690f16-360b-3386-967d-48c9bf1831ad | -21.36625 | -55.69372 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc593895-ec4f-3c3b-802a-5c936abc6ad8 | -21.36544 | -55.6978 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b10b505-09a3-3352-bd9c-36f3cee83a37 | -21.36495 | -55.69022 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b50620d-8cd4-350a-a2bd-7ac4f1214399 | -21.3642 | -55.69419 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README110.md)
