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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef29dfa4-6dfa-3451-a91d-dc7b1c0e8999 | -6.3096 | -42.492599 | 2024-09-27 00:35:15 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb771e64-4e89-30c2-bcbd-d67d42f356e1 | -6.2999 | -42.4949 | 2024-09-27 00:35:15 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| df5056de-3a15-32c7-a653-a391e4242d2b | -6.2901 | -42.4972 | 2024-09-27 00:35:15 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aba568b8-d0b6-3f3b-bd5f-adbbe19fd010 | -7.5162 | -47.551601 | 2024-09-27 00:35:15 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce478751-ec38-3a49-8276-08b4c8fa569a | -7.5178 | -47.558498 | 2024-09-27 00:35:15 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb884d80-3655-335c-ac18-bf707e6f191f | -7.5064 | -47.553799 | 2024-09-27 00:35:15 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74f058a9-ab8a-34bc-a49b-1d62a36c4671 | -7.2793 | -46.600498 | 2024-09-27 00:35:15 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed061ef-85a4-3d2c-b68e-37a47181b582 | -7.2678 | -46.595402 | 2024-09-27 00:35:15 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8abbb1c-114b-3717-8b4e-491d01e8cb56 | -7.2695 | -46.602699 | 2024-09-27 00:35:15 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4491be0a-4a37-3046-8f54-36f45599e555 | -7.2711 | -46.609901 | 2024-09-27 00:35:15 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d6e67f3-c840-3ef3-82b7-713821d6d5bc | -8.6631 | -53.168598 | 2024-09-27 00:35:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4e94899-fe75-39fa-9c85-18eba3f732fe | -8.6654 | -53.179501 | 2024-09-27 00:35:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af626a2c-08b8-35fe-89fe-458facf62caa | -8.6533 | -53.1707 | 2024-09-27 00:35:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bab3936-fa66-3ee4-803f-8ba35f2ea460 | -8.0327 | -50.427299 | 2024-09-27 00:35:17 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73aa833e-2246-3c89-8d35-b3ae7f8017d7 | -6.5693 | -44.158298 | 2024-09-27 00:35:17 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa93c6f2-bd31-3b1d-aa7a-ce72c40c7cd5 | -6.5716 | -44.167801 | 2024-09-27 00:35:17 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d8b3383-845d-32f3-8519-eebdb33a0eb0 | -6.5738 | -44.177299 | 2024-09-27 00:35:17 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12e8ad4e-bf82-3c3b-a1f4-e26ed1cb5fe4 | -7.0968 | -46.4342 | 2024-09-27 00:35:17 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cfb19b6-b5b0-30db-8889-5d1f4028513c | -7.0985 | -46.441601 | 2024-09-27 00:35:17 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be093b23-9b22-335d-ae80-9ffe12e87fdd | -7.898 | -50.000999 | 2024-09-27 00:35:17 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4bc2b1-97e7-3523-b260-29c5dd157743 | -6.5596 | -44.160599 | 2024-09-27 00:35:17 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfd6464c-6066-3f8a-b2ae-1e09bb282417 | -6.5618 | -44.170101 | 2024-09-27 00:35:17 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9edcd33b-01f4-38d1-b046-d11b441b2b56 | -7.8882 | -50.003101 | 2024-09-27 00:35:17 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78f48860-ca46-37f7-9c25-928985994e6a | -8.5734 | -53.324699 | 2024-09-27 00:35:18 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82534e59-760e-3dcd-9ad1-3409c9ff9741 | -8.5758 | -53.335701 | 2024-09-27 00:35:18 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5524e853-c917-3472-9bd6-a7cb08ee1554 | -7.0167 | -46.805 | 2024-09-27 00:35:20 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8054ef31-0a51-31a9-a0fa-b31ebdaeb1ca | -7.0183 | -46.812199 | 2024-09-27 00:35:20 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64aa2b22-b86e-3fe6-82e9-0fcec89c9585 | -8.7038 | -54.777302 | 2024-09-27 00:35:21 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ddc5669-784b-3439-bb85-eba0b32ac401 | -8.7067 | -54.791199 | 2024-09-27 00:35:21 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3bc956b-c7ea-37a0-9b49-33d9ca64c7e9 | -8.6912 | -54.765499 | 2024-09-27 00:35:21 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0814eb6e-edee-3949-838e-aede68afa01a | -8.6941 | -54.7794 | 2024-09-27 00:35:21 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66418c31-6328-388e-a9a6-f0cb1782b9b1 | -2.6783 | -57.5893 | 2024-09-27 00:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c33d86ea-0306-3665-b2bc-3d411a30d7c5 | -2.8611 | -51.6699 | 2024-09-27 00:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a66027ea-ce6e-34b0-83b9-3edd2a3bfa54 | -2.8795 | -51.6695 | 2024-09-27 00:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 48862b34-521e-391a-9084-d52c91c32c41 | -3.0107 | -51.0652 | 2024-09-27 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| db0a13a4-6ab0-3fed-8a5d-105e31c22f88 | -6.3847 | -44.780102 | 2024-09-27 00:35:23 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad8042d-47ca-3974-a21e-85d61b99165b | -8.5359 | -54.557201 | 2024-09-27 00:35:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8abad52f-b7e4-328d-b36d-80a75af1bd2d | -8.5262 | -54.559299 | 2024-09-27 00:35:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44160244-7d02-3eff-be25-96508cafdf67 | -8.529 | -54.572601 | 2024-09-27 00:35:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc6de76-fd6f-3d53-8a81-600a7b106aa9 | -3.1134 | -59.1445 | 2024-09-27 00:35:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| cfb37869-0e1c-3ec4-9309-e9b6b662a119 | -3.1135 | -59.1253 | 2024-09-27 00:35:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b52c27eb-83fe-380f-a053-415c8a5eee3c | -3.1317 | -59.1441 | 2024-09-27 00:35:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| ade0f13b-f84a-3704-8d30-a47d69196134 | -3.1318 | -59.125 | 2024-09-27 00:35:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7f6a5f61-ce78-32cc-b011-3ff44643dd17 | -6.6607 | -46.330799 | 2024-09-27 00:35:24 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9529e4ae-9db6-3a29-bc14-6d52f5df8da5 | -7.3551 | -49.544701 | 2024-09-27 00:35:24 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 112538dc-3d5e-3586-9cc7-748bda84c393 | -7.3566 | -49.5518 | 2024-09-27 00:35:24 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f905b5d-fb48-3504-8f55-3b81100f3418 | -8.4258 | -54.663898 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8101bd1-9807-3094-bd86-5d3f1cd5ba45 | -6.0489 | -44.004601 | 2024-09-27 00:35:25 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18f5f865-c34f-3de7-8ae7-7539ad43d573 | -6.0512 | -44.0144 | 2024-09-27 00:35:25 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9861511b-2c23-3958-9925-821273b7aeab | -6.0535 | -44.0242 | 2024-09-27 00:35:25 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03015035-2689-3e20-9272-e6e2c132e5b8 | -8.4188 | -54.679298 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5597d4f-bbc7-3d31-84d5-240af30bc772 | -8.4216 | -54.692902 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44fb43db-2e12-3b56-94a2-c6ba55699831 | -8.5179 | -55.1567 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1527f060-b2f5-3b3e-b4b3-e3b5aab16549 | -8.5209 | -55.171299 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 171b666d-ef76-3bf8-a8b0-bc68f2d68a04 | -8.5082 | -55.158699 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 858d6108-a3ac-37ad-b861-deabdfd9046f | -8.5112 | -55.173302 | 2024-09-27 00:35:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2340243-f468-3b17-aab6-7c975d9237c9 | -5.8701 | -43.856998 | 2024-09-27 00:35:27 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 298f1618-32b7-396a-b471-bf6265ef61b6 | -5.8724 | -43.8671 | 2024-09-27 00:35:27 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8211371-362e-37d8-bbf1-6dbaac014477 | -6.4068 | -45.9888 | 2024-09-27 00:35:27 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdaddd8-895a-3507-8a2c-9217eb407c39 | -6.4086 | -45.996498 | 2024-09-27 00:35:27 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9110fe59-e05d-309d-b613-d1b281c6a549 | -6.0952 | -44.687801 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71905999-9466-37a2-9d16-0ccc500d1aa3 | -6.0973 | -44.696701 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a2de7f0-fb34-384b-976d-65104db7eef8 | -6.5487 | -46.652 | 2024-09-27 00:35:27 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3b680ae-5d3d-3dea-b875-fdc2a320f3fb | -6.5504 | -46.659302 | 2024-09-27 00:35:27 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e72627d9-1608-367d-ba7a-8da1e50414de | -6.0854 | -44.689999 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8125e034-003f-37fb-8de6-47739e933b11 | -6.0875 | -44.698898 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7f6b06d-16d2-3f4c-91c1-312822df3913 | -6.0757 | -44.692299 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b472b74-617d-3392-85fb-45ee3dd83a7b | -6.0778 | -44.701199 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa3bf9f-90cf-3760-b843-9b6b2100c00f | -6.068 | -44.703499 | 2024-09-27 00:35:27 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 189ab9c5-f60d-3c3f-a075-2295270f6666 | -8.3514 | -55.0406 | 2024-09-27 00:35:27 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb618c6-cdce-3e9d-8b2e-f09335084a34 | -8.3544 | -55.054798 | 2024-09-27 00:35:27 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41015291-c60d-3732-89fe-91bd55c61b4c | -8.3417 | -55.042599 | 2024-09-27 00:35:28 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 504c6cbe-a1f4-39d7-a790-56cc9f23df2c | -8.3447 | -55.056801 | 2024-09-27 00:35:28 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 139f47ed-619d-3cd8-85ca-bab86297376f | -8.3201 | -54.987801 | 2024-09-27 00:35:28 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a42e0dbb-2d98-3b28-bc37-93e913d4d36f | -8.3075 | -54.9757 | 2024-09-27 00:35:28 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc197a2-cff2-3606-ba6e-a2d09bce32b0 | -8.3104 | -54.989799 | 2024-09-27 00:35:28 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2f3232-6a28-3791-9f3b-70f8a007d5dd | -8.3134 | -55.004002 | 2024-09-27 00:35:28 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f57f3df6-a9a2-392d-bd29-a1c9ffe6a28b | -5.5768 | -42.918098 | 2024-09-27 00:35:29 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2b5803a-5e18-3224-a9a0-b75257b5a61c | -5.5795 | -42.929798 | 2024-09-27 00:35:29 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ff520cc4-89a8-316a-8c32-ae86c148ac24 | -5.567 | -42.920399 | 2024-09-27 00:35:29 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 305cedff-05ea-320e-abe9-5bdc6a850276 | -5.5697 | -42.932098 | 2024-09-27 00:35:29 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| afe41578-ace2-33e4-920e-f56e7e6d83ad | -5.5725 | -42.943699 | 2024-09-27 00:35:29 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d412cea-52d1-3a65-aa8f-1cd731558abb | -8.1121 | -54.771099 | 2024-09-27 00:35:30 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d0cbd3-28c4-3a46-8f6e-f2bc3a5d21bf | -8.1084 | -55.046299 | 2024-09-27 00:35:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 992be024-6e94-3f83-9510-9aaa8ee46cd9 | -8.1114 | -55.060501 | 2024-09-27 00:35:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54c9ac5f-0e15-39e6-ab04-26670e0fd778 | -5.6854 | -44.344501 | 2024-09-27 00:35:32 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26d1ac62-4fc3-311b-a864-042697e2aed0 | -5.6876 | -44.354 | 2024-09-27 00:35:32 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25a7e5dc-0edd-33ca-a75a-695b687d756c | -5.3952 | -43.414001 | 2024-09-27 00:35:33 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b126e3bf-cb79-361c-82f7-7da55f67adf4 | -5.3978 | -43.424999 | 2024-09-27 00:35:33 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b75f6fd4-51f7-3d6f-8c68-3cde0c4fccd6 | -5.4003 | -43.435902 | 2024-09-27 00:35:33 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99f20913-87be-38dd-8123-7b4f0b1a351f | -7.9237 | -54.6982 | 2024-09-27 00:35:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3681b1e1-9ea1-35ba-929a-a0ca76a0972a | -7.9111 | -54.686901 | 2024-09-27 00:35:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17040963-d340-38fe-9632-cba7709ce04a | -7.9139 | -54.700199 | 2024-09-27 00:35:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 131caa3d-5e8f-3ead-96e4-d8cb4cfbc952 | -4.3189 | -39.124699 | 2024-09-27 00:35:34 | METOP-B | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 226a4d33-319c-3213-829f-67d7c58f72ea | -5.388 | -43.427299 | 2024-09-27 00:35:34 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf9ac095-1921-3d7a-9670-95d30c67c159 | -7.8846 | -54.706299 | 2024-09-27 00:35:34 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5f9a06b-1b94-344e-870b-89e52ff7c40e | -5.0199 | -43.7839 | 2024-09-27 00:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| bceb0176-59b1-32dc-bcc0-1616ef441f74 | -7.8107 | -54.694 | 2024-09-27 00:35:35 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 737129a0-6e1c-3d70-ab05-29bb027c7af8 | -7.8135 | -54.707298 | 2024-09-27 00:35:35 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9743fbe1-e298-39c1-8c68-d3b8dd0cc883 | -7.8163 | -54.7206 | 2024-09-27 00:35:35 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
