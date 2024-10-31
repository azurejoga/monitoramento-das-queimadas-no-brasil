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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc07a292-8d45-3e3d-a1ff-20c53e6960e9 | -22.42498 | -48.5833 | 2024-10-31 04:53:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eff4abb5-664f-3cd8-9591-2c8691a3f89c | -22.42444 | -48.58845 | 2024-10-31 04:53:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 94c8f4be-7d19-3492-9e0b-52349a0c3724 | -22.42388 | -48.58197 | 2024-10-31 04:53:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ce58e39d-86ff-3edb-8d35-1abac81aea3b | -22.42331 | -48.58714 | 2024-10-31 04:53:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4a006f64-b254-37f7-b283-dac0c4e98ea4 | -22.42025 | -48.58281 | 2024-10-31 04:53:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32bb975e-eeb5-351e-a1cd-7583fd10f618 | -21.56218 | -48.7988 | 2024-10-31 04:53:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a31f3af3-82d7-324c-8e5a-454d449bf591 | -22.36121 | -48.76061 | 2024-10-31 04:53:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f9e60b05-9570-304a-9453-9606386229bf | -22.88636 | -49.22229 | 2024-10-31 04:53:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18bf0b8d-5ec6-30d1-ba87-dc939df0c7ee | -22.54048 | -48.81488 | 2024-10-31 04:53:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d2d9cd3-1d65-3488-a643-ae92a0810518 | -19.49372 | -56.71358 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 882e1204-b225-322e-97ba-62bcca0bb5b3 | -19.52468 | -49.64054 | 2024-10-31 04:53:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ce9e3f9-71fe-341f-b44e-525fe7293bf4 | -19.52892 | -49.64113 | 2024-10-31 04:53:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 50cd0e96-4f5b-3933-8c24-1cfa81d4dff1 | -20.31652 | -50.01147 | 2024-10-31 04:53:00 | NOAA-20 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74d575ba-1724-33bf-a5e6-833711d30997 | -20.31602 | -50.01547 | 2024-10-31 04:53:00 | NOAA-20 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0576e6ff-5c2f-3ee9-9322-04a3480b6d58 | -24.24246 | -50.74077 | 2024-10-31 04:53:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dfac7dd8-8515-3451-89ed-389b7d9c835d | -23.2166 | -52.50686 | 2024-10-31 04:53:00 | NOAA-20 | TAMBOARA | PARANÁ | Brasil | 4126702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19d93b0d-4c29-36ac-8efe-2768882acc93 | -23.146 | -52.6677 | 2024-10-31 04:53:00 | NOAA-20 | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d0399fc5-e220-3e16-9144-b2b7598ca2bb | -19.49312 | -56.7173 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9f1e9cb7-367c-3644-bdf0-64b25a97e004 | -21.56351 | -54.21178 | 2024-10-31 04:53:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 102d0068-05ab-399e-8a9a-c3a04e20d0af | -23.58093 | -54.75785 | 2024-10-31 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 48941a7a-c2a6-3e06-8308-bbfe2b5421a3 | -23.58085 | -54.75668 | 2024-10-31 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f43d080-a487-3217-b9c7-0a4ccc989a2c | -23.74405 | -55.1278 | 2024-10-31 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78963f0a-6b5f-3db5-b08b-9497ff6f725f | -23.74347 | -55.13173 | 2024-10-31 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa4ee39e-6cef-313e-8e68-16f0824c7b8c | -23.74317 | -55.12865 | 2024-10-31 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2097e9d3-56d0-39f0-b280-1eeacf9e85b0 | -18.00005 | -54.44585 | 2024-10-31 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1380739-77ac-3ba4-8d26-94770ef582d2 | -20.57926 | -55.5725 | 2024-10-31 04:53:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1273ad6-f25a-361a-98e9-786a71aea3cd | -21.38323 | -55.70594 | 2024-10-31 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9f6a192-5ae3-3e1f-89bb-e28a6e023eec | -19.48849 | -56.62493 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7080d56e-d70e-37bf-bf2a-b5918586e0b7 | -19.48243 | -56.62002 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| deb0a567-1035-3d8c-96cd-ab100fd73ad0 | -19.47576 | -56.61882 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| dce2999b-9ce1-32d1-834b-ebe10549acf8 | -19.47243 | -56.61821 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f63aa1da-594d-38e4-9e0b-27270a47c8ea | -19.47157 | -56.64476 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| aa18018e-54c3-38e3-8091-5d4f6533d964 | -19.4691 | -56.61761 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8f0b6f47-5a1b-31ec-a2b8-e6757c9353d4 | -19.4791 | -56.61942 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| e0eb3230-728a-3013-af99-93e42e2102c2 | -19.47763 | -56.64968 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2a25ba2f-a0b4-3dff-b254-115552c44d20 | -19.47516 | -56.62252 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 86f6cd60-d3ce-3402-986a-5cd0e52976d5 | -19.47463 | -56.66823 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 92d43368-b632-304e-9aef-4b6a82d1ae64 | -19.46823 | -56.64416 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 420cec5f-47a4-3a73-8a4a-c7b0a9e8b5a0 | -19.46763 | -56.64787 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 950326d0-2075-3d37-817e-bf1c2871c3f9 | -19.46703 | -56.65158 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 832ea9e7-18fa-3787-94a4-e311fbc7ff25 | -19.4643 | -56.64727 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a51c6313-b6c4-3dda-8cdf-ecd9f5380062 | -19.4755 | -56.64165 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9e7fd4a-48b3-3794-bfcc-da529d4226f3 | -19.47096 | -56.64847 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| c884eb6b-d5bf-3784-83dc-3d562b5c56d6 | -19.47036 | -56.65218 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 07204620-e73e-31d5-bd22-ef8a76dd530b | -18.26535 | -55.96558 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 01aedfa9-ccbf-3181-9131-4912aa85f0ae | -18.26203 | -55.965 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f4d3f3e-3cde-3ff7-aa16-af1ad075ef8d | -18.2593 | -55.96077 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 35638844-5a5b-3534-ac4e-f9b67098b132 | -18.25871 | -55.96441 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7192ec5e-7355-302e-8906-d67220d2497c | -18.25795 | -55.99048 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 791888d4-42cc-3d68-8ec5-d1e8e9cf56cc | -18.25737 | -55.99413 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a16d37bf-8cc5-3c04-b27d-e778e72b4455 | -18.2554 | -55.96383 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9e099be8-68a4-3ed8-86ab-282ea8e79c05 | -18.25208 | -55.96325 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1fe906dc-ca51-3ea5-875d-347ee213e74e | -18.24818 | -55.9663 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b3e3a818-8878-3c43-a9b7-5eef048c9597 | -19.53831 | -56.71402 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| aa4e7543-db46-3fff-83b0-57e809e190c9 | -19.52223 | -56.70728 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ed4c9e88-379d-37a4-9626-b34ab639cd1b | -19.50768 | -56.71229 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2bba098e-ddab-31f0-9665-ae89a3d89143 | -19.50525 | -56.68509 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7c2b82ce-3d67-30dd-bbda-cb00ab9b999f | -19.50434 | -56.71169 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2df4f807-8e5a-3f62-9b3b-f4e8c84fa5ad | -19.48828 | -56.66291 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e90cfa8-f3e5-3eda-86bb-71ea1bab2052 | -19.48767 | -56.66662 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 04b8c684-fb45-3c63-be3c-00f9747bba86 | -19.54619 | -56.7078 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e63e274b-665f-337c-a221-55ee510d99de | -19.54044 | -56.72206 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| a321946b-4da3-34a9-a7c6-73a6782827ed | -19.53103 | -56.71653 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| bec166c3-aa43-315c-b0f8-7dc3d82c1595 | -19.52405 | -56.69614 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| eacf3537-42af-3cd0-b65c-6903c5c17178 | -19.52345 | -56.69985 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b1e662e5-d534-3dfa-80c6-0449f2ccede5 | -19.52284 | -56.70357 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e5c7bf78-0fe5-3890-bcc0-0c499c885aa6 | -19.50919 | -56.68198 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 445b8770-cc34-3fa3-9342-636896be31cd | -19.50798 | -56.6894 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| dd5a0ba7-8ef6-35ab-8ce9-65935aeb67cb | -19.50556 | -56.70425 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| c0ab1d74-cd94-3aea-9d7c-179778f33492 | -19.50282 | -56.69994 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f0920625-2fe1-36b8-9ac1-7da7d9066f73 | -19.5007 | -56.69191 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fcbd8f66-41f8-3389-b512-b3f884569527 | -19.49888 | -56.70304 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 34f573a0-9b59-3bd9-9f6f-13549e00aabf | -19.49433 | -56.70987 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| de999300-da0e-319f-9ad8-12cfaf4cf382 | -19.4916 | -56.70555 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b2103102-e376-363d-bfbd-2243a3bcd6d8 | -19.49009 | -56.69381 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1855dd82-03bd-3ff7-99c4-67f640f28f56 | -19.48978 | -56.71669 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| b84a7e32-883b-33f1-a6a6-e0961cba736f | -19.48917 | -56.72041 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 702040a5-8285-3c37-82b7-b7f9a0348c56 | -19.48583 | -56.71981 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 341bbedd-04d6-35ed-935a-de18f246dc7e | -19.48311 | -56.71549 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| af0650d6-70d6-3f7b-9d32-9146e3d14e44 | -19.4825 | -56.66201 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8ddb7b8-9194-3039-aae8-379f3b9f9701 | -19.48157 | -56.64657 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b96354fe-7b03-302f-bb65-12a217596e28 | -19.54559 | -56.71151 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bbb7ded6-cf82-39a3-adb8-85ab2817f042 | -19.54285 | -56.7072 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| defcdc0d-fb52-38cd-a197-5e909c9aa560 | -19.53952 | -56.70659 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e95f8139-8d52-35a0-a650-09cb684a6fdd | -19.53891 | -56.71031 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dab1dd16-7805-331c-b3fa-feb8cc0b6643 | -19.53558 | -56.7097 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4616a51b-06f2-354a-b377-f01f1eca9872 | -19.53497 | -56.71342 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2f521ed4-2ddb-36bf-9b43-29913e57008a | -19.53284 | -56.70538 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2240ab86-cd11-3bae-aaa2-ea66db6a9b8b | -19.5289 | -56.70849 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e2150243-6aa6-3f5d-8f03-20ad8f1e141d | -19.5283 | -56.71221 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d1d06b01-2c01-3c29-982b-3e9fb83acdd7 | -19.52557 | -56.70789 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c66a8feb-0b20-3cb4-b34f-2ebe7cf8742a | -19.52497 | -56.71161 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 30f08c93-a6bb-342e-9acf-5ebd6f787d6a | -19.52465 | -56.69243 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f15af5f6-fdb0-3a6b-beaa-9fcfe41b62ed | -19.51283 | -56.70175 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.8 |
| b987bec6-f995-3f48-8086-8011f4389c52 | -19.5095 | -56.70115 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 64d0b2c3-80f4-3002-aea5-9a40487edd7d | -19.50192 | -56.68448 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bb08e76d-9c1f-3dd6-b58b-4aadd7a318fd | -19.49372 | -56.62955 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| afbd1398-4696-3958-88f2-19eaf851bfc3 | -19.49242 | -56.62183 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2cfe065e-e54b-3413-b3a6-c642c94de891 | -19.5371 | -56.72145 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| f4b3208b-3c0e-30c5-bd17-528b2aaf176e | -19.53437 | -56.71714 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |


[Clique aqui para ver as próximas entradas](README41.md)
