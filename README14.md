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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9251e8f-e6eb-38f0-a39b-c1e737d42a6c | -5.21563 | -46.02898 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9dc2a6e-d949-3043-85f5-f61c6d9d5632 | -4.78231 | -43.65754 | 2026-09-27 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b60bbf00-9ae1-3f4c-9209-ae6f97e08e6b | -8.34801 | -44.1835 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 9e3baef9-53ea-32b6-9d48-f71bed48e02f | -8.34604 | -44.18017 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c75bfe0-7f7e-3cd2-9be6-6ab563a856d1 | -8.35324 | -44.1528 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10a76bd2-b1c8-3b9b-8ce6-7adcde757c1d | -5.51742 | -40.88358 | 2026-09-27 04:08:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c03dd343-b6bb-3c43-99fb-a16f6ab8a74d | -7.42123 | -48.36076 | 2026-09-27 04:08:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04aea2a4-da03-37a6-abf5-29d4b8c34302 | -5.73411 | -45.01985 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8affbcc3-80ba-309d-886e-2eb63395e433 | -7.40189 | -42.62478 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab1c4ce1-554b-3fb4-9c0c-6b1727761367 | -5.75998 | -45.29137 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa05fad3-734f-3742-8a53-3d8e5ba1b2fb | -8.35692 | -44.15343 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 13cfe103-8654-3606-ac73-04964f5255de | -7.36117 | -42.1032 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 79d76180-14bb-3996-9d3b-d8338e24919a | -3.85213 | -49.13817 | 2026-09-27 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9feaa325-d870-3730-8f63-5fd396f6ae4b | -8.34582 | -44.1741 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 2ffa59eb-d2d9-349c-bdb6-76e220a0a16e | -10.92695 | -43.86327 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7940292a-8f8d-3e00-8802-01f34065fde7 | -6.12106 | -39.52315 | 2026-09-27 04:08:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 434b7920-d0fb-3955-8954-224ebfabce1d | -9.08044 | -49.87425 | 2026-09-27 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e44fda69-9c2d-3dab-a9a8-45def1851ff0 | -5.88853 | -46.58047 | 2026-09-27 04:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a62c865-c1c5-3681-9cf9-2d86b1a38753 | -9.83753 | -44.94606 | 2026-09-27 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b33fb63-94e2-38ea-a93b-90368ac13789 | -5.51025 | -38.00754 | 2026-09-27 04:08:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40c74644-3221-31c8-b420-dea029f8fdde | -8.3628 | -44.16343 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e5673277-823b-3054-a4e2-8254e02f538d | -6.31517 | -43.3382 | 2026-09-27 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82589235-647b-3cc4-ab53-2361325213a7 | -8.33993 | -44.16412 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adc9b644-9762-3ef7-b0c0-6fe63dd7eb80 | -10.92562 | -43.87121 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4075d9da-3b13-31e8-8d5d-90e37da848f1 | -6.39918 | -42.78782 | 2026-09-27 04:08:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d85b990d-384f-3e35-8aa0-bcc68691e226 | -8.35037 | -44.15377 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2e6fe09-05a9-39c5-94bd-917d983cc74f | -10.0156 | -52.10154 | 2026-09-27 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b742516a-43e1-3318-baa4-1a6c36c1db80 | -8.351 | -44.16593 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0345251f-145c-3673-9e83-7fbd2325b1ee | -8.35027 | -44.13128 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a3e0137-2dcb-39b0-a560-a1f8de50b816 | -6.83784 | -43.50853 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9400e094-bffa-3084-a7e6-9e177d68c0a9 | -7.36961 | -42.11589 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2587788d-e77d-3c60-ac31-9b73c268fb63 | -8.3554 | -44.1847 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 526407e4-a5bd-33d3-a457-1e2f9168f557 | -6.17237 | -44.59032 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03f2da68-c60b-3bfd-bd58-8ea56f47f40c | -7.34242 | -39.31305 | 2026-09-27 04:08:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31bb11c4-6260-34fc-bd9d-fc93c1e621b6 | -6.12938 | -53.06228 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6ec50b7-b9a7-3ab5-8b40-0499a6aa747c | -10.1123 | -50.19703 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1de93671-6550-32c4-b6a2-0becec343098 | -6.31155 | -43.33763 | 2026-09-27 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4bd5bad-024e-3529-99e5-19aa4a02691d | -7.36842 | -42.12327 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 40b53492-5ce0-3789-a4aa-4ead1bc88f82 | -2.97281 | -49.56336 | 2026-09-27 04:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3703324-2973-32d5-bc02-84a4b31bfa11 | -8.35026 | -44.17031 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f56e5300-c9fb-3845-8827-a277a6924acf | -3.69255 | -51.37272 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e451234d-a14b-33e8-a27f-915a4b77471b | -6.9264 | -42.86594 | 2026-09-27 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 18718fe7-f0af-37bd-98ff-063d3071ed93 | -9.78777 | -44.828 | 2026-09-27 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b3c2770-b0d6-3599-b639-322cbd760099 | -6.92869 | -41.61563 | 2026-09-27 04:08:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7248f540-027d-3a3b-9332-efb7da192011 | -5.42733 | -43.44588 | 2026-09-27 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0cbbacf7-0f7e-3421-ab92-7598d971edc9 | -5.17396 | -46.08451 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e5a8945-0173-355d-b30c-80782f8b0a80 | -3.19259 | -51.03972 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 450661c9-c881-38e9-b7a0-c61965f85444 | -8.15748 | -44.45602 | 2026-09-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 337ad531-e9c0-3bcd-b63c-511d909dcebe | -8.34219 | -44.13439 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e267c7c8-1637-3e2b-be5a-08ec64d85d78 | -9.08105 | -49.87096 | 2026-09-27 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9969aa06-0ace-3ddd-b3b7-4ed29350472d | -3.19042 | -51.03559 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2ef67995-de3f-390a-a89e-d9205b7f4557 | -5.47897 | -48.579 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4766821e-e2cc-3655-b48e-cb4760fdbba5 | -7.33233 | -42.08718 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a61dea2-f855-3eb3-914c-a3199f31abef | -10.63962 | -45.11597 | 2026-09-27 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0cee1ad-a786-3bdc-bb4d-d5614453de9b | -5.7327 | -43.27679 | 2026-09-27 04:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51fced52-6ccb-307c-a534-9188a41e38d3 | -10.93685 | -43.8691 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52dcb77e-3102-33a1-a438-4865362ec866 | -8.35246 | -44.17969 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| df4b66cb-eb6e-3b84-a318-211b5c1fca0a | -5.22413 | -43.47448 | 2026-09-27 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34bf399e-14ad-3e4e-be97-d62c52574bb9 | -4.25177 | -51.05135 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 512da787-f3a6-3ca3-83aa-a9a84f07beeb | -7.12656 | -44.77625 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06fac678-925a-3306-a079-c4da87650707 | -6.41689 | -45.85679 | 2026-09-27 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ec3947a-f7b0-32e0-80f4-1bdfa692f6e9 | -3.19668 | -51.03671 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f823acac-74e1-3f72-b4d2-e105f374f1db | -6.17157 | -44.59517 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfd16214-d270-3360-9cfc-f7f637b2bf02 | -9.93756 | -49.3732 | 2026-09-27 04:08:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a51f9e4b-0253-31b9-b479-af5c00229867 | -9.31458 | -47.63229 | 2026-09-27 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b74399bc-aae2-3039-8640-87620357fa94 | -5.50228 | -45.51467 | 2026-09-27 04:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73588395-d05e-32c5-b8f0-e2287c6e7c73 | -5.74309 | -45.06515 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 714f4475-e359-3959-9417-e3f5e44ae2c4 | -5.73234 | -45.03032 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fc34b05-954f-3655-8646-6837cd617a50 | -4.81252 | -45.92863 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ac0aab7-4cea-3c3a-877d-06719fa9d105 | -3.9599 | -48.12381 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd3fa540-dad3-3a95-8717-1c0bf1f672c1 | -7.19267 | -46.50753 | 2026-09-27 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 324e5768-337f-3c3b-9b8c-f4bbeac9814d | -4.25261 | -51.04665 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abc6e151-d0d9-3fe1-9320-191aa3c9be79 | -7.29216 | -43.30489 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe0b3634-68f9-3dfe-9ad5-911e2ed05454 | -8.34148 | -44.13876 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c299cb0-b59e-38f1-a04c-110988acd508 | -9.7638 | -48.20405 | 2026-09-27 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b691a48f-832b-35ba-8216-6aa6bd08d719 | -4.56276 | -44.08283 | 2026-09-27 04:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc98dd03-7134-3bc0-8138-286ff70f6b7b | -8.34532 | -44.18459 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 757a692f-d2ae-3d33-a835-5751fff01a12 | -3.05759 | -50.33997 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dabaf61-ac44-3381-8c1d-d70221e33e19 | -8.34821 | -44.16695 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c7088a1-b868-3c80-b5cd-5f6c7e3944f7 | -5.1778 | -46.11551 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16dd9e25-6367-3c57-bb9d-9e276041cd88 | -5.73518 | -45.03808 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6427ad01-44ce-378a-851d-ba90f163c945 | -8.36944 | -44.14657 | 2026-09-27 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddba2643-a97f-3bc5-b1a1-78673bffc1a6 | -8.34438 | -44.16032 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8778d96f-608c-36a4-958a-ac61b47b5e84 | -7.30261 | -46.03238 | 2026-09-27 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 832c93cd-4f45-392c-8816-2ac25f32edd8 | -8.35175 | -44.16155 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 79533c1a-ee17-387e-9a6b-39e4366b110c | -8.35096 | -44.18849 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4608af69-aec9-3705-ab5d-fc22bf435e60 | -10.93048 | -43.86387 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 099e1b01-5d6b-32bc-a1c5-f66ef58bc28f | -5.66501 | -46.36014 | 2026-09-27 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f8a670-1f01-3e9f-9366-4a54fde9fce6 | -8.34884 | -44.14001 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d355f64-6d09-31be-99e7-13901ba79904 | -3.84424 | -45.13853 | 2026-09-27 04:08:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de47376d-396b-3a8e-a915-b87337e548da | -5.17831 | -46.0853 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c2fe7e-4ed6-3644-b1fd-be012a552c32 | -4.81683 | -45.92959 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76c5d9a5-bfc7-39b3-8586-c5ca176b59eb | -7.40882 | -42.6259 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0fe77694-7c4f-3ff4-95cd-9852d723991c | -3.20294 | -51.03781 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f8e7b5c-35af-3060-a08e-6f2c403b9a0f | -6.82398 | -39.32964 | 2026-09-27 04:08:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bc0b7beb-7020-3af2-9269-547fc74cdf9f | -4.99363 | -37.09791 | 2026-09-27 04:08:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11823a94-09d1-386a-a405-d680a170fa4a | -6.13837 | -53.06277 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86932338-cf22-3070-90a0-32008df31335 | -5.93855 | -42.72423 | 2026-09-27 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2d3e4b6-ba97-39b7-acd0-fcdf4a8c5946 | -4.14352 | -48.2197 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa90327f-13e4-387a-b225-50e18b95a895 | -7.02202 | -46.4524 | 2026-09-27 04:08:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
