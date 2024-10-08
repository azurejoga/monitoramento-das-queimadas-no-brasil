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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3087c813-8154-3c0e-81ed-144a6d4efad9 | -20.78399 | -54.83745 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bff2c70-4e22-372f-988c-4185ddb3a9fd | -20.78349 | -54.83945 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0684018-1988-37a7-841c-00d142968f51 | -20.78315 | -54.84208 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a482698-e6fa-3c18-9caa-446e645c23aa | -20.77703 | -54.83341 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e89d2771-bde7-3963-9a81-4f3588f5db1f | -20.77666 | -54.81414 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d39b221b-a01f-3911-8229-941017bc5628 | -20.77622 | -54.83801 | 2024-10-08 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 539f7a83-dd74-3d92-a140-24896acbb01c | -20.07988 | -54.51945 | 2024-10-08 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a3ad053-9ea3-3153-8824-ea395354cde4 | -20.07965 | -54.5165 | 2024-10-08 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ebf0aa8-a2cf-3edc-a139-21ecd606bb3a | -20.07546 | -54.52325 | 2024-10-08 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9c08598-66dd-3458-bcc4-4f006640c15c | -20.07446 | -54.52483 | 2024-10-08 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6bd303a-4d57-307a-81b5-51d257b6b087 | -21.39491 | -55.67902 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e59d15b-45e8-3521-b743-215f4af84975 | -21.39463 | -55.68078 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96b23f38-13c4-333e-b6ef-133af7ad36de | -21.39398 | -55.68395 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7ade01de-f537-3418-b9f6-157d2673a235 | -21.39373 | -55.68573 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e0ef9f7-7cb2-3edb-aacd-8d7bfabe1a9d | -21.39113 | -55.67831 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c363a32e-3895-3f9c-b25f-d3db19b0a92f | -21.39085 | -55.68005 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab05c548-60c8-3cab-93b3-8116fd8950d6 | -21.39022 | -55.68319 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 91181902-5fe9-35a2-9be1-14129f64db64 | -21.38997 | -55.68493 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22067f2c-a407-3be3-b02d-9b2e452bedaa | -21.36379 | -55.70008 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c689ade9-b558-3b00-9f85-1452c636e027 | -21.36096 | -55.69413 | 2024-10-08 04:38:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eecebd02-9630-3873-bf53-e9903ede044d | -21.35628 | -55.69839 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57f75905-289b-3624-b244-ffb011c71fde | -21.32995 | -55.69268 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d18cba0b-c226-314e-8c7c-03792a432031 | -21.32904 | -55.69764 | 2024-10-08 04:38:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 842b0591-7584-3414-9352-54df94b3d162 | -21.32527 | -55.69687 | 2024-10-08 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f038d16-5f8a-3b52-8374-c885882b2bba | -21.34694 | -54.61296 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 773e1985-b2ad-371b-880b-2531991bdd94 | -21.34232 | -54.63929 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d27add52-685c-3a92-ad52-2372bb377d31 | -21.34155 | -54.64368 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd888579-e9bb-369b-907f-e683dbedc8f7 | -21.34078 | -54.64809 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e28636a-ad57-3bf5-9638-ed027a0b107f | -21.33875 | -54.63855 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 549e3703-dde7-3feb-b4ba-6f54d14c1792 | -21.33798 | -54.64294 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44cbed3c-41dd-30db-a0b8-a44a8f7568de | -21.33721 | -54.64735 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79dfb94a-9fa0-3d6b-80a6-699cd9ff4c02 | -21.3344 | -54.64222 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c927758-62ca-39e3-acac-170b199cf550 | -23.72057 | -55.25465 | 2024-10-08 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bbca165c-2a35-3eed-bdd8-60e8e034bb52 | -23.72137 | -55.25019 | 2024-10-08 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| be2a2447-e771-3abb-9ed5-bd7482ea198d | -23.24294 | -55.47925 | 2024-10-08 04:38:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4651021a-ea92-331c-9e86-c885286dd844 | -23.23122 | -55.48161 | 2024-10-08 04:38:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0e142a97-8d38-3522-8c6f-b9030e3268a5 | -22.72906 | -55.27679 | 2024-10-08 04:38:00 | NOAA-21 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d5a89ee1-421b-3aba-8f23-8a40964e716b | -18.63539 | -57.29516 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6155274a-31c2-353e-a699-85208369acd5 | -19.70981 | -56.48762 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e8a71ca9-fc93-3482-97df-431fdf811853 | -19.66669 | -56.47075 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 16fb1c34-63a3-3582-b0b0-4158f5a2727f | -19.66264 | -56.4699 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 22812892-0a72-39d3-b0aa-945b4a88ab1b | -19.66192 | -56.47369 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 611c9d13-4920-3d6f-86cc-ce084ab1df68 | -19.66002 | -56.46148 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 374c4d37-428f-3c9d-a3f0-3a2016bea568 | -19.65275 | -56.5671 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 60f9a562-e920-3330-853b-db513371ea18 | -19.6494 | -56.5624 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aaf1c49d-52f5-3988-8b11-92e2bc88dee8 | -19.64868 | -56.56625 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c66fcf73-c5a4-3633-88e4-745f7b9280d0 | -19.64533 | -56.56156 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e0725f5e-4033-3775-94ef-ad3b2d543ea8 | -19.64473 | -56.49781 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7bdf065c-e56b-3e2b-98db-bde9b6b77c02 | -19.64139 | -56.49315 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6cd44160-8865-3181-8299-584fd3d846ec | -19.59193 | -56.53411 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b41f939f-32c1-3387-b2e7-1d1d12885ef9 | -19.58786 | -56.53326 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 92742d5d-25cf-319f-9967-a1fbb25fc519 | -19.58379 | -56.53241 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bf1300c3-d949-3b95-835f-63beb04de745 | -19.57972 | -56.53157 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 15a87138-659e-3150-bec0-b04082e65f16 | -20.27767 | -56.93335 | 2024-10-08 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f31f5559-3ec1-3aae-8a63-fbde36f87c7e | -21.43214 | -57.23022 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb733085-31b4-3556-9e30-4d024e78efcc | -21.43196 | -57.2222 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 703f79b5-76f6-32ee-8003-f187622cb30b | -21.43134 | -57.23445 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d2d7faf-575d-3542-8e82-7572ddffd7ab | -21.43118 | -57.24792 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebaecc20-0e62-3fab-9ad9-f126782ac055 | -21.43044 | -57.22991 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 48b699d1-76c4-39ef-8c7d-e8a766f4fbaa | -21.43039 | -57.25191 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1ebaf04e-0038-38b0-b095-c12fd457edaa | -21.42973 | -57.24298 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68337510-384c-39c8-aeca-e0e66b12866f | -21.42962 | -57.23408 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 83a9a0dd-bd6b-3af5-b1a3-a1c9687ca308 | -21.42952 | -57.22151 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f7adbaa-237c-3bd4-b204-8bb15a2dfa54 | -21.42894 | -57.24716 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62aeb474-a5d3-3f7d-8a5d-19ce3a1c0d0a | -21.42808 | -57.22909 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d056a99f-fb01-3097-ad0e-424ee5828076 | -21.42795 | -57.24253 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 094c8401-1aae-35b9-b06f-a6f1e3eb1105 | -21.42729 | -57.23324 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f6416aa-c637-3c68-a786-b16caea383e2 | -21.42611 | -57.21693 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa6c8789-1d93-32e5-8a57-839be9e868c0 | -21.4176 | -57.26177 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ec9c6520-5360-3be6-afb8-a0dcf9515f72 | -21.41431 | -57.2565 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 00de5d7f-088c-37ed-8ca8-04631d5cab19 | -21.40865 | -57.26375 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1f8c9211-cc9a-31af-bc72-ce43b01efd14 | -21.40459 | -57.26255 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| feecb705-0fd9-3976-bdb1-8ffb0be2d535 | -21.40058 | -57.26107 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c474272d-3bc6-3212-bde4-e0cd7f932c10 | -21.39646 | -57.23781 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1733140-d35e-3a92-afcb-c9bb7af62971 | -21.39415 | -57.24986 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e56a05fa-b269-3e43-906f-691208adbe8e | -21.39338 | -57.2539 | 2024-10-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c134399-0228-3d06-9d57-bbd3e37efe9a | -18.6351 | -57.22671 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d8234fea-6286-3229-a889-2d57d4a3e761 | -18.63426 | -57.23107 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79b15079-b83b-3d8d-b8b9-f042bf7ccbed | -18.7257 | -57.27607 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 25b1886c-33ea-3266-8067-1c94c1771bed | -18.72485 | -57.28044 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ef39f820-d386-3a5a-9d54-780645a4a352 | -18.724 | -57.28482 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fbc65cbc-928d-3597-a4a5-03e6b83730f4 | -18.72138 | -57.27515 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4ef1d152-1ddd-3ea9-859b-707b8c8faef3 | -18.72053 | -57.27952 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c11203fd-53b4-32a3-aeb5-ef46362107b2 | -18.71967 | -57.2839 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| df392980-f0ef-3b5e-9916-023a0e87f5b1 | -18.71705 | -57.27425 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a6834334-b901-32ce-a3a1-ed8daa8fa462 | -18.71534 | -57.28299 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 838f9cef-dc03-31d0-9fdd-e7e085d2de14 | -18.63942 | -57.22761 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 651c2ae1-ddd0-32c9-84d8-0ea0308f49c0 | -18.63858 | -57.23197 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ed0ca1fa-bbe4-3396-97d6-f375670f1860 | -18.63624 | -57.29077 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 57e8175f-1c64-3480-8a01-19c21704d6f2 | -18.62824 | -57.2389 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 81a4f270-47b3-34be-85d8-bdbd7342e811 | -18.62739 | -57.24326 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 493bfad7-2d85-3019-a844-a9574cb959c1 | -18.61704 | -57.25019 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3be1e8c6-e38f-3890-8472-450af0655e67 | -18.61448 | -57.26334 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c3f12be8-df97-3e0e-a11d-99092db4365c | -18.61271 | -57.24929 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2679eac9-10ab-3d99-ab79-5ab3845e2eba | -18.61186 | -57.25367 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| cb26c557-d187-398f-bd2a-0cde76b382b4 | -18.61101 | -57.25805 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 2cd9b793-7bf1-3037-9bf0-72212da2c1bc | -18.61015 | -57.26243 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 6efd6b96-abc0-3571-8499-ca156e2f8a13 | -18.60838 | -57.24838 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2e680ccf-60d3-301a-92e9-b5bb6e1954f2 | -18.60753 | -57.25276 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 21e44659-4cea-37e6-9225-d50fe236fd3b | -18.60667 | -57.25714 | 2024-10-08 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |


[Clique aqui para ver as próximas entradas](README78.md)
