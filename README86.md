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
| ab4655d8-b380-363a-a6a4-ce33b2c57f4d | -8.49211 | -57.61753 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cc46f64-8c43-3591-903a-f8e46c414758 | -5.81501 | -57.74006 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db203cf-068a-3acb-a8b8-c0abef88cb8b | -10.9155 | -53.94171 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c484f95b-01b8-331c-8b1f-6be44ae8c9f9 | -10.29228 | -50.53167 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4be8317-2209-3bd7-984b-b86508053e4a | -5.89113 | -52.09288 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c91d1ede-3c13-31c6-9220-fe88c3976201 | -5.82674 | -52.02933 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b059b211-28e5-3cf0-a9e3-77c463a15d59 | -6.15584 | -57.95596 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ef61947-953e-31d7-bbd5-299d71afd412 | -8.34901 | -50.86209 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1012500d-6cd8-37de-948b-b06b753469f7 | -6.26271 | -50.80782 | 2026-09-23 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bfe45b2-963b-34d4-be7a-845183a62156 | -11.66648 | -50.97985 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d27660d2-ae08-37ac-854e-fd8130e3c462 | -6.61065 | -43.74445 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aefffbb8-4962-311c-8a25-1399c50b37fa | -6.61282 | -59.96478 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7499739-1a7a-3ac7-a386-7fd2d4a0fbb7 | -6.23794 | -51.01063 | 2026-09-23 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec0dd369-a04e-3f91-9d02-4af0921427fd | -8.85529 | -62.41944 | 2026-09-23 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fb8a22d-be65-345f-929b-b0e39f5c828f | -7.56053 | -57.67002 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db71db52-c192-3d20-af10-a824d9a939b0 | -6.15985 | -57.70787 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc2a97e6-13a3-347b-9ecd-e7c1cafd0e24 | -8.92422 | -61.49191 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e96a2b2-c187-36ba-b7bc-09a8238540ea | -5.80623 | -57.74212 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76f40a97-a3ad-30cb-b193-f6077576bb6e | -6.34516 | -57.77404 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5ae251c-c8a9-3d2d-bdbb-673dc9d8a936 | -9.5928 | -48.45692 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5cb1be8-7663-3e6b-82b8-6306575986e4 | -5.57406 | -52.02121 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebbb7c0-a3b4-3e17-b971-1c786260ca24 | -8.28667 | -54.77359 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 353c3c05-b760-36ed-b9b5-e6363cf9fba2 | -9.16334 | -61.36672 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62e01792-b022-3649-97fc-5bcc7020406c | -11.95366 | -50.0787 | 2026-09-23 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96658993-6561-3b2d-a67c-d7e645434f0e | -10.91105 | -53.94821 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4358da20-99f1-3aa5-827d-d82ba168e1c1 | -6.28531 | -52.95613 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 173694be-f848-37b0-8d29-8b2e982e9848 | -5.80422 | -49.15107 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c3d1c06-d9b4-3b20-8080-a035ea1359a1 | -10.54326 | -43.98073 | 2026-09-23 05:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85c7dcdd-9177-3a6d-8858-c156d26dce4b | -6.18599 | -52.79795 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d562385-26bb-3ab6-9113-821bca381650 | -3.6581 | -54.26587 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf833e3f-b8a7-3e19-8dcf-de736ab45041 | -4.55948 | -54.93949 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b23dddd8-c215-3a00-8fd5-bdbd77b13b6c | -8.4857 | -46.86762 | 2026-09-23 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16431a78-2387-3506-b6b3-42fa23c0f166 | -10.25128 | -50.20933 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 396e8d59-3cfc-3567-9f83-705ddfe6c15d | -7.13435 | -43.07532 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6889c8c-a554-3a80-a1c6-073f76cf7c56 | -6.65278 | -59.93074 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae64814b-a4c1-3fed-9e5d-1fce4d630177 | -5.98158 | -57.783 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289093ad-ae11-3dc2-8f62-8cf697b2a6e3 | -4.0918 | -62.09727 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e0508953-5d62-3c28-9265-33d58d4b3687 | -6.78094 | -59.62712 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7efeca86-14da-3de6-a762-48d236ddfa59 | -5.8739 | -52.07233 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbe005c7-3ed6-3acc-923f-138efb1b88af | -6.45598 | -59.99064 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38fb5cdc-46f6-3d34-9180-03b59c1a871d | -4.25832 | -60.01165 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ccdcdbcd-bc23-323e-b6d8-d96be0b59049 | -7.31716 | -42.26028 | 2026-09-23 05:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5fdcb691-d16f-3e86-a8ac-bd8b339dc637 | -5.62042 | -45.24606 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 67866a93-3298-308b-859c-cca900417c17 | -5.80289 | -53.51929 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc1e9d4d-dd6c-34b6-ba7f-0780e6afc536 | -5.60693 | -45.94386 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a683ff60-7ab4-3323-891a-9be7f436e1c2 | -6.63241 | -59.93075 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0db65caf-4f0a-30f3-81b7-6af2b1a05275 | -6.48894 | -57.87985 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac45ca7c-67b1-3f39-91a1-450df06a1ad4 | -10.28336 | -50.51763 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc6de7b2-afa9-316e-bf6d-309918e2e4ae | -6.61063 | -59.91656 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 300eeb3b-aee2-3851-9f82-179cd9920d08 | -10.29352 | -50.5234 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464f4f12-8b25-340a-b5a8-2fd280c2267c | -10.90603 | -53.95823 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e1ace70-a618-3e41-aa1f-3a76992dae67 | -10.28274 | -50.52176 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff193e5e-91c2-3114-8261-aae7ff2ce328 | -6.67826 | -58.5684 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98e0b85d-bbeb-3019-84c1-3c5b4931b9d2 | -6.75166 | -63.14165 | 2026-09-23 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90c809fd-623b-3c2e-ba9d-b09e76a7d99f | -6.61339 | -43.72486 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac744e49-d0b8-3017-b43a-9ec336d8c1ed | -8.09489 | -44.4273 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 861abbda-5170-3f52-aaa6-961eee60d527 | -6.64551 | -50.92622 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15dfb1e8-ae37-372b-98b1-ac18cf9c8608 | -3.90857 | -55.83656 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffc84691-cd22-30a3-8a2a-2c2e4b9f7dc5 | -5.12133 | -48.79899 | 2026-09-23 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 629c3686-4188-3ec5-9fdc-4903ffcdd37d | -8.17745 | -54.82093 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43290ba4-8a44-392f-b5c7-af16ff8595c5 | -4.41962 | -55.47249 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed0da93b-3998-32e5-a43e-3c0c74bfd03e | -9.26217 | -65.44184 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad7b526e-536c-3ef3-b6f9-2334667fb68a | -6.67865 | -55.06553 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b805ec46-d4cd-3203-a9bb-24d420c2b832 | -9.52303 | -45.39882 | 2026-09-23 05:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f9d8dc3-579a-3d3b-8330-d5f564e46d4d | -8.23289 | -54.67434 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0029d7a2-50f6-3623-888c-0b2f2904ed4b | -6.09343 | -55.55169 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2b0ffcd-d01d-3f98-988d-5336f716f90d | -3.46381 | -60.26075 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ccfec296-6276-3b77-a361-8898e9fd6c07 | -6.18898 | -45.31524 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3ee167b-30ad-3d3c-a163-2eb6bbddd3a0 | -5.87718 | -52.05149 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19711b48-464c-31f9-9216-e1e6b447f004 | -6.84546 | -45.5497 | 2026-09-23 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ab19d52-3b74-341c-992e-492652c302f7 | -5.41765 | -49.27032 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f942fbd-15f2-3a38-88a3-7cb8f99a9627 | -5.81792 | -52.06356 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99b62c1f-71cd-379f-aacc-e99f62bd6245 | -5.80865 | -57.74318 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 630147ef-15aa-3dcc-b0b7-e59c1ccffa22 | -7.13315 | -42.06032 | 2026-09-23 05:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0b6c493-4bdc-3f95-bdd1-ab3edd81fba1 | -6.94258 | -42.88288 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 64f75993-21c2-381a-b225-9f13f175be1b | -11.6418 | -50.93485 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 593800f4-1721-30df-aa09-071e9eefb1d5 | -9.24259 | -57.1573 | 2026-09-23 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e676702-1706-3969-99b9-8f21b58fce58 | -9.93515 | -48.46363 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20116fd9-b04c-328e-ac66-27a3cddc94cd | -6.73973 | -55.09151 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d038b26-409d-39ba-8ca3-a6a958a14293 | -6.09932 | -57.67602 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28095fe4-68ce-350c-8dc6-55be17e3f23a | -8.44575 | -55.01685 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 273508ba-25f0-3aad-ac29-3bd8b1bb9b09 | -10.88125 | -54.09163 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a1712ff-12c7-30a7-a942-1fa5829ba567 | -6.61156 | -43.73795 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 2dc32556-8091-34db-9d22-128dbf148b5e | -4.99989 | -49.47384 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cbb2102-7198-3331-aa83-356153fd9618 | -10.00468 | -45.21668 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1100097-9a0a-382e-a8e3-dbd7f4d87679 | -3.78232 | -60.75035 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2274f550-ad15-33d7-811d-6a03e1e46cfc | -10.24096 | -45.50238 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62bace28-01cf-3e5f-ba29-b64a525fb7d2 | -6.13251 | -59.9649 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94597d60-9f6b-3f44-90af-6dcfe7734489 | -9.59289 | -43.93349 | 2026-09-23 05:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f02520b6-6587-335b-97b1-8a66b93e18cb | -5.73058 | -52.2344 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10a376a6-4a95-3727-955c-ba54e61aa2bc | -7.31792 | -55.22136 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ee5c6ea-1ebf-3cfb-bd05-a648b2d5d3e0 | -6.98796 | -52.85747 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d78a3bb-cf16-33a4-9986-0afb160c00f7 | -3.9093 | -55.83207 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bb82072-fbe7-3912-a3ed-4d6984034b56 | -8.86343 | -50.18925 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70bb9d3b-94a1-3bb8-8055-aa0d0d3044e5 | -10.04919 | -50.21711 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4d19582-5471-3836-94b4-479f7bbdcd36 | -10.25428 | -50.21414 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b117903a-382a-3eb4-a5c9-189ce5fb23bb | -11.64118 | -50.93895 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02458862-1844-3748-b6cd-b43356da456f | -8.10042 | -44.42528 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d85f47c-3ef1-3bf3-bf72-63a093b03577 | -6.10279 | -57.68036 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22d6737d-ce43-39f8-9aaf-fa1a95ed3088 | -8.80905 | -44.26759 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README87.md)
