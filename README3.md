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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f84895b4-2013-38ca-8cce-8a7b35d338e6 | -14.59622 | -47.97158 | 2026-04-24 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01ff6324-5f15-3462-9eae-2340eaf2ace6 | -18.27335 | -52.91049 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc98146c-fec8-3381-a72d-95845dfd88cb | -18.2655 | -52.89353 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a913020-71fe-38d3-a444-b4e351d0e31a | -16.42356 | -54.92049 | 2026-04-24 04:12:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d00ae81c-5768-3956-9da4-3cb4a21b3732 | -18.27766 | -52.91412 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e4a2b99-84e3-33d9-824e-22c2ab523aa6 | -18.2733 | -52.88363 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28643a8f-00a5-3a13-89c5-72afd9a1ae00 | -18.29386 | -52.94502 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4943760a-411f-31bf-bb35-bce06cefb400 | -18.8615 | -41.98066 | 2026-04-24 04:12:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b58e9df-5be2-394b-89d4-62c55b23edd8 | -18.27802 | -52.91543 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a500a50-e14d-302c-998b-e72efc94d73e | -18.27686 | -52.91782 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b2b27a1-5c00-357b-9784-bfb95df224f7 | -19.80011 | -44.63703 | 2026-04-24 04:12:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e376425e-d647-3ab6-bbc0-9fda6bc115f6 | -17.48118 | -51.08844 | 2026-04-24 04:12:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb408944-86b0-369d-bf02-e0a88604e6e4 | -16.00521 | -41.67899 | 2026-04-24 04:12:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d0c8ff1-1774-3643-982e-e731f5a03d95 | -18.26706 | -52.88617 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3edb3600-0797-3ba4-b2cf-372c9972071d | -14.74758 | -42.46284 | 2026-04-24 04:12:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c60950c-56b9-3390-8ea8-30d2fb0a6829 | -19.96224 | -44.68999 | 2026-04-24 04:12:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f251f75-32b6-3149-95bc-edb8c5b22622 | -17.53106 | -44.75377 | 2026-04-24 04:12:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b635358e-244a-3a52-8c48-c07253fe0128 | -13.54744 | -47.88982 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d3274c1-d107-3d54-b89a-fc4eb391fc78 | -13.53708 | -47.88972 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5bc49f0-209c-3b43-b74a-8b7a20a92ddf | -16.70531 | -44.95718 | 2026-04-24 04:12:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df390d1b-fc45-3f67-9187-0b0f7c278f43 | -19.09715 | -56.06708 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c5d3079a-1662-3af3-bbc2-417fd42192fb | -21.69679 | -48.43767 | 2026-04-24 04:14:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 487b42d7-ea28-39c7-8329-6cc3b8a94b59 | -20.19777 | -46.92363 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aad89e8-e43e-343a-b0f4-ee67129f7474 | -20.20442 | -46.88616 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ced337a8-7cca-3ac7-afdd-8b919f5808f0 | -20.15666 | -46.85684 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cc2ffbd-f6ec-338b-ac43-009ac0cc0d0b | -25.65063 | -50.12516 | 2026-04-24 04:14:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52e7e96c-936c-3d96-90a7-a6d2007ddc06 | -20.2101 | -46.81163 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e842b59b-9174-345e-8339-1b11033b1ef2 | -22.74538 | -43.46149 | 2026-04-24 04:14:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b014d7d-af1f-39fb-b1a0-32513057cfc8 | -19.44501 | -56.62165 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fa3c6c63-73bd-3868-bd79-e560bf987d62 | -20.19335 | -46.9271 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfb34f10-1991-33df-bd28-abb8ef785997 | -20.675 | -48.96511 | 2026-04-24 04:14:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 496c8f57-9801-3acf-a38e-a47c58be8a03 | -20.16026 | -46.85788 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7372838d-3647-3302-9512-22546246378c | -20.17168 | -46.79443 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3db2079f-5bf2-388a-94b9-8c0fbfef268a | -20.19081 | -46.7298 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aba1801c-94cf-3fe9-b43f-162599141060 | -20.18721 | -46.7289 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b1ad9a5-f8fc-33b5-bc46-055c04025a91 | -20.16387 | -46.85886 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce0a7109-7127-35ae-aefd-082e56437b0f | -22.93267 | -48.80629 | 2026-04-24 04:14:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a36cb556-6d42-38be-b6ff-e092e9a8cd12 | -21.58768 | -41.93182 | 2026-04-24 04:14:00 | NPP-375D | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b488923b-4317-3e7d-a591-c618c5ae0db0 | -20.23481 | -46.75728 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7a8b2be-a873-3c3d-b1dd-2e6ee2d4e8f1 | -23.54009 | -47.63061 | 2026-04-24 04:14:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c151499-4886-3231-a811-3dde2d5bff16 | -19.45158 | -56.62345 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9e860108-dfbe-30ca-a811-8392df8e5e49 | -20.18904 | -46.88745 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4479209-a479-37e2-b699-3d74fac171b2 | -22.93314 | -48.80463 | 2026-04-24 04:14:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68455f15-9ede-3975-9dfd-6ed6fe5cfb8f | -21.69725 | -48.43593 | 2026-04-24 04:14:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14f85b60-ac9e-3e41-b676-772d831dae28 | -19.09728 | -56.06092 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 27a6b4a8-f8de-3bf1-b461-b19908f48d3c | -20.19441 | -46.7307 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9083f23a-b25e-3cc9-b414-0cef804b2208 | -21.20234 | -44.20799 | 2026-04-24 04:14:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7cc32d88-9677-3c90-8896-03341aae7552 | -20.23842 | -46.75818 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6238f18c-358d-3631-a004-84da69a41a33 | -20.19798 | -46.8798 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd74bf9e-145b-3920-886b-cf55deadf721 | -20.17085 | -46.79903 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73d40d20-ec45-3a21-9d0c-6f743b1664fd | -21.69822 | -48.43069 | 2026-04-24 04:14:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 508f43c7-322c-37ab-9d3a-ccc87c2357d1 | -26.79948 | -50.40484 | 2026-04-24 04:14:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3acbe356-7c29-3d2c-9c8f-f5fc9d25fff7 | -20.20648 | -46.8108 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 177a7a5f-bcb7-3195-b025-0dec7485b65b | -20.20159 | -46.88078 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce07ee2d-5374-3f69-a540-08cd0402e172 | -20.24978 | -46.77672 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fd6e12a-27de-36a4-b9d0-975616646ade | -20.20727 | -46.80637 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fcd056a-3f48-3768-9555-3c674780cac8 | -21.20568 | -44.2086 | 2026-04-24 04:14:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ddec880-1de0-3e7f-bc54-50f7ace1bb8d | -20.16224 | -46.86791 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1fc5e030-3c41-3a62-8244-2c614b95d4ff | -22.55246 | -42.2106 | 2026-04-24 04:14:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4facb6d0-1766-3811-9728-6280e1d7fb70 | -20.1941 | -46.75348 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34c727ff-c357-3a4e-a2c0-14795bcb16ab | -22.96785 | -52.69527 | 2026-04-24 04:14:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f661f366-40f4-3add-9dce-6e22e195df9e | -22.93772 | -47.16653 | 2026-04-24 04:14:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 367772ee-41b8-3fc0-b9db-e579cb652b6d | -20.18814 | -46.7657 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55efa404-adcd-3a03-84fd-e072fdb16b6d | -25.6546 | -50.12623 | 2026-04-24 04:14:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e6b02f9e-822d-343d-9e73-878d63955bbd | -21.21783 | -48.61271 | 2026-04-24 04:14:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2846f225-3261-32f8-a3d7-7595b161c9f5 | -22.94051 | -47.17167 | 2026-04-24 04:14:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ae4131d4-adcd-3151-a399-e21a750dfbcd | -20.20806 | -46.8019 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6704822-d168-339d-9046-ae49d1e9821d | -20.21091 | -46.80706 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9e3bfaf-f57a-3726-96ea-815fc6b8f5db | -25.65534 | -50.12247 | 2026-04-24 04:14:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3e73210c-a3af-346e-905e-2c460260dc84 | -20.24709 | -46.77298 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7bab65b-5e8c-3b99-b775-4898b1b20071 | -22.83749 | -49.29721 | 2026-04-24 04:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 783cbf44-646d-31a0-a3de-e4194b042956 | -19.09846 | -56.06141 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4669ae1b-6535-39e1-86b6-4ee5b6230205 | -23.03866 | -48.43747 | 2026-04-24 04:14:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda157f7-51af-340a-9677-53ad7bce2ec5 | -20.67573 | -48.96126 | 2026-04-24 04:14:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de371328-f387-3e9b-925a-5f77c0c3c73e | -21.58657 | -41.93457 | 2026-04-24 04:14:00 | NPP-375D | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7149f04c-4a81-3013-9a44-00c3561c20dd | -19.45303 | -56.61737 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5c3c2348-add0-33ee-aecf-7ca5617a785d | -21.45192 | -48.47816 | 2026-04-24 04:14:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83ca0a6e-7b74-31b4-bd72-f7d7258d0b40 | -20.19769 | -46.75443 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f2ed70d1-f778-3aa9-b8e9-6f41a96230e1 | -21.65939 | -41.32624 | 2026-04-24 04:14:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1dd2f95b-6753-32ee-9705-cd57200f550a | -20.2507 | -46.77384 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f36ce5b9-6440-37ce-877f-a766f15a4e3e | -20.21291 | -46.81709 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50c23a03-5a37-3a2f-ac40-c4535f0d3ba7 | -21.85401 | -46.98307 | 2026-04-24 04:14:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 359019f2-d949-36e0-bbb2-fc4a06c61080 | -20.17723 | -46.80554 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e36edc-849a-32c5-b242-df93e905034e | -20.21373 | -46.81246 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 168932f1-c4db-3885-bbaa-9a2d9de06393 | -20.91625 | -40.8217 | 2026-04-24 04:14:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 18785223-021d-3059-9e03-0e6c567a3790 | -20.24346 | -46.77218 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c04a3d3f-21ff-393c-8f60-105523c81a08 | -21.69877 | -48.42726 | 2026-04-24 04:14:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3be4788-b40a-396b-abf9-bf78d8c960c5 | -19.09593 | -56.06657 | 2026-04-24 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2028c4c6-476d-394e-b103-0e6059e2f186 | -20.22966 | -46.76515 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08b4b9b6-8911-3598-8614-90f57e17b7e1 | -20.24205 | -46.75892 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0219dad2-ae9b-306e-b471-b78f82b4b469 | -26.74448 | -51.21901 | 2026-04-24 04:14:00 | NPP-375D | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d6eec8a-66d9-37bb-8c6b-16193652aaa4 | -20.16306 | -46.86335 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdf433bc-5c39-3144-b6ab-1843b90b6fad | -20.17361 | -46.93129 | 2026-04-24 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dd00874-080b-3383-aee7-9e1363b915b4 | -20.18538 | -46.88669 | 2026-04-24 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe8be63e-ec41-363b-8541-d8653c5383d2 | -27.49799 | -51.40052 | 2026-04-24 04:17:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e3552e60-54e1-3c7b-bdcc-81dcdf621b36 | -27.49885 | -51.39631 | 2026-04-24 04:17:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f04d004a-ca56-38dc-979b-b9bb1732f3fa | -27.94806 | -51.06168 | 2026-04-24 04:17:00 | NPP-375D | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f071aa9-4a8b-3ced-be2b-aef7e6dc82bc | -11.57029 | -54.56298 | 2026-04-24 04:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e8cb9e-81da-3883-ba12-ad13d99a8a40 | -12.54859 | -54.61067 | 2026-04-24 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d453c0-8982-316e-999e-205a1b5334b1 | -12.98425 | -54.68098 | 2026-04-24 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README4.md)
