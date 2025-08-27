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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e43300b-7d29-3846-b09a-7ba3cbcb02e1 | -9.1009 | -49.5621 | 2025-08-27 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| c736fffa-c0dd-3dcc-b42e-98c3e9bcbb5f | -9.0821 | -49.5638 | 2025-08-27 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 78851248-4d53-3e72-b30f-ea5e8312d2f3 | -9.1715 | -59.5599 | 2025-08-27 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e6834ee0-96d1-3a09-81c3-bf0a86c2895f | -8.8842 | -60.7507 | 2025-08-27 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 680ae724-d839-3bda-b6ff-7771a00162ed | -9.0819 | -49.5853 | 2025-08-27 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2569928a-b649-36bb-9885-bdc7d42b7cc4 | -9.3878 | -60.5143 | 2025-08-27 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 86c69916-3e6e-3144-adab-2b32bb82357f | -8.9028 | -60.7498 | 2025-08-27 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d57e43d4-30ba-304c-80c1-d317352db6f8 | -9.4249 | -60.5316 | 2025-08-27 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 25a4a0bb-d614-3f91-9bc8-f57db3ead136 | -9.1007 | -49.5835 | 2025-08-27 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 6f277df4-6de3-3247-bce7-ef8bfb726f6d | -9.0816 | -49.6068 | 2025-08-27 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 31227455-7138-3829-bf4f-b6b3de873e57 | -13.1644 | -45.2897 | 2025-08-27 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0d676db8-32dc-3ac2-9397-494efa7cea40 | -8.7164 | -64.0231 | 2025-08-27 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 65ba5f3c-c108-3132-8ea0-9e930c7f8637 | -9.425 | -60.5124 | 2025-08-27 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9f2eb13b-db4e-32bb-9669-9551cedef48f | -6.8412 | -58.9746 | 2025-08-27 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fa818bd4-2236-315d-bf0b-6729536a4f63 | -9.1009 | -49.5621 | 2025-08-27 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 90dc01de-1e8d-3c36-b277-f5ade051dbbd | -9.4062 | -60.5326 | 2025-08-27 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 6f37fcde-f0fc-3cd4-bc97-0b65dfb100e5 | -13.4027 | -46.9214 | 2025-08-27 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 4d4c087f-5878-3378-b23d-6415417cbdd1 | -9.1715 | -59.5599 | 2025-08-27 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3d27769f-4ed0-3fb5-bcab-b0af3f2a20e0 | -13.4032 | -46.8987 | 2025-08-27 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| be532749-f5c6-32a8-8576-d212c11d4b58 | -13.1837 | -45.2865 | 2025-08-27 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 994558f4-79d6-373c-8485-0c06ab4524de | -6.8228 | -58.9753 | 2025-08-27 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2208463a-941f-3b73-bf9b-18f43a853634 | -9.0819 | -49.5853 | 2025-08-27 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 68aada27-daca-3625-a163-cbfeb8423748 | -12.9072 | -44.6346 | 2025-08-27 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 7823e291-60b8-34c3-93b8-a871d6d5090f | -9.4064 | -60.5133 | 2025-08-27 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 199.9 |
| bfbebf74-1580-3b2f-971b-ba3026624a3e | -12.9068 | -44.658 | 2025-08-27 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| f838459d-87ce-3aa4-8374-7107c6e6794d | -9.7915 | -64.265 | 2025-08-27 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 49ab6ef0-d11b-36ef-896d-2e194a30c26f | -8.9026 | -60.769 | 2025-08-27 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a4be39c2-60e7-324b-a487-5904741e0ff8 | -5.118 | -43.2198 | 2025-08-27 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f71a0f6c-74f2-3618-9e5f-b34bc6c10e2b | -6.8229 | -58.956 | 2025-08-27 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2db2b16e-c5d7-3e11-9830-ee29acdc4a30 | -8.8841 | -60.7699 | 2025-08-27 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d2e6892e-41fa-3164-9172-f1a67e7794cd | -6.8413 | -58.9552 | 2025-08-27 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d126e896-5cc7-386c-a015-8f989da837b7 | -9.1529 | -59.5609 | 2025-08-27 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ed5677ef-73e4-3c9b-ba1c-072413cedb3f | -9.4065 | -60.4941 | 2025-08-27 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 8372e713-78a0-3869-8e2a-67a094a18925 | -9.0821 | -49.5638 | 2025-08-27 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 275985cc-3bc2-3f7a-acd7-2964c530964c | -5.1181 | -43.1964 | 2025-08-27 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 4033b58c-3f4c-3b8b-8396-6ee376cd7606 | -8.9453 | -65.989304 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08f9fd50-fafa-3d68-b8fc-d98608879e32 | -10.253 | -64.4935 | 2025-08-27 02:04:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 72282194-a3d5-3c5b-9d8a-d28ab7f777e5 | -8.6865 | -63.992199 | 2025-08-27 02:04:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe9080c-60f6-3aab-937f-77a065f5509d | -8.903 | -65.904297 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e79b0e0b-af25-353c-96f6-363cf998a8ff | -8.9088 | -65.926903 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a05b2ce2-fa80-3758-bdc6-50adde8db462 | -8.9281 | -65.921898 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb9dfe5-552c-3cdb-9485-6ec9efa9cc80 | -8.9299 | -65.969398 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d79e3ae8-ea17-30fc-82e3-f5eb5d796632 | -8.9338 | -65.944504 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f353a19-8ca9-37f8-856a-4fe1261ce7cb | -9.0546 | -66.055496 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3213386d-cd7a-3de7-8479-d5f3fb67b6ed | -8.9492 | -65.964401 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca40baf-56ba-3318-8f1e-59ad2f4b46d6 | -8.8992 | -65.929398 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a52bec16-8e60-370b-a5f2-84db0d6be165 | -9.045 | -66.057999 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5687a78a-a613-3b03-a124-dc836b82fc51 | -8.9145 | -65.949501 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5e86b3-2e58-303e-919b-c798f31e6683 | -8.9184 | -65.9244 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e71238d0-b8f2-3082-be2a-878456399488 | -8.6946 | -64.022903 | 2025-08-27 02:04:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17a79b00-1cb2-3166-a9f4-4eed5a9ba70c | -8.7041 | -64.020302 | 2025-08-27 02:04:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b3b3fad-6ec2-3dd0-a7bf-bbe4452cd747 | -8.9396 | -65.966904 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1d6fba2-c9c5-324a-a929-fbde8e76dbab | -8.9435 | -65.942001 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68d4a5cb-a120-3557-844f-aa4bc4286c11 | -8.9242 | -65.946999 | 2025-08-27 02:04:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6613efd-2a02-3149-a0a3-0d0f729be174 | -8.9026 | -60.769 | 2025-08-27 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3cf5278f-a71a-3369-ab50-f733510a910f | -9.4065 | -60.4941 | 2025-08-27 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| d3488da8-ad69-3ff3-af27-8c3138fd12a5 | -9.1715 | -59.5599 | 2025-08-27 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| fa47fb27-e018-3adb-8795-04f8866556a0 | -9.4249 | -60.5316 | 2025-08-27 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9cf20029-9de3-36c0-84f9-af10e7a2197a | -9.0821 | -49.5638 | 2025-08-27 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 785c968a-459e-3ea3-b6c9-b26deb057af0 | -9.4064 | -60.5133 | 2025-08-27 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 82f6ed86-da51-30aa-8dbe-3953b0b8b882 | -9.1007 | -49.5835 | 2025-08-27 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| b9205e2c-fb59-3500-8a65-368d9cc366f7 | -6.8413 | -58.9552 | 2025-08-27 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a0c4047e-4855-3e88-8453-20319904b3ec | -13.1837 | -45.2865 | 2025-08-27 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0ad9c6dc-245a-366e-8972-04e4c01b6a3a | -8.8841 | -60.7699 | 2025-08-27 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 79d0ba45-5177-3281-85b4-340a34c43563 | -9.4062 | -60.5326 | 2025-08-27 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| d9f46323-1505-38ab-b155-864415665fda | -9.1009 | -49.5621 | 2025-08-27 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| a67b0b00-62e4-34ef-b21a-bb6f4f1e026f | -6.8412 | -58.9746 | 2025-08-27 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0f16d796-de68-315d-b8b4-8e5d500749ab | -9.425 | -60.5124 | 2025-08-27 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 68ea4f25-0e65-3e7a-8783-4ad6d448ed49 | -10.2743 | -64.4907 | 2025-08-27 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.9 |
| dae59588-af59-3ff7-b2cd-901453ceff04 | -8.7164 | -64.0231 | 2025-08-27 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d73cea46-aa78-33b3-80a8-a19a065b398a | -12.9068 | -44.658 | 2025-08-27 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 0ccbf037-fdaa-3d40-9b7e-c415ffafbcb5 | -13.1644 | -45.2897 | 2025-08-27 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| e23cde96-c584-3519-83c3-bf76d253f416 | -9.0819 | -49.5853 | 2025-08-27 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a313bfbe-494d-375d-a405-11779dad9dbb | -6.2459 | -60.0174 | 2025-08-27 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f4cfc0fa-cb3b-3ae2-a487-64d72271ada2 | -6.8228 | -58.9753 | 2025-08-27 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f628e5b7-dd71-3701-a1cb-a8d8ade5f797 | -9.7915 | -64.265 | 2025-08-27 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 4a1b38a2-8e95-30a3-a368-85c8155d702f | -12.9068 | -44.658 | 2025-08-27 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6c1e335f-c135-3f8e-a157-e0a525ef8845 | -9.1007 | -49.5835 | 2025-08-27 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| dd034d3d-456a-35fa-816c-fc323b3c13c4 | -6.8412 | -58.9746 | 2025-08-27 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b82e9fc1-7619-399f-9b82-adba198a7cf2 | -13.1644 | -45.2897 | 2025-08-27 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9f49c2cd-6685-3cb4-9c74-522a4216038b | -9.4064 | -60.5133 | 2025-08-27 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 9a5f866c-f296-3a7f-8f2f-8500a93c7476 | -6.8413 | -58.9552 | 2025-08-27 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0854534d-3ca3-3070-a230-593b6dcaf56d | -6.8228 | -58.9753 | 2025-08-27 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f222107a-3cac-3668-ab54-acb88c1f1b18 | -9.1715 | -59.5599 | 2025-08-27 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3657e369-397f-39bc-b33c-bca38ccf12ca | -9.0821 | -49.5638 | 2025-08-27 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3b0de6c0-5de5-3cdd-bb8b-b6bed2ec84aa | -9.4062 | -60.5326 | 2025-08-27 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 43f7900a-dbdf-30b4-87c9-52e25f757f44 | -8.8841 | -60.7699 | 2025-08-27 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4ebc20d6-fb07-3d60-9ac4-af9bf45bb558 | -9.4065 | -60.4941 | 2025-08-27 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 769f1579-e985-3ba6-b280-151afa5c87a9 | -10.2743 | -64.4907 | 2025-08-27 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| c0444b01-fbc4-36a6-a2be-19a422688440 | -13.1837 | -45.2865 | 2025-08-27 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 821a9841-8ed4-3605-a175-37419422ce0e | -9.1529 | -59.5609 | 2025-08-27 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e15e1529-7e4b-34c9-a318-1cb450a4dbf1 | -9.1009 | -49.5621 | 2025-08-27 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 94f474ea-034e-30d5-bc62-4247828769bb | -8.7164 | -64.0231 | 2025-08-27 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 6249ce88-3417-347d-b14a-2f481cb6a273 | -13.1644 | -45.2897 | 2025-08-27 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8cf4f96a-7f4d-3815-b540-32ac745d80f8 | -6.8413 | -58.9552 | 2025-08-27 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ca9c62c8-41bd-36a0-8f0d-4fe718c65329 | -9.4064 | -60.5133 | 2025-08-27 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 38421838-635d-32f4-bda3-c73942a3a292 | -8.7349 | -64.0224 | 2025-08-27 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 43ff58c6-8f78-363e-9403-d8bb04548221 | -9.0819 | -49.5853 | 2025-08-27 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 0c1261f4-2a97-3d83-93c6-f205bc163994 | -8.8841 | -60.7699 | 2025-08-27 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 065de688-f571-3233-acb5-d410c96c9e89 | -9.8101 | -64.2642 | 2025-08-27 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |


[Clique aqui para ver as próximas entradas](README16.md)
