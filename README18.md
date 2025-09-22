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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3737062-7647-3855-9c09-bc2d1bd5b611 | -11.4715 | -46.93972 | 2025-09-22 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41d02528-a1d3-3f1a-8e2b-11a8a3bcdc36 | -7.91315 | -43.878 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cce5012-1be2-31fe-810c-4a54075c2fc6 | -13.70812 | -47.57641 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bac75d6-a22b-3693-8abb-6fc3e0d623be | -6.90139 | -44.76228 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4a005c2c-9e9a-3ab9-83bc-87980b2120aa | -7.36377 | -43.84428 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05ca3fd7-6fb3-3a59-bea7-2a6a08db59b8 | -11.73298 | -47.80758 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bf2bfa0-4ce0-3d62-99a6-5a04e169ce07 | -13.67783 | -47.71101 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a1b8c04-2951-314b-8cb6-16f7f167bc6f | -7.35596 | -44.6089 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5f6539a-ea85-3e5a-b39f-d3b0a1e78834 | -7.36249 | -44.54712 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 974c7d44-8fe4-35b9-ab67-57dffc8a4200 | -5.65482 | -51.46204 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 451cfb7b-69ca-3aca-be84-5b01de46058e | -5.574 | -42.13036 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 817e7b86-d833-3235-af73-32568ac5505b | -5.03621 | -43.61112 | 2025-09-22 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac38d16a-7868-3b57-93d8-aaa08359ccc2 | -13.67072 | -47.70959 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3971bb58-6f1f-3cc0-bb47-ce6b6c4bb901 | -11.26391 | -49.24601 | 2025-09-22 04:17:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef20525b-a886-3e1d-be3d-6f31168142b3 | -4.31719 | -48.08878 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6d2dc7a-d956-3359-b18d-a62b92dc291b | -14.97405 | -44.40933 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a12599c0-57b2-3cb9-b7dc-2133d1ef3cc5 | -4.99341 | -45.15511 | 2025-09-22 04:17:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13ad572f-da59-34f5-8ef1-a15990ebfc3e | -7.606 | -44.48723 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57cf8d3b-f02e-3140-94d2-7a7699b21ff2 | -15.09554 | -43.84223 | 2025-09-22 04:17:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5e21a1a-ee38-33d9-bced-572cf7c83d09 | -7.35574 | -44.54603 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d977a2a6-6f86-3650-872d-6742bd53934f | -7.38261 | -44.57249 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1b6fc8e-86d8-3266-ba97-94fa8a3435b3 | -4.52193 | -44.03171 | 2025-09-22 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d6adf62-c7ac-3429-a15a-d756c8c7958c | -5.58476 | -49.24604 | 2025-09-22 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2b32a75-88a1-31cd-bfed-99621534f56e | -6.89445 | -44.7836 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61b9bc5c-231e-3b9b-8b37-71f4e98b3e97 | -12.72415 | -46.83522 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2deec2d7-5002-3812-99f4-25ac34a4725b | -11.26553 | -47.47916 | 2025-09-22 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9ad0ba0-7157-3b22-a199-71ce6e5c47f0 | -6.81534 | -41.75266 | 2025-09-22 04:17:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 112d7ba5-31c2-3027-aa4a-f7178de82e9a | -7.60557 | -44.44701 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85cc6d7b-6207-324d-b49f-b64a255c6f8f | -11.22446 | -46.16602 | 2025-09-22 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d4198ed-9454-332a-b84f-14a70462bd26 | -7.64819 | -44.43918 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc0ef728-5458-3da4-8ec8-afd295d4b58d | -11.63638 | -44.3331 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 782553db-08b6-35c8-80d4-de49dbba70ca | -12.73589 | -46.82929 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbf66a23-328f-3a0d-a376-48a2a7d5ec43 | -11.66264 | -47.49451 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25c06421-c6cf-3e1a-a5d8-ae63023278c0 | -14.40335 | -48.5547 | 2025-09-22 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38d6a964-3e23-3022-b4e1-d997546c00d0 | -14.43967 | -46.52696 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb6b5a64-c34b-337d-99b6-2bbad2e20a0e | -11.66626 | -47.49515 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 606f84ab-f382-376a-b6f8-de1837907c01 | -7.35633 | -44.54242 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df02a833-5d93-3106-bab8-9af660bece4b | -12.13427 | -44.7761 | 2025-09-22 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58e19c87-d448-386f-bcd2-766ad396bd3b | -7.45719 | -42.62893 | 2025-09-22 04:17:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f10732cd-e0a0-3c09-a579-556b06e470f3 | -7.35737 | -44.55738 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b173c268-1a1a-3079-aa94-361bb8827cf3 | -13.31501 | -47.29455 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1468df1-390a-37b3-8fff-2e3fb7e620f9 | -7.93804 | -44.1083 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbe5e963-9a9e-37c8-8122-f7d8850a4a16 | -7.22423 | -43.74699 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 699390d5-0bfa-35c8-8b21-c99cfc5e81b5 | -12.70807 | -40.47374 | 2025-09-22 04:17:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab7075cd-5291-33cd-af18-e67c12dc849d | -7.35399 | -44.55685 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cc8c23d-b23a-3034-b068-019d4f621edf | -13.86121 | -44.41355 | 2025-09-22 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4f04ba2-b29a-348f-bdfe-b599d1e5252c | -12.43158 | -45.14219 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dece20e2-fa13-3b2c-9e9c-623bdd00fad3 | -7.62611 | -46.82196 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acf10ace-8839-3904-8f71-d525c337395a | -12.06803 | -44.82706 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b6a3d6e-107c-3c8f-9f3d-47d4d1237c06 | -12.44509 | -45.10052 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c80a5f5-3751-3410-8b55-d8d3a3c0b56a | -7.50753 | -43.68453 | 2025-09-22 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2e8f307a-e4f8-3804-ad6c-c8ad9d7e0d5f | -2.64157 | -48.0443 | 2025-09-22 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d2c81e9-071c-3510-9460-c14d0daf216e | -14.52987 | -44.87739 | 2025-09-22 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d854dd0-7e40-3a5a-a3cc-70582c64c5d0 | -5.65167 | -51.46238 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6732ca8-2756-30f8-8d8c-29a581558b7c | -7.23033 | -43.75154 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba34bb6b-e3ee-3ef6-b837-961a2cdfbf98 | -5.33109 | -44.82247 | 2025-09-22 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3799e363-8f19-38a1-9b55-a6170d800998 | -12.71053 | -47.70451 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d396eab-53c8-3ca1-95e5-2c6cf84ba3ed | -3.38499 | -44.76725 | 2025-09-22 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc20e2f6-45e2-3100-b885-3e9be3f0d1d4 | -14.32251 | -47.76658 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 443b2c3b-6d23-3b4c-8638-83c3aed5d6d9 | -13.96509 | -44.42691 | 2025-09-22 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54f3cbd0-7357-3acc-a42c-82c8800d07ea | -5.06452 | -40.47398 | 2025-09-22 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ffb06f4b-137e-3533-9e4f-0c0b488c85a8 | -7.61272 | -44.4883 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e4855c9-ad94-318d-a08d-501aba44efcc | -7.36074 | -44.55789 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f12e42b-db33-3472-90f2-51bca84e20fc | -12.07981 | -44.79622 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d2d5a358-fd7e-360f-b867-8154c2c497e1 | -5.6543 | -51.46508 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80a3c8e1-3265-3aac-8268-fa460d09ce8d | -7.37645 | -44.56778 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c3d14d-fee9-3e84-a9d2-9fe97dcd55cb | -6.45237 | -45.67976 | 2025-09-22 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fd17d78-e5fe-3c49-b612-cedb6ce48d4f | -11.66335 | -47.49037 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35a1302c-a32c-39b5-ab4d-1610b39d4d83 | -11.32216 | -54.35133 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 804f5bc1-81ff-358a-9cc3-00cc439c0e5d | -5.58548 | -49.2417 | 2025-09-22 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e023eabf-4d2a-3df1-8f51-0e2ff26e2969 | -11.65903 | -47.49384 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| baf1a8af-0b93-3e3e-8f5b-02aeaaf38f36 | -14.32467 | -47.79687 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44971c1d-7f5f-3d5c-bd45-3ed187062fe3 | -7.60993 | -44.48421 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 69feff0e-ee9c-359f-a51f-8aa88d04b54d | -5.5851 | -46.25616 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad921888-9765-3d17-8fd6-8e16662d18ab | -12.74284 | -46.83052 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 167118a3-a214-31b6-bd2c-304ea67ae8c6 | -11.64527 | -44.32008 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f84d87c-847b-3639-824d-9b2def5e171e | -7.60615 | -44.44344 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e62be906-0296-33ad-a458-e6ced8761c72 | -14.44427 | -46.52025 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e468219-b97e-30fd-b9c3-5cdb400e8859 | -3.14089 | -44.42922 | 2025-09-22 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41e8bcc1-d3ba-3755-8da9-7f1cfad52815 | -4.77838 | -43.71857 | 2025-09-22 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d005cf22-4db9-3608-9b95-1d51b62e678a | -5.6506 | -51.46843 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2714c9c9-f235-3c84-a3c3-6b43db21b911 | -4.43035 | -43.06156 | 2025-09-22 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99bb9fde-78fb-3e22-afdf-c54ee26aae9c | -12.45302 | -45.10508 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88ba603d-1b11-33a4-87e7-6711e9823ccc | -14.44643 | -46.52834 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1e3fe813-9422-36b5-8395-1a6fe0793956 | -2.25679 | -47.88404 | 2025-09-22 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9990ef0-9d3b-39b6-a66a-1bce828caf6a | -12.6896 | -46.84218 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b39aecf-28e2-33af-87b5-b7ac0129fab5 | -5.63894 | -45.95104 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9322c41d-907f-3a44-a9a8-ef320389f6f7 | -7.23311 | -43.75556 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddc69df2-e13a-359f-be32-b48aad84550f | -5.64355 | -51.46626 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2356568e-1292-300f-96c8-fd6ba926cfc9 | -4.31303 | -48.08808 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d37acc7b-ec41-31d4-b241-9b6cc00cce14 | -7.36191 | -44.55069 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8962613a-c8dc-305f-9b8e-54ae9e7340ac | -13.27374 | -47.64576 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dc9b64d-74c0-3018-bd49-65dae2e811e3 | -4.52251 | -44.02812 | 2025-09-22 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef66a3c-b28b-3208-937b-3adacf8d1b45 | -13.50493 | -47.26016 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7677b423-f35c-3950-a1f4-0008b92742a3 | -13.30725 | -47.29753 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6266a0c4-dc7a-3692-ac0b-fbfc1c0a66d5 | -11.33333 | -54.35389 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd3bd557-5730-37bd-b758-6b8e2e6235ea | -15.25413 | -43.08565 | 2025-09-22 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3ba0af43-b459-3a2a-a425-4000b66a3d8c | -12.00004 | -44.96181 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c8e885c-0d6f-35f9-b8be-705a40b8a63c | -13.67143 | -47.70543 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d7bc622-b066-3a98-9508-329ee6b8d23d | -11.47216 | -46.93571 | 2025-09-22 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
