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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 031d08f1-d78c-3bb1-aab8-9befea7781b6 | -3.2343 | -50.5162 | 2025-11-17 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| bf3e52c2-616a-30ff-8f29-5b1b26fa1eb8 | -2.5053 | -47.812 | 2025-11-17 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 652b8f30-87d8-3cea-8152-31b53f6c2f07 | -6.6687 | -42.0314 | 2025-11-17 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| fb0a6ab7-f824-3354-9c29-d727eccfac63 | -6.6875 | -42.0296 | 2025-11-17 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| d06a977c-c34a-39e9-96b9-f0249199a7a4 | -3.2344 | -50.4952 | 2025-11-17 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| adaf3ad2-a0dc-306a-875c-d3ed6bf057fe | -3.776 | -49.2517 | 2025-11-17 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1d170806-d1df-3e7e-b777-6656839100e7 | -15.8365 | -42.6633 | 2025-11-17 02:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 382e017e-8620-36da-86b5-fb3092ce8ab7 | -6.6873 | -42.0535 | 2025-11-17 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| e03d8bc2-5c9c-3725-8670-7dbfde7bbf4d | -3.2344 | -50.4952 | 2025-11-17 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a51fb1da-7e01-3d56-8a6e-076cc10170e5 | -15.8359 | -42.6879 | 2025-11-17 02:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.5 |
| e50c86cc-4cfd-343d-9e77-7bd34995490d | -6.6687 | -42.0314 | 2025-11-17 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| c7036d64-548d-3190-8bf0-2b00eb144fcd | -11.7017 | -48.8692 | 2025-11-17 02:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| edfce43e-9e4d-3e06-ad8e-e101afef9291 | -6.6875 | -42.0296 | 2025-11-17 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 60c74de2-61e6-32dd-893e-e707fea50981 | -15.8365 | -42.6633 | 2025-11-17 02:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| a43d0451-c878-387c-bf0b-e5257b42e2c1 | -11.8486 | -49.2218 | 2025-11-17 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 12ff58f1-a58a-3814-aa3d-807ebb1159d2 | -12.8611 | -46.0279 | 2025-11-17 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| addbe2a3-8671-3ccd-8138-74edcd969d2e | -2.5053 | -47.812 | 2025-11-17 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| df4e0cf6-bfe1-31e7-b83c-5a2800965224 | -3.2343 | -50.5162 | 2025-11-17 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 119b1ef9-ece8-3af1-b730-59362fc108f2 | -4.8995 | -44.8686 | 2025-11-17 02:30:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 19c2e399-3725-3964-9eb3-2bcd68189fac | -2.5238 | -47.8115 | 2025-11-17 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7a49f8d3-f4e9-3bc2-b142-ca248c9aa1c7 | -15.8359 | -42.6879 | 2025-11-17 02:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 0164a726-1de7-3110-a218-ddec959956ff | -2.5053 | -47.812 | 2025-11-17 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1339fd82-826d-372d-a746-48564e2df40e | -2.5238 | -47.8332 | 2025-11-17 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ec8a51ed-a073-3b05-bc42-02e8cb5b9242 | -12.8804 | -46.0249 | 2025-11-17 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| a8efee43-7803-3473-ad49-6db95f21faa4 | -6.6875 | -42.0296 | 2025-11-17 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 4579ea66-f431-3d8b-afb5-953be5c1ac5f | -11.8486 | -49.2218 | 2025-11-17 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 377b482d-8d89-395f-af08-56a7df4b09b2 | -3.2343 | -50.5162 | 2025-11-17 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 88fac326-a605-3672-8345-aab0c8c310cb | -3.2344 | -50.4952 | 2025-11-17 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ff2189d7-f1ca-3f3b-810e-0084a09b1171 | -2.5238 | -47.8115 | 2025-11-17 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d4453631-cf77-3c6a-a433-57f90e83a1df | -6.6873 | -42.0535 | 2025-11-17 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 84acfec8-f4b9-395f-907d-60e93c5e3be2 | -12.8611 | -46.0279 | 2025-11-17 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d50f0910-e493-30e9-9248-4b7c08f59f17 | -6.6687 | -42.0314 | 2025-11-17 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| ca5e9eee-f00b-302a-8a7c-b677bda2492c | -11.8486 | -49.2218 | 2025-11-17 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 78bc8e04-e65e-31da-88fd-46c42ae2c134 | -2.5238 | -47.8115 | 2025-11-17 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0cfc2642-568c-388f-a230-c098cc7f1a15 | -2.5053 | -47.812 | 2025-11-17 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 90dc4669-99e8-3f44-8f40-5087c52340b2 | -3.2344 | -50.4952 | 2025-11-17 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8645e7da-83c6-36df-ae44-f39804536350 | -3.2343 | -50.5162 | 2025-11-17 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 46947875-ad13-3d7f-bc87-4e5d031432c6 | -6.6875 | -42.0296 | 2025-11-17 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 97d78efe-39dd-3076-b693-ca4b05d77bdb | -2.5238 | -47.8332 | 2025-11-17 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 37e19728-8764-38e3-a25e-332e2466b27d | -6.6687 | -42.0314 | 2025-11-17 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 64fd4f4e-b5d3-318e-9327-b9fc90404b91 | -6.6873 | -42.0535 | 2025-11-17 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 3b09ab24-98f2-383d-b095-89c6741a9107 | -10.00888 | -36.06003 | 2025-11-17 02:57:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 041b5378-c1dc-3201-87ac-940dda5c56fd | -10.00287 | -36.0588 | 2025-11-17 02:57:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ba702135-8532-30a8-8f49-c699d2df25c2 | -2.5238 | -47.8115 | 2025-11-17 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d0483292-bcb3-3b78-9242-a03b4a321774 | -3.2344 | -50.4952 | 2025-11-17 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d6bf170e-0338-310e-8ef3-bbc3851b89ae | -11.8486 | -49.2218 | 2025-11-17 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 24f3b132-67bd-35e3-b04b-69b87203d250 | -2.5053 | -47.812 | 2025-11-17 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c70c75f8-eaa9-3cfb-ab4b-e1940a050a1f | -6.6875 | -42.0296 | 2025-11-17 03:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 8b3eae34-58b8-3eb2-8311-b7fecdf38cc1 | -6.6687 | -42.0314 | 2025-11-17 03:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| cfcac6d3-29d5-3ebc-b795-9943fd706dd6 | -6.6873 | -42.0535 | 2025-11-17 03:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 2fba3c06-0943-3cbb-a95b-da6958361b96 | -6.6873 | -42.0535 | 2025-11-17 03:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 4561d344-4074-3003-bc41-ae67af3adb2e | -11.8486 | -49.2218 | 2025-11-17 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 41614df6-59e1-38fa-8fb5-c8e140bc7e64 | -3.2343 | -50.5162 | 2025-11-17 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6a263fc7-20c9-3459-b5a1-0e3e4aac89d2 | -3.2344 | -50.4952 | 2025-11-17 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b1ed842d-7a2d-3b49-847d-7d2b6754bea5 | -2.5053 | -47.812 | 2025-11-17 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0ab38420-7b06-3d3f-8212-fedff4323b2e | -6.6875 | -42.0296 | 2025-11-17 03:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| ae6cf93d-eff8-3fe3-bac4-b6ab8d5460a2 | -2.5238 | -47.8115 | 2025-11-17 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7beaf47a-00bc-3431-af57-7efd09749af1 | -5.0401 | -43.5973 | 2025-11-17 03:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a094e36c-f71e-3f30-a860-fbe839300a5e | -3.2344 | -50.4952 | 2025-11-17 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 3dcb2301-ea53-37fd-8b27-b3931a639433 | -6.6873 | -42.0535 | 2025-11-17 03:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 5797eabf-1923-3ef7-8fc7-dc1fa2fada2f | -6.6875 | -42.0296 | 2025-11-17 03:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 41b27140-33d5-3159-8e46-62abc030ba33 | -2.5053 | -47.812 | 2025-11-17 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 115d818e-eb5c-3f92-b323-27ab1a915e3e | -2.5238 | -47.8115 | 2025-11-17 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f1fc0060-20a9-3cba-aff4-966c8bbc69db | -6.48519 | -39.76826 | 2025-11-17 03:25:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f77c48e5-3fda-3f50-a069-4169339b515e | -5.3256 | -43.04693 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d3639c2e-192c-3739-9bc1-d3d82d09bde2 | -3.5896 | -43.59995 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db0cc3cc-2979-3a31-8628-b1a21740cdf7 | -5.41611 | -41.02797 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0722da92-cad9-3aac-aea8-d6bf07d37577 | -4.31695 | -38.49153 | 2025-11-17 03:25:00 | NPP-375D | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a922200e-f852-34eb-8091-70a36d2c2703 | -4.14189 | -38.35102 | 2025-11-17 03:25:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d98311c-18e2-39e6-ab53-56212fdf94e8 | -5.03837 | -43.61019 | 2025-11-17 03:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ea56d4dc-8fce-3f63-ac4f-eec3ba907c8c | -5.49479 | -39.16717 | 2025-11-17 03:25:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45424e36-34dc-3c6a-a291-a5304b2f3845 | -5.04537 | -43.61145 | 2025-11-17 03:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7c9c4a68-3a42-3c01-b9ed-90ca3a92b7d7 | -5.3309 | -43.04861 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 82cd94cb-5f72-3e0c-a755-3b73e5dbc5f7 | -3.5927 | -43.60797 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31970716-a49a-3082-910a-f6b7e46a0474 | -5.333 | -43.03674 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da88b6fb-778a-37ec-aac1-4b7055bf6372 | -3.35388 | -43.49862 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d70df8e-65b4-3b24-a7a9-ecb6c75dbc2b | -4.13677 | -38.35019 | 2025-11-17 03:25:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ac5a3ea-6225-366b-870a-f3015f77aae9 | -3.22044 | -43.35975 | 2025-11-17 03:25:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91439846-2aba-3817-a889-3fd940916177 | -5.4761 | -40.96556 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04acad33-31fe-3f03-b4bd-f236e6345fe7 | -3.34793 | -43.4904 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bd452d12-b8f8-3d68-aae1-15aae9bb7450 | -3.34679 | -43.4971 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bb510f43-148e-32a5-ab9b-50e35ab3ddf8 | -6.12923 | -41.82234 | 2025-11-17 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4375d9fb-0451-32bc-9487-2cb7dccd0add | -5.32666 | -43.04116 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d507e674-5f40-38d5-b364-ed757e3aef89 | -5.97747 | -37.83258 | 2025-11-17 03:25:00 | NPP-375D | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e7e34e95-4b34-3291-bea3-c2fb10608825 | -5.33339 | -43.04251 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bc51c98b-c89d-3224-b6ac-af497b14f634 | -4.19999 | -40.68213 | 2025-11-17 03:25:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb40d88f-b3fc-3ccf-b2da-b421eda18b17 | -5.33972 | -43.03811 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5901c9d2-9f47-3484-85b4-1aa135abcd15 | -5.32522 | -43.04131 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 24d4368b-fbb9-315a-8382-6acb334df99b | -5.46516 | -40.97277 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d0aadcc-3894-36d2-b27c-ad65eff44f45 | -5.33409 | -43.03057 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 080307d8-2f54-387c-b70a-1adf8e4892f9 | -6.13012 | -41.81739 | 2025-11-17 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a7f1664f-692a-341b-882e-1e4687e94ed7 | -3.21926 | -43.36659 | 2025-11-17 03:25:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb233a7b-6663-3c1f-9035-3292f801ea60 | -5.03135 | -43.60901 | 2025-11-17 03:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 856f911e-e311-32cd-ad5e-913769b8c030 | -3.61126 | -42.41877 | 2025-11-17 03:25:00 | NPP-375D | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 449df302-7869-31d4-ad37-cff4b570196d | -6.49056 | -39.76938 | 2025-11-17 03:25:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 533ac9ed-ebdc-3c41-839d-fc64259d1b1a | -5.33195 | -43.04266 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e733a66-9767-3f0f-8d70-6c3b78c1415a | -3.59671 | -43.60145 | 2025-11-17 03:25:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92b4a06a-ec1d-3017-a755-93984199dcad | -5.3242 | -43.04708 | 2025-11-17 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7a40e952-3e7e-3042-b616-a2068b7a7959 | -5.4788 | -40.9651 | 2025-11-17 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d580171e-37c1-3815-86ee-4e0b86864fc5 | -3.60822 | -42.41712 | 2025-11-17 03:25:00 | NPP-375D | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
