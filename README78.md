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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d2c5fb0-91d6-3b17-8835-7cb9e986d641 | -2.81157 | -49.47833 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 394c590f-1d24-34b6-9219-eae90df20faf | -2.80505 | -49.06791 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ee81277-41c9-3f56-8b5c-47a5061ec8bf | -2.76453 | -49.39603 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87c234b0-b67e-31a0-afdb-b11b29f56cc9 | -2.73882 | -49.37715 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf3c6210-c75f-37b3-ba8b-4dc53fefce97 | -2.73416 | -49.37645 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c5c5911-a580-3680-a38e-ad3ad0dfcb28 | -2.73342 | -49.38138 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76bb065e-8f36-3053-a5f5-d8b30e7124b8 | -2.72876 | -49.38068 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d9fa321-7c5e-30c6-8fc7-39a65933ad70 | -2.72802 | -49.38559 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92984a8f-e4e6-3509-be9d-13332bd6dd3e | -2.72484 | -49.37509 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34397af1-0587-3116-af5f-a717146d72e5 | -2.72264 | -49.38972 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b895337-c2a2-3b16-b233-d4f08ac2e933 | -2.71799 | -49.38902 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 166244e5-d9ab-3437-8ff3-6955a53a3d6d | -2.71224 | -49.42736 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e71970f-dc43-34a7-9093-a5020a44430a | -2.71151 | -49.43218 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fee46abc-fde6-3dc9-bbf3-498d37afc9af | -2.70373 | -49.29232 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4561e74f-5fb6-3c64-b024-a781eb9cf53a | -2.70301 | -49.29721 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae96b6c0-3ddb-3840-ac93-54538d685510 | -2.70102 | -49.2952 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd47d864-35c4-350b-8cc6-485c7d40849e | -2.69905 | -49.29159 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 615f09dc-9889-3ab2-864a-2a1c08b1a044 | -2.69834 | -49.29642 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5173e7fe-6336-3b5a-9533-93f3b9141e98 | -2.69345 | -49.34381 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8778d7e1-3e93-31cf-9282-81e940b12f2f | -2.69271 | -49.34861 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5737d09-3469-305f-a4d8-bdbd579676ff | -2.68188 | -49.408 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c074f22-5f63-33b7-a9ac-0c06cd08ea67 | -2.68015 | -49.45181 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9cedeb1-b797-36c2-a0c4-d65dd33e2eef | -2.67885 | -49.49834 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75bec827-fa31-3c37-8358-2c8ed4e462ca | -2.67773 | -49.50008 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d96b01d9-d663-3159-b8f6-ac3fbc1e55ff | -2.67701 | -49.44946 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d015a5f2-6bfb-3af9-be69-01284d0c27c4 | -2.67627 | -49.45424 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 694efa94-6f4c-3ede-9eb1-7ea195a71f4f | -2.67623 | -49.44631 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3dd20b7-543a-30dd-abd0-50bea733df5d | -2.67552 | -49.4511 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed69552-82e2-32d1-917f-92821c7924a7 | -2.67481 | -49.45588 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13dd7bdc-bcb3-3787-88e0-aacb8fcb31ab | -2.67238 | -49.44878 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4b5ab67-4778-3ec6-ae39-c86821d8ba0d | -2.67089 | -49.45041 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2e4c120e-c8ea-3df5-a872-1c83d402ff9b | -2.65139 | -49.1153 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cc727853-37a0-3622-aed1-efebaf18d3e2 | -2.59476 | -49.39786 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e4561c7e-8270-3517-a372-de799d59784b | -3.95364 | -50.73135 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38c271d1-1f6e-3399-91cc-238b8fc64a4e | -3.92521 | -50.7146 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8372163-effd-396e-8b7e-f47fcd14fc5d | -3.8227 | -49.23769 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 622bb2c9-653d-3cbd-aa04-a52cd743eb08 | -4.42517 | -49.44798 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 116de603-96e1-3bff-a639-e3d96c85bef1 | -4.22762 | -49.72279 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dc30a36-6b13-343c-875e-c74faef0d7bd | -4.19312 | -50.59982 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa8f047f-e601-3d10-964d-438389944c3f | -4.18874 | -50.59919 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd50a0f0-28a5-3a61-a57e-e00fd8e054fb | -4.0544 | -50.60128 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5697beb9-337d-3ca2-9e83-33b3e09bf252 | -4.42444 | -49.45298 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65e9f12b-34b3-3d4f-ad90-e58a143c04a3 | -4.22297 | -49.72208 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d922364e-4a82-34bf-8a32-358a30882967 | -4.18436 | -50.59858 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0fecd0c-5dc8-3e96-bc74-7e11c7f23b95 | -4.05503 | -50.59708 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2632727-92f6-3c14-88e5-18ccb8ea44e4 | -3.97468 | -50.70938 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 595cd4ff-ce18-3e97-816f-fe49d9098bba | -3.9586 | -50.72783 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13b58ca1-6c9b-3120-9fbe-41fb38922d27 | -3.9549 | -50.72306 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47286301-2705-394b-b964-690264417e23 | -3.95427 | -50.72721 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1afea37f-04c9-358c-b776-eb78e20450a4 | -3.9246 | -50.71872 | 2024-11-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45ff35d0-81d9-3ef5-8788-af1faae53165 | -3.82193 | -49.24284 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a52a97b-2b15-3ab3-b531-52f41e75dfac | -3.75468 | -49.33664 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24cfb8d4-a14c-3234-877f-e5cab80b1e9b | -3.75408 | -49.33501 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26b46f06-3aca-35b7-945f-4cbc9890ca6f | 2.37305 | -50.82632 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b82a510a-8aa9-3280-af30-50794d0684e4 | 2.36914 | -50.82694 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b03c7a8c-dd86-3ea6-aae3-87bedf207ccd | 2.01594 | -50.47915 | 2024-11-03 05:08:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5232e786-f9e0-395c-b1bf-604b6281c223 | 2.01537 | -50.47569 | 2024-11-03 05:08:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5149256d-79c0-3c9f-b39c-f02a009314fd | 1.96 | -50.39471 | 2024-11-03 05:08:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6c6b565-0b59-325a-93d2-c1e4a8806ba1 | 1.95597 | -50.39536 | 2024-11-03 05:08:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f048d02-df7d-3b54-9dbd-c8c94bec07ca | 1.05831 | -50.62327 | 2024-11-03 05:08:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eea6581-f8e2-3eac-8535-9f5f72fde558 | 1.05812 | -50.62297 | 2024-11-03 05:08:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdc83cc8-a94c-3f22-90bc-32fa7ca214e0 | 1.0372 | -50.72619 | 2024-11-03 05:08:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a3d424-54f1-3262-856d-08826b4e3071 | 1.03375 | -50.7303 | 2024-11-03 05:08:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5193c9f-5205-3d19-8fca-caf539f814e8 | 0.62322 | -50.23534 | 2024-11-03 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9cdc47e-a361-37c7-9da6-6589267b095e | 0.02179 | -51.2617 | 2024-11-03 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab0edb9b-0076-31ca-a282-f025da3c5470 | 0.01472 | -51.34391 | 2024-11-03 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daf8e808-7aa4-32b0-904a-45376f606693 | 0.0108 | -51.34451 | 2024-11-03 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75f9f5eb-b766-30a6-9953-c3d9b834b910 | -2.2509 | -50.46136 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6873058-1a9e-36a9-ab81-147a9e19f560 | -2.24661 | -50.46071 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f7c890-56d9-378f-98f5-27565d438625 | -2.15013 | -50.44646 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93c5edce-ba32-3469-ae8f-9281ecaa822e | -2.08991 | -50.39328 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a87013f6-0ac3-3689-b172-bb192c0a0f25 | -2.08928 | -50.3973 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 086e9f0e-3db7-3fcd-b699-c4aa04b4ca01 | -2.0874 | -50.40935 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e419fd-3e9a-3274-93e4-2b6aae8ea2fa | -2.08562 | -50.39261 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40fad30d-b82f-3c41-b13e-9007f5bd5b83 | -2.08499 | -50.39664 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e09a48a-1a7b-3e58-9a55-d66ca35b7c79 | -2.0831 | -50.4087 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1faebe6-dc6d-3a73-85fb-a88a502ee8b0 | -2.08069 | -50.39596 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ea1c407-84eb-30ab-97b5-eae258df03d0 | -2.0764 | -50.39531 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b69d5d3-fe80-3108-ac6e-96df0ba2f017 | -2.06501 | -50.66317 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59f74936-1d78-3db3-83fb-2f597efdc433 | -2.03348 | -50.75364 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a90c83ae-f8d0-3c28-b2f9-22390825d7f9 | -2.02989 | -50.74922 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eba29bc-b9fd-3a5f-bcff-50601ee3d00c | -2.02427 | -50.47744 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d52fac01-058a-3cbd-8f13-2ee709eedc77 | -2.02365 | -50.45286 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca738840-e71b-30c9-92f2-23f831575c85 | -2.02304 | -50.45686 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3182c6ec-f006-30e2-bf13-65fb9239052b | -1.99926 | -50.46951 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b130cf22-4a27-3fc5-a035-cb4b63fc3331 | -1.99672 | -50.42831 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c220b74-2afb-3928-9b25-b846fdeb082e | -1.99499 | -50.46886 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108168ed-15d8-310a-b56b-43185a51f655 | -1.99191 | -50.66089 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1923a7d-535d-3812-98c4-6d7ee922a1d0 | -1.98986 | -50.58913 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b81b810-f202-3f07-a614-857a461b6245 | -1.98547 | -50.86998 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9e1ac33-ad14-30a1-b09f-13d260d7108e | -1.97109 | -50.96288 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d6665ad-d04d-3e65-a62a-2b361f263e99 | -1.97083 | -50.65765 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a97b0e1f-cfcd-3289-9d08-9c406896a2ce | -1.97025 | -50.6615 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adb8427d-f745-3fbf-b82a-c69e689a432b | -1.95476 | -50.79214 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cecf3b04-40ea-3a20-8c68-fd5c95c90a68 | -1.95419 | -50.79592 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e861b74c-083d-397c-a92c-5190968a17f8 | -1.95058 | -50.7915 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 244d0274-5fe8-3406-82fa-b4e180dddae1 | -1.94224 | -50.79019 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f33db4f1-cffa-3f99-a746-7d6c4be4eaac | -1.92765 | -51.05368 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95a3031f-19c9-3a4a-ae49-be806edab9e7 | -1.92543 | -50.86558 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88905bfc-ea86-3647-bc02-f90fca9ad47d | -1.79487 | -50.59733 | 2024-11-03 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
