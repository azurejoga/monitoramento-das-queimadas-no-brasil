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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cc9f19d-fb04-375b-a326-a44188a043d4 | -12.53685 | -49.60299 | 2025-10-25 04:19:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e681877-3c11-309d-ba5d-d1465831f448 | -7.33495 | -46.14418 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b0dbfa5-5b56-38a9-af6d-190099d8a48f | -10.41774 | -44.50064 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b2a0a44-1755-3e7f-9751-28ed4fed495a | -7.85094 | -46.43393 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f4ce438-1376-375d-a9f1-d1cab5fdfd13 | -10.63967 | -45.23204 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1b0769f-f22d-3d4a-84cf-06ffd1603eb7 | -7.93444 | -43.21051 | 2025-10-25 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc9c36a9-981a-3f30-aee7-c9ed3340789a | -8.31528 | -47.8633 | 2025-10-25 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c802af5-c588-3d7f-b7b8-c4577ed9d07b | 1.63339 | -55.75584 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f29deeac-ae2e-3b2a-b072-051694cb2f25 | -8.13787 | -47.04194 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21ee7b86-60a3-3963-a737-c80dd947ee77 | -9.24083 | -45.61425 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a1f848b-5b0d-31ea-8df9-6a12c26224fa | -12.55922 | -48.55722 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdea003e-f1bf-3cc4-a509-f94e61356297 | -8.86734 | -48.29139 | 2025-10-25 04:19:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92bea138-32f6-3b54-b6f8-68c88f4c6a0b | -12.57583 | -47.34713 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a02720c2-2a07-3330-901a-4e8191bfd0a5 | -12.0615 | -46.44451 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3208cd4b-7e30-36f2-b620-9a8b790f6d10 | 0.35975 | -50.92598 | 2025-10-25 04:19:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9981f078-5d49-379e-8c15-b18f66cf5b49 | -10.68989 | -48.08499 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8329196a-2217-3a3d-9052-1305ea96b45a | -7.40843 | -46.60722 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a629bfb-47a8-343b-82aa-b0ee866614c6 | -12.80392 | -48.67622 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5e9360f-c1fb-37a7-8893-98813df570f3 | -7.63961 | -42.16875 | 2025-10-25 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 77d2824b-fbcd-31d1-9ff7-5a563eaf1bba | -12.0837 | -46.4119 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb55b382-0b81-30e2-b2b6-65063609bee0 | -6.83471 | -44.78073 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17c877e6-ab8c-326d-aa2b-2d1c37b7655c | -9.49119 | -47.45732 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c23c853d-2f9d-3e15-9981-77adb655e560 | -12.0886 | -46.42381 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6c1d668-d586-3a54-bb83-ab122a7dc4a3 | -9.92471 | -47.99869 | 2025-10-25 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e12c47e-2074-39c4-83b7-c2a895f80e86 | -11.84849 | -49.86139 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6593b17-b6b2-3df0-b6c0-55f444b20681 | -12.06246 | -43.98907 | 2025-10-25 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cd789ab-8811-32ac-aaf5-99351f77a258 | -7.03173 | -43.93783 | 2025-10-25 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e588d69-97d4-3484-88c3-8bbcea733951 | -12.24795 | -47.44287 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 872a2001-c082-36c4-a60d-e4a0ae890d7d | -7.15908 | -46.09013 | 2025-10-25 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4e536ea-39d9-34a1-94d8-29a50a9606f0 | -9.32566 | -45.1855 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a121781f-0f29-3845-b76b-d6c6ddbdd50b | -10.91017 | -47.89594 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f52d8ab6-f663-3a1a-979b-668f54b326b4 | -13.04357 | -47.20855 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ace15970-da51-35c1-9acc-390452154521 | -6.91607 | -42.2443 | 2025-10-25 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77bcb364-37cd-32c2-b625-8836d998bee1 | -12.85486 | -48.54892 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28666f19-539b-324d-82b0-7f39959c4a1b | -10.46618 | -44.29213 | 2025-10-25 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b3db37c-e374-3fea-bc46-da58c1db109f | -13.34614 | -48.79863 | 2025-10-25 04:19:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43c9db16-7b93-3ea4-a440-8f24f80d5d1e | -10.55341 | -49.77399 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4cd8a66-d697-31ec-8269-37bb768a6a9c | -10.88458 | -47.22208 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1a239c2-8d59-3504-9947-81b9ec2c7116 | -10.82394 | -47.99749 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bf11322-9637-32f2-b93e-956732be684f | -6.80943 | -45.43164 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f686160-9c1e-3ff8-897b-6a55bf448d26 | -13.62412 | -47.61159 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 983681f9-f334-3407-b32c-9bed8597f7e0 | -12.36425 | -48.12275 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bc18c6f-65d6-341f-bfbe-891537b3389d | -9.95604 | -48.26657 | 2025-10-25 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7860ff2-47c3-39e1-9051-8f202874ca05 | -8.71584 | -49.60775 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc0c5ea7-f973-38f7-b104-926c430fb3a7 | -12.79471 | -48.66642 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 669dd5bb-4eed-345a-a86a-6738c82e845b | -6.85248 | -46.2895 | 2025-10-25 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd43dfed-1aff-389c-a4db-03206ead6f96 | -8.71875 | -48.01028 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80dfb65e-796f-38a9-ab28-e99044ce0a15 | -10.51788 | -44.17863 | 2025-10-25 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1251c11-e166-3cbd-a7eb-4b55b615c3e9 | -13.34603 | -47.41139 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 863476c8-b5a6-3ffe-9be1-10247ffce110 | -6.60055 | -48.76652 | 2025-10-25 04:19:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03db97b4-50d4-30e6-891e-c06a5c6d5aad | -10.56502 | -47.98748 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab12f449-2210-3aa2-bd91-92c27c2b02a3 | -11.32525 | -53.93066 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63154826-c2c9-37fb-94a6-a5b74c6e9fc1 | -12.25591 | -47.44371 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be010872-e7f1-3bd1-ad7d-573036b4a620 | -6.41669 | -46.18657 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6eef05e-4887-335d-a271-8abb6a36bb37 | -6.88794 | -43.6167 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 268740fe-ff0d-3c61-91cb-092f7c349d2e | -13.31302 | -46.77854 | 2025-10-25 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d2b9559-5952-3d16-8bac-458ea050e163 | -9.60887 | -46.90442 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b292989-a173-31e8-be09-05803db73df4 | -10.63596 | -48.06333 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e56cfbca-3737-3fd2-a0ea-754cd0ebe785 | -7.94323 | -47.19786 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9160df38-9726-3676-8b8b-8756924dc085 | -13.33933 | -47.91713 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec5dcdc0-c979-3492-8caa-cdc1ce0bfa34 | -13.28512 | -47.49869 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12204cae-b738-3c15-9c3c-8766ebca54fc | -12.07157 | -46.40265 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa76d4e4-c4b3-3833-8a9f-9d00b7c42156 | -7.65153 | -44.57766 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7906042e-2e06-33c5-b97c-72969b68038a | -13.35491 | -47.42032 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba9f488a-6572-379e-9fa4-623428e9e8cc | -12.19817 | -43.46103 | 2025-10-25 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0cc758-8b69-394e-9ffd-20180a25f4dc | -6.80999 | -45.42813 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d1f143-8443-3e33-b608-853b9de2116c | -6.92677 | -45.1647 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 726bcb6a-b743-34f3-9918-3f839937da0d | -8.55241 | -50.04205 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54ee9515-7f6c-3c17-9bcd-fb63f1bae913 | -12.8305 | -48.67183 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 770d6e11-2da4-3cc8-8f3e-444ff104e120 | -9.60429 | -44.62206 | 2025-10-25 04:19:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fab24c34-c8f2-3ff1-a84f-1c9931d2db4c | -12.22803 | -46.50791 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84809a26-2a4f-3e19-88fa-46797b12ea4c | -8.4301 | -42.46393 | 2025-10-25 04:19:00 | NOAA-20 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a0cd7e4-53cc-3fc2-b151-f98529daaa92 | -11.62679 | -48.53759 | 2025-10-25 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30bbc293-2f2d-3ee9-9e37-3f21ff89948f | -13.29893 | -47.45627 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da6e52d0-a963-3d94-bb9e-211112110f7e | -12.08039 | -46.41134 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1780cb5-b1a3-37b6-ad0b-6499e637563e | -10.27331 | -43.8736 | 2025-10-25 04:19:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afeff574-7ae7-384a-9796-9ca8a42879f1 | -12.1649 | -47.00626 | 2025-10-25 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ff2c07e-8836-3894-aa50-61fe34a662d0 | -8.46482 | -45.55736 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 324cea81-1bd8-309c-a1c2-a8b899a7a0e3 | -12.08095 | -46.40782 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b00084f9-8ed5-351a-bf41-ed0f0da0d921 | -7.49039 | -47.03277 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c361ea79-818b-3944-b0cc-0df4a8e66cec | 1.6393 | -55.75494 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b615596-7811-3bd3-9c24-305ae385c372 | -5.72368 | -49.09834 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9c2719af-ee7a-339a-8765-2a8e14fa8be0 | -8.55726 | -49.85822 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb44ea36-ee20-3088-a43d-fb17f3a3ba6a | -8.13382 | -47.04514 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04bf192d-15be-3801-b99d-4df036eba8d6 | -11.5694 | -51.47537 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8ec30a8-9dca-381c-8b28-5f85ecaf7d5b | -9.51718 | -47.72304 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2901e5f-0337-3b33-ad1e-d4eba7e9887e | -11.00828 | -50.30617 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bca6b276-5920-34e6-b53d-4049c9a23559 | -7.36133 | -45.01729 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e932c64d-d379-365f-ad5c-053662c05e0b | -12.83326 | -48.6342 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 914a4a05-6d9b-3a1d-a4bc-803df498a898 | -12.57642 | -47.34348 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3b3195e-e98a-36b0-a908-acf50ee18783 | -12.94592 | -48.50533 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b455505f-27a5-3b65-ba7a-8232b61b05cd | -9.74887 | -47.83322 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9159e3d6-438b-324f-8df4-3d2e2232ead9 | -9.32126 | -46.97151 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d33a0042-1c90-36e7-9e51-2ead611f9d75 | -12.08314 | -46.41544 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe9f48e9-5eb9-3995-994b-648730d10c29 | -10.23298 | -52.13429 | 2025-10-25 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8f71ed9-c664-36cf-87d1-00f22f883638 | -12.24076 | -47.48737 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 197ae44e-1827-3c4b-a0e9-8a536eb7be46 | -13.32441 | -47.96552 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eec0a8ca-83db-359b-9e5b-29bea3f04f00 | -10.69055 | -48.08104 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34bd23d3-5e77-3589-a4a8-203930c4004d | -10.42451 | -48.00472 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7687139b-9887-3af9-b2f2-18bbf3e01e46 | -9.9603 | -48.26296 | 2025-10-25 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
