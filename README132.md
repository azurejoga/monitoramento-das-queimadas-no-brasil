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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c92bece-9255-3db4-b521-fc83a9d5a2b0 | -14.75347 | -45.77044 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d0f20df-d955-3e9f-9ea1-6494144e1cb5 | -14.70463 | -48.13279 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aaec636-b0e6-35df-95cc-56b6d95e5a98 | -14.43718 | -46.36468 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6c548af-62ec-3c80-b782-dd8941946c07 | -14.0211 | -46.32383 | 2025-10-01 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 953066a4-6e49-358f-90db-a9b18c88cc00 | -14.43832 | -46.35329 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a119f408-7d28-3cd3-b118-9177b7ebf352 | -14.06008 | -45.04779 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c4412973-50cb-35ca-8e1a-2ee0372597d9 | -13.78763 | -51.23231 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 231558a7-1079-32eb-aa38-d2ae009ee942 | -13.97265 | -44.88435 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a226e428-09f4-3920-9d33-42216c468f1e | -15.28084 | -56.78688 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 277f08f4-e77b-38a2-9146-ffdb083c5303 | -14.90006 | -48.1166 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d3d4419a-2893-3afa-ab45-10ada6de52f9 | -14.70461 | -48.21561 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1fbb19f-07f7-3fb9-8707-0dfe26588b9d | -14.79912 | -45.80289 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6fac40e-00f7-3cdc-9208-c5b68875ab86 | -15.60487 | -46.91301 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9de4c31-3331-3226-9a40-5d77a37e0f1f | -16.05666 | -51.013 | 2025-10-01 05:12:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c59d127-41cd-3475-96b3-4b34809427d3 | -15.33613 | -56.63205 | 2025-10-01 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f5bd49b-fb02-3547-a56b-15e861e80ef3 | -13.75893 | -47.93443 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc620115-99af-3a05-b9d8-6cb7589bc70b | -14.7237 | -48.15084 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6be039c8-4629-39cb-b4de-108da5e6ce35 | -14.78535 | -45.80166 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 77199a33-756c-30bf-a97c-4ab34de43c28 | -14.71764 | -48.15105 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82fb49d9-6776-3879-943f-5db00d513e2c | -15.41965 | -47.05857 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a17e182b-83d8-3cd5-94a0-1c8aeb1900d1 | -15.33904 | -56.95715 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2229c5ed-743b-32f4-8edb-e6425d7b8eee | -14.60396 | -48.22472 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45a27574-da9a-33a9-813b-dcbe6f1bcb59 | -16.40561 | -47.05363 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e33149f-2732-30a7-b5b4-5e8ed89b7635 | -13.73274 | -48.68961 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79657285-001d-39d3-a488-3eb96114adc2 | -14.53056 | -53.11779 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a968f66b-7aae-316e-834e-e9844257a44c | -13.78043 | -48.0132 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8640686-d871-32b3-8139-a0575af783b6 | -15.94552 | -48.11694 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aebdcb69-db9c-30a0-9028-58dcd603f8b3 | -14.51047 | -48.48557 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9e07024-a50e-31e1-9e5c-809a9ff867d6 | -14.95713 | -46.88207 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb907e3b-1325-3838-ab47-913a8ba778dc | -13.81823 | -47.50211 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 239d62dc-1978-3d0b-9072-e2d569fe66a1 | -15.55174 | -48.18507 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed45d00d-5433-3b0d-8440-56a25912e551 | -14.9827 | -50.76801 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e095089a-ee47-3e17-b3c2-cfb8ebb9796c | -14.91445 | -51.67585 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 848ab705-245c-3d62-b1cd-f7509b63e3bc | -17.38757 | -47.14991 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8b6e8e5-2ef2-376d-beae-0535c6a0ff4a | -15.3064 | -56.78917 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 451e0169-cf23-357f-a0cc-b1a8a26151c3 | -14.68992 | -48.12787 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 666fee5e-2665-3b94-8e7f-f6e52f9d71ac | -13.77003 | -47.96829 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f48f0e30-ea25-3390-af0c-ca72e19447c5 | -14.95299 | -47.51199 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc412176-b0ff-33df-93d5-153458cded37 | -14.87449 | -48.32491 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f71202c-88bd-3829-8598-92a1b7236664 | -13.76116 | -47.94088 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94e7cfe8-454e-301d-9229-6ee8b8cc1dc2 | -15.16938 | -52.8108 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 745a2aab-d9e4-32f2-a916-50cfe4d2b1ca | -15.98952 | -59.51942 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e003ed03-ebda-310e-9ee0-fbe114767d1f | -14.02883 | -53.88161 | 2025-10-01 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 195e17dd-e160-373b-bba1-c5b51a3439a5 | -14.90381 | -47.21272 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 915581f2-13df-3e79-a35b-e407c70cd2b9 | -15.24209 | -48.73613 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2cad011-a072-33e7-b30e-c32d2ed5adc5 | -14.68054 | -48.23799 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6e76d30-3538-31b5-83bb-413f930d48e7 | -14.71853 | -48.14285 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48bf2a7b-a00e-3700-b719-cca578801912 | -14.59813 | -48.22316 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d064567-58a0-3b51-9d42-78c53a4f7b92 | -14.34687 | -45.92036 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4200b2a3-b9dd-353a-a341-7a9f7c1b2bd1 | -14.59181 | -48.22606 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 19f10605-42ce-33cc-b445-a17e6fb988ce | -15.8398 | -56.39021 | 2025-10-01 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a194b83-c5f7-3123-b10f-3ea8a06b8617 | -15.41241 | -47.05574 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a892b60-8013-39c5-92b1-4fbfa9e5d01f | -15.14886 | -48.01724 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 705c9173-2f25-3824-972c-808df025197f | -17.85974 | -47.14841 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c19be28-ea86-3238-b0ea-7008c38e723c | -14.90148 | -48.12706 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11bf2d07-6384-3a6d-b6a1-410901c29350 | -14.98233 | -50.77101 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 455ce3ca-62da-3335-b9a4-878c25fe0e5f | -15.80753 | -59.51086 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70a30a64-2a93-3dc1-a20f-4e09cb2fb922 | -15.28203 | -56.77882 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c522a31f-aa43-3dec-a70c-2d85975d6a37 | -16.07773 | -51.04581 | 2025-10-01 05:12:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fef6b20f-5730-347a-bec5-90fa98dfa287 | -15.47694 | -45.87306 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbe784a0-1b08-36e9-8398-802c2b209d82 | -17.4121 | -47.16912 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 447da3c5-28ab-30b6-94b0-72372a809602 | -16.39327 | -47.04525 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef159351-b1c8-3787-ad06-df97e2d9bdc8 | -15.94557 | -48.12783 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 391433ee-18c3-3ab4-8440-6bd227107b3b | -15.6056 | -46.9057 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88a89274-98df-380d-b575-9dbe4570f614 | -14.19096 | -46.1183 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a221d83-a572-3302-829a-5d6d16f29ac4 | -13.9183 | -48.1015 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8589d58e-68f7-3e97-9a49-2e720e3ee2ae | -15.299 | -56.78512 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b4cc178-0eff-3134-8366-8588f650310a | -17.86125 | -47.14221 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c14f34-855e-3a0c-87ae-17abe482a2e3 | -13.66671 | -48.08164 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 111c5749-2a8f-3844-96b7-2bd5f610b921 | -15.26943 | -51.48112 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aac88070-0420-33b1-87a7-54d06f6d362c | -13.77596 | -47.96928 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eea05359-3439-39ec-98a1-9ab46684f82d | -13.75941 | -47.93005 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 081a6138-4af9-3c4f-9fb6-526d4f9042ec | -14.631 | -46.98023 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01bcf081-bea3-349d-a597-d08085d10908 | -14.79223 | -45.80233 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d9a700a7-d297-32e1-a45d-7b2b06446678 | -16.01612 | -50.87925 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d658ba2b-cb7b-357f-8eb6-d8c3f196f12e | -13.91342 | -48.09164 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b21198f0-4f57-33ab-9ae1-52089607221f | -14.04977 | -47.98502 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1356900e-1ce4-3c4f-9d7f-eb076309030e | -14.09106 | -49.74737 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5914a176-1157-38df-ba49-3c2a86dd0baa | -13.94478 | -48.11568 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd6fe53c-2873-3d26-9e80-116fc21e0934 | -17.89924 | -57.6264 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 84c93f5a-1391-396e-995a-9c0d90a842ab | -17.89562 | -57.57751 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 1c798f58-90a0-3dab-9a81-37f3d81aecb2 | -13.97622 | -44.91999 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 559d5a6c-b0b0-37a9-9b86-6beb3e1727d7 | -14.68249 | -48.11475 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64cb4b94-0e41-3699-a24f-b889d65ef1f6 | -13.98491 | -44.90609 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7eef6331-c65d-37df-a3fb-54e16fed6b54 | -15.94505 | -48.12128 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f4ea5108-c642-3dfb-8e22-513f14b524fe | -14.36454 | -47.1452 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7002cbff-7ba9-3abe-aba0-f7ecfc2b2d9e | -14.67378 | -45.30085 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 556eac18-012d-35d8-9581-ba7e32c1c81c | -13.67502 | -48.06111 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bffa61f-ad46-3f0f-82e4-8899c448bf5f | -15.41876 | -47.05714 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9490612f-db84-3306-84ef-e37aaae122ec | -14.88875 | -48.13285 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9065cbe4-5b0a-3271-8252-73dd9db8a0bd | -13.81807 | -47.50411 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07eaa72c-e285-3c56-8ea8-66ead24103d2 | -15.61217 | -46.90579 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb317933-5a3f-368b-aa63-75a141941cfc | -17.86771 | -47.14402 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a16d01b-9f95-36ad-b969-cce48ae0f2bc | -18.80674 | -47.55545 | 2025-10-01 05:12:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8be245ff-431a-31c5-ad34-97de51934107 | -18.70616 | -49.17041 | 2025-10-01 05:12:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc67be59-0b53-3e8a-b0e3-b8b4e7a28ce4 | -14.8942 | -48.11477 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| da4d40b1-2528-30d4-88b4-9a1e41e8cae8 | -17.89966 | -57.57406 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 1a73e9c2-06f0-379d-a70d-357ac4c81663 | -14.89827 | -48.13253 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d08e102-161a-3a98-96db-cbced7cbac1e | -12.92494 | -54.73004 | 2025-10-01 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6df56eb2-d2c8-3c11-8cc0-4fe3d271ee83 | -14.0399 | -47.96525 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README133.md)
