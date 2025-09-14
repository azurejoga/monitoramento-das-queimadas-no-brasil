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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2996323a-2763-31b7-9019-a5a189ae5e24 | -12.97372 | -48.03234 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 57ecb24e-9461-3f7e-8e3d-45bd57f46da0 | -8.77326 | -46.02253 | 2025-09-14 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c155e172-39a2-3b3e-9c7b-4801d51d751f | -12.77822 | -48.04648 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f2a31a5a-e99a-39cd-8b29-f9ce27ae30d9 | -8.91603 | -46.17773 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 1988e7e9-177b-3170-a169-5e6275690fde | -8.94589 | -46.16966 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| bd27acbf-a71b-3edd-89ef-c517ba1c7f16 | -11.38701 | -47.33989 | 2025-09-14 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a72cea81-c5d1-3860-854d-dc2e0fc9c72e | -8.81825 | -47.12458 | 2025-09-14 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| db4b86ab-ccb0-3e5e-984e-b95a2710a665 | -9.0988 | -44.81504 | 2025-09-14 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 41c9614b-fc78-30dc-b59c-9608e1f0fd9b | -11.32718 | -51.13866 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 586e1e0f-3878-3161-bd32-453788d91616 | -12.76575 | -48.00772 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0ddfe767-304b-38fc-a4a2-dc9d4adb9934 | -11.28866 | -50.80689 | 2025-09-14 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 488810c5-dfee-34df-a3f6-e614da2a1eb3 | -10.76743 | -46.51351 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9665380c-a547-3a50-a832-506658e1d0f1 | -11.45376 | -43.56551 | 2025-09-14 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8e734fdb-07ca-336f-b9cb-230d8304fd51 | -10.76999 | -46.49535 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 34bb2e30-9f47-349f-ba17-b2ea6e62d7e1 | -12.82456 | -47.144 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| ae42eecb-6c8a-30cd-adda-4e883b1eac71 | -7.51115 | -44.38487 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bbd526b2-5686-3fda-8ec0-39e7fd551937 | -11.63255 | -47.36683 | 2025-09-14 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 71f1155b-3804-34a8-bc86-3b82e45f1152 | -13.47872 | -41.47405 | 2025-09-14 12:17:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 1f79b946-753b-31ac-bf32-15fb2a5dee1b | -7.70981 | -44.87024 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 69ed80ce-91c4-3547-9e00-feeed9ce3b80 | -10.76614 | -46.52259 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47dbb9ba-2361-365f-8fa6-a07eaf9afa01 | -12.81439 | -47.1518 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b81cc2b1-5650-362a-bdba-b40ef4341bbb | -10.91074 | -47.19479 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b51ab3a4-5608-3cf4-aef7-f7f30b285154 | -10.182 | -46.15595 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d6832013-ff74-33ac-acff-bda0fef46877 | -9.00596 | -45.80761 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| fa079b4d-2478-33fe-8820-cfc97688fb9e | -6.40202 | -42.80403 | 2025-09-14 12:17:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 3895db9a-a337-3b6d-a521-756a5a9a07d4 | -10.76871 | -46.50444 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0662e8a8-5bbb-31c2-95e1-2ebb1bf377dd | -9.0202 | -47.06593 | 2025-09-14 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f3f5a0c7-80e9-3c5d-9754-2e59bd999a6d | -12.75982 | -47.1532 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1a1c5a24-bda5-371c-8774-1e3755790484 | -8.89681 | -45.46858 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 01f26ab5-83c3-34bf-8143-654777957e1d | -8.96244 | -46.05236 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c60bd3ae-38f5-3fa0-9ec3-a447f779b7ae | -13.5193 | -41.4656 | 2025-09-14 12:17:00 | TERRA_M-T | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 72f092b7-f59e-39a7-a0db-0d5bca01999a | -8.90841 | -46.16751 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| a8b787f7-231d-3ecc-96ee-cf2faeaab20d | -10.9331 | -47.35317 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0ec10b6c-62df-3229-8cc0-f38252e45dcf | -5.73437 | -43.19884 | 2025-09-14 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1034759d-52f0-3b56-b7c1-efdc5713c8b6 | -6.47511 | -45.65059 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 54cf54bc-7f4d-3ad9-89e2-e37f1ddfe07f | -11.2447 | -47.6242 | 2025-09-14 12:17:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a9c008fe-3ab5-3d15-ae2b-a113bd366b29 | -10.67545 | -46.25292 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b4fada74-c513-3f9c-aa1e-be5ea5537b8b | -11.37688 | -47.34757 | 2025-09-14 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 52016454-16b9-322f-b16a-10a3875c6308 | -10.63974 | -46.2415 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 2720cf17-7b95-35fe-95d5-ad3b3a39b8d5 | -12.77724 | -47.99086 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 8141066d-4bdf-3012-8a20-798e4581e265 | -11.70809 | -46.90026 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 50032f33-9cb4-3156-b0a3-165d90a0eaed | -11.27095 | -51.11082 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0e0bca5f-de49-3cde-9da5-545a3cfda93d | -12.78708 | -48.04779 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 0ebde84f-ad83-3336-bcf6-8d0640f8b695 | -8.94422 | -46.04365 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 75a25b90-9a94-3d92-a3e7-d66d39f2dc0f | -11.27291 | -51.09835 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7da2855a-535b-3e87-8c64-63bf0d4d6d23 | -8.99955 | -45.78801 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 49ca3338-d8f9-3afc-84e0-ec51cb1bdeec | -11.28323 | -51.09998 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1de0bdac-3e9e-350f-9713-50447de69608 | -12.0445 | -46.53846 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2023361e-83b7-3802-ad57-5560d3af5060 | -11.29228 | -50.78309 | 2025-09-14 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 346ee3bf-8eb7-32b1-8d45-2229d293da2f | -13.50427 | -41.4845 | 2025-09-14 12:17:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 152.4 |
| 2ea9cca6-4356-3d4e-b974-e44665045fd0 | -6.3182 | -43.3437 | 2025-09-14 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 193f4107-e535-3f67-b55f-b593c78abab6 | -13.504 | -41.47763 | 2025-09-14 12:17:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 174.8 |
| 7dcb4995-b231-38c7-bf0f-3d9d63a1b191 | -9.73724 | -46.04349 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cec57556-4f53-3de8-a80d-c1919c6db352 | -7.22793 | -43.84825 | 2025-09-14 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 46b659c8-974c-3a4b-b0b5-4ffddcd98f53 | -11.29408 | -50.77123 | 2025-09-14 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f7de90bf-da9f-33fb-aa15-0030d819233f | -12.13637 | -47.57148 | 2025-09-14 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 82660f3b-bd47-3887-8e55-ec4ed5611878 | -7.00108 | -44.53596 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5dcfaa07-192b-3ef6-af58-cec7d729fe8e | -6.99836 | -44.55544 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 395bb563-93bb-36a9-ac40-da726f081b4c | -11.77434 | -50.51101 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2a00d92e-8c9c-3c68-99c5-651f50d1132c | -8.09084 | -44.50708 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 36ab4101-d4e7-32ca-9b74-8835aa85ef54 | -11.76103 | -50.53208 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 7a6f6d02-d95f-37dc-8adb-b2931ab198bc | -14.31485 | -46.09016 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3739ab7c-2f29-3cee-aeb7-8d0158e7aa48 | -14.28107 | -45.10904 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cdd2e871-ba58-3c0a-b95e-53b87b96be51 | -20.18918 | -47.0476 | 2025-09-14 12:19:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9b3ff23f-6e50-32ec-b590-2f35eaf29a1e | -14.21982 | -46.18205 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 666ab42c-df8c-3fc7-bc34-3802d5b65d83 | -14.17793 | -46.15976 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 09912510-42b6-3671-9b46-3ce5993b4b81 | -14.21848 | -46.19186 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1a1f1705-053e-31e9-af6c-ad98877179da | -14.48061 | -55.96151 | 2025-09-14 12:19:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| aa9b3048-9c4d-38f1-9071-bad0e9e3ff59 | -13.93714 | -44.85411 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7f5fc215-ddfb-31e8-ab66-af53a82358a7 | -14.1793 | -46.14988 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2f4f8099-4db6-33c3-a5b2-fe960d174dd4 | -16.52465 | -43.76869 | 2025-09-14 12:19:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3dd8d03a-8815-360f-8325-a98a8fdf64a4 | -18.03049 | -46.96482 | 2025-09-14 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 101e6b21-c5c3-3e6a-a36e-509ab0489dd8 | -14.19192 | -46.31839 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f1cb40a7-9161-3e0f-b2f3-0277cfed6659 | -13.93564 | -44.8656 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e7d8ccdf-fa13-3b5d-84f0-4c508aaed0a3 | -12.93787 | -54.73899 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 1d38ad0d-28cd-36e9-9456-9d3cc0145fb5 | -15.03531 | -47.99929 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 03efa94c-c000-322e-a44e-03eb76357811 | -15.20899 | -50.12596 | 2025-09-14 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 4d52caa5-3e4c-354f-a332-a9fb3eeb799e | -20.45908 | -54.54348 | 2025-09-14 12:19:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b39b74c2-af1b-334a-af8e-6a1fc68b3cf3 | -16.6579 | -49.76064 | 2025-09-14 12:19:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f5b01b84-a91b-3ff1-9c30-8617e10f8ab0 | -19.72188 | -45.42773 | 2025-09-14 12:19:00 | TERRA_M-T | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| df90a43d-6f60-3caf-a4f5-3056284410eb | -23.05348 | -48.58239 | 2025-09-14 12:19:00 | TERRA_M-T | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9dfe1f4e-ecb3-32f3-9500-d16a13d50867 | -22.50592 | -50.631 | 2025-09-14 12:19:00 | TERRA_M-T | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 67cafe9d-7f97-3274-bafe-60128dd3a235 | -12.21736 | -53.87521 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 5d418630-3a71-38fc-bdb4-9983c731516d | -14.13854 | -45.41739 | 2025-09-14 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 34d3bf23-1dcc-372b-94df-3c6833667fc9 | -12.69149 | -54.72179 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 932fbc09-3d16-3b4e-bd76-5ef33b31732e | -14.33203 | -46.10263 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 1afd88e8-297a-30d9-ad1d-235f4f7ff8f5 | -15.72571 | -56.21124 | 2025-09-14 12:19:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 354dc97e-b5da-3901-a8dd-e426cc4c38fe | -15.92478 | -47.23627 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8e412d24-34ce-3055-8317-d517ef0df688 | -15.84186 | -47.2371 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| fb7e2ee1-b79e-39d5-8b3f-ab59c207eed0 | -13.72377 | -42.82232 | 2025-09-14 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 805df46d-f200-3402-8327-dde78662c49f | -16.98997 | -45.85881 | 2025-09-14 12:19:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 17b28201-0998-3049-a9eb-8612584efbd7 | -12.66032 | -54.68676 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f0b4ad6b-93bd-3dfd-a374-e482a76ae841 | -17.36295 | -52.90683 | 2025-09-14 12:19:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9a5490ce-64cb-3fa6-9c1c-0eb3d0c2baab | -15.64795 | -47.04193 | 2025-09-14 12:19:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 824f5529-c03e-321d-a878-62ecc134bd47 | -14.18559 | -46.15721 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 4fbe89c5-91ea-36a3-9f55-9924d37c2458 | -12.68575 | -54.67611 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c97d7d9e-59d0-3f31-9550-9e1b368c4b1a | -20.3838 | -50.50914 | 2025-09-14 12:19:00 | TERRA_M-T | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| c73a180f-e043-315b-a0f4-107cbc3674a5 | -15.84055 | -47.24655 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 2afb3cfa-a725-3b75-9ec1-ee221d2ba400 | -14.21193 | -46.17098 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4b2c23e0-0c63-34f4-9dcf-89f1e17868ea | -14.41132 | -46.40069 | 2025-09-14 12:19:00 | TERRA_M-T | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README80.md)
