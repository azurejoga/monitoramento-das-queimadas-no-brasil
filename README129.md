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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d319898-44e2-3f5d-b402-dc67f6d23857 | -3.31975 | -49.14423 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da79f118-51f4-3baf-9bc2-b5e1a895d21f | -3.31917 | -50.45975 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6197bae-763e-32b1-a825-7acaad1c9a1a | -3.31833 | -50.4654 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caf9b589-b323-335f-8093-b4334c5493b0 | -3.31668 | -50.45976 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bbcc4ef-62a0-3b12-bc7f-76f78e7a4d23 | -3.31587 | -50.4654 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef572ef9-fcde-382a-8176-73e84559d65b | -3.31334 | -50.45337 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bc36c65-167c-3ce8-85a3-87dacb641143 | -3.31252 | -50.45885 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79fd5107-c3fe-31ed-b4eb-8093d9d1520b | -3.31169 | -50.46439 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5745898b-37d7-367b-a6e6-01ae95af3bfe | -3.31165 | -50.44743 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e7501de-eecb-3705-994d-071a82ee215f | -3.31082 | -50.45327 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8658b28a-4b02-32f8-856f-8f7b99d77470 | -3.31004 | -50.45878 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff1f7bf2-106c-39f5-815d-cf6709355cc9 | -3.30925 | -50.46432 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92477fb7-abc6-3652-934a-2ab327045dac | -3.30674 | -50.45212 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c023398-774a-3db8-a652-20a294814cfe | -3.30591 | -50.45767 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 931dade0-1acb-342f-b94b-bf7a737b2714 | -3.30507 | -50.4633 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0055f03e-c9a7-354b-ad78-181e609652bc | -3.30422 | -50.45197 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5beeb9ac-80e0-3d4d-8b4b-1089fa2e41ba | -3.30421 | -50.46912 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a35aa086-226c-36f0-a513-d6ff8c031c40 | -3.30342 | -50.45758 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bad40f05-ee35-3ba4-bc9a-e868dceb3713 | -3.30262 | -50.46323 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f26605d6-feca-3ceb-be93-a597b45bc225 | -3.3018 | -50.46906 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e4625ad-1532-3716-b7b1-50c93a631d3e | -3.30011 | -50.45103 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fc977b2-4ce2-3cbb-b435-90aa7c1967dc | -3.29927 | -50.4567 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0b13981-d9de-3a47-90da-4b30db142552 | -3.29844 | -50.46225 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 937bf6b9-6eb4-3846-bf17-29fadaa8a852 | -3.29348 | -50.44998 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 478dae20-d701-3fb9-96ae-bd073fada516 | -3.29262 | -50.45581 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e37f98e-30ea-3660-9edb-96dec097e8fb | -3.28684 | -50.44898 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6a28bc9-9e83-3a16-ae13-7486f14a939f | -3.28597 | -50.45487 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 334bf0b9-4106-38f4-8383-333063b2d393 | -3.27673 | -49.13787 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5251d71-fbbf-3c3e-9ae0-a4487bc74e93 | -3.27572 | -49.14476 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86860911-3d06-335f-bb9d-3e2d2dccbda3 | -3.27411 | -49.12567 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00c64f75-b719-31ad-892a-6edc563f265c | -3.2731 | -49.13282 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21f75b95-1bf6-32b0-8f87-c17f39ec6dbe | -3.27211 | -49.13986 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 98d20963-285b-38e8-9f90-a994b531c987 | -3.27167 | -49.12249 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 08837015-c32b-3eee-b9f7-6a25af2a90e1 | -3.27061 | -49.12971 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c9dc1618-b534-3909-9b8a-db73c6148ac9 | -3.26957 | -49.1368 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cdf81353-84cd-3a67-bb03-ea93c60b4f38 | -3.26854 | -49.14373 | 2024-10-06 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c030a0d-be40-3815-b5a7-e92fc799de8b | -3.24449 | -50.36635 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c657014-3923-3c25-9158-1d41aee4a992 | -3.24366 | -50.3721 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d75dc44-f018-3917-8e07-c240bb824ae7 | -3.24184 | -50.36562 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 530bf93d-ef22-3f20-8f39-15f0a931d112 | -3.24098 | -50.37137 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81e1a60b-77e8-3033-adab-91b21690d3f2 | -3.23782 | -50.36528 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b8e1359-04d2-388b-8223-7d7f9d352092 | -3.237 | -50.37101 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7632083-0864-36f8-8f62-9e0d5f450f18 | -3.23433 | -50.37025 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7706d4b5-57fa-373d-9c86-a5f28910a246 | -4.86828 | -50.76877 | 2024-10-06 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a69692a6-9b3f-3f37-bbf9-d46a5af660bc | -4.86896 | -49.9561 | 2024-10-06 05:33:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba875f0-a9ed-301a-8743-53c0b98c8506 | -4.86197 | -49.95519 | 2024-10-06 05:33:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 995272e5-d0b5-33f2-8e28-5dacabffde80 | -3.51323 | -50.84184 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebff53a5-b551-352d-a3d2-c4d257b5962c | -3.48582 | -50.80413 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0f532b7-f271-3e41-af4b-9e544115d456 | -3.4465 | -50.66287 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e03eed2-61e4-3d4f-95f9-be308b98ca2a | -3.44568 | -50.66851 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e479c018-de4d-3a3e-9638-cf1a10525e27 | -3.23608 | -50.83721 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32e3f77a-ae91-34fd-83b8-acd98acdf585 | -3.2353 | -50.84246 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e664749e-9ec4-311c-aaf3-12f33fbdd3bf | -3.22958 | -50.83641 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42b74cfd-0e2b-3023-bd48-9873a9df0f5a | -3.22879 | -50.84172 | 2024-10-06 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63f2717a-833c-30bc-bce0-d3414fe5526f | -4.66741 | -50.98661 | 2024-10-06 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c29e54a-f967-3eaa-bf22-dd9694656499 | -4.66665 | -50.99202 | 2024-10-06 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 447e57ff-06cc-38e8-a88f-b7fb343673b0 | -4.10401 | -51.09874 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 806d827e-0dfc-3e96-bd23-5919244fd36e | -4.10331 | -51.10365 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8301160-5f42-3743-a540-acca1bdd5f55 | -3.91128 | -51.24091 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bef8a9c-49bf-3b04-8a78-4996af6f5466 | -3.91054 | -51.246 | 2024-10-06 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6adbc404-af34-3b91-8d6c-6dbd50ee86a4 | -3.03967 | -53.03806 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8941380b-9711-3e97-ad45-db1bf5cdb214 | -3.03673 | -53.03911 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86019a3a-ef01-3995-93c6-f28fd57fbf5b | -3.03616 | -53.04288 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a461536-c440-374c-83a4-a675bcc729a4 | -3.03406 | -53.03714 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8600a308-bfee-34bd-b197-73c96cdcce91 | -6.22885 | -53.33012 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 895f89ba-5e41-3fb7-8a7f-0a6092834e16 | -6.22831 | -53.33405 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3bf711-9f9e-328c-84f0-550a7007beda | -1.75026 | -54.00724 | 2024-10-06 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81cf70d2-05ce-3f0d-a2a3-42663015c60b | -1.5565 | -54.77523 | 2024-10-06 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62c99976-768d-3936-abe4-da4c95b45432 | -1.55164 | -54.7744 | 2024-10-06 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14c51402-2c32-3811-b49e-ff96ec85b1d0 | -1.22347 | -54.22133 | 2024-10-06 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fcecce8-e072-3431-b74a-3fcd7ee3ab77 | -1.22302 | -54.22425 | 2024-10-06 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c91b2306-283d-37d8-9ecf-f6939442230f | -1.03985 | -53.53909 | 2024-10-06 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39db2f46-a36b-355d-84cf-98b4acf054f9 | -1.03936 | -53.54236 | 2024-10-06 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ebac0a7-1526-34b1-9c03-6fb1425c7d0f | -3.06705 | -54.7753 | 2024-10-06 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a1cb7bdd-b5fd-3078-895b-d88aeffd7140 | -2.9567 | -53.72388 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebf6bb14-d598-390a-a5b7-5f28e03e00b6 | -2.94892 | -53.70215 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3a4a85c-6035-3dfd-979e-5a18c8daa09f | -2.94842 | -53.70552 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07499ea2-8231-31e2-b525-64bbda5c41e4 | -2.94794 | -53.70887 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2afc06d8-22e5-35c4-a707-2e1ad7678f86 | -2.94672 | -53.70248 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f58aa7ac-4cc3-3da3-983e-2c4cbd9a67dd | -2.9462 | -53.70583 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcec861d-fc58-39b7-b9ba-ce50d30a6685 | -2.94569 | -53.70917 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb5d1603-de34-3c66-b8a8-0cf388151d9a | -2.93867 | -53.69712 | 2024-10-06 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 204e66e7-60e7-3f77-9a81-de7a32d2a136 | -2.811 | -54.58545 | 2024-10-06 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c16394f-afef-3e8f-aff6-dc456051acd3 | -2.80981 | -54.58271 | 2024-10-06 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001f85ef-3c17-3167-a4a8-3c33cdf06d88 | -2.80939 | -54.58562 | 2024-10-06 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e003fdc-43ca-3566-866c-c416c7beac68 | -2.60844 | -54.54369 | 2024-10-06 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c93b300-4d92-3eb2-bf78-97bb566ae369 | -2.60798 | -54.54663 | 2024-10-06 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 544bd795-a7ca-39e1-bd54-2cb9e1d04c16 | -2.6067 | -54.54413 | 2024-10-06 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eae6550c-cf3d-31e1-b6e9-7748a2b8fca8 | -2.60627 | -54.54705 | 2024-10-06 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50e1e01c-7540-3e6f-b0ee-5f623b519d7e | -2.60297 | -54.54573 | 2024-10-06 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 572d07b8-3dde-3909-b708-31c97fe9631d | -3.85508 | -54.01519 | 2024-10-06 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b92d32a-24fc-3fbd-9ca1-88415f6ac9b9 | -3.85459 | -54.01846 | 2024-10-06 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da15813-c3ed-3c76-bab7-c7449e416948 | -3.85347 | -54.0147 | 2024-10-06 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41f23837-7ccc-3250-9e63-6587cbc3f5fb | -3.85301 | -54.01796 | 2024-10-06 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 555fa2fe-b55c-3087-a80a-a693fccb1566 | -7.98086 | -54.76622 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5363720-8a14-3a92-a9fe-507725e0cf52 | -7.98041 | -54.76956 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b47561d-eef2-3b2a-b748-8dec8d3fa27d | -7.97995 | -54.77295 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 518bbc9a-0a1c-3d91-a50b-55fa7062ee68 | -7.97781 | -54.74837 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5100a46d-859e-3bb0-b4be-2fff67b519e4 | -7.97734 | -54.75182 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50f27cf4-efaa-3bda-9328-ef01d3f58fae | -7.97687 | -54.75525 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README130.md)
