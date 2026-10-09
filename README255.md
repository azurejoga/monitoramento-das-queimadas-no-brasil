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

## Dados Diários - Página 255

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44a6f696-b090-3f67-a852-981304eff8b1 | -2.9173 | -57.2151 | 2026-10-09 15:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1bfd4cd8-52ea-3c24-a655-5d11f7347862 | -2.7613 | -54.0941 | 2026-10-09 15:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 41ebb9b1-42a9-329d-b631-89a75b9113e7 | -20.855 | -44.89204 | 2026-10-09 15:56:00 | NPP-375 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 9a71fef5-c5ff-30a0-91ba-2a21d5fca685 | -18.63765 | -41.35456 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| de0de76a-bf53-331b-a94b-c603bc23d34b | -19.29104 | -42.21481 | 2026-10-09 15:56:00 | NPP-375 | IAPU | MINAS GERAIS | Brasil | 3129301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 789813c3-adc7-396d-bda9-7260c2b9eae2 | -19.08887 | -43.99238 | 2026-10-09 15:56:00 | NPP-375 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bff2990a-5d43-3a46-8cdf-954c5b6b6de4 | -18.64458 | -41.35015 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f68c24ab-7e92-39bf-8a5b-efb08b67b905 | -18.63911 | -41.35032 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 603753d2-0459-339f-a3ff-e2a3b19d09c9 | -18.73596 | -41.86845 | 2026-10-09 15:56:00 | NPP-375 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 040267ac-338f-3159-8e79-3e7a7e0ac8a6 | -18.63371 | -41.35119 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| c4ee80d1-763f-3a83-9203-50d872c5bae9 | -18.62901 | -41.35896 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 96cf250c-4c6b-3609-97a6-475879a35a0a | -19.86572 | -40.26353 | 2026-10-09 15:56:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cdf3eebe-7898-300c-a789-03d24ac58a65 | -18.64351 | -41.33965 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 29ca5903-7d4e-3247-b2fd-9977bf492192 | -21.2768 | -43.92229 | 2026-10-09 15:56:00 | NPP-375 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0ba38425-d88c-3af9-a1a0-f0a286c255fe | -18.6344 | -41.35802 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fc28108d-09dc-3e95-b0dd-8eaaf2b09d6f | -18.63149 | -41.34829 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 81741ce7-1691-3540-b983-d01ce09f53b1 | -18.63472 | -41.3612 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 261d9b5f-1157-30f4-97ad-bc1e23fbc19a | -18.73556 | -41.86448 | 2026-10-09 15:56:00 | NPP-375 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d7720d9a-4e24-312b-83ae-b7574ea3f0be | -18.73518 | -41.86073 | 2026-10-09 15:56:00 | NPP-375 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ea86b36d-9875-3c56-b2f0-1241862705e7 | -18.63261 | -41.35872 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6ed22847-3035-367d-8360-49b844c8f727 | -21.09242 | -43.8989 | 2026-10-09 15:56:00 | NPP-375 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 06365ae5-dbdc-324b-adae-81c3bf3fbc80 | -19.11833 | -40.55885 | 2026-10-09 15:56:00 | NPP-375 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 85271362-9f95-31ae-8fb5-fcfb79ab0ac1 | -18.38617 | -40.31472 | 2026-10-09 15:56:00 | NPP-375 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 64c8734a-f9ba-34c3-8236-0a613552319e | -18.64194 | -41.34353 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 2097b04f-d150-34f8-b099-21c5a3818ed3 | -18.64421 | -41.34651 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c5656615-b604-3e23-913d-f219c6afcdcd | -21.93944 | -43.02636 | 2026-10-09 15:56:00 | NPP-375 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b23813d9-c636-3906-816b-855f8712f8c4 | -18.64271 | -41.35068 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6af0be54-c561-3f2d-82e6-126cb0c6b5f8 | -19.96775 | -40.63332 | 2026-10-09 15:56:00 | NPP-375 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bd3552ef-a9c0-32c1-ae14-f5499ed2a6cc | -20.29262 | -42.41132 | 2026-10-09 15:56:00 | NPP-375 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3357286c-f609-3009-8e2a-2787d78d4cd2 | -20.4643 | -44.19362 | 2026-10-09 15:56:00 | NPP-375 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b59d3bff-2a79-3a3f-8bb6-4b5a2fad015f | -18.6311 | -41.3447 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2555bd6f-734f-398a-b4bb-172510ea5dad | -18.63334 | -41.34745 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 553e15c0-acb0-3fdc-ba37-945648b7ab53 | -19.17778 | -44.90481 | 2026-10-09 15:56:00 | NPP-375 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4bedfc2-6441-3b98-b234-9ba164fda566 | -18.63726 | -41.35096 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 287f2975-018a-3dfe-85fd-a54590a8643a | -21.09784 | -43.89891 | 2026-10-09 15:56:00 | NPP-375 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 709c5ded-6617-3537-b9d8-c1ea2a384a39 | -20.46186 | -44.19178 | 2026-10-09 15:56:00 | NPP-375 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 94dae826-81ad-3def-88ac-4310b47fcf92 | -19.11315 | -40.55946 | 2026-10-09 15:56:00 | NPP-375 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1953c6e1-a3db-3406-8fc8-2b24faadf5f2 | -18.63299 | -41.34396 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6187012e-c635-336d-b4ed-338409fa012f | -18.74088 | -41.86098 | 2026-10-09 15:56:00 | NPP-375 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6136a368-d861-3ef5-b869-7ad3804c9485 | -18.63295 | -41.36186 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 97e14fa5-177c-39f0-bd60-375b9b8afbf7 | -18.62869 | -41.35579 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bd67ead6-e331-3a1e-898a-bd31eb9e7d3c | -19.32984 | -40.02866 | 2026-10-09 15:56:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4111769a-0cd6-3cfb-b1b8-7b3bcaf4576e | -18.63807 | -41.34005 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 18fd7b47-9528-312b-abe4-b229b70428bb | -18.64231 | -41.347 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d7912786-df91-3595-9fa8-008c774d36e0 | -20.46858 | -42.49385 | 2026-10-09 15:56:00 | NPP-375 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a85ac69b-c490-3ed0-8e11-51a5c5edcbc7 | -18.62932 | -41.36206 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1e2de544-dae1-38c4-ae38-c44bcbb075b3 | -18.64386 | -41.34303 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d7c22c9a-63b1-3fa0-bd1b-863b3cf38f4a | -20.45988 | -42.14025 | 2026-10-09 15:56:00 | NPP-375 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d9013009-f0ee-3463-ac4d-0ba0fa082a2a | -20.21566 | -41.84723 | 2026-10-09 15:56:00 | NPP-375 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f7f3a28b-c50d-3ccb-bee0-0cfd90f35dc8 | -20.18787 | -41.8578 | 2026-10-09 15:56:00 | NPP-375 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0607e32f-3c6d-3853-8bbe-74ea04496ccd | -20.85457 | -44.89344 | 2026-10-09 15:56:00 | NPP-375 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1d6bc20e-0c84-3663-9ad3-e11ff9260019 | -18.63649 | -41.34383 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 590a575d-0a68-359a-89c0-8d60288ac408 | -19.32948 | -40.0271 | 2026-10-09 15:56:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7905fb94-03d1-36d1-a047-acf374ab1ced | -18.6384 | -41.34325 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d11bee59-d2d8-3038-b55b-342564934764 | -18.61966 | -40.00695 | 2026-10-09 15:56:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| a32f9039-51aa-3bd1-985d-4773f9ac0384 | -19.10125 | -45.52477 | 2026-10-09 15:56:00 | NPP-375 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe48d48-1db6-3a5f-8f02-972128cb70a0 | -19.11799 | -40.55556 | 2026-10-09 15:56:00 | NPP-375 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ba4e5df0-3366-303f-b169-6024fee8a8c6 | -18.64158 | -41.34023 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| a4f92f2e-a03e-3f22-b390-faef21f803d6 | -19.18253 | -44.90587 | 2026-10-09 15:56:00 | NPP-375 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b0559a95-5867-3bb2-b83c-ed0574ff6fd5 | -18.63227 | -41.35552 | 2026-10-09 15:56:00 | NPP-375 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d8838c97-5e87-3196-8757-759b60d25a16 | -16.64725 | -39.74556 | 2026-10-09 15:58:00 | NPP-375 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 60836bb9-55e5-39b1-b205-b4cfb1a6c006 | -12.13418 | -43.3104 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 7b945d7b-66e1-3ee2-a22e-a05fe472f599 | -18.32932 | -42.37874 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f25a00b3-289b-3e66-b333-4f4db9364afb | -16.27129 | -44.17574 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 54366d02-3f57-316f-8482-7619cdcdd4f4 | -12.21941 | -44.62006 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9af323a1-72e8-3a07-b19c-96a5106cc64b | -15.09833 | -39.87817 | 2026-10-09 15:58:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 75e5888c-5be6-3cfa-9549-4c47f9331821 | -11.99301 | -43.46476 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 40d2c34b-6a88-34fe-a6e1-fa5e3b5f0ab8 | -14.65351 | -43.52603 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 5bb46dc1-7c76-3ab6-ab5d-583bdce933c2 | -11.59891 | -43.70327 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 52b12c77-a992-30b4-95de-2a6fe171b229 | -12.21841 | -44.82758 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a6657366-2f2a-3cd0-8349-980cf6e18829 | -15.38825 | -41.9048 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| 04b3e9b2-a500-3bc5-949b-d76bd80a928e | -12.17896 | -44.6487 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b4b651d9-69e5-33c9-acba-4ecb23e07daa | -14.32452 | -41.29969 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 596767cb-ab82-3bf9-b163-64e17e3cab4e | -15.38865 | -41.90823 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 204.9 |
| 637a6e46-c98e-372e-8c03-6df6848b5ebd | -11.77745 | -43.52867 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a828491-e988-326b-9a04-11482589032b | -11.66384 | -46.77826 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a20e8d38-037b-3e74-9e63-69ca0ef5d48a | -12.90415 | -43.46091 | 2026-10-09 15:58:00 | NPP-375 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cab2b784-29f3-30b2-8dc4-3b889ea95e74 | -14.44206 | -43.93641 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 7383e006-7d78-39a6-804a-c7ad3581ae79 | -12.00171 | -43.44152 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7061e49c-6716-3e5a-a070-2b53a99ee4a1 | -11.58018 | -43.64289 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 76283b1f-c242-3db2-8bfc-01e5edcecd0a | -16.93918 | -42.07726 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 0b8a988f-6c5a-327d-99bd-64aa436d3542 | -11.98301 | -43.47778 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5e8ae5fc-7067-39a8-9ec6-a7483a1054f6 | -12.23314 | -44.79097 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d3461441-b9c4-3b94-a7d5-eeb951abab1d | -11.98363 | -43.47379 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a9cf0211-af84-3c2d-98c1-1ef6de864de1 | -12.91483 | -45.11456 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8acf4646-b9f3-303a-9c5a-7b5229ce58e2 | -15.7888 | -44.68347 | 2026-10-09 15:58:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 397e0dc3-2cda-3e68-8416-b2f2ed69d128 | -11.97106 | -43.47482 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 7fddfb4f-038d-3e12-b2c5-94500e73fb05 | -17.10055 | -40.76659 | 2026-10-09 15:58:00 | NPP-375 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1ecb5103-e059-3e9a-b479-35c95589887b | -11.2069 | -40.55924 | 2026-10-09 15:58:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7d1beb36-a318-35c3-b001-d6c43a24f55f | -15.42787 | -43.31034 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 915ec8bc-39f9-3281-b128-1f0cc6a61e40 | -13.85643 | -42.6481 | 2026-10-09 15:58:00 | NPP-375 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 40db50cf-48c0-32a7-88e8-955716a13c3c | -13.77515 | -43.47593 | 2026-10-09 15:58:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4c2233ff-8d79-32bf-9941-72aeadba4df1 | -12.2374 | -44.78721 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 2e3bddd7-87a3-3a6c-9280-5ed5408028ce | -16.0064 | -41.23927 | 2026-10-09 15:58:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 88e0c5c2-8bdc-30af-9aa7-ad9586e912e7 | -16.8592 | -41.087 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| 718afee6-9f75-3a4f-aeb2-3ee621328fbc | -17.44519 | -45.05715 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 547cc0e5-765f-39c0-a030-690832d7ac67 | -17.42616 | -43.58808 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 47c69ff3-1f0c-3617-90b9-0f3a909481f7 | -14.57284 | -43.83031 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 3dc0967a-d0af-355b-9443-16ce4c92bc09 | -15.79481 | -43.38514 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88b647b5-6f0d-3ab0-8185-f1ee85ed2621 | -12.81497 | -42.34765 | 2026-10-09 15:58:00 | NPP-375 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README256.md)
