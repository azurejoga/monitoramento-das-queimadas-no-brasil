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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28c61436-c0e4-3d31-9096-e750ec7c5ac3 | -7.1011 | -44.572399 | 2024-10-08 00:07:21 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f891cb59-bd27-35fa-a80e-07741129d657 | -7.0877 | -44.5578 | 2024-10-08 00:07:21 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2996abb5-8229-3960-a3e3-ce33f974456c | -7.0895 | -44.5662 | 2024-10-08 00:07:21 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 371f6230-3c02-3e47-b11a-5bc8eaf9366d | -7.0913 | -44.574501 | 2024-10-08 00:07:21 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3ccd743-5b1c-3015-bbf5-cdce1ca55da1 | -6.4616 | -42.048901 | 2024-10-08 00:07:22 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b598798c-629e-349b-9cb7-2f1323115752 | -6.5426 | -42.689301 | 2024-10-08 00:07:23 | METOP-B | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02bbaff7-a648-30f1-b36a-fc3a88425af7 | -6.5442 | -42.6964 | 2024-10-08 00:07:23 | METOP-B | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f111c5a9-efae-345f-8945-ad467332ba5c | -6.94 | -44.633499 | 2024-10-08 00:07:24 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58f33434-c140-311d-bb78-0e83e0883abb | -6.2568 | -41.870499 | 2024-10-08 00:07:25 | METOP-B | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6544693c-b3a5-36f2-9ad1-30e26f789316 | -6.6951 | -43.937 | 2024-10-08 00:07:25 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 284d6cbb-bdac-355b-9ec9-5cdd345b8925 | -6.6968 | -43.944801 | 2024-10-08 00:07:25 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99e7d66d-3b2c-3abc-8a2b-b0665b8f3354 | -6.6985 | -43.952499 | 2024-10-08 00:07:25 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98285328-80d5-3a10-8d1e-94a152ef0195 | -6.6971 | -44.133202 | 2024-10-08 00:07:26 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6e8c3f-2af8-38c1-8be6-f3905f3dad9e | -6.9351 | -45.2243 | 2024-10-08 00:07:26 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22544931-e046-3693-8cf6-aed83a47d0a7 | -6.4805 | -43.336601 | 2024-10-08 00:07:27 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c918ce7-0bf2-3957-95f4-ecfe2a965e02 | -6.4834 | -43.862099 | 2024-10-08 00:07:28 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 717b0705-73ba-383b-b90b-c75e0d210aa3 | -6.4851 | -43.869801 | 2024-10-08 00:07:28 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f02b430c-5b50-3e43-a91f-ed58bddb6e7f | -6.5794 | -44.158798 | 2024-10-08 00:07:28 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac7786f9-0f98-3042-b3e6-3e3b5c0c34cf | -6.5811 | -44.166599 | 2024-10-08 00:07:28 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9344e70-766c-3ecf-aac0-50ee2587b551 | -6.6822 | -44.628201 | 2024-10-08 00:07:28 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a49ca3a-909e-39ce-89e6-ea88fcb13dc5 | -6.615 | -44.4617 | 2024-10-08 00:07:28 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18edf941-420b-3878-ac7f-ca03e325e9bf | -6.3105 | -43.358501 | 2024-10-08 00:07:29 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87809235-87bc-375f-b216-a5799d23a5a6 | -6.3122 | -43.365898 | 2024-10-08 00:07:29 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cacf83da-edda-38bd-abd1-c203e96bcfc1 | -6.8918 | -46.066898 | 2024-10-08 00:07:30 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9bdb0d9-5b2c-3ff3-bbe2-558ef9dcf6b5 | -5.5826 | -40.573002 | 2024-10-08 00:07:31 | METOP-B | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9c42bf4a-fa02-3bc7-9044-7e82be4d3c37 | -6.0804 | -42.739601 | 2024-10-08 00:07:31 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aeae8594-93ea-35be-b6a8-62b34438896b | -5.8758 | -41.962399 | 2024-10-08 00:07:31 | METOP-B | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0247d9ad-6b76-3006-aaa9-2c078b8d9fc5 | -5.8789 | -41.9762 | 2024-10-08 00:07:31 | METOP-B | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e9401205-6f94-3bca-824a-9bc596e8e51a | -5.8804 | -41.983002 | 2024-10-08 00:07:31 | METOP-B | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 77cbaf6b-8156-392d-b6a9-2fdffae371d1 | -6.16 | -43.514999 | 2024-10-08 00:07:32 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a865619-4567-3bb0-8a00-4c42035259b6 | -5.8416 | -42.637798 | 2024-10-08 00:07:34 | METOP-B | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba5446f7-c467-387d-ace5-1cfcc2c1244a | -5.9627 | -43.274399 | 2024-10-08 00:07:35 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| a3489298-be06-3acb-b713-dfbf470ff2be | -6.6598 | -47.082199 | 2024-10-08 00:07:37 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a605468-1ef6-397e-9367-ac2e2d07daaf | -6.6622 | -47.0938 | 2024-10-08 00:07:37 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43bbe504-ad73-3d9d-aade-c9e4283346e1 | -5.8878 | -43.864601 | 2024-10-08 00:07:38 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 063fe22e-2c48-3fd6-bee2-e29dd1fba84d | -5.9897 | -44.4202 | 2024-10-08 00:07:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5eaa0f7b-7bfc-359d-81c6-d6a22337f2f1 | -5.9915 | -44.4282 | 2024-10-08 00:07:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 764be931-2587-3e0d-b55c-e7f069813cad | -5.1785 | -41.2906 | 2024-10-08 00:07:40 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ae963d21-e46d-37fe-b99c-a14a4c2293c9 | -5.7689 | -43.9781 | 2024-10-08 00:07:40 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51e1ec27-40cc-3776-b681-9e18b5508490 | -5.7706 | -43.985802 | 2024-10-08 00:07:40 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d8bcc12-d80f-31f6-a04f-b492f27fb524 | -5.8173 | -44.104099 | 2024-10-08 00:07:40 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4afb74a1-ff77-3b3e-916f-391c536145bf | -5.819 | -44.1119 | 2024-10-08 00:07:40 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d939acdc-72e5-33ea-aa9a-6ee96b6f1c86 | -5.8207 | -44.119598 | 2024-10-08 00:07:40 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e24dc13b-38b6-39ba-b57c-12434726f86c | -5.8075 | -44.106201 | 2024-10-08 00:07:40 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2686ed-985a-3af2-9c8a-43abf29fc354 | -5.8092 | -44.113998 | 2024-10-08 00:07:40 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a2af8b7-40e9-3360-979e-4ccf8a50db54 | -5.8109 | -44.1217 | 2024-10-08 00:07:40 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c06ed5cd-29a6-3603-a848-10d6393f35e0 | -5.8484 | -44.852402 | 2024-10-08 00:07:42 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7262a60f-3883-3fa2-aeb8-636d3cd2ba01 | -5.8502 | -44.860802 | 2024-10-08 00:07:42 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f34942a4-e993-3490-976e-2ed60f517a36 | -5.7011 | -44.276001 | 2024-10-08 00:07:43 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01c300fe-59c8-339c-bb71-ae0c8f4963f0 | -5.9222 | -45.376999 | 2024-10-08 00:07:43 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc17776d-74e1-3b43-95b1-91ba7623b277 | -5.9105 | -45.3703 | 2024-10-08 00:07:43 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e81124db-4291-3fa6-84dc-3971f45e8b1e | -5.9124 | -45.379101 | 2024-10-08 00:07:43 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ece1eca-9546-3d1f-b8be-0b0de6facdbc | -5.9143 | -45.388 | 2024-10-08 00:07:43 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0a02ec4-7ae4-3da9-96bc-d73f98555c86 | -5.3886 | -43.560902 | 2024-10-08 00:07:45 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c3205af-4e6e-3c85-94ba-529aa4644601 | -5.3869 | -43.5536 | 2024-10-08 00:07:45 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39fec0e3-6963-35fd-b744-e6da29683560 | -6.0503 | -46.579201 | 2024-10-08 00:07:45 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| add6f92d-52be-3e07-a614-c926cd5e98d7 | -6.0526 | -46.589699 | 2024-10-08 00:07:45 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69189b2d-ec77-321b-b34a-947432436d6a | -6.0383 | -46.570801 | 2024-10-08 00:07:45 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6324e7cd-0f29-3e27-9780-ef3be94d712d | -6.0405 | -46.581299 | 2024-10-08 00:07:45 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 323f8f94-d55b-3448-8910-39ba7ba97b8b | -6.0428 | -46.591801 | 2024-10-08 00:07:45 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 363805df-3a61-3ab0-9851-3b01a410a6ac | -5.478 | -44.243 | 2024-10-08 00:07:46 | METOP-B | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b451b4b-8881-3e4c-a278-867e5455d43f | -5.4682 | -44.245098 | 2024-10-08 00:07:46 | METOP-B | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbfd005-1519-3d15-9249-b07ee5473ce6 | -5.1313 | -42.868099 | 2024-10-08 00:07:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3118a7d-492d-3c8a-b012-5a0b1e92f07f | -5.1328 | -42.875099 | 2024-10-08 00:07:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e36748b-10f4-30ab-9aa0-4882496ebb3d | -5.1426 | -42.872898 | 2024-10-08 00:07:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d939fce1-7900-3d06-a2d9-d48168d96573 | -5.1411 | -42.865898 | 2024-10-08 00:07:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c983fa5a-1f89-3c47-ad35-f9f80237b12f | -4.9157 | -41.953098 | 2024-10-08 00:07:47 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bcb50aa5-3fa9-3246-9e10-f52d783e149d | -5.3198 | -43.714699 | 2024-10-08 00:07:47 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38bb98b8-1059-39fd-8ff6-432e7d7d8d05 | -5.3215 | -43.722099 | 2024-10-08 00:07:47 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b52f78b-3345-3cfd-ba92-10c20cff2d00 | -5.5827 | -44.8578 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a093f5d5-ebe1-3d3e-b1b1-04d28ce1d61f | -5.5845 | -44.8661 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07278e4b-4d75-345c-86b4-e1ef3021fe5b | -5.571 | -44.8517 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccc0fa56-d93a-3dd4-9d35-fd24a4a64d9b | -5.5729 | -44.860001 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 265a9e93-b84b-302e-9366-a835b4c66482 | -5.5747 | -44.868301 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44e67494-a042-3907-b985-508b8f561dc4 | -5.5631 | -44.862099 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a37e2d1-55b0-300f-bd35-e7d2b18407ad | -5.5649 | -44.870399 | 2024-10-08 00:07:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e13b7b13-eee3-3c33-8eae-49c19a785148 | -5.6532 | -45.8358 | 2024-10-08 00:07:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4404b28-52d4-3acf-80d8-be99c792633d | -5.6552 | -45.8452 | 2024-10-08 00:07:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 319d25b5-70fe-3708-826d-dc32f4be4f26 | -5.3939 | -44.933498 | 2024-10-08 00:07:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a71dbd3b-d3dc-3f77-83b8-dce6d166701a | -5.3957 | -44.941898 | 2024-10-08 00:07:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaf34bd1-9de6-3171-be37-926a113d13b5 | -5.5108 | -45.465801 | 2024-10-08 00:07:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c80fd00a-1c23-3ba4-908f-9a6f90d4d00d | -5.5127 | -45.474701 | 2024-10-08 00:07:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e65e413-d150-3a51-a7c5-e8ca35a0e92b | -5.7119 | -46.435299 | 2024-10-08 00:07:50 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22115a65-9d27-34f1-b3bd-0e983830b6aa | -5.7142 | -46.4454 | 2024-10-08 00:07:50 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a284ad36-217e-3003-9dd1-4c89ff384b5f | -4.8242 | -42.738499 | 2024-10-08 00:07:51 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff1e619-711b-3dde-8830-7f3765945612 | -5.5628 | -46.267799 | 2024-10-08 00:07:52 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1950f3d-5830-3ccc-944c-deafe8ec9df4 | -5.2764 | -45.099499 | 2024-10-08 00:07:52 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0a174dd-79c2-3225-8c25-7b94a2daccf7 | -5.2782 | -45.108002 | 2024-10-08 00:07:52 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a35d1f1d-7e9f-314f-b19b-f8c1ec079465 | -5.167 | -44.649399 | 2024-10-08 00:07:53 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90d24a5e-6a5b-328d-be3a-196a55700bac | -5.2666 | -45.101601 | 2024-10-08 00:07:53 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aac33984-4417-34a6-bc0b-1efaf9e794ee | -5.2684 | -45.1101 | 2024-10-08 00:07:53 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8289778-2382-351a-af8f-11da6f59a8eb | -5.0101 | -44.080299 | 2024-10-08 00:07:53 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f2edd49-33b9-3954-8572-7826b0dfcbb4 | -5.282 | -45.358799 | 2024-10-08 00:07:53 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec1e87fc-618f-3b01-b2b1-f6a2e34d996d | -5.2839 | -45.3675 | 2024-10-08 00:07:53 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dd54cc9-e2ec-386b-9b48-8906f4737daf | -5.5019 | -46.364201 | 2024-10-08 00:07:53 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fcf5d90-dd6a-3e06-b679-41b2e6dc9b18 | -4.2674 | -41.226501 | 2024-10-08 00:07:55 | METOP-B | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa567aca-52b1-3427-84fe-1a22de084028 | -5.078 | -45.178001 | 2024-10-08 00:07:56 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| febe2151-f735-3887-89fd-2e313ad6a6b1 | -4.2463 | -41.908401 | 2024-10-08 00:07:58 | METOP-B | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44561566-7cda-3a9d-96a4-4611519029ba | -4.2478 | -41.915199 | 2024-10-08 00:07:58 | METOP-B | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5a43495-2e33-34e1-8cae-1b66c882de46 | -4.6594 | -43.751598 | 2024-10-08 00:07:58 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
