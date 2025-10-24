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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 117608ec-b6f0-3eef-bd54-f09cb4e4753a | -16.32966 | -49.08442 | 2025-10-24 04:40:00 | NOAA-20 | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9edf6366-0c0f-315a-a2c4-7c64f0e89f1f | -17.47345 | -45.99214 | 2025-10-24 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aedbe40d-f3b1-3eae-8fbf-8a6207d9c274 | -15.83187 | -49.10123 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c5f19dc-469e-3433-821d-a4b2a566bfc5 | -14.86281 | -59.63304 | 2025-10-24 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f68c8947-68c4-3d5f-bdf6-f2a83d91610a | -13.28734 | -47.48644 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a852ffe-b7f5-311c-911c-0d9a847abe7c | -12.03416 | -46.91918 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c12f0b73-5f39-3518-ae16-0dbb5df21e05 | -12.9468 | -47.70059 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26c7d3a2-88fd-3eeb-8689-71629fc54bdd | -12.05571 | -46.42545 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| edc1800b-b9c3-359e-b934-0446be59333a | -14.50325 | -57.34634 | 2025-10-24 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4b7c19c-bcbf-35b2-a607-ae8b5896be28 | -13.93178 | -49.40617 | 2025-10-24 04:40:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b43cabe7-b924-3b0b-84bb-ca726d8774a4 | -12.81006 | -48.63063 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69e30e9a-2594-3bbf-8cec-92efce6877c1 | -12.36559 | -51.47482 | 2025-10-24 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb699a02-e415-30fb-b6fa-7eb52b99a897 | -15.86907 | -45.25789 | 2025-10-24 04:40:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b169b846-e3de-3b58-9566-112992486dec | -12.0329 | -46.92781 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9038286d-3ee2-34a5-b96f-aef2c37ed712 | -12.24972 | -47.45948 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af866302-939e-30a3-9033-74c594c954d0 | -16.5037 | -51.47608 | 2025-10-24 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70e9de76-b05f-3862-acd4-77f7d1ed1f3b | -13.72686 | -51.46374 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee3f455b-c95f-3d2a-b50d-6c17626a4682 | -13.18481 | -48.48761 | 2025-10-24 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14ae9ff0-cd11-3222-b680-7052e29a713e | -12.25092 | -47.45132 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f39ac8c5-b481-32b9-b6ad-61cce26443d4 | -15.16754 | -51.26875 | 2025-10-24 04:40:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a6db57d-39ec-31fc-be48-b58bd2ea2b0c | -14.02484 | -48.0088 | 2025-10-24 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 059df5eb-e59c-3eea-a249-67cbdc54351a | -13.2991 | -47.45623 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3971c52-7e66-3fa1-b263-f6d6b9760cf8 | -10.84791 | -48.96532 | 2025-10-24 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c96939c9-881c-382f-8cc5-ba5759885c16 | -12.82406 | -50.94398 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 409c37c7-0c90-3d9e-bfba-dfdb0fe11671 | -13.9232 | -50.25874 | 2025-10-24 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38032168-5332-3077-8ed7-d2aa7b4dfc05 | -12.67361 | -48.62907 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d73a800-76ab-3da8-93d4-90adb97b1df3 | -16.08282 | -51.40976 | 2025-10-24 04:40:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7df51365-47ac-32c4-9f41-2a9836f0e181 | -12.24912 | -47.46361 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 555f655c-9ed8-3a5a-ba4f-243d314cab6b | -13.36769 | -50.46799 | 2025-10-24 04:40:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d83c405a-18dc-35c6-9b02-29f8b464f4d6 | -11.3251 | -54.26298 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e62c717-c84c-336d-a5c3-ebe513428845 | -13.27382 | -47.98454 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c354ec87-49e0-33a0-95f6-4a910482e8f6 | -12.37006 | -51.46825 | 2025-10-24 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee32e117-4acd-371d-8041-8eb0ead4c852 | -13.52883 | -55.65479 | 2025-10-24 04:40:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e736d7-365e-3467-86db-b62f00b059fb | -17.65627 | -46.66766 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5d41a0a-cbc4-3165-ac0c-a16a7093709c | -18.46594 | -44.44792 | 2025-10-24 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0562e8b-cb02-340e-8525-3e979b08b1b3 | -13.12481 | -48.58124 | 2025-10-24 04:40:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52337168-6906-3ca6-a29e-50442274d981 | -15.94509 | -51.0531 | 2025-10-24 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1129efe3-3300-396b-9c88-b2203ee09d5b | -15.8359 | -49.09799 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7513d910-a4e2-3a94-93af-d62357d8fc63 | -12.94575 | -47.63151 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47ea5d68-9437-3478-b2c2-d1734894598f | -13.29848 | -47.46057 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f4569b8-9e03-3568-aee4-9919f7a8d6fb | -14.92102 | -48.14175 | 2025-10-24 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35c1baf8-c4f0-3021-bd69-7e38d6f9d85c | -12.28638 | -47.4609 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39535542-1c5a-3eaf-a0e7-081a57ff9680 | -12.67305 | -48.63285 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34b36a1a-8f27-3a93-9d0c-384f03142bb1 | -12.22415 | -43.30841 | 2025-10-24 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21fc4e0f-cd30-38c9-b275-b414c78bdf62 | -12.06899 | -46.44128 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d399d42c-3d85-3a25-b739-a5f316d47034 | -11.35543 | -45.94643 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35d9bf75-fc6b-376b-a7dc-24423e7130e6 | -9.75615 | -55.34243 | 2025-10-24 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5611d7b1-d2ef-3fe5-9e51-6457efbb87e4 | -13.89606 | -48.34605 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e75d9246-5fd9-3c91-aaa7-bc2f22c84901 | -12.67768 | -48.64908 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 671e942b-b088-3d91-98d4-13473b6cc771 | -12.81246 | -50.95292 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20263c21-91d0-3e66-a641-d2d677da43d3 | -12.67017 | -48.62852 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81c71f0d-ebe8-3a98-b4bd-294b1cab7f84 | -14.77254 | -44.97098 | 2025-10-24 04:40:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1220eec8-5318-3714-af3b-9bece5f0b85f | -9.97225 | -54.20436 | 2025-10-24 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63887516-5a76-35a1-b02b-e56b38ef2ca8 | -13.33079 | -47.96325 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235f8fdb-30fe-3819-a4e0-8ce0b8bdd0a2 | -16.99535 | -51.48066 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4bbcb098-5cd6-3fb9-b8c9-a052a3a7de94 | -12.82075 | -50.94344 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2651549-5206-38d5-9af8-7c5c27feec47 | -12.66674 | -48.62794 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0cbc76f-d9f3-34cb-9afe-4a28d050a358 | -13.35506 | -47.97147 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8662ae3-9b73-3b09-a50b-c79c1c3612cf | -13.92265 | -50.26232 | 2025-10-24 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3dbc7ee-4e7f-3c0d-893c-a935d3004676 | -13.88015 | -48.37733 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6312cc40-58c4-34bb-ac2e-402cac989079 | -15.49946 | -50.445 | 2025-10-24 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1862f509-fd45-3a7e-b863-825dfa0733d3 | -11.35473 | -45.95137 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b226573-c247-3d51-9731-cbb07c27ac4b | -11.36844 | -45.93851 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30f4ebd4-31f1-36fe-887f-fba197d516a1 | -15.83937 | -49.09855 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bad13f8b-8184-36c9-926e-df3960d29900 | -11.46044 | -43.70771 | 2025-10-24 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5c4d5b1-9b74-332d-865a-228665df0756 | -15.844 | -49.0913 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 767338a5-f808-3622-a0bf-e414c3ba2730 | -16.82184 | -45.70819 | 2025-10-24 04:40:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f462b32-d982-30fa-bb60-33251048e973 | -12.07371 | -46.40828 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fade50ac-65b7-3397-9e01-0ad30902007c | -11.0098 | -47.88003 | 2025-10-24 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c23e1321-382f-3d89-8609-1b3285d7169a | -14.77095 | -49.29516 | 2025-10-24 04:40:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0063c9ff-1b3e-3bf5-8b6e-584fd6cd2e6f | -10.59365 | -49.64053 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e123108-6a79-327e-91a1-c3ad3af78419 | -13.88425 | -48.37393 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcf3ba2e-dc2d-305a-87ab-f1aa0184d664 | -15.95267 | -49.60396 | 2025-10-24 04:40:00 | NOAA-20 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b766555-bd46-3a29-8020-f85c00eaf5bf | -15.31075 | -46.89051 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f8a6f0a-599f-3d62-aa78-6007c8843cf8 | -10.54302 | -54.87025 | 2025-10-24 04:40:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 671b4544-db77-3015-aba8-0cfa1cb66907 | -12.80556 | -48.66081 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfec918e-a845-33cf-9845-febf0f475eb8 | -11.04388 | -47.89894 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a1f03b4-37f4-3b55-aaf0-5e86e55a2698 | -15.49341 | -45.98749 | 2025-10-24 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1869b991-4bfa-38a4-a82b-12d00e3b686a | -12.06024 | -46.42088 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fff301cf-a70c-34da-868a-c71255b0b10e | -11.3382 | -56.20871 | 2025-10-24 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a9b87a5-954b-383f-909f-ae233253390a | -12.38876 | -57.52729 | 2025-10-24 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9012997-4498-30df-8be1-9f63adcd3f5e | -11.98846 | -43.3227 | 2025-10-24 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75aae65c-9b67-3495-ba8f-c41643da5d68 | -12.39898 | -54.16346 | 2025-10-24 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccd21298-75ba-3483-bec7-e739274812e1 | -11.03078 | -47.90659 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc0a82ac-3ffd-3ff4-b9db-4f733609b313 | -12.29328 | -45.52973 | 2025-10-24 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42339b0d-bdab-3ee6-b4a0-65ed83284a8c | -16.54813 | -46.43707 | 2025-10-24 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcc13744-cbbe-3e60-939e-298797ca33ae | -12.78479 | -48.56308 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e822ec3-df00-3ccd-a982-c9833628631e | -12.07617 | -46.41825 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38464ced-673b-3463-b4be-aabee53d814b | -11.51565 | -47.22171 | 2025-10-24 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48586193-f1c7-3713-a420-c18d8645338b | -12.83007 | -48.63823 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa51d386-6802-323c-9626-13812e20a28b | -17.01961 | -55.90888 | 2025-10-24 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5b95c29d-85a0-35b2-9cc0-0d1b21d7092d | -12.06609 | -46.40717 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9ccb45e-cfbf-378d-8c0f-b73dfafeb611 | -16.1293 | -54.00862 | 2025-10-24 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4888b3e-570f-3a96-907e-19c02732747c | -11.34053 | -47.64981 | 2025-10-24 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 739840ee-8998-38f5-8a14-cfe31faf0267 | -17.0192 | -55.91104 | 2025-10-24 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b2b984bf-1e01-39c1-b4b6-7b3329f4a958 | -17.39203 | -49.17541 | 2025-10-24 04:40:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 691e7211-2ff5-3140-a5a2-5c608c6d3560 | -11.00921 | -47.88391 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05e7fca7-f17f-3b3e-9998-92bdae7c09ca | -13.21952 | -47.75473 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cc347a3-5ac4-3dc2-b218-71926b15479d | -13.8966 | -48.3921 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a2ceb2a-b69e-35b3-869b-1ae71bcd26b0 | -11.36319 | -45.94761 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
