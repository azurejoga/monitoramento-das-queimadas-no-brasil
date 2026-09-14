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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77c3d0d1-40a4-3f3b-a597-6d46c2767162 | -14.84717 | -48.14757 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3d7992c-716e-3b40-8891-2c0f45bea798 | -15.08288 | -48.33069 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00a9e8a0-3edb-318b-abae-06b186a19323 | -10.67272 | -54.14084 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f28c4147-fc3a-3517-b5e5-f1f14934299a | -10.54414 | -51.30327 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8af42c71-f1e7-330c-91a6-d13a3df55d8f | -10.53888 | -46.28351 | 2026-09-14 04:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28e36c3b-e503-3dd1-9e9f-81e5a8f6fe73 | -10.67513 | -54.14479 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbfae707-b358-37d0-a7a6-ad0dc3b56a0a | -10.54279 | -51.31111 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f848035b-d3e8-37b6-8c0d-71924d72cec0 | -13.58815 | -47.89766 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c4b0dda-a9d3-32d8-8ff5-56882b72f236 | -10.10387 | -48.85903 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9ff1125-0cdc-3046-b25b-fdf40712c960 | -15.50476 | -47.91154 | 2026-09-14 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4bf86d6-5017-307c-a6d1-28dc2c940692 | -10.66947 | -54.15858 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 177f1d67-5265-3ad8-901a-b0d533e30d3a | -15.06147 | -48.56377 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6da8afcc-6ad2-3b26-bde4-949fed25cca8 | -9.98255 | -50.27024 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3649f4be-7903-3cb5-9e1f-d49593f0af50 | -10.54854 | -51.30309 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45989b82-290e-314d-86f7-bcd263de0a89 | -15.56097 | -48.79415 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b6cfedc1-108c-3845-a579-1691544542a5 | -10.64373 | -50.58117 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 46a5e9e3-4eb4-3b42-8855-f58e4b026f34 | -10.68354 | -54.16742 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0a6474cb-d8cc-386e-ac55-240f03a2a0bf | -13.56734 | -51.46077 | 2026-09-14 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c153f90c-f1f5-3184-ac5c-22135128c366 | -10.58411 | -51.34594 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef5876f-6213-3593-9eb3-2e75934dc32e | -13.56135 | -49.9044 | 2026-09-14 04:34:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 976261c8-d785-30e8-aeca-29f8e29276cc | -14.17818 | -47.39141 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29171d25-19e7-3359-ac91-b92533359531 | -10.17733 | -48.06301 | 2026-09-14 04:34:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec02c4b6-19ee-39a0-be5d-f3a1f7abdd17 | -10.24107 | -50.90826 | 2026-09-14 04:34:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dac24ed4-2044-34ec-a638-47e1bd10946b | -14.18487 | -47.39255 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5b83352b-6b95-3704-bdb8-28a6a7a9037f | -10.10872 | -48.87133 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0532d523-6265-35ed-b493-15e53782bb7c | -13.77676 | -48.80834 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ded8ed06-45e7-3d21-8a08-49b55ff639dc | -13.58537 | -47.8934 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9e210bd-4c46-3ee5-8eaf-6ffad2b65c19 | -13.7781 | -48.80032 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf3b0c01-86dd-3984-b766-7ea8ef0eecdf | -11.8064 | -46.58943 | 2026-09-14 04:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8eaf49ec-113c-30cd-a2bc-abc4e71a18e2 | -10.68129 | -54.13988 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c4dbf91-a072-3aac-b792-0610180374b4 | -13.78024 | -48.80906 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8dba1ee-7b6d-30cb-9490-a121147680dd | -13.62706 | -47.89664 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c178e037-01da-3478-a69d-31dc986403a7 | -12.09779 | -47.31313 | 2026-09-14 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b8852d-5c82-3221-a3d5-6eebc7cefda9 | -10.66103 | -54.14759 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9a3368f0-adea-314e-b2dd-32f93d1d3a08 | -15.44812 | -44.84175 | 2026-09-14 04:34:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1d150b08-6881-375e-b7ba-8f8bee25e06e | -9.68836 | -54.84169 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2446f783-4cac-3c14-92e8-010b0ff3d893 | -14.82742 | -48.14056 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7b41dec-cff5-3df1-b795-7e6ec6c2b1b0 | -12.85173 | -44.387 | 2026-09-14 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b3a88de-be40-3928-bfb6-6414177e0a51 | -15.56439 | -48.7948 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b312013f-3974-3abe-8c9d-2414ee1af733 | -11.18099 | -42.80918 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3b25647e-6dfa-3778-aa0a-1dfa2a7244eb | -13.59579 | -47.87239 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a84c248b-3068-3eaa-b9c2-588b56331ae9 | -16.36916 | -46.5482 | 2026-09-14 04:34:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82611346-c2c9-351c-bee2-1cdf8c6c46b8 | -15.26668 | -42.79588 | 2026-09-14 04:34:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 967e5a6d-bce6-3535-aa7b-7f95e7c9a8e2 | -10.67163 | -54.14676 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c4fa6bf2-6d25-366e-8d98-336510c9588b | -13.62768 | -47.89293 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccbdc41a-a98b-3b0e-b016-337889fb7816 | -13.59179 | -47.8755 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0fa88eb-ad69-3373-9a1b-dc6fd8b845b4 | -10.63906 | -45.99968 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b47ed0f-7b37-3f2b-9808-48e61a0fd35a | -11.33846 | -46.78295 | 2026-09-14 04:34:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa97a19-7f6a-37ad-b1d0-0d62ecc23c12 | -10.58064 | -51.34109 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0abfa546-3215-3a64-bb0f-f9e21258a5cf | -12.15743 | -48.95919 | 2026-09-14 04:34:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4fba73b-c73d-399a-8713-35f0eac3fcf9 | -10.69082 | -54.17228 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c84ca0-8fc8-36d2-adf9-266d27633719 | -10.58194 | -51.33376 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92b2468a-943e-3d5a-b263-14549c4fc5dc | -10.67847 | -54.1665 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 439713f7-9924-3347-9117-161def72ef40 | -11.2265 | -46.4319 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db524ca4-7c91-331a-814e-d1e9e699ad26 | -14.91259 | -44.67064 | 2026-09-14 04:34:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d18df69-3b46-3c54-a555-37ece1101f21 | -10.68623 | -54.15261 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 68fda932-d9a3-3225-821f-705fefe3df81 | -10.67232 | -54.15952 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 98d2d981-4e92-319e-8c3c-abcac0ab7f74 | -10.64154 | -50.57005 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16301f1a-e7b1-399d-9434-a23eb16beec8 | -10.10732 | -48.85764 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92169084-a92d-3264-b7cb-90bf73fd27cc | -13.46557 | -48.46723 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9910ab91-b0f1-3354-a21a-545eaaffafd2 | -10.66769 | -54.13979 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 7b381f1a-96ba-3002-a1f6-64b499936fe6 | -13.56212 | -49.9 | 2026-09-14 04:34:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64e48916-2aff-3c57-9e36-ab16a8d0049b | -10.68462 | -54.16145 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2cdb52c3-64c2-33be-b1be-b993b18bd0b9 | -15.04476 | -48.53735 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2470b3d0-a7e4-3bc2-b643-8cbf7734e03d | -11.18879 | -42.80613 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| abd57566-33b6-38c9-b3f2-377fd0d73730 | -15.78254 | -42.15531 | 2026-09-14 04:34:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cd88d35-071b-3205-82e8-84fbbd4df620 | -9.68771 | -54.84521 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e4a9d00-f5b0-33dc-bdfc-60c9ff9858c0 | -11.3418 | -46.78352 | 2026-09-14 04:34:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b0a8a52-4e5f-3542-adf3-3e0987dcdc0b | -10.68064 | -54.15464 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f77787cd-e194-3cd0-afab-4387a8231f9c | -13.78785 | -48.80652 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6680296-543f-39a8-9b40-007cc40f2acd | -11.29332 | -47.67672 | 2026-09-14 04:34:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19adc18b-cb99-3b9a-a747-0c60526b65fb | -12.68523 | -54.66656 | 2026-09-14 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20db136d-fcf9-3837-bfb5-3835813584c9 | -10.65708 | -54.14066 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7a14083a-46f5-3f15-b842-5c69900ddb01 | -10.47113 | -51.32525 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06ea5f56-6d19-33f4-b0b2-7f3ed92920cc | -11.59828 | -46.7707 | 2026-09-14 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 409096ef-ee17-384f-850f-39fdc83ea405 | -11.25512 | -54.12647 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d7ba741-193e-3be1-84a0-3af1cdce1400 | -10.65546 | -54.14946 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5fff1b6-2deb-37b3-a9d8-4bdb13dd976d | -10.68299 | -54.15843 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84a08941-3b0b-3cf7-a941-96f8c0f7ffeb | -15.54654 | -48.79579 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a579978-f9bf-3883-ae09-0a54a7d1de7f | -13.29766 | -51.31464 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dfd8554-7830-3e85-b6f8-939ba07dc865 | -13.5533 | -42.4104 | 2026-09-14 04:34:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fe18aa7-1436-386a-8555-95c864dceefc | -10.65763 | -54.1377 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7feef6dc-883a-3a53-b434-448c9dbcd29f | -10.54059 | -51.2989 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81533cdc-0aba-33c4-9ef2-fbbbb60e019b | -10.64462 | -50.57597 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45a9d854-e095-3a1d-b4bb-a67c84cb33a7 | -12.09839 | -47.3095 | 2026-09-14 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1591fbe0-07b1-3316-b481-3e26be246ca5 | -10.6852 | -54.1468 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b686b3e9-1123-3af4-b345-6c304e2c28eb | -10.10947 | -48.86694 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3676215c-6a8d-35ff-9abd-758e21683812 | -16.48154 | -43.42435 | 2026-09-14 04:34:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a2419a2-207f-3c55-a85e-0c473497f1ed | -13.78223 | -48.79708 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79b54e9a-0f23-3181-bb33-629bd2b02641 | -14.17391 | -47.43885 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 308f4270-7fd1-34fd-b8c1-9869b37ecd1b | -9.9865 | -50.27094 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9393b36-2997-3003-8669-b30e5916d967 | -10.51708 | -51.35952 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 008e0e92-8bf5-3a6a-bfdc-f412987fec8c | -15.26695 | -42.79319 | 2026-09-14 04:34:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e59057e1-30e9-36eb-8573-29e73286f55b | -10.68521 | -54.17427 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd34955f-5ff2-3a1b-89cf-26c290e70bd1 | -15.08628 | -48.33131 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04a0b63f-7636-3be5-a727-24547980f99b | -13.45803 | -48.46978 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1151549-64e0-3754-8a5c-9c1690d73009 | -11.59713 | -46.77782 | 2026-09-14 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd176b71-7e13-3cbd-b82b-e13f5c0c1aae | -10.68224 | -54.14589 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7b5784c-7a09-3238-8520-6ccd1526669d | -14.17347 | -47.42035 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa483c22-f6d8-3c7e-a72a-944f52d26146 | -10.68464 | -54.17728 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README30.md)
