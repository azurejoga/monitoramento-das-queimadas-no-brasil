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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f5135f1-1a21-3162-9a69-9830d964dd42 | -3.78773 | -60.75697 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aff79ca8-f03e-3544-b094-1f4369b8fbe4 | -2.85665 | -60.9121 | 2026-09-22 01:02:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 66d1588e-5f7e-38c0-a68e-cc0bb3790171 | -3.6797 | -60.61951 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 684c0c60-b0c1-3da3-98ab-e1decf54e6f2 | -3.9058 | -60.60236 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ba0cf165-c07a-3295-8d34-966e50485edb | -2.41715 | -58.27318 | 2026-09-22 01:02:00 | TERRA_M-M | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7f53f9b6-0039-3681-b17b-af86425105a6 | -3.54563 | -60.58012 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 70c29d69-3d67-3aad-83fe-bfe5e5d0d4fa | -3.42443 | -61.32224 | 2026-09-22 01:02:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e48256ff-461a-3cb2-9c83-bc3922d9878d | 0.16646 | -60.4959 | 2026-09-22 01:02:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b25f514f-0949-38bb-8547-10a8250f0e89 | -4.08919 | -62.09899 | 2026-09-22 01:02:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10a25b31-987f-3cb5-beb9-02592474e87f | -3.14779 | -61.39293 | 2026-09-22 01:02:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6b205a6-9181-3b67-b6bb-2c0e902470ff | -3.4037 | -59.58624 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 27.4 |
| d952d455-1c33-32c0-a723-9b241a3794a4 | -3.33816 | -59.85266 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 34e6d66c-5888-3c30-bcbe-9fd18a899a18 | 1.77627 | -60.22731 | 2026-09-22 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6641c0c0-a5b8-32d5-9482-cc3cc7a61479 | -3.46419 | -59.53636 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 77d855c4-e56f-3e20-94cf-cd3f8701940b | -2.85633 | -57.79547 | 2026-09-22 01:02:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a706146e-84da-3d17-9337-f152151f958a | -3.92164 | -60.55772 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 111c5002-856d-3677-b8bf-0bf3d4017746 | -2.85981 | -57.81928 | 2026-09-22 01:02:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 1f359063-f6f3-3fd4-9358-70514626286f | -3.68856 | -60.60409 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4ca2a0af-ddb0-382f-a3a8-8099d4da27c6 | -3.28716 | -57.85112 | 2026-09-22 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 9d587f10-e2a0-35d3-ac26-4da44091ec88 | -3.42208 | -60.19888 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 95dc3a06-7bad-3c00-8b78-f926f2e36f96 | -3.0698 | -61.26995 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 669eef58-6c38-3a66-813c-380c4a250df5 | 1.53673 | -55.90124 | 2026-09-22 01:02:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 89fea176-1431-3de3-a7e1-51468890ae84 | -3.42263 | -61.3098 | 2026-09-22 01:02:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fffd2ca6-dc74-3f5e-a408-da4e0f5f18e3 | 3.30892 | -61.2734 | 2026-09-22 01:02:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d71fa59a-1d98-3d9e-a55a-50427db175f4 | -3.71925 | -60.58535 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| c870e184-3d47-3cf8-9362-d7003d45ba5c | 1.52958 | -55.93571 | 2026-09-22 01:02:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 459c2dfe-c9dd-376d-8d1b-7b9f80a2d93e | -3.07161 | -61.28261 | 2026-09-22 01:02:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 83f253be-65cd-3977-afa3-46f6a1ae433c | -3.41202 | -60.20595 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9f76552f-f2c6-3bd4-b77f-f413c184005a | -3.90382 | -60.58859 | 2026-09-22 01:02:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 618e4a18-b966-3537-bde1-4a77ffd44655 | -3.36954 | -61.28527 | 2026-09-22 01:02:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f7c723a9-1867-3f47-b7e9-ade185cd95fd | -3.68653 | -60.59022 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 6cfff12e-da00-335d-9c6c-009ef559fc5e | -4.08763 | -62.08814 | 2026-09-22 01:02:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2182a369-e6f8-3bcb-aaf4-a815cfd76b0f | -3.6845 | -60.57631 | 2026-09-22 01:02:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| d5cd2db4-ef71-3152-b18b-6dad8891f372 | -9.2573 | -46.1647 | 2026-09-22 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 7eeb2b36-2c8f-3f7e-b0c7-7d06fef55bcf | -12.165 | -47.3948 | 2026-09-22 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 287adbee-a757-3504-aee7-cf814a491044 | -18.727 | -46.9345 | 2026-09-22 01:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 416ca89c-4112-3b3d-ae64-679436eed1c9 | -6.5898 | -44.15 | 2026-09-22 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5974e02a-001c-3eeb-9fb4-fd37a5920643 | -9.2576 | -46.1422 | 2026-09-22 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.4 |
| fc44c125-45a2-399b-a7d0-54aeb80b6ff8 | -7.5889 | -57.6757 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 5abcdb7c-e3f9-3e59-b4ab-3837f93c2fa9 | -12.1653 | -47.3724 | 2026-09-22 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1c141cf7-33ab-3e52-9332-478fc9535e35 | -6.1109 | -57.684 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6c1c502a-6bf1-3fcb-9f19-ee5391683aac | -3.405 | -59.522 | 2026-09-22 01:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| a137d437-dd94-3c0b-8a40-8d0c364da194 | -11.3255 | -54.0487 | 2026-09-22 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| d03d153b-6d19-302f-96a8-2ca6ea7ebbb1 | -5.7571 | -45.0613 | 2026-09-22 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 417a9822-3180-3f00-92e9-537cb0126926 | -5.7756 | -45.0826 | 2026-09-22 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9b54bdd0-6882-3509-a144-d0500d322bc5 | -12.1458 | -47.3974 | 2026-09-22 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 1722a8d5-d0c7-37d7-a929-6344474f83ab | -9.2383 | -46.1668 | 2026-09-22 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 474.2 |
| 849f76a1-70bd-33ba-a5ac-7ba0e1e66644 | -11.3066 | -54.0505 | 2026-09-22 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 29e4aff7-a728-30d0-96e7-903f9c068d20 | -6.0549 | -57.8227 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| aff473fd-4cce-3e81-91a2-82d18d1e4a6c | -6.0928 | -57.6262 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 289b6ae3-586b-375d-b1d9-f8d9eaa214dc | -5.7567 | -45.1067 | 2026-09-22 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ec6d37b7-f5a2-366a-8ba3-3ad92e0f155d | -8.6169 | -54.6328 | 2026-09-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5b3b7daf-ae15-31b2-8fa1-3f27e8b95dab | -11.7672 | -50.8253 | 2026-09-22 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6b355228-31c1-338c-b1e8-6de1d9b89e87 | -11.4213 | -47.338 | 2026-09-22 01:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| fc020009-19cf-3d3a-af02-6b266a0d99de | -3.0542 | -54.4081 | 2026-09-22 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 20e9db05-7967-3c5d-87da-164c5fbf1521 | -9.5594 | -66.0359 | 2026-09-22 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 306c7ffc-a35a-3192-8300-33d686a2c40a | -6.467 | -59.9902 | 2026-09-22 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 45e795bd-4403-37bb-a37f-6bd65d7a1b18 | -8.2576 | -55.2403 | 2026-09-22 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| eb18e9b7-c03f-3d7c-954e-9d08b3a1c72e | -6.571 | -44.1516 | 2026-09-22 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 38fefb25-fc13-3a16-8424-c0e418e090c1 | -8.257 | -55.3005 | 2026-09-22 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 26757dd9-cf24-3035-82d8-7e17b491d3eb | -7.5888 | -57.6953 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 39877170-7d0e-3d5b-b127-8b7d0b624596 | -5.9333 | -59.9899 | 2026-09-22 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| c93d509b-0710-3010-8e53-9f028374b674 | -11.3257 | -54.0282 | 2026-09-22 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |
| acfecc4c-ccab-3b0b-9e18-f4dc144e92ea | -18.7466 | -46.9534 | 2026-09-22 01:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0ab5004e-6241-3a8b-934d-dedeac551f8d | -3.2212 | -53.9422 | 2026-09-22 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8fed63fa-d949-3241-af01-2d208508947f | -7.7144 | -61.2419 | 2026-09-22 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2e5634df-7175-3f72-a046-6974272fc024 | -5.7569 | -45.084 | 2026-09-22 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 368.4 |
| 57eb02bc-7b91-384d-981d-db6078e4cdad | -11.6793 | -43.4684 | 2026-09-22 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 21a681b6-70ed-3f7a-af01-a69e8534372e | -2.8608 | -57.7994 | 2026-09-22 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 82bfb8ef-26c1-34f7-9792-9b35f3296ea9 | -7.5704 | -57.6766 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1bb68b82-064c-3a5c-8f93-594aaa016ae6 | -11.7675 | -50.804 | 2026-09-22 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f009001e-6278-3338-8a83-81c5116d6d0f | -5.7382 | -45.0853 | 2026-09-22 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 614bca25-8173-3334-bcc3-c44f259b4984 | -6.0365 | -57.8235 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 7f73db6d-b05c-35eb-8de1-44921400957a | -9.2386 | -46.1443 | 2026-09-22 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 427.6 |
| b0b40b1c-16de-359a-aafc-b2c1dae61843 | -5.9334 | -59.9707 | 2026-09-22 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1b0e71c2-4861-3cd3-a10d-0676248a54d4 | -8.2574 | -55.2604 | 2026-09-22 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 553d9cc5-930e-38e9-9a71-a250553e6257 | -8.7916 | -44.2778 | 2026-09-22 01:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| fc7686d5-2841-314d-9b8a-b3ef2e8b300a | -12.1462 | -47.3751 | 2026-09-22 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 4b76d507-7d5c-3c49-980e-6b46f671b367 | -6.0925 | -57.6847 | 2026-09-22 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 69d26e41-6cfe-3e49-b81c-8d204a8d0251 | -18.7472 | -46.93 | 2026-09-22 01:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 93ab5907-154f-3036-b4d7-896a01e02e44 | -9.25 | -46.11 | 2026-09-22 01:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab26f0c1-c17a-338b-8843-7f44b147efb1 | -9.25 | -46.16 | 2026-09-22 01:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e0b4ec8-53ca-3544-a620-544ab1923c70 | -9.28 | -46.17 | 2026-09-22 01:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37b33a91-d136-3068-ac46-e2f588f9a33c | -10.59 | -53.98 | 2026-09-22 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3ef7e25-e11f-3f75-b13d-4b64d6195f29 | -5.73 | -45.09 | 2026-09-22 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a259f60e-2cc3-3d30-abe6-2b2b7c2e063e | -9.22 | -46.16 | 2026-09-22 01:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7c91d84-890e-36ad-be6f-00e35b76e4db | -5.76 | -45.09 | 2026-09-22 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6feb016c-6c55-3780-a1f9-d20f8a0cab81 | -4.3025 | -49.1152 | 2026-09-22 01:19:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 199f9577-945b-3074-92ea-cfb22cf94b21 | -6.005 | -57.709702 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09814334-cf96-32ce-95cf-b681bff3c7a6 | 1.5505 | -55.881401 | 2026-09-22 01:19:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebb082aa-1964-3638-a39e-db859f250b0c | -2.418 | -57.903999 | 2026-09-22 01:19:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 258db77b-cdf3-380b-8090-6a7d54877a87 | -7.3186 | -55.2099 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6690aed-f517-3ef6-adf2-409903297f68 | -3.0016 | -60.797901 | 2026-09-22 01:19:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebe7b00-43f5-31b8-bd2d-336e1517f965 | -3.3421 | -59.8536 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3947c615-5d4f-3a1a-8ed0-504b44b8e7dc | -11.3996 | -46.758999 | 2026-09-22 01:19:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdeca346-5017-343f-86c4-be34b002782d | -10.6075 | -53.9725 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b92907dc-aa84-3651-9818-2a34f2c2d531 | -7.5941 | -57.664799 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 559e5b66-ab25-307b-8bb1-ac40701d74aa | -7.5827 | -57.66 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86b98eff-2e7b-3059-bf4f-a1bc0df89a59 | -4.0711 | -56.231098 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abee6c65-bb41-3606-a1fc-b85c2e2f7b2f | -2.672 | -54.969002 | 2026-09-22 01:19:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
