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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 863119cc-a607-31e6-806d-c6ea009e8a58 | -9.39484 | -51.6387 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af340ec0-dd09-3a21-9b73-bf35daa97329 | -11.7735 | -54.50965 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6325b3c0-cd7b-3c70-b844-d84f3bec03cc | -7.37259 | -45.06681 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 26b8a615-9dde-321a-9ac7-4489c6344e10 | -12.19303 | -57.23322 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f3d87c2-26bb-3f03-9a65-bcf984de9def | -11.48043 | -58.50959 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b3e95834-e036-3adc-9725-4d81917529d2 | -9.67205 | -47.95504 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f4759c8c-fc9a-3e2a-8fe8-8be755eaf114 | -10.12764 | -50.3185 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 233c9a3d-a8ff-3cb3-94c3-1a1c81190943 | -11.32211 | -45.18343 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 8ea358fe-c165-31fd-818a-d6a1246c029a | -11.37499 | -45.19564 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5dc0b830-b136-36dc-8fd6-575e7cb94abe | -10.05422 | -48.68039 | 2026-08-31 16:50:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 00d3fd2e-5234-3bdd-8a33-0ffd5007fe61 | -9.61379 | -47.62245 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bd3956f1-68fe-36e0-a59d-305a6f4dc04b | -5.57974 | -42.3366 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d5b5aab8-a96d-38ff-90cc-bca55e61d948 | -7.69147 | -55.3392 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 794f3b2c-e4a5-3570-988d-510c849b4c26 | -9.16627 | -59.54213 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 722bd5e0-3eb1-3c67-8865-aae3488a7770 | -9.47576 | -57.02526 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 712de4d0-7b19-313d-a153-4a968ab6242b | -11.21521 | -45.10412 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5567894b-e3f8-3eb2-b5ef-d8564d849375 | -12.10873 | -47.27162 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5226299d-7a83-3f90-bfdc-4619404e8068 | -10.86185 | -50.48363 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e30fde86-df2b-3a35-bd5c-9c5860d8cdba | -11.21882 | -45.34958 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 605bc3d7-5614-372f-858c-42456abe43b9 | -12.8972 | -45.83865 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 446b7c2c-378e-3197-8c70-232907caf784 | -10.57798 | -57.50182 | 2026-08-31 16:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d3d74f5d-e691-3d17-888a-9139f89bab1e | -6.69763 | -44.03754 | 2026-08-31 16:50:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2b76b173-70a2-39a8-8f8d-9b7be6b6bba5 | -13.96329 | -54.3978 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 82ff66ea-1974-30e0-acda-52e18e3b0069 | -10.02128 | -45.5625 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3f657e21-32e7-3b50-bdcd-93abfa25dec7 | -6.93923 | -55.63752 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 2b4fa414-2f3d-331d-9283-5e50dc13d368 | -9.65016 | -46.05113 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2e8ed7a-5499-3561-a05c-99bda82f26c5 | -11.07678 | -51.52901 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ce8b8a2d-95d0-3e4e-b148-983942809ec5 | -5.59086 | -42.32178 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 42223a3b-d8d6-3db6-bac8-4920c6f6c9cd | -10.11623 | -50.31248 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f0f1662-bf19-393e-bf91-212417af76f8 | -11.31857 | -45.18404 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8db99248-3fc8-344b-a783-016f8461f103 | -9.64668 | -46.05167 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| adb6fbf9-c1ca-371d-830a-788689ab8e62 | -13.94225 | -54.41528 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80a2b4eb-855f-3c36-8825-0156a882df39 | -13.27539 | -51.60714 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 2ee7b15a-f36a-372d-b80c-2316179d8baa | -8.74231 | -46.44913 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ada7e9c-2d9f-3aef-97b6-44bf6a53db73 | -10.10389 | -50.27577 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3eb3837b-21a5-31e0-91b8-f814235cf4cd | -11.05196 | -49.68343 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8f8ac489-0a4c-3b69-afd0-20a24d3d1f86 | -11.51811 | -46.94268 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 852ff0cf-e434-386a-be8a-74be0c98acf3 | -10.15595 | -45.69797 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e8338147-0828-3594-8cf9-c5f53ccc19ea | -13.84502 | -54.09587 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 38b201c1-d473-3d54-ad9a-40418b52984a | -9.8363 | -47.83184 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f8eec7d-2e8d-3ccc-87e4-1c047ccc29ac | -10.836 | -45.99341 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de582976-754e-30de-ba0e-3791f353bb76 | -11.37978 | -45.20411 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a5c15601-5c3b-3ecd-b4c0-4c96845e6e07 | -12.10128 | -45.02745 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| adb557ab-b272-316a-a89c-3d63763f0120 | -6.40961 | -45.42538 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0be1978d-7b73-334e-8495-0bea13921d9e | -6.40329 | -49.93068 | 2026-08-31 16:50:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 481d17a5-43f4-37a0-9e5b-b82b76254fdf | -10.82386 | -50.68974 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| d716194b-de5a-31be-b9ee-8b51fd8f30ed | -10.31518 | -49.99907 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1e9ea2fb-744e-3f33-8c80-57b2f9870512 | -5.59166 | -42.32644 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e4217d9a-56d9-3fb6-9912-96fad922f4fb | -8.92322 | -45.04127 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| be67c970-fbad-37fc-8b96-087dd39e0ac9 | -10.47592 | -49.95233 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f95bc569-6782-39ca-8610-a2611b627a08 | -6.25739 | -42.86944 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 662533c9-1a52-3c47-8a6e-0f83167bc19c | -5.76392 | -44.11752 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b8c63bad-1d61-3fce-8e79-2e51759f5f8a | -11.02932 | -49.69438 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e9ac2e38-f048-3669-9414-4bcc3b2e87fb | -7.60225 | -44.93031 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1d6491be-7421-30a4-97bc-05558a6635d3 | -11.35131 | -45.229 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8c3b428f-d65d-3927-8124-f4e59356e730 | -11.68392 | -47.59812 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 06e486ef-cbb1-3e6c-ad04-a8a51b9b1d0b | -8.70047 | -39.23358 | 2026-08-31 16:50:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5bb3aad0-87f9-35ce-bcee-0de1b7b552d3 | -11.07067 | -51.51215 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d68de85c-c353-335f-af39-6be2eb71cef7 | -8.76627 | -46.44958 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 033fc0a5-6593-3ffc-a2b8-7975473d22db | -6.91209 | -55.7055 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c512cf94-8b43-3f97-84cc-48ad10f9a581 | -7.26895 | -45.35244 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1b718445-7f00-3f88-b94b-56b607e3f98f | -11.52637 | -45.50728 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9c73297b-eb77-3517-893e-09fe938692a4 | -10.04428 | -48.68192 | 2026-08-31 16:50:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 2872df41-4bb2-30fb-9687-65e1a94922e6 | -9.67152 | -47.95155 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 40d1c134-ece0-33b8-b681-47f670f32d0b | -7.79245 | -44.07379 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 91b35298-f91c-3d93-9578-3ab3862ac646 | -9.41236 | -51.68306 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1fe6dc52-d461-30cc-b8ac-16a773d0c207 | -7.00634 | -52.89058 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 152ddbfd-b0ad-38ce-bd6f-2cf30b329fe1 | -7.43985 | -44.95505 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3fa8944b-b668-3343-aaa5-04ab26303aef | -7.74488 | -44.73516 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 598e5dab-f6f0-3741-ad28-a371f43d51f5 | -11.93472 | -45.09642 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 50d8255b-759b-3997-928d-bde6272d97f5 | -13.43935 | -51.75984 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b5827f2-52e9-30a2-9341-0dfbf7e9ca82 | -10.99666 | -48.38609 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d0580db-9843-3405-b874-3574c06de0ee | -10.83497 | -46.00917 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bd2e34d0-f74b-3423-8bbd-8b9ea29f3928 | -6.25815 | -42.87394 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5461605d-3d0f-3aac-a23e-2e20564c9a28 | -6.82008 | -43.53947 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 02fe61c1-6613-3fef-863c-3ebbe12ffcb1 | -8.6111 | -54.82436 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4b4c2062-d260-382f-9f80-f9ee08f7964c | -8.76405 | -45.37773 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 349681ee-6878-30ba-ae65-8d0a32b97946 | -7.09724 | -43.87904 | 2026-08-31 16:50:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 294c5cd2-9eda-397e-be67-e39a770b13f7 | -7.28976 | -52.3588 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b498926e-5edf-35af-9464-74b379bf31e7 | -8.85707 | -47.08553 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c8b3c05b-74c5-3ac1-9053-bcc0f9d21d77 | -11.19947 | -46.1199 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 98619d88-2c0a-35df-a9f8-668d3a9f3ad1 | -11.19799 | -45.04331 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8d75f8e3-b1b2-304d-9cd4-66af8cd8ebcd | -11.32653 | -45.16586 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 98bea25e-9ada-3c46-ad83-f7fd3df842ba | -10.85188 | -45.32275 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 80e38fd6-8f15-3ee3-b0dd-362e88c5016a | -11.24912 | -45.09452 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d8c35610-cce7-3edd-a92d-4c20b2fefae5 | -8.75775 | -46.46263 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 15f78f1d-768b-3509-9a8c-5a4a4d0ca5ef | -8.86209 | -47.07354 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 473b2c35-22f4-3bd2-9673-97c3874c0f1e | -9.59719 | -47.6034 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 80e5e79b-bba7-33cc-abfb-0d28a8705165 | -7.6175 | -44.88103 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 77c5f289-2ab0-329a-b3a9-d739ca5a87ac | -11.21538 | -46.10975 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| cece8b70-b695-3da6-9f15-7011aeba7146 | -10.54013 | -50.77528 | 2026-08-31 16:50:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f1d900ec-49d9-3a2c-9635-122b756bb0a4 | -8.82651 | -47.95242 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 08b482d6-aa7a-3403-a27c-778ad4bbc3d2 | -7.93967 | -44.23758 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e15d1e6e-8d59-34de-baa7-5272ad0a490f | -10.10717 | -50.2984 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8e9189c8-e5aa-3042-8bb7-bc9db2a6f9f1 | -9.16575 | -49.98734 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 95478353-834d-3499-8301-1124e65e9f7b | -5.58819 | -42.33054 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5c65fe61-8632-36f1-b92a-afabb2e80adc | -7.09484 | -45.78183 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| daa5f90b-ad70-3165-aa56-aa2ed2cb159e | -9.17177 | -59.37129 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f63fada5-60b7-3132-8adb-f5228449dbd6 | -7.36089 | -55.192 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4215e3ff-47fe-3841-afd2-723d29503740 | -13.46493 | -57.04361 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |


[Clique aqui para ver as próximas entradas](README155.md)
