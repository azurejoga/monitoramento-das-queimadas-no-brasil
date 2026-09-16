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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 470e9fa9-f361-3564-8cf3-373ea227f0f7 | -6.30396 | -41.67869 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd3e0159-e600-3b34-8e5c-1e6a5bba1272 | -11.16844 | -42.7908 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b16f3118-bac8-3804-ac4d-05d0ddf7d5a2 | -8.8525 | -44.91067 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee568bf7-05e4-3ff0-8aee-e4e130c3b49e | -5.9833 | -44.83631 | 2026-09-16 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 042d810f-a78e-37b3-a0c7-c42230c2e131 | -9.8 | -46.50181 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63873c3c-fc11-3ffb-aac7-1e8377e2e6e9 | -10.59611 | -47.75534 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad3bfa8b-f49d-3dd6-bf20-19f5428eae2b | -5.53425 | -43.37816 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee6d2b61-dc50-36df-9ea6-29a4e2257663 | -7.07467 | -45.23988 | 2026-09-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8c89dc2-838b-3b60-b9b5-fe9028052fce | -11.25593 | -43.45752 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f4414a7-34db-311e-99f9-784b63e878d6 | -10.40836 | -48.649 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24d7b1fb-4c8a-3405-91ce-fd8702d2d37e | -9.57153 | -46.59222 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61c3fd01-7d39-38da-a3ef-35edb4d699a5 | -10.10272 | -45.61016 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c45eeb-1e46-3bbe-8b15-147ed6781625 | -6.39641 | -44.05867 | 2026-09-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1add0645-c734-3f70-a195-d29f4e55882a | -6.15686 | -55.7158 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 004cc9e6-1f7e-34cc-a1c6-648bd3440997 | -7.85506 | -55.45461 | 2026-09-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0277eae0-bbb3-3efc-a5d6-5c4702cd2582 | -3.01401 | -51.34501 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4422f4e6-dc1d-30e9-93d7-897f799a4842 | -5.55619 | -43.43855 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b59b9f21-1328-306f-a59a-4de90acfbef4 | -10.40545 | -48.64036 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e8f40f9-7601-3320-9f7f-89ee70fe6471 | -2.81816 | -51.34202 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1415f1f8-3f88-3f5b-ab4a-965452897c9e | -10.40831 | -48.66426 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0d1c5a5-1ea8-36be-b338-e3d6a15ad1aa | -8.55234 | -44.4892 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e010dab9-9e40-376f-bcd6-053df6c47a0c | -5.99627 | -52.10414 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94df558f-f435-309e-b97d-835c78ccd1b0 | -10.83555 | -46.20299 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc4bc74d-bef7-382f-96b3-7cb398fdcba5 | -6.18889 | -44.02921 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0943b767-5ba7-3a60-847b-23816561eebf | -8.55643 | -44.486 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c02ed2c-dc14-3707-bc1c-fcfd49cd7c82 | -4.18083 | -49.40609 | 2026-09-16 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 588f13ad-0725-3256-b24e-766cbad9c4a6 | -9.1034 | -45.73166 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 95bda73a-0b10-353e-afe5-5f1e29e38c3f | -10.76452 | -46.22221 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56376ef2-3cdb-3a33-971a-f832f2e17477 | -10.77333 | -46.2147 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afae99d8-fa8b-3099-b4fa-c80542009193 | -2.88999 | -50.42195 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4755908-c264-3ff5-8b8f-1fd4ffe232ef | -7.12317 | -42.14659 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06226033-81f3-3cde-a1e6-494821161f2b | -5.77253 | -45.09345 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e999f35d-af8d-3965-86a2-1363822517da | -11.23876 | -43.45831 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7247bef4-5137-3589-83b1-3777c37a6bbb | -5.10621 | -47.61385 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c4165244-ddf9-3eff-b57a-2416b4d1fefd | -11.23608 | -43.4325 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fddf72ad-990d-34f9-ba00-fcc1e58994ab | -5.60541 | -44.85397 | 2026-09-16 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c36ece86-0543-3e31-a160-649a551b752f | -8.84009 | -45.86859 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0badb274-2cca-3fce-bbc7-b498a0e2449b | -10.46019 | -44.94378 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03d9b7f6-137e-3f51-828e-ecb05c629ecc | -9.11141 | -45.72863 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84255147-2413-3613-9f02-f75c5bd8c5fe | -10.59332 | -47.74765 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7028e7f8-0263-3edb-aafb-c0ef24c4385a | -9.54773 | -45.422 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc32708c-1472-39fc-97be-958dabaf2445 | -5.63269 | -51.69131 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23ffc805-462a-3120-8415-33fe38cc5eff | -4.36123 | -47.78129 | 2026-09-16 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 2fac4951-b672-397a-a440-452bd574c662 | -2.91184 | -50.42568 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 695c196b-1db4-39b5-9a27-8a8cbac60554 | -7.35443 | -44.49973 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07c86211-d4e2-37c6-a197-bafaf6fff33b | -9.86332 | -49.82465 | 2026-09-16 04:14:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21d20f78-2e4c-35c9-9cfb-87d387739a59 | -7.07479 | -41.82975 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1700e21-7208-31d5-9b1f-9383e30c6f64 | -11.14102 | -40.48228 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d109bab5-6a12-33b2-a562-0d86968bee30 | -2.91965 | -50.41249 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcbc0df9-a7ba-3c97-bb62-105c842d0f4b | -9.14374 | -51.57209 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6d08b1-2342-3c39-952b-29b9f7744ad0 | -6.17207 | -46.729 | 2026-09-16 04:14:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e18b4965-c374-31b0-9304-e53546f93c6e | -7.51855 | -47.33297 | 2026-09-16 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80e9cc54-dec1-3fba-9fa0-557d179687b7 | -11.20037 | -42.82473 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2e62dfeb-e6ad-3222-915b-034f5bb06679 | -9.48933 | -45.44173 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29121218-5780-3aa4-bb2c-568917703491 | -6.82257 | -44.76194 | 2026-09-16 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 514b1f8b-f9a6-3619-9938-59a1140439a8 | -7.06418 | -46.74241 | 2026-09-16 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7906406-81fc-30dc-bebe-cb056fbc15b6 | -4.90583 | -45.67577 | 2026-09-16 04:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b514afe9-80a8-325d-a631-f57e18a04016 | -2.95506 | -50.40724 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a261f959-d90e-32c5-8db3-18cb5bbc0802 | -2.91907 | -50.416 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373e905d-4c0f-3413-bedb-aeafdd079602 | -2.88821 | -50.43254 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23b04f28-4d03-3360-9cda-70e0eee89f8f | -7.26155 | -46.176 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aff3ea22-01ff-318a-9c07-d3ace3eaf32a | -7.15801 | -44.2409 | 2026-09-16 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78edc216-ffc6-3a73-abac-0a1b8d47478e | -2.95529 | -50.40044 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32faf6b2-6133-36ce-82a8-1bc6d07ff5c4 | -7.11244 | -41.80768 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3fcda898-64cc-319b-a76f-ffa9ed293cf3 | -10.59486 | -47.76242 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9af2fedc-32aa-3e92-993d-05b60da46cea | -11.3818 | -43.94162 | 2026-09-16 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54dede51-99f8-3749-bede-a2eac33eacb5 | -9.78348 | -46.48469 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fcad9a0-6968-3ec1-afe4-48933f18572a | -3.37913 | -50.84248 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 391331e6-1e37-39a8-bf83-d57f852136cd | -6.62893 | -55.13084 | 2026-09-16 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba6b4af5-18a3-3087-8876-57dc729a2384 | -11.24589 | -43.47761 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e5e7a46-6e94-3144-ad55-2f676ece277f | -7.21788 | -44.44947 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7173680d-a817-31d6-a24c-011106f7bc10 | -5.63133 | -51.69915 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 10dc3c4b-ed9b-37dc-8234-e61f9e904cb7 | -3.23032 | -50.58399 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13be9609-cdb6-38d2-8889-06578df9a358 | -8.70819 | -49.61946 | 2026-09-16 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd83614e-034c-3232-a6c8-8eb2cc2e7499 | -11.19926 | -42.83174 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 7c1f6326-b561-37b4-b36d-9dce29b43449 | -7.17255 | -41.81367 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af353792-3a65-385c-bd54-cae92307a760 | -5.58147 | -43.56511 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aad885e-eeaa-3fa4-9b99-c44bb93e6567 | -10.40761 | -48.65334 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 043d7d93-ea3b-3b4b-b8b3-2507406f153f | -5.77989 | -45.09463 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad4e8542-928c-3c25-91f9-7f0d4ea210bc | -10.37214 | -45.12892 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 910c3c46-5816-385a-bcf4-fca2fc25932c | -2.81884 | -51.33792 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fae5c1c-aed0-3378-b1b0-8c92285ceb14 | -7.09336 | -42.09921 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bdb4c07b-172a-3263-9c76-babd1b306fd7 | -3.84224 | -51.76368 | 2026-09-16 04:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f89e7ed4-5ef6-3271-9956-fdb8f57690a5 | -10.83918 | -46.2011 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e94185cc-4e0e-332a-8a26-8a141d66c818 | -6.39231 | -44.06197 | 2026-09-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2bf004f-5bd2-3255-9960-1746a8bc1d83 | -7.57558 | -44.93612 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b703a1e-242c-350e-b176-4cd535132c5d | -9.23351 | -46.7 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 510d939f-54bb-3b4a-825c-a62d093d311f | -9.53085 | -42.96292 | 2026-09-16 04:14:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45802d44-70ae-3412-a96c-fe5fc4764a50 | -6.37114 | -55.83846 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80fc0189-162a-3e81-858b-6060224f6ca1 | -3.37417 | -50.8379 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfa97da1-8937-30b4-a81c-f7c78b1b6f91 | -6.1761 | -46.72973 | 2026-09-16 04:14:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 680b0f04-09bc-3419-b853-4ab069d49239 | -4.30094 | -49.12201 | 2026-09-16 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fa1d033-590e-348d-9306-128cd9be7ebb | -7.1651 | -42.09648 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c4e5008-80bb-3654-8493-888d32757e1c | -2.90459 | -50.43543 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27e62552-f723-348b-b853-22aed393fa5d | -10.36799 | -45.13224 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eff2b266-982e-36fe-b1a4-323a4220aa9b | -4.52122 | -54.97607 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f444511-5c05-3a51-a595-e2a43fab5b30 | -7.13803 | -42.09567 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce0c0bc6-36a9-361e-b5e5-4c862db524ed | -9.79754 | -46.49469 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf15c3a6-0c77-31d5-b320-6bf1670ef362 | -8.80111 | -46.89423 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e50a7a13-ca80-363a-b4a0-0a44ecb7f884 | -9.35138 | -50.18521 | 2026-09-16 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README28.md)
