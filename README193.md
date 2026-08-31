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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b35182f-1b83-3e84-8e48-71ae9accb13a | -10.9859 | -48.4308 | 2026-08-31 19:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bc7aa695-9e73-303e-8688-11d3a207a615 | -11.7973 | -47.6672 | 2026-08-31 19:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 549fd1c6-1530-3cc3-b93b-b439469af294 | -9.0057 | -65.456 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6d74fe2e-9287-3a2d-ad71-8ac1b514bcf6 | -10.3199 | -49.9996 | 2026-08-31 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8a303579-4441-3645-87cb-b09b7ad1bdd7 | -10.8043 | -50.5259 | 2026-08-31 19:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| fc8e9c5c-fc0e-3d63-8c01-8e86b14ae6da | -9.2144 | -47.99 | 2026-08-31 19:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5c99c1a1-2893-3319-831d-852fba6bfd37 | -19.1736 | -57.416 | 2026-08-31 19:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.7 |
| 352ea5b4-ea68-3daa-aaa5-6831151ee86b | -6.6233 | -58.383 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 52ff1b1d-fd2f-3688-ac8d-23d216b02c04 | -7.917 | -61.3481 | 2026-08-31 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 14fe9c4b-a741-306e-9361-6fc18a49df3e | -11.3236 | -45.1778 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 442154bd-3722-32f8-8e80-c7511d083d3b | -8.6859 | -62.8172 | 2026-08-31 19:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 21f722f9-ad5a-3975-8701-8e7dd9f38a92 | -5.8686 | -52.1693 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1595065b-30bb-3795-9c1f-019113430059 | -9.1953 | -48.0138 | 2026-08-31 19:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0ec30ff0-3971-37dc-a924-e965ec1ec911 | -9.1419 | -61.1027 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8880d934-0369-3828-a217-3a5535df1d69 | -8.9428 | -63.2797 | 2026-08-31 19:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1a382c91-f878-3ce0-b9a0-9371ba58df8a | -5.5831 | -60.2307 | 2026-08-31 19:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d6fe162c-8ce3-332c-971e-d2c36781f6c1 | -7.0243 | -59.2181 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2635a829-9829-3da9-bf48-9f0b36b5cf86 | -10.8631 | -45.333 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e1952c4c-003b-3b2f-923c-dbfe7d0894b5 | -19.1347 | -57.3589 | 2026-08-31 19:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.0 |
| ababa213-564d-3e00-ae95-bb9b88d32e6d | -10.8218 | -50.6306 | 2026-08-31 19:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 934fbc5b-491c-3c1b-9772-04f4704b4b47 | -11.5283 | -45.4933 | 2026-08-31 19:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c2c88437-da56-3d6b-ace4-b3e394ec88d3 | -14.5028 | -52.1913 | 2026-08-31 19:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 579379b3-7cb1-37f5-ad76-465ad8b99850 | -4.9788 | -55.8417 | 2026-08-31 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| df3656e7-4877-34ae-9045-91c5283f59dc | -9.0059 | -65.4186 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ad755aaf-2011-390d-b0db-48ea8b27ba1e | -6.6792 | -52.864 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a7665562-bda8-34a1-a1ee-2ba0fad4db0b | -5.8872 | -52.1683 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1fe2b168-da26-31a2-8857-7106e11e3c93 | -6.1175 | -59.9452 | 2026-08-31 19:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9cfbe7a1-31ee-3db8-9d0b-0bcf68b8be95 | -5.8688 | -52.1487 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5284a75c-1cb0-3641-98aa-8e409f0ab5b9 | -9.208 | -65.8044 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 95c5bae5-0313-385b-877f-5e9ecc39418e | -10.9862 | -48.4088 | 2026-08-31 19:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| fd60f287-bd56-3119-9a1a-ca20aa749514 | -17.3228 | -42.6878 | 2026-08-31 19:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 300.6 |
| 879ad564-8b6e-3ed0-a137-7023f3f0f048 | -9.1711 | -59.618 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6921101f-f67a-3969-85d2-e1d133bce0b5 | -7.7941 | -44.0609 | 2026-08-31 19:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2489aae6-608e-363e-9df1-b2ab4231a1e1 | -15.9703 | -55.9583 | 2026-08-31 19:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 363175ac-0d49-38db-b5b5-d731899b41d5 | -8.8207 | -71.2797 | 2026-08-31 19:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 0a8e287c-6008-30ba-ba75-5c7de43d7774 | -11.2107 | -45.0786 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 19042d2a-fc10-33a5-814b-a1f0cc1fd5cf | -2.7303 | -47.0644 | 2026-08-31 19:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 660b4d79-259f-3cc7-9e3c-dcce92be524a | -12.1113 | -45.0163 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4cd51d1c-d894-34b7-8a6a-774ba1fe6d5a | -12.0921 | -45.0192 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 0cd8ec61-d203-3818-9c97-60b4a51dc9de | -5.4876 | -57.1416 | 2026-08-31 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 95c3ce0e-f4a7-3ed5-8ec5-9368517a1e49 | -10.5719 | -57.495 | 2026-08-31 19:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ecd979ec-c274-38fd-86fa-aac12088fd00 | -10.0677 | -59.412 | 2026-08-31 19:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 64667341-185f-3e28-ac40-f341a623a6bb | -10.4634 | -46.5638 | 2026-08-31 19:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7ad494e1-cf45-30bd-9306-6db6ecf064af | -14.1263 | -52.8106 | 2026-08-31 19:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 88de984d-8b0e-3873-9eac-ce7b4088e01f | -9.1897 | -59.6171 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b0078ae4-f1a3-3d0a-82a6-c2e768eda1ec | -3.4002 | -61.3465 | 2026-08-31 19:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f143d25b-461f-3d10-8dc3-8ef817f012a8 | -19.1344 | -57.3797 | 2026-08-31 19:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 210.8 |
| 18aa8001-ef53-399d-8d91-cf02caeaf07b | -2.7118 | -47.0649 | 2026-08-31 19:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1525682e-9fc7-397a-a51e-c908f6fcaf65 | -3.1083 | -61.2191 | 2026-08-31 19:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 97d76ba3-9280-3626-aedf-9644f0512b2c | -6.8009 | -59.5742 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b90d15c2-2af2-3bd7-959d-717bba9b21f3 | -3.4185 | -61.3273 | 2026-08-31 19:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6a3dfbb0-4ac1-36c9-8d03-8137f9783b58 | -9.1895 | -59.6364 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| eb45aabf-5ddc-373c-9a9b-f4cd6b931626 | -6.3844 | -55.2251 | 2026-08-31 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5e891e57-79ad-39c1-a5dd-6d6c843e10b3 | -7.9894 | -72.3483 | 2026-08-31 19:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 367e29a6-6d3f-35b0-a257-d6bc86853a58 | -2.7304 | -47.0424 | 2026-08-31 19:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a8f8a134-fc9b-323d-978c-7e8171aae539 | -3.8692 | -49.1202 | 2026-08-31 19:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 002a14c3-606c-3db6-982c-ce18923b30bd | -9.4149 | -45.6953 | 2026-08-31 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d60acd8b-9ed8-3c52-a595-4d6fc5ccfbe4 | -9.1529 | -59.5609 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 69743bdf-c67f-3130-bddd-d94bbb1197e6 | -9.0245 | -65.3994 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| fb522bc6-5eba-30bd-8f8a-945b3595e31b | -3.9708 | -60.0067 | 2026-08-31 19:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ede68138-b50c-39ad-9e69-c8162c879ad4 | -3.4002 | -61.3276 | 2026-08-31 19:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| bcec2d68-54b3-3f60-90a5-9a36bca63858 | -12.9225 | -45.8352 | 2026-08-31 19:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 19aafa3c-fda7-3133-aaa5-f7b996f3b431 | -6.0743 | -57.6465 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 8b8933b2-6f83-32bb-ae1f-3ed90525545d | -7.0703 | -52.7175 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 1117c75d-545b-3b44-a66b-8bf435e5d237 | -15.8844 | -56.4819 | 2026-08-31 19:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 2e1ee0ce-932b-30cd-af2f-90b65318a71a | -11.6975 | -54.5467 | 2026-08-31 19:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| cb7b63b1-b20a-3126-9d23-83c2258f5002 | -10.1134 | -45.8621 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 189.7 |
| c7102e83-f57a-3624-a10b-e0c1f059a215 | -11.2478 | -45.1425 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a7aeb730-cdc4-3018-8f83-f29e0e2889c9 | -7.6805 | -55.3355 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 65babff4-7abd-379b-8711-a4dbc7ead870 | -11.0747 | -51.5153 | 2026-08-31 19:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 09ef98fa-faf2-3022-be27-356ae365aed9 | -11.5479 | -45.4676 | 2026-08-31 19:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 308.8 |
| a69a5e88-2ab4-3892-ae05-e1f5414f7944 | -19.1547 | -57.3562 | 2026-08-31 19:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.5 |
| 5ee45e97-5a75-3ce2-9879-79d25c52a63c | -9.0058 | -65.4373 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e7780ccf-301b-3489-9e51-ede1f898fe55 | -6.1294 | -57.6833 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4fcdae45-f6fc-34be-8ed4-0dbcde2d8f03 | -6.8193 | -59.5734 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 55e00b80-8f21-3e0d-9310-b726589a1928 | -8.7628 | -46.4642 | 2026-08-31 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 50d4b03a-9ada-3029-ba98-80c546643f7a | -14.5868 | -54.1153 | 2026-08-31 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e2b1bcaf-e6a8-31bf-9646-9feea92df66f | -10.7593 | -54.0589 | 2026-08-31 19:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 78a70c52-22b7-301c-a7a0-50cc37de91cc | -9.2256 | -59.7894 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 47fcbce4-7d3e-371a-b401-c57b35a77fc9 | -14.2599 | -52.8782 | 2026-08-31 19:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 27e7bada-306f-38f8-b94f-36124627f1ba | -2.7119 | -47.043 | 2026-08-31 19:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ad9b4bd7-0b78-3b12-b34b-2f95f3cbb630 | -8.7439 | -46.4661 | 2026-08-31 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bc878001-4c13-3b32-85cb-c6a1f91d5831 | -3.4185 | -61.3461 | 2026-08-31 19:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 9fac9c29-66d2-396b-9147-1dcb3616d246 | -15.7349 | -56.1093 | 2026-08-31 19:10:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| c6115e96-f1e3-31a9-bcd4-5919e5470f69 | -7.0292 | -55.6511 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2244e2fd-64b2-3f27-aa34-8d6cf27515f6 | -10.4963 | -59.6001 | 2026-08-31 19:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 21c3e1e4-f38a-38e1-9bb6-42bb458a2173 | -3.3871 | -59.4075 | 2026-08-31 19:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 292f8c3b-a35c-3cc0-b02a-6b630741f308 | -8.5363 | -67.1617 | 2026-08-31 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 33eaff46-5f16-368c-856a-db2eb89acfcf | -8.5739 | -66.9754 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 31d9e7ef-8473-3029-b0cb-ac0fe6f9004f | -7.77 | -61.2015 | 2026-08-31 19:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 38b68b28-dc1d-38f9-ad8f-e10dad7c2a30 | -8.3601 | -70.8458 | 2026-08-31 19:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 4cf6553d-c675-3041-82aa-8fd75942f412 | -6.4055 | -49.9228 | 2026-08-31 19:10:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 8eb83307-52ae-30c5-8e7f-ca6b926a9f84 | -3.3871 | -59.3883 | 2026-08-31 19:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 13002088-1f17-3f43-a6e9-6457378f1f09 | -17.9064 | -52.0737 | 2026-08-31 19:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 60c72d3e-3895-387a-942c-389a49bb0e99 | -5.9636 | -57.6704 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e159fb62-61fa-3270-84a6-bdd5ded05b18 | -11.0936 | -51.5134 | 2026-08-31 19:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 7270a2bc-57dc-344a-a641-d9518610494c | -11.5475 | -45.4906 | 2026-08-31 19:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| e12ec847-8ad5-3928-b9c9-678834e06ee8 | -8.87 | -66.9121 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b889dbf8-91fa-3fc7-a191-332ef4271223 | -13.5341 | -59.7589 | 2026-08-31 19:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a42fa0eb-7a3d-3a70-9203-354f9c41201c | -7.6251 | -55.2987 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 243.1 |


[Clique aqui para ver as próximas entradas](README194.md)
