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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0311fb5-0933-3d1d-81cb-b21a3298bef7 | -10.1583 | -45.4016 | 2026-09-17 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c9a6e084-94d0-3dc0-a806-65544b216fc3 | -14.1742 | -45.1407 | 2026-09-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 1abac770-20fb-32eb-9ef7-a227c84b7f2c | -11.8069 | -58.1759 | 2026-09-17 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cb0e17fd-8fcf-3289-8b79-9c39dec9a9eb | -8.8644 | -45.8919 | 2026-09-17 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 66024b74-9a8b-3b3e-8f4c-9ddef3821369 | -7.0451 | -42.0666 | 2026-09-17 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 56efc958-f63f-3b7d-a7eb-90fa6c7e47e1 | -30.6109 | -53.0283 | 2026-09-17 14:30:00 | GOES-19 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 135.8 |
| bdf18772-fcc9-35b9-be50-7f7b63b3dde7 | -8.8647 | -45.8693 | 2026-09-17 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 5f0e7b84-79af-394e-a764-5b96fdbad9dc | -13.3758 | -57.026 | 2026-09-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 1c97af58-a992-3c8e-a669-78474b3ae65e | -6.7963 | -47.8967 | 2026-09-17 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| cb977998-1f82-3164-ae64-0bfeed79d848 | -10.8192 | -50.8223 | 2026-09-17 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 23237f21-f0cd-343b-8d9d-bb9730651a19 | -9.5512 | -45.4296 | 2026-09-17 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 41dddd3c-b9c2-3048-b6e1-ee088bc5b73f | -7.3669 | -38.9584 | 2026-09-17 14:30:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 166.3 |
| 42dd815e-207f-3ac6-bf47-9d8dabf659c5 | -4.5045 | -54.9646 | 2026-09-17 14:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 281.7 |
| 146ca90a-aa72-3cc7-b37c-4fb87a346c4e | -1.8233 | -54.9307 | 2026-09-17 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bb5e1da3-13eb-37b8-b218-b223f67d48f7 | -7.8033 | -44.8651 | 2026-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| fe6faf89-35f9-3e44-b1f0-6740df1c98d7 | -6.7776 | -47.8981 | 2026-09-17 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 4476211d-1a24-3e35-9d24-2ca2cfb4b3a2 | -9.7606 | -60.4754 | 2026-09-17 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 324208dd-bec8-3ce2-8f17-43dc1a62a541 | -10.9107 | -54.0045 | 2026-09-17 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ecb875ff-095e-397f-9f52-6c73caf79766 | -15.5715 | -54.223 | 2026-09-17 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f9630412-e904-3073-a5f9-0fcd96643bcc | -7.6402 | -44.3303 | 2026-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 23ea8289-b0bb-3b48-8960-923dab7a88e0 | -11.8924 | -50.0823 | 2026-09-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| dcc182e8-d431-3780-9f3d-44b28d7a024b | -6.7778 | -47.8763 | 2026-09-17 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 40a0a0e1-bc41-3280-9d7a-3ed4062c4440 | -18.8906 | -46.8284 | 2026-09-17 14:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 57fcee56-8a2d-386f-a2b7-dab7242a6fb9 | -13.3758 | -51.7193 | 2026-09-17 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b583ae2e-df94-3421-b46d-cff3b38cc498 | -13.3055 | -51.3235 | 2026-09-17 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 26d3dc37-29dd-32ab-b1a6-0e74a98f1448 | -10.4772 | -50.9634 | 2026-09-17 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d542564b-eed9-3aff-a1d2-c58864db0f9b | -18.8906 | -46.8284 | 2026-09-17 14:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3c9fc68a-bcaf-3ae9-a2a2-b96e91ce8b42 | -9.7608 | -60.4561 | 2026-09-17 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| cefe6fa4-44a3-35c0-8493-e149b7af42b5 | -9.7497 | -46.1089 | 2026-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 0dfdc5fa-9252-326d-b9e9-8d7aa3305599 | -9.1056 | -60.9703 | 2026-09-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 016d3e37-52f9-3ab4-b063-c34b840cfcb3 | -7.4595 | -42.1199 | 2026-09-17 14:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 8e7f39b6-1c7b-3497-a43f-20a74a136a94 | -10.0422 | -45.5528 | 2026-09-17 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 6e370d76-c4e4-386d-a363-19e6078a37ca | -7.0262 | -42.0685 | 2026-09-17 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| fa3ed30b-482a-3e44-abb8-fd6decdde6c8 | -4.5229 | -54.9639 | 2026-09-17 14:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| b8d23b8c-e9b1-3598-863a-842e13f60e85 | -10.911 | -53.984 | 2026-09-17 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 95a22795-663d-347a-a9a0-4409e7b8844f | -9.7793 | -60.4744 | 2026-09-17 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9dd0c515-bf83-3855-9492-b5fae9848705 | -8.8923 | -62.3917 | 2026-09-17 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b4f3f5e6-1498-3098-a346-bb0e6f7c7b89 | -10.0418 | -45.5756 | 2026-09-17 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 264.1 |
| c2810ff4-ccc7-34b1-b361-bf120564c50b | -7.9543 | -44.8273 | 2026-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| b52f0bc1-5974-3cec-9dcf-4afcdb62b3d8 | -14.8376 | -59.5515 | 2026-09-17 14:40:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bf71ca4f-1aa4-3b94-992b-da82eb9e29e1 | -11.3442 | -43.9906 | 2026-09-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 2f2997cf-011b-3df7-a7d8-dba141cf15a8 | -9.1337 | -65.844 | 2026-09-17 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 3e2113e7-6653-3d58-9da2-99cbfc5f187c | -11.8924 | -50.0823 | 2026-09-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 71045ce5-f512-39fa-9c16-1fa9d0fd84b8 | -9.1711 | -49.9835 | 2026-09-17 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1be5b93b-8621-39c9-a240-a2dee2847fdc | -13.3946 | -57.0444 | 2026-09-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b530c8fa-1f25-34c9-bd22-0b18caab293f | -11.8069 | -58.1759 | 2026-09-17 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8732cb34-fd2e-3473-a52f-63bdb3e17c4f | -13.3949 | -57.0242 | 2026-09-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 297.8 |
| b4eb41c1-d29c-31d6-b5f4-c81478069974 | -9.8322 | -48.3417 | 2026-09-17 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 28b35ed0-0d1e-344d-8046-ced5f9bfd355 | -8.8644 | -45.8919 | 2026-09-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 7185a1c6-09e4-3490-ac63-084e282329f8 | -8.475 | -46.8943 | 2026-09-17 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 8d378666-f560-3166-85ea-ee8dae03b54b | -11.738 | -50.2295 | 2026-09-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 33f6c68b-c857-3144-8037-4e2871a66b84 | -12.6826 | -54.6763 | 2026-09-17 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f849ba9c-bad1-3d06-8151-4dfa95d86741 | -13.3755 | -57.0462 | 2026-09-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0345e284-fb5d-3bbc-9934-4781c9aa0bc3 | -13.2678 | -51.2856 | 2026-09-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5758640f-78f6-3dfc-8fba-8579811cda5e | -9.7794 | -60.4551 | 2026-09-17 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b3f61380-84e9-386a-9f63-1d6f67fca91d | -9.4139 | -50.1103 | 2026-09-17 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 484cf4d7-d600-3068-b00a-903a7f1c5d8c | -9.4325 | -50.1299 | 2026-09-17 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a2c08957-7cc6-3830-a05e-00fa93dec426 | -8.8836 | -45.8672 | 2026-09-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| d9519354-e37f-3f26-b124-e1f68b9ce801 | -13.3758 | -51.7193 | 2026-09-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1e1058b9-d994-3986-a5f4-a340bfb8439e | -11.3446 | -43.9671 | 2026-09-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| e83cbf33-214c-375a-91dc-e962453461da | -7.1384 | -42.1529 | 2026-09-17 14:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 5dbc1be5-6afd-39c0-88eb-3ceb9e9992ff | -14.5709 | -46.5941 | 2026-09-17 14:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 02434e63-e294-33ed-bbe2-51981b85a3c9 | -14.1547 | -45.1442 | 2026-09-17 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 2bb415b6-d63d-3bc4-b876-fb7e94f7b08c | -7.6381 | -46.1478 | 2026-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7a5b37f7-e1a6-3e77-9b57-21d59f8d2417 | -13.3754 | -51.7406 | 2026-09-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 593dcb03-dacc-319d-b6b2-b2ac8f81ebba | -5.6472 | -44.7964 | 2026-09-17 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4e5559d0-aa76-347b-91d3-e150329ead93 | -12.7051 | -48.276 | 2026-09-17 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| ff6d0a21-4ee0-35a8-bcc9-abed0f4e2178 | -8.8647 | -45.8693 | 2026-09-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| cbf38a42-38e6-3d86-a587-9f5cb535b1d9 | -4.5589 | -42.9289 | 2026-09-17 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d292d39f-119b-3639-90e2-96eacc539742 | -11.3629 | -44.0112 | 2026-09-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7bd42d6a-f707-3da9-831d-4f522e3a96b8 | -13.2986 | -51.7501 | 2026-09-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6cbc0744-7f6a-370d-9cfa-be0e272afe85 | -6.6703 | -43.6337 | 2026-09-17 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 51f33f54-117d-3328-907f-b66445b16ec4 | -14.1742 | -45.1407 | 2026-09-17 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 578c59a9-29b2-3d21-a5ac-a2e9ab3f6a96 | -8.4983 | -57.6271 | 2026-09-17 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8fce7cf8-d9c2-3827-a416-f7874c385262 | 3.9353 | -59.6446 | 2026-09-17 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 494ff492-9ca2-3d53-8b64-8ce57dff7809 | -14.1737 | -45.1641 | 2026-09-17 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| a992ee73-640d-3241-bbf6-bb1300f59856 | -9.1057 | -60.9511 | 2026-09-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a48c5a20-6c11-3133-a2f2-7a4f312dde11 | -7.0454 | -42.0427 | 2026-09-17 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 2bd6d076-6767-3a1f-a224-e2cc232731d8 | -8.1424 | -44.854 | 2026-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| fafd8561-9339-3255-a9d8-11f599b576ef | -10.6335 | -50.5651 | 2026-09-17 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 72c372a4-1b49-3af2-bdcd-3b513e1abc9d | -13.6148 | -46.9334 | 2026-09-17 14:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e78f9a7f-7b29-34cc-b4ff-cc23caa4f901 | -7.0084 | -43.6497 | 2026-09-17 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 9984b083-0aea-307b-9eaf-feb735769c54 | -12.7713 | -51.2189 | 2026-09-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 18219dec-f5ed-3576-9362-bdb3e3aab168 | -11.3161 | -46.7699 | 2026-09-17 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1446e5e2-cd25-3422-bebb-803e7fef0a27 | -6.7778 | -47.8763 | 2026-09-17 14:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| a7805950-98b6-3442-b342-886dcba65cb5 | -7.8221 | -44.8632 | 2026-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b31a9a2d-298e-3210-95b5-3966ee422d3e | -7.9355 | -44.8291 | 2026-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 711e5086-a8ff-3fc1-b53d-15040ce57c56 | -8.5239 | -44.5153 | 2026-09-17 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| c0d7869b-465b-33ca-b96b-f71f91c3a702 | -10.1583 | -45.4016 | 2026-09-17 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 25c45309-1161-36f0-b7c5-a42ab147c35e | -9.7687 | -46.1067 | 2026-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 25450ab4-8d98-39b8-8051-33620808f2ad | -9.3564 | -50.201 | 2026-09-17 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 6eada941-b91b-3332-a8d2-81f01521075f | -10.6525 | -50.5631 | 2026-09-17 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 24287f34-0ff1-30a7-8d76-90b82083a2bf | -6.5837 | -58.8498 | 2026-09-17 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c235e1b8-6149-3d9c-896d-1f8ff4719163 | -9.376 | -50.1352 | 2026-09-17 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 48017a25-bf99-39d5-b57f-86f4c8ba9c22 | -13.3758 | -57.026 | 2026-09-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 257.1 |
| 0eed27d4-e32e-36c6-aed9-be146358e742 | -12.7243 | -48.2734 | 2026-09-17 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 89eb8d22-cc79-31ad-aa1a-2821dc396ad6 | -6.6515 | -43.6354 | 2026-09-17 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 5923215c-6d23-3e16-922e-a74ac77f773c | -9.3893 | -60.3022 | 2026-09-17 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a32fa0c8-52db-3f9f-9db3-076f8fab71f1 | -9.3572 | -50.137 | 2026-09-17 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| af71d613-b613-362a-9e0d-66c2314aafd7 | -10.8919 | -54.0062 | 2026-09-17 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |


[Clique aqui para ver as próximas entradas](README95.md)
