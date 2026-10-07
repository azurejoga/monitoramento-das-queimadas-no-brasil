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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e9993ed-0487-3bc6-bac4-0e27c2c130d6 | -3.50723 | -54.64262 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 636a5569-6818-3339-afa4-03c0729cb8dc | -2.84092 | -54.07269 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f43da4fb-3332-3667-87fe-4f5f25c7e6a5 | -3.28044 | -50.41069 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9aa4a1e-0587-357c-aff2-6e28d43bf091 | -3.02561 | -53.9088 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 9efa95ff-30bb-3023-b634-a514bb2baada | -0.04898 | -53.2518 | 2026-10-07 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eecc47e5-cb25-3fff-b827-dd5e044aff0b | -4.15681 | -55.15854 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0576578b-0753-3559-b8a6-bd25e52e0267 | -4.04421 | -50.98423 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 148d7597-d579-3b8c-be3c-5696f4281df4 | -2.14472 | -54.44552 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6465298f-e71c-347e-bd36-1c8e246d5ddc | -3.67551 | -57.06675 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f90dd44-71c5-3d01-a08b-ed49b1a7884a | -4.35968 | -47.78305 | 2026-10-07 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 507081d4-b9f6-358e-9441-4c57b0b6776c | -3.80319 | -51.98988 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3730f207-150d-3faf-977b-4130bd2da0ed | -3.57869 | -54.3181 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba02385d-2d13-3632-938d-263c0f735196 | -2.99419 | -54.05239 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4a150d5-50cb-37b2-ac17-94d80fc64b7a | -2.76906 | -54.08998 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a43e72b8-3761-35d1-8dd6-ea460b0caba5 | -3.50141 | -59.6051 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 140f70a1-0c65-3da5-aa9c-f1c0ad997be8 | -3.03668 | -53.90006 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c256a16-0ce9-3377-899e-f3d29781b921 | -2.94889 | -54.06561 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 0de1ab58-eb6d-3c06-8789-a7d2189bd38c | -3.2706 | -54.05842 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e29cc2cb-8a95-37d5-af55-c532e29a2c0e | -3.9915 | -56.26443 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62fc35c9-756b-330b-90c7-6bd2a4aa868d | -3.07168 | -54.25162 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17abefb2-b416-3d3e-919f-c10276a8fe4e | -4.1524 | -55.15769 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ddd7f95-f419-3afc-8959-da18bf1bca84 | 2.43587 | -50.83971 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65227bdc-e51c-3572-9079-612267a53183 | -3.77522 | -58.52517 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7ea4128-6f1e-3946-856f-c067e6a1d9e1 | -1.29076 | -54.56743 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccc8fb12-2ddb-3c45-9d42-22b153aa2573 | -3.08023 | -54.25796 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88da362c-dca9-3424-9cd9-56befc2e391e | -2.95602 | -54.1466 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ee10df-1ace-3053-be99-d4b4e64c4bda | -3.28294 | -54.01591 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fdcd2ec9-a57c-3347-a39b-501bacdda106 | -3.73259 | -51.21004 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82627a10-5541-350b-af9c-263f7a1047d9 | -2.80257 | -54.09012 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18f411d1-2044-32b0-83da-a2db7284e8be | -3.20651 | -53.87673 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29a3893e-6b14-3f2a-9040-ed441a5627f8 | -3.46714 | -50.07835 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d59cc90-78d2-3753-a58d-c066b7234582 | -3.00646 | -54.12968 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62177365-1ed2-361f-b311-f00865e4fcd6 | -3.61244 | -54.59474 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2597a75-b950-367f-a9dd-6c89a91532c4 | -3.48116 | -59.57975 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 359ffb7b-4af9-3780-9a77-93052cfb609b | -2.46764 | -56.06656 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adbb9275-755b-3fd0-8902-067bb20dff80 | -3.28603 | -53.86399 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88280d12-a74f-31e0-a0ca-852bf1bdc232 | -4.18641 | -51.13622 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fab55bc-9ab7-3d6f-bee5-e6a81bc90e0c | 2.44067 | -50.8354 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e25e0499-0d88-32c4-a7f4-cc61f46a50ed | -3.50743 | -51.68175 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 497729d8-fb4e-35e1-b91b-36ea8e87db77 | -2.14631 | -54.44322 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41afde2a-623f-3b63-ba16-5d9dbe81cb81 | -3.06277 | -54.2159 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fc2f392-297b-3e38-886a-2ed5c76a69d2 | -3.18987 | -50.56403 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 73f9045a-3f04-3955-bab9-e0ca5a779b00 | -4.44652 | -54.98083 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b83e0fae-9484-3a0c-86f7-b949fd758c8c | -3.67594 | -55.94065 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14a374ac-bb59-3e5b-826e-f8974a661ead | -3.27602 | -54.02347 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8358f69-5f57-3524-a83c-cfde367a5110 | -3.02316 | -53.89285 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f414cb12-22e1-3c14-9283-4d040a6454c5 | -2.93494 | -53.92945 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ed794e-b858-3ac7-b55e-1f52b7d79f70 | -1.50946 | -54.83342 | 2026-10-07 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a14e9900-28d2-3b48-b2f7-47297aacd0cb | -3.27456 | -54.06411 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d965a566-120b-335c-8976-f67f2ceab9c4 | -3.28707 | -54.01482 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4df8f67d-8763-335f-9e8b-c9992242e892 | -3.28473 | -54.02987 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6c426214-1bef-331c-978c-cf8ad8584d40 | 3.59289 | -60.85975 | 2026-10-07 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a84a440-3c7a-3a73-aea6-d9f35dca6945 | -3.06205 | -54.22073 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d47a6a4-4ca8-3fa8-abce-a2f0a9539238 | -3.525 | -54.64759 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06b1c2f8-afd9-3e88-bdcc-2b87cc0344f7 | -3.48801 | -54.616 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 418a502a-9aea-30da-87d7-d2d26677a224 | 3.9832 | -59.73199 | 2026-10-07 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f70bf0d-a669-3c90-9cce-0169bc0a728a | -3.60702 | -55.47918 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8774b95d-ebec-33f4-b935-26f04029189c | -3.21113 | -53.87342 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6f9280a-3a05-3502-84e0-dd7dc82c4c41 | -1.29142 | -54.56313 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b58543a5-0289-37bf-8b1d-a3f022505a80 | -3.74596 | -59.44476 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67f93e92-db55-32dd-b565-e8f89d7d2c60 | -3.28154 | -54.01915 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8caec6cc-a38e-3a9c-8e29-bdaf9c5a7ef6 | -3.55874 | -59.48516 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 962cc867-cc59-3d4f-b3f9-014b27f79322 | -3.11107 | -53.762 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a06ed90-9b9d-38ad-9301-15962c29de13 | -3.43937 | -56.94146 | 2026-10-07 05:40:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 751e8be0-8228-3bd6-b0b1-6ad5b0992c10 | 1.79781 | -55.53296 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13aaf2f-3780-3079-a7d5-601a8f124f12 | -3.1051 | -54.15723 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdf939bb-4c58-356f-a320-c9f6d71c7736 | -2.75337 | -57.66441 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eb39cd2-d5a4-3ad9-9839-cf64278d7b0a | -3.28555 | -54.05564 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3ebeddd-2101-3bdb-86ee-80c7907fee06 | -3.28124 | -53.86324 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 374b1213-1cd7-3135-8bc7-d36daff033ed | -3.15933 | -50.43719 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d03ef939-e833-38f1-9fcc-ff13c7af0f5c | -3.09979 | -54.28549 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 416cc278-bff0-398c-b2f9-e8696cd35a1a | -3.16374 | -50.43577 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a01ffd0d-a17a-3e7d-ba6d-a51fdeab3873 | -3.52251 | -54.63296 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27dddc0c-f610-3b99-be89-21883e40fc15 | -2.13376 | -54.79574 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b5a09013-55dd-335e-bb25-d18b73e1e7ed | -3.9377 | -51.01424 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6849478f-adda-3071-ac09-5fca316d7986 | -2.52945 | -58.09819 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a341a582-4a5f-3045-bc89-0ae0aa3a36ee | -4.11491 | -50.81183 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce0476e0-35f2-3598-9139-c251956bd46f | -3.54154 | -59.48249 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adbec399-8a49-3d34-8184-8ddc50eeaff0 | -3.12069 | -53.76349 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e954336-3918-3f52-85b1-4e50d40770b3 | -3.10702 | -53.75607 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08e2cc11-62be-37f5-aa2a-a6be4c3e2efd | -2.76511 | -54.0844 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9be2da6e-c4e9-36bd-aad7-a390fceefafe | -3.28695 | -54.02163 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5bcb11bf-a589-31fd-a170-fc8a9e7cd5e7 | -1.36234 | -55.71442 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2277249-21ee-3123-917c-143d7807d928 | -3.07487 | -54.26198 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6ba62f8-da61-3a0a-9789-51638ae65372 | -3.06217 | -54.1561 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c3dbeed-f20a-3d15-831e-7cc59220f535 | -3.27124 | -54.02958 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 14620962-24a4-3c12-a1b3-3ae20dbbf12c | -3.28368 | -54.01089 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7e95b5f-5257-369f-96b4-6e9ac544d853 | -3.27956 | -54.07158 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c717ff80-83b6-3b08-b263-0c3a035fd385 | -1.18833 | -54.13986 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea76f573-91e4-3726-b000-9de1978cc3ee | -2.87406 | -54.20197 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7a295c2-35b4-3545-bf96-4fed0a13dd24 | -3.6793 | -59.62886 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37585373-8e91-3d45-ae75-6b26a1b87f5a | -3.24059 | -53.8728 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15d6f24a-3e51-32f0-b1f2-8ddf6d266ce6 | -3.93614 | -52.18838 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 441f1837-68f5-3307-b4ad-393ed6a96c69 | -3.40233 | -59.59014 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ac742dc-8b1e-3ebe-b03f-36626cf354a6 | -3.7466 | -59.29125 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b34a5e5-97e7-36c4-a075-b62c389b7d67 | -2.10679 | -52.06815 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73df951b-d627-3928-9578-b125901f2c64 | -3.68257 | -55.95324 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45f5f489-5f9a-3114-b4a6-4f06d92a9969 | -2.48061 | -56.09048 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 842b1d2b-3151-3429-9af4-3b98c3b7c314 | -2.76833 | -54.09479 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 45922a6a-d1cd-3fff-9eed-cfb8df8e683b | -3.27928 | -54.06481 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README107.md)
