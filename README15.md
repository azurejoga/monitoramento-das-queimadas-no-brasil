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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 896dd6ba-7d9b-34c4-9c4f-ad16695f3b98 | -7.40668 | -39.82836 | 2025-10-31 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09121879-bd3c-30bf-9044-2d9f51c84827 | -6.22915 | -42.52814 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 435da071-b11b-3ea6-b6dd-f1266c7be07e | -6.35341 | -46.21622 | 2025-10-31 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d56cb017-fd1a-3190-90b1-e3e41d2d77e1 | -6.01255 | -41.96966 | 2025-10-31 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc9f29c7-462a-3419-80f3-f2bc32ac51c0 | -4.35508 | -46.77518 | 2025-10-31 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf932d00-fa07-3503-bd37-e3d54f9f1e63 | -7.78715 | -41.57794 | 2025-10-31 04:06:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a57c602-9ed6-3fd2-9f80-96f3f622d1a0 | -5.79639 | -44.82297 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53b10005-3de9-357e-b703-9ac971927cc6 | -4.67552 | -46.52064 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aaa0e3b-a360-3975-ad4b-b6f561ab50ec | -5.5874 | -48.0493 | 2025-10-31 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efc6e469-0758-378b-83d4-9526ed7be6d1 | -4.93308 | -43.66399 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b83d8866-27bc-32d8-9c31-b9ac433c3dda | -4.30384 | -46.69114 | 2025-10-31 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 995129af-0e28-3236-9f5b-fa9670a298d5 | -6.11572 | -41.70522 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9c39da18-d540-3220-b60b-1b9f48349585 | -5.0261 | -44.81333 | 2025-10-31 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b9479a1-81b6-38ff-a2b4-410faf0d7780 | -5.29107 | -42.20968 | 2025-10-31 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e713891f-b3fb-372c-aded-557490d7a481 | -6.15861 | -41.62702 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4d9f3d3b-f2c8-335d-8162-3839f02dd418 | -6.5134 | -40.79731 | 2025-10-31 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37ebdc3d-d976-346a-9402-6a894ccdfd15 | -6.15236 | -42.39316 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 740a68b4-3e3d-3cef-9c1b-2a3889891c0c | -4.78019 | -46.87872 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e7adbe8-20f5-38c8-a570-d39404d6422c | -4.24546 | -40.70299 | 2025-10-31 04:06:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e59104b3-2150-38f2-8b66-46e1a09a27c5 | -6.10857 | -41.72889 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d0c11770-c5aa-3b3d-b98c-0f2e580e8a95 | -5.01626 | -45.56718 | 2025-10-31 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0415fbf-5172-3d93-aaf0-1e27401f4717 | -6.01532 | -41.97365 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c4229c25-0f10-38ff-989b-eba865462e20 | -5.82088 | -40.79512 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eaef9e2a-a421-37ea-b0ca-ca285242a26b | -5.90601 | -44.6321 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e23d5408-2681-3c55-b252-6ebdfadb610a | -7.31067 | -44.98021 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0856bb34-0fae-335f-acfc-57c65bd25e3b | -3.56834 | -45.35073 | 2025-10-31 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91992cee-b3a5-3490-a6cf-7a14ce7d55dd | -4.2951 | -43.70831 | 2025-10-31 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c83be2e-9f9c-352c-945f-487116d48f77 | -6.11506 | -43.52034 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1288569-9a2f-330f-baf3-5fc1e65cfde1 | -7.03208 | -41.47538 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7cc9388-0896-3f53-9639-fc682111328c | -5.03955 | -43.61266 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc0ce829-e57b-34f3-b01c-cd159f2a1a11 | -5.70054 | -43.15283 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0318a0ac-d75d-397a-8217-f3bd377e3021 | -7.06764 | -42.02393 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 57494261-82d5-3dfa-9bf6-610e47c36923 | -5.14127 | -46.13118 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6842c166-e94c-3347-94d9-72d391a9d101 | -5.96824 | -43.38512 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 37add6b3-b9dc-3535-bec1-5444c64d70fb | -7.89073 | -40.67773 | 2025-10-31 04:06:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0002ce5f-5e1a-3fad-bff2-40811fd1d081 | -2.92963 | -51.46411 | 2025-10-31 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1583cd6f-953c-3083-b83f-f71dda9f7cf9 | -5.17069 | -45.33271 | 2025-10-31 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8bbbda80-e111-368d-b755-02c8601f3bd0 | -5.69534 | -43.1633 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5c46fb35-748c-38c5-8d30-583ea444f4e1 | -5.94868 | -43.96934 | 2025-10-31 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2c4844-8007-3f90-b213-782b6f109870 | -4.42458 | -43.37186 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d75334f-5cba-344c-ae50-e93449262304 | -5.69994 | -43.1565 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d44a9ef8-413a-30db-8313-93e2518675c1 | -4.83463 | -45.32474 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af0f8a6b-619d-33e1-9f0b-7b24281c2c03 | -7.61727 | -43.62308 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c1d3ec1-dbaa-389a-b3cb-217abbd068d9 | -8.10998 | -38.76082 | 2025-10-31 04:06:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20a799f6-681c-3ec9-8ac2-2fd7a806ccb2 | -5.87889 | -44.70629 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94a93130-ee9c-3b4f-bee3-64b835c94928 | -7.32349 | -42.4864 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29109b47-5d41-3f89-b883-38407e380b84 | -3.78783 | -43.89395 | 2025-10-31 04:06:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f2ab4fb-0016-3c92-8b8e-39fc7ff2e66c | -5.80474 | -40.83222 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb14ea38-2234-3e10-8184-0aaf0de5af7d | -5.00232 | -42.10271 | 2025-10-31 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4747afcf-52cb-3f46-9be7-e5ee08482404 | -3.52446 | -47.55194 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07614f21-2592-35aa-8ff5-4cfbc5a7bbc3 | -5.80529 | -40.82874 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db8e97d4-e4ac-3959-ba5b-346870ce00b8 | -4.85552 | -42.73825 | 2025-10-31 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab666061-3d3e-395c-b58b-aa0d0d1992a6 | -2.44565 | -49.01336 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6535f989-ab6a-3714-aded-8de60777dc08 | -2.0951 | -48.04935 | 2025-10-31 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9311f4e2-97b9-301d-8681-f02b200a74a2 | -6.26937 | -41.80737 | 2025-10-31 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9815cb6e-1798-3d5f-a3e6-eb04a7ce58ab | -3.9893 | -43.42791 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6844e70c-03ad-313e-b861-e267815a900e | -4.48319 | -45.1929 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 375562df-2401-3b2b-8feb-bbf0df4e7143 | -3.53043 | -47.55125 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6644feb0-3c69-3cf6-93e4-641e84906999 | -3.58311 | -50.26704 | 2025-10-31 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fafb6be4-2761-36b5-94af-47c85f9ba386 | -4.90577 | -45.72624 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa48c22f-b212-3d25-b73c-e2b664583d55 | -5.39607 | -46.05001 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e52fee83-f932-34b4-97b3-f5c720ff8e71 | -3.29184 | -51.92959 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f84ea773-a568-3740-9c7c-94fe826af2bc | -3.29422 | -51.91553 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27cb0147-59d1-3a31-96b4-e952681528d4 | -2.9075 | -45.40805 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a7519142-3c66-3fc2-b7bf-ff3ca848c8ab | -5.13 | -40.63025 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a21d197-f9d3-3e31-ac96-f870cd85c2a4 | -3.08502 | -49.50636 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 685ce3ee-006b-3c26-af75-e740757088df | -4.98314 | -44.84287 | 2025-10-31 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb19cd65-3ec1-3f5e-b716-3069922e2670 | -2.79255 | -50.29097 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17c2ead9-8a45-354b-ab35-3b6e0080b4e4 | -6.06597 | -47.28516 | 2025-10-31 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8fc70c41-aff2-30cb-82bd-0a2799525f0e | -3.99824 | -45.54844 | 2025-10-31 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| da103053-7032-3828-989b-a26090837247 | -6.51326 | -41.34016 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 379a50fe-34c6-33ff-951b-dab72970008e | -5.85156 | -41.27067 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2917d7ae-cabd-31ee-b190-14678303999e | -5.69253 | -43.15906 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8a19504-2128-378b-b224-c5fdbba53d56 | -4.80503 | -43.02796 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 8e5c1ccb-7625-3721-a25a-5916ad49ce73 | -5.63037 | -41.09798 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30a53b2e-66d6-3aea-bfba-0b8c4b9ca273 | -4.72167 | -44.40382 | 2025-10-31 04:06:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffb948d8-2c9d-398a-b02d-b49e3ae29f2b | -1.16647 | -49.26282 | 2025-10-31 04:06:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 825551f8-922e-3cc5-834b-402bbeea7288 | -4.05414 | -40.90204 | 2025-10-31 04:06:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f86f2582-f2af-3f76-ad7a-78dc2a4014d1 | -3.52519 | -47.54736 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2336a187-227c-3034-a966-880c5e2b85a0 | -3.77797 | -42.40975 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e309fd29-4ec0-36b1-ba98-5ccf342b9069 | -7.22626 | -39.36278 | 2025-10-31 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 51421cf1-3a73-3e32-9b94-e68cc337f16d | -4.30314 | -41.43531 | 2025-10-31 04:06:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c191cc35-def2-3949-b8eb-d11dde2e7082 | -4.47998 | -46.57124 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1f76180-31cd-37e6-817d-61518b2e298e | -6.40723 | -39.74107 | 2025-10-31 04:06:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c85e1afb-398c-3182-9ebe-6b682c9d4377 | -3.9858 | -43.42734 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eccbcbe9-1ba4-312a-a1a5-5ab5fca2cdf7 | -4.70464 | -46.49937 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e98b807-9484-3a77-8074-6e6e41e0b7dd | -5.41094 | -41.23946 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c0731d64-5eaa-3097-8d88-0bec8da9d12e | -5.06476 | -43.83421 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2bf66230-a4fe-36ce-b9f5-4f162d765b03 | -4.71441 | -43.91631 | 2025-10-31 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 986fc92f-2e6e-33c6-a720-e958fdf5a5e7 | -6.12074 | -41.86576 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c7eb29aa-eb2e-398c-a563-2731c4a8bb38 | -5.10552 | -45.18333 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54067196-83ab-38a1-bc25-e4fc9bee27f5 | -6.30513 | -42.33083 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2f0e4956-d78a-36e5-b872-5e3cef25f9f3 | -4.67505 | -50.44627 | 2025-10-31 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ee11b1-cb97-39a1-940a-e789c5d45c0a | -4.67397 | -45.81251 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceb26463-64f6-3f1e-8f5b-0ec6d8f56423 | -6.66836 | -44.69188 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5aa851a-eda9-3d95-8ee6-4491b1fc5c91 | -6.05512 | -44.8648 | 2025-10-31 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e30a96fe-6998-39ca-ae90-0996553100d7 | -6.91054 | -45.51076 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 92b33a7d-f2a0-3946-a584-f99626f4678a | -6.80842 | -44.45454 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7de3629-5957-3e0a-8072-0245a2ad0d94 | -7.38614 | -42.47845 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f28b33f9-38f8-3024-b63a-8ceb7bcf9fa5 | -6.99704 | -39.14129 | 2025-10-31 04:06:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
