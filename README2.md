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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54dffa19-e1d0-3414-bce1-df5e4f33977a | -11.162 | -48.625999 | 2025-07-16 00:37:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 535fc3ed-decc-39d8-a16e-e43538444b78 | -6.5592 | -51.099701 | 2025-07-16 00:37:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de3953f-3833-3491-bb86-886a5f5c55cd | -7.9352 | -49.662899 | 2025-07-16 00:37:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b64bfe0f-9118-343a-a694-715bd6963082 | -6.7026 | -44.335098 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57195848-46fc-32e4-88f9-8c8871f9e911 | -4.2922 | -48.107201 | 2025-07-16 00:37:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c62d79bb-0662-338d-9f28-df11320fadd9 | -5.7862 | -45.084702 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 699497fd-53f2-3cd4-bc41-bbb5d51d3932 | -7.1856 | -43.120399 | 2025-07-16 00:37:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 585df4f6-2120-34a0-bf66-6920d0ca1fc1 | -6.7123 | -44.332802 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff5afe4-ff56-38d1-bbe2-b64409130401 | -6.7243 | -44.339699 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37b803b0-5ee6-3976-bc7a-2f31dedcf5b3 | -6.6982 | -44.316601 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13e06029-70a9-3c29-84c6-c03988bf7c75 | -10.5627 | -49.123901 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca96a77c-d476-3972-8d09-00cf1365be89 | -7.1733 | -43.112 | 2025-07-16 00:37:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 216c92cb-4976-3fb0-a395-abe7ee9d0d9a | -3.3183 | -48.7164 | 2025-07-16 00:37:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0743577-30d5-3414-9c07-4b556b8aec02 | -5.7218 | -44.506802 | 2025-07-16 00:37:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 138a4321-d1c7-3682-ac1a-3b72a59f908b | -5.7068 | -44.835701 | 2025-07-16 00:37:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8a7bc99-88aa-38ab-b45a-af14daccd653 | -4.0133 | -48.060799 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e0ab84-23a7-3884-8e4e-1a63505d1e1e | -7.1758 | -43.1227 | 2025-07-16 00:37:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca0a4c1c-e4c2-300f-b0e6-557b37a5ba5f | -5.7842 | -45.076099 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52cfbbaf-4e93-3535-9cf0-bff0948edf5f | -7.336 | -49.608101 | 2025-07-16 00:37:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5ac076f-0690-3b80-8cdd-a79ab72dae41 | -7.3344 | -49.601002 | 2025-07-16 00:37:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a12b47aa-cfb2-3388-8e1c-2eb6d0c7d5c9 | -7.1882 | -43.1311 | 2025-07-16 00:37:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02990bda-1f14-3dbd-a0a0-ba3acde2001c | -4.2697 | -46.362598 | 2025-07-16 00:37:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13511758-73b4-32da-9ebc-825fdaeb5fb6 | -5.8667 | -42.398701 | 2025-07-16 00:37:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 81d7dc97-94f7-372e-9b10-299ce0559cbe | -5.7744 | -45.0784 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d39770a-5ad1-3247-b7cb-02e1cac27d90 | -10.2095 | -55.435299 | 2025-07-16 00:37:00 | METOP-C | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e84757a-fe64-32cf-a573-4a1c9a017229 | -11.482 | -48.077202 | 2025-07-16 00:37:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1afbb5c5-10a3-365b-b1ae-b36c3d9b0674 | -11.4655 | -47.318199 | 2025-07-16 00:37:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3381715-ea3a-31c2-bb68-de4745ab6960 | -5.558 | -46.532799 | 2025-07-16 00:37:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55649a37-b205-3a64-98fe-02a07ff9d123 | -8.5006 | -43.3078 | 2025-07-16 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f8cda8d0-862b-3b13-8762-a2155d61d24c | -8.8937 | -47.346298 | 2025-07-16 00:37:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dcb553e-daee-32bc-859a-144fe812b5ab | -2.907 | -48.229401 | 2025-07-16 00:37:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5a5ea2-5fca-33ba-b947-7a7f0776e693 | -6.8956 | -52.850899 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8453b5-6178-3160-90c4-447ded9e5995 | -10.2762 | -47.619701 | 2025-07-16 00:37:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a3233c8-3334-3aac-b2fb-1c6fab3a2aaa | -6.7221 | -44.330502 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15ce3253-066b-363e-993b-e635e3e4c404 | -5.4525 | -45.332802 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| beb2ee63-7dad-3e27-8fb7-dce607cbab09 | -4.2906 | -48.1003 | 2025-07-16 00:37:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e94099fc-2f49-3ad0-b543-08b65545f90c | -9.2912 | -44.843201 | 2025-07-16 00:37:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f200afd-a706-3558-826b-64d9baa6174d | -10.9496 | -49.2458 | 2025-07-16 00:37:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd79da20-4570-3c5b-9458-20b1cd33d2cc | -5.5678 | -46.530602 | 2025-07-16 00:37:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af3a9e9d-2dcb-310e-87d9-01c427665c50 | -10.2664 | -47.621899 | 2025-07-16 00:37:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15f8fdcb-aae9-3d02-86fa-c6cbe580f530 | -10.5561 | -49.140701 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ec982db-26cd-3c28-b915-759e96bd5d3d | -2.9102 | -48.243301 | 2025-07-16 00:37:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff6047a-0da7-319f-b937-1e32c09f4e2c | -2.9086 | -48.236401 | 2025-07-16 00:37:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b088f374-e2c7-3c13-94c1-e275e5059815 | -5.8697 | -42.411201 | 2025-07-16 00:37:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cffa393b-3045-3b9c-b43f-ad19ccda917b | -5.7784 | -45.0956 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9aeaee2c-068c-3dcf-97f9-53d3d0c52730 | -7.298 | -45.762901 | 2025-07-16 00:37:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d002bc0e-6fff-3919-8a8e-b5cb5a94ef7e | -9.8403 | -47.879002 | 2025-07-16 00:37:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d56add26-1e52-308f-a55f-772be9e84ade | -10.6313 | -49.480301 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9bb779f6-5788-349b-a64b-3385713848ae | -9.4843 | -48.126999 | 2025-07-16 00:37:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7250add7-42b0-30e9-900b-ae68513fca7a | -7.4935 | -46.6898 | 2025-07-16 00:37:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f0e0336-c2b1-3c28-9aff-00697a90dbac | -8.5344 | -47.8494 | 2025-07-16 00:37:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45255bd4-914e-338f-9bf3-bf154d18e01c | -4.7727 | -45.3377 | 2025-07-16 00:37:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef0de8ce-8c59-3f53-8524-f0aa09775195 | -10.8909 | -49.212399 | 2025-07-16 00:37:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 451bbb87-5cf3-32a7-b405-20363dfe1866 | -11.1604 | -48.6189 | 2025-07-16 00:37:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 314e9a65-6068-39be-8ca8-173f6e5f29c9 | -7.1957 | -45.3279 | 2025-07-16 00:37:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddfd422d-9710-37db-b88d-2de66fe090b5 | -6.7101 | -44.323502 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 197be273-e331-3627-8386-3f7d6f9679d7 | -8.6348 | -47.746899 | 2025-07-16 00:37:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2247b14d-5f2c-3b3f-99ae-981771e88cdc | -6.4096 | -45.321602 | 2025-07-16 00:37:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44ffc7b6-1586-32b3-b812-e696f6a2334e | -7.1784 | -43.1334 | 2025-07-16 00:37:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 027794f5-03bd-3a49-8960-1842770fa30c | -4.0974 | -48.2019 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9f03d8-7546-3871-91be-8c6632ae7a97 | -8.5262 | -47.858501 | 2025-07-16 00:37:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11caad98-cce4-3e3b-980e-0eef9f2e0305 | -10.6394 | -49.470699 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6325f8af-99ed-38a7-9c45-e5806d0700ce | -10.2648 | -47.615002 | 2025-07-16 00:37:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be65b612-9e9f-310a-a513-5a200ac0f55d | -6.9075 | -52.858601 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a71d5ee2-3b2a-3a59-a725-dc454d557f0f | -4.099 | -48.208801 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bbe5f95-3ab3-35f7-b68b-ac5146eb9795 | -5.6577 | -43.717098 | 2025-07-16 00:37:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9c02fa5-4c52-3ebb-8b2f-d428c6bf41dc | -11.1718 | -48.623798 | 2025-07-16 00:37:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97daad97-38eb-3b7b-967a-cbadea129263 | -10.6296 | -49.472801 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2de3250b-836d-320f-aaba-8e2d6d94cf2d | -7.8254 | -44.194901 | 2025-07-16 00:37:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae96a474-86ce-3a6a-8796-aa83d9e4a455 | -10.8811 | -49.2146 | 2025-07-16 00:37:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96b66049-8f4c-3948-bbf7-1c5dbfd7a5e0 | -10.561 | -49.1166 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d041fa77-e3d6-3d6a-9185-a5d02665b658 | -3.0287 | -48.982201 | 2025-07-16 00:37:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0621c0c7-51b2-3ba7-99df-d4b5ba06a85c | -10.2746 | -47.612801 | 2025-07-16 00:37:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39f7c524-e76c-31ee-88c8-b944ea84d0af | -5.521 | -43.879101 | 2025-07-16 00:37:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30064716-3ebe-3977-87cb-1bf03056fd63 | -4.0149 | -48.067699 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 813436e8-eb06-3787-9ac0-63ecb11795ca | -8.7516 | -46.595798 | 2025-07-16 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb635658-e40f-3fbf-b930-be4edd4751f5 | -6.9394 | -44.941799 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1174bcef-e17a-3ebf-a42c-2b9b8e7a51bc | -5.7145 | -44.8246 | 2025-07-16 00:37:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4c589c6-a4ef-3a06-ab52-bad8060a1b30 | -7.932 | -49.648499 | 2025-07-16 00:37:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 061da274-c745-3b35-813a-ead119dd2c8c | -6.9296 | -44.944099 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae36a232-1d3d-3de6-a4a5-cd99921758bd | -5.5234 | -43.889198 | 2025-07-16 00:37:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 028862d1-02ea-30d8-ba75-ffd211908f3a | -5.4545 | -45.341202 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7718b4de-0eab-3bd2-9164-23c9706cee84 | -4.7707 | -45.329102 | 2025-07-16 00:37:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d35c8949-db5a-340e-807c-5caed675759c | -8.2352 | -44.919998 | 2025-07-16 00:37:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23f0f769-9de6-3dc0-9f45-edbadd2a1c5d | -4.0247 | -48.065399 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8feae1d-c709-3269-ba89-12334d5d0cf3 | -9.301 | -44.8409 | 2025-07-16 00:37:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| daa3cf63-a511-358e-9394-c4d1efc1fe12 | -7.1831 | -43.109699 | 2025-07-16 00:37:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4197d8fe-6540-3cb8-8b9a-747c10992c1e | -5.7166 | -44.833401 | 2025-07-16 00:37:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48adad3d-ffc4-32c5-9256-ac50132d1218 | -6.9054 | -52.848801 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ced87b8-1a6b-3466-9b55-cc8cd8c7fd4d | -10.9513 | -49.253201 | 2025-07-16 00:37:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66fa26c6-81f4-3bc8-9a60-02227eed1cee | -8.9051 | -47.351002 | 2025-07-16 00:37:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7647f2a-7060-3ff6-9119-35c9c57559ab | -5.7047 | -44.8269 | 2025-07-16 00:37:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb9449b8-046b-3d01-b68f-c91307ca4ded | -7.2998 | -45.770699 | 2025-07-16 00:37:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e86acade-6130-30ef-8b9d-e1e2435338c2 | -6.9414 | -44.950298 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d62a617-9ec0-37b6-9750-c6fba2ea647a | -7.3453 | -49.7411 | 2025-07-16 00:37:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90dd070-3b12-3560-a877-07e3008fffda | -5.7756 | -45.0826 | 2025-07-16 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d81ce299-60e3-32ac-ba17-bcc2f5f57cb0 | -13.0146 | -45.0593 | 2025-07-16 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 5ce9751e-b58f-3b64-91c6-5f9215929395 | -7.2025 | -43.1171 | 2025-07-16 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| af0a8d2f-eaaa-36c6-8e67-dc8e1e744d03 | -20.3507 | -41.4914 | 2025-07-16 00:40:00 | GOES-19 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| d889d683-3fd1-3ac9-8447-28c39365d06a | -13.0339 | -45.0561 | 2025-07-16 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |


[Clique aqui para ver as próximas entradas](README3.md)
