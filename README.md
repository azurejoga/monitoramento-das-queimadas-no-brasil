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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 800ec2fd-e255-390a-a40b-4ba71c0c3a84 | -12.3891 | -50.0218 | 2026-05-02 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d14275cc-a719-3d52-9cd8-2153e58d929b | -12.37 | -50.0242 | 2026-05-02 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| c1d4c958-3b16-3bea-93d1-1ac316a97523 | -10.9815 | -45.0874 | 2026-05-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 0efef39b-6e5e-3338-9ebc-98d55cb0c5d6 | -10.9819 | -45.0643 | 2026-05-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 488bf191-4b0c-3952-a175-c802bc2fb02f | -12.3887 | -50.0435 | 2026-05-02 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 98e341ec-7b7c-37ff-85bd-8e972c8629bd | -10.9624 | -45.09 | 2026-05-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9d77a515-1d98-3510-b457-0e61a3a118f5 | -13.8178 | -43.6504 | 2026-05-02 00:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f581d128-9994-3071-8d7d-7d4e0056a39d | -12.3696 | -50.0459 | 2026-05-02 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 247.5 |
| b9968fac-5615-33df-a795-a9e3e08d72fa | -13.8178 | -43.6504 | 2026-05-02 00:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 586fcafa-4f8b-3523-8d04-a6d2444172bb | -12.288 | -57.4024 | 2026-05-02 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2a1cdb9b-afd3-38a4-86ab-c5f9e9660733 | -12.3887 | -50.0435 | 2026-05-02 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| cf22cb82-23d8-339d-b8da-cb6541c79e9e | -12.37 | -50.0242 | 2026-05-02 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 612e003f-19c2-361c-8dee-c2b0d8ad0836 | -12.3696 | -50.0459 | 2026-05-02 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 2fefeaef-afc4-36ce-9441-8768c96ca024 | -10.9815 | -45.0874 | 2026-05-02 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3f4f7ba0-8162-3e4b-80f5-d043ccafaddd | -12.3891 | -50.0218 | 2026-05-02 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a8ee87bf-f851-3f5d-944b-17db18f27dbb | -10.9624 | -45.09 | 2026-05-02 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3053d23c-e541-3b74-ae29-fe23adaedae2 | -10.9819 | -45.0643 | 2026-05-02 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e4383f74-1c6d-3822-9af7-1986f36199d1 | -12.3891 | -50.0218 | 2026-05-02 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 455b81ad-2528-382c-884b-2ebf8986170c | -12.3887 | -50.0435 | 2026-05-02 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 8a19b894-853e-3ab1-934b-010f6019fe13 | -10.9815 | -45.0874 | 2026-05-02 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| fcd5bec8-0b57-362f-a301-da1461beed79 | -10.9819 | -45.0643 | 2026-05-02 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8642b131-a5cb-32d4-9939-a9561a9b4337 | -10.9624 | -45.09 | 2026-05-02 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8d5025cd-2bc9-38f6-8c43-d2f943b48f02 | -12.3696 | -50.0459 | 2026-05-02 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 8496f446-c67b-36a7-a057-e409f02d7507 | -12.37 | -50.0242 | 2026-05-02 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 68e31189-f1b4-3453-9a8e-149048618994 | -12.37 | -50.0242 | 2026-05-02 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| be27af2e-fdd4-3b32-a2cd-33b017a00fcf | -12.3887 | -50.0435 | 2026-05-02 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6a1cc5e9-12af-35fa-bd83-e6448bcc5165 | -13.8178 | -43.6504 | 2026-05-02 00:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a563c4c3-aa4a-331b-8568-e4f09f247e14 | -10.9624 | -45.09 | 2026-05-02 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6f785c5f-0076-3028-8f8a-23ebd55291ff | -10.9815 | -45.0874 | 2026-05-02 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 9aa3c6e8-5d15-32b2-9dac-95b1b04010a5 | -10.9819 | -45.0643 | 2026-05-02 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3af7b1b5-7dc3-3247-ab57-1eeb9c15c994 | -12.3696 | -50.0459 | 2026-05-02 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 259.5 |
| ad9e290f-f1a5-315d-8cde-6e04371b5f57 | -12.37 | -50.0242 | 2026-05-02 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 5c680136-a4a7-37eb-b000-d23225683141 | -12.3891 | -50.0218 | 2026-05-02 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7c42afea-7eb8-346b-bde8-4fd2c8ccd62f | -10.9819 | -45.0643 | 2026-05-02 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 9b0a53fc-0b7a-3dfe-b545-b61471aa8870 | -10.9624 | -45.09 | 2026-05-02 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d93d9da3-c91e-318d-acad-1156839eadf0 | -12.3696 | -50.0459 | 2026-05-02 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 9543b8a1-1a40-30b9-bf36-8f558b06afc7 | -12.3887 | -50.0435 | 2026-05-02 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 953aa865-7f9e-3e9c-ba53-ca2ce3b805c6 | -10.9815 | -45.0874 | 2026-05-02 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 0434e980-6844-3ee7-adad-4817bc28fb24 | -10.9815 | -45.0874 | 2026-05-02 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 5627bbb0-5ffc-302a-af1a-90e2d7d3142e | -12.3887 | -50.0435 | 2026-05-02 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| dcd317cb-88cf-3aec-a7fa-a5188261adc5 | -12.37 | -50.0242 | 2026-05-02 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 115c76ef-33b7-3dfc-b260-b4a05a1303ed | -12.3696 | -50.0459 | 2026-05-02 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 4f79dab7-7393-3a27-8422-257501f5967d | -10.9624 | -45.09 | 2026-05-02 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6c143c73-cf27-3bd9-bb40-2af7df7b0fc7 | -10.9819 | -45.0643 | 2026-05-02 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 09c688aa-9cb1-3820-b5f6-5ac3318026ea | -12.3891 | -50.0218 | 2026-05-02 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f5c63efd-3cb9-3d30-9439-d502ab44acce | -10.9819 | -45.0643 | 2026-05-02 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8252536c-966d-30a1-a9be-4032e20302ae | -12.37 | -50.0242 | 2026-05-02 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| b02ad22d-8c37-3db8-8cba-97494056fbdb | -10.9624 | -45.09 | 2026-05-02 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 520e69bd-8555-3868-95bb-bfa157231bd1 | -12.3696 | -50.0459 | 2026-05-02 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 174.9 |
| a43572c9-9962-35e9-9fac-b5d0d9f2e791 | -10.9815 | -45.0874 | 2026-05-02 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| fa4c458d-3100-3638-bdd0-686e8c9a751b | -12.3887 | -50.0435 | 2026-05-02 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a03a43e3-40d8-32db-8766-f06cb9bb5222 | -12.3891 | -50.0218 | 2026-05-02 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 93e1c62d-f413-3f16-a73d-7aef72ceafeb | -21.66367 | -56.31465 | 2026-05-02 01:09:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a76e2576-bf9f-3523-869d-c09ef51eafaa | -12.3887 | -50.0435 | 2026-05-02 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2e0ae852-f0df-391c-bd1f-0338042fdf6c | -10.9624 | -45.09 | 2026-05-02 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 8bccd185-e76d-36e2-b015-bc70e8f124f9 | -12.37 | -50.0242 | 2026-05-02 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9e666767-f5fa-34b0-a468-e4a27fe8dbc8 | -10.9815 | -45.0874 | 2026-05-02 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 8e74aa3e-7bba-38b6-be59-23666dd8c05c | -12.3696 | -50.0459 | 2026-05-02 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| f15c162a-e164-3af4-9991-809bca2c1a1e | -10.9819 | -45.0643 | 2026-05-02 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 72a36259-4add-33f8-be8a-1ad7298885c6 | -12.3891 | -50.0218 | 2026-05-02 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 81567a4a-2669-320f-83a0-a8a7d9252a35 | -8.64211 | -63.99703 | 2026-05-02 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e7a3f7d-ba4e-3604-a2eb-191db312c37c | -12.29801 | -57.40284 | 2026-05-02 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| d88d1c45-cafb-329b-ac4f-61a2d81d9c6f | -12.29517 | -57.38499 | 2026-05-02 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5a78ecda-0901-3983-bd7b-1c9438a03513 | -12.28591 | -57.40483 | 2026-05-02 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cb7a6ea3-9f38-3932-9977-5b44bd89543a | -12.28305 | -57.38705 | 2026-05-02 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b215b86b-dc24-3657-8a9d-8e218b424bc4 | -7.86709 | -61.50074 | 2026-05-02 01:13:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a2936ef9-c514-369b-a652-622a7579a8d4 | -10.9819 | -45.0643 | 2026-05-02 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| df31a005-e596-3359-a5f8-5644fb90e9f0 | -12.3891 | -50.0218 | 2026-05-02 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4c0e9e3a-f47e-334d-914e-347888e4dd40 | -12.3887 | -50.0435 | 2026-05-02 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 7ee3d7ca-f2ea-3dbd-a73c-ee76b0951d89 | -10.9624 | -45.09 | 2026-05-02 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 45bbdac3-08d2-3050-84a8-cfd38e6f75b2 | -12.37 | -50.0242 | 2026-05-02 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 02d66fa0-3e49-382e-9e73-4d64997c89ed | -12.3696 | -50.0459 | 2026-05-02 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 64b9ed61-84ba-38c7-8faa-c84fd098cfb1 | -10.9815 | -45.0874 | 2026-05-02 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 16a92579-7926-3f10-815c-54f6f5309475 | -10.9819 | -45.0643 | 2026-05-02 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 04d4250e-248f-39f8-b7b1-d3860eafc7e4 | -12.37 | -50.0242 | 2026-05-02 01:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ad3827d7-a570-3eab-bdef-1cbdc05ce9c9 | -12.3891 | -50.0218 | 2026-05-02 01:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ce5b1e48-311a-3c0f-aa7b-16d69a1c7026 | -10.9624 | -45.09 | 2026-05-02 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2683933c-fc73-3925-bd04-cef583c2c68e | -12.3696 | -50.0459 | 2026-05-02 01:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| bddeccdd-1b6f-307a-a955-1ab0ff678d63 | -12.3887 | -50.0435 | 2026-05-02 01:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 9d3c5df1-4285-3112-b5df-e35d0d979695 | -10.9815 | -45.0874 | 2026-05-02 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 8521f458-1c07-30e4-bb97-8a9a86f8e346 | -12.3887 | -50.0435 | 2026-05-02 01:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 104fd716-23e4-32ca-8ebe-88a344ab862b | -12.3696 | -50.0459 | 2026-05-02 01:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| aa134b00-881e-36d0-a9fb-3cd537afd597 | -10.9815 | -45.0874 | 2026-05-02 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 074cec7d-f82d-3771-9534-706eeab6163b | -12.37 | -50.0242 | 2026-05-02 01:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 34fcd134-361e-362c-b52d-9adfe79c2d3c | -10.9819 | -45.0643 | 2026-05-02 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 273c3c2d-8e7f-31d0-91b5-33710933a9d6 | -12.3891 | -50.0218 | 2026-05-02 01:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4f3ae131-c22f-38b8-88a4-aa01f09a75c8 | -10.9624 | -45.09 | 2026-05-02 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e22f3131-00c6-3ea4-acaa-a5553e44afab | -10.9815 | -45.0874 | 2026-05-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 62d53e27-fee4-3a9c-aeb6-fab67f60e55e | -12.3891 | -50.0218 | 2026-05-02 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 44c97d4a-f39d-320b-a677-4f1331abe087 | -10.9624 | -45.09 | 2026-05-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 015e2b06-6455-306e-9377-485408c9b912 | -10.9819 | -45.0643 | 2026-05-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 454d919e-0b9e-3ed7-9467-7de32d510903 | -12.3696 | -50.0459 | 2026-05-02 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 6f78b22e-55c6-36b1-87ca-45be6de6c310 | -12.37 | -50.0242 | 2026-05-02 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 63193f84-41dc-3336-a3cb-82c95b19a08a | -12.3887 | -50.0435 | 2026-05-02 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c35e5e18-0c28-3591-8b18-e7776b80237c | -12.37 | -50.0242 | 2026-05-02 02:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8a6a81ad-4f54-3806-8376-da54df406b8c | -10.9815 | -45.0874 | 2026-05-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| bf7ce7d4-35ff-3046-97a3-bf50024541c7 | -10.9819 | -45.0643 | 2026-05-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| dcb79c99-5457-33dc-85d4-87102566fcc5 | -12.3887 | -50.0435 | 2026-05-02 02:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f914ce68-d4b9-3a83-9ce7-d6ce79b23252 | -12.3696 | -50.0459 | 2026-05-02 02:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 2b6f3c89-e626-3d08-aa27-82ce594c45fd | -10.9624 | -45.09 | 2026-05-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |


[Clique aqui para ver as próximas entradas](README2.md)
