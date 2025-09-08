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
| 14be0856-b5a1-3ca7-94b1-042db55e5661 | -13.91354 | -53.96828 | 2025-09-08 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f5fb5baf-6dbd-3b2e-ba67-5c9411ac802b | -9.9844 | -51.68472 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4e72acad-5c9a-3b3a-acf6-45891af8d254 | -11.34621 | -50.38032 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| e0ca945e-8565-3c88-bc4f-1bc3b0195e59 | -13.83832 | -46.29033 | 2025-09-08 00:50:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0aa52105-61eb-3965-acef-31e18eb83d12 | -11.37805 | -50.4054 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3698e591-946e-33ee-be53-298d944b3427 | -15.75522 | -56.43222 | 2025-09-08 00:50:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 047c279f-4a2b-3bb8-b06e-5764816c6b72 | -11.21999 | -55.01057 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9173ead6-3214-380b-850d-4d8282bae7b8 | -11.3554 | -50.37891 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ecbdd854-23cf-3ab7-b0e8-1ec7af95de37 | -16.33327 | -52.93238 | 2025-09-08 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c408157f-dc58-3400-b1f0-f95e97313a87 | -12.52694 | -53.84158 | 2025-09-08 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c5edd4b-aa49-39e3-bc6a-be7c6ce076e5 | -11.41057 | -50.37047 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| accbd76a-1f0d-3234-b0a9-87753a6a10c7 | -11.27626 | -46.44187 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0afbddef-4a06-3fb7-bf31-421f9465337e | -11.19923 | -55.00237 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 0ac0aded-9f69-3850-b9d0-fc88d4ef63b6 | -9.68485 | -51.07184 | 2025-09-08 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3347166b-ffa5-3d42-8e6e-ee533c8dd4f3 | -13.00706 | -45.21552 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b4711589-196d-3bda-b000-70ab88b55887 | -9.99456 | -51.69241 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d61660b7-219f-3642-8ba0-f014c7dabee1 | -11.28381 | -46.44721 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 8870d6a5-28b3-3ec8-bc4f-cb86a5340e22 | -11.10615 | -52.0672 | 2025-09-08 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 226aafb4-4778-3a75-b8a5-40d00f3245f0 | -11.40916 | -50.36068 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 26188514-f1ff-3e34-8d5c-01fff69e2f6d | -9.84701 | -48.85706 | 2025-09-08 00:50:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0a66618c-0b4e-3312-b537-33ffbe26e5f1 | -10.51053 | -57.78897 | 2025-09-08 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7f6d00f1-09a1-3734-91f8-093f3ccef13a | -12.20303 | -53.90469 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6f615779-d8e8-39c5-8007-c5d7273aa310 | -11.85966 | -51.06209 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3cfaa205-3673-3d55-ba3f-6d03a357e183 | -11.28657 | -46.46486 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 18cb024d-8328-3263-98f5-f33c01d307e6 | -11.10491 | -52.05826 | 2025-09-08 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b46396a7-9414-3faf-b2d9-9ddcf5f6226e | -12.19508 | -53.91576 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 8fe1d8f9-b8af-3fac-b847-44075721a8ec | -15.16494 | -47.96946 | 2025-09-08 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| af5c37dd-f129-395f-9bd3-1d20d4a63a8e | -10.0021 | -51.61714 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| db1648a0-ffc8-3dab-acfd-e899dfbbf9ed | -19.45276 | -47.88997 | 2025-09-08 00:50:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6d45b69a-e433-3ea8-ac44-84ec67c3b509 | -11.86097 | -51.07132 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a2ebde74-99ad-3066-9380-fc5fc2b08a0e | -9.99329 | -51.68344 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ecf1bec4-0caf-3f05-ab60-4d251934d322 | -14.48001 | -48.79215 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 57dc22b3-3b29-33df-978e-d79f9a1b641f | -14.8808 | -55.81357 | 2025-09-08 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| e45ad3a2-d354-3526-b124-2cc4cc6c4c0f | -13.64617 | -43.79189 | 2025-09-08 00:50:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 2a5ccb89-583a-3a42-a9d3-72cd8e71dbc9 | -15.83016 | -52.26054 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9c15dba9-3c8b-3060-bcde-ab9d7ccba1f1 | -14.5105 | -48.79844 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 436e1032-7aac-3063-8ab4-d658ccd1cd9f | -13.32384 | -51.70713 | 2025-09-08 00:50:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 86ecbf2b-c1aa-3995-9de4-f3a4cfbc842d | -12.95245 | -54.81193 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 88f5f60a-e08d-340f-80d2-5114c36ff214 | -12.16503 | -43.93005 | 2025-09-08 00:50:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| bdc5746f-99f8-35e2-b589-c8b279bfc837 | -16.4443 | -49.29092 | 2025-09-08 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2f55af1-296f-368e-b411-b9a38f49c8e4 | -12.16955 | -43.95719 | 2025-09-08 00:50:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c0b5c21f-561d-3129-83f5-a49ff83cc1d8 | -9.99203 | -51.67447 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b6b32ca2-ff3b-3159-9d3f-207ad5f2d338 | -9.03496 | -49.79274 | 2025-09-08 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2121380c-4ca7-3c67-a9a8-c5b69f9d23b1 | -9.98945 | -51.6562 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dc0e72f8-868a-3770-b21e-ca673c0e4113 | -15.08346 | -50.07312 | 2025-09-08 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d4602a36-57b5-3a87-af61-155bfd4fdf3f | -12.41635 | -47.50403 | 2025-09-08 00:50:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ef5e136f-0a38-3dfa-9d2b-c2950c130125 | -11.12632 | -48.38354 | 2025-09-08 00:50:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 7b13dc37-876f-306f-837a-45c2f87bdfe8 | -12.94368 | -54.7622 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8756d1b4-de73-3e61-b2ce-8e910aa2037f | -14.98882 | -48.02428 | 2025-09-08 00:50:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 19202bb0-01f9-37ec-9213-3d9748c1346b | -10.82572 | -47.73199 | 2025-09-08 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6d6018d1-3416-37d3-bd9b-a531bd4cb713 | -12.83283 | -52.89538 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cf72db41-12f9-38c1-9dce-bc1a44a0dc29 | -15.74858 | -53.53362 | 2025-09-08 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e915a0b-3ca0-3846-91d2-cc043990d730 | -18.58137 | -48.70834 | 2025-09-08 00:50:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5c4ccf51-1f82-314d-8b8b-2fdddd563742 | -9.20981 | -46.04476 | 2025-09-08 00:50:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1e3c2f99-3e9d-3a89-bcfd-0c8a04440fb1 | -13.69577 | -45.48164 | 2025-09-08 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e7e87cf8-19e7-3916-8441-666ae9a956f9 | -12.94965 | -54.78953 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1d577f90-c449-3f20-b59c-06f8f603a6e2 | -9.99834 | -51.65486 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5989a705-a247-30ef-8b33-dcbf65afe294 | -16.28557 | -45.67776 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a4981740-3683-3278-a5dc-086774f3e354 | -16.58418 | -49.23093 | 2025-09-08 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f5d8f485-b5f2-38e9-a93f-43290b422f1f | -11.76962 | -50.62611 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c8343fec-1daa-38c9-b675-997742d6872c | -16.2883 | -45.69424 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 35a0e055-a627-340e-bac0-8be12c2c3988 | -11.02196 | -46.0335 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 21d43ecb-b632-3ac7-b28b-c81afad04fdc | -15.51295 | -52.77626 | 2025-09-08 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f62e1545-5e08-39e6-afd2-2fb24ae123a2 | -13.03589 | -47.1228 | 2025-09-08 00:50:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3a00d852-74d3-3b13-9a59-17ac59695e03 | -11.37028 | -50.41654 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 75922136-74dd-3946-b5bb-c4bf68dba415 | -8.85365 | -48.09312 | 2025-09-08 00:50:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7fbffbdd-c450-38c4-90c2-e926b9001e23 | -11.12896 | -48.37652 | 2025-09-08 00:50:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9c7dca8d-20ca-31b0-9c0f-acd96ba71a0d | -12.1938 | -53.90591 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2dc92f0d-a4ff-3631-8b15-1d0405bceb4f | -12.82345 | -47.9995 | 2025-09-08 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81c9134f-0209-35de-8b6c-0967d75c4fef | -12.60754 | -56.97424 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 3a280682-ef83-3158-b7ef-f715629ea40c | -14.8066 | -48.23725 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 67249617-27f4-3891-82d6-c78ad863b947 | -11.39871 | -43.55982 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 69bde8f4-b32e-3963-a03e-26c3e577c7ba | -9.99074 | -51.66534 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 3a61ff76-9b9e-30ce-b434-61bf9d1ec57a | -15.85064 | -52.2705 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1a94d3d-d7f6-3756-ae26-b2fc3c9064e1 | -11.61065 | -47.14664 | 2025-09-08 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c2edf151-2723-3f81-8eee-e21c70c0ee9d | -15.53322 | -49.24242 | 2025-09-08 00:50:00 | TERRA_M-M | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 445d7e48-8076-3700-8172-8a3b5023660b | -18.96236 | -46.80423 | 2025-09-08 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2ee45745-fb3f-3f15-8fbd-ad6d37cef119 | -14.72302 | -55.93141 | 2025-09-08 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cfcf0cdd-2876-3bce-8fde-ca1511e4674f | -9.99577 | -51.63663 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0d3a1b21-b7c0-3dd2-912c-20a7616bbed4 | -17.53817 | -43.74744 | 2025-09-08 00:50:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c553e612-151c-3b68-bd04-4b31f3473279 | -18.24491 | -46.6297 | 2025-09-08 00:50:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2183ee05-17da-381f-9a5e-7aca2aa639ed | -14.52915 | -53.97875 | 2025-09-08 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ef6a1b34-a65c-3cf1-b50c-170903e4f55c | -13.83683 | -46.30047 | 2025-09-08 00:50:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7b50f268-d78a-3ead-9642-41b1aed968b5 | -15.83145 | -52.27002 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e5997121-7a18-3467-8dee-6ee75ad43e55 | -15.25193 | -53.80934 | 2025-09-08 00:50:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 89f6e211-5cbb-305e-9bbf-e5aaeb232a6e | -10.81684 | -47.74743 | 2025-09-08 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| d932902d-bd5b-34b0-83ef-dce408650d30 | -15.1668 | -47.98145 | 2025-09-08 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1132df65-45cf-35c8-b75a-34a008982160 | -11.00408 | -52.06102 | 2025-09-08 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6a2038cb-58ab-36f9-a1f0-a28d1d387204 | -9.98313 | -51.67576 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a39757dd-1a0c-394a-85ae-31722411e909 | -17.8385 | -44.25529 | 2025-09-08 00:50:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4dd296a5-817d-3294-a5eb-956ea8c4229b | -16.06439 | -50.48085 | 2025-09-08 00:50:00 | TERRA_M-M | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3d7a6018-7641-3202-9bfe-f91a969cb2e7 | -12.94686 | -54.76728 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| ba8e72d9-066a-33f2-aba0-632aa24e0227 | -12.54062 | -49.10895 | 2025-09-08 00:50:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d043deb7-f3f6-33b5-a435-fa13f69495e3 | -12.83906 | -52.94162 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b9d690a8-1ffa-32df-a15a-83a5109a7af5 | -14.5121 | -48.80923 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 239efa1f-7874-3670-bcb7-4618b2e05f33 | -16.34375 | -52.94098 | 2025-09-08 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bcee3e03-cd8c-30d5-bd11-db303ff7f6c6 | -15.7499 | -53.54398 | 2025-09-08 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d14e9c93-c746-38c2-8267-a8bb2b866d89 | -9.8977 | -53.79507 | 2025-09-08 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 27f59b60-3a23-33f6-ac94-415fe71465a1 | -12.95105 | -54.80073 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| eb0d3620-eeaf-3a08-8214-4b90a4f8f6d6 | -13.6719 | -44.22828 | 2025-09-08 00:50:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |


[Clique aqui para ver as próximas entradas](README11.md)
