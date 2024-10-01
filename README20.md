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
| ae0e33cd-1175-3d9c-9c04-3ec08226f1fc | -2.9092 | -49.5191 | 2024-10-01 00:54:10 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb13968d-967f-39b7-a4c6-6da15db9b5b4 | -3.0862 | -50.469501 | 2024-10-01 00:54:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 894e6973-6ea8-3eab-8617-e74eac8a544a | -2.9038 | -50.7076 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a0c515f-b043-3f91-b7a7-a865a56f784b | -2.9056 | -50.715599 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6203bb32-e041-3e3f-8e31-1ffc0c5c3c10 | -2.9075 | -50.723701 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12b16bdd-ec57-3a32-9ec2-2841a6d13e1e | -2.9093 | -50.731701 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b308743c-e8f1-3201-8aeb-a50ee83f9701 | -2.9111 | -50.7397 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0125f113-bfd2-3096-a591-b94f62c02110 | -2.913 | -50.7477 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a639f9d8-9efe-345a-a8e3-22d3d5ec78b0 | -2.8903 | -50.693699 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9c0ecec-a0bd-3a8d-bc4c-0fa7c69e58c1 | -2.8921 | -50.701801 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec12fda6-1b6f-36b7-95ff-3e5adaa7f2bd | -2.894 | -50.709801 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d7e9d86-4188-3f60-be3c-a44f5ca089cd | -2.8958 | -50.717899 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f48622c-92dc-3d6c-90be-87b7d51dbdf8 | -2.8977 | -50.725899 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c27e085-4b18-3b14-aa24-56f85f1b376f | -2.8995 | -50.733898 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7175567-04ca-3420-9f9f-dd2f83ccbefd | -2.9013 | -50.742001 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28127561-4320-37a8-bb05-fc300d6b8f15 | -2.9032 | -50.75 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a700a6-f7aa-3222-a956-3fd96eeb5e04 | -3.0329 | -51.3181 | 2024-10-01 00:54:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c46ee0-1fb9-321b-bc15-da729d1472b1 | -3.0346 | -51.325699 | 2024-10-01 00:54:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9be56d-77f7-30ce-a722-5bf7a95e825b | -2.8786 | -50.687801 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 642af32b-7f8f-336f-b849-e65a83f906b0 | -2.8823 | -50.703999 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f990a2a6-12f4-3457-9caf-1eaed85aa526 | -2.8842 | -50.712002 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795bf500-6f91-31bf-9bc0-43ccb3cf00e4 | -2.886 | -50.7201 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f574ce0-555e-36ae-bdf6-e342490a9d0d | -2.8879 | -50.7281 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab875b2-40c7-37ec-a727-cec20572e1a5 | -2.8897 | -50.736099 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae7b02e0-a9aa-316d-b0d6-d3ec4bbc8cf4 | -2.8915 | -50.744202 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5843152-b6b2-318b-8da5-168883d3736a | -2.8934 | -50.752201 | 2024-10-01 00:54:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaa5c3aa-55bc-3b80-9199-be54d8a06095 | -3.0231 | -51.320301 | 2024-10-01 00:54:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0248e719-52c1-348c-b86e-8db5b1ea316f | -3.0248 | -51.3279 | 2024-10-01 00:54:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4e86531-2387-3f93-a725-6ba91297f398 | -2.8688 | -50.689999 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee3ae51-92c3-307d-b4e6-85bb0d1192b7 | -2.8707 | -50.698101 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66cad456-8e81-3f03-a05e-33d7b1dc0de0 | -2.8725 | -50.7062 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a5082d-cf4c-3560-ae40-24fcaaeb68d5 | -2.8744 | -50.714199 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d7b156-3e78-3b13-9dff-a93056740dbe | -2.8762 | -50.722301 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713546ca-524f-31f4-a228-6b91d958d9b1 | -2.8781 | -50.730301 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc12b4fc-f3c0-31f9-9c88-765b40c3aa9b | -2.8799 | -50.7383 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd39a0c-3e89-3485-bbf6-15f2be240bd7 | -2.8817 | -50.746399 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 222898bd-a943-328d-bc91-9e83dc8f101c | -2.8836 | -50.754398 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf6e33d-272e-373f-acfc-ae29b2740ee9 | -3.015 | -51.330101 | 2024-10-01 00:54:15 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5481ff7d-9cc9-399c-9a19-6a4750395dd6 | -2.8609 | -50.700298 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb214fe-1fe1-3505-8bd8-6e64ce7b819d | -2.8627 | -50.708401 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b4c90f-1667-3e49-94e1-4751c5dd0a73 | -2.8646 | -50.7164 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 685dba6a-d5d7-3830-9023-40f8bd7b4f40 | -2.8664 | -50.724499 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90555ebb-cc05-3922-9694-904c3d01d5ae | -2.8683 | -50.732498 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66cb6e55-8127-3ebb-a1f3-c7d26ecbfa50 | -2.8701 | -50.740501 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fe2bcd-3a65-3acd-a090-18f2e010042a | -2.8719 | -50.7486 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70e98685-fdf3-3673-a395-435ba817eb24 | -2.8738 | -50.756599 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1e5f5ed-3ce1-3d0d-9d85-25e706c1eda3 | -2.8492 | -50.694401 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9e2fff-c2b4-3ed9-8e95-f91013ad6a5b | -2.8511 | -50.702499 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36cd8b89-a80f-3ace-9af1-774ed8cfe4d8 | -2.8529 | -50.710602 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdaaf4cb-29be-3adb-abe5-8a0810c8525f | -2.8548 | -50.718601 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd6c8f55-9a9f-3ffd-bb9c-2b98ce062814 | -2.8566 | -50.7267 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb5bfaf8-7bc9-3e00-8628-1f0d231c740b | -2.8585 | -50.734699 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f51ec736-f547-36e1-8201-6f4ad9bc7d69 | -2.8603 | -50.742699 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d92ba96-92f3-358d-9e94-d4645b9724fe | -2.8621 | -50.750801 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9787597-b08b-3e7d-acc8-1829c63b1f93 | -2.8394 | -50.696602 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff85863a-b4d8-3271-88d7-3609b0c5448e | -2.8413 | -50.7047 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83648b0-6010-34cd-849f-9d720455ba13 | -2.8431 | -50.712799 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39db1744-633f-3091-9d60-92c8a1389254 | -2.845 | -50.720798 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65eb4160-ec42-3252-9530-f808416f9aac | -2.8468 | -50.728901 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf5b4cbd-c151-3011-b767-e5593fa4b79b | -2.8487 | -50.7369 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e70a7a3-1918-306c-ae38-ddc4d7025f58 | -2.8505 | -50.7449 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e15f1d9-3639-329a-bbfe-8504c478648b | -2.8333 | -50.715 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2d733c-d5ec-37fa-9fd0-865cbd762039 | -2.8352 | -50.723 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09e51035-93fc-38d0-bd96-9274b3f081ac | -2.837 | -50.731098 | 2024-10-01 00:54:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71daa6af-61bd-3268-aa14-3f3822b1ce86 | -3.4686 | -53.786098 | 2024-10-01 00:54:16 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 323d17ef-0f3d-3951-a327-52d6d17a9781 | -2.4022 | -50.3158 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1a35f2-a24a-3a73-86fa-f1f218ab9944 | -2.4041 | -50.324402 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45218e2-874e-3911-9813-46cb6038d180 | -2.3885 | -50.300999 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e517a284-613e-3c4d-97ad-f4df3cddee97 | -2.3904 | -50.309502 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05de8c7a-0843-3bf1-bd5c-15d019917a96 | -2.3924 | -50.318001 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5842e20-5699-3799-bc33-e39e56d0a335 | -2.3943 | -50.326599 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3789852-63b6-3b01-8757-bea9b76e44de | -2.3807 | -50.311699 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abae4c20-d461-3f9b-9557-a845d3442272 | -2.3827 | -50.320301 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 846bfc72-7545-3596-9d1d-9bfda3ca52b2 | -2.3846 | -50.3288 | 2024-10-01 00:54:21 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0ee1ffd-8970-3f6b-a0c8-6e6365602020 | -2.6761 | -51.6968 | 2024-10-01 00:54:21 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3fc23b-4456-321b-aef5-303b3d499aba | -3.1223 | -53.712399 | 2024-10-01 00:54:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0de25546-66c6-37be-9a1a-fa57d7cc56ec | -3.1239 | -53.7192 | 2024-10-01 00:54:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5143cb-8a63-3b4f-afa5-1dba412f6170 | -3.1254 | -53.726002 | 2024-10-01 00:54:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc144fc-5af6-31a9-ba5b-d12b25f43db5 | -3.1269 | -53.732899 | 2024-10-01 00:54:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447dd288-c45e-3b9e-912e-f6858fdc1829 | -3.1285 | -53.7397 | 2024-10-01 00:54:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf6a388-3659-304b-8284-e3f7c22eeca7 | -2.8554 | -53.306 | 2024-10-01 00:54:24 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97e024d-4ac6-3adc-ba3a-540a875439b5 | -2.8441 | -53.301399 | 2024-10-01 00:54:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a226a3d-45fc-3bb1-baa6-7c5c8edcb686 | -2.8456 | -53.308201 | 2024-10-01 00:54:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93fb9c8b-af90-38d2-9c44-2576a89661eb | -2.9319 | -53.690201 | 2024-10-01 00:54:25 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90825050-89e0-3bfe-9d94-9be0dccea580 | -2.6108 | -54.917999 | 2024-10-01 00:54:34 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef157b9-929d-33e3-8683-fa3f93eb80c8 | -2.3492 | -54.350101 | 2024-10-01 00:54:36 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e38538f3-c41a-39c7-8f68-aee8ecceea29 | -2.4872 | -58.043999 | 2024-10-01 00:54:48 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aac6aa20-66d6-3f05-97ee-2b4e74d6c8fe | -0.1582 | -51.5396 | 2024-10-01 00:55:02 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d95d58bc-70ac-3471-8188-b3cf878f3355 | -0.1599 | -51.547401 | 2024-10-01 00:55:02 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 74f39df9-f50e-34ec-a614-cd40f4cd591f | -2.4048 | -50.3085 | 2024-10-01 00:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| c55caed0-5a1a-3105-b451-4d93b33406e1 | -2.4047 | -50.3295 | 2024-10-01 00:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 378.7 |
| b9ec29e9-4126-39b1-bf42-0e537f0ca06e | -2.4046 | -50.3505 | 2024-10-01 00:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 172ac9f3-f65b-3984-88e9-4d37b19807ba | -2.3863 | -50.309 | 2024-10-01 00:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 14cc4529-83d7-3c84-a513-18b10af9363b | -2.3863 | -50.3299 | 2024-10-01 00:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 82290756-e635-3e46-9ace-e478fcae9f68 | -3.0282 | -51.3345 | 2024-10-01 00:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 68e60a00-4499-3de5-bc17-ce791210c3f4 | -4.6987 | -49.8062 | 2024-10-01 00:55:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c7af318d-9ed6-3d6e-8304-4508c02927cf | -4.7172 | -49.8053 | 2024-10-01 00:55:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 595c5334-ae61-349b-9598-54b8c2b92844 | 2.1266 | -50.664001 | 2024-10-01 00:55:35 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 778e6cb7-e918-31bd-9134-19f415766d21 | 2.1245 | -50.673199 | 2024-10-01 00:55:35 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 944ac6b9-9a2c-3051-9dbc-3c269cbf157d | -5.7715 | -45.5574 | 2024-10-01 00:55:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |


[Clique aqui para ver as próximas entradas](README21.md)
