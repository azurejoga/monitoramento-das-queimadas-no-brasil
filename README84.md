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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84d50322-9d72-3e13-83fe-3d935324cba4 | -14.4119 | -51.25341 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac4a9ad2-ded4-3991-9e4d-56d9aeb72976 | -12.644 | -47.63948 | 2026-10-01 05:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce6dedf9-858e-398e-9ddf-fc89ba5ea87e | -14.39884 | -51.2702 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fdd18e00-4842-325a-bf3b-7f44631805fb | -13.66719 | -53.94896 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8925f756-261e-38a8-881b-eb3a302f06c7 | -12.6416 | -47.63432 | 2026-10-01 05:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23238169-a488-309f-b504-ce043b7c3349 | -14.86522 | -51.84828 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0071c20e-7fcf-3806-94f6-84f21a1ec416 | -12.64464 | -47.6335 | 2026-10-01 05:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1e779c2-f781-3cd8-a1fe-83ed8c2a44bb | -14.44591 | -51.25592 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9b9d542-fcc7-3eaa-a51c-793f1f50faa7 | -14.38451 | -51.24986 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 667319d6-ffc9-34f3-81ce-8e139e6ac083 | -14.38832 | -51.26514 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 83938bc6-a6ba-310a-84f9-2bb888d9f7cf | -14.42068 | -51.32088 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ef2ce3-36f8-32bc-8924-4b8bc2f9e82d | -11.18349 | -58.16729 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8906c54-04b8-37fa-9b91-f86c63d93b76 | -17.22934 | -49.43769 | 2026-10-01 05:21:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83fe4931-7987-3b70-a6b0-e10eab700b8e | -12.70115 | -54.06779 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 281626c7-ad0b-388e-806f-6947d9db3067 | -14.15304 | -51.11754 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea673eec-39a3-33c3-b0de-9297637630a0 | -12.77548 | -54.01221 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00359f1d-e437-387c-b60a-9dea5fd1d18a | -14.87915 | -51.86716 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4eb69e6-c86f-37d8-a274-edbd26344932 | -14.87425 | -51.86311 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f0fcd85-eb95-3b75-8eef-23967ab7aa7b | -13.53362 | -49.18926 | 2026-10-01 05:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41d2dc32-bed3-3e60-80cc-0f2f1d9fe8c9 | -12.26137 | -54.00013 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 513a9a08-d04f-3636-936d-42780f8f21e6 | -14.15056 | -51.13967 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f39879c6-ffad-3fba-9c16-4695b157f630 | -12.71059 | -54.06461 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 637d0c55-762e-30c5-9bcd-52076f8f36c5 | -12.77372 | -54.02562 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c56c9f3-093b-379e-81b4-1a1a0e464145 | -13.38591 | -46.83133 | 2026-10-01 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 54e8dcfb-1d64-3c75-9920-aee5562ce75e | -14.42875 | -51.25191 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7c2df2-d4c2-32f5-9ded-59d1ada246ce | -11.18748 | -58.16401 | 2026-10-01 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 892aa9a2-f4f1-37a9-afde-630a009c0ab6 | -14.13941 | -51.13643 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ec8a6211-dad6-3dfb-bcac-40d22b9d27ae | -14.39463 | -51.25858 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0936fb97-97a2-3b70-b6f6-c18902191196 | -14.44551 | -51.25957 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ceb9f10-8c91-3bce-b017-78e58b0d3344 | -13.64578 | -53.93652 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 67c767b3-5875-3e94-ae6a-c49d1328cfc7 | -12.38806 | -54.09434 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43d81399-620e-3c8f-a85d-79f20ced5257 | -14.43423 | -51.25261 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b696556d-f811-3b26-b127-8a19189b3110 | -14.13997 | -51.13455 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 2f38b5c1-3f33-3a86-b0a3-39c5ad8a076d | -13.65603 | -53.92847 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f88e1dfa-1bf8-311e-93ba-866dc03471c7 | -14.38915 | -51.25785 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f0d747ce-c26f-37b0-9ed4-432822dbf938 | -14.86934 | -51.85905 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19f95326-1e28-3172-94e9-7296770f844f | -14.39421 | -51.26222 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 602686f0-1647-31d2-a101-3771c2526cc6 | -14.44003 | -51.25885 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13ba76b2-417c-3e65-87ec-60c004a8b65d | -14.38998 | -51.25058 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29c7e4fd-8650-3671-8718-b8aca8cc15e8 | -14.38409 | -51.2535 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29a2743a-f187-370f-8196-073f96dad4ad | -13.53312 | -49.19384 | 2026-10-01 05:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f186d9-abd1-3ab2-bbd7-9daa47dfda25 | -14.14447 | -51.14081 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9783b3e3-7fa6-3c7e-a2cf-d0345e75a809 | -14.40094 | -51.25201 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00f13b01-f198-37ae-a33f-6480d4fc34d7 | -14.43495 | -51.25447 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3721e195-78b7-3886-bb34-ab5cc8465f29 | -13.65993 | -53.93388 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 96f397ea-68d9-3bf2-9984-867ed6d17f65 | -14.88815 | -51.88199 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a674d369-b876-3494-adcb-d6ae0f242e9a | -16.4255 | -47.1862 | 2026-10-01 05:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 313c4c03-a396-3d8b-b422-762feeb5d9cc | -12.08813 | -50.69612 | 2026-10-01 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b8f8734-a080-3caa-8c67-e25a779ac02c | -12.70535 | -54.06573 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3bae96d-4069-37b3-b45a-5a1773bc6f96 | -14.4001 | -51.25928 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 382d6f79-6236-3bc5-8f77-0c92b1f0f12e | -11.9533 | -55.92217 | 2026-10-01 05:21:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bff6ea9c-a89a-38f5-ba50-a14dd1d76374 | -14.13985 | -51.13274 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b1ed1bb6-3872-3f27-9bf8-79edfbadc3b0 | -12.69673 | -54.06718 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78068c43-3ab0-3ddd-8a48-4e57e7cb80f7 | -11.71584 | -59.35242 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5171a5cd-0ae6-3a74-b0c0-78cc11d0ef4d | -13.66055 | -53.92908 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40806f84-b983-3551-9cd6-66bd949b685d | -14.86895 | -51.86242 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5f9f51a-fd96-3052-aacc-952bac79e064 | -14.39087 | -51.29129 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7910d1c2-1457-329b-aaeb-050de3589a34 | -14.49649 | -48.30717 | 2026-10-01 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 513f69f0-fedd-330b-a484-c5628c6dd874 | -14.39843 | -51.27384 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d269de4e-c5c3-3d5e-be08-68bdeb103e1d | -12.70557 | -54.06841 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf5115a5-c686-3465-a981-7d11667c3203 | -14.44476 | -51.25767 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da2be6e0-433d-3fa6-b3d2-0c31a342739b | -12.39301 | -54.09069 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec7411e3-a715-3149-9007-0c49e6f78499 | -13.65029 | -53.93726 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6851f174-6474-31e9-a702-897605bcff68 | -14.14588 | -51.13158 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76562ddd-9f0d-371b-93ce-c8bc559bf5d7 | -14.14029 | -51.12904 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7cc11ce9-7384-33b7-a8a1-2cae1432ab58 | -14.14535 | -51.13345 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a0233909-8f71-3557-8a93-7b9bd20f8078 | -16.4224 | -47.18866 | 2026-10-01 05:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d3c68a9-073d-3953-ad4b-9eafcff375a5 | -13.53926 | -49.19503 | 2026-10-01 05:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a56399de-2d2c-3ce6-93dd-29747e2e29b2 | -12.70978 | -54.06636 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01e4572c-1f34-38ba-8cbb-c40a3340855a | -14.14974 | -51.14702 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7743921e-e97e-3bcf-826c-d115c43f13f1 | -14.88246 | -51.88466 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9cfc4149-872c-3847-a390-ad487d4eaf23 | -13.37805 | -46.83802 | 2026-10-01 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 38f1e355-201a-34e3-a0bd-2fd323b0864f | -11.71972 | -59.34938 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c2f9cd8-3b46-37b9-b211-85b00946bb26 | -14.3854 | -51.29058 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c80893b7-a469-3a78-9861-37907d09b10b | -13.66778 | -53.94439 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13fbec27-376e-302d-89f6-886974831358 | -18.2811 | -54.7733 | 2026-10-01 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2982c22e-a662-3cca-9bac-f33e1f5cb082 | -14.40052 | -51.25564 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f35f1d1-1fec-33b8-8bdb-22dc2be13d52 | -12.31241 | -50.28603 | 2026-10-01 05:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abd69327-9b3a-381b-9ebd-d5c3a43f399e | -14.88775 | -51.88535 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b31603e-b61c-3c1e-a608-f9bf0326516b | -14.41737 | -51.25412 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f18e5c3-6c2c-3040-b845-689255f89fe3 | -13.6497 | -53.94185 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d8b5425-d3c8-3cb4-8560-364d30d7e44c | -14.15015 | -51.14335 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a54d07c3-3a09-3563-ba26-c3e360036955 | -13.65421 | -53.94255 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84399ad3-5eb3-39a1-bcd8-a2d8063ab268 | -14.39379 | -51.26585 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a62f0624-3673-377f-89b3-019d63f60da6 | -12.26255 | -53.99136 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01b7992e-cd09-3e45-a9cd-fe9a6783383a | -16.43332 | -47.17944 | 2026-10-01 05:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dc9c0d5-dd28-30d0-a9fa-3b1857196968 | -14.38499 | -51.2942 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adc21187-e9dd-34be-b18b-a85e579b00b5 | -12.7142 | -54.06699 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9241b13-fcbf-3fb7-a701-7a7f4eb02936 | -14.42947 | -51.25377 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20060fe9-0133-3445-b198-aab61549ed41 | -10.99136 | -58.95376 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cc68001-9e09-3f07-9b37-f13b6c6324b2 | -12.3919 | -54.0993 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2117cebb-8c7d-32ce-984a-56859f6e7db1 | -12.69594 | -54.06891 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf2fcf8-af42-3841-ac37-147c2d87e8cf | -11.25677 | -59.19674 | 2026-10-01 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa30653c-6aeb-35a6-b52a-0c2fc7b3f15f | -14.39546 | -51.2513 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75737cf0-9df6-3ef8-b623-452ba8912e6b | -13.65933 | -53.93859 | 2026-10-01 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c35f44d2-b079-3d3f-83d8-d942a5fdd8c4 | -12.65577 | -54.07036 | 2026-10-01 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9086da70-7e1c-3956-a401-6e9064b533bb | -14.38457 | -51.29783 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebaa53cb-02da-3971-b391-3936cee3a179 | -14.86974 | -51.85567 | 2026-10-01 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e3b23e74-54f7-3b2d-a67c-9690d2e8453e | -14.40642 | -51.25271 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66bafb4d-4b1b-3b9b-b8d8-7283f444cfef | -14.14038 | -51.13086 | 2026-10-01 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |


[Clique aqui para ver as próximas entradas](README85.md)
