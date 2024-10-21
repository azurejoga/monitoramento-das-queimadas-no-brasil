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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75ac8ec6-5665-3123-aa84-85877ac3c6cd | -2.79887 | -48.68064 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8cd7c9-885f-396c-b501-42c849857548 | -2.79886 | -51.36185 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ae56055e-5122-395d-84f1-8d6083eb8e87 | -2.79828 | -51.36523 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d2d27138-f9b9-3f90-9106-5832f5770b56 | -2.79816 | -48.68507 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7230d3a9-8018-3c71-bd85-29edaa6efe7b | -2.79771 | -51.36861 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 105eae5f-51a8-38fa-95a2-5ea6326bdba6 | -2.7975 | -51.35746 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a6b3a19-174b-3c5c-991b-b84d6dcffe50 | -2.79695 | -51.36083 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f13bb1bc-8c4d-33dc-bc79-37c884151bcc | -2.79641 | -51.36421 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07bda935-8767-396e-94f0-0418305fe469 | -2.79586 | -51.36758 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3d8094ac-551f-3f84-a99d-aeea27a8028c | -2.79531 | -51.37096 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1d041e14-1eba-300f-a430-656b4f547506 | -2.79406 | -51.3576 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd5b1e63-859d-313d-bcea-921fe0d26f2d | -2.79348 | -51.36097 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 01e87d4f-e3bb-3a4c-8fd7-bc466470acfe | -2.7929 | -51.36435 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b60e8188-b767-39c9-b223-e4d5bf5d0cce | -2.79233 | -51.36774 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0724ce1c-8386-3b47-8067-646d1e98f02d | -2.79175 | -51.37115 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6cadb4e2-4d3e-3f8a-b451-7fed4464e589 | -2.79158 | -51.35992 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8dbe0cc-ddab-3442-91b8-c00b781ac65e | -2.79103 | -51.3633 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac48e9fa-8552-371c-aef4-e32c0987f796 | -2.79048 | -51.36671 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 90744a65-7d3e-302f-8aed-17e2238fb1de | -2.78992 | -51.37012 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b928d8b3-0e65-3eca-8a89-9866d3ca2c9b | -2.78386 | -49.29499 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a26f8678-ba9f-3ee1-a4e8-21665a5a9060 | -2.78307 | -49.29985 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77a0806f-52dc-3bf7-a043-ede60d0efdac | -2.78228 | -49.30473 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc649024-f15e-372d-b678-8353e0c8cbe5 | -2.78149 | -49.30961 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d615cd3-095c-3b91-82dd-9955802c8481 | -2.7784 | -49.2991 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf911dbb-5cb6-3389-8cb5-ef841e94631a | -2.7776 | -49.30399 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0ecfe59-5b71-3b6b-b495-a64038d047ab | -2.77681 | -49.30885 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 432c5909-7a89-3b79-8a49-71cd9b82978c | -2.77602 | -49.31373 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 884fb00c-82b7-3c79-81a1-080718fd994e | -2.77373 | -49.29834 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c267e1b-1a15-3600-8714-27142918b2ed | -2.77293 | -49.30323 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 123d3fbe-ea98-33cd-a41e-d6d1dbaf2336 | -2.77214 | -49.30812 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1fdd291a-16dd-310e-807d-eaf819787d7c | -2.77134 | -49.313 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2da61c25-d13f-3d54-95b4-9e664554f0f9 | -2.77042 | -48.65786 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741ecd60-4bff-38e5-bdd2-5c564cbc4eaa | -2.76985 | -49.29272 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed326502-4ce1-37cd-9fab-25d50f8c6523 | -2.76971 | -48.66227 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d482720d-aa56-3b0c-84d5-baa0117a5559 | -2.76519 | -49.29195 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f720626-9715-3f6b-bae1-5f565234705a | -2.76333 | -49.36219 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12b428cf-191a-3e2d-9e4a-5e7579991374 | -2.75864 | -49.36139 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7df82d7e-c912-3ee1-9bad-09cf4754c573 | -2.69023 | -52.06777 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 105bcc46-737f-3e92-9dce-6f909549fcd1 | -2.68958 | -52.07165 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 285d2412-2f19-3138-8ba9-f08e25cefa9c | -2.68787 | -52.06749 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebf73307-091d-39fe-8929-6972f01e6bcc | -2.68724 | -52.07137 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd38e936-26a3-342c-87cf-603547068e02 | -2.64555 | -49.99137 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b0067ec-4061-31f4-838a-133451cfc500 | -2.64065 | -49.9905 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d556d2f1-9494-3ed8-b2df-5f1032a8ec9a | -2.63132 | -48.52655 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e19c5d4-6d80-3a83-87db-ef975bcfef27 | -2.6289 | -48.52871 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ad5dd22-f135-325e-8485-5b1513d7799a | -2.59988 | -46.12757 | 2024-10-21 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5df0a946-7404-3a61-a89b-656d84dc2f87 | -2.55651 | -47.34076 | 2024-10-21 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 262bb4e2-b344-3d70-bf84-b0dce651b3dd | -2.55288 | -49.18714 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 538b956a-353c-351e-adc1-94b3e5ec57e7 | -2.5226 | -45.98668 | 2024-10-21 04:12:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8262ee0-2207-38f2-ab9b-98f4772d2141 | -2.51957 | -45.98152 | 2024-10-21 04:12:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8660cd2d-3a65-3b8a-bc03-7fe6f6fd618a | -2.51883 | -45.98608 | 2024-10-21 04:12:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2892f9ea-6929-3733-9f98-b95736e6caf0 | -2.51736 | -45.99516 | 2024-10-21 04:12:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf477b28-7faa-3542-af34-b391d36b3b8e | -2.4869 | -49.11009 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 850e3405-7021-39a0-a9e6-a76a2dd783ef | -2.48613 | -49.11488 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 923b30de-b53b-3cf4-b7d3-12b0a6eec1c6 | -2.48535 | -49.11968 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0ec8403-89b9-3834-839c-5fca762535dd | -2.48305 | -49.10454 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836f4f99-3d72-3863-8a36-3f20c302e83d | -2.48227 | -49.10934 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9c9b037-e79b-3275-884c-30b97bcfca39 | -2.48149 | -49.11414 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00dda1a4-9123-315d-9416-08e8a3b2a4de | -2.48072 | -49.11892 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f69ab09-0252-3875-8d76-57d3a88854af | -2.47994 | -49.12372 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1eb883e-96e9-3c59-922b-89e27cf36773 | -2.47842 | -49.10378 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 341efc94-fd4f-33e1-8f06-103e17f0aaee | -2.47764 | -49.10857 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 415de6b3-a2bc-3c68-8bc7-0140c9333a63 | -2.47686 | -49.11339 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d16c2832-1b02-3d1f-bc2b-4c69218a4976 | -2.47608 | -49.11816 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0440ecc2-2b47-32b0-a081-ac95e34a4de8 | -2.47456 | -49.09831 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc8a3a65-5864-3172-ac2c-acb9d087d78a | -2.47379 | -49.10305 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08863160-aa0b-3d97-b9dc-e89a35696ed4 | -2.47301 | -49.10783 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ccfe041-ccca-319c-80bd-91a71db9aad8 | -2.47223 | -49.11263 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ccd2ec9-c788-3f60-a512-c34ced9d43f6 | -2.46993 | -49.09755 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d286c73-a0e5-3bdf-80c6-da88d0f598d8 | -2.46916 | -49.1023 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a710714-9786-3653-8993-3554cd998028 | -2.43186 | -50.33204 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d740595a-ab58-3031-a078-8273ffae8a51 | -2.42992 | -50.2797 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8302b225-e788-3c5c-b451-4062014f4497 | -2.42899 | -50.28547 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5ceca8c6-24cc-3bd0-a7e6-2a13c7ed33ca | -2.42785 | -50.28681 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c0969337-02fd-3057-919e-bb2200a9a18f | -2.42397 | -50.28463 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 324b14f7-155e-3dd9-b960-1ae02b21f156 | -2.41894 | -50.2838 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f0c40fa-8520-39f6-8ff5-de4aea7da0c7 | -2.38619 | -50.45412 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102b3954-2965-3675-bd23-d692ba8ceea0 | -2.3844 | -47.60653 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63e099a4-1cf2-33d6-8062-fec5938e0e2b | -2.38187 | -48.51217 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77f0fb2c-0049-39be-909b-e5470e90d596 | -2.37742 | -48.51144 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 486c89fd-9423-3772-b268-2b3cba9944b6 | -2.36511 | -52.51789 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af3a34c5-c850-3c03-841a-ffd38f8dd67c | -2.36446 | -52.52189 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cf4ec1a-10f0-3e73-b967-9b445120326c | -2.36193 | -46.82704 | 2024-10-21 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca06c26f-c698-3ab8-9851-db9ea72fa831 | -2.3586 | -52.521 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a738f96f-0c54-3def-8c52-b3d1a611e414 | -2.30281 | -46.62486 | 2024-10-21 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d757d28f-701c-3620-b7c6-82e1bc4627a8 | -2.30279 | -48.57598 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 534ed641-1366-309d-8c54-450035874b29 | -2.30205 | -48.58043 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88a8fd14-0ca7-3931-9f28-fd2988165263 | -2.29983 | -48.5809 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8db1d45-201f-372c-8e80-ee5a15989b24 | -2.29913 | -48.58535 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d382e47-4e9f-3b99-aed4-691b68e4a1fe | -2.29684 | -48.58418 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3210e9b-0f18-3b19-96fb-966f955927bf | -2.29609 | -48.58865 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1bd2e1c-a50b-3c04-a519-a48f044f5da9 | -2.29465 | -48.58464 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f08abb35-daa7-320a-9a0f-81b8b21b32c2 | -2.29395 | -48.58912 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6bfb642-901e-31b6-9e80-f697f4ab2515 | -2.28798 | -49.09826 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6542c72-1a57-37f8-b52e-a73982862da7 | -2.27413 | -53.75356 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad5ec3ad-404d-37ea-b869-2eee1b8f53dd | -2.27055 | -47.07796 | 2024-10-21 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4531fa-8ea6-3e11-8f45-fc1c6273b466 | -2.26698 | -53.75748 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c75481d-1c4a-338e-8591-3fced5c2c5f4 | -2.26649 | -47.07735 | 2024-10-21 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 809081bd-5e56-3a33-9f79-da2a176113bf | -2.26159 | -46.73978 | 2024-10-21 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aca23a5c-5fe0-3a61-9d14-e5e90bbab6d6 | -2.26034 | -46.73609 | 2024-10-21 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
