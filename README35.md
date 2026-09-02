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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2bcc367-c173-3625-b3bb-14dd3df73058 | -11.01835 | -48.37603 | 2026-09-02 04:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 715e7d6f-c734-3f17-a21c-6a12b1cf462f | -8.44023 | -54.71616 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6302e023-d5bb-3fe7-837a-11ef8a384a78 | -6.20516 | -53.47741 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5bb8ae1-2201-3d29-98ec-930f3788593b | -10.44113 | -46.73189 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b882365d-d6a2-3209-945d-1d4b88538873 | -10.40422 | -50.00713 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 608a9be5-1deb-3659-9637-68d44f3bb0e8 | -11.02142 | -48.38118 | 2026-09-02 04:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c76a875d-2ad8-3ee7-8ae0-f071974b601c | -7.6526 | -45.87384 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a9799275-d738-38ac-a81b-252f196e100a | -6.19094 | -55.2752 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7717d02-2e80-3b2d-b869-5e853ca97c5c | -10.04817 | -48.69873 | 2026-09-02 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 966e2490-9492-36b2-a692-4c00a4aa2724 | -9.94394 | -53.99318 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70e0802c-3913-3683-8998-ccdeb7cfaa63 | -11.29831 | -50.62878 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67a5bac3-a137-3959-a769-ce62a482cf3f | -13.7103 | -43.88135 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d522533d-df7b-31f9-a5c0-84094dbc838e | -8.42938 | -54.71437 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| daaa4ba0-f488-3e1e-8966-bd455d467218 | -6.94236 | -56.46287 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c56486f8-d9e7-3820-beea-d033e0299804 | -8.44826 | -54.73471 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8f0f2bd-de01-3837-95a2-c29521264879 | -7.41198 | -49.73654 | 2026-09-02 04:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2e21bf-5b57-3e77-9939-46cb943c0d4b | -6.04762 | -53.84614 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac379135-5240-3cf3-88e4-44a868a723ad | -12.15032 | -47.11626 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98b1a08a-95bd-3de8-817e-84eca8f4bce1 | -7.94617 | -52.45987 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2db8c46-36aa-33de-a132-9be08a8bc435 | -8.91066 | -62.35514 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b491bc4f-a2bf-3f96-86a6-79b5aa3e8ba4 | -12.63154 | -45.0733 | 2026-09-02 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 88cd2c8c-9ad2-3c73-ac88-58de5aa2a3ad | -11.3164 | -45.15364 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 470f26cb-40fb-3ed6-81ba-4115cb0944da | -9.23012 | -47.97426 | 2026-09-02 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bef0854-7512-3944-88d0-bfb3b8ff59ba | -8.5706 | -63.18828 | 2026-09-02 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a57d7c-f622-34f0-858c-4922aaa1ea90 | -12.12873 | -47.05999 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65ce06a1-8ffa-3f1b-9999-f459f941f1fd | -12.13593 | -47.09906 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20a0db6f-03ba-3295-8d6c-8494be4aa5d8 | -8.44605 | -54.72573 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 464a5bd7-0592-39f9-ae97-e671cef9bda4 | -11.66441 | -50.18544 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 372c59fe-44e9-3a70-a3a5-ad9c2897eca5 | -12.84464 | -51.78236 | 2026-09-02 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 500e8222-3197-3bda-ab1f-9da625a20354 | -8.46624 | -54.71618 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9ce9a017-586d-39e8-a40c-7f2c4d1c4704 | -11.4837 | -45.08947 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3ad5a029-5968-3129-b0f9-ef5a5591d1fe | -6.77002 | -59.43613 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60af1641-de15-380f-8155-85cbb07c881a | -8.57154 | -63.18341 | 2026-09-02 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8b69937-05e9-390b-a7f4-bf7e0340ee47 | -10.40882 | -50.00007 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3d8384d-cbfa-321b-bd2f-f70e391a00f3 | -11.52867 | -46.91149 | 2026-09-02 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b110019e-ffa3-343d-b1aa-cd3c5d160f44 | -6.9191 | -59.64482 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da944180-2cf3-3a72-9959-e13272d368fb | -8.44896 | -54.73052 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8c4e0f45-69f0-3903-8ae9-5f805334d2ec | -10.89703 | -45.33398 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9611b1b-a2ac-3f29-b0d8-5e13ba596a37 | -8.43309 | -54.71234 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79e36dfd-7d5e-3d44-bdc8-662d0539eb82 | -9.47031 | -57.03318 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5334dd30-7528-3f2e-b485-e31dcb0f46f9 | -8.46333 | -54.71138 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7f9690a-90c9-3129-bc2f-178f189499ae | -9.715 | -54.33574 | 2026-09-02 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d618005-921d-3716-b88c-2b28c161cb0d | -5.97479 | -53.58492 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2392335e-8bcf-3aed-ae37-fd965dac23d2 | -11.35205 | -45.40753 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef721741-bcae-32c0-a36b-18c75ee2a81b | -12.1426 | -47.1415 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 64c58ae5-9439-3f10-a4dc-06f17374e229 | -8.42648 | -54.70953 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 243ad46b-5c62-39f8-9420-43988b7a9546 | -8.99859 | -50.7775 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e8df024-5fda-30ac-91cf-521e409c8be1 | -10.68275 | -52.50389 | 2026-09-02 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c2d3b40-8f12-3764-be1a-a1defb80684d | -8.13209 | -54.95234 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc9db58-2a97-3d4d-8079-5dfff749b84c | -12.1313 | -47.07185 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 072da5c5-c1bd-329d-9a07-e730b7bac97d | -8.45249 | -54.70957 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5897def9-62cc-3db2-984d-d04fc393bcdf | -10.99621 | -45.07726 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3ffd59ad-d937-35ad-85b9-3049446a303c | -10.50206 | -59.61517 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f15d3544-e1c6-37d5-a1fe-f8e069a6f289 | -10.79225 | -44.7486 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95d9e538-a36f-3196-add4-1681fa680a57 | -9.70079 | -47.2088 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05056deb-f78b-3849-93fd-2708f206ca93 | -12.12461 | -47.05937 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0e78e0b-1f9c-36df-946b-a98ba4d8c14a | -5.97536 | -55.70387 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f26ba5dd-7d15-322f-b1d3-0d8b4092185c | -8.44746 | -54.71735 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8919b9dd-f563-3e6a-9760-100647f51996 | -8.2659 | -54.95622 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 111f8896-6d0d-3c00-9946-977a74304da0 | -12.14159 | -47.11874 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af2bf437-3c2f-3816-a486-80da7163f4ca | -9.39734 | -51.68315 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a3063f1-e4a3-3616-a946-5a358be376b0 | -6.41292 | -56.17793 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4001563a-dddf-3f0c-84c6-55ccf3fe1316 | -11.75915 | -50.54927 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f2777e0-498e-3af0-9406-200a7a9d6fca | -8.43103 | -54.72492 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0393ddcd-c06d-39f0-988b-0d6d3e44f8e3 | -8.11731 | -54.95039 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d553281-491a-37f2-b9c3-b35a1b40cefc | -6.68535 | -58.75708 | 2026-09-02 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f9a1ebb-992b-396a-b34c-2a3535eb4e55 | -8.44235 | -54.70358 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aa72927-719f-367c-8bea-2deb6fef622b | -5.9735 | -53.59284 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30051c95-0542-3378-85e7-7668b8e13a93 | -10.90677 | -45.33059 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 72bc1895-7fc3-3575-922b-447fb4d9692d | -10.78427 | -44.76719 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2eda2b89-602e-3e67-b59c-03fb8fa27505 | -8.44525 | -54.70839 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7beed13a-5279-339a-94d5-8c4864d07fee | -12.07439 | -47.13138 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b36aff0-366e-3af7-b846-5afd3a3d7aec | -10.78636 | -44.75201 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7da0eeb-061a-389c-a67a-ead4d94224b1 | -7.75768 | -61.19727 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da00d26d-ccac-3dbe-916a-2560311ea385 | -8.43447 | -54.70388 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9192d730-7826-3500-945b-188c183eaa3d | -8.44596 | -54.70421 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3575f9f4-7d92-3071-b1d9-707c4cdbd0f9 | -9.00807 | -50.7827 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 092b859b-6915-383e-a817-d606024bbceb | -10.35124 | -49.96862 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ae3d80-0441-329a-b660-66fd10086c5a | -8.50386 | -55.29785 | 2026-09-02 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3d20cc-2829-3f3d-8b77-6e348e5aacda | -8.287 | -54.91945 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e0fc36e-9139-3959-93d2-bb0218713464 | -6.07682 | -53.66647 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a3420bc-8750-3004-8e18-ddf7604074ad | -8.4568 | -54.70601 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 464e51f9-3ae4-3b51-b16d-5667f070f3f3 | -9.94111 | -53.98881 | 2026-09-02 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54b0eb3f-ec00-3775-ab91-ec6baf1eef8e | -6.25248 | -55.43557 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77389e81-46a4-3ef3-bc18-3edc8f5a4e33 | -8.91651 | -62.35632 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90cece6f-85f6-3477-8d9c-d9abb1cdc1f4 | -6.2414 | -53.47532 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5f091d0-9e45-31c6-ad8b-2caae0f720a7 | -13.7541 | -43.8275 | 2026-09-02 04:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c34993ce-a94b-3f03-a950-b6b028a0aa4e | -6.25277 | -55.42796 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 962ba1c3-acaf-34a0-b3c4-a0d67f9032cd | -8.47336 | -54.69583 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28b40c80-722e-314f-a6f4-2db46536dc1a | -6.88146 | -56.50514 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d92551f4-6a08-3807-8350-51e1a6beef7d | -9.21754 | -47.98163 | 2026-09-02 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4b8c99a-591b-3975-be32-f57d78b85761 | -6.86019 | -59.47744 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8779dc37-0be7-3481-99d6-843119fd3b0b | -7.36691 | -45.05109 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdc6b0f5-9043-3506-a220-3157a4c844bb | -10.67943 | -52.50335 | 2026-09-02 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7787dc9f-6304-320d-a7d2-546dcbdc6620 | -11.48304 | -45.09434 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c9d8b6f-1452-3298-b8f7-0a0c16c40bc9 | -10.74975 | -47.98045 | 2026-09-02 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73430a84-e756-3b72-a9c8-ac24ed45f0a3 | -5.97191 | -53.58043 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40ed5f0d-7481-381d-8d3a-3f62eeec0a6d | -10.85252 | -54.04207 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d602dbd3-63c0-3cf2-bf78-bc7aa52f93f2 | -10.41169 | -50.0044 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 107d3e5e-cefe-3137-9ee4-4da8e4a16415 | -9.08399 | -65.38007 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README36.md)
