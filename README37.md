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
| a58c6aaf-be6c-3693-a66a-a188280b7d5e | -12.31516 | -47.94996 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5d753d4-545e-31e2-8b8f-d5a61fd9eb4d | -11.7062 | -43.44559 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 362c5e28-9c98-3757-888e-1802074f7d2a | -11.18175 | -44.83422 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4922e45-f007-31f0-b981-182ec1be70cb | -10.9 | -56.17794 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c69cba58-2894-36c0-9cde-c423cb3af830 | -11.37378 | -51.02314 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5d4b7e9-6fdb-3581-a36e-4ed2d80f67b5 | -12.05703 | -46.44583 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7309ad1-5566-395b-94ba-2b8a194ac29b | -11.38793 | -51.01442 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de44243-1081-3c65-bab0-61e57c80eba8 | -9.96909 | -47.98454 | 2026-09-30 04:34:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4aec92e-7bdb-3fc4-866e-da35a292f90d | -13.33988 | -43.94954 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b50f92a-193f-3674-852d-db2f2d264748 | -9.81591 | -48.21343 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32967978-ebc6-376b-a81a-ab4ae0a1be45 | -11.39926 | -50.99768 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5b41bd7-f9fa-3277-82a6-9cab4003a24e | -11.4037 | -50.97224 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 25d493ef-cde1-3a59-8f36-5557cdad8dcd | -11.84678 | -50.96359 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27508e28-c2ca-3fd4-a7dd-7da2133c3021 | -11.41544 | -47.02348 | 2026-09-30 04:34:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c943f38-2ce1-3fc8-83b2-76e91fa89e99 | -8.26886 | -54.76117 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0983a791-293e-3891-8bee-ac1f2cff0df8 | -15.13003 | -43.62477 | 2026-09-30 04:34:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48b3df52-bae0-3a49-b772-b206769bbf62 | -12.62944 | -48.35836 | 2026-09-30 04:34:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3e301fd-998d-3a6c-81c7-40f555e6a384 | -11.39455 | -51.00056 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 209bbb66-3476-3b9d-83e6-cff76226efbf | -11.1851 | -44.83476 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05b27369-5b56-3f6e-873d-b334c85fe724 | -10.83739 | -48.71572 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d53318f-a55c-3b97-8df0-ada3ae362f6b | -11.67099 | -44.51104 | 2026-09-30 04:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26313fca-185b-3065-9461-366acb2fc84b | -14.12512 | -46.26502 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 572a5393-640c-3629-a908-0c97fe3c3a8b | -13.1813 | -48.51719 | 2026-09-30 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c33c0b4-d6f3-37dd-9a39-3338da3bdb48 | -11.84345 | -47.78294 | 2026-09-30 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00188c4e-d05b-378e-8bb6-5b721316add3 | -11.84212 | -50.96642 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| db655af4-1a2f-3947-9cf4-2592de76705f | -11.96407 | -51.00651 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 376ec036-e0e0-3fc9-804f-35c69e886a2c | -11.42804 | -43.42953 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99576722-19f6-3be4-bd0d-fe6b7376d62c | -16.86346 | -42.46615 | 2026-09-30 04:34:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 172902be-54a8-3dbe-b911-d7ce69330000 | -12.0798 | -46.45335 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aeec901c-3e51-3aa1-8574-4857cefb3dfe | -12.31172 | -47.94936 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fed9f0b5-0df1-357e-be7e-621cc6fd8816 | -12.34699 | -48.19537 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9736c94-01e3-3701-bd54-5b20dcbf5deb | -11.38666 | -43.37088 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade1cd02-7708-337b-8dc3-55c4c324f158 | -10.73642 | -44.44085 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc2000af-14d3-359e-91d5-7772e7cd73f2 | -13.1892 | -48.55544 | 2026-09-30 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cb50442-5595-3f87-877d-43bc74d0e2f0 | -17.52412 | -43.70517 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e22f5bf4-f8be-36bf-be9f-3edbd3080247 | -10.2561 | -44.59353 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc3b8caf-e11e-3e6f-a8d9-a51d1683aa20 | -10.89482 | -56.1744 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c45b470-f5bf-3490-a823-b75d72759679 | -15.46536 | -46.128 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96f15386-768c-3509-9ad2-fa49d97a83ca | -11.1756 | -44.82958 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51d40039-9e41-3297-93d5-c0e47749e8dc | -13.39672 | -40.07011 | 2026-09-30 04:34:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7b1ff0a2-5e60-325f-92f1-64e27073c239 | -9.76794 | -44.81805 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8a74e0a-beae-3dee-81ad-3ac5a7f20266 | -8.94544 | -49.79324 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ffb1059-6448-3cb2-bb02-820a790f43f1 | -10.89423 | -56.17683 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60cbddfb-f5b6-35f3-97bb-9f7cbbb6c410 | -12.78484 | -53.9932 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d341cfc-588c-363f-85df-9dbcc23ec4d3 | -17.57557 | -43.70585 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 733b8ed2-6b66-38f2-b953-59053521e633 | -11.34767 | -50.98071 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d674e55c-a6d7-3285-9189-bc5b6fffbd77 | -15.2021 | -46.14375 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77708272-fced-308d-a750-262daad714e4 | -11.62864 | -43.53115 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 295c8de2-e9a1-32d4-9ff3-2321422689e7 | -13.42856 | -43.81014 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 1b53c25a-4d6e-3f19-8aa6-d27813936d87 | -13.38225 | -44.02414 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 816f4dee-a748-3dc0-a78d-da5a3a81018f | -14.5302 | -48.29357 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e525553-eb59-3f0b-9e0a-e2952f51b699 | -11.16665 | -44.82082 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5c13d938-6e3c-334d-aa19-3e09cb8b2c01 | -10.70709 | -50.83486 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c2d442c-6a74-3a1a-8ec1-f5030506d891 | -12.51762 | -43.08766 | 2026-09-30 04:34:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ab9a415-230b-3353-80d8-8e27c78efce4 | -10.89409 | -56.17819 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64086aec-12fe-367d-8fb8-b2c3d1f1f82d | -8.11716 | -54.85417 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5efc9df6-f276-34c1-805a-c2fca5193c15 | -11.8415 | -50.97 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78a5b0ec-46a1-3638-bedd-12d65d401a98 | -11.19469 | -45.1246 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d770e65f-911e-3b7a-9d51-860ce61fd384 | -12.0781 | -46.464 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de411b80-52ea-3bcc-a231-5d2619ed2906 | -13.38282 | -44.02029 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51f1ce60-88e7-34f1-8400-72ee6746d183 | -9.82591 | -48.2193 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f58157b-35c3-31f4-9c46-a065bdf0f18c | -15.25896 | -44.81903 | 2026-09-30 04:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24608c50-4909-3d1a-a426-ace4d13543db | -12.94816 | -46.64391 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0617e76b-2eef-32a6-93aa-ce55fbc24594 | -12.19489 | -47.11163 | 2026-09-30 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d5cf41d-bd0a-3d30-9da2-2432a8c22974 | -12.78565 | -54.01555 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f286195-123c-3e94-ad21-d9aef592df8d | -15.4765 | -46.12249 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cb8da30-5300-39e9-835c-ecf187ffd389 | -15.20154 | -46.14734 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ce98773-42e6-3158-a4d8-0acfcc23364a | -14.50625 | -48.2895 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 032ea341-662d-3dc2-a917-ce5d1922412a | -11.19525 | -45.12104 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b600c25b-4d77-3550-8125-bce48ebf76cb | -10.71842 | -44.42324 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 700431b4-5fc5-3a0d-9a47-e36cd096014b | -11.4065 | -50.98024 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 991c4857-426d-396a-81d1-15916a93bd0d | -8.26955 | -54.7575 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a2738c2-38d1-30f9-8e43-2eee73d3ee5b | -11.29853 | -50.97987 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31df3569-f07e-32e5-937e-d78775f96f0f | -13.37505 | -46.83134 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cffabb4a-e5df-3779-a998-9aa6a282742d | -10.83954 | -48.70273 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2937a55b-3e91-389c-ac5d-5100c83d4eec | -12.51824 | -43.08345 | 2026-09-30 04:34:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0eec00a-a38f-371c-88ba-32e5df4e1cd7 | -10.73417 | -44.43306 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c1bd433-eedf-3066-b664-909d6d63b31b | -13.68054 | -44.28996 | 2026-09-30 04:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d23ccb78-fcc7-375a-87e5-685b292ee697 | -10.51863 | -45.36029 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19bd812d-841e-38e8-ab13-7a0ecce00c32 | -11.3971 | -43.46879 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b5a4044-053f-3590-af36-a02503108fba | -15.34924 | -50.15471 | 2026-09-30 04:34:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ddbe521-0364-3d08-82bc-6fabd1b6b48d | -10.71167 | -44.42221 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90a98a70-fc00-366a-9cff-e9e2bf052ee1 | -10.08165 | -50.31937 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a70e936-59fb-3de1-ba94-f23f9dd0578f | -10.13083 | -45.1321 | 2026-09-30 04:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85d7f40d-16cb-3441-9a2a-aba747f966bc | -11.19246 | -45.11696 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad105122-3864-3477-aa5f-0c9252e4d256 | -10.78067 | -47.25375 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c3ecb88-0248-3ca5-870a-5a03d4911000 | -11.19795 | -44.8405 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0a86480f-f092-3196-b571-d78e1b3b57f6 | -12.25492 | -50.27708 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a409181b-cccb-3fe7-8191-c9a24c822d2c | -14.01528 | -42.90762 | 2026-09-30 04:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bb2e6c0d-1f02-3b00-bdec-83390ec5616a | -11.38618 | -50.97652 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66ab3702-f934-391e-a0a1-ed45a20b53b0 | -13.86566 | -44.44769 | 2026-09-30 04:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2521fd2-560c-3ae0-843b-6718a166055b | -11.83809 | -50.96567 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ba9855fc-896a-3e56-aaec-0b328a107e43 | -13.1864 | -48.55076 | 2026-09-30 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 949d78eb-e735-3fc2-924c-fd7a948aeec3 | -8.06437 | -55.34241 | 2026-09-30 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0997ae8a-eaef-3254-b60c-4bdebadb87b2 | -11.93983 | -44.80237 | 2026-09-30 04:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31b55c20-a71f-31d6-92d5-a0eb81ffaeb6 | -21.10581 | -45.80136 | 2026-09-30 04:36:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85b8d995-9883-346d-bfc2-11a68639c005 | -20.77043 | -46.3062 | 2026-09-30 04:36:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3343d68a-9c44-33eb-b965-6769fd53c6e0 | -21.68174 | -45.64433 | 2026-09-30 04:36:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a4c104c9-731e-3f18-bc80-93d7e546d9e6 | -20.89253 | -49.34617 | 2026-09-30 04:36:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ac7bac7-8e5f-371e-a5cb-ab4d08b8a320 | -22.5051 | -47.60648 | 2026-09-30 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
