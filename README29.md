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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 908ee98a-b157-31ca-a86c-19bbcf6d3309 | -6.59713 | -35.24991 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c369c249-7c2e-331f-9c87-fe9f5aabfd1f | -7.19695 | -34.98491 | 2024-10-08 03:15:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0364e1c6-c3cb-3dfe-a2c7-fdb03a74cf84 | -7.19624 | -34.98902 | 2024-10-08 03:15:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 756b82b4-25d7-3982-a825-283e51be3429 | -6.99618 | -34.9482 | 2024-10-08 03:15:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 22b1cce3-fbf8-3a37-99c6-a19f277a9ab9 | -6.99255 | -34.9433 | 2024-10-08 03:15:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1374e9f2-8d0d-3a4a-ab9f-ece38b6671c1 | -6.99182 | -34.94753 | 2024-10-08 03:15:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 306f9ac2-7d0e-3e6c-87bb-870c2e19dae1 | -6.99109 | -34.95176 | 2024-10-08 03:15:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| c7a697d7-2f3a-352c-8747-2e0bcbf99cbc | -6.60478 | -35.244 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4f42fa36-1ddd-3e86-afa0-9830018e3176 | -6.60312 | -35.24194 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a8fe0fd8-3a68-3c3d-9c6c-22e1c275bf9a | -6.60237 | -35.2462 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 63aed599-2d5d-32b3-bf65-581b158a9ba7 | -6.6003 | -35.24337 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| c4ed7090-1a6f-3f1c-9563-cb84e6bc5435 | -6.59788 | -35.24564 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b37025d9-0c26-38d2-a60e-7627bd40e866 | -6.67199 | -37.46941 | 2024-10-08 03:15:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9bc2251-509e-36ac-9645-ef193d083b59 | -6.66678 | -37.4687 | 2024-10-08 03:15:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9bd7c9c8-c117-3472-9e4c-de2f3e8ca134 | -6.43375 | -38.83167 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ca906f4-85d6-34f2-9523-02870efee753 | -6.43302 | -38.83574 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6b7cc82a-4026-3656-97e7-db48fe07fe93 | -6.43225 | -38.84002 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 52dd471b-b5d0-32f6-8409-e013cfe27513 | -6.42872 | -38.82704 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2895c8ab-445e-3a4e-9225-ca5e45f28f2d | -6.42799 | -38.83103 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96f0cfa8-6b72-39d1-89d3-a62649491ca6 | -6.42722 | -38.83532 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dfdfa3a9-0e44-3d47-9609-a38ec57d1f89 | -6.42574 | -38.84351 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6886d617-d344-3d63-b5df-a94f2c1785f2 | -6.42502 | -38.84748 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10b8e738-d91f-3844-bf85-fb2abafc4a77 | -6.42296 | -38.82641 | 2024-10-08 03:15:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49e3e237-27b1-3c3c-b993-fe41db9ed520 | -5.5718 | -44.87 | 2024-10-08 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c6a7d3de-6b7c-38dc-ada7-066b6746c8ed | -5.5716 | -44.8927 | 2024-10-08 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 195f2a72-32f6-3354-aee9-067bc950ad74 | -9.445 | -66.7289 | 2024-10-08 03:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 042f8316-db94-30e3-b6c3-c71932676d9b | -9.4087 | -66.5438 | 2024-10-08 03:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 370b3dde-5637-3b1e-8290-a14f881de7fb | -9.3901 | -66.5444 | 2024-10-08 03:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 61e0fa4d-8706-365a-b65d-eb807420ea2e | -10.6256 | -55.9154 | 2024-10-08 03:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f2658168-5c29-340f-a673-ea413c24b0fc | -10.8755 | -63.8979 | 2024-10-08 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bdcd7c98-4e08-3fe6-a1e5-8f16d26d10d8 | -10.8754 | -63.9169 | 2024-10-08 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b938a082-1f25-3ab5-8cc5-de52d5fc698e | -10.8941 | -63.916 | 2024-10-08 03:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 05e9d0ad-88ce-3d36-9fbf-5a4f8c6cd9a3 | -11.3461 | -51.0635 | 2024-10-08 03:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5971cec8-3bb6-3c3d-9297-a15b89812d06 | -11.3081 | -51.0676 | 2024-10-08 03:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 982fb728-7dfa-3984-9bdb-2032ba17d931 | -11.5233 | -65.137 | 2024-10-08 03:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e4951ef8-9534-3800-9f2f-be3bb4a62918 | -11.5232 | -65.1559 | 2024-10-08 03:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 82e1b878-3268-3bf3-8446-0b9a79d7e886 | -12.572 | -53.0544 | 2024-10-08 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| ea03abec-80cc-3c08-94c6-31a5b8a5781f | -12.5717 | -53.0753 | 2024-10-08 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 8816ba9e-b62d-349f-851c-ee68884fb833 | -12.4605 | -62.9977 | 2024-10-08 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e496cc11-2d0f-38d7-a8dd-0324ea9761e2 | -12.4603 | -63.0169 | 2024-10-08 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d547725b-80d0-3495-b86c-3ace94da3523 | -15.7068 | -59.4326 | 2024-10-08 03:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f84c4a00-084f-3776-b60e-1dc83b808421 | -15.6874 | -59.4344 | 2024-10-08 03:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8aa0b58c-1e7a-3f04-b5c0-bc1ab300b717 | -16.5902 | -46.4746 | 2024-10-08 03:16:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0dfc1a29-4cff-3771-9015-45220066ae91 | -16.9211 | -57.4881 | 2024-10-08 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| ac2c2b95-3995-3ac3-9d4a-fe7172d47461 | -16.8048 | -57.4197 | 2024-10-08 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 80cafafc-f509-31f8-b6b8-909f77357ba2 | -16.8045 | -57.4402 | 2024-10-08 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| b660f4ab-5789-31a0-9d45-ddab86cbc194 | -17.1274 | -56.828 | 2024-10-08 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 9a619940-e31a-3186-a408-0eb1b7d7a395 | -17.1175 | -57.4449 | 2024-10-08 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.2 |
| ef9c488e-5323-3d0a-91c6-85cf8ccc47c4 | -17.1078 | -56.8304 | 2024-10-08 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 02c67adb-e553-3e85-a114-d3b81425c5ea | -17.1074 | -56.851 | 2024-10-08 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 03f27935-0d90-3a92-920b-638dfda790ea | -17.0992 | -57.3651 | 2024-10-08 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 7f0a868e-e855-3705-81a1-a01e4d651798 | -17.0982 | -57.4267 | 2024-10-08 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 950a5853-6ffb-32ce-aa25-48c7d8a55f73 | -17.0881 | -56.8328 | 2024-10-08 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.7 |
| efb92bd8-6f09-35fc-a46d-c490793ff8aa | -16.9407 | -57.4859 | 2024-10-08 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 9be71846-52c8-3e66-8ff7-ab4aaf9a72a6 | -17.1178 | -57.4244 | 2024-10-08 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 6f1470a3-5c66-3316-97b7-e397a7696e61 | -17.1375 | -57.4221 | 2024-10-08 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| f81befc8-8fd2-3e8a-8784-eaad67dae6ed | -18.6195 | -57.2396 | 2024-10-08 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| e3f196f0-f8d3-3b1d-b5c2-0681ab3d9409 | -18.6192 | -57.2603 | 2024-10-08 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 9594b7e2-f49c-30b8-bb61-3e4dfc3fe654 | -20.4144 | -43.9356 | 2024-10-08 03:16:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.1 |
| 1056711c-97f1-3a6d-9744-f40c5ab9abc3 | -20.3946 | -43.9163 | 2024-10-08 03:16:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 6a69e7e1-f399-341d-bdeb-3bffb1de7648 | -20.3938 | -43.9412 | 2024-10-08 03:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 173.1 |
| 6b586ef2-a02e-37c2-b811-6b5a82c47a0a | -14.78383 | -42.84361 | 2024-10-08 03:17:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 011db2da-39f7-388a-8e46-7cba2e1291ef | -14.53431 | -43.22262 | 2024-10-08 03:17:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85566547-7215-37f3-93af-31ebe37a0bf5 | -13.5194 | -44.40429 | 2024-10-08 03:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13ca58ee-837c-3922-a84a-e03cf27a1c27 | -13.41835 | -43.79727 | 2024-10-08 03:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 630c2b5f-7e96-374d-ae70-a8daea185caf | -13.41698 | -43.80364 | 2024-10-08 03:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ea26c11-42a2-395e-b0b6-49ab09b31330 | -13.37487 | -43.76761 | 2024-10-08 03:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5bc0b4ee-3fcc-3ee0-bb4b-43c746e282e3 | -13.37435 | -43.76725 | 2024-10-08 03:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe32294f-c1a1-3571-a159-0038ad6ea4ea | -13.373 | -43.77362 | 2024-10-08 03:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91a60375-8af3-32d4-bd2d-bf498a91329a | -14.11656 | -44.10102 | 2024-10-08 03:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e88e42a8-14d4-30f4-b367-bc756ee8a29b | -14.10974 | -44.09938 | 2024-10-08 03:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a71a2427-4f7c-36c2-92aa-89b3ba9ab535 | -13.95731 | -44.62628 | 2024-10-08 03:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cad538d-ca6e-353a-aacc-caaf3b2a84f7 | -13.95418 | -44.62733 | 2024-10-08 03:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08f601d1-a444-3dfc-b00e-98b3e7ebae87 | -13.95193 | -44.61715 | 2024-10-08 03:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4180ea7-9c24-3a11-92a6-733444ed9a6b | -13.9488 | -44.61802 | 2024-10-08 03:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ca3d9529-7e40-3a3a-a0bf-fa71f0ed5df9 | -13.94498 | -44.6151 | 2024-10-08 03:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8abdceab-ab36-3262-accf-fc2fc48fd72a | -13.91915 | -44.63116 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f28a0a65-6d15-3b75-96a2-982cea59da27 | -13.91771 | -44.62479 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f469366-d67c-3f06-a5f5-968a517a0eda | -13.91685 | -44.5948 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c91874b-f027-3753-8dbb-8518e76bafb6 | -13.9138 | -44.62195 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27564adf-5c08-3095-b2de-95ec2df6877c | -13.9131 | -44.59216 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb40f776-e5b3-38d1-970a-9fe9f84c15ae | -13.91229 | -44.61567 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab8ddbb6-ecd3-3c6f-90e9-07ac2185774a | -13.91156 | -44.59898 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff1263e1-498a-3cc2-9e90-51598d1f9ff5 | -13.91072 | -44.62286 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ce8eb1f-b303-3421-88fb-642e9661a1a9 | -13.90839 | -44.59966 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3aec7536-cbc7-34f7-96de-3032c606f965 | -13.90533 | -44.61361 | 2024-10-08 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6096daa5-60eb-3099-9cf6-68091f7c6048 | -13.92311 | -44.63401 | 2024-10-08 03:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e02a27f-0792-30ae-b249-e35525170270 | -20.99723 | -43.0546 | 2024-10-08 03:19:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff3250a0-cd1a-3f77-b8d6-6d0841c5638a | -19.45225 | -44.11614 | 2024-10-08 03:19:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e743a0d-f618-3a8e-ad3e-3692c1be5ce9 | -19.45109 | -44.12116 | 2024-10-08 03:19:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3fac98b-a40b-39aa-a2ac-30d13ed60d80 | -19.82175 | -43.84172 | 2024-10-08 03:19:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 901afb8c-f097-31d6-a821-7d1037d5a7d7 | -19.82135 | -43.84459 | 2024-10-08 03:19:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2575f18d-5915-3628-b69d-d6957034cd26 | -19.82069 | -43.84629 | 2024-10-08 03:19:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c677e05-7fa6-3457-ba05-59b9670c4fc6 | -19.82022 | -43.84965 | 2024-10-08 03:19:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3243fe6b-02b0-35e3-a42e-5cfe65fcb7c8 | -19.74565 | -44.28118 | 2024-10-08 03:19:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e46f60f2-0af7-341c-8575-19375243f989 | -19.74435 | -44.28677 | 2024-10-08 03:19:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1c43ad1c-d6c8-3b65-9ac9-2c5e125e0431 | -20.40612 | -43.93466 | 2024-10-08 03:19:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9131d529-a73d-3145-8a25-b401a858350b | -20.40444 | -43.94201 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 4f7820a3-d623-3cce-a29f-776a8a0a6ebc | -20.40302 | -43.94826 | 2024-10-08 03:19:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| ed98f5be-2969-33b0-84e4-3704bc80b373 | -20.40045 | -43.93156 | 2024-10-08 03:19:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |


[Clique aqui para ver as próximas entradas](README30.md)
