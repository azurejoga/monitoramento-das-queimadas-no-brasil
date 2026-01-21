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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8dbef58-0bf0-3bea-bf26-9e099b612551 | 2.68111 | -60.08386 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e26f2cff-06ad-336b-8a49-9debfe3eb992 | 2.9182 | -60.94609 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a506f843-3ee0-3813-a54d-5fc22b6adcd8 | 2.69535 | -60.09967 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 568dc662-15cd-3a36-a286-2df25a939396 | 3.3404 | -60.07145 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c200b45-f69a-34cd-bad0-3fd6b22913e8 | 2.10455 | -61.53516 | 2026-01-21 05:10:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 639ded3a-da67-32bf-96a8-619db6f457d3 | 2.10028 | -61.53592 | 2026-01-21 05:10:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e794e5-5133-37b9-a2e0-383dda414e7a | 2.92238 | -60.94547 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb17048a-5fe0-38bc-a0ea-9215b04a079c | 3.34922 | -60.04929 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b709389f-d239-37f2-af0a-07f1bb4101e7 | 2.92181 | -60.94167 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11860e7d-6059-30c8-80e4-906d0adc70ba | -4.10006 | -47.30252 | 2026-01-21 05:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0334e55-2023-3172-a655-3eefc4981ff6 | 1.0204 | -60.54763 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24de6064-3dc4-349d-be18-e71ba870a157 | 3.34526 | -60.04988 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd781dfc-2cbd-38ed-994c-17d206f8689c | 3.16702 | -60.38475 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 798100e0-2c22-3c48-8236-9a0bd4b1c8e8 | 2.56282 | -60.38346 | 2026-01-21 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40b9e9d7-03b3-3510-b594-6e1271cc889d | 2.68129 | -60.08649 | 2026-01-21 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 982ac7c9-cbc1-373e-b198-04dc06ba7d9f | 2.91802 | -60.95308 | 2026-01-21 05:10:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b2b10e-57d8-3254-952f-3f53043b7bcc | 2.54638 | -60.57264 | 2026-01-21 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc569cb-3eb0-3ea9-be9c-2082cdd702f2 | 1.14048 | -60.5254 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a8e0af7-c6d0-3cba-be2e-43c5e9e37f95 | 1.13969 | -60.52032 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 356ecc8c-9cbd-354e-b84d-84415a97e21c | 1.13257 | -60.52665 | 2026-01-21 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9074cd30-f6a4-3636-9ac0-0531bd4db22b | 2.54584 | -60.56907 | 2026-01-21 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a091956c-db33-3208-b888-20d7fd2d1ca4 | -15.9737 | -56.27732 | 2026-01-21 05:14:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a6b6d57f-0c6d-3dfe-885f-b55d10956b49 | -15.35187 | -57.88747 | 2026-01-21 05:14:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6129219b-a924-3291-85ee-3df0f9df31bc | -16.07039 | -56.59137 | 2026-01-21 05:14:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc386747-4483-31d0-96c2-83833c1aa12a | -15.97067 | -56.27233 | 2026-01-21 05:14:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 36f2a629-a7ae-33a6-a755-ec8e03b5e68f | -15.97432 | -56.2729 | 2026-01-21 05:14:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4106c22a-41ff-3871-a3dc-5c578c5b7452 | -16.17143 | -57.95073 | 2026-01-21 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ecd2f6fe-e0f5-36ba-a8be-37bb0323108f | -16.07101 | -56.58712 | 2026-01-21 05:14:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a81aab1e-d339-3d38-a061-1b1e9a015921 | -15.02032 | -57.85892 | 2026-01-21 05:14:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a5e6cd0-0a0f-30db-aff8-bd6e672b8e6a | -20.36111 | -57.89807 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6a678d62-e973-32a0-a7ab-07051aa1d16b | -19.43072 | -57.21366 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 668354b9-f9c3-353c-bf43-fd9f490ff681 | -18.59762 | -55.94668 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 81e1f10f-fc16-3a4c-8bc7-6c7b87bb5506 | -19.42328 | -57.29328 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2b84f9ad-6090-395c-a98c-831d2c61f333 | -18.82142 | -51.61764 | 2026-01-21 05:16:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c655e627-7122-3256-8e1f-931fb7878b5a | -19.65982 | -56.95619 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 62c0ec8d-3b8e-31f0-8e82-207ce1acbb1c | -19.39019 | -57.2658 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c5cbb380-d60c-3b1e-ac7d-5858c8bf2ca3 | -19.21335 | -53.43793 | 2026-01-21 05:16:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac21fed6-9d39-38b9-88a7-11978ae7e48b | -19.44876 | -57.24345 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b768985d-7997-3610-a897-ee7117f7688b | -19.67288 | -56.88794 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4cea3d82-587b-3d77-97dc-aadefcc7ad37 | -19.4372 | -57.27307 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b057c39a-94a8-3e0b-8e69-3c511dfa0e63 | -23.6042 | -48.26612 | 2026-01-21 05:16:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3cd10cad-b720-3d7c-9e4f-cb2c642460e8 | -19.44098 | -57.21975 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a589887b-439c-31a1-8edd-f3a1b4dc13a2 | -19.66918 | -56.88737 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1158a38e-5fba-3b21-99b9-97dd00bdce28 | -19.44628 | -57.26103 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a9200e5f-0309-34bd-bf0a-4870a54eefa9 | -19.44081 | -57.27363 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3c733731-39f1-3b8f-b21b-1c694ac22956 | -20.33086 | -57.91224 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dbd12336-de58-3fcb-b2cf-c79a6d4d8d88 | -19.43434 | -57.21421 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e577d451-5f97-3616-be09-ccacb91a8b1f | -20.31849 | -57.89731 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7f6c1cff-05c4-3123-8001-d4c0e662c70d | -19.42709 | -57.2131 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0c7737ee-2a2f-34ad-b00d-1bf28d2b44ad | -18.81668 | -51.61369 | 2026-01-21 05:16:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5360abe7-972e-395e-8e81-e8b7ffdb8d75 | -18.82177 | -51.61444 | 2026-01-21 05:16:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec49ea5f-aae5-34f2-8e9d-4d071581c94b | -20.34747 | -57.89757 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 66a8969b-b125-3540-aa11-f862cd4f4cf2 | -19.4269 | -57.29384 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 29e53475-69c9-3d9c-bb2a-5fda11f6ca50 | -21.19645 | -56.93115 | 2026-01-21 05:16:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a575f2-acba-3ca4-afb5-410625a0cb7c | -19.42267 | -57.29765 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3ac3035d-e9f3-3bb6-8114-7f35b12877f6 | -19.44637 | -57.23409 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9c1c1480-ef0c-3c00-bdca-05cc47eda50e | -20.34807 | -57.89334 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 847c859e-8ced-37f1-9e1d-1b12730c1888 | -19.43235 | -57.28127 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 69545187-603e-36ac-a40c-2cb900697865 | -19.21282 | -53.44258 | 2026-01-21 05:16:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 498972ef-be95-39c5-870e-2353d9ef0a81 | -19.38898 | -57.27455 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 491d9301-b78e-3561-9039-19516880b654 | -19.64326 | -56.93966 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| df6b637d-a2f1-3133-8d71-b8d8f7ac2722 | -19.42751 | -57.28947 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0e01ab9a-dc2f-3307-be43-07b45cde660d | -19.67225 | -56.89254 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ccd48c20-42a9-379e-8d2d-96634b80e614 | -19.43797 | -57.21478 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3a199ad2-5866-3b3c-b444-b64f7e68737e | -20.31909 | -57.89308 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 11ed25bb-7c2b-3415-8f36-a6be526c98c9 | -19.4469 | -57.25664 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d1b80e3d-1d88-324a-a747-40df086e71df | -19.44143 | -57.26925 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 757aca65-f996-3f36-b93f-9ad7325c1610 | -20.34452 | -57.89277 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c62fe547-933c-354f-9a77-46c7e2822127 | -20.34098 | -57.89221 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5b49467e-1c4a-3893-bf18-83b6e5cd475a | -23.60467 | -48.25982 | 2026-01-21 05:16:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d53f20b2-0720-3859-bcd5-41f5578c4011 | -19.44567 | -57.26542 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 16f95fd7-f50d-344f-86a3-eb6d0926fcc5 | -19.17168 | -57.54424 | 2026-01-21 05:16:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e385c041-bd9e-340c-bce3-db31fa052102 | -19.66856 | -56.89198 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22c9f3f7-e394-3321-b377-83520cce1655 | -19.10708 | -57.61596 | 2026-01-21 05:16:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| acd87316-1c2c-391a-ba06-a33987b72f08 | -22.01936 | -56.34557 | 2026-01-21 05:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 479de64a-4363-36d5-96d7-67a0c0192af8 | -20.729 | -55.15763 | 2026-01-21 05:16:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2585a3-6415-3e48-9b9d-5ec8432bbdd5 | -20.33146 | -57.90802 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7dc452f9-7c85-35ee-afc6-0b6f7ec7b0c5 | -19.44399 | -57.22472 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5d978a5b-c9be-356b-8372-8b13d7d71f7b | -19.44814 | -57.24784 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c3663201-7910-34ed-b8b6-861f030aa685 | -19.43658 | -57.27745 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 97fe1cda-e61b-3463-8571-193f3b69c1d7 | -19.41845 | -57.30147 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 54e90cce-a76c-3849-a248-b5bd5e875efa | -20.72438 | -55.16096 | 2026-01-21 05:16:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06dd4294-19e7-3c5a-8cf9-fc4bdd5c7398 | -19.66413 | -56.95218 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3943d42e-1d2c-3e0a-bacd-4d7c1945e876 | -23.60279 | -48.26124 | 2026-01-21 05:16:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e26d5882-bb3a-3a9f-b77d-fe0b74435484 | -19.4402 | -57.27802 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 56993f0d-1a2d-3d3d-85e3-658c41eaf13d | -19.42812 | -57.28509 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9403d58c-9075-39fd-9ae7-fcc5e208a3e6 | -20.32618 | -57.8942 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d79c6097-ca99-362a-a86b-197a60991bdf | -20.72852 | -55.16156 | 2026-01-21 05:16:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e786529a-7558-391b-9fc3-9de26a3bc9a7 | -19.43174 | -57.28565 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ef818b65-e710-3fd4-a981-e8391ca75512 | -20.9059 | -56.38757 | 2026-01-21 05:16:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7650598d-df74-3287-a443-5b30501c78b5 | -19.21206 | -53.44171 | 2026-01-21 05:16:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f591a4ba-310c-35e2-b9b0-71b58a3ac8a8 | -19.44699 | -57.22968 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 029d0cf2-722e-3e97-8967-6af005e5ad79 | -19.41784 | -57.30584 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b7f28341-84d9-3b4f-949a-304ffcbe14d7 | -19.66843 | -56.94817 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| acbb4f1d-4b93-3497-ba68-9b858feb9323 | -19.43597 | -57.28183 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 05d9d338-a8f7-30c2-8019-2b14f52570e0 | -20.34037 | -57.89645 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1b11b728-f4e5-3864-ab86-5cf1ddc1a194 | -19.38838 | -57.27893 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 55bfb044-cd3b-310e-a7aa-660bd6238aca | -23.60236 | -48.26767 | 2026-01-21 05:16:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 52289a91-55b6-34b3-baa8-47fdfb507e1c | -19.67595 | -56.89311 | 2026-01-21 05:16:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d8f7ba47-95af-38c9-9d39-4605572f72ec | -20.32263 | -57.89364 | 2026-01-21 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README6.md)
