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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ea17d1d-bc94-3c29-84bb-4d2aabae489d | -12.7373 | -44.4521 | 2026-07-08 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e6632fb7-ce1c-3f32-9936-d50aa701f0ff | -6.42603 | -55.80362 | 2026-07-08 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1faa942b-20f8-3509-9269-3585af0b13fa | 0.8739 | -59.70319 | 2026-07-08 00:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 307c47d7-a14a-3564-a003-987cfd55ae5f | -21.8033 | -56.2729 | 2026-07-08 00:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 77ba4761-53d4-3d9f-9f41-3b0878397aed | -12.7566 | -44.449 | 2026-07-08 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 39d33736-6af6-3c13-8cbf-111ac0771ee4 | -9.2258 | -48.5782 | 2026-07-08 00:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e5b7bc3e-b6ed-37ee-a7d5-10298122e3c5 | -5.6701 | -44.3147 | 2026-07-08 00:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ad51e16a-b072-32ac-8d1b-049f2717d7c0 | -13.9589 | -45.2251 | 2026-07-08 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| e552f754-fccd-37f8-8b64-0dc6a8a2d12a | -21.3642 | -49.1664 | 2026-07-08 00:50:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| c8d48058-78b9-3f3e-af27-f7f9443eafd5 | -12.7373 | -44.4521 | 2026-07-08 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 008a04eb-7b11-37db-862f-a0b28212b62e | -21.8037 | -56.2514 | 2026-07-08 00:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b36775af-1e9f-393c-bd17-b467aeda346d | -12.3561 | -47.413 | 2026-07-08 00:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c77101f8-4c5a-33d0-b625-bed0480bfc5b | -21.373899 | -49.167198 | 2026-07-08 00:53:00 | METOP-C | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0b4f37f-eb8c-3602-acca-afcdbbb1a246 | -8.7389 | -49.452999 | 2026-07-08 00:53:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4f1d45-987d-3116-909f-1cbf3d4a5be8 | -13.2873 | -45.183701 | 2026-07-08 00:53:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a21af007-d189-3655-ac1c-2767d2d8e04b | -14.1405 | -52.884701 | 2026-07-08 00:53:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5cd4dbe1-cec4-370b-a429-0106561e8258 | -5.6595 | -44.2953 | 2026-07-08 00:53:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8eb1ed-65af-3f69-924c-692717c46d12 | -4.9474 | -48.242599 | 2026-07-08 00:53:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c836219b-c17f-3bff-beaa-7396b70578f3 | -13.4785 | -49.9203 | 2026-07-08 00:53:00 | METOP-C | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44357d58-a512-3064-8a80-6be44e2f0112 | -4.8249 | -46.8097 | 2026-07-08 00:53:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38857ed8-5a23-3f7f-b778-7eadf18cac1c | -8.605 | -48.003101 | 2026-07-08 00:53:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 966e9c0a-e98c-3fc6-998d-94284eff2be3 | -15.5796 | -48.2365 | 2026-07-08 00:53:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad46913-49d3-3f71-bd96-f152d2502914 | -5.3068 | -47.2332 | 2026-07-08 00:53:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6eed876-94f4-3ba4-80c7-58d553c4a0e1 | -6.5037 | -42.231998 | 2026-07-08 00:53:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c301d0a0-3af0-3596-b5af-6f27fbac548a | -9.373 | -48.808998 | 2026-07-08 00:53:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a16a98f-c933-3fef-a835-b998da1268ca | -14.6004 | -52.062599 | 2026-07-08 00:53:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a427ef94-87ba-36d2-910a-a7ce10108bc7 | -13.282 | -45.162102 | 2026-07-08 00:53:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e796bc96-a76b-3566-be2b-7547c2e11909 | -12.7484 | -44.431198 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d64f1ea3-451a-32d4-9166-cdc56df4391d | -13.5374 | -52.941502 | 2026-07-08 00:53:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32883bca-bcd7-3bdb-8770-e3d10ec59f87 | -11.0465 | -45.827999 | 2026-07-08 00:53:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5b16ef-1211-3633-b9c1-29f825517b48 | -8.1333 | -47.105801 | 2026-07-08 00:53:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 691e7ad9-ffb9-36dd-addf-f6527caaac75 | -12.3636 | -47.431702 | 2026-07-08 00:53:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2239dfd3-b044-3594-ae2e-72c129305c47 | -13.2857 | -54.4137 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0b055c-276a-3897-b77e-44676f104950 | -21.810801 | -52.722401 | 2026-07-08 00:53:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a3bb933f-31cb-3474-9a76-f4808461745c | -6.9383 | -43.684898 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc837172-938f-38c7-971a-df2260b2e0b5 | -9.7364 | -49.038601 | 2026-07-08 00:53:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80c9f11d-e993-31a2-864c-401b3750100a | -13.2838 | -54.4044 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7a534c-8187-3b64-bf44-9a94ea1a44d6 | -12.7514 | -44.443501 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcab1801-426e-33c9-8e2d-d4f76065daf3 | -18.083599 | -54.021999 | 2026-07-08 00:53:00 | METOP-C | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3b7040dc-c287-321a-a6e5-aecdf3c4e999 | -6.8505 | -50.655499 | 2026-07-08 00:53:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3559e21c-af47-3299-8e02-675fbd812414 | -12.3498 | -47.417301 | 2026-07-08 00:53:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a906df0-f951-345e-949e-556a5a1d7005 | -9.3039 | -51.921902 | 2026-07-08 00:53:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2de56d30-1044-3d90-aeb2-8ff346f659ad | -9.2358 | -48.576199 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7f6f69d-d56e-3d18-a5db-f17bfb5182ba | -13.9575 | -45.215801 | 2026-07-08 00:53:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba18e77-b566-3448-9356-aa96437f5ad6 | -17.2799 | -50.016399 | 2026-07-08 00:53:00 | METOP-C | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 67544f8b-5c89-30e4-b3e8-c087b3739f2a | -7.6432 | -50.0229 | 2026-07-08 00:53:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6cf5a6-1ff1-3d69-9945-8318f506b122 | -13.4769 | -49.9133 | 2026-07-08 00:53:00 | METOP-C | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6340767-cf66-33dc-9d4f-ff5b22e7dd90 | -13.9601 | -45.226299 | 2026-07-08 00:53:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cff372d-43ec-3c36-96dc-3be3f8e81b8d | -9.7462 | -49.036301 | 2026-07-08 00:53:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d81d604-9a92-3048-98b7-03477cd0a048 | -12.3616 | -47.423401 | 2026-07-08 00:53:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a97f3066-f7c0-3c55-90e4-180a04cd739e | -8.5973 | -48.014099 | 2026-07-08 00:53:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52012549-1cb4-3aa1-aee1-673a659dd009 | -13.9549 | -45.205299 | 2026-07-08 00:53:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5c72c69-edda-3516-acd4-0f473b37828b | -13.3288 | -54.375301 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce727f7b-7738-3030-80a9-cf6c0f6dd52d | -6.8473 | -50.641399 | 2026-07-08 00:53:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dae89a9-31fc-34c4-abd4-2f9a88dfe381 | -5.8052 | -43.799801 | 2026-07-08 00:53:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccc544da-6170-307c-847d-3851e64a79fb | -12.7575 | -44.4678 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69329a3b-bf25-3cee-866e-fb355c894746 | -10.9333 | -43.0574 | 2026-07-08 00:53:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2065751-4767-39fd-8049-31ca4b2b74f9 | -8.607 | -48.0117 | 2026-07-08 00:53:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8e70da-6d5f-3b0b-8f19-29390d377f19 | -8.1235 | -47.108101 | 2026-07-08 00:53:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d74fbb9-5b8f-348b-a3ce-60b4baf4db0c | -6.9522 | -43.699402 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0f57f22-9193-316d-95d9-52f0b1a69f84 | -5.6674 | -44.3274 | 2026-07-08 00:53:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74677cc7-609c-3f5c-976f-f60a741aa973 | -8.7371 | -49.445599 | 2026-07-08 00:53:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81dc3c21-26b8-3ceb-a5f6-80b468712f45 | -21.062 | -47.243801 | 2026-07-08 00:53:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 191e54c4-8db1-3d82-a7e1-59d3bc585979 | -20.9613 | -48.6404 | 2026-07-08 00:53:00 | METOP-C | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09c1d1c0-c981-393d-b974-6137b6dc3466 | -13.9504 | -45.228802 | 2026-07-08 00:53:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8ce1345-9003-3535-9015-eb6a66bdc9bd | -7.6415 | -50.015701 | 2026-07-08 00:53:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e27508b-0d80-3a11-9738-b76c080f4ef3 | -12.7448 | -44.458199 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e438e5b-b9d8-35b1-aaf4-8bb0a9cd41cc | -12.8491 | -44.379002 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c2caa47-ed59-3585-b80b-d93fefbabb83 | -6.4886 | -42.212799 | 2026-07-08 00:53:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29999ed1-9ee2-3ec0-a491-dffe566c0ecf | -21.7868 | -56.2658 | 2026-07-08 00:53:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 636bd462-8653-3aca-b09c-de038c327167 | -9.2242 | -48.570499 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2a296ce-6e11-3959-a9b1-e7e6db61905f | -13.3308 | -54.384602 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09bf1e37-6988-37d1-9408-278f32ab8460 | -9.2279 | -48.586399 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa35ebb0-c984-36a4-9961-89f9230003d4 | -22.287399 | -46.8647 | 2026-07-08 00:53:00 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2f8dd27c-0e13-361f-87b5-b7e11908a41b | -21.065399 | -47.258801 | 2026-07-08 00:53:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 263a9247-b171-3ce9-89dc-cf50e162507f | -8.3812 | -48.235001 | 2026-07-08 00:53:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca4054e-2911-3b8b-adb4-ffbdbada8b26 | -11.9119 | -55.91 | 2026-07-08 00:53:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2079155b-52c1-32c8-bd10-13caa0b1575a | -21.0637 | -47.251301 | 2026-07-08 00:53:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a253edbd-71f8-3f62-8d9c-686d8c6e27e3 | -12.3596 | -47.415001 | 2026-07-08 00:53:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12c8c1e5-a765-33dd-b195-7635071f17bd | -9.3137 | -51.919701 | 2026-07-08 00:53:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d03507-ec71-3d52-9e4b-4b63fa94efc2 | -8.1212 | -47.0984 | 2026-07-08 00:53:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c85d6f1-03f3-3cbe-850c-e9b0de1ac473 | -13.5276 | -52.9436 | 2026-07-08 00:53:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28dc09e0-2cc5-34d6-8e10-fc3d8e287d2e | -13.2955 | -54.411598 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb405978-50c7-3f6f-a04f-8a4c0098760f | -11.0439 | -45.817402 | 2026-07-08 00:53:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9efb8821-0e60-3cff-b78c-fb7ca5f315df | -12.1339 | -48.252399 | 2026-07-08 00:53:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4fd130-c622-3aa2-a5d4-238185355538 | -13.2936 | -54.402302 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef16a06d-29f2-3352-85c3-43d49ef00e62 | -9.3764 | -44.707199 | 2026-07-08 00:53:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39fd8bbc-0e7f-3d8b-aa65-6d542e037b1a | -8.5953 | -48.005501 | 2026-07-08 00:53:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 532acf39-758f-3cef-bf5f-9e253f456ca9 | -12.7417 | -44.445999 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bcc3684-5531-3457-a64f-ed2d67233d17 | -9.3368 | -47.910599 | 2026-07-08 00:53:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26bb5f39-0c0d-391a-9f6b-75d58e395e97 | -9.3122 | -51.9128 | 2026-07-08 00:53:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea4f3830-2a95-3d88-9707-b05a1f77fb86 | -14.1388 | -52.876598 | 2026-07-08 00:53:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 27fac088-f50d-3c05-b375-493d2bf4e5c2 | -9.3024 | -51.915001 | 2026-07-08 00:53:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02bd99ea-8ba2-30d7-af35-63379802520a | -13.3386 | -54.373199 | 2026-07-08 00:53:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a953ab4-d2d1-3388-9fe2-b0a30f9edee8 | -9.2162 | -48.580898 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da41be1e-0217-3c9b-bb67-6f85fcf7de4d | -20.107901 | -53.337799 | 2026-07-08 00:53:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ad3a7e45-517d-35a9-a6b6-f7d08bd979c4 | -18.742901 | -46.910099 | 2026-07-08 00:53:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af0f4545-a953-3f28-80f4-780a9a865758 | -21.7938 | -56.247501 | 2026-07-08 00:53:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 57ef4577-b03c-3b4b-854f-7b9d9972332d | -8.7354 | -49.438099 | 2026-07-08 00:53:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f55fb8a4-217c-384f-9828-12014ff50180 | -5.3379 | -44.705002 | 2026-07-08 00:53:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
