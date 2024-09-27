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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcbf0c9e-6f8e-37f1-b5af-995c26df5f5d | -15.60723 | -56.96912 | 2024-09-27 01:22:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 287a7523-f3c9-33e9-95cc-622660e336d6 | -13.2326 | -45.65663 | 2024-09-27 01:22:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 32ba1301-be0e-30fc-aa96-602d5b2e117c | -18.3936 | -51.96872 | 2024-09-27 01:22:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c0ef72ca-04eb-395e-84b2-b7850cd9dcda | -16.84037 | -47.7197 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 722ee63f-4bfe-3c57-bce0-a043842cc3fe | -19.38759 | -42.58585 | 2024-09-27 01:22:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.0 |
| 71434545-1d03-3509-8daa-54d75344e7bd | -19.38013 | -42.58434 | 2024-09-27 01:22:00 | TERRA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.1 |
| 0eed7d3b-9605-32fa-b21d-8e88e0f5eb3b | -18.70936 | -42.12543 | 2024-09-27 01:22:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| 5d5d4fed-9c9f-3ce3-a7a1-b8e827cf62f3 | -18.70187 | -42.08813 | 2024-09-27 01:22:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| 658b4eec-6b7e-398e-9ef0-36e3a3e68e10 | -18.69819 | -42.0961 | 2024-09-27 01:22:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 179.3 |
| 9d4bd142-6104-325e-a63c-aed54bd813d0 | -19.62118 | -42.83701 | 2024-09-27 01:22:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| be99e463-e38d-34e4-b046-c1ebe18484a9 | -19.61534 | -42.83327 | 2024-09-27 01:22:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.8 |
| 91cc9acd-b348-3a18-8473-9a3c63f7d651 | -19.61455 | -42.80299 | 2024-09-27 01:22:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 6efa2888-504c-37c2-999a-687a82f3c883 | -19.60825 | -42.7983 | 2024-09-27 01:22:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 35499d2d-e192-3d18-a99b-e84ef688c01a | -20.15558 | -44.34081 | 2024-09-27 01:22:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.2 |
| 2c10f1c9-0a8d-36e2-ac86-c2f1207a59c4 | -13.43514 | -44.00904 | 2024-09-27 01:22:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b6178635-dd7b-3147-be03-c161986b7a37 | -13.42554 | -44.00532 | 2024-09-27 01:22:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5b79b3d7-066d-3e63-a85d-8abe27b2dd16 | -13.44139 | -44.04429 | 2024-09-27 01:22:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 01ce5c26-68c1-3785-83fe-417ece5d08a0 | -13.43204 | -44.04039 | 2024-09-27 01:22:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 79c3e9a4-db47-3987-9e4c-c1c7d3f079bb | -19.60631 | -45.88194 | 2024-09-27 01:22:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| de1b3c53-bcfa-3137-870c-a1904d4862eb | -19.58088 | -46.11717 | 2024-09-27 01:22:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3d68bf59-6b6d-3fc6-a66f-f60079ae310b | -14.71975 | -45.49122 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 9ba68426-6499-351f-afb0-a2abd94e68c5 | -14.71785 | -45.53793 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 0f25152b-b882-3da4-bbd7-6a95529a7db7 | -14.71323 | -45.51219 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 910.3 |
| 74cf86f2-edef-3323-9ac6-740e545614d9 | -14.70863 | -45.48665 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| fc4ffc42-cfd4-3295-8d19-461cbb3f0473 | -14.72418 | -45.51706 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 285.3 |
| f5e23a9c-bac8-349a-8af3-855c4ba993e8 | -14.71 | -45.51951 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 426.3 |
| 7f548508-be28-3424-a4b9-50b53d27562b | -14.70556 | -45.49375 | 2024-09-27 01:22:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 12b97816-9634-3981-9ad7-9af44e5e93bc | -17.2375 | -46.2922 | 2024-09-27 01:22:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2e7282c7-3ce7-3d3f-b6bf-5037cb668790 | -19.99204 | -47.16668 | 2024-09-27 01:22:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e8204c8a-44e6-39d2-97f2-9769909737cf | -19.98928 | -47.15065 | 2024-09-27 01:22:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e3192246-09b0-3623-94bb-11e0419ba969 | -19.97933 | -47.15948 | 2024-09-27 01:22:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 84e4463b-a89e-3cbe-97a1-27523ed88bb4 | -19.60282 | -46.98588 | 2024-09-27 01:22:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 07d1b79b-471b-3560-a37e-0d2900d41319 | -19.6 | -46.96954 | 2024-09-27 01:22:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 811137fb-25e9-3293-a1b8-8c7faf72a031 | -19.59137 | -46.98806 | 2024-09-27 01:22:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3a7b5fa5-a15a-34b7-b124-6362d84f3a68 | -19.54004 | -47.90118 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| cddfc8c8-4b4a-3e4f-a561-c064f16998a6 | -19.53764 | -47.88699 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| bf40ac62-111d-3691-8038-c59e3b9989b2 | -19.53489 | -47.894 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 929d42c7-de62-3d96-a479-abf59c0308f5 | -19.53259 | -47.87982 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| fddbbbd1-216e-354c-8fc2-b12e181b474b | -19.52417 | -47.89603 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d931e7dc-3f3b-3e01-a496-cd466901f748 | -19.52185 | -47.88182 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 95eafd19-6dd3-350b-8e21-0df74b79b901 | -19.5111 | -47.88381 | 2024-09-27 01:22:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| bd5c82db-5a69-38a9-aa11-9dcd42e4998f | -13.80774 | -48.13568 | 2024-09-27 01:22:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 34810e8d-62a7-3dd0-89f3-81aab3f0c294 | -16.51537 | -48.05013 | 2024-09-27 01:22:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a266a9dc-75e2-32c5-9aba-7d76f269b13c | -16.51694 | -48.06029 | 2024-09-27 01:22:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 00ada843-505e-3a97-a88b-04d1fdd40e46 | -17.15401 | -47.65723 | 2024-09-27 01:22:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 0ae3b2ac-f0fd-3a11-b75f-a3336063482f | -17.15132 | -47.6411 | 2024-09-27 01:22:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 829292a1-7cc8-3a57-b1d2-95bbf178c5a5 | -16.84827 | -47.76618 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| aaa9ba88-559f-3ae2-898a-a2d4cac1ebbb | -16.84061 | -47.70909 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9df5125b-d9d3-3dc5-a3fb-9b72ce851b12 | -16.83935 | -47.77345 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| bd1ab677-6390-34f2-9de6-ca02ea6116e4 | -16.83766 | -47.70378 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4a51cc80-97ed-304a-be8f-f28a1708aff4 | -16.83691 | -47.75852 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 3c294198-941d-32e9-a5cc-2c590a040472 | -16.83688 | -47.76824 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 36eaf6fc-9dcd-3802-adab-10384b276ecf | -16.83439 | -47.74315 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 6ee925a6-0684-32b7-8172-ae9f30ef8709 | -16.83433 | -47.75333 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 7dc38202-5a49-361d-8576-d518541aa563 | -16.83169 | -47.73787 | 2024-09-27 01:22:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| fa1ce725-dd1a-31d2-ab9c-c7d4790571d5 | -18.59321 | -48.99656 | 2024-09-27 01:22:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7b2bb60d-12bb-3a45-b869-d1971c5de3a9 | -18.59291 | -48.81034 | 2024-09-27 01:22:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 3956af6a-c4d5-37fd-80d4-865c0aa85a6e | -18.59126 | -48.98416 | 2024-09-27 01:22:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 086c243c-d080-3721-bc49-ea1d11a20bb0 | -15.14422 | -48.77237 | 2024-09-27 01:22:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7ede0ceb-1e36-34ce-a3c1-c038ed2cd8af | -16.32803 | -49.46114 | 2024-09-27 01:22:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 17b42834-5146-34e5-a12f-ca7681093350 | -16.32608 | -49.44886 | 2024-09-27 01:22:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 435348d7-cd51-35a9-b431-223a6656db24 | -16.36167 | -49.93415 | 2024-09-27 01:22:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ceec9845-e7b6-38a8-8716-29d9cd480d1b | -18.39762 | -49.31748 | 2024-09-27 01:22:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7a145371-d463-30e2-91d9-ec50a82eaded | -13.56939 | -50.71034 | 2024-09-27 01:22:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 774f0695-ffd0-3e17-a79f-a6bf0c65998b | -14.9287 | -51.46125 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d8dcf4f3-f6ee-3ecb-814d-e9a32887c7a6 | -14.90871 | -51.45421 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 579b89ca-13f8-3515-a9fe-c1c9bd6afd0f | -14.90054 | -51.52717 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0dfeb528-c34e-336c-97cf-5aeab7f108ff | -14.87316 | -51.47019 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 17fb939e-5c0a-352f-be53-664bd32d5396 | -14.8639 | -51.47168 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b3362222-f897-3355-8497-8757d98ee15a | -14.86212 | -51.52313 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a488ec14-a80c-30de-b9e8-62bf2cf460f8 | -14.85465 | -51.47317 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f20a373b-bff9-31d9-b582-88533e1a406e | -14.93017 | -51.47128 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7fc941f8-c360-3791-9c83-9d63976995cd | -14.91945 | -51.46275 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fb67929d-0046-3242-bd49-537e3e761d4c | -14.84539 | -51.47466 | 2024-09-27 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 145c1a55-41ea-3904-86a0-43955a8c3a1e | -15.87009 | -51.41518 | 2024-09-27 01:22:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f23cd39c-f528-3a12-8214-63ef5078a20d | -18.39494 | -51.97811 | 2024-09-27 01:22:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2ce13a40-1895-3958-a312-b490323bd5d3 | -16.12455 | -52.01569 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ba619cc6-9e69-332b-bdaa-903399e94e9b | -16.10525 | -51.94737 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 7c353fc5-b987-3a54-936a-eecc55847cab | -16.10036 | -51.97739 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2e46d58d-8706-390e-96df-4a0204938efa | -16.09136 | -51.97879 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 034336f3-dbf1-39e8-8286-6ae6c8a550a9 | -16.08372 | -51.98961 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b3a86c1-4a23-305e-9060-aca6d867b653 | -16.12939 | -51.98581 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ae23e7ac-88fc-312e-a107-ddd418e68340 | -16.128 | -51.97631 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ba8b4c4-cfaa-3453-b983-3a1483861cc2 | -16.12317 | -52.00625 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5865d62f-2df4-3b86-a97c-3eeaa7a78222 | -16.10799 | -51.96646 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 567e5560-4d4b-36ef-b99a-3b8890a7abfd | -16.10663 | -51.95697 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e019a47c-4cb7-3476-a16a-9de09375b6d9 | -16.09899 | -51.9679 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 10b3d949-4d61-36f2-a360-ae2848df4463 | -16.09273 | -51.98826 | 2024-09-27 01:22:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3e82d33b-6b45-39a5-9a87-7b0f13eade21 | -8.17634 | -53.15228 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| caee942a-bc44-3b51-8f1a-5607da71547f | -8.13514 | -52.87048 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 00013edc-c269-3a1d-aa34-3e8f89365bd9 | -8.13369 | -52.86058 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 27ea4024-46c7-31ee-8ce7-aaaed2e0c835 | -8.12795 | -52.86768 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2967464a-ed05-3386-8973-a1a40a9c6fa8 | -8.78957 | -52.04203 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d63abf6d-161c-3b9e-8f6f-e13f16ddc238 | -8.70844 | -51.98316 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cec06cd2-5a36-30a1-bc7f-f8f69116e269 | -8.69876 | -51.98462 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 14ded1eb-474e-3add-abaf-c59021053ddd | -9.72338 | -53.20098 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 743974e5-5acf-3dfc-bbed-4e9e1695fc33 | -9.66846 | -53.5274 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49bdd12b-0cd7-3759-9a53-9b8358fa1906 | -9.61354 | -53.27129 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 75fce5f5-8842-3730-97f1-438bfe2c28df | -9.55945 | -53.40847 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2471421a-ceaa-368c-a482-5543c9258276 | -9.55813 | -53.39922 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README24.md)
