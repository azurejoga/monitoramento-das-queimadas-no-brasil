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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe68aaf1-acc3-357d-b34d-18a2d7a3fa6a | -11.20694 | -47.71238 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2367b4b9-fa5b-331a-b507-ca913427a2bb | -7.31165 | -44.60128 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25db10bf-09e2-302e-8bf2-2ccb8320c8f6 | -3.22394 | -42.80218 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8f7d0557-a27b-3dc7-a3f5-af9a3059f30e | -8.49091 | -49.60212 | 2026-09-28 16:26:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 93a113eb-cc5f-388d-bd8a-184b62f5a996 | -9.49095 | -46.35518 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9e221e5c-e5d9-3e08-a04a-bb7b8ddd0e64 | -9.77633 | -44.86297 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 32518cf1-9335-355e-bbb1-d536b6f0c7ea | -9.49659 | -46.35674 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7641440b-b615-38bc-98d2-99396792782f | -3.20549 | -42.48347 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 27353a0e-0958-330e-b069-095b9ea2968f | -11.15489 | -50.06316 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b43c14db-7c74-3ffe-8e9b-05802aa773d1 | -9.0686 | -47.18272 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f69505aa-4b59-3dc6-950a-b464ba70f029 | -8.66902 | -45.36517 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ac53864a-2829-3e51-ac5c-86d4eabed29e | -4.32452 | -48.62904 | 2026-09-28 16:26:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 104d1d8e-4318-3728-bd31-3afa5820bee4 | -5.57338 | -52.04871 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa36d8bd-cfea-3375-b171-1091adf8212c | -9.06812 | -47.17915 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44880754-b3b8-343c-a74f-3676068328f6 | -7.38081 | -42.1296 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| df2c9a09-1363-3771-8aa2-f0bedaeaa2f8 | -8.10436 | -39.59463 | 2026-09-28 16:26:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 57ad7cbc-44ed-3a91-90ab-34226a9226cb | -6.93072 | -44.04026 | 2026-09-28 16:26:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9362e55-75ea-3f6c-a807-eead521b7efa | -9.25936 | -47.36411 | 2026-09-28 16:26:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b3bbcbb2-009b-3a57-819e-5d0c200d46bd | -7.26177 | -43.35434 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bebccb96-e86a-3c5f-a82e-77e8533b4971 | -10.24453 | -49.99855 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3ba32097-09b8-3225-b4e2-73c4528e808a | -11.34122 | -54.11008 | 2026-09-28 16:26:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8dedfdfb-fb6b-329a-91ce-19a8880fd3d6 | -10.92251 | -50.70834 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 99e0644b-b840-3d50-be16-db50a02a701c | -9.07714 | -46.50132 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f1eb2a17-40a6-3c54-b743-476911471b11 | -9.38732 | -46.38755 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf7238af-fe1b-3639-a9e4-93ed3ba7dc1d | -9.85188 | -44.93972 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8953b161-e032-3632-8de2-d9fab78ec993 | -11.10352 | -51.11554 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e5625764-e3e2-309a-b647-3ca004a038f4 | -7.72468 | -44.91032 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c401fd36-bd7a-3d69-89c3-20281462583b | -8.02973 | -42.84669 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fb1a4e37-8dd9-3d57-9673-bbec294c0bc2 | -11.15527 | -50.0661 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4d867248-1cf2-3ecc-8f7e-66de387a409a | -10.19719 | -49.99438 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ef5e742d-5663-386d-8dd6-921069f0c3b8 | -8.73811 | -44.90004 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4041ae50-7f1c-3a3f-b0c0-6dc173be27f1 | -9.5212 | -46.37555 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 08d0574b-bddb-348b-93ee-fc5c017a58f2 | -9.3295 | -45.36314 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1d9a8b26-1f15-3ef6-9338-056de893cc93 | -8.367 | -45.47055 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 205c9491-cc96-3a36-89ba-06dca8e79d46 | -7.49834 | -44.56166 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7a786ba4-1068-3d8e-adc4-93120fb192d5 | -10.95466 | -50.6646 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 26bc52f6-a640-3ff4-a3ba-a65918d1f2bb | -8.7772 | -45.83047 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 5e2cfd6f-7b18-3f52-a3c2-43b56100c532 | -11.14404 | -50.05854 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ef9ecef0-8724-37f5-b370-a4bc99254c04 | -11.34206 | -54.11029 | 2026-09-28 16:26:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ec982dc3-9d95-32b0-939e-a408ab3f3d5d | -9.83449 | -44.93756 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 39c8c53b-637f-30b5-83c0-582343730907 | -5.1856 | -37.06555 | 2026-09-28 16:26:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 843385e8-9279-3e70-9ac0-eaeb329a19fc | -8.73222 | -44.90887 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2bd0a989-d5fc-3284-9c65-71b99bc59e94 | -11.70057 | -50.03764 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3bcb56a-9e2f-307d-bb71-2945489592b4 | -8.03025 | -42.85017 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 230.1 |
| 204729fb-1e0a-351b-9570-3045654c0672 | -9.09613 | -49.89249 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 03bfa3a7-c538-3c99-a35c-9fe50c3dea87 | -9.75517 | -48.19927 | 2026-09-28 16:26:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 53862363-7032-3a95-8146-af32921e416f | -3.88644 | -40.8357 | 2026-09-28 16:26:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bbce42f0-e9d2-3e56-a3d0-747332c56919 | -7.40806 | -42.61951 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 703d0557-476e-34f1-b652-427a5e065720 | -7.71308 | -44.90413 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fe2549c6-27bb-376a-b630-fa601c8a8334 | -5.38842 | -45.67692 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4c399509-f8d7-30cf-91dc-1481d793ce6b | -7.26715 | -45.33455 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 616602ac-9389-377c-95f5-07ee94ca1caf | -8.35262 | -45.47284 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6c0c4835-3ed2-36b5-acbe-9fc3959448a9 | -9.52889 | -46.37443 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e5cff6a-822f-3244-8d9f-27bfa0c9efd0 | -6.71556 | -45.58847 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76e7addf-709e-3864-bab3-387820c36542 | -10.29109 | -49.96945 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7d65c6c5-76e8-32e3-b9ec-41ba71d006c7 | -7.54183 | -50.92973 | 2026-09-28 16:26:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aac2656d-dbb2-31d9-9351-eb1bc0589ac4 | -3.22008 | -42.79921 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 414fca5f-42cb-38f8-96f1-305cffcda370 | -7.47563 | -44.86012 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68a7fbfd-17f9-3b99-847f-9b6717cc595a | -9.93351 | -50.23574 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| aced01d8-1f07-3ca3-a938-e2cc86cb1b12 | -10.78068 | -48.74541 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7401fe75-7d8c-35cd-8d2e-2cac8abea765 | -10.93239 | -47.58756 | 2026-09-28 16:26:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d06f345f-111d-3220-a5cf-4ecd5186491a | -6.31773 | -43.61694 | 2026-09-28 16:26:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 64e17df5-3770-312e-897b-a805ceee0095 | -6.76427 | -43.60846 | 2026-09-28 16:26:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8c96d16-09da-343b-8b5a-c2e5895cb66a | -5.72348 | -53.45148 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| ec5d9313-5140-3f2f-a6a7-f70648e9ef12 | -11.13938 | -50.06215 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2da42674-79dc-3088-80f5-343ba61c8e2c | -9.97553 | -50.24506 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 051b008c-427e-3c56-8d3a-010999c5ed51 | -6.36079 | -45.80008 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f3e843c3-ccd7-33f7-b481-d5f347504423 | -6.9506 | -41.61051 | 2026-09-28 16:26:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f4b0baa4-5a84-3d78-99e8-5b9ac36fd5f6 | -7.49068 | -45.96306 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b06dd73-4a99-3500-85ff-3df2a38c619b | -11.12855 | -50.05753 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| dd393e34-7c03-3226-b8dc-6c7c58115c63 | -3.77771 | -45.44363 | 2026-09-28 16:26:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| aa36b159-ce50-3445-ab89-72494ba7fd4f | -9.80159 | -45.71189 | 2026-09-28 16:26:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5a035524-1321-3f2f-b0bf-c34b1d42bde9 | -9.76511 | -44.83565 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 7e960901-8f9a-33b4-9205-d31c58a52e57 | -7.31508 | -44.60071 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35b77a9f-8f0f-38bf-be46-ec95bf24caa2 | -9.97951 | -45.36674 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 19455978-1ea1-39c3-89f7-7c3c71d8f68f | -10.97482 | -50.69819 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 143803e1-99f4-360e-a8d4-600e9d3a5930 | -10.92851 | -43.87261 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 581dd8d3-66e1-37ee-8e69-e25e1d366b9d | -10.552 | -49.77695 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d740163d-178d-3c72-9e1f-8a7751d7b5ec | -7.40624 | -42.11857 | 2026-09-28 16:26:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| d3012361-080f-333f-b23d-a2a3369a9e4f | -8.05714 | -44.81435 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 798ef91c-2809-392b-96f5-f42666f39e27 | -10.78948 | -48.74115 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 91256c7e-4176-373d-92f6-c5837d99bfd2 | -7.51402 | -44.57478 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 978b87ff-54fe-3b2d-80b6-48483d4cde01 | -8.63384 | -49.47982 | 2026-09-28 16:26:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5792427c-2ce6-3e4b-9ed8-2e77ae2383c6 | -10.207 | -49.98059 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| de944726-9024-37ed-abeb-d0be37439548 | -7.38433 | -42.08639 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 56ca4f99-6f9c-3e3b-9771-6be8e7d2ab9d | -7.68416 | -44.8768 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9ac00115-62da-3c84-9aa5-28e2f5d0212f | -10.9607 | -50.67038 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 163b1046-7c14-3ecb-91b7-ef36faf3ae06 | -10.79885 | -48.74195 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 7b964b8f-60e8-3280-93d5-f6596a747507 | -8.3005 | -45.41733 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6e3c24a2-6ec0-331a-ae3b-71033b379bdf | -6.22638 | -46.63741 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a75b6e9e-a6bc-3628-9f04-050855b14ca1 | -11.16031 | -50.06546 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9cead900-ef6d-3415-bd2a-62435b2edfe9 | -4.25961 | -46.89051 | 2026-09-28 16:26:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 0918ff3d-8a43-3194-a8af-dccfc29a3e7b | -6.19865 | -41.62155 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 478d08c4-b28d-3ac3-bfa2-a7a582984fb1 | -7.27823 | -46.93444 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7c116081-3175-3559-adff-cad430f98072 | -10.48846 | -51.29748 | 2026-09-28 16:26:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 97dd7709-e2e5-32e6-a60e-ee1df893de3d | -11.46117 | -49.74452 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1693347e-dbd5-3fa5-8c25-ea04aecf5470 | -7.44674 | -44.59241 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9fc97ed-dcd5-3921-889e-5490dbdb0f34 | -6.92735 | -44.04077 | 2026-09-28 16:26:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6bc11dde-86ab-39c7-9763-1a731ce2fded | -10.22048 | -50.0075 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| ee008c71-6b77-3ca1-8d94-d392a757d159 | -9.11695 | -49.90059 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README109.md)
