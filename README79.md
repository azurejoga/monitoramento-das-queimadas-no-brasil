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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dad1b8b0-91c7-3e77-bc3f-6e115d794069 | -1.39605 | -54.10852 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24684254-5ad0-3de5-ae53-c12f55c8160f | -1.39552 | -54.11197 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eac9046-2252-3612-a48e-eb8aa6fb16f4 | -1.38953 | -54.1287 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38e17cc8-31b4-327d-add9-e5cab549a8d1 | -1.38676 | -54.12475 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 377521d0-6f92-31b8-8cdc-da593ceea96a | -1.38622 | -54.1282 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0180e50c-acfd-3947-b1b2-509854170e5b | -1.38345 | -54.12425 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f961733-1cb5-3498-81bc-a2a60a36d429 | -1.38292 | -54.1277 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55878757-0bfe-3798-8972-9fa50dc40cde | -1.27569 | -53.37233 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11af6444-9bf6-348f-a384-fd122c14672f | -1.27289 | -53.36825 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 704b221e-e884-3e7c-84b0-f02544ffd0c8 | -1.27234 | -53.3718 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 525a7eb2-44eb-3b84-8acf-c9fbf09c0f30 | -1.25568 | -53.39093 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fa1b5e3-a22a-3744-bc46-0e01fbd6b4f9 | -1.25233 | -53.39042 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 233035ed-2561-39f6-8830-b20764c54fbd | -1.23216 | -54.15753 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4086dbc5-1aea-3cda-a406-da498b31c3f4 | -1.22006 | -53.38219 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 471172e2-ee00-3f25-9a6c-59d16fa9532b | -1.21672 | -53.38166 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ecc880a7-e69a-3761-967c-7725fad0d32e | -1.21439 | -53.65791 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75150e15-113b-3d40-a3d0-b1e44d4cbc7d | -1.21215 | -53.65042 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef11baad-7cd9-3745-8a80-74f3df131188 | -1.21161 | -53.6539 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a5eef7c-b49f-3cd6-8321-29ac2f801a96 | -1.21107 | -53.65741 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5ea78cb-ae54-3890-b502-69acf53e75ef | -1.21053 | -53.66091 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdfd2307-0c21-307d-b979-d02f779f2569 | -1.20936 | -53.64642 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| deb07d05-f7e4-36ca-bd12-0f0b215db263 | -1.20882 | -53.64991 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c617eb14-9f11-39e2-b716-36ee4fd655a1 | -1.20828 | -53.65341 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08829e1f-3e55-366a-a21d-329f9446286e | -1.2031 | -54.01466 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e1c86dd-c446-3d1f-acc8-e9c87ef2cccf | -1.20213 | -53.91206 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 159b6637-b001-3fed-ba48-0d4a7042a2c1 | -1.20159 | -53.91553 | 2024-11-02 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8ce85fae-3476-3abc-9e1c-2aba00466cfd | -3.62997 | -53.96243 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f862fe13-7e81-307b-aec7-dea11e932a50 | -3.62943 | -53.96593 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d3482dd-32cb-3245-a15a-151b3bf691e1 | -3.62663 | -53.9619 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 060c2901-3c39-3df8-ad51-f5889ce6c3e0 | -3.62609 | -53.96541 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e2342fa-dc8c-332a-a744-75012cd72511 | -3.51739 | -54.68637 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7882d4ab-9301-3de8-b84f-dab17fdaae6f | -3.49053 | -54.02703 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 962d7bdb-15df-39af-9e33-4fc4c00e51dd | -3.48998 | -54.03055 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db784427-2ca1-36e8-8e0b-76c2f8feab8f | -3.40595 | -53.80434 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c007657e-5d8f-38d4-8df0-68fb0a580b9b | -3.40541 | -53.80789 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf5af828-1ba2-3975-a2ff-575c1dc916db | -3.4026 | -53.80382 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac3f39a6-8f86-3b1f-aa63-439f62d9f4b0 | -3.37108 | -54.70907 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e08e31ee-5d4a-36d7-9e40-7e001f15c6da | -3.33872 | -54.61239 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f999c61-d324-34ac-8cc8-1449c74b76c1 | -3.33818 | -54.61584 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e02c1c4-6677-3fd5-bc3c-e55db37bded4 | -3.31318 | -54.13971 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ebd02b4-ab31-3e49-b7d6-f77ff906c7b7 | -3.3104 | -54.13569 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62317742-bc02-3d4e-89b8-f5e18001c249 | -3.30986 | -54.13919 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24ef09a7-b4eb-3837-83a4-5abec1535a2e | -3.3078 | -54.69913 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e02f3946-319a-3d31-84e2-e5b973bdb457 | -3.30761 | -54.13166 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7ae03e1-8d2b-39bd-a933-8b4a3b75871d | -3.30707 | -54.13516 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50d46bd0-c6ef-3380-bf16-17b609ff082e | -3.30482 | -54.12763 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dd4434e-11ab-399c-a54a-cff0246045af | -3.30428 | -54.13113 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f785d70c-57f6-3e72-86a2-dcdaf99086d0 | -3.30364 | -54.11319 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fed965a-f8c4-3c04-a14e-a86723dfa2e3 | -3.30311 | -54.11665 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a549f7ca-a4ee-3c22-ac3b-8d9aa0b094e2 | -3.30043 | -54.1129 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 713b009f-e980-3d23-a741-d108252db285 | -3.29989 | -54.11636 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad9f67ce-e137-35a3-a194-65cb206665d4 | -3.29336 | -54.15827 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6df97a78-24c9-3575-89df-ca2a27e8c095 | -3.29282 | -54.16175 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5fc653f-d194-3f48-9ce8-4d4ef8d0721b | -3.29228 | -54.16522 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aae8236-dbc7-38ef-825e-04069ad32d69 | -3.28949 | -54.16124 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b51f78b-91cb-36b7-a097-2b7ea51516f5 | -3.28895 | -54.16471 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0288854a-9d8b-3c17-8bcd-e379cdfe83a1 | -3.284 | -54.17464 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d484399d-79d3-35f1-b007-731f6853c0ed | -3.27348 | -54.17662 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14268d3e-14b3-3895-9b5c-7ad022852951 | -3.27239 | -54.18361 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 955515ac-99ff-3675-bd57-a51400c2fa7e | -3.2707 | -54.17262 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78b085f0-a3e4-3347-ab7d-8045c6d9bfe4 | -3.27015 | -54.17611 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe96b145-8e21-327d-88d7-f885420c0ee4 | -3.26737 | -54.17211 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23370bf8-29c6-3ee4-9d7d-d2e1b70a35a4 | -3.26683 | -54.17561 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34209524-0d9d-32c0-b2c3-65f6afa6ac5d | -3.25353 | -54.17358 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3dedb4e2-a79c-39d4-ba4d-fd217324d006 | -3.21499 | -54.09251 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4dbb2f6-0630-352b-9a12-4819eb703b8d | -3.20864 | -53.85007 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 794c6e76-3a57-3b9f-9f44-5ea4cc48837c | -3.20809 | -53.85362 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec6364a-1deb-36d6-aeaa-3d14335af38f | -3.20584 | -53.84602 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64b99be7-0945-35f5-852c-f819e38e5480 | -3.20529 | -53.84956 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fef9fcb-e5a3-3ef5-a1bf-741f0f16d6e3 | -3.20474 | -53.8531 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8a01476-a72b-3fa1-b4df-f83933fa47a7 | -3.2014 | -53.85257 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f651a2e-e8a1-3e2e-a327-f1797f28d3c8 | -2.65469 | -54.35037 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 685ee0c7-f773-3ec0-aac8-0ed5ca1fa960 | -2.65138 | -54.34986 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0ec4a73-47a4-3e26-bdae-3c6b81fe6fe0 | -2.65119 | -54.30741 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40dc610a-5ea6-3edf-be2e-d82d20be85aa | -2.64107 | -54.26337 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faeca406-d1bd-394d-9f41-54d52163af0c | -2.64053 | -54.26683 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0435c0f-4965-3851-a059-a1de0f47dffe | -2.63775 | -54.26286 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 27cd16e2-e595-3c6d-91e9-4046edb9296f | -2.63722 | -54.26632 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cfdb7d0c-e72e-35b4-8158-731f5e1a56cb | -2.59729 | -54.32401 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e3ea29d-a1ad-30ed-8384-dee75ee979d8 | -2.58187 | -54.7967 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d6ba406-cbe1-3277-9bec-fa2c555eb93c | -2.57964 | -54.78933 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac357ca0-356d-3807-a0c6-38470c6029cb | -2.57911 | -54.79276 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35b4f377-2fe4-359b-9255-1e59e26072ff | -2.57857 | -54.79619 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 115ff81e-fd69-314a-924c-dbdc445ba140 | -2.57687 | -54.7854 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 265c8c8f-8932-341f-8643-47e0b1da9e99 | -2.57634 | -54.78882 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 885f4778-dded-3c0a-8893-3c9fb0add219 | -2.57527 | -54.79568 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a643ca-13f3-37e2-bfa7-6a60595ed6d7 | -2.56241 | -54.28682 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb463946-891e-3673-a848-3c6daece8a59 | -2.5214 | -54.24516 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b7d1095-1c91-34ec-9e3c-7d1cd7d307f5 | -2.20804 | -54.53101 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d2a6a60-5768-34c3-bf26-1d1bba6b5cb3 | -2.20474 | -54.53051 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 287daced-0667-35df-86c3-9e9e80552419 | -2.20353 | -54.75504 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| de0c15bc-70d1-31a9-819e-6b5eb577269e | -2.404 | -53.66161 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14f7deba-ba19-3809-ad25-b430b6c19237 | -2.40345 | -53.66514 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14e5d6d2-d172-3d0a-b2a5-1c132fbf2ecb | -2.40291 | -53.66866 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2db037a-1ac1-3aa8-bf57-c85dbd43acf0 | -2.40065 | -53.66109 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e71605d-fef9-34a5-9a43-f271958aac37 | -2.30796 | -53.69025 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628ee715-061c-3739-b1e1-af61899015df | -2.27179 | -53.66262 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55d4eea0-8b02-3b14-b2a4-db6da9ef72f8 | -2.26845 | -53.66211 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea8035a5-a256-3e13-813a-c01db790373f | -2.2679 | -53.66565 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d1e2a9f-fb1d-37fd-889b-ced1b4a40b88 | -2.2651 | -53.66162 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README80.md)
