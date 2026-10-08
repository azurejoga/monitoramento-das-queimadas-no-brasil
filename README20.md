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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68e56e5b-6ba9-3db8-acf3-ec843205c3a0 | -6.7258 | -55.062801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 980f97dc-2085-336b-8a68-b9846f91b0e4 | -3.0385 | -54.2491 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d21c2b05-892f-3784-8ded-14de5494baaa | -7.2791 | -46.803001 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8cac499-67c9-32da-ac44-e7923653846e | -3.2345 | -53.886002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e441e6a-b8b0-39fd-a0fd-eb2269c1bb27 | -1.1 | -54.157101 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffd5c0b3-eddf-38ad-84b2-76e24549e371 | -11.6157 | -43.6763 | 2026-10-08 00:26:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41023a10-3181-399d-bf7c-83fcb0db5cc5 | -4.2984 | -50.789398 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f8863d-b022-31a2-ae09-fb1d009962b4 | -7.2194 | -55.152 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f86c97a-860e-3e7d-9816-339c6be560d1 | -7.4518 | -42.838799 | 2026-10-08 00:26:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bc888377-865b-37f1-a643-ef9bafba84e6 | -2.5099 | -56.244598 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df5d350-31e8-372b-8e09-e04a1c295fcc | -7.3702 | -47.604301 | 2026-10-08 00:26:00 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23c5f2db-f546-3b8b-93bd-58c82d8581f2 | -3.0887 | -54.288502 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2a87d5-77c5-34ab-a7fd-ffa41a245a89 | -2.5482 | -57.378399 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd0843b1-ce45-3d6f-ad28-f6b25f8f4445 | -3.068 | -54.242599 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c5f575f-2f0a-3b40-bc37-f546ef08e402 | -7.3869 | -55.211201 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2241d5c3-c519-3a38-9bc9-230961c477be | -6.509 | -55.383202 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5518efd-b73a-36df-b28c-aab467190bd1 | -4.9232 | -55.844601 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce8a6e7a-e14a-345b-b01b-488f3c1cdbf1 | -2.5067 | -56.230598 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf60893-b6a3-3159-a196-2a3b954006a6 | -3.9752 | -56.210201 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 385f9fc1-fa5f-3f14-9444-a3c906d63034 | -3.0983 | -54.148998 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a76353-a9e0-3aa4-830a-dc3555c89292 | -3.5912 | -54.549801 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 000d95f6-7c3b-328e-b48e-7c48599847ec | -2.9354 | -54.112999 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12cd88d7-7a83-33b4-9cc8-feaa01d2701a | -4.293 | -49.086399 | 2026-10-08 00:26:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60c727e-bd8d-34b7-8ff5-c73e9ba31315 | -3.0551 | -54.230999 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b50a18b-fffd-375d-a2cb-567f339f4c6d | -16.859301 | -40.615601 | 2026-10-08 00:26:00 | METOP-B | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1644f19d-ee90-3d84-9f90-c182ddec852c | -2.9692 | -54.1707 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50af75bf-d21c-37de-8f08-3b42575b66a1 | -3.1242 | -54.172199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1e7336e-b76b-3188-aac0-0f45813a470d | -5.6828 | -53.4972 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8d8ae61-46e2-35b2-bd05-d38989e970cf | -3.7454 | -59.430302 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 422acdd0-2568-375f-91d0-625bfbe40de0 | -3.4792 | -59.572102 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c01c864e-e399-30b8-92b3-b8cd886875e7 | -3.2086 | -53.862598 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468164d1-59db-3d43-898e-6736a980ed3b | -2.7533 | -54.0373 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 631a8d41-61c9-38c5-abbd-0d8012de0d8c | -2.9312 | -54.048599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818d69ce-3ea4-3367-8e05-4359354da416 | -15.5438 | -42.966301 | 2026-10-08 00:26:00 | METOP-B | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84a4429b-9d7d-38b8-86eb-ba7bd5f583c9 | -5.2902 | -60.073601 | 2026-10-08 00:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae815bd-b61c-3ae1-9c37-5d38f0ec3210 | -2.7194 | -57.452801 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40bd9881-3a85-3aff-8c1b-e38f0ba42de8 | -1.8247 | -55.035702 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b154a8-54eb-354d-9c66-c7fdd2449144 | -2.844 | -54.1189 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69662b67-c0dc-376c-8741-f1f1fc6d2918 | -2.8554 | -54.1236 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48b855ea-c2ae-3a8e-8bc1-1fed239a1a03 | -3.2578 | -54.033699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e06c116-cca5-31de-ae8d-76996a3dd344 | -3.0657 | -54.141899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de0c042b-1d15-38e7-9843-c6d69391f1d5 | -3.1367 | -54.364101 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0a41a4d-4fe7-34ec-bf28-4ec83e7e9217 | -2.9814 | -54.0882 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23c96ebb-3be2-3c0f-b8c7-36d8f3a0cde0 | -3.2805 | -54.043098 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54c322c2-b5b7-336f-8586-ce7200512414 | -3.5659 | -54.483799 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa64c4e-a89d-3297-b48f-00800b98e581 | 1.7078 | -55.598202 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccaeead5-f56e-35cc-846b-047bd54dde43 | -2.9908 | -54.129601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ae6585-6084-3620-9455-b01265d46189 | -3.0954 | -54.272499 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf9d3985-9076-39f4-b870-46b9c8b24cbd | -3.0519 | -54.2173 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9fb5b17-5447-32f4-af28-4b44ab90a39f | -6.0983 | -55.712101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ce0d14-dd70-3332-8c3e-c37461c665d1 | -2.9898 | -56.592602 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7998f812-9a81-3ce4-a469-4717fdb8400b | -3.171 | -54.743599 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d51882b2-fb7e-35c4-8ed0-677dbe9ca443 | -6.9247 | -49.629299 | 2026-10-08 00:26:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f6e9f3f-9c13-3126-965f-cbf021c5fede | -2.8777 | -54.176601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aad3354-c9e1-3b45-bfe3-a787b4764e7b | -8.2132 | -46.368599 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29567c80-c9b3-3d18-a93f-c4d0261bc182 | -2.5777 | -56.1343 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 346f329d-eaad-38eb-8cd0-666046985e7b | 1.7048 | -55.6119 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34a2c4cc-541c-38d5-999f-2025f1bcba14 | -2.89 | -54.094101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 106bd385-bd55-3274-9b87-eeacbb87f8d9 | -3.297 | -54.025002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29b2c7a4-4bba-37f9-ad7a-fea83acfa5c4 | -5.9885 | -55.358101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 136c8ee2-8809-3def-8d79-eb69b3391d94 | -2.9628 | -57.758999 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a95ebd29-9730-37d8-a67a-576d838bf2d0 | -2.5503 | -56.287201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a21113f2-9044-33ae-b5c8-3bfc803fb398 | -1.5244 | -54.801998 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77f7c0b0-cb0a-35dd-b12f-752e1f596c4c | -3.0947 | -54.178799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75806096-82fc-3530-9187-1a08a7978a15 | -4.0683 | -59.8251 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3adbb0c7-1d43-32b7-a7bf-8215e9bd50d6 | -2.5043 | -56.128502 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92cb376f-2c77-369c-b215-4fc1c0649e52 | -3.7302 | -58.851101 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aeb6f894-de68-3200-9930-233bab2a175c | -3.0352 | -54.0979 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb6abd3-f448-399c-924f-afddbdaf0515 | -6.6716 | -55.096802 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7747c1-65b6-3c93-bf53-e6a5ab0c8215 | -1.2828 | -55.420101 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f387ad4-dfaf-37b7-a466-43af82d0405d | -3.2129 | -50.5508 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d07614-ab25-345b-8122-e20a1f8cae1d | -2.9815 | -54.7714 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbf030f3-491f-3d27-942a-e9f99ad6b180 | -4.0562 | -59.816502 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cdc1313-1418-37d9-af65-468199bff177 | -5.7288 | -45.168701 | 2026-10-08 00:26:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49229bcb-87a6-3712-87d0-2533bdf9b920 | -2.9656 | -54.200401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aecb8b03-814f-317e-9efe-08695b606771 | -3.1804 | -58.827202 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4511b0e-342b-34b3-abb9-9a0ec2beaf0c | -2.8373 | -54.134899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af173dcc-a131-350c-9a6e-5208172a89f2 | -5.9673 | -55.355499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 133f35da-c9b5-3fcc-b02c-1e022a11d6a9 | -2.4664 | -58.069801 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e048fca4-2a20-3ef7-aef2-5abdaffb2006 | -1.1251 | -57.278099 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a240408-2ec0-3e41-ad35-b8f813cd3907 | -6.2055 | -52.848202 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0adb359-e119-3fb5-af31-5e6f93d02401 | -2.4926 | -56.167702 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3572a1ba-80f2-3fe8-9c7a-94daabb2053a | -3.3099 | -53.854599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 432c4be1-07da-3995-addf-e794e6f3f0b9 | -2.7871 | -54.0952 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf9a8a1-cef5-3ec3-ba05-7e700db85c74 | -3.0488 | -51.224098 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09425f4f-0cad-3e63-9098-71d8b6269f7b | -6.0917 | -55.7286 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46845df7-0077-3932-8497-3c4e09414c15 | -2.3528 | -48.8806 | 2026-10-08 00:26:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38249adf-c0d8-3697-ac1f-95e78892ae05 | -3.0142 | -54.232899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084d1299-0f42-3f41-b9ce-24a238921d6e | -3.0461 | -54.146198 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f61bac1-b86a-38c8-863e-069092617920 | -18.098101 | -42.547401 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| deaab8d5-7998-3756-a191-677b6ccc1c3d | 1.6873 | -55.6437 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35bd51ea-c929-36a9-a461-602395d71350 | -2.8966 | -54.077999 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d70c35e-ca39-356d-8da0-592a3e325be7 | -3.168 | -54.73 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e054ecb-1c01-3e0e-bd53-904a74f52002 | -3.5168 | -59.324699 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 766135e3-1adf-38d1-91b4-42c584f5ca80 | -3.3495 | -54.165298 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2bd227-4220-318b-9448-aada277fc091 | -3.5675 | -54.217602 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e776c17e-f366-3109-9da4-d41f08197fa5 | -3.1014 | -54.1628 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b11617-e0a9-3aa8-8a81-b0f5a3e18c4e | -2.7938 | -57.6474 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5768b946-977e-3740-8f1e-9a9455b197e8 | -2.9479 | -54.168201 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b970946c-8f90-315a-82a9-0b26116d0156 | -5.6977 | -53.472 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README21.md)
