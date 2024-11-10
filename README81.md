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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b118411-fc14-38d8-9c6f-13b03c0738a7 | -3.96431 | -48.17712 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5b6df6d6-5276-36c8-9ac2-5a1b4c5d64fb | -2.82396 | -48.34978 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ca661cc-cf34-3ba1-8bed-b2bce813316d | -4.14494 | -48.25488 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 642a8949-c73c-34cf-9722-c37aabde7700 | -4.27616 | -50.18487 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9033af85-7f42-3f6c-a014-14b4ea7e5aed | -2.9414 | -49.43254 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 873ec6f1-72a2-3b55-ac62-8ebbe90705a6 | -3.98083 | -48.13696 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7f07990-7375-3d33-9c5c-17d7aa1e4d74 | -6.73376 | -46.38433 | 2024-11-10 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19d18451-cfb8-3fd3-a7e9-2d9119850d1b | -2.38743 | -49.82473 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f7c8ba4-3de0-3e98-8fb5-34c33b3ea305 | -3.87105 | -50.07379 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6edefbf9-9b76-30f9-a868-9d7688c8da7e | -3.2372 | -49.12519 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d44eb775-23e5-3bb9-919a-54f600f6a55e | -4.38062 | -48.15296 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eae3a74c-f144-35c5-bc74-c432d275ef3d | -2.45698 | -53.68948 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a311352f-795e-3af8-b8d7-5c4429bed33a | -5.39977 | -48.26069 | 2024-11-10 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 983fb029-aad7-39fc-a6cd-f9a6d9c52012 | -3.07044 | -48.03468 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a170843-2353-36b2-a90c-3c662d077138 | -2.8828 | -49.22681 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdce3dd8-bfd4-3855-adcf-e495a074511f | -3.87267 | -48.33354 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a049fb5-8a88-3346-87b3-b149ac06c8c8 | -3.4781 | -50.34566 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de7fd4d4-e62d-3393-91d6-4cbcd0f1cf03 | -3.38883 | -51.46168 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bad411b0-eb0a-3895-9e11-b31c8df8436a | -3.01197 | -51.04108 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bec57c3-111c-337a-836d-51e21fe07661 | -3.09107 | -49.50936 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d6e5c3e-59ef-3abd-8db3-3ed8b0c51180 | -3.28219 | -50.34895 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4b47ee4-5472-3228-b2fc-9cc1b42b42e6 | -4.09106 | -49.11757 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 905c4f5c-a49f-3b69-83ff-2fc5a9511331 | -2.85964 | -48.44714 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a76604f-187c-3125-ad3e-9c1b51210e08 | -2.21456 | -50.76669 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a8161a-0942-3c30-81b9-65fc3543e75d | -2.68202 | -51.82675 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fccb38-d0c2-369b-b272-595b7a2ae7ee | -4.60652 | -49.57948 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89272739-cfd7-3651-9b9e-6095b2a02d18 | -3.51483 | -54.03182 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea1b2bbc-10a6-3996-9af1-93a09640552b | -3.78928 | -47.46228 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ce66bdf-f47d-3c7b-bda7-f6b16a45ad1a | -2.48476 | -48.80929 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628d3439-162c-36ab-9639-6eca8348f507 | -3.04058 | -50.33051 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5947a13-b74f-3809-acb1-268568739fbc | -4.22794 | -48.61203 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e695e4bb-cf94-325b-b45a-b691942bf564 | -6.46346 | -40.77712 | 2024-11-10 04:38:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 920d1052-3fd4-338f-b59d-f0ab3a6ff5c2 | -4.09993 | -49.12605 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c46444ef-8161-3730-b5ee-5132b6e65e97 | -2.21801 | -50.45178 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cc0af10-a1ad-3f4b-97aa-ed5e62682b5f | -4.41761 | -43.64339 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2284a89-d85a-37f7-afa3-18e4a9162943 | -3.20182 | -50.63646 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f3bd3316-a559-3101-836a-0df55810ca42 | -2.24926 | -50.41066 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad5c9d3a-e3e5-3ed3-8460-75d28abf32a8 | -4.11413 | -46.8792 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd5a750b-49e3-3815-939e-d2c8bfbf8d7a | -4.57353 | -45.41132 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe5a1740-0046-3985-8aff-6125a7e0f032 | -4.36238 | -48.14622 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f166488-c78e-34d8-a6a6-80d7a3d21940 | -4.25832 | -45.85823 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94ff1cef-af29-3860-a760-c0793990b875 | -3.28206 | -49.46445 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63666b28-fe5d-348b-9dc5-f1092802c644 | -3.97927 | -48.16874 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ebc0407-46aa-39cd-825c-4465762e6196 | -3.04607 | -48.03798 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5511f4c6-f50e-3085-bb5e-73c72cb1c5b3 | -2.46022 | -50.40052 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84795f1b-d90f-3c2e-b1fa-37d01a2ddfcf | -2.38021 | -53.84837 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a1c72a-cb23-3737-a8fe-947875796f1f | -8.3789 | -44.1171 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17e7cbea-cce0-3083-97fd-5c930affba73 | -2.58624 | -48.16468 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e37385aa-ce18-3bcf-89a6-6dc8705b0903 | -2.24078 | -53.77014 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22228993-29c7-3bd4-b5ec-7dd882bf6213 | -3.18825 | -50.58833 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bbc6126-0394-3c2d-8dfa-9c7a9918310b | -2.85465 | -47.81221 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 578b8d5d-4c39-3c00-8f76-f16add579d25 | -4.10325 | -49.12656 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 27357f40-2c27-3e96-98a2-92ae8abc667e | -2.42453 | -50.42543 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98d2bbc5-2f7a-3b3e-8578-f4131d377623 | -3.24629 | -50.33252 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93227cf0-71b2-3374-957a-9b1e64f16029 | -3.09231 | -53.32728 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3928204d-7969-357f-b96a-c303b9bfbc4d | -4.31868 | -45.65976 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88266036-b919-3996-b2f0-79aa6768cdf6 | -2.61086 | -49.1875 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94a0514e-cd9b-36d8-ad49-2b887cd283e8 | -6.24354 | -45.68898 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ee68c8f-09de-386e-bcc2-f4606093ea62 | -2.36153 | -50.61978 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c45f421-5c4d-3f01-bafe-782c0818fa86 | -3.14846 | -46.50899 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9242934b-a450-3682-a4b6-afe3428766fe | -3.08493 | -49.56956 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8870bff-3be8-3404-b57f-79cc3e19ec73 | -3.44934 | -56.93443 | 2024-11-10 04:38:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c6183f-f188-3cd9-80e4-15846cf7e238 | -3.24922 | -46.44353 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c8afbb6-a969-33a3-b129-0c60c1b16254 | -4.1193 | -55.04528 | 2024-11-10 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1db590b9-8f9f-30d5-9413-4e94e759238f | -2.19365 | -50.23118 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0182fa3-cbbd-3699-bbe2-d1bc1a2b8d98 | -2.1234 | -50.84354 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf157f82-2ead-3be5-bd7c-613871e721f2 | -2.87128 | -51.4757 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| dc261322-b999-3f44-bf2d-776e8dad26fe | -4.11745 | -46.92542 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 231d9723-df8e-395b-92ac-6e10ef895367 | -2.89508 | -49.25727 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 294f4265-8056-36ea-a8a6-57763f9ceb5a | -3.90526 | -46.44239 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26d19b65-e00c-37b1-860f-0cd2617067be | -6.24953 | -43.5626 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cb71a47-920c-37b0-8315-9b95751f05ed | -2.69654 | -49.32931 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8b3f38-9f97-36a3-ab06-6bf5210e3cd1 | -2.67837 | -51.82617 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0160079-93e1-3950-900d-949e4bb61c8c | -2.22803 | -50.52273 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdc6a47a-cb12-3602-abd0-522f13deb8da | -3.12535 | -49.20725 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b41d9da2-061f-3fcf-baa5-8fc8c0d7b8f3 | -2.93297 | -52.77298 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 54ab61dd-f046-3726-993b-c863a52089f8 | -4.73052 | -50.37752 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 684e2295-3dd8-3133-9ec5-5ff71b02604d | -4.27279 | -50.18435 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf160f32-721e-378f-9582-d129ea29cc08 | -4.39895 | -49.4147 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f749c80-70c2-3a4d-96e8-96fb72d8ebf8 | -2.59386 | -48.31072 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f18e54-d68e-3b4c-af5f-9175aac9d5c9 | -5.29752 | -47.88978 | 2024-11-10 04:38:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2737e41-6079-3233-87fb-9611b9617097 | -2.98429 | -53.97818 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41c8293f-68c7-3f8d-9d3f-8bdf6f901b0c | -2.19434 | -50.82688 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 20da13a1-8919-302b-a7d7-25cf8b5b853b | -2.73421 | -51.89432 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 133debdf-de4f-3619-99ed-2a856a964875 | -2.7717 | -49.35182 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 979c5eb2-2689-37b7-89f8-fa8dca7cc6a9 | -4.2644 | -46.92018 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51d725be-e3fa-3498-b84d-d865a94cfd58 | -2.58956 | -48.16519 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62d5a58a-a279-365e-861e-7bb473a492f2 | -3.24652 | -50.46445 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 479053e0-d058-31c2-8269-c42c6718fc41 | -3.03959 | -49.54131 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e238bf57-213f-3084-a992-74873171cd74 | -3.09212 | -54.45988 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f35e75fa-ba3a-38a2-b995-62a5dd497f81 | -4.56412 | -49.59726 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15dae0f2-06e2-3244-a23d-82b5acce5f10 | -3.12507 | -50.4383 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 26576835-2a8b-314a-9765-528ade862c0e | -3.98035 | -48.1618 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea1978e-a941-3f7a-abdf-245da0b71bca | -3.69709 | -54.61288 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f20671a-5bb1-355e-abfa-693b0f8dafe1 | -2.84424 | -49.44984 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2ded7e3-8449-33c1-b075-4c80fc8a0179 | -3.39846 | -53.79909 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 729b12f9-f54d-35cf-a5b5-4e5e1f2bbce1 | -2.94039 | -49.52586 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e01afe6-219e-3477-967e-e2df015fd67d | -2.94019 | -49.3535 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49ef83b5-f664-3bcb-beff-90bc185d2649 | -4.79822 | -48.47092 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b00fae-99f8-3e7d-95ce-c0e7b89a3e49 | -3.69052 | -51.28656 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README82.md)
