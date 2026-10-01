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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b7d36e3-9957-30b3-b513-f7c1d2e2e1b9 | -9.3881 | -49.1473 | 2026-10-01 13:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 0eecd3fb-b0a4-362c-baa7-60527c881a9d | -8.6259 | -45.3737 | 2026-10-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 8a188762-0080-3595-b7fc-5428551f3c81 | -9.8803 | -44.9553 | 2026-10-01 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 64d89790-2250-3619-8d38-6409b7436b79 | -14.3379 | -44.7605 | 2026-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 7c59ce02-6599-3dad-b0cd-3191da9b8f2b | -9.1154 | -49.9246 | 2026-10-01 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f0424b73-aa7c-3ec4-abe1-d79fdae83c08 | -11.6583 | -43.5662 | 2026-10-01 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| b6400153-f82e-3770-b28a-8194b9f07abb | -9.9026 | -50.17 | 2026-10-01 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 45969042-9158-3dd6-acbf-99e5709d6d82 | -11.6203 | -43.5485 | 2026-10-01 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 5b7ed74a-7ef8-3a5f-a869-866d76251b35 | -11.2091 | -45.1709 | 2026-10-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ef6fdc4e-cf86-397a-9928-f2082623eb4f | -8.3211 | -44.1447 | 2026-10-01 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| e8bf3d52-c112-3de2-afde-202609a9182d | -11.2275 | -45.2143 | 2026-10-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f6adccaa-af5a-3ccb-84e6-3a106c7ba3e0 | -8.3074 | -46.7549 | 2026-10-01 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 7b468a20-99ca-3711-b1f3-eec58865ba8c | -5.9152 | -53.4762 | 2026-10-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 66335b2b-e19c-3b85-aff4-ba91edc5cb8d | -6.7002 | -55.0493 | 2026-10-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f356fa2c-3dee-3fa5-8b6d-482d528c18f6 | -9.7843 | -53.8344 | 2026-10-01 13:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 71c8c2c5-366e-3dbb-86b5-9bac78fcaae2 | -8.3208 | -44.1679 | 2026-10-01 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 48524c86-3654-3819-9851-bd2b7496b85d | -8.1401 | -43.5361 | 2026-10-01 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 8f7862cc-8819-36df-b6c1-84a8acdcaf73 | -11.2278 | -45.1913 | 2026-10-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 93be2cf4-5ecc-3e82-936d-8b422cc2aae4 | -9.3881 | -49.1473 | 2026-10-01 13:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4dce75dc-b021-3207-b5f2-924fe4987bf5 | -9.8803 | -44.9553 | 2026-10-01 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| c4f77f42-ba41-3f83-ae09-9eef7cb012f9 | -8.2097 | -45.5075 | 2026-10-01 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| fe272556-0da0-33b3-9500-f670c3b376f5 | -11.2438 | -44.2626 | 2026-10-01 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 6a0a5d99-0944-3c95-b374-2e65f5c5361a | -7.0798 | -42.3255 | 2026-10-01 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| eadbc595-e304-3079-a274-be0bb4651b6b | -15.7527 | -43.6514 | 2026-10-01 13:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5f60c37f-9850-3297-8fdf-b98759a59a55 | -15.6481 | -44.7217 | 2026-10-01 13:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 01aaf0fe-e09b-340d-ad43-4531a27a7295 | -8.3263 | -46.7531 | 2026-10-01 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 090c0db9-e307-30f3-b5a7-8c7f556ae660 | -9.8064 | -44.8265 | 2026-10-01 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 76284955-d716-3ddb-89ba-3c37bf412b46 | -8.2099 | -45.4848 | 2026-10-01 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a02cf101-6dbf-379e-9751-e40739779481 | -7.0547 | -42.8726 | 2026-10-01 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| a72d39e1-378e-327c-9ce9-38bc0779a10c | -7.0738 | -42.8472 | 2026-10-01 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 5165863d-6ca6-3656-a482-8f7e82559102 | -8.1908 | -45.5093 | 2026-10-01 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 16570ad6-398e-34f6-a6b4-f02296251da1 | -8.6265 | -45.3282 | 2026-10-01 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 479bfb9f-6afa-3bcc-ac8f-cd596cb21715 | -16.9909 | -45.4594 | 2026-10-01 13:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 89cb7c07-c842-352d-bcdd-89baa5559314 | -17.5069 | -45.4666 | 2026-10-01 13:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9518e44a-15aa-3d76-b0e9-9990645670ad | -8.6259 | -45.3737 | 2026-10-01 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| cf364850-5a07-379b-8d74-621e4e1da833 | -6.7002 | -55.0493 | 2026-10-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| da56bdb7-add2-3855-97e9-544cd0078307 | -9.1154 | -49.9246 | 2026-10-01 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 708e9ab3-e29d-338b-becf-01b633b82f29 | -5.8597 | -53.479 | 2026-10-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| cde3c8ee-4580-36a8-b8a4-e36c2d106f36 | -5.9151 | -53.4965 | 2026-10-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 2f8fd315-d12d-3a5a-b518-4a65a47c4979 | -8.3074 | -46.7549 | 2026-10-01 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 796adbab-0829-3298-827f-3c5a77f457c0 | -12.4539 | -44.1702 | 2026-10-01 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| a81f5aba-92b6-331a-8900-a3098c4e944f | -11.2282 | -45.1682 | 2026-10-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 81660268-e60a-387d-b556-89c08dfd9bfd | -9.9215 | -50.1682 | 2026-10-01 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 93cf8c03-ee4d-3bdd-8c93-9c0b22f1f23c | -7.055 | -42.849 | 2026-10-01 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 1270d2af-ca3b-3b3e-8264-470c9a1878a6 | -9.8807 | -44.9323 | 2026-10-01 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| c0407891-22fd-3841-b981-1ceb9372982a | -8.3208 | -44.1679 | 2026-10-01 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| a9c5d266-9d6c-3293-b38a-b7c7686dd62a | -8.2886 | -46.7567 | 2026-10-01 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 718438d4-a55d-3ca8-813f-bb8a47ad1851 | -9.88 | -44.9783 | 2026-10-01 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| fb35dd6e-f957-3e38-9b6f-cbe2cf0d6214 | -9.9026 | -50.17 | 2026-10-01 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 3a399ef0-82b4-3b2d-b34b-592f34583fae | -10.5388 | -45.3759 | 2026-10-01 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.6 |
| b1218dc4-7427-3346-b1cd-6b30429c7e89 | -12.4535 | -44.1937 | 2026-10-01 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e0efbf56-e8a4-3d9d-90db-b13b13049189 | -13.384 | -43.9895 | 2026-10-01 13:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 96a74df9-e19d-3bd7-8609-ae9cf9c59160 | -8.34 | -44.1427 | 2026-10-01 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 24c3a73f-9963-3b61-931a-e634b56838f3 | -8.0166 | -42.8681 | 2026-10-01 13:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| eac7cc04-933f-32fc-9625-6e5cf91a4a48 | -9.7877 | -44.8058 | 2026-10-01 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| e4d5c69b-d75f-3352-8601-eb72f8cb2c63 | -11.7182 | -43.4386 | 2026-10-01 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 9fbaeb93-9ce9-3b5b-bbba-6575487a9852 | -8.3397 | -44.1658 | 2026-10-01 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| b1a6fe4b-17a9-3741-b4d8-a29e686aa388 | -14.3574 | -44.7569 | 2026-10-01 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 74583e8d-6a5b-3407-bb34-4d31196ae22d | -7.0359 | -42.8744 | 2026-10-01 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 7584a476-64e3-3471-9407-f15f8c5a1d2c | -13.3835 | -44.0132 | 2026-10-01 13:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 4753d0b6-9811-383f-86d1-f6235c212752 | -11.2278 | -45.1913 | 2026-10-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| f51373d3-917f-32b0-906f-78ee9bb25465 | -13.403 | -44.0098 | 2026-10-01 13:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| ff0e178e-4e70-34cf-b8a1-20fe832bfba6 | -14.659 | -41.0175 | 2026-10-01 13:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 9c0fe0c9-fc50-3daa-b1a2-eeff3d39c6f8 | -8.0162 | -42.8917 | 2026-10-01 13:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 251.6 |
| a9d87eaa-c660-346c-878e-a7c179ae86b0 | -5.9152 | -53.4762 | 2026-10-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 89768071-4d00-3309-aedd-37d8ea349633 | -5.8412 | -53.4799 | 2026-10-01 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 85d6a800-35ea-3a12-9e33-df1c7c473214 | -8.3211 | -44.1447 | 2026-10-01 13:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fc885064-baae-3b97-98c9-6e381e49e27d | -14.3384 | -44.7369 | 2026-10-01 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| d0a994ba-7ee0-3225-9f54-c5bdb5e155ec | -7.0609 | -42.3274 | 2026-10-01 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| ad096234-4a66-3ab3-aa27-ab81cd081bfb | -11.6199 | -43.5722 | 2026-10-01 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 90c94e96-d800-34e0-9893-4230bf9934ca | -12.9036 | -44.8217 | 2026-10-01 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| f5f72ac7-7de7-3f8a-82e9-f0ae8ee436f4 | -13.04 | -51.23 | 2026-10-01 13:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3200d6f-7585-359e-ad7a-97c1fd71ad91 | -13.07 | -51.24 | 2026-10-01 13:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43f5d5bc-2dea-3af0-821e-fcd05f665e26 | -8.02 | -42.89 | 2026-10-01 13:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e4781e6e-e7a7-3034-b45e-c58c044478a4 | -5.8412 | -53.4799 | 2026-10-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4331f120-286d-3466-96f2-da3c1c9e2abc | -8.6265 | -45.3282 | 2026-10-01 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 0013e331-b2e7-3710-8248-2b4ca8328ae8 | -11.2438 | -44.2626 | 2026-10-01 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| d8ed04b8-2c7c-3680-ad84-532509d0390e | -14.8981 | -41.6625 | 2026-10-01 13:20:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 80774e64-cf12-342a-9ffa-4aed93972b71 | -9.9026 | -50.17 | 2026-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 22b51d59-34bf-335a-a72c-c26f61369abd | -12.4732 | -44.167 | 2026-10-01 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e9554743-e6ad-3850-b0f8-4435197dd19d | -7.0612 | -42.3035 | 2026-10-01 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 218a781f-a222-3a3e-9c2b-2c10555e0bef | -11.2087 | -45.1939 | 2026-10-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 3ae33846-dbf3-36a1-aa1a-72def88e45c0 | -9.8067 | -44.8035 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 29ca096f-62eb-3992-b5d3-ac357a054cae | -8.0166 | -42.8681 | 2026-10-01 13:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| cae75694-1432-3582-85a6-833a3fb58036 | -10.7285 | -50.5339 | 2026-10-01 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0a83e5a4-73a1-3f00-8f66-4a6191783f7a | -14.3764 | -44.7769 | 2026-10-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 19b236c8-0a7a-3ec8-9009-c00ef4d9f383 | -12.9036 | -44.8217 | 2026-10-01 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 90fc51b4-1691-3816-be41-a5258968202b | -8.3211 | -44.1447 | 2026-10-01 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| edf335cc-41f6-3c7a-b1ed-8c80c56c3f8f | -13.384 | -43.9895 | 2026-10-01 13:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| e5cec16f-7072-37c9-aef9-28215f58a1f6 | -8.6454 | -45.3261 | 2026-10-01 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 14582a6f-689d-321d-9cfd-61a02e8c0c51 | -12.4535 | -44.1937 | 2026-10-01 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 9fca614b-26f4-31b7-80a6-d160fc7ed411 | -14.659 | -41.0175 | 2026-10-01 13:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 8836ae0d-7ffb-3105-aa33-848ff116fe2c | -6.7333 | -55.6066 | 2026-10-01 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2c869452-6268-3dd6-b3c0-ebbdeaf54f6f | -13.403 | -44.0098 | 2026-10-01 13:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| d0d33757-10ef-3cb8-90b1-f17ff2b41db3 | -5.9152 | -53.4762 | 2026-10-01 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 18c6209b-1fb0-38c3-b31b-36e487e457a0 | -8.1908 | -45.5093 | 2026-10-01 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f53175c4-cf45-385e-b9d0-b50ee7e29c50 | -14.3574 | -44.7569 | 2026-10-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 19b64d8c-03cb-3c69-83a7-f22fd188662c | -10.5388 | -45.3759 | 2026-10-01 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 254.6 |
| 6185bcc3-1b97-3af6-af79-f9dd0f0522c4 | -10.7104 | -50.4718 | 2026-10-01 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a00fc251-0275-38b2-8e9b-964e60c8e4fc | -9.8807 | -44.9323 | 2026-10-01 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 257.1 |


[Clique aqui para ver as próximas entradas](README98.md)
