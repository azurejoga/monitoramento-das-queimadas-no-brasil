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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 259c3ce0-cce1-3627-9a9c-c11e28837aea | -6.12881 | -50.95271 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 231260eb-ecc9-34bd-a29d-deebe62dbce6 | -6.12823 | -50.95633 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbb94a00-113a-32e1-98b7-b21a3a15a0d3 | -6.12765 | -50.95995 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cef18c30-ecd8-309b-817f-c9c585f48ce6 | -6.12428 | -50.95939 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 485f16f7-70e6-3917-871a-f0157460e27f | -6.1237 | -50.96301 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d06bb8cb-5b5e-3581-8182-48293b847b2e | -6.12196 | -50.97392 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9849fe15-b2b8-3087-9691-a539f1a7bfe6 | -6.1209 | -50.95884 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5853babf-91ac-3798-8205-a95b28931b4f | -6.12032 | -50.96246 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 991198a0-95cc-3af5-b45e-c255fd34b317 | -6.11974 | -50.96609 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6fde541-6b26-311b-a02e-5f330e9c598e | -6.11916 | -50.96973 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86a8d50c-1d2b-3658-8c7f-15f3ea3e7fec | -6.11858 | -50.97338 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa9a28e0-c2d1-3213-baee-dd52f68dbf7f | -6.11694 | -50.96192 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09c22b06-1bf4-3775-be4c-1108919e04b8 | -6.11636 | -50.96555 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bdd3c62-6606-3fbc-946c-b6db4c702b40 | -6.11578 | -50.9692 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93170f53-bee5-362d-9425-bbd9eb6d085a | -6.11519 | -50.97285 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b324085a-078a-3594-9456-664d989961de | -5.84673 | -49.87903 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24b6885-efad-3fbc-9291-a16883575188 | -5.78554 | -49.83392 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12c9ef19-9912-3186-bf98-a0e66679b82a | -5.785 | -49.83739 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abede734-a7ba-3a25-b4e9-945958dee18b | -6.20044 | -51.18537 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da58e452-18ac-37e2-8d6d-1e87093f8f73 | -6.19704 | -51.18479 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76206f5e-2337-34d1-a2b6-7a5103d18eab | -6.17087 | -51.19574 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd12679c-8ed0-34f2-b609-e30d3c97a810 | -6.14109 | -51.11531 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f001196-a200-3a67-b698-7150746619a3 | -6.13712 | -51.11842 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d20c0f5a-631d-3465-8ce0-5a519677e08e | -6.12638 | -51.12027 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4eae32cd-e4ac-31d0-b842-b2332b98831b | -6.1258 | -51.12392 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a7441fe-b64c-389e-83aa-5bc616ce9ce5 | -6.12521 | -51.1276 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8d3809c8-3e71-3542-824f-9bc3bbeba458 | -6.12417 | -51.11231 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9874acb4-6f2a-3425-a6e1-d01748359905 | -6.12291 | -51.01131 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5264e50-a914-3351-a8fa-5846267bc648 | -6.12241 | -51.12331 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a175d06-f404-35df-875a-cd699bc18cb0 | -6.12233 | -51.01495 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c50ca8d5-4c73-3f41-abb1-16bac63f06ad | -6.12182 | -51.12706 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e494b55b-2a61-3d67-8fc1-f4cfeb78b926 | -6.12116 | -51.02225 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1aa88981-7922-320a-ad64-31ea96dbb60e | -6.11953 | -51.01076 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31c385a4-1019-322d-8093-b3913b1401b4 | -6.11902 | -51.12276 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 049b3017-3b74-3be3-8e77-5c67afd23a40 | -6.11895 | -51.0144 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc05578d-bfe2-3be7-b5c8-79ae4ac091dc | -6.11836 | -51.01806 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73e85724-de88-3d6c-aeb4-44a899f42836 | -6.11778 | -51.02171 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd4d000-149a-3750-822a-d92a040d9fce | -6.11731 | -51.00295 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f80dc048-73c4-37d9-95f4-924fa5b3d5e9 | -6.11682 | -50.98432 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acc4aba9-1ce6-35aa-9f79-a19fe2453d99 | -6.11624 | -50.98795 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c44c51c-df74-3411-8cb9-e0cd4239546a | -6.11621 | -51.11853 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d955848b-b475-338f-b4fd-28b845f85700 | -6.11562 | -51.12228 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be46c149-3c3b-366b-a240-998282e24ac7 | -6.11501 | -51.12606 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fe9bfef-c1e1-3ecb-a117-2165461e0507 | -6.11393 | -51.00239 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a686c3a8-12ce-367e-badb-0c8563b79fd6 | -6.11344 | -50.98379 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74ce1479-c990-3bf1-a1e3-4899333ca7cc | -6.1134 | -51.11436 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57ae0df8-6e60-3201-8c30-3c5b47e0ea51 | -6.11286 | -50.98743 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6efdfc9d-f875-31d5-acfd-e970b3c4dbeb | -6.11281 | -51.11808 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02835371-3953-3d35-b68b-48e288b7ffd6 | -6.11221 | -51.1218 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32970b36-3685-3aae-bde8-ad4fabbbfa50 | -6.11169 | -50.99469 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c452c463-af70-362e-a8d4-d485caaea90f | -6.11161 | -51.12557 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 525f570b-b658-32c1-9c96-ed35ecae11ca | -6.11112 | -50.99829 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55c590b5-1035-35da-a722-e73b9ab6c0eb | -6.11101 | -51.02064 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce4dc81-db42-3eb3-8632-f78e1b885bca | -6.11057 | -51.11025 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 52a26e0a-92cb-35e1-8613-919230ca44d1 | -6.11042 | -51.02428 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec017339-26c0-342b-8da8-863b75bbc4f5 | -6.10999 | -51.11392 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6441a40b-896c-34fd-a4de-8efc0281129f | -6.10939 | -51.11763 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3aee3d2b-3134-39dc-a8d2-e7effd5e9f0e | -6.1088 | -51.12136 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c72c7ea6-ae5a-3993-92e1-3e112e18cc55 | -6.10703 | -51.02378 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914d787c-276b-3fd3-9014-a493cd1c806e | -6.10056 | -51.08589 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 253a51df-f1b5-3c90-acd3-ac1d9aee621e | -6.09779 | -51.05975 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5789fce-c0c5-36a7-bf76-47e3ffbc0680 | -6.09722 | -51.06331 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02585722-c18e-316c-ae6a-0494231e2223 | -6.09717 | -51.08531 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a78b1dfe-5933-3342-8d26-d7a5c650754e | -6.09658 | -51.089 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68df52ef-5ee5-3bac-aaf8-faddf05eb714 | -6.09498 | -51.05562 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ec67f6a-f17b-3820-9d51-9ccc3dfc6a14 | -6.09441 | -51.05918 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5f9d169-5b41-316b-a1e5-dba00753734a | -6.09437 | -51.0811 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e508632-6ba6-33d5-8cbd-8d01e6bf88fe | -7.17679 | -51.14606 | 2024-09-27 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c2567df-fc26-3f82-909f-52412ac90a08 | -7.17342 | -51.1455 | 2024-09-27 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6598867b-6fd5-34a2-b440-02576b6801d9 | -7.11629 | -51.26321 | 2024-09-27 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6795a28-7378-3ea7-a40c-da6a8b06ef44 | -7.09313 | -51.24777 | 2024-09-27 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfd2b54e-6b93-3e4b-b2d8-f567c7c148bf | -7.08975 | -51.24715 | 2024-09-27 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acc53b1d-fa25-387f-8ccb-da2f206a2ca2 | -7.08915 | -51.25092 | 2024-09-27 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a252bd-4e50-3fb0-bc2f-120cdd95c69e | -8.12146 | -51.17561 | 2024-09-27 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37feaffd-0143-345b-8440-87293de52b2f | -9.33532 | -50.73957 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd25e702-ec6b-3ef7-a646-fa449daa5ba2 | -8.60518 | -51.46832 | 2024-09-27 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc2e3116-5bb3-35f2-98a6-2414d7947866 | -10.8018 | -51.02201 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c71cfbc-1f7c-3f9c-86e0-3625e3f81f2e | -10.73321 | -51.06796 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 7457f220-e885-3dd3-a332-533947ec0c91 | -10.73265 | -51.07148 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7533433e-5ca1-38f2-a24f-9f9f346a1dae | -10.73209 | -51.075 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fe03c167-05b2-3242-8be7-b511865b1e43 | -10.73154 | -51.07852 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| caadb19f-ded2-322c-bd3b-0ecc5d0ccab6 | -10.73046 | -51.0639 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 787c6553-dbb2-36ef-ab91-27ebc39f6a8b | -10.7299 | -51.06742 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| cafa5129-79a1-3caf-98b5-7fb90fc1cbc9 | -10.72934 | -51.07094 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2b8297bd-ee87-3162-a05c-939f0fedf240 | -10.7277 | -51.05984 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8b9cc76b-9514-3d61-890c-fe81d7320ff6 | -10.72714 | -51.06337 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 149634cc-d03c-32bd-b63c-5df392176f58 | -10.72658 | -51.06688 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 6a2d15b8-97b5-3589-912e-4340487c7472 | -10.72602 | -51.0704 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60ae423c-6a73-38f3-b005-55357b8fa8d6 | -10.72547 | -51.07393 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3f2d54d-aeb5-34d3-9c4c-eaf26e6dd9dc | -10.72439 | -51.05931 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 33726a7e-6e1b-3827-969d-54f38b829fac | -10.72383 | -51.06283 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 40e6393c-bf3f-3903-bb0c-a7967c71d38a | -10.72327 | -51.06634 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| a01812aa-3ee9-3fa9-943d-e8519a0e803a | -10.72107 | -51.05877 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 568b2dcb-34e0-320b-99d7-240553a8db1f | -10.72051 | -51.06229 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dcb906a8-8acb-35f6-b3a1-22bc5b370c4c | -10.71995 | -51.06581 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76d45d84-bc30-3d0a-a18c-4e09a2605dac | -10.7172 | -51.06175 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 833342f0-67e7-33ee-a546-c6ef94107e88 | -10.71664 | -51.06527 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9f70c87-b20e-3e9f-814e-df0c9a850abd | -10.68918 | -50.98148 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a52ce1ea-e373-31d7-944c-348009470a4c | -10.68643 | -50.97744 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba3e2c22-7b92-3300-9d22-c5dbbac12a18 | -10.68587 | -50.98095 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README93.md)
