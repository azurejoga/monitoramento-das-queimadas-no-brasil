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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b45a5eb-48de-3b48-b855-9fd02cf2ede9 | -3.62687 | -54.66938 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d81779e-0929-31b9-8842-d6b1b91586d1 | -3.62225 | -54.67231 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9412fae8-653f-3d1c-b55e-04d0a35268c2 | -3.60941 | -54.72951 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48c482d2-b459-367e-bda4-3f44651cca2d | -4.04048 | -54.77262 | 2024-10-16 05:23:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89ce1991-1959-3b6a-91bb-2810c3b4e9ec | -3.71973 | -54.19992 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 668f8023-bec3-3e47-bc81-8acb3b8a1662 | -3.6228 | -54.6687 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e42a24c2-e284-34c1-957f-eeb5508e44bc | -4.11135 | -54.15826 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173af1b6-32d7-35e2-9b5b-c708fc7dff79 | -4.06692 | -54.02524 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e37f383e-ecd5-3474-8fb8-1c38e7219d72 | -3.82776 | -54.2303 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35dc1967-ed5b-3442-98cd-e2d61554c4f7 | -3.79881 | -54.04884 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f95bf5-0397-3a0d-84c1-b2fc3632a5c8 | -3.71913 | -54.20389 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 603b04cf-0bdc-3ffc-8db2-a888e9128491 | -2.04255 | -56.37665 | 2024-10-16 05:23:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4288b095-48f2-3572-9764-64648121ad22 | -1.62206 | -55.89923 | 2024-10-16 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c526e329-00bb-3778-a0c5-7d4cf96fb0fb | -1.62109 | -55.90156 | 2024-10-16 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72fd681a-3abe-3935-840e-5925b890724c | -1.2646 | -55.90652 | 2024-10-16 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6624c893-f240-3b97-940e-507f4673b767 | -1.26093 | -55.90596 | 2024-10-16 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd48316c-bb42-37c4-a0ae-b6b921322dc6 | -1.73354 | -55.19234 | 2024-10-16 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a1e6085-6a6d-30f3-9956-6365e8bbe518 | -2.25975 | -56.2574 | 2024-10-16 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b4475e5-bce0-300c-95f3-fc355c6cd984 | -3.64693 | -55.49223 | 2024-10-16 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faf542ae-c213-3063-bc1b-0f9531e029cf | -3.48737 | -55.45352 | 2024-10-16 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6efb4b6-458b-396b-95b5-f18296a03b31 | -2.22839 | -56.88372 | 2024-10-16 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f524c302-b4d4-3f22-841e-50aa7d652111 | -2.20019 | -56.71611 | 2024-10-16 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d523e71-0845-344e-a49b-48db492cdafe | -2.0566 | -56.63869 | 2024-10-16 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0599bfab-cbc6-3956-b367-51e19f641b07 | -2.05597 | -56.64268 | 2024-10-16 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 427be31b-ba01-389b-82f3-d74d366fec7a | -2.05569 | -56.64178 | 2024-10-16 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a737ad19-24d0-3068-96f0-90a9b44b66ad | -2.05304 | -56.63819 | 2024-10-16 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e357ea23-26aa-3251-b494-17b40fe458ac | -2.05241 | -56.64217 | 2024-10-16 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72ad753c-7e95-3cbb-bf89-dcda5cdc3d86 | -2.05213 | -56.64127 | 2024-10-16 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 217c8f77-66b6-31f3-8e0d-15fef3820ef2 | -3.22359 | -58.01657 | 2024-10-16 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3dbe4fa-8024-3253-823f-8d62d426996b | -2.47411 | -57.9807 | 2024-10-16 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc634e6-53da-300c-a527-8c699a857175 | -2.31417 | -57.15502 | 2024-10-16 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7765249a-d92d-3108-a344-aa31f2e75f16 | -2.31068 | -57.15448 | 2024-10-16 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f640a14-4190-3435-b810-16bdfe14ff70 | -7.17747 | -59.88778 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37cec4e1-acff-3120-8af4-e641a6e80fea | -6.6852 | -59.48739 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0be20fd-c0bc-3a9b-b60d-5aabe826095e | -7.4609 | -60.40695 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c674a8e-303c-3f7c-bec7-53f3fc7d0a09 | -6.91251 | -59.75358 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e520ac37-987a-399c-8919-1d96bf5a7bf1 | -6.90918 | -59.75308 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d15e8eb-2a9a-361b-9827-69e47aa4454d | -6.90864 | -59.7566 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1b25a59c-b244-3b10-ba4e-6f994bd418ca | -6.78714 | -59.35408 | 2024-10-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43a3f4e8-3152-3f42-83bc-da7a91b0669f | 0.95533 | -60.143 | 2024-10-16 05:23:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55bda48a-8e57-3057-8fae-554f465c3a70 | 0.61441 | -59.76977 | 2024-10-16 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed25aa12-fede-32ab-8d95-51986a2bc6e8 | -1.41598 | -60.40865 | 2024-10-16 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6cd32c1-0afd-39c4-a382-fcedc7a29356 | -1.41543 | -60.41214 | 2024-10-16 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13fe6dbf-bde9-31c2-932a-151c9157716d | -7.93354 | -61.55478 | 2024-10-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e65b086-b9a7-3354-9553-126a4ae299a5 | -7.91913 | -61.55909 | 2024-10-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847199fd-b4da-30bf-aa15-a8312402937f | -8.98755 | -61.43192 | 2024-10-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c15b70ad-ddde-37b5-9c7b-8402f3b5b700 | -8.9848 | -61.42793 | 2024-10-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f42ac045-cc05-38db-affb-319d3fb6d93d | -8.98425 | -61.4314 | 2024-10-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fd7b21f-d11d-3397-859d-8e30001419ab | -8.68921 | -61.33752 | 2024-10-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40c9fdff-6a13-3127-b144-923c41d5c184 | -8.34104 | -61.49527 | 2024-10-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38c664ba-f8bd-357f-b7da-f8e29192a4d0 | -8.3449 | -61.4923 | 2024-10-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5af50ab-1ac7-322a-8371-246226004d22 | 1.11203 | -60.51447 | 2024-10-16 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 110cfff9-69f7-385d-91ec-384bd83f0347 | 1.94283 | -60.86451 | 2024-10-16 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa9a76b-4459-3e76-b21c-5c1e96f2c13e | 1.94224 | -60.86075 | 2024-10-16 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d3a24f7-58ce-34a3-af54-e0cc41ddf504 | -0.56389 | -60.9803 | 2024-10-16 05:23:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f82e37f3-d67f-35d4-a842-f115dbf2cc1d | -8.93107 | -64.31715 | 2024-10-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd347c51-c6fc-3c08-b5c9-69cb46bdc3f2 | -8.93468 | -64.31775 | 2024-10-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f97557e-a5e1-38d2-9f85-c718a9db2764 | -8.92426 | -64.24739 | 2024-10-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0270fd6d-2364-3f6f-abcd-d8d33642fb6e | -7.4092 | -72.61361 | 2024-10-16 05:23:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2b6851-8663-3751-850a-c3f4abba5cfc | -7.40196 | -72.6176 | 2024-10-16 05:23:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa8cbb83-0151-326d-9f53-1dc33c4abc8b | 1.0016 | -52.2164 | 2024-10-16 05:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 2ced8428-94dc-32cd-9407-26523debe5d6 | -9.19386 | -67.20623 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c34c7ff-b264-3b17-a354-ea0c4e93854b | -9.19314 | -67.21033 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa00d361-a6bd-303d-b647-b15f86caabf8 | -9.18959 | -67.20545 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a21d464-4fa7-336c-a372-44f8de49268f | -9.18887 | -67.20954 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7c56fbd-51c9-3779-9e6d-51b38df7ac98 | -10.41758 | -67.56998 | 2024-10-16 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41323f79-bb65-3906-a861-e1f822974b35 | -10.11582 | -67.23596 | 2024-10-16 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9fb82bf-5695-343c-860f-5699c57d4246 | -10.11159 | -67.23524 | 2024-10-16 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dbb2c67-699c-38b4-a842-32a0fff8e461 | -10.10067 | -67.34862 | 2024-10-16 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3c6db04-9a6e-3cb9-8643-59123386bb2a | -10.09642 | -67.34782 | 2024-10-16 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9b0160c-5a66-3b15-a7e6-41f527335ad3 | -10.09613 | -67.22421 | 2024-10-16 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1a73948-ced0-3e92-99f1-4616cde09da4 | -9.99981 | -66.90825 | 2024-10-16 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0c1dfc-a424-3859-86f0-b31721034e95 | -9.9929 | -66.85991 | 2024-10-16 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc45c352-e887-3f47-8887-b7b36018d129 | -9.99197 | -66.85638 | 2024-10-16 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b59b99-d3eb-3585-b103-d8a4695c2355 | -9.9913 | -66.86015 | 2024-10-16 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ba57fe-da58-362d-a041-0172100031c4 | -9.87438 | -67.19807 | 2024-10-16 05:25:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a5dbd79-7fb8-3827-9a22-b2c07690d3bb | -9.75627 | -67.32709 | 2024-10-16 05:25:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f80cbb3-1b2a-3ffe-a131-c130ddc5daf0 | -9.70265 | -67.05935 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cb8ac51-94ca-321a-a292-3418396c96f7 | -9.59077 | -66.78197 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cd6e0df-4daf-34b2-a191-9cf2ee356e1f | -9.5594 | -66.45741 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6d5f1c7-1bcf-309b-b49f-b25a9adc1d73 | -9.47625 | -66.55173 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcdb4e1d-ce50-3c33-93f3-ff3861f6caaf | -9.46217 | -67.06652 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae6f6c9-2486-37f6-bc3b-7bba1cda8f0d | -9.45795 | -67.06578 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89bc4a0b-bd17-3f5c-8d3b-e606222c04ae | -9.45254 | -67.14684 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 955d1647-73ae-335a-8a3b-8a49401be6bf | -9.45235 | -67.07296 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0c0334-eb76-3647-af13-93a10c5fdbb0 | -9.45183 | -67.15087 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 507b4633-248f-3683-9ffb-f6d7ef388cce | -9.44829 | -67.14612 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1fb5e30-1468-339d-b0be-a97243ddca62 | -9.44759 | -67.15016 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9178550-c021-310e-872e-8793ee1ea3f3 | -9.44391 | -67.07148 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92a8f31c-e980-372b-a551-e31252840d70 | -9.44039 | -67.0668 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 374ef146-0511-36b5-b0f2-0a5d464dcc3a | -9.4397 | -67.07075 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff33200f-f77d-3920-8d5e-467e9cae1945 | -10.00047 | -66.90448 | 2024-10-16 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a21e88-4fb9-3da6-a957-a15fc5b4c8a1 | -9.40236 | -67.84524 | 2024-10-16 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d67ffb2-5257-3473-9d7d-94853fbac53b | -9.39626 | -67.75499 | 2024-10-16 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef2c5778-edfa-3807-a11f-bf2ca61223ac | -8.79324 | -67.62749 | 2024-10-16 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0beb96a1-3746-3a61-b67f-ed0595009370 | -8.78881 | -67.62672 | 2024-10-16 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57081160-cdaf-30ee-a59d-0dc4199e6a59 | -10.87053 | -68.2271 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c64a91fd-a84f-3f25-b703-df2f066735c4 | -10.8312 | -68.27619 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893dfe99-3d6e-3450-965b-ca5500330100 | -10.82957 | -68.27509 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea1deca8-f227-3f5c-b686-13f6f567dc61 | -10.82875 | -68.27959 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README60.md)
