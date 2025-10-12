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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20e01476-f0e8-3298-b14d-3ee532f6318a | -13.34335 | -43.96059 | 2025-10-12 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52b9e381-e36d-3eb5-bc1d-df4fe15a1139 | -10.7826 | -43.95461 | 2025-10-12 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8673fda-15c0-3252-a27f-1922cad9175b | -11.50006 | -43.49423 | 2025-10-12 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c426e0d-95c7-34a9-b0fe-106cb4ada049 | -15.01504 | -46.29163 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04c6d97f-8ae6-3f97-8ada-03739c072cfb | -13.46298 | -51.27763 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a5b2af87-1b57-33c4-8b83-8a0da45120a6 | -16.26599 | -50.99994 | 2025-10-12 04:44:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70f4d786-a9ed-334f-af37-1293622851eb | -14.94131 | -46.73888 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fe86e1af-7a19-364b-b7e3-c12852e0cb48 | -9.40413 | -45.76014 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6d6c3010-0a93-3131-bf7c-6997a266a91f | -14.67963 | -44.76091 | 2025-10-12 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b2e91bf-1591-3879-9454-babaf8b22ce8 | -13.44375 | -51.25587 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ec20ad1-6359-3425-91b7-3122cc6b4b5e | -15.00301 | -53.88423 | 2025-10-12 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e3b7c73-3cf4-385c-b6ea-e243307be86c | -15.02153 | -46.27448 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee39ef3-de92-3e95-b2e0-51ee0cc72f01 | -12.21122 | -64.36751 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86628d9b-042d-30ff-b122-caa49c29271d | -15.22896 | -56.86334 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19094314-c57d-3946-81f7-53e51e11691f | -9.0794 | -48.03034 | 2025-10-12 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e759466-4229-3660-b8ba-2559d15a72e6 | -10.15642 | -44.54762 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a28f331e-2a70-31f6-9c71-cf139e946131 | -11.79742 | -46.35635 | 2025-10-12 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3de9d244-c1fb-3aaa-84ef-dfd999ac3c06 | -14.41233 | -47.9584 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e86507d-09be-335b-b187-1ab3ae0877ec | -13.46021 | -51.27352 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ec92538-9afb-3473-9bcc-0f1ccd48d98e | -13.57018 | -46.34779 | 2025-10-12 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd73f977-c2a4-3104-ab1d-308080bdbca3 | -12.21671 | -64.3756 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84534417-6fb9-3cc0-91a0-ab2748d8f510 | -15.19983 | -56.86702 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9966431f-fcdd-38ab-941c-4b6e34cbbc15 | -15.29785 | -46.14482 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7e1663b-4592-3fb2-afef-a37b57fbafd3 | -11.62791 | -55.01548 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4398dfed-90fe-3e01-ba2a-66ea0bf93ce1 | -14.15907 | -42.53363 | 2025-10-12 04:44:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5a9113ee-9b9a-3ce3-b45c-f70697f09844 | -13.44526 | -51.26011 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e099a8c9-624f-364f-8726-7f8dcf937bf7 | -16.50516 | -49.04251 | 2025-10-12 04:44:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd6f0274-bf17-3e78-9895-0a39f1d5731d | -14.53611 | -45.58142 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdf2673c-806d-39ad-82fc-d39f853bf922 | -14.98649 | -44.93922 | 2025-10-12 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 191f2c66-bf58-34f8-8621-deea15b51e09 | -14.91606 | -46.77616 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a042c86-bc31-39cb-8735-2370e7057302 | -11.79816 | -46.35398 | 2025-10-12 04:44:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19151454-da33-39c8-91ae-a2f10ff3a5c5 | -11.62509 | -55.01701 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85048ba2-4f16-32d5-82a3-1124ba8b381a | -10.17896 | -44.54169 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73731f15-5527-31cf-89f8-1703e242ab1e | -15.29522 | -46.13284 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5634c18d-78ab-3d1c-9e8d-ae8c08c63532 | -12.21076 | -64.36788 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3920724c-278e-395a-a5ab-46b52af3aaaa | -14.16426 | -42.53409 | 2025-10-12 04:44:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e716c18-af3c-3e6d-b12f-b101f3a5c8a3 | -11.6221 | -55.01147 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e993ccf-21c1-3c58-b615-6f2eaeec76a0 | -11.85039 | -56.86901 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30177ec2-fd2c-3a8d-bffe-adf1cc2f76f8 | -9.40555 | -45.75053 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f26de7f-f6c8-3738-9e9e-087c703cee86 | -14.91676 | -46.77106 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0432ae3-8d18-3cd1-b581-98707ab7db62 | -15.19891 | -56.86622 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69525162-808a-3571-b651-9a9fb11dea14 | -12.13813 | -45.58854 | 2025-10-12 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4440de6-3a83-31f3-9c15-364190a19c56 | -10.18704 | -44.60767 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 077ebf19-6c0f-35e7-baeb-e1be595ded83 | -13.45908 | -51.28063 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 841ee3b6-6c56-3b38-aa55-58ceb4cbb859 | -15.17052 | -56.84254 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c013c347-c32e-3465-bcdd-0c05de72e5a4 | -11.39345 | -55.16876 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58057722-f7c3-3c26-925e-cf6cb174e55d | -15.28964 | -46.14337 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8f60fa9-bdde-30e1-b512-07bb637d8a3a | -15.20712 | -56.86745 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ea409c-d81f-38cc-a3fd-fc54d39800ad | -14.94738 | -45.58038 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 72495d59-c5ca-34be-b048-7594da9577cf | -9.40168 | -45.74977 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee1f0713-051e-3c15-a5ea-5f773eb47923 | -15.75969 | -48.9795 | 2025-10-12 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3fe6179-5d40-328f-8842-5b97c89d14b2 | -13.44639 | -51.253 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 01beb10e-8e85-37e8-bac0-ae7d59650a06 | -11.75285 | -43.30894 | 2025-10-12 04:44:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd39efdb-2ab8-3bae-b857-9c944b871ecd | -13.45965 | -51.27708 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5978b517-01f4-3528-a065-434f0e1161b4 | -15.19233 | -56.86184 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eed6bad-1ffd-329a-8ae1-9dce39686916 | -15.67292 | -46.64338 | 2025-10-12 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 720a8943-9f09-38bf-8127-bd3cf5a51b40 | -15.2669 | -56.90973 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eea78cbb-bb8f-3395-9eea-bdfa6e649b6f | -14.38489 | -47.99384 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1da76fe4-b815-32e1-b68d-64a97486a33a | -13.34799 | -43.96122 | 2025-10-12 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7c31ce41-795e-3653-a33f-986513ee1d0b | -15.67767 | -46.63842 | 2025-10-12 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b2d75c8-e46c-389f-8436-49d9f13a421c | -15.15491 | -56.81255 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d7dc6f5-12c4-39ad-b45e-c8a80ce8fabc | -11.85045 | -56.8623 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 218a5fc3-8ebe-3bc2-9ad9-476884500f3b | -15.18823 | -56.86118 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d9051de-d0c8-3981-ad4f-e8343daa8701 | -14.40494 | -47.98407 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cd3577d-edaa-3949-a572-d1076136a74b | -14.92817 | -46.74657 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ff1c18a7-ce64-3bd7-b8ed-d511d7e28435 | -12.21258 | -64.36094 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e3d2741-b9f3-327a-a88b-ec821ef2cdd3 | -15.20301 | -56.86686 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a7901a0-2c68-38d4-a1b4-87af358be4fc | -13.28292 | -47.98419 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 460b3ff1-bea2-38a3-a6c1-1718876ecb1a | -15.29938 | -46.13315 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 545ea5af-23a1-38e1-84fa-5d4f6454f269 | -15.20053 | -56.86308 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45b3d1da-ab26-3fe7-90f2-85cadb2c3efc | -13.98944 | -54.89099 | 2025-10-12 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c217396a-8655-3b32-9f16-8e13a5820f0d | -11.75691 | -43.3147 | 2025-10-12 04:44:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 643bbb0d-61c1-3685-9dd2-9a102266ad29 | -14.93278 | -46.74231 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8fdf22f8-2ea2-34bd-9670-f2fd1bdb358d | -15.22036 | -46.39025 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19d527d0-c73a-3ca6-b902-3bdf58bd26b9 | -12.21622 | -64.37589 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8218a580-5420-3e97-901b-7606c69ef3db | -13.28589 | -47.98908 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac54073c-e4b9-3beb-981d-f7abaf303a41 | -16.50871 | -49.04309 | 2025-10-12 04:44:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49bf2ee7-e726-3812-8361-9a56ed9514ba | -13.44582 | -51.25655 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ecdd494a-ae3a-37f9-9dcf-1ff1a9a08afe | -13.22063 | -47.80082 | 2025-10-12 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e79ce595-b8b9-3849-87b8-818b1f263673 | -15.28917 | -46.14699 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91378ae2-57b8-3ee1-a5fd-2d7a279df66c | -11.36377 | -41.88224 | 2025-10-12 04:44:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0d6840c-793a-364e-98a2-c72367c61ac7 | -14.94258 | -45.58396 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 92d1e0b4-e9f0-342b-b85b-654fb6bc7250 | -14.98145 | -44.94314 | 2025-10-12 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b0fdac55-58ee-34e4-9b59-79add9dc6bb5 | -15.29373 | -46.14418 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4becdfba-9130-3a19-bf2e-271d01bfe20f | -10.20887 | -44.6063 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2df38977-b1d4-3e9c-b05a-30715cabfda3 | -13.46687 | -51.27463 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 317a0280-02b1-32d4-b0cf-c030858e2cc7 | -11.67093 | -43.78246 | 2025-10-12 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56d49c38-f5c4-3d7f-b4ae-2609fe9fcf3a | -15.23515 | -56.87554 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29ae3e4e-69f4-3614-a46f-9530fd480818 | -9.4083 | -45.76286 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a030228-a970-31be-8222-4acb37d72e29 | -15.02515 | -46.27837 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1b751a3-2da0-3f74-8dfa-81f08b6baacb | -15.2906 | -46.13606 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6de51d5-3eb6-33e9-abc9-7a168b95f615 | -13.29373 | -47.986 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1a8e4bc-fd32-30aa-8ea1-f6e6e02196ae | -11.62406 | -55.01477 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c7b993d-cd35-36f4-b10e-0690673bae96 | -11.84972 | -56.86646 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2492aa53-dd53-3276-802a-4982c862cae9 | -13.98789 | -54.89999 | 2025-10-12 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8d8abed1-627e-3b3e-bc28-064452601757 | -14.53558 | -45.58541 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27152f96-a1af-36ac-9c8c-2c1c3c51b437 | -15.23717 | -47.16542 | 2025-10-12 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3434dad-26c5-3e77-9c57-96d034c5a564 | -12.20935 | -64.37445 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 574c7f71-a16b-369f-812e-c3122bf827bc | -15.01912 | -46.29212 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b396f8a5-1e47-3bf8-9133-c1396b366365 | -13.98866 | -54.89549 | 2025-10-12 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README34.md)
