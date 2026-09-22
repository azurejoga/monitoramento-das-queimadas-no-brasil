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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fef1e775-1324-34cd-86c4-f048f8aca8a0 | -5.78821 | -43.77736 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0edbf748-7ec7-3efb-b552-f1a911cc2af2 | -10.4742 | -51.30233 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 72f9ad2c-5221-3dd5-b024-44f5c26caf7f | -9.62323 | -43.94264 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d8cce481-1b6b-3e15-8435-f81800f2bacd | -9.02286 | -44.90989 | 2026-09-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdbf845c-adde-3fb0-b809-50b580f1ab79 | -5.75418 | -45.08932 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| c20bd723-d669-3bda-b5cd-766da02af491 | -5.64928 | -43.41547 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a89bb956-4134-3671-a4f1-b9cc55ba7365 | -11.14797 | -42.84118 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d7705406-6da9-3c8a-8500-848c27ea4738 | -11.4481 | -47.33121 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 646c7658-edb5-3e5a-a1c5-e2d2b7a92fba | -7.05247 | -49.91967 | 2026-09-22 04:02:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6edd5fdd-df71-34c3-ba6b-dc610cab85ca | -6.97867 | -42.17077 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2001f363-ba5e-3926-8882-bc187a9a59bd | -11.15775 | -51.11815 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 19fc9ef8-38cd-3c29-b0c1-67db68845376 | -11.43382 | -47.32612 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dd3619f-83b3-3e8b-a42f-77152f7354a3 | -6.56652 | -44.90005 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f379c5c5-dc8d-388a-916f-fef7afe262f5 | -9.59378 | -47.7759 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd9ad48c-713e-31b8-90b4-02d39aae29df | -5.99058 | -44.7286 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff73e9b3-8ee6-3184-82f2-1be4b881eee8 | -5.82744 | -44.13102 | 2026-09-22 04:02:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d70d040-3234-3304-af96-6e825d2f791b | -7.83206 | -44.9729 | 2026-09-22 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0af8f371-82ff-32a3-ae77-3abad14210ab | -6.71019 | -43.98425 | 2026-09-22 04:02:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4894388-cfb7-363b-9c63-511efe7d71e0 | -12.29938 | -39.65906 | 2026-09-22 04:02:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0b57ad6b-a09e-3472-ae47-13b68bbb6d1f | -10.20599 | -44.15777 | 2026-09-22 04:02:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41dbcff0-80d6-3a65-a6e1-631209da5880 | -12.14182 | -47.39271 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2129eae0-0040-3238-b175-6211d9b95a5f | -6.90415 | -41.69426 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 144c9308-0a8c-3bbe-9206-301a2ff93da8 | -7.78086 | -44.80894 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb177319-487c-3489-ba4f-0756ee93d873 | -9.37999 | -47.76179 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b85818c0-9025-3ac8-989d-993cd592549c | -6.29345 | -41.75671 | 2026-09-22 04:02:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5025a07c-8a6c-3491-bfb7-eea66ad68dac | -11.87516 | -46.84256 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 473cc2a9-7021-32d7-82de-48141c30437b | -5.64868 | -43.41902 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fd75121-d3e2-3304-806f-2c0c11f16b41 | -11.15921 | -51.11208 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f40c96eb-f578-3a8d-8e73-083214ef35bd | -6.97473 | -47.49956 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 95a57b5a-7eb3-333e-85ed-37de2049984f | -11.67908 | -43.45218 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36a61b63-9fc0-3ad4-b59a-c12f80b32a2a | -9.52872 | -45.38842 | 2026-09-22 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dc09f66-897d-304f-a91a-ae2d76c06752 | -6.77833 | -48.66805 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ba7f1a6-c31e-37bc-88b4-ee1652dd175d | -12.60191 | -45.08793 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfb816a1-37d5-36e1-b7d2-feb7609e7362 | -7.02282 | -42.08516 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 279ff242-4abd-394d-b563-8e5fdac65d1a | -9.90739 | -45.09411 | 2026-09-22 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bea929c-76c7-3927-a415-4ea4457f168e | -11.32649 | -43.40537 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a2e7027-b520-3fb2-a82f-7e447422487e | -5.68434 | -43.42878 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04762cea-9e4e-3393-b662-39aad6454e13 | -6.90188 | -42.95501 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3941af80-8b21-3828-8c02-8417c3e5e781 | -7.54363 | -47.32723 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bbb20f7-c3a8-321d-918a-70bddca0843c | -10.47511 | -51.2978 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d15518b5-90c6-3867-8637-5f9c10fac56d | -10.78453 | -50.73653 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6efb1cf-7c07-3af6-982a-8b2dfba93fb9 | -10.11956 | -45.54529 | 2026-09-22 04:02:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5254577b-56b4-33f3-bff2-ef621da505e8 | -7.38818 | -44.79886 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f397251-0f3c-3277-a175-a64725dd4dbf | -11.44238 | -47.33308 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b490ee8-fe45-30ec-98e0-e59179754c39 | -5.84648 | -49.78383 | 2026-09-22 04:02:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db27cdda-5fa1-3927-be40-6fcdff3e8e2a | -9.61014 | -43.92482 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aaff4428-2c14-3e55-a397-b827c513f561 | -5.73537 | -43.72265 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dc7f98a-2120-3fdb-aea3-891a31385cfd | -6.89629 | -41.69723 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82c3e179-ea4a-3baa-8070-43b666fc74e6 | -7.45372 | -44.74121 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd227f35-d648-3305-98b1-036bedb257e3 | -10.68151 | -50.76621 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ef073d-25e1-3b84-89e1-35a81e6a59db | -11.1016 | -48.31736 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e988234-ea22-372a-b3b1-482d9887fb4d | -6.90042 | -42.95267 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 424c6662-cf7b-3b56-b0f3-2ae38fb55399 | -11.67757 | -43.46112 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb860f82-c4fc-3042-803f-b4fd17550fcb | -5.82643 | -43.85249 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd2f49b5-9443-38ad-a8cd-6bb34c22da12 | -6.88086 | -41.71317 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 085a09d8-5e9b-3bcf-a2a6-7c4e8d2cce4f | -6.67199 | -47.37458 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff270387-5910-34a5-b2f0-14638baccc14 | -9.62103 | -43.93191 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| be7afaf1-8f27-3369-a124-7902c2a4c9b1 | -6.15764 | -44.1801 | 2026-09-22 04:02:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49c1ff81-8ef6-3441-a540-f8623e8f72d8 | -7.94374 | -45.64935 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0b9eb61-93f2-32b6-b088-19f005529f5f | -6.47501 | -42.77861 | 2026-09-22 04:02:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 81c4edb1-eb85-3344-af0f-9a717bcd42b2 | -7.82335 | -45.26033 | 2026-09-22 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a479fa6-26df-3f49-a9ca-780a930429ca | -7.36608 | -44.26995 | 2026-09-22 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee56227e-50a6-30ee-a6e7-04378a786193 | -10.86988 | -50.15837 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07456a2-f38b-3af1-b4e9-f6829152dc03 | -10.47045 | -51.30029 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29026294-78a7-35cd-896c-983ed42aff1a | -12.60531 | -45.09222 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea3cbbbe-7777-36dd-a8e0-e4802c7599fd | -11.94523 | -46.51522 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7303f54-a563-33d2-bec1-0dffcca56d76 | -12.56386 | -45.97021 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2dad6480-6e40-3890-ab8d-d7e7cef2f29d | -7.13525 | -42.08438 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2ea8c5d-ce61-37d7-a2dc-4c4014e1ae33 | -4.64296 | -50.99668 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7eed014-11b0-3baa-811c-73aca1622421 | -10.6897 | -48.72184 | 2026-09-22 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a246c9f7-f9b9-3c64-a7ab-4a504e7a7957 | -11.67017 | -43.45981 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 427d445f-d523-34e9-bbb7-263939a5b560 | -6.47344 | -42.78821 | 2026-09-22 04:02:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 64188848-dd86-3540-ae13-f68a02831aec | -10.78134 | -50.74176 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87d6679f-3841-34c1-a561-8f8661f4641c | -6.88895 | -42.92633 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6114a133-3958-39df-aa84-8499b7432ebb | -11.41282 | -46.79088 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e4cd916-41a1-3f5b-a7c0-a4a807bb726a | -9.89626 | -48.48442 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15bc9bd0-0443-333e-8764-06592d97cc2e | -6.87928 | -41.70016 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 810fae50-fc49-3345-9c94-9bb3e1260102 | -8.4186 | -46.86741 | 2026-09-22 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f19f01f-7631-3181-9386-7c1d71e6d58a | -7.50673 | -45.44685 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 64d9cd81-a623-3414-8091-56e718a3ee73 | -12.5646 | -45.9602 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d888bc8a-d1ff-3bbe-bf12-8c49c984d716 | -12.55962 | -45.96936 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef753410-255f-3a59-bf38-9dd6bc7d718f | -12.02231 | -47.81746 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 87186005-950b-36e2-8e49-5ab530cf6720 | -11.44147 | -47.3381 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90ab8574-d51f-3cf5-96dc-82a2f9e77a73 | -8.79088 | -44.29154 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4683d60-4b77-3c8c-bc7b-d7d4f9f2dbad | -9.28528 | -46.1898 | 2026-09-22 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fd83d4ea-724d-380f-af33-1dabf7ae7fbc | -12.56033 | -45.96533 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcc94926-f4cf-3ced-9716-c198c8fe1817 | -5.98183 | -44.72712 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c890d9c5-721a-3c11-8b72-18ad55f906f8 | -11.1493 | -42.84025 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2090ffb-4db6-3376-b4ac-005d39508dbb | -11.14744 | -51.10611 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c697c27-2ffa-3dba-b631-3b3dd298f4d5 | -4.02062 | -51.05527 | 2026-09-22 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94f29323-cc40-333e-98e0-55ddf671e8d0 | -4.64958 | -50.99838 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f71454f-67be-343b-8f9b-aa1d1b80d3ff | -6.47731 | -42.76459 | 2026-09-22 04:02:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5e154bd1-c7d2-31bf-a786-074ca11b906b | -10.25588 | -49.98566 | 2026-09-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b2a6caa-cf00-3da6-b7e3-bdb088449c0e | -11.87149 | -46.83693 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba46540c-f4f8-3ae1-a20d-a2ca1e9cbb1b | -8.78932 | -44.27623 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| da3e67dc-acf3-3bf4-aecc-3d752a57be95 | -12.55961 | -45.96343 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 91ef01a8-e6f0-326c-b5e3-435b181519c6 | -11.4706 | -47.74654 | 2026-09-22 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eee5df6e-5b6a-342c-97ef-c0b9e5ee9a9a | -12.55681 | -45.96043 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1b50aad4-8557-3a20-9aa6-36d7a50e7cb1 | -11.43861 | -47.32937 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3af001d-cd27-373d-8d52-acb9242bf78e | -12.84021 | -44.34007 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |


[Clique aqui para ver as próximas entradas](README35.md)
