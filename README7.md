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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 607863a1-d06d-3b0c-bed1-2a7daaf100da | -3.0973 | -53.7491 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc68a51-3e40-376d-8f18-4800a8445460 | -3.036 | -54.146702 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fbb5a3d-58ed-312e-a6a4-fb9071e134ba | -3.9812 | -59.331699 | 2026-10-07 00:47:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6fb252c-3cfd-3a47-8a2f-dc20b8c5fec4 | -3.292 | -54.009998 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387f77c0-a33b-3c8d-a7ac-a90dcb52d46e | -4.1568 | -55.158699 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ddfb20-533c-3117-857a-208737fb1ff1 | -3.0365 | -53.884602 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1af42ef8-a34a-3774-bb78-687224f816e2 | -3.476 | -54.622398 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11bbf346-44ef-3f92-a988-9c19ce742e59 | 0.9393 | -60.412102 | 2026-10-07 00:47:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ac6fa67b-aa92-34c5-b270-a9b5c64689fc | 1.5307 | -55.9608 | 2026-10-07 00:47:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0892acb-9862-36df-aa74-721142306d41 | -3.2053 | -53.858898 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c49d52c-3ea5-3d56-9fd2-ef52f9a3779e | -3.5041 | -51.686901 | 2026-10-07 00:47:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcddbcfb-ec4d-3842-a463-343abf3b6d7d | -2.9953 | -54.1045 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbb98ea0-0f5e-3407-8884-526142fe5629 | -3.2977 | -54.034599 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 666cc2ee-172c-38cf-8ddb-e4c334d00799 | -2.7566 | -54.094501 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c626abe-afdc-3123-9247-a8b11dcc58d0 | -3.5177 | -54.624599 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9eb3bff-2a66-3757-912e-7d838b4dad80 | -3.0137 | -54.139 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4bad3d-0412-31f3-92b3-97878c299c1c | -1.3248 | -56.405102 | 2026-10-07 00:47:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 088887b5-e073-3636-815d-13c0777f7d08 | -3.0598 | -54.205002 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7848f915-3cf6-3e3e-b810-f22bdb6fefb0 | -3.2989 | -53.8638 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f2f747f-7f86-3ec8-aeed-36d5ece32e64 | -3.5406 | -59.480598 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ccdb2f0-8d59-32c7-9332-1bb3a56ebf4d | -3.5951 | -54.559502 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b1f4d7-a939-3798-9982-406632770539 | -3.5254 | -54.657902 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf6b42d-c462-35aa-a23a-e402137e2333 | -3.0893 | -57.6339 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aae98c2b-3221-3f2e-9a50-cd7f11540922 | -3.6808 | -55.948299 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 898916f5-0b13-3c57-9853-ede0338ba1ed | -3.4593 | -50.087898 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31540431-8ada-30cb-85cc-4dcc7369ecd4 | -3.5326 | -54.644501 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 056b17f8-de11-36ab-a34f-fc5c1376e8ac | -3.5119 | -59.945999 | 2026-10-07 00:47:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70f38944-dc45-37f1-9c19-bb256ab42b84 | -3.3495 | -59.501701 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8d22eb2-279b-3780-b06c-3ed184962580 | -11.0939 | -45.724602 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e858788-3fa6-31a5-b3ee-843e247aa4e0 | 0.4465 | -60.539501 | 2026-10-07 00:47:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 696befa0-8074-3239-9176-93d3ee68d5fc | -3.2788 | -59.553501 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f551c837-3f36-3e95-9410-52c36077c954 | 0.7906 | -59.199501 | 2026-10-07 00:47:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 982a93f2-e73e-3cd6-bb04-57b5f52af157 | -4.9894 | -56.036098 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1b7b9e9-aec9-3736-a346-3f7ed0cb92df | -3.5348 | -59.409901 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d40a8199-0496-39fe-8b35-0a0a27f0e68f | -2.9925 | -54.092201 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54cc3799-917a-39c4-b83a-9530bf2caa2d | -10.8445 | -50.666599 | 2026-10-07 00:47:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45305ef2-9c00-36fc-9555-0ecd23184f1f | -3.1874 | -50.573299 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e96d617c-fff4-3462-aead-60fa17769dad | -3.7404 | -59.407101 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd234659-5236-33a9-80f8-3c33630eca17 | -9.1521 | -65.923798 | 2026-10-07 00:47:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9e27a43-33af-3109-ba59-490a80c3faff | 3.2186 | -61.047001 | 2026-10-07 00:47:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a388a409-2571-39a5-a6e4-71e7c62a882c | 2.0151 | -61.080399 | 2026-10-07 00:47:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 59132cd1-0ca3-302e-868a-b8778de5b912 | -7.1877 | -55.115501 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acb7a3d8-1b9d-3a43-8c94-233e210c20e5 | -3.1728 | -58.6329 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2380ef4-ab63-3186-be51-280feccab625 | -3.2725 | -54.0145 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aafc525-86af-3787-ba3f-9bce87dc6f64 | -2.9855 | -54.1068 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e86b5b-2bc7-3cf3-a30a-049f45f16fa8 | -2.9878 | -54.028198 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 980fc638-c954-34a1-a5b9-3e2d8990bcc1 | -3.3727 | -57.521198 | 2026-10-07 00:47:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b46adc47-590e-303b-89b8-bfb12e9f0add | -3.0418 | -54.2598 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f0decdb-965d-33ac-8646-27eec9cfe432 | 4.1544 | -61.240299 | 2026-10-07 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bc100541-0b20-32e1-bfea-8db8309a5db7 | -3.0513 | -53.947701 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 345f11a7-a448-38d6-bb4d-906b467e90b4 | 2.012 | -61.094002 | 2026-10-07 00:47:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1667796e-6807-391a-bf99-1ef9d1ff4e71 | -3.8948 | -59.314999 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c37761a5-cfb2-3e55-9343-41fd29500c48 | -3.6169 | -55.2724 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 004eb65e-13cc-3455-86f4-bdcc1d19b0a7 | -3.3433 | -59.474201 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e57b135c-a627-3acd-bd73-64a130af4927 | -2.7728 | -51.6698 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2034f62f-006c-3a41-9954-d9d47bb2b4ee | -3.0933 | -54.171799 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78251c82-f0a9-3a44-a4ed-d2036c8c7724 | -2.2186 | -58.109798 | 2026-10-07 00:47:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68b4dea5-e8cf-3de1-9737-3ff409e759ad | -3.8866 | -59.324001 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 732ce249-1c0a-3904-bc13-9197df732cb5 | -2.7825 | -51.6675 | 2026-10-07 00:47:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21a49def-c4be-3c3a-8380-3e677bc33ca5 | -3.5079 | -54.6269 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b474c6c-fdfe-3078-a597-2c52324730ba | -2.7733 | -54.077599 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee07df62-dd9b-3e52-b645-dab3f7780198 | -2.923 | -54.146999 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32fd9ea2-cffe-3b84-9bbe-00e85d2a30d5 | -2.9356 | -54.157001 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc115413-de7d-3354-ba5c-7fcd9e114134 | -4.0822 | -54.882401 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30cc6350-5619-37b2-bf62-a6b2f6253633 | -3.0822 | -54.300701 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 543ef782-647c-3a16-af7f-51855e08910b | -2.8754 | -54.119202 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 570ee974-e9a5-3c07-893f-36f5a551e8a3 | -2.8444 | -54.074299 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e67bf99b-e65b-3564-8766-6d95ac4a7d11 | -3.0511 | -57.511902 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1a2304-9e9c-3e4b-a2ac-3d3174d0b362 | -3.017 | -53.889099 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd3a640-a304-38af-bfdf-fd81c5a82e88 | -3.6786 | -55.939098 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1174f19e-c55d-3015-b55a-41c3cb1506f6 | -4.0615 | -59.823601 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44ff76b3-865e-3664-8d18-bd63580efd2a | -3.02 | -53.901798 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33362527-364a-3558-9381-0cff721b14f3 | -3.2243 | -54.292999 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a440b08b-8b63-3fc9-ad00-7b76b495917c | -3.2937 | -54.061401 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff29e5be-c180-320c-a57b-d17d3d2a7d8f | -3.1132 | -53.772598 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f5a4178-930c-3c1b-a0c5-b4b4daa869c7 | -3.5352 | -54.655602 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0c0b66-9652-36e7-aafa-b850c16eec92 | -1.8056 | -57.112499 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c25303b6-1b67-3f91-8247-32a27c2e8c7e | -3.6775 | -59.629799 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f897d0b-a6ad-3e87-b8e0-c10898c41bc1 | -4.1286 | -54.9049 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcf22f8-0561-3a13-997b-887e46a59961 | -3.2908 | -54.049198 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73149dad-97a9-3e65-8da1-a4086a2e64e7 | -3.4444 | -56.934399 | 2026-10-07 00:47:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc320def-7884-3a26-a140-32f3ccced5af | -5.9525 | -55.345798 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7dace09-ebc9-34ec-a8d2-03c895cfe577 | -3.0943 | -53.736198 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72bf261a-5f76-38ef-a906-c5ab3ebadf5f | -2.4787 | -56.0951 | 2026-10-07 00:47:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 710e4d01-a11a-3b39-8778-d6602da495f0 | -3.092 | -54.2985 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b18f3fb-fb86-3539-8899-40d268375d64 | -3.0463 | -53.882301 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de309acf-29c7-36e8-94a7-f39644432b66 | -3.4635 | -50.062698 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 104032c4-5aad-356a-8659-ed7205a4d4b3 | -9.4748 | -64.334396 | 2026-10-07 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67ccb1c8-986b-3287-815b-7dcebeaddbf1 | -3.5649 | -59.496799 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef189146-3313-33ac-9072-9f41b99cc75f | -3.0973 | -54.145302 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b86e809-44bd-3a7b-961a-223a202c4f48 | -2.9982 | -54.116699 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2543748-7000-34b8-807e-112bffdbe816 | -4.5705 | -54.944901 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab0bfde-3f4f-34a0-af53-e7843a3613fc | -3.4538 | -50.064999 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e8e7af-d905-33b6-ab13-1255ef9ee263 | -3.5618 | -59.483101 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d569ad4c-f537-3080-b8ef-fa71faeb53c9 | -2.857 | -59.103401 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89b37b18-46b1-3a3a-8b23-ff0bedc814f3 | -3.4889 | -59.571301 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60445de1-bd1c-3efc-b08e-845a6a5569b6 | -2.4851 | -58.057899 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecf5c58-afde-3284-beec-7ea5fa06b885 | -4.0631 | -59.830399 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3220ee19-0938-3599-8507-dcac585d646a | -3.071 | -54.252998 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e8879f-3626-38c5-a7cf-abccbaa13c52 | -3.0892 | -54.286598 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
