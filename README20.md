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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e50cf3-d8bc-34ce-8a3a-7508ac939928 | -6.5926 | -47.17191 | 2026-09-28 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21e50a1f-9a80-30c0-8d88-0dbc01bd0472 | -11.54349 | -50.52898 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5754c5a2-d482-34ee-8837-6d5437f96d44 | -9.79312 | -44.82811 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67e9d1cd-035b-343f-8eb8-838829058e84 | -12.30876 | -46.40491 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 979fa3e8-bbb1-37c9-b076-3fbf1471cc3b | -11.20467 | -44.78741 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7c00bf7-1070-33c5-a676-a3be626659fb | -12.7222 | -47.28483 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba74c452-d7f7-362c-b614-73ff3c427ed8 | -11.70356 | -44.52655 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0881eb66-537b-34e2-aec3-b6369ad8c449 | -10.25659 | -44.61504 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51273874-0ba3-3d7a-98d1-9ed534de7e9a | -7.7153 | -39.34961 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa0e92b5-be7a-3d8c-8a41-4919aebdf7af | -8.1373 | -44.44799 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9843a96-6eae-39bb-9b1d-7ea13368ad22 | -7.28081 | -44.31319 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4c9aeab-4d06-31d9-93ec-98e282abe359 | -7.34982 | -42.07619 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd53c705-c055-3ec9-97b3-46f06b99bef3 | -12.65483 | -47.31914 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e9a6555-badf-342f-806b-571e92d88441 | -11.18351 | -44.81795 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a873043-bfa5-392a-9ae2-3a0b7e94f59a | -6.98837 | -42.70414 | 2026-09-28 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4a557e2-3a89-3aa7-b2c2-800491458528 | -12.31393 | -46.4142 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cd223736-9ecb-3ecc-a893-f5bd3e3bf6dd | -8.73162 | -47.98355 | 2026-09-28 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20400034-652d-3c7d-83f5-219c478b1604 | -12.71079 | -47.2827 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc3c4a0c-9f3a-3e65-a4a5-7fc6e54efc6c | -11.38123 | -43.42278 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8b4f317-5f33-3950-b19d-75d2c06c64ae | -10.21538 | -49.98679 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14c4fcec-2aa9-3778-b5b0-136bf2817a96 | -13.85534 | -46.37953 | 2026-09-28 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84c64d69-34fe-37e3-bf9c-40f18957e364 | -11.38039 | -43.42738 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88956f2-189e-3daf-b8bd-b41d6758ca43 | -9.98185 | -50.15273 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7148670a-ce3b-33e9-a991-a438696f8cca | -11.45009 | -44.93683 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 133b8e65-0f0c-3b2b-9fe7-8bf04a6c1dac | -11.1915 | -44.80233 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| b74dbb89-fb21-3678-b70d-619eab18af80 | -11.44343 | -44.91714 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf612c7f-e27a-374b-8770-c03919149fd7 | -10.91843 | -50.6754 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 294ecda2-4ba8-3e93-a84b-c24f678d92a9 | -7.99933 | -39.70079 | 2026-09-28 03:49:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99f561a9-f23f-300c-ae86-a4338286eb80 | -11.17963 | -44.81102 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| aebf376e-9625-3421-8def-7ebe2415f8e1 | -10.19871 | -49.99723 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecbdb2c5-3054-3a47-a1fa-e9c786ac4b5a | -7.38079 | -42.10086 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 187ab9a6-9be4-3e33-9c9c-65c149d960ac | -6.98919 | -42.69941 | 2026-09-28 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5cecf1e1-d7ad-3d51-a018-affd083a57ee | -11.44397 | -44.91429 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fcac6b7-34ed-3fa2-b1df-7f854a342776 | -11.1925 | -44.79715 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4e4ba014-c389-38c7-836c-95bd80095013 | -9.81856 | -45.26561 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0afef174-6e9c-3625-86f7-b727e92f011a | -7.33578 | -42.07821 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a4424367-869f-3181-8c24-67e88f2d71c1 | -8.14246 | -44.44875 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b349bfbf-7913-3dda-8bf0-531031c89a27 | -9.98043 | -50.15967 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 075c3bec-32f6-3d3f-a508-f8a8758d2dd5 | -9.82983 | -44.94464 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 625421d5-3349-320e-8981-06980d2752e0 | -8.23697 | -45.41278 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed493d5c-9ce7-31c9-b265-f7d24581694b | -7.71315 | -39.35223 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d9136c2-b8ef-3f44-81c3-9a11068ed676 | -13.74189 | -41.27754 | 2026-09-28 03:49:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8069212b-eeb4-38f3-83ea-413a5841171a | -12.7165 | -47.28373 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9841e56-a4d3-3e9d-9b82-db8f741b2ae4 | -8.14135 | -44.4548 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7202ece0-cf61-3220-bfb9-c11baa8e3557 | -1.8548 | -47.97988 | 2026-09-28 03:49:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e0024ce-cd64-343d-9083-e5ff5196a2c9 | -12.7319 | -47.29554 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7c1ce3f-05e7-3b0a-901b-e84a980e6dfe | -8.23022 | -45.48093 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82966231-5333-3f81-a67f-4142a3f01e64 | -8.14192 | -44.45171 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73fbb5ff-34f4-3078-b283-5165dbb93c85 | -11.18764 | -44.79556 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| bf259916-d929-3832-b1a2-ac4822e146d0 | -11.4468 | -44.92674 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 694cbe99-5c35-3b57-b04d-5c8cbe5409b0 | -12.62132 | -47.27868 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c83bc2a-f85a-397d-8063-a6dd2414dbcf | -7.38392 | -47.02399 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08447df5-d9d3-3b76-8749-f0660a5576b2 | -8.28284 | -45.41208 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cc29ca8-2046-3f32-84b2-612905a2d007 | -8.36541 | -45.45797 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40bcb3a7-ff00-3212-860a-996c6d3b88f4 | -9.78859 | -44.82407 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03a1df62-bb88-34e4-8cc4-72c2642e9eaa | -9.77395 | -44.83263 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e900d83-facb-33cb-ac40-86ebbc6c4f9c | -11.70428 | -44.54932 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acae6103-f94b-331c-8709-3eab27df27a3 | -8.72527 | -47.98227 | 2026-09-28 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99b2b7d6-252a-3576-8c45-99f96d26b671 | -13.45531 | -46.3195 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c50f910-3c19-3f3d-acba-764b91c183a4 | -6.76221 | -45.37262 | 2026-09-28 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d67c400-2ec9-3e3b-af13-1b6f7b29ee1b | -8.28635 | -45.42064 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89c290c1-6194-3fc9-84bf-36702fb1b6b5 | -8.24437 | -44.83673 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3232ab3-a0d7-3366-a73e-cc9fdcd31cee | -10.92406 | -50.6843 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ffe365b-1d5d-33f1-afd5-2997d34770fa | -1.86189 | -47.98094 | 2026-09-28 03:49:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e3b149d-7456-3f11-a879-2f3a9e662a64 | -14.89751 | -41.02643 | 2026-09-28 03:49:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a051d427-22b0-38c9-b052-faaa92cb685f | -11.19298 | -44.82261 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ec947553-b44a-3445-b33a-61d2674ce6e6 | -13.46486 | -48.60281 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dbde47b0-afe8-3ea8-8cd9-7e041133600a | -11.53986 | -50.52516 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c57c6f6-2274-36b2-9d5b-5e03536f4ab4 | -11.37305 | -43.41637 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6890bb5b-712b-3e66-b101-accf5eb263cc | -12.7416 | -47.30635 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 68266fcc-a851-39d8-aa1e-7601d8ef9f17 | -7.28024 | -44.31635 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a5ada70-55d9-39b1-9574-d82da531cb83 | -12.62959 | -47.32663 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d7d0c148-8a7f-3400-8122-6e28acdff77b | -13.46659 | -48.59469 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5dc883fd-3603-3e4c-8628-ef747c6c8eea | -9.15095 | -45.63143 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a0ab0c47-98a6-3a33-a078-ea3c050c0bd0 | -11.19353 | -44.81963 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a5558de8-21e5-3a94-abdf-38e775be9c51 | -12.73761 | -47.2966 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91d9dda7-9ae6-3e78-a39f-5d145cc0bec9 | -8.24907 | -45.40834 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7258fbe-79b3-3615-9acb-f9ab0c9164ae | -7.37962 | -47.01303 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b3a8f78-7dc5-31cb-8d86-a67b5f143d4a | -10.91941 | -50.68207 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e9d43668-d761-3e9c-9e47-8b4db61f6bb0 | -6.69582 | -45.5934 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e7b9574-54a2-3716-b38b-2eca41bbeb47 | -8.42085 | -44.87499 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b762c11-a437-31b9-a5d4-9456458e1210 | -12.87519 | -44.77785 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e830a6d-777b-35e0-ad14-bc92f3e07495 | -11.68697 | -44.53459 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daf89986-47de-3b21-a295-8c67c68e6b69 | -11.70047 | -44.54291 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a04cee1-233c-3ee1-b75d-acf764e80423 | -11.38408 | -45.40051 | 2026-09-28 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97ec6cbd-1faf-3bfd-91f5-42f85fd1b465 | -7.32984 | -42.08628 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d98ff99-b541-30a1-93c6-c4c05e90509e | -14.19094 | -44.3687 | 2026-09-28 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d6f601f-07e7-3282-931c-85fe0d52fe56 | -12.68335 | -45.02028 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f5f8a1c1-f9dc-3163-b92b-07558d4217d0 | -8.3648 | -45.46124 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5198414-4a50-3195-a810-d6ed7cdb4f55 | -9.97902 | -50.16655 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d03b705e-4231-3307-9c7e-b496eccffb4c | -8.65554 | -45.42264 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 668d9455-0fb6-3cd6-900c-36aa19add49d | -6.83788 | -43.57024 | 2026-09-28 03:49:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d6bc3e7-05b3-3ef2-937a-a336d00dc785 | -11.44071 | -44.93158 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4a88dc3-7fc5-3655-8fdc-9e318c7ec2dc | -10.92109 | -50.69884 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0a46b701-2ce8-37e8-89e1-97a479ebdd26 | -10.91634 | -50.69658 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d121c26c-e820-3a48-9188-2e9943e6f887 | -11.1815 | -44.80084 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| feaddf7f-c06d-32e6-817b-a2df29f842ef | -11.66442 | -43.52659 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a55e8ac-805b-3eab-98ba-c7b95b7875fa | -9.82408 | -44.94691 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb8fdcb-7358-3669-b9ea-77c8ca76605d | -7.37871 | -47.01789 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d03fbaff-7924-3c74-bb38-600db4b50c00 | -9.32211 | -45.38182 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README21.md)
