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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2934112b-15a0-357b-a71c-0caf93a01c36 | -6.53854 | -39.51271 | 2026-10-05 16:37:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 154ac4f9-b4d9-3084-8903-064efb059538 | -7.4016 | -40.22149 | 2026-10-05 16:37:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 514fb1a2-ea96-36cb-a182-190cba304f01 | -11.02668 | -41.27705 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a3f7cef3-776b-34cf-a175-b93aefe9f63c | -7.17252 | -41.99836 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 1e65eded-5009-3da9-915d-ab3693e20839 | -9.85031 | -44.78059 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1254535d-40e4-314a-a81a-ca645bc2b101 | -11.08165 | -41.25675 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1801b052-2e1b-369d-b3de-8f1f60d6202c | -8.70626 | -45.80673 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 04eca1bd-a3df-3c6a-9c39-b93302e34e1d | -12.81796 | -43.29472 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a721d4a7-d194-3170-8995-38f4272e89af | -10.39729 | -47.53165 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80709942-0476-3933-b232-e959353575a9 | -6.37682 | -43.63458 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4b020955-628e-3713-b2f4-850796c420fd | -11.43613 | -47.68834 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9edaf379-75de-327c-b397-c2804607a61c | -5.68721 | -36.71365 | 2026-10-05 16:37:00 | NOAA-21 | ANGICOS | RIO GRANDE DO NORTE | Brasil | 2400802 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c521cdc6-b8a5-37fc-a4c8-0cea9abf5c82 | -6.61426 | -41.77001 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 846047a0-ad5e-30ac-8e87-f60b3ae23c25 | -11.63987 | -43.63683 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 922f6f2b-4760-37c3-acf2-b61eec21578e | -9.84749 | -44.78496 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f3019ae6-9ebd-359f-a239-c1bdfe4cd762 | -12.053 | -43.43279 | 2026-10-05 16:37:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1fce927c-d1fa-31f8-b67a-f06be2e0fbbc | -9.02839 | -45.15408 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca426a50-1680-3899-b36a-85b459b31255 | -6.70635 | -45.22966 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| cf26b44a-cebd-3024-b84a-d3c661b90e64 | -7.40242 | -40.22632 | 2026-10-05 16:37:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 0eaf1381-24d4-3231-9530-8d1f9f2850ac | -8.52992 | -54.58219 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 97a127a5-49e0-3516-a119-b25691576c62 | -7.84732 | -46.8924 | 2026-10-05 16:37:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1e0eabe-9051-3145-85d0-2831d5983a7b | -10.7434 | -39.39281 | 2026-10-05 16:37:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 48b5ec09-42f7-3a2a-b6d6-a39d38d20cef | -11.82223 | -47.36331 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 0c17351e-8335-3705-8f84-bf8a99539b7a | -6.5945 | -41.57446 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8837aeb5-9db8-3529-9642-a80ae6aebcbe | -11.68317 | -43.65853 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 421c734d-6333-3720-88f5-e3c1d433552a | -10.23189 | -46.66019 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 519e5a6d-0d97-3914-8aad-c3786750c763 | -10.11755 | -45.89581 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 15509f7d-af1a-3e4f-aef8-ac2e2ba6c191 | -7.22537 | -39.27731 | 2026-10-05 16:37:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5f368e05-5d58-340b-bba3-8f38ba937e6f | -8.56021 | -54.58546 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a9f11ef8-97eb-3aae-8b7d-9de8652c4ad1 | -8.52921 | -54.57709 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 836ae30d-16b6-3a44-8c73-7952eefc2698 | -11.34235 | -46.6788 | 2026-10-05 16:37:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc36c5c5-5fd2-31f1-9032-ef161c44678f | -11.09566 | -41.26569 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6551dff4-a4c4-36a6-84c9-c35ea6ae3d10 | -7.39306 | -45.60429 | 2026-10-05 16:37:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5efca661-0bd6-366d-9ead-c4cbf9bcbe31 | -9.81839 | -44.80087 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 15a024c9-f5f7-3670-a3d1-b4ff3380e571 | -10.12088 | -45.89529 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a2ea1406-5808-3234-addf-789887eeed0d | -12.26736 | -40.68059 | 2026-10-05 16:37:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1a96ea56-31fe-33e5-af23-7af2fc29de11 | -10.95104 | -45.41727 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c57b087d-f6fb-30a4-b84f-537b723daeab | -11.73959 | -43.42473 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2650f393-590f-3f84-a2d1-c1ce8a6702b7 | -7.39249 | -45.60061 | 2026-10-05 16:37:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9ca8b89-7627-368e-b6f9-63198a766ea5 | -7.49618 | -44.42167 | 2026-10-05 16:37:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6da6aa44-8813-3c41-9421-4020f9c1a2c9 | -11.74467 | -47.71106 | 2026-10-05 16:37:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc66c503-6715-32ee-b69f-fef487c32724 | -9.02734 | -45.16948 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 692fc907-de1f-361e-9905-baaaa5afd137 | -9.03519 | -45.15297 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f2bb778a-e47c-3c08-8d4a-f0404be48f10 | -11.26982 | -45.23627 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a661bd03-5b14-33a3-ba86-7253b3babf60 | -19.12629 | -41.07111 | 2026-10-05 16:37:00 | NOAA-21 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| cbb69153-7ba9-35f0-9177-a50ff8ebff44 | -11.82672 | -43.53644 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a362dc39-d88a-392a-96bc-eeddee358e41 | -11.07779 | -47.49438 | 2026-10-05 16:37:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5a3e3a-492a-33fe-86fd-19a57d8a2ad6 | -7.4843 | -42.80141 | 2026-10-05 16:37:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 5ef402c9-01be-35f4-afb3-aa5903761502 | -7.21777 | -46.05224 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0cb2ae41-e3c3-32cd-aa70-42337557b4aa | -14.11865 | -43.89166 | 2026-10-05 16:37:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ca26c7b-70ce-3049-b185-68cc500035b0 | -11.73248 | -43.42592 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db75fc5c-0291-3052-ba39-7a3f5b54d5f3 | -8.33354 | -49.688 | 2026-10-05 16:37:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff70470d-5f30-31a8-8547-4892980c5a5e | -6.33768 | -42.53724 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 32b17f4e-ad88-3c93-b7ca-ba9b6d54e68d | -9.84529 | -44.79314 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 22fa4545-1c2b-3696-95e9-d6a1815d7ab5 | -11.65356 | -43.60967 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| df925f4f-b1d2-37ed-8c6c-9f5f07b914d6 | -9.02498 | -45.15462 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 499e6a01-1deb-389c-bc13-21997e10b0bc | -9.79685 | -47.78518 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5dac900-f223-3153-985e-42701e4fe79a | -6.42496 | -43.7127 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 07fffd55-997f-3965-a59b-ebf24a3310fd | -10.18944 | -52.56236 | 2026-10-05 16:37:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3cd819ea-2bf8-3554-a89d-534fec2cb72f | -11.80888 | -47.36537 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2c1e406b-045e-34b7-89d9-ff2cc6996648 | -12.50635 | -41.21057 | 2026-10-05 16:37:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| efb40a4e-0168-33ee-9086-6bfde98b5e44 | -9.77384 | -53.832 | 2026-10-05 16:37:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d4c34ecf-57d6-364b-a217-53ce87d5c7d5 | -7.10235 | -42.53542 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c0bf62c1-49ce-38bc-8369-d515dd7ea1ac | -7.16924 | -45.58679 | 2026-10-05 16:37:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eb11f4e6-e32a-3ec4-9214-e7da77b74b27 | -11.46248 | -43.39773 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4c588336-1770-3ab9-bae9-28858f3337e4 | -9.87342 | -44.81553 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 50b67985-9525-3b7c-b351-0ad57c17f6aa | -6.85664 | -38.68338 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1bb6c889-c18e-398c-9fbf-7f276ea91c1a | -11.807 | -43.52696 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 85d986d5-ed9c-3799-b657-6856d321d731 | -11.01919 | -41.28199 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 13bb7be5-5e5e-392b-ba71-0f15b2783c01 | -9.09124 | -46.51496 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3787fa4f-61e8-3839-967e-96d9b212fdbd | -6.72535 | -44.27327 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 07a2d7aa-5ab3-3be1-ae29-6d8e2f148c76 | -6.60013 | -41.58184 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| efa1bd2f-4805-3e51-87e4-fde0028e998d | -11.74381 | -43.42823 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f6e90b30-59b7-3804-a52c-14c4a861e495 | -8.42017 | -46.94636 | 2026-10-05 16:37:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98e09eb5-def2-3308-a8b5-ef1ab40ae38d | -6.89509 | -43.66982 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e3cde539-e088-3b03-8a5b-5f4a492144f1 | -7.23859 | -44.01356 | 2026-10-05 16:37:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e66dcd6-6dd0-38d9-bd0b-cf74d9572670 | -12.24603 | -42.11133 | 2026-10-05 16:37:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| b8e0dd76-3f6b-3bf9-8ebc-388a8a3672aa | -11.83095 | -43.54012 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d5184360-1427-3965-be27-59f46a0de1ae | -7.55226 | -46.7186 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb909d0c-4768-3298-bcbc-0625575e29e4 | -11.45657 | -47.73338 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2905647b-082c-3e04-9a79-c90b11095915 | -11.85409 | -47.3066 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 278b0967-4622-3141-ac36-8924cdaaba92 | -14.31661 | -46.49176 | 2026-10-05 16:37:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 299762bb-2bc4-33ed-8821-51de81b4eefa | -9.40191 | -40.32138 | 2026-10-05 16:37:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 0cbd480b-c204-3b70-b41a-92d765147ebc | -10.49596 | -46.03345 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7a87013c-dade-3015-9450-532e3acc8a6b | -6.88533 | -43.68055 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 821dfb28-0663-308c-922d-03aa1c715ed3 | -6.37307 | -43.6352 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9860a2e8-d42b-3970-aef3-c697ee63579a | -8.43396 | -39.54672 | 2026-10-05 16:37:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 0dfd8e9e-a3fd-32a1-bbdc-db28fe32e6bf | -11.01172 | -47.87197 | 2026-10-05 16:37:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21cba8da-bb26-34e4-ab43-5d9edaed5ef1 | -6.89422 | -43.68833 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 67aaa8f8-6f2a-3a5e-8a2c-749f2ec3a1f1 | -13.20758 | -40.45686 | 2026-10-05 16:37:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bbbd4ed4-b603-3432-b305-7bd86262ffae | -9.84126 | -44.78992 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c9c99a69-150c-3b80-84f8-6d1f5e5c568f | -9.0278 | -45.15036 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5311bf7-7ec9-3268-a65a-b8383dfc507d | -17.94027 | -39.47982 | 2026-10-05 16:37:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9c867263-7c8f-33a3-8e25-e49664308b80 | -9.04199 | -45.15183 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b018f432-342f-3ea7-974c-d6569070993a | -13.04561 | -41.03983 | 2026-10-05 16:37:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6d360967-8742-3aa8-83ec-891596cd3aa7 | -11.23914 | -45.25959 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3a398563-2c49-33ec-b4f1-31d148626097 | -18.12398 | -42.93973 | 2026-10-05 16:37:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b053cf54-0a9d-394c-8ca8-2ab27237c9a7 | -9.91524 | -47.69034 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a1754e9a-e722-3f1b-a324-30c5620fb4aa | -11.26199 | -45.23011 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 96dcf5c5-3a93-3253-9961-7af21f49b32b | -9.91471 | -47.68679 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README87.md)
