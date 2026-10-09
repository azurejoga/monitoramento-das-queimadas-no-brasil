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

## Dados Diários - Página 264

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 080b906b-6694-33ec-9fef-681ba28a3395 | -11.58497 | -43.63833 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 2bdc31ed-a905-3f50-96e3-10d775e67444 | -15.10776 | -43.84018 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ce93aa3e-72a1-3a8f-9c06-4c441b6acd59 | -12.3728 | -46.56881 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2920aef0-4a46-3634-84cf-0e702ee45b82 | -11.77872 | -46.80141 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4c257d29-7744-314c-97c2-0c17a87ab549 | -14.60022 | -41.28196 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ca0bf951-c9b9-30a3-b5a0-ebfe437a5dfc | -12.22133 | -44.64127 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 94728a84-b208-3c7a-9c16-1d92e15d26d9 | -12.12897 | -43.31495 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d444deea-d8dc-36bd-9c60-cbd0ae6fb342 | -14.60058 | -41.28507 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3ff8396f-85de-3224-9013-7ded25e07e66 | -10.89584 | -41.2963 | 2026-10-09 15:58:00 | NPP-375 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| dbdc7ed7-88ca-3978-b3cf-025a21858065 | -11.97289 | -43.48989 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 55e43c56-602e-3462-8f43-bf700ceb8a4a | -14.49639 | -40.82902 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8608cc40-c08d-3fcc-a06a-b19a7fea169e | -11.5878 | -43.65823 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| ae7b1245-63a0-3d20-817c-f2dd5a071204 | -16.24443 | -44.06425 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 61dae613-55be-3421-9462-2773af8633a4 | -15.90807 | -38.95669 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bccb6f97-2fcf-360b-82fe-ae5bc0af10d6 | -12.23683 | -38.99432 | 2026-10-09 15:58:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 32f8862a-c0e2-34d5-bd30-693607fc4dbc | -15.37626 | -41.89544 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| bde0d2af-4cea-32a1-9c09-bba00c16850a | -12.23198 | -44.78101 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 1bc22f1a-dcd7-3915-9355-608cb639cc2e | -15.22748 | -41.10476 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| eabb2d53-6c9e-3d63-bb39-7101ac788d5a | -11.98537 | -43.48889 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c80d1592-1bca-3153-a7c0-398b14aacb20 | -13.7508 | -43.47021 | 2026-10-09 15:58:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bf0a633-29c1-3e62-9e71-39d8b1a7b945 | -16.82531 | -42.3002 | 2026-10-09 15:58:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 56e1e839-e551-3cee-beaf-bc17c4690004 | -15.00581 | -46.25502 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0eb30834-2504-3f93-856f-89f3f98c19cc | -11.96938 | -43.46105 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 159e58b0-613d-3779-a2e3-f81576b978c9 | -11.59792 | -43.64493 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 2ef4f9fc-901c-3b1e-b315-f258ed1462b2 | -12.35774 | -40.308 | 2026-10-09 15:58:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 37dd8dc6-c73d-353f-9a3c-7913909a8143 | -11.59841 | -43.69958 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| c83ddaa2-9355-350f-b43a-142a4adf85ff | -11.7441 | -43.63765 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 21640e9b-ba10-392b-8ecd-c062b0e0204d | -15.99017 | -44.86443 | 2026-10-09 15:58:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 60450f45-fb1a-3b4c-987c-7227f7587133 | -11.99368 | -43.46048 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e00cad4f-5727-39d3-a059-4e7caf0fc901 | -16.67613 | -43.74758 | 2026-10-09 15:58:00 | NPP-375 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f8b8e06-93e7-35b4-bc23-5c0eef55c8fa | -11.97577 | -43.46594 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 90b05338-7e41-382f-9f8a-abf86aeca746 | -11.77049 | -44.95482 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4947ed22-8528-326f-8022-db8be252a62a | -11.90113 | -47.3926 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 0e81287d-198e-3249-a54a-d11148e8c78b | -11.15197 | -41.83943 | 2026-10-09 15:58:00 | NPP-375 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b470976f-4f9f-3119-89ed-b3da731c12ca | -15.36551 | -44.83743 | 2026-10-09 15:58:00 | NPP-375 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 52d382ba-59e5-3f19-95b5-39bcc076c662 | -11.60178 | -43.62822 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f2f362dd-bbb1-3a2f-9e32-52371665588b | -11.59227 | -43.69653 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2d8f8142-b410-38a9-b936-f5c564cfbed6 | -11.96551 | -38.39124 | 2026-10-09 15:58:00 | NPP-375 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 81ed035d-0431-3575-b938-9e258615e584 | -16.2643 | -42.5238 | 2026-10-09 15:58:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96a26a14-d611-368b-b2f1-2894b077f119 | -16.12071 | -43.39653 | 2026-10-09 15:58:00 | NPP-375 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f14293fd-e77c-3b05-9a5c-05547f39682c | -14.05207 | -43.83876 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 48cd2e0d-34a8-39d0-87ee-8fca408bba57 | -12.24776 | -44.75417 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 74d28ab7-9b18-36c8-a20f-edfda6902ae5 | -12.23877 | -44.78508 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c32466a1-cf35-3952-b410-bae686ff6cb2 | -11.57495 | -43.65168 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 69847851-c524-3a7e-a65e-bc4c496c03fc | -12.11291 | -47.35625 | 2026-10-09 15:58:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73ac8321-9731-372e-91c0-cafa89d18350 | -12.1923 | -44.82057 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 632f7f2e-e5f0-3a91-91d0-9a3447fc7513 | -16.76747 | -40.93346 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 582db396-2d35-313d-8f19-724c04220da9 | -14.80085 | -47.13002 | 2026-10-09 15:58:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2fdacf58-4b13-3c68-a63c-2f460f263e17 | -12.22169 | -44.63952 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9554ddf8-5e6f-3212-ae33-b4b2f619a49d | -12.03844 | -43.44709 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e38f2056-adbe-33ec-8158-b11c2ce3c0c3 | -14.27062 | -42.18526 | 2026-10-09 15:58:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 91ffab93-e428-3fbf-9bc6-5f855c470c7e | -11.77886 | -43.53196 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46f66195-c506-3cba-a5d3-1aa2860169c6 | -14.74765 | -41.14999 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 306c0daf-76d5-369f-8d41-aa81d8c0990a | -14.35279 | -40.86236 | 2026-10-09 15:58:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 8660ad8e-2ac1-3a83-9139-9e983b2bc04f | -11.60225 | -43.6322 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 58c5bf30-9ec1-351d-a0a5-773d88d6b27e | -15.38407 | -41.91594 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.3 |
| d21637c6-11dc-386c-a1a1-f4396557b2cc | -14.9272 | -42.01035 | 2026-10-09 15:58:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| c5690873-8104-38ba-99fe-0c05fe778662 | -11.99416 | -43.46464 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e426778a-a180-3edb-84d3-3870c3fa5f65 | -11.59659 | -43.6849 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60a962c3-d032-33e2-9cb5-fa33b51f3fbd | -15.36605 | -44.84269 | 2026-10-09 15:58:00 | NPP-375 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 213b2630-4c52-338f-817b-ff0c0788ae56 | -11.77174 | -43.52938 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6b9e8ce3-05ba-3bff-bda7-d750c5868aba | -11.57965 | -43.68991 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a33885cf-11f0-3252-88c4-bf1e1be9711d | -10.70999 | -39.833 | 2026-10-09 15:58:00 | NPP-375 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1cc771b1-c84a-3c45-8fe6-246de3b7b9cb | -14.44814 | -43.93576 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1b70c970-4d40-3b47-ab9c-23f7c0eaf89e | -10.61559 | -38.88139 | 2026-10-09 15:58:00 | NPP-375 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 3fc331ea-e8ad-3a49-93c9-818d22ba6f61 | -12.23533 | -44.75576 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b4fba796-5a22-3e37-850f-d26c4a065007 | -14.05997 | -44.78016 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a8a6c0ea-e44a-3adc-9be6-361af252fa2d | -17.09492 | -39.47822 | 2026-10-09 15:58:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3e6be776-43fc-37ce-8e0b-c62bd732c196 | -16.13592 | -41.69224 | 2026-10-09 15:58:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b78a5fd8-ffd7-369e-a39b-b4b1c3f5e563 | -17.51619 | -43.67812 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d45fda2e-beec-366e-a184-9a8d464f49b2 | -11.84269 | -43.58031 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 75ca1053-bf86-3251-ab88-a395622eee99 | -13.36097 | -40.12004 | 2026-10-09 15:58:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c8fe6450-a36a-34dd-8ed7-4074754726d4 | -15.01068 | -46.25909 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3b8c35e7-e88b-3668-b5ff-fdb70b4087d0 | -15.84862 | -42.03047 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| c2a05f61-5cdc-329a-98f7-52d1b3b73e0c | -16.12912 | -42.85334 | 2026-10-09 15:58:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 592ba6fc-5504-3224-a21c-af13bea4371b | -15.25847 | -42.37606 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| e71d723d-46c0-3536-9fa6-9dc1148c7bfb | -12.21274 | -44.83332 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2dc046d2-5c41-3bcd-ae13-63058573db5a | -11.83696 | -43.58107 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7724fdef-830c-3198-accf-ea0547ee02a7 | -13.40023 | -43.48227 | 2026-10-09 15:58:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 0eb3d127-d5b5-3adb-842e-62ea4acf8200 | -11.61637 | -42.811 | 2026-10-09 15:58:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 83ec731c-c9f1-3c40-ac25-de9eb78662a4 | -14.05486 | -43.84193 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| fbd9cc4a-b3b9-3d69-9579-44178f51a190 | -11.89753 | -47.37919 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f1e654fc-06c9-37f3-945a-1df0f2da4b35 | -15.22206 | -41.10253 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f74c4f37-a3c0-3e97-874d-bfb3b59918b9 | -11.65737 | -43.70243 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2cb7bd80-2f28-3946-b97f-fc3a30ffbd6a | -12.1958 | -44.63206 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 289.2 |
| e8efe830-a977-3625-90bf-63808c9e87cd | -12.90368 | -43.45687 | 2026-10-09 15:58:00 | NPP-375 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a69d1b7d-b50b-3be5-9802-04a8af172612 | -12.15378 | -45.34889 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 095bbcde-1cd2-3d3d-a51c-f0c5e1d11c55 | -17.51371 | -43.67004 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5322841f-f374-3635-94fb-4958e59c328a | -12.31114 | -47.04935 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1d0ce1ce-3c47-3415-a12a-666a4101a7ed | -16.12851 | -39.00886 | 2026-10-09 15:58:00 | NPP-375 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 386110c9-9a79-3f1d-8046-8b3a9d7b0772 | -14.54746 | -44.91413 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 17c081dc-5131-332c-b34f-7753d9fb67fd | -11.98967 | -43.48478 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5ecc7b2a-a528-3559-9b8c-b343ad83475d | -11.97371 | -43.49662 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 53832c2c-86ef-30c2-a371-9dcdf78e6b9c | -17.31765 | -41.4001 | 2026-10-09 15:58:00 | NPP-375 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7689176e-73c3-3771-8b44-55ddcedcb241 | -11.9984 | -43.45131 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 25fb7148-082d-30bd-b60f-f1fd32b27445 | -13.28541 | -40.32463 | 2026-10-09 15:58:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 75da8251-18ab-322e-b1ac-ddd3da620e77 | -12.2489 | -44.76391 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4539f6e3-043b-3a84-a743-c6851c0d32bd | -13.10761 | -46.34314 | 2026-10-09 15:58:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4c5375a8-b675-398f-86a7-12cab0834f5b | -12.05384 | -43.43071 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 429170c5-6cbf-342b-9955-daf5d1a04e8e | -14.62144 | -42.70461 | 2026-10-09 15:58:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |


[Clique aqui para ver as próximas entradas](README265.md)
