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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d75085b-78ed-327e-b5b6-afe4413ca2d6 | -16.43583 | -57.31365 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| de653e01-549e-3dc5-b6ec-cd181e4a29bb | -16.43545 | -57.26162 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a2a2149b-ea68-3e5d-8efe-079a446787a7 | -16.4348 | -57.26622 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| de48ca75-d84c-37bd-a325-4a4b6a57e1a9 | -16.43416 | -57.27084 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b35fe212-a31c-3a57-bed3-e8a4d76eba06 | -16.43352 | -57.27547 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e2d0c365-6ffe-3b84-9ae5-f026d7ca0152 | -16.4317 | -57.26104 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a7efc660-d102-3939-bd0e-25c79e61e869 | -16.43105 | -57.26566 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0d5d4ba1-9276-3560-b7a2-e585703f7ba9 | -16.43079 | -57.32236 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eb24cb56-888b-30c4-bb87-6512bc9a1f33 | -16.43041 | -57.27028 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 351e0aff-3660-3d7d-9093-d1464c7e1c34 | -16.42847 | -57.28418 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 41b65807-ebea-37f5-93da-cbced202dd11 | -16.42783 | -57.28881 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c610bc36-997e-3b9a-a7f7-4704f0abff80 | -16.4273 | -57.26509 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3228fdfe-ec9a-3ea4-98c3-e45485647961 | -16.42705 | -57.3218 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ff5fad4f-748c-3817-b9ea-0a7a4121d936 | -16.4264 | -57.32644 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6262953b-43c5-391e-acc7-5f9f33b062f9 | -16.4233 | -57.32124 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f63c8bbb-d629-3f20-8306-d72c6bb96b1e | -16.42266 | -57.32587 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6b2cabc1-46a9-320e-a320-c6e78135c70b | -16.42137 | -57.33509 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 116ef2f8-46ba-3e38-b510-368a9460b884 | -16.42073 | -57.3397 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f8226c4b-3ed7-326a-b144-3fdd3470b998 | -16.42033 | -57.28771 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d22e234e-da5c-3750-98f6-01bfedc2c623 | -16.41968 | -57.29234 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 51ccce70-4ac9-3b9c-9ed6-4a8d88a485a8 | -16.41956 | -57.32069 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1232a1df-44e3-3aca-b42b-c1faeae3d4e7 | -16.41904 | -57.29697 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b36d37f4-bd27-3d9b-ae46-6d423e18a24b | -16.41722 | -57.28252 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a43a95dc-dee7-3488-a59f-fbf16a3f40f7 | -16.4171 | -57.31092 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ca7ed091-0f63-3dfa-b9be-28c9ac05d5a4 | -16.41658 | -57.28715 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a8cf9cdc-4352-33e8-a441-f6694dc16327 | -16.41582 | -57.32014 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1632fffc-7f23-320a-bb22-80bc83a85377 | -16.41529 | -57.29645 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| edf4a293-ac01-3b84-87c0-29fee63d50f6 | -16.41464 | -57.30111 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 69112824-5d00-3290-a813-bf372e497293 | -16.41399 | -57.30577 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9ba28784-5362-3247-ac24-aeb05395ded4 | -16.41335 | -57.31039 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 56dfb701-2f11-303f-bd2b-65bcbaf067de | -16.41271 | -57.31499 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eaaf231e-a7b2-362a-b6eb-1821b58af2f1 | -16.41218 | -57.29125 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 34f03c46-953d-3a59-b31b-8eb4484975ad | -16.41089 | -57.30058 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7abfdad6-813f-31e1-9a6d-1e78dfad7763 | -16.41025 | -57.30523 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 55ff59c4-4973-3ae5-830d-63e1cac89914 | -16.40961 | -57.30984 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 45838756-eff7-31d5-b2e7-97590bafa49e | -16.40951 | -57.33804 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| ce7ae137-7a39-305f-a210-9074b4231730 | -16.40887 | -57.34266 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9d30d1b1-5a61-3a2d-9736-098534146627 | -16.4065 | -57.30466 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 681c0c08-60a1-319d-9442-d60da57c9fbd | -16.64111 | -57.16265 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 78afbcd6-eea8-39c3-a3b1-37f82b739090 | -16.63862 | -57.15259 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aa93b833-3e76-39ee-9177-5e61a0d06c71 | -16.63797 | -57.15734 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6598d607-3d7a-3c21-aee0-961320aa53c2 | -16.63732 | -57.16208 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 30d6fa6c-1586-3ff8-b49d-a97eee163912 | -16.63483 | -57.15203 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 71251821-04fb-3d08-b513-ae977b471033 | -16.63418 | -57.15678 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a93525e9-470b-3c87-af11-6d0df9002b78 | -16.63299 | -57.13722 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 2a6536c7-6a61-3b86-b9ab-3e83feeadb25 | -16.63234 | -57.14197 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 9e331dc7-83bb-3d26-a431-758e97c6cb83 | -16.63169 | -57.14672 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| a32c1d1c-a2b5-307a-9d9c-899418e1fc10 | -16.63104 | -57.15147 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7ea62199-be28-3ddd-a7e7-421617c79814 | -16.6304 | -57.15621 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7176d005-fb1c-3923-9710-126d695cf2f4 | -16.62984 | -57.13189 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| bd01a071-2d3c-307a-872c-72aba4d70116 | -16.6292 | -57.13665 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 3a712be4-d2fd-3fd0-80c0-46c005286dc6 | -16.62855 | -57.14141 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| aeb8ed23-d01a-3c88-8b4e-f7198388ad6a | -16.6279 | -57.14616 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 60758bef-aefd-325d-ba4f-51ca9f9fe645 | -16.62725 | -57.15091 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5d5a451a-ab97-3f4f-a17e-04249fdc9807 | -16.62541 | -57.13609 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b3353f27-8f02-3ebf-87ff-76e2b5f63c9e | -16.62476 | -57.14084 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1f406da4-2d39-3d98-b1fc-52655a8ef5ab | -16.62411 | -57.14559 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e9047c2-b674-37ac-93a6-c82db859fe77 | -16.62347 | -57.15034 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ff9c47cd-db36-36a1-b23c-4ad7b8ac14e2 | -16.62097 | -57.14028 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 80344380-18a6-3939-99f8-5b38c4c8c396 | -16.62033 | -57.14502 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d40da187-82ff-39b9-b00d-854cb263f112 | -16.61968 | -57.14977 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5b7be788-95c9-317b-a554-c22ba4c872c7 | -16.61718 | -57.13971 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| d49750a5-ae49-33e7-844a-fab105bd8091 | -16.61654 | -57.14446 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| ee115629-fc2b-3c5c-aacf-9dbbf8c61851 | -16.61589 | -57.14921 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| c3a4fef4-d36e-3976-bca5-c785398985be | -16.61339 | -57.13915 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 7780898a-48ec-3af8-8391-847f1efdef54 | -16.61275 | -57.1439 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 3528fde2-db31-3cd2-bc95-f4baea71917b | -16.61211 | -57.14865 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| a960f55a-2798-309e-8bfa-188ac937de14 | -16.61146 | -57.15339 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 662eae6c-456b-351a-8964-1aa8457d0594 | -16.60896 | -57.14334 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 0c4082af-d404-3e39-a754-73663091b075 | -16.60832 | -57.14808 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| bef5670e-baa4-3fe7-9113-08415cd0dc8e | -16.58875 | -57.15002 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7c51d003-1343-3bee-b649-fcccad32ba3c | -16.58628 | -57.14694 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 144aa130-bea9-31b7-9553-4d87011baf14 | -16.58561 | -57.15171 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 8cec0074-bffb-38da-b0d7-8a24ada2090b | -16.58495 | -57.15645 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2006d958-a7b1-3b2f-ad92-b8cf1b307c5f | -16.58249 | -57.14639 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 28a3abb0-9f59-329f-b7b9-5cd8e438b6ae | -16.58182 | -57.15118 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 6e24fb46-9240-3660-9b62-91479d26ab0c | -16.58116 | -57.15594 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 06384d7a-5e8c-3be1-a708-ac15c5419eef | -16.57871 | -57.14583 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2db21cf6-c618-3f08-9c66-f2a994eb5265 | -16.57804 | -57.15064 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3a1026e2-f7f8-3d60-b02d-03671c2063f4 | -16.57737 | -57.15541 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| da03e56a-c619-3808-ad03-f613137eceae | -16.57492 | -57.14527 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 02ebe4ab-13bc-3322-995b-c1bba9266da2 | -16.57425 | -57.15008 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e41743b6-fed0-3878-a84e-202f69366ce9 | -16.57358 | -57.15487 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 467d5440-a513-3a94-aa1d-3ec2e12ca8ca | -16.57096 | -57.17365 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 09362b5d-508a-3c7d-9b05-4c8f286cc160 | -16.57047 | -57.14951 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9445a752-802c-34bf-ac15-6bbf5971bdd1 | -16.5698 | -57.1543 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 468394dd-4c6c-39ae-9190-4f7840bb8824 | -16.58455 | -57.21413 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0329e4a8-5e83-37aa-89c7-839b8b840d6b | -16.58389 | -57.21883 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d2c98abd-819f-3bf2-8f08-2f23b0641e7c | -16.58364 | -57.21674 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| e110cea5-9024-305a-b610-69daa56a6a54 | -16.583 | -57.22144 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 23a4ce12-0a93-3812-8d96-12aebfb4c827 | -16.58012 | -57.21827 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 533eecc8-353e-37e7-ae02-309a338a0ee0 | -16.56635 | -57.20663 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e1525c9e-2e0f-393e-8a26-d4cba7f345fd | -16.56324 | -57.20137 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ebe7085e-816b-3619-9ce6-2c8588fe7198 | -16.5629 | -57.25877 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| eccfa37e-e1f1-34f9-827a-f60dd168e648 | -16.56258 | -57.20607 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 918f4589-f000-3360-bd18-096e487cefc1 | -16.54098 | -57.25074 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c6ee92f2-8c12-3e6a-a882-a6b8170fd73f | -16.53786 | -57.24554 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 916b3262-a6f3-3926-b121-710a9fc5c4a1 | -16.53721 | -57.2502 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 45f9f07a-ad15-3d28-a2cf-a9343a89cd3f | -16.53657 | -57.25486 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fb5e5bae-88f6-32bc-8c0a-fe0777ff056c | -16.52969 | -57.2491 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README118.md)
