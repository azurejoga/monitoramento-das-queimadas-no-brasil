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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6499467-bd69-39ec-8b01-181a135d21bd | -7.07759 | -46.10524 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61a0313c-f791-3c5e-8c4a-3b3f3a84cf70 | -7.42558 | -45.98171 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f0968ec-6727-3e7e-b2bb-47ed12ffc618 | -7.37082 | -42.44212 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a572f7cf-1fa0-3bd2-9165-f6c5e1c6f19b | -7.50634 | -46.28054 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3397847-f1d8-3352-8abf-d9907fcdde7a | -6.11055 | -42.43662 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cc3fffc7-f392-35ea-bef6-d66a1222c36f | -7.43749 | -45.12863 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aba18c2-edaa-32f7-9f1f-0114af4953f9 | -7.49805 | -47.03844 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebe5524b-73b7-3208-badf-19a060e440f3 | -7.87305 | -48.41456 | 2025-10-29 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32fe2a2b-58ef-3c2e-8eea-edbd98168f7f | -7.4454 | -46.61335 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d02949a2-444f-3b06-8fca-37a4116cc228 | -6.16172 | -41.5278 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3a3a0d5e-1d20-3344-b57b-1ebff21269ed | -6.54356 | -46.76686 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 406989db-eced-3580-8d2a-90be95cdd4d9 | -5.1987 | -46.18643 | 2025-10-29 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 255c0389-e011-3cac-9862-97327a856ff9 | -6.10665 | -41.74018 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c7d8f4ec-2c9e-376b-8533-f6e8aa2c5ccd | -8.61433 | -44.8083 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf1bbc22-5663-37fa-b533-f0145f4d3e54 | -5.58865 | -51.12975 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23042f61-d4c3-3bbe-962e-4c8ec4b8f0b8 | -10.57968 | -49.75676 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9d191af-736a-31a9-ab3d-c4d4ff768d74 | -7.60513 | -43.57568 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aabd158-8c3a-3fa3-8798-5a00d9b42c68 | -5.75526 | -43.39532 | 2025-10-29 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56810dce-1572-3cff-a45a-e3899fd03bdd | -8.69293 | -47.13456 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa80d15d-023b-3e5d-800f-71d575c09936 | -7.82721 | -45.22715 | 2025-10-29 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f03eeb4e-91cb-3b0f-8e66-5befb9d14af5 | -8.50501 | -40.53311 | 2025-10-29 04:23:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f9d1a099-a7c3-3886-b689-614066f2e8d8 | -6.28173 | -47.87618 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e196e357-ad33-31f2-a7d0-9ea275398d86 | -7.59365 | -46.79686 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8653dc1b-d258-3e44-b066-c7d200f381bb | -10.76642 | -47.83093 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5d3861-b16d-38e0-a645-3222b6225ba5 | -7.81345 | -45.37844 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0d74104-c814-38b5-b506-09a80fd01360 | -5.30337 | -44.95311 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 511cab2c-0618-3493-95d1-f8bdac9a01a4 | -6.11174 | -42.42897 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92a15113-bf81-3a56-aae0-1d54b2e13439 | -6.14484 | -41.69033 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b5bbd04c-879a-38a3-815e-4aa7efca8dfe | -10.64796 | -48.09294 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cd7ece0-db8c-38b6-9e8f-6530a4a70d84 | -7.62993 | -46.92007 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0bcead1-e87c-39da-8cd5-42b6b93372a2 | -7.61195 | -43.59897 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db26d6ec-793d-33fc-bef1-61d58a87e683 | -7.12624 | -47.0136 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9047b8a3-3bbb-397d-add2-61445334ad84 | -9.57753 | -46.93675 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 242724ce-48bc-38be-8222-1f3f85453657 | -6.60105 | -44.63974 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d8c0af5-543e-3f70-b62f-e6b00b890483 | -6.13123 | -41.85402 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c740c37-1c07-3b53-b9ad-095f7e3f5e88 | -6.54072 | -46.76258 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d4492a-fb1b-3abd-8d84-8226bccbb7e9 | -7.80325 | -46.43153 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41199f98-e532-302f-832f-2d02a94f0ebc | -11.1484 | -44.93312 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95a1dd00-2132-30fc-b896-d54adcf0e77f | -6.14119 | -41.68303 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b69ccecf-aee7-31c7-a1cb-d5e5d870937b | -7.3368 | -42.47687 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 14f8ef4b-a6e3-3833-951e-38bc437e48d1 | -5.35688 | -46.11403 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4594f0c4-aae2-3866-9a89-9023e9d2c5e4 | -10.52223 | -44.2039 | 2025-10-29 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbba10b0-8b24-317f-89fe-6d29a245a47f | -10.21771 | -45.94704 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe23194e-4c57-33f2-98f0-7ac08cd09560 | -8.33232 | -46.15969 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb3023a-a588-31c6-b163-5896b8c4a63d | -7.7984 | -46.48286 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a42961b2-47e2-3a6d-b027-1c5e913750ea | -10.64327 | -45.24216 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2940b5ac-0aaf-37bf-b469-dc412bdbd337 | -6.13678 | -41.71144 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 21523656-21f1-3d75-a5ff-05a4ba3674f7 | -7.29496 | -45.06696 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a4f1322-4c5d-3ea7-b8d2-837ee08a1b59 | -7.36106 | -47.63668 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4a32df15-7932-3680-b875-225098067021 | -7.98385 | -47.36127 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d08325f9-09dc-3a01-ac12-89d947e86040 | -8.76298 | -46.51065 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41fb764d-2bcf-3a98-9063-914260954473 | -5.60855 | -47.11707 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d189d7a5-e49f-395a-b8df-32d022ff891c | -5.07235 | -47.11243 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a1c2eb3-af3a-38d8-a04a-06bd839de8a3 | -5.67486 | -45.21212 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccf5a7c4-e48a-3509-8244-dc169197ecef | -6.10521 | -42.47108 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2688305c-dedd-3aef-a539-de5933594445 | -7.75187 | -44.71885 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73181183-6070-3ae7-8d4a-1ff9f1d3bd7a | -6.96086 | -49.40261 | 2025-10-29 04:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b3cf880-e8bc-39a1-be80-6e1c7d5fab9f | -6.17891 | -49.31686 | 2025-10-29 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 280b6b72-c795-35b3-9167-7a5ac03653b8 | -6.14729 | -41.67397 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 57ad53fb-a59a-3e95-b6aa-b8321e462a44 | -9.31444 | -47.07142 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87f70410-3fc9-375f-ace1-37b48cfd473e | -10.9317 | -47.9914 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d124e61-8740-3bd4-8417-c6bd3319114d | -7.80017 | -46.47196 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4b593da-a180-3629-aa6f-1e5426486c63 | -7.0635 | -44.47419 | 2025-10-29 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 964ced52-807b-3e56-bc4f-91eb994671ee | -7.35091 | -43.91069 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac05d2b-f298-3aa2-9691-8aa863b43134 | -6.18021 | -41.69952 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4e993cc3-71dd-37a0-a261-ec8d319ea9ac | -5.59313 | -51.13056 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ca2bd53-a6f1-39eb-b68e-ed13b7a42b02 | -7.80076 | -46.46832 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48ec36b5-6c05-34b3-9a54-6422ce0f123a | -10.21383 | -45.95003 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 535b3add-1bcc-317f-aa1f-d77b4ca42c8c | -7.92955 | -45.51835 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07e9b6c8-8866-38f8-b2b8-e4c1d18e3cb9 | -10.38683 | -47.11726 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c83e52e5-2444-3157-b0d5-e60ddd09dc5f | -7.72991 | -42.18772 | 2025-10-29 04:23:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6541b2d3-0479-3126-be9f-6e14120ae4b0 | -7.79517 | -46.45998 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6552590b-4464-36a6-bac3-5ccf16d20ee1 | -6.13459 | -41.70973 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ad89b4ad-4c50-3497-8f3e-a6c0bcb14cf9 | -10.51659 | -47.73087 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 387cc26f-81d2-386d-8abe-79643e7f5d0a | -9.44366 | -46.90005 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c6d7cf7-1c37-3315-bfdf-3ba2ae5ddee9 | -7.64306 | -46.92606 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a414c2b4-d98d-31cc-a66f-da68ac68ec76 | -7.19677 | -46.74727 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88c196b5-a01b-3095-99ef-9e94eea1f868 | -9.36792 | -43.68179 | 2025-10-29 04:23:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ddf4593-818d-3f1c-99b5-083e8b9269e0 | -10.52222 | -47.73968 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86e56d67-a798-3d54-a53d-038ed160f29d | -7.27054 | -46.9009 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c9b1ca3-0054-3fdc-809d-f9f989deacdf | -10.57252 | -49.84277 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bea9654-aa95-3a93-954e-598302c712f0 | -7.42927 | -41.86005 | 2025-10-29 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bb68d98c-bc89-3857-81fd-448bbf26bce3 | -8.19081 | -46.95183 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6878a64-eb3a-3620-b99c-74a025e0eb0e | -10.87968 | -47.99477 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c89b74b-b9a3-3208-a1ec-1a45f98fdb5b | -7.79899 | -46.47924 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d59ec594-1672-37ab-a8bd-e46438d998d3 | -7.37964 | -46.22318 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac52d7dc-3814-37fb-b6c0-fe707f66ee15 | -10.55026 | -44.83898 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1166af3f-e5b3-3509-b163-48b548d4088c | -7.30493 | -45.68376 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84e9e9ad-4056-3736-98a6-2a89363e7cc6 | -7.95799 | -47.84961 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea84b885-fabf-3803-a14c-e214f9356d86 | -6.13992 | -41.69123 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8229bc22-742e-3d54-a5f4-3091608c2498 | -7.2772 | -46.89391 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 68c665d5-e44b-30cf-8a71-e8f880eaa39d | -8.29278 | -49.31197 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18588d42-5a4d-37d4-8205-50c17a5b0177 | -7.98168 | -45.53385 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b9bea57-ddd5-3ce7-af75-dd76ac97b18b | -5.08712 | -47.7183 | 2025-10-29 04:23:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3170135e-35a8-3263-88e2-6c7899d1c73a | -10.22215 | -45.94054 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15c35a91-4992-38ba-ac56-7e43ede39f07 | -10.20774 | -45.94547 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9efa6002-9cd0-362d-94d6-b4b7d1716f74 | -7.34441 | -42.47405 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 60bc5e95-2714-3582-a891-b0238192af3b | -6.1064 | -42.46342 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 452c4879-8b1f-3bc2-beab-a38aa9bd7d34 | -7.12929 | -47.20187 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d28e479a-c11b-34cd-ac2b-9977f6698207 | -6.94313 | -41.55418 | 2025-10-29 04:23:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README36.md)
