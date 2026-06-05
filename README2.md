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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2de94b3-dd04-3b85-9c00-455dd22bbfcd | -8.7211 | -48.3222 | 2026-06-05 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| a462d0dd-d28a-3a87-a509-15e901edb8ab | -11.5499 | -52.7867 | 2026-06-05 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 26247409-71d7-3564-b454-c9f11b975692 | -12.4466 | -58.4627 | 2026-06-05 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d7cf7b14-42b9-3021-a1b1-a2160dd8857f | -11.5493 | -52.8284 | 2026-06-05 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1abe5a9a-10b8-3a01-bc70-1e3040a0f7e5 | -12.4464 | -58.4825 | 2026-06-05 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 831327e3-bd29-348f-b3ca-0a6d710de34a | -8.7208 | -48.3441 | 2026-06-05 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| fad28c0a-8ee0-3c0c-bfe5-782d88bacf11 | -11.5688 | -52.7848 | 2026-06-05 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b2244aaa-7562-3e98-8d23-3356937bf1f9 | -11.5496 | -52.8076 | 2026-06-05 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 293.9 |
| d38b8045-81b9-38bf-9be5-15824dc62172 | -11.5686 | -52.8057 | 2026-06-05 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 169.2 |
| ba5e63fc-b849-3aeb-84ed-24c0d8805e22 | -12.4466 | -58.4627 | 2026-06-05 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 73cba646-cf84-3d9a-9615-2c9bbd05b629 | -8.7211 | -48.3222 | 2026-06-05 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 846629fc-5795-3ff9-b3cc-b934fa5ddf02 | -12.4464 | -58.4825 | 2026-06-05 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9a601996-cf36-38da-9a13-b05a09c0fd31 | -11.5499 | -52.7867 | 2026-06-05 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| be89e504-779b-3faf-89eb-47c3888359e1 | -12.4274 | -58.484 | 2026-06-05 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 6c587180-ac9c-34d9-b97f-c1655c50e007 | -21.22584 | -48.96249 | 2026-06-05 00:24:00 | TERRA_M-M | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 57a0c3e6-ec21-3545-acdd-f44fbc022a40 | -19.71776 | -54.65533 | 2026-06-05 00:24:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f0abf45c-e521-3ba9-a673-7a2a0bcca524 | -21.2753 | -48.61395 | 2026-06-05 00:24:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 482e8270-a5c0-3085-8ea6-0afc5485f096 | -21.27684 | -48.62417 | 2026-06-05 00:24:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 03670bf3-73ca-31fa-9680-b62262566317 | -19.72802 | -54.65409 | 2026-06-05 00:24:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1fc7b394-f1d0-3a60-a8f5-036408aba789 | -19.73785 | -53.54835 | 2026-06-05 00:24:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 38ab0c42-1fa0-36c7-ba64-ca5175da7ef1 | -19.74741 | -53.54705 | 2026-06-05 00:24:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7c011aa8-2113-3699-b43b-df9c969e2bc4 | -21.19763 | -48.2684 | 2026-06-05 00:24:00 | TERRA_M-M | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4e4781cd-09e4-3d40-960f-1a316be0d2e7 | -19.73651 | -53.53739 | 2026-06-05 00:24:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b07ca241-ae8d-31b6-8d95-12247df7d2a1 | -19.73921 | -53.55945 | 2026-06-05 00:24:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ef8e2c28-8e93-3f4e-8cc7-7d04b70fed83 | -21.81196 | -49.12017 | 2026-06-05 00:24:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 0cdbef4f-be33-3345-af5f-a5b8749108e9 | -12.31557 | -54.11829 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| fcdbdd41-3a82-3d2e-b681-9f8694e0d358 | -11.07075 | -54.51379 | 2026-06-05 00:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4402b80a-988c-3e61-8c97-7f41310856aa | -11.5772 | -54.58202 | 2026-06-05 00:26:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 934ab08a-d1ba-3a1b-a3ca-891ac9cd1767 | -10.57433 | -57.33131 | 2026-06-05 00:26:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b55e71d8-8053-322c-a134-decbee471b05 | -12.44876 | -58.4809 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b41ebd42-72d9-34f6-8f33-d86bcada8e34 | -12.44557 | -58.48768 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5bd36b4c-cfbd-333e-983c-051a153adbb8 | -11.88262 | -57.82592 | 2026-06-05 00:26:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4345eb3c-d028-3186-84d2-a43ce3a41514 | -14.1034 | -59.38641 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f4e92a58-00ea-3beb-899e-64601fea2aa4 | -11.00774 | -54.31792 | 2026-06-05 00:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b0b4842-e088-3d6d-9b41-0f9fde5dce5b | -10.86579 | -53.73874 | 2026-06-05 00:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7bdeb4c-c0aa-3692-a438-fa9fa7c94f84 | -11.54972 | -52.80549 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 202.9 |
| 5b485d50-435c-3a57-a4b5-ca72423c7930 | -11.56612 | -52.79399 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a940faa4-8077-36db-9257-2f21f3192e86 | -12.09266 | -52.00551 | 2026-06-05 00:26:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4c8e9c4-aafe-3c7d-b84f-ee3788cb828d | -9.76632 | -50.01568 | 2026-06-05 00:26:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 746d5d83-d56c-32cb-b6a2-63f9eaf72129 | -12.2284 | -57.28592 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6d7fa067-3805-391f-af7f-036b0d3d0d39 | -11.38816 | -47.81391 | 2026-06-05 00:26:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 045bb56a-4e28-324c-af86-ad87f1ecae7b | -12.80971 | -54.85899 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6593651c-1d98-3786-82fc-aa518795b5ea | -12.43648 | -58.48244 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c0d3b9ba-37e6-35e3-8620-abcdbb72a1b9 | -11.55854 | -52.80421 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 308.0 |
| 2ed9c2d3-dc47-358d-86ac-6653590272b4 | -11.55095 | -52.81443 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| f19d2d5e-e73f-3a0b-b6fc-651374ada6e9 | -12.43859 | -58.50095 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4c53d639-9456-3346-a2ac-a0341c428773 | -16.1482 | -58.49842 | 2026-06-05 00:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 0dbf0057-05e9-306c-bd74-da14c6b12f54 | -12.44337 | -58.46965 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 8c96e4ab-a477-3972-b160-09fa239dedda | -12.09013 | -51.98743 | 2026-06-05 00:26:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 838f3ad9-aa70-3365-b66e-b9bce22b4d08 | -11.03194 | -44.31297 | 2026-06-05 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 76c2679f-dd7c-3deb-b0bb-1c55de4de5ba | -11.05742 | -56.92069 | 2026-06-05 00:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8599ecfd-258d-3831-9015-e32d6481a74d | -10.59979 | -55.42306 | 2026-06-05 00:26:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 07af5b26-236c-3671-95c4-9a3ca0f2b583 | -11.56736 | -52.80293 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 41a7c603-a4d8-38d0-9911-fd66273af1e7 | -11.55977 | -52.81316 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 87f1aec4-fa6c-3be0-8b26-93e41e80c0c3 | -12.72747 | -54.74365 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ffec64c4-437a-37b1-8d8a-845ef9392082 | -16.59966 | -58.22692 | 2026-06-05 00:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| a4807ad4-38d0-3c65-8242-766b8b3769e8 | -11.03671 | -44.34154 | 2026-06-05 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ea4fab11-ca87-3b50-9bc2-fd3162097f5c | -14.09178 | -54.33921 | 2026-06-05 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 4b9f0ec3-320c-32e6-9ebb-5ab94933b6ae | -10.57261 | -57.3173 | 2026-06-05 00:26:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0cc26e6d-54fe-3a42-b761-0647bab5d041 | -12.44251 | -58.42657 | 2026-06-05 00:26:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| bfebb34f-ec26-32ed-b594-ebe761d26b1a | -14.09767 | -59.38168 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1e2a4da5-809f-3cfa-b16b-f138e5bb5fd8 | -14.10011 | -59.40435 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 760ce85d-efd1-3cd8-91bf-cee61a9bc486 | -13.51765 | -54.31096 | 2026-06-05 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 4bdde979-37c5-3d61-adf3-642ad02e3a6a | -12.4404 | -58.40829 | 2026-06-05 00:26:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| fda1c570-63b4-39d8-bae5-0108cca98cdf | -16.60129 | -58.241 | 2026-06-05 00:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 52fbab54-1cb9-39e8-82ba-801faa9aad3b | -12.43328 | -58.48915 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f8d820d6-c4f3-3aae-8cc9-47357083674c | -12.4467 | -58.46301 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| c0eabaff-0904-3774-8c35-ef40e3ba7446 | -14.77336 | -52.67719 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d55feae3-9204-34b6-83f8-369bf125893f | -11.54849 | -52.79654 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 4eda3e8c-4103-377c-a789-1c729c310e3e | -10.91 | -54.13647 | 2026-06-05 00:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1d32f073-4f1e-39c4-b56c-240a0715ae74 | -12.73422 | -54.72174 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0084a499-d44f-3ce8-b8ae-fcc9dd04f66b | -11.60915 | -55.33803 | 2026-06-05 00:26:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 682d8104-cded-35d5-b6a4-98a26165c257 | -11.03544 | -44.33641 | 2026-06-05 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a37213a1-fe34-3341-bd0d-2e1cc50139bd | -11.59955 | -55.33932 | 2026-06-05 00:26:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d805dca5-0f96-3c1b-ada9-7a89b40cc507 | -11.05302 | -56.92897 | 2026-06-05 00:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| adace0fe-d072-354b-ac4c-8bb6ba3fb6e9 | -11.27375 | -53.96629 | 2026-06-05 00:26:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07d4ece8-aa20-324a-87ce-fa12b0904243 | -12.81108 | -54.86942 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 064570fe-31cf-3b62-b77e-1d740f053ebc | -11.00649 | -54.30841 | 2026-06-05 00:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 48a5e21b-0af8-3bf0-b89c-5a94f4595cca | -14.04649 | -53.36584 | 2026-06-05 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cac54e37-fa79-3faa-a6ba-128a1ed76e1a | -11.01682 | -54.31665 | 2026-06-05 00:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bb76607a-c79b-3e00-ac7e-b03bbfb376a7 | -12.72614 | -54.73335 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7cc7dae4-3c40-327b-86dc-8acdb9bdd6a3 | -12.73687 | -54.74229 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ce9f665b-def1-3f75-8f8e-7ec47e65ca45 | -12.31684 | -54.12785 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| eab70c06-f80a-37ce-a275-d19732f08e5a | -11.55731 | -52.79527 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d5d3c467-abe5-3b64-8b35-d91f18b19ecd | -12.0914 | -51.99647 | 2026-06-05 00:26:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9faa462b-6f33-37d4-90ee-0da70e26bd0b | -11.54055 | -48.27337 | 2026-06-05 00:26:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 014f656d-ea67-3f4b-9ec7-04a078f6d6e6 | -12.0638 | -48.07982 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d581f5ff-b8c0-3adc-8db2-588787ecdc48 | -12.4509 | -58.49943 | 2026-06-05 00:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 28efcf2d-db87-3bc3-baa1-13ffa658cadd | -11.61052 | -55.34876 | 2026-06-05 00:26:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fb811226-1a4e-3157-aaeb-283b22474e3d | -9.89505 | -52.44397 | 2026-06-05 00:26:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 251adfc8-8df8-350a-a20e-75b4a2c88540 | -10.38898 | -49.44779 | 2026-06-05 00:26:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 8b13d6b5-3988-3449-808f-1a7d75d37660 | -16.12215 | -58.50148 | 2026-06-05 00:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 4720dafb-7556-3b6c-af1a-e182ea644ec9 | -14.30315 | -58.63993 | 2026-06-05 00:26:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fff1c9b8-9a0b-332e-b3f2-e897c7055a9a | -12.45264 | -58.40699 | 2026-06-05 00:26:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f01e04d8-4d3d-3658-a895-a217194d0803 | -12.73554 | -54.73199 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 1afa67e9-c84a-3726-bb6a-ba82b4fc41fc | -16.60198 | -58.24763 | 2026-06-05 00:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 60426248-0a48-342d-bc64-ca9ac7e3b2a2 | -11.3328 | -51.39127 | 2026-06-05 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ec334b5-a183-3d7d-ae93-8231cfc38fae | -12.22663 | -57.27122 | 2026-06-05 00:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f8ec0dc5-4698-31c5-9a27-342656afa832 | -8.04988 | -50.68081 | 2026-06-05 00:28:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 71c160c8-ac54-312a-bdd0-48c5ac19ff7b | -8.66013 | -54.72546 | 2026-06-05 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README3.md)
