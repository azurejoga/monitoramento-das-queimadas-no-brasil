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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7eab1fc-c8a6-3048-a8ce-e12fba20b9ae | -5.60378 | -45.95668 | 2026-09-24 05:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c1a1f13-800c-34e7-a82e-07950dd4829b | -4.42404 | -55.08552 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92bfc1e-d833-3fb1-986b-0e76ecdecba0 | -3.23094 | -54.32293 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 894898e9-1380-3dab-8306-ef85ea850296 | -4.98669 | -45.55157 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5bf55977-9347-36b1-b8cf-f25a1fe610aa | -6.61815 | -59.9101 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1948d10-fb26-345e-a289-e28f4ce80778 | -1.19682 | -54.14497 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| caf0bb3d-ec7a-39df-892e-bf8d8fb6b9fa | -8.30741 | -56.36275 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eddee909-8eeb-3574-82f5-f88e2ade07ae | -6.62199 | -59.93805 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3431b1cd-5681-3ebb-89cb-52cb606be31a | -6.67063 | -58.54951 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa25ffee-d1f2-3742-a7c6-c230c0aceabc | -4.55289 | -54.93944 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ed1a9db-ee2c-34b2-a4d0-9d14982528e9 | -4.94371 | -56.01681 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e50e2a0-27dc-3c4c-a36b-bf1c665873fa | -6.43812 | -59.95352 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 676365c6-0983-37ec-b0fc-3e78d2e22814 | -1.62103 | -54.91344 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e11c4870-3db6-385a-9deb-155066a7c864 | -7.46525 | -55.00084 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d67167d0-340c-3f82-bc31-e05f1e8c5cae | -3.76391 | -54.8187 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d372abe-0e50-307c-b126-fa7b096807ed | -4.51671 | -54.97727 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac2c83b7-302f-32f3-ba4f-f57901b350f1 | -10.07956 | -46.01143 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 67e988f9-a619-3b99-b04a-b0944e673722 | -2.79315 | -49.58144 | 2026-09-24 05:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c12cfffd-7725-3d24-9987-988c2440c2c5 | -7.6757 | -45.49072 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b14a3e23-6b64-30e5-8a79-5469af0373ce | -6.43202 | -48.46394 | 2026-09-24 05:04:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e083755e-8c8c-366d-b88a-13a47fd1daa0 | -5.81532 | -47.76357 | 2026-09-24 05:04:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7670b00e-101d-3d86-8850-3acfa8823da6 | -3.83416 | -59.39074 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7984df10-165a-3153-b7f0-1904e1629d39 | -6.8792 | -55.56386 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37922710-f65d-3555-84af-dc3a2007bebb | -3.16178 | -57.69076 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84a57aff-0c43-39ed-a686-08d31f75872e | -8.2049 | -54.72808 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba3047b-2184-3357-b085-a90345d4257d | -4.86957 | -55.84655 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce6d8924-3a30-35dc-90b3-b7afa7fc80e1 | -5.77425 | -45.09866 | 2026-09-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 629bade2-ce48-31a7-bc77-124e6fed53d4 | -5.51818 | -50.03122 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 074e82fd-af58-339f-9759-af56f5798556 | -3.80978 | -58.88527 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3684939a-75e5-3136-b419-62a7691d653e | -7.04346 | -62.933 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c736b00c-b4eb-344f-82a0-d9fcddb4cda8 | -6.06364 | -57.81039 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90ad2bbc-fb4b-302f-9dba-ff5ac6129f29 | -6.16143 | -59.94448 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 328f3039-ff0b-3957-a283-5b35d3be069b | -6.57432 | -44.14545 | 2026-09-24 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea7f651-0aba-3f13-9304-e76e7e91fe78 | -6.52835 | -62.93959 | 2026-09-24 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98717c9a-292c-333e-87b3-d8bdeed9c6fe | -5.36919 | -56.05366 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ea898d8-9ee2-33de-b4ba-2569302afa54 | -3.48756 | -59.20019 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dedd9b8-78f0-32d5-8986-64a1bc5b9485 | -3.68504 | -60.58663 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d330cfe-7703-3d81-9c10-b3266fce4ea8 | -5.91728 | -59.92724 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88dd5170-483f-32ff-a233-1aeea03acfa1 | -4.4246 | -55.082 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b3caf22-d367-3488-ae52-24da0e724107 | -4.02296 | -52.07174 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0f3f72c3-2596-32d7-8307-51c3bb686705 | -6.89891 | -57.62878 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f8e077a-a928-3615-8678-b8bddf69d702 | -3.86115 | -58.82488 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7325e86a-38d7-34ec-ba57-71a71e1129cf | -2.88778 | -54.08786 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 397c0bed-1ba4-3aa7-b765-ae304bf3a26a | -4.99984 | -45.55243 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08d84b1d-4f9f-3176-84c1-bc7980b4584d | -3.58256 | -59.07407 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17161473-9a5f-367b-be78-67caca579cb3 | -3.4471 | -60.5761 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cdceca8-2e51-334f-b516-09d80b8d379d | -1.82585 | -55.71358 | 2026-09-24 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25c8b2db-fa5c-30b6-8f84-1d5daffb50f8 | -6.53174 | -55.46102 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c2413c5-c551-3edf-9409-4867def56066 | -5.83851 | -53.86195 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 332fe980-eef5-389b-a7b9-50940795ccc9 | -6.5106 | -55.3637 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a2c1180-d468-3755-a751-57075e79b0b6 | -4.99939 | -45.55542 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94ac0708-b82f-37b1-9edf-969696e62822 | -1.25814 | -54.67941 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04af438f-3b60-3da3-b2a8-1f1a6b7e8e7f | -2.73803 | -49.46209 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac838dcd-1420-344a-9fc3-57f29ba5949e | -3.45164 | -50.0864 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1944d95f-e18a-345b-8aa4-f6471c1ccfc4 | -5.83575 | -53.85797 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a936ac54-3fd9-3b7b-9d2a-0c8fad530d30 | -3.76528 | -60.72662 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da95624-4d00-3028-ba5a-f334ac075cca | -1.82351 | -55.33538 | 2026-09-24 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78cc237e-474d-3be8-adbc-8dc811735c9d | -2.88833 | -54.08442 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77ff55d5-e15b-3e9c-80f0-1c6087694263 | -4.38283 | -55.02847 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90211a5e-5cba-3aa3-b630-8e7f012d9d77 | -6.06946 | -57.79798 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6129d90-619f-3ad5-aa39-6212e6c8ff97 | -6.33422 | -43.36559 | 2026-09-24 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b433e9a5-59c5-3057-878a-b13e3fdcf684 | -7.40134 | -44.77183 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e173fedf-0073-3723-be4f-926a1f7e25eb | -4.68872 | -55.92424 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcba0557-7be7-3194-bc87-794dfc1ca2dc | -3.7131 | -54.19698 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3f222d4-2a11-3367-ada2-630ba9e9aa84 | -3.58717 | -50.03325 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2029da6-7e6d-3466-8c7c-0d2786a4a6a5 | -3.73262 | -59.42638 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60a34fc8-bbf6-306c-91f2-e755d3f7dd03 | -3.5258 | -49.37538 | 2026-09-24 05:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e993cc9a-3cce-3d93-b004-476b17e5d486 | -4.559 | -54.944 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e84319-082d-3f0c-b4e9-defc8ae826df | -3.72434 | -60.57449 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e11ba5ae-db43-31d8-843c-b9fcbdcdb575 | -9.54445 | -45.36772 | 2026-09-24 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 384433b8-0a6e-3196-a6aa-ac03d4fdbc98 | -3.83507 | -59.35965 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fd93a0c-9cda-3f3f-a259-2bf97d3155f3 | -8.29057 | -54.78834 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d15769ac-3f5b-32fc-b2b4-6cd59ae2bcc6 | -4.55295 | -54.8964 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9da7290-1515-3ed2-9101-60460d177ee5 | -3.52011 | -51.63541 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1252d231-4448-38dc-9dc7-c41705c8cd60 | -6.61084 | -59.92826 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1b581ef1-1c9a-3619-8c4d-b5bfede1cad6 | -6.23777 | -60.03186 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8ccaee4-5bb3-359b-9094-b3ca44a2515c | -6.92413 | -62.90895 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e80c173-374a-3a0a-a4c2-fe779e563f4f | -4.99739 | -45.54992 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 375b2bc9-1704-3077-83de-50ebd4c109da | -3.80456 | -58.89169 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59caadd4-bea1-36b0-8208-e44c7f69cc0d | -5.41193 | -60.21709 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c48008bf-0c90-34b0-866b-b6ed0b38e92c | -7.03146 | -44.64844 | 2026-09-24 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a16b376-aede-3f3f-afff-78d1e8a51b8c | -4.02012 | -52.06755 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0746e4f7-af66-30ae-b28e-249b7c55447b | -8.36125 | -57.67977 | 2026-09-24 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df8d0226-6df1-3b66-b5a5-b8f3d86afb83 | -3.68049 | -60.58589 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c29ade43-b72b-3ca6-b682-c0cbe5bde1cd | -6.89422 | -55.57714 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ea4024-d374-3d22-919b-5bcd96721332 | -7.1933 | -47.46972 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f538a3ff-0764-36ce-8f62-6ea978550d08 | -4.25878 | -60.01064 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 886e94a9-d60e-3b58-883f-1c1600ea2e47 | -6.16257 | -57.71039 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83f220a8-f6f8-3aa4-abe6-dc99dcd80c8e | -3.77598 | -60.7188 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d47c51f2-1b34-3933-87d4-a8bf5d3e2c99 | -7.19943 | -47.46027 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f239ee4-b937-3678-9c7b-f60479ca3e57 | -3.83027 | -59.36271 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ec7d243-2ac9-38d6-a283-9e1f364b2698 | -5.85492 | -49.77485 | 2026-09-24 05:04:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11d7573f-fe73-3a43-97dc-214bc8b70455 | -7.19474 | -47.45987 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36765160-9f40-361e-b539-88f84924b909 | -5.91793 | -59.92345 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c121b18-5f2b-33d1-9106-7e2ce9a3a9a8 | -6.20628 | -47.49709 | 2026-09-24 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17e634d2-250b-3111-9515-8ece76a783a8 | -4.53668 | -54.97648 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eb901ca-d8e2-3808-ace1-53e352863117 | -3.17076 | -60.65651 | 2026-09-24 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d755881-8051-3fd1-8369-df9cc219e8a8 | -6.2061 | -47.49599 | 2026-09-24 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdb9692e-0ff3-3032-80cd-c95a7ff5460d | -3.46107 | -50.07422 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e83afd1e-b471-3850-a28c-3fda79a10767 | -6.88116 | -59.8625 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README73.md)
