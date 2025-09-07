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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7f40324-5baa-3f5e-a5ad-7d2d1c0be775 | -11.5979 | -47.174599 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f2c37c2-0a86-3ce7-bbf7-4e7d0e637527 | -12.0068 | -47.788799 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9813d4b-3351-37ef-a895-ba157deac62a | -13.6997 | -46.889999 | 2025-09-07 00:45:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c524e85a-53b7-37ec-af9c-d4beb9677bb0 | -13.048 | -48.062401 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb2578d-d469-3760-912d-22fef898ee6a | -10.3322 | -44.9072 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95d2fabf-a531-3ee3-a247-0e7eed52ab44 | -6.7922 | -52.819698 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdd857a1-e7db-3017-87c9-12e225dfbdd7 | -7.3245 | -48.512001 | 2025-09-07 00:45:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ef98ea7-1547-3fed-bb8f-5db583c3e0d5 | -11.256 | -46.456001 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2652759-57f3-38b9-8cf3-6089309bf16e | -7.7283 | -48.833401 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6173b191-524c-3da7-b2ee-40a8033f9dc4 | -12.5299 | -49.108501 | 2025-09-07 00:45:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9335f17-fcb5-3c40-8973-03fb29088e69 | -7.6718 | -50.309601 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f901eab-b5c4-314f-acdd-d37310f92fd9 | -13.6981 | -46.8829 | 2025-09-07 00:45:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fed3d7f2-4c68-3136-ab9e-ce7e437f7bb0 | -4.8848 | -49.926998 | 2025-09-07 00:45:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9cfd49b-5f1f-3c4d-a5df-d4eb20f6de12 | -19.8808 | -41.429401 | 2025-09-07 00:45:00 | METOP-C | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8479ebb7-17e1-3868-bf57-18fcaca2e57f | -11.7699 | -47.5644 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b8d147c-7fc8-32f6-a062-6affe6405a41 | -13.5446 | -48.117599 | 2025-09-07 00:45:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e721db5e-c537-3409-8ac4-54c6e4ed4746 | -6.0105 | -45.8853 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d72d8ff4-5adf-381e-b315-a4a1bbab41eb | -6.187 | -43.599098 | 2025-09-07 00:45:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f017d0e0-7e8d-3dd5-987f-04beea557eff | -11.4081 | -43.625099 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f67cb875-72b3-3195-850b-1bc4bbc44b2a | -7.4286 | -44.945801 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dde65b13-ad0d-336d-b50e-ded4e5f76396 | -21.686899 | -47.2029 | 2025-09-07 00:45:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ea91dc3-0e6a-3764-a5b8-acb83ebdc6a6 | -16.916201 | -45.791901 | 2025-09-07 00:45:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3907b29-0515-3a54-a1ef-903122f9ee46 | -11.5635 | -47.744598 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18a9742c-bd92-32d3-bd3d-01ade90e6102 | -8.1803 | -50.144199 | 2025-09-07 00:45:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b172b9d5-25dc-3025-b779-d9c361a482aa | -14.7484 | -47.5126 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e85e4d78-cec5-36a6-a82b-81b0b15aeeed | -7.6304 | -46.760399 | 2025-09-07 00:45:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93bf6d80-046a-3272-abf3-0cde4958c9d4 | -18.351 | -43.919701 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bad7f69e-89e1-3a41-b658-025829ea4a30 | -17.685499 | -44.519501 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca5275d6-4b9a-39db-a8f0-5bca1450eefa | -7.7397 | -48.838001 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ef1a5f6f-eb51-3d20-b16e-63226ef0ad6b | -9.6836 | -51.073502 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35225859-0cb7-3c54-a13a-e97fd5dceb3a | -11.14 | -48.375999 | 2025-09-07 00:45:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e67cd41-c051-31c4-bac2-a7ba618d9c35 | -17.219299 | -46.720001 | 2025-09-07 00:45:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af139886-b434-3ac4-ba90-fb41758900f9 | -15.6931 | -53.568401 | 2025-09-07 00:45:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 466741ad-7f48-31af-bc4d-61436162798f | -6.1867 | -43.384399 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8129a263-1762-3721-8e5d-bd5d63aadf22 | -10.3663 | -44.963001 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60e7493c-05d0-396e-a3ef-7fc65180669a | -17.360399 | -42.647598 | 2025-09-07 00:45:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 872cce0d-a8e2-3044-8317-ddad8379a004 | -21.59 | -49.1264 | 2025-09-07 00:45:00 | METOP-C | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8eaecea-307a-3112-8c2d-9a980bfcb10f | -6.696 | -51.418999 | 2025-09-07 00:45:00 | METOP-C | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6aee9df-4f92-3e71-a459-e95b77443a87 | -12.8692 | -48.000599 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58e13ccb-7cdd-3893-b923-02319f6a8992 | -13.7737 | -52.7747 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b40ef63a-4cea-3091-8863-f1a19520ebd1 | -3.5851 | -47.512199 | 2025-09-07 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbd6849-6d3c-31d1-a891-cc71aa6554f0 | -5.6012 | -48.108501 | 2025-09-07 00:45:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 48511acb-aa4a-3298-8bb2-23e2b3347e44 | -3.5887 | -47.527599 | 2025-09-07 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad0d7aff-85d3-3cd9-89d7-b9f7fec548c1 | -20.0387 | -41.2299 | 2025-09-07 00:45:00 | METOP-C | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7e29ff6-6e0d-387e-8b4a-a5f07f07f444 | -21.198799 | -44.331902 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf2a01b8-9b51-3afc-a29c-63d8aaa362e4 | -5.9893 | -44.148701 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc08629a-522e-32ea-a7e3-4e2829ec11d4 | -18.096201 | -45.174 | 2025-09-07 00:45:00 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c52f364-afd1-3828-acca-5592228e8b14 | -13.1799 | -44.493801 | 2025-09-07 00:45:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76334454-b42d-3d9d-aeec-c52b45f5ce00 | -5.9454 | -46.178299 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a774d414-5185-3d2b-88da-92634c1e1f2a | -13.0496 | -48.069401 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db7a9990-4727-3d9d-8ca3-226126f10af2 | -16.9291 | -45.757999 | 2025-09-07 00:45:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f78f34ae-23cc-3c90-8f22-bf34c9985e05 | -11.3934 | -43.6497 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab52d92-545b-393c-a3e8-7bd63947f41d | -7.6707 | -47.331299 | 2025-09-07 00:45:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a971578c-0ba2-3c71-9485-3d3ac739f96f | -7.6724 | -47.3386 | 2025-09-07 00:45:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bfbf209-d237-3a24-b01e-c7fc65d42688 | -15.0628 | -50.080002 | 2025-09-07 00:45:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7d8408a-5e6c-3934-abc9-b7c6f30b5d37 | -9.7294 | -48.974098 | 2025-09-07 00:45:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58cbdcb2-4d76-3b90-8ce6-650d18dc4174 | -8.9267 | -48.662701 | 2025-09-07 00:45:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 90c22a3a-7efe-3aa2-a88d-51facd3a3f93 | -8.1422 | -44.864498 | 2025-09-07 00:45:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74af0f4c-a916-34b3-a04c-b80bfdf69467 | -11.5651 | -47.751598 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89027605-0b6a-304a-a9d0-7f7e78edcd39 | -6.1904 | -42.6357 | 2025-09-07 00:45:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7926bb19-3370-39fb-874f-1f96a7b01174 | -6.2935 | -51.4137 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3104b1-a64a-3663-8234-833184d2cc71 | -17.0065 | -49.188301 | 2025-09-07 00:45:00 | METOP-C | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64f6b28f-6841-3d18-9062-5457613114a3 | -5.6814 | -48.142601 | 2025-09-07 00:45:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| da20d9d0-9aa4-397f-947c-5469c3ca7b9e | -4.2592 | -48.194801 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a88af39-10d5-3bf3-aa3a-8aa821946d0a | -19.619801 | -48.893299 | 2025-09-07 00:45:00 | METOP-C | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a69f72da-b20b-3d2f-b6d5-9f159bc2bcb5 | -6.0126 | -45.894001 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 634f645b-a9ca-3964-8ba6-2a9a661d0ff3 | -5.0309 | -45.319901 | 2025-09-07 00:45:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 979a1729-6942-3cee-8d88-73a61a5a7578 | -10.7971 | -47.7309 | 2025-09-07 00:45:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 175e04e2-9e21-3660-bbe7-66edb91dff0f | -7.6768 | -50.286201 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d270aa6c-37f4-3efc-bcc4-f72194e96067 | -7.7252 | -48.819698 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a0a36e31-e176-3bac-8d2a-628d92e481a3 | -17.216101 | -46.7057 | 2025-09-07 00:45:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd048a76-f5d4-3c62-a0b6-b0b6acfd604a | -8.1043 | -49.261501 | 2025-09-07 00:45:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76848e77-ec35-3dc9-83b0-4fbdd0f22fc8 | -6.7175 | -50.4627 | 2025-09-07 00:45:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b9e1d0-b0b6-3300-a51c-6a6bebf5dd61 | -17.544901 | -44.405399 | 2025-09-07 00:45:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c31f2a1c-d29b-3c6e-a5a1-4c5aa5853d3d | -8.5039 | -51.316399 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaf4ab83-75a2-3e4f-b9cc-ac2d9284ce8a | -17.217699 | -46.712898 | 2025-09-07 00:45:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 580951d1-3796-3f84-a4c2-85e0c4946a76 | -6.8098 | -52.806801 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2af40a7-0fb4-3510-beaa-05f6582790ea | -11.8423 | -50.5168 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d73f9370-4662-3cda-8649-c66d13b829e0 | -4.2575 | -48.187599 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3bb19a1-464b-35e4-a794-9b47abaf10a5 | -11.0343 | -54.1758 | 2025-09-07 00:45:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8848ec1-1ee6-3929-821f-54de9b0a0eca | -12.7597 | -52.953899 | 2025-09-07 00:45:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0afd9ae-c15f-38a6-a569-af4942981ea6 | -13.0018 | -45.223 | 2025-09-07 00:45:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2f749a9-4270-3140-8d28-da98c950e103 | -15.1719 | -47.9799 | 2025-09-07 00:45:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29bede9c-0a20-3413-a1c5-8288d5d6129d | -11.5749 | -47.749298 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d24329ba-01e0-3cb1-85ff-4e71587b7f48 | -12.9194 | -48.040501 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be615b56-2dcc-3533-9638-88c25fed2361 | -9.4011 | -46.7827 | 2025-09-07 00:45:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1573f2b7-4d50-33f1-b140-4a3d650a6e36 | -6.1726 | -45.436401 | 2025-09-07 00:45:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a30662f0-86c6-3f4c-97c7-ba52a9ba329d | -6.5818 | -43.9963 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02e7adff-8ff0-36cd-b73b-a0ae0cf02625 | -21.688499 | -47.210602 | 2025-09-07 00:45:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 926fa3d8-63ef-3918-b2d3-c6a101046465 | -11.8818 | -50.9827 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28c310d8-a42c-3065-8037-88c59baa9749 | -18.025101 | -47.1012 | 2025-09-07 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc0fc97c-e357-3ddf-8f3f-0acb0a1c3b09 | -12.7575 | -52.943298 | 2025-09-07 00:45:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c51e805-c540-3ace-a1be-3854bb868874 | -15.0645 | -50.0881 | 2025-09-07 00:45:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31a3bc6a-7cd2-3406-8a1b-44f4cd929a25 | -3.5869 | -47.519901 | 2025-09-07 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a94f88-e875-3724-8004-27ee5ea57b20 | -5.0234 | -45.331699 | 2025-09-07 00:45:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9037be58-fbe5-38c9-b185-2eb1e4427cd5 | -6.7902 | -52.811001 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 877e3544-0d06-337d-8068-6d8d881fff4d | -12.9394 | -54.786598 | 2025-09-07 00:45:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89bdf057-5560-3d2f-b96e-8c0845a8a568 | -20.07 | -43.748001 | 2025-09-07 00:45:00 | METOP-C | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b65c3ef5-9c70-3b88-b806-7d6d24e657cb | -18.0061 | -44.918598 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 67d21f6c-09df-391f-bf41-37ea023e4226 | -13.5431 | -48.1106 | 2025-09-07 00:45:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
