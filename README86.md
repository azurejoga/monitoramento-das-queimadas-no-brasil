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
| 71cfa6bf-8b25-3e60-844d-944f74184b12 | -9.8319 | -48.3636 | 2026-09-17 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9e85a9f1-7eae-3572-832a-09921bb64cd9 | -10.8189 | -50.8436 | 2026-09-17 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| bb557f13-aa7e-3b5e-8fd7-5dd80b3b2527 | -10.8308 | -46.1569 | 2026-09-17 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| cc393df7-18d0-3fa1-8223-6647cc8858e1 | -9.8697 | -48.3595 | 2026-09-17 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 965b86c0-70ea-37a4-8b7d-053368e10c16 | -12.4343 | -50.79 | 2026-09-17 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| b839ffa1-2567-330e-832e-e55fbd48fb36 | -10.7999 | -50.8455 | 2026-09-17 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d93ffe7c-010c-3c71-bb8b-41d589657c5d | -7.0161 | -44.6642 | 2026-09-17 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 196.7 |
| cdff7823-76c8-3cf6-83fa-0446f76af55a | -10.8305 | -46.1796 | 2026-09-17 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 52e61fc3-4e91-307b-beeb-c00957bfdae4 | -12.5094 | -50.8664 | 2026-09-17 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 53765ba4-90fd-3549-b614-065cded99a58 | -12.5097 | -50.845 | 2026-09-17 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c069fca3-8f6d-337d-8ce4-42e616672791 | -12.5118 | -50.7164 | 2026-09-17 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 401.9 |
| 59c767d9-2147-3834-bc60-4eaeedd626ad | -9.9143 | -46.5172 | 2026-09-17 11:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8a5b86ab-93ba-38a2-b103-b69a5ad11af3 | -7.0164 | -44.6413 | 2026-09-17 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| dca576d8-598a-3096-b3bf-1cf13d6efe45 | -12.493 | -50.6972 | 2026-09-17 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 17256b35-499f-3e06-9e0a-5bfed9fcb3a3 | -12.5121 | -50.6949 | 2026-09-17 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 66ac30d5-0696-3f98-abec-f7c06120bab4 | -7.6402 | -44.3303 | 2026-09-17 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 8a98ee60-0489-32e5-8acf-5d0f9b1a6ccc | -30.60398 | -53.03878 | 2026-09-17 11:51:00 | TERRA_M-M | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| 3ca126c8-386d-36c7-adcc-60ba34ff487c | -27.32885 | -52.60907 | 2026-09-17 11:51:00 | TERRA_M-M | ERVAL GRANDE | RIO GRANDE DO SUL | Brasil | 4307203 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b4359352-0617-3c2d-a684-d5e94ba1fe4a | -30.60544 | -53.02855 | 2026-09-17 11:51:00 | TERRA_M-M | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| 061785db-9cce-359b-929b-78b89a6ec06c | -7.0161 | -44.6642 | 2026-09-17 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 269.8 |
| 56b54300-5e0a-39d2-adc9-ef6a545ce2c5 | -11.8069 | -58.1759 | 2026-09-17 12:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 00bfc7de-1957-3582-8046-8e1cbadf7667 | -11.4853 | -45.7737 | 2026-09-17 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9fd5220e-4412-3dca-9f44-6576c5cd16de | -7.0349 | -44.6625 | 2026-09-17 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 70ba9009-ffb4-38e9-a002-43cb50ef85de | -7.5661 | -42.656 | 2026-09-17 12:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 43d8a721-db8b-3944-9274-e394e9018d65 | -12.5289 | -50.8427 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 157.9 |
| eabf9858-c8f7-30fd-8e2d-583dd0d0ffa9 | -9.8319 | -48.3636 | 2026-09-17 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1d41f46d-5758-3dd9-aa59-e4c2c492db21 | -12.5121 | -50.6949 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 32cb347f-2958-3919-8e5b-56d7fb4785a1 | -12.4343 | -50.79 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7094ec6c-7550-3639-9057-386c17611ae3 | -10.8118 | -46.1594 | 2026-09-17 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e015f257-761e-3c66-b27f-c57f07979fde | -11.8937 | -47.6099 | 2026-09-17 12:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a1d9ccfa-c8f8-3f3e-ab7f-df1a28b70592 | -12.5097 | -50.845 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 214.8 |
| f2488fe1-7c3b-31e7-b910-45e2c4ea5807 | -12.4333 | -48.4897 | 2026-09-17 12:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8d6ccaf3-4753-3fec-af7a-83e740c62afd | -10.8189 | -50.8436 | 2026-09-17 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9e548d77-9770-3690-baa5-da50d9072227 | -9.8322 | -48.3417 | 2026-09-17 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| fdfc631a-3752-3124-bfa4-5be4c8403ff8 | -10.8305 | -46.1796 | 2026-09-17 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| ace4592f-d1de-3ea3-a994-63a163991412 | -10.8308 | -46.1569 | 2026-09-17 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 32e07673-02d0-34ae-a4b7-bfe52c656b88 | -12.493 | -50.6972 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c8d464b9-0e6f-3380-9c4c-e0a8537f502e | -12.5094 | -50.8664 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 267.0 |
| e5974806-a9dd-31bd-94a8-cf8cd10841ce | -9.8697 | -48.3595 | 2026-09-17 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ade4c0ff-3e8e-3fe9-8778-600afb33920f | -7.0164 | -44.6413 | 2026-09-17 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 0bae139a-7f08-3508-b018-c7dfb24da62c | -12.5118 | -50.7164 | 2026-09-17 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 8b5d44a5-309b-3a8c-8255-35cdbd92ab69 | -7.6402 | -44.3303 | 2026-09-17 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a1c6040c-407f-30cc-9bce-001d90547751 | -11.8941 | -47.5876 | 2026-09-17 12:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 44ab8919-1e49-3fe5-9f85-d54fdfbc6218 | -7.3666 | -38.9837 | 2026-09-17 12:00:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 131.4 |
| ef9c3754-5dea-3dd8-8c27-a5571e654c08 | -10.8305 | -46.1796 | 2026-09-17 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 09820d7b-8b9e-32ff-aced-f7f61f333459 | -7.3666 | -38.9837 | 2026-09-17 12:10:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 37c0d95e-ad7d-3753-a2f4-262ce4cfd222 | -10.8189 | -50.8436 | 2026-09-17 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 56d4fbb9-d343-367f-b91b-6115397af591 | -7.0164 | -44.6413 | 2026-09-17 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 186a41d4-16bc-39e7-b866-52de703f60dc | -12.493 | -50.6972 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5278a2b8-7334-355e-ad7c-0768e31100d3 | -7.0349 | -44.6625 | 2026-09-17 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a5a192e7-e44c-3129-9f2e-c278bb720c6b | -10.7999 | -50.8455 | 2026-09-17 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 63efa23a-c6ac-3fbc-bd12-15fb97f30dee | -9.8694 | -48.3814 | 2026-09-17 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d198e44b-6f0e-36ca-8ed6-e1b0b8d96933 | -7.6402 | -44.3303 | 2026-09-17 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a843ac27-bcc0-3f5b-b882-8799b3824d25 | -12.5097 | -50.845 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| eae0d128-f265-3f9d-9df6-eed8fbb14801 | -12.4151 | -50.7923 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ffc454d7-f34a-327d-a527-90fb97e956fc | -11.8069 | -58.1759 | 2026-09-17 12:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| a99514d6-a79a-3d19-b31b-a1b5f54c4b0d | -12.4343 | -50.79 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| b33e395e-3b83-357a-a8aa-226afc3bdcea | -7.5661 | -42.656 | 2026-09-17 12:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 38ebf472-04ba-34a0-b102-5396e865a7a3 | -11.4853 | -45.7737 | 2026-09-17 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| f8cd787a-d699-3f6f-9504-d436e7ff4be3 | -10.8118 | -46.1594 | 2026-09-17 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| dccbcad0-b27e-3bc4-85db-f11608ec136f | -8.4669 | -44.5445 | 2026-09-17 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 83bdbd8e-168d-383f-8f61-455d1f200840 | -7.0161 | -44.6642 | 2026-09-17 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 258.3 |
| eaa5b1e6-12f6-380e-9492-5e1866513d57 | -12.5094 | -50.8664 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 78e59fef-dfc6-309f-ac0a-245bceb34932 | -12.4534 | -50.7876 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| eae3641a-032c-3cb7-bacb-61f00d8c9072 | -9.8697 | -48.3595 | 2026-09-17 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3a67f10f-68d5-3043-852c-009d45557e33 | -7.0804 | -47.5031 | 2026-09-17 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| fcc1438e-3b90-3683-b481-337245273503 | -12.5118 | -50.7164 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 879cdad5-8b26-39c2-b331-3d59b599182f | -9.8319 | -48.3636 | 2026-09-17 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 605ef460-324f-3b4b-a88f-6664fe160778 | -12.5121 | -50.6949 | 2026-09-17 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| afe66e4a-6c20-3c36-8a79-d6ea65cc1ad9 | -10.8308 | -46.1569 | 2026-09-17 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 1e7246e2-732e-379c-a361-c27c41f389d6 | -7.841 | -44.8614 | 2026-09-17 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| faae64aa-6537-37bd-8591-1659df5d5fed | -14.1742 | -45.1407 | 2026-09-17 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7a6b8a6a-6bfb-3978-b47f-5ba7e7245491 | -10.7999 | -50.8455 | 2026-09-17 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6f75bc6f-89d8-3c88-b159-8c04d9d1de40 | -7.0164 | -44.6413 | 2026-09-17 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 73c450e2-a405-3f83-86b8-669d958d4913 | -10.8499 | -46.1544 | 2026-09-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 7260c142-beac-3f5b-97b5-b8ff8a44a3a3 | -10.8189 | -50.8436 | 2026-09-17 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 82e4641b-2796-380f-95e1-1f8b276d0e3a | -7.3666 | -38.9837 | 2026-09-17 12:20:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 147.4 |
| abd24620-a878-37f8-b692-9d1c2c502a47 | -7.0161 | -44.6642 | 2026-09-17 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 336.4 |
| 65b548b1-ad17-3335-850a-46d1c34686bb | -9.8694 | -48.3814 | 2026-09-17 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c1401f42-cfda-3fc4-8a56-1124127f8639 | -12.5094 | -50.8664 | 2026-09-17 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 170.1 |
| cd9a706b-3c96-386c-b3b6-1b83e1cd4530 | -7.6402 | -44.3303 | 2026-09-17 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c0fea3b2-913e-359b-a4ce-c6537f93d674 | -7.0349 | -44.6625 | 2026-09-17 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 9f79d99e-444a-3965-899e-175cad603a07 | -11.8941 | -47.5876 | 2026-09-17 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9108f4e7-95b8-36be-84b0-d1d8aefdd8e8 | -7.5661 | -42.656 | 2026-09-17 12:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 193ff0c6-18bf-3d27-bf90-dac480ed15c3 | -10.8308 | -46.1569 | 2026-09-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 526ac000-4cf8-341f-a4fd-0ce8a67c659c | -11.4853 | -45.7737 | 2026-09-17 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 208277f9-c383-303c-8010-70daca797ce5 | -10.8118 | -46.1594 | 2026-09-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 761856ac-f9b8-390c-8dbe-02d2a2954a9b | -9.8697 | -48.3595 | 2026-09-17 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d6a60eb2-84fd-3850-b92a-6f22eebe1174 | -12.4343 | -50.79 | 2026-09-17 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f2ea985d-72d0-38e7-88bc-ae451193a7bf | -7.0804 | -47.5031 | 2026-09-17 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1afc9b22-484e-3d19-b824-590bd29377e2 | -11.5811 | -46.8919 | 2026-09-17 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ff1176d6-4108-3ed2-8a4e-00c2340f5dd9 | -10.8305 | -46.1796 | 2026-09-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 51f3487a-5cfa-361c-8807-e3b6bd07e43d | -12.5097 | -50.845 | 2026-09-17 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 7c56bcec-2518-30ca-86e0-51746a1b27ca | -12.5289 | -50.8427 | 2026-09-17 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| bc7fd059-313a-3b82-ad6e-f4e36565b19c | -14.1937 | -45.1372 | 2026-09-17 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ebf6fd04-5b9a-3795-aa5f-ee6a576e45f8 | -8.4669 | -44.5445 | 2026-09-17 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 4fffae29-267f-358f-b0b4-8c531d0057f0 | -7.0352 | -44.6396 | 2026-09-17 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 36fc37ac-3845-3fb0-a5a0-3b15fc40e001 | -11.8069 | -58.1759 | 2026-09-17 12:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| a4000ae4-161c-32bd-91a7-b08b875e7048 | -9.8697 | -48.3595 | 2026-09-17 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 68a9ace7-0985-3f29-887e-8cc293a1e717 | -10.7999 | -50.8455 | 2026-09-17 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |


[Clique aqui para ver as próximas entradas](README87.md)
