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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04904336-1165-3649-9606-d6d6b4c157c9 | -4.12936 | -56.22347 | 2024-10-29 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72012990-07a0-365f-816e-b0a9139fb6fe | -4.10242 | -55.49939 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c9eed25-7f91-3faa-9dd3-75ea335a1d8b | -3.91818 | -55.38549 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 713f280c-c6c1-320c-91a8-be6977596fa1 | -3.76991 | -55.96935 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3e97a2c-5fe2-3c9f-a4e1-bc11a3fe7436 | -4.85766 | -55.89269 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b6cf13a-a420-3cf8-b0c5-4bf503abe48c | -4.73584 | -56.05374 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 11f2d026-30a7-340f-ae05-f8888f14f7c0 | -4.21114 | -55.46949 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3210836-de35-3ceb-a2ba-fc922154ff65 | -4.1272 | -56.22025 | 2024-10-29 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714e4b3e-ff57-31e8-a196-79fc789da0df | -4.10316 | -55.49492 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a6dbcbd-9cbf-32a1-8665-150b19fee09c | -4.09867 | -55.49429 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7f38f80-a355-3fc4-919d-80ef1409665f | -4.08446 | -56.31957 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abda2aad-71e1-3fd5-9cbc-a2708193f3e6 | -3.84496 | -55.7179 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bb7277c-7474-3563-8ab5-45d900d0366d | -6.33233 | -56.05806 | 2024-10-29 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286543d0-2cd5-360e-af46-816758e06439 | -5.30606 | -55.83564 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bd1809d-99be-36dd-9fbb-ab7a1b1fda2d | -5.30528 | -55.84018 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbf67833-9464-37df-b1f5-9985fa9f87a2 | -6.33681 | -56.05885 | 2024-10-29 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a97ed73-fe66-3712-a04d-2bc78620268e | -6.33512 | -56.05661 | 2024-10-29 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6418286a-5c6d-33d7-990a-de540f6d5d15 | -5.3076 | -55.82663 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e727d17-e6a9-3f55-855d-1feed9ccccfd | -5.30683 | -55.83112 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 015f9417-a14c-3b07-8742-0ee399e94f9c | -5.30313 | -55.8258 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6a1bd3d-0650-3876-84f9-4ec813a0d121 | -5.30236 | -55.8303 | 2024-10-29 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f7de80f-be74-3e1c-b404-109e1929b339 | -9.36777 | -56.83308 | 2024-10-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9358e578-2b95-3e6e-92f2-1d3a1d3b84a7 | -9.74206 | -56.97956 | 2024-10-29 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c93008f-a0e5-345f-918c-0e9c0432c3cf | -10.26057 | -56.75699 | 2024-10-29 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d969883-389e-30f3-80da-8841535711e9 | -3.55496 | -57.68679 | 2024-10-29 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edd28ff8-477f-3ebf-a750-d05d2b88fb14 | -3.56074 | -57.68442 | 2024-10-29 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a9ee1c-f9f0-3d6f-a6f3-244f788924d3 | -3.56322 | -58.69334 | 2024-10-29 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2730ccfd-a101-3de5-ad19-ca414844e07e | -3.56259 | -58.69711 | 2024-10-29 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e2afe18-cb61-380d-bdb4-68144f665b0e | -3.54766 | -58.68313 | 2024-10-29 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 705bdd30-5c69-3062-a042-199e2589bb84 | -3.54829 | -58.67939 | 2024-10-29 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8e18f71-76a3-34a6-9d61-b82c5f6b12d6 | -3.43803 | -59.25522 | 2024-10-29 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 899dd62d-6031-3ed5-bbbf-bf9b251b3572 | -13.89099 | -43.97345 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e0758e8-5d18-343f-971a-c40707e96bae | -13.25791 | -48.24167 | 2024-10-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ee2541a-5a5b-3df9-8a45-2c7ea438ab9f | -13.33512 | -41.80069 | 2024-10-29 04:42:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 1f789133-7cc8-38d7-8610-90ae921aef67 | -13.3347 | -41.80409 | 2024-10-29 04:42:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| f54d47df-217d-373d-9f0c-d987ac7247f5 | -15.93143 | -41.97701 | 2024-10-29 04:42:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca528fad-07de-3b50-b9b8-1f31cddbd136 | -15.92565 | -41.97958 | 2024-10-29 04:42:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e28dd7e0-6b91-359d-ae9f-af4fd5042daa | -15.92527 | -41.9831 | 2024-10-29 04:42:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c8d3aac-a08e-3fdd-9bd6-983c1e0f2f12 | -14.19626 | -43.7256 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c860dfa8-0614-3b25-95f1-b02a12cde75f | -13.55606 | -43.4184 | 2024-10-29 04:42:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ce55dc-b063-3442-b351-ff07e9a3b076 | -13.55539 | -43.42361 | 2024-10-29 04:42:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feb41321-a68c-355e-add4-f818de9ce961 | -14.94815 | -43.35235 | 2024-10-29 04:42:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a4d3e24-94c6-33f5-8d33-04d6f641ee2c | -14.47939 | -43.35879 | 2024-10-29 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2037d15b-c6af-35c9-b847-569cd8a063fb | -15.45 | -43.62973 | 2024-10-29 04:42:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bca5f17-9149-3d5b-9b62-58419fc06397 | -15.44517 | -43.62912 | 2024-10-29 04:42:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d791555-e19c-34db-8db9-7322d8a1d527 | -13.73111 | -44.05613 | 2024-10-29 04:42:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d85b523c-e0c3-3682-b8b5-3216e6c8926b | -13.66984 | -44.05925 | 2024-10-29 04:42:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9be73544-2f63-32de-b6aa-2b6b6923d365 | -13.46824 | -44.4366 | 2024-10-29 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cebbddb-3dc0-3948-8d74-b8452f6b3c51 | -13.39911 | -44.41971 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0483fcda-50b8-3817-b26d-97e142bb93e9 | -13.39469 | -44.41894 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102ce04d-9bed-3110-83c4-267c60f742c4 | -13.30221 | -43.57439 | 2024-10-29 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a54f736-55f6-3c43-bd1d-ff75f4563bb8 | -13.17144 | -44.05286 | 2024-10-29 04:42:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 597ad6be-b2d0-3c0b-bf78-186fc190f453 | -13.17085 | -44.05756 | 2024-10-29 04:42:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 719dc20c-180a-308f-8713-4bc08af7407b | -13.16959 | -44.05618 | 2024-10-29 04:42:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 619bfb41-0d9b-38c8-8b43-dfccb1139434 | -13.01005 | -44.10245 | 2024-10-29 04:42:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dbb4deb-6912-3d88-98f3-d1bea2c6e2d0 | -12.8898 | -44.61541 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e0a58b5-15f4-3bdf-b503-68cbdb6359e1 | -12.88926 | -44.61965 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a84c0ae4-2050-354c-9d48-c174f12d3274 | -12.88798 | -44.61755 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 882d1c64-1cba-3302-a7b3-f8e53aafe196 | -12.88436 | -44.62338 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fb2b3b2-7482-3328-a334-81391b1fa2b0 | -12.88246 | -44.62558 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c98d45c-4007-3648-b851-59a7b94d72cb | -12.87811 | -44.625 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ace5f18-0575-3611-9ff9-03d73639b5c8 | -12.87263 | -44.63284 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e19bafe3-bf8c-3f64-b4c6-5a55dd864831 | -12.86188 | -44.61409 | 2024-10-29 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa5897bc-b06b-3289-b6a2-956e94c66986 | -12.66832 | -43.81857 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d7220130-1a4b-32d5-9235-ce26fba528f5 | -12.66821 | -43.81713 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e8d8b08-d85c-3018-a5a6-5fad1e2650a5 | -12.66772 | -43.82335 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 400a0acd-9d7f-35ff-aa44-2931b26e1ed7 | -12.66757 | -43.8219 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 808f1c0a-5bd6-3440-ae92-842980df7f06 | -12.66694 | -43.82667 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ba65d92-202a-3205-a575-6e53d656f531 | -12.66374 | -43.81791 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f9755b4a-52ad-3200-9908-3e30d2775074 | -12.66364 | -43.81649 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 38c492f0-3381-3cf3-a808-4fc59488e937 | -12.66315 | -43.82269 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 36a064aa-5ee9-34b5-9d10-72dc349e77c3 | -12.663 | -43.82125 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0d5de229-cba9-3780-80e9-8496ec960ebe | -12.66237 | -43.82602 | 2024-10-29 04:42:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d478f45-f41d-307f-bdc7-1e0a7e65010b | -14.87709 | -44.11498 | 2024-10-29 04:42:00 | NOAA-21 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 218be7ae-0842-3fe7-8342-e513117953d1 | -14.59711 | -44.2606 | 2024-10-29 04:42:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 669280e7-9eac-39a6-bba2-b12b041f3ce7 | -14.5965 | -44.26544 | 2024-10-29 04:42:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88e49345-fbb5-35e4-af36-cc0daca9c493 | -14.59192 | -44.265 | 2024-10-29 04:42:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1ae1a273-9c19-31ed-aa16-b68e5dd503f2 | -14.16633 | -44.65619 | 2024-10-29 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59b383c5-f6c0-323c-be1e-dddb5f1eab27 | -14.16576 | -44.66053 | 2024-10-29 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2d7edbc-b457-3608-9dcb-2394fd1b397c | -14.1487 | -44.07704 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ceaebe9c-c0fe-363e-8e58-cccc5c653f0d | -14.14837 | -44.07842 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 5f42db59-d7f7-3da5-9261-5274666da0d0 | -14.14807 | -44.08187 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 114f7827-8188-3a46-a79f-e98ee7db5083 | -14.14411 | -44.07642 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a77a6300-4941-3727-b116-fef84ed6c0ba | -14.14378 | -44.07779 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| c145f7f8-e6be-3cb6-b601-90547f2da377 | -14.14348 | -44.08124 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f2a6f765-e01f-3764-aac5-4ca7b6536fc8 | -14.14319 | -44.08262 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 6325573e-5704-3742-aed4-26870288c05d | -14.13951 | -44.07581 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2ab306a8-1b99-3a81-912f-2468efe75408 | -14.13919 | -44.07716 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaba2a30-38f0-32a6-bf93-3e38b3b1ef70 | -14.13889 | -44.08061 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8da20391-c0db-3e79-92fa-8c295b249440 | -14.13233 | -44.35639 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 05c5f8b0-0d62-3c8a-996e-00fa8a6b63e8 | -14.13174 | -44.36103 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c1a1423-1d76-32d5-880b-5aae6d7a8406 | -14.12784 | -44.35566 | 2024-10-29 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c719494e-3d63-3f7c-a151-e1efd5671639 | -13.99717 | -44.0192 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76688b72-c51e-3980-a790-e486c4329ffd | -13.88638 | -43.97282 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| af4c5771-d7e4-3f75-992b-cca932382257 | -13.86153 | -43.98423 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0d4d719-4e80-3d9f-ad91-d5fffd3a8dfc | -13.85753 | -43.97872 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df8757f0-4537-3fa0-ac3f-98d847bd52c3 | -13.85693 | -43.98359 | 2024-10-29 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90083714-6b7f-3f33-b73e-3ae69d152887 | -14.16357 | -46.15503 | 2024-10-29 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72d580d6-5a85-3911-a280-205ce2143788 | -13.69967 | -46.12069 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1611d144-d6f4-3afb-872c-894be95c25db | -13.69919 | -46.12421 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README67.md)
