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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bac4526-07ae-3ff7-96a0-fc667c3849f4 | -9.81526 | -44.78281 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b1c9ad66-49e6-33ab-beb4-1a805dadeed5 | -10.67739 | -47.81752 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 919a8096-1e41-35fe-8a16-5dc322a78170 | -9.44233 | -45.84022 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ec3a26fe-27a6-3ba0-bd29-f1f56627e935 | -9.4301 | -45.83007 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| b56f0f11-257b-3f1f-ac10-5159174a0dd2 | -6.24479 | -44.87674 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ad6fd8f-9493-320f-9c2e-b37526853692 | -7.90133 | -54.72536 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 27590ed0-866c-3322-b21f-ecf4a87cf642 | -6.21899 | -52.82698 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 30d8e07a-dd17-3f4a-a5b4-19cbf327dbe0 | -10.99943 | -45.48977 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 6be300ff-8dc5-33a6-9e29-827dce115351 | -6.00328 | -53.49877 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 663c5823-0971-3884-9408-86e4652e2056 | -6.86769 | -39.10166 | 2026-10-07 16:37:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9b7afc4c-054a-3152-bf15-e29f79404338 | -3.76416 | -44.65648 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 33bab500-144b-3803-b2dd-b3b0ad7cb7ad | -7.89603 | -44.176 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 58d3a5e1-756b-376c-973b-e3bc6abf24c7 | -6.33436 | -43.82338 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 234e5554-0589-33a6-99b9-9ae4873aef86 | -7.51018 | -45.77782 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dd501dcc-451c-35d2-a2e7-1f3d19823d63 | -6.00422 | -53.50551 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9da65b57-5b82-372c-841b-773ef35b79a0 | -4.78609 | -45.68145 | 2026-10-07 16:37:00 | NPP-375 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 94970274-7ffd-3f77-825d-8d1b9d5a2aad | -9.9204 | -44.81123 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e6f6bd2-0679-3ba0-986a-952c1e302f6c | -3.94871 | -40.72652 | 2026-10-07 16:37:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| c4384a9f-6252-3f7c-a364-1f1493d94c67 | -6.32981 | -43.74949 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 257ac023-7a56-3c04-97da-eb5915ad1e93 | -6.22246 | -52.85192 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 549f56ec-d9e9-3aa4-bc6a-c902b710e881 | -8.07123 | -55.29284 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 8b6ed2f9-0f91-3900-bb01-e567ec4d651b | -4.11877 | -49.06528 | 2026-10-07 16:37:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b1103ca4-bd3f-3b75-a524-02548855a508 | -3.896 | -44.1046 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1c558378-f580-3141-9bcf-d93ee93d01e6 | -7.05042 | -44.3278 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f586b99b-94dc-3d91-bed3-7120c7b36fba | -6.66649 | -52.97776 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6c9c9d81-3ced-3c72-a75c-3378485df410 | -5.95636 | -43.87248 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 95a150d5-6d74-3807-9aae-b39b03e98863 | -7.90017 | -54.71624 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5470f22f-4f79-3550-8b33-cf0788703c37 | -3.87822 | -42.2099 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9558183a-044e-3c78-a292-fc7f164a725b | -4.58257 | -40.77526 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 5044dff5-1537-3ac3-ab03-716a29f10d05 | -17.03147 | -42.36497 | 2026-10-07 16:37:00 | NPP-375 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6a8ae4b-4112-32f1-b413-6e1ba203b8e2 | -11.10809 | -47.59148 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 766e6c1e-785e-362d-a963-07e7fc1c693a | -10.52294 | -47.29073 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c2f8d563-b311-3156-a226-91da64916ad4 | -9.91537 | -44.80075 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 33da0918-53fa-35fa-bc02-d7237ebac334 | -8.53875 | -47.535 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8ac60a1-3ab8-349a-8587-75d7e1a4c11d | -5.4866 | -42.84998 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 89c52a54-17a8-3a0d-910d-3f80327fe058 | -4.83723 | -40.72817 | 2026-10-07 16:37:00 | NPP-375 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 4c7d1e68-37fb-3550-85e6-6a1b8336b2b4 | -3.95178 | -41.53884 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| ac7ff68c-ab8f-3cbd-a11f-800f3aaaa848 | -11.3776 | -46.6731 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba7dc209-7c7c-35c7-a089-14d57a18aec7 | -4.28924 | -43.02744 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1d14fd5a-a9c4-32fc-9e54-d72fd410ebf1 | -14.7813 | -41.59979 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 737c27ca-efea-3671-b49e-00038bac09b3 | -3.19502 | -42.61406 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b8e14881-0cc2-3d62-890c-6c7c5af82bbe | -5.62257 | -43.04892 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c31ceb2a-aa4c-3b63-ac80-8d99a78fd74a | -15.7605 | -43.01967 | 2026-10-07 16:37:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d64147cd-f6eb-3cc7-9026-172056d75a3d | -4.28743 | -43.64497 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| df03429c-3ab0-37dd-82a2-1853a3bd501d | -5.49507 | -42.83764 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 5b768cdb-a1a7-3259-b729-5caa496e31f1 | -11.17335 | -49.47934 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 553ce742-390f-36fd-9bfa-1423b4c6320b | -8.9663 | -47.57305 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 856df933-05ed-3a26-b8af-09339ccc1630 | -8.72492 | -48.98436 | 2026-10-07 16:37:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b367629d-8754-32b3-8e2e-8ab5375bf056 | -7.75602 | -43.81008 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7d6a5292-14bd-3ab9-b71b-09932e972ea3 | -3.58526 | -45.48233 | 2026-10-07 16:37:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3ff8dba2-a981-3f4e-808f-db2d36601e2b | -6.15768 | -51.73412 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d0378a9e-01c8-3d3e-b8f8-c54d8314645d | -3.15974 | -41.95419 | 2026-10-07 16:37:00 | NPP-375 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cb90ae3c-83f2-3f8b-9d60-bad17a5296eb | -6.17446 | -42.96447 | 2026-10-07 16:37:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| ba42fbe2-430b-3975-ae01-7eaa851eca4a | -3.90056 | -41.59336 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 995a8654-9d51-371b-b82a-c553b3333117 | -11.14683 | -47.30164 | 2026-10-07 16:37:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb806578-c664-3920-a27f-5579122416b5 | -10.99885 | -45.48582 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6466f8e3-c868-3c79-9acc-1c87651af8a6 | -6.23031 | -53.14272 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b56e28ea-12e4-3b18-b954-7f4c6d22e7e0 | -6.32883 | -43.34892 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| d8642cfb-0ea7-3058-8894-a31a9bff065a | -4.98864 | -45.63618 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d264e255-c0b0-3866-aeb5-2d7f19bef7ba | -7.00083 | -44.04739 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5230b4af-9a4b-3968-9903-e2a2f7a8fb58 | -3.95018 | -40.73566 | 2026-10-07 16:37:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b3d6742c-4a5a-3f29-be72-c68d6c00f54a | -3.50675 | -41.95604 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| d6feab5a-d986-3646-97eb-c418f90f84a8 | -8.96217 | -47.56148 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 49e0c053-0a26-363a-a14b-9bf26f4846a9 | -16.45625 | -41.06323 | 2026-10-07 16:37:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 51fa2a2a-1339-3397-9ec1-385fa649ee04 | -4.66497 | -40.56771 | 2026-10-07 16:37:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| fdfeedd3-9c6c-36ad-8627-45bf8e0b1a33 | -6.04805 | -53.49047 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 84dc46fc-ec07-3b04-8c95-b298f4d75927 | -11.91367 | -50.6506 | 2026-10-07 16:37:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 15af48a1-710b-3f8a-b832-ec17940fe147 | -11.32234 | -46.68612 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ea4a2695-f1cf-3bf1-92e6-e4f29875d09f | -9.12418 | -45.10507 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 33fb260e-fe8c-3038-8447-815a0d9df9f4 | -6.50274 | -41.83129 | 2026-10-07 16:37:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1716173a-1da8-30d7-8337-236e162decdf | -7.53894 | -39.1166 | 2026-10-07 16:37:00 | NPP-375 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 826790df-a967-3761-ad65-4f741ce4d1be | -3.47268 | -44.54345 | 2026-10-07 16:37:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcb62239-c7fc-30ea-b79b-18fdc9b4ad34 | -7.77172 | -43.80675 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| afd5d44d-7274-3914-8a50-c31cb1745b0f | -11.01801 | -47.97954 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b00ecb96-f404-3472-82ff-490e122d4a9d | -7.75549 | -43.8066 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 33488fad-f830-3c5e-bc51-2dc1e031ccc8 | -3.92613 | -40.39034 | 2026-10-07 16:37:00 | NPP-375 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3f2e570c-da56-3048-b874-fbc26b5ba88d | -6.46435 | -55.44477 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b17b1a06-f499-3738-b3ab-440e6fefeb60 | -4.63997 | -40.58094 | 2026-10-07 16:37:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 38d028d8-2270-3d1f-bffb-2598c3e1a3c0 | -9.25226 | -45.6429 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0302ef54-ed43-3d30-97bc-fc15d00b7e9e | -6.87678 | -43.6764 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7bad3e18-a797-31fe-897c-db0b2ed29a6b | -5.89664 | -44.03485 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fb648d27-bb0c-3208-b930-39682fdda11f | -7.8379 | -45.50065 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| df9a27df-534b-309c-b0e6-aea066bdab19 | -16.05822 | -39.8654 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| b9b95276-ad79-32c8-b3fa-f7ec0531807b | -15.96657 | -40.7046 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| cc88f743-a9a6-33df-aa30-f196097c0167 | -7.8729 | -54.99478 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b2e1794e-bbf9-39ec-9bbf-b7a5c00fe331 | -4.24056 | -49.98371 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 1c8ed157-8658-3989-b981-ab2b864895f3 | -15.00374 | -39.73711 | 2026-10-07 16:37:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 77e877a0-6c5c-3b3b-a75c-fae278cd26d1 | -7.34732 | -55.01538 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d50a1acb-5ec7-3712-9cf5-d72e48ddcd7b | -3.48476 | -41.51011 | 2026-10-07 16:37:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d9b3b0ec-976c-30a1-adaa-a55642c92079 | -10.1997 | -46.69807 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f3a75400-0a51-31d2-bacc-34710ab6cc0d | -6.84675 | -41.79686 | 2026-10-07 16:37:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| beae297e-75b1-33d8-b6f2-7522382357bf | -4.70591 | -49.68943 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04c0d481-41d6-3a85-80ec-6a455d4cb54d | -5.96695 | -40.93494 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| f7a58087-ff64-3acd-86a1-6bfa59f558e6 | -5.72597 | -45.1551 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d3724d52-b5a0-3829-8cda-9fb150b5a322 | -16.19894 | -41.58126 | 2026-10-07 16:37:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 305d48ac-71d3-3de0-bd48-54d4c10f6891 | -6.80534 | -55.30083 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0a15622b-844a-38ba-9030-49f96f76f68c | -4.76279 | -42.59322 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 42012b7d-2fdf-3779-838e-638cc5738328 | -3.20229 | -42.95419 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 33e1d2cf-c776-33f8-9c88-dbbe976193b5 | -3.47944 | -44.76484 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0779e5d-d078-3827-a7c0-68a21d7ecc6f | -5.73738 | -41.71676 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |


[Clique aqui para ver as próximas entradas](README188.md)
