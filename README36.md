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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c1b068a-b0e4-3db2-ac33-08fb2a178cb3 | -12.5713 | -45.66914 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1878874b-839c-396a-8fa5-acbf44167133 | -14.17736 | -46.25965 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 448c8ecd-3ffd-3bdf-aac8-f1e6d69cadad | -20.02881 | -47.638 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faa44b52-f986-3ab1-ac44-f9c188fa83b6 | -14.2102 | -46.26056 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd62cf91-5f2f-33ad-bc4a-ddc42a78a91a | -18.44137 | -45.93097 | 2025-09-13 03:47:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df73dd3a-a45c-34f7-bd52-e8807f605612 | -16.41383 | -49.0508 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bccfdcff-f81a-3fb3-87f7-7254605c1752 | -15.86747 | -49.94621 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fa36d9d-df52-3202-9661-957d3203b5e3 | -15.70685 | -50.59127 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b4e7f23-195b-3148-9466-85e39d0559cd | -16.5297 | -43.73483 | 2025-09-13 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59395863-e168-327c-b300-04849a91b880 | -17.34657 | -42.63309 | 2025-09-13 03:49:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e7f4e93-219a-3c64-8f81-c1daad215131 | -16.77982 | -41.71975 | 2025-09-13 03:49:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e1fbccfa-ccc6-3efa-ac9b-9a30f8b86e69 | -16.25698 | -50.07676 | 2025-09-13 03:49:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ed8fbd9-14d0-39fe-b5b3-a43f329c1821 | -22.66482 | -53.12358 | 2025-09-13 03:49:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e22d0a31-7aea-3843-8dcb-2a1adeb64537 | -20.41508 | -50.74885 | 2025-09-13 03:49:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6b01a62e-b815-37c8-9e24-2f4834249c94 | -16.81583 | -42.21753 | 2025-09-13 03:49:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b9c77fdc-bc23-37bb-bdb4-16cfc3267fa5 | -15.45446 | -47.33826 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 40fa440c-7fa9-3cfe-836d-77b419eac192 | -14.46001 | -47.3217 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ae5d52-fe86-3cd2-8151-c48c1e597fd9 | -16.08678 | -49.96236 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 461336be-a88b-35a2-85ad-1adc0eed9857 | -14.44315 | -47.31798 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19827bdb-e62c-30d4-99aa-604da6c63b5f | -15.86218 | -49.93972 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82af4e6a-5952-3ab5-a41c-212d327d4984 | -16.06378 | -50.00539 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 048498b3-8432-32da-87ec-8d97516a79dd | -21.58181 | -48.41794 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0617eff7-7a0e-3b9f-a58e-c0eb4656c55e | -21.61035 | -46.80844 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f091123d-0d06-3345-88a2-1cb291dc9bce | -15.69756 | -50.5821 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11970ce6-79c1-303e-af7e-2e7187b32216 | -16.25191 | -50.06913 | 2025-09-13 03:49:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49f70cef-1c03-3988-9190-ab4b54968c2e | -15.50313 | -47.29771 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65a2be52-5e6a-30c0-a7f9-7a79cc28a44e | -15.14926 | -50.12706 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0a1bf6e-a6e0-3ce0-91ee-c6bdc5f12bf6 | -16.06262 | -50.0106 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 63547eb9-7f2f-3395-bfc4-5439c0961b30 | -22.18613 | -49.61934 | 2025-09-13 03:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bd1f5b0d-b47b-3c0a-889e-001b2674706b | -15.85681 | -47.238 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69f3278d-5762-3d03-8d8f-96cadb53c31f | -14.62361 | -46.35396 | 2025-09-13 03:49:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a93c97f-2cb1-377d-a0ab-2bb8b8ca129e | -23.6979 | -51.79576 | 2025-09-13 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aa94203e-1a3b-3ad0-b736-1686ce26d601 | -21.61619 | -46.79938 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 75229064-51be-3a8c-8ee6-d856867801ca | -20.64902 | -48.69748 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdb40936-f34c-38f7-9c54-73c5ed381b99 | -16.28576 | -45.68708 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbb3be17-98b2-3a1c-a88b-ded676309af5 | -22.79629 | -47.80258 | 2025-09-13 03:49:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d6c02ac-d34c-31b9-8a78-d48011ab9d20 | -15.50956 | -47.29434 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a97d5e6-07ac-331b-9ce9-187ab8046914 | -20.42057 | -50.74467 | 2025-09-13 03:49:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6479ab3e-8af0-3eca-b2c5-aa494902d9c2 | -16.85074 | -41.54043 | 2025-09-13 03:49:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a3810e4-af55-3a38-b321-7ba2ebdaf610 | -15.05486 | -46.46992 | 2025-09-13 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c60425ca-fd4c-3eb2-a574-cdff064c78c7 | -15.70545 | -50.57817 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6182b869-0ae5-3b65-ad09-4f629de04fa4 | -20.41942 | -50.74958 | 2025-09-13 03:49:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b6cae024-f83d-3db1-8b90-7448f4205350 | -15.70929 | -50.59221 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 79a657bf-8fca-35a3-ad91-a9e6edab4ed9 | -16.66043 | -40.84513 | 2025-09-13 03:49:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 08ba9cf8-6c60-3c45-bc4e-7af292f607ad | -25.52002 | -49.11039 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d61e5919-8b89-3589-801a-40343055db59 | -15.70163 | -50.58313 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3673dc1b-6dcf-34d2-9e56-30f2fd50e5cc | -22.79638 | -47.80336 | 2025-09-13 03:49:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| deae33d2-1f1c-3112-941a-433bf1296c5b | -15.16255 | -50.16125 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c8313c1-ca90-3394-893d-3323ed0bbe5e | -16.0844 | -49.97311 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c14535a1-7a09-3717-b447-8ebc241f5212 | -22.25644 | -49.56865 | 2025-09-13 03:49:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0ec89b36-f0a2-3839-863e-ee8a4bedd0a9 | -20.60065 | -50.41138 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| be3fae08-d6a3-3d49-9808-fad251a0ac20 | -20.64475 | -48.69161 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec31dc35-cbcc-3886-8bed-323d8e8233e9 | -20.6436 | -48.69611 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5426ba17-547c-3f94-b7e1-4d15c98214cb | -23.70528 | -51.79213 | 2025-09-13 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9444912c-fa1e-38c6-9df8-80b2a0ae5c1c | -20.41621 | -50.74389 | 2025-09-13 03:49:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2dfdb773-e3db-32cd-b4ec-39136ee4007f | -15.68941 | -50.58714 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3e8e026-a5c2-30b4-ba37-31b962d9a7d2 | -21.61633 | -46.80347 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0d1122c-ef33-3b6c-8e0f-0af78be86880 | -20.6018 | -50.40643 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ebbe1b54-72aa-39c5-9cc7-81e590afb684 | -21.32128 | -44.99988 | 2025-09-13 03:49:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cc27233f-9ad3-3e90-bd87-ab1f8c391edc | -20.59591 | -50.40408 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 96080efb-3681-38a2-9905-76e7d753cd2e | -15.16382 | -50.15533 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77946052-03a1-37d8-a017-4d2c688f6492 | -21.58173 | -48.42518 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b4cb3fe6-dfee-368f-8a59-407ae4b2a995 | -15.46226 | -47.32842 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce992d49-98a6-3a33-acc3-f20a233801b0 | -16.52889 | -43.73915 | 2025-09-13 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1092bba-890f-30b8-84d9-d74dacd9ceb9 | -15.71724 | -50.58803 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c4f10130-18f1-3f28-8e51-834822f3ec71 | -16.06421 | -49.99602 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2b2cd9a1-2984-3bd4-91a0-ca66a08987d3 | -15.24845 | -51.3965 | 2025-09-13 03:49:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dd251de-cfdd-3426-a6b8-cf1533e9d8ea | -15.69616 | -50.58825 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c498b3f2-239e-3ba6-bc5b-d02009fc4126 | -20.603 | -50.40082 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1b00cf4a-0f12-390f-8d9d-9562581e8f77 | -16.28202 | -45.68032 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ab2f1d5-dae1-3d82-852e-813a9e7210ac | -15.14842 | -50.12181 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1366fccb-6c5b-308a-b729-9b222c63d477 | -15.15057 | -50.12101 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5ed11a4-4335-34f3-8e80-07b2e0aa5230 | -16.06754 | -49.98849 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39866257-1d06-3be8-8534-11cd6e6594fe | -15.45599 | -47.33087 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7ae6390d-a90b-3f19-88ce-8cdf0b62c785 | -17.36259 | -42.70271 | 2025-09-13 03:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0339dea7-5ab3-3a34-96bc-525d274dd45e | -17.35862 | -42.70192 | 2025-09-13 03:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0411042c-dbcd-3baf-b005-d4e3b22bb584 | -15.04951 | -48.15664 | 2025-09-13 03:49:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 921c9177-12ed-3c66-9992-eaf69048fd8d | -16.07276 | -49.99529 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0306237e-b27d-3374-9198-8077688a4fd3 | -15.60755 | -47.93061 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 99dc483c-d2e2-3982-ad31-5f973069cae2 | -21.61895 | -46.80989 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5d25293a-4e7e-3f64-b1f4-8c6266c78e56 | -20.60674 | -50.41233 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4139e0b8-88e6-3685-9d3b-f428a4f82bc9 | -14.46225 | -47.32297 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68eeeaa6-45da-3331-8cd4-053af2b17675 | -14.43274 | -48.43381 | 2025-09-13 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8da647a-d1ac-32d4-a23e-c33ea27e7727 | -16.07947 | -49.99535 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1ea9a96-527c-3cae-b53f-c404791f29d3 | -17.24489 | -43.87041 | 2025-09-13 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a97c53e-8440-3455-8d45-5607d8b5562d | -16.65144 | -44.93254 | 2025-09-13 03:49:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc458748-3872-32ae-8620-fd470e1b4c4f | -23.14205 | -49.65499 | 2025-09-13 03:49:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 066c9f56-d395-34d3-872a-c25f71d6f44d | -21.58776 | -48.41601 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9444ca5b-2e8f-3dd5-bbad-d585df62022f | -15.16285 | -50.14987 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27a7e992-8974-3fe1-914a-8e4d654de209 | -21.58028 | -48.42482 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 13ae5da8-2e64-34b3-a936-dfba9575b6ba | -16.28452 | -45.6851 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48105be1-632d-3454-af6f-91cbd77e94a0 | -16.05622 | -50.0091 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 84f4cbd8-2425-377d-bae4-07acf891b72d | -16.6468 | -44.93162 | 2025-09-13 03:49:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a86a84db-c069-3e7e-a45e-c4973a5ec1a2 | -14.61039 | -46.33751 | 2025-09-13 03:49:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 950d0c59-6d18-3238-be27-4544adf52504 | -21.63069 | -46.80143 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 29b99812-d13f-3f5c-b6f2-003443847859 | -15.71342 | -50.59325 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e560323b-0e2b-316a-a9a3-9ef4e544070c | -21.24011 | -47.76419 | 2025-09-13 03:49:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1bc3faf-c798-3da5-93e1-2712a32730d7 | -15.60555 | -47.9356 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 21722f91-7cd6-3886-924b-a81b5aaa4ba7 | -21.587 | -48.41945 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e47a42b5-a97a-39ce-b01e-a66adc0117db | -14.43625 | -48.44225 | 2025-09-13 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README37.md)
