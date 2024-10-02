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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dac17c4-5f5d-3e96-a02b-880ab7a1f8bf | -16.52195 | -57.29326 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e069333b-986e-3d38-9543-0dbc6b32a1f3 | -16.52136 | -57.29724 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 50b7739d-ee55-389e-9bf7-441acbc81565 | -16.52086 | -57.33264 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4373872b-f04d-39ff-9cd2-4c3f5beeca55 | -16.52077 | -57.30122 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 030b47e9-a604-38aa-97b6-9bd66bd56e57 | -16.51955 | -57.33356 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f9a4f51e-95c1-36d9-a29a-086290be0fb5 | -16.51846 | -57.29271 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 97f53b42-52d8-3dda-aa1d-2a3b0dfe0357 | -16.51787 | -57.2967 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 623094ba-da54-3a87-ade5-ee2f07385ec2 | -16.51728 | -57.30067 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9c2e5610-8435-3ade-8e38-0f66b621b245 | -16.51607 | -57.33302 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bba0cec9-9144-3216-a6df-5b9c4fe05fb9 | -16.51556 | -57.28819 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| afe48982-52f3-3f17-bb70-90cf41e413b3 | -16.51497 | -57.29217 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 37751a1e-f73b-32ae-b730-0881b33a1d9d | -16.51438 | -57.29615 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 1196449d-9f63-33ec-bc36-6c779b091113 | -16.51207 | -57.28764 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3e3920f5-dece-39b1-805d-626db7ac6b5e | -16.51203 | -57.31207 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ed903d25-32db-35bd-a6d4-225adedc51cc | -16.51148 | -57.29162 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d9115d12-2771-39d9-816d-5b95a946ce67 | -16.51089 | -57.2956 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7e272307-de13-3661-92ef-6d37d441470d | -16.5103 | -57.29958 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2e773f15-38ba-3d19-a7e7-7da53db75a36 | -16.50972 | -57.30357 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4f3f7246-ee94-3a3b-a05e-d187caa5f847 | -16.50913 | -57.30754 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 06977d4b-2622-32db-ad92-fbb2adf42715 | -16.50799 | -57.29108 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d24a7caf-8bae-3c4e-a2c6-58946551014c | -16.5074 | -57.29506 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 84b298b1-b297-3be8-8081-c4391f41e511 | -16.50681 | -57.29904 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 90c180e2-23e0-3a7a-92b5-31158df5d191 | -16.50623 | -57.30303 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 47f6a846-342b-383a-97dd-423548b4b5be | -16.50564 | -57.307 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9bbf68d8-c8a8-3ebf-a970-7b54ef8a5e43 | -16.50505 | -57.31098 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1556e867-26dc-3a64-a1e2-3c690028fbdc | -16.50391 | -57.29452 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 03a69677-6d7a-3a80-a0bf-cecca2778af2 | -16.50388 | -57.31892 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c76cf6f8-423d-32c9-8ec4-47cbe39f9486 | -16.50271 | -57.32686 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 59c84549-2902-3a84-9f69-5f50729bb011 | -16.50215 | -57.30646 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6f464dcf-a92e-3098-98e1-f99c43852f86 | -16.50212 | -57.33083 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b3cba6d3-5177-33a1-be1b-edcd20c13674 | -16.50098 | -57.3144 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ce53aedc-ebb3-3671-a1bd-e4d5cac7938b | -16.50039 | -57.31838 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 20e18f12-54de-34ae-b9ad-2a1d1e263a53 | -16.49864 | -57.33028 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 73581741-b85b-3b70-ab00-0e2de9a2d48f | -16.49808 | -57.3099 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e968a24c-3d00-367b-bcb5-b2446d0c7444 | -16.49516 | -57.32974 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 17e7ce9f-dd6c-333b-8d91-733f5406aeda | -16.49457 | -57.3337 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 222cb132-f5a1-369b-bdf1-f322d7e23a6d | -17.13963 | -56.73505 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bfdf6314-ff57-3f7c-a509-2d9103eee49f | -17.13541 | -56.73875 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b6205f22-5b88-36e6-afbe-93ff01a887d2 | -17.13121 | -56.74246 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| d54dbdb0-207f-369c-bc6e-d7065c02ad29 | -17.12761 | -56.74191 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 008dd393-09ca-3e78-be5c-54dfbdeeb0a7 | -17.11683 | -56.74026 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1a645601-8722-3d5c-aa22-fbce83f7d28e | -17.11024 | -56.7349 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b2670044-994b-327c-b717-dea0708f9184 | -17.10781 | -56.7519 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ba12090a-c551-3831-b81d-b155b8978413 | -17.10604 | -56.73861 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 72f439c4-3575-39e4-af62-4caac7330507 | -17.10543 | -56.74286 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3fa4e90b-c28d-34ff-9be2-e3277d9b110f | -17.10483 | -56.74711 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7958e44f-49a0-3ac7-a2d5-b2f597822a82 | -17.10422 | -56.75135 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4fb20b10-baab-3c3d-a1da-13e800e382de | -17.10361 | -56.7556 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3c8740a8-7f71-3eb8-a197-e3c2607171a4 | -17.10301 | -56.75983 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| e4b3ddc9-50eb-31ec-b0be-aaf7fc58ba7b | -17.10123 | -56.74656 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| acd5f667-6dc5-34dd-9c63-51400f3c430d | -17.10063 | -56.7508 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2f94ce40-3f98-36d9-a6fe-e64f2ab81440 | -17.0982 | -56.76776 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 4419d7b1-378a-346d-9b9d-3dac3ef6db9b | -17.09461 | -56.76721 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 958d57cb-c283-32d8-b8df-56586b8efceb | -17.09404 | -56.74545 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d68978c8-de36-3f23-b777-9ef06550470a | -17.09344 | -56.7497 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e507e129-e185-3969-963e-b44d4cfca629 | -17.09283 | -56.75394 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7f902dd2-7e89-3f56-b93d-65b44600aabc | -17.09223 | -56.75819 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 66b3f2d4-67fc-3a87-abfe-f4da09242775 | -17.09102 | -56.76666 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| fe5acc1b-dce6-3b04-9c11-d8e3702cf6f2 | -17.08864 | -56.75763 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 41ff0542-3377-3401-a778-8be542fffee4 | -17.08804 | -56.76187 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 8709aa84-954d-3e23-ae95-6af096194fc1 | -17.08505 | -56.75708 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 91742653-4902-319a-ad55-b17b94a59e18 | -17.07606 | -56.7687 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 14e1983c-d924-31e5-b884-4fc32eee02e2 | -17.07187 | -56.77238 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 23212310-a2ad-3cee-af1f-148206a91794 | -17.06889 | -56.76759 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 80ffc391-a698-339d-bccf-1e9881bd6624 | -17.06829 | -56.77182 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| abc9fab8-7707-3f2f-8afe-98fbeab485ec | -17.0647 | -56.77127 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e40b76c4-2cb8-3dac-9f07-33c8430a6f47 | -17.0641 | -56.7755 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 786895ae-32e1-3c33-ab97-ee69a8dc7b2e | -17.06111 | -56.77071 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| a32d6c7b-4c91-367d-b0ff-62b9253cf895 | -17.05394 | -56.76961 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| be4a36d3-88a7-392d-8778-66561d5b581c | -17.05154 | -56.76058 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 92ff97be-ae77-3675-a821-da0b6063cba8 | -17.0515 | -56.70847 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 16ad638b-1e8c-364a-88ad-ad16ca7a9a6f | -17.05094 | -56.76482 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6cbd98a1-5e7a-36fa-bbe7-2f910d3cd87d | -17.04972 | -56.72126 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 953fda38-7237-3f45-a8d9-0a9fef94f648 | -17.04735 | -56.76427 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6eb1e70c-4d2e-35aa-9675-66475c7bc067 | -17.04674 | -56.74251 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9c70db6f-9ced-30ce-b220-c02962db45dd | -17.04614 | -56.74675 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0ed19cd5-6a1d-3fca-8c74-2c4883310309 | -17.04612 | -56.7207 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 20f02994-6a3a-3049-9dcf-db3481981717 | -17.04496 | -56.75523 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e1378c3e-e470-3ad4-8545-f5333119ed8e | -17.04436 | -56.75948 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0d4f17df-d2e8-35c4-b6de-8500aac56448 | -17.04315 | -56.74195 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e8beffab-5d7a-3413-b1ce-06a67bd9d758 | -17.04074 | -56.73291 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a0e553ce-ed35-3cc0-accf-4bf8f76fdf67 | -17.04025 | -56.72586 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c9360761-a074-3339-b268-9404d80dde34 | -16.69954 | -57.21202 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a4dda1e4-8d87-3d45-9171-6d505b1bf81b | -16.69954 | -57.18729 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 16394e0c-26a4-3c5c-a2a5-6583ed5b7dc9 | -16.6972 | -57.17866 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e1a729a1-f350-3684-a618-503ab307270c | -16.69661 | -57.1827 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 05acb3c2-aa3b-3117-9895-3a63b59881eb | -16.69603 | -57.21147 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aba2a4b5-02a2-34ae-a533-44c0ba247a87 | -16.69603 | -57.18674 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| c3d60fb5-687a-3e6c-a4ae-93806c8de439 | -16.69544 | -57.19078 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 815f6b0d-3639-3875-a086-196effb07ba0 | -16.69369 | -57.17811 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e7f8336a-032f-372d-b36e-436b47b65796 | -16.6931 | -57.18215 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e59a5b75-a78b-3ad7-a6b8-701565bd5d0a | -16.69252 | -57.18619 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1c759ab6-306d-342d-a2b9-de2618a36207 | -16.69195 | -57.23962 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 05c6cd14-b8fb-3d79-91e9-6f320b59f43d | -16.69193 | -57.19023 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 6ab34094-87a0-3313-a3b8-33b1e63499e7 | -16.69017 | -57.17757 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d21ec149-5244-324d-b359-dcacd532b5e4 | -16.68959 | -57.1816 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 4be855fa-9640-36cf-b795-1bdbff53e316 | -16.689 | -57.18564 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 2fb3100d-4d8b-3b8f-b7a8-79aa29857102 | -16.68784 | -57.19371 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0edf1bdd-267c-3f6b-b978-d076a942e6ef | -16.68608 | -57.18105 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 407321cc-03ba-335f-a6d2-e719ae32ee80 | -16.6855 | -57.18509 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README150.md)
