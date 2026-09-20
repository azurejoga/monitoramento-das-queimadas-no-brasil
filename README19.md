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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8564cc9c-ec1a-305c-959f-3b65d60ff6e5 | -12.75624 | -46.21867 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27b8772f-3cff-3b90-907b-055f92aaa6f4 | -9.96591 | -46.54903 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b641622-cf7a-3a86-8ca1-f274d719b2f3 | -7.0192 | -45.24347 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e120355f-48b1-30fe-9e68-b2ace6ca86bc | -9.69801 | -48.32278 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c33880a-9eea-3e57-ade0-3f5b0cc7d5aa | -7.54381 | -45.42327 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8d3a6390-38bf-350e-802c-fe991b3fdd46 | -6.99636 | -45.68011 | 2026-09-20 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5638994-af65-3fdb-a0af-3ed3586ef8f8 | -8.76367 | -48.67527 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 282d63e0-e49b-3f67-b1f9-f93248d0f40a | -6.97203 | -42.17413 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8d08a10-4707-3daa-86cd-ea57f6d2fa20 | -9.79152 | -48.32668 | 2026-09-20 03:45:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d98cbe4f-47eb-30bc-b23b-378d8b47d5dc | -11.01885 | -46.59175 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1507a183-4aae-3056-93ce-83530711a81f | -11.43328 | -45.42197 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7a40fde-6b7c-372e-b3e5-57d51513ccbe | -7.55043 | -45.38628 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d308511-5078-3e87-86f5-f53967559c19 | -7.54314 | -45.42704 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c1248a75-7a78-3920-a19f-ed956fce0fd3 | -11.24318 | -48.38102 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc0cda45-4b0a-3d24-a7b7-d01dc46903f8 | -7.41866 | -44.69835 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 246a6773-f34f-33e1-b59b-b00da03c8691 | -11.85858 | -46.86348 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb421c79-6499-32af-a939-9eec02c909ea | -13.03634 | -46.9136 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 920cbee5-3829-3675-9d5f-2702ca857a04 | -11.66249 | -43.42962 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7c56b56f-b5fc-3eec-9976-bcb3f9562ba2 | -11.02005 | -48.30011 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2e34fa0-e16c-37d9-86e9-d89abd93e676 | -7.80265 | -44.93743 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d99a208-4020-3bef-a4fc-fccdf8665847 | -11.08754 | -48.30792 | 2026-09-20 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af89e4f8-3469-3f89-b79b-21c3f8632625 | -12.64464 | -50.92542 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0311a32-2a90-3af5-8080-e77cc390a1f2 | -6.686 | -43.62589 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acf86fb5-9c00-3eb1-9c5d-837c4c8da581 | -7.29937 | -46.74367 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9f56d6a0-0693-397a-9cd6-1e49fdc364b5 | -10.47052 | -45.09487 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5092bfbd-645d-3e1f-98ce-6afef788198b | -7.30011 | -46.73965 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c80ddcc-8649-3ffb-8fd1-aae0ccac46a7 | -10.54807 | -46.73282 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e964e64b-9c43-3369-b23c-a54b0eb55990 | -7.04374 | -45.23328 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9cf4405b-02a6-3350-b9a9-fc114cb5654a | -9.82874 | -46.44332 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5672def-a74e-36ef-965d-0b4ed3eed9b2 | -8.43689 | -45.82618 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76d560be-bb87-3148-8caa-249ff1823228 | -7.43217 | -44.74489 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7ae5baa-7381-3aff-8838-f9c5b5196c71 | -6.46623 | -48.43868 | 2026-09-20 03:45:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f7c797d-ff64-3a6d-86db-dbaf324cc9c2 | -12.1311 | -47.03984 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78ee342e-1938-3416-998b-370181f44a63 | -11.45114 | -45.3835 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d2620fa-3630-3f4b-b108-c3c893367a4e | -10.23752 | -45.35473 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bd43e0b-6eb1-39a3-856d-a0d4071dac41 | -9.22664 | -43.18057 | 2026-09-20 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c071cbac-0cf4-3e8d-8e99-b01219790014 | -8.43078 | -45.85967 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b3c309-3dad-334b-968f-eaf555e92f27 | -6.3195 | -47.62932 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 88ab3751-7929-3748-b1dc-88ef66847536 | -6.29555 | -47.61393 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9051087c-86df-3af0-8d9f-2d94816571d2 | -9.23758 | -46.23203 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6fa42faf-ae54-3cac-b8c9-ec2024fedcbc | -6.31842 | -47.63538 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 794bd6ce-0914-36c3-b345-69193ce7ba56 | -10.39699 | -48.90262 | 2026-09-20 03:45:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cac2ea7-2e1d-3d59-a959-4a19c6dbce82 | -11.66866 | -43.42124 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82d63206-7792-31d2-a862-2494ae479d2a | -11.66332 | -43.42501 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f7fed8b-8d2f-34b8-8714-55f43a086f3e | -8.65656 | -45.43705 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d268474-2605-349e-8f5e-318448009d33 | -7.42807 | -44.73722 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf876612-0d67-3203-b901-c0d7975af7cf | -6.61201 | -43.75557 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57822266-17a1-3cfd-81b8-0152923e6f70 | -6.30523 | -47.6346 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 178aa6bf-1b42-3231-a1a1-109c916a3591 | -11.85427 | -47.67542 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 83b57b69-6cb6-399c-84ed-f0e0189f97c0 | -7.43809 | -44.74229 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3409531d-ed23-3766-87fd-200fcc003ced | -6.80016 | -47.82098 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 75922ee3-d42d-3ab3-b087-5d3f0ac90cd8 | -12.5277 | -50.04284 | 2026-09-20 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 219ae581-8c3a-3a82-b08c-4dd5c46c533d | -7.8015 | -44.94378 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a78dfecf-8d62-3c0c-a570-636602d0d0a3 | -10.29889 | -45.43101 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b244758c-c130-3498-a479-4d49b92543d4 | -8.04417 | -46.27027 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f1170da-0bd0-350e-9595-4f84cb1613fe | -11.24215 | -48.38611 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88932f70-0869-3fb9-b197-0a1844e242d4 | -11.44367 | -45.39494 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6fe823d-3f7f-3359-bd63-3259d8cb5de8 | -12.11864 | -47.03041 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b0d0c18-1bf0-311b-9012-a63ad1e70e0e | -12.53095 | -50.03812 | 2026-09-20 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e3eae554-e6bf-332b-b571-257da14c11c9 | -11.8569 | -47.66211 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29332306-b923-3fd8-80f8-0db22601ce83 | -8.18378 | -40.82165 | 2026-09-20 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c2484e8-6c66-31a7-9b40-e9f18f03dee1 | -9.12451 | -45.73418 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 52abaa20-38f0-305b-97fc-410ab7b4c23b | -9.12514 | -45.73067 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| a9ab2350-b8e5-3893-bcd7-0fe9f5d797cc | -8.38782 | -45.62815 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42729c4a-6409-3beb-9265-1455f57ac249 | -7.02922 | -42.08239 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 14be68ff-a97d-3f9a-b8fc-d9900cc2f522 | -11.44425 | -45.39184 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9267ad90-b116-3df0-b8f7-86614bd1a7fb | -6.99373 | -45.68057 | 2026-09-20 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42daec4c-4dff-3037-b787-b931049ad5cb | -9.01824 | -44.91761 | 2026-09-20 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b27d90f4-0ea5-3c8c-b036-7f9b748fe327 | -12.52896 | -50.03671 | 2026-09-20 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d358d2fe-6dfc-3fa1-bd72-171ffa26fdc9 | -6.91852 | -44.90859 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c816886-e26a-365a-99bf-b8d1f42d2d12 | -8.49987 | -47.44035 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1576a159-ab0f-3125-8417-023ac9f5144d | -12.53767 | -50.03952 | 2026-09-20 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8fbf481f-4ea6-33da-af9a-a4c865e443d3 | -11.44883 | -45.39594 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df2ce131-636b-368b-9e8c-bf0f9ef4fa86 | -10.19978 | -44.14448 | 2026-09-20 03:45:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e7871f5-26fd-361c-af63-906dde6ea4aa | -10.30238 | -50.25732 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7dec8b75-70ae-3b7c-a3d9-37bc3bb5da1b | -8.37427 | -47.19639 | 2026-09-20 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebc234ae-1cd5-3a69-a29b-71a14c82cd88 | -11.24053 | -48.3735 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cbf50d3-f2cb-3ad9-acad-3d28728bb3e1 | -7.43039 | -44.75488 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f27ecb46-0006-3a0c-a551-a01538511330 | -7.76568 | -44.05478 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e89c8ed-3abb-30fe-9a7c-656e6e5a1db5 | -13.02874 | -46.92319 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 05e5c360-b4c5-38da-8d10-01a8c1bb69f1 | -8.63002 | -47.61899 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5727a1de-a1b5-37a6-86d6-c9c2a64a0b7f | -8.42314 | -45.86974 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 620f721c-d050-382b-bbd3-ee4f87f62ebc | -7.42684 | -44.74411 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27149dd1-4d7d-3aa8-9de0-43a3d4a1fb9b | -8.38706 | -45.63236 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce463b07-90e3-396c-ae22-adc3b721d542 | -11.45342 | -45.39991 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf42c8f5-d99c-33a6-8cfc-b45cf31ce9e5 | -13.01106 | -46.92549 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8c0b017-b534-3f37-965b-f5986953706b | -11.03894 | -48.30284 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ce93dbeb-ce03-3702-a2cf-81a352743679 | -9.61676 | -45.8735 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4587432d-28b0-3634-bb41-36c45e26162b | -9.00291 | -45.0017 | 2026-09-20 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3dbef67-ac31-3860-b11c-9831ab400df9 | -8.71025 | -45.45012 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6582b76-10ee-3cbf-829b-588256415cd1 | -8.22068 | -45.60761 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 982a4f19-0fb5-32b5-84f4-4609a601da6b | -11.07629 | -49.5057 | 2026-09-20 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 980cb84a-652c-3892-bea4-e7fa0f137763 | -6.75433 | -47.92393 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c65ccbf1-6a18-3af4-a218-91f4307cbc49 | -9.26335 | -46.20351 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 59aafe3d-ac80-357e-844f-40b4c83acff7 | -6.56313 | -45.5793 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d01ddff-301b-3287-8679-35a4f4c950c5 | -9.77581 | -45.06801 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 122ddcbb-1492-3d07-bae7-8a2efa7c6334 | -11.24112 | -48.39122 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d3e2535-aed8-3540-bf90-958006395755 | -7.96915 | -44.07082 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45890f22-6a89-383a-b911-430e37b5bcb9 | -7.54247 | -45.43077 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8c8c1022-8a8e-334e-8498-30bd34959ff7 | -10.31784 | -50.21697 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |


[Clique aqui para ver as próximas entradas](README20.md)
